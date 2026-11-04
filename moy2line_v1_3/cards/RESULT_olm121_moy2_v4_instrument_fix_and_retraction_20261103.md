HEAD(R1) = b643e948(執筆時の HEAD = 凍結の commit・fetch 済・origin より 17 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記だけ)

# RESULT(札 `olm121`・2026-11-03): 述語 v4 — 取りこぼし 3 本は消え、本物の当たり 3 本は残った(Q1 **直った**・予想 0.85 で当たり)。だが olm118 の Q3(外接線の印の olm117 − olm113 の差)の帯が **変わらない(Δ +0.039)→ 間(Δ +0.063・境まで 0.003)** に動いた(Q2 **変わる**・予想 0.15 で外れ)。動いた理由は v3 の誤りでなく **v4 の PAR4 が本物の当たりを一本落とした**こと(olm113 の証明の欄 b0_j16「The inner common tangent at Tc on c and at Th on h1 is parallel to the line O1O2.」= 主語と動詞の間の「at Tc on c and at Th on h1」で主語の形に合わない)。olm120 の判定は同じ(下がる・下がる・外接線の印は 4 → 2 / 40)。RETR(口にして退けた・本文): olm113 で O1O2 ⊥ 接線 12 / 21・接線 ∥ O1O2 5 / 18・点対称 3 / 7・**線対称 0 / 11**、olm117 で 8 / 24・7 / 13・1 / 10・1 / 11 = olm118 §5 の L3 が計器の値になった。v4 は PBIS の修正は本物、PAR の修正は狭すぎ(本文で本物の当たり 5 本も落とす)= v5 の材料

- 札 = [PREREG](PREREG_olm121_moy2_v4_instrument_fix_and_retraction_20261103.md)(凍結 b643e948・HEAD(R1) efd421a4・G10 通る・台帳 済)・runner `ConstructGap/exp/olm121_moy2_v4_instrument_fix_and_retraction_20261103.py`(md5 `9c0b2b4e…`・model なし)・読み込むだけの部品 `olm118_…py`(`136f72b9…`・v3)・`olm117_…py`(`ab678f30…`)・`hq_moy12_…py`(`426e2089…`)・入力 6 本(olm113 / olm117 / prf5 / olm116 の出力・olm118 / olm120 の read.json)= guard で一致。
- 出力 = `ConstructGap/exp/olm121/read.json`(md5 `84bd89e1…`)・`read_run.log`。走り = zebrashark 11-03 15:29 JST(`--read`・数秒・olm119 の本走と並行)・Traceback 0。provenance = commit b643e948・dirty true(台帳の追記のみ)・prereg md5 `79b7cabd…`。
- 較正 = 74 / 74(v3 の 54 例を v4 の名で + 20 例)。陰性統制 = prf5 の証明 20 本。
- 開示: PREREG §0 のとおり v3 の値は全部既知。v4 で当たりが変わる行は未知で読んだ。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | md5 一致・較正 74 / 74 | 一致・74 / 74 | ✓ |
| G1(証明の欄) | prf5 で OUTER4_a ≤ 1 | 0 / 20(PAR4 の当たり 1 = fable_r4「O1O2 is not parallel to l1」= 否定 = asserted でない) | ✓ |
| G1(同) | PT_a + LN_a ≤ 1 | 0 / 20 | ✓ |

## §2. 判定

| Q | 値 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** 取りこぼし 3 本が消え・本物 3 本が残る | 消えた: prf5 fable_r4 の本文 PBIS ✓・olm116 k1_1_j04 PAR ✓・k1_1_j08 PBIS ✓ / 残った: k1_0_j03 PAR ∧ PERP ✓・k1_0_j13 PBIS ✓・olm117 b0_j04 PBIS ✓ | **直った** | 直った **0.85** → 当たり |
| Q2 olm118 の Q1〜Q3・olm120 の Q1〜Q2 の判定 | olm118: Q1 線対称 変わらない(Δ +0.030・同じ)・Q2 点対称 増える(+0.087・同じ)・**Q3 外接線 変わらない → 間(Δ +0.039 → +0.063)** / olm120: 下がる・下がる(同じ) | **変わる**(5 つのうち 1 つ) | 変わらない **0.85**・変わる 0.15 → **外れ**(PREREG §3 で「Q3 は一本の違いで動きうる」と置いた所) |
| Q3 | 記述 | §3 | — |

- **Q3 の帯が動いた理由(逐語)**: olm113 の証明の欄 b0_j16(MIDO3)「The inner common tangent at Tc on c and at Th on h1 is parallel to the line O1O2. Since O3 lies on O1O2 and is its midpoint, …」は接線 ∥ 中心線の主張(本物・偽)で v3 は拾ったが、**v4 の PAR4 は主語「tangent」と動詞「is」の間に「at Tc on c and at Th on h1」があって合わず落とした**。olm113 の OUTER4_a が 10 → 9 / 41(0.244 → 0.220)になり、olm117 は 13 / 46(0.283)のままで、Δ が +0.039 → +0.063(帯の境 0.06 を 0.003 越える)。この一本を数えれば Δ は v3 と同じ +0.039 で「変わらない」。**凍結の v4 の判定は「間」のまま置き、v4 の取りこぼしとして記す**(olm118 の RESULT に追記で注記)。

