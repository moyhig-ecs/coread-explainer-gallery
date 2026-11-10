"""check_claims.py — the THIRD route of every number, and the coverage of the claims. Reads claims_anchors.json (an anchor = a place + an expected value) and looks at the place itself:
  count        the number of rows of `files` (filtered by model / arm / variant; only rows with `raw` unless raw_only = false) whose `field` is true      == expect
  n            the number of such rows                                                                                                          == expect
  route5       the number of prf1 rows whose route5 == value                                                                                     == expect
  median       the median of a numeric field (dotted path) over such rows                                                                       == expect
  pack_cell    the value the page carries (generated/pack.json cells[cell][key]) == the same recount done here (field / n / route5 / median)
  text_contains  a literal string occurs in a text file (read as TEXT)
  md5          the md5 of a file starts with `expect`
  phrase       a literal occurs in the `raw` of one row (file, model, arm, rep)
  summary_sum  the API high knowledge arms of the SUMMARY's frozen table (md5 556b9dfb) sum to expect_n / expect_cut / expect_ans (parsed here, separately from pack_data.py)
  construct    the construction recomputed here from the frozen question's coordinates gives K, P_y, J within `tol`
  json_key     (v2) a value at a key path (a list) of a card's output json (ConstructGap/exp/<file>) == expect (within `tol` if given)
  cell_counts  (v2) one strip as the page prints it: answer field / whole / floor / n recounted from raw (G-22: every strip's numbers anchored)
  median_len   (v2.1) the median of len(field) over the selected rows (the `relations` lists: mean of the two middle rows)
  median_high  (v2.1) statistics.median_high of a numeric field (the SUMMARY §6 table's thinking values)
  count_all    (v2.1) the number of selected rows whose `fields` are ALL true (a locus sentence and a cut in the same answer field)
  grade_rule   (v2.1) the grade rule of BRIEF v2.1 §2-5 recomputed HERE from SCOPE 10-31 (rule i: a whole-token name in the 根拠 column / a 言えない bullet; first of 判定 > 較正 > 記述 > 言えない)
               or from the card's RESULT line (rule ii, `literal`) — independently of pack_data.py — == expect
  grade_sum    (v2.1) the five columns over the 20 cards recomputed here == expect (their sum must be 20)
  cone         (v2.2) BRIEF v2.2 §1 recomputed here from the frozen coordinates: C on the tangents f (at G) and g (at E), F the antipode of G, GE perpendicular to the axis CA,
               the half-angle asin(r / CA), and P_y lifted above H on the cone (`q` names the quantity; |value - expect| <= tol)
  plane        (v2.3) BRIEF v2.3 §1 recomputed here from the frozen coordinates: the cutting plane through the line FVD (line j) perpendicular to the board — V and D on j, V the midpoint of FD,
               the distance from A to j (= r) and AF ⟂ j, the unit along j, the parabola's samples (vertex j ∩ g, focus F, up to P_y lifted above H) in the plane and on the cone, the plane ⟂ the board
  Coverage reads every CLAIMS*.md (v2 splits the ledger into CLAIMS.md · CLAIMS_cells.md · CLAIMS_after.md, each < 60 KB).
It never imports pack_data.py / data.mjs / an experiment's script. Coverage: every anchor id must be a row of CLAIMS.md and every row id of CLAIMS.md must have an anchor.
    python -I check_claims.py          (exit 1 if anything is missing or differs)
"""
import hashlib
import json
import math
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(__import__("os").environ.get("MOY5_REPO", HERE / "data"))   # bundle: the frozen files are copied under data/ at their repo paths (MOY5_REPO = another root, e.g. the house repo)
X = REPO / "ConstructGap" / "exp"
_cache = {}


def rows_of(f):
    if f not in _cache:
        _cache[f] = [json.loads(l) for l in (X / f).read_text(encoding="utf-8").splitlines() if l.strip()]
    return _cache[f]


def select(a):
    rs = [r for f in a["files"] for r in rows_of(f)]
    for k in ("model", "arm", "variant"):
        if k in a:
            rs = [r for r in rs if r.get(k) == a[k]]
    if a.get("raw_only", True):
        rs = [r for r in rs if r.get("raw")]
    return rs


