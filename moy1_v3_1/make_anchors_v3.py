"""make_anchors_v3.py — writes the anchors of v3 (K43 rewritten for 43 states; K50-K69 new; K06c / K09a changed by decision 1) into claims_anchors.json, once.
An anchor = a place in a frozen file (or a recount by check_claims.py's own code) and the value the figure says. The expected values here are typed from the RESULT / SCOPE lines (rounded as printed; `tol` = the rounding)
or recounted by check_claims.py from the raw rows; they are never read back from the pack. The pack's own copy is looked at by pack_equals_json / pack_close_derived anchors.
    python3 -I make_anchors_v3.py        (idempotent: it removes the anchors of the ids it writes first)
"""
import json
import pathlib
import string

HERE = pathlib.Path(__file__).resolve().parent
A = json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8"))
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
pack = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
NEW_BASES = {f"K{n}" for n in range(50, 70)} | {"K43"}
A = [a for a in A if a["id"][:3] not in NEW_BASES and a["id"][:3] != "K43"]
for a in A:                                                    # decision 1: blocked s8 has no answer field
    if a["id"] == "K06c":
        a["expect"] = 6
        a["note"] = "v3: blocked's answer field is O1O2 in 6 rows (s8 has no JSON: no answer field)"
    if a["id"] == "K09a":
        a["expect"] = {"0": "o1o2", "2": "o1o2", "3": "hehi", "7": "o1o2", "8": "other"}
        a["note"] = "v3: s8 has no answer field (v2 read its last paragraph as o1o2)"
out = []
cnt = {}


def add(base, kind, **kw):
    cnt[base] = cnt.get(base, 0) + 1
    i = cnt[base] - 1
    sfx = (string.ascii_lowercase + string.ascii_uppercase)[i] if i < 52 else f"x{i}"
    out.append({"id": f"{base}{sfx}", "kind": kind, **kw})


RJ = lambda c, f="read.json": f"ConstructGap/exp/{c}/{f}"
J = lambda base, file, key, expect, note=None: add(base, "repo_json_equals", file=file, key=key, expect=expect, **({"note": note} if note else {}))
C = lambda base, file, key, expect, tol, note=None: add(base, "repo_json_close", file=file, key=key, expect=expect, tol=tol, **({"note": note} if note else {}))
PJ = lambda base, pkey, file, jkey, note=None: add(base, "pack_equals_json", file=file, key=pkey, jkey=jkey, **({"note": note} if note else {}))
D = lambda base, name, args, expect, note=None: add(base, "derived", name=name, args=args, expect=expect, **({"note": note} if note else {}))
DC = lambda base, name, args, expect, tol, pick=None, note=None: add(base, "derived_close", name=name, args=args, expect=expect, tol=tol, **({"pick": pick} if pick is not None else {}), **({"note": note} if note else {}))
PCD = lambda base, name, args, pkey, tol, pick=None, note=None: add(base, "pack_close_derived", name=name, args=args, file="generated/pack.json", key=pkey, tol=tol, **({"pick": pick} if pick is not None else {}), **({"note": note} if note else {}))
T = lambda base, file, literal, note=None: add(base, "repo_text_contains", file=file, literal=literal, **({"note": note} if note else {}))
PE = lambda base, pkey, expect, note=None: add(base, "pack_equals", file="generated/pack.json", key=pkey, expect=expect, **({"note": note} if note else {}))
SCOPE = "conversations/2026-11-01/SCOPE_line1_inference_space_after_olm83_92_20261101.md"
RES = {"olm76": "conversations/2026-10-30/RESULT_olm76_moy1_commit_window_before_answer_brace_20261030.md", "olm95": "conversations/2026-11-01/RESULT_olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.md",
       "olm101": "conversations/2026-11-01/RESULT_olm101_moy1_pointer_or_value_at_final_position_interchange_das_20261101.md", "olm106": "conversations/2026-11-01/RESULT_olm106_moy1_single_position_interchange_sel_ctl_dem_early_layers_20261101.md",
       "olm108": "conversations/2026-11-01/RESULT_olm108_moy1_multi_position_interchange_pointer_to_value_layers_12_32_20261101.md", "olm112": "conversations/2026-11-02/RESULT_olm112_moy1_apex_status_and_geometric_proof_20261102.md",
       "olm114": "conversations/2026-11-02/RESULT_olm114_moy1_frontier_proof_prefix_ladder_20261102.md", "olm128": "conversations/2026-11-06/RESULT_olm128_moy1_cue_json_start_blocked_bind_20261106.md"}

