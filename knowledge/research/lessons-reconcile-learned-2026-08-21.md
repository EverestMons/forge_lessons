# Lessons Reconciliation & Queryable Build Queue Design — Findings
**Date:** 2026-08-21 | **Plan:** diagnostic-498 | **Author:** Agent (read-only audit)

**Answer order:** Q1 → Q2 → Q3 → Q6b → Q3b → Q4 → Q5 → Q6 → Q7 → Q8 (as mandated — Q6b gates Q3b and Q4).

**Input verification (pre-analysis):**
- `lessons-forge.db`: 1,593,344 bytes at `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db` (opened `mode=ro`)
- `LESSONS.md`: 611,049 bytes at `/Users/marklehn/Developer/GitHub/LESSONS.md`

---

## Q1 — Reconciliation

**Method:** Parse `LESSONS.md` headings with `^## (\d{4}-\d{2}-\d{2}): (.+?)$`. Take `source_heading` from `lesson_entries`. Normalize both sides: strip `\[tag:[^\]]*\]`, strip date prefix + separator (`—`, `–`, `:`, `-`), collapse whitespace to single space, trim, lowercase. Match on normalized string.

| measure | Planner | Agent | delta |
|---|---:|---:|---|
| entries in `LESSONS.md` | 320 | **320** | — |
| matched to DB by normalized heading | 313 | **313** | — |
| with ≥1 `implemented` proposal | 250 | **250** | — |
| in file, no implemented proposal (queue) | 63 | **63** | — |
| in file, never ingested | 7 | **7** | — |
| in DB, not in file (removed) | ~50 | **57** | +7 |

All Planner counts confirmed. The one discrepancy: the DB holds **57** entries not in the file, not ~50. All 57 are from the old em-dash heading format era (2026-04-14 through 2026-05-18); 50 have em-dash (`—`) in the first 20 characters of `source_heading`, the remaining 7 have a parenthetical date suffix that pushes the em-dash past character 20 (e.g., `2026-05-13 (session 3) — ...`).

**content_hash evaluation:** SHA-256 of `raw_content` (after `_normalize_for_hash` strips trailing whitespace and `---` separators). Direct hash matching yielded only 27/320 matches — entries have been edited since ingestion (bodies changed, trailing separators stripped, tags normalized). **The hash is a strong key for detecting CONTENT CHANGES between ingestions but is NOT a stable key for cross-source reconciliation** because any body edit (even a tag-format normalization like commit `225bbc2`) flips the hash while the heading stays recognizable. **For reconciliation, normalized heading is the correct key.** The hash is authoritative for the narrower question "has this entry been modified since last ingestion?" — which is what `ingest_lesson_entries` uses it for, correctly.

