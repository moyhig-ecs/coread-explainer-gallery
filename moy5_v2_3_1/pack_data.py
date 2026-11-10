"""pack_data.py — the FIRST route of every number (moy-5: the routes to the apex = the mean proportional).
Reads ONLY the frozen outputs named in BRIEF v1 §1 (jsonl rows with their full `raw`, and a few .md / .txt files read as text) and writes generated/pack.json.
Never imports or runs an experiment's script (the b5bp runner is read as TEXT for the β′ constant). No model, no network, no git writes.
Every count is a count of the data's own fields (`bind`, `cut_in_conjecture`, `closure` / `floor`, `route5`, `lat_sym`, `fd_use`, `malformed`, `form_focal`, `form_vertex`, `thinking`): the reader is not run again.
    python -I pack_data.py
"""
import hashlib
import json
import math
import pathlib
import re
import statistics

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(__import__("os").environ.get("MOY5_REPO", HERE / "data"))   # bundle: the frozen files are copied under data/ at their repo paths (MOY5_REPO = another root, e.g. the house repo)
X = REPO / "ConstructGap" / "exp"
C = REPO / "conversations"
OUT = HERE / "generated"
OUT.mkdir(exist_ok=True)

# ---- the md5 prefixes of BRIEF v1 §1-2 (a file that does not match is not the frozen one: stop)
MD5 = {
    "results_essay4_moy5_20261014_claude-opus-5-5_a.jsonl": "ba48de9c", "results_essay4_moy5_20261014_claude-fable-5-1_a.jsonl": "580206dc",
    "results_essay4_moy5_20261014_claude-sonnet-5-5_a.jsonl": "68d9fcc3", "results_essay4_moy5_20261014_claude-haiku-5-5_a.jsonl": "d50cd49e",
    "results_essay4_moy5_20261014_claude-haiku-5-5_r.jsonl": "0f08d497",
    "results_essay4_moy5_20261014_claude-opus-5-5_r.jsonl": "d41d8cd9", "results_essay4_moy5_20261014_claude-fable-5-1_r.jsonl": "d41d8cd9", "results_essay4_moy5_20261014_claude-sonnet-5-5_r.jsonl": "d41d8cd9",
    "results_b5bp_20261014_claude-opus-5-5_a.jsonl": "d589e2bb", "results_b5bp_20261014_claude-sonnet-5-5_a.jsonl": "5051e5a1", "results_b5bp_20261014_claude-fable-5-1_a.jsonl": "960afdbb",
    "results_moy5c_20261015.jsonl": "c616f21a", "results_arg5_20261016_gemini-4-argon_a.jsonl": "1c7ee8be", "results_arg5d_20261016_gemini-4-argon_a.jsonl": "04af6068",
    "results_neq3_moy5_20261019_claude-opus-5-5.jsonl": "b49fcad2", "results_neq3_moy5_20261019_claude-fable-5-1.jsonl": "8585a2a8", "results_neq2f_moy5_20261019.jsonl": "f54d5897",
    "results_neq6_moy5_20261019_claude-opus-5-5.jsonl": "a957c784", "results_neq6_moy5_20261019_claude-fable-5-1.jsonl": "37bd5ab7",
    "results_prf1_20261021.jsonl": "8880f1b7", "results_prf3_20261021.jsonl": "3fa335be",
    "results_mnw1_moy5_20261022_claude-opus-5-5.jsonl": "d9de546a", "results_mnw1_moy5_20261022_claude-fable-5-1.jsonl": "aa494c4c",
    "results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl": "700bef16", "results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl": "84eb74a0",
    "results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl": "f7133073", "results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl": "83abd34c",
    "results_rte1_20261015_api_max.jsonl": "3e0b14f7", "results_rte1_20261015_cc_high.jsonl": "03441ed2",
}
DOCS = {  # read as text (the SUMMARY's data table and the sentences added to the question)
    "summary_txt": ("2026-10-16/data_moy5_summary/summary_table_moy5_cut_all_cards_20261016.txt", "556b9dfb"),
    "summary": ("2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md", "39b74e9a"),
    "source": ("2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md", "574ea5c5"),
}
md5_of = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
FILES = {}
for f, pre in MD5.items():
    h = md5_of(X / f)
    assert h.startswith(pre), f"{f}: md5 {h} is not the frozen {pre}"
    FILES[f] = h
for k, (f, pre) in DOCS.items():
    h = md5_of(C / f)
    assert h.startswith(pre), f"{f}: md5 {h} is not {pre}"
    FILES[f] = h