# ---- K43 (rewritten): the card marks of every state = config.json's list, and the rule of the marks (the cards of the data a state draws) gives the same set
for n, marks in enumerate(cfg["card_marks"]):
    add("K43", "here_json_equals", file="config.json", key=f"card_marks.{n}", expect=marks, note=f"state {n}: the cards whose data it draws")
for n, marks in enumerate(cfg["card_marks"]):
    add("K43", "derived", name="marks_rule", args=[n], expect=sorted(marks), note=f"state {n}: the marks by the rule (config.json state_data -> card_of_data)")

# ---- K50: the cards were frozen before they were read (the commit that first added the PREREG = the RESULT's freeze) and the grade words come from the SCOPE / the RESULTs
for c in pack["after"]["cards"]:
    D("K50", "freeze", [c["id"]], c["freeze"], f"{c['id']}: git's first commit of its PREREG")
T("K50", SCOPE, "olm89 Q1 ✓(olm87 の 107 行", "確かめた記述: olm89")
T("K50", SCOPE, "olm92 Q1 の枝「残る」", "確かめた記述: olm92")
T("K50", SCOPE, "olm94 Q2 ✓(", "判定: olm94")
T("K50", SCOPE, "olm98 Q1 ✓(", "判定: olm98")
T("K50", SCOPE, "olm76 Q1 ✗・Q3 ✗", "記述: olm76")
T("K50", RES["olm101"], "0 個(Q1 = 偽・Q2 = 片方なし・Q3 = 間", "olm101: no claim moved")
T("K50", RES["olm106"], "0 個(Q1 遅い・Q2 無い・Q3 無い)", "olm106: no claim moved")
T("K50", RES["olm108"], "2 つ(新しい判定", "olm108: two claims moved")
T("K50", RES["olm95"], "統制 C2 ✗ = 読まない", "olm95: not read")

# ---- K51: olm76
f76, c76 = RJ("olm76"), RJ("olm76", "control.json")
J("K51", f76, "Q1_bind_close_rises.pos", 28); J("K51", f76, "Q1_bind_close_rises.n", 48); J("K51", f76, "Q1_bind_close_rises.pass", False)
C("K51", f76, "Q1_bind_close_rises.median", 0.0127, 6e-5); C("K51", f76, "Q1_bind_close_rises.sign_p", 0.156, 6e-4)
J("K51", c76, "C2_pseudo_window.sae_close.pos", 21); C("K51", c76, "C2_pseudo_window.sae_close.sign_p", 0.844, 6e-4)
J("K51", f76, "desc_all_keys.sae_close|attractor.pos", 7); C("K51", f76, "desc_all_keys.sae_close|attractor.median", 0.0425, 6e-5)
C("K51", f76, "Q3_close_bind_gt_attractor.diff", -0.0298, 6e-5); C("K51", f76, "Q3_close_bind_gt_attractor.perm_p", 0.834, 6e-4); J("K51", f76, "Q3_close_bind_gt_attractor.pass", False)
J("K51", c76, "C3_commit_positive.pos", 14); J("K51", c76, "C3_commit_positive.n", 18); J("K51", c76, "C3_commit_positive.ok", False)
PJ("K51", "after.l3.q1.pos", f76, "Q1_bind_close_rises.pos"); PJ("K51", "after.l3.q1.median", f76, "Q1_bind_close_rises.median"); PJ("K51", "after.l3.pseudo.pos", c76, "C2_pseudo_window.sae_close.pos"); PJ("K51", "after.l3.q3.perm_p", f76, "Q3_close_bind_gt_attractor.perm_p")

# ---- K52: olm84 / 85 / 86 (AUC of the layer-32 probe against the J-lens readout; E)
for card, key, i, v32, vj, e in (("olm84", "Q1", 0, 0.996, 0.994, 0.002), ("olm85", "Q1_next_sentence_O", 1, 0.878, 0.879, -0.002), ("olm86", "Q1_k32", 2, 0.777, 0.775, 0.002)):
    f = RJ(card)
    C("K52", f, f"{key}.auc.L32.median", v32, 6e-4); C("K52", f, f"{key}.auc.J.median", vj, 6e-4); C("K52", f, f"{key}.E.L32.median", e, 7e-4); J("K52", f, f"{key}.pass", False)
    PJ("K52", f"after.space.look.{i}.auc.L32.med", f, f"{key}.auc.L32.median"); PJ("K52", f"after.space.look.{i}.auc.J.med", f, f"{key}.auc.J.median")

