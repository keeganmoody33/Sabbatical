# Freeze 3 personal Gmail and Calendar

Freeze 1 Gmail extracts and Freeze 2 platform files were not recoded.

This freeze adds the remaining personal-mailbox queries and an unfiltered sweep of keeganmoody33@gmail.com primary calendar.

## Retrieval

| query | status | threads or events |
|---|---|---|
| Q7 re-run from start | exhausted | 195 unique threads |
| Q6 sent, no attachment | exhausted | 3 threads |
| Q9 anywhere including spam and trash | exhausted | 178 unique threads |
| Q3b reconstructed remaining domains | exhausted | 183 unique threads |
| Q8c primary calendar, 90-day blocks | exhausted | 338 events |
| Pressure-test name and domain searches | done | log 034 |

MCAT PREP and SI CHM222 calendars were listed and not swept.

## Coding

Coder `freeze3`. One documented extract of new artifacts. Not a second independent LLM pair. Role-lane kappa is not recomputed.

### New rows with `register = opportunity`

These stay out of the application census.

| company | role | interviewed | terminal |
|---|---|---|---|
| Pin | unspecified | yes, Erica 2025-06-30 then Conor 2025-07-07 | rejected_after_interview 2025-07-07 |
| Hotglue | BDM Role | yes, 2026-04-20 | still_open |
| Opsin | unspecified | yes, James Pham 2026-03-13 | still_open |

No ATS submission receipt exists for those three. They do not enter the 298.

### Calendar corroboration on existing rows

| application_id | new event | already interviewed in Freeze 1 |
|---|---|---|
| beautiful-ai\|unspecified\|c1 | gcal Interview with beautiful.ai 2026-03-17 | yes |
| every-to\|gtm-engineer\|c1 | gcal 30 min with Austin 2026-04-21 | yes |
| phrasiq\|unspecified\|c1 | gcal GTM Deep Dive 2026-04-15, occurrence now evidenced | yes |
| the-hog\|gtm-engineer\|c1 | gcal Hudson Liao 2026-06-16 | yes, opportunity |
| glytec\|unspecified\|c1 | gcal Clayton Maike 2026-01-27 | yes, opportunity. No submission receipt |

### Exclusions added

- BCOFA: consulting_prospect
- TrueBuilt GTM project quote: consulting_prospect (the LinkedIn applied-list GTM Engineer row stays in Freeze 2)
- Mobb.dev: employment onboarding, not a search application
- Mixmax Heath meeting: marketplace_profile, same decision as Freeze 1
- Kivira weekly outbound: consulting_prospect, same decision as Freeze 1

## Census

- Freeze 1 application census: 221
- Freeze 2 full census: **298**
- Freeze 3 net-new `register = application` rows: **0**
- Interviewed applications: **14** (14/298)
- Opportunity-register interviews (Pin, Hotglue, Opsin, The Hog, Glytec, WorkOS, and others) stay outside that rate

Capture recapture was not computed. The LinkedIn file still lacks an Easy Apply versus external ATS label.

## Judgement calls

1. Pin has no submission artifact, so it is opportunity even though two interviews and a rejection exist.
2. Opsin recruiter called the Pham meeting a video interview and a later take-home the 2nd round. Round_number on the Pham event is 1 because no earlier interview event is in the corpus.
3. TrueBuilt LinkedIn applied-list GTM Engineer and the July GTM project quote are not merged. Different artifact classes.
4. Mobb is excluded rather than coded as an application. Gusto first-day and a Mobb employment mailbox are employment, not a search cycle.
5. Glytec stays opportunity. Clayton Maike is on the personal calendar the same day as the interview logistics thread. That does not mint a submission.
