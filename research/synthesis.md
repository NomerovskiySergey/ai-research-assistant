# Робочий огляд — 2026-10-09
Статус: scoping-пілот із доступних відкритих текстів. Межі brief залишаються робочими; настанову «продовжуй» використано для продовження пошуку, без перетворення пропозицій на формальне людське схвалення протоколу.

## Що саме адаптується
У відкритому корпусі є різні об’єкти адаптації. Or & Klein навчають оцінку процесного шуму Q (C-001); Irfan et al. описують сенсорні ваги й адаптацію R (C-004); прототип IMM-KF перетворює діагностики на довіру та масштабування R (C-006). Нечіткі ваги зовнішнього позиціювання залишено контекстом (C-008). [Or & Klein](https://arxiv.org/html/2207.12082v3), [Irfan et al.](https://myresearchspace.uws.ac.uk/ws/files/60048035/2025_02_07_Irfan_et_al_LSAF_final.pdf), [IMM-KF](https://icsfti-proc.kpi.ua/article/view/365751/354636).

Інтерпретація reviewer: ці механізми слід порівнювати окремо. Зменшення похибки не саме по собі доказ калібрування reliability score як імовірності. Це правило інтерпретації цього огляду, а не висновок про всі існуючі методи.

## Перевірка та суперечності
У Or & Klein наведено польове порівняння з адаптивним baseline (C-003); спільні базові траєкторії симуляційного split обмежують силу тесту перенесення, хоча польовий запис відокремлено (C-002; інтерпретація reviewer). У LSAF handheld-сценарій відрізняється від польоту (C-005); потенційну табличну неузгодженість C-009 залишено PARTIAL до візуальної перевірки. Загальні відсотки покращення між цими працями не об’єднано.

Негативний результат збережено: автор IMM-KF повідомляє погіршення за сильної деградації LiDAR (C-007) і пояснює його втратою впливу ключового джерела корекції. Це обмежує висновок у межах конкретного прототипу, а не доводить неефективність адаптивного комплексування загалом. [Результати та висновки](https://icsfti-proc.kpi.ua/article/view/365751/354636).

## Пропозиція для уточнення дослідницького питання
Запропоноване питання: «Як перетворювати оцінку достовірності сенсорів на адаптацію комплексування з урахуванням їхнього внеску у спостережуваність навігаційного стану?»
Гіпотеза C-010: спільна перевірка калібрування довіри, закону адаптації та ролі сенсора може бути корисною. Наукову новизну/прогалину ще не встановлено.

Пропонований план порівняння: однакові сенсори й маршрути; fixed fusion, innovation-based adaptation та learned reliability; окремі bias/dropout/hold і комбіновані деградації; розбиття за маршрутами/середовищами; ablation оцінки довіри й закону адаптації; точність, калібрування, false alarms, час відновлення й ресурси. Це план майбутнього дослідження, а не виконаний експеримент.

## Межі покриття
Виконано лише запити search-log.csv; нативні Scopus/WoS/IEEE не виконувалися. Результати вебпошуку вибіркові; всі snippets не screened. Full text відкрито для E-001–E-004, але extraction охоплює зазначені розділи, без незалежної реплікації. E-005–E-008 очікують текстів; registry/corrections-перевірка неповна. Немає другого reviewer, meta-analysis чи PRISMA. Див. access-limitations.md, bias-assessment.csv та notes/.



## Continuation 2: diagnosis, fusion and reporting
Sun et al. use ANFIS decisions to update the online learning database (C-011), and discuss accumulation of erroneous labels (C-012). Their author-defined false-alarm denominator is total detected faults (C-014). This diagnostic study is contextual: detection performance is not treated as evidence of downstream adaptive-navigation improvement. [Publisher JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5677314/fullTextXML).

Negru et al. use GRU INS correction/master fusion with HIL validation (C-013). This is retained as hybrid-navigation context; a calibrated sensor-level reliability-to-adaptation mechanism was not established in the read sections. [Publisher JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10857391/fullTextXML).

C-009 is now SUPPORTED: visual inspection confirms the LSAF table/text discrepancy. This supports caution about reporting; it does not establish the correct underlying effect. [Local verification](verification/E-002-p23.png).

Proposed focus, still a hypothesis rather than established novelty: jointly evaluate trust calibration, the trust-to-fusion mapping and sensor contribution to observability (C-010). Add protection against erroneous online labels (motivation C-012), and specify false-alarm denominators explicitly (motivation C-014). A method should be compared using the same sensor suite and separate routes/environments; this remains a research proposal, not an executed experiment.

Verified bibliographic subset is in references.bib/index. Erratum metadata E-009 is matched, but its corrected content remains unavailable (C-015 PARTIAL). No quantitative UWB/GNSS conclusion is adopted.
