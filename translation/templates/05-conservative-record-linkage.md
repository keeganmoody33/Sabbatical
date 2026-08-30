# Template 5. Conservative record linkage and an idempotent dedup key

**What this proves you can do:** design a deduplication key that survives being re-run, and a matcher that refuses to guess when it cannot tell.

**Extracted from:** `adjudication/ingest_platform.py:328-507`, `codebook.md`, `paper/DEFECTS.md:31`, `knowledge/01-engagement.md:61`.

**One-line form:** Match `{{SOURCE_A_RECORDS}}` against `{{SOURCE_B_RECORDS}}` using `{{NORMALIZATION}}` plus `{{ALIAS_TABLE}}` plus `{{EQUIVALENCE_RULE}}`, bounded by `{{REFUSE_ON_AMBIGUITY}}`, and output `{{MATCH_STATUS}}` per record, one of overlap, net_new, ambiguous with its candidate parent ids, or {{NON_CENSUS}}.

---

## The problem it solves

Four trackers each hold a partial record of the same activity. Every one of them double-counts the others. Sum them naively and you get a number that is confidently wrong in the direction that makes you look busiest.

The source study's own accounting (`knowledge/01-engagement.md:61`):

> "The Jobright row is the strongest single argument in the paper: 40 raw rows produced 5 net-new applications. A naive sum across four trackers would have reported roughly 315 instead of 247."

That is a 28 percent overstatement avoided by matching rather than adding.

---

## Part 1. The dedup key

```
KEY = {{NORMALIZED_ENTITY}} | {{NORMALIZED_SUBJECT}} | {{CYCLE}}

Three properties, all required:

DETERMINISTIC. Same inputs always produce the same key. No timestamps, no
random ids, no row numbers, no insertion order.

IDEMPOTENT. Re-running the pipeline on the same data produces the same keys
and therefore the same merges. You can re-run without accumulating rows.

CYCLE-AWARE. The third component is what lets a genuine repeat be a repeat.

  Rule: a new {{PRIMARY_EVENT}} for the same entity and subject, AFTER a
  terminal outcome on the previous cycle, increments the cycle and counts
  again. Without a terminal outcome it is the same cycle, no matter how
  many artifacts arrived.
```

The cycle component is the part people leave out, and the source study documents exactly what it cost them (`paper/DEFECTS.md:31`, `knowledge/01-engagement.md:79`). Their original key was `company|role`. Two genuine re-applications, to FOSSA and to Attentive, collapsed into their first attempts. The fix was `company|role|cycle`.

The counting rule that governs it (`codebook.md`, `knowledge/00-core.md:46`): FOSSA's first cycle carries a rejection dated 2026-05-20, and that terminal outcome is what licenses the second cycle dated 2026-05-21. A repeat without a terminal outcome is not a new cycle. Pogo had three artifacts across Gem and Ashby with no terminal outcome between them, and stayed one cycle (`coding/cursor/notes__cursor.md` item 14).

## Part 2. The matcher