def rows(f):
    with open(X / f, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


SHORT = {"claude-opus-5-5": "Opus 5.5", "claude-fable-5-1": "Fable 5.1", "claude-sonnet-5-5": "Sonnet 5.5", "claude-haiku-5-5": "Haiku 5.5", "gemini-4-argon": "Argon"}


def path_of(r):
    """API (a Messages / Gemini request with req_opts) or `claude -p` (a Claude Code result: num_turns). Read from the row, not typed."""
    if "num_turns" in r:
        return "cc"
    if r.get("req_opts") is not None:
        return "api"
    raise AssertionError(f"no path for {r.get('card')} {r.get('arm')} {r.get('rep')}")


def effort_of(r):
    o = r.get("req_opts") or {}
    if isinstance(o, dict):
        if isinstance(o.get("output_config"), dict) and o["output_config"].get("effort"):
            return o["output_config"]["effort"]
        if o.get("effort"):
            return o["effort"]
        gc = o.get("generationConfig")
        if isinstance(gc, dict):
            tc = gc.get("thinkingConfig")
            return ("thinking " + tc["thinkingLevel"].lower()) if tc else "thinking default"
    return r.get("effort")


# ---- one CELL = one model x one arm of one card. `dots` = one code per drawn row, in rep order (the unit chart: one dot = one answer).
#   kind "cut":  A = a cut in the answer field (cut_in_conjecture) · R = a cut only in the reason field (bind and not cut_in_conjecture) · F = no cut, the floor stated (closure) · N = neither
#   kind "prf1": E = END-only · C = CHAIN · L = LAT-only · N = none            (route5 of prf1)
#   kind "prf3": S = LAT_SYM · D = FD_USE · M = malformed (no JSON answer) · N = neither · a trailing "m" = LAT_SYM in a row that also carries the malformed mark (Opus P5B r4)
#   kind "olm":  F = the floor stated · N = not · Z = an empty row (0 tokens; kept in the denominator = the number drawn, olm1 RESULT §1)
CELLS = {}


def cell(cid, card, files, model, arm, kind="cut", where=None, keep_raw_only=True, effort=None, path=None, label=None):
    rs = []
    for f in files:
        rs += [dict(r, _file=f) for r in rows(f)]
    rs = [r for r in rs if (model is None or r.get("model") == model) and r.get("arm") == arm and (where is None or where(r))]
    if keep_raw_only:
        rs = [r for r in rs if r.get("raw")]
    keys = [(r["_file"], r["rep"]) for r in rs]
    assert len(set(keys)) == len(keys), f"{cid}: a (file, rep) twice"
    reps = [r["rep"] for r in rs]
    assert len(set(reps)) == len(reps), f"{cid}: the same rep twice across files (mnw1 + mnw1b must not overlap)"
    rs.sort(key=lambda r: r["rep"])
    dots, n = [], len(rs)
    cnt = {}
    if kind == "cut":
        for r in rs:
            assert not (r.get("cut_in_conjecture") and not r.get("bind")), f"{cid}: an answer-field cut without bind"
            dots.append("A" if r.get("cut_in_conjecture") else "R" if r.get("bind") else "F" if r.get("closure") else "N")
        cnt = {"bind": sum(bool(r.get("bind")) for r in rs), "ans": sum(bool(r.get("cut_in_conjecture")) for r in rs), "floor": sum(bool(r.get("closure")) for r in rs)}
        if any("form_focal" in r for r in rs):
            cnt.update(focal=sum(bool(r.get("form_focal")) for r in rs), vertex=sum(bool(r.get("form_vertex")) for r in rs))
            cnt["marks"] = [("F" if r.get("form_focal") else "") + ("V" if r.get("form_vertex") else "") for r in rs]     # per row: the focal form / the vertex form (symptoma) of the lattice (mnw1 RESULT §1)
        if any("parabola_in_conjecture" in r for r in rs):
            cnt["parabola_ans"] = sum(bool(r.get("parabola_in_conjecture")) for r in rs)
            cnt["parabola_and_cut"] = sum(bool(r.get("parabola_in_conjecture")) and bool(r.get("cut_in_conjecture")) for r in rs)   # v2.1 ⑤: the rows that wrote both in the answer field (D1 R2 D-14)
        th = [r["thinking"] if "thinking" in r else (r.get("usage") or {}).get("output_tokens_details", {}).get("thinking_tokens") for r in rs]
        if all(isinstance(t, (int, float)) for t in th) and th:
            cnt["thinking_med"] = statistics.median(th)
        rt = [r.get("reasoning_tokens") for r in rs]          # v2 (P's state 13 moved here): the API rows carry `reasoning_tokens`; the median is the mean of the two middle rows (n 20)
        if rt and all(isinstance(t, (int, float)) for t in rt):
            cnt["reasoning_med"] = statistics.median(rt)
            cnt["reasoning_med_high"] = statistics.median_high(rt)   # the SUMMARY §6 table's value turned out to be this one (the upper of the two middle rows): disclosed, not drawn
        rl = [r.get("relations") for r in rs]                   # v2.1 (P's s14 moved: R3 D-11): the relations the reader v2 lists per answer, counted from the rows (median = mean of the two middle rows)
        if rl and all(isinstance(t, list) for t in rl):
            cnt["relations_med"] = statistics.median(len(t) for t in rl)
            cnt["relations_med_high"] = statistics.median_high(len(t) for t in rl)
    elif kind == "olmk":   # v2: OLMo on the positive control K (kept: empty rows = Z, in the denominator, like kind "olm"). A = answer-field cut · R = whole only · F = floor · N = neither
        for r in rs:
            dots.append("Z" if not r.get("raw") or ("conjecture" not in r and not r.get("ok")) else "A" if r.get("cut_in_conjecture") else "R" if r.get("bind") else "F" if r.get("closure") else "N")
        cnt = {"floor": sum(bool(r.get("closure")) for r in rs), "ans": sum(bool(r.get("cut_in_conjecture")) for r in rs), "bind": sum(bool(r.get("bind")) for r in rs), "empty": dots.count("Z")}
    elif kind == "prf1":
        code = {"END-only": "E", "CHAIN": "C", "LAT-only": "L", "none": "N"}
        dots = [code[r["route5"]] for r in rs]
        cnt = {k: sum(r["route5"] == k for r in rs) for k in code}
        cnt["floor"] = sum(bool(r.get("floor")) for r in rs)
    elif kind == "prf3":
        for r in rs:
            assert not (r["lat_sym"] and r["fd_use"]), f"{cid}: LAT_SYM and FD_USE in one row"
            d = "S" if r["lat_sym"] else "M" if r["malformed"] else "D" if r["fd_use"] else "N"
            if r["lat_sym"] and r["malformed"]:
                d = "Sm"
            dots.append(d)
        ok = [r for r in rs if not r["malformed"]]
        cnt = {"lat_sym": sum(bool(r["lat_sym"]) for r in rs), "fd_use": sum(bool(r["fd_use"]) for r in rs), "malformed": sum(bool(r["malformed"]) for r in rs),
               "lat_sym_ok": sum(bool(r["lat_sym"]) for r in ok), "n_ok": len(ok), "floor": sum(bool(r.get("floor")) for r in rs)}
    elif kind == "olm":
        for r in rs:
            dots.append("Z" if not r.get("raw") or ("conjecture" not in r and not r.get("ok")) else "F" if r.get("closure") else "N")
        cnt = {"floor": sum(bool(r.get("closure")) for r in rs), "ans": sum(bool(r.get("cut_in_conjecture")) for r in rs), "bind": sum(bool(r.get("bind")) for r in rs),
               "empty": dots.count("Z")}
    paths = {path or path_of(r) for r in rs} if kind not in ("olm", "olmk") else {"local"}
    efforts = {effort or effort_of(r) for r in rs}
    assert len(paths) == 1 and len(efforts) == 1, f"{cid}: one path and one effort per cell ({paths}, {efforts})"
    CELLS[cid] = {"id": cid, "card": card, "files": files, "model": SHORT.get(model, model), "arm": arm, "kind": kind, "n": n, "dots": dots, "reps": [r["rep"] for r in rs],
                  "path": paths.pop(), "effort": efforts.pop(), "label": label or arm, **cnt}
    return CELLS[cid]


E4 = lambda m: [f"results_essay4_moy5_20261014_claude-{m}_a.jsonl", f"results_essay4_moy5_20261014_claude-{m}_r.jsonl"]
for m, mm in [("opus-5-5", "claude-opus-5-5"), ("fable-5-1", "claude-fable-5-1"), ("sonnet-5-5", "claude-sonnet-5-5"), ("haiku-5-5", "claude-haiku-5-5")]:
    cell(f"essay4.A.{m}", "essay4", E4(m), mm, "A")
    cell(f"essay4.K.{m}", "essay4", E4(m), mm, "K")
MN = lambda m: [f"results_mnw1_moy5_20261022_{m}.jsonl", f"results_mnw1b_moy5_20261022_{m}.jsonl"]
for mm in ["claude-opus-5-5", "claude-fable-5-1"]:
    s = mm.split("-")[1]
    for arm in ["K", "none/Q1", "none/Q1f", "conf/Q1", "conf/Q1f", "cone/Q1", "cone/Q1f"]:
        cell(f"mnw1.{arm}.{s}", "mnw1", MN(mm), mm, arm)
for arm in ["A", "K", "L-name", "L-text", "A/Q2", "K/Q2", "L-name/Q2", "L-text/Q2"]:
    cell(f"neq3.{arm}.opus", "neq3", ["results_neq3_moy5_20261019_claude-opus-5-5.jsonl"], "claude-opus-5-5", arm)
for arm in ["A/Q2", "K/Q2", "L-name/Q2", "L-text/Q2"]:
    cell(f"neq3.{arm}.fable", "neq3", ["results_neq3_moy5_20261019_claude-fable-5-1.jsonl"], "claude-fable-5-1", arm)
for arm in ["A", "K", "L-name", "L-text"]:   # neq2f = Fable on Q1; the rows carry no effort field: xhigh is read from the RESULT's title (anchor X_neq2f_xhigh)
    cell(f"neq2f.{arm}.fable", "neq2f", ["results_neq2f_moy5_20261019.jsonl"], "claude-fable-5-1", arm, effort="xhigh")
for s, mm in [("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")]:
    for e in ["medium", "high", "max"]:
        cell(f"neq6.{e}.{s}", "neq6", [f"results_neq6_moy5_20261019_{mm}.jsonl"], mm, f"A/Q2@{e}")
    cell(f"neq6.K.{s}", "neq6", [f"results_neq6_moy5_20261019_{mm}.jsonl"], mm, "K/Q2@medium")
for m, mm in [("opus-5-5", "claude-opus-5-5"), ("sonnet-5-5", "claude-sonnet-5-5"), ("fable-5-1", "claude-fable-5-1")]:
    cell(f"b5bp.Bbp.{m}", "b5bp", [f"results_b5bp_20261014_claude-{m}_a.jsonl"], mm, "Bbp")
for mm in ["claude-opus-5-5", "claude-fable-5-1"]:
    s = mm.split("-")[1]
    cell(f"moy5c.{s}", "moy5c", ["results_moy5c_20261015.jsonl"], mm, "P-none")
    cell(f"rte1.api_max.{s}", "rte1", ["results_rte1_20261015_api_max.jsonl"], mm, "Bbp")
    cell(f"rte1.cc_high.{s}", "rte1", ["results_rte1_20261015_cc_high.jsonl"], mm, "P-none")
    cell(f"prf1.P5.{s}", "prf1", ["results_prf1_20261021.jsonl"], mm, "P5", kind="prf1")
    cell(f"prf1.P5K.{s}", "prf1", ["results_prf1_20261021.jsonl"], mm, "P5K", kind="prf1")
    cell(f"prf3.P5.{s}", "prf3", ["results_prf3_20261021.jsonl"], mm, "P5", kind="prf3")
    cell(f"prf3.P5B.{s}", "prf3", ["results_prf3_20261021.jsonl"], mm, "P5B", kind="prf3")
for arm in ["A", "Bbp", "K", "E-full", "E-full+Bbp"]:
    cell(f"arg5.{arm}", "arg5", ["results_arg5_20261016_gemini-4-argon_a.jsonl"], "gemini-4-argon", arm)
for arm in ["Bbp", "K"]:
    cell(f"arg5d.{arm}", "arg5d", ["results_arg5d_20261016_gemini-4-argon_a.jsonl"], "gemini-4-argon", arm)
OLM1 = "results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl"
for v in ["natural", "think"]:
    cell(f"olm1.{v}", "olm1", [OLM1], None, "none/Q1", kind="olm", where=lambda r, v=v: r.get("variant") == v, keep_raw_only=False, effort="temp 0.7", label=v)
cell("olm3.think", "olm3", ["results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl"], None, "none/Q1", kind="olm", keep_raw_only=False, effort="temp 0.6", label="B1")
for k in ["olm1.natural", "olm1.think"]:
    CELLS[k]["model"] = "OLMo-3 32B base"
CELLS["olm3.think"]["model"] = "OLMo-3 32B Think"
# the mnw1 Fable cone/Q1f is INCOMPLETE (11 / 20, mnw1 RESULT §6): the pack marks it, the page says it
CELLS["mnw1.cone/Q1f.fable"]["incomplete"] = True
# ---- v2 (station 3, the cells moved from entry P after the two readers agreed): the Q1 positive control K (neq3 Opus / neq2f Fable) and OLMo on K (olm1 / olm3)
#   (neq3.K.opus and neq2f.K.fable are already cells of v1: only the figure did not draw them)
for v in ["natural", "think"]:
    cell(f"olm1.{v}.K", "olm1", [OLM1], None, "K", kind="olmk", where=lambda r, v=v: r.get("variant") == v, keep_raw_only=False, effort="temp 0.7", label=f"{v} · K")
    CELLS[f"olm1.{v}.K"]["model"] = "OLMo-3 32B base"
cell("olm3.K", "olm3", ["results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl"], None, "K", kind="olmk", keep_raw_only=False, effort="temp 0.6", label="B1 · K")
CELLS["olm3.K"]["model"] = "OLMo-3 32B Think"
# the olm1 banner (10-27 audit A1): think K r3 wrote the cut in its answer JSON, the reader emptied the conjecture on a bad escape -> the RULE count of the answer field is 0 / 10, the READING is 1 / 10. bind (whole) is not touched.
_r3 = next(r for r in rows(OLM1) if r.get("variant") == "think" and r.get("arm") == "K" and r.get("rep") == 3)
assert _r3.get("bind") is True and not _r3.get("cut_in_conjecture") and "FP_x^2 = FV" in _r3["raw"], "olm1 banner: think K r3 is the row the banner names"
CELLS["olm1.think.K"]["banner_rep"] = 3
# parabola (locus) in the answer field, the Q2 cells (neq3 carries `parabola_in_conjecture`; neq2f does not)
TRAJ = {cid: CELLS[cid].get("parabola_ans") for cid in ["neq3.A/Q2.opus", "neq3.A/Q2.fable", "neq3.L-name/Q2.opus", "neq3.L-text/Q2.opus", "neq3.L-name/Q2.fable", "neq3.L-text/Q2.fable", "neq3.K/Q2.opus", "neq3.K/Q2.fable"]}
assert TRAJ == {"neq3.A/Q2.opus": 20, "neq3.A/Q2.fable": 5, "neq3.L-name/Q2.opus": 2, "neq3.L-text/Q2.opus": 0, "neq3.L-name/Q2.fable": 0, "neq3.L-text/Q2.fable": 1, "neq3.K/Q2.opus": 4, "neq3.K/Q2.fable": 0}, TRAJ

# ---- BRIEF v1 §6: the values the execution layer read (if a value differs, the data wins and the build stops here to say so)
def eq(cid, **kw):
    c = CELLS[cid]
    for k, v in kw.items():
        assert c[k] == v, f"BRIEF §6: {cid}.{k} = {c[k]} (brief {v})"


for m in ["opus-5-5", "fable-5-1", "sonnet-5-5"]:
    eq(f"essay4.A.{m}", bind=0, floor=20, n=20)
eq("essay4.A.haiku-5-5", bind=0, floor=19, n=19)                                            # V1 (_a 16 + _r 3)
eq("b5bp.Bbp.opus-5-5", bind=6, ans=0, n=20); eq("b5bp.Bbp.sonnet-5-5", bind=2, ans=0, n=20); eq("b5bp.Bbp.fable-5-1", bind=0, ans=0, n=20)
eq("arg5.Bbp", bind=20, ans=0, n=20); eq("arg5d.Bbp", bind=8, ans=0, n=20); eq("arg5.K", bind=20); eq("arg5d.K", bind=20)   # V2
eq("moy5c.opus", bind=10, n=10); eq("moy5c.fable", bind=6, n=10)                                                          # V3
eq("neq3.A.opus", ans=0, n=20); eq("neq3.A/Q2.opus", ans=7, n=20, parabola_ans=20); eq("neq3.L-name/Q2.opus", ans=20); eq("neq3.L-text/Q2.opus", ans=20)
eq("neq3.A/Q2.fable", ans=20, n=20); eq("neq2f.A.fable", ans=0, n=20)                                                     # V4
for cid, a, t in [("neq6.medium.opus", 0, 1038.5), ("neq6.high.opus", 1, 1371.0), ("neq6.max.opus", 19, 8506.5), ("neq6.medium.fable", 15, 2365.0), ("neq6.high.fable", 17, 2722.0), ("neq6.max.fable", 20, 7858.0)]:
    eq(cid, ans=a, thinking_med=t)                                                                                          # V5
eq("neq3.A/Q2.opus", thinking_med=1734.5); eq("neq3.A/Q2.fable", thinking_med=4144.0)                                     # xhigh = neq6 RESULT §1
eq("prf1.P5.opus", CHAIN=1, **{"END-only": 8, "LAT-only": 1}); eq("prf1.P5.fable", none=4, **{"END-only": 6}); eq("prf1.P5K.opus", CHAIN=10); eq("prf1.P5K.fable", CHAIN=9, **{"LAT-only": 1})   # V6
eq("prf3.P5.opus", lat_sym=0, fd_use=10, n=10); eq("prf3.P5B.opus", lat_sym=10, fd_use=0, malformed=1); eq("prf3.P5.fable", lat_sym=0, malformed=5); eq("prf3.P5B.fable", lat_sym=4, malformed=2, lat_sym_ok=4, n_ok=8)   # V7
for cid, b, a, fo, ve, n in [("mnw1.conf/Q1f.opus", 19, 19, 19, 0, 20), ("mnw1.none/Q1f.opus", 1, 1, 0, 1, 20), ("mnw1.cone/Q1.opus", 0, 0, 0, 0, 20), ("mnw1.conf/Q1f.fable", 17, 13, 17, 1, 20), ("mnw1.cone/Q1.fable", 5, 0, 0, 5, 20), ("mnw1.cone/Q1f.fable", 9, 6, 1, 8, 11)]:
    eq(cid, bind=b, ans=a, focal=fo, vertex=ve, n=n)                                                                         # V8
eq("olm1.natural", floor=0, n=20, ans=0); eq("olm1.think", floor=2, n=20, ans=0); eq("olm3.think", floor=5, n=20, ans=0)  # V9
# v2: the values the two readers (D_R1 / D_R2) read off entry P, recounted here (the data wins if they differ)
eq("neq3.K.opus", ans=6, bind=9, n=10); eq("neq2f.K.fable", ans=7, bind=9, n=10)                                          # P #s7 "Q1 の K: Opus 6 / 10 · Fable 7 / 10"
eq("olm1.natural.K", bind=2, ans=1, n=10, empty=5); eq("olm1.think.K", bind=10, ans=0, n=10); eq("olm3.K", bind=10, ans=0, n=10)   # P #s21 "2 / 10 · 10 / 10 · 10 / 10"
eq("mnw1.K.opus", bind=9, ans=1, n=10); eq("mnw1.K.fable", bind=10, ans=4, n=10)                                          # P #s4 mnw1 K
eq("essay4.K.fable-5-1", bind=19, ans=1, n=20); eq("essay4.K.sonnet-5-5", bind=20, ans=0, n=20)                           # essay4 Fable K: the stored bind (r17 false)
for cid, v, vh in [("b5bp.Bbp.sonnet-5-5", 1020.5, 1030), ("b5bp.Bbp.opus-5-5", 1742.5, 1753), ("b5bp.Bbp.fable-5-1", 2233.0, 2233), ("arg5.Bbp", 8468.5, 8494), ("arg5d.Bbp", 965.0, 1005)]:
    eq(cid, reasoning_med=v, reasoning_med_high=vh)                                                                       # P #s13 (data) and SUMMARY §6 (= the upper middle row)
assert sum(CELLS[f"mnw1.{a}.opus"]["n"] for a in ["K", "none/Q1", "none/Q1f", "conf/Q1", "conf/Q1f", "cone/Q1", "cone/Q1f"]) == 130
assert sum(CELLS[f"mnw1.{a}.fable"]["n"] for a in ["K", "none/Q1", "none/Q1f", "conf/Q1", "conf/Q1f", "cone/Q1", "cone/Q1f"]) == 121

# ---- the SUMMARY's data table (frozen text, md5 556b9dfb): the API high arms that give knowledge but not the relation (SUMMARY §5-1: not K, K@U, Bbp, E-full+Bbp)
SUMROWS = []
for line in (C / DOCS["summary_txt"][0]).read_text(encoding="utf-8").splitlines():
    # columns: n | cut (v2) | cut + r8 (may carry "r8 new [..]") | answer-field cut | floor | ...
    m = re.match(r"^(Haiku 5\.5|Sonnet 5\.5|Opus 5\.5|Fable 5\.1|Argon)\s+(API|Claude Code)\s+(\w+)\s+(\w+)\s+(\S+)\s+([0-9a-f]{8})\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(\d+)[^|]*\|\s+(\d+)\s+\|\s+(\d+)\s+\|", line)
    if re.match(r"^(Haiku|Sonnet|Opus|Fable|Argon) ", line):
        assert m, f"a row of the SUMMARY table was not parsed: {line[:80]}"
    if m:
        rel = re.search(r"\|\s+([\d.]+)\s+\|\s+([\d.]+)\s*$", line)
        SUMROWS.append({"model": m[1], "route": m[2], "effort": m[3], "card": m[4], "arm": m[5], "n": int(m[7]), "cut": int(m[8]), "cut_r8": int(m[9]), "ans": int(m[10]), "floor": int(m[11]), "rel_med": float(rel[1]), "cutrel_med": float(rel[2])})
KNOW = [r for r in SUMROWS if r["route"] == "API" and r["effort"] == "high" and r["model"] != "Argon" and r["arm"] not in ("K", "K@U", "Bbp", "E-full+Bbp")]
know_arms = sorted({(r["card"], r["arm"]) for r in KNOW})
assert len(know_arms) == 10, know_arms
KNOW_TOTAL = {"n": sum(r["n"] for r in KNOW), "cut": sum(r["cut"] for r in KNOW), "ans": sum(r["ans"] for r in KNOW), "arms": len(know_arms), "rows": len(KNOW)}
assert KNOW_TOTAL["n"] == 717 and KNOW_TOTAL["cut"] == 1 and KNOW_TOTAL["ans"] == 0, KNOW_TOTAL     # SUMMARY §5-1 "1 / 717" recounted from the frozen table
know_by_arm = {}
for r in KNOW:
    k = f"{r['card']} {r['arm']}"
    a = know_by_arm.setdefault(k, {"card": r["card"], "arm": r["arm"], "n": 0, "cut": 0, "ans": 0, "models": []})
    a["n"] += r["n"]; a["cut"] += r["cut"]; a["ans"] += r["ans"]; a["models"].append(r["model"])
BBP_REL = {r["model"]: r["rel_med"] for r in SUMROWS if r["card"] in ("b5bp", "arg5") and r["arm"] == "Bbp" and r["route"] == "API" and r["effort"] == "high"}
assert BBP_REL == {"Fable 5.1": 19.5, "Opus 5.5": 19.5, "Sonnet 5.5": 11.0, "Argon": 36.0}, BBP_REL          # SUMMARY §2-2 / §5-4: Bbp 36 vs 11-19.5
# v2.1 decision ① (BRIEF v2.1 §2-6): the SUMMARY table takes the median in two ways in two columns: relations = the mean of the two middle rows (19.5), thinking = the upper of the two (1,030 · 8,494)
_relc = {"Opus 5.5": "b5bp.Bbp.opus-5-5", "Fable 5.1": "b5bp.Bbp.fable-5-1", "Sonnet 5.5": "b5bp.Bbp.sonnet-5-5", "Argon": "arg5.Bbp"}
assert {m: CELLS[c]["relations_med"] for m, c in _relc.items()} == BBP_REL, "the rows' relations (mean of the two middle) give the SUMMARY's relations column"
assert {m: CELLS[c]["relations_med_high"] for m, c in _relc.items()} == {"Opus 5.5": 20, "Fable 5.1": 20, "Sonnet 5.5": 11, "Argon": 36}, "median_high would NOT give the SUMMARY's relations column"
assert all(CELLS[c]["reasoning_med_high"] == v for c, v in [("b5bp.Bbp.sonnet-5-5", 1030), ("arg5.Bbp", 8494)]) and CELLS["b5bp.Bbp.sonnet-5-5"]["reasoning_med"] == 1020.5
R8 = {(r["model"], r["card"], r["arm"]): r["cut_r8"] for r in SUMROWS if r["cut_r8"] != r["cut"]}
SUMTXT = {"total": KNOW_TOTAL, "arms": list(know_by_arm.values()), "bbp_rel_med": BBP_REL, "r8_differs": [[*k, v] for k, v in R8.items()]}

# ---- the frozen question (SOURCE l.56-84) and the sentences added to it (read as text; the b5bp runner is read as TEXT, never imported)
src_lines = (C / DOCS["source"][0]).read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(src_lines) if l.startswith("## moy-5 `parabola_section`"))
b0 = src_lines.index("```", i0) + 1
b1 = src_lines.index("```", b0)
prompt = "\n".join(src_lines[b0:b1]) + "\n"          # the frozen text ends with a newline: 1921 characters (SOURCE l.56)
pm = hashlib.md5(prompt.encode()).hexdigest()
assert pm.startswith("ee39ba02"), f"the frozen moy-5 prompt read from SOURCE has md5 {pm}, not ee39ba02"      # positive control of the verbatim reading
assert all(r["prompt_md5"] == pm for r in rows("results_essay4_moy5_20261014_claude-opus-5-5_a.jsonl") if r["arm"] == "A"), "essay4 A ran on this prompt"
FOCUS_Q1 = next(l for l in prompt.splitlines() if l.startswith("Focus on the relation"))
assert FOCUS_Q1 == "Focus on the relation that holds among the following objects: {E, J, K, P_y}."
FOCUS_Q2 = FOCUS_Q1.replace("{E, J, K, P_y}", "{F, V, P_x, P_y}")
neq3_prereg = (C / "2026-10-19/PREREG_neq3_moy5_lemma14_question_set_2x2_opus_fable_xhigh_20261019.md").read_text(encoding="utf-8").splitlines()
assert "{F, V, P_x, P_y}" in neq3_prereg[21] and FOCUS_Q1 in neq3_prereg[21], "PREREG neq3 l.22 is the replaced line"
coords = {}
for l in prompt.splitlines():
    m = re.match(r"^(\w+) = \((-?[\d.]+), (-?[\d.]+)\)$", l)
    if m:
        coords[{"Px": "P_x", "Py": "P_y"}.get(m[1], m[1])] = (float(m[2]), float(m[3]))
