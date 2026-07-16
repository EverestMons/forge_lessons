# Lessons Forge — Next Session Baton

**Last session:** 2026-07-16 (cycle + corpus-integrity root-cause fix + Gate 1 + advisory retirement — plans 203 / 204 / 205 / 206 / 207)
**Last session focus:** A routine 3-entry cycle (plan 203) halted at its Step 1 verdict on a **corpus-integrity bug that had silently corrupted every prior cycle**. Plan 204 fixed the root cause; 205 completed the cycle; 206 dispositioned Gate 1; 207 retired the plan-154 advisory whose justification the root-cause fix dissolved. **The arc is closed — no lessons-forge work is in flight.**

---

## The headline — read this before authoring anything

**Appending to LESSONS.md silently demoted the previous last entry's `implemented` proposal to `stale`, every single cycle.**

`parse_lessons_md` assigns lines up to the next `##` heading to an entry's body, so a wrap commit that appends new lessons — pure insertions, zero deletions — gave the previous last entry a trailing `\n\n---\n\n`. Its `content_hash` flipped over **7 bytes of whitespace** with zero substantive change (entry 137: `4ff4c905` → `b9875afa`, proven against `git show e57a22b^:LESSONS.md`). The ingest update path then staled its proposals via `WHERE entry_id=? AND status != 'stale'` — which demoted **any** status, including `implemented`.

**All 4 `stale` proposals in the corpus were this artifact.** Each entry was the last in the file when the prior cycle ran; 3 of 3 completed instances ended as a **rejected duplicate** — a 100% waste rate:

| Entry | Staled proposal | Reclassified as | Outcome |
|---|---|---|---|
| 93 | 98 | 122 | rejected |
| 116 | 121 | 123 | rejected |
| 123 | 130 | 131 | rejected |
| 137 | 145 | — | caught by the 203 halt |

**Reframing that matters: proposal 131 — the motivating case for plan 154's entire dedup-advisory build — was a downstream symptom of this bug.** Plan 154 automated catching the duplicates this bug manufactured instead of stopping their manufacture. Before building machinery to cope with duplicate proposals, suspect a generator.

---

## What shipped (2026-07-16)