```
Match each {{SOURCE_A}} record against {{SOURCE_B}} in three ordered tiers.
Stop at the first tier that produces exactly one candidate.

TIER 1, EXACT AFTER NORMALIZATION.
  Normalize: lowercase, strip all non-alphanumerics, then apply
  {{ALIAS_TABLE}}, a hand-maintained map of known equivalences.
  {{ALIAS_TABLE}} handles what no rule can: acquisitions, rebrands,
  legal-entity suffixes, and typos in the source export.

TIER 2, ENTITY-LEVEL FALLBACK.
  If the subject on the {{SOURCE_B}} side is literally "{{UNSPECIFIED}}",
  match on entity alone. Use this ONLY where the schema records an admitted
  unknown, never as a general loosening.

TIER 3, TOKEN-PREFIX EQUIVALENCE.
  Tokenize both subjects. Drop {{NOISE_TOKENS}}: location words, posting-site
  boilerplate, and workplace-type words. Expand {{ABBREVIATIONS}}. Delete
  parenthetical tails.
  Two subjects are equivalent when one token sequence is an exact ordered
  prefix of the other.

  This catches "AE" against "Account Executive", and "Solutions Engineer
  Atlanta" against "Solutions Engineer". It does NOT merge "GTM Engineer"
  with "GTM Engineering Team Lead", because `engineer` and `engineering`
  are different tokens.

THE RULE THAT MATTERS MOST:
  If tier 3 produces more than one candidate, MATCH NOTHING. A wrong merge
  silently destroys a record. An unmerged duplicate is visible and fixable
  later, but ONLY if you can still see it.

  So do not emit an ambiguous record as plain net_new. Give it its own
  status, `ambiguous`, and carry the candidate parent ids it could not
  choose between. A refusal you cannot find later is not conservative, it
  is an unrecorded merge decision.

  Never merge on a similarity score. If you cannot state the rule that made
  two records the same, you cannot defend the count.

OUTPUT, per record, one of FOUR statuses: overlap with a named parent id;
net_new; ambiguous with its candidate parent ids; or {{NON_CENSUS}}.
Never a bare merged total with no provenance.

REPORT the ambiguous count alongside the total. A census of {{N}} with
{{K}} unresolved is a different claim from a census of {{N}}.
```

The refusal rule is `ingest_platform.py:491`, a single line, `if len(equivalent) == 1`. It is the most defensible decision in the file.

## Two worked merges

**Listen and Listen Labs.** LinkedIn's applied list records the company as "Listen". Freeze 1 records "Listen Labs". Same Lead GTM Engineer role, same process. Treating them as two companies inflated the full census from 298 to 299. Caught by the alias table, and recorded in the commit that fixed it.

**Five titles that expand or abbreviate a known role** (`adjudication/FREEZE-2.md`): Thomson Reuters "AE Tax or Risk" against "Account Executive, Tax or Risk Products". Foursquare "AE New Business" against "Account Executive". UpGuard "SDR Manager". Verkada "Enterprise Solutions Engineer Atlanta", where "Atlanta" is a noise token. All five are overlap, not net-new. Without tier 3 the census would have been overstated by five.

## Adapting it

`{{NOISE_TOKENS}}` in the source is hardcoded to one person's geography: `atlanta`, `ga`, `austin`, `tx`, plus `remote`, `onsite`, `hybrid`, `greater`, `area`, `us`, `usa`, `united`, `states`, `based`, `in`, `role`, `relocation`, `package`, `products`. Replace the geography with your own. Note that `in` and `products` are aggressive, and `products` will strip a substantive word out of a title like "GTM Emerging Products". Prune before you reuse.

`{{ALIAS_TABLE}}` is inherently hand-maintained and that is fine. Expect it to grow every time you ingest a new source.

## Where the source implementation stops short

The refusal itself is implemented. `ingest_platform.py:491` declines to match when more than one candidate survives tier 3, which is the hard part and the right call.

What is missing is the record of it. `match_status` takes exactly three values, verified across all 134 rows of `adjudication/platform_match.csv`: `net_new` on 77, `overlap` on 56, `opportunity_or_non_census` on 1. There is no ambiguous status. So a record refused at line 491 falls through to line 506 and is emitted as `net_new`, indistinguishable from a record that genuinely had no counterpart.

The refusal is therefore invisible downstream. Nobody reading the 298-row full census can tell which rows are new and which are unresolved, and the count carries no "of which K unresolved" caveat. That is why the template above adds a fourth status. Add it before you reuse this.

## What breaks if you skip it

Two failures, in opposite directions, and you will usually have both at once. Match too loosely and you destroy real records: two distinct openings at one company become one, and the deleted one leaves no trace. Match too strictly and you double-count: the same role, spelled two ways across two trackers, becomes two applications. The source study's own dedup step is stricter than its matching step, so "GTM Engineer Remote" and "GTM Engineer" from the same company survive as two platform rows even though the alias table collapses them for matching. Pick one normalization and use it in both places.
