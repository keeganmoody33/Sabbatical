<!-- kit-meta
file: retrieval-log-052.md
created: 2026-08-30
source: VERIFY.md Part A against the 2026-08-30 care-package files in this session's upload directory, plus the Cursor Sabbatical working tree
method: independent CSV parser; fuzzy company matcher built for this pass; md5; line-level QUERY-MANIFEST diff; citations by file and line
-->

# Retrieval log 052

Adversarial audit. VERIFY.md Part A. No census total is changed. Ledger and MANIFEST edits are proposed at the end, not applied.

Two trees were in scope:

- **Package:** files dropped 2026-08-30 (`full-application-register.csv`, `08-census-ledger.md`, logs 001 to 051 except 029, `VERIFY.md`, `MANIFEST.md`, `AGENTS.md`).
- **This working tree:** `keeganmoody33/Sabbatical` on `cursor/pressure-test-interviews-b55f`, which already holds `artifacts/gmail/retrieval-log-001.md` through `036.md` plus a `029` that the package does not.

They are not the same corpus. Shared log numbers do not mean shared files.

## 1. What I checked and how

| id | claim | method (deliberately not the original query) |
|---|---|---|
| A1 | 321 / 298 / 234 / 87 / 35 / tiers A 291 B 23 C 7 / zero duplicate keys | Python `csv.DictReader` on `full-application-register_4dc9.csv`. Duplicate key = `re.sub(r'[^a-z0-9]+','', company.lower())` + same for role + raw `applied_date`. Outcome counts taken from the same parse. |
| A2 | Jobright join 21 / 15 / 4; Axon one row; Autodesk MavenAI Vanco absent; two blank dates | Own matcher: exact normalized name, then `SequenceMatcher` / substring, **no** hardcoded `tekioncorp→tekion` map. Then a **strict** recount that forbids short-substring hits (`Pin` inside `Pindrop`, `Vi` inside `VitalSource`). Axon / Autodesk / Maven / Vanco searched as case-insensitive contains across register, `gmail-stratum-roster.csv`, `linkedin-applications-in-window.csv`. |
| A3 | 0 interviews on 43 Jobright-tied rows, 18 / 16 / 9 | Strict company match (exact or alias/substr of full tokens only). Spot check: read log 008, 009, 012 rows for Trase, Clay, Pindrop, FOSSA, Nebius. Did not grep the word `interview` as a proxy for the outcome column. |
| A4 | ten (log 051) / eleven (VERIFY) 2026-05-20 vs 05-21 rows | Listed every register date at each named company. No mailbox or Jobright UI was opened. |
| A5 | extraction md5; A3 retirement; QUERY-MANIFEST superset; claude_ collapse | `hashlib.md5` of every `extraction*` file in the drop and `prompts/extraction.md` in this tree. Read `05-codebook-amendments-r1.md` A3 and `03-codebook_633e.md` vocab. Diffed `QUERY-MANIFEST_2db1.md` (57 lines) against `QUERY-MANIFEST_e839.md` (78 lines). |
| A6 | dangling file and id refs | Searched `logs 026 to 029`, `026, 027, 028, 029`, `ENG-B`, `Q12`, `LI-001`–`LI-105`, `S1`–`S6`. Did not use the brittle `log 029` / `log-029` / `logs 029` triple. |

## 2. Confirmed

