# Executable — Lessons Forge Cycle Run (first from new home)

**Plan ID:** executable-lessons-forge-cycle-run-2026-05-18
**Project:** lessons-forge
**Authored:** 2026-05-18
**Authored By:** Planner
**Plan Type:** Executable
**Depends on:** diagnostic-lessons-forge-cycle-readiness-2026-05-18 (Done)

---

## Goal

Run the first full Lessons Forge cycle from the new standalone repo location. Ingest 19 new LESSONS.md entries (dated 2026-05-13 → 2026-05-18), classify them via the Forge Lessons Agent, generate the report for Planner Gate 1 review.

## Scope

In-scope:
- `run_full_lessons_cycle()` end-to-end: parse → ingest → detect_duplicates → return needs_classification
- Classification of every entry in `needs_classification` via `insert_proposal()`
- `generate_lessons_report()` for Gate 1 review
- QA: test regression + DB invariants

Out-of-scope (deferred to separate plan):
- Hygiene fixes to `FORGE_LESSONS_AGENT.md` (7 stale references found in diagnostic)
- Hygiene fix to `PROJECT_STATUS.md` "Pending — Phase B.2" section
- Gate 2 governance edits (those happen after CEO reviews the report)

## Findings cited (from diagnostic, no source re-read by Planner)

- DB pre-cycle: 38 entries, 38 proposals, 0 unclassified (diagnostic section c)
- Ingestion delta: 19 new entries dated 2026-05-13 → 2026-05-18 (diagnostic section f)
- All wiring clean: imports OK, 25/25 tests pass, function defaults use `/Developer/GitHub/` (diagnostic sections a, b, g)
- Bellows daemon healthy, lessons-forge watched (diagnostic section j)

## Execution Map

`Step 1 (Forge Developer) → [verdict gate] → Step 2 (Forge Lessons Agent) → Step 3 (Forge Developer) → [verdict gate] → Step 4 (Forge Developer / QA)`

---

## STEP 1 — Forge Developer

### Specialist

Forge Developer.

### Working directory

`/Users/marklehn/Developer/GitHub/lessons-forge/`

### Pre-flight reads

1. `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — your specialist file (cross-repo read).
2. Skip the domain glossary read (Rule 16 — mechanical cycle invocation).
3. `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — for `run_full_lessons_cycle()` signature and return shape.

### Task

Run `run_full_lessons_cycle()` against `lessons-forge.db` and `LESSONS.md`. Capture the full return dict and persist `needs_classification` IDs to a JSON deposit for Step 2 to consume.

**Commands:**

```python
python3 << 'PY'
import sqlite3, json
from src.lessons_forge import run_full_lessons_cycle

conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
result = run_full_lessons_cycle(conn)
conn.commit()
conn.close()

# Persist the full result for Step 2 + audit trail
with open('/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/cycle-result-2026-05-18.json', 'w') as f:
    json.dump(result, f, indent=2, default=str)

# Print summary for verdict review
print('=== run_full_lessons_cycle result ===')
print(json.dumps(result, indent=2, default=str))
PY
```

**Verification commands (run after the above):**

```bash
# DB row counts post-ingestion
python3 -c "
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
print('lesson_entries:', cur.execute('SELECT COUNT(*) FROM lesson_entries').fetchone()[0])
print('lesson_proposals:', cur.execute('SELECT COUNT(*) FROM lesson_proposals').fetchone()[0])
print('entries needing classification:', cur.execute('SELECT COUNT(*) FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id = e.id)').fetchone()[0])
print('duplicate proposals just created:', cur.execute(\"SELECT COUNT(*) FROM lesson_proposals WHERE category = 'duplicate' AND created_at >= date('now', '-1 day')\").fetchone()[0])
conn.close()
"
```

**Expected output:**
- `lesson_entries`: 57 (was 38, +19 from diagnostic delta)
- `lesson_proposals`: ≥ 38 (38 existing + N new duplicate proposals from detect_duplicates)
- `entries needing classification`: equal to `len(result["needs_classification"])`
- The cycle-result JSON file exists at `knowledge/development/cycle-result-2026-05-18.json`

