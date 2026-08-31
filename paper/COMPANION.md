# The Field You Cannot Recover

### What a second reconstruction of the same job search did to my numbers, and what it proved about the one field I failed to capture

*Companion to [What 223 Job Applications Actually Show](PAPER.md). N = 1, and labeled as such throughout.*

No dashes are used as punctuation in this piece. Every number traces to a named view or script; the map is in [NUMBERS.md](NUMBERS.md).

---

## Why this is a separate piece

The parent paper reports what fifteen months of applying to go-to-market engineering roles produced: 223 applications with employer-side proof, 14 that reached an interview, and roughly half the funnel ending in silence.

Two things did not fit inside it, and both are more useful than the funnel.

The first is the question the study most wanted to answer and could not: **which origination channels actually convert.** The second is what happened when a second, independently produced reconstruction of the same fifteen months showed up after the analysis was finished and was used to attack it.

They belong together because they turned out to be the same story. The challenger lost on coverage for exactly the reason the origin field is dangerous.

## Part 1: the question with no answer

### What was asked, and what is there

Every job-search tracker is built to answer one question eventually: where should I spend my effort. Referrals or cold applies. LinkedIn or the company site. A recruiter's inbox or my own outbound.

The schema had a field for it from the first day. `discovery_source`, a controlled vocabulary, one of ten values, with `unknown` available so a coder always had a legal way to say "I could not tell."

That field reads `unknown` on **208 of 223** census rows. 93.3 percent.

A 93 percent gap is a coverage problem. What makes it worth a piece of its own is the shape underneath it.

| Stratum | Rows knowing their origin | Of those, rows with an observable outcome |
|---|---|---|
| Application census, 223 | 15 | 15 |
| Full census, 317 | 109 | 15 |

On the full census, **88 rows know they came from LinkedIn and zero of them have an observable outcome.** A platform applied-list row carries no employer-side artifact, so it has no events, so nothing ever happens to it in the data. Meanwhile the 208 rows that do have outcomes are precisely the ones whose origin is unknown, because their only evidence is employer-side mail, and an ATS receipt never says where you found the posting.

**Origin is known almost exactly where outcome is not.** The two facts sit in complementary halves of the dataset, and the overlap that could answer the question is 15 rows out of 223, spread across five channels, the largest of which holds 7.

The sharpest version of it is in the response-latency slices. Cut by origin, the only group large enough to publish a median response time is the group labeled `unknown`.

### It is not simply gone, and the difference matters

An earlier draft of the paper stated this as a flat 93 percent unknown, which implies the information no longer exists anywhere. That was too strong, and the challenger is what forced the correction.

Splitting the census by *how* origin could be recovered gives three tiers, not two.

| Recovery tier | n | Share |
|---|---|---|
| Captured at write time | 15 | 6.7 percent |
| Recoverable later, only because a platform export recorded the row | 60 | 26.9 percent |
| Unrecoverable by any route | 148 | 66.4 percent |

The middle tier is real and it is weak. Those 60 rows can have an origin attached after the fact by matching a LinkedIn or Jobright export against the census. But what that recovers is the platform that *recorded* the application, which is not the same as where the role was found, and it is available only where a platform happened to keep a log. It is a proxy, and a biased one: it can only ever tell you about channels that write things down.

The bottom tier is two thirds of the census. For those the information is gone in the ordinary sense. Nothing recovers it.

The recovered values are deliberately **not** written back into `discovery_source`. The coded field stays as the two blind coders left it, with the recovery sitting beside it in `views/origin_recoverability.csv`. A derived value overwriting a coded one would make the census unauditable against the coder tables, and the whole claim to rigor here rests on being able to trace any row back to what a coder actually read.

### Why no completeness percentage either

The same gap kills the estimator that would say how much of the search was captured at all.

Two-source capture recapture needs two sources that could each have observed the same record. The pre-registered plan restricted it to LinkedIn rows submitted through an external applicant-tracking system rather than Easy Apply, because Easy Apply generates no employer mail and is therefore invisible to the other source by construction.

The LinkedIn data download that arrived with the challenger was the best remaining chance at that label. It does not carry one. Twenty rows mention "Easy Apply" in free text and all twenty also carry a downstream ATS confirmation, so the phrase describes the export record rather than the channel.

What the export does give:

| LinkedIn rows | n |
|---|---|
| With downstream employer-side confirmation | 16 |
| With no employer-side confirmation | 83 |

The 83 mix two populations the estimator has to separate: rows that were Easy Apply and therefore structurally invisible to ATS mail, and rows that did generate ATS mail which the Gmail sweep missed. Only the second is informative about completeness. Nothing in the data distinguishes them, and inferring the split from whether ATS mail was found would assume the very thing being estimated.

