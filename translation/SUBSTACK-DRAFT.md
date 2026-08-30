# The Sabbatical repo, translated

Sections 3 through 6 of an adversarial translation pass. Paste-ready, in order.

Every claim below is traceable to a file in this repository, cited inline. Where the repository does not establish something, it is marked **UNVERIFIED**.

---

# 3. Reader leverage map

A technique is only worth writing about if someone can lift it. This section takes every part of the repository that scored 3 or higher on extractability and asks four questions: what is the technique underneath the code, does it survive being pulled out of this stack, what skill does it prove, and what does the extracted version look like.

The skills named here are deliberately narrow. Each one maps to a technique that is actually implemented in this repository. None is a compliment.

## 3.1 Define exhaustion as a condition a machine can check

**The technique.** Do not search until the results stop looking new. Assign every query a stable id, record its intent in plain language, and terminate it on a condition the source itself reports. In this repository that condition is the absence of a pagination token: "A query is `done` only when the API returns no `nextPageToken`" (see: `QUERY-MANIFEST.md`). Twenty-two queries, each with a status of done, blocked, or incomplete, with the blocker named inline.

The corollary matters more than the rule. When you search a source by the obvious keyword and get zero results, you cannot tell whether the thing is absent or merely called something else. The study searched its calendar for "interview" and got zero events, because interview loops lived inside invites titled "30 minute meeting" (see: `knowledge/protocol.md`). Sweeping the full window in 90-day blocks with no keyword at all returned 31 events (see: `artifacts/calendar/q8-lecturesfrom-primary.csv`).

**Extractable?** Yes, cleanly. Nothing about it is specific to Gmail. Any paginated source gives you an equivalent stop condition.

**What it proves you can do.** Define coverage as a testable claim rather than a feeling, and distinguish "not there" from "not searched". The repository has a phrase for this that is worth stealing whole: data can be **unharvested rather than empty** (see: `knowledge/protocol.md`). Its own prior audits searched only from 2025-08-25 forward, which made five months look like a quiet period when they were simply outside the search boundary.

**Template:** `templates/01-bounded-exhaustive-sweep.md`, reproduced in Section 5.

## 3.2 Turn an inbox into a schema without the model inventing rows

**The technique.** A generation prompt built around three devices that are rare in the wild: an asymmetric error statement, a named fallback for every field, and a mandatory reflective footer.

The error statement leads: "Accuracy beats coverage. An omitted row can be recovered later. A fabricated row poisons the census" (see: `prompts/extraction.md`). Most extraction prompts imply both errors cost the same. Saying which one you fear tells the model which way to lean.

The fallbacks are specific rather than general. `unknown` where the vocabulary includes it, `none_observed` for the applicant-tracking-system field, and never both (see: `codebook.md`). A model with no legal way to say "I could not tell" will invent something plausible.

The footer is one line and it does real work: "If you were tempted to fill a gap and did not, say what the gap was" (see: `prompts/extraction.md`). It worked here. The coder wrote "The Hog: no ATS receipt. Coded application from a titled GTM interview plus take-home. Medium confidence. Could have been opportunity" (see: `coding/cursor/notes__cursor.md`). Adjudication later reversed exactly that call. The model predicted its own error.

**Extractable?** Yes, though it currently opens by pointing at another file, so it cannot be used standalone as written. The extracted version inlines the schema slots.

**What it proves you can do.** Turn an unstructured inbox into a structured funnel, and design the guardrails that keep a language model from filling gaps with plausible fiction.

**Template:** `templates/02-artifact-to-schema-extraction.md`.

## 3.3 Split the funnel before you compute the rate

**The technique.** Two registers, decided by origination, only one of which is ever a denominator. Applications are roles the subject submitted himself. Opportunities are referrals, recruiter-initiated processes, and matching-platform contracts where no submission exists. Both stay in the dataset. Only the first is a denominator (see: `knowledge/00-core.md`).

The reason is stated plainly: those opportunities "produced real interviews and real money. They never enter the application census, because putting them there inflates the conversion rate with outcomes that did not come from applying."

**Extractable?** Yes, and it generalizes further than the repository claims. The repository says so itself: "a job search has two independent pipelines, and mixing them makes both unmeasurable" (see: `knowledge/00-core.md`). Substitute any funnel with both an outbound motion and an inbound motion.

**What it proves you can do.** Recognize denominator contamination and design a schema that prevents it structurally, rather than a convention that discourages it. Note which direction the contamination runs. Ten processes were adjudicated into the opportunity register in this freeze (see: `adjudication/ADJUDICATION.md`), and Mercor, a matching-platform contract path that converted to paid work, is one of them. The rows that would have inflated the rate are the ones with the good outcomes, which is exactly why nobody catches this.

