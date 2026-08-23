# Learned Promotion Diagnostic — 2026-08-23

**Diagnostic:** Which LESSONS.md entries are ENFORCED? Establish the `learned` promotion set.

**Corpus identity:** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — 1,593,344 bytes, `lesson_entries` = 370 rows (E confirmed).

**Symbol table verification:** N=327, X=239, P=74, Q=14 (=327−239−74). All confirmed via grep against `/Users/marklehn/Developer/GitHub/LESSONS.md`.

---

## Q1 — Enforcement Surface Inventory

### Gates (`bellows/gates.py`) — 9 blocking, 1 informational, 1 utility

| # | Gate | Rule enforced | Character |
|---|------|--------------|-----------|
| G1 | `_gate_receipt_status` (line 241) | Agent receipt status must be "Complete" | Blocking |
| G2 | `_gate_ceo_flags` (line 247) | Agent must not raise CEO-escalation flags | Blocking |
| G3 | `_gate_no_errors` (line 253) | Agent run must not error out | Blocking |
| G4 | `_gate_no_permission_denials` (line 261) | Agent must not be denied non-read-class tool permissions | Blocking |
| G5 | `_gate_deposit_exists` (line 405) | Every plan-declared deposit must exist on disk and be committed | Blocking |
| G6 | `_gate_rule_20_self_check` (line 551) | QA report must contain Rule 20 banner with PASSED status | Blocking (QA steps only) |
| G7 | `_gate_rule_22_verification` (line 605) | QA verification tables must have positive status, no hedging | Blocking |
| G8 | `_gate_qa_test_result` (line 733) | Test failures must not exceed `known_failures` threshold | Blocking (QA steps only) |
| G9 | `_gate_scope_check` (line 850) | Agent must not modify files outside declared Scope | Blocking |
| G10 | `_gate_file_change_audit` (line 844) | Records files changed (passthrough) | Informational |
| G11 | `_gate_is_qa_step` (line 803) | Predicate: is this step a QA step? | Utility (not a gate) |

### plan_lint.py — 10 checks (4 blocking/FAIL, 6 WARN-only)

| # | Check | Rule enforced | Character |
|---|-------|--------------|-----------|
| L-a | Header parse | `dispatch_mode` ∈ {bellows, manual_bootstrap}; `pause_for_verdict` ∈ recognized set | Blocking (FAIL) |
| L-b | Deposits block | Steps mentioning "deposit" must yield parseable Deposits paths | Blocking (FAIL) |
| L-c | QA banner pair | QA plans must contain both Rule 20 strings | Blocking (FAIL) |
| L-d | Scope block | Present `**Scope:**` blocks must parse to ≥1 entry | Blocking (FAIL) |
| L-e | Step heading case | Must use uppercase `## STEP N`, not `## Step N` | Blocking (FAIL) |
| L-f | Drafting Cycle | T1+ plans need DC block with required lenses, closing line | WARN |
| L-g | Ledger ordering | C-ledger entries must be ascending | WARN |
| L-h | Stale closing | Contradiction: lens results recorded but Closing claims "no lens has read" | WARN |
| L-i | on_failure coupling | `pause_for_verdict=on_failure` requires parseable `qa_steps` | Blocking (FAIL) |
| L-j | Inherited premise | Flags `[INHERITED FROM N — NOT RE-EXECUTED]` markers | WARN |
| L-k | Clone-claim | Clone-framed plan must name newest same-class comparison | WARN |
| L-l | Clone-mutation | Clone-framed plan firing T-2 at tier < T2 | WARN |
| L-n | Non-F grep | `grep` on literal pattern without `-F` flag | WARN |
| L-o1 | Input path existence | Paths mentioned in plan should exist on disk | WARN |
| L-o2 | Deposits form | Deposits entries should be project-prefixed or absolute | WARN |
| L-p | C-ledger executable | C-ledger entry without backtick-quoted command | WARN |
| L-q | Pin verification | SHA256/git pins verified against disk | WARN |

