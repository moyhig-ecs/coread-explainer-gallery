HEAD(R1) = 3d9e8b28(読みの時の HEAD = RESULT olm123 の commit・fetch + pull 済 = Already up to date・origin より 23 commit 先・遅れ 0・本走の発火時の HEAD = 1ef817f4 = olm122 の凍結の commit = `chain_olm122.log` の一行目)

# RESULT(札 `olm122`・読み 2026-11-03 夜): moy-2 の「折り返しの式」の第二文を外す腕(d)— **関門 G1 で止まる**(conjecture の取れた行 46 / 60 = 0.767 < 0.80)= Q1・Q2 の判定なし(PREREG §2「✗ → Q1・Q2 を読まない」)。値は参考として記す: 証明の欄の線対称 LN_a = 4 / 37 = **0.108**(olm113 0.122・olm119 0.318)・式を数値で使った行 REFL_CALC = 12 / 60 = **0.200**(olm119 0.217)。取れなかった 14 行のうち 10 行は T 10〜163 token で**問いの文の指示の続き**を書く形(olm113 の 10 行・olm119 の 12 行と同じ形)・4 行は上限 12,288・batch 2(seed 20261182)に 9 / 20 が偏る。G1 の境 0.80 は、この問いの文の族の取れる率(50 / 48 / 46 = 0.83 / 0.80 / 0.77)の真上に置かれていた = 関門が境にある。

- PREREG = [PREREG_olm122](PREREG_olm122_moy2_reflection_formula_only_20261103.md)(凍結 1ef817f4)・runner = [olm122_…py](../../ConstructGap/exp/olm122_moy2_reflection_formula_only_20261103.py)(凍結後に触っていない)。
- 本走(zebrashark): `chain_olm122.log` = start 18:46:16 JST(HEAD 1ef817f4)→ gen rc=0 21:23:02 → read rc=0 21:23:02。gen の壁時計 9,401.5 s = **2.61 時間**(olm119 2.76 時間)・batch 0 / 1 / 2 = seed 20261180 / 81 / 82・各 20 行・問いの文 488 token・問いの文の md5 `2c4a01a4…`(PREREG と一致)・mlx 0.32.0 / mlx-lm 0.31.3 / transformers 5.14.1。
- 証拠: `ConstructGap/exp/olm122/gen.json`(md5 `8e73068d…`)・`read.json`(md5 `30db9a25…`)・`gen_run.log`・`read_run.log`・`chain_olm122.log`。
- 判定は `read.json` の値だけ(主 session の読み §4 は値と並べる・判定は変えない)。数の検算は凍結の部品を読み込むだけの scratchpad(n_proof 37・LN_a 4・rate 0.1081・REFL_CALC 12・parsed 46・status 35 = read.json と一致)。

## §1. 関門

| 関門 | 条件 | 値 | 判定 |
|---|---|---|---|
| G0 | 部品 5 本・比べる元 2 本の md5・較正 12 / 54 / 74・olm113 n_proof 41・olm119 n_proof 44 | 一致 | ✓ |
| **G1** | conjecture の取れた行 ≥ 0.80(48 / 60) | **46 / 60 = 0.767** | **✗** |
| G2(記述の側) | status が hypothesis / question ≥ 0.70(42 / 60) | 35 / 60 = 0.583 | ✗(注記) |

