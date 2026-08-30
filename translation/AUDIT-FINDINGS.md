# Audit findings

Internal QA record. Sections 1 and 2 of the adversarial translation pass. Not for publication.

The reader this audit assumes: a smart GTM or marketing professional who understands funnels, denominators, and outcomes, and who has never written a line of code. A meaningful subset of that audience is trying to break into GTM engineering and is reading this repository as evidence of how a practitioner thinks.

## Scoring scale

**1 to 5, where 5 is worst.**

| Code | Criterion | What a 5 means |
|---|---|---|
| JAR | Jargon density | A non-engineer cannot read a paragraph without leaving to look something up |
| SO | The "so what" test | Describes implementation and never says why a reader should care |
| ASM | Hidden assumptions | Assumes the reader already knows the tool, API, or pattern being referenced |
| REP | Reproducibility gap | A reader without this exact environment would fail, and fail silently |
| OVR | Overclaiming | Language implies more automation, certainty, or intelligence than the code delivers |
| LEV | Leverage gap | A genuinely reusable technique is buried where a reader cannot see or lift it |

LEV is scored independently of the other five on purpose. A file can be well written and still score a 5 on LEV, because clarity and extractability are different properties. A 5 on LEV is a compliment to the technique and a criticism of its packaging.

## Verification note

Every quantitative claim below was recomputed from the CSVs. The published headline figures all check out: census 221, full census 298, interviewed 14, rate 14/221 = 0.0633, exact-date 195 and non-exact 26, and the exact-date monthly series in `ADJUDICATION.md:44`. The findings that follow are about how the work is described and packaged, not about arithmetic errors in the result.

---

# Section 1. File-by-file findings

## Root

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `README.md` | 22-line front door that names the study window, lists five directories, and fences off the headline numbers as unpublishable | 3 | 2 | 4 | 4 | 1 | 2 | "Gmail and Calendar connectors must be the accounts named in `QUERY-MANIFEST.md`. Exhaustion means no `nextPageToken`." (line 22). Two sentences that assume the reader knows what a connector is, what pagination is, and that "exhaustion" is a formal stop rule rather than a mood. |
| `codebook.md` | Coder-facing data dictionary: six design principles, three table schemas, evidence tiers, eight counting rules, ten controlled vocabularies, five worked examples | 4 | 3 | 4 | 2 | 1 | 5 | "**Store observations, compute rollups.** `interviewed` and `rounds` are never fields. They are derived from the events table." (line 9). The best idea in the file is gated behind "rollup", a word never defined here or anywhere in the repository. **Separate defect:** line 53 reads "This is what makes PhrasIQ legible." PhrasIQ is a real in-census company with a three-round interview chain (`knowledge/03-codebook.md:126`). Every other real entity was genericized when this blinded copy was derived from the internal one. This one survived, so a blinded coder learns a fact about the corpus from the codebook. |
| `QUERY-MANIFEST.md` | 22-row ledger of every retrieval query, with per-query page counts, yields, log mapping, and a done/blocked/incomplete status, followed by a stop rule the file then declares unmet | 4 | 3 | 5 | 4 | 1 | 5 | "A query is `done` only when the API returns no `nextPageToken`." (line 3). This is the single most portable idea in the repository, a machine-checkable definition of "I have looked everywhere", and it is delivered as a bare API token with no gloss. |
| `CORPUS-MANIFEST.md` | Declares which artifacts every coder receives, the redaction scheme, and the two-freeze structure | 4 | 2 | 4 | 3 | 1 | 4 | "Frozen 2026-08-29 ET for independent coding. Every coder receives this set. A coder holding a different set is running a different study." (line 3). Excellent reasoning. "Frozen" is used as a noun, a verb, and an ordinal across this repository roughly 25 times and is never defined. |

## paper/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `paper/RESULTS.md` | Coverage accounting, a refusal to publish completeness, agreement statistics, the 221-row census, the Freeze 2 addendum to 298, interview derivation, a monthly series, and a blocklist of numbers a skeptic must not be shown | 5 | 2 | 5 | 3 | 2 | 4 | "The intended estimator is stratified two-source capture recapture on the overlap where LinkedIn and external ATS mail could both have seen the same application." (line 24). Six pieces of undefined vocabulary in one sentence. A reader who does not already know what capture recapture is cannot tell whether this is a strong claim or a refusal to make one. It is a refusal, and that is the interesting part. |
| `paper/DEFECTS.md` | Four-item integrity register, each defect either closed with a named artifact or left explicitly open | 5 | 2 | 4 | 2 | 1 | 3 | "A key that omitted cycle would collide those pairs." (line 31). "Key", "omitted cycle", and "collide" are all load-bearing and all undefined. The underlying point, that two genuine re-applications to the same company and role were being silently merged into one, is immediately legible to any GTM reader once translated. |
| `paper/METHODS.md` | Compressed methods: window, unit of analysis, two-register rule, harvest-then-code separation, date precision, completeness estimator, limitations | 5 | 3 | 5 | 3 | 2 | 3 | "Naive Lincoln Petersen on Easy Apply versus ATS mail is invalid because those sources are near-disjoint by construction." (line 15). A named statistical method, a platform feature, and a technical phrase, none defined, in one sentence that is actually making a careful and correct point. |

