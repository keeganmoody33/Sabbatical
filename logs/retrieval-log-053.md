<!-- kit-meta
file: retrieval-log-053.md
created: 2026-08-30
source: Claude care-package ingest after inventory in package/INVENTORY.md
method: file inventory of 119 uploads / 86 unique md5; independent match of linkedin-applications-in-window.csv to applications__full_census.csv; scoped redaction via scripts/redact_corpus.py
-->

# Retrieval log 053

Care-package ingest. No census total is changed. This log records what was committed and what was held.

## Inventory

119 files in the drop, 86 unique by md5, 33 extra copies. Full list and classes: `package/INVENTORY.md`.

Nothing in the drop failed to open. The drop is markdown and CSV only.

Absent from the drop, still absent from this freeze: [S1] xlsx, [S2] xlsx, Ladders, YC dashboard, LinkedIn `Job Applications.csv`, package log 029, Gmail bodies, raw calendar export, applied-list UI pages after 10.

## Identity of logs 001–036

Confirmed again after copy: 0 of 35 overlapping numbers are byte-identical between `artifacts/gmail/` and `package/logs/`. Package 001–036 stay under `package/logs/`. This tree's `artifacts/gmail/` is untouched. Package 037–051 are appended to `logs/` as a new series because they are not a continuation of this tree's 022–036.

## Match of the 105 LinkedIn extract

File: `adjudication/package_linkedin_match.csv`.

- 89 overlap with the 298
- 1 company present, role differs (Evolution USA typo FDE / FDA). Treated as the existing census row
- 3 opportunity or non-census: BX Studio, The Hog, Colossus. Not minted
- 12 candidate_net_new, held, listed in the inventory

No `application_id` added, merged, or removed.

## Redaction

Scoped to new ingest files. Freeze 1 Gmail, Freeze 2 platform CSVs, and Freeze 3 calendar CSVs were not rewritten.

58 files updated. Gmail thread IDs hashed `gth_`. Third-party addresses hashed `eml_`. Study mailboxes including `keegan@morphdatastrategies.com` kept. ATS local-parts kept as domain identity, matching `scripts/redact_corpus.py`. Log 052 was not passed through the 16-hex replacer because its md5 suffixes would have been false positives.

## Treatments applied versus held

Applied: sidecar `package/`; logs 037–051 append-only; Jobright and LinkedIn pages 1–10 as overlap; 105-row extract as a hint list; meetings CSV as a hint list; package register and ledger ignored as this freeze's finding.

Held, pending confirmation per row: the 12 LinkedIn candidates. JetBridge two dates. Insignia Assets versus Insignia Collab. A second Kiln interview dated only in package log 037.

## Census

`adjudication/applications__full_census.csv` still has 298 rows after ingest. Interviewed applications remain 14. Opportunity register unchanged.
