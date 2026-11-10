"""check_claims.py — the FOURTH route of every number, and the coverage of the claims (moy-1).
Reads claims_anchors.json (an anchor = a file, a key and an expected value) and looks at the place itself, in the frozen files, with code that is written separately from
pack_moy1.py (route 1) and data.mjs (route 2): a stack-based JSON-object finder instead of raw_decode, its own regexes, its own counting.
  repo_json_equals     the value at `key` (dotted path; list indices are numbers) of a JSON file of the repo equals `expect`
  file_md5             the md5 of a repo file equals `expect`
  derived              a number RECOUNTED from scratch here (DERIVED[name](*args)) equals `expect`
  pack_equals_derived  the number the page carries (generated/pack.json at `key`) equals the recount
  derived_close        like `derived`, for numbers / lists / dicts of floats: equal within `tol` (default 1e-6: read.json's medians are float32 arithmetic, the recount here is float64)
  pack_close_derived   the pack's value at `key` equals the recount within `tol` (`pick` = a key / an index into the recount)
  pack_equals          the pack's value at `key` equals `expect` (the page carries the card's own value)
  repo_text_contains   a literal string occurs in a text file of the repo (the inventory's check_values.out: the BRIEF's values V1..V11, read by another author's script)
Coverage: every anchor's base id (K03a -> K03) must be a claim row of CLAIMS.md, and every claim row (K01..) must have at least one anchor.
It proves that the quoted words and values are there and that the counted numbers are the cards', not that a figure's sentence is a fair reading of them (that is the L3 half, for the reader).
    python3 -I check_claims.py          (exit 1 if anything is missing or differs)
"""
import glob
import hashlib
import json
import subprocess
from collections import Counter
import unicodedata
import math
import os
import pathlib
import re
import sys

import numpy as np                                       # v2: the olm59 arrays are recounted here (own loader, own windows by cumulative sums, own median)

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(os.environ.get("MOY1_REPO", pathlib.Path(__file__).resolve().parent / "data"))   # bundle: the frozen files are copied under data/ at their repo paths
def _git_fact(args):   # bundle: the `git log` answers recorded from the house repo (data/git_facts.json) when REPO is not a git checkout
    if (REPO / ".git").exists():
        import subprocess as _sp
        return _sp.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True).stdout
    _f = json.loads((pathlib.Path(__file__).resolve().parent / "data" / "git_facts.json").read_text(encoding="utf-8"))
    return _f["answers"][json.dumps(list(args), separators=(",", ":"), ensure_ascii=False)]
INV = REPO / "conversations/2026-10-28/explainer_moy1/inventory/check_values.out"


def J(rel):
    return json.loads((REPO / rel).read_text(encoding="utf-8"))


PC1 = "probes/olmo3-pc1-cue-invariance/results/pc1_runs.json"
CFG = "probes/moy1-claude5-replication/results/replication_config_frozen.json"
C13 = "probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt13_blocked_bind_moment_in_thinking.json"
C5 = "probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt5_first_token_fixed_sampling.json"
SCR = "probes/olmo3-base-bf16-screen/results/screen_olmo3_base_bf16.json"
THK = "probes/olmo3-behavior-screen/results/screen_olmo-3_32b.json"
SUITE = "ConstructGap/exp/moy_suite_report.json"
_cache = {}


def cached(rel):
    if rel not in _cache:
        _cache[rel] = J(rel)
    return _cache[rel]


def rows(cond, cue="nlnl"):
    return sorted([r for r in cached(PC1)["rows"] if r["cue_tag"] == cue and r["condition"] == cond], key=lambda r: r["seed"])


# ---- a different way to find the last JSON object that carries a field: scan for "{", match braces outside strings, json.loads the slice
def objects(text):
    i = 0
    while True:
        i = text.find("{", i)
        if i < 0:
            return
        depth, instr, esc, j = 0, False, False, i
        while j < len(text):
            ch = text[j]
            if instr:
                esc = (not esc) and ch == "\\"
                if ch == '"' and not esc:
                    instr = False
            elif ch == '"':
                instr = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        try:
            yield i, json.loads(text[i:j + 1])
            i = j + 1
        except Exception:
            i += 1


def last_field(text, field):
    got = ""
    for _, o in objects(re.sub(r"```(?:json)?", "", text)):
        if isinstance(o, dict) and field in o:
            got = str(o.get(field) or "")
    return got


def answer_text(r):
    # v3 (decision 1 of the BRIEF §2): the answer field is the last JSON's `conjecture`; a row with no JSON has none (v2 read the last paragraph: blocked s8 -> O1O2, 7 / 10; the frozen label_json_fields gives B-flail to every row without JSON in cmt5)
    return last_field(r["content"], "conjecture")


