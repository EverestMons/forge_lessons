# Lessons Report — 2026-05-18


## Summary


| Category | Count |
|---|---|
| governance_rule | 17 |
| instrumentation | 6 |
| structural | 2 |

**Total proposals:** 25


## Governance Rule


### 2026-05-17 — Defensive diagnostic before destructive cross-repo work pays off in surprising ways


- **Suggested action:** Add rule to PLANNER_TEMPLATE: before any executable that does destructive cross-cutting work, author a pre-cutover unknowns diagnostic distinct from any surface diagnostic. Questions must target specific values, line numbers, exact text, and runtime states.
- **Reasoning:** Entry explicitly proposes a new Planner heuristic: 'Before any executable that does destructive cross-cutting work, author a pre-cutover unknowns diagnostic distinct from any earlier surface diagnostic.' Grounded in evidence: the unknowns diagnostic 'surfaced two things the surface diagnostic missed: (1) stale /Desktop/GitHub/ default paths and (2) GitHub remote did not exist yet.' The fix is a documentary planning rule, not a code change.
- **Confidence:** high

### 2026-05-16 — Splitting destructive cross-cutting work into stand-up + cutover phases behind a verdict gate


- **Suggested action:** Add plan-authoring guidance to PLANNER_TEMPLATE: when multi-step plans include destructive or cross-cutting steps, split at the natural verification point (new system stands alone before old system is modified). Use verdict gate between phases.
- **Reasoning:** Entry proposes a plan-shape heuristic: 'identify whether any step is destructive to a working system the user depends on or cross-cutting across multiple repos/governance docs. If yes, look for the natural verification point and split at that point.' Grounded in evidence: Phase A/B split produced three benefits — real verification gate, bounded half-state, reduced recovery surface. The fix is a documentary rule for plan authoring.
- **Confidence:** high

### 2026-05-15 — Claude has two filesystems and the wrong tool silently writes to the wrong one


- **Suggested action:** Add tool-discipline rule to specialist files or PLANNER_TEMPLATE: for every file write to /Users/marklehn/ paths, use Filesystem:write_file (MCP), never create_file (sandbox). create_file to a /Users/ path is always a bug.
- **Reasoning:** Entry documents a silent failure mode: 'create_file had written to Claude\'s container filesystem at the same nominal path; the user\'s Mac filesystem received nothing.' Proposes clear rule: 'For every file write into a /Users/marklehn/Developer/GitHub/ path, use Filesystem:write_file, never create_file.' The fix is a documentary rule change distinguishing sandbox vs Mac filesystem tools.
- **Confidence:** high

### 2026-05-15 — Bellows lifecycle commits in a submodule need a governance-root pointer bump in the same session


- **Suggested action:** Add session-wrap rule to PLANNER_TEMPLATE: after any commit-push inside a submodule, run git status at governance root and bump the submodule pointer. Verify with git submodule status (clean prefix) at session close.
- **Reasoning:** Entry proposes a mandatory two-commit pattern: 'After any commit-push inside a submodule, the next mandatory action is cd ~/Developer/GitHub && git status to check for a dirty submodule pointer. If present: git add <submodule-dir> && git commit.' The fix is a documentary rule for session-wrap procedure, grounded in evidence: 'git status in the governance root showed M bellows — the submodule pointer in the parent recorded an older commit.'
- **Confidence:** high

### 2026-05-15 — Canary "captured cwd" flag is a cheap, decisive answer to "does feature X work in arrangement Y"


- **Suggested action:** Add canary plan authoring guidance to PLANNER_TEMPLATE: when designing canary plans, identify binary 'does X work' questions the canary naturally touches and add Flags-for-CEO instructions to report the relevant runtime fact as a literal value.
- **Reasoning:** Entry proposes a plan-authoring technique: 'When designing a canary plan, identify any binary does-X-work question the canary\'s execution naturally touches, and add an explicit Flags-for-CEO instruction to report the relevant runtime fact.' Grounded in evidence: adding 'report cwd' to canary answered both relocation-fix verification and worktree question 'in one cycle instead of two or three.' Medium confidence because this is a recommended technique rather than a hard rule — but the entry frames it as a directive.
- **Confidence:** medium

