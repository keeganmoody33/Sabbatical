# Citations

Two classes of source stay distinct. This freeze (Gmail and Calendar extracts, platform CSVs, overlay, retrieval logs on this tree) can support findings. Foreign assemblies (absent prior-audit workbooks, the care-package ledger) are cited only to refuse them as this freeze's census.

Published copy never includes raw or hashed provider IDs (`gth_`, `cal_`, `tok_`, `eml_`). Those pointers belong in the working record and in freeze files.

## In-text keys

| key | what it points at |
|---|---|
| [census] | `adjudication/applications__full_census.csv` |
| [adj] | `adjudication/applications__adjudicated.csv` (Freeze 1 221) |
| [events] | `coding/cursor/events__cursor.csv` (interview set derived here) |
| [metrics] | `adjudication/derive_metrics.py` |
| [kappa] | `adjudication/PRE-ADJUDICATION.md` |
| [F2] | `adjudication/FREEZE-2.md` |
| [F3] | `adjudication/FREEZE-3.md` |
| [F4] | `adjudication/FREEZE-4.md` |
| [ORIGINS] | `adjudication/ORIGINS.md`, `adjudication/origins__subject_confirmed.csv` |
| [delta] | `adjudication/package_vs_census_delta.csv` |
| [Q] | `QUERY-MANIFEST.md` |
| [log N] | `logs/retrieval-log-NNN.md` |
| [codebook] | `knowledge/03-codebook.md` rev 1 |
| [S1] | Absent `job_search_reconciled_audit.xlsx`. Historical. Not this census. |
| [S2] | Absent `Keegan_Moody_Job_Applications_Audit_2025-08_to_2026-08.xlsx`. Historical. |
| [pkg] | `package/` sidecar. Different assembly. Do not print its ledger totals as this freeze. |

## Where each Results integer lives

| integer | source |
|---|---|
| 298 applications | [census], register = application |
| 273 companies | distinct `company_canonical` on those 298 |
| 221 | [adj] |
| 77 net-new | [F2] |
| 14 interviewed | [events] ∩ [census]; [metrics] |
| 14/221, 14/298, 14/220 | same, Freeze 1 / full / employer_artifact |
| 0 coded offers | `terminal_outcome` on [census]; Q11 in [log 059] |
| 73 / 6 / 18 / 124 | [adj] `terminal_outcome` |
| role_lane 86 … 8 | [adj]; kappa [kappa] |
| GTM 113 on 298 | [census]; no second kappa |
| 195 / 26 exact | [adj] `date_precision` |
| 201 / 97 exact | [census]; 71 `relative_display` |
| 33 in 2026-07 | exact-date monthly on [census] and [adj] |
| 13 companies, 25 extra rows | [census] |
| 6 Mercor marketplace rows | [census], company Mercor |

## Retired and foreign figures (refuse as findings)

| figure | status |
|---|---|
| 247 applications | [S1], absent workbook, retired |
| 11 interviews | [S1]/[S2], retired numerator |
| 4.45 percent | 11/247, retired |
| 321 | [pkg] on-disk register row count |
| 325 | [pkg] ledger after a Jobright addendum this freeze already contains |
| 101 `no_response` of 200 | [pkg] codebook rev 2 / A2. Not applied here |
| 51 of 325 unlaned | [pkg]. This freeze unspecified is 35/221 |

Naive 325 minus 298 equals 27 is not 27 missing applications. Arithmetic and named rows: [delta], [log 059] C1.

## Retrieval logs this manuscript leans on

| log | use |
|---|---|
| 052 | VERIFY Part A |
| 053 | care-package ingest completion |
| 054 | LinkedIn messages unpacking |
| 055 | pressure-test restatement |
| 056, 057 | overlay and confirmation |
| 058 | Doug predates AICRO; freeze headlines |
| 059 | red-team C1 through C9; Q11 |

## Punch list on current drafts

Scanned `paper/METHODS.md`, `paper/results-narrative.md`, `paper/discussion.md`, `paper/conclusion.md`, `paper/introduction.md`, `paper/title-and-abstract.md`, `paper/figures.md`.

| sentence risk | disposition |
|---|---|
| 14/298 printed as 4.70 percent in the abstract | Not used. Abstract prints 14/298. |
| Retired 4.45 percent | Discussion names it retired only. Not in abstract. |
| Package 321/325 | Cited in citations and Results ledger as a different assembly. Not a finding. |
| Completeness percent | Not printed. |
| Combined conversation count as a rate | Not printed. |
| "None of the money is in 298" | Not used. Mercor marketplace rows flagged. |
| Mixmax, Mercor, Mobb, Kivira.health, BCOFA in working copy | Flagged for naming pass in Results, Discussion, Fig 6, Acknowledgments, abstract. |
| jobmail.io stored `rejected_no_interview` | Disclosed in Results and DEFECTS. Not recoded. |
| Hashed IDs in body prose | Drafts cite files, not `gth_` strings, except Methods describing the hash scheme. |

Unsupported on purpose: any later page of LinkedIn, Ladders, YC, personal Q11, and the twelve held LinkedIn rows. Those are limitations, not findings.
