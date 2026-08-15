# Lessons Forge — Cycle Run 2026-08-14, PLAN A: ingest the 1-entry residual-bucket batch (classification held to Plan B)

**Date:** 2026-08-14 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest the 1) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-ingest-residual-bucket-2026-08-14`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Ingest only.** This plan takes the **1** un-ingested `LESSONS.md` entry (the residual-bucket lesson, appended 2026-08-14 at root commit `8f40920`) into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification and the report are **Plan B**; Gate-1 routing is a third plan after that.

**Why this batch matters procedurally:** the entry it ingests is the evidence base for a queued `PLANNER_TEMPLATE` change that the Planner authored, evidenced, and benefits from. **The corpus path exists so a non-author routes it at Gate 1** — that is the entire reason this plan exists instead of a direct doctrine edit. The ingest must therefore be exactly as disciplined as a six-entry batch; a batch of one is not a reason to relax a guard.

**Clone lineage — measured, not recalled:** 247 → … → 397 → **411** (direct origin AND newest same-class; both roles resolve to the same plan, verified against `Done/` by ship date — 411 closed 2026-08-14). ⚠️ **This plan was derived by READING 411 SECTION BY SECTION and re-deriving every value, NOT by token-swapping it** — 411's own header records what a token-swapped derivation cost in this lineage (17 of 18 origin-carried findings, one a run-halting BLOCKER).

### ⚠️⚠️ INHERITED FACTS FROM 411 THAT ARE FALSE HERE — every one re-measured 2026-08-14

1. **⚠️⚠️ THE NON-TERMINAL SET GREW — it is EXACTLY `{340, 342, 346, 350, 352}` (5), NOT 411's `{340, 342, 346}` (3). 411's G1 would HALT this run.** Plan 416 routed 350 and 352 `accepted|codify` the same day. G1 stays a **VALUE guard keyed by id**, re-keyed to the measured five: `340` (route `codify`, no target), `342`/`350`/`352` (`codify` → `PLANNER_TEMPLATE.md`), `346` (`codify` → `PLANNER_TEMPLATE.md`). ⚠️ Note `342`'s target is `DRAFTING_CYCLE.md`. A count-only check would pass a foreign in-window row that displaced one of ours — and this cycle proves the count itself is not stable across two same-day plans.
2. **⚠️ THE EM-DASH FALLBACK NOW FIRES FOR THE ENTIRE BATCH — 0 of 1 headings carry ` — `.** 411 was the first batch where it fired at all (3 of 6); here it fires for the only entry, so `duplicates_marked_count` rests **entirely** on the fallback path with no separator-matched control inside the batch. Measured by running the real `run_full_lessons_cycle` against a scratch COPY of canonical: **`duplicates_marked_count = 0`.** That is an EXECUTED result, not an argument.
3. **⚠️ THE HOSTILE CHARACTER CHANGED CLASS — it is a DOUBLE QUOTE, not an apostrophe.** The heading contains `"everything else"`. 411's hazard was `'` (a string-literal break); `"` is worse in one specific place: **in the `sqlite3` CLI, double quotes are IDENTIFIER quoting**, so a heading pasted into a shell-built query can silently resolve as a column name rather than erroring. Bind headings as query parameters everywhere, and never interpolate this heading into a `sqlite3` CLI invocation.
4. **THE BATCH IS 1**, dated 2026-08-14, appended after the last ingest at root commit `8f40920`, at file position **288 of 288 parsed**. Dry run (real `ingest_lesson_entries`, scratch copy): **would_insert 1 / would_update 0 / unchanged 287**.
5. **BASELINES MOVED:** `E0 = 344`, `P0 = 352` (`sqlite_sequence` agrees on both). Status distribution (zero-emitting, all EIGHT statuses): implemented **281** · superseded **28** · reference **20** · rejected **15** · **accepted 5** · stale **3** · proposed **0** · ambiguous **0** — total **352**. **`SURFACEABLE_BASE = 0`** (proposed + ambiguous) ⚠️ **distinct from NT, which is 5** — the two came apart at 411 and stay apart. `STALE_COUNT = 3` (98/121/130).
6. **THE SENTINEL MOVES TO ENTRY 344** — content-hash `e7b607bde3cdaf801fe266d06137b549bab7786accb99356e4eda315351e723d`, heading `2026-08-14: A session that crosses midnight carries a stale date into every slug it authors [tag: operational-recovery]` (it was 411's own batch's last entry). Named by id, never `MAX(id)`; **parsed-match count is measured at Step 1a-bis, not asserted here**; not file-last (this batch's one entry follows it).
7. **THE DOCTRINE PINS MOVED — DRAFTING_CYCLE is now v2.11** (plans 420/421):
   - v2.11, moved since 411 pinned `943971f5…` v2.10:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` → `2501724385f1212e31134fbdfd9c69c38477dbb5c91e0dbaf4c7cc51af2a482d`
   - v4.88, unchanged third cycle:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` → `4f33c3884b426189ba9f019c0722681a4446e5f9223b1f0f10c117f7de0691a0`
   - unchanged seventh cycle running:
     `shasum -a 256 /Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` → `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0`
   ⚠️ **The interleaved descriptor lines are LOAD-BEARING, not decoration: the (q) resolver takes the FIRST path in a token's context window, so three consecutive `shasum` lines make each digest resolve against the PRECEDING pin's path — measured as two false MISMATCHes at 411 before this form was restored.**
   ⚠️ **PT is pinned as UNCHANGED and this plan's own downstream executable will CHANGE it (4.88 → 4.89). That executable must not run before this cycle completes**, or the pin falls between plans in the same arc.
   ⚠️⚠️ **AND THERE IS A SECOND, INDEPENDENT REASON FOR THAT ORDER, which the pin does not cover: `PLANNER_TEMPLATE.md` IS `detect_duplicates`' DEFAULT REFERENCE FILE** (`src/lessons_forge.py` `:297`, `reference_files=None` → `["…/PLANNER_TEMPLATE.md"]`). Criterion 2 is a case-insensitive substring match of the entry's title against that file — so **doctrine text derived from a lesson can retroactively make that lesson look like a duplicate of doctrine.** Measured 2026-08-14: this entry's title occurs **0** times in the current PT and **0** times in the builder's post-edit output, so there is no collision today or after 4.89 — but the coupling is structural and every future plan in this lineage inherits it. **Ingest before the doctrine edit, always.** ⚠️ **The agent's obligation stops there** — the wider rule this implies (*a plan whose doctrine text quotes its own source lesson must re-measure criterion 2 rather than inherit a prior rehearsal's zero*) binds FUTURE plans, which this plan cannot enforce; stating it here would be enforcement-by-prose in a document no future author reads. It is **routed instead**: recorded in this cycle's walk register and carried in the baton for the next `LESSONS.md` sweep. ⚠️ It cannot be appended as a lesson now — **guard (a) freezes `LESSONS.md` while this fingerprint-pinned plan is deposited-but-un-run**, which is the guard working as designed rather than an obstacle. *(w1-3: an unstated coupling between the corpus mechanism and the artifact this arc edits. w2-3: its forward half re-homed out of this plan.)*