**Template:** `templates/03-two-register-funnel-split.md`.

## 3.4 Measure whether your categories are real

**The technique.** Two independent classifiers on a frozen corpus and a frozen codebook, neither seeing the other's output, disagreements resolved in a named pass afterwards, with the pre-adjudication agreement rate published rather than the clean post-adjudication one (see: `knowledge/protocol.md`).

Four requirements, each with its own failure mode attached, which is what makes the list usable: freeze the codebook, freeze the corpus, stay blind, adjudicate after. The second one is the sharpest: "A coder who sees more artifacts is not a second rating, it is a different study."

**Extractable?** Yes. The design is stack-independent. The implementation has defects worth knowing about before copying, listed in the template.

**What it proves you can do.** Distinguish a pattern in your data from a habit of your classifier, and put a number on the difference. The repository states the principle better than most methods papers: "Until independent coders agree on lane assignment, that gap cannot be attributed to behavior rather than coding" (see: `knowledge/protocol.md`).

It also proves you can read your own statistics honestly. Two agreement figures are published here (see: `adjudication/PRE-ADJUDICATION.md`). Role-lane agreement is 0.9621 with a kappa of 0.9510, which is strong. The include-or-exclude decision has 0.9905 agreement and a kappa of 0.7452. That 24-point drop is the whole reason kappa exists: almost every record was an include, so two raters guessing "include" every time would agree nearly as often. The honest number is the lower one, and it rests on two disagreements.

**Template:** `templates/04-blind-double-coding.md`.

## 3.5 Design a dedup key that survives a re-run, and a matcher that refuses

**The technique.** A three-part key, `entity | subject | cycle`, and a three-tier match cascade that stops at the first tier producing exactly one candidate.

The cycle component is the part people omit. This repository documents what omitting it cost: the original key was `company|role`, and two genuine re-applications collapsed into their first attempts (see: `paper/DEFECTS.md`). The rule that governs it is precise. A repeat counts as a new cycle only after a terminal outcome on the previous one. FOSSA's first cycle carries a rejection dated 2026-05-20, and that rejection is what licenses the second cycle dated 2026-05-21 (see: `knowledge/03-codebook.md`). Three Pogo artifacts across two systems with no terminal outcome between them stayed one cycle (see: `coding/cursor/notes__cursor.md`).

The matcher runs exact-after-normalization, then an entity-level fallback for admitted unknowns, then ordered token-prefix equivalence after stripping location noise and expanding abbreviations. And then the line that earns the most credit in the whole codebase: if the third tier produces more than one candidate, it matches nothing (see: `adjudication/ingest_platform.py`). A wrong merge silently destroys a record. An unmerged duplicate is visible and fixable.

That credit needed one qualification when this audit was written, and the audit is the reason it no longer does. The refusal was implemented; the record of it was not. `match_status` carried three values, `net_new`, `overlap`, and one non-census, with no ambiguous state, so a refused record shipped as `net_new` and became indistinguishable from one that genuinely had no counterpart. A refusal nobody can find downstream is an unrecorded merge decision rather than a conservative one. That is now fixed: ambiguous rows carry `match_status = ambiguous` with their candidate parent ids and are held out of the census (see: `adjudication/ingest_platform.py`). No row in the current corpus hits that branch, so the published figures did not move. The point stands for anyone reusing the pattern, which is why the template specifies four statuses rather than three.

**Extractable?** Yes, with pruning. The noise-token list is hardcoded to one person's geography.

**What it proves you can do.** Reconcile overlapping sources without inflating the total, and know which direction to fail in when you cannot tell. The payoff is measurable: 40 raw tracker rows produced 5 net-new applications, and "a naive sum across four trackers would have reported roughly 315 instead of 247" (see: `knowledge/01-engagement.md`).

**Template:** `templates/05-conservative-record-linkage.md`.

## 3.6 Things worth naming that did not become templates

Smaller moves, each reusable, each currently invisible to a reader.

