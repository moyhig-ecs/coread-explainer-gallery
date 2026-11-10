#!/usr/bin/env python3
"""make_manifest.py — MANIFEST.md of this bundle (path, bytes, md5 of every file) — generated, never hand-written.

    python3 -I make_manifest.py            write MANIFEST.md
    python3 -I make_manifest.py --verify   recompute and compare with MANIFEST.md (exit 1 on any difference)
"""
import datetime
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "MANIFEST.md"
SKIP = {".DS_Store"}


def listing():
    rows = []
    for p in sorted(HERE.rglob("*")):
        if not p.is_file() or p.name in SKIP or p == OUT or ".chrome" in p.parts or "__pycache__" in p.parts:
            continue
        b = p.read_bytes()
        rows.append((str(p.relative_to(HERE)), len(b), hashlib.md5(b).hexdigest()))
    return rows


def render(rows):
    total = sum(r[1] for r in rows)
    head = [f"# MANIFEST — {HERE.name}", "",
            f"- generated {datetime.datetime.now().isoformat(timespec='seconds')} by `make_manifest.py` ({len(rows)} files, {total:,} bytes = {total / 1e6:.1f} MB)",
            "- verify: `python3 -I make_manifest.py --verify`", "", "| path | bytes | md5 |", "|---|---:|---|"]
    return "\n".join(head + [f"| `{r[0]}` | {r[1]} | `{r[2]}` |" for r in rows]) + "\n"


def parse(text):
    rows = {}
    for line in text.splitlines():
        if line.startswith("| `") and line.count("|") == 4:
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows[cells[0].strip("`")] = (int(cells[1]), cells[2].strip("`"))
    return rows


def main():
    rows = listing()
    if "--verify" in sys.argv:
        want = parse(OUT.read_text(encoding="utf-8"))
        have = {r[0]: (r[1], r[2]) for r in rows}
        missing = sorted(set(want) - set(have)); extra = sorted(set(have) - set(want))
        changed = sorted(k for k in want if k in have and want[k] != have[k])
        print(f"manifest {len(want)} files; on disk {len(have)}; missing {len(missing)}; extra {len(extra)}; changed {len(changed)}")
        for k in missing: print("  missing", k)
        for k in extra: print("  extra  ", k)
        for k in changed: print("  changed", k, want[k], "->", have[k])
        return 0 if not (missing or extra or changed) else 1
    OUT.write_text(render(rows), encoding="utf-8")
    print(f"wrote {OUT.name}: {len(rows)} files, {sum(r[1] for r in rows):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