### 2026-05-14 — Recovery plan had a gap (empty index after bare-to-non-bare conversion); agent improvised through it instead of halting


- **Suggested action:** Add to PLANNER_TEMPLATE: (1) when authoring plans with git-internal operations, walk the intermediate state mentally and address it explicitly; (2) reinforce that 'safe and non-destructive' is not an agent judgment call — even side-effect-free operations not in the plan require verdict.
- **Reasoning:** Entry proposes two governance changes. First: 'the Planner walks the resulting state mentally before deposit — what does git status show? what does the index look like?' Second, explicitly: 'Reinforce in PLANNER_TEMPLATE that safe and non-destructive is not an agent judgment call within an executable plan... This is a candidate for a new Rule or amendment to the existing improvisation prohibition.' The agent had run 'git reset HEAD' without authorization despite the plan not including it.
- **Confidence:** high

### 2026-05-13 (session 3) — Phase 1.5 skipped at session start; cost was four diagnostics on a foundation already answered


- **Suggested action:** Strengthen Phase 1.5 enforcement in PLANNER_TEMPLATE: Phase 1.5 read happens FIRST in any session that opens with project work, regardless of task size. 'This is just cleanup, I don\'t need full context' is the failure mode to guard against.
- **Reasoning:** Entry proposes strengthening an existing rule: 'Phase 1.5 read happens FIRST in any session that opens with project work, regardless of task size or how narrow the opening question seems.' Grounded in evidence: 'The Planner went straight to investigation and authored four sequential diagnostics... before discovering PLANNER_TEMPLATE was at v4.41 (memory said v4.26).' The fix is a documentary rule reinforcement.
- **Confidence:** high

### 2026-05-13 (session 3) — Verdict directory error recurred for the third time in 24 hours; reading is not internalizing


- **Suggested action:** Add rule to PLANNER_TEMPLATE: the Planner runs the three-item verdict-file mechanical check out loud (visible in response text) before any file write that Bellows will read. Visible execution, not silent execution.
- **Reasoning:** Entry proposes a behavioral rule: 'The Planner runs the check out loud (as visible text in the response) before any file write that Bellows will read — verdict responses, plan deposits with Deposits blocks.' Grounded in evidence of triple recurrence: 'Across three rounds... the Planner wrote verdict response files to verdicts/pending/ instead of verdicts/resolved/. Each round the Planner performed manual file moves to fix the symptom.'
- **Confidence:** high

### 2026-05-13 (session 3) — Bellows step-pause behavior model was wrong; per-step pause is manual-bootstrap, not Bellows


- **Suggested action:** Amend PLANNER_TEMPLATE to distinguish manual-bootstrap vs Bellows-dispatch execution modes. Document that STOP/wait instructions in step prose are ignored by Bellows. auto_close:false controls only the final pause, not per-step pauses.
- **Reasoning:** Entry explicitly proposes PLANNER_TEMPLATE amendments: 'Two clarifications needed in PLANNER_TEMPLATE governance: (1) Distinguish the two execution modes explicitly. Manual Claude Code bootstrap pauses after every step by the agent\'s own discipline. Bellows dispatch pauses only at gate-triggered events. (2) The STOP, wait for confirmation instructions inside step prompts are ignored by Bellows.' Grounded in evidence: 'The daemon dispatched all four steps end-to-end without pausing between them.'
- **Confidence:** high

### 2026-05-13 (session 3) — Negative grep results during dormancy ≠ architectural finding


- **Suggested action:** Add diagnostic methodology rule to PLANNER_TEMPLATE: when concluding 'X doesn\'t surface in Y' based on grep of historical artifacts, verify that X\'s preconditions were met during the observation window. Negative grep results during dormancy are not architectural evidence.
- **Reasoning:** Entry proposes a diagnostic methodology rule: 'When a diagnostic concludes X doesn\'t surface in Y based on grep of historical artifacts, the diagnostic must establish that X was supposed to surface during the observation window.' Grounded in evidence: 'The diagnostic grepped reports from a period when drift count was 0... The grep found that absence and treated it as evidence that drift content never reaches reports.' The broader lesson: 'Negative results are weak evidence unless paired with proof the feature should have fired.'
- **Confidence:** high

