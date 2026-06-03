# Executable — Lessons Forge Cycle (2026-06-03)

**Plan slug:** executable-lessons-forge-cycle-2026-06-03
**Plan type:** executable
**Project:** lessons-forge
**Specialist:** Forge Developer (Steps 1, 3, 4) + Forge Lessons Agent (Step 2). QA role in Step 4 uses Forge Developer (FORGE_QA not yet authored — carry-forward).
**Auto-close:** false
**Pause for verdict:** always
**Dispatch Mode:** bellows
**Priority:** 1
**Depends on:** none
**Created:** 2026-06-03
**qa_steps:** 4

---

## Context

Routine Lessons Forge cycle. Ingests new `LESSONS.md` entries dated after the 2026-05-27 cycle (which ingested 36 entries, IDs 58-93, all dispositioned to `implemented`), classifies them via the Forge Lessons Agent, and generates the report for CEO Gate 1 review in a separate session. New input confirmed present (>=2 entries dated 2026-05-29 plus session-flagged candidates); Step 1 reports the authoritative new-entry count via content-hash dedup.

Structure mirrors the clean 2026-05-18 cycle plan; conventions current as of the 2026-05-27 plans (`qa_steps` header field, `**Pause for verdict:**` header enum, `**Deposits:**` blocks, monotonic `## STEP N` headers).

## Scope

In-scope: `run_full_lessons_cycle()` (parse -> ingest -> detect_duplicates), classification of every entry in `needs_classification` via `insert_proposal()`, `generate_lessons_report()`, QA (test regression + DB invariants + schema drift + Rule 20).

Out-of-scope (separate sessions): CEO Gate 1 disposition of proposals; Gate 2 governance edits to PLANNER_TEMPLATE; hygiene fixes to FORGE_LESSONS_AGENT.md stale references.

## Execution Map

`Step 1 (Forge Developer) -> [verdict] -> Step 2 (Forge Lessons Agent) -> [verdict] -> Step 3 (Forge Developer) -> [verdict] -> Step 4 (Forge Developer / QA) -> [verdict]`

---

## STEP 1 — Forge Developer

**Role:** Developer
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — specialist file (cross-repo).
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — `run_full_lessons_cycle()` signature and return shape.
- Skip the domain glossary (Rule 16 — mechanical cycle invocation).

**Task:**

Run `run_full_lessons_cycle()` against `lessons-forge.db` and the governance-root `LESSONS.md`. Capture the full return dict and persist `needs_classification` IDs to a JSON deposit for Step 2.

```python
python3 << 'PY'
import sqlite3, json
from src.lessons_forge import run_full_lessons_cycle

conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
result = run_full_lessons_cycle(conn)
conn.commit()
conn.close()

with open('/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/cycle-result-2026-06-03.json', 'w') as f:
    json.dump(result, f, indent=2, default=str)

print('=== run_full_lessons_cycle result ===')
print(json.dumps(result, indent=2, default=str))
PY
```

Verification:

```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
print('lesson_entries:', cur.execute('SELECT COUNT(*) FROM lesson_entries').fetchone()[0])
print('lesson_proposals:', cur.execute('SELECT COUNT(*) FROM lesson_proposals').fetchone()[0])
print('needs classification:', cur.execute('SELECT COUNT(*) FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id = e.id)').fetchone()[0])
conn.close()
"
```

Report the new-entry count and the `needs_classification` IDs. If zero new entries, set the Output Receipt status accordingly and stop — no classification needed.

**Deposits:**
- `knowledge/development/cycle-result-2026-06-03.json` — full cycle result dict (Step 2 input)
- `knowledge/development/dev-log-cycle-step-1-2026-06-03.md` — commands, full stdout, verification output

**Output Receipt fields required:**
- What was done
- Files deposited
- New-entry count + `needs_classification` IDs
- Flags for CEO
- Flags for Next Step

---

## STEP 2 — Forge Lessons Agent

**Role:** Lessons Agent
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md` — specialist file (ADR-002 six-value taxonomy in the Operating Procedure section).
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — `insert_proposal()` signature.
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/cycle-result-2026-06-03.json` — entry IDs needing classification.

**Task:**

