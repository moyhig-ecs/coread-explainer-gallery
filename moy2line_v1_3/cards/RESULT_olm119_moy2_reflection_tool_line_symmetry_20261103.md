HEAD(R1) = d07229c1(執筆時の HEAD・fetch 済・origin より 18 commit 先・遅れ 0・tracked の変更なし)

# RESULT(札 `olm119`・2026-11-03): moy-2 の「折り返しの式」— olm113 の M2A の問いの文に O1O2 での折り返しの式を一段(# Tool・使えとは書かない)足した OLMo-3 32B base の 60 行では、**証明の欄で O1O2 についての線対称を肯定して述べる行が 14 / 44 = 0.318**(olm113 5 / 41 = 0.122・Δ **+0.196**・Q1 **上がる**・予想は 上がる 0.05 で**大外れ**〔変わらない 0.40〕)— 式を数値で使った行は **13 / 60 = 0.217**(Q2 **間**・予想 使わない 0.40 で外れ〔間 0.35〕)— 使った 13 本は本文で線対称を口にした 11 本のうち 8 本が計算の後に退ける(「Not the same. So Th's reflection is not Tc」)が、退けた後に**証明の欄で線対称を書く行が 3 本**(「Maybe my calculation is off」)— 使わない 47 本は 22 本が線対称を口にし、退けたのは 1 本 = **式の説明の文(「Two points are symmetric with respect to the line O1O2 exactly when each is the reflection of the other」)が前提として植わる**— 答えの分布も動く: 共線 MIDO3 0.34 → 0.60・等距離 EQ 0.32 → 0.17(計算した行は EQ 6 / OTHER 5 / MIDO3 1・計算しない行は MIDO3 28 / 47)

- 札 = [PREREG](PREREG_olm119_moy2_reflection_tool_line_symmetry_20261103.md)(凍結 86af77f0・HEAD(R1) 8ba1a5bf・G10 通る・台帳 済)・runner `ConstructGap/exp/olm119_moy2_reflection_tool_line_symmetry_20261103.py`(md5 `d8d4062f…`)・読み込むだけの部品 `hq_moy12_…py`(`426e2089…`)・`olm117_…py`(`ab678f30…`・v2)・`olm118_…py`(`136f72b9…`・v3)・比べる元 `olm118/read.json`(`bffeb826…`)= guard で一致。問いの文 md5 `d4c07f24…`(TOOL の段を外すと olm113 の M2A `56182280…`・guard)。
- 走り = zebrashark 11-03 15:20:02 → 18:05:27 JST(`--gen` 9,920 s = 2.76 時間・batch 3,368 / 3,154 / 3,398 s・seed 20261170〜72・温度 0.7・max_new 12,288・olm117 の 1.87 時間より長いのは上限に着いた行が 6 本)→ `--read`(同時刻)。Traceback 0。provenance = commit d07229c1・dirty false。
- 出力 = `ConstructGap/exp/olm119/gen.json`(md5 `781f0e70…`)・`read.json`(`f2138597…`)・`gen_run.log`・`read_run.log`・`chain_olm119.log`。
- 較正 = REFL 12 / 12・v3 54 / 54(guard)。
- 開示: PREREG §0 のとおり。主 session は `--read` の印字を read.json と同時に見た。§3 の逐語と類ごとの集計は、凍結の部品(読み込むだけ)で gen.json を読み直して取った(判定は read.json の値だけ)。**v4(olm121・凍結 b643e948・読み込むだけ)の RETR / KEPT は参考として並べ、判定には使わない**(この札の計器は v3 + REFL)。折り返しの座標は主 session が numpy で検算した(§3 末)。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | olm118 の read.json の olm113 の証明の欄 n = 41・md5 一致 | 41・一致 | ✓ |
| G1 | conjecture が取れた行 ≥ 0.80 | **48 / 60 = 0.80**(境の上・余裕 0) | ✓ |
| G2(記述の側) | status が hypothesis / question ≥ 0.70 | 43 / 60 = 0.717(olm113 42 / 60 = 0.70) | ✓ |

