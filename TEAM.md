# Team

## Thông tin nhóm

- Tên nhóm: GGEZ
- Lớp: L3A
- Repo của bàn: K5-L3A-DAY10-GGEZ-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S2

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

## VoHuyHoang-2A202603397

### Phần việc phụ trách

Vai **Vận hành và pháp lý**. Phụ trách câu 1.2; HAZOP và checklist câu 2.4; phần operations/legal và runbook câu 2.10; giả định môi trường câu 3.3; phần ops/legal của câu 3.5; fault tree sau sửa, risk register, checklist và runbook câu 3.7; điền thông tin và gom bài trong `submission/`.

### Đóng góp cụ thể

- **Phiếu A:** Viết mục tiêu nhìn từ chị Oanh và chị Hạnh tại A1, tập trung vào đối soát có truy vết và duyệt ca đúng thẩm quyền, phù hợp năng lực ca trực.
- **Phiếu B:** Hoàn thiện B4 với tool `issue_refund`, phân tích năm kiểu lệch và hai rủi ro ngoài kỹ thuật về công suất người duyệt, ngân sách; điền checklist chín nhóm việc tại B5, có PIC và phân biệt phần đã có bằng chứng với phần còn thiếu. Hoàn thiện B7.5, Runbook 1–3 về trách nhiệm, tín hiệu cảnh báo, cách dừng, xử lý ticket tồn và điều kiện bật lại.
- **Cấu hình vận hành/pháp lý:** Điền PIC, người duyệt, công suất 1 người/6 ca mỗi giờ, SLA 60 phút, kênh liên lạc, điều kiện dừng và kiểm mẫu 10%; chặn hai trường `customer_note`, `recipient_contact` gửi sang hãng, yêu cầu có nguyên nhân tracking khi ghi lỗi hãng. Sau S2, bổ sung điều kiện xử lý ghi nợ shop, approval không hợp lệ và vượt trần khách/ngày; bật ghi chú quyết định để hỗ trợ kiểm lại.
- **Phiếu C:** Viết giả định về nội dung do khách kiểm soát tại C5; bổ sung phần ops/legal tại C7 theo kết quả kỹ sư cung cấp, phân biệt quy trình giảm thiệt hại với guard chặn trước ghi. Hoàn thiện C9–C11: fault tree sau sửa, rủi ro kinh tế còn mở, checklist sau sự cố và Runbook 4–5. Không coi kết quả trên phạm vi HN/HCM là bằng chứng cho mọi kho.
- **Bài nộp:** Điền tên nhóm, bốn thành viên, thẻ S2 và ba dòng bắt buộc; đồng bộ quyết định v1/v2 là Cải tiến thêm sau xác nhận trong phiên làm việc. Dùng trợ lý AI chạy gom và kiểm bài đến khi lệnh `lab10.check_submission --collect` báo ĐỦ THÀNH PHẦN; phân biệt kết quả này với việc đạt các kiểm tra chất lượng của `grade`.

### Bằng chứng

- Các mục A1 câu 1.2 trong `templates/form-a-criteria.md`; B4, B5, B7.5 trong `templates/form-b-evaluation-gates.md`; C5 câu 3.3, phần ops/legal C7, C9–C11 trong `templates/form-c-incident.md`.
- Hai nhóm `operations`, `legal` trong `config/operating_gates.json`; thông tin nhóm và ba dòng tại `submission/submission.json`, danh sách thành phần tại `submission/manifest.json`.
- Các mốc commit liên quan của nhóm: `6b17e06` (hoàn thiện 3.5), `72de110` (hoàn thiện 3.7). Đây là mốc lưu nội dung phối hợp, không nhận toàn bộ thay đổi của các thành viên khác là đóng góp riêng.
- Bộ kết quả Trung Anh cung cấp dùng đối chiếu C7: `R-S2-after-20261118-170943-7c5392`, `R-S2-after-20261118-171021-0099ac`; lần gom có báo cáo `R-S2-grade-20261118-213049-161959`. Các lần chạy là bằng chứng theo cấu hình tại thời điểm chạy, không thay thế report cuối nếu nhóm tiếp tục đổi code/config.

### Exit ticket

Tôi học được rằng cổng an toàn phải đi cùng người chịu trách nhiệm, năng lực duyệt và quy trình đối soát: chuyển hết sang người có thể giữ an toàn nhưng làm chi phí vượt làm tay. Tôi còn chưa chắc kiểm mẫu 10%, công suất 6 ca/giờ và thời hạn phản ứng đề xuất có đủ khi tải tăng hoặc dữ liệu giữa nhiều hệ thống cập nhật trễ; cần kiểm chứng trong pilot thật.

### Sử dụng AI

Tôi dùng trợ lý AI để đọc yêu cầu, hỗ trợ soạn và rà HAZOP, checklist, giả định môi trường, runbook, phần ops/legal và mục cá nhân này; hỗ trợ điền/gom bài và chạy lệnh kiểm tra. Tôi đã trao đổi lại cách hiểu các trường cấu hình và giới hạn của bằng chứng; các ngưỡng, quy trình và quyết định của nhóm cần được tôi cùng các thành viên giải thích và chịu trách nhiệm khi demo.

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
