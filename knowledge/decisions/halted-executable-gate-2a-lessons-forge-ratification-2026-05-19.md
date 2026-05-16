# Executable: Gate 2a — Lessons Forge Cycle 2026-05-18 Ratification

**Plan slug:** executable-gate-2a-lessons-forge-ratification-2026-05-19
**Plan type:** executable
**Project:** lessons-forge
**Specialist:** Forge Developer
**Auto-close:** false
**Pause for verdict:** after_step_1
**Priority:** 1
**Depends on:** none
**Created:** 2026-05-19

---

## Context

Gate 1 review of the Lessons Forge cycle 2026-05-18 dispositioned 25 new proposals + 1 pre-existing proposal touch. The Gate 1 decision matrix is the authoritative source:

- **Deposit:** `lessons-forge/knowledge/research/gate-1-decisions-2026-05-18.md`
- **Cycle report:** `lessons-forge/reports/lessons-report-2026-05-18.md`

This plan ratifies the dispositions in `lessons-forge.db` by updating `lesson_proposals.status` for each affected row. No code changes, no schema changes — DB writes only.

**Count reconciliation (Planner-resolved 2026-05-19):** The decision matrix has internal count inconsistencies — the Summary table says "Accept: 20" and the Governance sub-header says "13", but the body tables list 2 structural + **11** governance + 5 instrumentation = **18 accepted**. The 11-count is authoritative (matches the row enumeration in the matrix and matches the CEO's own Gate 2b sizing of "11 rules + 5 procedures"). The Summary's 20 and the sub-header's 13 are authoring errors in the matrix; this plan operates against the body-table row enumeration.

**Two-step structure:**

- **Step 1 — Manifest.** Agent reads the decision matrix + cycle report + DB, derives the `(proposal_id, target_status, status_updated_by, duplicate_of)` mapping for all 26 row touches, and deposits a JSON manifest. **No DB writes.** Plan pauses for Planner verdict.
- **Step 2 — Apply.** After verdict, agent reads the manifest and executes the updates inside a single transaction, then verifies status distribution.

**Why two-step:** mapping the Gate 1 disposition labels (G1, S1, I1, etc.) to actual `lesson_proposals.id` values is the part of this plan most likely to be wrong. Catching a mapping error before any write costs one extra verdict gate; catching it after writes costs a follow-up correction plan plus a status audit.

**Row-touch count (26):**
- 18 new proposals → `accepted`
- 2 new proposals → `deferred`
- 5 new proposals → `rejected`
- 1 pre-existing proposal (ID 38) → `superseded`

The matrix calls this "27 dispositions" because it counts CEO sub-decisions per Gate 1 entry (G16's "supersedes ID 38" and G17's "duplicate of G16" are sub-decisions on existing rows, not separate row touches).

**G16 special handling:** G16's new proposal is `accepted` AND its `duplicate_of` column is set to 38 (per the decision matrix: "G16 also supersedes the pre-existing `proposed` proposal ID 38"). Pre-existing proposal ID 38 itself transitions to `superseded`.

---

## Step 1 — Derive ratification manifest

You are the Forge Developer. Read `forge/agents/FORGE_DEVELOPER.md` and `lessons-forge/CLAUDE.md`. Operate against the lessons-forge repo at `/Users/marklehn/Developer/GitHub/lessons-forge/`. Database is `lessons-forge.db` (not forge.db).

**Inputs (read all three before writing):**

- `lessons-forge/knowledge/research/gate-1-decisions-2026-05-18.md` — Gate 1 decision matrix
- `lessons-forge/reports/lessons-report-2026-05-18.md` — cycle report listing the 25 new proposals with their IDs
- `lessons-forge.db`, table `lesson_proposals` — verify each proposal_id you map exists and is in the expected pre-write status

**Task:**

For each Gate 1 disposition in the decision matrix, derive the mapping `(proposal_id, target_status, status_updated_by, duplicate_of)`. The decision matrix uses labels (G1..G17, S1..S2, I1..I6); the cycle report lists proposals with their numeric IDs and source entry dates/headings. Cross-reference both to get the right proposal_id for each label.

**The Planner has reconciled the matrix's count inconsistencies — operate against the body-table row enumeration, not the Summary or sub-header counts. Specifically: 18 accepted (S1, S2, G1, G2, G3, G4, G6, G7, G8, G9, G10, G11, G16, I1, I2, I4, I5, I6).**

**Mapping rules:**

1. **Accepted (18 labels):** S1, S2, G1, G2, G3, G4, G6, G7, G8, G9, G10, G11, G16, I1, I2, I4, I5, I6
   - Target status: `accepted`
   - status_updated_by: `ceo`
   - duplicate_of: null EXCEPT for G16, where duplicate_of = 38

2. **Deferred (2 labels):** G5, I3
   - Target status: `deferred`
   - status_updated_by: `ceo`
   - duplicate_of: null

3. **Rejected (5 labels):** G12, G13, G14, G15, G17
   - Target status: `rejected`
   - status_updated_by: `ceo`
   - duplicate_of: For G12/G13/G14/G15, set to the prior implemented proposal_id named in the matrix (34/35/36/37 respectively). For G17, set to G16's proposal_id (the internal duplicate the matrix names).

4. **Pre-existing proposal ID 38:**
   - Target status: `superseded`
   - status_updated_by: `ceo`
   - duplicate_of: G16's proposal_id

**Verification before deposit:**

For each mapped proposal_id, run `SELECT id, entry_id, category, status, status_updated_at FROM lesson_proposals WHERE id = ?` and confirm:
- For new proposals (S/G/I labels): row exists with `status = 'proposed'`
- For pre-existing ID 38: `status = 'proposed'`
- For pre-existing IDs 34/35/36/37: `status = 'implemented'` (these are the targets of G12-G15's `duplicate_of`, no write happens against these rows, just referential verification)

If any mapped ID does not exist or is in an unexpected pre-write state, halt and flag — do not deposit the manifest.

**Sanity checks:**

- Count rows in the manifest by target_status. Must equal: accepted=18, deferred=2, rejected=5, superseded=1. Total: 26 row touches.
- For G16 and ID 38, verify the cross-reference (G16's manifest entry has `duplicate_of = 38`; ID 38's manifest entry has `duplicate_of = <G16's id>`) is internally consistent.

**Deposit format (JSON):**

```json
{
  "plan_slug": "executable-gate-2a-lessons-forge-ratification-2026-05-19",
  "step": 1,
  "decision_matrix_source": "lessons-forge/knowledge/research/gate-1-decisions-2026-05-18.md",
  "planner_count_reconciliation": "matrix Summary says 20 accepted; body tables list 18; this manifest operates on 18 per Planner authoring decision 2026-05-19",
  "row_counts": {
    "accepted": 18,
    "deferred": 2,
    "rejected": 5,
    "superseded": 1,
    "total": 26
  },
  "mappings": [
    {
      "gate_1_label": "S1",
      "proposal_id": 0,
      "entry_date": "2026-05-18",
      "source_heading_snippet": "first 60 chars",
      "current_status": "proposed",
      "target_status": "accepted",
      "status_updated_by": "ceo",
      "duplicate_of": null
    }
  ],
  "verification": {
    "all_mapped_ids_exist": true,
    "all_new_proposals_currently_proposed": true,
    "id_38_currently_proposed": true,
    "ids_34_35_36_37_currently_implemented": true,
    "g16_duplicate_of_38_consistent": true,
    "id_38_duplicate_of_g16_consistent": true
  }
}
```

Deposit to: `lessons-forge/knowledge/development/gate-2a-ratification-manifest-2026-05-19.json`

Also write a brief dev-log:

```markdown
# Dev Log — Gate 2a Step 1 (manifest derivation)

Read: <decision matrix path>, <cycle report path>, lessons-forge.db
Mapped: 26 row touches (18 accepted, 2 deferred, 5 rejected, 1 superseded)
Verification: <each check result>
Anomalies: <none, or list>
```

Deposit dev-log to: `lessons-forge/knowledge/development/dev-log-gate-2a-step-1-2026-05-19.md`

**No DB writes in this step.** Step 1 is mapping + verification only.

**Output Receipt:**
- Agent: Forge Developer
- Step: 1
- Status: Complete (only if all 26 mappings verified with no anomalies); Blocked (if any verification check failed)
- What Was Done: derived ratification manifest for 26 row touches
- Files Deposited: `lessons-forge/knowledge/development/gate-2a-ratification-manifest-2026-05-19.json`, `lessons-forge/knowledge/development/dev-log-gate-2a-step-1-2026-05-19.md`
- Files Created or Modified: none in DB; no commits
- Decisions Made: 26 (proposal_id, target_status) mappings
- Flags for CEO: any disposition where the matrix label was ambiguous; any verification anomaly
- Flags for Next Step: Planner Rule 22 read of manifest; on continue verdict, Step 2 applies the writes

**Deposits:**
- `lessons-forge/knowledge/development/gate-2a-ratification-manifest-2026-05-19.json`
- `lessons-forge/knowledge/development/dev-log-gate-2a-step-1-2026-05-19.md`

**STOP.** Do NOT move the plan to Done. Do NOT proceed to Step 2.

---

## Step 2 — Apply ratification writes

You are the Forge Developer. Before starting, read the prior step's deposit at `lessons-forge/knowledge/development/gate-2a-ratification-manifest-2026-05-19.json` and verify its Output Receipt status is Complete. If not, stop and report.

**Inputs:**
- `lessons-forge/knowledge/development/gate-2a-ratification-manifest-2026-05-19.json` (Step 1 deposit, Planner-verified)
- `lessons-forge.db`

**Task:**

Inside a single transaction, apply all 26 row updates from the manifest's `mappings` array. Each update is:

```sql
UPDATE lesson_proposals
SET status = ?,
    status_updated_by = ?,
    status_updated_at = ?,
    duplicate_of = CASE WHEN ? IS NOT NULL THEN ? ELSE duplicate_of END
WHERE id = ?
```

The CASE expression: if the manifest's duplicate_of is null, leave the existing value alone; if it's a value, write that value. Pass `manifest_duplicate_of` to both `?` placeholders inside the CASE.

Use a single ISO-8601 UTC timestamp for `status_updated_at` across all rows (capture once at start of transaction).

**Post-write verification (inside the same transaction, before commit):**

1. Query status distribution: `SELECT status, COUNT(*) FROM lesson_proposals GROUP BY status`. Confirm the deltas match expected:
   - accepted: +18 from pre-write count
   - deferred: +2
   - rejected: +5
   - superseded: +1
   - proposed: -26 (all touched rows leave proposed state)
   - other statuses (implemented, ambiguous, stale): unchanged

2. For each mapped proposal_id in the manifest, re-query the row and confirm status, status_updated_by, status_updated_at, duplicate_of match the manifest.

3. Re-check G16/ID 38 cross-reference: G16's row has `duplicate_of = 38`; ID 38's row has `duplicate_of = <G16's id>`; both have `status` matching the manifest (`accepted` for G16, `superseded` for ID 38).

If all three verifications pass: COMMIT. If any fails: ROLLBACK and report.

**Commit (git):**

```bash
cd /Users/marklehn/Developer/GitHub/lessons-forge && git --no-pager add lessons-forge.db && git --no-pager commit -m "feat: lessons forge cycle 2026-05-18 gate 2a — 26 ratifications (18 accepted, 2 deferred, 5 rejected, 1 superseded)"
```

**Dev log:**

```markdown
# Dev Log — Gate 2a Step 2 (ratification apply)

Transaction: <start ISO>, <end ISO>
Status distribution before: <pre-write counts>
Status distribution after: <post-write counts>
Deltas: accepted +18, deferred +2, rejected +5, superseded +1, proposed -26
G16/ID 38 cross-reference: verified consistent
Commit: <SHA>
Anomalies: <none, or list>
```

Deposit to: `lessons-forge/knowledge/development/dev-log-gate-2a-step-2-2026-05-19.md`

**Rule 20 self-check (literal banner, no decoration):**

```python
import os
required = [
    "knowledge/development/gate-2a-ratification-manifest-2026-05-19.json",
    "knowledge/development/dev-log-gate-2a-step-1-2026-05-19.md",
    "knowledge/development/dev-log-gate-2a-step-2-2026-05-19.md",
]
missing = [f for f in required if not os.path.exists(f)]
if missing:
    print(f"FAILED - missing evidence: {missing}")
else:
    print("PASSED - SELF-CHECK PASSED - all evidence files present, no hedging keywords found.")
```

Render the banner inside a fenced code block with NO surrounding shell-prompt prefix, NO `===` separator lines, NO title line, NO summary line — just the literal banner output, fenced. (See LESSONS.md 2026-05-18 strike-5 entry.)

**Output Receipt:**
- Agent: Forge Developer
- Step: 2
- Status: Complete (all 26 updates applied, verifications passed, commit landed); Blocked (transaction rolled back due to verification failure)
- What Was Done: applied 26 ratification updates to lesson_proposals; committed lessons-forge.db
- Files Deposited: `lessons-forge/knowledge/development/dev-log-gate-2a-step-2-2026-05-19.md`
- Files Created or Modified: `lessons-forge.db` (data only, no schema), commit `<SHA>`
- Decisions Made: 26 row updates applied
- Flags for CEO: any anomaly during apply or verification
- Flags for Next Step: cycle bookkeeping closed; next gate is Gate 2c

**Deposits:**
- `lessons-forge/knowledge/development/dev-log-gate-2a-step-2-2026-05-19.md`

Standard prompt feedback protocol → `lessons-forge/knowledge/research/agent-prompt-feedback.md`.

---

## How to run

Bellows dispatches automatically once this plan lands in `lessons-forge/knowledge/decisions/`. Step 1 runs, deposits the manifest, and pauses for verdict. The Planner reads the manifest under Rule 22, verifies the 26 mappings against the decision matrix in conversation with the CEO, then deposits a continue verdict to `bellows/verdicts/resolved/verdict-executable-gate-2a-lessons-forge-ratification-2026-05-19-step-1.md` (bare format: `verdict: continue` on line 1). Step 2 then runs end-to-end and Bellows moves the plan to Done.