⚠️ **The `:297` cite above is a SOURCE line anchor, and this plan may sit held.** Re-verify at dispatch: `grep -nF "def detect_duplicates" /Users/marklehn/Developer/GitHub/lessons-forge/src/lessons_forge.py` — if the line moved, the anchor is reported as a finding and the surrounding claim re-read at the definition, never silently followed. *(w2-2: the walk-1 fold introduced a line-anchored source cite into a plan carrying no re-verify obligation.)*
8. **THE BACKUP GLOB POPULATION IS 14** (411: 13). ⚠️ **The `.db` suffix is load-bearing in every `find`: a bare prefix also matches `-wal`/`-shm` sidecars and returns ~3 per backup.** The count is not the guard; the id token `-<id>-` is.
9. **The candidate pool** of parsed-and-matched ids measured **287** (411: 281); `detect_duplicates` signature unchanged.
10. **`decisions/` state:** lessons-forge carries **ZERO** non-Done entries (re-measured). Other repos are out of scope — the single-writer probe globs `in-progress-*.md` in THIS project only.
11. **⚠️ A ONE-ENTRY BATCH WEAKENS TWO GUARDS, AND BOTH ARE RE-ARMED BELOW.** (a) ⚠️ **The weakening is NOT positional.** The draft claimed the one-heading fingerprint "can no longer detect a REORDERING, so G6's range arithmetic carries that weight" — **false on both halves: a 1-element sequence has no ordering to lose, and G6 is a membership test on `{345}` that never inspects order** *(scout S1-5)*. The real loss is the **`would_insert` BAND**: with six, any value in 1..5 proved a foreign writer at a glance; with one, `would_insert == 1` is not self-evidently ours. That is compensated by the FINGERPRINT, which pins content exactly and is checked before the mutation. (b) **G5's `ingested_count == 0` arm is more ambiguous here**: with a batch of 6, zero-vs-six is unmistakable; with a batch of 1, `0` is equally consistent with "already ingested" and "the entry was never appended." **The confirming arm at G5 is therefore MANDATORY, not advisory.** ⚠️ **The rule for that arm is stated ONCE, at G5, and this item deliberately does not restate it** — it names the PROBLEM (a batch of one makes `0` ambiguous), G5 owns the REMEDY. *(w7-1: this item previously carried its own version of the rule — `COUNT(*) WHERE id > 344 == 1` — which the cold scout's S1-4 fold had already replaced at G5 with an identity check, because a count admits any single foreign row. G5 even cited THIS item as its authority, so a reader following the pointer landed on the superseded rule. Found by an untargeted confirming pass, which is what §2.7 says confirming passes are for: record decay hides from aimed passes because attention follows what changed.)*

