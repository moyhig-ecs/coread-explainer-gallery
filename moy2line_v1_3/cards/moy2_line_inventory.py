"""moy-2 の「折り返しの道具」の系列(olm113 M2A・olm117・olm119・olm122・olm124・olm125・olm127)の棚卸し(図解の材料)。
凍結の出力(gen.json・read.json)だけを読み、凍結の述語(olm122 の score_row = v2 + v3 + REFL + v4 + tool_named / olm126 の score_v6・rej6)を読み込むだけで
行ごとの印と腕ごとの数を一つの JSON に書く。判定(帯)は各 read.json の記録を写す(数え直しは照合として assert)。
usage: python3 moy2_line_inventory.py  → moy2_line_inventory.json / .out(照合の値)
"""
from __future__ import annotations
import hashlib, importlib, json, pathlib, re, statistics, subprocess, sys, time, collections

REPO = pathlib.Path("/Users/manabu/lancedb-rag"); EXP = REPO / "ConstructGap/exp"; HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(EXP))
M122 = importlib.import_module("olm122_moy2_reflection_formula_only_20261103")      # frozen: score_row・TOOL_D
M126 = importlib.import_module("olm126_moy2_v6_par_window_ln_object_rej_20261104")  # frozen: score_v6・rej6
M119 = importlib.import_module("olm119_moy2_reflection_tool_line_symmetry_20261103")  # frozen: SECOND(宣言の文)
M125 = importlib.import_module("olm125_moy2_reflection_use_to_check_20261104")       # frozen: TOOL_U(指示の文)
H = M122.H


def md5f(p): return hashlib.md5(pathlib.Path(p).read_bytes()).hexdigest()


ARMS = [  # (arm, label_ja, gen path, read path(判定の記録), rows loader kind)
    ("olm113", "道具なし(M2A)", EXP / "olm113/gen.json", EXP / "olm118/read.json", "arms_M2A"),
    ("olm117", "半径の等しい図(対照)", EXP / "olm117/gen.json", EXP / "olm118/read.json", "batches"),
    ("olm119", "式 + 宣言の文", EXP / "olm119/gen.json", EXP / "olm119/read.json", "batches"),
    ("olm122", "式だけ(一回目・G1 落ち)", EXP / "olm122/gen.json", EXP / "olm122/read.json", "batches"),
    ("olm124", "式だけ(二回目)", EXP / "olm124/gen.json", EXP / "olm124/read.json", "batches"),
    ("olm125", "式 + 指示の文(一回目)", EXP / "olm125/gen.json", EXP / "olm125/read.json", "batches"),
    ("olm127", "式 + 指示の文(二回目)", EXP / "olm127/gen.json", EXP / "olm127/read.json", "batches"),
]


def rows_of(kind, g):
    if kind == "arms_M2A":
        for b in sorted(g["arms"]["M2A"], key=int):
            for j, x in enumerate(g["arms"]["M2A"][b]["rows"]): yield f"b{b}_j{int(x.get('j', j)):02d}", x, g["arms"]["M2A"][b].get("seed")
    else:
        for b in sorted(g["batches"], key=int):
            for x in g["batches"][b]["rows"]: yield f"b{b}_j{int(x['j']):02d}", x, g["batches"][b].get("seed")


