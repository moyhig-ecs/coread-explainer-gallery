"""pack_after.py — v3: the FIRST route of every number of the part that was added after the 10-28 figure (the cards the home struck after it: olm76 ... olm128).

Run by pack_moy1.py (runpy), never on its own. Only reads: the cards' read.json / control.json (frozen outputs), the RESULT files (as text: the frozen commit and the grade the card's own words give),
and `git log` of each PREREG (a read: the commit that first added the file = the freeze). No experiment script is opened, imported or run; no model, no network.
Every value that the figure prints is copied from a read.json key (never from a RESULT's summary line); the RESULT / SCOPE lines are used only as CHECK values (asserted, then dropped).
Returns AFTER (a dict) for the pack.
"""
import glob
import json
import os
import re
import subprocess
from pathlib import Path

REPO = Path(os.environ.get("MOY1_REPO", Path(__file__).resolve().parent / "data"))   # bundle: the frozen files are copied under data/ at their repo paths
def _git_fact(args):   # bundle: the `git log` answers recorded from the house repo (data/git_facts.json) when REPO is not a git checkout
    if (REPO / ".git").exists():
        import subprocess as _sp
        return _sp.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True).stdout
    _f = json.loads((Path(__file__).resolve().parent / "data" / "git_facts.json").read_text(encoding="utf-8"))
    return _f["answers"][json.dumps(list(args), separators=(",", ":"), ensure_ascii=False)]
HERE = Path(__file__).resolve().parent


def J(rel):
    return json.loads((REPO / rel).read_text(encoding="utf-8"))


def git_first_add(rel):
    """the short hash of the commit that first added the file (oldest 'A') — the freeze commit of a PREREG"""
    out = _git_fact(["log", "--diff-filter=A", "--format=%h", "--", rel]).split()
    return out[-1] if out else ""


def result_path(card):
    hits = sorted(glob.glob(str(REPO / f"conversations/*/RESULT_{card}_moy1_*.md")))
    assert len(hits) == 1, (card, hits)
    return str(Path(hits[0]).relative_to(REPO))


