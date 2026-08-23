# lessons-forge — CORRECTIVE diagnostic to 503: settle the `learned` promotion set by stating the two rules it never stated

**Date:** 2026-08-23 | **Project:** lessons-forge | **Tier:** Medium | **Dispatch Mode:** bellows | **cycle_tier:** T1 | **Test Scope:** none (read-only diagnostic) | **Execution:** Step 1 (READ-ONLY DIAGNOSTIC) | **Priority:** 1

**auto_close:** false
**pause_for_verdict:** after_step_1

**Depends on:** `lessons-forge/knowledge/decisions/Done/diagnostic-503.md` and its findings `knowledge/research/learned-promotion-2026-08-23.md` — **this plan CORRECTS them and does not inherit their conclusion.** Newest same-class and clone origin: the same 503, shipped 2026-08-23.

## Why this exists

Diagnostic-503 produced a promotion set of `V` entries. A cold DISCOVERY seat reviewing the executable that would apply it found the set **corresponds to no class 503 itself defines**, and the Planner author-verified both defects:

1. **The PARTLY split is arbitrary.** 503 classifies each mapping FULLY or PARTLY. `F` are FULLY and every one was promoted. `R` are PARTLY — and **three were promoted while three were demoted, with no stated basis.** 503's own Q2 instruction says a lesson only PARTLY enforced **"is not completion"**.
2. **Some promotions are CIRCULAR — the mechanism is the SUBJECT of the lesson, not its enforcement.** Entry 191 ("*An honest QA failure passes the Rule 20 self-check*") was promoted on `_gate_rule_20_self_check`; entry 121 ("*Bellows gates do not include suite-green*") on `_gate_qa_test_result`; entry 106 ("*`scope_check` false-positive… Planner override is the right disposition*") on `_gate_scope_check`. ⚠️ **503 SAW this and promoted anyway** — its own note on 121 reads "(names the gap this gate fills)".

**`G` therefore has four defensible values — 503's prose figure, `F`, `V`, or `F` less the circular promotions — and the companion executable cannot proceed while that is true.** ⚠️ Named by SOURCE rather than as numerals, deliberately: three of the four are owned symbols and the fourth is the figure 503 got wrong, so writing them as bare digits is how they drift. This plan settles it by stating the two rules 503 left implicit and re-deriving the set against the demonstrations 503 already produced.

## What this plan does NOT do

- **It does NOT re-run the detector or re-demonstrate any fire.** ⚠️ **Be precise about what was verified, because this plan is about an over-claim and must not commit one:** the Planner re-ran **three** of 503's demonstrated gates directly — `receipt_status`, `no_errors`, `ceo_flags` — each firing on its violation and passing its control. The remainder are ASSERTED sound on 503's own report, not independently re-run. **That is sufficient here, and the reason is structural: Q3 asks whether a mechanism is the lesson's SUBJECT rather than its enforcement, and that question is answered by reading the lesson against the mechanism — it does not depend on the fire having been re-observed.** If your reading turns up a candidate whose verdict WOULD depend on re-running its fire, say so and mark it undecided rather than assuming.
- **It does NOT edit `LESSONS.md`, write to any DB, or re-label anything.**
- **It does NOT re-open the 220 demoted entries.** They had no demonstrated mechanism at all and are not candidates. ⚠️ Say so explicitly in your findings rather than leaving it implied — a reader must be able to tell "not a candidate" from "considered and rejected".
- ⚠️⚠️ **It DOES re-open the `W` entries, and this is the inverse of 503's error.** 503's Q2 identified `W` entries as **FULLY enforced** that are currently marked `pending`, and its Q4 silently excluded them by scoping the promotion set to entries already labelled `learned`. Under the CEO's ruling that scoping is backwards: `learned` means a mechanism enforces the rule, not that the entry was previously guessed to be finished. One of them — "*A function that computes a LOOKUP KEY must be the identity*" — is the exec-499/500 lesson, guarded by the `test_key_heading_*` suite. **503's error ran in both directions: it promoted entries that had not earned it AND left entries that had.**

## Numbers discipline

⚠️ **This table owns every quantity the plan ACTS ON.** Values measured at walk 0, 2026-08-23. **RE-DERIVE every one; if yours differ, yours supersede and you say so.**

