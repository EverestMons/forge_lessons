# Executable: Lessons Forge Cycle 2026-05-27 — Run + Phase 2A Classification (Split Batch)

**Plan slug:** executable-lessons-forge-cycle-2026-05-27
**Plan type:** executable
**Project:** lessons-forge
**Specialist:** Forge Lessons Agent
**Dispatch Mode:** Bellows
**Auto-close:** false
**Pause for verdict:** always
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-27

---

## Context

First Lessons Forge cycle since 2026-05-18 (gates 2a/2b/2c/2d all closed; 62 prior proposals at terminal status: 32 implemented, 24 superseded, 6 rejected). Between 2026-05-18 and 2026-05-27, LESSONS.md underwent substantial editing — pre-cycle diagnostic confirms parser sees 36 entries in current LESSONS.md, DB has 57 entries from prior cycles, **zero heading overlap**. All 36 current parser entries will be ingested as new this cycle.

**Pre-state baseline (live DB query 2026-05-27):**

| Metric | Value |
|---|---|
| lesson_entries (total in DB) | 57 |
| lesson_proposals (total in DB) | 62 |
| Proposals at status='proposed' or 'accepted' | 0 |
| Proposals at terminal status | 62 |
| Parser sees in current LESSONS.md | 36 entries |
| Headings overlapping DB ↔ LESSONS.md | 0 |
| Entries expected to ingest as new | 36 |

**Why split batch:** Cycle 1 (2026-05-01) classified 14 entries in one agent invocation; cycle 2 (2026-05-13) classified 5. This cycle's 36 entries is 2.5× the largest prior batch. Per CEO decision (h)(2), Phase 2A is split into Step 2a (entries 1-18) and Step 2b (entries 19-36), each its own Bellows dispatch with verdict pause between them, to bound context pressure and produce durable per-batch commits.

**Scope per CEO decision:** This plan runs the deterministic cycle + Phase 2A classifications. CEO Gate 1 review of classification quality happens in a follow-up conversation. Phase 2B (PLANNER_TEMPLATE / specialist file edits driven by accepted proposals) is NOT in scope.

**Steps and pause semantics:**

- Step 1 (cycle run) → verdict pause → CEO inspects ingestion count and `needs_classification` queue
- Step 2a (classify entries 1-18) → verdict pause → CEO inspects first-batch classification quality
- Step 2b (classify entries 19-36) → verdict pause → CEO inspects second-batch quality + cross-cutting patterns
- Step 3 (closeout + PROJECT_STATUS) → plan moves to Done

## API reference (verified against `src/lessons_forge.py` 2026-05-27)

- `run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md") → dict`
  - Returns `{ingested_count, updated_count, unchanged_count, duplicates_marked_count, needs_classification, cycle_timestamp}`
  - Does NOT call `conn.commit()` — caller must commit.
- `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, status='proposed', target_layer=None, target_artifact=None, duplicate_of=None, subcategory=None) → proposal_id`
  - `category` ∈ {`structural`, `instrumentation`, `governance_rule`, `language`, `narrative`, `duplicate`}
  - `confidence` ∈ {`low`, `medium`, `high`}
  - `status` ∈ {`proposed`, `accepted`, `rejected`, `ambiguous`, `stale`, `superseded`, `implemented`}
  - `target_layer` ∈ {`structure`, `governance`, `language`, `none`} or `NULL`
  - Does NOT call `conn.commit()` — caller must commit.
  - **Agent MUST NOT assign `category='duplicate'`** — reserved for deterministic `detect_duplicates()`.

---

## STEP 1 — Forge Lessons Agent: Run Deterministic Cycle

You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` for taxonomy reference (used in Steps 2a/2b; loading now is acceptable). Skip glossary read. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.

**Sub-step 1.0 — Pre-state snapshot.** Use `Filesystem:write_file` to create scratch file `pre_state.py`:

```python
import sqlite3

