#!/usr/bin/env python3
"""Regression tests for published-only learning scorecards."""

from __future__ import annotations

import importlib.util
import unittest
from datetime import date
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("weekly_score.py")
SPEC = importlib.util.spec_from_file_location("weekly_score", MODULE_PATH)
assert SPEC and SPEC.loader
weekly_score = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(weekly_score)


def record(day: str, artifacts: list[dict]) -> dict:
    return {
        "date": day,
        "_source": f"{day}.json",
        "activities": [{"track": "Writing", "minutes": 30, "consumed": 1}],
        "shipped": artifacts,
    }


class WeeklyScoreTests(unittest.TestCase):
    def test_only_unique_published_ids_count_and_drive_streak(self) -> None:
        draft = {"artifact_id": "draft-1", "status": "draft"}
        scheduled = {"artifact_id": "scheduled-1", "status": "scheduled"}
        published = {"artifact_id": "published-1", "status": "published"}
        records = [
            record("2026-07-29", [draft]),
            record("2026-07-30", [published, published]),
            record("2026-07-31", [scheduled, published]),
        ]
        report = weekly_score.score(records, date(2026, 7, 29), date(2026, 7, 31))
        self.assertEqual(report["shipped_units"], 1)
        self.assertEqual(report["published_artifact_ids"], ["published-1"])
        self.assertEqual(report["current_streak_days"], 2)
        self.assertEqual(report["days_logged"], 3)

    def test_legacy_boolean_or_numeric_shipped_values_do_not_inflate_output(self) -> None:
        records = [
            {
                "date": "2026-07-31",
                "_source": "2026-07-31.json",
                "activities": [{"track": "Code", "shipped": True}],
                "shipped": 7,
                "summary": {"shipped": 9},
            }
        ]
        report = weekly_score.score(records, date(2026, 7, 31), date(2026, 7, 31))
        self.assertEqual(report["shipped_units"], 0)
        self.assertEqual(report["current_streak_days"], 0)


if __name__ == "__main__":
    unittest.main()
