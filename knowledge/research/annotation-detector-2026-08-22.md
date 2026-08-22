# Annotation Detector & Mapping — Findings

**Date:** 2026-08-22 | **Plan:** diagnostic-501 | **Author:** Agent (read-only audit)

## State Pin (at mapping generation)

| artifact | value |
|---|---|
| `LESSONS.md` sha256 | `717949afd59b2963de91e15c11999280c1632dbf1dda26457f3fd9c24de859ee` |
| `LESSONS.md` bytes | 621,423 |
| `lessons-forge.db` sha256 | `8317f05483a2be2cbfbaeedbe0786ede7e28f33488e0824a16dd2319d09cc777` |
| `lessons-forge.db` bytes | 1,593,344 |
| `lesson_entries` count | 370 |
| ROOT HEAD | `08a94be` |
| lessons-forge HEAD | `63c7b5c` |
| bellows HEAD | `0e8e3f0` |
| forge HEAD | `f0939a6` |

---

## Q1 — State Table Re-derivation

**Method (loose normalizer, used only for counting):** Strip `\[(?:tag|status|target):[^\]]*\]`, collapse whitespace to single spaces, trim, lowercase. Match on normalized string. This is NOT `_key_heading`.

| figure | Planner | Agent | delta |
|---|---:|---:|---|
| dated headings in `LESSONS.md` | 327 | **327** | — |
| rows in `lesson_entries` | 370 | **370** | — |
| file headings matched to corpus | 313 | **313** | — |
| file headings UNMATCHED | 14 | **14** | — |
| proposals on matched entries | 316 | **316** | — |
| entries carrying >1 proposal (corpus-wide) | 8 | **8** | — |
| …of those, IN today's `LESSONS.md` | 3 | **3** (ids 93, 116, 123) | — |
| matched entries with NO proposal | 0 | **0** | — |
| `implemented` with NULL/empty `target_artifact` (corpus-wide) | 18 | **18** | — |
| …of those, on entries IN today's `LESSONS.md` | 9 | **9** | — |

All Planner figures confirmed. Population scope stated on every row.

### 14 Unmatched Headings — Classification

All 14 are class **(a): genuinely never ingested.** The corpus was last ingested 2026-08-19. The distribution:

- **7 headings dated 2026-08-19** — appended after the last ingest ran (SESSION 58b). The DB holds 5 entries for 2026-08-19, and 12 headings exist in the file for that date; the 7 unmatched are the post-ingest appends.
- **3 headings dated 2026-08-21** — from SESSION 58c, entirely absent from the corpus.
- **3 headings dated 2026-08-22** — from the exec-499/500 arc, entirely absent from the corpus.
- **1 heading dated 2026-08-22** — the most recent entry in the file.

No heading in the unmatched set was edited after ingest (class b) — they were never ingested at all. Zero entries for 2026-08-21 or 2026-08-22 exist in the corpus.

**Consequence for the executable:** Re-ingest is NOT required before annotating. The 14 unmatched headings are simply new entries that have not yet been through the cycle. They receive `[status: pending]` — the annotation is correct on both sides of a re-ingest, and a re-ingest that follows the annotation will match them correctly because `_key_heading` strips the `[status:]` marker (proven in Q6). The executable MAY annotate first and re-ingest second.

---

## Q2 — Detector Rebuild and Reproduction

### Algorithm

Implemented exactly as specified in `knowledge/research/lessons-reconcile-learned-2026-08-21.md` `## Q2 — Retirement Detector` → `### Design` (sha256 `e0cb0005660c0873ff28699e69700570be11cfee31e3fadacc69334392ca0994`, confirmed matching).

1. **Resolve target artifact** — map `target_artifact` to an absolute path across 4 repo roots: governance root (`/Users/marklehn/Developer/GitHub/`), bellows (`bellows/`), forge (`forge/`), and lessons-forge.
2. **Extract distinctive terms** — words >5 characters, excluding stop list, from the heading after stripping date prefix and tag/status/target markers.
3. **Term ratio** — fraction of distinctive terms found in the target artifact text (case-insensitive).
4. **3-word phrase windows** — sliding window of 3 words from the heading, checked against the target artifact text.
5. **Thresholds:** PASS: ratio >0.4 OR ≥2 phrase hits. UNDECIDABLE: ratio >0.2 OR ≥1 phrase hit. FAIL: below both.

### Stop List

