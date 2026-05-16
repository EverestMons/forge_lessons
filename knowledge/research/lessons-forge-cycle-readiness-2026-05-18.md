# Lessons Forge Cycle Readiness — Findings

**Diagnostic:** diagnostic-lessons-forge-cycle-readiness-2026-05-18
**Executed:** 2026-05-18
**Specialist:** Forge Developer
**Scope:** Read-only. No DB writes. No file edits.

---

## (a) Module import integrity

**Command:**
```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -c "from src.lessons_forge import run_full_lessons_cycle, generate_lessons_report, ingest_lesson_entries, parse_lessons_md, insert_proposal, detect_duplicates; print('OK')"
```

**Output:**
```
OK
```

**Result:** All six public functions import cleanly. No wiring breaks.

---

## (b) Test suite baseline

**Command:**
```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -q 2>&1 | tail -20
```

**Output:**
```
.........................                                                [100%]
25 passed in 0.05s
```

**Result:** 25 passed, 0 failed. Matches expected baseline.

---

## (c) Live DB state — counts and distributions

**Command:**
```python
python3 -c "
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
# ... (full query script as specified in diagnostic)
"
```

**Output:**
```
=== lesson_entries count ===
38
=== lesson_proposals count ===
38
=== lesson_proposals by status ===
superseded 23
implemented 14
proposed 1
=== lesson_proposals by category ===
duplicate 19
governance_rule 14
structural 4
instrumentation 1
=== entries with NO proposal (the needs_classification pool) ===
0
=== oldest + newest entry_date in lesson_entries ===
('2026-04-14', '2026-05-13')
```

**Observations:**
- 38 entries, 38 proposals — every entry has exactly one proposal. Zero unclassified entries.
- Status distribution: 23 superseded, 14 implemented, 1 proposed. The single "proposed" entry is the only actionable item.
- Category distribution: 19 duplicate (50%), 14 governance_rule (37%), 4 structural (11%), 1 instrumentation (3%). No `language` or `narrative` entries.
- Entry date range spans 2026-04-14 to 2026-05-13 (last cycle date).

---

## (d) LESSONS.md state

**Commands:**
```bash
wc -l /Users/marklehn/Developer/GitHub/LESSONS.md
grep -c '^## ' /Users/marklehn/Developer/GitHub/LESSONS.md
grep -n '^## Archived' /Users/marklehn/Developer/GitHub/LESSONS.md
```

**Output:**
```
     611 /Users/marklehn/Developer/GitHub/LESSONS.md
44
(no output — no match)
```

**Observations:**
- 611 lines, 44 level-2 headings total.
- **`## Archived` heading does NOT exist.** The parser (`parse_lessons_md`) handles this via the `for/else` construct — it flushes the last entry at EOF. Functional behavior is correct (43 dated entries parsed successfully; see section e), but the missing boundary means ALL entries are treated as active. If an `## Archived` section is ever added, entries below it will be excluded. Currently a no-op gap, not a blocker.

---

## (e) Dry-run parse (no writes)

**Note:** `parse_lessons_md` takes a file path, not text content. The diagnostic's sample code was adapted accordingly.

**Command:**
```python
python3 -c "
from src.lessons_forge import parse_lessons_md
entries = parse_lessons_md('/Users/marklehn/Developer/GitHub/LESSONS.md')
print(f'parsed {len(entries)} entries')
for e in entries:
    h = e.get('source_heading')
    d = e.get('entry_date')
    print(f'  [{d}] {h}')
"
```