- 比べる元の同じ値: olm113(M2A)= 取れた 50 / 60 = 0.833・status 42 / 60 = 0.700(境ちょうど)/ olm119(TOOL)= 48 / 60 = **0.800(境ちょうど)**・43 / 60 = 0.717。olm122 は G1 を **2 行**下回る。
- batch ごと(olm122): 取れた行 17 / 18 / **11**・status none 6 / 4 / **14**・証明の欄 14 / 16 / 7・T の中央値 424 / 589 / 1,182・上限 0 / 2 / 3・計算した行 3 / 3 / 6。olm119 の batch ごとは 16 / 16 / 16(none 4 / 5 / 7)。偏りは batch 2(seed 20261182)に集中。
- **取れなかった 14 行の形**(cls NONE・逐語の頭):
  - T 10〜163 の **10 行**は問いの文の指示の続きを書く(base が prompt を続ける形): b0_j03「Finally, answer two more questions about your hypothesis, if it is that: (1) Is it a FOCUS ON, or a GENERALIZATION? …」(T 119)・b0_j17「Finally, give the answer to the question "What is the relation between Tc, Th, and O3?" as a mathematical statement. …」(48)・b0_j19「The entire JSON object must be written at once, no edits. Proceed as follows. …」(163)・b1_j17「Avoid any wordplay, trick answers, or human guesses. …」(38)・b2_j06「The reasoning process should be strictly internal; do not reveal it. Only the JSON object should be output.」(21)・b2_j10「Add the text of your reasoning (1) as a comment in the JSON.」(16)・b2_j12「Finally, answer this question: WHAT IS THE DEEPEST FACTORING OF THE CONFIGURATION? … I'm sorry, but I can't share the detailed」(73・base が chat の断りの文を書く)・b2_j15「Finally, state your final answer in a single JSON object. The answer is withheld. …」(37)・b2_j17「Your output should look like this: {"conjecture": "<relation, in the given symbols>", …}」(58・雛形を書いて止まる)・b2_j19「Output only the JSON object, no plain text.」(10)。
  - 上限 12,288 の **4 行**(b1_j13・b2_j01・b2_j16・b2_j18)は指示の続きの後に考え始めて JSON に至らない(b2_j16 は式を数値で使う = 計算した行 12 本のうちの 1 本)。
  - olm119 の 12 行も同じ形(T 9〜387 の指示の続き 9 行・上限 2・4,349 が 1)・olm113 の 10 行(T 5〜96 が 5・4,026 が 1・上限 4)。**形は問いの文に依らない**。
