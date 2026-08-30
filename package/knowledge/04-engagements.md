<!-- kit-meta
file: 04-engagements.md
tier: 0 (durable)
created: 2026-08-29
updated: 2026-08-29 (rev 2, after Q8b)
sources: [retrieval logs 026, 027, 028, 029]
status: DRAFT. Descriptions are Keegan's to write. Spans are evidence-bound and are not his to move.
-->

# Table 4: engagements

A codebook addendum. Adding this table does not invalidate any prior row in Tables 1 to 3, because it introduces no new fields there. Everything the analysis needs from it is **derived at query time**, per design principle 1.

## Why this table exists

Retrieval logs 026 to 029 established that engagements ran across much of the study window. Every conversion figure in Results is a rate computed on a denominator produced by someone who was, much of the time, working. A reader cannot evaluate an application rate without that condition stated.

## The disclosure rule

The subject has elected not to name the engagements **in the published paper**, while retaining names throughout the working record until a single redaction step immediately before publication. That is the right call: redacting early destroys the ability to audit the analysis against the artifacts, and every number in Results has to stay traceable to a source id right up until the moment it ships.

- **Identity is retained in the working record and withheld from the paper.** Names, domains, counterparties and amounts live in this file and in the retrieval logs. None of them reach the manuscript.
- **The condition is disclosed.** The paper states that engagements ran concurrently, gives their spans, and reports the concurrency alongside every rate.
- **Descriptions are the subject's to write, with a floor.** Scope, nature and character are his. A description may not be more favourable than the artifacts support. An engagement that stalled may not be described as one that completed.

## Redaction protocol

The failure mode of late redaction is a find-and-replace pass over a finished manuscript that misses one instance. The protocol below makes that structurally impossible rather than relying on a careful reading.

**Rule 1: the manuscript never contains a name in the first place.** Draft every section against `ENG-A` through `ENG-E` from the first sentence. Names live only in this file and the retrieval logs. Redaction is then the deletion of a crosswalk, not the editing of prose. Nothing has to be found, so nothing can be missed.

**Rule 2: descriptions are written redaction-safe on the first pass.** This is the live risk. A description like "a bariatric care software company in Atlanta" names the company as surely as the company name does. Write to the level of "a healthcare software company" or "an early-stage GTM consultancy". Sector plus stage is usually safe. Sector plus stage plus geography plus niche is not.

**Rule 3: figures and appendices are checked too.** Axis labels, legend entries, tooltip text, spreadsheet tab names, and any exported CSV. Names leak through artifacts more often than through body text.

**Rule 4: one crosswalk file, deleted at publication.** The `company_canonical` column in this file is the only mapping. At publication, that column is deleted and this file is archived unpublished alongside the retrieval logs. The archived copy stays intact; the published kit ships without it.

**Rule 5: run a pre-publication scan.** Grep the full manuscript, figures and supplementary tables for every value in `company_canonical`, every counterparty surname in logs 026 to 029, and every domain. Expect zero hits. A non-zero result means Rule 1 was broken somewhere and the section has to be rewritten, not patched.

**What Substack and LinkedIn change.** The derivative posts are the higher-risk surface, not the paper. They are shorter, more narrative, and more tempting to make concrete. Rules 1 through 5 apply to them identically. Log 027 also carries a separate sensitivity flag on ENG-C, which is not a naming question and is not resolved by redaction.

## Rev 2: what changed and why

Rev 1 recorded ENG-A as a continuous span 2025-02 to 2026-04 and ENG-B as running from 2025-06 with an unknown end. **Both were wrong in the same direction: they inferred continuity from endpoints.** That is the exact error this project's rules forbid, and it had the effect of making the window look fully covered.

Two corrections:

