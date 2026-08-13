# Lessons Forge — Cycle Run 2026-08-13, PLAN A: ingest the 4-entry session-40 sweep batch (classification held to Plan B)

**Date:** 2026-08-13 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 4) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-ingest-s40sweep-2026-08-13`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Ingest only.** This plan takes the 4 un-ingested `LESSONS.md` entries (the session-40 sweep batch, appended 2026-08-13 at root commit `a2f5c57`) into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**, authored against the work list this plan leaves behind. The A/B split is carried from the 339/340→357/359 lineage — the split collapses the verdict-gate guard matrix to ONE write step, ONE gate, ONE window — and is kept even at 4-entry scale because the newest same-class shipped that way and the structural reason (not the batch size) was the licence.

**Clone lineage — measured, not recalled:** 247 → 257 → 274 → 281 → 283 → 288 → 296 → 311 → 339 → **357** (direct origin AND newest same-class; both roles resolve to the same plan, verified against `Done/` at authoring). Cycle-class diff run at walk 0, every inherited fact RE-MEASURED 2026-08-13 read-only against live canonical.

### ⚠️⚠️ INHERITED FACTS FROM 357 THAT ARE FALSE HERE — every one re-measured 2026-08-13

1. **THE BATCH IS 4, uniform and late:** all four dated 2026-08-13, appended after the last ingest at root commit `a2f5c57`, sitting at file positions 268–271 of 271 parsed. Dry run measured **would_insert 4 / would_update 0 / unchanged 267** over 271 parsed headings. **Never derive the batch from a date filter; the parser diff is authoritative.**
2. **BASELINES MOVED:** `E0 = 324`, `P0 = 332` (`sqlite_sequence` agrees on both). Status distribution (zero-emitting, all EIGHT schema statuses): implemented **271** · superseded **28** · rejected **15** · reference **15** · stale **3** · accepted **0** · proposed **0** · ambiguous **0** — total 332. **`SURFACEABLE_BASE = 0`** (proposed + ambiguous). `STALE_COUNT = 3` (proposals 98/121/130, settled 2026-07-16 — leave untouched). Whole-corpus `DUP_COUNT = 19` (baseline, UNCHANGED since 357; G3 uses the batch-scoped form).
3. **`NT` REMAINS EMPTY — `NT_COUNT = 0`, re-measured, not inherited.** Every proposal is terminal, the 357/359 batch's six (proposals 327–332) included — the claim rests on the live NT read alone, not on per-id flip recall. Per 339's doctrine that safety is a MEASUREMENT, not a construction: `would-UPDATE = 0` re-measured immediately pre-mutation (Step 1a-bis), G1 re-asserts `NT_COUNT = 0` live. G1's arms are carried from 357's empty-NT rebuild, not from 339's 42-row arms.
4. **THE HASH-TRAP SENTINEL MOVES TO ENTRY 324** — DB content-hash `04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a` (a corpus value, not a file digest — no file pin exists for it), heading `2026-08-12: The warm walk's mechanical/judgment split transfers to the panel — four structures that cut the replication layer without touching discovery [tag: drafting-cycle]`. Named by id, never `MAX(id)`. Not file-last (the 4 follow it), so the trailing-separator trap cannot reach it; regression sentinel for `_normalize_for_hash` only. (357's sentinel was entry 318; 324 is the newest ingested entry with a DB-recorded content-hash and sits directly before this batch.)
5. **THE EM-DASH UNIFORMITY HOLDS: 4 of 4 headings carry ` — `** (measured per-heading, not assumed from the streak). The whole-heading fallback branch of `detect_duplicates` does not fire on this batch; say so rather than reporting a uniform "no hits."
6. **ONE OF THREE DOCTRINE PINS MOVED** — each measured at authoring against the live tree; the agent re-measures at Step 1a-ter; these are the authoring reference:
   - v2.7, moved by plan 373 (357 pinned `817677db…` v2.5):
     `shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` → `5d4c8d8c0598c4853dc536c23f4640b6936d2d6d1b1e9b2ffd4f373e319f612c`
   - v4.87, **unchanged second cycle**:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` → `8aac8aa9f107fc9b7b4dc7b7241ea9a253d57d07aab2877c81b748a88f84a58e`
   - **unchanged fourth cycle running**:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` → `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0`
