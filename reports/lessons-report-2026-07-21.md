# Lessons Report — 2026-07-21


## Summary


| Category | Count |
|---|---|
| governance_rule | 12 |

**Total proposals:** 12


## Governance Rule


### 2026-07-21: Parallelism belongs WITHIN a drafting-cycle pass, never ACROSS lenses — across-lens parallelism severs the cumulative property [tag: planner-discipline]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md that parallelism within a single lens pass is permitted but cross-lens parallelism is prohibited — across-lens parallel runs sever the cumulative property and must be labeled as panel passes, not walks.
- **Reasoning:** Entry states "Running the lenses concurrently against one frozen draft breaks exactly that: every reviewer sees the pre-fold draft, and the folds that walk produces are examined by nobody." Cites evidence: "The parallel run was re-designated a panel pass (a legitimate multi-finder sweep on a frozen draft, folding once as a composite) and walk 4 was re-run sequentially — where its very first lens immediately found a defect inside the panel's own fold." Distinguishing rule: "parallelism is compatible within one pass — the same cycle's ACID pass ran three tracers, each reading a different step, feeding ONE fold — and incompatible across lenses."
- **Confidence:** high

### 2026-07-21: A guard must observe from the tree where the state actually lives — lifecycle state is main-tree-uncommitted and structurally invisible to worktrees [tag: qa-discipline]


- **Suggested action:** Add QA discipline to PLANNER_TEMPLATE.md — any guard reading lifecycle or dispatch state must use an absolute main-tree path and assert a positive signal proving it is reading the live tree; absence-based checks over uncommitted state are structurally vacuous.
- **Reasoning:** Entry states "Bellows lifecycle renames (executable- -> in-progress- -> verdict-pending- -> Done/) are uncommitted filesystem operations in the MAIN tree. A worktree checkout therefore cannot see them at all — not stale, absent." Cites evidence: "Plan 244's isolation pre-flight ran ls knowledge/decisions/ relative to its worktree and reported 'no in-progress-* found' — while its OWN in-progress file sat in the main tree at that moment." Prescribes: "any guard reading lifecycle or dispatch state must use an absolute main-tree path, and must assert a positive signal proving it is reading the live tree."
- **Confidence:** high

### 2026-07-21: Resume machinery is justified only when the interrupted work is NOT reproducible from its recipe — reproducible work gets restore-and-redo [tag: plan-authoring]


- **Suggested action:** Add plan-authoring discipline to PLANNER_TEMPLATE.md — before building resume machinery, ask whether the interrupted work can be regenerated from a recipe the plan already carries; if yes, use restore-and-redo instead of surgical resume.
- **Reasoning:** Entry states "Surgical resume requires intactness verification, mangle detection, and apply-remainder logic — real machinery, each piece its own defect surface. Restore-and-redo requires none of it: it is deterministic and idempotent, and the failure modes a surgical resume must detect cannot survive the restore." Provides the deciding criterion: "The deciding question is reproducibility." Cites evidence: "The lessons-forge classification resume (plans 203/205) is justified — a committed classification is not reproducible, and blind re-classification manufactures duplicate proposals. The Gate-2 template apply is not — every edit is fully reproducible from the SA blueprint."
- **Confidence:** high

### 2026-07-21: Plan boilerplate inherited from the manual-execution era can instruct the exact act the daemon codifies as a violation [tag: bellows-integration]


- **Suggested action:** Add plan-authoring discipline to PLANNER_TEMPLATE.md — a bellows-dispatched plan's final instruction is the deposit commit, never a Done/ move; when a convention exists in two execution models, plan boilerplate must state which model it targets. Consider a plan_lint check for Dispatch Mode: bellows plans that instruct Done/ moves.
- **Reasoning:** Entry states "Under Bellows dispatch that move belongs to the daemon, on continue-verdict consumption. An agent-side move is Mode A: bellows.py detects 'agent moved to Done/ without authorization', force-recovers the file, appends an unauthorized_done_move failure, and flips the step's gates to FAILED." Explains persistence: "it is empirically latent. Every bellows agent ignored it; zero Mode-A events exist in the retained logs. Harmlessness is exactly what let it propagate — but its only possible outcomes are nothing or harm, never benefit."
- **Confidence:** high

