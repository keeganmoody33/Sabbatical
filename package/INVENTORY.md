# Claude care package inventory

Dropped 2026-08-30 into this chat. Inventoried 2026-08-30. This file is the inventory. It is not a census update.

**This working tree's defended numbers stay 298 applications and 14 interviewed applications.** Package ledgers are a different assembly. They are not adopted by existing.

Upload directory: 119 files, 86 unique by md5. 33 extra copies. Nothing in the drop failed to open. All files are markdown or CSV.

## What the drop does not contain

These holes from the ingest plan remain empty. They were named in the package and are still absent here.

| named hole | status in this drop |
|---|---|
| LinkedIn applied-list UI pages after 10 | absent |
| Easy Apply versus external ATS labels on the applied-list UI | absent. The 105-row extract sets `linkedin_easy_apply` on every row, a value this tree's codebook does not include |
| Ladders full list / `LADDERS.png` [S5] | absent |
| YC Work at a Startup dashboard | absent |
| Prior workbooks [S1] and [S2] xlsx | absent. Log 046 stopped on [S1] |
| LinkedIn data download `Job Applications.csv` / `messages.csv` | Raw CSVs still absent. The 105-row file is a Claude extract of that download, not the download. A Claude analysis of `messages.csv` arrived separately 2026-08-30 (`artifacts/linkedin/job-threads-analysis-2025-06-to-2026-08.md`). 54 job threads matched, census unchanged |
| Package `retrieval-log-029.md` (ENG-B / Mobb evidence) | absent. This tree's `artifacts/gmail/retrieval-log-029.md` is the 33@lecturesfrom identity check, a different document |
| Gmail thread bodies | absent. Package logs are summaries |
| Raw Google Calendar export | absent. `meetings-to-classify.csv` is a 34-row Claude coding, not the export |

## Collision handling inside the sidecar

The drop was flat with hashed suffixes. Unique files were copied under `package/` using the package `MANIFEST.md` tree. First-file-wins was corrected for the four named collisions:

| collision | winner in `package/` | discarded sibling kept as |
|---|---|---|
| `extraction.md` x4 | `prompts/extraction.md` (byte identical, md5 prefix `dc6a5f19`) | not needed |
| `codebook.md` vs `03-codebook.md` rev 2 vs rev 1 | rev 2 at `knowledge/03-codebook.md` | `knowledge/codebook.md`; `knowledge/03-codebook-rev1-still-has-newsletter-community.md` |
| `QUERY-MANIFEST.md` 57-line vs 78-line | `protocol/QUERY-MANIFEST.md` (78-line, `e839`) | `protocol/QUERY-MANIFEST-discarded-57-line.md` |
| `02-current.md` two revisions | `knowledge/02-current.md` (the later 27883-byte file) | `knowledge/02-current-earlier.md` |
| `protocol.md` two revisions | `knowledge/protocol.md` (9820-byte, updated 2026-08-30) | `knowledge/protocol-alt.md` (5485-byte, 2026-08-29) |

This tree's `knowledge/03-codebook.md` (rev 1) was **not** replaced. Changing it would invalidate Freeze 1 and Freeze 2 rows.

## File list, unique objects

Classes: `raw_employer_artifact`, `platform_log`, `screenshot_transcription`, `claude_coding_table`, `paper_draft_or_notes`, `instructions`, `retrieval_log`, `out_of_scope`.

Apparent freeze is the package's own numbering, not this tree's Freeze 1/2/3.

### Platform logs (structured applied lists)

| unique object | rows | class | notes |
|---|---|---|---|
| `linkedin_applied_jobs_pages_1_to_10.csv` | 99 | platform_log | Same schema and 99 rows as Freeze 2. Differs only by CRLF versus LF. Not a later page set |
| `jobright_applications_log.csv` (two copies, identical) | 40 | platform_log | **Byte-identical** to Freeze 2 `artifacts/platform/jobright_applications_log.csv` |

### Claude coding tables (derived, not raw)

| unique object | rows | class | notes |
|---|---|---|---|
| `full-application-register.csv` | 321 | claude_coding_table | Package register. 234 `gmail/ATS`, 87 `LinkedIn`, 298 distinct `company`, 35 blank `applied_date`. VERIFY A1 held. Not this tree's census |
| `gmail-stratum-roster.csv` | 276 | claude_coding_table | Entity typing EMP/INT/ATS/ENG/EXC. Header says 276 data rows; package MANIFEST says 274 |
| `linkedin-applications-in-window.csv` | 105 | claude_coding_table | LI-001 to LI-105, minute timestamps, `dedupe_status=UNCHECKED` on every row. `submission_channel=linkedin_easy_apply` on all 105 |
| `linkedin-dedupe-resolution.csv` | 105 | claude_coding_table | Package adjudication of the 105. Claims 87 net_new. Independent match against this tree's 298 is in `adjudication/package_linkedin_match.csv` |
| `meetings-to-classify.csv` | 34 | claude_coding_table | Calendar meetings. `YOUR_CALL` already filled (VEND 13, VEND? 12, COMM 5, OPP 3, INT 1). Not a raw export |

