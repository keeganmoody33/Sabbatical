# Results

> **Superseded at Freeze 3, 2026-08-30.** Every figure below is the Freeze 2 state: census 221,
> 13/221, full census 298, latency base 196. The current numbers are 223, 10/223, 317 and 197.
> `paper/PAPER.md` and `paper/COMPANION.md` supersede this file. It is kept as the internal record
> of what Freeze 2 could defend, not deleted, because the point of the repository is that a
> superseded number stays visible with its date on it.

These are the numbers this freeze can defend. Prior-audit figures 247, 11 interviews, and 4.45 percent are not restated as findings.

No dashes are used as punctuation in this file.

## Search coverage (measured, not a census)

Harvest coverage of the frozen corpus, 2026-08-29:

- Gmail keeganmoody33@gmail.com, logs 001 to 021: 994 threads. Queries Q1 through Q5, Q3, Q4 exhausted. Q7 page 1 captured. Q7 page 2 and later, Q6, Q3b, Q9, Q10 on that mailbox were not run in this environment.
- Gmail 33@lecturesfrom.com, logs 022 to 029: 177 threads. Q6, Q7, Q3b, Q9, Q10 exhausted on this mailbox. Almost none were employment ATS receipts.
- Calendar 33@lecturesfrom.com: 31 events across five 90-day blocks with no keyword filter.
- Calendar transferred keegan@lecturesfrom.com: reachable and empty.
- Calendar keeganmoody33@gmail.com: not listed. Waived in writing.
- LinkedIn applied list pages 1 to 10: 99 rows in `artifacts/platform/linkedin_applied_jobs_pages_1_to_10.csv`. Relative stamps. `date_capture = 2026-08-29`. Page 10 has 10 rows, so a later page is not ruled out. The file does not label Easy Apply versus external ATS.
- Jobright tracker: 40 rows in `artifacts/platform/jobright_applications_log.csv`. Exact dates.
- Ladders full list, YC dashboard, [S1] and [S2] workbooks: absent.

Stop conditions: see `artifacts/STOP-CONDITIONS.md`. Personal Gmail Q7 is incomplete. Personal calendar is unswept.

## Completeness

95 percent completeness is a goal, not a verified claim. The intended estimator is stratified two-source capture recapture on the overlap where LinkedIn and external ATS mail could both have seen the same application.

That overlap stratum is still unmeasured. The LinkedIn file that arrived is pages 1 to 10 of an applied list. It does not mark which rows were Easy Apply versus an external ATS. No completeness percentage is published. No Lincoln Petersen estimate is computed.

Independence assumption: LinkedIn applied-list rows and employer ATS mail are not independent for Easy Apply, which is why that channel is excluded from the overlap stratum.

Likely bias direction if someone later runs an unstratified estimator anyway: Easy Apply is visible to LinkedIn and invisible to ATS mail, which would inflate apparent uniqueness and understate completeness.

Unmet or waived stops that still bound this census: personal Gmail Q7 page 2+, Q6, Q3b, Q9; personal calendar; LinkedIn pages beyond 10 and a channel-labeled ATS stratum; Ladders; YC; [S1] and [S2] workbooks.

## Pre-adjudication agreement

Two independent extracts: `bravo` and `cursor`. Alpha CSVs were not on disk for this pass.

Raw match key `company_canonical|role_as_listed|cycle`:

- bravo n = 228
- cursor n = 231
- intersection = 211
- role_lane percent agreement = 0.9621
- role_lane Cohen's kappa = 0.9510
- include percent agreement = 0.9905
- include kappa = 0.7452 (two disagreements: The Hog and BX Studio)

## Adjudicated application census

Confirmed applications, `register = application`, after include/exclude adjudication and alias merge: **221**.

Evidence class:

- employer_artifact: 220
- platform_log: 1 (Jobright.ai Product Manager Early Career)

Full census in Freeze 1, before platform files, equals that 221.

## Freeze 2 platform addendum

