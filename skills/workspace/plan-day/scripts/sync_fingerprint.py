#!/usr/bin/env python3
"""Create a provider-neutral SHA-256 fingerprint for one canonical calendar block."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

FIELDS = ("id", "title", "start", "end", "timezone", "type", "reminder_min")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="Canonical block JSON; omit for stdin")
    return parser.parse_args()


def canonical_block(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError("Calendar block must be a JSON object")
    missing = [field for field in FIELDS if field not in value]
    if missing:
        raise ValueError("Missing canonical fields: " + ", ".join(missing))
    block = {field: value[field] for field in FIELDS}
    if not all(isinstance(block[field], str) and block[field] for field in FIELDS[:-1]):
        raise ValueError("Canonical text fields must be non-empty strings")
    if not isinstance(block["reminder_min"], int) or isinstance(block["reminder_min"], bool):
        raise ValueError("reminder_min must be an integer")
    return block


def fingerprint(value: object) -> str:
    payload = json.dumps(
        canonical_block(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    args = parse_args()
    text = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
    try:
        value = json.loads(text)
        print(fingerprint(value))
    except (json.JSONDecodeError, OSError, ValueError) as error:
        raise SystemExit(f"Cannot fingerprint calendar block: {error}") from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
