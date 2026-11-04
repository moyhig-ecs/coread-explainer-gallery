HEAD(R1) = dddb7c7a(読みの時の HEAD = YouTube 裏取り MEMO の commit・fetch + pull 済 = Already up to date・origin より 26 commit 先・遅れ 0・本走の発火時の HEAD = 92aac558 = olm124 の凍結の commit = `chain_olm124.log` の一行目)

# RESULT(札 `olm124`・読み 2026-11-04 未明): moy-2 の「折り返しの式」の第二文を外す腕の走らせ直し(d')— **関門 G1 通る(45 / 60 = 0.750・境ちょうど)→ Q1 = 戻る**(証明の欄の線対称 LN_a = 4 / 37 = **0.108**・Δ113 = −0.014・Δ119 = −0.210・予想 戻る 0.57 = 当たり)・**Q2 = 間**(式を数値で使った行 REFL_CALC = 15 / 60 = **0.250**・olm119 0.217・予想 間 0.60 = 当たり)。olm122(関門で判定なし・参考 0.108 / 0.200)と**二回の 60 行が同じ帯に落ちる** = 式そのものは線対称の前提として植わらず、olm119 の +0.196 は第二文(宣言の文)の分(olm119 §4 の 1 を支持)。計器の開示: v3 の LN の形に無い「reflect(ing) Tc across O1O2」(目的語に of が無い)が 3 本あり、足せば 7 / 37 = 0.189(間 の帯の下の境 0.182 の上 0.007 = 一行の幅 0.027 の中)。判定は凍結の v3 で付け(戻る)、どの読みでも olm124 は olm113 の側(olm119 との差 −0.15 以下)。

- PREREG = [PREREG_olm124](PREREG_olm124_moy2_reflection_formula_only_rerun_20261103.md)(凍結 92aac558)・runner = [olm124_…py](../../ConstructGap/exp/olm124_moy2_reflection_formula_only_rerun_20261103.py)(凍結後に触っていない・md5 `06061244…` = gen.json / read.json の provenance と一致)。
- 本走(zebrashark): `chain_olm124.log` = start 11-03 21:35:44 JST(HEAD 92aac558)→ gen rc=0 11-04 00:29:45 → read rc=0 00:29:46。gen の壁時計 10,437.1 s = **2.90 時間**(olm122 2.61・olm119 2.76)・batch 0 / 1 / 2 = seed 20261183 / 84 / 85・各 20 行・batch の壁時計 3,399 / 3,406 / 3,632 s・問いの文 488 token・md5 `2c4a01a4…`(PREREG と一致 = olm122 と逐語同じ)・mlx 0.32.0 / mlx-lm 0.31.3 / transformers 5.14.1。read の provenance の commit は dddb7c7a(発火の後に HEAD が進んだ・runner は不変)。
- 証拠: `ConstructGap/exp/olm124/gen.json`(md5 `de43caa9…`)・`read.json`(md5 `ab5250a8…`)・`gen_run.log`・`read_run.log`・`chain_olm124.log`。
- 判定は `read.json` の値だけ(主 session の読み §4 は値と並べる・判定は変えない)。数の検算 = 凍結の部品(olm122 の `score_row`・olm123 の `score_v5`)を読み込むだけの scratchpad で gen.json の content から数え直し: 取れた行 45・証明の欄 37・LN_a 4(0.1081)・REFL_CALC 15・status 32 = read.json と一致・行ごとの不一致 0。

## §1. 関門

| 関門 | 条件 | 値 | 判定 |
|---|---|---|---|
| G0 | 部品 6 本・比べる元 3 本の md5・較正 12 / 54 / 74・olm113 n_proof 41・olm119 n_proof 44・olm122 取れた 46 / 証明 37 / G1 false | 一致 | ✓ |
| **G1** | conjecture の取れた行 ≥ 0.75(45 / 60) | **45 / 60 = 0.750(境ちょうど)** | **✓** |
| G2(記述の側) | status が hypothesis / question ≥ 0.70(42 / 60) | 32 / 60 = 0.533 | ✗(注記) |

