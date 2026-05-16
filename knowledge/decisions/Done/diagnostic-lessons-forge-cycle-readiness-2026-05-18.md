# Diagnostic — Lessons Forge Cycle Readiness

**Plan ID:** diagnostic-lessons-forge-cycle-readiness-2026-05-18
**Project:** lessons-forge
**Authored:** 2026-05-18
**Authored By:** Planner
**Plan Type:** Diagnostic (read-only, single step)

---

## Goal

Verify that Lessons Forge is operationally ready to run its first cycle from its new standalone repo location. Three weeks since the last cycle (2026-05-13, from forge), Phase A→B.1→B.2 extraction complete, four documented Bellows gate false positives in the last three weeks. Before authoring an executable that runs `run_full_lessons_cycle()` end-to-end, surface any wiring drift, stale references, or DB state surprises so the executable can be scoped to a known starting condition.

## Scope

Read-only. No DB writes. No file edits. Findings only.

## Execution Map

`Step 1 (Forge Developer) — diagnostic single step under Rule 22`

---

## Step 1 — Forge Developer

Single-step diagnostic. Read-only. Output is a findings file deposited at `lessons-forge/knowledge/research/lessons-forge-cycle-readiness-2026-05-18.md`.

### Specialist

Forge Developer (owns `src/lessons_forge.py` and the lesson DB schema).

### Working directory

`/Users/marklehn/Developer/GitHub/lessons-forge/`

### Pre-flight reads

