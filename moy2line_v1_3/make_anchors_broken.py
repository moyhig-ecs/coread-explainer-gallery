"""make_anchors_broken.py — the positive control of check_claims.py: a copy of claims_anchors.json with TWELVE anchors broken on purpose
(v1: K09 a rate · K33 a PREREG literal · K71 the apex; v1.1: K78 the four arms back to the old 43 / 47 (F1) · K91 one Fisher p (F4) · K97 the named rows of olm127 (F5) · K101 the olm126 Q3 row (F7); v1.2: K108 Fisher with none below 0.05 (G7) · K111 olm124 with olm125's edges (G8)).
check_claims.py --anchors checks/anchors_broken.json must report exactly these twelve (v1.3: + K120 · K123 · K126; run_checks.sh asserts it).
    python3 -I make_anchors_broken.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
A = json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8"))
BREAK = {"K09": ("expect", "9 / 40 = 0.226"), "K33": ("literal", "**戻る** \\|Δ113\\| < 0.05・**残る** \\|Δ119\\| < 0.05"), "K71": ("expect", [3.8421, 3.8429]),
         "K78": ("expect", [43, 47]), "K91": ("expect", [0.2284, 0.1062, 0.4631, 1.0, 0.124, 0.0142, 0.4721]), "K97": ("literal", "apex に数値で着く(b0_j00・b2_j08)か"),
         "K101": ("literal", "| Q3 REJ6 の回帰 | b0_j06 落ちた ✓・olm125 の残り 13 / 13 残った ✓・**olm124 の 12 本のうち b2_j03 が残った ✓**"),
         "K108": ("expect", [7, 0]), "K111": ("expect", [0.048, 0.168, 0.258, 0.378]),
         "K120": ("literal", "共線を行列式 = 0 / 媒介変数の一致で数値で退けた直後に"), "K123": ("expect", [6, 6, 0, 0]), "K126": ("expect", ["abcd", True, True])}   # v1.3: H1 the source literal · H2 all six at the cap · H5 the mechanism inside RECORD §6   # v1.2: G7 "none below 0.05" · G8 olm124 given olm125's edges
out = [{**a, BREAK[a["id"]][0]: BREAK[a["id"]][1]} if a["id"] in BREAK else a for a in A]
assert sum(1 for x, y in zip(A, out) if x != y) == len(BREAK)
(HERE / "checks" / "anchors_broken.json").write_text("[\n" + ",\n".join(" " + json.dumps(a, ensure_ascii=False) for a in out) + "\n]\n", encoding="utf-8")
print(f"checks/anchors_broken.json: {len(out)} anchors, {len(BREAK)} broken: {' · '.join(BREAK)}")