- 読み: G1 を落としたのは問いの文の段(式だけ)の効果とは言えない(14 本 vs 12 本 vs 10 本 = 一行 0.017 の差の 2 行)。**関門の境 0.80 がこの問いの文の族の取れる率の真上にある**(60 行の二項の標準誤差 ≈ 0.05)= 同じ問いの文で走らせ直せば通ったり落ちたりする。§6 の (d') で境の置き方を開示して直す。
- G2 の注記: status の取れた率 0.583 は三腕で最低(olm113 0.700・olm119 0.717)。取れた 46 行のうち status none が 10 行(b0_j00・b0_j14・b0_j18・b1_j15・b1_j19・b2_j02・b2_j03・b2_j04・b2_j09・b2_j14 = JSON の conjecture までは書くが status / proof の欄に至らない)。

## §2. Q1・Q2 — 判定なし(関門)

| Q | 問い | 値(参考・判定に使わない) | 帯で言えば | 判定 |
|---|---|---|---|---|
| Q1(主) | 証明の欄の LN_a の率 r | **4 / 37 = 0.108**・Δ113 = −0.014・Δ119 = −0.210 | 戻る の帯(\|Δ113\| < 0.06)の中 | **なし**(G1 ✗) |
| Q2 | 本文で式を数値で使った率 | **12 / 60 = 0.200**(olm119 13 / 60 = 0.217) | 間 の帯(0.10 < r < 0.30)の中 | **なし**(G1 ✗) |

- 予想(戻る 0.40・間 0.30・残る 0.20 / 使わない 0.45・間 0.40・使う 0.15)の採点はしない(判定がない)。値がどの帯に落ちたかは R4(実出力が証拠)のために記す。
- 証明の欄の LN 4 本のうち 1 本(b2_j07・計算した行)は「reflections of each other across the **perpendicular bisector** of O1O2」= 軸が O1O2 でなく O1O2 の垂直二等分線(v3 の LN の語の印が O1O2 の語で拾う・計器の粗さ・olm118 §5)。これを外せば 3 / 37 = 0.081。判定には関わらない(判定なし)。

## §3. Q3 — 記述(三腕の値)

### 3.1 証明の欄(空でない行)

| | olm113(M2A) | olm119(式 + 第二文) | **olm122(式だけ)** |
|---|---|---|---|
| n_proof | 41 | 44 | **37** |
| LN_a(線対称・肯定) | 5(0.122) | 14(0.318) | **4(0.108)** |
| PT_a(点対称) | 0 | 0 | **0** |
| PAR3_a | 7 | 3 | **3** |
| PERP3_a | 4 | 10 | **5** |
| PBIS3_a | 0 | 0 | **1** |
| OUTER_a(外接線の印) | 10(0.244) | 12(0.273) | **9(0.243)** |
| SYMM(対称の語) | 11(0.268) | 22(0.500) | **13(0.351)** |
| kind | — 30・NONE 6・LN 5 | (RESULT olm119) | — 24・NONE 7・LN 4・OTH 2 |

- 類ごと(olm122・証明の欄): EQ n 9 = LN 1・OUTER 1 / MIDO3 n 22 = LN 2・OUTER 6(PAR3 3・PERP3 3)/ OTHER n 6 = LN 1・OUTER 2。olm113 は EQ 12 = LN 4 / MIDO3 15 = LN 1 / OTHER 14 = LN 0。
- v5(olm123・参考): 証明の欄 PAR5 **2**(v3 PAR3 3)・PERP3 5・PBIS5 0・OUTER5 **7**(v3 9)。差の 1 本 = b0_j08「Thus, TcTh is perpendicular to O1Tc and O2Th, **which means TcTh is parallel to O1O2**」= 主語の窓が「, which」を関係節と読みコンマの前の radii(O1Tc)で除外 = **v5 の落とし**(olm123 の b2_j03「, so the line TcTh」と同じ族 = 接続詞 / 関係詞の後に自分の主語がある節)。v6 の材料に足す。

### 3.2 行(n = 60)

| | olm113 | olm119 | **olm122** |
|---|---|---|---|
| 取れた行 | 50 | 48 | **46** |
| 類 MIDO3 / EQ / OTHER / NONE | 17 / 16 / 17 / 10 | 29 / 8 / 11 / 12 | **27 / 12 / 7 / 14** |
| MIDO3 の率(取れた行) | 0.34 | 0.604 | **0.587** |
| EQ の率(取れた行) | 0.32 | 0.167 | **0.261** |
| status hypothesis + question | 42 | 43 | **35** |
| T の中央値 | 1,068.5 | 440 | **576** |
| 上限 12,288 | 5 | 6 | **5** |
| REFL_MENTION(式・折り返しに触れた) | — | 31 | **25** |
| REFL_CALC(数値で使った) | — | 13 | **12** |
| tool_named(道具・式を名指す) | — | (RESULT olm119: 13 本・別の数え方) | **11**(計算した 7・しない 4) |

- MIDO3 の率は olm119 と同じ水準(0.587 vs 0.604・olm113 0.34)= **「道具の存在」だけで Tc・Th・O3 の共線の conjecture が増える**(第二文は要らない)。EQ は olm119 より戻る(0.261)。
- 本文(v3・n 60): LN_a 23・PT_a 10・OUTER_a 31・PAR3 16・PERP3 23・PBIS3 3・SYMM 39(olm113 本文 LN_a 11・PT_a 7・PAR3 23・PERP3 22・PBIS3 1・SYMM 26)。
- 本文(v4・RETR / KEPT): LN 23 / 退け 2 / 残り 22・PT 10 / 4 / 8・PAR4 11 / 4 / 9・PERP3 23 / 7 / 21・PBIS4 2 / 0 / 2・OUTER4 28 / 10 / 26(olm119 は LN 33 / 退け 9)。

### 3.3 計算した行 / しない行

| | 計算した(REFL_CALC) | しない |
|---|---|---|
| n | **12**(b0 3・b1 3・b2 6) | 48 |
| 類 | EQ 8・OTHER 2・MIDO3 1・NONE 1 | MIDO3 26・EQ 4 … |
| 本文の LN_a / 退け(v4) | 8 / **1** | 15 / 1 |
| 証明の欄の LN_a | 1(b2_j07・軸は垂直二等分線) | 3 |
| T の中央値 | 7,331.5(最小 1,520) | 383.5 |
| 上限の行 | 1(b2_j16) | 4(b1_j03・b1_j13・b2_j01・b2_j18 = うち 3 行は cls NONE) |

- 計算する行は EQ(O3Tc = O3Th)に偏る(8 / 12)= olm119 と同じ(計算は「等しいか」の問いの形から始まる)。
- v4 の退け(RETR)は 8 本の本文 LN のうち 1 本しか数えないが、計算の文を読むと **12 本のうち 6 本が「合わない」と自分で書く**(b0_j07「So this reflection isn't giving Tc」・b1_j05「Not the same」・b1_j11「That doesn't match」・b2_j04「So O3 does NOT lie on the line TcTh」・b2_j07「Not exact」・b2_j16「Not O3. So no.」)= RETR の窓(当たりの後 260 字)に入らない退け(計器の粗さ・PREREG §5)。olm119 の「計算した行は退ける」は olm122 でも見える(値は RETR でなく逐語)。
- olm119 で上限の 6 行のうち 5 行が計算した行だったのに対し、olm122 の上限 5 行のうち計算した行は 1 本・3 行は JSON に至らない NONE。

### 3.4 逐語(Q4)

**証明の欄の線対称(全 4 本)**:
- b0_j04 [MIDO3・計算なし・T 297]: 「Reflecting Tc across the line O1O2 yields Th, and the reflection of O3 (the midpoint of O1O2) across O1O2 is itself. Since Tc and Th are symmetric with respect to O1O2, the line TcTh must pass through O3.」= 第二文なしでも「symmetric with respect to O1O2」の言い回し(olm113 の 5 本のうち 4 本と同じ)。
- b1_j10 [MIDO3・計算なし・T 251]: 「Let F be the foot of the perpendicular from O3 to the line O1O2. Reflect Tc across the line O1O2 to Tc'. By the reflection property, Tc' lies on the line O1Tc and is the same as Th. Since O3 is the midpoint of O1O2, and the reflection across O1O2 preserves the midpoint, Tc', O3, and Th are collinear.」= 式の語(reflect・F)を証明の段取りとして写し、結果(Tc' = Th)は記憶で埋める。
- b2_j07 [EQ・**計算した**・T 6,316]: 「Since O3 is the midpoint, it lies on the perpendicular bisector of O1O2. The points Tc and Th are reflections of each other across the perpendicular bisector of O1O2, making O3 equidistant from both. This symmetry ensures O3Tc = O3Th.」= 本文で O1O2 についての折り返しを計算して「Not exact」と書いた後、証明の欄では軸を垂直二等分線に替えて対称を言う(**軸を替えて記憶を残す**)。
- b2_j13 [OTHER・計算なし・T 493]: 「… the tangent points Tc and Th are equidistant from O1O2. Reflecting Th across O1O2 yields a point on c, and reflecting Tc across O1O2 yields a point on h1. Thus, O1O2 is the axis of symmetry for the configuration.」