For each entry ID in `cycle-result-2026-06-03.json` -> `needs_classification`:
1. Read it: `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id = ?`
2. Apply the ADR-002 six-value taxonomy from your specialist file.
3. Produce the classification object: `entry_id`, `category`, `confidence`, `suggested_action`, `reasoning`, `target_layer`, optional `target_artifact`, optional `subcategory`.
4. `insert_proposal(conn, **classification)`.

Per-entry `reasoning` MUST cite specific text from the entry's `raw_content` — generic category descriptions are insufficient. Do NOT assign `category='duplicate'` (deterministic detection already ran in Step 1; note suspected dupes in `reasoning`). Use `status='ambiguous'` if an entry fits no category — do not invent taxonomy values.

After all classifications, include a cross-batch synthesis in the summary: category distribution, confidence distribution, any clusters suggesting a consolidated PLANNER_TEMPLATE section (the strongest Gate 1 signal), and any ambiguous or suspected-duplicate entries.

**Deposits:**
- `knowledge/development/classifications-summary-2026-06-03.md` — distribution + cross-batch synthesis for CEO Gate 1
- `knowledge/development/dev-log-cycle-step-2-2026-06-03.md` — dev log

DB writes via `insert_proposal()` are tracked by row counts, not as file deposits.

**Output Receipt fields required:**
- What was done
- Files deposited
- Total classified + category/confidence distribution
- Flags for CEO (ambiguous entries, cluster signals)
- Flags for Next Step

---

## STEP 3 — Forge Developer

**Role:** Developer
**Working directory:** `/Users/marklehn/Developer/GitHub/lessons-forge/`
**Reads:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — `generate_lessons_report()` signature.
- `knowledge/development/classifications-summary-2026-06-03.md` — confirm Step 2 Output Receipt is Complete before running.

**Task:**

Run `generate_lessons_report()` and deposit the report for CEO Gate 1 review.

```python
python3 << 'PY'
import os, sqlite3
from src.lessons_forge import generate_lessons_report

conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
report = generate_lessons_report(conn)
conn.close()

os.makedirs('/Users/marklehn/Developer/GitHub/lessons-forge/reports/', exist_ok=True)
with open('/Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-06-03.md', 'w') as f:
    f.write(report)

print('Report written. Length:', len(report), 'chars')
for line in report.splitlines()[:80]:
    print(line)
PY
```

**Deposits:**
- `reports/lessons-report-2026-06-03.md` — full cycle report for CEO Gate 1 review
- `knowledge/development/dev-log-cycle-step-3-2026-06-03.md` — dev log

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
- `reports/lessons-report-2026-06-03.md` — confirm Step 3 Output Receipt is Complete.
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/db.py` — canonical schema for the drift check.

**Task — four checks:**

(a) Test regression:

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v 2>&1 | tail -40
```

Expected: 25 passed, 0 failed. Any failure -> flag and stop.

(b) DB invariants:

```python
python3 << 'PY'
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
print('orphan entries (should be 0):', cur.execute('SELECT COUNT(*) FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id = e.id)').fetchone()[0])
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

All four "should be 0" checks must return 0. Counts go in the QA report.

(c) Schema drift:

```bash
sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".schema lesson_entries"
sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".schema lesson_proposals"
```

Compare both DDLs against the canonical schema in `src/db.py`. Any drift is a QA failure.

(d) Rule 20 self-check: run the canonical PLANNER_TEMPLATE Rule 20 self-check block verbatim via `python3`; capture stdout literally in the QA report body (do not summarize as "PASSED").

After QA passes, update `PROJECT_STATUS.md` with a dated cycle entry (new-entry count, IDs, category/confidence distribution, post-cycle DB counts) per Rule 8.

**Deposits:**
- `knowledge/qa/cycle-qa-2026-06-03.md` — QA report: all four check results (literal output), Rule 20 stdout verbatim, PASS/FAIL verdict, Output Receipt block
- `knowledge/development/dev-log-cycle-step-4-2026-06-03.md` — dev log

**Output Receipt fields required:**
- What was done
- Files deposited
- Four-check results + post-cycle DB counts
- Flags for CEO
- Status: Complete

**Closeout:** On terminal continue verdict, Bellows moves the plan to `Done/`. Planner performs Rule 22 verification (read QA report + confirm all deposits exist) before authorizing.

**Feedback log:** Append a feedback entry per step to `/Users/marklehn/Developer/GitHub/forge/knowledge/research/agent-prompt-feedback.md`.