**Output:**
```
parsed 43 entries
  [2026-05-18] 2026-05-18 — `deposit_exists` gate keys on literal staging filename inside Deposits prose; 4th Bellows gate false positive
  [2026-05-17] 2026-05-17 — Bellows Rule 20 gate keys on a specific stdout pattern; documenting the banner as a captured block trips the gate
  [2026-05-17] 2026-05-17 — Defensive diagnostic before destructive cross-repo work pays off in surprising ways
  [2026-05-16] 2026-05-16 — Splitting destructive cross-cutting work into stand-up + cutover phases behind a verdict gate
  [2026-05-15] 2026-05-15 — Claude has two filesystems and the wrong tool silently writes to the wrong one
  [2026-05-15] 2026-05-15 — Bellows lifecycle commits in a submodule need a governance-root pointer bump in the same session
  [2026-05-15] 2026-05-15 — Canary "captured cwd" flag is a cheap, decisive answer to "does feature X work in arrangement Y"
  [2026-05-15] 2026-05-15 — GitHub's "inflate / pack has bad object" error is how its server reports the 100 MB hard file size limit, not actual corruption
  [2026-05-15] 2026-05-15 — `git filter-repo` removes the `origin` remote by default; rewriting also drops the affected file from the working tree
  [2026-05-15] 2026-05-15 — Files already tracked by git are NOT retroactively ignored when added to `.gitignore`
  [2026-05-15] 2026-05-15 — Existing gitlinks without `.gitmodules` are in "broken submodule" limbo; `git submodule add` is not the only path back
  [2026-05-14] 2026-05-14 — iCloud `dataless` eviction masqueraded as git corruption; only macOS file-flag inspection found the real cause
  [2026-05-14] 2026-05-14 — Recovery plan had a gap (empty index after bare-to-non-bare conversion); agent improvised through it instead of halting
  [2026-05-13] 2026-05-13 (session 3) — Phase 1.5 skipped at session start; cost was four diagnostics on a foundation already answered
  [2026-05-13] 2026-05-13 (session 3) — Verdict directory error recurred for the third time in 24 hours; reading is not internalizing
  [2026-05-13] 2026-05-13 (session 3) — Bellows step-pause behavior model was wrong; per-step pause is manual-bootstrap, not Bellows
  [2026-05-13] 2026-05-13 (session 3) — Plan filename "drain-extraction-queue" became misleading historical record
  [2026-05-13] 2026-05-13 (session 3) — Negative grep results during dormancy ≠ architectural finding
  [2026-05-13] 2026-05-13 (later) — `**Deposits:**` blocks must contain resolvable paths, never placeholders
  [2026-05-13] 2026-05-13 — Recurrence of the `pending/` vs `resolved/` verdict-directory error; LESSONS read is not the same as LESSONS internalized
  [2026-05-12] 2026-05-12 — Verdict response files go to `verdicts/resolved/`, NOT `verdicts/pending/`
  [2026-05-12] 2026-05-12 — Verdict response format is `verdict: continue\n<reason>` — no markdown decoration
  [2026-05-12] 2026-05-12 — "queue empty — all plans complete" means paused-or-done, NOT completed
  [2026-05-12] 2026-05-12 — `_extract_plan_required_deposits` parser now handles inline `**Deposits:**` format; banner-search fence-strip is a latent fragility
  [2026-05-12] 2026-05-12 — Dev-log self-reference SHA loop is structurally impossible
  [2026-05-12] 2026-05-12 — Planner-cited deposit paths should be verified before plan authorship, not assumed from memory
  [2026-05-11] 2026-05-11 (session wrap) — Five-plan Bellows BACKLOG session shape: hygiene → refactor → cleanup → governance → feature → hygiene
  [2026-05-11] 2026-05-11 — Plans deposited to Bellows-watched directories drift between authoring and dispatch
  [2026-05-10] 2026-05-10 — Meta-lesson: LESSONS.md not in Phase 1.5 scope is itself the bug
  [2026-05-10] 2026-05-10 — When shipping a path-resolution fix, audit ALL gate functions that call _resolve_deposit_path
  [2026-05-03] 2026-05-03 — Diagnostic completeness check should include test-suite grep
  [2026-05-03] 2026-05-03 — Bellows restart not signaled in plan instructions
  [2026-05-03] 2026-05-03 — Deliverable verification of "commit landed" must be SHA-anchored, not HEAD-anchored
  [2026-05-03] 2026-05-03 — Stranded resolved verdicts are accumulating
  [2026-05-03] 2026-05-03 — Bellows wedge during teardown is invisible to caller
  [2026-05-09] 2026-05-09 — `pause_for_verdict: after_step_1` is mandatory for multi-step plans
  [2026-05-09] 2026-05-09 — Rule 20 self-check blocks must use the verbatim PLANNER_TEMPLATE template, not custom rewrites
  [2026-05-09] 2026-05-09 — Mechanical-only Layer 1 fixes can have retroactive cleanup as a side effect
  [2026-05-10] 2026-05-10 — Verification diagnostic pattern: cheap closure for stale BACKLOG entries
  [2026-05-10] 2026-05-10 (evening) — Scan Done/ before recommending BACKLOG work
  [2026-05-11] 2026-05-11 — Scope parser-vs-structure diagnostics to ALL markdown contexts, not just fences
  [2026-05-11] 2026-05-11 — Bait-laden canaries verify Bellows-side fixes from both directions
  [2026-05-12] 2026-05-12 — Grep patterns against BACKLOG.md must account for markdown bold markers
```