radius = float(re.search(r"c = Circle\(A, ([\d.]+)\)", prompt)[1])
khint = src_lines[src_lines.index("```", next(i for i, l in enumerate(src_lines) if "moy-5 の陽性統制 K" in l)) + 1]
assert khint.startswith("Hint: the relation in question is a mean proportional")
b5bp_src = (X / "b5bp_moy5_blocking_beta_prime_20261014.py").read_text(encoding="utf-8").splitlines()
beta = "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', "\n".join(b5bp_src[18:21]))).replace("\\n", "\n").strip()
assert beta.startswith("In the reason field, explain WHY the equality you stated holds") and beta.endswith("in the given symbols."), beta
prf1_pre = (C / "2026-10-21/PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md").read_text(encoding="utf-8").splitlines()[24]
PROOF = re.search(r'"(.+)"', prf1_pre)[1]
prf2_pre = (C / "2026-10-21/PREREG_prf2_moy5_proof_block_focus_directrix_claude_p_20261021.md").read_text(encoding="utf-8").splitlines()[20]
BLOCK = re.search(r'"(.+)"', prf2_pre)[1].strip()
mnw1_pre = (C / "2026-10-22/PREREG_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md").read_text(encoding="utf-8").splitlines()
FORM = re.search(r"`\\nNote: (.+?)`", mnw1_pre[33])[1]
CONF = re.search(r"`(Cf\. Newton.+?)`", mnw1_pre[34])[1]
CONE_GIST = re.search(r"926 字[)\uff09]: (.+?)\s*\*\*問いの字", mnw1_pre[35])[1]
SENT = {"beta": beta, "proof": PROOF, "block": BLOCK, "form": "Note: " + FORM, "conf": CONF, "cone_gist_ja": CONE_GIST, "khint": khint, "focus_q1": FOCUS_Q1, "focus_q2": FOCUS_Q2}