| Move | Where | Why it is good |
|---|---|---|
| A blocklist of your own numbers | `paper/RESULTS.md` | "What a skeptic should not be shown as a finding" lists eight numbers and framings with the reason each is disqualified, including two that would have flattered the author. |
| `what_would_promote_it` as a column | `coding/*/exclusions__*.csv` | Every rejected row records the evidence that would reverse the rejection. Turns an exclusion list into a work queue. |
| Recording what a decision rules out | `knowledge/01-engagement.md` | A decisions table with the column "What it rules out" rather than only what it does. |
| Separating "not reachable" from "deliberately excluded" | `knowledge/sources.md` | A gap and a choice are different provenance facts and are usually conflated. |
| A "how to re-pull" column | `knowledge/sources.md` | Contains literal navigation paths. Makes a source register operational rather than decorative. |
| Stating the bias direction of an analysis you refused to run | `paper/RESULTS.md` | If someone runs the wrong estimator anyway, the file already says which way it will be wrong. |

## 3.7 One honest gap in this map

**UNVERIFIED, confirm with the author.** The extraction prompt in `prompts/extraction.md` is excellent, and this repository does not contain evidence that it was ever run against the corpus. `coding/cursor/generate_cursor_coding.py` describes itself as "Independent coding by coder_id=cursor from the frozen artifact corpus", but the script opens no input file. It is 221 literal records reshaped into CSVs. `coding/bravo/` has no generator at all.

The judgements may well have been produced exactly as described, in a session whose transcript is not committed, and `coding/cursor/notes__cursor.md` reads precisely like the reflective footer the prompt demands. But the technique in 3.2 is credited to the prompt's design, not to a documented run of it. A reader should know which of those two they are being shown.

---

# 4. How this actually works

## The plain-language version

A GTM engineer spent fifteen months applying for jobs and then did something unusual: rather than reporting a number, he treated his own job search as a dataset and tried to work out how many applications he could actually prove.

The honest answer turned out to be smaller and stranger than the number he started with.

**The problem is that the evidence is scattered and every source lies a little.** Application receipts sit in email. Interview loops sit in a calendar under names like "30 minute meeting". Applied lists sit inside LinkedIn with relative timestamps like "2mo ago". Agent tools like Jobright keep their own trackers. Every one of these overlaps the others, so adding them up double-counts. The repository puts the stakes concretely: a naive sum across four trackers would have reported roughly 315 applications instead of 247 (see: `knowledge/01-engagement.md`).

**So the first move is to define what "I looked everywhere" means.** Twenty-two searches, each with an id, a date window, and a stop condition the email service itself reports: keep going until it stops offering another page (see: `QUERY-MANIFEST.md`). The ledger records which searches finished, which were blocked, and which are still open. It then states plainly that the stop rule was not met, because one mailbox could not be reached.

That discipline caught a real blind spot. Searching the calendar for the word "interview" returned zero events, because interviews were booked under generic invite titles. Sweeping the whole window in 90-day chunks with no keyword filter at all returned 31 (see: `artifacts/calendar/q8-lecturesfrom-primary.csv`).

**The second move is to freeze the evidence and then read it twice, independently.** The raw retrieval logs were locked as a fixed corpus. Two separate extractors converted them into the same three tables, without seeing each other's work (see: `knowledge/protocol.md`). Then the disagreements were counted before anyone resolved them.

There were fewer than expected. The two extractors agreed on category assignment 96 percent of the time. On the more basic question of whether a record counts at all, they disagreed on exactly two rows out of 211 (see: `adjudication/PRE-ADJUDICATION.md`).

**Those two rows are the most instructive thing in the repository.**

Take The Hog. There was an interview invitation on 2026-06-15, an interview on 2026-06-16, and a roughly four-hour take-home exercise on 2026-06-18 (see: `artifacts/gmail/retrieval-log-021.md`). What there was not, anywhere, was a receipt showing an application had been submitted. One extractor called it an application at medium confidence and flagged its own doubt. The other called it an opportunity. The resolution is one sentence and it is the whole method in miniature: "Interview plus take-home do not mint an application row" (see: `adjudication/ADJUDICATION.md`).

So the interview stays in the dataset, and the application does not. Which sounds pedantic until you notice what it protects. This job search had two pipelines: roles applied to, and roles that arrived through referrals, recruiters, and matching platforms. The second pipeline produced real interviews and real money, including three engagements that converted to paid work. If those outcomes are counted against applications, applying looks more effective than it is (see: `knowledge/00-core.md`).

**The third move is reconciling the platform exports against what email already proved.** Ninety-nine LinkedIn rows and 40 Jobright rows were matched against the existing census. Five turned out to be the same roles under different names: LinkedIn lists "Listen" where the email record says "Listen Labs", and "AE Tax or Risk" where the receipt says "Account Executive, Tax or Risk Products" (see: `adjudication/FREEZE-2.md`). Those are overlap, not new applications. When the matcher cannot tell whether two records are the same, it deliberately declines to merge them.