conn = sqlite3.connect("lessons-forge.db")
entries_total = conn.execute("SELECT COUNT(*) FROM lesson_entries").fetchone()[0]
proposals_total = conn.execute("SELECT COUNT(*) FROM lesson_proposals").fetchone()[0]
proposed = conn.execute("SELECT COUNT(*) FROM lesson_proposals WHERE status = 'proposed'").fetchone()[0]
accepted = conn.execute("SELECT COUNT(*) FROM lesson_proposals WHERE status = 'accepted'").fetchone()[0]
max_entry_id = conn.execute("SELECT MAX(id) FROM lesson_entries").fetchone()[0]
max_proposal_id = conn.execute("SELECT MAX(id) FROM lesson_proposals").fetchone()[0]
print(f"lesson_entries total: {entries_total}")
print(f"lesson_proposals total: {proposals_total}")
print(f"  status=proposed: {proposed}")
print(f"  status=accepted: {accepted}")
print(f"max_entry_id: {max_entry_id}")
print(f"max_proposal_id: {max_proposal_id}")
conn.close()
```

Run: `python3 pre_state.py`. Capture output. Expected: entries=57, proposals=62, proposed=0, accepted=0.

**Sub-step 1.1 — Run the cycle.** Create scratch file `run_cycle.py`:

```python
import sqlite3, json
from src.lessons_forge import run_full_lessons_cycle

conn = sqlite3.connect("lessons-forge.db")
result = run_full_lessons_cycle(conn)
conn.commit()

output = {
    "ingested_count": result["ingested_count"],
    "updated_count": result["updated_count"],
    "unchanged_count": result["unchanged_count"],
    "duplicates_marked_count": result["duplicates_marked_count"],
    "needs_classification": result["needs_classification"],
    "cycle_timestamp": result["cycle_timestamp"],
}
print(json.dumps(output, indent=2))
conn.close()
```

Run: `python3 run_cycle.py`. Capture JSON output verbatim. Expected: `ingested_count` ≈ 36, `needs_classification` list of ~36 entry IDs.

**Sub-step 1.2 — Post-state snapshot.** Re-run `pre_state.py`, capture output, compute deltas.

**Sub-step 1.3 — Inspect `needs_classification` queue.** Create scratch file `inspect_queue.py`:

```python
import sqlite3

NEEDS_CLASSIFICATION_IDS = []  # REPLACE with list from sub-step 1.1 JSON output

conn = sqlite3.connect("lessons-forge.db")
conn.row_factory = sqlite3.Row

assert NEEDS_CLASSIFICATION_IDS, "fill IDs from sub-step 1.1"

placeholders = ",".join("?" * len(NEEDS_CLASSIFICATION_IDS))
rows = conn.execute(
    f"SELECT id, entry_date, substr(source_heading, 1, 100) AS heading, tags "
    f"FROM lesson_entries WHERE id IN ({placeholders}) ORDER BY id",
    NEEDS_CLASSIFICATION_IDS,
).fetchall()
for r in rows:
    tags = r["tags"][:60] if r["tags"] else "(no tags)"
    print(f"  #{r['id']:3d} {r['entry_date']} {r['heading']}")
    print(f"        tags: {tags}")