def row_record(key, x, seed):
    c = x["content"]; s = M122.score_row(c); proof = s.get("proof") or ""; hp = bool(proof.strip())
    v6 = M126.score_v6(proof) if hp else None; r6 = M126.rej6(c); refl = s["refl"]
    T = x.get("T_tokens"); cap = bool(x.get("hit_cap"))
    rec = {"key": key, "seed": seed, "cls": s["v2"]["cls"], "status": s.get("status"), "T": T, "hit_cap": cap, "answer_first": bool(x.get("answer_first")),
           "conjecture": (s.get("conjecture") or "")[:160], "has_proof": hp, "proof": proof,
           "calc": bool(refl["REFL_CALC"]), "mention": bool(refl["REFL_MENTION"]), "first_calc": refl.get("first_calc"), "tool_named": bool(s.get("tool_named")),
           "proof_v3": {k: bool(s["v3_proof"][k]) for k in ("LN_a", "PT_a", "OUTER_a", "PERP3_a", "PAR3_a", "PBIS3_a", "SYMM")} if hp else None,
           "proof_v3_first": s["v3_proof"]["first"] if hp else None,
           "proof_v6": {k: bool(v6[k]) for k in ("LN6_a", "LN6_r", "OUTER6_a", "PAR6_a", "PERP3_a", "PBIS6_a", "PT_a")} if hp else None,
           "proof_v6_ln_hits": [(f, t, bool(a)) for f, t, a in v6["ln6_hits"]] if hp else [],
           "body_v4": {k: bool(s["v4_body"][k]) for k in ("LN_a", "LN_r", "PT_a", "PT_r", "OUTER4_a", "OUTER4_r")},
           "rej6": bool(r6["REJ6"]), "rej6_first": r6["first"], "rej6_start": r6["start"],
           "head": c[:240].replace("\n", " ⏎ ")}
    rec["rej6_then_proof_LN6"] = bool(rec["rej6"] and hp and v6["LN6_a"])
    return rec


def agg(R):
    P = [r for r in R if r["has_proof"]]; n = len(R)
    cnt = lambda f: sum(1 for r in P if r["proof_v3"][f]); cnt6 = lambda f: sum(1 for r in P if r["proof_v6"][f])
    parsed = sum(1 for r in R if r["cls"] != "NONE"); calc = [r for r in R if r["calc"]]; noncalc = [r for r in R if not r["calc"]]
    def ln_split(S):
        Pp = [r for r in S if r["has_proof"]]; return {"n_proof": len(Pp), "LN_a": sum(1 for r in Pp if r["proof_v3"]["LN_a"]), "LN6_a": sum(1 for r in Pp if r["proof_v6"]["LN6_a"])}
    out = {"n": n, "parsed": parsed, "parsed_rate": round(parsed / n, 4), "status": dict(collections.Counter(r["status"] for r in R)),
           "status_hq_rate": round(sum(r["status"] in ("hypothesis", "question") for r in R) / n, 4),
           "cls": dict(collections.Counter(r["cls"] for r in R)), "MIDO3_rate_parsed": round(sum(r["cls"] == "MIDO3" for r in R) / parsed, 4) if parsed else None,
           "EQ_rate_parsed": round(sum(r["cls"] == "EQ" for r in R) / parsed, 4) if parsed else None,
           "n_proof": len(P), "proof_v3": {f: cnt(f) for f in ("LN_a", "PT_a", "OUTER_a", "PERP3_a", "PAR3_a", "PBIS3_a", "SYMM")},
           "proof_v3_rate": {f: round(cnt(f) / len(P), 4) for f in ("LN_a", "PT_a", "OUTER_a")} if P else None,
           "proof_v6": {f: cnt6(f) for f in ("LN6_a", "OUTER6_a", "PAR6_a", "PERP3_a", "PBIS6_a", "PT_a")},
           "proof_v6_rate": {f: round(cnt6(f) / len(P), 4) for f in ("LN6_a", "OUTER6_a")} if P else None,
           "REFL_CALC": len(calc), "REFL_CALC_rate": round(len(calc) / n, 4), "REFL_MENTION": sum(1 for r in R if r["mention"]), "tool_named": sum(1 for r in R if r["tool_named"]),
           "REJ6": sum(1 for r in R if r["rej6"]), "REJ6_in_calc": sum(1 for r in calc if r["rej6"]), "REJ6_then_proof_LN6": [r["key"] for r in R if r["rej6_then_proof_LN6"]],
           "calc_cls": dict(collections.Counter(r["cls"] for r in calc)), "calc_T_median": statistics.median([r["T"] for r in calc]) if calc else None,
           "noncalc_T_median": statistics.median([r["T"] for r in noncalc]) if noncalc else None, "T_median": statistics.median([r["T"] for r in R]),
           "hit_cap": sum(1 for r in R if r["hit_cap"]), "calc_split": ln_split(calc), "noncalc_split": ln_split(noncalc),
           "unparsed": [{"key": r["key"], "T": r["T"], "hit_cap": r["hit_cap"], "calc": r["calc"], "head": r["head"][:200]} for r in R if r["cls"] == "NONE"],
           "body_v4": {f: sum(1 for r in R if r["body_v4"][f]) for f in ("LN_a", "LN_r", "PT_a", "PT_r", "OUTER4_a", "OUTER4_r")}}
    return out


