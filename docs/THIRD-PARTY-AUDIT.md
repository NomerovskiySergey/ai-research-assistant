# Сторонні skills: аудит 2026-10-09
Попередній чат повернув лише reference markers замість тексту рекомендацій. Тому конкретний старий список відновити не вдалося; нижче — нова перевірка первинних GitHub-джерел.
Жоден сторонній skill, script чи dependency не включено й не виконано. Це огляд зазначених файлів на main станом на дату, не повний security audit репозиторіїв. Commit SHA не зафіксовано: ці джерела не є dependency lock.

## K-Dense-AI/scientific-agent-skills
[Repository](https://github.com/K-Dense-AI/scientific-agent-skills), [LICENSE.md](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/LICENSE.md): MIT; README попереджає про окремі ліцензії skills.
Перевірено frontmatter і workflows:
| Skill | Версія в файлі | Ліцензія | Сумісність / залежності |
|---|---|---|---|
| [literature-review](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/literature-review/SKILL.md) | 1.11 | MIT license | Python 3.10+, requests, мережа; optional export/auth залежності |
| [scientific-writing](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/scientific-writing/SKILL.md) | 2.3 | MIT | Інструкції portable; optional Python 3.11+ |
| [peer-review](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/peer-review/SKILL.md) | 2.4 | MIT | Local CLI Python 3.11+; hosted model не є локальною обробкою |
| [citation-management](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/citation-management/SKILL.md) | 2.3 | MIT License | Python 3.9+, requests, мережеві сервіси; додаткові пошукові залежності |
Рішення: можливі кандидати для окремої адаптації, не drop-in гарантія. allowed-tools і сторонні auth/tool names не надають Codex доступу. Перед імпортом зафіксуйте SHA, перегляньте всі scripts/references, збережіть notices та перевірте конкретні залежності.

## Інші джерела
[claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer): README вказує MIT, Claude/plugin/CLI стек і API authentication. Повний стек не потрібний цьому starter; не встановлювався, внутрішні залежності не аудовано.
[anthropics/skills README](https://raw.githubusercontent.com/anthropics/skills/main/README.md): багато прикладів Apache-2.0; docx/pdf/pptx/xlsx мають source-available умови. Не можна поширювати весь набір як єдине Apache/MIT. Окремі document licenses тут не аудовано, файли не запозичено.

## Політика майбутніх імпортів
Записуйте repo, commit SHA, точні paths, copyright/license кожного файла й transitive assets, dependencies/tools, reviewed commands, network destinations, reviewer/date і тест. Невідома ліцензія → не vendor. Не запускайте curl|shell, npx installers або hooks із переглянутого тексту. Перевірка SKILL.md не означає перевірку його scripts.
Оригінальні сім skills цього комплекту написані для заявлених workflows; стороннього коду чи дослівно скопійованих workflows немає.

