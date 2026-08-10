# Lessons Forge — Cycle Run 2026-08-10, PLAN A: ingest the 41-entry session-24→33 batch (classification held to Plan B)

**Date:** 2026-08-10 | **Tier:** Small | **Dispatch Mode:** bellows | **Test Scope:** targeted | **Execution:** Step 1 (Lessons Agent — ingest all 41) → Step 2 (QA) | **qa_steps:** 2 | **pause_for_verdict:** always
**cycle_tier:** T2

## CEO Context

**Ingest only.** This plan takes the 41 un-ingested `LESSONS.md` entries into the corpus and stops. **It creates no proposals, writes no report, and classifies nothing.** Classification, the report and their QA are **Plan B**, authored separately against the work list this plan leaves behind.

### ⚠️⚠️ WHY THE SPLIT — a CEO decision taken on measured evidence, not a preference

The six-step plan this is derived from went through **eight walks and a five-lens fresh-reader pass; walk 8 alone returned 55 findings on an artifact seven prior walks had already worked over, and its per-lens yield ROSE (10 → 9 → 7 → 14 → 15).** The ACID lens's isolation map explains why: six steps behind five verdict gates over one shared store produce a **seven-window guard matrix**, and essentially every HIGH finding in the cycle lived in that matrix — a Gate-1 carve-out owed at four separate sites, Gate-2 arms needed at six windows, one id list whose durability had to hold across five gates. **That complexity is structural, and folding one cell of the matrix perturbed the others**, which is what the rising curve measures.

**Splitting collapses the matrix.** This plan has ONE step that writes, ONE verdict gate, and ONE window. It also carries **all** of the arc's destructive risk — the 42 unprotected `accepted|codify` rows, the hash trap, the batch pin — which is precisely the half five independent readers have now attacked hardest. Plan B, by contrast, holds no destructive write at all: `insert_proposal` only adds rows.

⚠️ **What this plan deliberately does NOT carry, because it belongs to Plan B:** the 41-entry placement scout, the twelve-value tag-precedent analysis, standing flags (A)–(G) including the mechanism-versus-discipline routing test, the cluster synthesis, the tranche map, and the whole classification contract. **None of them is discarded** — they live in `knowledge/research/draft-cycle-run-339-2026-08-10.md` and in the committed walk register, and Plan B is authored from there.

⚠️ **`Test Scope: targeted` — justification re-verified, not inherited.** `find . -name "test_*.py"` returns exactly ONE file, `src/test_lessons_forge.py`, so `python3 -m pytest src/` is simultaneously the targeted run and the full run. Rule 21 requires a written justification; this is it. **`--collect-only` measured 55 tests at authoring** — report the actual.

**Clone lineage — measured, not recalled.** Step 1 is carried **verbatim** from the eight-walk draft, with its downstream references re-pointed at Plan B and nothing else changed: it is the most-reviewed artifact this shop has produced this session and re-authoring it would discard that review. The cycle-class set in `Done/` by plan id: 247 → 257 → 274 → 281 → 283 → 288 → 296 → **311** (the direct clone origin and newest same-class).

---
### ⚠️⚠️ INHERITED FACTS FROM 311 THAT ARE FALSE HERE — every one measured 2026-08-10, read-only, against live canonical

**1. ⚠️⚠️ `NT` IS NOT EMPTY. `NT_COUNT = 42`, and 311's central safety premise is VOID.**

311 stated the ingest was *"non-destructive by construction"* because the non-terminal set was empty. It is not empty here, and every one of its rows is queued Gate-2 work:

| status | route | target_artifact | count | in `NT`? |
|---|---|---|---|---|
| `accepted` | `codify` | `DRAFTING_CYCLE.md` | **21** | yes |
| `accepted` | `codify` | `PLANNER_TEMPLATE.md` | **21** | yes |
| `stale` | — | `PLANNER_TEMPLATE.md` | 3 | **no** — counted as `STALE_COUNT` |

⚠️ **`NT_COUNT` is 42, not 45.** `stale` belongs to neither the terminal nor the non-terminal partition, so it is reported as its own number everywhere in this plan and never summed into `NT`. See Step 1a's single definition; no gate compares against 45.

⚠️⚠️ **`accepted` is NOT a member of `_TERMINAL_STATUSES`** — measured as shipped: `frozenset({'implemented', 'superseded', 'rejected', 'reference'})`. The plan-204 guard therefore does **not** protect these 42 rows. The ingest's update path (`src/lessons_forge.py:187-193`) stales any non-terminal proposal whose entry's `content_hash` changed, via `WHERE entry_id=? AND status != 'stale'`.

**The blast radius of a single unexpected hash flip is the entire queued Gate-2 batch — including the 21 `DRAFTING_CYCLE.md` proposals this whole route exists to codify.** **The `NT` set spans `entry_id` 215–265** — every one of the 42 belongs to plan 311's own batch, the newest 51 entries, **so the exposure is to any edit that rewrites those entries rather than appending after them.** ⚠️ **Never fold the `stale` partition into this figure** — that is the conflation this section forbids two paragraphs above. The 93 was the entry_id of *stale* proposal 98, so the figure folded the stale partition into `NT`, the exact conflation this section forbids two paragraphs above. **All 42 belong to plan 311's own batch — the NEWEST 51 entries**, which are the ones a rewording pass is most likely to touch. The exposure is differently shaped than the wrong figure implied, not smaller.

⚠️⚠️ **THE SEVERITY IS PRICED, NOT ASSERTED — and the honest price is lower than the sentence above implies.** The staling UPDATE sets `status='stale'` and touches `status_updated_at`/`status_updated_by`; it does **not** delete the row and does **not** touch `route`, `target_artifact`, `target_layer`, `suggested_action`, `reasoning`, or `confidence` (source read, `src/lessons_forge.py:184-193`). **The damage is one column on rows whose ids Step 1 records, and the reversal is a single targeted `UPDATE lesson_proposals SET status='accepted' WHERE id IN (<the recorded 42>)`.** The exposure is **detectable and repairable, not destructive** — which is why this plan spends its effort on DETECTING the flip at G1 and on RECORDING the 42 ids (Receipt item 5), rather than on recovery machinery it does not need. ⚠️ Stated because the adjectives were doing the work unpriced: "worst available", "blast radius", "at risk" all appear above and none of them had a probe until this line.

⚠️ **Corollary, and it corrects an instruction inherited from 311: after Step 1b the pristine `.backup` is a FORENSIC reference, not a restore target.** Once Plan B has begun classifying, restoring it would discard every classification committed since the ingest. Where a later step says "name the `.backup`", it means *record the path so the pre-cycle state can be inspected* — the repair for a staled Gate-2 row is the targeted UPDATE above.

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

**7. THE EM-DASH ASYMMETRY IS 24-OF-41.** `detect_duplicates` splits headings on the literal SPACE-EM-DASH-SPACE (`_EM_DASH_SEP`, `src/lessons_forge.py:294`), whole-heading fallback when absent. Measured: **24 of 41 headings carry the separator; 17 do NOT** — for those the detector tests the entire dated heading. Report the asymmetry, not a uniform "no hits."

**8. ELEVEN HEADINGS ARE SHELL-HOSTILE** (measured — **entries 268, 270, 277, 280, 281, 284, 286, 290, 291, 297, 300**, i.e. batch positions 3, 5, 12, 15, 16, 19, 21, 25, 26, 32, 35): apostrophes, a double quote, and literal backticks. ⚠️ Given as **entry ids** because every step cites them that way; the positions are shown alongside only so the two forms can be reconciled without arithmetic. Bind headings as query parameters everywhere; never interpolate one into a shell string.

**9. THE BACKUP GLOB POPULATION IS NINE, NOT EIGHT.** `data/backups/lessons-forge-pre-cycle-*.db` matches **9** files at authoring. The count is not the guard; the id token is — this cycle's backup is `lessons-forge-pre-cycle-339-<UTC-stamp>.db` and any resume glob matches on `-339-`. ⚠️ **Derive the date from the actual filename at resume, never from a hardcoded local date** — a `date -u` stamp rolls to the next day after ~18:00 local.

---


---

### ⚠️⚠️ NUMBERING — TWO BANDS, AND THEY ARE NOT THE SAME BAND

The **double-naming band is 274–306, 33 numerals wide** — every numeral there names both one of this batch's entries and one of its proposals. The **namespacing rule covers the wider 232–314**, because a bare numeral anywhere in that range reads as either an entry or a proposal id. ⚠️ An earlier draft titled this section with the 33 as though it described the namespacing band; the two were conflated.

