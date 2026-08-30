# Freeze 4 care-package ingest

Freeze 1 Gmail extracts, Freeze 2 platform CSVs, and Freeze 3 personal mail and calendar were not recoded.

The 2026-08-30 Claude care package is inventoried in `package/INVENTORY.md`. Treatments that would add, merge, or remove an `application_id` remain held. Conservative treatments that cannot move the census were applied.

## Census

- Full application census remains **298**
- Interviewed applications remain **14**
- Net-new `register = application` rows in this freeze: **0**
- Net-new opportunity rows in this freeze: **0**

Package ledgers are a different assembly (321-row register, log 051 instructing 325). They are not this freeze's finding. Jobright Axon KAE, Autodesk, MavenAI, and Vanco are already inside the 298 from Freeze 2. Adding them again would double-count.

## What was ingested

| object | destination | coding |
|---|---|---|
| Package tree (86 unique files) | `package/` sidecar | comparison corpus only |
| Package logs 037–051 | `logs/` append-only | retriever notes, not rows |
| Package logs 001–036 | `package/logs/` only | do not replace `artifacts/gmail/` |
| LinkedIn in-window extract, 105 rows | `artifacts/platform/linkedin-applications-in-window.csv` | Claude coding table. Matched, not minted |
| LinkedIn dedupe resolution | `artifacts/platform/linkedin-dedupe-resolution.csv` | package adjudication, hint list |
| Independent match of the 105 to the 298 | `adjudication/package_linkedin_match.csv` | 89 overlap, 1 role-typo overlap, 3 opportunity/non-census, 12 held |
| meetings-to-classify.csv, 34 rows | `artifacts/calendar/meetings-to-classify.csv` | hint list against Freeze 3 calendar |
| Jobright 40-row tracker | already Freeze 2 | byte-identical, overlap |
| LinkedIn pages 1–10 | already Freeze 2 | same 99 rows, CRLF versus LF only |

## Independent match of the 105 (not a second LLM pair)

This is a documented column mapping of a structured extract onto the existing 298, the same class of work as Freeze 2. Role-lane kappa is not recomputed.

`submission_channel = linkedin_easy_apply` on all 105 is a package vocabulary value. This tree does not import it. Freeze 2 LinkedIn `submission_channel` stays `unknown`.

### Held LinkedIn candidates (no application_id)

Datricks, Bitovi, ScoutLab.io, JetBridge AI (two dates, same title), Abacus.AI, Brainfish, ClosedWon Talent, SWARM, Insignia Assets (possible Insignia Collab collision), Stealth Startup, Kana.

### Not applications

BX Studio, The Hog (YC F25), COLOSSUS TECHNOLOGY GROUP. Opportunity register unchanged.

## Still absent

Ladders, YC Work at a Startup dashboard, [S1] and [S2] workbooks, LinkedIn `Job Applications.csv`, package log 029, Gmail thread bodies, raw calendar export, applied-list UI pages after 10 with Easy Apply labels.

## VERIFY

Part A ran as `logs/retrieval-log-052.md`. Ingest completion is `logs/retrieval-log-053.md`. Package AGENTS and ledger edits proposed in log 052 were not applied to this tree.