# the grade each card takes, in the card's own words (RESULT) and the SCOPE of 11-01 where it is listed there. 'grade' is one of: 判定 · 確かめた記述 · 記述 · 較正 · 読まない(関門 ✗)
# (a card can hold claims of two grades; `grade` is the one the figure puts on its tile, `grade_note` says where the other sits)
CARDS = [
    # id, station, grade, where the grade comes from
    ("olm76", 1, "記述", "SCOPE 11-01 §2 記述(olm76 Q1 ✗・Q3 ✗)・§2 言えない(「結び」が答えの欄の手前で立つ)"),
    ("olm84", 2, "記述", "SCOPE 11-01 §2 記述(olm84 Q1 ✗)"),
    ("olm85", 2, "記述", "SCOPE 11-01 §2 記述(olm85 Q1 ✗)"),
    ("olm86", 2, "記述", "SCOPE 11-01 §2 記述(olm86 Q1 ✗・k = 8 は見てから気づいた)"),
    ("olm89", 2, "確かめた記述", "SCOPE 11-01 §2 確かめた記述(olm89 Q1 ✓・線 +0.05 の Q1b ✗)"),
    ("olm91", 2, "記述", "SCOPE 11-01 §2 記述(olm91 Q1 ✗)"),
    ("olm92", 2, "確かめた記述", "SCOPE 11-01 §2 確かめた記述(olm92 Q1 の枝「残る」・層 32 だけ)"),
    ("olm93", 3, "記述", "SCOPE 11-01 §2b 記述(olm93 Q1・L3 偽)・較正(C_lab)"),
    ("olm94", 3, "判定", "SCOPE 11-01 §2b 判定(olm94 Q2 ✓)・記述(Q0・Q1・Q3)"),
    ("olm95", 3, "読まない(関門 ✗)", "SCOPE 11-01 §2b 較正(olm95 C2 ✗ = 読まなかった)"),
    ("olm97", 3, "記述", "SCOPE 11-01 §2b 記述(olm97 Q1 偽・Q2)・較正(C2 0.971)"),
    ("olm98", 3, "判定", "SCOPE 11-01 §2b 判定(olm98 Q1 ✓・Q2 ✓)・記述(Q4・Q5)"),
    ("olm101", 3, "記述", "RESULT olm101 「動かした主張」= 0 個(Q1 偽・Q2 片方なし・Q3 間 = 錯覚の印)・SCOPE 11-01 には載っていない"),
    ("olm106", 3, "記述", "RESULT olm106 「動かした主張」= 0 個(Q1 遅い・Q2 無い・Q3 無い)・SCOPE 11-01 には載っていない"),
    ("olm108", 3, "判定", "RESULT olm108 「動かした主張」= 2 つ(Q1 ✓・Q3 在る)・SCOPE 11-01 には載っていない"),
    ("olm112", 4, "判定", "RESULT olm112 §2 判定(凍結の帯: Q1 偽・Q2 追わない・Q3 変わらない)・SCOPE には載っていない"),
    ("olm114", 4, "判定", "RESULT olm114 §2 判定(Q1 続ける・Q2 続ける・Q3 読まない = 関門 ✗)・(B) forward は記述・SCOPE には載っていない"),
    ("olm128", 5, "判定", "RESULT olm128 §2 判定(凍結の帯: Q1 保たれない・Q2 動く / 逆・Q3 書き始めでは説明されない)・§3 は事後の記述(判定でない)"),
]
READ = {c: f"ConstructGap/exp/{c}/read.json" for c, *_ in CARDS}
READ_PROV = {"olm76": "prov", "olm84": "prov", "olm85": "prov", "olm86": "prov", "olm89": "prov", "olm91": "prov", "olm92": "prov", "olm93": "prov", "olm94": "prov", "olm98": "prov", "olm101": "prov", "olm106": "prov", "olm108": "prov",
             "olm112": "provenance", "olm114": "provenance"}

cards = []
for cid, station, grade, why in CARDS:
    rp = result_path(cid)
    head = "\n".join((REPO / rp).read_text(encoding="utf-8").splitlines()[:9])
    m = re.search(r"\[PREREG\]\(([^)]+)\)\((?:凍結 )?`?([0-9a-f]{8})", head)
    assert m, (cid, "no [PREREG](...)(hash) in the RESULT's header")
    prereg_rel = str((Path(rp).parent / m.group(1)).as_posix())
    prereg_rel = os.path.normpath(prereg_rel)
    freeze = m.group(2)
    first = git_first_add(prereg_rel)
    assert first and freeze.startswith(first[:7]), (cid, "the RESULT's freeze commit", freeze, "is not git's first commit of the PREREG", first)
    date = re.search(r"_(\d{8})\.md$", rp).group(1)
    c = {"id": cid, "station": station, "grade": grade, "grade_from": why, "date": f"{date[4:6]}-{date[6:8]}", "freeze": freeze, "result": rp, "prereg": prereg_rel, "read": READ[cid] if (REPO / READ[cid]).exists() else None}
    if c["read"]:
        d = J(c["read"])
        c["read_commit"] = (d.get(READ_PROV.get(cid, "prov")) or {}).get("commit")
    cards.append(c)
