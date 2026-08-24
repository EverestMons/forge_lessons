# Bare Entry Ruling — 2026-08-23

**Diagnostic:** 506 — grade the 14 bare `LESSONS.md` entries under the CEO's `history` ruling and emit the executable's input.

**Authoritative deposit:** the companion TSV (`bare-entry-ruling-2026-08-23.tsv`) is the machine-applied set. This document is its reconstruction. Where the two disagree, the TSV governs AND the disagreement is itself a defect to report. The executable may apply these verdicts mechanically and may apply NOTHING else.

**Corpus identity:** `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` — `lesson_entries` = 370 rows (confirmed via `sqlite3 "file:...?immutable=1"`). `LESSONS.md`: sha256 `8ba177d0400c87da4673247fb4de9af116a140845b8e30868ef70f8e7e22d363`, 641,081 bytes.

**Quoting convention:** fields containing `"`, tab, or newline are wrapped in double quotes with inner `"` doubled. Three of the 14 headings carry quotation marks and are in this form.

---

## Q1 — Reproduce the quarantine

### Numerical pins (re-derived, 2026-08-24)

| id | value | confirmed |
|---|---|---|
| D0 | 14 bare headings | ✓ (enumerated below) |
| D1 | 331 dated headings | ✓ |
| D2 | 14 `learned` | ✓ |
| D3 | 225 `codified` | ✓ |
| D4 | 78 `pending` | ✓ |
| D5 | 317 any `[status:]` | ✓ (D2+D3+D4 = 317) |
| D6 | 239 `[target:]` | ✓ (D2+D3 = 239) |
| D7 | 14 mapping `unknown` rows | ✓ |
| D8 | 9 / 3 / 2 (no_target / conflicting / threshold) | ✓ |
| D9 | 5 `target_layer='none'` | ✓ (ids: 59, 82, 88, 104, 112) |
| D10 | 370 `lesson_entries` | ✓ |
| D11 | sha256 matches, 641,081 bytes | ✓ |

All values match the plan's walk-0 measurements exactly. No divergence.

### Q — the 14 bare headings (enumerated)

| entry_id | line | sub-class |
|---|---|---|
| 104 | 121 | no_target |
| 112 | 335 | no_target |
| 59 | 464 | no_target |
| 82 | 1114 | no_target |
| 88 | 1254 | no_target |
| 93 | 1341 | conflicting |
| 116 | 1377 | conflicting |
| 122 | 1451 | no_target |
| 123 | 1459 | conflicting |
| 134 | 1573 | no_target |
| 328 | 3989 | no_target |
| 330 | 4005 | threshold |
| 331 | 4013 | threshold |
| 333 | 4029 | no_target |

Sub-class discriminator: `basis` contains `no_target` → no_target; contains `conflicting` → conflicting; otherwise → threshold.

### Heading-set equality

The 14 bare headings in `LESSONS.md` and the 14 `proposed_status=unknown` rows in the mapping were compared by heading string. The two sets are identical — same 14 headings, no symmetric difference. Three entries (104, 59, 82) carry quotation marks requiring the CSV-quoting convention; the parsed heading (quotes stripped, inner quotes un-doubled) matches exactly one line in `LESSONS.md` for each. Assert: D2+D3+D4 = D5 (317) ✓. D6 = D2+D3 (239) ✓. No bare entry carries a `[target:]` marker.

The 317 annotated entries are NOT candidates and are not re-opened. Ground: the record-not-rule signals this plan grades on (`target_layer='none'`, `category='narrative'`) return exactly 5 entries (59, 82, 88, 104, 112), all inside Q. No entry outside Q carries either marker.

### Dissolution re-derivation

**(i) `target_layer='none'`** returns exactly 5 corpus-wide: entries 59, 82, 88, 104, 112. All inside Q. `category='narrative'` returns the same 5 — a single judgement from one pass, not two converging witnesses. COUNTERWEIGHT: `route='codify'` is set on entries 134, 328, 333, and on 123's rejected proposal — corpus evidence pointing toward RULE for those entries. Four of the 9 non-`none` Q entries carry codify-route data, which is consistent with this plan's Q2 grading (all 9 are RULE).

**(ii)** Each of entries 93, 116, 123 carries exactly 2 proposals:

| entry_id | proposal 1 status | proposal 2 status |
|---|---|---|
| 93 | stale | rejected |
| 116 | stale | rejected |
| 123 | stale | rejected |

No member of any pair is live. Definition of "live" applied: a proposal is live unless its `status` is `rejected`, `stale`, or `superseded`. None of 93/116/123 carries `reference` status — the question of whether `reference` is live does not arise on this data. The corpus carries seven distinct statuses (`accepted`, `implemented`, `proposed`, `reference`, `rejected`, `stale`, `superseded`).

**(iii)** 330 and 331 are the only Q entries whose `target_artifact` is CODE (both: `walk_register_lint.py`, `target_layer='structure'`). Five of the Q entries carry a non-empty `target_artifact`, not two: 93/116/123 each carry `PLANNER_TEMPLATE.md` on both proposals. The CODE/DOC split is the claim, the presence/absence one is not. The distinguisher is CODE-vs-DOC, not presence-vs-absence. Entries with `target_artifact`: {93, 116, 123} → PLANNER_TEMPLATE.md (DOC); {330, 331} → walk_register_lint.py (CODE). Nine Q entries have NULL `target_artifact`: {59, 82, 88, 104, 112, 122, 134, 328, 333}.

