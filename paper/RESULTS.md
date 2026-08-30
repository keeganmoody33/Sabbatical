# Results

These are the numbers this freeze can defend. Prior-audit figures 247, 11 interviews, and 4.45 percent are not restated as findings.

No dashes are used as punctuation in this file.

## Search coverage (measured, not a census)

Harvest coverage of the frozen corpus, 2026-08-29:

- Gmail keeganmoody33@gmail.com, logs 001 to 021: 994 threads. Queries Q1 through Q5, Q3, Q4 exhausted. Q7 page 1 captured in Freeze 1.
- Gmail keeganmoody33@gmail.com, logs 030 to 036: Q7 re-run from start exhausted (195 unique threads). Q6, Q9, and Q3b exhausted. Pressure-test names in log 034. The Kiln in log 036.
- Gmail 33@lecturesfrom.com, logs 022 to 029: 177 threads. Q6, Q7, Q3b, Q9, Q10 exhausted on this mailbox. Almost none were employment ATS receipts.
- Calendar 33@lecturesfrom.com: 31 events across five 90-day blocks with no keyword filter.
- Calendar transferred keegan@lecturesfrom.com: reachable and empty.
- Calendar keeganmoody33@gmail.com primary: 338 events across five 90-day blocks with no keyword filter. Hidden MCAT PREP and SI CHM222 calendars were listed and not swept.
- LinkedIn applied list pages 1 to 10: 99 rows in `artifacts/platform/linkedin_applied_jobs_pages_1_to_10.csv`. Relative stamps. `date_capture = 2026-08-29`. Page 10 has 10 rows, so a later page is not ruled out. The file does not label Easy Apply versus external ATS.
- LinkedIn dated in-window extract: 105 rows in `artifacts/platform/linkedin-applications-in-window.csv`. Claude coding table from a care package, not the LinkedIn `Job Applications.csv` download. Minute timestamps. Not independently recoded into the census. See Freeze 4.
- Jobright tracker: 40 rows in `artifacts/platform/jobright_applications_log.csv`. Exact dates.
- Ladders full list, YC dashboard, [S1] and [S2] workbooks: absent. The 2026-08-30 care package did not contain them.
- LinkedIn GTME Intro screenshots (The Kiln): transcribed 2026-08-30 in `artifacts/linkedin/gtme-intro-the-kiln.md`. Not a LinkedIn data download.
- LinkedIn messages unpacking: Claude analysis of a 2026-08-23 `messages.csv` (5,262 messages, 497 conversations claimed). 54 job-related threads plus 20 uncertain, matched in `adjudication/linkedin_dm_match.csv`. Raw `messages.csv` and `Job Applications.csv` are still absent. See Freeze 4.

Stop conditions: see `artifacts/STOP-CONDITIONS.md`. Personal Gmail Q6, Q7, Q3b, and Q9 are exhausted. Personal primary calendar is swept.

## Completeness

95 percent completeness is a goal, not a verified claim. The intended estimator is stratified two-source capture recapture on the overlap where LinkedIn and external ATS mail could both have seen the same application.

That overlap stratum is still unmeasured. The LinkedIn file that arrived in Freeze 2 is pages 1 to 10 of an applied list. It does not mark which rows were Easy Apply versus an external ATS. A later 105-row dated extract from the care package is a Claude coding table, not an independently labeled channel stratum. No completeness percentage is published. No Lincoln Petersen estimate is computed.

Independence assumption: LinkedIn applied-list rows and employer ATS mail are not independent for Easy Apply, which is why that channel is excluded from the overlap stratum.

Likely bias direction if someone later runs an unstratified estimator anyway: Easy Apply is visible to LinkedIn and invisible to ATS mail, which would inflate apparent uniqueness and understate completeness.

Unmet or waived stops that still bound this census: LinkedIn pages beyond 10 and a channel-labeled ATS stratum; Ladders; YC; [S1] and [S2] workbooks. The care package did not fill those holes. Personal Gmail Q7 page 2+, Q6, Q3b, Q9, and personal calendar are no longer in that list.

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

## Freeze 3 personal mail and calendar

Gmail Freeze 1 extracts and Freeze 2 platform files were not recoded. Personal Gmail Q6, Q7, Q3b, and Q9 were run to exhaustion. The keeganmoody33 primary calendar was swept in 90-day blocks with no keyword filter (338 events).

- Net-new `register = application` rows: **0**
- Full application census remains **298**
- Net-new opportunity rows in this freeze: Pin, Hotglue BDM, Opsin, The Kiln. They stay out of the 298.
- PhrasIQ GTM Deep Dive on 2026-04-15 is now on the personal calendar. Freeze 1 had only a proposed date.
- Interviewed applications remain **14**. Pin, Hotglue, Opsin, The Kiln, The Hog, and Glytec interviews sit in the opportunity register.

Pressure-test names (origin, what happened, interviewed). Origins tagged memory are not written onto frozen `discovery_source` fields.

