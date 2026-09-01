"""
Where the forge's inputs live on THIS machine — resolved, never recalled.

Two layouts exist (2026-09-01):
  shop  : ~/Developer/GitHub/{LESSONS.md, PLANNER_TEMPLATE.md, bellows/, forge/, lessons-forge/}
  mini  : ~/Developer/{eluvian-governance/{LESSONS.md, PLANNER_TEMPLATE.md}, bellows/, forge/, forge_lessons/}

Every default that used to be a shop-layout literal resolves through here.
Environment overrides win: ELUVIAN_WRAP_ROOT (governance root, the same
variable the wrap lock uses) and LESSONS_FORGE_DB (the database file).

The database is centralized on the Mac mini (CEO decision 2026-09-01) as
`<repo>/lessons-forge.db`, gitignored. A 0-byte file at any candidate path
is a decoy left by a misdirected sqlite3 call, never a database.
"""
from __future__ import annotations

import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def governance_root() -> Path | None:
    """The directory holding LESSONS.md and PLANNER_TEMPLATE.md."""
    env = os.environ.get("ELUVIAN_WRAP_ROOT")
    cands = ([Path(env)] if env else []) + [REPO.parent, REPO.parent / "eluvian-governance"]
    for c in cands:
        if (c / "LESSONS.md").is_file():
            return c
    return None


def lessons_md() -> Path | None:
    root = governance_root()
    return root / "LESSONS.md" if root else None


def planner_template() -> Path | None:
    root = governance_root()
    return root / "PLANNER_TEMPLATE.md" if root else None


def db_candidates() -> list[Path]:
    env = os.environ.get("LESSONS_FORGE_DB")
    return ([Path(env)] if env else []) + [REPO / "lessons-forge.db", REPO / "data" / "lessons-forge.db"]


def db_path() -> Path | None:
    """The live database: first candidate that exists and is non-empty."""
    for c in db_candidates():
        if c.is_file() and os.path.getsize(c) > 0:
            return c
    return None


def artifact_roots() -> list[Path]:
    """Directories a `target_artifact` basename may live under, on either layout."""
    root = governance_root()
    if root is None:
        return []
    roots = [root, root / "bellows", root / "forge", root.parent / "bellows", root.parent / "forge"]
    seen: list[Path] = []
    for r in roots:
        if r.is_dir() and r not in seen:
            seen.append(r)
    return seen
