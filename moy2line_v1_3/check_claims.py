"""check_claims.py — the FOURTH route of every number, and the coverage of the claims. Reads claims_anchors.json (an anchor = a file, a key and an expected value) and looks at the place itself:
  json_equals          the value at `key` (dotted path; list indices are numbers) of a JSON file equals `expect`
  derived              a number RECOUNTED here from the raw inventory rows / read.json (DERIVED[name](*args)) equals `expect` — not through pack_moy2.py, data.mjs or the page
  pack_equals_derived  the value the page carries (generated/pack.json at `key`) equals the recount
  text_contains        a literal string occurs in a text file (the file read as TEXT, even if it is JSON); repository-relative paths start with "repo:"
  md5                  the md5 of a file equals `expect`
Coverage: every anchor id appears in CLAIMS.md's tables and every id there has an anchor. It proves the quoted words and values are there and that the counted numbers are the card's,
not that a sentence of the figure is a fair reading of them (that is the L3 half, for the reader).
    python3 -I check_claims.py          (exit 1 if anything is missing or differs)
"""
import hashlib
import json
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE  # bundle: "repo:" anchors resolve inside this folder (cards/)
INV = json.loads((HERE / "data" / "moy2_line_inventory.json").read_text(encoding="utf-8"))
READ = {n: json.loads((HERE / "data" / "read" / f"olm{n}.json").read_text(encoding="utf-8")) for n in (118, 119, 122, 124, 125, 126, 127)}
rows = lambda a: INV["arms"][a]["rows"]
pf = lambda a: [r for r in rows(a) if r["has_proof"]]
ln3 = lambda r: bool((r["proof_v3"] or {}).get("LN_a"))
ln6 = lambda r: bool((r["proof_v6"] or {}).get("LN6_a"))
out3 = lambda r: bool((r["proof_v3"] or {}).get("OUTER_a"))
out6 = lambda r: bool((r["proof_v6"] or {}).get("OUTER6_a"))
r4 = lambda k, n: round(k / n, 4) if n else 0.0


def d_ln(a, v="v3"):
    p = pf(a); k = sum(1 for r in p if (ln3 if v == "v3" else ln6)(r)); return f"{k} / {len(p)} = {r4(k, len(p))}"
def d_parsed(a): return sum(1 for r in rows(a) if r["cls"] != "NONE")
def d_calc(a): return sum(1 for r in rows(a) if r["calc"])
def d_rej(a): return sum(1 for r in rows(a) if r["rej6"])
def d_rej_calc(a): return sum(1 for r in rows(a) if r["rej6"] and r["calc"])
def d_typ(a): return [r["key"] for r in rows(a) if r["rej6"] and r["has_proof"] and ln6(r)]
def d_split(a):
    c = [r for r in rows(a) if r["calc"] and r["has_proof"]]; n = [r for r in rows(a) if not r["calc"] and r["has_proof"]]
    return [sum(map(ln3, c)), len(c), sum(map(ln3, n)), len(n)]
def d_cls_rate(a, c): p = d_parsed(a); return r4(sum(1 for r in rows(a) if r["cls"] == c), p)
def d_out(a, v="v3"): return sum(1 for r in pf(a) if (out3 if v == "v3" else out6)(r))
def d_tn(a): return sum(1 for r in rows(a) if r["tool_named"])
def d_rej_cap(a): return sum(1 for r in rows(a) if r["rej6"] and r["hit_cap"])
def d_cap(a): return sum(1 for r in rows(a) if r["hit_cap"])
def d_calc_cls(a, c): return sum(1 for r in rows(a) if r["calc"] and r["cls"] == c)
def d_row(a, k, field): return next(r for r in rows(a) if r["key"] == k)[field]
def d_recount(): return [sum(1 for c in INV["recount_vs_read_json"] if c["ok"]), len(INV["recount_vs_read_json"])]
def d_v6_delta(a):
    p = pf(a); return round(r4(sum(map(ln6, p)), len(p)) - r4(sum(map(ln3, p)), len(p)), 4)
