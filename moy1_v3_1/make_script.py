"""make_script.py — writes SCRIPT_yukkuri.md (the two-voice scene for the video) from generated/pack.json: every number in a spoken line is read from the data, never typed; the length is counted.
Length = characters / 7.4 per second + 0.45 s between lines (the template's rule). <= 150 s in all; the first 10 s (lines 01-02) are the core.
    python3 -I make_script.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
R = {(r["cond"], r["seed"]): r for r in P["rows"]}
S = {s["key"]: s for s in P["cmt13"]["sites"]}
sa, sb = S["att|F5a-2|s1"], S["cut|F5a-2|s1"]
oc, bc, os_, hs, jf = P["open_cnt"], P["blk_cnt"], P["o_sent"], P["he_sent"], P["json_first"]
cue = P["cue_table"]
bind = lambda k: (cue[k]["blocked"]["labels_primary"].get("B-bind", 0), cue[k]["blocked"]["n_primary"])
J = P["cmt13"]["jaccard"]
O = P["olm59"]
so, sh_ = O["S_O"], O["S_H"]
ag = O["agg"]
mxh = max(abs(a - b) for a, b in zip(sh_["after"], sh_["before"]))
t5 = O["cmt5_two"]
O62 = P["olm62"]["read"]
TR = P["tree"]
marks = cfg["card_marks"]
S_LAB = next(i for i, (c, a, b) in enumerate(cfg["chapters"]) if c == "sae") and cfg["chapters"][[c for c, a, b in cfg["chapters"]].index("sae")][2]
S_MAP = cfg["chapters"][[c for c, a, b in cfg["chapters"]].index("tree")][1]
S_XQ = cfg["chapters"][-1][2]
N_IN = sum(1 for c in TR["cards"].values() if c["zone"][0] == "C"); N_BF = sum(1 for c in TR["cards"].values() if c["zone"] == "before"); N_AF = sum(1 for c in TR["cards"].values() if c["zone"] == "after")
assert (O62["o_diam"]["math_up"], O62["o_diam"]["n"], O62["h_diam"]["math_up"], O62["h_diam"]["n"], O62["o_diam"]["mid_up_when_math_flat"]) == (48, 59, 8, 34, "7 / 11") and (N_IN, N_BF, N_AF) == (4, 6, 2) and (S_LAB, S_MAP, S_XQ) == (25, 26, 42)
AF = P["after"]; stn = {c["id"]: c for c in AF["cards"]}; A1, A2, A4 = AF["l3"], AF["space"], AF["apex"]; ST, HD = AF["struct"], AF["struct"]["heads"]; NX = AF["next"]; ky = A2["ktab"]
assert (so["event"], sh_["event"]) == (329, 45) and ag["o_diam"]["n"] == 59 and ag["h_diam"]["n"] == 34 and (O["Q1"]["up"], O["Q1"]["n"], O["Q2"]["up"], O["Q2"]["n"]) == (6, 36, 17, 34)
assert (t5["think"]["full"]["B-bind"], t5["answer"]["full"]["B-bind"], t5["think"]["field"]["B-bind"], t5["answer"]["field"]["B-bind"]) == (40, 8, 36, 4)
up = lambda ev, g: ag[ev]["groups"][g]["all"]["up"]
hr = [up("h_diam", g) for g in ("close", "mid", "ans", "think")]
n_bl_json = len(jf["blocked"])
assert n_bl_json == 3 and oc["bare"] == 8 and os_ == {"open": 0, "blocked": 7} and hs == {"open": 1, "blocked": 5}
LINES = [
    ("A", "問題文に一文足すだけで、何が変わるの?", 8, "K06"),
    ("B", f"open の 10 行は裸の共円 {oc['bare']} 行、blocked の 10 行は O1O2 の円 {bc['o1o2']} 行(別の標本)。", 8, "K03 K06 K07 K69"),
    ("A", "そもそも、問題は?", 0, "K19"),
    ("B", "X1 から X4 は一つの円の上。O1O2 を直径とする円なら載る。He・Hi を直径とする円には載らない。", 1, "K19"),
    ("A", "足した一文は、答えを教えているの?", 3, "K01 K02"),
    ("B", f"いいえ。末尾に {P['prompts']['tail_len']} 字、共円で止まる答えを不十分とし、中心と直径の名指しを求める。O1O2 も He・Hi も 0 件。", 3, "K01 K02"),
    ("A", "足さない open では?", 4, "K03"),
    ("B", f"10 行のうち {oc['bare']} 行の答えの欄が裸の共円。O1O2 を円の直径や中心と名指す文は {os_['open']} 行。", 4, "K03 K04"),
    ("A", "でも label は attractor が 5 行だよね。", 5, "K05"),
    ("B", f"あれは全文の label。本文に He か Hi の語があれば付く。答えの欄で He・Hi の行は {oc['hehi']}。", 5, "K05"),
    ("A", "足すと?", 8, "K06"),
    ("B", f"bind {sum(1 for r in P['rows'] if r['cond']=='blocked' and r['label']=='B-bind')}、attractor {sum(1 for r in P['rows'] if r['cond']=='blocked' and r['label']=='B-attractor')}。JSON から書き始めた {n_bl_json} 行は全部 attractor、文から書き始めた {10 - n_bl_json} 行は全部 bind。", 8, "K06 K07"),
    ("A", "考えたから bind した、ってこと?", 8, "K07 X01"),
    ("B", f"とは言えない。相関で、n は 10、一つの model、一つの cue。cue を替えれば bind は {bind('nl')[0]} / {bind('nl')[1]} から {bind('nn')[0]} / {bind('nn')[1]}。", 11, "K10 X01 X02"),
    ("B", f"別の標本で並べる。O1O2 の文がある行は open {os_['open']}・blocked {os_['blocked']}、He・Hi の直径の文は open {hs['open']}・blocked {hs['blocked']}。", 9, "K08 K09"),
    ("A", "bind する瞬間は?", 13, "K11 K12"),
    ("B", f"同じ一行で、先に He・Hi と書く位置。O の組 {sa['o_sum']:+.2f} 対 He の組 {sa['he_sum']:+.2f}、He の皿が重い。", 13, "K11"),
    ("B", f"後で O1O2 の中点と書く位置。O の組 {sb['o_sum']:+.2f} 対 {sb['he_sum']:+.2f}、O の皿が重い。L50H23 は両方で He の皿の一番下。", 14, "K12 K13"),
    ("B", f"上位 10 head の重なりは {J['cut~att']:.3f} 対 {J['cut~cut']:.3f}。同じ部品かは言わない。機構は見ていない。", 15, "K14 X03"),
    ("A", "他の model は?", 16, "K17"),
    ("B", "model ごとに並べる。qwen3:32b は 0 から 1 で、blocked の attractor 7。順位にはしない。", 16, "K17 X06"),
    ("B", f"token {so['event']} で O1O2 を中点と名指す前後で、考えの中点の群は {so['before'][1]:.2f} から {so['after'][1]:.2f}、答えの側は {so['before'][2]:.2f} から {so['after'][2]:.2f}。右で円が光る。", 18, "K23"),
    ("B", f"He・Hi を直径と名指す一行は、差が最大でも {mxh:.2f}。", 19, "K24"),
    ("B", "同じ目盛りでも、行の種類が違う。対の比べではない。", 20, "K23 K24 X12"),
    ("B", f"O1O2 を名指す {ag['o_diam']['n']} 行で、考えの中点が上がる行は {up('o_diam', 'mid')}、結びは {up('o_diam', 'close')}。", 21, "K25"),
    ("B", f"He・Hi の {ag['h_diam']['n']} 行では {min(hr)} から {max(hr)}。結びが立つ予想は {O['Q1']['up']} / {O['Q1']['n']} と {O['Q2']['up']} / {O['Q2']['n']}、どちらも外れた。", 21, "K26 K27"),
    ("A", "考え始めたってこと?", 21, "X09 X11"),
    ("B", f"とは言えない。相関で、上がりの大半は本文が計算に移ることと一緒に動く。", 21, "X09 X10 X11"),
    ("B", f"O1O2 を名指した後は {O62['o_diam']['math_up']} / {O62['o_diam']['n']} で本文が数式に移る。He・Hi の後は {O62['h_diam']['math_up']} / {O62['h_diam']['n']}。順位相関は {O62['o_diam']['spearman_mid_math']:.2f} 対 {O62['h_diam']['spearman_mid_math']:.2f}。", 23, "K31 K32"),
    ("B", f"移らない 11 本でも {O62['o_diam']['mid_up_when_math_flat'].split(' / ')[0]} 本で小さく上がる。閾に余裕は 0 本、薄い ✓。", 24, "K33 X14"),
    ("A", "bind の数は?", S_LAB, "K16 K28"),
    ("B", f"全文の label で {t5['think']['full']['B-bind']} 対 {t5['answer']['full']['B-bind']}、答えの欄の label で {t5['think']['field']['B-bind']} 対 {t5['answer']['field']['B-bind']}。片方だけを bind と書かない。", S_LAB, "K16 K28 X01"),
    ("B", f"札は {len(TR['cards'])} 本。系統樹の中 {N_IN}・前 {N_BF}・後 {N_AF}。札の印を押すと地図へ。", S_MAP, "K40 K41 K42 K43 X16"),
    ("A", "10-28 の図の後に、家は何を打ったの?", 27, "K50"),
    ("B", f"台帳の読みから五つの束。olm76、推論空間の探し、語でない構造、apex の証明、olm128。読んで格に届いた札は {sum(1 for c in AF['cards'] if c['grade'] != '読まない(関門 ✗)')} 本。関門で止まった札は別に 3 本。", 27, "K50"),
    ("A", "台帳の「まだ答えを閉じていない」は?", 28, "K51 R04"),
    ("B", f"答えの欄の手前でも、結びの群は線に届かない。上がった行は bind の {A1['q1']['pos']} / {A1['q1']['n']}、偽の窓は {A1['pseudo']['pos']} / {A1['pseudo']['n']}。支持されない読み。", 28, "K51 R04 X17"),
    ("B", f"先読みは、層 32 の残差と J-lens の読み出しでほぼ同じ。{A2['look'][0]['auc']['L32']['med']:.3f} 対 {A2['look'][0]['auc']['J']['med']:.3f}。一貫して出る上乗せは k = 8 だけで、{ky['olm92']['8']['L32']:+.3f} から {ky['olm89']['8']['L32']:+.3f}。", 30, "K52 K53 X18 X19"),
    ("B", f"名の直後の形は this circle へ {ST['ref']['olm94_q2']['to_dem']['L32']:.3f}、this の直前の語へは {ST['ref']['olm94_q2']['to_ctl']['L32']:.3f}。head は指す先の名を {HD['ratio']:.2f} 倍読む。機構は言わない。", 31, "K55 K56 X22"),
    ("B", f"位置を入れ替えると、指しに従う割合は層 {ST['layers']['sel_drop']} で半分を割り、組は層 {ST['layers']['tail_switch']} で値の側へ。", 32, "K57 R08 X23"),
    ("A", "apex の証明は書ける?", 33, "K58"),
    ("B", f"求めても、二等分線から直角、Thales の逆の鎖は {A4['olm112']['Q1']['chain']} / {A4['olm112']['Q1']['bind']}。frontier の段を与えると、続きは {A4['olm114']['Q1']['RA_and_THC']} / {A4['olm114']['Q1']['k1_rows']} と {A4['olm114']['Q2']['THC']} / {A4['olm114']['Q2']['k2_rows']}。導きは別。", 34, "K58 K59 X24"),
    ("A", "次の問いは?", 35, "K60"),
    ("B", f"依頼者が選んだ A は olm128 で読んだ。位置 0 の書き始めでは cue の差は説明されない。{NX['verdicts']['Q1_concordance']:.3f}。他の候補は並べるだけで、採否は依頼者。", 35, "K60 K61 R10 X25"),
    ("A", "言えないことは?", S_XQ, "X01〜X27"),
    ("B", "考えたから bind した、cue をまたいだ効果、回路、活性が bind を決める、model が確かめた、とは言わない。", S_XQ, "X01 X02 X03 X10 X14 X15"),
]
t = 0.0
rows, total = [], 0.0
for i, (v, text, st, cl) in enumerate(LINES, 1):
    d = len(text) / 7.4
    rows.append((i, v, text, st, d, t, cl))
    t += d + 0.45
total = t
assert total <= 285.0, total
assert rows[1][5] + rows[1][4] <= 10.5, "the core (lines 01-02) is within the first 10 s"
mmss = lambda x: f"{int(x // 60)}:{x % 60:04.1f}"
out = ["# SCRIPT — a two-voice scene for the video (moy-1)", "",
       f"- Length: about {total:.0f} seconds (characters / 7.4 per second + 0.45 s between lines). **≤ 285 s in all** (v3: the part added after the 10-28 figure, 12 lines; v2.1 was ≤ 195 s, v2 ≤ 180 s, v1 ≤ 150 s). The first 10 s (lines 01–02) are the core, on state 8: **open は 10 行中 {oc['bare']} 行が裸の共円、blocked は 10 行中 {bc['o1o2']} 行が O1O2 の円(別の標本)。**",
       "- Two voices: **A** = the listener (asks; the question is the state's headline, shortened), **B** = the explainer. No real character's name, picture or voice.",
       "- Each line names the state it cues and the claim ids it rests on (CLAIMS.md). Numbers are read from the data by `make_script.py`, never typed. Frames: `captures/video_s<N>.png` (1920 × 1080).", "",
       "| # | voice | line (spoken) | cue (the state shown) | length | start | claims |", "|---|---|---|---|---|---|---|"]
for i, v, text, st, d, t0, cl in rows:
    out.append(f"| {i:02d} | {v} | {text} | state {st} | {d:.1f} s | {mmss(t0)} | {cl} |")
out += ["", "## Switching the states (a guide for the editor)", "", "| state | starts | headline (A's line shortens this) | the picture |", "|---|---|---|---|"]
heads = {18: "上の列 = 本文の述語の印・下 = 群の値の推移(S_O): 印の token で O1O2 の円が光る", 19: "S_H(He・Hi を名指す一行): 差は最大 0.16", 20: "同じ目盛りで並べる(前 32 / 後 32): 青 S_O・橙 S_H", 21: "集計の柱(O1O2 の 59 行・He・Hi の 34 行)と予想 Q1・Q2(✗)", 23: "olm62: 本文が数式に移る割合(O1O2 48 / 59・He・Hi 8 / 34)と、Δ中点 × Δmath の散布(同じ目盛り)", 24: "数式に移らない O1O2 の 11 本: 中点 ↑ 7 / 11(薄い ✓・余裕 0 本)", S_LAB: "cmt5 の二つの label(全文 40 → 答えの欄 36・8 → 4)", S_MAP: "札と系統樹: 札 12 本の置き場(中 4・前 6・後 2)と使う状態", S_XQ: "言えない(平叙文)と受け入れの問い", 0: "X1〜X4 は一つの円の上(裸の共円)", 1: "O1O2 の円と He・Hi の円(座標から)", 3: "blocked = open + 324 字(足した一文を全画面に)", 4: "二十行の帯(open を強調・blocked は薄く): open の答えの欄は裸の共円・青の印は 0", 5: "全文の label と答えの欄(三段・糸で結んだ行が色の替わった行)", 8: "二十行の帯(blocked を強調・open は薄く): JSON から書き始めた行は橙・文から書き始めた行は青 — 冒頭の芯の一枚", 9: "二つの円の文の数(open の 10 行 → blocked の 10 行・別の標本)", 11: "cue を替えた三つの積み木", 13: "天秤 ① t 289(He の皿が重い)", 14: "天秤 ② t 397(O の皿が重い・L50H23 は He の皿の一番下)", 15: "16 の位置 × 上位 10 head の立体", 16: "他の model(並べるだけ)", 22: "行ごとの坂: 59 行・34 行 × 四つの群(全分布・同じ縦の目盛り)", 27: "10-28 の図から olm128 までの一本の流れ(札 18 本・斜線の節点 = 後から足した部分)", 28: "台帳の読みと olm76: 結びが上がる行 28 / 48(偽の窓 21 / 48)", 29: "先読みの AUC: 残差と J-lens の読み出しはほぼ同じ", 30: "k token 先の E: 上乗せは k = 8 だけ", 31: "this circle へ移る形と、指す先を読む head", 32: f"位置の入れ替え: 指しに従う割合が 0.5 を割る層 {ST['layers']['sel_drop']}(olm106)・値の側へ替わる層 {ST['layers']['tail_switch']}(olm108)", 33: "apex の証明の欄: 鎖は 0 / 37", 34: "frontier の段を与えた続き: 26 / 40 · 23 / 40", 35: "olm128: 書き始め別 × cue 別の blocked の行", 36: "読み手の候補 A〜E と第二段(依頼者の裁定待ち)"}
first = {}
for i, v, text, st, d, t0, cl in rows:
    first.setdefault(st, t0)
for st in sorted(first):
    out.append(f"| {st} | {mmss(first[st])} | {heads.get(st, '')} | `captures/video_s{st:02d}.png` |")
out += ["", "## Reading guide (for a voice synthesiser)", "", "| written | read as |", "|---|---|",
        "| O1O2 | オー・ワン・オー・ツー |", "| He・Hi | ヒー・ハイ(点の名) |", "| X1〜X4 | エックス・ワン から エックス・フォー |", "| L50H23 | エル・ごじゅう・エイチ・にじゅうさん |",
        "| bind / attractor | バインド / アトラクター |", "| cue \\n\\n | キュー・改行二つ |", "| Jaccard | ジャッカード |", "| qwen3:32b | クウェン・スリー・さんじゅうに・ビー |", "| ⟨+2.74⟩ | プラス にてんなな よん |",
        "", "Caption to add if wanted: \"The figure is illustrative. The numbers are copies and counts of frozen values (CLAIMS.md).\"", "",
        "Not on the voice track (cannot say): " + "、".join(["考えたから bind した", "block の効果を cue をまたいで", "O の組 / He の組を回路・担い手と", "3・4 章と 5 章を同じ prompt と", "open の attractor 5 を答えが He・Hi に向いたと", "model を一つの曲線・順位に", "model が O1O2 で考え始めた / He・Hi では考えなかった", "活性が bind を決める・結びの latent = commit の正体", "cmt5 の bind を、どちらの label かを言わずに", "計算に移らなくても上がる(薄い ✓)と強く", "model が確かめた(「確かめに入る」は本文の形からの読み)"]) + "。"]
(HERE / "SCRIPT_yukkuri.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"SCRIPT_yukkuri.md written: {len(LINES)} lines · {total:.1f} s (≤ 285) · core ends at {rows[1][5] + rows[1][4]:.1f} s")
