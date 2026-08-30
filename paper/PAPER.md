# What 223 Job Applications Actually Show

### A forensic census of one GTM engineering job search, and the question the data could not answer

*Working title. N = 1, and labeled as such throughout.*

No dashes are used as punctuation in this paper. Every number traces to a named view or script; the map is in `paper/NUMBERS.md`.

---

## Abstract

I spent fifteen months applying for go-to-market engineering roles, then treated my own job search as a dataset and tried to establish how many applications I could actually prove. Evidence was harvested from email, calendar, and platform exports into a frozen corpus, coded independently by two language models blind to each other, and resolved in a named adjudication pass. The result is 223 applications with employer-side proof, 317 including rows visible only in platform logs, and 14 that reached an interview, a rate of 14/223.

Three findings. Roughly half of all applications produced a receipt and then silence: 97/197 of the rows with an exact-dated receipt drew no response, and the median substantive response, among those that did respond, arrived in 7 days. All 14 interviews sat in three of eight role lanes, and the five lanes covering the other 83 applications produced none. Third, and most useful to anyone building a tracker: **the study could not answer the question it most wanted to answer.** Origin was captured at the time on 15 of 223 rows, recoverable afterwards on 60 more only because a platform logged them, and unrecoverable on the remaining 148. That is a failure of the instrument, and it is reproducible in almost any job-search log kept the ordinary way.

This is a single subject studied by himself: a case study, not a market study. A second, independently produced reconstruction of the same fifteen months was used to attack these numbers after they were written; the companion piece, [The Field You Cannot Recover](COMPANION.md), reports what it moved and what it failed to move.

## 1. Introduction

Go-to-market engineering is a new enough job title that neither side of the hiring table agrees on what it means. In this dataset the same lane covers 37 distinct titles, from "GTM Engineer" through "Lead, Agentic Operations + GTM Engineering". Companies posting the role are still deciding what it is. People trying to enter it, most of them arriving from adjacent disciplines, are guessing at what to call themselves.

There is no public dataset on how this role actually hires. Aggregate job-board statistics do not resolve to a funnel, and the funnel is what a candidate or a hiring team needs. In that absence, one carefully instrumented log is worth something, provided it is honest about being one.

Almost nobody knows how many jobs they applied to. Evidence scatters across ATS receipts, applied lists, aggregator agents, and calendar invites, and every source overlaps the others, so adding them up double counts. My own prior estimates ranged from 163 to 247 depending on which source I trusted, and a naive sum across four trackers would have reported roughly 315.

This paper has two subjects. The visible one is what fifteen months of applying produced. The one that generalizes is what it takes to make a personal funnel dataset survive being checked.

## 2. Methods

**Window and unit.** 2025-06-01 to 2026-08-29, America/New_York, fifteen months. The unit is one application cycle, keyed `company_canonical + role_as_listed + cycle`. Cycle is in the key because a re-application after a closed first attempt is a second row, and a key without it collapses the pair. Two such pairs exist here, and in both the rejection on the first cycle licenses the second.

**Two registers, one denominator.** Applications are roles I submitted. Opportunities are referrals, recruiter-initiated processes, and matching-platform contracts where no submission exists. Both stay in the dataset; only applications are ever a denominator. The opportunity register contains three engagements that converted to paid work, so the rows that would inflate the conversion rate are the ones with the good outcomes, which is exactly why this contamination usually goes uncaught.

**Retrieval with a stop condition.** Twenty-two queries, each with a stable id, an intent, a date window, and a termination condition the source reports: done only when the API returns no next page. Four of seven stop conditions remain Partial or Unmet, and the census is reported as bounded by those gaps. One lesson is in the protocol: searching the calendar for "interview" returned zero events, because interview loops lived inside invites titled "30 minute meeting". Sweeping in 90-day blocks with no keyword returned 31.