| id | pin | value | probe |
|---|---|---|---|
| D0 | **`A`** — `learned` candidates 503 mapped to a demonstrated mechanism | **22** | `F` + `R`, counted as DISTINCT corpus ids — ⚠️ not as occurrences of the words FULLY/PARTLY, which number 29 in that section and include prose and non-`learned` entries |
| D0b | **`W`** — entries 503 marked FULLY that are NOT in the `learned` set | **2** | Q2 lines referencing an entry by LINE rather than by corpus id, tagged `[pending]` and FULLY |
| D1 | **`F`** — candidates 503 marked FULLY | **16** | count of `FULLY` verdicts in the Q2 mapping |
| D2 | **`R`** — candidates 503 marked PARTLY | **6** | count of `PARTLY` verdicts in the Q2 mapping |
| D3 | **`V`** — distinct entries in 503's deposited promotion TSV | **19** | `awk -F'\t' 'NR>1{print $1}' <tsv> \| sort -u \| wc -l` |
| D4 | **`X`** — headings currently reading `[status: learned]` | **239** | `grep -cE '^## .*\[status: learned\]' <abs LESSONS.md>` |
| D5 | **`N`** — dated headings in the register | **327** | `grep -cE '^## 20[0-9][0-9]' <abs LESSONS.md>` |
| D6 | corpus `lesson_entries` — negative pin | **370** | `sqlite3 "file:<abs>?immutable=1" "SELECT COUNT(*) FROM lesson_entries"` |

⚠️ **`V` ≠ `F` and `V` ≠ `F` + `R`.** That inequality IS the defect: the deposited set is `F` plus an arbitrary three of `R`.

## Drafting Cycle
**Tier:** T1 — triggers fired: **T-7** (the companion executable consumes the corrected set without re-deriving it) and **T-8** (novel: no prior plan grades a promotion set against the classification that produced it). T-5/T-6 do NOT fire — read-only, edits no doctrine, gate, template or contract.
**Walk register:** `governance/knowledge/research/walk-register-diagnostic-promotion-corrective.md`
**Walks:** in progress — walks 0-3 run.
**Walk 0 (context pin) — REAL, measured 2026-08-23:** newest same-class and clone origin are the same plan, `Done/diagnostic-503.md` (2026-08-23) — the plan this one corrects. This plan replaces text in no existing file, so §2.0's anchor measurements are structurally empty rather than skipped. The measurement that fixed its shape: **`V` is `F` plus exactly three of `R`** — the deposited set corresponds to no class 503 defines — and 503's own PARTLY note on one promoted entry reads "(names the gap this gate fills)", which is the circularity stated in the source and promoted anyway.
**Direction verdict (after walk 1): PROCEED** — the corrective's angle is the one the DISCOVERY seat's direction finding pointed at; nothing invalidates its origin, mechanism or scope premise.
- Weak spots:          w1 1 folded — instruction 1 / record 0; w2 1 folded — instruction 1 / record 0; w3 1 folded — instruction 1 / record 0.
- Destruction:         w1 1 folded — instruction 1 / record 0; w2 dry; w3 1 folded — instruction 1 / record 0.
- Vulnerabilities:     w1 1 folded — instruction 1 / record 0; w2 dry; w3 dry.
- Integration-record:  w1 2 folded — instruction 2 / record 0; w2 dry; w3 dry.
- ACID:                w1 1 folded — instruction 1 / record 0; w2 1 folded — instruction 1 / record 0; w3 dry.
⚠️ **Walk 0 carries no fold row and that is correct, not an omission:** for this plan walk 0 was a CONTEXT PIN whose output is the measurement that shaped v0 (`V` = `F` plus three of `R`), not a pass over a pre-existing draft. Its guards were authored INTO v0 rather than folded into it. A `cycle_check` run comparing walk 1 against an empty walk 0 reports `yield-rising`; that is the manual entry gate the cadence explicitly excludes from auto-advance (§2: walk 0, walk 1 and the direction verdict), not a convergence signal.
**Conformance (§5):** `plan_lint` exit **0**; `propagation_check` exit **0**.
**Cold panel:** not required at T1; scout at the Planner's call.

## MUST-PRESERVE