## §3. Q3(記述・read.json の逐語)

### v3 → v4 で当たりが変わった行(全部)

| 腕 | 所 | 行 | v3 → v4 | 文(逐語) | 読み(L3) |
|---|---|---|---|---|---|
| olm113 | 証明 | b0_j16(MIDO3) | PAR 1 → 0 | 「The inner common tangent at Tc on c and at Th on h1 is parallel to the line O1O2.」 | **v4 の落とし**(本物・偽の主張) |
| olm113 | 本文 | b0_j13(OTHER) | PAR 1 → 0 | 「Wait, maybe the line O3Tc is parallel to O1O2? Let's check.」 | 正しい落とし(主語 O3Tc) |
| olm113 | 本文 | b0_j16 | PAR 1 → 0 | 「the line through Tc and Th is parallel to O1O2 by the properties of inner common tangents.」 | **v4 の落とし**(「the line through Tc and Th」の形を主語に入れていない) |
| olm113 | 本文 | b1_j12(MIDO3) | PAR 1 → 0 | 「the line connecting these two points is parallel to the line connecting the centers of the circles, O1 and O2.」 | **v4 の落とし**(「these two points」= 接点) |
| olm113 | 本文 | b2_j07(EQ) | PAR 1 → 0 | 「perhaps the line O3M, where M is the midpoint of TcTh, is parallel to O1O2? Let's compute M」 | 正しい落とし(主語 O3M) |
| olm113 | 本文 | b2_j15(NONE) | PAR 1 → 0 | 「the line O1O2 is parallel to the line connecting Tc and Th? Wait, no.」 | **v4 の落とし**(目的語「the line connecting Tc and Th」の形)・退けている |
| olm117 | 証明 | b1_j13(OTHER) | PAR 1 → 0 | 「the line O3Tc is also perpendicular to l1 and thus parallel to O1O2.」 | 正しい落とし(主語 O3Tc) |
| olm117 | 本文 | b0_j12(MIDO3) | PAR 0 → 1 | 「so the line connecting the centers would be parallel to the tangent line? Or maybe not. … Wait, no.」 | 正しい拾い(v3 は「would be」を見ない)・退けている |
| olm117 | 本文 | b1_j06(OTHER) | PAR 1 → 0 | 「O1O2 is parallel to O3O3.」 | 正しい落とし(目的語が接線でない) |
| olm117 | 本文 | b1_j10・b1_j11(MIDO3) | PAR 1 → 0 | 「the inner common tangents are parallel to the line connecting the centers? Wait, no.」 | **v4 の落とし**(複数形「tangents」)・退けている |
| olm117 | 本文 | b1_j13(OTHER) | PAR 1 → 0 | 「the line O3Tc is parallel to O1O2 (both are perpendicular to the tangent).」 | 正しい落とし |
| olm117 | 本文 | b2_j03(NONE) | PAR 1 → 0 | 「Since Tc and Th are points of tangency, the line connecting them is parallel to the line joining the centers of the circles」 | **v4 の落とし**(「the line connecting them」) |
| olm117 | 本文 | b2_j05(MIDO3) | PAR 1 → 0 | 「the tangent at Tc is perpendicular to O2Tc, which is parallel to O1O2.」 | 正しい落とし(半径 ∥ O1O2 の主張・外接線の印ではない) |
| olm117 | 本文 | b2_j08(MIDO3) | PAR 1 → 0 | 「the line O1O2 is parallel to the line connecting the projections of O1 and O2 onto l1」 | 境(射影を結ぶ線 = l1 だが、語は接線でない) |
| prf5 | 証明・本文 | fable_r4 | PAR 0 → 1(asserted でない)・PBIS 1 → 0 | 「O1O2 is not parallel to l1; the construction is therefore well defined.」/「the perpendicular from O3 to l1 is the perpendicular bisector of TcTh」 | 両方 正しい(否定の拾い・主語が垂線の落とし) |
| olm116 | 続き | k1_1_j04・k1_1_j08 | PAR 1 → 0・PBIS 1 → 0 | olm120 §3 の 2 本 | 正しい落とし |

- **v4 の PAR4 の落とし = 本文 5 本 + 証明 1 本**(主語の形「tangent at X … and at Y」「the line through / connecting Tc and Th」「the line connecting these two points / them」「tangents」(複数))。正しい落とし = 7 本(O3Tc・O3M・O3O3・半径)。PBIS4 の修正は落としなし。
- v4 の値(証明の欄): olm113 n 41 = 点対称 0・線対称 5・外接線 **9**(PAR4 6・PERP3 4・PBIS4 0)/ olm117 n 46 = 4・7・**13**(7・4・2)/ prf5 0・0・0 / olm116 k1 n 40 = 1・0・**2**(1・1・1)・k2 n 38 = 全部 0。

