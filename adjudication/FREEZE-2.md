# Freeze 2 platform ingest

Freeze 1 Gmail and Calendar extracts were not recoded.

- Jobright tracker rows coded as applications: 40
- LinkedIn applied-list rows coded (including opportunity): 98
- Platform exclusions: 1
- Platform rows overlapping Freeze 1 applications: 56
- Net-new platform_log applications: 77
- Ambiguous, matched more than one Freeze 1 row, held out of the census: 0
- Of those, overlaps whose parent is unresolved and therefore unnamed: 1
- Freeze 1 application census: 221
- Full census (Freeze 1 plus net-new): 298
- Interviewed in Freeze 1 (cursor events, application register): 13
- Interviewed in full census: 13 (platform files carry no interview events)

Capture recapture was not computed. The LinkedIn file is pages 1 to 10 of an applied list and does not label Easy Apply versus external ATS. LinkedIn submission_channel is therefore unknown.

No platform row matched more than one Freeze 1 row under token-prefix equivalence, so no row is ambiguous in this freeze. The status is emitted rather than folded into net-new so that a later run cannot count an unresolved possible duplicate as a new application.

1 overlap rows matched more than one Freeze 1 row on the exact key or the unspecified-role fallback. These are overlaps either way, so the census is unaffected, but the parent attribution is a choice among candidates rather than a lookup. `role_key` omits cycle, so two cycles of one company and role collapse to a single key, which is the same collision `paper/DEFECTS.md` records for the dedupe key. Naming one of several equally eligible parents in `parent_id` would assert a resolution that does not exist, and a reader joining on that field would never see the choice. So these carry `match_status = overlap_parent_ambiguous`, an empty `parent_id`, and every candidate in `candidate_parent_ids`. They still count as overlap, so the census is unaffected. Fields that agree across all candidates stay populated, because those are not in doubt:

- `fossa|gtm-engineer|c1` matched fossa|unspecified|c1 and fossa|unspecified|c2. Both are equally eligible, so no parent is named.

Five platform titles matched Freeze 1 as the same opening: Thomson Reuters AE Tax or Risk, Foursquare AE New Business, UpGuard SDR Manager, Verkada Enterprise Solutions Engineer Atlanta, and Listen Lead GTM Engineer (LinkedIn lists Listen, Freeze 1 uses Listen Labs). They are overlap, not net-new.

## Net-new applications

