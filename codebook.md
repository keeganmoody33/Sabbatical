# Codebook

Self-contained. Everything a coder needs is in this file.

The logging schema for the Sabbatical dataset. Field definitions and controlled vocabularies. Changes to this file invalidate prior rows, so change it deliberately and log it.

## Six design principles

1. **Store observations, compute rollups.** `interviewed` and `rounds` are never fields. They are derived from the events table. A stored rollup and a stored event list will eventually disagree, and then neither is trustworthy.
2. **One row per application cycle, with cycle in the key.** A genuine re-application after a closed first attempt is a second row, not an overwrite. Without cycle in the key the two collide.
3. **Origin is three fields, not one.** Where the role was found, how the application was submitted, and where the evidence lives are independent. Collapsing them into one string makes it impossible to compare channels later.
4. **Every date carries a precision label and an anchor.** A relative stamp is only interpretable next to the date it was captured.
5. **Register is a field, not a separate sheet.** Moving rows between sheets loses history. Filter on `register` instead.
6. **Controlled vocabularies everywhere except `notes`.** Free text is where reproducibility dies.

## Table 1: applications

One row per application cycle.

| field | type | definition |
|---|---|---|
| `coder_id` | string | Independent coder who produced the row. Assigned, not derived. |
| `application_id` | key | `company_slug\|role_slug\|c{n}`, e.g. `fossa\|gtm-engineer\|c2` |
| `cycle` | int | 1 for first submission. Increment only after a terminal outcome on the prior cycle. |
| `company_canonical` | string | Normalized. DISQO, not DSQO. Anysphere, not Cursor, with the alias in notes. |
| `company_as_listed` | string | Verbatim from the source. Never overwritten. |
| `underlying_employer` | string | For intermediaries. HartleyCo, WilsonHCG, Jobgether, Talentpluto. `unknown` if not named. |
| `role_as_listed` | string | Verbatim. `unspecified` when the receipt omits it. Never inferred. |
| `role_lane` | enum | See vocabulary below. One lane, mutually exclusive. |
| `gtm_modifier` | enum | Only when `role_lane = explicit_gtm_engineering`. |
| `date_applied` | date | Best available submission date. |
| `date_precision` | enum | `exact`, `relative_display`, `evidence_bound`, `unknown` |
| `date_capture` | date | Required when precision is `relative_display`. The date the "1mo ago" stamp was read. |
| `date_evidence_anchor` | date | Required when precision is `evidence_bound`. The artifact date that bounds the submission, e.g. Fullsteam 2025-09-29. |
| `discovery_source` | enum | Where the role was found. |
| `submission_channel` | enum | How the application was sent. |
| `ats_system` | enum | See vocabulary below. Unrecognized or unnamed systems use `none_observed`, not `unknown`. |
| `evidence_tier` | enum | `A`, `B`, `C`. Defined below. |
| `evidence_class` | enum | `employer_artifact` or `platform_log`. This is the stratum used for sensitivity analysis. |
| `register` | enum | `application` or `opportunity`. Only `application` rows enter the census. |
| `terminal_outcome` | enum | See vocabulary below. |
| `terminal_outcome_date` | date | |
| `terminal_outcome_precision` | enum | Same values as `date_precision`. |
| `location` | string | As listed. |
| `work_type` | enum | `remote`, `hybrid`, `onsite`, `unstated` |
| `level_as_listed` | string | |
| `salary_range_listed` | string | Verbatim. `not_stated` if absent. |
| `confidence` | enum | `high`, `medium`, `low`. Item-level, not population-level. |
| `notes` | text | Free. Aliases, merge reasoning, anything that does not fit a field. |

## Table 2: events

One row per timestamped interaction. Many per application. This is what makes PhrasIQ legible.

| field | type | definition |
|---|---|---|
| `coder_id` | string | Independent coder who produced the row. Assigned, not derived. |
| `event_id` | key | `{application_id}\|e{n}` |
| `application_id` | fk | Joins to table 1. An event may never exist without a parent application row. |
| `event_date` | date | |
| `event_date_precision` | enum | Same values as `date_precision`. |
| `event_type` | enum | See vocabulary below. |
| `round_number` | int | Interview events only. 1, 2, 3. |
| `counterparty_name` | string | "Eddie". `unknown` if not recorded. |
| `counterparty_role` | string | "CEO", "recruiter", "hiring manager". |
| `medium` | enum | `video`, `phone`, `onsite`, `async`, `email`, `unknown` |
| `evidence_system` | enum | `gmail`, `gcal`, `linkedin`, `wellfound`, `jobright`, `ladders`, `screenshot`, `memory` |
| `evidence_id` | string | Hashed pointer (`gth_` Gmail thread, `cal_` calendar event). Raw provider IDs are not stored in the committed corpus. |
| `notes` | text | |

`evidence_system = memory` marks anything sourced from recall rather than an artifact. It is legitimate to log, and it must be visible so it can be excluded from the reproducible subset.

## Table 3: exclusions

Rows that were considered and rejected. Keeping this visible is what makes the census auditable.

| field | type | definition |
|---|---|---|
| `coder_id` | string | Independent coder who produced the row. Assigned, not derived. |
| `candidate_id` | string | Stable label for the considered-and-rejected item. |
| `date` | date | Artifact date. |
| `company` | string | As listed, or empty if unnamed. |
| `role` | string | As listed, or empty if unnamed. |
| `exclusion_reason` | enum | See vocabulary below. |
| `what_would_promote_it` | string | The specific artifact that would move it into the census. |
| `evidence_system` | enum | Same values as events. |
| `evidence_id` | string | Hashed pointer. Same rules as events. |

