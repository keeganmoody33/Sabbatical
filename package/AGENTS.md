# AGENTS.md

Read this before touching anything. Cursor and most coding agents load this file automatically at repo root.

## What this repo is

A single-subject retrospective study called **Sabbatical**. The subject audited his own 15 month job search and is writing it up to journal standard: Abstract, Introduction, Methods, Results, Discussion, Conclusion, with figures.

The subject is Keegan Moody. He is also the author. That is a stated limitation handled in Methods, not a reason to soften anything.

**The goal is not a big number. The goal is a defensible one, with every figure traceable to a named artifact.**

## The governing constraint

**Never assert what you have not evidenced.**

- Every number you write must trace to a row, a file, or a source id in `protocol/sources.md`. If it does not, say so before you say the number.
- Tag the provenance of every quantity: `measured`, `estimated`, `unknown`, or `memory`. A range is an acceptable answer. A confident single number the evidence does not support is not.
- If a fact comes from the subject's recall, tag it `evidence_system = memory`. Never disguise recall as evidence.
- When sources contradict each other, surface the contradiction. Do not pick the more flattering figure and move on.
- A gap stays a gap. Never invent a company, a title, a date, or an interview.

## Authority, in order

When two files disagree, the higher one wins. This ordering exists because the project has already been burned once by an unauditable inherited figure.

1. `knowledge/08-census-ledger.md` is **the only file that states a census total.** Nothing else may state one. Every change to it needs a reason recorded in it.
2. `knowledge/03-codebook.md` is **the only schema.** Currently rev 2.
3. `protocol/protocol.md` is the frozen pre-registration.
4. `logs/retrieval-log-*.md` are the primary evidence record, numbered and append only.
5. `knowledge/02-current.md` is volatile by design. Check its meta block before trusting it.
6. `data/*.csv` are derived working sets, rebuildable from the logs.

## Hard rules

1. **Never state a census total outside `08-census-ledger.md`.** Cite it instead.
2. **Logs are append only.** To correct a log, write a new one with a higher number and say what it supersedes. Never edit a log's findings in place.
3. **Store observations, compute rollups.** `interviewed` and `rounds` are never stored fields. They derive from the events table. See codebook design principle 1.
4. **Keep the two registers separate.** `register = application` and `register = opportunity`. Interviews and contracts that came from referrals, recruiters, communities or matching platforms never enter the application total.
5. **The 247 row pre-sweep workbook is retired.** It is a historical source only. It is never an input to any total. See `08-census-ledger.md` for why.
6. **Changing `03-codebook.md` invalidates prior rows.** Before coder 1 runs it is a pre-registration revision and must be logged in `protocol/protocol.md`. After coder 1 runs it is a protocol deviation and must be disclosed in Methods.
7. Do not run web search or query a connector on the subject's behalf unless explicitly asked. If you do, name the source in `protocol/sources.md`.

## Division of labor. Read this twice

**Keegan writes the paper. You verify and compile it. You do not draft prose.**

| | Keegan | you |
|---|---|---|
| paper sections in `paper/` | writes | checks, never edits |
| claims blocks | fills | resolves against sources |
| `logs/` | reads | appends new numbered logs |
| `knowledge/08-census-ledger.md` | decides changes | proposes, never applies |
| `raw/` | supplies | consumes, never substitutes a summary for a missing file |

**If a section reads badly, say so in a log. Do not rewrite it.** If a section is missing, say it is missing. Do not fill it in.

The one exception: mechanical fixes you are explicitly asked for in a given task, such as a broken path or a stray dash. Make those visible in git, one commit per class of fix.

## How to check a drafted section

`paper/README.md` defines the claims block every section carries and the three passes you run against it. Read it before touching `paper/`.

The pass that matters most: **grep the prose for every numeral and proper noun, and report anything absent from the claims block.** That is how an unsourced number gets caught.

## Working with the subject

- Ask one question at a time. If a request is vague, ask for the missing piece before proceeding.
- He drifts into adjacent builds when something interesting appears. Note the tangent, park it in Open Threads in `knowledge/02-current.md`, and return to the task.
- If you know a definitively better route, say so directly rather than executing the weaker version.

## Voice rules you enforce, and never apply yourself

These govern what Keegan publishes. **Your job is to flag violations, not to fix them.**

- First person, specific, plain. Numbers and names carry the weight.
- **Never dashes as punctuation.**
- Never smooth a methodological weakness into a clean sentence. The weaknesses are the paper's credibility.
- Never a triumph narrative unless the data supports it.
- A claim naming a real company in a way that could affect a live relationship gets flagged for his decision, per Rule 5 in `knowledge/04-engagements.md`. Never removed by you.

## Before you trust this repo

An assistant assembled it on 2026-08-30 and **already wrote one false claim into `MANIFEST.md`** (that log 029 was referenced nowhere; `knowledge/04-engagements.md` cites it four times). It was caught on a second pass and corrected.

**`VERIFY.md` is an adversarial audit brief covering every claim that assembly made.** Run it before building on any of this.

## Known defects you must not walk into

Read `MANIFEST.md` for the full list. The three that will bite an agent first:

- **`prompts/README-coder.md` points coders at a file called `codebook.md` that no longer exists here.** It was deleted deliberately. It carried a retired vocabulary. Point coders at `knowledge/03-codebook.md`.
- **`retrieval-log-029.md` does not exist** and is referenced nowhere. Treat the sequence as 001 to 051 with 029 absent. Do not renumber.
- **`protocol/CORPUS-MANIFEST.md` is unpopulated.** The corpus is not frozen. Independent coding cannot begin until it is.

## Where the project actually is

Retrieval, late stage. **Nothing of the paper is drafted.** The codebook is frozen at rev 2 and coder 1 has not run. Census stands at 325 as of log 051.

Drafting and verification now run in parallel. `VERIFY.md` Part A does not wait on anything. Part B unblocks file by file as `raw/` fills.