# ---- the construction (A0): the frozen coordinates; D and H are computed for drawing only (not data). Positive control: the computed K, P_y, J match the frozen ones within 1e-3.
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, k): return (a[0] * k, a[1] * k)
def perp(v): return (-v[1], v[0])
def meet(p, u, q, v):
    d = u[0] * v[1] - u[1] * v[0]
    t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / d
    return add(p, mul(u, t))
def dist(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])


def construct(P, Q):
    """Q = the frozen coordinates (A, G, E, F, C); P = a point P_x on h1. Returns every drawn point (drawing only)."""
    A, G, E, F, Cc = Q["A"], Q["G"], Q["E"], Q["F"], Q["C"]
    f_dir = perp(sub(G, A)); g_dir = perp(sub(E, A))
    V = meet(F, f_dir, E, g_dir)                      # j through F parallel to f, meets g at V
    D = meet(G, sub(E, G), F, f_dir)                  # chord GE meets j at D
    e_dir = perp(f_dir)                               # e perpendicular to j at D; h1 through V parallel to e
    K = meet(F, sub(P, F), D, e_dir)                  # the ray F -> P_x meets e at K
    Py = meet(P, perp(sub(P, F)), K, f_dir)           # m perpendicular to FP_x at P_x; the line through K parallel to j
    H = meet(Py, e_dir, F, f_dir)                     # the line through P_y parallel to h1 meets j at H
    J = meet(H, sub(E, G), E, g_dir)                  # the line through H parallel to GE meets g at J
    return {"V": V, "D": D, "K": K, "P_y": Py, "H": H, "J": J, "f_dir": f_dir, "g_dir": g_dir, "e_dir": e_dir}


cs = construct(coords["P_x"], coords)
ctrl = {k: dist(cs[k], coords[k]) for k in ["V", "K", "P_y", "J"]}
assert all(v < 1e-3 for v in ctrl.values()), f"drawing control failed: {ctrl}"
assert abs(dist(coords["F"], coords["A"]) - radius) < 1e-3 and abs(dist(coords["G"], coords["A"]) - radius) < 1e-3
CONSTRUCTION = {"coords": coords, "radius": radius, "D": cs["D"], "H": cs["H"], "control_max_err": max(ctrl.values()), "control": ctrl}


# ---- v2.3 (BRIEF v2.3 §1 · 依頼者 11-09): the cutting plane = the plane through the line FVD (line j) perpendicular to the board. DRAWING (computed from the frozen coordinates; not data).
#      Route 1 of three (route 2 = the page's FIGURE.planeCheck on what it draws, make_check.py check_v23; route 3 = check_claims.py kind `plane` from the SOURCE). The same definitions as figure.js cutPlane:
#      u = along j from F towards V and D; the parabola = 40 samples from the vertex (j meets g) towards F up to H + the top (P_y lifted above H); the rectangle from a little before H to a little past D, up to
#      a little above the highest point. V of §1 = the question's V (rounded to 4 decimals: off j by 4.1e-5); the parabola is drawn from j ∩ g (that rounding is not drawn).
def plane_values(Pt=coords, ctl=None):
    unit = lambda v: mul(v, 1 / math.hypot(*v)); dot = lambda a, b: a[0] * b[0] + a[1] * b[1]; cross = lambda a, b: a[0] * b[1] - a[1] * b[0]
    A, F, V, E, Cc = Pt["A"], Pt["F"], Pt["V"], Pt["E"], Pt["C"]
    c = construct(Pt["P_x"], Pt); u = unit(mul(c["f_dir"], -1)); off = lambda q: abs(cross(sub(q, F), u)); D, H, Vc = c["D"], c["H"], c["V"]
    ju = unit(sub(F, Vc)); p = dist(F, Vc); VH = dot(sub(H, Vc), ju); HPy = dist(c["P_y"], H)
    par = [(add(Vc, mul(ju, VH * (i / 40) ** 2)), math.sqrt(max(0.0, 4 * p * VH * (i / 40) ** 2))) for i in range(40)] + [(H, HPy)]
    if ctl == "frozenV": par = [(add(q, sub(V, Vc)), h) for q, h in par[:-1]] + par[-1:]      # positive control: the parabola from the question's rounded V must be caught
    ss = [dot(sub(q, F), u) for q in (H, Vc, F, D)]; s0, s1 = min(ss) - 0.6, max(ss) + 0.6; top = max(HPy, 1) * 1.06 + 0.4
    rect = [(add(F, mul(u, s0)), 0.0), (add(F, mul(u, s1)), 0.0), (add(F, mul(u, s1)), top), (add(F, mul(u, s0)), top)]
    if ctl == "tilt": rect[3] = (add(rect[3][0], mul(perp(u), 1e-3 * top)), top)                 # positive control: a plane leaned by 1e-3 rad must be caught
    e1 = (*sub(rect[1][0], rect[0][0]), rect[1][1] - rect[0][1]); e2 = (*sub(rect[3][0], rect[0][0]), rect[3][1] - rect[0][1])
    n = (e1[1] * e2[2] - e1[2] * e2[1], e1[2] * e2[0] - e1[0] * e2[2], e1[0] * e2[1] - e1[1] * e2[0])
    ax = unit(sub(A, Cc)); al = math.asin(radius / dist(A, Cc))
    def on_cone(q, h):
        w = sub(q, Cc); along = dot(w, ax)
        return abs(math.atan2(math.hypot(math.hypot(*sub(w, mul(ax, along))), h), along) - al)
    tV, tD = dot(sub(V, F), u), dot(sub(D, F), u)
    return {"u": u, "V_off_j": off(V), "D_off_j": off(D), "tV_over_tD": tV / tD, "FV": dist(F, V), "FD": dist(F, D), "A_to_j": off(A), "AF_dot_j": abs(dot(unit(sub(F, A)), u)),
            "par_n": len(par), "par_off_plane": max(off(q) for q, _ in par), "par_on_cone": max(on_cone(q, h) for q, h in par), "plane_dot_board": abs(n[2]) / math.hypot(*n), "top": top, "s0": s0, "s1": s1}


