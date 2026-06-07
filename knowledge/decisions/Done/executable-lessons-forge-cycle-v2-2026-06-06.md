# Executable — Lessons Forge Cycle v2 (2026-06-06)

**Plan slug:** executable-lessons-forge-cycle-v2-2026-06-06
**Plan type:** executable
**Project:** lessons-forge
**Specialist:** Forge Developer (Steps 1, 3, 4) + Forge Lessons Agent (Step 2). QA role in Step 4 uses Forge Developer (FORGE_QA not yet authored — carry-forward).
**Auto-close:** false
**Pause for verdict:** always
**Dispatch Mode:** bellows
**Priority:** 1
**Depends on:** none
**Created:** 2026-06-06
**qa_steps:** 4

---

## Context

Re-dispatch after the first 2026-06-06 cycle was halted at Step 1. Root cause: the DB-authoritative work-list query used by every cycle plan — `entries WHERE NOT EXISTS (any proposal)` — drops entries whose only proposal is `stale`. The ingestion update path marks an edited entry's prior proposal `stale` (the row persists) and requeues the entry for classification; the `any proposal` query never sees it. This silently dropped entry 93 (a high-confidence schema-migration `governance_rule` lesson, staled by a prior edit) across multiple cycles, and would have dropped entry 116 (the 05-29 straggler, re-staled by the first dispatch's `updated_count=1`) this cycle.

The buggy query is prescribed verbatim by entry 117's codified discipline rule (the over-reporting fix shipped this undercount) and is in this very batch awaiting classification. This plan fixes it at the source — a stale-aware helper `get_unclassified_entries(conn)` in `lessons_forge.py` — so future cycles call the helper instead of copying SQL, and entry 117's eventual codification references the helper rather than enshrining the wrong query.

The first dispatch's Step 1 ingest already landed (entries 117-123 inserted, 116 re-staled). `run_full_lessons_cycle()` is idempotent, so Step 1 here re-runs it as a no-op ingest and the work list is unchanged.

**Correct work list this cycle (9 entries): [93, 116, 117, 118, 119, 120, 121, 122, 123].**

**`needs_classification` over-reporting (unchanged):** the result dict's `needs_classification` lists every parsed entry (~66). Never loop it. The new helper is the sole source of the work list.

## Scope

In-scope:
- Add `get_unclassified_entries(conn)` to `src/lessons_forge.py` (stale-aware work-list query) + a unit test in `src/test_lessons_forge.py`.
- `run_full_lessons_cycle()` re-run (idempotent), classification of the helper's work list via `insert_proposal()`, `generate_lessons_report()`, QA (full suite + DB invariants + schema drift + Rule 20).

Out-of-scope (separate sessions): CEO Gate 1 disposition; Gate 2 governance edits to PLANNER_TEMPLATE (including correcting entry 117's prescribed query — that happens when 117 is codified); refactoring `run_full_lessons_cycle`'s `needs_classification` return shape (deeper change, file as BACKLOG); FORGE_LESSONS_AGENT.md stale `forge/`-path hygiene.

## Execution Map

`Step 1 (Forge Developer) -> [verdict] -> Step 2 (Forge Lessons Agent) -> [verdict] -> Step 3 (Forge Developer) -> [verdict] -> Step 4 (Forge Developer / QA) -> [verdict]`

---

## STEP 1 — Forge Developer

**Role:** Developer
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — specialist file (cross-repo).
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — placement context (`insert_proposal` at L155, `run_full_lessons_cycle` at L327) and return shape.
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/test_lessons_forge.py` — test style + the existing `test_ingest_stale_proposals` (the stale path this helper must respect).
- Skip the domain glossary (Rule 16 — mechanical).

**Task — two parts. Part A is a code fix; Part B runs the cycle.**

**Part A — add the stale-aware work-list helper.**

Add this function to `src/lessons_forge.py` (place it directly after `insert_proposal`, before `detect_duplicates`):

```python
def get_unclassified_entries(conn: sqlite3.Connection) -> list[int]:
    """Return entry IDs that need (re)classification this cycle.

    An entry needs classification if it has NO proposal whose status is
    anything other than 'stale'. This includes (a) entries with no proposal
    at all and (b) entries whose only proposal(s) are 'stale' — the state the
    ingestion update path leaves an edited entry in (old proposal staled, entry
    requeued). Entries with a 'proposed'/'accepted'/'implemented'/'rejected'/
    'superseded' proposal are excluded (active or dispositioned).

    This is the canonical work list. Do NOT derive a work list from
    run_full_lessons_cycle().needs_classification — it over-reports every
    parsed entry. Do NOT use `NOT EXISTS (any proposal)` — it drops stale-only
    entries and silently skips re-queued edits.
    """
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT e.id FROM lesson_entries e "
        "WHERE NOT EXISTS ("
        "  SELECT 1 FROM lesson_proposals p "
        "  WHERE p.entry_id = e.id AND p.status != 'stale'"
        ") ORDER BY e.id"
    ).fetchall()
    return [r[0] for r in rows]
