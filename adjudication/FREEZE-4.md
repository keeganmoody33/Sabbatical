# Freeze 4 care-package ingest

Freeze 1 Gmail extracts, Freeze 2 platform CSVs, and Freeze 3 personal mail and calendar were not recoded.

The 2026-08-30 Claude care package is inventoried in `package/INVENTORY.md`. Treatments that would add, merge, or remove an `application_id` remain held. Conservative treatments that cannot move the census were applied.

## Census

- Full application census remains **298**
- Interviewed applications remain **14**
- Net-new `register = application` rows in this freeze: **0**
- Net-new opportunity rows in freeze coder files: **0**
- Overlay opportunity rows in `coding/confirmed/` (not copied into the 298): Adam Andrewjeski / Stellar Growth, Doug Shankman informal CRO idea (predates AICRO; not merged with AICRO applications), Mixmax Heath parent for the interview event

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
| Subject-confirmed overlay | `adjudication/ORIGINS.md`, `adjudication/origins__subject_confirmed.csv`, `coding/confirmed/` | memory and origins; does not recode freezes |
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

## LinkedIn messages unpacking (same freeze)

Claude analysis of `messages.csv` from a 2026-08-23 LinkedIn data export. Not the raw CSV. Independent match in `adjudication/linkedin_dm_match.csv`. Retrieval log 054.

- Net-new application rows from DMs: **0**
- Net-new opportunity rows from DMs: **0** (Cyft, Starbridge, Aptean, Ambient.ai, Claudomat, Parallel, and others remain held)
- AnyInt AI is a held application candidate (named in DMs as an applied role, absent from the 105 and the 298)
- Hotglue and Pin are not in the 54 threads
- The Kiln Giorgio DM does not mint a second interview

## Still absent

Ladders, YC Work at a Startup dashboard, [S1] and [S2] workbooks, LinkedIn `Job Applications.csv`, raw `messages.csv`, package log 029, Gmail thread bodies, raw calendar export, applied-list UI pages after 10 with Easy Apply labels.

## Subject-confirmed overlay

If the subject says a conversation happened, it is logged. Recall is tagged `evidence_system = memory`. Overlay files:

- `adjudication/ORIGINS.md` (paper-facing)
- `adjudication/origins__subject_confirmed.csv` (flags `in_298`, `in_14`, `made_money`)
- `coding/confirmed/` (Adam, Doug, name and round overlays)

Frozen `discovery_source` and frozen `counterparty_name` were not recoded. The 14 does not include overlay rounds. Mixmax stays employment.

## VERIFY

Part A ran as `logs/retrieval-log-052.md`. Ingest completion is `logs/retrieval-log-053.md`. Package AGENTS and ledger edits proposed in log 052 were not applied to this tree. Messages unpacking is log 054. Pressure-test is log 055. Overlay is log 056. Confirmation pass (Patrick, James, Mercor count, Heath conversion, Hologram count, Adam Stellar Growth) is log 057. Doug predates AICRO and headlines are log 058.