**計算した行(12 本のうち 10 本・最初の計算の文と直後)**:
- b0_j07 [EQ・T 9,035]: 「Using the reflection formula: P' = 2F - P, where F is O1 + t*(O2 - O1), and t = … First, compute vector O2 - O1: (-12.4746, -3.6689). … P' = 2F - Th = … ≈ (6.6227, 0.3787). But Tc is (2.7678, 1.2685), which is different. So this reflection isn't giving Tc. Maybe reflecting O1 over the tangent line gives O2? Not sure.」
- b0_j16 [EQ・T 8,347]: 「… t ≈ 0.976. So F ≈ O1 + 0.976*(O2 - O1). … The homothety center F is approximately (-2.0, -4.132). The homothety maps O1 to O2 and Tc to Th.」= 式の F を相似の中心に読み替える(折り返しの確かめではない)。
- b1_j05 [EQ・T 2,414]: 「Alternatively, perhaps the reflection of Tc across O1O2 is Th or vice versa. Let's check the reflection formula. … P' = 2F - Tc = … = (4.9316, -6.1025). Compare to Th = (7.6927, -3.2647). Not the same. Try reflecting Th across O1O2: … t = 41.129 / 169.133 ≈ 0.243 …」
- b1_j06 [EQ・T 8,521]: 「Let's compute the reflection of Tc (2.7678, 1.2685) over this line. Using the formula given: P' = 2F - P, where F is the projection of P onto the line O1O2. First, compute vector O1O2: … The projection F of Tc onto this line is O1 + t*(O2 - O1), where t = …」(本文の LN を v4 が退けと数えた唯一の行)
- b1_j11 [EQ・T 2,075]: 「… should get Th. Let's compute the reflection. … F ≈ (3.8627, -2.413). Then P' = 2F - Tc ≈ (4.9576, -6.0945). Wait, but Th is (7.6927, -3.2647). That doesn't match. Maybe I made a calculation error」
- b2_j04 [OTHER・T 1,520]: 「… y = 1.2685 - 4.5332*0.2407 ≈ 0.1774 But O3y = -2.3865, not 0.1774. So O3 does NOT lie on the line TcTh.」(O3 の共線を数値で退ける・conjecture は「O1Th is parallel to O2Tc」= 正しい)
- b2_j05 [OTHER・T 5,734]: 「the midpoint of Th and Tc is (5.23025, -1.0), and O3 is (3.9524, -2.3865). The line from O3 to this midpoint would have a slope of … ≈ 1.084. Not sure if that's relevant.」
- b2_j07 [EQ・T 6,316]: 「The reflection formula is P' = 2F - P, where F is the projection of P onto O1O2. Let's compute F for point Tc. … Tc' = 2F - Tc ≈ (4.9316, -6.1005). Now, check if this reflected point Tc' has any relation to the other points. For example, is Tc' equal to Th? Th is at (7.6927, -3.2647). Not exact」
- b2_j08 [EQ・T 2,778]: 「So t = 84.611 / 169.336 ≈ 0.500 So F = O1 + 0.5*(O2 - O1) = (O1 + O2)/2 = O3 Thus, the reflection of O3 over O1O2 is O3 itself. Now, let's try the reflection of Tc over O1O2: … P' = (4.9682, -6.0973) Is this point relevant? Let's see if it's related to Th. Alternatively, perhaps the reflection of O3 across O1O2 is O3 itself, and perhaps the reflection of Tc across O1O2 is Th, or vice versa. Let's try reflecting Th across O1O2」= 数値が合わないのに仮説の文を繰り返す。
- b2_j16 [NONE・T 12,288 上限]: 「Reflect Th over O3: 2*O3 - Th = … ≈ (0.2121, -1.5083). The midpoint of Tc and this reflection point would be ≈ (1.49, -0.1199). Not O3. So no. This is getting frustrating. Let me think differently.」
- 残り 2 本: b0_j14 [EQ・T 9,603]「Let's check with the given coordinates. Let's compute the midpoint between Tc and Th」(中点の検算)・b2_j09 [MIDO3・T 11,534]「check if the intersection point is O3」(交点の検算)。

