#!/usr/bin/env python3
"""
Project `lesson_proposals.status` onto the `[status: …]` marker of every
matching `LESSONS.md` heading.

CEO decision 2026-09-01: the heading marker is a PROJECTION of the forge
database's routing record, not a second opinion. The marker vocabulary is the
`lesson_proposals.status` vocabulary verbatim — implemented / proposed /
accepted / reference / rejected / superseded (`stale` proposals are ignored
when a live sibling exists). One value is reserved for the file side only:

    [status: pending]  — the entry has NO row in the database yet
                         (appended by a wrap sweep, not yet ingested).

An entry with no DB row is never touched by this tool (`--unmatched leave`,
the default); `--unmatched pending` stamps bare unmatched headings `pending`.

Safety: every run parses the register with the forge's own parser before and
after the edit and REFUSES to write unless (a) the entry count is unchanged,
(b) every `_key_heading` key is unchanged in order, (c) every `content_hash`
is unchanged in order, and (d) every non-heading line is byte-identical.
Marker edits are key-transparent by construction (`_key_heading` strips
status/target/project markers), so an ingest after this tool runs sees the
same entries.

Usage:
    python3 scripts/project_status_markers.py                  # dry run; finds the live DB
                                                               # ($LESSONS_FORGE_DB, <repo>/lessons-forge.db,
                                                               # <repo>/data/lessons-forge.db) and LESSONS.md
                                                               # ($ELUVIAN_WRAP_ROOT/LESSONS.md or <repo>/../LESSONS.md)
    python3 scripts/project_status_markers.py --apply          # write it
    python3 scripts/project_status_markers.py --db PATH --lessons PATH   # explicit
    python3 scripts/project_status_markers.py --snapshot knowledge/research/corpus-snapshot-2026-08-21.sql \
        --lessons /path/to/LESSONS.md --apply             # from a dump, on a machine without the live DB
    … --mapping out.tsv                                   # write the per-heading transition table

Exit codes: 0 ok (dry run or applied), 2 proofs failed (nothing written),
3 bad input.
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.lessons_forge import parse_lessons_md, _key_heading  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DB_CANDIDATES = [REPO / "lessons-forge.db", REPO / "data" / "lessons-forge.db"]


def discover_db() -> Path | None:
    """The live DB: $LESSONS_FORGE_DB, else the first non-empty candidate in the repo."""
    env = os.environ.get("LESSONS_FORGE_DB")
    cands = ([Path(env)] if env else []) + DB_CANDIDATES
    for c in cands:
        if c.is_file() and os.path.getsize(c) > 0:
            return c
    return None


def discover_lessons() -> Path | None:
    """LESSONS.md: $ELUVIAN_WRAP_ROOT/LESSONS.md, else the repo's parent (shop layout)."""
    env = os.environ.get("ELUVIAN_WRAP_ROOT")
    cands = ([Path(env) / "LESSONS.md"] if env else []) + [REPO.parent / "LESSONS.md"]
    for c in cands:
        if c.is_file():
            return c
    return None

HEADING_RE = re.compile(r"^## (20\d\d.+)$")
STATUS_RE = re.compile(r"\s*\[status:\s*[a-z-]+\]", re.IGNORECASE)
TAG_RE = re.compile(r"\s*\[tag:[^\]]*\]", re.IGNORECASE)
SEP_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\s*[—:\-–]\s*")
FILE_ONLY_STATUS = "pending"


def normalize(heading: str, drop_tags: bool = False) -> str:
    """Key a heading the way the DB stores it, then flatten the separator style.

    `_key_heading` strips [status:]/[target:]/[project:] and keeps [tag:]. Old DB
    rows use `DATE — Title`; the file uses `DATE: Title`; both map to `DATE: `.
    """
    h = _key_heading(heading)
    if drop_tags:
        h = TAG_RE.sub("", h).rstrip()
    h = SEP_RE.sub(r"\1: ", h)
    return re.sub(r"\s+", " ", h).strip()


