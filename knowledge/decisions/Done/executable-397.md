# Lessons Forge — Cycle Run 2026-08-13, PLAN A: ingest the 10-entry session-42 sweep batch (classification held to Plan B)

**Date:** 2026-08-13 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 10) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-ingest-s42sweep-2026-08-13`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Ingest only.** This plan takes the 10 un-ingested `LESSONS.md` entries (the session-42 sweep batch, appended 2026-08-13 at root commit `f4dbfc6`) into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**, authored against the work list this plan leaves behind. The A/B split is carried from the 339/340→357/359→381/382 lineage — the split collapses the verdict-gate guard matrix to ONE write step, ONE gate, ONE window — and the structural reason (not the batch size) is the licence.

**Clone lineage — measured, not recalled:** 247 → 257 → 274 → 281 → 283 → 288 → 296 → 311 → 339 → 357 → **381** (direct origin AND newest same-class; both roles resolve to the same plan, verified against `Done/` at authoring by ship date). Cycle-class diff run at walk 0, every inherited fact RE-MEASURED 2026-08-13 read-only against live canonical.

### ⚠️⚠️ INHERITED FACTS FROM 381 THAT ARE FALSE HERE — every one re-measured 2026-08-13

1. **THE BATCH IS 10, uniform and late:** all ten dated 2026-08-13, appended after the last ingest at root commit `f4dbfc6`, sitting at file positions **272–281 of 281 parsed**. Dry run (real `ingest_lesson_entries` against a scratch COPY of canonical, rolled back) measured **would_insert 10 / would_update 0 / unchanged 271**. **Never derive the batch from a date filter — the four s40sweep entries carry the same date and are already ingested; the parser diff is authoritative.**
2. **BASELINES MOVED:** `E0 = 328`, `P0 = 336` (`sqlite_sequence` agrees on both). Status distribution (zero-emitting, all EIGHT schema statuses): implemented **275** · superseded **28** · rejected **15** · reference **15** · stale **3** · accepted **0** · proposed **0** · ambiguous **0** — total 336. **`SURFACEABLE_BASE = 0`** (proposed + ambiguous). `STALE_COUNT = 3` (proposals 98/121/130, settled 2026-07-16 — leave untouched). Whole-corpus `DUP_COUNT = 19` (baseline, UNCHANGED since 357; G3 uses the batch-scoped form).
3. **`NT` REMAINS EMPTY — `NT_COUNT = 0`, re-measured live, not inherited.** The 381/382/384 batch's four proposals (333–336) are terminal, as are 335/336 after 389's flip; the claim rests on the live NT read alone, never on per-id flip recall ([[the inherited-label class]] — 381's own walk-1 fold). G1 re-asserts it live pre-mutation.
4. **THE HASH-TRAP SENTINEL MOVES TO ENTRY 328** — DB content-hash `63b3831d2ddfdd553d9b8904df40723dbbd50d6fa442db72f2d16cfeb8762d26` (a corpus value, not a file digest — no file pin exists for it), heading `2026-08-13: A transcribed census row transposed two column values and stayed well-formed — spot-check rows against their cited sources [tag: verification]`. Named by id, never `MAX(id)`. Not file-last (the 10 follow it), so the trailing-separator trap cannot reach it; regression sentinel for `_normalize_for_hash` only. Parsed-match count measured **1**.
5. **THE EM-DASH UNIFORMITY HOLDS: 10 of 10 headings carry ` — `** (measured per-heading, not assumed from the streak). The whole-heading fallback branch of `detect_duplicates` does not fire on this batch; say so rather than reporting a uniform "no hits."
6. **TWO OF THREE DOCTRINE PINS MOVED** — each measured at authoring against the live tree; the agent re-measures at Step 1a-ter; these are the authoring reference:
   - v2.9, moved by plan 391 (381 pinned `5d4c8d8c…` v2.7):
     `shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` → `ea3049ce6fc8ad0c62b1e4da9525500826fe2c8495fb478ee038c03c2d995752`
   - v4.88, moved by plan 389 (381 pinned `8aac8aa9…` v4.87):
     `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` → `4f33c3884b426189ba9f019c0722681a4446e5f9223b1f0f10c117f7de0691a0`
   - **unchanged FIFTH cycle running:**
     `shasum -a 256 /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` → `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0`
7. **TWO HEADINGS ARE SHELL-HOSTILE** (apostrophes only — no quotes, no backticks): batch positions **2 and 7** → predicted entry ids **330, 335**. Bind headings as query parameters everywhere; never interpolate into a shell string.
8. **THE BACKUP GLOB POPULATION IS 12** (was 11 at 381; the glob is `data/backups/lessons-forge-pre-cycle-*.db` — the directory's raw file count is larger with sidecars and other names, and probing the wrong representation returns that confident wrong number). The count is NOT the guard; the id token `-<id>-` is. Derive resume dates from the actual filename, never the local dispatch date.
9. **`detect_duplicates` SIGNATURE UNCHANGED:** `(conn, entry_ids, reference_files=None)` — verified against live source by `inspect.signature` at authoring; the candidate pool of parsed-and-matched ids measured **271** (the 381 batch's 4 now match).
10. **⚠️ 381's "BOTH REPOS' `decisions/` ARE CLEAN" IS FALSE HERE — measured, and the guard is re-scoped rather than inherited:** `lessons-forge/knowledge/decisions/` carries ZERO non-Done entries (true, re-measured), but `bellows/knowledge/decisions/` carries TWO parked non-plan documents (`reporting-phase2-cycle-query-blueprint-2026-07-01.md`, `roadmap-per-plan-step-state-tracker-2026-04-17.md`) and `governance/knowledge/decisions/` carries `halted-executable-328.md` (the standing housekeeping item). **None of the three touches this plan's single-writer check, which globs `in-progress-*.md` in THIS project only** — the check's scope is stated below so no future clone re-imports 381's wider claim.

### ⚠️ NUMBERING — one band, stated once
- **`lesson_entries.id` 329–338** — THIS batch's 10 entries (after ingest; assigned in parse order, verified by source read: `ingest_lesson_entries` iterates the parser's list with AUTOINCREMENT).
- **`lesson_proposals.id` 337–346** — Plan B's 10 proposals (NOT this plan's; nothing here creates them; the prediction is verified against `P0` at Plan B's own authoring, never inherited from here).
- **Never write a bare numeral in 329–346 without its namespace** ("entry 329", "proposal 337"). This plan's own bellows id is a third space.
- Derivation, not a gate: every step keys on the parser diff and `source_heading`, never a predicted id; heading wins on any disagreement.

### Residual risk register
- **Best verified:** every number above produced this session by running the real code read-only against live canonical (the 10/0/271 rolled-back dry run; E0/P0 with `sqlite_sequence` agreement; the 8-status zero-emitting distribution; NT/STALE/DUP; entry-328's hash and its single parsed match; three pins; 10/10 em-dash; 2 hostile headings; 55 tests passed; the fingerprint below; glob 12; candidate pool 271; signature by `inspect`).
- **Not carried:** the placement scout, tag precedents, routing analysis — Plan B's, authored from the landed work list.
- **⚠️ The batch fingerprint is the plan's positional guard** (Step 1a-bis item 1b) — counts alone cannot see a swap.
- **⚠️ GENUINELY NEW SINCE 381 — A PARALLEL TERMINAL IS ACTIVE:** it shipped plans 393–396 (invoice-pulse) during this session and pushed two root commits after this batch landed. It shares **no lessons-forge store** (verified: all four plans target `/Users/marklehn/Developer/GitHub/invoice-pulse`), but it **does share the root repo**, so root HEAD may move in-window. G2's arm is the defense and it is CONDITIONAL: a HEAD mismatch whose path diff leaves `LESSONS.md` untouched is a reconcile-note; a diff TOUCHING `LESSONS.md` invalidates the fingerprint premise → HALT. Measured at authoring: root HEAD `3dca7f3`, and the two in-window commits (`5f7df30`, `3dca7f3`) left `LESSONS.md` untouched (`git diff --stat 058ac9d..3dca7f3 -- LESSONS.md` empty).

**Scope discipline:** cycle run only. Routes stay `NULL`; **no `insert_proposal` anywhere in this plan.** Do NOT edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py`, or `bellows/gates.py`. Do NOT touch proposals 98/121/130 (`stale`, settled). **⚠️⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is fingerprint-pinned, and PLANNER_TEMPLATE v4.88's corpus-freeze rule codifies exactly this prohibition.