- **READ-ONLY.** No edit to `LESSONS.md`, no write to any `.db`, no re-label, no new demonstration.
- ⚠️ **Corpus reads via `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?immutable=1`** — `immutable=1`, NOT `mode=ro`: the corpus is WAL, and `mode=ro` fails against a copy with no `-shm` sidecar and touches the live `-shm` mtime. 21 stale `pre-*.db` snapshots sit beside it answering fluently and wrong; assert `lesson_entries` equals `D6` before trusting any read.
- ⚠️ **`LESSONS.md` is in the governance ROOT repo** — `/Users/marklehn/Developer/GitHub/LESSONS.md` — and is ANNOTATED: `X` headings read `learned`, some read `pending`, and 14 are bare.
- ⚠️ **DO NOT "correct" 503's prose figure of 15.** It is wrong, its TSV is right about its own contents, and BOTH are beside the point — this plan re-derives the set from the CLASSIFICATION, not from either count. ⚠️ Note that 503's identity check cannot discriminate: it defines codified as `X` − `G` and then sums to `N`, so it balances for ANY value of `G` — which is why nothing internal to 503 caught the error, and why you must not treat a balancing identity as evidence the set is right.
- **`grep` here is ugrep: `-F` for every literal search.** ⚠️ A zero-match `grep -c` prints `0` and EXITS 1 — read the printed count, never the exit status. ⚠️ A `-E` pattern with a nested quantifier over this corpus can exceed the shim's complexity limit and ERROR rather than return empty; if that happens, narrow the pattern — do not read the error as an absence.
- ⚠️ **Invoke any checker by ABSOLUTE path** from `/Users/marklehn/Developer/GitHub/bellows/scripts/`; shell state does not persist between invocations, and a relative call after a `cd` reports `can't open file` and exits non-zero, which is easily misread as a check failing.

## STEP 1 — READ-ONLY DIAGNOSTIC

**Role:** DEV (read-only audit). Contract: `/Users/marklehn/Developer/GitHub/READONLY_AUDIT_CONTRACT.md`.

**Contract parameters.** `cwd`: your bellows worktree under `lessons-forge/.bellows-worktrees/<id>/`. `deposit_paths`: the two files in Deposits. `extra_forbidden`: any write to `LESSONS.md`, to any `.db`, or to any real `knowledge/decisions/` directory. `extra_preflight`: assert the corpus identity (path, byte size, `lesson_entries` equal to `D6`). ⚠️ **`C7` REPO SET, pinned explicitly because the contract HALTs on an unnamed set:** `/Users/marklehn/Developer/GitHub` (root), `/Users/marklehn/Developer/GitHub/lessons-forge`, `/Users/marklehn/Developer/GitHub/bellows`, `/Users/marklehn/Developer/GitHub/forge`.

**Q1 — Reproduce the defect.** Re-derive `A`, `F`, `R`, `V` and list the ids in each. Show that `V` is `F` plus exactly three of `R`, and name which three were promoted and which three were demoted. ⚠️ **State whether 503 gives ANY basis for that split** — read its Q2 mapping notes and its Q4 set arithmetic before answering, and if there is no basis, say so plainly rather than constructing one. ⚠️ **Then find the `W` entries** — Q2 references some entries by LINE rather than by corpus id, and at least `W` of those are tagged `[pending]` and FULLY. List them with their line numbers and headings. ⚠️ **Counting method matters here and the Planner got it wrong once: count DISTINCT CORPUS IDS, not occurrences of the words FULLY/PARTLY** — the words appear 29 times in that section, including in prose and against non-`learned` entries, and a word-count probe reports a confidently wrong candidate set.

**Q2 — RULE ONE: does PARTLY count as completion?** 503's Q2 instruction says a lesson only partly enforced is not completion. ⚠️ **That instruction was not invented after the fact** — it was folded into 503 at ITS walk 1, before it ran, precisely to stop a partial mechanism reading as completion. So the rule was intended and stated; what failed was applying it. ⚠️ **Do not simply ratify that — TEST it against the six.** For each `R` entry, read the lesson and the mechanism and state what the mechanism does NOT catch. ⚠️ **Take the lesson text from `LESSONS.md` by its heading, not from the mapping's `original_heading` alone** — the heading is a one-line summary and the body carries the rule's actual scope, which is what determines whether a mechanism covers it. Then answer: is "partly enforced" a third state, or is it `codified`? ⚠️ **Argue it from the six actual cases, not from the definition** — if any of them is partly-enforced only in a trivial or immaterial way, that is an argument for a narrower rule and you should say so.

