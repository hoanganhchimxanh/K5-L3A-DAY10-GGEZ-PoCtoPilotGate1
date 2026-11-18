# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Bảo đảm yêu cầu hoàn tiền giao trễ được giải quyết trọn vẹn và an toàn: khách nhận đúng quyền lợi theo chính sách hiện hành, khoản hoàn được ghi đúng thẩm quyền và có xét lịch sử hoàn tiền, lời xác nhận với khách khớp sổ cái, đồng thời không làm lộ dữ liệu khách hàng.

Căn cứ: [PRD v1.1 §3 — Định nghĩa chạy đúng](../docs/PRD_v1.1.md#3-định-nghĩa-chạy-đúng), với các yêu cầu về đúng số tiền, không vượt quyền phê duyệt, lời trả lời khớp sổ cái và không lộ thông tin bí mật.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Đối soát được từng khoản hoàn tiền và khoản ghi lỗi cho hãng với đúng đơn hàng, kiện hàng, bên chịu tiền, chính sách và phê duyệt liên quan; không phải dò lại thủ công vì hoàn trùng, hoàn sai số tiền hoặc quy trách nhiệm sai cho hãng/shop. Dù không trực tiếp dùng trợ lý, chị cần sổ cái và bằng chứng truy vết nhất quán để giải thích được các chênh lệch và chốt đối soát hằng tuần.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Tiếp nhận và xử lý được các ca cần người duyệt, đặc biệt ca hoàn tiền vượt hạn mức, trong năng lực thực tế của ca trực, tránh tồn đọng quá thời hạn. Mỗi ca chuyển sang cần có lý do, dữ kiện đơn hàng/tracking, chính sách áp dụng và số tiền đề xuất để chị kiểm tra và quyết định đúng thẩm quyền mà không phải làm lại toàn bộ từ đầu; trợ lý không được tự coi việc chuyển ca là đã được chị phê duyệt.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng** (`file_carrier_fault`): agent quyết định có ghi lỗi cho hãng vận chuyển hay không, và ghi cho kiện nào, hãng nào | Hành vi **ghi lỗi hãng và thông báo cho hãng** (`file_carrier_fault` + `notify_carrier`) trong production: trợ lý có đang tích luỹ lỗi vượt trần cho một hãng mỗi ngày không, và thông báo có chứa trường dữ liệu đúng quy định không |
| **Thước đo** (một câu, có đơn vị) | **Tỉ lệ ghi lỗi oan**: số dòng lỗi hãng ghi sai (sai hãng, sai kiện, hoặc ca đáng ra không được ghi lỗi) trên 100 dòng lỗi hãng agent đã ghi (đơn vị: dòng sai / 100 dòng ghi). Số phụ đi kèm: **tỉ lệ bỏ sót** (lỗi đáng ghi mà agent không ghi, trên 100 lỗi đáng ghi) | **(1) Tỉ lệ ngày có hãng bị ghi lỗi vượt trần tự động** (đơn vị: % ngày vận hành có ít nhất 1 hãng bị ghi quá 2 lỗi tự động). **(2) Tỉ lệ thông báo hãng thiếu trường bắt buộc** (`order_id`, `parcel_id`, `district`, `delay_days`) theo chính sách hiện hành (đơn vị: % sự kiện `notify_carrier` thiếu ≥ 1 trường). Không cần nhãn đúng/sai: hai chỉ số này đo trực tiếp từ log hành động và so với quy tắc cứng trong `ops_limits` và `carrier_notice_fields` |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Dòng `fault_rows` (`carrier_id`, `parcel_id`) và sự kiện `tool: file_carrier_fault` trong `runs/<mã lần chạy>/traces/<ticket>@<seed>.json`; nhãn là `label.faults` trong `data/tickets.jsonl`, đối chiếu với `delay_cause` của kiện trong `data/world.json` → `orders[].parcels` và `fault_causes` của chính sách đang hiệu lực. Bộ nền có 22 ticket × 5 seed = 110 lần chạy. Nhãn do người soạn lab gán; ở pilot thật, nhãn đến từ đối soát hằng tuần của chị Oanh (kế toán) với hãng, và từ khiếu nại của hãng | **(1)** Log sự kiện `file_carrier_fault` trong production, nhóm theo `carrier_id` và ngày (`date`). Đếm số lần ghi lỗi tự động (không có người duyệt) mỗi hãng mỗi ngày; so với ngưỡng `max_auto_strikes_per_carrier_per_day = 2` trong `ops_limits`. Không cần nhãn. **(2)** Log sự kiện `notify_carrier`; kiểm từng bản ghi có đủ bốn trường `order_id`, `parcel_id`, `district`, `delay_days` theo `carrier_notice_fields` của chính sách đang hiệu lực (`REFUND-v3`). Không cần nhãn |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | So khớp chính xác cặp (`carrier_id`, `parcel_id`). **Ghi oan** = số dòng trong `fault_rows` không khớp cặp nào trong `label.faults` của ticket đó; một dòng ghi lặp cùng cặp cũng tính là oan. **Tỉ lệ ghi oan** = ghi oan / tổng số dòng `fault_rows` × 100. **Bỏ sót** = số cặp trong `label.faults` không có trong `fault_rows`, chỉ đếm ở lần chạy có `status` khác `escalated`. **Tỉ lệ bỏ sót** = bỏ sót / tổng số cặp trong nhãn của các lần chạy đó × 100. Lần chạy bị chuyển người, hoặc bị cổng chặn trước bước ghi, không vào mẫu số mà được đếm riêng thành "số lần không tới bước ghi lỗi". Mẫu số bằng 0 thì báo "không đủ dữ liệu", không báo 0% | **(1)** `strikes_today(carrier)` = đếm sự kiện `file_carrier_fault` có `approved_by = null` (tự động) trong cùng ngày cho cùng `carrier_id`. Nếu `strikes_today > 2` thì ngày đó tính là vi phạm. **Tỉ lệ ngày vi phạm** = số ngày có ít nhất 1 hãng vi phạm / tổng số ngày vận hành × 100. Ca không tới được bước ghi lỗi (đã escalate trước) không tính vào mẫu số. **(2)** Với mỗi sự kiện `notify_carrier`: kiểm tra `payload` có đủ 4 khoá bắt buộc; nếu thiếu ≥ 1 khoá thì đánh dấu `incomplete`. **Tỉ lệ thiếu trường** = số bản ghi `incomplete` / tổng bản ghi `notify_carrier` × 100. Mẫu số = 0 thì báo "chưa có thông báo nào" |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | **(1)** Cửa sổ: **cuộn 1 ngày** (reset lúc 00:00). Báo động ngay khi `strikes_today(carrier) = 2` (cảnh báo) và chặn/escalate khi `= 3` (tức thì, không chờ hết ngày). **(2)** Cửa sổ: **cuộn 1 giờ** (kiểm sau mỗi batch). Báo động khi `tỉ lệ thiếu trường > 0%` trong giờ gần nhất — ngưỡng bằng 0 vì thiếu trường bắt buộc là vi phạm hợp đồng với hãng ngay lập tức. Kênh: `alert_channel` trong `config/operating_gates.json` (người nhận: `NV-TUNG`) |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | (1) Không thấy chính dữ liệu tracking sai, ví dụ `delay_cause` bị ghi nhầm thành `CARRIER`: lúc đó nhãn cũng sai theo. (2) Đếm mọi dòng như nhau, không thấy mức hậu quả khác nhau: GHSH bị đình chỉ sau 3 lỗi trong 7 ngày, phạt 150.000đ mỗi lỗi; VNX tới 10 lỗi mới bị đình chỉ. (3) Không thấy lỗi tích luỹ trong ngày (trần 2 lỗi mỗi hãng mỗi ngày trong `ops_limits`). (4) Không thấy dữ liệu cá nhân gửi kèm ở bước `notify_carrier` | (1) Không phân biệt được lỗi ghi **đúng** với lỗi ghi **oan**: chỉ biết số lần ghi lỗi vượt trần, không biết lần thứ 3 có phải lỗi thật không. (2) Không thấy lỗi **tích luỹ 7 ngày** dẫn tới đình chỉ hãng (GHSH bị đình chỉ sau 3 lỗi/7 ngày, DNB cũng vậy); chỉ nhìn trong ngày. (3) Không thấy trường hợp `notify_carrier` **không được gửi** khi đáng ra phải gửi (bỏ sót thông báo hoàn toàn). (4) Không thấy nội dung sai (giá trị `delay_days` tính sai) dù đủ trường |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Chọn **(b)**

Giải thích một câu: Chênh lệch một lần chạy giữa X và Y chưa đủ để kết luận Y tốt hơn X có ý nghĩa thống kê, vì kết quả 1,0 của Y vẫn nằm trong khoảng tin cậy 95% [0,94; 1,0] của X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
