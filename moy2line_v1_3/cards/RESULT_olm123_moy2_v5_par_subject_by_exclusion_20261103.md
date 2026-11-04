HEAD(R1) = 65c3db14(執筆時の HEAD = 凍結の commit・fetch 済・origin より 22 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記(olm122・olm123)と TODO)

# RESULT(札 `olm123`・2026-11-03): 述語 v5(PAR の主語を除外で書く)— v4 の落とし 7 本は当たりに戻り、正しい落とし 7 本と prf5 の fable_r4 は落ちたまま(Q1 **直った**・予想 0.80 で当たり)。だが olm118 の Q3(外接線の印の olm117 − olm113 の差)は v5 でも **間**(Δ +0.063・Q2 **違う**・予想 0.20 で外れ)。理由は **v5 の新しい落とし 1 本**: olm113 の証明の欄 b2_j03「The radii O1Tc and O2Th are collinear (as the tangent is common), **so the line TcTh is thus parallel to the line O1O2**.」= 主語の窓の規則が「, so」を関係節(前の主語の続き)と読み、コンマの前(radii)で除外した。この一本を数えれば olm113 の外接線の印は 10 / 41 で v3 と同じ Δ +0.039(変わらない)。拾いすぎ 1 本(olm113 の本文 b2_j07「the line connecting O3 to the midpoint of Th and Tc is parallel to the line O1O2」= O3 から出る線の言い回しが除外の形に無い)。olm120 の判定は同じ。olm119 の v5 = 証明の欄 PAR5 3(v3 3・v4 2)・OUTER5 12(v3 12)= olm119 の判定に影響なし

- 札 = [PREREG](PREREG_olm123_moy2_v5_par_subject_by_exclusion_20261103.md)(凍結 65c3db14・HEAD(R1) 1ef817f4・G10 通る・台帳 済)・runner `ConstructGap/exp/olm123_moy2_v5_par_subject_by_exclusion_20261103.py`(model なし)・読み込むだけの部品 `olm118_…py`(`136f72b9…`・v3)・`olm121_…py`(`9c0b2b4e…`・v4 = PBIS・RETR・`_hits4`)・`olm117_…py`(`ab678f30…`)・`hq_moy12_…py`(`426e2089…`)・入力 8 本(olm113 / olm117 / prf5 / olm116 / olm119 の出力・olm118 / olm120 / olm121 の read.json)= guard で一致。
- 出力 = `ConstructGap/exp/olm123/read.json`(md5 `d343c253…`)・`read_run.log`。走り = zebrashark 11-03 18:52 JST(`--read`・数秒・olm122 の本走と並行 = 読みだけ)・Traceback 0。provenance = commit 65c3db14・dirty true(台帳の追記のみ)。
- 較正 = 98 / 98(v4 の 74 例を v5 の名で + 24)。陰性統制 = prf5 の証明 20 本(OUTER5_a 0・PT_a + LN_a 0)。
- 開示: PREREG §0 のとおり v3 / v4 の値は既知で、較正の 14 例は olm121 §3 の逐語(Q1 は回帰の検査)。v4 → v5 で変わった行のうち較正に無い 3 本(b2_j03・b2_j07・b2_j08)は未知で読んだ。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | md5 一致・較正 98 / 98(v3 54・v4 74 も) | 一致・98 / 98 | ✓ |
| G1(証明の欄) | prf5 で OUTER5_a ≤ 1 | 0 / 20(PAR5 の当たり 1 = fable_r4「O1O2 is not parallel to l1」= 否定 = asserted でない) | ✓ |
| G1(同) | PT_a + LN_a ≤ 1 | 0 / 20 | ✓ |

## §2. 判定