# ---- K53: E at k = 8 and the olm92 E+
C("K53", RJ("olm86"), "Q2_desc_by_k.8.E.L32.median", 0.036, 6e-4); C("K53", RJ("olm86"), "Q2_desc_by_k.8.E.L48.median", 0.033, 6e-4)
C("K53", RJ("olm89"), "Q1_k8.E.L32.median", 0.041, 6e-4); C("K53", RJ("olm89"), "Q1_k8.E.L48.median", 0.031, 6e-4); J("K53", RJ("olm89"), "Q1_k8.Q1_repl_pass", True); J("K53", RJ("olm89"), "Q1_k8.Q1b_line_pass", False)
C("K53", RJ("olm92"), "Q_k8.E_old.L32.median", 0.022, 6e-4); C("K53", RJ("olm92"), "Q_k8.E_old.L48.median", 0.018, 6e-4)
C("K53", RJ("olm92"), "Q_k8.E_plus.L32.median", 0.022, 6e-4); C("K53", RJ("olm92"), "Q_k8.E_plus.L32.p05", 0.005, 6e-4); C("K53", RJ("olm92"), "Q_k8.E_plus.L32.p95", 0.037, 6e-4); J("K53", RJ("olm92"), "Q_k8.Q1_branch", "残る")
PJ("K53", "after.space.ktab.olm86.8.L32", RJ("olm86"), "Q2_desc_by_k.8.E.L32.median"); PJ("K53", "after.space.ktab.olm89.8.L32", RJ("olm89"), "Q1_k8.E.L32.median"); PJ("K53", "after.space.ktab.olm92.8.L32", RJ("olm92"), "Q_k8.E_old.L32.median"); PJ("K53", "after.space.plus.L32.med", RJ("olm92"), "Q_k8.E_plus.L32.median")
C("K53", RJ("olm89"), "Q2_desc_by_k.32.E.L48.median", 0.004, 6e-4); C("K53", RJ("olm86"), "Q1_k32.E.L48.median", -0.006, 6e-4)

# ---- K54: olm91
f91 = RJ("olm91")
C("K54", f91, "Q1_first64.auc.L32.median", 0.492, 6e-4); C("K54", f91, "Q1_first64.auc.L48.median", 0.489, 6e-4); C("K54", f91, "Q1_first64.auc.J.median", 0.527, 6e-4); C("K54", f91, "Q1_first64.auc.W.median", 0.578, 6e-4)
J("K54", f91, "Q1_first64.rows", 217); J("K54", f91, "Q1_first64.attractor", 51); C("K54", RJ("olm91", "control.json"), "C3_perm_null.auc.L32.p05", 0.366, 6e-4); C("K54", RJ("olm91", "control.json"), "C3_perm_null.auc.L32.p95", 0.601, 6e-4)
PJ("K54", "after.space.first64.auc.L32.med", f91, "Q1_first64.auc.L32.median"); PJ("K54", "after.space.first64.null.p95", RJ("olm91", "control.json"), "C3_perm_null.auc.L32.p95")

# ---- K55: olm94 / olm93
f94, f93 = RJ("olm94"), RJ("olm93")
for lay, v in (("L32", 0.970), ("L48", 0.766), ("J", 0.556)):
    C("K55", f94, f"Q2_V_post_to_dem_vs_ctl.to_dem.{lay}.median", v, 6e-4)
C("K55", f94, "Q2_V_post_to_dem_vs_ctl.to_dem.W.median", 0.5, 1e-9); C("K55", f94, "Q2_V_post_to_dem_vs_ctl.to_ctl.L32.median", 0.603, 6e-4); C("K55", f94, "Q2_V_post_to_dem_vs_ctl.to_ctl.L48.median", 0.601, 6e-4)
C("K55", f93, "Q1_name_to_dem.auc.L32.median", 0.870, 6e-4); C("K55", f93, "Q1_name_to_dem.auc.W.median", 0.946, 6e-4)
PJ("K55", "after.struct.ref.olm94_q2.to_dem.L32", f94, "Q2_V_post_to_dem_vs_ctl.to_dem.L32.median"); PJ("K55", "after.struct.ref.olm93_q1.W", f93, "Q1_name_to_dem.auc.W.median")