| claim | where it lives | check |
|---|---|---|
| 321 data rows, 298 distinct `company`, 234 `gmail/ATS`, 87 `LinkedIn`, 35 blank `applied_date` | `08-census-ledger.md` line 11 and line 15; VERIFY A1 | Parser: 321, 298, 234, 87, 35 |
| Tiers A 291, B 23, C 7 | VERIFY A1 | Parser |
| Zero exact duplicate keys on normalized company + role + date | VERIFY A1 | Parser, 0 groups |
| Jobright company-and-date matches = 21 | log 051 join table | Own matcher: 21 |
| Axon: exactly one register row, `Manager, Go-to-Market Readiness`, 2025-08-04 | log 051 section 2 | One hit, parser row 39 |
| Autodesk, MavenAI, Vanco absent from register, Gmail roster, LinkedIn in-window file, including `Maven AI` / `Maven` / `Vanco Payment Solutions` / `Autodesk Inc` | log 051 section 3 | Zero hits in all three files |
| `Jobright.ai, Product Manager (Early Career)` blank `applied_date`; `OpenObserve, Growth Marketer` blank `applied_date` | log 051 section 1 | Both blank; rejection dates 2026-03-31 and 2026-08-24 already present |
| Tekion Corp and CoLab match without the original two-entry alias map | log 051 method note | Substring on full names: Tekion Corp → Tekion; CoLab → CoLab Software |
| extraction copies md5 `dc6a5f19e963b824927ef39467a233fb` | MANIFEST collision 1 | Four drop files, 2889 bytes each, that hash |
| A3 in `05-codebook-amendments-r1.md` does retire `newsletter_community` | MANIFEST collision 2 | Amendments file lines 59–85; `03-codebook_633e.md` line 122 |
| `linkedin-applications-in-window.csv` is LI-001 through LI-105, 105 unique | log 037 | Parser |
| ENG-A through ENG-E are populated in `04-engagements.md` | codebook Table 4 | Table at line 77 |
| Duplicate drop copies of logs 001–021 are byte-identical pairs | MANIFEST collision 4 | 21 pairs, one md5 per number |
| Onit and ServiceTrade are 2026-05-21 in both Jobright and the register | log 051 section 4 | Parser |

## 3. Refuted