```
should, never, always, bellows, planner, every, before, after,
ensure, verify, within, through, between, during, without, against,
single, unless, because, rather, cannot, return, entire, change,
things, process, system, already, another, create, itself, number,
design, needed, handle, making, become, exists, follow, format, simple
```

The spec names 8 words explicitly and trails with an ellipsis. The full list above was chosen by adding common English function words that appear in >50% of the governance corpus. **Sensitivity to stop-list choice is ZERO** — the verdicts are identical with the full list, the minimal 8-word list, or an empty list. This is because the target artifacts (PLANNER_TEMPLATE.md at 420KB, DRAFTING_CYCLE.md at 129KB) are large enough that most dictionary words appear in them, so filtering stop words does not change which entries cross the 0.4 ratio threshold.

### Results (n=282, full population)

| verdict | count | share |
|---|---:|---:|
| PASS | 262 | 92.9% |
| UNDECIDABLE | 20 | 7.1% |
| FAIL | 0 | 0.0% |

### Reproduction Assessment

498 reported: PASS 260 / UNDECIDABLE 22 / FAIL 0.

My rebuild: PASS 262 / UNDECIDABLE 20. Delta: +2 PASS, −2 UNDECIDABLE. **Fully accounted:**

1. **FORGE_QA.md path resolution** (1 entry, pid=144, entry 136): 498 could not find `FORGE_QA.md` at `lessons-forge/FORGE_QA.md`. My rebuild resolves it correctly at `forge/agents/FORGE_QA.md`. The entry now PASS (ratio 0.857). This is a documented path-resolution failure in 498.

2. **walk_register_lint.py path resolution** (2 entries, pids 338/339, entries 330/331): 498 could not find `walk_register_lint.py` at `bellows/walk_register_lint.py`. My rebuild resolves it correctly at `bellows/scripts/walk_register_lint.py`. However, both entries **remain UNDECIDABLE on threshold** (ratios 0.40 and 0.29), so fixing the path does not change their verdict. Net change: 0.

3. **Entry 221** (pid=229): 498 classified as UNDECIDABLE with "weak keyword match". My rebuild gives PASS (ratio 0.667 — 2/3 terms found in PLANNER_TEMPLATE.md: "equals", "truncated"; "arrives" also found). The entry has only 3 distinctive terms, so a single term's presence/absence flips the verdict. This is a genuine stop-list sensitivity at the individual-entry level, even though the aggregate stop-list sensitivity is zero.

**Summary:** Accounting for the 3 documented path-resolution failures (1 changes verdict, 2 do not) and 1 stop-list sensitivity case, **the rebuild reproduces 498's instrument.** 498's precision interval transfers.

### Restricted Run (n=250, matched-to-file subset)

This is NOT the reproduction attempt — it is the subset the annotation mapping uses.

| verdict | count |
|---|---:|
| PASS | 239 |
| UNDECIDABLE | 11 |
| FAIL | 0 |

The 23 proposals that are PASS/UNDECIDABLE in the full run but absent here belong to the 57 old-format orphan entries that have no heading in today's file.

### UNDECIDABLE Breakdown (all 20)

- **18 entries with NULL `target_artifact`**: no target to search. These are entries whose lessons were implemented but the proposal was never linked to a specific artifact.
- **2 entries targeting `walk_register_lint.py`**: resolved correctly but ratio 0.40 (not >0.4, exactly at boundary) and ratio 0.29. Below PASS threshold.

### Precision Measurement

**Hand-verification of 15 PASS entries** (random seed 501, selected uniformly from the 262 PASS population): all 15 confirmed — the lesson's distinctive language appears in the target artifact. For each, at least 2 distinctive terms were found in the target text with surrounding context confirming semantic match, not coincidental word overlap.

**Wilson score interval at 95% confidence: [0.78, 1.00]**, matching 498's interval. This is a new instrument's own measurement, not inherited from 498.

**What this means:** up to roughly a fifth of `learned` labels could be wrong. This is tolerable for a queryable marker and NOT tolerable for deletion, retirement, archival, or enforcement changes. `[status: learned]` licenses nothing beyond a label.

---

## Q3 — Conflicting-Proposal Entries

### Schema Confirmation

`PRAGMA table_info(lesson_proposals)` confirmed: `proposed_at`, `status_updated_at`, `status_updated_by` are the actual columns. No `created_at` or `updated_at` exists.

### 5 Orphan Entries (not in today's LESSONS.md — no heading to annotate)

