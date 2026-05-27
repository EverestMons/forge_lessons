# Executable: Lessons Forge Cycle 2026-05-27 — Phase 2A Batch 2 Recovery (entries 76-93)

**Plan slug:** executable-lessons-forge-cycle-batch2-recovery-2026-05-27
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

The original cycle plan `executable-lessons-forge-cycle-2026-05-27` halted at Bellows-step-3 (which positionally aligned with the plan's `## STEP 2B` header). Cause: non-monotonic STEP labels (1 / 2A / 2B / 3) violated Bellows' positional step-parser contract. The agent dispatched against the literal `## STEP 3` prompt (the closeout step) and correctly refused — the closeout's prerequisite (Step 2B classification deposit) was missing.

**State preserved from the halted run:**
- Step 1 (deterministic cycle): COMPLETE. 36 entries ingested as IDs 58-93. Deposit: `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md`.
- Step 2a (batch 1: entries 58-75): COMPLETE. 18 proposals inserted as IDs 63-80, all status='proposed'. Deposit: `knowledge/research/lessons-forge-cycle-step2a-classifications-2026-05-27.md`.
- Step 2b (batch 2: entries 76-93): NOT EXECUTED. This is the work this plan recovers.
- Step 3 (closeout + PROJECT_STATUS): NOT EXECUTED. Will be authored after this plan closes.

**Pre-state baseline for this plan (live DB):**

| Metric | Value |
|---|---|
| lesson_entries (total) | 93 (was 57 pre-cycle; ingestion added 36) |
| lesson_proposals (total) | 80 (was 62 pre-cycle; Step 2a added 18) |
| Proposals at status='proposed' | 18 (the Step 2a batch awaiting Gate 1) |
| Proposals at status='accepted' | 0 |
| Entries 76-93 with existing proposals | 0 (this is the work) |

**Scope:** This plan executes the single missed batch — classify entries 76-93. Output identical in shape to the Step 2a deposit. Single STEP, single agent invocation. Closeout (PROJECT_STATUS update) is deferred to a separate follow-up plan.

## API reference (verified against `src/lessons_forge.py` 2026-05-27)

- `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, status='proposed', target_layer=None, target_artifact=None, duplicate_of=None, subcategory=None) → proposal_id`
  - `category` ∈ {`structural`, `instrumentation`, `governance_rule`, `language`, `narrative`, `duplicate`}
  - `confidence` ∈ {`low`, `medium`, `high`}
  - `status` ∈ {`proposed`, `accepted`, `rejected`, `ambiguous`, `stale`, `superseded`, `implemented`}
  - `target_layer` ∈ {`structure`, `governance`, `language`, `none`} or `NULL`
  - Does NOT call `conn.commit()` — caller must commit.
  - **Agent MUST NOT assign `category='duplicate'`** — reserved for deterministic `detect_duplicates()`.

---

## STEP 1 — Forge Lessons Agent: Classify Batch 2 (entries 76-93)

You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` in full — it is the authoritative reference for the ADR-002 taxonomy and edge-case handling. Also read `knowledge/research/lessons-forge-cycle-step1-2026-05-27.md` (the deterministic cycle deposit from the halted plan) — its Section 5 has the explicit Step 2b batch IDs and Section 4 has the queue listing with headings and tags. Skip glossary read — no domain glossary.

All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge`.

**Sub-step 1.0 — Load batch 2 entries.** Use `Filesystem:write_file` to create scratch file `load_entries.py` at repo root:

```python
import sqlite3, json

# Batch 2 entry IDs from step1 deposit Section 5
ENTRY_IDS = [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]

conn = sqlite3.connect("lessons-forge.db")
conn.row_factory = sqlite3.Row

placeholders = ",".join("?" * len(ENTRY_IDS))
rows = conn.execute(
    f"SELECT id, entry_date, source_heading, raw_content, tags "
    f"FROM lesson_entries WHERE id IN ({placeholders}) ORDER BY id",
    ENTRY_IDS,
).fetchall()

assert len(rows) == 18, f"Expected 18 entries, got {len(rows)}"

entries = [{"id": r["id"], "entry_date": r["entry_date"], "source_heading": r["source_heading"],
            "raw_content": r["raw_content"], "tags": r["tags"]} for r in rows]

with open("classification_input.json", "w") as f:
    json.dump(entries, f, indent=2)

print(f"Loaded {len(entries)} entries (IDs 76-93) to classification_input.json")
conn.close()
```

Run: `python3 load_entries.py`.

**Sub-step 1.1 — Classify each entry (you ARE the classifier).**

Read `classification_input.json`. For EACH of the 18 entries:

**(a) Read the entry's `source_heading`, `raw_content`, and `tags`.** Tags often pre-suggest classification (e.g., `[tag: planner-discipline, rule-22]` suggests `governance_rule` or `instrumentation`).

**(b) Apply the ADR-002 six-category taxonomy:**

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

**(c) Produce a classification dict per entry:**

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

**Sub-step 1.2 — Persist classifications.** Create scratch file `persist.py`:

```python
import sqlite3
from src.lessons_forge import insert_proposal

CLASSIFICATIONS = [
    # Fill with classification dicts from sub-step 1.1, one per entry
]

assert CLASSIFICATIONS, "fill CLASSIFICATIONS"
assert len(CLASSIFICATIONS) == 18, f"Expected 18 classifications, got {len(CLASSIFICATIONS)}"

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
print(f"Inserted {len(inserted)} proposals (batch 2 recovery):")
for entry_id, pid, cat, status in inserted:
    print(f"  entry {entry_id} → proposal {pid} ({cat}, {status})")
conn.close()
```

Edit `CLASSIFICATIONS` with the full list, run `python3 persist.py`, capture output.

**Sub-step 1.3 — Cleanup.** `rm load_entries.py persist.py classification_input.json`.

**Sub-step 1.4 — Commit.** `git add lessons-forge.db && git commit -m "feat: lessons forge 2026-05-27 — Phase 2A batch 2 recovery (entries 76-93)"`. Use `git add -f lessons-forge.db` if gitignored.

**Deposit:** `knowledge/research/lessons-forge-cycle-batch2-recovery-2026-05-27.md` with sections:
1. Batch metadata (entry ID range, count = 18, recovery context)
2. **Classification table** — one row per entry: `entry_id`, `category`, `confidence`, `target_layer`, `target_artifact`, `status`, `suggested_action` (truncated to ~80 chars)
3. **Distribution summary** — category counts within this batch, confidence breakdown
4. **Cross-cutting observations within batch** — patterns the agent noticed
5. **Cross-batch observations** — patterns spanning Step 2a batch (proposals 63-80, entries 58-75) plus this batch (entries 76-93). This is the human-review hook for CEO Gate 1.
6. **Ambiguous / low-confidence entries** — with reasoning
7. Output Receipt with status Complete

**Output Receipt:**
- Agent: Forge Lessons Agent
- Step: 1
- Status: Complete (18 proposals inserted with non-duplicate category); Partial (one or more entries flagged ambiguous, still Complete unless persistence failed); Blocked (CHECK constraint violation or FK violation during persist)
- What Was Done: classified 18 entries (IDs 76-93) via ADR-002 taxonomy, persisted via `insert_proposal`, produced cross-batch synthesis
- Files Deposited: `knowledge/research/lessons-forge-cycle-batch2-recovery-2026-05-27.md`
- Files Created or Modified: `lessons-forge.db` (committed)
- Decisions Made: 18 classification tuples + cross-batch synthesis
- Flags for CEO: ambiguous entries needing CEO judgment; any cross-batch patterns warranting CEO attention; any cluster suggesting a meta-pattern across the full 36-entry cycle
- Flags for Next Step: closeout plan (separate, follow-up) will update PROJECT_STATUS and verify all 36 entries have proposals

**Deposits:**
- `knowledge/research/lessons-forge-cycle-batch2-recovery-2026-05-27.md`

Standard prompt feedback protocol → `knowledge/research/agent-prompt-feedback.md`.

---

## How to run

Bellows dispatches Step 1 on next rescan. Pauses for verdict at completion. Planner reads deposit under Rule 22, verifies classifications quality and cross-batch synthesis, deposits continue verdict. Plan moves to Done. Closeout plan (PROJECT_STATUS update) will be authored separately after this plan closes.
