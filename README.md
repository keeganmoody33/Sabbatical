# Sabbatical

Forensic census of Keegan Moody's job search, study window 2025-06-01 to 2026-08-29, America/New_York.

This repository holds the protocol, the frozen artifact corpus, independent coder output, adjudication, and the numbers that can be published with a method behind them.

## Reproduce everything

```bash
make check
```

No dependencies. Python 3.11 standard library only. It runs the whole pipeline and fails if a re-run
of the frozen corpus moved a byte of any committed output. See `pipeline/README.md`.

## Do not publish yet

247 applications, 11 interviews, and 4.45 percent are prior-audit figures. They are not the output of this freeze. See `knowledge/protocol.md` and `artifacts/STOP-CONDITIONS.md`.

The paper is drafted and unpublished. `paper/NAMED-COMPANIES.md` lists seven still-open processes that need a naming decision before anything goes out.

## What this freeze found

221 applications with employer-side proof, 298 including platform-only rows, and 13 that reached an
interview. Roughly half of all applications produced a receipt and then nothing.

The most useful finding is an absence: where each role was found is unknown on 206 of 221 rows, and
on the rows where origin is known, no outcome is observable. No origination-channel conversion figure
exists here, and section 3.2 of the paper explains why none should be produced without new data.

## Layout

- `knowledge/` durable counting rules, codebook, protocol
- `schema.md` grain, keys, and the unit of analysis for every metric
- `assumptions.md` every inference rule, with its status and what it rules out
- `codebook.md` field definitions and controlled vocabularies
- `prompts/extraction.md` coder instructions
- `artifacts/` raw retrieval logs and calendar export
- `coding/` independent coder CSVs. Frozen, never edited
- `adjudication/` disagreement inventory, census, latency
- `pipeline/` the single entrypoint and the view and validation layer
- `views/` analysis tables the paper quotes from
- `data_quality_report.md` generated on every run
- `paper/` the draft, its number trace, figure specs, and naming checklist
- `translation/` the companion piece written for non-technical readers

## How to re-run retrieval

Gmail and Calendar connectors must be the accounts named in `QUERY-MANIFEST.md`. Exhaustion means no `nextPageToken`.