# where each card's numbers sit: the file (read.json unless said) and the top-level keys of it that the figure reads (each key is asserted to exist)
SRC_KEYS = {
    "olm76": ("read.json", ["Q1_bind_close_rises", "Q3_close_bind_gt_attractor", "desc_all_keys"]), "olm84": ("read.json", ["Q1"]), "olm85": ("read.json", ["Q1_next_sentence_O"]), "olm86": ("read.json", ["Q1_k32", "Q2_desc_by_k"]),
    "olm89": ("read.json", ["Q1_k8", "Q2_desc_by_k"]), "olm91": ("read.json", ["Q1_first64"]), "olm92": ("read.json", ["Q_k8", "Q3_desc_by_k"]), "olm93": ("read.json", ["Q1_name_to_dem"]),
    "olm94": ("read.json", ["Q2_V_post_to_dem_vs_ctl", "Q0_behaviour"]), "olm95": ("control.json", ["C2_direction_separates_test_dem"]), "olm97": ("read.json", ["Q1_dem_direction_swap_L32", "Q2_full_interchange"]),
    "olm98": ("read.json", ["Q1_top_heads_read_ref_name", "Q2_patch_top_heads", "Q4_cmt13_overlap"]), "olm101": ("read.json", ["Q1_curve_full_end", "Q2", "Q3"]), "olm106": ("read.json", ["table", "Q1", "branches"]),
    "olm108": ("read.json", ["Q1", "Q3", "branches"]), "olm112": ("read.json", ["Q1", "Q2", "Q3", "Q4_by_label_json"]), "olm114": ("read.json", ["Q1", "Q2", "Q3", "Q4_profiles"]), "olm128": ("read.json", ["blocked_cells", "verdicts"]),
}
for _c in cards:
    _f, _ks = SRC_KEYS[_c["id"]]
    _d = J(f"ConstructGap/exp/{_c['id']}/{_f}")
    assert all(k in _d for k in _ks), (_c["id"], _f, [k for k in _ks if k not in _d])
    _c["src_file"], _c["src_keys"] = f"ConstructGap/exp/{_c['id']}/{_f}", _ks
CARD = {c["id"]: c for c in cards}
assert CARD["olm76"]["freeze"] == "b7730f55" and CARD["olm101"]["freeze"] == "9fbbc072" and CARD["olm112"]["freeze"] == "cb12da8d" and CARD["olm114"]["freeze"] == "c82642a5" and CARD["olm128"]["freeze"] == "2f1ab745"
assert CARD["olm76"]["read_commit"] == "d7fbbd43"          # olm76 was frozen again at d7fbbd43 (a change of the output's conversion only, before any value was read: RESULT olm76 line 5)
STATIONS = [
    {"id": "S0", "cards": [], "date": "10-28"},
    {"id": "S1", "cards": ["olm76"], "date": "10-30"},
    {"id": "S2", "cards": ["olm84", "olm85", "olm86", "olm89", "olm91", "olm92"], "date": "10-31 – 11-01"},
    {"id": "S3", "cards": ["olm93", "olm94", "olm95", "olm97", "olm98", "olm101", "olm106", "olm108"], "date": "11-01"},
    {"id": "S4", "cards": ["olm112", "olm114"], "date": "11-02"},      # v3.1: the date of a card = the record's name (olm114's file is 20261102); the station takes its cards' dates
    {"id": "S5", "cards": ["olm128"], "date": "11-06"},
]
assert sorted(c for s in STATIONS for c in s["cards"]) == sorted(CARD) and all(CARD[c]["station"] == int(s["id"][1]) for s in STATIONS for c in s["cards"])


def med(x):          # a probe's AUC summary {n, median, p05, p95} -> the three numbers
    return {"med": x["median"], "p05": x["p05"], "p95": x["p95"]}


def auc_block(q):
    return {"auc": {k: med(q["auc"][k]) for k in ("L32", "L48", "J", "W")}, "E": {k: med(q["E"][k]) for k in ("L32", "L48")}, "n_pos": q.get("n_pos"), "n_neg": q.get("n_neg"), "pass": bool(q.get("pass", q.get("Q1_repl_pass", False)))}


