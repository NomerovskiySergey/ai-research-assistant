# AI Research Assistant — українська / English
Готовий файловий starter для Codex Desktop та ChatGPT з телефона. Версія 1.0, перевірка документації: 2026-10-09. Сім оригінальних skills, без стороннього виконуваного коду, API-ключів або платних залежностей.

## Запуск у Codex Desktop
1. Розпакуйте архів у окрему папку ai-research-assistant; не відкривайте ZIP як проєкт.
2. У Codex Desktop додайте/відкрийте цю локальну папку як проєкт. Створіть чат у корені.
3. Напишіть: «Прочитай AGENTS.md, docs/EVIDENCE.md і research/BRIEF.md. Допоможи заповнити brief для теми …; потім застосуй $literature-review. Запиши реальні запити й обмеження доступу».
4. Skills лежать у .agents/skills — офіційній repository location. Якщо не відображаються, відкрийте новий чат/перезапустіть app; як резерв попросіть прочитати конкретний SKILL.md.
5. Для PDF додайте файл у private/ і явно назвіть його. Наявність skill не додає PDF parser або доступ до баз: Codex використовує доступні інструменти, а недоступний текст позначає NOT_RETRIEVED.
6. Перевірте research/claims.csv і sources.csv; схвалення людини впишіть лише після особистої перевірки.
7. Для статті: «Застосуй $scientific-writing; створи manuscripts/draft-uk.md з templates/article-uk.md за перевіреними C-ID; пропуски познач».
8. Для аудиту: «Застосуй $peer-review, потім $citations. Надай major issues, непідтверджені твердження і список DOI mismatch».

## Git
У новій папці можна виконати:
~~~powershell
git init
git add .
git commit -m "Initialize research assistant"
~~~
Встановіть Git, якщо його немає. Через GitHub Desktop створіть приватний GitHub repository з цієї папки та Publish repository з увімкненою приватністю, або додайте власний remote. Цей комплект не публікувався автоматично.
Перед commit переглядайте diff і список файлів. private/, PDF, DOCX та .env виключені; це не замінює перевірку секретів і прав на матеріали.
Перед новою сесією зробіть Pull; після перевірених змін Commit і Push. Для значних чернеток використовуйте окрему branch. Не запускайте дві сесії, які одночасно редагують той самий файл.

## ChatGPT з телефона: два способи
**A. Codex mobile, якщо доступний вашому акаунту.** Офіційна документація описує керування cloud task або підключеним Mac/Windows PC з ChatGPT mobile; доступ залежить від rollout і workspace. Відкрийте Codex у мобільному застосунку, виберіть підключений комп’ютер і цей проєкт. Для cloud потрібне окремо налаштоване середовище з репозиторієм. Сам вхід в акаунт не завантажує локальні файли у cloud. Див. docs/COMPATIBILITY.md. Перевіряйте фактичний branch і commit перед роботою.
**B. Переносний ChatGPT Project — базовий шлях.**
1. Створіть ChatGPT Project «AI Research Assistant». Якщо Projects недоступні, використайте звичайний чат.
2. Вставте mobile/PROJECT-INSTRUCTIONS.txt у Project instructions; у звичайному чаті — першим повідомленням.
3. Завантажте mobile/MOBILE-KIT.md і mobile/CONTEXT.md. Це звичайний текстовий пакет, а не встановлення skills у мобільний застосунок. ZIP завантажувати не потрібно.
4. Окремо додайте лише дозволені для hosted AI статті/дані. Завантажені файли — snapshots; їхнє оновлення в Git не оновлює Project автоматично.
5. Напишіть: «Використай workflow paper-extraction із MOBILE-KIT.md для прикріпленої статті. Вказуй сторінки і невідомі дані; результат поверни як research note».
6. Попросіть handoff за templates/handoff.md із base commit, C/E-ID і пропозиціями змін. Скопіюйте відповідь у inbox/ на десктопі або збережіть її як файл.
7. Codex перевіряє повернення і вносить зміни; після review робіть commit. Нативна мобільна доступність і можливості інструментів не тестувалися у вашому акаунті.

## Синхронізація без втрати доказів
Git — головне сховище. ChatGPT Project — робоча копія контексту.
Перед телефоном: Commit → заповнити STATE.md → з кореня виконати:
~~~powershell
python scripts/export_mobile.py --revision YOUR_COMMIT_SHA
~~~
Замість YOUR_COMMIT_SHA вкажіть результат git rev-parse HEAD. Скрипт перезапише тільки три generated mobile files з явного allowlist; не включає private/, inbox/ чи рукописи. Python 3.10+ потрібен тільки для допоміжних скриптів, інструкції працюють і без нього.
Завантажте новий CONTEXT.md у Project, видаліть застарілий snapshot; назвіть новий base commit у повідомленні.
Після телефона: збережіть handoff в inbox/ → перевірте base commit проти поточного Git → за конфлікту попросіть Codex порівняти обидві версії → перевірте нові джерела і C-ID → прийміть diff → Commit/Push. Не перезаписуйте sources/claims CSV цілком мобільною відповіддю.
Без Python: вручну надішліть STATE.md, brief, sources/claims і потрібний шаблон, вказавши commit. MOBILE-KIT.md уже готовий.

## Структура
- AGENTS.md — правила агента.
- .agents/skills/ — literature-review, paper-extraction, research-gap-analysis, methodology-comparison, scientific-writing, peer-review, citations.
- research/ — brief, protocol, state, search/screening/source/claim журнали, bibliography.
- templates/ — research/paper notes, gap/method matrices, UA/EN IMRaD, review і handoff.
- manuscripts/ — чернетки; inbox/ — повернення з телефона; private/ — локальні вихідні файли.
- mobile/ — готові файли для ChatGPT.
- docs/ — evidence policy, сумісність, аудит сторонніх skills, acceptance scenarios.
- scripts/ — оригінальні offline export і structural audit.

## Перевірки
~~~powershell
python scripts/audit.py
python -m unittest discover -s tests -v
~~~
Audit перевіряє зв’язки й необхідні поля SUPPORTED claims, не зміст джерела. Порожній starter має проходити structural audit, але ще не містить наукових доказів.
Результати перевірки поставки: docs/VALIDATION.md. Сценарії для практичного приймання: docs/ACCEPTANCE.md.

## Джерела документації
[Codex skills](https://learn.chatgpt.com/docs/build-skills), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex mobile](https://learn.chatgpt.com/docs/mobile), [Projects](https://learn.chatgpt.com/docs/projects), [Crossref REST](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).
Ліцензія оригінального комплекту: MIT, LICENSE. Ліцензії наукових статей/даних залишаються їхнім правовласникам.

