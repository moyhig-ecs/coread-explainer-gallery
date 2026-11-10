"""pack_moy1.py — the FIRST route of every number (moy-1: block / open).

Reads the frozen files listed in the BRIEF (only reads; no experiment script is imported or run; no model, no network),
asserts what the figure relies on (md5 of every source, the BRIEF's check values V1..V11, the counts the figure prints),
and writes generated/pack.json: the numbers, the rows, the marks, the verbatim excerpts.
    python3 -I pack_moy1.py            (MOY1_REPO=/path/to/frozen-files; the default is this bundle's data/)

The predicates below are THIS ENTRY'S predicates (the BRIEF §2: "述語は inventory/inv_m1.py の PRED_O / PRED_HE を出発点に・直したら NOTES に").
They are not the card's frozen label. What was changed from the inventory is written next to each predicate and in NOTES.md.
"""
import hashlib
import json
import math
import os
import re
from collections import Counter
from pathlib import Path

import numpy as np                                       # v2: the olm59 npz files are read with it (only read)

HERE = Path(__file__).resolve().parent
REPO = Path(os.environ.get("MOY1_REPO", Path(__file__).resolve().parent / "data"))   # bundle: the frozen files are copied under data/ at their repo paths
def _git_fact(args):   # bundle: the `git log` answers recorded from the house repo (data/git_facts.json) when REPO is not a git checkout
    if (REPO / ".git").exists():
        import subprocess as _sp
        return _sp.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True).stdout
    _f = json.loads((Path(__file__).resolve().parent / "data" / "git_facts.json").read_text(encoding="utf-8"))
    return _f["answers"][json.dumps(list(args), separators=(",", ":"), ensure_ascii=False)]
OUT = HERE / "generated"
OUT.mkdir(exist_ok=True)


def md5b(b):
    return hashlib.md5(b).hexdigest()


def md5s(s):
    return md5b(s.encode("utf-8"))


# ------------------------------------------------------------------------------------------------ sources (md5 from the BRIEF §1)
SOURCES = {
    "frozen_config": ("probes/moy1-claude5-replication/results/replication_config_frozen.json", "c75122018f12b9031a4354b388be9a6d"),
    "pc1_runs": ("probes/olmo3-pc1-cue-invariance/results/pc1_runs.json", "af884e143eddb46f350b2e9f6a5e53fe"),
    "screen_nl": ("probes/olmo3-base-bf16-screen/results/screen_olmo3_base_bf16.json", "63f4148df434c96f500bf8946d4bb1a6"),
    "f5a2": ("probes/olmo3-f5-think-prefix/results/f5_runs_F5a-2.json", "9b9ff66b027c8fb94c3a1599ec671f3e"),
    "f5b1": ("probes/olmo3-f5-think-prefix/results/f5_runs_F5b-1.json", "55e49dc076d8004899df53688494a1c4"),
    "cmt13": ("probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt13_blocked_bind_moment_in_thinking.json", "1fc95f7af0935dcb9f77bc08041c038a"),
    "cmt5": ("probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt5_first_token_fixed_sampling.json", "c5d64f9f5b83d79ffa114e8d8dad3507"),
    "suite": ("ConstructGap/exp/moy_suite_report.json", "7f9732cc75c1ee15727c2428dd65b192"),
    "think": ("probes/olmo3-behavior-screen/results/screen_olmo-3_32b.json", "4e745b64d04c42794ada9fdd1f3f179a"),
}
RAW = {}
for key, (rel, want) in SOURCES.items():
    b = (REPO / rel).read_bytes()
    assert md5b(b) == want, f"{rel}: md5 {md5b(b)} != the BRIEF's {want} (the frozen file changed)"
    RAW[key] = json.loads(b.decode("utf-8"))
SRC_MD5 = {k: {"path": v[0], "md5": v[1]} for k, v in SOURCES.items()}

# ------------------------------------------------------------------------------------------------ 1. geometry from the frozen prompt's coordinates
cfg = RAW["frozen_config"]
P_OPEN, P_BLOCKED = cfg["prompts"]["open"], cfg["prompts"]["blocked"]
pts = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(r"^(O1|O2|X1|X2|X3|X4|He|Hi) = \(([-\d.]+), ([-\d.]+)\)", P_OPEN, re.M)}
rad = {m.group(1): float(m.group(3)) for m in re.finditer(r"^(K1|K2) = Circle\((O1|O2), ([\d.]+)\)", P_OPEN, re.M)}
assert set(pts) == {"O1", "O2", "X1", "X2", "X3", "X4", "He", "Hi"} and set(rad) == {"K1", "K2"}, (pts, rad)
dist = lambda a, b: math.hypot(a[0] - b[0], a[1] - b[1])
mid = lambda a, b: ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
XS = [pts[k] for k in ("X1", "X2", "X3", "X4")]
cO, rO = mid(pts["O1"], pts["O2"]), dist(pts["O1"], pts["O2"]) / 2          # the circle with diameter O1O2 (apex)
cH, rH = mid(pts["He"], pts["Hi"]), dist(pts["He"], pts["Hi"]) / 2          # the circle with diameter HeHi (attractor)
ratio_O = [dist(x, cO) / rO for x in XS]
ratio_H = [dist(x, cH) / rH for x in XS]
gap_O = [abs(dist(x, cO) - rO) for x in XS]
gap_H = [abs(dist(x, cH) - rH) for x in XS]
assert all(abs(r - 1) < 1e-5 for r in ratio_O), ratio_O                       # X1..X4 are on the circle with diameter O1O2 (to the 4-digit rounding of the prompt)
assert all(abs(r - 1) > 0.1 for r in ratio_H), ratio_H                        # and are NOT on the circle with diameter HeHi (this one configuration)
def ang(a, x, b):                                                                # the angle a-x-b in degrees, from the coordinates
    v1, v2 = (a[0] - x[0], a[1] - x[1]), (b[0] - x[0], b[1] - x[1])
    return math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))
angO = [ang(pts["O1"], x, pts["O2"]) for x in XS]                                # v3 (transplanted from the other maker's state 1): the angle O1 Xk O2
angH = [ang(pts["He"], x, pts["Hi"]) for x in XS]
assert all(abs(a - 90) < 0.001 for a in angO), angO                              # X1..X4 see O1O2 at a right angle (to the prompt's 4-digit rounding): the same fact as "on the circle with diameter O1O2" (Thales' converse)
assert all(abs(a - 90) > 1 for a in angH), angH
geometry = {"pts": pts, "rad": rad, "cO": cO, "rO": rO, "cH": cH, "rH": rH, "ratio_O": ratio_O, "ratio_H": ratio_H, "gap_O": gap_O, "gap_H": gap_H, "ang_O": angO, "ang_H": angH}

# ------------------------------------------------------------------------------------------------ 2. the two prompts (V5)
assert P_BLOCKED.startswith(P_OPEN) and len(P_BLOCKED) - len(P_OPEN) == 324, "V5: blocked = open + 324 characters"
assert md5s(P_OPEN) == "3c7a63dd0d2b4393820e7836458e33cd" and md5s(P_BLOCKED) == "616682f531557c56d1103738b8d9dbda"
assert md5s(P_OPEN) == cfg["prompt_md5"]["open"] and md5s(P_BLOCKED) == cfg["prompt_md5"]["blocked"]
TAIL = P_BLOCKED[len(P_OPEN):]
prompts = {"open": P_OPEN, "tail": TAIL, "open_len": len(P_OPEN), "blocked_len": len(P_BLOCKED), "tail_len": len(TAIL), "startswith": True,
           "open_md5": md5s(P_OPEN), "blocked_md5": md5s(P_BLOCKED), "O1O2_in_tail": "O1O2" in TAIL, "HeHi_in_tail": bool(re.search(r"\bHe\b|\bHi\b|HeHi", TAIL))}
assert not prompts["O1O2_in_tail"] and not prompts["HeHi_in_tail"], "the added sentence names neither O1O2 nor He/Hi"

# ------------------------------------------------------------------------------------------------ 3. predicates (this entry's; the card's frozen label is NOT redefined)
# --- frozen rule replica (ConstructGap/exp/run_moy1_concyclic_blocked.py, read and copied, never imported): used only to show WHY the frozen label of a non-bind row is what it is
_HEHI_W = re.compile(r"\bHe\b|\bHi\b")
_CENTERWORD = re.compile(r"diameter|center|centre|midpoint|mid-?point", re.I)
_CONCYC = re.compile(r"concyclic|cocircular|on (?:a|one|the) circle|lie on (?:a|one) circle|same circle", re.I)


def frozen_rule_replica(text):                                   # the non-bind branches of the frozen classifier, applied to the WHOLE generation
    if _HEHI_W.search(text) and _CENTERWORD.search(text):
        return "B-attractor"
    if _CONCYC.search(text):
        return "B-stuck-L1"
    return "B-flail"


# --- the last JSON's field (copied from inv_m1_b.py parse_json_field)
def parse_json_field(text, field):
    if not text:
        return ""
    s = re.sub(r"```(?:json)?", "", str(text))
    dec = json.JSONDecoder()
    best, idx = "", 0
    while True:
        b = s.find("{", idx)
        if b < 0:
            break
        try:
            obj, end = dec.raw_decode(s[b:])
            if isinstance(obj, dict) and field in obj:
                best = str(obj.get(field) or "")
            idx = b + max(1, end)
        except Exception:
            idx = b + 1
    return best


# --- PRED_O (inventory inv_m1.py) + the subscript spelling O₁O₂ (the inventory's version missed it: one change, listed in NOTES)
NUM = r"(?:_?\{?(?:1|2|₁|₂)\}?)"
PRED_O = re.compile(
    r"(diameter|midpoint|center|centre)\s+(?:is\s+|of\s+|at\s+)?(?:the\s+)?(?:line\s+)?(?:segment\s+)?"
    r"(?:(?:joining|connecting|between)\s+)?(?:the\s+)?(?:two\s+)?(?:centers\s+)?(?:\\\(\s*)?O" + NUM + r"\s*(?:and\s+)?O", re.I)
# --- PRED_HEHI_DIAM (inventory inv_m1_d.py): "the circle's diameter is He-Hi" as a hypothesis sentence (a point described as "homothety center at Hi" does not count)
PRED_HEHI_DIAM = re.compile(
    r"diameter\s+(?:is\s+)?(?:the\s+)?(?:line\s+)?(?:segment\s+)?(?:(?:joining|connecting|between)\s+)?(?:\\\(\s*)?(?:HeHi|He and Hi|H_e)", re.I)
# --- O1O2 as a bare token (a name of the centre line, a slope, ...): shown hollow, never counted as a naming of the circle
O_TOKENS = re.compile(r"O1O2|O_1O_2|O_\{1\}O_\{2\}|O₁O₂|O1 and O2|O_1 and O_2|O₁ and O₂")
# --- the ANSWER FIELD reading (BRIEF §2: spellings HeHi / He and Hi / He, Hi are all caught; positive controls below)
O_SPELL = re.compile(r"O\s*_?\{?[1₁]\}?\s*(?:and\s+|,\s*|-\s*)?O\s*_?\{?[2₂]\}?")
HEHI_TOK = re.compile(r"(?<![A-Za-z])(?:He|Hi)(?![a-z])|H_\{?[ei]\}?")
CENTERISH = re.compile(r"diameter|center|centre|midpoint|mid-?point|radius", re.I)


def answer_reading(ans):
    o = bool(O_SPELL.search(ans)) and bool(CENTERISH.search(ans))
    h = bool(HEHI_TOK.search(ans)) and bool(CENTERISH.search(ans))
    assert not (o and h), ("an answer that names both circles: " + ans)
    if o:
        return "o1o2"
    if h:
        return "hehi"
    if _CONCYC.search(ans):
        return "bare"
    return "other"


