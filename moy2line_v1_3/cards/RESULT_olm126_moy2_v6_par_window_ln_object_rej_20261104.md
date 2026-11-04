HEAD(R1) = b4030406(執筆時の HEAD = 凍結の commit・fetch + pull 済 = Already up to date・origin より 31 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記(olm126)だけ)

# RESULT(札 `olm126`・2026-11-04 朝): 述語 v6(PAR の主語の窓・LN の直の目的語と式の写し・REJ)— **Q1 直った**(PAR6 の回帰 19 / 19・olm118 の Q3 = 外接線の印の差は v6 で **変わらない(Δ +0.0387 = v3 と同じ値)** に戻る・予想 0.80 で当たり)・**Q2 同じ**(凍結の判定 7 / 7 が v6 でも同じ・名指した 8 行 8 / 8・LN6 の率 0.122 / 0.341 / 0.135 / 0.162 / 0.275 = §0 の見込みと一致・olm117 に直の目的語は 0 本で olm118 の Q1 は Δ +0.030 のまま・予想 0.60 で当たり)・**Q3 通らない**(予想 通る 0.75 = 外れ): olm125 の b0_j06 は落ち、足された 3 行(olm119 b1_j13・olm125 b0_j01 / b0_j15)は全部計算した行、b2_j07 の型の手の行 9 / 9 は含まれたが、**olm124 の b2_j03 が落ちた**。中身 = REJ5(olm125 の補助)がこの行で拾った語は「Wait, maybe I should use a **different** approach for reflection」(= 単独の different・REJ5 の拾いすぎ)で、本当の退けの文「Hmm, does this point relate to Th (7.6927, -3.2647)? **Not obviously.**」はどちらの語の表にも無い。REJ6 は規則どおり数えず、凍結の条件(olm124 の 12 本が残る)は満たさない = **判定は 通らない で置く**(落ちの正体は「残るべき 12 本」の側の拾いすぎ 1 + 退けの語の取りこぼし 1 = v7 の材料)。計器の値で言えば v6 は三つの直しを全部通し(§3)、凍結の判定は一つも動かなかった。

- 札 = [PREREG](PREREG_olm126_moy2_v6_par_window_ln_object_rej_20261104.md)(凍結 b4030406・HEAD(R1) 30b6ae31・G10 通る・台帳 済)・runner `ConstructGap/exp/olm126_moy2_v6_par_window_ln_object_rej_20261104.py`(md5 `d180725d…`・model なし・凍結後に触っていない)・読み込むだけの部品 8 本(hq・olm117・olm118・olm119・olm121・olm123・olm124・olm125)・入力 16 本(八腕の出力 + read.json 8 本)= guard で一致。
- 出力 = `ConstructGap/exp/olm126/read.json`(md5 `862327c3…`)・`read_run.log`。走り = zebrashark 11-04 08:36:38 JST(`--read`・数十秒)・Traceback 0。provenance = commit b4030406・dirty true(台帳の追記のみ)。
- 較正 = 144 / 144(v5 の 98 を v6 の名で + PAR6 9・LN6 20・REJ6 17)。陰性統制 = prf5 の証明 20 本(OUTER6_a 0・PT_a + LN6_a 0・PAR6 の当たり 1 = fable_r4「O1O2 is not parallel to l1」= 否定 = asserted でない)。
- 開示: PREREG §0 のとおり v3 / v5 の値・取りこぼし・拾いすぎは全部既知で、較正の多くは RESULT の逐語(Q1〜Q3 は回帰の検査)。較正に無い行で変わった物(§3)が未知の部分。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | 部品 8 本・入力 16 本の md5・較正 144 / 144(v3 54・v4 74・v5 98・olm125 15 も) | 一致 | ✓ |
| G1(証明の欄) | prf5 で OUTER6_a ≤ 1 | 0 / 20 | ✓ |
| G1(同) | PT_a + LN6_a ≤ 1 | 0 / 20 | ✓ |

## §2. 判定