# ---------------------------------------------------------------------------------------------------- (a) the L3 of the 10-28 ledger -> olm76
O76, C76 = J(READ["olm76"]), J("ConstructGap/exp/olm76/control.json")
L3 = {
    "q1": {k: O76["Q1_bind_close_rises"][k] for k in ("n", "pos", "median", "sign_p", "pass")},
    "q3": {k: O76["Q3_close_bind_gt_attractor"][k] for k in ("n_a", "n_b", "median_a", "median_b", "diff", "perm_p", "loo_pos", "loo_n", "pass")},
    "pseudo": {k: C76["C2_pseudo_window"]["sae_close"][k] for k in ("n", "pos", "median", "sign_p")},
    "attr": {k: O76["desc_all_keys"]["sae_close|attractor"][k] for k in ("n", "pos", "median")},
    "commit_c3": {k: C76["C3_commit_positive"][k] for k in ("n", "pos", "frac", "ok")},
    "by_kind": O76["desc_by_kind"], "counts": O76["counts"], "control_pass": O76["control_pass"],
}
assert (L3["q1"]["n"], L3["q1"]["pos"], L3["q1"]["pass"]) == (48, 28, False) and round(L3["q1"]["median"], 4) == 0.0127 and round(L3["q1"]["sign_p"], 3) == 0.156          # RESULT olm76 / SCOPE 11-01 §2: 28 / 48 · +0.013 · p 0.156
assert (L3["pseudo"]["n"], L3["pseudo"]["pos"]) == (48, 21) and round(L3["pseudo"]["sign_p"], 3) == 0.844 and (L3["attr"]["n"], L3["attr"]["pos"]) == (10, 7) and L3["commit_c3"]["ok"] is False

# ---------------------------------------------------------------------------------------------------- (b) the inference-space search: what a probe on the residual reads beyond J-lens and a bag of words
O84, O85, O86, O89, O91, O92 = (J(READ[c]) for c in ("olm84", "olm85", "olm86", "olm89", "olm91", "olm92"))
LOOK = [
    {"card": "olm84", "ev": "O の名を書く", "k": 3, **auc_block(O84["Q1"])},
    {"card": "olm85", "ev": "文の切れ目の次の文が O の名を名指す", "k": 12, **auc_block(O85["Q1_next_sentence_O"])},      # k = the median distance (tokens) of the name from the cut: SCOPE 11-01 §2 (12) — carried as the card's own description, not a measured field here
    {"card": "olm86", "ev": "O の名を新しく名指す", "k": 32, **auc_block(O86["Q1_k32"])},
]
def null_band(card):                      # the card's own null (control.json C3: false positives / pseudo / permutation) for the layer-32 probe: its 5 % .. 95 % AUC
    d = J(f"ConstructGap/exp/{card}/control.json")
    k = next(k for k in d if k.startswith("C3"))
    return {"key": k, "p05": d[k]["auc"]["L32"]["p05"], "med": d[k]["auc"]["L32"]["median"], "p95": d[k]["auc"]["L32"]["p95"]}


for x in LOOK:
    x["null"] = null_band(x["card"])
