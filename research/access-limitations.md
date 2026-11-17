# Межі доступу — 2026-10-09
Фактичні запити S-001–S-011 у search-log.csv. Пошук виконувався web.search, без нативного доступу до Scopus/WoS/IEEE та без інструментальних часових/мовних фільтрів. S-010 містив site:mdpi.com. Загальні та per-query counts інструмент не повідомив. Не трактувати це як нуль.
Для S-009–S-011 збережено спільний повернутий текст у raw/search-batch-009-011.txt; він включає також паралельні open-операції. Для попередніх запитів повного локального експорту немає. Реєстр screening містить лише вибрані релевантні кандидати.
## Відкриті тексти
- E-001: arXiv HTML доступний; методи та результати прочитано; PDF не відкривався.
- E-002: repository PDF UWS доступний через web.open; вибрані розділи витягнуто. Це відновлює доступ попри помилку на сайті видавця.
- E-003: publisher PDF доступний через посилання на landing page.
- E-004: NASA conference PDF доступний.
## Невдалі спроби
- PMC5677314: browser check/reCAPTCHA; Europe PMC mirror open — Internal Error.
- MDPI: 17/10/2243, numeric article227430, 24/3/981 та Machines13/2/130 — Internal Error. Ранній пробний URL 17/10/2331 не підтвердив ідентичність статті й не використаний як evidence.
- Cranfield PDF E-006: anti-bot «Oh noes!». Пошуковий кеш не вважається відкритим повним текстом.
- IEEE10938202: попередній HTTP418; повний текст/erratum не отримано.
- Kingston accepted manuscript Zweiri-Y-40951-AAM.pdf: HTTP403; metadata page відкрита.
- DOI resolvers TIM2022.3197775 / machines13020130 і Crossref /works із URL-encoded DOI: Internal Error. Це UNVERIFIED, не INVALID.
- Screenshots E-002 p23, E-003 p16, E-004 p4: Internal Error. Повтор E-002 p23 повідомив, що screenshot не може розпізнати PDF. Числа з цих PDF не використовуються як візуально перевірені; потенційна неузгодженість C-009 залишається PARTIAL.
## Межі висновків
Немає незалежного другого reviewer, повного citation chasing, повного deduplication видачі, перевірки всіх corrections чи реплікації коду. Пов’язані reports (журнальний E-001, конференційний попередник E-002, презентація E-004) не додані як незалежні studies.
CONTЕNT_OPENED у реєстрі означає відкритий текст із явно вказаним access_scope, а не підтвердження всіх методів/чисел. Paywall або глобальну недоступність баз не встановлено. Матеріали не завантажувалися в сторонні сервіси, платні API не застосовувалися.



## Continuation 2 — restored access and remaining limits
Sandbox download failed DNS. User-approved external-network commands obtained local E-002 PDF, publisher JATS E-005/E-006 via Europe PMC, Crossref metadata E-001/E-002/E-008, and erratum search metadata. All API attempts and SHA256 for successful responses are in access-attempts.csv. No confidential uploads, installs or paid API calls.
E-002 p23 rendered with bundled pypdfium2 and visually inspected; this closes the former image-check limit for that page only. Other PDF pages are not declared visually verified.
Crossref E-005/E-006 retries returned429; records remain valid candidates, not INVALID. Publisher JATS and EuropePMC metadata matched instead. Kingston old host failed DNS; current manuscript URL returned403 again. Publisher MDPI XML attempt returned429. PMC HTML still returned browser check; EuropePMC fullTextXML provided an open alternative.
Native EuropePMC DOI lookup and Crossref correction-title query were executed and logged; native Scopus/WoS/IEEE topic searches still were not. This is not an exhaustive systematic review.
New broad-search leads, including 2026 learned-trust/RL papers, are not yet screened and not used for substantive claims. E-008 primary text and E-009 corrected content remain NOT_RETRIEVED; corrections for other reports remain UNVERIFIED.
Crossref empty relation/update-to fields do not prove absence of corrections: E-008's erratum was found by title search.