### ⚠️ NUMBERING
- **`lesson_entries.id` 345** — THIS batch's one (verified by executing the real cycle against a scratch copy: id 345 assigned).
- **`lesson_proposals.id` 353** — Plan B's one (NOT this plan's; verified against `P0` at Plan B's own authoring). **The rehearsal confirmed `MAX(lesson_proposals.id)` stays 352 through the ingest.**
- **Never write a bare numeral in 345–353 without its namespace.** Derivation, not a gate: every step keys on the parser diff and `source_heading`.

### ⚠️⚠️ The backup is the ONLY undo — the corpus has no delete path
*(w1-4, Destruction lens.)* `lesson_entries` has **no `status` column and no `DELETE` statement anywhere in `src/` or `scripts/`** — nothing in the application can remove a row. `ingest_lesson_entries` is an **upsert**, so a wrong row's *content* can be overwritten by a later ingest, but the row itself is permanent and its id is spent. **Therefore an erroneous ingest is not reversible through the application: restoring the Step-1a backup is the only remedy, and it discards anything else written since.** This is why 1a runs BEFORE any read that could tempt a shortcut, why its `PRAGMA integrity_check` must print `ok` rather than be assumed, and why the resume glob must find the EARLIEST matching backup — a later one may already contain the damage. Treat the backup as the plan's single point of recovery, not as ceremony.

### Residual risk register
- **Best verified:** every number above produced by running the real code read-only or against a scratch COPY — including a FULL `run_full_lessons_cycle` rehearsal that landed 1 entry with 0 duplicates, returned `needs_classification: [345]`, and left P0 unmoved at 352.
- **⚠️ The batch fingerprint is the content guard:** `ec35aac0063056bd4daea52c8a3fe6532779d230ff2192e204a54ed90029b042`.
- **Genuinely new since 411:** a GROWN Gate-2 queue (item 1), a fully-fallback batch (item 2), a double-quote hazard (item 3), and the one-entry guard weakening (item 11).
- **⚠️ A parallel terminal shares the ROOT repo.** Root HEAD at authoring `439c9e5`, `LESSONS.md` porcelain clean. A root-HEAD move is EXPECTED; G2's arm is conditional on the path diff, not on the hash.
- **⚠️ This plan is one link in a three-plan arc** (ingest → classify → Gate-1 routing) that gates a fourth (the PT 4.89 executable). A HALT here stalls the arc; it does not damage it.

**Scope discipline:** cycle run only. Routes stay `NULL`; **no `insert_proposal` anywhere.** Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals 98/121/130 (`stale`) or 340/342/346/350/352 (the live Gate-2 queue). **⚠️⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is fingerprint-pinned.

### ⚠️ Freeze checklist — the deposit-time obligations, because this plan carries SIX `<id>` tokens in TWO namespaces
*(w8-1. Origin-carried by OMISSION: neither 411 nor 397 carries this section — grandparent 389 does, and an omission leaves no token for a clone-diff to catch, which is why seven walks and a cold scout all passed over it.)*

