# Lessons Forge — Gate 2 Codification (cycle 2026-07-22) → PLANNER_TEMPLATE v4.78
**Date:** 2026-07-22 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** none | **Execution:** Step 1 (SA) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

Gate 2 of the 2026-07-22 cycle. Gate 1 closed 2026-07-22 (plan 258): fifteen proposals routed **14 codify / 1 reference / 0 backlog**. This plan codifies the **fourteen** `codify` proposals as **eleven edits** to governance-root `PLANNER_TEMPLATE.md` (live **v4.77**, the dedup baseline) and transitions those fourteen to `implemented`.

**⚠️ Proposal 183 is NOT in scope and MUST NOT be touched** — already terminal at `status='reference'` (routed `reference` at Gate 1, "read the record before deriving", already codified as the Integration-vs-Record Floor). Any status write outside the fourteen is a defect.

### The edit map — fourteen proposals, eleven edits (all CEO-ratified 2026-07-22)

| # | Region | Proposals | Edit |
|---|---|---|---|
| E1 | `## The Drafting Cycle` — new rule | **172 + 173 + 179** (merge) | "Execute executable artifacts against real data before deposit" |
| E2 | `## The Drafting Cycle` — new rule | **178** | "A fix is a new draft" — re-run the lens that found the defect ON the fix |
| E3 | `## The Drafting Cycle` — new rule | **180** | "Restructuring for DRY trades a seam surface" |
| E4 | `## The Drafting Cycle` — new rule | **182** | "Sketch the deliverable's physical shape" before deposit |
| E5 | `## The Drafting Cycle` — new **mechanical pass** (NOT a lens) | **185** | "Mechanical conformance pass" — distinct from the five lenses |
| E6 | **NEW `## Halted-Plan Triage` section** | **174 + 175** (merge) | successor ladder + artifact-type-before-disposition |
| E7 | deposit/verification (near Rule 37 / `deposit_exists`) | **176** | a directory-declared deposit is `unmeasurable` (a third outcome) |
| E8 | Orchestration Plan Rules — amend **Rule 36** | **177** | completeness sweeps: `/usr/bin/grep` explicit, bounded, reported as a bounded-negative |
| E9 | Orchestration Plan Rules — **new #57** | **181** | generalize a guard → require the caller to pin the specifics |
| E10 | Orchestration Plan Rules — **new #58** | **186** | pre-state a conclusion only with anchors + licence to disagree + equal evidence burden |
| E11 | Bellows dispatch path rules | **184** | reads-absolute / writes-relative, phrased as operation ROLES |

**⭐ THE TWO MERGES (E1, E6) — CEO-ratified, apply the "related principles belong together" rule (the 249 precedent):**
- **E1 = 172 + 173 + 179.** One spine: *an executable check, computed gate, or repeatable procedure is validated only by RUNNING it against real corpus data before deposit — the five lenses cannot validate an executable check, only running it can.* Fold in each proposal's specific: text-parsing checks prefer extraction-free comparison (canonicalize + longest-common-substring, record the measured range — 172); "a lens pass that HARDENS a check rather than rewriting it is a signal to execute it, not evidence it is sound" (173); run a procedure on the hardest 1-2 real items to confirm the METHOD produces an answer, since "the instructions are correct" and "the instructions work" are separate questions (179).
- **E6 = 174 + 175.** Two halves of triaging a halted plan → one new section: (1) the three-rung successor ladder — slug-reference grep in `Done/` (qualified, or a bare id matches incidental digits), term-search for technical identifiers, date-adjacency (candidate-only, requires body confirmation); each rung's result is bounded. (2) Classify the artifact type before choosing the disposition test — an executable asks whether the CODE shipped; a diagnostic asks whether the QUESTIONS were answered (look in `Done/diagnostic-*`, `knowledge/research/`, restated questions in successors); source code is not evidence either way for a diagnostic.