def dig(obj, path):
    for p in path.split("."):
        obj = obj[p]
    return obj


def recount(a):
    rs = select(a)
    if "field" in a:
        return sum(bool(r.get(a["field"])) for r in rs)
    if "route5" in a:
        return sum(r.get("route5") == a["route5"] for r in rs)
    if "median" in a:
        return statistics.median(dig(r, a["median"]) for r in rs)
    return len(rs)


def expected_dots(c):
    """the dots of a cell, from raw (used by make_check.py's page-vs-raw check; the rules are the figure's legend, written here a second time)"""
    rs = [r for f in c["files"] for r in rows_of(f)]
    rs = [r for r in rs if r.get("arm") == c["arm"]]
    if c["kind"] in ("olm", "olmk"):
        v = c["id"].split(".")[1] if c["id"].startswith("olm1.") else None
        rs = [r for r in rs if v is None or r.get("variant") == v]
    else:
        full = {"Opus 5.5": "claude-opus-5-5", "Fable 5.1": "claude-fable-5-1", "Sonnet 5.5": "claude-sonnet-5-5", "Haiku 5.5": "claude-haiku-5-5", "Argon": "gemini-4-argon"}[c["model"]]
        rs = [r for r in rs if r.get("model") == full and r.get("raw")]
    rs.sort(key=lambda r: r["rep"])
    out = []
    for r in rs:
        if c["kind"] == "cut":
            out.append("A" if r.get("cut_in_conjecture") else "R" if r.get("bind") else "F" if r.get("closure") else "N")
        elif c["kind"] == "prf1":
            out.append({"END-only": "E", "CHAIN": "C", "LAT-only": "L", "none": "N"}[r["route5"]])
        elif c["kind"] == "prf3":
            out.append("Sm" if r["lat_sym"] and r["malformed"] else "S" if r["lat_sym"] else "M" if r["malformed"] else "D" if r["fd_use"] else "N")
        elif c["kind"] == "olmk":
            out.append("Z" if not r.get("raw") or ("conjecture" not in r and not r.get("ok")) else "A" if r.get("cut_in_conjecture") else "R" if r.get("bind") else "F" if r.get("closure") else "N")
        else:
            out.append("Z" if not r.get("raw") or ("conjecture" not in r and not r.get("ok")) else "F" if r.get("closure") else "N")
    return "".join(out)


def summary_sum():
    t = (REPO / "conversations/2026-10-16/data_moy5_summary/summary_table_moy5_cut_all_cards_20261016.txt").read_text(encoding="utf-8")
    n = cut = ans = 0
    arms = set()
    for line in t.splitlines():
        if not re.match(r"^(Haiku|Sonnet|Opus|Fable) \d\.\d\s+API\s+high\s", line):
            continue
        cols = [c.strip() for c in line.split("|")]
        head = cols[0].split()
        card, arm = head[-3], head[-2]
        if arm in ("K", "K@U", "Bbp", "E-full+Bbp"):
            continue
        arms.add((card, arm))
        n += int(cols[1]); cut += int(cols[2].split()[0]); ans += int(cols[4])
    return n, cut, ans, len(arms)


def construct_err():
    src = (REPO / "conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md").read_text(encoding="utf-8")
    P = {m[1]: (float(m[2]), float(m[3])) for m in re.finditer(r"^(\w+) = \((-?[\d.]+), (-?[\d.]+)\)$", src, re.M) if m[1] in ("A", "G", "E", "F", "V", "Px", "K", "Py", "J")}
    def meet(p, u, q, v):
        d = u[0] * v[1] - u[1] * v[0]; t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / d
        return (p[0] + u[0] * t, p[1] + u[1] * t)
    perp = lambda v: (-v[1], v[0]); sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
    fd, gd = perp(sub(P["G"], P["A"])), perp(sub(P["E"], P["A"]))
    D = meet(P["G"], sub(P["E"], P["G"]), P["F"], fd); ed = perp(fd)
    K = meet(P["F"], sub(P["Px"], P["F"]), D, ed); Py = meet(P["Px"], perp(sub(P["Px"], P["F"])), K, fd)
    H = meet(Py, ed, P["F"], fd); J = meet(H, sub(P["E"], P["G"]), P["E"], gd)
    return max(math.dist(K, P["K"]), math.dist(Py, P["Py"]), math.dist(J, P["J"]))


