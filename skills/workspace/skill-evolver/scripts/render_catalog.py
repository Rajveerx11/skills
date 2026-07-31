#!/usr/bin/env python3
"""Render the repository README catalog from canonical SKILL.md metadata."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

CATEGORY_NOTES = {
    "building": "applications, integrations, automation, and developer tooling",
    "checking": "review, testing, safety, cost, scale, and release quality",
    "design": "product, interface, visual-system, and presentation design",
    "sales": "support, lead research, enrichment, and outreach",
    "video": "video production, motion, captions, media, and HyperFrames",
    "workspace": "skills, planning, learning, notes, and session operations",
    "writing": "research, posts, proposals, resumes, slides, and communication",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("--apply", action="store_true")
    return parser.parse_args()


def metadata(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit(f"Missing frontmatter: {path}")
    raw = match.group(1)
    name_match = re.search(r"(?m)^name:\s*(.+)$", raw)
    description_match = re.search(
        r"(?ms)^description:\s*(?:>-?|\\|-?)?\s*(.+?)(?=\n[A-Za-z0-9_-]+:|\Z)",
        raw,
    )
    if not name_match or not description_match:
        raise SystemExit(f"Missing metadata: {path}")
    name = name_match.group(1).strip().strip("\"'")
    description = " ".join(description_match.group(1).split()).strip("\"'")
    return name, description


def summary(description: str, limit: int = 190) -> str:
    sentence = re.split(r"(?<=[.!?])\s+", description, maxsplit=1)[0]
    if len(sentence) <= limit:
        return sentence
    return sentence[: limit - 1].rstrip() + "…"


def render(repo: Path) -> str:
    skills = defaultdict(list)
    for path in sorted((repo / "skills").glob("*/*/SKILL.md")):
        category = path.parent.parent.name
        name, description = metadata(path)
        skills[category].append((name, description, path.relative_to(repo).as_posix()))
    total = sum(len(items) for items in skills.values())
    lines = [
        "# Agent Skills Portfolio",
        "",
        f"Canonical source for {total} skills shared across Codex, Claude Code, and the common agent-skills root.",
        "",
        "Each skill is outcome-driven: strong model judgment where work is subjective, exact guardrails where correctness or safety is fragile, reusable scripts for repeated operations, and observable quality gates.",
        "",
        "## Portfolio workflow",
        "",
        "```powershell",
        "python skills/workspace/skill-evolver/scripts/run_release_checks.py .",
        "python skills/workspace/skill-evolver/scripts/sync_portfolio.py . --prune --details",
        "python skills/workspace/skill-evolver/scripts/sync_portfolio.py . --apply --prune",
        "python skills/workspace/skill-evolver/scripts/sync_portfolio.py . --verify-only",
        "```",
        "",
        "`skills-manifest.json` controls install targets. Applied exact sync stages every change, backs up overwritten or pruned files under `~/.skill-evolver/backups`, writes a receipt, excludes runtime state, rolls back on failure, and verifies hashes. Personal profiles, logs, outcomes, caches, and temporary execution files are never canonical repository content.",
        "",
        "## Categories",
        "",
    ]
    for category in sorted(skills):
        lines.append(f"- **{category}** — {CATEGORY_NOTES.get(category, 'specialized workflows')}")
    for category in sorted(skills):
        lines.extend(["", f"## {category}", ""])
        for name, description, relative in sorted(skills[category]):
            lines.append(f"- **[{name}]({relative})** — {summary(description)}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    rendered = render(repo)
    if args.apply:
        (repo / "README.md").write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Wrote {repo / 'README.md'}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
