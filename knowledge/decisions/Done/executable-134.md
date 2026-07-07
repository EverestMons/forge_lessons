# Lessons Forge — Gate 2 Codification (cycle 2026-07-06): 10 edits from 13 codify-routed proposals
**Date:** 2026-07-07 | **Tier:** Medium | **Dispatch Mode:** bellows | **Test Scope:** none | **Execution:** Step 1 (SA) → Step 2 (DEV) → Step 3 (QA) | **qa_steps:** 3 | **pause_for_verdict:** always

## CEO Context

Gate 2 of the 2026-07-06 cycle. Gate 1 closed 2026-07-07 (plan 133): 15 proposals routed — 13 codify, 2 reference, 0 backlog. Routes live in `lessons-forge.db` (`status='proposed'`, route set). This plan codifies the 13 codify-routed proposals as **10 distinct edits**: 9 to governance-root `PLANNER_TEMPLATE.md` (live v4.70 — the dedup baseline) and 1 to `forge/agents/FORGE_QA.md`. Same SA → DEV → QA shape as `Done/executable-lessons-forge-gate-2-codification-2026-06-07.md` (the structural precedent for footer convention, prose register, anchor-map shape).

**Proposal set (ids from `gate1-dispositions-2026-07-06.md`; suggested_action/reasoning read verbatim from DB by SA — NOT transcribed here):**

| Proposal | Entry | Edit unit | Target |
|---|---|---|---|
| 133, 134, 137, 143 | 125, 126, 129, 135 | ONE umbrella rule (Cluster-1) | PLANNER_TEMPLATE.md |
| 131 | 123 | root-cause over inherited framing | PLANNER_TEMPLATE.md |
| 132 | 124 | no byte-identical gates on time-dependent scoring | PLANNER_TEMPLATE.md |
| 135 | 127 | cite artifact, don't paraphrase specifics | PLANNER_TEMPLATE.md |
| 136 | 128 | convention change → occurrence-grep | PLANNER_TEMPLATE.md |
| 138 | 130 | verdict prose ≠ instruction channel | PLANNER_TEMPLATE.md |
| 139 | 131 | step composition / Position A check | PLANNER_TEMPLATE.md |
| 142 | 134 | live-canary on daemon activations | PLANNER_TEMPLATE.md |
| 144 | 136 | QA evidence-source substitution | forge/agents/FORGE_QA.md |
| 145 | 137 | evidence-source contract in DB-out-of-git QA steps | PLANNER_TEMPLATE.md (Plan Authoring Checklist) |

**Locked CEO decisions (binding — do NOT re-litigate):**

