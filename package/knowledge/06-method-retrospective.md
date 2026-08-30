<!-- kit-meta
file: 06-method-retrospective.md
tier: 0 (durable)
created: 2026-08-30
sources: [logs 001-042] [protocol.md] [03-codebook.md]
status: Sections 1-3 are findings. Section 4 is a reusable artifact.
-->

# Method retrospective, confidence assessment, and the prompt that should have started this

## 1. The confidence question, answered honestly

**We are not at 95 percent, and a single completeness number is the wrong instrument.** Completeness differs by stratum by an order of magnitude, and the weakest stratum is the one Results depends on most.

### The saturation curve is the honest estimator

`protocol.md` correctly rejects an asserted completeness figure. The best available evidence is **marginal yield per probe**: when new queries stop returning new material, the corpus is approaching saturation.

**Every targeted probe in the last several rounds returned new material.**

| probe | yield |
|---|---|
| Q7, interview language | six complete or near-complete processes inside a window both prior audits treated as empty |
| LinkedIn export (log 035) | 87 net-new applications, plus three processes whose submissions existed nowhere else |
| Dagster Labs (log 040) | a held interview absent from the headline count |
| Orchestry (log 041) | a held interview recorded as missed |
| Subject register (log 042) | `discovery_source` for nine processes, one entirely new entity, two reclassifications |

**Five probes, five finds, hit rate approaching 100 percent.** A saturation curve that has not begun to flatten is direct evidence of distance from completeness. Claiming 95 percent against that curve would be asserting the opposite of what the data shows.

### Completeness by stratum

| stratum | state | why |
|---|---|---|
| **LinkedIn applications** | **High** | Export in hand, all 105 dedupe-resolved. **But Attentive's second cycle is in Gmail and absent from the export**, so the export itself is not proven complete |
| **Gmail employer artifacts** | **Moderate to high for queries run** | Q1, Q2a-d, Q3, Q4, Q5, Q7, Q7b exhausted, 1,152 threads. **Q3b, Q6, Q9, Q10 never run.** Q9 alone re-runs Q1 across spam and trash |
| **Event / interview layer** | **Low. This is the weakest stratum** | Two probes, two errors, opposite directions. Calendar blocks 4 to 6 unswept. Every rate in Results divides by this layer |
| **Opportunity register** | **Low** | Doug Shankman appeared from nothing in log 042. There is no systematic instrument for counterparty-initiated processes; they surface by accident |
| **`discovery_source`** | **Near zero from artifacts** | Unrecoverable from email for most rows. Currently ~100 percent recall-dependent. Not fixable by more retrieval |
| **Engagements (Table 4)** | **Moderate** | Five spans evidenced, Q12 unexhausted, `33@lecturesfrom.com` never swept, five descriptions unwritten |

### What is still unopened

Four Gmail queries. Three calendar blocks. One paginated query. Four platform exports (Ladders, Jobright, YC WFS, Wellfound). One mailbox. Three LinkedIn export files. 114 inbound conversations untriaged.

### The honest statement for Methods

> Census completeness is reported per stratum, not as a single figure. At the time of writing, marginal yield per retrieval query had not begun to decline, which is inconsistent with saturation. The application census is materially more complete than the event layer, and the event layer is the denominator for every conversion rate reported here.

**What would move it fastest**, in order of yield per hour: (1) calendar blocks 4 to 6 under the inverted method in section 2; (2) Q9, spam and trash; (3) the four platform exports; (4) `33@lecturesfrom.com`.

---

## 2. The instrument hierarchy was inverted, and it caused both interview errors

**The subject is right and this is the single largest method error in the project.**

The study was built email-first: Gmail swept exhaustively across ten query families, calendar treated as supplementary and swept in three of six blocks. But **email and calendar answer different questions, and the project asked email a question calendar answers better.**

| instrument | the question it actually answers |
|---|---|
| **Calendar** | **Did a meeting happen?** |
| **Email** | Did a submission happen, and what was the outcome? |
| **Platform exports** | What was submitted, and exactly when? |

Both interview-layer errors were "did a meeting happen" questions:

- **Dagster Labs** — a phone interview held 2026-03-30, recoverable from email only by reading a recruiter's phrase "the effort you have put into the interview process."
- **Orchestry** — a missed slot on 03-25 followed by a held one on 03-26, recoverable only by noticing that the counterparty's "we missed each other" email had no successor.

**Both would have been one row each in a calendar sweep.** Neither needed inference.

### The corrected method: calendar-first for the event layer

1. Sweep **all** calendar events across the full window in 90-day blocks, no keyword filter. This is already stop condition 2 and is half done.
2. For every event with an **external attendee**, work **backwards** to classify it: interview, community, vendor, personal, engagement.
3. Only then use email to supply the outcome and the submission that preceded it.
4. `interviewed` is derived from that event set. Never from a workbook.

