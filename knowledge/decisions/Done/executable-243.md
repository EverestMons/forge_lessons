# Lessons Forge — Cycle Run 2026-07-20 (ingest + classify the 07-19/07-20 batch)
**Date:** 2026-07-20 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** both | **Execution:** Step 1 (Lessons Agent) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

**This is the first of a three-plan arc that ends in PLANNER_TEMPLATE v4.75 → v4.76.** This plan runs the cycle only: ingest the un-ingested LESSONS.md entries and classify them into proposals. Gate 1 (route disposition) and Gate 2 (codification) are separate plans with CEO decisions between. Precedent: 205 → 206 → 208.

**Three amendments are owed at Gate 2** and are the reason this arc is running now — LESSONS entries covering (a) the ACID lens as a fifth Drafting Cycle pass, (b) the full cycle applying to DIAGNOSTICS, (c) a lens is not done at one pass — iterate until dry, and the last event before deposit must be a dry pass. **All three amend the SAME template section** (`## The Drafting Cycle`, PLANNER_TEMPLATE.md:314, with `### The Full Cycle` at :328). They are a cluster, not three scattered edits — say so in the Step 1 synthesis so Gate 1 can route them coherently.

**Two further entries are also un-ingested and come along** — the 07-19 "an instruction that is not a numbered row, a named test, or a gate evaporates" lesson and the 07-19 "grep presence is not effect" lesson. They are in scope for classification. This cycle is not scoped to the three amendments; the ingest is batch by nature.

**⚠️ The `updated_count` watch — this is the plan-204 hash trap's live test.** Appending the 07-19/07-20 entries gave the previously-last entry a trailing `---`, which is the exact trigger that used to flip a `content_hash` over whitespace and silently demote an `implemented` proposal. Plan 204 normalized the hash input and added the `_TERMINAL_STATUSES` guard, and the fix was production-proven at the 2026-07-16 wrap. **Expectation: `updated_count == 0` and no terminal proposal flagged. Verify and report the ACTUAL values; do not force the number.** A non-zero `updated_count` or a non-empty `terminal_proposals_flagged` is not a silent failure any more — 204's guard flags rather than demotes — but it is a loud finding: **halt and report it**, because it would mean the normalization regressed.

**⚠️ The plan-154 dedup advisory is RETIRED — do NOT expect advisory lines.** Plan 207 removed `detect_recently_implemented_overlaps`, its helper, both call sites, the rendering, and 7 tests. Verified absent from `src/` at authoring time. **Any `Recently-implemented overlap:` line in the generated report is a regression, not noise — halt and flag.** This is the opposite of the standing instruction in plan 205; that instruction is void here.

**Scope discipline:** cycle run only. Routes stay `NULL` at insert — the CEO assigns at Gate 1 via `set_proposal_route()`. **Do NOT edit PLANNER_TEMPLATE.md.** Codification is Gate 2 and is the one thing the record explicitly forbids doing outside the governed route. Do not pre-draft template wording in any deposit; a classification is not a codification.

**Deposit-once discipline:** deposited exactly once. If a second copy appears, that is a claim-dedup bug — do not double-claim.

**Authoring self-check (for the verdict gate).** `plan_lint.py` was run against this plan at authoring time: **exit 0**, checks (a)–(d) all PASS (uppercase `## STEP` headings, multi-line `**Deposits:**`, QA Rule-20 banner pair present, scope named per step). It emits **two WARNs** — "step 1 mentions tests but declares no test scope" and "step 3 mentions tests…". **Both are the known-benign `scope_check`-on-tests false-positive class** (see the `benign-gate-failure-classes` record): Step 1's "named test" is a quote from the lesson entry it classifies, and Step 3 is **verification-only** — QA runs the suite but modifies no `test_*.py`, so naming a test file in its scope would be *wrong*. **Do NOT add test files to any step's scope to silence these WARNs.** Exit 0 is the pass; the WARNs are expected.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-lessons-forge-cycle-2026-07-20.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — Lessons Agent