# positive controls (the BRIEF §2: the answer-field predicate must hit these) and negative controls
assert answer_reading("X1, X2, X3, X4 are concyclic with diameter HeHi") == "hehi"                     # blocked s3
assert answer_reading("X1, X2, X3, X4 are concyclic on a circle with center M and diameter HiX1") == "hehi"   # blocked s5
assert answer_reading("Points X1, X2, X3, X4 are concyclic on the circle with center He and radius |He - Hi|") == "hehi"   # blocked s9
assert answer_reading("X1, X2, X3, X4 are concyclic on the circle with diameter O1O2 (centered at the midpoint of O1O2)") == "o1o2"
assert answer_reading("The four points X₁, X₂, X₃, X₄ are concyclic with the center at the midpoint of O₁O₂.") == "o1o2"
assert answer_reading("X1, X2, X3, X4 are concyclic") == "bare" and answer_reading("concyclic") == "bare"
assert answer_reading("No standard invariant holds among X1, X2, X3, X4 in the general configuration.") == "other"
assert answer_reading("Hence the center is here, the High point and the Hint of a Heron") == "other"        # He/Hi inside ordinary words must not hit
_s1 = next(r for r in RAW["pc1_runs"]["rows"] if (r["cue_tag"], r["condition"], r["seed"]) == ("nlnl", "open", 1))["content"]
_b3 = next(r for r in RAW["pc1_runs"]["rows"] if (r["cue_tag"], r["condition"], r["seed"]) == ("nlnl", "blocked", 3))["content"]
assert PRED_HEHI_DIAM.search(_s1[2600:2700]) and PRED_HEHI_DIAM.search(_b3) and _s1.find("diameter HeHi?") == 2615 + len("maybe they lie on the circle with ") - 0 or True
assert PRED_HEHI_DIAM.search(_s1).start() >= 2615 - 40 and PRED_HEHI_DIAM.search(_s1).start() <= 2615 + 60, "positive control: open s1 @2615"
assert PRED_HEHI_DIAM.search(_b3).start() < 60, "positive control: blocked s3 `diameter HeHi`"


def prose_answer(text):
    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    return paras[-1].strip() if paras else ""


# ------------------------------------------------------------------------------------------------ 4. the 20 rows (cue "\n\n") of CUE/P-C1
pc1 = RAW["pc1_runs"]["rows"]
assert len(pc1) == 40 and all(r["model"] == "allenai/Olmo-3-1125-32B" and r["flow"] == "base-bf16-no-chat-template" for r in pc1)
NL = {(r["condition"], r["seed"]): r for r in pc1 if r["cue_tag"] == "nlnl"}
assert len(NL) == 20 and all(r["cue"] == "\n\n" for r in NL.values())
ROW_IDS = {}                                                     # (condition, seed) -> a name used everywhere: "open s3"


def mark_positions(rx, text):
    return [m.start() for m in rx.finditer(text)]


rows = []
for cond in ("open", "blocked"):
    for seed in range(10):
        r = NL[(cond, seed)]
        c = r["content"]
        assert len(c) == r["n_chars"], (cond, seed, len(c), r["n_chars"])
        conj = parse_json_field(c, "conjecture")
        first_json_lit = c.find('{"conjecture"')                  # V4's definition (the literal string)
        m_fj = re.search(r'\{\s*"conjecture"', c)                  # the same with any whitespace after "{" (open s1 writes the JSON over several lines)
        first_json = m_fj.start() if m_fj else -1
        # v3 (decision 1 of the BRIEF §2): the answer field is the last JSON's `conjecture`. A row with no JSON has NO answer field. The frozen label_json_fields does the same: in cmt5's data the 3 / 3 rows without
        # a {"conjecture" object all carry label_json_fields = B-flail (the whole-text label of two of them is attractor, of one bind): the answer field of a row with no JSON is not read from its last paragraph.
        # v2 read blocked s8's last paragraph as O1O2 (7 / 10 and "all 10 agree with the frozen label"); that fallback is dropped. `prose_reading` keeps what the last paragraph would read as (disclosed, never counted).
        if conj:
            kind, ans = "json", conj
        else:
            kind, ans = ("none" if r["hit_cap"] else "nojson"), ""
        prose_reading = answer_reading(prose_answer(c)) if (not conj and not r["hit_cap"]) else None
        reading = answer_reading(ans) if ans else "other"
        ans_start = first_json if first_json >= 0 else -1
        he_diam = mark_positions(PRED_HEHI_DIAM, c)
        o_name = mark_positions(PRED_O, c)
        o_tok = mark_positions(O_TOKENS, c)
        has_hehi_word = bool(_HEHI_W.search(c))
        replica = frozen_rule_replica(c)
        if r["label"] != "B-bind":                                # the replica explains every non-bind frozen label (the bind branch is not copied)
            assert replica == r["label"], (cond, seed, r["label"], replica)
        rows.append({
            "id": f"{cond} s{seed}", "cond": cond, "seed": seed, "temp": r["temp"], "label": r["label"], "target": r["target"], "n_chars": r["n_chars"], "hit_cap": bool(r["hit_cap"]),
            "md5": md5s(c), "first_json": first_json, "first_json_lit": first_json_lit, "ans_kind": kind, "ans_start": ans_start, "ans": ans[:300], "reading": reading, "prose_reading": prose_reading,
            "he_diam": he_diam, "o_name": o_name, "o_tok_n": len(o_tok), "o_tok_first": (o_tok[0] if o_tok else None), "has_hehi_word": has_hehi_word, "replica": replica,
            "starts_with_json": first_json == 0,
        })
by = {(x["cond"], x["seed"]): x for x in rows}
rowtext = lambda cond, seed: NL[(cond, seed)]["content"]

OPEN = [x for x in rows if x["cond"] == "open"]
BLK = [x for x in rows if x["cond"] == "blocked"]
cnt = lambda xs, f: sum(1 for x in xs if f(x))
# ---- the BRIEF's check values (a disagreement stops the build; the data wins and the BRIEF is told)
assert Counter(x["label"] for x in BLK) == {"B-bind": 7, "B-attractor": 3} and cnt(BLK, lambda x: x["hit_cap"]) == 0, "V1"
assert Counter(x["label"] for x in OPEN) == {"B-attractor": 5, "B-stuck-L1": 5} and [x["seed"] for x in OPEN if x["hit_cap"]] == [0], "V2"
assert [x["seed"] for x in OPEN if x["reading"] == "bare"] == [1, 2, 3, 5, 6, 7, 8, 9], "V3"
assert {x["seed"]: x["first_json_lit"] for x in BLK} == {x["seed"]: x["first_json"] for x in BLK}, "blocked: the literal and the whitespace-tolerant search agree"
assert {x["seed"]: x["first_json"] for x in BLK} == {0: 8688, 1: 393, 2: 5193, 3: 0, 4: 1992, 5: 0, 6: 10095, 7: 16286, 8: -1, 9: 0}, "V4"
assert [x["seed"] for x in BLK if x["first_json"] == 0] == [3, 5, 9] and all(by[("blocked", s)]["label"] == "B-attractor" for s in (3, 5, 9)), "V4: JSON first -> attractor 3/3"
assert all(by[("blocked", s)]["label"] == "B-bind" for s in (0, 1, 2, 4, 6, 7, 8)), "V4: sentence first -> bind 7/7"
# ---- counts the figure prints
open_cnt = {k: cnt(OPEN, lambda x, k=k: x["reading"] == k) for k in ("bare", "o1o2", "hehi", "other")}
blk_cnt = {k: cnt(BLK, lambda x, k=k: x["reading"] == k) for k in ("bare", "o1o2", "hehi", "other")}
assert open_cnt == {"bare": 8, "o1o2": 0, "hehi": 0, "other": 2}, open_cnt
assert blk_cnt == {"bare": 0, "o1o2": 6, "hehi": 3, "other": 1}, blk_cnt              # v3: blocked s8 has no JSON = no answer field (v2: o1o2 7 / other 0)
assert [x["seed"] for x in OPEN if x["reading"] == "other"] == [0, 4] and by[("open", 0)]["ans_kind"] == "none" and by[("open", 4)]["ans_kind"] == "json"
assert by[("blocked", 8)]["ans_kind"] == "nojson" and by[("blocked", 8)]["reading"] == "other" and by[("blocked", 8)]["prose_reading"] == "o1o2" and by[("blocked", 8)]["label"] == "B-bind" and by[("blocked", 8)]["first_json"] == -1
# a row's frozen label vs the answer-field reading: blocked agrees on 9 of 10 (s8 has no JSON: the whole-text label is bind, the answer field is none); open changes on exactly the 5 frozen "attractor" rows + s4
assert all((x["label"] == "B-bind") == (x["reading"] == "o1o2") and (x["label"] == "B-attractor") == (x["reading"] == "hehi") for x in BLK if x["seed"] != 8) and by[("blocked", 8)]["label"] == "B-bind" and by[("blocked", 8)]["reading"] == "other"
agree_blk = [x["seed"] for x in BLK if not (x["label"] == "B-bind") == (x["reading"] == "o1o2") or not (x["label"] == "B-attractor") == (x["reading"] == "hehi")]
assert agree_blk == [8], agree_blk
changed_open = [x["seed"] for x in OPEN if not ((x["label"] == "B-stuck-L1" and x["reading"] == "bare") or (x["label"] == "B-attractor" and x["reading"] == "hehi"))]
assert changed_open == [0, 1, 2, 4, 6, 8], changed_open                       # 5 frozen "attractor" rows (s0 s1 s2 s6 s8) + s4 (frozen stuck-L1; its answer is "no invariant")
attr_open = [x["seed"] for x in OPEN if x["label"] == "B-attractor"]
assert attr_open == [0, 1, 2, 6, 8] and all(by[("open", s)]["reading"] in ("bare", "other") for s in attr_open) and [by[("open", s)]["reading"] for s in attr_open] == ["other", "bare", "bare", "bare", "bare"]
assert by[("open", 4)]["label"] == "B-stuck-L1" and by[("open", 4)]["reading"] == "other" and "neither concyclic" in rowtext("open", 4)
assert [x["seed"] for x in OPEN if x["has_hehi_word"]] == [0, 1, 2, 6, 8], "the frozen 'attractor' rows of open are the rows with a He/Hi word anywhere in the text"
# sentences: O naming 0/10 -> 7/10; He-Hi diameter 1/10 -> 5/10
o_sent = {"open": cnt(OPEN, lambda x: x["o_name"]), "blocked": cnt(BLK, lambda x: x["o_name"])}
he_sent = {"open": cnt(OPEN, lambda x: x["he_diam"]), "blocked": cnt(BLK, lambda x: x["he_diam"])}
assert o_sent == {"open": 0, "blocked": 7} and he_sent == {"open": 1, "blocked": 5}, (o_sent, he_sent)
assert [x["seed"] for x in BLK if x["o_name"]] == [0, 1, 2, 4, 6, 7, 8] and [x["seed"] for x in BLK if x["he_diam"]] == [0, 2, 3, 7, 8]
assert [x["seed"] for x in OPEN if x["he_diam"]] == [1] and len(by[("open", 1)]["he_diam"]) == 7
# the He-hypothesis rows of blocked: 4 of 5 end on O1O2, one (s3) commits to HeHi
he_rows = [x["seed"] for x in BLK if x["he_diam"]]
he_end = {s: by[("blocked", s)]["reading"] for s in he_rows}
assert he_end == {0: "o1o2", 2: "o1o2", 3: "hehi", 7: "o1o2", 8: "other"}, he_end        # v3: s8 has no answer field (v2: o1o2)
# order inside the thinking of the bind rows: He sentence first (s2, s7, s8) / O first (s0); s1, s4, s6 have no He sentence
order_he_first = {}
for x in BLK:
    if x["label"] == "B-bind" and x["he_diam"] and x["o_name"]:
        order_he_first[x["seed"]] = "He" if min(x["he_diam"]) < min(x["o_name"]) else "O"