### The limit, stated so nobody over-trusts it

**A personal Google Calendar does not record attendance.** It records that an event existed, its attendees, and their RSVP status. It does not prove anyone joined. Meet attendance logs live in Workspace admin audit, which does not exist for a personal account.

So calendar is a **near-complete roster of scheduled meetings**, not proof of held ones. Orchestry is the proof: two scheduled events, one held. The correct rule is **calendar enumerates candidates, email adjudicates which were held** — which is the reverse of how this project ran, and is why both errors happened.

Log 030 also found this calendar's deletion behaviour inconsistent, so absence of an event is weak evidence. That limit stands.

---

## 3. What would change if this were run again

Eight items, in order of how much damage each caused.

**1. Interview the subject FIRST, not at log 042.**
The highest-yield retrieval in the entire project was asking Keegan what happened. Log 042 resolved `discovery_source` on nine processes, produced an entity that appears in no artifact anywhere, overturned an exclusion, reclassified TrueBuilt, and independently confirmed Dagster. Running it at log 042 meant **41 logs of retrieval without knowing what the target set was.**
Structured debrief first turns the sweep from *discovery* into *verification* — and verification has a stop rule, while discovery does not.

**2. Assign instruments to questions before writing a single query.**
See section 2. Cost: two interview-layer errors and an unauditable primary outcome.

**3. Freeze the corpus before extracting anything.**
`CORPUS-MANIFEST.md` was created with a table and never populated. Forty-two logs of extraction have run against a moving corpus. **The parallel-coding design in `protocol.md` is currently unrunnable** — there is no frozen artifact set to give coder 1 and coder 2, so no agreement statistic can be computed. This is the single largest threat to the paper's central methodological claim, and it is procedural, not empirical.

**4. Give design principles enforcement, not just statement.**
Principle 1 says `interviewed` is derived, never stored. The figure 11 was then carried as a stored value through forty logs and turned out to be wrong. A principle without a mechanism is a preference. **Mechanism: no number enters any document without a `derived_from` tag naming the table and filter that produced it.** Anything untagged is quarantined.

**5. Retrieval logs must record sequences, not conclusions.**
Orchestry's error was pure summarization: every artifact was captured, and the reading stopped at the miss. **Rule: for any process with more than two artifacts, the log records the full ordered sequence with timestamps before it states an outcome.** Log 040 and 041 adopt this; logs 001 to 034 mostly did not.

**6. Maintain the stop-rule instrument.**
`QUERY-MANIFEST 2.md` says "last updated after Q7" while logs ran to 042. The manifest is what decides whether retrieval is exhaustive. **A drifting stop rule cannot support an exhaustiveness claim in Methods.**

**7. Pilot the codebook on 20 rows before freezing it.**
Five amendments landed in one day (A1–A4 plus proposed A5), all fortunately before coder 1. A pilot coding pass of 20 diverse rows would have surfaced `no_response` anchoring, the referral-channel gap, the community split and the application-spawns-opportunity shape at a cost of about an hour.

**8. Choose the matching instrument before running it, not after.**
The batched company-name Gmail search burned three query shapes and returned newsletter noise at the result ceiling, because the company set contains ordinary English words. Set comparison against the already-swept corpus was both cheaper and more correct. **Rule: when matching entities, first ask whether the answer already exists in a structured artifact.**

**What NOT to change.** Four decisions paid for themselves and should be kept verbatim: the register split (`application` vs `opportunity`) which kept the largest paid outcome out of the conversion rate; `date_precision` with a required anchor; evidence tiers with `evidence_class` strata; and writing down known integrity defects instead of quietly fixing them.

---

## 4. The master prompt

Standalone. Assumes no memory of this project. Give it the sources listed in the Inputs block.

---

You are acting as the methodologist and retrieval agent for a single-subject retrospective study. The subject audited his own job search and wants it written up to the standard of a journal paper: abstract, introduction, methods, results, discussion, conclusion, with figures. The goal is not a big number. **The goal is a defensible one, with every figure traceable to an artifact.**

**Your governing constraint: never assert what you have not evidenced.** If a fact comes from the subject's memory, tag it. If it comes from an artifact, cite the artifact id. If you inferred it, say so and say from what. A figure with a caveat is publishable; a figure asserted from feel is not.

### Inputs

- The subject's mailbox (read access), calendar, and any platform data exports: LinkedIn, and any job boards used.
- Any prior spreadsheets or audits the subject has already built. **Treat these as claims to be verified, not as data.** They predate the sweep and will contain figures carried forward from before the evidence existed.

### Phase 0 — Debrief the subject before retrieving anything

Do this first. It defines the target set and converts the whole retrieval from open-ended discovery into bounded verification.

