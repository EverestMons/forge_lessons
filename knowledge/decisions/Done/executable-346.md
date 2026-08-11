# Executable: Gate 2 batch 3 — the DRAFTING_CYCLE codification batch (36 proposals): v2.2 → v2.3, then flip all 36 to `implemented` — the batch that DRAINS the Gate-2 queue

**Type:** Executable
**Project:** lessons-forge
**Depends on:** **executable-345** (lessons-forge, Done — the clone origin: the newest same-class Gate-2 batch, closed 2026-08-11 with 2/2 clean gates; the block-insert + all-or-nothing builder mechanism is inherited from it, proven at 37 edits), executable-344 (lessons-forge, Done — the predecessor whose per-vintage timestamp lesson both later batches carry), **executable-326 + executable-342** (lessons-forge, Done — the Gate-1 routing plans: 326 stamped 21 of these rows `2026-08-09T01:20:01Z` (Z-form, GLOB-MATCHING) and 342 stamped 15 rows `2026-08-11T13:42:09+00:00` (offset-form) — both values are pinned prior-value exclusions in G2), DRAFTING_CYCLE.md at v2.2 (precondition, checked at A0)
**Created:** 2026-08-11
**Author:** Planner
**Slug:** `gate2-dc-batch-2026-08-11` (authoring-time; stable across any crash-redo re-deposit — the A0 re-entry key and the Rule 20 `plan_slug`)
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T2
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — verified anew 2026-08-11: no source code changes; lessons-forge has a single test module (`find` over `src/` returned exactly `test_lessons_forge.py`); QA row 7 re-derives the premise; baseline 55 passed / 0 skipped)

⚠️ **ID NOTE — the deposit filename is decided AT DEPOSIT.** Slug+date name form; id read from `id_sequence` at deposit (`next_id` read **346** at authoring — a PREDICTION, not a pin).

---

## Why this exists — the last full batch, and it drains the queue

Thirty-six proposals routed `accepted|codify` with `target_artifact='DRAFTING_CYCLE.md'` are owed codification: **21 routed by the 2026-08-09 gate** (plan 326) and **15 by the 2026-08-11 gate** (plan 342). All 36 are `governance_rule`. ⚠️ **This batch IS the corpus's entire remaining `accepted|codify` floor: PRE and ACC coincide at 36, and a clean run leaves `accepted|codify` = 0 corpus-wide** — the Gate-2 queue opened 2026-08-09 closes with this plan (the §2 rewrite that remains is a rewrite, not a routed batch).

**The shape, cloned from 345 and adapted to a file with no numbered rules:** DRAFTING_CYCLE's units are prose sections with bullet clauses, so the 36 items land as **four section-end bullet blocks** — §2.6 +4, §2.7 +23, §2.8 +4, §3 +5 — **append-only, zero mid-line edits, six anchors total** (four block anchors + version + History). Items whose proposals say "extend clause X" open with "(extends the X clause above)" and sit adjacent in the same section; §6's addressable-unit convention ("add a sub-question to a lens — small, surgical, non-breaking") is exactly this form. Each bullet closes with its proposal citation, so the per-item presence count is a single grep.

**The mechanism is the 345 builder, unchanged in kind:** the plan GIVES the script verbatim (§ APPENDIX A); the agent writes it to a file and runs it. Single read, every anchor count-asserted BEFORE any mutation, all six edits in memory, single write — **an anchor failure anywhere aborts with zero bytes written** (proven again on this batch's dry-run). Re-run after success self-detects (the v2.2 version anchor no longer exists).

**Routing:** the corpus path proper — no §6 deviation. A DRAFTING-CYCLE deviation IS declared in the `## Drafting Cycle` block below (the 344/345 form: §2.0 pin ran; walks did not). ⚠️ One reflexive note, stated because this plan is the first to amend the doctrine that governs its own record's form: every §3 rule this plan must comply with (describe-don't-quote, earned phrasing, the register convention) is unchanged by its own edits — the four blocks ADD clauses and touch none of the rules this plan's Cycle Log is written under.

**Rule-46 splits, named where they occur:** 309's automated WARN-set diff (FORWARD 50) and 313's gate-span regex fix (FORWARD 45) are bellows-owned and NOT built here — each bullet's text names its split inline. **No step of this plan touches any FORWARD register.**

## Scope — one doctrine file, six script-applied edits; one scoped 36-row flip; nothing else

- **Edits exactly ONE existing file:** `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` (root repo), via the GIVEN script. The AFTER text is GIVEN — the agent PLACES it by running the script, never composes.
- **One DB write:** a scoped `UPDATE` flipping the 36 ids `accepted → implemented` at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`.
- **No code edit.** The builder and the two `.sql` files are DATA given verbatim. A script assertion failure is a HALT, never a patch site.
- ⚠️ **§6 coordinate-doctrine-and-gate: NO gate edit owed, discharged BY MEASUREMENT** (2026-08-11): the edits touch §2.6/§2.7/§2.8/§3 prose only — no trigger, no tier, and §4's check set is unchanged. Token sweep of distinctive new-bullet tokens against `plan_lint.py` and `gates.py`: all 0, with ONE classified exception — `not run` (quoted inside the 260 bullet) appears at `gates.py:60` in the Rule-19 hedging-keyword list, **which scans the agent's QA report, not doctrine and not plan text** (precedent: plans 344 and 345 both carried the phrase through clean gates). Re-verified at QA row 8; the QA step's own report must simply never use hedging phrasing, which Rule 19 requires anyway.
- **No LESSONS.md touch. No FORWARD register touch by any step.**
- ⚠️ **DOWNSTREAM EFFECT OF THE FLIP:** `implemented` IS terminal, `accepted` is NOT (`lessons-forge/src/lessons_forge.py:31`). Later edits to the 36 source entries flag rather than stale — intended, verified at QA row 9.
- ⚠️ **THE STALE HAZARD AND THE PREDICATE COINCIDE ON THIS BATCH:** corpus-wide `accepted|codify` = **36** = this plan's own row set. G1 asserts `ACC=36` and `PRE=36`; **either below 36 → HALT** (a smaller ACC is the ingest-stale signature; a smaller PRE means rows left the set). Post-flip expected: **0** — and QA row 6 asserts that zero WITH a positive control, because a zero from a broken query is indistinguishable from the earned one (the doctrine this very batch codifies at 244/261).
- ⚠️ **The doctrine edit lands in the REAL governance root, outside any bellows worktree** — the QA doc-integrity rows are the only guard and fail closed. Absolute operands everywhere. **PLACEMENT is the script; VERIFICATION is Bash-only.**
- ⚠️ **Verdict-window posture:** from the Step-1 commit until close, v2.3 GOVERNS the shop. A HALT holds it live; rollback is a CEO decision.
- **Deposit basenames are DECLARED.** The only live date is G2's in-statement `strftime`.
- ⚠️ **Expected `plan_lint` state at deposit:** recorded in the `## Drafting Cycle` block's Conformance paragraph, measured at the deposit-shaped path. Any WARN or FAIL not named there → do not deposit.

### ⚠️ Environment facts — observed, not predicted

