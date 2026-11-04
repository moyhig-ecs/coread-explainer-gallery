"""pack_moy2.py — the FIRST route of every number in the figure (moy-2 reflection-tool line, olm113 → olm127).
Reads ONLY frozen outputs: data/moy2_line_inventory.json (the main session's inventory, md5 3190663e…), data/read/olm1NN.json (each card's read.json),
and the literal sentences listed in quoted.json (PREREG / RESULT / RECORD / MEMO). The experiment scripts (ConstructGap/exp/*.py, inventory/*.py) are never imported or run; gen.json is never read.
Every count is recounted here from the inventory rows and asserted against (a) the inventory's own agg, (b) the read.json of the card, (c) the brief's values (BRIEF §2). A disagreement stops the build.
    python3 -I pack_moy2.py        -> generated/pack.json
"""
import hashlib
import json
import math
import pathlib
import re
import statistics

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE  # bundle: the quoted cards live in cards/
INV = HERE / "data" / "moy2_line_inventory.json"
OUT = HERE / "generated"
OUT.mkdir(exist_ok=True)
md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
inv = json.loads(INV.read_text(encoding="utf-8"))
Q = json.loads((HERE / "quoted.json").read_text(encoding="utf-8"))
READ = {n: json.loads((HERE / "data" / "read" / f"olm{n}.json").read_text(encoding="utf-8")) for n in (118, 119, 122, 124, 125, 126, 127)}
assert md5(INV) == "3190663eadc56b6ea426472b0551624e", "the inventory is the frozen one (BRIEF §2)"
assert (HERE / "data" / "moy2_line_inventory.out").read_text(encoding="utf-8").rstrip().endswith("json md5 3190663eadc56b6ea426472b0551624e size 737773")
READ_MD5 = {118: "bffeb8263fcf28c0998f4726765f83af", 119: "f21385976c22adbf81eea690030af57f", 122: "30db9a253671288c70440a8f44bb44e0", 124: "ab5250a87781b0981a8f38e6017832d2", 125: "d0171213f9fad88075597ccb6d3c4434", 127: "a14ae15972dcc11ce2d6326f2d1e6aa0"}
for n, m in READ_MD5.items():
    assert md5(HERE / "data" / "read" / f"olm{n}.json") == m == inv["inputs"][f"ConstructGap/exp/olm{n}/read.json"], f"read.json olm{n} is the one the inventory read"


def lit(entry):
    """a quoted literal must occur in its file (the file read as text)"""
    text = (REPO / entry["file"]).read_text(encoding="utf-8")
    assert entry["literal"] in text, f"literal not found in {entry['file']}: {entry['literal'][:60]}"
    return entry


ARMS = ["olm113", "olm117", "olm119", "olm122", "olm124", "olm125", "olm127"]
TOOL = {"olm113": "none", "olm117": "none_eq", "olm119": "decl", "olm122": "formula", "olm124": "formula", "olm125": "instr", "olm127": "instr"}
EN = {"olm113": "no tool (M2A)", "olm117": "equal-radii control", "olm119": "formula + declaration", "olm122": "formula only (1st · G1 ✗)", "olm124": "formula only (2nd)",
      "olm125": "formula + instruction (1st)", "olm127": "formula + instruction (2nd · G1 ✗)"}
G1_FAIL = {"olm122", "olm127"}
rate = lambda a, b: round(a / b, 4) if b else 0.0


def compact(r):
    v3, v6 = r["proof_v3"] or {}, r["proof_v6"] or {}
    b, j = re.match(r"b(\d)_j(\d\d)$", r["key"]).groups()
    hits = [h[1] for h in (r["proof_v6_ln_hits"] or [])]
    return {"k": r["key"], "b": int(b), "j": int(j), "seed": r["seed"], "cls": r["cls"], "st": r["status"], "T": r["T"], "cap": r["hit_cap"], "calc": r["calc"], "men": r["mention"],
            "tn": r["tool_named"], "pf": r["has_proof"], "ln3": bool(v3.get("LN_a")), "ln6": bool(v6.get("LN6_a")), "out3": bool(v3.get("OUTER_a")), "out6": bool(v6.get("OUTER6_a")),
            "pt": bool(v3.get("PT_a")), "rej": r["rej6"], "typ": r["rej6_then_proof_LN6"], "conj": r["conjecture"], "proof": r["proof"], "rejf": r["rej6_first"] or "",
            "fc": (r["first_calc"] or "")[:320], "head": r["head"], "hit": hits[0] if hits else ""}


