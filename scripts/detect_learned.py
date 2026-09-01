#!/usr/bin/env python3
"""
⚠️ SUPERSEDED FOR MARKER WRITES (CEO decision 2026-09-01): the `[status:]` marker
now carries `lesson_proposals.status` verbatim, projected by
`scripts/project_status_markers.py`. This detector's `proposed_status` values
(`pending` / `learned` / `unknown`) are the retired three-value file vocabulary;
use its PASS/FAIL detector verdicts as evidence for a DB status transition
(proposed -> implemented), never as a marker to write.

Retirement detector for LESSONS.md — determines which entries have been
codified into their target governance artifacts.

Rebuilt from the design in diagnostic-498's Q2 findings and persisted
by diagnostic-501 so the instrument is re-runnable and auditable.

Usage:
    python3 scripts/detect_learned.py
    python3 scripts/detect_learned.py --emit-mapping mapping.tsv
    python3 scripts/detect_learned.py --db /path/to/db --lessons /path/to/LESSONS.md
"""

import argparse
import csv
import os
import re
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import paths as _paths  # noqa: E402

# Layout-independent defaults (2026-09-01): resolved by src/paths.py, never literal.
DEFAULT_DB = str(_paths.db_path() or _paths.db_candidates()[0])
DEFAULT_LESSONS = str(_paths.lessons_md() or "LESSONS.md")
DEFAULT_EXPECTED_COUNT = 370
DEFAULT_ROOTS = [str(r) for r in _paths.artifact_roots()]

STOP_LIST = frozenset({
    "should", "never", "always", "bellows", "planner", "every",
    "before", "after", "ensure", "verify", "within", "through",
    "between", "during", "without", "against", "single", "unless",
    "because", "rather", "cannot", "return", "entire", "change",
    "things", "process", "system", "already", "another", "create",
    "itself", "number", "design", "needed", "handle", "making",
    "become", "exists", "follow", "format", "simple",
})

TARGET_MAP = {
    "PLANNER_TEMPLATE.md": "PLANNER_TEMPLATE.md",
    "DRAFTING_CYCLE.md": "DRAFTING_CYCLE.md",
    "RULE_20_SELF_CHECK_BLOCK.md": "RULE_20_SELF_CHECK_BLOCK.md",
    "PANEL_SEAT_TEMPLATE.md": "PANEL_SEAT_TEMPLATE.md",
    "bellows.py": "bellows/bellows.py",
    "runner.py": "bellows/runner.py",
    "walk_register_lint.py": "bellows/scripts/walk_register_lint.py",
    "FORGE_QA.md": "forge/agents/FORGE_QA.md",
}

HEADING_RE = re.compile(r"^## (20\d\d.+)$")
TAG_STATUS_TARGET_RE = re.compile(r"\[(?:tag|status|target):[^\]]*\]")
STATUS_TARGET_MARKER_RE = re.compile(r"\s*\[(?:status|target):[^\]]*\]", re.IGNORECASE)
DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[:\s—–-]+\s*")

CONFLICT_ENTRY_IDS = {93, 116, 123}


def resolve_target(target_artifact, roots):
    if not target_artifact:
        return None
    basename = target_artifact.strip()
    rel = TARGET_MAP.get(basename)
    if rel:
        for root in roots:
            candidate = os.path.join(root, rel)
            if os.path.isfile(candidate):
                return candidate
    for root in roots:
        for dirpath, _, filenames in os.walk(root):
            if basename in filenames:
                return os.path.join(dirpath, basename)
    return None


def extract_distinctive_terms(heading):
    h = DATE_PREFIX_RE.sub("", heading)
    h = TAG_STATUS_TARGET_RE.sub("", h)
    words = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", h)
    return [w.lower() for w in words if len(w) > 5 and w.lower() not in STOP_LIST]