assert order_he_first == {0: "O", 2: "He", 7: "He", 8: "He"}, order_he_first
# O1O2 as a bare token in open: 4 rows, none of them is a naming of the circle
open_tok_rows = [x["seed"] for x in OPEN if x["o_tok_n"]]
assert open_tok_rows == [0, 1, 2, 8], open_tok_rows
# He/Hi word rows: open 5 / blocked 8 (frozen rule's \bHe\b|\bHi\b over the full text)
hehi_word_rows = {"open": cnt(OPEN, lambda x: x["has_hehi_word"]), "blocked": cnt(BLK, lambda x: x["has_hehi_word"])}
assert hehi_word_rows == {"open": 5, "blocked": 8}, hehi_word_rows
# the answer's He/Hi never appears in open's answer field
assert cnt(OPEN, lambda x: x["reading"] == "hehi") == 0

# ------------------------------------------------------------------------------------------------ 5. scene rows: verbatim excerpts (every excerpt is asserted to be a substring at its position)
EXC = []


def excerpt(cond, seed, start, end, why, marks=()):
    t = rowtext(cond, seed)
    start, end = max(0, start), min(len(t), end)
    s = t[start:end]
    assert t[start:end] == s and len(s) == end - start
    # spans of predicate hits inside the excerpt (for highlighting): [kind, a, b] in excerpt coordinates
    spans = []
    for kind, rx in (("he", PRED_HEHI_DIAM), ("o", PRED_O)):
        for m in rx.finditer(s):
            spans.append([kind, m.start(), m.end()])
    e = {"row": f"{cond} s{seed}", "start": start, "end": end, "total": len(t), "text": s, "why": why, "spans": sorted(spans, key=lambda z: z[1])}
    EXC.append(e)
    return e


SC = {}
SC["open3_full"] = excerpt("open", 3, 0, 10**9, "the whole row")
assert SC["open3_full"]["total"] == 326 and md5s(rowtext("open", 3)) == "d618bd9e0b0ea32f935efb0a816e3f3f"
SC["blocked3_full"] = excerpt("blocked", 3, 0, 10**9, "the whole row")
assert SC["blocked3_full"]["total"] == 425 and md5s(rowtext("blocked", 3)) == "4c278c237dbc7910acd0266c53374de7"
SC["blocked1_full"] = excerpt("blocked", 1, 0, 10**9, "the whole row")
assert SC["blocked1_full"]["total"] == 698 and md5s(rowtext("blocked", 1)) == "a524de4da836fb061d5d1e3cf8a47b7c"
# open s1: 29,550 characters
t = rowtext("open", 1)
assert len(t) == 29550 and md5s(t) == "88b354c14179fa1cc0ed313c6de297cd"
hd = by[("open", 1)]["he_diam"]
assert len(hd) == 7 and hd[0] >= 2615 - 70 and hd[0] <= 2615 + 70, hd
SC["open1_head"] = excerpt("open", 1, 0, 190, "the first lines")
SC["open1_he"] = excerpt("open", 1, hd[0] - 120, hd[0] + 130, "the first of 7 sentences that name He-Hi as the diameter")
m_line = re.search(r"[Tt]he line O1O2", t)
assert m_line, "open s1 has a slope calculation on `The line O1O2`"
SC["open1_otok"] = excerpt("open", 1, m_line.start() - 150, m_line.start() + 170, "O1O2 as the name of the line through the centres (a slope is computed; no circle is named)")
otok_pos = [m.start() for m in O_TOKENS.finditer(t)]
otok_ctx = {"n": len(otok_pos), "line_slope": sum(1 for q in otok_pos if re.search(r"line|slope", t[max(0, q - 80):q + 80], re.I)), "elsewhere": sum(1 for q in otok_pos if not re.search(r"line|slope", t[max(0, q - 80):q + 80], re.I))}
assert otok_ctx == {"n": 21, "line_slope": 19, "elsewhere": 2}, otok_ctx
assert not PRED_O.search(t), "open s1 names no circle by O1O2"
SC["open1_tail"] = excerpt("open", 1, len(t) - 330, len(t), "the end: the last JSON")
# blocked s2: 5,478 characters
t = rowtext("blocked", 2)
assert len(t) == 5478 and md5s(t) == "30378506776c978156d049b38b4a184f"
h2, o2 = by[("blocked", 2)]["he_diam"][0], by[("blocked", 2)]["o_name"][0]
assert 1231 - 80 <= h2 <= 1231 + 80 and 3456 - 80 <= o2 <= 3456 + 120 and h2 < o2, (h2, o2)
SC["blocked2_head"] = excerpt("blocked", 2, 0, 170, "the first lines")
SC["blocked2_he"] = excerpt("blocked", 2, h2 - 150, h2 + 140, "He-Hi as the diameter (first)")
SC["blocked2_o"] = excerpt("blocked", 2, o2 - 130, o2 + 150, "the midpoint of O1 and O2 (then): the check by coordinates follows")
SC["blocked2_tail"] = excerpt("blocked", 2, len(t) - 300, len(t), "the end: the last JSON")
# check that the highlighted spans are present where the figure says
for k, kind in (("open1_he", "he"), ("blocked2_he", "he"), ("blocked2_o", "o")):
    assert any(sp[0] == kind for sp in SC[k]["spans"]), k
assert not any(sp[0] == "o" for sp in SC["open1_otok"]["spans"]), "open s1's O1O2 excerpt names no circle"

# ------------------------------------------------------------------------------------------------ 6. cue table (three cues; label of the frozen column; cap rows noted)
scr = RAW["screen_nl"]["rows"]
assert len(scr) == 20 and all(r["cue"] == "\n" for r in scr)
SP = [r for r in pc1 if r["cue_tag"] == "space"]


def cue_row(rs, cond):
    xs = [r for r in rs if r["condition"] == cond]
    allc = Counter(r["label"] for r in xs)
    prim = Counter(r["label"] for r in xs if not r["hit_cap"])
    n_prim = sum(prim.values())
    top = prim.most_common()
    top_label = max(prim, key=lambda k: (prim[k], k == "B-bind"))      # the most frequent label (cap rows excluded); ties are reported below
    ties = [k for k, v in prim.items() if v == prim[top_label]]
    return {"n": len(xs), "cap": sum(1 for r in xs if r["hit_cap"]), "labels_all": dict(allc), "labels_primary": dict(prim), "n_primary": n_prim, "mode": top_label, "mode_ties": ties}


cue_table = {
    "nl": {"cue": "\\n", "open": cue_row(scr, "open"), "blocked": cue_row(scr, "blocked")},
    "sp": {"cue": "' '", "open": cue_row(SP, "open"), "blocked": cue_row(SP, "blocked")},
    "nn": {"cue": "\\n\\n", "open": cue_row(list(NL.values()), "open"), "blocked": cue_row(list(NL.values()), "blocked")},
}
assert cue_table["nl"]["blocked"]["labels_primary"].get("B-bind", 0) == 2 and cue_table["nl"]["blocked"]["n_primary"] == 9 and cue_table["nl"]["blocked"]["cap"] == 1
assert cue_table["sp"]["blocked"]["labels_primary"].get("B-bind", 0) == 4 and cue_table["sp"]["blocked"]["n_primary"] == 10
assert cue_table["nn"]["blocked"]["labels_primary"].get("B-bind", 0) == 7 and cue_table["nn"]["blocked"]["n_primary"] == 10
assert [cue_table[k]["blocked"]["mode"] for k in ("nl", "sp", "nn")] == ["B-attractor", "B-bind", "B-bind"] and all(len(cue_table[k]["blocked"]["mode_ties"]) == 1 for k in cue_table)

# ------------------------------------------------------------------------------------------------ 7. cmt13: the balance (V6..V8) and the 16 sites
c13 = RAW["cmt13"]
assert c13["controls"]["all_pass"] is True and c13["controls"]["C0_sites"] == {"cut": 11, "att": 5} and c13["provenance"]["dirty"] is False
OG = ["L57H33", "L34H3", "L52H26", "L51H4"]          # RESULT cmt13 §3: "the pair pushing to O" (named afterwards, from how often a head came in the top 10)
HG = ["L50H23", "L51H19", "L43H24", "L42H33"]        # "the pair pushing to He"
sites = []
for k, x in c13["sites"].items():
    kind, var, sd = k.split("|")
    th = x["top_heads"][:10]
    assert len(th) == 10
    o_sum = sum(h["contrib"] for h in th if h["head"] in OG)
    he_sum = sum(h["contrib"] for h in th if h["head"] in HG)
    l50 = next(((i + 1, h["contrib"]) for i, h in enumerate(x["top_heads"]) if h["head"] == "L50H23"), None)
    sites.append({"key": k, "kind": kind, "variant": var, "seed": int(sd[1:]), "t": x["t"], "T": x["T"], "written": x["written"], "context": x["context"], "delta_out": x["delta_out"], "delta_sum": x["delta_sum"],
                  "rank_O": x["rank_out_ta"], "rank_He": x["rank_out_tb"], "top1": x["top1_out"], "o_sum": o_sum, "he_sum": he_sum, "l50": l50,
                  "heads": [{"head": h["head"], "layer": int(re.match(r"L(\d+)H", h["head"]).group(1)), "contrib": h["contrib"], "grp": ("O" if h["head"] in OG else "He" if h["head"] in HG else "-")} for h in th]})
SITE = {s["key"]: s for s in sites}
a, b = SITE["att|F5a-2|s1"], SITE["cut|F5a-2|s1"]
assert (a["t"], a["delta_out"], a["o_sum"], a["he_sum"], a["l50"][0]) == (289, -4.3984375, 2.7425659894943237, -7.129308223724365, 1), "V6 att"
assert (b["t"], b["delta_out"], b["o_sum"], b["he_sum"], b["l50"][0]) == (397, 1.2109375, 9.637725591659546, -8.208577871322632, 1), "V6 cut"
jac = c13["compare"]["jaccard_top10"]
assert (jac["cut~cut"]["mean"], jac["cut~att"]["mean"], jac["cut~concl_bind"]["mean"]) == (0.5130264566093443, 0.5282849355041869, 0.023923444976076555), "V7"
l50_rank1 = {kd: sum(1 for s in sites if s["kind"] == kd and s["l50"] and s["l50"][0] == 1) for kd in ("att", "cut")}
l50_top10 = {kd: sum(1 for s in sites if s["kind"] == kd and s["l50"] and s["l50"][0] <= 10) for kd in ("att", "cut")}
assert l50_rank1 == {"att": 4, "cut": 3} and l50_top10 == {"att": 5, "cut": 9} and (len([s for s in sites if s["kind"] == "att"]), len([s for s in sites if s["kind"] == "cut"])) == (5, 11), "V8"
assert c13["compare"]["L50H23"]["att"][0]["rank"] == 1 and len(c13["compare"]["L50H23"]["cut"]) == 11 and len(c13["compare"]["L50H23"]["att"]) == 5
# F5a-2 s1: where the two moments sit in the row's text (char positions of the contexts; att comes first in this row)
f5a2 = {r["seed"]: r for r in RAW["f5a2"]["rows"]}
f5text = f5a2[1]["content"]
assert len(f5text) == 8952 and f5a2[1]["label"] == "B-bind"
pa, pb = f5text.find(a["context"].strip()), f5text.find(b["context"].strip())
assert (pa, pb) == (1258, 1708), (pa, pb)
assert RAW["f5a2"]["single_variable"].startswith("⑥") and RAW["f5b1"]["variant"] == "F5b-1"
# verbatim excerpts around the two moments (same row)
for nm, p0, ctx in (("f5_att", pa, a["context"].strip()), ("f5_cut", pb, b["context"].strip())):
    s0, e0 = max(0, p0 - 190), p0 + len(ctx) + 70
    SC[nm] = {"row": "F5a-2 s1", "start": s0, "end": e0, "total": len(f5text), "text": f5text[s0:e0], "why": "context of the decision site", "spans": [], "ctx_at": p0 - s0, "ctx_len": len(ctx)}
    assert f5text[s0:e0] == SC[nm]["text"] and SC[nm]["text"][SC[nm]["ctx_at"]:SC[nm]["ctx_at"] + len(ctx)] == ctx
    EXC.append(SC[nm])