SUB = "₁₂"
O12 = re.compile(r"O[ _{]*[1" + SUB[0] + r"}]*\s*(?:and |, |- )?O[ _{]*[2" + SUB[1] + r"}]*")
HEHI = re.compile(r"(?<![A-Za-z])(?:He|Hi)(?![a-z])|H_[{]?[ei]")
CENTRE = re.compile(r"diameter|cent(?:er|re)|midpoint|mid-point|radius", re.I)
CIRC = re.compile(r"concyclic|cocircular|on (?:a|one|the) circle|lie on (?:a|one) circle|same circle", re.I)


def reading(a):
    if not a:
        return "other"
    if O12.search(a) and CENTRE.search(a):
        return "o1o2"
    if HEHI.search(a) and CENTRE.search(a):
        return "hehi"
    return "bare" if CIRC.search(a) else "other"


O_SENT = re.compile(r"(?:diameter|midpoint|center|centre)\s+(?:is\s+|of\s+|at\s+)?(?:the\s+)?(?:line\s+)?(?:segment\s+)?(?:(?:joining|connecting|between)\s+)?(?:the\s+)?(?:two\s+)?(?:centers\s+)?(?:\\\(\s*)?O_?\{?[12" + SUB + r"]\}?\s*(?:and\s+)?O", re.I)
HE_SENT = re.compile(r"diameter\s+(?:is\s+)?(?:the\s+)?(?:line\s+)?(?:segment\s+)?(?:(?:joining|connecting|between)\s+)?(?:\\\(\s*)?(?:HeHi|He and Hi|H_e)", re.I)


def d_reading_count(cond, kind):
    return sum(1 for r in rows(cond) if reading(answer_text(r)) == kind)


def d_sentence_rows(cond, which):
    rx = O_SENT if which == "O" else HE_SENT
    return [r["seed"] for r in rows(cond) if rx.search(r["content"])]


def d_he_hits(cond, seed):
    return len(HE_SENT.findall(next(r for r in rows(cond) if r["seed"] == seed)["content"]))


def d_frozen(cond):
    out = {}
    for r in rows(cond):
        out[r["label"]] = out.get(r["label"], 0) + 1
    return dict(sorted(out.items()))


def d_hehi_word_rows(cond):
    return [r["seed"] for r in rows(cond) if re.search(r"\bHe\b|\bHi\b", r["content"])]


def d_attractor_rows(cond):
    return [r["seed"] for r in rows(cond) if r["label"] == "B-attractor"]


def d_first_json(cond):
    return {str(r["seed"]): r["content"].find('{"conjecture"') for r in rows(cond)}


def d_json_first(cond):
    return [r["seed"] for r in rows(cond) if re.match(r"\s*\{\s*\"conjecture\"", r["content"])]


def d_prompts():
    p = cached(CFG)["prompts"]
    return p["open"], p["blocked"]


def d_tail_len():
    o, b = d_prompts()
    return len(b) - len(o)


def d_startswith():
    o, b = d_prompts()
    return b.startswith(o)


def d_tail_names_nothing():
    o, b = d_prompts()
    t = b[len(o):]
    return ("O1O2" not in t) and not re.search(r"\bHe\b|\bHi\b|HeHi", t)


def d_md5_prompt(which):
    o, b = d_prompts()
    return hashlib.md5((o if which == "open" else b).encode()).hexdigest()


def d_cue_bind(cue):
    if cue == "nl":
        xs = [r for r in cached(SCR)["rows"] if r["condition"] == "blocked" and not r["hit_cap"]]
    else:
        xs = [r for r in cached(PC1)["rows"] if r["cue_tag"] == ("space" if cue == "sp" else "nlnl") and r["condition"] == "blocked" and not r["hit_cap"]]
    return [sum(1 for r in xs if r["label"] == "B-bind"), len(xs)]


def d_cue_mode(cue):
    if cue == "nl":
        xs = [r for r in cached(SCR)["rows"] if r["condition"] == "blocked" and not r["hit_cap"]]
    else:
        xs = [r for r in cached(PC1)["rows"] if r["cue_tag"] == ("space" if cue == "sp" else "nlnl") and r["condition"] == "blocked" and not r["hit_cap"]]
    cnt = {}
    for r in xs:
        cnt[r["label"]] = cnt.get(r["label"], 0) + 1
    top = max(cnt.values())
    return [k for k, v in cnt.items() if v == top]


def d_he_end():
    return {str(r["seed"]): reading(answer_text(r)) for r in rows("blocked") if HE_SENT.search(r["content"])}


