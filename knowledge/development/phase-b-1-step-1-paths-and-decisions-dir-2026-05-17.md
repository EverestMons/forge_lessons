# Phase B.1 Step 1 — Fix Stale Paths + Scaffold decisions/

**Date:** 2026-05-17
**Plan:** `executable-lessons-forge-extraction-phase-b1-cutover-2026-05-17`
**Step:** 1
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`

---

## (a) Stale Path Fixes in `src/lessons_forge.py`

Three surgical edits applied via Edit tool:

| Location | Before | After |
|---|---|---|
| Line 235 (docstring) | `Defaults to ["/Users/marklehn/Desktop/GitHub/PLANNER_TEMPLATE.md"]` | `Defaults to ["/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md"]` |
| Line 246 (runtime default) | `reference_files = ["/Users/marklehn/Desktop/GitHub/PLANNER_TEMPLATE.md"]` | `reference_files = ["/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md"]` |
| Line 328 (function signature) | `lessons_md_path: str = "/Users/marklehn/Desktop/GitHub/LESSONS.md"` | `lessons_md_path: str = "/Users/marklehn/Developer/GitHub/LESSONS.md"` |

All three edits change `/Desktop/GitHub/` to `/Developer/GitHub/` per the 2026-05-14 governance-root relocation.

---

## (b) Defensive Grep Sweep

```
$ grep -rn "/Desktop/GitHub/" . --exclude-dir=.git --exclude-dir=__pycache__ --exclude-dir=.pytest_cache
Binary file ./lessons-forge.db matches
```

One hit in `lessons-forge.db` (binary SQLite database, gitignored). This is historical row data in the database, not a runtime path or default argument. No source code hits remain. No action required.

---

## (c) Signature Smoke Test

```
$ python3 -c "from src.lessons_forge import parse_lessons_md, run_full_lessons_cycle, detect_duplicates; import inspect; print('parse_lessons_md:', inspect.signature(parse_lessons_md)); print('run_full_lessons_cycle:', inspect.signature(run_full_lessons_cycle)); print('detect_duplicates:', inspect.signature(detect_duplicates))"

parse_lessons_md: (path: 'str') -> 'list[dict]'
run_full_lessons_cycle: (conn: 'sqlite3.Connection', lessons_md_path: 'str' = '/Users/marklehn/Developer/GitHub/LESSONS.md') -> 'dict'
detect_duplicates: (conn: 'sqlite3.Connection', entry_ids: 'list[int]', reference_files: 'list[str] | None' = None) -> 'list[dict]'
```

`run_full_lessons_cycle` default now shows `/Users/marklehn/Developer/GitHub/LESSONS.md`. `detect_duplicates` shows `None` (runtime default is assigned inside the function body, confirmed fixed via grep sweep above).

---

## (d) Scaffold `knowledge/decisions/`

```
$ mkdir -p knowledge/decisions && touch knowledge/decisions/.gitkeep
$ ls -la knowledge/decisions/
total 0
drwxr-xr-x  4 marklehn  staff  128 May 15 19:31 .
drwxr-xr-x  6 marklehn  staff  192 May 15 16:58 ..
-rw-r--r--  1 marklehn  staff    0 May 15 19:31 .gitkeep
drwxr-xr-x  2 marklehn  staff   64 May 15 16:58 Done
```

Directory exists with `.gitkeep` and a pre-existing `Done/` subdirectory (created during Phase A).

---

## (e) Test Suite

```
$ python3 -m pytest src/ -q
.........................                                                [100%]
25 passed in 0.05s
```

25 passed, 0 failed. Matches expected count.

---

## Output Receipt

**Plan:** `executable-lessons-forge-extraction-phase-b1-cutover-2026-05-17`
**Step:** 1 of 5
**Status:** Complete — all substeps passed
**Files Created or Modified (Code):**
- `src/lessons_forge.py` — 3 path default edits (`/Desktop/GitHub/` → `/Developer/GitHub/`)
**Files Created or Modified (Non-Code):**
- `knowledge/decisions/.gitkeep` — new (scaffolding for Bellows watch target)
- `knowledge/development/phase-b-1-step-1-paths-and-decisions-dir-2026-05-17.md` — this file
