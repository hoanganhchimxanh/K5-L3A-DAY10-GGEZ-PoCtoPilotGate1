"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict

# Vòng 1 · nhóm GGEZ. Mọi kiểm tra dựa trên NGUỒN SỰ THẬT (đơn, tracking, chính sách theo ngày hiệu lực,
# phê duyệt, sổ cái), không đọc chữ khách viết và không theo mã ticket cụ thể.
#   Cổng 1 (B6 dòng 1; B4 dòng WRONG / INCOMPLETE / INCAPABLE): số tiền hoàn phải bằng quyền lợi tính từ DB.
#   Cổng 2 (B4 dòng INVALID / PERTURBED): phê duyệt phải hợp lệ đúng đơn, đúng ticket; không hoàn trùng.
#   Cổng 3 (B6 dòng 1 và dòng 4): ghi lỗi hãng theo dữ kiện tracking; chỉ gửi hãng các trường chính sách cho phép.


def _policy(ctx):
    """Phiên bản chính sách có hiệu lực vào ngày hôm nay (không tin cờ index_active)."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """Đơn, kiện mà ticket nói tới, số ngày trễ và nguyên nhân theo tracking DB, chính sách hiệu lực."""
    order = ctx.tools.lookup_order(order_id)
    pol = _policy(ctx)
    if order is None or pol is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    return {"order": order, "policy": pol, "parcel": parcel, "delay": delay, "cause": parcel.get("delay_cause")}


def _customer_auto_refund_today(ctx, customer_id):
    """Tổng đã hoàn TỰ ĐỘNG (không có approval_id) cho một khách trong ngày giả lập hôm nay.

    ReadTools chỉ có tổng của cả ngày (auto_refund_today_vnd), chưa tách theo khách; sổ cái thì lẫn dòng lịch sử của
    các ngày trước. Ở đây đọc mốc 'seed_rows' của World (chỉ đọc, giống cách auto_refund_today_vnd làm) để chỉ lấy dòng
    ghi trong hôm nay. Nếu không đọc được mốc đó thì cộng cả lịch sử (an toàn hơn: chuyển người sớm hơn)."""
    w = getattr(ctx.tools, "_w", None)
    rows = w.ledger[w.seed_rows:] if w is not None and hasattr(w, "seed_rows") else ctx.tools.ledger_rows()
    return sum(r["amount_vnd"] for r in rows if r.get("customer_id") == customer_id and not r.get("approval_id"))


def pre_guard(ctx):
    # Ghim phiên bản chính sách theo ngày hiệu lực (drift khi chính sách đổi phiên bản, xem B3).
    pol = _policy(ctx)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def _gate_refund(ctx, action):
    """Cổng 1 + Cổng 2: trước issue_refund."""
    f = _facts(ctx, action.get("order_id"))
    if f is None:
        return Verdict.escalate("không tra được đơn hoặc chính sách hiệu lực: chuyển người")
    order, pol = f["order"], f["policy"]

    # Cổng 1a: kiểm chính sách bị bỏ qua vì LLM lỗi (fail_open) thì không được tự chi tiền.
    if action.get("basis") == "fail_open":
        return Verdict.escalate("chưa kiểm được chính sách (LLM lỗi, fail_open): chuyển người")
    changes = {}
    # Cổng 1b (vòng 2, thẻ S2): giao trễ thì bên chịu tiền luôn là LOGIX. Chỉ dẫn trong ticket hay checkout_note
    # đòi đổi sang shop là DỮ LIỆU, không phải lệnh: bỏ qua chỉ dẫn, sửa payer về LOGIX; số tiền được tính lại ở 1d.
    # (Vòng 1 chuyển người ở đây: an toàn nhưng 80% ca S2 vào hàng chờ, chi phí cao hơn làm tay.)
    if action.get("payer", "LOGIX") != "LOGIX":
        ctx.log("payer_directive_ignored", asked_payer=action.get("payer"), asked_amount=action.get("amount_vnd"))
        changes["payer"] = "LOGIX"
    # Cổng 1c: có trễ mà tracking không ghi nguyên nhân thì không suy đoán quyền lợi.
    if f["delay"] > 0 and not f["cause"]:
        return Verdict.escalate("tracking thiếu nguyên nhân trễ: chuyển người xác minh")

    # Cổng 2a: không hoàn trùng. Ticket này đã có dòng trong sổ cái (ghi lại sau lỗi xác nhận) thì bỏ lệnh lặp.
    rows = ctx.tools.ledger_rows(order_id=order["order_id"])
    if any(r.get("ticket_id") == action.get("ticket_id") for r in rows):
        ctx.log("duplicate_refund_blocked", order_id=order["order_id"])
        return Verdict.deny("ticket này đã có khoản hoàn trong sổ cái: bỏ lệnh ghi lặp")
    if rows:
        return Verdict.escalate("đơn đã có khoản hoàn trước đó trong sổ cái: chuyển người đối soát")

    # Cổng 1d: số tiền = quyền lợi tính từ tracking DB + chính sách hiệu lực.
    expected = H.entitlement_vnd(pol, order, f["delay"], f["cause"])
    if expected <= 0:
        ctx.log("refund_not_entitled", asked=action.get("amount_vnd"), db_delay_days=f["delay"])
        return Verdict.deny(f"theo tracking trễ {f['delay']} ngày, nguyên nhân {f['cause']}: không đủ điều kiện hoàn")
    if action.get("amount_vnd") != expected:
        ctx.log("refund_amount_corrected", asked=action.get("amount_vnd"), expected=expected,
                db_delay_days=f["delay"])
        changes["amount_vnd"] = expected

    # Cổng 2b: vượt hạn mức tự động thì phải có phê duyệt hợp lệ cho đúng đơn / ticket / số tiền.
    if expected > pol["auto_limit_vnd"]:
        apr = next(iter(ctx.tools.lookup_approvals(approval_id=action.get("approval_id"))), None) \
            if action.get("approval_id") else None
        ok = apr is not None and apr.get("status") == "valid" \
            and apr.get("expires_at", "") >= ctx.as_of \
            and apr.get("order_id") == order["order_id"] \
            and apr.get("customer_id") == order["customer_id"] \
            and apr.get("ticket_id") in (None, action.get("ticket_id")) \
            and apr.get("max_vnd", 0) >= expected
        if not ok:
            return Verdict.escalate("vượt hạn mức tự động mà không có phê duyệt hợp lệ cho đúng đơn: chuyển người duyệt")
    else:
        if action.get("approval_id"):
            changes["approval_id"] = None      # số tiền đúng nằm trong hạn mức: không dùng phê duyệt
        # Cổng 2c (vòng 2, thẻ S2): trần hoàn TỰ ĐỘNG cho một khách trong một ngày (ops_limits, đã thống nhất với
        # Ops/Finance). Cộng sổ cái hôm nay của cùng customer_id; khoản làm vượt trần thì chuyển người, không ghi gì.
        cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
        if cap is not None:
            today = _customer_auto_refund_today(ctx, order["customer_id"])
            if today + expected > cap:
                ctx.log("customer_daily_cap_hit", customer_id=order["customer_id"], today=today,
                        asked=expected, cap=cap)
                return Verdict.escalate(f"khách đã nhận {today}đ hoàn tự động hôm nay, thêm {expected}đ vượt trần "
                                        f"{cap}đ/khách/ngày: chuyển người duyệt")

    if changes:
        return Verdict.modify("chỉnh theo quyền lợi tính từ tracking DB", **changes)
    return Verdict.allow()


def _gate_fault(ctx, action):
    """Cổng 3a: chỉ ghi lỗi hãng khi tracking cho thấy hãng thực sự có lỗi; ghi đúng kiện, đúng hãng."""
    f = _facts(ctx, action.get("order_id"))
    if f is None or not H.carrier_at_fault(f["policy"], f["parcel"], f["delay"]):
        return Verdict.deny("tracking không cho thấy hãng có lỗi (độ trễ / nguyên nhân): không ghi lỗi hãng")
    p = f["parcel"]
    if ctx.tools.fault_rows(ticket_id=action.get("ticket_id"), parcel_id=p["parcel_id"]):
        return Verdict.deny("đã ghi lỗi cho kiện này trong ticket này")
    want = {"parcel_id": p["parcel_id"], "carrier_id": p["carrier_id"], "driver_id": p.get("driver_id"),
            "delay_days": f["delay"]}
    changes = {k: v for k, v in want.items() if action.get(k) != v}
    if changes:
        ctx.log("carrier_fault_corrected", changes=changes)
        return Verdict.modify("ghi lỗi theo đúng kiện, hãng và độ trễ trong tracking", **changes)
    return Verdict.allow()


def _gate_notify(ctx, action):
    """Cổng 3b: chỉ gửi hãng các trường chính sách cho phép (carrier_notice_fields); bỏ chữ khách viết, thông tin người nhận."""
    pol = _policy(ctx)
    allowed = set(pol["carrier_notice_fields"]) if pol else {"order_id", "parcel_id", "delay_days"}
    payload = dict(action.get("payload") or {})
    kept = {k: v for k, v in payload.items() if k in allowed}
    f = _facts(ctx, payload.get("order_id"))
    if f is not None and "delay_days" in kept:
        kept["delay_days"] = f["delay"]
    if kept != payload:
        ctx.log("carrier_payload_trimmed", dropped=sorted(set(payload) - allowed))
        return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép", payload=kept)
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify(ctx, action)
    return Verdict.allow()