conn.close()
```

Edit `NEEDS_CLASSIFICATION_IDS` with the list from sub-step 1.1, run `python3 inspect_queue.py`, capture output.

**Sub-step 1.4 — Compute batch split for Steps 2a/2b.** The queue is sorted by entry ID. Compute:
- Step 2a batch: first 18 IDs (`needs_classification[:18]`)
- Step 2b batch: remaining IDs (`needs_classification[18:]`)

Record both lists in the deposit explicitly so Steps 2a and 2b can load them without recomputing.

**Sub-step 1.5 — Cleanup.** `rm pre_state.py run_cycle.py inspect_queue.py`.

**Sub-step 1.6 — Commit.** `git add lessons-forge.db && git commit -m "feat: lessons forge cycle 2026-05-27 — ingest 36 new entries"`. Use `git add -f lessons-forge.db` if gitignored.

**Dev log / deposit:** Write `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md` with sections:
1. Pre-state snapshot (sub-step 1.0 output)
2. Cycle result JSON (sub-step 1.1 output verbatim)
3. Post-state snapshot + delta table
4. `needs_classification` queue listing (full list of IDs with date, heading, tags)
5. Batch split: Step 2a IDs and Step 2b IDs as separate explicit lists
6. Interpretation: did duplicates fire? was ingested_count exactly 36 or different (and why)? any anomalies?
7. Output Receipt with status Complete

**Output Receipt:**
- Agent: Forge Lessons Agent
- Step: 1
- Status: Complete (cycle ran, ingestion data captured); Blocked (cycle errored)
- What Was Done: ran `run_full_lessons_cycle`, captured ingestion deltas, inspected and split `needs_classification` queue for Steps 2a/2b
- Files Deposited: `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md`
- Files Created or Modified: `lessons-forge.db` (committed)
- Decisions Made: batch split for entries 1-18 / 19-36
- Flags for CEO: ingestion count differs from expected 36; or `duplicates_marked_count` > 0 (would indicate cross-entry duplication worth reviewing before classification)
- Flags for Next Step: Step 2a loads the first-18 batch from this deposit

**Deposits:**
- `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md`

Standard prompt feedback protocol → `knowledge/research/agent-prompt-feedback.md`.

---

## STEP 2A — Forge Lessons Agent: Classify First Batch (entries 1-18)

You are the Forge Lessons Agent. Read `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md` and verify Step 1 Output Receipt status is Complete. Read `agents/FORGE_LESSONS_AGENT.md` in full — it is the authoritative reference for the ADR-002 taxonomy and edge-case handling. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.

**Sub-step 2a.0 — Load Step 2a batch.** Read Section 5 of Step 1's deposit to get the first-18 entry IDs. Use `Filesystem:write_file` to create scratch file `load_entries_2a.py`:

```python
import sqlite3, json

ENTRY_IDS = []  # REPLACE with Step 2a batch from Step 1 deposit Section 5

conn = sqlite3.connect("lessons-forge.db")
conn.row_factory = sqlite3.Row

assert ENTRY_IDS, "fill ENTRY_IDS from Step 1 deposit"
assert len(ENTRY_IDS) == 18, f"Step 2a batch must be 18 entries, got {len(ENTRY_IDS)}"

placeholders = ",".join("?" * len(ENTRY_IDS))
rows = conn.execute(
    f"SELECT id, entry_date, source_heading, raw_content, tags "
    f"FROM lesson_entries WHERE id IN ({placeholders}) ORDER BY id",
    ENTRY_IDS,
).fetchall()

entries = [{"id": r["id"], "entry_date": r["entry_date"], "source_heading": r["source_heading"],
            "raw_content": r["raw_content"], "tags": r["tags"]} for r in rows]

with open("classification_input_2a.json", "w") as f:
    json.dump(entries, f, indent=2)

print(f"Loaded {len(entries)} entries to classification_input_2a.json")
conn.close()
```

Edit `ENTRY_IDS`, run `python3 load_entries_2a.py`.

**Sub-step 2a.1 — Classify each entry (you ARE the classifier).**

Read `classification_input_2a.json`. For EACH of the 18 entries:

**(a) Read the entry's `source_heading`, `raw_content`, and `tags`.** Tags often pre-suggest the classification (e.g., `[tag: planner-discipline, rule-22]` suggests `governance_rule` or `instrumentation`).

**(b) Apply the ADR-002 six-category taxonomy** (per `agents/FORGE_LESSONS_AGENT.md`):

| Category | Use when |
|---|---|
| `structural` | Change to file structure, directory layout, schema, or filesystem convention |
| `instrumentation` | Gate/mechanism/automation: enforce something mechanically rather than via prose rule |
| `governance_rule` | New or modified PLANNER_TEMPLATE / SPECIALIST_TEMPLATE / COMPANY rule |
| `language` | Phrasing/wording change in existing governance text without behavioral change |
| `narrative` | Pure observation; no proposed action; documenting reality |
| `duplicate` | DO NOT ASSIGN — reserved for deterministic detect_duplicates() |

**Decision tree for structural/instrumentation/governance_rule boundary:**
- Mechanical enforcement (gate, regex check, automated CI step) → `instrumentation`
- Prose rule for a governance file (Planner reads and applies) → `governance_rule`
- Filesystem or schema change (new directory, new column, new naming convention) → `structural`
- If ambiguous, prefer `governance_rule` with `confidence='medium'` and note the ambiguity in reasoning

**(c) Produce a classification dict per entry** with fields matching `insert_proposal` parameters:

```python
{
    "entry_id": <int>,
    "category": <str>,            # one of: structural, instrumentation, governance_rule, language, narrative
    "suggested_action": <str>,    # 1-2 sentence concrete recommendation
    "reasoning": <str>,           # MUST cite specific text from raw_content
    "confidence": <str>,          # low / medium / high
    "target_layer": <str|None>,   # structure / governance / language / none / None
    "target_artifact": <str|None>,# e.g. "PLANNER_TEMPLATE.md", None for narrative
    "status": <str>,              # default "proposed"; use "ambiguous" if entry resists classification
}
```

**Reasoning quality requirement (per specialist file):** `reasoning` MUST cite specific text from `raw_content`. Generic taxonomy descriptions are insufficient.

**Ambiguity handling:** If an entry doesn't fit any category, set `status='ambiguous'` and explain in reasoning. Do NOT invent new taxonomy values.

**Sub-step 2a.2 — Persist classifications.** Create scratch file `persist_2a.py`:

```python
import sqlite3
from src.lessons_forge import insert_proposal