def cone_geom():
    """(v2.2) BRIEF v2.2 §1 recomputed HERE from the frozen question's coordinates (SOURCE 10-14), apart from figure.js: the board = the plane through the axis of the cone with apex C"""
    src = (REPO / "conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md").read_text(encoding="utf-8")
    P = {m[1]: (float(m[2]), float(m[3])) for m in re.finditer(r"^(\w+) = \((-?[\d.]+), (-?[\d.]+)\)$", src, re.M) if m[1] in ("A", "C", "G", "E", "F", "Px")}
    r = float(re.search(r"c = Circle\(A, ([\d.]+)\)", src)[1])
    sub = lambda a, b: (a[0] - b[0], a[1] - b[1]); perp = lambda v: (-v[1], v[0]); unit = lambda v: (v[0] / math.hypot(*v), v[1] / math.hypot(*v)); dot = lambda a, b: a[0] * b[0] + a[1] * b[1]
    def meet(p, u, q, v):
        d = u[0] * v[1] - u[1] * v[0]; t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / d
        return (p[0] + u[0] * t, p[1] + u[1] * t)
    off = lambda p, q, u: abs((p[0] - q[0]) * u[1] - (p[1] - q[1]) * u[0]) / math.hypot(*u)
    A, C, G, E, F = P["A"], P["C"], P["G"], P["E"], P["F"]
    fd, gd = perp(sub(G, A)), perp(sub(E, A)); ax = unit(sub(A, C)); al = math.asin(r / math.dist(A, C))
    D = meet(G, sub(E, G), F, fd); ed = perp(fd)
    K = meet(F, sub(P["Px"], F), D, ed); Py = meet(P["Px"], perp(sub(P["Px"], F)), K, fd); H = meet(Py, ed, F, fd)
    w = sub(H, C); along = dot(w, ax); radial = math.hypot(math.hypot(w[0] - ax[0] * along, w[1] - ax[1] * along), math.dist(Py, H))
    return {"C_on_f": off(C, G, fd), "C_on_g": off(C, E, gd), "F_antipode_of_G": math.hypot(F[0] + G[0] - 2 * A[0], F[1] + G[1] - 2 * A[1]),
            "GE_perp_axis": abs(dot(unit(sub(E, G)), ax)), "half_angle_deg": math.degrees(al), "Py_on_cone": abs(math.atan2(radial, along) - al)}