PLANE = plane_values()
assert abs(PLANE["u"][0] - 0.992546) < 1e-6 and abs(PLANE["u"][1] - 0.121874) < 1e-6, PLANE["u"]                       # BRIEF v2.3 §1: the unit along j
assert abs(PLANE["V_off_j"] - 4.1e-5) < 1e-6 and PLANE["D_off_j"] < 1e-9, PLANE                                          # V (the question's, rounded) and D on j
assert abs(PLANE["tV_over_tD"] - 0.500007) < 1e-6 and abs(PLANE["FV"] - 2.3094) < 1e-4 and abs(PLANE["FD"] - 4.6188) < 1e-4, PLANE   # V = the midpoint of FD
assert abs(PLANE["A_to_j"] - 4.000018) < 1e-6 and PLANE["AF_dot_j"] < 1e-9, PLANE                                        # j touches the circle c at F (distance = r, AF ⟂ j)
assert PLANE["par_n"] >= 20 and PLANE["par_off_plane"] <= 1e-6 and PLANE["plane_dot_board"] < 1e-9 and PLANE["par_on_cone"] < 1e-4, PLANE   # the parabola in the plane (and on the cone); the plane ⟂ the board
assert plane_values(ctl="frozenV")["par_off_plane"] > 1e-6 and plane_values(ctl="tilt")["plane_dot_board"] > 1e-6, "plane: the positive controls were not caught"
CONSTRUCTION["plane"] = {k: v for k, v in PLANE.items() if k not in ("top", "s0", "s1")}

# ---- the scene rows (BRIEF §1-3): the predicate picks the row; the answer field is copied whole; each phrase must occur in `raw` letter for letter
def pick(f, model, arm, pred):
    rs = sorted([r for r in rows(f) if r.get("model") == model and r.get("arm") == arm and r.get("raw")], key=lambda r: r["rep"])
    return next(r for r in rs if pred(r))


SCENES = {}
def scene(sid, f, model, arm, pred, rep, phrases=(), files=None):
    rs = []
    for ff in (files or [f]):
        rs += [r for r in rows(ff) if r.get("model") == model and r.get("arm") == arm and r.get("raw")]
    rs.sort(key=lambda r: r["rep"])
    r = next(r for r in rs if pred(r))
    assert r["rep"] == rep, f"{sid}: the predicate picks rep {r['rep']} (brief {rep})"
    pos = []
    for p in phrases:
        i = r["raw"].find(p)
        assert i >= 0, f"{sid}: the phrase is not in raw: {p}"
        pos.append(i)
    SCENES[sid] = {"id": sid, "file": f, "model": SHORT[model], "arm": arm, "rep": r["rep"], "conjecture": r["conjecture"], "phrases": list(phrases), "at": pos, "raw_len": len(r["raw"]),
                   "thinking": r.get("thinking"), "card": r.get("card")}


P3, P1, N6 = "results_prf3_20261021.jsonl", "results_prf1_20261021.jsonl", "results_neq6_moy5_20261019_claude-opus-5-5.jsonl"
scene("A1L", P3, "claude-opus-5-5", "P5", lambda r: r["fd_use"], 0, ["perpendicular bisector of FK, so P_yF = P_yK"])
scene("A1R", P3, "claude-opus-5-5", "P5B", lambda r: r["lat_sym"] and not r["malformed"], 0, ["Parabola, derived without P_yF = P_yK", "VP_x² = VD·VH = FV·VH", "HP_y² = 4·VP_x² = 4·FV·VH"])
scene("C0", "results_mnw1_moy5_20261022_claude-opus-5-5.jsonl", "claude-opus-5-5", "none/Q1", lambda r: r.get("closure") and not r.get("bind"), 0, [], files=MN("claude-opus-5-5"))
scene("E1L", N6, "claude-opus-5-5", "A/Q2@medium", lambda r: not r.get("cut_in_conjecture"), 0, ["P_y lies on the parabola with focus F and vertex V"])
scene("E1R", N6, "claude-opus-5-5", "A/Q2@max", lambda r: r.get("cut_in_conjecture") and r.get("route_sim"), 0, ["FP_x^2 = FV · FP_y", "triangles F V P_x and F P_x P_y are similar"])
scene("G0", P1, "claude-opus-5-5", "P5", lambda r: r["route5"] == "END-only", 0, ["m is the perpendicular bisector of FK and P_yF = P_yK", "P_yKDH is a rectangle", "P_y is equidistant from the fixed point F and the fixed line e", "= 4·VF·VH"])
scene("G1", P1, "claude-opus-5-5", "P5", lambda r: r["latx"], 2, ["so they are similar", "VF·VH = VP_x²"])
scene("H0L", "results_mnw1_moy5_20261022_claude-opus-5-5.jsonl", "claude-opus-5-5", "none/Q1f", lambda r: not r.get("cut_in_conjecture"), 0, ["EJ : KP_y = KP_y : EJ"], files=MN("claude-opus-5-5"))
scene("H0R", "results_mnw1_moy5_20261022_claude-opus-5-5.jsonl", "claude-opus-5-5", "none/Q1f", lambda r: r.get("cut_in_conjecture"), 12, ["VE : VP_x = VP_x : VJ"], files=MN("claude-opus-5-5"))
scene("H1", "results_mnw1_moy5_20261022_claude-opus-5-5.jsonl", "claude-opus-5-5", "conf/Q1f", lambda r: r.get("cut_in_conjecture") and r.get("form_focal"), 0, ["FV : FP_x = FP_x : EJ", "Newton's Lemma XIV"], files=MN("claude-opus-5-5"))
scene("H2", "results_mnw1_moy5_20261022_claude-fable-5-1.jsonl", "claude-fable-5-1", "cone/Q1", lambda r: r.get("bind") and r.get("form_vertex"), 6, ["Menaechmus symptoma |P_yH|^2 = 4·VF·VH"], files=MN("claude-fable-5-1"))
assert SCENES["A1L"]["conjecture"].startswith("EJ = KP_y") and SCENES["A1R"]["conjecture"].startswith("EJ = KP_y"), "A1: both answer fields are the floor"
assert SCENES["E1L"]["thinking"] == 985 and SCENES["E1R"]["thinking"] == 10174
# the scene rows of prf3 are in the floor (the `floor` field) and on the routes the brief says
for sid, arm in [("A1L", "P5"), ("A1R", "P5B")]:
    r = next(r for r in rows(P3) if r["model"] == "claude-opus-5-5" and r["arm"] == arm and r["rep"] == 0)
    assert r["floor"] is True
    SCENES[sid].update(floor=r["floor"], fd_use=r["fd_use"], lat_sym=r["lat_sym"], malformed=r["malformed"])

# ---- v2 (station 3): "show up to the next" = the moy-5 cards the house froze AFTER the 10-28 figure (olm60-82 · thk1 / thk2; BRIEF v2 §2-4).
#   Every value is read from the card's OWN output (json key / jsonl field) and checked against the number its RESULT printed (R4: the RESULT is a claim, the output is the evidence).
#   status: "verdict" = at least one frozen prediction was read (✓ or ✗) · "gate" = a control / gate stopped the card before any prediction was read · "desc" = a card whose PREREG puts every line as a description (thk2)
#   grade (of the card's headline line, SCOPE 10-31 §1 where it lists the card): 判定 / 較正 / 記述 / 言えない (+ the gate cards: 関門で止まった)
POST_FILES = {}
def J(rel, *keys):
    p = X / rel
    if rel not in POST_FILES:
        POST_FILES[rel] = md5_of(p)
    o = json.loads(p.read_text(encoding="utf-8"))
    for k in keys:
        o = o[k]
    return o
def RES(card):
    hits = sorted(C.glob(f"2026-10-[23]*/RESULT_{card}_moy5_*.md"))
    assert len(hits) == 1, (card, hits)
    return hits[0]
def approx(v, want, tol):
    assert abs(v - want) <= tol, (v, want)
    return v
POST = []
def post(cid, grp, date, freeze, status, grade, vals, meter=None, src=None):
    res = RES(cid)
    txt = res.read_text(encoding="utf-8")
    assert freeze in txt[:1500], f"{cid}: the freeze commit {freeze} is not in the head of its RESULT"
    POST.append({"id": cid, "grp": grp, "date": date, "freeze": freeze, "status": status, "grade": grade, "v": vals, "meter": meter, "result": str(res.relative_to(REPO)), "src": src})
# (a) the frontier's road read by OLMo
post("olm60", "a", "10-28", "0e3edd75", "gate", "gate", {"fve": approx(J("olm60/control.json", "C1", "fve"), 0.3426, 5e-5), "n": J("olm60/control.json", "C1", "n")},
     meter={"x": J("olm60/control.json", "C1", "fve"), "line": 0.40, "lo": 0.2, "hi": 0.5, "gate": True}, src="olm60/control.json C1.fve")
post("olm61", "a", "10-28", "79076ae6", "verdict", "判定", {"apex_lat": J("olm61/read_text_only.json", "Q2", "apex", "lat"), "apex_n": J("olm61/read_text_only.json", "Q2", "apex", "n"),
     "floor_fd": J("olm61/read_text_only.json", "Q2", "floor", "fd"), "floor_n": J("olm61/read_text_only.json", "Q2", "floor", "n"), "fve": approx(J("olm61/control.json", "C1", "fve"), 0.3089, 5e-5)},
     meter={"k": J("olm61/read_text_only.json", "Q2", "floor", "fd"), "n": J("olm61/read_text_only.json", "Q2", "floor", "n"), "line": 0.5, "k2": J("olm61/read_text_only.json", "Q2", "apex", "lat"), "n2": J("olm61/read_text_only.json", "Q2", "apex", "n")}, src="olm61/read_text_only.json Q2.floor.fd · Q2.apex.lat")