def frozen_verdicts():
    """各 read.json の判定の記録(写すだけ)"""
    o18 = json.loads((EXP / "olm118/read.json").read_text()); o19 = json.loads((EXP / "olm119/read.json").read_text()); o22 = json.loads((EXP / "olm122/read.json").read_text())
    o24 = json.loads((EXP / "olm124/read.json").read_text()); o25 = json.loads((EXP / "olm125/read.json").read_text()); o26 = json.loads((EXP / "olm126/read.json").read_text())
    v = {"olm118(olm117 vs olm113)": {"Q1_LN": o18["Q1"], "Q2_PT": o18["Q2"], "Q3_OUTER": o18["Q3"], "gates": o18["gates"]},
         "olm119": {"gates": o19["gates"], "Q1": o19["Q1"], "Q2": o19.get("Q2")},
         "olm122": {"gates": o22["gates"], "Q1": o22["Q1"], "Q2": o22["Q2"], "parsed": o22["Q4_desc"]["formula_only"]["parsed"]},
         "olm124": {"gates": o24["gates"], "Q1": o24["Q1"], "Q2": o24["Q2"]},
         "olm125": {"gates": o25["gates"], "Q1": o25["Q1"], "Q2": o25["Q2"]},
         "olm126(v6)": {"gates": o26["gates"], "Q1": {k: o26["Q1"][k] for k in ("olm118_Q3_OUTER", "verdict")}, "Q2": {k: o26["Q2"][k] for k in ("LN6_rate_proof", "LN_rate_proof(v3)", "frozen", "v6", "verdict")},
                        "Q3": {k: o26["Q3"][k] for k in ("REJ6_counts", "REJ6_then_LN6", "verdict", "missing(残るべきで落ちた)")}, "calibration_n": o26["calibration_n"]}}
    p27 = EXP / "olm127/read.json"
    if p27.exists():
        o27 = json.loads(p27.read_text()); v["olm127"] = {"gates": o27["gates"], "Q1": o27["Q1"], "Q2": o27["Q2"], "pool_120": o27["Q3_desc"].get("pool_120(参考)")}
    return v