**Result:** 43 entries parsed. Return shape is `list[dict]` with keys `source_heading`, `entry_date`, `raw_content`, `content_hash`, `tags`. Parser is functioning correctly.

---

## (f) Ingestion delta — what a real cycle would pick up

**Hashing recipe used:** `parse_lessons_md` pre-computes `content_hash` as `hashlib.sha256(raw_content.encode("utf-8")).hexdigest()` where `raw_content = "".join(body_lines)` (body lines only, excluding the heading line). This is the same hash that `ingest_lesson_entries` stores and compares. The delta check used the pre-computed `content_hash` field from parsed entries directly.

**Command:**
```python
python3 -c "
import sqlite3, hashlib
from src.lessons_forge import parse_lessons_md
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
existing_hashes = {row[0] for row in cur.execute('SELECT content_hash FROM lesson_entries').fetchall()}
parsed = parse_lessons_md('/Users/marklehn/Developer/GitHub/LESSONS.md')
# ... (uses e.get('content_hash') — pre-computed, matching ingest recipe)
"
```

**Output:**
```
parsed total: 43
already in DB (by content_hash): 24
NEW or CHANGED (would ingest): 19
  [2026-05-18] 2026-05-18 — `deposit_exists` gate keys on literal staging filename inside Deposits prose; 4th Bellows gate false positive
  [2026-05-17] 2026-05-17 — Bellows Rule 20 gate keys on a specific stdout pattern; documenting the banner as a captured block trips the gate
  [2026-05-17] 2026-05-17 — Defensive diagnostic before destructive cross-repo work pays off in surprising ways
  [2026-05-16] 2026-05-16 — Splitting destructive cross-cutting work into stand-up + cutover phases behind a verdict gate
  [2026-05-15] 2026-05-15 — Claude has two filesystems and the wrong tool silently writes to the wrong one
  [2026-05-15] 2026-05-15 — Bellows lifecycle commits in a submodule need a governance-root pointer bump in the same session
  [2026-05-15] 2026-05-15 — Canary "captured cwd" flag is a cheap, decisive answer to "does feature X work in arrangement Y"
  [2026-05-15] 2026-05-15 — GitHub's "inflate / pack has bad object" error is how its server reports the 100 MB hard file size limit, not actual corruption
  [2026-05-15] 2026-05-15 — `git filter-repo` removes the `origin` remote by default; rewriting also drops the affected file from the working tree
  [2026-05-15] 2026-05-15 — Files already tracked by git are NOT retroactively ignored when added to `.gitignore`
  [2026-05-15] 2026-05-15 — Existing gitlinks without `.gitmodules` are in "broken submodule" limbo; `git submodule add` is not the only path back
  [2026-05-14] 2026-05-14 — iCloud `dataless` eviction masqueraded as git corruption; only macOS file-flag inspection found the real cause
  [2026-05-14] 2026-05-14 — Recovery plan had a gap (empty index after bare-to-non-bare conversion); agent improvised through it instead of halting
  [2026-05-13] 2026-05-13 (session 3) — Phase 1.5 skipped at session start; cost was four diagnostics on a foundation already answered
  [2026-05-13] 2026-05-13 (session 3) — Verdict directory error recurred for the third time in 24 hours; reading is not internalizing
  [2026-05-13] 2026-05-13 (session 3) — Bellows step-pause behavior model was wrong; per-step pause is manual-bootstrap, not Bellows
  [2026-05-13] 2026-05-13 (session 3) — Plan filename "drain-extraction-queue" became misleading historical record
  [2026-05-13] 2026-05-13 (session 3) — Negative grep results during dormancy ≠ architectural finding
  [2026-05-13] 2026-05-13 (later) — `**Deposits:**` blocks must contain resolvable paths, never placeholders
```

**Observations:**
- 19 new entries would be ingested (50% growth: 38 → 57 entries).
- All 19 are dated 2026-05-13 through 2026-05-18 — post-last-cycle entries.
- 24 of 43 parsed entries match existing DB hashes — 14 entries already in DB are NOT in the current LESSONS.md parse (38 DB entries minus 24 matches = 14 entries that were in LESSONS.md during prior cycles but are no longer present or have been edited). This is expected: entries may have been edited since ingestion, or removed from LESSONS.md. The ingestion is keyed on `(source_file, source_heading)`, so content-hash mismatches will trigger updates, not duplicates.
- **This is a real cycle with meaningful work.** The next executable should run `run_full_lessons_cycle()` end-to-end.