Ask, one question at a time:
1. Every company you interviewed with, the counterparty's name, and how many rounds.
2. For each: where did the opportunity come from? A job board, a referral, a community, an inbound message? Name the community and the channel if there was one.
3. Every conversation that reached a real discussion but was not an application — inbound recruiters, founders, community contacts.
4. Every piece of paid or unpaid client work that ran during the window, with rough start and end.
5. Anything that started as one thing and became another — an application that became contract work, a referral that became an application.

Record every answer as `evidence_system = memory`. **This is the target set. Retrieval now verifies it and looks for what it missed.**

### Phase 1 — Pre-register, then freeze

Write a protocol before the first query, containing: the study window with timezone; the unit of analysis; primary and secondary outcomes; the completeness-estimation method with its assumptions and the direction of likely bias; explicit stop conditions; and a list of known integrity defects.

Write a codebook: field definitions and closed vocabularies for applications, events and exclusions. **Then pilot it on 20 diverse rows and revise.** Only then freeze. Every change after the first coder runs is a protocol deviation that must be disclosed.

Six design rules that are worth stealing verbatim:
1. **Store observations, compute rollups.** `interviewed` and `rounds` are derived from an events table, never stored. Enforce this: no figure enters any document without a tag naming the table and filter it came from.
2. **One row per application cycle, with cycle in the key.** Two applications to the same role a month apart are two rows.
3. **Origin is three independent fields**: where it was found, how it was submitted, where the evidence lives. Never one string.
4. **Every date carries a precision label and, when bounded, an anchor date.**
5. **Register is a field, not a separate sheet.** `application` versus `opportunity`. Only applications enter the census. This will feel wrong when the largest paid outcome lands in the opportunity register — that is the rule working.
6. **Closed vocabularies everywhere except a free-text notes field.**

### Phase 2 — Assign instruments to questions

Do this explicitly, in writing, before querying.

- **Calendar answers: did a meeting happen.** Sweep the entire window in 90-day blocks with **no keyword filter** — keyword search fails because interviews live in generic invite titles. For every event with an external attendee, work backwards and classify it.
- **Email answers: did a submission happen, and what was the outcome.** Query families: ATS domains; receipt phrases; rejection and closure language that omits the word "application"; sent mail with attachments; sent mail without; interview and scheduling language; and a repeat of the first family across spam and trash.
- **Platform exports answer: what was submitted, and exactly when.** These carry exact timestamps and are the cleanest date stratum you will get.

**Calendar enumerates candidate meetings; email adjudicates which were held.** Note the limit: a personal calendar records that an event existed and who was invited, not that anyone joined.

### Phase 3 — Retrieve, and maintain the stop rule

Keep a query manifest: every query, its window, its status, and whether it returned a further page token. **A query is done only when the API returns no next page.** Update it every session — this manifest is the only thing that can support an exhaustiveness claim.

Log every retrieval. **For any process with more than two artifacts, record the full ordered sequence with timestamps before stating any outcome.** Read every thread to its end. A missed meeting is frequently followed by a rebooking within the hour; a summary that stops at the miss will record a held interview as a failure.

The retriever emits artifacts, never rows. If retrieval output contains a count, a category, or a judgement, it is contaminated.

When matching entities across sources, **first ask whether the answer already exists in a structured artifact.** Full-text search on company names fails badly when company names are ordinary words.

### Phase 4 — Reconcile and measure

Deduplicate across sources by comparing against what has already been extracted, not by re-searching. Report the measured overlap. Distinguish **rows already represented in the census** from **rows that could have been observed by both sources** — only the second is a capture-recapture stratum.

Then estimate completeness. Do not assert it. Use a stratified two-source estimator restricted to the stratum where both sources could have seen the same event, state the independence assumption, report the interval, and name the direction of likely bias. **Report marginal yield per query alongside it** — a discovery curve that has not flattened is evidence against saturation, whatever the estimator says.

### Phase 5 — Write

Report every rate at two strata: employer-confirmed evidence only, and full census. Report every recall-dependent figure twice: all sources, and artifact-confirmed only. Publish the disagreement inventory and the pre-adjudication disagreement rate. State the unmet stop conditions in Methods rather than omitting them.

If a condition existed that bears on the rates — concurrent employment, client work, anything that changes how many applications a person sends — disclose it as a condition on every rate, and make no causal claim about its direction.

### Failure modes to watch for, all observed in practice

1. A figure inherited from a pre-sweep spreadsheet and never recomputed. **This will be your worst error.** It is invisible because the number looks settled.
2. A summary that stops before the end of a thread.
3. A stop-rule manifest that drifts out of date while work continues.
4. A corpus that keeps growing while extraction runs, which silently makes any inter-coder agreement statistic meaningless.
5. Full-text entity matching on names that are also common words.
6. Absence of evidence read as evidence of absence. Before claiming a thing is not there, name the query you ran and show it could have reached it.
