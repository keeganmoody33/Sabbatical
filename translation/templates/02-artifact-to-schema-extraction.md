# Template 2. Artifact to schema extraction

**What this proves you can do:** turn an unstructured inbox into a structured funnel without the model inventing rows to fill gaps.

**Extracted from:** `prompts/extraction.md`, `coding/README-coder.md`, `codebook.md`.

**One-line form:** Classify `{{RAW_ARTIFACTS}}` into `{{SCHEMA}}` using `{{CONTROLLED_VOCABULARY}}`, bounded by `{{NEVER_INFER_RULES}}`, and output `{{ROWS}}` plus `{{JUDGEMENT_LOG}}`.

---

## The template

```
You are extracting structured records from {{ARTIFACT_TYPE}} into a research
dataset. Accuracy beats coverage. An omitted row can be recovered later. A
fabricated row poisons the dataset.

YOUR OUTPUT IS ROWS, NOT PROSE.
Emit {{TABLE_1}}, {{TABLE_2}}, and {{TABLE_3}} rows as tables using exactly
the field names and vocabularies below, with {{SOURCE_ID_FIELD}} as the first
field of every row. Do not invent fields. Do not invent vocabulary values.
If a value does not fit, emit the named fallback for that field and describe
the unmatched value in `notes`.

SCHEMA:
  {{TABLE_1}}: one row per {{PRIMARY_UNIT}}. Fields: {{FIELD_LIST_1}}
  {{TABLE_2}}: one row per timestamped interaction. Fields: {{FIELD_LIST_2}}
  {{TABLE_3}}: one row per candidate you considered and REJECTED.
               Fields: {{FIELD_LIST_3}}, including `what_would_promote_it`

VOCABULARIES: {{CONTROLLED_VOCABULARY}}
FALLBACKS: {{PER_FIELD_FALLBACK_MAP}}

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
4. Every date gets a precision label from {{DATE_PRECISION_VOCAB}}. A relative
   stamp requires a capture date. Never upgrade a relative date to an exact one.
5. A repeat {{PRIMARY_EVENT}} for the same {{ENTITY}} after a terminal outcome
   is a new cycle. Increment the cycle, mint a new id, do not overwrite.
6. Assign {{STRATUM_FIELD}} by WHO produced the artifact, not by how good it is.
   {{STRATUM_A_RULE}}. {{STRATUM_B_RULE}}.
7. Assign {{REGISTER_FIELD}} = {{SECONDARY_REGISTER}} when the process began
   without {{PRIMARY_EVENT}}. These rows stay in the dataset and out of the
   headline count. See template 03.
8. Anything sourced from recall rather than an artifact gets
   `evidence_system = memory`. Never disguise recall as evidence.
9. When two artifacts conflict, emit the better-evidenced value and record the
   conflict in `notes`. Do not average. Do not pick silently.

BEFORE THE TABLES, output a three-line header:
  - Artifacts processed: n
  - Rows emitted: {{TABLE_1}} n, {{TABLE_2}} n, {{TABLE_3}} n
  - Conflicts and unresolved identities: a numbered list, or "none"

AFTER THE TABLES, list every judgement call you made, one line each. If you
made none, say so. If you were tempted to fill a gap and did not, say what
the gap was.

Do not optimize toward a total. You are not trying to reach a number. Fewer
rows because the evidence was thinner is the job done correctly.
```

---

## The three parts that do the work

**The asymmetric error statement.** "An omitted row can be recovered later. A fabricated row poisons the dataset." Most extraction prompts imply both errors cost the same. They do not. Saying which one you fear tells the model which way to lean when it is unsure.

**A named fallback per field.** The original is specific: `unknown` where the vocabulary includes it, `none_observed` for `ats_system`, and never both (`codebook.md`). A model with no legal way to say "I could not tell" will invent something plausible. Give it a legal way.

**The temptation prompt.** "If you were tempted to fill a gap and did not, say what the gap was" (`prompts/extraction.md:28`). This one line surfaces near-hallucinations that would otherwise be invisible. In the source repository it worked: the coder wrote "The Hog: no ATS receipt. Coded application from a titled GTM interview plus take-home. Medium confidence. Could have been opportunity" (`coding/cursor/notes__cursor.md` item 10). Adjudication later reversed exactly that call. The model predicted its own error and was right.

## The rejection table is not optional

Most people building this keep two tables and throw away the rejects. Keep three. The `what_would_promote_it` column turns your exclusion list from a graveyard into a work queue: it records, per row, the exact evidence that would reverse the decision. A real example from `coding/cursor/exclusions__cursor.csv`, for an employer who said they could not find the application in their system: `what_would_promote_it = An ATS receipt the founder can see`.

## What breaks if you skip it

The model fills gaps. Not maliciously, and not obviously. It infers a company name from an email domain, upgrades "1mo ago" to a calendar date, or promotes a rejection letter into proof that an application was submitted. Each of these is individually reasonable and collectively fatal, because you can no longer tell which rows are observations and which are inferences.