| Q | 値 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** v4 の落とし 7 本が戻り・正しい落とし 7 本 + prf5 は落ちたまま | 戻った 7 / 7(olm113 証明 b0_j16・本文 b0_j16 / b1_j12 / b2_j15・olm117 本文 b1_j10 / b1_j11 / b2_j03)・落ちたまま 7 / 7(olm113 本文 b0_j13 / b2_j07 の O3M・olm117 証明 b1_j13・本文 b1_j06 / b1_j13 / b2_j05・olm116 k1_1_j04)・prf5 fable_r4 本文 PBIS なし・証明 PAR 否定 | **直った**(16 / 16) | 直った **0.80** → 当たり |
| Q2 olm118 の Q1〜Q3・olm120 の Q1〜Q2 の判定が v3 と同じ | olm118: Q1 線対称 変わらない(Δ +0.030・同じ)・Q2 点対称 増える(+0.087・同じ)・**Q3 外接線 間(Δ +0.063・v3 は 変わらない +0.039・v4 も 間 +0.063)** / olm120: 下がる・下がる(同じ) | **違う**(5 つのうち 1 つ・v4 と同じ所) | v3 と同じ **0.80**・違う 0.20 → **外れ** |
| Q3 | 記述 | §3 | — |

- **Q3 の帯が v5 でも動いた理由(逐語)**: olm113 の証明の欄で b0_j16(v4 の落とし)は戻った(+1)が、**b2_j03 が新しく落ちた(−1)**: 「The radii O1Tc and O2Th are collinear (as the tangent is common), so the line TcTh is thus parallel to the line O1O2.」— PAR5 (A) の主語の窓は「最後のコンマの後が which / that / and / so / hence … で始まれば、コンマの前(先行詞)を取る」(「the segment TcTh, which is parallel」「O2Tc, which is parallel」の為)としたが、ここでは「, so」の後に**新しい主語「the line TcTh」**がある。コンマの前「The radii O1Tc and O2Th …」に半径があって除外した。olm113 の OUTER5_a は 9 / 41(0.220)で v4 と同じ数(中身は一本入れ替わり)・olm117 は 13 / 46(0.283)で v3 / v4 と同じ → Δ +0.063(境 0.06 を 0.003 越える)。b2_j03 を数えれば 10 / 41 で Δ +0.039 = v3 と同じ「変わらない」。**凍結の v5 の判定は「間」のまま置き、v5 の落としとして記す**(olm118 の RESULT には追記しない = PREREG §3 の読みの軸)。

## §3. Q3(記述・read.json の逐語)

### v4 → v5 で PAR の当たりが変わった行(全部・10 本)

| 腕 | 所 | 行 | v4 → v5 | 文(逐語) | 札 |
|---|---|---|---|---|---|
| olm113 | 証明 | b0_j16(MIDO3) | 0 → 1 | 「The inner common tangent at Tc on c and at Th on h1 is parallel to the line O1O2. Since O3 lies on O1O2 and is its midpoint, …」 | **正しい拾い**(v4 の落としが戻る・olm121 §2 の一本) |
| olm113 | 本文 | b0_j16 | 0 → 1 | 「… because O3 is the midpoint of O1 and O2, and the line through Tc and Th is parallel to O1O2 by the properties of inner common tangents.」 | 正しい拾い(並列「and」の後の主語) |
| olm113 | 本文 | b1_j12(MIDO3) | 0 → 1 | 「… the inner common tangent line l1, the line connecting these two points is parallel to the line connecting the centers of the circles, O1 and O2.」 | 正しい拾い(「these two points」= 接点) |
| olm113 | **証明** | **b2_j03(MIDO3)** | **1 → 0** | 「The radii O1Tc and O2Th are collinear (as the tangent is common), so the line TcTh is thus parallel to the line O1O2.」 | **v5 の落とし**(「, so」の後の新しい主語をコンマの前の続きと読んだ・§2) |
| olm113 | 本文 | b2_j07(EQ) | 0 → 1 | 「Alternatively, the line connecting O3 to the midpoint of Th and Tc is parallel to the line O1O2. Let's check.」(同じ行の「the line O3M, where M is the midpoint of TcTh, is parallel to O1O2?」は落ちたまま = Q1) | **v5 の拾いすぎ**(O3 から出る線だが、除外の形に「connecting O3 to …」が無い) |
| olm113 | 本文 | b2_j15(NONE) | 0 → 1 | 「… and since the radii are perpendicular to l1, the line O1O2 is parallel to the line connecting Tc and Th? Wait, no.」 | 正しい拾い(退けている = RETR) |
| olm117 | 本文 | b1_j10(MIDO3) | 0 → 1 | 「Wait, no, for congruent circles, the inner common tangents are parallel to the line connecting the centers? Wait, no.」 | 正しい拾い(複数形「tangents」・退けている) |
| olm117 | 本文 | b1_j11(MIDO3) | 0 → 1 | 「Wait, but for equal circles, the inner common tangents are parallel to the line connecting the centers? No, wait, actually for equal circles, the inner …」 | 正しい拾い(退けている) |
| olm117 | 本文 | b2_j03(NONE) | 0 → 1 | 「Since Tc and Th are points of tangency, the line connecting them is parallel to the line joining the centers of the circles, and hence, the points Tc, Th, and …」 | 正しい拾い(「them」= 接点) |
| olm117 | 本文 | b2_j08(MIDO3) | 0 → 1 | 「… and since they are on opposite sides (inner tangent), the line O1O2 is parallel to the line connecting the projections of O1 and O2 onto l1」 | 境の拾い(O1・O2 の l1 への射影は Tc・Th なので意味では「接線 ∥ O1O2」= 本物・偽) |

