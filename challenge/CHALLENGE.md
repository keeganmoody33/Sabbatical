# Challenge: the checkpoint workbook against this census

A second, independently produced reconstruction of the same fifteen months arrived on
2026-08-30, after Freeze 1, blind coding, and adjudication were complete. It holds **353
records** where this repository holds **298**. This file is the adversarial reconciliation.

The useful question is not "do the two agree". They cannot, because they count different units.
The question is **what does each one have that the other does not, and who is right in each
direction.** Both answers turned out to be substantive.

Everything below recomputes from `python3 challenge/reconcile.py`. No dashes are used as
punctuation in this file.

## What the challenger is, and what it is not

It is an independent reconstruction built from a different source set, including a LinkedIn data
download and a LinkedIn message export that this repository never had. It carries its own defect
register with open items, which is why it deserves to be taken seriously.

**It is not a third blind coder.** The protocol's requirement is that every coder receives an
identical corpus, because "a coder who sees more artifacts is not a second rating, it is a
different study". This workbook saw a different set by construction. So no kappa is computed
against it, and its agreement with the census measures nothing about coder reliability.

**Its unit is not this repository's unit.** It counts "reconstructed application-process records",
a unit its own summary sheet admits "may still exceed the number of unique employer requisitions".
This repository counts application cycles keyed `company + role + cycle`. Comparing row to row
would manufacture agreement or disagreement out of a units mismatch, so the reconciliation is at
company grain, which is the coarsest claim both datasets actually make.

**Its 353 is not comparable to 221.** Of its records, 56 companies are recruiter outreach, cold
outreach, marketplace, or referral rows that are opportunity register here and can never enter an
application denominator. The workbook mixes both registers in one total. That is the denominator
contamination this repository's two-register rule exists to prevent, and its own summary flags the
count as a checkpoint rather than a census.

## Scorecard

| Contested point | Winner | Margin |
|---|---|---|
| LinkedIn application evidence | **Challenger** | 107 exact-dated rows with job IDs against 99 relative stamps |
| The Hog and BX Studio register | **Challenger** | Submission artifacts exist. Two adjudications reversed |
| Companies with employer-side proof | **Repository** | 8 rows the workbook excluded are Tier A here |
| Coverage breadth | **Split** | 20 companies only in the workbook, 27 only here |
| Outcome model | **Repository** | GHOSTED is a residual the workbook itself calls overloaded |
| Interview measurement | **Repository** | 13 derived from events against 334 of 353 UNKNOWN |
| Origin coverage | **Challenger, but not adoptable** | 353 of 353 against 15 of 223. See below |
| Unresolved role titles | **Challenger** | It carries 8 unresolved against this census's 40. Eleven are now fixed from this repository's own artifacts |
| Capture recapture | **Neither** | Still unmeasured, now for a precisely stated reason |

## 1. Where the challenger wins

### 1.0 It found a gap this pipeline had left open in its own corpus

This is the finding that most deserved to lead and did not in the first version of this file.

The challenger resolves role titles down to **8 unrecoverable rows**. This census carried **40** rows
at `role_as_listed = unspecified`. Coding them that way was correct under counting rule 8, because
the Gmail receipt genuinely omits the title and a guess is forbidden.

But the title was not always absent from the corpus. It was absent from the *Gmail* artifact while
sitting in plain text in `artifacts/platform/jobright_applications_log.csv` and
`artifacts/platform/linkedin_job_applications_export.csv`, both of which this repository has
committed. The platform matcher marked those rows `overlap`, kept the Freeze 1 row wholesale, and
discarded the title the platform row was carrying.

**Eleven of the 40 are resolvable from this repository's own committed artifacts, under strict
company normalization, with zero ambiguous companies, and every one matches the title the challenger
gives.** That is not a disagreement between the two datasets. It is this pipeline failing to read
evidence it already had, and the challenger is what surfaced it.