1. **Cluster-1 (proposals 133/134/137/143) consolidates into ONE scope-derivation umbrella rule** with sub-bullets covering the four constituent disciplines (SA-grep derivation, test-infra inclusion, generator-output enumeration, generous test scoping). Status mechanics at housekeeping: 133 `implemented`, 134/137/143 `superseded` (CEO decision A, 2026-07-07).
2. **Dedup baseline is LIVE PLANNER_TEMPLATE.md v4.70 with git blame on cited lines** (2026-06-07 discipline). Known overlap risks the SA MUST resolve with blame evidence: proposal 136/entry 128 vs existing convention-string rules (Checklist #16 family); proposal 138/entry 130 vs existing verdict-format rules. If fully subsumed, SA flags for CEO with the blame citation instead of authoring text — do not silently drop or silently duplicate.
3. **Proposal 144/entry 136 targets the EXISTING `forge/agents/FORGE_QA.md`** (created 2026-06-12, plan 8). The classifier's "file does not exist" flag was stale. SA additionally verifies whether lessons-forge QA dispatches reference forge's QA specialist; if they do not, SA notes in the blueprint that proposal 145's plan-text contract is the layer that reaches lessons-forge QA, and scopes 144's rule text as forge-project QA guidance — this affects rule wording, not whether the edit ships.
4. **Proposal 145/entry 137 lands in the Plan Authoring Checklist** — plan 130's per-row DB-source rule is the model; the two 2026-07-06 LESSONS entries (qa-discipline, planner-discipline) are its source material.
5. **No version bump in DEV.** `**Version:**` stays 4.70 through this plan; bump to 4.71 is Planner-direct at session-wrap with the Lessons row.
6. **Reference-routed proposals 140/141 are NOT touched by this plan.** Their terminal status ships in a separate migration plan (CEO decision B, 2026-07-07).

---
---

## STEP 1 — SA

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this plan and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Forge SA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge` unless a path says otherwise.
>
> **Scope:**
> - `knowledge/research/gate2-codification-blueprint-2026-07-06.md`
>
> Reads: (a) `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` full file — the v4.70 dedup baseline; (b) `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_QA.md` full file; (c) the canonical DB read-only: `sqlite3 "file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?mode=ro" "SELECT id, entry_id, suggested_action, reasoning FROM lesson_proposals WHERE id IN (131,132,133,134,135,136,137,138,139,142,143,144,145);"` — suggested_action is the authoritative source text, never paraphrase it away; (d) `knowledge/decisions/Done/executable-lessons-forge-gate-2-codification-2026-06-07.md` for footer convention (`Source: proposal N, lesson 2026-07-06`), heading style, and anchor-map shape; (e) this plan's CEO Context including all six locked decisions.
>
> Author ONE blueprint resolving dedup + placement + exact rule text for all 10 edit units. Per unit: (1) disposition APPEND-NEW vs STRENGTHEN-EXISTING, confirmed against the live v4.70 file — for the two flagged overlap risks (proposals 136, 138) run `git log -L` / `git blame` on the candidate existing lines and cite the evidence either way; (2) section home + heading with the next available number in existing style; (3) exact rule body prose DEV will write, with source footer; (4) per-edit anchor map — APPEND-NEW: verbatim line-before/line-after anchors; STRENGTHEN: verbatim old_string/new_string with exact whitespace. The Cluster-1 umbrella is one rule with four sub-bullets; name all four source proposals in its footer. For proposal 144, the FORGE_QA.md edit follows that file's existing section structure.
>
> **Liveness anchors (Rule 41):** one-line claim confirmation before your first read; one-line acknowledgment after each file read; one-line section marker at the start of each blueprint section.
>
> **Deposit:** `lessons-forge/knowledge/research/gate2-codification-blueprint-2026-07-06.md` — dedup pass (with blame citations for 136/138), per-unit dispositions and rule text, anchor map, and an Output Receipt with status, decisions made (final APPEND/STRENGTHEN counts; any unit found fully subsumed → flagged for CEO, not dropped), and flags for next step. In `### Ledger Updates` include `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/research/gate2-codification-blueprint-2026-07-06.md`
>
> STOP. Do NOT proceed to Step 2.

---
---

## STEP 2 — DEV

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this step and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Forge DEV. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge` unless a path says otherwise.
>
> **Scope:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
> - `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_QA.md`
>
> Reads: the Step 1 blueprint at `knowledge/research/gate2-codification-blueprint-2026-07-06.md` (source of truth) and both target files in full.
>
> Apply the blueprint exactly: the PLANNER_TEMPLATE.md edits (per blueprint's final APPEND-NEW/STRENGTHEN dispositions) and the FORGE_QA.md edit. Pre-edit verification per unit: every APPEND-NEW anchor pair exists verbatim at the cited lines; every STRENGTHEN old_string exists verbatim and EXACTLY ONCE. Confirm `**Version:** 4.70` unchanged (no bump — locked decision 5). If ANY anchor or old_string fails to match: set Output Receipt status to Partial, populate Flags for CEO with the mismatch evidence, edit NOTHING, end the step. Every new rule carries its `Source: proposal N, lesson 2026-07-06` footer (Cluster-1 umbrella names all four). If any unit was blueprint-flagged as fully subsumed (pending CEO), skip it and say so in the receipt. Do NOT renumber rules the blueprint does not touch. If the blueprint's edits change or rename any convention string, run `grep -rn '<old-string>'` across governance documents and report every hit as edited or deliberate-survivor (occurrence-grep discipline).
>
> **Deposit:** modified `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md` and `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_QA.md`. Do NOT commit the governance-root or forge files — the Planner commits cross-repo at session-wrap. Output Receipt: per-unit line ranges touched, insert vs in-place counts, pre-edit verification results, flags. In `### Ledger Updates` include `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `/Users/marklehn/Developer/GitHub/PLANNER_TEMPLATE.md`
> - `/Users/marklehn/Developer/GitHub/forge/agents/FORGE_QA.md`
>
> STOP. Do NOT proceed to Step 3.

---
---

## STEP 3 — QA

---

> **FIRST — before any reads or work: post a short visible message to chat (1-2 sentences) confirming you are starting this step and stating your immediate next action.** Do NOT rename the plan file.
>
> You are Forge QA. Read your specialist file at `lessons-forge/agents/FORGE_LESSONS_AGENT.md` first. All commands run from `/Users/marklehn/Developer/GitHub/lessons-forge` unless a path says otherwise.
>
> **Rule 20 self-check is gate-enforced on this step.** Your QA report MUST include the byte-exact banner `Rule 20 — QA Self-Check Results` and a `PASSED — SELF-CHECK PASSED` line; author and run the canonical block per `/Users/marklehn/Developer/GitHub/RULE_20_SELF_CHECK_BLOCK.md`, reproduce its stdout byte-identically, then self-grep your report for the banner.
>
> **Scope:**
> - `knowledge/qa/gate2-codification-qa-2026-07-06.md`
> - `knowledge/qa/evidence/gate2-codification-2026-07-06/git_diff.txt`
>
> Reads: the blueprint (source of truth), both modified target files, `RULE_20_SELF_CHECK_BLOCK.md`.
>
> Verification table, one PASS/FAIL row per check, with line citations: (1) per-unit verbatim match — each of the 10 units present at the blueprint's location with correct heading/number and source footer (one row per unit); (2) STRENGTHEN edits narrow — original text intact, only prescribed additions, before/after cited; (3) Cluster-1 umbrella is ONE rule naming all four source proposals with four sub-bullets; (4) no collateral disturbance — `git diff` in each target repo shows only blueprint-specified ranges; save combined diff to `knowledge/qa/evidence/gate2-codification-2026-07-06/git_diff.txt`; (5) `**Version:** 4.70` unchanged; (6) FORGE_QA.md edit conforms to that file's section structure; (7) any blueprint-flagged subsumed units were skipped by DEV, not edited; (8) canonical Rule 20 block run with `evidence_dir=lessons-forge/knowledge/qa/evidence/gate2-codification-2026-07-06/` and the git_diff evidence file required — stdout banner byte-identical. If any row fails, report and halt.
>
> **Deposit:** `lessons-forge/knowledge/qa/gate2-codification-qa-2026-07-06.md` — verification table, diff evidence reference, Rule 20 block stdout, Output Receipt. Commit ONLY the lessons-forge deposits (blueprint, QA report, evidence) — never the governance-root or forge files. In `### Ledger Updates` include: `#### Project Status` — one paragraph: Gate 2 codification for cycle 2026-07-06 verified (10 edit units: 9 PLANNER_TEMPLATE, 1 FORGE_QA), pending Planner wrap for statuses/version/commits; `#### Prompt Feedback` — standard.
>
> **Deposits:**
> - `lessons-forge/knowledge/qa/gate2-codification-qa-2026-07-06.md`
> - `lessons-forge/knowledge/qa/evidence/gate2-codification-2026-07-06/git_diff.txt`
>
> On full completion, move the plan file to `lessons-forge/knowledge/decisions/Done/` as the absolute last operation.

---

## End-of-Plan Housekeeping (Planner-side, post-QA-verdict — NOT agent work)

1. Bellows owns the terminal Done/ move on continue-verdict consumption.
2. Status advancement (Planner-direct SQL, decision A): `UPDATE lesson_proposals SET status='implemented', status_updated_at='2026-07-07', status_updated_by='planner' WHERE id IN (131,132,133,135,136,138,139,142,144,145);` then `UPDATE lesson_proposals SET status='superseded', status_updated_at='2026-07-07', status_updated_by='planner' WHERE id IN (134,137,143);` — adjust if any unit was subsumed-flagged and CEO-rejected.
3. Version bump 4.70 → 4.71 + Lessons row, Planner-direct.
4. Split commits: governance root (PLANNER_TEMPLATE.md), forge (agents/FORGE_QA.md), lessons-forge (deposits + lifecycle), then submodule pointer bump for lessons-forge at root.
5. Proposals 140/141 terminal status ships in the separate reference-status migration plan (decision B).
