"""make_script.py — writes SCRIPT_yukkuri.md (the two-voice script, ≤ 150 s) from generated/pack.json: every number in a line is read from the pack, never typed.
Length = characters / 7.4 per second + 0.45 s between lines (the skill's rule of thumb). A = the listener, B = the explainer; no real character's name, picture or voice.
    python3 -I make_script.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
A = {a["id"]: a["agg"] for a in P["arms"]}
G, SC, V, LG = P["geo"], P["scenes"], P["verdicts"], P["lineage"]
r3 = lambda v: f"{v:.3f}"
row = lambda a, k: next(r for r in next(x for x in P["arms"] if x["id"] == a)["rows"] if r["k"] == k)
same = sum(1 for k in LG["frozen"] if LG["frozen"][k] == LG["v6same"][k])
maxd = max(round(A[a]["LN6_rate"] - A[a]["LN3_rate"], 4) for a in ("olm113", "olm119", "olm122", "olm124", "olm125"))
FR = {(f["x"], f["y"]): f for f in P["fisher"]}
CC = A["olm125"]["calc_cls"]
UP, DN = [f for f in P["fisher"] if f["p"] >= 0.05], [f for f in P["fisher"] if f["p"] < 0.05]          # v1.2 G7
Q3 = " → ".join(q[2] for q in LG["q3"])                                                                     # v1.2 G12 (state 15)
# v1.1 F2: the first 10 s (lines 01-02) are the two real rows (state 0); the drafting board follows (state 1). F3: line 02 names the subject (the tangent), line 12 says what the classes are.
L = [
    ("A", 0, "同じ問いの文の二行。どちらも折り返しを計算して退けた？", ["K68", "K69"]),
    ("B", 0, f"はい。二行とも本文で Not the same と書く。でも二行のうち、証明の欄に O1O2 についての対称を書いたのは {SC['S1']['key']} だけ(主語は接線)。", ["K68", "K43", "K90", "K115", "K116"]),
    ("A", 1, "図で、何が真で何が偽？", ["K71"]),
    ("B", 1, f"等距離 O3Tc = O3Th は真で、どちらも {G['dTc']:.3f}。Th を O1O2 で折り返しても Tc には着かない。だから「接点は O1O2 について対称」は偽。", ["K71", "K73"]),
    ("A", 2, "腕ごとに、何が違うの？", ["K83"]),
    ("B", 2, "問いの文の Tool の段だけ。式だけ、式に宣言の文、式に指示の文。", ["K83"]),
    ("A", 6, "証明の欄の線対称の率は？", ["K04"]),
    ("B", 6, f"道具なし {r3(A['olm113']['LN3_rate'])}、式だけ {r3(A['olm122']['LN3_rate'])} と {r3(A['olm124']['LN3_rate'])}、宣言の文 {r3(A['olm119']['LN3_rate'])}、指示の文 {r3(A['olm125']['LN3_rate'])}。指示の文の二回目は判定なしで、参考 {r3(A['olm127']['LN3_rate'])}。{r3(A['olm124']['LN3_rate'])} は olm124 の帯で {V['olm124']['read']}、{r3(A['olm125']['LN3_rate'])} は olm125 の帯で {V['olm125']['read']}。境は札ごとの PREREG。", ["K04", "K07", "K08", "K06", "K09", "K10", "K20", "K22", "K33", "K110", "K112"]),   # v1.3 H3: the band words
    ("A", 4, "判定なし、って？", ["K17"]),
    ("B", 4, f"取れた行 0.75 以上が関門。{A['olm124']['parsed']} / 60 は境ちょうど、二回目は {A['olm127']['parsed']} / 60 で落ちた。", ["K14", "K15"]),
    ("B", 9, f"隣り合う腕の Fisher は参考。{len(P['fisher'])} 対のうち {len(UP)} 対は 0.05 の上、{len(DN)} 対、{'・'.join(f['x'] + ' 対 ' + f['y'] for f in DN)} は下。判定ではなく、多重比較は補正していない。", ["K79", "K91", "K108"]),
    ("B", 10, f"計算した行で数えると、退けは olm119 が {A['olm119']['REJ_calc']} / {A['olm119']['CALC']}(全行 {A['olm119']['REJ']})、olm122 が {A['olm122']['REJ_calc']} / {A['olm122']['CALC']}(全行 {A['olm122']['REJ']})、四腕で {P['four']['num']} / {P['four']['den']}。", ["K78", "K88"]),
    ("A", 11, "計算した行は、折り返しを退ける？", ["K36"]),
    ("B", 11, f"olm125 では計算した {A['olm125']['CALC']} 本のうち {A['olm125']['REJ_calc']} 本が退ける。{A['olm125']['CALC']} 本の最終の conjecture の類は、等距離 {CC['EQ']}、OTHER {CC['OTHER']}、JSON なし {CC['NONE']}、共線 {CC['MIDO3']}。", ["K39", "K48", "K49", "K50", "K89"]),
    ("A", 12, "退けた後の、証明の欄は？", ["K43"]),
    ("B", 12, f"線対称に戻る行が {len(A['olm125']['typ'])} 本。二回目は 0 本だが、退けた {A['olm127']['REJ']} 本のうち {sum(1 for r in next(x for x in P['arms'] if x['id'] == 'olm127')['rows'] if r['rej'] and r['cap'])} 本は上限で証明の欄に届かない。直ったとは言わない。", ["K43", "K45", "K87"]),
    ("B", 13, f"数値で退けた命題を次の候補に出し続ける行もある。{SC['S8']['key']} は {SC['S8']['loop_count']} 回、{SC['S10']['key']} は {SC['S10']['loop_count']} 回。", ["K66", "K67"]),
    ("B", 15, f"計器を直す間に、olm118 Q3 の帯は {Q3} と往復した。", ["K61", "K60"]),
    ("A", 16, "計器を替えたら、判定は変わる？", ["K62"]),
    ("B", 16, f"v6 で率は最大 +{maxd:.3f} 動く。でも凍結の判定は {same} / {len(LG['frozen'])} 同じ。", ["K62", "K63"]),
    ("B", 19, f"凍結の判定で言えるのは、式だけは{V['olm124']['read']}(一回目は参考)、宣言の文は{V['olm119']['read']}、指示の文は一回目 {V['olm125']['read']}・二回目は関門に落ちて判定なし = 二回で立たない、まで。答え合わせは在るが読みは無い、は主 session の読み。", ["K20", "K21", "K22", "K17", "K114"]),
]
t, out = 0.0, []
for i, (v, st, text, ks) in enumerate(L, 1):
    d = round(len(text) / 7.4, 1)
    out.append((i, v, text, st, d, t, ks)); t += d + 0.45
total = round(t - 0.45, 1)
assert total <= 150, total
assert out[0][3] == 0 and out[1][3] == 0 and out[2][5] >= 10, "the first 10 s are the scene (state 0)"
assert not any(w in x[2] for x in out for w in ("分けられない", "分けられず", "この図では偽")), "v1.2 G7 / G2: old wordings are not spoken"
assert {10, 15} <= {x[3] for x in out}, "v1.2 G12: states 10 and 15 have a line"
mmss = lambda s: f"{int(s // 60)}:{s % 60:04.1f}"
md = [f"# SCRIPT — a two-voice scene for the video (札 Q v1.3, 2026-11-04 夕)\n",
      f"- Length: **{total} s** in all (characters / 7.4 per second + 0.45 s between lines; written by `make_script.py` from `generated/pack.json`). ≤ 150 s. The first 10 s (lines 01–02) are state 0, the scene: the two real rows of olm125 (the same kind of calculation — S1 reflected Th, S2 reflected Tc — the same reject, different proof fields; v1.2 G1). The drafting board (what is true and false in the figure) follows at state 1 (v1.1 F2).",
      "- Two voices: **A** = the listener (asks), **B** = the explainer. No real character's name, picture or voice. Each line names the state it cues and the claim ids (CLAIMS.md) it rests on.",
      "- Words the script does not use: the model thought / understood / noticed / hesitated; \"fixed\" for olm127's zero; an order of the three sentences; a flat \"分けられない\" (v1.2 G7: 1 of the 7 Fisher pairs lies below 0.05).",
      "- **状態 8 は行を選ぶ道具。動画は 11〜13(述語に当たる行だけ灯す)を使う**(v1.2 G12)。状態 8 の 420 本の全点灯は、読者が行を選ぶための頁で、台本は cue しない。",
      "- The cues are **not in state order** (6 → 4 → 9: the rates first, then why two arms have no verdict, then the Fisher reference). v1.2 G12 added one line each for state 10 (the denominators) and state 15 (the round trip of the olm118 Q3 band). v1.3 H3: the state-6 line now says the band words (0.108 = olm124's band 戻る, 0.225 = olm125's band 上がる; the edges are each card's PREREG, printed on states 5 / 6); to stay ≤ 150 s the state-10 and state-15 lines were shortened. v1.3 H1: the state-13 line says 「数値で退けた」.\n",
      "| # | voice | line (spoken) | cue (state) | length | start | claims |", "|---|---|---|---|---|---|---|"]
for i, v, text, st, d, s0, ks in out:
    md.append(f"| {i:02d} | {v} | {text} | state {st} | {d} s | {mmss(s0)} | {' · '.join(ks)} |")
# v1.1 F8: the switching table names the video still and the desk / phone stills of the same state; then every state's stills by name
import re
NS = json.loads((HERE / "config.json").read_text(encoding="utf-8"))["chapters"][-1][2] + 1
KJ = dict((int(m.group(1)), m.group(2)) for m in re.finditer(r'kicker: "状態 (\d+) · ([^"]*)"', (HERE / "i18n.js").read_text(encoding="utf-8")))
mc = (HERE / "make_check.py").read_text(encoding="utf-8")
LIGHT = [int(x) for x in re.search(r'desk\("page_light", \[([\d, ]+)\]\)', mc).group(1).split(",")]
EN_DESK = [int(x) for x in re.search(r'capture_desk_en\.json", \[\["wait", 1500\]\] \+ \[x for i in \(([\d, ]+)\)', mc).group(1).split(",")]
EN_VID = [int(x) for x in re.search(r'capture_video_en\.json", \[\["wait", 1500\]\] \+ \[x for i in \(([\d, ]+)\)', mc).group(1).split(",")]
md += ["\n## Switching the states (a guide for the editor)", f"The order below is the order of the cues, **not the state numbers** (6 → 4 → 9; states {', '.join(str(n) for n in range(json.loads((HERE / 'config.json').read_text(encoding='utf-8'))['chapters'][-1][2] + 1) if n not in {x[3] for x in out})} are not cued; state 8 is the row-picking tool).", "| state | starts | video 1920 × 1080 | desk (1440, dark) | phone (390, dark) |", "|---|---|---|---|---|"]
seen = []
for i, v, text, st, d, s0, ks in out:
    if st not in seen:
        seen.append(st); md.append(f"| {st} | {mmss(s0)} | `captures/video_s{st}.png` | `captures/page_dark_s{st}.png` | `captures/phone_dark_s{st}.png` |")
STILLS = ["| state | heading | video | desk dark | phone dark | also |", "|---|---|---|---|---|---|"]
for n in range(NS):
    also = ([f"`page_light_s{n}.png`"] if n in LIGHT else []) + ([f"`page_dark_s{n}_en.png`"] if n in EN_DESK else []) + ([f"`video_en_s{n}.png`"] if n in EN_VID else []) + (["`video_s8a.png` · `video_s8b.png` (the drag)"] if n == 8 else [])
    STILLS.append(f"| {n} | {KJ[n]} | `video_s{n}.png` | `page_dark_s{n}.png` | `phone_dark_s{n}.png` | {' · '.join(also) or '—'} |")
md += ["\n## Every state's stills by name (folder `captures/`; v1.1 F8)"] + STILLS
readme = HERE / "README.md"
if readme.exists():
    rt = readme.read_text(encoding="utf-8"); a, b = "<!-- stills:begin (written by make_script.py) -->", "<!-- stills:end -->"
    if a in rt and b in rt:
        readme.write_text(rt[: rt.index(a) + len(a)] + "\n" + "\n".join(STILLS) + "\n" + rt[rt.index(b):], encoding="utf-8")
md += ["\n## Reading guide (for a voice synthesiser)", "| written | read as |", "|---|---|", "| O1O2 | オー・イチ・オー・ニ |", "| O3Tc / O3Th | オー・サン・ティー・シー / オー・サン・ティー・エイチ |", "| Tc / Th | ティー・シー / ティー・エイチ |", "| b1_j17 | ビー・イチ・ジェイ・イチナナ |", "| v6 | ブイ・ロク |", "| JSON | ジェイソン |",
       "\nCaption to add if wanted: 「図は説明用。数は凍結した札の出力の写しと数え直し。計器は書いた語の印で、証明の正しさは読まない。」"]
(HERE / "SCRIPT_yukkuri.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(f"SCRIPT_yukkuri.md: {len(out)} lines · {total} s")
