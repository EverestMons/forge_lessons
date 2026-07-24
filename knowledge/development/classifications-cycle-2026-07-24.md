# Classifications — Cycle 2026-07-24 (DRAFTING_CYCLE.md refinement batch)

**Cycle date:** 2026-07-24
**Batch size:** 4 entries (ids 179–182)
**All entries target:** `DRAFTING_CYCLE.md`

## Cycle Dict (verbatim)

```
ingested_count: 4
updated_count: 0
unchanged_count: 121
duplicates_marked_count: 0
needs_classification: [179, 180, 181, 182]
terminal_proposals_flagged: []
cycle_timestamp: 2026-07-24T22:47:41.285263+00:00
```

## Per-Entry Classifications

### Entry 179 → Proposal 187
**Category:** governance_rule | **Confidence:** high | **Status:** proposed
**target_layer:** governance | **target_artifact:** DRAFTING_CYCLE.md

**Source heading:** 2026-07-24: The Drafting Cycle's five lenses are written for executables — a read-only diagnostic under-exercises Destruction and ACID, which need diagnostic-mode residues

**Suggested action:** Amend DRAFTING_CYCLE.md §2.2 (Destruction) and §2.5 (ACID) to add diagnostic-mode residues — sub-questions tailored to read-only, non-mutating plans — the way §2.1 already carries a diagnostic-tailored sub-question (1.4). Keep the five-lens count per §6's "add a sub-question" amendment shape.

**Reasoning:** Entry 179 reports running the codified cycle on a "real read-only, single-step DIAGNOSTIC" and finding "§2's lens content is executable-primary. Two lenses mis-fit." Specifically: "§2.2 Destruction's skip-condition — 'only a pure-additive plan touching no existing behaviour' — does not map to a diagnostic: a diagnostic is non-mutating, not 'additive'" and "§2.5 ACID's Isolation sub-question (5.3) is built on a multi-step verdict-gated schedule and is structurally empty for a single-step diagnostic." The proposed fix is a documentary amendment to DRAFTING_CYCLE.md adding diagnostic-mode sub-questions.

---

### Entry 180 → Proposal 188
**Category:** governance_rule | **Confidence:** high | **Status:** proposed
**target_layer:** governance | **target_artifact:** DRAFTING_CYCLE.md

**Source heading:** 2026-07-24: §2 implies but does not STATE "run each lens against the prior lens's folded draft, never batch" — the gap let the Planner batch a walk twice in one session

**Suggested action:** Amend DRAFTING_CYCLE.md §2 to add an explicit clause: "Run each lens against the draft as folded by the prior lens; do NOT analyze all lenses against one draft and batch the folds." Name the recurring rationalization ("this pass is just confirmation, so cumulation doesn't matter here") as a self-check target.

**Reasoning:** Entry 180 states "DRAFTING_CYCLE.md §2 says 'one pass per lens per walk, fold after each pass, re-run a lens only on a subsequent walk' — which IMPLIES each lens runs against the draft as folded by the prior lens" but "it is implicit enough that the Planner batched all five lenses against one draft (losing a real finding — a fork lens 1 added was never seen by lenses 2/3 because they read the pre-fold draft)." It also notes a second instance: "proposed batching the closing walk as 'just verification, nothing to fold.' A confirming/expected-dry pass is still a walk." The fix is making the implicit sequential-execution rule explicit in the governance document.

---

### Entry 181 → Proposal 189
**Category:** governance_rule | **Confidence:** high | **Status:** proposed
**target_layer:** governance | **target_artifact:** DRAFTING_CYCLE.md

**Source heading:** 2026-07-24: The §4 plan_lint closing-line self-check is a gameable substring heuristic — it should read the last lens line's status, not the closing prose

**Suggested action:** Amend DRAFTING_CYCLE.md §4 closing-line self-check to read the LAST LENS line's status (structured "- ACID: … w3 dry") instead of keyword-guessing the closing prose. Coordinate the §4 text change with a `bellows/scripts/plan_lint.py` edit and its tests per §6 ("keep the self-check in lockstep").

