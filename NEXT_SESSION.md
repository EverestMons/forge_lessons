# Lessons Forge — Next Session Baton

**Last session:** 2026-07-16 (cycle run + a corpus-integrity root-cause fix — plans 203 / 204 / 205)
**Last session focus:** A routine 3-entry cycle (plan 203) halted at its Step 1 verdict on a **corpus-integrity bug that had silently corrupted every prior cycle**. Plan 204 fixed the root cause; plan 205 re-dispatched and completed the cycle. Corpus verified intact and now structurally protected.

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

## DB state (verified 2026-07-16, canonical read-only)

`lesson_entries`: **140**. `lesson_proposals`: **148** — implemented 97, superseded 28, rejected 15, **proposed 3**, stale 3, reference 2. Full suite: **61 passed**. Work list `get_unclassified_entries()`: `[]`.

---

## CEO Gate 1 agenda (nothing below is decided)

1. **Route disposition for proposals 146/147/148.**
   - **146** (entry 138, `structural`, targets `bellows/runner.py`) — **the fix already shipped.** Planner-verified on disk: `_check_session_limit` (runner.py:74), `_parse_session_reset` (runner.py:36), park machinery in `bellows.py`, plan 185 commit `38c1670` (2026-07-14). Strong reject/implemented candidate.
   - **147** (entry 139, `governance_rule`) — disk-verification discipline.
   - **148** (entry 140, `governance_rule`) — the `qa_steps` step-number-list trap.
2. **⚠️ Correction to carry into Gate 1:** the plan-205 classification summary cites `_parse_session_limit_reset`, which **does not exist**. The real function is **`_parse_session_reset`** (`bellows/runner.py:36`). Substance right, identifier wrong — do not let the wrong name shape a codification decision. (This is itself a mild instance of entry 139's failure mode, produced *while classifying entry 139*.)
3. **Proposals 98/121/130** — plan 204's audit recommends leaving all three `stale` (underlying rules already codified via the 06-03/06-07 ratifications; twins 122/123/131 all correctly rejected, so restoring would manufacture noise). Planner concurs. **CEO decides.**
4. **Plan 154's advisory — narrow or retire?** Now well-evidenced: first production run measured **353 overlaps DB-wide**; the 2026-07-16 report rendered **14 advisory lines across 3 proposals (~4.7 each)**, every one tag-equality shaped (`tag overlap: bellows; keyword overlap: bellows`). An advisory firing ~5×/proposal on tag overlap alone trains reviewers to skip it. Its motivating case is now known to be a symptom of the bug 204 fixed, so its value may have largely evaporated. CEO decision 2026-07-16 was **note-and-defer to Gate 1** — this is that Gate.
5. **Entry 139's rule may be too narrow** — as written it targets claims that *inform a disposition*; this cycle produced a supporting-evidence claim that was wrong while the disposition was right. Consider whether it should reach cited identifiers.

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