assert [round(x["null"]["p05"], 3) for x in LOOK] == [0.418, 0.519, 0.451]
assert [round(x["auc"]["L32"]["med"], 3) for x in LOOK] == [0.996, 0.878, 0.777] and [round(x["auc"]["J"]["med"], 3) for x in LOOK] == [0.994, 0.879, 0.775] and [round(x["E"]["L32"]["med"], 3) for x in LOOK] == [0.002, -0.002, 0.002]
assert all(x["pass"] is False for x in LOOK)                                                                                                 # Q1 ✗ in all three (the card's own flag)
K = {"1": None, "8": None, "16": None, "32": None}
KTAB = {
    "olm86": {"1": O86["Q2_desc_by_k"]["1"]["E"], "8": O86["Q2_desc_by_k"]["8"]["E"], "16": O86["Q2_desc_by_k"]["16"]["E"], "32": O86["Q1_k32"]["E"]},
    "olm89": {"1": O89["Q2_desc_by_k"]["1"]["E"], "8": O89["Q1_k8"]["E"], "16": O89["Q2_desc_by_k"]["16"]["E"], "32": O89["Q2_desc_by_k"]["32"]["E"]},
    "olm92": {"1": O92["Q3_desc_by_k"]["1"]["E_old"], "8": O92["Q_k8"]["E_old"], "16": O92["Q3_desc_by_k"]["16"]["E_old"], "32": O92["Q3_desc_by_k"]["32"]["E_old"]},
}
KTAB = {c: {k: {"L32": e["L32"]["median"], "L48": e["L48"]["median"]} for k, e in ks.items()} for c, ks in KTAB.items()}
assert [round(KTAB[c]["8"]["L32"], 3) for c in ("olm86", "olm89", "olm92")] == [0.036, 0.041, 0.022] and [round(KTAB[c]["32"]["L48"], 3) for c in ("olm86", "olm89", "olm92")] == [-0.006, 0.004, -0.008]
PLUS = {"L32": med(O92["Q_k8"]["E_plus"]["L32"]), "L48": med(O92["Q_k8"]["E_plus"]["L48"]), "branch": O92["Q_k8"]["Q1_branch"], "auc": {k: O92["Q_k8"]["auc"][k]["median"] for k in ("L32", "L48", "J", "W", "W3", "T", "Wp") if k in O92["Q_k8"]["auc"]}}
assert PLUS["branch"] == "残る" and round(PLUS["L32"]["med"], 3) == 0.022
E89 = {"L32": med(O89["Q1_k8"]["E"]["L32"]), "L48": med(O89["Q1_k8"]["E"]["L48"]), "repl": bool(O89["Q1_k8"]["Q1_repl_pass"]), "line": bool(O89["Q1_k8"]["Q1b_line_pass"])}
assert round(E89["L32"]["med"], 3) == 0.041 and E89["repl"] is True and E89["line"] is False
F64 = {**auc_block(O91["Q1_first64"]), "null": None, "rows": O91["Q1_first64"]["rows"], "attractor": O91["Q1_first64"]["attractor"]}
F64["null"] = null_band("olm91")
assert (F64["rows"], F64["attractor"]) == (217, 51) and [round(F64["auc"][k]["med"], 3) for k in ("L32", "L48", "J", "W")] == [0.492, 0.489, 0.527, 0.578]
SPACE = {"look": LOOK, "ktab": KTAB, "plus": PLUS, "e89": E89, "first64": F64, "line_candidate": 0.05, "line_false": 0.01}          # +0.05 / +0.01 = the thresholds the PREREGs froze (SCOPE 11-01 §0: E >= +0.05 with a 5 % point above 0 · false = E <= +0.01)

