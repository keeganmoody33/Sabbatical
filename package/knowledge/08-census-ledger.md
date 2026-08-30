<!-- kit-meta
file: 08-census-ledger.md
tier: 0 (durable)
created: 2026-08-30
updated: 2026-08-30 (Jobright stratum audited and named as a gap)
status: THE RUNNING COUNT. Every change to the census total is recorded here with a reason. Nothing else states a total.
-->

# Census ledger

**Current census: 321 applications across 298 distinct companies.**

Built from the ground up out of this project's own corpus. **The 247-row pre-sweep workbook is retired as an anchor** and is not a source of truth for this study.

Row counts re-verified against `claude/full-application-register.csv` on 2026-08-30 with a CSV parser: 321 data rows, 234 `gmail/ATS`, 87 `LinkedIn`, 298 distinct companies, 35 rows with no submission date. The file and this ledger agree.

## Why the 247 is gone

It was assembled before the retrieval sweep existed, from a different and smaller corpus, by a method this project cannot reproduce. Every time it was used as a base, it imported an unauditable figure into a ground-up build and then required a correction — the interview count was wrong by at least two for exactly this reason.

It is retained in `sources.md` as [S1], a historical source. It is no longer an input to any total.

**Consequence, stated plainly:** the census is now smaller in provenance and larger in defensibility. Every one of the 321 rows traces to a named artifact in a numbered retrieval log.

## The count, and how it was reached

| step | rows | note |
|---|---|---|
| Gmail / ATS stratum, extracted row-level from logs 001–034 | 238 | company, role, date, outcome, channel, tier |
| LinkedIn stratum, in-window | 105 | exact minute-level timestamps |
| — of which already represented in the Gmail stratum | −18 | measured in logs 038 and 039 |
| LinkedIn net additions | +87 | |
| Subtotal | 325 | |
| Adjudicated removals (below) | −4 | |
| **Census** | **321** | **298 distinct companies** |

## Adjudicated removals

Each removal has a reason. None was an automatic merge.

1. **BX Studio, Gmail 2026-04-08** — merged into `LI-036`. The LinkedIn row is the submission; the Gmail thread is the follow-up in which a video was sent and forwarded to the hiring manager. One application, recorded twice.
2. **Tapcheck, 2026-04-06** — a duplicate receipt, not a second cycle. Counting rule 4 licenses a new cycle only *after* a terminal outcome on the prior one, and the decline landed the same day as this receipt. **Flagged**: the role is `unspecified` on both rows, so this cannot be fully settled from the corpus. If they turn out to be different roles it becomes two.
3. **Weave, undated** — the 2026-08-17 process was recruiter-initiated with no application behind it. It belongs to the opportunity register, not the census. The 2025-07-27 Weave application stands as its own row.
4. **Mercor, "GTM contract"** — this is the `converted_to_contract` outcome, not a separate submission. The outcome has been carried onto an existing Mercor row.

## What the census contains

| stratum | rows |
|---|---|
| Gmail / ATS sweep | 234 |
| LinkedIn, net new | 87 |

| outcome | rows |
|---|---|
| No determinate outcome yet | 121 |
| **No reply at all** | **101** |
| Rejected, no interview | 71 |
| Role paused or closed | 9 |
| Interview scheduled or held | 8 |
| Rejected after interview | 7 |
| Assessment sent | 3 |
| Converted to contract | 1 |

**286 of 321 rows carry a submission date.** 35 do not and are excluded from any time series.

## Known gaps in this number

The census is a floor, and these are the reasons — not a vague hedge:

1. **Q9 and Q10 run but not closed** — both returned at the API result ceiling, dominated by material already counted. Reaching a page limit is not reading the results. Q3b and Q6 are **closed**, and added nothing [log 050].
2. **One mailbox unswept**: `keegan@morphdatastrategies.com`. (`33@lecturesfrom.com` was dropped by the subject on 2026-08-30 and is no longer a gap.)
3. **The YC Work at a Startup inbox is unread.** It is a live channel — Hotglue came through it.
4. **Phone-arranged conversations are invisible** to both Gmail and Calendar. Two surfaced only by accident.
5. **The Gmail rows come from the logs, not from re-reading the mailbox.** They inherit whatever the logs missed, and that is known to be non-zero — Opsin had five artifacts, two with "Interview" in the subject, and appeared in no log.
6. **The Jobright stratum is missing entirely, and it is quantified. See below.**
7. **Ladders, YC WFS and Wellfound full exports** were never taken. Stop conditions 4 and 6.

