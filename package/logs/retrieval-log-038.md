# Retrieval log 038

**The LinkedIn dedupe, resolved.** The blocking task named in logs 035 and 037 is closed. Also: codebook rev 2 in force, and a method change that must be disclosed.

## Method change, disclosed

Log 037 scoped the dedupe as "roughly ten batched Gmail queries at ten companies per query." **That method was attempted and abandoned.** Three query shapes were run against the study window: bare `{company OR company...}`, the same with `in:anywhere`, and the same with a twenty-domain newsletter exclusion list. All three returned `resultCountEstimate` at the 201 ceiling, dominated by newsletter text. The cause is structural: the LinkedIn company set contains ordinary English words — *gigs*, *applause*, *swarm*, *propel*, *massive*, *2X*, *Vi* — and full-text Gmail search cannot separate a company name from a word. One live example: `closedwon` matched twenty-plus issues of a sales newsletter at `eml_438ca90753f4`, an entity unrelated to ClosedWon Talent.

**Method used instead: set comparison against the existing corpus.** The Gmail employer-artifact layer is already exhausted for Q1, Q2a-d, Q3, Q4, Q5, Q7, Q7b — 1,152 threads across logs 001 to 025, plus calendar and subject-supplied material in 026 to 034. Every company holding an employer artifact was already extracted into those logs. The 98 distinct LinkedIn companies were compared against that roster.

**Why this is the better instrument, not just the cheaper one.** The abandoned method would have run a *second, noisier* retrieval over ground the first sweep already covered exhaustively, and any disagreement between the two would have been a property of the query, not of the corpus. The set comparison asks the question the census actually needs answered: does this company appear anywhere in the swept artifact layer.

**Limit, stated.** This inherits the completeness of logs 001 to 034. A company holding an artifact that the Gmail sweep missed will read as `net_new` here. Q3b, Q6, Q9, Q10 and Q8 blocks 4 to 6 are unexhausted, so a later sweep can flip a row from `net_new` to duplicate. **The count below is therefore an upper bound on net additions and a lower bound on overlap.** It is not final until those queries close.

## Result

| dedupe_status | rows |
|---|---|
| `net_new` | 80 |
| `duplicate_gmail_receipt` | 17 |
| `unresolved` | 4 |
| `net_new_employer_artifact_exists` | 3 |
| `distinct_cycle_net_new` | 1 |
| **total** | **105** |

**Measured overlap: 17 of 105, 16.2 percent.** Written to `linkedin-dedupe-resolution.csv`, one row per LinkedIn application, joining to `linkedin-applications-in-window.csv` on `linkedin_row_id`. A separate resolution table rather than a rewritten source table, so the extract stays as retrieved.

The 17 duplicate rows span 16 companies: Gigs, Applause, proteanTecs, Verkada, DISQO, PandaDoc, Crossing Hurdles, AppGate, Auctane, Wall Street Quants, Adaptive6, Huzzle, Armada, Attentive, Jobgether, and talentpluto, which contributes two distinct rows on the same day.

**Thirteen of the seventeen carry a Gmail receipt dated the same day as the LinkedIn timestamp; fifteen fall within one day.** That is strong evidence the two sources are recording one event rather than two submissions. The two outliers, proteanTecs at four days and DISQO at four days, are matched on company and role and should be adjudicated rather than assumed.

## The finding this produces

**The two sources are structurally near-disjoint, and now that is measured rather than asserted.**

`protocol.md` predicted this and used it to reject naive Lincoln-Petersen. The prediction holds at 16.2 percent overlap. But the prediction had a consequence the protocol did not follow through: the pre-registered capture-recapture method restricts the estimate to *LinkedIn rows submitted through an external ATS rather than Easy Apply*, because only there could both sources have observed the same application.

