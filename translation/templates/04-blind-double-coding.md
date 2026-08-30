# Template 4. Blind double-coding with named adjudication

**What this proves you can do:** tell the difference between a real pattern in your data and an artifact of whoever categorized it, and prove the difference with a number.

**Extracted from:** `knowledge/protocol.md:31-46`, `adjudication/compare_coders.py`, `adjudication/adjudicate.py`, `adjudication/ADJUDICATION.md`.

**One-line form:** Have `{{N}}` independent raters classify `{{FROZEN_CORPUS}}` using `{{FROZEN_CODEBOOK}}`, bounded by `{{BLINDNESS_RULE}}`, and output `{{AGREEMENT_STATISTIC}}` plus `{{NAMED_ADJUDICATION_DECISIONS}}`.

---

## The problem it solves

You ask a model to sort 200 records into eight categories. It does. The output looks authoritative because it is consistent.

Consistency is not accuracy. A single classifier is consistent with itself by construction, so its consistency tells you nothing. If you then find that category X is 20 points more common in one slice than another, you cannot tell whether that is a fact about the world or a habit of the classifier.

Run two independent classifiers and the question becomes answerable. Where they agree, the signal is probably in the data. Where they disagree, the signal was in the classifier.

---

## The template

```
DESIGN: {{N}} independent raters classify the same records using the same
codebook, without seeing each other's output.

FOUR REQUIREMENTS, IN THIS ORDER. Each has its own failure mode.

1. FREEZE THE CODEBOOK FIRST.
   No vocabulary changes after rater 1 begins. If you add a category
   mid-run, earlier rows were coded under a different instrument and the
   agreement statistic is meaningless.

2. FREEZE THE CORPUS.
   All raters receive an identical, enumerated, dated input set.
   A rater who sees more records is not a second rating. It is a
   different study.

3. BLIND.
   No rater sees another's rows before all runs finish. If any output is
   read first, independence is destroyed and the statistic is invalid.
   This includes you. Do not peek and then run the second rater.

4. ADJUDICATE AFTER, NOT DURING.
   Resolve disagreements in a single named pass, AFTER the raw agreement
   rate has been computed and recorded. Publish the pre-adjudication rate,
   not just the clean post-adjudication result.

WHAT TO REPORT:
  - Percent agreement and Cohen's kappa on {{PRIMARY_CATEGORICAL_FIELD}},
    computed on the subset both raters produced
  - Percent agreement on the binary include or exclude decision
  - A disagreement inventory: every differing row, the field, and both values
  - Every adjudication decision by name, with the rule applied

THE CAVEAT YOU MUST STATE:
  Kappa computed on the intersection measures agreement between raters
  CONDITIONAL on their already agreeing that a record exists. Records only
  one rater produced are excluded from that statistic by construction.
  Report those counts separately and prominently. They are usually the
  disagreements that matter most.

  In the source study: intersection 211, only-rater-A 17, only-rater-B 20.
  The published kappa of 0.9510 describes the 211 and says nothing about
  the 37.

ADJUDICATION RULES:
  - Every decision gets a written reason, not a preference.
  - Reasons must be rules that would apply to the next case:
    "{{EXAMPLE_ADJUDICATION_RULE}}"
  - When one rater flagged its own low confidence, weight that.
  - Record the decision even when both raters were wrong.
```

---

## How to read the numbers

The source study reports two kappas and they mean very different things (`adjudication/PRE-ADJUDICATION.md`):

| Statistic | Value | What it says |
|---|---|---|
| `role_lane` percent agreement | 0.9621 | Raters picked the same category 96 percent of the time |
| `role_lane` kappa | 0.9510 | Still 95 percent after subtracting agreement expected by chance. Strong. The category assignments are real. |
| include percent agreement | 0.9905 | Raters agreed on 99 percent of include or exclude calls |
| include kappa | 0.7452 | Only 75 percent after chance correction |

That last row is the interesting one, and it is why kappa exists. Percent agreement of 0.9905 looks flawless. But nearly every record was an include, so two raters guessing "include" every time would agree almost as often. Kappa strips that out, and the honest number drops 24 points, on the basis of just two disagreements: The Hog and BX Studio.

**The general rule:** when one category dominates, percent agreement is close to meaningless and kappa is the number to publish. Publish both, so a reader can see the gap.

## Where the source implementation falls short

Worth knowing before you copy it, because these are easy to avoid in your own version:

- The agreement figures printed in `adjudication/ADJUDICATION.md` are hardcoded string literals in `adjudicate.py:130-133`. The script never recomputes them. They happen to be correct today. Compute yours at write time.
- The eight alias merges are 15 hand-typed match keys in `adjudicate.py:48-69`, not a rule. Any retitling breaks them with an uncaught error.
- `adjudicate.py:88` resolves every agreed row by taking rater B's version unconditionally. In the source study rater B had a constant where rater A had observations, so one field was silently flattened across the whole census. If your raters disagree on a field you are not measuring agreement on, decide the tie-break per field, not per row.

## What breaks if you skip it

You publish a distribution and cannot defend it. The source study is explicit about this, and it is the cleanest statement of the principle anywhere in the repository:

> "Until independent coders agree on lane assignment, that gap cannot be attributed to behavior rather than coding." (`knowledge/protocol.md:48`)