arms = []
for a in ARMS:
    A = inv["arms"][a]
    rows = A["rows"]
    ag = A["agg"]
    assert len(rows) == 60 == ag["n"], a
    assert len({r["key"] for r in rows}) == 60, a
    pr = [r for r in rows if r["has_proof"]]
    calc = [r for r in rows if r["calc"]]
    nonc = [r for r in rows if not r["calc"]]
    cnt = lambda rs, f: sum(1 for r in rs if f(r))
    ln3 = lambda r: bool((r["proof_v3"] or {}).get("LN_a"))
    ln6 = lambda r: bool((r["proof_v6"] or {}).get("LN6_a"))
    parsed = cnt(rows, lambda r: r["cls"] != "NONE")
    cls = {c: cnt(rows, lambda r, c=c: r["cls"] == c) for c in ("MIDO3", "EQ", "OTHER", "NONE")}
    rec = {
        "n": 60, "parsed": parsed, "n_proof": len(pr),
        "LN3": cnt(pr, ln3), "LN6": cnt(pr, ln6), "OUT3": cnt(pr, lambda r: bool((r["proof_v3"] or {}).get("OUTER_a"))), "OUT6": cnt(pr, lambda r: bool((r["proof_v6"] or {}).get("OUTER6_a"))),
        "PT": cnt(pr, lambda r: bool((r["proof_v3"] or {}).get("PT_a"))), "CALC": len(calc), "TN": cnt(rows, lambda r: r["tool_named"]), "MEN": cnt(rows, lambda r: r["mention"]),
        "REJ": cnt(rows, lambda r: r["rej6"]), "REJ_calc": cnt(calc, lambda r: r["rej6"]), "typ": [r["key"] for r in rows if r["rej6_then_proof_LN6"]],
        "cap": cnt(rows, lambda r: r["hit_cap"]), "cls": cls,
        "calc_split": {"n_proof": cnt(calc, lambda r: r["has_proof"]), "LN3": cnt(calc, lambda r: r["has_proof"] and ln3(r)), "LN6": cnt(calc, lambda r: r["has_proof"] and ln6(r))},
        "noncalc_split": {"n_proof": cnt(nonc, lambda r: r["has_proof"]), "LN3": cnt(nonc, lambda r: r["has_proof"] and ln3(r)), "LN6": cnt(nonc, lambda r: r["has_proof"] and ln6(r))},
        "calc_cls": {c: cnt(calc, lambda r, c=c: r["cls"] == c) for c in ("MIDO3", "EQ", "OTHER", "NONE")},
        "T_med": statistics.median(r["T"] for r in rows), "T_med_calc": statistics.median(r["T"] for r in calc) if calc else None, "T_med_noncalc": statistics.median(r["T"] for r in nonc),
        "seeds": sorted({r["seed"] for r in rows}), "status_hyp": cnt(rows, lambda r: r["status"] == "hypothesis"),
    }
    rec["LN3_rate"], rec["LN6_rate"] = rate(rec["LN3"], rec["n_proof"]), rate(rec["LN6"], rec["n_proof"])
    rec["OUT3_rate"], rec["OUT6_rate"] = rate(rec["OUT3"], rec["n_proof"]), rate(rec["OUT6"], rec["n_proof"])
    rec["PT_rate"] = rate(rec["PT"], rec["n_proof"])
    rec["MIDO3_rate"], rec["EQ_rate"] = rate(cls["MIDO3"], parsed), rate(cls["EQ"], parsed)
    rec["parsed_rate"], rec["CALC_rate"] = rate(parsed, 60), rate(len(calc), 60)
    # (a) the inventory's own agg
    assert (rec["parsed"], rec["n_proof"], rec["CALC"], rec["REJ"], rec["REJ_calc"], rec["TN"], rec["cap"]) == (ag["parsed"], ag["n_proof"], ag["REFL_CALC"], ag["REJ6"], ag["REJ6_in_calc"], ag["tool_named"], ag["hit_cap"]), a
    assert (rec["LN3"], rec["LN6"], rec["OUT3"], rec["OUT6"], rec["PT"]) == (ag["proof_v3"]["LN_a"], ag["proof_v6"]["LN6_a"], ag["proof_v3"]["OUTER_a"], ag["proof_v6"]["OUTER6_a"], ag["proof_v3"]["PT_a"]), a
    assert rec["typ"] == ag["REJ6_then_proof_LN6"] and rec["cls"] == {c: ag["cls"].get(c, 0) for c in rec["cls"]}, a
    assert rec["calc_split"] == {"n_proof": ag["calc_split"]["n_proof"], "LN3": ag["calc_split"]["LN_a"], "LN6": ag["calc_split"]["LN6_a"]}, a
    assert rec["noncalc_split"] == {"n_proof": ag["noncalc_split"]["n_proof"], "LN3": ag["noncalc_split"]["LN_a"], "LN6": ag["noncalc_split"]["LN6_a"]}, a
    assert rec["T_med"] == ag["T_median"] and rec["MIDO3_rate"] == ag["MIDO3_rate_parsed"] and rec["EQ_rate"] == ag["EQ_rate_parsed"], a
    if calc:
        assert rec["T_med_calc"] == ag["calc_T_median"] and rec["T_med_noncalc"] == ag["noncalc_T_median"], a
    assert {c: v for c, v in rec["calc_cls"].items() if v} == {c: v for c, v in ag["calc_cls"].items() if v}, a
    arms.append({"id": a, "label": A["label"], "label_en": EN[a], "tool": TOOL[a], "g1fail": a in G1_FAIL, "prompt_md5": A.get("prompt_md5"), "agg": rec, "rows": [compact(r) for r in rows]})
AR = {x["id"]: x["agg"] for x in arms}

# (b) the read.json of each card (second route for the frozen numbers)
r118, r119, r122, r124, r125, r126, r127 = (READ[n] for n in (118, 119, 122, 124, 125, 126, 127))
assert r118["Q1"]["LN_a_rate_proof"] == {"olm113": AR["olm113"]["LN3_rate"], "olm117": AR["olm117"]["LN3_rate"]}
assert r118["Q2"]["PT_a_rate_proof"] == {"olm113": AR["olm113"]["PT_rate"], "olm117": AR["olm117"]["PT_rate"]}
assert r118["Q3"]["OUTER_a_rate_proof"] == {"olm113": AR["olm113"]["OUT3_rate"], "olm117": AR["olm117"]["OUT3_rate"]}
assert r119["Q1"]["LN_a_rate_proof"]["tool"] == AR["olm119"]["LN3_rate"] and r119["Q2"]["n"] == AR["olm119"]["CALC"] and r119["Q2"]["REFL_CALC_rate"] == AR["olm119"]["CALC_rate"]
assert r122["Q1"]["LN_a_rate_proof"]["formula_only"] == AR["olm122"]["LN3_rate"] and r122["Q3_desc"]["MIDO3_rate_parsed"]["formula_only"] == AR["olm122"]["MIDO3_rate"] and r122["Q2"]["n"] == AR["olm122"]["CALC"]
assert r122["Q3_desc"]["tool_named"] == AR["olm122"]["TN"] and r122["Q3_desc"]["proof_OUTER_a"]["formula_only"] == AR["olm122"]["OUT3"]
assert r124["Q1"]["LN_a_rate_proof"]["rerun"] == AR["olm124"]["LN3_rate"] and r124["gates"]["G1_parsed"] == AR["olm124"]["parsed"] and r124["Q2"]["n"] == AR["olm124"]["CALC"]
assert r125["Q1"]["LN_a_rate_proof"]["use"] == AR["olm125"]["LN3_rate"] and r125["gates"]["G1_parsed"] == AR["olm125"]["parsed"] and r125["Q2"]["n"] == AR["olm125"]["CALC"]
assert r127["Q1"]["LN_a_rate_proof"]["rerun"] == AR["olm127"]["LN3_rate"] and r127["gates"]["G1_parsed"] == AR["olm127"]["parsed"] and r127["Q2"]["n"] == AR["olm127"]["CALC"]
assert r127["Q1"]["n_proof"] == AR["olm127"]["n_proof"] and r127["Q1"]["LN_a"] == AR["olm127"]["LN3"]
for a in ("olm113", "olm119", "olm122", "olm124", "olm125"):
    assert r126["Q2"]["LN6_rate_proof"][a] == AR[a]["LN6_rate"] and r126["Q2"]["LN_rate_proof(v3)"][a] == AR[a]["LN3_rate"], a
    assert r126["Q3"]["REJ6_counts"][a] == AR[a]["REJ"] and r126["Q3"]["REJ6_then_LN6"][a] == AR[a]["typ"], a