| claim | file:line | evidence |
|---|---|---|
| Ledger outcome split "Interview scheduled or held 8" and "Rejected after interview 7" | `08-census-ledger.md` lines 60–61 | Same CSV as A1: `interview_scheduled` = **7**, `rejected_after_interview` = **8**. The 15 interview-ish rows exist; the labels are swapped. Line 15's 321/298/234/87/35 self-audit does not cover this table. |
| Log 051 "Ten rows" dated 2026-05-20 vs register 2026-05-21 | `retrieval-log-051.md` line 62 | The name list on line 64 is **eleven** companies. VERIFY A4 also says eleven. The −1 day pattern holds for the matching title at Nebius, DBeaver, FOSSA cycle 2, TRACTIAN Sales Engineer Automation, Applied Systems, Pindrop GTM Systems, CoLab, VitalSource AI Enablement, Telnyx, Deepgram, NiCE. TRACTIAN also has a 2026-05-19 Hubspot row (offset the other way). FOSSA also has 2026-04-22. |
| That −1 day cluster is "the agent queued a batch late on 05-20 and the ATS receipts landed 05-21" | log 051 lines 68–70 | Interpretation. No artifact in this pass discriminates queue time from timezone from tracker-recorded intent. Competing explanations in VERIFY A4 remain open. |
| `AGENTS.md`: log 029 "does not exist and is referenced nowhere" | `AGENTS.md` line 93 | Same false claim VERIFY already caught in MANIFEST. `04-engagements.md` lines 6, 16, 38, 79 still cite it. MANIFEST was corrected; AGENTS was not. |
| Log 051 "Census 321 to 325" as a completed ledger move | log 051 lines 58, 101, 175 | `08-census-ledger.md` header line 11 and changelog still end at **321**. Gap 6 (lines 78–105) still describes Jobright as missing. The 325 is a log instruction, not a ledger fact. |
| `05-codebook-amendments-r1.md` status PENDING APPROVAL vs `03-codebook_633e.md` changelog "rev 2, amendments A1 to A4 applied" | amendments line 5; codebook changelog | One file says not in force; the other says applied. Both are in the drop. |
| QUERY-MANIFEST `_2` is "strictly a superset" of the discarded file | MANIFEST collision 3 | The **query table** in `QUERY-MANIFEST_e839.md` is newer (Q7 done, Q7b added). The discarded 57-line file still holds progress narrative that the 78-line file does not copy: Q7 page-1 token, Hypergen interview not on the Interviews sheet, Q2b named additions (Virtru, Lumenalta, Celonis, New Relic, Crossing Hurdles / Montauk, Ambrook Partnerships Lead), 994-thread running total. Superset of the table, not of the document. |
| This working tree's logs 001–036 are the same objects as the package logs 001–036 | user instruction to disregard already-ingested logs | **0 of 35 overlapping numbers are byte-identical.** Workspace 022–028 and 030–036 are a different harvest (lecturesfrom / Freeze 3). Package 022+ continues the original Gmail sweep. Workspace **has** `artifacts/gmail/retrieval-log-029.md` (33@lecturesfrom identity check). The package's missing 029 is the ENG-B evidence file. Same number, different documents. |
| `codebook.md` was dropped and no other file depends on it | MANIFEST collision 2 | This working tree still has `codebook.md` and `coding/README-coder.md` lines 7 and 33 still point at it. Drop still contains `codebook_e871.md` (9.9K class) **and** `03-codebook_c66f.md`, which still lists `newsletter_community`. `prompts/README-coder.md` in the drop still says `codebook.md`. |
| Jobright-tied rows: 0 interviews, 43 rows, 9 `unknown` | log 051 line 121 | Strict match: **43** rows, 18 `rejected_no_interview`, 16 `no_response`, **9 `unknown`, 0 interview outcomes.** Holds **only** if `Pin` is not matched to `Pindrop`. A substring matcher attaches Pin (`rejected_after_interview`, logs 024–025) and `Vi` (VitalSource). Beautiful.ai `rejected_after_interview` is in the register (row 81) and is **not** a Jobright tracker company, which is consistent with section 8. |
| `02-current.md` "Census status: no total may be stated" together with `AGENTS.md` "Census stands at 325" | `02-current.md` line 18; `AGENTS.md` line 98 | Direct contradiction. Authority order says the ledger wins; the ledger still says 321. |
| `02-current.md` Gmail Q3b/Q6/Q9/Q10 still pending | `02-current.md` line 24 | Package log 050 (cited by the ledger changelog) claims Q3b and Q6 closed. Not re-derived here beyond reading those sentences. |

Spot checks for A3 (named companies, against the log in `source`, not against the outcome column):

- **Nebius** log 009: "Thank you for applying" 2026-05-21. No interview subject. Outcome `rejected_no_interview` is at least not contradicted by that row.
- **FOSSA** log 009: receipt 2026-04-22, decline 2026-05-20, second receipt 2026-05-21. No interview subject. Matches two-cycle coding.
- **Pindrop** log 008: thank-you 2026-05-21; decline 2026-05-27 for GTM Systems Platform Specialist. Consistent with `rejected_no_interview`.
- **Trase** log 009: thank-you 2026-04-27; log 012 has a later Healthcare GTM Engineer row. No interview subject in those hits.
- **Clay** log 012: thanks for applying 2026-06-24; declined 2026-06-25. Consistent with `rejected_no_interview`.

These five do not prove the other 38 outcomes. They also do not use Gmail bodies. Completeness of the outcome column remains unverified (Part B2).

## 4. Could not check

