import re, sys
EXPECTED = 4
BULLET_RE = re.compile(r"^(?:-\s|\d+\.\s)")          # verbatim, bellows.py:1409
doc = open(sys.argv[1], encoding="utf-8").read()
lu = re.search(r"### Ledger Updates\s*\n(.*?)(?=\n## |\Z)", doc, re.DOTALL)
lu_body = lu.group(1) if lu else ""
fw = re.search(r"#### (?:Forward Register|FORWARD(?: Additions)?)\s*\n(.*?)"
               r"(?=\n#### |\n### |\n## |\n\s*\n|\Z)", lu_body, re.DOTALL)
fw_text = (fw.group(1).strip() if fw else "")
lines   = [l for l in fw_text.splitlines() if l.strip()]
bullets = [l for l in lines if BULLET_RE.match(l.strip())]
rows    = ([" ".join(b.split()) for b in bullets] if len(bullets) >= 2
           else ([" ".join(lines[0].split())] if lines else []))
wrap_ok = len(lines) == len(bullets)
print(f"FILE={sys.argv[1]}")
print(f"LU={bool(lu)} FW={bool(fw)} NONBLANK={len(lines)} BULLETS={len(bullets)} DAEMON-ROWS={len(rows)}")
print(f"WRAP-CHECK={'PASS' if wrap_ok else 'FAIL - non-bullet line inside block WILL BE DROPPED'}")
for r in rows: print("   ROW:", r)
sys.exit(0 if (len(rows) == EXPECTED and wrap_ok) else 1)