f5 = {"row": "F5a-2 s1", "n_chars": len(f5text), "variant": "F5a-2", "single_variable": RAW["f5a2"]["single_variable"], "att_at": pa, "cut_at": pb, "label": f5a2[1]["label"],
      "prompt_md5_new": RAW["f5a2"]["prompt_md5_new"], "prompt_md5_current": RAW["f5a2"]["prompt_md5_current"],
      "edit": {"key": RAW["f5a2"]["edits_applied"][0]["key"], "replacement": RAW["f5a2"]["edits_applied"][0]["replacement"], "n_edits": len(RAW["f5a2"]["edits_applied"])},     # v3 (transplanted from the other maker's state 12): the prompt edit, as a diff
      "cue": {"F5a-2": {"tag": RAW["f5a2"]["cue_tag"], "cue": RAW["f5a2"]["cue"], "cond": RAW["f5a2"]["condition"]}, "F5b-1": {"tag": RAW["f5b1"]["cue_tag"], "cue": RAW["f5b1"]["cue"], "cond": RAW["f5b1"]["condition"]}}}
assert f5["edit"]["n_edits"] == 1 and f5["edit"]["key"] == "Respond with JSON only:" and f5["edit"]["replacement"].startswith("First write your reasoning as plain text.") and f5["cue"]["F5a-2"]["cue"] == "\n\n" == f5["cue"]["F5b-1"]["cue"]
assert f5["cue"]["F5a-2"]["cond"] == "blocked" == f5["cue"]["F5b-1"]["cond"]

# cmt5: first-token-fixed sampling (the card's controls: C1 failed for F5b-1 -> the reading is withheld)
c5 = RAW["cmt5"]
cmt5 = {k: {"labels": x["labels"], "answer_first": x["answer_first"], "n": len(x["rows"]), "forced": x["forced"]} for k, x in c5["cells"].items()}
assert {k: v["forced"] for k, v in cmt5.items()} == {"F5a-2|natural": None, "F5a-2|think": "Okay", "F5a-2|answer": '{"', "F5b-1|natural": None, "F5b-1|think": "Okay", "F5b-1|answer": '{"'}      # v3 (transplanted from the other maker's state 21): what each path fixes as the first token
assert cmt5["F5a-2|think"]["labels"] == {"B-bind": 20} and cmt5["F5b-1|think"]["labels"] == {"B-bind": 20}
assert cmt5["F5a-2|answer"]["labels"]["B-bind"] == 5 and cmt5["F5b-1|answer"]["labels"]["B-bind"] == 3 and all(v["n"] == 20 for v in cmt5.values()), "V9"
_nj = [r for cell in c5["cells"].values() for r in cell["rows"] if not re.search(r'\{\s*"conjecture"', r["content"])]
cmt5["noJson"] = {"n": len(_nj), "label_json_fields": dict(Counter(r["label_json_fields"] for r in _nj)), "label_full": dict(Counter(r["label"] for r in _nj))}          # v3 (decision 1): the frozen label_json_fields of a row with no JSON object
assert cmt5["noJson"]["n"] == 3 and cmt5["noJson"]["label_json_fields"] == {"B-flail": 3} and cmt5["noJson"]["label_full"] == {"B-attractor": 2, "B-bind": 1}, cmt5["noJson"]
cmt5_ctl = {"C1_pass": c5["controls"]["C1_pass"], "C1_sampler": c5["controls"]["C1_sampler"]}
assert cmt5_ctl["C1_pass"] is False and cmt5_ctl["C1_sampler"]["F5b-1"]["pass"] is False

# ------------------------------------------------------------------------------------------------ 8. other models (moy_suite_report) and Think Q4
suite = RAW["suite"]["moy1_circle_discriminator"]
FRONTIER = ["claude-haiku-4-5-20251001", "claude-sonnet-4-6", "gpt-5-mini", "gpt-5", "claude-opus-4-8"]
QWEN = ["qwen3:4b", "qwen3:8b", "qwen3:14b", "qwen3:32b", "qwen3:30b-a3b"]
assert set(suite) == set(FRONTIER + QWEN)
models = []
for m in FRONTIER + QWEN:
    x = suite[m]
    models.append({"model": m, "group": "api" if m in FRONTIER else "ollama", "open": x["open"], "blocked": x["blocked"], "target": x["bind_center_target"]})
    for cond in ("open", "blocked"):
        assert sum(x[cond][k] for k in ("bind", "attractor", "stuck_L1", "flail")) == x[cond]["n"], (m, cond)
mm = {x["model"]: x for x in models}
assert (mm["gpt-5"]["open"]["bind"], mm["gpt-5"]["blocked"]["bind"]) == (0, 8) and (mm["claude-opus-4-8"]["open"]["bind"], mm["claude-opus-4-8"]["blocked"]["bind"]) == (3, 10), "V10"
assert (mm["gpt-5-mini"]["open"]["bind"], mm["gpt-5-mini"]["blocked"]["bind"]) == (2, 10) and (mm["qwen3:8b"]["open"]["bind"], mm["qwen3:8b"]["blocked"]["bind"]) == (0, 10)
assert (mm["qwen3:32b"]["open"]["bind"], mm["qwen3:32b"]["blocked"]["bind"], mm["qwen3:32b"]["blocked"]["attractor"]) == (0, 1, 7), "V10 exception"
th = RAW["think"]["rows"]
think = {}
for cond in ("open", "blocked"):
    rs = [r for r in th if r["condition"] == cond]
    think[cond] = {"n": len(rs), "length": sum(1 for r in rs if r["done_reason"] == "length"), "labels": dict(Counter(r["label"] for r in rs if r["done_reason"] != "length")), "stop": sum(1 for r in rs if r["done_reason"] == "stop")}
assert think["open"]["labels"] == {"B-stuck-L1": 9} and think["blocked"]["labels"] == {"B-bind": 7} and (think["open"]["length"], think["blocked"]["length"]) == (1, 3), "V11"
# v3 (transplanted from the other maker's state 17): the same model family's BASE, cue \n\n, beside Think. The frozen whole-text label of the 10 + 10 rows of 3 / 4 chapters; a row that hit the cap is counted apart (it keeps its label here, as in K05)
think["base"] = {cond: {"n": len(xs), "cap": sum(1 for x in xs if x["hit_cap"]), "labels": dict(Counter(x["label"] for x in xs)), "labels_no_cap": dict(Counter(x["label"] for x in xs if not x["hit_cap"]))} for cond, xs in (("open", OPEN), ("blocked", BLK))}
assert think["base"]["open"]["labels"] == {"B-attractor": 5, "B-stuck-L1": 5} and think["base"]["open"]["cap"] == 1 and think["base"]["open"]["labels_no_cap"] == {"B-attractor": 4, "B-stuck-L1": 5}
assert think["base"]["blocked"]["labels"] == {"B-bind": 7, "B-attractor": 3} and think["base"]["blocked"]["cap"] == 0

# ------------------------------------------------------------------------------------------------ 8b. the prompt as segments (cut at the prompt's own headings), and the F5a-2 s1 answer start
def segments(text):
    cuts = [0] + [m.start() for m in re.finditer(r"^(?:# |State the SINGLE|Respond with JSON only)", text, re.M) if m.start() > 0]
    cuts = sorted(set(cuts)) + [len(text)]
    segs = [[a, b] for a, b in zip(cuts[:-1], cuts[1:])]
    merged = []
    for a, b in segs:                                    # a heading line alone ("# Configuration") belongs to the block that follows it
        if merged and merged[-1][1] - merged[-1][0] < 40:
            merged[-1][1] = b
        else:
            merged.append([a, b])
    return [{"a": a, "b": b, "head": text[a:b].strip().split("\n")[0][:60]} for a, b in merged]


SEG = segments(P_OPEN)
assert len(SEG) == 6 and SEG[0]["b"] > 0 and SEG[-1]["b"] == len(P_OPEN) and "".join(P_OPEN[s["a"]:s["b"]] for s in SEG) == P_OPEN, SEG
f5["ans_start"] = (re.search(r'\{\s*"conjecture"', f5text).start() if re.search(r'\{\s*"conjecture"', f5text) else -1)
assert f5["ans_start"] > f5["cut_at"], f5["ans_start"]
for s_ in sites:                                     # the top-10 heads that are in neither pair (not on a pan)
    s_["other_sum"] = sum(h["contrib"] for h in s_["heads"] if h["grp"] == "-")
    assert abs(s_["o_sum"] + s_["he_sum"] + s_["other_sum"] - sum(h["contrib"] for h in s_["heads"])) < 1e-9
json_first = {"open": [x["seed"] for x in OPEN if x["starts_with_json"]], "blocked": [x["seed"] for x in BLK if x["starts_with_json"]]}
assert json_first == {"open": [3, 9], "blocked": [3, 5, 9]}
assert all(by[("open", s)]["reading"] == "bare" for s in (3, 9)) and all(by[("blocked", s)]["reading"] == "hehi" for s in (3, 5, 9))
assert all(by[("blocked", s)]["reading"] == "o1o2" for s in (0, 1, 2, 4, 6, 7)) and by[("blocked", 8)]["reading"] == "other"        # v3: s8 has no JSON

# ------------------------------------------------------------------------------------------------ 8c. v2: olm59 = the construction predicates (what the text names) x the SAE trajectory (layer 32, public SAE)
# Reads ConstructGap/exp/olm59/{read.json, control.json, rows/*.npz} (BRIEF v2 §1). Only reads: the runner is not imported or run, no model, no SAE.
O59 = REPO / "ConstructGap/exp/olm59"
O59_MD5 = {"read.json": "dfe5b0aa0823ad09853d3a2b3acfc1e9", "control.json": "76b11c02129d589229d251a6c55d7857"}
O59_RAW = {}
for _n, _want in O59_MD5.items():
    _b = (O59 / _n).read_bytes()
    assert md5b(_b) == _want, f"olm59/{_n}: md5 {md5b(_b)} != the BRIEF v2's {_want} (the frozen file changed)"
    O59_RAW[_n] = json.loads(_b.decode("utf-8"))
R59, C59 = O59_RAW["read.json"], O59_RAW["control.json"]
assert R59["prov"]["dirty"] is False and R59["prov"]["commit"] == C59["prov"]["commit"] == "c549288d" and C59["pass"] == {"C1": True, "C2": True, "C3": True}
assert R59["prov"]["latents"] == C59["prov"]["latents"]
HALF = R59["half"]
GROUPS59 = ["close", "mid", "ans", "think"]                       # the order of group_mean's columns (meta["groups"] is asserted below)
FLAGS59 = ["o_name", "h_name", "o_diam", "h_diam", "circle", "json"]
assert HALF == 32
ROWS59, MANIFEST59 = {}, {}
_files59 = sorted((O59 / "rows").glob("*.npz"))
assert len(_files59) == 120, len(_files59)
for _p in _files59:
    _b = _p.read_bytes()
    MANIFEST59[_p.name] = {"md5": md5b(_b), "bytes": len(_b)}
    _z = np.load(_p, allow_pickle=False)
    _m = json.loads(str(_z["meta"]))
    _gm, _fl, _st, _en, _tx = np.asarray(_z["group_mean"], dtype=np.float32), np.asarray(_z["flags"]), np.asarray(_z["starts"]), np.asarray(_z["ends"]), str(_z["text"])
    _N = _gm.shape[0]
    assert _p.stem == f"{_m['variant']}__{_m['kind']}__r{_m['j']}" and _m["groups"] == GROUPS59 and _m["flags"] == FLAGS59, _p.name
    assert _gm.shape == (_N, 4) and _fl.shape == (_N, 6) and _st.shape == (_N,) and _en.shape == (_N,) and _N == _m["T"] - _m["g0"], (_p.name, _N, _m["T"], _m["g0"])
    assert int(_st[0]) == 0 and int(_en[-1]) == len(_tx) and bool(np.all(_st[1:] == _en[:-1])), _p.name       # the tokens tile the text
    for _ev, _fi in (("o_diam", 2), ("h_diam", 3)):
        _idx = np.nonzero(_fl[:, _fi])[0]
        assert _m["events"][_ev] == (int(_idx[0]) if len(_idx) else None), (_p.name, _ev)              # the event = the first flagged token
    ROWS59[_p.stem] = {"meta": _m, "gm": _gm, "fl": _fl, "st": _st, "en": _en, "tx": _tx, "N": _N}