## §2. 判定(v3 の LN_a・REFL・Δ = 式あり − olm113 の証明の欄)

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** 証明の欄の線対称 LN_a | 式あり **14 / 44 = 0.318**・olm113 5 / 41 = 0.122・Δ = **+0.196** | **上がる**(Δ ≥ +0.08・境まで 0.116) | 変わらない **0.40**・間 0.30・下がる 0.25・上がる **0.05** → **大外れ**(四番目の帯) |
| Q2 本文で式を数値で使った率 REFL_CALC | **13 / 60 = 0.217** | **間**(0.10 < 率 < 0.30) | 使わない **0.40**・間 0.35・使う 0.25 → 外れ(二番目の帯) |
| Q3(記述)使った行の証明の欄の LN_a | **3 / 13**(b0_j13・b1_j06・b2_j16)・本文の LN_a 11 / 13・類 EQ 6 / OTHER 5 / NONE 1 / MIDO3 1 | — | — |

- 読みの軸(PREREG §3)との照らし: 「式を使って線対称が下がる → 支持」「使わず変わらない → 検証されず」「使っても変わらない → 反証」のどれでもない四つ目の形: **使わない行に式の説明の文が前提として植わり、率が上がる**。計算した行の中では L3 のとおり退ける(8 / 11)が、全体の率はそれで決まらない(§4)。
- Q2 の 13 本のうち 1 本(b0_j10)は式を引いて方向ベクトルを計算した行で、折り返し自体は計算していない(REFL_CALC の `P'` の後 220 字に座標の対、の粗さ)。それを除いても 12 / 60 = 0.20 で 間のまま。

## §3. Q4(記述)

### 3.1 腕ごとの印(証明の欄 = 空でない行・本文 = 60 行・asserted の数)

| 腕 | n | SYMM | 種類 PT / LN / BOTH / OTH / NONE / — | PT_a | LN_a | OUTER_a | PAR3_a | PERP3_a | PBIS3_a |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| **式あり(olm119)証明の欄** | 44 | 22 | 0 / **14** / 0 / 1 / 7 / 22 | 0 | **14** | 12 | 3 | **10** | 0 |
| olm113 の証明の欄(比べる元) | 41 | 11 | 0 / 5 / 0 / 0 / 6 / 30 | 0 | 5 | 10 | 7 | 4 | 0 |
| (参考)olm117 の証明の欄 | 46 | 18 | 3 / 6 / 1 / 0 / 8 / 28 | 4 | 7 | 13 | 8 | 4 | 2 |
| **式あり 本文** | 60 | 42 | 2 / 25 / 8 / 2 / 5 / 18 | 9 | **33** | 30 | 11 | 23 | 6 |
| olm113 の本文 | 60 | 26 | 5 / 9 / 2 / 0 / 10 / 34 | 7 | 11 | 29 | 23 | 21 | 1 |

- 率(証明の欄): LN_a 0.122 → **0.318**・PT_a 0 → 0・OUTER_a 0.244 → 0.273(PAR3 0.171 → 0.068・**PERP3 0.098 → 0.227**・PBIS3 0 → 0)。線対称と一緒に「O1O2 ⊥ 接線」が増え、「接線 ∥ O1O2」が減る(線対称の帰結は ⊥ = 前提が帰結を連れてくる・§4)。
- 本文: 線対称 11 → **33**・点対称 7 → 9・外接線の印 29 → 30。
- (参考・v4 = olm121 の計器・判定には使わない)証明の欄 OUTER4_a 11(PAR4 2・PERP3 10・PBIS4 0)。本文の RETR: 線対称 asserted 33 のうち退けた 9・残した 33、点対称 9 / 3 / 7、O1O2 ⊥ 接線 23 / 9 / 21、PAR4 9 / 5 / 7、PBIS4 6 / 3 / 5。

### 3.2 類ごと(式ありの腕)

| 類 | 本文 n | 証明の欄 n | 証明 LN_a | 証明 OUTER_a | 本文 LN_a | 式に触れた | 式を計算 |
|---|---:|---:|---:|---:|---:|---:|---:|
| EQ(等距離・真) | 8 | 8 | 3 | 0 | 6 | 8 | **6** |
| MIDO3(共線・偽) | 29 | 27 | **8** | 11 | 17 | 12 | **1** |
| OTHER | 11 | 9 | 3 | 1 | 7 | 7 | 5 |
| NONE | 12 | 0 | — | — | 3 | 4 | 1 |
| (olm113)EQ / MIDO3 / OTHER の証明 | 12 / 15 / 14 | | 4 / 1 / 0 | 2 / 4 / 4 | | | |

