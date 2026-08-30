"""Single entrypoint for the Sabbatical pipeline.

One command reproduces every published number from the frozen corpus and the
frozen coder CSVs. Nothing here re-codes an artifact or edits a coder file.

The stages are the scripts that already existed, run in dependency order, plus
the two view-layer stages. This module orchestrates them. It does not
reimplement them, because their outputs are published and a reimplementation
that produced the same numbers by a different route would still have to be
proven equivalent.

    python3 pipeline/run.py            # check mode, the default
    python3 pipeline/run.py --write    # permit intended changes
    python3 pipeline/run.py --list     # show the stages and exit

CHECK MODE IS THE POINT. Every stage declares the files it writes. Check mode
hashes each of them before the run and again after, and exits non-zero if any
existing file changed. The corpus is frozen and the coder CSVs are frozen, so
a re-run that moves a byte means the pipeline is not deterministic, and a
census that cannot be reproduced cannot be defended. A file that did not exist
before is reported as created rather than changed, which is what a first run of
a new view looks like.

Use --write when a change is intended. An intended change must also be logged
in the `knowledge/protocol.md` changelog with a date and a reason, and
disclosed in `paper/DEFECTS.md`, per the rule at the head of the protocol.
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Stage:
    name: str
    script: str
    owns: str
    outputs: list[str] = field(default_factory=list)


# Order is a dependency order, not a preference.
#   compare_coders reads the coder CSVs and must run before anything consumes
#     the agreement statistics.
#   adjudicate produces applications__adjudicated.csv, which ingest_platform
#     matches platform rows against and derive_latency joins to.
#   ingest_platform produces the full census.
#   derive_latency reads the adjudicated census and both coders' events.
#   derive_metrics prints per-coder summaries to stdout and writes nothing.
#   build_views and data_quality read the outputs of everything above.
STAGES: list[Stage] = [
    Stage(
        name="compare_coders",
        script="adjudication/compare_coders.py",
        owns="Pre-adjudication agreement between the blind coders, and the disagreement inventory.",
        outputs=[
            "adjudication/PRE-ADJUDICATION.md",
            "adjudication/disagreements.csv",
        ],
    ),
    Stage(
        name="adjudicate",
        script="adjudication/adjudicate.py",
        owns="The 223-row application census, and the written rule behind every resolved disagreement.",
        outputs=[
            "adjudication/applications__adjudicated.csv",
            "adjudication/ADJUDICATION.md",
        ],
    ),
    Stage(
        name="ingest_platform",
        script="adjudication/ingest_platform.py",
        owns="Platform rows through Freeze 3, the match cascade, and the 317-row full census.",
        outputs=[
            "coding/platform/applications__freeze2.csv",
            "coding/platform/exclusions__freeze2.csv",
            "adjudication/platform_match.csv",
            "adjudication/applications__full_census.csv",
            "adjudication/FREEZE-2.md",
        ],
    ),
    Stage(
        name="derive_latency",
        script="adjudication/derive_latency.py",
        owns="Time to first response and time to first interview, on exact-dated rows only.",
        outputs=[
            "adjudication/latency__by_application.csv",
            "adjudication/LATENCY.md",
        ],
    ),
    Stage(
        name="derive_metrics",
        script="adjudication/derive_metrics.py",
        owns="Per-coder summary counts, printed for inspection. Writes nothing.",
        outputs=[],
    ),
    Stage(
        name="build_views",
        script="pipeline/build_views.py",
        owns="The analysis views every number in the paper is quoted from.",
        outputs=[
            "views/origin_coverage.csv",
            "views/origin_recoverability.csv",
            "views/funnel_by_role_lane.csv",
            "views/funnel_by_submission_channel.csv",
            "views/funnel_by_evidence_class.csv",
            "views/monthly_trend.csv",
            "views/title_language.csv",
            "views/latency_by_slice.csv",
        ],
    ),
    Stage(
        name="data_quality",
        script="pipeline/data_quality.py",
        owns="The generated data quality report: missing fields, duplicates, vocabulary violations, outliers, row completeness.",
        outputs=["data_quality_report.md"],
    ),
]


def digest(path: Path) -> str | None:
    """sha256 of a file, or None when it does not exist yet."""
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def committed_at_head(rel: str) -> bool:
    """True when HEAD carries this path. Distinguishes a genuinely new output
    from a committed one that is missing because the checkout is incomplete.

    Without this, deleting a committed output and running check mode passes:
    the stage regenerates the file, it is classified as `created`, and
    verification reports success on a tree that never contained the thing being
    verified.

    HEAD rather than the index, deliberately. `git ls-files` reads the index, so
    `git rm` removes the path from it and the check silently reverts to the
    behaviour this function exists to prevent. The question being asked is
    whether the committed state holds this file, and only HEAD answers that.
    A staged deletion cannot change it.

    Returns False if git is unavailable or there is no HEAD yet, which degrades
    to the old behaviour rather than failing a run for the absence of a tool.
    """
    try:
        result = subprocess.run(
            ["git", "cat-file", "-e", f"HEAD:{rel}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    except OSError:
        return False
    return result.returncode == 0


def snapshot(stages: list[Stage]) -> dict[str, str | None]:
    return {out: digest(ROOT / out) for stage in stages for out in stage.outputs}


def run_stage(stage: Stage) -> None:
    """Run one stage, surfacing its stderr. Raises on a non-zero exit."""
    result = subprocess.run(
        [sys.executable, str(ROOT / stage.script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        raise SystemExit(f"stage {stage.name} failed with exit code {result.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--write",
        action="store_true",
        help="permit changes to existing outputs. Without it, a changed output fails the run.",
    )
    parser.add_argument("--list", action="store_true", help="print the stages and exit")
    args = parser.parse_args()

    if args.list:
        for stage in STAGES:
            print(f"{stage.name}\n  {stage.script}\n  {stage.owns}")
            for out in stage.outputs:
                print(f"    writes {out}")
        return 0

    before = snapshot(STAGES)

    for stage in STAGES:
        print(f"[{stage.name}] {stage.script}")
        run_stage(stage)

    after = snapshot(STAGES)

    absent_before = [p for p in after if before[p] is None and after[p] is not None]
    # A committed output that was missing before the run is an incomplete
    # checkout, not a new view. Regenerating it and calling that success would
    # verify a tree that never held the file.
    restored = [p for p in absent_before if committed_at_head(p)]
    created = [p for p in absent_before if p not in restored]
    changed = [p for p in after if before[p] is not None and before[p] != after[p]]
    missing = [p for p in after if after[p] is None]

    print()
    unchanged = len(after) - len(created) - len(restored) - len(changed) - len(missing)
    print(f"outputs unchanged: {unchanged}")
    for path in created:
        print(f"created: {path}")
    for path in restored:
        print(f"RESTORED: {path}")
    for path in changed:
        print(f"CHANGED: {path}")
    for path in missing:
        print(f"NOT WRITTEN: {path}")

    if missing:
        print("\nA declared output was not written. The stage list and the scripts disagree.")
        return 1

    if restored and not args.write:
        print(
            "\nA committed output was missing before this run and the pipeline regenerated it.\n"
            "That is an incomplete checkout, not a verification: the run cannot confirm the\n"
            "committed file reproduces, because the committed file was not there to compare\n"
            "against. Restore the working tree (git checkout -- <path>) and re-run, or use\n"
            "--write if the regeneration is intended."
        )
        return 1

    if changed and not args.write:
        print(
            "\nAn existing output changed on a re-run of a frozen corpus.\n"
            "Either the pipeline is not deterministic, or a change was made without being logged.\n"
            "If the change is intended, re-run with --write, log it in the knowledge/protocol.md\n"
            "changelog with a date and a reason, and disclose it in paper/DEFECTS.md."
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
