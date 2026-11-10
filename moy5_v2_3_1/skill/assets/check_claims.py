"""check_claims.py — the FOURTH route of every number, and the coverage of the claims (template). Reads claims_anchors.json (an anchor = a file, a key and an expected value) and looks at the place itself:
  json_equals          the value at `key` (dotted path; list indices are numbers: rows.A.ranks.3.2) of a JSON file equals `expect`
  json_len             the length of the list / dict at `key` equals `expect`
  derived              a number RECOUNTED from scratch here (DERIVED[name](raw, *args)) equals `expect`  — not through build.mjs and not through the page's own JS
  pack_equals_derived  the number the page carries (generated/pack.json at `key`) equals the recount
  text_contains        a literal string occurs in a text file (e.g. a sentence the card's RESULT keeps beside its number)
Coverage: every anchor id must appear in CLAIMS.md and every id in CLAIMS.md's tables must have an anchor (a claim without a place to look at is not a claim).
It proves that the quoted words and values are there and that the counted numbers are the card's, not that the figure's sentence is a fair reading of them (that is the L3 half, for the reader).
    python3 -I check_claims.py          (exit 1 if anything is missing or differs)
"""
import json
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
RAW = HERE / "data" / "synthetic_readout.json"


def derived_key_rank(raw, row):
    """the band median of the clipped ranks at the key position of `row`, counted from the raw ranks"""
    lo, hi = raw["constants"]["band"]
    clip = raw["constants"]["clip"]
    r = raw["rows"][row]
    col = r["ranks"][r["key_pos"]]
    return statistics.median(min(v, clip + 1) for v in col[lo : hi + 1])


DERIVED = {"key_rank": derived_key_rank}      # add one function per number the page prints: the recount lives HERE, written separately from build.mjs / data.mjs


def get(obj, key):
    for part in key.split("."):
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def load(path):
    p = HERE / path
    return json.loads(p.read_text(encoding="utf-8")) if p.suffix == ".json" else p.read_text(encoding="utf-8")


raw = json.loads(RAW.read_text(encoding="utf-8"))
anchors = json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8"))
count, missing = 0, []
for a in anchors:
    count += 1
    try:
        k = a["kind"]
        if k == "json_equals":
            ok = get(load(a["file"]), a["key"]) == a["expect"]
        elif k == "json_len":
            ok = len(get(load(a["file"]), a["key"])) == a["expect"]
        elif k == "derived":
            ok = DERIVED[a["name"]](raw, *a.get("args", [])) == a["expect"]
        elif k == "pack_equals_derived":
            ok = get(load(a["file"]), a["key"]) == DERIVED[a["name"]](raw, *a.get("args", []))
        elif k == "text_contains":
            ok = a["literal"] in (HERE / a["file"]).read_text(encoding="utf-8")      # the file as TEXT, even if it is JSON
        else:
            raise ValueError("unknown kind " + k)
    except Exception as e:      # a missing file / key is a missing anchor, not a crash
        ok = False
        a = {**a, "error": repr(e)}
    if not ok:
        missing.append((a["id"], a.get("file", a.get("name")), a.get("key", a.get("literal", "")), a.get("expect"), a.get("error", "differs")))

# coverage: CLAIMS.md <-> anchors
ids = {a["id"] for a in anchors}
claims = (HERE / "CLAIMS.md").read_text(encoding="utf-8") if (HERE / "CLAIMS.md").exists() else ""
rows = set(re.findall(r"^\|\s*(K\d+)\s*\|", claims, re.M))
for i in sorted(ids - rows):
    missing.append((i, "CLAIMS.md", "an anchor without a claim row", None, "not in CLAIMS.md"))
for i in sorted(rows - ids):
    missing.append((i, "claims_anchors.json", "a claim row without an anchor", None, "no anchor"))
count += len(ids ^ rows)
print(f"anchors checked: {count} · missing or different: {len(missing)}")
for m in missing:
    print("  MISSING", m)
sys.exit(1 if missing else 0)