**The result is 221 applications with employer-side proof, plus 77 more visible only in platform logs, for 298 total. Thirteen produced interviews, a rate of 13/221** (see: `adjudication/ADJUDICATION.md`).

And the repository refuses to turn that into a completeness percentage. The standard method for estimating what you missed requires two sources that could each have seen the same record. Here they cannot: LinkedIn Easy Apply usually generates no email at all, so the two sources barely overlap by construction (see: `knowledge/protocol.md`). Rather than run the estimator anyway, the file names the method, explains why it fails, and states the direction the wrong answer would err in.

The most quotable line in the whole thing is about that refusal: "A completeness figure with a method and a caveat is publishable. A completeness figure asserted from feel is not."

## Component by component

**The frozen corpus.** *Problem:* two people reading different evidence will disagree for reasons that have nothing to do with judgement. *Mechanism:* the raw retrieval output is locked, dated, and enumerated, and every extractor receives that identical set (see: `CORPUS-MANIFEST.md`). *If you skip it:* your agreement statistic measures nothing, because the file states the failure exactly: "A coder holding a different set is running a different study."

**Retrieval.** *Problem:* you cannot tell an absent record from an unsearched one. *Mechanism:* numbered queries with plain-language intents, date windows, and a stop condition the source reports (see: `QUERY-MANIFEST.md`). *If you skip it:* you publish a time series with a hole in it and call the hole a quiet period.

**The extraction prompt.** *Problem:* a language model asked to structure messy evidence will fill gaps with plausible inventions. *Mechanism:* nine hard rules, a named fallback value for every field so the model always has a legal way to say "I could not tell", and a required log of every judgement call including the ones it was tempted to make and did not (see: `prompts/extraction.md`). *If you skip it:* you get a clean-looking dataset where observations and inferences are indistinguishable.

**Double coding.** *Problem:* a single classifier is consistent with itself by construction, so its consistency proves nothing. *Mechanism:* two extractors, blind to each other, with the raw disagreement rate published before anyone resolves anything (see: `knowledge/protocol.md`). *If you skip it:* you cannot tell whether a pattern is in your data or in your classifier.

**Adjudication.** *Problem:* disagreements resolved by preference are unreviewable. *Mechanism:* every decision written as a rule that would apply to the next case, with the reasoning attached (see: `adjudication/ADJUDICATION.md`). *If you skip it:* your resolutions cannot be audited and your next dataset repeats the argument from scratch.

**Platform ingest.** *Problem:* four trackers holding overlapping records of the same activity. *Mechanism:* normalize, apply a hand-maintained alias table, then compare titles by ordered token prefix after stripping location noise, and refuse to merge when more than one candidate matches (see: `adjudication/ingest_platform.py`). *If you skip it:* 315 instead of 247.

**Redaction.** *Problem:* publishing an evidence trail means publishing mailbox identifiers. *Mechanism:* every provider id and third-party address is replaced by a stable hashed pointer, so independent coders can still join on evidence without the raw identifiers being published, while the study's own mailboxes stay readable so the search scope remains auditable (see: `scripts/redact_corpus.py`, `CORPUS-MANIFEST.md`). *If you skip it:* you either publish other people's addresses or you publish a corpus nobody can verify.

## Glossary

Nine terms this repository uses as settled and never defines.

**Census.** The reconciled set of records you can actually prove, as opposed to the set you remember or the set some tracker claims.

**Freeze.** A dated, enumerated, locked input set. Not "finished". "No longer permitted to change."

**Register.** Which of two datasets a record belongs to. Here: applications you submitted, or opportunities that arrived. Both are kept; only one is ever a denominator.

**Evidence tier.** How strong the proof is. A is an employer or system message using explicit application language, B is corroborated across two artifacts, C is a self-logged tracker row with nothing from the employer side.

**Evidence class.** Who produced the artifact. Employer-side, or platform log. Different question from tier, used for a different purpose: tier gates confidence, class defines the slices you compare.

**Coding.** The research sense, not the programming sense. Reading unstructured material and assigning each piece to a category from a fixed list.

**Adjudication.** A single pass, after all coders have finished, that resolves disagreements with a written rule rather than a preference.

**Cohen's kappa.** Agreement between two raters after subtracting the agreement you would expect from chance alone. It matters most when one category dominates, because plain percent agreement flatters you there.

**Capture recapture.** Estimating a population you cannot see by measuring the overlap between two independent attempts to see it. It requires that both attempts could have seen the same record, which is precisely why this study declined to use it.

