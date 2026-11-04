HEAD(R1) = 191fe098(執筆時の HEAD = 凍結の commit・fetch 済・origin より 12 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記だけ)

# RESULT(札 `olm118`・2026-11-03): moy-2 の述語 v3 — 証明の欄で **O1O2 についての線対称**を肯定して述べる率は図で変わらない(olm113 5 / 41 = 0.122・olm117 7 / 46 = 0.152・Δ +0.030・Q1 **変わらない**・予想 0.45 で当たり)、**O3 についての点対称**は等しい図でだけ証明に残る(0 / 41 → 4 / 46・Δ +0.087・Q2 **増える**・境まで 0.007・予想 0.50 で当たり)、**外接線の記憶の印**(接線 ∥ O1O2・O1O2 ⊥ 接線・O1O2 が垂直二等分線)は変わらない(10 / 41 = 0.244 → 13 / 46 = 0.283・Δ +0.039・Q3 **変わらない**・予想 0.40 で当たり)— 本文では線対称 11 / 60 対 11 / 60 で同じ・点対称は olm113 の本文にも 7 本あるが数値で確かめて退ける(「O3 is not on ThTc. So this contradicts.」)ため証明に 0・線対称は確かめられず退けられない — 陰性統制 = frontier 20 本の証明の欄で全部 0 — 計器の取りこぼし 1(frontier の本文の真の文「the perpendicular from O3 to l1 is the perpendicular bisector of TcTh」を PBIS3 が拾う・OLMo の腕の値には影響なし)

- 札 = [PREREG](PREREG_olm118_moy2_symmetry_kind_outer_marker_v3_20261103.md)(凍結 191fe098・HEAD(R1) 46f8fca8・G10 通る・台帳 済)・runner `ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py`(md5 `136f72b9…`・model なし)・読み込むだけの部品 `hq_moy12_status_proof_common_20261102.py`(`426e2089…`)・`olm117_moy2_equal_radii_control_20261103.py`(`ab678f30…`)・入力 `olm113/gen.json`(`db0fde6e…`)・`olm117/gen.json`(`b5795850…`)・`results_prf5_20261102.jsonl`(`995650e5…`)= 全部 guard で一致。
- 出力 = `ConstructGap/exp/olm118/read.json`(md5 `bffeb826…`)・`read_run.log`。走り = zebrashark 11-03 15:06 JST(`--read`・数秒)・Traceback 0。provenance = commit 191fe098・dirty **true**(= 凍結の直後に G10 の台帳へ一行足した分・`git status` で tracked の変更はそれだけ)・prereg md5 `e934fa94…`。
- 較正 54 / 54(guard・PT 10・LN 9・BOTH 1・OTH 3・NONE 4・語なし 2・OUTER 陽性 10・陰性 7・否定 8)。
- 開示: PREREG §0 のとおり olm117 の側は粗く既知(点対称 5・線対称 5・外接線の印 7 前後 / 46)、olm113 の側と両腕の本文は未知で読んだ。凍結と `--read` の間に行は読んでいない。主 session は `--read` の印字(= 判定の値)を read.json と同時に見た。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | 入力 3 本・部品 2 本の md5 一致・較正 54 / 54 | 一致・54 / 54 | ✓ |
| G1(陰性統制・証明の欄) | prf5 の 20 本で OUTER_a ≤ 1 | **0 / 20** | ✓ |
| G1(同) | PT_a + LN_a ≤ 1 | **0 / 20** | ✓ |

- 記述(frontier の本文 = JSON の全文): PAR3 1 本 = fable_r8「angle TcO3Th is not 90°, O3 is not the midpoint of TcTh, and TcTh is not parallel to O1O2, so equidistance (perpendicular bisector) is the …」→ **asserted でない**(極性の計器が効いた・frontier は偽の性質を否定するために名指す)。PBIS3 1 本 = fable_r4「So the perpendicular from O3 to l1 is the perpendicular bisector of TcTh, giving O3Tc = O3Th.」→ **真の文を拾った = 計器の取りこぼし**(主語が l1 でなく「the perpendicular from O3 to l1」・`l1 is the perpendicular bisector` の形に当たる)。OLMo の腕の PBIS3 の当たり(olm113 本文 1・olm117 証明 2・本文 6)は全部読んで、この形の物はない(§4)。

