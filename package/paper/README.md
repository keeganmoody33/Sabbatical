# paper/

**Keegan drafts here. Cursor checks. Cursor does not draft.**

Target structure: Abstract, Introduction, Methods, Results, Discussion, Conclusion, with figures. Derivatives: a Substack post and a LinkedIn post.

One file per section: `01-abstract.md`, `02-introduction.md`, `03-methods.md`, `04-results.md`, `05-discussion.md`, `06-conclusion.md`.

## The claims block

**Every section file ends with a claims block.** This is the whole mechanism. It keeps the prose clean and makes verification mechanical instead of interpretive.

```
<!-- claims
| # | quantity as written | value | source | tier |
|---|---|---|---|---|
| 1 | applications in the census | 325 | knowledge/08-census-ledger.md | measured |
| 2 | distinct companies | 298 | data/full-application-register.csv, verified log 051 A1 | measured |
| 3 | Jobright rows sent by agent | 31 of 40 | raw/jobright_applications_log.csv, Application Method | measured |
| 4 | Beautiful.ai discovery source | Jobright, hedged | logs/retrieval-log-042.md, 051 section 8 | memory |
| 5 | Gmail stratum completeness | not estimated | none | unknown |
-->
```

`tier` is one of **`measured`**, **`estimated`**, **`memory`**, **`unknown`**. Nothing else.

Rows tagged `estimated` must carry the method and the direction of likely bias in the source column. Rows tagged `memory` must name the log that recorded the recall.

## What Cursor does with it

Three passes per section, all mechanical.

1. **Resolve.** Every source named in the claims block must exist and must actually contain that value.
2. **Sweep.** Grep the prose for every numeral and every proper noun. **Anything not in the claims block is a finding.** This is the pass that catches numbers which drifted in while writing.
3. **Style.** The rules below.

Cursor writes findings to a numbered log. **It does not edit prose.**

## Style rules Cursor enforces

- **No dashes as punctuation.** Not em, not en, not spaced hyphens.
- **No census total stated outside `knowledge/08-census-ledger.md`.** Prose cites the ledger.
- A quantity tagged `estimated` or `unknown` must be visibly hedged in the prose too. A bare figure carrying an `estimated` tag is a finding.
- No triumph narrative unless the claims block supports it.
- Real company names get flagged for a human decision, per Rule 5 in `knowledge/04-engagements.md`. Never removed by an agent.
- First person, specific, plain.

## Figures

Write the caption before generating anything. It states the chart, the underlying slice, and the caveat.

Standing caveat for any time series: **35 of 321 register rows carry no submission date and 3 are `evidence_bound`.** A monthly curve is drawn on 283 exact-dated rows and must say so.

## What is drafted

Nothing yet.