Applied at Freeze 3.1: unspecified role lanes fall from 36 to 25, and `explicit_gtm_engineering`
gains 5 rows. `application_id` is deliberately not regenerated, because the events tables join on it
and a new slug would orphan every event on the row. Audit trail in
`adjudication/title_backfill.csv`.

The remaining 29 split three ways: 19 the challenger resolves from evidence outside this corpus
(contemporaneous job newsletters, LinkedIn job recommendations, archived listings), 6 it cannot
resolve either, and 4 whose companies it does not hold. The 19 are addressed in section 3.1.

### 1.1 The LinkedIn formal export is the artifact stop condition 3 was waiting for

107 rows from `Job Applications_5.csv` and `_6.csv`, each with a job ID, a job URL, and an **exact
application date**, spanning 2025-06-14 to 2026-08-22.

This repository has been working from a 99-row scrape of applied-list pages 1 to 10 carrying
**relative stamps** such as "2mo ago", which `assumptions.md` C2 forbids upgrading to calendar
dates. Those rows were structurally barred from the monthly series and from every latency figure.

The export supersedes the scrape outright. It is primary evidence, not reconstruction, and it is
adopted into Freeze 3.

| Comparison | Rows |
|---|---|
| Formal export, exact dates and job IDs | 107 |
| Paged scrape, relative stamps | 99 |
| Scrape companies absent from the export | 13 |
| Export companies absent from the scrape | 21 |
| Export companies absent from the 298 after alias resolution | 15 |

The 13 scrape companies missing from the export matter as much as the additions. The export was
generated 2026-08-23, so it cannot contain later activity, and page-scraped rows are not
automatically superseded. Both sources are kept.

### 1.2 Two adjudications are reversed by new evidence

The Hog and BX Studio were the **only two include or exclude disagreements between the blind
coders**, the two rows that produced the include kappa of 0.7452. Both were adjudicated to the
opportunity register on one stated ground: no submission artifact existed anywhere in the corpus.

The export contains submission rows for both, each dated before its process events.

| Company | Export row | First process event here | Gap |
|---|---|---|---|
| The Hog (YC F25), Founding GTM Engineer | 2026-06-04 | interview invitation 2026-06-15 | 11 days |
| BX Studio, GTM Engineer | 2026-04-06 | employer acknowledgment 2026-04-08 | 2 days |

The premise of both adjudications is now false. The rule was correct and is unchanged: an
interview with no submission does not mint an application row. A submission now exists, so both
become applications.

**This is the exclusion design working.** Every excluded row carries a `what_would_promote_it`
column naming the artifact that would reverse it. This is that artifact arriving.

Consequence: census 221 becomes 223, and because The Hog carries interview events, interviewed
applications 13 becomes 14 and the rate 13/221 becomes 14/223.

## 2. Where this repository wins

### 2.1 Origin-first classification discards provable applications

This is the sharpest result in the reconciliation, and it inverts the paper's own thesis.

The workbook's `Remaining Excluded` sheet drops 10 rows for unresolvable origin. **Eight of them
are in this census with Tier A employer artifacts.**

| Company | Workbook reason for exclusion | Status here |
|---|---|---|
| Lattice | Ladders Apply4Me, origin unresolved | application, Tier A, employer artifact |
| Firstup | Ladders Apply4Me, origin unresolved | application, Tier A, employer artifact |
| Ava Labs | Wellfound, origin unresolved | application, Tier A, employer artifact |
| Fibr AI | Wellfound, origin unresolved | application, Tier A, employer artifact |
| 12100 Collective | Wellfound, origin unresolved | application, Tier A, employer artifact |
| Infisical | Wellfound, origin unresolved | application, Tier A, employer artifact |
| PhrasIQ | Wellfound, origin unresolved | application, Tier A, employer artifact |
| Classet | Wellfound, origin unresolved | application, Tier B, employer artifact |
| UNKNOWN, Ladders | no company named | absent here too |
| Unknown client via Dexian | recruiter outbound | opportunity register here |

PhrasIQ is one of the thirteen interviewed applications.