### Deposits

- `knowledge/development/cycle-result-2026-05-18.json` — full cycle result dict (Step 2 input)
- `knowledge/development/dev-log-cycle-run-step-1-2026-05-18.md` — dev log with the commands, full stdout, and the verification output

### pause_for_verdict: after_step_1

After Step 1, Bellows pauses for CEO verdict. Planner will:
- Read `cycle-result-2026-05-18.json` directly (Rule 22 — verify before authorizing)
- Verify entry count delta matches diagnostic prediction (19 new)
- Inspect duplicate-detection findings before authorizing LLM classification spend in Step 2
- Issue verdict: `continue` or `stop`

---

## STEP 2 — Forge Lessons Agent

### Specialist

Forge Lessons Agent (at `/Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md`).

**Note for the agent:** Your specialist file has stale references to `forge.db` and `forge/src/` paths — these are documentation lag from pre-extraction (2026-04-23). Operate against `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` and `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py`. A separate hygiene plan will fix the references later.

### Working directory

`/Users/marklehn/Developer/GitHub/lessons-forge/`

### Pre-flight reads

1. `/Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md` — your specialist file (note staleness caveat above).
2. `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — for `insert_proposal()` signature.
3. `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/development/cycle-result-2026-05-18.json` — input list of entry IDs needing classification.

### Task

Loop through every entry ID in `cycle-result-2026-05-18.json` → `needs_classification`. For each entry:

1. Read the entry from `lessons-forge.db`: `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id = ?`
2. Apply the ADR-002 six-value taxonomy (see your specialist file, "Operating Procedure" section).
3. Produce the JSON classification object with fields: `entry_id`, `category`, `confidence`, `suggested_action`, `reasoning`, `target_layer`, `target_artifact` (optional), `subcategory` (optional).
4. Call `insert_proposal(conn, **classification)` to persist.

**Per-entry reasoning must cite specific text from the entry's `raw_content`.** Generic category descriptions are insufficient.

**Do NOT assign `category='duplicate'`.** Duplicate detection ran deterministically in Step 1 and already wrote duplicate proposals to `lesson_proposals`. If you believe an entry is a duplicate that the deterministic check missed, classify based on the entry's substantive content and note the potential duplication in `reasoning`.

**Use `status='ambiguous'` (pass as the `status` arg to `insert_proposal()`) if an entry fits no category — do not invent new taxonomy values.**

### Output Receipt

After all classifications complete, write a summary to `knowledge/development/classifications-summary-2026-05-18.md`:

- Total entries classified
- Distribution by category (count per category)
- Distribution by confidence (low/medium/high)
- List of any `ambiguous` entries with reasoning
- Any entries flagged for potential duplication
- Total wall-clock time

### Deposits

- `knowledge/development/classifications-summary-2026-05-18.md` — classification summary for Planner
- `knowledge/development/dev-log-cycle-run-step-2-2026-05-18.md` — dev log

Database writes via `insert_proposal()` are tracked via DB row counts, not as file deposits.

---

## STEP 3 — Forge Developer

### Specialist

Forge Developer.

### Working directory

`/Users/marklehn/Developer/GitHub/lessons-forge/`

### Task

Run `generate_lessons_report()` and deposit the human-readable report for Planner Gate 1 review.

**Commands:**

```python
python3 << 'PY'
import sqlite3
from src.lessons_forge import generate_lessons_report

conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
report = generate_lessons_report(conn)
conn.close()

with open('/Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-cycle-report-2026-05-18.md', 'w') as f:
    f.write(report)

print('Report written. Length:', len(report), 'chars')
print()
print('=== first 80 lines for verdict review ===')
for line in report.splitlines()[:80]:
    print(line)