1. **ENG-A is not continuous.** An account existed from 2025-02 and intensive activity is evidenced 2026-03 to 2026-04. Nothing evidences the fourteen months between. ENG-A is now recorded as the evidenced active period only, with the earlier account existence held in notes.
2. **ENG-B is bounded, not unknown.** Q8b searched the full window for the standing meeting. It returns **exactly one instance, 2025-06-09.** The series was created 2025-04-07 and last modified 2025-07-28. The last email artifact is 2025-07-01. Evidenced activity therefore runs 2025-06 to 2025-07, with an outer bound of 2025-07-28.

**Consequence: the window is not fully covered.** Three months carry no evidenced engagement activity. That gives the concurrency analysis an actual comparison group, which rev 1 had accidentally destroyed.

## Schema

| field | type | definition |
|---|---|---|
| `engagement_id` | key | `ENG-A` through `ENG-E`. Assigned in order of first evidenced activity. Never reassigned. |
| `company_canonical` | string | **Retained in the working record. Never reaches the paper.** Removed at the publication redaction step by deleting the crosswalk, not by editing prose. |
| `description` | text | **Written by the subject.** One or two lines. Nature and scope. Must survive redaction, so it may not contain identifying detail even while names are retained here. |
| `span_start` | month | `YYYY-MM`. First evidenced *activity*, not first account existence. |
| `span_start_precision` | enum | `exact`, `evidence_bound`, `unknown` |
| `span_end` | month | `YYYY-MM`, or `ongoing`. |
| `span_end_precision` | enum | Same values. |
| `continuity` | enum | `continuous_evidenced`, `endpoints_only`, `single_point`. Whether activity is evidenced *throughout* the span or only at its edges. **New in rev 2.** Without this field a span silently asserts continuity it has not earned. |
| `compensation_evidenced` | enum | `yes`, `no_artifact_retrieved`, `unknown`. Whether a payment or contract artifact exists, **not** whether the work was paid. |
| `intensity` | enum | `recurring_standing`, `project_burst`, `single_deliverable`, `unknown`. Derived from meeting cadence and deliverable frequency, not asserted. |
| `evidence_log` | string | Pointer to the retrieval log holding the unredacted record. |
| `notes` | text | Free. |

**Granularity: month, by default.** The coarsest resolution that still permits Figure C. Coarser than month collapses the figure entirely. A move to quarter must be decided before any figure is generated and removes Figure C from the paper.

## Register, populated (rev 2)

**Names are retained here by the subject's instruction and are removed at publication. See the redaction protocol below.**

| id | company_canonical | span | precision | continuity | comp. evidenced | intensity | log | description |
|---|---|---|---|---|---|---|---|---|
| ENG-A | BCOFA | 2026-03 to 2026-04 | exact / evidence_bound | `continuous_evidenced` | `no_artifact_retrieved` | `project_burst` | 028 | *subject to write* |
| ENG-B | Mobb.ai | 2025-06 to 2025-07 | exact / evidence_bound | `endpoints_only` | `no_artifact_retrieved` | `unknown` | 027, 029 | *subject to write* |
| ENG-C | Mixmax | 2025-09 to 2025-12 | exact / exact | `continuous_evidenced` | `yes` | `recurring_standing` | 027 | *subject to write* |
| ENG-D | Kivira.health | 2026-04 to 2026-07 | exact / evidence_bound | `continuous_evidenced` | `no_artifact_retrieved` | `recurring_standing` | 028 | *subject to write* |
| ENG-E | Morph Data Strategies | 2026-05 to ongoing | exact / ongoing | `continuous_evidenced` | `yes` | `project_burst` | 028 | *subject to write* |

### Notes on the spans

