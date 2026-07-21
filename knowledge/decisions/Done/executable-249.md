# Lessons Forge — Gate 2 Codification (cycle 2026-07-21) → PLANNER_TEMPLATE v4.77
**Date:** 2026-07-21 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** none | **Execution:** Step 1 (SA) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

Gate 2 of the 2026-07-21 cycle. Gate 1 closed 2026-07-21 (plan 248): twelve proposals routed **9 codify / 1 reference / 2 backlog**. This plan codifies the **nine** `codify` proposals as **seven edits** to governance-root `PLANNER_TEMPLATE.md` (live **v4.76**, the dedup baseline) and transitions those nine to `implemented`.

**⚠️ Proposals 161, 164, 169 are NOT in scope and MUST NOT be touched.** They are already terminal at `status='reference'` (161/169 routed `backlog`, 164 routed `reference`). Any status write outside the nine is a defect.

### The edit map — nine proposals, seven edits

| # | Region | Proposals | Edit |
|---|---|---|---|
| E1 | `## The Drafting Cycle` — lens 5 (ACID) | **160** | **WIDEN the Isolation clause** to cover multi-step schedules |
| E2 | `## The Drafting Cycle` — The Full Cycle | **163 + 170** | The lens set is OPEN; a novel lens's fold is provisional |
| E3 | `## The Drafting Cycle` — The Full Cycle | **166** | Parallelism belongs WITHIN a pass, never ACROSS lenses |
| E4 | `## The Drafting Cycle` — The Full Cycle | **171** | Rotate the reviewer when late walks go quiet |
| E5 | Plan Authoring Checklist **#26** (`:1244`) | **162** | Generalize: any anti-pattern fix gets a full-artifact sibling sweep |
| E6 | Orchestration Plan Rules — **new #55** | **165 + 167** | Assert a positive signal from the repo/tree that holds the state |
| E7 | Orchestration Plan Rules — **new #56** | **168** | Resume machinery only when the work is not reproducible |

**⭐ E1 IS THE CEO'S FORM DECISION AND IT IS A MERGE, NOT AN ADDITION — read this before drafting a word of it.**
CEO decision 2026-07-21: conflict-serializability (proposal 160) joins the **ACID lens as a facet of Isolation**; it does **NOT** become a sixth named lens. The rationale is principled — conflict serializability is the formal content of the "I" in ACID (a schedule is serializable iff its conflict graph is acyclic), so it belongs inside that lens rather than duplicating its theory alongside it.

**⚠️ But the widening MUST be substantive, not a cross-reference.** The live clause reads, in full: *"Isolation: what does a concurrent actor observe mid-operation?"* — **single-operation scoped.** The record's evidence is that this exact wording does not produce the finding: across the 2026-07-20 Gate-2 cycle **ACID ran three times (walks 1/2/3) and found ZERO between-step windows, while conflict-serializability found one on EACH of its three applications** (DEV→QA template shasum chain; QA→wrap template re-match; DEV→QA per-id DB byte-match) — same drafts, same reviewer, different question. **A merge that appends "…and consider serializability" reproduces that failure while reading as though it fixed it.** The widened clause must explicitly name the **multi-step schedule** — the windows *between* steps, separated by verdict gates of arbitrary wall-clock time, across shared stores — and must prompt the reader to enumerate reads/writes as a schedule. Do not assume the existing wording covers it; the record says in terms that it does not.

**✅ The lens COUNT stays FIVE — no lens-count sweep is required, and this is load-bearing.** v4.76's most dangerous near-miss was three live doctrine phrases still saying "four" after the list became five, caught only by cold readers on pass 8. Verified at authoring: the two live count phrases are `:333` ("five **named lenses**") and `:345` ("five heavy passes"), and **both remain correct under a merge.** The only "four" occurrence left is a **changelog row (`:1826`)**, which is historical and must be **PRESERVED**. **Do NOT sweep counts on this plan, and do NOT "fix" the changelog.** A sixth lens would have forced a five→six sweep; the merge is what removes that entire defect class.

### Dedup baseline and anchors — all verified at authoring against live v4.76