## prompts/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `prompts/extraction.md` | The literal prompt handed to each coder: role frame, output-shape constraint, nine hard rules, a mandatory pre-table header, and a mandatory judgement-call log | 3 | 2 | 3 | 2 | 1 | 5 | "Emit `applications`, `events`, and `exclusions` rows as tables using the exact field names and controlled vocabularies in the codebook, including `coder_id` as the first field of every row." (line 9). The file is the most directly liftable artifact in the repository and it opens by pointing at another file, so it cannot be used standalone. Its best line, "If you were tempted to fill a gap and did not, say what the gap was" (line 28), is a general-purpose hallucination-surfacing device and is buried on the last line. |

## knowledge/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `knowledge/00-core.md` | Durable persona and standard: who the subject is, voice rules, publication standard, nine counting rules, evidence tiers, the two-register rule, a glossary, a quality bar | 4 | 2 | 3 | 2 | 2 | 4 | "Reject: consultant register, LinkedIn-inspirational register, hedging that hides a number." (line 27). "Register" here means tone. Thirty-five lines later at line 62 "register" means which of two datasets a row belongs to. Same file, same word, incompatible meanings, no signal to the reader that a switch occurred. |
| `knowledge/protocol.md` | The pre-registration: window, unit, outcomes, four requirements for blind parallel coding, reliability statistics, stratified capture-recapture, seven stop conditions, three known defects | 5 | 2 | 5 | 3 | 3 | 5 | "The current data already shows a 20 point gap in explicit GTM engineering share between the `employer_artifact` stratum (50.9 percent) and the `platform_log` stratum (30.2 percent)." (line 48). See Section 2, finding G3: the `platform_log` stratum is empty in the adjudicated census, and it is empty for a mechanical reason, so this gap cannot currently be recomputed from the committed data at all. The file's own next sentence is the right instinct and does not go far enough. |
| `knowledge/01-engagement.md` | Project brief: prior workbooks, the build from 163 to 247, source reconciliation, decisions and what they rule out, six known data problems, approaches already tried | 4 | 2 | 4 | 3 | 2 | 4 | "**Tier C dominates the increment.** 78 of the 84 net-new rows are LinkedIn applied-list rows with no employer-side artifact." (line 82). This is the most important sentence in the repository for a reader deciding how much to trust the number, and it requires knowing the tier ladder to parse at all. |
| `knowledge/02-current.md` | Explicitly disposable state file: headline numbers, role lanes, two conflicting monthly series, the opportunity register, open threads, paper status | 4 | 3 | 4 | 3 | 2 | 3 | "Both are in play and they disagree. The paper must show one and explain the other." (line 44). Correct and admirable. A reader has no way to know which of the two curves became the published one without cross-reading three other files. |
| `knowledge/instructions.md` | Operating instructions for the assistant: Role, How to behave, Always, Never, Output, and a map of the knowledge files | 3 | 2 | 3 | 2 | 1 | 4 | "Distinguish "measured", "estimated", and "unknown" in every sentence that carries a quantity." (line 12). A genuinely reusable epistemic discipline, stated once, in a file no reader of the paper will ever open. |
| `knowledge/sources.md` | Six-row source register mapping `[S1]` to `[S6]`, with a "how to re-pull" column, plus explicit "Not reachable" and "Deliberately excluded" sections | 3 | 2 | 3 | 2 | 1 | 4 | "No connector was queried in this run. Gmail, Calendar, Drive, Notion, and Todoist are connected but were not named as sources, so nothing was pulled from them." (line 25). The distinction between "we could not get it" and "we chose not to get it" is a real provenance idea, and it is delivered in tooling vocabulary. |
| `knowledge/03-codebook.md` | Internal twin of `codebook.md`: same schema, but argued from the real ledger's actual defects and using real corpus entities in its worked examples | 4 | 3 | 4 | 2 | 1 | 4 | "**Origin is three fields, not one.** Where you found it, how you submitted it, and where the evidence lives are independent. The current ledger collapses them into strings like "Gmail Ashby", which makes it impossible to ask whether Wellfound outperformed Easy Apply." (line 18). The clearest statement of business value anywhere in the repository, sitting in an internal file that no published artifact points a reader to. |

