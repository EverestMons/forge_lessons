# Dev Log — classify-307-318 Step 1 (2026-08-11)

## A0 — Precondition Checks (fresh state, condition 3)

- `get_unclassified_entries` = `[307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318]` — exactly the twelve ✓
- PARSER_COUNT = 261 ✓
- LESSONS.md sha256 = `f79ea236bb2ca8614c4c3c96ea7ca04b8f6c56c1d63a91fd240e728dc0c64f69` — matches A1 pin ✓
- `lesson_proposals` MAX(id) = 314 ✓
- `lesson_entries` MAX(id) = 318 ✓
- Per-entry proposal coverage: all 12 entries have 0 proposals → fresh state confirmed

## A1 — Pins (verified)

- LESSONS.md sha256: `f79ea236bb2ca8614c4c3c96ea7ca04b8f6c56c1d63a91fd240e728dc0c64f69` ✓
- `lesson_proposals` MAX(id) = 314 ✓
- `lesson_entries` MAX(id) = 318 ✓

## B — Backup

- Backed up to `pre-classify-s36-20260811_235358.db` beside the DB
- Restorability by value (`?immutable=1`): `SELECT COUNT(*) FROM lesson_entries WHERE id BETWEEN 307 AND 318` → **BK=12** ✓

## Classification — 12 entries, 12 proposals inserted

| entry_id | proposal_id | category | confidence | target_layer | target_artifact | quote_ratio |
|---|---|---|---|---|---|---|
| 307 | 315 | instrumentation | high | governance | DRAFTING_CYCLE.md | 0.317 |
| 308 | 316 | governance_rule | high | governance | PLANNER_TEMPLATE.md | 0.248 |
| 309 | 317 | governance_rule | high | governance | DRAFTING_CYCLE.md | 0.363 |
| 310 | 318 | governance_rule | high | governance | DRAFTING_CYCLE.md | 0.165 |
| 311 | 319 | governance_rule | high | governance | DRAFTING_CYCLE.md | 0.270 |
| 312 | 320 | structural | high | structure | DRAFTING_CYCLE.md | 0.304 |
| 313 | 321 | governance_rule | high | governance | DRAFTING_CYCLE.md | 0.163 |
| 314 | 322 | governance_rule | high | governance | DRAFTING_CYCLE.md | 0.275 |
| 315 | 323 | governance_rule | high | governance | DRAFTING_CYCLE.md | 0.191 |
| 316 | 324 | governance_rule | high | governance | PLANNER_TEMPLATE.md | 0.124 |
| 317 | 325 | governance_rule | high | governance | PLANNER_TEMPLATE.md | 0.533 |
| 318 | 326 | governance_rule | high | governance | PLANNER_TEMPLATE.md | 0.446 |

All `changes()=1` per call. Running tally: 12 INSERTs, 0 failures.

### Flag Coverage

- **Flag (G) applied to all 12 entries** — each names its observable (mechanism-shaped)
- **Flag (D) entries (codified by v2.1–v2.4):**
  - 310: clone-diff timing — §2.6 already codified; entry argues for timing change
  - 312: collapse protocol — v2.4 codifies repeated-folds-on-one-region-means-delete; entry adds collapse technique
  - 313: reclassification control-flow diff — v2.3 codifies sequential-lens requirement; entry adds proactive prevention
  - 315: walk-0 context pin — v2.4 codifies this directly; entry is the source

### Quote-Ratio Report

Method (Rule 61 ext.): character count of verbatim-copied entry text (substrings of length ≥20 matched against suggested_action+reasoning) over total proposal text character count, agent-computed per proposal.

- Range: 0.124–0.533
- Batch max: 0.533 (entry 317, proposal 325)
- Ceiling: 0.800
- All proposals within ceiling ✓

## Capture + Sentinels

### Pre-State
- proposals COUNT: 314
- proposals MAX(id): 314
- `COUNT(*) WHERE id<=314 AND status<>'proposed'`: 314

### Post-State
- proposals COUNT: 326
- proposals MAX(id): 326
- POST_UNCLASSIFIED: 0
- new proposals (id>314) all `status='proposed'`, `route` NULL

### Delta
- proposals COUNT: 314 → 326 (+12)
- proposals MAX(id): 314 → 326
- INSERT-only proven: `COUNT(*) WHERE id<=314 AND status<>'proposed'` unchanged (314 → 314) ✓

## Report

- Generated: `reports/lessons-report-2026-08-11.md`
- Surfaces: 12 proposals (≥12 ✓)

## Receipt

- **WORKLIST:** `[307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318]` (n=12)
- **PARSER_COUNT:** 261
- **BK:** 12 (pre-classify-s36-20260811_235358.db, `?immutable=1`)
- **INSERTED:** 12 (changes()=1 per call, running tally, final count)
- **ENTRIES_COVERED:** [307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318] (all 12, each ≥1 proposal)
- **POST_UNCLASSIFIED:** 0
- **PROPOSALS_MAX_POST:** 326

### Ledger Updates

#### Prompt Feedback

None.

#### Forward Register

NONE.