**Note:** WARN-only checks are NOT enforcement mechanisms — they are advisory and do not cause plan_lint to exit non-zero. Only checks that produce FAIL results and contribute to exit 1 are counted as mechanisms.

### Checker scripts (`bellows/scripts/`) — 3 real enforcers, 3 non-enforcers

| # | Script | Rule enforced | Character |
|---|--------|--------------|-----------|
| S1 | `propagation_check.py` | Internal numeric/ordering consistency within a plan | Blocking (exit 1 on divergence) |
| S2 | `cycle_check.py` | Drafting cycle diminishing-returns bar (CONTINUE/BAR_MET/ESCALATE) | Blocking (exit 1 on ESCALATE) |
| S3 | `fold_check.py` | Fold must not change artifact's machine-readable state | Blocking (exit 1 on drift) |
| — | `walk_register_lint.py` | Walk-register table validation | Non-enforcer (WARN-only, exit 0) |
| — | `check_backlog_freshness.py` | Stale backlog detection | Non-enforcer (halted experiment, reference-only) |
| — | `cycle_yields.py` | Cycle yield data extraction | Non-enforcer (data collector, not validator) |

### Hooks (`bellows/hooks/eluvian/`) — 1 blocker, 1 advisory, 2 support

| # | Hook | Rule enforced | Character |
|---|------|--------------|-----------|
| H1 | `wrap_stop_hook.py` | Session wrap ritual must be complete before stopping | Blocking (decision: block) |
| H2 | `wrap_debt_hook.py` | Surface prior wrap debt at session start | Advisory (always exit 0) |
| — | `wrap_arm_hook.py` | Arm the wrap completion lock | Support (fail-open) |
| — | `wrap_check.py` | Shared verifier for 4-repo wrap checklist | Support (used by H1/H2) |

### Tests as enforcement in own right (`test_lessons_forge.py`) — 8 tests

These tests ARE the enforcement — nothing else catches the violation. A test that guards a mechanism is NOT itself a mechanism; the mechanism is. These 8 fall on the enforcement side of that line.

| # | Test | Property enforced |
|---|------|------------------|
| T1 | `test_key_heading_annotated_matches_unannotated` | Annotated heading produces same key as unannotated form |
| T2 | `test_hash_trailing_separator_invariant` | Trailing `---` separator does not change content hash |
| T3 | `test_hash_substantive_edit_changes_hash` | Normalization does not over-collapse distinct content |
| T4 | `test_raw_content_stored_verbatim_with_separator` | Normalization is hash-only, not storage-level |
| T5 | `test_terminal_status_guard` | Terminal-status proposals never silently staled |
| T6 | `test_trailing_separator_only_delta_zero_stales` | Separator-only delta produces zero stales |
| T7 | `test_needs_classification_plus_duplicates_equals_total` | Partition invariant |
| T8 | `test_detect_duplicates_tag_substring_not_flagged` | Tags in prose not treated as structural tags |

**Total primary enforcement mechanisms (M):** 11 gates (9 blocking) + 5 blocking plan_lint checks + 3 checker scripts + 1 blocking hook + 8 enforcement-tests = **28 callable enforcement units**. The plan's D4 pin of M=36 counted 11 `_gate_` defs + 18 lettered checks + 7 scripts. My count differs because: (a) 2 of the 11 `_gate_` defs are not enforcement (G10 informational, G11 utility); (b) the 18 "lettered checks" conflates blocking FAIL checks with WARN-only checks — only 5 produce FAIL; (c) 4 of the 7 scripts are not enforcers (walk_register_lint, check_backlog_freshness, cycle_yields, plus migrate_config/migrate_orphan_verdicts are utilities); (d) I add 8 enforcement-in-own-right tests and 1 blocking hook. The plan's M was a walk-0 estimate; **my measured M is 28**.

---

## Q2 — Mechanism-to-Entry Mapping

### Direction 1: Mechanism → LESSONS.md entries

**G1 (`_gate_receipt_status`)**  
No entry fully states "receipt status must be Complete."  
Partly covered: entry 85/line 1551 ("Agents may emit the Output Receipt inside a tool call") [pending].

