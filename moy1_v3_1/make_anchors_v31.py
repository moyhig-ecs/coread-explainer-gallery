"""make_anchors_v31.py — the anchors of v3.1 (BRIEF v3.1 §2-5 / §2-6 / §2-7): the decisions made from the data and the audit's fixes, each tied to a frozen file
(or to this folder's config / the build's derivation). Added under existing claim ids (base K\\d+), with the suffix "v31x" so that make_anchors_v3.py's ids are not touched.
    python3 -I make_anchors_v31.py        (idempotent: it removes the anchors whose id contains "v31" first; run it after make_anchors_v3.py)
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
A = [a for a in json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8")) if "v31" not in a["id"]]
n = {}


def add(base, kind, **kw):
    n[base] = n.get(base, 0) + 1
    A.append({"id": f"{base}v31{chr(96 + n[base])}", "kind": kind, **kw})


SCOPE = "conversations/2026-11-01/SCOPE_line1_inference_space_after_olm83_92_20261101.md"
# card marks (§2-5): config.json card_marks = the marks the build derived from what each state reads (generated/marks_derived.json has no difference)
add("K43", "here_json_equals", file="generated/marks_derived.json", key="differences", expect=[], note="v3.1: build.mjs derives every state's marks from the DATA paths it reads (entry P's rule); no difference with config.json")
for s, marks in ((8, ["pc1", "cmt5"]), (11, ["pc1", "screen_bf16"]), (18, ["replication_config_frozen", "olm59", "olm7", "olm4"]), (21, ["olm59", "olm7", "olm4", "olm62"])):
    add("K43", "here_json_equals", file="config.json", key=f"card_marks.{s}", expect=marks, note=f"v3.1: state {s} (8 + cmt5 · 11 without the card after 10-28 · 18-20 + the frozen coordinates · 21 + olm62)")
# s17 (§2-6): base open by the frozen rule = the primary denominator without the row cut at the cap (PREREG pc1 §6), all rows listed beside it
add("K64", "repo_text_contains", file="conversations/2026-07-30/PREREG_pc1_cue_invariance_20260730.md", literal="**primary 分母から除外 + 全行込みを並記**", note="v3.1: the rule for a row cut at the cap (base side)")
add("K64", "derived", name="base", args=["open"], expect={"labels": {"B-attractor": 5, "B-stuck-L1": 5}, "cap": 1, "labels_no_cap": {"B-attractor": 4, "B-stuck-L1": 5}}, note="v3.1: base open = attractor 4 · stuck-L1 5 (primary) · all rows attractor 5 / 10")
# s18 (§2-6): k −20 is the token " the" that opens "the midpoint of ..."; " midpoint" is k −19 (recounted from the npz)
add("K66", "pack_equals", key="olm59.S_O.wordcirc.k_the", expect=-20, note="v3.1: ' the' before 'midpoint' = k −20 (entry P's k)")
add("K66", "pack_equals", key="olm59.S_O.wordcirc.k_phrase", expect=-19, note="v3.1: ' midpoint' = k −19 (entry Q's k)")
# olm76's commits (§2-6): frozen b7730f55, re-frozen d7fbbd43 before reading (the output conversion only)
add("K50", "repo_text_contains", file="conversations/2026-10-30/RESULT_olm76_moy1_commit_window_before_answer_brace_20261030.md", literal="(b7730f55 → 凍結し直し d7fbbd43 = 出力の変換だけ・読みの前)", note="v3.1: both commits of olm76")
# the cards stopped at a control / gate that the pack does not read (the counting rule of §2-5)
for f, lit in (("conversations/2026-10-31/RESULT_olm83_moy1_inference_space_lookahead_beyond_lens_and_words_20261031.md", "凍結 c05ce44d"), ("conversations/2026-10-31/RESULT_olm83_moy1_inference_space_lookahead_beyond_lens_and_words_20261031.md", "統制 C1 ✗"),
               ("conversations/2026-10-31/RESULT_olm88_moy1_inference_space_outcome_from_first_tokens_20261031.md", "凍結 d7eba25d"), ("conversations/2026-10-31/RESULT_olm88_moy1_inference_space_outcome_from_first_tokens_20261031.md", "入口の関門 ✗"),
               (SCOPE, "olm83 = 統制 ✗ で読んでいない。"), (SCOPE, "olm88 = 入口の関門 ✗ で読んでいない。")):
    add("K50", "repo_text_contains", file=f, literal=lit, note="v3.1: a card stopped at a control / gate (counted apart)")
# G-01 / G-02 (olm76): "does not reach the line" (SCOPE 11-01's words) · the attractor median to 4 digits vs SCOPE's +0.043
add("K51", "repo_text_contains", file=SCOPE, literal="結びの群は bind の行で線に届かない(28 / 48・+0.013・p 0.156)", note="v3.1 G-01: SCOPE 11-01's words")
add("K51", "repo_json_close", file="ConstructGap/exp/olm76/read.json", key="Q3_close_bind_gt_attractor.median_b", expect=0.0425, tol=0.00005, note="v3.1 G-02: attractor median +0.0425 (3 digits +0.042)")
add("K51", "repo_text_contains", file=SCOPE, literal="+0.013 対 +0.043", note="v3.1 G-02: what SCOPE 11-01 prints")
# G-03 + §2-5 (olm89 / olm92): +0.02 was set after seeing olm86; the frozen false condition is +0.01
add("K53", "repo_text_contains", file=SCOPE, literal="**線 +0.02 は olm86 の値を見てから置いた「確かめの線」**(PREREG olm89 §0)", note="v3.1 G-03: the +0.02 line is after the fact")
add("K53", "repo_text_contains", file=SCOPE, literal="偽の条件 = L32・L48 とも E の中央値 ≤ +0.01", note="v3.1 §2-5: the frozen line of the judgment")
# G-04: k = 16 of olm86 vanishes on 400 rows
add("K53", "repo_text_contains", file=SCOPE, literal="一貫して出るのは、k = 8 の薄い上乗せだけ", note="v3.1 G-04")
# G-11: the 8 / 53 of R04
add("K25", "repo_json_equals", file="ConstructGap/exp/olm59/read.json", key="Q3_desc.o_diam|close|B-bind.after_gt_before", expect=8, note="v3.1 G-11: after > before in 8 of the bind rows")
add("K25", "repo_json_equals", file="ConstructGap/exp/olm59/read.json", key="Q3_desc.o_diam|close|B-bind.n", expect=53, note="v3.1 G-11: of 53 bind rows")
# G-12 (prf4 = another card, a chat model, the same sentence)
add("K59", "repo_json_equals", file="ConstructGap/exp/prf4/read.json", key="units.claude-opus-5-5|M1A.chain_in_bind", expect=8, note="v3.1 G-12: prf4 Opus 5.5 chain in bind rows")
add("K59", "repo_json_equals", file="ConstructGap/exp/prf4/read.json", key="units.claude-opus-5-5|M1A.bind", expect=8, note="v3.1 G-12: prf4 Opus 5.5 bind rows")
add("K59", "pack_equals", key="after.apex.prf4.chain", expect=8, note="v3.1: the page carries the same")
# G-13 (olm114 k = 0: the gate G2 is B-bind 5 < 8; the 18 rows cut at the cap are another number)
add("K59", "repo_text_contains", file="conversations/2026-11-02/RESULT_olm114_moy1_frontier_proof_prefix_ladder_20261102.md", literal="| G2(k = 0) | label の無い行 ≤ 4 **かつ** 答えの欄 B-bind ≥ 8 | label なし 0 ✓・**B-bind 5** ✗ | **✗ → Q3 を読まない** |", note="v3.1 G-13: the gate's reason")
add("K59", "repo_json_equals", file="ConstructGap/exp/olm114/read.json", key="Q3.hit_cap", expect=18, note="v3.1 G-13: the rows cut at the cap (not the gate's reason)")
# s10 (D1 E): the order He -> O is in 3 of the 7 bind rows; 4 have both sentences
add("K09", "pack_equals", key="order_he_first", expect={"0": "O", "2": "He", "7": "He", "8": "He"}, note="v3.1: He first in 3 (s2 · s7 · s8) · O first in 1 (s0) · 4 rows with both")
(HERE / "claims_anchors.json").write_text(json.dumps(A, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"claims_anchors.json: {len(A)} anchors ({sum(n.values())} written by make_anchors_v31.py) · {n}")
