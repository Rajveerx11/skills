#!/usr/bin/env python3
"""Inject or refresh concise, per-skill adaptive sections from quality profiles."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

START = "<!-- skill-evolver:adaptive-start -->"
END = "<!-- skill-evolver:adaptive-end -->"
PORTABLE_KEYS = {"name", "description"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    parser.add_argument("--profiles", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Replace existing adaptive sections; default preserves hand-tuned sections",
    )
    return parser.parse_args()


def normalize_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end < 0:
        return text
    kept: list[str] = []
    keep_block = False
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keep_block = match.group(1) in PORTABLE_KEYS
        if keep_block:
            kept.append(line)
    return "---\n" + "\n".join(kept) + text[end:]


def section(profile: dict) -> str:
    gates = "; ".join(profile["quality_gates"])
    return (
        f"{START}\n"
        "## Adaptive excellence\n\n"
        f"- Optimize for: {profile['outcome']}\n"
        f"- Freedom: {profile['freedom']}\n"
        "- Autonomy: inspect available context first, infer low-risk details, choose strong defaults, "
        "and finish the authorized workflow end to end. Ask only when a choice materially changes "
        "outcome, risk, cost, or irreversible state.\n"
        f"- Quality gate: {gates}. Revise once when any gate is weak.\n"
        f"- Learning: after explicit feedback or measurable results, record {profile['learning']} "
        "through `skill-evolver`. Never self-edit from silence, a single unverified outcome, or model self-rating.\n"
        f"{END}\n"
    )


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    profile_path = (args.profiles or repo / "skills" / "workspace" / "skill-evolver" / "references" / "quality-profiles.json").resolve()
    profiles = json.loads(profile_path.read_text(encoding="utf-8"))
    skills = {
        path.parent.name: path
        for path in (repo / "skills").rglob("SKILL.md")
        if "node_modules" not in path.parts
    }
    changed: list[str] = []
    missing: list[str] = []
    for name, profile in profiles.items():
        path = skills.get(name)
        if not path:
            missing.append(name)
            continue
        text = normalize_frontmatter(path.read_text(encoding="utf-8"))
        adaptive = section(profile)
        if START in text and END in text and args.refresh:
            pattern = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
            updated = pattern.sub(adaptive, text)
        elif START in text and END in text:
            updated = text
        else:
            updated = text.rstrip() + "\n\n" + adaptive
        if updated != path.read_text(encoding="utf-8"):
            changed.append(name)
            if args.apply:
                path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Profiles={len(profiles)} changed={len(changed)} missing={len(missing)}")
    if changed:
        print("Changed: " + ", ".join(sorted(changed)))
    if missing:
        print("Missing: " + ", ".join(sorted(missing)))
    if not args.apply:
        print("Dry run only. Add --apply to write.")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
