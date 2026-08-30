# Retrieval log 018

Query Q4, rejection and closure language that need not contain the word "application":
`{"move forward with other candidates" "moving forward with other candidates" "position has been filled" "pursue other candidates" "not be moving forward" "decided to move forward with" "other applicants" "no longer under consideration" "regret to inform"} -from:substack.com -from:ziprecruiter.com`

Window 2025-06-01 to 2026-08-30. Page 1 of n. `nextPageToken` for page 2: `tok_0febae1f78a8`. Result count estimate 201. Returned this page: 50 threads.

## Artifacts not previously captured

| date | sender | subject | thread_id |
|---|---|---|---|
| 2026-08-04 | no-reply@lattice.com | Lattice, Update on the GTM Engineer role (position filled) | gth_5d12791102226fed |
| 2026-07-23 | eml_0a253147bb65 | **Update on the Founding GTM Role at Bluejay** (declined after process) | gth_2961922ee1e05822 |
| 2026-06-25 | recruiting.echo.newtonsoftware.com | Lead, Agentic Operations + GTM Engineering at RevSpring | gth_272cbf95970f4335 |
| 2026-04-25 | eml_a6197bff6164 | **Re: Digital Product Builder, Thank You** (Switchyards, declined) | gth_9a641357cd288f9d |
| 2026-04-03 | eml_d3df7b160e39 | **Dagster Labs follow-up** (2 msg thread, includes SENT: "thank you for taking the time to chat with me") | gth_1c8ae3fa0432b375 |
| 2026-03-30 | no-reply@pandadoc.com | We got it (PandaDoc GTM Engineer application received) | gth_02ae1915406326ae |
| 2026-03-27 | eml_87e77a84a157 | Orchestry GTM Engineer (Sales) update, declined after interview process (2 msgs, includes SENT) | gth_0051fcbedbb7f591 |

Previously captured rejections re-surfaced by this query, confirming the phrase set works: OpenObserve, Great Question, RevPartners (x2), IBM, Clutch, Hyperbound, Toast, HUD, jobmail.io Growth Lead, WireScreen, MinIO, Enlace Health, Cloudflare, Wealth.com, Adaptive6, Boulevard, ServiceTrade, ApartmentIQ, CoLab, Airtable, FOSSA, Unframe, Teleport, Ontra, Rula, Sur, Sardine, G2, Tapcheck (x2), DISQO, Beautiful.ai, Ambrook, Foursquare, Vonage, Agroknow, Crypto.com, Fullsteam.

One false positive: `eml_6dfb8c5aaa49` "We Regret to Inform You…", an automotive parts promotion.

## Retriever notes

- **The HartleyCo client is Bluejay.** The 2026-07-23 message from Josh Kelly declines the Founding GTM role at Bluejay after Keegan went "through the process." The prior ledger carries this as "Confidential client via HartleyCo" with the underlying employer unknown, and the Interviews sheet lists it as a confidential client. The employer is now named.
- **Dagster Labs interviewed him.** Delaney Housley wrote on 2026-04-03 thanking him for taking the time to chat and declining. The prior ledger records Dagster Labs as a receipt only, and the Interviews sheet does not list it.
- **Switchyards appears twice, a year apart, for different roles.** Launch Manager, declined 2025-08-19, and Digital Product Builder, declined 2026-04-25. Only the first was in the corpus before this query, and neither is in the prior ledger.
- **PandaDoc's receipt exists after all.** `no-reply@pandadoc.com` sent "We got it" on 2026-03-30, the same day as the Greenhouse security code. The retriever's inference in log 006 that no receipt existed was wrong on both counts: the application completed and the receipt was sent, just from the employer's own domain rather than Greenhouse's.
- Orchestry's decline confirms an interview process concluded on 2026-03-27, consistent with the recruiter screens and no-show found in log 006.
- This query is doing exactly what it was designed for. Every rejection it surfaces that uses none of the Q1 phrases is an application the earlier sweep could not have seen from the rejection side alone.
