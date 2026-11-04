HEAD(R1) = 109d26bf(読みの時の HEAD = Qwen R3〜R5 の MEMO 追記の commit・fetch + pull 済 = Already up to date・origin より 29 commit 先・遅れ 0・本走の発火時の HEAD = a18c3857 = olm125 の凍結の commit = `chain_olm125.log` の二行目)

# RESULT(札 `olm125`・読み 2026-11-04 朝): moy-2 の「使って確かめよ」の腕(e)— 式だけの問いの文(olm124)の Tool の段に指示の一行「Use it to check: compute the reflection with the given coordinates before you rely on it.」を足した 60 行。**関門 G1 通る(45 / 60 = 0.750・境ちょうど・olm124 と同じ)→ Q2(主)= 変わらない**(本文で式を数値で使った行 REFL_CALC = 18 / 60 = **0.300**・olm124 0.250・Δ = +0.050・予想 上がる 0.60 = **外れ**・変わらない の予想 0.37)・**Q1 = 上がる**(証明の欄の線対称 LN_a = 9 / 40 = **0.225**・olm124 0.108・Δ124 = **+0.117**・帯の境 +0.06 = 7 / 40 の上 2 行・予想 変わらない 0.50 = **外れ**・上がる の予想 0.15)。指示の一行は**計算を増やさず(15 → 18 本)、道具の名指しを増やし(tool_named 11 → 18)、証明の欄の線対称を増やした**。増えた線対称は**計算しない行**に在る(計算しない行の証明の欄 3 / 30 = 0.100 → 7 / 31 = 0.226・計算した行 1 / 7 → 2 / 9)= PREREG §3 の読みの軸の三つ目(「指示が reflection の語を一度多く置くことで線対称の記憶が増える = 植える効果の別経路」)の側。三種の文の並び(参考)= 宣言の文(olm119)0.318 > 指示の文(olm125)**0.225** > 式だけ(olm122 / olm124)0.108 / 0.108 ≈ 道具なし(olm113)0.122。ただし 60 行ずつでは 0.225 は両隣と分けられない(Fisher 参考: 対 olm124 0.23・対 式だけ pool 120 行 0.11・対 olm119 0.46)= 判定は帯で付け(上がる)、大きさの読みは走らせ直しが要る(§6)。

- PREREG = [PREREG_olm125](PREREG_olm125_moy2_reflection_use_to_check_20261104.md)(凍結 a18c3857・G10 の台帳に記入済)・runner = [olm125_…py](../../ConstructGap/exp/olm125_moy2_reflection_use_to_check_20261104.py)(凍結後に触っていない・md5 `e1c2f85d…` = gen.json / read.json の provenance と一致)。
- 本走(zebrashark): `chain_olm125.log` = queued 11-04 00:49:50(Qwen 0.8B の R3〜R5 の鎖の後ろに)→ start 01:18:51 JST(HEAD a18c3857)→ gen rc=0 04:09:15 → read rc=0 04:09:15。gen の壁時計 10,219.6 s = **2.84 時間**(olm124 2.90・olm122 2.61・olm119 2.76)・batch 0 / 1 / 2 = seed 20261186 / 87 / 88・各 20 行・batch の壁時計 3,382 / 3,431 / 3,406 s・問いの文 **506 token**(olm124 488・TOOL_U の分)・md5 `718d1601…`(PREREG と一致・`tool_u` の逐語も gen.json に)・mlx 0.32.0 / mlx-lm 0.31.3 / transformers 5.14.1。read の provenance の commit は 109d26bf(発火の後に HEAD が進んだ・runner は不変)。Traceback 0(gen / read)。
- 証拠: `ConstructGap/exp/olm125/gen.json`(md5 `32a0298a…`)・`read.json`(md5 `d0171213…`)・`gen_run.log`・`read_run.log`・`chain_olm125.log`。
- 判定は `read.json` の値だけ(主 session の読み §4 は値と並べる・判定は変えない)。数の検算 = 凍結の部品(olm122 の `score_row`・olm123 の `score_v5`)を読み込むだけの scratchpad で gen.json の content から数え直し: 取れた行 45・証明の欄 40・LN_a 9(0.225)・REFL_CALC 18・status 37 = read.json と一致・**行ごとの不一致 0**。四腕の並べ直し(§3.3・§2 の開示)も凍結の述語(olm122 `score_row`・olm125 `supp_ln` / `rej`)を読み込むだけで、olm124 の RESULT に手で書いた四腕の値(5 / 41・15 / 44・5 / 37・7 / 37)と一致。

## §1. 関門

| 関門 | 条件 | 値 | 判定 |
|---|---|---|---|
| G0 | 部品(olm122・olm124 とその下 5 本)・比べる元 5 本の md5・較正 12 / 54 / 74 + SUPP / REJ 15 / 15・olm113 n_proof 41・olm119 n_proof 44・olm124 取れた 45 / 証明 37 / LN 0.1081 / RC 0.25 / G1 true / 判定 戻る | 一致 | ✓ |
| **G1**(Q1 だけ) | conjecture の取れた行 ≥ 0.75(45 / 60) | **45 / 60 = 0.750(境ちょうど)** | **✓** |
| G2(記述の側) | status が hypothesis / question ≥ 0.70(42 / 60) | 37 / 60 = 0.617 | ✗(注記) |