def d_order():
    out = {}
    for r in rows("blocked"):
        if r["label"] == "B-bind":
            h, o = HE_SENT.search(r["content"]), O_SENT.search(r["content"])
            if h and o:
                out[str(r["seed"])] = "He" if h.start() < o.start() else "O"
    return out


def d_pair(key, which):
    OG, HG = {"L57H33", "L34H3", "L52H26", "L51H4"}, {"L50H23", "L51H19", "L43H24", "L42H33"}
    th = cached(C13)["sites"][key]["top_heads"][:10]
    return sum(h["contrib"] for h in th if h["head"] in (OG if which == "O" else HG))


def d_l50_rank1(kind):
    n = 0
    for k, x in cached(C13)["sites"].items():
        if k.startswith(kind + "|") and x["top_heads"] and x["top_heads"][0]["head"] == "L50H23":
            n += 1
    return n


def d_cmt5(cell):
    return cached(C5)["cells"][cell]["labels"].get("B-bind", 0)


def d_think(cond):
    xs = [r for r in cached(THK)["rows"] if r["condition"] == cond and r["done_reason"] != "length"]
    cnt = {}
    for r in xs:
        cnt[r["label"]] = cnt.get(r["label"], 0) + 1
    return cnt


def d_ratio(which):
    txt = d_prompts()[0]
    P = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(r"^(O1|O2|X1|X2|X3|X4|He|Hi) = \(([-\d.]+), ([-\d.]+)\)", txt, re.M)}
    a, b = (P["O1"], P["O2"]) if which == "O" else (P["He"], P["Hi"])
    c = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    r = math.dist(a, b) / 2
    return [round(math.dist(P[k], c) / r, 3) for k in ("X1", "X2", "X3", "X4")]


def d_otok_open_s1():
    t = next(r for r in rows("open") if r["seed"] == 1)["content"]
    toks = [m.start() for m in re.finditer(r"O1O2|O_1O_2|O_\{1\}O_\{2\}|O₁O₂|O1 and O2|O_1 and O_2|O₁ and O₂", t)]
    return [len(toks), sum(1 for q in toks if re.search(r"line|slope", t[max(0, q - 80):q + 80], re.I))]


# ============================================================================================ v2: olm59 (BRIEF v2 §1 / §3) — recounted from the npz arrays with code that is not the pack's
O59 = "ConstructGap/exp/olm59"
_o59 = {}


def o59_rows():
    """every row once: stem -> (meta, group_mean float64, flags, text). The loader and everything below are written separately from pack_moy1.py (cumulative sums for the windows, a hand-written median)."""
    if not _o59:
        for p in sorted((REPO / O59 / "rows").glob("*.npz")):
            z = np.load(p, allow_pickle=False)
            _o59[p.stem] = (json.loads(str(z["meta"])), np.asarray(z["group_mean"], dtype=np.float64), np.asarray(z["flags"]), str(z["text"]))
    return _o59