## artifacts/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `artifacts/gmail/retrieval-log-001.md` through `-029.md` (29 files, grouped) | Raw retrieval output: query string, account, page and token state, thread count, then a table of date, sender, subject, and hashed thread pointer, then retriever notes | 3 | 4 | 4 | 4 | 2 | 5 | Log 028: "Full thread ID lists for pages 1 and 2 are in the run transcript files under the agent tools directory for this session. They are SaaS marketing and are listed here by sender mix rather than 100 individual marketing subjects, because the query was exhausted and no employment ATS receipt appeared." The corpus is declared frozen and identical for every coder (`CORPUS-MANIFEST.md:3`), and this log points at files that are not in the repository. **Deviations:** logs 014 to 021 use bespoke table headers; 023, 024, and 026 have zero rows; 028 does not enumerate pages 1 and 2; 029 is not a retrieval log at all but a connectivity note. |
| `artifacts/STOP-CONDITIONS.md` | Seven stop conditions as a status table with an explicit waiver column | 4 | 2 | 4 | 3 | 1 | 3 | "Waivers are explicit. They are not silent omissions." (header). Scored low on overclaiming because this is the opposite of overclaiming. The jargon score is for "stop condition" and "waiver" arriving undefined in a file whose whole job is to be the honest one. |
| `artifacts/platform/PROVENANCE.md` | Freeze 2 file provenance: row counts, date-stamp types, and a "What this freeze is not" section | 3 | 3 | 3 | 3 | 1 | 2 | "Relative stamps are not upgraded to exact calendar dates." A one-line rule doing a lot of quiet work, with no statement of what would go wrong if you did upgrade them. |
| `artifacts/platform/KEEGAN-EXPORTS-ABSENT.md` | Negative-result document: what was searched for, where, and not found | 3 | 3 | 3 | 3 | 1 | 2 | Filename in shouting caps is the loudest signal in the repository and names a person rather than the finding. The document itself is a good idea, recording absence as a citable artifact. |
| `artifacts/platform/linkedin_applied_jobs_pages_1_to_10.csv` | 99 rows scraped from the LinkedIn applied list, with relative date stamps and no channel label | 2 | 4 | 3 | 3 | 1 | 2 | Header row: `tracker_page,job_title,company,location,workplace_type,applied_date_relative,posting_or_availability,visible_activity`. The absence of any Easy Apply versus external ATS column is the single fact that blocks the completeness estimate for the whole paper, and nothing in the file says so. |
| `artifacts/platform/jobright_applications_log.csv` | 40 rows from the Jobright tracker with exact ISO dates and an application-method column | 2 | 4 | 3 | 3 | 1 | 2 | `Application Method` takes four values, of which `Applied by Agent` covers 31 of 40 rows. That an agent submitted most of these is a substantive fact about the funnel and appears nowhere in the paper. |
| `artifacts/calendar/q8-lecturesfrom-primary.csv` | 31 calendar events swept in five 90-day blocks with no keyword filter, plus one sentinel row | 3 | 4 | 4 | 3 | 1 | 3 | The empty block is encoded as a data row with the literal string `no events in block` shifted into the `end` column. A structurally invalid row inside the frozen corpus, which any coder or script reading this file must special-case or silently mis-parse. |
| `artifacts/calendar/q8-transferred-empty.md` | Records a calendar that was swept and found empty, and one that could not be reached at all | 3 | 3 | 3 | 2 | 1 | 2 | "keeganmoody33@gmail.com primary calendar is not in `list_calendars`. Interview loops documented in the 247-row Interviews sheet (Beautiful.ai, Pearl, Great Question, Hologram, Fullsteam, and others) are expected to live there." Names five companies whose interviews are known to be missing from the corpus. This is the most consequential gap in the study and it lives in a 21-line file nothing links to. |

