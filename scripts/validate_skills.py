#!/usr/bin/env python3
"""Small stdlib validator for public Codex skill packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

BANNED_PATTERNS = [
    "/" + "Users" + "/",
    "pimenov" + "." + "ai",
    "Work" + "Ops",
    "Lin" + "ear",
    "OPENAI" + "_API" + "_KEY",
    "Key" + "chain",
    "Not" + "ion",
    "WRK" + "-",
    "." + "env",
]

STYLE_ANCHOR_PATTERNS = [
    "warm" + " amber",
    "warm" + " off-white",
    "paper" + " texture",
    "cream" + " paper",
    "brown" + " palette",
    "sep" + "ia",
    "parch" + "ment",
]

NAME_RE = re.compile(r"^[a-z0-9-]+$")
TEXT_EXTENSIONS = {".md", ".py", ".sh", ".yaml", ".yml", ".txt"}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter fence")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter fence")
    block = text[4:end]
    result: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def text_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix in TEXT_EXTENSIONS
    )


def main() -> int:
    errors: list[str] = []

    if not SKILLS.is_dir():
        errors.append(f"Missing skills directory: {SKILLS}")
    else:
        skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if not skill_dirs:
            errors.append("No skill directories found.")

        for skill_dir in skill_dirs:
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                errors.append(f"{skill_dir.name}: missing SKILL.md")
                continue

            text = skill_file.read_text(encoding="utf-8")
            try:
                meta = parse_frontmatter(text)
            except ValueError as exc:
                errors.append(f"{skill_dir.name}: {exc}")
                continue

            name = meta.get("name")
            description = meta.get("description")
            if not name:
                errors.append(f"{skill_dir.name}: missing name")
            elif name != skill_dir.name:
                errors.append(f"{skill_dir.name}: frontmatter name is {name!r}")
            elif not NAME_RE.match(name):
                errors.append(f"{skill_dir.name}: invalid skill name")

            if not description:
                errors.append(f"{skill_dir.name}: missing description")
            elif len(description) < 80:
                errors.append(f"{skill_dir.name}: description looks too short")

    for path in text_files(ROOT):
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in BANNED_PATTERNS:
            if pattern in text:
                rel = path.relative_to(ROOT)
                errors.append(f"{rel}: banned public-safety pattern {pattern!r}")
        lower_text = text.lower()
        for pattern in STYLE_ANCHOR_PATTERNS:
            if pattern in lower_text:
                rel = path.relative_to(ROOT)
                errors.append(f"{rel}: banned default-style anchor {pattern!r}")

    if errors:
        print("Skill package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = len(list(SKILLS.iterdir())) if SKILLS.exists() else 0
    print(f"Validated {skill_count} skill(s) and public-safety scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
