<!-- kit-meta
file: retrieval-log-056.md
created: 2026-08-30
source: subject confirmation that recalled conversations happened; pressure-test names from log 055; overlay coding/confirmed
method: log recall as evidence_system = memory; do not recode Freeze 1 or Freeze 2; do not pour opportunity or employment into 298 or 14/298
-->

# Retrieval log 056

Subject confirmation overlay. Census remains **298**. Interviewed applications remain **14**. The overlay does not recode frozen `discovery_source` or frozen `counterparty_name`.

Rule applied: if the subject says a conversation happened, it is logged. Recall is tagged `memory` so a skeptic can drop it. Happened is not the same as `register = application`.

## Why 298 did not absorb these rows

| name | happened | register | why it stays out of 298 and out of 14/298 |
|---|---|---|---|
| Mixmax / Heath | calendar 2025-08-14, then service agreement | employment | Contractor GTM after GTM Engineer School. Freeze 3 exclusion `marketplace_profile`. Subject calls the Heath meeting an interview. That label is memory. Not a submitted search application. |
| Mercor contract | Claire, Daniel Luo, Instant Work Offer, contract 2026-08-21 | opportunity | Made money. Separate Mercor marketplace receipts stay in the 298 without interviews. Mixing the contract into the denominator would double-count Mercor and mix paid work into the search rate. |
| Pin, The Hog, Glytec, Opsin, Hotglue, The Kiln | interviews evidenced | opportunity | No ATS submission receipt (or LinkedIn applied-list opportunity treatment for The Hog). Interviews sit outside 14/298 by register. |
| WorkOS | TopHire slot booked 2025-08-25 | opportunity | Recruiter path. `recruiter_screen` event is a booked slot. A completed live call is not separately dated. |
| Adam Andrewjeski | calendar 2025-06-18 | overlay opportunity | Informal. No employer string. Company stays `unknown`. Not an application. |
| Doug Shankman | calendar 2025-10-27 | overlay opportunity | Informal plus CRO idea. Organizer domain is not used as an invented employer. Not an application. |
| Kivira.health | GTM Overview and weekly outbound | consulting | Three month GTM via Josh Pappas. Client work. Not a search application. |
| BCOFA / Dr. Blaney | calendar 2026-03-06 | consulting | Fizzled. No money. |
| Jorge Macias | recurring calendar from 2025-07-04 | communal | GTM Engineering School TA and mentorship. Not a job. |
| Kellen Casebeer | calendar 2025-06-16 | communal | Clay Cafe founder, TA, Mobb prep. Not a search opportunity. |

The twelve held LinkedIn candidates (Datricks, Bitovi, ScoutLab.io, JetBridge AI, Abacus.AI, Brainfish, ClosedWon Talent, SWARM, Insignia Assets, Stealth Startup, Kana) and AnyInt AI were not confirmed as applications in this pass. They stay held.

## Overlay rows minted

`coding/confirmed/applications__confirmed.csv` (not merged into `applications__full_census.csv`):

- `unknown|informal-adam-andrewjeski|c1`
- `unknown|cro-idea-doug-shankman|c1`

`coding/confirmed/events__confirmed.csv`:

| event_id | parent | what memory adds | token |
|---|---|---|---|
| unknown\|informal-adam-andrewjeski\|c1\|e1 | overlay Adam row | interview classification | tok_4c79cbbc329f |
| unknown\|cro-idea-doug-shankman\|c1\|e1 | overlay Doug row | interview classification | tok_654cb884181e |
| opsin\|unspecified\|c1\|e0 | freeze3 Opsin | Colossus phone round before James Pham | tok_b1f3dc9b0958 |
| the-kiln\|unspecified\|c1\|e3 | freeze3 The Kiln | Giorgio as interviewer (introducer remains artifact) | tok_8c8acbc92d3c |
| phrasiq\|unspecified\|c1\|name | freeze PhrasIQ | Eddie | tok_f70bd14e358a |
| pearl\|lead-gtm-engineer\|c1\|name | freeze Pearl | Chris on round 2 | tok_fd8fde3f5245 |
| great-question\|senior-demand-generation-manager\|c1\|name | freeze Great Question | Harry (artifact spelling Harri) | tok_01583f192d92 |
| dagster-labs\|gtm-engineer\|c1\|medium | freeze Dagster | phone medium | tok_6ad68eb83f3c |

Name overlays do not add a round. Opsin e0 and Kiln e3 add a memory round on an existing opportunity parent. They do not enter the 14.

Mixmax is not given a Table 1 parent. It stays employment in `adjudication/ORIGINS.md` and `adjudication/origins__subject_confirmed.csv`. Calendar pointer for the Heath meeting: `cal_3e5387362a5b33e3`.

## Combined scoreboard (not one number)

Paper-facing writeup: `adjudication/ORIGINS.md`. Machine-readable join: `adjudication/origins__subject_confirmed.csv` with flags `in_298`, `in_14`, `made_money`.

- A. Artifact census: 298 applications, 14 interviewed, rate 14/298
- B. Opportunity conversations outside the 14, plus overlay Adam and Doug
- C. Money: Mixmax, Mercor contract, Mobb, Kivira.health. BCOFA unpaid
- D. Communal: Jorge, Kellen

`adjudication/derive_metrics.py` still reads only `cursor`, `alpha`, and `bravo`. Coder `confirmed` is excluded from that derivation on purpose.

## What this log does not do

- Recode Freeze 1 Gmail or Freeze 2 platform CSVs
- Write Eddie, Chris, Harry, or GTM Cafe onto frozen event or application rows
- Adopt package 321 or 325
- Mint the twelve held LinkedIn rows or AnyInt AI