- **G1 は二回続けて境ちょうど**(開示): 五腕の取れる率 = olm113 0.833・olm119 0.800・olm122 0.767・olm124 0.750・**olm125 0.750**。一行少なければ落ちていた。この問いの文の族の取れる率は 0.75〜0.83(60 行の二項の SE ≈ 0.05)で、境 0.75 はその下端に在る = 次の札でも G1 は「通るか落ちるか」が半々に近い(R6・§6)。判定は PREREG のとおり付ける。
- batch ごと(olm125): 取れた行 18 / 13 / 14・status none 5 / 8 / 7(other 1 / 1 / 1)・証明の欄 15 / 12 / 13・証明の欄の LN 3 / 4 / 2・T の中央値 **1,292** / 367.5 / 394・上限 1 / 3 / 2・計算した行 7 / 7 / 4。三 batch とも証明の欄の LN は 2 本以上(一つの batch の偏りではない)。batch 0 の T の中央値が高いのは計算した行 7 本のうち上限が 1 本だけで、長いまま JSON に至った行が多いため。
- **取れなかった 15 行の形**(cls NONE・逐語の頭・全部): 
  - 問いの文の指示の続きを書く短い行 **10**(T 11〜257): b2_j03「Only respond with the JSON object, no other text.」(11)・b1_j08「Finally, respond with the JSON object only. No other text.」(13)・b1_j14「Finally, respond with the JSON object. ⏎ Do not copy-paste your answer, but edit it in a new session.」(24)・b0_j17「After that, answer two more questions about your proof. (1) What is the domain? (2) What is the codomain? ⏎ The answer is withheld.」(33)・b0_j00「Do not say anything about your reasoning except in plain text. Do not refer to your reasoning in the JSON object. Do not claim the invariant holds because the reasoning shows it; you must appeal to the configuration. …」(51)・b1_j03「Do not add any remarks, explanations, or other text. Just the JSON. ⏎ The key invariant is that the three points O3, Tc, and Th are collinear …」(94・散文で MIDO3 を書くが JSON に至らない)・b2_j09「Then give a single relevant question (open or closed) whose ANSWER is the invariant, as a relation. …」(150)・b2_j17「Finally answer one more question: rewrite the invaraint in geometry language, …」(157)・b2_j00「After that, answer two more questions about your invariant. (1) Is it a HYPOTHESIS or a QUESTION? (2) Give its backing: a proof that it holds. …」(190・続きで「the line O3Tc is perpendicular to O1O2 … because the reflection of Tc across the line O1O2 yields Th」と散文)・b1_j00「The response must be self-contained and not reference this chat session. Put the JSON object at the top, and your reasoning in a code block below it. …」(257・JSON の conjecture「Tc, Th, and O3 are collin…」を書き始めて止まる)。
  - 上限 12,288 の **5**(全部が式を数値で使った**計算した行**): b1_j15「Finally, write the conclusion in this format: ⏎ Conclusion: _____ invariant is generally true. …」・b1_j16「Then stop. ⏎ Okay, let's try to figure out the invariant here. …」・b1_j19「After that, answer one more question about your invariant. (3) Is it a LEAN theorem? …」・b2_j02「The following is a summary of what I found. It will also serve as a check for the reader. ⏎ The answer is withheld. …」・b2_j04「Use no symbols for objects (O1, etc.) and no parentheses. … All configurations can be explored interactively at https://mathpix.com/cermath/…」= 指示の続きの後に考え始め、計算して、JSON に至らない。
  - 中間(散文で結ぶ)**0**(olm124 は 1)。
  - 五腕の形は同じ(指示の続き / 上限)で配分が違う: olm113 = 短 5・中 1・上限 4 / olm119 = 短 9・中 1・上限 2 / olm122 = 短 10・上限 4 / olm124 = 短 6・中 1・上限 8 / **olm125 = 短 10・上限 5**。上限の行は全部で 6 本(取れた b0_j09 を含む・olm124 9・olm119 6・olm122 5・olm113 5)。
- G2 の注記: status の取れた率 0.617(olm113 0.700・olm119 0.717・olm122 0.583・olm124 0.533)。取れた 45 行のうち status none が **5 行**(b0_j11・b0_j14・b0_j15・b1_j18・b2_j10 = JSON の conjecture までは書くが status / proof の欄に至らない・うち 4 本は計算した行)・other 3(b0_j04・b1_j11・b2_j06)。

## §2. Q2・Q1 — 判定

