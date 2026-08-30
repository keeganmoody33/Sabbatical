<!-- kit-meta
file: protocol.md
tier: 0 (durable)
created: 2026-08-29 14:24 ET
updated: 2026-08-30 ET
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

## Known integrity defects to resolve before publication

1. WorkOS, GTM Engineer, 2025-08-25, Tier A, marked Interviewed in the 212 row ledger, absent from the 247 row ledger. Resolve before any interview count is published.
2. The 212 to 163 reconciliation is undocumented.
3. The current dedupe key omits cycle, producing two false duplicate keys.

## Changelog

- 2026-08-29 14:24 ET: created from [S1] [S2] [S6]. Window set to 2025-06-01 through 2026-08-29. Gmail and Google Calendar named as authorized sources by the user on 2026-08-29.
- 2026-08-30 ET: coding correction after coding and adjudication were complete, logged here under the rule at the head of this file. The Weave 2026-08-18 `hiring_manager_interview` was attached to `weave|business-development-manager|c1`, an application already rejected 2025-07-31. The artifact `gth_0339a17e3860d167` is a post-interview decline, so an interview did happen, but for a separate 2026 opening. That opening is inbound with no submission artifact anywhere in the corpus, so it is adjudicated to the opportunity register on the same rule as The Hog. The event is excluded from the interview derivation by named decision in `adjudication/adjudicate.py`, and the Weave application's terminal outcome reverts to `rejected_no_interview` dated 2025-07-31, which is bravo's coding. Consequence: interviewed applications 14 becomes 13, the rate 14/221 = 0.0633 becomes 13/221 = 0.0588, `rejected_after_interview` 6 becomes 5, `rejected_no_interview` 73 becomes 74. The application census stays 221 and the full census stays 298. Time to first interview moves from n=12 median 6 mean 40.3 max 387 to n=11 median 6 mean 8.8 max 34, so that single event was carrying the mean. Source of the correction: the author, from recall, after seeing the analysis. That is the failure mode blind coding exists to prevent and is disclosed as such. Two things support it. Bravo independently excluded the same artifact during blind coding as having no parent, so the correction moves the census toward the blind coder's judgement. And cursor and bravo disagreed on this row's terminal outcome, a field adjudication never covered. The role title, the counterparty, and the inbound origination remain author recall and are not written into any structured field, per `prompts/extraction.md` rule 8. Coder CSVs were not edited. Disclosed in `paper/DEFECTS.md`.
- 2026-08-30 ET: pipeline change after coding and adjudication were complete, logged here under the rule at the head of this file. `adjudication/ingest_platform.py` gained an `ambiguous` match status. The tier 3 matcher already refused to choose when token-prefix equivalence returned more than one Freeze 1 candidate, but the refused row fell through to the net-new branch, where it was indistinguishable from a row with no counterpart. A possible duplicate could therefore enter the full census with nothing recording that it was unresolved. Ambiguous rows now carry `match_status = ambiguous` and a `candidate_parent_ids` column, are written to `adjudication/platform_match.csv`, and are held out of `adjudication/applications__full_census.csv`, on the ground that an omitted row is recoverable and an inflated census is not. Reason for the change: a defect found while auditing the repository, disclosed in `paper/DEFECTS.md`. No published figure moved. Zero rows hit the branch on the current corpus, verified by instrumenting the three tiers before the change: 46 exact, 6 unspecified-fallback, 4 unique-equivalent, 77 with no candidate. `platform_match.csv` remains 134 rows at overlap 56, net-new 77, opportunity or non-census 1. `applications__full_census.csv` remains 298 and byte-identical. Because no real row exercises the new branch, it was tested against synthetic Freeze 1 rows rather than by re-running alone. This change alters the instrument, not the frozen corpus, and no coder output was recoded.

- 2026-08-30 ET: pipeline and reporting layer added after coding and adjudication were complete, logged here under the rule at the head of this file. No stage of the instrument changed and no coder output was recoded. What was added: `pipeline/run.py`, a single entrypoint that runs the existing scripts in dependency order and, in its default check mode, hashes every declared output before and after and exits non-zero if an existing file changed. The full pipeline was verified byte-reproducible against the committed outputs before the entrypoint was written, and the guard subsequently caught a real change during development, which is the behaviour it exists for. Also added: `pipeline/build_views.py` and `views/`, materializing the tables the paper quotes from, asserting census 221, full census 298, interviewed 13 and latency base 196 on every run; `pipeline/data_quality.py` and `data_quality_report.md`, generated rather than written, reading the controlled vocabularies out of the root `codebook.md` at run time so the validator cannot drift from the frozen instrument; `pipeline/origin_taxonomy.csv`, a presentation lookup read by the view layer only and deliberately not shared with the matcher's alias table, because a lookup shared between the census and the analysis would let an analysis change move the census; and `schema.md` and `assumptions.md`, which write down the grain, the keys, the per-metric unit of analysis, and every inference rule with its status. One new defect was found by the added consistency check and is disclosed in `paper/DEFECTS.md`: `jobmail-io|growth-lead|c1` carries an interview event and a stored `terminal_outcome` of `rejected_no_interview`, from one coder with no blind second reading. It is left open rather than resolved by preference. No published figure moved; every previously committed output is byte-identical.