# ---- K56: olm98
f98 = RJ("olm98")
C("K56", f98, "Q1_top_heads_read_ref_name.ratio_median", 2.37, 6e-3); C("K56", f98, "Q1_top_heads_read_ref_name.share_by_span_median.ref_name", 0.350, 6e-4); C("K56", f98, "Q1_top_heads_read_ref_name.share_by_span_median.oth_name", 0.148, 6e-4)
C("K56", f98, "Q2_patch_top_heads.e_top_median", 2.19, 6e-3); C("K56", f98, "Q2_patch_top_heads.top_minus_rand_median", 2.11, 6e-3); C("K56", f98, "Q2_patch_top_heads.flip_top", 0.513, 6e-4)
J("K56", f98, "Q4_cmt13_overlap", ["L50H23", "L51H19", "L51H4", "L52H26", "L57H33"]); J("K56", f98, "Q5_head_reading_dem_most.head", "L13H30"); J("K56", f98, "Q5_head_reading_dem_most.rank_by_dla", 312)
PJ("K56", "after.struct.heads.ratio", f98, "Q1_top_heads_read_ref_name.ratio_median"); PJ("K56", "after.struct.heads.flip", f98, "Q2_patch_top_heads.flip_top")

# ---- K57: olm101 / olm106 / olm108 (layers)
f101, f106, f108 = RJ("olm101"), RJ("olm106"), RJ("olm108")
C("K57", f106, "table.sel_L12.test・ptr_only", 0.929, 6e-4); C("K57", f106, "table.sel_L16.test・ptr_only", 0.339, 6e-4); C("K57", f106, "table.sel_L20.test・ptr_only", 0.013, 6e-4); J("K57", f106, "Q1.L_drop", 16)
J("K57", f101, "Q1_curve_full_end.4.L", 24); C("K57", f101, "Q1_curve_full_end.4.F_vo", 0.381, 6e-4); J("K57", f101, "Q1_curve_full_end.5.L", 28); C("K57", f101, "Q1_curve_full_end.5.F_vo", 0.990, 6e-4); J("K57", f101, "Q2.L_val_first", 28)
J("K57", f108, "Q1.curve_tail.4.0", 20); C("K57", f108, "Q1.curve_tail.4.1", 0.432, 6e-4); C("K57", f108, "Q1.curve_tail.4.2", 0.552, 6e-4); J("K57", f108, "Q1.L_switch_tail", 20); J("K57", f108, "Q3.scattered_layers", [16, 18])
PJ("K57", "after.struct.layers.sel_drop", f106, "Q1.L_drop"); PJ("K57", "after.struct.layers.end_val_first", f101, "Q2.L_val_first"); PJ("K57", "after.struct.layers.tail_switch", f108, "Q1.L_switch_tail")
PJ("K57", "after.struct.layers.end.4.vo", f101, "Q1_curve_full_end.4.F_vo"); PJ("K57", "after.struct.layers.tail.4.po", f108, "Q1.curve_tail.4.1")

# ---- K58: olm112
f112 = RJ("olm112")
J("K58", f112, "Q1.chain", 0); J("K58", f112, "Q1.bind", 37); J("K58", f112, "Q1.verdict", "偽")
J("K58", f112, "Q2.bind_hyp", 36); J("K58", f112, "Q2.bind_hq", 36); J("K58", f112, "Q2.attr_hyp", 28); J("K58", f112, "Q2.attr_hq", 29); C("K58", f112, "Q3.new_rate", 0.300, 6e-4); C("K58", f112, "Q3.baseline_rate", 0.255, 6e-4)
for k, v in (("BIS", 1), ("RA", 4), ("THC", 13), ("CHAIN", 0), ("ALT_radical", 11), ("ALT_homothety", 9), ("ALT_power", 6)):
    J("K58", f112, f"Q4_by_label_json.B-bind.{k}", v)
T("K58", RES["olm112"], "**CHAIN を満たした証明 = 0 本**", "RESULT olm112 §4")
PJ("K58", "after.apex.olm112.bind.THC", f112, "Q4_by_label_json.B-bind.THC"); PJ("K58", "after.apex.olm112.Q1.chain", f112, "Q1.chain")