---

# 5. Reusable prompt templates

Five operations, rewritten for someone who has never seen this repository. Adapt the variables and nothing else. Each has a fully annotated version, with worked examples and failure modes, in `translation/templates/`.

## 5.1 Bounded exhaustive sweep

*Proves you can define coverage as a testable claim rather than a feeling.*

> Search `{{SOURCE}}` for `{{SIGNAL_SET}}`, bounded by `{{WINDOW}}` and split into `{{SUB_WINDOWS}}`, terminated by `{{EXHAUSTION_CONDITION}}`, and output `{{QUERY_LEDGER}}`.

```
You are running an exhaustive retrieval sweep. You are not filtering, judging,
or counting. Your only job is to prove coverage.

SOURCE: {{SOURCE}}
WINDOW: {{START_DATE}} to {{END_DATE}}, {{TIMEZONE}}, inclusive

Run each query below. For every query, record: a stable query id; the query
intent in plain language, not just the raw string; the window it covered; the
termination state (done, incomplete, or blocked); the yield; and which output
log holds the results.

A query is `done` ONLY when {{EXHAUSTION_CONDITION}}.
It is `incomplete` when the source still offers more and you stopped.
It is `blocked` when you could not run it at all. Name the blocker inline.

QUERIES:
1. Known-sender sweep. Search for {{PHRASE_SET}} from {{KNOWN_DOMAIN_LIST}}.
2. Discovered-sender sweep. Re-run query 1 with any sender that appeared in
   query 1 and was not in {{KNOWN_DOMAIN_LIST}}. Repeat until no new
   senders appear.
3. Negative-language sweep. Search for {{OUTCOME_PHRASE_SET}} with no sender
   filter, minus {{NOISE_DOMAIN_LIST}}. This catches records whose sender
   you never learned.
4. Own-output sweep. Search {{OUTBOUND_SOURCE}} for {{OUTBOUND_PHRASE_SET}}.
   What you sent is evidence too.
5. Unfiltered block sweep. For {{SECONDARY_SOURCE}}, sweep the full window in
   {{BLOCK_SIZE}} blocks with NO keyword filter at all.

RULES:
- If a single query paginates past {{PAGE_LIMIT}}, split it into sub-windows
  with a one-unit overlap at each boundary. Overlap costs duplicates. A gap
  costs records.
- Never filter {{SECONDARY_SOURCE}} by the obvious keyword without also
  running query 5. If the obvious keyword returns zero, you cannot tell
  whether the thing is absent or merely named differently.
- Record zero-result queries. A query that returned nothing is coverage.
- Do not deduplicate, classify, or count during retrieval.

STOP RULE: retrieval is exhaustive when every query returns
{{EXHAUSTION_CONDITION}} on every source, AND a final pass over newly
discovered senders returns nothing new. If that rule is not met, say so and
list what is still open. Do not describe a partial sweep as complete.

OUTPUT: a query ledger table, plus one raw log per query.
```

## 5.2 Artifact to schema extraction

*Proves you can turn an unstructured inbox into a structured funnel without inventing rows.*

> Classify `{{RAW_ARTIFACTS}}` into `{{SCHEMA}}` using `{{CONTROLLED_VOCABULARY}}`, bounded by `{{NEVER_INFER_RULES}}`, and output `{{ROWS}}` plus `{{JUDGEMENT_LOG}}`.