| Q | 値 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** PAR6 の回帰 | 戻った 8 / 8(v4 の落とし 7 + v5 の落とし b2_j03)・落ちたまま 10 / 10(v4 の正しい落とし 7 + v5 の拾いすぎ b2_j07 + prf5 fable_r4 の 2)・olm118 の Q3: v3 変わらない(+0.0387)→ v4 間(+0.0631)→ v5 間(+0.0631)→ **v6 変わらない(+0.0387)**(olm113 の証明の欄 OUTER6_a 10 / 41・olm117 13 / 46) | **直った**(19 / 19) | 直った **0.80** → 当たり |
| Q2 凍結の判定 7 つ + 名指した 8 行 | olm118 Q1 線対称 変わらない(Δ +0.0302・同じ)・Q2 点対称 増える(+0.087)・olm120 Q1 下がる(−0.122)・Q2 下がる(−0.194)・olm119 Q1 上がる(Δ113 +0.219)・olm124 Q1 戻る(Δ113 +0.040・Δ119 −0.179)・olm125 Q1 上がる(Δ124 +0.113)= **7 / 7 同じ**・名指した 8 行 **8 / 8**(olm124 b0_j00 / b0_j17 / b2_j05 足され・b1_j01 外れ・olm125 b0_j12 / b1_j11・olm122 b1_j11・olm119 b2_j13 足され) | **同じ** | 同じ **0.60** → 当たり |
| Q3 REJ6 の回帰 | b0_j06 落ちた ✓・olm125 の残り 13 / 13 残った ✓・**olm124 の 12 本のうち b2_j03 が落ちた ✗**・足された 3 行(olm119 b1_j13・olm125 b0_j01・b0_j15)は全部計算した行 ✓・計算しない行に足された 0 ✓・b2_j07 の型の手の行 9 / 9 含む ✓(足された 0) | **通らない**(1 項目) | 通る **0.75** → **外れ** |
| Q4 | 記述 | §3 | — |

