# Agent Prompt Feedback

None.

None.

NONE.

None.

None.

None.

None.

None.

#### Forward Register

None.

#### Forward Register
NONE
Now committing deposits with cd-first and toplevel print per Rule 85.
Step 2 (QA) complete. Commit `e5e6132`, all 5 QA files deposited.

#### Forward Register
NONE

No prompt feedback.

- Row 9b: `get_unclassified_entries` requires a `sqlite3.Connection` object, not a path string. The plan's instruction "run `get_unclassified_entries` (read-only)" could benefit from naming the expected calling convention to avoid a wasted invocation.

- The `-readonly` flag on `sqlite3` failed to open the backup DB file (`exit=14`, `unable to open database file`); the read succeeded without `-readonly`. The backup is a standalone file without WAL companions, which may be the cause. The plan's `-readonly` directive is on the canonical DB path (which worked), not the backup.

No prompt-feedback observations from this step.

No prompt-feedback observations from this step.

Now running the Rule 20 self-check.
Rule 20 passed. Now updating the QA report with the actual self-check output.
```
============================================================
Rule 20 — QA Self-Check Results
============================================================
PASSED — SELF-CHECK PASSED — all evidence files present, no hedging keywords found.
Evidence folder: /Users/marklehn/Developer/GitHub/lessons-forge/.bellows-worktrees/343/knowledge/qa/evidence/dc-direction-verdict-2026-08-11/
Files verified: 3
```
Now committing the deposits — pathspec on the commit, then asserting `git show --name-only`.
Commit `7de527c` contains exactly the four deposit files. No push.

Now committing the dev log in the worktree.
Step 1 complete. Both commits landed cleanly:

None.

Step 5 QA executed cleanly on first dispatch. All 11 rows (0-10) pass. The 42-row Gate-2 queue survived intact (id-for-id, symmetric difference empty). Classification depth measurements show no inter-tranche cliff and all 41 proposals pass both bounds. One near-ceiling ratio at proposal 309 (0.748) is an isolated value, not a clustering pattern.

Step 2 QA executed cleanly. All 8 verification rows pass. The id-for-id comparison at row 7 is the headline check this split exists to protect, and it confirms the 42 accepted|codify proposals survived the ingest without a single stale flip. The plan-204 sentinel held, doctrine is unchanged, and the schema matches src/db.py with only the expected cosmetic RENAME artifact.

Step 1 executed cleanly on first dispatch. The 42-row Gate-2 queue (accepted|codify) survived intact through the ingest, verified by G1's composition check (pre-ingest) and by G4's post-ingest stale-count hold. The `would_update=0` guard at Step 1a-bis provided the load-bearing assurance before mutation. The batch fingerprint matched exactly, confirming the 41 entries are the ones scouted at authoring. No classification was performed — `get_unclassified_entries()` returning 41 is the correct closing state for Plan B.

(none)

- The `-readonly` flag on `sqlite3` fails with SQLITE_CANTOPEN (error 14) when opening a `.backup`-produced copy of a WAL-mode database, because `-readonly` cannot create the required shared-memory file. The backup restorability assert succeeded using a read-only SELECT without the flag. Future plans that assert against WAL-mode backup copies should note this mechanism limit.

No prompt feedback.

No prompt feedback.

None.
Exactly the five intended paths committed. Step 6 is complete. Here are the Ledger Updates:

None.

None.
Now committing both deposit files.
Step 3 complete. Tranche B classified — 17 entries (232–248) → 17 proposals (240–256), all `governance_rule`, all `proposed`, all `route=NULL`. All reasoning-depth measurements pass (match 59–188, ratio 0.102–0.303). 17 remaining unclassified entries [249–265] for Step 4.

None.

None.

No prompt feedback for this step.

- The plan was clear and executable. All verification rows passed on the first measurement. Receipt item 0b correctly declared a fresh run (k=0), and all before-items were present, enabling normal adjudication on every row.

