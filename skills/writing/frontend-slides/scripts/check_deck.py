#!/usr/bin/env python3
"""Validate the structural contract of a standalone frontend-slides deck."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.slides: list[dict[str, object]] = []
        self._slide_depth = 0
        self._current: dict[str, object] | None = None
        self.main_deck = False
        self.nav = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "title":
            self._in_title = True
        if tag == "main" and "deck" in classes:
            self.main_deck = True
        if tag == "nav" and (values.get("aria-label") or "").lower().startswith("slide"):
            self.nav = True
        if tag == "section" and "slide" in classes:
            self._slide_depth = 1
            self._current = {
                "id": values.get("id") or "",
                "aria_hidden": values.get("aria-hidden"),
                "heading": False,
                "fragments": 0,
            }
            self.slides.append(self._current)
        elif self._slide_depth:
            self._slide_depth += 1
            if tag in {"h1", "h2"} and self._current is not None:
                self._current["heading"] = True
            if "data-fragment" in values and self._current is not None:
                self._current["fragments"] = int(self._current["fragments"]) + 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if self._slide_depth:
            self._slide_depth -= 1
            if self._slide_depth == 0:
                self._current = None

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def validate(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(text)
    errors: list[str] = []
    warnings: list[str] = []

    if not parser.title.strip():
        errors.append("missing non-empty <title>")
    if not parser.main_deck:
        errors.append('missing <main class="deck">')
    if not parser.slides:
        errors.append('no <section class="slide"> elements')
    if not parser.nav:
        errors.append("missing labeled slide navigation")

    ids = [str(slide["id"]) for slide in parser.slides]
    if any(not item for item in ids):
        errors.append("every slide needs a non-empty id")
    duplicates = sorted({item for item in ids if item and ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate slide ids: " + ", ".join(duplicates))

    for number, slide in enumerate(parser.slides, start=1):
        if not slide["heading"]:
            warnings.append(f"slide {number} ({slide['id'] or 'missing-id'}) has no h1/h2 claim")
        if slide["aria_hidden"] not in {"true", "false"}:
            errors.append(f"slide {number} ({slide['id'] or 'missing-id'}) needs aria-hidden")

    required_patterns = {
        "viewport metadata": r'name=["\']viewport["\']',
        "reduced-motion styles": r"prefers-reduced-motion",
        "print styles": r"@media\s+print",
        "keyboard navigation": r"addEventListener\(\s*[\"']keydown[\"']",
        "URL hash state": r"location\.hash",
        "live slide announcement": r"aria-live=[\"']polite[\"']",
    }
    for label, pattern in required_patterns.items():
        if not re.search(pattern, text, re.IGNORECASE):
            errors.append(f"missing {label}")

    remote_assets = re.findall(r'(?:src|href)=["\']https?://', text, re.IGNORECASE)
    if remote_assets:
        warnings.append(f"{len(remote_assets)} remote asset reference(s); offline playback needs fallbacks")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.deck.is_file():
        print(f"Deck not found: {args.deck}", file=sys.stderr)
        return 2
    try:
        errors, warnings = validate(args.deck)
    except (OSError, UnicodeError) as error:
        print(f"Unable to read deck: {error}", file=sys.stderr)
        return 2
    result = {
        "deck": str(args.deck.resolve()),
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARNING: {item}")
        print(f"Validated deck: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
