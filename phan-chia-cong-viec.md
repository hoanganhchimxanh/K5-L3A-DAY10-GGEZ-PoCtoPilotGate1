# 📋 Phân công việc – Nhóm GGEZ · LAB 10

> **3 vai · 4 người** – thứ tự theo dòng thời gian của lab

---

## Thành viên & vai

| Người | MSSV | Vai |
|---|---|---|
| **Nguyễn Hoàng Anh** *(trưởng nhóm)* | 2A202603385 | Vận hành và pháp lý |
| **Võ Huy Hoàng** | 2A202603397 | Vận hành và pháp lý |
| **Nguyễn Trung Anh** | 2A202603413 | Kỹ sư cổng |
| **Nguyễn Tuấn Hiếu** | 2A202603374 | Sản phẩm và kinh doanh |

> [!NOTE]
> Vận hành và pháp lý có **2 người** (Hoàng Anh + Huy Hoàng) → chia đôi theo mục cụ thể bên dưới.
> Mọi **quyết định v1, v2** do **cả bàn** cùng chốt.

---

## ⏱️ Phút 0–15 · Cài đặt & chia vai

| Việc | Người làm | File |
|---|---|---|
| Tạo repo, mời collaborator, cài đặt Git | **Hoàng Anh** (trưởng nhóm) | GitHub |
| Clone repo, chạy `python3 -m unittest discover -s tests` kiểm `Ran 13 tests OK` | Cả bàn | — |
| Chọn 1 eval card + 1 PRD v1.1 từ Lab 9 làm bản chung | Cả bàn thống nhất | `docs/` |
| Điền `TEAM.md` bảng thành viên ✅ *(đã xong)* | Hoàng Anh | `TEAM.md` |

---

## ⏱️ Phút 15–60 · Khối 1: Viết Bản tiêu chí (Phiếu A)

| Câu | Nội dung tóm tắt | Người cầm bút | File/Mục |
|---|---|---|---|
| **1.1** | Mục tiêu cấp hệ thống (từ PRD §3) | **Tuấn Hiếu** | Phiếu A · A1 |
| **1.2** | Mục tiêu từ góc nhìn chị Oanh (kế toán) & chị Hạnh (trưởng ca) | **Huy Hoàng** | Phiếu A · A1 |
| **1.3** | Offline metric cho 1 bước của agent | **Trung Anh** | Phiếu A · A2 cột Offline |
| **1.4** | Telemetry production (khung thời gian + ngưỡng báo động) | **Hoàng Anh** | Phiếu A · A2 cột Telemetry |
| **1.5** | Đọc khoảng tin cậy, chọn kết luận đúng | **Cả bàn** | Phiếu A · A3 |
| **1.6** | Viết Bản tiêu chí đầy đủ + ranh giới đầu ra; điền `acceptance_criteria.json` | **Tuấn Hiếu** | Phiếu A · A4; `config/acceptance_criteria.json` |

---

## ⏱️ Phút 60–65 · Ký tiêu chí (Phiếu A · A5)

| Việc | Người làm |
|---|---|
| Soát lại `acceptance_criteria.json` lần cuối | **Tuấn Hiếu** + cả bàn |
| Chạy `python3 -m lab10.criteria sign` → commit → push | **Trung Anh** (chạy lệnh) |

> [!IMPORTANT]
> **Không chạy `lab10.eval` trước bước này.** Sau khi ký, không sửa `acceptance_criteria.json` nữa.

---

## ⏱️ Phút 65–85 · Khối 2A: Tìm rủi ro (Phiếu B)

> Ba vai làm song song 10 phút đầu, rồi cả bàn làm pre-mortem 10 phút.

