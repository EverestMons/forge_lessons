# Lessons Forge — Next Session Baton

**Last session:** 2026-07-16 (cycle + corpus-integrity root-cause fix + Gate 1 + advisory retirement + Gate 2 — plans 203 / 204 / 205 / 206 / 207 / 208)
**Last session focus:** A routine 3-entry cycle (plan 203) halted at its Step 1 verdict on a **corpus-integrity bug that had silently corrupted every prior cycle**. Plan 204 fixed the root cause; 205 completed the cycle; 206 dispositioned Gate 1; 207 retired the plan-154 advisory whose justification the root-cause fix dissolved. 208 codified the results into PLANNER_TEMPLATE **v4.74**. **The arc is closed end-to-end — `proposed` is 0 and no lessons-forge work is in flight.**

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

- **Plan 208 (Gate 2 codification, closed):** PLANNER_TEMPLATE **v4.73 → v4.74**. **Rule 52** (from proposal 147, CEO-widened): re-verify any claim inherited from a generated artifact before it informs a disposition/routing/plan-shape — an explicit **sibling to Rule 39**, which protects an *edit* while 52 protects a *decision* (the FORGE_QA.md case involved no edit, so 39 would never have fired). **Checklist #16 refined** (proposal 148's residue): known-good is necessary but not sufficient — a degenerate exemplar cannot teach which reading of a convention is meant. **148's qa_steps clause REJECTED as already-covered** (`:407`, blame evidence — the 131/135 precedent). Statuses: 147/148 `implemented`, 146 `reference`.

## DB state (verified 2026-07-16, canonical read-only)

`lesson_entries`: **140**. `lesson_proposals`: **148** — implemented **99**, superseded 28, rejected 15, **proposed 0** (the 2026-07-16 cycle is fully dispositioned), stale 3, reference **3**. Routes: 18 non-NULL (15 from the 07-06 Gate 1 + 146/147/148). Full suite: **55 passed** (was 61 pre-207). Work list `get_unclassified_entries()`: `[]`.

**⭐ Plan 204's fix is PROVEN IN PRODUCTION (2026-07-16, at wrap).** Appending the new `2026-07-16: Never state a bare expected number` lesson to LESSONS.md gave entry 140 a trailing `\n\n---\n\n` — the exact trigger of the bug. Verified post-append: entry 140's hash is **STABLE** and **0 entries flipped**. Under the old code this append would have staled **proposal 148** — the rule codified an hour earlier, demoted by the bug it was written alongside. The loop is dead.

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

## Gate 2 — DONE 2026-07-16 (plan 208, closed). PLANNER_TEMPLATE now **v4.74**.

Nothing is owed from the 2026-07-16 cycle. `proposed` is 0. Both codify-routed proposals landed; 146 has its honest terminal `reference` status.

**One lesson awaits the next cycle:** `2026-07-16: Never state a bare expected number in plan text [planner-discipline]` is in LESSONS.md, un-ingested — routed through the corpus per CEO decision rather than codified directly at Gate 2 (Gate 2 codifies what Gate 1 routed; it is not a side door). Evidence: 4/4 Planner-predicted numbers wrong across plans 203-207, all caught only by the paired verify-and-explain clause. **The next cycle ingests exactly this one entry.**

## In-flight threads (carry forward)

### plan_lint qa_steps cross-check [NEXT UP — still not started]
Warn when a QA-labeled step is absent from the `qa_steps` list, or when `qa_steps` names a non-QA step. `qa_steps` is a step-number list (gates.py:724), not a count. Entry 140 is the source lesson; proposal 148 is its classification. No lint logic exists yet. Small; deposit as a Bellows plan.

### ✅ RESOLVED — two threads this baton carried were ALREADY DEAD (corrected 2026-07-16 at wrap)
Both were closed on 2026-07-09 and had been propagated as "open" for a week. Caught by re-reading the live template — **the exact failure Rule 52 now names**, committed by the Planner while writing this baton:
- **~~Workaround #3 factual tension~~** — **corrected in v4.73** (2026-07-09). Verdict prose reaches only the ledger/humans, never an agent; Workaround #3 now aligns with Rule 51. Nothing owed.
- **~~Session-end-suite evidence-file convention~~** — **retired in v4.72** (2026-07-09, CEO decision). The `pytest_session_end.txt` convention is gone; session-end suite state lives in the wrap baton, sourced from the last full-suite plan run. Nothing owed.
- **FORGE_QA dispatch wiring [verify when relevant]:** confirm lessons-forge QA dispatches actually read `forge/agents/FORGE_QA.md`. (The file EXISTS — re-disk-verified this session. The old "does not exist" flag was stale for three weeks and is dead.)

---

## Operational notes for next session

- **Capture drift (CEO):** LESSONS.md has had **no new entries since 2026-07-07**, despite nine days of shop work (exec-196 → 201, auto-park guard fix, schema-v17 fix). The corpus is hand-fed; the thin cycle reflects the capture habit lapsing, not a quiet shop. Several of those lessons were captured as *agent memory* instead — worth deciding whether the two channels should converge.
- **If you change the hash function again, the BACKFILL is the dangerous part.** All 83 parsed entries change hash under any normalization tweak; a naive re-hash routes them through the update path and stales **79 proposals (64 implemented)**. Backfill `content_hash` with **direct SQL only** — never via `ingest_lesson_entries`/`run_full_lessons_cycle`. Model on `scripts/backfill_normalized_hashes_2026-07-16.py` (idempotent; asserts the proposal distribution is unchanged).
- LESSONS.md parses to **83** entries while `lesson_entries` holds **140** — expected, not a defect: `parse_lessons_md` stops at `^## Archived`.
- `status_updated_by` has a CHECK constraint: only `planner` / `ceo` / `auto` (or NULL). A plan asking for anything else will fail — plan 204's text got this wrong and the agent correctly substituted `ceo`.
- `qa_steps` is a **list of QA step numbers**, not a count (`qa_steps: 3` for a 3-step plan whose step 3 is QA).
- PLANNER_TEMPLATE is at **v4.74** — Gate 2 (plan 208) bumped it from v4.73 this session. (v4.72/v4.73 landed 2026-07-09 between cycles; this baton claimed v4.71 for a week — verify the live header, do not trust this line.)
- `timeout` is unavailable on macOS; use `python3 -m pytest` directly.