**G2 (`_gate_ceo_flags`)**  
NO ENTRY.

**G3 (`_gate_no_errors`)**  
No entry fully states the rule. Partly mentioned in passing at line 603.

**G4 (`_gate_no_permission_denials`)**  
Partly covered: entry at line 497 (log-mining methodology, not the gate rule itself).

**G5 (`_gate_deposit_exists`)**  
- Entry 98/line 29: "Name deposit file paths literally" [learned] — FULLY
- Entry 61/line 544: "Inline Deposits blocks with un-prefixed paths" [learned] — FULLY
- Entry 85/line 1168: "QA-step deposits blocks must declare exactly one .md" [learned] — FULLY
- Entry 90/line 1286: "Use Deposits blocks for ALL agent deposits" [learned] — FULLY
- Entry 231/line 2827: "Two gates over the same list pull in opposite directions" [learned] — FULLY

**G6 (`_gate_rule_20_self_check`)**  
- Entry 70/line 796: "QA-step prompts must reference RULE_20_SELF_CHECK_BLOCK.md" [learned] — FULLY
- Entry 109/line 227: "Strict Bellows convention strings must be copied" [learned] — PARTLY (item 2 covers banner)
- Entry 191/line 2259: "An honest QA failure passes the Rule 20 self-check" [learned] — FULLY
- Entry 120/line 1435: "Gate-enforced QA steps must be made unmissable" [learned] — FULLY
- Entry 184/line 2175: "Choose the QA Rule 20 self-check FORM by plan class" [learned] — FULLY

**G7 (`_gate_rule_22_verification`)**  
- Entry 96/line 17: "A QA 'full suite passes' headline" [learned] — PARTLY
- Entry at line 1130: "Rule 22 (d) hedging-keyword detector false-positive" [pending] — FULLY

**G8 (`_gate_qa_test_result`)**  
- Entry 121/line 1443: "Run the FULL test suite during DEV and Planner review" [learned] — PARTLY (names the gap this gate fills)

**G9 (`_gate_scope_check`)**  
- Entry 98/line 29: "Name deposit file paths literally — scope_check authorizes from named paths" [learned] — FULLY
- Entry 106/line 158: "scope_check false-positive on plan-required evidence files" [learned] — FULLY
- Entry 62/line 581: "scope_check trip identified the WRONG file" [learned] — PARTLY
- Entry 116/line 1377: "scope_check gate cannot evaluate plans that delegate file lists to a referenced blueprint" [bare/Q]

**L-a (dispatch_mode/pause_for_verdict validation)**  
- Entry 111/line 317: "Dispatch Mode: standard rejection" [learned] — FULLY
- Entry 89/line 1269: "pause_for_verdict accepts only three values" [learned] — FULLY
- Entry 119/line 1427: "pause_for_verdict must be validated" [learned] — FULLY

**L-b (deposits block parse)**  
- Entry 61/line 544: "Inline Deposits blocks" [learned] — FULLY
- Entry 90/line 1286: "Use Deposits blocks for ALL agent deposits" [learned] — FULLY

**L-c (QA banner pair)**  
- Entry 70/line 796: "QA-step prompts must reference RULE_20_SELF_CHECK_BLOCK.md" [learned] — FULLY

**L-e (step heading case)**  
- Entry 114/line 394: "Non-monotonic STEP header labels" [learned] — PARTLY (about header labels, not case specifically)

**L-i (on_failure coupling)**  
- Entry 140/line 1639: "qa_steps header is a step-number list, not a count" [learned] — FULLY

**S1 (propagation_check.py)**  
No entry fully states the rule. Partly: entry at line 4381 (propagation_check by name, but lesson is about when to run it).

**S2 (cycle_check.py)**  
- Entry 142/line 1663: "High-stakes executables get a drafting cycle" [learned] — FULLY

**S3 (fold_check.py)**  
- Entry 340/line 4085: "A fold's own prose can break a machine contract" [learned] — FULLY (cites proposals 347, 348)
- Entry 339/line 4077: "A fold is the only edit in the system with no post-condition" [learned] — PARTLY