### 2026-05-13 (later) — `**Deposits:**` blocks must contain resolvable paths, never placeholders


- **Suggested action:** Add rule to PLANNER_TEMPLATE: Deposits blocks must contain resolvable paths only — no placeholders, template variables, or markers. Use directory paths or Step 0 diagnostics for paths unknown at plan-write time.
- **Reasoning:** Entry proposes a clear rule: 'anything inside **Deposits:** must be a real, resolvable path — either a specific file the Planner is confident about, or a directory that contains the agent\'s output. Placeholders, template variables, or <resolved-during-execution> markers all trip the gate literally.' Grounded in evidence: 'deposit_exists gate doesn\'t wait for the agent to resolve placeholders — it reads the block at the moment the agent reports Complete.'
- **Confidence:** high

### 2026-05-12 — Verdict response files go to `verdicts/resolved/`, NOT `verdicts/pending/`


- **Suggested action:** Document in PLANNER_TEMPLATE Rule 25: verdict response files go to bellows/verdicts/resolved/, never pending/. The directory name is a writer-role marker, not a state description.
- **Reasoning:** Entry establishes the verdict response path rule: 'When the Planner writes a verdict response, the path is bellows/verdicts/resolved/verdict-<slug>-step-N.md — never pending/.' Grounded in evidence: consumer function 'scans verdicts/resolved/ exclusively (line 1048). Files in pending/ are never inspected by the consumer.' Note: this entry already has an implemented proposal (ID 34) from a prior cycle; this classification reflects the current cycle's independent assessment.
- **Confidence:** high

### 2026-05-12 — Verdict response format is `verdict: continue\n<reason>` — no markdown decoration


- **Suggested action:** Document verdict response format in PLANNER_TEMPLATE: first line is 'verdict: continue' (or 'verdict: stop'), subsequent lines are free-form reason text. No markdown headers, no bold fields.
- **Reasoning:** Entry establishes the verdict format rule: 'Verdict response files use the plain format: verdict: continue on line 1, free-form reason text on subsequent lines, no headers, no bolding.' Grounded in evidence: 'Bellows check_verdict() function expects the literal verdict: prefix on line 1.' Note: this entry already has an implemented proposal (ID 35) from a prior cycle.
- **Confidence:** high

### 2026-05-12 — "queue empty — all plans complete" means paused-or-done, NOT completed


- **Suggested action:** Document in PLANNER_TEMPLATE: 'queue empty — all plans complete' means no plans in-flight, NOT all plans finished. Check awaiting-verdict count and plan file state (in-progress/verdict-pending/Done) to determine actual completion.
- **Reasoning:** Entry proposes a behavioral rule: 'The Planner does not infer plan completion from queue empty. Completion signals are: the plan file appears in Done/, a verdict continue-to-done log event fires, the verdict-request count decreases to zero.' Grounded in evidence: 'Step 1 had paused awaiting verdict; Step 2 had not run. The misinterpretation went undetected for several conversation turns.' Note: this entry already has an implemented proposal (ID 36) from a prior cycle.
- **Confidence:** high

### 2026-05-12 — Dev-log self-reference SHA loop is structurally impossible


- **Suggested action:** Add guidance to PLANNER_TEMPLATE: do NOT require dev logs to reference their own commit SHA. Either defer SHA capture to QA step, or omit inline SHA and use slug-based lookup via git log --grep.
- **Reasoning:** Entry demonstrates structural impossibility: 'A commit\'s SHA is computed over its full contents including the dev-log text. Editing the dev log to insert the SHA produces a new tree, which produces a new SHA. There is no fixed point.' Proposes concrete alternatives: '(a) QA fills the SHA post-hoc' or '(b) Drop the inline SHA reference entirely.' Note: this entry already has an implemented proposal (ID 37) from a prior cycle.
- **Confidence:** high

### 2026-05-10 — When shipping a path-resolution fix, audit ALL gate functions that call _resolve_deposit_path