### Retrieval logs

| unique object | class | notes |
|---|---|---|
| Package logs 001–021 (21 unique, each duplicated in the drop) | retrieval_log | Continue the original personal-Gmail sweep. **0 of 35 overlapping numbers 001–036 are byte-identical** to `artifacts/gmail/` |
| Package logs 022–028, 030–036 (no 029) | retrieval_log | Package continues Gmail. This tree's 022–036 are Freeze 3 lecturesfrom / personal remainder. Same numbers, different files |
| Package logs 037–051 | retrieval_log | New to this tree. Copied to `logs/retrieval-log-037.md` through `051.md`. Never recoded into application rows |
| Package log 029 | missing | ENG-B source. Do not renumber. Do not treat this tree's 029 as a substitute |

Log 052 in this tree is the VERIFY Part A audit of the drop. It is not a package file.

### Knowledge, protocol, prompts, instructions

| unique object | class | notes |
|---|---|---|
| `08-census-ledger.md` | paper_draft_or_notes | Package-internal total 321. Changelog ends at 321. Log 051 instructs 325. Not this freeze's census |
| `03-codebook.md` rev 2 (`633e`) | paper_draft_or_notes | A1–A4 applied. Do not copy over this tree's codebook |
| `03-codebook.md` rev 1 (`c66f`) and `codebook.md` | paper_draft_or_notes | Still list `newsletter_community`. Handout that would invalidate independent coding |
| `05-codebook-amendments-r1.md` | paper_draft_or_notes | Status still PENDING APPROVAL, while rev 2 claims A1–A4 applied |
| `00-core.md`, `01-engagement.md`, `02-current.md` (two revs), `04-engagements.md`, `06-method-retrospective.md`, `07-meetings-to-classify.md` | paper_draft_or_notes | Citation and structure only |
| `protocol.md` (two revs), `sources.md`, `QUERY-MANIFEST` (two revs), empty `CORPUS-MANIFEST.md` | paper_draft_or_notes | Package protocol. Empty corpus table. Q12 cited elsewhere and absent from both QUERY-MANIFEST files |
| `extraction.md` (4 identical copies) | instructions | Artifact-to-row rules |
| `README-coder.md` (3 identical copies) | instructions | Still points at `codebook.md` |
| `AGENTS.md`, `MANIFEST.md`, `VERIFY.md` | instructions | Package contract. VERIFY Part A is `logs/retrieval-log-052.md` |
| `README.md`, `raw/README.md`, `paper/README.md`, `project/README.md`, `other/description.md`, `instructions.md` | paper_draft_or_notes / out_of_scope | Package README states 325; that is package AGENTS copy, not a ledger move, and not this tree |

## Independent match of the 105 LinkedIn extract to this tree's 298

Source: `adjudication/package_linkedin_match.csv`. Matching used Freeze 2 ingest rules plus aliases (Elios AI to Elios, QuadSci to QuadSci.ai, SoTalent to Solant, Method Recruiting long name, The Hog YC F25). No application_id was added.

| match_status | n | treatment |
|---|---|---|
| overlap | 89 | already in the 298. Do not double-count |
| company_present_role_differs | 1 | Evolution USA: LinkedIn "Forward Deplyed Engineer (FDE)"; census already has Forward Deployed Engineer (FDA Applied AI / GenAI). Typo, same row |
| opportunity_or_non_census | 3 | BX Studio, The Hog (YC F25), COLOSSUS TECHNOLOGY GROUP. Stay opportunity / non-census. Do not mint as applications |
| candidate_net_new | 12 | **held**. See below |

### Twelve LinkedIn rows held (would move 298 if added)

