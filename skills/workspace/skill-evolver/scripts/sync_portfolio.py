#!/usr/bin/env python3
"""Plan, verify, or transactionally synchronize a canonical skill portfolio."""

from __future__ import annotations

import argparse
import ctypes
import fnmatch
import hashlib
import json
import os
import shutil
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

BASE_EXCLUDES = {
    ".git",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".consent",
}
VALID_TARGETS = ("codex", "claude", "agents")
REPARSE_POINT = 0x0400


@dataclass(frozen=True)
class Operation:
    source: str | None
    destination: str
    target: str
    skill: str
    action: str
    source_sha256: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--prune", action="store_true", help="Back up and remove stale destination files")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--details", action="store_true", help="Print every planned file operation")
    parser.add_argument("--target", choices=("all", *VALID_TARGETS), default="all")
    return parser.parse_args()


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def tree_digest(path: Path) -> str:
    hasher = hashlib.sha256()
    for item in sorted(
        (candidate for candidate in path.rglob("*") if candidate.is_file()),
        key=lambda candidate: candidate.relative_to(path).as_posix(),
    ):
        relative = item.relative_to(path).as_posix()
        hasher.update(relative.encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(digest(item).encode("ascii"))
        hasher.update(b"\0")
    return hasher.hexdigest()


def is_reparse_point(path: Path) -> bool:
    if path.is_symlink():
        return True
    if os.name != "nt":
        return False
    attributes = ctypes.windll.kernel32.GetFileAttributesW(str(path))
    return attributes != -1 and bool(attributes & REPARSE_POINT)


def direct_skill_directories(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted(
        (
            directory
            for directory in root.iterdir()
            if directory.is_dir()
            and not is_reparse_point(directory)
            and (directory / "SKILL.md").is_file()
        ),
        key=lambda directory: directory.name.casefold(),
    )


def excluded(relative: Path, patterns: list[str]) -> bool:
    if any(part in BASE_EXCLUDES for part in relative.parts):
        return True
    if any(part == ".env" or part.startswith(".env.") and part != ".env.example" for part in relative.parts):
        return True
    relative_text = relative.as_posix()
    return any(
        fnmatch.fnmatchcase(relative_text, pattern.replace("\\", "/"))
        for pattern in patterns
    )


def load_manifest(path: Path) -> dict:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("schema") != 1 or not isinstance(manifest.get("skills"), list):
        raise SystemExit(f"Unsupported manifest schema: {path}")
    names: set[str] = set()
    for item in manifest["skills"]:
        name = item.get("name")
        path = item.get("path")
        targets = item.get("targets")
        if not isinstance(name, str) or not name or name in names:
            raise SystemExit(f"Invalid or duplicate manifest skill: {name!r}")
        names.add(name)
        if not isinstance(path, str) or not path or Path(path).is_absolute():
            raise SystemExit(f"Skill has invalid canonical path: {name}")
        if not isinstance(targets, list) or not targets:
            raise SystemExit(f"Skill has no targets: {name}")
        if len(targets) != len(set(targets)):
            raise SystemExit(f"Skill has duplicate targets: {name}")
        invalid = sorted(set(targets) - set(VALID_TARGETS))
        if invalid:
            raise SystemExit(f"Invalid targets for {name}: {', '.join(invalid)}")
        patterns = item.get("runtime_excludes", [])
        if not isinstance(patterns, list) or not all(
            isinstance(pattern, str) and pattern for pattern in patterns
        ):
            raise SystemExit(f"Skill has invalid runtime exclusions: {name}")
    return manifest


def ensure_within(path: Path, root: Path, label: str) -> None:
    resolved = path.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as error:
        raise SystemExit(f"{label} escapes root: {resolved}") from error


def canonical_files(source_dir: Path, patterns: list[str]) -> dict[Path, Path]:
    files: dict[Path, Path] = {}
    for source in source_dir.rglob("*"):
        if not source.is_file():
            continue
        try:
            source.resolve().relative_to(source_dir.resolve())
        except ValueError as error:
            raise SystemExit(f"Canonical file escapes skill root: {source}") from error
        relative = source.relative_to(source_dir)
        if not excluded(relative, patterns):
            files[relative] = source
    return files


def collect_operations(
    repo: Path,
    manifest: dict,
    roots: dict[str, Path],
    target_filter: str,
    include_deletes: bool,
) -> tuple[list[Operation], list[str]]:
    operations: list[Operation] = []
    stale: list[str] = []
    selected_targets = {
        target
        for target in VALID_TARGETS
        if target_filter == "all" or target == target_filter
    }
    expected_directories = {
        target: {
            item["name"]
            for item in manifest["skills"]
            if target in item["targets"]
        }
        for target in selected_targets
    }
    for item in manifest["skills"]:
        source_dir = (repo / item["path"]).resolve()
        ensure_within(source_dir, repo, f"Source for {item['name']}")
        if not (source_dir / "SKILL.md").is_file():
            raise SystemExit(f"Missing canonical SKILL.md: {source_dir}")
        patterns = item.get("runtime_excludes", [])
        source_files = canonical_files(source_dir, patterns)
        for target in item["targets"]:
            if target_filter != "all" and target != target_filter:
                continue
            root = roots[target].resolve()
            target_dir = root / item["name"]
            ensure_within(target_dir, root, f"Target for {item['name']}")
            for relative, source in source_files.items():
                destination = target_dir / relative
                ensure_within(destination, root, f"Destination for {item['name']}")
                source_hash = digest(source)
                if not destination.exists():
                    action = "add"
                elif digest(destination) != source_hash:
                    action = "update"
                else:
                    continue
                operations.append(
                    Operation(str(source), str(destination), target, item["name"], action, source_hash)
                )
            if target_dir.is_dir():
                for destination in target_dir.rglob("*"):
                    if not destination.is_file():
                        continue
                    relative = destination.relative_to(target_dir)
                    if excluded(relative, patterns) or relative in source_files:
                        continue
                    label = f"{target}:{item['name']}:{relative.as_posix()}"
                    stale.append(label)
                    if include_deletes:
                        operations.append(
                            Operation(None, str(destination), target, item["name"], "delete", None)
                        )
    for target in sorted(selected_targets):
        root = roots[target].resolve()
        for directory in direct_skill_directories(root):
            if directory.name in expected_directories[target]:
                continue
            ensure_within(directory, root, f"Out-of-policy skill for {target}")
            label = f"{target}:{directory.name}:<whole-skill-directory>"
            stale.append(label)
            if include_deletes:
                operations.append(
                    Operation(
                        None,
                        str(directory),
                        target,
                        directory.name,
                        "delete-tree",
                        None,
                    )
                )
    operations.sort(key=lambda item: (item.target, item.skill, item.destination, item.action))
    return operations, sorted(stale)


def print_plan(operations: list[Operation], stale: list[str]) -> None:
    counts: dict[str, int] = {}
    skills: set[str] = set()
    for operation in operations:
        key = f"{operation.target}:{operation.action}"
        counts[key] = counts.get(key, 0) + 1
        skills.add(operation.skill)
    summary = ", ".join(f"{key}={counts[key]}" for key in sorted(counts)) or "no changes"
    print(f"Sync plan: {summary}; skills={len(skills)}; stale={len(stale)}")


def operation_label(operation: Operation, roots: dict[str, Path]) -> str:
    if operation.action == "delete-tree":
        return f"delete-tree {operation.target}:{operation.skill}:<whole-skill-directory>"
    target_skill = roots[operation.target] / operation.skill
    relative = Path(operation.destination).relative_to(target_skill).as_posix()
    return f"{operation.action} {operation.target}:{operation.skill}:{relative}"


def verify_manifest(
    repo: Path,
    manifest: dict,
    roots: dict[str, Path],
    target_filter: str,
) -> list[str]:
    operations, _ = collect_operations(repo, manifest, roots, target_filter, include_deletes=True)
    return [operation_label(operation, roots) for operation in operations]


def atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.skill-evolver-{uuid.uuid4().hex}.tmp")
    try:
        shutil.copy2(source, temporary)
        if digest(source) != digest(temporary):
            raise RuntimeError(f"Temporary hash verification failed: {destination}")
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def write_receipt(path: Path, receipt: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def prepare_transaction(
    operations: list[Operation],
    roots: dict[str, Path],
    backup: Path,
    repo: Path,
    manifest_path: Path,
    stamp: str,
) -> tuple[list[dict], Path]:
    records: list[dict] = []
    for operation in operations:
        destination = Path(operation.destination)
        relative = destination.relative_to(roots[operation.target])
        original = backup / "original" / operation.target / relative
        staged = backup / "staged" / operation.target / relative
        old_hash: str | None = None
        if operation.action in {"update", "delete"}:
            original.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(destination, original)
            old_hash = digest(original)
        elif operation.action == "delete-tree":
            original.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(destination, original, symlinks=True)
            old_hash = tree_digest(original)
        if operation.action in {"add", "update"}:
            source = Path(operation.source or "")
            staged.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, staged)
            if digest(staged) != operation.source_sha256:
                raise RuntimeError(f"Staging hash verification failed: {source}")
        record = asdict(operation)
        record.update(
            {
                "old_sha256": old_hash,
                "backup": str(original) if original.exists() else None,
                "staged": str(staged) if staged.exists() else None,
            }
        )
        records.append(record)
    receipt = {
        "schema": 1,
        "status": "pending",
        "timestamp": stamp,
        "repo": str(repo),
        "manifest": str(manifest_path),
        "operations": records,
    }
    receipt_path = backup / "sync-receipt.json"
    write_receipt(receipt_path, receipt)
    return records, receipt_path


def rollback(records: list[dict], roots: dict[str, Path]) -> None:
    for record in reversed(records):
        destination = Path(record["destination"])
        if record["action"] == "add":
            destination.unlink(missing_ok=True)
        elif record["action"] == "delete-tree":
            root = roots[record["target"]]
            ensure_within(destination, root, "Whole-skill rollback")
            if destination.resolve() == root.resolve():
                raise RuntimeError(f"Refusing to replace target root: {destination}")
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(Path(record["backup"]), destination, symlinks=True)
        else:
            backup = Path(record["backup"])
            atomic_copy(backup, destination)


def apply_transaction(
    records: list[dict],
    receipt_path: Path,
    receipt: dict,
    repo: Path,
    manifest: dict,
    roots: dict[str, Path],
    target_filter: str,
) -> None:
    fail_after = int(os.environ.get("SKILL_EVOLVER_TEST_FAIL_AFTER", "0") or "0")
    applied = 0
    current_record: dict | None = None
    try:
        for record in records:
            current_record = record
            destination = Path(record["destination"])
            if record["action"] == "delete":
                destination.unlink()
            elif record["action"] == "delete-tree":
                root = roots[record["target"]]
                ensure_within(destination, root, "Whole-skill deletion")
                if destination.resolve() == root.resolve():
                    raise RuntimeError(f"Refusing to delete target root: {destination}")
                shutil.rmtree(destination)
            else:
                atomic_copy(Path(record["staged"]), destination)
                if digest(destination) != record["source_sha256"]:
                    raise RuntimeError(f"Hash verification failed: {destination}")
            applied += 1
            current_record = None
            if fail_after and applied >= fail_after:
                raise RuntimeError("Injected sync failure")
        mismatches = verify_manifest(repo, manifest, roots, target_filter)
        if mismatches:
            raise RuntimeError(f"Post-sync verification failed: {len(mismatches)} mismatches")
    except Exception as error:
        rollback_records = records[:applied]
        if current_record is not None:
            rollback_records = [*rollback_records, current_record]
        rollback_error: Exception | None = None
        try:
            rollback(rollback_records, roots)
        except Exception as caught:
            rollback_error = caught
        receipt["status"] = "rollback_failed" if rollback_error else "rolled_back"
        receipt["error"] = str(error)
        receipt["applied_before_rollback"] = applied
        if rollback_error:
            receipt["rollback_error"] = str(rollback_error)
        write_receipt(receipt_path, receipt)
        if rollback_error:
            raise SystemExit(
                f"Sync failed and rollback also failed: {error}; rollback: {rollback_error}"
            ) from error
        raise SystemExit(f"Sync failed and rolled back: {error}") from error
    receipt["status"] = "completed"
    receipt["applied"] = applied
    write_receipt(receipt_path, receipt)


def main() -> int:
    args = parse_args()
    if args.apply and args.verify_only:
        raise SystemExit("Choose --apply or --verify-only, not both.")
    repo = args.repo.resolve()
    manifest_path = (args.manifest or repo / "skills-manifest.json").resolve()
    manifest = load_manifest(manifest_path)
    user = Path(os.environ.get("USERPROFILE") or Path.home()).resolve()
    roots = {
        "codex": user / ".codex" / "skills",
        "claude": user / ".claude" / "skills",
        "agents": user / ".agents" / "skills",
    }

    if args.verify_only:
        mismatches = verify_manifest(repo, manifest, roots, args.target)
        if mismatches:
            print("\n".join(mismatches))
            print(f"Verification failed: {len(mismatches)} mismatches")
            return 1
        print(f"Verification passed: {len(manifest['skills'])} manifest skills")
        return 0

    operations, stale = collect_operations(
        repo, manifest, roots, args.target, include_deletes=args.prune
    )
    print_plan(operations, stale)
    if stale:
        print("Stale destination files:")
        for item in stale:
            print(f"  - {item}")
    if args.details:
        print("Planned operations:")
        for operation in operations:
            print(f"  - {operation_label(operation, roots)}")
    if stale and not args.prune:
        print("Stale destination files found. Review a --prune dry run before applying exact sync.")
        if args.apply:
            return 2
    if not args.apply:
        print("Dry run only. Add --apply; add --prune for backup-backed exact sync.")
        return 0
    if not operations:
        print("No changes. Installed portfolio already exact.")
        return 0

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    backup = user / ".skill-evolver" / "backups" / stamp
    records, receipt_path = prepare_transaction(
        operations, roots, backup, repo, manifest_path, stamp
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    apply_transaction(records, receipt_path, receipt, repo, manifest, roots, args.target)
    print(f"Applied {len(records)} operations. Backup and receipt: {backup}")
    print("Post-sync exact verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