- **ENG-A.** An account was provisioned 2025-02, four months before the window opens. Activity is evidenced only 2026-03 to 2026-04. The intervening period is **not** evidenced and is not claimed. The engagement ends on a counterparty message asking whether the project was continuing. That is a stall, not a completion, and the description must not imply completion.
- **ENG-B.** The subject states this was employment, not contract work, and that he left. `continuity = endpoints_only` and `intensity = unknown` because a standing series that occurs once cannot support an intensity claim. Log 030 found the standing meeting exactly once in the full window. That single instance may mean the series was truncated, or that later instances were removed; log 030 also established that this calendar's deletion behaviour is inconsistent, so absence is weak evidence either way. **Do not read the single instance as proof the arrangement ended in June.**
- **ENG-C.** The cleanest record in the table: dated agreement, sequential invoices, dated closure. Internal structure supplied by the subject: a **two week contract trial** that converted into the three month engagement. The 2025-09-04 service agreement is therefore most likely the trial instrument rather than the engagement instrument, which the artifacts alone do not distinguish. Sourced by the counterparty through GTM Engineer School, preceded by a nine week informal interview process (log 031). **Opportunity register, not census** (log 032).
- **ENG-D.** Ends on the last instance of a recurring series. That bounds evidenced activity, not the arrangement.
- **ENG-E.** Live at window close, with a payment landing on the final day of the study window.

`compensation_evidenced = no_artifact_retrieved` means exactly that. Three of these five may well have been paid; the artifacts retrieved so far do not show it. This is a retrieval gap, not a finding, and the paper must not read it as one. Q12 is unexhausted and may flip ENG-A and ENG-D.

## Derived, never stored

Computed at query time by joining `applications.date_applied` against the engagement spans:

- `concurrent_engagement_count` — engagements with evidenced activity in the month an application was submitted.
- `months_without_evidenced_engagement` — **3 of 15: 2025-08, 2026-01, 2026-02.** Note the wording. These are months with no evidenced engagement activity. They are not months of established idleness, and the paper must use the longer phrase.
- `applications_per_engaged_month` versus `applications_per_unevidenced_month` — now computable, on an n of 3 against 12. Report the n alongside the ratio every time. A three-month comparison group supports a description, not an inference.

## Figure C, specified before generation

**Chart:** dual-axis monthly series. Bars, applications submitted per month. Shaded bands beneath, engagement concurrency per month, with the three unevidenced months left unshaded.
**Slice:** `register = application` only. Opportunity rows excluded.
**Caveats, required in the caption:** (a) a large share of `date_applied` values are `relative_display` approximations, so monthly placement is approximate for those rows; (b) the unshaded months indicate absence of evidence, not evidence of absence.
**Produce twice:** once on the full census, once on `date_precision = exact` only. Show both.
**What it must not claim:** any causal reading of engagement load on application volume. n is one subject, the engagements are not independent of his search behaviour, and the comparison group is three months.

## Draft Methods paragraph (rev 2)

> The subject was not continuously unemployed during the study window. Five engagements are evidenced across the fifteen months, with concurrent activity in twelve of them; three months carry no evidenced engagement activity, which is a statement about the corpus rather than about the subject's occupation. Engagements are reported here as anonymized spans at month resolution, with a continuity flag distinguishing spans evidenced throughout from spans evidenced only at their endpoints. Identities, counterparties and amounts are withheld at the subject's election and held in the unpublished retrieval record. This is a material condition on every rate reported in Results: most applications in the census were submitted by an applicant who was concurrently billing or delivering client work, which bears on volume, cadence, and selectivity. The study makes no claim about the direction of that effect.

## Open threads

1. **Descriptions unwritten.** Five one-liners from the subject. Blocks Methods.
2. **ENG-B's real end date.** Bounded to 2025-07 by evidence; the subject can state the actual end. Affects whether 2025-08 belongs in the comparison group.
3. **Q12 not exhausted.** Page token `tok_2e25d4a276d2`. May flip `compensation_evidenced` on ENG-A and ENG-D.
4. **Q8 calendar blocks 2 to 6 pending.** Blocks 2 and 3 cover 2025-08 to 2026-02, which is now the analytically important stretch, because it contains all three unevidenced months.
5. **`33@lecturesfrom.com` unswept** and possibly still accessible. It organised meetings for ENG-D and ENG-E, so it likely holds engagement records, and it may hold applications.