⚠️⚠️ **`<id>` IS NOT ONE TOKEN IN THIS PLAN. A blanket find-and-replace at deposit CORRUPTS the receipt format.**
- **PLAN-id sites (4) — replace with this plan's actual id at deposit:** the Bootstrap line (`in-progress-executable-<id>.md`); the backup filename `BK=…-pre-cycle-<id>-$(date -u …)`; the Step-1a resume glob `-name 'lessons-forge-pre-cycle-<id>-*.db'`; and item 8's prose naming the `-<id>-` token as the real guard.
- **ENTRY-id site (1) — LEAVE IT:** the Self-report's `- ingested entry=<id>` is the RECEIPT FORMAT and its `<id>` is `lesson_entries.id` (**345**), written by the agent at runtime. Substituting the plan id here would make the receipt assert the wrong namespace — the same failure the NUMBERING section forbids for bare numerals, in placeholder form.

**Then, in order:** (1) **faithful-mirror `plan_lint`** at a deposit-shaped scratchpad path — **NEVER the real `decisions/`**, where the daemon claims and dispatches within one second — with the real referenced files copied in, expecting only the `(o1)` mirror-fidelity advisories and the `(q)` pin lines; (2) `id_sequence` read **AT deposit**, read-only — the authoring-time read is a prediction an in-window dispatch can consume; (3) the defensive claim-race commit sequence with its `restore --staged` fallback; (4) post-deposit `ls` of the deposited path. ⚠️ **The deposit basename does NOT change if this plan is held past today** — re-date nothing.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate re-assert the non-terminal set is **exactly `{340, 342, 346, 350, 352}`** — a changed set means in-window routing, and a changed COUNT alone is not the test.
- After QA, confirm `lessons-forge/knowledge/FORWARD.md` is still **18** rows against the Step-1a baseline (probe form `grep -c "^| "`).
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — additive single-write ingest (T-2 fires); structure-for-structure clone of shipped 411, so T-8 silent.
**Walk register:** `governance/knowledge/research/walk-register-cycle-ingest-residual-bucket-2026-08-14.md` (schema 0.3), committed per phase; any bundling DECLARED.
**Status:** cycle CLOSED 2026-08-14 on a fully DRY walk. ⚠️ **Walk count, fold count and per-finding detail are stated ONCE — in the walk register — and nowhere in this plan.**

**Closing:** the final walk read **DRY on all five lenses — instruction 0 / record 0**, with no restructuring fold, so §2's bar is met on a dry pass rather than a judged stop and there is **no residue to enumerate**. The dryness is evidenced, not asserted: eleven load-bearing numbers re-verified against live state (E0; P0; entry count == max id, i.e. no gaps; the NT id-set; STALE ids; the full eight-status distribution; the sentinel hash; parsed count; would_insert; candidate pool; the batch fingerprint), `fold_check` CLEAN at 10 signals, and every `(item N)` authority citation re-read against its target. Fold-and-deposit exactly once. *(w5-1, site 1 of 3: this line still read "walks 1 and 2 COMPLETE" after walks 3 and 4 had run — the seventh record-lag of the session.)*
**Walk 0 (context pin):** the FALSE-HERE table above IS the pin, and every value in it was measured at authoring, not inherited. Clone-diff vs 411 returned **11** re-derivations, two of them run-halting.
**Walks:** recorded in the walk register `governance/knowledge/research/walk-register-cycle-ingest-residual-bucket-2026-08-14.md`, which is the single site for walk count, fold count, finding ids, classes and dispositions. ⚠️ **This line names no count and enumerates no walk, deliberately.** *(w6-1: the walk-4 collapse removed the DETAIL but kept an ENUMERATION — `1 · 2 · scout · 3 · 4` — which went stale the moment walk 5 ran, the eighth record-lag of the session. An enumeration is a derived value restated outside its source and stales exactly like a restatement; removing detail while keeping the list was a fix to the symptom.)*

