# PubDeck

PubDeck is my personal publication catalogue. It tracks accepted papers, their
venues, preprint links, and the public code release for each paper.

## Repository layout

- `catalog/publications.md` — the canonical publication checklist
- `catalog/conventions.md` — editorial conventions for catalogue entries
- `scripts/check_links.py` — link sanity checker
- `archive/` — frozen snapshots of earlier catalogue releases
- `assets/` — branding and badges

## Branches

`main` is the working catalogue. Release branches (for example `release-2026.11`)
are cut from `main` for each catalogue publication window and are the branches
used when preparing a release.