def median(xs):
    t = sorted(xs)
    n = len(t)
    return t[n // 2] if n % 2 else (t[n // 2 - 1] + t[n // 2]) / 2


GI = {"close": 0, "mid": 1, "ans": 2, "think": 3}
FB = {"o_diam": 2, "h_diam": 3}


def o59_windows(ev):
    """stem -> (before[4], after[4]) for the rows whose first `ev` token has 32 tokens on both sides inside the generation; before = [e-32, e), after = [e, e+32)"""
    out = {}
    for stem, (m, g, fl, _) in o59_rows().items():
        col = fl[:, FB[ev]]
        e = next((i for i in range(len(col)) if col[i]), None)
        if e is None or e < 32 or e + 32 > len(col):
            continue
        cs = np.vstack([np.zeros((1, 4)), np.cumsum(g, axis=0)])
        out[stem] = ((cs[e] - cs[e - 32]) / 32, (cs[e + 32] - cs[e]) / 32, e, m)
    return out


def d_o59_q3(ev, grp, oc):
    w = [(a[GI[grp]] - b[GI[grp]]) for b, a, e, m in o59_windows(ev).values() if oc == "all" or m["label_json"] == oc]
    return [len(w), sum(1 for x in w if x > 0), median(w)]


def d_o59_q(which):
    if which == "Q1":
        w = [(a[0] - b[0]) for b, a, e, m in o59_windows("o_diam").values() if m["kind"] == "think" and m["label_json"] == "B-bind"]
    else:
        w = [(a[0] - b[0]) for b, a, e, m in o59_windows("h_diam").values()]
    return [len(w), sum(1 for x in w if x > 0), median(w)]


def d_o59_scene(stem, ev):
    m, g, fl, _ = o59_rows()[stem]
    col = fl[:, FB[ev]]
    e = next(i for i in range(len(col)) if col[i])
    b, a, _, _ = o59_windows(ev)[stem]
    return {"n": len(g), "event": e, "before": list(b), "after": list(a)}


def d_o59_rank(stem, ev, grp):
    d = {k: (a[GI[grp]] - b[GI[grp]]) for k, (b, a, e, m) in o59_windows(ev).items()}
    v = d[stem]
    return [1 + sum(1 for x in d.values() if x > v), 1 + sum(1 for x in d.values() if abs(x) > abs(v)), len(d)]


def d_o59_scene_choice():
    o = sorted(((len(o59_rows()[k][1]), k) for k, (b, a, e, m) in o59_windows("o_diam").items() if m["kind"] == "think" and m["label_json"] == "B-bind"))
    h = sorted(((len(o59_rows()[k][1]), k) for k, (b, a, e, m) in o59_windows("h_diam").items() if m["label_json"] == "B-attractor"))
    return [o[0][1], o[0][0], o[1][0], h[0][1], h[0][0], h[1][0]]                     # the shortest id and length, and the next length (a unique minimum)


def d_o59_counts():
    rows = o59_rows()
    first = lambda ev: sum(1 for (m, g, fl, t) in rows.values() if fl[:, FB[ev]].any())
    tot = {n: int(sum(int(fl[:, i].sum()) for (m, g, fl, t) in rows.values())) for i, n in enumerate(["o_name", "h_name", "o_diam", "h_diam", "circle", "json"])}
    return {"rows_o": first("o_diam"), "rows_h": first("h_diam"), "fit_o": len(o59_windows("o_diam")), "fit_h": len(o59_windows("h_diam")), "tokens": tot}


def d_o59_labels():
    out = {}
    for (m, g, fl, t) in o59_rows().values():
        k = f"{m['kind']}|{m['label']}|{m['label_json']}"
        out[k] = out.get(k, 0) + 1
    return dict(sorted(out.items()))


def d_o59_manifest_md5():
    lines = "".join(f"{p.name} {hashlib.md5(p.read_bytes()).hexdigest()}\n" for p in sorted((REPO / O59 / "rows").glob("*.npz")))
    return hashlib.md5(lines.encode("utf-8")).hexdigest()


def d_cmt5_bind(path, which):
    """bind rows of cmt5 pooled over F5a-2 and F5b-1: which = full (the whole-text label) | field (label_json_fields)"""
    key = "label" if which == "full" else "label_json_fields"
    return sum(1 for v in ("F5a-2", "F5b-1") for r in cached(C5)["cells"][f"{v}|{path}"]["rows"] if r[key] == "B-bind")


def d_cmt5_bind_cell(cell, which):
    key = "label" if which == "full" else "label_json_fields"
    return sum(1 for r in cached(C5)["cells"][cell]["rows"] if r[key] == "B-bind")


def d_cmt5_full_bind_to(path):
    out = {}
    for v in ("F5a-2", "F5b-1"):
        for r in cached(C5)["cells"][f"{v}|{path}"]["rows"]:
            if r["label"] == "B-bind":
                out[r["label_json_fields"]] = out.get(r["label_json_fields"], 0) + 1
    return dict(sorted(out.items()))


# ============================================================================================ v2.1: olm62 and the card tree — recounted here with code that is not the pack's / data.mjs's
# (own loader of the arrays, own regex for a token's formula-character share, own selection of the events, own rank code; the window means of the share are the direct means of the card's arithmetic: the rank rule is tie-sensitive)
MATHRE = re.compile(r"[0-9²³·×=+\-^*/()√]")
_tf = {}


def o62_tokfrac(stem):
    if stem not in _tf:
        z = np.load(REPO / O59 / "rows" / f"{stem}.npz", allow_pickle=False)
        tx, st, en = str(z["text"]), z["starts"], z["ends"]
        _tf[stem] = np.array([(len(MATHRE.findall(tx[int(a):int(b)])) / (int(b) - int(a))) if int(b) > int(a) else 0.0 for a, b in zip(st, en)])
    return _tf[stem]


def o62_events(ev):
    out = {}
    for stem, (b, a, e, m) in o59_windows(ev).items():
        tf = o62_tokfrac(stem)
        out[stem] = (a - b, float(tf[e:e + 32].mean() - tf[e - 32:e].mean()), m["kind"], m["label_json"])
    return out


def ordinal(x):                                         # the card's rank rule: ordinal ranks (argsort of argsort, numpy's default sort), not tie-averaged
    return np.argsort(np.argsort(np.asarray(x, dtype=np.float64)))


def rho(a, b):
    return float(np.corrcoef(ordinal(a), ordinal(b))[0, 1])


def d_o62(ev, key):
    E = o62_events(ev)
    dm, dma = [v[0][1] for v in E.values()], [v[1] for v in E.values()]
    up, flat = [x > 0 for x in dma], [x <= 0 for x in dma]
    med = float(np.median(dma))
    frac = lambda sel, vals: f"{sum(1 for v, s in zip(vals, sel) if s and v > 0)} / {sum(sel)}"
    if key == "math":
        return [len(dma), sum(up), med]
    if key == "spearman":
        return rho(dm, dma)
    if key == "flat":
        return frac(flat, dm)
    if key == "upd":
        return frac(up, dm)
    if key == "mid_median_flat":
        return float(np.median([v for v, s in zip(dm, flat) if s]))
    if key == "split":
        lo = [x <= med for x in dma]
        return [frac(lo, dm), frac([not s for s in lo], dm)]
    if key == "flat_groups":
        return [frac(flat, [v[0][g] for v in E.values()]) for g in range(4)]
    raise KeyError(key)


def d_o62_pooled():
    stems = sorted(o59_rows())
    return rho(np.concatenate([o59_rows()[s][1][:, 1] for s in stems]), np.concatenate([o62_tokfrac(s) for s in stems]))


def d_o62_c2():
    dig = digpos = alp = alpzero = 0
    for s in sorted(o59_rows()):
        z = np.load(REPO / O59 / "rows" / f"{s}.npz", allow_pickle=False)
        tx, st, en = str(z["text"]), z["starts"], z["ends"]
        for a, b, f in zip(st, en, o62_tokfrac(s)):
            t = tx[int(a):int(b)]
            if t.isdigit() and t.isascii():
                dig += 1
                digpos += 1 if f > 0 else 0
            u = t.strip()
            if u and all(unicodedata.category(c).startswith("L") for c in u):
                alp += 1
                alpzero += 1 if f == 0 else 0
    return [dig, digpos, alp, alpzero]


def d_o62_events(ev):
    return [{"id": k, "kind": v[2], "lj": v[3], "dmid": float(v[0][1]), "dmath": v[1]} for k, v in o62_events(ev).items()]


def d_o62_point(stem, ev):
    E = o62_events(ev)
    v = E[stem]
    return {"id": stem, "dmid": float(v[0][1]), "dmath": v[1], "rank_math": 1 + sum(1 for x in E.values() if x[1] > v[1]), "n": len(E)}


def d_o62_flat():
    return sorted(({"id": k, "kind": v[2], "dmid": float(v[0][1]), "dmath": v[1]} for k, v in o62_events("o_diam").items() if v[1] <= 0), key=lambda z: z["dmid"])


TREE = "conversations/2026-10-27/card_tree_v2/entry_merged_v2_2_1/tree_src.json"


def d_tree(what, *a):
    T = cached(TREE)
    dates = lambda ids: sorted(next(n for n in T["nodes"] if n["id"] == m)["date"] for m in ids)
    if what == "counts":
        return [len(T["clusters"]), len(T["nodes"])]
    if what == "cluster_n":
        return [len(c["members"]) for c in T["clusters"]]
    if what == "span":
        ds = sorted(n["date"] for n in T["nodes"])
        return [ds[0][5:], ds[-1][5:]]
    if what == "node":
        return next(x for x in T["nodes"] if x["id"] == a[0])[a[1]]
    if what == "cluster_field":
        return T["clusters"][a[0]][a[1]]
    if what == "cluster_span":
        ds = dates(T["clusters"][a[0]]["members"])
        return [ds[0][5:], ds[-1][5:]]
    raise KeyError(what)


def d_name_date(rel):
    m = re.search(r"_(\d{8})\.md$", rel)
    return m.group(1)[4:6] + "-" + m.group(1)[6:8]


def d_git_date(rel):                                    # a read of git's log (the file's last commit)
    return _git_fact(["log", "-1", "--format=%ad", "--date=short", "--", rel]).strip()[5:]


# ============================================================================================ v3: the part added after the 10-28 figure, and what v3 transplanted — recounted here with code that is not the pack's / data.mjs's
def d_freeze(card):
    """the first 8 hex digits of the commit that first added the card's PREREG (git) — the RESULT's first lines name the PREREG by a link (own regex, own git call)"""
    hits = sorted(glob.glob(str(REPO / f"conversations/*/RESULT_{card}_moy1_*.md")))
    assert len(hits) == 1, (card, hits)
    head = "\n".join(pathlib.Path(hits[0]).read_text(encoding="utf-8").splitlines()[:9])
    link = re.search(r"\[PREREG\]\(([^)]+)\)", head).group(1)
    rel = os.path.normpath(os.path.join(os.path.dirname(os.path.relpath(hits[0], REPO)), link))
    out = _git_fact(["log", "--diff-filter=A", "--format=%H", "--", rel]).split()
    return out[-1][:8]


def d_angle(which, k):
    P = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(r"^(O1|O2|X1|X2|X3|X4|He|Hi) = \(([-\d.]+), ([-\d.]+)\)", cached(CFG)["prompts"]["open"], re.M)}
    a, b = ("O1", "O2") if which == "O" else ("He", "Hi")
    x = P[f"X{k}"]
    v, w = (P[a][0] - x[0], P[a][1] - x[1]), (P[b][0] - x[0], P[b][1] - x[1])
    return math.degrees(math.atan2(abs(v[0] * w[1] - v[1] * w[0]), v[0] * w[0] + v[1] * w[1]))