| Câu | Nội dung tóm tắt | Người làm | Mục |
|---|---|---|---|
| **2.1** | Chạy mốc `base`, đọc report, ghi mã lần chạy | **Trung Anh** | Phiếu B · B0, B1 |
| **2.2** | Trace `T-002@seed55`, điền bảng soát lỗi | **Trung Anh** | Phiếu B · B2 |
| **2.3** | Bản đồ dữ liệu + ví dụ drift 3 tháng tới | **Tuấn Hiếu** | Phiếu B · B3 |
| **2.4** | HAZOP mở rộng (≥3 dòng kỹ thuật + ≥2 ngoài kỹ thuật); checklist 9 nhóm việc lần 1 (có PIC tên) | **Hoàng Anh** + **Huy Hoàng** | Phiếu B · B4, B5 |
| **2.5** | Pre-mortem 4 lăng kính, chọn 2–3 lý do thành cổng | **Cả bàn** | Phiếu B · B6 |

---

## ⏱️ Phút 85–105 · Khối 2B: Dựng cổng phòng ngừa (Phiếu B)

| Câu | Nội dung tóm tắt | Người làm | File/Mục |
|---|---|---|---|
| **2.6** | Code 2–3 cổng trong `guards.py` (`pre_guard` / `write_gate`); chạy eval + unittest | **Trung Anh** | `lab10/guards.py`; Phiếu B · B7.1 |
| **2.7** | 2 bước tránh rò rỉ dữ liệu | **Trung Anh** | Phiếu B · B7.2 |
| **2.8** | Viết 1 behavioral test + 2 ticket hiểm, chạy `--adhoc` | **Trung Anh** + **1 người không code** *(Tuấn Hiếu hoặc Huy Hoàng)* | Phiếu B · B7.3 |
| **2.9** | Điền `operating_gates.json` mục `business` (trần hoàn, ngân sách/ticket, phạm vi pilot, ROI) | **Tuấn Hiếu** | `config/operating_gates.json` → `business`; Phiếu B · B7.4 |
| **2.10** | Điền mục `operations` + `legal`; viết runbook phần 1–3 + Giờ cao điểm | **Hoàng Anh** + **Huy Hoàng** | `config/operating_gates.json` → `operations`, `legal`; Phiếu B · B7.5, B7.6 |

> [!TIP]
> **Huy Hoàng** phụ trách phần `operations` (PIC, người trực, hàng chờ, kênh báo tin).
> **Hoàng Anh** phụ trách phần `legal` + toàn bộ runbook 1–3.

---

## ⏱️ Phút 105–115 · Chốt cổng vòng 1 + Quyết định v1 (Phiếu B · B8)

| Việc | Người làm |
|---|---|
| Chạy `python3 -m lab10.checkpoint` | **Trung Anh** |
| Chạy `lab10.eval --stage prepared` + `lab10.gate` | **Trung Anh** |
| Điền cột v1 (quyết định, 3 bằng chứng, decision_rule, ngày quyết định lại) | **Tuấn Hiếu** (viết) + cả bàn chốt |
| Commit + push | **Hoàng Anh** |

---

## ⏱️ Phút 115–125 · Nghỉ 🧘

---

## ⏱️ Phút 125–135 · Nhận thẻ sự cố (Phiếu C · C0, C1)

| Việc | Người làm |
|---|---|
| `git pull --no-rebase ...` để tải thẻ | **Trung Anh** |
| Cử 1 người lên bốc số S1–S8 | **Hoàng Anh** (trưởng nhóm) |
| Ghi số thẻ vào đầu Phiếu C | **Huy Hoàng** |
| Chạy ngay `python3 -m lab10.grade --incident Sx` **trước khi sửa gì** | **Trung Anh** |
| Điền C0 (mã prepared), C1 (cổng vòng 1 đỡ được gì; đối chiếu pre-mortem) | **Cả bàn** |

---

## ⏱️ Phút 135–155 · Phân tích sự cố (Phiếu C · C2–C6)

| Câu | Nội dung tóm tắt | Người làm | Mục |
|---|---|---|---|
| **3.1** | Trace ≥2 ticket hỏng; bảng soát lỗi | **Trung Anh** (trace) + **Huy Hoàng** (phần riêng thẻ) | Phiếu C · C2, C3, C4 |
| **3.2** | Viết 1 specification bị vi phạm → tác hại | **Tuấn Hiếu** | Phiếu C · C5 |
| **3.3** | Giả định môi trường ngầm, có thể sai ngoài thực tế | **Huy Hoàng** | Phiếu C · C5 |
| **3.4** | Fault tree trước khi sửa (≥2 nhánh, 2 tầng khác nhau) | **Cả bàn** | Phiếu C · C6 |