**Concurrency:** dispatch with NO other lessons-forge cycle in flight (queues measured at authoring: 390–396 all closed or halted, none in_progress, none targeting lessons-forge). The parallel terminal's invoice-pulse work is store-disjoint; see the risk register's root-HEAD note.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict (`pause_for_verdict` is a header contract the runtime does not police).
- At every gate re-assert `accepted|codify` count is **0** (one command; a non-zero means in-window routing — investigate before continuing).
- After QA, confirm `lessons-forge/knowledge/FORWARD.md` gained **ZERO rows** (re-run the probe form `grep -c "^| "`, comparing against the value the agent captures at Step 1a — the baseline is a MEASUREMENT the plan takes, not a number this text asserts; a row appearing = the QA agent's habit or a foreign writer — check the transcript FIRST, in that order).
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — additive single-write ingest (T-2 fires); structure-for-structure clone of shipped 381, so T-8 silent; no T-5/T-6 surface. Walk-0 clone-diff run against 381 (origin = newest same-class, both roles verified by ship date), all deltas enumerated in the FALSE-HERE table above.

**Walk register:** `governance/knowledge/research/walk-register-cycle-ingest-s42sweep-2026-08-13.md` (schema **0.3** — the version this session shipped; the verbatim-ellipsis annotation is available and used where pre-image bytes carry display-prefix ellipses), committed per phase.

**Walk 0 (context pin):** the FALSE-HERE table IS the pin — E0/P0 328/336, NT 0, STALE 3, DUP 19, batch 10/0/271 over 281 parsed at positions 272–281, fingerprint `578148c3…`, sentinel entry-328 `63b3831d…` (1 parsed match), three doctrine pins (DC moved to v2.9 by 391, PT moved to v4.88 by 389, R20 unchanged fifth cycle), 10/10 em-dash, 2 hostile ids (330/335), glob 12, candidate pool 271, `detect_duplicates` signature by `inspect`, tests 55 passed, root HEAD `3dca7f3` with `LESSONS.md` porcelain clean and untouched in-window, lessons-forge `decisions/` zero non-Done. Clone-diff verdict vs 381: 1 inherited premise measured FALSE and re-scoped (item 10 — the "both repos clean" claim; the single-writer check's scope now stated explicitly), 1 inherited obligation de-asserted (the FORWARD baseline is now agent-measured rather than plan-asserted — 381 hardcoded 18), everything else carried re-tokened. **Scout seat: DECLINED — T1, small surface, proven clone at the 381 form; the cold panel is not owed at T1** (the decline is recorded per §2.0, and the batch-size delta 4→10 changes no step's structure — every guard is count-parameterized, verified per guard at walk 1).

**Walks (2 warm):**
- Weak spots:          w1 dry (every count-parameterized guard re-verified against the 10-batch); w2 dry.
- Destruction:         w1 dry (both subtractions stricten or de-risk: the premise re-scope narrows a claim without weakening the check; the FORWARD de-assertion replaces a stale constant with a live capture); w2 dry.
- Vulnerabilities:     w1 1 folded — **record-class, and it is evidence: the v0.3 marker-collision channel priced in the schema THIS SESSION fired on the FIRST register written after the feature shipped** (a row that MENTIONED the marker while describing the class was read as attesting; the verdict was correct by accident, which is the dangerous mode). Folded to a deliberate attestation; recorded for the corpus. Battery re-run live (10/0/271, fingerprint, sentinel, pool 271, signature, glob 12, tests 55, pins 3/3); w2 dry.
- Integration-record:  w1 dry (lineage extended; v4.88 corpus-freeze citation verified live; stray-origin-token sweep zero operative hits); w2 dry.
- ACID:                w1 dry (one write step, one gate window; the G2 arm models the live parallel terminal); w2 dry.

- **Walks 3–4 (the conformance re-open):** w3 1 folded — **INSTRUCTION-class clone-drift the walk-0 diff could not see: the origin ships project-PREFIXED Deposits paths and this draft dropped the prefix on all six** (six (o2) advisories measured by the first lint run; the clone-diff had compared guards and counts, not path FORM). Fixed, re-measured EXIT 0 / zero WARNs — the origin's earned state. w4 all five lenses dry.

**Splits: w1 instruction 0 / record 1 · w2 dry · w3 instruction 1 / record 0 (bar UNMET, re-opened) · w4 dry.** The bar is met at walk 4 with nothing restructured.

**Conformance (§5):** faithful-mirror plan_lint at the deposit-shaped scratchpad mirror — **NEVER at the real `decisions/`** (the daemon claims and DISPATCHES a plan-shaped file same-second, proven live twice this session). Mirror faithful by construction for (q) — the resolver takes the project repo from the `Project:` header, not the file's location. First run (post-walk-2): EXIT 0 with SIX (o2) advisories — folded as instruction-class (f6, the Deposits path form), re-opening the walk. Final run (post-walk-4, at the freeze): **EXIT 0, ZERO WARNs, (o1) fired=0** — the advisory set is EARNED, not pre-classified away. (q) telemetry — the two moved doctrine pins `result=ok` verified against the live files (the truncated-prefix form was caught and fixed at walk 0, f3), R20 `result=ok`, sentinel + fingerprint tokens `ambiguous` (telemetry-only, correct: a DB value and a derived digest, neither having a file to verify).

**Closing:** walk 4 read dry on every lens — **instruction 0 / record 1: this Cycle-Log fill itself, written at close with measured content** (0 of 1 fold-introduced — the fill is the close's own act, named per §2's bar); the closing-record re-read ran against the filled block; clone-diff at walk 0 per §2.0; scout declined with reasoning at walk 0; fold-and-deposit exactly once.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Lessons Agent (ingest the 10; NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1-2 sentences): starting, and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.** Run from your own working tree; the only main-tree writes are the `.backup` and the DB mutation (both gitignored).
>
> **⚠️ EXECUTION ORDER — exactly: Step 0 → 1a → 1a-ter → 1a-bis → G2 → G1 → 1b (the only mutation) → G3–G6 → the ONE deposit.** ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning the full 10-id work list is this plan's CORRECT closing state.
>
> **Step 0 — dispatch state.** Probe three places (capture every exit code; silence is not a determination): (1) `git -C <your worktree> show HEAD:knowledge/development/dev-log-cycle-s42-step-1-2026-08-13.md`; (2) the working tree; (3) `git log --all -- <that path>` PLUS `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'` — probe 3's exit code carries NO signal; pair with a positive control against `knowledge/FORWARD.md` and only then read silence as no-hit. Any hit → RESUME (the stub's recorded values are authoritative). All absent → FRESH. State the determination first in the dev log.
>
> **Single-writer check (scope stated — item 10):** (1) `get_unclassified_entries` stable across two reads; (2) `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY; other repos' `decisions/` contents are irrelevant to it and two such files legitimately exist elsewhere.** This plan's OWN renamed file present is the normal state; **ZERO matches means the probe is broken** (re-verify the path); **any OTHER match → HALT** (lessons-forge `decisions/` measured clean of parked files at authoring).
>
> **⚠️ HALT DURABILITY:** on any HALT, commit existing deposit files by explicit pathspec; record the gate, its measured value, and whether the ingest committed. **DO NOT REPAIR — authorized writes: the `.backup`, `run_full_lessons_cycle`, this step's deposit.**
>
> **Scope:**
> - `knowledge/development/dev-log-cycle-s42-step-1-2026-08-13.md`
>
> ### Step 1a — restore point, then baseline
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<id>-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> `<id>` = this plan's ACTUAL id from your plan filename. Do NOT inline `$(date …)` between single-quoted parts. VERIFY: `sqlite3 "file:<backup>?immutable=1" 'PRAGMA integrity_check;'` → `ok` (⚠️ `?immutable=1`, never `?mode=ro`, for backup reads — sidecars absent); backup counts == live counts (fresh: **328 entries / 336 proposals**; on RESUME do not assert them). Resume glob: `-<id>-` token, ends `.db`, EARLIEST match, prove pristine by `MAX(id)` = 328/336.
>
> **Baseline capture (read-only, raw output):** (1) the zero-emitting status distribution over ALL EIGHT statuses (expected: implemented 275 · superseded 28 · rejected 15 · reference 15 · stale 3 · accepted 0 · proposed 0 · ambiguous 0); (2) proposals by category; (3) total `lesson_entries` (328); (4) sentinel entry 328 hash == `63b3831d2ddfdd553d9b8904df40723dbbd50d6fa442db72f2d16cfeb8762d26` (mismatch = HALT, not correction); (5) `STALE_COUNT=3` labelled; (5b) `SURFACEABLE_BASE=0` labelled; (6) `E0 = MAX(id) FROM lesson_entries` == **328**, `P0` == **336** (differing → HALT — but on a "fresh" read of E0=338, search `bellows-preserved/*` for the stub before diagnosing); (7) **NT capture:** `SELECT 'NT_COUNT=' || COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous');` → printed token required; silence = broken invocation → HALT; (8) **FORWARD baseline:** `grep -c "^| " /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/FORWARD.md` — record the number raw (the Planner's wrap re-runs this exact probe form against this capture; do not assert any expected value). **Capture only — G1 owns the verdict.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write + `git commit` the stub `knowledge/development/dev-log-cycle-s42-step-1-2026-08-13.md`: `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)`; the absolute backup path; E0/P0; the NT_COUNT line; STALE_COUNT; SURFACEABLE_BASE; the FORWARD baseline; the full status/category distribution; the sentinel hash; **the three doctrine pins — `shasum -a 256` on `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}`, raw, HALT unless all three print** (G2 and the Receipt CITE this capture; neither re-measures). **THE OVERWRITE RULE:** the final Receipt rewrites this file but carries any first-dispatch ingest dict forward verbatim; on a resume the stub's values are authoritative.
>
> ### Step 1a-bis — pre-ingest guard (read-only)
> 1. From your worktree, `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` (the same parser the ingest calls); tally the whole-corpus dry run by `source_heading` lookup. **FRESH → assert `would_insert == 10` AND `would_update == 0`** (Planner measured 10 / 0 / 271 over 281 parsed). **RESUME → `would_update == 0` and `would_insert ∈ {0, 10}`** — anything in 1..9 = foreign writer → HALT. ⚠️ `would_update == 0` stays load-bearing as a plan-204-regression detector even with NT empty.
> 1b. **THE BATCH FINGERPRINT:** sha256 of `"\n".join(<would-insert headings in parse order>)`. **Expected `578148c3135cc8f6e923ed1ebfb262ce17c2d7f16b6f0c6412824af9afce28fa`** (first heading starts `2026-08-13: One action per ops compound`, last starts `2026-08-13: The daemon claims an uncommitted deposit`). Mismatch → HALT (the batch is not the batch this plan pinned; a legitimate post-authoring append is still a HALT — CEO re-parameterizes). **RESUME with `would_insert == 0` → the digest of the empty string can never match: SKIP, record `FINGERPRINT SKIPPED (post-ingest resume)`.**
> 2. **Sentinel:** parsed entry matching entry 328's heading — exactly 1 match, hash equal → PASS; else HALT (classify whitespace-only vs substantive).
> 3. **Duplicate pre-check, both paths:** (a) pre-existing ids — mirror the ingest's candidate construction (parsed-and-matched; ~**271** ids; PRINT the list length first, HALT if 0 or wildly off — the function's empty-list early-return examines nothing); `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. (b) the 10 parsed batch entries (no ids yet — replicate the detector's current source read-only; reference at ABSOLUTE `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`): criterion 1 reported as **UNFALSIFIABLE (reference carries no Tag: lines — inert)**, criterion 2 the `_EM_DASH_SEP` title-substring — **all 10 headings carry the separator; the whole-heading fallback does not fire on this batch.** Any hit → HALT. **POSITIVE CONTROL from ONE read:** byte length + the LOWERCASE sentinel `orchestration plan rules` in the lowered in-memory string (the detector lowercases; a cased probe against it is entry-303's class); zero length or missing sentinel → every zero is void → HALT.
> 4. Record actuals — measured numbers, never a pre-composed "empty" string.
>
> ### Gates run pre-mutation
> - **G2 — provenance:** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (didn't run); non-empty output → HALT (never ingest an uncommitted corpus). Record `rev-parse --short HEAD` (authoring: `3dca7f3`; **a mismatch is EXPECTED — a parallel terminal shares this repo**: run the path diff `git -C /Users/marklehn/Developer/GitHub diff --stat 3dca7f3..HEAD -- LESSONS.md` — empty → reconcile-note and PROCEED; non-empty → HALT, the fingerprint premise fell). Confirm the stub carries the three pins.
> - **⚠️⚠️ G1 — the non-terminal precondition:** capture `NT_COUNT` and `STALE_COUNT`. Arms in order, first match wins: (1) **`NT_COUNT == 0` AND `STALE_COUNT == 3`** → PASS (on a step-0 RESUME record `PASS (resume, pre-mutation)`). (2) **`NT_COUNT > 0`** → HALT naming every id, status, route — with NT empty at authoring, ANY non-terminal row is in-window foreign routing; no carve-out exists on this run. (3) **`STALE_COUNT != 3`** (either direction) → HALT.
>
> ### Step 1b — the ingest (ONCE)
> Open canonical read-WRITE. **`run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()`. **IMMEDIATELY append the verbatim returned dict to the stub and commit it again** (the dict is unreproducible). Print all seven keys. ⚠️ **Re-verify the function against live source before running** (authoring source-read: parses → ingests → builds candidate ids from parsed-and-matched → `detect_duplicates` → inserts a `duplicate` proposal per hit → returns `get_unclassified_entries`; it does NOT classify) — changed behaviour → HALT.
>
> ### Post-mutation gates (report EVERY gate as a table row; run all before halting)
> - **G3 — `duplicates_marked_count == 0`**; scoped resume form `SELECT COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 328` (whole-corpus DUP is 19 by baseline and would false-HALT). A zero is valid ONLY against 1a-bis's positive control; control absent → `HALT (unverified)`.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty** (detector; on failure diff `status='stale'` vs baseline, name the backup).
> - **G5 — work exists:** `ingested_count == 10` → PASS. `== 0` + Complete receipt (DB-confirm `COUNT(*) WHERE id > 328` == 10) → idempotent re-dispatch note, stop. `== 0` + stub/absent receipt → deposit-completion resume: regenerate the Receipt FROM THE STUB (pins never re-measured; dict verbatim or declared absent; E0/P0/backup/sentinel/STALE/SURFACEABLE/FORWARD/distribution all stub-sourced). **∉ {0, 10} → HALT.**
> - **G6 — work-list reconciliation:** every id in `needs_classification` is `> 328` and `≤ 338` (range computed from confirmed E0, never from the list). Outside-range → HALT; write the `### Deferred entries (G6 candidate)` section (bare ids, one per line; approval = the CEO continue on this halt) AND the arithmetic 10-line ingested-entry anchor.
>
> **Self-report:** `SELECT id, source_heading FROM lesson_entries WHERE id > 328 ORDER BY id` → **10 rows (329–338)**, recorded as `- ingested entry=<id>` lines; `get_unclassified_entries()` == exactly those 10, verbatim. **Receipt status from the CLOSED SET** (Complete / Complete-idempotent / Partial-HALTED-at-gate / Partial-in-flight-stub), carrying: the dict verbatim; the G1–G6 table; the baseline distribution + sentinel + STALE + SURFACEABLE + FORWARD; E0/P0; the NT_COUNT line; the 10-line anchor; the backup path labelled `pristine (pre-cycle)`; `#### Files Created or Modified` split `##### Committed deposits` / `##### Untracked artifacts`; flags; `#### Doctrine pins` verbatim from the stub. RAW output throughout; canonical Python file-write, no heredoc; commit by explicit pathspec with post-commit `git show --name-only --format= HEAD` + `git rev-parse --show-toplevel`. `#### Prompt Feedback` in `### Ledger Updates`. `#### Forward Register`: `NONE`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-cycle-s42-step-1-2026-08-13.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

## STEP 2 — QA

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`), with the single G6-deferral exception (`HALTED at G6` token + a `### Deferred entries (G6 candidate)` section — this step running IS the approval; open your message with `OPERATING UNDER G6 DEFERRAL: ids <list>`).
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, absolute path). **Verification + reporting only; a failing check is reported, never fixed. No Monitor. No classification.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-ingest-s42sweep-2026-08-13`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-ingest-s42-qa-2026-08-13.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/`; `required_evidence_files` `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]`. All four files AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim in the deposited report; end with the self-grep. ⚠️ Rule 19 verbatim: a check you cannot complete is `❌` with a reason, never a hedged `✅`. Status column exactly one glyph; no `|` in table cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-ingest-s42-qa-2026-08-13.md`
> - `knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/invariants.txt`
> - `knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/schema.txt`
>
> **IN-WINDOW RECONCILIATION:** whole-corpus rows adjudicate in two parts — (a) HARD by id against Step 1's 10-line anchor (validate: 10 integers, none blank; missing/truncated → dependent rows `❌ (unverifiable)`, NO predicate fallback); (b) RECONCILE everything outside the set (report, note, still `✅`).
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — scoped to the Receipt's `##### Committed deposits`; per path `git log --oneline -1 -- <path>` (empty = ❌) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"`.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY (baseline 55 passed at authoring; delta reported never asserted).
> 2. ⚠️⚠️ **`get_unclassified_entries(conn)` returns EXACTLY the 10 ids — NOT `[]`.** The inversion every prior cycle QA invites: an empty work list means something CLASSIFIED the batch, which nothing here is authorized to do. `[]` → ❌ Critical.
> 3. **The 10 landed, only those** — `SELECT id, source_heading FROM lesson_entries WHERE id IN (<the 10>)` → 10 rows, headings equal to the anchor **bound as query parameters** (two carry apostrophes — predicted ids 330/335); reconcile `COUNT(*)` derivation `328 + 10 = 338`. → `invariants.txt`
> 4. **Plan-204 held, NO proposal created** — stale still 3 (98/121/130); entry-328 hash `63b3831d…` unchanged; dict's `updated_count`/`terminal_proposals_flagged` from the Receipt; ⚠️⚠️ **`SELECT COUNT(*) FROM lesson_proposals` == 336 UNCHANGED** (337+ means the detector fired and G3 should have halted); **the FULL zero-emitting 8-status distribution before/after, every bucket unchanged against the Receipt's item — a count is not a value guard**; `NT_COUNT` still 0. → `hash-trap.txt`
> 5. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`.
> 6. **Fingerprint provenance** — recompute the batch fingerprint over the 10 anchor headings read FROM THE DB (parse order = id order): == `578148c3…`; and `LESSONS.md` porcelain still clean at root.
> 7. **Corpus-freeze posture** — `accepted|codify` count still **0**; this plan's own `in-progress-executable-<id>.md` is the ONLY non-Done entry in **lessons-forge's** `decisions/` (other repos out of scope — item 10; any other lessons-forge match = in-window deposit, report names).
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-ingest-s42-qa-2026-08-13.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/hash-trap.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s42sweep-2026-08-13/schema.txt`
