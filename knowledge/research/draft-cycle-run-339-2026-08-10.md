# Lessons Forge — Cycle Run 2026-08-10 (ingest + classify the 41-entry session-24→33 batch, classification split across three steps)

**Date:** 2026-08-10 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 41) → Step 2 (classify tranche A) → Step 3 (classify tranche B) → Step 4 (classify tranche C) → Step 5 (DEV — report) → Step 6 (QA) | **qa_steps:** 6 | **pause_for_verdict:** always
**cycle_tier:** T2

## CEO Context

Cycle run only: ingest the 41 un-ingested `LESSONS.md` entries and classify them into proposals. Gate 1 (route disposition) and Gate 2 (codification) are separate plans with CEO decisions between.

**Why this batch, now.** Six FORWARD rows owe amendments to `DRAFTING_CYCLE.md` — 51 (§3 walk-register doctrine/practice divergence), 53 (§2 convergence signal), 50 governance half (§3 retraction silencing a gate token), 45 governance half (§3 gate-span placement), 52 (mandate/observer pairing), 54 (task-paragraph accretion). §6 admits amendments **only through the corpus**, and the corpus was ingested only through 2026-08-07, so every one of the six was outside the amendment path. Three of them had no `LESSONS.md` entry at all; those were written and committed at `ad3c2d7` before this plan was drafted, which is why the batch is 41 and not 38.

**This plan is the enabler, not the amendment.** It routes nothing and codifies nothing. Its output is 41 proposals for Gate 1 to route.

### ⚠️⚠️ CEO DECISION TAKEN (2026-08-10, at authoring): SHAPE (b), carried from plan 311 — ingest as ONE Step-1 transaction, classification SPLIT across THREE steps (~14 each) with verdict gates between, report and QA following.

Carried rather than re-decided, on 311's own measured result: the three-tranche split **held classification quality with no inter-tranche cliff at 3.2× the record batch** (entry 6 of THIS batch is that measurement, and this plan is its first consumer). At 41 the split is well inside the validated range. Consequences the plan must carry, named here rather than discovered:

1. **The created-proposal anchor is created in THREE pieces** — each classification step records its own tranche list; Step 6 reads the union and fails closed if any tranche's list is missing.
2. **The isolation window is FIVE verdict gates wide** — see the inverted G1 below; unlike 311, this window is **not** empty of staleable rows.
3. **Tail-decay instrumentation is per-tranche AND whole-batch** — each classification step reports its ~14 measured reasoning-depth pairs; Step 6 reports all 41 in id order.

⚠️ **`Test Scope: targeted` — the justification is re-verified here, not inherited.** Measured this session: `find . -name "test_*.py"` returns exactly ONE file, `src/test_lessons_forge.py`, so `python3 -m pytest src/` is simultaneously the targeted run and the full run. Rule 21 requires a written justification for `targeted`; this is it. The contract-change carve-out does not fire — this plan changes no code. **`--collect-only` measured 55 tests at authoring** — report the actual. ⚠️ **TRACKING (CEO, 2026-07-31, continued through 288 / 296 / 311): `targeted` on a single-module repo is a precedent under observation; this is the sixth data point.** Falsified by: a defect reaching `Done/` that a broader run would have caught.

**Clone lineage — measured, not recalled.** Direct clone of **311** (`Done/executable-311.md`), which is also the newest same-class plan: the cycle-class set in `Done/` by plan id — 247 → 257 → 274 → 281 → 283 → 288 → 296 → **311**. The newest plan of ANY class on this corpus is **330** (Gate 2, DRAFTING_CYCLE v1.7 → v1.8); its machinery is a different class (doctrine edit, not cycle run), and the diff obligation against it stands for the cold panel.

---

### ⚠️⚠️ INHERITED FACTS FROM 311 THAT ARE FALSE HERE — every one measured 2026-08-10, read-only, against live canonical

**1. ⚠️⚠️ `NT` IS NOT EMPTY. `NT_COUNT = 45`, and 311's central safety premise is VOID.**