So no completeness figure is published. A completeness figure with a method and a caveat is publishable. One asserted from feel is not.

One more absence, stated plainly because it is easy to miss: **`company_stage` does not exist in this schema at all.** No cut by company size or stage is available anywhere in this dataset. That is not a suppressed cell, it is a missing instrument.

## Part 1b: the field the census had and was not reading

There is a second version of this failure, and it is less forgivable than the first.

Forty census rows carried `role_as_listed = unspecified`. Coding them that way was correct: the
Gmail receipt genuinely omits the role, and counting rule 8 forbids guessing one.

But absent from the Gmail artifact is not the same as absent from the corpus. For **11 of those 40**
the title was sitting in plain text in the Jobright tracker and the LinkedIn export, both committed
in this repository. The record matcher had seen those rows, marked them `overlap`, kept the Gmail
row wholesale, and discarded the title the platform row was carrying.

The challenger is what surfaced it. It resolves titles down to 8 unrecoverable rows against this
census's 40, and reading its resolutions carefully is what sent me back to my own artifacts.

Applied at Freeze 3.1, with strict company matching and a refusal on any company carrying more than
one platform title: unspecified role lanes fall from 36 to 25, `explicit_gtm_engineering` gains 5
rows, and every backfilled title matches what the challenger gives independently. The census, the
interview count and the latency base are unchanged. `application_id` is deliberately not
regenerated, because the events tables join on it.

Nineteen further titles the challenger resolves are **not** adopted. Its routes are specific, a
contemporaneous job newsletter or a same-period LinkedIn job recommendation, and each establishes
that the company had an opening by that name in that period. None establishes which opening the
application was for, and a company running two openings makes the inference wrong with nothing in
the data showing it. A platform applied-list row does not have that problem: it is a record of a
submission, not of a posting that existed nearby.

## Part 2: the challenger

### What arrived

On 2026-08-30, after the corpus was frozen, after two language models had independently coded it blind, and after adjudication was closed, a second reconstruction of the same fifteen months appeared. It was built separately from a different source set, including a LinkedIn data download and a LinkedIn message export this study never had. It holds **353 records** against this study's 317.

It is not a third coder, and the distinction is not pedantic. The pre-registration requires every coder to receive an identical corpus, on the grounds that "a coder who sees more artifacts is not a second rating, it is a different study." So no agreement statistic is computed against it. It is a challenger: the useful question is not whether the two agree but what each holds that the other does not, and who is right in each direction.

Its 353 is also not comparable to 223. It mixes recruiter outreach, cold outreach, marketplace and referral rows into one total, where this study keeps those in a separate register that never enters an application denominator. Its own summary sheet calls the count a checkpoint that "may still exceed the number of unique employer requisitions."

The full technical reconciliation is in [`challenge/CHALLENGE.md`](../challenge/CHALLENGE.md).

### Where it won

**The LinkedIn data download is a genuine artifact and it is now in the corpus.** 107 rows, each with a job ID, a job URL, and an exact application date, against the 99 relative stamps ("2mo ago") this study had been working from. Relative stamps can never be upgraded to calendar dates without converting a range into a false fact, so every scraped row had been barred from the monthly series and from all response-time figures. After ingesting the export, the full census holds 284 exact dates of 317 with only 6 relative stamps left.

**And it overturned two adjudications.** The export contains submission rows for two companies, The Hog and BX Studio, dated 2026-06-04 and 2026-04-06.

| Company | Submission in the export | First process event already recorded here | Gap |
|---|---|---|---|
| The Hog, Founding GTM Engineer | 2026-06-04 | interview invitation 2026-06-15 | 11 days |
| BX Studio, GTM Engineer | 2026-04-06 | employer acknowledgment 2026-04-08 | 2 days |

Those two rows were the **only** include-or-exclude disagreements between the blind coders, the pair that produced the include kappa of 0.7452. Both had been adjudicated into the opportunity register on one stated ground: no submission artifact existed anywhere in the corpus. An interview with no submission does not mint an application row.

The rule did not change. Its premise did. A submission now exists for each, dated before the process events, which is the corroboration pattern that makes them submissions rather than coincidence.

| | Before | After |
|---|---|---|
| Application census | 221 | **223** |
| Interviewed applications | 13 | **14** |
| Application to interview rate | 13/221 | **14/223**, then **11/223** and **10/223** at Freeze 4 |
| Full census | 298 | **317** |

This is the exclusion design working exactly as intended. Every excluded row in this study carries a `what_would_promote_it` column naming the specific artifact that would put it back. This was that artifact arriving, fifteen months later.

