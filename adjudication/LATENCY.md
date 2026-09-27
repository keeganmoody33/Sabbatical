# Response latency

Secondary outcomes named in `knowledge/protocol.md`, computed under the rule stated there: only rows where both dates carry `precision = exact`, with the excluded n reported alongside. This executes the pre-registration and does not deviate from it.

## Base population

- Adjudicated application census: 223
- With an exact-dated `submission_receipt`, the base for every figure below: 197
- Excluded for lacking one: 26

The base is not the census. Any rate below is stated against 197, and the published application-to-interview rate remains 10/223.

## Response rate and latency are separate

- Substantive response, `employer_ack` excluded: 76/197
- Any response, `employer_ack` included: 99/197
- No response at all beyond the receipt: 98/197

The medians below are conditional on having responded. They describe responders only and must not be quoted as a typical response time for an application.

| definition | n | median | p25 | p75 | mean | max | day zero |
|---|---|---|---|---|---|---|---|
| substantive, headline | 76 | 7 | 3 | 19 | 15.1 | 140 | 9 (11.8%) |
| any, includes ack | 99 | 5 | 1 | 15 | 13.0 | 140 | 22 (22.2%) |

The day-zero share roughly doubles when `employer_ack` is included, which is what an automated acknowledgment arriving with the receipt looks like. The substantive figure is the headline for that reason. The distribution is right-skewed in both cases, mean well above median, so the median is the statistic to quote.

## Time to first interview

- n = 7, median 5 days, mean 7.3, range 0 to 24

What follows is about the interview set rather than the latency arithmetic, because this figure inherits whatever that set gets wrong.

**Excluded by named adjudication decision.** These events are removed from this figure and from the census interview count, and the reason is recorded rather than the event silently disappearing:

- `weave|business-development-manager|c1`, `hiring_manager_interview` dated 2026-08-18. Belongs to a separate inbound Weave process, not this application. gth_0339a17e3860d167 is a post-interview decline, so an interview did happen, but the BDM application was already rejected 2025-07-31. Bravo excluded this artifact during blind coding as having no parent.
- `hypergen|gtm-engineer|c1`, `hiring_manager_interview` dated 2026-04-14. An interview INVITATION from people@hypergen.io replying to the March 11 confirmation, with nothing after it. Flagged at retrieval time: retrieval-log-006 records that the prior ledger held Hypergen as a receipt only and that the Interviews sheet does not list it. Bravo blind-coded the same artifact `employer_ack`; cursor is the lone outlier and adjudication took cursor.
- `testgorilla|go-to-market-engineer|c1`, `recruiter_screen` dated 2026-02-20. A recruiter INTRO message, alongside an assessment invitation the same day and a recruiter update on 2026-04-23. No scheduling artifact, no completion signal, no SENT reply. Both coders made this call, which is why it is recorded as a missing codebook rule rather than a coder error.
- `jobmail-io|growth-lead|c1`, `recruiter_screen` dated 2026-07-13. The decline credits 'completing the requested steps through' a named party that is an AUTOMATED SCREENING PRODUCT, not a person at the employer: the sending address and the reply-to both belong to that product rather than to the hiring company. The steps were therefore asynchronous and machine-administered. Kept at Freeze 4 as ambiguous on the retrieval note alone; resolved when the author supplied the decline itself. Also the row carrying the standing contradiction between a derived interview and a stored `rejected_no_interview`, from one coder with no blind second reading.
- `revspring|lead-agentic-operations-gtm-engineering|c1`, `recruiter_screen` dated 2026-06-10. A Recruiter Screen REQUEST. The surrounding thread is two submission receipts and two employer acknowledgments, with no scheduling artifact and no completion signal. Both coders made this call.

**Provenance.** The census records 10 interviewed applications. Both coders independently found 9. The remaining 1 rest on cursor alone, and bravo contributes none that cursor missed: `hartleyco|founding-gtm|c1`. Agreement on which applications were interviewed is therefore 9/10, which is much weaker than the published role-lane kappa of 0.9510 implies. Event-level agreement is not among the reliability statistics `knowledge/protocol.md` requires, so this is unmeasured rather than measured and small.

No interview event postdates a rejection on the same application.

## Right censoring

Applications submitted near the 2026-08-29 window end have had less time to draw a response. The rate is stable across exposure windows, so censoring is not driving it.

| minimum exposure | base n | responded | rate |
|---|---|---|---|
| 0 days | 197 | 99 | 0.503 |
| 14 days | 193 | 96 | 0.497 |
| 30 days | 192 | 96 | 0.500 |
| 60 days | 159 | 84 | 0.528 |
| 90 days | 131 | 65 | 0.496 |

Applications with under 30 days of exposure: 5.

## Slices, cells under 5 suppressed

Median days to any response, `employer_ack` included, so the cells are as populated as the data allows. Suppressed groups are named with their counts rather than dropped silently.

### By role lane

| role_lane | n | median days |
|---|---|---|
| explicit_gtm_engineering | 45 | 6 |
| sales_bd_partnerships | 16 | 3.5 |
| unspecified | 8 | 8 |
| growth_demand_marketing | 8 | 5.5 |
| sales_solutions_engineering | 7 | 7 |
| revops_gtm_ops_strategy | 6 | 3 |
| other | 5 | 7 |

Suppressed, 1 of 8 groups: product_ai_technical (n=4).

### By ATS

| ats_system | n | median days |
|---|---|---|
| Greenhouse | 28 | 10 |
| none_observed | 25 | 4 |
| Ashby | 25 | 5 |
| Workable | 6 | 0 |

Suppressed, 9 of 13 groups: Rippling (n=4), Lever (n=2), Teamtailor (n=2), Workday (n=2), Comeet (n=1), iCIMS (n=1), Recruitee (n=1), Breezy (n=1), Gem (n=1).

### By month applied

| month | n | median days |
|---|---|---|
| 2026-06 | 19 | 3 |
| 2026-03 | 14 | 6.5 |
| 2026-04 | 13 | 16 |
| 2026-07 | 12 | 3 |
| 2026-05 | 11 | 7 |
| 2025-07 | 9 | 3 |
| 2025-08 | 7 | 10 |
| 2026-02 | 5 | 1 |

Suppressed, 4 of 12 groups: 2026-01 (n=3), 2026-08 (n=3), 2025-12 (n=2), 2025-06 (n=1).

The ATS table is the one to read carefully. Most systems in this corpus appear too few times to support a median, so the published rows are a minority of the systems observed and are not a ranking of ATS platforms.