311 stated the ingest was *"non-destructive by construction"* because the non-terminal set was empty. It is not empty here, and the composition is the worst available:

| status | route | target_artifact | count |
|---|---|---|---|
| `accepted` | `codify` | `DRAFTING_CYCLE.md` | **21** |
| `accepted` | `codify` | `PLANNER_TEMPLATE.md` | **21** |
| `stale` | — | `PLANNER_TEMPLATE.md` | 3 |

⚠️⚠️ **`accepted` is NOT a member of `_TERMINAL_STATUSES`** — measured as shipped: `frozenset({'implemented', 'superseded', 'rejected', 'reference'})`. The plan-204 guard therefore does **not** protect these 42 rows. The ingest's update path (`src/lessons_forge.py:187-193`) stales any non-terminal proposal whose entry's `content_hash` changed, via `WHERE entry_id=? AND status != 'stale'`.

**The blast radius of a single unexpected hash flip is the entire queued Gate-2 batch — including the 21 `DRAFTING_CYCLE.md` proposals this whole route exists to codify.** The `NT` set spans `entry_id` 93–265, i.e. old entries, so the exposure is to any edit that rewrote LESSONS.md history rather than appended to it.

⚠️ **What makes the run safe is a MEASUREMENT, not a construction: `would-UPDATE = 0`.** That is the property G1 must gate on, and it must be re-measured immediately before the mutation rather than inherited from this table. The three `stale` rows (proposals 98/121/130) are the known plan-204 artifacts, settled at Gate 1 on 2026-07-16 — leave untouched, and do not read their existence as a live defect.

**2. THE BATCH IS 41, AND SIX OF ITS ENTRIES ARE OLDER THAN THE BATCH BOUNDARY.** A date-based count of `LESSONS.md` returns 35 (2026-08-08 → 2026-08-10). The parser returns **41**. The six extra are dated **2026-08-07** and were appended after 311's batch was parser-pinned at 51 — 311's own scope line forbade appending while it was deposited-but-un-run, and these are that prohibition's residue arriving on schedule. **Never derive this batch from a date filter; `get_unclassified_entries()` is authoritative.**

**3. ONE DOCTRINE PIN DID NOT MOVE — 311's all-three-moved pattern is BACK TO 296's.** Measured with `shasum -a 256` against the live working tree at authoring:

| file | pin (authoring, 2026-08-10) | vs 311 |
|---|---|---|
| `DRAFTING_CYCLE.md` (v2.0) | `0964e1a70d6752f8656051b865ebcbdf76cb3e35e1b12415e547b54c45e4a7c7` | **MOVED** (311: `7cc27a3a…`, v1.6) |
| `PLANNER_TEMPLATE.md` | `eb767e3284f1a42b70aec9b3a1ab50226a13276f31f854d4117de26de4815b5f` | **MOVED** (311: `807f6cd9…`, v4.84) |
| `RULE_20_SELF_CHECK_BLOCK.md` | `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0` | **UNCHANGED** (byte-identical to 311's pin) |

⚠️ A clone carrying 311's pins forward would diff two of three — a **partial** mismatch, which is the pattern that reads as a transcription slip rather than as a stale clone. The one capture point (Step 1a-ter stub) and the cite-everywhere structure are carried unchanged.

**4. THE HASH-TRAP SENTINEL IS ENTRY 265.** `content_hash` = `c30fdaff226570c030e544648af0bc6096ff633452795387abada9d00a07fa83`, heading `2026-08-07: A true record invisible to the checker's grammar reads as false — write records in the checker's representation [tag: instrumentation]`. The highest-id entry, named by id so `MAX(id)` moving under a resume cannot retarget it. ⚠️ **Note the asymmetry from 311: entry 265 is no longer the LAST entry in the file** (41 entries follow it), so the trailing-separator trap cannot reach it on this run. It is retained as a **regression** sentinel for `_normalize_for_hash`, not as a live hazard.

**5. THE TAG SET IS TWELVE VALUES, AND FIVE HAVE ZERO CORPUS PRECEDENT.** Measured over the 41 parsed entries against `lesson_entries.tags` with backtick-exact equality:

| tag | batch | prior entries | categories of those priors |
|---|---|---|---|
| `drafting-cycle` | **10** | 6 | `governance_rule` ×6 |
| `verification` | **10** | 14 | `governance_rule` ×14 |
| `process-discipline` | **5** | 2 | ⚠️ **`instrumentation` ×2 — inverts the dominant pattern** |
| `bellows-integration` | 3 | 20 | `governance_rule` ×18, `instrumentation` ×2 |
| `instrumentation` | 3 | 3 | `governance_rule` ×3 |
| `instruction-design` | **3** | **0** | **none** |
| `planner-discipline` | 2 | 94 | `governance_rule` ×80, `duplicate` ×14, `instrumentation` ×1 |
| `drafting` | 1 | 4 | `governance_rule` ×4 |
| `bellows-mechanics` | **1** | **0** | **none** |
| `probe-integrity` | **1** | **0** | **none** |
| `measurement` | **1** | **0** | **none** |
| `mechanization` | **1** | **0** | **none** |

⚠️ **The QA category bound CANNOT be a uniform tag→category map.** Seven entries carry a tag with **no precedent at all**, and `process-discipline`'s only two priors were classified `instrumentation`, not `governance_rule`. Do NOT assert `governance_rule` uniformly; for the precedent-poor set, classify from each entry's substance alone.

**6. FAMILY LINES ARE ABSENT ENTIRELY — 0 of 41.** 311 measured 16 of 51 and instructed per-disposition reporting of what was found. Here **every** placement derivation comes from the body alone. Say so per disposition line; never report a Family line you did not find.

**7. THE EM-DASH ASYMMETRY IS 24-OF-41.** `detect_duplicates` splits headings on the literal SPACE-EM-DASH-SPACE (`_EM_DASH_SEP`, `src/lessons_forge.py:294`), whole-heading fallback when absent. Measured: **24 of 41 headings carry the separator; 17 do NOT** — for those the detector tests the entire dated heading. Report the asymmetry, not a uniform "no hits."

**8. ELEVEN HEADINGS ARE SHELL-HOSTILE** (measured — batch positions 3, 5, 12, 15, 16, 19, 21, 25, 26, 32, 35): apostrophes, a double quote, and literal backticks. Bind headings as query parameters everywhere; never interpolate one into a shell string.

**9. THE BACKUP GLOB POPULATION IS NINE, NOT EIGHT.** `data/backups/lessons-forge-pre-cycle-*.db` matches **9** files at authoring. The count is not the guard; the id token is — this cycle's backup is `lessons-forge-pre-cycle-339-<UTC-stamp>.db` and any resume glob matches on `-339-`. ⚠️ **Derive the date from the actual filename at resume, never from a hardcoded local date** — a `date -u` stamp rolls to the next day after ~18:00 local.

---

### ⚠️⚠️ NUMBERING — THE COLLISION BAND IS 33 NUMERALS WIDE

- **`lesson_entries.id` 266–306** — THIS batch's 41 entries (after ingest).
- **`lesson_proposals.id` 274–314** — THIS batch's 41 proposals (after classification).
- **`lesson_proposals.id` 232–273** — PRE-EXISTING and **NOT terminal**: these are the 42 `accepted|codify` rows of the queued Gate-2 batch. ⚠️ **Leave untouched. They are the rows finding 1 puts at risk.**
- ⚠️⚠️ **EVERY NUMERAL IN 274–306 NAMES BOTH A NEW ENTRY AND A NEW PROPOSAL — both this plan's own, and they are NOT paired.** The pairing is `entry 266+k → proposal 274+k` (offset **+8**), so entry 274 pairs with proposal 282, not proposal 274. **Never write a bare number in 232–314 without its namespace.** Foreign ids are namespaced too: "311's C9", "entry 266", "proposal 274", "FORWARD 53".
- File-position counts are a further namespace: `parse_lessons_md` sees **249** `##` entries in `LESSONS.md`; the corpus row count is **265**. 208 of the 249 parsed match DB rows, and the **57 unmatched DB rows are orphans** from reworded headings, all classified — which is why `get_unclassified_entries()` is `[]` pre-cycle. Measured: NO `## Archived` heading exists, so the parser's archived-stop branch never fires. **249 and 265 are both correct and neither is the other's baseline.**

**Tranche map (expectation, not gate — `get_unclassified_entries` is authoritative at each step):**
- **Tranche A (Step 2):** first 14 of the work list — expected entries 266–279 → proposals 274–287.
- **Tranche B (Step 3):** next 14 — expected entries 280–293 → proposals 288–301.
- **Tranche C (Step 4):** last 13 — expected entries 294–306 → proposals 302–314.

---

### ⚠️ Preconditions measured at authoring (2026-08-10), read-only against live canonical

| what | measured | where re-checked at run time |
|---|---|---|
| **non-terminal set `NT`** | ⚠️ **45** — 42 `accepted\|codify` + 3 `stale` | G1 (pre-ingest; HALTs on composition change) |
| **`would-UPDATE` (the real safety property)** | **0** over 249 parsed | G1 — **HALT on any non-zero**, this is the gate finding 1 turns on |
| whole-corpus dry run through `parse_lessons_md` | **41 would-INGEST / 0 would-UPDATE / 208 unchanged**, over 249 parsed | Step 1a-bis (pre-ingest, HALTs) |
| `stale` count | **3** (proposals 98, 121, 130) | G1 (`STALE_BASE`) |
| `E0` / `P0` | **265 / 273**, `sqlite_sequence` agreement, no gap | Step 1a |
| entry-265 sentinel hash | `c30fdaff…` | Step 1a-bis item 2 |
| status distribution | implemented 171 · superseded 28 · rejected 15 · **accepted 42** · reference 14 · stale 3 (**no `proposed` row — `GROUP BY` omits empty buckets**) | Step 1a baseline; Step 6 |
| `duplicate`-category rows | **19**, all pre-dating this cycle | batch-scoped assertions only (`entry_id > 265`) |
| `get_unclassified_entries()` | **`[]`** pre-cycle | Step 1a |
| `LESSONS.md` provenance | porcelain **EMPTY** after `ad3c2d7` | G2 — HALT on non-empty or non-zero exit |
| root HEAD | `ad3c2d7` — ⚠️ **RECONCILE-NOTE ONLY, NEVER A HALT, EXPECTED TO DIFFER** (deposit commits move it before dispatch) | G2 |
| collected tests | **55** | Step 6 |
| `reports/lessons-report-2026-08-10.md` | **does not exist** | Step 5 pre-check |
| deposited plans of this class | **NONE** — `knowledge/decisions/` holds `Done/` and `halted-executable-334.md` only | deposit-once discipline |
| batch `raw_content` length range | **766–2695 chars** | Step 6 floor sanity |
| backup glob population | **9** files | resume glob (`-339-`) |

⚠️ **Every figure above is the Planner's measurement, not a gate value** (Checklist #29): confirm each against your own read and HALT on a mismatch — **except the root-HEAD row, which is reconcile-only and near-certain to differ by dispatch time.**

**⚠️⚠️ G1 precondition — INVERTED from 311, and this is the plan's single most important guard.** 311 could argue non-destructiveness *by construction* because `NT` was empty. Here `NT = 45` and 42 of those rows are the queued Gate-2 batch. Non-destructiveness therefore rests entirely on `would-UPDATE = 0` — a measurement that can change between authoring and dispatch if anything rewrites `LESSONS.md` history rather than appending to it. **G1 re-runs the dry run and HALTs on any non-zero `would-UPDATE`, naming the affected headings, before the mutation.** A `stale` count above 3 at any later step is the same defect detected late.

---

### The 41 entries — placement scout

**Governing rule: Rule 58 — pre-stated conclusions require verification anchors and equal evidence burden.** Rule 58(2): **this table records where the Planner looked, not a distribution** — a placement absent from it is not rejected; a fourth artifact is a legitimate outcome. Rule 58(3): every disposition carries the same evidence burden; agreeing with the scout is not the low-effort path. No Rule 27 citation — no diagnostic precedes this plan.

⚠️ **Scout depth is declared, not implied (entry 26 of this batch).** Each row was derived from the entry's **heading plus its `How to apply:` clause**, read in full; bodies were not read end-to-end. That is a heading-and-remedy scout, and it is weaker than 311's body-level read. Gate 1 owes each entry a body read before routing.

| # | entry | substance (one line) | scouted `target_artifact` |
|---|---|---|---|
| 1 | 266 | a continue verdict is one bit; a plan reading approval from advancement converts every continue into that approval | `PLANNER_TEMPLATE.md` (halt-with-options authoring) — ⚠️ **Rule 46 split; verdict-channel half is bellows-owned** |
| 2 | 267 | the confirming pass measured composition-clean and literal-dirty in the same pass | `DRAFTING_CYCLE.md` §2/§3 (yield by class) — ⚠️ **cluster (A)**, sibling of entries 306 and 294 |
| 3 | 268 | three constraints opened from the batch's own entries were breached by the folds that followed | `DRAFTING_CYCLE.md` §2.8 — sibling of entry 288 |
| 4 | 269 | `id_sequence` at authoring is a prediction; the verify-at-deposit clause must enumerate every site | `PLANNER_TEMPLATE.md` (deposit discipline) — ⚠️ this plan's own deposit step practices it |
| 5 | 270 | the untargeted confirming pass caught the record's own three-line decay | `DRAFTING_CYCLE.md` §2.7/§3 — ⚠️ **flag (D): v2.0 codified the closing-record re-read and the Cycle-Log-as-covered-region; residue is the sweep-the-tracking-lines clause** |
| 6 | 271 | the three-tranche split held classification quality — no inter-tranche cliff at 3.2× the record batch | ⚠️ likely `reference` (calibration datum) — **this plan is its first consumer**; Gate 1 decides |
| 7 | 272 | a recognized-value enum lives in every tool that reads it — census every copy before adding one | `PLANNER_TEMPLATE.md` (multi-copy census rule) |
| 8 | 273 | argue a trade from the population the change actually touches | `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md` §2.7 — Gate 1 splits |
| 9 | 274 | a truth-restoration edit is held to its own standard in both directions | `PLANNER_TEMPLATE.md` (doc-correction rule) |
| 10 | 275 | a filter can silence its own evidence base — re-check coherence after every narrowing fold | `DRAFTING_CYCLE.md` §2.6 — ⚠️ **flag (D): the evidence-attack brief exists at v1.7; residue is the after-every-fold cadence** |
| 11 | 276 | a specified test fixture can FORCE a guard-weakening | `DRAFTING_CYCLE.md` §2.2 (destruction) or `PLANNER_TEMPLATE.md` (test authoring) |
| 12 | 277 | a checker's mechanics approximate its condition; the gap fires in both directions | `DRAFTING_CYCLE.md` §3 (earned-phrasing clause) — sibling of entry 301 |
| 13 | 278 | panel economics, first metered run — HIGHs come from aimed briefs | `DRAFTING_CYCLE.md` §2.6 — ⚠️ **flag (D): the seat-brief registry landed at v1.7; residue is the residue-battery cadence and the metering convention** |
| 14 | 279 | close-commit counts wrong or absent 4-for-4 — enumerate populations by PATH | `DRAFTING_CYCLE.md` §2.7 |
| 15 | 280 | the shell's cwd resets between calls; cd-first plus a toplevel assert is the whole fix | `PLANNER_TEMPLATE.md` (git-commit mechanics) |
| 16 | 281 | the Bellows verdict grammar is continue/stop only; a redo is a stop plus a corrected re-deposit | `PLANNER_TEMPLATE.md` (verdict-gate authoring) — ⚠️ **Rule 46 split** |
| 17 | 282 | a dash-leading constructed grep pattern parses as an OPTION — exit 2, empty stdout | `DRAFTING_CYCLE.md` §2.7 (beside the `grep -F` clause) |
| 18 | 283 | a nine-element compound instruction dropped exactly one element | `PLANNER_TEMPLATE.md` (per-element QA asserts) — cluster with entries 302 and 306 |
| 19 | 284 | a walk examines the WHOLE artifact, so "no walk has examined this region" is never true | ⚠️ **flag (D), strongest case: v2.0's §2 and §2.7 appear to codify this in full.** Candidate `reference`; measure clause-by-clause at Gate 1 |
| 20 | 285 | an inherited SEVERITY label survives every check that catches an inherited factual claim | `DRAFTING_CYCLE.md` §2.7 or `PLANNER_TEMPLATE.md` — **v2.0 did NOT codify it** |
| 21 | 286 | `plan_lint`'s expected-WARN set is LOCATION-dependent | `DRAFTING_CYCLE.md` §5 (record the exit code *and* the resolution it was taken at) |
| 22 | 287 | a sweep whose fixes quote what they fixed can never be verified by a count reaching zero | `DRAFTING_CYCLE.md` §2.7 (verify by classification, not count) |
| 23 | 288 | a constraint opened mid-cycle is never swept backwards over what already existed | `DRAFTING_CYCLE.md` §2.8 — sibling of entry 268 |
| 24 | 289 | a check that fails a correct run is a check an agent will loosen | `PLANNER_TEMPLATE.md` (derived expectations over constants) — sibling of entry 303 |
| 25 | 290 | a guard's stated REASON is part of the guard — correct the premise and the guard is weakened | `DRAFTING_CYCLE.md` §2.7 |
| 26 | 291 | `LESSONS.md` entries carry no numbers, so an ordinal citation is unverifiable | `PLANNER_TEMPLATE.md` (citation convention) — ⚠️ this plan's scout declares its depth because of this entry |
| 27 | 292 | a changelog says what changed, not which direction — read the diff | `DRAFTING_CYCLE.md` §2.6 (clone-diff) / §2.7 |
| 28 | 293 | folding a defect class in one plan does not immunise the next | ⚠️ **routing principle, not a doctrine clause** — recurrence across artifacts ⇒ mechanization queue. Gate 1 decides |
| 29 | 294 | a restructuring pass resets the convergence curve | `DRAFTING_CYCLE.md` §2/§3 — ⚠️ **cluster (A)** |
| 30 | 295 | a corrected corpus measures the FALSE-positive surface and cannot measure true positives | `PLANNER_TEMPLATE.md` (census authoring) / `DRAFTING_CYCLE.md` §2.7 — sibling of entry 305 |
| 31 | 296 | measure how many DIALECTS a record has before computing anything from it | `DRAFTING_CYCLE.md` §2.7 or `PLANNER_TEMPLATE.md` |
| 32 | 297 | `pause_for_verdict: always` is a header contract nothing enforces | `PLANNER_TEMPLATE.md` (verdict-gate check: steps vs commits vs deposits) — ⚠️ **Rule 46 split; FORWARD 46** |
| 33 | 298 | when a self-marking agent returns a NEGATIVE result, the missing independence matters far less | `PLANNER_TEMPLATE.md` (verdict adjudication) |
| 34 | 299 | a census measuring PRECISION over survivors has not measured the class — RECALL decides a check | `PLANNER_TEMPLATE.md` (diagnostic authoring) / `DRAFTING_CYCLE.md` §2.1 sub-question 1.4 |
| 35 | 300 | a walk's convergence is told by what its findings TOUCH, not where they came from | ⚠️⚠️ **`DRAFTING_CYCLE.md` §2 doneness criterion — cluster (A) CENTERPIECE. FORWARD 53** |
| 36 | 301 | a gate that reads a token can be silenced by the record RETRACTING that token | `DRAFTING_CYCLE.md` §3 — ⚠️ **Rule 46 split; FORWARD 50** |
| 37 | 302 | mandates and their observers drift because they are written in different places | `PLANNER_TEMPLATE.md` (mandate names its QA item inline) — **FORWARD 52** |
| 38 | 303 | a mismatched literal probe returns a confident FALSE ABSENCE, on the verification step | `DRAFTING_CYCLE.md` §2.7 (derive the probe from the target) |
| 39 | 304 | the walk register is doctrine-ephemeral and practice-permanent | ⚠️ **`DRAFTING_CYCLE.md` §3. FORWARD 51** — the baton's NEXT #1 |
| 40 | 305 | a per-string prohibition did not hold a structural hazard; the record must leave the gate span | `DRAFTING_CYCLE.md` §3 (placement convention) — ⚠️ **Rule 46 split; FORWARD 45** |
| 41 | 306 | a task paragraph accretes correct folds until an agent acts on a subset | `PLANNER_TEMPLATE.md` (task authoring as ordered sub-items) — **FORWARD 54** |

**⚠️⚠️ STANDING FLAGS FOR GATE 1 — named so they are decided deliberately, not discovered mid-disposition:**

**(A) THE §2 DONENESS CLUSTER — entries 267, 270, 284, 294, 300 (+ 268/288 adjacent).** All bear on §2's convergence criterion, and FORWARD 53 records that criterion as **self-contradictory**: the same origin-split number is both the bar's convergence condition and the section's own noise-floor signature. Entry 300 is the centerpiece and carries the measured replacement (classify findings by the surface they touch). ⚠️ **Routing these independently would produce several surgical edits to a clause that needs one coherent rewrite.** Recommendation: Gate 1 routes the cluster as one unit.

**(B) THE FORWARD-ROW CLUSTER — entries 300, 301, 302, 304, 305, 306 map one-to-one onto FORWARD rows 53, 50, 52, 51, 45, 54.** These six are the reason this plan exists. ⚠️ **Gate 1 must reconcile each proposal against its FORWARD row rather than routing it fresh**, or the register and the corpus double-count the same owed work and each closes independently of the other.

**(C) RULE 46 CANDIDATES — entries 266, 281, 297, 301, 305.** Each pairs an authoring rule (codify) with a bellows-owned tooling defect (route to the owning register, never codify a workaround). 297 and 301 already have FORWARD rows on the bellows side (46 and 50); 305's bellows half is FORWARD 45.

**(D) PARTIALLY OR FULLY CODIFIED BY v2.0 — entries 270, 275, 278, 284.** Entry 284 is the strongest `reference` candidate; v2.0's §2 and §2.7 read as covering it in full. ⚠️ **The failure mode in both directions: a `reference` routing that discards uncodified residue, and a `codify` routing that re-lands what v1.7/v2.0 already shipped.** Each of the four is measured clause-by-clause at Gate 1, against the live file, by diff — not against the History rows (entry 292 of this batch is exactly that error).

**(E) THE PRECEDENT-POOR TAGS — `instruction-design` (3), `bellows-mechanics` (1), `probe-integrity` (1), `measurement` (1), `mechanization` (1): SEVEN entries whose tag has no corpus precedent at all.** Plus `process-discipline` (5 in batch), whose only two priors were classified `instrumentation`. These twelve classifications set precedent for every future batch and carry the higher reason-sourcing burden.

**(F) THE BATCH DESCRIBES THIS PLAN — entries 269, 271, 291, 306.** Four entries prescribe practices this plan itself executes (deposit-time id re-tokening, the tranche split, citation-by-date-and-fragment, tasks as ordered sub-items). ⚠️ **A classifier that notices this must not soften the classification to match the plan**, and the Planner must not read the plan's conformance as evidence for the proposal.

**Cluster synthesis for Gate 1:** *"41 entries from sessions 24–33 — 10 `drafting-cycle`, 10 `verification`, 5 `process-discipline`, 3 each `bellows-integration` / `instrumentation` / `instruction-design`, 2 `planner-discipline`, and one each of five further tags; a FIVE-entry cluster bearing on a §2 clause its own FORWARD row calls self-contradictory; SIX entries mapping one-to-one onto open FORWARD rows; FIVE Rule 46 splits; FOUR partial-codification measurements; and TWELVE classifications on precedent-poor tags."* Do NOT skip or downgrade any.

**Do NOT dedup against `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, or `RULE_20_SELF_CHECK_BLOCK.md` during classification.** Gate 1 dedups against live doctrine; the flag-(D) measurements are handed to it, not enforced here.

---

### Residual risk register

- **Best verified — the measured baseline.** Every number above was produced this session by running the real code against live canonical, read-only: the 41/0/208 dry run, `E0=265`/`P0=273` with `sqlite_sequence` agreement, `NT_COUNT=45` with its full composition, `_TERMINAL_STATUSES` read as shipped, `STALE_COUNT=3`, `DUP_COUNT=19`, entry-265's hash, the three pins, the 12-value tag distribution with exact-match precedent, the 24/41 em-dash and 0/41 Family asymmetries, 55 collected tests, the status distribution.
- **Least verified — the scout.** Heading-and-remedy depth, declared above. 311's scout was body-level. Gate 1 owes each of the 41 a body read.
- **⚠️ Explicitly NOT verified.** Whether the 41 scouted placements are correct — Gate 1/2's question. Whether classification quality holds across three agents (entry 271 says it did at 51; this is the confirming instance, not the establishing one). Whether the `would-UPDATE = 0` property survives to dispatch — **G1 is the only thing standing between a hash flip and 42 staled proposals**, and that branch has never executed on a non-empty `NT`.
- **The `NT`-non-empty branch is genuinely new machinery.** 311 and 296 both ran with `NT` empty. Every guard in this plan that reasons about the queued Gate-2 batch is unexercised.

**Scope discipline:** cycle run only. Routes stay `NULL` at insert. **Do NOT edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py`, or `bellows/gates.py`.** **Do NOT touch proposals 232–273** (the queued Gate-2 batch — `accepted|codify`, unprotected by `_TERMINAL_STATUSES`). **Do NOT touch proposals 98/121/130** (`stale`, settled 2026-07-16). **⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is parser-pinned at 41, and finding 2 is what that prohibition looks like when it is ignored.

**⚠️ Concurrency — dispatch with NO other lessons-forge cycle in flight.** Detection: the branched staleability checks at the heads of Steps 3–4, the whole-corpus `STALE_COUNT` baseline check at every classification step, and Step 6's reconciliation.

**No diagnostic precedes this plan, deliberately** (247→296→311 lineage practice): every unknown was measured inline against live data at authoring. **✅ `LESSONS.md` is committed and porcelain-clean** — root HEAD `ad3c2d7` at authoring.

**Deposit-once discipline:** to be deposited exactly once (`knowledge/decisions/` enumerated this session; holds `Done/` and `halted-executable-334.md` only). ⚠️ **`339` is the plan id read from `id_sequence` at authoring and it is a PREDICTION (entry 269 of this batch).** Sites carrying it: the title, the backup filename token `-339-`, the dev-log filenames, the report filename, the QA report and evidence directory paths, and the deposit filename. **Re-read `id_sequence` at deposit and re-token all seven site classes before copying in.**

---

## STEP 1 — Lessons Agent (ingest the whole corpus; NO classification in this step)

*(steps to be drafted — this is walk 0, the shape and the measured basis only)*

---

## Drafting Cycle
**Tier:** T1 computed — triggers fired: T-2 (production-data mutation: the corpus write) and T-8 (novel: 311's `NT`-empty premise does not hold, so the ingest's safety machinery is new). **Self-escalated to T2**, stated reason: the ingest's staling path is unprotected for `accepted` rows and its blast radius is the entire queued Gate-2 batch, which includes the 21 proposals this route exists to codify.
**Walks:** 0 — draft v1 not yet walked.
- Weak spots:          not yet run.
- Destruction:         not yet run.
- Vulnerabilities:     not yet run.
- Integration-record:  not yet run.
- ACID:                not yet run.
**Cold panel (T2):** not yet convened.
**Closing:** not reached — draft v1 deposited to the drafting path only, no lens has run.
