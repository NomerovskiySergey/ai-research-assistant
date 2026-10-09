# Протокол огляду
Version/date: 0.1 / 2026-10-09. Робочі межі — BRIEF.md. Поточний результат: пілот, не завершений систематичний огляд.
## Eligibility — до screening
2015–2026-10-09; українська/англійська. Основний корпус: первинні дослідження БПЛА з оцінюванням достовірності сенсорів і адаптацією комплексування. Класичні методи — comparator; огляди й інші платформи — окремий контекст. Препринти позначати. Abstract-only дає лише попереднє рішення.
Виключення: керування без навігаційного оцінювання; детекція зовнішніх БПЛА; fusion без адаптації; поза часовими межами після перевірки online-first.
## Стратегія
Синоніми: UAV/drone/unmanned aerial vehicle/quadrotor; navigation/localization/positioning/odometry; sensor fusion/integrated navigation; reliability/uncertainty/confidence/trust/fault detection; machine learning/neural network/deep learning/fuzzy/reinforcement learning.
Запропонований Scopus: TITLE-ABS-KEY((UAV OR drone OR "unmanned aerial vehicle") AND (navigation OR localization) AND ("sensor fusion" OR "integrated navigation") AND (adaptive OR uncertainty OR reliability) AND ("machine learning" OR "neural network" OR fuzzy)). Мета: міждисциплінарне покриття.
Запропонований Web of Science: TS=((UAV OR drone OR "unmanned aerial vehicle") AND (navigation OR localization) AND ("sensor fusion" OR "integrated navigation") AND (adaptive OR uncertainty OR reliability) AND ("machine learning" OR "neural network" OR fuzzy)). Мета: доповнення і citation tracking.
Запропонований IEEE Xplore: All Metadata: (UAV OR quadrotor) AND (navigation OR localization) AND ("sensor fusion" OR "integrated navigation") AND (adaptive OR uncertainty OR reliability) AND ("machine learning" OR "neural network" OR fuzzy). Синтаксис перевірити в інтерфейсі. Мета: інженерні публікації.
arXiv — препринти і версії; видавці/репозитарії — тексти. Ці database-specific запити НЕ виконувалися. Реальні запити — search-log.csv.
## Screening і extraction
Reviewer: Codex; другого незалежного reviewer немає; human_review=PENDING. Назва/abstract → full text; недоступність не дорівнює невідповідності. Конфлікти — людині.
record_id = запис; E-ID = report/версія; study_id = дослідження. Deduplication: нормалізований DOI або назва/автори/рік; зіставляти препринт і журнальний report перед підрахунками. Поки перевірено один кандидат, deduplication всього корпусу не виконано.
Поля extraction: сенсори, деградації, модель достовірності, адаптація Q/R/ваг/gating, train/test, платформа, comparator, метрики, hardware/latency, код/дані, локатори.
Bias: запропонована інженерна матриця, не валідований клінічний інструмент: leakage, незалежність test, ground truth, справедливість baselines, ablation, реалістичність відмов, повтори, переносимість, ресурси. Abstract-only: ці домени NOT_RETRIEVED.
Синтез: механізм достовірність → адаптація → перевірка; окремо covariance tuning, weighting/gating, federated filters, factor graphs. Несумісні ефекти не об’єднувати. Meta-analysis потребує окремого погодженого плану.
Amendment: два discovery-запити виконано до запису цього протоколу, screening — після. PRISMA не розраховувати на основі неповної видачі.

Amendment 2026-10-09: statistical reliability prototype included as comparator; external fuzzy positioning retained as context. Extraction follows paper-extraction; reading limited to notes locators. PDF numerical claims withheld where image verification failed. Related reports not counted independently. Native database proposals remain unexecuted; no meta-analysis or PRISMA. Existing E-001/C-001 IDs preserved.