- **計算した 13 本は等距離(真)か OTHER に着き、共線(偽)は 1 本**。計算しない 47 本は共線 28・等距離 2。式の文は共線へ押し(MIDO3 の率 0.34 → 0.60・parsed)、式の計算は共線から引き離す。
- 分布: 類 MIDO3 29 / EQ 8 / OTHER 11 / NONE 12(olm113 17 / 16 / 17 / 10・olm117 37 / 0 / 13 / 10)。status hypothesis 42 / none 16 / other 1 / question 1(olm113 41 / 18 / 0 / 1)。T 中央値 **440**(olm113 1,068.5・olm117 560)・上限 12,288 に着いた行 6(olm113 5)・答えを先に書いた行 1(b1_j04)。

### 3.3 計算した行と計算しない行

| | n | 本文 LN_a | うち退けた(v4 参考) | 証明の欄 LN_a | 類 MIDO3 / EQ | T 中央値 | 上限 |
|---|---:|---:|---:|---:|---|---:|---:|
| 式を計算した | 13 | 11 | **8** | 3(/ 13) | 1 / 6 | 5,406(最小 2,039) | **5** |
| 計算しない | 47 | 22 | **1** | 11(/ 31 の空でない証明) | 28 / 2 | 342 | 1 |

- 退けた 8 本 = b0_j01・b0_j08・b0_j18・b1_j06・b1_j10・b1_j11・b2_j03・b2_j15。計算しない側で退けた 1 本 = b1_j00(「the question asks for a general invariant, not necessarily involving reflections」= 道具を使わない旨で、線対称を退けた句ではない)。
- 計算した行は長く(最小 2,039・上限 5 / 13)、計算しない行は olm113 より短い(中央値 342 対 1,068.5)。

### 3.4 式を数値で使った行の計算の文(10 本・逐語・PREREG §4)