assert r126["Q2"]["frozen"] == r126["Q2"]["v6"] and len(r126["Q2"]["frozen"]) == 7 and r126["Q2"]["verdict"] == "同じ"
for name, n in (("olm126(v6)", 126), ("olm125", 125), ("olm127", 127), ("olm124", 124), ("olm119", 119), ("olm122", 122)):
    for q, sec in inv["frozen"][name].items():
        if isinstance(sec, dict) and q in READ[n]:
            assert all(READ[n][q].get(k) == v for k, v in sec.items()), (name, q)      # the inventory's copy of the frozen verdicts is a subset of the read.json
assert all(c["ok"] for c in inv["recount_vs_read_json"]) and len(inv["recount_vs_read_json"]) == 20

# (c) the brief's values (BRIEF §2). Where the brief and the data differ the data wins: those places are listed in CLAIMS.md §D, and asserted here as data.
assert [AR[a]["LN3"] for a in ARMS] == [5, 7, 14, 4, 4, 9, 3] and [AR[a]["n_proof"] for a in ARMS] == [41, 46, 44, 37, 37, 40, 35]
assert [AR[a]["LN6"] for a in ARMS] == [5, 7, 15, 5, 6, 11, 3]
assert [AR[a]["parsed"] for a in ARMS] == [50, 50, 48, 46, 45, 45, 40]
assert [AR[a]["CALC"] for a in ARMS] == [6, 0, 13, 12, 15, 18, 10] and [AR[a]["REJ"] for a in ARMS] == [0, 0, 11, 6, 11, 15, 6]
assert [AR[a]["typ"] for a in ARMS] == [[], [], ["b0_j13", "b1_j06", "b2_j08"], ["b1_j11", "b2_j07"], ["b2_j07"], ["b1_j11", "b1_j17", "b2_j19"], []]
assert [(AR[a]["calc_split"]["LN3"], AR[a]["calc_split"]["n_proof"], AR[a]["noncalc_split"]["LN3"], AR[a]["noncalc_split"]["n_proof"]) for a in ("olm125", "olm124", "olm119", "olm122", "olm113", "olm127")] == [(2, 9, 7, 31), (1, 7, 3, 30), (3, 10, 11, 34), (1, 9, 3, 28), (0, 3, 5, 38), (0, 3, 3, 32)]
assert [AR[a]["MIDO3_rate"] for a in ARMS] == [0.34, 0.74, 0.6042, 0.587, 0.5111, 0.4444, 0.5] and [AR[a]["EQ_rate"] for a in ARMS] == [0.32, 0.0, 0.1667, 0.2609, 0.2667, 0.3111, 0.125]
assert [AR[a]["OUT3"] for a in ARMS] == [10, 13, 12, 9, 9, 10, 6] and [AR[a]["OUT6"] for a in ARMS] == [10, 13, 12, 8, 9, 10, 6]
assert [AR[a]["TN"] for a in ARMS] == [1, 0, 12, 11, 11, 18, 7]
assert AR["olm125"]["calc_cls"] == {"MIDO3": 0, "EQ": 9, "OTHER": 4, "NONE": 5}

# the bands of the frozen verdicts (from the PREREG literals in quoted.json) — the verdict is recomputed here and must equal the read.json verdict
B = Q["bands"]
for k in B:
    lit(B[k])


def band_of(spec, r, base=None):
    if spec["kind"] == "diff1":
        d = round(r - (base if base is not None else spec["base"]), 4)
        for name, op, th in spec["rules"]:
            if (op == "abs<" and abs(d) < th) or (op == ">=" and d >= th - 1e-9) or (op == "<=" and d <= th + 1e-9):
                return name
        return spec["else"]
    if spec["kind"] == "two":
        d113, d119 = r - spec["base113"], r - spec["base119"]
        if abs(d113) < 0.06: return "戻る"
        if abs(d119) < 0.06: return "残る"
        if d119 >= 0.06: return "上がる"
        if d113 <= -0.06: return "下回る"
        return "間"
    for name, lo, hi in spec["segs"]:
        if (lo is None or r > lo) and (hi is None or r < hi):
            return name
    return spec["segs"][-1][0]


def segs_of(spec, base=None):
    """the band as segments on the rate axis (absolute r), from the frozen rule"""
    if spec["kind"] == "abs":
        return [[n, lo, hi] for n, lo, hi in spec["segs"]]
    if spec["kind"] == "two":
        b1, b9 = spec["base113"], spec["base119"]
        return [["下回る", None, round(b1 - .06, 3)], ["戻る", round(b1 - .06, 3), round(b1 + .06, 3)], ["間", round(b1 + .06, 3), round(b9 - .06, 3)], ["残る", round(b9 - .06, 3), round(b9 + .06, 3)], ["上がる", round(b9 + .06, 3), None]]
    b0 = base if base is not None else spec["base"]
    rules = {n: (op, th) for n, op, th in spec["rules"]}
    pts = sorted({round(b0 + (th if op != "abs<" else s * th), 3) for n, (op, th) in rules.items() for s in ((-1, 1) if op == "abs<" else (1,))})
    edges = [None] + pts + [None]
    out = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mid = (lo if lo is not None else hi - .05) + ((hi - lo) / 2 if lo is not None and hi is not None else (.025 if lo is None else -.025)) if (lo is not None or hi is not None) else 0
        if lo is None: mid = hi - .02
        if hi is None: mid = lo + .02
        out.append([band_of(spec, mid, b0), lo, hi])
    return out


