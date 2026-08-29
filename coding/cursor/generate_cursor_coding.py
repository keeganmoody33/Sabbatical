#!/usr/bin/env python3
"""Independent coding by coder_id=cursor from the frozen artifact corpus.

Reads nothing from coding/alpha or coding/bravo.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

OUT = Path("/workspace/coding/cursor")
CODER = "cursor"


def slug(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return cleaned or "unspecified"


def aid(company: str, role: str, cycle: int) -> str:
    return f"{slug(company)}|{slug(role)}|c{cycle}"


APP_FIELDS = [
    "coder_id",
    "application_id",
    "cycle",
    "company_canonical",
    "company_as_listed",
    "underlying_employer",
    "role_as_listed",
    "role_lane",
    "gtm_modifier",
    "date_applied",
    "date_precision",
    "date_capture",
    "date_evidence_anchor",
    "discovery_source",
    "submission_channel",
    "ats_system",
    "evidence_tier",
    "evidence_class",
    "register",
    "terminal_outcome",
    "terminal_outcome_date",
    "terminal_outcome_precision",
    "location",
    "work_type",
    "level_as_listed",
    "salary_range_listed",
    "confidence",
    "notes",
]

EVENT_FIELDS = [
    "coder_id",
    "event_id",
    "application_id",
    "event_date",
    "event_date_precision",
    "event_type",
    "round_number",
    "counterparty_name",
    "counterparty_role",
    "medium",
    "evidence_system",
    "evidence_id",
    "notes",
]

EXCL_FIELDS = [
    "coder_id",
    "candidate_id",
    "date",
    "company",
    "role",
    "exclusion_reason",
    "what_would_promote_it",
    "evidence_system",
    "evidence_id",
]


# Compact application tuples. Empty string means not observed.
# (canonical, as_listed, underlying, role, lane, gtm, date, precision, anchor,
#  discovery, channel, ats, tier, register, outcome, outcome_date, work, level,
#  loc, conf, notes, receipt_tid)
APPS: list[tuple] = [
    ("Crypto.com", "Crypto.com", "", "Product Growth Hacker: Exchange & Main App", "growth_demand_marketing", "", "2025-08-05", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "rejected_no_interview", "2025-11-02", "unstated", "", "", "high", "Receipt 2025-08-05; 2025-11-02 Lever thank-you/decline of same role merged. Evidence IDs 1987abec68c6f639 and 19a45779c86938f1.", "1987abec68c6f639"),
    ("Fullsteam", "Fullsteam", "", "Senior Sales Development Representative", "sales_bd_partnerships", "", "2025-09-29", "evidence_bound", "2025-09-29", "unknown", "ats_direct", "Workday", "B", "application", "still_open", "", "unstated", "Senior", "", "medium", "Workday update not a first-receipt. Date is evidence-bound to the update.", "199972ac6d0a123f"),
    ("Anaconda", "Anaconda", "", "Senior BDR", "sales_bd_partnerships", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "Senior", "", "high", "Rippling receipt 2025-07-27; 2025-08-22 update thread 198d3b3bf3993a49 merged.", "1984b6a766e1d92f"),
    ("Sage", "Sage", "", "Director of Growth, Small", "growth_demand_marketing", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Director", "", "high", "careers.sage.com thanks-for-application 2025-08-04; 2025-09-03 update 1990fabad455beb5.", "19874db50c4ae6aa"),
    ("Ava Labs", "Ava Labs", "", "Growth Lead, Core", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Wellfound submission 19874eb54159ac4e. Employer thanks-for-interest 2025-08-14 198a9f80268b55a5 merged.", "19874eb54159ac4e"),
    ("ClassDojo", "ClassDojo", "", "unspecified", "unspecified", "", "2025-08-08", "evidence_bound", "2025-08-08", "unknown", "ats_direct", "Gem", "B", "application", "still_open", "", "unstated", "", "", "medium", "Gem update only. Role omitted.", "1988b0ce0d7e9ae5"),
    ("proteanTecs", "proteanTecs", "", "SDR", "sales_bd_partnerships", "", "2025-08-08", "exact", "", "unknown", "ats_direct", "Comeet", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19888824d442ae2c"),
    ("Beckhoff Automation", "Beckhoff Automation", "", "Sales Engineer", "sales_solutions_engineering", "", "2025-08-08", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2025-08-08", "unstated", "", "", "high", "Paycom incomplete notice 2025-08-07 then 2025-08-08 rejection thanking him for applying. Submission treated as completed that day.", "1988bb3318ed28b3"),
    ("Seamless.AI", "Seamless.AI", "", "SDR Remote US", "sales_bd_partnerships", "", "2025-08-05", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2025-08-07", "remote", "", "", "high", "Thank you 2025-08-05; status 2025-08-07 1988561b3341f748.", "1987ae68b5aee0d0"),
    ("Ambrook", "Ambrook", "", "Partnerships Lead", "sales_bd_partnerships", "", "2025-08-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from 2026 Business Operations Lead.", "1987cfcb64fc0b3c"),
    ("Blackthorn.io", "Blackthorn.io", "", "unspecified", "unspecified", "", "2025-08-05", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted on receipt.", "1987ab36c560b894"),
    ("Axon", "Axon", "", "Manager, Go-to-Market Readiness", "revops_gtm_ops_strategy", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2025-08-04", "unstated", "Manager", "", "high", "Apply then reviewed same day. Threads 198768a8edd78a10 and 198769522c958870.", "198768a8edd78a10"),
    ("4flow", "4flow", "", "Director, Go To Market Strategy", "revops_gtm_ops_strategy", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "Director", "", "high", "", "198768e9cb938b46"),
    ("ITC Infotech", "ITC Infotech", "", "Manager, Business Development", "sales_bd_partnerships", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Manager", "", "high", "", "198768c3e75ab651"),
    ("Fibr AI", "Fibr AI", "", "Founding SDR + AE", "sales_bd_partnerships", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "19874ec5b07b5475"),
    ("12100 Collective", "12100 Collective", "", "SEO Lead", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19874e996f09c1dd"),
    ("Infisical", "Infisical", "", "Founding Growth Marketer", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "19874e8276978aa8"),
    ("AirGarage", "AirGarage", "", "Consumer Growth Hacker", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19874e6f875e3d0e"),
    ("OnBoard", "OnBoard", "", "unspecified", "unspecified", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "1987276c3943fd47"),
    ("GTP Software", "GTP Software, Inc.", "", "Revenue Enablement Manager", "revops_gtm_ops_strategy", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Thank you 2025-07-27; named role on 2025-08-01 19866f31583b7516.", "1984b74316b2b6d9"),
    ("Weave", "Weave", "", "Business Development Manager", "sales_bd_partnerships", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_after_interview", "2026-08-18", "unstated", "", "", "high", "Greenhouse receipt 2025-07-27. sarah@weave.bio declined 2025-07-31 then Ashby 2026-08-18 thanks for meeting and interview. Long gap; one cycle because no second submission artifact.", "1984b6cd8216c3a8"),
    ("Hex", "Hex", "", "SDR", "sales_bd_partnerships", "", "2025-07-31", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "1985e2fcbbc5a557"),
    ("Phiture", "Phiture", "", "US Growth Lead, Mobile Marketing Strategist", "growth_demand_marketing", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "no-reply@phiture.com receipt; ariel.kowalczyk follow-up 2025-07-29.", "1984b79b760961bf"),
    ("Galileo", "Galileo", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2025-07-28", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from Growth Engineer 2025-07-02.", "1985321472fcbc46"),
    ("Slingshot AI", "Slingshot AI", "", "Conversation Designer", "product_ai_technical", "", "2025-07-25", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Thank you 2025-07-25; update 2025-07-28.", "198417c793254f3f"),
    ("Replit", "Replit", "", "Sales Engineer", "sales_solutions_engineering", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Follow-up 2025-07-30 1985bf4a7f1cded7.", "1984b7803d828099"),
    ("Stedi", "Stedi", "", "unspecified", "unspecified", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "1984b76f3129f436"),
    ("Shaped", "Shaped", "", "Founding SDR", "sales_bd_partnerships", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Dover", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "1984b7295c12359b"),
    ("Volley", "Volley", "", "unspecified", "unspecified", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "1984b6beef9627b2"),
    ("90 Seconds", "90 Seconds", "", "unspecified", "unspecified", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "1984b664dfc9c86d"),
    ("Exa", "Exa Labs Inc.", "", "Growth Lead", "growth_demand_marketing", "", "2025-07-25", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from June 2025 Exa product outreach.", "19843b40babe3689"),
    ("ScaleOps", "ScaleOps", "", "Sales Engineer, USA", "sales_solutions_engineering", "", "2025-07-17", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Spark Hire Recruit named in subject.", "19816fa4ed2957bf"),
    ("Classet", "Classet", "", "Head of GTM", "sales_bd_partnerships", "", "2025-07-09", "evidence_bound", "2025-07-09", "wellfound", "wellfound_apply", "none_observed", "B", "application", "rejected_no_interview", "2025-07-09", "unstated", "", "", "medium", "Wellfound update/decline. No separate submission receipt in corpus. Evidence-bound.", "197efe9bab3feb22"),
    ("Designit", "Designit", "", "unspecified", "unspecified", "", "2025-07-08", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "197ea85c50a5e246"),
    ("Applause", "Applause", "", "Enterprise SDR", "sales_bd_partnerships", "", "2025-07-08", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "rejected_no_interview", "2025-07-09", "unstated", "", "", "high", "Data copy 197e8533c3fb823c plus receipt/rejection 197e8563609b2b60.", "197e8533c3fb823c"),
    ("Headway", "Headway", "", "Growth Marketing Specialist", "growth_demand_marketing", "", "2025-07-03", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "197d047a6d227e74"),
    ("Galileo", "Galileo", "", "Growth Engineer", "growth_demand_marketing", "", "2025-07-02", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Different title from GTM Engineer 2025-07-28.", "197cbf50d42e42d4"),
    ("Gigs", "Gigs", "", "unspecified", "unspecified", "", "2025-06-30", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "197c324e2c6972a8"),
    ("Runway", "Runway", "", "Go-To-Market AI Engineer", "explicit_gtm_engineering", "ai_product_vertical", "2025-06-26", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "197a9b7e36f15a96"),
    ("Trace3", "Trace3", "", "SDR", "sales_bd_partnerships", "", "2025-06-25", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "role_paused_or_closed", "2025-06-25", "unstated", "", "", "high", "Opening filled on the application notice.", "197a864d4c88286e"),
    ("Circle", "Circle", "", "GTM Engineer, Outbound", "explicit_gtm_engineering", "sales_presales", "2025-06-20", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "1978fae6c43de77c"),
    ("Drata", "Drata", "", "SDR Remote", "sales_bd_partnerships", "", "2025-06-16", "evidence_bound", "2025-06-16", "unknown", "ats_direct", "Greenhouse", "B", "application", "still_open", "", "remote", "", "", "medium", "Update artifact, not a first receipt.", "197794fc216fb2ec"),
    ("Foursquare", "Foursquare", "", "AE New Business", "sales_bd_partnerships", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-01-08", "unstated", "", "", "high", "", "19b800cded020e8f"),
    ("SailPoint", "SailPoint", "", "Account Exec Enterprise Accounts", "sales_bd_partnerships", "", "2026-01-03", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "", "", "high", "Received 19b81f2c7de63f3d then thank you 19b8497068491dca.", "19b81f2c7de63f3d"),
    ("Proofpoint", "Proofpoint", "", "unspecified", "unspecified", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19b803c28687651e"),
    ("Thomson Reuters", "Thomson Reuters", "", "AE Tax or Risk", "sales_bd_partnerships", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "", "", "high", "JREQ195996. Update 2026-02-20 19c7a359b58ab0c0.", "19b801325a600eb1"),
    ("MediaLab.AI", "MediaLab.AI Inc.", "", "unspecified", "unspecified", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19b7cc5e65e62942"),
    ("Primer", "Primer", "", "unspecified", "unspecified", "", "2025-12-09", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2025-12-15", "unstated", "", "", "high", "Role omitted on both artifacts.", "19b04485943e8fdd"),
    ("Linear", "Linear", "", "AE Growth", "sales_bd_partnerships", "", "2025-12-08", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2025-12-11", "unstated", "", "", "high", "", "19afe3b978ef29ba"),
    ("Vonage", "Vonage", "", "SDR API/CPaaS", "sales_bd_partnerships", "", "2025-12-08", "evidence_bound", "2025-12-08", "unknown", "ats_direct", "Greenhouse", "B", "application", "rejected_no_interview", "2025-12-08", "unstated", "", "", "medium", "Status update declined. No earlier receipt in corpus.", "19b0016aed15e1ff"),
    ("Agroknow", "Agroknow", "", "North America Sales", "sales_bd_partnerships", "", "2025-11-25", "evidence_bound", "2025-11-25", "unknown", "unknown", "none_observed", "B", "application", "rejected_no_interview", "2025-11-25", "unstated", "", "", "medium", "Thank you for time and interest. No ATS receipt.", "19aba7c991e83d06"),
    ("Teleport", "Teleport", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-14", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-05-07", "unstated", "", "", "high", "", "19d89d00fa4cd01e"),
    ("Rollstack", "Rollstack", "", "AI Growth Hacker", "growth_demand_marketing", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d782b522666c50"),
    ("AirOps", "AirOps", "", "Growth Engineer", "growth_demand_marketing", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d76ecf6a22732c"),
    ("Cresta", "Cresta", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-10", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d76d01aa417859"),
    ("Auctane", "Auctane", "", "Pre-Sales Engineer", "sales_solutions_engineering", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-14", "unstated", "", "", "high", "Receipt omits role; decline names Pre-Sales Engineer.", "19d76cd69aa1a5ff"),
    ("Redis", "Redis", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d76c3b3e2ae594"),
    ("Ontra", "Ontra", "", "unspecified", "unspecified", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-24", "unstated", "", "", "high", "Role omitted on receipt.", "19d76be5511647d3"),
    ("LangChain", "LangChain", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d7586f3104286a"),
    ("Sur", "Sur", "", "AI Revenue Engineer", "explicit_gtm_engineering", "ai_product_vertical", "2026-04-09", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "rejected_no_interview", "2026-04-09", "unstated", "", "", "high", "", "19d7311fcb46666b"),
    ("Sardine", "Sardine", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-09", "unstated", "", "", "high", "", "19d6306f81d1fff8"),
    ("G2", "G2", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "role_paused_or_closed", "2026-04-09", "unstated", "", "", "high", "Position filled.", "19d3efd2db98f59f"),
    ("Fixify", "Fixify", "", "GTM Engineer (Contract)", "explicit_gtm_engineering", "plain", "2026-04-03", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Receipts 2026-04-03 and 2026-04-06 plus update. One cycle.", "19d539197b0eccec"),
    ("Pearl", "Pearl, Inc.", "", "Lead GTM Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "Ashby receipt plus later interview scheduling artifacts.", "19d639bd2d75a64a"),
    ("Valsoft", "Valsoft Corporation", "", "GTM Engineer, DockMaster", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Workable data copy 19d6386d8b135dd0.", "19d638eb381bdfd1"),
    ("Payabli", "Payabli", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d6374d64714d79"),
    ("Wrapbook", "Wrapbook", "", "GTM Systems Engineer", "explicit_gtm_engineering", "systems_operations", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "NDA request in confirmation.", "19d636da39acd54c"),
    ("AppGate", "AppGate Cybersecurity", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d630a32187eb2b"),
    ("Tapcheck", "Tapcheck", "", "unspecified", "unspecified", "", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-06", "unstated", "", "", "high", "Thank you 2026-03-30; second thank you and decline 2026-04-06 treated as one cycle.", "19d3f065b6c86f9d"),
    ("Solv Health", "Solv Health", "", "unspecified", "unspecified", "", "2026-04-06", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "rejected_no_interview", "2026-04-21", "unstated", "", "", "high", "Role omitted on receipt.", "19d63017a38b1d93"),
    ("Unframe", "Unframe", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-12", "remote", "", "", "high", "Second Greenhouse receipt 2026-04-17 merged as same opening. IDs 19d6301094a74ba5 and 19d9bc38883d43fc.", "19d6301094a74ba5"),
    ("Rula", "Rula", "", "GTM Engineer Remote", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-22", "remote", "", "", "high", "", "19d62ff8d5126fb6"),
    ("Liatrio", "Liatrio", "", "GTM RevOps Engineer", "explicit_gtm_engineering", "systems_operations", "2026-04-05", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d5ec03888c1dd9"),
    ("Virtru", "Virtru", "", "Director of Go-to-Market AI", "explicit_gtm_engineering", "ai_product_vertical", "2026-03-09", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-04-04", "unstated", "Director", "", "high", "Greenhouse thank you 2026-03-09; decline names the director role.", "19cd373c4ed544d6"),
    ("CompanyCam", "CompanyCam", "", "GTM Systems Engineer", "explicit_gtm_engineering", "systems_operations", "2026-04-03", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d539acd9491585"),
    ("Brand.ai", "brand.ai", "", "GTME", "explicit_gtm_engineering", "plain", "2026-04-02", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-04-07", "unstated", "", "", "high", "Sent mail to jana@brand.ai with portfolio. Comp discussion then rejection in same thread.", "19d4e5e256da787a"),
    ("Boulevard", "Boulevard", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-31", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-04", "unstated", "", "", "high", "", "19d45fc7e04c3dc4"),
    ("DISQO", "DISQO", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-31", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "rejected_no_interview", "2026-03-31", "unstated", "", "", "high", "Canonical DISQO not DSQO.", "19d45d67bebea78a"),
    ("PhrasIQ", "PhrasIQ", "", "unspecified", "unspecified", "", "2026-03-31", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Wellfound: application accepted, schedule interview. Role omitted. Calendar Discovery 2026-04-02. Relay mentions GTM System Deep Dive after Discovery Session.", "19d453fe2506a0f5"),
    ("Mento", "Mento", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Second thank you 2026-03-30 merged.", "19d1d7963478c31c"),
    ("Tiger Data", "Tiger Data", "", "GTM AI Engineer", "explicit_gtm_engineering", "ai_product_vertical", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-03-30", "unstated", "", "", "high", "", "19d3f415525c9364"),
    ("Vercel", "Vercel", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d3f09c5fd55395"),
    ("Roboflow", "Roboflow", "", "RevOps GTM Engineer", "explicit_gtm_engineering", "systems_operations", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d3f0327312df05"),
    ("Dagster Labs", "Dagster Labs", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_after_interview", "2026-04-03", "unstated", "", "", "high", "Receipt plus security-code resubmit same day. Delaney Housley thanked him for chatting 2026-04-03.", "19d3ef8798237401"),
    ("Unstructured", "Unstructured", "", "GTM Engineer, Operations", "explicit_gtm_engineering", "systems_operations", "2026-03-30", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d3ebf796ee1523"),
    ("PandaDoc", "PandaDoc", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-04-27", "unstated", "", "", "high", "Greenhouse security code plus no-reply@pandadoc.com We got it same day. Decline 2026-04-27.", "19d3f0236cb930e4"),
    ("Adapt", "Adapt", "", "GTM Engineer / RevOps Lead", "explicit_gtm_engineering", "systems_operations", "2026-03-27", "exact", "", "unknown", "ats_direct", "Dover", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19d305c5bd7e45ef"),
    ("Beautiful.ai", "Beautiful.ai", "", "unspecified", "unspecified", "", "2026-03-08", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_after_interview", "2026-03-26", "unstated", "", "", "high", "Role omitted on receipt. Interview process through at least 2026-03-19. Hiring manager Brandon Ness named in sent-mail thread.", "19ccb2322bf41b13"),
    ("Orchestry", "Orchestry", "", "GTM Engineer (Sales)", "explicit_gtm_engineering", "sales_presales", "2026-03-24", "exact", "", "unknown", "ats_direct", "Breezy", "A", "application", "rejected_after_interview", "2026-03-27", "unstated", "", "", "high", "Receipt, two recruiter-screen invites, missed interview, then post-process decline.", "19d1d7f5546fef70"),
    ("Pinterest", "Pinterest", "", "Apprentice Engineer", "product_ai_technical", "", "2026-03-25", "exact", "", "referral", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-04-28", "unstated", "Apprentice", "", "high", "Greenhouse application 2026-03-25. Distinct from June 2025 referral-accept messages which did not prove submission.", "19d2273d2d508ca1"),
    ("Hypergen", "Hypergen", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-11", "exact", "", "unknown", "ats_direct", "Recruitee", "A", "application", "still_open", "", "unstated", "", "", "high", "Confirmation then interview invitation 2026-04-14 from people@hypergen.io.", "19cdd6fb062a3cd8"),
    ("Anthropic", "Anthropic", "", "Software Engineer, Business Technology", "product_ai_technical", "", "2026-03-08", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-03-09", "unstated", "", "", "high", "", "19ccb1821c91f6e0"),
    ("SentiLink", "SentiLink", "", "Go-to-Market Strategy Analyst", "revops_gtm_ops_strategy", "", "2026-02-23", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-13", "unstated", "", "", "medium", "2026-02-23 thank you omits role. 2026-06-22 thank you. 2026-07-13 decline names Go-to-Market Strategy Analyst. One cycle.", "19c8bb6dffb8003a"),
    ("TestGorilla", "TestGorilla", "", "Go-to-Market Engineer", "explicit_gtm_engineering", "plain", "2026-02-20", "exact", "", "unknown", "ats_direct", "Teamtailor", "A", "application", "still_open", "", "unstated", "", "", "high", "Assessment invitation plus recruiter intro same day. Recruiter update 2026-04-23.", "19c7cb89ca3f84c5"),
    ("Smeetz", "Smeetz", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-02-20", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19c7c6278e50d7ad"),
    ("WilsonHCG", "WilsonHCG", "unknown", "Outbound Sales Consultant III", "sales_bd_partnerships", "", "2026-02-13", "exact", "", "unknown", "recruiter_submitted", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Agency thank you for application. Underlying employer unnamed. Distinct from later Dexian outreach on same title.", "19c54cd5aa16fc0d"),
    ("Ambrook", "Ambrook", "", "Business Operations Lead", "revops_gtm_ops_strategy", "", "2026-02-11", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-02-12", "unstated", "", "", "high", "Second Ambrook role. Followup_sent to no-reply after rejection.", "19c4aed736a76871"),
    ("GitLab", "GitLab", "", "GTM Planning & Operations Analyst", "revops_gtm_ops_strategy", "", "2026-02-10", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "role_paused_or_closed", "2026-04-17", "unstated", "", "", "high", "", "19c49ec3a2733b19"),
    ("Gather AI", "Gather AI", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-02-09", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19c405de94390d83"),
    ("Manifold AI", "Manifold AI", "", "Growth Marketing Manager", "growth_demand_marketing", "", "2026-02-06", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-02-06", "unstated", "", "", "high", "", "19c30a63128e9d4e"),
    ("Verkada", "Verkada", "", "Enterprise Solutions Engineer, Atlanta", "sales_solutions_engineering", "", "2026-02-04", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "Atlanta", "unstated", "", "high", "", "19c2849b7457a18e"),
    ("Beacon Software", "Beacon Software", "", "unspecified", "unspecified", "", "2026-01-26", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code then completed receipt 79 seconds later.", "19bf83553cbd0629"),
    ("Huzzle", "Huzzle", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Workable submitted successfully with data copy. Later Huzzle emails call an AI video interview required and also say talent pool. Coded as application from the Workable submission language.", "19e9214f255608aa"),
    ("Adaptive6", "Adaptive6", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-04", "exact", "", "unknown", "ats_direct", "Comeet", "A", "application", "rejected_no_interview", "2026-06-16", "unstated", "", "", "high", "", "19e920eb6b7b55f0"),
    ("4MindsAI", "4MindsAI", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Application #49830118.", "19e91037278affa0"),
    ("RevSpring", "RevSpring", "", "Lead, Agentic Operations + GTM Engineering", "explicit_gtm_engineering", "founding_senior_lead", "2026-06-04", "exact", "", "recruiter_inbound", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "Newton receipt 2026-06-04; duplicate 2026-06-23; LinkedIn recruiter approach 2026-05-29; recruiter screen request 2026-06-10.", "19e91027e41faf49"),
    ("Cloudflare", "Cloudflare", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-06-23", "unstated", "", "", "high", "", "19e90ffd1bc9ed7d"),
    ("Pogo Technologies", "Pogo Technologies", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "Gem", "A", "application", "still_open", "", "unstated", "", "", "high", "Gem 2026-06-04. Gem 2026-06-26 and Ashby 2026-07-08 are later receipts on the same title with no terminal outcome, so they stay on c1.", "19e90fa204f97711"),
    ("ServiceTrade", "ServiceTrade", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-05-29", "unstated", "", "", "high", "Role omitted on thank you.", "19e4b44fc00eaf2e"),
    ("CoLab Software", "CoLab Software", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Greenhouse thank you; hiring.colabsoftware.com Sales Engineer 2026-05-28.", "19e48971b300d9ad"),
    ("Apollo.io", "Apollo.io", "", "unspecified", "unspecified", "", "2026-05-28", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Two identical receipts 62 seconds apart. Role omitted.", "19e6c874ef395028"),
    ("Airtable", "Airtable", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-05-21", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-05-27", "unstated", "", "", "high", "", "19e483d68ffad276"),
    ("Pindrop", "Pindrop", "", "GTM Systems Platform Specialist", "explicit_gtm_engineering", "systems_operations", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-27", "unstated", "", "", "high", "Thank you 2026-05-21 omits role; decline names the specialist title. Second thank you 2026-06-22 merged.", "19e48980896f8941"),
    ("Speechify", "Speechify", "", "Go-to-Market Engineer, Atlanta", "explicit_gtm_engineering", "plain", "2026-05-25", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "Atlanta", "", "", "high", "", "19e5eab99cdf81af"),
    ("EvenUp", "EvenUp", "", "AI Adoption Manager, Southeast", "other", "", "2026-05-25", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-06-04", "unstated", "", "", "high", "", "19e5dd62d00d3326"),
    ("Deepgram", "Deepgram", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-05-21", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-05-22", "unstated", "", "", "high", "", "19e4885d926c2eef"),
    ("Onit", "Onit", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19e4b49694584b22"),
    ("TRACTIAN", "TRACTIAN", "", "Sales Engineer, Automation", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from Senior GTM Engineer Hubspot 2026-05-19.", "19e48a2ceaaaf575"),
    ("Applied Systems", "Applied Systems", "", "Sales Enablement GTM Readiness Lead", "revops_gtm_ops_strategy", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "iCIMS", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "iCIMS verify, welcome, and receipt within 28 seconds.", "19e48a0f793edaa7"),
    ("VitalSource", "VitalSource", "", "AI Enablement Lead", "other", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Jobvite", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "", "19e489445bf1588b"),
    ("Telnyx", "Telnyx", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19e4887929bac69d"),
    ("ApartmentIQ", "ApartmentIQ", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-28", "unstated", "", "", "high", "Role omitted on receipt.", "19e48830325dab6d"),
    ("NICE", "NICE", "", "AI Solution Strategist", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19e488224ece6bbd"),
    ("Nebius", "Nebius", "", "Director GTM Physical AI", "explicit_gtm_engineering", "ai_product_vertical", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-16", "unstated", "Director", "", "medium", "2026-05-21 thank you omits role. 2026-07-16 decline names Director GTM Physical AI. One cycle.", "19e48813db65a1ed"),
    ("DBeaver", "DBeaver", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-05", "unstated", "", "", "high", "", "19e4859d61d1fb64"),
    ("FOSSA", "FOSSA", "", "unspecified", "unspecified", "", "2026-04-22", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-20", "unstated", "", "", "high", "Cycle 1. Role omitted. Terminal 2026-05-20 licenses c2.", "19db79c8ee22ec32"),
    ("FOSSA", "FOSSA", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Cycle 2 after 2026-05-20 decline. Subject says second cycle.", "19e484115163beb9"),
    ("TRACTIAN", "TRACTIAN", "", "Senior GTM Engineer, Hubspot", "explicit_gtm_engineering", "systems_operations", "2026-05-19", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "Senior", "", "high", "", "19e4291127b40a17"),
    ("10x Genomics", "10x Genomics", "", "unspecified", "unspecified", "", "2026-05-02", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-14", "unstated", "", "", "high", "Two receipts 14 seconds apart from greenhouse-mail and careers.10xgenomics.com.", "19de744df3cc8058"),
    ("Trase", "Trase", "", "GTM Engineer, Healthcare", "explicit_gtm_engineering", "ai_product_vertical", "2026-04-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-10", "unstated", "", "", "high", "2026-04-27 thank you omits healthcare modifier; 2026-06-26 thank you; 2026-07-10 decline names Healthcare. One cycle not two: no terminal between April and June receipts.", "19dccd718095daa6"),
    ("OXOS Medical", "OXOS Medical", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19dccd63689d53b4"),
    ("WallStreetQuants", "WallStreetQuants", "", "unspecified", "unspecified", "", "2026-04-17", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted on data-copy thank you.", "19d99de120567117"),
    ("Built Recruiting", "Built Recruiting", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-16", "evidence_bound", "2026-04-16", "unknown", "ats_direct", "Greenhouse", "B", "application", "role_paused_or_closed", "2026-04-16", "unstated", "", "", "medium", "Position filled update. No earlier receipt.", "19d96c817e5530a8"),
    ("Mercor", "Mercor", "", "Sales Engineering Expert", "sales_solutions_engineering", "", "2026-08-18", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-08-25", "remote", "", "", "high", "Application Submitted receipt. Per-application register.", "1a015e476731c1c4"),
    ("Mercor", "Mercor", "", "B2B Sales Expert", "sales_bd_partnerships", "", "2026-08-18", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-08-25", "remote", "", "", "high", "", "1a015e4424bbd69e"),
    ("Mercor", "Mercor", "", "Sales and Marketing Expert", "growth_demand_marketing", "", "2026-08-18", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "still_open", "", "remote", "", "", "high", "", "1a015e4b3b0e08ad"),
    ("Mercor", "Mercor", "", "Biology & Biophysics Research Collaborator", "product_ai_technical", "", "2026-07-20", "exact", "", "referral", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-07-27", "remote", "", "", "high", "Application Submitted on Cincinnatus. Referral from Victor Ekuta same day is a separate pathway.", "19f80db568ec6cea"),
    ("Mercor", "Mercor", "", "Education / school Evaluator", "other", "", "2026-06-22", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-06-29", "remote", "", "", "high", "", "19eefdfd5fb4bb63"),
    ("Mercor", "Mercor", "", "General Sales / GTM Evaluator", "sales_bd_partnerships", "", "2026-06-22", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-06-29", "remote", "", "", "high", "", "19eefdeb355c085a"),
    ("Uncapped", "Uncapped", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-08-22", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "rejected_no_interview", "2026-08-25", "unstated", "", "", "high", "", "1a0284aba5f7f81a"),
    ("OpenObserve", "OpenObserve", "", "Growth Marketer", "growth_demand_marketing", "", "2026-08-24", "evidence_bound", "2026-08-24", "unknown", "ats_direct", "Ashby", "B", "application", "rejected_no_interview", "2026-08-24", "unstated", "", "", "medium", "Decline update. No earlier receipt in corpus.", "1a0355ff0ad43420"),
    ("LiveKit", "LiveKit", "", "GTM Systems Engineer", "explicit_gtm_engineering", "systems_operations", "2026-07-20", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-08-17", "unstated", "", "", "high", "", "19f7fdf16a84eeb7"),
    ("Tripleseat", "Tripleseat", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-08-06", "exact", "", "unknown", "recruiter_submitted", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Hirebridge: profile submitted to Tripleseat #611301.", "19fd83cab4f5a68d"),
    ("Great Question", "Great Question", "", "Senior Demand Generation Manager", "growth_demand_marketing", "", "2026-07-17", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_after_interview", "2026-07-29", "unstated", "Senior", "", "high", "Receipt, screening scheduling, two interview reminders, post-interview decline.", "19f7078ecf3d9598"),
    ("Gradient Labs", "Gradient Labs", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-21", "evidence_bound", "2026-07-21", "unknown", "unknown", "Ashby", "B", "application", "rejected_no_interview", "2026-07-27", "unstated", "", "", "medium", "ZipRecruiter prompt to complete plus later Ashby decline. No completed-receipt phrase on ZipRecruiter for this employer.", "19fa440801dc6151"),
    ("AI Digital", "AI Digital", "", "Growth Director", "growth_demand_marketing", "", "2026-07-24", "exact", "", "ladders", "apply4me_agent", "none_observed", "A", "application", "rejected_no_interview", "2026-07-27", "unstated", "Director", "", "high", "Apply4Me Application Sent plus employer decline.", "19f94904962c2e2b"),
    ("IBM", "IBM", "Confluent", "Manager, Applied AI & GTM Systems", "explicit_gtm_engineering", "systems_operations", "2026-06-22", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-07-26", "unstated", "Manager", "", "high", "IBM submission confirmation Ref 119353 Candidate ID 13806529. Decline names Confluent.", "19ef0dc6fd9601c2"),
    ("Hightouch", "Hightouch", "", "Go-to-Market Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-24", "unstated", "", "", "high", "Security code then receipts 2026-07-15 and 2026-07-22 merged as one cycle.", "19f672b1c753c07d"),
    ("Lattice", "Lattice", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-24", "exact", "", "ladders", "apply4me_agent", "Greenhouse", "A", "application", "role_paused_or_closed", "2026-08-04", "unstated", "", "", "high", "Apply4Me sent plus matching Greenhouse receipt same minute. Position filled 2026-08-04.", "19f9445f8807e40b"),
    ("Firstup", "Firstup", "", "Manager, GTM Systems", "explicit_gtm_engineering", "systems_operations", "2026-07-23", "exact", "", "ladders", "apply4me_agent", "Lever", "A", "application", "still_open", "", "unstated", "Manager", "", "high", "Apply4Me sent plus matching Lever receipt same minute.", "19f8ca07274d9777"),
    ("Clutch", "Clutch", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-19", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Receipt then 2026-07-22 note.", "19f7a5451367af23"),
    ("Owner.com", "Owner.com", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-22", "exact", "", "unknown", "ats_direct", "Ashby", "B", "application", "still_open", "", "unstated", "", "", "medium", "Subject GTM Engineer; body names Product Builder, GTM Product. Used subject verbatim. Conflict in notes.", "19f8aa5a9dee405a"),
    ("Revic", "Revic", "", "Founding GTM AI Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-21", "exact", "", "unknown", "unknown", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "ZipRecruiter: application is complete.", "19f82bde8c27b1f9"),
    ("Lorikeet", "Lorikeet", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "role_paused_or_closed", "2026-07-20", "unstated", "", "", "high", "", "19f6712399be4ba0"),
    ("Hyperbound", "Hyperbound", "", "Founding RevOps Lead", "revops_gtm_ops_strategy", "", "2026-07-17", "evidence_bound", "2026-07-17", "unknown", "ats_direct", "Ashby", "B", "application", "rejected_no_interview", "2026-07-17", "unstated", "Founding", "", "medium", "Decline names the role. No earlier receipt.", "19f70d1eb116ee40"),
    ("Toast", "Toast", "", "GTM Engineer, Sales Workflow Automation", "explicit_gtm_engineering", "sales_presales", "2026-06-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-16", "unstated", "", "", "high", "Thanks 2026-06-24 omits modifier; decline 2026-07-16 names Sales Workflow Automation.", "19efaf07476920ba"),
    ("Together AI", "Together AI", "", "unspecified", "unspecified", "", "2026-07-13", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code 2026-07-13 then receipts 07-13 and 07-15. Role omitted. One cycle.", "19f59187b2f99900"),
    ("HUD", "HUD", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-16", "unstated", "", "", "high", "", "19f673230c047acf"),
    ("Higgsfield", "Higgsfield", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19f67338d222bbfd"),
    ("GatherUp", "GatherUp", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19f67309cd2aae85"),
    ("BrightHire", "BrightHire", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19f672edb15894d3"),
    ("Scribe", "Scribe", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19f672d2bf2e6a71"),
    ("Nooks", "Nooks", "", "GTM Engineer, Marketing", "explicit_gtm_engineering", "growth_marketing", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19f6712efa07f534"),
    ("Yuno", "Yuno", "", "Go To Market Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19f66efcd7ca225a"),
    ("Handshake", "Handshake", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19f66e96998790fa"),
    ("Attentive", "Attentive", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-22", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-07", "unstated", "", "", "high", "Cycle 1.", "19eefbc31ff6b3b6"),
    ("Attentive", "Attentive", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Cycle 2 after 2026-07-07 decline.", "19f66e0efd40b3f4"),
    ("Anduril Industries", "Anduril Industries", "", "Technical Operations Engineer, Launched Effects", "product_ai_technical", "", "2026-06-21", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-07-15", "unstated", "", "", "medium", "2026-06-21 names Technical Operations Engineer. 2026-07-15 recruiting.anduril.com thank you/decline omits that title. Treated as one cycle.", "19ee93283584432d"),
    ("Productboard", "Productboard", "", "Associate GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-13", "exact", "", "unknown", "ats_direct", "Gem", "A", "application", "still_open", "", "unstated", "Associate", "", "high", "Gem GTM Engineer 2026-07-13 and Associate GTM Engineer 2026-07-15. Same company, similar titles, no terminal between. Merged as one cycle using the more specific listed title from 07-15.", "19f591197ecd2b88"),
    ("Hologram", "Hologram", "", "GTM Engineer Pre-Sales", "explicit_gtm_engineering", "sales_presales", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code then activated. Screening Amy Schwartz 2026-07-20. Cross-functional Derrick Calderon 2026-07-22.", "19f66680cb338333"),
    ("Axiad", "Axiad", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code then thank you. Role omitted.", "19f663a7ea0c599a"),
    ("Conversion", "Conversion", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-14", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19f630abd3eb09e5"),
    ("Anysphere", "Cursor", "", "GTM, Emerging Products", "explicit_gtm_engineering", "ai_product_vertical", "2026-07-12", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-13", "unstated", "", "", "high", "Company as listed Cursor. Canonical Anysphere.", "19f581850e4bdee5"),
    ("HartleyCo", "HartleyCo", "Bluejay", "Founding GTM", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-13", "evidence_bound", "2026-07-13", "recruiter_inbound", "recruiter_submitted", "none_observed", "B", "application", "rejected_after_interview", "2026-07-23", "unstated", "Founding", "", "high", "Josh Kelly thread regarding GTM Engineer application then 2026-07-23 decline of Founding GTM at Bluejay after the process. Recruiter thank-you-for-applying rule. Client named Bluejay on the decline.", "19f59c69bc094dbf"),
    ("Patch", "Patch", "", "Growth Engineering Lead", "growth_demand_marketing", "", "2026-07-13", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "", "19f591484e264a9d"),
    ("Talentpluto", "talentpluto", "unknown", "Go-to-Market Engineer", "explicit_gtm_engineering", "plain", "2026-07-12", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Workable submitted successfully with data copy. Talentpluto later said process incomplete pending a Pluto call. Underlying employer unnamed.", "19f5862ce3bd83b7"),
    ("Talentpluto", "talentpluto", "unknown", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-12", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "medium", "Second Workable submission three minutes later, title GTM Engineer vs Go-to-Market Engineer. Counted as second role not a duplicate because titles differ as listed.", "19f5862ce3bd83b7"),
    ("Listen Labs", "Listen Labs", "", "Lead GTM Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-12", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "", "19f581abc17d4940"),
    ("Confido", "Confido", "", "Founding GTM Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-12", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "19f5811658f16a5d"),
    ("Douglas County School System", "Douglas County School System", "", "unspecified", "other", "", "2026-07-09", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "AppliTrack submission confirmed 7/9/2026. Role omitted.", "19f47b33ae935a1d"),
    ("jobmail.io", "jobmail.io", "unknown", "Growth Lead", "growth_demand_marketing", "", "2026-07-07", "exact", "", "unknown", "unknown", "none_observed", "A", "application", "rejected_no_interview", "2026-07-13", "unstated", "", "", "high", "Stealth company unnamed. Decline says steps completed through Jack.", "19f3ec27ee050c8d"),
    ("InRule Technology", "InRule Technology", "", "unspecified", "unspecified", "", "2026-07-06", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "19f3945ca9b2c382"),
    ("UpGuard", "UpGuard", "", "SDR Manager", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "rejected_no_interview", "2026-06-29", "unstated", "", "", "high", "", "19efc056918b6c04"),
    ("MinIO", "MinIO", "", "BDR Enterprise", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-06-27", "unstated", "", "", "high", "", "19efc06d34fcb255"),
    ("Tekion", "Tekion", "", "Senior Manager Inside Sales", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-27", "unstated", "Senior Manager", "", "high", "", "19efc04fdbc254f8"),
    ("City Schools Of Decatur", "City Schools Of Decatur", "", "unspecified", "other", "", "2026-06-26", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "AppliTrack started then submission confirmed 6/26/2026. Role omitted.", "19f0591daff91fe0"),
    ("WireScreen", "WireScreen", "", "Partnerships Manager", "sales_bd_partnerships", "", "2026-06-25", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-03", "unstated", "", "", "high", "", "19efcac922c14bff"),
    ("Clay", "Clay", "", "Growth Strategist, Enterprise", "growth_demand_marketing", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-06-25", "unstated", "", "", "high", "", "19efc05ffdf85b11"),
    ("Automation Anywhere", "Automation Anywhere", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19efb606b9d8d30c"),
    ("Canals", "Canals", "", "Sales Manager", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19efb4665f5d3e35"),
    ("StackAI", "StackAI", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19efb45de31b9ab1"),
    ("Enlace Health", "Enlace Health", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-26", "unstated", "", "", "high", "", "19efb21f0d264cc7"),
    ("Jobgether", "Jobgether", "unknown", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-22", "exact", "", "unknown", "unknown", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Jobgether next-steps plus match score. Underlying employer unnamed.", "19ef0388de687866"),
    ("Syncro", "Syncro", "", "GTM Operations Manager", "revops_gtm_ops_strategy", "", "2026-06-22", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19eefe0d482170d6"),
    ("Wealth.com", "Wealth.com", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-22", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-06-22", "unstated", "", "", "high", "", "19eefcd985ae33a4"),
    ("Armada", "Armada", "", "AI Factory, Value Engineer", "sales_solutions_engineering", "", "2026-06-22", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "19eefba5be8f7ef6"),
    ("Atlanta Public Schools", "Atlanta Public Schools", "", "unspecified", "other", "", "2026-06-19", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-06-22", "unstated", "", "", "high", "AppliTrack submission confirmed 6/19/2026 5:09:44 PM. APS later said not accepting substitute applications. Both facts recorded.", "19ee1ef014efde21"),
    ("The Hog", "The Hog", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-15", "evidence_bound", "2026-06-15", "unknown", "unknown", "none_observed", "B", "application", "still_open", "", "unstated", "", "", "medium", "No ATS receipt. Invitation to GTM Interview plus take-home. Coded as application because the employer process names GTM Engineer and a take-home assignment. Evidence-bound to the invitation date. Could have been opportunity; chose application from role-titled process plus assignment.", "19ecda5fa25e0d35"),
    ("RevPartners", "RevPartners", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-24", "exact", "", "unknown", "ats_direct", "Teamtailor", "A", "application", "still_open", "", "unstated", "", "", "high", "Teamtailor complete-application plus later status messages.", "19efb237bd508b63"),
    ("Practical Prospecting", "Practical Prospecting", "", "unspecified", "unspecified", "", "2026-05-20", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Sent resume to jed@practicalprospecting.io. Role omitted in subject.", "19e464b4cc0113a9"),
    ("Spider.cloud", "Spider.cloud", "", "Growth lead", "growth_demand_marketing", "", "2026-05-03", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Sent: Growth lead app.", "19deeeb2c2f91f78"),
    ("AICRO", "AICRO", "", "GTM Engineering Team Lead", "explicit_gtm_engineering", "founding_senior_lead", "2026-02-06", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Team Lead", "", "high", "Sent to gtm@aicro.co.", "19c314590d03fe1c"),
    ("Nero", "Nero", "", "Founding Engineer", "product_ai_technical", "", "2026-01-07", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "Founding Engineer Application, video attached.", "19b965c7ecaf827d"),
    ("Insignia Collab", "Insignia Collab", "", "unspecified", "unspecified", "", "2025-11-18", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "Atlanta", "", "", "medium", "Sent resume. Subject is operator/architect/Atlanta resident. Role as listed unspecified.", "19a965b6167b161d"),
    ("Inertia Growth", "Inertia Growth", "", "Outbound Campaign Manager", "growth_demand_marketing", "", "2025-07-26", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "rejected_no_interview", "2025-07-30", "unstated", "", "", "high", "Sent GTME role resume 2025-07-26. Decline 2025-07-30 names Outbound Campaign Manager Role. Used the decline's listed title.", "19844e86afa37157"),
    ("Inven.ai", "Inven.ai", "", "unspecified", "unspecified", "", "2025-06-11", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "medium", "Sent resume. Role omitted.", "19760e837eee9624"),
    ("Every.to", "Every.to", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-20", "evidence_bound", "2026-04-20", "unknown", "unknown", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "austin@every.to thanks for applying for the GTM Engineer role. Call booked. No ATS receipt.", "19dab8026601594d"),
    ("Switchyards", "Switchyards", "", "Launch Manager", "other", "", "2025-08-08", "evidence_bound", "2025-08-08", "unknown", "email_direct", "none_observed", "B", "application", "rejected_no_interview", "2025-08-19", "unstated", "", "", "medium", "Kayla thread plus Brooks Launch Manager. Resume review. No ATS receipt.", "1988b77b61974363"),
    ("Switchyards", "Switchyards", "", "Digital Product Builder", "product_ai_technical", "", "2026-04-25", "evidence_bound", "2026-04-25", "unknown", "unknown", "none_observed", "B", "application", "rejected_no_interview", "2026-04-25", "unstated", "", "", "medium", "Decline thank-you. No ATS receipt. Distinct role from Launch Manager.", "19dc62db344bac51"),
    ("Lumenalta", "Lumenalta", "", "unspecified", "unspecified", "", "2026-03-24", "exact", "", "unknown", "unknown", "none_observed", "B", "application", "still_open", "", "unstated", "", "", "medium", "You're In next-step 2026-03-24; update 2026-04-10. Role omitted.", "19d1d60ce6d16048"),
    ("Stellar Substitute", "Stellar Substitute", "", "unspecified", "other", "", "2026-07-28", "evidence_bound", "2026-07-28", "unknown", "ats_direct", "none_observed", "B", "application", "role_paused_or_closed", "2026-07-28", "unstated", "", "", "medium", "Frontline position filled notice. Role omitted beyond substitute.", "19fa91f897b687a8"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Murphey Candler ES", "other", "", "2026-08-11", "evidence_bound", "2026-08-11", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-11", "unstated", "", "", "high", "Position you applied for has been filled. Distinct school.", "19ff13b56c64cee0"),
    ("DeKalb County School District", "DeKalb County School District", "", "Specialty Area STAR Substitute, Margaret Harris Comprehensive", "other", "", "2026-08-06", "evidence_bound", "2026-08-06", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-06", "unstated", "", "", "high", "", "19fd85c477301fa8"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Chapel Hill ES", "other", "", "2026-07-14", "evidence_bound", "2026-07-14", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-04", "unstated", "", "", "medium", "Filled notices 2026-07-14 and 2026-08-04 for Chapel Hill ES. One cycle, two notices, not a second posting without a new submission date.", "19f6119f0dd579d3"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Canby Lane ES", "other", "", "2026-08-04", "evidence_bound", "2026-08-04", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-04", "unstated", "", "", "high", "", "19fcd8dec2fb8745"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area High School STAR Substitute, Columbia HS", "other", "", "2026-07-28", "evidence_bound", "2026-07-28", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-28", "unstated", "", "", "high", "", "19faa500c9abd541"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Cedar Grove ES", "other", "", "2026-07-27", "evidence_bound", "2026-07-27", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-27", "unstated", "", "", "high", "", "19fa53991ca6a94c"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 1 Elementary STAR Substitute, Ashford Park ES", "other", "", "2026-07-24", "evidence_bound", "2026-07-24", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-24", "unstated", "", "", "high", "", "19f9592eeee392b1"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 4 Elementary Substitute STAR, Browns Mill ES", "other", "", "2026-07-22", "evidence_bound", "2026-07-22", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-22", "unstated", "", "", "high", "", "19f8b596fe19b8b0"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Rowland ES", "other", "", "2026-07-14", "evidence_bound", "2026-07-14", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-14", "unstated", "", "", "high", "", "19f620f9470e136d"),
    ("DeKalb County School District", "DeKalb County School District", "", "Horizon Area Substitute STAR, Flat Rock ES", "other", "", "2026-07-08", "evidence_bound", "2026-07-08", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-08", "unstated", "", "", "high", "", "19f4373e9e27352c"),
]

# Opportunity register: recruiter/referral/matching with no submission, still in dataset.
OPPS: list[tuple] = [
    ("WorkOS", "WorkOS", "WorkOS", "GTM Engineer", "explicit_gtm_engineering", "plain", "2025-08-25", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "remote", "", "", "high", "TopHire Somya Shruti approach. Interest confirmed, slot booked, resume requested. No submission receipt.", "198e28511c2c7be7"),
    ("ThriveLink", "ThriveLink", "", "Healthcare Business Development Rep", "sales_bd_partnerships", "", "2025-08-05", "exact", "", "referral", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Josh Pappas referral introduction. No ATS submission artifact.", "1987c108c41ff59d"),
    ("Mercor", "Mercor", "", "Growth Strategist", "growth_demand_marketing", "", "2026-08-20", "exact", "", "recruiter_inbound", "unknown", "none_observed", "A", "opportunity", "offer_accepted", "2026-08-21", "remote", "", "", "high", "Instant Work Offer states he did not apply directly. Recruiter Claire Gauthier path. Contract activated 2026-08-21. Not in application census.", "1a021442493bec48"),
    ("micro1", "micro1", "unknown", "AI Training Pilot Project", "other", "", "2026-01-14", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Profile submitted to unnamed client by micro1. Matching pathway.", "19bbd5c1dc792315"),
    ("Dexian", "Dexian", "unknown", "Outbound Sales Consultant III (Remote)", "sales_bd_partnerships", "", "2026-06-05", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "remote", "", "", "high", "Recruiter approach. No submission. Distinct intermediary from WilsonHCG.", "19e9805d2feb7656"),
    ("Luzmo", "Luzmo", "", "SDR", "sales_bd_partnerships", "", "2026-06-30", "exact", "", "jobright", "unknown", "none_observed", "C", "opportunity", "still_open", "", "unstated", "", "", "high", "Jobright recruiter sequence. No application evidence.", "19f18abcd6c662a8"),
    ("Glytec", "Glytec", "", "unspecified", "unspecified", "", "2026-01-27", "evidence_bound", "2026-01-27", "unknown", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Interview logistics and portfolio send. No submission receipt.", "19bfd208daa544b6"),
    ("BX Studio", "BX Studio", "", "unspecified", "unspecified", "", "2026-04-08", "evidence_bound", "2026-04-08", "unknown", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Video sent, forwarded to hiring manager. No submission receipt.", "19d6bb0d0e645a4a"),
    ("Crossing Hurdles", "Crossing Hurdles", "Montauk Capital", "Head of Commercial", "sales_bd_partnerships", "", "2026-04-01", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Ceipal via Crossing Hurdles. No submission receipt.", "19d48a4c443ee08c"),
    ("SmartMode AI", "SmartMode AI", "", "unspecified", "unspecified", "", "2025-07-18", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Begin your interview process. No submission receipt.", "1981dd746a37cc50"),
]

# Extra events beyond auto submission_receipt. (application_id_lookup via company|role|cycle, date, type, round, name, role, medium, system, eid, notes)
# Filled after apps are minted using keys.


def extra_event_specs(apps_by_key: dict[str, str]) -> list[dict[str, str]]:
    def k(company: str, role: str, cycle: int) -> str:
        return apps_by_key[aid(company, role, cycle)]

    specs: list[tuple] = [
        ("weave|business-development-manager|c1", "2025-07-31", "rejection", "", "Sarah", "unknown", "email", "gmail", "19862454367cf6f1", "Early decline before 2026 interview artifact."),
        ("weave|business-development-manager|c1", "2026-08-18", "hiring_manager_interview", "1", "unknown", "unknown", "unknown", "gmail", "1a015b9c5373e9bf", "Post-interview decline proves an interview occurred. Date of interview itself not on this artifact."),
        ("pearl|lead-gtm-engineer|c1", "2026-04-30", "hiring_manager_interview", "1", "Alex DeCeglie", "unknown", "unknown", "gmail", "19ddebc217206005", "Interview @ Pearl scheduling."),
        ("pearl|lead-gtm-engineer|c1", "2026-05-04", "hiring_manager_interview", "2", "unknown", "unknown", "phone", "gmail", "19df3f05ef98302b", "Reminder upcoming interview May 5 phone."),
        ("pearl|lead-gtm-engineer|c1", "2026-05-11", "reschedule", "", "unknown", "unknown", "email", "gmail", "19e17cc7e99d523e", "Submit availability, duplicated 8 seconds apart."),
        ("pearl|lead-gtm-engineer|c1", "2026-05-17", "hiring_manager_interview", "3", "unknown", "unknown", "video", "gmail", "19e363d55b30e7dd", "Zoom reminder Lead GTM Engineer."),
        ("revspring|lead-agentic-operations-gtm-engineering|c1", "2026-05-29", "employer_ack", "", "Stephanie Cunningham", "recruiter", "email", "gmail", "19e74662ea5ede3c", "LinkedIn InMail preceding screen."),
        ("revspring|lead-agentic-operations-gtm-engineering|c1", "2026-06-10", "recruiter_screen", "1", "unknown", "recruiter", "unknown", "gmail", "19eb280cfa60523e", "Recruiter Screen Request."),
        ("the-hog|gtm-engineer|c1", "2026-06-15", "hiring_manager_interview", "1", "Hudson Liao", "unknown", "unknown", "gmail", "19ecda5fa25e0d35", "Invitation GTM Interview Jun 16."),
        ("the-hog|gtm-engineer|c1", "2026-06-18", "assessment_sent", "", "Hudson Liao", "unknown", "async", "gmail", "19ed8711b82f46a2", "Take-home about 4 hours."),
        ("the-hog|gtm-engineer|c1", "2026-06-18", "technical_exercise", "2", "Hudson Liao", "unknown", "async", "gmail", "19ed8711b82f46a2", "Take-home is a technical exercise event."),
        ("phrasiq|unspecified|c1", "2026-03-31", "employer_ack", "", "unknown", "founder", "email", "gmail", "19d453dbfa5af222", "Founder outreach via Wellfound relay."),
        ("phrasiq|unspecified|c1", "2026-04-02", "hiring_manager_interview", "1", "unknown", "unknown", "video", "gcal", "bac9katosqoobn46ohd1hemm5k", "Calendar Discovery | Keegan Moody<>PhrasIQ."),
        ("phrasiq|unspecified|c1", "2026-04-06", "hiring_manager_interview", "2", "unknown", "unknown", "unknown", "gmail", "19d453dbfa5af222", "GTM System Deep Dive proposed after Discovery Session."),
        ("hologram|gtm-engineer-pre-sales|c1", "2026-07-16", "employer_ack", "", "Megan Koch", "recruiter", "email", "gmail", "19f6c7190ae437a1", "Intro-call confirmation thread."),
        ("hologram|gtm-engineer-pre-sales|c1", "2026-07-20", "recruiter_screen", "1", "Amy Schwartz", "recruiter", "video", "gmail", "19f7b0d6008a9e23", "Preliminary Screening Call."),
        ("hologram|gtm-engineer-pre-sales|c1", "2026-07-22", "panel", "2", "Derrick Calderon", "unknown", "video", "gmail", "19f8515939b5e54d", "Cross-Functional Interview."),
        ("beautiful-ai|unspecified|c1", "2026-03-17", "hiring_manager_interview", "1", "Brandon Ness", "hiring manager", "unknown", "gmail", "19cfd5722bd49b45", "Post-interview follow-up names HM."),
        ("beautiful-ai|unspecified|c1", "2026-03-26", "rejection", "", "Emily", "unknown", "email", "gmail", "19d2c002fd6328f6", "Post-interview decline."),
        ("hypergen|gtm-engineer|c1", "2026-04-14", "hiring_manager_interview", "1", "unknown", "unknown", "unknown", "gmail", "19cdd6fb062a3cd8", "Interview invitation."),
        ("dagster-labs|gtm-engineer|c1", "2026-04-03", "hiring_manager_interview", "1", "Delaney Housley", "unknown", "unknown", "gmail", "19d54b76f8ffb104", "Thank you for taking the time to chat."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-24", "recruiter_screen", "1", "unknown", "recruiter", "video", "gmail", "19d20d67ae959204", "Breezy recruiter screen."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-25", "recruiter_screen", "1", "unknown", "recruiter", "video", "gmail", "19d26fa4dceba5a6", "Second recruiter screen invite next day. Same round_number."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-25", "no_show", "", "unknown", "unknown", "video", "gmail", "19d26be3aa1d4344", "Missed interview."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-27", "rejection", "", "Jay Banga", "unknown", "email", "gmail", "19d31b20a0dfedb3", "Declined after interview process."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-24", "recruiter_screen", "1", "Harri", "unknown", "unknown", "gmail", "19f922b1dc3fa017", "Screening call scheduling."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-25", "hiring_manager_interview", "2", "unknown", "unknown", "video", "gmail", "19f9add09d4e62b9", "Interview reminder."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-26", "hiring_manager_interview", "2", "unknown", "unknown", "video", "gmail", "19f9fcc92979fc8b", "Google Meet reminder."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-29", "rejection", "", "unknown", "unknown", "email", "gmail", "19fb03b48343c7d3", "Post-interview decline."),
        ("testgorilla|go-to-market-engineer|c1", "2026-02-20", "assessment_sent", "", "Mirae Lee", "recruiter", "async", "gmail", "19c7cb89ca3f84c5", "TestGorilla assessment invitation."),
        ("testgorilla|go-to-market-engineer|c1", "2026-02-20", "recruiter_screen", "1", "Mirae Lee", "recruiter", "email", "gmail", "19c7cad276dff04a", "Recruiter intro."),
        ("huzzle|gtm-engineer|c1", "2026-06-04", "assessment_sent", "", "unknown", "unknown", "async", "gmail", "19e92180ca58bd3a", "Required AI video interview."),
        ("every-to|gtm-engineer|c1", "2026-04-20", "hiring_manager_interview", "1", "Austin", "unknown", "unknown", "gmail", "19dab8026601594d", "Call booked after thanks for applying."),
        ("hartleyco|founding-gtm|c1", "2026-07-13", "recruiter_screen", "1", "Josh Kelly", "recruiter", "unknown", "gmail", "19f59c69bc094dbf", "Call scheduled same day."),
        ("hartleyco|founding-gtm|c1", "2026-07-23", "rejection", "", "Josh Kelly", "recruiter", "email", "gmail", "19f8e4194f9a477d", "Founding GTM at Bluejay declined after process."),
        ("ambrook|business-operations-lead|c1", "2026-02-12", "followup_sent", "", "unknown", "unknown", "email", "gmail", "19c52cbdcc25bd0d", "Reply to no-reply asking for elaboration."),
        ("ambrook|business-operations-lead|c1", "2026-02-12", "rejection", "", "unknown", "unknown", "email", "gmail", "19c52cbdcc25bd0d", ""),
        ("workos|gtm-engineer|c1", "2025-08-25", "recruiter_screen", "1", "Somya Shruti", "recruiter", "unknown", "gmail", "198e28511c2c7be7", "Slot booked. Opportunity register."),
        ("mercor|growth-strategist|c1", "2026-08-18", "recruiter_screen", "1", "Claire Gauthier", "recruiter", "unknown", "gmail", "1a0161d3e41b96dd", "Claire meeting."),
        ("mercor|growth-strategist|c1", "2026-08-21", "offer", "", "unknown", "unknown", "email", "gmail", "1a025862aa01f0dc", "Offer acceptance confirmation GTM Engineer hourly contract. Title on offer differs from Growth Strategist instant offer."),
        ("glytec|unspecified|c1", "2026-01-27", "hiring_manager_interview", "1", "unknown", "unknown", "unknown", "gmail", "19bfd208daa544b6", "Interview logistics."),
        ("jobmail-io|growth-lead|c1", "2026-07-13", "recruiter_screen", "1", "Jack", "unknown", "unknown", "gmail", "19f5b79c8f0892a7", "Steps completed through Jack then declined."),
        ("atlanta-public-schools|unspecified|c1", "2026-06-22", "rejection", "", "unknown", "unknown", "email", "gmail", "19edf97699db02b8", "Not currently accepting substitute applications."),
        ("fossa|unspecified|c1", "2026-05-20", "rejection", "", "unknown", "unknown", "email", "gmail", "19e466fffd8be312", "First cycle declined."),
        ("crypto-com|product-growth-hacker-exchange-main-app|c1", "2025-11-02", "rejection", "", "unknown", "unknown", "email", "gmail", "19a45779c86938f1", ""),
        ("huzzle|gtm-engineer|c1", "2026-06-11", "assessment_sent", "", "unknown", "unknown", "async", "gmail", "19eb650805cfef0a", "Final reminder complete your interview."),
        ("pogo-technologies|gtm-engineer|c1", "2026-06-26", "employer_ack", "", "unknown", "unknown", "email", "gmail", "19f046ca4b4ba350", "Gem first-cycle note. Same title, no terminal on c1."),
        ("pogo-technologies|gtm-engineer|c1", "2026-07-08", "submission_receipt", "", "unknown", "unknown", "email", "gmail", "19f3f0957b849e79", "Ashby thank you. Same cycle as 2026-06-04 Gem receipt."),
    ]
    rows = []
    for spec in specs:
        app_id, date, etype, rnd, name, crole, medium, system, eid, notes = spec
        if app_id not in {aid(a[0], a[3], 1) for a in APPS + OPPS} and app_id not in {
            aid(a[0], a[3], 2) for a in APPS if False
        }:
            pass
        rows.append(
            {
                "application_id": app_id,
                "event_date": date,
                "event_date_precision": "exact",
                "event_type": etype,
                "round_number": rnd,
                "counterparty_name": name,
                "counterparty_role": crole,
                "medium": medium,
                "evidence_system": system,
                "evidence_id": eid,
                "notes": notes,
            }
        )
    return rows


EXCLUSIONS: list[tuple] = [
    ("meshy-interview-prewindow", "2025-06-01", "Meshy", "unspecified", "out_of_window", "A submission receipt dated on or after 2025-06-01", "gmail", "197294f8d50e00cf"),
    ("graph-one-not-in-ats", "2025-07-27", "graph.one", "unspecified", "attempted_not_submitted", "An ATS receipt the founder can see", "gmail", "1984d88bee15d217"),
    ("beckhoff-incomplete-first", "2025-08-07", "Beckhoff Automation", "Sales Engineer", "attempted_not_submitted", "Superseded by 2025-08-08 completed rejection thanking him for applying", "gmail", "1988608ae766bb44"),
    ("gwinnett-started-expired", "2026-06-08", "Gwinnett County Public Schools", "unspecified", "attempted_not_submitted", "AppliTrack submission confirmation", "gmail", "19ea5b7862cb3792"),
    ("dekalb-general-expired", "2026-07-23", "DeKalb County School District", "unspecified", "attempted_not_submitted", "Already have position-level filled notices as applications. General file confirmation would still help", "gmail", "19f8e524b8ac30ab"),
    ("gwinnett-expire-warning", "2026-07-04", "Gwinnett County Public Schools", "unspecified", "attempted_not_submitted", "Submission confirmation", "gmail", "19f2c8bf68806916"),
    ("sbga-prewindow", "2025-04-11", "SBGA", "Remote Outside Sales Rep", "out_of_window", "A submission inside 2025-06-01 to 2026-08-29", "gmail", "196270d68f2adaad"),
    ("umicas-openai", "2025-06-21", "getcrate.app / Umicas", "OpenAI Backend Software Engineer", "unresolvable_identity", "Employer-domain confirmation from OpenAI", "gmail", "19794f4f00396b15"),
    ("umicas-google", "2025-06-21", "getcrate.app / Umicas", "Google Senior Software Engineer Gemini", "unresolvable_identity", "Employer-domain confirmation from Google", "gmail", "197934f165cb9c11"),
    ("crate-missing-materials", "2025-06-23", "Crate", "Software Engineering", "unresolvable_identity", "Employer-domain receipt", "gmail", "1979aae8acdd4534"),
    ("pinterest-referral-pm", "2025-06-30", "Pinterest", "Product Manager II, Search", "attempted_not_submitted", "Submission confirmation. Referral accept said application may still be unsubmitted", "gmail", "197c192980869142"),
    ("pinterest-referral-apr", "2025-06-28", "Pinterest", "Apprentice Product Researcher", "attempted_not_submitted", "Submission confirmation", "gmail", "197b4e0054e600c8"),
    ("gong-gdpr", "2025-07-08", "Gong.io", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "197eb3b08adb3220"),
    ("spot-ai-gdpr", "2025-07-26", "Spot AI", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "1984894435106b68"),
    ("new-relic-retention", "2026-03-28", "New Relic", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "19d35a3c32b6d6a4"),
    ("celonis-retention", "2026-04-02", "Celonis", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "19d4f2cd06b07502"),
    ("saveurdays-unnamed", "2026-04-11", "unknown", "unspecified", "unresolvable_identity", "Named employer and role plus submission language", "gmail", "19d7da158589ce88"),
    ("mixmax-welcome", "2025-09-04", "Mixmax", "unspecified", "marketplace_profile", "An employment application receipt. Product welcome is not an application", "gmail", "19915c326a0ac33b"),
    ("apple-card", "2025-09-12", "Apple Card", "unspecified", "marketplace_profile", "Not employment", "gmail", "1993d6b1bd912044"),
    ("leidos-dover-unverified", "2025-09-23", "Leidos Systems", "Software Engineer III REQ16295", "unresolvable_identity", "Employer-domain receipt. Sender is dover@mail.beehiiv.com", "gmail", "19977d1dfaaa5d09"),
    ("dover-rippling-sem", "2025-12-12", "Rippling", "Software Engineering Manager, Banking", "unresolvable_identity", "Employer-domain receipt. Sender dover@mail.beehiiv.com", "gmail", "19b146233d7f7833"),
    ("wellfound-podium-saved", "2025-06-04", "Podium", "SDR", "attempted_not_submitted", "Wellfound application submitted receipt", "gmail", "1973b7795bb1ae0e"),
    ("wellfound-nomi-saved", "2025-07-16", "Nomi.ai", "Growth Hacker", "attempted_not_submitted", "Wellfound application submitted receipt", "gmail", "19813c2cd09f20e5"),
    ("exa-product-june", "2025-06-12", "Exa", "unspecified", "consulting_prospect", "This is product outreach after API signup, not employment", "gmail", "19765c64cf83eead"),
    ("coldiq-accelerator", "2025-06-11", "ColdIQ", "Accelerator Program", "marketplace_profile", "Employment submission", "gmail", "1975ccc76268e020"),
    ("breakthrough-z", "2025-07-08", "Breakthrough Z", "Clarity Call", "consulting_prospect", "Employment application", "gmail", "197e7fc9a0915aea"),
    ("wells-fargo-banking", "2026-03-06", "Wells Fargo", "Clear Access Banking", "marketplace_profile", "Not a job application", "gmail", "19cc4a62e5143fd6"),
    ("kimi-beta", "2026-06-20", "Kimi", "Code Beta Program", "marketplace_profile", "Not employment", "gmail", "19ee44d95cf17f20"),
    ("alibaba-paylater", "2026-06-21", "Alibaba.com", "Pay Later for Business", "marketplace_profile", "Not employment", "gmail", "19ee9f880d3fe262"),
    ("yc-profile-sharing", "2025-10-08", "Y Combinator Work at a Startup", "unspecified", "marketplace_profile", "Dashboard export of applied roles", "gmail", "199c42e525610e8f"),
    ("anthropic-job-alerts", "2026-04-14", "Anthropic", "unspecified", "marketplace_profile", "Job alert is not an application", "gmail", "19d8be044fd27742"),
    ("ziprecruiter-alerts", "2026-07-21", "ZipRecruiter", "unspecified", "marketplace_profile", "A completed-application receipt for a named role", "gmail", "19f8353985778abd"),
    ("jobright-alerts", "2025-11-18", "Jobright", "unspecified", "marketplace_profile", "Tracker export or application-submitted receipt", "gmail", "log-028"),
    ("jorge-gtme-calendar", "2026-04-29", "gtm-engineering.io", "unspecified", "unresolvable_identity", "Artifact stating this meeting was a job process", "gcal", "14rkurrlp8aemiaaskduc7hphc"),
    ("kivira-connect", "2026-04-06", "kivira.health", "unspecified", "consulting_prospect", "Submission or explicit job-interview language", "gcal", "5a784jadrogo9aind47jdj6lmg"),
    ("rocketeer-onboarding", "2026-04-07", "Rocketeer", "unspecified", "consulting_prospect", "Employment application", "gcal", "chn54lrp98p6uta7cor62rjqah432krfe5940gr1dgn66rrd"),
    ("common-room-chilipiper", "2026-05-28", "Common Room", "unspecified", "unresolvable_identity", "Purpose of meeting stated as job process plus submission", "gmail", "19e702c268104fe7"),
    ("anyint-inmail", "2026-06-09", "unknown", "unspecified", "unresolvable_identity", "Named employer, role, and submission", "gmail", "19eac30589bfe8b9"),
    ("greenhouse-unnamed-jul12", "2026-07-12", "unknown", "GTM Engineer", "unresolvable_identity", "Employer name on the Greenhouse receipt", "gmail", "19f586b7fbc50265"),
    ("talentpluto-incomplete-chase", "2026-07-14", "Talentpluto", "unspecified", "attempted_not_submitted", "This chase is about an incomplete Pluto call. Workable submissions already coded as applications", "gmail", "19f62b55cb2667f8"),
    ("josh-pappas-clinics", "2026-06-04", "Pappas Healthtech", "unspecified", "consulting_prospect", "Employment application", "gmail", "19e9436ce4e43ad8"),
    ("certn-mercor-screen", "2026-08-21", "Mercor", "unspecified", "marketplace_profile", "Background screen is contract onboarding not a new application", "gmail", "1a021cf914f4c0b0"),
    ("micro1-finance-expert", "2026-01-21", "micro1", "Finance Expert", "recruiter_initiated", "Submission artifact", "gmail", "19bdf90e1b30ffa0"),
    ("micro1-chatgpt-pool", "2026-06-05", "micro1", "Certified Expert Pool", "recruiter_initiated", "Titled role submission", "gmail", "19e9866ed62fb9b9"),
    ("the-hog-product-welcome", "2026-06-16", "The Hog", "unspecified", "marketplace_profile", "Product signup is not an application", "gmail", "19ed298800137744"),
]


def build_app_row(item: tuple, cycle_override: int | None = None) -> dict[str, str]:
    (
        canonical,
        as_listed,
        underlying,
        role,
        lane,
        gtm,
        date,
        precision,
        anchor,
        discovery,
        channel,
        ats,
        tier,
        register,
        outcome,
        outcome_date,
        work,
        level,
        loc,
        conf,
        notes,
        tid,
    ) = item
    cycle = cycle_override if cycle_override is not None else 1
    # FOSSA and Attentive c2 already encoded by calling with cycle 2 via date uniqueness: detect from notes
    if "Cycle 2" in notes or "second cycle" in notes.lower() or notes.startswith("Cycle 2"):
        cycle = 2
    if canonical == "FOSSA" and date == "2026-05-21":
        cycle = 2
    if canonical == "Attentive" and date == "2026-07-15":
        cycle = 2
    if canonical == "Galileo" and role == "Growth Engineer":
        cycle = 1
    if canonical == "Galileo" and role == "GTM Engineer":
        cycle = 1
    if canonical == "Ambrook" and "Partnerships" in role:
        cycle = 1
    if canonical == "Switchyards" and "Digital" in role:
        cycle = 1
    row = {f: "" for f in APP_FIELDS}
    row["coder_id"] = CODER
    row["application_id"] = aid(canonical, role, cycle)
    row["cycle"] = str(cycle)
    row["company_canonical"] = canonical
    row["company_as_listed"] = as_listed
    row["underlying_employer"] = underlying
    row["role_as_listed"] = role
    row["role_lane"] = lane
    row["gtm_modifier"] = gtm
    row["date_applied"] = date
    row["date_precision"] = precision
    row["date_capture"] = "2026-08-29" if precision == "relative_display" else ""
    row["date_evidence_anchor"] = anchor if precision == "evidence_bound" else ""
    row["discovery_source"] = discovery
    row["submission_channel"] = channel
    row["ats_system"] = ats
    row["evidence_tier"] = tier
    row["evidence_class"] = "employer_artifact"
    row["register"] = register
    row["terminal_outcome"] = outcome
    row["terminal_outcome_date"] = outcome_date
    row["terminal_outcome_precision"] = "exact" if outcome_date else ""
    row["location"] = loc
    row["work_type"] = work
    row["level_as_listed"] = level
    row["salary_range_listed"] = "not_stated"
    row["confidence"] = conf
    row["notes"] = notes
    row["_receipt_tid"] = tid
    return row


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    app_rows: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for item in APPS + OPPS:
        row = build_app_row(item)
        if row["application_id"] in seen_ids:
            # Collision: bump cycle
            base = row["application_id"].rsplit("|c", 1)[0]
            n = 2
            while f"{base}|c{n}" in seen_ids:
                n += 1
            row["application_id"] = f"{base}|c{n}"
            row["cycle"] = str(n)
            row["notes"] = (row["notes"] + " application_id cycle bumped to avoid key collision.").strip()
        seen_ids.add(row["application_id"])
        app_rows.append(row)

    event_rows: list[dict[str, str]] = []
    counters: dict[str, int] = {}
    for row in app_rows:
        app_id = row["application_id"]
        counters[app_id] = 1
        n = counters[app_id]
        event_rows.append(
            {
                "coder_id": CODER,
                "event_id": f"{app_id}|e{n}",
                "application_id": app_id,
                "event_date": row["date_applied"],
                "event_date_precision": row["date_precision"],
                "event_type": "submission_receipt" if row["register"] == "application" else "employer_ack",
                "round_number": "",
                "counterparty_name": "unknown",
                "counterparty_role": "",
                "medium": "email",
                "evidence_system": "gmail",
                "evidence_id": row.pop("_receipt_tid"),
                "notes": "",
            }
        )

    extras = extra_event_specs({})
    valid_ids = {r["application_id"] for r in app_rows}
    skipped_extra = 0
    for extra in extras:
        app_id = extra["application_id"]
        if app_id not in valid_ids:
            skipped_extra += 1
            continue
        counters[app_id] = counters.get(app_id, 0) + 1
        n = counters[app_id]
        event_rows.append(
            {
                "coder_id": CODER,
                "event_id": f"{app_id}|e{n}",
                "application_id": app_id,
                "event_date": extra["event_date"],
                "event_date_precision": extra["event_date_precision"],
                "event_type": extra["event_type"],
                "round_number": extra["round_number"],
                "counterparty_name": extra["counterparty_name"],
                "counterparty_role": extra["counterparty_role"],
                "medium": extra["medium"],
                "evidence_system": extra["evidence_system"],
                "evidence_id": extra["evidence_id"],
                "notes": extra["notes"],
            }
        )

    excl_rows = []
    for item in EXCLUSIONS:
        cand, date, company, role, reason, promote, system, eid = item
        excl_rows.append(
            {
                "coder_id": CODER,
                "candidate_id": cand,
                "date": date,
                "company": company,
                "role": role,
                "exclusion_reason": reason,
                "what_would_promote_it": promote,
                "evidence_system": system,
                "evidence_id": eid,
            }
        )

    def write_csv(name: str, fields: list[str], rows: list[dict[str, str]]) -> None:
        path = OUT / name
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                writer.writerow({k: row.get(k, "") for k in fields})

    write_csv("applications__cursor.csv", APP_FIELDS, app_rows)
    write_csv("events__cursor.csv", EVENT_FIELDS, event_rows)
    write_csv("exclusions__cursor.csv", EXCL_FIELDS, excl_rows)

    n_app_reg = sum(1 for r in app_rows if r["register"] == "application")
    n_opp = sum(1 for r in app_rows if r["register"] == "opportunity")
    notes = f"""# Coder cursor notes

