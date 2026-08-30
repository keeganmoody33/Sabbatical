# Template 3. Two-register funnel split

**What this proves you can do:** spot denominator contamination before it flatters your numbers, and design a schema that makes the contamination impossible rather than merely discouraged.

**Extracted from:** `knowledge/00-core.md:62-69`, `prompts/extraction.md` rule 7, `adjudication/ADJUDICATION.md:18-19` and `:32-34`.

**One-line form:** Split `{{ALL_RECORDS}}` into `{{PRIMARY_REGISTER}}` and `{{SECONDARY_REGISTER}}` using `{{ORIGINATION_TEST}}`, bounded by `{{HARD_EVIDENCE_REQUIREMENT}}`, and report `{{RATE}}` with BOTH its denominator and its numerator restricted to `{{PRIMARY_REGISTER}}`.

---

## The problem it solves

A funnel rate is a fraction. Everyone argues about the numerator. The denominator is where the lying happens, and usually nobody is lying on purpose.

In the source study, some interviews came from applying. Others came from referrals, recruiter outreach, and matching-platform contracts, where no application was ever submitted. Those second ones produced real interviews and real revenue. Counting them in an application-to-interview rate would make applying look more effective than it is, because the outcome did not come from applying (`knowledge/00-core.md:67`).

The generalizable statement, and the reason this is worth stealing:

> "A job search has two independent pipelines, and mixing them makes both unmeasurable." (`knowledge/00-core.md:69`)

Replace "job search" with any funnel that has both an outbound motion and an inbound or referral motion. Which is most of them.

---

## The template

```
You are separating {{ALL_RECORDS}} into two registers before any rate is
computed. Both registers stay in the dataset. Only one is a denominator.

PRIMARY REGISTER, {{PRIMARY_REGISTER}}:
  Records where {{ORIGINATION_ACTOR}} initiated the process by
  {{PRIMARY_EVENT}}. This is the ONLY denominator for {{RATE}}.

SECONDARY REGISTER, {{SECONDARY_REGISTER}}:
  Records where the process began through {{INBOUND_PATHWAY_LIST}} and
  {{PRIMARY_EVENT}} never happened. These produced real outcomes. They are
  tracked, reported, and never mixed into {{RATE}}.

THE ORIGINATION TEST, applied to every record:
  Is there an artifact showing {{ORIGINATION_ACTOR}} performed
  {{PRIMARY_EVENT}}?
    YES  -> {{PRIMARY_REGISTER}}
    NO   -> {{SECONDARY_REGISTER}}

  A downstream artifact is NOT an origination artifact. {{DOWNSTREAM_LIST}}
  prove a process existed. They do not prove {{PRIMARY_EVENT}} happened.

WHEN IN DOUBT:
  Assign {{SECONDARY_REGISTER}}. Under-counting the primary register makes
  {{RATE}} conservative. Over-counting makes it wrong in the flattering
  direction, which is the direction nobody catches.

REPORTING:
  - The numerator MUST be intersected with {{PRIMARY_REGISTER}} ids before
    the rate is computed:
        numerator = {ids with a qualifying outcome} INTERSECT
                    {ids in {{PRIMARY_REGISTER}}}
    Moving a doubtful record to {{SECONDARY_REGISTER}} removes it from the
    denominator. Its outcomes stay visible in the interaction table, so a
    numerator counted straight off that table still includes them, and the
    rate goes UP. Without this intersection, "when in doubt, exclude" is
    not conservative. It is the opposite.
  - Report {{RATE}} as an unreduced fraction against
    {{PRIMARY_REGISTER}} only.
  - Report {{SECONDARY_REGISTER}} as a separate parallel track with its own
    outcomes.
  - Never publish a combined rate. If someone asks for one, give them both
    fractions and let them do the arithmetic in the open.
```

---

## Two worked decisions from the source data

Both of these were live disagreements between two independent coders, resolved in a named pass (`adjudication/ADJUDICATION.md:18-19`).

**The Hog.** An interview invitation on 2026-06-15, the interview on 2026-06-16, and a roughly four-hour take-home exercise sent on 2026-06-18 (`artifacts/gmail/retrieval-log-021.md`). No submission receipt anywhere. One coder called it an application, at medium confidence, and flagged its own doubt. The other called it an opportunity. Adjudicated: **opportunity**. The stated reason is the whole template in one sentence:

> "Interview plus take-home do not mint an application row."

The interview events survive in `coding/bravo/events__bravo.csv`. The application row does not. So the interview is visible in the dataset and absent from the denominator, which is exactly right, and which is also exactly the trap the intersection rule above exists to close.

The source repository closes it. `adjudication/adjudicate.py:102-108` computes the numerator by walking both coders' event tables and keeping only events whose id is in `census_ids`. That single condition is what makes the exclusion conservative rather than inflationary.

The numbers show it working. Across both coders, 21 distinct records carry an event with a qualifying interview type. Fourteen of them are in the census. The seven that are not include The Hog. So the published rate is 14/221, and a numerator counted straight off the event tables would report 21/221, which is 0.0950 against 0.0633. The denominator shrank and the rate would have grown by half.

**BX Studio.** A video forwarded to a hiring manager. Coded application by one coder, opportunity by the other. Adjudicated **opportunity**: "Video forwarded to a hiring manager is not a submission."

Ten processes ended up in the secondary register in this freeze (`adjudication/ADJUDICATION.md:34`): WorkOS, Mercor, ThriveLink, Dexian, Luzmo, Glytec, SmartMode AI, Crossing Hurdles, micro1, and Pinterest. None of them counts in the 221.

Mercor is the one to look at. It is a matching-platform contract path that converted to paid work, and it is held out of the application census anyway, because the money did not come from applying.

## Adapting it

| Placeholder | Source study | A sales team's version |
|---|---|---|
| `{{PRIMARY_REGISTER}}` | application | self-sourced outbound |
| `{{SECONDARY_REGISTER}}` | opportunity | inbound, referral, partner-sourced |
| `{{PRIMARY_EVENT}}` | a submission the candidate made | a first-touch the rep made |
| `{{DOWNSTREAM_LIST}}` | interview invites, rejection letters, take-homes | a booked meeting, a demo request |
| `{{RATE}}` | application-to-interview | outbound-to-meeting |

## What breaks if you skip it

Your best-performing channel is whichever one you accidentally let into the denominator, and you will not find out for a year.

The contaminating rows tend to be the ones with the *good* outcomes, which is why nobody catches this. In the source study, Mercor sits in the secondary register and converted to paid work (`adjudication/ADJUDICATION.md:34`). A separate prior audit, whose figures this freeze deliberately does not restate, recorded seven such opportunities of which three converted (`knowledge/02-current.md:54`). Either way the shape is the same: merging the registers would raise the reported conversion rate using outcomes the measured activity did not produce.