## §2. 判定(証明の欄・asserted の率・Δ = olm117 − olm113)

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** 線対称 LN_a | olm113 **5 / 41 = 0.122**・olm117 **7 / 46 = 0.152**・Δ = **+0.030** | **変わらない**(\|Δ\| < 0.06・境まで 0.030) | 変わらない **0.45**・間 0.25・増える 0.15・減る 0.15 → **当たり** |
| Q2 点対称 PT_a | olm113 **0 / 41**・olm117 **4 / 46 = 0.087**・Δ = **+0.087** | **増える**(Δ ≥ 0.08・**境まで 0.007** = 一行 0.022 の内) | 増える **0.50**・間 0.30・変わらない 0.15・減る 0.05 → 当たり(境) |
| Q3 外接線の印 OUTER_a | olm113 **10 / 41 = 0.244**・olm117 **13 / 46 = 0.283**・Δ = **+0.039** | **変わらない**(\|Δ\| < 0.06・境まで 0.021) | 変わらない **0.40**・間 0.25・減る 0.25・増える 0.10 → 当たり |
| Q4 | 記述 | §3 | — |

- 三つとも予想の最頻の帯。Q2 は境の内側 0.007 で、olm117 の点対称が一本少なければ「間」。Q1 と Q3 は帯の中央近く。
- 未知だった olm113 の側: 線対称 0.122(読みの前の見込み 0.05〜0.10 より少し上)・点対称 **0**・外接線の印 0.244(見込み 0.20)。
- **追記(11-03 夕・[olm121](RESULT_olm121_moy2_v4_instrument_fix_and_retraction_20261103.md) の v4)**: 取りこぼしを直した v4 で当て直すと、Q1(線対称)・Q2(点対称)は同じ値・同じ帯、**Q3(外接線の印)は Δ +0.039 → +0.063 で帯が「間」**(境 0.06 まで 0.003)。動いた理由は v4 の PAR4 が olm113 の証明の欄の本物の当たり b0_j16「The inner common tangent at Tc on c and at Th on h1 is parallel to the line O1O2.」を落としたこと(v4 の取りこぼし)で、これを数えれば v3 と同じ +0.039。この札の判定(v3・変わらない)は本文のまま置き、v4 の判定(間)と理由を olm121 に記す。

## §3. Q4(記述・read.json の逐語)

### 証明の欄(空でない物・asserted の数)

| 腕 | n | SYMM(v2) | 種類 PT / LN / BOTH / NONE / — | 名指し率(語ありの中) | PT_a | LN_a | OUTER_a | PAR3_a | PERP3_a | PBIS3_a |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| olm113 M2A | 41 | 11 | 0 / 5 / 0 / 6 / 30 | 0.455 | **0** | **5** | **10** | 7 | 4 | 0 |
| olm117 | 46 | 18 | 3 / 6 / 1 / 8 / 28 | 0.556 | **4** | **7** | **13** | 8 | 4 | 2 |
| prf5(frontier) | 20 | 0 | 0 / 0 / 0 / 0 / 20 | — | 0 | 0 | 0 | 0 | 0 | 0 |

### 本文(= 生成の全文・「口にした」・asserted の数)

| 腕 | n | SYMM(v2) | 種類 PT / LN / BOTH / OTH / NONE / — | 名指し率 | PT_a | LN_a | OUTER_a | PAR3_a | PERP3_a | PBIS3_a |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| olm113 M2A | 60 | 26 | 5 / 9 / 2 / 0 / 10 / 34 | 0.615 | 7 | **11** | 29 | 23 | 21 | 1 |
| olm117 | 60 | 27 | 7 / 7 / 4 / 1 / 8 / 33 | 0.704 | 10 | **11** | 33 | 20 | 24 | 6 |
| prf5(frontier) | 20 | 0 | 0 / 0 / 0 / 0 / 0 / 20 | — | 0 | 0 | 1 | 0 | 0 | 1 |

