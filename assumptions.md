# Assumptions

Every inference rule this dataset rests on, with the reason it was adopted, what it rules out, and
whether it is settled or still open.

Two kinds of entry live here. **Frozen** assumptions were fixed in the pre-registration before
extraction began and cannot change without invalidating prior rows. **Post-hoc** assumptions were
adopted after coding, which is a weaker position, and each one says so and names its date.

A rule that only appears in code is not an assumption anyone can audit. Everything below points at
the file that implements it.

No dashes are used as punctuation in this file.

## How to read the status column

| Status | Meaning |
|---|---|
| Frozen | Pre-registered before extraction. Changing it invalidates coded rows. |
| Post-hoc | Adopted after coding. Logged in `knowledge/protocol.md` with a date. Weaker, and disclosed as such. |
| Analysis | Introduced by the view and reporting layer. Changes no census figure, only how figures are presented. |
| Open | Not resolved. The paper reports it as unresolved rather than picking a value. |

---

## A. Scope and window

**A1. The study window is 2025-06-01 to 2026-08-29, America/New_York, inclusive.** *Frozen.*
Prior audits searched only from 2025-08-25 forward. Declaring the wider window makes June through
early November 2025 **unharvested rather than empty**, which is a different claim from "quiet
period". Rules out: reading a search-boundary artifact as a behavioral finding. Source:
`knowledge/protocol.md`.

**A2. The two prior workbooks are floors, not inputs.** *Frozen.* 247, 212, and 163 are prior-audit
figures and are not inherited by this freeze. Rules out: carrying forward a number whose derivation
cannot be reconstructed. Source: `paper/DEFECTS.md`.

**A3. The relationship between the 212-row audit and the 163-row Gmail floor is unreconstructable.**
*Open.* Both workbooks are absent from the repository and were not found in Drive. The paper reports
this as an open defect rather than proposing a reconciliation. Source:
`artifacts/platform/KEEGAN-EXPORTS-ABSENT.md`.

## B. What counts as an application

**B1. The unit of analysis is `company_canonical + role_as_listed + cycle`.** *Frozen.* Rules out:
counting a rejection thread as a second application, and collapsing a genuine re-application into
its first attempt. Source: `codebook.md` counting rule 1, `schema.md`.

**B2. A repeat submission opens a new cycle only after a terminal outcome on the previous one.**
*Frozen.* The terminal outcome is what licenses the second row. Applied in both directions: FOSSA and
Attentive became `c1` and `c2` because a decline sat between the receipts, and three Pogo artifacts
across two systems stayed one cycle because nothing terminal sat between them. Source: `codebook.md`
counting rule 4.

**B3. An interview with no submission artifact does not mint an application row.** *Frozen, applied
in adjudication.* This is the rule that decided The Hog, BX Studio, WorkOS, and the 2026 Weave
opening. All four stay in the dataset under `register = opportunity`. Rules out: inflating the
conversion rate with outcomes that did not come from applying. Note the direction of the bias it
removes: the opportunity rows are the ones with the *good* outcomes, including three that converted
to paid work, which is why this contamination is rarely caught. Source: `adjudication/ADJUDICATION.md`.

**B4. Creating a marketplace profile is not applying. Submitting a titled role through a marketplace
is.** *Frozen.* Source: `codebook.md` counting rule 5.

**B5. An agent or aggregator send counts only when the receipt states the application was sent, or a
matching ATS receipt exists.** *Frozen.* Rules out: counting an agent's queued intent as a
submission. Source: `codebook.md` counting rule 6.

**B6. A receipt that omits the role is coded `unspecified`, never guessed.** *Frozen.* 39 rows carry
it. Rules out: inferring a title from a company's typical openings to make a table look complete.
Source: `codebook.md` counting rule 8.

## C. Dates

**C1. Every date carries a precision label and, where relative, a capture date.** *Frozen.*

**C2. A relative stamp is never upgraded to a calendar date.** *Frozen.* "2mo ago" read on
2026-08-29 is a range. Writing 2026-06-29 into a date column converts a range into a false fact.
Consequence: 26 census rows cannot enter the monthly series and are printed beside it.

**C3. Precision-constrained metrics run only on rows where both dates are exact.** *Frozen.* This is
why the latency base is 196 rather than 221 and the time-to-first-interview n is 11 rather than 13.
The excluded n is reported alongside every such figure. Source: `knowledge/protocol.md`.

## D. Coding and adjudication

**D1. Coders are blind to each other and the codebook was frozen before the first ran.** *Frozen.*
A coder who sees more artifacts is not a second rating, it is a different study. Source:
`knowledge/protocol.md`.

**D2. Pre-adjudication agreement is the published statistic, not post-adjudication agreement.**
*Frozen.* Reporting agreement after resolving disagreements would report the resolution, not the
instrument.

**D3. Interviewed-ness is derived from events on every run and never stored on an application row.**
*Frozen.* Implemented once, in `adjudication/_common.py`, and imported by every consumer rather than
restated. Rules out: two published interview counts that disagree.

