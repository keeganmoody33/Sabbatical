<!-- kit-meta
file: retrieval-log-059.md
created: 2026-08-30
source: adversarial review of the Cursor freeze headline block (C1–C9)
reviewed against: this freeze 298, freeze events, ORIGINS overlay, package/data/full-application-register.csv (321), package/knowledge/08-census-ledger.md, logs 032/035/038/044/049/051, LinkedIn DM match, QUERY-MANIFEST
method: set comparison both directions; interview-set audit of the 14; offer-language sweep on the authenticated mailbox; overlay key correction. Do not recode Freeze 1 or Freeze 2. Do not adopt 321 or 325.
-->

# Retrieval log 059

Red-team contact. Census remains **298 applications**. Interviewed applications remain **14**. Offers from the 298 remain **0** as a coded-outcome claim.

The review was written without this tree's `paper/RESULTS.md` or log 058. Both exist here. Challenges are answered against the corpus, not against those files as unseen. Where log 058 already closed a point, that is recorded.

Priority order as given: C4, C5, C1, C3, C2, then C7, C6, C9.

## C4. "Freeze 2 added 77 applications and zero interviews"

**Verdict: wording trap. Not a census contradiction.** The 77 are net-new `platform_log` **application** rows. They carry **no interview-set events**. That is true of 14/298. It is not a claim that LinkedIn produced no conversations.

The four named threads:

| name | this tree | interview in the 14? |
|---|---|---|
| Melavex | `melavex|founding-gtm-lead|c1` in the 298 (Freeze 2). LI-DM-043. Founder Antony Liu asked for a quick chat. Analysis: unclear if the call landed. Do not mint an interview. | No |
| The Hog / Hudson Liao | Opportunity, not one of the 77. Calendar interview 2026-06-16 already coded. Outside the 14. | No (outside the rate) |
| TrueBuilt | `truebuilt|gtm-engineer|c1` in the 298. Founder Jon Sibley rescoped FT to a project quote. Consulting, not an interview-set event. | No |
| AnyInt AI | Held application candidate. Not in the 298. | No |

Log 035's "three processes whose submissions existed nowhere else" (package log 038: Bask Health, BX Studio, The Hog) is a statement about **submission evidence**, not about interviews entering the 14. BX Studio and The Hog are opportunity on this tree. They cannot both falsify "zero interview-set events on the 77" and be outside the application register.

**Fix applied.** Headlines now say the 77 carry no interview-set events, and that this is not a claim about LinkedIn conversations. Melavex is not minted.

## C5. "The applications instrument did not see the work that paid"

**Verdict: the absolute version dies. The honest version is in the headlines.**

This codebook (rev 1) has no `converted_to_contract`. Package does. This tree did **not** carry the Mercor contract onto a census row. Package removal 4 did.

Mercor in this freeze:

- Six marketplace evaluator/expert receipts in the 298. No interview-set events. Did not convert.
- `mercor|growth-strategist|c1` is opportunity. Instant Work Offer states he did not apply directly. Cursor `offer` event `gth_04388c5d54511960`. Made money. Outside the 14.

TrueBuilt is in the 298. The 2026-07-15 rescope is a project quote. Not paid. Not an interview. Not on the money list.

**Rewrite in force:** the largest paid outcomes came through channels the applications instrument cannot treat as 14/298. Mercor marketplace rows are in 298 without conversion. TrueBuilt applied, then a quote, not paid. Do not write "none of the money is in 298."

## C1. 298 vs 325. Name the 27.

**Verdict: two assemblies, not two estimates of one quantity. The 27 is not 27 missing applications.**

| assembly | applications | companies | citation |
|---|---|---|---|
| This freeze | **298 applications** | 273 companies | `adjudication/applications__full_census.csv`. Freeze 1 221 + Freeze 2 77. |
| Package on disk | 321 | **298 companies** | `package/data/full-application-register.csv` |
| Package ledger after log 051 | 325 instructed | 298 companies plus four Jobright | `package/knowledge/08-census-ledger.md` |

**Collision warning, confirmed.** Package 321 spans 298 companies. This freeze's application count is also 298. Label the unit everywhere.

Naive 325 − 298 = 27 mixes "package 321 plus four Jobright" with this freeze **that already contains those four Jobright rows** (Axon KAE, Autodesk, MavenAI, Vanco). RevPartners is a fifth `jobright_agent` row here and already sits in the package 234 as gmail/ATS.

Arithmetic that produces 27 without naming holes:

- Gmail/ATS: package 234 vs Freeze 1 221. Net **13**.
- LinkedIn net: package 87 vs Freeze 2 LinkedIn 72. Net **15**.
- Jobright addendum: package +4 vs this freeze's 5 `jobright_agent` (the four plus RevPartners).
- 13 + 15 + 4 − 5 = **27**.