- 正しい拾い 7 + 境 1・v5 の落とし 1(証明)・拾いすぎ 1(本文)。v4 の正しい落とし 7 本(O3Tc・O3M・O3O3・半径・through O3)は全部 落ちたまま(Q1)。

### PAR の当たりの数(v3 / v4 / v5)と外接線の印(証明の欄)

| 腕 | 所 | n | PAR v3 / v4 / v5 | PERP3 | PBIS v3 / v4=v5 | OUTER v3 / v4 / v5 |
|---|---|---:|---|---:|---|---|
| olm113 | 証明 | 41 | 7 / 6 / **6** | 4 | 0 / 0 | 10 / 9 / **9**(0.244 / 0.220 / 0.220) |
| olm113 | 本文 | 60 | 23 / 18 / **22** | 21 | 1 / 1 | 30 / — / 29(asserted) |
| olm117 | 証明 | 46 | 8 / 7 / **7** | 4 | 2 / 2 | 13 / 13 / **13**(0.283) |
| olm117 | 本文 | 60 | 20 / 13 / **18**(asserted 17) | 24 | 5 / 5 | 33 / — / 32(asserted) |
| prf5 | 証明 | 20 | 0 / 1 / 1(否定・asserted 0) | 0 | 0 / 0 | 0 / 0 / 0 |
| olm116 k1 | 続き | 40 | 2 / 1 / **1** | 1 | 2 / 1 | 4 / 2 / **2**(0.05) |
| olm116 k2 | 続き | 38 | 0 / 0 / 0 | 0 | 0 / 0 | 0 / 0 / 0 |
| olm119(参考) | 証明 | 44 | 3 / 2 / **3** | 10 | 0 / 0 | 12 / 11 / **12**(0.273) |
| olm119(参考) | 本文 | 60 | 11 / 9 / **11** | 23 | 6 / 6 | 30 / 30 / 30 |

- olm119 の証明の欄の PAR5 3 本(逐語): b0_j00「… and O3 is the midpoint of O1O2, the line through Tc and Th is parallel to O1O2, hence Tc, Th, and O3 are collinear.」・b0_j08「… and O1O2 is perpendicular to l1 (inner common tangent); therefore TcTh is parallel to O1O2.」・b2_j18「… the segment TcTh is parallel to the line O1O2. The midpoint of TcTh is therefore the same as …」= v3 の 3 本と同じ。v4 は b0_j00 の「the line through Tc and Th」を落としていた。

### RETR / KEPT(本文・v5・行の数)