# ---- K59: olm114
f114 = RJ("olm114")
J("K59", f114, "Q1.RA_and_THC", 26); J("K59", f114, "Q1.k1_rows", 40); J("K59", f114, "Q2.THC", 23); J("K59", f114, "Q2.k2_rows", 40); J("K59", f114, "Q3.bind", 5); J("K59", f114, "Q3.k0_rows", 40); J("K59", f114, "Q3.verdict", None)
J("K59", f114, "Q1.by_family.opus.RA_and_THC", 12); J("K59", f114, "Q1.by_family.fable.RA_and_THC", 14); J("K59", f114, "Q2.by_family.opus.THC", 7); J("K59", f114, "Q2.by_family.fable.THC", 16); J("K59", f114, "gates.G2_k0_none<=4", True)
T("K59", RES["olm114"], "k = 1 の続き 40 本のうち 12(満たした 26 のうち 7・満たさなかった 14 のうち 5)", "the 12 / 40 the figure cites: the executing layer's regex, outside the instrument (RESULT §5)")
PJ("K59", "after.apex.olm114.Q1.RA_and_THC", f114, "Q1.RA_and_THC"); PJ("K59", "after.apex.olm114.Q2.THC", f114, "Q2.THC")

# ---- K60 / K61: olm128 (the card's own file; the cells recounted from the raw rows)
f128 = RJ("olm128")
for k, rk, exp in (("nl", "nl", {"n": 9, "json": 7, "text": 2, "bind": 2, "json_bind": 1, "text_bind": 1, "early": 8, "early_bind": 2, "late": 1, "late_bind": 0}),
                   ("sp", "space", {"n": 10, "json": 0, "text": 10, "bind": 4, "json_bind": 0, "text_bind": 4, "early": 7, "early_bind": 2, "late": 3, "late_bind": 2}),
                   ("nn", "nlnl", {"n": 10, "json": 3, "text": 7, "bind": 7, "json_bind": 0, "text_bind": 7, "early": 3, "early_bind": 0, "late": 7, "late_bind": 7})):
    D("K60", "cue_start", [k], exp, f"cue {k}: blocked rows (cap rows removed) recounted from the raw rows: the start at position 0 and the post-hoc 100-character description")
    for key in ("n", "json", "text", "bind", "json_bind", "text_bind"):
        J("K60", f128, f"blocked_cells.{rk}.{key}", exp[key])
C("K60", f128, "verdicts.Q1_concordance", 0.579, 6e-4); J("K60", f128, "verdicts.Q1", "保たれない"); J("K60", f128, "verdicts.Q1_N", 19); C("K60", f128, "verdicts.Q2_nl_diff", 0.478, 6e-4); C("K60", f128, "verdicts.Q2_space_diff", -0.30, 6e-4)
J("K60", f128, "verdicts.Q2_nl", "動く(説明の向き)"); J("K60", f128, "verdicts.Q2_space", "逆"); J("K60", f128, "verdicts.Q3", "書き始めでは説明されない"); J("K60", f128, "verdicts.gates.C0_nlnl_reproduces_K11", True)
PJ("K60", "after.next.verdicts.Q1_concordance", f128, "verdicts.Q1_concordance"); PJ("K60", "after.next.cells.space.json", f128, "blocked_cells.space.json")
T("K61", RES["olm128"], "(25〜84 字目に 7 行)", "RESULT olm128 §0: the first JSON of cue \" \" sits at 25-84 characters in 7 rows")
D("K61", "cue_first", ["space"], pack["cue_start"]["space_first"], "the first {\"conjecture\" positions of cue \" \" (blocked, cap rows removed) recounted from the raw rows")
PCD("K61", "cue_start", ["sp"], "cue_start.early.sp.early", 0, pick="early")
PCD("K61", "cue_start", ["nl"], "cue_start.early.nl.early_bind", 0, pick="early_bind")
T("K61", RES["olm128"], "早い 8 / 9(bind 2)", "RESULT olm128 §3: the post-hoc description (not a verdict)")

# ---- K62: the angles (a different formula: atan2 of the cross and the dot)
for k in (1, 2, 3, 4):
    DC("K62", "angle", ["O", k], 90.0, 0.001, note=f"X{k}: the angle O1 X{k} O2")
    PCD("K62", "angle", ["O", k], f"geometry.ang_O.{k - 1}", 1e-9)
    PCD("K62", "angle", ["H", k], f"geometry.ang_H.{k - 1}", 1e-9)
DC("K62", "angle", ["H", 1], pack["geometry"]["ang_H"][0], 1e-6, note="the angle He X1 Hi is not 90 degrees")

# ---- K63: the F5 edit and the cue
D("K63", "f5", ["edit"], [1, "Respond with JSON only:", "First write your reasoning as plain text."]); D("K63", "f5", ["cue"], ["\n\n", "\n\n", "blocked", "blocked"])
PE("K63", "f5.edit.key", "Respond with JSON only:"); PE("K63", "f5.cue.F5a-2.cue", "\n\n")