The 13 and the 15 are named in `adjudication/package_vs_census_delta.csv`.

**Freeze 1's 13 (package gmail/ATS extras):**

1. SBGA Remote Outside Sales Rep, 2025-04-11. **Out of this freeze window** (before 2025-06-01).
2. ThriveLink
3. micro1
4. saveurdays
5. Celonis
6. Gong.io
7. graph.one
8. Leidos Systems
9. Meshy
10. New Relic
11. Rippling Software Engineering Manager, Banking
12. SmartMode AI
13. Spot AI

Those 12 unmatched plus SBGA are the stratum gap. They are not silently added to 298. Several have blank dates and unspecified roles in the package register.

**Freeze 2's LinkedIn extras (15):**

- 12 held LinkedIn candidates: Datricks, Bitovi, ScoutLab.io, JetBridge AI ×2, Abacus.AI, Brainfish, ClosedWon Talent, SWARM, Insignia Assets, Stealth Startup, Kana. Subject has not confirmed these as applications.
- 3 opportunity on this tree: BX Studio, COLOSSUS TECHNOLOGY GROUP, The Hog (YC F25).

**Aliases and splits (not holes):** Cursor = Anysphere; Cincinnatus = Mercor biology; Bluejay = HartleyCo `underlying_employer`; Montauk Capital / Crossing Hurdles intermediary split.

**Census-only Jobright already in 298:** Autodesk, MavenAI, Vanco, Axon KAE. Adding them to reach 325 would double-count.

**Census-only Freeze 2 LinkedIn:** 8X, Armanino, Block+Tackle.

This freeze does **not** cite `08-census-ledger.md` as its total, because that file is a different assembly's governing ledger. Protocol on that file is respected by not quoting 325 as this freeze's finding. The citation for 298 is `adjudication/applications__full_census.csv` and this log's delta file.

Do not recode Freeze 1 Gmail or Freeze 2 CSVs to absorb the 12 held LinkedIn rows or Pin/Hog.

## C3. The 14, Glytec, the four post-[S1] names, and log 049

**Verdict: the 14 is not stale. Rate proximity to 4.45 percent is explained, not inherited.**

Interviewed is derived from cursor events whose `event_type` is in {recruiter_screen, hiring_manager_interview, panel, technical_exercise, final_round} intersected with the 298. `derive_metrics.py` does not read coder `confirmed`.

| name | in the 14? | why |
|---|---|---|
| Glytec | **No** | Opportunity. `glytec|unspecified|c1` is not in the 298. CEO-initiated. Correctly out. |
| Dagster Labs | **Yes** | `dagster-labs|gtm-engineer|c1`. Hiring manager interview 2026-04-03. |
| Hypergen | **Yes** | `hypergen|gtm-engineer|c1`. Interview invitation 2026-04-14. |
| Orchestry | **Yes** | `orchestry|gtm-engineer-sales|c1`. Recruiter screens then decline. |
| Opsin | **No** | Opportunity. James Pham freeze3. Not an application. |

Log 049 is the package meetings-to-classify pass. This freeze's Freeze 3 swept the personal calendar (338 events, Q8c). The 14 is post that sweep. Treating package log 049 as a missing pass that stale-dates the 14 is a cross-assembly error.

**4.70 vs 4.45.** 14/298 = 4.70 percent. Retired figure 11/247 = 4.45 percent. If the rebuild had inherited [S1]'s numerator, the rate would be 11/298 = 3.69 percent. It is 14. Freeze 2 added 77 applications and zero interview-set events, which **drops** the rate from 14/221 (6.33 percent) toward the retired figure from above. That is the opposite of copying the old 11. Do not restate 4.45 percent.

## C2. "Offers: 0" needs a search for offers

**Verdict: the coded zero stands. The offer-language family is closed on 33@lecturesfrom.com and not closed on keeganmoody33@gmail.com.**

`QUERY-MANIFEST.md` had no offer-language query. Q7 is interview language. Protocol: unharvested is not empty.

This tree's Q9 on keeganmoody33 is **done** (178 threads, log 032). That is receipt language including spam and trash, not offer language. Package gap 1 (Q9/Q10 unread at the ceiling) does not describe this freeze's personal-mailbox Q9.

**Q11 run 2026-08-30** on the authenticated Gmail MCP mailbox.

Mailbox identity: 33@lecturesfrom.com (messages are addressed to that account; `from:keeganmoody33@gmail.com` returns forwards into it). Personal mailbox keeganmoody33 is **not** connected this pass.

Queries, study window `after:2025/06/01 before:2026/08/30`, `includeTrash` true, `in:anywhere` on the second family:

- `"pleased to offer" OR "offer letter" OR "compensation package" OR "we are pleased to" OR "contingent offer" OR "job offer"`
- `"offer letter" OR "job offer" OR "we would like to offer" OR "pleased to offer you" OR "background check" OR "reference check" OR "compensation package" OR "start date is" OR "your start date" OR "instant work offer"`
- `subject:offer OR subject:"you've been selected" OR "welcome to the team" OR "onboarding packet"`

No further page token. Hits were marketing (GitHub Universe, Wix, Emergent, Idea Browser, Airtable, Replit, Nike, Serato, Medium, Accio) plus one employment-adjacent thread:

- AIT HOME DELIVERY, LLC background screening instructions (`gth_d9cd6181e69ae399`), 2025-11-17. Sterling/First Advantage as part of an application process. Not an offer letter. AIT is not in the 298. Not a GTM search offer.

**Known offer artifact already harvested on the personal mailbox:** Mercor Instant Work Offer, opportunity, "we know you didn't apply directly."

Publishable sentence: zero `offer_accepted` / `offer_declined` on the 298; Q11 on 33@lecturesfrom.com found no census-row offer letter; personal-mailbox offer-language family is still open. Unharvested on keeganmoody33 is not empty.

## C6. Doug keyed unknown, company resolved

**Verdict: ruling out of the rate was already right. The key was wrong. Fixed.**

Log 044: Doug Shankman, **Renoir**, `renoir.one`, 2025-10-27, counterparty-booked, 15 minutes, no outcome artifact. Overlay was `unknown|cro-idea-doug-shankman|c1` after log 058 (predates AICRO). `unknown` in a dedupe key is a merge hazard.

Now `renoir|informal-cro-idea|c1`. `company_canonical = Renoir`. AICRO is later identity in notes (`tok_53b6c592660c`). `underlying_employer` is not AICRO: AICRO did not exist at the meeting date. Register still opportunity. Not in 298. Not in the 14.

**Two AICRO application rows are two cycles, not a twin:**

- `aicro|gtm-engineering-team-lead|c1`, email 2026-02-06
- `aicro|gtm-engineer|c1`, LinkedIn, package match LI-045 `distinct_cycle_net_new` dated 2026-05-25

Do not merge Doug into either.

## C7. 124 still_open and no no_response

**Verdict: A2 was not applied on Freeze 1. Do not recode. Do not import package 101.**

This codebook lists `no_response` and `still_open` as distinct terminal outcomes. Package codebook rev 2 adds A2's outbound-anchor rule and `evidenced_silence_days`. This freeze's Freeze 1 closes on 221: 73 `rejected_no_interview`, 6 `rejected_after_interview`, 18 `role_paused_or_closed`, **124 `still_open`**. Zero `no_response`. The 77 platform rows are blank.

If those 124 are published as still open, that is a coding choice from Freeze 1, not a measured ghosting count. `evidenced_silence_days` is uncomputable on this freeze. Package "101 of 200 received no reply" is **not** this freeze's finding.

Defensible on Freeze 1 only, and not as a full-census percent: 73 of 221 received an explicit decline before interview.

Do not recode the 124 in this pass.

## C8. Stronger numbers from the package ledger

**Verdict: those figures are package-assembly findings. Do not print them as this freeze's.**

| package claim | this freeze analogue |
|---|---|
| 51 of 325 cannot be laned | Freeze 1 `role_lane = unspecified` is 35/221. Not one in six of 325. |
| Agent-submission blind spot 3 of 31 | Jobright's four net-new are already inside 298. Blind spot size is not restated from [S1]. |
| Sweep added 78 and roughly zero GTM engineering | Do not print 108/247 or 106/325. [S1] is unreproducible here. |
| Seven probes, seven finds | Completeness is still unmeasured. `09-locked-headline` is package. |

## C9. Naming pass

**Verdict: not decided. Flagged.**

Working record names Mixmax, Mercor, Mobb, Kivira.health, BCOFA. `01-engagement.md`: companies are named throughout the ledger; anything published needs a naming pass. Package `04-engagements.md`: names stay in the working record; the paper is drafted against redaction-safe labels.

Package log 027: Mixmax exit involves a disputed final invoice. That is a sensitivity flag, not a naming question. Do not publish the dispute without Keegan's explicit decision.

This pass does not invent publication aliases.

## What changed in the corpus this log

- Overlay Doug retargeted to `renoir|informal-cro-idea|c1`
- Headlines in `paper/RESULTS.md` qualified for C4, C5, C1 unit label, C2, C7
- `adjudication/ORIGINS.md` money claim rewritten
- `adjudication/package_vs_census_delta.csv` written
- Q11 added to `QUERY-MANIFEST.md`

Census still 298. The 14 unchanged. Freeze 1 and Freeze 2 CSVs not recoded.