VERD = {}
b113 = AR["olm113"]["LN3_rate"]
VERD["olm117"] = {"band": "olm118", "base": b113, "r": AR["olm117"]["LN3_rate"], "read": r118["Q1"]["verdict"], "segs": segs_of(B["olm118"], b113), "calc": band_of(B["olm118"], AR["olm117"]["LN3_rate"], b113)}
VERD["olm119"] = {"band": "olm119", "r": AR["olm119"]["LN3_rate"], "read": r119["Q1"]["verdict"], "segs": segs_of(B["olm119"]), "calc": band_of(B["olm119"], AR["olm119"]["LN3_rate"])}
VERD["olm122"] = {"band": "olm122", "r": AR["olm122"]["LN3_rate"], "read": r122["Q1"]["verdict"], "segs": segs_of(B["olm122"]), "calc": band_of(B["olm122"], AR["olm122"]["LN3_rate"])}
VERD["olm124"] = {"band": "olm124", "r": AR["olm124"]["LN3_rate"], "read": r124["Q1"]["verdict"], "segs": segs_of(B["olm124"]), "calc": band_of(B["olm124"], AR["olm124"]["LN3_rate"])}
VERD["olm125"] = {"band": "olm125", "r": AR["olm125"]["LN3_rate"], "read": r125["Q1"]["verdict"], "segs": segs_of(B["olm125"]), "calc": band_of(B["olm125"], AR["olm125"]["LN3_rate"])}
VERD["olm127"] = {"band": "olm127", "r": AR["olm127"]["LN3_rate"], "read": r127["Q1"]["verdict"], "segs": segs_of(B["olm127"]), "calc": band_of(B["olm127"], AR["olm127"]["LN3_rate"])}
for a, v in VERD.items():
    if a in G1_FAIL:
        assert v["read"] is None, f"{a}: G1 failed, so read.json has no verdict"
    else:
        assert v["calc"] == v["read"], f"{a}: the band recomputed from the PREREG ({v['calc']}) equals the frozen verdict ({v['read']})"
assert VERD["olm122"]["calc"] == "戻る" and VERD["olm127"]["calc"] == "戻る"     # what the reference value WOULD sit in (shown only with the 'no verdict' tag)
assert [s[1:] for s in VERD["olm124"]["segs"]][1] == [0.062, 0.182] and [s[1:] for s in VERD["olm125"]["segs"]][1] == [0.048, 0.168]
q3 = band_of(B["olm118_Q3"], AR["olm117"]["OUT3_rate"], AR["olm113"]["OUT3_rate"])
assert q3 == r118["Q3"]["verdict"] == "変わらない" and round(AR["olm117"]["OUT3_rate"] - AR["olm113"]["OUT3_rate"], 4) == r118["Q3"]["diff"] == 0.0387

# gates (G1)
G = lit(Q["gate"]); lit(G["old"])
gates = {"olm119": r119["gates"]["G1_conj_parsed>=0.80"], "olm122": r122["gates"]["G1_conj_parsed>=0.80"], "olm124": r124["gates"]["G1_conj_parsed>=0.75"], "olm125": r125["gates"]["G1_conj_parsed>=0.75"], "olm127": r127["gates"]["G1_conj_parsed>=0.75"]}
assert gates == {"olm119": True, "olm122": False, "olm124": True, "olm125": True, "olm127": False}
assert [AR[a]["parsed_rate"] for a in ("olm113", "olm119", "olm122", "olm124", "olm125", "olm127")] == [0.8333, 0.8, 0.7667, 0.75, 0.75, 0.6667]

# the instrument's lineage
L4 = lit(Q["lineage_v4v5"])
lin = inv["instrument_lineage"]
assert lin["calibration"] == {"v3": 54, "v4": 74, "v5": 98, "v6": 144} and lin["olm118_Q3_OUTER_by_version"]["v3"] == "変わらない" == lin["olm118_Q3_OUTER_by_version"]["v6"]
assert all(lin["negative_control_prf5"].values()) and r118["gates"]["n_prf5"] == 20 and r126["calibration_n"] == 144
lineage = {"cal": lin["calibration"], "q3": [["v3", lin["olm118_Q3_OUTER_by_version"]["diff_v3"], lin["olm118_Q3_OUTER_by_version"]["v3"]], ["v4", L4["v4"], L4["v4_band"]], ["v5", L4["v5"], L4["v5_band"]], ["v6", lin["olm118_Q3_OUTER_by_version"]["diff_v6"], lin["olm118_Q3_OUTER_by_version"]["v6"]]],
           "neg": {"n": r118["gates"]["n_prf5"], "outer": 0, "pt_ln": 0}, "frozen": r126["Q2"]["frozen"], "v6same": r126["Q2"]["v6"], "q1_126": r126["Q1"]["verdict"], "q3_126": r126["Q3"]["verdict"], "missing126": r126["Q3"]["missing(残るべきで落ちた)"]}
for b in L4["v4"], L4["v5"]:
    assert band_of(B["olm118_Q3"], b, 0.0) == "間"
for c in Q["lineage_cases"]:
    lit(c)
cases = []
for c in Q["lineage_cases"]:
    row = next(r for r in inv["arms"][c["arm"]]["rows"] if r["key"] == c["key"])
    assert c["literal"] in row["proof"], c["id"]
    cases.append({"id": c["id"], "arm": c["arm"], "key": c["key"], "ver": c["ver"], "proof": row["proof"], "out3": row["proof_v3"]["OUTER_a"], "out6": row["proof_v6"]["OUTER6_a"]})
# v6 LN hits of olm124 (what the v6 reader added: direct object / formula copy): the rows whose v6 LN is true but v3 LN is false
v6_added = {a: [r["k"] for r in next(x for x in arms if x["id"] == a)["rows"] if r["pf"] and r["ln6"] and not r["ln3"]] for a in ARMS}
v6_dropped = {a: [r["k"] for r in next(x for x in arms if x["id"] == a)["rows"] if r["pf"] and r["ln3"] and not r["ln6"]] for a in ARMS}
named = r126["Q2"]["named_rows"]
assert sorted(f"{a}_{k}_+" for a in v6_added for k in v6_added[a] if a not in ("olm117", "olm127")) == sorted(k for k in named if k.endswith("+")), "the rows v6 added = olm126's named rows (+)"
assert sorted(f"{a}_{k}_−" for a in v6_dropped for k in v6_dropped[a] if a not in ("olm117", "olm127")) == sorted(k for k in named if k.endswith("−")), "the rows v6 dropped = olm126's named rows (−)"

# scenes (S1..S10) and loops
SC = {}
for name, s in inv["scenes"].items():
    sid = name.split("_")[0]
    arm = re.search(r"\((olm\d+) (b\d_j\d\d)\)", name)
    SC[sid] = {"name": name, "arm": arm.group(1), "key": arm.group(2), "pred": s["pred"], "loop_phrase": s.get("loop_phrase"), "loop_count": s.get("loop_count")}
    row = next(r for r in inv["arms"][arm.group(1)]["rows"] if r["key"] == arm.group(2))
    assert row == s["row"], sid