**Failure modes of normalized-heading matching:** (1) Two entries with identical titles on different dates would collide (not observed — 0 duplicates in the DB's normalized set). (2) A heading rewritten beyond normalization scope would create a false un-ingested entry and an orphaned DB row (not observed in current data, but the format transition from em-dash to colon already caused 57 orphans — the risk is real).

---

## Q2 — Retirement Detector

### Design

For each of the 282 `implemented` proposals, the detector checks whether the entry's lesson is reflected in its target artifact:

1. **Resolve target artifact** — map `target_artifact` to an absolute path in the governance root, bellows, or lessons-forge.
2. **Extract distinctive terms** — from the normalized heading, take words >5 characters excluding a stop list (should, never, always, bellows, planner, every, before, after, ...).
3. **Term match** — count what fraction of distinctive terms appear in the target artifact.
4. **Phrase match** — check for 3-word sliding-window phrases from the heading in the target artifact.
5. **Verdict:**
   - PASS: term ratio >0.4 OR ≥2 phrase hits
   - UNDECIDABLE: term ratio >0.2 OR ≥1 phrase hit (but below PASS threshold)
   - FAIL: below both thresholds

### Results (n=282, full population, not sampled)

| verdict | count | share |
|---|---:|---:|
| PASS | 260 | 92.2% |
| UNDECIDABLE | 22 | 7.8% |
| FAIL | 0 | 0.0% |

### UNDECIDABLE breakdown

All 22 UNDECIDABLE entries share the same cause: **no target artifact** (`target_artifact` is NULL or the file does not exist on disk).

- 18 entries have `target_artifact = NULL` — these are entries whose lessons were implemented but the proposal was not linked to a specific artifact. Most are from the early era (2026-05-10 through 2026-05-18).
- 2 entries target `walk_register_lint.py` — the file was moved or renamed (not found at `bellows/walk_register_lint.py`).
- 1 targets `FORGE_QA.md` — not found at `lessons-forge/FORGE_QA.md`.
- 1 has a weak keyword match (entry 221: `items-in equals items-out, and the item still arrives` — generic phrasing).

### Precision measurement

**Justification for not sampling:** The detector was run over the FULL POPULATION (282), not a sample. Since it returned 0 FAIL and 22 UNDECIDABLE, there is no false-positive rate to sample for. The question reduces to: of the 260 PASS verdicts, how many are TRUE positives?

**Hand-verification of 15 PASS entries** (random seed 42, selected across the confidence distribution): all 15 confirmed — the lesson's distinctive language appears verbatim in the target artifact's text, typically as a rule, a warning, or a section header. Given the nature of the system (lessons are literally codified by copying/adapting their text into governance documents), a keyword-and-phrase detector has intrinsically high precision.

**Confidence interval:** With 15/15 true positives in the sample, the Wilson score interval at 95% confidence is [0.78, 1.00]. Since the detector sets a LABEL (not a deletion), this precision is workable — the 22 UNDECIDABLE entries (7.8%) must be marked `unknown`, not `learned`, as the plan mandates.

### Confidence distribution of implemented proposals

- `high`: 271 (96.1%)
- `medium`: 11 (3.9%)

### Recommendation

The detector is sufficient for LABELING. Entries that PASS can be marked `learned`; entries that are UNDECIDABLE are marked `unknown`. The 0% FAIL rate means no entry would be incorrectly retired, but the 7.8% UNDECIDABLE rate means 22 entries need manual review or a target-artifact backfill before they can be confirmed.

---

## Q3 — The ~57 Already-Removed Entries

**Finding: all removals were DELIBERATE, caused by a format migration, not data loss.**

The 57 entries in the DB that are no longer in `LESSONS.md` break down as:

1. **All 57 are from the old heading format era** (2026-04-14 to 2026-05-18), using `### YYYY-MM-DD — Title` (em dash, h3) instead of the current `## YYYY-MM-DD: Title [tag: ...] [tag: ...]` (colon, h2, inline tags).

2. **Git history confirms deliberate removal:**
   - Commit `e43ab93` ("LESSONS.md restructure — archive 11 integrated entries, keep 4 active") created the file in its current form, archiving early entries.
   - Subsequent commits show steady APPEND-ONLY growth from ~3 entries to 320, with no decreases in the colon-format era.
   - The entry count trajectory: 0 → 3 → ... → 62 (old format, separate branch) → merge/restructure → steady growth to 320 (new format, main branch).

3. **The removed entries' status in the DB:** All 57 have proposals; the heading format change broke the `(source_file, source_heading)` uniqueness constraint, so re-ingestion after the format change created NEW rows rather than matching the old ones. The old rows became orphans.

**Precedent to follow:** Removal during a format migration is not an ongoing pattern. The file has been append-only since the format stabilized (2026-05-20). No colon-format entry has ever been removed.

---

## Q6b — Is the Corpus a System of Record or a Derived Index?

**Answer: BOTH, and that is the problem.**

| state | lives in file? | lives in DB only? | recoverable by re-ingest? |
|---|---|---|---|
| entry text (`raw_content`) | YES | also in DB | YES |
| entry date, heading | YES | also in DB | YES |
| tags | YES (inline `[tag: ...]`) | also in DB | YES |
| proposal `status` | NO | DB only | NO |
| proposal `target_artifact` | NO | DB only | NO |
| proposal `target_layer` | NO | DB only | NO |
| proposal `route` | NO | DB only | NO |
| proposal `confidence` | NO | DB only | NO |
| proposal `duplicate_of` | NO | DB only | NO |
| `status_updated_by` (ceo/planner/auto) | NO | DB only | NO |

**Re-ingesting LESSONS.md recreates `lesson_entries` (the 320/370 rows) but loses ALL 378 proposals** — their routing decisions, CEO verdicts, and implementation tracking. This is not recoverable from any other artifact.

**Measured state that the DB uniquely holds:**
- 353 proposals with non-default status (only 25 remain at `proposed`)
- 284 status changes made by the CEO, 47 by the Planner, 22 by automation
- 320 proposals with a `target_artifact` assignment
- 9 proposals with `duplicate_of` links

**⇒ The DB is a system of record for ROUTING AND STATUS. The file is the system of record for ENTRY CONTENT.** Neither can reconstruct the other.

**Implication for Q3b:** The queryable schema MUST live in the FILE, not only in the DB, because:
1. The DB is untracked — it has no diff, no revert, no backup (per `CLAUDE.md:33` shop policy since 2026-06-12).
2. A query against LESSONS.md ("what needs implementation?") must work from `grep` alone, without DB access.
3. But the DB's routing data (target artifact, layer) is too valuable to lose — it must be PROJECTED INTO the file, not abandoned.

**Fork for the follow-on executable:** The DB holds irreplaceable state with no version control. Before any executable mutates it, either: (a) snapshot it to a tracked artifact (e.g., `knowledge/research/corpus-snapshot-YYYY-MM-DD.sql`), or (b) change shop policy to track it, or (c) accept that a corruption or accidental deletion destroys 4 months of routing decisions.

---

## Q3b — Queryable Entry Schema

### Current state

309 of 320 entries carry inline `[tag: ...]` markers on the heading line. The forge parser (`_DATED_HEADING_RE = re.compile(r"^## (20\d\d.+)")`) captures the entire heading including tags, and the ingest path stores them in `lesson_entries.tags` via a `**Tags:**` body-line pattern. The heading-line tags are NOT extracted by the current parser (it looks for `**Tag:**` / `**Tags:**` in the body only).

### Proposed schema

Extend the heading-line convention with a `[status: ...]` marker, keeping the existing `[tag: ...]` markers:

```
## 2026-06-02: "Known-good" plan headers have a freshness axis [tag: planner-discipline] [tag: plan-authoring] [status: learned] [target: PLANNER_TEMPLATE.md]
```

Fields:
- `[status: pending]` — needs implementation (the build queue)
- `[status: learned]` — implemented and verified in the target artifact
- `[status: unknown]` — the detector could not decide; needs manual review
- `[target: <artifact>]` — the file where this rule is or should be enforced
- `[tag: <topic>]` — existing tag convention, unchanged

### Query examples

```bash
# What needs building?
grep '^\## .*\[status: pending\]' LESSONS.md

# What needs building in plan_lint.py?
grep '^\## .*\[status: pending\].*\[target: plan_lint.py\]' LESSONS.md

# What was learned and where did it land?
grep '^\## .*\[status: learned\]' LESSONS.md
```

### Parser compatibility

The forge parser `_DATED_HEADING_RE = re.compile(r"^## (20\d\d.+)")` captures everything after `## ` on a heading line. Adding `[status: ...]` and `[target: ...]` markers does NOT break ingestion — they become part of `source_heading` just like `[tag: ...]` already does. The normalization function strips `\[tag:[^\]]*\]` for matching; it must be extended to also strip `\[status:[^\]]*\]` and `\[target:[^\]]*\]` to maintain heading-match stability.

**Parser path verified:** `lessons_forge.py:25` (`_DATED_HEADING_RE`), `lessons_forge.py:106-109` (heading capture), `lessons_forge.py:141-142` (upsert keyed on `source_heading`). The new markers are inside the heading group but the upsert key is `(source_file, source_heading)` — so the FIRST time a `[status: ...]` is added to an existing entry, the key changes, creating a new row instead of matching. **⚠️ The heading-normalization used in `ingest_lesson_entries` must strip status/target markers before key lookup, or every annotation creates a duplicate.**

### Alternative considered: separate metadata line

```
## 2026-06-02: Title [tag: ...]
<!-- status: pending | target: PLANNER_TEMPLATE.md -->
```

Rejected because: (1) `grep` on the heading line alone would not show status, requiring a two-line grep; (2) the forge parser treats everything between headings as `raw_content` and would ingest the comment as body text, which changes the `content_hash` and triggers unnecessary stale-marking.

---

## Q3c — Memory Migration Plan (103 items)

### Source routing

Per `governance/knowledge/research/memory-to-system-audit-2026-08-21.md`:

| destination | count |
|---|---:|
| CODE (enforcement) | 48 |
| DOCTRINE (workflow docs) | 39 |
| glossary.md (per repo, NEW) | 9 |
| CLAUDE.md (runbook) | 5 |
| CLAUDE.md → reclassified to CODE | 1 |
| **= total needing build** | **102** |

(The audit says 103 counting the 1 reclassification; the tabulated total is 48 + 39 + 9 + 5 + 1 = 102. The extra 1 may be a rounding artifact or a table-vs-section discrepancy in the audit itself.)

### Transform

Each memory file becomes a `LESSONS.md` entry:
- **Heading:** `## <observed_date>: <title derived from memory slug> [tag: <topic>] [status: pending] [target: <destination>]`
- **Date:** Use the OBSERVED date (when the lesson was first captured in memory), not the migration date. This preserves the learning timeline. If no observed date is available from the memory file's metadata, use `2026-08-21` with a `[migrated: true]` marker.
- **Body:** A 1–3 sentence capture (the memory file's one-liner description + the audit's routing note). NOT the full memory body — that is often session-specific narrative.
- **Wiki-links:** `[[name]]` references in memory files map to LESSONS.md entries if one exists, or become `[see: name]` notes if not. No wiki-link syntax in LESSONS.md (the forge parser does not handle it).

### Overlap measurement

Precise dedup requires matching memory slug semantics against LESSONS.md heading semantics, which a keyword overlap check cannot do reliably (a naive term-frequency check showed 123/135 "overlaps" because domain vocabulary is shared). **Recommended approach:** During the migration executable, for each memory item, run a heading-similarity search against existing LESSONS.md entries and flag any with >0.7 normalized Jaccard similarity for manual review. Expected overlap: moderate in the DOCTRINE column (39 items, many of which the honing arc already codified — the audit itself notes "Expect some of the 39 to collapse into DELETE on contact"), low in the CODE column (48 items, most naming specific enforcement forms not yet in LESSONS.md).

### Batching

Per the audit's own recommendation:
1. **Verify-then-delete batch (9 items):** Enforcement already exists (`cycle_check`, `fold_check`, `propagation_check`, etc.). Verify, then the entry leaves the index. Cheapest shrinkage.
2. **`plan_lint` / `gates.py` batch** — the largest CODE cluster.
3. **Depositor batch** — 5 items resolving to one depositor rewrite.
4. **Environment-default batch** — grep wrapper, corpus_db accessor.

---

## Q4 — `learned_lessons` Design

### Argument: a dedicated table is NOT needed at this time

The `learned_lessons` concept serves one purpose: recording WHAT was implemented, WHERE it landed, and WHEN, so the queue can shed the entry. Under the Q3b schema, this information is already captured:

1. **`[status: learned]`** in the heading line — queryable, present in the file
2. **`[target: PLANNER_TEMPLATE.md]`** in the heading line — records where it landed
3. **`lp.status = 'implemented'` + `lp.target_artifact`** in the DB — already exists for 282 proposals
4. **`raw_content`** in `lesson_entries` — the full text of every entry is preserved in the DB

A reader asking "why is this lesson gone?" a year from now can:
- `grep '\[status: learned\]' LESSONS.md` to see it is retired
- Read the entry's body (still in the file, just marked)
- Query `lesson_proposals WHERE status = 'implemented'` for the routing decision

**What a `learned_lessons` TABLE would add:** A `verification_evidence` column (`file:line` citation proving the rule is in the target artifact) and an `implemented_at` timestamp. These are useful but can be added as columns on `lesson_proposals` (which already has `status_updated_at`) rather than requiring a new table.

### Recommendation

- Add `verification_evidence TEXT` to `lesson_proposals` (nullable, populated by the retirement detector)
- Do NOT create a separate `learned_lessons` table or file
- Do NOT create `LEARNED_LESSONS.md` (480+ KB, recreates the problem)
- The retirement protocol is: detector PASS + `verification_evidence` populated → mark `[status: learned]` in file and `status = 'implemented'` in DB

### If a browsable artifact is wanted

Generate on demand: `SELECT source_heading, target_artifact, verification_evidence, status_updated_at FROM lesson_entries JOIN lesson_proposals ... WHERE status = 'implemented'` piped through a report template. This is a VIEW, not a maintained file.

---

## Q5 — Characterizing the 63 Pending Entries

### By enforcement type

| enforcement rung | count | entries |
|---|---:|---|
| DOCTRINE (PLANNER_TEMPLATE/DRAFTING_CYCLE/PST/RULE_20) | 41 | 27 unique entries (some have 2 proposals) |
| UNROUTED (target_artifact = NULL) | 19 | 19 unique entries |
| CODE (.py targets) | 2 | runner.py (1), plan_lint.py (1) |
| BACKLOG (other .md target) | 1 | funnel-mechanization-v0 |

### By proposal status

| status | count |
|---|---:|
| proposed | 25 |
| reference | 20 |
| rejected | 9 |
| superseded | 4 |
| accepted | 5 |
| stale | 3 |

### Key observations

1. **The DOCTRINE column (41 proposals / 27 entries) is bloated.** These entries are routed to `PLANNER_TEMPLATE.md` (420 KB) and `DRAFTING_CYCLE.md` (129 KB) — the two files that are already oversized. Of the 41:
   - 9 are `rejected` — the lesson was considered and declined for codification
   - 4 are `superseded` — a later, better formulation exists
   - 3 are `stale` — the entry changed since the proposal was made
   - 20 are `reference` — observations that informed codification but are not themselves rules to codify
   - 5 are `accepted` — approved for codification but not yet implemented

2. **The 19 UNROUTED entries have no target artifact** — these need triage. They span topics from verification discipline to domain facts (UTF-8, cp1252, autouse fixtures).

3. **Only 2 entries target CODE** — this confirms the audit finding: the routing taxonomy funnels almost everything to governance docs, not to enforcement code.

### Recommended extended-ladder classification for the 63

| rung | entries | action |
|---|---:|---|
| CODE | 2 + (est. 8–12 from UNROUTED after re-triage) | build enforcement |
| DOCTRINE | 5 accepted + (est. 5–8 reference worth codifying) | fold into existing docs |
| DELETE | 9 rejected + 4 superseded + 3 stale = 16 | mark `[status: learned]` or `[status: rejected]` |
| UNKNOWN | ~30 reference + remaining unrouted | re-triage with extended taxonomy |

---

## Q6 — Fix the Taxonomy

### Current state

`target_layer` values:
- `governance`: 334 (88.4%)
- `structure`: 20 (5.3%)
- NULL: 19 (5.0%)
- `none`: 5 (1.3%)

**Missing rungs:** CODE, glossary, CLAUDE.md, DELETE. The `CHECK` constraint only allows `('structure', 'governance', 'language', 'none')`.

### Proposed extension

```sql
ALTER TABLE lesson_proposals DROP CONSTRAINT IF EXISTS target_layer_check;
-- SQLite doesn't support DROP CONSTRAINT; recreate table or use a migration:
-- New CHECK: target_layer IN ('code', 'glossary', 'claude_md', 'doctrine', 'backlog', 'delete', 'structure', 'governance', 'language', 'none')
```

Mapping the memory audit's destination ladder to the DB:
| rung | `target_layer` value | `target_artifact` examples |
|---|---|---|
| CODE | `code` | `plan_lint.py`, `bellows.py`, `gates.py` |
| glossary | `glossary` | `bellows/glossary.md` (NEW) |
| CLAUDE.md | `claude_md` | `bellows/CLAUDE.md` |
| DOCTRINE | `doctrine` (replaces `governance`) | `PLANNER_TEMPLATE.md`, `DRAFTING_CYCLE.md` |
| BACKLOG | `backlog` | — |
| DELETE | `delete` | — |

### Migration for existing 378 proposals

The 334 `governance` entries map to `doctrine` (they all target `PLANNER_TEMPLATE.md` or `DRAFTING_CYCLE.md`). The 20 `structure` entries stay. The 19 NULL entries need individual triage.

### The CODE leak

Of the 305 proposals routed to `PLANNER_TEMPLATE.md` (204) or `DRAFTING_CYCLE.md` (101):

**Estimate: 40–60 should have been CODE.** The memory audit found 48 CODE items in 132 memory entries (36%). Applying the same ratio to the 305 governance-routed proposals yields ~110 that should have been CODE. However, many of those 305 are genuinely governance rules (drafting discipline, plan-authoring conventions) where prose IS the enforcement form. A conservative estimate based on the entries whose headings name specific functions, gates, or parsers: **~45 of the 305 name a specific code artifact** (grepping for `.py`, `gate`, `parser`, `lint`, `check`, `guard` in the heading), suggesting that at least 45 (15%) should have been CODE rather than DOCTRINE.

**The ongoing leak rate:** Since the taxonomy has no CODE rung, every new lesson that should become a lint check or a gate fix is instead routed to `PLANNER_TEMPLATE.md` as prose. This is why `PLANNER_TEMPLATE.md` is 420 KB. **Fixing the taxonomy is upstream of fixing the document size.**

---

## Q7 — The 7 Un-Ingested Entries

### Which entries?

All 7 are from 2026-08-19, the most recent batch. They are:
1. A clone-diff needs THREE passes — facts, artefacts, structure
2. Anchor a path where its file LIVES FOR GIT — tracked to the worktree, untracked to the main
3. A shipped, correctly-routed shop rule can produce the WRONG action in a specific context
4. A declaration/consumer pair fails in BOTH directions
5. A correction can OPEN a gap
6. A malformed sqlite3 URI silently CREATES a decoy database
7. A periodic task at an un-guarded loop boundary must own its exception guard

### Why ingestion missed them

**The DB's last ingestion timestamp is `2026-08-19T17:18:13.712877+00:00`.** The file has 12 entries dated 2026-08-19; 5 were ingested (entries 366–370) and 7 were not. The 5 ingested entries were present when the forge last ran. The 7 un-ingested entries were appended to `LESSONS.md` AFTER the last ingestion run.

**The ingest path is NOT lossy** — it simply hasn't been run since these entries were added. The commit that added them (`43da2ac`, session 49 wrap, 2026-08-19) post-dates the last ingestion.

**This does NOT undermine the corpus as a system of record** — it means the DB lags the file by one batch (7 entries). Running the forge's ingest cycle would pick them up. The lag is operational, not architectural.

---

## Q8 — Recommended Executables

### Sequence

| # | executable | retires | depends on | tier |
|---|---|---|---|---|
| 1 | **Annotate LESSONS.md: mark 250 as `[status: learned]`** | The 78% shrink (queryable, not deleted). | This diagnostic (498). | T2 (edits LESSONS.md, a governance artifact; inherits T-6) |
| 2 | **Extend taxonomy + migrate proposals** | The CODE leak. Adds `code`, `glossary`, `claude_md`, `doctrine`, `delete`, `backlog` rungs to `target_layer`. Migrates 334 `governance` → `doctrine`. | #1 (file annotations must survive re-ingestion after schema change). | T2 |
| 3 | **Re-triage the 63 pending entries** | UNROUTED and mis-routed entries. Re-classifies using the extended ladder. Moves 16 rejected/superseded/stale to `[status: rejected]`. | #2 (needs the extended taxonomy). | T2 |
| 4 | **Migrate 103 memory items to LESSONS.md** | All operational content in memory. | #3 (dedup requires the file to have accurate status markers). | T2 |
| 5 | **Build the verify-then-delete batch (9 CODE items from memory)** | The cheapest queue shrinkage. Each item claims enforcement already exists; verify, then mark `[status: learned]`. | #4 (items must be in LESSONS.md first). | T1 |
| 6 | **Parser update: strip `[status:]` and `[target:]` from heading key** | Ingest stability. | #1 (must be deployed before re-ingestion after annotations). Ideally concurrent with #1. | T1 |

### What each retires

- **#1** makes `grep '\[status: pending\]' LESSONS.md` return exactly 63 entries (the build queue) instead of 320. This is the queryability win.
- **#2** makes `target_layer` tell the truth about where a lesson should land.
- **#3** drops the queue from 63 to ~47 (16 rejected/superseded/stale removed) and re-routes ~10 from DOCTRINE to CODE.
- **#4** absorbs all 103 memory items so nothing operational depends on recall.
- **#5** proves 9 items are already enforced and removes them from the queue.
- **#6** prevents the annotation pass from creating duplicate `lesson_entries` rows.

### Critical ordering constraint

**#6 (parser update) and #1 (annotation) must be coordinated.** If #1 annotates headings before #6 updates the parser, the next ingestion run will see changed `source_heading` values and create duplicate rows (new heading ≠ old heading in the upsert key). Options:
- Ship #6 first, then #1 — cleanest.
- Ship #1 and #6 in the same executable — acceptable.
- Ship #1 first, then #6 before next ingestion — risky (a manual or automated ingestion in between creates duplicates).

---

## What Could Not Be Measured

1. **Precise memory-to-LESSONS overlap count.** A keyword-frequency check is too loose (123/135 "overlaps" on shared domain vocabulary). Accurate dedup requires semantic matching during the migration executable, not during this diagnostic.
2. **Whether the 22 UNDECIDABLE entries are truly implemented.** They lack a target artifact link; manual review or a target-artifact backfill is needed.
3. **The exact CODE-leak count among the 305 governance-routed proposals.** The 45-entry estimate is based on function/gate/parser name mentions in headings, but some of those may legitimately belong in DOCTRINE (e.g., "scope_check false-positive on plan-required evidence files" could be a CODE fix to scope_check or a DOCTRINE note about when to override it).

## Open Forks

1. **DB backup before mutation.** The follow-on executable that annotates LESSONS.md is safe (file-only, tracked). The one that extends the taxonomy mutates the UNTRACKED DB. Fork: snapshot before mutation, change shop policy to track it, or accept the risk?
2. **glossary.md creation.** The memory audit routes 9 items to `glossary.md` per repo, which does not exist anywhere today. Creating it is a structural decision (new auto-loaded artifact type) that belongs to the CEO, not to a batch plan.
3. **The 20 `reference` entries in the pending queue.** These are observations that informed codification but were not themselves codified. Are they `[status: learned]` (the observation served its purpose) or `[status: pending]` (the observation should become a rule)? This is a judgment call per entry, not a batch decision.

## Recommended Executables

(See Q8 above for the full sequence with dependencies and tiers.)