def d_same7():
    q = READ[126]["Q2"]; return [sum(1 for k in q["frozen"] if q["frozen"][k] == q["v6"][k]), len(q["frozen"])]


def d_four():
    """v1.1 F1: the four arms' rejects among calc rows (REJ6 ∧ REFL_CALC / REFL_CALC), recounted here"""
    k = [d_rej_calc(a) for a in ("olm119", "olm124", "olm125", "olm127")]; n = [d_calc(a) for a in ("olm119", "olm124", "olm125", "olm127")]; return [sum(k), sum(n)]
def d_four_num(): return d_four()[0]
def d_rej_pf(a): return [r["key"] for r in rows(a) if r["rej6"] and r["has_proof"]]
def d_calc_pf(a): return sum(1 for r in rows(a) if r["calc"] and r["has_proof"])
def d_proof_has(a, k, s): return s in (d_row(a, k, "proof") or "")
def d_t_med(a):
    import statistics
    c = [r["T"] for r in rows(a) if r["calc"]]; n = [r["T"] for r in rows(a) if not r["calc"]]; return [statistics.median(c) if c else None, statistics.median(n)]
def d_prompt_lens(): P = INV["prompts"]; return [len(P["TOOL_D(式だけ・olm122/124)"]), len(P["SECOND(宣言の文・olm119)"]), len(P["TOOL(式 + 宣言の文・olm119)"]), len(P["TOOL_U(指示の文・olm125/127)"])]
def d_fisher():
    """v1.1 F4: the two-sided Fisher exact p of the seven pairs, recounted here from the rows (not through the pack)"""
    def lnp(a): p = pf(a); return [sum(map(ln3, p)), len(p)]
    def f(a, n1, b, n2):
        K, N = a + b, n1 + n2; pr = lambda x: math.comb(n1, x) * math.comb(n2, K - x) / math.comb(N, K); p0 = pr(a)
        return round(min(1.0, sum(pr(x) for x in range(max(0, K - n2), min(K, n1) + 1) if pr(x) <= p0 * (1 + 1e-7))), 4)
    pf_ = [lnp("olm122")[0] + lnp("olm124")[0], lnp("olm122")[1] + lnp("olm124")[1]]; pi_ = [lnp("olm125")[0] + lnp("olm127")[0], lnp("olm125")[1] + lnp("olm127")[1]]
    pairs = [(lnp("olm125"), lnp("olm124")), (lnp("olm125"), pf_), (lnp("olm125"), lnp("olm119")), (lnp("olm127"), lnp("olm124")), (lnp("olm127"), lnp("olm125")), (lnp("olm127"), lnp("olm119")), (pi_, pf_)]
    return [f(x[0], x[1], y[0], y[1]) for x, y in pairs]


def d_geo(what):
    """the configuration recomputed HERE from S1's text (independent of pack_moy2.py): the reflection of Th across O1O2, the apex distances, the midpoint gap"""
    r = INV["scenes"]["S1_rej_then_LN(olm125 b1_j17)"]["row"]; h, rf = r["head"], r["rej6_first"]; num = r"(-?\d+\.\d+)"
    O1 = [float(x) for x in re.search(r"O1 = \(" + num + ", " + num, h).groups()]; O2 = [float(x) for x in re.search(r"O2 = \(" + num + ", " + num, h).groups()]
    Th = [float(x) for x in re.search(r"Th = \(" + num + ", " + num, h).groups()]; Tc = [float(x) for x in re.search(r"Tc: \(" + num + ", " + num, rf).groups()]
    O3 = [(O1[0] + O2[0]) / 2, (O1[1] + O2[1]) / 2]; d = [O2[0] - O1[0], O2[1] - O1[1]]
    t = ((Th[0] - O1[0]) * d[0] + (Th[1] - O1[1]) * d[1]) / (d[0] ** 2 + d[1] ** 2); F = [O1[0] + t * d[0], O1[1] + t * d[1]]; R = [2 * F[0] - Th[0], 2 * F[1] - Th[1]]
    M = [(Tc[0] + Th[0]) / 2, (Tc[1] + Th[1]) / 2]
    return {"refl_Th": [round(R[0], 4), round(R[1], 4)], "gap_refl": round(math.dist(R, Tc), 4), "apex": [round(math.dist(O3, Tc), 4), round(math.dist(O3, Th), 4)], "gap_mid": round(math.dist(M, O3), 4)}[what]