**Blind independent coding.** The codebook was frozen, then the corpus, then two language-model coders extracted the same artifact set into the same tables without seeing each other's output. Disagreements were counted before anyone resolved them. This is what makes the categories measurable rather than assertable.

**Derived, never stored.** Whether an application was interviewed is computed from the events table on every run, never written on the application row. A stored rollup and a stored event list will eventually disagree, and then neither can be trusted. Section 5 reports what happened where this was applied in one direction and not the other.

**Precision as a field.** Every date carries a precision label. A LinkedIn stamp reading "2mo ago" is never upgraded to a calendar date, because it is a range and writing a date would convert a range into a false fact. The monthly series runs on 195 exact-dated rows with the 26 excluded printed beside it.

**Reproducibility.** One command, `make check`, rebuilds every published figure from the frozen inputs, hashing every output before and after and failing if a re-run moved a byte. It passes, so the numbers below are reproducible rather than merely recorded.

## 3. Results

### 3.1 The funnel

| Stage | n | Against |
|---|---|---|
| Applications with employer-side proof | 223 | the census |
| Full census including platform-only rows | 317 | census plus 94 net-new |
| Applications reaching at least one interview | 14 | 14/223 |
| Applications with any response beyond the receipt | 100 | 100/197 exact-dated base |
| Applications with a substantive response | 79 | 79/197 |
| Applications with no response at all | 97 | 97/197 |

Three denominators are in play and they are not interchangeable. 223 is the census. 197 is the subset carrying an exact-dated receipt, the only rows where a response time can be computed. 317 adds 94 rows visible only in platform exports, which carry no employer-side artifact and therefore no events, so an interview rate against 317 is arithmetically smaller for a reason unrelated to the search.

The plainest line in the funnel is the one worth keeping: **roughly half of all applications produced a receipt and then nothing.**

### 3.2 The finding that is an absence

The question this study most wanted to answer is which origination channels convert. It cannot.

`discovery_source` reads `unknown` on 208 of 223 census rows, 93.3 percent. The structure underneath that number is what matters: on the full census, 88 rows know they came from LinkedIn and **zero** of them have an observable outcome, because a platform applied-list row carries no employer-side artifact and therefore no events. The rows that do have outcomes are the 208 whose origin is unknown. **Origin is known almost exactly where outcome is not**, and the overlap that could answer the question is 15 rows of 223.

It is not simply gone, which is a correction to an earlier draft of this paper. Splitting the census by how origin could be recovered gives three tiers:

| Recovery tier | n | Share |
|---|---|---|
| Captured at write time | 15 | 6.7 percent |
| Recoverable later, only because a platform export recorded the row | 60 | 26.9 percent |
| Unrecoverable by any route | 148 | 66.4 percent |

The middle tier is a proxy and a biased one: it recovers the platform that *recorded* the application, not where the role was found, and only where a platform kept a log. The bottom tier, two thirds of the census, is evidenced entirely by employer-side mail, and an ATS receipt never says where the applicant found the posting.

This is not a withheld analysis. There is no analysis to withhold. The field existed in the schema from the beginning; the data never got into it, because at the moment of applying, where I found the role felt like the least important thing to write down.

`company_stage` is worse still. It does not exist in the schema at all, so no cut by company size or stage is available anywhere in this dataset.

**The full treatment is in the companion piece, [The Field You Cannot Recover](COMPANION.md)**, along with why no completeness percentage is published and what a second, independently produced reconstruction of this search did to these numbers.

### 3.3 Role lane and title language

All 14 interviews sit in three of eight lanes.

| Role lane | n | Interviewed | Rate | Wilson 95 percent |
|---|---|---|---|---|
| explicit_gtm_engineering | 92 | 10 | 10/92 | 0.060 to 0.189 |
| sales_bd_partnerships | 31 | 0 | 0/31 | 0.000 to 0.110 |
| unspecified | 25 | 2 | 2/25 | 0.022 to 0.250 |
| growth_demand_marketing | 23 | 2 | 2/23 | 0.024 to 0.268 |
| other | 18 | 0 | 0/18 | 0.000 to 0.176 |
| sales_solutions_engineering | 16 | 0 | 0/16 | 0.000 to 0.194 |
| revops_gtm_ops_strategy | 10 | 0 | 0/10 | 0.000 to 0.278 |
| product_ai_technical | 8 | 0 | 0/8 | 0.000 to 0.324 |