def d_f5(which):
    a, b = cached("probes/olmo3-f5-think-prefix/results/f5_runs_F5a-2.json"), cached("probes/olmo3-f5-think-prefix/results/f5_runs_F5b-1.json")
    if which == "edit":
        return [len(a["edits_applied"]), a["edits_applied"][0]["key"], a["edits_applied"][0]["replacement"].split("\n")[0]]
    return [a["cue"], b["cue"], a["condition"], b["condition"]]


def d_base(cond):
    rs = rows(cond)
    return {"labels": dict(Counter(r["label"] for r in rs)), "cap": sum(1 for r in rs if r["hit_cap"]), "labels_no_cap": dict(Counter(r["label"] for r in rs if not r["hit_cap"]))}


def d_nojson_cmt5():
    got = [r for cell in cached(C5)["cells"].values() for r in cell["rows"] if not any(isinstance(o, dict) and "conjecture" in o for _, o in objects(re.sub(r"```(?:json)?", "", r["content"])))]
    return {"n": len(got), "label_json_fields": dict(Counter(r["label_json_fields"] for r in got)), "label_full": dict(Counter(r["label"] for r in got))}


def d_forced():
    return {k: v["forced"] for k, v in cached(C5)["cells"].items()}


def d_slopes(ev):
    return [{"id": k, "kind": m["kind"], "lj": m["label_json"], "d": [round(float(x), 5) for x in (a - b)]} for k, (b, a, e, m) in sorted(o59_windows(ev).items())]


