# Retrieval log 037

Two items: a classification settled, and the first deliverable extracted from the LinkedIn export.

## The Kiln, settled

The subject confirms "two engagements" meant **two meetings**, not paid work. The terminology collision flagged in log 036 is resolved in favour of the artifacts.

Final classification:

- `register = opportunity`. Counterparty-initiated, no application, no receipt. **Does not enter the census.**
- Two interview events: round 1 with Giorgio Zanella 2026-03-03, round 2 with Patrick Spychalski 2026-03-04.
- `discovery_source` = GTM Engineer School, via a published testimonial.
- `terminal_outcome = no_response`, `terminal_outcome_precision = evidence_bound`, bound 2026-07-17.
- **No Table 4 entry.** ENG-A through ENG-E stand unchanged at five.

Worth keeping visible in Discussion: The Kiln reached two founder-level conversations in thirty-two hours and then produced nothing, with no decision ever communicated. Alongside Glytec's soft decline and Starbridge's "we found a dream candidate through our network", the counterparty-initiated channel converts to conversation reliably and to outcome rarely. That is a different failure mode from the application channel, which mostly fails to convert to conversation at all.

## Deliverable: the 105 LinkedIn applications, codebook-shaped

Extracted to `linkedin-applications-in-window.csv`. One row per application, sorted by date, keyed `LI-001` to `LI-105`.

Columns map directly onto Table 1: `date_applied`, `date_precision`, `company_as_listed`, `role_as_listed`, `job_url`, `resume_name`, `discovery_source`, `submission_channel`, `evidence_tier`, `evidence_class`, `register`, `dedupe_status`.

Values pre-set and defensible on the source:

- `date_precision = exact`. Minute-level timestamps straight from the platform.
- `evidence_tier = A`. Platform-authoritative record of submission.
- `evidence_class = platform_log`, **not** `employer_artifact`. This matters. `00-core.md` splits these strata precisely so that a sensitivity analysis can be run on employer-confirmed rows only. All 105 sit in the weaker stratum until a receipt is matched to them.
- `register = application`. Every row is an outbound submission by the subject.
- `dedupe_status = UNCHECKED` on all 105.

`resume_name` is populated on most rows and is a bonus the codebook did not anticipate. It permits a question nobody has asked yet: whether résumé version correlates with anything. Park it, do not chase it.

## The blocking task is unchanged and is now scoped

Until every row carries `dedupe_status`, **the census total cannot be stated.** Some of these 105 generated ATS receipts already captured in logs 001 to 020; those are the same application counted twice. Some generated nothing and are net additions.

Scope: 98 distinct companies. A batched Gmail sweep at roughly ten companies per query, using curly-brace OR grouping, resolves it in about ten queries. Companies already known from earlier logs and visible in this extract include Attentive, Applause, Bask Health, BX Studio, and 2X, so the overlap is real and non-trivial.

**Do not estimate the overlap rate.** Measure it.

## Codebook changes now pending, consolidated

Four, all invalidating prior rows if made mid-harvest:

1. `terminal_outcome`: add `converted_to_contract` (log 031).
2. `terminal_outcome`: add `no_response` (log 036).
3. `discovery_source`: add community values. Logs 032 and 036 argue for **two separate values**, GTM Cafe and GTM Engineer School, since one produced an application and the other produced three counterparty-initiated processes.
4. A means of recording that a network contact caused an ATS submission (log 035, the Greg Reardon case).

Make all four before the dedupe writes any rows.

## Open

- Dedupe, 10 batched Gmail queries.
- Triage the 114 inbound LinkedIn conversations.
- `Invitations.csv`, `Saved Jobs`, screening-question responses: unexamined.
- Q8 blocks 4 to 6. Block 4 covers March 2026 and would show whether anything followed The Kiln off-platform.
- Q12 pagination.
- Five engagement descriptions.