Gmail and Calendar extracts were not recoded. LinkedIn pages 1 to 10 and the Jobright tracker were coded as `platform_log` and matched to Freeze 1 on `company_canonical + role_as_listed + cycle`. Titles that expand or abbreviate an existing Freeze 1 role at the same company (AE vs Account Executive, location parentheticals) are the same application. They do not increment the census.

LinkedIn `submission_channel` is `unknown`. The applied-list file does not label Easy Apply versus external ATS.

- Platform rows overlapping Freeze 1: 56
- Net-new `platform_log` applications: **77**
- Full census (Freeze 1 plus net-new): **298**
- Evidence class on the 298: employer_artifact 220, platform_log 78
- One LinkedIn row with a blank company was excluded (`unresolvable_identity`)
- The Hog LinkedIn row stays opportunity, matching Freeze 1

Thomson Reuters AE Tax or Risk, Foursquare AE New Business, UpGuard SDR Manager, Verkada Enterprise Solutions Engineer Atlanta, and Listen Labs Lead GTM Engineer (LinkedIn lists Listen) were already in the 221. Jobright and LinkedIn titles for those openings are overlap, not net-new.

This is a documented column mapping of structured applied lists, not a second independent LLM pair. Role-lane kappa is not recomputed on the 77.

Ladders is still absent.

## Interviews (derived, never stored)

Interviewed means at least one event whose `event_type` is in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round}.

- Interviewed applications in the Freeze 1 221: **13**
- Application-to-interview rate on Freeze 1: 13/221
- Interviewed applications in the Freeze 2 full census: **13**
- Application-to-interview rate on the 298: 13/298
- Platform files carry no interview events. Adding LinkedIn applied-list and Jobright rows does not add interviews.
- Opportunity-register interviews (WorkOS, Mercor contract path, Weave 2026, and other recruiter-only processes) sit outside those denominators

The Hog is opportunity, not an application, so its interview events do not enter the 13.

Both coders independently found 10 of the 13. Three rest on cursor alone, and bravo contributes none that cursor missed. Agreement on the interview set is therefore 10/13, weaker than the role-lane kappa of 0.9510 suggests. Event-level agreement is not among the reliability statistics the protocol requires, so it is unmeasured rather than measured and small. See `adjudication/LATENCY.md`.

One event was removed from this count by named adjudication decision on 2026-08-30: a Weave `hiring_manager_interview` that belonged to a separate 2026 opening, not to the 2025 application it was attached to. That opening is inbound with no submission artifact, so it sits in the opportunity register. See `paper/DEFECTS.md`.

## Response latency (`precision = exact` on both dates)

Secondary outcomes named in the protocol, computed under the rule stated there. Full tables in `adjudication/LATENCY.md`, row-level data in `adjudication/latency__by_application.csv`.

### Base

196 of the 221 carry an exact-dated `submission_receipt`. That is the denominator for every figure in this section. The 25 without one are excluded and must be printed alongside, the same way the 26 non-exact dates are printed beside the monthly series.

The base is not the census. The application-to-interview rate stays 13/221.

### Rate and latency are reported separately

- Substantive response, `employer_ack` excluded: 79/196
- Any response, `employer_ack` included: 100/196
- No response beyond the receipt: 96/196

Roughly half of all applications produced a receipt and then nothing.

The medians below are conditional on having responded. They describe responders only. A single "typical response time" that folded in the 96 silent applications would drop them from the denominator, which is the same error the two-register rule exists to prevent on the interview rate.

| definition | n | median | p25 | p75 | mean | max | day zero |
|---|---|---|---|---|---|---|---|
| substantive, headline | 79 | 7 | 3 | 19 | 15.1 | 140 | 9 (11.4 percent) |
| any, includes ack | 100 | 5.5 | 1 | 15 | 12.8 | 140 | 22 (22.0 percent) |

Two definitions are published because the choice moves the number. The day-zero share doubles when `employer_ack` is counted, which is what an automated acknowledgment arriving with the receipt looks like. The substantive figure is the headline for that reason. Both distributions are right-skewed, mean well above median, so the median is the statistic to quote.

### Time to first interview

n = 11, median 6 days, mean 8.8, range 0 to 34. Small, and it inherits whatever the interview set gets wrong. See the agreement note above.