```

Add `get_unclassified_entries` to the test file's import from `src.lessons_forge`, and add a unit test that builds a temp DB with: one entry with no proposal, one entry whose only proposal is `stale`, and one entry with an `implemented` proposal — asserting the helper returns exactly the first two IDs (stale-only IS included; implemented is NOT). Mirror the tempfile/`db.init_db` pattern used by `test_ingest_stale_proposals`.

Run the FULL suite (no `-k`, no early exit):

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v 2>&1 | tail -45
```

Expected: 26 passed (25 prior + 1 new), 0 failed. Any failure -> flag and halt the step.

**Part B — run the cycle and derive the authoritative work list via the helper.**

```python
python3 << 'PY'
import sqlite3, json
from src.lessons_forge import run_full_lessons_cycle, get_unclassified_entries

conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
result = run_full_lessons_cycle(conn)        # idempotent — expect 0 ingested / 0 updated
conn.commit()
worklist = get_unclassified_entries(conn)    # authoritative work list
conn.close()

with open('/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/cycle-result-v2-2026-06-06.json', 'w') as f:
    json.dump({"cycle_result": result, "worklist": worklist}, f, indent=2, default=str)

print('ingested:', result['ingested_count'], 'updated:', result['updated_count'])
print('WORKLIST (', len(worklist), '):', worklist)
PY
```

Expected: `WORKLIST` is exactly `[93, 116, 117, 118, 119, 120, 121, 122, 123]` (9 entries). If the list differs, halt and flag — do not proceed to classification with a divergent work list.

**Deposits:**
- `knowledge/development/cycle-result-v2-2026-06-06.json` — `{cycle_result, worklist}` (Step 2 input)
- `knowledge/development/dev-log-cycle-v2-step-1-2026-06-06.md` — helper diff, full pytest summary line, Part B stdout

**Output Receipt fields required:**
- What was done
- Files deposited
- Test result (X passed / Y failed) + the authoritative worklist
- Flags for CEO
- Flags for Next Step

---

## STEP 2 — Forge Lessons Agent

**Role:** Lessons Agent
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md` — ADR-002 six-value taxonomy.
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — `insert_proposal()` and `get_unclassified_entries()` signatures.
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/cycle-result-v2-2026-06-06.json` — confirm Step 1 worklist; cross-check only.

**Task:**

Derive the authoritative work list by calling the helper directly (do not trust a copied list, and never loop `needs_classification`):

```python
python3 << 'PY'
import sqlite3
from src.lessons_forge import get_unclassified_entries
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
print('to classify:', get_unclassified_entries(conn))
conn.close()
PY
```

Expected: `[93, 116, 117, 118, 119, 120, 121, 122, 123]`. Classify exactly these. For each ID:
1. Read it: `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id = ?`
2. Apply the ADR-002 taxonomy.
3. Produce the classification object (`entry_id`, `category`, `confidence`, `suggested_action`, `reasoning`, `target_layer`, optional `target_artifact`, `subcategory`).
4. `insert_proposal(conn, **classification)`.

**Note on 93 and 116:** both already carry a prior `stale` proposal (staled by content edits). Do NOT attempt to mutate the stale row — `insert_proposal()` writes a fresh proposal; the stale one remains as history. This is correct.

Per-entry `reasoning` MUST cite specific text from the entry's `raw_content`. Do NOT assign `category='duplicate'`. Use `status='ambiguous'` only if an entry fits no category — do not invent taxonomy values.

**Flag explicitly in the synthesis:** entry 117's content prescribes the buggy `NOT EXISTS (any proposal)` work-list query. Whatever category you assign, note in its `reasoning` that the prescribed query needs the stale-aware correction (now implemented as `get_unclassified_entries`) when this lesson is codified — so Gate 2 does not enshrine the bug. Also call out any governance_rule cluster across the 06-06 batch (119-123 are tagged planner-discipline / bellows-architecture / qa-discipline).

**Deposits:**
- `knowledge/development/classifications-summary-v2-2026-06-06.md` — distribution + cross-batch synthesis for CEO Gate 1
- `knowledge/development/dev-log-cycle-v2-step-2-2026-06-06.md` — dev log

DB writes via `insert_proposal()` are tracked by row counts, not as file deposits.

**Output Receipt fields required:**
- What was done
- Files deposited
- Total classified (expect 9) + category/confidence distribution
- Flags for CEO (117 query-correction note, ambiguous entries, cluster signals)
- Flags for Next Step

