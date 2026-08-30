# Paper-section subagents

Project subagents for the Sabbatical manuscript. Invoke in this order. Abstract and title last.

## Drafting sequence

1. `paper-methods` (technical writing). Materials and methods first so every later number has a procedure behind it.
2. `paper-results`. Only quantities in `paper/RESULTS.md` and the freeze census.
3. `paper-figures`. Specs and captions that cite those results. Cross-references for other sections.
4. `paper-discussion`. Interprets results. Does not mint new counts.
5. `paper-conclusion`. Bounded claims. No new findings.
6. `paper-introduction`. Written after methods and results exist, so the question matches the instrument.
7. `paper-citations`. Bibliography and in-text keys.
8. `paper-acknowledgments`. Dual-role disclosure and thanks. No data.
9. `paper-abstract-title`. Last. Compresses what the other sections actually said.

Orchestrator: `paper-orchestrator`. Use it to run or resume the sequence, not to draft a section itself.

## What a freeze is

A freeze is a locked snapshot of evidence. After it, those artifacts are not recoded. Later work may add a new source or a sidecar overlay. It may not rewrite the earlier extracts. That is why 298 and 14 stay reproducible.

| freeze | what was locked | what it did to the census |
|---|---|---|
| 1 | Gmail and Calendar extracts, independently coded | 221 applications |
| 2 | LinkedIn applied-list pages 1–10 and Jobright tracker | +77 `platform_log` = **298**. Interviews still 14 |
| 3 | Remaining personal Gmail queries and the keeganmoody33 calendar | +0 applications. Opportunity rows (Pin, Hotglue, Opsin, The Kiln) stay out of 298 |
| 4 | Claude care package as a sidecar, then a subject-confirmed overlay | +0 applications. Overlay does not recode Freeze 1–3 |

Do not print 247, 11 interviews, 4.45 percent, 321, or 325 as this freeze's finding.