**H1 (wrap_stop_hook.py)**  
No entry fully states "session wrap must be complete before stopping." Entry at line 3747 is PARTLY relevant.

**T1 (`test_key_heading_annotated_matches_unannotated`)**  
- Entry at line 4599: "A function that computes a LOOKUP KEY must be the identity" [pending] — FULLY

### Direction 2: Mechanisms with NO entry

These mechanisms enforce rules the corpus never captured:

| Mechanism | Rule | Finding |
|-----------|------|---------|
| G2 (`_gate_ceo_flags`) | No CEO flags raised | NO ENTRY |
| G3 (`_gate_no_errors`) | No errors in receipt | NO ENTRY (mentioned in passing only) |
| L-e (step heading case) | Uppercase `## STEP N` | NO ENTRY (L394 covers non-monotonic labels, not case) |
| S1 (`propagation_check.py`) | Internal numeric consistency | NO ENTRY |
| H1 (`wrap_stop_hook.py`) | Wrap ritual completion | NO ENTRY (L3747 is about the conflict, not the rule) |
| T5 (`test_terminal_status_guard`) | Terminal proposals never staled | NO ENTRY |
| T6 (`test_trailing_separator_only_delta_zero_stales`) | Separator-only delta = zero stales | NO ENTRY |

---

## Q3 — DEMONSTRATE THE FIRE

### DEMONSTRATED — violation constructed, mechanism observed rejecting it

**D1. `_gate_receipt_status`**  
Violation: `{'receipt_status': 'Incomplete'}`  
Rejection: `gate=receipt_status evidence=Incomplete`  
Positive control: `{'receipt_status': 'Complete'}` → failures=0

**D2. `_gate_ceo_flags`**  
Violation: `{'ceo_flags': ['Agent cannot resolve ambiguity']}`  
Rejection: `gate=ceo_flags evidence=Agent cannot resolve ambiguity`  
Positive control: `{'ceo_flags': ['none']}` → failures=0

**D3. `_gate_no_errors`**  
Violation: `{'is_error': True, 'error': 'agent crashed'}`  
Rejection: `gate=no_errors evidence=agent crashed`  
Positive control: `{'is_error': False}` → failures=0

**D4. `_gate_no_permission_denials`**  
Violation: `{'permission_denials': [{'tool_name': 'Bash', 'tool_input': {'command': 'rm -rf /'}}]}`  
Rejection: `gate=no_permission_denials evidence=1 blocking denial(s): {'tool_name': 'Bash', ...}`  
Positive control: `{'permission_denials': []}` → failures=0

**D5. `_gate_deposit_exists`**  
Violation: Plan declares `knowledge/research/must-exist.md` as deposit; file does not exist.  
Rejection: `gate=deposit_exists evidence=missing: knowledge/research/must-exist.md`  
Positive control: Deposit path points to a real file → failures=0

**D6. `_gate_rule_20_self_check`**  
Violation: QA report contains "Rule 20 — QA Self-Check Results" banner but no "PASSED — SELF-CHECK PASSED" line.  
Rejection: `gate=rule_20_self_check evidence=banner present but PASSED line missing in /tmp/tmpl1rzb2p7.md`  
Positive control: Report with both banner and PASSED line → failures=0

**D7. `_gate_rule_22_verification`**  
Violation: QA verification table row contains `✅ should pass` — positive status token with hedging keyword in same cell.  
Rejection: `gate=rule_22_verification evidence=(d) Hedging keyword 'should pass' in positive-status row: | Test A | ✅ should pass | looks ok |`  
Positive control: Table row with `✅` and no hedging → failures=0

**D8. `_gate_qa_test_result`**  
Violation: pytest summary shows "2 failed, 10 passed"; `known_failures=0`.  
Rejection: `gate=qa_test_result evidence=pytest regressions: 2 failed (bad=2, known_failures=0, delta=2)`  
Positive control: "12 passed" with `known_failures=0` → failures=0

