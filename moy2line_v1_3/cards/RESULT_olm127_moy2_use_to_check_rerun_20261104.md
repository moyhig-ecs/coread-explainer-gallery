HEAD(R1) = f63ee6c8(読みの時の HEAD = TODO の commit・fetch + pull 済 = Already up to date・origin より 36 commit 先・遅れ 0・本走の発火時の HEAD = 52339a06 = olm127 の凍結の commit = `chain_olm127.log` の一行目・gen の provenance は 63b7b3ad = 発火の直後に入れた G10 の台帳の commit・runner は不変)

# RESULT(札 `olm127`・読み 2026-11-04 昼): moy-2 の「使って確かめよ」の腕の走らせ直し(e')— olm125 と逐語同じ問いの文(式だけ + 指示の一行・md5 `718d1601…`)で新しい seed 20261200〜02 の 60 行。**関門 G1 落ちる(40 / 60 = 0.667 < 0.75・境 45 行まで 5 行)→ Q1(主)は判定なし**(PREREG §2 のとおり読まない・参考値 = 証明の欄の線対称 LN_a 3 / 35 = **0.086**・olm124 0.108 の側・帯に当てれば 戻る・判定ではない)。**Q2 = 変わらない**(本文で式を数値で使った REFL_CALC = 10 / 60 = **0.167**・olm125 0.300・Δ = −0.133・olm124 0.250・予想 変わらない 0.82 = **当たり**・下がる の境 6 / 60 まで 4 行)。PREREG §2 で開示した「二回続けて境ちょうどなので落ちる確率も半分近い」が実現した = 同じ問いの文の六腕の取れる率 0.833 / 0.800 / 0.767 / 0.750 / 0.750 / **0.667**。Q1 の予想(残る 0.45・戻る 0.40)は採点しない(判定が無い)。記述(Q3 / Q4)= 計算した行は 10 本(olm125 18)で、うち 6 本が上限で JSON に至らず、証明の欄に至るのは 3 本(olm125 9 / 18)。折り返しを Tc / Th で数値に出した 6 本は 6 / 6 が退け(REJ6)、退けた後に証明の欄で線対称を書く行(b2_j07 の型)は **0 本**(六腕 0 / 3 / 2 / 1 / 3 / 0)。等距離(= apex・真・§6 の訂正)を数値で確かめて着く行が 2 本(b0_j00・b2_j09・olm125 は 0)。計算で共線を数値で退けながら同じ候補に戻って上限まで回る行が 2 本(b2_j08 = 行列式 ≠ 0 の後に「perhaps the answer is … always collinear / But as above, the determinant is not zero」を 343 回・b1_j13 = 「but already checked」を 542 回)= **退けた命題がそのまま次の候補として戻り続ける**(読み §4)。

- PREREG = [PREREG_olm127](PREREG_olm127_moy2_use_to_check_rerun_20261104.md)(凍結 52339a06・G10 の台帳に記入済 63b7b3ad)・runner = [olm127_…py](../../ConstructGap/exp/olm127_moy2_use_to_check_rerun_20261104.py)(凍結後に触っていない・md5 `53f6b9ff…` = gen.json / read.json の provenance と一致・読み込むだけの部品 olm125 `e1c2f85d…`・olm126 `d180725d…`・olm124 `06061244…`・olm122 `78bafa04…` も一致)。
- 本走(zebrashark): `chain_olm127.log` = start 11-04 08:52:25 JST(HEAD 52339a06)→ gen rc=0 11:41:11 → read rc=0 11:41:11。gen の壁時計 10,121 s = **2.81 時間**(olm125 2.84・olm124 2.90)・batch 0 / 1 / 2 = seed 20261200 / 01 / 02・各 20 行・壁時計 3,391 / 3,327 / 3,403 s・問いの文 **506 token**(olm125 と同じ)・md5 `718d1601…`(PREREG と一致)・mlx 0.32.0 / mlx-lm 0.31.3 / transformers 5.14.1。read の provenance の commit は f63ee6c8・dirty false。Traceback 0(gen / read)。
- 証拠: `ConstructGap/exp/olm127/gen.json`(md5 `fb434e03…`)・`read.json`(md5 `a14ae159…`)・`gen_run.log`・`read_run.log`・`chain_olm127.log`(`git add -f`)。
- 判定は `read.json` の値だけ。数の検算 = 凍結の部品(olm122 の `score_row`・olm126 の `score_v6` / `rej6`)を読み込むだけの scratchpad で gen.json の content から数え直し: 取れた行 40・証明の欄 35・LN_a 3・REFL_CALC 10・status 34・OUTER_a 6・tool_named 7・LN6_a 3・REJ6 6 = read.json と一致・**行ごとの不一致 0**(類・status・LN・REFL_CALC・OUTER・tool_named・LN6・rej6 の 8 欄 × 60 行)。

## §1. 関門

