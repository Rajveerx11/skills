#!/usr/bin/env python3
"""Validate a dual Codex/Claude skill portfolio without third-party packages."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_REFERENCE_RE = re.compile(r"`((?:references|scripts|assets)/[^`\s]+)`")
IGNORED_PARTS = {".git", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache"}
PORTABLE_KEYS = {"name", "description"}
PROFILE_KEYS = {"outcome", "freedom", "quality_gates", "learning"}


@dataclass
class Finding:
    level: str
    skill: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict-warnings", action="store_true")
    return parser.parse_args()


def skill_files(root: Path) -> list[Path]:
    if (root / "SKILL.md").is_file():
        return [root / "SKILL.md"]
    return sorted(
        path
        for path in root.rglob("SKILL.md")
        if not any(part in IGNORED_PARTS for part in path.parts)
    )


def frontmatter(text: str) -> tuple[dict[str, object], str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, "missing opening delimiter"
    end = normalized.find("\n---\n", 4)
    if end < 0:
        return {}, "missing closing delimiter"
    raw = normalized[4:end]
    data: dict[str, object] = {}
    active: str | None = None
    folded: list[str] = []
    for line in raw.splitlines():
        if active and (line.startswith("  ") or not line.strip()):
            folded.append(line.strip())
            continue
        if active:
            data[active] = " ".join(folded).strip()
            active = None
            folded = []
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if not match:
            continue
        key, value = match.groups()
        value = (value or "").strip()
        if value in {">", "|", ">-", "|-"}:
            active = key
            continue
        data[key] = value.strip("\"'")
    if active:
        data[active] = " ".join(folded).strip()
    return data, ""


def add(findings: list[Finding], level: str, skill: str, path: Path, message: str) -> None:
    findings.append(Finding(level, skill, str(path), message))


def validate_openai_yaml(base: Path, skill: str, findings: list[Finding]) -> None:
    path = base / "agents" / "openai.yaml"
    if not path.is_file():
        add(findings, "error", skill, path, "missing agents/openai.yaml")
        return
    text = path.read_text(encoding="utf-8")
    fields: dict[str, str] = {}
    for key in ("display_name", "short_description", "default_prompt"):
        match = re.search(rf'(?m)^\s{{2}}{key}:\s+"([^"\r\n]*)"\s*$', text)
        if not match:
            add(findings, "error", skill, path, f"missing quoted interface.{key}")
        else:
            fields[key] = match.group(1)
    short = fields.get("short_description", "")
    if short and not 25 <= len(short) <= 64:
        add(findings, "error", skill, path, "short_description must be 25-64 characters")
    prompt = fields.get("default_prompt", "")
    if prompt and f"${skill}" not in prompt:
        add(findings, "error", skill, path, f"default_prompt must mention ${skill}")
    if "TODO" in text:
        add(findings, "error", skill, path, "contains TODO placeholder")


def validate_resources(base: Path, skill: str, text: str, findings: list[Finding]) -> None:
    raw_targets = list(LINK_RE.findall(text)) + list(CODE_REFERENCE_RE.findall(text))
    for raw_target in raw_targets:
        target = raw_target.strip().split("#", 1)[0].strip("<>").rstrip(".,:;")
        if (
            not target
            or re.match(r"^[a-z]+://", target, re.I)
            or target.startswith("#")
            or "$" in target
            or "<" in target
        ):
            continue
        if not (base / target).resolve().exists():
            add(findings, "error", skill, base / "SKILL.md", f"broken relative resource: {raw_target}")


def validate_python(base: Path, skill: str, findings: list[Finding]) -> None:
    for path in base.rglob("*.py"):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as error:
            add(findings, "error", skill, path, f"Python parse failed: {error}")


def validate_skill(path: Path, names: dict[str, Path], findings: list[Finding]) -> str | None:
    skill = path.parent.name
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        add(findings, "error", skill, path, f"not UTF-8: {error}")
        return None
    data, error = frontmatter(text)
    if error:
        add(findings, "error", skill, path, error)
        return None
    name = str(data.get("name", ""))
    description = str(data.get("description", ""))
    if not name:
        add(findings, "error", skill, path, "missing name")
    elif not NAME_RE.fullmatch(name):
        add(findings, "error", skill, path, "name must use lowercase hyphen-case")
    elif name != skill:
        add(findings, "error", skill, path, f"name '{name}' differs from folder '{skill}'")
    elif name in names:
        add(findings, "error", skill, path, f"duplicate name; first at {names[name]}")
    else:
        names[name] = path
    if not description:
        add(findings, "error", skill, path, "missing description")
    if len(description) > 1024:
        add(findings, "error", skill, path, "description exceeds 1024 characters")
    if "<" in description or ">" in description:
        add(findings, "error", skill, path, "description contains angle brackets")
    unsupported = sorted(set(data) - PORTABLE_KEYS)
    if unsupported:
        add(findings, "error", skill, path, f"non-portable frontmatter keys: {', '.join(unsupported)}")
    lines = text.count("\n") + 1
    if lines > 500:
        add(findings, "warning", skill, path, f"SKILL.md has {lines} lines; use progressive disclosure")
    if "TODO" in text or "[TODO" in text:
        add(findings, "error", skill, path, "contains TODO placeholder")
    if "catalog stub" in text.lower():
        add(findings, "error", skill, path, "catalog stub has no local executable workflow")
    if text.count("<!-- skill-evolver:adaptive-start -->") != 1:
        add(findings, "error", skill, path, "must contain exactly one adaptive-start marker")
    if text.count("<!-- skill-evolver:adaptive-end -->") != 1:
        add(findings, "error", skill, path, "must contain exactly one adaptive-end marker")
    validate_resources(path.parent, skill, text, findings)
    validate_openai_yaml(path.parent, skill, findings)
    validate_python(path.parent, skill, findings)
    return name or None


def validate_manifest(root: Path, names: set[str], findings: list[Finding]) -> None:
    repo = root if (root / "skills").is_dir() else root.parent
    path = repo / "skills-manifest.json"
    if not path.is_file():
        add(findings, "error", "portfolio", path, "missing skills-manifest.json")
        return
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        add(findings, "error", "portfolio", path, f"invalid JSON: {error}")
        return
    entries = manifest.get("skills", [])
    manifest_names = [item.get("name") for item in entries if isinstance(item, dict)]
    if len(manifest_names) != len(set(manifest_names)):
        add(findings, "error", "portfolio", path, "duplicate manifest names")
    missing = sorted(names - set(manifest_names))
    extra = sorted(set(manifest_names) - names)
    if missing:
        add(findings, "error", "portfolio", path, f"manifest missing: {', '.join(missing)}")
    if extra:
        add(findings, "error", "portfolio", path, f"manifest has unknown skills: {', '.join(extra)}")
    for item in entries:
        if not isinstance(item, dict):
            continue
        source = repo / str(item.get("path", ""))
        if not (source / "SKILL.md").is_file():
            add(findings, "error", str(item.get("name")), path, f"invalid source path: {source}")
        targets = item.get("targets", [])
        if not targets or set(targets) - {"codex", "claude", "agents"}:
            add(findings, "error", str(item.get("name")), path, f"invalid targets: {targets}")


def validate_profiles(root: Path, names: set[str], findings: list[Finding]) -> None:
    repo = root if (root / "skills").is_dir() else root.parent
    path = repo / "skills" / "workspace" / "skill-evolver" / "references" / "quality-profiles.json"
    try:
        profiles = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        add(findings, "error", "portfolio", path, f"cannot read profiles: {error}")
        return
    missing = sorted(names - set(profiles))
    extra = sorted(set(profiles) - names)
    if missing:
        add(findings, "error", "portfolio", path, f"profiles missing: {', '.join(missing)}")
    if extra:
        add(findings, "error", "portfolio", path, f"profiles have unknown skills: {', '.join(extra)}")
    for name, profile in profiles.items():
        if not isinstance(profile, dict) or not PROFILE_KEYS.issubset(profile):
            add(findings, "error", name, path, "profile missing required fields")
            continue
        gates = profile.get("quality_gates")
        if not isinstance(gates, list) or len(gates) != 3 or not all(isinstance(gate, str) and gate for gate in gates):
            add(findings, "error", name, path, "quality_gates must contain three strings")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.exists():
        print(f"Root does not exist: {root}", file=sys.stderr)
        return 2
    files = skill_files(root)
    findings: list[Finding] = []
    names: dict[str, Path] = {}
    for path in files:
        validate_skill(path, names, findings)
    validate_manifest(root, set(names), findings)
    validate_profiles(root, set(names), findings)
    errors = sum(item.level == "error" for item in findings)
    warnings = sum(item.level == "warning" for item in findings)
    if args.json:
        print(json.dumps({
            "skills": len(files),
            "errors": errors,
            "warnings": warnings,
            "findings": [asdict(item) for item in findings],
        }, indent=2))
    else:
        for item in findings:
            print(f"{item.level.upper()} [{item.skill}] {item.message} ({item.path})")
        print(f"Validated {len(files)} skills: {errors} errors, {warnings} warnings")
    return 1 if errors or (args.strict_warnings and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
