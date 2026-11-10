"""compare_v22.py — BRIEF v2.3 §2-3: the cutting plane changes no other page. Reads two dumps of check_v23_dump.json (drive's stdout: lines 'dump23 {...}') — one of a v2.2 build, one of this build —
for the same page and frame, and compares per state: the page's text, the figure's svg and the key lines (hashes). Expected: equal everywhere EXCEPT the board states 0 and 7 with the overlay on
(the plane is drawn and its key line added there); and on those two, the page's text differs from v2.2 only by the key line (checked: text equal once the key line is removed is not possible from hashes,
so the key hash must differ and the overlay-off dumps must be equal).
    python -I compare_v22.py <dump of v2.2> <dump of v2.3> <label>      (exit 1 on any unexpected difference)
"""
import json
import sys

def load(f):
    out = {}
    for line in open(f, encoding="utf-8"):
        i = line.find("dump23 ")
        if i < 0:
            continue
        s = line[i + 7:].rstrip().rstrip('"').replace('\\"', '"')
        d = json.loads(s)
        out[(d["state"], d["tag"])] = d
    return out

a, b, label = load(sys.argv[1]), load(sys.argv[2]), sys.argv[3]
assert a and set(a) == set(b), (label, len(a), len(b))
same, diff, bad = 0, [], []
for k in sorted(a):
    d = [f for f in ("text", "svg", "keys") if a[k][f] != b[k][f]]
    expected = k in ((0, "on"), (7, "on"))
    if d:
        diff.append((k, d))
    else:
        same += 1
    if expected and d != ["text", "svg", "keys"]:
        bad.append((k, "expected the plane (svg) and its key line (text, keys) to differ", d))
    if not expected and d:
        bad.append((k, "changed", d))
print(f"compare_v22 {label}: {len(a)} dumps · equal {same} · differ {len(diff)} {[f'{s}/{t}' for (s, t), _ in diff]} · unexpected {len(bad)}")
for x in bad:
    print("  UNEXPECTED", x)
sys.exit(1 if bad else 0)