---

## ⏱️ Phút 155–185 · Sửa + Chỉ số theo dõi (Phiếu C · C7–C11)

| Câu | Nội dung tóm tắt | Người làm | File/Mục |
|---|---|---|---|
| **3.5 (code)** | Sửa `guards.py` cho nguyên nhân kỹ thuật | **Trung Anh** | `lab10/guards.py`; Phiếu C · C7 |
| **3.5 (business)** | Sửa `operating_gates.json` mục `business` | **Tuấn Hiếu** | `config/operating_gates.json` |
| **3.5 (ops/legal)** | Sửa `operating_gates.json` mục `operations`, `legal` | **Hoàng Anh** + **Huy Hoàng** | `config/operating_gates.json` |
| **3.6** | Thêm chỉ số theo dõi mới trong `monitors.py` | **Trung Anh** | `lab10/monitors.py`; Phiếu C · C8 |
| **3.7** | Fault tree sau sửa; ≥1 dòng Risk register; cập nhật checklist; runbook 4–5 | **Huy Hoàng** + **Hoàng Anh** | Phiếu C · C9, C10, C11 |
| Chạy kiểm tra | **Trung Anh** | `lab10.eval --suite Sx --stage after` + `lab10.grade` |

---

## ⏱️ Phút 185–200 · Quyết định v2 + Gom bài (Phiếu C · C12)

| Việc | Người làm | File |
|---|---|---|
| Điền cột v2 (quyết định, 3 mã lần chạy, 3 dòng bắt buộc) | **Tuấn Hiếu** (viết) + cả bàn chốt | Phiếu C · C12 |
| Điền `submission/submission.json` (team, members, incident, decision_v1, v2, three_lines) | **Huy Hoàng** | `submission/submission.json` |
| Chạy `python3 -m lab10.check_submission --collect` tới khi `ĐỦ THÀNH PHẦN` | **Huy Hoàng** | — |
| Commit + push bài lần cuối | **Hoàng Anh** | — |

---

## ⏱️ Phút 200–240 · Demo + Nộp bài

| Việc | Người làm |
|---|---|
| Demo 3 mốc base · prepared · after | **Trung Anh** (chạy lệnh) + **Tuấn Hiếu** (trình bày số) |
| Phản biện từ bàn kia (chạy ticket hiểm, đổi thử config) | **Trung Anh** xử lý live |
| Trả số về bản v2, chạy lại `lab10.grade` + `check_submission` | **Trung Anh** + **Huy Hoàng** |
| Mỗi thành viên nộp link repo trên LMS + viết exit ticket trong `TEAM.md` | **Từng người tự nộp** |

---

## 📌 Tổng kết phân công theo người

| Người | Vai chính | Phụ trách trọng tâm |
|---|---|---|
| **Nguyễn Hoàng Anh** | Vận hành & Pháp lý | Telemetry (1.4), HAZOP & checklist (2.4), `legal` + runbook 1–3 (2.10), cổng vòng 2 ops/legal (3.5), push các mốc |
| **Võ Huy Hoàng** | Vận hành & Pháp lý | Mục tiêu Oanh/Hạnh (1.2), `operations` config (2.10), phần riêng thẻ (3.1), giả định môi trường (3.3), `submission.json` + gom bài |
| **Nguyễn Trung Anh** | Kỹ sư cổng | Offline metric (1.3), chạy tất cả lệnh eval/trace/grade, code `guards.py`, `monitors.py`, behavioral test (2.8), demo live |
| **Nguyễn Tuấn Hiếu** | Sản phẩm & Kinh doanh | Mục tiêu hệ thống (1.1), Bản tiêu chí + ký (1.6), bản đồ dữ liệu (2.3), `business` config (2.9, 3.5), specification (3.2), quyết định v1+v2 |
