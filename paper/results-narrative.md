# Results

I report measurements from this freeze. Interpretation sits in Discussion. The number ledger is `paper/RESULTS.md`. Figure IDs are in `paper/figures.md`.

The unit is applications, not companies. The census is **298 applications** at **273 companies**. A foreign ledger that spans 298 companies is a different quantity. I label the unit every time the two could collide.

## Application census

Freeze 1 locked 221 applications after two independent Gmail and Calendar extracts were adjudicated (Fig 3, Table 1). Freeze 2 mapped LinkedIn applied-list pages 1 to 10 and the Jobright tracker onto that 221 without recoding Gmail. Fifty-six platform rows overlapped Freeze 1. Net-new `platform_log` applications: **77**. Full census: **298**.

Evidence class on the 298: `employer_artifact` 220, `platform_log` 78. One of those 78 is the Freeze 1 Jobright.ai Product Manager Early Career row. The other 77 are Freeze 2. Evidence tier: A 205, B 16, C 77. The 77 Freeze 2 rows are the C stratum.

Freeze 3 (remaining personal Gmail and the keeganmoody33 primary calendar, 338 events) added **0** applications. Freeze 4 (care-package sidecar and subject-confirmed overlay) added **0** applications. Overlay rows are not copied into the 298.

Thirteen companies have more than one row, which produces 25 extra rows on top of 273 companies. DeKalb County School District is ten STAR substitute titles, all `role_lane = other`. Mercor is six marketplace evaluator and expert receipts. FOSSA and Attentive are `c1` then `c2`. Two AICRO rows are two cycles (email February 2026, LinkedIn May 2026). They are not a twin of the Doug overlay at Renoir.

`work_type = Atlanta` on three rows is a vocabulary error. I do not interpret it.

## Interviewed applications

Interviewed is derived. An application is interviewed when freeze events include at least one of `{recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round}` and that `application_id` sits in the 298. `adjudication/derive_metrics.py` reads `cursor`, `alpha`, and `bravo` only. Overlay events cannot move this count.

Interviewed applications: **14**. Rate **14/298**. On Freeze 1 only: **14/221**. On the employer-artifact stratum: **14/220**. All 14 are Freeze 1. All 14 are `employer_artifact`.

The 14, with stored `terminal_outcome` as Freeze 1 coded it:

| company | lane | interview-set events (cursor) | stored close |
|---|---|---|---|
| Beautiful.ai | unspecified | hiring_manager_interview | rejected_after_interview |
| Dagster Labs | explicit_gtm_engineering | hiring_manager_interview | rejected_after_interview |
| Every.to | explicit_gtm_engineering | hiring_manager_interview | still_open |
| Great Question | growth_demand_marketing | recruiter_screen, two hiring_manager_interview | rejected_after_interview |
| HartleyCo | explicit_gtm_engineering | recruiter_screen | rejected_after_interview |
| Hologram | explicit_gtm_engineering | recruiter_screen, panel | still_open |
| Hypergen | explicit_gtm_engineering | hiring_manager_interview | still_open |
| jobmail.io | growth_demand_marketing | recruiter_screen | rejected_no_interview |
| Orchestry | explicit_gtm_engineering | two recruiter_screen | rejected_after_interview |
| Pearl | explicit_gtm_engineering | three hiring_manager_interview | still_open |
| PhrasIQ | unspecified | two hiring_manager_interview | still_open |
| RevSpring | explicit_gtm_engineering | recruiter_screen | still_open |
| TestGorilla | explicit_gtm_engineering | recruiter_screen | still_open |
| Weave | sales_bd_partnerships | hiring_manager_interview | rejected_after_interview |

Glytec is not in the 14. Dagster, Hypergen, and Orchestry are. Opsin is opportunity and is not in the 14. Pin, Hotglue, The Hog, The Kiln, the Mercor contract path, WorkOS, Adam (Stellar Growth), and Doug (Renoir) are also outside the 14. Mixing those conversations into the numerator would replace an application-to-interview rate with a combined conversation count. I do not print that combined count as a rate.

jobmail.io is the stored-versus-derived disagreement. It is in the 14 because of a `recruiter_screen`. The stored close is `rejected_no_interview`. I disclose it. I do not recode Freeze 1 (`paper/DEFECTS.md`).

