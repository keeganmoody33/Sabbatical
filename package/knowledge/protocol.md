<!-- kit-meta
file: protocol.md
tier: 0 (durable)
created: 2026-08-29 14:24 ET
updated: 2026-08-30
review-by: 2027-08-29
sources: [S1] [S2] [S6]
-->

# Pre-registration

Frozen before extraction begins. Any change after the first coder runs must be logged here with a date and a reason, and disclosed in the paper.

## Study window

2025-06-01 to 2026-08-29, America/New_York, inclusive. 15 months.

Declared harvest boundary: the prior audits searched only 2025-08-25 forward, so 2025-06-01 to 2025-11-01 is unharvested rather than empty. No time series may be published until that gap is swept.

## Unit of analysis

One application cycle. `company_canonical + role_as_listed + cycle`. Defined in `knowledge/03-codebook.md`.

## Primary and secondary outcomes

- Primary: count of confirmed applications in the `application` register, reported at two strata, `employer_artifact` and full census.
- Secondary: application-to-interview rate, role lane distribution, time to first response, time to first interview.

Precision-constrained metrics (time to response, time to interview) are computed only on rows where both dates carry `precision = exact`. The excluded n is reported alongside.

## Coding design: independent parallel coding

Multiple LLM coders extract the same artifact set using `prompts/extraction.md`, without seeing each other's output. This is the design decision that upgrades the paper from one person's spreadsheet to a measured instrument.

Requirements, in order:

1. **Freeze the codebook first.** No vocabulary changes after coder 1 begins.
2. **Freeze the artifact set.** All coders receive the identical corpus. A coder who sees more artifacts is not a second rating, it is a different study.
3. **Blind.** No coder sees another coder's rows before all runs are complete. If any coder's output is read first, independence is destroyed and the agreement statistic is invalid.
4. **Adjudicate after, not during.** Disagreements are resolved in a named pass, and the pre-adjudication disagreement rate is published.

## Pre-registration revisions

A revision made **before coder 1 runs and before any Table 1 row exists** is a change to the pre-registration, not a deviation from it. It is logged here for the audit trail and stated in Methods as such. A change made after coding begins is a deviation, must be disclosed as one, and requires either re-coding or exclusion of affected rows.

### Revision 1 — 2026-08-30 — codebook amendments A1 to A4

**Trigger.** Logs 031, 032, 035, 036 and 037 each surfaced a vocabulary or field gap while retrieval was still running. Log 037 consolidated four pending changes. On inspection against `03-codebook.md`, one was already in force and two required reshaping.

**State at the time of the change.** `CORPUS-MANIFEST.md` unpopulated, coder 1 not run, zero Table 1 rows written. Migration cost zero.

**Changes, in force as of 2026-08-30:**

| id | change | type |
|---|---|---|
| A1 | `terminal_outcome` += `converted_to_contract`, linked to Table 4 via `notes`, excluded from `interview_rate` | vocabulary addition |
| A2 | Table 1 += `terminal_outcome_evidence_anchor`, with the `no_response` anchoring rule and derived `evidenced_silence_days` | field addition |
| A3 | `discovery_source`: `newsletter_community` retired, replaced by `community_gtm_cafe`, `community_gtm_engineer_school`, `community_other`, `newsletter` | **vocabulary replacement** |
| A4 | `event_type` += `referral_offered`; `medium` += `message`, `async` narrowed to assessment formats; derived `referral_assisted`; `exclusion_reason` += `referral_without_submission` | vocabulary addition |

**Corrections to the record.** Logs 036 and 037 both recorded `no_response` as a missing `terminal_outcome` value. It was already present. `reschedule` was likewise already present in `event_type`, closing open item 5 in `QUERY-MANIFEST 2.md`. A2 as enacted addresses the gap those logs were actually pointing at: an `evidence_bound` terminal outcome had no anchor field.

**Rationale for A3, the only replacement.** The study's central structural result — that the instrument capturing applications is blind to the channel that produced the outcomes — is a claim about the GTM community channel. It is not measurable on a value that fuses communities with newsletters, and it cannot be disaggregated after coding.

**Deferred, non-blocking.** Whether the two named communities appear by name in the published manuscript or as `community_A` / `community_B`. The working record retains names either way; this is settled at the redaction step.

**Full rationale:** `claude/05-codebook-amendments-r1.md`.

## Reliability statistics to report

