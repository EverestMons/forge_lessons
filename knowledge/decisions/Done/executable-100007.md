# forge_lessons — executable: cycle W=28 — ingest + classify the 28 post-08-26 corpus entries, the FIRST forge cycle on the mini (NO routing; Gate 1 follows outside, non-author)

**Date:** 2026-09-01 | **Project:** forge_lessons | **Tier:** Small | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** targeted (the forge suite — 80 tests at forge_lessons `9dea317` — run into a per-plan evidence file; the pins + fresh-connection post-conditions are the instrument for the DB) | **Execution:** Step 1 (DEV — ingest) → Step 2 (Lessons Agent — classify) → Step 3 (QA — report + probes + suite) | **qa_steps:** 3 | **pause_for_verdict:** always

**auto_close:** false

**Depends on:** the CEO's "Go" (2026-09-01) after the pipeline's re-homing: the lessons-forge DB lives ONLY on the Mac mini since 2026-09-01 (`forge_lessons/CLAUDE.md` "Database Files"; fingerprint `9d9fa77d…5330` proven identical to the retired shop copy); the mini's daemon watches this project (verified). Clone of `Done/executable-556.md` (the NEWEST same-class plan, 2026-08-26, W=3) with the 530 Lessons-Agent classify step RESTORED — a declared deviation: 28 entries is a judgment batch, not a dictated one. Walk register: `/Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-cycle-w28-2026-09-01.md` (governance root, per §3).

## CEO Context

**Ingest + classify only — NO ROUTING.** Every proposal this plan mints leaves `route` NULL and `status` `proposed`. Gate 1 follows OUTSIDE this plan under the 459 non-author law (*the classifier may propose; only Gate 1 may accept, and Gate 1 is not the Planner*): the CEO has named the shop machine's Remote Control session as the cold non-author for the routing packet, with the flips applied on the mini where the DB lives.

⚠️ **This is the first forge cycle dispatched on the mini.** Every path in this plan is the MINI's: the DB `/Users/marklehn/Developer/forge_lessons/lessons-forge.db` and the register `/Users/marklehn/Developer/eluvian-governance/LESSONS.md` are the two deliberate absolute operands (both outside your worktree; the DB is untracked by policy). `src/paths.py` resolves relative to the checkout it runs from and finds NO DB inside a worktree — pass these two paths explicitly, never rely on discovery. The shop's plans in `Done/` carry the shop's paths; they are not this machine's.

⚠️ **Two entries WILL update at ingest, and that is the expected state.** Entries **347** and **398** carry riders later sessions wrote into their bodies (347: the 2026-08-27 "still pending, and it cost us again" note; 398: the 2026-08-26 "RECURRED" note). Both proposals (355, 406) are `implemented` — terminal — so the ingest FLAGS them and stales nothing. Rehearsed with the real functions on a scratch copy: the M1 dict below is that rehearsal's exact output. 556 halted on `updated > 0`; this plan halts on anything OTHER than exactly those two.

⚠️ **Corpus freeze — this deposit IS the freeze.** No `LESSONS.md` append (no wrap 3b sweep) from deposit until this plan closes: M8 pins the register's sha and Step 3 re-asserts it, so an append between steps fails a CORRECT run (the 2026-08-23 wrap-collision class). Guard (a) of the wrap applies.

**Author-conflict disclosure, date-keyed:** the four entries dated **2026-09-01** (ids 430–433 after ingest) were written by two mini Planner sessions of this same day (e62dc27b, c8dcc100); the authoring Planner session of THIS plan (90cfa5b9) wrote none of the 28. They are marked `[AUTHOR-CONFLICT]` anyway — the marker is disclosure for Gate 1; over-marking costs one read, under-marking hides a conflict.

## Numbers discipline

⚠️ **This table is the ONLY place a quantity is declared; every value MEASURED 2026-09-01 on the mini (read-only against the live DB; the ingest dict from a scratch-copy rehearsal of the real functions). The agent re-measures each pre-flight; mismatch → HALT with measured vs expected. Bind every id and heading as a PARAMETER — batch headings contain backticks, apostrophes and quotes.**

