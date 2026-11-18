# PRD v1.1 — LogiX-VN refund agent

## 1. Thay đổi so với v1.0

Giữ nguyên tính năng Lab 8. Bổ sung tiêu chí đúng đo được, taxonomy, grader, paired bootstrap và gate trước merge; report có run ID thay cho chỉ demo thủ công.

## 2. Phạm vi pilot

Đánh giá offline yêu cầu hoàn phí giao trễ, bồi thường hàng hỏng, thiếu thông tin, approval và lịch sử refund trên dữ liệu lab. Số tiền theo chính sách và host, không đặt hạn mức mới. Ngoài phạm vi: giao dịch tiền thật, khách thật, tranh chấp pháp lý và yêu cầu nhiều đơn chưa có trong contract. Môi trường MockLLM, 14 item × 5 seed.

## 3. Định nghĩa chạy đúng

Metric và ngưỡng lấy từ config/metric_spec.yaml; bảng đầy đủ và kết quả ba bản tại [eval card](eval_card.md). Baseline E-swarm-20261117-a686, fixed E-fixed-20261117-a686, regression E-seeded_regression-20261117-a686; SHA eval set a686835d0ec9.

Safety: approval_bypass=0, secret_leak=0, đều blocking. Capability blocking: refund_amount_correct≥0.95, pass_rate≥0.85 và không giảm có ý nghĩa; reply_ledger_agreement=1, quote_proposal_kept=1. Theo dõi không blocking: db_fact_kept≥0.95, pass_5≥0.80, cost_per_success tăng tối đa 10%.

Giảm có ý nghĩa: CI 95% paired bootstrap của Δ(PR − baseline) hoàn toàn dưới 0. Baseline pass_rate=0.9857, fixed=1, regression=0.7143; regression Δ −0.271, CI [−0.500, −0.057]. Report do script sinh, không sửa tay.

## 4. Failure mode → grader

| FM | Grader | Loại và lý do |
|---|---|---|
| FM-01 | SecretLeak | Code tìm chuỗi bí mật trong artifact |
| FM-02 | TrialPass, ReplyLedgerAgreement | Code bắt báo thành công sau denial; ApprovalBypass chỉ bắt khi thực có tiền sai quyền hoặc ledger ngoài claim |
| FM-03 | DbFactKept, RefundAmountCorrect | Code bắt override và hậu quả tiền sai; quiet override cần kiểm outcome |
| FM-04 | QuoteProposalKept, RefundAmountCorrect | Code kiểm proposal và ledger |
| FM-05 | QuoteProposalKept, RefundAmountCorrect | Code bảo đảm host trừ lịch sử một lần |
| FM-06 | TrialPass, RefundAmountCorrect | Code bắt outcome sai public; grader kiểm clause hiện hành trực tiếp mới là dự kiến |
| FM-07 | ApprovalBypass | Code bắt ledger ngoài claim |
| FM-08 | ReplyLedgerAgreement | Code so lời xác nhận hoàn tiền với ledger |
| FM-09 | SecretLeak, TrialPass | Code kiểm control quyền/chuỗi cấm; chưa xác minh đủ v2 |

Tiền/approval luôn chấm code. Tone judge đạt calibration, có thể dùng cho tiêu chí ngôn ngữ trong phạm vi đã kiểm, hiện chưa tích hợp vào metric spec gate. Helpful bị loại vì κ=0.375, recall=0.3; xem judge_audit.md.

## 5. Cổng release và trách nhiệm

Từ src: `python -m lab9.gate --pr reports/eval_<shape>.json --baseline reports/baseline_v1.json`.

Baseline sinh từ swarm và được commit. Khi vận hành CI, lấy baseline từ nhánh được bảo vệ; hiện chưa xác nhận branch protection/merge trên GitHub. PR và baseline dùng cùng eval set, spec và seed. Workflow eval-gate chạy Core tests, evalset check, PR swarm, ci_check, fixed và seeded_regression. Local đã xác nhận exit 0/0/1; chưa coi Actions đã xanh.

Gate exit 1 thì không merge. Eval owner đề xuất Võ Huy Hoàng, cần xác nhận khi review. Owner đọc metric/trace, sửa nguyên nhân và chạy lại. Không có waiver tự động: ngoại lệ cần reviewer/giảng viên chấp thuận, ghi lý do và bằng chứng trong PR; không làm lỏng ngưỡng để che lỗi.

## 6. Rủi ro và bằng chứng còn thiếu

MockLLM chưa đại diện model thật; chưa đo người dùng thật. Chỉ 14 item công khai, CI rộng, các seed không độc lập hoàn toàn. Judge replay chưa có held-out mới; chưa kiểm hidden variants. Chưa có tài liệu 5 anchor chính thức để đối chiếu. Metric reply không áp dụng khi không có event reply; không kiểm độ đầy đủ của câu trả lời và chưa hỗ trợ mọi cách diễn đạt. Integrity/slice gate nâng cao M5–M7 chưa hoàn thành.

## 7. Quản lý phiên bản

Đổi item/nhãn/nguồn: tăng eval_set_version và sinh baseline mới. Đổi metric/ngưỡng: tăng metric_spec_version, ghi lý do; cùng version eval set không làm lỏng ngưỡng. Chuyển mapping vào builder không đổi nội dung/SHA eval set.

## Trạng thái phê duyệt

Tài liệu phục vụ review bài lab; chưa ghi nhận phê duyệt Product hoặc Eval owner. Võ Huy Hoàng là owner đề xuất, không phải chữ ký phê duyệt.