- **G1 は境ちょうど**(開示): 四腕の取れる率 = olm113 50 / 60 = 0.833・olm119 48 / 60 = 0.800・olm122 46 / 60 = 0.767・**olm124 45 / 60 = 0.750**。較正した境 0.75 で通ったが、一行少なければ落ちていた = 関門の境がこの問いの文の族の取れる率の帯(0.75〜0.83・60 行の二項の SE ≈ 0.05)の中にあることは変わらない(R6)。判定は PREREG のとおり付ける(境は凍結の前に置いた・olm122 の落ちを見た後に置き直したことは PREREG §0 で開示済)。式だけの二腕(46・45)が M2A(50)より低く見えるが、2 腕 × 60 行の差 0.07 は SE の中で、記述に留める。
- batch ごと(olm124): 取れた行 16 / 16 / **13**・status none 6 / 8 / **9**・証明の欄 14 / 12 / 11・T の中央値 412.5 / 446.5 / **4,805.5**・上限 2 / 2 / **5**・計算した行 4 / 3 / **8**。olm122 も batch 2(seed 20261182)に偏った(17 / 18 / 11)。偏りの中身が違う: olm122 の batch 2 は指示の続きの短い行、olm124 の batch 2 は**計算して長くなり上限か JSON に至らない行**。
- **取れなかった 15 行の形**(cls NONE・逐語の頭):
  - 問いの文の指示の続きを書く短い行 **6**(T 5〜251): b0_j16「The answer is withheld.」(5)・b1_j02「Then answer a third question: "Is the invariant needed to prove the goal or is it a distractor?" …」(72)・b1_j15「Finally, wrap up your final answer in the JSON object: {"conjecture": …」(150)・b0_j01「Finally, answer two more questions about your proof. (1) Does it use the reflection tool? (2) Is it purely algebraic (coordinates) or geometric (no coordinates)? …」(161・**base が道具の使用を問う指示を自分で続ける**)・b2_j13「The reasoning must be worded simply and clearly. Remain within the scope of the given premises and objects. …」(174)・b0_j03「Finally, state the figure's TYPE: "triangle", "hyperbola", …」(251)。
  - 上限 12,288 の **8**: b0_j05「Write your reasoning step-by-step in plain text. ⏎ Okay, let's see. …」・b1_j08「Do not provide any explanation other than the JSON. ⏎ Okay, let's see. …」・b1_j17「Then answer the auxiliary questions. (3) How does this invariant help solve the problem? …」・b2_j06「Now use your invariant to answer the following question: **Find a point P (in terms of the given objects) that is always collinear with Tc and Th.** …」・b2_j08「Then comment on the correctness and completeness of the answer …」・b2_j12「Then answer two more questions about the proof. (1) What are its TYPE and STRATEGY? …」・b2_j15「Then answer three more questions. (3) What is the INTERPRETATION of the invariant …」・b2_j16「Output only the JSON object, nothing else. ⏎ Let me restate the configuration: …」= 指示の続きの後に考え始めて JSON に至らない(**うち 4 本 b0_j05・b2_j08・b2_j12・b2_j15 は式を数値で使った計算した行**)。
  - 中間 **1**: b2_j18(T 5,906)= 指示の続き「Finally, answer a third question about your invariant. (3) Is it a definition or a theorem? …」の後に折り返しを計算して退け、「the key invariant here is the equidistance of O3 from both tangent points … The reflection tool provided relates to the symmetry across the line of centers」と散文で結んで JSON に至らない。
  - 四腕の形は同じ(指示の続き / 上限)で、配分が違う: olm113 = 短 5・中 1・上限 4 / olm119 = 短 9・中 1・上限 2 / olm122 = 短 10・上限 4 / **olm124 = 短 6・中 1・上限 8**。上限の行 9 本(取れた b0_j14 を含む)は四腕で最多(olm113 5・olm119 6・olm122 5)。
- G2 の注記: status の取れた率 0.533 は四腕で最低(olm113 0.700・olm119 0.717・olm122 0.583)。取れた 45 行のうち status none が **8 行**(b0_j10・b0_j14・b1_j04・b1_j06・b1_j07・b1_j19・b2_j09・b2_j17 = JSON の conjecture までは書くが status / proof の欄に至らない)・other 5。

## §2. Q1・Q2 — 判定

| Q | 問い | 値 | 帯 | 判定 | 予想 |
|---|---|---|---|---|---|
| **Q1(主)** | 証明の欄の LN_a の率 r | **4 / 37 = 0.108**・Δ113 = −0.014・Δ119 = −0.210 | 戻る(\|Δ113\| < 0.06) | **戻る** | 戻る 0.57 = **当たり** |
| Q2 | 本文で式を数値で使った率 | **15 / 60 = 0.250**(olm119 13 / 60 = 0.217・olm122 12 / 60 = 0.200) | 間(0.10 < r < 0.30) | **間** | 間 0.60 = **当たり** |

- olm122(参考)と同じ帯: Q1 0.108 / 0.108・Q2 0.200 / 0.250。二回の 60 行で同じ所に落ちた。
- **Q1 の計器の開示(R6・判定は変えない)**: v3 の LN の 4 本の内訳と、v3 の形に無い文:
  - v3 が数えた 4 本: b0_j02(「symmetry of the configuration about the line O1O2 … reflecting Tc across O1O2 results in Th」= 本物)・b0_j19(「symmetric with respect to the line joining the centers O1 and O2」= 本物・ただし続きで軸を垂直二等分線にも替える)・**b1_j01(「P' = 2F − P is the reflection of P across O1O2. Applying this to Th …」= 式の写しで Tc ↔ Th の対称は言っていない = 拾いすぎの候補)**・b2_j07(「symmetric with respect to the line O1O2」= 本物・計算で退けた後)。
  - **v3 の形に無い 3 本**: b0_j00「Reflecting Th over O1O2 yields Tc due to circle symmetry」・b0_j17「Reflect O3 across the line O1O2 … the reflection swaps the contact points Tc↔Th」・b2_j05「Because reflecting Tc across O1O2 gives Th」。v3 の `_LN[1]` は `reflect\w*\s+(?:of\s+…)?(?:over|across|…)\s+O1O2` で、**目的語が of 無しで直に来る「reflect(ing) Tc across O1O2」を拾わない**(olm118 の較正例 l02「reflections across the line」・l04「mirror images over O1O2」は目的語なし)。
  - 同じ形を四腕の証明の欄に当てると(参考): olm113 5 / 41 = 0.122(+0)・olm119 15 / 44 = 0.341(+1・b2_j13)・olm122 5 / 37 = 0.135(+1・b1_j11)・**olm124 7 / 37 = 0.189(+3)**。読みの幅 = 拾いすぎ 1 本を外し取りこぼし 3 本を足すと 6 / 37 = 0.162(戻る)・足すだけなら 0.189(間 の下の境の上 0.007 = 一行の幅 0.027 の中)。**どの読みでも olm124 は olm113 の側で、olm119(0.318 / 0.341)との差は −0.15 以下**。判定は凍結の v3 の値(0.108・戻る)で付け、取りこぼしの形は v6 の材料(§6)。

## §3. Q3 — 記述(四腕の値)

### 3.1 証明の欄(空でない行)

| | olm113(M2A) | olm119(式 + 第二文) | olm122(式だけ・参考) | **olm124(式だけ・再走)** |
|---|---|---|---|---|
| n_proof | 41 | 44 | 37 | **37** |
| LN_a(線対称・肯定) | 5(0.122) | 14(0.318) | 4(0.108) | **4(0.108)** |
| PT_a(点対称) | 0 | 0 | 0 | **1**(b0_j11) |
| PAR3_a | 7 | 3 | 3 | **3** |
| PERP3_a | 4 | 10 | 5 | **7** |
| PBIS3_a | 0 | 0 | 1 | **0** |
| OUTER_a(外接線の印) | 10(0.244) | 12(0.273) | 9(0.243) | **9(0.243)** |
| SYMM(対称の語) | 11(0.268) | 22(0.500) | 13(0.351) | **15(0.405)** |
| kind | — 30・NONE 6・LN 5 | (RESULT olm119) | — 24・NONE 7・LN 4・OTH 2 | **— 22・NONE 10・LN 4・PT 1** |

- 類ごと(olm124・証明の欄): EQ n 8 = LN 1・OUTER 1 / MIDO3 n 21 = LN 3・OUTER 7 / OTHER n 8 = LN 0・OUTER 1(olm122: EQ 9 = LN 1・OUTER 1 / MIDO3 22 = LN 2・OUTER 6 / OTHER 6 = LN 1・OUTER 2)。
- v5(olm123・参考): 証明の欄 PAR5 **3** / OUTER5 **9** = v3 と同じ(落とし 0・olm122 では落とし 1)。
- **点対称が証明の欄に 1 本**(b0_j11「the symmetry of the configuration implies that the points Tc and Th are symmetric with respect to O3」)= 四腕で初(olm117 の等しい半径の図で 0 → 4 / 46 に増えた形が、式だけの腕にも 1 本)。
- 線対称の 4 本 + 形に無い 3 本 = 「式だけでも植わる行」は 60 行に 4〜7 本(olm122 の 3〜4 本と同じ水準)。

### 3.2 行(n = 60)

| | olm113 | olm119 | olm122 | **olm124** |
|---|---|---|---|---|
| 取れた行 | 50 | 48 | 46 | **45** |
| 類 MIDO3 / EQ / OTHER / NONE | 17 / 16 / 17 / 10 | 29 / 8 / 11 / 12 | 27 / 12 / 7 / 14 | **23 / 12 / 10 / 15** |
| MIDO3 の率(取れた行) | 0.34 | 0.604 | 0.587 | **0.511** |
| EQ の率(取れた行) | 0.32 | 0.167 | 0.261 | **0.267** |
| status hypothesis + question | 42 | 43 | 35 | **32** |
| T の中央値 | 1,068.5 | 440 | 576 | **661.5**(取れた行 499・取れない行 12,288) |
| 上限 12,288 | 5 | 6 | 5 | **9** |
| REFL_MENTION | — | 31 | 25 | **28** |
| REFL_CALC | — | 13 | 12 | **15** |
| tool_named | — | 13(別の数え方) | 11(計算 7・しない 4) | **11**(計算 10・しない 1 = b1_j08) |

- MIDO3 の率 0.511 は olm119 / olm122(0.604 / 0.587)より少し低いが olm113(0.34)より高い = **道具の存在だけで共線の conjecture が増える**は二回目も見える(幅は一行 0.022 で 3〜4 行の差)。EQ は olm122 と同じ(0.267 / 0.261)。
- 本文(v3・n 60): LN_a 24・PT_a 8・OUTER_a 34・PAR3 24・PERP3 29・PBIS3 6・SYMM 42(olm122 23・10・31・16・23・3・39・olm113 11・7・—・23・22・1・26)。
- 本文(v4・RETR): LN 24 / 退け **11**・PT 8 / 1・PAR4 20 / 13・PERP3 29 / 11・PBIS4 6 / 0・OUTER4 32 / 15(olm122 は LN 23 / 退け 2・olm119 33 / 9)。退けが olm122 より多く拾われたのは、今回の計算した行の退けの文が当たりの後 260 字の窓に入ったため(計器は同じ・§4 の 4)。

### 3.3 計算した行 / しない行

| | 計算した(REFL_CALC) | しない |
|---|---|---|
| n | **15**(b0 4・b1 3・b2 8) | 45 |
| 類 | EQ 8・MIDO3 1・OTHER 1・NONE 5 | MIDO3 22・EQ 4・OTHER 9・NONE 10 |
| 本文の LN_a / 退け(v4) | 14 / **10** | 10 / 1 |
| 証明の欄の LN_a | 1(b2_j07) | 3 |
| T の中央値 | 8,849(最小 3,571) | 405 |
| 上限の行 | 4(b0_j05・b2_j08・b2_j12・b2_j15) | 5(b0_j14・b1_j08・b1_j17・b2_j06・b2_j16) |

- 計算する行は EQ(O3Tc = O3Th)に偏る(8 / 15 = olm122 8 / 12・olm119 と同じ)。
- **Tc / Th を O1O2 で折り返して数値を出した行は 13 / 15**(b2_j08 は O3 の折り返しと中点・b2_j19 は相似の中心 H)。**そのうち 12 本が「Not the same / is not Th / doesn't match」と逐語で書く**(b1_j05 は窓に無い・垂直二等分線の計算に移る)。olm122 では 12 本のうち 6 本。
- 計算した 15 本のうち JSON に至らない NONE が 5(olm122 は 1)= 計算すると長くなり、上限か散文で終わる。

### 3.4 逐語(Q4)

**証明の欄の線対称(v3 の 4 本・全部)**:
- b0_j02 [MIDO3・計算なし・T 455]: 「The points Tc, O3, and Th lie on a line due to the symmetry of the configuration about the line O1O2. Since O3 is the midpoint of O1 and O2, reflecting Tc across O1O2 results in Th, which implies that Tc, O3, and Th are collinear.」= 第二文なしでも(olm122 の b0_j04 と同じ型)。
- b0_j19 [MIDO3・計算なし・T 325]: 「The inner tangent line l1 connecting Tc and Th is symmetric with respect to the line joining the centers O1 and O2. O3, being the midpoint of O1 and O2, lies on the perpendicular bisector of the segment joining O1 and O2. Since Tc and Th are points where the inner tangent intersects the circles, they must lie on the line that is symmetric about the perpendicular bisector, meaning they are collinear with O3.」= 軸が O1O2 と垂直二等分線の間で揺れる。
- b1_j01 [MIDO3・計算なし・T 836]: 「Let F = O1 + t(O2 − O1) be the foot of the perpendicular from P to O1O2. Then P' = 2F − P is the reflection of P across O1O2. Applying this to Th, we get Th' = 2F − Th. But since Tc and Th are contact points of the inner common tangent, the line TcTh is perpendicular to O1O2, so F is the midpoint of TcTh. Therefore O3, as the midpoint of O1O2, is also the midpoint of TcTh.」= **式を証明の欄に写し、Tc ↔ Th の対称は言わず、結論は記憶(TcTh ⊥ O1O2)で埋める**(olm122 の b1_j10 と同じ型・v3 は式の写しを LN と数える)。
- b2_j07 [EQ・**計算した**・T 4,053]: 「By the symmetry of the configuration, the distances from O3 to Tc and Th are equal. This follows because the configuration is symmetric with respect to the line O1O2, and the inner common tangent is equidistant from both centers.」= 本文で「Step 18. Revisiting the reflection tool … If we reflect Tc across O1O2, do we get Th? Let's check. … P' = (4.9316, -6.1025) This is not Th.」と退けた後、証明の欄で軸を替えずに線対称を書く(olm119 の b1_j06 / b2_j16 と同じ型 = 結論は数値で直り理由は記憶で埋まる・olm122 の b2_j07 は軸を垂直二等分線に替えた)。

**v3 の形に無い線対称(3 本・全部)**:
- b0_j00 [MIDO3・T 221]: 「Let M be the midpoint of TcTh. The line O1O2 passes through O3. Reflecting Th over O1O2 yields Tc due to circle symmetry. Thus M lies on O1O2 and also on TcTh, making TcThO3 collinear.」
- b0_j17 [MIDO3・T 279]: 「Reflect O3 across the line O1O2 to obtain O4. Since O3 is the midpoint of O1O2, O4 coincides with O3. Under this reflection, circle c (center O2) maps to circle h1 (center O1), and the inner tangent line l1 maps to itself. Hence the reflection swaps the contact points Tc↔Th. …」= 式の「reflect across O1O2」を段取りに写し、円が入れ替わる(偽)を記憶で足す。
- b2_j05 [OTHER・T 341]: 指示の続き「Example of an acceptable answer: {"conjecture": "Chord TcTh is parallel to O1O2", … "proof": "Because reflecting Tc across O1O2 gives Th, the segment TcTh is perpendicular to O1O2, which means the chord is parallel to O1O2 …"}」= base が「答えの例」を自分で書き、その中に線対称と外接線の記憶を並べる。

**点対称(1 本)**: b0_j11 [MIDO3・計算なし・T 253]: 「The inner common tangent of two circles is perpendicular to the line joining their centers. Given that O3 is the midpoint of O1O2, the symmetry of the configuration implies that the points Tc and Th are symmetric with respect to O3. Therefore, the points Tc, Th, and O3 must lie on the same straight line.」

**計算した行(15 本のうち 10 本・折り返しの計算と結果の文)**:
- b0_j05 [NONE・上限]: 「Let's try reflecting Tc across the line O1O2 and see if it gives Th. Let's compute F for P = Tc.」→「≈ (4.9316, -6.1025). This is not Th (7.6927, -3.2647). So the reflection of Tc across …」→ 相似・平行・共線を順に数値で退け、上限。
- b0_j06 [EQ・T 3,571]: 「Let's try the reflection tool: Reflect O3 across O1O2. … So t = 84.635 / 169.178 ≈ 0.500 … which is exactly O3. So, reflecting O3 across O1O2 gives O3 itself.」→「check if Tc and Th are symmetric with respect to O1O2, i.e., if O3 is the midpoint of TcTh. Midpoint of TcTh: (5.23025, -0.9981), which is not O3.」→「= (4.9416, -6.1025) Compare to Th = (7.6927, -3.2647). Not the same.」= 線対称を「O3 が中点」に読み替えてから折り返しも計算して退ける。
- b0_j07 [EQ・T 7,291・conj「O3 is collinear with the midpoint of TcTh and lies on the perpendicular bisector of TcTh」]: 「So reflection of Th over O1O2 is not Tc. So that's not the case.」/ 垂直二等分線は「So y≈-1.388 -1 = -2.388. The actual y-coordinate of O3 is -2.3865, which is very close. … So O3 lies on the perpendicular bisector of TcTh.」= 真の等距離に数値で着く。
- b0_j10 [EQ・T 6,201]: 「reflecting Tc over O1O2 might give Th, or something like that. Let's try.」→「reflection of Tc over O1O2 is not Th. Therefore, that approach doesn't seem to work.」
- b1_j04 [EQ・T 9,128]: 「reflecting Th across O1O2 gives Tc, or vice versa. Let's check.」→「Compare this to Tc, which is (2.7678,1.2685). Not the same. So reflection of Th across O1O2 is not Tc. Similarly, if we reflect Tc across O1O2 … Not the same. So reflection of Tc is not Th.」= 両向きを計算して退ける。
- b1_j07 [EQ・T 10,268]: 「Maybe the tangent points Tc and Th are reflections of each other across O1O2? If that's the case, then the midpoint of Tc and Th would lie on O1O2.」→「Compare this to Th (7.6927, -3.2647). Not the same. So reflecting Tc across O1O2 doesn't give Th.」
- b2_j07 [EQ・T 4,053]: 上の証明の欄の 4 本目。「Step 11. Reflecting Tc across O3 to see if it lands on Th … This is not Th.」(点対称を先に退け)→「Step 18. … P' = (4.9316, -6.1025) This is not Th.」(線対称も退け)→ 証明の欄は線対称。
- b2_j11 [MIDO3・T 10,508]: 「These slopes are not equal, so Tc, O3, Th are not collinear.」…「But Tc' has y≈-6.1045, which doesn't match. So not on the line.」→ **conjecture は「Tc, O3, Th are collinear」= 数値で退けた命題を conjecture に書く**(olm119 の b0_j13 と同じ型)。
- b2_j12 [NONE・上限]: 「if we reflect Th across O1O2, does it land on Tc? Let's compute the reflection of Th using the formula given.」→「Compare this to Tc, which is (2.7678, 1.2685). Not the same. So reflection of Th across O1O2 is not Tc. So maybe that's not the invariant.」
- b2_j18 [NONE・T 5,906]: 「Compare this to Tc, which is (2.7678, 1.2685). Not the same. So Th reflected over O1O2 is not Tc. So that's not the case.」→ 散文で「the key invariant here is the equidistance of O3 from both tangent points」と結び JSON なし。
- 残り 5: b1_j05 [EQ・4,081](垂直二等分線を計算「Which matches O3's y-coordinate (-2.3865). So yes! O3 lies on the perpendicular bisector of TcTh」)・b2_j03 [OTHER・8,849](折り返しを計算し「Maybe I made a calculation error」)・b2_j08 [NONE・上限](O3 の折り返しと中点・「-3.655 ≠ -1.090, so O3 does NOT lie on TcTh」)・b2_j15 [NONE・上限](「Not the same. So reflection of Tc is not Th. Similarly, reflec…」)・b2_j19 [EQ・5,558](相似の中心「if H were O3, the ratio would be 1, which doesn't match. Therefore, H is not O3」)。

**式に触れたが計算しない行(13 本のうち 5 本)**:
- b0_j08 [EQ・T 2,213]: 「Let's try the reflection tool. … Let's try to reflect O3 across O1O2. O3 is the midpoint of O1 and O2, so its reflection should be itself. Alternatively, perhaps the line TcTh is parallel …」= 道具を名指し、計算せず記憶で済ませる。
- b0_j09 [MIDO3・T 1,212]: 「the configuration is symmetric with respect to the line O1O2, and the points Tc and Th are reflections of each other over O1O2, so their midpoint is O3.」(本文)→ 証明の欄は「the vectors from O1 to Tc and from O2 to Th are parallel and in the same direction」= 本文の線対称が証明の欄では平行に替わる。
- b1_j03 [OTHER・T 405]: 「"construction": "Reflect Th across O1O2 to get Th'. Then TcTh' is a diameter of h1 and thus perpendicular to O1Th', which is parallel to O1O2."」= 道具を作図の段に使う(結果は記憶)。
- b2_j14 [MIDO3・T 349]: 「By reflecting O1 across O1O2, we obtain a point O'1 such that the line O'1Tc is parallel to O1Th.」= O1 は軸の上(動かない)= 式は読まれていない(olm122 の b0_j08 と同じ混同)。
- b2_j17 [OTHER・T 499]: 「… follows from the construction of O3 as the midpoint of O1 and O2 and the reflection of Tc and Th across O1O2.」→ conjecture「O1, O2, Tc, Th are concyclic」。

## §4. 読み(主 session・値と並べる・判定は変えない)

1. **判定 = 戻る・二回の 60 行が同じ値**(olm122 参考 0.108・olm124 0.108)。olm113 → olm119 の +0.196 は式ではなく第二文(宣言の文「Two points are symmetric … exactly when …」)が植えた、という olm119 §4 の 1 の読みを、新しい 60 行の判定として支持する。式(第一文)だけの腕は olm113 の M2A と同じ水準に留まる。
2. **計器の取りこぼし**(R6・開示): 「reflect(ing) Tc across O1O2」(目的語に of 無し)を v3 の LN が拾わない。olm124 に 3 本・olm119 / olm122 に 1 本ずつ・olm113 に 0。足した読み(0.189)は 間 の境の上 0.007 で、一行の幅(0.027)の中。判定は凍結の v3 で付け、**どの読みでも olm124 は olm113 の側**。式の写し(b1_j01)を LN と数える拾いすぎも 1 本。v6 の材料(§6)。
3. **式だけでも植わる行はある**(60 行に 4〜7 本 = olm122 の 3〜4 本と同じ水準): 「Reflecting Th over O1O2 yields Tc」(b0_j00)・「reflecting Tc across O1O2 results in Th」(b0_j02)・「the reflection swaps the contact points Tc↔Th」(b0_j17)。道具の見出しだけで線対称の記憶が呼ばれる行が一定数あり、olm119 の 14 本との差が第二文の分。
4. **計算した行は退ける**: 折り返しを数値で出した 13 本のうち 12 本が「Not the same / is not Th / doesn't match」と書く(olm122 は 12 本のうち 6 本)。v4 の RETR が今回 10 本拾ったのは退けの文が窓(260 字)に入ったからで、計器は同じ。退けは「計算の結果の文」で読むべき(olm122 §4 の 5 と同じ)。
5. **退けた後に証明の欄で線対称**(b2_j07): 点対称(Step 11)と線対称(Step 18)を両方数値で退けた行が、証明の欄で「symmetric with respect to the line O1O2」を軸を替えずに書く = olm119 の 3 本(b1_j06・b2_j16)と同じ型。olm122 の b2_j07(軸を垂直二等分線に替える)と合わせ、**計算で退けても証明の欄は記憶で埋まる**が二腕で見えた。
6. **退けた命題を conjecture に**(b2_j11): 傾きで「not collinear」と書いた後 conjecture「Tc, O3, Th are collinear」= olm119 の b0_j13 と同じ型。
7. **MIDO3 の増えは式だけで二回**(0.587 / 0.511・olm113 0.34)。二回目は 3〜4 行低いが帯は同じ。EQ は二回とも 0.26 台。
8. **計算すると JSON に至らない**: 計算した 15 本のうち NONE 5(上限 4 + 散文 1)。上限の行 9 本は四腕で最多で、batch 2 の T 中央値 4,805 が示すとおり計算する行が長い。取れる率 0.750(境ちょうど)の下がりはこの側(短い指示の続きは 10 → 6 に減った)。
9. **点対称が証明の欄に初めて 1 本**(b0_j11)。olm117(等しい半径)で増えた形が式だけの腕でも出る = 道具の存在が「対称」の語を呼び(SYMM 0.405・olm113 0.268)、その中身が線 / 点に分かれる。

## §5. 主張しないこと

- 判定は v3 の値(0.108)で付け、§2 の取りこぼしを足した 0.189 は参考。計器の形を直した判定は v6 の凍結の後。
- G1 が境ちょうど(0.750)だったことは開示するが、判定は PREREG の条件で付ける。式だけの二腕の取れる率が M2A より低いとは言わない(差 0.07・SE 0.05)。
- 計算した行の「違う」の 12 本は主 session の逐語の読み(窓 700 字の正規表現)で、計器(RETR)の値ではない。
- 一つの model・一つの温度・60 行。正しさの率は測らない。pool 120 行(olm122 + olm124)は参考(取れた 91 / 120・証明 74・LN 8 = 0.108・REFL_CALC 27 = 0.225・MIDO3 0.550・EQ 0.264・PERP3 12・OUTER 18・T 622・上限 14・帯で言えば 戻る)で、olm122 の関門の結果を覆さない。

## §6. 次の候補

- **(e)「使って確かめよ」の腕 = olm125**(先生「(d) (e) (f) へ順次進みます。」の (e)・土台は (d') が 戻る なので**式だけ + 指示**): olm124 の問いの文(M2A + TOOL_D)の TOOL の段に「使って確かめよ」の一行を足し、60 行。Q = 計算した率(REFL_CALC・olm124 0.250 → 上がるか)・証明の欄の線対称(0.108 → 下がるか・計算した行は退けるので)・退けた後に証明の欄で書く行(b2_j07 の型)の数。G1 ≥ 0.75(同じ較正)。計器は olm122 の score_row を読み込むだけ + 計算の結果の文で退けを読む補助(記述)。
- v6 の材料(起案しない): 「reflect(ing) <点> across O1O2」(of 無し)を LN に足す・式の写し(P' = 2F − P is the reflection of P across O1O2)を LN から分ける・退けは計算の結果の文で読む・接続詞の後の主語(olm123)・軸を替えた対称(olm122)。