**⭐ E2 and 178 stay SEPARATE (not folded into E1) — CEO-ratified.** 178's "re-run the lens that found the original defect ON the fix itself; treat the fix as a draft no pass has examined" is a distinct idea from E1's execute-against-real-data (though 178's executable-fix half cross-references E1). **E2 cross-references Plan Authoring Checklist #26** (the sibling-sweep generalized at v4.77) — a fix is a new draft is the lens-side companion to #26's artifact-side sweep; cross-reference, do not duplicate.

**⭐ E5 IS A MECHANICAL PASS, NOT A SIXTH LENS — the lens count stays FIVE, and this is load-bearing.** The five adversarial lenses (destruction/integration/correctness/ACID/…) check a plan against *reality*; E5's conformance pass checks it against the *codified authoring rules* (plan_lint, then walk the Orchestration Plan Rules + Plan Authoring Checklist by scope), run once the plan's shape is stable, before the closing walk. **Verified at authoring:** the two live count phrases — `:333` ("five named lenses") and `:351` ("five heavy passes") — must stay FIVE and unchanged; the only other count reference is the `:1845`/`:1846` changelog rows (historical, PRESERVE). **Do NOT introduce a sixth lens, do NOT sweep counts, do NOT touch the changelog's historical counts.** Word E5 so it is unmistakably a mechanical/non-adversarial pass adjacent to — not inside — the five-lens list.

### Dedup baseline, anchors, section maxima — all verified at authoring against live v4.77 (SA re-derives every one)

- **Version is v4.77** (`:5` `**Version:** 4.77` — bare number, no `v` prefix; `:6` `**Last Updated:**`). Bump both to **v4.78**.
- **Orchestration Plan Rules highest is #56** (v4.77 added #55/#56) → **E9 = #57, E10 = #58.** **Rule 36** is E8's target (amend in place). **Re-derive the max live; do not trust this number.**
- **Plan Authoring Checklist** — E2 cross-references **#26** (the anti-pattern sibling sweep, generalized at v4.77); do NOT edit #26, only reference it. (Note the two independent `### 26.` — Orchestration Rules #26 is "Deposits field convention", unrelated.)
- **No `## Halted-Plan Triage` section exists** (grep 0) → E6 creates a NEW top-level section; SA places it after `## The Drafting Cycle` or where it reads best.
- **The fourteen were grep-verified absent (or adjacent-but-distinct) at Gate 1.** Re-verify each edit's substance against live v4.77 before blueprinting; if any is already present, halt and report rather than adding a competing statement. Known adjacencies to word AROUND, not duplicate: E1 vs `:598` "execute every check" (QA-runtime, not draft-time); E2 vs Checklist #26 (cross-ref); E5 vs `:1252` plan_lint mandate (E5 is broader); E7 vs Rule 37 (extends it); E8 amends Rule 36 in place; E11 vs the existing absolute-path/vacuous-git rules (adds the write-relative half).

**ADR-004 constraint (respect while wording E1-E5):** ADR-004 D6 defers extracting `## The Drafting Cycle` and requires the extracted spec separate **shared doctrine** from the **consequence lens-set**. E1-E5 are consequence-lens/cycle material — word them to stay cleanly separable from general adversarial doctrine. Do NOT perform any extraction here.

**Gate 2 is a governance edit with NO test suite — Planner verification is the safety net (`Test Scope: none`).** SA blueprints exact insertion/replacement text + unique anchors; DEV applies VERBATIM; QA verifies structure. PLANNER_TEMPLATE lives in the governance ROOT — DEV edits it in place by absolute path and it stays **UNCOMMITTED** (the Planner commits cross-repo at wrap).

**⚠️ Wrap-commit protocol (binds the PLANNER).** Between QA's certification and the wrap commit the template sits modified-uncommitted in the main tree. Before committing, the Planner re-runs `shasum -a 256` on the template and matches it against the Step-2 dev-log hash. Match → commit. Mismatch → a post-QA edit landed; investigate. Integrity chain: **SA read (commit pin) → DEV write (A0) → QA read (hash row) → wrap commit (re-match).**

**Scope discipline:** this plan edits ONE file (`PLANNER_TEMPLATE.md`) and transitions FOURTEEN proposal statuses. No `src/`, no schema, no other proposal.

**Deposit-once discipline:** deposited exactly once. **Authoring self-check:** `plan_lint.py` run at authoring — exit 0, (a)-(d) PASS; the one known-benign "step mentions tests but declares no test scope" WARN is the `Test Scope: none` governance-edit class (no suite exists) — do NOT add a test file to any scope to silence it.

## How to Run This Plan

**Bootstrap prompt:**
```
Read the plan at lessons-forge/knowledge/decisions/in-progress-executable-<id>.md (daemon renames the deposited placeholder on claim). Execute Step 1 ONLY. After completing Step 1, STOP and wait for my confirmation. Do NOT proceed to Step 2.
```

---
---

## STEP 1 — SA (Solution Architect)

---

> **FIRST — post a short visible chat message (1-2 sentences) confirming you are starting this plan and your immediate next action.** Do NOT rename the plan file.
>
> You are the Solution Architect. Run commands from your own working tree. The target is governance-root `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` — **READ-ONLY this step; you blueprint, DEV applies.**
>
> **Read the fourteen proposals VERBATIM from canonical, with their source lessons, by DB join (never by ordinal counting):**
> `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT p.id, p.entry_id, p.suggested_action, p.reasoning, e.source_heading, e.raw_content FROM lesson_proposals p JOIN lesson_entries e ON e.id=p.entry_id WHERE p.id IN (172,173,174,175,176,177,178,179,180,181,182,184,185,186) ORDER BY p.id"`
> `raw_content` IS the lesson body. **Confirm exactly fourteen rows and that 183 is ABSENT** (out of scope, terminal).
>
> **Scope:**
> - `knowledge/development/gate-2-blueprint-2026-07-22.md`
>
> **Read the live template regions before blueprinting (re-derive EVERY line number; those in this plan are authoring-time):** `## The Drafting Cycle` (`:314`, with the five-lens list and the two count phrases `:333`/`:351`), `## Orchestration Plan Rules` (`:486`; Rule 36; the tail for the current highest # — expect 56), Plan Authoring Checklist **#26** (for E2's cross-reference), the deposit/`deposit_exists`/Rule-37 region (E7), and the Bellows dispatch path rules (E11). **Pin your read:** record `git -C /Users/marklehn/Developer/GitHub rev-parse HEAD` and the template's last-touching commit (`git -C /Users/marklehn/Developer/GitHub log -1 --format=%H -- PLANNER_TEMPLATE.md`). DEV re-checks the latter before applying.
>
> **Blueprint ELEVEN edits + two mechanical edits — for each: the exact final text, and an exact anchor (a verbatim substring occurring EXACTLY ONCE in the live file — verify uniqueness by grep and state the count), and whether it is an insertion or replacement.** DEV is a faithful applicator and will not improvise.
>
> **E1 — new `## The Drafting Cycle` rule, merging 172+173+179.** Text must state: any executable check, computed gate, or repeatable procedure inside a plan is validated ONLY by running it against real corpus data before deposit — the five lenses cannot validate an executable check; a text-parsing check prefers extraction-free comparison (canonicalize + longest-common-substring), records the measured range; a lens pass that HARDENS a check rather than rewriting it is a signal to execute it, not evidence it is sound; a repeatable procedure is run on the hardest 1-2 real items to confirm the METHOD produces an answer ("the instructions are correct" ≠ "the instructions work").
> **E2 — new rule, 178.** A fix is a new draft: after folding a fix, re-run the lens that found the ORIGINAL defect on the fix itself; where the fix contains an executable step, run it against real data (per E1); treat the fix as a draft no pass has examined. **Cross-reference Plan Authoring Checklist #26** (the artifact-side sibling sweep) — E2 is its lens-side companion; do not duplicate #26.
> **E3 — new rule, 180.** Before splitting or extracting shared content, diff the candidate regions and move only byte-identical clauses; after extraction walk the seam as its own surface (the ACID and destruction lenses have the most purchase there); state the four-part extraction contract — what moves, what stays, how the moved content is retrieved, what the retrieval promises.
> **E4 — new rule, 182.** Before deposit, sketch one real block of the finished deliverable (the actual rows/cells/sections one item produces) and confirm the mandated format can hold everything the plan requires per item; where per-item output is rich, prefer a block-per-item structure with a compact summary index over a table.
> **E5 — new MECHANICAL pass (NOT a lens), 185.** A mechanical conformance pass, distinct from the five adversarial lenses: run plan_lint, then walk the plan against the Orchestration Plan Rules and the Plan Authoring Checklist by scope; run it once the plan's shape is stable, before the closing walk. **Word it as explicitly mechanical/non-adversarial and adjacent to — not inside — the five-lens list. Do NOT alter the lens count; confirm `:333` and `:351` still read "five" unchanged.**
> **E6 — NEW top-level `## Halted-Plan Triage` section, merging 174+175.** (1) The three-rung successor ladder (slug-reference grep in `Done/`, qualified; term-search for technical identifiers; date-adjacency, candidate-only requiring body confirmation) — each rung bounded. (2) Classify the artifact type before the disposition test — executable → did the code ship; diagnostic → were the QUESTIONS answered (`Done/diagnostic-*`, `knowledge/research/`, restated questions in successors); source is not evidence for a diagnostic. Place after `## The Drafting Cycle` or where it reads best; give the section anchor.
> **E7 — extend the deposit-verification rules, 176** (near Rule 37 / the `deposit_exists` description — verify the anchor). A directory-declared deposit is neither present nor missing — a THIRD outcome, `unmeasurable`; fall through to discriminating evidence (a file inside the directory attributable to that plan; the verdict text overrides the `landed` flag).
> **E8 — amend Orchestration Plan Rule 36 in place, 177.** For completeness sweeps: use `/usr/bin/grep` explicitly and state which binary (the shell `grep` is ignore-aware and silently under-reports); bound with `--exclude-dir=.git,.bellows-worktrees,logs` + `--include` globs to stay under step-timeout, and report the bounds as part of the finding; state the result as a bounded negative, never as exhaustive. Preserve Rule 36's existing content; extend it.
> **E9 — new Orchestration Plan Rule #57, 181** (confirm #57 is next). Generalizing a guard into a reusable/generic form: keep the mechanism generic but require the CALLER to pin the specifics; the absence of a pin is a HARD failure. Ask of any generalization: did the concrete version carry information (a list, a count, a name) the general version turns into a judgment call? If so, re-supply the specifics at the point of use.
> **E10 — new Orchestration Plan Rule #58, 186.** Pre-state a conclusion only with (1) named, agent-runnable verification anchors + explicit licence to disagree; (2) a statement that the pre-resolutions are a fact about which items were investigated, not a distribution; (3) equal evidence burden on every disposition, so the cheap/default one is not the low-effort path.
> **E11 — extend the Bellows dispatch path rules, 184.** Split path rules by operation ROLE: READS of shared state (canonical DB, other repos, config) take an ABSOLUTE path; WRITES of the step's own deposits take a path RELATIVE to the agent's working tree; never a blanket "run from X." **Phrase as operation roles, NOT a worktree presupposition** — a lessons-forge cycle ran IN-PLACE 2026-07-22, so the rule is about operation type, not dispatch topology.
>
> **Two mechanical edits:** the version bump `4.77 → 4.78` (bare number, `:5` and `:6`), and a changelog row summarising this Gate 2 — name all fourteen proposals, the eleven edits, the two merges (E1, E6), the new `## Halted-Plan Triage` section, and that **the lens count deliberately stays five** (E5 is a mechanical pass, not a lens). **Append — never rewrite existing changelog rows.**
>
> **Dedup EVERY edit against live v4.77 before blueprinting it** (state the grep + count for each). Already-present substance → halt and report. **Confirm the lens count stays five and the historical changelog counts are untouched.**
>
> **Deposit:** `knowledge/development/gate-2-blueprint-2026-07-22.md` — the eleven edits with exact text + grep-verified unique anchors, the two mechanical edits, the dedup greps with counts, the pinned HEAD + template last-touching commit, and an Output Receipt. Canonical Python file-write — no heredoc. Commit it. `#### Prompt Feedback` in `### Ledger Updates`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-blueprint-2026-07-22.md`
>
> **STOP. Do NOT proceed to Step 2. Wait for CEO verdict.**

---
---

## STEP 2 — DEV

---

> **Before starting, read the Step 1 blueprint and confirm Output Receipt status Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 2.
>
> You are the Forge Developer. Apply the Step-1 blueprint to `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (governance root, ABSOLUTE path, in place) **VERBATIM** — a faithful applicator, not a re-author. If the blueprint and the live template disagree on an anchor, **halt and report**.
>
> **Scope:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` (edit in place; leave **UNCOMMITTED** — the Planner commits at wrap)
> - `knowledge/development/gate-2-codification-dev-2026-07-22.md`
>
> **Task A0 — pre-edit cleanliness gate, with resume disambiguation.** `git -C /Users/marklehn/Developer/GitHub status --short -- PLANNER_TEMPLATE.md` must be **empty**, AND the template's last-touching commit must **match the Step-1 blueprint's**. A clean tree with a different last commit → the template moved after SA read it → **HALT.** **Use `git -C <root>`** — the template is tracked by the ROOT repo; a bare `git status` from your worktree passes vacuously (this is proposal 184, which this plan codifies as E11). **If DIRTY, disambiguate:** grep the modified template for this plan's own anchors (`4.78`; `### 57.`; `### 58.`; `## Halted-Plan Triage`). Any present → this plan's own prior work → (1) snapshot the dirty file aside to a durable gitignored MAIN-tree path (`.bellows-cache/`), record the path; (2) attribute every hunk via `git -C <root> diff` — every hunk must match blueprint content; ANY unattributable hunk = MIXED dirt → HALT, never restore. All attributable → `git -C <root> restore PLANNER_TEMPLATE.md`, verify clean + last-commit match, reapply. **No anchor present → foreign modifications → HALT, do NOT restore.**
>
> **Recovery for a botched apply — SCOPED to this plan's own work:** the pre-edit template is committed (A0 verifies) → `git -C <root> restore PLANNER_TEMPLATE.md` → HALT and report. **Never hand-patch over a bad apply** (the retry belongs to a fresh dispatch, per Rule #56).
>
> **Execute in label order: A0 → A → B → B2 → B3 → C0 → C.**
>
> **Task A — version bump FIRST** (both `:5`/`:6` header lines to `4.78`), so even an early death leaves `4.78` for A0's anchor test on re-dispatch.
> **Task B — apply E1 through E11 exactly as blueprinted.** After each, grep-confirm the new text landed. **Section-scoped greps:** confirm E9/E10 landed in **Orchestration Plan Rules** as #57/#58; confirm E8 amended **Rule 36** (not another rule); confirm E2 only CROSS-REFERENCES Checklist #26 and did not edit it; confirm the new `## Halted-Plan Triage` section exists.
> **Task B2 — apply the CHANGELOG row** (append; never rewrite). Must name **v4.78** (matching Task A), the fourteen proposals, the eleven edits, the two merges, the new section, and that the lens count stays five.
> **Task B3 — the count guard.** Confirm `:333` and `:351` still read **five** and were NOT altered, and the historical changelog counts (`:1845`/`:1846` "five"/"four") are intact. Report both as explicit checks. **E5 adds a mechanical pass, not a lens — no count sweep.**
> **⚠️ TASK ORDER IS LOAD-BEARING — the template edit (A/B) MUST complete before the DB transition (C).** If the template lands and the DB fails, the corpus says `proposed` while the template carries the rule — recoverable, obvious at the gate. If the DB landed first and the template failed, the corpus asserts fourteen `implemented` with no codification behind them — a false permanent claim no later gate re-checks.
> **Task C0 — DB PRECONDITION, immediately before the write** (found by applying E1's own execute-before-deposit discipline to this plan): read + assert the fourteen ids (172-186 except 183) are each `status='proposed'` AND `route='codify'` (already `implemented` → prior dispatch, idempotent, proceed; any other status/route → HALT); and **183 is still `status='reference'`** (moved → HALT). Report as RAW CLI output.
> **Task C — transition the FOURTEEN to `implemented`.** Take a restore point first (`.backup`, MAIN-tree absolute path, colon-free; HALT if it fails/zero-bytes). Then `UPDATE lesson_proposals SET status='implemented', status_updated_at=<UTC now>, status_updated_by='ceo' WHERE id IN (172,173,174,175,176,177,178,179,180,181,182,184,185,186)` — parameterised, **never a bare UPDATE without WHERE**; **183 MUST NOT appear** and must remain `reference` (read it back to prove untouched). `conn.commit()` once.
>
> **Deposit:** `knowledge/development/gate-2-codification-dev-2026-07-22.md` — the applied-edit confirmations (section-scoped greps), the B3 count-guard results, before/after status distributions as RAW output, the **post-Task-C per-id read as RAW `sqlite3` CLI output** (`SELECT id, status, status_updated_at, status_updated_by FROM lesson_proposals WHERE id IN (172,173,174,175,176,177,178,179,180,181,182,183,184,185,186) ORDER BY id` — include 183 so its untouched row is visible; QA byte-compares raw-to-raw), the backup path, and the **post-edit template hash** (`shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`). Canonical Python file-write — no heredoc. **Commit the dev-log only — NOT the template.** `#### Prompt Feedback` in `### Ledger Updates`.
>
> **Deposits:**
> - `lessons-forge/knowledge/development/gate-2-codification-dev-2026-07-22.md`
>
> **STOP. Do NOT proceed to Step 3. Wait for CEO verdict.**

---
---

## STEP 3 — QA

---

> **Before starting, read the Step 1 + Step 2 deposits and confirm both Output Receipts Complete; otherwise halt and report.** Post a short visible chat message confirming you are starting Step 3 (QA). You are Lessons Forge QA. **Verification + reporting only — no template edits, no DB writes.** If a check fails, report it — do NOT fix it. Do NOT use Monitor. Do NOT edit PROJECT_STATUS directly.
>
> **MANDATORY — Rule 20 self-check banner.** Deposit MUST contain, verbatim, `## Rule 20 — QA Self-Check Results` and a line `**PASSED — SELF-CHECK PASSED**`. End with a self-grep confirming the banner.
>
> **Evidence rule.** Deposit **RAW command output, never a summary.** Every DB row states which DB.
>
> **Scope:**
> - `knowledge/qa/gate-2-codification-qa-2026-07-22.md`
>
> Verification table, one row per claim:
> 0. **Template integrity — FIRST.** `shasum -a 256 /Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` byte-compared against the Step-2 dev-log hash. Mismatch → halt (every row below would certify bytes DEV never produced).
> 1. **Version 4.78** on both `:5`/`:6` header lines (no `v` prefix on `:5`).
> 2. **E1-E5 present in `## The Drafting Cycle`** — quote each. Confirm E1 names execute-against-real-data for checks AND procedures; E2 cross-references #26 without editing it; **E5 is a MECHANICAL pass, explicitly NOT a lens — the lens list still runs 1–5 and `:333`/`:351` still read "five".** A sixth lens or altered count is a FAIL.
> 3. **E6 — the new `## Halted-Plan Triage` section exists** with both halves (successor ladder + artifact-type triage) — quote the section head + key clauses.
> 4. **E7 present** (directory deposit `unmeasurable`), **E8 amended Rule 36** (`/usr/bin/grep` + bounds; Rule 36's prior content retained), **E11 present** (reads-absolute/writes-relative as roles) — quote each; confirm the anchors are the intended ones.
> 5. **E9=#57, E10=#58** in Orchestration Plan Rules (section-scoped; state the section). Confirm #56 is the prior highest and nothing renumbered.
> 6. **The historical changelog counts (`:1845`/`:1846`) are INTACT** — quote them. This plan swept no counts.
> 7. **New changelog row** for this Gate 2 naming the fourteen proposals, the two merges, the new section, and the lens-count-stays-five decision.
> 8. **The fourteen proposals are `implemented`.** Re-run the Step-2 per-id query as raw CLI and byte-compare against the Step-2 block: 172,173,174,175,176,177,178,179,180,181,182,184,185,186 → `implemented`, `status_updated_by='ceo'`.
> 9. **⚠️ 183 UNTOUCHED at `status='reference'`.** 183 at `implemented` is a FAIL (out of scope).
> 10. **Corpus totals:** 178 entries, 186 proposals; **`proposed` is now 0** (the fourteen were the last). Report actuals.
> 11. **No `src/` change, no schema drift** — `git -C /Users/marklehn/Developer/GitHub/lessons-forge status --porcelain -- src/` empty.
>
> If any row fails, report and halt.
>
> **Deposit:** `knowledge/qa/gate-2-codification-qa-2026-07-22.md` — verification table, raw output, the Rule 20 banner + PASSED line, Output Receipt. Canonical Python file-write — no heredoc. Commit it. In `### Ledger Updates` include `#### Project Status` (one milestone paragraph: Gate 2 complete — PLANNER_TEMPLATE **v4.78**, fourteen proposals implemented, two merges [E1 execute-before-deposit, E6 halted-triage], a new `## Halted-Plan Triage` section, the mechanical conformance pass added distinct from the five lenses, lens count deliberately five, `proposed` now 0; the 2026-07-22 lessons arc is COMPLETE) and `#### Prompt Feedback`.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate-2-codification-qa-2026-07-22.md`
>
> **Do NOT move this plan to `Done/`.** The close path is owned by Bellows on continue-verdict consumption (Rule 8) — never by the agent.