Five lanes covering 83 applications produced no interviews at all. That is the strongest pattern in the dataset, and the intervals show how much weight it can bear: the upper bound on the zero lanes runs from 0.11 to 0.32, so "zero" is consistent with a true rate near the explicit-GTM rate in the smaller lanes. What the data supports is that adjacent-title applications did not visibly outperform on-title ones, not that they cannot.

Within explicit GTM engineering, titles carrying seniority or founding language show the highest rate in the set, 3/7, with a Wilson interval of 0.158 to 0.750. The interval is the finding. A 43 percent point estimate on seven rows is not a result, and quoting it without the interval is quoting noise.

The whole interview set is small enough to print, which is itself the honest way to present it. Ten of the fourteen titles carry GTM or go-to-market language.

Two of the titles below were not in the Gmail receipt at all. They were recovered at Freeze 3.1 from platform exports already in the corpus, which is described in the companion piece.

| Company | Title as listed | Lane | Terminal outcome |
|---|---|---|---|
| Beautiful.ai | unspecified | unspecified | rejected after interview |
| Dagster Labs | GTM Engineer | explicit GTM | rejected after interview |
| Every.to | GTM Engineer | explicit GTM | still open |
| Great Question | Senior Demand Generation Manager | growth | rejected after interview |
| HartleyCo | Founding GTM | explicit GTM | rejected after interview |
| Hologram | GTM Engineer Pre-Sales | explicit GTM | still open |
| Hypergen | GTM Engineer | explicit GTM | still open |
| jobmail.io | Growth Lead | growth | see note |
| Orchestry | GTM Engineer (Sales) | explicit GTM | rejected after interview |
| Pearl | Lead GTM Engineer | explicit GTM | still open |
| PhrasIQ | unspecified | unspecified | still open |
| RevSpring | Lead, Agentic Operations + GTM Engineering | explicit GTM | still open |
| TestGorilla | Go-to-Market Engineer | explicit GTM | still open |
| The Hog | GTM Engineer | explicit GTM | still open |

Two rows carry a caveat. The jobmail.io row is the contradiction described in section 5: it carries an interview event and a stored outcome of `rejected_no_interview`, from one coder, with no blind second reading. The Hog entered the census only at Freeze 3, when a submission artifact for it was found; the companion piece gives that story.

Correlation and causation are not close here. I chose which roles to apply to, so title language is confounded with where I was a plausible fit, with what I was willing to spend effort on, and with market timing. Nothing is randomized, and no causal claim is available.

### 3.4 Response latency

Computed only on rows where both dates are exact, n = 197, with the 26 excluded rows reported alongside.

| Definition | n responders | Median days | p25 | p75 | Mean | Max | Same-day share |
|---|---|---|---|---|---|---|---|
| Substantive, excludes automated acknowledgment | 79 | 7 | 3 | 19 | 15.1 | 140 | 9, 11.4 percent |
| Any response, includes acknowledgment | 100 | 5.5 | 1 | 15 | 12.8 | 140 | 22, 22.0 percent |

Two definitions are published because the choice moves the number, and it is not the analyst's to make silently. The same-day share roughly doubles when automated acknowledgments count, which is what a receipt and an acknowledgment arriving together looks like. Both distributions are right skewed, so the median is the statistic to quote.

The medians are conditional on having responded. They describe responders only. Folding in the 97 silent applications would drop them from the denominator, which is the same error the two-register split exists to prevent on the interview rate.

Time to first interview: n = 11, median 6 days, mean 8.8, range 0 to 34.