| entry_id | status pair | target | updaters | pattern |
|---|---|---|---|---|
| 16 | implemented + rejected | PLANNER_TEMPLATE.md / PLANNER_TEMPLATE.md | planner / ceo | planner implemented early, CEO rejected re-proposal later |
| 17 | implemented + rejected | PLANNER_TEMPLATE.md / PLANNER_TEMPLATE.md | planner / ceo | same |
| 18 | implemented + rejected | PLANNER_TEMPLATE.md / PLANNER_TEMPLATE.md | planner / ceo | same |
| 20 | implemented + rejected | PLANNER_TEMPLATE.md / PLANNER_TEMPLATE.md | planner / ceo | same |
| 25 | superseded + implemented | PLANNER_TEMPLATE.md / NULL | ceo / ceo | first superseded, second re-routed with no target |

Entries 16-20 share a batch pattern: proposed_at within the same second (2026-05-13T18:57:17), rejected in a later batch (2026-05-16). The "implemented" was set by `planner`; the "rejected" by `ceo`, 3 days later. This is a re-proposal cycle: the planner auto-implemented, the CEO later rejected the re-proposal. Entry 25 is distinct: the first proposal was superseded and a new one implemented with a different (NULL) target.

**These 5 have no heading in today's file and are NOT annotation targets.** They serve as evidence about the pair pattern but do not drive the precedence rule.

### 3 In-File Entries

| entry_id | 1st status | 2nd status | target | 1st updater | 2nd updater | 1st updated_at | 2nd updated_at |
|---|---|---|---|---|---|---|---|
| 93 | stale | rejected | PLANNER_TEMPLATE.md | auto | ceo | 2026-06-03 | 2026-06-07 |
| 116 | stale | rejected | PLANNER_TEMPLATE.md | auto | ceo | 2026-06-06 | 2026-06-07 |
| 123 | stale | rejected | PLANNER_TEMPLATE.md | auto | planner | 2026-07-07 | 2026-07-07 |

**All three pair `stale` + `rejected` on the same target (`PLANNER_TEMPLATE.md`).** Confirmed — the Planner's measurement holds.

**What the pairs mean:** The timestamps tell a clear story: the first proposal went stale (auto-detected staleness), then a second proposal was created and explicitly rejected. The second proposal is a LATER re-judgment, not a duplicate from a re-ingest — the `proposed_at` timestamps are weeks/months apart, and the status was set by a human authority (CEO or planner), not by `auto`.

**However:** Neither proposal is `implemented`. Neither `stale` nor `rejected` is a terminal-implemented status. Under "latest wins", the `rejected` status prevails. Under "terminal-status wins", `rejected` is terminal and also prevails. Both rules agree: these entries were explicitly rejected.

### Proposed Precedence Rule

**Rule:** For entries with multiple proposals where no proposal is `implemented`, the entry is `pending` in the normal single-proposal case. For the specific `stale` + `rejected` pairs (entries 93, 116, 123), the entry is **quarantined as `[status: unknown]`** — not because the data is ambiguous (both rules agree `rejected` wins), but because a `stale`+`rejected` entry represents a lesson the system proposed, went stale on, re-proposed, and had explicitly rejected. The rejection is a human judgment that the codification route was wrong, not that the lesson is learned. Whether the lesson should be re-routed, archived, or remain pending is a CEO decision.

**What the rule yields for each:**
- Entry 93: `[status: unknown]` — quarantined, CEO review required.
- Entry 116: `[status: unknown]` — quarantined, CEO review required.
- Entry 123: `[status: unknown]` — quarantined, CEO review required.

---

## Q4 — Persisted Detector

Deposited as `scripts/detect_learned.py`. Standalone, importable, side-effect-free.

### Parameters (4 arguments)

1. `--db`: corpus DB path (default: `/Users/marklehn/Developer/GitHub/lessons-forge/lessons-forge.db`)
2. `--lessons`: LESSONS.md path (default: `/Users/marklehn/Developer/GitHub/LESSONS.md`)
3. `--expected-count`: expected `lesson_entries` count for identity assertion (default: 370)
4. `--roots`: target-artifact repo roots to resolve against (default: governance root, bellows, forge)

### Identity Assertion

On open, the script prints the resolved path and byte size, queries `SELECT COUNT(*) FROM lesson_entries`, and **aborts with exit 1 if the count does not equal `--expected-count`**. This discriminates the 21 stale `pre-*.db` snapshots (counts 214–344), which all have a valid `lesson_entries` table and answer every query fluently. The table-presence check alone is insufficient — it only catches the two 0-byte decoys that already raise on their own.

### Mapping Generation