# ---- K64: the base model's rows beside Think
D("K64", "base", ["open"], {"labels": {"B-attractor": 5, "B-stuck-L1": 5}, "cap": 1, "labels_no_cap": {"B-attractor": 4, "B-stuck-L1": 5}}); D("K64", "base", ["blocked"], {"labels": {"B-bind": 7, "B-attractor": 3}, "cap": 0, "labels_no_cap": {"B-bind": 7, "B-attractor": 3}})
PCD("K64", "base", ["open"], "think.base.open.labels", 0, pick="labels"); PCD("K64", "base", ["blocked"], "think.base.blocked.labels", 0, pick="labels"); PCD("K64", "base", ["open"], "think.base.open.cap", 0, pick="cap")

# ---- K65: the path x label of the event rows (the pack's by_kind against the recount)
D("K65", "bykind", ["o_diam"], {"answer|B-bind": 1, "answer|B-stuck-L1": 2, "natural|B-attractor": 2, "natural|B-bind": 16, "natural|B-flail": 1, "think|B-attractor": 1, "think|B-bind": 36})
D("K65", "bykind", ["h_diam"], {"answer|B-attractor": 1, "natural|B-attractor": 6, "natural|B-bind": 6, "think|B-attractor": 4, "think|B-bind": 17})
add("K65", "pack_equals_derived", name="bykind", args=["o_diam"], file="generated/pack.json", key="olm59.agg.o_diam.by_kind"); add("K65", "pack_equals_derived", name="bykind", args=["h_diam"], file="generated/pack.json", key="olm59.agg.h_diam.by_kind")
D("K65", "forced", [], {"F5a-2|natural": None, "F5a-2|think": "Okay", "F5a-2|answer": '{"', "F5b-1|natural": None, "F5b-1|think": "Okay", "F5b-1|answer": '{"'}, "what each path fixes as the first token (cmt5.json)")
for ev in ("o_diam", "h_diam"):
    PCD("K65", "slopes", [ev], f"olm59.slopes.{ev}", 1.1e-5, note=f"the row-by-row slopes of {ev}: the pack's against a recount with a separate loader (cumulative sums)")

# ---- K66: the sentence that says the circle in words
D("K66", "wordcirc", [], [1, 297, 323, 310, -19, 329], "[the sentence occurs once, first token, last token, the phrase's token, the phrase's distance from the event, the event token]")
PE("K66", "olm59.S_O.wordcirc.tok_a", 297); PE("K66", "olm59.S_O.wordcirc.k_phrase", -19)

# ---- K67: ties averaged (a number outside the card)
DC("K67", "o62_tie", ["o_diam"], 0.7809, 6e-5); DC("K67", "o62_tie", ["h_diam"], 0.2212, 6e-5); DC("K67", "o62_tie", ["pooled"], 0.4891, 6e-5)
for k in ("o_diam", "h_diam", "pooled"):
    PCD("K67", "o62_tie", [k], f"olm62.tie.{k}", 1e-9)

# ---- K68: olm62's Q2 holds two rules
D("K68", "olm62_q2_rule", [], [True], "the PREREG's Q2 sentence: fewer than 8 events = not read")
J("K68", RJ("olm62"), "o_diam.mid_up_when_math_flat", "7 / 11")
T("K68", "conversations/2026-10-28/PREREG_olm62_moy1_mid_rise_vs_math_shift_20261028.md", "8 本未満なら「読まない」", "olm62's Q2: the reading condition")

# ---- K69: decision 1 (blocked s8)
for k, v in (("o1o2", 6), ("hehi", 3), ("other", 1), ("bare", 0)):
    D("K69", "reading_count", ["blocked", k], v, "the answer field = the last JSON's conjecture; a row without JSON has none")
D("K69", "nojson_cmt5", [], {"n": 3, "label_json_fields": {"B-flail": 3}, "label_full": {"B-attractor": 2, "B-bind": 1}}, "cmt5: the rows without a JSON object carry label_json_fields = B-flail")
PE("K69", "cmt5.noJson.n", 3); PE("K69", "blk_cnt.o1o2", 6)

A += out
(HERE / "claims_anchors.json").write_text(json.dumps(A, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"claims_anchors.json: {len(A)} anchors ({len(out)} written by make_anchors_v3.py) · per base id {dict(sorted(cnt.items()))}")