**Reasoning:** Entry 181 identifies "DRAFTING_CYCLE.md §4's 'closing asserts a dry lens pass' self-check is implemented in bellows/scripts/plan_lint.py as 'if 'fold' in closing_text and 'dry' not in closing_text: WARN'" and finds "two brittle consequences": "a genuinely bad close that happens to contain 'dry' (e.g. 'last event was a fold, not dry') PASSES; and a good closing line reporting the fold COUNT (e.g. '16 folds across 3 walks') only passes because it also says 'dry.'" The proposed fix is structural — read the last lens line's status rather than keyword-matching prose — but the primary artifact is the §4 governance text, with `plan_lint.py` as a coordinated gate edit.

**Doc+gate coupling:** This entry implicates both `DRAFTING_CYCLE.md` (§4 text) and `bellows/scripts/plan_lint.py` (the implementing gate). Gate 2 should pair both edits per §6.

---

### Entry 182 → Proposal 190
**Category:** governance_rule | **Confidence:** high | **Status:** proposed
**target_layer:** governance | **target_artifact:** DRAFTING_CYCLE.md

**Source heading:** 2026-07-24: DRAFTING_CYCLE.md §3's own T0 cycle_tier format example TRIPS the §4 plan_lint regex — a live doc-vs-gate contradiction

**Suggested action:** Fix the DRAFTING_CYCLE.md §3-vs-§4 contradiction: §3's T0 format example ("cycle_tier: T0 (no trigger); integration-vs-record pass: <result>.") trips §4's regex (re.match(r'^T([012])$')). Either loosen the regex to ^T([012])\b or change the §3 example to a bare "cycle_tier: T0" with the result on the next line. Coordinate the doc fix with a `bellows/scripts/plan_lint.py` regex edit + test per §6.

**Reasoning:** Entry 182 reports "§3 specifies the T0 collapsed form as, verbatim: '**cycle_tier:** T0 (no trigger); integration-vs-record pass: <result>.' — explanation on the same line as the tier token. But §4's gate (plan_lint.py) reads the whole header value and matches re.match(r'^T([012])$', cycle_tier_raw), which requires the value to be EXACTLY T0/T1/T2." Found live: "a T0 plan's first draft used the §3 form and WARNed; a bare '**cycle_tier:** T0' (result moved to the next line) passed clean. This is exactly the doc-vs-gate coordination hazard §6 names."

**Doc+gate coupling:** This entry implicates both `DRAFTING_CYCLE.md` (§3 example text + §4 description) and `bellows/scripts/plan_lint.py` (the regex). Gate 2 should pair both edits per §6.

---

## Gate 1 Cluster Synthesis

### DRAFTING_CYCLE.md refinements (4 entries)

All four entries propose amendments to `DRAFTING_CYCLE.md`, the single-source governance file for the Drafting Cycle (v1.0; PLANNER_TEMPLATE.md v4.80 is a 7-line pointer). The batch divides into two sub-groups:

**Sub-group A — Lens content gaps (entries 179, 180):**
- Entry 179: §2.2 (Destruction) and §2.5 (ACID) lack diagnostic-mode residues; their lens content is executable-primary.
- Entry 180: §2's sequential-lens-execution rule is implicit, not stated, enabling a batch-all-lenses error twice in one session.

Both are pure doc amendments — no code coupling.

**Sub-group B — Doc+gate coordination (entries 181, 182):**
- Entry 181: §4's closing-line self-check (implemented in `plan_lint.py`) is a gameable substring heuristic; should read the last lens line's structured status instead.
- Entry 182: §3's T0 format example trips §4's regex — a live doc-vs-gate contradiction §6 names.

Both entries name the `bellows/scripts/plan_lint.py` coupling explicitly. Gate 2 should pair each doc edit with the corresponding `plan_lint.py` code + test edit per §6 ("keep the self-check in lockstep with §1/§3").

**No ambiguous classifications.** All 4 are `governance_rule` / `high` confidence.