- **⚠️ NUMBERING CORRECTION, carried deliberately: E5's target is Plan Authoring Checklist #26 (`:1244`), NOT "Rule 26."** The Gate-1 plan's CEO Context called it "Rule 26" — that was a mis-citation. `### 26.` occurs **twice**: Orchestration Plan Rules #26 is *"Deposits field convention"* (`:795`) — **unrelated, do not touch it** — and Plan Authoring Checklist #26 is *"Convention-change plans grep for all occurrences"* (`:1244`), which is E5's actual target. Gate 1 only set routes, so nothing executed against the wrong anchor; this plan corrects the record. **The two sections number INDEPENDENTLY — this is pre-existing convention, not a collision to fix.**
- **Section maxima, measured at authoring:** Orchestration Plan Rules (`:480–1073`) holds 54 items, highest **#54** — so E6/E7 become **#55** and **#56**. Plan Authoring Checklist (`:1086–1287`) holds 32 items, highest **#32** — E5 amends **#26** in place rather than adding #33. Re-derive both live before applying; do not trust these numbers.
- **The eight non-160 proposals were grep-verified absent from the template at Gate 1** (`lens set`/`novel lens`/`provisional`/`standing lens` 0; `git -C` 0 and `positive signal` 0; `main-tree`/`main tree` 0; `restore-and-redo`/`resume machinery`/`reproducible` 0; `rotate`/`cold`/`fresh-context`/`saturat` 0). **Re-verify at SA time against live v4.76 — the template may have moved.**

### Pair-merge rationale (E2 and E6), and its limit