```
You are extracting structured records from {{ARTIFACT_TYPE}} into a research
dataset. Accuracy beats coverage. An omitted row can be recovered later. A
fabricated row poisons the dataset.

YOUR OUTPUT IS ROWS, NOT PROSE. Emit {{TABLE_1}}, {{TABLE_2}}, and
{{TABLE_3}} rows using exactly the field names and vocabularies below, with
{{SOURCE_ID_FIELD}} first on every row. Do not invent fields or values. If a
value does not fit, emit the named fallback for that field and describe the
unmatched value in `notes`.

SCHEMA:
  {{TABLE_1}}: one row per {{PRIMARY_UNIT}}.  Fields: {{FIELD_LIST_1}}
  {{TABLE_2}}: one row per timestamped interaction. Fields: {{FIELD_LIST_2}}
  {{TABLE_3}}: one row per candidate you considered and REJECTED.
               Fields: {{FIELD_LIST_3}}, including `what_would_promote_it`
VOCABULARIES: {{CONTROLLED_VOCABULARY}}
FALLBACKS:    {{PER_FIELD_FALLBACK_MAP}}

HARD RULES:
1. Never infer {{ENTITY}} or {{ATTRIBUTE}}. If the artifact omits it, use the
   fallback. A missing value is data.
2. Never emit a {{PRIMARY_UNIT}} row from a downstream artifact alone.
   {{DOWNSTREAM_EXAMPLE}} proves a process existed, not that
   {{PRIMARY_EVENT}} happened. Emit the interaction, flag the missing parent,
   and add a rejection row until a {{PRIMARY_EVENT}} artifact appears.
3. Never merge two artifacts into one row silently. One artifact produces one
   interaction. Merging happens at the {{PRIMARY_UNIT}} level and must be
   stated in `notes` with both evidence IDs.
4. Every date gets a precision label. A relative stamp requires a capture
   date. Never upgrade a relative date to an exact one.
5. A repeat {{PRIMARY_EVENT}} for the same {{ENTITY}} after a terminal
   outcome is a new cycle. Increment the cycle, mint a new id, do not
   overwrite the first.
6. Assign {{STRATUM_FIELD}} by WHO produced the artifact, not by how good it
   is. {{STRATUM_A_RULE}}. {{STRATUM_B_RULE}}.
7. Assign {{REGISTER_FIELD}} = {{SECONDARY_REGISTER}} when the process began
   without {{PRIMARY_EVENT}}. These rows stay in the dataset and out of the
   headline count.
8. Anything sourced from recall rather than an artifact gets
   `evidence_system = memory`. Never disguise recall as evidence.
9. When two artifacts conflict, emit the better-evidenced value and record
   the conflict in `notes`. Do not average. Do not pick silently.

BEFORE THE TABLES, output a three-line header: artifacts processed; rows
emitted per table; conflicts and unresolved identities as a numbered list or
the word "none".

AFTER THE TABLES, list every judgement call you made, one line each. If you
made none, say so. If you were tempted to fill a gap and did not, say what
the gap was.

Do not optimize toward a total. Fewer rows because the evidence was thinner
is the job done correctly.
```

## 5.3 Two-register funnel split

*Proves you can spot denominator contamination and design it out structurally.*

> Split `{{ALL_RECORDS}}` into `{{PRIMARY_REGISTER}}` and `{{SECONDARY_REGISTER}}` using `{{ORIGINATION_TEST}}`, bounded by `{{HARD_EVIDENCE_REQUIREMENT}}`, and report `{{RATE}}` with BOTH its denominator and its numerator restricted to `{{PRIMARY_REGISTER}}`.

```
You are separating {{ALL_RECORDS}} into two registers before any rate is
computed. Both registers stay in the dataset. Only one is a denominator.

PRIMARY REGISTER, {{PRIMARY_REGISTER}}: records where {{ORIGINATION_ACTOR}}
  initiated the process by {{PRIMARY_EVENT}}. The ONLY denominator for
  {{RATE}}.

SECONDARY REGISTER, {{SECONDARY_REGISTER}}: records where the process began
  through {{INBOUND_PATHWAY_LIST}} and {{PRIMARY_EVENT}} never happened.
  These produced real outcomes. They are tracked, reported, and never mixed
  into {{RATE}}.

THE ORIGINATION TEST, applied to every record:
  Is there an artifact showing {{ORIGINATION_ACTOR}} performed
  {{PRIMARY_EVENT}}?
    YES -> {{PRIMARY_REGISTER}}
    NO  -> {{SECONDARY_REGISTER}}
  A downstream artifact is NOT an origination artifact. {{DOWNSTREAM_LIST}}
  prove a process existed. They do not prove {{PRIMARY_EVENT}} happened.

WHEN IN DOUBT: assign {{SECONDARY_REGISTER}}. Under-counting the primary
register makes {{RATE}} conservative. Over-counting makes it wrong in the
flattering direction, which is the direction nobody catches.

REPORTING:
- The numerator MUST be intersected with {{PRIMARY_REGISTER}} ids before the
  rate is computed:
      numerator = {ids with a qualifying outcome} INTERSECT
                  {ids in {{PRIMARY_REGISTER}}}
  Moving a doubtful record to {{SECONDARY_REGISTER}} removes it from the
  denominator. Its outcomes stay visible in the interaction table, so a
  numerator counted straight off that table still includes them and the rate
  goes UP. Without this intersection, "when in doubt, exclude" is not
  conservative. It is the opposite.
- Report {{RATE}} as an unreduced fraction against {{PRIMARY_REGISTER}} only.
- Report {{SECONDARY_REGISTER}} as a separate parallel track with its own
  outcomes.
- Never publish a combined rate. If asked for one, give both fractions and
  let the reader do the arithmetic in the open.
```