PY
```

**Verification:**

```bash
ls -la /Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-cycle-report-2026-05-18.md
wc -l /Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-cycle-report-2026-05-18.md
```

If the `reports/` directory doesn't exist, create it: `mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/reports/`.

### Deposits

- `reports/lessons-cycle-report-2026-05-18.md` — full cycle report for Planner Gate 1 review
- `knowledge/development/dev-log-cycle-run-step-3-2026-05-18.md` — dev log

### pause_for_verdict: after_step_3

Terminal-style verdict pause. Planner will read the report directly (Rule 22), apply Gate 1 review judgment, and issue verdict:
- `continue` → advance to Step 4 (QA)
- `stop` → halt cycle, report state to CEO

---

## STEP 4 — Forge Developer (QA)

### Specialist

Forge Developer (acting as QA — FORGE_QA specialist not yet authored, long-standing carry-forward item).

### Working directory

`/Users/marklehn/Developer/GitHub/lessons-forge/`

### Task

QA verification of the cycle. Four checks:

**(a) Test suite regression**

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v 2>&1 | tail -40
```

Expected: 25 passed, 0 failed. Any failure is a regression — flag and stop.

**(b) DB invariants**

```python
python3 << 'PY'
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()

# Every entry has at least one proposal (no orphans)
orphans = cur.execute('SELECT COUNT(*) FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id = e.id)').fetchone()[0]
print('orphan entries (should be 0):', orphans)

# Every proposal has a valid entry_id (referential integrity)
dangling = cur.execute('SELECT COUNT(*) FROM lesson_proposals p WHERE NOT EXISTS (SELECT 1 FROM lesson_entries e WHERE e.id = p.entry_id)').fetchone()[0]
print('dangling proposals (should be 0):', dangling)

# No proposals with category outside taxonomy
bad_cat = cur.execute("SELECT COUNT(*) FROM lesson_proposals WHERE category NOT IN ('structural','instrumentation','governance_rule','language','narrative','duplicate')").fetchone()[0]
print('proposals with invalid category (should be 0):', bad_cat)

# No proposals with confidence outside valid set
bad_conf = cur.execute("SELECT COUNT(*) FROM lesson_proposals WHERE confidence NOT IN ('low','medium','high')").fetchone()[0]
print('proposals with invalid confidence (should be 0):', bad_conf)

# Post-cycle counts
print('---')
print('lesson_entries total:', cur.execute('SELECT COUNT(*) FROM lesson_entries').fetchone()[0])
print('lesson_proposals total:', cur.execute('SELECT COUNT(*) FROM lesson_proposals').fetchone()[0])
print('proposals by status:')
for row in cur.execute('SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY 2 DESC').fetchall():
    print(' ', row[0], row[1])
print('proposals by category:')
for row in cur.execute('SELECT category, COUNT(*) FROM lesson_proposals GROUP BY category ORDER BY 2 DESC').fetchall():
    print(' ', row[0], row[1])
conn.close()
PY
```

All four "should be 0" checks must return 0. Counts go in the QA report.

**(c) Schema drift check**

```bash
sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".schema lesson_entries"
sqlite3 /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".schema lesson_proposals"
```

Compare both DDLs against the canonical schema in `src/db.py`. Any drift is a QA failure.

**(d) Rule 20 self-check**

Use the verbatim PLANNER_TEMPLATE Rule 20 self-check block. Print literal stdout in the QA report body (per the agent-prompt-feedback 2026-04-23 lesson — do not summarize as "PASSED").

### Output Receipt

QA report at `knowledge/qa/cycle-run-qa-2026-05-18.md` with:

- All four check results (literal command output)
- Rule 20 self-check stdout printed verbatim
- Final verdict: PASS / FAIL with rationale
- Output Receipt block per GUARDRAILS.md

### Deposits

- `knowledge/qa/cycle-run-qa-2026-05-18.md` — QA report
- `knowledge/development/dev-log-cycle-run-step-4-2026-05-18.md` — dev log

### Closeout

After Step 4 completes, agent reports `Status: Complete`. Planner handles housekeeping under Rule 22 (read QA report, verify all deposits exist, move plan to `Done/`).

### Feedback log

Per cross-repo precedent (Phase B.1 entries), append a feedback entry to `/Users/marklehn/Developer/GitHub/forge/knowledge/research/agent-prompt-feedback.md` at the end of EACH step covering what went well + what could be improved in that step's prompt.