The mechanism is worth stating plainly, because the paper argues hard for capturing origin. A
schema organized around **where a role came from** loses rows whose origin cannot be resolved. A
schema organized around **whether a submission can be proved** keeps them. Origin is the more
useful field and the more fragile one, and it must never gate inclusion. The paper's Discussion
now says so.

### 2.2 The workbook is missing 27 companies this census holds

After alias resolution, 27 companies appear here and nowhere in the workbook, 24 of them with
employer-side artifacts. Fullsteam and Toast are absent from every sheet of it.

Neither dataset is complete. The union is larger than either, which is the honest reading and is
also why neither can publish a completeness percentage.

| | Companies |
|---|---|
| In both | 237 |
| Only in the workbook, application-capable | 20 |
| Only in this repository | 27 |

Full row-level detail in `challenge/reconciliation__companies.csv`.

### 2.3 The outcome model does not survive contact

| Workbook | n | This repository | n |
|---|---|---|---|
| GHOSTED | 252 | still_open | 124 |
| REJECTED | 94 | rejected_no_interview | 74 |
| OFFER | 3 | role_paused_or_closed | 18 |
| APPLIED | 2 | rejected_after_interview | 5 |
| SCREENING, WITHDRAWN | 2 | | |

252 of 353 records labeled GHOSTED is not an observation. It is a residual, and the workbook says
so itself, in its own defect register, marked HIGH and OPEN:

> GHOSTED is an overloaded residual rather than one employer behavior. The category mixes
> applied-then-silence, inbound recruiter non-response, outreach inactivity ... The GHOSTED total
> cannot be interpreted as an applied-and-ignored rate without a behavior split.

This repository reports `still_open` for a live application and computes silence as a measured
quantity instead: 96 of 196 exact-dated applications drew no response beyond the receipt. That is
a number with a denominator and an observation window. GHOSTED is a label applied to whatever is
left.

### 2.4 Interviews are measured here and estimated there

`Interview Count` is `UNKNOWN` on **334 of 353** workbook records. The workbook's own register
flags the column as encoding several different states at once, and separately warns that only two
of seven rows labeled Phone Screen were confirmed completed.

This repository derives interviews from a timestamped events table, never stores the rollup, and
carries the derivation in code. It also publishes the weakness of that set honestly: both coders
independently found 10 of the 13, and event-level agreement is unmeasured.

Thirteen measured beats nineteen estimated, and the challenger's own defect register agrees.

## 3.1 The 19 title resolutions that rest on outside evidence

Beyond the 11 above, the challenger resolves 19 more titles from sources this corpus does not hold.
Its stated routes are specific and checkable in principle: "a contemporaneous job newsletter", "a
same-period LinkedIn job recommendation", "an archived contemporaneous job listing".

These are not adopted, and the reason is a distinction rather than a doubt. Each establishes **that
the company had an opening by that name in that period**. None establishes **which opening the
application was for**. A company running two openings makes the inference wrong without anything in
the data showing it. The eleven adopted above do not have this problem: a platform applied-list row
is a record of a specific submission, not of a posting that existed nearby.

One labeling defect is worth recording, because it is the kind of thing that makes a good workbook
look worse than it is. Eight rows carry `Role Title Resolution = "Exact title present in source
evidence"` while their own `Notes` say the role was absent or unresolved. Reading the notes resolves
it: each names a Jobright or LinkedIn source, so the title came from the platform log and the Gmail
receipt is what omitted it. The finding is right and the label is wrong. Those eight are a subset of
the eleven this repository has now adopted from its own copies of those same platform files.

## 3. Origin: the challenger has it, and it still cannot be adopted

The workbook assigns a normalized source category to **353 of 353** records. This census has a
known origin on **15 of 221**. On coverage there is no contest.

It is not adopted, for a reason that is about method rather than quality.

Those categories are another instrument's judgments, produced by a different process from a
different source set. Writing them into a blind-coded census would put a second, unblinded
instrument inside the dataset whose entire claim to rigor is that two coders read one frozen
corpus without seeing each other. The origin finding would then rest on an assignment nobody
could audit against an artifact.