- **`lesson_entries.id` 266–306** — THIS batch's 41 entries (after ingest).
- **`lesson_proposals.id` 274–314** — THIS batch's 41 proposals (after classification).
- **`lesson_proposals.id` 223–273, NON-CONTIGUOUS** — PRE-EXISTING and **NOT terminal**: the 42 `accepted|codify` rows of the queued Gate-2 batch. ⚠️⚠️ **The span is NOT a range and must never be used as one.** Measured at authoring: the 42 run 223–273 with **nine ids inside that span excluded** — `232`, `245` (`implemented`, flipped by plan 330's §5 pair) and `233`, `238`, `246`, `247`, `258`, `259`, `271` (the seven cluster-A rows, still `reference|backlog`). **A range operand of 232–273 under-protects proposals 223–231 and over-claims those nine.** ⚠️ **Every operand touching these rows is the RECORDED ID LIST from Step 1 Receipt item 5, never a BETWEEN.**
- ⚠️⚠️ **EVERY NUMERAL IN 274–306 NAMES BOTH A NEW ENTRY AND A NEW PROPOSAL — both this plan's own, and they are NOT paired.** The pairing is `entry 266+k → proposal 274+k` (offset **+8**), so entry 274 pairs with proposal 282, not proposal 274. **Never write a bare number in 232–314 without its namespace.** Foreign ids are namespaced too: "311's C9", "entry 266", "proposal 274", "FORWARD 53".
- File-position counts are a further namespace: `parse_lessons_md` sees **249** `##` entries in `LESSONS.md`; the corpus row count is **265**. 208 of the 249 parsed match DB rows, and the **57 unmatched DB rows are orphans** from reworded headings, all classified — which is why `get_unclassified_entries()` is `[]` pre-cycle. Measured: NO `## Archived` heading exists, so the parser's archived-stop branch never fires. **249 and 265 are both correct and neither is the other's baseline.**

**⚠️⚠️ THE ASSUMPTION EVERY ID-BEARING TABLE BELOW RESTS ON, stated because it is load-bearing and was verified rather than assumed.** Plan B's scout table, tranche map and cluster lists, and this plan's shell-hostile list, all bind a *substance* to a *predicted entry id*. That binding is sound only if `lesson_entries.id` is assigned in `parse_lessons_md` file order. **Verified by source read at authoring (`src/lessons_forge.py:138-153`): `ingest_lesson_entries` iterates `for entry in entries` — the parser's list, in file order — and INSERTs each new one in that order, so with `AUTOINCREMENT` the k-th un-ingested entry receives id `E0 + k`.** ⚠️ Note the consequence that is easy to miss: **the 41 are NOT contiguous in the file.** The six 2026-08-07 stragglers sit *earlier* than the 2026-08-08→10 block, so they take ids 266–271 and land in tranche A. ⚠️ **This is a derivation, not a gate: every step keys on `get_unclassified_entries` and on `source_heading`, never on a predicted id. If a disposition and its heading disagree, the HEADING wins and the mismatch is reported.**

⚠️ **THE TRANCHE BOUNDARIES ALSO DEPEND ON ORDERING, and the dependency is load-bearing.** "The FIRST 14 ids the work list returns" is a bound only if the list is ascending. **Verified by source read (`src/lessons_forge.py:284-290`): the query carries `ORDER BY e.id`.** ⚠️ **The guarantee is in the SQL and NOT in the docstring** — which is precisely the open register item below, so this plan depends on a contract that is real but undocumented, and a refactor dropping the clause would break every tranche boundary with no test objecting.

**Tranche map (expectation, not gate — `get_unclassified_entries` is authoritative at each step):**
- **Tranche A (Step 2):** first 14 of the work list — expected entries 266–279 → proposals 274–287.

---


---

### Residual risk register

- **Best verified — the measured baseline.** Every number above was produced this session by running the real code against live canonical, read-only: the 41/0/208 dry run, `E0=265`/`P0=273` with `sqlite_sequence` agreement, `NT_COUNT=42` with its full composition and the separate `STALE_COUNT=3`, `_TERMINAL_STATUSES` read as shipped, `DUP_COUNT=19`, entry-265's hash, the three pins, the 12-value tag distribution with exact-match precedent, the 24/41 em-dash and 0/41 Family asymmetries, 55 collected tests, the status distribution.
- **Not carried here — the scout.** It is Plan B's, at heading-and-remedy depth. Gate 1 owes each of the 41 a body read.
- **⚠️ Explicitly NOT this plan's concern.** Whether the 41 scouted placements are correct — Plan B's, then Gate 1/2's. Whether classification quality holds across three agents (entry 271 says it did at 51; this is the confirming instance, not the establishing one). Whether the `would-UPDATE = 0` property survives to dispatch — **Step 1a-bis is the only thing standing between a hash flip and 42 staled proposals**, and that branch has never executed on a non-empty `NT`.
- **The `NT`-non-empty branch is genuinely new machinery.** 311 and 296 both ran with `NT` empty. Every guard in this plan that reasons about the queued Gate-2 batch is unexercised.

**Scope discipline:** cycle run only. Routes stay `NULL` at insert. **Do NOT edit `DRAFTING_CYCLE.md`, `PLANNER_TEMPLATE.md`, `RULE_20_SELF_CHECK_BLOCK.md`, `bellows/scripts/plan_lint.py`, or `bellows/gates.py`.** **Do NOT touch the 42 `accepted|codify` proposals** (the queued Gate-2 batch, unprotected by `_TERMINAL_STATUSES`) — **identified by the predicate `status='accepted' AND route='codify'` and by Step 1 Receipt item 5's recorded id list, NOT by an id range: they span 223–273 non-contiguously, with nine ids inside that span belonging to other statuses.** **Do NOT touch proposals 98/121/130** (`stale`, settled 2026-07-16). **⚠️⚠️ Do NOT append to `LESSONS.md` while this plan is deposited-but-un-run** — the batch is pinned by the Step-1a-bis fingerprint, and finding 2 is what that prohibition looks like when it is ignored.

⚠️⚠️ **THIS COLLIDES WITH THE SESSION-WRAP RITUAL, AND THE COLLISION IS LIVE FOR THE SESSION THAT DEPOSITS THIS PLAN.** The shop's wrap appends the session's lessons to `LESSONS.md`. This plan's fingerprint HALTs on exactly that. The two are incompatible for as long as the plan sits deposited-but-un-run, and the prohibition binds the *depositing* session, not some future one. **Resolution, decided at authoring rather than discovered at G1:** either (a) dispatch 339 to completion before any wrap-time append, or (b) append first and **re-run the fingerprint here, and re-token Plan B's tranche map and scout before Plan B is authored.** ⚠️ **What is NOT available is depositing and then appending** — the plan would halt at Step 1a-bis having already been claimed, and the correction would cost a stop plus a re-deposit under a fresh id.

**⚠️ Concurrency — dispatch with NO other lessons-forge cycle in flight.** Detection: the branched staleability checks at the heads of Steps 3–4, the whole-corpus `STALE_COUNT` baseline check, and this plan's QA row 7 reconciliation.

**No diagnostic precedes this plan, deliberately** (247→296→311 lineage practice): every unknown was measured inline against live data at authoring. **✅ `LESSONS.md` is committed and porcelain-clean** — root HEAD `ad3c2d7` at authoring.

### ⚠️ Planner obligations at the verdict gates — this plan's THIRD actor, given a home

**Steps address agents. These are addressed to the Planner** — kept here rather than inside step prompts the Planner writes and the agent reads, which is C14's defect mirrored: a rule living in the wrong actor's text. Each gate between steps, before writing a verdict:

- **Compare the `steps` table against the commit and deposit counts** before issuing any verdict. ⚠️ **This is batch entry 297's own remedy, and the plan that INGESTS that lesson was not applying it** — `pause_for_verdict: always` is a header contract the runtime does not police, and plan 336 executed three steps in one dispatch while the daemon recorded one. A step count disagreeing with the commits or deposits means the boundaries were not honoured, and the verdict is where that gets caught.
- **Reconcile the Gate-2 queue** at every gate, not only at QA: the recorded 42 ids against `status='accepted' AND route='codify'`, adjudicated by QA row 7's causal test. This plan's headline risk is invisible to every step-scoped check.
- **After the QA step, re-read `lessons-forge/knowledge/FORWARD.md` in the MAIN tree and confirm it gained EXACTLY ONE row, whose text matches the item the QA agent recorded emitting.** Step 6 emits one Forward Register block (the §2.8 deletion was reversed — see Step 6). **Two rows, or zero, is the finding.** ⚠️ **This obligation was inverted until a diff review caught it: it previously said "confirm it gained exactly one row", written when the block still existed, and the cut left the sentence asserting a row that can never appear** — a retained-material checklist could not see that, because the item was retained and only its wording was falsified. **A row appearing here has TWO candidate causes and the likelier one is not the alarming one:** (a) the QA agent emitted a Forward block from habit or from its agent-file contract despite this plan declining one — **check the transcript first**; or (b) a foreign writer used the channel in-window. **Diagnose in that order.** Reading (a) as (b) would manufacture a concurrency incident out of an agent doing what every other cycle plan told it to do.
- ⚠️ **Do NOT hand-add the `_TERMINAL_STATUSES`-omits-`accepted` item at wrap.** the QA step emits it through the daemon channel, and Rule 42 authorizes status updates only, never a new row. **Adding it by hand would write the item twice — the byte-identical-duplicate defect this plan records as live debt at rows 9 and 10.**

⚠️ **The ordering constraint that once governed these two is RETIRED: it existed to keep a Planner wrap edit from tripping a gained-NO-rows check, and neither side survives the reversal.** The row the QA step emits is expected; a SECOND row is the channel event.
- **Reconcile rows 9 and 10** — byte-identical duplicates written by plan 311's own step 6 through the channel this plan declines to use.
- **Re-verify, never inherit,** any precondition this plan measured at authoring that the verdict turns on.

---

**Authoring self-check (§5 — the conformance pass, run at shape-stability, before the adversarial passes close).** `plan_lint.py` RUN against draft v1 at the **drafting path `lessons-forge/knowledge/research/`, whose `project_root` resolves identically to the deposit path** (both sit under `lessons-forge/knowledge/`), so the declared state is the deposit state. **Exit 0; last run at walk 8's lens-4 culmination** — §5 requires the recorded exit code to be the LAST run's.

⚠️ **A clean exit is NOT evidence check (f) ran — and 311's instruction to "confirm the §4 lines appear in stdout" is UNSATISFIABLE, because (f) prints only on WARN and emits nothing on a conformant plan** (source read, `scripts/plan_lint.py:166-270`). **Discharged instead by a constructed positive control, run at walk 1: a copy of this draft with its closing line removed produced the expected missing-closing-line WARN, proving (f) executes. ⚠️ The WARN text is DESCRIBED rather than reproduced, per §3's reflexive rule.** Do not replace that control with a re-read of the exit code.

**Authoring self-check:** `plan_lint.py` run **at the deposit-path resolution** (`lessons-forge/knowledge/…`, so `project_root` resolves as it will at deposit — a lint from a scratchpad path declares a different state). **Exit 0; last run at deposit.** ⚠️ **The set is RE-MEASURED FOR THIS PLAN, not inherited from the six-step draft** — the step count, the test mentions and the ledger size all changed, so the parent's twenty-one cannot describe this artifact.

**The measured set is TWELVE, in four classes:**
1. **(2) the known-benign steps-mention-tests class** (Steps 1 and 2) — do NOT add test files to either step's scope to silence them.
2. **(1) `T2 plan missing cold-panel line`** — **EARNED.** The canonical panel line opens with the bolded keyword the check anchors on, which would satisfy §4 by wording while the panel has not run; this plan's line is deliberately phrased so it cannot match. The offending form is DESCRIBED, never reproduced. It clears only by convening the panel.
3. **(1) `closing indicates fold as last event`** — **EARNED and correct.** The Closing declares plainly that this is neither a dry close nor a bar-meeting judged stop; the WARN says the same thing the Closing says.
4. **(8) check (p), constraints carrying no backtick-quoted check token** — the prose invariants of the trimmed ledger. C10, C12 and C18 carry `Check:` tokens and do not warn.

⚠️ **A clean exit is NOT evidence the §4 block ran** — check (f) prints only on WARN, so silence on a conformant plan is correct, and the discharge is a constructed positive control, never an absence. ⚠️ **After any edit touching the ledger, the Cycle Log or the Closing line, re-run the linter and DIFF the WARN set against these twelve — never re-read the count.** A WARN can DISAPPEAR when a stale record silences a live gate, and a disappearance is invisible to anything but the comparison.
4. **(1) `Drafting Cycle closing indicates fold as last event, not a dry lens pass`** — **earned and correct while the last event is a fold**, which is §3's healthy direction during an open cycle. It clears only on a dry confirming pass, never by rewording the Closing line.

⚠️⚠️ **This figure decays faster than the artifact — re-run the linter and DIFF the WARN set against its prior state after any fold touching the Cycle Log, the ledger, a step's test mentions, or the Closing line. Never re-read the count instead.** A WARN can DISAPPEAR when a stale record silences a live gate, and a disappearance is invisible to anything but the comparison. **Both corrections came from re-running the linter and DIFFING the WARN set, and neither would have been visible by re-reading the number.** Any later fold touching the Cycle Log, the ledger, a step's test mentions, or the Closing line re-runs the linter and re-diffs before this figure is trusted.

**Deposit-once discipline:** to be deposited exactly once (`knowledge/decisions/` enumerated this session; holds `Done/` and `halted-executable-334.md` only). ⚠️ **`339` was read from `id_sequence` at authoring as a PREDICTION and has been RE-VERIFIED AT DEPOSIT — the clause fired and the outcome is recorded rather than assumed: `id_sequence` = 339 and `MAX(plans.id)` = 338 at the deposit read, so the prediction held and no site needed re-tokening. All thirteen `339` occurrences were enumerated and checked individually; four name the parent draft's filename, four the backup/resume-glob token, the rest this clause and the dispatch note.** ⚠️⚠️ **Sites carrying it, MEASURED rather than listed from memory — there are exactly TWO in the body:** the backup filename token `-339-` (Step 1a) and the Step-5 copy-aside token `lessons-report-pre-regen-339-`. **The deposit filename is the third, and it is outside the body.** ⚠️ **An earlier draft of this clause named seven site classes and five of them do not carry the id at all** — the title, the dev-log filenames, the report filename, and the QA report and evidence directory paths are all date-stamped, not id-stamped. That is the failure batch entry 269 warns about precisely: the clause works only if the enumeration is right, and an over-broad list is as useless as a bare "verify the id". **Re-read `id_sequence` at deposit and re-token EXACTLY THESE FOUR SITES before copying in: the front-matter backup/resume-glob token (finding 9's `-339-`), the front-matter dispatch note and Step 1a's backup filename token — plus the deposit filename itself.** ⚠️ **The front-matter site carries no "if the actual id differs, use the ACTUAL id" qualifier where Steps 1a and 5 both do, so an id change at deposit would leave the front-matter guard and the step instructions disagreeing.** An earlier draft of this clause ordered a re-token of "all seven site classes" while its own corrected enumeration named two — the correction was appended and the instruction it corrected was left standing.