**D9. `_gate_scope_check`**  
Violation: Plan Scope declares `knowledge/research/allowed.md`; agent also changed `src/sneaky_edit.py`.  
Rejection: `gate=scope_check evidence=out-of-scope files: src/sneaky_edit.py ... not in declared **Scope:** block`  
Positive control: Only `knowledge/research/allowed.md` changed → failures=0

**D10. plan_lint check (a) — dispatch_mode/pause_for_verdict**  
Violation: `Dispatch Mode: bogus_mode | pause_for_verdict: bogus_pause`  
Rejection: `FAIL: (a) dispatch_mode — unrecognized: 'bogus_mode'` and `FAIL: (a) pause_for_verdict — unrecognized: 'bogus_pause'`. Exit 1.  
Positive control: `Dispatch Mode: bellows | pause_for_verdict: after_step_1` → both PASS. Exit 0.

**D11. plan_lint check (c) — QA banner pair**  
Violation: QA plan with `qa_steps: 1` but no Rule 20 banner or PASSED line.  
Rejection: `FAIL: (c) QA banner pair — missing: banner, PASSED line`. Exit 1.  
Positive control: Plan with both strings → PASS. Exit 0.

**D12. plan_lint check (e) — step heading case**  
Violation: `## Step 1 — QA REVIEW` (lowercase "Step").  
Rejection: `FAIL: (e) step heading format — header declares qa_steps but no uppercase '## STEP N' heading found — step checks (b)/(d) were skipped (vacuous pass)`. Exit 1.  
Positive control: `## STEP 1` → no (e) failure.

**D13. plan_lint check (i) — on_failure coupling**  
Violation: `pause_for_verdict: on_failure` with no `qa_steps` field.  
Rejection: `FAIL: (i) on_failure qa_steps — pause_for_verdict=on_failure requires a parseable qa_steps field`. Exit 1.  
Positive control: `pause_for_verdict: after_step_1` → no (i) check triggered.

**D14. `propagation_check.py`**  
Violation: Plan declares `N=42` in symbol table; prose later says "there are 37 entries."  
Rejection: `(1) RESTATED VALUE — N = 42 restated unqualified ... DIVERGENCES: 1`. Exit 1.  
Positive control: Plan with consistent numbers → `CLEAN — no divergence found`. Exit 0.

**D15. `cycle_check.py`**  
Violation: Drafting Cycle with rising yields (2, 3, 5) and claimed close.  
Rejection: `ESCALATE:claimed-close-unmet`. Exit 1.  
Positive control: Declining yields (5, 1, 0, 0) → `BAR_MET`. Exit 0.

**D16. `fold_check.py`**  
Violation: Baseline saved with `Dispatch Mode: bellows`; fold changed it to `bogus_mode`.  
Rejection: `FOLD-CHECK DRIFT — the fold changed the machine-readable state: APPEARED: plan_lint: FAIL: (a) dispatch_mode — unrecognized: 'bogus_mode'; EXIT: plan_lint: exit 0 -> 1`. Exit 1.  
Positive control: Prose-only change → `FOLD-CHECK CLEAN: machine-readable state unchanged`. Exit 0.

### ASSERTED — mechanism read, fire not exercised

**A1. `wrap_stop_hook.py` / `wrap_check.py`**  
Obstacle: The hook runs inside the Claude Code session lifecycle via the hooks framework (`decision: block` response). Demonstrating it requires an active Claude Code session with the wrap lock armed via `.wrap-in-progress-{session_id}` sentinel and incomplete 4-repo wrap checklist. Cannot be replicated from a standalone script invocation — the hook reads `BELLOWS_DISPATCH` env var and session sentinels that are session-lifecycle artifacts.

