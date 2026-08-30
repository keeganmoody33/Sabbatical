"""Assert freeze headlines this manuscript is allowed to print."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "paper" / "figures"))

from series import assert_freeze_headlines, compute  # noqa: E402

BANNED_AS_FINDING = [
    (r"\b247\b", "247"),
    (r"\b4\.45\b", "4.45"),
    (r"\b321\b", "321"),
    (r"\b325\b", "325"),
]

# Sections that may mention retired/foreign figures only to refuse them.
ALLOW_REFUSAL = {
    ROOT / "paper" / "RESULTS.md",
    ROOT / "paper" / "DEFECTS.md",
    ROOT / "paper" / "citations.md",
    ROOT / "paper" / "README.md",
    ROOT / "paper" / "discussion.md",
    ROOT / "paper" / "figures.md",
    ROOT / "paper" / "METHODS.md",
}

FINDING_FILES = [
    ROOT / "paper" / "title-and-abstract.md",
    ROOT / "paper" / "introduction.md",
    ROOT / "paper" / "results-narrative.md",
    ROOT / "paper" / "conclusion.md",
    ROOT / "paper" / "acknowledgments.md",
    ROOT / "paper" / "manuscript.md",
    ROOT / "paper" / "derivatives" / "substack.md",
    ROOT / "paper" / "derivatives" / "linkedin.md",
]


def file_text_for_finding_scan(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if path.name == "manuscript.md":
        text = text.split("\n# Sources\n")[0]
    return text


def check_banned() -> list[str]:
    errors: list[str] = []
    for path in FINDING_FILES:
        if not path.exists():
            continue
        text = file_text_for_finding_scan(path)
        for pattern, label in BANNED_AS_FINDING:
            if re.search(pattern, text):
                errors.append(f"{path.name} contains {label} (not licensed as a finding)")
    return errors


def check_punctuation() -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "paper").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "—" in text or "–" in text:
            errors.append(f"{path.name} contains an em/en dash")
        if " - " in text:
            errors.append(f"{path.name} contains space-hyphen-space punctuation")
    return errors


def main() -> int:
    data = compute()
    assert_freeze_headlines(data)
    errors = check_banned() + check_punctuation()
    if errors:
        print("verify_numbers: FAIL")
        for err in errors:
            print(" ", err)
        return 1
    print("verify_numbers: 298 applications, 14 interviewed, 0 coded offers, figures series match.")
    print("verify_numbers: no banned findings in abstract/results/conclusion/introduction.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