It is also a caution. The adjudication was correct on the evidence available and still produced the wrong answer for over a year. That is what a bounded census means in practice, and it is why the paper's Limitations now says these numbers are bounded by what has been found rather than by what happened.

### Where it lost

**Eight of the ten rows it drops for unresolvable origin are in this census with Tier A employer artifacts.**

| Company | Its reason for exclusion | Status here |
|---|---|---|
| Lattice | Ladders, origin unresolved | application, Tier A |
| Firstup | Ladders, origin unresolved | application, Tier A |
| Ava Labs | Wellfound, origin unresolved | application, Tier A |
| Fibr AI | Wellfound, origin unresolved | application, Tier A |
| 12100 Collective | Wellfound, origin unresolved | application, Tier A |
| Infisical | Wellfound, origin unresolved | application, Tier A |
| PhrasIQ | Wellfound, origin unresolved | application, Tier A |
| Classet | Wellfound, origin unresolved | application, Tier B |

PhrasIQ is one of the ten interviews.

**It is also missing 27 companies this census holds**, 24 of them with employer-side artifacts. Fullsteam and Toast appear on no sheet of it at all. Running the comparison the other way, 20 companies appear only in the challenger. Neither reconstruction is complete, and the union of the two is larger than either.

**Its outcome model does not survive contact.** It labels 252 of 353 records GHOSTED. Its own defect register, to its credit, marks that HIGH and OPEN and says the category "mixes applied-then-silence, inbound recruiter non-response, outreach inactivity" and "cannot be interpreted as an applied-and-ignored rate." This study reports `still_open` for a live application and computes silence as a measured quantity instead: 97 of 197 exact-dated applications drew no response beyond the receipt. That is a number with a denominator and an observation window.

**Its interviews are estimated, not measured.** `Interview Count` reads UNKNOWN on 334 of its 353 rows. This study derives interviews from a timestamped events table, never stores the rollup, and publishes the weakness of that set honestly: both coders independently found 11 of the 14, and event-level agreement is unmeasured.

### The finding underneath

Here is why the two halves of this piece are one story.

**A schema organized around where a role came from loses rows whose origin cannot be resolved. A schema organized around whether a submission can be proved keeps them.**

The challenger built its ledger around origin. When origin was unresolvable, the row went to an excluded sheet. Eight provable applications went with it, one of which produced an interview. This study built its ledger around evidence of submission, kept those eight, and separately admitted it did not know where they came from.

Origin is the more useful field. It is also the more fragile one. Those two facts together are the whole argument: **record origin, and never let it gate inclusion.** They are different jobs and they need different fields.

## What to do with this in your own tracker

Five things, in the order they will save you the most.

1. **Capture origin at the moment you apply.** Not later. Later is 60 rows out of 223, recovered through a proxy, and only where a platform kept a log. It costs one dropdown at the one moment the information exists.

2. **Never let origin decide whether a row counts.** Inclusion is decided by whether you can prove the thing happened. Origin is an attribute of a row that already counts.

3. **Give yourself a legal way to say "I do not know".** `unknown` is a recorded observation, not a missing value. Without it a tracker fills gaps with plausible guesses and you can no longer tell an observation from an inference.

4. **Write down what would reverse each exclusion.** One column, naming the artifact that would put the row back. Two rows came back here by exactly that route when the evidence finally arrived. It turns an exclusion list into a work queue instead of a graveyard.

5. **Do not label your residual.** "Ghosted" is not an observation, it is everything left over after the things you could name. Report silence as a count against a denominator with an observation window attached.

## Limitations of this piece

Everything in the parent paper's Limitations applies here, and two more besides.

**The comparison is at company grain, not row grain.** The two datasets count different units, so matching row to row would manufacture agreement or disagreement out of a units mismatch. Company presence is the coarsest claim both actually make.

**The company matching fails toward merging.** An unmerged pair invents a coverage gap that does not exist and overstates the challenge, so the reconciliation strips legal suffixes aggressively and every residual gap is listed in full rather than reported as a bare count. This runs opposite to the census matcher, which refuses ambiguous merges because there a wrong merge destroys a record.

**The challenger's freshness boundary is 2026-08-23**, six days before the study window closes. Anything after that is not in it.

---

## Suggested pull quotes

1. "Origin is known almost exactly where outcome is not."
2. "A schema organized around where a role came from loses rows whose origin cannot be resolved. One organized around whether a submission can be proved keeps them."
3. "The adjudication was correct on the evidence available and still produced the wrong answer for over a year."
4. "Eight provable applications went into an excluded sheet because nobody could establish where they came from. One of them had produced an interview."
5. "Ghosted is not an observation. It is everything left over after the things you could name."