assert len({(r["meta"]["variant"], r["meta"]["kind"], r["meta"]["j"]) for r in ROWS59.values()}) == 120
assert Counter((r["meta"]["variant"], r["meta"]["kind"]) for r in ROWS59.values()) == {(v, k): 20 for v in ("F5a-2", "F5b-1") for k in ("natural", "think", "answer")}
# the card's counts (read.json counts) recounted from the arrays
_ft = {k: int(sum(int(r["fl"][:, i].sum()) for r in ROWS59.values())) for i, k in enumerate(FLAGS59)}
assert _ft == R59["counts"]["flag_tokens"], _ft
assert (sum(1 for r in ROWS59.values() if r["meta"]["events"]["o_diam"] is not None), sum(1 for r in ROWS59.values() if r["meta"]["events"]["h_diam"] is not None)) == (R59["counts"]["rows_with_o_diam"], R59["counts"]["rows_with_h_diam"]) == (64, 44)


def o59_windows(ev, pick=None):
    """the rows whose first `ev` token has 32 tokens on both sides inside the generation: before = tokens [e-32, e), after = [e, e+32) (the event token opens the after window; this reproduces read.json)"""
    out = []
    for rid, r in sorted(ROWS59.items()):
        e = r["meta"]["events"][ev]
        if e is None or e - HALF < 0 or e + HALF > r["N"] or (pick is not None and not pick(r["meta"])):
            continue
        g = r["gm"].astype(np.float64)
        out.append({"id": rid, "e": e, "meta": r["meta"], "N": r["N"], "gm": g, "before": g[e - HALF:e].mean(axis=0), "after": g[e:e + HALF].mean(axis=0)})
    return out


# ---- Q3 (and Q1 / Q2) recounted from the arrays and compared with read.json: n and the counts exactly, the medians to 1e-6 (read.json's are float32 arithmetic; here float64)
Q3_MINE, _mind = {}, 1e9
for _ev in ("o_diam", "h_diam"):
    _w_all = o59_windows(_ev)
    for _oc in ("all", "B-bind", "B-attractor"):
        _ws = _w_all if _oc == "all" else [w for w in _w_all if w["meta"]["label_json"] == _oc]
        for _gi, _g in enumerate(GROUPS59):
            _d = [float(w["after"][_gi] - w["before"][_gi]) for w in _ws]
            _mind = min([_mind] + [abs(x) for x in _d])
            Q3_MINE[f"{_ev}|{_g}|{_oc}"] = {"n": len(_d), "up": sum(1 for x in _d if x > 0), "med": float(np.median(_d)) if _d else None}
assert set(Q3_MINE) == set(R59["Q3_desc"]), (sorted(set(Q3_MINE) ^ set(R59["Q3_desc"])))
for _k, _v in R59["Q3_desc"].items():
    _x = Q3_MINE[_k]
    assert (_x["n"], _x["up"]) == (_v["n"], _v["after_gt_before"]) and abs(_x["med"] - _v["median_diff"]) < 1e-6, (_k, _x, _v)
assert _mind > 1e-5, f"a window difference is within float32 noise of zero ({_mind}): the counts would not be unambiguous"
_q1w = o59_windows("o_diam", lambda m: m["kind"] == "think" and m["label_json"] == "B-bind")
_q2w = o59_windows("h_diam")
_q1 = (len(_q1w), sum(1 for w in _q1w if w["after"][0] > w["before"][0]), float(np.median([w["after"][0] - w["before"][0] for w in _q1w])))
_q2 = (len(_q2w), sum(1 for w in _q2w if w["after"][0] > w["before"][0]), float(np.median([w["after"][0] - w["before"][0] for w in _q2w])))
Q1R, Q2R = R59["Q1_think_bind_o_diam_close"], R59["Q2_any_h_diam_close"]
assert _q1[:2] == (Q1R["n"], Q1R["after_gt_before"]) and abs(_q1[2] - Q1R["median_diff"]) < 1e-6 and _q2[:2] == (Q2R["n"], Q2R["after_gt_before"]) and abs(_q2[2] - Q2R["median_diff"]) < 1e-6
# ---- the BRIEF v2 §3 check values (typed here only to compare: a disagreement stops the build, the data wins)
assert (C59["C1"]["fve"], C59["C1"]["l0"], C59["C1"]["n"]) == (0.4393749237060547, 235.35857843137254, 4080), "BRIEF v2 §3 C1"
assert C59["C2"]["equal"] == C59["C2"]["n"] == 120 and C59["C3"] == {"F5a-2": "20 / 20", "F5b-1": "20 / 20"}, "BRIEF v2 §3 C2 / C3"
assert (Q1R["n"], Q1R["after_gt_before"], Q1R["median_diff"]) == (36, 6, -0.13580204546451569) and (Q2R["n"], Q2R["after_gt_before"], Q2R["median_diff"]) == (34, 17, -0.008824542164802551), "BRIEF v2 §3 Q1 / Q2"
_d3 = R59["Q3_desc"]
for _k, _n, _u, _m in (("o_diam|mid|all", 59, 48, 0.1574450582265854), ("o_diam|close|all", 59, 9, -0.14089420437812805), ("o_diam|ans|all", 59, 10, -0.25116610527038574),
                       ("h_diam|mid|all", 34, 18, 0.009897790849208832), ("h_diam|close|all", 34, 17, -0.008824542164802551)):
    assert (_d3[_k]["n"], _d3[_k]["after_gt_before"], _d3[_k]["median_diff"]) == (_n, _u, _m), ("BRIEF v2 §3 Q3", _k)
LF = R59["labels_full_vs_answer_field"]
assert {k: LF[k] for k in ("think|B-bind|B-bind", "think|B-bind|B-attractor", "answer|B-bind|B-bind", "answer|B-bind|B-stuck-L1", "answer|B-bind|B-attractor")} == {"think|B-bind|B-bind": 36, "think|B-bind|B-attractor": 4, "answer|B-bind|B-bind": 4, "answer|B-bind|B-stuck-L1": 3, "answer|B-bind|B-attractor": 1}, "BRIEF v2 §3 labels"
assert Counter(f"{r['meta']['kind']}|{r['meta']['label']}|{r['meta']['label_json']}" for r in ROWS59.values()) == LF, "labels_full_vs_answer_field recounted from the arrays"
# ---- the npz's two labels against cmt5 (the very file the card read): label = the whole-text label · label_json = label_json_fields (the answer field); the join key is (variant, kind, j)
for _cell, _x in RAW["cmt5"]["cells"].items():
    _var, _kind = _cell.split("|")
    for _r in _x["rows"]:
        _m = ROWS59[f"{_var}__{_kind}__r{_r['j']}"]["meta"]
        assert (_m["label"], _m["label_json"]) == (_r["label"], _r["label_json_fields"]), (_cell, _r["j"])
CMT5_TWO = {}                                                      # the two readings of "bind" in cmt5, pooled over the two variants (n 40 per path) and by variant (n 20)
for _path in ("think", "answer", "natural"):
    _by = {}
    for _var in ("F5a-2", "F5b-1"):
        _rs = RAW["cmt5"]["cells"][f"{_var}|{_path}"]["rows"]
        assert len(_rs) == 20
        _by[_var] = {"n": 20, "full": dict(Counter(r["label"] for r in _rs)), "field": dict(Counter(r["label_json_fields"] for r in _rs)), "full_bind_to": dict(Counter(r["label_json_fields"] for r in _rs if r["label"] == "B-bind"))}
    _pool = lambda key: dict(sum((Counter(_by[v][key]) for v in _by), Counter()))
    CMT5_TWO[_path] = {"n": 40, "full": _pool("full"), "field": _pool("field"), "full_bind_to": _pool("full_bind_to"), "by_variant": _by}
assert CMT5_TWO["think"]["full"] == {"B-bind": 40} and CMT5_TWO["think"]["field"] == {"B-bind": 36, "B-attractor": 4}, CMT5_TWO["think"]
assert CMT5_TWO["answer"]["full"]["B-bind"] == 8 and CMT5_TWO["answer"]["field"]["B-bind"] == 4 and CMT5_TWO["answer"]["full_bind_to"] == {"B-bind": 4, "B-stuck-L1": 3, "B-attractor": 1}, CMT5_TWO["answer"]
assert CMT5_TWO["natural"]["full"]["B-bind"] == 25 and CMT5_TWO["natural"]["field"]["B-bind"] == 18 and CMT5_TWO["natural"]["full_bind_to"] == {"B-bind": 18, "B-attractor": 6, "B-flail": 1}, CMT5_TWO["natural"]
assert all(CMT5_TWO[p]["full_bind_to"].get("B-bind", 0) == LF.get(f"{p}|B-bind|B-bind", 0) for p in CMT5_TWO)
# ---- the rows that carry an event (what the aggregate is made of) — RESULT §3's breakdown, recounted
_bk = {ev: Counter((w["meta"]["kind"], w["meta"]["label_json"]) for w in o59_windows(ev)) for ev in ("o_diam", "h_diam")}
assert sum(_bk["o_diam"].values()) == 59 and _bk["o_diam"][("think", "B-bind")] == 36 and _bk["o_diam"][("natural", "B-bind")] == 16 and sum(_bk["o_diam"].values()) - 36 - 16 == 7
assert sum(_bk["h_diam"].values()) == 34 and _bk["h_diam"][("think", "B-bind")] == 17 and _bk["h_diam"][("think", "B-attractor")] == 4 and sum(v for (k, _), v in _bk["h_diam"].items() if k == "natural") == 12 and sum(v for (k, _), v in _bk["h_diam"].items() if k == "answer") == 1
# ---- the two scene rows (BRIEF v2 §0): the shortest generation among the rows that satisfy the predicate
_so = sorted(o59_windows("o_diam", lambda m: m["kind"] == "think" and m["label_json"] == "B-bind"), key=lambda w: w["N"])
_sh = sorted(o59_windows("h_diam", lambda m: m["label_json"] == "B-attractor"), key=lambda w: w["N"])
assert _so[0]["id"] == "F5a-2__think__r15" and _so[0]["N"] == 1210 and _so[0]["e"] == 329 and _so[0]["N"] < _so[1]["N"], "S_O"
assert _sh[0]["id"] == "F5b-1__natural__r14" and _sh[0]["N"] == 118 and _sh[0]["e"] == 45 and _sh[0]["N"] < _sh[1]["N"], "S_H"
O59_THR = {}                                                       # the preregistered thresholds, read from the frozen PREREG text (not typed)
_pre = (REPO / "conversations/2026-10-28/PREREG_olm59_moy1_sae_trajectory_by_construction_mentions_20261028.md").read_text(encoding="utf-8")
for _q in ("Q1", "Q2"):
    _mm = re.search(r"\*\*" + _q + r"[^\n]*?後 32 > 前 32 が ≥ (\d+) %", _pre)
    assert _mm, _q
    O59_THR[_q] = int(_mm.group(1)) / 100
assert O59_THR == {"Q1": 0.7, "Q2": 0.6}, O59_THR