## coding/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `coding/README-coder.md` | The coder brief: five rules of the exercise and the output filename template | 3 | 2 | 3 | 3 | 1 | 4 | "**Do not optimize toward a total.** You are not trying to reach a number. A coder who produces fewer rows because the evidence was thinner is doing the job correctly." Genuinely excellent instruction design, aimed at an audience of two language models, and never surfaced to any human reader. |
| `coding/cursor/generate_cursor_coding.py` | 691 lines. Reshapes 221 literal application tuples, 10 opportunity tuples, 48 event tuples, and 11 exclusion tuples into three CSVs and a notes file | 5 | 4 | 5 | 5 | 5 | 3 | "Independent coding by coder_id=cursor from the frozen artifact corpus. / Reads nothing from coding/alpha or coding/bravo." (lines 2 to 4). `main()` never opens an input file. It does not read the frozen artifact corpus either. See Section 2, finding G1. Additionally `OUT = Path("/workspace/coding/cursor")` at line 13 is the only non-repo-relative path in the codebase, so this script creates that directory and reports success while writing nowhere near the repository. |
| `coding/cursor/notes__cursor.md` | 27 numbered judgement calls, 4 conflicts, and 3 vocabulary gaps, produced as the extraction prompt requires | 4 | 2 | 4 | 2 | 2 | 4 | "10. The Hog: no ATS receipt. Coded application from a titled GTM interview plus take-home. Medium confidence. Could have been opportunity." Model behaviour worth publicising: the coder flagged its own most likely error, and adjudication later reversed exactly that call. Buried in a notes file. |
| `coding/bravo/notes__bravo.md` | One line explaining that this coder filed no notes file | 1 | 3 | 2 | 2 | 1 | 1 | "Coder bravo did not file a separate notes file. Judgement calls on individual rows are in the `notes` column of applications__bravo.csv." Honest and complete. The asymmetry it records, that one coder complied with the prompt's reflective footer and the other did not, is never discussed anywhere. |
| `coding/bravo/*.csv` and `coding/cursor/*.csv` (6 files, grouped) | The two coders' extracts: 228 and 231 applications, 414 and 279 events, 44 and 45 exclusions | 4 | 3 | 4 | 3 | 2 | 3 | Bravo emitted `evidence_tier = A` on all 228 rows. Cursor emitted A on 205, B on 25, C on 1. A total systematic divergence on a field the protocol treats as central, and `evidence_tier` appears in none of the agreement statistics, so it is unmeasured. |
| `coding/platform/applications__freeze2.csv` and `exclusions__freeze2.csv` | 134 platform rows mapped from the LinkedIn and Jobright exports by script, plus one exclusion | 4 | 3 | 4 | 3 | 2 | 2 | Every row carries `confidence = medium`, `ats_system = none_observed`, `evidence_tier = C`, and `evidence_class = platform_log` as constants stamped by `ingest_platform.py:208-220`. These are defaults, not observations, and nothing in the CSV distinguishes them from coded values. |

## adjudication/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `adjudication/README.md` | Three-command runbook, the match-key spec, and the capture-recapture prohibition | 4 | 3 | 4 | 4 | 2 | 3 | "Match keys: lowercase `company_canonical` + `\|` + lowercase `role_as_listed` + `\|c` + `cycle`. If cycle is empty, treat as 1." The runbook lists three scripts. There are five, and `ingest_platform.py`, which produced the published 298-row full census, is not one of the three. A reader following this runbook cannot reproduce the headline number. |
| `adjudication/PRE-ADJUDICATION.md` | Machine-generated statistics block, the only place in the repository where kappa is actually computed and written down | 5 | 4 | 5 | 2 | 1 | 2 | "role_lane_kappa: 0.9510" (line 11). A bare number with no interpretation scale anywhere in the repository. A reader cannot tell whether 0.9510 is good, and cannot tell whether 0.7452 on the next-but-one line is a problem. One of those two answers is "yes". |
| `adjudication/ADJUDICATION.md` | The resolutions: two register disagreements, eight alias merges, seven uniques included, the opportunity list, and the headline census | 5 | 2 | 4 | 3 | 4 | 3 | "- evidence_class: employer_artifact (platform_log stratum empty; LinkedIn export absent) / - full census equals the employer_artifact stratum in this freeze" (lines 39 to 40). Both statements are false on this file's own output: `applications__adjudicated.csv` contains 220 `employer_artifact` rows and 1 `platform_log` row. The stratum is not empty, and the full census does not equal the stratum. See Section 2, finding G3 for why it is nearly empty. |
| `adjudication/FREEZE-2.md` | Freeze 2 accounting: 40 Jobright rows, 98 LinkedIn rows, 56 overlaps, 77 net-new, full census 298 | 4 | 2 | 4 | 3 | 2 | 3 | "Interviewed in full census: 14 (platform files carry no interview events)" The full census grows by 77 rows and the numerator stays fixed, so the reported rate falls from 14/221 to 14/298 for a purely structural reason. The parenthetical says so. Nothing forces a reader to notice that this is not a finding about the search. |
| `adjudication/compare_coders.py` | 221 lines. Loads each coder's applications into a dict keyed on company, role, and cycle, then computes percent agreement and Cohen's kappa on `role_lane` and on a binarized include decision, over the key intersection only | 4 | 3 | 4 | 3 | 3 | 5 | "```python\nboth = set(a) & set(b)\n```" plus the kappa computed only over `both`. The headline 0.9510 measures agreement between two coders *conditional on their already having agreed that a row exists at all*. The 17 bravo-only and 20 cursor-only rows, the disagreements that most affect the census, are excluded from the statistic by construction and reported separately. The file is correct and the reporting does not carry the caveat. |
| `adjudication/adjudicate.py` | 176 lines. Builds the 221-row census by unioning four hand-typed lists of match keys, then emits `ADJUDICATION.md` | 4 | 3 | 4 | 4 | 5 | 4 | Lines 130 to 133, inside the report's f-string: "- role_lane percent agreement: 0.9621 / - role_lane Cohen's kappa: 0.9510 / - include percent agreement: 0.9905 / - include kappa: 0.7452 (two disagreements on a rare class)". These are string literals. The script never calls `kappa()` and never imports `compare_coders`. See Section 2, finding G2. |
| `adjudication/derive_metrics.py` | 79 lines. Joins each coder's applications and events, derives interview status from event types, prints a JSON block per coder, writes nothing | 4 | 3 | 4 | 4 | 3 | 3 | "application_to_interview_rate_employer_artifact" (line 57) divides the *full census* interview count by the *employer_artifact* denominator. Running this script today prints `n_interviewed_census: 15` for cursor and `11` for bravo, against a published census figure of 14. Both are correct for what they measure and neither is the published number, and nothing in the file or the runbook explains the difference. |
| `adjudication/ingest_platform.py` | 584 lines. Converts the two platform exports into the study schema by substring rules, dedups them, matches them against Freeze 1 through a three-tier cascade, and writes five artifacts | 4 | 3 | 5 | 5 | 5 | 5 | `role_lane()` at lines 84 to 121: a 38-line if/elif ladder of `in` substring tests, with a modifier block at lines 89 to 97 that is a sequence of non-exclusive overwrites, so the last matching branch wins. `"lead"` matches inside "Lead Generation". One word-boundary test exists in the entire function. This is the closest thing in the repository to classification and it is a substring cascade. |
| `adjudication/*.csv` (4 files, grouped) | The adjudicated census (221), the full census (298), the platform match table (134), and the disagreement inventory (47) | 4 | 3 | 4 | 2 | 2 | 2 | `disagreements.csv` records 37 rows with `field = presence`, against 8 for `role_lane` and 2 for `register`. Most of those 37 are the same opening keyed two ways, not coder disagreement, and the file does not distinguish the two. |