The 77 net-new Freeze 2 rows carry **zero** interview-set events (Fig 4). That sentence is about events on those 77 application rows. It is not a claim that LinkedIn produced no conversations. Melavex stays in the 298 without an interview minted. The Hog is opportunity. TrueBuilt is in the 298; the later project quote is not an interview-set event.

## Offers

Coded offers from the 298: **0** `offer_accepted` and **0** `offer_declined`.

Q11 offer-language on 33@lecturesfrom.com, including trash, found no employment offer letter. Hits were marketing plus one employment-adjacent AIT Home Delivery background-screening thread that is not an offer and is not in the 298. The authenticated mailbox for that pass was not keeganmoody33@gmail.com. The personal-mailbox offer-language family is still open. Unharvested is not empty.

The cursor `offer` event is the Mercor Instant Work Offer. That process is opportunity. The message states I did not apply directly. It does not enter 14/298.

## Freeze 1 closes

Freeze 1 coded a terminal outcome on every one of the 221 (Fig 5). The 77 platform rows are blank.

| terminal_outcome | n of 221 |
|---|---|
| rejected_no_interview | 73 |
| rejected_after_interview | 6 |
| role_paused_or_closed | 18 |
| still_open | 124 |

Zero `no_response`. Amendment A2 (outbound-anchor silence) was not applied. The 124 are not a ghosting count. `evidenced_silence_days` is uncomputable on this freeze.

A reply statistic, if used, is defined on Freeze 1 only: 73 of 221 received an explicit decline before interview. I do not mix the 77 blank outcomes into a percent over 298.

Of the 14 interviewed applications, six are `rejected_after_interview`, seven are `still_open`, and one is the jobmail.io disagreement above.

## Role lanes

Cohen's kappa on `role_lane` for the Freeze 1 intersection (n = 211 matched keys) is 0.9510. That kappa licenses lane counts on the 221. Freeze 2 is a documented column mapping. Kappa is not recomputed on the 77.

Table 1. Role lane, Freeze 1 (n = 221) and full census (n = 298). See Fig 3.

| role_lane | Freeze 1 | Freeze 2 add | full 298 |
|---|---|---|---|
| explicit_gtm_engineering | 86 | 27 | 113 |
| unspecified | 35 | 0 | 35 |
| sales_bd_partnerships | 28 | 6 | 34 |
| growth_demand_marketing | 22 | 10 | 32 |
| sales_solutions_engineering | 15 | 16 | 31 |
| other | 18 | 12 | 30 |
| revops_gtm_ops_strategy | 9 | 5 | 14 |
| product_ai_technical | 8 | 1 | 9 |

Interviewed applications by Freeze 1 lane:

| role_lane | interviewed / Freeze 1 n |
|---|---|
| explicit_gtm_engineering | 9/86 |
| unspecified | 2/35 |
| growth_demand_marketing | 2/22 |
| sales_bd_partnerships | 1/28 |
| sales_solutions_engineering | 0/15 |
| other | 0/18 |
| revops_gtm_ops_strategy | 0/9 |
| product_ai_technical | 0/8 |

GTM modifiers among the 86 Freeze 1 explicit GTM rows: plain 55, systems/operations 11, founding/senior/lead 7, AI/product/vertical 7, sales/presales 4, growth/marketing 2. Among the 113 in the 298: plain 71, founding/senior/lead 15, systems/operations 11, AI/product/vertical 8, sales/presales 4, growth/marketing 4.

## Monthly series, exact dates only

Monthly charts use `date_precision = exact` only. Relative LinkedIn stamps are not upgraded. Evidence-bound dates are printed as the companion count, not plotted as if they were exact.

Freeze 1: n exact = 195, n not exact = 26 (Fig 1). Full 298: n exact = 201, n not exact = 97, of which 71 are LinkedIn `relative_display` (Fig 2).

| month | Freeze 1 exact | full 298 exact |
|---|---|---|
| 2025-06 | 5 | 5 |
| 2025-07 | 19 | 19 |
| 2025-08 | 16 | 16 |
| 2025-09 | 0 | 0 |
| 2025-10 | 0 | 0 |
| 2025-11 | 1 | 1 |
| 2025-12 | 2 | 2 |
| 2026-01 | 7 | 9 |
| 2026-02 | 10 | 10 |
| 2026-03 | 21 | 21 |
| 2026-04 | 26 | 26 |
| 2026-05 | 22 | 24 |
| 2026-06 | 28 | 30 |
| 2026-07 | 33 | 33 |
| 2026-08 | 5 | 5 |

