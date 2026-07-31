#!/usr/bin/env python3
"""Append one evidence record to the private skill-evolver outcome store."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

SIGNALS = ("feedback", "preference", "metric", "failure", "success")
SECRET_RE = re.compile(
    r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*\S+|"
    r"\b(?:ghp|github_pat|sk-[A-Za-z0-9_-]{8})[A-Za-z0-9_-]{12,}\b"
)


def default_store() -> Path:
    base = Path(os.environ.get("USERPROFILE") or Path.home())
    return base / ".skill-evolver" / "outcomes.jsonl"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", required=True)
    parser.add_argument("--signal", required=True, choices=SIGNALS)
    parser.add_argument("--observation", required=True)
    parser.add_argument("--evidence", default="")
    parser.add_argument("--artifact", default="")
    parser.add_argument("--run-id", default="")
    parser.add_argument("--store", type=Path, default=default_store())
    return parser.parse_args()


def clean(value: str) -> str:
    value = " ".join(value.strip().split())
    if SECRET_RE.search(value):
        raise SystemExit("Refusing to store text that resembles a secret.")
    return value


def recent_records(path: Path, limit: int = 250) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines()[-limit:]:
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return records


def main() -> int:
    args = parse_args()
    record = {
        "schema": 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "skill": clean(args.skill).lower(),
        "signal": args.signal,
        "observation": clean(args.observation),
        "evidence": clean(args.evidence),
        "artifact": clean(args.artifact),
        "run_id": clean(args.run_id),
        "status": "pending",
    }
    duplicate_key = (
        record["skill"],
        record["signal"],
        record["observation"].casefold(),
        record["evidence"].casefold(),
    )
    for old in recent_records(args.store):
        old_key = (
            old.get("skill"),
            old.get("signal"),
            str(old.get("observation", "")).casefold(),
            str(old.get("evidence", "")).casefold(),
        )
        if old_key == duplicate_key:
            print(f"Duplicate evidence skipped: {args.store}")
            return 0

    args.store.parent.mkdir(parents=True, exist_ok=True)
    with args.store.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Recorded pending evidence: {args.store}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
