#!/usr/bin/env python3
"""Calculate deterministic weekly execution metrics from plan-day logs."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logs", type=Path)
    parser.add_argument("--end", type=date.fromisoformat, default=date.today())
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def load_logs(root: Path, start: date, end: date) -> list[dict]:
    records: list[dict] = []
    cursor = start
    while cursor <= end:
        path = root / f"{cursor.isoformat()}.json"
        if path.exists():
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                raise SystemExit(f"Invalid JSON in {path}: {error}") from error
            record["_date"] = cursor.isoformat()
            records.append(record)
        cursor += timedelta(days=1)
    return records


def number(value: object) -> float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    return 0.0


def calculate(records: list[dict], start: date, end: date) -> dict:
    total = completed = rolled = 0
    planned_minutes = actual_minutes = 0.0
    by_type: dict[str, dict[str, float]] = defaultdict(
        lambda: {"tasks": 0, "completed": 0, "planned_min": 0, "actual_min": 0}
    )
    overcommit_days: list[str] = []
    for record in records:
        day_rollovers = 0
        tasks = record.get("tasks", [])
        if not isinstance(tasks, list):
            continue
        for task in tasks:
            total += 1
            done = bool(task.get("completed"))
            rollover = bool(task.get("rolled"))
            completed += done
            rolled += rollover
            day_rollovers += rollover
            planned = number(task.get("planned_min"))
            actual = number(task.get("actual_min"))
            planned_minutes += planned
            actual_minutes += actual
            kind = str(task.get("type", "unclassified")) or "unclassified"
            by_type[kind]["tasks"] += 1
            by_type[kind]["completed"] += done
            by_type[kind]["planned_min"] += planned
            by_type[kind]["actual_min"] += actual
        if day_rollovers >= 3:
            overcommit_days.append(record["_date"])
    return {
        "range": {"start": start.isoformat(), "end": end.isoformat()},
        "days_logged": len(records),
        "tasks": total,
        "completed": completed,
        "completion_rate": completed / total if total else None,
        "rollovers": rolled,
        "planned_minutes": planned_minutes,
        "actual_minutes": actual_minutes,
        "actual_to_planned_ratio": actual_minutes / planned_minutes if planned_minutes else None,
        "overcommit_days": overcommit_days,
        "by_type": dict(by_type),
    }


def fmt_ratio(value: object) -> str:
    return "n/a" if value is None else f"{float(value):.2f}"


def render(report: dict) -> str:
    lines = [
        "# Schedule Review",
        "",
        f"- Range: {report['range']['start']} to {report['range']['end']}",
        f"- Days logged: {report['days_logged']}",
        f"- Tasks completed: {report['completed']} / {report['tasks']}",
        f"- Completion rate: {fmt_ratio(report['completion_rate'])}",
        f"- Rollovers: {report['rollovers']}",
        f"- Planned minutes: {report['planned_minutes']:g}",
        f"- Actual minutes: {report['actual_minutes']:g}",
        f"- Actual/planned ratio: {fmt_ratio(report['actual_to_planned_ratio'])}",
        f"- Overcommit days: {', '.join(report['overcommit_days']) or 'none'}",
        "",
        "## By type",
        "",
    ]
    for kind, values in report["by_type"].items():
        lines.append(
            f"- {kind}: {int(values['completed'])}/{int(values['tasks'])} complete; "
            f"{values['actual_min']:g}/{values['planned_min']:g} min actual/planned"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.days < 1:
        raise SystemExit("--days must be positive")
    start = args.end - timedelta(days=args.days - 1)
    report = calculate(load_logs(args.logs.resolve(), start, args.end), start, args.end)
    print(json.dumps(report, indent=2) if args.json else render(report), end="\n" if args.json else "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