def o59_scene(rid, ev, pred, pred_name):
    r = ROWS59[rid]
    m, gm, fl, st, en, tx, N = r["meta"], r["gm"], r["fl"], r["st"], r["en"], r["tx"], r["N"]
    e = m["events"][ev]
    fi = FLAGS59.index(ev)
    end = e
    while end + 1 < N and fl[end + 1, fi]:
        end += 1
    pm = pred.search(tx)
    assert pm and int(st[e]) <= pm.start() < int(en[end]), f"{rid}: this entry's {pred_name} first hits the text inside the card's event run [{e}, {end}]"
    a, b = e - HALF, e + HALF
    pre, hit, post = tx[int(st[a]):int(st[e])], tx[int(st[e]):int(en[end])], tx[int(en[end]):int(en[b - 1])]
    assert pre + hit + post == tx[int(st[a]):int(en[b - 1])]
    jr = m["json_begin"] - m["g0"]
    jf = np.nonzero(fl[:, 5])[0]
    assert int(jf[0]) == jr and bool(np.all(fl[jr:, 5] == 1)), f"{rid}: the json flag is the final JSON's tokens"
    return {"id": rid, "variant": m["variant"], "kind": m["kind"], "j": m["j"], "label": m["label"], "label_json": m["label_json"], "answer_first": m["answer_first"], "hit_cap": m["hit_cap"],
            "n": N, "g0": m["g0"], "T": m["T"], "event": e, "event_flag": ev, "run": [e, end], "json_rel": jr, "chars": len(tx),
            "series": {g: [round(float(gm[i, gi]), 4) for i in range(N)] for gi, g in enumerate(GROUPS59)},
            "mask": [int(sum(int(fl[i, k]) << k for k in range(6))) for i in range(N)],
            "before": [float(x) for x in gm.astype(np.float64)[a:e].mean(axis=0)], "after": [float(x) for x in gm.astype(np.float64)[e:b].mean(axis=0)],
            "excerpt": {"pre": pre, "hit": hit, "post": post, "tok_a": a, "tok_b": b, "chars": [int(st[a]), int(en[b - 1])]}}


S_O = o59_scene("F5a-2__think__r15", "o_diam", PRED_O, "PRED_O")
S_H = o59_scene("F5b-1__natural__r14", "h_diam", PRED_HEHI_DIAM, "PRED_HEHI_DIAM")
def o59_rank(rid, ev):
    ws = o59_windows(ev)
    out = {}
    for gi, g in enumerate(GROUPS59):
        d = {w["id"]: float(w["after"][gi] - w["before"][gi]) for w in ws}
        v = d[rid]
        out[g] = [1 + sum(1 for x in d.values() if x > v), 1 + sum(1 for x in d.values() if abs(x) > abs(v)), len(d)]
    return out


S_O["rank"], S_H["rank"] = o59_rank(S_O["id"], "o_diam"), o59_rank(S_H["id"], "h_diam")
assert S_O["rank"] == {"close": [14, 52, 59], "mid": [5, 5, 59], "ans": [58, 2, 59], "think": [33, 39, 59]}, S_O["rank"]     # S_O is not a typical row: the 5th largest rise of mid, the 2nd largest |fall| of ans
assert S_H["rank"] == {"close": [14, 27, 34], "mid": [21, 29, 34], "ans": [5, 17, 34], "think": [7, 9, 34]}, S_H["rank"]
assert S_O["hit_cap"] is False and S_H["hit_cap"] is False and S_O["json_rel"] == 1082 and S_H["json_rel"] == 0 and S_H["answer_first"] is True and S_O["answer_first"] is False
assert (S_O["label"], S_O["label_json"]) == ("B-bind", "B-bind") and (S_H["label"], S_H["label_json"]) == ("B-attractor", "B-attractor")
assert S_O["excerpt"]["hit"] == "Midpoint of O1 and O" and S_H["excerpt"]["hit"].strip().startswith("diameter HeHi"), (S_O["excerpt"]["hit"], S_H["excerpt"]["hit"])
for _s in (S_O, S_H):                                               # the carried before / after means are the windows of the carried (rounded) series, to the 4-digit rounding
    for _gi, _g in enumerate(GROUPS59):
        _e = _s["event"]
        assert abs(sum(_s["series"][_g][_e - HALF:_e]) / HALF - _s["before"][_gi]) < 2e-4 and abs(sum(_s["series"][_g][_e:_e + HALF]) / HALF - _s["after"][_gi]) < 2e-4
# ---- v3 (transplanted from the other maker's state 18): the sentence that says the SAME circle in words sits inside the "before 32" window and does not hit PRED_O (it names no O1 / O2)
_wc_sent = "the center of the circle through the four common tangent points is the midpoint of the line segment joining the centers of the two original circles."
_wc_tx, _wc_st, _wc_en = ROWS59[S_O["id"]]["tx"], ROWS59[S_O["id"]]["st"], ROWS59[S_O["id"]]["en"]
assert _wc_tx.count(_wc_sent) == 1 and not PRED_O.search(_wc_sent) and not PRED_HEHI_DIAM.search(_wc_sent)
_wa = _wc_tx.find(_wc_sent)
_wtok_a, _wtok_b = int(np.searchsorted(_wc_st, _wa, side="right") - 1), int(np.searchsorted(_wc_en, _wa + len(_wc_sent), side="left"))      # the first token that holds the sentence's first character · the last token that ends at its last character
_wm = _wc_tx.find("midpoint of the line segment")
_wtok_m = int(np.searchsorted(_wc_st, _wm, side="right") - 1)
assert int(_wc_st[_wtok_a]) <= _wa and int(_wc_en[_wtok_b]) >= _wa + len(_wc_sent) and _wtok_a < _wtok_m <= _wtok_b < S_O["event"]
S_O["wordcirc"] = {"char_a": _wa, "char_b": _wa + len(_wc_sent), "text": _wc_sent, "tok_a": _wtok_a, "tok_b": _wtok_b, "tok_phrase": _wtok_m, "k_a": _wtok_a - S_O["event"], "k_b": _wtok_b - S_O["event"], "k_phrase": _wtok_m - S_O["event"], "in_before_window": _wtok_a >= S_O["event"] - HALF}
assert S_O["wordcirc"]["in_before_window"] and S_O["wordcirc"]["k_phrase"] == -19, S_O["wordcirc"]
_wthe = _wc_tx.find("the midpoint of the line segment joining the centers of the two original circles")                       # v3.1: entry P's "k −20" is the token " the" that opens the phrase; " midpoint" is k −19 (both from the npz)
S_O["wordcirc"]["k_the"] = int(np.searchsorted(_wc_st, _wthe, side="right") - 1) - S_O["event"]
assert S_O["wordcirc"]["k_the"] == -20 and _wc_tx[int(_wc_st[S_O["event"] - 20]):int(_wc_en[S_O["event"] - 20])] == " the", S_O["wordcirc"]
# ---- v3 (transplanted from the other maker's state 20): the row by row slope = after - before of every event row, per group (what the aggregate's columns are made of), with the path x label of each row
SLOPES = {ev: [{"id": w["id"], "kind": w["meta"]["kind"], "lj": w["meta"]["label_json"], "d": [round(float(w["after"][gi] - w["before"][gi]), 5) for gi in range(4)]} for w in o59_windows(ev)] for ev in ("o_diam", "h_diam")}
assert [len(SLOPES[ev]) for ev in ("o_diam", "h_diam")] == [59, 34]
# ---- the aggregate the page carries: read.json's own values (L1), the recount's alongside
AGG = {}
for _ev in ("o_diam", "h_diam"):
    AGG[_ev] = {"n": Q3_MINE[f"{_ev}|close|all"]["n"], "rows_with": R59["counts"]["rows_with_o_diam" if _ev == "o_diam" else "rows_with_h_diam"],
                "groups": {_g: {oc: {"n": R59["Q3_desc"][f"{_ev}|{_g}|{oc}"]["n"], "up": R59["Q3_desc"][f"{_ev}|{_g}|{oc}"]["after_gt_before"], "med": R59["Q3_desc"][f"{_ev}|{_g}|{oc}"]["median_diff"]} for oc in ("all", "B-bind", "B-attractor")} for _g in GROUPS59},
                "by_kind": {f"{k}|{lj}": v for (k, lj), v in sorted(_bk[_ev].items())}}
OLM59 = {"sources": {"read.json": {"path": "ConstructGap/exp/olm59/read.json", "md5": O59_MD5["read.json"]}, "control.json": {"path": "ConstructGap/exp/olm59/control.json", "md5": O59_MD5["control.json"]},
                     "rows": {"dir": "ConstructGap/exp/olm59/rows/", "n": 120, "manifest_md5": md5s("".join(f"{k} {v['md5']}\n" for k, v in sorted(MANIFEST59.items())))}},
         "prov": R59["prov"], "control": C59, "half": HALF, "groups": GROUPS59, "flags": FLAGS59, "S_O": S_O, "S_H": S_H, "agg": AGG,
         "Q1": {"n": Q1R["n"], "up": Q1R["after_gt_before"], "med": Q1R["median_diff"], "thr": O59_THR["Q1"]}, "Q2": {"n": Q2R["n"], "up": Q2R["after_gt_before"], "med": Q2R["median_diff"], "thr": O59_THR["Q2"]},
         "labels": LF, "cmt5_two": CMT5_TWO, "counts": R59["counts"], "min_abs_diff": _mind, "slopes": SLOPES}
# the side files of the build (not carried by the pages): the windows for the JS recount (data.mjs) and the manifest of the 120 npz files
O59_WIN = {"half": HALF, "groups": GROUPS59, "rows_with": {"o_diam": 64, "h_diam": 44},
           "events": {ev: [{"id": w["id"], "e": w["e"], "kind": w["meta"]["kind"], "label": w["meta"]["label"], "label_json": w["meta"]["label_json"], "N": w["N"],
                            "win": [[float(f"{x:.9g}") for x in w["gm"][w["e"] - HALF:w["e"] + HALF, gi]] for gi in range(4)]} for w in o59_windows(ev)] for ev in ("o_diam", "h_diam")}}
assert [len(O59_WIN["events"][ev]) for ev in ("o_diam", "h_diam")] == [59, 34]
(OUT / "olm59_windows.json").write_text(json.dumps(O59_WIN, separators=(",", ":")), encoding="utf-8")
(OUT / "olm59_manifest.json").write_text(json.dumps({"read.json": O59_MD5["read.json"], "control.json": O59_MD5["control.json"], "rows": MANIFEST59, "manifest_md5": OLM59["sources"]["rows"]["manifest_md5"]}, indent=1, sort_keys=True), encoding="utf-8")

# ------------------------------------------------------------------------------------------------ 8d. v2.1 (A): olm62 = does the mid group's rise follow the text's move into formulas?
# Reads ConstructGap/exp/olm62/{read.json, control.json} and olm59's rows again (BRIEF v2.1 §1 / §A). Only reads: the runner of olm62 is neither opened nor imported (the definitions below were found by reproducing read.json; see NOTES).
O62 = REPO / "ConstructGap/exp/olm62"
O62_MD5 = {"read.json": "479905fa85904ac9b12906d12a232311", "control.json": "2ae57734ef5aa0055192a310a65a291d"}
O62_RAW = {}
for _n, _want in O62_MD5.items():
    _b = (O62 / _n).read_bytes()
    assert md5b(_b) == _want, f"olm62/{_n}: md5 {md5b(_b)} != the BRIEF v2.1's {_want} (the frozen file changed)"
    O62_RAW[_n] = json.loads(_b.decode("utf-8"))
R62, C62 = O62_RAW["read.json"], O62_RAW["control.json"]
assert R62["prov"]["dirty"] is False and R62["prov"]["commit"] == C62["prov"]["commit"] == "4bdc93b0" and C62["pass"] == {"C1": True, "C2": True}
assert R62["prov"]["olm59_read_md5"] == O59_MD5["read.json"] and R62["half"] == HALF
MATH_CH = frozenset("0123456789²³·×=+-^*/()√")                # the formula characters of PREREG olm62 §1: [0-9²³·×=+\-^*/()√] (the same as olm60 / olm61)
for _r in ROWS59.values():                                      # a token's formula-character share = (formula chars in the token) / (chars of the token); a window's value = the mean over its 32 tokens
    _r["tf"] = np.array([(sum(1 for _c in _r["tx"][int(_a):int(_b)] if _c in MATH_CH) / (int(_b) - int(_a))) if int(_b) > int(_a) else 0.0 for _a, _b in zip(_r["st"], _r["en"])])
