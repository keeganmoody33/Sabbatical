#!/usr/bin/env python3
"""Freeze 2: code LinkedIn and Jobright applied lists, then match to Freeze 1.

Does not recode Gmail. Interviewed-ness is not stored. Relative LinkedIn
stamps stay relative_display with date_capture 2026-08-29. LinkedIn
submission_channel is unknown because the applied list does not label
Easy Apply versus external ATS.

A platform row that matches more than one Freeze 1 row is emitted with
match_status ambiguous and its candidate parent ids, and held out of the
full census. Counting an unresolved possible duplicate as net-new would
inflate the census with nothing downstream to correct it by.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "adjudication"
PLATFORM = ROOT / "coding" / "platform"
CAPTURE = "2026-08-29"
CODER = "freeze2"

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


def slug(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return cleaned or "unspecified"


def work_type(raw: str) -> str:
    lowered = (raw or "").strip().lower()
    if not lowered:
        return "unstated"
    if "hybrid" in lowered:
        return "hybrid"
    if "remote" in lowered:
        return "remote"
    if "on-site" in lowered or "onsite" in lowered or "on site" in lowered:
        return "onsite"
    return "unstated"


def role_lane(role: str) -> tuple[str, str]:
    title = (role or "").lower()
    if not title or title == "unspecified":
        return "unspecified", ""
    if any(k in title for k in ("gtm engineer", "go-to-market engineer", "go to market engineer", "gtm engineering", "go-to-market growth engineer", "marketing / gtm", "marketing gtm")):
        modifier = "plain"
        if any(k in title for k in ("founding", "lead", "senior", "director")):
            modifier = "founding_senior_lead"
        if "growth" in title:
            modifier = "growth_marketing"
        if any(k in title for k in ("ops", "operations", "systems", "enablement", "readiness")):
            modifier = "systems_operations"
        if any(k in title for k in ("product", "ai factory", "healthcare", "agents")):
            modifier = "ai_product_vertical"
        return "explicit_gtm_engineering", modifier
    if re.search(r"\bgtm\b", title) and any(k in title for k in ("founding", "lead", "strategy", "sales", "account")):
        if any(k in title for k in ("ops", "operations", "strategy analyst", "planning")):
            return "revops_gtm_ops_strategy", ""
        if "sales" in title or "account executive" in title:
            return "sales_bd_partnerships", ""
        return "explicit_gtm_engineering", "founding_senior_lead" if "founding" in title else "plain"
    if "gtm" in title and any(k in title for k in ("ops", "operations", "enablement", "readiness", "strategy")):
        return "revops_gtm_ops_strategy", ""
    if any(k in title for k in ("sales engineer", "solutions engineer", "pre-sales", "presales", "value engineer", "technical sales", "field sales")):
        return "sales_solutions_engineering", ""
    if any(k in title for k in ("forward deployed", "deployment strategist")):
        return "sales_solutions_engineering", ""
    if any(k in title for k in ("growth", "demand generation", "user acquisition", "content", "marketing")) and "engineer" not in title:
        return "growth_demand_marketing", ""
    if "growth engineer" in title:
        return "growth_demand_marketing", ""
    if any(k in title for k in ("sdr", "bdr", "business development", "account executive", "partnerships", "sdr manager")):
        return "sales_bd_partnerships", ""
    if any(k in title for k in ("product manager", "ai engineer", "technical operations")):
        return "product_ai_technical", ""
    if any(k in title for k in ("revops", "revenue operations")):
        return "revops_gtm_ops_strategy", ""
    return "other", ""


CANONICAL = {
    "anyspere inc.": "Anysphere",
    "anyspere": "Anysphere",
    "cursor": "Anysphere",
    "dsqo": "DISQO",
    "tekion corp": "Tekion",
    "4mindsai inc.": "4MindsAI",
    "cloudflare, inc.": "Cloudflare",
    "colab": "CoLab Software",
    "the hog (yc f25)": "The Hog",
    "jobright.ai": "Jobright.ai",
    "huzzle.com": "Huzzle",
    "anduril industries": "Anduril",
    "listen": "Listen Labs",
}


def canonical(name: str) -> str:
    raw = (name or "").strip()
    return CANONICAL.get(raw.lower(), raw)


def jobright_channel(method: str) -> str:
    value = (method or "").strip()
    if value == "Applied by Agent":
        return "jobright_agent"
    if value == "Direct Apply":
        return "unknown"
    return "unknown"


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def platform_row(
    *,
    company_listed: str,
    role: str,
    source: str,
    channel: str,
    date: str,
    precision: str,
    capture: str,
    location: str,
    work: str,
    level: str,
    salary: str,
    notes: str,
    register: str = "application",
    underlying: str = "",
) -> dict[str, str]:
    company = canonical(company_listed)
    role_clean = (role or "").strip() or "unspecified"
    lane, modifier = role_lane(role_clean)
    if lane != "explicit_gtm_engineering":
        modifier = ""
    aid = f"{slug(company)}|{slug(role_clean)}|c1"
    return {
        "coder_id": CODER,
        "application_id": aid,
        "cycle": "1",
        "company_canonical": company,
        "company_as_listed": company_listed.strip(),
        "underlying_employer": underlying,
        "role_as_listed": role_clean,
        "role_lane": lane,
        "gtm_modifier": modifier,
        "date_applied": date,
        "date_precision": precision,
        "date_capture": capture,
        "date_evidence_anchor": "",
        "discovery_source": source,
        "submission_channel": channel,
        "ats_system": "none_observed",
        "evidence_tier": "C",
        "evidence_class": "platform_log",
        "register": register,
        "terminal_outcome": "",
        "terminal_outcome_date": "",
        "terminal_outcome_precision": "",
        "location": location,
        "work_type": work_type(work),
        "level_as_listed": level,
        "salary_range_listed": salary or "not_stated",
        "confidence": "medium",
        "notes": notes,
    }


def code_jobright() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    apps: list[dict[str, str]] = []
    excl: list[dict[str, str]] = []
    for row in load_csv(ROOT / "artifacts" / "platform" / "jobright_applications_log.csv"):
        company = (row.get("Company") or "").strip()
        role = (row.get("Role Applied For") or "").strip()
        date = (row.get("Date Applied") or "").strip()
        if not company:
            excl.append(
                {
                    "coder_id": CODER,
                    "candidate_id": f"jobright-{slug(role)}-{date}",
                    "date": date,
                    "company": "",
                    "role": role,
                    "exclusion_reason": "unresolvable_identity",
                    "what_would_promote_it": "A company name on the tracker row.",
                    "evidence_system": "jobright",
                    "evidence_id": "jobright_applications_log.csv",
                }
            )
            continue
        underlying = ""
        if company.lower() in {"talentpluto", "jobgether"}:
            underlying = "unknown"
        notes = f"Jobright tracker. Application Method {row.get('Application Method') or 'not stated'}."
        apps.append(
            platform_row(
                company_listed=company,
                role=role,
                source="jobright",
                channel=jobright_channel(row.get("Application Method") or ""),
                date=date,
                precision="exact",
                capture="",
                location=row.get("Location") or "",
                work=row.get("Work Type") or "",
                level=row.get("Level") or "",
                salary=row.get("Salary Range") or "not_stated",
                notes=notes,
                underlying=underlying,
            )
        )
    return apps, excl


def code_linkedin() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    apps: list[dict[str, str]] = []
    excl: list[dict[str, str]] = []
    for i, row in enumerate(load_csv(ROOT / "artifacts" / "platform" / "linkedin_applied_jobs_pages_1_to_10.csv"), start=1):
        company = (row.get("company") or "").strip()
        role = (row.get("job_title") or "").strip()
        relative = (row.get("applied_date_relative") or "").strip()
        page = row.get("tracker_page") or ""
        if not company:
            excl.append(
                {
                    "coder_id": CODER,
                    "candidate_id": f"linkedin-blank-company-p{page}-r{i}",
                    "date": "",
                    "company": "",
                    "role": role,
                    "exclusion_reason": "unresolvable_identity",
                    "what_would_promote_it": "The company name on the applied-list row.",
                    "evidence_system": "linkedin",
                    "evidence_id": f"linkedin_applied_jobs_pages_1_to_10.csv#page{page}",
                }
            )
            continue
        register = "application"
        underlying = ""
        notes = (
            f"LinkedIn applied list page {page}. Stamp {relative}. "
            f"{row.get('posting_or_availability') or ''} {row.get('visible_activity') or ''}".strip()
        )
        if company.lower() in {"talentpluto", "jobgether"}:
            underlying = "unknown"
        if "method recruiting" in company.lower() or company.lower() in {"roc search", "crossing hurdles", "greenway collins", "horizonai talent", "franklin fitch", "intelli pro", "intellipro", "scout global"}:
            underlying = "unknown"
            notes += " Recruiter or agency listing. Client unnamed in this file."
        if "the hog" in company.lower():
            register = "opportunity"
            notes += " Freeze 1 adjudicated this opening as opportunity. Platform row kept out of the application census."
        apps.append(
            platform_row(
                company_listed=company,
                role=role,
                source="linkedin",
                channel="unknown",
                date="",
                precision="relative_display",
                capture=CAPTURE,
                location=row.get("location") or "",
                work=row.get("workplace_type") or "",
                level="",
                salary="not_stated",
                notes=notes,
                register=register,
                underlying=underlying,
            )
        )
    return apps, excl


def norm_company(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


def norm_role(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


ROLE_ALIASES = {
    ("anaconda", "seniorbusinessdevelopmentrepresentative"): "seniorbdr",
    ("fossa", "gtmengineer"): "gtmengineer",
    ("unframe", "gtmengineerremote"): "gtmengineer",
    ("minio", "businessdevelopmentrepresentativeenterprise"): "bdrenterprise",
    ("tekion", "seniormanagerinsidesales"): "seniormanagerinsidesales",
    ("jobrightai", "productmanagerearlycareer"): "productmanagerearlycareer",
    ("jobrightai", "productmanagerentrylevel"): "productmanagerearlycareer",
    ("anduril", "technicaloperationsengineerlacereffects"): "technicaloperationsengineerlaunchedeffects",
    ("anduril", "technicaloperationsengineerlasereffects"): "technicaloperationsengineerlaunchedeffects",
    ("auctane", "presalesengineeratlanta"): "presalesengineer",
    ("anysphere", "gtmemergingproducts"): "gtmemergingproducts",
    ("armada", "aifactoryvalueengineer"): "aifactoryvalueengineer",
    ("4mindsai", "gtmengineer"): "gtmengineer",
    ("adaptive6", "salesengineer"): "salesengineer",
    ("appgate", "gtmengineer"): "gtmengineer",
    ("cloudflare", "gtmengineer"): "gtmengineer",
    ("pindrop", "gtmsystemsplatformspecialist"): "gtmsystemsplatformspecialist",
    ("appliedsystems", "salesenablementgtmreadinesslead"): "salesenablementgtmreadinesslead",
    ("colabsoftware", "salesengineer"): "salesengineer",
    ("servicetrade", "gtmengineer"): "unspecified",
    ("enlacehealth", "salesengineer"): "salesengineer",
    ("90seconds", "seniorbusinessdevelopmentmanagerenterpriseus"): "unspecified",
    ("talentpluto", "gotomarketengineer"): "gtmengineer",
    ("talentpluto", "gtmengineer"): "gtmengineer",
    ("thehog", "foundinggtmengineer"): "foundinggtm",
    ("hartleyco", "gtmengineer"): "foundinggtm",
    ("clay", "growthstrategistenterprisecustomersuccess"): "growthstrategistenterprise",
    ("sentilink", "gotomarketgtmstrategyanalyst"): "gotomarketstrategyanalyst",
}


def role_key(company: str, role: str) -> tuple[str, str]:
    c = norm_company(canonical(company))
    r = norm_role(role)
    r = ROLE_ALIASES.get((c, r), r)
    return c, r


# Location and posting-site words that Jobright/LinkedIn append to an otherwise
# identical title. Not function words that change the opening (lead, founding).
ROLE_NOISE_TOKENS = {
    "remote",
    "onsite",
    "hybrid",
    "greater",
    "area",
    "atlanta",
    "ga",
    "us",
    "usa",
    "united",
    "states",
    "products",
    "role",
    "based",
    "in",
    "austin",
    "tx",
    "relocation",
    "package",
}


def expand_role_abbreviations(text: str) -> str:
    cleaned = re.sub(r"\([^)]*\)", " ", text or "")
    cleaned = re.sub(r"\bAEs?\b", "account executive", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bBDRs?\b", "business development representative", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bSDRs?\b", "sales development representative", cleaned, flags=re.IGNORECASE)
    return cleaned


def role_tokens(role: str) -> tuple[str, ...]:
    parts = re.findall(r"[a-z0-9]+", expand_role_abbreviations(role).lower())
    return tuple(p for p in parts if p not in ROLE_NOISE_TOKENS)


def roles_equivalent(platform_role: str, freeze1_role: str) -> bool:
    """True when one title expands or abbreviates the other.

    Catches AE vs Account Executive, parenthetical location tails, and
    'Greater Atlanta Area' vs Atlanta. Does not merge GTM Engineer with
    GTM Engineering Team Lead, or RevOps Strategist with GTM Engineer.
    """
    platform_tokens = role_tokens(platform_role)
    freeze1_tokens = role_tokens(freeze1_role)
    if not platform_tokens or not freeze1_tokens:
        return False
    if platform_tokens == freeze1_tokens:
        return True
    return (
        platform_tokens == freeze1_tokens[: len(platform_tokens)]
        or freeze1_tokens == platform_tokens[: len(freeze1_tokens)]
    )


def dedupe_platform(apps: list[dict[str, str]]) -> list[dict[str, str]]:
    """One row per company + role. Prefer Jobright exact dates over LinkedIn relative stamps."""
    ranked: dict[tuple[str, str], dict[str, str]] = {}
    order = {"jobright": 0, "linkedin": 1}

    def better(a: dict[str, str], b: dict[str, str]) -> dict[str, str]:
        if order.get(a["discovery_source"], 9) < order.get(b["discovery_source"], 9):
            winner, other = a, b
        elif order.get(b["discovery_source"], 9) < order.get(a["discovery_source"], 9):
            winner, other = b, a
        else:
            winner, other = a, b
        notes = winner.get("notes") or ""
        extra = f" Also listed on {other['discovery_source']} ({other.get('date_applied') or other.get('date_capture') or 'relative'})."
        if extra.strip() not in notes:
            winner["notes"] = (notes + extra).strip()
        return winner

    for row in apps:
        key = (norm_company(row["company_canonical"]), norm_role(row["role_as_listed"]))
        if key not in ranked:
            ranked[key] = row
        else:
            ranked[key] = better(ranked[key], row)
    return list(ranked.values())


def match_freeze1(
    platform_apps: list[dict[str, str]], freeze1: list[dict[str, str]]
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    census = [r for r in freeze1 if r.get("register") == "application"]
    opportunities = [r for r in freeze1 if r.get("register") == "opportunity"]
    by_cr: dict[tuple[str, str], list[dict[str, str]]] = {}
    by_company: dict[str, list[dict[str, str]]] = {}
    for row in census + opportunities:
        key = role_key(row["company_canonical"], row.get("role_as_listed") or "")
        by_cr.setdefault(key, []).append(row)
        by_company.setdefault(norm_company(row["company_canonical"]), []).append(row)

    overlaps: list[dict[str, str]] = []
    novel: list[dict[str, str]] = []
    ambiguous: list[dict[str, str]] = []
    for row in platform_apps:
        if row.get("register") != "application":
            key = role_key(row["company_canonical"], row["role_as_listed"])
            parents = by_cr.get(key) or by_company.get(norm_company(row["company_canonical"])) or []
            overlaps.append({**row, "match_status": "opportunity_or_non_census", "parent_id": parents[0]["application_id"] if parents else ""})
            continue
        key = role_key(row["company_canonical"], row["role_as_listed"])
        parents = by_cr.get(key, [])
        if not parents:
            cands = by_company.get(norm_company(row["company_canonical"]), [])
            unspecified = [p for p in cands if (p.get("role_as_listed") or "").lower() == "unspecified"]
            if unspecified:
                parents = unspecified
            else:
                equivalent = [
                    p
                    for p in cands
                    if roles_equivalent(row["role_as_listed"], p.get("role_as_listed") or "")
                ]
                if len(equivalent) == 1:
                    parents = equivalent
                elif equivalent:
                    # Refusing to guess is only conservative if the refusal is
                    # recorded. Emitting these as net_new would count a possible
                    # duplicate as a new application, with nothing downstream to
                    # correct it by. They are held out of the census instead.
                    ambiguous.append(
                        {
                            **row,
                            "match_status": "ambiguous",
                            "parent_id": "",
                            "candidate_parent_ids": ";".join(
                                p["application_id"] for p in equivalent
                            ),
                        }
                    )
                    continue
        if parents:
            parent = parents[0]
            overlaps.append(
                {
                    **row,
                    "match_status": "overlap",
                    "parent_id": parent["application_id"],
                    "parent_register": parent.get("register"),
                    "parent_evidence_class": parent.get("evidence_class"),
                }
            )
        else:
            novel.append({**row, "match_status": "net_new"})
    return overlaps, novel, ambiguous


def main() -> None:
    jr_apps, jr_excl = code_jobright()
    li_apps, li_excl = code_linkedin()
    apps = jr_apps + li_apps
    excl = jr_excl + li_excl
    apps = dedupe_platform(apps)
    freeze1 = load_csv(ROOT / "adjudication" / "applications__adjudicated.csv")
    freeze1_apps = [r for r in freeze1 if r.get("register") == "application"]
    overlaps, novel, ambiguous = match_freeze1(apps, freeze1)

    PLATFORM.mkdir(parents=True, exist_ok=True)
    write_csv(PLATFORM / "applications__freeze2.csv", APP_FIELDS, apps)
    write_csv(PLATFORM / "exclusions__freeze2.csv", EXCL_FIELDS, excl)

    match_fields = APP_FIELDS + [
        "match_status",
        "parent_id",
        "parent_register",
        "parent_evidence_class",
        "candidate_parent_ids",
    ]
    write_csv(OUT / "platform_match.csv", match_fields, overlaps + novel + ambiguous)

    # Ambiguous rows are recorded above and deliberately excluded here. They may
    # be duplicates of a Freeze 1 row, so counting them would inflate the census.
    union = list(freeze1_apps)
    for row in novel:
        union.append({**row, "adjudication_source": "freeze2_platform", "adjudication_note": "net_new_platform_log"})
    union_fields = list(freeze1[0].keys()) if freeze1 else APP_FIELDS
    write_csv(OUT / "applications__full_census.csv", union_fields, union)

    interviewed_types = {
        "recruiter_screen",
        "hiring_manager_interview",
        "panel",
        "technical_exercise",
        "final_round",
    }
    events = load_csv(ROOT / "coding" / "cursor" / "events__cursor.csv")
    interviewed = {
        e["application_id"]
        for e in events
        if e.get("event_type") in interviewed_types
    }
    freeze1_ids = {r["application_id"] for r in freeze1_apps}
    interviewed_221 = interviewed & freeze1_ids
    novel_ids = {r["application_id"] for r in novel}
    full_ids = freeze1_ids | novel_ids
    interviewed_full = interviewed & full_ids

    report = []
    report.append("# Freeze 2 platform ingest")
    report.append("")
    report.append("Freeze 1 Gmail and Calendar extracts were not recoded.")
    report.append("")
    report.append(f"- Jobright tracker rows coded as applications: {len(jr_apps)}")
    report.append(f"- LinkedIn applied-list rows coded (including opportunity): {len(li_apps)}")
    report.append(f"- Platform exclusions: {len(excl)}")
    report.append(f"- Platform rows overlapping Freeze 1 applications: {sum(1 for r in overlaps if r.get('match_status')=='overlap')}")
    report.append(f"- Net-new platform_log applications: {len(novel)}")
    report.append(f"- Ambiguous, matched more than one Freeze 1 row, held out of the census: {len(ambiguous)}")
    report.append(f"- Freeze 1 application census: {len(freeze1_apps)}")
    report.append(f"- Full census (Freeze 1 plus net-new): {len(union)}")
    report.append(f"- Interviewed in Freeze 1 (cursor events, application register): {len(interviewed_221)}")
    report.append(f"- Interviewed in full census: {len(interviewed_full)} (platform files carry no interview events)")
    report.append("")
    report.append("Capture recapture was not computed. The LinkedIn file is pages 1 to 10 of an applied list and does not label Easy Apply versus external ATS. LinkedIn submission_channel is therefore unknown.")
    report.append("")
    if ambiguous:
        report.append(
            f"{len(ambiguous)} platform rows matched more than one Freeze 1 row under token-prefix equivalence. "
            "The matcher refuses to choose between candidates, so these carry match_status ambiguous in "
            "platform_match.csv with their candidate parent ids, and they are held out of the full census. "
            f"The census is {len(union)} with {len(ambiguous)} unresolved, not {len(union) + len(ambiguous)}."
        )
    else:
        report.append(
            "No platform row matched more than one Freeze 1 row under token-prefix equivalence, so no row is "
            "ambiguous in this freeze. The status is emitted rather than folded into net-new so that a later run "
            "cannot count an unresolved possible duplicate as a new application."
        )
    report.append("")
    report.append("Five platform titles matched Freeze 1 as the same opening: Thomson Reuters AE Tax or Risk, Foursquare AE New Business, UpGuard SDR Manager, Verkada Enterprise Solutions Engineer Atlanta, and Listen Lead GTM Engineer (LinkedIn lists Listen, Freeze 1 uses Listen Labs). They are overlap, not net-new.")
    report.append("")
    report.append("## Net-new applications")
    report.append("")
    report.append("| company | role | source | channel |")
    report.append("|---|---|---|---|")
    for row in sorted(novel, key=lambda r: (r["company_canonical"], r["role_as_listed"])):
        report.append(
            f"| {row['company_canonical']} | {row['role_as_listed']} | {row['discovery_source']} | {row['submission_channel']} |"
        )
    (OUT / "FREEZE-2.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
