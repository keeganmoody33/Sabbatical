# Results

These are the numbers this freeze can defend. Prior-audit figures 247, 11 interviews, and 4.45 percent are not restated as findings.

No dashes are used as punctuation in this file.

## Search coverage (measured, not a census)

Harvest coverage of the frozen corpus, 2026-08-29:

- Gmail keeganmoody33@gmail.com, logs 001 to 021: 994 threads. Queries Q1 through Q5, Q3, Q4 exhausted. Q7 page 1 captured. Q7 page 2 and later, Q6, Q3b, Q9, Q10 on that mailbox were not run in this environment.
- Gmail 33@lecturesfrom.com, logs 022 to 029: 177 threads. Q6, Q7, Q3b, Q9, Q10 exhausted on this mailbox. Almost none were employment ATS receipts.
- Calendar 33@lecturesfrom.com: 31 events across five 90-day blocks with no keyword filter.
- Calendar transferred keegan@lecturesfrom.com: reachable and empty.
- Calendar keeganmoody33@gmail.com: not listed. Waived in writing.
- LinkedIn Job Applications.csv, Ladders full list, Jobright full export, YC dashboard, [S1] and [S2] workbooks: absent. Waived in writing.

Stop conditions: see `artifacts/STOP-CONDITIONS.md`. Personal Gmail Q7 is incomplete. Personal calendar is unswept.

## Completeness

95 percent completeness is a goal, not a verified claim. The intended estimator is stratified two-source capture recapture on the overlap where LinkedIn and external ATS mail could both have seen the same application.

That overlap stratum is unmeasured because Job Applications.csv is not in the corpus. No completeness percentage is published. No Lincoln Petersen estimate is computed.

Independence assumption, stated for when the export arrives: LinkedIn applied-list rows and employer ATS mail are not independent for Easy Apply, which is why that channel is excluded from the overlap stratum.

Likely bias direction if someone later runs an unstratified estimator anyway: Easy Apply is visible to LinkedIn and invisible to ATS mail, which would inflate apparent uniqueness and understate completeness.

Unmet or waived stops that bound this census: personal Gmail Q7 page 2+, Q6, Q3b, Q9; personal calendar; LinkedIn, Ladders, Jobright, YC exports; [S1] and [S2] workbooks.

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

Full census in this freeze equals that 221. There is no LinkedIn applied-list stratum to add.

Item confidence on the contributing extracts is high or medium. Population completeness is not a percentage.

## Interviews (derived, never stored)

Interviewed means at least one event whose `event_type` is in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round}.

- Interviewed applications in the 221: **14**
- Application-to-interview rate on the employer_artifact-dominated census: 14/221
- Opportunity-register interviews (WorkOS, Mercor contract path, and other recruiter-only processes) sit outside that denominator and are not mixed into 14/221

The Hog is opportunity, not an application, so its interview events do not enter the 14.

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

## What a skeptic should not be shown as a finding

- 247
- 11 interviews
- 4.45 percent
- Naive capture recapture on 17 overlap versus 163 and 99
- Mixmax product onboarding in the application denominator
- Mercor Growth Strategist contract mixed into the application denominator
- Weave treated as recruiter-initiated with no application (Greenhouse receipt, log 002)
- The Hog counted in the application-to-interview rate