The 17 duplicates **are** that stratum, empirically identified. They are the LinkedIn rows that generated ATS mail. This gives the estimator a real, measured stratum for the first time instead of an assumed one — and it simultaneously falsifies the blanket `submission_channel = linkedin_easy_apply` assignment on all 105 rows, since a row that produced a Workable or Greenhouse receipt was not an Easy Apply. See integrity defect 4 in `protocol.md`.

## Three rows that are not duplicates and matter more than the duplicates

`net_new_employer_artifact_exists`: **Bask Health (LI-033), BX Studio (LI-036), The Hog (LI-054).**

Each has employer correspondence in Gmail — outreach, a hiring-manager thread, a full interview-plus-take-home sequence — and **no submission receipt anywhere**. The application exists only in the LinkedIn export. Without the export these three processes were attached to nothing.

The Hog is the sharpest case: it is one of the eleven in-census interviews, and until now the row it belongs to had no submission evidence at all.

**Consequence for the codebook:** all three move from `evidence_class = platform_log` to `employer_artifact`. That is the stratum the sensitivity analysis runs on, so this is not bookkeeping.

## Four unresolved, listed so they are not lost

1. **LI-014, Insignia.** LinkedIn says "Insignia Assets," 2025-11-18, Easy Apply. Log 020 says "Insignia Collab," 2025-11-18, direct emailed application with resume. Same date, different name, different channel. One event recorded twice under two names, or two separate submissions. **Do not merge without the artifact.**
2. **LI-048, Jobright.ai.** Product Manager, Entry Level, 2026-05-26. Log 006 has Product Manager, Early Career, 2026-03-31. Same role renamed in a second cycle, or one process with a late platform stamp.
3. **LI-058, Jobright.ai.** AI Engineer, 2026-06-04, no Gmail match. Resolve with LI-048 once the Jobright tracker is exported — stop condition 5.
4. **LI-097, HartleyCo.** Log 012 has recruiter outreach 2026-07-13 referencing a GTM Engineer application for an unnamed San Francisco client; logs 018 and 020 tie HartleyCo to the Bluejay Founding GTM process. The reconciled ledger already carries a HartleyCo interview. **Live double-count risk.** Adjudicate before any census total is published.

## What this does and does not license

**Does:** the LinkedIn stratum is now dedupe-resolved, so stop condition 8 is met for the four sources swept to date. Net additions from LinkedIn are **84**, held to that figure pending the four unresolved rows and the unexhausted queries.

**Does not:** state a census total. Q3b, Q6, Q9, Q10 and Q8 blocks 4 to 6 remain open, and the four unresolved rows sit on the boundary. A total published now would be a total for the corpus as swept, not for the window.

## One thing the export shows that the census cannot

Attentive has **two** cycles in Gmail — a receipt 2026-06-22, a decline 2026-07-07, a second receipt 2026-07-15. The LinkedIn export carries **only the first**. The export was generated 2026-08-19 and should have caught both. Either the second cycle was submitted off-platform, or the LinkedIn applied list is not complete for the window. That bears directly on stop condition 3, which asks whether the LinkedIn applied list is complete and currently assumes the export settles it. **It does not.**

## Codebook rev 2, in force

Amendments A1 to A4 applied 2026-08-30, before coder 1 and before any Table 1 row existed. Logged in `protocol.md` as pre-registration revision 1, not a deviation. Rationale in `claude/05-codebook-amendments-r1.md`. Two corrections to the record: `no_response` and `reschedule` were already in the vocabularies; logs 036 and 037 recorded them as missing in error.

## Open

- Adjudicate the four unresolved rows.
- `submission_channel` on all 105 rows: non-conforming value, and now falsified for at least 17 of them. Integrity defect 4.
- Attentive second cycle: does the LinkedIn export miss applications, and if so how many.
- Triage the 114 inbound LinkedIn conversations.
- `Invitations.csv`, Saved Jobs, screening-question responses: unexamined.
- Q3b, Q6, Q9, Q10; Q8 blocks 4 to 6; Q12 pagination.
- Five engagement descriptions. Still blocking Methods.
