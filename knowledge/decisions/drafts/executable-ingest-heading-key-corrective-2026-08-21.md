# lessons-forge — CORRECTIVE to halted-499: `_key_heading` must not collapse internal whitespace
**Date:** 2026-08-21 | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** targeted (DEV) → full suite + controlled-A/B canary (QA) | **Execution:** Step 1 (DEV) → Step 2 (QA) | **Priority:** 1 | **qa_steps:** 2 | **Depends on:** halted-executable-499 (its Step 1 is COMMITTED at `7e8b2a2` and is the starting point)

**auto_close:** false
**pause_for_verdict:** always

## Context

Plan 499 added `_key_heading` and applied it at the three ingest sites so that annotating a `LESSONS.md` heading with `[status: ...]` / `[target: ...]` cannot duplicate corpus rows. **All seven gates passed and the step was still wrong**, so it was stopped and its Step 1 remains committed at `7e8b2a2`. **The three call sites are CORRECT and this plan must not touch them.** One function is wrong.

**The defect (Planner-measured 2026-08-21):**

    return re.sub(r'\s+', ' ', cleaned).strip()      # src/lessons_forge.py:57

`_key_heading` collapses INTERNAL whitespace. **40 of the 370 stored `source_heading` values contain a run of more than one space** — the house heading style puts TWO spaces before the first `[tag: ...]`. So the lookup uses a collapsed key while the DB holds the original: those 40 rows MISS and are **RE-INSERTED on every ingest**, with or without annotation. This is broader than the defect 499 set out to fix, and **it is live in `main` right now** — any forge cycle run today inserts 40 duplicates.

**Measured against a `cp` copy (live DB verified byte-identical by `shasum -a 256` before and after):** a controlled A/B gave CONTROL `inserted=51` and TREATMENT (3 headings annotated) `inserted=51` — delta 0, so 499's *annotation* fix genuinely works. But the correct figure for both arms is **11** (of 324 file entries, 313 match a stored heading exactly; the 11 are 4 appended during the 2026-08-21 wrap plus the 7 un-ingested that diagnostic-498 identified). The extra **40** are exactly the double-space rows.

**⚠️ A SINGLE-ARM PROBE IS UNINTERPRETABLE HERE, AND THIS IS WHY THE QA CANARY IS AN A/B.** The Planner's first probe reported "51 inserted" and that number alone cannot distinguish this regression from pre-existing corpus drift. Only running the ingest twice — once unannotated, once annotated — separates the two. Do not replace the A/B with a single run and an expected constant.

## The correction (VERIFIED BY THE PLANNER BEFORE PRESCRIBING IT — re-verify, do not trust)

    _STATUS_TARGET_MARKER_RE = re.compile(r'\s*\[(?:status|target):[^\]]*\]', re.IGNORECASE)

    def _key_heading(heading: str) -> str:
        return _STATUS_TARGET_MARKER_RE.sub('', heading).rstrip()

Consume the whitespace PRECEDING a marker; `rstrip` the tail; never touch internal runs. Measured over all 370 stored headings: **0 change** — perfect identity — while an annotated heading still resolves to the same key as its unannotated form and internal double-spacing survives.

## MUST-PRESERVE

- ⚠️ **NEVER write to the live corpus DB** (`/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`) — untracked, sole system of record for 378 proposals and 284 CEO routing decisions. All exercises use a `cp` copy in the step's TMP dir, by absolute path, OUTSIDE the repo and your worktree.
- ⚠️ **Do not modify `LESSONS.md`.**
- ⚠️ **Do not touch the three call sites** (`:147`, `:381`, `:481`) — 499 got them right and they are committed. This plan changes ONE function and its tests. If you believe a call site is wrong, STOP and report rather than widening the change.
- Strip ONLY `[status: ...]` and `[target: ...]`; **never `[tag: ...]`** — tags are part of every stored heading and stripping them would fail to match all 370 rows.
- Do not change `_normalize_for_hash` or hash semantics: `raw_content` is body-only, so heading annotation cannot flip the hash and cannot stale the 250 implemented proposals.

## Drafting Cycle
**Tier:** T1 — triggers computed: **T-2 FIRES** (the ingest path writes the corpus DB; the defect being fixed inserts rows into production data). T-5 does not fire — code is tracked and a verified snapshot exists (`knowledge/research/corpus-snapshot-2026-08-21.sql`). T-6, T-7, T-8 do not fire. ⇒ T1: full five-lens walk, no cold panel.
**Walk 0 (context pin) — REAL (2026-08-21):**
1. Newest same-class: `halted-executable-499` itself — this is its corrective, in the exec-490→492 shape (stop, then a corrective re-deposit that changes only what was wrong).
2. Pre-edit pins (agent RE-VERIFIES): `_STATUS_TARGET_MARKER_RE` at `:52`, `_key_heading` at `:55-57`, call sites at `:147`, `:381`, `:481`. Baseline commit `7e8b2a2`.
3. The identity property is the acceptance criterion, and it is measurable: over the 370 stored headings the corrected normalizer must change **0**.

## STEP 1 — DEV: correct the normalizer

**Role:** DEV. ⚠️ You run in a worktree — edit and commit INSIDE it at the same relative paths. The corpus DB is untracked and absent from your worktree; you do not need it here.