**Per-lens lines** *(required by §3 and by `plan_lint`, which checks for the five lens NAMES; kept compact deliberately — the draft's version restated seventeen finding ids and would have gone stale on every subsequent walk. Findings, ids, classes and dispositions live ONLY in the walk register.)*
- **Weak spots:** findings at multiple walks and from the cold scout; the last pass dry. Its late yield was superseded cross-references — sites still asserting what a later fold had refuted.
- **Destruction:** findings early and from the cold scout; dry thereafter. Yield: the backup is the only undo, and a count-guard where the plan demands an identity guard.
- **Vulnerabilities:** dry at every walk, and the dryness MEASURED rather than assumed — the fenced exact-string survives `strip_fenced_code_blocks` (2 before, 2 after), and the pre-mutation duplicate check was proved un-runnable by execution rather than by reading.
- **Integration-record:** the cycle's highest-yield lens, and every one of its findings an instance of a single class — a record site restating what another site already stated.
- **ACID:** dry at every walk; the plan/register contradictions it would otherwise have caught were reached by Integration-record first.

⚠️ **These lines name no walk numbers and no counts, deliberately** — the version written at the scout fold enumerated walks 1–5, went stale as walks 6–10 ran, and was caught by the closing-record re-read. Per-walk detail lives in the register.

**Conformance (§5):** `plan_lint` run at a FAITHFUL deposit-shaped scratchpad mirror — never the real `decisions/`. Expected set at the close: the `(o1)` advisories for mirror-fidelity paths only. *(scout S1-9: no exit code or phase was recorded; the close run's measured set is what freeze binds to.)*

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Lessons Agent (ingest the 1; NO classification anywhere in this plan)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you run in a worktree** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.**
>
> **⚠️ EXECUTION ORDER — exactly: Step 0 → 1a → 1a-ter → 1a-bis → G2 → G1 → 1b (the only mutation) → G3–G7 → the ONE deposit.** ⚠️ **NO CLASSIFICATION.** `get_unclassified_entries()` returning the single-id work list `[345]` is this plan's CORRECT closing state.
>
> **Step 0 — dispatch state.** Three-place probe on `knowledge/development/dev-log-residual-bucket-step-1-2026-08-14.md` (committed HEAD; working tree; `git log --all` + `branch --list 'bellows-preserved/*'`), each with its exit code captured; probe 3's exit carries NO signal — pair it with a positive control against `knowledge/FORWARD.md` before reading silence as no-hit. Any hit → RESUME. All absent → FRESH. State the determination first.
>
> **Single-writer check:** `get_unclassified_entries` stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY**; this plan's own file present is normal, ZERO matches means the probe is broken, any OTHER match → HALT.
>
> **⚠️ HALT DURABILITY:** on any HALT commit existing deposit files by explicit pathspec and record the gate, its measured value, and whether the ingest committed. **Authorized writes: the `.backup`, `run_full_lessons_cycle`, this step's deposit.**
>
> **Scope:**
> - `knowledge/development/dev-log-residual-bucket-step-1-2026-08-14.md`
>
> ### Step 1a — restore point, then baseline
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<id>-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> `<id>` = this plan's ACTUAL id. VERIFY, **in exactly this form**: `sqlite3 -readonly "file:$BK?immutable=1" 'PRAGMA integrity_check;'` → `ok`. ⚠️ **The `file:` URI prefix and `?immutable=1` are BOTH load-bearing — `.backup` writes a WAL-header DB with no `-shm`, and a plain `sqlite3 -readonly "$BK"` fails with `unable to open database file (14)`.** Backup counts == live (fresh: **344 entries / 352 proposals**). Resume glob: `find … -name 'lessons-forge-pre-cycle-<id>-*.db'` — **`.db`-scoped; a bare prefix matches sidecars and returns ~3 per backup, firing a spurious HALT** — EARLIEST match, prove pristine by `MAX(id)` = 344/352.
>
> **Baseline capture (read-only, raw):** (1) the zero-emitting distribution over ALL EIGHT statuses (expected: implemented 281 · superseded 28 · reference 20 · rejected 15 · **accepted 5** · stale 3 · proposed 0 · ambiguous 0); (2) proposals by category; (3) total `lesson_entries` (**344**); (4) sentinel entry 344 hash == `e7b607bd…` (mismatch = HALT, not correction); (5) `STALE_COUNT=3`; (5b) `SURFACEABLE_BASE=0` ⚠️ **labelled distinctly from NT, which is 5**; (6) `E0` == 344, `P0` == 352; (7) **NT capture BY ID, not by count:** `SELECT 'NT='||GROUP_CONCAT(id) FROM (SELECT id FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous') ORDER BY id);` → printed token required; silence = broken invocation → HALT; (8) FORWARD baseline `grep -c "^| "`, recorded raw (**18** at authoring). **Capture only — G1 owns the verdict.**
>
> ### Step 1a-ter — commit the before-anchor BEFORE the ingest
> Write + `git commit` the stub `knowledge/development/dev-log-residual-bucket-step-1-2026-08-14.md`: `Status: Partial — in flight (pre-ingest stub)`; the absolute backup path; E0/P0; **the NT id-list line**; STALE; SURFACEABLE; the FORWARD baseline; the full distribution; the sentinel hash; **the three doctrine pins, raw, HALT unless all three print.** The final Receipt rewrites this file but carries any first-dispatch ingest dict forward verbatim.
>
> ### Step 1a-bis — pre-ingest guard (read-only)
> 1. `parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")`; tally the whole-corpus dry run by `source_heading` lookup. **FRESH → assert `would_insert == 1` AND `would_update == 0`** (Planner measured 1 / 0 / 287 over 288 parsed). **RESUME → `would_update == 0` and `would_insert ∈ {0, 1}`.** ⚠️ **With a batch of one there is no intermediate value to catch a foreign writer** — so a `would_insert` of 1 on a RESUME is NOT self-evidently ours: confirm it against the fingerprint below before proceeding.
> 1b. **THE BATCH FINGERPRINT:** sha256 of `"\n".join(<would-insert headings in parse order>)` == **`ec35aac0063056bd4daea52c8a3fe6532779d230ff2192e204a54ed90029b042`** (the single heading starts `2026-08-14: A residual` and contains a DOUBLE-QUOTED phrase — see item 3). Mismatch → HALT. **RESUME with `would_insert == 0` → SKIP, record `FINGERPRINT SKIPPED (post-ingest resume)`.**
> 2. **Sentinel:** parsed entry matching entry 344's heading — **measure the match count and PRINT it**; exactly 1 match with hash equal → PASS; else HALT.
> 3. **Duplicate pre-check.** (a) pre-existing ids — mirror the ingest's candidate construction (parsed-and-matched, ~**287**; PRINT the list length first, HALT if 0 or wildly off); `detect_duplicates(conn, <ids>)` read-only → non-empty = HALT. (b) the 1 parsed batch entry: criterion 1 **INERT — verified here on live data, not inherited** (`detect_duplicates`' default reference file is `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`, which carries **0** `**Tag:**`/`**Tags:**` lines, AND this entry's `tags` column is **NULL** — the criterion is doubly unfalsifiable, by both operands); criterion 2 the `_EM_DASH_SEP` title-substring — ⚠️⚠️ **the heading carries NO separator, so the WHOLE-HEADING FALLBACK is the ONLY path this batch takes. Unlike 411, there is no separator-matched entry beside it to act as an in-batch control.**
>
> ⚠️⚠️ **DO NOT CALL `detect_duplicates` FOR THE BATCH ENTRY — IT CANNOT ANSWER, AND IT ANSWERS ANYWAY.** It reads each id out of `lesson_entries` and hits `if row is None: continue` (`lessons-forge/src/lessons_forge.py` `:363–369`) for an entry that has not been ingested yet, returning `[]` — a confident false zero on the one pre-mutation check this plan calls a HALT condition. **Executed live against the read-only corpus 2026-08-14: `detect_duplicates(conn,[345]) = []` while `COUNT(*) WHERE id=345` was `0`.** *(scout S1-6; origin-carried from 411, where the same prose named no runnable mechanism.)*
>
> **Do this instead — mirror criterion 2 by hand, which DOES run pre-mutation:** read the reference file `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` ONCE into memory, lowercase it, and count occurrences of **the exact string the code uses**, lowercased. ⚠️ **That string is `source_heading.strip()` IN FULL** (`:375–378` — the `else` branch when `_EM_DASH_SEP` is absent), i.e. **including the leading date AND the trailing `[tag: …]`**, not the descriptive title alone:
> ```
> 2026-08-14: A residual "everything else" bucket silently absorbs the class that deserved its own bin [tag: governance-design]
> ```
> **Planner-measured 2026-08-14 with THAT exact string: `0`.** *(w3-1: the walk-2 fold mandated this probe but measured the title-only form — a different string. The answer survives because the title is a strict substring of the whole heading, so a zero on the subset guarantees a zero on the superset; the containment is stated because the conclusion rests on it, not on the two probes being equivalent.)* Non-zero → HALT: doctrine already contains this lesson's title and the entry would be flagged a duplicate the moment it is ingested. **POSITIVE CONTROL from that same single read — PINNED, not described:** the lowered text must have non-zero length AND must contain the literal **`orchestration plan rules`** (Planner-measured: **5** occurrences). Zero length or zero occurrences of that literal → the read failed and **every zero above is void** → HALT. *(scout S1-7: the draft had de-pinned 411's named literal to "a LOWERCASE sentinel substring" — a control that names no literal cannot fail.)*
>
> Then report what the post-mutation dict returns for `duplicates_marked_count`; the Planner's rehearsal of the REAL cycle against a scratch copy measured **0**, so 0 is expected ON EVIDENCE — a hit is a finding, not a contradiction, and HALTs.
> 4. Record actuals — measured numbers, never a pre-composed "empty" string.
>
> ### Gates run pre-mutation
> - **G2 — provenance:** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (didn't run); non-empty output → HALT (never ingest an uncommitted corpus). Record `rev-parse --short HEAD` (authoring: `439c9e5`; **a mismatch is EXPECTED — a parallel terminal shares this repo**: run `git diff --stat 439c9e5..HEAD -- LESSONS.md` — empty → reconcile-note and PROCEED; non-empty → HALT, the fingerprint premise fell). Confirm the stub carries the three pins.
> - **⚠️⚠️ G1 — the non-terminal precondition, RE-KEYED TO THE MEASURED FIVE (this is the arm 411's form would have failed):** capture the NT id-list and `STALE_COUNT`. Arms in order, first match wins: (1) **NT is EXACTLY `340,342,346,350,352` AND `STALE_COUNT == 3`** → PASS (the live Gate-2 queue; on a step-0 RESUME record `PASS (resume, pre-mutation)`). (2) **NT contains ANY id outside that set** → HALT naming every id, status and route — that is in-window foreign routing. (3) **NT is MISSING any of the five** → HALT: a queue row was consumed under this plan. (4) **`STALE_COUNT != 3`** → HALT. ⚠️ **A count-only check is NOT sufficient, and this cycle is the proof: the count moved 3 → 5 between two plans on the same day.**
>
> ### Step 1b — the ingest (ONCE)
> Open canonical read-WRITE. **`run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()`. **IMMEDIATELY append the verbatim returned dict to the stub and commit it again.** Print all seven keys. ⚠️ Re-verify the function against live source before running (authoring source-read + a full rehearsal: parses → ingests → builds candidates → `detect_duplicates` → inserts a `duplicate` proposal per hit → returns `get_unclassified_entries`; it does NOT classify) — changed behaviour → HALT.
>
> ### Post-mutation gates (report EVERY gate as a table row; run all before halting)
> - **G3 — `duplicates_marked_count == 0`**; scoped resume form `SELECT COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 344`. A zero is valid ONLY against 1a-bis's positive control.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty.**
> - **G5 — work exists:** `ingested_count == 1` → PASS. **`== 0` → the IDENTITY-confirm arm is MANDATORY** (item 11b). ⚠️ **It is an IDENTITY check, not a count** — this plan says four times that a count is not the guard, and the draft's own compensation was `COUNT(*) == 1`, which any single foreign row satisfies while the `would_insert == 0` resume path has already skipped the fingerprint, leaving no heading-level check anywhere in Step 1 *(scout S1-4)*. The arm: `SELECT source_heading FROM lesson_entries WHERE id > 344` must return **exactly one row whose heading recomputes to the batch fingerprint `ec35aac0…`** (sha256 of the heading; the QA row-6 mechanism, run here) AND a Complete receipt must exist — only then is this an idempotent re-dispatch, recorded and stopped; `== 0` with a stub or absent receipt → deposit-completion resume from the stub; `== 0` with no entry in the DB → **HALT, the entry was never appended.** **∉ {0, 1} → HALT.**
> - **G6 — work-list reconciliation:** every id in `needs_classification` is `> 344` and `≤ 345` (range computed from confirmed E0). ⚠️ **This is a MEMBERSHIP check, not a positional one** — it asserts every returned id lies in `{345}` and inspects no ordering. *(w9-1: G6 previously claimed to carry "the positional weight the one-heading fingerprint cannot" and cited item 11a as its authority — but the cold scout's S1-5 fold had already established at item 11a that the claim is false on both halves: a 1-element sequence has no ordering to lose, and this gate never inspects order. The corrected site was being cited BY the uncorrected one — structurally identical to w7-1, and the FOURTH unswept fold of this cycle.)* Outside-range → HALT + the `### Deferred entries (G6 candidate)` section AND the arithmetic 1-line anchor.
> - **G7 — the queue is untouched:** the non-terminal set is STILL exactly `340,342,346,350,352` after the ingest, and `MAX(lesson_proposals.id)` is still **352** (the rehearsal confirmed the ingest creates no proposal). Any change → HALT.
>
> **Self-report:** `SELECT id, source_heading FROM lesson_entries WHERE id > 344 ORDER BY id` → **1 row (345)**, recorded as an `- ingested entry=<id>` line, **heading bound as a query parameter — it contains double quotes (item 3)**; `get_unclassified_entries()` == exactly `[345]`. **Receipt status from the CLOSED SET**, carrying: the dict verbatim; the G1–G7 table; the baseline distribution + sentinel + STALE + SURFACEABLE + the NT id-list + FORWARD; E0/P0; the 1-line anchor; the backup path labelled `pristine (pre-cycle)`; `#### Files Created or Modified` split committed/untracked; `#### Doctrine pins` verbatim from the stub. RAW output throughout; canonical Python file-write; explicit-pathspec commit with post-commit `git show --name-only --format= HEAD` + `git rev-parse --show-toplevel`. `#### Prompt Feedback` in `### Ledger Updates`. `#### Forward Register`: `NONE`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-residual-bucket-step-1-2026-08-14.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for verdict.**

## STEP 2 — QA

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (allowlist: `Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`), with the single G6-deferral exception.
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB **read-only** (`?mode=ro`, absolute path). **Verification + reporting only; a failing check is reported, never fixed. No Monitor. No classification.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-ingest-residual-bucket-2026-08-14`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-ingest-residual-bucket-qa-2026-08-14.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/`; `required_evidence_files` `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]`. All four files AND the report with its table written BEFORE the block; APPEND the stdout; banner `Rule 20 — QA Self-Check Results` + `PASSED — SELF-CHECK PASSED` verbatim; end with the self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` immediately after the table.
>
> **Scope:**
> - `knowledge/qa/cycle-ingest-residual-bucket-qa-2026-08-14.md`
> - `knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/invariants.txt`
> - `knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/schema.txt`
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows before halting:
> 0. **Deliverables (Rule 17)** — per path `git log --oneline -1 -- <path>` (empty = ❌) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"`.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` ONLY. **Baseline MEASURED at authoring 2026-08-14 by THIS ROW'S OWN MANDATED COMMAND — `python3 -m pytest src/ -v` from the lessons-forge root — `55 passed`.** *(w2-1: the walk-1 fold measured it with `-q` while this row mandates `-v`; both return 55, but a baseline declared by a method other than the mandated one is the numbers-by-mandated-method-only violation, and re-measuring cost one command.)* ⚠️ This is a reference point, not a gate: a delta is **reported with both numbers**, never asserted away and never treated as a failure by itself. *(w1-1: the draft removed a predicted number and removed the reference along with it, leaving QA asked for a delta against nothing.)*
> 2. ⚠️⚠️ **`get_unclassified_entries(conn)` returns EXACTLY `[345]` — NOT `[]`.** An empty work list means something CLASSIFIED the batch. `[]` → ❌ Critical.
> 3. **The 1 landed, only it** — `SELECT id, source_heading FROM lesson_entries WHERE id = 345` → 1 row, heading equal to the anchor **bound as a query parameter (it contains DOUBLE QUOTES — never interpolate it into a `sqlite3` CLI string, where `"` is identifier quoting)**; reconcile `COUNT(*)` derivation `344 + 1 = 345`. → `invariants.txt`
> 4. **Plan-204 held, NO proposal created** — stale still 3; entry-344 hash `e7b607bd…` unchanged; dict's `updated_count`/`terminal_proposals_flagged` from the Receipt; ⚠️⚠️ **`SELECT COUNT(*) FROM lesson_proposals` == 352 UNCHANGED**; the FULL zero-emitting 8-status distribution before/after, every bucket unchanged; **the non-terminal set still EXACTLY `340,342,346,350,352` by id** (a count is not the guard — the id set is). → `hash-trap.txt`
> 5. **No schema drift** — PRAGMA table_info + constraints vs `src/db.py` DDL; raw `.schema` both tables → `schema.txt`.
> 6. **Fingerprint provenance** — recompute the batch fingerprint over the anchor heading read FROM THE DB: == `ec35aac0…`; and `LESSONS.md` porcelain still clean at root.
> 7. **Register posture** — lessons-forge `decisions/` non-Done contents: this plan's own `in-progress-*` file ONLY (other repos out of scope); `knowledge/FORWARD.md` delta against Step 1's captured baseline is **ZERO** by the same probe form (any new row is a finding: a `NONE.`-item row = a regression of plan 376's guard, a real-text row = foreign writer).
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-ingest-residual-bucket-qa-2026-08-14.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/hash-trap.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-residual-bucket-2026-08-14/schema.txt`