E2 and E6 each combine two proposals into one edit, applying the same principle as E1: **related principles belong together.** E2 — 163 (the lens set is open) and 170 (a novel lens's fold is provisional) are two halves of one claim about novel lenses. E6 — 165 (`git -C` the tracking repo) and 167 (guards read the live main tree) are two instances of one rule: *empty output is not verification; assert a positive signal from the thing that actually holds the state.* **The limit: 166 and 171 stay SEPARATE edits.** Both concern how a walk is executed, but they are different failure modes (parallelism severs cumulation; saturation blinds a reviewer) with different remedies, and merging them would produce a paragraph that states neither sharply. **A merge is warranted by shared principle, not by shared neighbourhood.**

**Gate 2 is a governance edit with NO test suite — Planner verification is the safety net (`Test Scope: none`).** SA blueprints exact insertion/replacement text; DEV applies VERBATIM; QA verifies structure. PLANNER_TEMPLATE lives in the governance ROOT — DEV edits it in place by absolute path and it stays **UNCOMMITTED** (the Planner commits cross-repo at wrap; plan-134/208/228/246 precedent).

**⚠️ Wrap-commit protocol (binds the PLANNER, recorded here because the wrap is this schedule's final write).** Between QA's certification and the wrap commit the template sits modified-uncommitted in the main tree — an unguarded window. Before committing, the Planner MUST re-run `shasum -a 256` on the template and match it against the hash in the Step-2 dev-log. Match → commit (the certified bytes are the committed bytes). Mismatch → a post-QA edit landed; investigate before committing. This closes the integrity chain end to end: **SA read (commit pin) → DEV write (A0) → QA read (hash row) → wrap commit (re-match).**

**Scope discipline:** this plan edits ONE file (`PLANNER_TEMPLATE.md`) and transitions NINE proposal statuses. It touches no `src/`, no schema, and no other proposal.

**Deposit-once discipline:** deposited exactly once.

**Authoring self-check (for the verdict gate).** `bellows/scripts/plan_lint.py` was run against this plan at authoring time: **exit 0**, checks (a)-(d) all PASS (header parsed, dispatch_mode bellows, pause_for_verdict always, all three steps' Deposits and Scope resolved, QA banner pair present). It emits **one known-benign WARN** — "step 2 mentions tests but declares no test scope" — which is the `scope_check`-on-tests false-positive class: this is a governance edit with `Test Scope: none` (no suite exists to run), and Step 2's only mention of tests is the statement that there is no test suite. **Do NOT add a test file to any step's scope to silence it** — doing so would declare a test scope this plan does not have. Exit 0 is the pass.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/executable-gate-2-codification-2026-07-21.md. Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — SA (Solution Architect)

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Solution Architect. Run commands from your own working tree. The target file is the governance-root `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — **READ-ONLY this step; you blueprint, DEV applies.**
>
> **Read the nine proposals VERBATIM from canonical, and their source lessons via the DB join — never by ordinal counting:**
> `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT p.id, p.entry_id, p.suggested_action, p.reasoning, e.source_heading, e.raw_content FROM lesson_proposals p JOIN lesson_entries e ON e.id = p.entry_id WHERE p.id IN (160,162,163,165,166,167,168,170,171) ORDER BY p.id"`
> `raw_content` IS the lesson body. **Confirm you retrieved exactly nine rows and that 161/164/169 are absent from your result set** — they are out of scope and terminal.
>
> **Scope:**
> - `knowledge/development/gate-2-blueprint-2026-07-21.md`
>
> **Read the live template regions before blueprinting** (re-derive every line number; the ones in this plan are authoring-time): `## The Drafting Cycle` (`:314–:348`, with `### The Full Cycle` at `:331` and the ACID lens at `:339`), Plan Authoring Checklist **#26** (`:1244`), and the tail of Orchestration Plan Rules (`:1066` = Rule 54, the current highest). **Pin your read:** record `git -C /Users/marklehn/Developer/GitHub rev-parse HEAD` and the template's last-touching commit (`git -C /Users/marklehn/Developer/GitHub log -1 --format=%H -- PLANNER_TEMPLATE.md`). DEV re-checks the latter before applying — if the template changes between your read and DEV's write, your anchors are stale even if the tree is clean.
>
> **Blueprint SEVEN edits — exact final text plus an exact, unambiguous anchor for each.** For every edit give: the anchor (a verbatim substring that occurs EXACTLY ONCE in the live file — verify the uniqueness by grep and state the count), whether it is an insertion or a replacement, and the complete text DEV will apply. DEV is a faithful applicator and will not improvise.
>
> **E1 — WIDEN the ACID lens's Isolation clause (proposal 160). This is the plan's centrepiece; give it the most care.**
> Current text, verified verbatim: `Isolation: what does a concurrent actor observe mid-operation?`
> Replace it with wording that keeps the single-operation question AND adds the multi-step schedule. It must: (a) name the plan's steps as a **schedule** whose reads and writes on shared stores should be enumerated; (b) name the **windows between steps** — separated by verdict gates of arbitrary wall-clock time — as the place unguarded conflicts live; (c) prompt for R-W / W-R / W-W conflicts against a plausible concurrent actor; (d) require an explicit guard (a pin, a byte-match, a locked transaction) rather than an assumption of quiescence. **Do NOT introduce a sixth lens, do NOT renumber the lenses, and do NOT alter the lens count anywhere.** Keep the clause inside lens 5's existing sentence structure (`Atomicity: … Consistency: … Isolation: … Durability: …`) so the lens reads as one coherent question set.
> **Evidence to honour in the wording:** ACID-as-written found zero between-step windows in three runs; the conflict-serializability question found one on each of three applications. If your drafted clause would not have prompted a reader to ask about the DEV→QA window, it has not been widened enough — say so and redraft.
>
> **E2 — the lens set is OPEN and a novel lens's fold is provisional (proposals 163 + 170).** One addition to `### The Full Cycle`. Must state: add a lens when a plan class raises a question the standing lenses do not ask; and a novel lens's first fold is **provisional** — sequence a standing lens (weak spots or vulnerabilities) immediately behind it, aimed specifically at whether the new guard is **executable**, not at whether the window is real. Cite the empirical shape from the entries: a novel lens reliably finds the right WINDOW and reliably ships a broken MECHANISM.
>
> **E3 — parallelism belongs WITHIN a pass, never ACROSS lenses (proposal 166).** One addition to `### The Full Cycle`. Parallel work inside a single lens pass is permitted; running lenses concurrently is prohibited because it severs the cumulative property (each lens must read the draft as the prior lens left it). A concurrent multi-lens run is a **panel pass**, not a walk, and must be labelled as such.
>
> **E4 — rotate the reviewer when late walks go quiet (proposal 171).** One addition to `### The Full Cycle`. A "dry" verdict from a saturated reviewer is weak evidence. When late walks stop finding things, rotate the **reviewer** — run the standing lenses **cold** (fresh-context readers given only the artifact plus repo read access), **sequentially** so cumulation is preserved — not the lens. Author verification of cold findings remains required: cold readers can misread deliberate design as defect.
> **⚠️ E3 and E4 interact — make the blueprint state the reconciliation explicitly.** E3 prohibits running lenses concurrently; E4 prescribes cold reviewers run sequentially. They are consistent (both preserve cumulation), but a careless reading takes "run cold lenses" as licence for a parallel panel. The text must make sequential-cold the prescribed form.
>
> **E5 — generalize Plan Authoring Checklist #26 (proposal 162).** ⚠️ **The target is Plan Authoring Checklist #26 at `:1244` ("Convention-change plans grep for all occurrences"), NOT Orchestration Plan Rules #26 at `:795` ("Deposits field convention").** Verify both anchors by grep and state which you are editing. Amend #26 **in place** so its discipline covers **any fix of an anti-pattern instance**, not only convention changes: after fixing one instance, sweep the whole artifact for siblings and confirm zero remain, explicitly including places that merely QUOTE the pattern — negative examples, rationale text, documentation. Preserve #26's existing convention-change content as the worked example; do not delete it. **Update the item's title if the generalization makes it inaccurate.**
>
> **E6 — new Orchestration Plan Rule #55 (proposals 165 + 167).** One rule, two instances of one principle: **empty output is not verification — assert a positive signal from the repo or tree that actually holds the state.** (a) A `git status`/`git diff -- <file>` run from a submodule or worktree that does not track the file passes **VACUOUSLY** — the file is *absent*, not clean; use `git -C <absolute path to the tracking repo>`. (b) Bellows lifecycle/dispatch state is **main-tree uncommitted** and therefore structurally invisible to a worktree; a guard reading it must use an absolute main-tree path and assert a positive signal proving it is reading the live tree. Give the canonical positive-signal example: a plan's own isolation pre-flight should confirm **its own in-progress file is visible**, because that proves the read reached the right tree. Cite the concrete evidence: plan 244's pre-flight reported "no in-progress-* found" while its own in-progress file sat in the main tree.
> **Confirm #55 is the correct next number** — Rule 54 is the current highest in Orchestration Plan Rules (`:1066`).
>
> **E7 — new Orchestration Plan Rule #56 (proposal 168).** Before building resume machinery, ask whether the interrupted work can be **regenerated from a recipe the plan already carries**. If yes, prefer **restore-and-redo** over surgical resume: resume machinery is justified only when the interrupted work is NOT reproducible. Surgical resume adds state, branches, and its own failure modes to buy back work a deterministic re-run would reproduce for free.
>
> **ADR-004 constraint to respect while wording E1-E4.** ADR-004 (Decision 6) defers extracting `## The Drafting Cycle` into a standalone spec, and Decision 6(a) requires that the extracted spec internally separate **shared doctrine** (referencable by Forge's analysis cycle) from the **consequence lens-set** (Drafting Cycle only). E1-E4 are all consequence-lens material and belong with the lens set — word them so they stay cleanly separable from the general adversarial doctrine (walk the list, fold, verify-mid-analysis) rather than interleaving the two. ADR-004 explicitly leaves the sixth-lens-vs-ACID-facet question open, so E1's merge is within its bounds, not against it. Do NOT perform any extraction here — that is D6's own future plan.
>
> **Dedup EVERY edit against the live template before blueprinting it** (the 2026-06-07 discipline) and state the grep and its count for each. If any edit's substance is already present, **halt and report** rather than adding a competing statement.
>
> **⚠️ Do NOT change the lens count anywhere, and do NOT touch the `:1826` changelog row's historical "four" reference.** State in the blueprint that you verified the two live count phrases (`:333`, `:345`) still read "five" and are correct **unchanged** under this merge.
>
> **Also blueprint the two mechanical edits:** the version bump `4.76 → 4.77` (note **line 5 carries no `v` prefix** — grep the bare number; there are two header lines to update, `**Version:**` and `**Last Updated:**`), and the changelog row appended to the changelog table summarising this Gate 2 (name all nine proposals, the seven edits, the E1 merge decision and its rationale, and that the lens count deliberately stays five).
>
> **Deposit:** `knowledge/development/gate-2-blueprint-2026-07-21.md` — the seven edits with exact text and grep-verified unique anchors, the two mechanical edits, the dedup greps with counts, the pinned HEAD and template last-touching commit, and an Output Receipt. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-blueprint-2026-07-21.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV

---

> **Before starting, read the Step 1 blueprint and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2.
>
> You are the Forge Developer. Apply the Step-1 blueprint to `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (governance root, ABSOLUTE path, in place) **VERBATIM** — you are a faithful applicator, not a re-author. If the blueprint and the live template disagree on an anchor, **halt and report** rather than improvise.
>
> **Scope:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (edit in place; leave **UNCOMMITTED** — the Planner commits at wrap)
> - `knowledge/development/gate-2-codification-dev-2026-07-21.md`
>
> **Task A0 — pre-edit cleanliness gate, with resume disambiguation.**
> `git -C /Users/marklehn/Developer/GitHub status --short -- PLANNER_TEMPLATE.md` must be **empty**, AND the template's last-touching commit (`git -C /Users/marklehn/Developer/GitHub log -1 --format=%H -- PLANNER_TEMPLATE.md`) must **match the one recorded in the Step-1 blueprint**. A clean tree with a different last commit means the template moved after SA read it → the anchors are stale → **HALT; do not apply a blueprint against a state the SA never read.**
> **Use `git -C <root>`** — the template is tracked by the ROOT repo; a bare `git status` from your worktree passes **vacuously**. (This is proposal 165, which this very plan is codifying as Rule #55. Do not let this plan fail the rule it is writing.)
> **If the tree is DIRTY, disambiguate before halting:** grep the modified template for this plan's own anchors (the bare number `4.77`; `### 55.`; `### 56.`). **Any one present → this plan's own prior work.** Before ANY restore, two protections: (1) **snapshot the dirty file aside** to a durable, gitignored, MAIN-TREE path that survives worktree teardown — `cp /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-cache/template-dirty-snapshot-$(date -u +%Y%m%dT%H%M%SZ)-$$.md` (create `.bellows-cache/` if absent; it is gitignored; the `$$` suffix makes the name collision-safe) and record the absolute path in your dev log; (2) **attribute the dirt** — `git -C /Users/marklehn/Developer/GitHub diff -- PLANNER_TEMPLATE.md`, and every hunk must match blueprint content. **ANY unattributable hunk = MIXED dirt → HALT, never restore** (restoring would destroy someone else's uncommitted work). All hunks attributable → `git -C /Users/marklehn/Developer/GitHub restore PLANNER_TEMPLATE.md`, verify the restore landed (status clean AND last-touching commit still matches the blueprint), then reapply fully from the clean baseline. **No anchor present → foreign modifications → HALT, do NOT restore.**
>
> **Recovery rule for a botched application — SCOPED to this plan's own work.** The pre-edit template is committed (A0 verifies), so the safety net is `git -C /Users/marklehn/Developer/GitHub restore PLANNER_TEMPLATE.md` → then **HALT and report**. **Never hand-patch over a bad apply** — a restore is clean; an incremental fix-up over a mangled state is how a governance file rots. **The retry belongs to a fresh dispatch with fresh context, not to the agent that just failed** (self-retry over one's own botch is the hand-patch spiral by another name). ⚠️ This restore path is ONLY for modifications that are demonstrably this plan's own; A0's foreign-dirty branch remains HALT-only, and the snapshot-aside plus per-hunk attribution apply before EVERY restore in this plan, including this mid-step one. (Note this rule is itself proposal 168, which this plan is codifying as Rule #56: the work is reproducible from the blueprint, so restore-and-redo beats surgical repair.)
>
> **Execute the tasks in label order: A0 → A → B → B2 → B3 → C0 → C.** The count guard (B3) runs AFTER every template edit including the changelog, because it verifies counts across the whole finished file; the DB tasks (C0, C) run last, after the template is complete — see the task-order note below.
>
> **Task A — apply the version bump FIRST, as one atomic edit covering BOTH header lines** (`**Version:** 4.77` and `**Last Updated:**`). Doing it first means even the earliest death leaves `4.77` present for A0's anchor test on a re-dispatch.
>
> **Task B — apply E1 through E7 exactly as blueprinted.** After each, grep-confirm the new text landed. **Section-scoped greps only:** `### N.` numbering repeats across sections, so an unscoped `grep '### 55\.'` is fine (new) but `grep '### 26\.'` hits BOTH sections — when confirming E5, verify you edited the **Plan Authoring Checklist** instance (`:1244` region) and that Orchestration Plan Rules #26 ("Deposits field convention") is **unchanged**.
>
> **Task B2 — apply the CHANGELOG row.** Append the blueprinted changelog row to the changelog table. **This is a separate task deliberately: it is blueprinted by SA and verified by QA row 7, and in an earlier draft of this plan no task actually applied it** — an edit can fall through the gap between 'apply the version bump' and 'apply E1-E7'. The row must name **v4.77**, matching the header Task A wrote (a changelog row naming a different version than the header is a self-inconsistent governance file), and must record: the nine proposals, the seven edits, the E1 merge decision (conflict-serializability as an ACID **Isolation facet**, NOT a sixth lens) with its rationale, and that **the lens count deliberately remains five**. **Append — never rewrite or reflow existing changelog rows.**
>
> **Task B3 — the count guard (do this explicitly, it is the v4.76 near-miss).** Confirm the two live count phrases still read **five** and were NOT altered, and that the `:1826` changelog row's historical "four" reference is **intact**. Report both as explicit checks. This plan must not sweep counts — the merge keeps the count at five by design.
>
> **⚠️ TASK ORDER IS LOAD-BEARING — the template edit (Tasks A/B) MUST complete before the DB transition (Task C). Do not reorder.**
> If the template edit lands and the DB write fails, the corpus says `proposed` while the template already carries the rule — understated, recoverable, and obvious at the verdict gate. > If the DB write landed first and the template edit failed, the corpus would assert nine proposals are `implemented` with **no codification behind them** — a false claim in the permanent record, and one no later gate re-checks. > The asymmetry is the whole reason for the order; it is stated here so a future editor does not 'tidy' the steps into failure.
>
> **Task C0 — DB PRECONDITION, immediately before the write.** The template half of this step has a full cleanliness-and-pin gate (A0); the DB half had none until this check was added — **found by applying E1's own widened Isolation question to this plan's schedule**, which is the clearest possible argument for the edit you are about to make. Read, and assert, immediately before Task C's UPDATE:
> - the nine target ids are each `status='proposed'` AND `route='codify'` — a target that is already `implemented` means a prior dispatch got here (tolerated, idempotent — proceed); a target at any OTHER status, or a route that is not `codify`, means the DB drifted since Gate 1 → **HALT**;
> - **161, 164, and 169 are each still `status='reference'`** — if any has moved, something outside this plan wrote them → **HALT and report**; do not proceed to overwrite nine rows in a corpus that is already drifting.
> Report the precondition read as RAW CLI output. **Do not skip this because A0 passed — A0 gates the template, not the database; they are different stores with different windows.**
>
> **Task C — transition the NINE proposals to `implemented` on the canonical DB.** `UPDATE lesson_proposals SET status='implemented', status_updated_at=<UTC now>, status_updated_by='ceo' WHERE id IN (160,162,163,165,166,167,168,170,171)` — parameterised, **never a bare UPDATE without a WHERE clause**. ⚠️ **161, 164, and 169 MUST NOT appear in that id list and MUST remain `status='reference'`.** Read them back explicitly to prove they were untouched. `conn.commit()` once after the UPDATE.
> **Take a restore point before this write** — the same discipline as the Gate-1 plan, because this is a hand-written UPDATE against the canonical corpus: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" ".backup '/Users/marklehn/Developer/GitHub/lessons-forge/data/backups/lessons-forge-pre-gate2-<UTC stamp>.db'"` (colon-free; `.backup` not `cp`; MAIN-tree absolute path so teardown cannot destroy it). **If the backup fails, is missing, or is zero bytes — HALT and write nothing.**
>
> **Deposit:** `knowledge/development/gate-2-codification-dev-2026-07-21.md` — the applied-edit confirmation (grep each new anchor, section-scoped), the Task B2 count-guard results, the before/after proposal-status distributions as RAW output, the **post-Task-C per-id read as RAW `sqlite3` CLI output** (`SELECT id, status, status_updated_at, status_updated_by FROM lesson_proposals WHERE id IN (160,161,162,163,164,165,166,167,168,169,170,171) ORDER BY id` — include all twelve so the three untouched rows are visible; deposit the CLI output, NOT Python-side values, because QA re-runs this identical query and byte-compares raw-to-raw — this pins the Step-2→Step-3 DB window), the backup path, and **the post-edit template hash (`shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`)** — QA verifies the file is byte-identical at its read. Canonical Python file-write pattern — no heredoc. **Commit the dev-log only — NOT the template.** In `### Ledger Updates` include `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-codification-dev-2026-07-21.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 1 and Step 2 deposits and confirm both Output Receipt statuses Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA).
>
> You are Lessons Forge QA. **Verification + reporting only — no edits to the template, no DB writes.** If a check fails, **report it — do NOT fix it**. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly; route it via the receipt.
>
> **MANDATORY — Rule 20 self-check banner.** Your deposit MUST contain, verbatim, a section headed exactly `## Rule 20 — QA Self-Check Results` followed (anywhere below it) by a line reading exactly `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner is present.
>
> **Evidence rule.** Deposit **RAW command output, never a summary of it.** Every DB row states which DB it ran against.
>
> **Scope:**
> - `knowledge/qa/gate-2-codification-qa-2026-07-21.md`
>
> Verification table, one row per claim:
> 0. **Template integrity — FIRST.** `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` and byte-compare against the hash in the Step-2 dev-log. Mismatch → the file changed between DEV's write and your read → **halt**; every row below would be certifying bytes DEV never produced.
> 1. **Version is 4.77** on BOTH header lines (note line 5 carries no `v` prefix).
> 2. **E1 — the ACID Isolation clause is WIDENED, and the lens count is still FIVE.** Quote the new Isolation text verbatim. Confirm it names the multi-step schedule / between-step windows, not only "mid-operation". **Confirm there is NO sixth lens** — the lens list still runs 1–5 and the two live count phrases still read "five". A sixth lens, a renumbering, or an altered count is a **FAIL**.
> 3. **E2, E3, E4 present** in `### The Full Cycle` — quote each. Confirm E3/E4 reconcile (cold reviewers run **sequentially**; no licence for a parallel panel).
> 4. **E5 amended the right item.** Plan Authoring Checklist #26 (`:1244` region) now generalizes beyond convention changes AND retains its convention-change worked example. **Orchestration Plan Rules #26 ("Deposits field convention", `:795`) is UNCHANGED** — quote it to prove it. Editing the wrong #26 is a **FAIL**.
> 5. **E6 and E7 exist as Rules #55 and #56**, section-scoped to Orchestration Plan Rules (an unscoped `### 55.` grep is acceptable only because no other section reaches 55 — state the section you found them in). Confirm #55 covers BOTH the `git -C` tracking-repo case and the live-main-tree guard case.
> 6. **The `:1826` changelog row's historical "four" reference is INTACT** — quote it. This plan must not have swept it.
> 7. **The changelog has a new row** for this Gate 2 naming the nine proposals and the E1 merge decision.
> 8. **The nine proposals are `implemented`.** Re-run the Step-2 per-id query as raw CLI output and byte-compare against the Step-2 deposit's block. 160, 162, 163, 165, 166, 167, 168, 170, 171 → `implemented` with `status_updated_by='ceo'`.
> 9. **⚠️ 161, 164, 169 are UNTOUCHED at `status='reference'`.** Any of the three at `implemented` is a **FAIL** — they were routed backlog/reference at Gate 1 and are out of scope.
> 10. **Corpus totals unchanged:** 163 entries, 171 proposals; `proposed` is now **0** (the nine were the last of them). Report actuals.
> 11. **No `src/` change and no schema drift** — `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/` empty.
>
> If any row fails, report and halt — do not pass a broken deliverable.
>
> **Deposit:** `knowledge/qa/gate-2-codification-qa-2026-07-21.md` — verification table, raw output, the Rule 20 banner + PASSED line, and an Output Receipt. Canonical Python file-write pattern — no heredoc. Commit it. In `### Ledger Updates` include: `#### Project Status` — one milestone paragraph (Gate 2 complete: PLANNER_TEMPLATE v4.77, nine proposals implemented, conflict-serializability merged into the ACID lens as an Isolation facet per CEO decision, lens count deliberately unchanged at five, `proposed` now 0); `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-2-codification-qa-2026-07-21.md`
>
> **Do NOT move this plan to `Done/`.** The close path is owned by Bellows on continue-verdict consumption (Rule 8) — never by the agent.