**A2–A8. Tests as enforcement (T1–T7)**  
`test_key_heading_annotated_matches_unannotated`, `test_hash_trailing_separator_invariant`, `test_hash_substantive_edit_changes_hash`, `test_raw_content_stored_verbatim_with_separator`, `test_terminal_status_guard`, `test_trailing_separator_only_delta_zero_stales`, `test_needs_classification_plus_duplicates_equals_total`, `test_detect_duplicates_tag_substring_not_flagged`.  
Obstacle: Demonstrating failure (the test rejecting a violation) requires modifying the function under test — a code edit that violates the read-only contract. All 8 tests run green, confirming the property holds. For T1 specifically: `_key_heading(annotated)` produces the same key as `_key_heading(unannotated)` — without the normalization, they differ. The test WOULD catch this. But the mechanism rejecting a violation can only be observed by breaking the function.

### Mechanisms that DID NOT reject their violation

None. Every mechanism tested rejected its constructed violation for the correct reason.

---

## Q4 — Promotion Set

The TSV is deposited at `knowledge/research/learned-promotion-2026-08-23.tsv`.

**Promotion-eligible entries:** Only entries mapped to a DEMONSTRATED mechanism may be promoted. ASSERTED mechanisms (A1–A8) produce no promotable entries.

**Rows in TSV:** 21 (entry, mechanism) pairs.  
**Distinct entries:** 15.  
**Rows with blank `entry_id`:** 0 — all 15 entries have corpus rows.

### Set arithmetic for the companion executable

The companion executable performs two operations:
1. **Demote:** Move all X (=239) currently-`learned` entries to `codified`
2. **Promote:** Move this plan's DEMONSTRATED set to `learned`

These sets OVERLAP: every promoted entry is currently marked `learned` and appears in the X set. The correct order is:

1. Compute `PROMOTE = {entry_ids from this TSV where class = DEMONSTRATED}` (15 entries)
2. Compute `DEMOTE = X \ PROMOTE` (= 239 − 15 = 224 entries)
3. Apply DEMOTE: mark 224 entries `codified`
4. Apply PROMOTE: mark 15 entries `learned` (they were already `learned` and remain so)

Equivalently: demote all X entries, then promote the DEMONSTRATED set. The promote overwrites the demote for the 15 entries. The order does not matter as long as both operations complete, but demote-then-promote is the simpler implementation (one UPDATE per set, no set-difference query).

**Authority:** A row in this file promotes an entry to the state that means DONE. A wrong promotion re-commits the exact error this arc exists to correct. The executable may apply DEMONSTRATED rows mechanically and may apply NOTHING else.

- DEMONSTRATED rows: 21 (covering 15 distinct entries)
- ASSERTED rows: 0 (not in the TSV; ASSERTED entries are NOT promotable)

---

## Q5 — Three-State Counts After Promotion

| State | Count | Derivation |
|-------|-------|------------|
| `learned` | 15 | DEMONSTRATED promotion set |
| `codified` | 224 + 74 = 298 | (X − PROMOTE) + P = (239 − 15) + 74. Note: current `pending` entries become `codified` under the CEO's ruling that `codified` means "written down but not enforced" — but that is the companion executable's call, not this diagnostic's. If `pending` stays `pending`, then `codified` = 224 and `pending` = 74. |

**Correction:** The CEO's three-state model is `pending → codified → learned`. The re-label executable demotes X entries to `codified`. It does NOT touch `pending` entries — those remain `pending` (they have not been written down at all). So:

| State | Count |
|-------|-------|
| `learned` | 15 |
| `codified` | 224 (= X − PROMOTE = 239 − 15) |
| `pending` | 74 |
| `bare` (Q) | 14 |
| **Total** | **327** |

**Identity check:** 15 + 224 + 74 + 14 = 327 = N. ✓  
**Three-state subtotal:** 15 + 224 + 74 = 313 = N − Q = 327 − 14. ✓

---

## Q6 — Convention for Mechanical Enforcement Mapping

### Current state

Walk 0 measured C=3 distinct lesson-id citations using the `[Pp]roposal [0-9]+|entry [0-9]+` pattern across the enforcement surface. These 3 are all in `fold_check.py`: proposals 347, 348, 311.

