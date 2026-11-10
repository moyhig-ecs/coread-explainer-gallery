"""make_anchors_v21.py — v2.1 (BRIEF v2.1 §2-2〜§2-7): adds the anchors of what this version moved, decided and fixed, and writes CLAIMS_v21.md (one row per anchor).
Run once after pack_data.py (it reads generated/pack.json for the grade of each card and for the values it anchors; the anchors then check the PLACE itself, never the pack).
Idempotent: anchors whose note starts with "v2.1 " are dropped and written again. It also rewrites the grade words of rows K250–K269 in CLAIMS_after.md (G-26).
    python -I make_anchors_v21.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(__import__("os").environ.get("MOY5_REPO", HERE / "data"))   # bundle: the frozen files are copied under data/ at their repo paths (MOY5_REPO = another root, e.g. the house repo)
X = REPO / "ConstructGap" / "exp"
P = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
A = [a for a in json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8")) if not a.get("note", "").startswith("v2.1 ")]
nid = max(int(a["id"][1:]) for a in A) + 1
POST = {p["id"]: p for p in P["post"]}
SCOPE = "conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md"
rows = []   # (id, claim, source, level, states)


def add(kind, note, claim, source, states, level="L1", **kw):
    global nid
    a = {"id": f"K{nid:03d}", "kind": kind, "note": "v2.1 " + note, **kw}
    A.append(a)
    rows.append((a["id"], claim, source, level, states))
    nid += 1


def res_of(cid):
    return POST[cid]["result"]


# ---- 1. the grade rule (§2-5): one anchor per card (recomputed in check_claims.py from SCOPE 10-31 or the RESULT line) + the five columns
grade_cards = []
for cid, p in POST.items():
    kw = {"card": cid, "rule": p["rule"]}
    if p["rule"] == "ii":
        line = p["grade_src"].split("«", 1)[1].rstrip("»")
        kw.update(file=res_of(cid), literal=line, grade_ii=p["grade5"])
        src = f"`{res_of(cid)}` · «{line}»"
    else:
        src = f"`{SCOPE}` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: {' · '.join(p['tiers'])}"
    add("grade_rule", f"grade {cid}", f"{cid} · grade **{p['grade5']}** · rule ({p['rule']})", src, "23–26, 30", expect=p["grade5"], **kw)
    grade_cards.append({k: v for k, v in kw.items()})
T = P["post_tally"]["grade"]
add("grade_sum", "grade five columns", f"the five columns: 判定 {T['判定']} · 記述 {T['記述']} · 較正 {T['較正']} · 言えない {T['言えない']} · 関門で止まった {T['関門']} = **20** (rule i {P['post_tally']['rule']['i']} · ii {P['post_tally']['rule']['ii']})",
    f"`{SCOPE}` §1 + the RESULT lines of the 9 cards not named there", "23, 30", expect=T, cards=grade_cards)

# ---- 2. states 0–11 and 12–22: the values moved from entry P and the data decisions ①–⑦
B = lambda m: f"results_b5bp_20261014_claude-{m}_a.jsonl"
for m, mod, want in [("opus-5-5", "claude-opus-5-5", 19.5), ("fable-5-1", "claude-fable-5-1", 19.5), ("sonnet-5-5", "claude-sonnet-5-5", 11.0)]:
    add("median_len", f"relations median b5bp Bbp {m}", f"b5bp Bbp {m} · median number of relations = **{want}** (mean of the two middle rows = the SUMMARY's relations column)", f"`ConstructGap/exp/{B(m)}` · relations", "14", files=[B(m)], model=mod, arm="Bbp", field="relations", expect=want)
add("median_len", "relations median arg5 Bbp", "arg5 Bbp · median number of relations = **36.0**", "`ConstructGap/exp/results_arg5_20261016_gemini-4-argon_a.jsonl` · relations", "14", files=["results_arg5_20261016_gemini-4-argon_a.jsonl"], arm="Bbp", field="relations", expect=36.0)
for f, mod, want in [(B("sonnet-5-5"), "claude-sonnet-5-5", 1030), (B("opus-5-5"), "claude-opus-5-5", 1753), (B("fable-5-1"), "claude-fable-5-1", 2233), ("results_arg5_20261016_gemini-4-argon_a.jsonl", None, 8494)]:
    kw = {"files": [f], "arm": "Bbp", "field": "reasoning_tokens", "expect": want}
    if mod:
        kw["model"] = mod
    add("median_high", f"reasoning median_high {f}", f"{f.split('_')[1]} Bbp {mod or 'Argon'} · the upper of the two middle rows of reasoning_tokens = **{want:,}** (= the SUMMARY §6 table's value · decision ①)", f"`ConstructGap/exp/{f}` · reasoning_tokens", "14", **kw)
add("count_all", "parabola and cut neq3 A/Q2 opus", "neq3 A/Q2 Opus · rows with a parabola AND a cut in the answer field = **7** (every cut row also writes the locus)", "`results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · parabola_in_conjecture ∧ cut_in_conjecture", "8",
    files=["results_neq3_moy5_20261019_claude-opus-5-5.jsonl"], model="claude-opus-5-5", arm="A/Q2", fields=["parabola_in_conjecture", "cut_in_conjecture"], expect=7)
add("count_all", "parabola and cut neq6 max opus", "neq6 max Opus · rows with both in the answer field = **18** (locus 19 · cut 19 · decision ⑤)", "`results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · parabola_in_conjecture ∧ cut_in_conjecture", "11",
    files=["results_neq6_moy5_20261019_claude-opus-5-5.jsonl"], model="claude-opus-5-5", arm="A/Q2@max", fields=["parabola_in_conjecture", "cut_in_conjecture"], expect=18)
add("text_contains", "P5K = essay4 K hint verbatim", "prf1 P5K = Bbp + essay4's K hint verbatim + PROOF (decisions ③ ④: the K-hint card's source is SOURCE 10-14, not mnw1; P5K is kept off the road)", "`conversations/2026-10-21/PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md` l.23", "4, 17",
    file="conversations/2026-10-21/PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md", literal="Bbp + essay4 の K の hint(逐語)+ PROOF")
add("text_contains", "P5K = the instrument's positive control", "prf1's PREREG names P5K the instrument's positive control (gate: LATX ≥ 8 / 10) — decision ④", "same PREREG l.52", "4",
    file="conversations/2026-10-21/PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md", literal="**計器の陽性統制(gate)**: P5K の LATX ≥ 8 / 10")
MN = {"opus": ("results_mnw1_moy5_20261022_claude-opus-5-5.jsonl", "claude-opus-5-5"), "fable": ("results_mnw1_moy5_20261022_claude-fable-5-1.jsonl", "claude-fable-5-1"), "fableb": ("results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl", "claude-fable-5-1")}
for key, rep, lit in [("opus", 12, "VE : VP_x = VP_x : VJ"), ("fable", 3, "VE : VP_x = VP_x : VJ"), ("fableb", 7, "VE : VP_x = VP_x : VJ"), ("fableb", 17, "FV : FP_x = FP_x : KP_y")]:
    f, mod = MN[key]
    add("phrase", f"none/Q1f cut row {mod} r{rep}", f"mnw1 none/Q1f {mod} r{rep} · the answer field writes the floor as a ratio, then «{lit}» (decision ⑦: an answer-field cut, not only a degenerate proportion)", f"`ConstructGap/exp/{f}` · raw", "28", file=f, model=mod, arm="none/Q1f", rep=rep, literal=lit)

# ---- 3. the part after 10-28 (D3 ①–⑥ and the one-reader items kept) — the card's own json (R4)
J = [("olm67", "olm67/read.json", ["Q2", "frac_top5_by_k", "2"], 0.75, "post-hoc look-ahead 2 tokens before = 75 % (dashed; D3 ①)", "24"),
     ("olm67", "olm67/read.json", ["Q3", "diff"], 0.053865, "Q3 run-up difference cut − floor = +0.054 (✓; not for outside use · D3 ② · G-04)", "24"),
     ("olm67", "olm67/read.json", ["Q1_desc", "cut|opus", "median_delta"], 0.824649, "d̂ cut Opus +0.825 (G-01)", "24"),
     ("olm67", "olm67/read.json", ["Q1_desc", "cut|fable", "median_delta"], 0.744157, "d̂ cut Fable +0.744 (G-01)", "24"),
     ("olm67", "olm67/read.json", ["Q1_desc", "floor_only|opus", "median_delta"], 0.867854, "d̂ floor Opus +0.868 (G-01)", "24"),
     ("olm67", "olm67/read.json", ["Q1_desc", "floor_only|fable", "median_delta"], 0.226849, "d̂ floor Fable +0.227 (G-01: Fable separates)", "24"),
     ("olm67", "olm67/read.json", ["Q1", "median_delta"], 0.76525, "d̂ cut all median +0.765 (G-24)", "24"),
     ("olm67", "olm67/read.json", ["Q1", "null_median_p95"], 0.135165, "random 95 % point 0.135 (G-24)", "24"),
     ("olm67", "olm67/read.json", ["Q1_desc", "floor_only|all", "median_delta"], 0.512018, "d̂ floor all +0.512 (G-24)", "24"),
     ("olm64", "olm64/read.json", ["Q1_P5B_lat_L32", "null_median_p95"], 0.17652, "olm64 random 95 % point 0.1765 (G-24)", "24"),
     ("olm64", "olm64/read.json", ["Q3_apex_minus_floor_L32", "null_p95"], 0.364516, "olm64 Q3 null 0.3645 (G-24)", "24"),
     ("olm71", "olm71/read.json", ["gates_test", "BODY|L", "rows_nonempty"], 57, "olm71 BODY|L 57 / 75 = 76 % (D3 ③)", "25"),
     ("olm71", "olm71/read.json", ["gates_test", "BODY|L", "n_rows"], 75, "olm71 BODY|L n 75", "25"),
     ("olm71", "olm71/read.json", ["gates_test", "BODY|A", "rows_nonempty"], 11, "olm71 BODY|A 11 / 16 = 69 % (D3 ③)", "25"),
     ("olm71", "olm71/read.json", ["gates_test", "BODY|A", "n_rows"], 16, "olm71 BODY|A n 16", "25"),
     ("olm72", "olm72/read.json", ["gates_test", "BODY|L", "rows_nonempty"], 57, "olm72 BODY|L 57 / 75 (D3 ③)", "25"),
     ("olm72", "olm72/read.json", ["gates_test", "BODY|A", "rows_nonempty"], 11, "olm72 BODY|A 11 / 16 (D3 ③)", "25"),
     ("olm80", "olm80/control.json", ["C2_within_card_null", "null_auc32", "median"], 0.521949, "olm80 within-card null median 0.522 (the line 0.60 is on the 95 % point · decision ⑨ · G-21)", "26"),
     ("olm81", "olm81/read.json", ["Q3_desc", "F_vs_W_O", "diff_F_minus_W"], 0.027467, "olm81 Q3 formula − words +0.027 (R3 one-reader item kept: SCOPE 記述)", "25"),
     ("olm81", "olm81/read.json", ["Q3_desc", "F_vs_W_O", "perm_p_two_sided"], 0.128, "olm81 Q3 permutation p 0.13", "25"),
     ("olm81", "olm81/read.json", ["Q1_formula_only_O", "median"], 0.069812, "olm81 median +0.070 (G-24)", "25"),
     ("olm74", "olm74/read.json", ["Q2", "binom_p"], 8.063903e-09, "olm74 Q2 sign test p 8.1e−9 (rows as independent · G-06)", "25"),
     ("olm63", "olm63/read.json", ["Q1_ascii_gain", "S2_minus_S1"], 0.009313, "olm63 Q1 ASCII +0.0093 ✗ (decision ⑪)", "26"),
     ("olm63", "olm63/read.json", ["Q2_no_prompt_gain", "S3_minus_S1"], 0.051562, "olm63 Q2 no question text +0.0516 ✓ (decision ⑪)", "26"),
     ("olm82", "olm82/read.json", ["Q2_jlens_rho_common_vs_entropy", "S2_given_route"], 0.772181, "olm82 ρ min 0.772 (line 0.3 · G-24)", "25"),
     ("olm82", "olm82/read.json", ["Q2_jlens_rho_common_vs_entropy", "S3_formula_only"], 0.836082, "olm82 ρ max 0.836", "25")]
for cid, f, path, want, what, st in J:
    tol = 1e-12 if want < 1e-6 else (5e-6 if isinstance(want, float) else None)
    kw = {"file": f, "path": path, "expect": want}
    if tol:
        kw["tol"] = tol
    add("json_key", f"{cid} {'.'.join(path)}", f"{what}", f"`ConstructGap/exp/{f}` · {' → '.join(path)}", st, **kw)
for mod, field, want in [("claude-opus-5-5", "thinking_tokens", 2724), ("claude-fable-5-1", "thinking_tokens", 7704), ("claude-opus-5-5", "summary_chars", 2762), ("claude-fable-5-1", "summary_chars", 8342)]:
    f = f"results_thk1_moy5_20261030_{mod}.jsonl"
    add("median", f"thk1 {mod} {field}", f"thk1 {mod} · {field} = **{want:,}** (one row · R2 one-reader item kept · token vs characters = decision ⑩)", f"`ConstructGap/exp/{f}` · {field}", "26", files=[f], model=mod, raw_only=False, median=field, expect=want)
TXT = [(res_of("olm72"), "語が残らない行の 113 / 118 は", "olm72: 113 of the 118 rows without a word have a formula-only cut sentence (RESULT olm72's diagnosis; the 118 is recounted from read.json)", "25"),
       (res_of("olm82"), "Q1a S1 の t+1 で最終層の分布が集まる", "olm82 Q1a ✗ (R3 one-reader item kept)", "25"),
       (res_of("olm82"), "解けない(凍結の解ける条件のとおり)", "olm82 L3 cannot be resolved", "25"),
       (res_of("olm80"), "入れ替えた零の AUC₃₂ = 中央値 0.522・5〜95 % 点 0.248〜0.739(線 ≤ 0.60 ✗)", "olm80 C2: median 0.522, 95 % point 0.739, the line ≤ 0.60 on the 95 % point (decision ⑨)", "26"),
       (res_of("olm74"), "**192 / 288 = 0.667**・中央値 +0.052・p **8.1e−9**", "olm74 Q2: 192 / 288 = O rows with d > 0 against the same row's pseudo event; +0.052 = the median of d (decision ⑧)", "25"),
       (res_of("olm74"), "L **−0.040** 対 O **+0.052**", "olm74 Q3: the same +0.052 is O's median d, compared with L (decision ⑧)", "25"),
       (SCOPE, "15 / 19(p 0.0096・Sonnet rc03)", "olm74: by card × model 15 / 19, p 0.0096 (G-06)", "25, 30"),
       (SCOPE, "Opus だけでは 33〜64 が p 0.052(プールだけ ✓・Sonnet L2-2)", "olm68: Q1 ✓ pooled only, Opus alone p 0.052 (G-13)", "25"),
       (SCOPE, "Q2 Opus 36 / 53(通る最小の上 3 行)", "olm81: Opus 36 / 53 = 3 rows above the smallest pass (G-14)", "25"),
       (SCOPE, "補助定理の腕の弱さは Opus と Fable で割れる(行ごとの d: Opus の L +0.022・Fable の L −0.139)", "olm74: the lemma arms' weakness splits by model (G-15)", "25"),
       (SCOPE, "ただし **Fable では cut +0.744 / 床 +0.227 で分ける**", "olm67: Fable separates cut and floor (G-01)", "24"),
       (SCOPE, "その寄りの過半は窓の語の積み上がり", "olm78: 'most of it is the words piling up' = SCOPE's wording, put at L3 (G-07 · D3 ⑥)", "25, 30"),
       (SCOPE, "新しい行(CLI 2.1.314・11 月・A/Q2 n 47)では検出できなかった", "SCOPE's 11-07 note on the main verdict (thk3 Q2 ✗)", "30"),
       (SCOPE, "自分の語の計器(olm69〜73・79 = 6 札)", "the own-word instruments closed (SCOPE §4 · D3 ③ title)", "25"),
       (SCOPE, "先読みは句の幅(2 token 前 75 %・3 token 前 21 % = 乱数の 95 % 点の 3 倍だが関門 30 % 未満)", "olm67 Q2: 2 tokens before 75 % is post hoc (D3 ①)", "24"),
       (SCOPE, "「床の文の手前と比べて」は外向けに使わない", "olm67 Q3 / olm68: not for outside use (G-04 · G-05)", "24, 25"),
       (SCOPE, "olm68 Q1 は **cut の行 対 床の行**の比べ", "olm68: the 10-31 correction (G-05)", "25"),
       (SCOPE, "Opus・Fable の**中の**状態・思考の本文(API は生の思考を返さない = MEMO p21)・因果", "the inner state is not said (D3 ⑤ · G-10)", "29, 30"),
       ("conversations/2026-11-06/coread_station2_3/station3_moy5/BRIEF_v2_1_moy5_received_version_one_maker_20261107.md", "**束 ① に「家が打つ」の印を付ける**", "bundle ① carries 'the house fires it' (PI 11-07 F4 = C7)", "27"),
       ("conversations/2026-11-06/coread_station2_3/station3_moy5/RESULT_station3_moy5_next_visible_two_maker_variation_20261106.md", "③ 点の集合 × 足した文(Q1 の {E, J, K, P_y} と Q2 の {F, V, P_x, P_y})= 5 問", "bundle ③ in the RESULT's words (D3_R2 D-19)", "27")]
for f, lit, what, st in TXT:
    add("text_contains", what[:60], what, f"`{f}`", st, file=f, literal=lit)
for q in P["n4"]["quotes"]:
    f = "conversations/2026-11-06/coread_station2_3/" + q["file"]
    add("text_contains", f"N4 quote {q['file']} {q['qn']}", f"bundle example (reader's verbatim) {q['file'].split('/')[-2]} {q['qn']}: «{q['quote'][:48]}…»", f"`{f}`", "27", file=f, literal=q["quote"])

(HERE / "claims_anchors.json").write_text(json.dumps(A, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
out = ["# CLAIMS_v21 — what v2.1 moved, decided and fixed (BRIEF v2.1 §2-2〜§2-7 · 2026-11-07)", "",
       "Each row has one anchor in `claims_anchors.json` (`check_claims.py` looks at the place itself: the card's json / jsonl, SCOPE 10-31, a RESULT, a PREREG). Written by `make_anchors_v21.py` (never by hand).",
       "The grade of each card is recomputed by `check_claims.py` from SCOPE 10-31 (rule i) or the card's RESULT line (rule ii), apart from `pack_data.py`.", "",
       "| id | claim (value as the figure prints it) | source (file · key) | level | state |", "|---|---|---|---|---|"]
out += [f"| {i} | {c} | {s} | {lv} | {st} |" for i, c, s, lv, st in rows]
(HERE / "CLAIMS_v21.md").write_text("\n".join(out) + "\n", encoding="utf-8")
# G-26: the grade words of K250–K269 in CLAIMS_after.md follow the rule (the freeze-commit anchors stay)
ca = (HERE / "CLAIMS_after.md").read_text(encoding="utf-8")
for cid, p in POST.items():
    ca = re.sub(rf"(\| {cid} · frozen at «{p['freeze']}» · )status \w+ · grade [^|]+\|", lambda m: f"{m[1]}grade **{p['grade5']}** (rule {p['rule']} · v2.1) |", ca)
ca = ca.replace("Status = verdict / gate / desc (pack_data.py `post`); grade = SCOPE 10-31 §1 where it lists the card.",
                "v2.1 (G-26): the grade of each card follows the requester's rule (BRIEF v2.1 §2-5): (i) the tier of SCOPE 10-31 §1 / §2 where the card is named, (ii) otherwise the tier criteria applied to its RESULT; five columns 判定 / 記述 / 較正 / 言えない / 関門で止まった, sum 20 (anchors in CLAIMS_v21.md).")
(HERE / "CLAIMS_after.md").write_text(ca, encoding="utf-8")
print(f"anchors: {len(A)} ({len(rows)} v2.1) · CLAIMS_v21.md {len(rows)} rows")