| id | company_as_listed | role_as_listed | date_applied | open question |
|---|---|---|---|---|
| LI-002 | Datricks | Sales Engineer - US (Remote) | 2025-06-20 | application? |
| LI-003 | Bitovi | AI Enablement Engineer | 2025-06-30 | application? |
| LI-005 | ScoutLab.io | Brand New Role! - AI FinTech Heavyweight! - Solutions | 2025-06-30 | application? recruiter spam title |
| LI-006 | JetBridge AI | Sr. SDR for Profitable AI Startup | 2025-07-01 | same title as LI-008, different date. Counting rule 4: one cycle or two? |
| LI-007 | Abacus.AI | Senior Sales Development Representative | 2025-07-02 | application? |
| LI-008 | JetBridge AI | Sr. SDR for Profitable AI Startup | 2025-07-08 | pair with LI-006 |
| LI-009 | Brainfish | Sales Development Representative (SDR) | 2025-07-08 | application? |
| LI-011 | ClosedWon Talent | Founding Account Executive | 2025-07-09 | application? Log 038 names brian at closedwon.xyz |
| LI-012 | SWARM | Sales Engineer | 2025-07-09 | application? |
| LI-014 | Insignia Assets | Head of Digital | 2025-07-10 | Log 038: possible collision with census Insignia Collab unspecified |
| LI-096 | Stealth Startup | GTM Leader / Head of Growth [33260] | 2026-07-22 | unresolvable identity unless a later artifact names the employer |
| LI-098 | Kana | GTM Engineer | 2026-07-24 | application? |

Jobright Axon KAE, Autodesk, MavenAI, and Vanco are **already in the 298** as Freeze 2 `platform_log`. Adding them again to match a package 325 would double-count.

## Treatments (proposed and applied where they cannot move 298 / 14)

The ingest plan forbids adding, merging, or removing an `application_id` until a treatment is confirmed per class. Conservative treatments below do not change 298 or 14. Census-moving treatments stay **held**.

| class | treatment | status |
|---|---|---|
| Package sidecar `package/` | Keep as a comparison corpus. Do not overwrite this tree's codebook, Freeze 1 Gmail, Freeze 2 platform CSVs, or `applications__full_census.csv` | **applied** |
| Package logs 037–051 | Append-only into `logs/`. Retriever notes, not rows | **applied** |
| Package logs 001–036 | Second sequence under `package/logs/` only. Do not replace `artifacts/gmail/` | **applied** |
| Jobright CSV | Duplicate of Freeze 2. Log as overlap. Do not double-count. Do not recode | **applied** |
| LinkedIn pages 1–10 | Duplicate of Freeze 2 aside from line endings. Log as overlap. Do not recode | **applied** |
| LinkedIn 105 extract | Claude coding of an absent `Job Applications.csv`. Use as a hint list. Independent match only. `linkedin_easy_apply` is not imported into this codebook | **applied as match, not as census** |
| 12 `candidate_net_new` LinkedIn rows | Do not mint `application_id` until confirmed per row | **held** |
| BX Studio, The Hog, Colossus | Opportunity / non-census. Do not mix into the 14 or the 298 | **applied (no mint)** |
| `full-application-register.csv` and package ledger 321 / 325 | Third-coder comparison and hint list. Ignore as this freeze's finding | **applied (not adopted)** |
| `meetings-to-classify.csv` | Hint list against Freeze 3 calendar. Do not recode the 338-event sweep | **applied as copy under `artifacts/calendar/`, not recoded** |
| Paper drafts, methods, READMEs, AGENTS, VERIFY | Citation and structure. Not a data source. VERIFY Part A already in log 052. Proposed package AGENTS/ledger edits are not applied here | **applied** |
| Raw Gmail/Calendar/ATS in the drop | None present | n/a |
| Screenshot / transcription | None in the drop. Kiln screenshots were already Freeze 3 | n/a |
| LinkedIn messages analysis (separate drop) | Claude coding of `messages.csv`. Match, do not mint. Log 054 | **applied as match, census unchanged** |

## Questions still asked (not guessed)

For any later confirmation that would move a number:

1. Study window for the 105-row extract: same 2025-06-01 to 2026-08-29 America/New_York, or a different window?
2. For each of the 12 held LinkedIn rows: application, opportunity, consulting, or employment?
3. JetBridge AI LI-006 and LI-008: one cycle or two?
4. Insignia Assets versus Insignia Collab: same employer, or two strings from two artifacts?
5. Package log 037 codes two Kiln interviews (Giorgio 2026-03-03 and Patrick 2026-03-04). This tree has one dated artifact (Patrick, 2026-03-04) and Giorgio as introducer. The messages analysis adds a Giorgio same-day video on 2026-03-03 in a different thread. Mint a Giorgio interview, or keep `evidence_system = memory` for a second round?
6. Can package log 029 (ENG-B) be recovered from the original chat?
7. AnyInt AI: mint as `platform_log` application, or wait for `Job Applications.csv`?
8. Cyft and Starbridge: mint as opportunity from package Gmail 024 plus these DMs, or wait?
9. Hotglue is not in the 54 threads. Was Kevin Wright's inbound in `messages.csv` under a different keyword, or a different channel?

## What this inventory will not do

- Write the paper.
- Treat 247, 11 interviews, 4.45 percent, 321, or 325 as this freeze's finding.
- Mix opportunity interviews into 14/298.
- Invent a company or a role to force a match.
- Recode the frozen 221 or the Freeze 2 platform files.