7. **TWO HEADINGS ARE SHELL-HOSTILE** (apostrophes only — no quotes, no backticks): batch positions 1 and 2 → predicted entry ids **325, 326**. Bind headings as query parameters everywhere; never interpolate into a shell string.
8. **THE BACKUP GLOB POPULATION IS 11** (was 10 at 357; the glob is `data/backups/lessons-forge-pre-cycle-*.db` — the directory's raw file count is 50 with sidecars and other names, and probing the wrong representation returns that confident wrong number). The count is NOT the guard; the id token `-<id>-` is. Derive resume dates from the actual filename, never the local dispatch date.
9. **`detect_duplicates` SIGNATURE UNCHANGED:** `(conn, entry_ids, reference_files=None)` — verified against live source at authoring; the candidate pool of parsed-and-matched ids measured **267** (the 357 batch's 6 now match; the orphan gap is unchanged and reconciled by the parser diff itself).
10. **⚠️ `decisions/` IS CLEAN — the halted-file carve-outs are DELETED, premise measured absent:** plans 374/375 archived every parked halted file (verified at authoring: zero non-Done entries in both repos' `decisions/`). 357's "halted-executable-334.md is expected and parked" exception language does NOT carry. The single-writer check and QA row 7 below expect this plan's OWN in-progress file as the ONLY non-Done entry; ANY other match → HALT.

### ⚠️ NUMBERING — one band, stated once
- **`lesson_entries.id` 325–328** — THIS batch's 4 entries (after ingest; assigned in parse order, verified by source read: `ingest_lesson_entries` iterates the parser's list with AUTOINCREMENT).
- **`lesson_proposals.id` 333–336** — Plan B's 4 proposals (NOT this plan's; nothing here creates them; the prediction is verified against `P0` at Plan B's own authoring, never inherited from here).
- **Never write a bare numeral in 325–336 without its namespace** ("entry 325", "proposal 333"). This plan's own id and the 374–379 housekeeping ids are a third space.
- Derivation, not a gate: every step keys on the parser diff and `source_heading`, never a predicted id; heading wins on any disagreement.

### Residual risk register
- **Best verified:** every number above produced this session by running the real code read-only against live canonical (the 4/0/267 dry run; E0/P0 with `sqlite_sequence` agreement; the 8-status zero-emitting distribution; NT/STALE/DUP; entry-324's hash; three pins; 4/4 em-dash; 2 hostile headings; 55 collected tests; fingerprint below).
- **Not carried:** the placement scout, tag precedents, routing analysis — Plan B's, authored from the landed work list.
- **⚠️ The batch fingerprint is the plan's positional guard** (Step 1a-bis item 1b) — counts alone cannot see a swap.
- **Genuinely new since 357:** the clean-`decisions/` posture (item 10) and the dispatcher-side changes (the daemon now runs the NONE/empty receipt guard and the disk preflight, plans 376/379 — environment hardening; no step in this plan keys on either).

**Scope discipline:** cycle run only. Routes stay `NULL`; **no `insert_proposal` anywhere in this plan.** Do NOT edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py`, or `bellows/gates.py`. Do NOT touch proposals 98/121/130 (`stale`, settled). **⚠️⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is fingerprint-pinned, and PLANNER_TEMPLATE v4.87's corpus-freeze rule codifies exactly this prohibition.

**Concurrency:** dispatch with NO other lessons-forge cycle in flight (queues measured EMPTY at authoring; no parallel terminal known active). **Root HEAD at authoring `a2f5c57` — a HEAD mismatch at G2 is a reconcile-note, not a halt, IF the path diff shows `LESSONS.md` untouched; a diff touching `LESSONS.md` is a fingerprint-invalidating append → HALT.**

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict (`pause_for_verdict` is a header contract the runtime does not police).
- At every gate re-assert `accepted|codify` count is **0** (one command; a non-zero means in-window routing — investigate before continuing).
- After QA, confirm `lessons-forge/knowledge/FORWARD.md` gained **ZERO rows** (baseline 18 pipe-lines at authoring by `grep -c "^| "` — re-run the SAME probe form; this plan emits none; a row appearing = the QA agent's habit or a foreign writer — check the transcript FIRST, in that order).
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — additive single-write ingest (T-2 fires); structure-for-structure clone of shipped 357, so T-8 silent; no T-5/T-6 surface. Walk-0 clone-diff run against 357 (origin = newest same-class, both roles verified), all deltas enumerated in the FALSE-HERE table above.

**Walk 0 (context pin):** the FALSE-HERE table IS the pin — E0/P0 324/332, NT 0, STALE 3, DUP 19, batch 4/0/267 over 271 parsed, fingerprint `ae15bf50…`, sentinel entry-324 `04d2bff7…`, three doctrine pins (DC moved to v2.7, PT+R20 unchanged), 4/4 em-dash, 2 hostile ids (325/326), glob 11 (pre-cycle form), tests 55 collected, root HEAD `a2f5c57`, `detect_duplicates(conn, entry_ids, reference_files=None)` signature verified, `decisions/` zero non-Done both repos. Clone-diff verdict: 1 deletion-with-premise-measured-absent (the halted-334 carve-outs — item 10), G1 carried from 357's empty-NT rebuild (premise re-measured TRUE here), everything else carried re-tokened. **Scout seat: DECLINED — T1, small surface (a proven clone at 4-entry scale, single-write), per the 376/377/379 precedent; the cold panel is not owed at T1.**

**Walk 1** (whole artifact, five lenses, sequential):
- Weak spots:          w1 2 folded — instruction (item 3 carried a per-id flip narrative only partially verified: the inherited-label class; rewritten to rest on the live NT read alone. The FORWARD-baseline obligation named a number without its probe form; the form — `grep -c "^| "` = 18 — is now stated so the wrap re-runs the same probe).
- Destruction:         w1 dry (single INSERT path; backup verified before mutation; the one subtraction — the halted-334 carve-outs — is premise-measured-absent AND strictens the check: with `decisions/` clean, any non-self match is a real foreign writer).
- Vulnerabilities:     w1 1 folded — instruction (the backup-glob population was probed at the WRONG representation: raw `ls | wc -l` = 50 vs the actual `-pre-cycle-*.db` glob = 11; the probe-must-match-representation class, caught by re-deriving the probe from 357's stated glob). Battery re-run live this session: positions 268–271 measured (not derived), `entry_id` column present, `_EM_DASH_SEP` = ` — ` in live source, `run_full_lessons_cycle` seven dict keys confirmed by source read, PT lowered-sentinel present, `get_unclassified` = [] pre-state.
- Integration-record:  w1 dry (lineage table verbatim-extended with 357; the v4.87 corpus-freeze citation verified live — PT sha unchanged second cycle; deposits blocks name every expected file inline; no stray origin tokens — swept mechanically for 318/319/1e3eb3de/260857bb/cold-panel).
- ACID:                w1 dry (one write step, one gate window; G1–G6 ordering carried from 357 with G2/G1 pre-mutation; the G2 HEAD-mismatch arm is now CONDITIONAL on the path diff — a `LESSONS.md`-touching diff HALTs since it invalidates the fingerprint premise, a stricter form than 357's blanket reconcile-note; the backup is the durability floor).

**Walk-1 split: instruction 3 / record 1** (the record item: file positions 268–271 moved from derived to measured, no text change). Direction verdict: **PROCEED**. Re-opens; walk 2 owed.

**Walk 2** (whole artifact; new surface = the walk-1 folds):
- All five lenses:     w2 dry — the three folded regions re-read coherent (item 3's claim now rests on a measurement, item 8 carries the glob form, the pin line and obligations agree); no guard relaxed by any fold; no new numbers introduced unmeasured; token sweep re-run clean; ACID schedule untouched by folds.

**Walk-2 split: instruction 0 / record 1: this Cycle Log's own fill, written at close with measured content (no placeholder rows).**

**Conformance (§5), first run (post-walk-2):** at the deposit-shaped scratchpad mirror (NEVER at the real `decisions/` — the daemon claims and DISPATCHES a plan-shaped file same-second, proven live 2026-08-12). Mirror faithful: the four real files copied in (`src/test_lessons_forge.py`, `src/db.py`, `agents/FORGE_LESSONS_AGENT.md`, `knowledge/FORWARD.md`); for check (q) the mirror is faithful BY CONSTRUCTION — the resolver takes the project repo from the `Project:` header, not the file's location, so the mirror result IS the deposit result. First run: EXIT 0, five (q) WARNs — the doctrine pins written in 357's one-line form resolve against the wrong file (they misattribute to a relative `DRAFTING_CYCLE.md` the project repo lacks), and the resume token `FINGERPRINT=n/a` parsed as a path. **Folded (instruction-class — the resume token is an agent-written string): the pin block restructured to per-pin `shasum <absolute path>` lines the resolver verifies, and the resume token reworded slash-free. Re-opens; walk 3 owed.**

**Walk 3** (whole artifact; new surface = the conformance folds):
- All five lenses:     w3 dry — 1a-ter's instruction agrees with item 6's per-pin commands; the sentinel's "no file pin exists" clarification strengthens, relaxes nothing; item renumbering (em-dash 5, pins 6) leaves every cross-reference intact (items 3/8/10 cited elsewhere are untouched); the fingerprint reword drops only an explanatory literal, the SKIP semantics carried; no gate, guard, or schedule element touched.

**Walk-3 split: instruction 0 / record 1** (this walk's own Cycle Log row). The walk phase meets the §2 bar on the dry branch; T1, no panel owed.

**Conformance (§5), final run (post-walk-3, at deposit):** EXIT 0, **ZERO WARNs**, (q) telemetry EARNED — doctrine pins 3/3 `result=ok` verified live against the actual files; sentinel + fingerprint tokens `ambiguous` (telemetry-only — correct: DB value and derived digest, no file to verify); (o1) fired=0.

**Closing:** walk 3 dry — instruction 0 / record 1 (the walk-3 Cycle Log row, this line's own account); closed on the dry branch after 3 walks; clone-diff at walk 0 per §2.0; scout declined with reasoning at walk 0; residue: none.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Lessons Agent (ingest the 4; NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1-2 sentences): starting, and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.** Run from your own working tree; the only main-tree writes are the `.backup` and the DB mutation (both gitignored).
>
> **⚠️ EXECUTION ORDER — exactly: Step 0 → 1a → 1a-ter → 1a-bis → G2 → G1 → 1b (the only mutation) → G3–G6 → the ONE deposit.** ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning the full 4-id work list is this plan's CORRECT closing state.
>
> **Step 0 — dispatch state.** Probe three places (capture every exit code; silence is not a determination): (1) `git -C <your worktree> show HEAD:knowledge/development/dev-log-cycle-step-1-2026-08-13.md`; (2) the working tree; (3) `git log --all -- <that path>` PLUS `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'` — probe 3's exit code carries NO signal; pair with a positive control against `knowledge/FORWARD.md` and only then read silence as no-hit. Any hit → RESUME (the stub's recorded values are authoritative). All absent → FRESH. State the determination first in the dev log.
>
> **Single-writer check:** (1) `get_unclassified_entries` stable across two reads; (2) `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **this plan's OWN renamed file present is the normal state; ZERO matches means the probe is broken** (re-verify the path); **any OTHER match of any kind → HALT** (`decisions/` measured clean of parked files at authoring — no carve-out exists on this run).
>
> **⚠️ HALT DURABILITY:** on any HALT, commit existing deposit files by explicit pathspec; record the gate, its measured value, and whether the ingest committed. **DO NOT REPAIR — authorized writes: the `.backup`, `run_full_lessons_cycle`, this step's deposit.**
>
> **Scope:**
> - `knowledge/development/dev-log-cycle-step-1-2026-08-13.md`
>
> ### Step 1a — restore point, then baseline
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<id>-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> `<id>` = this plan's ACTUAL id from your plan filename. Do NOT inline `$(date …)` between single-quoted parts. VERIFY: `sqlite3 "file:<backup>?immutable=1" 'PRAGMA integrity_check;'` → `ok` (⚠️ `?immutable=1`, never `?mode=ro`, for backup reads — sidecars absent); backup counts == live counts (fresh: **324 entries / 332 proposals**; on RESUME do not assert them). Resume glob: `-<id>-` token, ends `.db`, EARLIEST match, prove pristine by `MAX(id)` = 324/332.
>
> **Baseline capture (read-only, raw output):** (1) the zero-emitting status distribution over ALL EIGHT statuses (expected: implemented 271 · superseded 28 · rejected 15 · reference 15 · stale 3 · accepted 0 · proposed 0 · ambiguous 0); (2) proposals by category; (3) total `lesson_entries` (324); (4) sentinel entry 324 hash == `04d2bff7a7bfd9552ef5aab0fd099d81214ed97b8fa1a9ee8082e9c218c88c4a` (mismatch = HALT, not correction); (5) `STALE_COUNT=3` labelled; (5b) `SURFACEABLE_BASE=0` labelled; (6) `E0 = MAX(id) FROM lesson_entries` == **324**, `P0` == **332** (differing → HALT — but on a "fresh" read of E0=328, search `bellows-preserved/*` for the stub before diagnosing); (7) **NT capture:** `SELECT 'NT_COUNT=' || COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous');` → printed token required; silence = broken invocation → HALT. **Capture only — G1 owns the verdict.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write + `git commit` the stub `knowledge/development/dev-log-cycle-step-1-2026-08-13.md`: `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)`; the absolute backup path; E0/P0; the NT_COUNT line; STALE_COUNT; SURFACEABLE_BASE; the full status/category distribution; the sentinel hash; **the three doctrine pins — `shasum -a 256` on `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}`, raw, HALT unless all three print** (G2 and the Receipt CITE this capture; neither re-measures). **THE OVERWRITE RULE:** the final Receipt rewrites this file but carries any first-dispatch ingest dict forward verbatim; on a resume the stub's values are authoritative.
>
> ### Step 1a-bis — pre-ingest guard (read-only)
> 1. From your worktree, `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` (the same parser the ingest calls); tally the whole-corpus dry run by `source_heading` lookup. **FRESH → assert `would_insert == 4` AND `would_update == 0`** (Planner measured 4 / 0 / 267 over 271 parsed). **RESUME → `would_update == 0` and `would_insert ∈ {0, 4}`** — anything in 1..3 = foreign writer → HALT. ⚠️ `would_update == 0` stays load-bearing as a plan-204-regression detector even with NT empty.
> 1b. **THE BATCH FINGERPRINT:** sha256 of `"\n".join(<would-insert headings in parse order>)`. **Expected `ae15bf50053fd470a0813287afb745f2ba3736702f4b3a9fb495854ecca3f525`** (first heading starts `2026-08-13: The panel's own fold round is new surface`, last starts `2026-08-13: A transcribed census row transposed`). Mismatch → HALT (the batch is not the batch this plan pinned; a legitimate post-authoring append is still a HALT — CEO re-parameterizes). **RESUME with `would_insert == 0` → the digest of the empty string can never match: SKIP, record `FINGERPRINT SKIPPED (post-ingest resume)`.**
> 2. **Sentinel:** parsed entry matching entry 324's heading — exactly 1 match, hash equal → PASS; else HALT (classify whitespace-only vs substantive).
> 3. **Duplicate pre-check, both paths:** (a) pre-existing ids — mirror the ingest's candidate construction (parsed-and-matched; ~**267** ids; PRINT the list length first, HALT if 0 or wildly off — the function's empty-list early-return examines nothing); `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. (b) the 4 parsed batch entries (no ids yet — replicate the detector's current source read-only; reference at ABSOLUTE `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`): criterion 1 reported as **UNFALSIFIABLE (reference carries no Tag: lines — inert)**, criterion 2 the `_EM_DASH_SEP` title-substring — **all 4 headings carry the separator; the whole-heading fallback does not fire on this batch.** Any hit → HALT. **POSITIVE CONTROL from ONE read:** byte length + the LOWERCASE sentinel `orchestration plan rules` in the lowered in-memory string (the detector lowercases; a cased probe against it is entry-303's class); zero length or missing sentinel → every zero is void → HALT.
> 4. Record actuals — measured numbers, never a pre-composed "empty" string.
>
> ### Gates run pre-mutation
> - **G2 — provenance:** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (didn't run); non-empty output → HALT (never ingest an uncommitted corpus). Record `rev-parse --short HEAD` (authoring: `a2f5c57`; on mismatch run the path diff — `LESSONS.md` untouched → reconcile-note; touched → HALT, the fingerprint premise fell). Confirm the stub carries the three pins.
> - **⚠️⚠️ G1 — the non-terminal precondition (arms carried from 357's empty-NT rebuild, premise re-measured TRUE at authoring):** capture `NT_COUNT` and `STALE_COUNT`. Arms in order, first match wins: (1) **`NT_COUNT == 0` AND `STALE_COUNT == 3`** → PASS (on a step-0 RESUME record `PASS (resume, pre-mutation)`). (2) **`NT_COUNT > 0`** → HALT naming every id, status, route — with NT empty at authoring, ANY non-terminal row is in-window foreign routing; no carve-out exists on this run. (3) **`STALE_COUNT != 3`** (either direction) → HALT.
>
> ### Step 1b — the ingest (ONCE)
> Open canonical read-WRITE. **`run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()`. **IMMEDIATELY append the verbatim returned dict to the stub and commit it again** (the dict is unreproducible). Print all seven keys. ⚠️ **Re-verify the function against live source before running** (authoring source-read: parses → ingests → builds candidate ids from parsed-and-matched → `detect_duplicates` → inserts a `duplicate` proposal per hit → returns `get_unclassified_entries`; it does NOT classify) — changed behaviour → HALT.
>
> ### Post-mutation gates (report EVERY gate as a table row; run all before halting)
> - **G3 — `duplicates_marked_count == 0`**; scoped resume form `SELECT COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 324` (whole-corpus DUP is 19 by baseline and would false-HALT). A zero is valid ONLY against 1a-bis's positive control; control absent → `HALT (unverified)`.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty** (detector; on failure diff `status='stale'` vs baseline, name the backup).
> - **G5 — work exists:** `ingested_count == 4` → PASS. `== 0` + Complete receipt (DB-confirm `COUNT(*) WHERE id > 324` == 4) → idempotent re-dispatch note, stop. `== 0` + stub/absent receipt → deposit-completion resume: regenerate the Receipt FROM THE STUB (pins never re-measured; dict verbatim or declared absent; E0/P0/backup/sentinel/STALE/SURFACEABLE/distribution all stub-sourced). **∉ {0, 4} → HALT.**
> - **G6 — work-list reconciliation:** every id in `needs_classification` is `> 324` and `≤ 328` (range computed from confirmed E0, never from the list). Outside-range → HALT; write the `### Deferred entries (G6 candidate)` section (bare ids, one per line; approval = the CEO continue on this halt) AND the arithmetic 4-line ingested-entry anchor.
>
> **Self-report:** `SELECT id, source_heading FROM lesson_entries WHERE id > 324 ORDER BY id` → **4 rows (325–328)**, recorded as `- ingested entry=<id>` lines; `get_unclassified_entries()` == exactly those 4, verbatim. **Receipt status from the CLOSED SET** (Complete / Complete-idempotent / Partial-HALTED-at-gate / Partial-in-flight-stub), carrying: the dict verbatim; the G1–G6 table; the baseline distribution + sentinel + STALE + SURFACEABLE; E0/P0; the NT_COUNT line; the 4-line anchor; the backup path labelled `pristine (pre-cycle)`; `#### Files Created or Modified` split `##### Committed deposits` / `##### Untracked artifacts`; flags; `#### Doctrine pins` verbatim from the stub. RAW output throughout; canonical Python file-write, no heredoc; commit by explicit pathspec with post-commit `git show --name-only --format= HEAD` + `git rev-parse --show-toplevel`. `#### Prompt Feedback` in `### Ledger Updates`. `#### Forward Register`: `NONE`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-08-13.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

## STEP 2 — QA

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`), with the single G6-deferral exception (`HALTED at G6` token + a `### Deferred entries (G6 candidate)` section — this step running IS the approval; open your message with `OPERATING UNDER G6 DEFERRAL: ids <list>`).
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, absolute path). **Verification + reporting only; a failing check is reported, never fixed. No Monitor. No classification.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-ingest-s40sweep-2026-08-13`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-ingest-qa-2026-08-13.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/`; `required_evidence_files` `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]`. All four files AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim in the deposited report; end with the self-grep. ⚠️ Rule 19 verbatim: a check you cannot complete is `❌` with a reason, never a hedged `✅`. Status column exactly one glyph; no `|` in table cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-ingest-qa-2026-08-13.md`
> - `knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/invariants.txt`
> - `knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/schema.txt`
>
> **IN-WINDOW RECONCILIATION:** whole-corpus rows adjudicate in two parts — (a) HARD by id against Step 1's 4-line anchor (validate: 4 integers, none blank; missing/truncated → dependent rows `❌ (unverifiable)`, NO predicate fallback); (b) RECONCILE everything outside the set (report, note, still `✅`).
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — scoped to the Receipt's `##### Committed deposits`; per path `git log --oneline -1 -- <path>` (empty = ❌) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"`.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY (baseline 55 collected; delta reported never asserted).
> 2. ⚠️⚠️ **`get_unclassified_entries(conn)` returns EXACTLY the 4 ids — NOT `[]`.** The inversion every prior cycle QA invites: an empty work list means something CLASSIFIED the batch, which nothing here is authorized to do. `[]` → ❌ Critical.
> 3. **The 4 landed, only those** — `SELECT id, source_heading FROM lesson_entries WHERE id IN (<the 4>)` → 4 rows, headings equal to the anchor **bound as query parameters** (two carry apostrophes — ids 325/326); reconcile `COUNT(*)` derivation `324 + 4 = 328`. → `invariants.txt`
> 4. **Plan-204 held, NO proposal created** — stale still 3 (98/121/130); entry-324 hash `04d2bff7…` unchanged; dict's `updated_count`/`terminal_proposals_flagged` from the Receipt; ⚠️⚠️ **`SELECT COUNT(*) FROM lesson_proposals` == 332 UNCHANGED** (333+ means the detector fired and G3 should have halted); **the FULL zero-emitting 8-status distribution before/after, every bucket unchanged against the Receipt's item — a count is not a value guard**; `NT_COUNT` still 0. → `hash-trap.txt`
> 5. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`.
> 6. **Fingerprint provenance** — recompute the batch fingerprint over the 4 anchor headings read FROM THE DB (parse order = id order): == `ae15bf50…`; and `LESSONS.md` porcelain still clean at root.
> 7. **Corpus-freeze posture** — `accepted|codify` count still **0**; this plan's own `in-progress-executable-<id>.md` is the ONLY non-Done `decisions/` entry (any other = in-window deposit, report names).
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-ingest-qa-2026-08-13.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/hash-trap.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-s40sweep-2026-08-13/schema.txt`