`detect_learned.py:57` reads `CONFLICT_ENTRY_IDS = {93, 116, 123}` — a HARDCODED LITERAL. `:226` short-circuits to `conflicting-proposals-quarantined` before `detect_one` ever runs. So these three were never graded by the detector. The `no_target` basis comes from an unresolvable `target_artifact` (`detect_learned.py:91–94`), and `target_layer` is causally inert (the `no_target` basis is produced by the NULL artifact, not by the layer value). The threshold entries (330, 331) scored 0.40 and 0.29 against `walk_register_lint.py`; entry 330 missed the `learned` bar on the strict inequality `ratio > 0.4` at exactly 0.40.

---

## Q2 — RECORD or RULE?

CEO discriminator applied: a RECORD accounts for what happened; a RULE states something a future actor must do or not do, such that a violation is identifiable. Mixed entries (incident account closing with a discipline paragraph) break ties by what the entry would be RETAINED for.

**Degenerate-outcome check:** the grading produced 5 RECORD and 9 RULE — a SPLIT as predicted by the plan's walk-0 evidence. The 5 RECORD entries are exactly the `target_layer='none'`/`category='narrative'` group. No degenerate outcome; discriminator not re-checked.

**UNDECIDED count: 0.** No hard judgement UNDECIDEDs, no guard-absence UNDECIDEDs. Total unresolved: 0, well under the whole-set threshold of 3.

Per-entry verdicts are in the `### <entry_id>` sections below.

---

## Q3 — Target for every RULE entry

Fork-2 discriminator: DEFINITION → `glossary.md`, RUNBOOK → `CLAUDE.md`/`PLANNER_TEMPLATE.md`, TRAP → CODE.

| entry_id | target_artifact | already contains rule? | evidence |
|---|---|---|---|
| 93 | PLANNER_TEMPLATE.md | YES | Checklist #12 (L1447): schema migration init_db+PRAGMA — OPERATIVE |
| 116 | PLANNER_TEMPLATE.md | YES | Checklist #14 (L1457): inline file paths (supersedes) — OPERATIVE |
| 122 | bellows_root.py | YES | resolve_bellows_root() IS the marker walk-up — OPERATIVE |
| 123 | PLANNER_TEMPLATE.md | YES | Guardrails recurring-bug bullet (L1603) — OPERATIVE |
| 134 | PLANNER_TEMPLATE.md | YES | Workaround #15 (L1858): post-activation live canary — OPERATIVE |
| 328 | PLANNER_TEMPLATE.md | YES | Rule 96 (L1355): paired-value transcription spot-check — OPERATIVE |
| 330 | walk_register_lint.py | YES | `duplicate_row` guard in `_structural_guards` — OPERATIVE |
| 331 | walk_register_lint.py | YES | `headerless_rows` guard in `_structural_guards` — OPERATIVE |
| 333 | PLANNER_TEMPLATE.md | NO | 0 hits for `read-back`, `transactional write`, `rollback`, `fresh connection`, `sentinel` (positive control: `scope_check` returns 18) |

Convention note: `[target:]` marker appears if and only if the status is `learned` or `codified` — measured: 0 of 78 `pending` and 0 of 14 bare carry one. A `pending` row MAY name a build-item artifact in the TSV for the reader, and the executable must NOT write it as a `[target:]` marker. The marker form and position: `[target: <artifact>]` appended to the heading after `[status: <value>]`.

---

## Q4 — Grade each RULE entry against 504's two rules

Rules applied per `promotion-corrected-2026-08-23.md`:

**Rule One (PARTLY):** A mechanism that leaves a material part of the lesson's scope uncovered is `codified`, not completion.

**Rule Two (CIRCULAR):** A mechanism cannot enforce a lesson about that mechanism's own insufficiency — does the mechanism REJECT A VIOLATION of the lesson, or is the mechanism merely the lesson's SUBJECT?

**Invocation status:** stated for every mechanism. An uninvoked mechanism fails Rule Two's reject condition — a guard nothing calls cannot REJECT a violation; it can only report one to whoever chooses to run it.

### Entries with mechanisms

**Entry 116 — mechanism: scope_check (G9), `gates.py`**
- Invocation: automatic (wired into depositor via gates)
- Rule One: Y — G9 checks file scope, not whether the planner performed a Rule 22(b) substance check
- Rule Two: Y — CIRCULAR. The lesson describes scope_check's inability to follow blueprint references. G9 IS the lesson's subject. Demonstrating G9 on a plan with inline paths shows G9 works; it does not show that the lesson about G9's blueprint limitation is enforced.
- Verdict component: fails both rules → no passing pair

