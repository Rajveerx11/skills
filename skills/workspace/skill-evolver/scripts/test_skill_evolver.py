#!/usr/bin/env python3
"""Regression tests for skill-evolver portfolio tooling."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import run_release_checks as release_checks

HERE = Path(__file__).resolve().parent


def run_script(name: str, *args: object, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(HERE / name), *(str(arg) for arg in args)],
        text=True,
        encoding="utf-8",
        errors="strict",
        capture_output=True,
        env=env,
        check=False,
    )


def sample_skill() -> str:
    return """---
name: sample-skill
description: Create a deterministic sample artifact when testing portfolio tools.
---

# Sample Skill

Complete the sample task and verify the artifact.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a verified sample artifact
- Freedom: Low.
- Autonomy: finish the fixture.
- Quality gate: output exists; content matches; rerun is idempotent.
- Learning: record nothing.
<!-- skill-evolver:adaptive-end -->
"""


def make_portfolio(root: Path) -> Path:
    skill = root / "skills" / "checking" / "sample-skill"
    (skill / "agents").mkdir(parents=True)
    (skill / "SKILL.md").write_text(sample_skill(), encoding="utf-8", newline="\n")
    (skill / "agents" / "openai.yaml").write_text(
        """interface:
  display_name: "Sample Skill"
  short_description: "Create a deterministic sample artifact"
  default_prompt: "Use $sample-skill to create the sample artifact."