def d_bykind(ev):
    c = Counter(f"{m['kind']}|{m['label_json']}" for b, a, e, m in o59_windows(ev).values())
    return dict(sorted(c.items()))


def d_wordcirc():
    stem = "F5a-2__think__r15"
    z = np.load(REPO / O59 / "rows" / f"{stem}.npz", allow_pickle=False)
    tx, st, en = str(z["text"]), z["starts"], z["ends"]
    sent = "the center of the circle through the four common tangent points is the midpoint of the line segment joining the centers of the two original circles."
    a, m = tx.find(sent), tx.find("midpoint of the line segment")
    ev = o59_windows("o_diam")[stem][2]
    ta, tb, tm = int(np.searchsorted(st, a, side="right")) - 1, int(np.searchsorted(en, a + len(sent), side="left")), int(np.searchsorted(st, m, side="right")) - 1
    return [tx.count(sent), ta, tb, tm, tm - ev, ev]


def avg_rank(x):
    x = np.asarray(x, dtype=np.float64)
    order, r, i = np.argsort(x, kind="stable"), np.empty(len(x)), 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and x[order[j + 1]] == x[order[i]]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return r


def d_o62_tie(which):
    if which == "pooled":
        stems = sorted(o59_rows())
        a, b = np.concatenate([o59_rows()[s][1][:, 1] for s in stems]), np.concatenate([o62_tokfrac(s) for s in stems])
    else:
        E = o62_events(which)
        a, b = [v[0][1] for v in E.values()], [v[1] for v in E.values()]
    return float(np.corrcoef(avg_rank(a), avg_rank(b))[0, 1])