def plane_geom(ctl=None):
    """(v2.3) BRIEF v2.3 §1 recomputed HERE from the frozen question's coordinates (SOURCE 10-14), apart from pack_data.py and figure.js. ctl = a planted fault (the calibration must catch it):
    'frozenV' = the parabola drawn from the question's rounded V (off j by 4.1e-5) · 'tilt' = the plane leaned by 1e-3 rad · 'shift' = one sample moved 1e-4 off the plane"""
    src = (REPO / "conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md").read_text(encoding="utf-8")
    P = {m[1]: (float(m[2]), float(m[3])) for m in re.finditer(r"^(\w+) = \((-?[\d.]+), (-?[\d.]+)\)$", src, re.M) if m[1] in ("A", "C", "G", "E", "F", "V", "Px")}
    r = float(re.search(r"c = Circle\(A, ([\d.]+)\)", src)[1])
    A, C, G, E, F, V, Px = (P[k] for k in ("A", "C", "G", "E", "F", "V", "Px"))
    # j = the line through F parallel to the tangent f at G (perpendicular to AG); g = the tangent at E; D = GE meets j; e = through D perpendicular to j (the directrix folded onto the board)
    jx, jy = -(G[1] - A[1]), G[0] - A[0]; n0 = math.hypot(jx, jy); ux, uy = -jx / n0, -jy / n0          # the unit along j from F towards V and D
    def line_meet(p, d1, q, d2):
        den = d1[0] * d2[1] - d1[1] * d2[0]; t = ((q[0] - p[0]) * d2[1] - (q[1] - p[1]) * d2[0]) / den
        return (p[0] + d1[0] * t, p[1] + d1[1] * t)
    gdir = (-(E[1] - A[1]), E[0] - A[0])
    D = line_meet(G, (E[0] - G[0], E[1] - G[1]), F, (ux, uy)); Vj = line_meet(F, (ux, uy), E, gdir)    # D = GE ∩ j · Vj = j ∩ g (the vertex drawn)
    K = line_meet(F, (Px[0] - F[0], Px[1] - F[1]), D, (-uy, ux)); Py = line_meet(Px, (-(Px[1] - F[1]), Px[0] - F[0]), K, (ux, uy)); H = line_meet(Py, (-uy, ux), F, (ux, uy))
    s_of = lambda q: (q[0] - F[0]) * ux + (q[1] - F[1]) * uy                                                   # position along j
    d_of = lambda q: abs((q[0] - F[0]) * uy - (q[1] - F[1]) * ux)                                              # distance from j = from the vertical plane through j
    p = s_of(Vj) - s_of(F); a_end = s_of(Vj) - s_of(H); top_h = math.dist(Py, H)                             # focal length |VF| · how far the parabola runs from V towards F (to H)
    samples = [((Vj[0] - ux * a, Vj[1] - uy * a), math.sqrt(max(0.0, 4 * p * a))) for a in (a_end * (i / 40) ** 2 for i in range(40))] + [(H, top_h)]
    if ctl == "frozenV": samples = [((q[0] + V[0] - Vj[0], q[1] + V[1] - Vj[1]), h) for q, h in samples]
    if ctl == "shift": samples[20] = ((samples[20][0][0] - uy * 1e-4, samples[20][0][1] + ux * 1e-4), samples[20][1])
    # the plane as two edges (along j on the board, and up); its normal by the cross product; the board's normal is (0, 0, 1)
    up = (0.0, 0.0, 1.0) if ctl != "tilt" else (-uy * 1e-3, ux * 1e-3, 1.0)
    along = (ux, uy, 0.0); nrm = (along[1] * up[2] - along[2] * up[1], along[2] * up[0] - along[0] * up[2], along[0] * up[1] - along[1] * up[0])
    ca = math.dist(A, C); half = math.asin(r / ca); axx, axy = (A[0] - C[0]) / ca, (A[1] - C[1]) / ca
    def cone_res(q, h):
        wx, wy = q[0] - C[0], q[1] - C[1]; t = wx * axx + wy * axy
        return abs(math.atan2(math.sqrt((wx - axx * t) ** 2 + (wy - axy * t) ** 2 + h * h), t) - half)
    return {"u_x": ux, "u_y": uy, "V_off_j": d_of(V), "D_off_j": d_of(D), "tV_over_tD": s_of(V) / s_of(D), "FV": math.dist(F, V), "FD": math.dist(F, D),
            "A_to_j": d_of(A), "AF_dot_j": abs(((F[0] - A[0]) * ux + (F[1] - A[1]) * uy) / math.dist(F, A)), "par_n": len(samples),
            "par_off_plane": max(d_of(q) for q, _ in samples), "par_on_cone": max(cone_res(q, h) for q, h in samples), "plane_dot_board": abs(nrm[2]) / math.sqrt(sum(x * x for x in nrm))}


SCOPE_F = REPO / "conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md"
TIERS = ["判定", "較正", "記述", "言えない"]


def scope_tiers(card):
    """rule (i), written here a second time: the tiers of §1 / §2 whose 根拠 cell (tables) or bullet (言えない) names the card as a whole token"""
    t = SCOPE_F.read_text(encoding="utf-8")
    body, tier, hit = t[t.index("## §1."):t.index("## §3.")], None, set()
    pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(card) + r"(?![0-9])")
    for line in body.splitlines():
        m = re.match(r"^### (判定|較正|記述|言えない)", line)
        if m:
            tier = m[1]; continue
        if line.startswith("## "):
            tier = None; continue
        cell = None
        if tier and line.startswith("|") and not line.startswith("|---") and not line.startswith("| 文 |"):
            cell = line.split("|")[2]
        elif tier == "言えない" and line.lstrip().startswith("- "):
            cell = line
        if cell is not None and pat.search(cell):
            hit.add(tier)
    return [x for x in TIERS if x in hit]