def d_band(arm):
    """the verdict recomputed HERE from the PREREG rule (independent of pack_moy2.py), for the gated arms"""
    r = r4(sum(map(ln3, pf(arm))), len(pf(arm)))
    if arm == "olm119":
        dd = round(r - 0.122, 4); return "下がる" if dd <= -0.08 else "上がる" if dd >= 0.08 else "変わらない" if abs(dd) < 0.04 else "間"
    if arm == "olm124":
        return "戻る" if abs(r - 0.122) < 0.06 else "残る" if abs(r - 0.318) < 0.06 else "上がる" if r - 0.318 >= 0.06 else "下回る" if r - 0.122 <= -0.06 else "間"
    if arm == "olm125":
        dd = round(r - 0.108, 4); return "下がる" if dd <= -0.06 else "上がる" if dd >= 0.06 else "変わらない"
    if arm == "olm117":
        dd = round(r - r4(sum(map(ln3, pf("olm113"))), len(pf("olm113"))), 4); return "変わらない" if abs(dd) < 0.06 else "増える" if dd >= 0.12 else "減る" if dd <= -0.12 else "間"
    raise KeyError(arm)


# ---- v1.2 (BRIEF v1.2 G1 / G2 / G7 / G8 / G9 / G11): recounted HERE from the raw rows / read.json / PREREG text, not through the pack
def d_fisher_sides():
    """G7: how many of the seven pairs lie above / below the 0.05 reference tick"""
    p = d_fisher(); return [sum(1 for x in p if x >= 0.05), sum(1 for x in p if x < 0.05)]
def d_fisher_below():
    names = [["olm125", "olm124"], ["olm125", "pool_f"], ["olm125", "olm119"], ["olm127", "olm124"], ["olm127", "olm125"], ["olm127", "olm119"], ["pool_i", "pool_f"]]
    return [n for n, x in zip(names, d_fisher()) if x < 0.05]
def d_edges(arm):
    """G8: the band edges from the PREREG rule of the card, recomputed here (olm124: |Δ113| / |Δ119| < 0.06 around 0.122 / 0.318; olm125: |Δ124| < 0.06 around 0.108)"""
    if arm == "olm124": return [round(0.122 - 0.06, 3), round(0.122 + 0.06, 3), round(0.318 - 0.06, 3), round(0.318 + 0.06, 3)]
    if arm == "olm125": return [round(0.108 - 0.06, 3), round(0.108 + 0.06, 3)]
    raise KeyError(arm)
def d_typ_lens(): return [len(d_typ(a)) for a in ("olm113", "olm119", "olm122", "olm124", "olm125", "olm127")]
def d_frozen_words():
    """G11: the verdict words the script's last line may say (olm124 / olm119 / olm125 Q1; olm127 has none: G1 failed)"""
    return [READ[124]["Q1"]["verdict"], READ[119]["Q1"]["verdict"], READ[125]["Q1"]["verdict"], READ[127]["Q1"]["verdict"] if READ[127]["gates"]["G1_conj_parsed>=0.75"] else None]
def d_refl_of(a, k):
    """G1: the point the row reflected first (its reject computation starts '2F - Th' or '2F - Tc')"""
    return re.match(r"\s*2F\s*-\s*(Tc|Th)\b", d_row(a, k, "rej6_start")).group(1)
def d_mido3_counts(): return [sum(1 for r in rows("olm113") if r["cls"] == "MIDO3"), d_parsed("olm113"), sum(1 for r in rows("olm117") if r["cls"] == "MIDO3"), d_parsed("olm117")]