- **Q3 の落ちた 1 本(olm124 b2_j03・OTHER・T 8,849・逐語)**: 計算「Then the reflection P' of Tc is 2F - Tc ≈ … ≈ (4.9276, -6.1005). ⏎ Hmm, does this point relate to Th (7.6927, -3.2647)? **Not obviously.** Maybe I made a calculation error. Let me check again. ⏎ Wait, maybe I should use a **different** approach for reflection. Alternatively, perhaps the reflection of Tc across O1O2 is Th? If that's the case, …」— REJ5 の当たりは「a different approach」の different(REJ5 の語の表に単独の different がある = **REJ5 の拾いすぎ**)。REJ6 は単独の different を数えないので落ちる(規則どおり)。だが本文の退け「Not obviously.」は REJ5 にも REJ6 にも無い形(**退けの語の取りこぼし**)。PREREG の「olm124 の 12 本が残る」は REJ5 の 12 本をそのまま残るべき集合に置いたので、その中の拾いすぎ 1 本で通らない。判定は凍結のとおり 通らない で置き、v7 の材料(§6)に「Not obviously / not obvious / unclear」の形を足す。
- Q3 で**足された 3 行**(計算した行・正しい拾い): olm119 b1_j13「2*F - Tc x: … = 4.9420 y: … = -6.0981 ⏎ Now, is this equal to Th? Th = (7.6927, -3.2647) ⏎ No, the y-coordinate does not match, so Th is not the reflection of Tc.」(始まり = 「2F − Tc」= 無し・v6 で足した始まり)・olm125 b0_j01「2F − P = 2*(3.8497, -2.414) − (2.7678, 1.2685) = (7.6994, -4.… ⏎ Step 6. Now, is P' = Th? Th = (7.6927, -3.2647). The x-coordinates are close (4.93 ≠ 7.69), so Tc is not reflected to Th.」(≠)・olm125 b0_j15「Then P' = 2F - Tc ⏎ x': … ≈ 4.9356 ⏎ y': … ≈ -6.0985 ⏎ But Th is (7.6927, -3.2647). The computed reflection point (4.9356, -6.0985) doesn't match Th.」(較正 r11 の逐語)。

## §3. Q4(記述・read.json の逐語)

### 3.1 v5 → v6 で PAR の当たりが変わった行(全部・6 本)

| 腕 | 所 | 行 | v5 → v6 | 文(逐語) | 札 |
|---|---|---|---|---|---|
| olm113 | **証明** | **b2_j03**(OTHER) | **0 → 1** | 「The radii O1Tc and O2Th are collinear (as the tangent is common), so the line TcTh is thus parallel to the line O1O2.」 | **正しい拾い**(v5 の落としが戻る・較正 a01) |
| olm113 | 本文 | **b2_j07**(EQ) | **1 → 0** | 「Alternatively, the line connecting O3 to the midpoint of Th and Tc is parallel to the line O1O2. Let's check.」 | **正しい落とし**(v5 の拾いすぎ・較正 a06) |
| olm113 | 本文 | b0_j04(EQ) | 1 → 0 | 「the key invariant is that the line connecting O3 to the midpoint of TcTh is parallel to the line O1O2. Let's check.」 | 正しい落とし(較正に無い・同じ形) |
| olm122 | 本文 | b1_j13(NONE) | 1 → 0 | 「Wait, maybe the line connecting O3 to the midpoint of Th and Tc is parallel to O1O2. Earlier, the midpoint of Th and Tc is (5.23025, …」 | 正しい落とし(同じ形) |
| olm124 | 本文 | b0_j07(EQ) | 1 → 0 | 「maybe the line connecting O3 to the midpoint of TcTh is parallel to O1O2. Let's check. The midpoint of TcTh is (5.23025, …」 | 正しい落とし(同じ形) |
| olm122 | **証明** | b0_j08(MIDO3) | **0 → 1** | 「Thus, TcTh is perpendicular to O1Tc and O2Th, which means TcTh is parallel to O1O2. Since O3 is the midpoint of O1O2, the line through …」 | **正しい拾い**(較正に無い・「, which means TcTh」= 接続詞の後の新しい主語・v5 は先行詞「TcTh is perpendicular to O1Tc and O2Th」の半径で除外していた) |

- 「the line connecting O3 to the midpoint of …」は olm113 / olm122 / olm124 に **4 本**(較正の b2_j07 + 3)= O3 から出る線の言い回しとして定型で、除外に足した形が本文の同じ形を全部落とした(拾いすぎの残り 0)。
- 接続詞の後の新しい主語の規則は、較正の b2_j03 の他に olm122 の証明 b0_j08 を戻した(olm122 の証明の欄 OUTER6_a 7 → **8**・olm122 の判定は G1 で無し = 影響なし)。olm113 の証明の欄 OUTER6_a は 9 → **10**(= v3 の 10 と同じ数・中身は b2_j03 が戻り b0_j16 も入ったまま)。
- 六腕の本文で PAR6_a: olm113 22 → 20・olm122 17 → 16・olm124 23 → 22(落としの 3 本)・ほか同じ。

### 3.2 v3 → LN6 で LN_a が変わった行(全部・9 行 14 欄)

| 腕 | 所 | 行 | v3 → v6 | 文(逐語) | 形 | 札 |
|---|---|---|---|---|---|---|
| olm119 | 証明 | b2_j13(MIDO3) | 0 → 1 | 「Reflect Tc across the line O1O2; by the definition of the inner common tangent and the reflection property, the image is Th.」 | 直の目的語(the image is Th) | 正しい拾い(較正 l07) |
| olm122 | 証明 | b1_j11(EQ) | 0 → 1 | 「Reflecting Tc across the line O1O2 yields Th by the tool. Since O3 is the midpoint of O1O2, …」 | 直の目的語 | 正しい拾い |
| olm122 | 本文 | b2_j02(MIDO3) | 1 → 0 | 「# Tool Reflection of P across O1O2: P′ = 2F − P, F = O1 + t(O2−O1), …」(問いの文の Tool の段の写し) | 式の写し | **正しい落とし**(較正に無い・問いの文の丸写しが v3 の LN に入っていた) |
| olm124 | 証明 + 本文 | b0_j00(MIDO3) | 0 → 1 | 「Reflecting Th over O1O2 yields Tc due to circle symmetry.」 | 直の目的語 | 正しい拾い(較正 l01) |
| olm124 | 証明 + 本文 | b0_j17(MIDO3) | 0 → 1 | 「Under this reflection, circle c (center O2) maps to circle h1 (center O1), and the inner tangent line l1 maps to itself. Hence the reflection swaps the contact points Tc↔Th.」(その前に「Reflect O3 across the line O1O2」) | 入れ替え | 正しい拾い(較正 l08) |
| olm124 | 証明 + 本文 | b1_j01(MIDO3) | 1 → 0 | 「Then P' = 2F − P is the reflection of P across O1O2. Applying this to Th, we get Th' = 2F − Th.」 | 式の写し | 正しい落とし(較正 n01・本文では 2 当たりとも落ちる) |
| olm124 | 本文 | b1_j05(EQ) | 1 → 0 | 「But reflection requires the tool given. The tool says reflection of P across O1O2 is P' = 2F - P, where F is the projection of P on …」 | 式の写し | 正しい落とし(較正に無い・道具の説明の写し) |
| olm124 | 証明 | b2_j05(OTHER) | 0 → 1 | 「Because reflecting Tc across O1O2 gives Th, the segment TcTh is perpendicular to O1O2」 | 直の目的語 | 正しい拾い(較正 l02) |
| olm125 | 証明 | b0_j12(MIDO3) | 0 → 1 | 「This can be seen by reflecting Th across O1O2 to Tc, and noting that the midpoint O3 is equidistant from O1 and O2」 | 直の目的語(to Tc) | 正しい拾い(較正 l05) |
| olm125 | 本文 | b0_j18(OTHER) | 1 → 0 | 「# Tool (available if you need it) Reflection of a point P across the line O1O2: P' = 2F − P, where F = …」(問いの文の丸写し) | 式の写し | 正しい落とし(較正に無い・olm125 §3.3 の「指示の写し 1 本」) |
| olm125 | 証明 | b1_j11(EQ) | 0 → 1 | 「By symmetry, reflecting Tc over O1O2 yields Th. Since O3 lies on O1O2, it is equidistant from Tc and Th」 | 直の目的語 | 正しい拾い(較正 l06) |

- 較正に無い変化は **3 本、全部が式の写し(問いの文の Tool の段か道具の説明の写し)の落とし** = v3 は問いの文の丸写しを本文の線対称に数えていた(olm122 b2_j02・olm125 b0_j18・olm124 b1_j05 = 本文の LN_a が 23 → 22・30 → 29・24 → 24(b0_j00・b0_j17 が足され b1_j01・b1_j05 が落ちる))。証明の欄に直の目的語の仮定の文(asserted でない)・仮の名の文は 0 本(直の目的語の当たりで direct_hyp は六腕の証明の欄で 0)。
- **olm117(半径の等しい図)に直の目的語は 0 本**: 証明の欄の LN6_a 7 = v3 の 7(全部「symmetric with respect to the line connecting the centers」の v3 の形)。olm118 の Q1 は動かない。
- 六腕の証明の欄(v3 → v6): 

| | olm113 | olm117 | olm119 | olm122 | olm124 | olm125 |
|---|---|---|---|---|---|---|
| n_proof | 41 | 46 | 44 | 37 | 37 | 40 |
| LN_a(v3)→ **LN6_a** | 5 → **5**(0.122) | 7 → **7**(0.152) | 14 → **15**(0.341) | 4 → **5**(0.135) | 4 → **6**(0.162) | 9 → **11**(0.275) |
| PT_a | 0 | 4 | 0 | 0 | 1 | 1 |
| OUTER5_a → **OUTER6_a** | 9 → **10**(0.244) | 13 → **13**(0.283) | 12 → **12** | 7 → **8** | 9 → **9** | 10 → **10** |
| PAR6_a / PERP3_a / PBIS6_a | 7 / 4 / 0 | 7 / 4 / 2 | 3 / 10 / 0 | 3 / 5 / 0 | 3 / 7 / 0 | 2 / 7 / 1 |
| LN6_r(退け)/ LN6_k | 0 / 5 | 0 / 7 | 0 / 15 | 0 / 5 | 0 / 6 | 0 / 11 |
| kind6 | — 30・NONE 6・LN 5 | — 28・NONE 8・LN 6・PT 3・BOTH 1 | — 22・LN 15・NONE 6・OTH 1 | — 24・LN 5・NONE 6・OTH 2 | — 22・LN 6・NONE 8・PT 1 | — 22・LN 10・NONE 7・BOTH 1 |

- 本文の RETR / KEPT(v6): LN6_a / LN6_r / LN6_k = olm113 11 / 0 / 11・olm117 11 / 1 / 10・olm119 33 / 9 / 33・olm122 22 / 2 / 21・olm124 24 / 12 / 23・olm125 29 / 11 / 29。OUTER6_a / _r / _k = 28 / 14 / 26・32 / 12 / 28・30 / 13 / 29・32 / 10 / 30・35 / 15 / 32・32 / 12 / 31。

### 3.3 REJ → REJ6 で変わった行(全部・5 本)と REJ6 の数

| 腕 | 行 | REJ5 → REJ6 | 文(逐語) | 札 |
|---|---|---|---|---|
| olm125 | b0_j06(EQ) | 1 → 0 | 「3.6550 = t*(-3.6689) => t = 3.6550 / -3.6689 ≈ -0.997 ⏎ So t is not the same for both」(共線の媒介変数) | 正しい落とし(較正 r14) |
| olm124 | b2_j03(OTHER) | 1 → 0 | 「(4.9276, -6.1005). ⏎ Hmm, does this point relate to Th (7.6927, -3.2647)? Not obviously. … Wait, maybe I should use a different approach for reflection.」 | **REJ5 の拾いすぎ(different)が落ち、本当の退け「Not obviously」は両方の取りこぼし**(§2) |
| olm119 | b1_j13(EQ) | 0 → 1 | 「2*F - Tc x: … = 4.9420 y: … = -6.0981 ⏎ Now, is this equal to Th? … No, the y-coordinate does not match, so Th is not the reflection of Tc.」 | 正しい拾い(始まり「2F − Tc」= 無し) |
| olm125 | b0_j01(EQ) | 0 → 1 | 「2F − P = … = (7.6994, -4.…) … Step 6. Now, is P' = Th? Th = (7.6927, -3.2647). The x-coordinates are close (4.93 ≠ 7.69), so Tc is not reflected to Th.」 | 正しい拾い(≠) |
| olm125 | b0_j15(OTHER) | 0 → 1 | 「The computed reflection point (4.9356, -6.0985) doesn't match Th. So maybe the reflection of Tc isn't Th.」 | 正しい拾い(較正 r11) |

- REJ6 の数(本文・七腕): olm113 0(計算した行 4)・olm117 0(0)・prf5 0・olm119 **11**(REJ5 10・計算 12)・olm122 6(6・9)・olm124 **11**(12・14)・olm125 **15**(14・15)。計算した行のうち退けた率 = olm119 11 / 12・olm122 6 / 9・olm124 11 / 14・olm125 15 / 15。
- b2_j07 の型(REJ6 ∧ 証明の欄 LN6_a)= olm113 0・olm119 3(b0_j13・b1_j06・b2_j08)・olm122 2(b1_j11・b2_j07)・olm124 1(b2_j07)・olm125 3(b1_j11・b1_j17・b2_j19)= RESULT olm125 §3.3 の手の数と行がそのまま一致(足し引き 0)。

## §4. 主 session の読み(値と並べる・判定は変えない)

1. **三つの直しは全部、較正の文の外でも同じ向きに働いた**: 「connecting O3 to the midpoint」は較正の 1 本の外に 3 本あって全部落ち(定型句)、式の写しは較正の 1 本の外に 3 本あって全部落ち(問いの文の Tool の段の丸写し = v3 が「本文の線対称」に数えていた)、接続詞の後の主語は較正の外で 1 本戻した(olm122 b0_j08)。拾いすぎの新規 0・落としの新規 0(§3.1〜3.2)。
2. **凍結の判定は計器の形に依らない**(Q2 7 / 7): 五腕の線対称の率は v3 → v6 で +0.000 / +0.023 / +0.027 / +0.054 / +0.050 動いたが、どの帯の境も越えない。olm118 の Q3 は v3 の値(+0.0387)に戻り、v4 / v5 の「間」は窓の規則の落としだった(olm123 §4 の 3 の見込みどおり)= **外接線の印の計器は v6 で据える**。
3. **REJ の難しさは語の表にある**: 退けの語は「not the same / is not Th / doesn't match / ≠」の他に「Not obviously」(olm124 b2_j03)のような弱い形があり、逆に「different」は「a different approach」で拾いすぎる。v6 は後者を直して前者を落とした。「残るべき集合」を REJ5 の出力で置いたことが Q3 の設計の弱さ(拾いすぎを含む集合を回帰の基準にした)で、次は手で読んだ行の集合を基準にする(§6)。
4. 始まりに「2F − Tc」(= 無し)を足したことで、式を接点に当てた行の退けが 3 本増えた(olm119 b1_j13・olm125 b0_j01 / b0_j15)= 計算した行の退けの率は olm125 で 15 / 15(全部)・olm124 で 11 / 14。計算した行は、ほぼ全部が折り返しを退ける。
5. 較正の限界(R6): 回帰の検査(較正の逐語を本文で読み直す)は三つとも通り、未知の部分(較正に無い行)でも落とし・拾いすぎは出なかったが、Q3 の基準の集合に拾いすぎが混じっていた = 計器の較正だけでなく、**比べる元の集合も述語(手で読んだ陽性)で作る**(R5)。

## §5. 主張しないこと(PREREG §5 のまま + v6 の落とし)

- v6 も語の印。「Not obviously / not obvious / unclear / hard to see」の退けは読まない(olm124 b2_j03)。主語の窓・像の窓・退けの窓は粗いまま。
- 凍結の RESULT(olm118 / 120 / 121 / 123 / 119 / 122 / 124 / 125)は書き換えない(追記もしない)。olm118 の Q3 が v6 で 変わらない に戻ったことはこの札に置く。
- REJ6 ∧ LN6 の共起(b2_j07 の型)は同じ命題の退けと復活とは限らない。
- 新しい model の出力はない。

## §6. 次(先生の言葉で・起案はしない)

- v7 の材料: 退けの語に「not obvious(ly) / unclear / hard to see / does not seem」を足す(較正に olm124 b2_j03 の逐語)・Q3 型の回帰は基準の集合を手で読んだ陽性で作る。
- (e') の残り = 同じ問いの文(olm125・md5 `718d1601…`)の走らせ直し、対照の一行(reflection の語だけ置く)は先生の裁定。読みは v3 で判定し v6 を参考に並べる(olm122 以降の型)。

## 訂正(冷間監査・2026-11-04 夜・U4)
- §3.3「計算した行のうち退けた率 = olm119 11 / 12・olm122 6 / 9・olm124 11 / 14・olm125 15 / 15」と §4 の 4「olm125 で 15 / 15(全部)」は、全行の REJ6 の総数を分子にした比。行の集合(read.json の rows の `calc` ∧ `rej6`)では **olm119 10 / 12・olm122 5 / 9・olm124 11 / 14・olm125 14 / 15**(calc の外の退け = olm119 b2_j08・olm122 b1_j19・olm125 b0_j09 / calc だが退けていない = olm125 b1_j15・主 session が read.json で再計算)。読み(計算した行はほぼ全部が退ける)は変わらない。
