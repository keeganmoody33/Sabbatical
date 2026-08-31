# Integrity defects

None of these is closed by inventing a number. Each is closed by an artifact or disclosed as unmet.

## The Hog and BX Studio were adjudicated out on a premise that turned out to be false

Closed at Freeze 3, 2026-08-30. Logged in `knowledge/protocol.md`.

Both were adjudicated to the opportunity register at Freeze 1 on one stated ground: no submission artifact existed anywhere in the corpus. They were also the only two include-or-exclude disagreements between the blind coders, the pair that produced the include kappa of 0.7452.

The LinkedIn formal export, ingested at Freeze 3, carries a submission row for each. The Hog applied 2026-06-04, eleven days before its interview invitation. BX Studio applied 2026-04-06, two days before its employer acknowledgment. Both precede the process events already coded here, which is the corroboration pattern that makes them submissions rather than coincidence.

The rule did not change. An interview with no submission still does not mint an application row. Its premise did. Each row was taken from the coder who had read it as an application, so the surviving row is a real coder's judgement rather than one assembled during adjudication.

Consequence: census 221 becomes 223, interviewed applications 13 becomes 14, the rate 13/221 becomes 14/223, the latency base 196 becomes 197, and the full census 298 becomes 317.

This is the `what_would_promote_it` column working as designed. It is also a caution: the adjudication was correct on the evidence available and still produced the wrong answer for fifteen months, which is what a bounded census means in practice.

## The ambiguous match branch fired on real rows for the first time

Not a defect. Recorded because an earlier entry in this file stated that zero rows hit the branch, and that is no longer true.

When the LinkedIn export was ingested at Freeze 3, two rows hit the multi-candidate refusal: Attentive GTM Engineer and FOSSA GTM Engineer, each matching both cycles of a genuine re-application. The matcher declined to name a parent, carried both candidate ids, and counted the rows as overlap without asserting which cycle they belong to.

That is exactly the case the branch was written for. `platform_match.csv` now reports 61 overlap, 2 overlap with an unresolved parent, and 94 net-new.


## WorkOS register assignment

Closed for this freeze.

Artifact: Gmail log 020, thread with Somya Shruti at TopHire, 2025-08-25 to 2025-08-27. Recruiter approach for a remote GTM Engineer role at WorkOS. Interest confirmed, a slot booked, a resume requested. No submission receipt exists in the frozen corpus.

Adjudication rule applied: `discovery_source = recruiter_inbound`, `register = opportunity`. It stays in the dataset. It does not enter the application census or any application-to-interview rate.

The 212-row prior audit listed WorkOS as Interviewed. The 247-row ledger omitted it. Both can be true under the two-register rule. The 212 row was an opportunity. Dropping it from an application ledger was correct. Treating the drop as a missing application would be wrong.

## 212 to 163

Still undocumented.

The prior Gmail-only floor used as the [S1] base was 163. The relationship from the 212-row audit to that 163 is not reconstructable in this repository. The [S1] and [S2] workbooks are not in the artifact set. See `artifacts/platform/KEEGAN-EXPORTS-ABSENT.md`.

This freeze does not inherit 163, 212, or 247 as counts. Those remain prior-audit floors.

## Dedupe key includes cycle

The unit of analysis is `company_canonical + role_as_listed + cycle`. Application IDs are `company-slug|role-slug|c{n}`.

FOSSA in this corpus: receipt 2026-04-22, decline 2026-05-20, second receipt 2026-05-21. That is `c1` then `c2`.

Attentive: receipt 2026-06-22, decline 2026-07-07, second receipt 2026-07-15. That is `c1` then `c2`.

A key that omitted cycle would collide those pairs.

## Weave 2026 interview attached to the wrong application

Closed for this freeze. Coding correction logged in `knowledge/protocol.md`.

Artifact: `gth_0339a17e3860d167`, Ashby, 2026-08-18, retrieval log 010, reading "thank you for taking the time to meet and interview with us." That is a post-interview decline, so an interview did happen.

Cursor attached it to `weave|business-development-manager|c1` as a `hiring_manager_interview` and set that application's terminal outcome to `rejected_after_interview`. The BDM application was submitted 2025-07-27 and declined 2025-07-31, so the interview event sat 383 days after the rejection that closed the same cycle. Bravo did not attach it at all, filing it as an exclusion with reason `unresolvable_identity` and the note that it has no parent. The two coders also disagreed on this row's terminal outcome, a field the adjudication pass never covered.

Rule applied: the 2026 process is a separate opening at the same company. It is inbound with no submission artifact anywhere in the corpus, which is the same case as The Hog, so it goes to the opportunity register. An interview with no submission does not mint an application row. The event is excluded from the interview derivation by named decision in `adjudication/adjudicate.py`, and the BDM application reverts to `rejected_no_interview` dated 2025-07-31.

