# Lessons Forge — Cycle Run 2026-08-13, PLAN B: classify the 10 session-42 sweep entries, deposit the report

**Date:** 2026-08-13 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (classify all 10) → Step 2 (DEV — report) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always
**cycle_tier:** T1
**Slug:** `cycle-classify-s42sweep-2026-08-13`
**Project:** lessons-forge
**dispatch_mode:** bellows

## CEO Context

**Classification and report only.** Plan A (id 397, `cycle-ingest-s42sweep-2026-08-13`, Done) ingested the 10 session-42 sweep entries as **329–338**; this plan turns them into proposals **337–346** (predicted; the DB assigns) and deposits the report. Gate 1 (route disposition) and Gate 2 (codification) remain separate plans with CEO decisions between. Clone origin: **382** (the newest same-class Plan B; its single-tranche shape carries at 10-entry scale — 382 shipped 4 in one tranche and the tranche rule keys on step saturation, not count; the 279 calibration puts 10 far below the measured cliff).

**This plan contains NO destructive write TO THE DB** (382's property, re-verified): `insert_proposal` only adds rows; no ingest, no UPDATE, no delete. ⚠️ **It is NOT write-free on the filesystem: it OVERWRITES one committed file** — `reports/lessons-report-2026-08-13.md`, plan 382's report (FALSE-HERE item 5). The overwrite is declared, git-recoverable at `595ae5c`, and preceded by a verified copy-aside; 382's blanket "no destructive write" sentence would have mispriced this plan's risk and is deliberately scoped here.

**Tier: T1** — same computation as 382: parent cycle closed dry (Plan A closed at walk 4, both gates first-run clean), additive-only production-data writes (T-2) compute T1; structure-for-structure clone of shipped 382 keeps T-8 silent.

### What Plan A established — each item RE-MEASURED at authoring 2026-08-13, read-only

| fact | measured now |
|---|---|
| the 10 entries exist | ids **329–338**, `MAX(lesson_entries.id)` 338, COUNT 338, `sqlite_sequence` agrees |
| no proposals exist for them | `entry_id > 328` → **0 rows** |
| `P0` = **336** and did NOT move | `MAX(lesson_proposals.id)` 336, `sqlite_sequence` 336 — the split's invariant, re-measured not inherited |
| the work list | `get_unclassified_entries()` = **exactly [329, 330, 331, 332, 333, 334, 335, 336, 337, 338]**, ascending |
| the Gate-2 queue | `accepted` = **0** (nothing to protect) |
| `STALE_COUNT` | **3** (proposals 98/121/130, settled) |
| `SURFACEABLE_BASE` | **0** (no `proposed`/`ambiguous` row exists) |
| batch `raw_content` range | **847–1155** chars (382's 1216–1534 does NOT carry) |
| ⚠️ DB `tags` column | **NULL for all ten** — the tag lives in the heading text (**5× `[tag: drafting-cycle]`, 4× `[tag: verification]`, 1× `[tag: operational-recovery]`** — a different mix from 382's 2/1/1); report the heading-embedded tag, never assert the column |
| report predicate | `WHERE p.status IN ('proposed','ambiguous')` — source-verified `src/lessons_forge.py:541` (UNCHANGED); **surfaced expectation = SURFACEABLE_BASE + 10 = 10** |
| `insert_proposal` | `src/lessons_forge.py:202` (UNCHANGED) — five required positionals BY NAME in order (`conn, entry_id, category, suggested_action, reasoning, confidence`); a sixth positional binds to CHECK-constrained `status` and fails; `status`/`target_layer`/`target_artifact`/`duplicate_of`/`subcategory`/`route` are keywords (signature re-verified live by `inspect.signature`) |
| sentinel | entry **328** content-hash `63b3831d2ddfdd553d9b8904df40723dbbd50d6fa442db72f2d16cfeb8762d26` (Plan A's sentinel, carried) |
| FORWARD.md baseline | **18** pipe-lines by `grep -c "^| "` — re-measured, unchanged since 382; same probe form at every gate |
| Plan A's pristine backup | `data/backups/lessons-forge-pre-cycle-397-20260814T123337Z.db` (from 397's dev log; verified present on disk) |

### ⚠️⚠️ INHERITED FACTS FROM 382 THAT ARE FALSE HERE

5. **A 2026-08-13 REPORT ALREADY EXISTS — 382's own, committed at `595ae5c` (`reports/lessons-report-2026-08-13.md`).** 382 measured "no 2026-08-13 report exists"; that premise is dead the moment two cycles run on one date. **Consequence, DECLARED not discovered:** `generate_lessons_report(conn, "2026-08-13")` writes the same filename, so this plan OVERWRITES 382's report. This is accepted and is the correct behaviour — the report is a **whole-corpus generated artifact keyed by date**, its predicate surfaces only `proposed`/`ambiguous` rows, and 382's four proposals are now `implemented` (flipped by 386/389), so the regenerated report is a strict superset in currency, not a loss of information. Two guards: (a) 382's version stays recoverable at commit `595ae5c` — named here so a reader never has to hunt it; (b) Step 2 copy-asides the existing file BEFORE regenerating, and that arm is now the **EXPECTED path**, not an exception branch.
6. **The overlap detector's string does not exist in the generator** — `grep -F "Recently-implemented"` over `src/lessons_forge.py` returns nothing (measured). 382's zero-expectation therefore carries as a **regression sentinel for a REMOVED feature**: zero lines is the pass, and a non-zero count means the feature returned (plan-207's class) → HALT. Stated so no future clone reads the zero as evidence the feature ran and found nothing.
7. **A parallel terminal is live** (it shipped invoice-pulse plans 393–396 this session and shares the root repo; `id_sequence` next **399** at authoring — a PREDICTION, re-read at deposit). It touches no lessons-forge store. The FORWARD/`decisions/`-posture checks are the in-window detectors.

### ⚠️ NUMBERING
- **`lesson_entries.id` 329–338** — created by Plan A; this plan never writes entries.
- **`lesson_proposals.id` 337–346** — the 10 proposals this plan creates (predicted; the DB assigns).
- Pairing `entry 329+k → proposal 337+k` (offset **+8**) is a DERIVATION, never an operand. **Never write a bare numeral in 329–346 without its namespace.**
- **`lesson_proposals.id` ≤ 336** — PRE-EXISTING. Touch none of them.

### Flag (G) — mechanism-versus-discipline, the batch's live instrument (producer: Step 1's disposition lines)
**Ten entries, SEVEN clusters** (382's batch was 4 in 3). The Planner's authoring-time read, handed as EXPECTATION not gate — the classifier applies the test to each entry's own `How to apply:` and may disagree (**licence stated; a disagreement is a finding, not an error**):

- **Cluster 1 — the register/validator pair (entries 330, 331):** DUP-APPEND rows and headerless-row invisibility. **MECHANISM-shaped, owner named, and ALREADY SHIPPED — see Flag (H).** Name the pairing in both disposition lines.
- **Cluster 2 — the ops-compound singleton (entry 329):** one action per compound with a post-condition close, plus the Gate-1-severance framing. **MECHANISM-shaped, owner `PLANNER_TEMPLATE.md` Rule 85 — ALREADY SHIPPED, Flag (H).**
- **Cluster 3 — attestation integrity (entries 334, 337):** a summary attesting a run that never happened / a pre-classification falsified by its own instrument (334), and stale deliverable counts in templates after a late addition (337). DISCIPLINE-shaped; mechanism candidates in `DRAFTING_CYCLE.md` §2.7's lens-attestation and record-sweep bullets. Pair-cluster.
- **Cluster 4 — probe integrity (entries 333, 336):** in-transaction sentinels print before COMMIT (333) and probes authored from prediction rather than measurement (336). DISCIPLINE-shaped with strong mechanism candidates (a QA-row convention for post-COMMIT read-back; a probe-derivation clause beside §2.7's execute-against-real-data bullet). Pair-cluster.
- **Cluster 5 — the anchor-decoy singleton (entry 335):** a strike note quoting a structural token becomes a second anchor match. DISCIPLINE-shaped; candidate owner `DRAFTING_CYCLE.md` §2.7's edit-anchor bullet.
- **Cluster 6 — the realpath/inode singleton (entry 332):** a case-insensitive filesystem defeats a string-realpath guard. MECHANISM-shaped, owner is a **builder-authoring convention with no single artifact today** — say "unnamed" rather than inventing one; Gate 1 decides the home.
- **Cluster 7 — the deposit claim-race singleton (entry 338):** daemon claims within one second; predict ids, never mint. DISCIPLINE-shaped, largely already carried by PLANNER_TEMPLATE + memory; Gate 1 dedups.

**Cluster synthesis for Gate 1** (Step 1 deposits it; no other step owns it): *"10 entries, seven clusters: the register/validator pair (330/331 — mechanism, ALREADY SHIPPED in plan 392), the ops-compound singleton (329 — mechanism, ALREADY SHIPPED in PT v4.88 via 389), the attestation pair (334/337 — discipline, §2.7 candidates), the probe-integrity pair (333/336 — discipline with strong mechanism candidates), the anchor-decoy singleton (335), the realpath/inode singleton (332 — mechanism, owner unnamed), the claim-race singleton (338 — discipline, likely already carried). Tags heading-embedded (5 drafting-cycle / 4 verification / 1 operational-recovery), DB column NULL 10/10."*

### ⚠️ Flag (H) — THE ALREADY-SHIPPED SUBSET (new this batch; hand to Gate 1, do NOT act on it here)
**Three of the ten document remedies that SHIPPED THIS SESSION, after the lesson was written:** entry 329's ops-compound rule shipped as `PLANNER_TEMPLATE.md` Rule 85's widening (plan 389, PT v4.88); entries 330 and 331 shipped as the walk-register schema v0.3 guards and `walk_register_lint.py`'s `duplicate_row` / `headerless_rows` checks (plan 392). **This is a classification input, not a classification verdict — and emphatically not a licence to skip them:** the corpus records the lesson independently of whether a remedy exists, and **Gate 1 owns the dedup against live doctrine** (382's rule, carried verbatim). The classifier states the shipped-remedy fact in `suggested_action`/`reasoning` where it applies so Gate 1 routes from evidence rather than rediscovering it; a plausible Gate-1 outcome for these three is `reference`/`implemented` rather than `codify`, but that call is not this plan's.

**Scope discipline:** classification + report only. Routes stay NULL at insert (Gate 1 assigns). Do NOT edit doctrine files, `plan_lint.py`, `gates.py`, or `LESSONS.md`. Do NOT touch proposals with id ≤ 336. Do NOT touch entries (no ingest — Plan A's mutation is done). **⚠️ The `LESSONS.md` freeze re-engages while THIS plan sits deposited-but-un-run** (PT v4.88's rule; the daemon's same-second claim makes the window seconds wide — measured three times this session).

**Concurrency:** deposit with no other lessons-forge cycle in flight (397 reached Done at `cc99785`; verified before deposit). The parallel terminal's invoice-pulse work is store-disjoint.

### ⚠️ Planner obligations at the verdict gates
- Compare the `steps` table against commit and deposit counts before any verdict.
- At every gate: `accepted` count still 0 (or in-window Gate-1 dispositions of THIS batch's proposals — `ceo` actor, in-window stamp — recorded and carried, per Step 2's carve-out).
- FORWARD.md delta ZERO at every gate (baseline 18 pipe-lines, same probe form); any row is a finding — a `NONE.`-item row is a regression of plan 376's guard, a real-text row is a foreign writer.
- Re-verify, never inherit, any authoring measurement a verdict turns on.

---

## Drafting Cycle

**Tier:** T1 — see the computation above. Clone of 382 (newest same-class Plan B) at 10-entry scale, single tranche carried; every inherited fact re-measured (the tables above); Plan A (397)'s cycle record is the adjacent parent.

**Walk register:** `governance/knowledge/research/walk-register-cycle-classify-s42sweep-2026-08-13.md` (schema 0.3), committed per phase.

**Walk 0 (context pin):** the re-measured tables ARE the pin — worklist [329–338], P0 336, `sqlite_sequence` agreement, batch proposals 0, accepted 0, stale 3, surfaceable 0, raw_content 847–1155, tags NULL 10/10 with the 5/4/1 heading mix, predicate `:541` and `insert_proposal` `:202` signature both re-verified live (incl. every keyword), sentinel entry-328 `63b3831d…`, FORWARD 18 pipe-lines, Plan A's backup verified on disk, tests 55 passed, `id_sequence` 399 (prediction), hostile headings 2 (entries 330/335). **Clone-diff vs 382 (run BEFORE walk 1, every inherited guard verified against live data):** the report-collision premise INVERTED with the overwrite declared and copy-aside promoted to the expected path (item 5); the overlap-detector expectation re-grounded as a removed-feature sentinel (item 6); flag (G) rebuilt for this batch (seven clusters vs three); **flag (H) is NEW** (no 382 antecedent — three entries' remedies shipped in-session); numbering bands re-tokened (337–346, wall ≤ 336); the staling-arm backup re-pointed to 397's; the parallel-terminal note added (item 7). Every count-parameterized guard verified at 10 (surfaced 10, manifest 10, row-3 ten rows, distribution delta +10). **Scout seat: DECLINED — T1, proven-clone shape, additive-only writes, per 382's own precedent; recorded per §2.0.**

**Walks (2 warm):**
- Weak spots:          w1 dry (pre-flight, manifest-first, per-insert commit and all three resume arms re-read against the measured tables; every count agrees with the 10-batch); w2 dry.
- Destruction:         w1 1 folded — instruction: the cloned header claim "NO destructive write" was true of the DB and FALSE of the filesystem once the report collision (item 5) was established; scoped to the DB with the overwrite named inline; w2 dry (the copy-aside + `cmp` + mandatory QA cross-check verified as a real restore path).
- Vulnerabilities:     w1 dry (signature/predicate/worklist re-verified live; route-grep `-F`/`--`/exit-code form carried; both hostile headings bound as parameters; `output_dir` cwd trap carried); w2 dry.
- Integration-record:  w1 dry (PT v4.88 freeze citation verified live; Deposits project-prefixed with Scope repo-relative per the origin — the path-FORM check 397's own cycle had to learn, applied deliberately here; stray-origin-token sweep zero operative hits); w2 dry.
- ACID:                w1 dry (three steps, two gate windows, additive-only; per-insert commits bound a mid-list death; the copy-aside precedes the only overwrite); w2 dry.

**Splits: w1 instruction 1 / record 0 · w2 all five lenses dry.** The bar is met at walk 2 with nothing restructured.

**Conformance (§5):** faithful-mirror plan_lint at the deposit-shaped scratchpad mirror — NEVER at the real `decisions/`. First run (post-walk-2) surfaced TWO WARNs, both instrument-side rather than plan-side: the placeholder lens lines this fill clears, and an (o1) missing-path advisory proving the MIRROR was unfaithful (it lacked `src/lessons_forge.py`, which this plan references by line number). Mirror repaired and re-run: **EXIT 0, ZERO WARNs**; (q) telemetry — the two sentinel tokens `ambiguous` (correct: a DB content-hash value with no file to verify). Last run: at the freeze.

**Closing:** walk 2 read dry on every lens — **instruction 0 / record 1: this Cycle-Log fill itself, written at close with measured content** (0 of 1 fold-introduced — the fill is the close's own act, named per §2's bar); the closing-record re-read ran against the filled block; clone-diff at walk 0 per §2.0 (five findings, four of them inherited-premise deaths); scout declined with reasoning; fold-and-deposit exactly once.

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for verdict. Do NOT proceed to Step 2 or move the plan to Done.
```

---

## STEP 1 — Classify all 10 (the whole work list; ONE tranche)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file. You are the Forge Lessons Agent (`agents/FORGE_LESSONS_AGENT.md`). Own working tree; canonical DB by ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (`forge/forge.db` is a different database — never open it).
>
> **Step 0 — dispatch state** (three-place probe on this step's dev log `knowledge/development/dev-log-classify-s42-step-1-2026-08-13.md`; probe-3 positive control against `knowledge/FORWARD.md`; state the determination first). **Single-writer check:** work list stable across two reads; `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — **THIS PROJECT ONLY** (other repos' `decisions/` contents are irrelevant and such files legitimately exist elsewhere); this plan's own file is the normal state, zero matches = broken probe, **any OTHER match → HALT**.
>
> **Pre-flight (read-only):** `get_unclassified_entries()` == `[329, 330, 331, 332, 333, 334, 335, 336, 337, 338]` exactly. Fewer with proposals already present for the missing ids → deposit-completion resume (below). More, or different ids → HALT. `MAX(lesson_proposals.id)` == 336 on FRESH (greater → foreign in-window insert → reconcile: extra rows with `entry_id ≤ 328` and non-this-plan provenance → record + HALT for CEO; this plan's own ids on a resume → resume arms).
>
> **Manifest FIRST:** write + commit the 10-id manifest (the work-list read verbatim) into the dev log stub BEFORE the first insert (`Status: Partial — in flight`).
>
> **Per entry, ids ascending:** read `id, source_heading, raw_content, entry_date` FROM THE DB ROW (⚠️ `tags` is NULL for all ten — the tag is heading-embedded: 5× `[tag: drafting-cycle]`, 4× `[tag: verification]`, 1× `[tag: operational-recovery]`); apply ADR-002 on a BODY read; call `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — **five required positionals BY NAME in that order; a sixth positional binds to CHECK-constrained `status` and fails**; `status`/`target_layer`/`target_artifact`/`route`/`subcategory` as keywords; **route stays NULL**; **`conn.commit()` after EACH insert** (a mid-list death costs the remainder, not the batch — load-bearing at 10). Shell-hostile headings (entries **330** and **335** — apostrophes): bind as parameters, never interpolate.
>
> **Flag (G)'s PRODUCER — every disposition line:** `| remedy: mechanism | owner: <named or "unnamed">` or `| remedy: discipline`, from the entry's own `How to apply:` (observed by Step 3 row 3). Where mechanism: `suggested_action` states the mechanism AND owner in its own words (Gate 1 routes from `suggested_action`). **Entries 330/335 are the register/validator pair — name the pairing in both lines; entries 334/337 and 333/336 are the other two pair-clusters — name each pairing likewise.** Entry 332's owner is genuinely **unnamed** today — say so rather than inventing an artifact.
> **Flag (H)'s PRODUCER — the shipped-remedy note:** for entries **329, 330, 331** the disposition line ALSO carries `| shipped-remedy: <plan id + artifact>` (329 → PT v4.88 Rule 85 via plan 389; 330/331 → schema v0.3 + walk_register_lint guards via plan 392), and `reasoning` states the fact. **This does NOT change the classification you would otherwise make and is NEVER a reason to skip an entry — Gate 1 owns the dedup.** The Planner's expectations are in CEO Context; **licence to disagree is granted — a disagreement is a finding, not an error.**
>
> **Deposit** the dev log: the manifest; per-proposal disposition lines (`- proposal=<id> entry=<id> category=<…> confidence=<…> | remedy: … | …`); the cluster synthesis (verbatim from CEO Context, corrected by anything classification surfaced); the created-proposal id list; `MAX(lesson_proposals.id)` after (expect 346). **Deposit-completion resume:** manifest present + all 10 proposals in DB + dev log incomplete → regenerate disposition lines from DB rows (`reason: not recorded (regenerated)`), **flag-(G)/(H) fields re-derived from the entries' own `How to apply:` and marked `remedy: re-derived on resume`** (they live in no DB column), re-deposit, stop. Canonical Python file-write; explicit-pathspec commit; name-only + toplevel asserts. `#### Prompt Feedback` · `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `knowledge/development/dev-log-classify-s42-step-1-2026-08-13.md`
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-classify-s42-step-1-2026-08-13.md`
>
> **STOP. Wait for verdict.**

## STEP 2 — DEV (generate the report)

> **Before starting: Step 1's Receipt carries a PROCEED-value** (allowlist: Complete / Complete-idempotent). Post a visible message. Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Own tree; canonical DB **read-only** (`?mode=ro`).
>
> **⚠️ THE 2026-08-13 REPORT ALREADY EXISTS (plan 382's, committed `595ae5c`) — the copy-aside is the EXPECTED path, not an exception.** Pre-check, branch never an unconditional HALT (340's brick-the-run lesson carried):
> - this step's dev log committed AND opening with a PROCEED-value → idempotent re-dispatch (append a `### Re-dispatch note`, stop);
> - otherwise (the normal FRESH path): **copy the existing report aside FIRST** to `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-report-pre-regen-<id>-<UTC-stamp>.md` (`<id>` = ACTUAL plan id; main tree, outside Scope; record as `copy-aside (pre-regen): <abs path>` — Step 3 row 0 cross-checks the token), verify the copy is non-empty and byte-identical to the source (`cmp`, echoed exit), THEN regenerate. **The overwrite is intended and declared** (CEO Context item 5); 382's version remains at `595ae5c`.
>
> Run `generate_lessons_report(conn, "2026-08-13")` — whole-corpus; the date is filename/title only. **`output_dir` defaults to `"reports"` RELATIVE TO CWD** — `pwd` first; state the returned absolute path; filename matches Scope.
>
> **Two derived expectations** (operands: Step 1's recorded 10-proposal list; missing/unparseable → STOP, no literal fallback):
> 1. **Surfaced proposals = 10** — derivation `SURFACEABLE_BASE (0, re-measured at authoring) + 10 classified` against the report predicate `status IN ('proposed','ambiguous')` (source-verified `src/lessons_forge.py:541`). Outside-the-10 surfaced row → reconcile-note + CONTINUE if attributable; unattributable → HALT. **Below 10 → check IN ORDER:** (i) any of the recorded 10 `status='stale'` (printed count token) → the staling signature → HALT naming Plan A's pristine backup (`data/backups/lessons-forge-pre-cycle-397-20260814T123337Z.db`, from 397's dev log, verified on disk at authoring); (ii) any of the recorded 10 `accepted|codify` with `ceo` actor + in-window stamp → a legitimate in-window Gate-1 → record + CONTINUE with the adjusted expectation. Neither explaining it → HALT.
> 2. **Zero `- **Route:**` lines** — count with `grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"` (**both `-F` and `--`; never pipe to `head`**): exit 1 = the expected zero; exit 0 = matches (attribute by `source_heading` via the DB join with BOUND parameters — two headings are shell-hostile; a route on one of OUR 10 with status still `proposed` → in-window Gate 1 → record + CONTINUE; any other → HALT); exit ≥2 = the check did not run → HALT, never record zero.
> - Any `Recently-implemented overlap:` line (same grep form + exit codes) → HALT. ⚠️ **This is a sentinel for a REMOVED feature** — the string does not occur in `src/lessons_forge.py` (measured at authoring), so zero is the pass and a hit means the feature returned (plan-207's class). Do not read the zero as evidence the detector ran a comparison.
>
> **Deposit:** report + dev log (`Status:` line first — Step 3 reads it; files-modified; the copy-aside token; report length; surfaced count; route-line count + exit codes; overlap count + exit code). Canonical Python write; explicit-pathspec commit; name-only + toplevel. `#### Forward Register`: `NONE`.
>
> **Scope:**
> - `reports/lessons-report-2026-08-13.md`
> - `knowledge/development/dev-log-classify-s42-step-2-2026-08-13.md`
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-13.md`
> - `lessons-forge/knowledge/development/dev-log-classify-s42-step-2-2026-08-13.md`
>
> **STOP. Wait for verdict.**

## STEP 3 — QA

> **⚠️ STEP 0 — DISPATCH-STATE DETERMINATION FIRST:** three-place probe on `knowledge/qa/cycle-classify-s42-qa-2026-08-13.md` with the positive control; a hit on ANY → idempotent re-dispatch (append `### Re-dispatch note`, leave the committed report untouched, STOP — a bare daemon retry re-emitting the register block is the dup-append defect). FRESH → state it first.
>
> **Before starting: Steps 1–2 Receipts BOTH PROCEED-values** (allowlist, named). Post a visible message. Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`); own tree; DB read-only; **verification + reporting only; no Monitor; no fixes.**
>
> **Rule 20 self-check** (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`): `plan_slug` `cycle-classify-s42sweep-2026-08-13`; `qa_report_path` `<tree-abs>/knowledge/qa/cycle-classify-s42-qa-2026-08-13.md`; `evidence_dir` `<tree-abs>/knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/`; `required_evidence_files` `["pytest_targeted.txt", "proposals.txt", "report.txt", "schema.txt"]`. All four files AND the report with its table BEFORE the block; append stdout; the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line byte-exact in the deposited report; self-grep. Rule 19 verbatim; one glyph per status cell; no `|` in cells; `## Evidence and Narrative` directly after the table.
>
> Table under `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |` — run ALL rows, then halt if owed:
> 0. **Deliverables (Rule 17)** — Steps 1–2 committed deposits: `git log --oneline -1 -- <path>` (empty = ❌) + porcelain with echoed exit; **the copy-aside token cross-check is MANDATORY here** (Step 2's copy-aside is the expected path, not conditional): the recorded absolute path exists and is non-empty.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail → `pytest_targeted.txt`; value cell `<N> passed` only (baseline 55 passed at authoring; delta reported never asserted).
> 2. **`get_unclassified_entries(conn)` == `[]`** — the classify-plan inversion of Plan A's row 2: a NON-empty list means classification is incomplete; quote with a count token. Non-empty → ❌ Critical.
> 3. **Ten proposals, exactly ours** — `SELECT p.id, p.entry_id, p.category, p.status, p.route, p.confidence FROM lesson_proposals p WHERE p.entry_id > 328 ORDER BY p.id` → 10 rows; entry_ids exactly 329–338; ids match Step 1's recorded list (predicted 337–346; the RECORD is the operand); every `status='proposed'` (or in-window `accepted|codify|ceo` — reconcile per the carve-out, named ids); every `route` NULL (same carve-out); **every disposition line in Step 1's dev log carries the flag-(G) field** (grep the committed dev log; a missing field = ❌ by id); **entries 329/330/331's lines carry the flag-(H) `shipped-remedy` note**; the three pair-clusters (330/331, 334/337, 333/336) are each named in both of their lines. Total `lesson_proposals` == **346** (336 + 10); above → name foreign ids, reconcile. → `proposals.txt`
> 4. **Report integrity** — report exists at the Scope path; surfaced count == the Step-2 recorded expectation (10, or its recorded in-window adjustment); the route-grep + overlap-grep exit codes from Step 2's dev log re-run fresh (same `-F`/`--`/exit-code form); report references the 10 by heading (spot-check 2 with bound-parameter joins — both hostile headings among them). → `report.txt`
> 5. **No schema drift** — PRAGMA + constraints vs `src/db.py`; raw `.schema` → `schema.txt`.
> 6. **Corpus preservation** — entries still 338/338; sentinel entry-328 content-hash `63b3831d2ddfdd553d9b8904df40723dbbd50d6fa442db72f2d16cfeb8762d26` unchanged; stale still 3 (98/121/130); `accepted` still 0 OR only the row-3 carve-out ids; the 8-status zero-emitting distribution delta is EXACTLY +10 `proposed` (or the carve-out split), every other bucket unchanged. → `proposals.txt`
> 7. **Register posture** — lessons-forge `decisions/` non-Done contents: this plan's own `in-progress-*` file ONLY (any other = in-window deposit, report names; other repos out of scope); **FORWARD.md delta since the authoring baseline (18 pipe-lines by `grep -c "^| "`) is ZERO; ANY new row is a finding: a `NONE.`-item row = a regression of plan 376's guard (❌ naming it), a real-text row = foreign writer (❌ naming it).** → `report.txt`
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit deposits: cd-first + pathspec + name-only assert + bare `git rev-parse --show-toplevel`.
>
> **Scope:**
> - `knowledge/qa/cycle-classify-s42-qa-2026-08-13.md`
> - `knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/proposals.txt`
> - `knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/report.txt`
> - `knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/schema.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-classify-s42-qa-2026-08-13.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/pytest_targeted.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/proposals.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/report.txt`
> - `lessons-forge/knowledge/qa/evidence/cycle-classify-s42sweep-2026-08-13/schema.txt`