Right censoring is not driving the response rate. Applications submitted near the window end have had less time to draw a reply, so the rate was recomputed at rising exposure thresholds: 0.510 at 0 days, 0.508 at 30, 0.532 at 60, 0.500 at 90. Stable.

### 3.5 Timeline

Exact-dated applications per month, n = 196, with 27 non-exact rows excluded and printed here rather than hidden: 2025-06 5, 2025-07 19, 2025-08 16, 2025-09 0, 2025-10 0, 2025-11 1, 2025-12 2, 2026-01 7, 2026-02 10, 2026-03 21, 2026-04 27, 2026-05 22, 2026-06 28, 2026-07 33, 2026-08 5.

Zero in September and October 2025 is a count of exact-dated rows, not a claim that nothing happened. At least one application in that gap is dated only by an evidence bound. Prior audits that read the same period as near-empty were reading a search-boundary artifact: they had searched only from 2025-08-25 forward, which made five unharvested months look like a quiet period.

### 3.6 How much to trust the coding

| Statistic | Value |
|---|---|
| Rows coded, bravo / cursor / intersection | 228 / 231 / 211 |
| Role lane percent agreement | 0.9621 |
| Role lane Cohen's kappa | 0.9510 |
| Include or exclude percent agreement | 0.9905 |
| Include or exclude kappa | 0.7452 |
| Interview set found by both coders | 11 of 14 |

The 24-point gap between the two include statistics is the whole reason kappa exists. Almost every record was an include, so two raters guessing "include" every time would agree nearly as often. The honest number is the lower one, and it rests on two disagreements.

Those same two disagreements are the ones Freeze 3 later reversed. They were the only rows where the coders split on whether a record counted at all, and new evidence eventually showed that on both, one coder was right and the adjudication was wrong. A kappa of 0.7452 on two contested rows was, in hindsight, pointing exactly where the weakness was. The companion piece has the reversal in full.

The last row is the one that should temper everything above it. Agreement on *which applications were interviewed* is 11/14. Three rest on one coder alone. Event-level agreement is not among the reliability statistics the protocol requires, so it is unmeasured rather than measured and small, and the interview-based findings inherit that.

## 4. Discussion

### 4.1 For companies designing a GTM engineering hiring motion

Three things in this data are actionable from the employer side.

**Half your applicants hear nothing after the receipt.** Here 97/197 applications produced an automated receipt and then silence. That is one candidate's view of many companies, so read it as a market norm rather than an indictment of any firm. The norm is the opportunity: the median substantive response arrived in 7 days, p75 19. A team that reliably responds inside a week is not competing against a high bar.

**Your title is doing recruiting work you have not accounted for.** This dataset contains 37 distinct titles inside a single role lane. When the same job is posted as GTM Engineer, Founding GTM, Lead Agentic Operations, and Go-to-Market Engineer, applicants cannot search for it and cannot tell whether they are qualified. The internal cost is a smaller and worse-sorted pipeline. The external cost is that nobody can build the labor-market data that would tell you what to pay.

**Distinguish the acknowledgment from the response in your own metrics.** That choice moved this study's median from 5.5 days to 7 and doubled the same-day share. If your ATS reports time-to-first-touch counting the auto-acknowledgment, your reported responsiveness is measuring your mail server.

### 4.2 For someone moving into GTM engineering from another discipline

I came to this from a biochemistry research background, so this section is the one I would have wanted.

**Apply on-title, and expect the adjacent lanes to be quieter.** Every interview in this log came from three of eight lanes. The other five, covering 83 of 223 applications across sales, solutions engineering, RevOps, product-adjacent, and miscellaneous titles, produced none. The intervals do not permit "those lanes do not work". They do support a resource-allocation reading: the adjacent-title strategy did not visibly outperform here, and it consumed more than a third of the applications.

**Expect a low rate and budget accordingly.** 14/223 is the honest headline. Most applications end in silence rather than rejection, so a pipeline built on applications alone gives very little to steer on. Half of what you send never resolves into anything you can learn from.