assert POST[-1]["v"]["apex_lat"] == 7 and POST[-1]["v"]["apex_n"] == 26 and POST[-1]["v"]["floor_fd"] == 22 and POST[-1]["v"]["floor_n"] == 30
post("olm64", "a", "10-28", "b0c690fa", "verdict", "判定", {"up": J("olm64/read.json", "Q1_P5B_lat_L32", "up"), "n": J("olm64/read.json", "Q1_P5B_lat_L32", "n"),
     "med": approx(J("olm64/read.json", "Q1_P5B_lat_L32", "median_delta"), 1.0892, 5e-5), "null95": approx(J("olm64/read.json", "Q1_P5B_lat_L32", "null_median_p95"), 0.1765, 5e-5),
     "q3": approx(J("olm64/read.json", "Q3_apex_minus_floor_L32", "diff"), 0.3508, 5e-5), "q3null": approx(J("olm64/read.json", "Q3_apex_minus_floor_L32", "null_p95"), 0.3645, 5e-5)},
     meter={"k": J("olm64/read.json", "Q1_P5B_lat_L32", "up"), "n": J("olm64/read.json", "Q1_P5B_lat_L32", "n"), "line": 0.6}, src="olm64/read.json Q1_P5B_lat_L32")
assert POST[-1]["v"]["up"] == 11 and POST[-1]["v"]["n"] == 13
post("olm67", "a", "10-29", "4729c23e", "verdict", "判定", {"up": J("olm67/read.json", "Q1", "up"), "n": J("olm67/read.json", "Q1", "n"), "med": approx(J("olm67/read.json", "Q1", "median_delta"), 0.765, 5e-4),
     "null95": approx(J("olm67/read.json", "Q1", "null_median_p95"), 0.135, 5e-4), "fl_up": J("olm67/read.json", "Q1_desc", "floor_only|all", "up"), "fl_n": J("olm67/read.json", "Q1_desc", "floor_only|all", "n"),
     "fl_med": approx(J("olm67/read.json", "Q1_desc", "floor_only|all", "median_delta"), 0.512, 5e-4), "lens": approx(J("olm67/control.json", "C1_lens", "all", "lens_med"), 0.706, 5e-4),
     "ident": approx(J("olm67/control.json", "C1_lens", "all", "ident_med"), 0.513, 5e-4), "q2": approx(J("olm67/read.json", "Q2", "frac_top5_by_k", "3"), 0.214, 5e-4)},
     meter={"k": J("olm67/read.json", "Q1", "up"), "n": J("olm67/read.json", "Q1", "n"), "line": 0.6}, src="olm67/read.json Q1 · control.json C1_lens")
assert (POST[-1]["v"]["up"], POST[-1]["v"]["n"], POST[-1]["v"]["fl_up"], POST[-1]["v"]["fl_n"]) == (238, 361, 344, 509)
# (b) the run-up to the cut sentence
post("olm68", "b", "10-29", "cd4a7ae0", "verdict", "判定", {"diff": approx(J("olm68/read.json", "Q1", "diff"), 0.0313, 5e-5), "pos": J("olm68/read.json", "Q2", "cards_median_pos"), "cards": J("olm68/read.json", "Q2", "cards_n_ge_10"),
     "placebo": approx(J("olm68/control.json", "C2_placebo_pseudo_event", "diff"), -0.0347, 5e-5)}, meter={"k": J("olm68/read.json", "Q2", "cards_median_pos"), "n": J("olm68/read.json", "Q2", "cards_n_ge_10"), "line": 0.7}, src="olm68/read.json Q1.diff · Q2")
assert (POST[-1]["v"]["pos"], POST[-1]["v"]["cards"]) == (7, 9)
post("olm69", "b", "10-29", "3f138f1e", "verdict", "記述", {"L": J("olm69/read.json", "Q1", "L", "cut_word_in_cut_sentence"), "Ln": J("olm69/read.json", "Q1", "L", "n"), "A": J("olm69/read.json", "Q1", "A", "cut_word_in_cut_sentence"),
     "An": J("olm69/read.json", "Q1", "A", "n"), "c3": approx(J("olm69/control.json", "C3_own_k1", "median_u"), 0.905, 5e-4)}, src="olm69/read.json Q1 · control.json C3_own_k1")
assert (POST[-1]["v"]["L"], POST[-1]["v"]["Ln"], POST[-1]["v"]["A"], POST[-1]["v"]["An"]) == (52, 75, 6, 16)
post("olm70", "b", "10-29", "f4e56ab0", "gate", "gate", {"u": approx(J("olm70/read.json", "C_test_k1", "median_u_k1"), 0.933, 5e-4), "cal": approx(J("olm70/calibrate.json", "rules", "R3", "median_u_k1"), 0.968, 5e-4)},
     meter={"x": J("olm70/read.json", "C_test_k1", "median_u_k1"), "line": 0.95, "lo": 0.85, "hi": 1.0, "gate": True}, src="olm70/read.json C_test_k1.median_u_k1")
post("olm71", "b", "10-29", "417dff60", "gate", "gate", {"rows": J("olm71/calibrate.json", "BODY", "rows_nonempty"), "n": J("olm71/calibrate.json", "BODY", "n_rows"), "u": approx(J("olm71/calibrate.json", "BODY", "median_u_k1"), 0.994, 5e-4)},
     meter={"k": J("olm71/calibrate.json", "BODY", "rows_nonempty"), "n": J("olm71/calibrate.json", "BODY", "n_rows"), "line": 0.8, "gate": True}, src="olm71/calibrate.json BODY")
assert (POST[-1]["v"]["rows"], POST[-1]["v"]["n"]) == (178, 275)
post("olm72", "b", "10-29", "842ecabf", "gate", "gate", {"rows": J("olm72/calibrate.json", "BODY", "rows_nonempty"), "n": J("olm72/calibrate.json", "BODY", "n_rows"), "u": approx(J("olm72/calibrate.json", "BODY", "median_u_k1"), 0.995, 5e-4)},
     meter={"k": J("olm72/calibrate.json", "BODY", "rows_nonempty"), "n": J("olm72/calibrate.json", "BODY", "n_rows"), "line": 0.8, "gate": True}, src="olm72/calibrate.json BODY")
assert (POST[-1]["v"]["rows"], POST[-1]["v"]["n"]) == (180, 275)
post("olm73", "b", "10-29", "30b429fe", "verdict", "言えない", {"pos": J("olm73/read.json", "Q2", "pos"), "n": J("olm73/read.json", "Q2", "n"), "med": approx(J("olm73/read.json", "Q2", "median"), -0.047, 5e-4), "p": approx(J("olm73/read.json", "Q2", "binom_p"), 0.992, 5e-4)},
     meter={"k": J("olm73/read.json", "Q2", "pos"), "n": J("olm73/read.json", "Q2", "n"), "line": 0.6}, src="olm73/read.json Q2")
assert (POST[-1]["v"]["pos"], POST[-1]["v"]["n"]) == (20, 57)
post("olm74", "b", "10-29", "ec45e01c", "verdict", "判定", {"pos": J("olm74/read.json", "Q2", "pos"), "n": J("olm74/read.json", "Q2", "n"), "med": approx(J("olm74/read.json", "Q2", "median"), 0.0522, 5e-5),
     "L": approx(J("olm74/read.json", "Q1", "median_L"), -0.067, 5e-4), "O": approx(J("olm74/read.json", "Q1", "median_O"), 0.044, 5e-4), "dL": approx(J("olm74/read.json", "Q3", "median_L"), -0.040, 5e-4),
     "dO": approx(J("olm74/read.json", "Q3", "median_O"), 0.052, 5e-4), "Lpos": J("olm74/read.json", "Q3", "L_sign", "pos")}, meter={"k": J("olm74/read.json", "Q2", "pos"), "n": J("olm74/read.json", "Q2", "n"), "line": 0.6}, src="olm74/read.json Q1 · Q2 · Q3")
assert (POST[-1]["v"]["pos"], POST[-1]["v"]["n"], POST[-1]["v"]["Lpos"]) == (192, 288, 33)
post("olm77", "b", "10-30", "3fdfeb93", "gate", "gate", {"W": approx(J("olm77/control.json", "C1_positive_1_8", "W"), -0.0185, 5e-5), "p": approx(J("olm77/control.json", "C1_positive_1_8", "perm_p"), 0.924, 5e-4),
     "up": sum(1 for c in J("olm77/control.json", "C1_positive_1_8", "per_card").values() if c["diff"] > 0), "cards": len(J("olm77/control.json", "C1_positive_1_8", "per_card"))}, src="olm77/control.json C1_positive_1_8")
assert (POST[-1]["v"]["up"], POST[-1]["v"]["cards"]) == (1, 6)
post("olm78", "b", "10-30", "8b5673be", "verdict", "判定", {"rW": approx(J("olm78/read.json", "Q1_layer48_word_order", "r_W"), 0.575, 5e-4), "q2pos": J("olm78/read.json", "Q2_final_layer_effect", "pos"), "q2n": J("olm78/read.json", "Q2_final_layer_effect", "n"),
     "q2p": approx(J("olm78/read.json", "Q2_final_layer_effect", "sign_p"), 0.108, 5e-4)}, meter={"x": J("olm78/read.json", "Q1_layer48_word_order", "r_W"), "line": 0.5, "lo": 0, "hi": 1}, src="olm78/read.json Q1_layer48_word_order.r_W · Q2_final_layer_effect")