The origin null result also is not really about coverage. It is about **when** the field is
captured. The workbook reconstructed origin after the fact, largely from which export a row
appeared in, which is why its categories skew toward the platform that recorded the row rather
than toward where the role was actually found. That is the same survivorship bias the Limitations
section already names, arriving through a different door.

What the challenger does change: it demonstrates that after-the-fact origin reconstruction is
**possible but weak**, where the paper implied it was impossible. That correction is going into
the paper.

The extracted categories stay in `challenge/checkpoint__source_classification.csv`, quarantined
and available to anyone who wants to argue the other way.

## 4. Capture recapture is still unmeasured, and now for a precise reason

The protocol restricts the estimator to LinkedIn rows submitted through an external ATS rather
than Easy Apply. The hope was that the formal export would carry that label.

**It does not.** Twenty rows mention "Easy Apply" in free text, and all twenty also carry a
downstream ATS confirmation, so the phrase is a generic descriptor of the export record rather
than a per-row channel flag.

What the export does give:

| LinkedIn rows | n |
|---|---|
| With downstream employer-side confirmation | 16 |
| With no employer-side confirmation | 83 |

The 83 mix two populations the estimator must separate: rows that were Easy Apply and therefore
**structurally invisible** to ATS mail, and rows that generated ATS mail which Gmail retrieval
**missed**. Only the second is informative about completeness. Nothing in the export distinguishes
them, and inferring the split from whether ATS mail was found would assume the very thing being
estimated.

Stop condition 3 is now **Met for the applied list** and **still Unmet for the channel label**.
This is a sharper statement than the repository had before, and it stays a refusal.

## 5. Adopted into Freeze 3

1. `artifacts/platform/linkedin_job_applications_export.csv`, 107 rows, as primary evidence.
2. The Hog and BX Studio reversed to `register = application`, by the existing adjudication rule
   applied to new evidence. Census 221 to 223, interviews 13 to 14.
3. Exact dates from the export applied to LinkedIn rows that previously carried relative stamps.
4. Stop condition 3 restated as partially met.

## 6. Not adopted, and why

| Not adopted | Reason |
|---|---|
| The 353-record count | Mixes both registers. Not comparable to 221 |
| Origin categories on 353 rows | Another instrument's unblinded judgments. Section 3 |
| GHOSTED and REJECTED outcomes | Overloaded residual, by the workbook's own admission |
| Interview counts | UNKNOWN on 334 of 353 |
| 53 LinkedIn recruiter threads | Mostly opportunity register. Deferred, not rejected |

## 7. Open after this pass

- **20 companies appear only in the workbook** and are not yet resolved row by row. Fifteen arrive
  through the adopted export. The remainder need artifacts before they can enter the census.
- **The Pogo cluster.** The workbook flags three GTM Engineer records across Gem and Ashby as
  possibly one to three requisitions. This repository holds them as one cycle on the same reasoning.
  Neither has requisition-level evidence.
- **A possible 2025-08-08 interview** the workbook cannot attribute to a company or role. If real,
  both datasets understate interviews.
- **The workbook's freshness boundary is 2026-08-23**, six days before the study window closes.
- **The 53 recruiter threads** are a channel this repository never harvested. They are almost
  entirely opportunity register, so they would not move the application census, but they would
  materially expand the opportunity side the paper currently describes only in aggregate.

## Provenance

Source: `combined_job_search_audit_checkpoint_updated.xlsx`, sha256
`5a5c012f3a438ef388ba5afb235d635ecdffb860c9a7979f647a581db402c0a9`, received 2026-08-30.

The workbook is **not committed**. It names real recruiters and this repository is public.
`challenge/extract_checkpoint.py` writes the redacted CSVs committed here, replacing every personal
name with a stable `per_<sha256[:12]>` pointer following the convention in
`scripts/redact_corpus.py`. No reverse map is committed.
