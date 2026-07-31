#!/usr/bin/env python3
"""Security regression tests for merge_leads CSV output."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("merge_leads.py")


class MergeLeadsCsvSafetyTests(unittest.TestCase):
    def test_formula_leading_external_fields_are_neutralized(self) -> None:
        dangerous = {
            "name": '=HYPERLINK("https://example.invalid","click")',
            "title": "+SUM(1,1)",
            "company": "-2+3",
            "evidence": "@SUM(1,1)",
            "domain": "normal.example",
        }

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "input.json"
            output = root / "output.csv"
            source.write_text(json.dumps([dangerous]), encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(SCRIPT), str(source), "--output", str(output)],
                text=True,
                encoding="utf-8",
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            with output.open("r", encoding="utf-8-sig", newline="") as handle:
                row = next(csv.DictReader(handle))

        for field in ("name", "title", "company", "evidence"):
            self.assertEqual(row[field], "'" + dangerous[field])
        self.assertEqual(row["domain"], "normal.example")


if __name__ == "__main__":
    unittest.main()
