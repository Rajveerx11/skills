#!/usr/bin/env python3
"""Run the complete, reproducible local release gate for the skill portfolio."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SCRIPT_SUFFIXES = {".js", ".cjs", ".mjs"}
SHELL_SMOKE_RE = re.compile(r"^smoke(?:-[a-z0-9][a-z0-9._-]*)?\.sh$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=HERE.parents[3])
    return parser.parse_args()


def run(command: list[str], repo: Path, env: dict[str, str]) -> bool:
    result = subprocess.run(
        command,
        cwd=repo,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    label = " ".join(command)
    if result.returncode:
        print(f"FAIL: {label}")
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip())
        return False
    print(f"PASS: {label}")
    return True


def static_checks(repo: Path) -> list[str]:
    failures: list[str] = []
    files = [
        path
        for path in (repo / "skills").rglob("*")
        if path.is_file() and "node_modules" not in path.parts and "__pycache__" not in path.parts
    ]
    for path in files:
        relative = path.relative_to(repo).as_posix()
        if path.suffix == ".py":
            try:
                compile(path.read_text(encoding="utf-8"), str(path), "exec")
            except (SyntaxError, UnicodeError) as error:
                failures.append(f"{relative}: Python syntax: {error}")
        elif path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeError) as error:
                failures.append(f"{relative}: JSON: {error}")

    manifest = repo / "skills-manifest.json"
    try:
        json.loads(manifest.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as error:
        failures.append(f"skills-manifest.json: JSON: {error}")

    markdown_files = [path for path in files if path.suffix.casefold() == ".md"]
    link_count = 0
    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0].strip("<>")
            if (
                not target
                or target.startswith(("#", "/"))
                or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I)
                or any(character in target for character in "{}*")
            ):
                continue
            link_count += 1
            if not (path.parent / unquote(target)).resolve().exists():
                failures.append(f"{path.relative_to(repo).as_posix()}: broken link: {raw_target}")
    print(
        f"Static checks: files={len(files)} markdown={len(markdown_files)} "
        f"relative_links={link_count} failures={len(failures)}"
    )
    return failures


def discovered_tests(repo: Path) -> list[list[str]]:
    commands: list[list[str]] = []
    for path in sorted((repo / "skills").rglob("test*.py")):
        if "node_modules" not in path.parts:
            commands.append([sys.executable, "-X", "utf8", str(path)])
    for path in sorted((repo / "skills").rglob("*")):
        if not path.is_file() or "node_modules" in path.parts:
            continue
        if path.name.startswith("test-") and path.suffix == ".mjs":
            commands.append(["node", str(path)])
        elif any(path.name.endswith(suffix) for suffix in (".test.js", ".test.cjs", ".test.mjs")):
            commands.append(["node", str(path)])
    commands.extend(discovered_shell_smoke_tests(repo))
    return commands


def discovered_shell_smoke_tests(repo: Path) -> list[list[str]]:
    """Discover opt-in shell smokes named smoke.sh/smoke-*.sh in scripts/tests/."""
    commands: list[list[str]] = []
    for path in sorted((repo / "skills").rglob("*.sh")):
        if (
            path.is_file()
            and "node_modules" not in path.parts
            and path.parent.name == "tests"
            and path.parent.parent.name == "scripts"
            and SHELL_SMOKE_RE.fullmatch(path.name)
        ):
            commands.append(["bash", path.relative_to(repo).as_posix()])
    return commands


def syntax_commands(repo: Path) -> list[list[str]]:
    commands: list[list[str]] = []
    node_files = sorted(
        path
        for path in (repo / "skills").rglob("*")
        if path.is_file() and path.suffix in SCRIPT_SUFFIXES and "node_modules" not in path.parts
    )
    shell_files = sorted(
        path
        for path in (repo / "skills").rglob("*.sh")
        if "node_modules" not in path.parts
    )
    if node_files and not shutil.which("node"):
        raise SystemExit("Node.js is required to validate JavaScript skills.")
    if shell_files and not shutil.which("bash"):
        raise SystemExit("Bash is required to validate shell scripts.")
    commands.extend(["node", "--check", str(path)] for path in node_files)
    commands.extend(
        ["bash", "-n", path.relative_to(repo).as_posix()]
        for path in shell_files
    )
    return commands


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    failures = static_checks(repo)
    commands = [
        [
            sys.executable,
            "-X",
            "utf8",
            str(HERE / "validate_portfolio.py"),
            str(repo),
            "--strict-warnings",
        ],
        *discovered_tests(repo),
        *syntax_commands(repo),
    ]
    passed = 0
    for command in commands:
        if run(command, repo, env):
            passed += 1
        else:
            failures.append("command failed: " + " ".join(command))
    for failure in failures:
        print(f"FAIL: {failure}")
    print(f"Release checks: commands={len(commands)} passed={passed} failures={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