## scripts/

| File | What it actually does | JAR | SO | ASM | REP | OVR | LEV | Worst offending block, verbatim |
|---|---|---|---|---|---|---|---|---|
| `scripts/redact_corpus.py` | 212 lines. Walks every `.md`, `.csv`, `.py`, `.txt`, and `.tsv` file in the repository and rewrites Gmail thread IDs, calendar event IDs, page tokens, and third-party email addresses into truncated SHA-256 pointers, in place | 4 | 2 | 4 | 5 | 3 | 4 | "Stable, one-way pointers" (line 4). For a low-entropy input space such as an email address, an unsalted truncated SHA-256 is reversible by dictionary attack in seconds. The pointers are stable and idempotent, which is the real and valuable property. They are not meaningfully one-way. Separately, if `artifacts/calendar/q8-lecturesfrom-primary.csv` is missing, `collect_calendar_ids` returns an empty set and the script proceeds, printing `calendar_ids=0` and leaving every calendar ID unredacted. That is a silent privacy failure presented as a successful run. |

## Where the repository is already adversarial

An audit that flags everything flags nothing. These score 1 on overclaiming because they are the opposite of overclaiming, and they are the reason this repository is worth translating rather than rewriting.

| File | The move |
|---|---|
| `README.md:9` | "247 applications, 11 interviews, and 4.45 percent are prior-audit figures. They are not the output of this freeze." A quarantine block at the front door that names the specific tempting numbers and refuses them. |
| `paper/RESULTS.md:120-128` | "What a skeptic should not be shown as a finding", an explicit blocklist of eight numbers and framings with the reason each is disqualified, including two that would have flattered the author. |
| `paper/DEFECTS.md:3` | "None of these is closed by inventing a number. Each is closed by an artifact or disclosed as unmet." |
| `artifacts/STOP-CONDITIONS.md` | "Waivers are explicit. They are not silent omissions." Seven stop conditions, four Partial, two Unmet, one Met, published as a table rather than quietly dropped. |
| `prompts/extraction.md:7` | "Accuracy beats coverage. An omitted row can be recovered later. A fabricated row poisons the census." An asymmetric-error statement at the top of a generation prompt. |
| `prompts/extraction.md:28` | "If you were tempted to fill a gap and did not, say what the gap was." |
| `knowledge/protocol.md:60` | "A completeness figure with a method and a caveat is publishable. A completeness figure asserted from feel is not." |
| `coding/cursor/notes__cursor.md` item 10 | A coder flagging its own most likely error, which adjudication then reversed. |

