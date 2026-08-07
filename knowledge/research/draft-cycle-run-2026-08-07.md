# Lessons Forge — Cycle Run 2026-08-07 (ingest + classify the 51-entry session-18→24 batch, classification split across three steps)

**Date:** 2026-08-07 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 51) → Step 2 (classify tranche A) → Step 3 (classify tranche B) → Step 4 (classify tranche C) → Step 5 (DEV — report) → Step 6 (QA) | **qa_steps:** 6 | **pause_for_verdict:** always
**cycle_tier:** T2

## CEO Context

Cycle run only: ingest the 51 un-ingested `LESSONS.md` entries (dated 2026-08-03 → 2026-08-07, sessions 18 through 24) and classify them into proposals. Gate 1 (route disposition) and Gate 2 (codification) are separate plans with CEO decisions between.

**This is the largest batch the cycle has ever run — 51, against a prior maximum of 16 (plan 296), which was itself 2× the record before it.** The mechanism is unchanged; the scale is not.

**✅ CEO DECISION TAKEN (2026-08-07, at authoring): SHAPE (b) — ingest as ONE Step-1 transaction, classification SPLIT across THREE steps (~17 each) with verdict gates between, report and QA following.** The alternatives — (a) one classification step at 3.2× the record, and (c) sub-batching the ingest, which requires a code change the parser does not support — were offered and declined. Recorded as settled so an un-struck alternative does not read as a live fork. Consequences of (b) the plan must carry, named here rather than discovered:
1. **The created-proposal anchor is created in THREE pieces** — each classification step records its own tranche list; Step 6 reads the union and fails closed if any tranche's list is missing.
2. **The isolation window is WIDER** — five verdict gates sit between the ingest and QA. With the non-terminal set measured EMPTY, the only staleable rows in the corpus during this plan's life are this cycle's own proposals; every classification step therefore re-checks `STALE_IN_SET` over all previously created tranche lists before classifying.
3. **Tail-decay instrumentation is per-tranche AND whole-batch** — each classification step reports its ~17 measured reasoning-depth pairs; Step 6's row 9 reports all 51 in id order.

⚠️ **`Test Scope: targeted` — carried from 296/288/287, and the justification is re-verified here rather than inherited.** Measured this session: `find . -name "test_*.py"` returns exactly ONE file, `src/test_lessons_forge.py`, so `python3 -m pytest src/` is simultaneously the targeted run and the full run. Rule 21 requires a written justification for `targeted`, and this is it. The contract-change carve-out does NOT fire — this plan changes no code; its only writes are DB mutations and markdown deposits. **`--collect-only` measured 55 tests at authoring** — report the actual. ⚠️ **TRACKING (CEO, 2026-07-31, continued through 288 and 296): `targeted` on a single-module repo is a precedent under observation; this is the fifth data point.** Falsified by: a defect reaching `Done/` that a broader run would have caught.

**Clone lineage — measured, not recalled (entry 219 of the batch this plan ingests).** The shipped cycle-class set, sorted by ship date: 247 → 257 → 274 → 281 → 283 → 288 → **296 (2026-08-03, the newest — verified by `ls -t knowledge/decisions/Done/` this session)**. Direct clone of **296**. The newest plan of ANY class on this corpus is **298** (Gate 2, 2026-08-03); its machinery is a different class (doctrine edit, not cycle run), and the diff obligation against it stands for the cold panel. ⚠️ **The newest same-lineage hardening ANYWHERE in the shop is exec-309 (governance, 2026-08-07)** — its cold-panel lessons (grep -c line-blindness, terminal-record blind spot, foreign-id namespacing, checker-representation records) are entries 262–265 OF THIS BATCH and are applied to this plan's own machinery below.

---

### ⚠️⚠️ INHERITED FACTS FROM 296 THAT ARE FALSE HERE — every one measured this session (2026-08-07), read-only, against live canonical

**1. THE ANCHORS MOVED. `E0 = 214`, `P0 = 222`** (296: 198/206). Verified: `sqlite_sequence` == `MAX(id)` for both tables, **no gap** → inserts land at **entries 215–265 / proposals 223–273**. G6 derives the range arithmetically from the confirmed `E0`, never from these literals.

**2. ALL THREE DOCTRINE PINS MOVED — 296's trap INVERTED.** In 296's window two pins moved and the third's stability was the trap. **This window all three moved** (309 landed doctrine 1.6 on 2026-08-07; the template is at 4.84; `RULE_20_SELF_CHECK_BLOCK.md` changed since session 14's byte-stable run). Measured with `shasum -a 256` against the live working tree at authoring:

| file | pin (authoring, 2026-08-07) | vs 296 |
|---|---|---|
| `DRAFTING_CYCLE.md` (v1.6) | `7cc27a3aac5b71393d09ab8d9690f27cf295dbadfb61912d1c3f9411c6aa42a3` | **MOVED** (296: `2d5cf9ab…`, v1.3) |
| `PLANNER_TEMPLATE.md` (v4.84) | `807f6cd91065c78bce5b422cbf4e2f9d026d7cbda144597d040c7ffb05bdd6d1` | **MOVED** (296: `e8289d50…`, v4.82) |
| `RULE_20_SELF_CHECK_BLOCK.md` | `d291b7b2cecf5e4e018a49674f383cb97c2d74d0d8659d134e44e3c70ae133a0` | **MOVED** (296: `3accbce0…`) |

⚠️ A clone carrying 296's pins forward would diff ALL three — a full-mismatch pattern that at least announces itself; the guard structure (one capture point in the Step-1a-ter stub, cited everywhere) is carried unchanged.

**3. THE HASH-TRAP SENTINEL IS ENTRY 214, NOT 198.** `content_hash` = `0017ec873912a6c75e3fb61f50b02813a3216c2c26356a02bcdf77d278987ae2`, heading `2026-08-03: A post-activation live canary can be paid for by the backlog it records [tag: process-discipline]`. The highest-id entry — where a trailing-separator hash flip would land if the plan-204 `_normalize_for_hash` fix regressed. A regression sentinel, named by id so `MAX(id)` moving under a resume cannot retarget it.

**4. THE TAG SET IS EIGHT VALUES, AND FIVE HAVE NO CORPUS PRECEDENT AS TAGS.** Measured over the 51 parsed entries and against `lesson_entries.tags` with backtick-exact equality:

| tag | batch count | corpus precedent (entries → categories) |
|---|---|---|
| `planner-discipline` | **19** | dominant; recent precedent overwhelmingly `governance_rule` |
| `verification` | **13** | **ONE prior entry** (210 → `governance_rule`) |
| `bellows-integration` | **4** | 16 prior (14 `governance_rule`, 2 `instrumentation`) |
| `drafting-cycle` | **4** | **TWO prior** (208, 209 → both `governance_rule`) |
| `drafting` | **4** | **ZERO prior entries. No precedent.** |
| `instrumentation` | **3** | **ZERO prior entries carry it as a TAG** (the CATEGORY `instrumentation` has 11 uses — different namespace; do not conflate) |
| `mechanics` | **2** | **ZERO prior** (old entries 46–49 carry `mechanics` only inside compound tag strings, not as this exact value — measured: exact-match count 0) |
| `design` | **2** | **ZERO prior as exact value** |

⚠️ **The QA category bound therefore CANNOT be a uniform tag→category map** — see Step 6 row 3 for the measured three-part form. Do NOT assert `governance_rule` uniformly; for the five precedent-less tags, classify from each entry's substance alone.