assert (SC["S8"]["loop_count"], SC["S10"]["loop_count"]) == (343, 542) and SC["S8"]["loop_phrase"] == "But as above, the determinant is not zero" and SC["S10"]["loop_phrase"] == "but already checked"
row = lambda a, k: next(r for r in next(x for x in arms if x["id"] == a)["rows"] if r["k"] == k)
s1, s2 = row("olm125", "b1_j17"), row("olm125", "b0_j16")
assert (s1["cls"], s1["T"], s1["rej"], s1["ln6"]) == ("EQ", 4315, True, True) and (s2["cls"], s2["T"], s2["rej"], s2["ln6"], s2["pf"]) == ("EQ", 7335, True, False, True)
assert row("olm127", "b2_j09")["proof"].startswith("Compute O3Tc and O3Th: both are sqrt(14.764)")
assert row("olm127", "b2_j08")["calc"] is False and row("olm127", "b1_j13")["calc"] is True and row("olm127", "b2_j08")["cap"] and row("olm127", "b1_j13")["cap"]
H = lit(Q["hint_quote"])
for k in ("four_arms", "four_arms_parts", "four_arms_127", "four_arms_retracted", "four_arms_retracted_127", "rej_to_proof_125", "fisher127_more", "apex_rows_127", "q3_126_row",
          "loop_quotes", "b1_j03_quote", "question", "memo_answer", "radius_equal", "apex_def", "seeds_record", "fisher", "fisher127"):
    lit(Q[k])
lit({"file": Q["fisher127_more"]["file"], "literal": Q["fisher127_more"]["pool"]["literal"]})
for m in Q["memo_rows"]:
    lit({"file": Q["memo_file"], "literal": m["literal"]})
# v1.1 F1: the OLD four-arm number (43 / 47, RECORD §4 / RESULT olm127 §4) is kept only to be named as NOT kept (RECORD correction 3); its parts sum to it (the literal is what it is) —
assert sum(v[0] for d in (Q["four_arms_parts"]["parts"], Q["four_arms_127"]["parts"]) for v in d.values()) == Q["four_arms"]["num"]
assert sum(v[1] for d in (Q["four_arms_parts"]["parts"], Q["four_arms_127"]["parts"]) for v in d.values()) == Q["four_arms"]["den"]
# — and the figure's number is the inventory predicate (REJ6 ∧ REFL_CALC / REFL_CALC), recounted from the rows (L2) and equal to the RECORD correction 3
FOUR = ["olm119", "olm124", "olm125", "olm127"]
four = {"num": sum(AR[a]["REJ_calc"] for a in FOUR), "den": sum(AR[a]["CALC"] for a in FOUR), "parts": {a: [AR[a]["REJ_calc"], AR[a]["CALC"]] for a in FOUR + ["olm122", "olm113"]},
        "old": [Q["four_arms"]["num"], Q["four_arms"]["den"]]}
assert (four["num"], four["den"]) == (Q["four_arms_retracted"]["num"], Q["four_arms_retracted"]["den"]) == (42, 56)
assert four["parts"] == {"olm119": [10, 13], "olm124": [11, 15], "olm125": [15, 18], "olm127": [6, 10], "olm122": [5, 12], "olm113": [0, 6]}

# v1.1 F4: two-sided Fisher exact tests between neighbouring arms (reference; not frozen; no correction for multiple comparisons) — counted HERE from the rows (L2) and set against the RESULT literals (L1)


def fisher(a, n1, b, n2):
    """two-sided exact p: the sum of the probabilities of the tables (same margins) that are no more probable than the observed one"""
    K, N = a + b, n1 + n2
    pr = lambda x: math.comb(n1, x) * math.comb(n2, K - x) / math.comb(N, K)
    p0 = pr(a)
    return min(1.0, sum(pr(x) for x in range(max(0, K - n2), min(K, n1) + 1) if pr(x) <= p0 * (1 + 1e-7)))


LNp = lambda a: [AR[a]["LN3"], AR[a]["n_proof"]]
pool_f = [AR["olm122"]["LN3"] + AR["olm124"]["LN3"], AR["olm122"]["n_proof"] + AR["olm124"]["n_proof"]]
pool_i = [AR["olm125"]["LN3"] + AR["olm127"]["LN3"], AR["olm125"]["n_proof"] + AR["olm127"]["n_proof"]]
F_PAIRS = [("olm125", "olm124", LNp("olm125"), LNp("olm124"), Q["fisher"]["p124"], "RESULT olm125 §2"),
           ("olm125", "pool_f", LNp("olm125"), pool_f, Q["fisher"]["ppool"], "RESULT olm125 §2"),
           ("olm125", "olm119", LNp("olm125"), LNp("olm119"), Q["fisher"]["p119"], "RESULT olm125 §2"),
           ("olm127", "olm124", LNp("olm127"), LNp("olm124"), Q["fisher127"]["p124"], "RESULT olm127 §2"),
           ("olm127", "olm125", LNp("olm127"), LNp("olm125"), Q["fisher127"]["p125"], "RESULT olm127 §2"),
           ("olm127", "olm119", LNp("olm127"), LNp("olm119"), Q["fisher127_more"]["p119"], "RESULT olm127 §2"),
           ("pool_i", "pool_f", pool_i, pool_f, Q["fisher127_more"]["pool"]["p"], "RESULT olm127 §2")]
fisher_rows = []
for x, y, kx, ky, lit_p, src in F_PAIRS:
    p_ = round(fisher(kx[0], kx[1], ky[0], ky[1]), 4)
    nd = len(str(lit_p).split(".")[1]) if "." in str(lit_p) else 0
    assert round(p_, max(nd, 1)) == lit_p or (lit_p == 1.0 and p_ == 1.0), f"Fisher {x} vs {y}: rows give {p_}, the RESULT writes {lit_p} (the data would win: tell the main session)"
    fisher_rows.append({"x": x, "y": y, "kx": kx, "ky": ky, "p": p_, "lit": lit_p, "lit_s": str(lit_p), "src": src})
assert pool_f == [8, 74] and pool_i == [12, 75]

# v1.1 F5: the two olm127 rows that reach the equidistance with numbers (RESULT olm127 §3.4 / §4 name them; the inventory has no predicate for it = L1 text anchor)
APEX = Q["apex_rows_127"]
for k in APEX["keys"]:
    r_ = row("olm127", k)
    assert r_["cls"] == "EQ" and r_["calc"] and not r_["rej"], k