assert (POST[-1]["v"]["q2pos"], POST[-1]["v"]["q2n"]) == (155, 288)
post("olm79", "b", "10-30", "1ad08f57", "gate", "gate", {"pos": J("olm79/control.json", "C1_sensitivity_O_rows", "pos"), "n": J("olm79/control.json", "C1_sensitivity_O_rows", "n"), "p": approx(J("olm79/control.json", "C1_sensitivity_O_rows", "sign_p"), 0.086, 5e-4)},
     meter={"k": J("olm79/control.json", "C1_sensitivity_O_rows", "pos"), "n": J("olm79/control.json", "C1_sensitivity_O_rows", "n"), "line": 0.6, "gate": True}, src="olm79/control.json C1_sensitivity_O_rows")
assert (POST[-1]["v"]["pos"], POST[-1]["v"]["n"]) == (45, 77)
post("olm81", "b", "10-31", "6671fe53", "verdict", "判定", {"pos": J("olm81/read.json", "Q1_formula_only_O", "pos"), "n": J("olm81/read.json", "Q1_formula_only_O", "n"), "med": approx(J("olm81/read.json", "Q1_formula_only_O", "median"), 0.070, 5e-4),
     "op": J("olm81/read.json", "Q2_by_model", "opus", "pos"), "on": J("olm81/read.json", "Q2_by_model", "opus", "n"), "fp": J("olm81/read.json", "Q2_by_model", "fable", "pos"), "fn": J("olm81/read.json", "Q2_by_model", "fable", "n")},
     meter={"k": J("olm81/read.json", "Q1_formula_only_O", "pos"), "n": J("olm81/read.json", "Q1_formula_only_O", "n"), "line": 0.6}, src="olm81/read.json Q1_formula_only_O · Q2_by_model")
assert (POST[-1]["v"]["pos"], POST[-1]["v"]["n"], POST[-1]["v"]["op"], POST[-1]["v"]["on"], POST[-1]["v"]["fp"], POST[-1]["v"]["fn"]) == (69, 98, 36, 53, 33, 45)
_rho = J("olm82/read.json", "Q2_jlens_rho_common_vs_entropy")
post("olm82", "b", "10-31", "61e7917d", "verdict", "判定", {"rho_min": approx(min(_rho.values()), 0.772, 5e-4), "rho_max": approx(max(_rho.values()), 0.836, 5e-4), "q1b": approx(J("olm82/read.json", "Q1b_jlens", "entropy_rank_frac"), 0.11, 5e-3)},
     meter={"x": min(_rho.values()), "line": 0.3, "lo": 0, "hi": 1}, src="olm82/read.json Q2_jlens_rho_common_vs_entropy · Q1b_jlens")
# (c) does the layer-32 residual go beyond the words (olm80) · when the SAE can be used (olm63)
post("olm63", "c", "10-28", "842aefce", "verdict", "判定", {"s0": approx(J("olm63/control.json", "S0", "all", "fve"), 0.4495, 5e-5), "best": approx(J("olm63/read.json", "S4", "all", "fve"), 0.384, 5e-4),
     "ascii": approx(J("olm63/read.json", "Q1_ascii_gain", "S2_minus_S1"), 0.0093, 5e-5), "noprompt": approx(J("olm63/read.json", "Q2_no_prompt_gain", "S3_minus_S1"), 0.0516, 5e-5)},
     meter={"x": J("olm63/read.json", "S4", "all", "fve"), "line": 0.40, "lo": 0.2, "hi": 0.5}, src="olm63/read.json S4.all.fve · control.json S0.all.fve")
post("olm80", "c", "10-31", "32e1b4ad", "gate", "gate", {"dw": approx(J("olm80/control.json", "C1_words_instrument_calibration", "delta_word", "median"), 0.056, 5e-4), "null95": approx(J("olm80/control.json", "C2_within_card_null", "null_auc32", "p95"), 0.739, 5e-4),
     "auc32": approx(J("olm80/control.json", "C3_effect_exists", "auc32_cut", "median"), 0.941, 5e-4), "auc0": approx(J("olm80/control.json", "C3_effect_exists", "auc0_cut", "median"), 0.956, 5e-4)},
     meter={"x": J("olm80/control.json", "C1_words_instrument_calibration", "delta_word", "median"), "line": 0.03, "lo": 0, "hi": 0.1, "gate": True, "below": True}, src="olm80/control.json C1 · C2 · C3")
# (d) the frontier's thinking summary (thk1 / thk2: the jsonl rows)
TK1 = [r for m in ["opus-5-5", "fable-5-1"] for r in rows(f"results_thk1_moy5_20261030_claude-{m}.jsonl")]
TK2 = [r for m in ["opus-5-5", "fable-5-1"] for r in rows(f"results_thk2_moy5_20261030_claude-{m}.jsonl")]
for f in [f"results_thk{k}_moy5_20261030_claude-{m}.jsonl" for k in (1, 2) for m in ("opus-5-5", "fable-5-1")]:
    POST_FILES[f] = md5_of(X / f)
assert len(TK1) == 2 and all(r["api_key_source"] == "ANTHROPIC_API_KEY" for r in TK1)
post("thk1", "d", "10-30", "f2ccf1be", "gate", "gate", {"rows": len(TK1), "keysrc": TK1[0]["api_key_source"]}, src="results_thk1_*.jsonl api_key_source")
thk2_rows = [{"model": SHORT[r["model"]], "rep": r["rep"], "think": r["thinking_tokens"], "chars": r["summary_chars"], "ans": bool(r["ans_cut"]), "summ": bool(r["summ_cut"]), "key": r["api_key_source"]} for r in TK2]
assert len(thk2_rows) == 8 and all(r["key"] == "none" for r in thk2_rows) and all(r["chars"] > 0 for r in thk2_rows)
_ans = [r for r in thk2_rows if r["ans"]]
post("thk2", "d", "10-30", "85464c61", "desc", "記述", {"rows": len(thk2_rows), "nonempty": sum(r["chars"] > 0 for r in thk2_rows), "ans": len(_ans), "both": sum(r["summ"] for r in _ans),
     "agree": sum(r["ans"] == r["summ"] for r in thk2_rows), "cpt": approx(statistics.median(r["chars_per_thinking_token"] for r in TK2), 0.983, 5e-4)}, src="results_thk2_*.jsonl ans_cut · summ_cut · summary_chars")
assert (POST[-1]["v"]["ans"], POST[-1]["v"]["both"], POST[-1]["v"]["agree"]) == (5, 5, 8)
assert len(POST) == 20 and len({p["id"] for p in POST}) == 20
# ---- v2.1: the values the readers moved from entry P (D3 ①–⑥ and the one-reader items kept), each from the card's own output (R4)
_v = {p["id"]: p["v"] for p in POST}
_v["olm67"].update(q2k2=approx(J("olm67/read.json", "Q2", "frac_top5_by_k", "2"), 0.75, 5e-4), q2pass=J("olm67/read.json", "Q2", "pass"),
                   q3=approx(J("olm67/read.json", "Q3", "diff"), 0.0539, 5e-4), q3pass=J("olm67/read.json", "Q3", "pass"))
assert _v["olm67"]["q2pass"] is False and _v["olm67"]["q3pass"] is True
next(p for p in POST if p["id"] == "olm67")["meter2"] = {"x": _v["olm67"]["q2"], "line": 0.30, "post": _v["olm67"]["q2k2"], "lo": 0, "hi": 1, "lab": "Q2"}   # ①: frozen 30 % (3 token before) solid · post-hoc 75 % (2 token before) dashed
for cid in ("olm71", "olm72"):
    gt = J(f"{cid}/read.json", "gates_test")
    _v[cid].update(L=gt["BODY|L"]["rows_nonempty"], Ln=gt["BODY|L"]["n_rows"], A=gt["BODY|A"]["rows_nonempty"], An=gt["BODY|A"]["n_rows"])
    _v[cid]["empty"] = (_v[cid]["n"] - _v[cid]["rows"]) + (_v[cid]["Ln"] - _v[cid]["L"]) + (_v[cid]["An"] - _v[cid]["A"])
assert (_v["olm71"]["L"], _v["olm71"]["Ln"], _v["olm71"]["A"], _v["olm71"]["An"]) == (57, 75, 11, 16) and _v["olm72"]["empty"] == 118
_t72 = RES("olm72").read_text(encoding="utf-8"); assert "語が残らない行の 113 / 118 は" in _t72[:1500]          # the 113 is a diagnostic of RESULT olm72 (no json key; the 118 is recounted above)
_v["olm72"]["formula"] = 113
_v["thk1"].update(opus=next(r["thinking_tokens"] for r in TK1 if r["model"] == "claude-opus-5-5"), fable=next(r["thinking_tokens"] for r in TK1 if r["model"] == "claude-fable-5-1"),
                  opus_c=next(r["summary_chars"] for r in TK1 if r["model"] == "claude-opus-5-5"), fable_c=next(r["summary_chars"] for r in TK1 if r["model"] == "claude-fable-5-1"))
assert (_v["thk1"]["opus"], _v["thk1"]["fable"]) == (2724, 7704)
_v["olm80"]["null_med"] = approx(J("olm80/control.json", "C2_within_card_null", "null_auc32", "median"), 0.522, 5e-4)       # ⑨: the line 0.60 is on the 95 % point (RESULT olm80 C2), the median is under it
_v["olm81"].update(q3=approx(J("olm81/read.json", "Q3_desc", "F_vs_W_O", "diff_F_minus_W"), 0.027, 5e-4), q3p=approx(J("olm81/read.json", "Q3_desc", "F_vs_W_O", "perm_p_two_sided"), 0.128, 5e-4))
_v["olm74"]["p"] = J("olm74/read.json", "Q2", "binom_p"); assert _v["olm74"]["p"] < 1e-8
_v["olm67"].update(cut_o=approx(J("olm67/read.json", "Q1_desc", "cut|opus", "median_delta"), 0.825, 5e-4), cut_f=approx(J("olm67/read.json", "Q1_desc", "cut|fable", "median_delta"), 0.744, 5e-4),
                   fl_o=approx(J("olm67/read.json", "Q1_desc", "floor_only|opus", "median_delta"), 0.868, 5e-4), fl_f=approx(J("olm67/read.json", "Q1_desc", "floor_only|fable", "median_delta"), 0.227, 5e-4))   # G-01: Fable separates, Opus does not