### Right censoring is not driving the rate

Applications submitted near the window end have had less time to draw a response. The rate is stable across exposure windows, so the response rate is not an artifact of the cutoff.

| minimum exposure | base n | responded | rate |
|---|---|---|---|
| 0 days | 196 | 100 | 0.510 |
| 30 days | 191 | 97 | 0.508 |
| 60 days | 158 | 84 | 0.532 |
| 90 days | 130 | 65 | 0.500 |

Five applications have under 30 days of exposure.

### Slices, cells under 5 suppressed

Median days to any response. Suppressed groups are named with their counts rather than dropped silently.

By role lane, 7 of 8 groups reach n = 5: explicit_gtm_engineering 43 at 5 days, sales_bd_partnerships 15 at 3, unspecified 11 at 8, growth_demand_marketing 9 at 6, sales_solutions_engineering 7 at 7, revops_gtm_ops_strategy 6 at 3, other 5 at 7. Suppressed: product_ai_technical (n=4).

By month applied, 8 of 12 groups reach n = 5. Suppressed: 2026-01 (n=3), 2026-08 (n=3), 2025-12 (n=2), 2025-06 (n=1).

By ATS, only 4 of 13 groups reach n = 5: Greenhouse 28 at 10 days, none_observed 26 at 4.5, Ashby 25 at 5, Workable 6 at 0. Nine systems are suppressed at n = 1 to 4. **The published rows are a minority of the systems observed and are not a ranking of ATS platforms.** Anyone reading a per-ATS response time out of this table is reading four cells and nine absences.

### What this section does not support

Discovery source is `unknown` on 206 of the 221, and the 78 rows that do know their source carry one terminal outcome between them, because platform exports contain no events. No claim about which platform or job board produced faster or better responses is available from this data, and none is made.

## Role lane (after kappa)

Kappa on the intersection is 0.9510. Lane counts on the 221, using the adjudicated row's `role_lane` (cursor title when keys were merged):

- explicit_gtm_engineering: 86
- unspecified: 35
- sales_bd_partnerships: 28
- growth_demand_marketing: 22
- other: 18
- sales_solutions_engineering: 15
- revops_gtm_ops_strategy: 9
- product_ai_technical: 8

## Monthly series (`date_precision = exact` only)

n exact = 195. n not exact = 26. The 26 must be printed next to any chart.

Exact-date counts: 2025-06 5, 2025-07 19, 2025-08 16, 2025-09 0, 2025-10 0, 2025-11 1, 2025-12 2, 2026-01 7, 2026-02 10, 2026-03 21, 2026-04 26, 2026-05 22, 2026-06 28, 2026-07 33, 2026-08 5.

Zero exact rows in September and October 2025 is not a claim of zero search activity. Fullsteam 2025-09-29 is evidence_bound. Prior audits that treated Q1 as about one row were looking at a search-boundary artifact.

## Defects

1. WorkOS: closed as opportunity. TopHire recruiter path, 2025-08-25. No submission receipt.
2. 212 to 163: still undocumented. Workbooks absent.
3. Cycle is in the key. FOSSA c1/c2 and Attentive c1/c2 are separate rows.
4. Weave 2026 interview: closed 2026-08-30. Attached to the wrong application, corrected by named adjudication decision. Interviews 14 became 13. The correction came from the author, from recall, which is disclosed rather than smoothed. Bravo had independently excluded the same artifact under blind conditions.

## What a skeptic should not be shown as a finding

- 247
- 11 interviews
- 4.45 percent
- Naive capture recapture on 17 overlap versus 163 and 99
- Mixmax product onboarding in the application denominator
- Mercor Growth Strategist contract mixed into the application denominator
- Weave treated as recruiter-initiated with no application (Greenhouse receipt, log 002). Resolved 2026-08-30: the 2025 Business Development Manager application is real and stays in the census, rejected without interview. The separate 2026 opening is inbound with no submission artifact and sits in the opportunity register. See `paper/DEFECTS.md`.
- The Hog counted in the application-to-interview rate
