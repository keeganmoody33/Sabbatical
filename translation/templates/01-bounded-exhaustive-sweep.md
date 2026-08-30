# Template 1. Bounded exhaustive sweep

**What this proves you can do:** define "I have looked everywhere" as a condition a machine can check, instead of a feeling you have when the results stop looking new.

**Extracted from:** `QUERY-MANIFEST.md`, `artifacts/gmail/retrieval-log-001.md` through `-029.md`, `knowledge/protocol.md:69`.

**One-line form:** Search `{{SOURCE}}` for `{{SIGNAL_SET}}`, bounded by `{{WINDOW}}` and split into `{{SUB_WINDOWS}}`, terminated by `{{EXHAUSTION_CONDITION}}`, and output `{{QUERY_LEDGER}}`.

---

## The template

```
You are running an exhaustive retrieval sweep. You are not filtering, judging,
or counting. Your only job is to prove coverage.

SOURCE: {{SOURCE}}
WINDOW: {{START_DATE}} to {{END_DATE}}, {{TIMEZONE}}, inclusive

Run each query below. For every query, record:
  - a stable query id
  - the query intent in plain language, not just the raw string
  - the window it covered
  - the termination state: done, incomplete, or blocked
  - the yield (how many records came back)
  - which output log holds the results

A query is `done` ONLY when {{EXHAUSTION_CONDITION}}.
It is `incomplete` when the source still offers more and you stopped.
It is `blocked` when you could not run it at all. Name the blocker inline.

QUERIES:
1. Known-sender sweep. Search for {{PHRASE_SET}} from {{KNOWN_DOMAIN_LIST}}.
2. Discovered-sender sweep. Re-run query 1 with any sender domain that
   appeared in query 1 results and was not in {{KNOWN_DOMAIN_LIST}}. Repeat
   until no new domains appear.
3. Negative-language sweep. Search for {{OUTCOME_PHRASE_SET}} with no sender
   filter, minus {{NOISE_DOMAIN_LIST}}. This catches records whose sender you
   never learned.
4. Own-output sweep. Search {{OUTBOUND_SOURCE}} for {{OUTBOUND_PHRASE_SET}}.
   What you sent is evidence too.
5. Unfiltered block sweep. For {{SECONDARY_SOURCE}}, sweep the full window in
   {{BLOCK_SIZE}} blocks with NO keyword filter at all.

RULES:
- If {{WINDOW}} is long enough that a single query paginates past
  {{PAGE_LIMIT}}, split it into sub-windows with a one-unit overlap at each
  boundary. Overlap costs duplicates. A gap costs records.
- Never filter by the obvious keyword on {{SECONDARY_SOURCE}} without also
  running the unfiltered block sweep. See the note below.
- Record zero-result queries. A query that returned nothing is coverage.
- Do not deduplicate, classify, or count during retrieval. That is a
  separate pass with separate rules.

STOP RULE:
Retrieval is exhaustive when every query returns {{EXHAUSTION_CONDITION}} on
every source, AND a final pass over newly discovered senders returns nothing
new. If that rule is not met, say so explicitly and list what is still open.
Do not describe a partial sweep as complete.

OUTPUT: a query ledger table, plus one raw log per query.
```

---

## Why the unfiltered block sweep is in there

This is the part worth stealing even if you take nothing else.

The original study searched its calendar for the word "interview" and got zero events (`knowledge/protocol.md:69`). Not few. Zero. Interview loops lived inside Ashby and Google Meet invites with generic titles like "30 minute meeting", so the obvious keyword matched nothing.

The fix was to stop filtering. Sweeping the full window in 90-day blocks with no keyword at all returned 31 events (`artifacts/calendar/q8-lecturesfrom-primary.csv`).

The general lesson: when you search for a thing by its name and get zero, the two explanations are "it is not there" and "it is not called that". Only an unfiltered sweep tells you which.

## Adapting it

- `{{KNOWN_DOMAIN_LIST}}` in the original was 12 ATS sender domains: greenhouse.io, ashbyhq.com, lever.co, myworkday.com, workable.com, icims.com, jobvite.com, breezy.hr, teamtailor.com, recruitee.com, rippling.com, smartrecruiters.com. Query 2 discovered four more. Swap the whole list for your own stack.
- `{{EXHAUSTION_CONDITION}}` was "the API returns no `nextPageToken`". Any source with cursor pagination gives you an equivalent. A source without one needs a different condition, and you should state what it is.
- `{{BLOCK_SIZE}}` was 90 days, chosen to stay under the calendar API's result cap.

## What breaks if you skip it

You get a number with no coverage story attached. The original study's own prior audits searched only from 2025-08-25 forward, which made five months look empty when they were merely unsearched. `knowledge/protocol.md:18` names the distinction: "unharvested rather than empty". Without a query ledger you cannot tell those two apart, and neither can anyone reading your result.
