# Manifest

What every file is, which file wins when two disagree, and what was changed when this repo was assembled from the Claude Project on 2026-08-30.

## Collisions resolved during assembly

The Project held 75 flat files with four unflagged collisions. Handing an agent contradictory sources of truth is the exact failure this study exists to document, so each was resolved before packaging. **Every resolution is reversible: nothing was destroyed, the originals remain in the Claude Project.**

| # | collision | resolution | basis |
|---|---|---|---|
| 1 | `extraction.md`, `extraction_2.md`, `extraction_3.md` | kept one as `prompts/extraction.md` | **byte identical**, same md5 `dc6a5f19…` |
| 2 | `codebook.md` (9.9K) vs `03-codebook.md` (15.0K) | **`codebook.md` dropped.** `knowledge/03-codebook.md` is the only schema | not duplicates. `codebook.md` was a coder handout carrying **`newsletter_community`**, a value **retired by amendment A3**. It had no A1 to A4 content at all. `README-coder.md` pointed coders at it. **A coder run against that file would have used a retired vocabulary and invalidated the independent coding design before it started** |
| 3 | `QUERY-MANIFEST.md` (14 query rows, 57 lines, progress stops at Q2b) vs `QUERY-MANIFEST_2.md` (15 rows, 78 lines, progress through Q7) | `_2` kept as `protocol/QUERY-MANIFEST.md` | `_2` is strictly newer and strictly a superset |
| 4 | `claude_` filename prefix on 12 files | stripped | artifact of Project file naming, not meaningful |

**Open item from collision 2:** `prompts/README-coder.md` still says a coder receives "`codebook.md`". That line needs editing to `knowledge/03-codebook.md` before any coder runs. Left unedited here so the change is yours and visible in git.

## Defects carried in, not introduced here

| defect | state |
|---|---|
| **`retrieval-log-029.md` does not exist**, and **it is cited as a source.** Sequence runs 001 to 028, 030 to 051 | **Corrected 2026-08-30.** An earlier pass here claimed it was referenced nowhere. That was a brittle-query error: the grep looked for `log 029`, `log-029`, `logs 029` and missed the forms actually used. `knowledge/04-engagements.md` cites it four times: in its `sources:` meta block, in "retrieval logs 026 to 029 established that engagements ran across much of the study window", in the Rule 5 pre-publication scan instruction, and as a source for **ENG-B (Mobb.ai)**. **This is a missing evidence file, not an unused number.** ENG-B's provenance is partly unrecoverable without it. **Do not renumber.** Recover it from the original chat history if possible; if not, `04-engagements.md` needs a stated gap |
| **`protocol/CORPUS-MANIFEST.md` is unpopulated** | every row blank. The corpus is not frozen, so independent parallel coding cannot legitimately begin |
| **`raw/` is nearly empty** | see below. This blocked log 046 mid task and will block a fresh agent the same way |
| **Rule 6 unresolved** | whether an agent tracker's "Applied by Agent" satisfies counting rule 6. Log 051 routed around it using subject recall. Next agent-only row without recall is blocked |

## Tree

```
AGENTS.md                    behavioral contract, agents load this first
MANIFEST.md                  this file
README.md                    orientation for a human
knowledge/                   the durable and volatile knowledge tiers
  00-core.md                 how the subject works, publication standard, definitions
  01-engagement.md           the paper, the dataset, decisions made, constraints
  02-current.md              VOLATILE. current numbers, open threads, draft status
  03-codebook.md             THE SCHEMA. rev 2. changing it invalidates prior rows
  04-engagements.md          engagement register ENG-A to ENG-E, redaction protocol
  05-codebook-amendments-r1.md   rationale for amendments A1 to A4
  06-method-retrospective.md     confidence assessment, saturation curve, reusable master prompt
  07-meetings-to-classify.md     34 counterparty meetings awaiting classification
  08-census-ledger.md        THE ONLY FILE THAT STATES A TOTAL
protocol/
  protocol.md                frozen pre-registration, revisions logged
  sources.md                 S1 to S6, what each contributed, how to re-pull
  QUERY-MANIFEST.md          every retrieval query, status, exhaustion state
  CORPUS-MANIFEST.md         UNPOPULATED. freeze the corpus here before coding
prompts/
  extraction.md              artifact to schema row rules. use verbatim
  README-coder.md            coder brief. NEEDS THE codebook.md PATH FIXED
logs/                        retrieval-log-001 to 051, no 029. APPEND ONLY
data/                        derived working sets, rebuildable from logs
  full-application-register.csv    321 rows as built. log 051 takes it to 325
  gmail-stratum-roster.csv         274 entities typed EMP/INT/ATS/ENG/EXC
  linkedin-dedupe-resolution.csv   105 LinkedIn rows, all resolved
  linkedin-applications-in-window.csv
  meetings-to-classify.csv
raw/                         PRIMARY SOURCES. mostly missing, see below
paper/                       empty. nothing drafted yet
project/                     original Claude Project config, provenance only
```

## What `raw/` is missing

These are named in `protocol/sources.md` but live on Keegan's machine, not in the Project. **Log 046 stopped dead because [S1] was unavailable.** A cloud agent will hit the same wall.

| id | file | why it matters |
|---|---|---|
| S1 | `job_search_reconciled_audit.xlsx` | the retired 247 ledger. Historical, but log 046's join needs it |
| S2 | `Keegan_Moody_Job_Applications_Audit_2025-08_to_2026-08.xlsx` | the prior 212 floor and counting rules 1 to 8 |
| S3 | `linkedin_applied_jobs_pages_1_to_10.csv` | the 99 row scraped page set |
| S3b | LinkedIn data export: `Job Applications.csv`, `messages.csv` | 1,279 applications and 5,256 messages all time |
| S4 | `jobright_applications_log.csv` | **present.** confirmed complete by the subject, log 051 |
| S5 | `LADDERS.png` | 3 Apply4Me rows |
| — | Google Calendar export, 6 blocks, 277 events | the event layer. Currently only summarized inside logs |
| — | Gmail thread bodies, 1,152 threads | logs record thread ids only. Bodies were never exported |

**The last two are the largest hole.** The retrieval logs are summaries written by a reader of those artifacts. They are not the artifacts. A second independent coder cannot be run against a summary, which means the pre-registered independent parallel coding design is currently unexecutable.

## Provenance of this repo

Assembled 2026-08-30 from the Claude Project "Sabbatical", 75 files, 700K. No content was rewritten. Files were renamed, deduplicated and foldered. `AGENTS.md`, `MANIFEST.md`, `README.md`, `.gitignore` and the `raw/` and `paper/` READMEs are new and are the only files here not carried over.