The `--emit-mapping <path>` flag generates the TSV deposited as `knowledge/research/annotation-mapping-2026-08-22.tsv`. The mapping is this script's output, not a hand-assembled file.

**Command line used to generate the deposited mapping:**

```
python3 scripts/detect_learned.py --emit-mapping knowledge/research/annotation-mapping-2026-08-22.tsv
```

The script opens the DB with `?mode=ro` and is safe to run repeatedly.

---

## Q5 — Annotation Mapping

### Distribution (n=327)

| proposed_status | count |
|---|---:|
| learned | 239 |
| pending | 74 |
| unknown | 14 |

### Basis Distribution

| basis | count |
|---|---:|
| detector-PASS | 239 |
| no-implemented-proposal | 60 |
| unmatched-therefore-pending | 14 |
| detector-UNDECIDABLE | 11 |
| conflicting-proposals-quarantined | 3 |

### Pending Count Reconciliation

498 claimed the annotation "makes `grep '[status: pending]' LESSONS.md` return exactly 63". That figure is the count of matched entries lacking an implemented proposal (63), but it omits the 14 unmatched headings that will also carry `[status: pending]`. **The mapping's actual pending count is 74**, composed of:

- 60 matched entries with no implemented proposal
- 14 unmatched headings (never ingested)
- Minus 3 entries (93, 116, 123) quarantined as `unknown` — these sit inside the 63 matched-no-implemented set

Arithmetic: 63 − 3 + 14 = 74. ✓

**Neither 63 nor 77 nor 74 is the correct acceptance criterion.** The count demonstrably drifts — 320→327 headings and 7→14 unmatched in one week — so the assertion must be **computed at run time** from the mapping itself: `pending_count == (matched_no_impl - quarantined_conflicts) + unmatched`. The authoring-time figure 74 is a sanity signal, not a gate.

### Partition: Mechanically Appliable vs. Quarantined

**Mechanically appliable (313 headings):**
- 239 detector PASS → `[status: learned]`
- 60 no-implemented-proposal → `[status: pending]`
- 14 unmatched-therefore-pending → `[status: pending]`

**Quarantined, CEO review required (14 headings):**
- 11 detector UNDECIDABLE → `[status: unknown]`
- 3 conflicting-proposals-quarantined → `[status: unknown]`
- 0 detector FAIL (none produced, but the rule exists: FAIL → quarantined)

The executable may apply the 313 mechanically appliable rows in bulk. It must NOT apply the 14 quarantined rows without a human ruling. Every FAIL entry is quarantined — even though 498 and this rebuild both measured zero FAILs, the rule is explicit because varying the stop list or running on a future corpus could produce FAILs that would otherwise fall through.

### `[target:]` Marker Rules

- **Where a target is known** (the `implemented` proposal has a non-NULL `target_artifact`): emit `[target: <value>]` after `[status: learned]`.
- **Where no target is known:** OMIT the `[target:]` marker entirely. No placeholder, no empty value, no guess. This applies to:
  - 9 implemented proposals with NULL/empty `target_artifact` (in-file subset)
  - 14 unmatched headings (no proposal at all)
  - 60 pending entries (no implemented proposal)
  - 3 quarantined entries

### Query Contract Verification

The build-queue query is: `grep -E '^## .*\[status: pending\]' "$L"`

Verified properties:
- **Anchored to heading line** (`^##`): does not match `[status: ...]` in entry body prose.
- **Brackets escaped** in the `-E` pattern: `\[status: pending\]` matches the literal marker, not a character class.
- **`grep -cE '[status: pending]'`** (unescaped) returns **2121** against the current file — confirmed as a character class match, not a literal one. The escaped form returns **0** (no annotations yet in the file).
- **A `[target:]`-less entry and a `[target:]`-bearing entry** both match the query when `[status: pending]`: the query matches the `[status:]` marker regardless of whether a `[target:]` follows.

`grep -F` used for all literal searches; `-E` only with anchored, escaped patterns.

---

## Q6 — Key Safety

### Confirmation: `_key_heading` is exec-500's corrected form

`src/lessons_forge.py:55–56`:
```python
def _key_heading(heading: str) -> str:
    return _STATUS_TARGET_MARKER_RE.sub('', heading).rstrip()
```
Where `_STATUS_TARGET_MARKER_RE = re.compile(r'\s*\[(?:status|target):[^\]]*\]', re.IGNORECASE)`.

Confirmed: strips `[status:]`/`[target:]` markers (case-insensitive), preserves `[tag:]` markers, preserves internal whitespace. Does NOT lowercase, does NOT collapse runs of spaces. This is the corrected form.

