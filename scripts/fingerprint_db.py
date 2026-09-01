import sqlite3, hashlib, sys
p=sys.argv[1]; con=sqlite3.connect(f"file:{p}?mode=ro", uri=True)
h=hashlib.sha256()
for t in ("lesson_entries","lesson_proposals"):
    cols=[r[1] for r in con.execute(f"pragma table_info({t})")]
    for row in con.execute(f"select {','.join(cols)} from {t} order by id"):
        h.update(repr(tuple(row)).encode()); h.update(b"\n")
    n,mx=con.execute(f"select count(*),max(id) from {t}").fetchone(); print(f"{t}: rows={n} max_id={mx} cols={len(cols)}")
print("schema objects:", con.execute("select count(*) from sqlite_master").fetchone()[0])
print("integrity:", con.execute("pragma integrity_check").fetchone()[0])
print("fingerprint:", h.hexdigest())