CLASSIFICATIONS = [
    # Fill with classification dicts from sub-step 2a.1, one dict per entry
]

assert CLASSIFICATIONS, "fill CLASSIFICATIONS"
assert len(CLASSIFICATIONS) == 18, f"Step 2a expects 18 classifications, got {len(CLASSIFICATIONS)}"

conn = sqlite3.connect("lessons-forge.db")
inserted = []
for c in CLASSIFICATIONS:
    status = c.get("status", "proposed")
    pid = insert_proposal(
        conn,
        entry_id=c["entry_id"],
        category=c["category"],
        suggested_action=c["suggested_action"],
        reasoning=c["reasoning"],
        confidence=c["confidence"],
        status=status,
        target_layer=c.get("target_layer"),
        target_artifact=c.get("target_artifact"),
    )
    inserted.append((c["entry_id"], pid, c["category"], status))

conn.commit()
print(f"Inserted {len(inserted)} proposals (Step 2a):")
for entry_id, pid, cat, status in inserted:
    print(f"  entry {entry_id} → proposal {pid} ({cat}, {status})")
conn.close()
```

Edit `CLASSIFICATIONS`, run `python3 persist_2a.py`, capture output.

**Sub-step 2a.3 — Cleanup.** `rm load_entries_2a.py persist_2a.py classification_input_2a.json`.

**Sub-step 2a.4 — Commit.** `git add lessons-forge.db && git commit -m "feat: lessons forge 2026-05-27 — Phase 2A batch 1 (entries 1-18) classified"`.

**Deposit:** `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md` with sections:
1. Batch metadata (entry ID range, count = 18)
2. **Classification table** — one row per entry: `entry_id`, `category`, `confidence`, `target_layer`, `target_artifact`, `status`, `suggested_action` (truncated to ~80 chars)
3. **Distribution summary** — category counts within this batch, confidence breakdown
4. **Cross-cutting observations within batch** — any patterns the agent noticed
5. **Ambiguous / low-confidence entries** — entries that resisted classification with the recorded reasoning
6. Output Receipt with status Complete

**Output Receipt:**
- Agent: Forge Lessons Agent
- Step: 2a
- Status: Complete (18 proposals inserted with non-duplicate category); Partial (one or more entries flagged ambiguous, still Complete unless persistence failed); Blocked (CHECK constraint violation or FK violation during persist)
- What Was Done: classified 18 entries via single-loop batch dispatch, persisted via `insert_proposal`
- Files Deposited: `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md`
- Files Created or Modified: `lessons-forge.db` (committed)
- Decisions Made: 18 classification tuples
- Flags for CEO: ambiguous entries needing CEO judgment; any category that surprised the agent
- Flags for Next Step: Step 2b loads entries 19-36 from Step 1 deposit and applies the same classification procedure

**Deposits:**
- `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md`

Standard prompt feedback protocol.

---

## STEP 2B — Forge Lessons Agent: Classify Second Batch (entries 19-36)

You are the Forge Lessons Agent. Read `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md` and verify Step 2a Output Receipt status is Complete. The classification procedure is identical to Step 2a; this step processes the second batch from Step 1's split.

All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.

**Sub-step 2b.0 — Load Step 2b batch.** Read Section 5 of Step 1's deposit to get the remaining-18 entry IDs. Use `Filesystem:write_file` to create scratch file `load_entries_2b.py`:

```python
import sqlite3, json