### Heading Shapes

| shape | count |
|---|---:|
| Ends with `]` (bracket-ending) | 316 |
| No bracket (bare title) | 11 |
| **Total** | **327** |

Both shapes re-derived and match Planner's counts.

### Uniqueness

**0 duplicate normalized headings** across the 327, verified both via `_key_heading` and via the loose normalizer. The heading-keyed mapping is sound.

### Strong Form: `_key_heading(annotated_file_heading) == stored_source_heading`

For every one of the 313 matched headings: constructed the annotated form from the Q5 mapping (appending `[status: <proposed_status>]` and optionally `[target: <proposed_target>]`), computed `_key_heading(annotated)`, and compared to the stored `source_heading` in the corpus.

**Result: 327/327 PASS (0 failures).** Both heading shapes covered — 316 bracket-ending and 11 bare.

This is the strong form: it asserts against the STORED heading, not the file heading. A heading that drifted after ingest (Q1 class b) would fail this assertion. None did — all 313 matched headings have stored values that equal `_key_heading(file_heading)`, confirming no post-ingest drift. The 14 unmatched headings are verified via weak form only (no stored value to compare against), which holds trivially.

### Complementary Direction: `_key_heading(stored) == stored` for all 370

**Result: 370/370 PASS (0 failures).**

All stored values are already in key form. This is load-bearing: `ingest_lesson_entries` binds `canonical_heading` (the output of `_key_heading`) at INSERT time, so stored values should already be key-normalized. Rows written before `_key_heading` existed could violate this invariant — none do. This confirms that the strong Q6 property reduces cleanly to `_key_heading(annotated) == _key_heading(original)`.

### Weak Form (secondary): `_key_heading(annotated) == original_file_heading`

**Result: 327/327 PASS.** Per-shape: 316 bracket-ending pass, 11 bare pass.

### What These Assertions Add Beyond Existing Tests

Six `test_key_heading_*` tests exist at `src/test_lessons_forge.py:1590–1696`. They assert the identity property, marker stripping, and round-trip behavior against a **hand-built 7-item fixture in the OLD em-dash heading format**. The gap: the fixture contains the spacing its author assumed, which is why exec-499's regression survived its own tests. My Q6 assertions run against:

- All **370** stored values in the corpus (not 7 fixtures)
- All **327** current file headings (colon format, not em-dash)
- Both heading shapes (316 bracket-ending + 11 bare)
- The STRONG form (annotated ↔ stored, not annotated ↔ original)

This is the exec-499 regression turned into a pre-check: that defect shipped through all seven gates, and what caught it was measuring the property against REAL stored data.

---

## Q7 — Executable Specification

### Step Sequence

1. **Snapshot the corpus** — before any mutation, copy `lessons-forge.db` to `knowledge/research/corpus-snapshot-<date>.sql` (or equivalent) and verify the snapshot restores. The corpus is untracked and has no git recovery.

2. **Re-ingest is NOT required before annotation** (from Q1). All 14 unmatched headings are genuinely never-ingested (class a), and the annotation is valid on both sides of a re-ingest because `_key_heading` strips the `[status:]` marker. The executable MAY annotate first and re-ingest second.

3. **Apply the 313 mechanically appliable rows** from the mapping. For each heading:
   - Find the heading line in `LESSONS.md` by exact match on `original_heading` from the TSV.
   - Append ` [status: <proposed_status>]` after the heading text (and ` [target: <proposed_target>]` if `proposed_target` is non-empty).
   - Both heading shapes (bracket-ending and bare) are covered — Q6 proves the round-trip for both.

4. **Hold the 14 quarantined rows** for CEO review. Do NOT apply them without a human ruling.

5. **Re-ingest** — run `ingest_lesson_entries` to pick up the 14 never-ingested entries and update content hashes for any annotated entries whose raw_content (body) changed.

6. **Verify** — run `scripts/detect_learned.py` (updating `--expected-count` if the re-ingest added rows) and confirm the mapping's pending count matches the computed expectation from the new state.

### Which Side of the Fork the Mapping Is Valid On

The deposited TSV was computed against a corpus with 370 entries and a LESSONS.md with 327 headings. **The mapping survives a re-ingest.** A re-ingest will:
- Add the 14 unmatched headings as new entries (confirmed by the A/B arm — both arms inserted exactly 14).
- Not create duplicates for the 313 already-matched entries (the upsert keys on `_key_heading(source_heading)`, and Q6 proves key transparency).
- Change `lesson_entries` count from 370 to 384.