---

> **FIRST — before any reads or work: post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read your specialist file at `agents/FORGE_LESSONS_AGENT.md` first (ADR-002 six-value taxonomy). **⚠️ Its file paths are STALE — trust THIS plan's paths over the specialist's.** The specialist says `forge/src/lessons_forge.py` and `forge.db`; the real module is `lessons-forge/src/lessons_forge.py` and the corpus is `lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database (the forge prompt-workshop) — never open or write it.** Every canonical-DB path in this plan is absolute and authoritative; the specialist's classification GUIDANCE (taxonomy, confidence rules, target-field assignment) is authoritative, its PATHS are not.
>
> **Single-writer assumption.** This plan writes to the one canonical DB and is the only thing that should. Before Step 1a, confirm no daemon or other session is mid-cycle: `get_unclassified_entries` should be stable across two reads a moment apart, and no `in-progress-*lessons*` plan should exist in `knowledge/decisions/`. If either check suggests a concurrent writer, HALT — a second cycle running against the same corpus is exactly how a proposal gets staled out from under you.
>
> **Working location — read carefully, this is the plan-225 trap.** Run commands from **your own working tree** and write every file there. **The ONLY exception is canonical-DB access, which uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — the worktree has no DB copy and that is never a reason to substitute. Do NOT `cd` to the main tree to run the cycle: `generate_lessons_report` and the deposit writes all resolve RELATIVE paths, so a main-tree cwd puts output in main while you commit in the worktree, which is exactly the untracked-file collision that tore down plan 225's Step 3.
>
> **Scope:**
> - `knowledge/development/classifications-summary-2026-07-20.md`
> - `knowledge/development/dev-log-cycle-step-1-2026-07-20.md`
>
> **The expected batch is the five un-ingested LESSONS.md entries** — the four dated 2026-07-19 and the one dated 2026-07-20. **Parser-verified at authoring time** (`parse_lessons_md` on the live file vs the canonical DB): the current file has 94 entries, exactly **5** have headings not yet in the DB (these five, all three Drafting-Cycle amendments among them), and `get_unclassified_entries()` returns **`[]`** — so post-ingest the work list is exactly these 5.
>
> **⚠️ The corpus row count is 146, NOT 94 — do not read that as corruption.** `lesson_entries` holds **146** rows while the file has 94 entries: the other **57** are orphan rows from headings that were reworded over the project's history (a heading change inserts a new row and leaves the old one). All 146 are classified (that is why `get_unclassified_entries()` is `[]`). **After this cycle expect 151 rows (146 + 5), not ~99.** A reader who assumes "94 + 5" will see 151 and cry corruption — it is expected.
>
> **Confirm all of this against what the ingest actually returns; if `ingested_count` is not 5, or the work list is not exactly these five headings, halt and explain the delta rather than adjusting to match this text.**
>
> **Step 1a — take a restore point, then capture the pre-cycle baseline. Before touching anything.**
>
> **Back up the canonical DB first — with `.backup`, NOT `cp`.** The canonical DB has a live WAL (`lessons-forge.db-wal` exists at authoring time), so a filesystem copy of the `.db` file alone would silently miss any un-checkpointed pages and produce a subtly stale restore point. Use SQLite's own backup, which checkpoints correctly.
> **⚠️ Write the backup to the MAIN tree, by ABSOLUTE path — a worktree-local backup is destroyed by teardown, which is when you would need it.** This plan runs worktree-isolated (lessons-forge cycles do — plan 225), so a relative `data/backups/` resolves inside your worktree and vanishes at teardown along with the restore point. Target the main tree explicitly and `mkdir -p` that same absolute directory (not a relative one): `mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups && sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-<UTC timestamp>.db'"` (colon-free stamp). The `.gitignore` matches `*.db` (verified), so it will not be committed — confirm with `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain` showing the backup absent. **State the absolute backup path in your dev log.** This is the CEO's restore point if a committed cycle later needs unwinding — belt-and-suspenders, since G1 (below) makes the ingest provably non-destructive. Every precedented corpus/DB write in this shop took one (the sentinel repair, the floor-only migration); this is not a new ceremony.
>
> **Then capture the baseline.** Read from canonical and record verbatim in your dev log: proposals grouped by `status`, proposals grouped by `category`, total `lesson_entries` count, and the id + `content_hash` of **the entry that is currently last in LESSONS.md** (identify it by file position, then look it up — do not just take `MAX(id)` and assume the two agree). That entry is the hash-trap's target: appending this batch gave it a trailing `---` separator, which is the exact trigger. **Verified at authoring time:** LESSONS.md uses `^---$` between entries (95 of them, the last immediately above the 07-20 heading), so the trigger condition genuinely occurred. Step 3 verifies the 204 watch against these figures and cannot do so if you skip this. Capture BEFORE the ingest — after is worthless.
>
> **⚠️ PRECONDITION (G1) — the fresh-run safety.** The ingest's update path stales **non-terminal** proposals when an entry's hash changes; plan 204's `_TERMINAL_STATUSES` guard protects only `implemented`/`rejected`/`superseded`/`reference`. So `proposed`, `accepted`, and `ambiguous` proposals are destructible when their entry is updated. **Measured at authoring time: ZERO of those three statuses in the corpus** — which on a fresh run makes the ingest provably non-destructive. **Confirm from your own baseline. On a FRESH run (nothing yet ingested this cycle), any `proposed`/`accepted`/`ambiguous` proposal voids the safety argument — HALT before the ingest.** The one exception is a **resume** (a prior dispatch already ingested and was interrupted mid-classification): there, `proposed` proposals from that partial run are expected and G1 is satisfied post-ingest by `updated_count == 0` — see G1 for the full disambiguation. Do not proceed on the strength of this plan's measurement; the number is from authoring time, and the corpus is the thing that may have changed.
>
> **Step 1b — run the ingest.** Open canonical **read-WRITE** for the cycle — a plain `sqlite3.connect("/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db")` (default is read-write). **Do NOT reuse a `?mode=ro` handle here** — those are only for the Step 1a baseline snapshot and the `.backup`; the ingest INSERTs, and a read-only connection makes it fail. Then call `run_full_lessons_cycle(conn)` (it defaults to reading `/Users/marklehn/Developer/GitHub/LESSONS.md` — confirm that is the path it read, do not assume). **`conn.commit()` after it returns**, before classifying — the same commit-after-cycle pattern proven safe on plans 205/226/228. The safety does NOT rest on transaction gymnastics: **G1 (below) guarantees the ingest cannot destroy anything.** The `ingest_lesson_entries` staling `UPDATE` only touches `proposed`/`accepted`/`ambiguous` proposals (verified: `WHERE status != 'stale' AND status NOT IN (terminal)`), and G1 halts *before* the ingest runs if any such proposal exists — so the staling matches zero rows and a committed ingest is non-destructive by construction. (This is why no rollback/deferred-commit machinery is needed; an earlier draft built it, then this pass verified G1 already excludes the case it defended.)
>
> **⚠️ "Commit" means `conn.commit()` — the SQLite transaction — NOT a git commit.** `run_full_lessons_cycle` does not commit internally (verified: "caller is responsible for committing"), and the DB is gitignored (`*.db`), so there is nothing to `git commit` and no `.md` deposit exists yet. Skip `conn.commit()` and a step death LOSES the ingest — the opposite of the plan-203 resume rationale, which relies on the ingest being durable so a re-dispatch resumes via G5. (The git commit of the `.md` deposits comes later, after classification.)
>
> **⚠️ Understand what you are running: this is a WHOLE-CORPUS operation, not a tail append.** `run_full_lessons_cycle` parses **all** of LESSONS.md and re-hashes **every** entry, then upserts. The five new entries are merely the expected delta. Any edit anywhere in that file since the last cycle — a typo fix, a reflow, a separator shift — lands in this same write and shows up as `updated_count`. That is why G4 below is a real integrity watch, not a formality — it catches an unexpected change to the corpus even though G1 already guarantees no destruction.
>
> **Record and report the ACTUAL returned values** for `ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `terminal_proposals_flagged`, and `needs_classification`. Do not paraphrase them into a narrative — print the dict.
>
> ## Step 1 gates — G1 through G6
>
> **These are GATES, not advice.** Report **every** gate as a row in a table in your dev log, each with its measured value and `PASS` or `HALT` — including the ones that pass. A gate you do not report is a gate you did not run. This plan states them as numbered gates deliberately: **one of the entries you are about to classify is the lesson that an instruction which is not a numbered row, a named test, or a gate is an instruction that evaporates.** Do not let this plan prove its own batch's point.
>
> **Gate timing:** G2 is **pre-ingest** (Step 1a). G1 is pre-ingest **on a fresh run** — a clean baseline lets the ingest proceed safely; but if the baseline is non-empty G1 defers its verdict until after the (no-op) ingest so it can distinguish a fresh-run violation from an expected resume (see G1). G3–G6 read the Step 1b return dict on the already-committed result and are HALT-and-report watches: they surface an unexpected outcome for the CEO, not a rollback.
>
> **G1 — non-terminal proposals precondition (FRESH-run gate; exempt on resume).** G1's real guarantee is that the ingest stales no live proposal — which holds when no *updated* entry has a non-terminal proposal. On a **fresh** run: the Step 1a baseline must show zero `proposed`/`accepted`/`ambiguous` proposals; any such proposal → **HALT before the ingest**. **On a RESUME, G1 is satisfied by construction, NOT violated.** A resume (G5 `PASS (resume)`) means the batch is already ingested and this run's ingest updates nothing — G4's `updated_count == 0` proves the ingest staled nothing — so the `proposed` proposals left by the interrupted classification are EXPECTED and do not trip G1. Concretely: if the Step 1a baseline shows non-terminal proposals, do not halt immediately — run the (no-op) ingest and check G5/G4 first; halt on G1 only if this is a fresh run (`ingested_count == 5`) with unexpected pre-existing non-terminal proposals. Without this exemption G1 would block every resume, which is the state the G5/G6-deferral paths explicitly rely on.
>
> **G2 — LESSONS.md provenance.** Before the ingest, confirm the source file is committed and pin what you read: `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md` must be **empty**, and record `git -C /Users/marklehn/Developer/GitHub rev-parse HEAD`. **Use `git -C <absolute root>` — do NOT rely on cwd.** `lessons-forge` is a submodule and LESSONS.md does not exist inside it; a bare `git status -- LESSONS.md` from your worktree reports clean because the file is *absent*, which is a vacuous pass, not a verification. (This exact mistake was made once while authoring this plan — that is why the gate is worded this way.) A dirty LESSONS.md means the corpus would record content that exists in no commit → **HALT**. Expected at authoring time: clean, root HEAD `5bad9ee`; report the actual.
>
> **G3 — `duplicates_marked_count` is zero.** This is the silent-drop guard. `run_full_lessons_cycle` inserts duplicate proposals at `status='proposed'` and only THEN computes `needs_classification` via `get_unclassified_entries`, which excludes any entry holding a non-stale proposal — so a duplicate-marked entry **disappears from the work list with no error**. Measured at authoring time against the live detector: the tag criterion is a no-op (PLANNER_TEMPLATE.md has no `**Tag:**` lines) and all five headings are clean on substring, so the expected value is 0. Non-zero → **HALT** and name exactly which entry IDs were marked and why — a dropped amendment entry would silently defeat this whole arc.
>
> **G4 — `updated_count` is zero and `terminal_proposals_flagged` is empty.** A pure-append cycle expects both. Non-zero either way → **HALT** and diagnose — do NOT prejudge it as a regression. Report **which entry IDs updated** and show each diff, classifying it as one of: **(a) whitespace-only** — the plan-204 hash-trap has regressed (a trailing-`---` flip should be normalized away); or **(b) substantive** — someone edited an existing entry's body, which is a *legitimate* re-ingest, not a bug, but is unexpected for this cycle and the CEO must confirm it was intended before the run continues. Either way HALT with the evidence; the distinction decides whether the finding is a code regression or a content change. A bare count forces a re-dispatch to learn which.
>
> **G5 — there is work to do.** `ingested_count == 0` **AND** `needs_classification` empty → *probably* nothing to do — but **before halting, disambiguate two states that look identical here.** (a) **Truly nothing to do:** no proposals exist for this cycle's five batch entry IDs → **HALT** and report. (b) **Classification done, deposits not landed:** proposals for the five batch entries DO exist (a prior run classified and `conn.commit()`ed them, then died before or during the deposit git-commit) AND the Step 1 deposits (`classifications-summary-2026-07-20.md`) are absent from the tree → this is a **deposit-completion resume**: do NOT re-classify (that would duplicate — though `get_unclassified` would prevent it, the intent is wrong) and do NOT halt as nothing-to-do; **re-generate the Step 1 deposits from the committed DB state and commit them**, then STOP for verdict. **If `ingested_count` is 0 but `needs_classification` is NON-empty, that is a legitimate resume** (a prior run committed the ingest and stopped before classifying — the plan-203/205 state): record it as `PASS (resume)` and proceed; do not halt. **A `PASS (resume)` here is also what clears G1's deferred verdict** (non-terminal proposals from the interrupted classification are expected on a resume — see G1).
>
> **G6 — work-list reconciliation.** The derived work list matches the entries the ingest just inserted; any divergence is reconciled per the DB-wide note below. `needs_classification` unexpectedly larger than the batch → **HALT** (an older entry surfacing means a prior proposal went `stale` — the plan-204 signature). **On that HALT the CEO chooses one of: (i) classify the batch AND the extra entry this cycle; (ii) classify the batch only and DEFER the extra entry to a later cycle; (iii) investigate the stale first, classify nothing.** If the CEO chooses (ii), record the deferred entry ID(s) explicitly in the Step 1 deposit under a heading `### Deferred entries (CEO-approved)` — Step 3 reads exactly that list and will otherwise treat any residual unclassified entry as a failure. This is the ONLY way an entry legitimately remains unclassified at Step 3. **Re-entry mechanics:** because Step 1 STOPs at this HALT, the CEO decision arrives on a re-dispatch; the ingest is already committed, so the resumed Step 1 hits G5's `PASS (resume)` path, classifies only the batch, and writes the deferred-entries heading — it does not re-ingest.
>
> **After the gate table: if every gate reads PASS (or `PASS (resume)` on G5), continue to classification. Any HALT — stop and report; the ingest stays committed (G1 made it safe) and the CEO decides.**
>
> **Derive the work list yourself** from `needs_classification` (Orchestration Rule #47 — never a hand-copied list). Do NOT hand-type entry IDs from this plan; this plan deliberately names none.
>
> **⚠️ `needs_classification` is DB-WIDE, not scoped to what this cycle ingested** — its docstring says so, and it returns any entry whose only proposals are `stale` as well as any entry with none. So the work list can legitimately be LARGER than the batch. **Reconcile the two explicitly and report the reconciliation:** list the entry IDs the ingest inserted, list the work list, and name any entry present in the work list but NOT in this batch. Do **not** silently classify such an entry as part of this cycle, and do **not** silently skip it — **halt and report it** under the halt discipline above. An unexpected older entry surfacing usually means a prior proposal went `stale`, which is itself the plan-204 failure signature and belongs in the CEO's hands, not in a classification.
>
> For each entry ID in the work list: read `id, source_heading, raw_content, tags, entry_date` from `lesson_entries`, apply the ADR-002 taxonomy, and call `insert_proposal(conn, ...)`. **All FOUR of these are REQUIRED positional args (the function has no defaults for them) — supply every one:**
> - `category` — one of `structural`/`instrumentation`/`governance_rule`/`language`/`narrative` per ADR-002 (the drafting-cycle amendments are `governance_rule`, matching plan 228's 149–154; do NOT hand-assign `duplicate` — the cycle function owns that).
> - `suggested_action` — a concrete natural-language recommendation for the entry (what should change and where). This is not optional; omitting it is a `TypeError`.
> - `reasoning` — cites specific `raw_content` text from that entry (see the evidence rule below).
> - `confidence` — one of `low`/`medium`/`high`.
>
> **Set `target_layer` and `target_artifact` per the specialist file** (`FORGE_LESSONS_AGENT.md` — the agent assigns these; a `governance_rule` amendment gets `target_layer='governance'`, `target_artifact='PLANNER_TEMPLATE.md'`, exactly as plan 228's proposals 149–154 do — DB-verified). **Only `route` and `subcategory` stay `None`:** `route` is the Gate 1 CEO disposition (NULL at classification — the record's `codify`/`reference` values were added later at Gate 1), and `subcategory` is Phase-2-reserved. Use `status='ambiguous'` (the default status is `proposed`) only for a genuine no-fit. ⚠️ Do not conflate the two: leaving `target_layer`/`target_artifact` NULL would contradict both the specialist file and every prior cycle's proposals — only `route` is Gate 1's. Do NOT dedup against PLANNER_TEMPLATE — Gate 1 dedups against the LIVE template (2026-06-07 discipline); your job is classification only. **`conn.commit()`** after inserting the proposals (SQLite durability, as in Step 1b), THEN git-commit the two `.md` deposits.
>
> **`reasoning` is quoted evidence, not free narration.** Every proposal's `reasoning` must cite specific text from that entry's own `raw_content` — quote it, and name the entry ID it came from. Gate 1 disposes proposals by reading this field and does not re-read the source entry; a `reasoning` that paraphrases, embellishes, or imports a claim the entry does not make becomes a false premise wearing the authority of a completed classification. Do not carry any assertion from this plan's CEO Context into a `reasoning` field as if the entry said it — the entry is the only source.
>
> **If any entry classifies `ambiguous`, call it out by ID at the TOP of your summary with the specific reason.** An ambiguous proposal carries no route, so Gate 1 has nothing to dispose and the arc stalls on it. This matters most for the three Drafting-Cycle amendment entries — they are the arc's payload; an ambiguous verdict on one of them is a finding the CEO needs immediately, not a line in a distribution table.
>
> **Disk-verify every filesystem claim in your SUMMARY (Rule 52, and one of this batch's own entries is the grep-presence-is-not-effect lesson).** This applies to the analytical claims in your classification summary and synthesis — distinct from the `reasoning` DB field above, which quotes `raw_content` only and by construction makes no filesystem claim. If any summary claim asserts a file, function, or section exists, does not exist, or moved, verify it against disk with `ls`/`grep`/`git log` BEFORE writing it, and state in the summary that you did.
>
> **⚠️ One tension to surface, not to resolve — and it is THREE-WAY, not two.** The cycle's stop condition currently has three competing statements:
> 1. **The live template** (`## The Drafting Cycle`) — repeat until a pass honestly reports **diminishing returns**, with CEO rationale preserved in that section defending it.
> 2. **One entry in this batch** — re-run the **same lens until it runs dry**, then advance.
> 3. **CEO direction, 2026-07-20** — **one pass per lens; walk the whole lens list; a lens is re-run only when the cycle starts the list over.**
>
> These are not the same rule, and (3) post-dates and corrects the entry that states (2) — which means **Gate 2 cannot codify that entry verbatim.** **Do not decide between them; that is a Gate 2 authoring call.** Record all three in your synthesis, each with the source you read it from (template line, entry text, this plan), so the conflict reaches Gate 1 already visible instead of being discovered mid-codification.
>
> **Deposit:** `knowledge/development/classifications-summary-2026-07-20.md` — the raw cycle dict, count, category/confidence distribution, per-entry reasoning, and cluster synthesis for CEO Gate 1. **Expect and name the Drafting-Cycle cluster** (the entries amending `## The Drafting Cycle` belong together) and the diminishing-returns/dry tension above. Plus `knowledge/development/dev-log-cycle-step-1-2026-07-20.md` with an Output Receipt (cycle dict verbatim, total classified, distribution, derived work list, flags). Canonical Python file-write pattern — no heredoc. Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-summary-2026-07-20.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-07-20.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV

---

> **Before starting, read the Step 1 deposits and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2.
>
> You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md`; skip with a note if absent).
>
> **Working location — same rule as Step 1.** Run commands from **your own working tree**; canonical DB by ABSOLUTE path is the only exception. Do NOT `cd` to the main tree.
>
> **Scope:**
> - `reports/lessons-report-2026-07-20.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-07-20.md`
>
> **Before generating: check whether `reports/lessons-report-2026-07-20.md` already exists. If it does, HALT and report — do not overwrite it.** `generate_lessons_report` writes that path unconditionally, so a Step 2 re-run after a partial failure silently destroys the first run's report, which is the only record of what that run produced. Verified at authoring time: no 07-20 report exists (the most recent is 2026-07-17), so the expected state is "absent". If it is present, something ran before you did and the CEO needs to know that before anything is overwritten.
>
> Run `generate_lessons_report(conn, "2026-07-20")` against the canonical DB.
>
> **Two halt conditions, both regressions rather than noise:**
> 1. All route values are NULL this cycle — the report must render without route lines (plan-128 conditional render). If any `- **Route:**` line appears, **halt and flag**.
> 2. **If any `Recently-implemented overlap:` advisory line appears, halt and flag.** Plan 207 retired that detector entirely; its output reappearing means the retirement regressed. Do NOT tune or reinstate it.
>
> `generate_lessons_report` resolves `output_dir="reports"` RELATIVE to cwd — which is why the working-location rule above is load-bearing here rather than boilerplate. Run `pwd` before the call, capture the **path the function RETURNS**, and state that resolved absolute path in your dev log. **Confirm the returned filename matches the file named in Scope above; if the function's naming convention differs, report the actual name rather than renaming the file to match this plan.**
>
> Print the report head (~80 lines) for the transcript.
>
> **Deposit:** the report plus `knowledge/development/dev-log-cycle-step-2-2026-07-20.md` with an Output Receipt (report length, proposals surfaced, route-line count, advisory-line count). Canonical Python file-write pattern — no heredoc. Commit both. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-07-20.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-07-20.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 1 and Step 2 deposits and confirm both Output Receipt statuses Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA).
>
> You are Lessons Forge QA. Read `agents/FORGE_LESSONS_AGENT.md` first. **Working location — same rule as Steps 1 and 2:** run commands from your own working tree; canonical DB by ABSOLUTE path is the only exception. **Verification + reporting only — no product-code changes.** If a test fails, **report it — do NOT fix it**. If you find a blocker, STOP and report it. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly; route it via the receipt.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present in your deposited report.
>
> **Evidence-source rule.** Every SQL/PRAGMA row states which DB it ran against. Canonical reads use `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "<query>"`. Worktree DB absence is never a substitution reason. Deposit **RAW command output, never a summary of it** — a hand-written summary is not acceptable evidence.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-07-20.md`
>
> Verification table, one row per claim, each with a DB-source column:
> 1. **Full suite** — `python3 -m pytest src/ -v` (`python3 -m pytest`, NOT the `timeout` binary — unavailable on macOS) to an explicit pass/fail, raw tail shown. **Compute the baseline yourself from `--collect-only` and reconcile it against the most recent prior QA report in `knowledge/qa/`; do NOT carry a number forward from any plan text, including this plan's.** Report the actual and confirm 0 regressions.
> 2. `get_unclassified_entries(conn)` on canonical returns `[]` — every entry this cycle ingested is now classified. **The one legitimate non-empty result is a G6 deferral:** if Step 1's deposit contains a `### Deferred entries (CEO-approved)` heading (the G6 outcome (ii) path), the row passes iff the residual list equals exactly those deferred IDs — quote both the deposit heading and the query output. Any residual entry NOT on that CEO-approved list, or a non-empty result with no such heading in the Step 1 deposit, is a **FAIL**.
> 3. **Invariants** on canonical: dangling proposals 0, invalid category 0, invalid confidence 0, and every proposal created this cycle has `route IS NULL`. **Also verify the target fields WERE set** (Step 1 requires them — see the classification contract): every non-`ambiguous` proposal created this cycle has `target_layer IS NOT NULL` and `target_artifact IS NOT NULL`, and the `governance_rule` amendments specifically carry `target_layer='governance'` + `target_artifact='PLANNER_TEMPLATE.md'` (this is what pre-stages them for Gate 2). A non-ambiguous proposal with NULL target fields is a **FAIL** — the requirement went unenforced.
> 4. **The 204 fix held (the hash-trap regression watch).** Read the **pre-cycle baseline table Step 1 deposited in its dev log** — proposals by status, proposals by category, entry count, and the highest-id entry's `content_hash`. If that baseline is missing from the Step 1 deposit, **halt**: this row is unverifiable without it and a post-hoc count proves nothing. Re-read the same figures from canonical now and diff them. Confirm `stale` has NOT grown, no proposal moved off a terminal status, and the pre-existing entry hash Step 1 recorded is unchanged. Report `updated_count` and `terminal_proposals_flagged` as Step 1 recorded them. If anything was demoted, halt loudly.
> 5. **Report** exists, proposal counts match DB, zero `- **Route:**` lines, **zero `Recently-implemented overlap:` lines**, and `detect_recently_implemented_overlaps` is still absent from `src/` (plan 207 retirement intact).
> 6. **No schema drift** — `.schema lesson_entries` / `.schema lesson_proposals` on canonical vs `src/db.py` DDL. This plan changes no schema. Any delta is a FAIL.
> 7. **PLANNER_TEMPLATE.md is UNCHANGED by this arc.** ⚠️ **This row is the ONE place you must reach outside your working tree, and it is a deliberate second exception to the working-location rule** (the first being canonical-DB access). `lessons-forge` is a **submodule**; `PLANNER_TEMPLATE.md` is tracked by the **root** repo at `/Users/marklehn/Developer/GitHub` and does **not exist** in your worktree — a plain `git diff -- PLANNER_TEMPLATE.md` from where you are will find nothing and pass vacuously. Run it against the root repo explicitly: `git -C /Users/marklehn/Developer/GitHub diff --exit-code -- PLANNER_TEMPLATE.md`, and show the exit code. Exit 0 is the pass; any diff is a FAIL. (Self-contained deliberately: do NOT assert what version the header "should" read — no baseline for that was captured, and an eyeballed version string is not evidence.) Codification is Gate 2; this cycle must not have touched the template.
> 8. **Post-cycle DB counts** — entries total, proposals by status and category, stated as actuals. **Expected entries total is 151** (146 pre-cycle + 5 this batch); the 146 includes ~57 orphan rows from historically-reworded headings and is NOT the file's 94-entry count — do not flag 151 as anomalous. Report the actual; a value other than 151 is worth a note, not necessarily a fail (a concurrent reword could shift it), but explain it.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-07-20.md` — verification table with DB-source column, raw full-suite tail, the mandatory Rule 20 banner + PASSED line, and an Output Receipt with status. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (cycle 2026-07-20 complete: the 07-19/07-20 batch ingested and classified, report deposited, corpus integrity held; Gate 1 route disposition pending, including the Drafting-Cycle amendment cluster and the diminishing-returns/iterate-to-dry tension); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-07-20.md`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.