---

# Section 2. Global translation gaps

## The five concepts that recur untranslated

Ranked by how many files assume them. These are the highest-leverage rewrite targets because fixing one word fixes many paragraphs.

| Concept | Files that assume it | Why it blocks the reader | First honest definition |
|---|---|---|---|
| **freeze** | `README.md`, `CORPUS-MANIFEST.md`, `PROVENANCE.md`, `FREEZE-2.md`, `ADJUDICATION.md`, all seven `knowledge/` files | Used roughly 25 times as noun, verb, and ordinal ("Freeze 1", "this freeze", "frozen"). Never defined. A reader assumes it means "finished" when it means "no longer allowed to change". | A dated, enumerated, immutable input set. `CORPUS-MANIFEST.md:3` gets closest: "A coder holding a different set is running a different study." |
| **register** | `codebook.md`, `00-core.md`, `03-codebook.md`, `extraction.md`, `ADJUDICATION.md`, `RESULTS.md` | Two incompatible meanings, both in `00-core.md`. Line 27 means tone. Line 62 means which of two datasets a row belongs to. Nothing marks the switch. | The dataset sense is the important one, and it is the single best idea in the repository. See below. |
| **kappa** | `protocol.md:44`, `PRE-ADJUDICATION.md`, `ADJUDICATION.md`, `RESULTS.md`, `adjudicate.py` | Published as a bare decimal with no interpretation scale anywhere. A reader cannot tell that 0.9510 is strong and 0.7452 is the number that should worry them. | Agreement between two raters after subtracting the agreement you would expect from chance alone. |
| **capture recapture / Lincoln-Petersen** | `protocol.md:54-60`, `METHODS.md:15`, `RESULTS.md:24-30`, `DEFECTS.md:35`, `adjudication/README.md` | Named five times, always as a thing the paper is *not* doing. A reader cannot evaluate a refusal to use a method they have never heard of. | Estimating a population you cannot see by measuring the overlap between two independent attempts to see it. |
| **evidence tier vs evidence class** | `codebook.md`, `00-core.md:53-60`, all coder CSVs, `RESULTS.md`, `protocol.md` | Two orthogonal axes with similar names, never contrasted in one place. Tier is how strong the proof is (A, B, C). Class is who produced it (employer or platform). | They answer different questions and are used for different things: tier gates confidence, class defines the sensitivity-analysis strata. |

Honourable mentions, all undefined and all load-bearing: `stratum`, `dedupe key`, `census`, `floor`, `net-new`, `cycle`, `date precision`, `ATS`, `Easy Apply`, `interview loop`, `harvest`, `sweep`, `gold standard`, `pre-registration`, and `nextPageToken`.

## What is genuinely interesting and currently buried

| Finding | Where it is now | Why a GTM reader would care |
|---|---|---|
| Jobright's 40 raw tracker rows produced 5 net-new applications | `01-engagement.md:61` | "A naive sum across four trackers would have reported roughly 315 instead of 247." This is a 28 percent overstatement avoided by deduplication, and it is the most concrete argument in the repository for doing the boring work. It sits in an internal brief. |
| Calendar keyword search for "interview" returned zero events | `protocol.md:69`, `01-engagement.md:96` | The obvious query returned nothing because interview invites carry generic titles. The fix was to stop filtering and sweep 90-day blocks exhaustively, which found 31 events. A transferable lesson about searching for a thing by the wrong name. |
| The two-register rule | `00-core.md:62-69` | "A job search has two independent pipelines, and mixing them makes both unmeasurable." Named "the single most important structural decision in this work" and never explained to a reader outside the internal files. |
| `what_would_promote_it` as a column | `exclusions__*.csv`, `codebook.md` | Every rejected row records what evidence would reverse the rejection. That turns an exclusion list from a graveyard into a work queue. |
| A coder predicting its own error | `notes__cursor.md` item 10 | The model flagged The Hog as its least confident call. Adjudication reversed exactly that call. Direct evidence that the reflective footer in the extraction prompt does real work. |
| 31 calendar events, 1 in the events tables | `q8-lecturesfrom-primary.csv`, coder CSVs | Both coders emitted exactly one `gcal` event. The calendar sweep was the fix for a known blind spot and produced almost nothing downstream. Nothing in the paper notes this. |

## Where the repository overclaims

Five findings, each verified against the code.

### G1. "Independent coding" describes judgements that the committed script does not perform