The plan was clear and executable as written. The A00 single-match guard, A0-pre per-row checks, and the total_changes delta assertions all worked as documented. The C8 command discipline (`;` never `&&`) was followed throughout.

None — plan instructions were clear and execution was unambiguous.

None — plan instructions were clear and the execution sequence was unambiguous.

**Agent:** QA (Step 3, Plan 291)
**Plan:** 291 — Gate 2 Plan A: codify proposals 201–206

**Agent:** DEV (Step 2, Plan 291)
**Plan:** 291 — Gate 2 Plan A: codify proposals 201–206

**Agent:** SA (Step 1, Plan 291)
**Plan:** 291 — Gate 2 Plan A: codify proposals 201–206

None.

None.

None — all plan instructions were followed without ambiguity or contradiction requiring deviation.

None — all plan instructions were followed without ambiguity or contradiction requiring deviation.

- **(QA, plan 287, Step 3):** The `grep -F` discipline for literal bold-marker anchors is essential on the ugrep shim — without `-F`, patterns starting with `**` silently error and produce empty stdout that reads as "not found" having verified nothing. Confirmed during must-survive clause verification.

- **(DEV, plan 287, Step 2):** The `grep -F` discipline for literal-string anchors on a ugrep shim is load-bearing — every bold-marker anchor (`**Version:**`, `**Landing posture…**`) errors silently without `-F`, producing an empty stdout that reads as "not found → PASS" having verified nothing. This was tested and confirmed during execution.

- **(SA, plan 287, Step 1):** The diagnostic map's line-number-to-text associations should be verified at the point of use rather than trusted — the map associated `:82` with "Sketch one real block." when line 82 in the live file is actually the Sequential-fold rule. Line numbers drift between authoring and execution; quoted unique strings do not.

- The plan's rewritten halt conditions (10 proposals not 2, 2 route lines not 0) correctly matched the measured state. The live re-read of NT ids before computing the expectation was straightforward since Gate 2 had not shipped.
- The route-line attribution via DB join was necessary since the report prints neither proposal id nor entry_id — the heading correlation worked cleanly.

- The plan's detailed Step 1a-bis parent-hash guard and detect_duplicates pre-check were valuable for confirming ingest safety before mutation.
- The three-probe dispatch-state determination (HEAD, working tree, preserved branches) cleanly resolved to FRESH.
- The scout disposition agreement across all 8 entries reflects thorough pre-authoring analysis by the Planner.

No feedback items.

No feedback items.

- The plan's detailed gate structure (G1–G6) with explicit fresh/resume disambiguation was effective — each gate had a clear measured value and pass/fail criterion.
- The split-target guidance with explicit licence-to-disagree (VA1) was well-calibrated: both entries' raw_content independently supported the scout's placement, so no divergence to record, but the explicit invitation to verify independently prevented blind anchoring.
- The backup verification requirement (DA1/CA1) with integrity_check + count-match was straightforward to execute and provides a genuine restore-point guarantee.

- The plan's instruction to cross-check E4's doc text against the shipped `plan_lint.py` code (Row 5) was load-bearing — it verifies the doc describes the ACTUAL mechanism, not the superseded edit-map design.
- The E5 three-case structure (standalone / folded / SA-omitted) made QA row 6 mechanical: identify which case the SA chose, then verify accordingly.
- The "own working tree" instruction for Row 11 (`git status --porcelain -- src/`) correctly avoids the vacuous `-C <main>` trap on a worktree run.
- The evidence-file structure (db-invariants.txt for rows 9–10, doc-integrity.txt for rows 0/0b/1–8) cleanly maps the Rule 20 block's required_evidence_files to the verification rows.

- The blueprint's edit-application order (M1 first, E5 before E4 since both are in §4) avoided line-number drift between edits — each anchor was still unique when its turn came.
- The surgical date-swap approach for M1 (scoping the Edit anchor to the version+date substring, not the whole line) worked cleanly — the trailing clause survived without needing to be reproduced.
- The C0 precondition check immediately before the write, separate from Step 1's SA confirmation, is well-placed — it catches a concurrent status change between SA and DEV.
- The `.backup` method for the restore point is the right choice over `cp` for a WAL-mode DB.