**The second pipeline is the one that paid.** Every engagement that converted to paid work in these fifteen months came through the opportunity register rather than the application register: referrals, recruiter-initiated processes, and matching platforms. Keeping those out of the application denominator is what makes the observation visible. Mixed together, applying would look more effective than it was, and I would have done more of the thing that was not working.

**Record where you found it, at the moment you apply.** See below. This is the single highest-value thing in this paper for a job seeker, and it costs one field.

### 4.3 For anyone tracking a funnel, in any domain

The subject matter here is incidental. The transferable practice is not.

**Decide what one row means before you decide what columns it has.** Every wrong number in this project's prior audits was a grain error, not a field error: a rejection thread counted as a second application, a recruiter process counted in an application denominator, a re-application collapsed into its first attempt.

**Capture origin at write time, because only a third of it is recoverable later.** This is the paper's central practical finding, and it cost the study its headline analysis. Sixty of 223 rows here could have origin reattached afterwards, but only because a platform kept its own log, and what that recovers is the platform that recorded the application rather than where the role was found. For the other 148 the only evidence is employer-side mail, and a receipt never says where you found the posting. One required field at the moment of the event would have made the whole channel analysis possible.

**Never let a fragile field gate inclusion.** The competing reconstruction organized around origin and dropped eight applications this study proves with employer artifacts, one of which produced an interview. Record origin, and separately record whether a submission can be proved. Only the second decides whether a row counts.

**Give yourself a legal way to say "I do not know".** `unknown` is a recorded observation, not a missing value. Without it a tracker fills gaps with plausible guesses, and you can no longer tell an observation from an inference.

**Store observations and compute rollups.** Section 5 has a live example of what happens when you do not.

**Suppress small cells, and keep the row.** A group that disappears is indistinguishable from a group that never existed. Keep the n, blank the rate, say why.

**Write down what would reverse each exclusion.** Every excluded row carries a `what_would_promote_it` column naming the artifact that would put it back. Two rows were reinstated by exactly that route, which turns an exclusion list into a work queue rather than a graveyard.

**Split any funnel with an inbound and an outbound motion into two registers.** Only one is ever a denominator. The contaminating rows usually have the best outcomes, which is why nobody catches this on their own data.

## 5. Limitations

**N = 1, and the subject is the author.** Nothing here estimates a population parameter, and no reader should treat 14/223 as a rate to expect.

**Self-authored, and it showed.** One correction came from me, from recall, after I had seen the analysis. It was right, and a blind coder had independently reached nearly the same conclusion, but the provenance is the exact failure mode blind coding exists to prevent, and it is disclosed rather than smoothed.

**A stored field contradicts a derived one.** One application carries an interview event and a terminal outcome of `rejected_no_interview`, both from the same coder on a row the other never saw. No published count moves, because interviewed is derived, but the contradiction is left open rather than resolved by preference.

**Two figures here already changed once.** The census was 221 and the rate 13/221 until a second reconstruction supplied submission artifacts for two rows adjudicated out. The process working, and also direct evidence that these numbers are bounded by what has been found, not by what happened.

**The census is not complete and does not claim to be.** Four of seven stop conditions are Partial or Unmet, and no completeness percentage is published: the estimator requires two sources that could each have seen the same record, and LinkedIn Easy Apply generates no ATS mail, so the two here are near-disjoint by construction.

**Selection bias in what got logged, survivorship bias in origin.** Applications that produced no artifact anywhere are invisible by construction, and they are disproportionately the ones that went nowhere. The rows that do know where they came from are the ones a platform recorded, which is a biased sample of channels.

**Coders are language models, not a human gold standard.** Agreement between two models measures reproducibility of the coding rule, not correctness, and only on role lane and the include decision. Event-level agreement is unmeasured, and that is where the interview set lives.