# ---------------------------------------------------------------------------------------------------- (c) structures that are not words: reference / head / interchange
O93, O94, O98 = J(READ["olm93"]), J(READ["olm94"]), J(READ["olm98"])
q2 = O94["Q2_V_post_to_dem_vs_ctl"]
REF = {
    "olm94_q2": {"to_dem": {k: q2["to_dem"][k]["median"] for k in ("L32", "L48", "J", "W")}, "to_ctl": {k: q2["to_ctl"][k]["median"] for k in ("L32", "L48", "J", "W")}, "diff": {k: q2["dem_minus_ctl"][k]["median"] for k in ("L32", "L48")}},
    "olm94_q0": O94["Q0_behaviour"], "olm94_q1_auc": {k: O94["Q1_V_dem_in_place"]["auc"][k]["median"] for k in ("L32", "L48", "J", "W")},
    "olm93_q1": {k: v["median"] for k, v in O93["Q1_name_to_dem"]["auc"].items()}, "olm93_q1_E": {k: v["median"] for k, v in O93["Q1_name_to_dem"]["E"].items()},
}
assert [round(REF["olm94_q2"]["to_dem"][k], 3) for k in ("L32", "L48", "J")] == [0.970, 0.766, 0.556] and [round(REF["olm94_q2"]["to_ctl"][k], 3) for k in ("L32", "L48")] == [0.603, 0.601] and round(REF["olm94_q2"]["diff"]["L32"], 3) == 0.366
assert round(REF["olm93_q1"]["L32"], 3) == 0.870 and round(REF["olm93_q1"]["L48"], 3) == 0.830 and REF["olm94_q0"]["V"]["n"] == 640 and round(REF["olm94_q0"]["V"]["acc"], 3) == 0.981 and set(REF["olm94_q1_auc"].values()) >= {1.0, 0.5}
HEADS = {
    "ratio": O98["Q1_top_heads_read_ref_name"]["ratio_median"], "diff": O98["Q1_top_heads_read_ref_name"]["diff_median"], "n": O98["Q1_top_heads_read_ref_name"]["n"], "share": O98["Q1_top_heads_read_ref_name"]["share_by_span_median"],
    "e_top": O98["Q2_patch_top_heads"]["e_top_median"], "top_minus_rand": O98["Q2_patch_top_heads"]["top_minus_rand_median"], "boot_lo": O98["Q2_patch_top_heads"]["top_minus_rand_boot_lo"], "flip": O98["Q2_patch_top_heads"]["flip_top"],
    "overlap": O98["Q4_cmt13_overlap"], "dem_head": O98["Q5_head_reading_dem_most"],
}
assert round(HEADS["ratio"], 2) == 2.37 and round(HEADS["e_top"], 2) == 2.19 and round(HEADS["flip"], 3) == 0.513 and len(HEADS["overlap"]) == 5 and HEADS["dem_head"]["head"] == "L13H30" and HEADS["dem_head"]["rank_by_dla"] == 312
O101, O106, O108 = J(READ["olm101"]), J(READ["olm106"]), J(READ["olm108"])
LAYERS = {
    "end": [{"L": r["L"], "po": r["F_po"], "vo": r["F_vo"], "both": r["F_both"]} for r in O101["Q1_curve_full_end"]],
    "sel": [{"L": L, "po": O106["table"][f"sel_L{L}"]["test・ptr_only"], "vo": O106["table"][f"sel_L{L}"]["test・val_only"], "both": O106["table"][f"sel_L{L}"]["test・both"]} for L in (-1, 0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 32)],
    "ctl_max": max(max(O106["table"][f"{n}_L{L}"][c] for c in ("test・ptr_only", "test・val_only", "test・both")) for n in ("ctl", "dem") for L in (-1, 0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 32)),
    "tail": [{"L": r[0], "po": r[1], "vo": r[2]} for r in O108["Q1"]["curve_tail"]],
    "tail_scatter": O108["Q3"]["scattered_layers"], "tail_switch": O108["Q1"]["L_switch_tail"], "sel_drop": O106["Q1"]["L_drop"], "end_val_first": O101["Q2"]["L_val_first"], "branches": {"olm101": [O101["Q1"]["branch"], O101["Q2"]["branch"], O101["Q3"]["branch"]], "olm106": [O106["branches"]["Q1"], O106["branches"]["Q2"], O106["branches"]["Q3"]], "olm108": [O108["branches"]["Q1"], O108["branches"]["Q2"], O108["branches"]["Q3"]]},
    "das": {"layer": O101["Q3"]["layer_by_dev"], "d_das": O101["Q3"]["D_das_test"], "d_full": O101["Q3"]["D_full_test"], "selectivity": O101["Q3"]["selectivity"]},
}
assert [r["L"] for r in LAYERS["end"]] == [8, 12, 16, 20, 24, 28, 32, 40, 48, 56] and LAYERS["sel_drop"] == 16 and LAYERS["tail_switch"] == 20 and LAYERS["tail_scatter"] == [16, 18] and LAYERS["end_val_first"] == 28
assert round(next(r for r in LAYERS["sel"] if r["L"] == 12)["po"], 3) == 0.929 and round(next(r for r in LAYERS["end"] if r["L"] == 24)["vo"], 3) == 0.381 and round(next(r for r in LAYERS["tail"] if r["L"] == 20)["vo"], 3) == 0.552 and LAYERS["ctl_max"] <= 0.01
STRUCT = {"ref": REF, "heads": HEADS, "layers": LAYERS}