A broader scan finds additional citation forms:
- `(plan 204)`, `(plan 499)` in `test_lessons_forge.py` comments
- `(500)` bare in `test_lessons_forge.py` docstrings (5 occurrences)
- `(plan 497)` in `wrap_stop_hook.py` docstring

Total distinct IDs across ALL forms: 7 (proposals 311, 347, 348; plans 204, 497, 499, 500). Two incompatible citation forms coexist.

### Proposed convention

**Citation form:** `# enforces: entry <id>` as a comment in the mechanism's source file. Use `entry` (the corpus primary key), not `proposal` (a different table) or `plan` (a dispatched plan, not a lesson). Multiple entries on one mechanism get multiple comments.

**Why `entry` and not `proposal` or `plan`:**
- A `plan_id` is the plan that created or investigated the lesson — it is provenance, not identity.
- A `proposal_id` is a classification event in the corpus — one entry can have many proposals.
- An `entry_id` is the stable row in `lesson_entries` — it is the thing being promoted.

**Where the citation belongs:** IN THE CODE, not in the corpus. Reason: the question "is this lesson enforced?" starts from the mechanism and walks to the entry. A citation in the corpus ("this entry is enforced by mechanism X") requires the corpus to track the enforcement surface, which it cannot do — it has no schema for mechanisms and no way to detect when one is removed. A citation in the code ("this mechanism enforces entry Y") is verifiable by grep and dies with the mechanism if the mechanism is deleted.

**Backfill cost:** 28 enforcement units × reading task to confirm mapping = 1–2 hours of mapping work. The TSV this plan deposits is the seed: 21 of the 28 mappings are already established.

### `detect_learned.py` emitter fix

`detect_learned.py:245` currently emits `"proposed_status": "learned"` unconditionally for every detector PASS. Under the CEO's ruling, a detector PASS means the lesson text appears in its target artifact — which is `codified`, not `learned`. The emitter should emit `"proposed_status": "codified"` for detector PASS. Promotion to `learned` requires the separate evidence this plan produces: a demonstrated mechanism rejecting a violation.

---

## What could not be measured

1. **wrap_stop_hook.py firing** — requires active Claude Code session lifecycle. ASSERTED with obstacle named.
2. **Tests-as-enforcement failure path** — requires modifying the function under test (code edit in read-only diagnostic). ASSERTED; all 8 tests run green confirming properties hold.
3. **gate interactions in live dispatch** — the `check()` orchestrator runs all gates sequentially and returns a composite result. Tested gates individually via direct Python calls, not through the dispatch pipeline.
4. **WARN-only checks' advisory value** — plan_lint WARN checks (f, g, h, j, k, l, n, o1, o2, p, q) are not enforcement mechanisms (they do not cause exit 1), but they surface issues. Their contribution to lesson enforcement is unmeasured.

## Open forks

1. The Q=14 bare entries still await a CEO ruling and belong to no state.
2. Whether a mechanism's lesson-citation belongs in the code or the corpus is answered in Q6 (code), but this is a proposal, not a decision.
3. The companion re-label executable is not yet authored and must consume this plan's promotion set with the set arithmetic Q4 specifies.
4. `detect_learned.py:245` emits `"proposed_status": "learned"` — under the CEO's ruling it should emit `"codified"`. This is a finding, not a fix (read-only diagnostic).
5. Entry 116/line 1377 ("scope_check cannot evaluate blueprint-delegated file lists") is one of the Q=14 bare entries — it has no `[status:]` marker and is quarantined.

## Recommended executables

1. **Re-label executable** — demote X entries to `codified`, promote the 15 DEMONSTRATED entries to `learned`. Must consume the TSV with the set arithmetic in Q4. Must fix `detect_learned.py:245` to emit `codified` instead of `learned`.
2. **Citation backfill executable** — add `# enforces: entry <id>` comments to all 28 enforcement units using the TSV mapping as seed.
3. **ASSERTED-to-DEMONSTRATED executable** — for the 8 tests-as-enforcement, construct a mutation-testing harness that temporarily breaks each function and verifies the test fails. This would promote their mapped entries (currently only entry at line 4599 has a mapping; the others have no entry).
