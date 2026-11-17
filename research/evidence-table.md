# Таблиця доказів — доступний корпус, 2026-10-09
Рішення одного reviewer; human_review=PENDING. Це таблиця вибраних кандидатів, не PRISMA. Повторний рядок R-001 у screening — історія рішення, не окремий record.

| Report / study | Роль | Механізм | Перевірка і межа |
|---|---|---|---|
| E-001 / ST-001, Or & Klein | Основний корпус | DNN → Q → es-EKF (C-001) | Окремий польовий запис; train/test мають спільні базові траєкторії (C-002); табличне порівняння C-003 |
| E-002 / ST-002, Irfan et al. | Основний корпус | LSTM → ваги/R → fusion (C-004) | Є handheld сценарій (C-005); можлива таблична неузгодженість C-009, кількісний висновок відкладено |
| E-003 / ST-003, Morozov-Leonov | Статистичний comparator | Діагностики IMM → score → R (C-006) | Симуляція; негативний результат за сильної деградації LiDAR (C-007) |
| E-004 / ST-004, Cook & Cohen | Контекст | Fuzzy confidence → ваги (C-008) | Зовнішнє позиціювання; не доказ польотної бортової навігації |
| E-005 / ST-005 | Очікує тексту | UNVERIFIED | Лише пошукова підказка; claim support відсутній |
| E-006 / ST-006 | Очікує тексту | UNVERIFIED | Лише пошукова підказка; claim support відсутній |
| E-007 / ST-007 | Очікує тексту | NOT_RETRIEVED | Зіставлено metadata; це не перевірка методу |
| E-008 / ST-008 | Очікує тексту | UNVERIFIED | Erratum і застосовність до БПЛА не перевірено |

DOI, взяті з PDF або пошукових підказок, мають окремі межі перевірки в metadata-checks.csv. CONTENT_OPENED не означає, що всі metadata, числа та corrections підтверджено.



## Continuation 2 — supersedes earlier pending rows
E-005 full XML retrieved: diagnostic context, C-011/C-012/C-014; explicit closed-loop fusion adaptation not established.
E-006 full XML retrieved: GRU/EKF HIL context, C-013; no independently established calibrated sensor-trust mapping.
E-008 metadata matched through Crossref; full text still pending. E-009 erratum metadata is a related report of ST-008, not a new study.
E-002 p23 visually checked; C-009 confirmed as table/text inconsistency, not proof of which value is correct.
Current selected register: 9 reports, 8 study clusters; 3 core reports, 3 context reports, 2 primary reports awaiting content, 1 related correction report. Provisional study clustering; not PRISMA totals.