def grade_of(a):
    ts = scope_tiers(a["card"])
    if ts:
        return ts[0], "i"
    p = pathlib.Path(a["file"]); p = p if p.is_absolute() else REPO / p
    if a["literal"] not in p.read_text(encoding="utf-8"):
        return None, "ii: the RESULT line is not there"
    return a["grade_ii"], "ii"


def check(a):
    k = a["kind"]
    if k == "median_len":
        return statistics.median(len(r[a["field"]]) for r in select(a)) == a["expect"], statistics.median(len(r[a["field"]]) for r in select(a))
    if k == "median_high":
        v = statistics.median_high(dig(r, a["field"]) for r in select(a)); return v == a["expect"], v
    if k == "count_all":
        v = sum(all(r.get(f) for f in a["fields"]) for r in select(a)); return v == a["expect"], v
    if k == "grade_rule":
        g, rule = grade_of(a); return (g, rule) == (a["expect"], a["rule"]), (g, rule)
    if k == "grade_sum":
        tally = {"判定": 0, "記述": 0, "較正": 0, "言えない": 0, "関門": 0}
        for c in a["cards"]:
            g, _ = grade_of(c); tally[g] = tally.get(g, 0) + 1
        return tally == a["expect"] and sum(tally.values()) == 20, tally
    if k in ("count", "n", "route5", "median"):
        return recount(a) == a["expect"], recount(a)
    if k == "pack_cell":
        pack = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
        v = pack["cells"][a["cell"]][a["key"]]
        return v == recount(a), (v, recount(a))
    if k == "text_contains":
        p = pathlib.Path(a["file"]); p = p if p.is_absolute() else REPO / p
        if not p.is_file() and "/reads/" in a["file"]:   # bundle: a reader's reply (house record, not shipped) — the same check, made on it when the bundle was cut
            return [a["file"], a["literal"]] in json.loads((HERE / "data" / "reader_reply_facts.json").read_text(encoding="utf-8"))["contains"], None
        return a["literal"] in p.read_text(encoding="utf-8"), None
    if k == "md5":
        p = pathlib.Path(a["file"]); p = p if p.is_absolute() else REPO / p
        h = hashlib.md5(p.read_bytes()).hexdigest()
        return h.startswith(a["expect"]), h
    if k == "phrase":
        r = next(r for r in rows_of(a["file"]) if r.get("model") == a["model"] and r.get("arm") == a["arm"] and r.get("rep") == a["rep"] and r.get("raw"))
        return a["literal"] in r["raw"], None
    if k == "summary_sum":
        n, cut, ans, arms = summary_sum()
        return (n, cut, ans, arms) == (a["expect_n"], a["expect_cut"], a["expect_ans"], a["expect_arms"]), (n, cut, ans, arms)
    if k == "construct":
        e = construct_err()
        return e < a["tol"], e
    if k == "cone":
        v = cone_geom()[a["q"]]
        return abs(v - a["expect"]) <= a["tol"], v
    if k == "plane":
        v = plane_geom(a.get("ctl"))[a["q"]]
        return abs(v - a["expect"]) <= a["tol"], v
    if k == "json_key":
        o = json.loads((X / a["file"]).read_text(encoding="utf-8"))
        for key in a["path"]:
            o = o[key]
        ok = abs(o - a["expect"]) <= a["tol"] if "tol" in a else o == a["expect"]
        return ok, o
    if k == "cell_counts":
        rs = select(a)
        got = {"ans": sum(bool(r.get("cut_in_conjecture")) for r in rs), "bind": sum(bool(r.get("bind")) for r in rs), "floor": sum(bool(r.get("closure")) for r in rs), "n": len(rs)}
        return got == a["expect"], got
    raise ValueError("unknown kind " + k)


