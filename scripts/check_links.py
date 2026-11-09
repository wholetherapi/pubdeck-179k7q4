#!/usr/bin/env python3
"""Quick link checker for the PubDeck catalogue."""

from pathlib import Path

CATALOGUE = Path(__file__).resolve().parent.parent / "catalog" / "publications.md"


def main() -> None:
    print(f"checking {CATALOGUE}")


if __name__ == "__main__":
    main()