| company | role | source | channel |
|---|---|---|---|
| 2X | GTM Engineer | linkedin | unknown |
| 8X | GTM Engineer | linkedin | unknown |
| AICRO | GTM Engineer | linkedin | unknown |
| Ailytics | Revenue Operations (RevOps) Specialist | linkedin | unknown |
| Armanino | AI Factory, Value Engineer | linkedin | unknown |
| Autodesk | Sr. Sales Specialist, Fusion Enterprise | jobright | jobright_agent |
| Axon | Key Account Executive | jobright | jobright_agent |
| Bask Health | Sales Engineer | linkedin | unknown |
| Baton AI | Founding GTM | linkedin | unknown |
| Block+Tackle | Forward Deployed Marketing Engineer | linkedin | unknown |
| CRMIT Solutions | AI Solutions Sales Specialist | linkedin | unknown |
| Casper Studios | GTM Engineer | linkedin | unknown |
| Company.ai | GTM Sales Lead | linkedin | unknown |
| Coverwatch | Founding GTM | linkedin | unknown |
| Crash Override | Growth Engineer | linkedin | unknown |
| Crossing Hurdles | GTM Lead | linkedin | unknown |
| Databar.ai | GTM Engineer (Growth & Sales) | linkedin | unknown |
| DevSignal | Growth Specialist | linkedin | unknown |
| Doomers AI | Founding GTM | linkedin | unknown |
| DripShop | Growth Lead - User Acquisition | linkedin | unknown |
| Duckbill | Founding Sales / GTM | linkedin | unknown |
| Durham Geo Slope Indicator (DGSI) | Technical Sales Engineer | linkedin | unknown |
| Elios | Senior Forward Deployed Engineer | linkedin | unknown |
| Entelligence.AI | Founding GTM | linkedin | unknown |
| Evolution USA | Forward Deployed Engineer (FDA Applied AI / GenAI) | linkedin | unknown |
| Flexbone | Founding GTM Account Executive | linkedin | unknown |
| Fractional Demand | GTM Engineer | linkedin | unknown |
| Franklin Fitch | AI Training and Adoption Consultant | linkedin | unknown |
| Freshtix | Business Development Manager | jobright | unknown |
| Greenway Collins | GTM Engineer | Remote (US) | linkedin | unknown |
| GridBank | GTM Engineer | linkedin | unknown |
| Hartfiel Automation | Sales Engineer | linkedin | unknown |
| Hermetic AI | Sales Development Representative - Atlanta, GA | linkedin | unknown |
| Hippocratic AI | Deployment Strategist | linkedin | unknown |
| HorizonAI Talent | Forward Deployed Engineer | linkedin | unknown |
| Human Delta | Founding GTM Engineer | linkedin | unknown |
| IntelliPro | Founding Sales - AI Generic | linkedin | unknown |
| Inworld AI | GTM Lead | linkedin | unknown |
| Jobright.ai | AI Engineer | linkedin | unknown |
| Kognitos | Senior Solutions Engineer | linkedin | unknown |
| Light Labs | GTM Engineer, Agents | linkedin | unknown |
| Logicbroker | AI GTM Engineer | linkedin | unknown |
| Lyra Health | Senior GTM Enablement Specialist | linkedin | unknown |
| MAJC | Revenue Operations & Business Development | linkedin | unknown |
| MICHELIN Connected Fleet | Demand Generation and Growth Marketing Manager | linkedin | unknown |
| Massive | GTM | linkedin | unknown |
| MavenAI | GTM Engineer | jobright | jobright_agent |
| Melavex | Founding GTM Lead | linkedin | unknown |
| Method Recruiting, a 3x Inc. 5000 company | Founding GTM Engineer | linkedin | unknown |
| NetRise | Go To Market (GTM) Engineer / Outbound Pipeline Development | linkedin | unknown |
| Nudge AI | Growth Lead | linkedin | unknown |
| Pegasystems | GTM GenAI Product Owner | linkedin | unknown |
| Pickering Interfaces | Field Sales Engineer - Southeast | linkedin | unknown |
| Piper AI | Growth & Content | linkedin | unknown |
| Propel | Founding Sales Engineer | linkedin | unknown |
| QuadSci.ai | Marketing GTM Engineer | linkedin | unknown |
| RTScale AI | Founding Growth Lead | linkedin | unknown |
| Recur Software | GTM Engineer | linkedin | unknown |
| RevPartners | RevOps Strategist | jobright | jobright_agent |
| RevPilots | GTM Engineer | linkedin | unknown |
| Ritz Instrument Transformers USA | Sales Engineer | linkedin | unknown |
| Robert Half | Go-To-Market Lead | linkedin | unknown |
| Roc Search | Founding GTM Strategy | linkedin | unknown |
| SOLAYA | GTM Engineer | linkedin | unknown |
| Scout Global | Forward Deployed Engineer | linkedin | unknown |
| Scout Global | Founding Sales Engineer | linkedin | unknown |
| Sidepocket | Go-To-Market Growth Engineer | linkedin | unknown |
| Solant | Generative AI Agent Engineer (Remote) | linkedin | unknown |
| Taste Labs | Growth Lead | linkedin | unknown |
| TechLinkSphere | Micro-SaaS Launch & Growth Engineer | linkedin | unknown |
| The Biological Computing Co. (TBC) | Lead Sales and Product Engineer | linkedin | unknown |
| The Vincit Group | Systems Engineering and Sales | linkedin | unknown |
| TrueBuilt | GTM Engineer | linkedin | unknown |
| Valoh | Fractional GTM Operations Lead | linkedin | unknown |
| Vanco | GTM Enablement Manager | jobright | jobright_agent |
| Verdent AI | Growth Marketing | linkedin | unknown |
| Vi | Sr. Forward Deployed Engineer | linkedin | unknown |