def extract_phrases(heading, window=3):
    h = DATE_PREFIX_RE.sub("", heading)
    h = TAG_STATUS_TARGET_RE.sub("", h)
    words = [w.lower() for w in re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", h)]
    return [" ".join(words[i:i + window]) for i in range(len(words) - window + 1)]


def detect_one(heading, target_artifact, roots, target_cache):
    path = resolve_target(target_artifact, roots)
    if path is None:
        return "UNDECIDABLE", 0.0, 0, "no_target"

    if path not in target_cache:
        with open(path, encoding="utf-8") as f:
            target_cache[path] = f.read().lower()
    content = target_cache[path]

    terms = extract_distinctive_terms(heading)
    if not terms:
        return "UNDECIDABLE", 0.0, 0, "no_terms"

    hits = sum(1 for t in terms if t in content)
    ratio = hits / len(terms)

    phrases = extract_phrases(heading)
    phrase_hits = sum(1 for p in phrases if p in content)

    if ratio > 0.4 or phrase_hits >= 2:
        return "PASS", ratio, phrase_hits, "threshold"
    if ratio > 0.2 or phrase_hits >= 1:
        return "UNDECIDABLE", ratio, phrase_hits, "threshold"
    return "FAIL", ratio, phrase_hits, "threshold"


def loose_normalize(h):
    h = TAG_STATUS_TARGET_RE.sub("", h)
    h = re.sub(r"\s+", " ", h).strip().lower()
    return h


def run(db_path, lessons_path, expected_count, roots, emit_mapping=None):
    resolved_db = os.path.realpath(db_path)
    db_size = os.path.getsize(resolved_db)
    print(f"DB path: {resolved_db}")
    print(f"DB size: {db_size} bytes")

    uri = f"file:{resolved_db}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row

    count = conn.execute("SELECT COUNT(*) FROM lesson_entries").fetchone()[0]
    print(f"lesson_entries count: {count}")
    if count != expected_count:
        print(
            f"ABORT: expected {expected_count} lesson_entries, got {count}. "
            f"This may be a stale snapshot, not the live corpus.",
            file=sys.stderr,
        )
        conn.close()
        sys.exit(1)

    with open(lessons_path, encoding="utf-8") as f:
        lines = f.readlines()

    file_headings = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.rstrip())
        if m:
            file_headings.append((i + 1, m.group(1)))

    print(f"Dated headings in LESSONS.md: {len(file_headings)}")

    db_entries = conn.execute("SELECT id, source_heading FROM lesson_entries").fetchall()
    db_norm = {}
    for row in db_entries:
        n = loose_normalize(row["source_heading"])
        db_norm.setdefault(n, []).append((row["id"], row["source_heading"]))

    matched = {}
    unmatched = []
    for line_no, h in file_headings:
        n = loose_normalize(h)
        if n in db_norm:
            matched[(line_no, h)] = db_norm[n]
        else:
            unmatched.append((line_no, h))

    print(f"Matched: {len(matched)}, Unmatched: {len(unmatched)}")

    proposals = conn.execute(
        "SELECT id, entry_id, status, target_artifact FROM lesson_proposals"
    ).fetchall()
    proposals_by_entry = {}
    for p in proposals:
        proposals_by_entry.setdefault(p["entry_id"], []).append(dict(p))

    target_cache = {}
    from collections import Counter
    verdicts_all = Counter()

    impl_proposals = conn.execute(
        "SELECT p.id, p.entry_id, p.target_artifact, e.source_heading "
        "FROM lesson_proposals p JOIN lesson_entries e ON e.id = p.entry_id "
        "WHERE p.status = 'implemented'"
    ).fetchall()

    detector_results = {}
    for row in impl_proposals:
        verdict, ratio, phrase_hits, reason = detect_one(
            row["source_heading"], row["target_artifact"], roots, target_cache
        )
        verdicts_all[verdict] += 1
        detector_results[row["entry_id"]] = {
            "verdict": verdict,
            "ratio": ratio,
            "phrase_hits": phrase_hits,
            "reason": reason,
            "target": row["target_artifact"],
        }

    print(f"\n=== Detector verdicts (n={len(impl_proposals)}, all implemented) ===")
    for v in ["PASS", "UNDECIDABLE", "FAIL"]:
        print(f"  {v}: {verdicts_all[v]}")

    mapping_rows = []
    for line_no, h in file_headings:
        n = loose_normalize(h)
        entry_ids = [eid for eid, _ in db_norm.get(n, [])]

        if not entry_ids:
            mapping_rows.append({
                "line_no": line_no,
                "entry_id": "",
                "original_heading": h,
                "proposed_status": "pending",
                "proposed_target": "",
                "basis": "unmatched-therefore-pending",
            })
            continue

        entry_id = entry_ids[0]

        if entry_id in CONFLICT_ENTRY_IDS:
            mapping_rows.append({
                "line_no": line_no,
                "entry_id": str(entry_id),
                "original_heading": h,
                "proposed_status": "unknown",
                "proposed_target": "",
                "basis": "conflicting-proposals-quarantined",
            })
            continue

        if entry_id in detector_results:
            dr = detector_results[entry_id]
            if dr["verdict"] == "PASS":
                target_val = dr["target"] if dr["target"] else ""
                mapping_rows.append({
                    "line_no": line_no,
                    "entry_id": str(entry_id),
                    "original_heading": h,
                    "proposed_status": "learned",
                    "proposed_target": target_val,
                    "basis": f"detector-PASS(ratio={dr['ratio']:.2f},phrases={dr['phrase_hits']})",
                })
            elif dr["verdict"] == "UNDECIDABLE":
                mapping_rows.append({
                    "line_no": line_no,
                    "entry_id": str(entry_id),
                    "original_heading": h,
                    "proposed_status": "unknown",
                    "proposed_target": "",
                    "basis": f"detector-UNDECIDABLE(ratio={dr['ratio']:.2f},phrases={dr['phrase_hits']},reason={dr['reason']})",
                })
            else:
                mapping_rows.append({
                    "line_no": line_no,
                    "entry_id": str(entry_id),
                    "original_heading": h,
                    "proposed_status": "unknown",
                    "proposed_target": "",
                    "basis": f"detector-FAIL(ratio={dr['ratio']:.2f},phrases={dr['phrase_hits']})",
                })
        else:
            entry_proposals = proposals_by_entry.get(entry_id, [])
            has_implemented = any(p["status"] == "implemented" for p in entry_proposals)
            if has_implemented:
                mapping_rows.append({
                    "line_no": line_no,
                    "entry_id": str(entry_id),
                    "original_heading": h,
                    "proposed_status": "pending",
                    "proposed_target": "",
                    "basis": "implemented-but-no-detector-result",
                })
            else:
                mapping_rows.append({
                    "line_no": line_no,
                    "entry_id": str(entry_id),
                    "original_heading": h,
                    "proposed_status": "pending",
                    "proposed_target": "",
                    "basis": "no-implemented-proposal",
                })

    status_dist = Counter(r["proposed_status"] for r in mapping_rows)
    basis_dist = Counter(r["basis"].split("(")[0] for r in mapping_rows)

    print(f"\n=== Mapping distribution (n={len(mapping_rows)}) ===")
    for s in ["learned", "pending", "unknown"]:
        print(f"  {s}: {status_dist[s]}")

    print(f"\n=== Basis distribution ===")
    for b, c in sorted(basis_dist.items()):
        print(f"  {b}: {c}")

    mechanically_appliable = sum(
        1 for r in mapping_rows
        if r["basis"].startswith("detector-PASS")
        or r["basis"] == "no-implemented-proposal"
        or r["basis"] == "unmatched-therefore-pending"
    )
    quarantined = sum(
        1 for r in mapping_rows
        if r["basis"].startswith("detector-UNDECIDABLE")
        or r["basis"].startswith("detector-FAIL")
        or r["proposed_status"] == "unknown"
    )

    print(f"\n=== Partition ===")
    print(f"  Mechanically appliable: {mechanically_appliable}")
    print(f"  Quarantined (CEO review): {quarantined}")

    if emit_mapping:
        with open(emit_mapping, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerow([
                "line_no", "entry_id", "original_heading",
                "proposed_status", "proposed_target", "basis",
            ])
            for r in mapping_rows:
                writer.writerow([
                    r["line_no"], r["entry_id"], r["original_heading"],
                    r["proposed_status"], r["proposed_target"], r["basis"],
                ])
        print(f"\nMapping written to: {emit_mapping}")

    conn.close()
    return mapping_rows


def main():
    parser = argparse.ArgumentParser(description="LESSONS.md retirement detector")
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to lessons-forge.db")
    parser.add_argument("--lessons", default=DEFAULT_LESSONS, help="Path to LESSONS.md")
    parser.add_argument(
        "--expected-count", type=int, default=DEFAULT_EXPECTED_COUNT,
        help="Expected lesson_entries count (identity assertion)",
    )
    parser.add_argument(
        "--roots", nargs="+", default=DEFAULT_ROOTS,
        help="Target-artifact repo roots to resolve against",
    )
    parser.add_argument("--emit-mapping", help="Path to write TSV mapping")
    args = parser.parse_args()

    run(args.db, args.lessons, args.expected_count, args.roots, args.emit_mapping)


if __name__ == "__main__":
    main()