# ---------------------------------------------------------------------------------------------------- (d) the apex proof: olm112 (frontier-free) and olm114 (the frontier's proof given in steps)
O112, O114 = J(READ["olm112"]), J(READ["olm114"])
b = O112["Q4_by_label_json"]
APEX = {
    "olm112": {"n": O112["n"], "gates": O112["gates"], "Q1": O112["Q1"], "Q2": O112["Q2"], "Q3": {k: O112["Q3"][k] for k in ("baseline_n", "baseline_attr", "new_attr", "baseline_rate", "new_rate", "diff", "verdict")},
               "label_json": O112["Q3"]["new_label_json"], "bind": {k: b["B-bind"][k] for k in ("n", "BIS", "ADJ", "RA", "THC", "CHAIN", "COORD", "ALT_radical", "ALT_homothety", "ALT_power", "proof_nonempty", "T_med")}, "attr": {k: b["B-attractor"][k] for k in ("n", "BIS", "RA", "THC", "CHAIN", "ALT_homothety")}},
    "olm114": {"n": O114["n"], "gates": O114["gates"], "Q1": {k: O114["Q1"][k] for k in ("k1_rows", "RA_and_THC", "rate", "verdict")}, "Q2": {k: O114["Q2"][k] for k in ("k2_rows", "THC", "rate", "verdict")},
               "Q3": {k: O114["Q3"][k] for k in ("k0_rows", "bind", "chain_in_bind", "bind_rate", "olm112_bind_rate", "hit_cap", "label_json", "verdict")},
               "fam": {"k1": {f: {k: O114["Q1"]["by_family"][f][k] for k in ("n", "RA_and_THC", "CHAIN", "BIS")} for f in ("opus", "fable")}, "k2": {f: {k: O114["Q2"]["by_family"][f][k] for k in ("n", "THC", "RA_and_THC")} for f in ("opus", "fable")}},
               "profile": {k: {x: O114["Q4_profiles"][k][x] for x in ("n", "BIS", "ADJ", "RA", "THC", "CHAIN", "RA_and_THC")} for k in ("k1", "k2")},
               "look": {nm: O114["B"]["lookahead"][nm]["frac_top5_by_k"] for nm in O114["B"]["lookahead"] if isinstance(O114["B"]["lookahead"][nm], dict) and "frac_top5_by_k" in O114["B"]["lookahead"][nm]}, "B_control": O114["B"]["control"]["pass"]}}
assert (APEX["olm112"]["Q1"]["bind"], APEX["olm112"]["Q1"]["chain"]) == (37, 0) and APEX["olm112"]["label_json"]["B-bind"] == 37 and APEX["olm112"]["bind"]["RA"] == 4 and APEX["olm112"]["bind"]["THC"] == 13
assert (APEX["olm114"]["Q1"]["RA_and_THC"], APEX["olm114"]["Q1"]["k1_rows"]) == (26, 40) and (APEX["olm114"]["Q2"]["THC"], APEX["olm114"]["Q2"]["k2_rows"]) == (23, 40) and (APEX["olm114"]["Q3"]["bind"], APEX["olm114"]["Q3"]["k0_rows"]) == (5, 40) and APEX["olm114"]["gates"]["G2_k0_none<=4"] is True
# v3.1 (D3 ⑥ = entry P #s30 · G-12): the chat model on the same sentence = another card (prf4), with its file and keys
_P4 = J("ConstructGap/exp/prf4/read.json")["units"]["claude-opus-5-5|M1A"]
APEX["prf4"] = {"model": "Opus 5.5 xhigh", "bind": _P4["bind"], "chain": _P4["chain_in_bind"], "file": "ConstructGap/exp/prf4/read.json", "key": "units[claude-opus-5-5|M1A].bind · .chain_in_bind"}
assert (APEX["prf4"]["bind"], APEX["prf4"]["chain"]) == (8, 8), APEX["prf4"]
assert APEX["olm114"]["fam"]["k1"]["opus"]["RA_and_THC"] == 12 and APEX["olm114"]["fam"]["k1"]["fable"]["RA_and_THC"] == 14 and APEX["olm114"]["fam"]["k2"]["opus"]["THC"] == 7 and APEX["olm114"]["fam"]["k2"]["fable"]["THC"] == 16
# olm114's Q3 gate (the RESULT's §1 reads "G2 (k = 0): label_none <= 4 AND answer-field B-bind >= 8": the second half is the RESULT's own description; read.json carries G2_k0_none only, and Q3's verdict is null = not read)
assert APEX["olm114"]["Q3"]["verdict"] is None and APEX["olm114"]["Q3"]["bind"] < 8