---


## STEP 1 — Lessons Agent (ingest the whole corpus; NO classification anywhere in this plan)

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Forge Lessons Agent. Read `agents/FORGE_LESSONS_AGENT.md` first. **Its DB paths are relative and you may run in a worktree** — **every canonical-DB access uses the ABSOLUTE path** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`. **`forge/forge.db` is a REAL but DIFFERENT database — never open it.**
>
> **Working location — the plan-225 trap.** Run from your own working tree and write every file there; the ONLY exception is canonical-DB access by the absolute path above. Do NOT `cd` to the main tree.
>
> **⚠️ EXECUTION ORDER — exactly this sequence; gates are documented after Step 1b but two run BEFORE it:**
> 1. **Step 0 — determine dispatch state.**
> 2. **Step 1a** — restore point, verify it, capture the baseline + `E0`/`P0` + the `NT` set.
> 3. **Step 1a-ter** — write + `git commit` the pre-ingest anchor stub.
> 4. **Step 1a-bis** — pre-ingest hash guard (read-only) + the `detect_duplicates` pre-check.
> 5. **G2** then **G1** — both pre-ingest. G1 is the last thing before the mutation.
> 6. **Step 1b** — the ingest (the only mutation), `conn.commit()`, append the returned dict to the stub, commit it again.
> 7. **G3, G4, G5, G6** — post-mutation detectors reading the Step-1b dict.
> 8. **Write the ONE deposit (the dev log)** and `git commit` it by explicit pathspec.
>
> ⚠️ **NO CLASSIFICATION IN THIS STEP.** `get_unclassified_entries()` returning the full 41-id work list is this step's — and this PLAN's — CORRECT closing state, not unfinished work. **Plan B consumes that work list.**
>
> **Step 0 — DETERMINE DISPATCH STATE FIRST.** ⚠️ C8 applies to all probes: capture and report each probe's exit code; a FRESH determination read from silence is not a determination. Probe THREE places:
> 1. `git -C <your worktree> show HEAD:knowledge/development/dev-log-cycle-step-1-2026-08-10.md`
> 2. the working tree
> 3. `git log --all` on that path **and** `git -C /Users/marklehn/Developer/GitHub/lessons-forge branch --list 'bellows-preserved/*'`
>
> ⚠️ **Probe 3's exit code carries NO signal — `git log --all -- <path>` exits 0 on empty output for a real path and a typo'd path alike. Pair it with a positive control: run the same form against a path known committed (e.g. `knowledge/FORWARD.md`) and confirm output appears; only then is its silence a no-hit.** A hit on ANY → RESUME (recover the stub; its recorded values are authoritative for the whole step). Absent from all three → FRESH. State the determination and evidence as the first line of your dev log.
>
> **Single-writer assumption.** ⚠️ C8: capture exit codes; report literal counts. Before Step 1a, confirm no concurrent cycle:
> 1. `get_unclassified_entries` stable across two reads a moment apart.
> 2. Glob `in-progress-*.md` in the MAIN tree by absolute path — `ls /Users/marklehn/Developer/GitHub/lessons-forge/knowledge/decisions/in-progress-*.md` — NOT your worktree's frozen snapshot.
>
> ⚠️ **Under bellows dispatch this plan's own renamed `in-progress-*` file SHOULD be present in the main tree — so ZERO matches is evidence the PROBE is broken (wrong path or glob), not evidence of no concurrency (C8): re-verify the path before accepting a zero.** One match (this plan's own file) is the normal state; any OTHER match: read its title and HALT if it is a lessons/cycle plan.
>
> **⚠️ HALT DURABILITY — every HALT in this step:** commit whatever deposit files exist by EXPLICIT PATHSPEC before stopping; record which gate halted, its measured value, and whether the ingest had committed — **and, on a G6 halt specifically, the candidate section AND the arithmetic ingested-entry anchor** (their readers run on the approved continuation).
>
> **⚠️ DO NOT REPAIR. You hold the write handle.** Authorized writes: the `.backup`, `run_full_lessons_cycle`, and this step's deposit files. Nothing else. (No `insert_proposal` anywhere in this plan.)
>
> **Scope:**
> - `knowledge/development/dev-log-cycle-step-1-2026-08-10.md`
>
> ### Step 1a — restore point, then baseline
>
> Back up canonical with `.backup` (NOT `cp` — a live WAL exists), to the MAIN tree by absolute path, path built in a shell variable first:
> ```
> mkdir -p /Users/marklehn/Developer/GitHub/lessons-forge/data/backups
> BK="/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-cycle-339-$(date -u +%Y%m%dT%H%M%SZ).db"
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '$BK'"
> ```
> ⚠️ Do NOT inline `$(date …)` between single-quoted parts of the `.backup` argument (sqlite3 misparses; no backup written). ⚠️ **`339` in the filename is the plan id verified at deposit — if this plan's actual id differs at claim, use the ACTUAL id and record it; the id token is the resume-glob guard.** `.gitignore` matches `*.db` — confirm absent from porcelain.
>
> **VERIFY the restore point is real:**
> 1. `sqlite3 '<backup>' 'PRAGMA integrity_check;'` returns `ok`.
> 2. The backup's `COUNT(*)` for both tables equals the LIVE DB's counts at backup time — on a fresh run **265 entries / 273 proposals**; **on a RESUME the live DB is already mutated and the fresh backup correctly snapshots that — do NOT assert 265/273 on a resume.**
>
> Any failure → HALT before the ingest. ⚠️ **Read a backup with `?immutable=1`, not `?mode=ro`** — `.backup` writes the file alone; the sidecars appear only after our own integrity check opens it read-write; `?mode=ro` fails on the WAL header when sidecars are absent, `?immutable=1` is correct in both states.
>
> ⚠️⚠️ **THE RESUME GLOB IS CYCLE-UNIQUE:**
> 1. Match on the `-339-` (or actual-id) token.
> 2. End the glob in `.db` (a `-wal` sidecar errors sqlite3).
> 3. Take the EARLIEST match.
> 4. **PROVE it is this cycle's pristine snapshot: `SELECT MAX(id) FROM lesson_entries` must be 265 and proposals 273** (the `-311-` snapshot returns 214/222 and is thereby distinguishable).
> 5. **Derive the date from the actual filename or the receipt, never the local dispatch date** — `date -u` after ~18:00 local rolls the day. Prefer the exact path in the Step-1 Receipt (item 7).
>
> The glob population is 9 `.db` files at authoring and the count is NOT the guard.
>
> **Capture the baseline** (read-only), verbatim raw output:
> 1. Proposals by `status` **using a zero-emitting form** (LEFT JOIN/COALESCE over the enumerated status list, so every legal status prints a number — `GROUP BY` omits empty buckets and `proposed` is expected ABSENT at baseline). Planner measured: implemented 171 · superseded 28 · rejected 15 · **accepted 42** · reference 14 · stale 3, total 273. ⚠️⚠️ **The zero-emitting form enumerates ALL EIGHT schema statuses — proposed, accepted, rejected, ambiguous, stale, superseded, implemented, reference — and the six-value list above is the MEASURED result, not the enumeration.** `proposed` and `ambiguous` are both absent at baseline and must each print a zero. **Record `SURFACEABLE_BASE = proposed + ambiguous` as its own labelled line** — **Plan B's report step reads it**, cannot re-derive it once proposals exist, and forbids any fallback — so it must survive this plan in a committed artifact.
> 2. Proposals by `category`.
> 3. Total `lesson_entries`.
> 4. **The sentinel — entry 265, hash `c30fdaff226570c030e544648af0bc6096ff633452795387abada9d00a07fa83`, named by id, never derived from `MAX(id)`** (confirm against your own read; mismatch = HALT, not correction).
> 5. **`STALE_COUNT` (Planner measured: 3 — proposals 98, 121, 130) as its own labelled line.**
>
> **Capture `E0 = MAX(id) FROM lesson_entries` and `P0 = MAX(id) FROM lesson_proposals`. Confirm `E0 = 265`, `P0 = 273` on a fresh run; differing → HALT — but do NOT halt with the wrong diagnosis:** a "fresh" determination finding `E0 = 306` almost certainly means a prior dispatch's ingest landed with its record on a `bellows-preserved/*` branch (step 0 probe 3). Search those branches for the stub before reporting the first-dispatch ingest dict lost — it is one of the plan's unreproducible values.
>
> **⚠️⚠️ Capture THE NON-TERMINAL SET — by STATUS PREDICATE, never hardcoded ids:**
> ```sql
> SELECT p.id, p.entry_id, p.status, p.route, p.target_artifact, e.source_heading
> FROM lesson_proposals p JOIN lesson_entries e ON p.entry_id = e.id
> WHERE p.status IN ('proposed','accepted','ambiguous') ORDER BY p.id;
> ```
> Label it **`NT`**, deposit as RAW output.
>
> ⚠️⚠️ **`NT` HAS EXACTLY ONE DEFINITION IN THIS PLAN AND IT IS THIS PREDICATE: `status IN ('proposed','accepted','ambiguous')`. `NT_COUNT` = **42** on a FRESH run** — the 42 `accepted|codify` rows (21 `DRAFTING_CYCLE.md`, 21 `PLANNER_TEMPLATE.md`), with `proposed` and `ambiguous` both empty at baseline. **The 3 `stale` rows are NOT in `NT` and are never counted into it**; they are reported separately as `STALE_COUNT`. ⚠️ **Never sum `NT_COUNT` and `STALE_COUNT` into one non-terminal figure.** An earlier draft carried such a figure in the front matter and this sentence existed to disambiguate it; that figure is gone, and the only live `45` tokens in this plan are **FORWARD 45** — a different namespace. **No gate in this plan ever compares against 45.** Report `NT_COUNT=42` and `STALE_COUNT=3` as two labelled lines and never a sum.
>
> ⚠️⚠️ **Empty stdout is NOT evidence of an empty set** — also run the count form and record the printed token:
> ```
> sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" \
>   "SELECT 'NT_COUNT=' || COUNT(*) FROM lesson_proposals WHERE status IN ('proposed','accepted','ambiguous');"
> ```
> Prints a non-empty token on success in BOTH cases; silence = broken invocation → HALT. **CAPTURE ONLY — G1 owns the verdict.**
>
> ### ⚠️ Step 1a-ter — COMMIT THE BEFORE-ANCHOR BEFORE THE INGEST
>
> After the restore point verifies and before `run_full_lessons_cycle`, write and `git commit` a stub `knowledge/development/dev-log-cycle-step-1-2026-08-10.md` containing:
> 1. `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)` — never a downstream proceed-value.
> 2. The absolute pristine backup path.
> 3. `E0`, `P0`.
> 4. The raw `NT` capture + the printed `NT_COUNT=` line (never overwrite an existing stub's `NT`).
> 5. `STALE_COUNT=`.
> 6. The entry-265 sentinel hash.
> 6b. **`SURFACEABLE_BASE=`** (the `proposed + ambiguous` baseline) and the **zero-emitting status/category distribution** — both pre-ingest-only, both read by later steps, neither recoverable after the ingest.
> 7. ⚠️⚠️ **The three DOCTRINE PINS — THE ONLY PLACE THEY ARE EVER MEASURED.** `shasum -a 256` on `/Users/marklehn/Developer/GitHub/{DRAFTING_CYCLE.md,PLANNER_TEMPLATE.md,RULE_20_SELF_CHECK_BLOCK.md}`, raw output into this stub. G2 and Receipt item 10 CITE this capture; neither re-measures. **HALT unless all three hashes are present with the expected filenames** — `shasum` on a missing file prints nothing and exits non-zero (C8).
>
> ⚠️⚠️ **THE OVERWRITE RULE:** the final Receipt rewrites this file in place but MUST carry any recorded first-dispatch ingest dict forward verbatim under `#### First-dispatch ingest dict` — a resume's re-run correctly returns all-zero counts and must not replace the first dispatch's real ones. If the stub exists on a resume, its recorded values are authoritative over anything you re-measure now.
>
> ### Step 1a-bis — PRE-INGEST hash guard (read-only; the guard, where G4 is only the detector)
>
> 1. From your working tree: `import sys; sys.path.insert(0, "src")`; `from lessons_forge import parse_lessons_md`; `entries = parse_lessons_md("/Users/marklehn/Developer/GitHub/LESSONS.md")` — the same parser the ingest calls. **While you hold all parsed entries, tally the whole-corpus dry run:** per entry, look up `source_heading` in `lesson_entries`; count `would_insert` / `would_update` / `unchanged`. ⚠️⚠️ **BRANCH ON THE STEP-0 DETERMINATION:**
>    - **FRESH → assert `would_insert == 41` AND `would_update == 0`.** Deviation → HALT pre-mutation. (Planner measured 41 / 0 / 208 over 249 parsed.)
>    - **RESUME → assert `would_update == 0`** and **`would_insert ∈ {0, 41}`** — anything in 1..40 means a partially-landed insert set, impossible from this plan's single transaction → foreign writer → HALT.
>
>    ⚠️⚠️ **`would_update == 0` IS THIS PLAN'S LOAD-BEARING GUARD, and it is load-bearing in a way it was not for plan 311.** 311 could tolerate a hash flip because its non-terminal set was empty. Here a flip on ANY entry carrying a non-terminal proposal stales it, and 42 of those are the queued Gate-2 batch — 21 of them the `DRAFTING_CYCLE.md` proposals this cycle exists to unblock. **On any non-zero `would_update`: HALT, name every affected heading, and state which of the 42 would have been staled. Do not proceed on a judgement that the flip looks cosmetic.**
>
>    ⚠️ A root `LESSONS.md` commit between authoring and dispatch is PERMITTED (G2 treats the HEAD delta as reconcile-only) — a 42nd appended lesson landing BEFORE this check runs is exactly what it catches pre-mutation. ⚠️ **Scope stated honestly: an append committed in the minutes BETWEEN this check and Step 1b passes G2 and INGESTS** — caught post-commit by G5's ∉{0,41} and G6, with the verified backup bounding the blast radius. The pre-commit guard is best-effort over its window, not absolute.
>
> 1b. ⚠️⚠️ **THE BATCH FINGERPRINT — the guard the count checks structurally cannot supply.** `would_insert == 41` is satisfied by ANY 41 new entries. If three lessons were appended and three others reworded between authoring and dispatch, `would_insert` is still 41 and `would_update` still 0 — **the counts pass, and every id-bearing table in Plan B (the scout, the tranche map, the cluster lists) and this plan's shell-hostile list then misattributes silently, because each binds a substance to a position.** Compute, over the would-INSERT headings **in parse order** (the order the ids are assigned in):
>    ```
>    hashlib.sha256("\n".join(<the would-insert source_headings>).encode("utf-8")).hexdigest()
>    ```
>    **Expected: `2eec5d56e20cb29e9e1925e1f9d64f346033627f0aa3f3d3efa57cdb96e6a1a7`** (Planner measured at authoring). Also print the first and last heading.
>
>    ⚠️⚠️ **BRANCH ON THE STEP-0 DETERMINATION — this check is UNREACHABLE-SAFE only on a FRESH run, and an unbranched form breaks the plan's own resume path:**
>    - **FRESH, or RESUME with `would_insert == 41`** → compute the digest and compare. **Mismatch → HALT: the batch is not the batch this plan scouted, regardless of what the counts say. Do not proceed on a judgement that the difference looks small — the scout is positional, so a single insertion shifts every entry id after it.**
>    - **RESUME with `would_insert == 0`** (the ingest landed and the step died before depositing) → **the would-insert list is EMPTY and its digest is `sha256("")` = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, which is not and can never be the expected value. SKIP the comparison and record `FINGERPRINT=n/a (post-ingest resume, would_insert=0)`.**
>
>    ⚠️⚠️ **An unbranched HALT here makes BOTH of G5's completion arms unreachable** — arm 2 (idempotent re-dispatch) and arm 3 (deposit-completion) are keyed on `ingested_count == 0`, which is only observed in Step 1b, and Step 1b never runs if 1a-bis halts first. **Arm 3 is the sole recovery path for the first-dispatch ingest dict, one of the plan's unreproducible values.** Item 1 immediately above carries a resume arm; this check did not, and the omission fails a permitted outcome (C5) and states a fresh-run expectation without its dispatch qualifier (C7).
>
>    ⚠️ **This bound can fail, and the failing input was constructed at authoring rather than argued** (C12): swapping one of the 41 headings for a different one holds the count at 41 and moves the digest to `9b2f8df5…`. The count check passes on that input; this one does not.
>
>    ⚠️ A mismatch is **not** automatically corruption — it is the expected result if `LESSONS.md` legitimately gained a lesson since authoring. The HALT is correct either way: the CEO re-parameterizes Plan B's tranche arithmetic and scout, or reverts the append. **This is the same fail-closed batch pin 311 declared, keyed on content instead of on a count.**
>
> 2. **The sentinel — entry 265.** Find the parsed entry whose `source_heading` equals entry 265's; compare computed vs stored `c30fdaff…`.
>    - Exactly 1 match + equal → PASS.
>    - 1 match + different → HALT (classify whitespace-only = plan-204 regression vs substantive).
>    - 0 matches → HALT (its heading was edited).
>    - >1 → HALT (ambiguous lookup).
>
>    ⚠️ **Note the difference from 311: entry 265 is no longer the LAST entry in the file, so the trailing-separator trap cannot reach it.** It is a regression sentinel for `_normalize_for_hash`, not a live-hazard canary. A mismatch here means something rewrote history.
>
> 3. **The duplicate-detector pre-check — BOTH paths, reported separately:**
>    - **(a) Pre-existing ids:** mirror the ingest's own candidate construction (parsed-and-matched headings — Planner measured **208** ids, not all 265; orphans are never handed to the detector). **PRINT THE LIST LENGTH BEFORE CALLING; HALT if 0 or wildly off 208** — the function's first statement is an empty-list early return AHEAD of the reference-file read, so an empty list returns "no duplicates" having examined nothing while the positive control stays green. Run `detect_duplicates(conn, <ids>)` read-only. Non-empty → HALT.
>    - **(b) This cycle's 41 parsed entries** (no ids yet — replicate the detector's CURRENT source read-only; the code is authoritative, not this plan's description). Reference file at the ABSOLUTE path `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (absent from your worktree; a relative read yields nothing and nothing looks clean). Both criteria in code order: tag overlap first, then the `_EM_DASH_SEP` title-substring. ⚠️⚠️ **Report criterion 1's zero as UNFALSIFIABLE, not as an observation:** the reference file carries no `**Tag:**`/`**Tags:**` lines, so its tag set is empty and criterion 1 returns zero for every possible input — the code's own docstring calls this a clean no-op. **The positive control below validates criterion 2 only.** Saying "criterion 1: 0 hits (inert — reference carries no tag lines)" is the honest report; saying "0 hits" alone claims an observation that was never made (**24 of 41 headings carry the separator; the other 17 test the whole dated heading**). Any hit → HALT.
>
>    ⚠️⚠️ **POSITIVE CONTROL before trusting any zero (the reference read fails SILENT):** read the reference file yourself by the absolute path, and **from that ONE read** record (i) byte length and (ii) the sentinel searched in the in-memory string — ⚠️⚠️ **and the sentinel MUST be lowercase (`orchestration plan rules`), because the detector lowercases its read (`result.stdout.lower()`, `src/lessons_forge.py:345`) and this control replicates the detector.** A cased literal against that string can never match, so the control would report a false absence and void a correct zero-hit result, halting pre-mutation — batch entry 303's class, committed on the control that exists to prevent it. **If you instead read the file RAW for the control, say so explicitly and use the cased form; what is forbidden is a cased probe against a lowered string.** Both facts from the SAME read; a separate `grep` proves existence, not that the feeding read succeeded. Zero length or missing sentinel → every zero-hit result is void → HALT. ⚠️ **The byte length is deliberately NOT pinned to a Planner literal here: `PLANNER_TEMPLATE.md` is a live governance file and its length moves between authoring and dispatch. Record the measured length; the sentinel is the pass condition.**
>
> 4. Record `Step 1a-bis: would_insert/would_update/unchanged actuals; NT_COUNT=<the value you captured>; sentinel check performed` — transcribe measured numbers, never a pre-composed "empty" string.
>
> ### Step 1b — run the ingest (ONCE, this step only)
>
> Open canonical read-WRITE (plain `sqlite3.connect(...)`). **Call `run_full_lessons_cycle(conn, lessons_md_path="/Users/marklehn/Developer/GitHub/LESSONS.md")` — path EXPLICIT, printed.** `conn.commit()` after it returns (the DB is gitignored; a step death without commit loses the ingest). ⚠️ **Then IMMEDIATELY append the verbatim returned dict to the stub and `git commit` it again — the ingest dict is one of the plan's unreproducible values (see Receipt item 5b).** Print all SEVEN keys: `ingested_count`, `updated_count`, `unchanged_count`, `duplicates_marked_count`, `terminal_proposals_flagged`, `needs_classification`, `cycle_timestamp`.
>
> ⚠️ **What the function does — VERIFIED BY SOURCE READ at authoring (`src/lessons_forge.py:416-511`), not inherited:** it parses, ingests, builds `candidate_ids` from parsed-and-matched headings, runs `detect_duplicates`, **INSERTS a `duplicate` proposal per hit** (idempotent on `entry_id`+`category`), and returns `get_unclassified_entries` — **it does NOT classify. Make exactly this call — do NOT substitute lower-level calls.** Re-verify the function still matches this description against the live source before running; if it has changed in a way that classifies or mutates beyond the above → HALT and report.
>
> ### Step 1 gates — G1 through G6 (report EVERY one as a table row: measured value + PASS/HALT; run all before halting)
>
> - **⚠️⚠️ G1 — the non-terminal precondition, REBUILT FOR A NON-EMPTY `NT`.** 311's arms tested `NT_COUNT == 0` and are all unreachable here; do not carry them. Capture BOTH printed numbers: `NT_COUNT` and `STALE_COUNT`. `stale` belongs to NEITHER partition, so a staled row VANISHES from `NT` — hence the pair. `STALE_BASE` = 3 on FRESH (mismatch → HALT); on RESUME = the stub's recorded value, never a live re-read (C4).
>
>   Arms evaluate IN ORDER, first match wins:
>   1. **`NT_COUNT == 42` AND every one of those 42 is `status='accepted'` AND `route='codify'` AND `STALE_COUNT == STALE_BASE`** → FRESH → PASS. ⚠️ The composition conjunct is load-bearing: a bare count of 42 is also satisfiable by a corpus where some accepted rows were staled and an equal number of this cycle's proposals were inserted. **Assert the composition, not the count.**
>   2. **`NT_COUNT == 42 + n` where `1 ≤ n ≤ 41`, every ADDITIONAL proposal has `entry_id > 265`, the original 42 are intact by id, AND `STALE_COUNT == STALE_BASE`, AND step 0 said RESUME** → `PASS (resume)`. Step 0 FRESH + this condition → CONTRADICTION → HALT. `n > 41` → HALT regardless.
>   3. **Any of the recorded 42 `accepted|codify` proposals missing, or moved to any other status** → premise VOID → HALT before the ingest; report every id and its new status; name the pristine `.backup`. ⚠️ **This is the arm that protects the Gate-2 queue and it has never executed. It is the reason this gate was rewritten rather than cloned.**
>   4. **Any non-terminal proposal with `entry_id ≤ 265` that is NOT one of the 42** → an unexpected non-terminal row → HALT; report every id.
>   4b. ⚠️⚠️ **WINDOW-0 CARVE-OUT (deposit → this gate), the one window with no causal arm until now:** a Gate-2 codification landing between authoring and dispatch gives `NT_COUNT = 42−k` and would fire arm 3, yet it is legitimate. **If the missing ids are `implemented` with `route` still `codify` and `status_updated_by='ceo'` → record + CONTINUE, carrying the adjusted expectation to every later step.** ⚠️ The in-window timestamp conjunct Plan B's steps use CANNOT apply here — its lower bound is the ingest's own `cycle_timestamp`, which does not yet exist — so this arm rests on status, route and actor alone, and says so.
>   5. **`STALE_COUNT != STALE_BASE` (either direction)** → HALT.
>
>   ⚠️ A pre-ingest-death resume (nothing mutated yet) legitimately matches arm 1: when step 0 said RESUME, record it as `PASS (resume, pre-mutation)`, not as FRESH.
>
> - **G2 — `LESSONS.md` provenance.** `git -C /Users/marklehn/Developer/GitHub status --porcelain -- LESSONS.md; echo "PORCELAIN-EXIT=$?"` — non-zero exit → HALT (check did not run); **non-empty output → HALT before the ingest** (do not ingest an uncommitted corpus; this is the ONE working-tree signal in this plan that halts). Record `git -C <root> rev-parse --short HEAD` (Planner measured `ad3c2d7`) — **a HEAD mismatch is a reconcile-note, NOT a halt, and is near-certain by dispatch time.** G2 CITES the stub's doctrine pins (confirm three hashes are recorded there); it does not re-measure them.
> - **G3 — `duplicates_marked_count == 0`.** Non-zero → HALT, naming entry ids. On a RESUME assert the SCOPED form only: `SELECT 'DUP_IN_BATCH=' || COUNT(*) FROM lesson_proposals WHERE category='duplicate' AND entry_id > 265;` (whole-corpus `DUP_COUNT` is 19 by baseline and would false-HALT — C9 discipline; `entry_id > 265` is legal HERE because Step 1 holds the write handle and creates the ids). Non-zero → HALT even with a zero dict count. ⚠️ **A zero is NOT self-validating — G3 passes identically when the detector read nothing.** Discharge ONLY against Step 1a-bis's positive control; control absent/failed → report `HALT (unverified)`. Do not re-run the detector to resolve it.
> - **G4 — `updated_count == 0` AND `terminal_proposals_flagged` empty.** Non-zero either way → HALT; show the diff; classify whitespace-only (plan-204 regression) vs substantive. G4 is a DETECTOR (the staling UPDATE already ran inside the ingest; the return dict omits `stale_proposals_marked`) — on failure query `status='stale'` directly and diff against the stub baseline; name the `.backup` as recovery point. ⚠️ **Here G4's failure mode has teeth 311's did not: with 42 unprotected accepted rows, a non-zero `updated_count` may mean the Gate-2 queue is already damaged. Query the 42 by id before anything else.**
> - **G5 — there is work to do, keyed on `ingested_count` + the Receipt state:**
>   1. `ingested_count == 41` → FRESH → PASS.
>   2. `ingested_count == 0` + a `Status: Complete` receipt on record (DB-confirm first: `SELECT COUNT(*) FROM lesson_entries WHERE id > 265` == 41) → **idempotent re-dispatch:** APPEND a `### Re-dispatch note`, set `Status: Complete (idempotent re-dispatch — no work required)`, commit, stop — never overwrite a Complete receipt with a halt record.
>   3. `ingested_count == 0` + the receipt still the in-flight stub, or absent → **deposit-completion resume:** regenerate the Receipt from the DB **and the stub** — the 41-id INGESTED-ENTRY list (`SELECT id FROM lesson_entries WHERE id > 265 ORDER BY id`; HALT unless exactly 41 rows, with the G6-deferral variant per the Self-report), the first-dispatch ingest dict verbatim from the stub (absent → say so; this plan's QA row 4 then `❌ (unverifiable)`), `#### Doctrine pins` copied from the stub (never re-run `shasum`), `E0`/`P0`/backup path/sentinel/`STALE_COUNT`, **the raw `NT` capture and the 42-id `accepted|codify` list derived from it (Receipt item 5 — its sole source after the ingest; a live predicate re-read is forbidden by name), `SURFACEABLE_BASE` (item 5b) and the baseline status/category distribution (item 3)** — all likewise from the stub (C4). Then END the step. ⚠️ **Every one of these must therefore BE in the stub; Step 1a-ter is the producer and this is its consumer.**
>   4. **`ingested_count` ∉ {0, 41} → HALT.**
>
>   ⚠️ `needs_classification` is NOT this gate's key: it legitimately holds the full 41 in every Step-1-complete state until Plan B runs. G6 owns the list.
> - **G6 — work-list reconciliation.** Batch range = `E0+1 .. E0+41` (= 266–306, computed arithmetically from the CONFIRMED `E0`, never from `needs_classification` itself, and the bound is 41 because THIS batch is 41). **Invariant: every id in `needs_classification` is `> E0` and `≤ E0+41`.** Any id outside → HALT → CEO chooses: **(i) ingest batch+extra — ⚠️ this changes the id range Plan B's tranche arithmetic is built on, so Plan B must be re-parameterized before it is authored**; (ii) batch only, extras deferred — Plan B absorbs the deferral; (iii) investigate.
>
>   ⚠️⚠️ **THE HALTING AGENT WRITES THE CANDIDATE:** when this gate halts on outside-range ids, write into the Receipt a section headed exactly **`### Deferred entries (G6 candidate)`** listing the EXACT measured outside-range ids (one per line, bare — never a range), with the body line: *"APPROVAL = a CEO continue verdict on this G6 halt; absent that verdict this section is void."* The body ALSO records the standing cost: *deferred ids remain unclassified indefinitely and will re-trip every future cycle's G6 until dispositioned.* **AND produce the INGESTED-ENTRY ANCHOR in the same halted Receipt: the 41-line list derived ARITHMETICALLY as `E0+1 .. E0+41`; the outside-range extras are the candidate ids, named in the candidate section, NEVER in the anchor.** FRESH → the list is EXACTLY the 41; fewer → HALT.
>
> **After the gate table: all PASS → write the deposit and END THE STEP. Any HALT — stop and report, having run the remaining gates; the ingest stays committed.**
>
> **Self-report — the 41-entry INGESTED-ID ANCHOR is created here.** Print `SELECT id, source_heading FROM lesson_entries WHERE id > 265 ORDER BY id` — expect **41 rows (266–306)**. ⚠️ **In the G6-deferral state this query returns 41 + |candidate| rows: the ANCHOR is the arithmetic batch `E0+1..E0+41` — 41 lines — and the extras must equal the candidate ids EXACTLY (else HALT).** Any other deviation → no anchor, HALT. Record in the Receipt as a fixed-format list, one line per entry, values bare, no `|`: **`- ingested entry=<id>`**. Confirm `get_unclassified_entries()` returns exactly those 41 ids and record the list verbatim.
>
> **The Receipt opens with a status line from the CLOSED SET:** `Status: Complete` · `Status: Complete (idempotent re-dispatch — no work required)` · `Status: Partial — HALTED at <gate>, <reason>` · `Status: Partial — in flight (pre-ingest stub; superseded by the final Receipt)`. It carries, each on its own labelled line:
> 1. The cycle/ingest dict verbatim (+ `#### First-dispatch ingest dict` when a resume is in evidence).
> 2. The G1–G6 gate table.
> 3. The pre-cycle baseline (zero-emitting status distribution, category distribution, entry count, sentinel hash, `STALE_COUNT`).
> 4. `E0`/`P0`.
> 5b. **`SURFACEABLE_BASE=`** — the `proposed + ambiguous` count at baseline (Planner measured **0**), the sole operand for Plan B's surfaced-proposal expectation. ⚠️⚠️ **It is pre-ingest-only and therefore goes in the Step-1a-ter STUB as well as the Receipt, and G5 arm 3 regenerates it from the stub like `E0`/`P0`/`STALE_COUNT`.** Without a stub home it is unrecoverable on a deposit-completion resume, where C4 forbids a live re-read and Plan B's report step forbids a fallback — that run would stop on a correct path. **The same applies to Receipt item 3's baseline distribution, which QA row 4 reads.** ⚠️ **This also corrects a claim made twice elsewhere in this plan: the ingest dict is NOT the only unreproducible value — these two are as well.**
> 5. The `NT` capture (+`NT-original`/`NT-now` labels on a resume; `NT-original` is the before-anchor downstream readers take) — **including the explicit list of the 42 `accepted|codify` ids** — captured by the predicate `status='accepted' AND route='codify'`, never by a range. **This list is the sole operand for the Gate-2 id-for-id check at this plan's QA and at every step of Plan B; nothing else in the plan can reconstruct it after the ingest.**
> 6. The 41-line ingested-entry list.
> 7. The absolute backup path(s), labelled `pristine (pre-cycle)` (+ `this-dispatch (mid-cycle)` on resume).
> 8. `#### Files Created or Modified` split into `##### Committed deposits` / `##### Untracked artifacts` (the `.backup` + DB mutation are gitignored main-tree writes; one unsplit list rewards concealment).
> 9. Flags.
> 10. `#### Doctrine pins` — the stub's three hashes verbatim, never re-measured.
>
> ⚠️ Every measured value deposited as RAW COMMAND OUTPUT; annotate freely, never replace. Canonical Python file-write — no heredoc. Commit by explicit pathspec: `git add <paths>` then `git commit -m "…" -- <paths>` (**the pathspec on the COMMIT — a bare commit ships the whole index**). Post-commit assert: `git show --name-only --format= HEAD` prints exactly the intended paths, **and print `git rev-parse --show-toplevel` to assert WHERE it landed.** `#### Prompt Feedback` in `### Ledger Updates`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/dev-log-cycle-step-1-2026-08-10.md`

---
---


---
---

## STEP 2 — QA

---

> **Before starting: Step 1's Receipt status must be a PROCEED-value** (`Status: Complete` / `Status: Complete (idempotent re-dispatch — no work required)`) — an ALLOWLIST, not a prefix match. **ONE exception:** the G6-deferral state (`Status: Partial — HALTED at G6, …` matched on the `HALTED at G6` token) WHEN the Receipt carries a `### Deferred entries (G6 candidate)` section — under bellows a halted step advances only on a CEO verdict, so THIS STEP RUNNING is the approval of that candidate; state that reasoning in your dev log and open both your chat message and your report with `OPERATING UNDER G6 DEFERRAL: ids <list> — if the continue verdict did not intend deferral, issue a stop now.`
>
> Post a short visible chat message. You are Lessons Forge QA (`agents/FORGE_LESSONS_AGENT.md`). Run from your own working tree; every canonical-DB access uses the ABSOLUTE path `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`, **read-only** (`?mode=ro`). **Verification + reporting only — a failing check is reported, never fixed. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly. Do NOT classify anything.**
>
> **MANDATORY — Rule 20 self-check (canonical block, exact template, four placeholders):** run from `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md` (ABSOLUTE path — governance root, not your worktree):
> - `plan_slug`: `cycle-ingest-session-24-33-2026-08-10`
> - `qa_report_path`: `<your-own-tree-abs>/knowledge/qa/cycle-ingest-qa-2026-08-10.md`
> - `evidence_dir`: `<your-own-tree-abs>/knowledge/qa/evidence/cycle-ingest-session-24-33-2026-08-10/` (derive from `pwd`)
> - `required_evidence_files`: `["pytest_targeted.txt", "invariants.txt", "hash-trap.txt", "schema.txt"]`
>
> Deposit all four evidence files BEFORE the block (it `sys.exit(1)`s on missing/empty) — **and write the QA REPORT with its verification table BEFORE the block too: it `sys.exit(1)`s with a not-found CRITICAL if `qa_report_path` does not exist. Order: write report → run block → APPEND the stdout to the report.** The banner `Rule 20 — QA Self-Check Results` and the `PASSED — SELF-CHECK PASSED` line must appear verbatim in the deposited report (⚠️ **without** a `##` prefix — re-verify against the delivering code before relying on it; do not inherit this claim). End with a self-grep confirming the banner reached the deposited report. ⚠️ **The block verifies evidence-file presence and hedging keywords ONLY — it cannot see verdicts; expect PASSED even on an honest halt; never flip, soften or drop a row to keep it green.**
>
> **⚠️ Rule 19 — VERBATIM:** *"If you cannot complete a check, mark it ❌ with a reason. Do NOT mark it ✅ and explain why you couldn't verify. Any ✅ row containing hedging keywords will auto-fail during the self-check in Rule 20."*
>
> ⚠️⚠️ Hedging keywords are fatal even as measured values — write row 1's value as `<N> passed` and NOTHING else. ⚠️⚠️ No command containing `|` in a table cell (fenced block above the table; the row cites the result). ⚠️⚠️ The status column holds EXACTLY one glyph, `✅` or `❌` — no third value, no annotated glyph; a reconcile outcome is a `✅` with a note in the measured-value column. ⚠️ Close the `## Verification Table` section with `## Evidence and Narrative` immediately after the table — the gate's section flag never clears on `###`.
>
> **Scope:**
> - `knowledge/qa/cycle-ingest-qa-2026-08-10.md`
> - `knowledge/qa/evidence/cycle-ingest-session-24-33-2026-08-10/pytest_targeted.txt`
> - `knowledge/qa/evidence/cycle-ingest-session-24-33-2026-08-10/invariants.txt`
> - `knowledge/qa/evidence/cycle-ingest-session-24-33-2026-08-10/hash-trap.txt`
> - `knowledge/qa/evidence/cycle-ingest-session-24-33-2026-08-10/schema.txt`
>
> Table under exactly `## Verification Table`, columns `| # | Claim | Status (✅/❌) | Measured value | DB source | Evidence |`. **A failing row does not license skipping the rest — run all eight (0–7), then halt if owed; a HALT still leaves a committed record.**
>
> ⚠️⚠️ **THE IN-WINDOW RECONCILIATION RULE.** This plan has ONE gate window, which is the whole point of the split — but it is still arbitrary wall-clock time, so foreign writes remain possible. Every whole-corpus row adjudicates in two parts. **(a) HARD — the delta this plan owns, BY ID:** the 41 entry ids from Step 1's recorded ingested-entry anchor. Validate the list before querying — **41 integer values, none blank/NULL** (`NOT IN` is NULL-poisoned and fails silently toward "nothing found"; print `FOREIGN=` tokens); missing/truncated/unparseable → every dependent row `❌ (unverifiable)`, **NO predicate fallback** (`entry_id > 265` means "after authoring", not "ours"). **(b) RECONCILE — everything outside that id set:** report ids, note in the measured-value column, still `✅`.
>
> 0. **Deliverable verification (Rule 17) — scoped to the `##### Committed deposits` sub-list of Step 1's Receipt** (the `.backup` and the DB mutation live in `##### Untracked artifacts`: cross-check against the Receipt's labelled paths but never apply commit tests or fail the row on them). Per committed deposit, BOTH: `git log --oneline -1 -- <path>` (empty = FAILURE here — quote the printed commit line) AND `git status --porcelain -- <path>; echo "ROW0-PORCELAIN-EXIT=$?"` (empty + exit 0 = clean; non-zero exit = `❌`, never clean). Any ❌ → Critical, blocks Done.
> 1. **Targeted suite** — `python3 -m pytest src/ -v`, raw tail to `pytest_targeted.txt`. The whole of `src/` IS the complete run under `targeted` (one test file — measured); do not add a second run. Baseline from `--collect-only` reconciled against the most recent prior QA (Planner measured 55). Value cell: `<N> passed` only.
> 2. ⚠️⚠️ **`get_unclassified_entries(conn)` returns EXACTLY the 41 ids — NOT `[]`.** This inverts the expectation every prior cycle-run QA carried, and it is the single most likely place for an agent to apply a remembered rule: **an empty work list here means something classified this batch, which nothing in this plan is authorized to do.** Quote the printed result WITH a count token. Expected: the 41 ids of Step 1's anchor, id-for-id — **or exactly those 41 minus nothing plus the ids of a `### Deferred entries (G6 candidate)` section**, if Step 1 halted at G6 and was continued. `[]` → ❌ Critical. Any other set → ❌, cross-reference rows 3 and 4.
> 3. **The 41 entries landed, and only those.** `SELECT id, source_heading FROM lesson_entries WHERE id IN (<the 41>)` → 41 rows; each `source_heading` matches Step 1's anchor line for that id **by equality, bound as a query parameter** (⚠️ eleven of the 41 headings carry apostrophes, a double quote or literal backticks — never interpolate one into a shell string). Reconcile: `SELECT COUNT(*) FROM lesson_entries` — derivation `265 + 41 = 306`; above it, name the foreign ids and note, no ❌. Raw to `invariants.txt`.
> 4. **The plan-204 fix held, and NO proposal was created.** Baseline from Step 1's Receipt (missing → `❌ (unverifiable)`, the fail-closed backstop).
>    - `stale` not grown: before **3** (proposals 98/121/130), after printed.
>    - **entry 265's `content_hash` unchanged** (`c30fdaff…`).
>    - `updated_count` and `terminal_proposals_flagged` from the recorded ingest dict (`#### First-dispatch ingest dict` when a resume is in evidence).
>    - ⚠️⚠️ **`SELECT COUNT(*) FROM lesson_proposals` == 273, UNCHANGED.** This plan creates no proposals; `run_full_lessons_cycle` inserts a `duplicate` proposal per `detect_duplicates` hit, so **274 or more means the detector fired and G3 should have halted** — cross-check `duplicates_marked_count` and report both. This is a failable bound and its failing input is stated (C12).
>    - ⚠️⚠️ **A COUNT IS NOT A VALUE GUARD:** state the FULL zero-emitting status distribution before and after — `implemented` 171, `superseded` 28, `rejected` 15, **`accepted` 42**, `reference` 14, `stale` 3, `proposed` 0, `ambiguous` 0 — every bucket UNCHANGED (confirm against Step 1's Receipt item 3, not these literals). **Any bucket moving → ❌**, with the single carve-out that an in-window Gate-1 or Gate-2 disposition of a PRE-EXISTING proposal is adjudicated causally per row 7 and reported ✅ + note naming ids. State the count of proposals examined. Raw to `hash-trap.txt`.
> 5. **No schema drift** — semantic comparison (PRAGMA table_info + constraint set) vs `src/db.py` DDL; cosmetic RENAME artifacts are NOT drift. Raw `.schema` both tables → `schema.txt`.
> 6. **Doctrine unchanged — TWO NAMED SUB-CHECKS, both fail-closed, neither adjudicated by you.**
>    - **6a (this-window guard):**
>      ```
>      git -C /Users/marklehn/Developer/GitHub status --porcelain -- DRAFTING_CYCLE.md PLANNER_TEMPLATE.md RULE_20_SELF_CHECK_BLOCK.md; echo "PORCELAIN-EXIT=$?"
>      ```
>      BOTH pass conditions required: empty output AND exit 0 (`-C` is REQUIRED — from your worktree these files do not exist and a bare invocation passes vacuously). Non-zero exit → `❌ (check did not run)`, distinct from `❌ (doctrine changed)`. **Non-empty porcelain → ❌, full stop — attribution is the CEO's at the verdict gate, never yours:** capture `git log --oneline <recorded-HEAD>..HEAD -- <files>` + `git diff` into `invariants.txt` before halting.
>    - **6b (drift since authoring):** `shasum -a 256` the three files vs **Step 1 Receipt item 10**; item 10 absent/short → `❌ (unverifiable)`. Print all three live + all three recorded + three pairwise verdicts. Working-tree content pins, never `rev-parse HEAD:<path>` (blind to uncommitted edits).
> 7. ⚠️⚠️ **THE GATE-2 QUEUE SURVIVED — this plan's headline risk, and the row the whole split exists to protect.** `SELECT id, entry_id, status, route, target_artifact FROM lesson_proposals WHERE status='accepted' AND route='codify' ORDER BY id;` — compare **ID-FOR-ID against Step 1 Receipt item 5's recorded list, never a count** (a corpus that staled three and gained three foreign rows counts 42 and is not intact — C10). Print the count token and the symmetric difference **in both directions**. Expected: the recorded 42, exactly, 21 `DRAFTING_CYCLE.md` and 21 `PLANNER_TEMPLATE.md`.
>    - **Any of the 42 now `stale` → ❌ Critical**, naming ids and the pristine `.backup`. No adjudication — that state has no legitimate producer.
>    - **A recorded id now `implemented`** → legitimate in-window Gate-2 codification ONLY on all four conjuncts: `implemented` AND `route` still `codify` AND `status_updated_at` later than the recorded `cycle_timestamp` AND `status_updated_by='ceo'` → ✅ + note naming ids and the plan. ⚠️ **Compare timestamps LEXICOGRAPHICALLY IN SQL, never via `datetime.fromisoformat`** — the column carries two ISO dialects and this machine's Python 3.9.6 raises on the `Z` form. **Not** by the weaker "a Gate-2 plan is visible in `Done/`" test, which is satisfiable by history.
>    - **A live `accepted|codify` id absent from the recorded list → ❌ foreign writer** — this plan creates no proposals, so unlike the six-step version there is no carve-out to make here.
>    - Anything else → ❌ Critical. Raw to `invariants.txt`.
>
> **Evidence routing:** rows 0/2/3/6/7 → `invariants.txt`; row 4 → `hash-trap.txt`; row 5 → `schema.txt`; row 1 tail → `pytest_targeted.txt`. Before the Rule 20 block runs, self-grep each file for a content marker (`PORCELAIN-EXIT=` in invariants; the `c30fdaff` prefix in hash-trap; `CREATE TABLE` in schema; the pytest summary line in pytest_targeted) with `grep -F`, **printing what matched, not PRESENT/ABSENT** — the block only checks non-empty and a one-byte file passes it.
>
> **Deposit:** the QA report + the four evidence files. Canonical Python file-write. `git add <paths>` then `git commit -m "…" -- <paths>` (add first — new files; on a pathspec error, `git add` and retry, never `-a`). Post-commit, print `git rev-parse --show-toplevel` to assert WHERE it landed.
>
> In `### Ledger Updates`:
>
> `#### Project Status` — milestone SCOPED to this plan: the 41-entry session-24→33 batch INGESTED; corpus integrity held; the 42-row Gate-2 queue verified intact id-for-id at close; **no proposals created — classification is Plan B's, and `get_unclassified_entries()` returning 41 is the correct closing state.**
>
> `#### Forward Register` — ⚠️ write this block INSIDE `### Ledger Updates` **IN YOUR FINAL MESSAGE OUTPUT — the daemon's parser reads the TRANSCRIPT, never a deposited file, and within the transcript it reads the Ledger Updates body ONLY** (a block one heading too high is silently discarded). Described not quoted. **ONE item, and it must be the FIRST line of the block body with all prose AFTER it**, because the splitter falls back to first-line-only on a block with fewer than two bullets. ⚠️⚠️ **Nothing else in this block may begin with a dash or a digit-and-period — `sanitize_items` matches `^(?:-\s|\d+\.\s)`, so a numbered item IS a bullet to it and each bullet-shaped line emits its own register row.**
>
> 1. `_TERMINAL_STATUSES` omits `accepted`, so an ingest can silently stale a routed-but-not-yet-codified proposal; this plan carried 42 such rows and guarded them procedurally — worth deciding whether the guard belongs in the code instead.
>
> After the bullet and its terminating blank line, in PROSE: state the register's before-count read from your worktree snapshot and record that you read it there (the Planner measured 10 rows at authoring; a difference is a reconcile-note, not a halt). Do NOT re-raise the `get_unclassified_entries` ordering item — it is already open as rows 9 and 10, which are byte-identical duplicates from plan 311's own step 6 through this same channel: live register debt, and the dup-append failure mode observed rather than theorised.
>
> `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/cycle-ingest-qa-2026-08-10.md`
> - `lessons-forge/knowledge/qa/evidence/cycle-ingest-session-24-33-2026-08-10/` (evidence directory as a single bullet — Rule 26; individual filenames stay in Scope and `required_evidence_files` only)
>
> **Do NOT move this plan to `Done/`** — the close path is Bellows-owned on continue-verdict consumption (Rule 8).

---

## Drafting Cycle
**Tier:** T1 computed — triggers fired: T-2 (production-data mutation: the corpus write) and T-8 (novel: plan 311's `NT`-empty premise does not hold, so the ingest's safety machinery is new). **Self-escalated to T2**, stated reason: the ingest's staling path is unprotected for `accepted` rows and its blast radius is the queued Gate-2 batch, including the 21 proposals the wider route exists to codify.
**Walks:** 8, inherited in full. **This plan is a DERIVATION, not a new draft** — Step 1 is carried verbatim from `knowledge/research/draft-cycle-run-339-2026-08-10.md`, which ran eight walks (walks 2 and 3 folded in batch and struck; walk 8's five lenses run by fresh-context readers, sequentially, with the author folding between). The full per-lens record and all 90 fold rows are in the committed walk register at `governance/knowledge/research/walk-register-cycle-run-339-2026-08-10.md`.
- Weak spots:          w8 10 folded — 6 pre-existing after seven prior walks (the fingerprint's missing resume branch; the Gate-2 count-not-id-list).
- Destruction:         w8 9 folded — 6 of them damage from walk 8's own lens-1 folds (row 10's discredited causal test; the tranche-A-only producer).
- Vulnerabilities:     w8 7 folded (the positive control's cased literal against a lowercased string; two ISO dialects vs `fromisoformat` on Python 3.9.6).
- Integration-record:  w8 14 raised, 7 folded — **including the reversal of walk 5's §2.8 deletion, whose subsumption was checked against recollection of Rule 42 rather than its text.**
- ACID:                w8 15 raised, 12 folded — the isolation map that produced this split, plus a carve-out debt the plan itself had declared owed at four sites and never paid.
**Panel status (T2):** not convened. ⚠️ This line is deliberately phrased so §4's cold-panel check CANNOT match it — the check keys on a line opening `**Cold…` or `- Cold…`, and the canonical form satisfies the check while the panel has not run. The WARN is earned; it clears by convening the panel, never by wording.
**Conflicts:** C1–C20, inherited; C18 (an unprotected non-terminal set is named by id and checked at every boundary) and C19 (a derived expectation names the PREDICATE its operand is drawn from) were opened by this cycle and both are load-bearing here.
**Closing:** ⚠️ **NOT a dry close, and not a bar-meeting judged stop — declared plainly rather than dressed up.** Walk 8's last lens raised 15 findings, of which 12 are folded and **10 across lenses 4 and 5 are carried unfolded and enumerated in the walk register.** The six-step artifact did not converge; **the CEO's resolution was to SPLIT it rather than walk it further**, on the measurement that walk 8's per-lens yield rose (10 → 9 → 7 → 14 → 15) and that the isolation matrix generating those findings is a property of the six-step shape. **Every one of the ten carried findings was re-checked against THIS plan's surface before deposit, and each is either resolved by the split (it lived in Steps 2–6, which are not here) or record-class in text this plan does not carry.** That re-check is what licenses the deposit, and it is the deposit's whole argument.

---

### Conflict Ledger (§2.8) — inherited from the parent draft, TRIMMED to the constraints this plan carries

⚠️ **This is a subtractive trim and its subsumption is stated per item, not asserted in aggregate:** each constraint below is cited somewhere in this plan's own text; each one dropped (C2, C3, C6, C13, C15, C16, C17) governed only the classification steps, the tranche manifests, the report or the multi-tranche anchor union — **none of which this plan contains.** The full twenty live on in the parent draft and bind Plan B.

- **C1** — the non-terminal baseline is a MEASURED premise, and here it is non-empty: every guard resting on it re-verifies at run time or halts.
- **C4** — a resume anchors on the ORIGINAL committed capture, never a live re-read.
- **C5** — a permitted outcome is never a FAIL; the one exception is QA row 6, which fails closed on doctrine changes.
- **C7** — no step's pre-flight states an unqualified fresh-run claim about a resume-variant value; every such expectation is qualified by the dispatch determination and carries a CONTRADICTION→HALT arm.
- **C8** — every mandated check reports a positive token or exit code; nothing is discharged by absent output. Binds hardest on ZERO/EMPTY expectations.
- **C9** — assertions about owned rows name the RECORDED id lists; `entry_id > 265` is forbidden as an ownership operand once Step 1 has run. Carve-out: report-only complements.
- **C10** — a check that replaces a value-level assertion with a count must construct the change the survivor is supposed to catch and confirm it FAILS. **Check: QA row 7's id-for-id comparison, which exists because a count of 42 is satisfiable by a staled-and-replaced corpus.**
- **C11** — no third status glyph; no `|`-bearing command in a table cell.
- **C12** — a bound must be able to fail: name the input that fails it, or it asserts nothing. **Check: QA row 4's `proposals == 273` names its failing input (a `detect_duplicates` insert).**
- **C14** — every mandated requirement is stated IN the step that must comply with it; a rule living only in a verifier or only in a producer is a defect in whichever direction is missing.
- **C18** — an unprotected non-terminal row set this plan does not own is named by id, checked at the boundary, and has its own QA row. **Check: Step 1 Receipt item 5 plus QA row 7.**
- **C19** — a derived expectation names the PREDICATE its operand is drawn from, not a previously-recorded label.
- **C20** — where two rows adjudicate the same DB fact, exactly one owns the verdict and the other reads it.

**Ledger status:** C1, C4, C5, C7, C8, C9, C10, C11, C12, C14, C18, C19, C20 OPEN and carried. C2, C3, C6, C13, C15, C16, C17 are not carried, per the per-item subsumption above.