## 5.4 Blind double-coding with named adjudication

*Proves you can tell a real pattern from an artifact of your classifier, with a number.*

> Have `{{N}}` independent raters classify `{{FROZEN_CORPUS}}` using `{{FROZEN_CODEBOOK}}`, bounded by `{{BLINDNESS_RULE}}`, and output `{{AGREEMENT_STATISTIC}}` plus `{{NAMED_ADJUDICATION_DECISIONS}}`.

```
DESIGN: {{N}} independent raters classify the same records using the same
codebook, without seeing each other's output.

FOUR REQUIREMENTS, IN ORDER. Each has its own failure mode.
1. FREEZE THE CODEBOOK FIRST. No vocabulary changes after rater 1 begins.
   Add a category mid-run and earlier rows were coded under a different
   instrument, which makes the agreement statistic meaningless.
2. FREEZE THE CORPUS. All raters receive an identical, enumerated, dated
   input set. A rater who sees more records is not a second rating. It is a
   different study.
3. BLIND. No rater sees another's rows before all runs finish. This includes
   you. Do not peek and then run the second rater.
4. ADJUDICATE AFTER, NOT DURING. Resolve disagreements in one named pass,
   AFTER the raw agreement rate is computed and recorded. Publish the
   pre-adjudication rate, not just the clean post-adjudication result.

REPORT:
- Percent agreement AND Cohen's kappa on {{PRIMARY_CATEGORICAL_FIELD}}
- Percent agreement on the binary include or exclude decision
- A disagreement inventory: every differing row, the field, both values
- Every adjudication decision by name, with the rule applied

STATE THIS CAVEAT EXPLICITLY: kappa computed on the intersection measures
agreement CONDITIONAL on both raters already agreeing a record exists.
Records only one rater produced are excluded by construction. Report those
counts separately and prominently. They are usually the disagreements that
matter most.

READING THE RESULT: when one category dominates, percent agreement is close
to meaningless and kappa is the number to publish. Publish both so the reader
can see the gap. A large gap means your agreement was mostly the base rate.

ADJUDICATION RULES:
- Every decision gets a written reason, not a preference.
- Reasons must be rules that would apply to the next case.
- When one rater flagged its own low confidence, weight that.
- Record the decision even when both raters were wrong.
```

## 5.5 Conservative record linkage

*Proves you can reconcile overlapping sources without inflating the total, and know which way to fail.*

> Match `{{SOURCE_A_RECORDS}}` against `{{SOURCE_B_RECORDS}}` using `{{NORMALIZATION}}` plus `{{ALIAS_TABLE}}` plus `{{EQUIVALENCE_RULE}}`, bounded by `{{REFUSE_ON_AMBIGUITY}}`, and output `{{MATCH_STATUS}}` per record, one of overlap, net_new, ambiguous with its candidate parent ids, or {{NON_CENSUS}}.