# ---- v1.3 (BRIEF v1.3 H1 / H2 / H5 / H6): recounted HERE from the raw rows / the RECORD and MEMO text
def d_rej_cap_proof(a): rj = [r for r in rows(a) if r["rej6"]]; return [len(rj), sum(1 for r in rj if r["hit_cap"]), sum(1 for r in rj if r["has_proof"]), sum(1 for r in rj if r["has_proof"] and ln6(r))]
def d_extra_rej(): return [r["key"] for a in ("olm119", "olm122") for r in rows(a) if r["rej6"] and not r["calc"]]
def d_record6():
    """H5: the candidate letters of RECORD §6 and whether MEMO §4 item 3's mechanism is (not) among them"""
    rec = (REPO / "cards/RECORD_moy2_reflection_tool_line_olm113_127_closure_20261104.md").read_text(encoding="utf-8").split("## §6.")[1].split("\n## ")[0]
    memo = (REPO / "cards/MEMO_youtube_selfplay_alphazero_factcheck_and_house_contrast_evaluation_function_20261104.md").read_text(encoding="utf-8").split("## §4.")[1].split("\n## ")[0]
    return ["".join(re.findall(r"^- \(([a-z])\)", rec, re.M)), "退けが commit を支配する仕組み" in memo.split("\n3. ")[1].split("\n4. ")[0], "退けが commit を支配する仕組み" in rec]


DERIVED = {k[2:]: v for k, v in globals().items() if k.startswith("d_")}


def get(obj, key):
    for part in (key if isinstance(key, list) else key.split(".")):
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def path_of(f): return REPO / f[5:] if f.startswith("repo:") else HERE / f
def load(f):
    p = path_of(f); return json.loads(p.read_text(encoding="utf-8")) if p.suffix == ".json" else p.read_text(encoding="utf-8")


AF = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "--anchors" else HERE / "claims_anchors.json"      # --anchors <file>: the positive control (a broken copy must fail)
anchors = json.loads(AF.read_text(encoding="utf-8"))
count, missing = 0, []
for a in anchors:
    count += 1
    try:
        k = a["kind"]
        if k == "json_equals": ok = get(load(a["file"]), a["key"]) == a["expect"]
        elif k == "derived": got = DERIVED[a["name"]](*a.get("args", [])); ok = got == a["expect"]
        elif k == "pack_equals_derived": got = DERIVED[a["name"]](*a.get("args", [])); ok = get(load("generated/pack.json"), a["key"]) == got
        elif k == "text_contains": ok = a["literal"] in path_of(a["file"]).read_text(encoding="utf-8")
        elif k == "md5": ok = hashlib.md5(path_of(a["file"]).read_bytes()).hexdigest() == a["expect"]
        else: raise ValueError("unknown kind " + k)
        if not ok and k in ("derived", "pack_equals_derived"): a = {**a, "error": f"got {got!r}"}
    except Exception as e:
        ok = False; a = {**a, "error": repr(e)}
    if not ok:
        missing.append((a["id"], a.get("file", a.get("name")), str(a.get("key", a.get("literal", "")))[:60], a.get("expect"), a.get("error", "differs")))
ids = [a["id"] for a in anchors]
dup = sorted({i for i in ids if ids.count(i) > 1})
claims = (HERE / "CLAIMS.md").read_text(encoding="utf-8") if (HERE / "CLAIMS.md").exists() else ""
rowids = set(re.findall(r"^\|\s*(K\d+)\s*\|", claims, re.M))
for i in sorted(set(ids) - rowids): missing.append((i, "CLAIMS.md", "an anchor without a claim row", None, "not in CLAIMS.md"))
for i in sorted(rowids - set(ids)): missing.append((i, "claims_anchors.json", "a claim row without an anchor", None, "no anchor"))
for i in dup: missing.append((i, "claims_anchors.json", "duplicate id", None, "dup"))
count += len(set(ids) ^ rowids)
print(f"anchors checked: {count} · missing or different: {len(missing)}")
for m in missing:
    print("  MISSING", m)
sys.exit(1 if missing else 0)