1. `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — your specialist file (lives in forge, not lessons-forge — cross-repo read).
2. Skip the domain glossary read (Rule 16 — mechanical introspection task).
3. `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — to ground the wiring sanity checks below.
4. `/Users/marklehn/Developer/GitHub/lessons-forge/src/db.py` — for the lesson DDL (you'll cross-reference against live schema).

### Investigation tasks

Produce ONE findings deposit at `knowledge/research/lessons-forge-cycle-readiness-2026-05-18.md`. The deposit must include sections (a)–(j) below, each with literal command output as evidence. No prose-only sections — every claim cites a command and its output.

**(a) Module import integrity**

Run:
```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -c "from src.lessons_forge import run_full_lessons_cycle, generate_lessons_report, ingest_lesson_entries, parse_lessons_md, insert_proposal, detect_duplicates; print('OK')"
```

Expected: `OK`. Any ImportError is a wiring break — capture the full traceback.

**(b) Test suite baseline**

Run:
```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && python3 -m pytest src/test_lessons_forge.py -q 2>&1 | tail -20
```

Expected: 25 passed. Capture the last 20 lines verbatim including the summary.

**(c) Live DB state — counts and distributions**

Run a single Python heredoc against `lessons-forge.db`:
```python
python3 -c "
import sqlite3
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
print('=== lesson_entries count ===')
print(cur.execute('SELECT COUNT(*) FROM lesson_entries').fetchone()[0])
print('=== lesson_proposals count ===')
print(cur.execute('SELECT COUNT(*) FROM lesson_proposals').fetchone()[0])
print('=== lesson_proposals by status ===')
for row in cur.execute('SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status ORDER BY 2 DESC').fetchall():
    print(row[0], row[1])
print('=== lesson_proposals by category ===')
for row in cur.execute('SELECT category, COUNT(*) FROM lesson_proposals GROUP BY category ORDER BY 2 DESC').fetchall():
    print(row[0], row[1])
print('=== entries with NO proposal (the needs_classification pool) ===')
print(cur.execute('SELECT COUNT(*) FROM lesson_entries e WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals p WHERE p.entry_id = e.id)').fetchone()[0])
print('=== oldest + newest entry_date in lesson_entries ===')
print(cur.execute('SELECT MIN(entry_date), MAX(entry_date) FROM lesson_entries').fetchone())
conn.close()
"
```

Capture the full output verbatim under section (c).

**(d) LESSONS.md state**

Run:
```bash
wc -l /Users/marklehn/Developer/GitHub/LESSONS.md
grep -c '^## ' /Users/marklehn/Developer/GitHub/LESSONS.md
grep -n '^## Archived' /Users/marklehn/Developer/GitHub/LESSONS.md
```

Capture all three outputs. The third anchors the parser boundary — confirm the `## Archived` heading exists and report its line number.

**(e) Dry-run parse (no writes)**

Run:
```python
python3 -c "
from src.lessons_forge import parse_lessons_md
with open('/Users/marklehn/Developer/GitHub/LESSONS.md') as f:
    text = f.read()
entries = parse_lessons_md(text)
print(f'parsed {len(entries)} entries')
for e in entries:
    # Field names per src/lessons_forge.py — adjust if shape differs.
    h = e.get('source_heading') if isinstance(e, dict) else getattr(e, 'source_heading', None)
    d = e.get('entry_date') if isinstance(e, dict) else getattr(e, 'entry_date', None)
    print(f'  [{d}] {h}')
"
```

If the entry shape is not dict and not the attribute names guessed above, adapt the print loop to match `parse_lessons_md`'s actual return shape (you read the source in pre-flight). Capture the count + the entry list.

**(f) Ingestion delta — what a real cycle would pick up**

Run:
```python
python3 -c "
import sqlite3, hashlib
from src.lessons_forge import parse_lessons_md
conn = sqlite3.connect('/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db')
cur = conn.cursor()
existing_hashes = {row[0] for row in cur.execute('SELECT content_hash FROM lesson_entries').fetchall()}
with open('/Users/marklehn/Developer/GitHub/LESSONS.md') as f:
    text = f.read()
parsed = parse_lessons_md(text)
new_count = 0
new_list = []
for e in parsed:
    # Compute hash the same way ingest_lesson_entries does — read src for the canonical recipe.
    # If parse_lessons_md returns content_hash already, use that field instead of recomputing.
    h = e.get('content_hash') if isinstance(e, dict) else getattr(e, 'content_hash', None)
    if h is None:
        # Recompute from raw_content using the same algorithm as ingest.
        raw = e.get('raw_content') if isinstance(e, dict) else getattr(e, 'raw_content', '')
        h = hashlib.sha256(raw.encode()).hexdigest()
    if h not in existing_hashes:
        new_count += 1
        heading = e.get('source_heading') if isinstance(e, dict) else getattr(e, 'source_heading', None)
        date = e.get('entry_date') if isinstance(e, dict) else getattr(e, 'entry_date', None)
        new_list.append((date, heading))
print(f'parsed total: {len(parsed)}')
print(f'already in DB (by content_hash): {len(parsed) - new_count}')
print(f'NEW or CHANGED (would ingest): {new_count}')
for d, h in new_list:
    print(f'  [{d}] {h}')
conn.close()
"
```

If the hashing recipe in `ingest_lesson_entries` differs from `sha256(raw_content)` (e.g., normalized whitespace, or includes tags) — match it exactly. The deposit must report which recipe was used.

**(g) Wiring sanity — function defaults**

Run:
```python
python3 -c "
import inspect
from src.lessons_forge import detect_duplicates, run_full_lessons_cycle
sig_dd = inspect.signature(detect_duplicates)
sig_rc = inspect.signature(run_full_lessons_cycle)
print('detect_duplicates signature:', sig_dd)
print()
print('run_full_lessons_cycle signature:', sig_rc)
"
```

Capture both signatures. Confirm:
- `detect_duplicates`'s `reference_files` default points at `/Developer/GitHub/PLANNER_TEMPLATE.md` (not `/Desktop/GitHub/`).
- `run_full_lessons_cycle`'s `lessons_md_path` default points at `/Developer/GitHub/LESSONS.md` (not `/Desktop/GitHub/`).

If either still references `/Desktop/GitHub/`, that's a stale reference — Phase B.1 was supposed to fix this. Flag it.

**(h) Stale references in specialist file**

Run:
```bash
grep -n -E 'forge\.db|forge/src/|forge/agents/|\*\*Project:\*\* forge' /Users/marklehn/Developer/GitHub/lessons-forge/agents/FORGE_LESSONS_AGENT.md
```

Capture all hits with line numbers. Context: file Last Updated 2026-04-23 (pre-extraction). Expect multiple hits referring to the old forge location — this is documentation lag, not a code defect, but the deposit should enumerate every stale reference so the next executable knows what to fix.

**(i) Stale PROJECT_STATUS section**

Run:
```bash
grep -n -A2 '^## Pending — Phase B.2' /Users/marklehn/Developer/GitHub/lessons-forge/PROJECT_STATUS.md | head -10
```

If the "Pending — Phase B.2 (next session)" section still exists in PROJECT_STATUS.md (B.2 already shipped 2026-05-18), report the line range. This is closeout lag from the previous session.

**(j) Bellows daemon health + watch config**

Run:
```bash
cd /Users/marklehn/Developer/GitHub/bellows && cat config.json 2>&1 | python3 -c "import sys, json; c = json.load(sys.stdin); wps = c.get('watched_projects', []); print(f'watched_count: {len(wps)}'); print('lessons-forge present:', any('lessons-forge' in p for p in wps)); [print('  '+p) for p in wps]"
```

Also check daemon liveness:
```bash
tail -5 /Users/marklehn/Developer/GitHub/bellows/logs/terminal/bellows-$(date +%Y-%m-%d).log
```

Capture both outputs. Confirm `watched_count` is 9 and `lessons-forge` appears in the list.

### Gap Assessment (REQUIRED — this diagnostic is change-proposing)

At the end of the deposit, include a Gap Assessment table with these columns:

| # | Gap | Evidence (cite section) | Severity | Proposed fix |
|---|---|---|---|---|

Rows you'll likely need (don't fabricate — only include gaps section (a)–(j) actually surface):

- Stale references in `FORGE_LESSONS_AGENT.md` (from section h)
- Stale "Pending — Phase B.2" section in PROJECT_STATUS.md (from section i)
- Any wiring breakage discovered in (a), (b), (g)
- Any DB state surprises in (c) — e.g., entries with stale proposals, ambiguous status proposals, unexpected category distributions
- The ingestion-delta size (section f) drives whether the next executable is a full cycle run or a no-op skip

Severity scale: blocker (executable can't run until fixed) / wiring (cycle would run but with stale defaults) / hygiene (documentation lag, doesn't affect cycle) / informational (state observation, no fix).

### Output Receipt (REQUIRED)

End the deposit with a standard Output Receipt block per GUARDRAILS.md.

### Deposits

- `lessons-forge/knowledge/research/lessons-forge-cycle-readiness-2026-05-18.md` — findings deposit
- `lessons-forge/knowledge/development/dev-log-lessons-forge-cycle-readiness-2026-05-18.md` — dev log per closeout convention

### Closeout

1. Verify both deposit files exist on disk.
2. Append a feedback entry to `forge/knowledge/research/agent-prompt-feedback.md` describing what went well + what could be improved in this prompt (the feedback log lives in forge, not lessons-forge — cross-repo append is correct per the Phase B.1 feedback entries' precedent).
3. Report Status: Complete in conversation. Planner handles housekeeping under Rule 22.