assert not row("olm127", "b0_j00")["pf"] and row("olm127", "b0_j00")["st"] == "none" and APEX["b2_j09"]["literal"] in row("olm127", "b2_j09")["proof"]
assert APEX["b0_j00"]["literal"] in (REPO / APEX["file"]).read_text(encoding="utf-8")

# BRIEF §2 items 1–18 (v1 items 1–11 are asserted above; v1.1 items 12–18 here). Each check is a (item, ok) pair; the build prints the count.
_rows125 = next(x for x in arms if x["id"] == "olm125")["rows"]
BRIEF = [
    (1, [AR[a]["LN3"] for a in ARMS] == [5, 7, 14, 4, 4, 9, 3] and [AR[a]["n_proof"] for a in ARMS] == [41, 46, 44, 37, 37, 40, 35]),
    (2, [AR[a]["LN6"] for a in ARMS] == [5, 7, 15, 5, 6, 11, 3]),
    (3, [AR[a]["parsed"] for a in ARMS] == [50, 50, 48, 46, 45, 45, 40]),
    (4, [AR[a]["CALC"] for a in ARMS] == [6, 0, 13, 12, 15, 18, 10] and [AR[a]["REJ"] for a in ARMS] == [0, 0, 11, 6, 11, 15, 6]),
    (5, [(AR[a]["calc_split"]["LN3"], AR[a]["calc_split"]["n_proof"], AR[a]["noncalc_split"]["LN3"], AR[a]["noncalc_split"]["n_proof"]) for a in ("olm125", "olm124", "olm119", "olm122", "olm113", "olm127")] == [(2, 9, 7, 31), (1, 7, 3, 30), (3, 10, 11, 34), (1, 9, 3, 28), (0, 3, 5, 38), (0, 3, 3, 32)]),
    (6, [AR[a]["MIDO3_rate"] for a in ARMS] == [0.34, 0.74, 0.6042, 0.587, 0.5111, 0.4444, 0.5] and [AR[a]["EQ_rate"] for a in ARMS] == [0.32, 0.0, 0.1667, 0.2609, 0.2667, 0.3111, 0.125]),
    (7, [AR[a]["OUT3"] for a in ARMS] == [10, 13, 12, 9, 9, 10, 6] and [AR[a]["OUT6"] for a in ARMS] == [10, 13, 12, 8, 9, 10, 6]),
    (8, (r118["Q1"]["verdict"], r118["Q2"]["verdict"], r118["Q3"]["verdict"], r119["Q1"]["verdict"], r124["Q1"]["verdict"], r124["Q2"]["verdict"], r125["Q1"]["verdict"], r125["Q2"]["verdict"], r126["Q1"]["verdict"], r126["Q2"]["verdict"], r126["Q3"]["verdict"], r127["Q1"]["verdict"], r127["Q2"]["verdict"]) == ("変わらない", "増える", "変わらない", "上がる", "戻る", "間", "上がる", "変わらない", "直った", "同じ", "通らない", None, "変わらない")),
    (9, lin["calibration"] == {"v3": 54, "v4": 74, "v5": 98, "v6": 144} and [q[2] for q in lineage["q3"]] == ["変わらない", "間", "間", "変わらない"]),
    (10, (SC["S8"]["loop_count"], SC["S10"]["loop_count"]) == (343, 542) and (s1["cls"], s1["T"]) == ("EQ", 4315) and (s2["cls"], s2["T"]) == ("EQ", 7335) and row("olm127", "b2_j09")["T"] == 3570),
    (11, sum(c["ok"] for c in inv["recount_vs_read_json"]) == 20 == len(inv["recount_vs_read_json"])),
    (12, [(AR[a]["REJ_calc"], AR[a]["CALC"]) for a in ARMS] == [(0, 6), (0, 0), (10, 13), (5, 12), (11, 15), (15, 18), (6, 10)] and (four["num"], four["den"]) == (42, 56) and [AR[a]["REJ"] for a in ARMS] == [0, 0, 11, 6, 11, 15, 6]),
    (13, [r["k"] for r in _rows125 if r["rej"] and r["pf"]] == ["b0_j01", "b0_j08", "b0_j09", "b0_j16", "b1_j11", "b1_j17", "b2_j06", "b2_j19"] == Q["rej_to_proof_125"]["keys"]
         and sum(1 for r in _rows125 if r["calc"] and r["pf"]) == 9 and AR["olm125"]["calc_cls"] == {"MIDO3": 0, "EQ": 9, "OTHER": 4, "NONE": 5}),
    (14, [(AR[a]["T_med_calc"], AR[a]["T_med_noncalc"]) for a in ARMS] == [(9268, 789), (None, 560), (5406, 342), (7331.5, 383.5), (8849, 405), (8748.5, 254.5), (12288, 397)]),
    (15, (len(inv["prompts"]["TOOL_D(式だけ・olm122/124)"]), len(inv["prompts"]["SECOND(宣言の文・olm119)"]), len(inv["prompts"]["TOOL(式 + 宣言の文・olm119)"]), len(inv["prompts"]["TOOL_U(指示の文・olm125/127)"])) == (162, 106, 267, 90)
         and inv["prompts"]["prompt_md5"]["olm122/124"].startswith("2c4a01a4") and inv["prompts"]["prompt_md5"]["olm125/127"].startswith("718d1601")),
    (16, [(r118[q]["diff"], r118[q]["verdict"]) for q in ("Q1", "Q2", "Q3")] == [(0.0302, "変わらない"), (0.087, "増える"), (0.0387, "変わらない")]),
    (17, [f["lit"] for f in fisher_rows[:5]] == [0.23, 0.11, 0.46, 1.0, 0.12] and all(round(f["p"], 2) == round(f["lit"], 2) for f in fisher_rows)),
    (18, APEX["keys"] == ["b0_j00", "b2_j09"]),
]
# ---- v1.2 (BRIEF v1.2 G1 / G7 / G8 / G2): the scene's frame phrase and which point each scene row reflected · the band edges as printed · the Fisher pairs on each side of the 0.05 reference tick
_raw125 = {r["key"]: r for r in inv["arms"]["olm125"]["rows"]}
S1_PHRASE = "the inner common tangent is symmetric with respect to O1O2"          # G1: the words the v3 reader caught in S1's proof field (inside its v3 window)
assert S1_PHRASE in _raw125["b1_j17"]["proof"] and S1_PHRASE in (_raw125["b1_j17"]["proof_v3_first"]["LN"] or "") and not _raw125["b0_j16"]["proof_v6_ln_hits"]
_refl = {k: re.match(r"\s*2F\s*-\s*(Tc|Th)\b", _raw125[k]["rej6_start"]).group(1) for k in ("b1_j17", "b0_j16")}
assert _refl == {"b1_j17": "Th", "b0_j16": "Tc"}, _refl                         # G1: S1 reflects Th (compares with Tc) · S2 reflects Tc (compares with Th)
slip0 = {"phrase": S1_PHRASE, "refl": _refl, "start": {k: _raw125[k]["rej6_start"][:60] for k in _refl}}
lit127 = B["olm127"]["literal"]
assert "**残る** 0.165 ≤ r < 0.285" in lit127 and "**戻る** 0.048 < r < 0.168" in lit127 and "重なりは 戻る が先" in lit127
def edges_of(a):
    """G8: the band edges of the arm's own PREREG, as printed next to the band / the short ticks (olm127: the 残る edge is 0.165 with the overlap 0.165–0.168 going to 戻る)"""
    vs = sorted({v for _, lo, hi in VERD[a]["segs"] for v in (lo, hi) if v is not None})
    return [[v, "0.165〜0.168" if (a == "olm127" and v == 0.168) else f"{v:.3f}"] for v in vs]