- asserted でない当たりは全部で **2**(olm113 本文 b2_j01 PERP3「For inner common tangents, the line connecting the centers is not perpendicular to the tangent line.」・olm117 本文 b1_j11 PT「But in that case, Th and Tc would be symmetric with respect to O3.」)。極性の計器は前と中の否定だけを見るので(PREREG §5)、本文の「…? Wait, no」(次の文で退ける形)は asserted のまま数えている(§5 の L3 で粗く数える)。
- SYM_OTH(他の軸)= olm117 の本文 2 本だけ(b0_j08「the line O3O1 and O3O2 are symmetric with respect to l1」・b2_j17「the inner tangent line l1 is symmetric with respect to O1 and O2」)・olm113 0。
- 線対称は本文で **11 対 11**(同じ数)・証明の欄で 5 対 7。点対称は本文 7 対 11・証明 0 対 4。外接線の印は本文 29 対 33・証明 10 対 13。PERP3(O1O2 ⊥ 接線)は両腕の本文の約 1 / 3(21・24)。PBIS3 は等しい図で 1 → 6(「the line joining centers is the perpendicular bisector of the tangent segment」の類)。

### 類ごと(conjecture の類 = olm117 の v2)

| 腕 | 類 | 証明 n | 証明 SYMM → 種類 | 証明 PT_a / LN_a / OUTER_a | 本文 n | 本文 SYMM → 種類 | 本文 PT_a / LN_a / OUTER_a |
|---|---|---:|---|---|---:|---|---|
| olm113 | EQ(等距離) | 12 | 8 → LN 4・NONE 4 | 0 / 4 / 2 | 16 | 15 → LN 8・BOTH 2・PT 3・NONE 2 | 5 / 10 / 9 |
| olm113 | MIDO3 | 15 | 2 → LN 1・NONE 1 | 0 / 1 / 4 | 17 | 5 → PT 1・LN 1・NONE 3 | 1 / 1 / 8 |
| olm113 | OTHER | 14 | 1 → NONE 1 | 0 / 0 / 4 | 17 | 3 → PT 1・NONE 2 | 1 / 0 / 11 |
| olm113 | NONE | — | — | — | 10 | 3 → NONE 3 | 0 / 0 / 1 |
| olm117 | MIDO3 | 33 | 16 → PT 3・LN 6・BOTH 1・NONE 6 | 4 / 7 / 9 | 37 | 21 → PT 6・LN 7・BOTH 2・OTH 1・NONE 5 | 7 / 9 / 26 |
| olm117 | OTHER | 13 | 2 → NONE 2 | 0 / 0 / 4 | 13 | 6 → BOTH 2・PT 1・NONE 3 | 3 / 2 / 6 |
| olm117 | NONE | — | — | — | 10 | 0 | 0 / 0 / 1 |

- olm113 の EQ(等距離)の行: 証明の「対称性」8 本の内訳は **線対称 4・名なし 4・点対称 0**。本文では線対称 10 / 16・点対称 5 / 16 で、点対称は考えの中には出る。

## §4. 逐語(PREREG §4・行の名の順)

### olm113(半径 3.6869 / 7.4607)— 証明の欄

- 線対称 LN(5 本・全部):
  - b0_j08(EQ)「Since the tangent points are symmetric with respect to the line joining the centers, their distances to O3 are equal. Thus, |O3-Tc| = …」
  - b0_j11(EQ)「… the inner common tangent's points of contact Tc and Th are symmetric with respect to the line O1O2, the distances from O3 to Tc and Th must be equal」
  - b1_j06(MIDO3)「… the line O1O2 is perpendicular to the common tangent at Tc and Th, the points Tc and Th are symmetric with respect to O1O2, and thus O3 lies on the line through Tc and Th.」
  - b1_j14(EQ)「The construction of the tangent ensures symmetry about the line O1O2, so the distances from O3 to Tc and Th are equal.」
  - b2_j02(EQ)「… and the inner tangent points Tc and Th being symmetric with respect to O1O2, implies O3Tc = O3Th.」