---

## STEP 3 — Forge Developer

**Role:** Developer
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — `generate_lessons_report()` signature.
- `knowledge/development/classifications-summary-v2-2026-06-06.md` — confirm Step 2 receipt Complete before running.

**Task:**

```python
python3 << 'PY'
import os, sqlite3
from src.lessons_forge import generate_lessons_report
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
report = generate_lessons_report(conn)
conn.close()
os.makedirs('/Users/marklehn/Developer/GitHub/lessons-forge/reports/', exist_ok=True)
with open('/Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-06-06.md', 'w') as f:
    f.write(report)
print('Report written. Length:', len(report), 'chars')
for line in report.splitlines()[:80]:
    print(line)
PY
```

**Deposits:**
- `reports/lessons-report-2026-06-06.md` — full cycle report for CEO Gate 1 review
- `knowledge/development/dev-log-cycle-v2-step-3-2026-06-06.md` — dev log

**Output Receipt fields required:**
- What was done
- Files deposited
- Report length + proposal count surfaced
- Flags for CEO
- Flags for Next Step

---

## STEP 4 — Forge Developer (QA)

**Role:** QA (Forge Developer acting as QA — FORGE_QA not yet authored)
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `reports/lessons-report-2026-06-06.md` — confirm Step 3 receipt Complete.
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/db.py` — canonical schema for the drift check.

**Task — four checks:**

(a) Test regression — FULL suite (no `-k`, no early exit):

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v 2>&1 | tail -45
```

Expected: 26 passed, 0 failed. Report the literal summary line. Any failure -> flag and halt.

(b) DB invariants (note: the orphan check is the stale-aware helper, not `NOT EXISTS any proposal`):

```python
python3 << 'PY'
import sqlite3
from src.lessons_forge import get_unclassified_entries
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
print('unclassified after cycle (should be 0):', get_unclassified_entries(conn))
print('dangling proposals (should be 0):', cur.execute('SELECT COUNT(*) FROM lesson_proposals p WHERE NOT EXISTS (SELECT 1 FROM lesson_entries e WHERE e.id = p.entry_id)').fetchone()[0])
print('invalid category (should be 0):', cur.execute("SELECT COUNT(*) FROM lesson_proposals WHERE category NOT IN ('structural','instrumentation','governance_rule','language','narrative','duplicate')").fetchone()[0])
print('invalid confidence (should be 0):', cur.execute("SELECT COUNT(*) FROM lesson_proposals WHERE confidence NOT IN ('low','medium','high')").fetchone()[0])
print('---')
print('lesson_entries total:', cur.execute('SELECT COUNT(*) FROM lesson_entries').fetchone()[0])
print('lesson_proposals total:', cur.execute('SELECT COUNT(*) FROM lesson_proposals').fetchone()[0])
for row in cur.execute('SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY 2 DESC').fetchall():
    print(' status', row[0], row[1])
for row in cur.execute('SELECT category, COUNT(*) FROM lesson_proposals GROUP BY category ORDER BY 2 DESC').fetchall():
    print(' category', row[0], row[1])
conn.close()
PY
```

`get_unclassified_entries` must return `[]` (all 9 classified) and the three `0` checks must be 0. The two stale rows (entries 93, 116 prior proposals) remain — expected; the newly-inserted `proposed` rows for 93 and 116 are what clear them from the work list. Counts go in the QA report.

(c) Schema drift:

```bash
sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".schema lesson_entries"
sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".schema lesson_proposals"
```

Compare both DDLs against `src/db.py`. Any drift is a QA failure. (The helper adds no schema change — drift is not expected.)

(d) Rule 20 self-check: run the canonical PLANNER_TEMPLATE Rule 20 block verbatim via `python3`; capture stdout literally in the QA report (do not summarize as "PASSED").

After QA passes, update `PROJECT_STATUS.md` with a dated cycle entry (new-helper note, work list 9 IDs, category/confidence distribution, post-cycle DB counts) per Rule 8.

**Deposits:**
- `knowledge/qa/cycle-qa-v2-2026-06-06.md` — QA report: four check results (literal output), Rule 20 stdout verbatim, PASS/FAIL verdict, Output Receipt block
- `knowledge/development/dev-log-cycle-v2-step-4-2026-06-06.md` — dev log

**Output Receipt fields required:**
- What was done
- Files deposited
- Four-check results + post-cycle DB counts
- Flags for CEO
- Status: Complete

**Closeout:** On terminal continue verdict, Bellows moves the plan to `Done/`. Planner performs Rule 22 verification (read QA report + confirm all deposits exist) before authorizing.

**Feedback log:** Append a feedback entry per step to `/Users/marklehn/Developer/GitHub/forge/knowledge/research/agent-prompt-feedback.md`.