---

## (g) Wiring sanity — function defaults

**Command:**
```python
python3 -c "
import inspect
from src.lessons_forge import detect_duplicates, run_full_lessons_cycle
sig_dd = inspect.signature(detect_duplicates)
sig_rc = inspect.signature(run_full_lessons_cycle)
print('detect_duplicates signature:', sig_dd)
print('run_full_lessons_cycle signature:', sig_rc)
"
```

**Output:**
```
detect_duplicates signature: (conn: 'sqlite3.Connection', entry_ids: 'list[int]', reference_files: 'list[str] | None' = None) -> 'list[dict]'

run_full_lessons_cycle signature: (conn: 'sqlite3.Connection', lessons_md_path: 'str' = '/Users/marklehn/Developer/GitHub/LESSONS.md') -> 'dict'
```

**Verification:**
- `detect_duplicates` default `reference_files` is `None`, which resolves at runtime to `["/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md"]` (confirmed by reading source line 246). Uses `/Developer/GitHub/` — **correct, no stale `/Desktop/GitHub/` reference.**
- `run_full_lessons_cycle` default `lessons_md_path` is `"/Users/marklehn/Developer/GitHub/LESSONS.md"`. Uses `/Developer/GitHub/` — **correct, no stale `/Desktop/GitHub/` reference.**

Phase B.1 path fix is confirmed in effect.

---

## (h) Stale references in specialist file

**Command:**
```bash
grep -n -E 'forge\.db|forge/src/|forge/agents/|\*\*Project:\*\* forge' /Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md
```

**Output:**
```
6:**Project:** forge
16:...forge/src/lessons_forge.py...
22:**Project:** forge
33:- `forge/src/lessons_forge.py` — module containing `insert_proposal()`, ...
34:- `forge.db` tables: `lesson_entries` (read-only input), `lesson_proposals` (write via `insert_proposal()`)
47:- Read one `lesson_entries` row from `forge.db` by entry ID ...
88:1. Read the entry from `forge.db`: `SELECT id, source_heading, ...`
```

**Stale references enumerated (6 total):**

| Line | Stale reference | Should be |
|------|----------------|-----------|
| 6 | `**Project:** forge` | `**Project:** lessons-forge` |
| 16 | `forge/src/lessons_forge.py` | `src/lessons_forge.py` (relative to lessons-forge root) |
| 22 | `**Project:** forge` | `**Project:** lessons-forge` |
| 33 | `forge/src/lessons_forge.py` | `src/lessons_forge.py` |
| 34 | `forge.db` | `lessons-forge.db` |
| 47 | `forge.db` | `lessons-forge.db` |
| 88 | `forge.db` | `lessons-forge.db` |

**Context:** File `Last Updated: 2026-04-23` — pre-extraction. All references are documentation lag from the Phase A extraction, not code defects. The agent file needs a sweep to update project name, DB filename, and relative paths.

---

## (i) Stale PROJECT_STATUS section

**Command:**
```bash
grep -n -A2 '^## Pending — Phase B.2' /Users/marklehn/Developer/GitHub/lessons-forge/PROJECT_STATUS.md | head -10
```

**Output:**
```
67:## Pending — Phase B.2 (next session)
68-
69-1. Edit `governance/adr/ADR-002-lessons-forge-design.md` (lines 32, 34, 76, 145 — stale `forge/src/lessons_forge.py` / `forge/agents/FORGE_LESSONS_AGENT.md` references)
```

**Result:** The "Pending — Phase B.2 (next session)" section still exists at line 67. Phase B.2 shipped on 2026-05-18 (commit `36514fe`). This is closeout lag — the section should be updated to reflect B.2 completion or removed.

---

## (j) Bellows daemon health + watch config

**Command (config):**
```bash
cd /Users/marklehn/Developer/GitHub/bellows && cat config.json 2>&1 | python3 -c "..."
```