# ---- v2.1 the grade rule (BRIEF v2.1 §2-5 = 依頼者 11-07「F2 推しで」; the maker grades nothing):
#   (i)  the card's name is in SCOPE 10-31 §1 / §2 (the 根拠 column of the 判定 / 較正 / 記述 tables, or a bullet of 言えない) -> copy that tier.
#        Machine condition: the name matched as a whole token (not olm7 inside olm77). Excluded: the 動き column, §0, §3, §4.
#        A card named in several tiers takes the first of 判定 > 較正 > 記述 > 言えない (the maker's tie-break, mirroring rule (ii) "a ✓ anywhere = 判定"; disclosed in NOTES).
#   (ii) not named -> the SCOPE's tier criteria on the card's RESULT: a ✓ on a frozen prediction = 判定 / a gate failed and no frozen prediction was read = 関門で止まった /
#        read but no ✓ = 記述 / a card of controls only = 較正. The facts are typed below and each is pinned to the RESULT's own line (text_contains) — R4: the RESULT's verdict marks are its judgments of frozen predicates.
_scope_p = C / "2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md"
_scope = _scope_p.read_text(encoding="utf-8"); POST_FILES["SCOPE_10-31"] = hashlib.md5(_scope.encode()).hexdigest()
_body = _scope[_scope.index("## §1."):_scope.index("## §3.")]
_hits, _tier = {p["id"]: set() for p in POST}, None
for line in _body.splitlines():
    m = re.match(r"^### (判定|較正|記述|言えない)", line)
    if m:
        _tier = m[1]; continue
    if line.startswith("## "):
        _tier = None; continue
    ev = None
    if _tier and line.startswith("|") and not line.startswith("|---") and not line.startswith("| 文 |"):
        ev = line.split("|")[2]
    elif _tier == "言えない" and line.lstrip().startswith("- "):
        ev = line
    if ev:
        for cid in _hits:
            if re.search(rf"(?<![A-Za-z0-9]){cid}(?![0-9])", ev):
                _hits[cid].add(_tier)
ORDER5 = ["判定", "較正", "記述", "言えない"]
RULE2 = {   # card: (grade, the RESULT's own line that decides it)
    "olm60": ("関門", "Q1〜Q5 は走っていない(判定なし)"), "olm61": ("判定", "**22 / 30**(73 %) | ✓"), "olm63": ("判定", "**+0.0516** | ✓"),
    "olm64": ("判定", "観測以上の乱数 0 / 2000) | ✓"), "olm70": ("関門", "C ✗ のため**読まない**"), "olm71": ("関門", "Q2〜Q5 は読まない"),
    "olm72": ("関門", "Q2・Q3 は読まない"), "olm82": ("判定", "S1 **0.83**・S2 **0.77**・S3 **0.84** | **✓**"), "thk1": ("関門", "止める規則 §4 で各 model 1 行で止まった")}
for p in POST:
    h = _hits[p["id"]]
    if h:
        p.update(grade5=next(t for t in ORDER5 if t in h), rule="i", tiers=[t for t in ORDER5 if t in h], grade_src="SCOPE 10-31 §1")
        assert p["id"] not in RULE2, p["id"]
    else:
        g, line = RULE2[p["id"]]
        txt = RES(p["id"]).read_text(encoding="utf-8")
        assert line in txt, (p["id"], line)
        p.update(grade5=g, rule="ii", tiers=[], grade_src=f"RESULT {p['id']}: «{line}»")
GRADE_TALLY = {g: sum(p["grade5"] == g for p in POST) for g in ["判定", "記述", "較正", "言えない", "関門"]}
assert sum(GRADE_TALLY.values()) == 20, GRADE_TALLY
RULE_TALLY = {"i": sum(p["rule"] == "i" for p in POST), "ii": sum(p["rule"] == "ii" for p in POST)}
assert GRADE_TALLY == {"判定": 9, "記述": 4, "較正": 0, "言えない": 2, "関門": 5} and RULE_TALLY == {"i": 11, "ii": 9}, (GRADE_TALLY, RULE_TALLY)
POST_TALLY = {"grade": GRADE_TALLY, "rule": RULE_TALLY, "n": len(POST)}
CODE5 = {"判定": "verdict", "記述": "desc", "較正": "cal", "言えない": "cannot", "関門": "gate"}
for p in POST:   # v2.1: the figure's mark and badge follow the rule's grade (v2's own status / grade are replaced; "判定に届いた" is no longer a word of this figure = G-08)
    p["status_v2"], p["grade_v2"] = p["status"], p["grade"]
    p["status"], p["grade"] = CODE5[p["grade5"]], ("gate" if p["grade5"] == "関門" else p["grade5"])
# the five bundles of the readers' next questions the house has not fired (RESULT station 3 §1 N4) — read as text, counts parsed and asserted
_st3 = (C / "2026-11-06/coread_station2_3/station3_moy5/RESULT_station3_moy5_next_visible_two_maker_variation_20261106.md").read_text(encoding="utf-8")
POST_FILES["RESULT_station3"] = hashlib.md5(_st3.encode()).hexdigest()
_n4 = next(l for l in _st3.splitlines() if l.startswith("- N4"))
N4 = {"total": int(re.search(r"(\d+) 問\)の大きな束", _n4)[1]), "bundles": [int(x) for x in re.findall(r"= (\d+) 問", _n4)]}
assert N4 == {"total": 29, "bundles": [8, 4, 5, 3, 4]}, N4
# v2.1 (D3 ④ = both readers): one verbatim question per bundle with the reply's id (moved from entry P #s28; each quote is asserted in its reply file here, md5 kept)
_ST3 = C / "2026-11-06/coread_station2_3/station3_moy5"
_NQ = [("reads/N_R2_Q/judge_reply.md", "N-2", "同じ札・同じ effort の腕の中で、答えの欄に cut が出た行と出なかった行は、行ごとの thinking の token 数で分かれるか(neq6)。"),
       ("reads/N_R2_Q/judge_reply.md", "N-3", "β′ の一文を一つの札で、経路 {API, claude -p} × effort {high, max} の 2 × 2 に同じ n で掛けたとき、全体の cut を動かすのは経路か effort か。"),
       ("reads/T_R2/judge_reply.md", "N-4", "比例の形の一文を Q1 の点の集合 {E, J, K, P_y} でなく Q2 の {F, V, P_x, P_y} に足すと、退化した比例が消えて答えの欄に cut が出るか(形の指図 × 点の集合の 2 × 2)"),
       ("reads/N_R1_Q/judge_reply.md", "N-1", "塞ぎの一文を禁止と指図に分ける — prf3 P5B の LAT_SYM(Opus 10 / 10・Fable 4 / 10)は「do not use …」の禁止だけの腕でも、「Derive the equation from other relations …」の指図だけの腕でも出るか(claude -p · max · n 10)"),
       ("reads/N_R2_P/judge_reply.md", "N-4", "読み取り器 v1・v2・人の裁定で cut の判定が割れるのはどの行か。その割れは答えの欄と理由の欄のどちらに集まるか。")]
N4["quotes"] = []
for rel_, qn, quote in _NQ:
    if not (_ST3 / rel_).is_file():   # bundle: the readers' replies are house records and are not shipped; the same checks were made on them when the bundle was cut
        _rf = json.loads((HERE / "data" / "reader_reply_facts.json").read_text(encoding="utf-8"))
        assert [rel_, qn, quote] in _rf["checked"], (rel_, qn)
        POST_FILES["station3/" + rel_] = _rf["md5"][rel_]
        N4["quotes"].append({"file": "station3_moy5/" + rel_, "qn": qn, "quote": quote})
        continue
    _txt = (_ST3 / rel_).read_text(encoding="utf-8")
    assert quote in _txt, (rel_, qn)
    _ls = _txt.splitlines(); _i = _ls.index(qn)                       # the id stands on its own line; the quote is in its block (before the next id)
    assert any(quote in l for l in _ls[_i + 1:_i + 6]), (rel_, qn)
    POST_FILES["station3/" + rel_] = hashlib.md5(_txt.encode()).hexdigest()
    N4["quotes"].append({"file": "station3_moy5/" + rel_, "qn": qn, "quote": quote})
N4["home"] = 0   # 依頼者 11-07 F4「束 ① thinking の量」(C7 = the house fires bundle ①): BRIEF v2.1 §2-9

pack = {"files": FILES, "cells": CELLS, "summary_txt": SUMTXT, "sentences": SENT, "construction": CONSTRUCTION, "scenes": SCENES,
        "prompt_md5": pm, "prompt_chars": len(prompt), "traj": TRAJ, "post": POST, "post_tally": POST_TALLY, "post_files": POST_FILES, "thk2_rows": thk2_rows, "n4": N4}
(OUT / "pack.json").write_text(json.dumps(pack, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"pack: {len(CELLS)} cells · {sum(c['n'] for c in CELLS.values())} rows drawn as dots · {len(SCENES)} scene rows · prompt md5 {pm[:8]} · drawing control max err {CONSTRUCTION['control_max_err']:.2e} · SUMMARY table 1 / 717 recounted ({KNOW_TOTAL})")
print(f"plane (v2.3, route 1): u ({PLANE['u'][0]:.6f}, {PLANE['u'][1]:.6f}) · V off j {PLANE['V_off_j']:.2e} · D off j {PLANE['D_off_j']:.1e} · tV/tD {PLANE['tV_over_tD']:.6f} · FV {PLANE['FV']:.4f} · FD {PLANE['FD']:.4f} · A to j {PLANE['A_to_j']:.6f} · AF·u {PLANE['AF_dot_j']:.1e} · parabola {PLANE['par_n']} samples off the plane <= {PLANE['par_off_plane']:.1e} · on the cone <= {PLANE['par_on_cone']:.1e} rad · plane normal · board normal {PLANE['plane_dot_board']:.1e} · controls caught (frozen V, tilt)")
