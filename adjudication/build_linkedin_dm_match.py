#!/usr/bin/env python3
"""Parse the LinkedIn job-threads analysis and independently match each thread."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(
    "/home/ubuntu/.cursor/projects/workspace/uploads/"
    "LinkedIn_Job_Threads_Analysis_2025-06_to_2026-08_1653.md"
)
OUT = ROOT / "adjudication" / "linkedin_dm_match.csv"

OVERRIDES = {
    "Heather Tatum": (
        "candidate_opportunity_held",
        "Speakeasy Inc. inbound Sales Consultant. No reply. Not in the 298. Do not mint.",
    ),
    "Scott Reffett": (
        "exclusion",
        "Thrivent financial-advisor pitch. Insurance recruiting. Not an application.",
    ),
    "Marina Ghilchik → Jacob Bowman": (
        "unidentifiable",
        "Warm GTME intro. Employer unnamed in the analysis. No census row.",
    ),
    "benyamin (🏍)": (
        "candidate_opportunity_held",
        "Cyft Calendly link. This tree's coding CSVs have no Cyft row. Package Gmail log 024 has a scheduled then canceled interview. Hold.",
    ),
    "Teresa Vitale": (
        "candidate_opportunity_held",
        "Protecht inbound about a January 2025 application, outside the study window. In-range touch only. Not in the 298.",
    ),
    "Eoin Clancy": (
        "candidate_opportunity_held",
        "AirOps then thecannonproject. Census AirOps Growth Engineer 2026-04-10 is a later application, not this 2025 inbound. Hold a new opportunity row.",
    ),
    "Justin Wenig": (
        "candidate_opportunity_held",
        "Starbridge. Not in this tree's coding CSVs. Package log 024 has email cancellation. Hold. Do not mix into the 14.",
    ),
    "Sana Hussain Khan": (
        "candidate_opportunity_held",
        "AutoLeap SDR inbound. Ghosted after GTM filter reply. Not in the 298.",
    ),
    "Alex Martin": (
        "exclusion",
        "Outlier AI freelance graphic-design gig. Not a search application.",
    ),
    "Kelly Patterson": (
        "held_role_collision",
        "Soliant AE Atlanta inbound. Census has Solant Generative AI Agent Engineer. Different title. Do not merge without the artifact string.",
    ),
    "Siddharth Gopi": (
        "already_opportunity",
        "WorkOS GTM Engineer agency pitch. WorkOS is already opportunity. Booking link, no evidenced call. Does not enter the 14.",
    ),
    "Alex Plavljanic": ("unidentifiable", "Outbound. Employer unnamed."),
    "Samiyah Smythe": (
        "exclusion",
        "Unnamed financial-agency pitch. Insurance/finance recruiting noise.",
    ),
    "Mounika Ravi": (
        "candidate_opportunity_held",
        "Flexton Enablement Lead for unnamed client. Not in the 298.",
    ),
    "Nicole Kim": (
        "candidate_opportunity_held",
        "Ambient.ai first GTM Engineer inbound. Not in the 298 or the 105. Ghosted after questions.",
    ),
    "Neeraj Singh": (
        "unidentifiable",
        "Agency AI Enablement Specialist. Employer unnamed.",
    ),
    "Outlier": (
        "exclusion",
        "Outlier image-annotation gig. Not a search application.",
    ),
    "Ayesha Asghar": (
        "exclusion",
        "Capital Linguists part-time SDR contractor. Not a search application of record.",
    ),
    "Gagandeep Bajaj": (
        "candidate_opportunity_held",
        "Unnamed-client SDR Alpharetta. Not replied to.",
    ),
    "Jamie Neubeck": (
        "unidentifiable",
        "Warm referral, friend's company unnamed. Not replied to.",
    ),
    "Patrick F. Cua": (
        "already_opportunity",
        "Glytec CEO inbound. Glytec already opportunity. Clayton 2026-01-27 already coded. 'Background churn' is new detail, not a new interview. Stays outside the 14.",
    ),
    "Alex McClelland": (
        "exclusion",
        "Handshake AI Fellowship gig. Census Handshake GTM Engineer 2026-07-15 is a different row.",
    ),
    "Vikas CV": (
        "held_role_collision",
        "IBM Brand Technical Sales Specialist inbound. Census IBM is Manager Applied AI and GTM Systems 2026-06-22. Different title.",
    ),
    "Giorgio Zanella": (
        "already_opportunity",
        "The Kiln already opportunity. This thread: same-day video with Giorgio 2026-03-03, founder intro promised, 2026-03-06 follow-up unanswered. Patrick call is the GTME Intro screenshots, a different thread. Do not mint a second interview from this summary. Do not adopt package log 037's two-interview coding.",
    ),
    "Puneet Seth": (
        "exclusion",
        "New York Life financial advisor. Insurance recruiting.",
    ),
    "Kayla Gottschalk": ("unidentifiable", "Outbound. Employer unnamed."),
    "Rachel Downs": (
        "already_application",
        "Virtru Director of GTM AI. Census Virtru Director of Go-to-Market AI 2026-03-09, same day. DM is recruiter pitch on an existing application. Not in the 14.",
    ),
    "Joe Rhew": (
        "candidate_opportunity_held",
        "Parallel founder soft no. Not in the 298. Hold.",
    ),
    "McKenzie Skamarycz": (
        "already_opportunity",
        "Opsin via agency. Opsin already opportunity. James Pham 2026-03-13 already coded. Does not add to the 14.",
    ),
    "Stephanie Gray": (
        "exclusion",
        "New York Life financial. Insurance recruiting.",
    ),
    "Andrew Cummins": (
        "unidentifiable",
        "Outbound 'just applied.' Company and role not identifiable.",
    ),
    "Chrissy Repko": (
        "already_application",
        "2X GTM Engineer. Census has 2X GTM Engineer. Do not add an interview from unclear scheduling.",
    ),
    "Laura R.": (
        "candidate_opportunity_held",
        "Best Version Media Sales Specialist. Not in the 298.",
    ),
    "Alice Imundo": (
        "candidate_opportunity_held",
        "Aptean RevOps Analyst GTM AI. Not in the 298. Do not mint an interview from a proposed slot.",
    ),
    "Noah Jacobs": (
        "exclusion",
        "Direct ask. Explicit not hiring. No opportunity.",
    ),
    "Eric Quanstrom": (
        "already_application",
        "AICRO GTM Engineer. Census has AICRO GTM Engineer. Cold DM after applying. Not an interview.",
    ),
    "Melissa Eisenach": (
        "candidate_opportunity_held",
        "Second Aptean recruiter, RevOps Clay. Proposed 2026-06-02 slots. Not in the 298. Hold.",
    ),
    "Stephanie Cunningham": (
        "already_application",
        "RevSpring Lead Agentic Ops. Census 2026-06-04 and in the 14. This inbound 2026-05-29 was not replied to.",
    ),
    "Woody Hu": (
        "candidate_application_held",
        "AnyInt AI Founding Sales. Analysis says a LinkedIn application. Not in the 105 extract and not in the 298. Candidate explanation for 107 versus 105. Hold. Do not mint.",
    ),
    "Hudson Liao": (
        "already_opportunity",
        "The Hog. Already opportunity. Calendar interview 2026-06-16 already coded. Stays outside the 14.",
    ),
    "Jordan (Morse) Burley": (
        "held_role_collision",
        "Sage BDR inbound. Census Sage is Director of Growth Small 2025-08-04. Different title.",
    ),
    "Jon Sibley": (
        "already_application",
        "TrueBuilt GTM Engineer. In the 298. Not in the 14. FT rescoped to contract project. Matches Freeze 3.",
    ),
    "Antony Liu": (
        "already_application",
        "Melavex Founding GTM Lead. Census and LI-077. Do not mint an interview from 'unclear if the call landed.'",
    ),
    "Mark Kutz": (
        "already_application",
        "Gradient Labs GTM. Census Gradient Labs GTM Engineer 2026-07-21. Outbound DM ghosted.",
    ),
    "Michael Berry": (
        "candidate_opportunity_held",
        "Unnamed Series B warehouse-intelligence RevOps. Call scheduling in motion at export. Hold.",
    ),
    "Brad Vogel": (
        "already_application",
        "Patch application plus weak-tie referral. Census Patch Growth Engineering Lead 2026-07-13.",
    ),
    "Holli Adams": (
        "exclusion",
        "Unnamed financial-team talent scout. Insurance/finance pattern.",
    ),
    "M. Shoaib Arshad": (
        "candidate_opportunity_held",
        "Unnamed hospice AE. Not replied to.",
    ),
    "Aleksandra Belousova": (
        "candidate_opportunity_held",
        "Claudomat GTM Engineer inbound. Not in the 298 or the 105. Subject ghosted the recruiter. Hold.",
    ),
    "Freemen Pasurai": (
        "exclusion",
        "Azul 4-month Marketing AI contract. Not a search application of record.",
    ),
    "Matt Cassel": (
        "candidate_opportunity_held",
        "Unnamed construction/fabrication SaaS Senior RevOps Engineer. Ongoing at export. Hold.",
    ),
    "Ajmal Khan": (
        "exclusion",
        "Global Financial Impact 1099 BDR. Insurance-adjacent.",
    ),
    "Geneve Kay S.": (
        "already_application",
        "WilsonHCG Fortune 500 client. Census WilsonHCG Outbound Sales Consultant III 2026-02-13. August 2026 re-approach is not a new application.",
    ),
    "Olivia Lezama": (
        "exclusion",
        "Thread started 2020. In-range resume send to unnamed Atlanta staffing. Not a new application row.",
    ),
}

UNC_OVERRIDES = {
    "Timi Digifa": (
        "exclusion",
        "Reverse: he asked the subject for GTME help. Not the subject's opportunity.",
    ),
    "Nuella Olu-Ighama": (
        "exclusion",
        "Reverse: she pitched herself as a GTM Engineer for hire.",
    ),
    "Jinnatun Nisha": (
        "exclusion",
        "Reverse: she asked the subject for openings.",
    ),
    "Daniel Hill": (
        "exclusion",
        "Friend sharing leads. No named employer process.",
    ),
    "Jordan Crawford": (
        "exclusion",
        "Networking. No role on the table. Pre-range start.",
    ),
    "Doug Bell": (
        "exclusion",
        "Advisory. Content/copy JD may have been a referral for someone else. Not minted.",
    ),
    "Jan Durbin": (
        "already_opportunity",
        "Recruiter networking around Glytec's Sr GTM Software Engineer. Corroborates Glytec. Not a second Glytec row.",
    ),
    "Harkin Randhawa": (
        "exclusion",
        "Friendly 'ever hiring' feeler. No role.",
    ),
    "Hallies Coleman": (
        "exclusion",
        "Generic Amazon TA follow-me note. No specific opportunity.",
    ),
    "Jim (Boris) Ryss": (
        "exclusion",
        "Expert-network / knowledge-monetization pitch.",
    ),
    "Gurjap Sandhu + Kofi Boamah O.": (
        "exclusion",
        "Identical template. Scam pattern.",
    ),
    "mahmoud taman": (
        "exclusion",
        "Bitget crypto pitch. Scam-adjacent.",
    ),
    "Andrew Jones": (
        "exclusion",
        "Shin-Etsu impersonation scam format.",
    ),
    "Masood Amirbeiki": (
        "exclusion",
        "Financial-advisor prospecting cadence.",
    ),
    "Amal Patnaik": (
        "exclusion",
        "Dev-shop service sale, not a job.",
    ),
    "Pravat Abraham": (
        "exclusion",
        "Wrong-name mass blast.",
    ),
    "Dave Dargatz": (
        "exclusion",
        "Franchise coaching. Not employment.",
    ),
    "Jenny May Gementiza-Navarro": (
        "exclusion",
        "Paid job-application service pitching to job seekers.",
    ),
    "Hunter Deskin": (
        "exclusion",
        "Fractional-SDR course funnel. Pre-range start.",
    ),
    "Pierre Verhoeven": (
        "held_implied_interview",
        "Peer note Good luck for tomorrow on 2025-08-08 implies an interview that day. Not enough to mint. Do not invent a company.",
    ),
}

FIELDS = [
    "thread_id",
    "section",
    "thread_start",
    "last_activity",
    "direction",
    "person",
    "role",
    "company",
    "job_title",
    "analysis_stage",
    "analysis_confidence",
    "match_status",
    "census_company",
    "census_role",
    "linkedin_row_id",
    "notes",
]


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def parse_rows(block: str, expected_cols: int) -> list[list[str]]:
    out: list[list[str]] = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        compact = line.replace("|", "").replace("-", "").strip()
        if compact == "":
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if cols[0] in {"Thread Start", "Contact"}:
            continue
        if len(cols) < expected_cols:
            cols += [""] * (expected_cols - len(cols))
        out.append(cols[:expected_cols])
    return out


def load_census():
    return list(
        csv.DictReader(open(ROOT / "adjudication" / "applications__full_census.csv"))
    )


def load_li():
    return list(
        csv.DictReader(
            open(ROOT / "artifacts" / "platform" / "linkedin-applications-in-window.csv")
        )
    )


def find_census(company: str, census) -> list[dict]:
    n = norm(company)
    if not n or n in {"unknown", "unnamed"}:
        return []
    exact = []
    loose = []
    for row in census:
        cn = norm(row["company_canonical"])
        al = norm(row.get("company_as_listed"))
        if n == cn or n == al:
            exact.append(row)
        elif n in cn or cn in n:
            if n not in {"pin"}:
                loose.append(row)
    return exact or loose


def find_li(company: str, li) -> list[dict]:
    n = norm(company)
    if not n:
        return []
    return [
        r
        for r in li
        if n == norm(r["company_as_listed"]) or n in norm(r["company_as_listed"])
    ]


def main() -> None:
    text = SRC.read_text()
    job_block = text[
        text.index("## Job-Related Threads") : text.index("## Uncertain Threads")
    ]
    unc_block = text[
        text.index("## Uncertain Threads") : text.index("## Summary Statistics")
    ]
    jobs = parse_rows(job_block, 11)
    unc = parse_rows(unc_block, 4)
    if len(jobs) != 54:
        raise SystemExit(f"expected 54 job threads, got {len(jobs)}")
    if len(unc) != 20:
        raise SystemExit(f"expected 20 uncertain, got {len(unc)}")

    census = load_census()
    li = load_li()
    out_rows = []
    tid = 1
    skip_census_people = {
        "Giorgio Zanella",
        "Hudson Liao",
        "Patrick F. Cua",
        "Siddharth Gopi",
        "McKenzie Skamarycz",
        "Woody Hu",
        "benyamin (🏍)",
        "Justin Wenig",
        "Olivia Lezama",
    }
    for cols in jobs:
        person = cols[3]
        company = cols[5]
        if person not in OVERRIDES:
            raise SystemExit(f"missing override: {person}")
        status, notes = OVERRIDES[person]
        section = (
            "pre_range_start_in_range_activity"
            if person == "Olivia Lezama"
            else "job_related"
        )
        cen = [] if person in skip_census_people else find_census(company, census)
        if person == "Kelly Patterson":
            cen = find_census("Solant", census)
        li_hits = find_li(company, li)
        if person == "Kelly Patterson":
            li_hits = find_li("Solant", li) + find_li("SoTalent", li)
        if person in skip_census_people:
            li_hits = find_li(company, li)
        if person == "Hudson Liao":
            li_hits = find_li("The Hog", li)
        out_rows.append(
            {
                "thread_id": f"LI-DM-{tid:03d}",
                "section": section,
                "thread_start": cols[0],
                "last_activity": cols[1],
                "direction": cols[2],
                "person": person,
                "role": cols[4],
                "company": company,
                "job_title": cols[6],
                "analysis_stage": cols[7],
                "analysis_confidence": cols[10],
                "match_status": status,
                "census_company": cen[0]["company_canonical"] if cen else "",
                "census_role": cen[0]["role_as_listed"] if cen else "",
                "linkedin_row_id": li_hits[0]["linkedin_row_id"] if li_hits else "",
                "notes": notes,
            }
        )
        tid += 1

    for cols in unc:
        person = cols[2]
        if person not in UNC_OVERRIDES:
            raise SystemExit(f"missing unc override: {person}")
        status, notes = UNC_OVERRIDES[person]
        out_rows.append(
            {
                "thread_id": f"LI-DM-{tid:03d}",
                "section": "uncertain",
                "thread_start": cols[0],
                "last_activity": cols[1],
                "direction": "",
                "person": person,
                "role": "",
                "company": "",
                "job_title": "",
                "analysis_stage": "",
                "analysis_confidence": "",
                "match_status": status,
                "census_company": "",
                "census_role": "",
                "linkedin_row_id": "",
                "notes": notes + " " + cols[3],
            }
        )
        tid += 1

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(out_rows)
    print(dict(Counter(r["match_status"] for r in out_rows)))
    print(f"wrote {OUT} n={len(out_rows)}")


if __name__ == "__main__":
    main()