| id | pin | before | after | probe |
|---|---|---|---|---|
| M1 | ingest result | — | EXACTLY `{inserted: 28, updated: 2, unchanged: 346, stale_proposals_marked: 0}` with `terminal_proposals_flagged` naming exactly `{entry 347 / proposal 355 / implemented}` and `{entry 398 / proposal 406 / implemented}` | the dict returned by `ingest_lesson_entries`; ANY deviation → `ROLLBACK` and HALT listing the measured dict |
| M2 | unclassified | **0** → **28** post-ingest | **0** post-classify (the inversion) | `get_unclassified_entries(conn)` on a FRESH read-only connection |
| M3 | P0 proposals | **413, ALL terminal** (implemented 314 / reference 29 / rejected 38 / stale 3 / superseded 29; proposed 0, accepted 0) | 413 + `K`, `K` ≥ 28 (K record-only — pinning K forces fabrication) | `SELECT status, COUNT(*) … GROUP BY status` |
| M4 | new-proposal band | — | route NULL AND status `proposed`, every one | `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND (route IS NOT NULL OR status <> 'proposed')` → **0** (MAXP = the captured pre-flight MAX(id), 413 expected — bound, never hard-coded) |
| M5 | pre-existing terminal set | the full `(id, status, route)` triple-set for ids <= MAXP, captured pre-flight | **SET-IDENTICAL** post (a count cannot see a value move) | full triple-set select, compared as sets |
| M6 | E0 entries | **405**, MAXE=405 | **433**; new band **406–433** contiguous, `entry_date` between 2026-08-26 and 2026-09-01 | `SELECT COUNT(*), MAX(id)`; `SELECT id, entry_date FROM lesson_entries WHERE id > :MAXE ORDER BY id` |
| M7 | `[AUTHOR-CONFLICT]` markers | — | **4** — exactly the proposals whose entry has `entry_date='2026-09-01'`, NEVER an id range | BOTH directions, parameter-bound: (i) the set of `entry_id` over new proposals whose reasoning LIKE '%[AUTHOR-CONFLICT]%' == the set of `lesson_entries.id` with `entry_date='2026-09-01'` in the band (4 = 4); (ii) zero new proposals carry the marker whose entry is dated otherwise |
| M8 | the register | parser yields **376** entries; sha256-prefix `f4b732f1c6bb2fa113bc` | **byte-unchanged** — this plan READS the register, never writes it | `shasum -a 256 /Users/marklehn/Developer/eluvian-governance/LESSONS.md`; `len(parse_lessons_md(<path>))` |
| M9 | the six prior reports (destructible, tracked) | 08-13 `7cfd7904c84919764530` · 08-14 `f1807cf266b369541ce5` · 08-15 `b21281169ac1a138ade4` · 08-19 `7f9b283bf42a31eb9fca` · 08-25 `0984fdd3521e682c3c0a` · 08-26 `3c8362d2191da39ec388` | **all six byte-identical** | worktree-anchored `shasum -a 256`; recovery `git -C "$(pwd)" checkout -- reports/<file>` |
| M10 | today's report | ABSENT | exists at `"$(pwd)/reports/lessons-report-2026-09-01.md"`, none of M9 | ls + shasum, worktree-anchored (⚠️ the 425 trap: NEVER the main-repo absolute path) |
| M11 | content hashes of pre-existing entries | the `(id, content_hash)` set for ids <= MAXE | SET-IDENTICAL **except** 347 → `8074f58c13c75e2a6ce5…` and 398 → `3ccad66aec088b633e98…` (prefixes) | full select, compared as sets after removing the two named ids; the two re-selected individually |
| M12 | stale proposals | **3** | **3, unchanged** | `SELECT COUNT(*) FROM lesson_proposals WHERE status='stale'` |
| M13 | the backup | ABSENT | `/Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-01-<HHMMSS>.db` exists, byte size == the DB's size measured immediately before the copy | `ls -l` both; the house `pre-<slug>-<ts>.db` convention (529); untracked (`*.db` ignored) |
| M14 | the suite | `80 passed` at forge_lessons HEAD `9dea317` (measured with the pinned interpreter) | the same line, raw, in the evidence file | `/Users/marklehn/Developer/bellows/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider` from the WORKTREE toplevel (⚠️ `python3` on this machine has NO pytest and forge_lessons has NO venv — the interpreter is pinned, and that gap is the provisioning residue the multi-machine sketch names) |
| M15 | DISPOSITION lines | — | **28** in Step 2's dev log | `/usr/bin/grep -cF 'DISPOSITION | entry=' <dev log>` |
| M17 | new-proposal ↔ entry pairing | — | every new proposal's `entry_id` ∈ 406–433, and NO entry in the band carries more than one new proposal | `SELECT entry_id, COUNT(*) FROM lesson_proposals WHERE id > :MAXP GROUP BY entry_id HAVING COUNT(*) > 1` → 0 rows; `SELECT COUNT(*) FROM lesson_proposals WHERE id > :MAXP AND entry_id NOT BETWEEN :MAXE_pre+1 AND :MAXE_post` → 0 (K ≥ 28 is permitted only by proposals that are NOT second proposals for one entry — with M17, K == 28 exactly unless the agent reports why) |
| M16 | duplicates on this batch | **0** (Planner-measured: `detect_duplicates` over the 28 rehearsal ids against `PLANNER_TEMPLATE.md` returned 0) | **0** new `category='duplicate'` proposals | the classifier never assigns `duplicate`; recorded, and asserted as 0 post |