EDGES = {a: edges_of(a) for a in VERD}
assert [v for v, _ in EDGES["olm124"]] == [0.062, 0.182, 0.258, 0.378] and [v for v, _ in EDGES["olm125"]] == [0.048, 0.168] and EDGES["olm127"] == [[0.048, "0.048"], [0.168, "0.165〜0.168"], [0.285, "0.285"]]
f_below = [[f["x"], f["y"]] for f in fisher_rows if f["p"] < 0.05]
assert f_below == [["olm127", "olm119"]] and sum(1 for f in fisher_rows if f["p"] >= 0.05) == 6       # G7: 6 pairs above the reference tick, 1 below (olm127 3 / 35 vs olm119 14 / 44, p 0.0142)
BRIEF += [
    (19, [s[1:] for s in VERD["olm124"]["segs"]][1] == [0.062, 0.182] and [s[1:] for s in VERD["olm125"]["segs"]][1] == [0.048, 0.168] and VERD["olm125"]["segs"][2][1] == 0.168
         and [s[1:] for s in VERD["olm127"]["segs"]] == [[None, 0.048], [0.048, 0.168], [0.168, 0.285], [0.285, None]] and "0.165 ≤ r < 0.285" in lit127),
    (20, f_below == [["olm127", "olm119"]] and next(f for f in fisher_rows if f["x"] == "olm127" and f["y"] == "olm119")["p"] == 0.0142 and LNp("olm127") == [3, 35] and LNp("olm119") == [14, 44]),
    (21, (AR["olm113"]["cls"]["MIDO3"], AR["olm113"]["parsed"], AR["olm113"]["MIDO3_rate"], AR["olm117"]["cls"]["MIDO3"], AR["olm117"]["parsed"], AR["olm117"]["MIDO3_rate"]) == (17, 50, 0.34, 37, 50, 0.74)),
]
# v1.3 (BRIEF v1.3 §2 items 22–23): olm127's rejecting rows (cap 5 · proof field 1, no line symmetry) and the sources of state 18's candidates (RECORD §6 (a)–(e) · MEMO §4 item 3)
for k_ in ("record6", "memo4_3", "rej127_split", "rej127_numeric"): lit(Q[k_])
_r127 = inv["arms"]["olm127"]["rows"]
_sec6 = (REPO / Q["record6"]["file"]).read_text(encoding="utf-8").split("## §6.")[1].split("\n## ")[0]
_sec4 = (REPO / Q["memo4_3"]["file"]).read_text(encoding="utf-8").split("## §4.")[1].split("\n## ")[0]
_item3 = _sec4.split("\n3. ")[1].split("\n4. ")[0]
BRIEF += [
    (22, sum(1 for r in _r127 if r["rej6"] and r["hit_cap"]) == 5 and [r["key"] for r in _r127 if r["rej6"] and r["has_proof"]] == ["b2_j11"] and not any((r["proof_v6"] or {}).get("LN6_a") for r in _r127 if r["rej6"] and r["has_proof"])),
    (23, re.findall(r"^- \(([a-z])\)", _sec6, re.M) == list("abcde") and "(e) 図解" in _sec6 and "退けが commit を支配する仕組み" in _item3 and "退けが commit を支配する仕組み" not in _sec6),
]
assert [i for i, _ in BRIEF] == list(range(1, 24)) and all(ok for _, ok in BRIEF), [i for i, ok in BRIEF if not ok]