""",
        encoding="utf-8",
        newline="\n",
    )
    evolver_refs = root / "skills" / "workspace" / "skill-evolver" / "references"
    evolver_refs.mkdir(parents=True)
    profiles = {
        "sample-skill": {
            "outcome": "a verified sample artifact",
            "freedom": "Low.",
            "quality_gates": ["output exists", "content matches", "rerun is idempotent"],
            "learning": "nothing",
        }
    }
    (evolver_refs / "quality-profiles.json").write_text(
        json.dumps(profiles), encoding="utf-8", newline="\n"
    )
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
    (root / "skills-manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8", newline="\n"
    )
    return skill


class SkillEvolverTests(unittest.TestCase):
    def test_release_gate_discovers_only_opt_in_shell_smokes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            test_dir = repo / "skills" / "video" / "sample" / "scripts" / "tests"
            test_dir.mkdir(parents=True)
            for name in ("smoke.sh", "smoke-render.sh", "setup.sh", "run.sh"):
                (test_dir / name).write_text("#!/usr/bin/env bash\n", encoding="utf-8")
            outside = repo / "skills" / "video" / "sample" / "scripts" / "smoke.sh"
            outside.write_text("#!/usr/bin/env bash\n", encoding="utf-8")

            commands = release_checks.discovered_shell_smoke_tests(repo)

            self.assertEqual(
                {tuple(command) for command in commands},
                {
                    (
                        "bash",
                        "skills/video/sample/scripts/tests/smoke-render.sh",
                    ),
                    ("bash", "skills/video/sample/scripts/tests/smoke.sh"),
                },
            )

    def test_portfolio_security_and_portability_invariants(self) -> None:
        repo = HERE.parents[3]
        skill_files = {
            name: repo / relative
            for name, relative in {
                "product-launch-video": "skills/video/product-launch-video/SKILL.md",
                "pr-to-video": "skills/video/pr-to-video/SKILL.md",
                "website-to-video": "skills/video/website-to-video/SKILL.md",
                "agent-reach": "skills/writing/agent-reach/SKILL.md",
                "researcher": "skills/writing/researcher/SKILL.md",
                "youtube-researcher": "skills/writing/youtube-researcher/SKILL.md",
            }.items()
        }
        for name, path in skill_files.items():
            text = path.read_text(encoding="utf-8")
            self.assertIn(
                "## Untrusted input invariant",
                text,
                f"{name} must define an explicit external-content trust boundary",
            )

        website_root = repo / "skills" / "video" / "website-to-video"
        website_text = "\n".join(
            path.read_text(encoding="utf-8", errors="strict")
            for path in website_root.rglob("*.md")
        )
        self.assertNotIn("skills/website-to-video", website_text)
        self.assertNotIn("skills/hyperframes", website_text)

        agent_reach_root = repo / "skills" / "writing" / "agent-reach"
        agent_reach_text = "\n".join(
            path.read_text(encoding="utf-8", errors="strict")
            for path in agent_reach_root.rglob("*.md")
        )
        self.assertNotIn("/tmp", agent_reach_text)

    def test_packaged_optional_sfx_is_truthful(self) -> None:
        repo = HERE.parents[3]
        for name in (
            "faceless-explainer",
            "pr-to-video",
            "product-launch-video",
            "website-to-video",
        ):
            root = repo / "skills" / "video" / name / "assets" / "sfx"
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(
                manifest,
                {},
                f"{name} must not advertise audio files that are not packaged",
            )
            self.assertEqual(
                list(root.glob("*.mp3")),
                [],
                f"{name} repository package must not silently vendor unreviewed audio",
            )
            credits = (root / "CREDITS.md").read_text(encoding="utf-8").casefold()
            self.assertIn("no sound-effect audio is bundled", credits)
            self.assertIn("licensed", credits)

    def test_video_trigger_precedence_is_explicit(self) -> None:
        repo = HERE.parents[3]
        shorts = (repo / "skills" / "video" / "shorts" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        launch = (
            repo / "skills" / "video" / "product-launch-video" / "SKILL.md"
        ).read_text(encoding="utf-8")
        shorts_description = shorts.split("---", 2)[1].casefold()
        launch_description = launch.split("---", 2)[1].casefold()
        self.assertIn("product-launch-video", shorts_description)
        self.assertIn("shorts", launch_description)
        self.assertIn("youtube short", shorts_description)
        self.assertIn("youtube short", launch_description)

    def test_repository_readme_matches_catalog_renderer(self) -> None:
        repo = HERE.parents[3]
        readme = repo / "README.md"
        if not readme.is_file():
            self.skipTest("Canonical repository README is unavailable")
        rendered = run_script("render_catalog.py", repo)
        self.assertEqual(rendered.returncode, 0, rendered.stderr + rendered.stdout)
        self.assertEqual(readme.read_text(encoding="utf-8"), rendered.stdout)

    def test_manifest_preserves_policy_and_requires_new_assignment(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = root / "repo"
            make_portfolio(repo)
            user = root / "empty-user"
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)
            stable = run_script("build_manifest.py", repo, "--apply", env=env)
            self.assertEqual(stable.returncode, 0, stable.stderr + stable.stdout)
            manifest = json.loads((repo / "skills-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["skills"][0]["targets"], ["codex"])
            new_skill = repo / "skills" / "writing" / "other-skill"
            new_skill.mkdir(parents=True)
            (new_skill / "SKILL.md").write_text(
                "---\nname: other-skill\ndescription: Exercise explicit target policy.\n---\n",
                encoding="utf-8",
            )
            missing = run_script("build_manifest.py", repo, env=env)
            self.assertNotEqual(missing.returncode, 0)
            assigned = run_script(
                "build_manifest.py", repo, "--apply", "--new-targets", "agents", env=env
            )
            self.assertEqual(assigned.returncode, 0, assigned.stderr + assigned.stdout)
            manifest = json.loads((repo / "skills-manifest.json").read_text(encoding="utf-8"))
            targets = {item["name"]: item["targets"] for item in manifest["skills"]}
            self.assertEqual(targets["sample-skill"], ["codex"])
            self.assertEqual(targets["other-skill"], ["agents"])

    def test_validator_accepts_complete_portfolio(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            make_portfolio(repo)
            result = run_script("validate_portfolio.py", repo)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertIn("0 errors, 0 warnings", result.stdout)

    def test_apply_profiles_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            skill = make_portfolio(repo)
            first = run_script("apply_profiles.py", repo, "--apply")
            self.assertEqual(first.returncode, 0, first.stderr + first.stdout)
            before = (skill / "SKILL.md").read_bytes()
            second = run_script("apply_profiles.py", repo)
            self.assertEqual(second.returncode, 0, second.stderr + second.stdout)
            self.assertIn("changed=0", second.stdout)
            self.assertEqual(before, (skill / "SKILL.md").read_bytes())

    def test_record_outcome_rejects_secret_and_deduplicates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            store = Path(temporary) / "outcomes.jsonl"
            args = (
                "--skill", "sample-skill",
                "--signal", "feedback",
                "--observation", "Prefer compact output",
                "--store", store,
            )
            first = run_script("record_outcome.py", *args)
            second = run_script("record_outcome.py", *args)
            self.assertEqual(first.returncode, 0, first.stderr + first.stdout)
            self.assertEqual(second.returncode, 0, second.stderr + second.stdout)
            self.assertEqual(len(store.read_text(encoding="utf-8").splitlines()), 1)
            secret = run_script(
                "record_outcome.py",
                "--skill", "sample-skill",
                "--signal", "failure",
                "--observation", "token=topsecretvalue",
                "--store", store,
            )
            self.assertNotEqual(secret.returncode, 0)

    def test_sync_backs_up_updates_and_verifies(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = root / "repo"
            source_skill = make_portfolio(repo)
            (source_skill / ".env").write_text("TOKEN=private", encoding="utf-8")
            (source_skill / ".env.example").write_text("TOKEN=", encoding="utf-8")
            user = root / "user"
            destination = user / ".codex" / "skills" / "sample-skill"
            destination.mkdir(parents=True)
            (destination / "SKILL.md").write_text("old", encoding="utf-8")
            (destination / "stale-secret.txt").write_text("stale", encoding="utf-8")
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)
            before = run_script("sync_portfolio.py", repo, "--verify-only", env=env)
            self.assertNotEqual(before.returncode, 0)
            self.assertIn("delete codex:sample-skill:stale-secret.txt", before.stdout)
            plan = run_script(
                "sync_portfolio.py", repo, "--prune", "--details", env=env
            )
            self.assertEqual(plan.returncode, 0, plan.stderr + plan.stdout)
            self.assertIn("delete codex:sample-skill:stale-secret.txt", plan.stdout)
            applied = run_script("sync_portfolio.py", repo, "--apply", "--prune", env=env)
            self.assertEqual(applied.returncode, 0, applied.stderr + applied.stdout)
            self.assertEqual(
                (source_skill / "SKILL.md").read_bytes(),
                (destination / "SKILL.md").read_bytes(),
            )
            self.assertFalse((destination / ".env").exists())
            self.assertTrue((destination / ".env.example").is_file())
            self.assertFalse((destination / "stale-secret.txt").exists())
            receipts = list((user / ".skill-evolver" / "backups").rglob("sync-receipt.json"))
            self.assertEqual(len(receipts), 1)
            receipt = json.loads(receipts[0].read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"], "completed")
            self.assertTrue(any(item["action"] == "delete" for item in receipt["operations"]))
            verified = run_script("sync_portfolio.py", repo, "--verify-only", env=env)
            self.assertEqual(verified.returncode, 0, verified.stderr + verified.stdout)

    def test_sync_preserves_manifest_excluded_runtime_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = root / "repo"
            source_skill = make_portfolio(repo)
            manifest_path = repo / "skills-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["skills"][0]["runtime_excludes"] = ["memory/**"]
            manifest_path.write_text(
                json.dumps(manifest),
                encoding="utf-8",
                newline="\n",
            )
            (source_skill / "memory" / "posts").mkdir(parents=True)
            (source_skill / "memory" / "posts" / "private.md").write_text(
                "canonical runtime placeholder",
                encoding="utf-8",
            )
            user = root / "user"
            destination = user / ".codex" / "skills" / "sample-skill"
            (destination / "memory" / "posts").mkdir(parents=True)
            private = destination / "memory" / "posts" / "private.md"
            private.write_text("user private state", encoding="utf-8")
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)
            applied = run_script("sync_portfolio.py", repo, "--apply", "--prune", env=env)
            self.assertEqual(applied.returncode, 0, applied.stderr + applied.stdout)
            self.assertEqual(private.read_text(encoding="utf-8"), "user private state")
            verified = run_script("sync_portfolio.py", repo, "--verify-only", env=env)
            self.assertEqual(verified.returncode, 0, verified.stderr + verified.stdout)

    def test_sync_rolls_back_injected_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = root / "repo"
            make_portfolio(repo)
            user = root / "user"
            destination = user / ".codex" / "skills" / "sample-skill"
            destination.mkdir(parents=True)
            (destination / "SKILL.md").write_text("old", encoding="utf-8")
            env = dict(os.environ)
            env["USERPROFILE"] = str(user)
            env["SKILL_EVOLVER_TEST_FAIL_AFTER"] = "1"
            failed = run_script("sync_portfolio.py", repo, "--apply", "--prune", env=env)
            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual((destination / "SKILL.md").read_text(encoding="utf-8"), "old")
            self.assertFalse((destination / "agents" / "openai.yaml").exists())
            receipts = list((user / ".skill-evolver" / "backups").rglob("sync-receipt.json"))
            self.assertEqual(len(receipts), 1)
            receipt = json.loads(receipts[0].read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"], "rolled_back")


if __name__ == "__main__":
    unittest.main()