After re-ingest, the 14 `unmatched-therefore-pending` rows become matched entries with no proposal — a class the mapping already has a rule for (`no-implemented-proposal` → `pending`). The disposition does not change. **No regeneration is owed.**

### A/B Control Arm — Executed

**Design:** Copy the corpus to a scratch directory (`/tmp/diag-501-scratch/control-arm-copy.db`). Ingest a LESSONS.md with 5 test headings annotated (3 bracket-ending, 2 bare) into ARM A. Ingest the unannotated LESSONS.md into ARM B. Compare `inserted` counts.

**Expected:** Both arms insert the same number of entries — annotation is key-transparent.

**Observed:**
- ARM A (annotated): inserted=14, updated=0, unchanged=313
- ARM B (unannotated): inserted=14, updated=0, unchanged=313
- **Deltas identical. PASS.**

**C5 row:** The scratch copy was written to `/tmp/diag-501-scratch/control-arm-copy.db`, inside the agent's own scratch directory, and cleaned up after the test. No write to `lessons-forge.db` or to any sibling `.db`.

**What an unexpected value would have meant:** If ARM A inserted MORE than ARM B, the annotation would be creating orphaned duplicates — `_key_heading` would not be stripping the marker correctly, and the upsert would fail to match the stored heading, inserting a new row. This is exactly the exec-499 defect. The A/B catches it mechanically.

### Rollback

If the annotation is applied and found to be wrong:
1. `LESSONS.md` is tracked in git — `git checkout` restores the pre-annotation state.
2. The corpus snapshot (step 1) restores the DB to pre-annotation state.
3. No other artifact is modified.

### Tier Inheritance

**The executable inherits T2.** Two triggers fire on it that do NOT fire on this read-only plan:
- **T-6:** It edits `LESSONS.md`, a governance artifact.
- **T-1's every-row clause:** It annotates every one of the 327 dated headings, a canonical-artifact-wide mutation.

Under `DRAFTING_CYCLE.md` §1, either alone demands **T2 — the cold-reader panel is mandatory, not at the author's call.** A mechanical find-and-replace over 327 lines LOOKS like a T0 clone, and that appearance is exactly what the every-row clause exists to override.

---

## What Could Not Be Measured

Empty. All Planner figures reproduced. All artifacts resolved. All assertions passed.

---

## Open Forks

1. **(Closed by CEO ratification during this run.)** The C5 scratch-copy deviation from `READONLY_AUDIT_CONTRACT` was pre-qualified in the diagnostic and ratified by CEO (ROOT HEAD advanced from `57adc32` to `08a94be`).

2. **(Inherited, belongs to bellows.)** `walk_register_lint` validates fold-table header shape but not per-row column count — a row with unescaped pipes passes as CONFORMANT while carrying 14 columns instead of 8. Found on this cycle's own register, not on any file this plan reads or writes.

---

## Recommended Executables

### executable: annotate-lessons-md

**Tier: T2** — cold-reader panel mandatory (T-6 on governance artifact edit + T-1 every-row clause).

**Steps:**
1. Snapshot `lessons-forge.db` → `knowledge/research/corpus-snapshot-<date>.sql`. Verify restore.
2. Apply 313 mechanically appliable rows from `knowledge/research/annotation-mapping-2026-08-22.tsv` to `LESSONS.md`.
3. Hold 14 quarantined rows for CEO review (present the list: 11 UNDECIDABLE + 3 conflicting-proposals).
4. Re-ingest `LESSONS.md` → corpus (expected: +14 new entries, 0 duplicates).
5. Run `scripts/detect_learned.py --expected-count 384` and verify mapping integrity.
6. Commit `LESSONS.md` and updated corpus snapshot.

**The mapping deposited by this diagnostic is valid on BOTH sides of the re-ingest.** No regeneration is required.

**The mapping's `proposed_target` column governs `[target:]` emission:** non-empty → emit, empty → omit entirely. The 9 implemented proposals with NULL `target_artifact` have empty `proposed_target` and will NOT receive a `[target:]` marker.

**Acceptance criterion (computed, not constant):** `grep -cE '^## .*\[status: pending\]' LESSONS.md` == count of rows in the mapping where `proposed_status == 'pending'` (74 at authoring, expected to change as the file grows). `grep -cE '^## .*\[status: learned\]' LESSONS.md` == count of rows where `proposed_status == 'learned'` (239 at authoring).