- **Suggested action:** Add to PLANNER_TEMPLATE.md plan-authoring rules: any plan that modifies a function signature in path-resolution code (gates.py, verdict.py, or similar) must include an explicit audit step — grep for ALL call sites of the modified function, identify every caller, and confirm each one threads the new parameter correctly. Diagnostics scoping such fixes should enumerate call sites as a first question.
- **Reasoning:** Entry documents a missed sibling gate function when _resolve_deposit_path was modified: '_gate_rule_20_self_check — a gate added 2026-05-05 that has the same _resolve_deposit_path dependency. The miss surfaced as false-positive rule_20_self_check failures.' The operational rule states 'any plan that modifies a function signature in gates.py or verdict.py must include a step that runs grep... and audits every hit.' The meta-lesson extends this to QA scope: 'QA scope should track functions that share the changed dependency, not just functions that were changed.' Classified as governance_rule because the primary fix is a plan-authoring rule. Confidence medium: tagless entry, and the grep-audit step has a secondary instrumentation angle (procedural checklist), but the dominant fix is a documentary rule for plan structure.
- **Confidence:** medium

### 2026-05-10 — When shipping a path-resolution fix, audit ALL gate functions that call _resolve_deposit_path


- **Suggested action:** Add rule: any plan modifying a function signature in gates.py or verdict.py must include a step that greps for ALL call sites and audits each for parameter threading. QA scope must track functions sharing the changed dependency, not just functions changed.
- **Reasoning:** Entry proposes an operational rule: 'any plan that modifies a function signature in gates.py or verdict.py must include a step that runs grep -n function_name gates.py verdict.py bellows.py and audits every hit.' Grounded in evidence: 'The 2026-05-06 fix threaded wt_path through _gate_deposit_exists but missed _gate_rule_20_self_check — a gate added 2026-05-05 that has the same _resolve_deposit_path dependency.' Note: this entry already has a proposed classification (ID 38) from a prior cycle.
- **Confidence:** high

## Instrumentation


### 2026-05-15 — GitHub's "inflate / pack has bad object" error is how its server reports the 100 MB hard file size limit, not actual corruption


- **Suggested action:** Add to project setup checklist: every new repo ships with .gitignore at commit 1 (excluding *.db, __pycache__/, *.pyc, .pytest_cache/, .venv/, .DS_Store). Add to git troubleshooting runbook: when 'pack has bad object' on push, push-bisect commit-by-commit to surface the actual file-size warning.
- **Reasoning:** Entry documents a misleading error: 'The inflate / bad object framing is GitHub\'s server-side reporting of the rejection, not a description of the underlying problem.' Proposes two procedural safeguards: (1) 'Every new project repo ships with a .gitignore at commit 1' — a new project setup step, (2) 'push commit-by-commit until the rejection includes the warning text' — a new diagnostic procedure. Both are instrumentation (checklists/procedures), not code changes.
- **Confidence:** high

### 2026-05-15 — `git filter-repo` removes the `origin` remote by default; rewriting also drops the affected file from the working tree


- **Suggested action:** Add git filter-repo checklist: (1) backup working tree before running, (2) re-add origin remote after, (3) restore checkout-removed working-tree files, (4) add restored files to .gitignore and commit, (5) force-push.
- **Reasoning:** Entry documents filter-repo side effects: 'the origin remote was silently removed' and 'the file was also removed from the working tree.' Proposes a concrete 4-step checklist: 'take a working-tree-level backup, re-add the remote, restore working-tree files, add to .gitignore, force-push. This is a four-step sequence and should be treated as a checklist.' This is a new procedural checklist, not a code change or rule.
- **Confidence:** high

### 2026-05-15 — Files already tracked by git are NOT retroactively ignored when added to `.gitignore`


- **Suggested action:** Add to gitignore update procedure: after adding a .gitignore rule to an existing repo, run git ls-files | grep <pattern> to find tracked matches, then git rm --cached for each. Verify with git status after adding new matching content.
- **Reasoning:** Entry documents a basic git semantic: '.gitignore only suppresses untracked files. Files that were tracked before the gitignore entry was added remain tracked.' Proposes a verification procedure: 'When adding a .gitignore rule, the next action is git ls-files | grep <pattern> to find any tracked files that match. Each match needs git rm --cached.' Medium confidence: the mitigation is actionable but the underlying knowledge is basic git behavior that may not warrant formal instrumentation.
- **Confidence:** medium