## Gap 6 in full: Jobright is a hole with a known size

**Audited 2026-08-30. The 321 contains zero Jobright-sourced applications.**

What the register does contain is Jobright as an *employer* — three rows, all applications *to* Jobright.ai for its own product roles:

| company | role | applied | outcome | stratum |
|---|---|---|---|---|
| Jobright.ai | Product Manager, Entry Level | 2026-05-26 | unknown | LinkedIn, LI-048 |
| Jobright.ai | AI Engineer | 2026-06-04 | unknown | LinkedIn, LI-058 |
| Jobright.ai | Product Manager (Early Career) | undated | rejected_no_interview 2026-03-31 | gmail/ATS, logs 006 |

**No row in the census carries Jobright as a submission channel.** The codebook values `jobright_agent` (`submission_channel`) and `jobright` (`discovery_source`) exist and are used zero times.

**The size of the hole is known from [S1]'s Source Reconciliation, recorded in `01-engagement.md`:**

| channel | raw rows | new unique | dupes | out of window |
|---|---|---|---|---|
| Jobright tracker | 40 | **5** | 30 | 5 |

Those **5 Jobright-only additions were an input to the retired 247.** They were "Jobright-only" precisely because they produced no Gmail artifact and no LinkedIn row — which is why retiring the 247 removed them from the count and why the ground-up rebuild could not have recovered them. **The 321 is short by at least those 5, by construction, and their identities are not held anywhere in this project.**

Two further consequences:

- The 30 dupes were measured against the **163-row Gmail floor**, not against this project's 234-row Gmail stratum. The true overlap against the current census is unmeasured and may be smaller or larger.
- [S4] records an **agent-applied vs manual** column. If Jobright's agent submitted on the subject's behalf without generating mail to his inbox, agent-applied rows are invisible to Gmail, Calendar *and* LinkedIn simultaneously — a submission channel no instrument in this study can see. The split of the 40 rows by method is unknown.

**Required to close:** the full `jobright_applications_log.csv` export (stop condition 5), deduped against the 321 by the same set-comparison method used on LinkedIn in logs 038 and 039. This is the same class of gap the LinkedIn stratum was before its export was mined, and that one produced 87 net additions.

## Rolling count protocol

**This file is the only place a census total is stated.** Any document quoting a total cites this file and its revision.

To change the count:

1. Add a row to the changelog below with the date, the delta, and the reason.
2. Name the artifact or the adjudication that licenses it.
3. Update the header figure and the stratum table.
4. **Never adjust the total to match an external figure.** If an external source disagrees, that is a finding to investigate, not a correction to apply.

An addition needs an artifact. A removal needs an adjudication. Neither needs permission, but both need a line here.

**Corollary, established by the Jobright audit:** a known missing stratum is recorded as a sized gap, not applied as a correction. The 321 does not become 326 because [S1] says five Jobright rows existed. It becomes 326 or more when the export is in hand and the rows are named.

## Changelog

| date | delta | census | reason |
|---|---|---|---|
| 2026-08-30 | +238 | 238 | Gmail/ATS stratum extracted row-level from logs 001–034 |
| 2026-08-30 | +87 | 325 | LinkedIn net additions, 105 rows less 18 already represented [logs 038, 039] |
| 2026-08-30 | −4 | **321** | four adjudicated removals, listed above |
| 2026-08-30 | — | 321 | **the 247-row pre-sweep workbook retired as an anchor.** Ground-up count adopted |
| 2026-08-30 | +0 | **321** | Q3b and Q6 run to exhaustion, **no new applications**. First queries in the project to close without adding. Pearl's outcome recovered, Starbridge's origin upgraded to artifact [log 050] |
| 2026-08-30 | — | **321** | **Jobright audited and sized.** Zero Jobright-channel rows in the census; three Jobright-as-employer rows only. [S1] records 5 Jobright-only additions to the retired 247, which by construction are absent here. Gap recorded, **total not adjusted**. Register row counts re-verified: 321 / 234 / 87 / 298 / 35. `33@lecturesfrom.com` dropped from the gap list at the subject's instruction |