`coding/cursor/generate_cursor_coding.py` opens with "Independent coding by coder_id=cursor from the frozen artifact corpus." Its `main()` never opens an input file. It does not read `artifacts/` at all. The file is 221 literal application tuples, 10 opportunity tuples, 48 event tuples, and 11 exclusion tuples, reshaped into CSVs by a loop.

This does not mean the coding was not independent. The judgements were plausibly made by a model reading the corpus in a prior session and then serialized into this file, and `notes__cursor.md` reads exactly like the reflective footer `prompts/extraction.md:28` demands. But the repository presents a *generator* as a *coder*, and a reader who runs it learns nothing about how the rows were produced. `coding/bravo/` has no generator at all.

**UNVERIFIED, confirm with the author:** whether an LLM produced the cursor tuples by reading the frozen corpus, and by what process bravo's CSVs were produced. Nothing in the repository establishes either.

The stakes are the paper's central claim. `protocol.md:33` says independent parallel coding "is the design decision that upgrades the paper from one person's spreadsheet to a measured instrument." That upgrade rests entirely on a process the committed artifacts do not document.

### G2. The published reliability statistics are string literals

`adjudicate.py:130-133` writes the four agreement figures into `ADJUDICATION.md` as hardcoded text inside an f-string. The script never calls its own `kappa()` function and never imports `compare_coders`. The real figures are computed by `compare_coders.py` into a different file, `PRE-ADJUDICATION.md`.

They agree today. Verified: both files carry 0.9621, 0.9510, 0.9905, and 0.7452. Nothing keeps them agreeing. Recode a single row, re-run `adjudicate.py`, and `ADJUDICATION.md` will report a freshly computed census `n` beside four stale kappa figures, with no error and no warning. `paper/RESULTS.md:44-46` quotes those figures as the paper's reliability evidence.

This is a structural defect, not a live contradiction, and it should be stated that way.

### G3. The `platform_log` stratum is empty for a mechanical reason, and the paper leans on it

Verified counts:

| File | employer_artifact | platform_log |
|---|---|---|
| `coding/bravo/applications__bravo.csv` | 211 | 17 |
| `coding/cursor/applications__cursor.csv` | 231 | 0 |
| `adjudication/applications__adjudicated.csv` | 220 | 1 |

Cursor's zero is not an observation. `generate_cursor_coding.py:517` sets `row["evidence_class"] = "employer_artifact"` unconditionally, for every row, with no branch. It is a constant.

`adjudicate.py:88` resolves every dual-agreement row with `add(cursor[k], ...)`, taking the cursor row whenever both coders produced one. So cursor's constant overwrites bravo's 17 actual `platform_log` observations, and the adjudicated census emerges with 1.

`ADJUDICATION.md:39-40` then reports "platform_log stratum empty" and "full census equals the employer_artifact stratum in this freeze". Both are slightly false on the file's own output, and the near-emptiness is an artifact of one generator's constant plus one tie-break rule.

The consequence reaches the protocol. `protocol.md:26` names the primary outcome as a count "reported at two strata, `employer_artifact` and full census". `protocol.md:48` rests a 20-point GTM-share gap between the two strata on data that the committed corpus can no longer reproduce, because one of the two strata was flattened before adjudication ran. `derive_metrics.py:57` computes a per-stratum interview rate that is only harmless because the two denominators are now identical.

### G4. The classification and matching are substring rules, and read as machine learning

Three places where the vocabulary invites a reader to assume more than the code does:

- `ingest_platform.py:84-121`, `role_lane()`. A 38-line if/elif ladder of substring tests that assigns every platform row to one of eight lanes. The modifier block at lines 89 to 97 applies non-exclusive overwrites, so a title matching four branches keeps only the last. One word-boundary test in the whole function.
- `ingest_platform.py:413-429`, `roles_equivalent()`. Ordered token-prefix containment. No edit distance, no similarity score, no threshold, no embedding.
- `compare_coders.py` and `adjudicate.py`. "Comparing coders" is dict intersection and `==`. "Adjudication" is the union of four hand-typed lists totalling 15 pasted match-key strings.

None of this is wrong. Deterministic rules are the right choice for an auditable census, and `ingest_platform.py:491` earns real credit for refusing ambiguous multi-hits (`if len(equivalent) == 1`) rather than guessing. The problem is only that "coding", "adjudication", and "classification" are doing rhetorical work the implementation does not.

### G5. Freeze 2 dilutes the interview rate for a structural reason

`FREEZE-2.md` reports the full census at 298 and interviewed at 14, unchanged, with the parenthetical "(platform files carry no interview events)". Platform rows carry no events by construction: `ingest_platform.py` emits no event rows at all. So the denominator grew by 77 and the numerator could not move.

Verified: interviewed on the 221-row census is 14, and interviewed on the 298-row full census is also 14.