- Glytec: LinkedIn DMs with CEO Patrick F. Cua (messages analysis). Calendar Clayton Maike 2026-01-27. No submission receipt. **Yes, opportunity, outside the 14.**
- The Hog: invitation 2026-06-15, calendar Hudson Liao 2026-06-16, take-home after. One live interview. No ATS receipt. **Yes, opportunity, outside the 14.**
- Mixmax: No Agenda Meeting with Heath 2025-08-14, then a Mixmax service agreement. Subject calls it an interview. Overlay keeps it employment. **No. Exclusion from 298.** Not a search application.
- Every.to: thanks for applying, calendar 2026-04-21 with Austin. GTM Cafe origin is memory. Census discovery_source is unknown. **Yes, in the 14.**
- PhrasIQ: Wellfound acceptance 2026-03-31. Discovery 2026-04-02 (30 min) and Deep Dive 2026-04-15 (60 min). User named Eddie. That string is not in the frozen mail or calendar titles, so counterparty stays unknown. **Yes, in the 14.**
- Beautiful.ai: Greenhouse receipt 2026-03-08. Calendar interview 2026-03-17. Hiring manager named in follow-up is Brandon Ness. Decline 2026-03-26 from Emily. Emily is the decline sender, not the interviewer. **Yes, in the 14.**
- Pearl: Ashby receipt 2026-04-06. Calendar interviews 2026-05-05 (mail says phone) and 2026-05-18. Scheduler named in mail is Alex DeCeglie. User named Chris on the second. That string is not on the Pearl artifacts. Garrett Wolfe / GTM Cafe origin is memory. **Yes, in the 14.**
- Great Question: Ashby receipt 2026-07-17. Screening named Harri. Calendar interview 2026-07-26. Decline 2026-07-29. User named Harry. Corpus uses Harri. GTM Cafe origin is memory. **Yes, in the 14.**
- Dagster Labs: Greenhouse 2026-03-30. Delaney Housley thank-you for chatting 2026-04-03 then decline. No calendar event. Phone medium is memory. **Yes, in the 14.**
- TrueBuilt: LinkedIn applied-list GTM Engineer in Freeze 2. Posting later marked no longer accepting applications. Separate Gmail GTM project quote after a Loom, passed on budget. That project is not an interview. **Application in the 298. Not in the 14.**
- Opsin: Colossus TG prep mail 2026-03-12. Calendar Opsin Sync with James Pham 2026-03-13. User recalled a Colossus phone alignment before James. No dated artifact for that first round. Overlay logs that round as memory (`tok_b1f3dc9b0958`). No ATS receipt. **Yes, opportunity, outside the 14.**
- Hotglue: Kevin Wright BDM conversation 2026-04-20. YC Work at a Startup origin is in the meetings file. No ATS receipt. Missing from the LinkedIn 54-thread analysis. **Yes, opportunity, outside the 14.**
- Mobb / mobb.dev: Gusto first-day and a Mobb employment mailbox. Employment, not a search application.
- Pin: Erica Stacy Tarwater 2025-06-30, Conor Kline 2025-07-07, then rejection. No ATS receipt. User recalled Erika. Mail uses Erica. GTM Cafe origin is memory. **Yes, opportunity, outside the 14.**
- Mercor contract: calendar Claire 2026-08-14, Daniel 2026-08-17, Claire 08-18, Claire 08-25. Gmail names Daniel Luo, not David Lou. Instant Work Offer 2026-08-20, contract 08-21. Separate Mercor marketplace receipts stay in the 298 without interviews. **Yes, opportunity, outside the 14.**
- The Kiln: LinkedIn GTME Intro on 2026-03-04. Giorgio Zanella introduced Keegan to co-founders Patrick Spychalski and Mathias Powell. Same-day call with Patrick. User recalled two interviews including Giorgio. Giorgio's artifact role is introducer. Overlay logs Giorgio as interviewer (`tok_8c8acbc92d3c`). **Yes, opportunity, outside the 14.**
- Doug Shankman: calendar 2025-10-27, 15 min, workshop connect brainstorm. Informal interview plus CRO idea. GTM Cafe origin is memory. Overlay mints `unknown|cro-idea-doug-shankman|c1` as opportunity. Company stays unknown. **Meeting happened. Overlay opportunity. Not in the 14.**
- Jorge Macias / GTM-engineering.io: recurring calendar from 2025-07-04. GTM Engineering School TA, mentorship. **No. Communal. Not a job opportunity.**
- BCOFA: GTM strategy with Dr. Blaney 2026-03-06. Fizzled on budget. Josh Pappas is not in this tree's census files. Origins before the window stay outside harvest. **No. Consulting.**
- Adam Andrewjeski: calendar 2025-06-18. Calendly note names Clay Cafe Slack. No company. Informal interview. Overlay mints `unknown|informal-adam-andrewjeski|c1` as opportunity. Company stays unknown. **Meeting happened. Overlay opportunity. Not in the 14.**
- Kellen Casebeer: calendar 2025-06-16, thedeallab.com. Founder of Clay Cafe / gtmcafe.com and a GTM Engineering School TA. Met as Mobb prep. **No. Communal.**
- Kivira.health: GTM Overview 2026-06-03 and weekly outbound check-ins. User described a three month GTM contract via Josh Pappas. **No. Consulting. Meetings happened.**

