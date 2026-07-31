#!/usr/bin/env python3
"""Regression tests for provider-neutral calendar fingerprints."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("sync_fingerprint.py")
SPEC = importlib.util.spec_from_file_location("sync_fingerprint", MODULE_PATH)
assert SPEC and SPEC.loader
sync_fingerprint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync_fingerprint)


class SyncFingerprintTests(unittest.TestCase):
    def setUp(self) -> None:
        self.canonical = {
            "id": "sandbox-feature",
            "title": "Sandbox feature",
            "start": "2026-06-15T11:00:00+05:30",
            "end": "2026-06-15T13:00:00+05:30",
            "timezone": "Asia/Kolkata",
            "type": "event",
            "reminder_min": 10,
        }

    def test_google_and_outlook_mappings_share_fingerprint(self) -> None:
        google = {
            "summary": "Sandbox feature",
            "start": {"dateTime": self.canonical["start"], "timeZone": self.canonical["timezone"]},
            "end": {"dateTime": self.canonical["end"], "timeZone": self.canonical["timezone"]},
        }
        outlook = {
            "subject": "Sandbox feature",
            "start": {"dateTime": self.canonical["start"], "timeZone": self.canonical["timezone"]},
            "end": {"dateTime": self.canonical["end"], "timeZone": self.canonical["timezone"]},
        }
        from_google = {
            **self.canonical,
            "title": google["summary"],
            "start": google["start"]["dateTime"],
            "end": google["end"]["dateTime"],
            "timezone": google["start"]["timeZone"],
        }
        from_outlook = {
            **self.canonical,
            "title": outlook["subject"],
            "start": outlook["start"]["dateTime"],
            "end": outlook["end"]["dateTime"],
            "timezone": outlook["start"]["timeZone"],
        }
        self.assertEqual(
            sync_fingerprint.fingerprint(from_google),
            sync_fingerprint.fingerprint(from_outlook),
        )

    def test_changed_time_changes_fingerprint_and_key_order_does_not(self) -> None:
        reordered = dict(reversed(list(self.canonical.items())))
        self.assertEqual(
            sync_fingerprint.fingerprint(self.canonical),
            sync_fingerprint.fingerprint(reordered),
        )
        changed = {**self.canonical, "end": "2026-06-15T13:30:00+05:30"}
        self.assertNotEqual(
            sync_fingerprint.fingerprint(self.canonical),
            sync_fingerprint.fingerprint(changed),
        )


if __name__ == "__main__":
    unittest.main()