Any reader comparing 14/221 against 14/298 is looking at a measurement artifact, not a change in outcomes. `RESULTS.md` reports both as unreduced fractions, which is the right instinct, and neither the results draft nor the freeze note states plainly that the second fraction cannot differ from the first.

## Reproducibility gaps, aggregated

Where a reader without this exact environment fails, and fails silently.

| Gap | Location | Failure mode |
|---|---|---|
| Hardcoded container path | `generate_cursor_coding.py:13`, `OUT = Path("/workspace/coding/cursor")` | Creates the directory, writes the CSVs there, prints success. The reader finds no output in the repository and no error. |
| Runbook omits the script that produced the headline | `adjudication/README.md` lists three scripts; `ingest_platform.py` produced the 298-row census | Following the runbook cannot reproduce the published full census. |
| 15 hardcoded match keys | `adjudicate.py:48-69` | Any retitling in a source CSV raises an uncaught `KeyError`. The merges are not a rule, they are 15 strings that must match byte for byte after lowercasing. |
| Destructive redaction with no dry-run | `scripts/redact_corpus.py` | In-place rewrite of every text file including itself, no backup, no confirmation, no flag. Recovery depends entirely on git. |
| Silent redaction failure | `redact_corpus.py:129-140` | A missing calendar CSV yields an empty ID set and the script proceeds, leaving every calendar ID in cleartext while printing `calendar_ids=0`. |
| Frozen capture date | `ingest_platform.py:19`, `CAPTURE = "2026-08-29"` | Re-running against a fresh export stamps the wrong capture date on every relative timestamp, silently corrupting the date-precision field. |
| Missing-file handling is inconsistent | `derive_metrics.load` and `ingest_platform.load_csv` have no existence guard; `compare_coders` and `adjudicate` do | Same repository, four different behaviours for the same failure. |
| No dependency manifest | repository root | No `requirements.txt`, no `pyproject.toml`. Stdlib only in practice, which is good and is nowhere stated. |
| Retrieval cannot be re-run by anyone | `README.md:22` | Requires live Gmail and Calendar connectors on two named accounts, one of which the repository itself records as unreachable. |
| Corpus points outside itself | `retrieval-log-028.md` | Refers to run transcript files "under the agent tools directory for this session" that are not committed, in a corpus declared identical for every coder. |

## Data defects worth fixing regardless of the translation

| Defect | Evidence |
|---|---|
| `work_type = Atlanta` on three rows | Verified in `applications__cursor.csv` and carried into both `applications__adjudicated.csv` and `applications__full_census.csv`: `verkada\|enterprise-solutions-engineer-atlanta\|c1`, `speechify\|go-to-market-engineer-atlanta\|c1`, `insignia-collab\|unspecified\|c1`. All three have empty `location`. A location value landed in the `work_type` slot. The codebook vocabulary is `remote`, `hybrid`, `onsite`, `unstated`. |
| PhrasIQ named in the blinded codebook | `codebook.md:53` |
| `ADJUDICATION.md:39-40` contradicts its own CSV | 220 plus 1, not 221 plus 0 |
| Counting rules numbered 1 to 9, cited as "rules 1 to 8" | `00-core.md:41` |
| "Q1" means a retrieval query in `QUERY-MANIFEST.md` and a calendar quarter in `RESULTS.md:110` | Same repository, same token, two referents |
| Calendar sentinel row is structurally invalid | `q8-lecturesfrom-primary.csv`, `no events in block` written into the `end` column |
| `Onsite` versus `On-site` un-normalized across the two platform exports | `jobright_applications_log.csv` and `linkedin_applied_jobs_pages_1_to_10.csv` |
| No `ambiguous` match status, so a refused match is emitted as `net_new` | `ingest_platform.py:491` correctly refuses to match when tier 3 yields more than one candidate, then line 506 emits the record as `net_new`. `match_status` carries three values across all 134 rows of `adjudication/platform_match.csv`: `net_new` 77, `overlap` 56, `opportunity_or_non_census` 1. The refusal is therefore invisible downstream, and the 298-row full census carries no "of which K unresolved" caveat. Surfaced by a review bot on this branch and verified. |
| `INTERVIEW_TYPES` duplicated verbatim in four files | `compare_coders.py:47` (unused), `derive_metrics.py:9`, `adjudicate.py:9`, `ingest_platform.py:533`. No shared module. A change in one silently desynchronizes the others. |
| Four incompatible identifier spaces | slugged `application_id`, the lowercase comparison key, `role_key()`'s alphanumeric-only key, and `dedupe_platform`'s un-aliased variant. Joins cross these boundaries in `adjudicate.py:102-108` and `ingest_platform.py:546-550`. |