| 行 | 類 / T | 計算の文(逐語・途中を … で省く) | その後 | 証明の欄の LN |
|---|---|---|---|---|
| b0_j01 | EQ / 5,406 | 「Let's try to compute the reflection of Tc over the line O1O2 and see if it lands on Th. According to the reflection formula given: … Tc' = 2F - Tc = … = (4.9376, 1.3575) But Th = (7.6927, -3.2647), which is not the same as Tc', so the reflection is not Th, but perhaps it's Th' -- let's try reflecting Th instead.」 | F の y の符号を誤る(正しくは (3.85, −2.42))が結論「not the same」は同じ。Th も折り返して合わず → 「Triangle O3TcTh is isosceles (O3Tc = O3Th)」 | 0 |
| b0_j08 | OTHER / 上限 | 「Using the reflection formula: P' = 2F - P, where F is the projection of P onto the line O1O2. … ≈ (6.6207, 0.3807). Compare this to Tc, which is (2.7678, 1.2685). Not the same. So Th's reflection is not Tc. … So maybe the reflection isn't the invariant here. Alternatively, maybe the line TcTh is perpendicular to O1O2? Let's check the slopes.」 | 傾きを計算して直交せず → 上限・conjecture「TcTh is parallel to O1O2」(偽)・status question | 0 |
| b0_j13 | OTHER / 4,445 | 「Let's use the reflection formula: P' = 2F - P, where F = O1 + t(O2 - O1), t = … Now, reflect Tc = (2.7678, 1.2685): … P' = 2*F - P = … = (4.9396, -6.0945) But this is not equal to Th = (7.6927, -3.2647). So the reflection is not Th. Alternatively, perhaps the lines O1Tc and O2Th are symmetric with respect to O1O2」 | **計算で否定した命題を「the only invariant that always holds」として出す**: conjecture「The lines O1Tc and O2Th are symmetric with respect to the line O1O2」 | **1** |
| b0_j18 | NONE / 上限 | 「Let's compute the reflection of Th across O1O2 using the formula provided. … So the reflection of Th over O1O2 is approximately (6.6167, 0.3787). But Tc is (2.7678, 1.2685). These don't match. Hmm, maybe I made a mistake in calculation. Wait, maybe I should check the reflection of Tc instead.」 | Tc も折り返して合わず → 上限・JSON なし | — |
| b1_j06 | EQ / 3,488 | 「The reflection of Tc over O1O2 should be Th, and vice versa. Let's check the coordinates numerically. … Let F = O1 + t(O2 - O1), where t = ((Tc - O1)·(O2 - O1)) / \|O2 - O1\|² … Dot product: … = 85.869」 | 合わず → 距離を計算「sqrt(14.766) ≈ 3.844 Very close, so the distances are nearly equal, but not exactly equal (likely due to rounding)」→ O3Tc = O3Th。**証明の欄**「The points Tc and Th are symmetric with respect to the line O1O2, and O3 is the midpoint of O1O2. Therefore, the configuration is symmetric, and the distances O3Tc and O3Th must be equal.」= 計算で退けた前提を証明に書く | **1** |
| b1_j10 | OTHER / 上限 | 「So the reflection of Tc over O1O2 is P' = 2F - Tc = 2*(3.8497, -2.415) - (2.7678, 1.2685) ≈ (4.9316, -6.0985). This is not equal to Th (7.6927, -3.2647). So Tc is not the reflection of Th over O1O2. Similarly, check if Th is the reflection of Tc.」 | 上限・conjecture「a < b」 | 0 |
| b1_j13 | EQ / 2,571 | 「Let me compute the reflection of Tc across O1O2 (call it Tc') and see if Th = Tc'. Let F = O1 + t(O2 - O1), … , which does not match Th. Alternatively, perhaps the key is that O3 is the midpoint of the segment joining the two tangent points Tc and Th. Let's check the distance from O3 to Tc and from O3 to Th.」 | 距離が等しい → conjecture「O3 is on the perpendicular bisector of TcTh」(真)・証明の欄「the midpoint of their centers lies on the perpendicular bisector of the segment joining the points of contact of their inner common tangent. This is a classical geometric property.」(理由は「classical」) | 0 |
| b2_j03 | MIDO3 / 上限 | 「Then, the reflection Th' = 2F - Th ≈ … ≈ (6.6267, 0.3787) Compare this to Tc: (2.7678, 1.2685). Not the same. So Th' is not equal to Tc. Therefore, Th and Tc are not symmetric with respect to O1O2. Hmm. This is getting complicated. Let's think differently.」 | 上限・conjecture「O3 = midpoint of Th and Tc」(偽・退化の主張) | 0 |
| b2_j04 | EQ / 2,039 | 「Reflection of Tc is P' = 2 * projection point - Tc = … = (4.9566, -6.0909). This is not equal to Th. Let's consider the midpoint property. … Midpoint of Tc and Th = (5.23025, -1.0). O3 = (3.9524, -2.3865). These are not the same.」 | 距離「O3Tc = … = 3.8425. O3Th = … = 3.8425」→ O3Tc = O3Th・証明の欄は距離の計算(LN なし)だが末尾に「Since O3Tc = O3Th, the points Tc, Th, and O3 are collinear and O3 is the midpoint of the segment TcTh」(自分で否定した中点を書く) | 0 |
| b2_j16 | EQ / 3,744 | 「Th' = 2F - Th = 2*(7.1567, -1.442) - (7.6927, -3.2647) ≈ (6.6207, 0.3807) Compare this to Tc = (2.7678, 1.2685). Hmm, these don't match. Maybe my calculation is off, or perhaps the reflection isn't the right approach.」 | 距離が等しい → O3Tc = O3Th。**証明の欄**「they are symmetric with respect to the line O1O2 (the line connecting the centers). … By the properties of symmetry, any point on the axis of symmetry (O1O2) is equidistant from the symmetric points (Tc and Th).」= 計算で合わなかった前提を証明に書く | **1** |

- 残り 3 本: b0_j10(EQ・4,284・式を引いて「the lines O2Tc and O1Th are parallel」の方向ベクトルを計算 = 折り返しは計算しない)・b1_j11(OTHER・11,204・「If that's the case, then Th is the reflection of Tc across O1O2. Let me check the coordinates.」→ 合わず → conjecture「O1Tc is parallel to O2Th」)・b2_j15(OTHER・上限・「Compare to Th (7.6927, -3.2647). Not the same. So Tc's reflection is not Th. Similarly, reflecting Th across O1O2 would give another point, which is not Tc.」→ conjecture「Tc is the midpoint of Th and O3」(偽))。

### 3.5 証明の欄の線対称(14 本・全部・逐語)

| 行 | 類 / 計算 | 文 | 読み |
|---|---|---|---|
| b0_j03 | OTHER / なし | 「The reflection of Tc across the line O1O2 is Th, so their midpoint lies on the line O1O2. Since O3 is the midpoint of O1 and O2, it also lies on O1O2. Therefore, the midpoint of Tc and Th is O3.」 | 式の言葉(reflection across)で偽の前提 → 偽の結論(中点 = O3) |
| b0_j06 | MIDO3 / なし | 「The inner common tangent l1 is invariant under reflection across O1O2, so its midpoint O3 lies on l1, which contains Tc and Th, thus O3, Tc, Th are collinear.」 | l1 が O1O2 で不変(半径の等しい図でだけ真) |
| b0_j07 | MIDO3 / なし | 「The tangent line l1 is perpendicular to O1O2, and Tc, Th are symmetric with respect to O1O2. Thus, the line through Tc and Th is the perpendicular to O1O2 at the midpoint O3, so Tc, O3, Th are collinear.」 | 線対称 + ⊥(PERP3)の鎖で共線へ |
| b0_j13 | OTHER / **あり** | 「The inner common tangent at Tc and Th are symmetric with respect to the line O1O2, as the tangent points and centers are symmetric under reflection across the line joining the centers. Therefore, O1Tc and O2Th are symmetric with respect to O1O2.」 | 計算で否定した命題(§3.4) |
| b1_j03 | MIDO3 / なし | 「By the properties of reflection, Tc and Th are symmetric with respect to the line O1O2, which passes through O3. Symmetric points with respect to a line, together with a point on that line, must be collinear. Therefore, Tc, Th, and O3 lie on the same line.」 | 二つ目の文は偽の補助定理(軸上の点と対称な 2 点は一般に共線でない) |
| b1_j06 | EQ / **あり** | 「The points Tc and Th are symmetric with respect to the line O1O2, and O3 is the midpoint of O1O2. Therefore, the configuration is symmetric, and the distances O3Tc and O3Th must be equal.」 | 結論は真・前提は計算で退けた物(§3.4) |
| b1_j07 | MIDO3 / なし | 「The line through Tc and Th is the inner common tangent, and these points are symmetric about the line O1O2. Hence, the midpoint of Tc and Th must lie on the line O1O2, which coincides with the line joining O1 and O2. Since O3 is already on O1O2, O3 must also lie on the line through Tc and Th」 | 同じ鎖 |
| b1_j08 | MIDO3 / なし | 「We reflect Th across the line O1O2 to obtain Tc'. By the reflection tool, Th and Tc' are symmetric with respect to O1O2. Since Th lies on h1 and Tc lies on c, and O3 is the midpoint of O1 and O2, the points Th, Tc, and O3 must lie on a straight line」 | **道具の名を引いて計算しない**・Tc' を作って Tc と同一視 |
| b1_j14 | MIDO3 / なし | 「Tc and Th are symmetric with respect to the line O1O2 (the perpendicular bisector of the segment joining the centers). O3 is the midpoint of O1O2 (and thus lies on O1O2). Therefore, the line TcTh, which is perpendicular to O1O2 …」 | O1O2 を「中心を結ぶ線分の垂直二等分線」と呼ぶ(語の混線) |
| b1_j19 | OTHER / なし | 「The configuration is symmetric with respect to O1O2: O1 and O2 are mirrored, and the circles h1 and c are symmetric. The inner common tangent l1 is symmetric with respect to O1O2, so its contact points Tc (on c) …」 | O1 と O2 が O1O2 で互いに鏡像(偽・軸上の点は動かない)・conjecture は線対称そのもの |
| b2_j08 | EQ / なし | 「The configuration is symmetric over O1O2: Tc and Th are symmetric and O3 is on O1O2, so \|O3Tc\| = \|O3Th\|.」 | 結論は真・前提は偽 |
| b2_j12 | MIDO3 / なし | 「O3 is the midpoint of O1O2 and the line connecting the centers of two circles is perpendicular to the common tangents, it follows that the common tangents are symmetric with respect to the line O1O2. The points of tangency on each circle along a common tangent are symmetric with respect to the line connecting the centers.」 | PERP3 → 線対称 |
| b2_j16 | EQ / **あり** | 「Since Tc and Th are contact points of the inner common tangent of circles c and h1, they are symmetric with respect to the line O1O2 (the line connecting the centers). The midpoint O3 of O1 and O2 lies on O1O2. By the properties of symmetry, any point on the axis of symmetry (O1O2) is equidistant from the symmetric points (Tc and Th).」 | 結論は真・前提は計算で合わなかった物(§3.4) |
| b2_j17 | MIDO3 / なし | 「By symmetry of the inner tangent with respect to the line O1O2, the points Tc and Th are symmetric with respect to O1O2. Their joining line is perpendicular to O1O2. Since O3 lies on O1O2, and the tangent points Tc and Th …」 | 線対称 → ⊥ → 共線 |

- 言い回し「symmetric with respect to (the line) O1O2」は 14 本中 10 本だが、**olm113 の 5 本も 4 本が同じ言い回し**(「Tc and Th are symmetric with respect to O1O2」)なので、言い回しでは「式の文の写し」と「記憶」を分けられない。分かるのは率(0.122 → 0.318)と、道具・折り返しを名指す行(「By the reflection tool」「the reflection of Tc across the line O1O2 is Th」「invariant under reflection across O1O2」= 60 行中 13 行が tool / formula の語を使い、うち 5 行は計算しない)。

### 3.6 式に触れたが計算しなかった行(5 本・逐語・全 18 本から)

| 行 | 類 / T | 文 | 読み |
|---|---|---|---|
| b0_j04 | MIDO3 / 446 | 「The available tools include the reflection of a point across the line O1O2. … In this case, the invariant that always holds true is the collinearity of the points Tc, Th, and O3.」 | 道具を目録に挙げて使わない |
| b1_j00 | EQ / 974 | 「The only given tools are about reflection across O1O2, but the question asks for a general invariant, not necessarily involving reflections.」 | 道具を退ける(線対称は口にして退けない) |
| b1_j12 | NONE / 80 | 「The tool is not used for the proof of the invariant. You can use the tool if you want to answer the question in the JSON object.」 | 指示の段を写す型(olm117 の 6 / 60 と同じ) |
| b2_j08 | EQ / 1,827 | 「Let's check: Is the reflection of Tc across O1O2 equal to Th? - Yes, for inner common tangents, the two contact points are symmetric across the line joining the centers (O1O2).」 | **「check」と言って計算せず記憶で答える** |
| b2_j13 | MIDO3 / 663 | 「Given the tool for reflection across the line O1O2, and the fact that the inner common tangent is related to the symmetry of the configuration across O1O2, it is natural to suspect that the points Tc and Th are symmetric with respect to O1O2.」 | 道具の存在から対称を「suspect」する = 式の文が前提を植える形そのもの |

### 3.7 検算(主 session・numpy・問いの文の座標)

- O1 (10.1897, −0.5520)・O2 (−2.2849, −4.2209)・Tc (2.7678, 1.2685)・Th (7.6927, −3.2647)・O3 (3.9524, −2.3865)。O1O2 での折り返し: **Tc' = (4.935, −6.101)**(t 0.508・F (3.852, −2.416))・**Th' = (6.622, 0.377)**(t 0.243・F (7.157, −1.444))。行の値(b0_j13 (4.9396, −6.0945)・b1_j10 (4.9316, −6.0985)・b2_j04 (4.9566, −6.0909)・b0_j08 / b0_j18 / b2_j03 / b2_j16 の Th' ≈ (6.62, 0.38))は丸めの範囲で一致 = 計算は合っていて、「not the same」は正しい。b0_j01 だけ F の y の符号を誤る(結論は同じ)。
- |O3Tc| = |O3Th| = 3.842(真・apex)。TcTh の中点 (5.230, −0.998) ≠ O3。TcTh と O1O2 の cos = −0.51(直交しない = PERP3 の 10 本は偽)。

## §4. 主 session の読み(L3 と並べる・判定は変えない)

1. **道具は使われるより読まれる**: 式を数値で使った行は 13 / 60。使わない 47 本のうち 22 本が線対称を口にし、退けたのは 1 本(それも道具を使わない旨)。式の段の第二文「Two points are symmetric with respect to the line O1O2 exactly when each is the reflection of the other」は定義の文だが、base はこれを図についての事実として読む(b2_j13「Given the tool … it is natural to suspect that the points Tc and Th are symmetric」・b1_j08「By the reflection tool, Th and Tc' are symmetric」)。「available if you need it」の但し書きは効かない。olm114 の k = 0(JSON だけの文は base に効かない)と対で、**宣言の文は効く(前提として)**。
2. **計算した行では L3 のとおり直る**: 11 本中 8 本が計算の後に線対称を退け、共線(偽)に着いた行は 13 本中 1 本、等距離(真)に 6 本が数値で着く(b2_j04「O3Tc = … = 3.8425. O3Th = … = 3.8425」)。olm118 の L3「数値で確かめられる前提は図で直る」の「確かめられる」を式で作れば、確かめた行では直る。
3. **だが証明の欄は記憶の文で埋まる**: 計算で「not the same」と言った後に証明の欄で線対称を書く行が 3 本(b1_j06・b2_j16・b0_j13)。b1_j06 と b2_j16 は結論(O3Tc = O3Th)が数値で真と分かった後、その理由を記憶の「対称だから等距離」で書く = olm117 の「結論は図に合い前提は記憶のまま」と同じ形。b0_j13 は計算で否定した命題を conjecture にする。b2_j04 は自分で否定した「中点 = O3」を証明の末尾に書く。**計算は結論を直すが、証明の欄の文は結論から逆向きに記憶で埋められる**。
4. **植わった前提は帰結を連れてくる**: 線対称と一緒に「O1O2 ⊥ 接線」(PERP3)が 4 → 10 に増え、「接線 ∥ O1O2」(PAR3)は 7 → 3 に減る。鎖「対称 → TcTh ⊥ O1O2 → 中点が O1O2 上 → O3 と共線」(b0_j07・b1_j07・b1_j14・b2_j17)が共線の誤アトラクタを太らせ、MIDO3 の率は 0.34 → 0.60(olm117 の半径の等しい図 0.74 に近づく)。式の文が「対称な図」の記憶を呼ぶ。
5. **予想の外れ**: 主 session は「base は与えた式を自発的には使わない」と見た(47 / 60 は使わない = その限りでは当たり)が、使わない行に式の説明の文が前提として植わることを見なかった(PREREG §5 に「答えの分布も変えうる」と書いただけ)。L3 の検証としては、式だけ(第二文なし)の腕と、「使って確かめよ」と書く腕があれば、植える効果と確かめる効果を分けられた = 次の札の候補(§6)。
6. 長さ: 計算した行は長い(T 最小 2,039・上限 5 / 13)。計算しない行は olm113 より短い(中央値 342 対 1,068.5)= 前提が手元にあると早く閉じる(読み・主張しない)。

## §5. 主張しないこと(PREREG §5 + 追加)

- TOOL の段は問いの文を 267 字長くし、答えの分布(MIDO3 0.34 → 0.60)も変えた。線対称の率の差を TOOL の中身だけに帰さない(同じ長さの中立の段の腕はない)。式(第一文)と説明(第二文)の効果も分けていない。
- REFL_CALC は語と数の印で、計算の正しさは見ない(§3.7 の検算は主 session の後付け・1 本は折り返しでない計算)。v4 の RETR / KEPT は参考で、退けた相手がその当たりとは限らない。
- 言い回しの一致(§3.5)は写しの証拠にならない(olm113 も同じ言い回し)。
- 一つの model・一つの温度・60 行。一行 = 0.017(本文)・0.023(証明の欄)。G1 は境の上(48 / 60 = 0.80・余裕 0)。

## §6. 次の候補(先生の言葉で・凍結なし)

- (d) **第二文を外す腕**: TOOL を式(第一文)だけにして 60 行 → 線対称の率が olm113 に戻るか(植える効果の分離)。
- (e) **「使って確かめよ」と書く腕**: 「Use the tool to check any symmetry you assume」→ REFL_CALC の率と、計算した行の証明の欄の LN(§4 の 3 の形が残るか)。
- (f) v5(PAR の主語を除外で書く・olm121 §7)。
