#!/usr/bin/env python3
"""Build a stable manifest from canonical skills and current direct installs."""

from __future__ import annotations

import argparse
import ctypes
import json
import os
import re
from pathlib import Path

TARGET_ORDER = ("codex", "claude", "agents")
REPARSE_POINT = 0x0400
RUNTIME_EXCLUDES = {
    "learn-day": ["data/**"],
    "linkedin-post-writer": [".consent", "memory/**", ".skill-data/**"],
    "plan-day": ["data/**"],
    "remotion-to-hyperframes": [
        "assets/test-corpus/run-report.json",
        "assets/test-corpus/tier-*/**/node_modules/**",
        "assets/test-corpus/tier-*/**/package-lock.json",
        "assets/test-corpus/tier-*/remotion-src/out/**",
        "assets/test-corpus/tier-*/hf-src/out/**",
        "assets/test-corpus/tier-*/hf.mp4",
        "assets/test-corpus/tier-*/diff/**",
        "assets/test-corpus/tier-*/strip/**",
        "assets/test-corpus/tier-2-multi-scene/remotion-src/public/**",
        "assets/test-corpus/tier-2-multi-scene/hf-src/assets/**",
    ],
    "remotion-video-prompt": ["LEARNINGS.md", "history/**", "memory/**", ".skill-data/**"],
    "shorts": ["LEARNINGS.md", "history/**", "memory/**", ".skill-data/**"],
    "skill-evolver": ["scripts/__pycache__/**", "scripts/*.pyc"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--new-targets", nargs="+", choices=TARGET_ORDER)
    parser.add_argument(
        "--bootstrap-from-installs",
        action="store_true",
        help="Infer targets only when creating an initial manifest; never use for routine release",
    )
    return parser.parse_args()


def frontmatter_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*['\"]?([^'\"\r\n]+)", text)
    if not match:
        raise SystemExit(f"Missing frontmatter name: {path}")
    return match.group(1).strip()


def is_reparse_point(path: Path) -> bool:
    if path.is_symlink():
        return True
    if os.name != "nt":
        return False
    attributes = ctypes.windll.kernel32.GetFileAttributesW(str(path))
    return attributes != -1 and bool(attributes & REPARSE_POINT)


def direct_installs(root: Path) -> dict[str, Path]:
    if not root.is_dir():
        return {}
    installs: dict[str, Path] = {}
    duplicates: dict[str, list[Path]] = {}
    for directory in root.iterdir():
        skill = directory / "SKILL.md"
        if not directory.is_dir() or is_reparse_point(directory) or not skill.is_file():
            continue
        name = frontmatter_name(skill)
        if name in installs:
            duplicates.setdefault(name, [installs[name]]).append(directory)
            continue
        installs[name] = directory
    if duplicates:
        detail = "; ".join(
            f"{name}: {', '.join(str(path) for path in paths)}"
            for name, paths in sorted(duplicates.items())
        )
        raise SystemExit(f"Duplicate direct skill installs under {root}: {detail}")
    return installs


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    skill_root = repo / "skills"
    output = (args.output or repo / "skills-manifest.json").resolve()
    user = Path(os.environ.get("USERPROFILE") or Path.home())
    roots = {
        "codex": user / ".codex" / "skills",
        "claude": user / ".claude" / "skills",
        "agents": user / ".agents" / "skills",
    }
    installed = {target: direct_installs(root) for target, root in roots.items()}
    existing_entries: dict[str, dict] = {}
    if output.is_file():
        existing = json.loads(output.read_text(encoding="utf-8"))
        existing_entries = {
            item["name"]: item
            for item in existing.get("skills", [])
            if isinstance(item, dict) and isinstance(item.get("name"), str)
        }
    canonical: dict[str, Path] = {}
    for skill_file in skill_root.rglob("SKILL.md"):
        if "node_modules" in skill_file.parts:
            continue
        name = frontmatter_name(skill_file)
        if name in canonical:
            raise SystemExit(f"Duplicate canonical name: {name}")
        canonical[name] = skill_file.parent

    entries: list[dict[str, object]] = []
    missing_policy: list[str] = []
    for name, directory in sorted(canonical.items()):
        existing = existing_entries.get(name)
        if existing:
            targets = list(existing["targets"])
        elif args.new_targets:
            targets = list(dict.fromkeys(args.new_targets))
        elif args.bootstrap_from_installs:
            targets = [target for target in TARGET_ORDER if name in installed[target]]
            if not targets:
                missing_policy.append(name)
                continue
        else:
            missing_policy.append(name)
            continue
        entry: dict[str, object] = {
            "name": name,
            "path": directory.relative_to(repo).as_posix(),
            "targets": targets,
        }
        excludes = existing.get("runtime_excludes") if existing else RUNTIME_EXCLUDES.get(name)
        if excludes:
            entry["runtime_excludes"] = excludes
        entries.append(entry)

    if missing_policy:
        raise SystemExit(
            "Explicit target policy required for new skills: "
            + ", ".join(missing_policy)
            + ". Pass --new-targets or edit skills-manifest.json."
        )

    manifest = {
        "schema": 1,
        "canonical_root": "skills",
        "roots": {
            "codex": ".codex/skills",
            "claude": ".claude/skills",
            "agents": ".agents/skills",
        },
        "skills": entries,
    }
    rendered = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if args.apply:
        output.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Wrote {output}: {len(entries)} skills")
    else:
        print(rendered, end="")
        print(f"Dry run: {len(entries)} skills", file=os.sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