# verbatim excerpts (the base model's own words; every one is asserted to be the frozen text, the RESULT's cited rows)
G112, G114 = J("ConstructGap/exp/olm112/gen.json"), J("ConstructGap/exp/olm114/gen.json")


def row112(key):
    bi, jj = int(key[1:key.index("j")]), int(key[key.index("j") + 1:])
    r = next(x for x in G112["batches"][str(bi)]["rows"] if x["j"] == jj)
    return {"key": key, "label_json": r["label_json_fields"], "T": r["T_tokens"], "text": r["proof"], "len": r["pm"]["proof_len"]}


def row114(batch, pid):
    r = next(x for x in G114["batches"][batch]["rows"] if x["pid"] == pid)
    return {"key": f"{batch} {pid}", "k": r["k"], "family": r["family"], "T": r["T_tokens"], "text": r["cont"], "len": r["cont_len"], "pm": {x: r["pm"][x] for x in ("BIS", "RA", "THC", "CHAIN")}}


APEX["olm112"]["ex"] = [row112("b0j0"), row112("b1j17")]
APEX["olm114"]["ex"] = [row114("k1_0", "opus_r1"), row114("k1_0", "fable_r3")]
assert APEX["olm112"]["ex"][0]["text"].startswith("Each X_i forms a right angle with O1 and O2 (verified by zero dot product)") and APEX["olm112"]["ex"][0]["label_json"] == "B-bind" and APEX["olm112"]["ex"][0]["len"] == 129
assert "Miquel theorem" in APEX["olm112"]["ex"][1]["text"] and APEX["olm112"]["ex"][1]["label_json"] == "B-bind"
assert APEX["olm114"]["ex"][0]["pm"] == {"BIS": True, "RA": True, "THC": True, "CHAIN": True} and "b ⊥ b'" in APEX["olm114"]["ex"][0]["text"] and APEX["olm114"]["ex"][1]["text"].startswith(" Step 3 (union of bisectors")

# ---------------------------------------------------------------------------------------------------- the next question (olm128) — the candidate A the teacher chose; read after the brief was written (the coordinator's update 11-06 12:0x)
O128 = J(READ["olm128"])
NEXT = {"cells": O128["blocked_cells"], "verdicts": O128["verdicts"], "open_cells": O128["open_cells_description"], "md5": O128["md5"], "greedy": O128["greedy_rows_description"]}
assert (NEXT["verdicts"]["Q1"], NEXT["verdicts"]["Q3"]) == ("保たれない", "書き始めでは説明されない") and round(NEXT["verdicts"]["Q1_concordance"], 3) == 0.579 and NEXT["verdicts"]["Q1_N"] == 19
assert round(NEXT["verdicts"]["Q2_nl_diff"], 3) == 0.478 and round(NEXT["verdicts"]["Q2_space_diff"], 2) == -0.30 and NEXT["cells"]["nl"]["json"] == 7 and NEXT["cells"]["space"]["json"] == 0 and NEXT["cells"]["nlnl"]["json"] == 3

AFTER = {"cards": cards, "stations": STATIONS, "l3": L3, "space": SPACE, "struct": STRUCT, "apex": APEX, "next": NEXT,
         "grades": ["判定", "確かめた記述", "記述", "較正", "言えない"], "head_note": "values = read.json keys; frozen commit = the RESULT's header, checked against git's first commit of the PREREG"}