## Freeze 4 care package

Gmail Freeze 1 extracts, Freeze 2 platform files, and Freeze 3 personal mail and calendar were not recoded. The Claude care package dropped 2026-08-30 is inventoried in `package/INVENTORY.md`. Package logs 001 to 036 are a second sequence under `package/logs/`. They are not this tree's `artifacts/gmail/` files.

- Net-new `register = application` rows: **0**
- Full application census remains **298**
- Interviewed applications remain **14**
- Opportunity register in freeze files unchanged. Adam and Doug sit in `coding/confirmed/`, not in the freeze opportunity register.

A 105-row dated LinkedIn extract arrived as a Claude coding table. Independent match against the 298: 89 overlap, one Evolution USA title typo on an existing row, three opportunity or non-census rows (BX Studio, The Hog, Colossus), twelve candidates held. No `application_id` was added. Package totals are a different assembly and are not this freeze's finding.

Jobright's four rows that a package log would add to reach a higher ledger (Axon KAE, Autodesk, MavenAI, Vanco) are already in the 298 from Freeze 2.

A LinkedIn messages analysis arrived 2026-08-30. It is a Claude coding of `messages.csv`, not the export. Independent match of 54 job-related threads and 20 uncertain threads: nine already in the 298, six already opportunity, one held application candidate (AnyInt AI), the rest exclusion, unidentifiable, or held opportunity. No `application_id` added. The Kiln Giorgio DM does not mint a second artifact interview. Overlay logs Giorgio as a memory interviewer. Hotglue is missing from the 54. Pin is missing from the 54.

VERIFY Part A is `logs/retrieval-log-052.md`. Ingest completion is `logs/retrieval-log-053.md`. Messages unpacking is `logs/retrieval-log-054.md`. Pressure-test restatement is `logs/retrieval-log-055.md`. Subject-confirmed overlay is `logs/retrieval-log-056.md`. Census still 298. Interviewed applications still 14.

## How the tally combines

The application census and the interview rate stay **298** and **14/298**. Other conversations are logged in a subject-confirmed overlay so they are traceable without entering that rate.

Four scoreboards, kept separate. Full tables and hashed pointers: `adjudication/ORIGINS.md`. Machine-readable flags: `adjudication/origins__subject_confirmed.csv`.

A. Artifact applications: 298. Interviewed applications: 14. Rate 14/298.

B. Opportunity conversations outside the 14: Glytec, The Hog, Pin, Hotglue, Opsin, The Kiln, Mercor contract, WorkOS (slot booked). Overlay adds Adam Andrewjeski and Doug Shankman with company unknown.

C. Money: Mixmax contractor GTM, Mercor hourly contract, Mobb employment, Kivira.health three month GTM. BCOFA unpaid. None of these sit in 298 or in the 14.

D. Communal: Jorge Macias, Kellen Casebeer.

If the subject says a conversation happened, it is in that overlay, tagged `evidence_system = memory` when the source is recall. That is not the same as adding it to 298. Frozen `discovery_source` is not recoded. GTM Cafe is not in this tree's codebook vocabulary.

Do not print 321 or 325 as this freeze's census. Do not print a combined conversation count as if it replaced 14/298.

## Interviews (derived, never stored)

Interviewed means at least one event whose `event_type` is in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round}.

- Interviewed applications in the Freeze 1 221: **14**
- Application-to-interview rate on Freeze 1: 14/221
- Interviewed applications in the Freeze 2 full census: **14**
- Application-to-interview rate on the 298: 14/298
- Platform files carry no interview events. Adding LinkedIn applied-list and Jobright rows does not add interviews.
- Opportunity-register interviews (WorkOS, Mercor contract path, Pin, Hotglue, Opsin, The Kiln, The Hog, Glytec, and other recruiter-only processes) sit outside those denominators
- Overlay opportunity rows (Adam, Doug) and overlay memory rounds (Opsin Colossus phone, Kiln Giorgio) also sit outside those denominators

The Hog, Pin, Hotglue, Opsin, The Kiln, and Glytec are opportunity, not applications, so those interview events do not enter the 14. Adam and Doug are overlay opportunity with no employer string, so they do not enter the 14.

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
- The Kiln counted in the application-to-interview rate
- A care-package ledger adopted as this freeze's census
- Overlay interviews (Adam, Doug, Mixmax, Opsin Colossus phone, Kiln Giorgio) mixed into 14/298
- A combined conversation count printed as if it replaced the application-to-interview rate
