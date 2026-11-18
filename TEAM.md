# Team

## Thông tin nhóm

- Tên nhóm: GGEZ
- Lớp: L3A
- Repo của bàn: K5-L3A-DAY10-GGEZ-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Hoàng Anh | 2A202603385 | Kỹ sư cổng | ✓ |
|   2 | Võ Huy Hoàng | 2A202603397 | Vận hành và pháp lý |  |
|   3 | Nguyễn Trung Anh | 2A202603413 | Kỹ sư cổng |  |
|   4 | Nguyễn Tuấn Hiếu | 2A202603374 | Sản phẩm và kinh doanh |  |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenHoangAnh-2A202603385

### Phần việc phụ trách

Trưởng nhóm, vai Kỹ sư cổng. Phụ trách telemetry ở câu 1.4 (Phiếu A); trace và phân tích ở câu 2.2 (Phiếu B) và 3.1 (Phiếu C); hai bước giảm rò rỉ dữ liệu và behavioral test ở câu 2.7–2.8; phối hợp sửa cổng vòng 2 ở câu 3.5; bổ sung monitor ở câu 3.6. Tham gia review, trình bày kỹ thuật và đẩy các mốc của nhóm.

### Đóng góp cụ thể

Tôi phân tích trace `T-002@55` và các ticket sự cố S2, ghi lại nguyên nhân trong Phiếu B/C; phối hợp kiểm tra các rủi ro về dữ liệu đầu vào và hành vi ghi; đóng góp vào sửa cổng vòng 2 và theo dõi tỷ lệ đề xuất payer khác LOGIX qua monitor `non_logix_payer_proposal_rate`. Tôi cũng phụ trách các mốc commit/push của nhóm theo phân công.

### Bằng chứng

Các commit liên quan: `2d41bc5` (Phiếu B câu 2.2), `f646fa5` và `ad90bc5` (Phiếu C câu 3.1), `df3ae03` (phối hợp cổng vòng 2 và Phiếu C), `ea75524` (câu 3.6). Báo cáo tự kiểm tra S2 mới nhất: `R-S2-grade-20261118-215953-161959`; monitor mới phát hiện tỷ lệ đề xuất payer khác LOGIX là `0.466667` trên gói sự cố. Phiếu liên quan: `templates/form-a-criteria.md` A2, `templates/form-b-evaluation-gates.md` B2/B7.2–B7.3, `templates/form-c-incident.md` C2–C4/C8.

### Exit ticket

Tôi học được rằng trace cần đối chiếu dữ kiện từ hệ thống với nội dung khách tự nhập; monitor cũng nên theo dõi tín hiệu sớm của lỗi, kể cả khi cổng đã chặn được thao tác gây hại. Tôi còn chưa chắc ngưỡng cảnh báo và tỷ lệ escalations sẽ phù hợp đến đâu khi lưu lượng, dữ liệu và hành vi khách hàng trong pilot thật khác bộ giả lập.

### Sử dụng AI

Tôi dùng trợ lý AI để tra cứu yêu cầu trong các file hướng dẫn và hỗ trợ soạn mục cá nhân này. Các phân tích, quyết định, ngưỡng và thay đổi code/config của nhóm cần được các thành viên tự giải thích và chịu trách nhiệm khi demo.

## NguyenTuanHieu-2A202603374

### Phần việc phụ trách

Nguyễn Tuấn Hiếu, vai trò **Sản phẩm và kinh doanh**. Phụ trách câu 1.1, 1.6, 2.3, 2.9, 3.2, phần business của câu 3.5 và soạn dự thảo quyết định Gate 1 tại B8, C12.

### Đóng góp cụ thể

- **Phiếu A (A1, A4):** Viết mục tiêu hệ thống và lập, ký bộ tiêu chí chấp nhận cho Gate 1.
- **Phiếu B (B3, B7.4, B8):** Lập bản đồ dữ liệu, phân tích rủi ro lệch phiên bản chính sách, cấu hình các cổng kinh doanh và soạn dự thảo quyết định Gate 1 v1.
- **Phiếu C (C5, C7, C12):** Viết đặc tả LogiX chịu tiền hoàn do giao trễ. Mở phạm vi đánh giá mô phỏng sang tất cả kho trong `config/operating_gates.json` để kiểm đủ 15 ticket S2, đối chiếu chi phí và ROI sau khi nhóm sửa cổng, rồi soạn dự thảo quyết định Gate 1 v2.

### Bằng chứng

- Commit tiêu chí đã ký `784e17a`, bản đồ dữ liệu `6fcf0a9`, cổng kinh doanh vòng 1 `307ac03`, dự thảo B8 `d060665`.
- Commit đặc tả C5 `6f59f2d`, phạm vi đánh giá và cập nhật C7 `4d139f0`, `b008a62`, dự thảo C12 `44097b8`.

### Exit ticket

Phạm vi thử hẹp có thể bỏ sót lỗi cộng dồn theo khách. Chưa rõ chi phí và thời gian chờ duyệt sẽ thay đổi thế nào khi ticket dồn vào giờ cao điểm.
