#!/usr/bin/env python3
"""Normalize, deduplicate, and transparently score public place exports."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ALIASES = {
    "place_id": ("placeId", "place_id", "cid"),
    "name": ("title", "name", "placeName", "businessName"),
    "category": ("categoryName", "category", "primaryCategory"),
    "website": ("website", "companyWebsite", "businessWebsite"),
    "phone": ("phone", "phoneNumber", "telephone"),
    "email": ("email", "businessEmail"),
    "address": ("address", "street", "fullAddress"),
    "city": ("city",),
    "state": ("state", "region"),
    "country": ("country", "countryCode"),
    "rating": ("totalScore", "rating", "stars"),
    "reviews_count": ("reviewsCount", "reviewCount", "reviews"),
    "source_url": ("url", "googleMapsUrl", "placeUrl", "mapsUrl"),
}

FIELDS = [
    "place_id",
    "name",
    "category",
    "website",
    "domain",
    "phone",
    "email",
    "address",
    "city",
    "state",
    "country",
    "rating",
    "reviews_count",
    "source_url",
    "digital_opportunity_score",
    "score_evidence",
    "source_row",
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
        return [
            value
            for line in path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()
            for value in [json.loads(line)]
            if isinstance(value, dict)
        ]
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
    return (urlsplit(candidate).hostname or "").casefold().removeprefix("www.")


def as_float(value: str) -> float | None:
    try:
        return float(value.replace(",", "."))
    except (AttributeError, ValueError):
        return None


def as_int(value: str) -> int | None:
    try:
        return int(float(value.replace(",", "")))
    except (AttributeError, ValueError):
        return None


def normalize(raw: dict[str, object], row_number: int) -> dict[str, str]:
    record = {field: first(raw, aliases) for field, aliases in ALIASES.items()}
    record["domain"] = domain_of(record["website"])
    record["source_row"] = str(row_number)
    score = 0
    evidence: list[str] = []
    if not record["website"]:
        score += 30
        evidence.append("source has no business website")
    rating = as_float(record["rating"])
    reviews = as_int(record["reviews_count"])
    if rating is not None and reviews is not None and reviews >= 10 and rating < 4.2:
        score += 15
        evidence.append(f"rating {rating:g} across {reviews} reviews")
    elif reviews is not None and reviews < 10:
        score += 5
        evidence.append(f"only {reviews} public reviews")
    record["digital_opportunity_score"] = str(score)
    record["score_evidence"] = "; ".join(evidence) or "no scored observable gap"
    return record


def identity(record: dict[str, str], ordinal: int) -> str:
    if record["place_id"]:
        return f"place:{record['place_id'].casefold()}"
    if record["domain"]:
        return f"domain:{record['domain']}"
    digits = re.sub(r"\D+", "", record["phone"])
    if digits:
        return f"phone:{digits}"
    name = re.sub(r"\W+", "", record["name"].casefold())
    address = re.sub(r"\W+", "", record["address"].casefold())
    if name and address:
        return f"location:{name}|{address}"
    return f"unmatched:{ordinal}"


def richness(record: dict[str, str]) -> int:
    return sum(bool(record.get(field)) for field in FIELDS)


def merge(existing: dict[str, str], incoming: dict[str, str]) -> dict[str, str]:
    primary, secondary = (
        (incoming, existing) if richness(incoming) > richness(existing) else (existing, incoming)
    )
    result = dict(primary)
    for field in FIELDS:
        if not result.get(field) and secondary.get(field):
            result[field] = secondary[field]
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw_records = read_records(args.input)
    unique: dict[str, dict[str, str]] = {}
    for index, raw in enumerate(raw_records, start=2):
        record = normalize(raw, index)
        key = identity(record, index)
        unique[key] = merge(unique[key], record) if key in unique else record

    rows = sorted(
        unique.values(),
        key=lambda row: (-int(row["digital_opportunity_score"]), row["name"].casefold()),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(
            {field: spreadsheet_safe(row.get(field, "")) for field in FIELDS}
            for row in rows
        )
    print(
        f"raw={len(raw_records)} unique={len(rows)} "
        f"duplicates={len(raw_records) - len(rows)} output={args.output.resolve()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
