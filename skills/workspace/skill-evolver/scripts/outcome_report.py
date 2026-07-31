#!/usr/bin/env python3
"""Summarize private skill outcome evidence without mutating skills."""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter, defaultdict
from pathlib import Path


def default_store() -> Path:
    base = Path(os.environ.get("USERPROFILE") or Path.home())
    return base / ".skill-evolver" / "outcomes.jsonl"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill")
    parser.add_argument("--store", type=Path, default=default_store())
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.store.exists():
        print("No outcome evidence recorded.")
        return 0

    grouped: dict[str, list[dict]] = defaultdict(list)
    for line in args.store.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        skill = str(record.get("skill", "unknown"))
        if args.skill and skill != args.skill.lower():
            continue
        grouped[skill].append(record)

    if args.json:
        print(json.dumps(grouped, indent=2, ensure_ascii=False))
        return 0

    for skill in sorted(grouped):
        records = grouped[skill]
        signals = Counter(str(item.get("signal", "unknown")) for item in records)
        print(f"{skill}: {len(records)} records; " + ", ".join(f"{k}={v}" for k, v in sorted(signals.items())))
        for item in records[-10:]:
            evidence = f" | {item.get('evidence')}" if item.get("evidence") else ""
            print(f"  - [{item.get('signal')}] {item.get('observation')}{evidence}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