| item | missing file |
|---|---|
| B1. Name [S1]'s five Jobright-only rows; choose among log 051's three explanations | `raw/job_search_reconciled_audit.xlsx` |
| B2. Mailbox miss rate for the Gmail stratum | Gmail export / live mailbox sample of ≥30 threads |
| B3. Re-derive 105 in-window and 18 overlaps from LinkedIn | `Job Applications.csv` (S3b). This tree has pages 1–10 scrape (`artifacts/platform/linkedin_applied_jobs_pages_1_to_10.csv`), not the data-download |
| B4. Re-derive 34 meetings and 277 events | Calendar export. This tree has a 338-event keeganmoody33 CSV, which is a **different count** than 277 and was not used as a substitute |
| B5. Recover package log 029 | Original Claude chat / local export. Workspace `retrieval-log-029.md` is not that file |
| A5 "re-derive md5 from the originals" as three Project filenames `extraction.md` / `_2` / `_3` | Drop has four hashed copies plus this tree's different `prompts/extraction.md` (md5 `892251a68c7f5f1485bf6d92a3609fdc`). Cannot see Claude Project filenames |
| A5 "no two claude_ files collapsed onto the same name" inside the Project | Prefixes already stripped in the drop; 001–021 exist as identical pairs with different upload suffixes, which is this chat's packaging, not proof about the Project |
| Whether tracker "Applied by Agent" satisfies counting rule 6 | Rule is explicitly unresolved in log 051 section 7 |

## 5. New findings

1. **Two log sequences share numbers.** Do not discard package 001–036 as "already ingested." This tree's 001–021 are redacted/hashed descendants of a similar sweep but are not identical. From 022 onward they diverge in role (lecturesfrom vs continued personal Gmail).
2. **This tree's application census (298 rows, 273 companies) is not the package's 321 rows / 298 companies.** Different grain, different files, different freeze. See the reconciliation table in the 2026-08-30 chat. Neither number was updated in this log.
3. **Pin / Pindrop / Vi false joins.** Any Jobright join that treats `pin` as a substring of `pindrop` will manufacture an interview in the Jobright company set. Log 051's zero-interview claim depends on not doing that.
4. **OpenObserve / Jobright.ai Early Career** are dated in this tree's `applications__full_census.csv` using the **rejection** date (`2026-08-24`, `2026-03-31`). The package register leaves `applied_date` blank and keeps the rejection on `outcome_date`. Log 051's precision upgrade to the tracker send-date is a different decision than the one already coded here.
5. **`Q12` is cited** in logs 028, 033, 034, 035, 037–039, 043–047, 049, 050, `02-current.md`, `04-engagements.md`, `06-method-retrospective.md`, and is **absent** from both QUERY-MANIFEST files in the drop.
6. **`linkedin_easy_apply`** is used on all 87 LinkedIn register rows and all 105 in-window rows. `03-codebook_633e.md` line 128 says that value is not in the vocabulary.
7. Workspace `knowledge/03-codebook.md` is still rev 1 (`newsletter_community` present). Package `03-codebook_633e.md` is rev 2. Independent coding against this tree would not match a coder handed the package schema.

## 6. Open

1. Human decision on 321 vs 325. Log 051 told the ledger to move. The ledger did not. VERIFY forbids this audit from moving it.
2. Human decision on the swapped 7/8 interview outcome counts.
3. Fix `AGENTS.md` line 93 (false 029 claim) without touching logs.
4. Point `README-coder.md` at `knowledge/03-codebook.md` (already flagged in MANIFEST).
5. Do not overlay package logs 037–051 onto this tree until the 001–036 identity question is decided.
6. Part B queue: S1, Gmail export, LinkedIn data-download, calendar export, package log 029.
7. Rule 6 (agent-applied without recall) still unanswered.

## Proposed edits (not applied)

To `knowledge/08-census-ledger.md`:

- Correct the outcome table to match the CSV, or say why the CSV is wrong.
- Either apply log 051's +4 with a changelog row, or record 325 as a pending delta. Do not leave header 321 and log 051 325 both speaking.
- Strike or rewrite Gap 6 if stop condition 5 is accepted as met.

To `MANIFEST.md` / `AGENTS.md`:

- Delete "referenced nowhere" from `AGENTS.md` line 93. Keep "does not exist" for the package sequence.
- Note that QUERY-MANIFEST `_2` is a superset of the **query table**, not of the discarded file's progress section.
- Note Q12 has no query-manifest row.

No census total is stated in this log except as a quotation of files already in the package.
