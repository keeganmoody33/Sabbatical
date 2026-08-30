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

- Interviewed applications in the Freeze 1 221: **14**
- Application-to-interview rate on Freeze 1: 13/221
- Interviewed applications in the Freeze 2 full census: **14**
- Application-to-interview rate on the 298: 14/298
- Platform files carry no interview events. Adding LinkedIn applied-list and Jobright rows does not add interviews.
- Opportunity-register interviews (WorkOS, Mercor contract path, and other recruiter-only processes) sit outside those denominators

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
- Weave treated as recruiter-initiated with no application (Greenhouse receipt, log 002). Resolved 2026-08-30: the 2025 Business Development Manager application is real and stays in the census, rejected without interview. The separate 2026 opening is inbound with no submission artifact and sits in the opportunity register. See `paper/DEFECTS.md`.
- The Hog counted in the application-to-interview rate