ENTRY_IDS = []  # REPLACE with Step 2b batch from Step 1 deposit Section 5

conn = sqlite3.connect("lessons-forge.db")
conn.row_factory = sqlite3.Row

assert ENTRY_IDS, "fill ENTRY_IDS from Step 1 deposit"

placeholders = ",".join("?" * len(ENTRY_IDS))
rows = conn.execute(
    f"SELECT id, entry_date, source_heading, raw_content, tags "
    f"FROM lesson_entries WHERE id IN ({placeholders}) ORDER BY id",
    ENTRY_IDS,
).fetchall()

entries = [{"id": r["id"], "entry_date": r["entry_date"], "source_heading": r["source_heading"],
            "raw_content": r["raw_content"], "tags": r["tags"]} for r in rows]

with open("classification_input_2b.json", "w") as f:
    json.dump(entries, f, indent=2)

print(f"Loaded {len(entries)} entries to classification_input_2b.json")
conn.close()
```

Edit `ENTRY_IDS`, run `python3 load_entries_2b.py`.

**Sub-step 2b.1 — Classify each entry.** Apply the identical procedure from Step 2a sub-step 2a.1 (taxonomy table, decision tree, classification dict shape, reasoning quality requirement, ambiguity handling). Produce one classification dict per entry.

**Sub-step 2b.2 — Persist classifications.** Create scratch file `persist_2b.py` (identical shape to `persist_2a.py` but for the Step 2b batch):

```python
import sqlite3
from src.lessons_forge import insert_proposal

CLASSIFICATIONS = [
    # Fill with classification dicts from sub-step 2b.1
]

assert CLASSIFICATIONS, "fill CLASSIFICATIONS"

conn = sqlite3.connect("lessons-forge.db")
inserted = []
for c in CLASSIFICATIONS:
    status = c.get("status", "proposed")
    pid = insert_proposal(
        conn,
        entry_id=c["entry_id"],
        category=c["category"],
        suggested_action=c["suggested_action"],
        reasoning=c["reasoning"],
        confidence=c["confidence"],
        status=status,
        target_layer=c.get("target_layer"),
        target_artifact=c.get("target_artifact"),
    )
    inserted.append((c["entry_id"], pid, c["category"], status))

conn.commit()
print(f"Inserted {len(inserted)} proposals (Step 2b):")
for entry_id, pid, cat, status in inserted:
    print(f"  entry {entry_id} → proposal {pid} ({cat}, {status})")
conn.close()
```

Edit `CLASSIFICATIONS`, run `python3 persist_2b.py`, capture output.

**Sub-step 2b.3 — Cleanup.** `rm load_entries_2b.py persist_2b.py classification_input_2b.json`.

**Sub-step 2b.4 — Commit.** `git add lessons-forge.db && git commit -m "feat: lessons forge 2026-05-27 — Phase 2A batch 2 (entries 19-36) classified"`.

**Deposit:** `knowledge/research/lessons-forge-cycle-step2b-classifications-2026-05-27.md` with sections:
1. Batch metadata (entry ID range, count)
2. Classification table for this batch
3. Distribution summary within batch
4. Cross-cutting observations within batch
5. **Cross-batch observations** — patterns spanning Steps 2a + 2b (e.g., recurring themes across the full 36-entry cycle). This is the human-review hook for CEO Gate 1.
6. Ambiguous / low-confidence entries
7. Output Receipt with status Complete

**Output Receipt:**
- Agent: Forge Lessons Agent
- Step: 2b
- Status: Complete; Partial; Blocked
- What Was Done: classified remaining 18 entries, persisted via `insert_proposal`, cross-batch synthesis
- Files Deposited: `knowledge/research/lessons-forge-cycle-step2b-classifications-2026-05-27.md`
- Files Created or Modified: `lessons-forge.db` (committed)
- Decisions Made: 18 classification tuples + cross-batch synthesis
- Flags for CEO: cross-cutting patterns warranting CEO attention; ambiguous entries; any cluster suggesting a meta-pattern
- Flags for Next Step: Step 3 closes out the plan

**Deposits:**
- `knowledge/research/lessons-forge-cycle-step2b-classifications-2026-05-27.md`

Standard prompt feedback protocol.

---

## STEP 3 — Forge Lessons Agent: Closeout + PROJECT_STATUS Update

You are the Forge Lessons Agent. Read all three prior deposits (`step1`, `step2a`, `step2b`) and verify all Output Receipts show Complete. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.

**Sub-step 3.0 — Verification queries.** Create scratch file `verify.py`:

```python
import sqlite3