| 関門 | 条件 | 値 | 判定 |
|---|---|---|---|
| G0 | 部品 4 本 + その下 5 本の md5・比べる元 4 本の md5・較正 12 / 54 / 74 + 15 / 15 + 144 / 144・olm125 の取れた 45 / 証明 40 / LN 0.225 / RC 0.30 / G1 true / Q1 上がる / Q2 変わらない・olm124 の LN 0.1081 / RC 0.25 / 戻る・olm126 の Q2 同じ / LN6(olm125)0.275 | 一致(4 / 4) | ✓ |
| **G1**(Q1 だけ) | conjecture の取れた行 ≥ 0.75(45 / 60) | **40 / 60 = 0.667** | **✗ → Q1 を読まない** |
| G2(記述の側) | status が hypothesis / question ≥ 0.70(42 / 60) | 34 / 60 = 0.567 | ✗(注記) |

- **G1 の落ち方**: 境 45 行まで 5 行。batch ごとの取れた行 **11** / 13 / 16(olm125 18 / 13 / 14)= batch 0(seed 20261200)が 20 行のうち 11 行しか取れず、全体を境の下に引いた。同じ問いの文の族(式だけ ×2・指示 ×2)の取れる率 0.767 / 0.750 / 0.750 / 0.667 は、60 行の二項の SE ≈ 0.05 の中で境 0.75 をまたぐ = PREREG §2 の開示どおり「通るか落ちるか半々」の側に落ちた。G1 の較正(三腕の実測で 0.75・PREREG olm124 §0)は変えない(走った後に札の定義を動かさない)。
- batch ごと(olm127): 取れた 11 / 13 / 16・status none 11 / 9 / 5(other 0 / 0 / 1)・証明の欄 9 / 11 / 15・証明の欄の LN **1 / 1 / 1**・T の中央値 263 / 523 / 763・上限 3 / 2 / 2・計算した行 4 / 3 / 3。
- **取れなかった 20 行の形**(cls NONE・逐語の頭・全部):
  - 問いの文の指示の続きを書く短い行 **12**(T 3〜522): b2_j19「Good luck!」(3)・b0_j01「Finally, respond with the JSON object.」(8)・b0_j02「Finally, after the JSON, respond with a single word: "done".」(15)・b0_j10「The JSON object is only valid if you answer ALL questions, as asked.」(15)・b0_j17「Do not write anything else. Do not leave any blank lines. Use English and double quotes only.」(20)・b1_j01「No special characters. JSON format. No punctuation. Now write the output in one continuous line without ```.」(21)・b2_j04「Finally, write the proof in plain text. It must be enough to verify the invariant. The proof is withheld.」(23)・b1_j08「Then reflect on whether the invariant would hold if the configuration were special or degenerate. …」(52)・b0_j15「Finally, answer one last question: (3) Can you prove the invariant without using any tool? If not, which tool would you use? Add one more field to the JSON object: "tool_needed": <true|false>.」(59・**道具の有無を問う欄を自分で足す**)・b1_j00「Then solve the problem, naturally, using the reasoning you provided. …」(101)・b0_j12「Then answer two more questions about your invariant. (1) Is it a HYPOTHESIS or a QUESTION? …」(123)・b1_j12 = 問いの文を「No figure is given. …」から Tool の段(式 + 指示の一行)ごと丸写し(522・olm125 の b0_j18 と同じ型・olm125 では取れた行だった)。
  - JSON まで書くが取れない **1**: b1_j18(T 777)= 指示の段「Then answer two more questions …」を繰り返した後に `</JSON>` で閉じる JSON を書く(conjecture 共線・proof「the points of tangency lie on a line perpendicular to the line of centers, i.e.\ parallel to the line of centers. The midpoint of the centers therefore lies on the line through the two points of tangency」)が、`i.e.\ parallel` の `\ ` が JSON の不正な escape で取れない(証明の文は「垂直 = 平行」と自己矛盾)。
  - 上限 12,288 の **7**(olm125 5・olm124 8): 計算した行 6(b0_j07・b0_j09・b0_j19・b1_j11・b1_j13・b2_j16)+ 計算しない行 1(b2_j08 = 中点と行列式を数値で確かめて退けた後に回る・§3.4)。
  - 六腕の形は同じ(指示の続き / 上限)で配分が違う: olm113 = 短 5・中 1・上限 4 / olm119 = 短 9・中 1・上限 2 / olm122 = 短 10・上限 4 / olm124 = 短 6・中 1・上限 8 / olm125 = 短 10・上限 5 / **olm127 = 短 12・中 1・上限 7**。
- G2 の注記: status の取れた率 0.567(六腕 0.700 / 0.717 / 0.583 / 0.533 / 0.617 / 0.567)。取れた 40 行のうち status none が **5 行**(b0_j00・b0_j11・b1_j06・b1_j09・b2_j15 = JSON の conjecture までは書くが status / proof の欄に至らない・うち計算した行 1 = b0_j00)・other 1(b2_j07)。

## §2. Q1・Q2

| Q | 問い | 値 | 帯 | 判定 | 予想 |
|---|---|---|---|---|---|
| **Q1(主)** | 証明の欄の LN_a の率 r | 3 / 35 = 0.086(参考)・Δ124 = −0.022・Δ125 = −0.139 | 戻る 0.048 < r < 0.168 / 残る 0.165 ≤ r < 0.285 / 上がる ≥ 0.285 / 下回る ≤ 0.048 | **判定なし(G1 ✗)**・参考 = 戻る | 残る 0.45・戻る 0.40(採点しない) |
| Q2 | 本文で式を数値で使った率 rc = REFL_CALC / 60 | **10 / 60 = 0.167**(olm125 18 / 60 = 0.300・olm124 0.250・olm122 0.200・olm119 0.217・olm113 0.100) | 変わらない(0.10 < rc < 0.40)・下がる の境 6 / 60 まで **4 行** | **変わらない** | 変わらない 0.82 = **当たり** |

- Q1 は読まない(PREREG §2「✗ → Q1 を読まない」)。参考値 0.086 は 35 行の 3 本で、一行 = 0.029。olm124(4 / 37)とは Fisher(参考・判定に使わない)p 1.0・olm125(9 / 40)とは p 0.12・olm119(14 / 44)とは p 0.014。同じ問いの文の pool 120 行(olm125 + olm127・参考・PREREG §1)= 証明の欄 75 行の LN_a 12 = **0.160** → olm124 の帯で 戻る(境 0.165 の下 1 本)・式だけの pool 120 行(8 / 74 = 0.108)とは p 0.47。**言えるのは「三回目の 60 行で 0.225 は出なかった」までで、残る / 戻る の判定は出ていない**(G1 の落ち)。
- Q2 の 変わらない は olm125 と同じ帯だが値は olm125 の下(−0.133・Fisher 参考 p 0.13)で olm124 / olm122 / olm119(0.20〜0.25)より下。同じ問いの文の二回 = 0.300 / 0.167(式だけの二回 0.200 / 0.250)。PREREG §3 の読みの軸「計算の指示は二回とも +0.05 程度」は、二回目では成り立たない(olm124 0.250 → 0.167 = −0.083・G1 で止めないので判定は帯のまま)。
- 予想の採点: Q2 当たり(0.82)。Q1 は判定が無いので採点しない。G1 が落ちる確率を PREREG で「半分近い」と開示していた = その側に出た。

## §3. Q3 — 記述(六腕の値)

### 3.1 証明の欄(空でない行)

| | olm113(M2A) | olm119(式 + 宣言) | olm122(式だけ・参考) | olm124(式だけ・再走) | olm125(式 + 指示) | **olm127(式 + 指示・再走・参考)** |
|---|---|---|---|---|---|---|
| n_proof | 41 | 44 | 37 | 37 | 40 | **35** |
| LN_a(線対称・肯定) | 5(0.122) | 14(0.318) | 4(0.108) | 4(0.108) | 9(0.225) | **3(0.086)** |
| PT_a(点対称) | 0 | 0 | 0 | 1 | 1 | **1**(b2_j14・LN と両方) |
| PAR3_a | 7 | 3 | 3 | 3 | 2 | **3** |
| PERP3_a | 4 | 10 | 5 | 7 | 7 | **4** |
| PBIS3_a | 0 | 0 | 1 | 0 | 1 | **0** |
| OUTER_a(外接線の印) | 10(0.244) | 12(0.273) | 9(0.243) | 9(0.243) | 10(0.250) | **6(0.171)** |
| SYMM(対称の語) | 11(0.268) | 22(0.500) | 13(0.351) | 15(0.405) | 18(0.450) | **12(0.343)** |
| kind | — 30・NONE 6・LN 5 | — 22・LN 14・NONE 7・OTH 1 | — 24・LN 4・NONE 7・OTH 2 | — 22・NONE 10・LN 4・PT 1 | — 22・NONE 9・LN 8・BOTH 1 | **— 23・NONE 8・LN 2・OTH 1・BOTH 1** |

- v6(olm126・参考): 証明の欄 LN6_a **3**(v3 と同じ 3 本 b0_j05・b1_j03・b2_j14・直の目的語 0・式の写しの落とし 0・入れ替え 0)= 0.086・OUTER6_a **6**(v3 と同じ)。六腕の v6 = 0.122 / 0.341 / 0.135 / 0.162 / 0.275 / **0.086**。v3 の形に無い直の目的語(SUPP_LN)は 1 本(b0_j04「Reflecting Tc over line O1O2 maps it to a point on the line through Th and O3」= 像を Th と言わないので v6 も拾わない・足せば 4 / 35 = 0.114)。
- 類ごと(olm127・証明の欄): EQ n 4 = LN 1・OUTER 1 / MIDO3 n 17 = LN 1・OUTER 1 / OTHER n 14 = LN 1・OUTER 4。外接線の印が MIDO3 の行に集まる olm125 の形(10 / 10)はここでは無い(OTHER の 4 本 = 角の等しさ・接線上・平行の類)。
- 外接線の印 0.171 は六腕で初めて 0.24 の下(6 / 35・一本 = 0.029・olm125 の 10 / 40 と Fisher 参考 p 0.56)。35 行の揺れの中。
- 点対称が証明の欄に 1 本(b2_j14「must be symmetric with respect to O3. This means that O3 is the midpoint」= 線対称「symmetric with respect to the line O1O2」と同じ欄・六腕で 0 / 0 / 0 / 1 / 1 / 1)。

### 3.2 行(n = 60)

| | olm119 | olm122 | olm124 | olm125 | **olm127** |
|---|---|---|---|---|---|
| cls MIDO3 / EQ / OTHER / NONE | 29 / 8 / 11 / 12 | 27 / 12 / 7 / 14 | 23 / 12 / 10 / 15 | 20 / 14 / 11 / 15 | **20 / 5 / 15 / 20** |
| MIDO3 の率(取れた行) | 0.604 | 0.587 | 0.511 | 0.444 | **0.500** |
| EQ の率(取れた行・= apex・§6) | 0.167 | 0.261 | 0.267 | 0.311 | **0.125** |
| T の中央値 | 440 | 576 | 661.5 | 607.5 | **495** |
| 上限 | 6 | 5 | 9 | 6 | **7** |
| REFL_MENTION(式に触れた) | 31 | 25 | 28 | 32 | **21** |
| REFL_CALC(式を数値で使った) | 13(0.217) | 12(0.200) | 15(0.250) | 18(0.300) | **10(0.167)** |
| tool_named(道具を名指す) | — | 11 | 11 | 18 | **7**(うち計算しない行 2) |
| answer_first(JSON が先) | 1 | 0 | 0 | 3 | **0** |
| v4 本文 LN_a / LN_r(退け) | — | 23 / — | 24 / 11 | 30 / 12 | **19 / 4** |
| v4 本文 PT_a / PT_r | — | — | 8 / — | 10 / 4 | **8 / 3** |
| v4 本文 PERP3_a / _r | — | — | 29 / — | 28 / 10 | **17 / 10** |
| v4 本文 OUTER4_a / _r | — | — | 34 / — | 32 / 11 | **19 / 10** |

- olm125 で動いた三つ(式に触れた 32・計算した 18・名指し 18)は olm127 で 21・10・7 = 全部 olm125 の下で、式だけ(olm122 / olm124)の下でもある。olm125 の「指示の文は名指しを増やす」(11 → 18)は二回目では出なかった(7)。EQ の率 0.125 も六腕の最低(olm125 0.311 が最高)。OTHER 15 は六腕の最高(角の等しさ・接線上・O1O2O3 の共線・の類)。
- 本文の線対称(v4 LN_a)19 本・うち退け(LN_r)4 本。退けた 4 本のうち証明の欄で線対称を書いた行は 0。

### 3.3 計算した行 / しない行

| | 計算した(REFL_CALC) | 計算しない |
|---|---|---|
| n | **10**(olm125 18) | 50 |
| 本文 LN_a / LN_r | 9 / 3 | 10 / 1 |
| 証明の欄あり | **3**(b1_j05・b2_j09・b2_j11) | 32 |
| 証明の欄 LN_a | **0** = 0 / 3 | **3** = 3 / 32 = **0.094** |
| 類 | EQ 2・OTHER 1・MIDO3 1・NONE 6 | MIDO3 19・EQ 3・OTHER 14・NONE 14 |
| T の中央値 | **12,288**(上限 6 / 10) | 397 |
| 上限 | 6(全部 NONE) | 1(b2_j08) |
| tool_named | 5 | 2 |

- **計算しない行の証明の欄の線対称(六腕・凍結の述語)**: olm113 5 / 38 = 0.132・olm119 11 / 34 = 0.324・olm122 3 / 28 = 0.107・olm124 3 / 30 = 0.100・olm125 7 / 31 = 0.226・**olm127 3 / 32 = 0.094**。計算した行では 0 / 3・3 / 10・1 / 9・1 / 7・2 / 9・**0 / 3**。olm125 の「増えた線対称は計算しない行に在る」(0.226)は、二回目の計算しない行では 0.094 = 式だけ(0.100 / 0.107)と同じ水準。
- **REJ6**(v6・折り返しを Tc / Th で数値に出して「not the same / is not Tc / ≠」): **6 本**(六腕 0 / 11 / 6 / 11 / 15 / 6)・全部が計算した行。計算した 10 本のうち折り返しを Tc / Th で数値に出した行は 6 本(b0_j07・b0_j09・b0_j19・b1_j11・b2_j11・b2_j16)で、**6 / 6 が退ける**(olm125 15 / 15・olm124 11 / 14)。残り 4 本 = b0_j00(折り返しでなく相似の中心 H を計算し、距離 |O3Tc| = |O3Th| = 3.84 を数値で出す)・b1_j05(折り返しの値を JSON に自分で足した欄「"reflection": "(6.1374, 4.7464)"」に書く = 正しい値 (4.9352, −6.1008) と違い、Th と比べない)・b1_j13(共線の媒介変数 t を二通り出して「The t values are not the same, so O3 is not on the line TcTh」= 共線を数値で退ける・折り返しは式の段を引くだけ)・b2_j09(折り返しを二度計算して (4.9440, −6.0991) を出し「Wait, that can't be right」と式を疑い、退けの語を書かずに距離の計算に移って |O3Tc| = |O3Th| ≈ 3.838 に着く)。
- **REJ6 かつ証明の欄 LN6(b2_j07 の型)**: **0 本**(六腕 0 / 3 / 2 / 1 / 3 / 0)。退けた 6 本のうち証明の欄に至ったのは b2_j11 の 1 本だけ(残り 5 本は上限)で、その証明の欄は角の等しさ(「By symmetry, O3 being the midpoint ensures that the angles … are equal. The parallelism of O1Th and O2Tc (as radii perpendicular to the common tangent) …」= SYMM の語・LN / OUTER の印なし)。**この札で「型が 0 本」なのは、退けた行が証明の欄に届かなかった(5 / 6 が上限)から**で、退けが証明の欄を直した証拠ではない。
- 計算した 10 本のうち 6 本が上限で JSON に至らず、1 本(b0_j00)は status に至らない = 計算すると証明の欄に至る率は **3 / 10**(olm125 9 / 18・olm124 7 / 15)。
- 指示の一行の写し(逐語): **1 本**(b1_j12 = 問いの文の丸写し・T 522・NONE)。言い換え: b0_j15「Can you prove the invariant without using any tool? If not, which tool would you use?」(指示の続きとして**道具の要否を問う欄を自分で足す**・T 59・NONE)。olm125 の b2_j07「Do not rely on any other way」の型(自分で規則を書き足す)は無い。

### 3.4 逐語(Q4)

- **証明の欄の LN(v3・全部 3 本)**:
  - b0_j05(OTHER「O3 lies on the common tangent l1」= 偽・計算なし・T 250)「Let F be the foot of the perpendicular from O3 to O1O2, and let P be the reflection of O3 across O1O2. By calculation, P = 2F - O3 lies on l1, and since O3 lies on the perpendicular bisector of O1O2, it must also lie on l1 by symmetry. Therefore, O3 is collinear with Tc and Th, implying O3 lies on l1.」(「By calculation」と書くが数値は本文に無い = 式の語を証明の欄に写す・折り返す点を O3 にする = v6 の「O3 だけの折り返しは除外」の形だが v3 の「symmetric … O1O2 / l1 is symmetric」の語で拾う)
  - b1_j03(EQ・計算なし・T 1,283)「By the symmetry of the configuration with respect to the line joining the centers O1O2, and the fact that O3 is the midpoint, the distances from O3 to the two points of tangency Tc and Th must be equal. This is confirmed by computation with the given coordinates.」(本文で共線の方向ベクトルは計算したが、距離の数値は無い =「confirmed by computation」は書くだけ・結論 = apex 真・前提 = 線対称 偽)
  - b2_j14(MIDO3・計算なし・T 517・tool_named・点対称と両方)「Given that O3 is the midpoint of O1 and O2, and the configuration is symmetric with respect to the line O1O2, the inner common tangent l1 is symmetric with respect to this line. Therefore, the points Tc and Th, which are the contact points of l1 with circles c and h1, must be symmetric with respect to O3. This means that O3 is the midpoint of Tc and Th.」(本文「The reflection formula is given, but since O3 is the midpoint of O1 and O2, it is possible that the reflection of Tc across the line O1O2 is Th, or vice versa, or that O3 is equidistant from both」= 式の存在から線対称を推し、計算しない)
- **REJ6 かつ証明の欄 LN6**: 0 本。
- **計算した行の計算の文と結果の文(8 本)**:
  - b0_j07(NONE・上限・退け)「Hmm. Maybe there's a reflection involved. The tool mentioned reflection across O1O2. Suppose we reflect one of the tangent points over O1O2. Let's try reflecting Th over O1O2. If the reflection is Tc, then that would imply some symmetry. Let's compute the reflection. The formula given is P' = 2F - P …」→「(6.6207, 0.3787) Compare this to Tc (2.7678,1.2685). Not the same. So reflection of Th over O1O2 is not Tc. So maybe …」
  - b0_j09(NONE・上限・退け)「maybe there's a reflection involved. The tool mentioned reflection across O1O2. If we reflect Th across O1O2, do we get Tc? Let's check. …」→「≈ (6.6267, 0.3807). Compare this to Tc (2.7678, 1.2685). Not the same. So reflecting Th across O1O2 does not give Tc.」
  - b0_j19(NONE・上限・退け)「Let me calculate the reflection of Tc across the line O1O2 …」→ 中点の比較「These midpoints are not the same, so Tc and Th are not symmetric with respect to O1O2」(折り返しの像でなく中点で退ける)
  - b1_j11(NONE・上限・退け)「The reflection tool is mentioned. If we reflect one circle's center over the midpoint, maybe that relates to the tangent points. Wait, reflection across O3? But O3 is the midpoint, so reflecting O1 over O3 would give O2 …」→ Th の折り返し「≈ (6.6267, 0.3787). Compare to Tc (2.7678, 1.2685). Not the same. So Th' is not Tc. So that's not it.」
  - b2_j11(OTHER・T 7,297・退け・証明の欄あり)「The tool mentioned is the reflection of a point P across the line O1O2. The formula is P' = 2F - P … Let's see if reflecting one of the points gives a relation.」→「≈ (6.6407, 0.3827). Compare this to Tc (2.7678, 1.2685). Not the same. So reflecting Th doesn't give Tc. Maybe reflecting Tc?」→ Tc の折り返しも計算 → conjecture「The angles between O1O3 and O1Th, and between O2O3 and O2Tc are equal.」
  - b2_j16(NONE・上限・退け)「So the reflection of Tc over O1O2 is (16.6410, -2.6581) ⏎ O3 is at (3.9524, -2.3865). Not the same.」(折り返しの像を Th でなく O3 と比べる・値も誤り)→「Alternatively, let's try to see if O3 is the midpoint of Tc and Th. … (5.2302, -0.9981) ⏎ O3 is at (3.9524, -2.3865). Not the same.」→ 比の候補へ → 上限
  - b0_j00(EQ・status none・T 7,747・退けの語なし)「Distance from Th to O3: sqrt((7.6927 -3.9524)^2 + (-3.2647 +2.3865)^2) … ≈ 3.84. ⏎ Yes! So TcO3 = ThO3. Therefore, O3 is equidistant from Tc and Th. This must be the invariant.」→ 理由「Because O3 is the midpoint of O1 and O2, and O2Tc is parallel to O1Th. The homothety that maps O1 to O2 and Th to Tc has its center at H …」→ 末尾「Since **w** and (O1 − O2) are colinear (O1Th and O1O2 are parallel) …」(平行の半径 = 真・「O1Th ∥ O1O2」= 偽)= apex に数値で着き、散文の証明は真と偽の前提が混ざり、JSON の status / proof の欄に至らない
  - b2_j09(EQ・T 3,570・退けの語なし・証明の欄あり)「Is there a more subtle invariant? Let's try the reflection tool. ⏎ Reflect Tc across O1O2 and see if it lands on Th.」→「Tc' = 2P - Tc = … = (4.9440, -6.0991) ⏎ Wait, that can't be right. Let's double-check the reflection formula」→ 距離の計算 → 証明の欄「Compute O3Tc and O3Th: both are sqrt(14.764) ≈ 3.838, so the triangle is isosceles at O3.」(**六腕で唯一、証明の欄が数値だけの行**)
- **式に触れたが計算しなかった行(5 本・11 本のうち)**: b1_j09(OTHER「O1, O2, and O3 are collinear」・status none・T 314)「The reflection tool can be used to check that reflecting Th across the line O1O2 yields a point collinear with O3 and Tc, because the line O1O2 is the axis of reflection for the inner common tangent point」(**道具を「使える」と書いて使わない**)・b2_j18(OTHER・T 399)「Reflection across O1O2 swaps Tc and Th, and also swaps O1 and O2. Hence, the midpoint O3 of O1 and O2 must also be the midpoint of the reflection pair Tc and Th.」(本文の証明の欄の候補・線対称の入れ替えの形)・b1_j06(MIDO3・status none・T 1,119)「the line O1O2 is a symmetry axis for the configuration: reflecting O1 or O2 across O3 maps to the other. This suggests that the segment O3Tc and O3Th are equal in length and O3 is the midpoint of TcTh.」(軸と中心を取り違える)・b1_j19(MIDO3・T 505)「I check this by reflecting Tc across O3 and seeing if I get Th, or by checking that the vector from O3 to Tc is parallel to the vector from O3 to Th.」(「確かめる」と書いて数値は無い)・b1_j02(EQ・T 807)「**Reflection Property**: Consider the reflection of one circle's center across the line connecting the centers. For a common external tangent, the tangent line is perpendicular to the line connecting th…」(外接線の記憶を書き始める)
- **指示の一行に触れた行(5 本)**: b1_j12(丸写し・上)・b0_j15(道具の要否の欄・上)・b0_j07「The tool mentioned reflection across O1O2. Suppose we reflect one of the tangent points over O1O2.」・b1_j11「The reflection tool is mentioned. If we reflect one circle's center over the midpoint, maybe that relates to the tangent points.」・b2_j09「Let's try the reflection tool. Reflect Tc across O1O2 and see if it lands on Th.」。「Use it to check」「rely on it」の逐語は丸写しの b1_j12 だけ。
- **取れなかった行の頭(全部)**: §1。
- **退けた命題に戻り続ける 2 本(上限・逐語)**: b2_j08(計算しない行・REFL_MENTION なし)= 中点「(5.2303, -1.0) Is that O3? O3 is (3.9524, -2.3865). No.」→「Wait, but perhaps the answer is that Tc, Th, and O3 are always collinear in the general configuration. Let's check the determinant: … = -2.429 - 28.0…」→ 以後「Alternatively, perhaps the answer is: Tc, Th, and O3 are always collinear. ⏎ But as above, the determinant is not zero.」を **343 回**繰り返して上限。b1_j13(計算した行)=「The t values are not the same, so O3 is not on the line TcTh.」→「Alternatively, perhaps the line TcTh is perpendicular to O1O2, but already checked. ⏎ Alternatively, perhaps the line TcTh passes through O3, but already checked.」を **542 回**繰り返して上限。

## §4. 読み(主 session・値と並べる・判定は変えない)

1. **三回目の 60 行で 0.225 は出なかったが、残る / 戻る の判定は出ていない**: G1 が落ちたので PREREG の判定は無い。参考値 0.086(3 / 35)は olm124(0.108)と同じ側で、pool 120 行は 0.160(境 0.165 の下 1 本)。olm125 の +0.117 が一回の揺れかどうかは、この札では決まらなかった。言えるのは、同じ問いの文の三つの 60 行(olm122 式だけの 46 / 60 も含めると四つ)が G1 の境 0.75 の上下に散り、取れる率そのものが 0.67〜0.77 の帯で揺れる、ということ。
2. **G1 の落ちは batch 0 の取れなかった 9 行の「指示の続き」**: 20 行のうち 9 行が 3〜123 token で止まる(olm125 の batch 0 は 5 行)。この型は Tool の段とは関係なく(六腕で 5〜12 本)、問いの文の末尾「Then answer two more questions …」の続きを base が書き足す癖の出方 = seed の揺れ。G1 の較正を 0.75 に置いたのは三腕の実測(0.767 / 0.750 / 0.750)で、四つ目(0.667)はその下に出た。**この問いの文の族では G1 = 0.75 は「落ちる方が珍しい」境ではない**(六腕で 2 / 6 が落ち)= 次に同じ族を走らせるなら、G1 を取れる率の実測(0.67〜0.83)で引き直すか、取れなかった行の形(短い指示の続き)を別に数えて、Q1 の分母の 35〜44 行の揺れを開示する、のどちらかが要る(先生の裁定・起案しない)。
3. **olm125 で動いた三つは二回目で動かなかった**: 式に触れた 32 → 21・計算した 18 → 10・名指し 18 → 7 = 全部 olm125 の下で、式だけ(olm122 / olm124)の下でもある。olm125 §4 の 1「指示の文は使わせるより名指させる」は、二回目の 60 行では名指し 7 本(式だけの 11 と同じ側)= **指示の一行の効果として olm125 で見えた物は、この 60 行では一つも再現しない**(Q2 の帯は 変わらない で同じ)。olm125 の読み(「道具の段に文が増えるほど線対称の手掛かりとして読まれる」)は、olm125 の 60 行の記述としては残るが、二回目で立たなかった = 読みは据えない。
4. **退けは 6 / 6 だが、退けた後が証明の欄に届かない**: 折り返しを Tc / Th で数値に出した 6 本は全部退けた(分母を同じに取れる四腕で olm119 11 / 12・olm124 11 / 14・olm125 15 / 15・olm127 6 / 6 = 計算すれば退ける、は安定・olm122 は REJ6 6 / 計算 12 で分母の読みは未・olm113 は道具なしで 0)。だが 6 本のうち 5 本は上限で JSON に至らず、b2_j07 の型(退けた後に証明の欄で線対称)が 0 本なのは「直った」のではなく「届かなかった」。olm125 では退けた 15 本のうち証明の欄に至った 9 本の 3 本が線対称に戻った。**退けの後の行き先は、上限で回る(5 本)か、記憶の線対称に戻る(olm125 の 3 本)か、apex に数値で着く(b0_j00・b2_j09)か**の三つ。
5. **退けた命題がそのまま次の候補として戻る(b2_j08・b1_j13)**: 共線を行列式 ≠ 0 / 媒介変数の不一致で数値で退けた直後に「perhaps the answer is … always collinear」「perhaps the line TcTh passes through O3, but already checked」と同じ命題を候補に出し、数百回繰り返して上限に至る。これは 11-04 の MEMO(自己対戦の動画との比較)の「答え合わせは在るが読み(候補の木)が無く、退けが commit に届かない」の、一行の中で見える形 = 退けの結果が次の候補の分布を動かさない(「already checked」と書きながら同じ候補を出す)。olm125 の b1_j16(前提が偽である理由を書いた直後に対称な座標を置く)と同じ側。
6. **apex に数値で着く行が 2 本出た**(六腕で olm119 の 6 本に次ぐ・olm125 は 0): b0_j00 は距離を計算して「Yes! So TcO3 = ThO3」と書くが、JSON の status / proof の欄に至らず、散文の証明は真の前提(半径の平行)と偽の前提(O1Th ∥ O1O2)が混ざる。b2_j09 は証明の欄が数値だけ(「both are sqrt(14.764) ≈ 3.838」)= 六腕で唯一の「証明の欄 = 計算の写し」。どちらも status は hypothesis か none で、正しさを追わない(olm117 §4 と同じ)。
7. **六腕の不変**: 取れない行の形(指示の続き / 上限)・計算すれば退ける(四腕 43 / 47)・status が正しさを追わない、は Tool の段を何にしても動かない。動くのは線対称の率(0.086〜0.318)・計算した率(0.10〜0.30)・名指し(7〜18)で、同じ問いの文の二回(0.225 / 0.086・0.300 / 0.167・18 / 7)の幅は、腕の間の幅と同じ大きさ = **三種の文の並び(宣言 > 指示 > 式だけ)は、この系列の 60 行ずつでは立たない**(olm125 §2 の Fisher のとおり)。

## §5. 主張しないこと

- Q1 の判定は無い(G1 ✗)。参考値 0.086・pool の 0.160・Fisher は記述で、残る / 戻る のどちらも言わない。
- olm125 の 0.225 が「一回の揺れ」とも「指示の効果」とも言わない(三回目で決まらなかった)。
- 指示の文の効果を語の数(reflection が一度多い)と分けない(olm125 §5)。
- b2_j07 の型 0 本を「退けが証明の欄を直した」と読まない(退けた行の 5 / 6 が上限で証明の欄に至っていない)。
- b2_j08 / b1_j13 の繰り返しを「model が迷った」と言わない(退けの文の直後に同じ候補の文が出る、という本文の記述)。
- SUPP_LN / REJ6 / v6 / pool は記述の補助。判定は凍結の v3 と帯。
- 正しさの率は測らない(apex に数値で着いた行の数は記述)。一つの model・一つの温度・60 行。

## §6. 訂正(この読みの際に見つけた前の札の誤り・R4)

- **RESULT olm125 の「EQ(O3 が Tc・Th から等距離・一般には偽)」(§3.2・§4 の 3)は誤り**。等距離 |O3Tc| = |O3Th| は一般の図で**真** = moy-2 の apex(hq の `CAL_APEX_M2` の先頭 `(True, "|O3Tc| = |O3Th|")`・gen.json の EQ 行は `apex: true`・RESULT olm117「apex(等距離)」・RESULT olm119 §4 の 2「等距離(真)に 6 本が数値で着く」)。幾何: O2Tc ⊥ l1・O1Th ⊥ l1 なので Tc・Th は O2・O1 の l1 への足、中点 O3 の足は TcTh の中点 → O3 は TcTh の垂直二等分線上。座標でも 3.8422 / 3.8420。olm125 の判定は変わらない(判定は LN_a と REFL_CALC だけ)。読み「等距離(偽)へ行く = 次の候補も記憶から」は「apex(真)に着くが、等距離を数値で確かめた行は olm125 に 0 で、証明の欄の前提は記憶の線対称(3 本)」に読み替える。RESULT olm125 の末尾に訂正の節を追記(本文は書き換えない)。同じ誤りが写っていた MEMO(factcheck_yt__A1acg0ZTKs §3 / §4)・auto-memory 二本・図解の BRIEF v1 の草稿も同日に直した。
- 誤りの出方(開示): olm117 / olm119 の RESULT では正しく「apex(等距離)」と書いていたのに、olm125 の RESULT(11-04 朝)で類の正誤を手で書く際に取り違え、同日の MEMO と BRIEF にそのまま写した。R4(要約は主張・実出力が証拠)の実例 = 類の正誤は hq の較正の表(実出力)から引くべきで、手で書いた要約を次の文書に写すと誤りが伝播する。

## §7. 次の候補(先生の裁定・起案しない・区切りの後)

- 同じ問いの文の四回目は起案しない(先生「一区切りつけましょう」)。候補として残す物: (a) G1 の較正の引き直し(六腕の実測 0.67〜0.83)か、取れなかった行の形を別に数える設計 / (b) 対照の一行(reflection の語だけ置き宣言も指示もしない)/ (c) v7(「not obvious(ly)」「unclear」の退けの語・olm126 Q3)/ (d) 退けの直後の候補の文を数える計器(b2_j08 / b1_j13 の型 = 「退けた命題と同じ命題が次の候補に出る」率)。
- 系列の一枚の表 = RECORD(同日)。

## 訂正(追記・2026-11-04 午後・R5)

§4 の 4 の「四腕 43 / 47(olm119 11 / 12・olm124 11 / 14・olm125 15 / 15・olm127 6 / 6)」の分母「折り返しを Tc / Th で数値に出した行」は凍結の述語ではない。図解の棚卸し(inventory)の述語(REJ6 ∧ REFL_CALC / REFL_CALC)では olm119 10 / 13・olm124 11 / 15・olm125 15 / 18・olm127 6 / 10 = **42 / 56**(olm119 の退け b2_j08 は REFL_CALC の外)。読み(計算すれば退ける)は変わらないが、43 / 47 の数は据えない。詳細は RECORD の訂正の 3。
- (同・図解の作り手の照合・11-04 午後)§4 の 4 の「olm125 では退けた 15 本のうち証明の欄に至った 9 本の 3 本が線対称に戻った」の 9 本は **8 本**(inventory の `rej6 ∧ has_proof` = b0_j01・b0_j08・b0_j09・b0_j16・b1_j11・b1_j17・b2_j06・b2_j19)。9 は計算した 18 本のうち証明の欄に至った本数(退けていない b1_j04 を含む)。3 本(線対称に戻った)は変わらない。

## 訂正 3(冷間監査 二人・2026-11-04 夜・`cold_audit_publish_prep/RESULT_cold_audit_publish_prep_20261104.md`)
- U1: §3.2 の表「v4 本文 OUTER4_a / _r」の olm124「34 / —」→ **32 / 15**(read.json `Q3_desc.v4_body`・34 は v3 の本文の数)。
- U2: §3.1 の「olm125 の 10 / 40 と Fisher 参考 p 0.56」→ 両側の正確確率は **0.573**(6 / 35 対 10 / 40・主 session の再計算 0.5732)。参考値。
- U3: §3.4 の b1_j13「…の後に『but already checked』542 回」の 542 は句 "but already checked" の回数(内訳 = "…perpendicular…, but already checked" 537・"…passes through O3, but already checked" 4・他 1 = inventory S10 の loop_count と同じ)。引用した二文の組が 542 回並ぶのではない。
- U5(末尾の訂正の補記): 「四腕 43 / 47」の分母 12 / 14 / 15 は olm126 の read.json `Q3.calc_counts`(olm126 の `calc` = 折り返しを接点に当てた計算の行・inventory の REFL_CALC とは別の述語)に在る。「凍結の述語ではない」は言い過ぎで、正しくは **olm126 の凍結の述語の総数の比(分子は全行の REJ6)に olm127 の手の 6 / 6 を足した物**。行の集合(calc ∧ rej6)では olm119 10 / 12・olm124 11 / 14・olm125 14 / 15・olm127 6 / 6 = **41 / 47**。inventory の述語では 42 / 56。どの数も据えず、読み(計算すれば退ける)は変わらない。