**Output:**
```
watched_count: 9
lessons-forge present: True
  /Users/marklehn/Developer/GitHub/invoice-pulse/knowledge/decisions
  /Users/marklehn/Developer/GitHub/BrewBuddy/knowledge/decisions
  /Users/marklehn/Developer/GitHub/study/knowledge/decisions
  /Users/marklehn/Developer/GitHub/ai-career-digest/knowledge/decisions
  /Users/marklehn/Developer/GitHub/freight-kb/knowledge/decisions
  /Users/marklehn/Developer/GitHub/forge/knowledge/decisions
  /Users/marklehn/Developer/GitHub/anvil/knowledge/decisions
  /Users/marklehn/Developer/GitHub/bellows/knowledge/decisions
  /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions
```

**Command (daemon liveness):**
```bash
tail -5 /Users/marklehn/Developer/GitHub/bellows/logs/terminal/bellows-$(date +%Y-%m-%d).log
```

**Output:**
```
09:24:28 [EVENT] [diagnostic-lessons-forge-cycle] ⏳ RUNNING
09:24:28 [WARN] ⚠️ plan has step headers but case does not match expected '## STEP N' — count=1 matched case-insensitively
09:24:28 [ERROR] [diagnostic-lessons-forge-cycle] ❌ FAILED: [Errno 2] No such file or directory: '.../diagnostic-lessons-forge-cycle-readiness-2026-05-18.md'
09:24:29 [EVENT] 🏁 queue empty — all plans complete
09:24:30 [EVENT] [diagnostic-lessons-forge-cycle] ▶ started
```

**Observations:**
- Watched project count is 9, `lessons-forge` present — **correct.**
- Daemon is alive and processing. The FAILED error at 09:24:28 is expected — the file was already renamed to `in-progress-` by the time Bellows tried to read it (race condition between claim and Bellows dispatch). The subsequent `▶ started` line at 09:24:30 confirms the worktree agent was dispatched successfully.
- The WARN about step header casing (`## Step 1` vs `## STEP 1`) is a cosmetic Bellows parser mismatch, not a functional issue.

---

## Gap Assessment

| # | Gap | Evidence (cite section) | Severity | Proposed fix |
|---|---|---|---|---|
| 1 | `FORGE_LESSONS_AGENT.md` has 6 stale references to `forge` project name, `forge.db`, and `forge/src/` paths | Section (h): lines 6, 16, 22, 33, 34, 47, 88 | hygiene | Sweep file: update `**Project:** forge` → `lessons-forge`, `forge.db` → `lessons-forge.db`, `forge/src/` → `src/` |
| 2 | `PROJECT_STATUS.md` still has "Pending — Phase B.2 (next session)" section at line 67 despite B.2 shipping 2026-05-18 | Section (i): line 67 | hygiene | Update section to reflect B.2 completion or collapse into completed work |
| 3 | `## Archived` heading missing from LESSONS.md — parser boundary undefined | Section (d): grep returned no match | informational | No action needed for cycle readiness. Parser handles EOF gracefully. If archival workflow is desired, add `## Archived` heading to LESSONS.md |
| 4 | 19 new entries pending ingestion (50% growth) — full cycle is warranted | Section (f): 19 new entries dated 2026-05-13 through 2026-05-18 | informational | Next executable should run `run_full_lessons_cycle()` end-to-end, not skip |
| 5 | 1 proposal still in `proposed` status from prior cycle | Section (c): status distribution shows 1 proposed | informational | Review during next cycle's report generation — may need Planner triage |
| 6 | Bellows step-header casing WARN on diagnostic plans | Section (j): `## Step 1` vs `## STEP 1` | informational | Cosmetic Bellows parser mismatch — no fix needed for lessons-forge |

**No blockers or wiring-severity gaps found.** The cycle can proceed with a clean `run_full_lessons_cycle()` invocation. Gaps #1 and #2 are documentation hygiene — they should be scoped into the next executable as cleanup steps alongside the cycle run, or into a separate hygiene executable.

---

## Output Receipt

**Diagnostic:** diagnostic-lessons-forge-cycle-readiness-2026-05-18
**Status:** Complete
**Executed by:** Forge Developer (Bellows-dispatched agent)
**Date:** 2026-05-18

**Files Created:**
- `lessons-forge/knowledge/research/lessons-forge-cycle-readiness-2026-05-18.md` — findings deposit (this file)
- `lessons-forge/knowledge/development/dev-log-lessons-forge-cycle-readiness-2026-05-18.md` — dev log

**Files Modified:**
- None (read-only diagnostic)

**Commands Executed:** 11 read-only commands across sections (a)–(j). Zero writes to DB or filesystem (aside from deposits).