def d_cue_start(cue):
    scr = cached(SCR)["rows"] if cue == "nl" else [r for r in cached(PC1)["rows"] if r["cue_tag"] == ("space" if cue == "sp" else "nlnl")]
    bl = [r for r in scr if r["condition"] == "blocked" and not r["hit_cap"]]
    js = lambda r: re.match(r'\{"conjecture"', r["content"]) is not None
    early = lambda r: (lambda m: m is not None and m.start() <= 100)(re.search(r'\{"conjecture"', r["content"]))
    b = lambda r: r["label"] == "B-bind"
    return {"n": len(bl), "json": sum(js(r) for r in bl), "text": sum(not js(r) for r in bl), "bind": sum(b(r) for r in bl), "json_bind": sum(js(r) and b(r) for r in bl), "text_bind": sum((not js(r)) and b(r) for r in bl),
            "early": sum(early(r) for r in bl), "early_bind": sum(early(r) and b(r) for r in bl), "late": sum(not early(r) for r in bl), "late_bind": sum((not early(r)) and b(r) for r in bl)}


def d_cue_first(cue):
    rs = [r for r in cached(PC1)["rows"] if r["cue_tag"] == cue and r["condition"] == "blocked" and not r["hit_cap"]]
    return sorted(r["content"].find('{"conjecture"') for r in rs if '{"conjecture"' in r["content"])


def d_marks_rule(n):
    """the card marks of state n by the rule (decision 4): the cards of the data the state draws (config.json state_data -> card_of_data), as a sorted set"""
    cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
    return sorted({c for k in cfg["state_data"][n] for c in cfg["card_of_data"][k]})


def d_olm62_q2_rule():
    t = (REPO / "conversations/2026-10-28/PREREG_olm62_moy1_mid_rise_vs_math_shift_20261028.md").read_text(encoding="utf-8")
    return ["8 本未満なら「読まない」" in t]


DERIVED = {
    "freeze": d_freeze, "angle": d_angle, "f5": d_f5, "base": d_base, "nojson_cmt5": d_nojson_cmt5, "forced": d_forced, "slopes": d_slopes, "bykind": d_bykind, "wordcirc": d_wordcirc, "o62_tie": d_o62_tie, "cue_start": d_cue_start, "cue_first": d_cue_first, "marks_rule": d_marks_rule, "olm62_q2_rule": d_olm62_q2_rule,
    "o62": d_o62, "o62_pooled": d_o62_pooled, "o62_c2": d_o62_c2, "o62_events": d_o62_events, "o62_point": d_o62_point, "o62_flat": d_o62_flat, "tree": d_tree, "name_date": d_name_date, "git_date": d_git_date,
    "o59_q3": d_o59_q3, "o59_q": d_o59_q, "o59_scene": d_o59_scene, "o59_rank": d_o59_rank, "o59_scene_choice": d_o59_scene_choice, "o59_counts": d_o59_counts, "o59_labels": d_o59_labels, "o59_manifest_md5": d_o59_manifest_md5,
    "cmt5_bind": d_cmt5_bind, "cmt5_bind_cell": d_cmt5_bind_cell, "cmt5_full_bind_to": d_cmt5_full_bind_to,
    "reading_count": d_reading_count, "sentence_rows": d_sentence_rows, "he_hits": d_he_hits, "frozen": d_frozen, "hehi_word_rows": d_hehi_word_rows, "attractor_rows": d_attractor_rows,
    "first_json": d_first_json, "json_first": d_json_first, "tail_len": d_tail_len, "startswith": d_startswith, "tail_names_nothing": d_tail_names_nothing, "md5_prompt": d_md5_prompt,
    "cue_bind": d_cue_bind, "cue_mode": d_cue_mode, "he_end": d_he_end, "order": d_order, "pair": d_pair, "l50_rank1": d_l50_rank1, "cmt5": d_cmt5, "think": d_think, "ratio": d_ratio, "otok_open_s1": d_otok_open_s1,
}


def close(a, b, tol):
    if isinstance(a, dict):
        return isinstance(b, dict) and set(a) == set(b) and all(close(a[k], b[k], tol) for k in a)
    if isinstance(a, (list, tuple)):
        return isinstance(b, (list, tuple)) and len(a) == len(b) and all(close(x, y, tol) for x, y in zip(a, b))
    if isinstance(a, float) or isinstance(b, float):
        return abs(a - b) <= tol
    return a == b


def get(obj, key):
    for part in key.split("."):
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


anchors = json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8"))
pack = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8")) if (HERE / "generated" / "pack.json").exists() else {}
count, missing = 0, []
inv_text = INV.read_text(encoding="utf-8") if INV.exists() else ""