PRE_CYCLE_MAX_PROPOSAL_ID = 0  # REPLACE with max_proposal_id from Step 1 pre-state (sub-step 1.0)

conn = sqlite3.connect("lessons-forge.db")
conn.row_factory = sqlite3.Row

print("=== Distribution of NEW proposals (this cycle) ===")
rows = conn.execute(
    "SELECT category, confidence, status, COUNT(*) AS c "
    "FROM lesson_proposals WHERE id > ? "
    "GROUP BY category, confidence, status ORDER BY category, confidence, status",
    (PRE_CYCLE_MAX_PROPOSAL_ID,),
).fetchall()
for r in rows:
    print(f"  {r['category']:20s} {r['confidence']:8s} {r['status']:12s} {r['c']}")

print()
total = conn.execute(
    "SELECT COUNT(*) FROM lesson_proposals WHERE id > ?",
    (PRE_CYCLE_MAX_PROPOSAL_ID,),
).fetchone()[0]
print(f"Total new proposals: {total}")

print()
print("=== Entries from this cycle without proposals (gap check) ===")
gap = conn.execute(
    "SELECT le.id, substr(le.source_heading, 1, 80) AS heading "
    "FROM lesson_entries le "
    "WHERE NOT EXISTS (SELECT 1 FROM lesson_proposals lp WHERE lp.entry_id = le.id) "
    "AND le.id > ?",
    (PRE_CYCLE_MAX_PROPOSAL_ID,),  # rough proxy — entries newer than pre-cycle baseline
).fetchall()
if gap:
    print(f"  {len(gap)} entries have no proposal:")
    for r in gap:
        print(f"    #{r['id']} {r['heading']}")
else:
    print("  (none)")

conn.close()
```

Edit `PRE_CYCLE_MAX_PROPOSAL_ID` from Step 1 pre-state, run `python3 verify.py`, capture output.

**Sub-step 3.1 — Rule 20 self-check.** Create scratch file `rule20_check.py`:

```python
import os, sys

deposits = [
    "knowledge/research/lessons-forge-cycle-step1-2026-05-27.md",
    "knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md",
    "knowledge/research/lessons-forge-cycle-step2b-classifications-2026-05-27.md",
]
hedging_keywords = ["pending", "inferred", "extrapolated", "estimated", "approximate", "assumed", "close enough", "should pass", "would pass", "not run"]
POSITIVE_STATUS_TOKENS = ["✅", "OK", "PASS", "[x]", "done", "complete", "verified"]

def is_positive_row(line):
    if "|" not in line:
        return False
    cells = [c.strip() for c in line.split("|")]
    for cell in cells:
        for token in POSITIVE_STATUS_TOKENS:
            if token == "✅":
                if "✅" in cell:
                    return True
            else:
                if cell.lower() == token.lower():
                    return True
    return False

failures = []
for p in deposits:
    if not os.path.isfile(p):
        failures.append(f"missing: {p}")
    elif os.path.getsize(p) == 0:
        failures.append(f"empty: {p}")
    else:
        with open(p) as f:
            text = f.read()
        for line in text.splitlines():
            if is_positive_row(line):
                lower = line.lower()
                for kw in hedging_keywords:
                    if kw in lower:
                        failures.append(f"hedging '{kw}' in positive row of {p}: {line.strip()[:120]}")
                        break