1. Replace `_STATUS_TARGET_MARKER_RE` and `_key_heading` with the corrected pair above. The regex gains a leading `\s*`; the body loses the `re.sub(r'\s+', ' ', ...)` collapse and uses `.rstrip()`.
2. **Targeted tests** in `src/test_lessons_forge.py`:
   - **The identity property (the acceptance criterion):** for a fixture list of headings that INCLUDES double-space examples in the house style (`title  [tag: x]`), assert `_key_heading(h) == h` for every one. ⚠️ Build the fixture from literal strings — the live DB is not available in a worktree and must not be reached for.
   - An annotated heading and its unannotated form produce the SAME key.
   - `[tag: ...]` survives; `[status:]`/`[target:]` are removed; matching is case-insensitive.
   - Internal double-spacing is PRESERVED (the regression guard — this test fails against 499's version).
   - A marker at the START or MIDDLE of a heading does not leave a doubled space.
3. ⚠️ **ORDER MATTERS — write the regression guard BEFORE applying the fix, and watch it fail.** Sequence: (a) add the internal-double-spacing test to `src/test_lessons_forge.py` while the code is still at `7e8b2a2`; (b) run it and paste the raw FAILING output — this proves the guard actually discriminates; (c) apply the correction from the Context; (d) re-run and paste the raw PASSING output. A guard written after the fix and only ever observed green guards nothing ([[earn-the-clean-gate-dont-author-it]]). Both outputs go in your Receipt.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py`
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/test_lessons_forge.py`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py`
- `/Users/marklehn/Developer/GitHub/lessons-forge/src/test_lessons_forge.py`

**Commit:** repo-asserting absolute form against YOUR worktree, explicit pathspec, add before commit. Your final operation is the commit.

## STEP 2 — QA: full suite + the CONTROLLED A/B ingest canary

**Role:** QA.

**MANDATORY Rule 20 self-check banner** — the deposited QA report MUST contain, verbatim, the heading `## Rule 20 — QA Self-Check Results` and, below it, `**PASSED — SELF-CHECK PASSED**`. Canonical block: `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`. `plan_slug: ingest-heading-key-corrective-2026-08-21`; `qa_report_path: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/ingest-heading-key-corrective-qa-2026-08-21.md`; `evidence_dir: /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-corrective-2026-08-21/`; `required_evidence_files: [pytest_full.txt, canary.txt]`. FAILED → halt.

0. `mkdir -p` the evidence directory first.
1. **Full suite**, foreground, raw output to `pytest_full.txt`; quote the counts line verbatim and report failures by IDENTITY, not by count alone.
2. **Controlled A/B ingest canary** — raw output to `canary.txt`. ⚠️ Every run against its OWN fresh `cp` copy of the corpus DB in the step's TMP dir, by absolute path; scratch `LESSONS.md` copies also in TMP, never in the repo. ⚠️ `ingest_lesson_entries(..., source_file="LESSONS.md")` — `source_file` is a KEY, not a path (`:121`); passing the copy's filesystem path makes every row miss and fails the canary on correct code.
   - **ARM A (control):** parse an UNANNOTATED copy of `LESSONS.md`, ingest into a fresh DB copy. Record `inserted`.
   - **ARM B (treatment):** annotate 3 headings that are VERIFIED PRESENT in the DB with `[status: learned] [target: PLANNER_TEMPLATE.md]`, ingest into another fresh DB copy. Record `inserted`.
   - Assertions, each reported SEPARATELY:
     - **(i)** `arm_B.inserted == arm_A.inserted` — annotation adds nothing.
     - **(ii)** ⚠️ **The corrective assertion — and it must be COMPUTED AT RUN TIME, not hard-coded.** The right form is `arm_A.inserted == (parsed_entries - exact_heading_matches)`, where `exact_heading_matches` counts file headings whose exact text is already a stored `source_heading`. At authoring time that evaluates to **11** (324 parsed − 313 matching) versus **51** under 499's version — but 11 is TIME-SENSITIVE: appending a single new entry to `LESSONS.md` makes it 12, and a hard-coded 11 would fail on correct code. Compute both sides, report them, and assert equality. Then state whether the number matched the authoring-time 11, as a sanity signal rather than a gate. If you measure the 40-row gap (i.e. `inserted` exceeds the computed expectation by ~40), the correction did NOT land.
     - **(iii)** `stale_proposals_marked == 0` in both arms — the 250 implemented proposals untouched.
     - **(iv)** the 3 annotated entries resolve to their ORIGINAL row ids.
     - **(v)** the identity property against REAL data: for every stored `source_heading` in the copy, `_key_heading(h) == h` — expect **370/370**.
   - ⚠️ **A FAILING canary looks like:** (ii) at 51, or (i) with a non-zero delta, or (v) below 370. None may be read as a pass.
3. Confirm the LIVE corpus DB is byte-identical before and after (`shasum -a 256`, both pasted).

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/ingest-heading-key-corrective-qa-2026-08-21.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-corrective-2026-08-21/pytest_full.txt`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-corrective-2026-08-21/canary.txt`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/ingest-heading-key-corrective-qa-2026-08-21.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-corrective-2026-08-21/pytest_full.txt`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/ingest-heading-key-corrective-2026-08-21/canary.txt`

**Commit:** repo-asserting absolute form against YOUR worktree, explicit pathspec. Your final operation is the commit.