| Q | 問い | 値 | 帯 | 判定 | 予想 |
|---|---|---|---|---|---|
| **Q2(主)** | 本文で式を数値で使った率 rc = REFL_CALC / 60 | **18 / 60 = 0.300**(olm124 15 / 60 = 0.250・olm122 0.200・olm119 0.217) | 変わらない(0.10 < rc < 0.40)・上がる の境 24 / 60 まで **6 行** | **変わらない** | 上がる 0.60 = **外れ**(変わらない 0.37) |
| Q1 | 証明の欄の LN_a の率 r・Δ124 = r − 0.108 | **9 / 40 = 0.225**・Δ124 = **+0.117**・Δ113 = +0.103・Δ119 = −0.093 | 上がる(Δ124 ≥ +0.06 = 7 / 40 以上)・境の上 **2 行** | **上がる** | 変わらない 0.50 = **外れ**(上がる 0.15) |

- 予想は二つとも外れた。Q2 は「計算の指示は半分前後は従われる」と見た(0.25 → 0.40〜0.60)が、増えたのは 3 行。Q1 は「率は動きにくい」と見た(0.50)が、+0.117(帯の境の約 2 倍)。
- olm124 の帯(参考・`_verdict1`): olm113(0.122)と olm119(0.318)の**間**(|Δ113| ≥ 0.06 かつ |Δ119| ≥ 0.06)。
- **Fisher の正確検定(参考・PREREG に無い・判定に使わない)**: 証明の欄の LN 9 / 40 対 olm124 4 / 37 = p 0.23・対 式だけ pool 120 行(olm122 + olm124)8 / 74 = p 0.11・対 olm119 14 / 44 = p 0.46。REFL_CALC 18 / 60 対 15 / 60 = p 0.68。= 60 行ずつでは 0.225 は 0.108 とも 0.318 とも分けられない。**判定は凍結の帯**(上がる・境の上 2 行)で付け、大きさの読み(§4 の 2)は走らせ直しの後(§6)。
- **Q1 の計器の開示(R6・判定は変えない)**: v3 の LN 9 本の内訳は §3.4(全部が Tc ↔ Th の O1O2 についての対称を肯定して述べる本物・olm124 の b1_j01 のような式の写しは 0)。v3 の形に無い直の目的語「reflect(ing) <点> across / over O1O2」(SUPP_LN・凍結の補助)は証明の欄に 4 本(b0_j12・b1_j07・b1_j11・b1_j12)、うち v3 が既に拾う 2 本を除いて **+2**(b0_j12「reflecting Th across O1O2 to Tc」・b1_j11「reflecting Tc over O1O2 yields Th」)= 足せば 11 / 40 = **0.275**。五腕に同じ凍結の述語を当てると(参考): olm113 5 / 41 = 0.122(+0)・olm119 15 / 44 = 0.341(+1)・olm122 5 / 37 = 0.135(+1)・olm124 7 / 37 = 0.189(+3)・**olm125 11 / 40 = 0.275(+2)**。どの読みでも olm125 は olm124 の上(+0.086〜+0.117)で olm119 の下(−0.066〜−0.093)。

## §3. Q3 — 記述(五腕の値)

### 3.1 証明の欄(空でない行)

| | olm113(M2A) | olm119(式 + 宣言の文) | olm122(式だけ・参考) | olm124(式だけ・再走) | **olm125(式 + 指示の文)** |
|---|---|---|---|---|---|
| n_proof | 41 | 44 | 37 | 37 | **40** |
| LN_a(線対称・肯定) | 5(0.122) | 14(0.318) | 4(0.108) | 4(0.108) | **9(0.225)** |
| PT_a(点対称) | 0 | 0 | 0 | 1 | **1**(b0_j05・LN と両方) |
| PAR3_a | 7 | 3 | 3 | 3 | **2** |
| PERP3_a | 4 | 10 | 5 | 7 | **7** |
| PBIS3_a | 0 | 0 | 1 | 0 | **1** |
| OUTER_a(外接線の印) | 10(0.244) | 12(0.273) | 9(0.243) | 9(0.243) | **10(0.250)** |
| SYMM(対称の語) | 11(0.268) | 22(0.500) | 13(0.351) | 15(0.405) | **18(0.450)** |
| kind | — 30・NONE 6・LN 5 | — 22・LN 14・NONE 7・OTH 1 | — 24・LN 4・NONE 7・OTH 2 | — 22・NONE 10・LN 4・PT 1 | **— 22・NONE 9・LN 8・BOTH 1** |

- 類ごと(olm125・証明の欄): EQ n 13 = LN 4・OUTER 0 / MIDO3 n 20 = LN 4・OUTER 10 / OTHER n 7 = LN 1・OUTER 0(olm124: EQ 8 = LN 1・OUTER 1 / MIDO3 21 = LN 3・OUTER 7 / OTHER 8 = LN 0・OUTER 1)。**外接線の印は MIDO3 の行にだけ**(10 / 10)・線対称は EQ と MIDO3 に半々。
- v5(olm123・参考): 証明の欄 PAR5 **2** / OUTER5 **10** = v3 と同じ(落とし 0・PAR5 の行 b1_j02・b1_j09)。
- 外接線の印(OUTER)は五腕で 0.24〜0.27 のまま動かない = 問いの文の Tool の段(式・宣言・指示)は外接線の記憶に触れない(olm118 / olm119 と同じ)。
- 点対称が証明の欄に 1 本(b0_j05「Tc and Th are symmetric with respect to O3, i.e., O3 is the midpoint of Tc and Th」= 線対称「symmetric with respect to the line joining the centers」と同じ欄に両方・olm124 の b0_j11 に続く 2 本目)。