**D4. The interview numerator is the union of both coders' events.** *Frozen.* Both coders found 10
of the 13 independently. Three rest on cursor alone and bravo contributes none that cursor missed, so
interview-set agreement is 10/13, weaker than the role-lane kappa of 0.9510 suggests. Event-level
agreement is not among the reliability statistics the protocol requires, so it is **unmeasured
rather than measured and small**, and the paper says so.

**D5. Adjudication resolves disagreements with a written rule that would apply to the next case,
never with a preference.** *Frozen.* Source: `adjudication/ADJUDICATION.md`.

**D6. Coder CSVs are never edited after the fact.** *Frozen.* Corrections are applied downstream by
name. Editing a blind coder's file retroactively destroys the agreement statistic that file was
produced to support.

## E. Record linkage against platform exports

**E1. A platform row matches a census row through three ordered tiers, stopping at the first tier
producing exactly one candidate.** *Frozen.* Exact after normalization, then an entity-level fallback
for admitted unknowns, then ordered token-prefix equivalence. Source:
`adjudication/ingest_platform.py`.

**E2. When tier 3 produces more than one candidate, nothing is matched.** *Frozen.* A wrong merge
silently destroys a record. An unmerged duplicate is visible and fixable.

**E3. A refused match is recorded as `ambiguous` with its candidate parents, not shipped as
`net_new`.** *Post-hoc, 2026-08-30.* Before this change a refusal was indistinguishable from a row
with no counterpart, so a possible duplicate could enter the census with nothing marking it
unresolved. Zero rows hit the branch on the current corpus and no published figure moved. Logged in
`knowledge/protocol.md`, disclosed in `paper/DEFECTS.md`.

**E4. The matcher's noise-token list is one person's geography and one person's abbreviations.**
*Open, and a known weakness.* It strips `atlanta`, `ga`, `austin`, `tx`, and also `products`, which
will quietly mangle a title such as "GTM Emerging Products" for anyone reusing it. It is correct
enough for this corpus and should be pruned before reuse. Source:
`adjudication/ingest_platform.py`, `translation/AUDIT-FINDINGS.md`.

**E5. Titles that expand or abbreviate an existing role at the same company are the same
application.** *Frozen.* AE and Account Executive, location parentheticals, "Listen" and "Listen
Labs". Those are overlap, not net-new. Rules out: a naive sum across four trackers reporting roughly
315.

## F. The Weave correction

**F1. The 2026-08-18 Weave decline evidences a real interview, but for a separate opening from the
2025 application it was attached to.** *Post-hoc, 2026-08-30.* That opening is inbound with no
submission artifact anywhere in the corpus, so under B3 it goes to the opportunity register.

**F2. The correction came from the author, from recall, after seeing the analysis.** *Disclosed, not
softened.* Subject and author are the same person, and this is the exact failure mode blind coding
exists to prevent. Two things support it: bravo independently excluded the same artifact under blind
conditions as having no parent, so the correction moves the census toward the blind coder's
judgement rather than away from it, and the artifact itself establishes that an interview happened.
Only its attachment was wrong.

**F3. The 2026 role title, the counterparty, and the inbound origination remain recall and are not
written into any structured field.** *Frozen rule, applied here.* `prompts/extraction.md` rule 8.
Recall is legitimate to hold and must never be disguised as evidence.

Consequence of F1 through F3: interviewed applications 14 became 13, the rate 14/221 became 13/221,
`rejected_after_interview` 6 became 5, `rejected_no_interview` 73 became 74, and time to first
interview moved from n = 12, mean 40.3, max 387 to n = 11, mean 8.8, max 34. One event was carrying
the mean.

## G. Completeness

**G1. 95 percent completeness is a goal, not a verifiable claim.** *Frozen.* Without a gold standard
there is nothing to verify it against.

**G2. Naive two-source capture recapture on Gmail against LinkedIn is invalid and was not run.**
*Frozen.* LinkedIn Easy Apply frequently generates no ATS mail at all, so the two sources are
near-disjoint by construction. Applying the estimator to the raw overlap would yield an implausible
population.

**G3. The defensible estimator is restricted to LinkedIn rows submitted through an external ATS
rather than Easy Apply.** *Frozen, and unmeasured.* The LinkedIn file that arrived is pages 1 to 10
of an applied list with no Easy Apply label, so the overlap stratum does not exist in the data. **No
completeness percentage is published.** Stated bias direction if someone runs the unstratified
estimator anyway: Easy Apply is visible to LinkedIn and invisible to ATS mail, which inflates
apparent uniqueness and understates completeness.

**G4. Four of the seven stop conditions are Partial or Unmet and the census is closed anyway.**
*Open, and disclosed.* Ladders and the YC dashboard are Unmet. Personal Gmail Q7 page 2 and beyond,
the personal calendar, LinkedIn pages beyond 10, and the Talentpluto and Jobgether employers are
Partial. The census is reported as bounded by those gaps rather than as complete. Source:
`artifacts/STOP-CONDITIONS.md`.