Artifacts processed: Gmail logs 001-029 (1171 threads listed), calendar CSV (31 events), platform-absent note. Retriever notes were not treated as facts.

Rows emitted: applications {len(app_rows)} (register=application {n_app_reg}, register=opportunity {n_opp}), events {len(event_rows)}, exclusions {len(excl_rows)}.

Skipped extra events whose application_id did not match a minted key: {skipped_extra}.

## Judgement calls

1. Weave: Greenhouse 2025-07-27 is the submission. 2026-08-18 interview decline is the same cycle (no second submission).
2. WorkOS: opportunity. Recruiter-sourced, no submission receipt.
3. Mercor: six Application Submitted rows are applications. Growth Strategist / hourly contract is opportunity.
4. Huzzle: Workable submission language wins over talent-pool marketing copy.
5. Talentpluto: two Workable titles three minutes apart counted as two applications. Underlying employer unknown.
6. DeKalb general expiry is attempted. Eleven position-filled notices are applications because the employer said the position you applied for. Chapel Hill ES two notices = one cycle.
7. Atlanta Public Schools: submitted, then district not accepting substitutes. Both recorded.
8. Gwinnett: started plus expiry = attempted_not_submitted.
9. Pinterest June 2025 referrals: attempted. March 2026 Apprentice Engineer Greenhouse row is the application.
10. The Hog: no ATS receipt. Coded application from a titled GTM interview plus take-home. Medium confidence. Could have been opportunity.
11. Owner.com: used subject GTM Engineer; body Product Builder recorded in notes.
12. Anysphere canonical for Cursor.
13. FOSSA and Attentive use cycle 2 after a terminal outcome.
14. Pogo Gem 2026-06-04, Gem 2026-06-26, and Ashby 2026-07-08 are one cycle. No terminal between them, so cycle is not incremented.
15. Unframe 04-06 and 04-17 merged as one cycle.
16. Productboard 07-13 GTM Engineer and 07-15 Associate GTM Engineer merged as one cycle using the more specific later title.
17. Meshy 2025-06-01 interview decline: out_of_window (submission likely before window).
18. Dover/beehiiv Leidos and Rippling SEM: unresolvable_identity.
19. Newsletters, Anthropic job alerts, ZipRecruiter alerts, Jobright alerts, study portals, Apple Card, Kimi beta, Alibaba, Wells Fargo banking: not coded as employment candidates except as listed exclusions. Remaining Substack/newsletter threads are classified as non-candidates by sender domain and are not one-row-per-thread.
20. Calendar PhrasIQ Discovery attached to the Wellfound PhrasIQ application. Jorge Macias / Kivira / Rocketeer / Mixmax product / Morphin are not applications.
21. Inertia Growth title taken from the decline (Outbound Campaign Manager), not the sent-mail subject GTME role.
22. IBM Confluent: underlying_employer Confluent on an IBM submission.
23. ThriveLink: opportunity (referral intro, no submission).
24. Classet: evidence_bound decline without a submission receipt.
25. Gradient Labs: ZipRecruiter complete-your-application plus later decline. Medium. Not promoted solely by the ZipRecruiter complete prompt.
26. Built Recruiting: evidence_bound position-filled update.
27. Salary always not_stated; never inferred.

## Conflicts

- Owner.com subject vs body titles. Subject used.
- Mercor 2026-06-30 marketing said not yet applied, contradicting 2026-06-22 Application Submitted receipts. Receipts win.
- Retriever notes that cite prior ledger totals were ignored.
- Weave 2025-07-31 decline vs 2026-08-18 interview: both kept; terminal is the later interview decline.

## Vocabulary wanted and not used

- AppliTrack / Frontline as ats_system. Used none_observed.
- Newton / Paycom / Gem already partly covered; Gem is in the vocab.
- event_type for marketplace contract activation. Used offer for Mercor contract.
"""
    (OUT / "notes__cursor.md").write_text(notes, encoding="utf-8")
    print(f"applications={len(app_rows)} application_register={n_app_reg} opportunity={n_opp} events={len(event_rows)} exclusions={len(excl_rows)} skipped_extra={skipped_extra}")


if __name__ == "__main__":
    main()