- 点対称 PT: **0 本**。
- 外接線の印 OUTER(10 本のうち 6 本):
  - b0_j01(OTHER・PAR3)「the line joining the points of tangency (Tc and Th) is parallel to the line joining the centers (O1O2)」
  - b0_j03(OTHER・PAR3)「… such that the segment TcTh is parallel to the segment O1O2, which connects the two centers.」
  - b0_j16(MIDO3・PAR3)「The inner common tangent at Tc on c and at Th on h1 is parallel to the line O1O2.」
  - b0_j19(MIDO3・PERP3)「This is because the inner common tangent is perpendicular to the line connecting the centers of the circles, and O3 lies on this line.」
  - b1_j15(OTHER・PAR3 ∧ PERP3)「TcTh ⊥ radius O1Tc, and O1O2 ⊥ tangent TcTh at Tc; hence TcTh || O1O2 by perpendicularity」(平行と垂直を同じ文で言う)
  - b2_j12(MIDO3・PERP3)「The inner common tangent l1 is perpendicular to O1O2 at Tc and Th. The midpoint O3 of O1O2 also lies o…」

### olm113 — 本文(口にした)

- 線対称(11 本のうち 6 本): b0_j02「the inner common tangent's points of contact are symmetric with respect to the line connecting the centers. Since O3 is the midpoint, it should lie on the p…」・b0_j04「the configuration is symmetric with respect to the line O1O2. The perpendicular bisector of TcTh should pass t…」・b0_j05「Then, perhaps there's a reflection symmetry across the line O1O2. If you reflect O1 over O3, you get O2, and vice …」・b0_j08 / b0_j11(証明と同じ文)・b0_j09「The inner tangent's contact points are symmetric with respect to the line joining the centers, and the midpoint O3 is the unique point equidist…」
- 点対称(7 本のうち 6 本): b0_j00「So the reflection over O3 swaps O1 and O2. Now, what happens to the tangent …」・b0_j01「Tc and Th are symmetric with respect to the midpoint of O1O2 (since the tangent is "between" the circles, and …」・b0_j05「the inner common tangent's points Tc and Th are symmetric with respect to O3, leading to equal distances.」・**b0_j15「Maybe reflecting Th over O3 gives Tc? Let's check. The reflection of Th over O3 would be (2*3.9524 -7.6927, 2*(-2.3865) - (-3.264…」**(数値で確かめる)・b2_j01「the configuration is symmetric with respect to O3. The inner common tangents are symmetric with res…」・b2_j07「So reflection of O1 over O3 is O2. Similarly, reflecting Th over O3 should gi…」
- 外接線の印(29 本のうち 6 本): b0_j00「the line connecting the points of tangency might be parallel to the line connecting the centers? Or maybe not. Hmm.」・b0_j01「the line Th-Tc is parallel to the line O1O2 (since both are perpendicular to the common tange…」・b0_j02「Maybe the line TcTh is parallel to O1O2. Let's check the slopes.」・b0_j06「the line joining the tangent points is parallel to the line connecting the centers (but for the *outer* tangent, it's parallel to th…」・b0_j02(PERP3)「the line connecting the points of tangency (Tc and Th) is perpendicular to the line connecting the centers (O1O2). Wait, no, actually, for external tangents …」・b0_j14(PBIS3)「Alternatively, perhaps the line O1O2 is the perpendicular bisector of TcTh? Let's check the midpoint of Tc and Th」

### olm117(半径 5.5738 ×2)— 証明の欄

- 線対称 LN(7 本のうち 6 本): b0_j01「This follows from the symmetry of the tangent line with respect to the line O1O2」・b0_j12「the tangent's contact points are reflections across the line connecting the centers.」・b1_j10「For congruent circles, the inner common tangent points Tc and Th are symmetric with respect to the line connecting their centers (O1O2).」・b1_j11「For two circles of equal radius, the inner common tangents are symmetric with respect to the line connecting their centers. The contact points Th and Tc must lie on the per…」・b1_j18(BOTH)「the inner common tangent l1 is symmetric with respect to O1O2, the tangent points Tc and Th are symmetric with …」・b2_j17「the tangent points Tc and Th are symmetric with respect to the line joining the centers. Thus, the segment TcTh is bisected by O3」
- 点対称 PT(4 本・全部): b0_j09「the contact points Tc and Th are symmetric with respect to O3. Calculating the midpoint of Tc and Th yields O3,」・b1_j05「The circles are congruent and the inner common tangent is symmetric with respect to the midpoint O3, so Tc and Th are symmetric about O3, i.e., O3 is …」・b1_j18(BOTH・上)・b2_j09「the tangent line l1 is symmetric with respect to O3. The tangent points Tc and Th are images of each …」
- 外接線の印 OUTER(13 本のうち 6 本): b0_j04(PBIS3)「the line O1O2 is the perpendicular bisector of the tangent segment TcTh.」・b0_j05(PAR3)「The inner common tangent of two circles is parallel to the line through their centers.」・b0_j08(PERP3)「For two disjoint circles, the line joining centers O1O2 is perpendicular to inner common tangent l1.」・b1_j11(PBIS3)「The contact points Th and Tc must lie on the perpendicular bisector of O1O2, which contains O3.」・b2_j04(PAR3)「Because c and h1 are disjoint and have equal radii, their inner common tangent line l1 is parallel to the line connecting their centers (O1O2).」・b2_j18(PAR3)「the radii O1Tc and O2Th are perpendicular to TcTh, hence O1O2 is parallel to TcTh.」

### olm117 — 本文(口にした)

- 点対称(11 本のうち 6 本): b0_j09(証明と同じ)・b0_j10「so the points Th and Tc should be symmetric around O3. Therefore, O3 would be the midpoint of ThTc.」・b0_j11「Wait, if you reflect over O3, which is the midpoint of O1O2, then O1 maps to O…」・b0_j15「perhaps Tc and Th are symmetric with respect to O3.」・b1_j05(証明と同じ)・**b1_j06「The configuration has point-symmetry about O3, mapping c↔h1, O2↔O1, Tc↔Th.」**
- 線対称(11 本のうち 6 本): b0_j01「the configuration is symmetric with respect to the line connecting the centers」・b0_j10「"consequence": "The configuration is symmetric with respect to the line O1O2."」・b1_j10「the inner common tangent's points Tc and Th are symmetric with respect to the line O1O2. That is, the line O1O2 is the perpendicular bise…」・b1_j11「since the circles are equal, the two inner common tangents are symmetric with respect to the line O1O2.」(二本の内接線が互いに = 真)・b1_j18「The tangent points Tc and Th are symmetric with respect to the line O1O2 (or, more precisely, the line joining the centers…」・b0_j12(証明と同じ)
- 外接線の印(33 本のうち 6 本): b0_j09「The inner tangent is parallel to the line connecting the centers? Wait, no, the tangent line itself isn't parallel.」・b1_j10「Wait, no, for congruent circles, the inner common tangents are parallel to the line connecting the centers? Wait, no. Wait, if two circles are congruent, th…」・b0_j12「Specifically, the line O1O2 is perpendicular to the common tangent. But wait, that's for external tangents.」・b0_j08「For two disjoint circles, the line joining the centers O1O2 is always perpendicular to the inner common tangent l1.」・b0_j07(PBIS3・reason の欄)「the line joining centers is the perpendicular bisector of the tangent segment.」・b2_j07(PBIS3)「That would be the case if the circles were congruent and the tangent was the perpendicular bisector, but that's not generally the case.」(この当たりは asserted でない・同じ行の別の当たりが asserted)

## §5. 主 session の読み(L3・値と並べる・判定は変えない)

1. **線対称の前提は図に依らない**: 証明で 0.12 / 0.15、本文で 11 / 11。二円は中心線 O1O2 について線対称(真)で、それを一本の内接線 l1 とその接点にまで延ばす(偽・l1 を O1O2 で折り返すともう一本の内接線)。この延長は OLMo の算術の手の内(傾き・内積・中点)では確かめられず、退けられない: 計器の外の粗い数(本文の当たりの後 260 字に `Wait, no / that's not / not it` など)で **olm113 の線対称 11 本のうち退けたのは 0**。
2. **点対称の前提は図で直る**: olm113 の本文に 7 本出る(等しい円の記憶)が、**中点か折り返しの計算で確かめて退ける**(b0_j15「The reflection of Th over O3 would be (2*3.9524 −7.6927, …」・b0_j00「according to the coordinates, O3 is not on ThTc. So this contradicts」・粗い数で 7 本中 3 本が退け、証明に残ったのは 0)。olm117 では同じ計算が通り(b0_j09「Calculating the midpoint of Tc and Th yields O3」)、11 本中 10 本が残って証明に 4。→ **数値で確かめられる前提は図で直り、確かめない前提は記憶のまま残る**。olm117 §5 の L3「結論は図に合い前提は記憶の図のまま」の、前提の側の内訳。
3. **外接線の印は図に依らない**: 「O1O2 ⊥ 接線」は両腕の本文の約 1 / 3(21・24)で口にされ、証明にも 4・4。本文ではしばしば「Wait, no, that's for external tangents」「that's more for outer tangents」と自分で退ける(粗い数: olm113 PERP3 22 本中 8・PAR3 23 本中 6 / olm117 24 本中 7・20 本中 8)= 外接線と内接線の区別は語としては持っていて、**最初に呼び出す図が外接線の図**。等しい図では「O1O2 が垂直二等分線」が 1 → 6 に増える(等しい円 + 線対称の記憶の合成)。
4. frontier(prf5・20 本)は証明の欄で全部 0。本文で名指す偽の性質は否定の形だけ(fable_r8「TcTh is not parallel to O1O2」)。計器の取りこぼし = fable_r4 の真の文(§1)。
5. 予想は三つとも当たり(olm114・116 で二枚外れ・117・118 で二枚当たり)。olm117 の側が粗く既知だった分、Δ の予想は olm113 の側の見込み(線対称 0.05〜0.10・点対称 ≈ 0・外接線 ≈ 0.20)に掛かっていて、実値 0.122・0・0.244 はその近く。Q2 は一行の内(0.007)。

## §6. 主張しないこと(PREREG §5 のまま + 計器の取りこぼし)

- 正規表現は語の印。対称性や平行を正しく使ったかの検証ではない。asserted は同じ節の 70 字の否定語だけで、次の文で退ける形(本文に多い)は拾わない。§5 の「退けた」の数は計器の外(凍結していない・粗い)。
- 線対称(O1O2)は両方の図で偽・点対称(O3)は等しい図でだけ真。正しさの率は測っていない。
- 本文の値は口にした物(却下した案を含む)。
- **PBIS3 は「the perpendicular from O3 to l1 is the perpendicular bisector of TcTh」(真)を拾う**(frontier の本文で 1 本)。OLMo の腕の PBIS3 の当たり 9 本は全部読んでこの形はなく、Q3 の値に影響はない。直すなら新しい札で(凍結の計器は触らない)。
- 一つの model・一つの温度・各 60 行。率の一行の幅 0.022〜0.024。Q2 は境の内。

## §7. 次(先生の言葉で)

- v3 の三つの問いは閉じた。候補(起案はしない): (a) 「確かめられる前提は直る」を測る = 線対称を数値で確かめる手(O1O2 での折り返しの式)を問いの文に与えた時に線対称の率が下がるか / (b) olm116 の続き(frontier の段 + OLMo)に v3 を当て、足場が外接線の印と線対称を抑えるか / (c) PBIS3 の主語の修正を含む v4。
