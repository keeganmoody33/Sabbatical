# Coder brief

You are one of several independent coders on a research dataset. Your job is to convert a fixed set of raw artifacts into structured rows. You are not analyzing, summarizing, or estimating anything.

## What you have

- `codebook.md`, the field definitions and controlled vocabularies
- `extraction.md`, the extraction rules
- `artifacts/`, the corpus

That is the complete set. Every coder receives the identical corpus.

## Study window

2025-06-01 to 2026-08-29, America/New_York, inclusive. Artifacts outside this window get an `exclusions` row with `exclusion_reason = out_of_window`. Do not silently drop them.

## Rules of the exercise

1. **Use only the artifacts provided.** Do not search the web. Do not query a mailbox, calendar, or any connector. Do not use what you know about these companies. If the corpus does not say it, it is not in your output.
2. **Do not consult another coder's output.** If you have seen one, say so at the top of your submission and stop.
3. **Do not optimize toward a total.** You are not trying to reach a number. A coder who produces fewer rows because the evidence was thinner is doing the job correctly.
4. **Code every artifact.** Uncertain ones become `exclusions` rows with a stated reason, not omissions. Exclusions are data.
5. **Do not revise the vocabularies.** If a value does not fit, emit the codebook fallback for that field (`unknown` where the vocabulary includes it; `none_observed` for `ats_system`) and explain in `notes`. If you find yourself wanting a new enum value more than twice, note it at the end rather than inventing one.

## Output format

Three CSV files, with these exact headers and nothing else in the file:

- `applications__{coder_id}.csv`
- `events__{coder_id}.csv`
- `exclusions__{coder_id}.csv`

Headers are the field lists in `codebook.md`, in the order given there, beginning with `coder_id`. Empty means not observed. Never write `N/A`, `none`, or a dash. Use the literal string `unknown` only where the codebook lists it. For `ats_system`, the fallback is `none_observed`.

Plus one plain text file, `notes__{coder_id}.md`, containing:

- Artifacts processed, rows emitted per table
- Every judgement call, one line each
- Every conflict between artifacts, with both values
- Any vocabulary term you wanted and did not have

`coder_id` is a short lowercase string you are assigned. Put it in every filename and in the `coder_id` column on every row.

## What happens next

All coders' outputs are compared before anyone sees another's. Agreement is measured on `role_lane` and on the include-or-exclude decision. Disagreements go to a named adjudication pass. The pre-adjudication disagreement rate is published.

This means your disagreements are useful. Do not hedge toward what you think another model would say.