**Q3 — RULE TWO: can a mechanism enforce a lesson about that mechanism's own insufficiency?** Three promotions look circular — 191, 121, 106 — and 503's own note on 121 reads "(names the gap this gate fills)". ⚠️ **Test every one of the `A` candidates against this, not only the three already named** — the three were found by a cold reader spot-checking, and a systematic pass is the point of this plan. For each, answer: does the demonstrated mechanism REJECT A VIOLATION OF THIS LESSON, or is the mechanism merely the lesson's subject matter? ⚠️ **State the discriminator you used** so it can be reused, and flag any case where the two readings are genuinely close.

**Q4 — RE-DERIVE THE PROMOTION SET.** Apply both rules and emit the corrected set. Deposit `knowledge/research/promotion-corrected-2026-08-23.tsv` with columns `entry_id`, `entry_heading`, `mechanism`, `mechanism_file`, `rule1_partly`, `rule2_circular`, `verdict`. ⚠️ **One row per (candidate, mechanism) PAIR — covering all `A` candidates AND the `W` pending-but-enforced entries, INCLUDING the rejected** — so the executable and any later reader can see what was excluded and why. 503's own TSV carried 21 rows over 19 entries, so candidates DO map to multiple mechanisms, and a one-row-per-candidate schema would silently pick one and discard the rest. ⚠️ **This matters for the verdict rule, not just the layout: rule two is a property of the (entry, mechanism) PAIR.** An entry can be circular with respect to one mechanism and genuinely enforced by another — so **an entry is `PROMOTE` if at least one of its mechanisms passes BOTH rules, and `CODIFIED` only if none does.** Record the per-pair columns, then state the per-entry verdict and the distinct-entry count separately from the row count. `verdict` is `PROMOTE` or `CODIFIED`. ⚠️ **Both rules can fire on one candidate, and either alone is disqualifying** — record both columns independently rather than short-circuiting once the first fires, because the two carry different lessons for Q6 and a reader needs to see which applied. Report the resulting `G` and how it differs from `V`. ⚠️ **STATE THE SET'S AUTHORITY, because 503's failure to do so is half of why we are here.** A `PROMOTE` row marks an entry as COMPLETE in the artifact the shop greps to decide what to build. **The executable may apply `PROMOTE` rows mechanically and may apply NOTHING else** — no inference from a `CODIFIED` row, no reconciliation against 503's TSV, no arithmetic that recovers a different `G`. Give the per-verdict counts so neither can be derived from the other.

**Q5 — Size the states and state the executable's input.** Give `learned`, `codified`, `pending` and bare counts, reconciling to `N` − bare for the three states and to `N` overall. ⚠️ Assert the arithmetic; do not transcribe a figure from this plan. ⚠️ **Say explicitly that the companion executable must read THIS file and not 503's TSV**, and name the file.

**Q6 — What should 503's detector have done?** The classification failed, not the demonstrations. ⚠️ Propose the change that would have caught this at source — a rule the detector applies, a column the TSV carries, or a check a later plan runs — and **argue whether it belongs in `detect_learned.py`, in the diagnostic template, or in doctrine.** State what it would cost.

**Findings document:** Q1–Q6, each answered with command output or `file:line`. Close with `## What could not be measured`, `## Open forks`, and `## Recommended executables`.

**Scope:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/promotion-corrected-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/promotion-corrected-2026-08-23.tsv`

**Deposits:**
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/promotion-corrected-2026-08-23.md`
- `/Users/marklehn/Developer/GitHub/lessons-forge/knowledge/research/promotion-corrected-2026-08-23.tsv`

**Commit:** ⚠️ **WORKTREE DISCIPLINE.** You are dispatched into `lessons-forge/.bellows-worktrees/<id>/`. Write both deposits at the SAME relative paths under YOUR cwd and commit them there in ONE commit: `git -C <your-worktree> add knowledge/research/<both> && git -C <your-worktree> commit -m "..."`. ⚠️ Do NOT write to the main checkout — `gates._resolve_deposit_path` falls back to "path as-is" and `_check_deposit_uncommitted` swallows the out-of-worktree git error, so writing to the wrong checkout passes both gates SILENTLY and the teardown-merge never picks your files up. Absolute for everything you READ, relative-to-cwd for everything you WRITE.