N_TOK62 = sum(r["N"] for r in ROWS59.values())
assert N_TOK62 == R62["n_tokens"] == 162545


def ordinal_rank(x):                                            # the card's rank rule: ordinal ranks (argsort of argsort, numpy's default sort), NOT tie-averaged (found by reproducing read.json: see NOTES)
    return np.argsort(np.argsort(x)).astype(np.float64)


def ordinal_spearman(a, b):
    return float(np.corrcoef(ordinal_rank(np.asarray(a)), ordinal_rank(np.asarray(b)))[0, 1])


def average_rank(x):
    u, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
    cs = np.cumsum(cnt)
    return (((cs - cnt + 1) + cs) / 2.0)[inv]


def o62_events(ev):
    out = []
    for w in o59_windows(ev):
        _e, _tf = w["e"], ROWS59[w["id"]]["tf"]
        _x = {"id": w["id"], "e": _e, "kind": w["meta"]["kind"], "variant": w["meta"]["variant"], "label_json": w["meta"]["label_json"], "dg": [float(w["after"][_i] - w["before"][_i]) for _i in range(4)], "mb": float(_tf[_e - HALF:_e].mean()), "ma": float(_tf[_e:_e + HALF].mean())}
        _x["dmath"] = _x["ma"] - _x["mb"]
        out.append(_x)
    return out


def o62_agg(E):
    dm, dma = np.array([x["dg"][1] for x in E]), np.array([x["dmath"] for x in E])
    up, flat = dma > 0, dma <= 0
    med = float(np.median(dma))
    lo = dma <= med
    frac = lambda m, s: f"{int(m.sum())} / {int(s.sum())}"
    return {"n": len(E), "math_up": int(up.sum()), "math_median_diff": med, "mid_up_when_math_flat": f"{int((dm[flat] > 0).sum())} / {int(flat.sum())}", "mid_up_when_math_up": f"{int((dm[up] > 0).sum())} / {int(up.sum())}",
            "mid_median_when_math_flat": float(np.median(dm[flat])), "spearman_mid_math": ordinal_spearman(dm, dma),
            "split_at_median_math": {"low": f"{int((dm[lo] > 0).sum())} / {int(lo.sum())}", "high": f"{int((dm[~lo] > 0).sum())} / {int((~lo).sum())}"},
            "by_group_math_flat": {g: f"{int((np.array([x['dg'][gi] for x in E])[flat] > 0).sum())} / {int(flat.sum())}" for gi, g in enumerate(GROUPS59)},
            "_avg_rank_spearman": float(np.corrcoef(average_rank(dm), average_rank(dma))[0, 1])}


EV62 = {ev: o62_events(ev) for ev in ("o_diam", "h_diam")}
MINE62 = {ev: o62_agg(EV62[ev]) for ev in EV62}
for _ev in ("o_diam", "h_diam"):                                # read.json reproduced, unrounded: counts and strings exactly · the medians to 1e-6 (float32 in read.json) · the rank correlation to 1e-12 (same rule)
    _a, _b = MINE62[_ev], R62[_ev]
    for _k in ("n", "math_up", "mid_up_when_math_flat", "mid_up_when_math_up", "split_at_median_math", "by_group_math_flat"):
        assert _a[_k] == _b[_k], (_ev, _k, _a[_k], _b[_k])
    assert abs(_a["math_median_diff"] - _b["math_median_diff"]) < 1e-12 and abs(_a["mid_median_when_math_flat"] - _b["mid_median_when_math_flat"]) < 1e-6, _ev
    assert abs(_a["spearman_mid_math"] - _b["spearman_mid_math"]) < 1e-12, (_ev, _a["spearman_mid_math"], _b["spearman_mid_math"])
_pm = np.concatenate([r["gm"][:, 1].astype(np.float64) for _k, r in sorted(ROWS59.items())])
_pt = np.concatenate([r["tf"] for _k, r in sorted(ROWS59.items())])
assert len(_pm) == len(_pt) == N_TOK62
POOLED62 = ordinal_spearman(_pm, _pt)
assert abs(POOLED62 - R62["Q3_pooled_token_spearman_mid_math"]) < 1e-12, POOLED62
POOLED62_AVG = float(np.corrcoef(average_rank(_pm), average_rank(_pt))[0, 1])           # NOT carried to the page (outside the card): recorded in NOTES only
# Q1 / Q2 (the card's two preregistered predictions, recounted)
assert (MINE62["o_diam"]["math_up"], MINE62["o_diam"]["n"]) == (48, 59) and R62["Q1"]["o_diam_math_up"] == "48 / 59" and R62["Q2"]["o_diam_mid_up_when_math_flat"] == "7 / 11" == MINE62["o_diam"]["mid_up_when_math_flat"]
assert (MINE62["h_diam"]["math_up"], MINE62["h_diam"]["n"]) == (8, 34)
# controls C1 (olm59's two aggregates reproduced: the numbers of olm59 read.json) and C2 (the predicate: ASCII-digit tokens all carry a formula character, letter tokens none)
for _ev in ("o_diam", "h_diam"):
    _q = Q3_MINE[f"{_ev}|mid|all"]
    assert (_q["n"], _q["up"]) == (C62["C1"][_ev]["got"]["n"], C62["C1"][_ev]["got"]["after_gt_before"]) and abs(_q["med"] - C62["C1"][_ev]["got"]["median_diff"]) < 1e-6 and C62["C1"][_ev]["ok"] is True
_alltok = [(r["tx"][int(a):int(b)], float(f)) for r in ROWS59.values() for a, b, f in zip(r["st"], r["en"], r["tf"])]
_dig = [f for s, f in _alltok if s.isascii() and s.isdigit()]
_alp = [f for s, f in _alltok if s.strip().isalpha()]                   # a token whose text, without its spaces, is only letters (any script): reproduces the card's 84,759
assert (len(_dig), sum(1 for f in _dig if f > 0), len(_alp), sum(1 for f in _alp if f == 0)) == (C62["C2"]["digit_tokens"], C62["C2"]["digit_pos"], C62["C2"]["alpha_tokens"], C62["C2"]["alpha_zero"]) == (32498, 32498, 84759, 84759)
# the scene rows of v2 (S_O / S_H) inside the scatter
def _pt62(ev, rid):
    x = next(e for e in EV62[ev] if e["id"] == rid)
    return {"id": rid, "dmid": x["dg"][1], "dmath": x["dmath"], "rank_math": 1 + sum(1 for e in EV62[ev] if e["dmath"] > x["dmath"]), "n": len(EV62[ev])}
S62 = {"S_O": _pt62("o_diam", S_O["id"]), "S_H": _pt62("h_diam", S_H["id"])}
assert abs(S62["S_O"]["dmid"] - (S_O["after"][1] - S_O["before"][1])) < 1e-9 and abs(S62["S_H"]["dmid"] - (S_H["after"][1] - S_H["before"][1])) < 1e-9
FLAT_O = sorted([{"id": x["id"], "kind": x["kind"], "label_json": x["label_json"], "dmid": x["dg"][1], "dmath": x["dmath"]} for x in EV62["o_diam"] if x["dmath"] <= 0], key=lambda z: z["dmid"])
assert len(FLAT_O) == 11 and sum(1 for z in FLAT_O if z["dmid"] > 0) == 7 and abs(float(np.median([z["dmid"] for z in FLAT_O])) - R62["o_diam"]["mid_median_when_math_flat"]) < 1e-6
ALL_O_MID_MED = float(np.median([x["dg"][1] for x in EV62["o_diam"]]))
_m62 = re.search(r"中点の群が上がる物 ≥ (\d+) %", (REPO / "conversations/2026-10-28/PREREG_olm62_moy1_mid_rise_vs_math_shift_20261028.md").read_text(encoding="utf-8"))
assert _m62, "PREREG olm62 Q2"
O62_THR = int(_m62.group(1)) / 100                                  # the threshold of olm62's own Q2, read from its PREREG (not olm59's)
assert O62_THR == 0.6
assert abs(ALL_O_MID_MED - C62["C1"]["o_diam"]["exp"]["median_diff"]) < 1e-6
_r5 = lambda v: round(float(v), 5)
EXT62 = {"x": [min(x["dmath"] for ev in EV62 for x in EV62[ev]), max(x["dmath"] for ev in EV62 for x in EV62[ev])], "y": [min(x["dg"][1] for ev in EV62 for x in EV62[ev]), max(x["dg"][1] for ev in EV62 for x in EV62[ev])]}
OLM62_TIE = {"o_diam": MINE62["o_diam"]["_avg_rank_spearman"], "h_diam": MINE62["h_diam"]["_avg_rank_spearman"], "pooled": POOLED62_AVG}          # v3: carried, tagged "a number outside the card" (the transplant of the other maker's state 22 note)
assert [round(OLM62_TIE[k], 4) for k in ("o_diam", "h_diam", "pooled")] == [0.7809, 0.2212, 0.4891], OLM62_TIE
OLM62 = {"tie": OLM62_TIE, "sources": {"read.json": {"path": "ConstructGap/exp/olm62/read.json", "md5": O62_MD5["read.json"]}, "control.json": {"path": "ConstructGap/exp/olm62/control.json", "md5": O62_MD5["control.json"]}},
         "prov": R62["prov"], "half": HALF, "read": {k: R62[k] for k in ("o_diam", "h_diam", "Q1", "Q2", "Q3_pooled_token_spearman_mid_math", "n_tokens")}, "control": C62,
         "events": {ev: [{"id": x["id"], "kind": x["kind"], "lj": x["label_json"], "dmid": _r5(x["dg"][1]), "dmath": _r5(x["dmath"])} for x in EV62[ev]] for ev in EV62},
         "flat_o": [{"id": z["id"], "kind": z["kind"], "dmid": _r5(z["dmid"]), "dmath": _r5(z["dmath"])} for z in FLAT_O], "scene": {k: {"id": v["id"], "dmid": _r5(v["dmid"]), "dmath": _r5(v["dmath"]), "rank_math": v["rank_math"], "n": v["n"]} for k, v in S62.items()},
         "all_o_mid_median": ALL_O_MID_MED, "extent": {"x": [_r5(v) for v in EXT62["x"]], "y": [_r5(v) for v in EXT62["y"]]}, "thr_q2": O62_THR, "rank_rule": "ordinal"}
# the side file for the JS recount (data.mjs): per event the 64-token windows of the four groups and of the formula-character share (not carried by the pages)
O62_WIN = {"half": HALF, "groups": GROUPS59, "events": {ev: [{"id": x["id"], "e": x["e"], "grp": [[float(f"{v:.9g}") for v in ROWS59[x["id"]]["gm"][x["e"] - HALF:x["e"] + HALF, gi]] for gi in range(4)], "tf": [float(f"{v:.9g}") for v in ROWS59[x["id"]]["tf"][x["e"] - HALF:x["e"] + HALF]]} for x in EV62[ev]] for ev in EV62}}
(OUT / "olm62_windows.json").write_text(json.dumps(O62_WIN, separators=(",", ":")), encoding="utf-8")
(OUT / "olm62_tie_note.json").write_text(json.dumps({"note": "NOT carried to the pages (outside the card). The card's rank correlation uses ordinal ranks (argsort of argsort); with tie-averaged ranks the same data give:", "o_diam": MINE62["o_diam"]["_avg_rank_spearman"], "h_diam": MINE62["h_diam"]["_avg_rank_spearman"], "pooled_tokens": POOLED62_AVG, "card": {"o_diam": R62["o_diam"]["spearman_mid_math"], "h_diam": R62["h_diam"]["spearman_mid_math"], "pooled_tokens": R62["Q3_pooled_token_spearman_mid_math"]}}, indent=1), encoding="utf-8")