# the configuration (moy-2): coordinates as written in S1's text (head + the reject sentence); the geometry below is computed from them and checked against the rows' own numbers
raw_s1 = inv["scenes"]["S1_rej_then_LN(olm125 b1_j17)"]["row"]
h, rf = raw_s1["head"], raw_s1["rej6_first"]
num = r"(-?\d+\.\d+)"
O1 = tuple(map(float, re.search(r"O1 = \(" + num + ", " + num + r"\), radius " + num, h).groups()))
O2 = tuple(map(float, re.search(r"O2 = \(" + num + ", " + num + r"\), radius " + num, h).groups()))
Th = tuple(map(float, re.search(r"Th = \(" + num + ", " + num + r"\)", h).groups()))
Tc = tuple(map(float, re.search(r"Compare this to Tc: \(" + num + ", " + num + r"\)", rf).groups()))
O3 = ((O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2)
dist = lambda p, q: math.hypot(p[0] - q[0], p[1] - q[1])
assert abs(dist(Tc, O2[:2]) - O2[2]) < 2e-3 and abs(dist(Th, O1[:2]) - O1[2]) < 2e-3, "the contact points lie on their circles"
t = (Th[0] - Tc[0], Th[1] - Tc[1])
assert abs(t[0] * (Tc[0] - O2[0]) + t[1] * (Tc[1] - O2[1])) / (math.hypot(*t) * O2[2]) < 2e-3 and abs(t[0] * (Th[0] - O1[0]) + t[1] * (Th[1] - O1[1])) / (math.hypot(*t) * O1[2]) < 2e-3, "l1 is tangent at both"


def reflect(P):
    d = (O2[0] - O1[0], O2[1] - O1[1])
    tt = ((P[0] - O1[0]) * d[0] + (P[1] - O1[1]) * d[1]) / (d[0] ** 2 + d[1] ** 2)
    F = (O1[0] + tt * d[0], O1[1] + tt * d[1])
    return (2 * F[0] - P[0], 2 * F[1] - P[1])


Th_r, Tc_r = reflect(Th), reflect(Tc)
assert dist(Th_r, (6.6167, 0.3767)) < 0.01, "S1's number for the reflection of Th equals the formula on these coordinates"
assert dist(Tc_r, (4.9316, -6.1025)) < 0.02, "S6's number for the reflection of Tc equals the formula on these coordinates"
assert "(6.6167, 0.3767)" in s1["rejf"] and "(4.9316, -6.1025)" in row("olm124", "b2_j07")["rejf"]
dTc, dTh = dist(O3, Tc), dist(O3, Th)
assert abs(dTc - dTh) < 1e-3, "apex: |O3Tc| = |O3Th| on these coordinates"
geo = {"O1": O1[:2], "r1": O1[2], "O2": O2[:2], "r2": O2[2], "Tc": Tc, "Th": Th, "O3": O3, "Th_r": [round(v, 4) for v in Th_r], "Tc_r": [round(v, 4) for v in Tc_r],
       "dTc": round(dTc, 4), "dTh": round(dTh, 4), "mid_TcTh": [round((Tc[0] + Th[0]) / 2, 4), round((Tc[1] + Th[1]) / 2, 4)], "gap_mid_O3": round(dist(((Tc[0] + Th[0]) / 2, (Tc[1] + Th[1]) / 2), O3), 4),
       "gap_refl": round(dist(Th_r, Tc), 4), "src": "olm125 b1_j17 head + rej6_first"}

pack = {
    "inventory": {"md5": md5(INV), "made": inv["made"], "commit": inv["commit"], "out_tail": "json md5 3190663eadc56b6ea426472b0551624e size 737773"},
    "read_prov": {f"olm{n}": {"commit": READ[n]["provenance"]["commit"], "dirty": READ[n]["provenance"]["dirty"], "md5": md5(HERE / "data" / "read" / f"olm{n}.json")} for n in READ},
    "prompts": {"formula": inv["prompts"]["TOOL_D(式だけ・olm122/124)"], "second": inv["prompts"]["SECOND(宣言の文・olm119)"], "decl": inv["prompts"]["TOOL(式 + 宣言の文・olm119)"], "use": inv["prompts"]["TOOL_U(指示の文・olm125/127)"], "md5": inv["prompts"]["prompt_md5"]},
    "arms": arms, "verdicts": VERD, "gates": gates, "g075": G["g075"], "g080": G["old"]["g080"],
    "frozen": {"o118": {"Q1": [r118["Q1"]["diff"], r118["Q1"]["verdict"]], "Q2": [r118["Q2"]["diff"], r118["Q2"]["verdict"]], "Q3": [r118["Q3"]["diff"], r118["Q3"]["verdict"]]},
               "o119": {"Q1": [r119["Q1"]["diff"], r119["Q1"]["verdict"]], "Q2": [r119["Q2"]["REFL_CALC_rate"], r119["Q2"]["verdict"]]},
               "o124": {"Q1": [r124["Q1"]["diff_vs_olm113"], r124["Q1"]["verdict"]], "Q2": [r124["Q2"]["REFL_CALC_rate"], r124["Q2"]["verdict"]]},
               "o125": {"Q1": [r125["Q1"]["diff_vs_olm124"], r125["Q1"]["verdict"]], "Q2": [r125["Q2"]["REFL_CALC_rate"], r125["Q2"]["verdict"]]},
               "o127": {"Q1": [r127["Q1"]["LN_a_rate_proof"]["rerun"], r127["Q1"]["verdict"]], "Q2": [r127["Q2"]["REFL_CALC_rate"], r127["Q2"]["verdict"]], "pool": r127.get("pool_120", inv["frozen"]["olm127"]["pool_120"])}},
    "lineage": lineage, "cases": cases, "v6_added": v6_added, "v6_dropped": v6_dropped, "scenes": SC, "geo": geo, "q3_118": q3,
    "quoted": {"fisher": Q["fisher"], "fisher127": Q["fisher127"], "fisher127_more": {"p119": Q["fisher127_more"]["p119"], "ppool": Q["fisher127_more"]["pool"]["p"]}, "hint": H, "r_equal": Q["radius_equal"]["r"],
               "q3_126": {"ja": Q["q3_126_row"]["text_ja"], "file": Q["q3_126_row"]["file"]}, "apex127": {"keys": APEX["keys"], "b0_j00": APEX["b0_j00"]["literal"], "b2_j09": APEX["b2_j09"]["literal"]}},
    "four": four, "slip0": slip0, "edges": EDGES, "fisher_below": f_below, "fisher": fisher_rows, "fisher_p": [f["p"] for f in fisher_rows], "rej_to_proof_125": Q["rej_to_proof_125"]["keys"], "brief_check": {"n": len(BRIEF), "ok": sum(1 for _, ok in BRIEF if ok)},
    "recount": {"n": len(inv["recount_vs_read_json"]), "ok": sum(c["ok"] for c in inv["recount_vs_read_json"])},
}
pack["pool127"] = r127.get("pool_120", inv["frozen"]["olm127"]["pool_120"])
assert pack["pool127"]["LN_a"] == AR["olm125"]["LN3"] + AR["olm127"]["LN3"] and pack["pool127"]["n_proof"] == AR["olm125"]["n_proof"] + AR["olm127"]["n_proof"]
(OUT / "pack.json").write_text(json.dumps(pack, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"pack: BRIEF §2 {sum(1 for _, ok in BRIEF if ok)} / {len(BRIEF)} · four arms {four['num']} / {four['den']} (old {four['old'][0]} / {four['old'][1]} not kept) · Fisher {[f['p'] for f in fisher_rows]}")
print(f"pack: {len(arms)} arms × 60 rows · LN v3 {[AR[a]['LN3'] for a in ARMS]} / n_proof {[AR[a]['n_proof'] for a in ARMS]} · verdicts {{{', '.join(f'{a}: {v['calc']}' + ('(判定なし)' if a in G1_FAIL else '') for a, v in VERD.items())}}} · geometry gap(refl Th, Tc) {geo['gap_refl']} · apex {geo['dTc']} / {geo['dTh']} · {(OUT / 'pack.json').stat().st_size // 1024} KB")