def calibrate(anchors):
    """the instrument is calibrated before use: for one anchor of every kind, a wrong expected value (or literal) must FAIL and the right one must PASS"""
    seen, bad = set(), []
    for a in anchors:
        if a["kind"] in seen:
            continue
        seen.add(a["kind"])
        ok, _ = check(a)
        w = dict(a)
        if "expect" in w and isinstance(w["expect"], (int, float)) and not isinstance(w["expect"], bool): w["expect"] = w["expect"] + 1
        elif "expect" in w and isinstance(w["expect"], dict) and "n" in w["expect"]: w["expect"] = dict(w["expect"], n=w["expect"]["n"] + 1)
        elif "expect" in w and isinstance(w["expect"], dict): w["expect"] = dict(w["expect"], 判定=w["expect"]["判定"] + 1)
        elif "expect" in w and w["kind"] == "grade_rule": w["expect"] = "関門" if w["expect"] != "関門" else "判定"
        elif "expect" in w: w["expect"] = "ffffffff"
        elif "literal" in w: w["literal"] = w["literal"] + " (not there)"
        elif "expect_n" in w: w["expect_n"] += 1
        elif "tol" in w: w["tol"] = 1e-9
        elif "cell" in w: w["key"] = "n" if w["key"] != "n" else "floor"
        try: wrong, _ = check(w)
        except Exception: wrong = False
        if not ok or wrong: bad.append((a["kind"], ok, wrong))
    print(f"calibration: {len(seen)} kinds · a wrong value fails and the right one passes in {len(seen) - len(bad)} / {len(seen)}")
    # (v2.3) the plane's instrument, every anchor of kind `plane`: a wrong value (expect + 1) fails and the right one passes; and three planted faults in the drawing must be caught
    #        (the parabola from the question's rounded V · one sample 1e-4 off the plane · the plane leaned by 1e-3 rad) while the true drawing passes the same anchor
    pa = [a for a in anchors if a["kind"] == "plane"]; pbad = []
    for a in pa:
        ok, _ = check(a); wrong, _ = check(dict(a, expect=a["expect"] + 1))
        if not ok or wrong: pbad.append(a["id"])
    planted = {"frozenV": "par_off_plane", "shift": "par_off_plane", "tilt": "plane_dot_board"}; caught = 0
    for ctl, q in planted.items():
        a = next(x for x in pa if x["q"] == q); ok, _ = check(a); hit, got = check(dict(a, ctl=ctl))
        caught += ok and not hit
        print(f"  plane control {ctl}: {q} = {got:.2e} (tol {a['tol']:g}) -> {'caught' if not hit else 'NOT CAUGHT'}")
    print(f"calibration (plane, v2.3): {len(pa) - len(pbad)} / {len(pa)} anchors (wrong value fails, right passes) · planted faults caught {caught} / {len(planted)}")
    return not bad and not pbad and caught == len(planted)


if __name__ == "__main__":
    anchors = json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8"))
    if "--calibrate" in sys.argv:
        sys.exit(0 if calibrate(anchors) else 1)
    count, missing = 0, []
    for a in anchors:
        count += 1
        try:
            ok, got = check(a)
        except Exception as e:
            ok, got = False, repr(e)
        if not ok:
            missing.append((a["id"], a["kind"], a.get("note", ""), a.get("expect"), got))
    ids = {a["id"] for a in anchors}
    claims = "\n".join(f.read_text(encoding="utf-8") for f in sorted(HERE.glob("CLAIMS*.md")))
    rows = set(re.findall(r"^\|\s*(K\d+)\s*\|", claims, re.M))
    for i in sorted(ids - rows):
        missing.append((i, "coverage", "an anchor without a claim row", None, "not in CLAIMS.md"))
    for i in sorted(rows - ids):
        missing.append((i, "coverage", "a claim row without an anchor", None, "no anchor"))
    print(f"anchors checked: {count} · claim rows: {len(rows)} · missing or different: {len(missing)}")
    for m in missing:
        print("  MISSING", m)
    sys.exit(1 if missing else 0)