- Percent agreement and Cohen's kappa on `role_lane`, across coders, on the subset both coded.
- Percent agreement on the binary include or exclude decision (`register = application` versus exclusion).
- Disagreement inventory: every row where coders differed, with the field and both values.

`role_lane` is the field that matters most. The current data already shows a 20 point gap in explicit GTM engineering share between the `employer_artifact` stratum (50.9 percent) and the `platform_log` stratum (30.2 percent). Until independent coders agree on lane assignment, that gap cannot be attributed to behavior rather than coding.

## Completeness estimation

Replace the asserted "88 to 93 percent" with an estimate that has a method behind it.

**Method: two-source capture-recapture, stratified.**

Naive Lincoln-Petersen across the full corpus will fail here, and the paper should say why. Gmail ATS receipts and the LinkedIn applied list are not independent captures. LinkedIn Easy Apply frequently generates no ATS mail at all, so the two sources are structurally near-disjoint by construction. Applying the estimator to the raw overlap of 17 against 163 and 99 yields an implausible population and would be a misuse of the method.

The defensible version restricts the estimate to the stratum where both sources could have observed the same application: LinkedIn rows for roles that were submitted through an external ATS rather than Easy Apply. Within that stratum, overlap estimates the unseen, and the resulting interval is extrapolated with the stratum share stated as an assumption.

Report the point estimate, the interval, the independence assumption, and the direction of likely bias. A completeness figure with a method and a caveat is publishable. A completeness figure asserted from feel is not.

**Threat to this method, opened 2026-08-30.** `linkedin-applications-in-window.csv` codes all 105 in-window rows as Easy Apply. If that assignment is correct, the stratum this estimator depends on — LinkedIn rows submitted through an external ATS — is **empty**, and the method as pre-registered cannot be run. The dedupe sweep measures this directly: any LinkedIn row that turns out to have a matching ATS receipt is by definition a member of that stratum. Do not choose a fallback estimator until the dedupe returns a count. See integrity defect 4.

**On the 95 percent target:** 95 percent completeness is a goal, not a claim that can be verified without a gold standard. What the paper can defend is a stated interval, the method that produced it, and the list of unmet stop conditions. If the interval's lower bound sits below 95, say so.

## Stop conditions

The census is not closed until all of these are met or explicitly waived in writing:

1. Gmail swept 2025-06-01 to 2026-08-29 for ATS domains, receipt phrases, and Sent mail with attachments.
2. Google Calendar swept for the same window in 90 day blocks without keyword filtering. Keyword search for "interview" previously returned zero events because loops lived in generic invite titles.
3. LinkedIn applied list confirmed complete, including whether pages beyond 10 exist.
4. Ladders applied list exported in full, not only the three Apply4Me receipts.
5. Jobright tracker exported in full.
6. YC Work at a Startup dashboard inspected.
7. Talentpluto and Jobgether underlying employers resolved or formally excluded.
8. **The 105 LinkedIn rows carry a resolved `dedupe_status`.** Until then no census total may be stated at any stratum. Added 2026-08-30 [log 035, log 037].

## Known integrity defects to resolve before publication

1. WorkOS, GTM Engineer, 2025-08-25, Tier A, marked Interviewed in the 212 row ledger, absent from the 247 row ledger. Resolve before any interview count is published.
2. The 212 to 163 reconciliation is undocumented.
3. The current dedupe key omits cycle, producing two false duplicate keys.
4. **`submission_channel` on the 105 LinkedIn rows is non-conforming and possibly unevidenced.** All 105 carry `linkedin_easy_apply`, which is not a value in the codebook vocabulary. Log 037 justified `date_precision`, `evidence_tier`, `evidence_class`, `register` and `dedupe_status` against the source but did not justify `submission_channel`. Two questions, both open: recode to `easy_apply` or add the value; and establish whether the LinkedIn export distinguishes Easy Apply from off-site submissions at all, or whether the blanket assignment was inferred. This is not cosmetic — it is load-bearing for the completeness estimator above. Opened 2026-08-30.

## Changelog

- 2026-08-29 14:24 ET: created from [S1] [S2] [S6]. Window set to 2025-06-01 through 2026-08-29. Gmail and Google Calendar named as authorized sources by the user on 2026-08-29.
- 2026-08-30: **Pre-registration revision 1** logged — codebook amendments A1 to A4, enacted before coder 1 and before any Table 1 row existed. Stop condition 8 added (LinkedIn dedupe). Integrity defect 4 added (`submission_channel` non-conforming on the 105 LinkedIn rows). Threat to the completeness estimator recorded against the capture-recapture section.
