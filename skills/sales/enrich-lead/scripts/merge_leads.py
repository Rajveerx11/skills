#!/usr/bin/env python3
"""Normalize and deduplicate CSV/JSON/JSONL lead enrichment exports."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ALIASES = {
    "input_id": ("input_id", "id", "lead_id", "record_id"),
    "name": ("name", "full_name", "contact_name", "person_name"),
    "title": ("title", "job_title", "headline", "position"),
    "company": ("company", "company_name", "organization", "organisation"),
    "domain": ("domain", "company_domain"),
    "company_url": ("company_url", "website", "company_website"),
    "linkedin_url": ("linkedin_url", "linkedin", "profile_url"),
    "email": ("email", "work_email", "business_email"),
    "phone": ("phone", "work_phone", "phone_number", "business_phone"),
    "location": ("location", "city", "company_location"),
    "industry": ("industry", "company_industry"),
    "employee_range": ("employee_range", "company_size", "employees"),
    "evidence": ("evidence", "notes", "source_note"),
    "sources": ("sources", "source", "source_url", "provenance"),
    "confidence": ("confidence",),
    "checked_at": ("checked_at", "retrieved_at", "updated_at"),
}

FIELDS = [
    "input_id",
    "name",
    "title",
    "company",
    "domain",
    "company_url",
    "linkedin_url",
    "email",
    "phone",
    "location",
    "industry",
    "employee_range",
    "evidence",
    "sources",
    "source_count",
    "confidence",
    "checked_at",
    "conflicts",
]


def clean(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return " ".join(str(value).strip().split())


def spreadsheet_safe(value: str) -> str:
    """Neutralize formula-leading cells only at the CSV output boundary."""
    return f"'{value}" if value and value[0] in "=+-@" else value


def read_records(path: Path) -> list[dict[str, object]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    if suffix in {".jsonl", ".ndjson"}:
        records: list[dict[str, object]] = []
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                value = json.loads(line)
                if isinstance(value, dict):
                    records.append(value)
        return records
    if suffix == ".json":
        value = json.loads(path.read_text(encoding="utf-8-sig"))
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
        if isinstance(value, dict):
            for key in ("items", "records", "results", "data"):
                nested = value.get(key)
                if isinstance(nested, list):
                    return [item for item in nested if isinstance(item, dict)]
                if isinstance(nested, dict) and isinstance(nested.get("items"), list):
                    return [item for item in nested["items"] if isinstance(item, dict)]
            return [value]
    raise ValueError(f"Unsupported input format: {path}")


def first(record: dict[str, object], aliases: tuple[str, ...]) -> str:
    lowered = {str(key).casefold(): value for key, value in record.items()}
    for alias in aliases:
        value = clean(lowered.get(alias.casefold()))
        if value:
            return value
    return ""


def domain_of(value: str) -> str:
    if not value:
        return ""
    candidate = value if "://" in value else f"https://{value}"
    host = urlsplit(candidate).hostname or ""
    return host.casefold().removeprefix("www.")


def normalized_url(value: str) -> str:
    if not value:
        return ""
    return value.split("?", 1)[0].rstrip("/").casefold()


def normalize(record: dict[str, object], source_file: Path, row_number: int) -> dict[str, str]:
    result = {field: first(record, aliases) for field, aliases in ALIASES.items()}
    if not result["domain"]:
        result["domain"] = domain_of(result["company_url"])
    else:
        result["domain"] = domain_of(result["domain"])
    sources = {f"file:{source_file.name}#row={row_number}"}
    for value in (result["sources"], result["company_url"], result["linkedin_url"]):
        for part in re.split(r"[|;,]\s*", value):
            if part:
                sources.add(part)
    result["sources"] = " | ".join(sorted(sources))
    result["conflicts"] = ""
    return result


def identity(record: dict[str, str], ordinal: int) -> str:
    if record["email"]:
        return f"email:{record['email'].casefold()}"
    if record["linkedin_url"]:
        return f"linkedin:{normalized_url(record['linkedin_url'])}"
    name = re.sub(r"\W+", "", record["name"].casefold())
    company = record["domain"] or re.sub(r"\W+", "", record["company"].casefold())
    if name and company:
        return f"person:{name}|{company}"
    if record["input_id"]:
        return f"id:{record['input_id'].casefold()}"
    return f"unmatched:{ordinal}"


def merge(existing: dict[str, str], incoming: dict[str, str]) -> None:
    conflicts = set(filter(None, existing.get("conflicts", "").split(" | ")))
    for field in FIELDS:
        if field in {"sources", "source_count", "confidence", "conflicts"}:
            continue
        new_value = incoming.get(field, "")
        old_value = existing.get(field, "")
        if not old_value and new_value:
            existing[field] = new_value
        elif old_value and new_value and old_value.casefold() != new_value.casefold():
            conflicts.add(f"{field}: {old_value} <> {new_value}")
    sources = set(filter(None, existing["sources"].split(" | ")))
    sources.update(filter(None, incoming["sources"].split(" | ")))
    existing["sources"] = " | ".join(sorted(sources))
    existing["conflicts"] = " | ".join(sorted(conflicts))


def finalize(record: dict[str, str]) -> dict[str, str]:
    sources = [item for item in record["sources"].split(" | ") if item]
    record["source_count"] = str(len(sources))
    supplied = record.get("confidence", "").strip().capitalize()
    if record["conflicts"]:
        record["confidence"] = "Low"
    elif supplied in {"High", "Medium", "Low"}:
        record["confidence"] = supplied
    elif len(sources) >= 3:
        record["confidence"] = "Medium"
    else:
        record["confidence"] = "Low"
    return {field: record.get(field, "") for field in FIELDS}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    merged: dict[str, dict[str, str]] = {}
    raw_count = 0
    for path in args.inputs:
        for row_number, raw in enumerate(read_records(path), start=2):
            raw_count += 1
            record = normalize(raw, path, row_number)
            key = identity(record, raw_count)
            if key in merged:
                merge(merged[key], record)
            else:
                merged[key] = record

    rows = [finalize(record) for record in merged.values()]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(
            {field: spreadsheet_safe(row.get(field, "")) for field in FIELDS}
            for row in rows
        )
    conflict_count = sum(bool(row["conflicts"]) for row in rows)
    print(
        f"raw={raw_count} unique={len(rows)} duplicates={raw_count - len(rows)} "
        f"conflicts={conflict_count} output={args.output.resolve()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
