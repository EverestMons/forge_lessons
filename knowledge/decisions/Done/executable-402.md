# Executable: Gate-1 routing write for proposals 337–346 — THREE route sets, per the s42sweep packet

**Type:** Executable
**Project:** lessons-forge
**Depends on:** executable-399 (Done — classified the ten, stamps NULL), executable-397 (Done — ingested the batch), `/Users/marklehn/Developer/GitHub/gate1-packet-s42sweep-2026-08-13.md` (the DECIDED block — root `2db9b0e`, owner rider `f6e6b12`)
**Created:** 2026-08-13
**Author:** Planner
**Slug:** `gate1-write-337-346-2026-08-13`
**dispatch_mode:** bellows
**pause_for_verdict:** always
**Priority:** 5
**cycle_tier:** T1
**qa_steps:** 2
**Test Scope:** targeted (Rule 21 — single module, session-verified; QA row 4 re-derives; baseline 55/0)

⚠️ **ID NOTE:** id read at deposit (`next_id` read fresh at the freeze — a PREDICTION, never a mint; the daemon mints at claim).

## Why

Gate 1 for the ten is DECIDED — **CEO instruction "gate 1 as recommended, 342 codify", 2026-08-13, this session, on `gate1-packet-s42sweep-2026-08-13.md` (DECIDED block, root `2db9b0e`)** — reversible on CEO review. **THE STRUCTURAL DELTA FROM THE CLONE ORIGIN (384): three route sets, not one.** 384 wrote a single A-set; this plan writes three, in one transaction, each scoped and separately sentinelled:

| set | proposals | status → | route → | why |
|---|---|---|---|---|
| **I-set** | 337, 338, 339 | `implemented` | **NULL** (declared — see below) | remedy already shipped: 337 → PT v4.88 Rule 85 (plan 389); 338/339 → schema v0.3 + `walk_register_lint` guards (plan 392) |
| **R-set** | 343, 344, 345 | `reference` | `reference` | live doctrine already carries the rule (§2.7 proposal-253 / 311 / count-in-prose bullets, each grep-verified present ×1) |
| **A-set** | 340, 341, 342, 346 | `accepted` | `codify` | measured-uncovered; becomes the Gate-2 queue of four |