## H. Origin, and why no channel finding exists

**H1. Origin is three independent fields, not one string.** *Frozen.* Where the role was found
(`discovery_source`), how it was submitted (`submission_channel`), and where the evidence lives
(`evidence_class`) are separate questions. Collapsing them into "Gmail Ashby" is what made the prior
ledger unable to compare channels at all. Source: `codebook.md` design principle 3.

**H2. `discovery_source = unknown` is an admitted unknown, not a missing value.** *Frozen.* The
codebook requires a legal way to say "I could not tell" for exactly this reason. It is recorded
honestly on 206 of 221 census rows.

**H3. No origination-channel conversion figure is published, and this is a finding rather than an
omission.** *Analysis.* `views/origin_coverage.csv` shows why: origin is known almost exactly where
outcome is unobservable. The 71 LinkedIn rows that know their origin carry zero observable outcomes,
because a platform applied-list row has no employer-side artifact and therefore no events. The rows
that do have outcomes are the 206 whose origin is `unknown`. The overlap that could answer the
question is 15 of 221, spread across five channels with the largest at 7.

**H4. Origin was never backfilled from recall.** *Frozen rule, applied.* It could have been, for a
large fraction of rows, and the result would have looked like data. Under F3 and extraction rule 8
it was not.

**H5. `company_stage` does not exist in this schema.** *Open.* No cut by company size or stage is
available anywhere in this dataset. This is a gap in the instrument rather than a suppressed cell,
and it means the brief's question about which company stages convert has no answer here at all.

## I. Analysis and presentation

These change no census figure. They govern how figures are presented, and each one could reasonably
have been decided differently.

**I1. Cells under n = 5 are suppressed, and suppressed groups keep their row and their n.**
*Analysis.* A dropped group is indistinguishable from a group that does not exist. The threshold
matches the one `adjudication/derive_latency.py` already applied.

**I2. A median is suppressed on the count it was computed from, not on the size of the group.**
*Analysis.* These medians are conditional on having responded. A group of 8 with 3 responders yields
a 3-point median, and publishing it beside a 43-point median because both cleared a base threshold
would present them as comparable. Implemented in `pipeline/build_views.py`, reported in the
`suppressed_because` column.

**I3. Every publishable rate carries a Wilson 95 percent interval, and no p-values are reported.**
*Analysis.* Wilson rather than the normal approximation because several cells have zero interviews,
where the normal interval collapses to zero width and asserts a certainty that is not there. With 13
interviews across 221 applications, significance testing would dress up noise.

**I4. Response rate and response latency are reported separately, and latency medians are conditional
on responding.** *Analysis.* A single "typical response time" folding in the 96 silent applications
would drop them from the denominator, which is the same error B3 exists to prevent on the interview
rate.

**I5. Both response definitions are published, substantive and any.** *Analysis.* Excluding
`employer_ack` moves the median from 5.5 days to 7 and halves the day-zero share, so the choice
changes the number and is not the analyst's to make silently. The substantive figure is the headline
because an automated acknowledgment arriving with the receipt is not a response.

**I6. Title-token groups overlap by construction and are never presented as a partition.**
*Analysis.* One title can match several tokens, so those rows do not sum to 221.

**I7. Title language and role lane are descriptive, never causal.** *Analysis.* The applicant chose
which roles to apply to, so both are confounded with self-selection. A lane that progressed may
reflect where he was a plausible fit rather than any property of the words. Nothing here is
randomized.

**I8. The origin taxonomy is read by the view layer only, never by the matcher.** *Analysis.*
`pipeline/origin_taxonomy.csv` is a presentation lookup. `adjudication/ingest_platform.py` keeps its
own alias table. A lookup shared between the census and the analysis would let an analysis change
move the census.

**I9. `pipeline/data_quality.py` treats the root `codebook.md` as authoritative.** *Analysis.* The
codebook exists twice and the two copies already differ in wording. The validator parses one of them
and this states which. The duplication should be resolved to a single file. Source: `schema.md`.

## J. Publication

**J1. Companies are named in the draft, with a checklist for the naming pass.** The repository names
companies throughout and `knowledge/01-engagement.md` requires a naming pass before publication.
`paper/NAMED-COMPANIES.md` lists every company the draft mentions and where, so the pass is a
checklist rather than a re-read. Which names survive is the author's decision alone.

**J2. Nothing is published externally without the author's explicit approval of the final draft.**
The draft lands in this repository. It is not posted anywhere.

## Changelog

- 2026-08-30: created. Gathers rules previously scattered across `knowledge/protocol.md`,
  `adjudication/ADJUDICATION.md`, `paper/DEFECTS.md`, and `codebook.md`, and adds the analysis-layer
  assumptions introduced with `pipeline/` and `views/`. No census figure moved.