def main():
    t0 = time.time(); inv = {"made": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "commit": subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip(),
                            "inputs": {}, "parts": {k: md5f(m.__file__) for k, m in (("olm122", M122), ("olm126", M126), ("olm119", M119), ("olm125", M125))},
                            "prompts": {}, "arms": {}, "frozen": frozen_verdicts(), "scenes": {}, "checks": []}
    # 問いの文の段(逐語)
    inv["prompts"] = {"TOOL_D(式だけ・olm122/124)": M122.TOOL_D, "SECOND(宣言の文・olm119)": M122.SECOND, "TOOL(式 + 宣言の文・olm119)": M119.TOOL,
                      "TOOL_U(指示の文・olm125/127)": M125.TOOL_U,
                      "prompt_md5": {"olm122/124": H.md5(M122.olmo_prompt()), "olm125/127": H.md5(M125.olmo_prompt())}}
    for arm, label, gpath, rpath, kind in ARMS:
        if not gpath.exists() or not rpath.exists(): inv["checks"].append(f"{arm}: skipped (no output yet)"); continue
        g = json.loads(gpath.read_text()); inv["inputs"][str(gpath.relative_to(REPO))] = md5f(gpath); inv["inputs"][str(rpath.relative_to(REPO))] = md5f(rpath)
        R = [row_record(k, x, seed) for k, x, seed in rows_of(kind, g)]
        A = agg(R); inv["arms"][arm] = {"label": label, "prompt_md5": g.get("prompt_md5"), "agg": A, "rows": R}
        inv["checks"].append(f"{arm}: n {A['n']} parsed {A['parsed']} n_proof {A['n_proof']} LN_a {A['proof_v3']['LN_a']} LN6_a {A['proof_v6']['LN6_a']} REFL_CALC {A['REFL_CALC']} REJ6 {A['REJ6']} typ {len(A['REJ6_then_proof_LN6'])}")
    # 照合(各 read.json の記録と数え直しの一致)
    fz = inv["frozen"]; ck = []
    def eq(name, a, b): ck.append({"check": name, "recount": a, "read_json": b, "ok": a == b})
    if "olm119" in inv["arms"]: eq("olm119 LN_a rate", inv["arms"]["olm119"]["agg"]["proof_v3_rate"]["LN_a"], fz["olm119"]["Q1"]["LN_a_rate_proof"]["tool"])
    if "olm124" in inv["arms"]: eq("olm124 LN_a rate", inv["arms"]["olm124"]["agg"]["proof_v3_rate"]["LN_a"], fz["olm124"]["Q1"]["LN_a_rate_proof"]["rerun"]); eq("olm124 REFL_CALC rate", inv["arms"]["olm124"]["agg"]["REFL_CALC_rate"], fz["olm124"]["Q2"]["REFL_CALC_rate"])
    if "olm125" in inv["arms"]: eq("olm125 LN_a rate", inv["arms"]["olm125"]["agg"]["proof_v3_rate"]["LN_a"], fz["olm125"]["Q1"]["LN_a_rate_proof"]["use"]); eq("olm125 REFL_CALC rate", inv["arms"]["olm125"]["agg"]["REFL_CALC_rate"], fz["olm125"]["Q2"]["REFL_CALC_rate"])
    if "olm122" in inv["arms"]: eq("olm122 parsed", inv["arms"]["olm122"]["agg"]["parsed"], fz["olm122"]["parsed"])
    for arm in ("olm113", "olm119", "olm122", "olm124", "olm125"):
        if arm in inv["arms"]: eq(f"{arm} LN6 rate (olm126)", inv["arms"][arm]["agg"]["proof_v6_rate"]["LN6_a"], fz["olm126(v6)"]["Q2"]["LN6_rate_proof"][arm]); eq(f"{arm} REJ6 (olm126)", inv["arms"][arm]["agg"]["REJ6"], fz["olm126(v6)"]["Q3"]["REJ6_counts"][arm])
    if "olm127" in inv["arms"] and "olm127" in fz: eq("olm127 LN_a rate", inv["arms"]["olm127"]["agg"]["proof_v3_rate"]["LN_a"], fz["olm127"]["Q1"]["LN_a_rate_proof"]["rerun"]); eq("olm127 REFL_CALC rate", inv["arms"]["olm127"]["agg"]["REFL_CALC_rate"], fz["olm127"]["Q2"]["REFL_CALC_rate"])
    if "olm113" in inv["arms"]: eq("olm113 LN_a rate (olm118)", inv["arms"]["olm113"]["agg"]["proof_v3_rate"]["LN_a"], fz["olm118(olm117 vs olm113)"]["Q1_LN"]["LN_a_rate_proof"]["olm113"])
    if "olm117" in inv["arms"]: eq("olm117 LN_a rate (olm118)", inv["arms"]["olm117"]["agg"]["proof_v3_rate"]["LN_a"], fz["olm118(olm117 vs olm113)"]["Q1_LN"]["LN_a_rate_proof"]["olm117"])
    inv["recount_vs_read_json"] = ck
    # 場面(述語で選ぶ・名指しは記録)
    def find(arm, key): return next(r for r in inv["arms"][arm]["rows"] if r["key"] == key)
    sc = {}
    if "olm125" in inv["arms"]:
        sc["S1_rej_then_LN(olm125 b1_j17)"] = {"pred": "rej6 ∧ proof_v6.LN6_a", "row": find("olm125", "b1_j17")}
        sc["S2_rej_then_noLN(olm125 b0_j16)"] = {"pred": "rej6 ∧ has_proof ∧ ¬proof_v6.LN6_a", "row": find("olm125", "b0_j16")}
        sc["S3_reason_then_cap(olm125 b1_j16)"] = {"pred": "calc ∧ hit_cap ∧ 'not necessarily true unless the circles are congruent' in content", "row": find("olm125", "b1_j16")}
        sc["S4_hint_reading(olm125 b1_j09)"] = {"pred": "¬calc ∧ mention ∧ proof_v3.LN_a=False ∧ 'likely relates to the symmetry' in content", "row": find("olm125", "b1_j09")}
        sc["S5_echo(olm125 b0_j18)"] = {"pred": "'Use it to check' in content", "row": find("olm125", "b0_j18")}
    if "olm124" in inv["arms"]: sc["S6_rej_then_LN(olm124 b2_j07)"] = {"pred": "rej6 ∧ proof_v6.LN6_a", "row": find("olm124", "b2_j07")}
    if "olm119" in inv["arms"]: sc["S7_declared(olm119 b1_j06)"] = {"pred": "rej6 ∧ proof_v6.LN6_a", "row": find("olm119", "b1_j06")}
    if "olm127" in inv["arms"]:
        g27 = json.loads((EXP / "olm127/gen.json").read_text()); c27 = {k: x["content"] for k, x, _ in rows_of("batches", g27)}
        sc["S8_reject_then_same_candidate_loop(olm127 b2_j08)"] = {"pred": "cls NONE ∧ hit_cap ∧ ¬calc ∧ 'the determinant is not zero' in content", "row": find("olm127", "b2_j08"),
                                                                   "loop_phrase": "But as above, the determinant is not zero", "loop_count": c27["b2_j08"].count("But as above, the determinant is not zero")}
        sc["S9_numeric_proof_apex(olm127 b2_j09)"] = {"pred": "cls EQ ∧ calc ∧ ¬rej6 ∧ 'sqrt(14.764)' in proof", "row": find("olm127", "b2_j09")}
        sc["S10_already_checked_loop(olm127 b1_j13)"] = {"pred": "cls NONE ∧ hit_cap ∧ calc ∧ 'but already checked' in content", "row": find("olm127", "b1_j13"),
                                                          "loop_phrase": "but already checked", "loop_count": c27["b1_j13"].count("but already checked")}
    inv["scenes"] = sc
    # 計器の系譜(olm126 Q1)
    o26 = json.loads((EXP / "olm126/read.json").read_text()); inv["instrument_lineage"] = {"olm118_Q3_OUTER_by_version": o26["Q1"]["olm118_Q3_OUTER"], "calibration": {"v3": 54, "v4": 74, "v5": 98, "v6": o26["calibration_n"]}, "negative_control_prf5": o26["gates"]}
    out = HERE / "moy2_line_inventory.json"; out.write_text(json.dumps(inv, ensure_ascii=False, indent=1) + "\n")
    lines = [f"made {inv['made']} commit {inv['commit']} wall {time.time() - t0:.1f}s", "inputs:"] + [f"  {k} {v}" for k, v in inv["inputs"].items()] + ["checks:"] + inv["checks"] + ["recount vs read.json:"] + [f"  [{'ok' if c['ok'] else 'NG'}] {c['check']}: {c['recount']} vs {c['read_json']}" for c in ck]
    for arm, a in inv["arms"].items():
        A = a["agg"]; lines.append(f"{arm} {a['label']}: parsed {A['parsed']}/{A['n']} n_proof {A['n_proof']} LN_a {A['proof_v3']['LN_a']} ({A['proof_v3_rate']['LN_a']}) LN6_a {A['proof_v6']['LN6_a']} ({A['proof_v6_rate']['LN6_a']}) OUTER_a {A['proof_v3']['OUTER_a']} OUTER6_a {A['proof_v6']['OUTER6_a']} PT_a {A['proof_v3']['PT_a']} MIDO3 {A['MIDO3_rate_parsed']} EQ {A['EQ_rate_parsed']} calc {A['REFL_CALC']} ({A['REFL_CALC_rate']}) REJ6 {A['REJ6']} (in calc {A['REJ6_in_calc']}) typ {A['REJ6_then_proof_LN6']} tool_named {A['tool_named']} cap {A['hit_cap']} T_med {A['T_median']} calc/noncalc LN_a {A['calc_split']} / {A['noncalc_split']}")
    (HERE / "moy2_line_inventory.out").write_text("\n".join(lines) + "\n"); print("\n".join(lines)); print("json md5", md5f(out), "size", out.stat().st_size)


if __name__ == "__main__": main()