### 2026-07-21: A novel lens reliably finds the right WINDOW and reliably ships a broken MECHANISM — sequence a standing lens behind its fold [tag: planner-discipline]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md that a novel lens's fold is treated as provisional — sequence a standing lens (weak spots or vulnerabilities) immediately behind it, aimed specifically at whether the new guard is executable, not at whether the window is real.
- **Reasoning:** Entry identifies a pattern across three demonstrations of the conflict-serializability lens: "each time the lens correctly identified an unguarded window that every standing lens had walked past; each time its fix carried a defect the next standing pass caught." States "A new lens's ANALYSIS is trustworthy — it is asking a question nobody asked. Its IMPLEMENTATION is untested — it has no track record of writing executable checks." Prescribes: "treat a novel lens's fold as provisional. Never deposit straight from it. Sequence a standing lens... immediately behind it, aimed specifically at whether the new guard is executable."
- **Confidence:** high

### 2026-07-21: Context saturation is a reviewer failure mode — when late walks go quiet, rotate the reviewer, not the lens [tag: planner-discipline]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md that when late drafting-cycle walks stop finding things, rotate the reviewer (run standing lenses cold with fresh-context agents reading only the artifact and verifying claims against the repo), sequentially to preserve cumulation; author verification of cold findings remains required.
- **Reasoning:** Entry states "A reviewer who authored the draft, or has read it through many passes, shares its assumptions and stops seeing them. A 'dry' verdict from a saturated reviewer is therefore weak evidence." Cites evidence: "six Planner-run walks had gone essentially quiet. A cold read — zero-context agents given only the draft plus read access to the repo — then found, on pass 8, a first-contact substance defect: three live doctrine phrases ('four-pass cycle', 'four named lenses', 'four heavy passes') that the five-lens amendment made false." Prescribes: "when late walks stop finding things, rotate the reviewer, not the lens."
- **Confidence:** high

### 2026-07-20: Add a conflict-serializability lens to the Drafting Cycle — model the plan's DB operations as a transaction schedule and check that concurrent execution stays serializable [tag: planner-discipline]


- **Suggested action:** Add a conflict-serializability lens to the Drafting Cycle in PLANNER_TEMPLATE.md — enumerate a plan's reads/writes on shared tables, identify R-W/W-R/W-W conflicts against plausible concurrent transactions, and require either an explicit isolation guard or a single locked transaction.
- **Reasoning:** Entry proposes a new Drafting Cycle lens: "none models the plan's operations as a SCHEDULE against concurrent transactions on shared state." It describes specific conflict patterns — "unrepeatable read yields a false verification halt" and "write-write conflict on the same row yields a silently-lost update" — and cites evidence from the Gate-1 plan where "A single pass of this new lens showed the isolation was assumed, never enforced." States it "Routes to Gate 2 as a Drafting Cycle amendment (a sixth lens, or a named facet of the ACID lens)."
- **Confidence:** high

### 2026-07-20: Drafting Cycle lenses have plan-shape-dependent skip-rules — destruction is provably dry on reversible-write plans; integration-vs-record is never skippable [tag: planner-discipline]


- **Suggested action:** Add plan-shape-dependent skip-rules to the Drafting Cycle lens descriptions in PLANNER_TEMPLATE.md — destruction is skippable after one dry pass on reversible/non-cascading-write plans; integration-vs-record is never skippable; ACID runs whenever >=2 lenses touch shared state.
- **Reasoning:** Entry specifies concrete tiered skip-rules from experiment: "Destruction — skippable after ONE pass on reversible/non-cascading-write plans" because "a plan whose only write is reversible and non-cascading cannot GROW a destruction surface through the cycle." States "Integration-vs-record — NEVER skip" because "it is the cycle's only SUBTRACTIVE lens (every other lens adds guards; integration measures the draft against the record/code and REMOVES over-build)." States "ACID — run whenever >=2 lenses touch shared state." Entry concludes "Routes to Gate 2."
- **Confidence:** high

