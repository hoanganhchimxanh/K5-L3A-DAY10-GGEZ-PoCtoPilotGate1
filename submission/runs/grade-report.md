# Tự kiểm tra sự cố S2 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S2-grade-20261118-213049-161959` · bàn: `K5-L3A-DAY10-GGEZ-PoCtoPilotGate1` · grader `lab10-1.0` · 0.79s
- Ba mốc: base `R-S2-before-20261118-213050-161959` · prepared `R-S2-prepared-20261118-213050-161959` · after `R-S2-after-20261118-213050-161959` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `c5aff4c2`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `1619595bd54a`
- Hash Bản tiêu chí chấp nhận: `042370e4ef62` · đã ký: `042370e4ef62` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S2` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S2 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ❌ | file khoá bị đổi: ['data/tickets.jsonl', 'data/world.json', 'incidents/S1/card.json', 'incidents/S1/card.md', 'incidents/S1/tickets.jsonl', 'incidents/S1/world_patch.json', 'incidents/S2/card.json', 'incidents/S2/card.md', 'incidents/S2/tickets.jsonl', 'incidents/S2/world_patch.json', 'incidents/S3/card.json', 'incidents/S3/card.md', 'incidents/S3/tickets.jsonl', 'incidents/S3/world_patch.json', 'incidents/S4/card.json', 'incidents/S4/card.md', 'incidents/S4/tickets.jsonl', 'incidents/S4/world_patch.json', 'incidents/S5/card.json', 'incidents/S5/card.md', 'incidents/S5/tickets.jsonl', 'incidents/S5/world_patch.json', 'incidents/S6/card.json', 'incidents/S6/card.md', 'incidents/S6/tickets.jsonl', 'incidents/S6/world_patch.json', 'incidents/S7/card.json', 'incidents/S7/card.md', 'incidents/S7/tickets.jsonl', 'incidents/S7/world_patch.json', 'incidents/S8/card.json', 'incidents/S8/card.md', 'incidents/S8/tickets.jsonl', 'incidents/S8/world_patch.json', 'lab10/__init__.py', 'lab10/_gradectx.py', 'lab10/_noop_guards.py', 'lab10/agent.py', 'lab10/check_submission.py', 'lab10/checkpoint.py', 'lab10/criteria.py', 'lab10/eval.py', 'lab10/gate.py', 'lab10/grade.py', 'lab10/helpers.py', 'lab10/mock_llm.py', 'lab10/ops.py', 'lab10/tools.py', 'lab10/trace.py', 'lab10/world.py', 'tests/test_public.py'] |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['non_logix_payer_proposal_rate']; sáng đèn: [('non_logix_payer_proposal_rate', 'before', 0.0, 0.466667), ('non_logix_payer_proposal_rate', 'after', 0.0, 0.466667)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.8 | 0.3333 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 2700 · 10000 | 14625 · 10000 | 5273 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 831 · 1500 | 731 · 1500 | 931 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -6606502 | -23125 | 70898 |
| ROI | -163.12 | -0.32 | 0.9 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 3230000 · 2000000 | 18000 · 2000000 | 282000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 6716000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.3333 | 1.0 |
| số kho đắt hơn làm tay | 0 | 1 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 15 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 721đ | — | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 821đ |
| kho DN | pass 0.4286; hoàn sai 21160000; oan 15; PII 0; chi phí 688đ | — | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4973đ |
| kho HCM | pass 0.0; hoàn sai 7470000; oan 0; PII 0; chi phí 670đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10570đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 670đ |
| kho HN | pass 0.3333; hoàn sai 4950000; oan 0; PII 0; chi phí 728đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 7328đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3495đ |
| hãng DNB | pass 0.5; hoàn sai 3930000; oan 0; PII 0 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.25; hoàn sai 5470000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 0.0; hoàn sai 560000; oan 5; PII 0 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.25; hoàn sai 23620000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.3077 | 0.2727 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 5934 · 10000 | 4456 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 670 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 52853 | 121962 |
| ROI | 1.34 | 0.69 | 1.24 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5909 | 1.0 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 665đ |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4646đ |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4567đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2308 | 0.2273 | +0.0 |
| visible | pass_rate | 0.4667 | 1.0 | 1.0 | +0.5333 |
| visible | pass_k | 0.4667 | 1.0 | 1.0 | +0.5333 |
| visible | wrongful_refund_vnd | 33580000 | 0 | 0 | -33580000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 15 | 0 | 0 | -15 |
| visible | merchant_debit_vnd | 32750000 | 0 | 0 | -32750000 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.8 | 0.2 | +0.2 |
