#!/usr/bin/env python3
"""Regression tests for whole-skill drift and duplicate-install detection."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_script(
    name: str,
    *args: object,
    env: dict[str, str],
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(HERE / name), *(str(arg) for arg in args)],
        text=True,
        encoding="utf-8",
        errors="strict",
        capture_output=True,
        env=env,
        check=False,
    )


def write_skill(path: Path, name: str, body: str = "Current\n") -> None:
    path.mkdir(parents=True, exist_ok=True)
    (path / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: Test {name}.\n---\n\n{body}",
        encoding="utf-8",
        newline="\n",
    )


def make_repo(root: Path) -> Path:
    repo = root / "repo"
    write_skill(repo / "skills" / "checking" / "sample-skill", "sample-skill")
    manifest = {
        "schema": 1,
        "skills": [
            {
                "name": "sample-skill",
                "path": "skills/checking/sample-skill",
                "targets": ["codex"],
            }
        ],
    }
    (repo / "skills-manifest.json").write_text(
        json.dumps(manifest),
        encoding="utf-8",
        newline="\n",
    )
    return repo


class WholeSkillSyncTests(unittest.TestCase):
    def test_prune_backs_up_and_removes_out_of_policy_skill_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = make_repo(root)
            user = root / "user"
            expected = user / ".codex" / "skills" / "sample-skill"
            legacy = user / ".codex" / "skills" / "taste-skill"
            write_skill(expected, "sample-skill")
            write_skill(legacy, "sample-skill", "Legacy duplicate\n")
            (legacy / "private-state.md").write_text("backup me", encoding="utf-8")
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)

            before = run_script("sync_portfolio.py", repo, "--verify-only", env=env)
            self.assertNotEqual(before.returncode, 0)
            self.assertIn("delete-tree codex:taste-skill", before.stdout)

            plan = run_script(
                "sync_portfolio.py", repo, "--prune", "--details", env=env
            )
            self.assertEqual(plan.returncode, 0, plan.stderr + plan.stdout)
            self.assertIn("delete-tree codex:taste-skill", plan.stdout)

            applied = run_script(
                "sync_portfolio.py", repo, "--apply", "--prune", env=env
            )
            self.assertEqual(applied.returncode, 0, applied.stderr + applied.stdout)
            self.assertFalse(legacy.exists())
            backups = list(
                (user / ".skill-evolver" / "backups").rglob(
                    "original/codex/taste-skill/private-state.md"
                )
            )
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "backup me")
            verified = run_script("sync_portfolio.py", repo, "--verify-only", env=env)
            self.assertEqual(verified.returncode, 0, verified.stderr + verified.stdout)

    def test_whole_skill_delete_rolls_back_after_injected_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = make_repo(root)
            user = root / "user"
            expected = user / ".codex" / "skills" / "sample-skill"
            legacy = user / ".codex" / "skills" / "taste-skill"
            write_skill(expected, "sample-skill")
            write_skill(legacy, "sample-skill", "Legacy duplicate\n")
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)
            env["SKILL_EVOLVER_TEST_FAIL_AFTER"] = "1"

            failed = run_script(
                "sync_portfolio.py", repo, "--apply", "--prune", env=env
            )
            self.assertNotEqual(failed.returncode, 0)
            self.assertTrue((legacy / "SKILL.md").is_file())
            receipts = list(
                (user / ".skill-evolver" / "backups").rglob("sync-receipt.json")
            )
            self.assertEqual(len(receipts), 1)
            receipt = json.loads(receipts[0].read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"], "rolled_back")

    def test_failure_before_later_tree_delete_rolls_back_only_started_operations(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = make_repo(root)
            user = root / "user"
            expected = user / ".codex" / "skills" / "sample-skill"
            stale = user / ".codex" / "skills" / "z-stale"
            write_skill(expected, "sample-skill", "Old installed version\n")
            old_bytes = (expected / "SKILL.md").read_bytes()
            write_skill(stale, "z-stale", "Unapplied stale skill\n")
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)
            env["SKILL_EVOLVER_TEST_FAIL_AFTER"] = "1"

            failed = run_script(
                "sync_portfolio.py", repo, "--apply", "--prune", env=env
            )

            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual((expected / "SKILL.md").read_bytes(), old_bytes)
            self.assertTrue((stale / "SKILL.md").is_file())
            receipts = list(
                (user / ".skill-evolver" / "backups").rglob("sync-receipt.json")
            )
            self.assertEqual(len(receipts), 1)
            receipt = json.loads(receipts[0].read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"], "rolled_back")
            self.assertEqual(receipt["applied_before_rollback"], 1)

    def test_manifest_builder_rejects_duplicate_direct_names(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = make_repo(root)
            user = root / "user"
            write_skill(
                user / ".codex" / "skills" / "design-taste-frontend",
                "design-taste-frontend",
            )
            write_skill(
                user / ".codex" / "skills" / "taste-skill",
                "design-taste-frontend",
            )
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)

            result = run_script("build_manifest.py", repo, env=env)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Duplicate direct skill installs", result.stderr)
            self.assertIn("taste-skill", result.stderr)


if __name__ == "__main__":
    unittest.main()
