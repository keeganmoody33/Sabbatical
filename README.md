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

The paper and its companion are drafted and unpublished. `paper/NAMED-COMPANIES.md` lists eight still-open processes that need a naming decision before anything goes out, and the companion names ten companies the paper does not.

## What this freeze found

223 applications with employer-side proof, 317 including platform-only rows, and 14 that reached an
interview. Roughly half of all applications produced a receipt and then nothing.

The most useful finding is an absence: origin was captured at the time on 15 of 223 rows, recovered
afterwards on 60 more only because a platform logged them, and is unrecoverable on the remaining 148.
No origination-channel conversion figure exists here, and section 3.2 of the paper explains why.

`challenge/CHALLENGE.md` is an adversarial reconciliation against a second, independently produced
reconstruction of the same fifteen months. It moved two figures and failed to move the rest.

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
- `paper/` the paper and its companion piece, plus the number trace, figure specs, and naming checklist
- `challenge/` the adversarial reconciliation against a second reconstruction
- `translation/` the companion piece written for non-technical readers

## How to re-run retrieval

Gmail and Calendar connectors must be the accounts named in `QUERY-MANIFEST.md`. Exhaustion means no `nextPageToken`.