Consequence for downstream numbers: interviewed applications 14 becomes 13. The application-to-interview rate 14/221 = 0.0633 becomes 13/221 = 0.0588. `rejected_after_interview` 6 becomes 5, `rejected_no_interview` 73 becomes 74. The application census stays 221 and the full census stays 298, because the opening moved to the opportunity register rather than out of the dataset. Time to first interview moves from n = 12, median 6, mean 40.3, max 387 to n = 11, median 6, mean 8.8, max 34, so that single event was carrying the mean.

Provenance of the correction, stated because it matters: it came from the author, from recall, after seeing the analysis. The subject and the author are the same person, which `knowledge/instructions.md` requires be treated as a stated limitation rather than softened. Two things support it. Bravo reached nearly the same conclusion independently under blind conditions, so the correction moves the census toward the blind coder's judgement rather than away from it. And the artifact itself establishes that an interview happened; only its attachment was wrong.

What remains recall and is not recorded as evidence: the 2026 role title, the counterparty's name, and the inbound origination. The corpus establishes none of the three. Under `prompts/extraction.md` rule 8 recall is never disguised as evidence, so none is written into a structured field. The interview date is unknown and bounded by the 2026-08-18 decline. The personal Gmail calendar, stop condition 2, remains unreachable and is where a calendar artifact for it would live.

## Ambiguous platform matches were counted as net-new

Closed for this freeze. Pipeline change logged in `knowledge/protocol.md`.

`adjudication/ingest_platform.py` matches platform rows against Freeze 1 in three tiers, the last of which treats two titles as the same opening when one token sequence is an ordered prefix of the other. That tier already refused to act when more than one Freeze 1 row matched, which is correct. The refusal had nowhere to go. The row fell through to the net-new branch and became indistinguishable from a row with no counterpart, so a possible duplicate could enter the full census with nothing marking it unresolved.

Rule applied: a platform row matching more than one Freeze 1 row carries `match_status = ambiguous` and a `candidate_parent_ids` column listing the rows it could not choose between. It is recorded in `adjudication/platform_match.csv` and held out of `adjudication/applications__full_census.csv`. An omitted row can be recovered later. An inflated census cannot be corrected once nothing distinguishes the inflating rows.

Consequence for downstream numbers: none in this freeze. Zero rows hit the branch on the current corpus. The three tiers were instrumented before the change and resolve to 46 exact, 6 unspecified-fallback, 4 unique-equivalent, and 77 with no candidate at all. `platform_match.csv` remains 134 rows at overlap 56, net-new 77, opportunity or non-census 1. `applications__full_census.csv` remains 298 and byte-identical. `FREEZE-2.md` now reports the ambiguous count, which is 0, and states the census as n with k unresolved whenever k is not 0.

The defect survived the original build because it was invisible. A refusal that produces no distinguishable output looks exactly like a decision that was never needed.

## A derived interview contradicts a stored terminal outcome

Open. Found 2026-08-30 by a check added in `pipeline/data_quality.py`, which now runs on every pipeline run.

`jobmail-io|growth-lead|c1` carries an interview event and a `terminal_outcome` of `rejected_no_interview`. Both values came from cursor, on a cursor-unique row that bravo never coded, so no blind second reading exists to break the tie.

No published figure moves. `interviewed` is derived from the events table and never stored, so the count of 13 and the rate 13/221 are unaffected either way. What is affected is the terminal-outcome distribution, where this row sits in `rejected_no_interview` while also appearing in the interview set.

It is not resolved here, for the same reason the Weave row was not resolved by preference. Terminal outcome is a field the adjudication pass never covered, this row has one coder rather than two, and closing it would require either a new artifact or a recall-sourced decision. Recall is what `prompts/extraction.md` rule 8 forbids writing into a structured field.

What would close it: the underlying artifact for that process, which would establish whether an interview happened and therefore which of the two fields is wrong.

The general point is the reason the check was added. `interviewed` is derived and `terminal_outcome` is stored, so the codebook's first design principle, store observations and compute rollups, was followed in one direction and not the other. Two representations of the same fact will eventually disagree, and this is what it looks like when they do.

## Capture recapture still not computed, now for a sharper reason

The Freeze 3 export was the best remaining chance at the stratum the protocol requires, and it does not deliver it.

The estimator is restricted to LinkedIn rows submitted through an external ATS rather than Easy Apply. The export carries no such flag. Twenty rows mention "Easy Apply" in free text and all twenty also carry a downstream ATS confirmation, so the phrase describes the export record rather than the channel.

What the export does give: 16 LinkedIn rows with downstream employer-side confirmation, and 83 without. The 83 mix rows that were Easy Apply and therefore structurally invisible to ATS mail with rows that generated ATS mail Gmail retrieval missed. Only the second is informative about completeness, and nothing distinguishes them. Inferring the split from whether ATS mail was found would assume the thing being estimated.

Stop condition 3 is now Met for the applied list and still Unmet for the channel label.

## Capture recapture not computed

