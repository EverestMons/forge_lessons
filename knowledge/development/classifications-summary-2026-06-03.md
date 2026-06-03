# Classifications Summary — 2026-06-03

**Total classified:** 23 entries (IDs 94-116)
**Proposals inserted:** 99-121

---

## Category Distribution

| Category | Count | % |
|---|---|---|
| governance_rule | 21 | 91.3% |
| narrative | 2 | 8.7% |
| structural | 0 | 0% |
| instrumentation | 0 | 0% |
| language | 0 | 0% |

## Confidence Distribution

| Confidence | Count | % |
|---|---|---|
| high | 16 | 69.6% |
| medium | 7 | 30.4% |
| low | 0 | 0% |

---

## Cross-Batch Synthesis

### Cluster 1: Bellows Operational Workarounds (11 entries, 47.8%)

Entries 95, 99, 100, 101, 103, 105, 107, 108, 110, 112, 116 all document Planner-side disciplines for navigating Bellows daemon behavior — teardown pre-checks, verdict mechanics, slug cache workarounds, and recovery procedures. This is the strongest signal for a consolidated PLANNER_TEMPLATE subsection (continuing the Bellows Operational Workarounds subsection shipped in v4.55).

Key sub-clusters:
- **Teardown discipline** (95, 100, 103, 108, 110): no-writes-during-dispatch + clean repo roots + R2 recovery
- **Verdict mechanics** (99, 105): read Gate Result JSON + write to resolved/
- **Daemon workarounds** (101, 107): orphan-guard replay prevention + _seen cache slug rename

### Cluster 2: Plan Authoring Discipline (8 entries, 34.8%)

Entries 94, 98, 102, 109, 111, 114, 115, 116 propose mechanical plan-authoring rules — header validation, literal path naming, memory-free convention strings, monotonic step labels, dispatch-mode checks, and blueprint completeness. These extend the Plan Authoring Checklist shipped in v4.55.

### Cluster 3: QA / Testing Verification (2 entries, 8.7%)

Entries 96, 97 propose QA verification discipline — feature-level assertion checking over aggregate pass counts, and wall-clock bounds external to pytest.

### Cluster 4: Gate 1 Routing (1 entry, 4.3%)

Entry 113 proposes a Gate 1 routing rule for daemon-bug workaround proposals.

---

## Narrative Entries (2)

| Entry | Heading | Reason |
|---|---|---|
| 104 | Wall-clock calibration — small-tier ≈ medium-tier | Observational timing data, no specific rule proposed |
| 112 | Verdict filename prefix tolerance | Documentation drift observation, no PLANNER_TEMPLATE action |

## Potential Consolidation Candidates

- **Entries 95 + 103:** Both document no-writes-during-dispatch discipline (different dates, overlapping substance)
- **Entries 108 + 110:** Both document R2 recovery for teardown cherry-pick conflicts (different variants of same shape)
- **Entries 98 + 116:** Both document literal file path naming for scope_check (different angles: deposit paths vs blueprint references)

## Ambiguous / Suspected-Duplicate Entries

No entries classified as ambiguous (status='ambiguous'). Three pairs flagged as potential consolidation candidates above — classified substantively per guardrail (do NOT assign category='duplicate').
