# Corpus manifest

Fill this in when the corpus is frozen. Every coder receives the identical set. A coder holding a different set is running a different study, and the agreement statistic becomes meaningless.

Freeze the corpus before coder 1 begins. If an artifact is added later, every coder re-runs or the addition is excluded.

| artifact | format | scope | rows or items | frozen on |
|---|---|---|---|---|
| Gmail sweep, ATS and receipt phrases | txt or csv, raw message text | 2025-06-01 to 2026-08-29 | | |
| Gmail sent mail with attachments | txt or csv | same window | | |
| Google Calendar export | csv or ics | same window, 90 day blocks, no keyword filter | | |
| LinkedIn applied list | csv | all pages | | |
| Jobright tracker | csv | full export | | |
| Ladders applied list | csv or image | full list | | |
| Wellfound applications | csv or screenshots | full list | | |
| YC Work at a Startup | screenshots | applied roles | | |

## Retrieval is not coding

One agent performs retrieval and outputs raw artifacts verbatim. That agent may also serve as a coder, because seeing raw artifacts is exactly what every coder does. What breaks the design is a coder seeing another coder's rows or judgements.

The retriever emits artifacts, never rows. If the retrieval output contains a count, a category, or an interpretation, it is contaminated and cannot enter the corpus.

## Redaction

Message IDs and calendar IDs stay in the corpus, since coders need them for `evidence_id`. They never appear in published output.
