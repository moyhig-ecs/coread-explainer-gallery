"""pack_data.py — the FIRST route of every number (template).
Reads the frozen card output (data/synthetic_readout.json; replace with your card's JSON), asserts what the figure relies on, and writes generated/pack.json:
the numbers the page needs (here: the band median of the ranks at every position, and the rank at the key position of each row).
Never import or run the experiment's own script: only read the card's output file. A value that disagrees with a brief is recorded and the data wins.
    python3 -I pack_data.py
"""
import hashlib
import json
import pathlib
import statistics

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "data" / "synthetic_readout.json"
OUT = HERE / "generated"
OUT.mkdir(exist_ok=True)

raw = json.loads(SRC.read_text(encoding="utf-8"))
# ---- what must hold before anything is drawn (the card's own guarantees)
assert raw["stage"] == "synthetic_card" and raw["forward"] == 0, "the card is a replay (forward 0)"
assert raw["provenance"]["dirty"] is False, "a card run from a dirty tree is not frozen"
assert all(c["pass"] for c in raw["controls"].values()), "a failed control stops the build: the figure's data is not written"
CL = raw["constants"]["clip"]                       # ranks above this are clipped (1001 = "below the 1000th"); drawn as fog, never as "sunk"
lo, hi = raw["constants"]["band"]                  # the record band (layers lo..hi)

def band_median(col):
    """median of the clipped ranks over the band. Order matters: clip first, then median (say so in the card's text; if an even count makes the order matter, disclose it)."""
    vals = [min(v, CL + 1) for v in col[lo : hi + 1]]
    return statistics.median(vals)

rows = {}
for key, r in raw["rows"].items():
    assert len(r["ranks"]) == raw["constants"]["positions"] and all(len(c) == raw["constants"]["layers"] for c in r["ranks"]), key
    assert all(1 <= v <= CL + 1 for c in r["ranks"] for v in c), key
    bm = [band_median(c) for c in r["ranks"]]
    rows[key] = {"label": r["label"], "keyPos": r["key_pos"], "keyWord": r["key_word"], "ranks": r["ranks"], "bandMedian": bm, "keyRank": bm[r["key_pos"]]}
pack = {"stage": raw["stage"], "provenance": raw["provenance"], "md5": hashlib.md5(SRC.read_bytes()).hexdigest(), "forward": raw["forward"], "controls": raw["controls"],
        "band": [lo, hi], "clip": CL, "positions": raw["constants"]["positions"], "layers": raw["constants"]["layers"], "rows": rows, "statements": raw["statements"]}
(OUT / "pack.json").write_text(json.dumps(pack, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"pack: {len(rows)} rows · key ranks {{{', '.join(f'{k}: {v['keyRank']:g}' for k, v in rows.items())}}} · md5 {pack['md5'][:8]}")