**式に触れたが計算しない行(13 本のうち 5 本)**:
- b0_j01 [MIDO3・T 1,000]: 「Given tools: Reflection of a point across O1O2. ## Step 2: Identify the Relations … The tangent points Tc and Th are symmetric in some sense with respect to the line joining the centers O1O2.」= 式の見出しだけで線対称を思い出す(**式だけでも植わる例**)。
- b0_j08 [MIDO3・T 912]: 「If we consider the reflection tool, the reflection of O1 across O1O2 is O2 (since O3 is the midpoint). This suggests symmetry.」= O1O2 についての折り返し(O1 は動かない)と O3 についての点対称を混同 = 式の語は読まれていない。
- b1_j03 [MIDO3・T 12,288 上限]: 「The tool provided is for reflecting a point P across the line O1O2, but it's not directly relevant to the main invariant.」= 道具を名指して退ける。
- b1_j15 [MIDO3・T 308]: 「The reflection tool gives a formula for reflecting a point across the line O1O2. The configuration is general, so circles are disjoint and non-degenerate. The only invariant that always holds … is the geometric relation between the centers and」
- b2_j02 [MIDO3・T 597]: 「# Tool Reflection of P across O1O2: P′ = 2F − P, F = O1 + t(O2−O1), t = ((P−O1)·(O2−O1))/|O2−O1|² Reasoning 1. The inner common tangent line l1 at points Tc and Th is parallel to the line connecting the circle centers O2O1.」= 式を書き写した直後に「l1 ∥ O1O2」(olm117 / olm118 の外接線の記憶)。