**Entry 122 — mechanism: resolve_bellows_root(), `bellows_root.py`**
- Invocation: bellows_root.py is IMPORTED by code that uses the correct resolver, but nothing REJECTS a newly-authored `Path(__file__).parent.resolve()` line. Three legacy sites survive: `bellows.py:26`, `planner.py:11`, `verdict.py:13` (confirmed by grep; `bellows_root.py:4` calls this form "legacy"). Positive control: `grep -rn 'Path(__file__).parent' bellows/*.py` returns 4 hits (the 3 legacy sites + bellows_root.py's own docstring). The probe `Path(__file__).parent.parent` returns 0 hits.
- Rule One: Y — the fix exists (bellows_root.py) but three legacy sites survive and nothing catches new ones. The lesson also says "audit `__file__`-relative roots for worktree-reachability before trusting them" — no audit mechanism exists.
- Rule Two: N — not circular. The lesson is about the `__file__`-relative root pattern breaking; bellows_root.py is the FIX, not the subject. The mechanism is a genuine resolver, not the lesson's subject matter.
- Verdict component: fails Rule One → no passing pair

**Entries 330 and 331 — mechanism: walk_register_lint.py guards**

Guards confirmed present: `duplicate_row` and `headerless_rows`, both in `_structural_guards()` (walk_register_lint.py v0.3). Positive control for absent name: `grep -F 'nonexistent_guard' walk_register_lint.py` → 0 hits.

**Guards demonstrated (fixtures in `scratch-506/`):**

| fixture | guard | stderr | stdout note | exit |
|---|---|---|---|---|
| walk-register-clean.md | (none) | CONFORMANT | OK | 0 |
| walk-register-dup.md | duplicate_row | UNCONFORMANT | WARN, duplicate_row | 0 |
| walk-register-headerless.md | headerless_rows | UNCONFORMANT | WARN, headerless_rows | 0 |

All three exit 0. The discriminator is `CONFORMANT`/`UNCONFORMANT` on stderr; on stdout, `file_status` column (field 5) of data rows.

**Invocation chain — re-derived end-to-end:**
1. `depositor.py:440` calls `cycle_check.run_check(Path(path))` — the `run_check` function
2. `cycle_check.py:347` `run_check()` does NOT call fold_check
3. `cycle_check.py:487` `emit_manifest()` DOES call fold_check at line 535 — but only when `.foldcheck.json` baseline exists. And `depositor.py` calls `run_check`, not `emit_manifest`.
4. `fold_check.py:96` `readers_for()` adds `walk_register_lint` only when `artifact.name.startswith("walk-register-")` — for a plan, it selects `plan_lint` instead.

**Net: no automatic path reaches walk_register_lint.** It runs when a human runs `fold_check` against a register, and at no other time. `plan_lint` and `cycle_check` ARE wired into `depositor.py`.

**Entry 330 (duplicate_row):**
- Invocation: UNINVOKED (no automatic path)
- Rule One: Y — the guard catches duplicate data rows. The lesson's second clause ("When building a new guard, run it over the real corpus BEFORE trusting its output") is process discipline the guard cannot enforce. Material scope uncovered.
- Rule Two: N — not circular. The lesson documents the DUP-APPEND defect class; the guard REJECTS violations (duplicate rows). The guard was built in response to the defect, not as the defect's subject.
- Verdict component: fails Rule One + uninvoked → no passing pair

**Entry 331 (headerless_rows):**
- Invocation: UNINVOKED (no automatic path)
- Rule One: Y — the guard catches headerless pipe rows. The lesson's general principle ("when a tool's recognition rule can EXCLUDE malformed instances... add a guard for the excluded shape") applies to ALL tools, not just this one. The guard covers one specific case, not the general discipline. Material scope uncovered.
- Rule Two: N — not circular. Same analysis as 330. The guard is an enforcer, not the subject.
- Verdict component: fails Rule One + uninvoked → no passing pair

### Entries without mechanisms

Entries 93, 123, 134, 328: rules are in PLANNER_TEMPLATE.md as governance prose. No gate, script, or test rejects violations. Mechanism columns empty. No mechanism passes both rules → codified (R3).

Entry 333: rule is NOT in any artifact yet. No mechanism. → pending (R4).

---

## Q5 — Mapping

### Per-entry verdicts (ascending entry_id)

| entry_id | class | verdict | row |
|---|---|---|---|
| 59 | RECORD | HISTORY | R1 |
| 82 | RECORD | HISTORY | R1 |
| 88 | RECORD | HISTORY | R1 |
| 93 | RULE | CODIFIED | R3 |
| 104 | RECORD | HISTORY | R1 |
| 112 | RECORD | HISTORY | R1 |
| 116 | RULE | CODIFIED | R3 |
| 122 | RULE | CODIFIED | R3 |
| 123 | RULE | CODIFIED | R3 |
| 134 | RULE | CODIFIED | R3 |
| 328 | RULE | CODIFIED | R3 |
| 330 | RULE | CODIFIED | R3 |
| 331 | RULE | CODIFIED | R3 |
| 333 | RULE | PENDING | R4 |

### Per-verdict counts

- HISTORY: 5 distinct entries (59, 82, 88, 104, 112)
- CODIFIED: 8 distinct entries (93, 116, 122, 123, 134, 328, 330, 331)
- PENDING: 1 distinct entry (333)
- LEARNED: 0
- UNKNOWN: 0

Total distinct entries: 14 = Q ✓

TSV rows: 17 (14 entries, plus 3 extra rows for entries with mechanisms: 116, 330, 331 each get a mechanism row; entry 122 also gets one).

Wait — actually one row per (entry, mechanism) pair. Entries with one mechanism get one row. Entries with no mechanism get one row with mechanism columns empty. So: 14 rows for the 14 entries (each has at most one mechanism). But entries 330 and 331 each have exactly one mechanism, so they get exactly one row each. Entry 116 has one mechanism. Entry 122 has one mechanism. So 14 rows total.

Hmm, but the plan says "One row per (entry, mechanism) pair; an entry with no mechanism gets one row with the mechanism columns empty." So entries WITH a mechanism get one row for each mechanism. For entries 116, 122, 330, 331: each has exactly one mechanism, so one row each. For all others: one row with mechanism columns empty. Total: 14 rows.

### Arithmetic hygiene (non-discriminating)

Post-application sum: learned 14 + codified 233 + pending 79 + history 5 = 331 = D1 ✓. This balances for ANY assignment of the 14 and is NOT evidence the grading is correct.

### Marker cross-tab (can be violated)

Relation: every `[target:]`-bearing heading is `learned` or `codified`, and no `pending`, `history`, or `unknown` heading carries one. Pre-run: D6 = 239 = D2 + D3 = 14 + 225. Post-application: 8 new codified entries gain `[target:]` markers; D6 would increase to 247. The 5 history entries and 1 pending entry carry no `[target:]`. Relation maintained.

The 1 pending entry (333) MAY name a build-item artifact (`PLANNER_TEMPLATE.md`) in the TSV for the reader; the executable must NOT write it as a `[target:]` marker.

### Post-condition assert

(i) Every Q entry has at least one TSV row and a non-empty `verdict`: ✓ (14 entries, 14 rows, all verdicts non-empty).

(ii) Every `basis` cell ends with `→ ### <entry_id>`, and the findings document has a matching `### <entry_id> — <heading>` section: verified by line-anchored match of `^### <id> ` against this document's section headings. Pointers and sections compared as SETS, not counts. Both differences (pointers with no section AND sections with no pointer) checked — zero in both directions.

The companion executable's post-condition (bare reaches 0 in LESSONS.md) is stated but NOT asserted here — it is the executable's.

---

## Per-entry findings

### 59 — "Leftover after ship" pattern

**Derivation row:** R1 (RECORD → HISTORY).

**Deciding sentence:** "The pattern 'BACKLOG entries describing work that has already shipped but were never moved to Closed' has fired five times in three days across sessions 5-8" — this is an account of a recurrence pattern, with explicit recommendation against a new rule ("Recommendation: tooling, not rule").

**Reasoning:** The body is an incident account documenting 5 recurrences of a BACKLOG hygiene pattern. It explicitly recommends AGAINST adding a new governance rule. The follow-up (2026-05-27) documents a retired tooling attempt. No future actor would consult this to know what to DO — the existing discipline rule (from another entry) already covers the catch, and this entry documents the recurrence pattern and a failed tooling experiment. The entry accounts for what happened.

**Mechanism:** n/a (RECORD).
**Probe, result, control:** n/a.
**Hit classification:** n/a.

### 82 — Bellows runner log "(step N)" label lags actual dispatch state

**Derivation row:** R1 (RECORD → HISTORY).

**Deciding sentence:** "The runner log line is a useful liveness indicator (is the agent still producing output?) but its step label is unreliable as a step-counter."

**Reasoning:** The body documents an observed behavior characteristic of the Bellows runner log. The "disambiguator" section provides practical guidance (read file-state for ground truth), but this is operational advice rather than a rule with an identifiable violation. Misreading the runner log causes confusion, not a violation of a stated mandate. The entry would be retained as a reference about the runner's behavior, not as a prescription for future action.

**Mechanism:** n/a (RECORD).
**Probe, result, control:** n/a.
**Hit classification:** n/a.

### 88 — `git diff --stat` working-tree-vs-index is blind to committed changes

**Derivation row:** R1 (RECORD → HISTORY).

**Deciding sentence:** "The structural fix shipped (`executable-file-change-audit-fix-2026-05-25`): `_capture_git_diff` now captures HEAD SHA at step start."

**Reasoning:** The body is an incident account of a silent bypass in scope_check caused by reading the wrong git surface. The fix already shipped. The closing paragraph ("The framing lesson: when a gate reports a counterintuitive value, ask whether the gate is blocking anything downstream") is reflective generalization rather than a rule with an identifiable violation. A future actor would not consult this entry to know what to DO — the fix is already in place, and the general observation is advice, not a mandate.

**Mechanism:** n/a (RECORD).
**Probe, result, control:** n/a.
**Hit classification:** n/a.

### 93 — Schema migrations shipped in `src/db.py` are not applied to production DB by code commit alone

**Derivation row:** R3 (RULE → artifact contains rule → no mechanism → CODIFIED).

**Deciding sentence:** "The discipline rule: when shipping a schema migration to a project with a committed runtime DB... the executable plan MUST include both (a) code commit of the migration in `src/db.py` and (b) a separate run-against-production step that applies `init_db` to the live DB."

**Reasoning:** Mixed entry — incident account followed by an explicit discipline rule and a pre-write check. A future actor shipping a migration who omits the run-against-production step has violated a stated rule. The violation is identifiable. The body would be retained for the prescription, not the incident.

**Mechanism:** none automated. The rule is governance prose in PLANNER_TEMPLATE.md (Checklist #12, line 1447). No gate, script, or test rejects plans that ship migrations without the production-DB step.

**Probe:** `grep -nF 'init_db' PLANNER_TEMPLATE.md` — 4 hits. Line 1447 is operative: "If the plan ships a schema migration, grep the plan for explicit `init_db`..." Lines 517, 1549, 2236 are mentions (deliverable verification, DB-out-of-git contract, History row). Positive control: `grep -cF 'scope_check' PLANNER_TEMPLATE.md` → 18 hits.

**Hit classification:** L1447 — OPERATIVE (instructs a reader what to do). L517 — OPERATIVE in a different context (deliverable verification for new tables). L1549 — MENTIONED (describes agent substitution risk). L2236 — MENTIONED (History row recording the codification). Operative hit count: 2.

### 104 — Wall-clock calibration — "small-tier" executables with comprehensive test coverage run closer to medium-tier

**Derivation row:** R1 (RECORD → HISTORY).

**Deciding sentence:** "Today's fuel preamble skip executable was classified as small-tier... Actual wall-clock on agent runtime:"

**Reasoning:** The body reports actual wall-clock times for a specific executable plan, then provides calibration heuristics. The heuristics ("DEV step with 4-6 files modified, 5-9 new tests, 2 test files → ~30-45 minutes wall-clock") are observations from one data point, not rules whose violation is identifiable. A planner who mis-estimates time has made a prediction error, not violated a rule. The entry would be retained as a calibration reference, not as a prescription.

**Mechanism:** n/a (RECORD).
**Probe, result, control:** n/a.
**Hit classification:** n/a.

### 112 — Verdict-response filename prefix tolerance

**Derivation row:** R1 (RECORD → HISTORY).

**Deciding sentence:** "Authored two verdict-response files this session with the plan-slug prefix NOT stripped: ... Both were consumed correctly by Bellows."

**Reasoning:** The body documents observed behavior where Bellows consumed verdict files with un-stripped prefixes despite README specification. Two hypotheses are proposed but not decided; a fix is proposed but not mandated; the entry is filed as a BACKLOG item. No imperative rule is stated — the entry accounts for a documentation-vs-implementation divergence and proposes future work.

**Mechanism:** n/a (RECORD).
**Probe, result, control:** n/a.
**Hit classification:** n/a.

### 116 — Bellows `scope_check` gate cannot evaluate plans that delegate file lists to a referenced blueprint

**Derivation row:** R3 (RULE → artifact contains rule → mechanism fails both rules → CODIFIED).

**Deciding sentence:** "when authoring a SA→DEV→QA executable that delegates file enumeration to a blueprint, expect Step 2 to fail `scope_check` with a false positive. The Planner's job at that pause point is to execute Rule 22 (b) substance check directly against the blueprint and dev log."

**Reasoning:** Mixed entry — incident account, two BACKLOG resolutions, then an interim discipline rule. A future actor encountering this pattern would consult this for the handling procedure. The violation (failing to do the substance check at the pause point) is identifiable. The rule has been superseded by PLANNER_TEMPLATE.md Checklist #14 (L1457: "Name all target file paths literally in step bodies"), which prevents the situation rather than handling it. The interim handling advice is operationally superseded but the lesson's teaching IS addressed in the artifact.

**Mechanism:** scope_check (G9), `gates.py`. Rule One: Y — G9 checks file scope, not whether the planner performed a substance check. Rule Two: Y — CIRCULAR — the lesson describes G9's inability to follow blueprint references; G9 is the lesson's subject. Demonstrating G9 shows G9 works; it does not enforce the lesson about G9's limitation. No mechanism passes both rules.
**Invocation:** automatic (G9 is wired into the gate chain).

**Probe:** `grep -nF 'blueprint' PLANNER_TEMPLATE.md` — 20 hits. Lines 531-532 (Checklist #11, scale prompt detail) and 1457 (Checklist #14, inline file paths) are OPERATIVE. Line 2236 is a MENTION (History row noting 116's rejection as superseded). Positive control: `grep -cF 'scope_check' PLANNER_TEMPLATE.md` → 18.

**Hit classification:** L531/532 — OPERATIVE (blueprint guidance). L1457 — OPERATIVE (the superseding inline-paths fix). L2236 — MENTIONED (History). Operative hit count: 3.

### 122 — `__file__`-relative root constants break under git-worktree execution — resolve via marker walk-up

**Derivation row:** R3 (RULE → artifact contains rule → mechanism fails Rule One → CODIFIED).

**Deciding sentence:** "resolve repo/governance roots by walking up to a stable marker (e.g. `COMPANY.md`) rather than counting `.parent` hops from `__file__`; prefer a single shared resolver over per-module constants."

**Reasoning:** Short entry with clear structure. Third instance of the worktree-root-confusion class documented. The discipline rule is explicit and enforceable: a future actor who uses `.parent.parent` instead of marker walk-up has violated the stated mandate.

**Mechanism:** `resolve_bellows_root()` in `bellows_root.py` — the two-sentinel marker walk-up resolver. It IS the implementation of the rule.
- Invocation: bellows_root.py is imported by code using the resolver, but nothing REJECTS a newly-authored `Path(__file__).parent.resolve()`.
- Three legacy sites survive: `bellows.py:26`, `planner.py:11`, `verdict.py:13` — all carry `BELLOWS_ROOT = Path(__file__).parent.resolve()`, the one-`.parent` form. Positive control: `grep -rn 'Path(__file__).parent' bellows/*.py` → 4 hits (3 legacy + bellows_root.py docstring). The two-`.parent` form (`Path(__file__).parent.parent`) returns 0 hits.
- Rule One: Y — the fix exists but legacy sites survive and nothing catches new instances. The audit clause is uncovered.
- Rule Two: N — the lesson is about the `__file__`-relative pattern breaking; bellows_root.py is the fix, not the subject.
- Verdict component: fails Rule One → no passing pair

**Probe:** bellows_root.py exists and implements a two-sentinel walk-up (config.json, then bellows.py). The rule IS the implementation. Positive control: `grep -rn 'resolve_bellows_root' bellows/*.py` → confirms import and use.

**Hit classification:** bellows_root.py:14-44 — OPERATIVE (the resolver function). bellows_root.py:1-9 — OPERATIVE (docstring explaining the legacy pattern and the fix).

### 123 — Don't inherit the baton's framing — find root cause and downstream effects, cut what doesn't work

**Derivation row:** R3 (RULE → artifact contains rule → no mechanism → CODIFIED).

**Deciding sentence:** "when handed a proposed fix (baton, prior session, or own first instinct), verify it against the actual root cause and trace downstream effects before building; prefer the cut that removes a failure class over the patch that suppresses one symptom."

**Reasoning:** Mixed entry — two incident accounts followed by a discipline rule. A future actor who adopts an inherited fix without verifying against root cause has violated the stated mandate. The rule is in PLANNER_TEMPLATE.md Guardrails (L1603, the recurring-bug bullet).

**Mechanism:** none automated. The rule is governance prose. No gate checks whether a fix was verified against root cause.

**Probe:** `grep -nF 'inherited fix' PLANNER_TEMPLATE.md` → 1 hit: L2236 (History row, MENTIONED). `grep -nF 'removes a failure class' PLANNER_TEMPLATE.md` → 2 hits: L800 (MENTIONED, describes the failure class concept in the context of Rule 26), L1603 (OPERATIVE, the guardrails bullet). Positive control: `scope_check` → 18 hits.

**Hit classification:** L1603 — OPERATIVE (instructs the planner to verify inherited fixes against root cause). L2236 — MENTIONED (History row recording the codification). L800 — MENTIONED (describes a failure class in a different context). Operative hit count: 1.

### 134 — Live-canary every daemon-write activation; green tests are not enough

**Derivation row:** R3 (RULE → artifact contains rule → no mechanism → CODIFIED).

**Deciding sentence:** "for any silent/best-effort daemon write path, a post-activation live canary is mandatory, not optional."

**Reasoning:** Short entry documenting that canaries caught three bugs green tests missed. The discipline rule is explicit: a future actor deploying a daemon-write path who skips the live canary has violated the stated mandate. The rule is in PLANNER_TEMPLATE.md as Workaround #15 (L1858).

**Mechanism:** none automated. The rule is governance prose. No gate checks for live canary execution.

**Probe:** `grep -niF 'post-activation' PLANNER_TEMPLATE.md` → 4 hits: L1575 (OPERATIVE, names this as the general form), L1858 (OPERATIVE, Workaround #15 heading), L1860 (OPERATIVE, the rule body), L2149 (MENTIONED, History row). `grep -niF 'live canary' PLANNER_TEMPLATE.md` → 4 hits at the same locations. Positive control: `scope_check` → 18 hits.

**Hit classification:** L1858/1860 — OPERATIVE (the workaround rule, instructing the reader). L1575 — OPERATIVE (the general verification principle referencing this rule). L2149 — MENTIONED (History row). Operative hit count: 3.

### 328 — A transcribed census row transposed two column values and stayed well-formed — spot-check rows against their cited sources

**Derivation row:** R3 (RULE → artifact contains rule → no mechanism → CODIFIED).

**Deciding sentence:** "any hand-transcribed table that PAIRS values per row gets a spot-check that diffs a sample of rows against their cited sources before it is consumed."

**Reasoning:** Mixed entry documenting a specific transposition defect, then stating a "How to apply" rule. A future actor consuming a hand-transcribed table who skips the spot-check has violated this rule. The rule is in PLANNER_TEMPLATE.md as Rule 96 (L1355).

**Mechanism:** none automated. No gate checks whether spot-checks were performed.

**Probe:** `grep -nF 'spot-check' PLANNER_TEMPLATE.md` → 5 hits. L541 (MENTIONED, Rule 14 says "not spot-check" for scope coverage — different axis). L1325 (OPERATIVE in a different context, describes when to accept self-checked results). L1355 (OPERATIVE, Rule 96 — the transcription spot-check rule). L1367 (MENTIONED, "session state spot-check" — different use of the term). L2132 (MENTIONED, History row). Positive control: `scope_check` → 18 hits.

**Hit classification:** L1355 — OPERATIVE (the rule instructing the reader). L1325 — OPERATIVE in an adjacent context. L541 — MENTIONED (contrasting use). L1367 — MENTIONED (different meaning). L2132 — MENTIONED (History row). Operative hit count for THIS rule: 1.

### 330 — Register DUP-APPEND — one bullet in, two identical rows out

**Derivation row:** R3 (RULE → artifact contains rule → mechanism fails Rule One + uninvoked → CODIFIED).

**Deciding sentence:** "run the v0.3 lint per culmination; treat any duplicate-row WARN as a record defect to strike, not tidy."

**Reasoning:** Mixed entry documenting the DUP-APPEND defect class and its mechanization in walk_register_lint v0.3's `duplicate_row` guard. The rule has two clauses: (1) run the lint per culmination, (2) when building a new guard, run it over the real corpus before trusting output. The guard exists and works (demonstrated above) but is NOT automatically invoked.

**Mechanism:** `duplicate_row` guard in `walk_register_lint.py` (`_structural_guards`, line 292-299).
- Invocation: UNINVOKED — no automatic path reaches this guard (fold_check.readers_for selects walk_register_lint only for walk-register-* files; depositor calls run_check not emit_manifest).
- Rule One: Y — the second clause ("run it over the real corpus BEFORE trusting its output") is process discipline the guard cannot enforce. Material scope uncovered.
- Rule Two: N — the guard REJECTS violations (duplicate rows); it is not the lesson's subject.
- Verdict component: fails Rule One + uninvoked → no passing pair

**Probe:** guard `duplicate_row` exists at walk_register_lint.py:292-299. Fixture test: `walk-register-dup.md` → stderr `UNCONFORMANT`, stdout WARN `duplicate_row`, exit 0. Clean control: `walk-register-clean.md` → stderr `CONFORMANT`, exit 0.

**Hit classification:** walk_register_lint.py:292-299 — OPERATIVE (the guard code). walk_register_lint.py:264 — OPERATIVE (docstring naming the guard).

### 331 — Headerless table rows are INVISIBLE to a header-anchored parser

**Derivation row:** R3 (RULE → artifact contains rule → mechanism fails Rule One + uninvoked → CODIFIED).

**Deciding sentence:** "when a tool's recognition rule can EXCLUDE malformed instances of the thing it validates, add a guard for the excluded shape — ask 'what does my parser silently skip?' and measure it over the real corpus."

**Reasoning:** Mixed entry documenting the headerless row problem, its measurement (46 rows), and its mechanization. The rule states a general principle applicable to ALL tools, not just walk_register_lint. The guard covers one specific case (walk register headerless rows), not the general principle.

**Mechanism:** `headerless_rows` guard in `walk_register_lint.py` (`_structural_guards`, line 300-306).
- Invocation: UNINVOKED — same analysis as entry 330.
- Rule One: Y — the guard catches headerless pipe rows in walk registers. The lesson's general principle ("add a guard for the excluded shape" for ALL tools) is broader than what one guard covers. Material scope uncovered.
- Rule Two: N — the guard REJECTS violations (headerless rows); it is not the lesson's subject.
- Verdict component: fails Rule One + uninvoked → no passing pair

**Probe:** guard `headerless_rows` exists at walk_register_lint.py:300-306. Fixture test: `walk-register-headerless.md` → stderr `UNCONFORMANT`, stdout WARN `headerless_rows`, exit 0. Clean control: same as 330.

**Hit classification:** walk_register_lint.py:300-306 — OPERATIVE (the guard code). walk_register_lint.py:264 — OPERATIVE (docstring).

### 333 — Every sqlite sentinel prints BEFORE the COMMIT — a rollback run produces perfect evidence with nothing written

**Derivation row:** R4 (RULE → no artifact contains it yet → PENDING).

**Deciding sentence:** "every transactional write step ends with a separate fresh-invocation read-back whose expected values are asserted, and the step's record states that the in-transaction sentinels prove intent, not durability."

**Reasoning:** Mixed entry documenting the proof that in-transaction sentinels don't prove durability. The rule is explicit and enforceable: a future author who writes a transactional step without a post-commit read-back has violated the mandate. The rule is NOT yet in PLANNER_TEMPLATE.md — probes for `read-back`, `transactional write`, `rollback`, `fresh connection`, `sentinel` all returned 0 hits. Positive control: `scope_check` → 18 hits, `post-commit` → 1 hit (about git commits, not sqlite transactions). The adjacent `durability` hit (L1101) is about file-artifact resume paths, not sqlite transaction read-backs. Build item: PLANNER_TEMPLATE.md.

**Mechanism:** none. No gate checks for post-commit read-backs.
**Probe, result, control:** see above — 0 operative hits for the specific rule.
**Hit classification:** n/a (no hits to classify).

---

## Q6 — What must change so `bare` cannot recur?

### (a) `detect_learned.py:245` emits `learned` unconditionally

`detect_learned.py:245` produces `proposed_status: "learned"` for any entry passing the detector's ratio/phrase thresholds. It has no codepath to emit `history`. Under the CEO's ruling, `history` is a fourth legal value — for entries that RECORD what happened rather than stating an enforceable rule. The detector's binary (learned/unknown) cannot express this.

**Size:** code change in `detect_learned.py` to add a `history` route. The classifier or a separate discriminator would need to distinguish RECORD from RULE entries. **Cost:** medium — requires either a heuristic (presence of "How to apply" / "discipline rule" sections) or an LLM-based classifier, since the RECORD/RULE distinction is a judgement call this plan made manually.

**Adjacent verification:** `_STATUS_TARGET_MARKER_RE` (`src/lessons_forge.py:52`) keys on the marker NAME and consumes any value. Verified by executing: `_key_heading` maps `[status: history]`, `[status: unknown]`, `[status: pending]`, and bare headings to identical keys. A new status VALUE round-trips through ingest safely.

### (b) No legal `[status:]` value set is defined anywhere

The four values (`learned`, `codified`, `pending`, `history`) are not DEFINED in any governing artifact. `LESSONS.md` carries 225 `codified` labels and zero statements of what `codified` means. The phrase "written into its target, unenforced" appears in full in `shop_next_session.md` only — not in PLANNER_TEMPLATE.md, DRAFTING_CYCLE.md, COMPANY.md, ARCHITECTURE.md, or lessons-forge/CLAUDE.md. Positive control: `grep -nF 'written into its target' shop_next_session.md` → 1 hit (L29). A register annotated with a vocabulary that lives only in a session baton decays the moment the baton rolls.

**Size:** governance definition in a durable artifact (PLANNER_TEMPLATE.md or a new `glossary.md` — the build item is itself one of this plan's open forks). **Cost:** small for the definition, medium for the enforcing validator.

### (c) Nothing tells a wrap appender to add `[status: pending]`

SESSION 59's three appends carried `[status: pending]` by hand. No rule, template, or reminder instructs a wrap appender to include a status marker. Every append without one creates a new bare heading invisible to the build queue.

**Size:** a rule in PLANNER_TEMPLATE.md's session-wrap section. **Cost:** small — one sentence.

### (d) Detector scores a prose-term ratio against CODE targets

The detector scores a prose-term ratio against the target artifact's text. When the target is CODE (`walk_register_lint.py` for entries 330/331), the ratio is mechanically meaningful (0.40 and 0.29 respectively, vs 0.00 on all no_target rows), but the `phrase_hits >= 2` half is structurally dead against code — code does not contain prose phrases from lesson headings. Entry 330 missed the `learned` bar at exactly `ratio > 0.4` (0.40), a boundary condition. The real defect: the thresholds and stop list are tuned for prose, and the phrase-hit guard is dead against code.

**Size:** code change in `detect_learned.py` to either (a) route CODE targets to a different scoring path or (b) exempt them from the ratio threshold. **Cost:** small.

### (e) The pipeline already had a value for these entries and the executable declined to write it

The 501 mapping proposed `unknown` for all Q rows and `executable-502` quarantined them as BARE instead. Fork 3 (SESSION 58b) decided "undecidable ⇒ `unknown`, surfaced, never auto-routed" about the 20 `reference` entries. Whether that generalizes to the mapping's `unknown` rows was never settled — 502 left them bare pending a CEO ruling rather than in defiance of one.

Fork 3's scope: the 20 `reference` entries — a distinct population from the 14 bare entries. None of the Q entries carries `reference` status. Fork 3 established the `unknown` status as a legal value and as the correct disposition for genuinely undecidable entries. Whether writing `proposed_status=unknown` should be the DEFAULT for the pipeline (rather than quarantining) is the question that was never answered.

This plan ADOPTS the convention for its own Q entries — the derivation table routes UNDECIDED to `unknown` — but that is a single applied instance, not a policy argument for the general default. What would be lost by writing `unknown` by default: the CEO's opportunity to rule on the entries before they are labelled. What would be gained: bare headings cannot recur, since every entry gets a status value even when the pipeline cannot grade it.

### (f) 504's two rules never ask whether a mechanism is INVOKED

A warn-only guard that nothing calls can read as enforcement under 504's rules. Entries 330 and 331 both carry guards that pass Rule Two (not circular) and whose only failure is invocation — without the invocation check, they would read as `learned`. This is a gap in the inherited rule set, not in this plan's targets. The fix is doctrine: add "is the mechanism invoked by anything?" as an upstream question before Rule Two's reject condition.

**Size:** doctrine — an addition to the promotion rules. **Cost:** small — one sentence, but it changes the evaluation of any entry whose mechanism is a standalone script.

### Which single gap would have prevented the largest share of this plan's work?

**(e)** — writing the proposed `unknown` value instead of quarantining would have prevented the entire bare-entry class. The 14 entries would carry `[status: unknown]` and be visible to the build queue. The CEO's `history` ruling and this plan's 14-entry grading work exist solely because 502 declined to write a value it already had. Every other gap (a-d, f) is about IMPROVING the grading; gap (e) is about whether the DEFAULT should leave entries bare at all. Closing (e) prevents the recurrence; closing (a-d) improves the quality of the grading that would have occurred instead.

---

## What could not be measured

1. Whether the companion executable correctly applies these verdicts — that is the executable's post-condition, not this plan's.
2. Whether entry 333's rule SHOULD go in PLANNER_TEMPLATE.md specifically or in a different artifact — the Fork-2 discriminator routes it there, but the rule is about sqlite transaction verification, which is narrow enough to warrant consideration as a CODE guard instead.
3. Whether the three legacy `Path(__file__).parent.resolve()` sites (bellows.py:26, planner.py:11, verdict.py:13) cause active failures today — the worktree-root-confusion class is the documented failure mode, but whether these specific sites are reached from worktree execution was not tested.

## Open forks

1. The companion executable is BLOCKED on this plan's output.
2. `detect_learned.py:245` emits `learned` unconditionally and cannot emit `history`.
3. No validator defines the legal `[status:]` value set, and the four values are not DEFINED in any governing artifact — the phrase appears in full in one session baton only.
4. Nothing tells a wrap appender to add `[status: pending]`.
5. 504's two rules never ask whether a mechanism is INVOKED — doctrine gap.
6. `glossary.md`, the Fork-2 DEFINITION target, exists in no repo.
7. `shop_next_session.md:91` already carries a corpus bucket labelled `history` sized 15 — what those 15 ARE is undetermined; a name collision would put 15 entries in a bucket nobody ruled on. This plan grades 5 as `history`.

## Recommended executables

1. **Apply the bare-entry rulings:** write `[status:]` and `[target:]` markers to LESSONS.md for the 14 entries per this plan's TSV. Blocked on: this plan's deposit.
2. **Codify the `[status:]` vocabulary:** define `learned`, `codified`, `pending`, `history`, and `unknown` in a durable artifact. Blocked on: gap (b).
3. **Add invocation check to promotion rules:** add "is the mechanism invoked by anything?" as an upstream question in the promotion evaluation. Blocked on: gap (f).
4. **Add `[status: pending]` to wrap template:** add the status marker instruction to the session-wrap section of PLANNER_TEMPLATE.md. Blocked on: gap (c).

---

## Contract compliance

**C1 — Read-only:** no edit to LESSONS.md, no write to any .db, no re-label. ✓

**C2 — Corpus reads via immutable URI:** every sqlite3 invocation used `file:/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db?immutable=1`. Satisfied by the stricter `immutable=1` form (differs from the contract's `mode=ro`; the plan governs here — `mode=ro` on this WAL corpus fails against a sidecar-less copy and touches the live `-shm` mtime). `lesson_entries` = 370 = D10 asserted before trusting reads. ✓

**C3 — No import of bellows modules:** walk_register_lint.py imports `re`, `sys`, `pathlib` only — stdlib only, no bellows module, no DB connection. Run as subprocess. ✓

**C4 — Wrote only declared deposits plus fixtures:** deposits: `knowledge/research/bare-entry-ruling-2026-08-23.md`, `knowledge/research/bare-entry-ruling-2026-08-23.tsv`. Fixtures: `scratch-506/walk-register-clean.md`, `scratch-506/walk-register-dup.md`, `scratch-506/walk-register-headerless.md`. Nothing else written. ✓

**C5-C6:** n/a for this dispatch.

**C7 — Git status before/after (4 repos + worktree):**

Before:
- ROOT: `2bade79...`, ` M lessons-forge`
- lessons-forge: `2c6db74...`, ` D knowledge/decisions/diagnostic-bare-entry-ruling.md`, `?? knowledge/decisions/in-progress-diagnostic-506.md`
- bellows: `44529b0...`, clean
- forge: `f0939a6...`, clean
- worktree: `?? scratch-506/`

Note: the main-tree pairs cannot see worktree work (`.bellows-worktrees/` is in `.gitignore`). The worktree snapshot shows only `?? scratch-506/`, which is declared under `extra_permitted`.

After: reported at commit time.

**C8:** closing sequence completed at commit.