## MUST-PRESERVE

- ⚠️ **BACKUP BEFORE ANY WRITE (M13).** No write to the live DB before the copy exists and its size matches.
- ⚠️ **TRANSACTION-WRAPPED, SENTINEL-GATED ingest:** `BEGIN`; call; PRINT the returned dict; compare to M1 EXACTLY; `COMMIT` only on match; any deviation → `ROLLBACK`, report the measured dict, END THE STEP as blocked — never commit a mismatched ingest, never retry.
- ⚠️ **`insert_proposal` and `ingest_lesson_entries` DO NOT COMMIT.** One commit per step, after all writes; every post-condition on a FRESH read-only connection.
- ⚠️ **`insert_proposal`'s six required positionals are `conn, entry_id, category, suggested_action, reasoning, confidence` — a SEVENTH positional binds to `status`. Pass everything after `confidence` BY KEYWORD (`route=None`).**
- ⚠️ **Worktree discipline:** your cwd IS the claimed tree — never `cd` to the main checkout. Report output is worktree-anchored (`"$(pwd)/reports"`). `git add` by explicit pathspec, never `-A`. Agents do not push.
- ⚠️ **Read the Bellows log yourself? No — Bellows owns the claim; do NOT rename the plan file.**

## Drafting Cycle
**Tier:** T1 computed — T-2 (production-data mutation: the canonical corpus DB) caps at T1; T-8 clone of `Done/executable-556.md` with every pin re-measured on THIS machine and the ingest rehearsed with the real functions.
**Walk register:** /Users/marklehn/Developer/eluvian-governance/governance/knowledge/research/walk-register-forge-cycle-w28-2026-09-01.md
**Walks:** walk 0 = the measured context pin + the three-pass clone-diff against 556 (facts re-pinned: E0/P0/W/update-arm/paths/suite; artefacts: every 556 mechanism counted 1, the pre-declared override replaced by a real suite deposit, 529's backup restored; structure: the 530 three-step split, better for W=28); **walks 1–2 complete** — five lenses each; walk 1 folded 6 (C1–C6: package import, M7 both directions, M17 pairing, hedging-safe receipt, the freeze stated in-plan, three lint-resolution fixes), walk 2 folded 1 record-class (C7: Task A names the import it relies on) and was otherwise dry.
**Direction verdict (after walk 1): PROCEED.** Tested, not judged — six findings, none direction-class; every pin held on re-measurement.
- Weak spots:          w1 2 folded — instruction 2 / record 0; w2 1 folded — instruction 0 / record 1
- Destruction:         w1 dry; w2 dry
- Vulnerabilities:     w1 2 folded — instruction 2 / record 0; w2 dry
- Integration-record:  w1 2 folded — instruction 0 / record 2; w2 dry
- ACID:                w1 dry; w2 dry
**Cold panel: NOT convened, decided with reasoning** — T1; T-8 clone of a plan that closed through its lane on 2026-08-26 with every inherited hazard restated and re-measured here; no direction-class finding; the residual risk sits behind a size-checked backup, a rollback-on-mismatch transaction, and set-identity pins.
**Conformance (§5):** recorded at the freeze from actual runs at the deposit resolution (an unclaimable `lintmirror-` copy inside the watched dir, name proven False by `is_runnable_plan`): plan_lint 0 FAIL — expected WARN set: (o2) ×7 project-relative deposit paths (the 556 form), PIN-CHECK ambiguous ×9 (sha prefixes); walk_register_lint CONFORMANT; cycle_check BAR_MET.
**Closing:** **walk 2 met the bar — instruction-class 0; one record-class fold, all five lenses otherwise dry.** Instruction series **4 → 0**. Receipt BEFORE staging → shop-infra hold (measured class) → release under the CEO's "Go" → claim.

## Cycle Manifest
tier: T1
target: forge_lessons/lessons-forge.db
class: shop-infra
reads: /Users/marklehn/Developer/eluvian-governance/LESSONS.md, /Users/marklehn/Developer/forge_lessons/lessons-forge.db, /Users/marklehn/Developer/forge_lessons/src/lessons_forge.py, /Users/marklehn/Developer/forge_lessons/agents/FORGE_LESSONS_AGENT.md, /Users/marklehn/Developer/forge_lessons/knowledge/decisions/Done/executable-556.md
writes: lessons-forge.db, pre-ingest-2026-09-01-HHMMSS.db, knowledge/development/dev-log-ingest-w28-2026-09-01.md, knowledge/development/dev-log-classify-w28-2026-09-01.md, knowledge/development/evidence-classify-w28-2026-09-01.txt, reports/lessons-report-2026-09-01.md, knowledge/qa/evidence/forge-cycle-w28-2026-09-01/probes-raw.txt, knowledge/qa/evidence/forge-cycle-w28-2026-09-01/full-suite-forge-cycle-w28.txt, knowledge/qa/evidence/forge-cycle-w28-2026-09-01/qa-receipt.md
open_forks: Gate 1 outside this plan — cold non-author = the shop's Remote Control session per the CEO, the four 2026-09-01 proposals carry AUTHOR-CONFLICT for the CEO's own read; Gate 2 codification for whatever Gate 1 accepts. The DB and the backup are untracked by policy (manifest writes name them without annotation — the manifest is comma-split).
walks: 2
yields: 6, 1
validation: cycle_check=BAR_MET, plan_lint=0_FAIL, fold_check=N/A
coherence: N/A

---

## STEP 1 — DEV (ingest; ONE commit; fresh-connection posts)

> **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file. You are the Forge Developer.
>
> **Task A — worktree discipline + dispatch state + pre-flight.** `cd "$(git rev-parse --show-toplevel)" && [ -f src/lessons_forge.py ] && echo TREE_OK` — HALT unless TREE_OK. **Dispatch-state probe** on this step's dev-log path (committed HEAD; working tree; `git log --all -- <path>`), each exit code captured, paired with a positive control against `knowledge/FORWARD.md`; any hit → RESUME (see below); all absent → FRESH. State the determination first. Pre-flight on a READ-ONLY connection to the live DB (`sqlite3.connect("file:/Users/marklehn/Developer/forge_lessons/lessons-forge.db?mode=ro", uri=True)`): M3 (the status histogram, 413 all-terminal), M6 before (405, MAXE captured), M2 (0), M8 (376 parsed from the register path — same package import as Task C; the sha), M12 (3); capture **MAXE** = `SELECT MAX(id) FROM lesson_entries` and **MAXP** = `SELECT MAX(id) FROM lesson_proposals` (⚠️ bind the MEASURED values — a COUNT and a MAX can diverge); capture M5's triple-set and M11's `(id, content_hash)` set to the dev log. Any mismatch → HALT with both values. **RESUME semantics:** M6 already 433 AND M1's flagged pair present in the log → the ingest landed on a prior run: do NOT re-ingest; re-run the posts read-only, record `RESUME (ingest already committed)`, reconstruct the lost in-run values honestly and LABEL them `RECONSTRUCTED (post-commit re-entry)`, never presented as the run's own output; E0 strictly between 405 and 433 → HALT (a single-transaction ingest cannot produce a partial band; a subset is positive evidence of a foreign writer).
>
> **Task B — backup (M13).** `ls -l` the live DB; `cp /Users/marklehn/Developer/forge_lessons/lessons-forge.db /Users/marklehn/Developer/forge_lessons/pre-ingest-2026-09-01-$(date +%H%M%S).db`; `ls -l` the copy; sizes must be equal — record both lines.
>
> **Task C — ONE python script (writing connection; NO commit until the dict matches).** `sys.path.insert(0, os.getcwd())` at the worktree toplevel; `from src.lessons_forge import parse_lessons_md, ingest_lesson_entries, get_unclassified_entries` — the PACKAGE import, the suite's own style (⚠️ `lessons_forge.py` imports `src.paths` inside two functions, so a bare `from lessons_forge import …` with `src/` on the path breaks the moment one of them runs); (1) `entries = parse_lessons_md("/Users/marklehn/Developer/eluvian-governance/LESSONS.md")` → assert `len(entries) == 376`; (2) open the live DB read-write (absolute path), `BEGIN`; (3) `result = ingest_lesson_entries(conn, entries)`; PRINT `result` verbatim; compare to **M1 EXACTLY** — the four counts AND the flagged list as a set of `(entry_id, proposal_id, status)` triples; on match `COMMIT`; on ANY deviation `ROLLBACK`, print `INGEST MISMATCH`, and end the step as blocked; (4) POSTS on a FRESH read-only connection: M6 after (433; the band `SELECT id, entry_date, substr(source_heading,1,72) FROM lesson_entries WHERE id > :MAXE ORDER BY id` — 28 rows, contiguous 406–433, dates 2026-08-26 … 2026-09-01), M2 (28), M3 (413, histogram unchanged), M5 (triple-set SET-IDENTICAL), M11 (the set minus {347, 398} identical; 347 and 398 re-selected — record their new hashes), M12 (3), M8 (sha unchanged).
>
> **Task D — dev log + commit.** `knowledge/development/dev-log-ingest-w28-2026-09-01.md`: the dispatch-state determination, the pre-flight raws (M5 and M11 captures included), the M13 lines, the M1 dict verbatim, the 28-row band listing, the post raws. Commit at the WORKTREE toplevel: `git add knowledge/development/dev-log-ingest-w28-2026-09-01.md && git commit -m "[<id from your plan filename>] forge-cycle-w28(forge-cycle-w28-2026-09-01): ingest 28 (405->433; updated 2 flagged, terminal; proposals 413 unchanged)" -- knowledge/development/dev-log-ingest-w28-2026-09-01.md && git rev-parse HEAD` — the DB and the backup are untracked by policy and are NOT added.
>
> **Deposits:**
> - `knowledge/development/dev-log-ingest-w28-2026-09-01.md`
>
> **Scope:**
> - `knowledge/development/dev-log-ingest-w28-2026-09-01.md`

## STEP 2 — Lessons Agent: classify the 28 (no report, no routing)

> **Step 1's Receipt status must be `Status: Complete`.** Anything else → HALT. **FIRST — post a short visible chat message (1–2 sentences).** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. ⚠️ **Its DB paths are relative and YOU RUN IN A WORKTREE** — every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/forge_lessons/lessons-forge.db`. Open no OTHER database: a 0-byte `.db` anywhere is a decoy returning false absences, and any `.db` outside this repo is a different system's.
>
> **⚠️ NO ROUTING.** `route` stays **NULL** at insert and `status` stays at its default `proposed`. Gate 1 belongs to a non-author. **No ingest, no UPDATE, no delete.** Bind every entry id and heading as a PARAMETER; never interpolate a heading into a `sqlite3` CLI string.
>
> **Dispatch-state probe** on this step's dev-log path (three-place, positive control against `knowledge/FORWARD.md`). RESUME semantics (single-commit design): work list == 28 → a prior dispatch died pre-commit, proceed as FRESH and say so; work list == 0 → classification landed — do NOT re-insert; record `RESUME (classification already committed)`, re-run the posts read-only, deposit, stop; **work list strictly between 0 and 28 → HALT** (positive evidence of a foreign writer).
>
> **Pre-flight (read-only, raw output for each):** `get_unclassified_entries(conn)` == exactly ids 406–433 (28, contiguous) · `SELECT COUNT(*) FROM lesson_proposals WHERE entry_id IN (<the 28 ids, parameter-bound>)` == **0** · **M3 before** (413, histogram) · capture **MAXP** (413 expected — bound, never hard-coded) · **M5** (capture the triple-set — the post-condition compares SET-IDENTITY) · **M6** (433) · **M12** (3). Any mismatch → HALT with measured vs expected.
>
> **Classify.** For each of the 28: parameter-bound `SELECT id, source_heading, raw_content, tags, entry_date FROM lesson_entries WHERE id = ?`; apply the ADR-002 six-value taxonomy per the specialist file (never `duplicate` — M16); then, with `sys.path.insert(0, os.getcwd())` at the worktree toplevel and `from src.lessons_forge import insert_proposal, get_unclassified_entries` (the PACKAGE import), `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, target_layer=<per taxonomy>, target_artifact=<if named>, route=None)` — keyword after `confidence`. Reasoning MUST quote specific text from the entry. ⚠️⚠️ **DISCLOSURE MARKERS — mechanically asserted, not judged.** `[AUTHOR-CONFLICT] ` is DETERMINISTIC: prepended to the reasoning of exactly the entries whose `entry_date = '2026-09-01'` (M7 = 4), no others. `[DEDUP]` and `[REMEDY-GATED]` are CONDITIONAL — apply only where true; their counts are recorded raw and never pinned. **THE DISPOSITION LINE — one per entry, byte-exact prefix:**
> ```
> DISPOSITION | entry=<id> | proposal=<id> | category=<c> | remedy: <one clause> | markers: <those that apply, or NONE>
> ```
> `markers: NONE` is legitimate and expected. Post-condition M15: exactly 28 such lines in the dev log.
>
> **THE COMMIT.** ⚠️⚠️ `insert_proposal` DOES NOT COMMIT. Issue exactly ONE `conn.commit()` after all 28 inserts.
>
> **Post-conditions — ON A FRESH READ-ONLY CONNECTION:** M2 (the inversion — `[]`), M3 after (413 + K, record K), M4 (0), M17 (0 rows / 0), M5 (SET-IDENTICAL), M6 (433), M7 (both directions), M12 (3), M16 (0 new `duplicate`), M8 (sha unchanged).
>
> **Deposit.** `knowledge/development/dev-log-classify-w28-2026-09-01.md` (the determination, pre-flight raws, the 28 DISPOSITION lines, the post raws) and `knowledge/development/evidence-classify-w28-2026-09-01.txt` (the raw SELECT outputs). `git add` both by explicit pathspec; commit `[<id from your plan filename>] forge-cycle-w28: classify 28 — route NULL, 4 author-conflict markers`.
>
> **Deposits:**
> - `knowledge/development/dev-log-classify-w28-2026-09-01.md`
> - `knowledge/development/evidence-classify-w28-2026-09-01.txt`
>
> **Scope:**
> - `knowledge/development/dev-log-classify-w28-2026-09-01.md`
> - `knowledge/development/evidence-classify-w28-2026-09-01.txt`

## STEP 3 — QA (report + probes + suite)

> **Step 2's Receipt status must be `Status: Complete`.** Dispatch-state probe first (three-place, positive control). **FIRST — post a short visible chat message (1–2 sentences).** You are the Forge QA agent.
>
> **MANDATORY — the Rule 20 self-check is gate-enforced** (`rule_20_self_check` greps the QA receipt for the byte-exact banner `Rule 20 — QA Self-Check Results` and the line `PASSED — SELF-CHECK PASSED`). The verification table does NOT satisfy it. ⚠️ The daemon's own prompt names the SHOP's path for the canonical block; on this machine the file is `/Users/marklehn/Developer/eluvian-governance/RULE_20_SELF_CHECK_BLOCK.md` — read THAT file, copy its canonical Python block, fill the four placeholders below, run it, and paste its stdout into the receipt. Before finishing, `/usr/bin/grep -c 'Rule 20 — QA Self-Check Results' <receipt>` must print 1.
> - `plan_slug`: `forge-cycle-w28-2026-09-01`
> - `qa_report_path`: `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/qa-receipt.md`
> - `evidence_dir`: `"$(pwd)/knowledge/qa/evidence/forge-cycle-w28-2026-09-01"` (the QA's OWN worktree — never a main-tree path)
> - `required_evidence_files`: `["probes-raw.txt", "full-suite-forge-cycle-w28.txt"]`
>
> **Item 1 — the report.** `cd "$(git rev-parse --show-toplevel)"`; python: `generate_lessons_report(conn, "2026-09-01", output_dir=os.path.join(os.getcwd(), "reports"))` — `cycle_date` is the PLAN's date, fixed when the batch was assembled (do NOT recompute from `date`); `output_dir` worktree-anchored (⚠️ the 425 trap — NEVER the main-repo path). M9 shasums BEFORE and AFTER, all six byte-identical (recovery `git -C "$(pwd)" checkout -- reports/<file>`); M10 (exists, none of M9). Quote the report's rendering of the new 28-proposal batch in the receipt — that is what Gate 1 reads. Commit: `git add reports/lessons-report-2026-09-01.md && git commit -m "[<id>] forge-cycle-w28: cycle report" -- reports/lessons-report-2026-09-01.md`.
> **Item 2 — DB probes on a FRESH read-only connection**, raw into `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/probes-raw.txt`: M2, M3, M4, M17, M5 (re-selected, SET-IDENTICAL vs Step 2's capture), M6, M7 (both directions), M11 (vs Step 1's capture, with the two named exceptions), M12, M16, M8's sha; M15 counted over Step 2's dev log.
> **Item 3 — the suite (M14).** From the worktree toplevel: `/Users/marklehn/Developer/bellows/.venv/bin/python -m pytest src scripts -q -p no:cacheprovider > knowledge/qa/evidence/forge-cycle-w28-2026-09-01/full-suite-forge-cycle-w28.txt 2>&1; echo "exit=$?" >> <the same file>` — the file must carry the raw `N passed` summary line (80 expected) and the exit code; a failure count > 0 is a Critical finding, not a note.
> **Item 4 — hygiene + receipt** `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/qa-receipt.md`: numstats (Step 1 commit 1 file; Step 2 commit 2 files; report commit 1 file); toplevel; `git reflog -n 5` → 0 amends; the per-item verification table `| Deliverable | Expected | Status (✅/❌) | Evidence |` citing the evidence files by path — ⚠️ the `rule_22_verification` gate substring-matches hedging vocabulary (`pending`, `partial`, `tentative`, `mostly`, …) in positive-status rows: status cells carry the glyph only, and the word `proposed` (a real column value) is the term to use for the new band, never `pending`; the Rule 20 block's stdout. Commit the evidence dir by explicit pathspec: `git add knowledge/qa/evidence/forge-cycle-w28-2026-09-01/ && git commit -m "[<id>] forge-cycle-w28: QA evidence — probes, suite, receipt" -- knowledge/qa/evidence/forge-cycle-w28-2026-09-01/`.
>
> **Deposits:**
> - `reports/lessons-report-2026-09-01.md`
> - `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/full-suite-forge-cycle-w28.txt`
> - `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/qa-receipt.md`
>
> **Scope:**
> - `reports/lessons-report-2026-09-01.md`
> - `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/probes-raw.txt`
> - `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/full-suite-forge-cycle-w28.txt`
> - `knowledge/qa/evidence/forge-cycle-w28-2026-09-01/qa-receipt.md`

Rule 20 banner (byte-exact, produced by RUNNING the canonical block — never hand-authored):

```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
```
