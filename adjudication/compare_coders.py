"""Compare independent coder CSVs. No coding. Match on company|role|cycle."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_apps(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            company = (row.get("company_canonical") or "").strip().lower()
            role = (row.get("role_as_listed") or "").strip().lower()
            cycle = (row.get("cycle") or "1").strip() or "1"
            key = f"{company}|{role}|c{cycle}"
            rows[key] = row
    return rows


def kappa(pairs: list[tuple[str, str]]) -> float:
    if not pairs:
        return float("nan")
    n = len(pairs)
    agree = sum(1 for a, b in pairs if a == b)
    p0 = agree / n
    labels = sorted({x for pair in pairs for x in pair})
    pa = Counter(a for a, _ in pairs)
    pb = Counter(b for _, b in pairs)
    pe = sum((pa[lab] / n) * (pb[lab] / n) for lab in labels)
    if pe == 1:
        return 1.0
    return (p0 - pe) / (1 - pe)


def load_events(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


INTERVIEW_TYPES = {
    "recruiter_screen",
    "hiring_manager_interview",
    "panel",
    "technical_exercise",
    "final_round",
}


def interviewed_ids(events: list[dict[str, str]]) -> set[str]:
    return {
        e["application_id"]
        for e in events
        if (e.get("event_type") or "") in INTERVIEW_TYPES
    }


def pair_report(
    name_a: str,
    name_b: str,
    a: dict[str, dict[str, str]],
    b: dict[str, dict[str, str]],
) -> dict[str, object]:
    both = sorted(set(a) & set(b))
    only_a = sorted(set(a) - set(b))
    only_b = sorted(set(b) - set(a))
    lane_pairs = [
        (a[k].get("role_lane") or "", b[k].get("role_lane") or "") for k in both
    ]
    include_pairs = []
    for key in both:
        a_inc = (a[key].get("register") or "") == "application"
        b_inc = (b[key].get("register") or "") == "application"
        include_pairs.append((str(a_inc), str(b_inc)))
    out: dict[str, object] = {
        f"{name_a}_n": len(a),
        f"{name_b}_n": len(b),
        "intersection": len(both),
        f"only_{name_a}": len(only_a),
        f"only_{name_b}": len(only_b),
        "only_a_keys": only_a,
        "only_b_keys": only_b,
        "both_keys": both,
    }
    if both:
        lane_agree = sum(1 for x, y in lane_pairs if x == y) / len(lane_pairs)
        inc_agree = sum(1 for x, y in include_pairs if x == y) / len(include_pairs)
        out["role_lane_pct_agreement"] = lane_agree
        out["role_lane_kappa"] = kappa(lane_pairs)
        out["include_pct_agreement"] = inc_agree
        out["include_kappa"] = kappa(include_pairs)
        out["lane_disagreements"] = [
            (k, a[k].get("role_lane"), b[k].get("role_lane"))
            for k in both
            if (a[k].get("role_lane") or "") != (b[k].get("role_lane") or "")
        ]
        out["include_disagreements"] = [
            (k, a[k].get("register"), b[k].get("register"))
            for k in both
            if ((a[k].get("register") or "") == "application")
            != ((b[k].get("register") or "") == "application")
        ]
    return out


def coder_paths() -> dict[str, Path]:
    coding = ROOT / "coding"
    found: dict[str, Path] = {}
    for coder in ("alpha", "bravo", "cursor"):
        path = coding / coder / f"applications__{coder}.csv"
        if path.exists():
            found[coder] = path
    return found


def main() -> None:
    paths = coder_paths()
    if len(paths) < 2:
        print("need at least two coder CSVs", file=sys.stderr)
        print("found:", sorted(paths), file=sys.stderr)
        sys.exit(1)
    loaded = {name: load_apps(path) for name, path in paths.items()}
    names = sorted(loaded)
    reports = []
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            reports.append((left, right, pair_report(left, right, loaded[left], loaded[right])))
    out_dir = ROOT / "adjudication"
    out_dir.mkdir(exist_ok=True)
    lines = ["# Pre-adjudication comparison", ""]
    for left, right, rep in reports:
        lines.append(f"## {left} vs {right}")
        lines.append("")
        for key in (
            f"{left}_n",
            f"{right}_n",
            "intersection",
            f"only_{left}",
            f"only_{right}",
            "role_lane_pct_agreement",
            "role_lane_kappa",
            "include_pct_agreement",
            "include_kappa",
        ):
            if key in rep:
                val = rep[key]
                if isinstance(val, float):
                    lines.append(f"- {key}: {val:.4f}")
                else:
                    lines.append(f"- {key}: {val}")
        lines.append("")
        lane_d = rep.get("lane_disagreements") or []
        inc_d = rep.get("include_disagreements") or []
        lines.append(f"role_lane disagreements: {len(lane_d)}")
        lines.append(f"include/exclude disagreements on intersection: {len(inc_d)}")
        lines.append("")
    report_path = out_dir / "PRE-ADJUDICATION.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    disagreement_path = out_dir / "disagreements.csv"
    with disagreement_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["pair", "match_key", "field", "left_value", "right_value"],
        )
        writer.writeheader()
        for left, right, rep in reports:
            for key, lv, rv in rep.get("lane_disagreements") or []:
                writer.writerow(
                    {
                        "pair": f"{left}-vs-{right}",
                        "match_key": key,
                        "field": "role_lane",
                        "left_value": lv,
                        "right_value": rv,
                    }
                )
            for key, lv, rv in rep.get("include_disagreements") or []:
                writer.writerow(
                    {
                        "pair": f"{left}-vs-{right}",
                        "match_key": key,
                        "field": "register",
                        "left_value": lv,
                        "right_value": rv,
                    }
                )
            for key in rep.get("only_a_keys") or []:
                writer.writerow(
                    {
                        "pair": f"{left}-vs-{right}",
                        "match_key": key,
                        "field": "presence",
                        "left_value": "present",
                        "right_value": "absent",
                    }
                )
            for key in rep.get("only_b_keys") or []:
                writer.writerow(
                    {
                        "pair": f"{left}-vs-{right}",
                        "match_key": key,
                        "field": "presence",
                        "left_value": "absent",
                        "right_value": "present",
                    }
                )

    print(report_path.read_text(encoding="utf-8"))
    print(f"wrote {report_path}")
    print(f"wrote {disagreement_path}")


if __name__ == "__main__":
    main()