| 腕 | 印 | 口にした(asserted) | 退けた(RETR) | 残した(KEPT) |
|---|---|---:|---:|---:|
| olm113 | 接線 ∥ O1O2(PAR5) | 22 | 7 | 20 |
| olm113 | O1O2 ⊥ 接線(PERP3) | 21 | 12 | 17 |
| olm113 | 点対称 / 線対称 | 7 / 11 | 3 / 0 | 7 / 11 |
| olm117 | PAR5 | 17 | 9 | 13 |
| olm117 | PERP3 | 24 | 8 | 19 |
| olm117 | 点対称 / 線対称 | 10 / 11 | 1 / 1 | 9 / 10 |
| olm119(参考) | PAR5 | 11 | 6 | 8 |
| olm119(参考) | PERP3 | 23 | 9 | 21 |
| olm119(参考) | 点対称 / 線対称 | 9 / 33 | 3 / **9** | 7 / 33 |
| olm119(参考) | PBIS5 | 6 | 3 | 5 |

- v4 の RETR の数(olm121 §3: olm113 PAR4 18 / 5・olm117 13 / 7)と比べ、v5 は PAR の当たりが増えた分 退けた数も増える(22 / 7・17 / 9)。線対称は相変わらず退けられない(0 / 11・1 / 11)。olm119 の線対称 9 / 33 の退けは計算した行(RESULT olm119 §3.3 の 8 本 + 1)。

## §4. 主 session の読み(値と並べる・判定は変えない)

1. **除外で書く形は効いた**: v4 の落とし 7 本は全部戻り、v4 の正しい落とし 7 本(O3Tc・O3M・O3O3・半径・through O3)は保たれた(14 / 14)。主語の語を列挙するより落としが少ない(olm121 §4 の 1 の見込みどおり)。
2. **新しい落としは窓の規則から**: 「, so / and / hence の後」を「前の主語の続き(, and is parallel …)」と一律に読んだが、接続詞の後に**自分の主語**がある節(「, so the line TcTh is …」)がある。直し方 = 接続詞の後に語(名詞句)があればそこを主語の窓にし、動詞だけなら前の節へ戻る(v6 の材料・起案しない)。拾いすぎは除外の形の欠け(「connecting O3 to the midpoint」= O3 から出る線の言い回し)。
3. **olm118 の Q3 の帯は三版で 変わらない / 間 / 間**: 値は +0.039 / +0.063 / +0.063 で、境 0.06 の上下 0.003 の差。どの版でも「olm117(半径の等しい図)の方が外接線の印が多い」向きは同じで、帯の名は一行(0.024)で変わる。**外接線の印の計器は v5 で据える**(落とし 1 本・拾いすぎ 1 本を添えて引用する)。
4. **較正の限界(R6)**: Q1(較正の逐語を本文で読み直す回帰)は通ったが、較正に無い形(接続詞の後の主語)で落ちた。較正は文の形ごとに陽性統制を置く(接続詞・挿入句・並列・関係節)必要があり、本文の形は較正より多様 = 「計器は較正から」の較正の集合が主張の射程を決める(R5)。
5. olm119 への影響はない(v5 の値は v3 と同じ 3 本・12 本)。olm120 の判定も同じ。(e) の読みでは v5 を参考に並べる(判定は v3 + REFL)。

## §5. 主張しないこと(PREREG §5 のまま + v5 の落とし)

- v5 も語の印。窓の規則は接続詞の後の主語を落とし(証明 1)、「connecting O3 to …」を拾う(本文 1)。v5 の値で外接線の印を引用する時はこの二つを添える。
- RETR / KEPT の粗さは v4 のまま。
- olm118 / olm120 / olm121 の RESULT の本文は書き換えない(追記もしない = PREREG §3)。olm119 の判定は変えない。
- 新しい model の出力はない。

## §6. 次(先生の言葉で・起案はしない)

- v6: 接続詞(so / and / hence / thus / therefore)の後に名詞句があれば新しい節として主語の窓を取る・除外の形に「(line) connecting / joining / from O3 to …」を足す・較正に b2_j03 と b2_j07 の逐語を入れる。
- (e)「使って確かめよ」の腕は (d) olm122 の RESULT の後に凍結(読みは v3 + REFL で判定・v5 を参考)。