### 2026-07-20: A fix is not done until a full-artifact sweep confirms no sibling instances of the same defect [tag: planner-discipline]


- **Suggested action:** Add sibling-sweep discipline to PLANNER_TEMPLATE.md — after fixing any anti-pattern instance, grep the whole artifact for the same pattern and confirm zero remaining, including negative examples and rationale text.
- **Reasoning:** Entry states "The defect is a CLASS, not the single instance in front of you; the class can have siblings elsewhere in the same artifact — and in the fix's own illustration." Prescribes: "after fixing any anti-pattern instance, grep the WHOLE artifact for the pattern (the bare number, the vacuous check, the wrong-signal guard, the un-isolated read) and confirm zero remaining — explicitly INCLUDING negative examples and rationale text." Cites evidence: "A hardcoded corpus count was removed from QA row 2 — but the same anti-pattern sat two rows down in QA row 4 (stale still 3), caught only a full walk later."
- **Confidence:** high

### 2026-07-20: The Drafting Cycle's lens set is OPEN — a novel lens finds what repetition cannot, and a new lens's first fold must be reviewed by the standing lenses [tag: planner-discipline]


- **Suggested action:** Codify in PLANNER_TEMPLATE.md that the Drafting Cycle's lens set is open (add a lens when a plan class raises a question existing lenses do not ask) and that a novel lens's fold must always be followed by a standing-lens sweep before deposit.
- **Reasoning:** Entry asserts "The cycle's power scales with the DIVERSITY of questions asked, not the number of repetitions of the same questions" and "A dry walk of the CURRENT lenses proves those questions are answered — not that the plan is sound." Proposes two rules: "treat the lens list as open, not closed — add a lens when a plan class raises a question the existing lenses do not ask" and "never deposit straight from a new lens's own fold — always follow a novel lens with a weak-spots (and ACID) sweep before deposit."
- **Confidence:** high

### 2026-07-20: Walk the lens list, don't re-run one lens to dry — a fold's defect is usually caught by a DIFFERENT lens reading a DIFFERENT source [tag: planner-discipline]


- **Suggested action:** Codify the walk-the-list model in PLANNER_TEMPLATE.md (one pass per lens, walk the whole list, a lens is re-run only on a subsequent walk, the cycle is done when a full walk returns only-minor findings), replacing the within-lens iterate-to-dry model.
- **Reasoning:** Entry states "three times, a defect INTRODUCED by a fold was caught only by a subsequent DIFFERENT lens, never by re-running the lens that would 'own' it" and provides three specific examples from the 2026-07-20 cycle. Explains: "folding changes the draft, AND each lens reads a different question against different evidence (code, record, specialist file, the plan-as-system). A defect born in a fold lands in text the owning lens has already passed, but is visible to the NEXT lens's distinct question." Proposes: "the stop condition should be rewritten to — one pass per lens; walk the whole list; a lens is re-run only on a subsequent walk; the cycle is done when a full walk returns only-minor findings."
- **Confidence:** high

### 2026-07-20: A `git status/diff -- <file>` from a submodule or worktree passes VACUOUSLY when the file is tracked by a different repo — use `git -C <the tracking repo>` [tag: qa-discipline]


- **Suggested action:** Add QA discipline to PLANNER_TEMPLATE.md — git verification of a file must run against the repo that tracks it using git -C <absolute path> and must assert on a positive signal, never merely empty output which absence also produces.
- **Reasoning:** Entry states "A git check scoped to a file that does not exist in the current tree reports 'clean' because the file is ABSENT, not because it is unmodified — a false green." Prescribes: "any git verification of a file must run against the repo that TRACKS that file — git -C <absolute path to the tracking repo> — and must assert on a POSITIVE signal (a known HEAD, a specific --exit-code diff), never merely 'empty output,' which absence also produces." Cites evidence: "git status -- LESSONS.md and git diff -- PLANNER_TEMPLATE.md both pass silently when run from inside the lessons-forge submodule/worktree, because both files are tracked by the ROOT repo."
- **Confidence:** high