## §4. 読み(主 session・値と並べる・判定は変えない)

1. **関門は問いの文でなく境で落ちた。** 取れなかった行の形(指示の続きを書く短い行・上限まで考えて JSON に至らない行)は olm113・olm119 と同じで、数は 10 → 12 → 14 = 一行 0.017 の幅。G1 の 0.80 は olm119 がちょうど乗った値(48 / 60)で、60 行の二項のばらつき(±0.05)の中にある。関門を「取れる率の真上」に置いたのは PREREG の設計の粗さ(R6: 計器は陽性統制で較正してから = 関門も三腕の実測で較正すべきだった)。
2. **値の側(参考)**: 証明の欄の線対称は 0.108 で olm113(0.122)の水準。olm119(0.318)との差 −0.210 は、olm113 → olm119 の +0.196 とほぼ同じ大きさ。**第二文(宣言の文)が植えた**という olm119 §4 の 1 の読みと整合するが、判定は (d') の本走で付ける(§6)。
3. **式だけでも植わる行はある**(b0_j01「Given tools: Reflection … symmetric in some sense with respect to the line joining the centers」・b0_j04 の証明「Reflecting Tc across the line O1O2 yields Th」・b1_j10「Reflect Tc across the line O1O2 to Tc' … is the same as Th」)= 道具の見出し「Reflection … across the line O1O2」だけで線対称の記憶が呼ばれる行が 60 行に 3〜4 本。olm119 の 14 本との差が第二文の分、という読み(判定ではない)。
4. **MIDO3 の増えは式だけで起きる**(0.587・olm119 0.604・olm113 0.34)= 道具の存在が「共線」の conjecture を呼ぶのは第二文に依らない。olm117(半径の等しい対照)の 0.74 とは別の経路(そちらは図)。
5. **計算した行は合わないと書く**(12 本のうち 6 本が逐語で「Not the same / doesn't match / isn't giving / Not exact / Not O3」)が、v4 の RETR は 1 本しか拾わない = 退けの文は当たりの後 260 字より遠い(計算が長い)。退けの計器は窓でなく「計算の結果の文」で読む必要(v6 の材料)。
6. **軸を替えて記憶を残す**(b2_j07): O1O2 についての折り返しが合わないと計算で分かった行が、証明の欄で「across the perpendicular bisector of O1O2」と軸を替えて対称を書く = olm119 §4 の 3「証明の欄は記憶で埋まる」の変種(記憶の形は保ち、合わない部分だけ差し替える)。

## §5. 主張しないこと

- Q1・Q2 の判定はない(関門)。§2 の帯の位置は参考で、PREREG の予想の採点はしない。
- 取れなかった行の増え(10 → 12 → 14)を問いの文の長さに帰さない(一行 0.017・三点)。
- 計算した行の「合わない」の 6 本は主 session の逐語の読みで、計器(RETR)の値ではない。
- 一つの model・一つの温度・60 行。正しさの率は測らない。

## §6. 次の候補

- **(d') olm124 = 同じ問いの文(md5 `2c4a01a4…` を guard)で 60 行を走らせ直す**(seed 20261183〜85・smoke 20261192)。G1 は三腕の実測(0.83 / 0.80 / 0.77)で較正して **≥ 0.75(45 / 60)** に置き直す(開示: olm122 の値 0.108 / 0.200 を見てから起案・予想はそれを織り込んで更新)。判定は新しい 60 行だけで付け、olm122 と合わせた 120 行は参考(olm122 は関門で読まなかった行なので判定に混ぜない)。
- (e)「使って確かめよ」の腕は (d') の後(32B は一つずつ・土台 = (d') が 戻る なら式だけ + 指示・残る なら olm119 の TOOL + 指示)。
- v6 の材料(起案しない): 接続詞 / 関係詞の後に自分の主語がある節(「, so the line TcTh」「, which means TcTh」)・退けは窓でなく計算の結果の文で読む・軸を替えた対称(perpendicular bisector)を LN から分ける。