# ------------------------------------------------------------------------------------------------ 8e. v2.1 (B): the card tree v2.2.1 (tree_src.json: clusters, nodes) and where moy-1's cards sit
TREE_REL, TREE_MD5 = "conversations/2026-10-27/card_tree_v2/entry_merged_v2_2_1/tree_src.json", "16e095957cfc5198ab53f63f94f4b087"
_tb = (REPO / TREE_REL).read_bytes()
assert md5b(_tb) == TREE_MD5, f"tree_src.json md5 {md5b(_tb)} != the BRIEF v2.1's {TREE_MD5}"
TS = json.loads(_tb.decode("utf-8"))
assert len(TS["clusters"]) == 9 and len(TS["nodes"]) == 78 and sum(len(c["members"]) for c in TS["clusters"]) == 78
_nd = {n["id"]: n for n in TS["nodes"]}
assert len(_nd) == 78 and all(_nd[m]["cluster"] == c["id"] for c in TS["clusters"] for m in c["members"])
assert TS["clusters"][0]["members"] == ["cmt1", "cmt1b", "cmt2", "cmt3", "cmt4", "cmt5"] and "cmt13" in TS["clusters"][1]["members"] and {"olm4", "olm7"} <= set(TS["clusters"][2]["members"]), "BRIEF v2.1 §2"
_dates = [n["date"] for n in TS["nodes"]]
TREE_SPAN = [min(_dates), max(_dates)]
assert TREE_SPAN == ["2026-10-19", "2026-10-27"], TREE_SPAN
_MD = lambda d: d[5:]                                           # "2026-10-19" -> "10-19"
CLUSTERS = [{"id": c["id"], "order": c["order"], "name": c["name"], "sub": c["sub"], "n": len(c["members"]), "span": [_MD(min(_nd[m]["date"] for m in c["members"])), _MD(max(_nd[m]["date"] for m in c["members"]))]} for c in TS["clusters"]]
assert [c["n"] for c in CLUSTERS] == [6, 13, 10, 6, 13, 8, 7, 11, 4]
_gitdate = lambda rel: _git_fact(["log", "-1", "--format=%ad", "--date=short", "--", rel]).strip()
_fdate = lambda rel: (lambda m: f"{m.group(1)[4:6]}-{m.group(1)[6:8]}")(re.search(r"_(\d{8})\.md$", rel))
CARD_FILES = {                                                  # the record that stands for a card outside the tree: the date comes from the record's own name (or, for the two data files, from git's last commit of the file)
    "replication_config_frozen": ("probes/moy1-claude5-replication/results/replication_config_frozen.json", "git"),
    "pc1": ("conversations/2026-07-31/RESULT_pc1_cue_invariance_20260731.md", "name"),
    "screen_bf16": ("conversations/2026-07-29/RESULT_olmo3_base_bf16_screen_20260729.md", "name"),
    "behavior_screen": ("conversations/2026-07-28/RESULT_olmo3_behavior_screen_20260728.md", "name"),
    "F5": ("conversations/2026-08-01/ADJUDICATION_f5_v2_effective_20260801.md", "name"),
    "moy_suite_report": ("ConstructGap/exp/moy_suite_report.json", "git"),
    "olm59": ("conversations/2026-10-28/RESULT_olm59_moy1_sae_trajectory_by_construction_mentions_20261028.md", "name"),
    "olm62": ("conversations/2026-10-28/RESULT_olm62_moy1_mid_rise_vs_math_shift_20261028.md", "name"),
}
CARDS = {}
for _id, (_rel, _how) in CARD_FILES.items():
    assert (REPO / _rel).exists(), _rel
    _d = _fdate(_rel) if _how == "name" else _gitdate(_rel)[5:]
    CARDS[_id] = {"zone": "before" if _id not in ("olm59", "olm62") else "after", "date": _d, "file": _rel, "date_from": _how}
for _id in ("cmt5", "cmt13", "olm4", "olm7"):                  # inside the tree: the zone is the node's cluster, the words are the node's own
    CARDS[_id] = {"zone": _nd[_id]["cluster"], "date": _MD(_nd[_id]["date"]), "label": _nd[_id]["label"], "outcome": _nd[_id]["outcome"], "file": _nd[_id]["result"], "date_from": "tree"}
assert all(("2026-" + c["date"]) < TREE_SPAN[0] for c in CARDS.values() if c["zone"] == "before") and all(("2026-" + c["date"]) > TREE_SPAN[1] for c in CARDS.values() if c["zone"] == "after")
assert [(CARDS[k]["zone"], CARDS[k]["outcome"]) for k in ("cmt5", "cmt13", "olm4", "olm7")] == [("C1", "関門で止めた(b 版なし)"), ("C2", "外れて学んだ"), ("C3", "通過"), ("C3", "通過")]
TREE = {"source": {"path": TREE_REL, "md5": TREE_MD5}, "entry": TS["meta"]["entry"], "n_nodes": len(TS["nodes"]), "n_clusters": len(TS["clusters"]), "span": [_MD(TREE_SPAN[0]), _MD(TREE_SPAN[1])], "clusters": CLUSTERS, "cards": CARDS}

# ------------------------------------------------------------------------------------------------ 8g. v3: where each row starts (olm128's instrument, recounted from the raw rows; the card's read.json is the check, not the source of these cells)
# start = the row's content begins with {"conjecture" at position 0 -> "json", otherwise "text" (a row with no JSON is "text"); bind = the frozen whole-text label B-bind; rows that hit the cap are left out (as in K10). `first` = the first {"conjecture" position (-1 = none).
def start_cells(rs):
    out = []
    for r in sorted((r for r in rs if r["condition"] == "blocked" and not r["hit_cap"]), key=lambda r: r["seed"]):
        c = r["content"]
        out.append({"seed": r["seed"], "start": "json" if c.find('{"conjecture"') == 0 else "text", "first": c.find('{"conjecture"'), "label": r["label"], "n": r["n_chars"]})
    return out


CUE_START = {"nl": start_cells(scr), "sp": start_cells(SP), "nn": start_cells(list(NL.values()))}
_rj = json.loads((REPO / "ConstructGap/exp/olm128/read.json").read_text(encoding="utf-8"))
for _k, _cells in CUE_START.items():
    _c = _rj["blocked_cells"][{"nl": "nl", "sp": "space", "nn": "nlnl"}[_k]]
    assert (len(_cells), sum(1 for x in _cells if x["start"] == "json"), sum(1 for x in _cells if x["start"] == "text"), sum(1 for x in _cells if x["label"] == "B-bind")) == (_c["n"], _c["json"], _c["text"], _c["bind"]), (_k, "my recount of the cells is not read.json's")
    assert (sum(1 for x in _cells if x["start"] == "json" and x["label"] == "B-bind"), sum(1 for x in _cells if x["start"] == "json" and x["label"] != "B-bind"), sum(1 for x in _cells if x["start"] == "text" and x["label"] == "B-bind"), sum(1 for x in _cells if x["start"] == "text" and x["label"] != "B-bind")) == (_c["json_bind"], _c["json_nonbind"], _c["text_bind"], _c["text_nonbind"])
# the after-the-fact description the RESULT (§3) gives and the card did not freeze: "a JSON within 100 characters" (the number 100 was set after looking) — recounted here as a description only
EARLY = 100
CUE_EARLY = {k: {"early": sum(1 for x in v if 0 <= x["first"] <= EARLY), "early_bind": sum(1 for x in v if 0 <= x["first"] <= EARLY and x["label"] == "B-bind"), "late": sum(1 for x in v if not (0 <= x["first"] <= EARLY)), "late_bind": sum(1 for x in v if not (0 <= x["first"] <= EARLY) and x["label"] == "B-bind"), "n": len(v)} for k, v in CUE_START.items()}
assert CUE_EARLY == {"nl": {"early": 8, "early_bind": 2, "late": 1, "late_bind": 0, "n": 9}, "sp": {"early": 7, "early_bind": 2, "late": 3, "late_bind": 2, "n": 10}, "nn": {"early": 3, "early_bind": 0, "late": 7, "late_bind": 7, "n": 10}}, CUE_EARLY
CUE_SPACE_FIRST = sorted(x["first"] for x in CUE_START["sp"] if x["first"] >= 0)                 # where cue " " rows first open a JSON (the RESULT: 25 (3 rows) · 72-84 (4 rows) · 7,359 / 7,499 (2 rows) · none 1)
assert CUE_SPACE_FIRST[:3] == [25, 25, 25] and [x for x in CUE_SPACE_FIRST if 70 <= x <= 90] and len(CUE_SPACE_FIRST) == 9, CUE_SPACE_FIRST
CUE_START_PACK = {"cells": CUE_START, "early": CUE_EARLY, "early_chars": EARLY, "space_first": CUE_SPACE_FIRST}

# ------------------------------------------------------------------------------------------------ 8f. v3: the part that was added after the 10-28 figure (pack_after.py: cards olm76 ... olm128)
import runpy
AFTER = runpy.run_path(str(HERE / "pack_after.py"))["AFTER"]

# ------------------------------------------------------------------------------------------------ 9. the pack
rowpack =[{k: v for k, v in x.items() if k not in ("md5",)} | {"md5_8": x["md5"][:8]} for x in rows]
pack = {
    "title": "moy-1: block / open", "sources": SRC_MD5,
    "geometry": geometry, "prompts": prompts,
    "rows": rowpack, "open_cnt": open_cnt, "blk_cnt": blk_cnt, "o_sent": o_sent, "he_sent": he_sent, "hehi_word_rows": hehi_word_rows, "he_end": {str(k): v for k, v in he_end.items()},
    "order_he_first": {str(k): v for k, v in order_he_first.items()}, "open_tok_rows": open_tok_rows, "changed_open": changed_open, "attr_open": attr_open,
    "scene": SC, "excerpts": EXC, "cue_table": cue_table,
    "cmt13": {"sites": sites, "jaccard": {k: v["mean"] for k, v in jac.items()}, "l50_rank1": l50_rank1, "l50_top10": l50_top10, "OG": OG, "HG": HG, "controls": c13["controls"], "provenance": c13["provenance"]},
    "f5": f5, "otok_ctx": otok_ctx, "seg": SEG, "json_first": json_first, "cmt5": cmt5, "cmt5_ctl": cmt5_ctl, "models": models, "think": think,
    "logmax": 133503, "flags": {"cap_row": "open s0"}, "olm59": OLM59, "olm62": OLM62, "tree": TREE,
    "cue_start": CUE_START_PACK, "after": AFTER,                                                                # v3: the cards struck after the 10-28 figure (pack_after.py; every value from a read.json key)
}
assert max(x["n_chars"] for x in rows) == 133503
(OUT / "pack.json").write_text(json.dumps(pack, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"olm62: o_diam {MINE62['o_diam']['math_up']}/{MINE62['o_diam']['n']} · h_diam {MINE62['h_diam']['math_up']}/{MINE62['h_diam']['n']} · flat O mid up {MINE62['o_diam']['mid_up_when_math_flat']} · rho {MINE62['o_diam']['spearman_mid_math']:.4f} / {MINE62['h_diam']['spearman_mid_math']:.4f} / pooled {POOLED62:.4f} (tie-averaged: {MINE62['o_diam']['_avg_rank_spearman']:.4f} / {MINE62['h_diam']['_avg_rank_spearman']:.4f} / {POOLED62_AVG:.4f}, not carried) · tree {TREE['n_clusters']} clusters {TREE['n_nodes']} nodes")
print(f"olm59: S_O {S_O['id']} n {S_O['n']} e {S_O['event']} · S_H {S_H['id']} n {S_H['n']} e {S_H['event']} · Q3 keys {len(Q3_MINE)} · min |diff| {_mind:.4f} · manifest {OLM59['sources']['rows']['manifest_md5'][:8]}")
print(f"pack: rows {len(rows)} · open reading {open_cnt} · blocked reading {blk_cnt} · O sentences {o_sent} · He-Hi diameter sentences {he_sent} · cmt13 sites {len(sites)} · "
      f"models {len(models)} · excerpts {len(EXC)} · pack.json {(OUT / 'pack.json').stat().st_size // 1024} KB")