Peak month on both series is 2026-07 at 33 exact. Freeze 2 added six exact Jobright dates: two in 2026-01, two in 2026-05, two in 2026-06. The 71 LinkedIn relative stamps stay off both charts.

Zero exact rows in 2025-09 and 2025-10 is not a claim of zero search activity. Fullsteam 2025-09-29 is `evidence_bound`.

## Money, listed beside the rate

Money is a separate scoreboard (Fig 6). It is not mixed into 14/298.

Paid in the working record, all outside the 14:

- Mixmax: interview, then a two-week trial, then a three-month contractor GTM engagement. Employment/consulting. Freeze 3 exclusion from 298 stands.
- Mercor hourly contract: Claire then Daniel Luo. Opportunity. Instant Work Offer states I did not apply directly.
- Mobb: employment onboarding. Not a search application.
- Kivira.health: three-month GTM consulting.

BCOFA was unpaid and fizzled. TrueBuilt is in the 298; the later project quote is not paid and is not an interview.

Mercor marketplace evaluator and expert receipts (six rows) sit in the 298. They carry no interview-set events and did not convert. The paid Mercor path is the opportunity contract, not those marketplace rows. Do not write that none of the money is in 298. Do not write that the marketplace rows converted.

Names in this working record still need a publication naming pass.

## Four scoreboards, not one rate

A. Artifact applications: 298. Interviewed applications: 14. Rate 14/298.

B. Opportunity conversations outside the 14, including overlay: Glytec, The Hog, Pin, Hotglue, Opsin (James happened; Colossus phone is memory), The Kiln (Patrick happened; Giorgio as interviewer is memory), Mercor contract, WorkOS, Adam at Stellar Growth, Doug at Renoir on 2025-10-27 (meeting predates AICRO).

C. Money: Mixmax, Mercor contract, Mobb, Kivira.health. BCOFA unpaid. Mercor marketplace in 298 without conversion. TrueBuilt in 298, quote not paid.

D. Communal, not jobs: Jorge Macias, Kellen Casebeer.

If I say a conversation happened, it is in the overlay, tagged memory when the source is recall. Happened is not `register = application`. Frozen `discovery_source` is not recoded. GTM Cafe is not in this codebook.

<!-- claims
| # | quantity as written | value | source | tier |
|---|---|---|---|---|
| 1 | applications | 298 | adjudication/applications__full_census.csv | measured |
| 2 | companies on those applications | 273 | same CSV, distinct company_canonical | measured |
| 3 | Freeze 1 applications | 221 | adjudication/applications__adjudicated.csv | measured |
| 4 | Freeze 2 net-new | 77 | adjudication/FREEZE-2.md | measured |
| 5 | interviewed applications | 14 | cursor events intersect 298; derive_metrics.py | measured |
| 6 | rate | 14/298 and 14/221 and 14/220 | same | measured |
| 7 | coded offers on 298 | 0 | terminal_outcome on census; Q11 log 059 | measured |
| 8 | Freeze 1 closes | 73 / 6 / 18 / 124 | applications__adjudicated.csv terminal_outcome | measured |
| 9 | role_lane 221 | GTM 86, unspecified 35, sales/BD 28, growth 22, other 18, solutions 15, RevOps 9, product/AI 8 | same, kappa 0.9510 | measured |
| 10 | role_lane 298 | GTM 113 | full census CSV; no second kappa | measured |
| 11 | Freeze 1 exact dates | 195 exact, 26 not exact | date_precision on 221 | measured |
| 12 | full 298 exact dates | 201 exact, 97 not exact, 71 relative_display | full census CSV | measured |
| 13 | 2026-07 peak | 33 exact | same | measured |
| 14 | Freeze 2 interview-set events on the 77 | 0 | freeze events | measured |
| 15 | jobmail.io stored close | rejected_no_interview while in the 14 | census row plus cursor recruiter_screen | measured |
| 16 | completeness percent | not printed | paper/DEFECTS.md | unknown |
| 17 | money names | Mixmax, Mercor contract, Mobb, Kivira.health | adjudication/ORIGINS.md | measured, naming pass required |
| 18 | Mercor marketplace in 298 | 6 rows, no conversion | full census, company Mercor | measured |
-->