## Evidence tiers

- **Tier A, definitive.** An ATS, employer, or recruiter message using explicit application language. Received, submitted successfully, thank you for applying.
- **Tier B, corroborated.** Application language is present but the employer or the title is partially missing, and a second artifact resolves it.
- **Tier C, self-logged.** A tracker row or applied-list row with no employer-side artifact.

`evidence_class` is a separate, coarser split. `employer_artifact` covers anything originating from the employer, their ATS, their recruiter, or the candidate's own sent mail. `platform_log` covers applied-list rows, tracker rows, and agent send confirmations.

## Counting rules

1. Unit of analysis is `company_canonical + role_as_listed + cycle`.
2. Same company, materially different title, is two applications.
3. Same company, same title, plus reminder and rejection threads, is one application.
4. A new submission artifact after a terminal outcome on the same company and title is a new cycle and counts again.
5. Marketplace: a titled role submission counts. Creating a profile does not.
6. An agent or aggregator send counts only when the receipt states the application was sent, or a matching ATS receipt exists.
7. A recruiter writing "thank you for applying" counts for that client role.
8. Never invent a company or a title. A receipt that omits the role is `unspecified`.

## Controlled vocabularies

**role_lane**: `explicit_gtm_engineering`, `sales_solutions_engineering`, `revops_gtm_ops_strategy`, `growth_demand_marketing`, `sales_bd_partnerships`, `product_ai_technical`, `unspecified`, `other`

**gtm_modifier**: `plain`, `founding_senior_lead`, `growth_marketing`, `systems_operations`, `sales_presales`, `ai_product_vertical`

**discovery_source**: `linkedin`, `wellfound`, `jobright`, `ladders`, `yc_wfs`, `referral`, `recruiter_inbound`, `company_site`, `newsletter_community`, `unknown`

**submission_channel**: `easy_apply`, `ats_direct`, `apply4me_agent`, `jobright_agent`, `email_direct`, `wellfound_apply`, `recruiter_submitted`, `marketplace_profile_submission`, `unknown`

**ats_system**: `Greenhouse`, `Ashby`, `Lever`, `Workable`, `Workday`, `iCIMS`, `Rippling`, `Gem`, `Dover`, `Teamtailor`, `Recruitee`, `Comeet`, `Breezy`, `Jobvite`, `none_observed`. If the ATS is unnamed or not in this list, use `none_observed`. Do not emit `unknown`.

**event_type**: `submission_receipt`, `employer_ack`, `assessment_sent`, `assessment_completed`, `recruiter_screen`, `hiring_manager_interview`, `panel`, `technical_exercise`, `final_round`, `offer`, `rejection`, `withdrawal`, `followup_sent`, `reschedule`, `no_show`, `unknown`

**medium**: `video`, `phone`, `onsite`, `async`, `email`, `unknown`

**terminal_outcome**: `no_response`, `rejected_no_interview`, `rejected_after_interview`, `ghosted_after_interview`, `withdrawn_by_candidate`, `role_paused_or_closed`, `offer_declined`, `offer_accepted`, `still_open`, `unknown`

**exclusion_reason**: `attempted_not_submitted`, `marketplace_profile`, `recruiter_initiated`, `consulting_prospect`, `out_of_window`, `unresolvable_identity`, `unknown`

## Derived metrics, never stored

- `interviewed` = any event where `event_type` is in the interview set
- `n_rounds` = count of interview events
- `days_to_first_response` = first `employer_ack` or `rejection` minus `date_applied`, computed only where both precisions are `exact`
- `days_to_interview` = first interview event minus `date_applied`, same precision constraint
- `interview_rate` = interviewed applications over total, reported separately for `evidence_class = employer_artifact` and for the full census

## Worked examples

These show format only. They are not answers to any row in your corpus.

**A role found on a jobs marketplace, applied through that marketplace, followed by three conversations with a founder.** One application row: `example-co|founding-gtm|c1`, `discovery_source = wellfound`, `submission_channel = wellfound_apply`, `evidence_tier = A`, `evidence_class = employer_artifact`, `register = application`. Four event rows: one `submission_receipt`, then three interview events with `round_number` 1, 2, 3, `counterparty_name` and `counterparty_role` filled from the invite, `evidence_system = gcal` with hashed calendar pointers.

**A role with a single interview and nothing else.** One application row, one interview event carrying the hashed calendar pointer as evidence. No rollup field is written anywhere.

**A re-application after rejection.** Two application rows, `c1` and `c2`, with different `date_applied`. The `c1` row carries a `terminal_outcome` of `rejected_no_interview` and its date. That terminal outcome is what licenses `c2` to exist as a separate row.

**A recruiter-sourced process with an interview and no submission artifact.** One application row with `discovery_source = recruiter_inbound` and `register = opportunity`, plus the interview event. It stays in the dataset and out of the census. Never omit it.

**A receipt that names no role.** `role_as_listed = unspecified`, `role_lane = unspecified`. Do not guess from the company's typical openings.

## Changelog

- 2026-08-29: `coder_id` is the first field of every table so CSV headers match this file. `unknown` added to `event_type`, `medium`, `terminal_outcome`, and `exclusion_reason`. Unrecognized ATS values use `none_observed`. `evidence_id` is a hashed pointer, not a raw provider ID.