print("Rule 20 — QA Self-Check Results")
if failures:
    print(f"FAILED — {len(failures)} issue(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
else:
    print("PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.")
```

Run: `python3 rule20_check.py`. Capture stdout verbatim. If FAILED, halt — do not update PROJECT_STATUS, do not advance plan. If PASSED, proceed.

**Sub-step 3.2 — Update PROJECT_STATUS.md.** Use `Desktop Commander:edit_block` to find the exact line `## Health` in `PROJECT_STATUS.md` and replace with:

```
## Health

Standalone repo fully integrated. Cycle run 2026-05-27 ingested [N] new entries from LESSONS.md (DB had 57 orphan entries from prior LESSONS.md state — zero heading overlap with current content). Phase 2A classifications shipped for [N] entries across two batches via Bellows-dispatched plan with verdict pauses between steps. Phase 2A complete. Next: CEO Gate 1 review of classifications (separate session).

---

## 2026-05-27 — Cycle run + Phase 2A classifications shipped (split-batch dispatch)

Ingested [N] new entries (parser saw 36 in current LESSONS.md). All [N] classified across Step 2a (entries 1-18) and Step 2b (entries 19-36) via separate Bellows dispatches. Distribution: [list category counts]. Confidence breakdown: [H] high, [M] medium, [L] low. Cross-cutting observations: [brief summary from Step 2b deposit Section 5]. CEO Gate 1 review pending in follow-up session.

**Deposits:**
- `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md`
- `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md`
- `knowledge/research/lessons-forge-cycle-step2b-classifications-2026-05-27.md`

Pre-cycle DB state: entries=57, proposals=62 (all terminal). Post-cycle: entries=[57+N], proposals=[62+N].

---
```

Replace bracketed placeholders with actual values from Step 1's post-state and Steps 2a/2b distribution summaries.

**Sub-step 3.3 — Commit.** `git add PROJECT_STATUS.md knowledge/research/agent-prompt-feedback.md && git commit -m "chore: lessons forge 2026-05-27 — status update + Phase 2A closeout"`.

**Sub-step 3.4 — Cleanup.** `rm verify.py rule20_check.py`.

**Dev log / deposit:** Write `knowledge/development/dev-log-lessons-forge-cycle-step3-2026-05-27.md` with:
1. Verification query output (sub-step 3.0)
2. Rule 20 self-check stdout (sub-step 3.1)
3. PROJECT_STATUS edit summary
4. Commits made this step
5. Output Receipt with status Complete

**Output Receipt:**
- Agent: Forge Lessons Agent
- Step: 3
- Status: Complete (Rule 20 PASSED, PROJECT_STATUS updated, final commit landed); Blocked (Rule 20 FAILED)
- What Was Done: ran post-cycle verification queries, executed Rule 20 self-check, updated PROJECT_STATUS, committed
- Files Deposited: `knowledge/development/dev-log-lessons-forge-cycle-step3-2026-05-27.md`
- Files Created or Modified: `PROJECT_STATUS.md` (committed)
- Decisions Made: none (mechanical closeout)
- Flags for CEO: any Rule 20 failure; any gap in proposal coverage
- Flags for Next Step: plan moves to Done; CEO Gate 1 review of classification quality is the next session's opening work

**Deposits:**
- `knowledge/development/dev-log-lessons-forge-cycle-step3-2026-05-27.md`

Standard prompt feedback protocol → `knowledge/research/agent-prompt-feedback.md`.

---

## How to run

Bellows dispatches Step 1 on next rescan. Step 1 ingests the cycle and pauses for verdict. Planner reads Step 1 deposit under Rule 22, verifies ingestion count and `needs_classification` queue split, deposits continue verdict. Bellows dispatches Step 2a, pauses for verdict. Planner reviews first-batch classification quality, deposits continue verdict. Bellows dispatches Step 2b, pauses for verdict. Planner reviews second-batch + cross-cutting observations, deposits continue verdict. Bellows dispatches Step 3, plan moves to Done. CEO Gate 1 review of classifications happens in a follow-up conversation.
