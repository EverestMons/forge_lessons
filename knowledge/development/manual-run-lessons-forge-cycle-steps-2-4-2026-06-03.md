# Manual Run — Lessons Forge Cycle Steps 2-4 (2026-06-03)

Bellows bypass: the daemon dispatch hit repeated worktree-teardown failures, so run these steps as a single manual Claude Code session **in the main checkout** (`/Users/marklehn/Developer/GitHub/lessons-forge/`). Do NOT create a git worktree. Step 1 (ingest of 23 new entries, IDs 94-116) already landed on main (commit 56ddcce). Run Steps 2 -> 3 -> 4 in order, then commit + push.

---

## STEP 2 — Forge Lessons Agent (classification)

Read `agents/FORGE_LESSONS_AGENT.md` (ADR-002 six-value taxonomy, Operating Procedure section) and `src/lessons_forge.py` for the `insert_proposal()` signature.

Derive the work list from the DB — entries with NO proposal yet. Do NOT use the cycle-result JSON's `needs_classification` (it lists already-classified entries too):

```python
python3 << 'PY'
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
todo = [r[0] for r in cur.execute('SELECT e.id FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id) ORDER BY e.id').fetchall()]
conn.close()
print('to classify (', len(todo), '):', todo)
PY
```

Expected: 23 IDs (94-116). For each: read `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id=?`, apply the taxonomy, and `insert_proposal(conn, **classification)` with fields `entry_id, category, confidence, suggested_action, reasoning, target_layer` (+ optional `target_artifact`, `subcategory`). `reasoning` MUST cite specific text from `raw_content`. Do NOT assign `category='duplicate'`. Use `status='ambiguous'` only if no category fits.

Deposit `knowledge/development/classifications-summary-2026-06-03.md`: total classified, category distribution, confidence distribution, cross-batch synthesis (clusters suggesting a consolidated PLANNER_TEMPLATE section — the strongest Gate 1 signal), and any ambiguous/suspected-duplicate entries.

---

## STEP 3 — Forge Developer (report)

```python
python3 << 'PY'
import os, sqlite3
from src.lessons_forge import generate_lessons_report
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
report = generate_lessons_report(conn)
conn.close()
os.makedirs('/Users/marklehn/Developer/GitHub/lessons-forge/reports/', exist_ok=True)
open('/Users/marklehn/Developer/GitHub/lessons-forge/reports/lessons-report-2026-06-03.md','w').write(report)
print('report chars:', len(report))
PY
```

---

## STEP 4 — QA + commit

Four checks (capture output for the QA report):

(a) `cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -v 2>&1 | tail -40` — expect 25 passed, 0 failed.

(b) DB invariants — all four must be 0:
```python
python3 << 'PY'
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
print('orphans:', cur.execute('SELECT COUNT(*) FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id=e.id)').fetchone()[0])
print('dangling:', cur.execute('SELECT COUNT(*) FROM lesson_proposals p WHERE NOT EXISTS (SELECT 1 FROM lesson_entries e WHERE e.id=p.entry_id)').fetchone()[0])
print('bad_category:', cur.execute("SELECT COUNT(*) FROM lesson_proposals WHERE category NOT IN ('structural','instrumentation','governance_rule','language','narrative','duplicate')").fetchone()[0])
print('bad_confidence:', cur.execute("SELECT COUNT(*) FROM lesson_proposals WHERE confidence NOT IN ('low','medium','high')").fetchone()[0])
for row in cur.execute('SELECT category, COUNT(*) FROM lesson_proposals GROUP BY category ORDER BY 2 DESC'): print(' cat', row[0], row[1])
conn.close()
PY
```

(c) Schema drift: `sqlite3 lessons-forge.db ".schema lesson_entries"` and `".schema lesson_proposals"` vs `src/db.py`. Any drift is a FAIL.

(d) Rule 20 self-check: run the canonical PLANNER_TEMPLATE block verbatim via `python3`; capture stdout literally in the QA report (do not summarize as "PASSED").

Update `PROJECT_STATUS.md` with a dated cycle entry: 23 new entries (94-116), category/confidence distribution, post-cycle DB counts. Deposit the QA report at `knowledge/qa/cycle-qa-2026-06-03.md`.

Then commit directly to main (no worktree) and push:
```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge
git add lessons-forge.db knowledge/development/classifications-summary-2026-06-03.md knowledge/development/dev-log-cycle-steps-2-4-2026-06-03.md reports/lessons-report-2026-06-03.md knowledge/qa/cycle-qa-2026-06-03.md PROJECT_STATUS.md
git commit -m "feat(lessons-forge): cycle 2026-06-03 — classify 23 new entries (94-116) + report + QA"
git fetch origin && git pull --rebase origin main && git push origin main
```

Report back: the 23 classified IDs, category/confidence distribution, QA PASS/FAIL, and the commit SHA.
