<!-- kit-meta
file: 02-current.md
tier: 2 (volatile)
created: 2026-08-29 13:37 ET
updated: 2026-08-29 13:37 ET
review-by: 2026-09-29
sources: [S1] [S2] [S3] [S4] [S5] [S6]
-->

# Current state

Everything here is assumed stale until the meta block says otherwise. Delete and regenerate freely.

## Headline numbers, as of the reconciled audit [S1]

| Metric | Value | Note |
|---|---|---|
| Confirmed unique applications | 247 | all status Confirmed |
| High-confidence rows | 244 | 3 Medium |
| Increment over prior Gmail floor | 84 | 163 to 247 |
| Applied companies interviewed | 11 | |
| Application to interview rate | 4.45 percent | 11 of 247 |
| Census completeness | 88 to 93 percent | estimated, stop conditions unmet |
| Distinct normalized companies | 229 | |
| Distinct non-empty title variants | 133 | |

## Role lanes, 247 applications [S1 Role Analytics]

| Lane | n |
|---|---|
| Explicit GTM engineering | 108 |
| Sales / solutions engineering | 30 |
| RevOps / GTM ops / strategy | 30 |
| Growth / demand / marketing | 23 |
| Sales / BD / partnerships | 22 |
| Unspecified / unresolved | 15 |
| Product / AI / technical adjacent | 15 |
| Other | 4 |

GTM title modifiers within the 108: Plain GTM Engineer 78, Founding/senior/lead 10, Growth/marketing 6, Systems/operations 6, Sales/pre-sales 4, AI/product/vertical 4.

## Monthly distribution, two versions

Both are in play and they disagree. The paper must show one and explain the other.

Prior 212-row ledger, By_Month [S2]: 2025-08 1, 2025-09 0, 2025-10 0, 2025-11 2, 2025-12 3, 2026-01 9, 2026-02 11, 2026-03 11, 2026-04 27, 2026-05 20, 2026-06 62, 2026-07 58, 2026-08 8.

Reconciled 247-row ledger, parsed from Submitted Date where parseable (154 of 247 rows parse cleanly; the remainder carry relative or unknown stamps and are excluded from this cut): 2025-11 1, 2025-12 2, 2026-01 9, 2026-02 9, 2026-03 17, 2026-04 27, 2026-05 23, 2026-06 29, 2026-07 33, 2026-08 4. [computed from S1 Master Ledger, 2026-08-29]

The shapes differ most in June and July. Until the relative dates are resolved to calendar dates, neither curve is publishable as-is without a stated caveat.

## Opportunity attribution register [S1]

Seven non-application opportunities identified. Three converted to paid work: Mixmax, Kivira Health, Mercor. BCOFA did not convert. Weave, TrueBuilt, and Luzmo produced no engagement. None of these count in the 247.

Interviews outside the application census: Mixmax (relationship-led, 2 interactions), Mercor (matching pathway, 4 conversations), Weave / WorkWeave (recruiter-initiated, 1 screen).

The 11 in-census interviews: Fullsteam, Glytec, Beautiful.ai, Orchestry Software, PhrasIQ, Every (Every.to), Pearl, The Hog, confidential client via HartleyCo, Hologram, Great Question.

## Open threads

| Thread | Status | Next action | Since |
|---|---|---|---|
| LinkedIn Applied pages 11 and beyond | Unknown whether they exist | Export LinkedIn Job Applications.csv via Settings, Data privacy, Get a copy of your data | [S2] |
| Full Ladders Applied List | Not exported, only 3 Apply4Me rows captured | Export the Ladders applied list, not just Gmail receipts | [S2] |
| YC Work at a Startup applied roles | No Gmail artifacts found | Inspect the YC dashboard directly | [S2] |
| Talentpluto underlying employers | Two 2026-07-12 submissions unresolved | Check the Talentpluto submission dashboard | [S1] |
| Jobgether intermediary row | LinkedIn shows applied, employer unknown | Pull the Jobgether tracker | [S1] |
| AnyInt AI, Founding Sales | Recruiter references an application, no receipt | Find the LinkedIn applied row or ATS receipt | [S1] |
| LinkedIn row with no company name | Cannot form a valid dedupe key | Recover the job URL from the archive | [S3 row 80] |
| Dedupe key missing cycle component | Two duplicate keys in the ledger | Decide: fix key or document the exception | [S1] |
| Window disagreement, 08-25 vs 08-27 | Unresolved | Pick one and restate in Methods | [S1] [S2] |
| 212 to 163 reconciliation | Undocumented | Write the note before publication | [S1] [S2] |

## Paper status

Nothing drafted yet. Structure agreed: Abstract, Introduction, Methods, Results, Discussion, Conclusion, with figures. [S6]

Figures under consideration, none built:
- Applications per month, exact-date subset only, with the approximate-date count annotated
- Source reconciliation waterfall, raw rows to net unique
- Role lane distribution
- Evidence tier composition of the census
- Funnel: applications, interviews, offers, with the opportunity register shown as a separate parallel track

## Derivatives planned

Substack post and LinkedIn post, both downstream of the paper. Not started. [S6]

## Changelog

- 2026-08-29 13:37 ET: created from [S1] [S2] [S3] [S4] [S5] [S6].