def evaluate(a):
    """(ok, err) of one anchor"""
    err = None
    try:
        k = a["kind"]
        if k == "repo_json_equals":
            ok = get(cached(a["file"]), a["key"]) == a["expect"]
        elif k == "file_md5":
            ok = hashlib.md5((REPO / a["file"]).read_bytes()).hexdigest() == a["expect"]
        elif k == "derived":
            got = DERIVED[a["name"]](*a.get("args", []))
            ok = (got == a["expect"]) if not isinstance(got, float) else abs(got - a["expect"]) < 1e-12
        elif k == "pack_equals_derived":
            ok = get(pack, a["key"]) == DERIVED[a["name"]](*a.get("args", []))
        elif k == "derived_close":
            got = DERIVED[a["name"]](*a.get("args", []))
            got = got[a["pick"]] if "pick" in a else got
            ok = close(got, a["expect"], a.get("tol", 1e-6))
        elif k == "pack_close_derived":
            got = DERIVED[a["name"]](*a.get("args", []))
            got = got[a["pick"]] if "pick" in a else got
            ok = close(get(pack, a["key"]), got, a.get("tol", 1e-6))
        elif k == "here_json_equals":                  # a json file of this folder (config.json: the card marks)
            ok = get(json.loads((HERE / a["file"]).read_text(encoding="utf-8")), a["key"]) == a["expect"]
        elif k == "pack_equals":
            got = get(pack, a["key"])
            ok = got == a["expect"]
        elif k == "repo_text_contains":
            ok = a["literal"] in (REPO / a["file"]).read_text(encoding="utf-8")
        elif k == "repo_json_close":                   # v3: a float of a frozen file is within `tol` of the value the RESULT / SCOPE prints (the printed value is rounded)
            got = get(cached(a["file"]), a["key"])
            ok = abs(got - a["expect"]) <= a["tol"]
        elif k == "pack_equals_json":                  # v3: the number the page carries equals the frozen file's, unchanged
            got = get(pack, a["key"])
            ok = got == get(cached(a["file"]), a["jkey"])
        else:
            raise ValueError("unknown kind " + k)
        if k != "repo_text_contains" and not ok:
            err = f"got {got if k in ('derived', 'derived_close', 'pack_close_derived', 'pack_equals', 'repo_json_close', 'pack_equals_json') else '?'}"
    except Exception as e:                       # a missing file / key is a missing anchor, not a crash
        ok, err = False, repr(e)
    return ok, err


for a in anchors:
    count += 1
    ok, err = evaluate(a)
    if not ok:
        missing.append((a["id"], a.get("file", a.get("name")), a.get("key", a.get("literal", "")), a.get("expect"), err or "differs"))

# the control of the checker itself (it breaks in both directions): five anchors of v2, each wrong in one way, must be reported
MUTATE = {"K25b": lambda a: {**a, "expect": a["expect"] + 1}, "K25br": lambda a: {**a, "expect": [a["expect"][0], a["expect"][1] - 1, a["expect"][2]]}, "K23c": lambda a: {**a, "pick": "after"},
          "K27c": lambda a: {**a, "literal": a["literal"].replace("70", "71")}, "K27e": lambda a: {**a, "expect": 0.71},
          "K32i": lambda a: {**a, "expect": a["expect"] + 0.001}, "K33i": lambda a: {**a, "expect": "8 / 11"}, "K40b": lambda a: {**a, "expect": [6, 13, 10, 6, 13, 8, 7, 11, 5]}, "K43l": lambda a: {**a, "expect": ["cmt13"]}}
caught = [not evaluate(MUTATE[a["id"]](a))[0] for a in anchors if a["id"] in MUTATE]
control_ok = len(caught) == len(MUTATE) and all(caught)
if not control_ok:
    missing.append(("control", "check_claims.py", "a wrong anchor was not reported", None, f"{sum(caught)} / {len(MUTATE)}"))

# coverage: CLAIMS.md <-> anchors (base ids: K03a -> K03)
base = lambda i: re.match(r"K\d+", i).group(0)
ids = {base(a["id"]) for a in anchors}
claims = (HERE / "CLAIMS.md").read_text(encoding="utf-8") if (HERE / "CLAIMS.md").exists() else ""
rowids = set(re.findall(r"^\|\s*(K\d+)\s*\|", claims, re.M))
for i in sorted(ids - rowids):
    missing.append((i, "CLAIMS.md", "an anchor without a claim row", None, "not in CLAIMS.md"))
for i in sorted(rowids - ids):
    missing.append((i, "claims_anchors.json", "a claim row without an anchor", None, "no anchor"))
count += len(ids ^ rowids)
print(f"anchors checked: {count} · missing or different: {len(missing)} · claim rows {len(rowids)} · control: {sum(caught)} / {len(MUTATE)} wrong anchors reported · anchors per kind " + str({k: sum(1 for a in anchors if a['kind'] == k) for k in sorted({a['kind'] for a in anchors})}))
for m in missing:
    print("  MISSING", m)
sys.exit(1 if missing else 0)