The Step 2 verification matrix was well-structured with clear pass/fail criteria and DB-source requirements. The vacuous-pass warning on Check 7 (PLANNER_TEMPLATE.md via root repo git, not worktree) correctly prevented a false pass — running `git -C` against the root repo is the right approach. The before-snapshot reconciliation in Check 4 (requiring cross-reference to Step 1's A0 deposit) ensures resume-invariant verification rather than assuming fresh-run deltas.

The plan's Task A00 backup command, Task A0 precondition checks, and single-transaction discipline for Task A + Task A2 were well-structured and executed cleanly. The explicit quiescence check (two reads a moment apart) and the parameterised WHERE clause requirement for Task A2 are good safety guards. The backup-to-main-tree instruction correctly prevents worktree teardown data loss.

No new prompt feedback. The QA step executed all nine checks cleanly; the evidence-source rule and vacuous-pass guards (Checks 6 and 7) correctly directed queries to the canonical DB and root repo respectively.

No new prompt feedback to record from this step. The plan's Task A00/A0/A/A2/B/C structure executed cleanly; the single-commit discipline for Task A + A2 was well-motivated and straightforward to implement.

No new prompt feedback to record from this step.

No new prompt feedback to record from this step.

No new prompt feedback to record from this step.

**2026-07-21 — Gate 2 Codification 2026-07-20 (DEV Step 2)**

**2026-07-21 — Gate 2 Codification 2026-07-20 (SA Step 1)**

**2026-07-20 — Lessons Forge Cycle 2026-07-20 (QA Step 3)**

**2026-07-20 — Lessons Forge Cycle 2026-07-20 (DEV Step 2)**

**2026-07-18 — Gate 2 codification QA (QA Step 3)**

| Feedback | Source |
|---|---|
| The blueprint's exact-anchor-line specification (line numbers + surrounding text) made faithful application a single-pass operation — zero ambiguity on insertion points, no scanning required. | Plan 228, Step 2 |
| Specifying the expected before/after distribution delta ("proposed 6→0, implemented 99→105") with a halt-on-mismatch clause made verification mechanical and caught-nothing a high-confidence signal rather than an absence of checking. | Plan 228, Step 2 |

| Feedback | Source |
|---|---|
| The plan's CEO Context section embedding the tiered trigger criteria (floor / escalate / full-cycle) with explicit rationale made blueprinting the Drafting Cycle section straightforward — the exact governance shape was decided at plan authoring, not left for SA to infer. | Plan 228, Step 1 |
| Specifying "highest Rule = 52, highest Checklist = 28" in CEO Context eliminated a potential anchoring error — without it SA would have had to scan and count, risking off-by-one on item numbering. | Plan 228, Step 1 |

No issues. All verification rows passed on the first run. The R2 recovery left main in a clean state consistent with the canonical DB.

| File | Agent | Feedback |
|---|---|---|
| executable-208.md | Lessons Forge QA | The plan's QA step is well-structured: 9 verification claims with explicit queries and expected values make the checks mechanical. The Rule 52 self-discipline requirement ("this is the Gate that codified it — do not be its first violation") is a strong forcing function for the QA agent to grep-before-asserting. The evidence-source rule (canonical DB path + read-only mode) prevents accidental writes during QA. |

| File | Agent | Feedback |
|---|---|---|
| executable-208.md | Forge Developer | The plan correctly anticipated the table name discrepancy — the schema uses `lesson_proposals` while the plan text refers to `proposals`. The plan's instruction to verify the API before writing SQL prevented a silent failure. The blast-radius verification pattern (before/after distribution + recency query) is thorough and mechanical. |

| File | Agent | Feedback |
|---|---|---|
| PLANNER_TEMPLATE.md | Forge Developer | The plan's pre-edit verification section is exemplary — having 4 explicit claim/query/expected triples made the verify-before-edit discipline trivially mechanical. The plan also dogfoods its own Rule 52 by requiring re-verification of all Planner-claimed line numbers. |

No prompt feedback this step.

- Plan Step 2 check 3 states "SELECT COUNT(*) FROM lesson_proposals WHERE route IS NOT NULL returns 3" — actual count is 18 (15 from 2026-07-06 cycle + 3 new). The Step 1 dev log already flagged this same discrepancy. The plan's phrasing should have said "delta is exactly +3" rather than "returns 3." Consistent with the Step 1 prompt feedback about the route-count expectation.
- The expected status distribution in the plan is correct and matches the actual DB state.

None — execution followed plan precisely.

The plan specified `status_updated_by='ceo-plan-203-recovery'` for the proposal 145 restore, but the `lesson_proposals` table has a CHECK constraint restricting `status_updated_by` to `('planner', 'ceo', 'auto', NULL)`. Used `'ceo'` instead — the semantically closest valid value for CEO-directed recovery. The plan's `stale_proposals_marked` key was expected in `run_full_lessons_cycle`'s return dict but isn't surfaced there (it's only in `ingest_lesson_entries`'s return); however, `updated_count == 0` proves no stale path fired.

None — execution followed plan precisely.

- The plan's verification item 1 ("by reading the code AND confirming test #4 exists and passes") is well-structured — requiring both static analysis and dynamic verification prevents false confidence from either alone.
- The dev-log's Task D validation section (entries 123/127) is clear and actionable for QA cross-reference. Reporting overlapping proposal IDs and match mechanisms provides verifiable evidence without requiring QA to re-run the live-DB query.

- The plan's instruction to strip backticks from tags was not explicit but was necessary — live DB stores tags with backtick delimiters (`` `planner-discipline` ``). Tokenizers processing raw tag fields should account for formatting characters.
- `date('now', '-N days')` in SQLite works correctly against ISO 8601 timestamps with timezone offsets for lexicographic comparison, but this should be tested explicitly if timestamp formats ever change.

No new prompt feedback generated during this step.

No new prompt feedback generated during this step.

**2026-07-07 — Gate 2 Codification 2026-07-06 (QA Step 3)**

**2026-07-07 — Gate 2 Codification 2026-07-06 (DEV Step 2)**

**2026-07-07 — Gate 2 Codification 2026-07-06 (SA Step 1)**

No prompt feedback to report. The evidence-source rule (read-only URI to canonical DB from any working directory) and Rule 20 self-check requirements were clear and followed without issue.

No prompt feedback to report. The plan's evidence-source rule (absolute path to canonical DB) and module API constraint were clear and followed without issue.

Plan Step 4 instructions were clear and comprehensive. The evidence-source contract (canonical DB absolute path, per-row DB-source column) worked as intended — all queries ran against the canonical DB without ambiguity. The Rule 20 self-check gate requirement (byte-exact banner + self-grep confirmation) is explicit enough to be mechanical.

No prompt feedback to report this step. The plan instructions were clear — work list derivation via Rule #47, cross-check against Step 1 JSON, per-entry classification with `route=None`, and cluster synthesis all proceeded as documented. The specialist file taxonomy guidance and decision tree were sufficient for all 15 entries without ambiguity.

No prompt feedback to report this step. The plan instructions were clear and unambiguous; the migration path, cycle execution, and work-list derivation all proceeded as documented.

Plan 130 instructions were precise and corrective. The evidence-source rule requiring each PRAGMA row to state which DB it ran against is an effective safeguard against the disclosure gap in the original report.

No prompt feedback to report this step. Plan instructions were precise and verification proceeded without ambiguity.

No prompt feedback to report this step. Execution was straightforward — plan instructions were clear and matched actual code shape.

No prompt feedback this session.

No prompt feedback this session.

None — plan instructions were precise and unambiguous; exact old/new strings matched on first attempt.

