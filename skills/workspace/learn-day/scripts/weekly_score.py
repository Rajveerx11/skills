#!/usr/bin/env python3
"""Calculate a deterministic learning scorecard from daily JSON logs."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logs", type=Path)
    parser.add_argument("--end", type=date.fromisoformat, default=date.today())
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def as_number(value: object) -> float:
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    return 0.0


def load_range(logs: Path, start: date, end: date) -> list[dict]:
    records: list[dict] = []
    current = start
    while current <= end:
        path = logs / f"{current.isoformat()}.json"
        if path.exists():
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise SystemExit(f"Invalid JSON in {path}: {error}") from error
            record["_source"] = str(path)
            records.append(record)
        current += timedelta(days=1)
    return records


def activities(record: dict) -> list[dict]:
    value = record.get("activities", record.get("items", record.get("studied", [])))
    return value if isinstance(value, list) else []


def artifact_records(record: dict, items: list[dict]) -> list[dict]:
    """Return structured artifact records without treating drafts as shipped."""
    candidates: list[object] = []
    for key in ("shipped", "artifacts", "posts"):
        value = record.get(key)
        if isinstance(value, list):
            candidates.extend(value)
    for item in items:
        for key in ("shipped", "artifacts"):
            value = item.get(key)
            if isinstance(value, list):
                candidates.extend(value)
            elif isinstance(value, dict):
                candidates.append(value)
    return [value for value in candidates if isinstance(value, dict)]


def published_artifact_ids(record: dict, items: list[dict]) -> set[str]:
    """Count only unique, explicitly published artifacts with stable identities."""
    published: set[str] = set()
    for artifact in artifact_records(record, items):
        artifact_id = artifact.get("artifact_id")
        if artifact.get("status") == "published" and isinstance(artifact_id, str) and artifact_id:
            published.add(artifact_id)
    return published


def score(records: list[dict], start: date, end: date) -> dict:
    tracks: Counter[str] = Counter()
    studied = minutes = 0.0
    logged_dates: list[date] = []
    published_dates: list[date] = []
    published_ids: set[str] = set()
    for record in records:
        items = activities(record)
        record_date = date.fromisoformat(str(record.get("date") or Path(record["_source"]).stem))
        artifacts = artifact_records(record, items)
        if items or artifacts or record.get("summary"):
            logged_dates.append(record_date)
        for item in items:
            track = str(item.get("track", "unclassified")).strip() or "unclassified"
            tracks[track] += 1
            minutes += as_number(item.get("minutes", item.get("duration_min", 0)))
            studied += as_number(item.get("consumed", item.get("sources", 1)))
        day_ids = published_artifact_ids(record, items)
        if day_ids:
            published_dates.append(record_date)
        published_ids.update(day_ids)

    streak = 0
    cursor = end
    published_days = set(published_dates)
    while cursor in published_days:
        streak += 1
        cursor -= timedelta(days=1)
    shipped = len(published_ids)
    ratio = shipped / studied if studied else None
    return {
        "range": {"start": start.isoformat(), "end": end.isoformat()},
        "days_expected": (end - start).days + 1,
        "days_logged": len(set(logged_dates)),
        "current_streak_days": streak,
        "study_units": studied,
        "shipped_units": shipped,
        "published_artifact_ids": sorted(published_ids),
        "consume_to_create_ratio": ratio,
        "minutes_recorded": minutes,
        "tracks": dict(tracks.most_common()),
        "sources": [record["_source"] for record in records],
    }


def render(report: dict) -> str:
    ratio = report["consume_to_create_ratio"]
    ratio_text = "n/a" if ratio is None else f"{ratio:.2f}"
    lines = [
        "# Learning Scorecard",
        "",
        f"- Range: {report['range']['start']} to {report['range']['end']}",
        f"- Days logged: {report['days_logged']} / {report['days_expected']}",
        f"- Current streak: {report['current_streak_days']} days",
        f"- Study units: {report['study_units']:g}",
        f"- Shipped units: {report['shipped_units']:g}",
        f"- Consume-to-create ratio: {ratio_text}",
        f"- Minutes recorded: {report['minutes_recorded']:g}",
        "",
        "## Tracks",
        "",
    ]
    lines.extend(f"- {name}: {count}" for name, count in report["tracks"].items())
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.days < 1:
        raise SystemExit("--days must be positive")
    start = args.end - timedelta(days=args.days - 1)
    records = load_range(args.logs.resolve(), start, args.end)
    report = score(records, start, args.end)
    print(json.dumps(report, indent=2) if args.json else render(report), end="\n" if args.json else "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