**⚠️ The I-set's NULL route is a DECLARED choice, not an omission.** The corpus carries both forms — `implemented|codify` **185 rows** and `implemented|NULL` **89 rows** (measured 2026-08-13). `codify` would assert these three passed through codification, which is FALSE: their remedies shipped BEFORE the proposals existed, so Gate 1 never routed them to a Gate-2 plan. NULL is the honest record and has 89 precedents; the shipped-remedy evidence lives in each row's existing `reasoning`/`suggested_action` text (written by 399's classifier, untouched here). **A future reader must not read `implemented|NULL` as un-routed** — this plan's dev-log Receipt is the routing record for those three.

**R-set route is `reference`, NOT `backlog`** — the corpus splits `reference` status 9 `reference` / 6 `backlog` (measured); `backlog` marks deferred WORK, and nothing here is deferred: the rule already exists and these are instances of it.

⚠️ **Sentinel posture — the cleanest case, RE-MEASURED not inherited: all ten prior stamps are NULL** (399's classifier set `proposed_at` only; `status_updated_by` and `status_updated_at` both NULL per id, measured 2026-08-13), so `status_updated_at IS NOT NULL` via the bare Z-GLOB is a complete value guard **with no prior-value exclusion needed** — the four-timestamp-forms trap cannot fire here. The GLOB must be proven to match the representation the UPDATE writes; the rehearsal below does that on a scratch copy.

⚠️ **This plan APPLIES proposal 341's own rule before 341 is codified:** every in-transaction sentinel prints BEFORE the COMMIT, so a rollback run emits perfect evidence with nothing written. **Task E-c's post-COMMIT read-back from a FRESH connection is therefore this plan's ONLY proof of durability**, and it is asserted, not merely logged. Stated here because the plan routing that lesson should not be the plan that ignores it.

**Post-write expected corpus (every number measured 2026-08-13, live, and re-derived by arithmetic the QA re-runs):** `proposed` **0** · `accepted|codify` **4** (the new Gate-2 queue: 340/341/342/346) · `implemented` **278** (275 + 3) · `reference` STATUS **18** (15 + 3), route split **12 `reference` + 6 `backlog`** (9 + 3; the six pre-existing backlog ids 161/169/291/294/299/301 are untouched) · `rejected` 15 · `stale` 3 (98/121/130) · `superseded` 28 · total **346** (no row created or deleted — this plan only UPDATEs).

**Dedup posture:** the packet's per-proposal grep evidence is the authority and A0 re-reads it live; **licence to disagree granted — a mismatch HALTs and the CEO re-decides**, never a silent re-route.

## Scope

- **One DB write session, THREE scoped UPDATEs in ONE transaction** at the canonical absolute path; `status_updated_by='ceo'` (the Gate-1 authority, lineage convention). No doctrine touch, no `LESSONS.md` touch, no FORWARD touch by any step (receipts say `NONE`).
- Env facts: the standing four (ugrep `-F` + zero-count exit-1, the printed count is the assertion; same-invocation state only; `find` never glob; canonical ABSOLUTE DB path — a bare relative name CREATES an empty file).

**Scope paths:**
- `knowledge/development/gate1-write-s42-dev-2026-08-13.md`
- `knowledge/development/g1-s42-route.sql`
- `knowledge/qa/evidence/gate1-write-337-346-2026-08-13/flip-capture.txt`
- `knowledge/qa/gate1-write-s42-qa-2026-08-13.md`
- `knowledge/qa/evidence/gate1-write-337-346-2026-08-13/probes-raw.txt`

*(The `pre-g1s42-*.db` backup lands at the lessons-forge root, gitignored — an untracked artifact, named in the dev note.)*

## Conflict Ledger

- **C1 — three UPDATEs, ONE transaction, each compare-and-swap scoped:** `id IN (…) AND status='proposed'`. A partial apply is impossible; a re-run is a no-op by the status predicate. *(observer: QA Item 2)*
- **C2 — sentinels BY NAME, counted:** PRE=10, BK=10, CH_I=3, CH_R=3, CH_A=4, CH_TOT=10, GLOBOK=10, PROP_POST=0, ACC_POST=4, IMPL_POST=278, REF_POST=18, TOT=346 — **twelve**, each asserted. *(observer: QA Item 5)*
- **C3 — durability is proven ONLY post-COMMIT** (the 341 rule): E-c re-opens a FRESH read-only connection and asserts all ten rows; any mismatch → HALT loudly, name the backup, do NOT re-run the UPDATE. *(observer: QA Item 5)*
- **C4 — the capture is a Deposit and must be committed** (an uncommitted deposit fails the gate; 386's S1-1 class). *(observer: QA Item 1)*
- **C5 — one action per ops compound with a post-condition close** (PT v4.88 Rule 85 — and proposal 337's own subject): backup, flip, read-back, and each commit are separate compounds, every one opening cd-absolute and closing on its own verification; no `--amend`. *(observer: QA Item 3)*
- **C6 — nothing outside the ten is touched:** the capture SELECT covers `id <= 336` and proves it by diff. *(observer: QA Item 5)*

## Freeze checklist (deposit path — items 1–4 BEFORE the copy, item 5 immediately AFTER)

1. Substitute the read id at the bootstrap `<id>` site; probe in OCCURRENCE form (`grep -oF -- '<id' <deposit-path> | wc -l`), and **derive the expected count by RUNNING the probe against the draft at the freeze — never from this sentence** (the 392 SC-1 class: a probe value written from prediction halts a correct run).
2. **Diff the draft against the mirror immediately before the copy** — an empty diff is the deposit precondition.
3. Final `plan_lint` at the FAITHFUL scratchpad mirror (NEVER the real `decisions/` — the daemon claims AND DISPATCHES same-second, proven live three times this session) — WARN set matches the Conformance paragraph.
4. A0-fresh re-check: all ten still `proposed` with NULL stamps; `accepted` still 0.
5. Post-copy, same minute: `ls` the real `decisions/` — the claim reads `in-progress-executable-<READ-ID>.md` with the item-1 id (mismatch = foreign in-window consumption — report, never re-copy).

---

## How to Run This Plan

**Bootstrap:**
```
Read the plan at knowledge/decisions/in-progress-executable-<id>.md (the daemon renames on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation.
```

---

## STEP 1 — DEV (the routing write)

> **FIRST — post a short visible chat message (1-2 sentences).** Do NOT rename the plan file. Own working tree; canonical DB by ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (`forge/forge.db` is a different database — never open it).
>
> **Task A0 — branches, catch-all LAST.**
> **(1) STATE:** `sqlite3 -readonly <abs> "SELECT id||'|'||status||'|'||COALESCE(route,'NULL')||'|'||COALESCE(status_updated_at,'NULL') FROM lesson_proposals WHERE id BETWEEN 337 AND 346 ORDER BY id;"` — ten rows.
> **(2) CLEANLINESS:** `git status --porcelain -- knowledge/development/gate1-write-s42-dev-2026-08-13.md knowledge/development/g1-s42-route.sql` empty.
> **(3) RE-ENTRY key:** `git log --oneline -1 -- knowledge/development/g1-s42-route.sql` — subject carries this plan's slug?
> - **FRESH** = all ten read `proposed|NULL|NULL` AND (2) empty AND (3) no → Task B.
> - **RE-ENTRY (write landed)** = (3) yes AND the ten read their target values → run Task E-c's read-back fresh, complete any uncommitted deposit for exactly the Scope paths, report complete. Do NOT re-run the UPDATE.
> - **NONE-MATCH** = anything else — including ANY row not `proposed`, any non-NULL stamp, or a route already set → **HALT quoting every row.** (With `accepted` measured 0 at authoring, a routed row means in-window foreign routing.)
>
> **Task B — backup (its own compound, closing on its own verification).** `mkdir -p` the evidence dir `knowledge/qa/evidence/gate1-write-337-346-2026-08-13` FIRST (nothing earlier creates it; the `.output` target needs it — ⚠️ ABSOLUTE path, no `<tree-abs>` placeholder). **A `pre-g1s42-*` backup already on the lessons-forge root → REUSE via prefix-only `find`, never a second; >1 match → HALT.** Otherwise: `sqlite3 -bail <canonical-abs> ".timeout 5000" ".backup /Users/marklehn/Developer/GitHub/lessons-forge/pre-g1s42-$(date -u +%Y%m%d_%H%M%S).db"`; then SEPARATELY assert against the backup with `?immutable=1` (never `?mode=ro` — sidecars absent): `SELECT 'BK='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 337 AND 346 AND status='proposed';` → **BK=10**; else HALT.
>
> **Task C — live pre-flight, ROLLBACK-guarded, BEFORE any write:** `sqlite3 -bail <canonical-abs> ".timeout 5000" "BEGIN IMMEDIATE; SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 337 AND 346 AND status='proposed' AND route IS NULL AND status_updated_at IS NULL; SELECT 'ACC0='||COUNT(*) FROM lesson_proposals WHERE status='accepted'; SELECT 'TOT0='||COUNT(*) FROM lesson_proposals; ROLLBACK;"` → assert **PRE=10, ACC0=0, TOT0=346**; any off → HALT with the per-id read, NOTHING written.
>
> **Task D — the write** (file `knowledge/development/g1-s42-route.sql`, exactly; runner `sqlite3 -bail <canonical-abs> ".timeout 5000" ".read <abs>"`, exit 0 + empty stderr):
> ```
> BEGIN IMMEDIATE;
> SELECT 'PRE='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 337 AND 346 AND status='proposed';
> .output /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/qa/evidence/gate1-write-337-346-2026-08-13/flip-capture.txt
> SELECT id||'|'||status||'|'||COALESCE(route,'')||'|'||category||'|'||COALESCE(status_updated_by,'')||'|'||COALESCE(status_updated_at,'') FROM lesson_proposals WHERE id <= 336 ORDER BY id;
> .output stdout
> UPDATE lesson_proposals SET status='implemented', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (337,338,339) AND status='proposed';
> SELECT 'CH_I='||changes();
> UPDATE lesson_proposals SET status='reference', route='reference', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (343,344,345) AND status='proposed';
> SELECT 'CH_R='||changes();
> UPDATE lesson_proposals SET status='accepted', route='codify', status_updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), status_updated_by='ceo' WHERE id IN (340,341,342,346) AND status='proposed';
> SELECT 'CH_A='||changes();
> SELECT 'GLOBOK='||COUNT(*) FROM lesson_proposals WHERE id BETWEEN 337 AND 346 AND status_updated_at GLOB '20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z';
> SELECT 'PROP_POST='||COUNT(*) FROM lesson_proposals WHERE status='proposed';
> SELECT 'ACC_POST='||COUNT(*) FROM lesson_proposals WHERE status='accepted';
> SELECT 'IMPL_POST='||COUNT(*) FROM lesson_proposals WHERE status='implemented';
> SELECT 'REF_POST='||COUNT(*) FROM lesson_proposals WHERE status='reference';
> SELECT 'TOT='||COUNT(*) FROM lesson_proposals;
> COMMIT;
> ```
> Assert **PRE=10, CH_I=3, CH_R=3, CH_A=4, GLOBOK=10, PROP_POST=0, ACC_POST=4, IMPL_POST=278, REF_POST=18, TOT=346**; capture **336 lines**. ⚠️⚠️ **Every sentinel above prints BEFORE the COMMIT executes — a rollback-instead-of-commit run produces perfect sentinels and a full capture with NOTHING written. Task E is therefore the ONLY proof of durability** (this is proposal 341's own rule, applied before it is codified).
> **Rehearse first on a scratch COPY** (`cp` the canonical DB to `<scratch>/`, run the identical `.read`, confirm all twelve sentinels and that GLOBOK matches the representation the UPDATE writes) — a rehearsal mismatch HALTs before any live write.
>
> **Task E — post-COMMIT read-back, FRESH invocation, ASSERTED (C3):** `sqlite3 -bail -readonly <canonical-abs> ".timeout 5000" "SELECT id||'|'||status||'|'||COALESCE(route,'NULL')||'|'||status_updated_by||'|'||status_updated_at FROM lesson_proposals WHERE id BETWEEN 337 AND 346 ORDER BY id;"` → **337/338/339 read `implemented|NULL|ceo|<Z-stamp>`; 343/344/345 read `reference|reference|ceo|<Z-stamp>`; 340/341/342/346 read `accepted|codify|ceo|<Z-stamp>`**; any other read → **HALT loudly (the COMMIT did not land — do NOT re-run the write; name the backup)**.
>
> **Task F — dev note + commit.** Write `knowledge/development/gate1-write-s42-dev-2026-08-13.md`: the A0 determination, the backup path, every sentinel raw, the read-back raw, the capture line count, and a `#### Routing record` section naming all three sets with their justification (**the I-set's NULL route explained — this section IS the routing record for 337/338/339**). Commit (ONE compound, cd-first to your tree root, no amend) the dev note + `g1-s42-route.sql` + the capture; then in a SEPARATE compound verify `git show --name-only --format= HEAD` lists exactly those three and `git rev-parse --show-toplevel`. `#### Prompt Feedback` in `### Ledger Updates`. `#### Forward Register`: `NONE`. Then STOP.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate1-write-s42-dev-2026-08-13.md`
> - `lessons-forge/knowledge/development/g1-s42-route.sql`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-337-346-2026-08-13/flip-capture.txt`
>
> **Scope:**
> - `knowledge/development/gate1-write-s42-dev-2026-08-13.md`
> - `knowledge/development/g1-s42-route.sql`
> - `knowledge/qa/evidence/gate1-write-337-346-2026-08-13/flip-capture.txt`

---

## STEP 2 — QA

> ⚠️⚠️ **PRECONDITION — Step 1 ran as its own dispatch:** `git log --oneline -1 -- knowledge/development/g1-s42-route.sql` names the Step-1 commit, made before this step began and not by this context. Otherwise mark the independence gap plainly. **No Monitor anywhere in this step; every command foreground.** DB read-only (`?mode=ro`, absolute path). **Verification only — a FAIL is reported, never repaired.**
>
> **(A) Rule 20 self-check block** — the canonical block from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (read live). Canonical header `Rule 20 — QA Self-Check Results`; on full pass the canonical line `PASSED — SELF-CHECK PASSED`. `required_evidence_files` = the evidence-directory subset of `## Scope`.
>
> **(B) Verification table** (`| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |`) — run ALL rows before halting:
> 1. **Deliverables (Rule 17)** — each Step-1 deposit: `git log --oneline -1 -- <path>` non-empty AND `git status --porcelain -- <path>` clean with the exit echoed (C4: the capture is a deposit).
> 2. **The three sets landed, exactly** — per id 337–346: status/route/actor/stamp against the Step-1 target values (the three-set table in this plan is the authority); every stamp Z-form by GLOB; `status_updated_by='ceo'` on all ten. → `probes-raw.txt`
> 3. **C5 commit shape** — the Step-1 commits are single non-amend commits (one parent each); toplevel printed; name-only lists exactly the deposited paths.
> 4. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail; value cell `<N> passed` only (baseline 55 passed at authoring; a delta is reported, never asserted).
> 5. **Corpus invariants (C2/C6)** — `proposed` **0**, `accepted` **4** (exactly 340/341/342/346, named), `implemented` **278**, `reference` **18** with route split **12 reference + 6 backlog** (the six backlog ids 161/169/291/294/299/301 named and unchanged), `rejected` 15, `stale` 3 (98/121/130), `superseded` 28, total **346**; entries still **338**; **re-run the EXACT capture SELECT (copy from `g1-s42-route.sql`, never re-type) and diff against the deposited 336-line `flip-capture.txt`** — any delta partitioned (impossible-id → FAIL; deleted-row → FAIL; else concurrent, named). → `probes-raw.txt`
> 6. **Routing-record completeness** — Step 1's dev note carries the `#### Routing record` section naming all three sets, **including the I-set NULL-route justification** (grep the committed file; missing = ❌, because `implemented|NULL` is otherwise indistinguishable from an un-routed row).
> 7. **Register posture** — lessons-forge `decisions/` non-Done contents: this plan's own `in-progress-*` file ONLY (other repos out of scope); `knowledge/FORWARD.md` unchanged at **18** pipe-lines by `grep -c "^| "` (any new row is a finding: a `NONE.`-item row = a regression of plan 376's guard, a real-text row = foreign writer).
> 8. **Raw output throughout.**
>
> `## Evidence and Narrative` · Receipt · `### Ledger Updates` · `#### Prompt Feedback` · `#### Forward Register`: `NONE`. **FINAL ACTION** — commit the receipt + raw file (cd-first, pathspec exactly them, no amend), then STOP.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate1-write-s42-qa-2026-08-13.md`
> - `lessons-forge/knowledge/qa/evidence/gate1-write-337-346-2026-08-13/probes-raw.txt`
>
> **Scope:**
> - `knowledge/qa/gate1-write-s42-qa-2026-08-13.md`
> - `knowledge/qa/evidence/gate1-write-337-346-2026-08-13/probes-raw.txt`

---

## Drafting Cycle

**Tier:** T1 — production-data mutation (T-2) on a shared store; structure-for-structure clone of shipped 384 keeps T-8 silent; no T-5/T-6 surface (no doctrine file is touched).

**Walk register:** `governance/knowledge/research/walk-register-gate1-write-337-346-2026-08-13.md` (schema 0.3), committed per phase.

**Walk 0 (context pin, measured 2026-08-13 read-only):** the ten read `proposed|NULL|NULL|NULL` per id (status/route/actor/stamp — the cleanest sentinel case, no prior-value exclusion owed); `accepted` 0; totals proposals 346 / entries 338; route conventions measured whole-corpus (`implemented|codify` 185, `implemented|NULL` **89** — the I-set precedent; `reference|reference` 9, `reference|backlog` 6 with ids 161/169/291/294/299/301); post-write arithmetic derived (278/18/4/0/346); targeted suite 55 passed; packet DECIDED block committed at `2db9b0e` with the owner rider at `f6e6b12`. **Newest-of-class, MEASURED not asserted (proposal 227's rule):** the Gate-1-write class sorted by ship date is 330 (2026-08-09) → 350 (2026-08-11) → 362 (2026-08-12) → **384 (2026-08-13)** — 384 is BOTH the clone origin and the newest same-class, named with its date. **Clone-diff vs 384:** the single A-set becomes THREE sets (three UPDATEs, one transaction, three `changes()` sentinels plus a total — 384's single `CHANGES_F` would have under-observed a partial apply); the I-set's NULL-route choice is NEW and declared with its 89-row precedent; the R-set's `reference`-not-`backlog` choice is NEW and declared; 384's prior-stamp analysis carried with its premise RE-MEASURED true (all NULL); the rehearsal-on-scratch-copy and post-COMMIT read-back carried and strengthened (the read-back is now named as the ONLY durability proof, per proposal 341 which this very plan routes). **Scout: DECLINED** — T1, proven-clone shape, single transaction; recorded per §2.0.

**Walks (2 warm):**
- Weak spots:          w1 1 folded — instruction: the freeze's occurrence-probe count was first written as a literal; replaced with a derive-at-the-freeze instruction (the 392 SC-1 class — a predicted probe value halts a correct run); w2 dry.
- Destruction:         w1 dry — every UPDATE is CAS-scoped on `status='proposed'`, so a re-run is a no-op and no pre-existing row (id ≤ 336) is reachable; the capture proves the untouched set by diff.
- Vulnerabilities:     w1 dry — the GLOB is proven against the representation the UPDATE writes by the scratch rehearsal, not by reasoning; `?immutable=1` for backup reads; absolute DB path everywhere (a relative name creates an empty file).
- Integration-record:  w1 dry — Deposits project-prefixed with Scope repo-relative per the lessons-forge convention (the path-FORM check applied deliberately); the packet's DECIDED block is cited by commit hash, not by recollection.
- ACID:                w1 dry — one transaction, so atomicity is structural; the backup is the durability floor and the post-COMMIT read-back the durability PROOF; the A0 arms cover every half-state.

**Splits: w1 instruction 1 / record 0 · w2 all five lenses dry.** The bar is met at walk 2 with nothing restructured.

**Conformance (§5):** faithful-mirror `plan_lint` at the deposit-shaped scratchpad mirror — NEVER the real `decisions/`. First run surfaced two WARNs: (k) the clone-framed plan not naming its newest same-class comparison — a REAL finding, folded by measuring the class by ship date (330→350→362→384) and naming 384 with its date; and one (o1) missing-path advisory. **Expected WARN set at deposit: exactly ONE (o1) line for `knowledge/qa/evidence/gate1-write-337-346-2026-08-13` — pre-classified and CORRECT: Step 1 Task B creates that directory, so it cannot exist at lint time.** Final run: **EXIT 0, that one advisory only**; (q) telemetry — no file-backed pins in this plan (the DB values are not file digests), so no PIN-CHECK line is owed. Re-run at the freeze (item 3).

**Closing:** walk 2 read dry on every lens — **instruction 0 / record 1: this Cycle-Log fill itself, written at close with measured content** (0 of 1 fold-introduced — the fill is the close's own act, named per §2's bar); closing-record re-read run against the filled block; clone-diff at walk 0 per §2.0; scout declined with reasoning; fold-and-deposit exactly once.