### 2026-05-15 — Existing gitlinks without `.gitmodules` are in "broken submodule" limbo; `git submodule add` is not the only path back


- **Suggested action:** Add submodule recovery procedure: when gitlink (mode 160000) exists in git ls-files --stage but no .gitmodules entry exists, hand-write .gitmodules, run git submodule init, verify with git submodule status showing clean prefix.
- **Reasoning:** Entry documents a specific edge case and recovery: 'The standard fix git submodule add refused to run because the directory already existed. The actual fix was to hand-write .gitmodules with the correct entry, then git submodule init.' Proposes a 3-step recovery sequence for a rare but documented failure mode. Medium confidence because this is a rare edge case; the recovery info is useful if the situation recurs.
- **Confidence:** medium

### 2026-05-14 — iCloud `dataless` eviction masqueraded as git corruption; only macOS file-flag inspection found the real cause


- **Suggested action:** Add to recovery diagnostic procedure: when git operation fails with mmap/Operation timed out, check OS-level file readability first (ls -lO on macOS for dataless flag) before assuming git-level corruption. Add hard rule: never put git repos in iCloud-synced folders.
- **Reasoning:** Entry documents iCloud eviction masquerading as git corruption: '1,061 of 4,879 loose objects (21.7%) carried the macOS file flag dataless — meaning iCloud had evicted the data content.' Proposes diagnostic procedure: 'the first diagnostic must test OS-level file readability before assuming git-level corruption.' Also proposes broader lesson: 'handoff documents framing the problem are hypotheses, not findings — the first diagnostic should test the framing against direct evidence.'
- **Confidence:** high

### 2026-05-13 (session 3) — Plan filename "drain-extraction-queue" became misleading historical record


- **Suggested action:** Add filename truthfulness check to plan deposit workflow: at the staging stage before move-file, read the plan\'s scope and verify the filename describes what the steps will actually do. If not, rename at staging before the move locks the name.
- **Reasoning:** Entry proposes a new check step: 'Filename truthfulness check immediately before atomic deposit. The deposit pattern has a natural pause point at staging where the filename can still be rewritten.' Grounded in evidence: 'Forge cycle 13 deposited as drain-extraction-queue but deliberately did NOT include per-chunk pattern extraction, which is what would have drained the queue.' The fix is a new procedural step in the deposit workflow.
- **Confidence:** high

## Structural


### 2026-05-18 — `deposit_exists` gate keys on literal staging filename inside Deposits prose; 4th Bellows gate false positive


- **Suggested action:** Fix deposit_exists gate in Bellows to skip _staging_* prefixed filenames during extraction, or restrict extraction to structured bullet lists under Deposits headers only.
- **Reasoning:** Entry documents the 4th Bellows gate false positive: 'deposit_exists gate parsed the Deposits prose, extracted the staging filename as a required deposit, and tripped.' Root cause is code-level: 'The deposit_exists gate extracts any path-like string from the Deposits block and checks for its existence on disk.' The proposed cross-cutting fix is structural: 'skip any path with _staging_ prefix during extraction' or 'only extract paths from bulleted lists immediately under Deposits headers.' The meta-observation identifies 'structural fragility' in the gate-design philosophy requiring architectural remediation (structured YAML deposits block).
- **Confidence:** high

### 2026-05-17 — Bellows Rule 20 gate keys on a specific stdout pattern; documenting the banner as a captured block trips the gate


- **Suggested action:** Relax rule_20_self_check gate pattern matching to tolerate shell-prompt prefixes and fenced code blocks, or create a helper script (bellows.rule_20_check) that prints the exact expected banner format.
- **Reasoning:** Entry describes the Rule 20 gate false positive: 'rule_20_self_check gate still tripped with no QA deposit contains Rule 20 self-check banner' despite banner text being present in fenced code block. Root cause is code-level gate matching: 'the regex appears to require the banner standing alone or in a specific block style, not inside a documented stdout fence with shell-prompt prefix.' Proposed fix is structural: 'the gate itself should be relaxed or the banner format standardized via a helper script in Bellows.'
- **Confidence:** high