1. `grep` is a ugrep shim: **`-F` for every literal**; a zero-match `grep -c` prints `0` and exits 1 — the printed count is the assertion.
2. Shell state does NOT persist between commands — create and use scratch dirs in the same invocation.
3. zsh aborts on an unmatched glob — use `find`, never a glob.
4. The DB is **gitignored and absent from any worktree** — canonical absolute path only.
5. ⚠️ **THE TWO-VALUE PRIOR-TIMESTAMP EXCLUSION IS LOAD-BEARING, same exposure as batch 2:** the 21 326-written rows carry exactly `2026-08-09T01:20:01Z`, **which MATCHES the Z-GLOB** — the bare GLOB is vacuous on those 21; the 15 342-written rows carry `2026-08-11T13:42:09+00:00`, structurally non-matching. G2's GLOBOK excludes **both** pinned values. (The 344→345 lesson, re-measured on this batch's actual rows rather than inherited.)

---

## The six edits — applied by the GIVEN script, all-or-nothing

**E1 — §2.6 block (+4):** 227 (newest-of-class is a measurement), 254 (diff the parent's FINAL text; check post-writing amendments), 283 (candidacy-narrowing re-trace), 286 (panel aim + residue-battery cadence + metering baseline). Inserted immediately before the §2.7 heading.
**E2 — §2.7 block (+23):** 231, 234, 235, 237, 241, 248, 249, 251, 252, 253, 256, 261, 262, 263, 270, 279, 287, 290, 295, 298, 300, 304, 311 — probe integrity (composed-vs-extracted probes, representation matching, constructed patterns, occurrence-form counts, retraction classification), sweep discipline (site enumeration, claim-level sweeps, premise-correction sweeps, self-flattering-error re-reads), closing-line ordering, population enumeration, tranche calibration, never-pipe, deletion-by-content. Inserted immediately before the §2.8 heading.
**E3 — §2.8 block (+4):** 224 (oscillation's second-reversal tell), 272 (namespaced foreign ids + local ledger rows), 276 (newest-constraint re-check after every fold), 296 (sweep-on-open). Inserted immediately before §2.8's closing paragraph.
**E4 — §3 block (+5):** 260 (unearnable-until-true phrasing, earned WARNs ship unsilenced), 273 (reword only when truer AND legible), 285 (pre-classify the over-match band), 309 (describe gate-keyed values, WARN-set diff after record edits — FORWARD 50 split named), 313 (record sections above the first step heading — FORWARD 45 split named). Inserted after §3's reflexive-prohibition paragraph, before the worked example.
**E5 — version line:** `2.2 (2026-08-11)` → `2.3 (2026-08-11)` within the unique lengthened anchor. ⚠️ The bare old token counts **2** (version + History row); the script's anchor is the full version line. Same-date bump is correct — third amendment today.
**E6 — History row**, prepended as the FIRST bullet, naming all 36 ids by section, the two vintages, the append-only form, and the Rule-46 splits. ⚠️ **Describes, never quotes, the retired version token** (the 344 discipline; QA's 2→1 count depends on it).

**Anchors (every count measured on sha `98c9c255…`, 2026-08-11):** the §2.7 and §2.8 full heading lines (count 1 each, newline-prefixed in the script so insertion is line-start-anchored); §2.8's closing-paragraph line start (`The ledger makes the cross-requirement constraint set`, count 1, newline-prefixed); §3's reflexive-prohibition sentence end (`including to the sentence that warns against quoting them.`, count 1 — append-after); the full version line (count 1); `## History` + newline (count 1).

**Measured deltas [EXECUTED 2026-08-11, dry-run, all six edits]: numstat `42 1`.** Structural integrity measured on the dry-run result: **all 36 proposal citations present** (`*(Proposal NNN, codified 2026-08-11.)*` total = 36); **every bullet verified inside its declared section span** (placement matrix computed: 4/23/4/5 across §2.6/§2.7/§2.8/§3, zero misplacements); all five section headings intact at count 1; §2.8 block precedes its closing paragraph; §3 block precedes the worked example; History bullets 12 → **13**; `2.2 (2026-08-11)` 2 → 1. The appendix script re-extracted from this plan produced a **byte-identical** result to the verified builder (`cmp` clean), and a re-run against the edited file **aborted at the version anchor with zero bytes written**.

---

## Conflict Ledger — run-time constraints

- **C1** — every anchor count-asserted by the script BEFORE mutation; all-or-nothing (single read, all asserts, single write). Line numbers are orientation, never operands.
- **C2** — the version swap is surgical within the unique full-line anchor; the History row describes, never quotes, the retired token.
- **C3** — doctrine committed BEFORE the DB flip.
- **C4** — backup ADJACENT to the flip, states the single write it inverts (the 243 rule §2.7 now carries — this plan complies with the doctrine it ships). A0 state 2 reuse is legitimate; `BK=36` restorability assert mandatory on every path reaching the flip.
- **C5** — flip scoped `WHERE id IN (<the 36>) AND status='accepted'`; `status_updated_by='ceo'`.
- **C6** — `CHANGES=36` AND `GLOBOK=36`, both read before trusting the run; protection is STRUCTURAL (G1's predicate proof + the scoped WHERE).
- **C7** — timestamp in-statement via `strftime`; no shell variable carries it.
- **C8** — capture inside G2's transaction, before the UPDATE. **QA's baseline is the DEPOSITED capture.**
- **C9** — commit path-scoped to exactly `DRAFTING_CYCLE.md`, pathspec ON THE COMMIT, name-only post-assert.
- **C10** — `busy_timeout` set; `database is locked` is a HALT.
- **C11** — post-conditions per edit kind, enumerated in Step 1's table, re-verified independently at QA.
- **C12** — **ORDER:** A0 → A1 → SCRIPT → E0 → DOC_SHA → F → F2 → B → G1 → G2 → G3 → deposits.
- **C13** — the History row asserts the flip in past tense from Task F onward, earned at G2; A0 state 2 completes the F→G2 half-state.
- **C14** — serialized dispatch is a stated assumption; non-dependent guards: A1's pin, E0's porcelain, F2's verify, G1's PRE/ACC, QA rows 1/6.
- **C15** — **the stale-hazard guard: `ACC` ≠ 36 at G1 → HALT before any write.** On this batch ACC and PRE coincide; both are asserted separately because they fail for different reasons (ingest-stale vs rows-left-the-set).
- **C16** — **the 36-id list is an IMMUTABLE INPUT**, stated once in §E2's enumeration and reused verbatim at B/G1/G2/G3/QA. A sentinel mismatch is never resolved by editing it.

---

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

Step 1 (DEV) → verdict gate → Step 2 (QA). `pause_for_verdict: always`. No step renames this file.

⚠️ **HALT ROUTING:** **Step 1 reads** this plan file, the live `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md`, and the canonical DB. **Step 2 reads** this plan file, the Step-1 dev-log, the live doctrine file, the canonical DB (read-only form), the merged Step-1 captures, and `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`. An unreadable deposited capture is a HALT (distinct from the DECLARED FALLBACK at QA row 6).

---
---

## STEP 1 — DEV (write the script, run it, commit, then flip)

---

> **FIRST — post a short visible chat message (1–2 sentences) confirming you are starting this plan.** Do NOT rename this plan file. You are the Developer. ⚠️ **The doctrine edit lands at the ABSOLUTE path `/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` — the real governance root, not your worktree.** If you HALT after the script has run, SAY SO LOUDLY: leave the tree as-is, report the script's output and the doctrine porcelain.
>
> **⚠️ TASK A0 — PRE-EDIT STATE CLASSIFICATION. FIRST match wins:**
> 1. **Flip already done** — all 36 ids read `implemented` (`COUNT(*)` = 36, `-readonly`) → verify the doctrine commit exists (newest log entry naming the slug `gate2-dc-batch-2026-08-11`; missing = REPORTABLE anomaly). Check the crashed run's deposits; a lost `outside-range-ids.txt` is unreconstructible — deposit a RECOVERY dev-log naming what is missing, produce the G3 read-back fresh, state QA row 6 takes its DECLARED FALLBACK. Report complete.
> 2. **Docs committed, flip not done** — newest doctrine commit names the slug AND the 36 read `accepted` → **skip to TASK B, then TASK G.** DOC_SHA from THE COMMIT, never the live file. A `pre-gate2-dc-` backup may exist: rediscover via prefix-only `find`, REUSE, and run the `BK=36` assert either way. Dirty-on-top-of-commit is reported LOUDLY, never swept in.
> 3. **Docs modified-uncommitted** → **HALT.** Sweep the six edits' QA probes against the live file, DEPOSIT the landed/not-landed table at `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/resume-sweep.txt`, report. ⚠️ The script is all-or-nothing, so a PARTIAL signature means a foreign or manual edit — say so.
> 4. **Fresh-with-unexplained-backup** — a `pre-gate2-dc-` backup with no doctrine commit and 36 `accepted` → **HALT.**
> 5. **Fresh** — porcelain clean; live version line reads `2.2`; no `pre-gate2-dc-` backup; `COUNT(*) WHERE id IN (<the 36>) AND status='accepted' AND route='codify' AND target_artifact='DRAFTING_CYCLE.md'` = **36** → proceed to A1.
>
> ⚠️ **Version cross-check on every path:** neither `2.2` nor a `2.3` whose FIRST History bullet names this slug → **HALT.** No-branch-matches → HALT with the full observed triple.
>
> **⚠️ TASK A1 — RE-VERIFY THE AUTHORING PIN.** `shasum -a 256 /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md` must equal
> `98c9c2553b4e87fbd19e82a21a2475c4677fdbacc78dc62818038895565cfa39`
> **Mismatch → HALT.** The per-anchor re-proof is the script's own asserts, executed structurally.
>
> **TASK SCRIPT — WRITE AND RUN THE GIVEN BUILDER.** Write § APPENDIX A's content VERBATIM to `knowledge/development/gate2-dc-edits.py` in your worktree via your file-WRITE tool. Then run:
> `python3 <your-tree-abs>/knowledge/development/gate2-dc-edits.py /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md /Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md`
> Assert: exit 0 and the final line `OK — 6 edits applied: …` naming all six labels. **Any AssertionError → HALT and quote it verbatim — the file is UNTOUCHED by construction; do not edit the script, do not retry with modifications.**
> Then verify post-conditions (C11) via Bash `grep -cF` against the live absolute path:
> | probe | expected |
> |---|---|
> | `*(Proposal 227, codified 2026-08-11.)*` (§2.6 block head) | 1 |
> | `*(Proposal 286, codified 2026-08-11.)*` (§2.6 block tail) | 1 |
> | `*(Proposal 231, codified 2026-08-11.)*` (§2.7 block head) | 1 |
> | `*(Proposal 311, codified 2026-08-11.)*` (§2.7 block tail) | 1 |
> | `*(Proposal 224, codified 2026-08-11.)*` (§2.8 block head) | 1 |
> | `*(Proposal 296, codified 2026-08-11.)*` (§2.8 block tail) | 1 |
> | `*(Proposal 260, codified 2026-08-11.)*` (§3 block head) | 1 |
> | `*(Proposal 313, codified 2026-08-11.)*` (§3 block tail) | 1 |
> | `codified 2026-08-11.)*` (all bullets) | **36** |
> | `### 2.7 Cross-cutting rules (apply within every walk)` | 1 |
> | `### 2.8 Conflict Ledger (keeps cross-lens folds from oscillating)` | 1 |
> | `The ledger makes the cross-requirement constraint set` | 1 |
> | `**Version:** 2.3 (2026-08-11). Amended only through the Iteration Protocol` | 1 |
> | `2.2 (2026-08-11)` | **1** (down from 2) |
> | `gate2-dc-batch-2026-08-11` | ≥1 (History row) |
> | History bullets — `awk '/^## History/{f=1;next} f&&/^## /{f=0} f&&/^- /{n++} END{print n+0}'` | **13** |
>
> **⚠️ TASK E0 — PRE-COMMIT DENYLIST.** Porcelain: expect `DRAFTING_CYCLE.md` modified. **HALT iff any OTHER governance doctrine file is dirty: `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `READONLY_AUDIT_CONTRACT.md`, `SPECIALIST_TEMPLATE.md`, `INTERMEDIATE_DECISION_PHRASES.md`.** Other dirty root files are REPORTED, never a HALT.
>
> **⚠️ TASK DOC_SHA — PIN BEFORE THE COMMIT.** `shasum -a 256` the edited file → **DOC_SHA** in the dev-log.
>
> **TASK F — COMMIT, path-scoped, BEFORE the DB (C3):** `git -C /Users/marklehn/Developer/GitHub add DRAFTING_CYCLE.md && git -C /Users/marklehn/Developer/GitHub commit -m "[<id>] gate2(gate2-dc-batch-2026-08-11): 36 proposals — four section blocks (2.6+4, 2.7+23, 2.8+4, 3+5) — doctrine 2.2 -> 2.3" -- DRAFTING_CYCLE.md`. Record the numstat — expect **`42	1	DRAFTING_CYCLE.md`**; different → HALT. ⚠️ `-C` is load-bearing.
>
> **TASK F2 — POST-COMMIT VERIFY:** commit-content sha == DOC_SHA; name-only lists exactly `DRAFTING_CYCLE.md`. Mismatch → HALT.
>
> **TASK B — BACKUP (C4):** `sqlite3 -bail /Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-gate2-dc-$(date -u +%Y%m%d_%H%M%S).db"` — exit 0, empty stderr; locate via prefix-only `find`. ⚠️⚠️ **RESTORABILITY, EVERY PATH:** `sqlite3 -bail -readonly "<found-backup>" ".timeout 5000" "SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status='accepted';"` → **`BK=36`**. Anything else → HALT before the flip.
>
> **TASK G — THE FLIP.** ⚠️ NO heredocs; `.sql` files via file-WRITE; `-bail` on every invocation, exit-0 + empty-stderr asserted (fresh same-invocation scratch dir outside every git tree). Captures in YOUR tree's evidence dir, `.output` path derived from `pwd`.
>
> **G1 — REHEARSAL (`knowledge/development/gate2-dc-flip-rehearsal.sql`), content exactly:**
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status='accepted' AND route='codify';
> SELECT 'ACC='||COUNT(*) FROM lesson_proposals WHERE status='accepted' AND route='codify';
> SELECT 'MAXID='||MAX(id) FROM lesson_proposals;
> ROLLBACK;
> ```
> Assert **`PRE=36`**, **`ACC=36`** (C15 — either below 36 → HALT; ACC > 36 → in-window routing landed → HALT), **`MAXID=314`** (higher reported-benign; the `id <= 314` bound stays).
>
> **G2 — THE FLIP (`knowledge/development/gate2-dc-flip.sql`), content exactly** (`.output` from `pwd`):
> ```
> BEGIN IMMEDIATE;
> .output <your-tree-abs>/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/outside-range-ids.txt
> SELECT id||'|'||category||'|'||status||'|'||COALESCE(route,'')||'|'||COALESCE(status_updated_at,'')||'|'||COALESCE(status_updated_by,'') FROM lesson_proposals WHERE id <= 314 AND id NOT IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status='accepted';
> SELECT 'CHANGES='||changes();
> SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id IN (224,227,231,234,235,237,241,248,249,251,252,253,254,256,260,261,262,263,270,272,273,276,279,283,285,286,287,290,295,296,298,300,304,309,311,313) AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z' AND status_updated_at NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00');
> COMMIT;
> ```
> ⚠️ **The two-value `NOT IN` is load-bearing (Environment fact 5): the 21 Z-vintage priors MATCH the GLOB.** **Sentinels: `CHANGES=36` and `GLOBOK=36`; either off → HALT with the numbers.** Capture must hold **278 lines** (314 − 36). The line-count assert reads AFTER commit — a mismatch is record-and-HALT with the flip reported as landed, never a re-run. **The 36-id list is IMMUTABLE (C16).**
>
> **G3 — READ-BACK** (`-readonly`): the same 36-id projection `id|status|status_updated_by|status_updated_at ORDER BY id` → deposit RAW as `flip-readback.txt` — all 36 `implemented|ceo|<Z-form>`, none equal to either pinned prior value.
>
> **Output Receipt required** — DOC_SHA, commit hash, numstat pair, PRE/ACC/MAXID/CHANGES/GLOBOK, every file deposited. **End with `### Ledger Updates` and `#### Prompt Feedback`.**
>
> **⚠️ FINAL ACTION — COMMIT YOUR DEPOSITS IN THE WORKTREE** (pathspec on the COMMIT; name-only assert). **`lessons-forge.db` and the backup never staged.**
>
> **Scope:**
> - `knowledge/development/dev-log-gate2-dc-batch-step-1-2026-08-11.md`
> - `knowledge/development/gate2-dc-edits.py`
> - `knowledge/development/gate2-dc-flip-rehearsal.sql`
> - `knowledge/development/gate2-dc-flip.sql`
> - `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/outside-range-ids.txt`
> - `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/flip-readback.txt`
>
> ⚠️ On A0 state 3 ONLY, `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/resume-sweep.txt` joins Scope. The doctrine file is NOT a deposit — committed at Task F, verified at F2.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-gate2-dc-batch-step-1-2026-08-11.md`
> - `lessons-forge/knowledge/development/gate2-dc-edits.py`
> - `lessons-forge/knowledge/development/gate2-dc-flip-rehearsal.sql`
> - `lessons-forge/knowledge/development/gate2-dc-flip.sql`
> - `lessons-forge/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/outside-range-ids.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/flip-readback.txt`

## STEP 2 — QA

---

> **FIRST — Deliverable Verification (Rule 8 / Rule 17).** Dev-log Receipt Complete; every claimed file exists and carries the change. Table: `| Deliverable | Expected | Status (✅/❌) | Evidence |`. Any ❌ → HALT.
>
> **MANDATORY — Rule 20 self-check (canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`).** Fill: `plan_slug`: `gate2-dc-batch-2026-08-11`; `qa_report_path`: `<your-tree-abs>/knowledge/qa/gate2-dc-batch-qa-2026-08-11.md`; `evidence_dir`: `<your-tree-abs>/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/`; `required_evidence_files`: `[doc-integrity.txt, db-invariants.txt, gate-neutrality.txt, pytest_targeted.txt]`. Deposit all four BEFORE running. **Include the literal stdout: the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line, byte-exact (em-dash U+2014).**
>
> ⚠️ **After the verification table, write exactly `## Evidence and Narrative`.** Evidence rule: RAW output. **ONE read-only DB form:** `sqlite3 -bail -readonly "/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db" ".timeout 5000" "<SQL>"`.
>
> **Verification table (HALT on any FAIL; rows 6/7 carry report-not-halt branches).**
>
> **1. DOC INTEGRITY.** Discover the commit independently (newest log entry naming the slug). Three-way sha: commit content == live == DOC_SHA (`e3b0c442…` = "the show failed"). Porcelain EMPTY; name-only exactly `DRAFTING_CYCLE.md`. → `doc-integrity.txt`
> **2. THE FOUR BLOCKS LANDED WHOLE.** Head AND tail bullet of each block → 1 apiece (227/286, 231/311, 224/296, 260/313 — a truncated insertion drops a tail); `grep -cF 'codified 2026-08-11.)*'` → **36**; all five section headings (§2.6, §2.7, §2.8, §3, §4) → 1 apiece; `grep -cF 'The ledger makes the cross-requirement constraint set'` → 1 (the §2.8 closing paragraph survived as the block's lower bound). → `doc-integrity.txt`
> **3. SECTION MEMBERSHIP, RE-DERIVED.** Run exactly: `python3 -c "import io,re;t=io.open('/Users/marklehn/Developer/GitHub/DRAFTING_CYCLE.md',encoding='utf-8').read().split(chr(10));h={};p={};[h.__setitem__(k,i) for i,l in enumerate(t,1) for k in [('h26','### 2.6 '),('h27','### 2.7 '),('h28','### 2.8 '),('h3','## 3. The Cycle Log'),('h4','## 4. The Self-Check')] if l.startswith(k[1]) for k in [k[0]]];[p.setdefault(m.group(1),i) for i,l in enumerate(t,1) for m in [re.search(r'\*\(Proposal (\d+), codified 2026-08-11\.\)\*',l)] if m];import sys;c={'26':0,'27':0,'28':0,'3':0};[c.__setitem__('26' if h['h26']<v<h['h27'] else '27' if h['h27']<v<h['h28'] else '28' if h['h28']<v<h['h3'] else '3' if h['h3']<v<h['h4'] else 'X',c.get('26' if h['h26']<v<h['h27'] else '27' if h['h27']<v<h['h28'] else '28' if h['h28']<v<h['h3'] else '3' if h['h3']<v<h['h4'] else 'X',0)+1) for v in p.values()];print('SECTIONS',c.get('26'),c.get('27'),c.get('28'),c.get('3'),len(p))"` → must print `SECTIONS 4 23 4 5 36`. Any other output → HALT. → `doc-integrity.txt`
> **4. NUMSTAT vs THE PIN.** `git -C /Users/marklehn/Developer/GitHub diff <commit>^ <commit> --numstat -- DRAFTING_CYCLE.md` → exactly `42	1`. → `doc-integrity.txt`
> **5. VERSION + CHANGELOG.** `grep -cF '**Version:** 2.3 (2026-08-11). Amended only through the Iteration Protocol'` → 1; `grep -cF '2.2 (2026-08-11)'` → **1** (the v2.2 History row, intact); the 2.3 row is the FIRST History bullet and names the slug; the prior first row (`- **2.2 (2026-08-11):** slug gate2-s3-register-2026-08-11`) intact immediately below; **tail probe** `grep -cF 'the §2 rewrite (the last queued batch) and every future cycle'` → 1 (measured 0 pre-edit — earnable, whole-row proof); History bullets (pinned awk) → **13**. → `doc-integrity.txt`
> **6. FLIP READ-BACK + THE DRAINED-QUEUE ZERO, WITH POSITIVE CONTROL + BLAST RADIUS.** (a) All 36 ids `implemented|ceo`, Z-GLOB-matching AND `NOT IN ('2026-08-09T01:20:01Z','2026-08-11T13:42:09+00:00')`; exactly 36 rows; `category` preserved per row. (b) `accepted|codify` count → **0** — ⚠️ **paired with a positive control on the same instrument** (the doctrine this batch ships at 244/261: a zero alone is indistinguishable from a broken query): `SELECT COUNT(*) FROM lesson_proposals WHERE status='implemented' AND route='codify'` → **207** (171 measured pre-flip 2026-08-11 + 36; if the live value differs, report the delta with named ids rather than asserting the constant). (c) Re-run the EXACT capture projection, diff against the deposited `outside-range-ids.txt` (278 lines). Partition: (i) any of the 36 in a differing line → HALT; (ii) present-in-capture-absent-now → HALT (deleted row); (iii) all else CONCURRENT ACTIVITY — name each, confirm none is in the 36, do NOT halt. → `db-invariants.txt` ⚠️ **DECLARED FALLBACK (capture lost):** degraded sweep, label `DEGRADED`: `COUNT(*) WHERE id <= 314` → 314; co-stamped sweep on id 224's stamp must include all 36; extra co-stamped ids REPORTED.
> **7. TARGETED TESTS + PREMISE.** `find …/src -name 'test_*.py'` → exactly `test_lessons_forge.py` (second module = report + widen, never HALT). `python3 -m pytest src/test_lessons_forge.py -q` → zero regressions vs 55 passed / 0 skipped (baseline moved → report the delta). → `pytest_targeted.txt`
> **8. GATE-NEUTRALITY WITH POSITIVE CONTROL.** (a) Distinctive new-bullet tokens against BOTH `bellows/scripts/plan_lint.py` and `bellows/gates.py`: `grep -cF 'second reversal'` → 0+0, `grep -cF 'namespaced'` → 0+0, `grep -cF 'over-match band'` → 0+0, `grep -cF 'occurrence form'` → 0+0. (b) ⚠️ **The ONE classified exception:** `grep -nF 'not run' /Users/marklehn/Developer/GitHub/bellows/gates.py` → exactly ONE hit at the Rule-19 hedging-keyword list (`gates.py:60` at authoring — re-derive the line number, don't inherit it); that list scans the agent's QA report, not doctrine — a SECOND hit anywhere, or a hit outside that list, → HALT. (c) POSITIVE CONTROL: `grep -cF 'Drafting Cycle' /Users/marklehn/Developer/GitHub/bellows/scripts/plan_lint.py` → **11**. (d) Zero-match `grep -c` prints 0 and exits 1. → `gate-neutrality.txt`
> **9. CONSUMER SEMANTICS.** (a) Quote `lessons_forge.py:31` verbatim. (b) `get_unclassified_entries` (read-only) → the 36 source entries (216, 219, 223, 226, 227, 229, 233, 240, 241, 243, 244, 245, 246, 248, 252, 253, 254, 255, 262, 264, 265, 268, 271, 275, 277, 278, 279, 282, 287, 288, 290, 292, 296, 301, 303, 305) ALL ABSENT from the work list. Paste raw. → `db-invariants.txt`
> **10. THE DOCTRINE STILL PARSES.** `grep -cE '^## '` → **the pre-edit heading count, unchanged (9, measured 2026-08-11 on both dry-run sides)**; `grep -cE '^### '` → **13, unchanged** (the blocks add only `- ` bullets, no headings). Deviation → HALT. → `doc-integrity.txt`
>
> **Then `## Evidence and Narrative`, then the Output Receipt.**
>
> ⚠️ **`### Ledger Updates`** — Write/Edit-authored, EXACTLY ONCE, `##`-level scope, blank line after the last subsection, one physical line per item.
>
> **`#### Forward Register`: the word `NONE`.** Deliberate non-emission (the FORWARD 45/50 splits are bellows-owned and ride bellows plans; Rule 42 updates are Planner-direct at wrap). A genuinely NEW run-time discovery replaces `NONE`.
>
> **⚠️ FINAL ACTION — COMMIT YOUR DEPOSITS**, pathspec on the COMMIT, name-only assertion. **`lessons-forge.db` never staged.**
>
> **Scope:**
> - `knowledge/qa/gate2-dc-batch-qa-2026-08-11.md`
> - `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/doc-integrity.txt`
> - `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/db-invariants.txt`
> - `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/gate-neutrality.txt`
> - `knowledge/qa/evidence/gate2-dc-batch-2026-08-11/pytest_targeted.txt`
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate2-dc-batch-qa-2026-08-11.md`
> - `lessons-forge/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/doc-integrity.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/db-invariants.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/gate-neutrality.txt`
> - `lessons-forge/knowledge/qa/evidence/gate2-dc-batch-2026-08-11/pytest_targeted.txt`

---

## Drafting Cycle

**Tier:** T2 — trigger fired: T-6 (governance surface: one doctrine file + the proposal corpus). Clone lineage: mechanism cloned from **executable-345** (the newest same-class batch, closed same-day, 2/2 clean gates; block-insert + all-or-nothing builder proven at 37 edits), adapted to a file whose units are prose sections rather than numbered rules — four section-end blocks instead of one, still zero mid-line edits.

**Walks:** ⚠️ **ZERO — the same declared partial DRAFTING-CYCLE deviation as 344/345, same standing CEO direction, recorded with its residue.** One reflexive note: this plan amends the doctrine governing its own record, and its four blocks touch none of the rules this Cycle Log is written under.

**What ran:** §2.0's context pin in full. Walk register committed at `governance/knowledge/research/walk-register-gate2-dc-batch-2026-08-11.md` (root commit `d5243a7`) per v2.2 §3. **Direction verdict: PROCEED** — clone origin confirmed at source (345); edit mechanism proven by executed dry-run (six anchors count-asserted, numstat `42 1`, placement matrix `4/23/4/5 = 36` zero misplacements, appendix byte-equivalence `cmp` clean, re-run abort proven); scope licensing confirmed (36 rows `accepted|codify|DRAFTING_CYCLE.md`, re-verified after 345 moved the floor to 36).

**What the pin caught:**
1. **PRE and ACC coincide at 36 — this batch is the corpus's whole remaining floor**, so the stale-hazard guard and the predicate proof fail for different reasons and are asserted separately; the post-flip zero gets a positive control because the doctrine this very batch ships (244/261) forbids trusting a bare zero.
2. **The timestamp exposure repeats batch 2's, re-measured not inherited:** 21 of 36 prior values MATCH the Z-GLOB; the two-value `NOT IN` carries the guard.
3. **One live gate token found by the sweep:** `not run` (quoted in bullet 260) sits in `gates.py`'s Rule-19 hedging list — classified as no-coupling (the list scans QA reports; 344/345 precedent), with a QA row pinning exactly one hit at that list.
4. **The step-heading hazard designed out at composition:** proposal 313's bullet describes record placement WITHOUT exhibiting a line-start step-heading token — inside this plan's appendix such a literal would parse as a phantom step boundary.

**The cost, recorded:** the same residue class as 345, at similar scale — **no adversarial prose read of the 36 composed bullet texts as doctrine.** The dry-run proves they LAND in the right sections; nothing in this process reads whether they SAY the right thing. Residue by class: (a) no adversarial prose read of the four blocks; (b) no independent QA-table-as-a-system pass; (c) no cold-panel clone-diff against 345/344; (d) §2.8 oscillation untestable (no folds). The standing adversarial-prose-read debt now covers Rules 65–94 AND these 36 bullets — one cold read over both is the efficient discharge.

**Conformance (§5) — last run at the pre-deposit freeze, `plan_lint` → EXIT 0, measured at the deposit-shaped path.** All 8 checks PASS. **THREE warnings stand, each classified:** (1) the missing-per-lens-result-lines warning — the EARNED deviation, DESCRIBED not quoted (the check substring-matches this block); (2) the missing cold-panel-line warning — same class; (3) `(o1)` missing-path on the conditional `resume-sweep.txt` — the lineage's standing known-benign class. The governance walk-register citation resolves (the file is committed before deposit, hash in this block). Any warning outside these classes → do not deposit.

**Closing:** ⚠️ **Does NOT meet §2's doneness bar and does not claim to** — no walk ran; deposited as a declared deviation, residue enumerated. Freeze-time re-verification, all re-derived live: authoring sha `98c9c255…` (= the live v2.2 file, itself byte-identical to 344's verified dry-run), dry-run numstat `42 1`, placement `4/23/4/5`, all head/tail probes earnable (0 pre-edit), `2.2 (2026-08-11)` 2 → 1, History 12 → 13, PRE=36 / ACC=36 / capture=278 / BK=36 measured at source, both prior-value exclusions verified against the actual rows. Fold-and-deposit exactly once.

---

## APPENDIX A — `gate2-dc-edits.py`, the GIVEN builder (write VERBATIM, run once)

```python
#!/usr/bin/env python3
# Gate-2 batch 3 builder - DRAFTING_CYCLE v2.2 -> v2.3.
# All-or-nothing: reads SRC once, asserts every anchor BEFORE any mutation,
# applies all six edits in memory, writes DST once. Assert failure => zero bytes written.
import io, sys

SRC = sys.argv[1]
DST = sys.argv[2]
s = io.open(SRC, encoding='utf-8').read()
edits_applied = []

def rep(old, new, expect=1, label=""):
    global s
    got = s.count(old)
    assert got == expect, f"ANCHOR COUNT {label}: expected {expect}, got {got} for {old[:60]!r}"
    s = s.replace(old, new, expect)
    edits_applied.append(label)

def b(pid, text):
    return f"- {text} *(Proposal {pid}, codified 2026-08-11.)*"

# ---------------- E1: section 2.6 block (4 items), inserted before the 2.7 heading
S26 = "\n".join([
b(227, "**Newest-of-class is a MEASUREMENT, not an assertion.** Before claiming any plan is the newest of its class, sort the shipped set by ship date and name the winner WITH its date, as a measured line in the plan. Measured cost of skipping it: an ACID pass spent a finding rediscovering a hardening a sibling had shipped one day after the claimed newest."),
b(254, "**Diff the parent's FINAL text, and ask whether the parent amended each inherited guard after first writing it** (extends the clone-diff rules above). A clone that rewrites a guard from its purpose imports the parent's ORIGINAL form — measured: a restored guard imported the pre-fold unscoped version of a guard the parent had scoped mid-cycle, and it would have blocked three questions that needed nothing from the missing input. Clone-drift has three depths: guards absent, guards present but unqualified, and corrections reaching some sites but not all."),
b(283, "**After any fold that NARROWS a check's candidacy (filter, exclusion, allowlist), re-trace every cited evidence case through the narrowed spec and confirm each can still fire.** A Why-table citation is a claim about the SHIPPED shape, not the prototype's — re-verify the pairing whenever either side moves. Measured: a check's cited evidence consisted entirely of cases its own new exclusion filtered out — the census's only measured true positives were exactly what the exclusion removed from candidacy."),
b(286, "**Aim panel seats at deletion premises and the clone-diff explicitly — the register's plain lenses under-produce cold.** Run the mechanical residue battery (lint + consistency sweeps) after EVERY culmination, so cold readers hunt novel defects rather than their predecessors' sync debt. Meter every panel and compare against the standing baseline (563k tokens / 45 findings, the first metered run — every HIGH came from the two aimed briefs; the lens-replication seats produced MEDIUM hardening). The seat-brief registry above carries the brief text; this bullet fixes the residue-battery cadence and the metering convention."),
])
H27 = "### 2.7 Cross-cutting rules (apply within every walk)"
rep("\n" + H27, "\n" + S26 + "\n\n" + H27, 1, "E1-s26-block")

# ---------------- E2: section 2.7 block (23 items), inserted before the 2.8 heading
S27 = "\n".join([
b(231, "**Any marker whose practical meaning is 'I did not run this' gets the INHERITED cost test regardless of its spelling** (extends the lens-attestation clause above). A clone that re-imports an identical excuse under a new marker name has laundered it past the rule — apply the test to the meaning, not to the one name the rule happens to use. Measured: a clone quoted the governing rule approvingly and then violated it under a renamed marker."),
b(234, "**Verify a deletion by the absence of the construct's CONTENT (its assertion text, its query), never by the absence of its label; excise the WHOLE SPAN of a multi-line construct** (extends the subtractive-trim clause above). Measured: a check was 'deleted' by removing its label line while the body — a fenced query and three assertions — survived six lines below, and the post-condition asked only whether the label string was gone."),
b(235, "**Budget a cut as an EDIT that will generate findings, not as a subtraction that reduces them.** After removing anything, sweep for references TO it and for captures that just lost their only reader — those are the two mechanical failure modes. Do not preserve numbering to protect references to removed items; measured: every reference that broke was to a deleted row, and the cut produced six dangling cross-references, two orphaned captures, and a stale justification clause."),
b(237, "**Never pipe a command whose exit code carries meaning** (extends the command-output clause above): the shell reports the LAST command's status, so a formatter's success silently replaces the checker's failure. Capture output to a variable or file, then inspect and report the code separately. Measured: four independent readers in one session fell to the same pipe-masked exit code."),
b(241, "**Enumerate every applicable site BEFORE applying a fix anywhere, with sweep weight highest on material written in the SAME SESSION as the fix.** The author who has just formulated a rule is the one least likely to re-scan for other instances — formulating it feels like discharging it. Measured: two same-shape HIGH findings each fixed at one site with the sibling site untouched, the second defect added in the same edit session as the first one's fix."),
b(248, "**A consumer sweep probes for the CLAIM in any phrasing — enumerate the sections that could plausibly hold it; never grep only the string you just edited.** A sweep built from one's own wording confirms only what was edited, and a retraction that specifies a count ('corrected in three places') gives false confidence. Measured: a fifth site held the same claim as a paraphrase the literal probe could not match."),
b(249, "**When a guard's safety depends on a claim about text, EXECUTE the guard's actual matcher — never reason about it — and report which branch fired and what it captured.** Measured: a gate was safe only by the accident of an incidental backtick; reasoning said 'probably fine', and running the real regexes showed one removed character away from capturing prose as a declared deposit list."),
b(251, "**Any probe over a plan that carries retractions must CLASSIFY each hit — instruction or retraction-of-instruction — before reporting.** A well-run cycle deliberately accumulates text of the form 'an earlier form said X — X was wrong', and every such retraction is a literal instance of X. Measured: two of seven probes fired false alarms on retraction text, and one would have been folded unchecked."),
b(252, "**Closing-line ordering: walk → culminate → final ACID → then close, with every count stated AS OF a named completed phase.** A closing line written one phase early is not merely incomplete — it is flattering by precisely the margin the missing phase would have removed. Measured: a fifth owed ACID pass found all three of an early-written closing line's claims defective."),
b(253, "**Anchor every structural search line-anchored, and strip fenced blocks and blockquotes before matching any token that also appears in prose** (companion to the count-is-not-value clause above). A document about a convention QUOTES that convention — decoy density is highest in exactly the files most likely to be measured. Measured: nine prose mentions of a heading token caused four misfired measurements in one session, one landing 251 lines early."),
b(256, "**Ask whether convenient facts make your own argument work before trusting them: re-read populations from the upstream table ROW BY ROW between sections, and diff same-population sites against each other.** A flattering substitution is not random — it is selected by the argument it rescues. Measured: a swap of two entry attributions that made a motivating claim true survived a walk, a culmination, an ACID pass and a second culmination."),
b(261, "**Three probe-integrity clauses from a four-for-four false-absence session:** zsh does not word-split unquoted parameter expansions, so a two-variable probe silently takes the whole string into the first and empties the second — a failure identical in shape to a true negative; a RECORDED relative path rarely resolves against the current repo — resolve each against its OWN project root before declaring the file missing; and a standard written for an agent binds the PLANNER too — verification discipline does not relax at authoring time. Measured: four confident NOT-FOUND lines, all four wrong, all four archived exactly where they should have been."),
b(262, "**A conformance probe must match the artifact's REPRESENTATION (regex, table, computed form), not the spec's prose literals** (companion to the grep -F clause above). Before recording an absence, read the implementation site; the positive control must use the SAME representation as the target. Measured: two panel-critical hardenings looked ABSENT because the spec's literals ship as regexes, and a literal probe cannot see a spec literal implemented as a pattern."),
b(263, "**After any fold, re-verify every factual claim in the fold's OWN text against the post-fold artifact** — counts, presences, behaviours: a fold edits the artifact AND silently invalidates the prose describing the fold. When a fix must reference the hazardous token it removes, reference it by description or measurement, never by exhibiting it; and author-verify a proposed fix by the same method that found the defect. Measured: a delimiter fold's replacement sentence still claimed the glyph occurred 'exactly once' after removing the occurrence it counted — and a cold reader's proposed fix spelled the new delimiter as a glyph, re-planting the bomb."),
b(270, "**A presence check for content that can duplicate INTRA-LINE uses the occurrence form (`grep -Fo | wc -l`), never `-c`** (companion to the count-is-not-value clause). A re-applied in-place tail extension lands both copies on ONE line: every `-c` count still prints 1 and a sha pin then certifies the corruption. Validate the instrument against a CONSTRUCTED failure, not only the success path — the occurrence form prints 2/1/0 across doubled/correct/absent, validated by execution."),
b(279, "**For large classification batches, prefer manifest-pinned tranches over a single saturated step, and carry the per-tranche depth distribution (floor, ceiling, ratio range) as the standing calibration instrument across cycles.** Validated at 3.2× the record batch with no inter-tranche cliff — and the measured risk at that scale was never classification quality but RESUME complexity, where all of the cycle's high-severity drafting findings lived."),
b(287, "**Any population a measurement depends on is enumerated MECHANICALLY (`git log --follow` by path, `SELECT` by key range) — a narrated count is a label, never the filter or the gate.** When two sections of one artifact each state a total over the same population, emit the reconciliation line at authoring; a reader-visible gap without one is a defect. Measured: four of four close-commit drafting-counts disagreed with path enumeration, and the measuring deposit then carried the same class inward (190 declared vs 174 classified, never cross-reconciled)."),
b(290, "**Every constructed or variable pattern is passed via `-e \"$PAT\"` (or after `--`)** (companion to the grep -F clause — '-F is mandatory' does not cover it). A run-time-concatenated pattern beginning with a dash errors as an unrecognized option with NOTHING on stdout. And note the composition trap: two independently-correct hardenings can compose into a failure when one normalizes the symptom of the other."),
b(295, "**For any sweep of a phrase whose fixes cite the original, verify by CLASSIFICATION — list every hit and mark each operative or correction — never by count.** The count never trends to zero: each fold records what it corrected, so the corrected wording survives inside the correction; one measured recount came back HIGHER than before the fold. Zero OPERATIVE hits is the pass condition; the total is meaningless."),
b(298, "**When any premise is corrected, grep the artifact for every guard resting on it and re-justify or remove each one — the correction is not complete at the site where the premise was stated.** An agent that can see through a guard's stated reason steps over the guard: the REASON is what carries authority in practice, because the reason is what an agent weighs when the rule is inconvenient. Measured: a hard read-only guard survived the measurement that falsified its own justification."),
b(300, "**Any claim that a governed text CHANGED — tightened, loosened, added, removed — is established by `git show <old>:<file>` against the live file, never by the changelog row** (applies in §2.6 clone work and here alike). A History row is accurate and directionally silent; a reader supplying the direction supplies the one that fits the story being written. Run one pass over a cycle's own conclusions record at the evidence standard the cycle enforced on its subject. Measured: a published, committed, pushed 'tightened' that one `git show` proved was 'loosened'."),
b(304, "**Before computing from a record, count its DIALECTS — sample the shape, not just the presence.** Make 'unparseable' a REPORTED outcome with the offending line attached, never a skip; ask structural questions with structural probes, not file-level searches. Measured: one corpus carried three record forms; the target field was machine-readable in 0 of 61 logs while a file-level grep reported it present."),
b(311, "**For any absence claim, derive the probe FROM the target text — open the file and copy the string — never compose it from memory.** A zero from a composed probe is a hypothesis; a zero from an extracted probe is evidence. Enumerate what IS there and read it, rather than asserting what is not. Measured: six composed-probe false absences in one session, all on verification steps; five would have licensed a wrong action."),
])
H28 = "### 2.8 Conflict Ledger (keeps cross-lens folds from oscillating)"
rep("\n" + H28, "\n" + S27 + "\n\n" + H28, 1, "E2-s27-block")

# ---------------- E3: section 2.8 block (4 items), inserted before the closing paragraph
S28 = "\n".join([
b(224, "**An enumerating constraint decays as oscillation, and the tell is the SECOND reversal, not the first.** A constraint corrected in one direction and then the other is enumerating, not converging — restate it as the PRINCIPLE the list was approximating rather than improving the enumeration. Measured: a ledger constraint oscillated through three formulations, each individually well-reasoned."),
b(272, "**Foreign constraint and finding ids are ALWAYS namespaced** (`plan-301's C24(a)`, `diag-302's C7`) — and when a fold applies a rule, verify the rule has a LOCAL ledger row: applying an unledgered rule is how a repeatedly-violated constraint stays invisible. Measured: a fold cited a bare id meaning another plan's constraint while the local id was an unrelated premise — the rule actually applied was ledgered nowhere and twice violated."),
b(276, "**After ANY fold, re-check it against the ledger's NEWEST constraints specifically** — the newest are the most breached, because subsequent folds embody habits that predate them. Three same-cycle breaches of freshly-opened constraints is the strongest evidence for pricing MECHANIZATION of a constraint over another prose restatement. Measured: three constraints opened from the very batch being processed, each then violated by a later fold in the same cycle."),
b(296, "**When a constraint is opened mid-cycle, run its check over the WHOLE artifact immediately — as part of opening it, not at the next culmination — and record the sweep result in the constraint row itself.** Opening a constraint feels like closing the class; it is not: it binds what is written after it, and everything already in the artifact is grandfathered in silently. Measured: a non-ASCII-probe constraint opened at walk 1 was violated at two load-bearing pins written BEFORE it existed; twenty lens passes read past them."),
])
TAIL28 = "\nThe ledger makes the cross-requirement constraint set"
rep(TAIL28, "\n" + S28 + "\n" + TAIL28, 1, "E3-s28-block")

# ---------------- E4: section 3 block (5 items), inserted after the reflexive-prohibition paragraph
S3 = "\n".join([
b(260, "**When declaring a tier whose gate you cannot yet satisfy, phrase the status line so it CANNOT match the gate's pattern until the condition is true, and rewrite to canonical form only once earned** (extends the earned-phrasing clause above). An EARNED warning ships unsilenced. Measured: a v0 with zero lens passes returned cleaner gate output than the same file after three walks, because 'not run' contains no fold-token — the gate was silent on the plan with no review and spoke on the one with the most."),
b(273, "**When a gate misreads an HONEST record, read the check's implementation and reword only when the truer statement is also the legible one** — never satisfy a checker with wording the state has not earned; the reword must increase accuracy, not just legibility. Probe-must-match-representation applies to WRITING records, not only reading them. Measured: a dry pass recorded in prose rows the closing-check's regex cannot match kept a WARN alive; recording it per-lens was simultaneously more accurate and checker-legible, and the WARN cleared earned."),
b(285, "**Beside every record a mechanical check reads, state the check's exact matching semantics and the earned-clear condition — and pre-classify the OVER-MATCH band.** A verifier built independently of its target both over-matches (flagging correct records) and under-matches (clearing incorrect ones); a verifier fire is a QUESTION about which side is right, not automatically a defect in the target. Measured: three specimens in one session — a WARN that cleared one phase early, a retraction that tripped a phrase-match by quoting the caught phrase, and a halt check built broader than its exclusion."),
b(309, "**When a record must mention a value a gate keys on, DESCRIBE it rather than reproduce it — including inside corrections and retractions.** After any record edit, re-run the gate and diff the WARN set against its prior state, treating a disappearance as a defect until explained. (The automated WARN-set diff is bellows-owned — FORWARD 50; this is the authoring half.) Measured: a struck token inside a retraction satisfied a negation-stripping check — the edit touched only the record and changed only the gate's verdict."),
b(313, "**Record sections — the Cycle Log and any register material — are placed OUTSIDE every step's span: above the first step heading, never trailing after the last step.** The final QA step's gate span absorbs a trailing record, and the class fired four times in one walk under a rule that already forbade it — when a hazard recurs under a rule that forbids it, measure the recurrence and change the GEOMETRY rather than hardening the wording. (The gate-span regex fix is bellows-owned — FORWARD 45; this is the placement half.)"),
])
ANCH3 = "including to the sentence that warns against quoting them."
rep(ANCH3, ANCH3 + "\n\n" + S3, 1, "E4-s3-block")

# ---------------- E5/E6: version + History ----------------
rep("**Version:** 2.2 (2026-08-11). Amended only through the Iteration Protocol",
    "**Version:** 2.3 (2026-08-11). Amended only through the Iteration Protocol", 1, "E5-version")

HIST = "## History\n"
ROW = ("- **2.3 (2026-08-11):** slug gate2-dc-batch-2026-08-11; Gate-2 codification of 36 proposals — the corpus path proper, no §6 deviation; "
"the largest DRAFTING_CYCLE batch (21 routed by the 2026-08-09 gate via plan 326, 15 by the 2026-08-11 gate via plan 342; all 36 flipped "
"accepted-to-implemented by this plan). Landed as four section-end bullet blocks, append-only, zero mid-line edits: §2.6 +4 (227 newest-of-class "
"as measurement, 254 diff-parent-final-text, 283 candidacy-narrowing re-trace, 286 panel aim/residue-battery cadence/metering baseline); §2.7 +23 "
"(231, 234, 235, 237, 241, 248, 249, 251, 252, 253, 256, 261, 262, 263, 270, 279, 287, 290, 295, 298, 300, 304, 311 — probe integrity, sweep "
"discipline, closing-line ordering, population enumeration, tranche calibration); §2.8 +4 (224 oscillation-tell, 272 namespaced ids, 276 "
"newest-constraint re-check, 296 sweep-on-open); §3 +5 (260 earned-phrasing extension, 273 legible-and-true rewording, 285 over-match "
"pre-classification, 309 describe-not-reproduce with the FORWARD 50 split, 313 record-placement geometry with the FORWARD 45 split). Rule-46 "
"splits stay bellows-owned and are named inline where they occur. §6 coordinate-doctrine-and-gate discharged by measurement: the gate reads "
"plan files, not this doctrine; token sweep against plan_lint.py and gates.py recorded in the shipping plan's QA. Inheritors: the §2 rewrite "
"(the last queued batch) and every future cycle.\n")
rep(HIST, HIST + ROW, 1, "E6-history")

io.open(DST, 'w', encoding='utf-8').write(s)
print(f"OK — {len(edits_applied)} edits applied: {', '.join(edits_applied)}")
```
