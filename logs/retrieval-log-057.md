<!-- kit-meta
file: retrieval-log-057.md
created: 2026-08-30
source: subject confirmation (Patrick, James Pham, Mercor two interviews, Heath Mixmax conversion, Hologram two interviews); LinkedIn profile screenshots for Adam Andrewjeski and Doug Shankman
method: log recall and screenshot company identity in coding/confirmed; do not recode Freeze 1 or Freeze 2; do not merge overlay AICRO into the 298 AICRO applications
-->

# Retrieval log 057

Subject confirmation. Census remains **298**. Interviewed applications remain **14**.

## Already on the artifact record (happened)

| name | subject | artifact | overlay |
|---|---|---|---|
| Patrick / The Kiln | I interviewed with Patrick. It happened. | freeze3 e2 hiring_manager_interview. GTME Intro tok_ad8a6c7aa631 | tok_1bdfc7313b38 confirms. Does not add a round. Outside the 14. |
| James Pham / Opsin | I interviewed with James Pham. It happened. | freeze3 e2 cal_d8dafd5d42786dbb 2026-03-13 | tok_8d0c98c0fb17 confirms. Does not add a round. Outside the 14. Colossus phone round remains memory e0. |
| Hologram | I interviewed with Hologram 2 times. | Amy Schwartz recruiter_screen 2026-07-20 cal_1e35ab92e7cb411b. Derrick Calderon panel 2026-07-22 cal_7f6169cd30cea34e | tok_3c7dc3e90dd6 confirms count. Already in the 14. Does not add a round. |
| Mercor | Two interviews. Once with Claire, second with Daniel. Inbound does not change that. | Claire 2026-08-14 cal_42f37bce17b3d555. Daniel 2026-08-17 cal_9b57b2e77fc58e94. Name Daniel Luo. | tok_10c69501feb3. Later Claire 08-18 and 08-25 are not additional interviews. Outside the 14. |

## Company identity from screenshots (not invented)

| person | company | pointer | distinct from |
|---|---|---|---|
| Adam Andrewjeski | Stellar Growth (StellarGrowth, Stellargrowth.ai). Headline Founding GTM & Agency Owner. | tok_155d133e690a. Transcription `artifacts/linkedin/profile-adam-andrewjeski-stellar-growth.md` | `stellar-substitute\|unspecified\|c1` in the 298 |
| Doug Shankman | AICRO. Headline Founder & CEO at AICRO. | tok_53b6c592660c. Transcription `artifacts/linkedin/profile-doug-shankman-aicro.md` | `aicro\|gtm-engineering-team-lead\|c1` and `aicro\|gtm-engineer\|c1` in the 298 |

Overlay application ids renamed:

- `stellar-growth|informal|c1` (was `unknown|informal-adam-andrewjeski|c1`)
- `aicro|informal-cro-idea|c1` (was `unknown|cro-idea-doug-shankman|c1`)

Merging Doug into either AICRO application would attach a 2025-10-27 founder conversation to a 2026 application and move 14. Not done.

## Mixmax / Heath

Subject: I interviewed with Heath. Calendar exists. Follow-up email sent. Two-week contract then three-month contract.

This tree:

- Calendar `No Agenda Meeting with Heath` 2025-08-14 `cal_3e5387362a5b33e3`
- Welcome to Mixmax thread including SENT replies `gth_beb7124e93244a82` 2025-09-04
- Freeze 3 exclusion `marketplace_profile` stands. Not in 298. Not in the 14.

Package log 032 already recorded two-week trial from 2025-09-04 then three-month engagement to about 2025-12-22. This pass writes that sequence on this tree's overlay.

Overlay parent `mixmax|contractor-gtm|c1` and event tok_d0400dd2eab3. Origins money_kind `two_week_trial_then_three_month_contract`.

## Census lock

298. 14. `adjudication/derive_metrics.py` still ignores coder `confirmed`.
