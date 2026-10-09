# Сумісність — перевірено 2026-10-09
| Середовище | Спосіб | Межа перевірки |
|---|---|---|
| Codex Desktop / CLI | AGENTS.md у корені, .agents/skills/<name>/SKILL.md | Підтверджено шлях та формат офіційною документацією; discovery у новому проєкті потребує smoke test |
| ChatGPT mobile → Codex | Cloud або підключений Windows/Mac project | Документовано; rollout/workspace-dependent, не перевірено в акаунті |
| ChatGPT Project / чат | Вставити instructions, завантажити MOBILE-KIT.md + CONTEXT.md | Текстовий fallback; автоматичне виконання repo skills не припускається |
| Git/GitHub | Commit/Push/Pull | Синхронізує repository files; не оновлює вкладення ChatGPT Project |
Core skills — Markdown з name/description, без tool aliases, hooks чи прив’язки до MCP. Фактичний search, PDF parsing, Python і мережа залежать від host permissions/tools.
Пошук неможливий offline: працюйте з наданими файлами, нові DOI залишайте UNVERIFIED.
Джерела: [skills](https://learn.chatgpt.com/docs/build-skills), [AGENTS](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [mobile](https://learn.chatgpt.com/docs/mobile), [projects](https://learn.chatgpt.com/docs/projects).
Не плутайте platform compatibility з підтвердженою науковою якістю.