### 3.2 行(n = 60)

| | olm119 | olm122 | olm124 | **olm125** |
|---|---|---|---|---|
| cls MIDO3 / EQ / OTHER / NONE | 29 / 8 / 11 / 12 | 27 / 12 / 7 / 14 | 23 / 12 / 10 / 15 | **20 / 14 / 11 / 15** |
| MIDO3 の率(取れた行) | 0.604 | 0.587 | 0.511 | **0.444** |
| EQ の率(取れた行) | 0.167 | 0.261 | 0.267 | **0.311** |
| T の中央値 | 440 | 576 | 661.5 | **607.5** |
| 上限 | 6 | 5 | 9 | **6** |
| REFL_MENTION(式に触れた) | 31 | 25 | 28 | **32** |
| REFL_CALC(式を数値で使った) | 13(0.217) | 12(0.200) | 15(0.250) | **18(0.300)** |
| tool_named(道具を名指す) | — | 11 | 11 | **18**(うち計算しない行 4) |
| answer_first(JSON が先) | 1 | 0 | 0 | **3**(b0_j06・b1_j05・b2_j13) |
| v4 本文 LN_a / LN_r(退け) | — | 23 / — | 24 / 11 | **30 / 12** |
| v4 本文 PT_a / PT_r | — | — | 8 / — | **10 / 4** |
| v4 本文 PERP3_a / _r | — | — | 29 / — | **28 / 10** |
| v4 本文 OUTER4_a / _r | — | — | 34 / — | **32 / 11** |

- MIDO3 は式だけ(0.587 / 0.511)から指示の文で **0.444** に下がり、olm113(0.34)に寄る。EQ(O3 が Tc・Th から等距離・一般には偽)が 0.311 で五腕の最高。計算した行の類は EQ 9・OTHER 4・NONE 5・**MIDO3 0**(olm124 1 / 15)= 計算すると共線 / 中点には行かず、等距離か JSON なしに行く。
- 本文の線対称(v4 LN_a)30 本・うち退け(LN_r)12 本 = 本文で線対称に触れた行の 4 割が退ける(olm124 24 / 11)。退けた 12 本のうち証明の欄で線対称を書いたのは b0_j13 の 1 本(§3.4・「O3Tc = O3Th」の EQ 行・本文で退けた後(v4 LN_r)に証明の欄で「reflections of each other with respect to O3」+ 「symmetric with respect to the line joining the centers O1O2」)。

### 3.3 計算した行 / しない行

| | 計算した(REFL_CALC) | 計算しない |
|---|---|---|
| n | **18**(olm124 15) | 42 |
| 本文 LN_a / LN_r | 16 / 11 | 14 / 1 |
| 証明の欄あり | 9 | 31 |
| 証明の欄 LN_a | **2**(b1_j17・b2_j19)= 2 / 9 | **7** = 7 / 31 = **0.226** |
| 類 | EQ 9・OTHER 4・NONE 5・MIDO3 0 | MIDO3 20・EQ 5・OTHER 7・NONE 10 |
| T の中央値 | **8,748.5** | 254.5 |
| 上限 | 5(全部 NONE)+ b0_j09(取れた) | 0 |
| tool_named | 14 | 4 |