- **Plan 204 (root-cause fix, closed):** `_normalize_for_hash()` strips trailing blank lines + `^[ \t]*-{3,}[ \t]*$` separators from the **hash input only** (`raw_content` still stored verbatim — the classifier reads it). `_TERMINAL_STATUSES` guard means an ingest can **never** silently demote `implemented`/`rejected`/`superseded`/`reference`; genuine edits to such entries surface via the new `terminal_proposals_flagged` key instead of being swallowed. Backfilled 83 hashes; restored proposal 145. Suite **52 → 61**, 0 regressions.
- **Plan 205 (cycle re-dispatch, closed):** classified entries 138/139/140 → proposals 146/147/148, report deposited, QA 100% PASS. Work list now `[]`.
- **Plan 203 (halted, superseded by 205):** its Step 1 ingest committed before halting — that is why 205 needed no ingest step.
- **Plan 206 (Gate 1 route disposition, closed):** proposals 146→`reference`, 147→`codify`, 148→`codify`. Routes only — statuses stayed `proposed` (Gate 2 owns transitions). Blast radius exactly +3 (15→18; the other 15 are plan 133's 2026-07-06 routes).
- **Plan 207 (advisory retirement, closed):** removed `detect_recently_implemented_overlaps`, `_tokenize_for_overlap`, both call sites, the report rendering, and 7 tests. **Plan 204's guard survived the excision from its own function** (`terminal_proposals_flagged` / `_TERMINAL_STATUSES` / `_normalize_for_hash` all intact); `detect_duplicates` untouched. Suite **61 → 55** (7 removed, 1 preserved: `test_report_no_overlap_unchanged`'s per-proposal rendering assertions were the suite's ONLY such coverage — kept as `test_report_renders_proposal_details`).

## DB state (verified 2026-07-16, canonical read-only)

`lesson_entries`: **140**. `lesson_proposals`: **148** — implemented 97, superseded 28, rejected 15, **proposed 3**, stale 3, reference 2. Routes: 18 non-NULL (15 from the 07-06 Gate 1 + 146/147/148). Full suite: **55 passed** (was 61 pre-207). Work list `get_unclassified_entries()`: `[]`.

---

## Gate 1 — DECIDED 2026-07-16 (plan 206, closed)

| Proposal | Entry | Route | Basis |
|---|---|---|---|
| 146 | 138 | **reference** | Fix already shipped (plan 185, `38c1670`, Planner disk-verified). Matches the plan-133 precedent for entries 132/133. Its residual — Bash-using steps still `gate_fail` on a cap instead of parking — is a **deliberate anti-stranding trade-off** (exec-197's `has_mutating_tool_use`), already tracked in the shop baton; routing to `backlog` would duplicate a live thread. |
| 147 | 139 | **codify** | Disk-verification discipline. NOT subsumed. |
| 148 | 140 | **codify** | The `qa_steps` step-number-list trap. NOT subsumed. |

**The advisory's subsumption flags were FALSE POSITIVES — settled, do not re-litigate.** It flagged the *same two* proposals (127/128) against *both* 147 and 148, purely on shared `planner-discipline` tag equality. 127 is about mandatory QA callouts; 128 about full-suite runs. Neither relates to disk-verification or `qa_steps` semantics.

**Also decided:**
- **Proposals 98/121/130 stay `stale`** — untouched. Their rules are already codified (06-03/06-07 ratifications) and their twins (122/123/131) were all correctly rejected; restoring would manufacture proposals for rules that already exist.
- **Plan 154's advisory: RETIRED** (plan 207). Evidence from its first and only production run: 353 overlaps DB-wide; 14 advisory lines across 3 proposals; **4 of 4 hits examined were false positives, 0 true positives**; and it **missed proposal 139** (entry 131, `planner-discipline`, `implemented` 2026-07-07, inside the 45-day window) — the nearest genuinely adjacent proposal to entry 140's lesson. Not merely noisy — **anti-correlated with relevance**. Its motivating case (proposal 131) was a symptom of the bug 204 fixed.

---

## CEO Gate 2 agenda (nothing below is decided)

1. **Codify proposals 147 + 148** into PLANNER_TEMPLATE (currently **v4.71**). Status transitions (`proposed` → `implemented`/`superseded`) happen here, not at Gate 1. Proposal 146 is `route=reference` — give it an honest terminal state per the plan-135 precedent (`status='reference'`), do NOT codify it.
2. **⚠️ Correction that MUST survive into Gate 2:** the plan-205 classification summary cites `_parse_session_limit_reset`, which **does not exist**. The real function is **`_parse_session_reset`** (`bellows/runner.py:36`). Substance right, identifier fabricated — do not let the wrong name shape a codification decision. (Itself a mild instance of entry 139's failure mode, produced *while classifying entry 139*.)
3. **Entry 139's rule may be too narrow** — as written it targets claims that *inform a disposition*, but item 2 above is a **supporting-evidence** claim that was wrong while the disposition was right. Consider whether the codified rule should reach cited identifiers, not just disposition-driving claims.
4. **⭐ NEW rule candidate — never state a bare expected number in plan text.** Four Planner-predicted numbers were wrong across this session's plans (a CHECK-constraint value, a stale suite baseline, a route count, and test arithmetic). **All four were caught only because each prediction was paired with an explicit "verify, don't assume — report the actual numbers" clause and halt-and-explain on mismatch.** In plan 207 the predicted 54 would have been the *worse* outcome: hitting it required silently dropping the suite's only per-proposal report-rendering coverage. The agents reconciled reality against the text every time and routed the deltas to Prompt Feedback. Candidate for the Plan Authoring Checklist.
5. **Entry 140 has a second half** — the `plan_lint` qa_steps cross-check (see In-flight below). Proposal 148 codifies the discipline rule only.

## In-flight threads (carry forward)

### plan_lint qa_steps cross-check [NEXT UP — still not started]
Warn when a QA-labeled step is absent from the `qa_steps` list, or when `qa_steps` names a non-QA step. `qa_steps` is a step-number list (gates.py:724), not a count. Entry 140 is the source lesson; proposal 148 is its classification. No lint logic exists yet. Small; deposit as a Bellows plan.

### Session-end-suite evidence-file convention [CEO decision, still open]
Template ~line 593 prescribes `session-YYYY-MM-DD/pytest_session_end.txt` but no such file has ever been written. Decide the convention or drop the rule. Suite results keep landing in batons instead.

### Carried from Gate 2 ratification
- **Workaround #3 factual tension:** verdict reasoning does NOT reach agents — the Workaround text implies it can. Diagnostic-first before correcting.
- **FORGE_QA dispatch wiring [verify when relevant]:** confirm lessons-forge QA dispatches actually read `forge/agents/FORGE_QA.md`. (The file EXISTS — re-disk-verified this session. The old "does not exist" flag was stale for three weeks and is dead.)

---

## Operational notes for next session

- **Capture drift (CEO):** LESSONS.md has had **no new entries since 2026-07-07**, despite nine days of shop work (exec-196 → 201, auto-park guard fix, schema-v17 fix). The corpus is hand-fed; the thin cycle reflects the capture habit lapsing, not a quiet shop. Several of those lessons were captured as *agent memory* instead — worth deciding whether the two channels should converge.
- **If you change the hash function again, the BACKFILL is the dangerous part.** All 83 parsed entries change hash under any normalization tweak; a naive re-hash routes them through the update path and stales **79 proposals (64 implemented)**. Backfill `content_hash` with **direct SQL only** — never via `ingest_lesson_entries`/`run_full_lessons_cycle`. Model on `scripts/backfill_normalized_hashes_2026-07-16.py` (idempotent; asserts the proposal distribution is unchanged).
- LESSONS.md parses to **83** entries while `lesson_entries` holds **140** — expected, not a defect: `parse_lessons_md` stops at `^## Archived`.
- `status_updated_by` has a CHECK constraint: only `planner` / `ceo` / `auto` (or NULL). A plan asking for anything else will fail — plan 204's text got this wrong and the agent correctly substituted `ceo`.
- `qa_steps` is a **list of QA step numbers**, not a count (`qa_steps: 3` for a 3-step plan whose step 3 is QA).
- PLANNER_TEMPLATE remains at **v4.71** — untouched this session (no Gate 2 ran).
- `timeout` is unavailable on macOS; use `python3 -m pytest` directly.