**5. `duplicates` EXIST — `DUP_COUNT=19`, unchanged since 296.** All pre-date this cycle. Every duplicate-scoped assertion in this plan uses the batch-scoped form (`entry_id > 214`), never a whole-corpus predicate (296's C9, carried).

**6. THE BACKUP GLOB POPULATION IS TWENTY, NOT SEVEN.** `data/backups/lessons-forge-pre-cycle-*.db` matches **20** files at authoring. The count is not the guard; the id token is: this cycle's backup is `lessons-forge-pre-cycle-310-<UTC-stamp>.db` and any resume glob matches on `-310-`. ⚠️ **`310` is the EXPECTED plan id (bellows `id_sequence` read 310 at authoring) — VERIFY against the id actually assigned at deposit and use THAT id in the filename; a filename carrying a dead or wrong id is the halted-302 trap.**

**7. THE EM-DASH ASYMMETRY IS 16-OF-51.** `detect_duplicates` splits headings on the literal SPACE-EM-DASH-SPACE (`_EM_DASH_SEP`, `src/lessons_forge.py:294`), whole-heading fallback when absent. Measured: **16 of 51 headings carry the separator (entries 215, 225, 226, 231, 233, 238, 241, 245, 247, 249, 251, 252, 255, 259, 262, 265); 35 do NOT** — for those the detector tests the entire dated heading. Report the asymmetry, not a uniform "no hits."

**8. FAMILY LINES ARE A MINORITY — 16 of 51** (entries 215–229 and 233 carry `**Family:**`; the other **35 do NOT**). 296's instruction assumed most entries carry one. Here the majority placement derivations come from the body alone — say so per disposition line; never report a Family line you did not find.

**9. EIGHT HEADINGS ARE SHELL-HOSTILE** (measured): apostrophes in 218, 226, 234, 244, 254, 265; a double-quote in 219; **literal backticks in 262**. Bind headings as query parameters everywhere; never interpolate one into a shell string.

---

### ⚠️⚠️ NUMBERING — THE COLLISION BAND IS 43 NUMERALS WIDE

- **`lesson_entries.id` 215–265** — THIS batch's 51 entries (after ingest).
- **`lesson_proposals.id` 223–273** — THIS batch's 51 proposals (after classification).
- **`lesson_proposals.id` 207–222** — PRE-EXISTING, all terminal (**measured: all 16 `implemented`**, plans 297/298's set). Leave untouched.
- ⚠️⚠️ **EVERY NUMERAL IN 223–265 NAMES BOTH A NEW ENTRY AND A NEW PROPOSAL — both this plan's own, and they are NOT paired.** The expected pairing is `entry 215+k → proposal 223+k` (so entry 223 pairs with proposal 231, not proposal 223). **Never write a bare number in 207–273 without its namespace.** Foreign ids are namespaced too (entry 264 of this batch): "296's C9", "entry 219", "proposal 223".
- File-position counts are a further namespace: `parse_lessons_md` sees **208** `##` entries in `LESSONS.md`; the corpus row count is **214** — the surplus is orphan rows from reworded headings, all classified, which is why `get_unclassified_entries()` is `[]` pre-cycle. Measured: NO `## Archived` heading exists, so the parser's archived-stop branch never fires. **208 and 214 are both correct and neither is the other's baseline.**

**Tranche map (expectation, not gate — `get_unclassified_entries` is authoritative at each step):**
- **Tranche A (Step 2):** the first 17 of the work list — expected entries 215–231 → proposals 223–239.
- **Tranche B (Step 3):** the next 17 — expected entries 232–248 → proposals 240–256.
- **Tranche C (Step 4):** the last 17 — expected entries 249–265 → proposals 257–273.

---

### ⚠️ Preconditions measured at authoring (2026-08-07), read-only against live canonical

| what | measured | where re-checked at run time |
|---|---|---|
| non-terminal set `NT` | **EMPTY** — `NT_COUNT=0` | G1 (pre-ingest, HALTs) |
| `stale` count | **3** (proposals 98, 121, 130) | G1 (`STALE_BASE`) |
| whole-corpus dry run through `parse_lessons_md` | **51 would-INGEST / 0 would-UPDATE / 157 unchanged**, over 208 parsed | Step 1a-bis (pre-ingest, HALTs) |
| `E0` / `P0` | 214 / 222, `sqlite_sequence` agreement, no gap | Step 1a |
| entry-214 sentinel hash | `0017ec87…` | Step 1a-bis item 2 |
| status distribution | implemented 169 · superseded 28 · rejected 15 · reference 7 · stale 3 (**no `proposed` row — `GROUP BY` omits empty buckets**) | Step 1a baseline; Step 6 row 4 |
| category distribution | governance_rule 177 · duplicate 19 · instrumentation 11 · structural 10 · narrative 5 · **language 0** | Step 6 row 3 |
| `LESSONS.md` provenance | porcelain **EMPTY**, `PORCELAIN-EXIT=0` | G2 — HALT on non-empty or non-zero exit |
| root HEAD | `0fb50e2` — ⚠️ **RECONCILE-NOTE ONLY, NEVER A HALT, EXPECTED TO DIFFER** (the draft/deposit commits move it before dispatch) | G2 |
| `detect_duplicates` path (a) | id list length **157**, **0 hits** | Step 1a-bis 2b(a) |
| `detect_duplicates` path (b) | **0 / 51** substring hits; tag criterion **inert** (reference file has 0 `**Tag:**`/`**Tags:**` lines) | Step 1a-bis 2b(b) |
| reference-file positive control | `PLANNER_TEMPLATE.md` at the absolute root path: **378,521 bytes**, sentinel `Orchestration Plan Rules` **PRESENT** | Step 1a-bis positive control |
| collected tests | **55** | Step 6 row 1 |
| `reports/lessons-report-2026-08-07.md` | **does not exist** | Step 5 pre-check |
| deposited plans of this class | **NONE** — `knowledge/decisions/` holds only `Done/` | deposit-once discipline |
| batch `raw_content` length range | **622–2131 chars** | Step 6 row 9 floor sanity |

⚠️ **Every figure above is the Planner's measurement, not a gate value** (Checklist #29): confirm each against your own read and HALT on a mismatch — **except the root-HEAD row, which is reconcile-only and near-certain to differ by dispatch time.**

**⚠️ G1 precondition.** The ingest's update path stales **non-terminal** proposals; the plan-204 `_TERMINAL_STATUSES` guard (`src/lessons_forge.py:31` — `{implemented, rejected, superseded, reference}`) protects only the terminal set. With `NT` empty the ingest is non-destructive **by construction** on a fresh run, and remains so precisely as long as no entry's `content_hash` changes. Any non-terminal proposal with `entry_id ≤ 214` at Step 1a voids the premise → HALT before the ingest.

**⚠️⚠️ G4 DETECTS hash-trap damage; Step 1a-bis PREVENTS it** — the staling UPDATE runs inside the ingest (`src/lessons_forge.py:187-193`), and `run_full_lessons_cycle` omits `stale_proposals_marked` from its return dict (`:503-511`). With `NT` empty the blast radius is zero on this corpus; the detector is retained because a non-zero `updated_count` also means file/corpus disagreement — a defect in its own right.

**⚠️⚠️ THE `NT` RECONSTRUCTION LADDER STAYS TRIMMED (296's trim, premise re-verified this session, not inherited):** `NT_COUNT=0` measured live; G1 re-verifies at run time, so a false premise HALTs rather than proceeding without machinery. The resume ladder for mid-step death IS retained — that state is reachable (session-cap exits and daemon kills are both in the shop's record). The two calls are deliberately asymmetric; a lens may attack either.

---

### The 51 entries — placement scout

**Governing rule: Rule 58 — pre-stated conclusions require verification anchors and equal evidence burden.** Rule 58(2): **this table records where the Planner looked, not a distribution** — a placement absent from it is not rejected; a fourth artifact is a legitimate outcome. Rule 58(3): every disposition carries the same evidence burden; agreeing with the scout is not the low-effort path. No Rule 27 citation — no diagnostic precedes this plan.

| # | entry | substance (one line) | scouted `target_artifact` |
|---|---|---|---|
| 1 | 215 | register append recorded a pointer, lost every item — parser reads `lu_body` only; verify in the SECTION the parser reads | `PLANNER_TEMPLATE.md` (Forward Register emission rules) — ⚠️ **cluster (B); the parser defect half is bellows-owned → Rule 46 question for Gate 1** |
| 2 | 216 | an enumerating ledger constraint decays as oscillation, not staleness; second reversal is the tell | `DRAFTING_CYCLE.md` §2.8 |
| 3 | 217 | a rule authored in the VERIFIER is never read by the producer; sweep both directions | `PLANNER_TEMPLATE.md` (new rule near 54/58) — 296/this plan already practice it; the rule is codified nowhere |
| 4 | 218 | a plan's claim about what a gate enforces is a claim to re-run (the `##`-banner error survived ten passes); a calibration range is evidence about the sample | `PLANNER_TEMPLATE.md` Rule 52 extension (re-verify inherited claims → gate-enforcement claims) |
| 5 | 219 | "newest same-class plan" is a measurement — sort by ship date and name the winner | `DRAFTING_CYCLE.md` §2.6 |
| 6 | 220 | a self-check reading the DEPOSIT cannot verify a channel parsing the TRANSCRIPT — state which artifact the consumer reads | `PLANNER_TEMPLATE.md` (channel-verification rule) — cluster (B) |
| 7 | 221 | items-in == items-out and the item still arrives truncated; constrain the shape (no wrapped bullets), compare content | `PLANNER_TEMPLATE.md` (Forward Register block format) — cluster (B); sibling of the count-is-not-value family |
| 8 | 222 | durability machinery clobbers its own artifact on the resume path it was built for; walk the RESUME path before the crash path | `PLANNER_TEMPLATE.md` (Rule 56/62 resume rules) — cluster with 261 |
| 9 | 223 | renaming an excuse launders it past the rule that forbids it; any marker meaning "I did not run this" gets the cost test | `DRAFTING_CYCLE.md` §2.7 (INHERITED-marker clause) — ⚠️ partial overlap: the cost-test clause EXISTS; the any-spelling scope does not |
| 10 | 224 | six adversarial passes; the one-command conformance check never ran and would have caught forty | `DRAFTING_CYCLE.md` §5 — ⚠️ **cluster (E) with 237; §5 exists since 1.5-era; residue is the ORDERING mandate (before the expensive passes) + exit-code recording** |
| 11 | 225 | a walk aimed at the last fold is not a walk; coverage map is the signal | ⚠️⚠️ **cluster (A) — the SHAPE DECISION (baton item 2). Route INTO the pending CEO decision, not to independent codification** |
| 12 | 226 | delete the check, not its label; verify a deletion by absence of what it DID | `DRAFTING_CYCLE.md` §2.7 (subtractive-trim bullet) — extension |
| 13 | 227 | a structural cut is an edit with its own defect class (dangling refs, orphaned captures, stale justifications); renumbering rationale was false | `DRAFTING_CYCLE.md` §2.7/§2.8 — sibling of 226 |
| 14 | 228 | in a block parsed subsection-by-subsection the LAST subsection is the exposed one; fix the class, not the noticed instance | `PLANNER_TEMPLATE.md` (Forward Register) — cluster (B); parser half bellows-owned → Rule 46 question |
| 15 | 229 | a pipe masks the exit code — four independent readers in one session | `DRAFTING_CYCLE.md` §2.7 (command-output rule) — ⚠️ partial: never-pipe is implied, not stated |
| 16 | 230 | a repair breaks what it repaired at the same severity; self-inflicted proportion is a convergence-negative signal | cluster (A) — shape decision |
| 17 | 231 | two gates over one Deposits list, opposite polarity (required vs tolerated); conditional artifacts go in prose | `PLANNER_TEMPLATE.md` (Rule 26/Deposits rules) |
| 18 | 232 | a pin whose extraction method is unstated is unreproducible and fails closed on the honest path; ship the command beside the value | `PLANNER_TEMPLATE.md` Rule 61 extension |
| 19 | 233 | the sweep fails at maximum context — fix and missed sibling written in the same sitting; enumerate sites BEFORE applying | `DRAFTING_CYCLE.md` §2.7 (fold-sweep) — extension |
| 20 | 234 | an independent referent sourced from the actor's own record is not independent; audit every NEW referent against the same test | `PLANNER_TEMPLATE.md` (new rule near 55) |
| 21 | 235 | a backup must sit adjacent to the write it inverts; state which single write each backup inverts | `PLANNER_TEMPLATE.md` (Rule 56 area) — ⚠️ this plan's own Step 1a practices it |
| 22 | 236 | a zero-difference result needs an inverse control on the same instrument in the same run | `PLANNER_TEMPLATE.md` Rule 55 extension — the positive-control generalization |
| 23 | 237 | the conformance pass catches what adversarial review structurally cannot; run when shape stabilises, not at deposit | cluster (E) with 224 → `DRAFTING_CYCLE.md` §5 |
| 24 | 238 | falling count measures aim — proven by REMOVING the aim (count rose); confirming walk must be untargeted | cluster (A) — shape decision; ⚠️ partial: §2's rotation clause landed in 1.4, the untargeted-confirming-walk residue is new |
| 25 | 239 | ten of ten ACID passes found a culmination-introduced defect; class drift (logic→record) is the judged-stop signal | cluster (A) — shape decision |
| 26 | 240 | a retraction naming its own scope can be incomplete; a consumer sweep probing the WORDING misses the CLAIM | `DRAFTING_CYCLE.md` §2.7 — claim-level probe rule |
| 27 | 241 | a guard can be safe by accident — execute the gate's real matcher; "currently passes" ≠ "cannot break" | `DRAFTING_CYCLE.md` §2.7 (:82 execute bullet) — ⚠️ partial overlap with 1.6's (D) clause; residue: report which branch fired |
| 28 | 242 | a number not produced by the plan's own mandated method is a prediction and needs a verify-clause; put the discipline inside the instrument | `PLANNER_TEMPLATE.md` Checklist #29 extension |
| 29 | 243 | probes degrade as an artifact accumulates retraction history — classify each hit as instruction vs retraction before reporting | `DRAFTING_CYCLE.md` §2.7 (probe rules) |
| 30 | 244 | a closing line written before the cycle's last phase is wrong by construction; walk → culminate → final ACID → then close | `DRAFTING_CYCLE.md` §2.7/§3 — sibling of 263; ⚠️ half sits in cluster (A) |
| 31 | 245 | an overloaded token appears in prose far more often than in position — anchor every structural search line-anchored, strip fences | `DRAFTING_CYCLE.md` §2.7 — sibling of 243 |
| 32 | 246 | copying a guard is not copying its history — inherit by diffing the parent's FINAL text; check the parent's log for folds that touched it | `DRAFTING_CYCLE.md` §2.6 — extension (three depths of clone-drift) |
| 33 | 247 | a success criterion must declare its polarity; three individually-correct patches mean the REGION is wrong | ⚠️ split: polarity half → `PLANNER_TEMPLATE.md` (diagnostic-authoring); per-region half **already codified** (1.4, §2.8) — scope to residue |
| 34 | 248 | the error that FLATTERS your own argument is the one no gate catches; re-read populations row by row; diff same-population sites | `DRAFTING_CYCLE.md` §2.7 |
| 35 | 249 | a recorded lesson does not bind its author — a rule you can EXECUTE beats a rule you must remember; recurrence after recording = mechanise | ⚠️ forge-meta: candidate `reference` or a Gate-1 ROUTING principle (recurrence → mechanization queue), not a doctrine edit. Gate 1 decides |
| 36 | 250 | the Cycle Log is the least-examined region BECAUSE it is rewritten every phase; walk it as a region on a schedule | `DRAFTING_CYCLE.md` §3/§2.6 — cluster (A)-adjacent |
| 37 | 251 | the dry condition is unreachable by construction — four consecutive plans closed without it; close on COMPOSITION | ⚠️⚠️ **cluster (A) CENTERPIECE — this IS the shape decision. diag-302/308 measured the same divergence. Route INTO the CEO decision** |
| 38 | 252 | an un-walked plan lints CLEAN while a fully-walked one WARNs — measured on one artifact | ⚠️ split: gate half (**not-run token treated as failing**) is **bellows-owned → Rule 46 fires, route to bellows FORWARD**; phrasing half already codified (§3, 1.4/1.6) — scope to residue |
| 39 | 253 | the negative-result standard adopted that morning was never applied to my own probes; zsh no-word-split; nonexistent dir == no match | ⚠️ **likely `reference` — this entry is the SOURCE of 1.6's (D) clause (History row cites diag-308).** Measure clause-by-clause at Gate 1; residue candidates: the zsh trap, path-relativity of recorded fields |
| 40 | 254 | a conformance probe must match the REPRESENTATION, not the spec's prose — a spec literal may ship as a regex | `DRAFTING_CYCLE.md` §2.7 — extension beside the `grep -F` clause |
| 41 | 255 | a fix can break its own DESCRIPTION — re-verify the describing sentence after the fold | `DRAFTING_CYCLE.md` §2.7 — sibling of 240/244 |
| 42 | 256 | a directional insert on a PREFIX anchor lands on the wrong side and passes the line-count proof; anchor on COMPLETE lines; sweep mirror form | `PLANNER_TEMPLATE.md` (edit-mechanics — new rule; memory `no-whole-file-rewrites` is adjacent but narrower) |
| 43 | 257 | commit scoping lives on the COMMIT, not the add — a bare commit ships the whole index | `PLANNER_TEMPLATE.md` (git-commit rules) — ⚠️ this plan's own steps already mandate the pathspec form; the RULE is codified nowhere |
| 44 | 258 | line numbers cited inside shipped code are load-bearing couplings for every doc edit; verify by value, not arithmetic | `PLANNER_TEMPLATE.md` (doc-edit rule, new) |
| 45 | 259 | a parent deposit can carry a DIRECTIVE to a future plan — sweep the source deposit's closing sections when authoring the successor | `PLANNER_TEMPLATE.md` (Rule 27/58 area) — ⚠️ swept for THIS plan: 296's deferred plan_lint requests are CEO-routed (wrap 2026-08-03), not this plan's obligation; no directive addressed to the next cycle found |
| 46 | 260 | a threshold clause written at a POLE silently drops the mid-band; construct mid-band cases BEFORE shipping | ⚠️ general form → `PLANNER_TEMPLATE.md` or §2.7; **the specific T-1/T-2 mid-band is SETTLED (1.5 History, consequence 4) — do NOT re-litigate**; scope to the general rule |
| 47 | 261 | a recovery branch must produce everything downstream consumers read; test recovery artifacts against the consumer's checks | `PLANNER_TEMPLATE.md` (Rule 56/62) — cluster with 222 |
| 48 | 262 | `grep -c` counts LINES — an intra-line duplicate is invisible; occurrence form `grep -Fo \| wc -l`; validate the instrument against a CONSTRUCTED failure | `DRAFTING_CYCLE.md` §2.7 — beside the count-is-not-value clause; ⚠️ this plan's own checks apply it |
| 49 | 263 | the closing record is pass-unexamined BY CONSTRUCTION; adversarial re-read of JUST the closing prose | cluster (A) + Forward #6 (shop register) — sibling of 244 |
| 50 | 264 | a foreign constraint id cited by bare number binds to the LOCAL ledger; namespace always; applied rules need LOCAL rows | `DRAFTING_CYCLE.md` §2.8 — extension |
| 51 | 265 | a true record invisible to the checker's grammar reads as false — write records in the checker's representation, only when accuracy increases | `DRAFTING_CYCLE.md` §3 — extension beside the earned-phrasing clause; sibling of 252 |

**⚠️⚠️ STANDING FLAGS FOR GATE 1 — named so they are decided deliberately, not discovered mid-disposition:**

**(A) THE SHAPE-DECISION CLUSTER — entries 225, 230, 238, 239, 250, 251, 263 (+ half of 244).** All are evidence bearing on the drafting-cycle shape decision the CEO has explicitly reserved (shop baton item 2; diag-302/308 measured the composition-bar/dry-condition divergence directly; Forward #6 tracks the post-dry-ACID datum). **Routing any of these to independent codification would pre-empt a reserved CEO decision.** The scout's recommendation: Gate 1 routes the cluster INTO that decision as its evidence set — the routing itself is the CEO's call.

**(B) THE FORWARD-REGISTER CHANNEL CLUSTER — entries 215, 220, 221, 228.** Four lessons on ONE channel (its FIFTH+ distinct failure mode). Each has an authoring-rule half and a bellows-owned parser half. Codified separately, one channel's contract ends up specified in four places. Gate 2 should weigh a single consolidated channel contract against four surgical edits; Gate 1 must split the Rule 46 halves (parser defects → bellows `FORWARD.md`).

**(C) RULE 46 CANDIDATES — 215, 228, 252 (gate half), 220 (parser half).** Each pairs an authoring rule (codify) with a tooling defect (route to the owning register, never codify a workaround).

**(D) PARTIALLY-CODIFIED — 223, 229, 238, 241, 247, 252, 253, 260.** Each measured above with its residue named. A `reference` routing that discards uncodified residue is the failure mode; so is re-codifying what 1.4/1.5/1.6 already landed.

**(E) CONFORMANCE-ORDERING CLUSTER — 224, 237.** One §5 scheduling edit, not two.

**(F) PRECEDENT-LESS TAGS — `drafting` (4), `instrumentation` (3), `mechanics` (2), `design` (2), `verification` (13 on ONE precedent).** These 24 classifications establish precedent for every future batch; they carry the higher reason-sourcing burden (Step 2–4 rules; Step 6 row 3).

**Cluster synthesis for Gate 1:** *"51 entries from sessions 18–24 — 19 planner-discipline, 13 verification, 4 bellows-integration, 4 drafting-cycle, 4 drafting, 3 instrumentation, 2 mechanics, 2 design; targets across ≥2 artifacts plus two registers; a SEVEN-entry cluster routing into the reserved shape decision; a FOUR-entry single-channel cluster with Rule 46 splits; EIGHT partial-codification measurements; and 24 classifications on five precedent-less tags."* Do NOT skip or downgrade any.

**Do NOT dedup against `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, or `RULE_20_SELF_CHECK_BLOCK.md` during classification.** Gate 1 dedups against live doctrine; the flag-(D) measurements are handed to it, not enforced here.

---

### Residual risk register

- **Best verified — the measured baseline.** Every number above was produced this session by running the real code against live canonical, read-only: the 51/0/157 dry run, `E0=214`/`P0=222` with `sqlite_sequence` agreement, `NT_COUNT=0`, `STALE_COUNT=3`, `DUP_COUNT=19`, entry-214's hash, the three pins, the 8-value tag distribution with exact-match precedent, the 16/51 em-dash and Family asymmetries, both `detect_duplicates` paths with the positive control, 55 collected tests, the status/category distributions.
- **Least verified — the split machinery.** The three-tranche classification structure is NEW — no prior cycle ran it. Its resume/isolation reasoning is stated per step and has never executed. A defect there costs a dispatch, not the corpus: every branch halts rather than mutates.
- **⚠️ Explicitly NOT verified.** Whether the 51 scouted placements are correct — Gate 1/2's question. Whether classification quality holds across three agents/steps — rows 9-analog per tranche + Step 6 row 9 measure it.
- **Declared exception to C5** — Step 6 row 7 fails closed on any in-window doctrine edit; the `❌` is an escalation channel, not a verdict.

**Scope discipline:** cycle run only. Routes stay `NULL` at insert. **Do NOT edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py`, or `bellows/gates.py`.** **Do NOT touch proposals 207–222** (terminal, plans 297/298). **⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is parser-pinned at 51.

**⚠️ Concurrency — dispatch with NO other lessons-forge cycle in flight.** This cycle's 51 proposals insert `status='proposed'`; with `NT` empty at baseline they are the ONLY staleable rows in the corpus for this plan's whole life — and the (b) split gives that window FIVE verdict gates instead of two. Detection: the `STALE_IN_SET` check at the head of every classification step + Step 6 rows 2/3/4.

**No diagnostic precedes this plan, deliberately** (247→296 lineage practice): every unknown was measured inline against live data at authoring. **✅ `LESSONS.md` is committed and porcelain-clean** — root HEAD `0fb50e2` at authoring.

**Deposit-once discipline:** to be deposited exactly once (`knowledge/decisions/` grepped this session; holds only `Done/`). **Authoring self-check:** `plan_lint.py` RUN against draft v1 (2026-08-07). **Measured: exit 0, all structural checks PASS (after one authoring fix — check (c) required the two Rule 20 strings verbatim in Step 6; the fix cites the BARE banner form per entry 218's measurement, not the parent's `##`-prefixed error), THREE WARNs, all correct:** (1)+(2) the known-benign steps-mention-tests-without-test-scope class (Steps 1 and 6; memory `benign-gate-failure-classes` — do NOT add test files to their scope to silence them); (3) **T2 plan missing cold-panel line — CORRECT: the panel has not run.** WARN 3 clears when and only when the panel actually runs; if it goes quiet while that condition is unmet, the wording has drifted into suppressing it and that is a defect. ⚠️ A clean exit is NOT evidence the §4 block ran (warn-only, exits 0 regardless) — confirm the §4 lines appear in stdout. ⚠️ A quiet §4 on an un-walked draft is a MEASURED GAP (entry 252 of this batch): silence is not evidence a cycle ran. Read the Cycle Log's lens lines directly.

## How to Run This Plan

Bellows dispatches this plan automatically when deposited; no manual bootstrap required (Rule 35).

---
---

## STEP 1 — Lessons Agent (ingest the whole corpus; NO classification in this step)

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you may run in a worktree** — **every canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.**
>
> **Working location — the plan-225 trap.** Run from your own working tree and write every file there; the ONLY exception is canonical-DB access by the absolute path above. Do NOT `cd` to the main tree.
>
> **⚠️ EXECUTION ORDER — exactly this sequence; gates are documented after Step 1b but two run BEFORE it:**
> 0. **DETERMINE DISPATCH STATE FIRST.** ⚠️ C8 applies to all probes: capture and report each probe's exit code; a FRESH determination read from silence is not a determination. Probe THREE places: (i) `git -C <your worktree> show HEAD:knowledge/development/dev-log-cycle-step-1-2026-08-07.md`; (ii) the working tree; (iii) `git log --all` on that path **and** `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'`. A hit on ANY → RESUME (recover the stub; its recorded values are authoritative for the whole step). Absent from all three → FRESH. State the determination and evidence as the first line of your dev log.
> 1. **Step 1a** — restore point, verify it, capture the baseline + `E0`/`P0` + the `NT` set.
> 2. **Step 1a-ter** — write + `git commit` the pre-ingest anchor stub (conditional — read the file first; a PROCEED-value stub with the work present in the DB routes to G5(a); a scoped duplicate count `SELECT 'DUP_IN_BATCH=' || COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 214` non-zero routes to G3 HALT, before any branch choice).
> 3. **Step 1a-bis** — pre-ingest parent-hash guard (read-only) + the `detect_duplicates` pre-check.
> 4. **G2** then **G1** — both pre-ingest. G1 is the last thing before the mutation.
> 5. **Step 1b** — the ingest (the only mutation), `conn.commit()`, append the returned dict to the stub, commit it again.
> 6. **G3, G4, G5, G6** — post-mutation detectors reading the Step-1b dict.
> 7. **Write the two deposits → `git commit` them ONCE by explicit pathspec.** ⚠️ **NO CLASSIFICATION IN THIS STEP** — shape (b): Steps 2–4 own classification behind their own verdict gates. `get_unclassified_entries()` returning the full 51-id work list is this step's CORRECT closing state, not unfinished work.
>
> **Single-writer assumption.** ⚠️ C8: capture exit codes; report literal counts. Before Step 1a, confirm no concurrent cycle: (a) `get_unclassified_entries` stable across two reads a moment apart, and (b) glob `in-progress-*.md` in the MAIN tree by absolute path — `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — NOT your worktree's frozen snapshot. Zero matches is normal; one match (this plan's own file) equally fine; any OTHER match: read its title and HALT if it is a lessons/cycle plan.
>
> **⚠️ HALT DURABILITY — every HALT in this step:** commit whatever deposit files exist by EXPLICIT PATHSPEC before stopping; record which gate halted, its measured value, and whether the ingest had committed.
>
> **⚠️ DO NOT REPAIR. You hold the write handle.** Authorized writes: the `.backup`, `run_full_lessons_cycle`, and this step's deposit files. Nothing else. (No `insert_proposal` in this step — shape (b).)
>
> **Scope:**
> - `knowledge/development/dev-log-cycle-step-1-2026-08-07.md`
>
> **Step 1a — restore point, then baseline.** Back up canonical with `.backup` (NOT `cp` — a live WAL exists), to the MAIN tree by absolute path, path built in a shell variable first:
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-310-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> ⚠️ Do NOT inline `$(date …)` between single-quoted parts of the `.backup` argument (sqlite3 misparses; no backup written). ⚠️ **`310` in the filename is the plan id assigned at deposit — if this plan's actual id differs, use the ACTUAL id and record it; the id token is the resume-glob guard.** `.gitignore` matches `*.db` — confirm absent from porcelain.
>
> **VERIFY the restore point is real:** `sqlite3 '<backup>' 'PRAGMA integrity_check;'` returns `ok`, AND the backup's `COUNT(*)` for both tables equals the LIVE DB's counts at backup time — on a fresh run 214 entries / 222 proposals; **on a RESUME the live DB is already mutated (≈265/…) and the fresh backup correctly snapshots that — do NOT assert 214/222 on a resume.** Any failure → HALT before the ingest. ⚠️ **Read a backup with `?immutable=1`, not `?mode=ro`** — `.backup` writes the file alone; the sidecars appear only after our own integrity check opens it read-write; `?mode=ro` fails on the WAL header when sidecars are absent, `?immutable=1` is correct in both states.
>
> ⚠️⚠️ **THE RESUME GLOB IS CYCLE-UNIQUE:** match on the `-310-` (or actual-id) token, end the glob in `.db` (a `-wal` sidecar errors sqlite3), take the EARLIEST match, and **PROVE it is this cycle's pristine snapshot: `SELECT MAX(id) FROM lesson_entries` must be 214 and proposals 222** (the `-296-` snapshot returns 198/206 and is thereby distinguishable). Derive the date from the actual filename or the receipt, never the local dispatch date (`date -u` after ~18:00 local rolls the day — memory `resume-glob-utc-date-vs-local`). Prefer the exact path in the Step-1 Receipt (item 7). The glob population is ~20 files and the count is NOT the guard.
>
> **Capture the baseline** (read-only), verbatim raw output: proposals by `status` **using a zero-emitting form** (LEFT JOIN/COALESCE over the enumerated status list, so every legal status prints a number — `GROUP BY` omits empty buckets and `proposed` is expected ABSENT from a bare GROUP BY at baseline), proposals by `category`, total `lesson_entries`, **the sentinel — entry 214, hash `0017ec873912a6c75e3fb61f50b02813a3216c2c26356a02bcdf77d278987ae2`, named by id, never derived from `MAX(id)`** (confirm against your own read; mismatch = HALT, not correction), and **`STALE_COUNT` (Planner measured: 3 — proposals 98, 121, 130) as its own labelled line.**
>
> **Capture `E0 = MAX(id) FROM lesson_entries` and `P0 = MAX(id) FROM lesson_proposals`. Confirm `E0 = 214`, `P0 = 222` on a fresh run; differing → HALT — but do NOT halt with the wrong diagnosis:** a "fresh" determination finding `E0 = 265` almost certainly means a prior dispatch's ingest landed with its record on a `bellows-preserved/*` branch (step 0 probe iii). Search those branches for the stub before reporting the first-dispatch ingest dict lost — it is the only unreproducible value in this plan.
>
> **⚠️ Capture THE NON-TERMINAL SET — by STATUS PREDICATE, never hardcoded ids:**
> ```sql
> SELECT p.id, p.entry_id, p.status, p.route, p.target_artifact, e.source_heading
> FROM lesson_proposals p JOIN lesson_entries e ON p.entry_id = e.id
> WHERE p.status IN ('proposed','accepted','ambiguous') ORDER BY p.id;
> ```
> Label it **`NT`**, deposit as RAW output. Expected on a FRESH run: ZERO rows — write the label and record it as empty; a missing label and an empty set are different findings. ⚠️⚠️ **Empty stdout is NOT evidence of an empty set** (entry 204's rule): also run the count form and record the printed token:
> ```
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
>   "SELECT 'NT_COUNT=' || COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous');"
> ```
> Prints a non-empty token on success in BOTH cases; silence = broken invocation → HALT. **CAPTURE ONLY — G1 owns the verdict, and it is branched: on a resume of a partially-classified corpus `NT_COUNT` is legitimately 1–51.** Report the numbers; let G1 judge.
>
> **⚠️ Step 1a-ter — COMMIT THE BEFORE-ANCHOR BEFORE THE INGEST** (the durability fix). After the restore point verifies and before `run_full_lessons_cycle`, write and `git commit` a stub `knowledge/development/dev-log-cycle-step-1-2026-08-07.md` containing:
> - `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)` — never a downstream proceed-value
> - the absolute pristine backup path
> - `E0`, `P0`
> - the raw `NT` capture + the printed `NT_COUNT=` line (never overwrite an existing stub's `NT`)
> - `STALE_COUNT=`
> - the entry-214 sentinel hash
> - ⚠️⚠️ **the three DOCTRINE PINS — THE ONLY PLACE THEY ARE EVER MEASURED.** `shasum -a 256` on `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}`, raw output into this stub. G2 and Receipt item 10 CITE this capture; neither re-measures (one source of truth — 296's collapsed-region lesson, entry 209's discipline, carried). **HALT unless all three hashes are present with the expected filenames** — `shasum` on a missing file prints nothing and exits non-zero (C8).
>
> ⚠️⚠️ **THE OVERWRITE RULE:** the final Receipt rewrites this file in place but MUST carry any recorded first-dispatch ingest dict forward verbatim under `#### First-dispatch ingest dict` — a resume's re-run correctly returns all-zero counts and must not replace the first dispatch's real ones. If the stub exists on a resume, its recorded values are authoritative over anything you re-measure now.
>
> **Step 1a-bis — PRE-INGEST hash guard (read-only; the guard, where G4 is only the detector):**
> 1. From your working tree: `import sys; sys.path.insert(0, "src")`; `from lessons_forge import parse_lessons_md`; `entries = parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` — the same parser the ingest calls. **While you hold all parsed entries, tally the whole-corpus dry run:** per entry, look up `(source_file='LESSONS.md', source_heading)` in `lesson_entries`; count `would_insert` / `would_update` / `unchanged`. ⚠️⚠️ **BRANCH ON THE STEP-0 DETERMINATION:**
>    - **FRESH → assert `would_insert == 51` AND `would_update == 0`.** Deviation → HALT pre-mutation. (Planner measured 51 / 0 / 157 over 208 parsed.)
>    - **RESUME → assert `would_update == 0`** and **`would_insert ∈ {0, 51}`** — anything in 1..50 means a partially-landed insert set, impossible from this plan's single transaction → foreign writer → HALT.
>    ⚠️ A root `LESSONS.md` commit between authoring and dispatch is PERMITTED (G2 treats the HEAD delta as reconcile-only) — a 52nd appended lesson is exactly what this assert catches BEFORE `run_full_lessons_cycle` would silently ingest it.
> 2. **The sentinel — entry 214.** Find the parsed entry whose `source_heading` equals entry 214's; compare computed vs stored `0017ec87…`. Exactly 1 match + equal → PASS. 1 match + different → HALT (classify whitespace-only = plan-204 regression vs substantive). 0 matches → HALT (the newest entry cannot be an orphan; its heading was edited). >1 → HALT (ambiguous lookup).
> 2b. **The duplicate-detector pre-check — BOTH paths, reported separately:**
>    - **(a) Pre-existing ids:** mirror the ingest's own candidate construction (parsed-and-matched headings — Planner measured **157** ids, not all 214; orphans are never handed to the detector). **PRINT THE LIST LENGTH BEFORE CALLING; HALT if 0 or wildly off 157** — the function's first statement is an empty-list early return AHEAD of the reference-file read, so an empty list returns "no duplicates" having examined nothing while the positive control stays green. Run `detect_duplicates(conn, <ids>)` read-only. Non-empty → HALT. (Planner measured: 0 hits.)
>    - **(b) This cycle's 51 parsed entries** (no ids yet — replicate the detector's CURRENT source read-only; the code is authoritative, not this plan's description). Reference file at the ABSOLUTE path `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (absent from your worktree; a relative read yields nothing and nothing looks clean). Both criteria in code order: tag overlap first (**inert today: 0 `**Tag:**`/`**Tags:**` lines in the reference — inert because the file has no tag lines, NOT because tags fail to overlap**), then the `_EM_DASH_SEP` title-substring (16 of 51 headings carry the separator — entries 215, 225, 226, 231, 233, 238, 241, 245, 247, 249, 251, 252, 255, 259, 262, 265; the other 35 test the whole dated heading). Any hit → HALT. (Planner measured: 0/51.)
>    ⚠️⚠️ **POSITIVE CONTROL before trusting any zero (the reference read fails SILENT — `cat` wrapped in `except: continue` then `if not ref_contents: return []`):** read the reference file yourself by the absolute path, and **from that ONE read** record (i) byte length (Planner measured **378,521**) and (ii) the sentinel `Orchestration Plan Rules` searched in the in-memory string (Planner: PRESENT). Both facts from the SAME read; a separate `grep` proves existence, not that the feeding read succeeded (any shell cross-check uses `grep -F` and is corroboration, never the control). Zero length or missing sentinel → every zero-hit result is void → HALT.
> 3. Record `Step 1a-bis: would_insert/would_update/unchanged actuals; NT_COUNT=<the value you captured>; sentinel check performed` — transcribe measured numbers, never a pre-composed "empty" string.
>
> **Step 1b — run the ingest (ONCE, this step only).** Open canonical read-WRITE (plain `sqlite3.connect(...)`). **Call `run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()` after it returns (the DB is gitignored; a step death without commit loses the ingest). ⚠️ **Then IMMEDIATELY append the verbatim returned dict to the stub and `git commit` it again — the ingest dict is the ONLY genuinely unreproducible value in this plan.** Print all keys: `ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `terminal_proposals_flagged`, `needs_classification`.
>
> ⚠️ **`run_full_lessons_cycle` may ALSO auto-classify or insert duplicate rows via its internal calls — read its CURRENT source before running and STATE what it will do with `needs_classification` under shape (b).** If the function classifies inline (rather than returning a work list), HALT BEFORE CALLING IT and report — shape (b) requires ingest-only in this step, and the correct call may be the lower-level `ingest_lesson_entries` + `detect_duplicates` pair. **Read the code, state the call you will make and why, then make it.** (Planner's read at authoring: the cycle function ingests, runs the detector, and RETURNS `needs_classification` without classifying — classification has always been the agent's own loop. Verify this against the live source; the code is authoritative.)
>
> ## Step 1 gates — G1 through G6 (report EVERY one as a table row: measured value + PASS/HALT; run all before halting)
>
> - **G1 — non-terminal precondition.** Capture BOTH printed numbers: `NT_COUNT` and `STALE_COUNT`. `stale` belongs to NEITHER partition (terminal vs non-terminal), so a staled row VANISHES from `NT` — the one way the empty expectation is satisfiable by corruption; hence the pair. `STALE_BASE` = 3 on FRESH (mismatch → HALT); on RESUME = the stub's recorded value, never a live re-read (C4), and a stub with no recorded baseline → report the anchor missing, comparison unverifiable.
>   - `NT_COUNT == 0` AND `STALE_COUNT == STALE_BASE` → FRESH → PASS.
>   - `NT_COUNT == n ≤ 51` where EVERY such proposal has `entry_id > 214` AND `STALE_COUNT == STALE_BASE` AND step 0 said RESUME → `PASS (resume)`. ⚠️ The `STALE_COUNT` conjunct is load-bearing: without it a staled-resume state matches both this branch (PASS) and the halt branch below. Step 0 FRESH + this condition → CONTRADICTION → HALT. `n > 51` → HALT regardless.
>   - ANY non-terminal proposal with `entry_id ≤ 214` → premise VOID → HALT before the ingest; report every id; do not improvise the removed ladder.
>   - `STALE_COUNT != STALE_BASE` (either direction) → HALT.
> - **G2 — `LESSONS.md` provenance.** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (check did not run); **non-empty output → HALT before the ingest** (do not ingest an uncommitted corpus; this is the ONE working-tree signal in this plan that halts). Record `git -C <root> rev-parse --short HEAD` (Planner measured `0fb50e2`) — **a HEAD mismatch is a reconcile-note, NOT a halt, and is near-certain by dispatch time.** G2 CITES the stub's doctrine pins (confirm three hashes are recorded there); it does not re-measure them.
> - **G3 — `duplicates_marked_count == 0`.** Non-zero → HALT, naming entry ids. On a RESUME assert the SCOPED form only: `SELECT 'DUP_IN_BATCH=' || COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 214;` (whole-corpus `DUP_COUNT` is 19 by baseline and would false-HALT — 296's C9 discipline; `entry_id > 214` is legal HERE because Step 1 holds the write handle and creates the ids). Non-zero → HALT even with a zero dict count (a prior dispatch's detector insert silently excludes that entry from every later work list). ⚠️ **A zero is NOT self-validating — G3 passes identically when the detector read nothing.** Discharge ONLY against Step 1a-bis's positive control; control absent/failed → report `HALT (unverified)` (a stop-value; bare `UNVERIFIED` has no branch in the closing rule). Do not re-run the detector to resolve it.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty.** Non-zero either way → HALT; show the diff; classify whitespace-only (plan-204 regression) vs substantive. G4 is a DETECTOR (the staling UPDATE already ran inside the ingest; the return dict omits `stale_proposals_marked`) — on failure query `status='stale'` directly and diff against the stub baseline; name the `.backup` as recovery point.
> - **G5 — there is work to do.** Fresh run expects `ingested_count == 51` and `needs_classification` == the 51 new ids. `ingested_count == 0` AND `needs_classification` empty → (a) idempotent re-dispatch of a completed Step 1 (ingest landed, deposits committed, `Status: Complete`): APPEND a `### Re-dispatch note`, set `Status: Complete (idempotent re-dispatch — no work required)`, commit, stop — never overwrite a Complete receipt with a halt record; DB-confirm first: `SELECT COUNT(*) FROM lesson_entries WHERE id > 214` == 51. (b) entries ingested but deposits absent → deposit-completion resume: regenerate the Receipt from the DB **and the stub** — the 51-id INGESTED-ENTRY list (`SELECT id FROM lesson_entries WHERE id > 214 ORDER BY id` — the write-handle carve-out; HALT unless exactly 51 rows), the first-dispatch ingest dict verbatim from the stub (absent → say so; Step 6 row 4 then `❌ (unverifiable)`), `#### Doctrine pins` copied from the stub (never re-run `shasum` — a live re-measure redefines the drift baseline as "now"), `E0`/`P0`/backup path/sentinel/`STALE_COUNT` likewise from the stub (C4). **`ingested_count` ∉ {0, 51} → HALT.**
> - **G6 — work-list reconciliation.** Batch range = `E0+1 .. E0+51` (= 215–265, ILLUSTRATIVE — computed arithmetically from the CONFIRMED `E0`, never from `needs_classification` itself, and the bound is 51 because THIS batch is 51, not a carried literal). **Invariant: every id in `needs_classification` is `> E0` and `≤ E0+51`.** Any id outside → HALT → CEO chooses (classify batch+extra / batch only with `### Deferred entries (CEO-approved)` / investigate). FRESH → the list is EXACTLY the 51; fewer → HALT. ⚠️ **Under shape (b) a FULL 51-id work list at this step's close is the CORRECT state** — do not "finish the work" by classifying; Steps 2–4 own it.
>
> **After the gate table: all PASS → write the deposits and END THE STEP (classification belongs to Steps 2–4). Any HALT — stop and report, having run the remaining gates; the ingest stays committed.**
>
> **Self-report — the 51-entry INGESTED-ID ANCHOR is created here.** Print `SELECT id, source_heading FROM lesson_entries WHERE id > 214 ORDER BY id` — expect **51 rows (215–265)**; anything else → no anchor, HALT. Record in the Receipt as a fixed-format list, one line per entry, values bare, no `|`: **`- ingested entry=<id>`**. Confirm `get_unclassified_entries()` returns exactly those 51 ids and record the list verbatim.
>
> **The Receipt opens with a status line from the CLOSED SET:** `Status: Complete` · `Status: Complete (idempotent re-dispatch — no work required)` · `Status: Partial — HALTED at <gate>, <reason>` · `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)`. It carries, each on its own labelled line: (1) the cycle/ingest dict verbatim (+ `#### First-dispatch ingest dict` when a resume is in evidence); (2) the G1–G6 gate table; (3) the pre-cycle baseline (zero-emitting status distribution, category distribution, entry count, sentinel hash, `STALE_COUNT`); (4) `E0`/`P0`; (5) the `NT` capture (+`NT-original`/`NT-now` labels on a resume; `NT-original` is the before-anchor downstream readers take; G1 alone adjudicates the live capture); (6) **the 51-line ingested-entry list**; (7) the absolute backup path(s), labelled `pristine (pre-cycle)` (+ `this-dispatch (mid-cycle)` on resume); (8) `#### Files Created or Modified` split into `##### Committed deposits` / `##### Untracked artifacts` (the `.backup` + DB mutation are gitignored main-tree writes; one unsplit list rewards concealment — 296's lesson, carried); (9) flags; (10) `#### Doctrine pins` — the stub's three hashes verbatim, never re-measured.
>
> ⚠️ Every measured value deposited as RAW COMMAND OUTPUT (memory `qa-evidence-raw-output`); annotate freely, never replace. Canonical Python file-write — no heredoc. Commit by explicit pathspec: `git add <paths>` then `git commit -m "…" -- <paths>` (**the pathspec on the COMMIT — entry 257 of this batch: a bare commit ships the whole index**). Post-commit assert: `git show --name-only --format= HEAD` prints exactly the intended paths. `#### Prompt Feedback` in `### Ledger Updates`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-08-07.md`

---
---

## STEP 2 — Classification tranche A (the FIRST 17 ids `get_unclassified_entries` returns)

---

> **Before starting, read Step 1's deposit; its Receipt status must be a PROCEED-value (`Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`) — an ALLOWLIST, not a prefix match; the in-flight stub value stops this step.** Post a short visible chat message. You are the Forge Lessons Agent (`agents/FORGE_LESSONS_AGENT.md`, ADR-002 six-value taxonomy). Same working-location + absolute-DB rules as Step 1. **Do NOT re-run the ingest. Do NOT touch proposals with id ≤ 222.**
>
> **Scope:**
> - `knowledge/development/classifications-cycle-2026-08-07-part1.md`
> - `knowledge/development/dev-log-cycle-step-2-2026-08-07.md`
>
> **⚠️ PRE-FLIGHT (all read-only, all with printed tokens — C8):**
> 1. `SELECT 'UNCLASSIFIED=' || COUNT(*) ...` via `get_unclassified_entries(conn)` length — expected **51** on a fresh Step 2 (Step 1 classified nothing); **a smaller list means a resume of THIS step (classify only the remainder) or a foreign writer (ids outside 215–265 → HALT).**
> 2. **`STALE_IN_SET`:** `SELECT 'STALE_IN_SET=' || COUNT(*) FROM lesson_proposals WHERE entry_id > 214 AND status='stale';` — non-zero → this cycle's proposals were staled by a concurrent ingest → HALT (the `.backup` is the recovery point; a staled row also puts its entry BACK on the work list, and classifying it would double-insert).
> 3. `STALE_COUNT` (whole corpus) still equals Step 1's recorded baseline (3) → else HALT.
> 4. Confirm no OTHER in-progress lessons/cycle plan (main-tree glob, as Step 1).
>
> **THE TRANCHE:** take the work list ASCENDING and classify **the FIRST 17 ids** (expected 215–231 — an expectation, never an operand: the LIST is authoritative). Fewer than 17 remaining → classify all that remain and say so.
>
> For each: read `id, source_heading, raw_content, tags, entry_date` **from the DB row in front of you**; apply ADR-002; call `insert_proposal(conn, entry_id, category, suggested_action, reasoning, confidence, ...)` — **five required positional args by NAME in this order; a sixth positional binds to CHECK-constrained `status` and fails.** `status`/`target_layer`/`target_artifact`/`route` are keywords. **`conn.commit()` after EACH insert** — a mid-list death costs the remainder, not the tranche.
> - `category` ∈ `structural`/`instrumentation`/`governance_rule`/`language`/`narrative` (never hand-assign `duplicate`). ⚠️ **The tag is EVIDENCE, not a synonym — and FIVE of this batch's eight tags have NO usable corpus precedent** (`drafting`, `instrumentation`-as-tag, `mechanics`, `design` at zero; `verification` at one). **These classifications SET the precedent; argue each from the entry's substance, and never anchor a category to a predicted id** (Rule 58(3)).
> - `suggested_action` — concrete; name any code coupling as a QUESTION for Gate 1 where Rule 46 might fire (entries 215/228's parser halves in this tranche).
> - `reasoning` — **quoted evidence from THAT entry's `raw_content`, bounded at BOTH ends** (Step 6 row 9 measures): longest contiguous quotation ≥ 40 chars (floor) and < 80% of the field's own length (ceiling — a paste is not an argument). Measured calibration, stated per entry 218's own caution that a range is evidence about the sample: 296's sixteen ran 0.089–0.643; the ceiling's margin is REAL but thinner than n=6 suggested. Cannot cite specific `raw_content` → STOP and report; never write generic justification.
> - `confidence` ∈ `low`/`medium`/`high`. `ambiguous` is a valid `status` for a genuine no-fit — say so by id.
> - **Set BOTH target fields on every non-`ambiguous` proposal** (`target_layer='governance'` expected; `target_artifact` per your OWN reading — the scout table is guidance with explicit LICENCE TO DISAGREE, Rule 58). Only `route`/`subcategory`/`duplicate_of` stay `None`.
>
> **⚠️ The scout is NOT a mandate.** Derive each target independently from `raw_content`. **16 of the batch's 51 entries carry a `**Family:**` line — in THIS tranche most do (215–229, 233 are the carriers); read it where present, and where absent derive from the body alone and SAY SO in the disposition line.** Divergence from the scout: set what the entry supports and RECORD it — silently conforming and silently overriding are both defects.
>
> **Deposit `#### Scout dispositions` in the DEV LOG (never the QA report — the lines carry `|`):** ONE line per proposal classified in this tranche, fixed formats: `- proposal <id> | entry <id> | agreed | reason: <text>` / `- proposal <id> | entry <id> | diverged | field: <category|target_artifact> | scouted: <v> | set: <v> | reason: <text>`, values bare. **Every `reason:` is drawn from the entry's own `raw_content` (or its Family line where one exists)** — never the tag, never this plan's scout prose. ⚠️ **The stricter form binds every proposal whose entry carries a precedent-less tag (`drafting`, `instrumentation`, `mechanics`, `design`, `verification`): the `reason:` must quote or name specific text justifying the CATEGORY** — these rows establish precedent for every future batch.
>
> **Also deposit the CREATED-PROPOSAL anchor for this tranche** in the Receipt, fixed format, no `|`: **`- created proposal=<id> entry=<id>`** — one line per insert, expected 17. This is one third of the anchor Steps 5–6 consume; a missing tranche list fails those rows closed.
>
> **Self-report:** `SELECT id, entry_id, status, category, target_artifact FROM lesson_proposals WHERE entry_id > 214 ORDER BY id` — expect exactly this tranche's rows (17 on a fresh run). Re-run the `NT` query, label `NT-post-tranche-A` (expected: exactly this tranche's proposals; any row with `entry_id ≤ 214` → foreign non-terminal → report prominently). Report `get_unclassified_entries()` — expected: the remaining 34 ids.
>
> **Receipt:** `Status:` line (Complete / Partial — HALTED …), the tranche's created-proposal list, per-tranche reasoning-depth self-measurement (longest-match length + ratio per proposal, id order — the tail-decay instrument runs where the work happens, not only at QA), `#### Files Created or Modified` (split lists), `#### Prompt Feedback`. Commit by explicit pathspec (pathspec on the COMMIT).
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-cycle-2026-08-07-part1.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-2-2026-08-07.md`

---
---

## STEP 3 — Classification tranche B (the NEXT 17)

---

> **Identical CONTRACT to Step 2 — restated here in full-binding compact form because each step's prompt must be self-sufficient (a rule living only in another step cannot be complied with — entry 217).** Preconditions: Step 1 AND Step 2 Receipts carry PROCEED-values (allowlist); pre-flight checks 1–4 exactly as Step 2, with expectations shifted: work list expected **34** (a different count → resume-of-this-step or foreign writer per Step 2's rule); `STALE_IN_SET` now also covers tranche A's recorded proposal ids — read them from Step 2's Receipt (**absent/unparseable → `❌`-equivalent: HALT; never reconstruct by predicate — 296's C9**) and check `SELECT 'STALE_IN_A=' || COUNT(*) FROM lesson_proposals WHERE id IN (<tranche A's 17 recorded ids>) AND status='stale';` — non-zero → HALT.
>
> **Scope:**
> - `knowledge/development/classifications-cycle-2026-08-07-part2.md`
> - `knowledge/development/dev-log-cycle-step-3-2026-08-07.md`
>
> Classify the FIRST 17 ids of the CURRENT work list, ascending (expected 232–248; the list is authoritative). All classification rules, bounds, disposition-line formats, anchor format (`- created proposal=<id> entry=<id>`, expected 17), self-report shape (`NT-post-tranche-B`; remaining work list expected 17), Receipt contents and commit discipline are THE SAME as Step 2's — and they are RESTATED as binding for this step by this sentence, not incorporated by reference for reading convenience only: if you have not read Step 2's full rule text in this plan file, read it now before classifying. ⚠️ **Family-line note for this tranche: expected carriers are ONLY entry 233** — the other ~16 have none; derive placements from the body and say so.
> ⚠️ **Shell-hostile headings CONCENTRATE here and in tranche C** (234, 244 apostrophes; 238 et al.); bind every heading as a query parameter, never into a shell string.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-cycle-2026-08-07-part2.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-3-2026-08-07.md`

---
---

## STEP 4 — Classification tranche C (the REMAINDER)

---

> **Identical CONTRACT to Step 2, restated as binding by this sentence (read Step 2's full rule text before classifying).** Preconditions: Steps 1–3 Receipts all PROCEED-values; pre-flight as Step 2 with expectations shifted: work list expected **17** (the remainder; a different count → resume/foreign per rule); `STALE_IN_SET` covers tranches A+B's recorded ids (from Steps 2–3 Receipts; missing list → HALT, no predicate fallback): `STALE_IN_AB` printed token, non-zero → HALT.
>
> **Scope:**
> - `knowledge/development/classifications-cycle-2026-08-07-part3.md`
> - `knowledge/development/dev-log-cycle-step-4-2026-08-07.md`
>
> Classify EVERY remaining id on the work list (expected 249–265). After the last insert: `get_unclassified_entries()` MUST return `[]` — record the empty result with a printed count token (`REMAINING=0`), not silence. Anchor list expected 17 lines. `NT-post-tranche-C` expected: all 51 of this cycle's proposals and nothing else. ⚠️ Family-line carriers in this tranche: NONE (entries 249–265 carry no `**Family:**` line — measured); every placement derivation is from the body; a disposition line reporting a Family line here is reporting something that does not exist. ⚠️ Entry 262's heading contains literal backticks; entries 249, 254, 265 apostrophes — parameters, never shell strings.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/classifications-cycle-2026-08-07-part3.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-4-2026-08-07.md`

---
---

## STEP 5 — DEV (generate the report)

---

> **Before starting: Steps 1–4 Receipts ALL carry PROCEED-values (allowlist — a stub or HALTED value stops this step; deliberate narrowing of the template's Partial-acceptable clause: every halt upstream concerns the integrity of the corpus this report derives from).** Post a short visible chat message. You are the Forge Developer (`/Users/marklehn/Developer/GitHub/forge/agents/FORGE_DEVELOPER.md` — skip with a note if absent). Same working-location + absolute-DB rules. **Open read-only** (`?mode=ro`).
>
> **Scope:**
> - `reports/lessons-report-2026-08-07.md`
> - `knowledge/development/dev-log-cycle-step-5-2026-08-07.md`
>
> **Pre-check:** if the report exists AND this step's dev log is committed → HALT (`generate_lessons_report` overwrites unconditionally). Report exists but deposit absent → deposit-completion resume: **copy the existing report aside FIRST** to `/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-report-pre-regen-310-<UTC-stamp>.md` (main tree, outside Scope — a worktree copy trips scope_check, an uncommitted one dies with teardown), recorded in `##### Untracked artifacts` on its own labelled line, exact form: `copy-aside (pre-regen): <absolute path>` (Step 6 row 0 cross-checks that token). Verified at authoring: no 2026-08-07 report exists.
>
> Run `generate_lessons_report(conn, "2026-08-07")` — whole-corpus; the date is only the filename/title. `pwd` before the call; state the returned absolute path; confirm the filename matches Scope. ⚠️ The known `encoding=` gap (`src/lessons_forge.py:593`, no explicit encoding) is a FORWARD item already filed by 296 — note, don't re-file.
>
> **Two DERIVED expectations (read Step 1's `NT` label — `NT-original` when present, NEVER `NT-now` — and Steps 2–4's created-proposal lists; any operand missing/unparseable → STOP and report, no literal fallback):**
> 1. Surfaced proposals = `<pre-ingest NT_COUNT> + <total classified count>` — with `NT` empty and 51 classified, **51**. A surfaced proposal OUTSIDE the recorded 51 is a RECONCILE-NOTE (id + heading recorded, CONTINUE — the gate windows are hours-to-days and a foreign in-window proposal is legitimate); one you cannot attribute at all → HALT.
> 2. **Zero `- **Route:**` lines expected** (`src/lessons_forge.py:584` emits under `if route is not None`; every insert left route NULL). ⚠️⚠️ Count with **`grep -Fc -- '- **Route:**' <report>; echo "ROUTE-GREP-EXIT=$?"`** — BOTH `-F` AND `--` (the pattern starts with `-`; without `--` it parses as an option: empty stdout, exit 2); NEVER pipe to `head` (masks the exit code). Exit 0 = matches (attribute, then decide); exit 1 = zero (the expected result); exit ≥2 = the check did not run → HALT, do not record zero. A route line attributable to one of the recorded 51 with `status` still `proposed` → Gate 1 walked in-window → record + CONTINUE. A route on any `entry_id ≤ 214` proposal, or unattributable → HALT.
>    ⚠️ The report prints NEITHER proposal id nor entry_id — attribute by `source_heading` via the DB join, **in SQL/Python with bound parameters, never shell interpolation** (eight of the 51 headings are shell-hostile; entry 262's contains backticks that EXECUTE in a double-quoted shell string).
> - Any `Recently-implemented overlap:` line → HALT (`grep -Fc --` + exit code; the detector was retired by plan 207; reappearance is a regression).
>
> **Deposit:** report + dev log with `Status:` line (Step 6 reads it), `#### Files Created or Modified`, report length, proposals surfaced, route-line count + exit codes, overlap-line count (expected zero, with exit code). Canonical Python file-write. Explicit-pathspec commit.
>
> **Deposits:**
> - `lessons-forge/reports/lessons-report-2026-08-07.md`
> - `lessons-forge/knowledge/development/dev-log-cycle-step-5-2026-08-07.md`

---
---

## STEP 6 — QA

---

> **Before starting: Steps 1–5 Receipt statuses ALL PROCEED-values (allowlist, named values — an instruction that merely says "confirm the status lines" is satisfied by observing a halted one; this one is not).** Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Same working-location + absolute-DB rules. **Verification + reporting only — a failing test is reported, never fixed. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly.**
>
> **MANDATORY — Rule 20 self-check (canonical block, exact template, four placeholders):** run from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path — governance root, not your worktree):
> - `plan_slug`: `cycle-session-18-24-captures-2026-08-07`
> - `qa_report_path`: `<your-own-tree-abs>/knowledge/qa/cycle-qa-2026-08-07.md`
> - `evidence_dir`: `<your-own-tree-abs>/knowledge/qa/evidence/cycle-session-18-24-captures-2026-08-07/` (derive from `pwd` — the plan-225 trap)
> - `required_evidence_files`: `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]` — quoted Python string literals.
>
> Deposit all four evidence files BEFORE the block (it `sys.exit(1)`s on missing/empty). Include the block's literal stdout in the QA report; the banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must appear verbatim in the deposited report (⚠️ stated WITHOUT a `##` prefix — entry 218 of this batch measured that `gates.py:567` enforces the bare string; the parent plan's `##`-prefixed claim was the inherited error) (passing runs; on a FAILED run route the stdout to `invariants.txt` and describe without reproducing the offending row — the one declared deviation). End with a self-grep confirming the banner reached the deposited report. ⚠️ **What the block verifies: evidence-file presence + hedging keywords ONLY — it cannot see verdicts; expect PASSED even on an honest halt; never flip/soften/drop a row to keep it green; a genuine `❌` fails at the rule_22 gate, and that is correct.** If any row is `❌`, add the standard one-line note under the stdout naming EVERY failing row.
>
> **⚠️ Rule 19 — VERBATIM:** *"If you cannot complete a check, mark it ❌ with a reason. Do NOT mark it ✅ and explain why you couldn't verify. Any ✅ row containing hedging keywords will auto-fail during the self-check in Rule 20."*
>
> ⚠️⚠️ Hedging keywords are fatal even as measured values — write row 1's value as `<N> passed` and NOTHING else (the word for zero-skips is itself a keyword). ⚠️⚠️ No command containing `|` in a table cell (fenced block above the table; the row cites the result; escaping `\|` silently breaks the command — entry 212). ⚠️⚠️ The status column holds EXACTLY one glyph, `✅` or `❌` — no third value, no annotated glyph (entries 211/203); a reconcile outcome is a `✅` with a note in the measured-value column. ⚠️ Close the `## Verification Table` section with `## Evidence and Narrative` immediately after the table — the gate's section flag never clears on `###`, and every later `|`-line would be scanned as table rows.
>
> **Scope:**
> - `knowledge/qa/cycle-qa-2026-08-07.md`
> - `knowledge/qa/evidence/cycle-session-18-24-captures-2026-08-07/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-session-18-24-captures-2026-08-07/invariants.txt`
> - `knowledge/qa/evidence/cycle-session-18-24-captures-2026-08-07/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-session-18-24-captures-2026-08-07/schema.txt`
>
> Table under exactly `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |`. **A failing row does not license skipping the rest — run all ten (0–9), then halt if owed; a HALT still leaves a committed record.**
>
> ⚠️⚠️ **THE IN-WINDOW RECONCILIATION RULE (rows 3, 5, 8, 9 inherit; FIVE gate windows exist under shape (b)):** every whole-corpus row adjudicates in two parts. **(a) HARD — the delta this plan owns, BY ID:** the **51 proposal ids and 51 entry ids from the recorded anchors** — Step 1's ingested-entry list + the UNION of Steps 2–4's created-proposal lists. Validate each list before querying: **51 integer values, none blank/NULL** (`NOT IN` is NULL-poisoned and fails silently toward "nothing found" — print `FOREIGN=` tokens, and a poisoned predicate attests it ran); missing/truncated/unparseable list → every dependent row `❌ (unverifiable)`, NO predicate fallback (`entry_id > 214` means "after authoring", not "ours" — a legitimate foreign in-window entry would land inside it). **(b) RECONCILE — everything outside the id set:** report ids, note in the measured-value column, still `✅`. **Gate-1 in-window on our own 51 (route set, status `proposed`) → ✅ + note. A move to `stale` → ❌ always. A terminal flip (Gate 2 landing in-window) → ✅ + note naming ids.** Row 7 is the declared C5 exception and fails closed on ANY doctrine change.
>
> 0. **Deliverable verification (Rule 17) — scoped to `##### Committed deposits` sub-lists of ALL FIVE prior Receipts** (the untracked backups/DB live in `##### Untracked artifacts`: cross-check against each Receipt's labelled paths — Step 1 item 7, Step 5's `copy-aside (pre-regen):` token via `grep -Fc --` + exit code (0/exit-1 is the expected normal-path result) — but never apply commit tests or fail the row on them). Per committed deposit, BOTH: `git log --oneline -1 -- <path>` (empty = FAILURE here — quote the printed commit line) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"` (empty + exit 0 = clean; non-zero exit = `❌`, never clean). Any ❌ → Critical, blocks Done.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail to `pytest_targeted.txt`. The whole of `src/` IS the complete run under `targeted` (one test file — measured); do not add a second run. Baseline from `--collect-only` reconciled against the most recent prior QA (Planner measured 55). Value cell: `<N> passed` only.
> 2. `get_unclassified_entries(conn)` == `[]` (quote the printed empty result WITH a count token). ⚠️ Non-empty has ONE diagnosis on a completed run: **the staling signature** (a concurrent ingest staled this cycle's proposals, un-excluding their entries) — report ids, `❌`, cross-reference rows 3/4, name the `.backup`.
> 3. **Invariants over exactly the 51 recorded proposal ids** (expect 51 rows): zero dangling `entry_id`; `route IS NULL` directional per the in-window rule; `status IN ('proposed','ambiguous')` directional (stale→❌ always; terminal→✅+note). Targets for each non-`ambiguous` proposal: `target_layer='governance'`; **`target_artifact` ∈ {`PLANNER_TEMPLATE.md`, `DRAFTING_CYCLE.md`, `RULE_20_SELF_CHECK_BLOCK.md`} as a MEMBERSHIP bound** (bare TEXT, no CHECK — free-text drift measured in corpus), **adjudicated on RECORDED DIVERGENCE, not membership alone:** outside the set + a Scout-dispositions line naming that exact proposal and target + the target RESOLVES (root file via `git -C <root> cat-file -e HEAD:<path>`; submodule-resident via `-C` against that submodule — the root form exits 128 on gitlinks) → ✅; outside with no recorded divergence → ❌ (indistinguishable from a typo). ⚠️ **Cluster-(A) proposals may legitimately carry a decision-register-shaped target or `ambiguous` status** — a recorded disposition line naming the shape-decision routing is the licence; unrecorded → ❌.
>    **Category bound, three parts (per-tag, matched with `LIKE '%tag%'` — the stored values carry literal backticks; equality returns zero rows and voids the bound; PRINT matched row counts, entry 210's rule):** `planner-discipline` (expect 19) → `governance_rule`; `bellows-integration` (expect 4) → ∈ {`governance_rule`, `instrumentation`}; **the five precedent-less tags — `verification` (13), `drafting-cycle` (4), `drafting` (4), `instrumentation` (3), `mechanics` (2), `design` (2) → ∈ {`governance_rule`, `instrumentation`, `structural`, `narrative`}** — a four-value bound; `language` (zero corpus uses) and `duplicate` are ❌. ⚠️ The bound is failable BECAUSE it is narrower than the schema CHECK (296's C12: a bound must be able to fail — the CHECK permits 6 values; these assert 1, 2 and 4). **The value-level half a membership bound cannot supply: for every precedent-less-tag proposal (~24 — the largest precedent-setting set any batch has carried), the disposition `reason:` quotes specific `raw_content` justifying the CATEGORY; empty/generic/tag-only → ❌ by id.** Partition BY THE TAG READ FROM THE ROW, never predicted ids; report measured tag counts (≠ 19/13/4/4/4/3/2/2 is itself the finding). `ambiguous` proposals exempt from target+category bounds; report by id. Scoped count ≠ 51 → FAIL. **FIRST count the disposition lines across the THREE dev logs: exactly one per created proposal (51 total; count per-tranche with `grep -Fc -- '- proposal'` + exit codes); fewer → ❌ naming the ids with no line.**
> 4. **The plan-204 fix held.** Baseline from Step 1's Receipt (missing → `❌ (unverifiable)`, the fail-closed backstop). `stale` not grown (before=3, after printed); no terminal-status departures; **entry 214's `content_hash` unchanged** (`0017ec87…`); `updated_count` + `terminal_proposals_flagged` from `#### First-dispatch ingest dict` when a resume is in evidence, else item 1. ⚠️⚠️ **A COUNT IS NOT A VALUE GUARD (entry 199, codified 1.4):** state (i) `stale` before, (ii) after, (iii) **the FULL zero-emitting status distribution before and after with this cycle's own delta subtracted** — expectation exact and failable: `implemented` 169, `superseded` 28, `rejected` 15, `reference` 7, `stale` 3 all UNCHANGED (confirm against Step 1's Receipt item 3, not these literals); `proposed` ABSENT before (GROUP BY omits empty buckets — no output will ever show `0`), present after at the classified count (51 fresh; a terminal Gate-2 in-window flip adjusts BOTH buckets — name ids). State the count of proposals examined; a row that cannot say how many rows it read has not run. Raw to `hash-trap.txt`.
> 5. **Report exists; in-window rule applies.** HARD: all 51 recorded proposals surfaced (attribute headings→ids via the DB join, bound parameters; the report prints neither id). Use the report's own `**Total proposals:** N` line. RECONCILE: foreign surfaced proposals listed by id, ✅+note. Pre-ingest `NT_COUNT` from `NT-original`/`NT` (never `NT-now`; both-present-and-indistinguishable → `❌ (unverifiable)`). Route lines: directional, `grep -Fc --` + exit code. Zero overlap lines; `detect_recently_implemented_overlaps` still absent from `src/`.
> 6. **No schema drift** — semantic comparison (PRAGMA table_info + constraint set) vs `src/db.py` DDL; cosmetic RENAME artifacts are NOT drift. Raw `.schema` both tables → `schema.txt`.
> 7. **Doctrine unchanged — TWO NAMED SUB-CHECKS, both fail-closed, neither adjudicated by you.** **7a (this-window guard):**
>    ```
>    git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md PLANNER_TEMPLATE.md RULE_20_SELF_CHECK_BLOCK.md; echo "PORCELAIN-EXIT=$?"
>    ```
>    BOTH pass conditions required: empty output AND exit 0 (`-C` is REQUIRED — from your worktree these files do not exist and a bare invocation passes silently/vacuously). Non-zero exit → `❌ (check did not run)`, distinct from `❌ (doctrine changed)`. **Non-empty porcelain → ❌, full stop — attribution is the CEO's at the verdict gate, never yours:** capture `git log --oneline <authoring-HEAD>..HEAD -- <files>` + `git diff` into `invariants.txt` before halting. **7b (drift since authoring):** `shasum -a 256` the three files vs **Step 1 Receipt item 10** (the stub's single measurement, republished); item 10 absent/short → `❌ (unverifiable)`. Print all three live + all three recorded + three pairwise verdicts (self-evidencing, C8). Working-tree content pins, never `rev-parse HEAD:<path>` (blind to uncommitted edits). `plan_lint.py`/`gates.py` deliberately unchecked (no write path from this cycle — a write-path argument, not an importance ranking; do not extend it to the three root files no other instrument can see).
> 8. **Post-cycle DB counts, in-window rule.** HARD by recorded id lists: entries `IN (<the 51>)` = 51; proposals `IN (<the 51>)` = 51 (validated lists; no `> 214` predicates — one foreign in-window row makes 52 and a false ❌). RECONCILE totals: derivation `214 + 51 = 265` entries, `222 + 51 = 273` proposals — Planner measurements to verify and explain, not force (Checklist #29). Above-derivation with owned delta correct → foreign ids named, reconcile-note, no ❌. Status+category actuals. Raw to `invariants.txt`.
> 9. **Classification depth — THE scale instrument, per-proposal over all 51 recorded ids.** Extraction-free: canon() (curly→straight, strip `*_` and backticks, collapse whitespace, lowercase), `difflib.SequenceMatcher(None, a, b, autojunk=False)` longest match; **PASS per proposal iff match ≥ 40 chars AND match < 80% of `canon(reasoning)`'s length.** Report all 51 (length, ratio) in id order — a monotone decline IS the finding independent of the floor; **also report the three per-tranche distributions side by side** — an inter-tranche cliff is the shape-(b) analogue of tail decay and no single-step cycle has ever measured it. Calibration (a range is evidence about the sample — entry 218): 296's sixteen ran match 62–115+/ratio 0.089–0.643 against the same bounds; batch `raw_content` 622–2131 chars, so the floor cannot false-FAIL on length. Any proposal failing either bound → ❌ naming id + bound + measured pair. Batch clustering near 0.80 → a finding about the classification work even if all pass.
>
> **Evidence routing:** rows 0/2/3/5/7/8/9 → `invariants.txt`; row 4 → `hash-trap.txt`; row 6 → `schema.txt`; row 1 tail → `pytest_targeted.txt`. Before the Rule 20 block runs, self-grep each file for a content marker (`PORCELAIN-EXIT=` in invariants; the `0017ec87` prefix in hash-trap; `CREATE TABLE` in schema; the pytest summary line in pytest_targeted) with `grep -F`, **printing what matched, not PRESENT/ABSENT** (entry 210) — the block only checks non-empty and a one-byte file passes it.
>
> **Deposit:** `knowledge/qa/cycle-qa-2026-08-07.md` + the four evidence files. Canonical Python file-write. `git add <paths>` then `git commit -m "…" -- <paths>` (add first — new files; on a pathspec error, `git add` and retry, never `-a`).
>
> In `### Ledger Updates`:
>
> `#### Project Status` — milestone SCOPED to this cycle's 51 (never a bare corpus-wide count — row 5(b) permits a foreign in-window proposal at close): cycle 2026-08-07 complete — the 51-entry session-18→24 batch ingested (Step 1) + classified across three tranches (Steps 2–4), report deposited, corpus integrity held, non-terminal baseline confirmed empty at G1, this cycle's 51 the only non-terminal rows this plan owns at close; Gate 1 pending for the 51.
>
> `#### Forward Register` — ⚠️ write this block INSIDE `### Ledger Updates` (the daemon's parser reads `lu_body` ONLY — entry 215 of this batch: a block one heading too high is silently discarded), one item per bullet line, no bullet wrapping onto a second physical line (entry 221: a wrapped continuation is never joined), described not quoted, with a terminating blank line after the last bullet (entry 228: the last subsection is the exposed one). **State the register's before-count read from your worktree snapshot (correct before-value — the daemon appends post-merge to the main tree) and record that you read it there.** TWO items:
> 1. The three-tranche split (shape (b)) ran for the first time — record whether any tranche boundary produced a measurable quality cliff (row 9's per-tranche distributions), as calibration data for the next large batch's shape decision.
> 2. `get_unclassified_entries` returns the full remainder with no ordering contract stated in its docstring; the tranche discipline depends on ascending-id order — worth a one-line documented guarantee (lessons-forge-owned, small).
>
> `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-qa-2026-08-07.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-session-18-24-captures-2026-08-07/` (evidence directory as a single bullet — Rule 26; individual evidence filenames stay in Scope and `required_evidence_files` only)
>
> **Do NOT move this plan to `Done/`** — the close path is Bellows-owned on continue-verdict consumption (Rule 8); unconditional, no post-verdict branch.

---

## Drafting Cycle
**Tier:** T2 — triggers fired: T-2 (production-data mutation → T1) and **T-5 (irreversible ingest — the unsure-fires rule applied: a committed 51-row canonical ingest with classification references landing behind five verdict gates is not cleanly revertible mid-arc) → T2.** ⚠️ Under 1.6 this is NOT T-1's every-row clause (51 inserts + 0 updates measured is not a table-wide mutation); T2 computes from T-5, stated so the 1.5 mid-band acceptance is not re-litigated. A proven-clone framing does not down-tier (§2.6) — and this plan is NOT a pure clone: the three-tranche split is novel machinery (T-8 also fires → T1; subsumed).
**Walks:** none yet — this is draft v1, no lens pass of any kind has run.
- Weak spots:          not yet run.
- Destruction:         not yet run.
- Vulnerabilities:     not yet run.
- Integration-record:  not yet run.
- ACID:                not yet run.
**Panel status (T2 cold reader panel):** NOT RUN — the panel has not been convened. ⚠️ This line is deliberately phrased so §4's line-anchored cold-panel pattern cannot match it; switch to the canonical opening ONLY when the panel has actually run (entries 252/265: a check must clear EARNED — and the un-walked state lints silent, which is a measured gap, not a clean bill).
**Conflicts:** ledger below, seeded at authoring; none tested yet.
**Closing:** not reached — v1 draft; no lens pass has run; not deposited.

---

### Conflict Ledger (§2.8) — seeded at authoring; ids are LOCAL (foreign ids namespaced — entry 264)

- **C1** — the empty non-terminal baseline is a measured premise: every guard resting on it re-verifies at run time or halts (carried from 296's C1).
- **C2** — no step hardcodes a count it can read from a recorded capture; literals are declared Planner measurements (296's C2).
- **C3** — a removal of inherited machinery is declared in the artifact with premise + run-time guard (296's C3).
- **C4** — a resume anchors on the ORIGINAL committed capture, never a live re-read (296's C4).
- **C5** — a permitted outcome is never a FAIL; ONE exception: Step 6 row 7 fails closed on doctrine changes (296's C5).
- **C6** — a fold that changes a convention lands here as a CONSTRAINT, not only at its site (296's C6).
- **C7** — no pre-ingest instruction states an unqualified fresh-run claim about a resume-variant value; qualify by the step-0 determination or capture-and-defer. No site roster (296's C7; roster form decayed twice there — entry 216's oscillation lesson noted).
- **C8** — every mandated check reports a positive token or exit code; nothing is discharged by absent output; binds hardest on ZERO/EMPTY expectations (296's C8).
- **C9** — post-Step-1 assertions about owned rows name the RECORDED id lists; `entry_id > 214` / `id > 222` forbidden as ownership operands past Step 1; carve-out: report-only complements. **Under shape (b) the anchor is a THREE-PART union — a missing tranche list fails dependents closed, never falls back to a predicate.**
- **C10** — a trim replacing a value-level assertion with a count constructs the change the survivor must catch and confirms it FAILS (296's C10; codified 1.4).
- **C11** — no third status glyph; no `|`-bearing command in a table cell (296's C11).
- **C12** — a bound must be able to fail: name the input that fails it, or it asserts nothing (296's C12; row 3's bounds are all narrower than the schema CHECK, stated inline).
- **C13** — a capture a LATER step/row/resume branch must read is deposited in a committed artifact; a value consumed within its producing step needs no home (296's C13 final form — the principle, no list, no axis).
- **C14 (new, this plan, from entry 217)** — every mandated requirement is stated IN the step that must comply with it; a rule living only in a verifier or only in a producer is a defect in whichever direction is missing. The classification rules are therefore restated as binding in Steps 3 and 4, not referenced for convenience.
- **C15 (new, this plan, from entries 220/221/228)** — a check on a delivery channel names the ARTIFACT the consumer reads; a block feeding a section-scoped parser is verified in that section; no bullet wraps; the block terminates with a blank line.
- **C16 (new, this plan, from entry 262)** — any presence check over content that can duplicate intra-line uses the occurrence form (`grep -Fo | wc -l` semantics), never a line count.

**Ledger status:** C1–C16 OPEN. C14–C16 were opened at authoring from the batch's own entries and have not been tested by any lens. None can be reported SATISFIED before the walks that would test them run.
