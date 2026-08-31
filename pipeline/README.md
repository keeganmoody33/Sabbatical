# Pipeline

One command reproduces every published number from the frozen corpus and the frozen coder CSVs.

```bash
make check      # python3 pipeline/run.py
```

No dependencies. Python 3.11 standard library only, which is what the existing scripts already used.

## What runs, in order

| # | Stage | Script | Owns |
|---|---|---|---|
| 1 | `compare_coders` | `adjudication/compare_coders.py` | Pre-adjudication agreement and the disagreement inventory |
| 2 | `adjudicate` | `adjudication/adjudicate.py` | The 223-row application census and the written rule behind every resolution |
| 3 | `ingest_platform` | `adjudication/ingest_platform.py` | Platform rows through Freeze 3, the match cascade, the 317-row full census |
| 4 | `derive_latency` | `adjudication/derive_latency.py` | Time to first response and time to first interview |
| 5 | `derive_metrics` | `adjudication/derive_metrics.py` | Per-coder summary counts, printed. Writes nothing |
| 6 | `build_views` | `pipeline/build_views.py` | `views/*.csv`, the tables the paper quotes from |
| 7 | `data_quality` | `pipeline/data_quality.py` | `data_quality_report.md` |

The order is a dependency order. Stage 2 produces the census that stages 3, 4, 6, and 7 read.

## The check contract

Check mode is the point of having an entrypoint at all.

Every stage declares the files it writes. `run.py` hashes each of them before the run and again
after. If a file that already existed comes back different, the run **exits non-zero**. The
corpus is frozen and the coder CSVs are frozen, so a re-run that moves a byte means either the
pipeline is not deterministic or something changed without being logged. A census that cannot be
reproduced cannot be defended.

A file that did not exist before splits two ways, decided by whether **HEAD** carries the path. If it
does not, the file is `created`, which is what a first run of a new view looks like. If HEAD does
carry it, the file is `RESTORED` and the run fails: a committed output missing before the run means
the checkout was incomplete, so regenerating it verifies nothing. There was nothing to compare
against.

HEAD rather than the index, deliberately. `git ls-files` reads the index, so `git rm` would take the
path out of it and quietly restore the hole this check exists to close. A staged deletion cannot
change what HEAD holds.

When a change is intended, run `make run` (`--write`), then log it in the `knowledge/protocol.md`
changelog with a date and a reason and disclose it in `paper/DEFECTS.md`. That rule is at the head
of the protocol and predates this pipeline.

## What this pipeline never does

- **It never edits a coder CSV.** `coding/bravo/` and `coding/cursor/` are blind independent
  output. Editing one after the fact destroys the agreement statistic retroactively. Corrections
  are applied downstream, by name, in `adjudication/_common.py` and `adjudication/adjudicate.py`.
- **It never re-codes an artifact.** `artifacts/` is the frozen corpus. Re-reading it with a
  different model is a different study, not a re-run.
- **It never touches the matcher's alias table from the view layer.** `pipeline/origin_taxonomy.csv`
  is read by `build_views.py` only. `ingest_platform.py` keeps its own alias table, because a
  lookup shared between the census and the analysis would let an analysis change move the census.

## Adding a view

Add the writer to `pipeline/build_views.py`, add its filename to the `build_views` stage in
`pipeline/run.py`, and document its grain in `views/VIEWS.md`. `run.py` fails if a declared
output is not written, so a view registered but not built is caught on the next run.

`build_views.py` asserts the four published figures on every run: census 223, full census 317,
interviewed 14, latency base 197. Those assertions are there so that a view built on a census
that no longer matches the paper fails immediately rather than being discovered later inside a
table.
