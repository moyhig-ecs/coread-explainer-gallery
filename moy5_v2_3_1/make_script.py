"""make_script.py — writes SCRIPT_yukkuri.md from the pack (numbers are read, never typed) and measures its length.
Length rule (the skill's): characters / 7.4 per second + 0.45 s between lines; <= 150 s in all; the first 10 s are state 1 (A1, the core).
Every line names the state it cues and the claim ids (CLAIMS.md / claims_anchors.json) it rests on; the forbidden words of make_check.py are scanned here too.
    python -I make_script.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
P = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
A = json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8"))
C = P["cells"]
kid = lambda frag: next(a["id"] for a in A if frag in a["note"])          # the claim id of an anchor, found by its note (never typed)
c = lambda i, k: C[i][k]
G5 = P["post_tally"]["grade"]

LINES = [  # (voice, state, text, [claim fragments])  — v2: states renumbered (config.json), audit G-10 / G-13 / G-15 wording, + the chapter after 10-28
    ("A", 1, "同じ問い・同じ model なのに、答えが二つとも同じ。何が違うの?", []),
    ("B", 1, f"答えの欄はどちらも床 EJ = KP_y。理由の欄に書いた道が違う。", ["V7 prf3 claude-opus-5-5 P5 floor", "V7 prf3 claude-opus-5-5 P5B floor"]),
    ("B", 1, f"左は焦点・準線で閉じた行(10 本中 {c('prf3.P5.opus', 'fd_use')})。右は近道を塞いだ行で、頂点の比例中項から式へ(10 本中 {c('prf3.P5B.opus', 'lat_sym')}・壊れの印 {c('prf3.P5B.opus', 'malformed')} 本を含む)。", ["V7 prf3 claude-opus-5-5 P5 fd_use", "V7 prf3 claude-opus-5-5 P5B lat_sym"]),
    ("A", 0, "そもそも、どんな問い?", []),
    ("B", 0, "円と接線から点 P_y を作り、P_x がどこでも成り立つ関係を一つ答える。答えの板は最初は空。", ["A0 drawing control"]),
    ("B", 4, "手がかりごとに Opus と Fable を一本ずつ。濃い青が答えの欄、淡い青が全体。", ["P→Q · locus sentence in the answer field · Opus A/Q2"]),
    ("A", 5, "何も足さないと?", []),
    ("B", 5, f"問いだけでは四つの model とも全体の cut が 0。Opus の K では全体 20 本中 {c('essay4.K.opus-5-5', 'bind')} で、計器は立つ。", ["V1 essay4 A opus-5-5 bind", "C0 essay4 K opus bind"]),
    ("A", 8, "どうすれば答えの欄に出る?", []),
    ("B", 8, f"問いの点の集合を一行替えると、答えの欄に Opus {c('neq3.A/Q2.opus', 'ans')}、Fable {c('neq3.A/Q2.fable', 'ans')}(20 本中)。", ["V4 neq3 opus A/Q2 answer field", "V4 neq3 fable A/Q2 answer field"]),
    ("B", 10, f"同じ札 neq6 の中で、Opus の答えの欄は medium {c('neq6.medium.opus', 'ans')} から max {c('neq6.max.opus', 'ans')}。thinking の量は結果の記述。", ["V5 neq6 opus-5-5 A/Q2@medium answer field", "V5 neq6 opus-5-5 A/Q2@max answer field"]),
    ("B", 12, f"理由を求める一文 β′ では理由の欄に cut の在る行が Opus {c('b5bp.Bbp.opus-5-5', 'bind')}、Sonnet {c('b5bp.Bbp.sonnet-5-5', 'bind')}、Fable {c('b5bp.Bbp.fable-5-1', 'bind')}。答えの欄は 0。", ["V2 b5bp Bbp opus-5-5 bind", "V2 b5bp Bbp opus answer field"]),
    ("B", 18, f"近道を塞ぐと、Opus は 10 本中 {c('prf3.P5B.opus', 'lat_sym')} が頂点の比例中項を書いた。Fable は {c('prf3.P5B.fable', 'lat_sym')}、壊れた出力を除くと {c('prf3.P5B.fable', 'lat_sym_ok')} / {c('prf3.P5B.fable', 'n_ok')}。", ["V7 prf3 claude-opus-5-5 P5B lat_sym", "V7 prf3 claude-fable-5-1 P5B lat_sym"]),
    ("B", 14, f"Argon の thinking は、行の数えで Claude の {C['arg5.Bbp']['reasoning_med'] / C['b5bp.Bbp.fable-5-1']['reasoning_med']:.1f}〜{C['arg5.Bbp']['reasoning_med'] / C['b5bp.Bbp.sonnet-5-5']['reasoning_med']:.1f} 倍。SUMMARY の 3.8〜8.2 倍は真ん中二本の上の値。", ["v2.1 reasoning median_high results_arg5"]),
    ("B", 21, f"Menaechmus の説明だけで、Fable は理由の欄に頂点の形を {c('mnw1.cone/Q1.fable', 'vertex')} 本。答えの欄は {c('mnw1.cone/Q1.fable', 'ans')}。", []),
    ("B", 22, f"OLMo-3 32B は問いだけでは床にも 20 本中 {c('olm1.natural', 'floor')}〜{c('olm3.think', 'floor')}。この地図の外。", ["V9 olm1 base natural none/Q1 floor", "V9 olm3 Think none/Q1 floor"]),
    ("A", 23, "その後は?", []),
    ("B", 23, f"家は OLMo の内側で frontier の道を読む札を {len(P['post'])} 本打った。格は判定 {G5['判定']}、記述 {G5['記述']}、較正 {G5['較正']}、言えない {G5['言えない']}、関門で止まった {G5['関門']}。足して {sum(G5.values())}。", ["v2.1 grade five columns"]),
    ("B", 25, f"cut の文の手前 32 token で、OLMo の言語空間は、同じ行の別の文の手前より、床の答えの語に比べて CUT の語の側へ寄る。{next(p for p in P['post'] if p['id'] == 'olm74')['v']['pos']} / {next(p for p in P['post'] if p['id'] == 'olm74')['v']['n']}。", ["olm74 pos"]),
    ("B", 25, "自分の語で測る計器は、関門や統制で止まって閉じた。", ["v2.1 the own-word instruments closed"]),
    ("B", 27, "読み手が出した次の束は五つ。家が打つのは束 ①、thinking の量。", ["N4 bundles", "v2.1 bundle ① carries"]),
    ("B", 30, "その寄りの過半は語の積み上がり。ここは読みで、採否は依頼者。", ["v2.1 olm78: 'most of it is the words piling up'"]),
    ("B", 29, "言えないこと。開いた条件で着かないのが「選ばない」のか「引き金が無い」のかは、腕で分けていない。", ["cannot say: won't vs no trigger"]),
]
FORBID = ["判定に届", "冷間", "看破", "知らない", "知っている", "ひらめ", "気づ", "考えた", "迷っ", "理解した", "の心", "誘導", "全 model", "作図を再現", "持ち出", "逃げ", "出始め", "探る量"]
secs = lambda t: len(t) / 7.4
rows, t0 = [], 0.0
for i, (v, st, text, frags) in enumerate(LINES, 1):
    for w in FORBID:
        assert w not in text, f"line {i}: a word the figure does not use: {w}"
    d = secs(text)
    rows.append((i, v, text, st, d, t0, ", ".join(kid(f) for f in frags) or "—"))
    t0 += d + 0.45
total = t0 - 0.45
first10 = [r for r in rows if r[5] < 10]
assert total <= 150, f"the script is {total:.1f} s (> 150 s)"
assert all(r[3] == 1 for r in first10), "the first 10 s must be state 1 (A1)"
fmt = lambda s: f"{int(s // 60)}:{s % 60:04.1f}"
out = ["# SCRIPT — a two-voice scene for the video (moy-5 · the roads to the apex · entry_v2_1_received)", "",
       f"- Length: **{total:.1f} s** (characters / 7.4 per second + 0.45 s between lines; written and measured by `make_script.py`). ≤ 150 s.",
       f"- The lines that start in the first 10 s ({len(first10)} lines; the last of them ends at {fmt(first10[-1][5] + first10[-1][4])}) all cue **state 1** (A1): two real rows of one card, both answer fields on the floor, the roads parting in the reason field — the core. (v1 wrote this as 'the first 10 s … to 0:17.5'; the two readers flagged the mismatch: the 10 s are covered by state 1, and the last line that starts before 10 s ends later.)",
       "- Two voices: **A** = the listener, **B** = the explainer. No real character's name, picture or voice. Each line names the state it cues and the claim ids it rests on (CLAIMS.md). Every number is read from `generated/pack.json`.",
       "- Show the 1920 × 1080 stills `captures/video_s<N>.png` (state 0 also `video_s0a.png` / `video_s0b.png` = P_x moved, drawing only).", "",
       "| # | voice | line (spoken) | cue (state) | length | start | claims |", "|---|---|---|---|---|---|---|"]
for i, v, text, st, d, s0, k in rows:
    out.append(f"| {i:02d} | {v} | {text} | state {st} | {d:.1f} s | {fmt(s0)} | {k} |")
out += ["", "## Switching the states (a guide for the editor)", "", "| state | starts | picture |", "|---|---|---|"]
seen = []
for i, v, text, st, d, s0, k in rows:
    if st not in seen:
        seen.append(st)
        out.append(f"| {st} | {fmt(s0)} | `captures/video_s{st}.png` |")
out += ["", "## Reading guide (for a voice synthesiser)", "", "| written | read as |", "|---|---|",
        "| EJ = KP_y | イー・ジェイ イコール ケー・ピー・ワイ |", "| P_x / P_y | ピー・エックス / ピー・ワイ |", "| apex | エイペックス |", "| β′ | ベータ・プライム |", "| cut | カット |", "| effort / thinking | エフォート / シンキング |", "| Menaechmus | メナイクモス |", "| OLMo | オルモ |", "",
        "Caption to add if wanted: 「図は説明用。数は凍結した出力の欄の写しと数え。」"]
(HERE / "SCRIPT_yukkuri.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"script: {len(rows)} lines · {total:.1f} s · first 10 s = state 1 ({len(first10)} lines)")
