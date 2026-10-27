"""Checks that every case study follows the template and is linked everywhere.

Run from the repository root: python scripts/check_docs.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CASE_STUDIES = DOCS / "case-studies"

REQUIRED_SECTIONS = [
    "Requirements",
    "Estimates",
    "Architecture",
    "Data model",
    "API",
    "Deep dives",
    "Failure modes",
    "Trade-offs",
    "Interview follow-ups",
]

LINK = re.compile(r"\]\(([^)#\s]+)(#[^)\s]*)?\)")


def check_case_study(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    if headings != REQUIRED_SECTIONS:
        errors.append(
            f"{path.name}: sections must be exactly {REQUIRED_SECTIONS}, found {headings}"
        )
    if not text.startswith("# Design "):
        errors.append(f"{path.name}: title must start with '# Design '")
    if "**Difficulty:**" not in text:
        errors.append(f"{path.name}: missing the **Difficulty:** line")
    if text.count("```mermaid") < 2:
        errors.append(f"{path.name}: needs at least two Mermaid diagrams")
    failure_rows = re.findall(r"^\|(?!---).+\|$", text.split("## Failure modes")[-1].split("## Trade-offs")[0], flags=re.MULTILINE)
    if len(failure_rows) < 5:
        errors.append(f"{path.name}: the failure-mode table needs at least 4 rows")
    return errors


def check_relative_links(path: Path) -> list[str]:
    errors = []
    for target, _ in LINK.findall(path.read_text(encoding="utf-8")):
        if re.match(r"^[a-z]+:", target):
            continue
        if not (path.parent / target).exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link to {target}")
    return errors


def main() -> int:
    errors = []
    studies = sorted(CASE_STUDIES.glob("*.md"))
    if not studies:
        errors.append("no case studies found")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    for study in studies:
        errors += check_case_study(study)
        rel = f"case-studies/{study.name}"
        if f"docs/{rel}" not in readme:
            errors.append(f"README.md doesn't link to {rel}")
        if rel not in index:
            errors.append(f"docs/index.md doesn't link to {rel}")
        if rel not in nav:
            errors.append(f"mkdocs.yml nav doesn't include {rel}")

    for page in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *DOCS.rglob("*.md")]:
        errors += check_relative_links(page)

    for error in errors:
        print(f"error: {error}")
    print(f"Checked {len(studies)} case studies: {'OK' if not errors else f'{len(errors)} errors'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
