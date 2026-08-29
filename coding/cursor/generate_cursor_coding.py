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
    ("Crypto.com", "Crypto.com", "", "Product Growth Hacker: Exchange & Main App", "growth_demand_marketing", "", "2025-08-05", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "rejected_no_interview", "2025-11-02", "unstated", "", "", "high", "Receipt 2025-08-05; 2025-11-02 Lever thank-you/decline of same role merged. Evidence IDs gth_2cbb1ee26d2137ac and gth_a5db72a965bb0178.", "gth_2cbb1ee26d2137ac"),
    ("Fullsteam", "Fullsteam", "", "Senior Sales Development Representative", "sales_bd_partnerships", "", "2025-09-29", "evidence_bound", "2025-09-29", "unknown", "ats_direct", "Workday", "B", "application", "still_open", "", "unstated", "Senior", "", "medium", "Workday update not a first-receipt. Date is evidence-bound to the update.", "gth_1a05f5a4e1ffa7ad"),
    ("Anaconda", "Anaconda", "", "Senior BDR", "sales_bd_partnerships", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "Senior", "", "high", "Rippling receipt 2025-07-27; 2025-08-22 update thread gth_ef44ed80a3ab9ffd merged.", "gth_cd513ab76e1d81dd"),
    ("Sage", "Sage", "", "Director of Growth, Small", "growth_demand_marketing", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Director", "", "high", "careers.sage.com thanks-for-application 2025-08-04; 2025-09-03 update gth_d24517830e4ccefb.", "gth_677cf91c6d68ffaa"),
    ("Ava Labs", "Ava Labs", "", "Growth Lead, Core", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Wellfound submission gth_f05b94b3d373f04c. Employer thanks-for-interest 2025-08-14 gth_2ef1129d4affda0a merged.", "gth_f05b94b3d373f04c"),
    ("ClassDojo", "ClassDojo", "", "unspecified", "unspecified", "", "2025-08-08", "evidence_bound", "2025-08-08", "unknown", "ats_direct", "Gem", "B", "application", "still_open", "", "unstated", "", "", "medium", "Gem update only. Role omitted.", "gth_8ecd48caabede254"),
    ("proteanTecs", "proteanTecs", "", "SDR", "sales_bd_partnerships", "", "2025-08-08", "exact", "", "unknown", "ats_direct", "Comeet", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_872a8cc666a982c0"),
    ("Beckhoff Automation", "Beckhoff Automation", "", "Sales Engineer", "sales_solutions_engineering", "", "2025-08-08", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2025-08-08", "unstated", "", "", "high", "Paycom incomplete notice 2025-08-07 then 2025-08-08 rejection thanking him for applying. Submission treated as completed that day.", "gth_7af99df6c0ed420a"),
    ("Seamless.AI", "Seamless.AI", "", "SDR Remote US", "sales_bd_partnerships", "", "2025-08-05", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2025-08-07", "remote", "", "", "high", "Thank you 2025-08-05; status 2025-08-07 gth_85e6fb438cf83c14.", "gth_ab6b5f0fdbb449ec"),
    ("Ambrook", "Ambrook", "", "Partnerships Lead", "sales_bd_partnerships", "", "2025-08-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from 2026 Business Operations Lead.", "gth_a40ab81ae9db447a"),
    ("Blackthorn.io", "Blackthorn.io", "", "unspecified", "unspecified", "", "2025-08-05", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted on receipt.", "gth_e16c1dce856c6501"),
    ("Axon", "Axon", "", "Manager, Go-to-Market Readiness", "revops_gtm_ops_strategy", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2025-08-04", "unstated", "Manager", "", "high", "Apply then reviewed same day. Threads gth_60df33526b5d45da and gth_e7990aa8e2799f88.", "gth_60df33526b5d45da"),
    ("4flow", "4flow", "", "Director, Go To Market Strategy", "revops_gtm_ops_strategy", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "Director", "", "high", "", "gth_b7e5dba6558a5e97"),
    ("ITC Infotech", "ITC Infotech", "", "Manager, Business Development", "sales_bd_partnerships", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Manager", "", "high", "", "gth_094809d092e62284"),
    ("Fibr AI", "Fibr AI", "", "Founding SDR + AE", "sales_bd_partnerships", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "gth_8a3654f6092433d7"),
    ("12100 Collective", "12100 Collective", "", "SEO Lead", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_9dbe21075064fa41"),
    ("Infisical", "Infisical", "", "Founding Growth Marketer", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "gth_40efade37d72ed11"),
    ("AirGarage", "AirGarage", "", "Consumer Growth Hacker", "growth_demand_marketing", "", "2025-08-04", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_8acfef93a25af4cf"),
    ("OnBoard", "OnBoard", "", "unspecified", "unspecified", "", "2025-08-04", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_63f80485d914a4d4"),
    ("GTP Software", "GTP Software, Inc.", "", "Revenue Enablement Manager", "revops_gtm_ops_strategy", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Thank you 2025-07-27; named role on 2025-08-01 gth_4bb74b4c4bfc7a0b.", "gth_6924b3fe0638af29"),
    ("Weave", "Weave", "", "Business Development Manager", "sales_bd_partnerships", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_after_interview", "2026-08-18", "unstated", "", "", "high", "Greenhouse receipt 2025-07-27. eml_33349183f8f1 declined 2025-07-31 then Ashby 2026-08-18 thanks for meeting and interview. Long gap; one cycle because no second submission artifact.", "gth_4871569df9c50a18"),
    ("Hex", "Hex", "", "SDR", "sales_bd_partnerships", "", "2025-07-31", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_e20c0699bee48877"),
    ("Phiture", "Phiture", "", "US Growth Lead, Mobile Marketing Strategist", "growth_demand_marketing", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "no-reply@phiture.com receipt; ariel.kowalczyk follow-up 2025-07-29.", "gth_c9f3515a2e4b0ec5"),
    ("Galileo", "Galileo", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2025-07-28", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from Growth Engineer 2025-07-02.", "gth_b3f40741923f1f49"),
    ("Slingshot AI", "Slingshot AI", "", "Conversation Designer", "product_ai_technical", "", "2025-07-25", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Thank you 2025-07-25; update 2025-07-28.", "gth_0ad56d4a618a161c"),
    ("Replit", "Replit", "", "Sales Engineer", "sales_solutions_engineering", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Follow-up 2025-07-30 gth_1474078ab0c749e8.", "gth_2f5a31ea4cfaa643"),
    ("Stedi", "Stedi", "", "unspecified", "unspecified", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_0dafa0f6f8c4b49a"),
    ("Shaped", "Shaped", "", "Founding SDR", "sales_bd_partnerships", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Dover", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "gth_07a51feca3245fbb"),
    ("Volley", "Volley", "", "unspecified", "unspecified", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_4ed68885f5da7029"),
    ("90 Seconds", "90 Seconds", "", "unspecified", "unspecified", "", "2025-07-27", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_3765f993cf7dedf7"),
    ("Exa", "Exa Labs Inc.", "", "Growth Lead", "growth_demand_marketing", "", "2025-07-25", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from June 2025 Exa product outreach.", "gth_f7fbf386a2206469"),
    ("ScaleOps", "ScaleOps", "", "Sales Engineer, USA", "sales_solutions_engineering", "", "2025-07-17", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Spark Hire Recruit named in subject.", "gth_f6b850f7faab1b86"),
    ("Classet", "Classet", "", "Head of GTM", "sales_bd_partnerships", "", "2025-07-09", "evidence_bound", "2025-07-09", "wellfound", "wellfound_apply", "none_observed", "B", "application", "rejected_no_interview", "2025-07-09", "unstated", "", "", "medium", "Wellfound update/decline. No separate submission receipt in corpus. Evidence-bound.", "gth_6af5520ff5313d68"),
    ("Designit", "Designit", "", "unspecified", "unspecified", "", "2025-07-08", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_a948ba26d1c760e9"),
    ("Applause", "Applause", "", "Enterprise SDR", "sales_bd_partnerships", "", "2025-07-08", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "rejected_no_interview", "2025-07-09", "unstated", "", "", "high", "Data copy gth_c267ece03dd32903 plus receipt/rejection gth_ead7e2e5ff24178c.", "gth_c267ece03dd32903"),
    ("Headway", "Headway", "", "Growth Marketing Specialist", "growth_demand_marketing", "", "2025-07-03", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_24f31ba9b6d07994"),
    ("Galileo", "Galileo", "", "Growth Engineer", "growth_demand_marketing", "", "2025-07-02", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Different title from GTM Engineer 2025-07-28.", "gth_3773ef97e4ae6325"),
    ("Gigs", "Gigs", "", "unspecified", "unspecified", "", "2025-06-30", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_7c1890f4eef1ccc1"),
    ("Runway", "Runway", "", "Go-To-Market AI Engineer", "explicit_gtm_engineering", "ai_product_vertical", "2025-06-26", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_951665f2d42f4160"),
    ("Trace3", "Trace3", "", "SDR", "sales_bd_partnerships", "", "2025-06-25", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "role_paused_or_closed", "2025-06-25", "unstated", "", "", "high", "Opening filled on the application notice.", "gth_664f031e9e76c4ce"),
    ("Circle", "Circle", "", "GTM Engineer, Outbound", "explicit_gtm_engineering", "sales_presales", "2025-06-20", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_d2d399fc49799ade"),
    ("Drata", "Drata", "", "SDR Remote", "sales_bd_partnerships", "", "2025-06-16", "evidence_bound", "2025-06-16", "unknown", "ats_direct", "Greenhouse", "B", "application", "still_open", "", "remote", "", "", "medium", "Update artifact, not a first receipt.", "gth_c3d031eb13592313"),
    ("Foursquare", "Foursquare", "", "AE New Business", "sales_bd_partnerships", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-01-08", "unstated", "", "", "high", "", "gth_733225d8d4947914"),
    ("SailPoint", "SailPoint", "", "Account Exec Enterprise Accounts", "sales_bd_partnerships", "", "2026-01-03", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "", "", "high", "Received gth_7cca95e87c341b02 then thank you gth_a63697864876f319.", "gth_7cca95e87c341b02"),
    ("Proofpoint", "Proofpoint", "", "unspecified", "unspecified", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_a3145491c3616deb"),
    ("Thomson Reuters", "Thomson Reuters", "", "AE Tax or Risk", "sales_bd_partnerships", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "", "", "high", "JREQ195996. Update 2026-02-20 gth_5921d0d724baf4ed.", "gth_1ac8722715175516"),
    ("MediaLab.AI", "MediaLab.AI Inc.", "", "unspecified", "unspecified", "", "2026-01-02", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_de042b60b756f45f"),
    ("Primer", "Primer", "", "unspecified", "unspecified", "", "2025-12-09", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2025-12-15", "unstated", "", "", "high", "Role omitted on both artifacts.", "gth_983699d74e67f6d7"),
    ("Linear", "Linear", "", "AE Growth", "sales_bd_partnerships", "", "2025-12-08", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2025-12-11", "unstated", "", "", "high", "", "gth_b8597f2567fc308f"),
    ("Vonage", "Vonage", "", "SDR API/CPaaS", "sales_bd_partnerships", "", "2025-12-08", "evidence_bound", "2025-12-08", "unknown", "ats_direct", "Greenhouse", "B", "application", "rejected_no_interview", "2025-12-08", "unstated", "", "", "medium", "Status update declined. No earlier receipt in corpus.", "gth_4f1dca61418b9c35"),
    ("Agroknow", "Agroknow", "", "North America Sales", "sales_bd_partnerships", "", "2025-11-25", "evidence_bound", "2025-11-25", "unknown", "unknown", "none_observed", "B", "application", "rejected_no_interview", "2025-11-25", "unstated", "", "", "medium", "Thank you for time and interest. No ATS receipt.", "gth_0b21a7d38201ea0b"),
    ("Teleport", "Teleport", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-14", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-05-07", "unstated", "", "", "high", "", "gth_a6bb3627c1238c47"),
    ("Rollstack", "Rollstack", "", "AI Growth Hacker", "growth_demand_marketing", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_203f7f8e466356a4"),
    ("AirOps", "AirOps", "", "Growth Engineer", "growth_demand_marketing", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_b1fbc862c73e63af"),
    ("Cresta", "Cresta", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-10", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_fafd577be7e1a362"),
    ("Auctane", "Auctane", "", "Pre-Sales Engineer", "sales_solutions_engineering", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-14", "unstated", "", "", "high", "Receipt omits role; decline names Pre-Sales Engineer.", "gth_d72556f0129de181"),
    ("Redis", "Redis", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_aca478c7614dc9a5"),
    ("Ontra", "Ontra", "", "unspecified", "unspecified", "", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-24", "unstated", "", "", "high", "Role omitted on receipt.", "gth_97436fb778aec959"),
    ("LangChain", "LangChain", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-10", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_53fa9e4321b3a4a5"),
    ("Sur", "Sur", "", "AI Revenue Engineer", "explicit_gtm_engineering", "ai_product_vertical", "2026-04-09", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "rejected_no_interview", "2026-04-09", "unstated", "", "", "high", "", "gth_af0f7a3755fa52f3"),
    ("Sardine", "Sardine", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-09", "unstated", "", "", "high", "", "gth_19f71d91ee76b11c"),
    ("G2", "G2", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "role_paused_or_closed", "2026-04-09", "unstated", "", "", "high", "Position filled.", "gth_c812a60595be4bf8"),
    ("Fixify", "Fixify", "", "GTM Engineer (Contract)", "explicit_gtm_engineering", "plain", "2026-04-03", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Receipts 2026-04-03 and 2026-04-06 plus update. One cycle.", "gth_ff01acda1552b4d3"),
    ("Pearl", "Pearl, Inc.", "", "Lead GTM Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "Ashby receipt plus later interview scheduling artifacts.", "gth_6d883e4b5af47f48"),
    ("Valsoft", "Valsoft Corporation", "", "GTM Engineer, DockMaster", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Workable data copy gth_c2a80a454a3437ef.", "gth_776d2ab8ef4459b1"),
    ("Payabli", "Payabli", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_9c4cac8383da6f98"),
    ("Wrapbook", "Wrapbook", "", "GTM Systems Engineer", "explicit_gtm_engineering", "systems_operations", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "NDA request in confirmation.", "gth_ae2e875da34e8501"),
    ("AppGate", "AppGate Cybersecurity", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_1ab720344bcdf47a"),
    ("Tapcheck", "Tapcheck", "", "unspecified", "unspecified", "", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-06", "unstated", "", "", "high", "Thank you 2026-03-30; second thank you and decline 2026-04-06 treated as one cycle.", "gth_7ddb451e25699d53"),
    ("Solv Health", "Solv Health", "", "unspecified", "unspecified", "", "2026-04-06", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "rejected_no_interview", "2026-04-21", "unstated", "", "", "high", "Role omitted on receipt.", "gth_fa5b40e229082ec9"),
    ("Unframe", "Unframe", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-12", "remote", "", "", "high", "Second Greenhouse receipt 2026-04-17 merged as same opening. IDs gth_4c96edfc630dd59e and gth_d4f5b5bf940f71d3.", "gth_4c96edfc630dd59e"),
    ("Rula", "Rula", "", "GTM Engineer Remote", "explicit_gtm_engineering", "plain", "2026-04-06", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-04-22", "remote", "", "", "high", "", "gth_b6c113b453e1bffe"),
    ("Liatrio", "Liatrio", "", "GTM RevOps Engineer", "explicit_gtm_engineering", "systems_operations", "2026-04-05", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_f3649f1c5cd028b0"),
    ("Virtru", "Virtru", "", "Director of Go-to-Market AI", "explicit_gtm_engineering", "ai_product_vertical", "2026-03-09", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-04-04", "unstated", "Director", "", "high", "Greenhouse thank you 2026-03-09; decline names the director role.", "gth_b58175071492ba76"),
    ("CompanyCam", "CompanyCam", "", "GTM Systems Engineer", "explicit_gtm_engineering", "systems_operations", "2026-04-03", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_a6efa263112ad015"),
    ("Brand.ai", "brand.ai", "", "GTME", "explicit_gtm_engineering", "plain", "2026-04-02", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-04-07", "unstated", "", "", "high", "Sent mail to eml_b7cd35bd64cf with portfolio. Comp discussion then rejection in same thread.", "gth_187b8559e8b2ddc3"),
    ("Boulevard", "Boulevard", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-31", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-04", "unstated", "", "", "high", "", "gth_d406fc3067b6a28c"),
    ("DISQO", "DISQO", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-31", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "rejected_no_interview", "2026-03-31", "unstated", "", "", "high", "Canonical DISQO not DSQO.", "gth_824453c938188f5e"),
    ("PhrasIQ", "PhrasIQ", "", "unspecified", "unspecified", "", "2026-03-31", "exact", "", "wellfound", "wellfound_apply", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Wellfound: application accepted, schedule interview. Role omitted. Calendar Discovery 2026-04-02. Relay mentions GTM System Deep Dive after Discovery Session.", "gth_e9be0ace83621c85"),
    ("Mento", "Mento", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Second thank you 2026-03-30 merged.", "gth_96c704b7fa571558"),
    ("Tiger Data", "Tiger Data", "", "GTM AI Engineer", "explicit_gtm_engineering", "ai_product_vertical", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-03-30", "unstated", "", "", "high", "", "gth_69cec22bbb737c42"),
    ("Vercel", "Vercel", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_507a0e29346925c4"),
    ("Roboflow", "Roboflow", "", "RevOps GTM Engineer", "explicit_gtm_engineering", "systems_operations", "2026-03-30", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_9bd9c95a760df71b"),
    ("Dagster Labs", "Dagster Labs", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_after_interview", "2026-04-03", "unstated", "", "", "high", "Receipt plus security-code resubmit same day. Delaney Housley thanked him for chatting 2026-04-03.", "gth_89b52fe76388035e"),
    ("Unstructured", "Unstructured", "", "GTM Engineer, Operations", "explicit_gtm_engineering", "systems_operations", "2026-03-30", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_a338fb40ebb27dbf"),
    ("PandaDoc", "PandaDoc", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-30", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-04-27", "unstated", "", "", "high", "Greenhouse security code plus no-reply@pandadoc.com We got it same day. Decline 2026-04-27.", "gth_02ae1915406326ae"),
    ("Adapt", "Adapt", "", "GTM Engineer / RevOps Lead", "explicit_gtm_engineering", "systems_operations", "2026-03-27", "exact", "", "unknown", "ats_direct", "Dover", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_692b221836ee7bf9"),
    ("Beautiful.ai", "Beautiful.ai", "", "unspecified", "unspecified", "", "2026-03-08", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_after_interview", "2026-03-26", "unstated", "", "", "high", "Role omitted on receipt. Interview process through at least 2026-03-19. Hiring manager Brandon Ness named in sent-mail thread.", "gth_93b7915bd98264ce"),
    ("Orchestry", "Orchestry", "", "GTM Engineer (Sales)", "explicit_gtm_engineering", "sales_presales", "2026-03-24", "exact", "", "unknown", "ats_direct", "Breezy", "A", "application", "rejected_after_interview", "2026-03-27", "unstated", "", "", "high", "Receipt, two recruiter-screen invites, missed interview, then post-process decline.", "gth_397ef5934d0939b2"),
    ("Pinterest", "Pinterest", "", "Apprentice Engineer", "product_ai_technical", "", "2026-03-25", "exact", "", "referral", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-04-28", "unstated", "Apprentice", "", "high", "Greenhouse application 2026-03-25. Distinct from June 2025 referral-accept messages which did not prove submission.", "gth_0b75334253c7b6e2"),
    ("Hypergen", "Hypergen", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-03-11", "exact", "", "unknown", "ats_direct", "Recruitee", "A", "application", "still_open", "", "unstated", "", "", "high", "Confirmation then interview invitation 2026-04-14 from people@hypergen.io.", "gth_d34cb1ecb8ba51f6"),
    ("Anthropic", "Anthropic", "", "Software Engineer, Business Technology", "product_ai_technical", "", "2026-03-08", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-03-09", "unstated", "", "", "high", "", "gth_c126aa1c636566e5"),
    ("SentiLink", "SentiLink", "", "Go-to-Market Strategy Analyst", "revops_gtm_ops_strategy", "", "2026-02-23", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-13", "unstated", "", "", "medium", "2026-02-23 thank you omits role. 2026-06-22 thank you. 2026-07-13 decline names Go-to-Market Strategy Analyst. One cycle.", "gth_b9233df609a22735"),
    ("TestGorilla", "TestGorilla", "", "Go-to-Market Engineer", "explicit_gtm_engineering", "plain", "2026-02-20", "exact", "", "unknown", "ats_direct", "Teamtailor", "A", "application", "still_open", "", "unstated", "", "", "high", "Assessment invitation plus recruiter intro same day. Recruiter update 2026-04-23.", "gth_f99a415b023fc244"),
    ("Smeetz", "Smeetz", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-02-20", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_d9ec75a3f4991195"),
    ("WilsonHCG", "WilsonHCG", "unknown", "Outbound Sales Consultant III", "sales_bd_partnerships", "", "2026-02-13", "exact", "", "unknown", "recruiter_submitted", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Agency thank you for application. Underlying employer unnamed. Distinct from later Dexian outreach on same title.", "gth_f2e8c95a6366fd5d"),
    ("Ambrook", "Ambrook", "", "Business Operations Lead", "revops_gtm_ops_strategy", "", "2026-02-11", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-02-12", "unstated", "", "", "high", "Second Ambrook role. Followup_sent to no-reply after rejection.", "gth_aad2435c82a5d834"),
    ("GitLab", "GitLab", "", "GTM Planning & Operations Analyst", "revops_gtm_ops_strategy", "", "2026-02-10", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "role_paused_or_closed", "2026-04-17", "unstated", "", "", "high", "", "gth_d806408b1ae0fa72"),
    ("Gather AI", "Gather AI", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-02-09", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_71a6f9dcebf0a9b0"),
    ("Manifold AI", "Manifold AI", "", "Growth Marketing Manager", "growth_demand_marketing", "", "2026-02-06", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-02-06", "unstated", "", "", "high", "", "gth_55db7a5c8e2dbd7a"),
    ("Verkada", "Verkada", "", "Enterprise Solutions Engineer, Atlanta", "sales_solutions_engineering", "", "2026-02-04", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "Atlanta", "unstated", "", "high", "", "gth_8fafa5db68268f59"),
    ("Beacon Software", "Beacon Software", "", "unspecified", "unspecified", "", "2026-01-26", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code then completed receipt 79 seconds later.", "gth_f9737e34553dc0b6"),
    ("Huzzle", "Huzzle", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Workable submitted successfully with data copy. Later Huzzle emails call an AI video interview required and also say talent pool. Coded as application from the Workable submission language.", "gth_27df3f45e3787608"),
    ("Adaptive6", "Adaptive6", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-04", "exact", "", "unknown", "ats_direct", "Comeet", "A", "application", "rejected_no_interview", "2026-06-16", "unstated", "", "", "high", "", "gth_522ae6cfc3094c5b"),
    ("4MindsAI", "4MindsAI", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Application #49830118.", "gth_1661e404aac612de"),
    ("RevSpring", "RevSpring", "", "Lead, Agentic Operations + GTM Engineering", "explicit_gtm_engineering", "founding_senior_lead", "2026-06-04", "exact", "", "recruiter_inbound", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "Newton receipt 2026-06-04; duplicate 2026-06-23; LinkedIn recruiter approach 2026-05-29; recruiter screen request 2026-06-10.", "gth_c6362282bdac9373"),
    ("Cloudflare", "Cloudflare", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-06-23", "unstated", "", "", "high", "", "gth_69c4854422c5249c"),
    ("Pogo Technologies", "Pogo Technologies", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-04", "exact", "", "unknown", "ats_direct", "Gem", "A", "application", "still_open", "", "unstated", "", "", "high", "Gem 2026-06-04. Gem 2026-06-26 and Ashby 2026-07-08 are later receipts on the same title with no terminal outcome, so they stay on c1.", "gth_4169aef833260ed9"),
    ("ServiceTrade", "ServiceTrade", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-05-29", "unstated", "", "", "high", "Role omitted on thank you.", "gth_4be457d1b02d7340"),
    ("CoLab Software", "CoLab Software", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Greenhouse thank you; hiring.colabsoftware.com Sales Engineer 2026-05-28.", "gth_ede7a771a6ee14a0"),
    ("Apollo.io", "Apollo.io", "", "unspecified", "unspecified", "", "2026-05-28", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Two identical receipts 62 seconds apart. Role omitted.", "gth_5b932a62ba112b24"),
    ("Airtable", "Airtable", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-05-21", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-05-27", "unstated", "", "", "high", "", "gth_9f99d96859f305bc"),
    ("Pindrop", "Pindrop", "", "GTM Systems Platform Specialist", "explicit_gtm_engineering", "systems_operations", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-27", "unstated", "", "", "high", "Thank you 2026-05-21 omits role; decline names the specialist title. Second thank you 2026-06-22 merged.", "gth_f0187eba1e53317a"),
    ("Speechify", "Speechify", "", "Go-to-Market Engineer, Atlanta", "explicit_gtm_engineering", "plain", "2026-05-25", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "Atlanta", "", "", "high", "", "gth_7a05cff9242e33b5"),
    ("EvenUp", "EvenUp", "", "AI Adoption Manager, Southeast", "other", "", "2026-05-25", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-06-04", "unstated", "", "", "high", "", "gth_aaf36ac9bb30b359"),
    ("Deepgram", "Deepgram", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-05-21", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-05-22", "unstated", "", "", "high", "", "gth_cecd897de39b6cdb"),
    ("Onit", "Onit", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_e4da05bda2874b5e"),
    ("TRACTIAN", "TRACTIAN", "", "Sales Engineer, Automation", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "Distinct from Senior GTM Engineer Hubspot 2026-05-19.", "gth_7c113a064b48c743"),
    ("Applied Systems", "Applied Systems", "", "Sales Enablement GTM Readiness Lead", "revops_gtm_ops_strategy", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "iCIMS", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "iCIMS verify, welcome, and receipt within 28 seconds.", "gth_d2bd22c2adab0841"),
    ("VitalSource", "VitalSource", "", "AI Enablement Lead", "other", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Jobvite", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "", "gth_06b529b78053784a"),
    ("Telnyx", "Telnyx", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_cea9fa54c06f8873"),
    ("ApartmentIQ", "ApartmentIQ", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-28", "unstated", "", "", "high", "Role omitted on receipt.", "gth_edc01e260d0ef795"),
    ("NICE", "NICE", "", "AI Solution Strategist", "sales_solutions_engineering", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_49380f0d59aa0532"),
    ("Nebius", "Nebius", "", "Director GTM Physical AI", "explicit_gtm_engineering", "ai_product_vertical", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-16", "unstated", "Director", "", "medium", "2026-05-21 thank you omits role. 2026-07-16 decline names Director GTM Physical AI. One cycle.", "gth_5d842e9f33e019d8"),
    ("DBeaver", "DBeaver", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-05", "unstated", "", "", "high", "", "gth_a0c4d42732c12c24"),
    ("FOSSA", "FOSSA", "", "unspecified", "unspecified", "", "2026-04-22", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-20", "unstated", "", "", "high", "Cycle 1. Role omitted. Terminal 2026-05-20 licenses c2.", "gth_a1f6e4b0fb7a200c"),
    ("FOSSA", "FOSSA", "", "unspecified", "unspecified", "", "2026-05-21", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Cycle 2 after 2026-05-20 decline. Subject says second cycle.", "gth_f8fa8c334b800ad6"),
    ("TRACTIAN", "TRACTIAN", "", "Senior GTM Engineer, Hubspot", "explicit_gtm_engineering", "systems_operations", "2026-05-19", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "Senior", "", "high", "", "gth_0ab53d541a00e4e3"),
    ("10x Genomics", "10x Genomics", "", "unspecified", "unspecified", "", "2026-05-02", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-05-14", "unstated", "", "", "high", "Two receipts 14 seconds apart from greenhouse-mail and careers.10xgenomics.com.", "gth_176c6e733d1bb47d"),
    ("Trase", "Trase", "", "GTM Engineer, Healthcare", "explicit_gtm_engineering", "ai_product_vertical", "2026-04-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-10", "unstated", "", "", "high", "2026-04-27 thank you omits healthcare modifier; 2026-06-26 thank you; 2026-07-10 decline names Healthcare. One cycle not two: no terminal between April and June receipts.", "gth_18c36945a10db7a4"),
    ("OXOS Medical", "OXOS Medical", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-27", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_e120aa29b59c54b8"),
    ("WallStreetQuants", "WallStreetQuants", "", "unspecified", "unspecified", "", "2026-04-17", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted on data-copy thank you.", "gth_d116539760cbc15e"),
    ("Built Recruiting", "Built Recruiting", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-16", "evidence_bound", "2026-04-16", "unknown", "ats_direct", "Greenhouse", "B", "application", "role_paused_or_closed", "2026-04-16", "unstated", "", "", "medium", "Position filled update. No earlier receipt.", "gth_0673b068984d168e"),
    ("Mercor", "Mercor", "", "Sales Engineering Expert", "sales_solutions_engineering", "", "2026-08-18", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-08-25", "remote", "", "", "high", "Application Submitted receipt. Per-application register.", "gth_ed5180a0df62cd59"),
    ("Mercor", "Mercor", "", "B2B Sales Expert", "sales_bd_partnerships", "", "2026-08-18", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-08-25", "remote", "", "", "high", "", "gth_8a2cdb8923883118"),
    ("Mercor", "Mercor", "", "Sales and Marketing Expert", "growth_demand_marketing", "", "2026-08-18", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "still_open", "", "remote", "", "", "high", "", "gth_49e6eeca403b197b"),
    ("Mercor", "Mercor", "", "Biology & Biophysics Research Collaborator", "product_ai_technical", "", "2026-07-20", "exact", "", "referral", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-07-27", "remote", "", "", "high", "Application Submitted on Cincinnatus. Referral from Victor Ekuta same day is a separate pathway.", "gth_81d08aee9ab37889"),
    ("Mercor", "Mercor", "", "Education / school Evaluator", "other", "", "2026-06-22", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-06-29", "remote", "", "", "high", "", "gth_0d17ddc7df5b3ff5"),
    ("Mercor", "Mercor", "", "General Sales / GTM Evaluator", "sales_bd_partnerships", "", "2026-06-22", "exact", "", "unknown", "marketplace_profile_submission", "none_observed", "A", "application", "rejected_no_interview", "2026-06-29", "remote", "", "", "high", "", "gth_76956966f57e2d8c"),
    ("Uncapped", "Uncapped", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-08-22", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "rejected_no_interview", "2026-08-25", "unstated", "", "", "high", "", "gth_ad4706bd7af58097"),
    ("OpenObserve", "OpenObserve", "", "Growth Marketer", "growth_demand_marketing", "", "2026-08-24", "evidence_bound", "2026-08-24", "unknown", "ats_direct", "Ashby", "B", "application", "rejected_no_interview", "2026-08-24", "unstated", "", "", "medium", "Decline update. No earlier receipt in corpus.", "gth_251fa3a1016af3d2"),
    ("LiveKit", "LiveKit", "", "GTM Systems Engineer", "explicit_gtm_engineering", "systems_operations", "2026-07-20", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-08-17", "unstated", "", "", "high", "", "gth_e469b6dd5dcf57de"),
    ("Tripleseat", "Tripleseat", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-08-06", "exact", "", "unknown", "recruiter_submitted", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Hirebridge: profile submitted to Tripleseat #611301.", "gth_1c8c8c22b376b3eb"),
    ("Great Question", "Great Question", "", "Senior Demand Generation Manager", "growth_demand_marketing", "", "2026-07-17", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_after_interview", "2026-07-29", "unstated", "Senior", "", "high", "Receipt, screening scheduling, two interview reminders, post-interview decline.", "gth_cf236998e25c2988"),
    ("Gradient Labs", "Gradient Labs", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-21", "evidence_bound", "2026-07-21", "unknown", "unknown", "Ashby", "B", "application", "rejected_no_interview", "2026-07-27", "unstated", "", "", "medium", "ZipRecruiter prompt to complete plus later Ashby decline. No completed-receipt phrase on ZipRecruiter for this employer.", "gth_ea6ecb88f1968d3e"),
    ("AI Digital", "AI Digital", "", "Growth Director", "growth_demand_marketing", "", "2026-07-24", "exact", "", "ladders", "apply4me_agent", "none_observed", "A", "application", "rejected_no_interview", "2026-07-27", "unstated", "Director", "", "high", "Apply4Me Application Sent plus employer decline.", "gth_1d99ac00eaaf286d"),
    ("IBM", "IBM", "Confluent", "Manager, Applied AI & GTM Systems", "explicit_gtm_engineering", "systems_operations", "2026-06-22", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-07-26", "unstated", "Manager", "", "high", "IBM submission confirmation Ref [redacted] Candidate ID [redacted]. Decline names Confluent.", "gth_3f4c8312020cfc53"),
    ("Hightouch", "Hightouch", "", "Go-to-Market Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-24", "unstated", "", "", "high", "Security code then receipts 2026-07-15 and 2026-07-22 merged as one cycle.", "gth_2477b047c9eee060"),
    ("Lattice", "Lattice", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-24", "exact", "", "ladders", "apply4me_agent", "Greenhouse", "A", "application", "role_paused_or_closed", "2026-08-04", "unstated", "", "", "high", "Apply4Me sent plus matching Greenhouse receipt same minute. Position filled 2026-08-04.", "gth_241e94478aaca3da"),
    ("Firstup", "Firstup", "", "Manager, GTM Systems", "explicit_gtm_engineering", "systems_operations", "2026-07-23", "exact", "", "ladders", "apply4me_agent", "Lever", "A", "application", "still_open", "", "unstated", "Manager", "", "high", "Apply4Me sent plus matching Lever receipt same minute.", "gth_d42d877d4ad1d8a6"),
    ("Clutch", "Clutch", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-19", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Receipt then 2026-07-22 note.", "gth_6f15db67a1602feb"),
    ("Owner.com", "Owner.com", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-22", "exact", "", "unknown", "ats_direct", "Ashby", "B", "application", "still_open", "", "unstated", "", "", "medium", "Subject GTM Engineer; body names Product Builder, GTM Product. Used subject verbatim. Conflict in notes.", "gth_42e02c48ed5bf0d4"),
    ("Revic", "Revic", "", "Founding GTM AI Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-21", "exact", "", "unknown", "unknown", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "ZipRecruiter: application is complete.", "gth_29fad35aef460808"),
    ("Lorikeet", "Lorikeet", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "role_paused_or_closed", "2026-07-20", "unstated", "", "", "high", "", "gth_3021dd8327f18e33"),
    ("Hyperbound", "Hyperbound", "", "Founding RevOps Lead", "revops_gtm_ops_strategy", "", "2026-07-17", "evidence_bound", "2026-07-17", "unknown", "ats_direct", "Ashby", "B", "application", "rejected_no_interview", "2026-07-17", "unstated", "Founding", "", "medium", "Decline names the role. No earlier receipt.", "gth_98e8de23b25e899a"),
    ("Toast", "Toast", "", "GTM Engineer, Sales Workflow Automation", "explicit_gtm_engineering", "sales_presales", "2026-06-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-16", "unstated", "", "", "high", "Thanks 2026-06-24 omits modifier; decline 2026-07-16 names Sales Workflow Automation.", "gth_8c8f0f471d0e4a6b"),
    ("Together AI", "Together AI", "", "unspecified", "unspecified", "", "2026-07-13", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code 2026-07-13 then receipts 07-13 and 07-15. Role omitted. One cycle.", "gth_95609241ea8ee9d7"),
    ("HUD", "HUD", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-16", "unstated", "", "", "high", "", "gth_0551733f2c4f4e2f"),
    ("Higgsfield", "Higgsfield", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_585f47fb9573f77c"),
    ("GatherUp", "GatherUp", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_7f32aa0dee0844c6"),
    ("BrightHire", "BrightHire", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_06030ef7ce1a1a86"),
    ("Scribe", "Scribe", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_ebcaa0e3a26e7ae0"),
    ("Nooks", "Nooks", "", "GTM Engineer, Marketing", "explicit_gtm_engineering", "growth_marketing", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_48896200b75b682e"),
    ("Yuno", "Yuno", "", "Go To Market Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_acdf2f35318498c8"),
    ("Handshake", "Handshake", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_375082948ea0ff94"),
    ("Attentive", "Attentive", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-22", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-07-07", "unstated", "", "", "high", "Cycle 1.", "gth_ed449ca6f36aaabd"),
    ("Attentive", "Attentive", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Cycle 2 after 2026-07-07 decline.", "gth_07f5c11803468801"),
    ("Anduril Industries", "Anduril Industries", "", "Technical Operations Engineer, Launched Effects", "product_ai_technical", "", "2026-06-21", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-07-15", "unstated", "", "", "medium", "2026-06-21 names Technical Operations Engineer. 2026-07-15 recruiting.anduril.com thank you/decline omits that title. Treated as one cycle.", "gth_c8b5ddd27cce25d9"),
    ("Productboard", "Productboard", "", "Associate GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-13", "exact", "", "unknown", "ats_direct", "Gem", "A", "application", "still_open", "", "unstated", "Associate", "", "high", "Gem GTM Engineer 2026-07-13 and Associate GTM Engineer 2026-07-15. Same company, similar titles, no terminal between. Merged as one cycle using the more specific listed title from 07-15.", "gth_fa753c8961d636b5"),
    ("Hologram", "Hologram", "", "GTM Engineer Pre-Sales", "explicit_gtm_engineering", "sales_presales", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code then activated. Screening Amy Schwartz 2026-07-20. Cross-functional Derrick Calderon 2026-07-22.", "gth_40e600e56434c3e4"),
    ("Axiad", "Axiad", "", "unspecified", "unspecified", "", "2026-07-15", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "Security code then thank you. Role omitted.", "gth_77fd2a371a72600e"),
    ("Conversion", "Conversion", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-14", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_a06a83e64880f9a3"),
    ("Anysphere", "Cursor", "", "GTM, Emerging Products", "explicit_gtm_engineering", "ai_product_vertical", "2026-07-12", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-13", "unstated", "", "", "high", "Company as listed Cursor. Canonical Anysphere.", "gth_15accea51012a907"),
    ("HartleyCo", "HartleyCo", "Bluejay", "Founding GTM", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-13", "evidence_bound", "2026-07-13", "recruiter_inbound", "recruiter_submitted", "none_observed", "B", "application", "rejected_after_interview", "2026-07-23", "unstated", "Founding", "", "high", "Josh Kelly thread regarding GTM Engineer application then 2026-07-23 decline of Founding GTM at Bluejay after the process. Recruiter thank-you-for-applying rule. Client named Bluejay on the decline.", "gth_59384916f1d2f6ca"),
    ("Patch", "Patch", "", "Growth Engineering Lead", "growth_demand_marketing", "", "2026-07-13", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "", "gth_732e82afc70cd870"),
    ("Talentpluto", "talentpluto", "unknown", "Go-to-Market Engineer", "explicit_gtm_engineering", "plain", "2026-07-12", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "high", "Workable submitted successfully with data copy. Talentpluto later said process incomplete pending a Pluto call. Underlying employer unnamed.", "gth_178d1a4678c84ee6"),
    ("Talentpluto", "talentpluto", "unknown", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-07-12", "exact", "", "unknown", "ats_direct", "Workable", "A", "application", "still_open", "", "unstated", "", "", "medium", "Second Workable submission three minutes later, title GTM Engineer vs Go-to-Market Engineer. Counted as second role not a duplicate because titles differ as listed.", "gth_178d1a4678c84ee6"),
    ("Listen Labs", "Listen Labs", "", "Lead GTM Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-12", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Lead", "", "high", "", "gth_a5148313a18f5ac0"),
    ("Confido", "Confido", "", "Founding GTM Engineer", "explicit_gtm_engineering", "founding_senior_lead", "2026-07-12", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "", "gth_bcd329b8b94614f7"),
    ("Douglas County School System", "Douglas County School System", "", "unspecified", "other", "", "2026-07-09", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "AppliTrack submission confirmed 7/9/2026. Role omitted.", "gth_4e49e610ace41a16"),
    ("jobmail.io", "jobmail.io", "unknown", "Growth Lead", "growth_demand_marketing", "", "2026-07-07", "exact", "", "unknown", "unknown", "none_observed", "A", "application", "rejected_no_interview", "2026-07-13", "unstated", "", "", "high", "Stealth company unnamed. Decline says steps completed through Jack.", "gth_531b132d1253925a"),
    ("InRule Technology", "InRule Technology", "", "unspecified", "unspecified", "", "2026-07-06", "exact", "", "unknown", "ats_direct", "Rippling", "A", "application", "still_open", "", "unstated", "", "", "high", "Role omitted.", "gth_14681505c9f65ec0"),
    ("UpGuard", "UpGuard", "", "SDR Manager", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Lever", "A", "application", "rejected_no_interview", "2026-06-29", "unstated", "", "", "high", "", "gth_4b10eb2f1db76d3b"),
    ("MinIO", "MinIO", "", "BDR Enterprise", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "rejected_no_interview", "2026-06-27", "unstated", "", "", "high", "", "gth_40f5f65ab5d529af"),
    ("Tekion", "Tekion", "", "Senior Manager Inside Sales", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-27", "unstated", "Senior Manager", "", "high", "", "gth_653430f586268a32"),
    ("City Schools Of Decatur", "City Schools Of Decatur", "", "unspecified", "other", "", "2026-06-26", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "AppliTrack started then submission confirmed 6/26/2026. Role omitted.", "gth_a6bd68e720c8c398"),
    ("WireScreen", "WireScreen", "", "Partnerships Manager", "sales_bd_partnerships", "", "2026-06-25", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-07-03", "unstated", "", "", "high", "", "gth_e7ee14570ffe622a"),
    ("Clay", "Clay", "", "Growth Strategist, Enterprise", "growth_demand_marketing", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-06-25", "unstated", "", "", "high", "", "gth_b54ed1d0b7cd70ca"),
    ("Automation Anywhere", "Automation Anywhere", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Workday", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_7eb495f5480f0b39"),
    ("Canals", "Canals", "", "Sales Manager", "sales_bd_partnerships", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_e4e764ac5937a26a"),
    ("StackAI", "StackAI", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_c08064541ef65721"),
    ("Enlace Health", "Enlace Health", "", "Sales Engineer", "sales_solutions_engineering", "", "2026-06-24", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "rejected_no_interview", "2026-06-26", "unstated", "", "", "high", "", "gth_af78469adf88e697"),
    ("Jobgether", "Jobgether", "unknown", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-22", "exact", "", "unknown", "unknown", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Jobgether next-steps plus match score. Underlying employer unnamed.", "gth_39fd61eed7768f9e"),
    ("Syncro", "Syncro", "", "GTM Operations Manager", "revops_gtm_ops_strategy", "", "2026-06-22", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_331d3bc7e9183987"),
    ("Wealth.com", "Wealth.com", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-22", "exact", "", "unknown", "ats_direct", "Ashby", "A", "application", "rejected_no_interview", "2026-06-22", "unstated", "", "", "high", "", "gth_31cf19b2d7f93c6d"),
    ("Armada", "Armada", "", "AI Factory, Value Engineer", "sales_solutions_engineering", "", "2026-06-22", "exact", "", "unknown", "ats_direct", "Greenhouse", "A", "application", "still_open", "", "unstated", "", "", "high", "", "gth_56900e76d4a66f13"),
    ("Atlanta Public Schools", "Atlanta Public Schools", "", "unspecified", "other", "", "2026-06-19", "exact", "", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-06-22", "unstated", "", "", "high", "AppliTrack submission confirmed 6/19/2026 5:09:44 PM. APS later said not accepting substitute applications. Both facts recorded.", "gth_69afd05b60e34a48"),
    ("The Hog", "The Hog", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-15", "evidence_bound", "2026-06-15", "unknown", "unknown", "none_observed", "B", "application", "still_open", "", "unstated", "", "", "medium", "No ATS receipt. Invitation to GTM Interview plus take-home. Coded as application because the employer process names GTM Engineer and a take-home assignment. Evidence-bound to the invitation date. Could have been opportunity; chose application from role-titled process plus assignment.", "gth_d1989dfb9542a2da"),
    ("RevPartners", "RevPartners", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-06-24", "exact", "", "unknown", "ats_direct", "Teamtailor", "A", "application", "still_open", "", "unstated", "", "", "high", "Teamtailor complete-application plus later status messages.", "gth_90376d5350b9a83a"),
    ("Practical Prospecting", "Practical Prospecting", "", "unspecified", "unspecified", "", "2026-05-20", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Sent resume to eml_c52a64cf2d7a. Role omitted in subject.", "gth_75b7c8464647fdc0"),
    ("Spider.cloud", "Spider.cloud", "", "Growth lead", "growth_demand_marketing", "", "2026-05-03", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "Sent: Growth lead app.", "gth_f8fe98826a08e486"),
    ("AICRO", "AICRO", "", "GTM Engineering Team Lead", "explicit_gtm_engineering", "founding_senior_lead", "2026-02-06", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Team Lead", "", "high", "Sent to eml_5ae85b46cbf3.", "gth_4d6db773dc5a1ad3"),
    ("Nero", "Nero", "", "Founding Engineer", "product_ai_technical", "", "2026-01-07", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "Founding", "", "high", "Founding Engineer Application, video attached.", "gth_fc0da77b80de52c2"),
    ("Insignia Collab", "Insignia Collab", "", "unspecified", "unspecified", "", "2025-11-18", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "Atlanta", "", "", "medium", "Sent resume. Subject is operator/architect/Atlanta resident. Role as listed unspecified.", "gth_1aa4bb3bc36115a4"),
    ("Inertia Growth", "Inertia Growth", "", "Outbound Campaign Manager", "growth_demand_marketing", "", "2025-07-26", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "rejected_no_interview", "2025-07-30", "unstated", "", "", "high", "Sent GTME role resume 2025-07-26. Decline 2025-07-30 names Outbound Campaign Manager Role. Used the decline's listed title.", "gth_fa180bfd756b2a92"),
    ("Inven.ai", "Inven.ai", "", "unspecified", "unspecified", "", "2025-06-11", "exact", "", "unknown", "email_direct", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "medium", "Sent resume. Role omitted.", "gth_2dc7b54c89818c53"),
    ("Every.to", "Every.to", "", "GTM Engineer", "explicit_gtm_engineering", "plain", "2026-04-20", "evidence_bound", "2026-04-20", "unknown", "unknown", "none_observed", "A", "application", "still_open", "", "unstated", "", "", "high", "eml_50d007c54e63 thanks for applying for the GTM Engineer role. Call booked. No ATS receipt.", "gth_3731d4c2c0e7637c"),
    ("Switchyards", "Switchyards", "", "Launch Manager", "other", "", "2025-08-08", "evidence_bound", "2025-08-08", "unknown", "email_direct", "none_observed", "B", "application", "rejected_no_interview", "2025-08-19", "unstated", "", "", "medium", "Kayla thread plus Brooks Launch Manager. Resume review. No ATS receipt.", "gth_94d60ee6f87c1b6f"),
    ("Switchyards", "Switchyards", "", "Digital Product Builder", "product_ai_technical", "", "2026-04-25", "evidence_bound", "2026-04-25", "unknown", "unknown", "none_observed", "B", "application", "rejected_no_interview", "2026-04-25", "unstated", "", "", "medium", "Decline thank-you. No ATS receipt. Distinct role from Launch Manager.", "gth_9a641357cd288f9d"),
    ("Lumenalta", "Lumenalta", "", "unspecified", "unspecified", "", "2026-03-24", "exact", "", "unknown", "unknown", "none_observed", "B", "application", "still_open", "", "unstated", "", "", "medium", "You're In next-step 2026-03-24; update 2026-04-10. Role omitted.", "gth_9b9158b0f51fd5c0"),
    ("Stellar Substitute", "Stellar Substitute", "", "unspecified", "other", "", "2026-07-28", "evidence_bound", "2026-07-28", "unknown", "ats_direct", "none_observed", "B", "application", "role_paused_or_closed", "2026-07-28", "unstated", "", "", "medium", "Frontline position filled notice. Role omitted beyond substitute.", "gth_d48351490423f643"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Murphey Candler ES", "other", "", "2026-08-11", "evidence_bound", "2026-08-11", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-11", "unstated", "", "", "high", "Position you applied for has been filled. Distinct school.", "gth_3ee7a7fafe9feee4"),
    ("DeKalb County School District", "DeKalb County School District", "", "Specialty Area STAR Substitute, Margaret Harris Comprehensive", "other", "", "2026-08-06", "evidence_bound", "2026-08-06", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-06", "unstated", "", "", "high", "", "gth_555da3709c031999"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Chapel Hill ES", "other", "", "2026-07-14", "evidence_bound", "2026-07-14", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-04", "unstated", "", "", "medium", "Filled notices 2026-07-14 and 2026-08-04 for Chapel Hill ES. One cycle, two notices, not a second posting without a new submission date.", "gth_24b057d92a4bfdae"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Canby Lane ES", "other", "", "2026-08-04", "evidence_bound", "2026-08-04", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-08-04", "unstated", "", "", "high", "", "gth_5e8021bc96301627"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area High School STAR Substitute, Columbia HS", "other", "", "2026-07-28", "evidence_bound", "2026-07-28", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-28", "unstated", "", "", "high", "", "gth_538352b44682647e"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Cedar Grove ES", "other", "", "2026-07-27", "evidence_bound", "2026-07-27", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-27", "unstated", "", "", "high", "", "gth_121caf4f0a6b0482"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 1 Elementary STAR Substitute, Ashford Park ES", "other", "", "2026-07-24", "evidence_bound", "2026-07-24", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-24", "unstated", "", "", "high", "", "gth_d1725cb9ebb1f225"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 4 Elementary Substitute STAR, Browns Mill ES", "other", "", "2026-07-22", "evidence_bound", "2026-07-22", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-22", "unstated", "", "", "high", "", "gth_1452981a99c8574e"),
    ("DeKalb County School District", "DeKalb County School District", "", "Area 3 Elementary STAR Substitute, Rowland ES", "other", "", "2026-07-14", "evidence_bound", "2026-07-14", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-14", "unstated", "", "", "high", "", "gth_dff168bf3a176124"),
    ("DeKalb County School District", "DeKalb County School District", "", "Horizon Area Substitute STAR, Flat Rock ES", "other", "", "2026-07-08", "evidence_bound", "2026-07-08", "unknown", "ats_direct", "none_observed", "A", "application", "role_paused_or_closed", "2026-07-08", "unstated", "", "", "high", "", "gth_0545dc889f7add62"),
]

# Opportunity register: recruiter/referral/matching with no submission, still in dataset.
OPPS: list[tuple] = [
    ("WorkOS", "WorkOS", "WorkOS", "GTM Engineer", "explicit_gtm_engineering", "plain", "2025-08-25", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "remote", "", "", "high", "TopHire Somya Shruti approach. Interest confirmed, slot booked, resume requested. No submission receipt.", "gth_7c798c988d52c12f"),
    ("ThriveLink", "ThriveLink", "", "Healthcare Business Development Rep", "sales_bd_partnerships", "", "2025-08-05", "exact", "", "referral", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Josh Pappas referral introduction. No ATS submission artifact.", "gth_8469ad4868580c10"),
    ("Mercor", "Mercor", "", "Growth Strategist", "growth_demand_marketing", "", "2026-08-20", "exact", "", "recruiter_inbound", "unknown", "none_observed", "A", "opportunity", "offer_accepted", "2026-08-21", "remote", "", "", "high", "Instant Work Offer states he did not apply directly. Recruiter Claire Gauthier path. Contract activated 2026-08-21. Not in application census.", "gth_da5b9d0848d88f36"),
    ("micro1", "micro1", "unknown", "AI Training Pilot Project", "other", "", "2026-01-14", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Profile submitted to unnamed client by micro1. Matching pathway.", "gth_840667159906faf1"),
    ("Dexian", "Dexian", "unknown", "Outbound Sales Consultant III (Remote)", "sales_bd_partnerships", "", "2026-06-05", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "remote", "", "", "high", "Recruiter approach. No submission. Distinct intermediary from WilsonHCG.", "gth_b2e79fb0aee71c4d"),
    ("Luzmo", "Luzmo", "", "SDR", "sales_bd_partnerships", "", "2026-06-30", "exact", "", "jobright", "unknown", "none_observed", "C", "opportunity", "still_open", "", "unstated", "", "", "high", "Jobright recruiter sequence. No application evidence.", "gth_bc1e528deaa64ce8"),
    ("Glytec", "Glytec", "", "unspecified", "unspecified", "", "2026-01-27", "evidence_bound", "2026-01-27", "unknown", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Interview logistics and portfolio send. No submission receipt.", "gth_7ff12c525a38011d"),
    ("BX Studio", "BX Studio", "", "unspecified", "unspecified", "", "2026-04-08", "evidence_bound", "2026-04-08", "unknown", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Video sent, forwarded to hiring manager. No submission receipt.", "gth_cd9b1dc5bcc04d6c"),
    ("Crossing Hurdles", "Crossing Hurdles", "Montauk Capital", "Head of Commercial", "sales_bd_partnerships", "", "2026-04-01", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Ceipal via Crossing Hurdles. No submission receipt.", "gth_bd8f44c8203a9798"),
    ("SmartMode AI", "SmartMode AI", "", "unspecified", "unspecified", "", "2025-07-18", "exact", "", "recruiter_inbound", "unknown", "none_observed", "B", "opportunity", "still_open", "", "unstated", "", "", "medium", "Begin your interview process. No submission receipt.", "gth_6861df0094613c68"),
]

# Extra events beyond auto submission_receipt. (application_id_lookup via company|role|cycle, date, type, round, name, role, medium, system, eid, notes)
# Filled after apps are minted using keys.


def extra_event_specs(apps_by_key: dict[str, str]) -> list[dict[str, str]]:
    def k(company: str, role: str, cycle: int) -> str:
        return apps_by_key[aid(company, role, cycle)]

    specs: list[tuple] = [
        ("weave|business-development-manager|c1", "2025-07-31", "rejection", "", "Sarah", "unknown", "email", "gmail", "gth_c655f424a2f921dd", "Early decline before 2026 interview artifact."),
        ("weave|business-development-manager|c1", "2026-08-18", "hiring_manager_interview", "1", "unknown", "unknown", "unknown", "gmail", "gth_0339a17e3860d167", "Post-interview decline proves an interview occurred. Date of interview itself not on this artifact."),
        ("pearl|lead-gtm-engineer|c1", "2026-04-30", "hiring_manager_interview", "1", "Alex DeCeglie", "unknown", "unknown", "gmail", "gth_fb41d68a16ad8c02", "Interview @ Pearl scheduling."),
        ("pearl|lead-gtm-engineer|c1", "2026-05-04", "hiring_manager_interview", "2", "unknown", "unknown", "phone", "gmail", "gth_0bd16122f1878883", "Reminder upcoming interview May 5 phone."),
        ("pearl|lead-gtm-engineer|c1", "2026-05-11", "reschedule", "", "unknown", "unknown", "email", "gmail", "gth_d0d3b09bb98ccb1f", "Submit availability, duplicated 8 seconds apart."),
        ("pearl|lead-gtm-engineer|c1", "2026-05-17", "hiring_manager_interview", "3", "unknown", "unknown", "video", "gmail", "gth_36d7d2bba0740912", "Zoom reminder Lead GTM Engineer."),
        ("revspring|lead-agentic-operations-gtm-engineering|c1", "2026-05-29", "employer_ack", "", "Stephanie Cunningham", "recruiter", "email", "gmail", "gth_1202203d544f6fc9", "LinkedIn InMail preceding screen."),
        ("revspring|lead-agentic-operations-gtm-engineering|c1", "2026-06-10", "recruiter_screen", "1", "unknown", "recruiter", "unknown", "gmail", "gth_d679e7c78f455a3c", "Recruiter Screen Request."),
        ("the-hog|gtm-engineer|c1", "2026-06-15", "hiring_manager_interview", "1", "Hudson Liao", "unknown", "unknown", "gmail", "gth_d1989dfb9542a2da", "Invitation GTM Interview Jun 16."),
        ("the-hog|gtm-engineer|c1", "2026-06-18", "assessment_sent", "", "Hudson Liao", "unknown", "async", "gmail", "gth_df78e875e89e162f", "Take-home about 4 hours."),
        ("the-hog|gtm-engineer|c1", "2026-06-18", "technical_exercise", "2", "Hudson Liao", "unknown", "async", "gmail", "gth_df78e875e89e162f", "Take-home is a technical exercise event."),
        ("phrasiq|unspecified|c1", "2026-03-31", "employer_ack", "", "unknown", "founder", "email", "gmail", "gth_cb452c55c8d2edd9", "Founder outreach via Wellfound relay."),
        ("phrasiq|unspecified|c1", "2026-04-02", "hiring_manager_interview", "1", "unknown", "unknown", "video", "gcal", "cal_aa344a710f544818", "Calendar Discovery | Keegan Moody<>PhrasIQ."),
        ("phrasiq|unspecified|c1", "2026-04-06", "hiring_manager_interview", "2", "unknown", "unknown", "unknown", "gmail", "gth_cb452c55c8d2edd9", "GTM System Deep Dive proposed after Discovery Session."),
        ("hologram|gtm-engineer-pre-sales|c1", "2026-07-16", "employer_ack", "", "Megan Koch", "recruiter", "email", "gmail", "gth_2a3e6638763bef64", "Intro-call confirmation thread."),
        ("hologram|gtm-engineer-pre-sales|c1", "2026-07-20", "recruiter_screen", "1", "Amy Schwartz", "recruiter", "video", "gmail", "gth_fc3a24d02960b24e", "Preliminary Screening Call."),
        ("hologram|gtm-engineer-pre-sales|c1", "2026-07-22", "panel", "2", "Derrick Calderon", "unknown", "video", "gmail", "gth_966e3da56037f91c", "Cross-Functional Interview."),
        ("beautiful-ai|unspecified|c1", "2026-03-17", "hiring_manager_interview", "1", "Brandon Ness", "hiring manager", "unknown", "gmail", "gth_ec1fac33cf5f23f1", "Post-interview follow-up names HM."),
        ("beautiful-ai|unspecified|c1", "2026-03-26", "rejection", "", "Emily", "unknown", "email", "gmail", "gth_1186b66d0556feda", "Post-interview decline."),
        ("hypergen|gtm-engineer|c1", "2026-04-14", "hiring_manager_interview", "1", "unknown", "unknown", "unknown", "gmail", "gth_d34cb1ecb8ba51f6", "Interview invitation."),
        ("dagster-labs|gtm-engineer|c1", "2026-04-03", "hiring_manager_interview", "1", "Delaney Housley", "unknown", "unknown", "gmail", "gth_1c8ae3fa0432b375", "Thank you for taking the time to chat."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-24", "recruiter_screen", "1", "unknown", "recruiter", "video", "gmail", "gth_75b51a62759f69be", "Breezy recruiter screen."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-25", "recruiter_screen", "1", "unknown", "recruiter", "video", "gmail", "gth_f5dbe645e66b665d", "Second recruiter screen invite next day. Same round_number."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-25", "no_show", "", "unknown", "unknown", "video", "gmail", "gth_a704149be7e63a1a", "Missed interview."),
        ("orchestry|gtm-engineer-sales|c1", "2026-03-27", "rejection", "", "Jay Banga", "unknown", "email", "gmail", "gth_0051fcbedbb7f591", "Declined after interview process."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-24", "recruiter_screen", "1", "Harri", "unknown", "unknown", "gmail", "gth_8dc62a9ea6433a08", "Screening call scheduling."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-25", "hiring_manager_interview", "2", "unknown", "unknown", "video", "gmail", "gth_8d1927922b817f7a", "Interview reminder."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-26", "hiring_manager_interview", "2", "unknown", "unknown", "video", "gmail", "gth_83dac2c7d6e9c709", "Google Meet reminder."),
        ("great-question|senior-demand-generation-manager|c1", "2026-07-29", "rejection", "", "unknown", "unknown", "email", "gmail", "gth_5929227e95606d2a", "Post-interview decline."),
        ("testgorilla|go-to-market-engineer|c1", "2026-02-20", "assessment_sent", "", "Mirae Lee", "recruiter", "async", "gmail", "gth_f99a415b023fc244", "TestGorilla assessment invitation."),
        ("testgorilla|go-to-market-engineer|c1", "2026-02-20", "recruiter_screen", "1", "Mirae Lee", "recruiter", "email", "gmail", "gth_3e7b5aedf6286ab2", "Recruiter intro."),
        ("huzzle|gtm-engineer|c1", "2026-06-04", "assessment_sent", "", "unknown", "unknown", "async", "gmail", "gth_985129a717dc5459", "Required AI video interview."),
        ("every-to|gtm-engineer|c1", "2026-04-20", "hiring_manager_interview", "1", "Austin", "unknown", "unknown", "gmail", "gth_3731d4c2c0e7637c", "Call booked after thanks for applying."),
        ("hartleyco|founding-gtm|c1", "2026-07-13", "recruiter_screen", "1", "Josh Kelly", "recruiter", "unknown", "gmail", "gth_59384916f1d2f6ca", "Call scheduled same day."),
        ("hartleyco|founding-gtm|c1", "2026-07-23", "rejection", "", "Josh Kelly", "recruiter", "email", "gmail", "gth_2961922ee1e05822", "Founding GTM at Bluejay declined after process."),
        ("ambrook|business-operations-lead|c1", "2026-02-12", "followup_sent", "", "unknown", "unknown", "email", "gmail", "gth_028345fa3b82dbe0", "Reply to no-reply asking for elaboration."),
        ("ambrook|business-operations-lead|c1", "2026-02-12", "rejection", "", "unknown", "unknown", "email", "gmail", "gth_028345fa3b82dbe0", ""),
        ("workos|gtm-engineer|c1", "2025-08-25", "recruiter_screen", "1", "Somya Shruti", "recruiter", "unknown", "gmail", "gth_7c798c988d52c12f", "Slot booked. Opportunity register."),
        ("mercor|growth-strategist|c1", "2026-08-18", "recruiter_screen", "1", "Claire Gauthier", "recruiter", "unknown", "gmail", "gth_f7fead83a662997f", "Claire meeting."),
        ("mercor|growth-strategist|c1", "2026-08-21", "offer", "", "unknown", "unknown", "email", "gmail", "gth_04388c5d54511960", "Offer acceptance confirmation GTM Engineer hourly contract. Title on offer differs from Growth Strategist instant offer."),
        ("glytec|unspecified|c1", "2026-01-27", "hiring_manager_interview", "1", "unknown", "unknown", "unknown", "gmail", "gth_7ff12c525a38011d", "Interview logistics."),
        ("jobmail-io|growth-lead|c1", "2026-07-13", "recruiter_screen", "1", "Jack", "unknown", "unknown", "gmail", "gth_a1cbc75584147ef9", "Steps completed through Jack then declined."),
        ("atlanta-public-schools|unspecified|c1", "2026-06-22", "rejection", "", "unknown", "unknown", "email", "gmail", "gth_ddaf156bd72853f5", "Not currently accepting substitute applications."),
        ("fossa|unspecified|c1", "2026-05-20", "rejection", "", "unknown", "unknown", "email", "gmail", "gth_bd2f135e89181c88", "First cycle declined."),
        ("crypto-com|product-growth-hacker-exchange-main-app|c1", "2025-11-02", "rejection", "", "unknown", "unknown", "email", "gmail", "gth_a5db72a965bb0178", ""),
        ("huzzle|gtm-engineer|c1", "2026-06-11", "assessment_sent", "", "unknown", "unknown", "async", "gmail", "gth_9792f5230a698358", "Final reminder complete your interview."),
        ("pogo-technologies|gtm-engineer|c1", "2026-06-26", "employer_ack", "", "unknown", "unknown", "email", "gmail", "gth_cff42e6b8ec6e894", "Gem first-cycle note. Same title, no terminal on c1."),
        ("pogo-technologies|gtm-engineer|c1", "2026-07-08", "submission_receipt", "", "unknown", "unknown", "email", "gmail", "gth_613e210e3d23935a", "Ashby thank you. Same cycle as 2026-06-04 Gem receipt."),
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
    ("meshy-interview-prewindow", "2025-06-01", "Meshy", "unspecified", "out_of_window", "A submission receipt dated on or after 2025-06-01", "gmail", "gth_8fa8bbcc79f30307"),
    ("graph-one-not-in-ats", "2025-07-27", "graph.one", "unspecified", "attempted_not_submitted", "An ATS receipt the founder can see", "gmail", "gth_130b96eacec9f065"),
    ("beckhoff-incomplete-first", "2025-08-07", "Beckhoff Automation", "Sales Engineer", "attempted_not_submitted", "Superseded by 2025-08-08 completed rejection thanking him for applying", "gmail", "gth_c4c43ebac6543f68"),
    ("gwinnett-started-expired", "2026-06-08", "Gwinnett County Public Schools", "unspecified", "attempted_not_submitted", "AppliTrack submission confirmation", "gmail", "gth_2032ad4875645a59"),
    ("dekalb-general-expired", "2026-07-23", "DeKalb County School District", "unspecified", "attempted_not_submitted", "Already have position-level filled notices as applications. General file confirmation would still help", "gmail", "gth_32be8996b8ef0914"),
    ("gwinnett-expire-warning", "2026-07-04", "Gwinnett County Public Schools", "unspecified", "attempted_not_submitted", "Submission confirmation", "gmail", "gth_11a583cffff742fb"),
    ("sbga-prewindow", "2025-04-11", "SBGA", "Remote Outside Sales Rep", "out_of_window", "A submission inside 2025-06-01 to 2026-08-29", "gmail", "gth_c689e114e0941fe1"),
    ("umicas-openai", "2025-06-21", "getcrate.app / Umicas", "OpenAI Backend Software Engineer", "unresolvable_identity", "Employer-domain confirmation from OpenAI", "gmail", "gth_dabc46cd132a51bf"),
    ("umicas-google", "2025-06-21", "getcrate.app / Umicas", "Google Senior Software Engineer Gemini", "unresolvable_identity", "Employer-domain confirmation from Google", "gmail", "gth_3770b36755228c64"),
    ("crate-missing-materials", "2025-06-23", "Crate", "Software Engineering", "unresolvable_identity", "Employer-domain receipt", "gmail", "gth_73b9f98c99a2ac43"),
    ("pinterest-referral-pm", "2025-06-30", "Pinterest", "Product Manager II, Search", "attempted_not_submitted", "Submission confirmation. Referral accept said application may still be unsubmitted", "gmail", "gth_e9eb93833f5ab340"),
    ("pinterest-referral-apr", "2025-06-28", "Pinterest", "Apprentice Product Researcher", "attempted_not_submitted", "Submission confirmation", "gmail", "gth_ac4c278fe3c7ffbb"),
    ("gong-gdpr", "2025-07-08", "Gong.io", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "gth_a9bc41cdfddf6b61"),
    ("spot-ai-gdpr", "2025-07-26", "Spot AI", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "gth_07fb922f7018f5b8"),
    ("new-relic-retention", "2026-03-28", "New Relic", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "gth_99e82290d8b26754"),
    ("celonis-retention", "2026-04-02", "Celonis", "unspecified", "unresolvable_identity", "Dated submission receipt", "gmail", "gth_3d703a46e1412abb"),
    ("saveurdays-unnamed", "2026-04-11", "unknown", "unspecified", "unresolvable_identity", "Named employer and role plus submission language", "gmail", "gth_515966939c6fbad4"),
    ("mixmax-welcome", "2025-09-04", "Mixmax", "unspecified", "marketplace_profile", "An employment application receipt. Product welcome is not an application", "gmail", "gth_beb7124e93244a82"),
    ("apple-card", "2025-09-12", "Apple Card", "unspecified", "marketplace_profile", "Not employment", "gmail", "gth_3fe2a9bc11c39212"),
    ("leidos-dover-unverified", "2025-09-23", "Leidos Systems", "Software Engineer III REQ16295", "unresolvable_identity", "Employer-domain receipt. Sender is eml_93bc653507a1", "gmail", "gth_1d79fc9cee4208fb"),
    ("dover-rippling-sem", "2025-12-12", "Rippling", "Software Engineering Manager, Banking", "unresolvable_identity", "Employer-domain receipt. Sender eml_93bc653507a1", "gmail", "gth_31655c2958e28390"),
    ("wellfound-podium-saved", "2025-06-04", "Podium", "SDR", "attempted_not_submitted", "Wellfound application submitted receipt", "gmail", "gth_62004513dadf9afb"),
    ("wellfound-nomi-saved", "2025-07-16", "Nomi.ai", "Growth Hacker", "attempted_not_submitted", "Wellfound application submitted receipt", "gmail", "gth_b2786ede1d5085b4"),
    ("exa-product-june", "2025-06-12", "Exa", "unspecified", "consulting_prospect", "This is product outreach after API signup, not employment", "gmail", "gth_19ce04c195e366c4"),
    ("coldiq-accelerator", "2025-06-11", "ColdIQ", "Accelerator Program", "marketplace_profile", "Employment submission", "gmail", "gth_fb1f9d2f933f8ecd"),
    ("breakthrough-z", "2025-07-08", "Breakthrough Z", "Clarity Call", "consulting_prospect", "Employment application", "gmail", "gth_2fbc4346a1749093"),
    ("wells-fargo-banking", "2026-03-06", "Wells Fargo", "Clear Access Banking", "marketplace_profile", "Not a job application", "gmail", "gth_11b5eab2896d7f3d"),
    ("kimi-beta", "2026-06-20", "Kimi", "Code Beta Program", "marketplace_profile", "Not employment", "gmail", "gth_4eb58e96e49a35dd"),
    ("alibaba-paylater", "2026-06-21", "Alibaba.com", "Pay Later for Business", "marketplace_profile", "Not employment", "gmail", "gth_4d700ecc18af3ae8"),
    ("yc-profile-sharing", "2025-10-08", "Y Combinator Work at a Startup", "unspecified", "marketplace_profile", "Dashboard export of applied roles", "gmail", "gth_75ea4ea59eca0ed0"),
    ("anthropic-job-alerts", "2026-04-14", "Anthropic", "unspecified", "marketplace_profile", "Job alert is not an application", "gmail", "gth_d1b6761640fd5283"),
    ("ziprecruiter-alerts", "2026-07-21", "ZipRecruiter", "unspecified", "marketplace_profile", "A completed-application receipt for a named role", "gmail", "gth_6a4d3c24bfcfa43a"),
    ("jobright-alerts", "2025-11-18", "Jobright", "unspecified", "marketplace_profile", "Tracker export or application-submitted receipt", "gmail", "log-028"),
    ("jorge-gtme-calendar", "2026-04-29", "gtm-engineering.io", "unspecified", "unresolvable_identity", "Artifact stating this meeting was a job process", "gcal", "cal_58e3b990c3e121a5"),
    ("kivira-connect", "2026-04-06", "kivira.health", "unspecified", "consulting_prospect", "Submission or explicit job-interview language", "gcal", "cal_b8a710c6ac400259"),
    ("rocketeer-onboarding", "2026-04-07", "Rocketeer", "unspecified", "consulting_prospect", "Employment application", "gcal", "chn54lrp98p6uta7cor62rjqah432krfe5940gr1dgn66rrd"),
    ("common-room-chilipiper", "2026-05-28", "Common Room", "unspecified", "unresolvable_identity", "Purpose of meeting stated as job process plus submission", "gmail", "gth_b9d4242b85dd638d"),
    ("anyint-inmail", "2026-06-09", "unknown", "unspecified", "unresolvable_identity", "Named employer, role, and submission", "gmail", "gth_4f89ecf4c7cbd2dd"),
    ("greenhouse-unnamed-jul12", "2026-07-12", "unknown", "GTM Engineer", "unresolvable_identity", "Employer name on the Greenhouse receipt", "gmail", "gth_4b81cb9e7d93d7a6"),
    ("talentpluto-incomplete-chase", "2026-07-14", "Talentpluto", "unspecified", "attempted_not_submitted", "This chase is about an incomplete Pluto call. Workable submissions already coded as applications", "gmail", "gth_8c42db8841df92ac"),
    ("josh-pappas-clinics", "2026-06-04", "Pappas Healthtech", "unspecified", "consulting_prospect", "Employment application", "gmail", "gth_92516c1c9f589417"),
    ("certn-mercor-screen", "2026-08-21", "Mercor", "unspecified", "marketplace_profile", "Background screen is contract onboarding not a new application", "gmail", "gth_30e2ea2fdec22504"),
    ("micro1-finance-expert", "2026-01-21", "micro1", "Finance Expert", "recruiter_initiated", "Submission artifact", "gmail", "gth_505e2213c50c65c4"),
    ("micro1-chatgpt-pool", "2026-06-05", "micro1", "Certified Expert Pool", "recruiter_initiated", "Titled role submission", "gmail", "gth_b3bb07f0ab28b8d1"),
    ("the-hog-product-welcome", "2026-06-16", "The Hog", "unspecified", "marketplace_profile", "Product signup is not an application", "gmail", "gth_4f900acf4573a3ad"),
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