**Three rows carry a city name in the workplace-type column.** They survived two coders, an adjudication pass, and two published CSVs, and were caught only when a second reader looked. The coder files are left uncorrected, because editing them retroactively would destroy the agreement statistic. Exactly the defect a second reader catches and a solo author never does.

## 6. Conclusion

Fifteen months, 223 provable applications, 14 interviews, and half the funnel ending in silence. Those numbers are worth what a single case is worth, which is not nothing and is not much.

The part I would keep is the absence. I built a schema with an origin field in it from the start and still could not answer which channels worked, because the field sat empty at the only moment it could have been filled. That failure is not specific to job searches or to this role. It is what happens to any funnel dataset assembled after the fact, and one required field at write time prevents it.

---

## Appendix A: Schema summary

Full version in `schema.md`.

| Table | Grain, one row per | Key |
|---|---|---|
| `applications` | application cycle | `company_slug\|role_slug\|c{n}` |
| `events` | timestamped interaction on one application | `{application_id}\|e{n}`, foreign key to applications |
| `exclusions` | candidate considered and rejected | `candidate_id` |
| `platform_match` | platform export row and its resolution | export row, carrying `match_status` |

Interviewed, rounds, days to response, and days to interview are derived from `events` and never stored.

## Appendix B: Origin taxonomy

Full lookup in `pipeline/origin_taxonomy.csv`. It maps every raw origin value to a normalized channel and a family, and the pipeline fails if the data contains a value the lookup does not cover.

| Family | Channels |
|---|---|
| professional_network | linkedin |
| job_board | ladders |
| talent_marketplace | wellfound, marketplace_profile |
| agent_platform | jobright, apply4me |
| employer_direct | employer_ats, email_direct |
| recruiter_inbound | recruiter_inbound, recruiter_submitted |
| network_warm_intro | referral |
| unknown | unknown |

## Appendix C: Starter kit

A blank tracker you can copy, with the validation rules that make it checkable. The columns marked required are the ones this study wishes it had enforced.

| Column | Required | Values | Note |
|---|---|---|---|
| `application_id` | yes | `company\|role\|c{n}` | Cycle in the key or re-applications collapse |
| `company_canonical` | yes | free text, normalized | Keep the verbatim version in a second column |
| `role_as_listed` | yes | verbatim, or `unspecified` | Never guess a title |
| `date_applied` | yes | ISO date | |
| `date_precision` | yes | exact, relative_display, evidence_bound, unknown | Never upgrade a relative stamp |
| **`discovery_source`** | **yes** | your channel list, plus `unknown` | **Fill this at write time. It is the field this study lost.** |
| `submission_channel` | yes | your channel list, plus `unknown` | How it was sent, which is a different question |
| `register` | yes | application, opportunity | Only one is ever a denominator |
| `evidence_class` | yes | employer_artifact, platform_log | Gates whether an outcome is observable |
| `terminal_outcome` | no | controlled list | Leave empty while open. Do not store `interviewed` |

**Validation rules to run on it.**

1. No two rows share an `application_id`.
2. Every event's `application_id` exists in the applications table.
3. Every categorical value is in its controlled list. Report violations, do not silently fix them.
4. Same company plus same role within 7 days is a candidate duplicate. Report the pairs you cleared, not just the ones you flagged, so an empty result means something.
5. A second cycle requires a terminal outcome on the first.
6. Any derived flag that contradicts a stored field is a defect. Report it.
7. Classify every row by what it can answer, and report the share that cannot answer your main question. If that share is high, that is the finding.

---

## Suggested pull quotes

1. "Roughly half of all applications produced a receipt and then nothing."
2. "Origin is known almost exactly where outcome is not."
3. "The rows that would inflate the conversion rate are the ones with the good outcomes, which is exactly why this contamination usually goes uncaught."
4. "A 43 percent point estimate on seven rows is not a result. The interval is the finding."
5. "I built a schema with an origin field in it from the start, and still could not answer which channels worked, because the field sat empty at the only moment it could have been filled."