- **計算しない行の証明の欄の線対称(五腕・凍結の述語)**: olm113 5 / 38 = 0.132・olm119 11 / 34 = 0.324・olm122 3 / 28 = 0.107・olm124 3 / 30 = 0.100・**olm125 7 / 31 = 0.226**。計算した行では 0 / 3・3 / 10・1 / 9・1 / 7・**2 / 9**。Q1 の +0.117 は計算しない行の分(+4 本)。
- **REJ**(凍結の補助・Tc / Th を O1O2 で折り返す計算の始まりから 700 字の中で「not the same / is not Th / doesn't match / not exact / different」): **14 本**(olm113 0・olm119 10・olm122 6・olm124 12)。うち計算した行 13(18 本のうち折り返しの数値を出して退けた行)・計算しない行 1(b0_j06 = 共線の媒介変数「t is not the same for both」を拾った = 計器の拾いすぎ 1・開示・真の REJ は 13)。
- **REJ かつ証明の欄 LN(b2_j07 の型)**: v3 で **2 本**(b1_j17・b2_j19)+ SUPP_LN だけで 1 本(b1_j11)= **3 本**(olm113 0・olm119 3・olm122 1 + 1・olm124 1)。退けた後に証明の欄で線対称を書く行は、計算した行の証明の欄 9 本のうち 3 本。
- 計算した 18 本のうち 5 本は上限で JSON に至らず、4 本は status に至らない(§1)= 計算すると証明の欄に至る率は 9 / 18(olm124 7 / 15)。
- 指示の一行の写し(「rely on it」「use it to check」の逐語): **1 本**(b0_j18 = 問いの文を Tool の段ごと丸写しして続ける・T 1,146・OTHER)。言い換え(逐語でない): b2_j07「If you need to use the reflection tool, use the formula given. Do not rely on any other way to compute reflections.」(指示の続きとして**道具の使い方の規則を自分で書き足す**・計算しない・MIDO3)・b0_j14「The coordinates are given, but I shouldn't rely on them for the general case.」(計算した行が「座標に頼らない」と書く・T 12,038)。

### 3.4 逐語(Q4)

- **証明の欄の LN(v3・全部 9 本)**:
  - b0_j05(MIDO3・計算なし・T 2,698・点対称と両方)「The inner common tangents are symmetric with respect to the line joining the centers, so Tc and Th are symmetric with respect to O3, i.e., O3 is the midpoint of Tc and Th. Therefore, O3 is equidistant from Tc and Th.」
  - b0_j07(MIDO3・計算なし・T 332)「The reflection of Th across the line connecting the centers of the circles, O1O2, results in the point Tc. Since O3 is the midpoint of O1O2, it also serves as the midpoint for the segment ThTc.」
  - b0_j13(EQ・計算なし・T 2,351・本文で線対称を退けた後)「The inner common tangent configuration is symmetric with respect to the line joining the centers O1O2. The midpoint O3 lies on this line, and the points of tangency Tc and Th are reflections of each other with respect to O3. Therefore, the distances O3Tc and O3Th are equal.」
  - b1_j05(MIDO3・計算なし・T 192・JSON が先)「The inner common tangent's line of contact points Tc and Th, by definition, are symmetric with respect to the line connecting the centers of the circles. Therefore, the line O1O2 is the perpendicular bisector of the segment TcTh, making Tc, Th, and O3 collinear.」
  - b1_j07(MIDO3・計算なし・T 221)「Reflect Th across O1O2 to Tc using the given reflection tool; since reflection preserves linearity and Th,Tc are symmetric with respect to O1O2, the line through Th and Tc passes through O3, the midpoint of O1O2」(**道具を名指して、使わずに、対称を前提に**)
  - b1_j12(OTHER「Tc and Th are reflections across O1O2」・計算なし・T 160)「The inner common tangent's contact points are symmetric with respect to the line joining the centers; reflecting Tc across O1O2 yields Th, by the tangent-secant theorem and midpoint properties.」(conjecture そのものが線対称)
  - b1_j17(EQ・**計算して退けた後**・T 4,315)「The distances from O3 to Tc and Th are equal due to the symmetry of the configuration: O3 is the midpoint of O1 and O2, and the inner common tangent is symmetric with respect to O1O2. This ensures |O3 - Tc| = |O3 - Th|.」
  - b2_j05(EQ・計算なし・T 2,834)「The configuration is symmetric with respect to the line O1O2, making Tc and Th mirror images across that line. O3, the midpoint of O1 and O2, lies on the perpendicular bisector of TcTh, ensuring that O3 is equidistant from Tc and Th.」
  - b2_j19(EQ・**計算して退けた後**・T 9,564)「The inner common tangent l1 is symmetric with respect to the line O1O2. Since O3 is the midpoint of O1 and O2, it lies on the axis of symmetry. The perpendicular bisector of TcTh must coincide with this axis, making O3 equidistant from Tc and Th.」
- **v3 の形に無い直の目的語(SUPP_LN だけ・2 本)**: b0_j12(MIDO3・計算なし・T 365)「This can be seen by reflecting Th across O1O2 to Tc, and noting that the midpoint O3 is equidistant from O1 and O2, and thus must lie on the line connecting the two points of tangency.」・b1_j11(EQ・**計算して退けた後**・T 9,442)「By symmetry, reflecting Tc over O1O2 yields Th. Since O3 lies on O1O2, it is equidistant from Tc and Th, ensuring |O3Tc| = |O3Th|.」
- **REJ かつ証明の欄 LN(3 本・退けの文と証明の欄)**:
  - b1_j17: 本文「Let's try reflecting Th across O3, and see if we get Tc. … Not the same.」→「reflecting Th across O1O2 … (6.6167, 0.3767) ⏎ Compare this to Tc: (2.7678, 1.2685). Not the same. ⏎ Now, try reflecting Tc across O3 …」→ 証明の欄(上)「the inner common tangent is symmetric with respect to O1O2」。
  - b2_j19: 本文「reflecting Th over O1O2 … (6.6107, 0.3747) ⏎ Compare this to Tc's coordinates: (2.7678, 1.2685). These are not the same, so reflecting Th over O1O2 does not give Tc. Hmm」→ 証明の欄「The inner common tangent l1 is symmetric with respect to the line O1O2.」
  - b1_j11: 本文「So F can be O3. Then reflection of Tc over O1O2 would be 2*O3 - Tc. … (5.137, -6.0415). Compare to Th (7.6927, -3.2647). Not the same. So that's not the case.」(F を O3 に置く = 射影でなく中点を使う誤り)→ 証明の欄「By symmetry, reflecting Tc over O1O2 yields Th.」
- **計算した行の計算の文と結果の文(10 本)**:
  - b0_j08(EQ・T 5,276)「Let's check: Is Th the reflection of Tc over O1O2? Let's reflect Tc over O1O2 and see if we get Th. ⏎ Let me compute the reflection of Tc = (2.7678, 1.2685) over line O1O2. …」→「≈ (4.932, -6.1045) ⏎ Compare this to Th = (7.6927, -3.2647). The y-coordinate is quite different, so the reflection does not land exactly on Th.」
  - b0_j09(EQ・T 12,288・上限だが取れた)「Suppose we reflect Tc over the line O1O2; does it map to Th? Or vice versa? ⏎ Let's compute the reflection of Tc over O1O2. … F = (3.8652, 1.3128)」→「(4.9626, 1.3571) ⏎ Compare to Th = (7.6927, -3.2647) ⏎ They are not equal. ⏎ So, reflection across O1O2 does not map Tc to Th」
  - b0_j15(OTHER・T 2,558)「Then P' = 2F - Tc ⏎ x': 2*3.8517 - 2.7678 ≈ 4.9356 ⏎ y': 2*(-2.415) - 1.2685 ≈ -6.0985 ⏎ But Th is (7.6927, -3.2647). The computed reflection point (4.9356, -6.0985) doesn't match Th. So maybe the reflection of Tc isn't Th. Hmm, that's confusing. Maybe the invariant isn't about reflection but something else.」
  - b0_j16(EQ・T 7,335)「If we reflect Tc over the line O1O2, do we get Th? Let's compute. The formula given is P' = 2F - P, where F is the projection of P onto O1O2. …」→「The x-coordinate is close (4.92 vs 7.69), but the y is -6.1 vs -3.26. Not the same. So the reflection of Tc is not Th.」
  - b1_j04(EQ・T 3,904)「The reflection of O3 across TcTh is: 2*projection - O3 = … (6.5112, 0.3865) ⏎ Is this point significant? Let's check if it is the midpoint of O1 and O2. … No. ⏎ Alternatively, perhaps the midpoint of TcTh is the reflection of O3 across O1O2.」(軸を接線に替えて式を使う)
  - b1_j16(NONE・上限)「reflecting Tc over O1O2 would give a point related to Th. However, this requires that the reflection of Tc over O1O2 is Th, **which is not necessarily true unless the circles are congruent**. ⏎ Another approach: Let's place O1 at (-a, 0) and O2 at (a, 0), so O3 is at (0,0). The inner common tangent will be horizontal if the circles are symmetric. …」(前提が偽である理由を正しく書く唯一の行・その後に対称な座標を置いて上限)
  - b1_j18(OTHER・T 2,480)「If we reflect Tc over the line O1O2, maybe it maps to Th? Let's test that with the given coordinates. Let's compute the reflection of Tc across O1O2. … The midpoint O3 is … (3.9524, -2.3865), which matches the given O3.」→「The computed reflection point (4.9356, -6.1005) is not the same as Th. So maybe that's not the case. Hmm.」
  - b1_j19(NONE・上限)「Reflecting Tc over O3: The reflection formula is 2*O3 - Tc. … (5.137, -6.0415). That's not Th (7.6927, -3.2647). So that's not the case.」(式を O3 での点対称に流用)
  - b2_j02(NONE・上限)「The tool mentioned is the reflection across O1O2. Let's compute the reflection of Th across O1O2 and see if it relates to Tc. ⏎ To reflect Th across the line O1O2, we can use the formula: P' = 2F - P …」→ 後段「Since the problem mentions the reflection tool, maybe the reflection of Th over O1O2 is Tc. Let's check that. Earlier, when we reflected Th over O1O2, we got approximately (6.6167, 0.3787), which is not Tc (2.7678,1.2685). So that's not the case.」(退けた後にもう一度同じ命題に戻って退ける)
  - b2_j06(OTHER・T 6,118)「Let's check if reflecting Tc over O1O2 gives Th. ⏎ Let's compute the reflection of Tc across O1O2: … t = -85.895 / 169.145 ≈ -0.5083 … P' = 2F − Tc = (30.2916, 1.3615) ⏎ This is not Th = (7.6927, -3.2647).」(符号を落として F が線分の外に出るが結論は同じ)
- **式に触れたが計算しなかった行(5 本・14 本のうち)**: b0_j12(MIDO3・T 365)「The reflection tool allows us to relate points on c and h1 with respect to the line O1O2. Since O3 is the midpoint of O1 and O2, and since Tc and Th are the points of tangency on the circles, their reflection properties …」・b1_j09(MIDO3・T 1,000)「7. Considering the provided reflection tool, it likely relates to the symmetry over the line O1O2. ⏎ 8. … perhaps O3 is the midpoint of Tc and Th.」(**道具の存在を手掛かりに読む**)・b2_j15(EQ・T 859)「Given the reflection tool, I suspect that Tc and Th are reflections of each other across the line O1O2. If that's true, O3, being the midpoint, should be the midpoint of Tc and Th as well. Let's check: - The midpoint of Tc and Th is … (5.23025, -0.9981). - O3 is at (3.9524, -2.3865). They're …」(確かめたのは中点で、折り返しは確かめない)・b2_j00(NONE・T 190)「The most important invariant is that the line O3Tc is perpendicular to O1O2. This holds because the reflection of Tc across the line O1O2 yields Th, and since O3 is the midpoint, O3Tc must be perpendicular to the line connecting the centers.」・b0_j07(MIDO3・T 332)「the line O1O2 is the axis of symmetry for the configuration. The reflection of Th across line O1O2 should lie on the line determined by Tc and O3, making O3 the midpoint of ThTc.」
- **指示の一行に触れた行(5 本)**: b0_j18(OTHER・T 1,146)= 問いの文の「# Tool (available if you need it) ⏎ Reflection of a point P across the line O1O2: P' = 2F − P … ⏎ Use it to check: compute the reflection with the given coordinates before you rely on it. ⏎ State the SINGLE most important invariant …」を丸写しして続ける・b2_j07(MIDO3・T 424・計算なし)「If you need a hint, ask for it. Do not try to solve the problem without a hint. ⏎ If you need to use the reflection tool, use the formula given. Do not rely on any other way to compute reflections.」(指示の続き)・b0_j14(EQ・T 12,038・計算あり)「The coordinates are given, but I shouldn't rely on them for the general case. The problem states that the configuration is general and non-degenerate, so the invariant should hold regardless of specific coordinates.」・b0_j01(EQ・T 1,438・計算あり)「Step 3. The configuration is general (non-degenerate), and the only geometric tool provided is the reflection formula. … Step 5. To check this, let's compute …」(Step の型で指示に従う唯一の行)・b1_j11(EQ・T 9,442・計算あり)「The reflection tool is mentioned, which uses the formula P' = 2F - P, where F is a point on the line O1O2. Maybe reflecting points across O1O2 could help find some symmetry.」

## §4. 読み(主 session・値と並べる・判定は変えない)

1. **指示の文は「使わせる」より「名指させる」**: 計算した行は 15 → 18(+3・Fisher 参考 0.68)で帯は動かず、道具を名指す行は 11 → 18。指示の一行を逐語で写した行 1・自分の規則に言い換えた行 1(b2_j07「Do not rely on any other way」)・指示の続きを書いて止まる短い行 10(olm124 6)。base は指示の文を**従う対象でなく続ける対象**として扱う = olm114「JSON だけの文は base に効かない」・olm124 b0_j01「Does it use the reflection tool?」と同じ側で、olm119 §4「道具は使われるより読まれる」が指示の文でも成り立つ。
2. **増えた線対称は計算しない行に在る**(3 / 30 → 7 / 31): 7 本は短く(T 160〜2,834)、5 本が式に触れ、証明の欄は「contact points … are symmetric with respect to the line joining the centers」「Reflect Th across O1O2 to Tc using the given reflection tool」の型。b1_j09「Considering the provided reflection tool, it likely relates to the symmetry over the line O1O2」・b2_j15「Given the reflection tool, I suspect that Tc and Th are reflections of each other across the line O1O2」が仕組みを逐語で書く: **道具の段に文が増えるほど、道具の存在が「線対称が答えだ」という手掛かりとして読まれる**。これは PREREG §3 の読みの軸の三つ目(植える効果の別経路・予想 0.15)で、olm119 の宣言の文(何が対称かを言う・0.318)と、指示の文(何が対称かを言わない・0.225)と、式だけ(0.108 / 0.108)の並びは「文が言う量」の順に見える。ただし §2 の Fisher のとおり 60 行ずつでは隣と分けられず、順は読みであって判定ではない。
3. **計算は試した命題だけ退け、次の命題は記憶から**: 計算した 18 本のうち 13 本が折り返しを数値で退け、共線 / 中点には 0 本が行き、等距離(EQ・一般には偽)に 9 本が行く。等距離を数値で確かめた行はない(退けたのは折り返しだけ)。退けた後に証明の欄で線対称を書く行 3 本(b1_j17・b2_j19・b1_j11 = olm124 の b2_j07 の型・五腕で 0 / 3 / 2 / 1 / 3)。b1_j16 だけが「reflection of Tc over O1O2 is Th … is not necessarily true unless the circles are congruent」と前提が偽である理由を書くが、直後に対称な座標(O1 = (−a, 0)・O2 = (a, 0))を置いて上限に至る = 理由を知っていても図は記憶の対称に戻る。
4. **計算の費用**: 計算した行の T の中央値 8,749(しない行 255)・上限 5 本は全部計算した行・証明の欄に至るのは 9 / 18。PREREG §0 で Q2 を G1 で止めなかった理由(計算させると取れる率が下がる)は向きは合っていたが、計算が +3 本しか増えなかったので G1 は境ちょうどで通った。
5. **五腕の不変**: 外接線の印 0.24〜0.27・取れる率 0.75〜0.83・取れない行の形(指示の続き / 上限)は Tool の段を何にしても動かない。動くのは線対称の率(0.108〜0.318)・MIDO3(0.34〜0.60)・計算した率(0.10〜0.30)。

## §5. 主張しないこと

- 判定は新しい 60 行だけ(Q2 変わらない・Q1 上がる)。olm124 との差は問いの文の一行の有無だが seed も違う。同じ問いの文の二回(olm122 → olm124)は 0.108 / 0.108・0.200 / 0.250 の幅だったので、0.225 が「同じ問いの文の二回目」でも残るかは走らせ直し(§6)でしか言えない。
- Q1 の上がりを指示の効果だけに帰さない(PREREG §5): TOOL_U は「reflection」の語を一度多く置き、問いの文を 90 字長くする。読み 2 はこの語の分を含む。
- 三種の文の順(宣言 > 指示 > 式だけ)は読みで、60 行ずつの Fisher では分けられない(§2)。
- SUPP_LN / REJ は記述の補助(較正 olm124 の逐語 15 例)。REJ は共線の「t is not the same」を 1 本拾った(拾いすぎ・開示)。v6 の材料。
- 予想が二つとも外れたことは記録する(Q2 上がる 0.60・Q1 変わらない 0.50)。予想の根拠「計算の指示は半分前後は従われる」は base には当たらなかった(従われたのは +3 本)。
- 正しさの率は測らない。一つの model・一つの温度・60 行。

## §6. 次の候補(先生の裁定・起案しない)

- **(e') olm126 = 同じ問いの文(md5 `718d1601…`)で新しい seed の 60 行**: olm122 → olm124 と同じ型の走らせ直し。0.225 が残れば「指示の文も植える(宣言の文より弱い)」が二回で言え、0.108 に戻れば一回の揺れ。G1 は二回続けて境ちょうどなので、落ちる確率も半分近い(開示)。
- **対照の一行**: 折り返しに触れるが宣言も指示もしない一行(例「(This tool is optional.)」の類で reflection の語を一度置く)を足す腕 = 読み 2 の「語を一度多く置く」分と「指示」の分を分ける。
- **v6 の計器**: 直の目的語「reflect(ing) <点> across / over O1O2」を LN に足す(SUPP_LN は凍結済・五腕で olm124 の手の数と一致)・式の写し(olm124 b1_j01)を LN から外す・REJ を正式に(共線の t を除く・較正例 = olm124 + olm125 の逐語 29 本)。
- 「植える文 / 使わせる文」の対の閉じ方: 今の並び(宣言 0.318・指示 0.225・式だけ 0.108 × 2・無し 0.122)は、(e') か対照の一行の後に一枚の表にする。

## 訂正(2026-11-04 昼・RESULT olm127 の読みの際に発見・上の本文は書き換えない)

- §3.2 の「EQ(O3 が Tc・Th から等距離・一般には偽)」と §4 の 3 の「等距離(EQ・一般には偽)」は**誤り**。等距離 |O3Tc| = |O3Th| は一般の図で**真**(= moy-2 の apex)。根拠(実出力・R4): hq の `CAL_APEX_M2` の先頭が `(True, "|O3Tc| = |O3Th|")`・gen.json の EQ 行は `apex: true`・RESULT olm117 の題「apex(等距離)の conjecture は 0 / 50」・RESULT olm119 §4 の 2「等距離(真)に 6 本が数値で着く」。幾何: O2Tc ⊥ l1・O1Th ⊥ l1 なので Tc・Th は O2・O1 の l1 への足、中点 O3 の足は TcTh の中点 → O3 は TcTh の垂直二等分線上。座標でも |O3Tc| = 3.8422・|O3Th| = 3.8420。
- 従って §4 の 3 の読み「等距離(偽)に 9 本が行く = 次の命題は記憶から」は、「計算した行は折り返し(偽)を数値で退けて **apex(真)の等距離に着く**(9 / 18)が、等距離を数値で確かめた行は 0 で、その証明の欄の前提は記憶の線対称のまま(3 本 = olm119 §4 の 3『結論は図に合い前提は記憶のまま』と同じ形)」に読み替える。§3.2 の「計算すると共線 / 中点には行かず、等距離か JSON なしに行く」は数の記述としてそのまま。
- 判定(Q2 変わらない・Q1 上がる)は変わらない(判定は LN_a と REFL_CALC の値だけで、類の正誤を使わない)。この誤りは MEMO(factcheck_yt__A1acg0ZTKs・§3 / §4)と auto-memory 二本と図解の BRIEF v1 の草稿に写っていたので、同日に同じ訂正を入れた(RESULT olm127 §6)。

## 訂正 2(冷間監査・2026-11-04 夜・U1)
- §3.2 の表「v4 本文 OUTER4_a / _r」の olm124 の欄「34 / —」は誤り。olm124 の read.json(`Q3_desc.v4_body`)は OUTER4_a **32**・OUTER4_r **15**(34 は v3 の本文の数 `body_count.OUTER_a`)。参考の行で判定に関わらない。