The protocol restricts two-source capture recapture to LinkedIn rows submitted through an external ATS, not Easy Apply. Freeze 2 has LinkedIn pages 1 to 10 without that channel label. Naive Lincoln Petersen on Gmail overlap versus Easy Apply is a misuse and was not run.

The overlap stratum is unmeasured. Completeness is therefore not reported as a percentage.

## Four redaction defects wrote real names into a public repository

Found by auditing the committed extracts under `challenge/`, not reported by anyone. Every one was
introduced by this repository's own code. They are recorded here in full because the failure mode
is the interesting part: each fix was individually reasonable and each created the next hole.

1. **The shape test required two to three tokens.** A `Contacts / Rounds` cell reading
   `Clayton (1 interview)` reduces to one word, which no rule matched. Thirteen interviewer given
   names shipped in the clear. Inside a column that holds people by definition, the absence of a
   surname is not evidence that a word is not a person.
2. **Parentheses were stripped after splitting, not before.** A semicolon inside the parentheses of
   `Eddie (2 interviews; final was 1 hour)` split it into fragments no shape test could judge. `+`
   was not a separator at all, so `Gurjap Sandhu + Kofi Boamah O.` stayed one six-token fragment and
   two full names survived.
3. **The organization guard matched raw substrings in both directions.** The workbook holds a
   company called `Vi`. That two-letter string is inside `Teresa Vitale` and `Vikas CV`, so the
   guard protected both names from redaction. The reverse direction is now gated at four characters.
4. **`UNKNOWN — <person>'s company` placeholders were treated as company names.** `Jacob Bowman` was
   shielded from redaction by a string built out of his own name.

Two further problems surfaced while fixing these, both of them over-redaction rather than leakage.
Redacting bare given names everywhere destroyed `Austin` the city inside a role title and two
locations, so given names are now scoped to columns that are not a company, role, title, location or
join key, while full names stay global. And the organization guard could only see companies the
workbook **kept**: `Lumenalta`, `Proofpoint` and `Designit` were dropped from its ledger, survive
only in a prose note about their removal, and were hashed as people until the guard was seeded from
this repository's own census, which still holds all three.

**What is now in place.** A review gate runs on the redacted text before anything is written. Any
capitalized word that survives redaction in a person-bearing column and appears on no list fails the
extraction with the list printed. The single-token prose case cannot be settled by shape, because
`Patrick originated the opportunity` and `Community post is the source` have identical form, so it
is settled by review once and recorded in two named sets. The previous version made that call
silently, which is precisely how the names shipped.

The extracts were audited in both directions after the fix: no person in the clear, and no company
or job title destroyed. No published figure moved. `challenge/supplementary_ledger.csv` changed only
because two redacted join keys changed, with every disposition count identical.

**What this does not fix.** The redaction is a best-effort heuristic over free text, not a
guarantee. It is now loud instead of silent, which is a real improvement and not the same as being
correct. The workbook itself remains uncommitted for this reason.

## Three of the fourteen interviews were invitations

**Corrected at Freeze 4, 2026-08-30. The headline moved from 14/223 to 11/223.**

The interview derivation counted an `event_type`. The codebook gave coders no rule separating an
artifact that **proposes** a conversation from one that **records** one, so `recruiter_screen` and
`hiring_manager_interview` were assigned to invitations as readily as to completed rounds.

Hypergen carried an interview invitation dated 2026-04-14 and nothing after it. TestGorilla carried
a recruiter intro and an assessment invitation. RevSpring carried a screen request. None carries a
scheduling confirmation, a post-process decline, a candidate survey, a `SENT` reply, or a later
stage, and all ten surviving interviews carry at least one of those.

**The corpus had already said so.** `artifacts/gmail/retrieval-log-006.md` records that the Hypergen
thread holds an invitation and that the prior ledger's Interviews sheet does not list Hypergen. That
note was written at capture time and nothing acted on it for the length of the study.

**Bravo blind-coded Hypergen `employer_ack`.** Cursor coded it an interview and adjudication took
cursor. The blind coder was right and the adjudication was wrong, which is the failure mode
adjudication is supposed to catch rather than introduce. On TestGorilla and RevSpring both coders
made the same call, so those two are a missing rule rather than a bad adjudication.

The author disputed these four rows from recall, which is what prompted the re-read. The resolution
came from the artifacts and does not rest on the recall: every fact was in the frozen corpus
already. `jobmail-io` remains counted and remains an open defect, because its decline says the
requested steps were completed, which an asynchronous screening would also produce.

Full evidence table for all fourteen: `adjudication/INTERVIEW-EVIDENCE.md`.

## Personal names in cleartext in the frozen corpus

`artifacts/gmail/*.md` carries nine personal names in cleartext across six retrieval logs, while the
same files redact sender addresses to `eml_` pointers. The inconsistency is pre-existing and sits in
frozen files.

Raised with the author on 2026-08-30, who elected to leave the corpus as it stands. Recorded here
and in `paper/NAMED-COMPANIES.md` so that it is a live decision before anything is published rather
than an oversight discovered afterwards.