```
KEY = {{NORMALIZED_ENTITY}} | {{NORMALIZED_SUBJECT}} | {{CYCLE}}

Three required properties:
  DETERMINISTIC. Same inputs always produce the same key. No timestamps, no
    random ids, no row numbers, no insertion order.
  IDEMPOTENT. Re-running produces the same keys and the same merges. You can
    re-run without accumulating rows.
  CYCLE-AWARE. A new {{PRIMARY_EVENT}} for the same entity and subject, AFTER
    a terminal outcome on the previous cycle, increments the cycle and counts
    again. Without a terminal outcome it is the same cycle, no matter how
    many artifacts arrived.

MATCH each {{SOURCE_A}} record against {{SOURCE_B}} in three ordered tiers.
Stop at the first tier producing exactly one candidate.

TIER 1, EXACT AFTER NORMALIZATION. Lowercase, strip non-alphanumerics, then
  apply {{ALIAS_TABLE}}, a hand-maintained map of known equivalences.
  {{ALIAS_TABLE}} handles what no rule can: acquisitions, rebrands, legal
  entity suffixes, and typos in the source export.

TIER 2, ENTITY-LEVEL FALLBACK. If the subject on the {{SOURCE_B}} side is
  literally "{{UNSPECIFIED}}", match on entity alone. Use this ONLY where the
  schema records an admitted unknown, never as a general loosening.

TIERS 1 AND 2 CAN ALSO RETURN MORE THAN ONE, AND IT MEANS SOMETHING ELSE.
  These two are lookups, so it is easy to assume they yield at most one row.
  They do not, whenever the match key omits a dimension the identity key
  includes.

  A multi-hit here is NOT the tier 3 case and is not resolved the same way.
  The record matched, so it is an overlap either way and the count does not
  move. What has quietly become a choice is WHICH parent it belongs to.

  So here, and only here: keep the record and keep it counted, but do NOT
  name one of the candidates as the parent. Give it a status that says the
  parent is unresolved, leave the parent field empty, and record every
  candidate. A populated parent field asserts a resolution, and a reader
  joining on that field would never see that it was a coin flip. Fields that
  agree across all candidates stay populated, because those are not in doubt.

  At tier 3 the open question is whether it is a match at all, which the
  count does depend on, so the answer there is to refuse. See THE RULE THAT
  MATTERS MOST below.

TIER 3, TOKEN-PREFIX EQUIVALENCE. Tokenize both subjects. Drop
  {{NOISE_TOKENS}}: location words, posting-site boilerplate, workplace-type
  words. Expand {{ABBREVIATIONS}}. Delete parenthetical tails. Two subjects
  are equivalent when one token sequence is an exact ordered prefix of the
  other.

THE RULE THAT MATTERS MOST: if tier 3 produces more than one candidate, MATCH
  NOTHING. A wrong merge silently destroys a record. An unmerged duplicate is
  visible and fixable later, but ONLY if you can still see it.

  So do not emit an ambiguous record as plain net_new. Give it its own status,
  `ambiguous`, carrying the candidate parent ids it could not choose between.
  A refusal you cannot find later is not conservative. It is an unrecorded
  merge decision.

  Never merge on a similarity score. If you cannot state the rule that made
  two records the same, you cannot defend the count.

OUTPUT, per record, one of FOUR statuses: overlap with a named parent id;
net_new; ambiguous with its candidate parent ids; or {{NON_CENSUS}}. Never a
bare merged total with no provenance.

REPORT the ambiguous count alongside the total. A census of {{N}} with {{K}}
unresolved is a different claim from a census of {{N}}.
```

---

# 6. What to take from this

Five capabilities are worth recognizing in yourself here, each mapping to a technique in Section 3.

**Define coverage as a testable condition** (3.1). Not "I checked everywhere" but a stop rule the source reports back to you, and a ledger of what stays open when the rule is unmet. Its sharper half: an obvious query returning zero is a hypothesis about your query, not a finding about the world.

**Build extraction guardrails** (3.2). Name the error you fear, give the model a legal way to say "I could not tell", and make it log the gaps it was tempted to fill. The proof: a coder here flagged its own least confident call, and adjudication reversed exactly that one.

**Protect a denominator** (3.3). Most funnel arguments are numerator arguments. Contamination is rarely caught early, because the contaminating rows usually have the good outcomes.

**Measure your own classifier** (3.4). Two blind passes and a kappa is the difference between "our data shows a 20 point gap" and "we can prove that gap is not an artifact of how we labeled it."

**Design a key that survives a re-run** (3.5). Deterministic, idempotent, cycle-aware, paired with a matcher that refuses when it cannot tell. Forty raw tracker rows resolving to 5 net-new is what that looks like when it pays.

## Fork it, and break it

These templates are visibly incomplete, in ways the repository records.

The sweep hardcodes twelve applicant-tracking domains. Swap them. The coder here wanted vocabulary values that did not exist and recorded them rather than inventing them: AppliTrack and Frontline as tracking systems, and an interaction type for a marketplace contract activation, where it used "offer" because nothing fit (see: `coding/cursor/notes__cursor.md`). Two named holes in a published taxonomy. Fill them.

The record linkage strips `atlanta`, `ga`, `austin`, and `tx` as noise, because those are one person's cities. It also strips `products`, which will quietly mangle "GTM Emerging Products". Prune it before you trust it.

The most useful contribution is what broke. Three rows here carry a city name in the workplace-type column. They survived two coders, an adjudication pass, and two published CSVs. Exactly the defect a second reader catches and a solo author never does.

## Why publish the method rather than the result

The result is 221 applications and a 13/221 interview rate. Neither number is interesting alone.

What is interesting is what it publishes that a case study normally hides: a list of numbers the author refuses to show a skeptic, two of which would have flattered him. A stop-conditions table with four items marked Partial and two Unmet. A defect register entry that reads "Still undocumented. Workbooks absent."

Outcomes are not transferable. A dedup key is. A stop rule is. A prompt that makes a model tell you what it was tempted to invent is. Take these, change the domains, add the categories that are missing, run them against data nothing like a job search, and report what fell over.
