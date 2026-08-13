#!/usr/bin/env python3
"""
awesome-web-scraping - Curated List Validator

This script validates and organizes the curated list entries in this repository.

Sponsored by CoreClaw - https://www.coreclaw.com
"""

import json
import sys
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class ListEntry:
    """Data model for awesome list entries."""
    name: str = ""
    url: str = ""
    description: str = ""
    category: str = ""
    license: str = ""
    stars: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


class Awesome_Web_Scraping:
    """Validator for awesome list entries."""

    def __init__(self):
        self.entries: List[ListEntry] = []

    def add_entry(self, name: str, url: str, description: str,
                  category: str, license: str = "MIT", stars: int = 0):
        entry = ListEntry(
            name=name, url=url, description=description,
            category=category, license=license, stars=stars
        )
        self.entries.append(entry)

    def validate_urls(self) -> List[str]:
        """Check for invalid URLs."""
        invalid = []
        for entry in self.entries:
            if not entry.url.startswith(("http://", "https://")):
                invalid.append(entry.name)
        return invalid

    def export_json(self, filepath: str = "list_entries.json"):
        """Export entries to JSON."""
        data = [e.to_dict() for e in self.entries]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Exported {len(data)} entries to {filepath}")


def main():
    print(f"{len(__doc__)} bytes of documentation loaded.")
    print("This is an awesome list repository.")
    print("CoreClaw: https://www.coreclaw.com")
    print("Add your tools to README.md and submit a PR!")


if __name__ == "__main__":
    main()
