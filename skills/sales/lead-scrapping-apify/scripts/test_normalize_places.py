#!/usr/bin/env python3
"""Security regression tests for normalize_places CSV output."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("normalize_places.py")


class NormalizePlacesCsvSafetyTests(unittest.TestCase):
    def test_formula_leading_external_fields_are_neutralized(self) -> None:
        dangerous = {
            "placeId": "safe-id",
            "title": '=HYPERLINK("https://example.invalid","click")',
            "categoryName": "+SUM(1,1)",
            "phone": "-2+3",
            "address": "@SUM(1,1)",
            "city": "Normal City",
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

        expected = {
            "name": dangerous["title"],
            "category": dangerous["categoryName"],
            "phone": dangerous["phone"],
            "address": dangerous["address"],
        }
        for field, value in expected.items():
            self.assertEqual(row[field], "'" + value)
        self.assertEqual(row["city"], "Normal City")


if __name__ == "__main__":
    unittest.main()
