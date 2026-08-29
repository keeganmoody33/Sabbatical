<!-- kit-meta
file: 03-codebook.md
tier: 0 (durable)
created: 2026-08-29 14:02 ET
updated: 2026-08-29 14:02 ET
review-by: 2027-08-29
sources: [S1] [S2] [S6]
-->

# Codebook

The logging schema for the Sabbatical dataset. Field definitions and controlled vocabularies. Changes to this file invalidate prior rows, so change it deliberately and log it.

## Six design principles

1. **Store observations, compute rollups.** `interviewed` and `rounds` are never fields. They are derived from the events table. A stored rollup and a stored event list will eventually disagree, and then neither is trustworthy.
2. **One row per application cycle, with cycle in the key.** This fixes the FOSSA and Attentive collision in the current ledger, where two legitimate second cycles share a dedupe key with their first.
3. **Origin is three fields, not one.** Where you found it, how you submitted it, and where the evidence lives are independent. The current ledger collapses them into strings like "Gmail Ashby", which makes it impossible to ask whether Wellfound outperformed Easy Apply.
4. **Every date carries a precision label and an anchor.** A relative stamp is only interpretable next to the date it was captured.
5. **Register is a field, not a separate sheet.** Moving rows between sheets loses history. Filter on `register` instead.
6. **Controlled vocabularies everywhere except `notes`.** Free text is where reproducibility dies.

## Table 1: applications

One row per application cycle.

| field | type | definition |
|---|---|---|
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
| `ats_system` | enum | Greenhouse, Ashby, Lever, Workable, Workday, iCIMS, Rippling, Gem, Dover, Teamtailor, Recruitee, Comeet, Breezy, Jobvite, none_observed |
| `evidence_tier` | enum | `A`, `B`, `C`. Defined in `00-core.md`. |
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
| `event_id` | key | `{application_id}\|e{n}` |
| `application_id` | fk | Joins to table 1. An event may never exist without a parent application row. |
| `event_date` | date | |
| `event_date_precision` | enum | Same values as `date_precision`. |
| `event_type` | enum | See vocabulary below. |
| `round_number` | int | Interview events only. 1, 2, 3. |
| `counterparty_name` | string | "Eddie". `unknown` if not recorded. |
| `counterparty_role` | string | "CEO", "recruiter", "hiring manager". |
| `medium` | enum | `video`, `phone`, `onsite`, `async`, `email` |
| `evidence_system` | enum | `gmail`, `gcal`, `linkedin`, `wellfound`, `jobright`, `ladders`, `screenshot`, `memory` |
| `evidence_id` | string | Message ID or calendar event ID. Pointer only, never published. |
| `notes` | text | |

`evidence_system = memory` marks anything sourced from recall rather than an artifact. It is legitimate to log, and it must be visible so it can be excluded from the reproducible subset.

## Table 3: exclusions

Rows that were considered and rejected. Keeping this visible is what makes the census auditable.

| field | definition |
|---|---|
| `candidate_id`, `date`, `company`, `role` | as above |
| `exclusion_reason` | `attempted_not_submitted`, `marketplace_profile`, `recruiter_initiated`, `consulting_prospect`, `out_of_window`, `unresolvable_identity` |
| `what_would_promote_it` | The specific artifact that would move it into the census. |
| `evidence_system`, `evidence_id` | |

## Controlled vocabularies

**role_lane**: `explicit_gtm_engineering`, `sales_solutions_engineering`, `revops_gtm_ops_strategy`, `growth_demand_marketing`, `sales_bd_partnerships`, `product_ai_technical`, `unspecified`, `other`

**gtm_modifier**: `plain`, `founding_senior_lead`, `growth_marketing`, `systems_operations`, `sales_presales`, `ai_product_vertical`

**discovery_source**: `linkedin`, `wellfound`, `jobright`, `ladders`, `yc_wfs`, `referral`, `recruiter_inbound`, `company_site`, `newsletter_community`, `unknown`

**submission_channel**: `easy_apply`, `ats_direct`, `apply4me_agent`, `jobright_agent`, `email_direct`, `wellfound_apply`, `recruiter_submitted`, `marketplace_profile_submission`, `unknown`

**event_type**: `submission_receipt`, `employer_ack`, `assessment_sent`, `assessment_completed`, `recruiter_screen`, `hiring_manager_interview`, `panel`, `technical_exercise`, `final_round`, `offer`, `rejection`, `withdrawal`, `followup_sent`, `reschedule`, `no_show`

**terminal_outcome**: `no_response`, `rejected_no_interview`, `rejected_after_interview`, `ghosted_after_interview`, `withdrawn_by_candidate`, `role_paused_or_closed`, `offer_declined`, `offer_accepted`, `still_open`

## Derived metrics, never stored

- `interviewed` = any event where `event_type` is in the interview set
- `n_rounds` = count of interview events
- `days_to_first_response` = first `employer_ack` or `rejection` minus `date_applied`, computed only where both precisions are `exact`
- `days_to_interview` = first interview event minus `date_applied`, same precision constraint
- `interview_rate` = interviewed applications over total, reported separately for `evidence_class = employer_artifact` and for the full census

## Worked examples

**PhrasIQ.** One application row: `phrasiq|founding-gtm-gtme|c1`, discovery_source `wellfound`, submission_channel `wellfound_apply`, evidence_tier A, evidence_class `employer_artifact`, register `application`. Three event rows: rounds 1 through 3, counterparty_name Eddie, counterparty_role CEO, evidence_system `gcal` with the calendar IDs, plus a `submission_receipt` event carrying the Wellfound accepted notice.

**Beautiful.ai.** One application row, one `hiring_manager_interview` event dated 2026-03-17 with the calendar ID as evidence.

**FOSSA.** Two application rows, `c1` dated 2026-04-22 and `c2` dated 2026-05-21. The `c1` row carries `terminal_outcome = rejected_no_interview` dated 2026-05-20, which is what licenses the second cycle.

**WorkOS.** One application row, discovery_source `recruiter_inbound`, register to be decided. Currently present in the 212 ledger and absent from the 247. Whichever register it lands in, it needs a row and an interview event, not silent omission.

## Changelog

- 2026-08-29 14:02 ET: created from [S1] [S2] [S6].
