#!/usr/bin/env python3
"""Regression tests for Obsidian audit output safety."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("audit_vault.py")


class AuditVaultTests(unittest.TestCase):
    def test_output_inside_vault_requires_explicit_override(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            vault = root / "vault"
            vault.mkdir()
            (vault / "note.md").write_text("# Note\n", encoding="utf-8")
            inside = vault / "audit.md"
            refused = subprocess.run(
                [sys.executable, str(SCRIPT), str(vault), "--output", str(inside)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(refused.returncode, 0)
            self.assertFalse(inside.exists())
            allowed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(vault),
                    "--output",
                    str(inside),
                    "--allow-inside-vault",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(allowed.returncode, 0, allowed.stderr + allowed.stdout)
            self.assertTrue(inside.is_file())

    def test_external_output_is_default(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            vault = root / "vault"
            vault.mkdir()
            (vault / "note.md").write_text("# Note\n", encoding="utf-8")
            output = root / "reports" / "audit.md"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(vault), "--output", str(output)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertTrue(output.is_file())


if __name__ == "__main__":
    unittest.main()
