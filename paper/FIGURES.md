# Figures

`knowledge/instructions.md` requires that a figure be specified as chart, underlying slice, and
caption caveat **before** anything is generated. This file is those specifications.

Nothing is rendered yet. This environment has no plotting library and the repository has no
dependencies, both deliberately, so the paper ships with tables and the figures are specified for a
later pass. Each spec below names the view it reads, so any of them can be built without touching
the pipeline.

No dashes are used as punctuation in this file.

## F1. The funnel

**Chart.** Horizontal bar, four bars, ordered by size. Not a funnel diagram, because the stages do
not share a denominator and a tapering shape would imply they do.

**Slice.** `views/funnel_by_evidence_class.csv` and `adjudication/LATENCY.md`. Bars: 221
applications, 196 with an exact-dated receipt, 100 with any response, 13 interviewed.

**Caption caveat, required.** "Three denominators, not one. 221 is the census. 196 is the subset
with an exact-dated receipt, the only rows where a response time exists. The 13 interviews are
13/221, not 13/100."

## F2. Origin coverage against outcome observability

**Chart.** Grouped bar, two series per origin value: rows, and rows with an observable outcome. Full
census stratum.

**Slice.** `views/origin_coverage.csv`, `stratum = full_census_298`, `field = discovery_source`.

**Caption caveat, required.** "The LinkedIn bar is 71 rows and 0 observable outcomes. Origin is
known almost exactly where outcome is not, which is why no channel conversion figure is published."

**Why this is the paper's lead figure.** It is the only chart here that shows an absence rather than
a quantity, and the absence is the finding.

## F3. Interview rate by role lane, with intervals

**Chart.** Dot plot, one row per lane, ordered by n. Point at the rate, horizontal line for the
Wilson 95 percent interval. Never a bar chart: bars imply the point estimate is the quantity, and
here the interval is.

**Slice.** `views/funnel_by_role_lane.csv`, all eight lanes including the five at zero.

**Caption caveat, required.** "Thirteen interviews across eight lanes. The zero lanes have upper
bounds from 0.12 to 0.32, so zero here is not evidence those lanes cannot work. Descriptive only:
the applicant chose which roles to apply to."

## F4. Applications per month

**Chart.** Column chart, one column per month across the fifteen-month window, with the two zero
months rendered as visible zero-height columns rather than gaps.

**Slice.** `views/monthly_trend.csv`, `n_applications_exact_date`.

**Caption caveat, required.** "Exact-dated rows only, n = 195. Twenty-six census rows carry a
relative or evidence-bound date and are not on this chart. Zero in 2025-09 and 2025-10 is a count of
exact-dated rows, not a claim that nothing happened."

**Do not** overlay interviews as a second series on the same axis. Thirteen points against columns
reaching 33 renders as a flat line at the baseline and reads as "no interviews".

## F5. Response latency distribution

**Chart.** Two overlaid histograms or a paired box plot, substantive against any, on days to first
response. Log or clipped x axis with the 140-day outlier annotated rather than dropped.

**Slice.** `adjudication/latency__by_application.csv`, columns `days_to_response_strict` and
`days_to_response_broad`.

**Caption caveat, required.** "Responders only, 79 and 100 of 196. The 96 applications that drew no
response are not in this distribution and are the larger group. Both distributions are right skewed,
so quote the median, 7 days substantive and 5.5 days any."

## F6. Source reconciliation waterfall

**Chart.** Waterfall from raw rows to net unique.

**Slice.** `adjudication/platform_match.csv` and `adjudication/FREEZE-2.md`. Steps: Freeze 1 census
221, platform rows considered 134, overlap removed 56, net-new added 77, full census 298.

**Caption caveat, required.** "One ambiguous match was held out of the census rather than counted,
on the rule that an omitted row is recoverable and an inflated census is not."

## Figures deliberately not specified

- **Any chart of interview rate by origination channel.** There is no such analysis. Drawing the
  axis at all would imply one exists.
- **Any chart of response time by ATS.** Four of thirteen systems clear n = 5. A ranking of four
  cells beside nine absences is a chart of the suppression rule.
- **A conversion funnel with a single tapering denominator.** See F1.