### RETR / KEPT(本文・口にして退けた / 残した・行の数)

| 腕 | 印 | 口にした(asserted) | 退けた(RETR) | 残した(KEPT) |
|---|---|---:|---:|---:|
| olm113 | 点対称 PT | 7 | **3** | 7 |
| olm113 | 線対称 LN | 11 | **0** | 11 |
| olm113 | 接線 ∥ O1O2(PAR4) | 18 | 5 | 16 |
| olm113 | O1O2 ⊥ 接線(PERP3) | 21 | **12** | 17 |
| olm113 | O1O2 が垂直二等分線(PBIS4) | 1 | 0 | 1 |
| olm117 | 点対称 PT | 10 | 1 | 9 |
| olm117 | 線対称 LN | 11 | 1 | 10 |
| olm117 | PAR4 | 13 | 7 | 9 |
| olm117 | PERP3 | 24 | 8 | 19 |
| olm117 | PBIS4 | 5 | 2 | 4 |

- 退けた と 残した は行の中の別の当たりで両方立ちうる(PT の 7 本は全部「残した」も立つ = 退けた後に別の所でまた口にする)。
- 退ける句の例(逐語): olm113 PERP3 b0_j02「the line connecting the points of tangency (Tc and Th) is perpendicular to the line connecting the centers (O1O2). Wait, no, actually, for external tangents …」・PT b0_j15「Maybe reflecting Th over O3 gives Tc? Let's check. The reflection of Th over O3 would be (2*3.9524 -7.6927, …」・PAR4 b0_j02「Maybe the line TcTh is parallel to O1O2. Let's check the slopes.」/ olm117 PERP3 b0_j12「the line O1O2 is perpendicular to the common tangent. But wait, that's for external tangents.」・PAR4 b0_j09「The inner tangent is parallel to the line connecting the centers? Wait, no, the tangent line itself isn't parallel」・LN b2_j01「the inner common tangents are symmetric with respect to the line connecting the centers. So the line l1 is perpendicular to the line conn…」(退ける句は後の別の案に掛かる = RETR の粗さ)。

## §4. 主 session の読み(L3・値と並べる・判定は変えない)

1. **PBIS の修正は効いた**(3 本とも消え・落としなし)。**PAR の修正は狭すぎた**: 主語を「接線」の語に限ったため、接点を結ぶ線の言い回し(「the line through / connecting Tc and Th」「these two points」「them」)と「tangent at Tc … and at Th」「tangents」を落とす。v3 の主語なしの `parallel to O1O2` は O3Tc・O3M(作図の線)を拾っていた(7 本)。正しい形は「主語が O3 から出る線でない」(除外で書く)か、主語の語を広げるか。v5 の材料。
2. **olm118 の Q3 の帯は計器の境の内**: v3 で +0.039、v4 で +0.063(落とし 1 本)、落としを戻せば +0.039。どちらの計器でも「olm117 の方が外接線の印が多い」向きは同じで、帯の名が変わるのは一行の違い。olm118 の RESULT には「v4 では間(v4 の落とし 1 本による)」と追記した。
3. **RETR は olm118 §5 の L3 を計器の値にした**: 線対称は退けられない(0 / 11・1 / 11)、O1O2 ⊥ 接線は半分以上退けられる(12 / 21・8 / 24・「that's for external tangents」)、点対称は olm113 で 3 / 7 が計算の後に退けられ、olm117(真)では 1 / 10。語の集合を広げた分(`but wait`・`that's for external`)、olm118 の粗い数(PERP3 8 / 22)より PERP3 の退けが増えた(12 / 21)。
4. prf5 の fable_r4「O1O2 is not parallel to l1」を PAR4 が拾って asserted でないと読んだ = 否定の計器の陽性例が一本増えた。
5. olm116 の続きは v4 で外接線の印 2 / 40(olm120 §3 の読みどおり)。判定は同じ。

## §5. 主張しないこと(PREREG §5 のまま + v4 の落とし)

- v4 も語の印。RETR の句は別の案に掛かる物を含む(b2_j01 の例)。
- v4 の PAR4 は本物の当たりを落とす(証明 1・本文 5)。v4 の値で olm113 / olm117 の外接線の印を引用する時は、この落としを添える。olm118 / olm120 の RESULT の本文は直さない(olm118 に追記)。
- 新しい model の出力はない。

## §6. 次(先生の言葉で)

- v5(起案はしない): PAR の主語を「O3 から出る線・半径でない」の除外で書き直し、「the line through / connecting Tc and Th / these two points / them」「tangents」を足して、較正にこの札の落とし 6 本を陰性 → 陽性の例として入れる。
- (a) olm119(折り返しの式)の RESULT は本走の終了後(v3 で読む・v4 / v5 の値は参考)。