def load_snapshot(sql_path: str) -> str:
    """Load a `.sql` dump that uses `unistr(...)` into a temp DB; return its path."""
    sql = Path(sql_path).read_text(encoding="utf-8")

    def dec(m: re.Match) -> str:
        s = m.group(1).replace("''", "'")
        s = re.sub(r"\\U([0-9a-fA-F]{8})", lambda x: chr(int(x.group(1), 16)), s)
        s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda x: chr(int(x.group(1), 16)), s)
        s = s.replace("\\\\", "\\")
        return "'" + s.replace("'", "''") + "'"

    sql = re.sub(r"unistr\('((?:[^']|'')*)'\)", dec, sql)
    fd, path = tempfile.mkstemp(prefix="corpus-", suffix=".db")
    os.close(fd)
    con = sqlite3.connect(path)
    con.executescript(sql)
    con.commit()
    con.close()
    return path


def governing_proposal(proposals: list[sqlite3.Row]) -> sqlite3.Row:
    """The proposal whose status the marker projects: newest non-stale row."""
    live = [p for p in proposals if p["status"] != "stale"] or list(proposals)
    return sorted(
        live,
        key=lambda p: (p["status_updated_at"] or p["proposed_at"] or "", p["id"]),
    )[-1]


def db_index(con: sqlite3.Connection):
    con.row_factory = sqlite3.Row
    props = collections.defaultdict(list)
    for r in con.execute("SELECT * FROM lesson_proposals ORDER BY entry_id, id"):
        props[r["entry_id"]].append(r)
    by_k1 = collections.defaultdict(list)
    by_k2 = collections.defaultdict(list)
    for e in con.execute("SELECT id, source_heading FROM lesson_entries"):
        by_k1[normalize(e["source_heading"])].append(e["id"])
        by_k2[normalize(e["source_heading"], drop_tags=True)].append(e["id"])
    return by_k1, by_k2, props


def plan_edits(lines: list[str], con: sqlite3.Connection, unmatched: str):
    by_k1, by_k2, props = db_index(con)
    edits = []  # (line_index, old, new, file_marker, db_status, entry_id)
    unmatched_rows = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        heading = m.group(1).strip()
        st = re.search(r"\[status:\s*([a-z-]+)\]", heading, re.IGNORECASE)
        file_marker = st.group(1).lower() if st else "NONE"
        ids = by_k1.get(normalize(heading)) or by_k2.get(normalize(heading, drop_tags=True))
        if not ids or len(ids) != 1 or not props.get(ids[0]):
            unmatched_rows.append((i, heading, file_marker))
            if unmatched == "pending" and file_marker == "NONE":
                edits.append((i, line, line.rstrip() + f" [status: {FILE_ONLY_STATUS}]",
                              file_marker, FILE_ONLY_STATUS, ""))
            continue
        status = governing_proposal(props[ids[0]])["status"]
        if STATUS_RE.search(line):
            new = STATUS_RE.sub(f" [status: {status}]", line, count=1)
        else:
            new = line.rstrip() + f" [status: {status}]"
        if new != line:
            edits.append((i, line, new, file_marker, status, ids[0]))
    return edits, unmatched_rows


