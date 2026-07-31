#!/usr/bin/env python3
"""Read-only structural audit for an Obsidian vault."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

WIKI_LINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
TAG_RE = re.compile(r"(?<![\w/])#([A-Za-z0-9][\w/-]*)")
IGNORED_PARTS = {".git", ".obsidian", ".trash", "node_modules", "__pycache__"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path)
    parser.add_argument("--output", type=Path, help="Write Markdown report to this path")
    parser.add_argument(
        "--allow-inside-vault",
        action="store_true",
        help="Permit an output path inside the vault when the user explicitly requested it",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown")
    return parser.parse_args()


def is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def markdown_files(vault: Path) -> list[Path]:
    return sorted(
        path
        for path in vault.rglob("*.md")
        if not any(part in IGNORED_PARTS for part in path.relative_to(vault).parts)
    )


def clean_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return unquote(target).replace("\\", "/").removesuffix(".md").strip("/")


def build_index(vault: Path, files: list[Path]) -> tuple[dict[str, list[Path]], dict[str, list[Path]]]:
    by_path: dict[str, list[Path]] = defaultdict(list)
    by_stem: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        relative = path.relative_to(vault).with_suffix("").as_posix().casefold()
        by_path[relative].append(path)
        by_stem[path.stem.casefold()].append(path)
    return by_path, by_stem


def resolve_wiki(target: str, by_path: dict[str, list[Path]], by_stem: dict[str, list[Path]]) -> list[Path]:
    key = clean_target(target).casefold()
    if not key:
        return []
    exact = by_path.get(key, [])
    if exact:
        return exact
    return by_stem.get(Path(key).name, [])


def resolve_markdown(source: Path, target: str, vault: Path) -> Path | None:
    clean = target.split("#", 1)[0].strip().strip("<>")
    if not clean or re.match(r"^[a-z][a-z0-9+.-]*:", clean, re.I):
        return None
    candidate = (source.parent / unquote(clean)).resolve()
    try:
        candidate.relative_to(vault)
    except ValueError:
        return candidate
    return candidate


def audit(vault: Path) -> dict[str, object]:
    files = markdown_files(vault)
    by_path, by_stem = build_index(vault, files)
    outgoing: Counter[Path] = Counter()
    incoming: Counter[Path] = Counter()
    broken: list[dict[str, str]] = []
    ambiguous: list[dict[str, object]] = []
    empty: list[str] = []
    missing_frontmatter: list[str] = []
    tags: Counter[str] = Counter()

    for source in files:
        relative_source = source.relative_to(vault).as_posix()
        text = source.read_text(encoding="utf-8", errors="replace")
        if not text.strip():
            empty.append(relative_source)
        if not text.startswith("---\n"):
            missing_frontmatter.append(relative_source)
        tags.update(match.casefold() for match in TAG_RE.findall(text))

        for raw in WIKI_LINK_RE.findall(text):
            matches = resolve_wiki(raw, by_path, by_stem)
            outgoing[source] += 1
            if len(matches) == 1:
                incoming[matches[0]] += 1
            elif not matches:
                broken.append({"source": relative_source, "target": raw, "kind": "wikilink"})
            else:
                ambiguous.append(
                    {
                        "source": relative_source,
                        "target": raw,
                        "matches": [path.relative_to(vault).as_posix() for path in matches],
                    }
                )

        for raw in MARKDOWN_LINK_RE.findall(text):
            candidate = resolve_markdown(source, raw, vault)
            if candidate is None:
                continue
            outgoing[source] += 1
            if candidate.exists():
                if candidate.suffix.casefold() == ".md" and candidate in files:
                    incoming[candidate] += 1
            else:
                broken.append({"source": relative_source, "target": raw, "kind": "markdown"})

    duplicates = {
        stem: [path.relative_to(vault).as_posix() for path in paths]
        for stem, paths in sorted(by_stem.items())
        if len(paths) > 1
    }
    orphans = [
        path.relative_to(vault).as_posix()
        for path in files
        if incoming[path] == 0 and outgoing[path] == 0
    ]
    return {
        "vault": str(vault),
        "summary": {
            "notes": len(files),
            "broken_links": len(broken),
            "ambiguous_links": len(ambiguous),
            "orphan_notes": len(orphans),
            "duplicate_stems": len(duplicates),
            "empty_notes": len(empty),
            "missing_frontmatter": len(missing_frontmatter),
        },
        "broken_links": broken,
        "ambiguous_links": ambiguous,
        "orphans": orphans,
        "duplicate_stems": duplicates,
        "empty_notes": empty,
        "missing_frontmatter": missing_frontmatter,
        "top_tags": tags.most_common(30),
    }


def markdown_report(report: dict[str, object]) -> str:
    summary = report["summary"]
    lines = [
        "# Obsidian Vault Audit",
        "",
        f"Vault: `{report['vault']}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- {key.replace('_', ' ').title()}: {value}")
    for title, key in (
        ("Broken links", "broken_links"),
        ("Ambiguous links", "ambiguous_links"),
        ("Orphan notes", "orphans"),
        ("Duplicate stems", "duplicate_stems"),
        ("Empty notes", "empty_notes"),
        ("Missing frontmatter", "missing_frontmatter"),
        ("Top tags", "top_tags"),
    ):
        value = report[key]
        lines.extend(["", f"## {title}", "", "```json", json.dumps(value, indent=2, ensure_ascii=False), "```"])
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    vault = args.vault.resolve()
    if not vault.is_dir():
        raise SystemExit(f"Vault does not exist: {vault}")
    report = audit(vault)
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n" if args.json else markdown_report(report)
    if args.output:
        output = args.output.resolve()
        if is_within(output, vault) and not args.allow_inside_vault:
            raise SystemExit(
                "Refusing to write the audit report inside the vault. "
                "Choose an external path or pass --allow-inside-vault after explicit approval."
            )
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Wrote {output}")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