def prove_inert(before_path: str, after_text: str) -> list[str]:
    """Return a list of proof failures (empty = the edit is mechanically inert)."""
    fails = []
    fd, tmp = tempfile.mkstemp(prefix="LESSONS-after-", suffix=".md")
    os.close(fd)
    try:
        Path(tmp).write_text(after_text, encoding="utf-8")
        b = parse_lessons_md(before_path)
        a = parse_lessons_md(tmp)
    finally:
        os.unlink(tmp)
    if len(a) != len(b):
        fails.append(f"entry count moved: {len(b)} -> {len(a)}")
    kb = [_key_heading(e["source_heading"]) for e in b]
    ka = [_key_heading(e["source_heading"]) for e in a]
    moved = sum(1 for x, y in zip(kb, ka) if x != y)
    if moved:
        fails.append(f"{moved} entry keys moved")
    hb = [e["content_hash"] for e in b]
    ha = [e["content_hash"] for e in a]
    moved = sum(1 for x, y in zip(hb, ha) if x != y)
    if moved:
        fails.append(f"{moved} content_hashes moved")
    bl = [l for l in Path(before_path).read_text(encoding="utf-8").split("\n") if not l.startswith("## ")]
    al = [l for l in after_text.split("\n") if not l.startswith("## ")]
    if bl != al:
        fails.append("non-heading lines differ")
    return fails


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--db", help="path to the live lessons-forge.db")
    src.add_argument("--snapshot", help="path to a corpus .sql dump (unistr-encoded is fine)")
    ap.add_argument("--lessons", help="path to LESSONS.md (default: $ELUVIAN_WRAP_ROOT/LESSONS.md or <repo>/../LESSONS.md)")
    ap.add_argument("--apply", action="store_true", help="write the file (default: dry run)")
    ap.add_argument("--mapping", help="write the per-heading transition TSV here")
    ap.add_argument("--unmatched", choices=["leave", "pending"], default="leave",
                    help="what to do with headings that have no DB row (default: leave)")
    args = ap.parse_args(argv)

    lessons = Path(args.lessons) if args.lessons else discover_lessons()
    if lessons is None or not lessons.is_file():
        print(f"no LESSONS.md: {args.lessons or '(no --lessons; set ELUVIAN_WRAP_ROOT or run from the shop layout)'}",
              file=sys.stderr)
        return 3
    if args.snapshot:
        db_path = load_snapshot(args.snapshot)
    else:
        db_path = Path(args.db) if args.db else discover_db()
        if db_path is None:
            print("no live DB found (tried $LESSONS_FORGE_DB, " + ", ".join(str(c) for c in DB_CANDIDATES)
                  + "); pass --db or --snapshot", file=sys.stderr)
            return 3
        if not db_path.is_file() or os.path.getsize(db_path) == 0:
            print(f"--db {db_path} is missing or 0 bytes (a decoy, not a database)", file=sys.stderr)
            return 3
    print(f"DB: {db_path}\nLESSONS: {lessons}")
    con = sqlite3.connect(f"file:{os.path.realpath(db_path)}?mode=ro", uri=True)

    text = lessons.read_text(encoding="utf-8")
    lines = text.split("\n")
    edits, unmatched_rows = plan_edits(lines, con, args.unmatched)
    con.close()

    transitions = collections.Counter((e[3], e[4]) for e in edits)
    print(f"headings: {sum(1 for l in lines if HEADING_RE.match(l))}  "
          f"edits: {len(edits)}  unmatched (no DB row): {len(unmatched_rows)}")
    for (a, b), n in sorted(transitions.items(), key=lambda x: -x[1]):
        print(f"  {n:4d}  {a:9s} -> {b}")

    new_lines = list(lines)
    for i, _old, new, *_ in edits:
        new_lines[i] = new
    after_text = "\n".join(new_lines)

    if args.mapping:
        with open(args.mapping, "w", encoding="utf-8") as o:
            o.write("line\tentry_id\tfile_marker\tdb_status\told\tnew\n")
            for i, old, new, fm, st, eid in edits:
                o.write(f"{i + 1}\t{eid}\t{fm}\t{st}\t{old}\t{new}\n")

    if not edits:
        print("nothing to do")
        return 0
    fails = prove_inert(str(lessons), after_text)
    if fails:
        print("REFUSED — proofs failed: " + "; ".join(fails), file=sys.stderr)
        return 2
    print("proofs: entry count, keys, content_hashes and non-heading lines all unchanged")
    if args.apply:
        lessons.write_text(after_text, encoding="utf-8")
        print(f"APPLIED {len(edits)} heading edits to {lessons}")
    else:
        print("DRY RUN — nothing written (pass --apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
