HEAD(R1) = 63f8a35c(執筆時の HEAD・origin の 1 commit を merge 済み・origin より 7 commit 先・遅れ 0)

# RESULT(札 `olm116`・2026-11-03): frontier(Opus 5.5 / Fable 5.1・prf5)の **moy-2** の証明の欄を OLMo-3 32B base に段で与えると、続きは書く — k = 1(半径 ⊥ 接線と足 / 平行の設定まで)で続きが「O3 の足 = TcTh の中点 → 垂直二等分線か等距離」を満たす 21 / 40 = 0.525(Q1 **続ける**・予想は 0.20 で最も低く置いた側・境まで 0.025)・射影の事実 → 結論の順(USE_PROJ)18 / 40・k = 2(足 = 中点の段まで)で「垂直二等分線か合同」で閉じる 19 / 40 = 0.475(Q2 **間**・予想は続ける 0.55)— family の差が大きい(k = 1 で Fable の文 15 / 20・Opus の文 6 / 20・Opus の続きは対称 5・共線 4)— 逐語 10 本のうち射影の推論を正しく書いたのは 4〜5 本で、残りは数値の確かめ・退化の主張(M = O3)・循環 — (B) forward は統制を通り、段の語の先読み = 中点・二等分線の語は 3〜4 token 前まで・足 / 射影の語は 3 token・commit 係数は −7.6 → −5.7 → −3.6(olm114 と同じ単調)

- 札 = [PREREG](PREREG_olm116_moy2_frontier_proof_prefix_ladder_20261103.md)(凍結 2559082a・HEAD(R1) 2c8d7e21・G10 の台帳 済)・runner `ConstructGap/exp/olm116_moy2_frontier_proof_prefix_ladder_20261103.py`・凍結の部品 `hq_moy12_status_proof_common_20261102.py`(`426e2089…`)・frontier の出力 = `results_prf5_20261102.jsonl`(`995650e5…`・guard で一致)。
- 出力 = `ConstructGap/exp/olm116/gen.json`(md5 `e66433f2…`)・`read.json`(`fda0f3dc…`)・`series/*.npz`(20 本・0.9 MB)・`gen_run.log`・`fire_run.log`・`read_run.log`・`chain_olm116.log`。
- 走り = zebrashark・11-03 12:26:37 `--gen` → 12:39:06(749 s・k1 292 + 158 s・k2 161 + 133 s)→ `--fire` → 12:40:49(103 s)→ `--read` → 12:41:01。Traceback 0。gen / read の provenance = commit 2559082a・dirty false。prompt md5 `9960091f…`(prf5 の M2B + cue)・prereg md5 `9b0aefa0…`。
- 較正 = hq 61 / 61 + この札の 29 / 29(guard)。書き出しは `conjecture` と `proof` の二欄だけ(`reason` なし)。k = 0 の腕は置いていない(PREREG §0)。
- 開示: gen の log は batch ごとに Q1 / Q2 の数を印字する作りで、主 session は生成中に k1_0 の行(Q1 11・Q2 11)を目にした。判定は read.json の値で付けた。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G1(k = 1) | 生成が空でない行 ≥ 24 | 40(閉じた 40・空の続き 0) | ✓ |
| G1(k = 2) | 同上 | 40(閉じた 40・空の続き 2 = JSON を即座に閉じた) | ✓ |
| (B) C1 | J-lens の cos > 恒等の cos が行の 95 % 以上 | 20 / 20(中央値 0.689 対 0.521) | ✓ |
| (B) C3 | 方向のノルム = olm4 の記録 | 19.647 = 19.647 | ✓ |
| (B) round_trip | — | 通る | ✓ |

## §2. 判定

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** | k = 1 の続きが MID2 ∧ (PB2 ∨ EQD): 21 / 40 = **0.525** | **続ける**(≥ 0.50・境まで 0.025) | 続ける **0.20**・続けない 0.35・間 0.45 → **外れ(最も低く置いた側)** |
| Q2 | k = 2 の続きが PB2 ∨ CONG2: 19 / 40 = **0.475** | **間**(0.10 < 0.475 < 0.50・境まで 0.025) | 続ける 0.55・間 0.30・続けない 0.15 → 外れ |
| Q3 | 記述 | §3 | — |

- 両方とも境のすぐ近く(0.025)。Q1 は olm114(moy-1・0.65)と同じ向きに外れた = 段を与えた時の OLMo の続きを、主 session は二枚続けて低く見た。Q2 は逆に高く見た: k = 2 の残りは短く(中央値 125 字・T 74)、OLMo は「垂直二等分線」や合同を言わずに **O3Tc = O3Th を言い直して閉じる**(EQD 32 / 40・PB2 19)。
- USE_PROJ(射影の事実 → 結論の順)= k = 1 で 18 / 40。MID2 を言った 22 本のうち 21 本が結論まで書いた(olm115 の PERPB_only = 0 と同じ: 事実を言えば結論は続く)。

## §3. Q3(記述・read.json の逐語)

### 続きの述語(続きだけに当てた)

| 腕 | n | 凍結 PROJ / PERPT / TRAP / PB / MIDTT / COORD / ALG / CONG | 凍結の route | v2 MID2 / PROJAFF / PB2 / EQD / CONG2 | Q1 | Q2 | USE_PROJ | SYMM / PAR / HOMO / POWER / COLL | status | T 中央値 | 字数 中央値 |
|---|---:|---|---|---|---:|---:|---:|---|---|---:|---:|
| k = 1 | 40 | 22 / 3 / 6 / 24 / 12 / 2 / 4 / 1 | PROJ 22・TRAP 6・OTHER 9・ANALYTIC 2・CONG 1 | 22 / 3 / 21 / 36 / 1 | **21** | 21 | 18 | 5 / 2 / 2 / 0 / 4 | hyp 35・other 3・question 1・none 1 | 169.5 | 361 |
| k = 1 Opus の文 | 20 | 10 / 1 / 1 / 13 / 5 / 1 / 1 / 0 | PROJ 10・OTHER 8 | 6 / 0 / 10 / 18 / 0 | **6** | 10 | 4 | **5** / 0 / 1 / 0 / **4** | hyp 16・other 2・question 1・none 1 | 171 | 344 |
| k = 1 Fable の文 | 20 | 12 / 2 / 5 / 11 / 7 / 1 / 3 / 1 | PROJ 12・TRAP 5 | 16 / 3 / 11 / 18 / 1 | **15** | 11 | 14 | 0 / 2 / 1 / 0 / 0 | hyp 19・other 1 | 168.5 | 420 |
| k = 2 | 40 | 15 / 2 / 0 / 21 / 11 / 0 / 1 / 0 | PROJ 15・OTHER 25 | 17 / 0 / 19 / 32 / 0 | 15 | **19** | 13 | 0 / 0 / 0 / 0 / 0 | hyp 35・other 4・none 1 | 74 | 125 |
| k = 2 Opus の文 | 20 | 9 / 0 / 0 / 11 / 10 / 0 / 0 / 0 | PROJ 9・OTHER 11 | 11 / 0 / 9 / 17 / 0 | 9 | 9 | 8 | 0 | hyp 17・other 2・none 1 | 78 | 119.5 |
| k = 2 Fable の文 | 20 | 6 / 2 / 0 / 10 / 1 / 0 / 1 / 0 | PROJ 6・OTHER 14 | 6 / 0 / 10 / 15 / 0 | 6 | 10 | 5 | 0 | hyp 18・other 2 | 72 | 126.5 |

- k = 1 で Q1 を満たした 21 本 / 満たさなかった 19 本: 満たした側は route PROJ 16・TRAP 3、偽の前提の印は PAR 2・SYMM 1。満たさなかった側は route OTHER 9・PROJ 6・TRAP 3、印は **SYMM 4・COLL 4・HOMO 2**、PB2 11・EQD 15(= 結論は言うが、足 = 中点の段が無い)。
- **family の差**(olm114 / 115 と同じ型の差): Fable の `Step n (題):` の型は題に「midpoint projection」「perpendicular bisector」を置けば段が埋まり、Opus の `n)` の型では OLMo が対称性・共線・相似の中心へ流れる(Opus の続きの SYMM 5・COLL 4・HOMO 1 対 Fable 0・0・1)。olm115 の moy-1 では直交の事実の使用に family 差が無かった(7 / 6)が、moy-2 では射影の段で差が出た。
- JSON の後の文字(tail)が 0 でない行 = 6 / 80。上限 1536 で切れた行 0。

### (B) forward(記述・統制は §1)

- **先読み**(証明の領域で語の集合が最初に出る位置 w の k token 前の u(w − k) が top 5 に入る行の割合・J-lens・層 48・null の p95 = 0.15〜0.20):

| 集合(n) | k = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PROJ ` project`・` projection`・` foot`(20) | 0.75 | 0.70 | 0.50 | 0.15 | 0.00 | 0.10 | 0.05 | 0.05 |
| PERPT ` perpendicular`(20) | 1.00 | 0.95 | 0.20 | 0.00 | 0.00 | 0.00 | 0.15 | 0.35 |
| MID ` midpoint`(20) | 1.00 | 0.95 | 0.70 | 0.50 | 0.40 | 0.05 | 0.15 | 0.40 |
| PB ` bis`(20) | 1.00 | 0.85 | 0.65 | 0.70 | 0.15 | 0.10 | 0.20 | 0.05 |
| ATTR ` coll`・` symmetric`・` symmetry`(0) | —(frontier の証明に無い) | | | | | | | |

  logit lens も同じ形(PROJ 0.80 / 0.65 / 0.50 / 0.20 …・MID 1.00 / 0.95 / 0.65 / 0.30 / 0.35 …・PB 1.00 / 0.85 / 0.65 / 0.15 …)。
- **切れ目の前後 32 token の窓の中央値**(20 行):

| 切れ目 | proj32 前 → 後 | u(PROJ) | u(PERPT) | u(MID) | u(PB) | u(ATTR) |
|---|---|---|---|---|---|---|
| k1(設定の段の終わり) | −7.62 → −5.26 | 0.63 → 0.64 | 0.68 → 0.52 | **0.52 → 0.68** | 0.56 → 0.56 | 0.52 → 0.47 |
| k2(足 = 中点の段の終わり) | −5.71 → −4.61 | 0.62 → 0.55 | 0.53 → 0.68 | 0.69 → 0.62 | **0.53 → 0.68** | 0.53 → 0.57 |
| 証明の終わり(前だけ) | −3.64 | 0.47 | 0.53 | 0.50 | 0.49 | 0.53 |

- 切れ目の後で上がるのは次の段の語(k1 の後に中点・k2 の後に二等分線)。commit 方向の係数は k1 → k2 → 終わりで単調に上がる(olm114 の −7.6 → −5.4 → −3.7 と同じ形)。語の集合ごとの陽性統制は無いので記述。

## §4. 逐語(PREREG §4 = k = 1: Q1 を満たした物を行の名の順に 10 本・満たさなかった物を 4 本おきに最大 10 本 / k = 2: 同じ型で各 5 本)

### k = 1・満たした 10 本(21 本中)

- **k1_0 fable_r0**(T 276・637 字・hypothesis・route ANALYTIC・MID2 PB2 EQD USE_PROJ)
  > Step 4 (midpoint O3 of O1O2): O3 = (O1+O2)/2 = (3.9524, −2.3865). Step 5 (midpoint M of TcTh): M = (Tc+Th)/2 = (5.2303, −0.9981). Step 6 (perpendicular-bisector theorem): in any line, the set of points equidistant from the two endpoints is the perpendicular bisector. We will show O3 is equidistant from Tc and Th. Step 7 (distance O3Tc): compute ||O3−Tc|| ≈ √(1.1843² + 3.6549²) ≈ 3.817. Step 8 (distance O3Th): compute ||O3−Th|| ≈ √(3.7403² + 1.3882²) ≈ 3.817. Step 9 (equal distances ⇒ perpendicular bisector): since O3Tc = O3Th, O3 lies on the perpendicular bisector of TcTh. Equivalently, ∠(O3−M)Tc = 90°. Thus the invariant holds.

  L3: 座標で距離を計算して等しいと言う(olm113 の b0j9 と同じ「数値の確かめ」)。MID2 は M の定義(M = (Tc+Th)/2)で付いた。射影の推論は無い。
- **k1_0 fable_r2**(T 172・261 字・hypothesis・PROJ・MID2 EQD USE_PROJ)
  > 4. O3 is the midpoint of O1 and O2, so O3 = (O1+O2)/2. 5. The midpoint M of Tc and Th is ((Tc+Th)/2) = ((O2+O1)/2) = O3, because Tc and Th are projections of O1 and O2 onto the same line. 6. Thus TcTh passes through O3 and O3 is its midpoint, i.e. O3Tc = O3Th.

  L3: **M = O3**(TcTh が O3 を通る)= 退化の主張で、この図では偽(半径が違う・olm117 の図でだけ真)。射影の語は使うが推論は誤り。
- **k1_0 fable_r3**(T 507・1,496 字・other・PROJ・MID2 PROJAFF PB2 EQD USE_PROJ・PAR)
  > 4. O3 is the midpoint of the segment O1O2, so O3 lies on the line O1O2 and is its midpoint (definition of midpoint). 5. The projection π is a linear mapping along the direction perpendicular to l1; it sends lines parallel to l1 to themselves, and it is an affine map. 6. Since O3 lies on line O1O2, its image π(O3) under projection onto l1 lies on line π(O1)π(O2); but π(O1) = Th and π(O2) = Tc, so π(O3) lies on line ThTc. 7. The projection π is a linear map whose kernel is the direction perpendicular to l1; in particular, π maps the direction O1O2 to the direction ThTc. 8. Now O1O2 is parallel to ThTc, because both are perpendicular to the same line l1 (from steps 1,2 and 3). 9. Hence the projection π sends the direction O1O2 into the direction ThTc. 10. But O3 is on O1O2, so π(O3) is on ThTc. 11. Moreover, the projection π carries midpoints on O1O2 to midpoints on ThTc: since π is a linear map, π(O3) = midpoint of π(O1) and π(O2) = midpoint of Th and Tc. 12. Therefore, π(O3) is the midpoint of Th and Tc. 13. Hence O3Tc = O3Th (distance from O3 to its projection on l1 is the same in either direction). 14. Equivalently, triangle Tc O3 Th is isosceles at O3, so O3 lies on the perpendicular bisector of TcTh. 15. Alternatively, if M is the midpoint of TcTh, then O3M is the line joinin(以下略)

  L3: 11〜12 は正しい射影の推論(affine → 中点を保つ)。8 の「O1O2 ∥ ThTc」は偽。13 の理由付けは意味を成さない。正しい段と偽の段が混ざる。
- **k1_0 fable_r4**(T 202・399 字・hypothesis・TRAP・MID2 EQD USE_PROJ)
  > 4. O3 is the midpoint of O1O2, so O3M = midpoint(O1O2) = midpoint of the two base‐endpoints of that trapezoid. 5. In a trapezoid, the line joining midpoints of the non‐parallel sides equals the line joining midpoints of the parallel sides, and is perpendicular to those bases. 6. Thus the segment joining O3 to M = midpoint(Tc, Th) is perpendicular to TcTh; equivalently O3Tc = O3Th and O3M ⟂ TcTh.

  L3: 台形の中線の言い方は崩れているが、結論(O3M ⟂ TcTh at the midpoint)は正しい形。
- **k1_0 fable_r5**(T 214・645 字・hypothesis・PROJ・MID2 EQD USE_PROJ)
  > Step 4 (O3 midpoint of O1O2): by definition O3 is the midpoint of O1O2, so O3 is the midpoint of the segment joining O1 and O2. Step 5 (midpoint of feet of perpendiculars): in any line, the midpoint of the feet of the perpendiculars from two points lies on the line perpendicular to that line at the midpoint of the two points. Equivalently, the segment O1O2 projects to a segment on l1 whose midpoint is the foot of the perpendicular from O3 to l1. Hence O3 is the foot of the perpendicular from O3 to l1, i.e. O3M ⊥ l1. Step 6 (conclude right angle): Since M = midpoint(Tc, Th), M lies on l1 and O3M ⊥ l1, so ∠O3MTc = 90°, giving O3Tc = O3Th.

  L3: Step 5 の前半は正しい原理(足の中点 = 中点の足)。「O3 is the foot of the perpendicular from O3」は崩れ。結論は正しい。
- **k1_0 fable_r6**(T 136・402 字・hypothesis・PROJ・MID2 PB2 EQD USE_PROJ)
  > Step 4 (midpoint projection): the projection of a point onto a line is onto the closest point on the line; the foot M of the perpendicular from O3 onto l1 is the projection of the midpoint O3 of O1O2 onto l1. Step 5 (midpoint of TcTh): by the projection property of midpoints, M = midpoint of TcTh. Step 6 (right angle): O3M ⊥ TcTh, so O3 lies on the perpendicular bisector of TcTh, hence O3Tc = O3Th.

  L3: **正しい鎖**(射影の性質 → M は中点 → 垂直二等分線 → 等距離)。
- **k1_0 fable_r7**(T 165・532 字・hypothesis・PROJ・MID2 PB2 EQD USE_PROJ)
  > Step 4 (midpoint of O1O2): O3 is defined as the midpoint of segment O1O2, hence the vector from O3 to O2 equals the vector from O1 to O3. Step 5 (projection midpoint): projective property of midpoints: the projection of the midpoint of two points onto a line is the midpoint of their projections. Therefore the foot M of the perpendicular from O3 to l1 is the midpoint of Tc and Th. Step 6 (perpendicular bisector): since M is the midpoint of TcTh and O3M ⟂ TcTh, O3 lies on the perpendicular bisector of TcTh, forcing O3Tc = O3Th.

  L3: **正しい鎖**。
- **k1_0 fable_r8**(T 119・283 字・hypothesis・TRAP・MID2 EQD)
  > 4. Thus O2−O1 is parallel to the segment Th−Tc. 5. O3 is the midpoint of O1O2, so by the midpoint‐bisector property in a trapezoid (or by vector addition) O3 is the midpoint of Th−Tc. 6. Hence O3Tc = O3Th (isosceles triangle at O3) and angle O3MTc = 90° where M is midpoint of TcTh.

  L3: 「O1O2 ∥ ThTc」偽・「O3 は ThTc の中点」= 退化の主張(偽)。
- **k1_0 opus_r2**(T 160・497 字・other・PROJ・MID2 PB2 EQD)
  > Therefore l1 is perpendicular to both O2Tc and O1Th. 3. The line through O3 parallel to l1 is the line through O3 perpendicular to both O2Tc and O1Th. Hence that line is perpendicular to the line joining Tc and Th, because Tc–Th is the intersection of the two lines perpendicular to O2Tc and O1Th, respectively. 4. Since O3Tc = O3Th, O3 is equidistant from Tc and Th, so it lies on the perpendicular bisector of TcTh. In fact the foot of the perpendicular from O3 to TcTh is the midpoint of TcTh.

  L3: 4 は循環(結論から結論)。MID2 は最後の一文で付いた。
- **k1_0 opus_r7**(T 185・354 字・hypothesis・PROJ・MID2 EQD USE_PROJ)
  > Step 4 (midpoint invariance under projection): since O3 is the midpoint of O1O2, its projection onto any line is the midpoint of the projections of O1 and O2. Therefore the projection of O3 onto TcTh is the midpoint of {Tc, Th}. Step 5 (perpendicular bisector property): that midpoint is the foot of the perpendicular from O3 to TcTh. Hence O3Tc = O3Th.

  L3: **正しい鎖**(Opus の文の続きで Step の型になっているのは、frontier の opus_r7 自身が `Step n (題):` で書いているから)。

### k = 1・満たさなかった 5 本(19 本中・4 本おき = 0・4・8・12・16 番目)

- **k1_0 fable_r1**(T 153・483 字・hypothesis・OTHER・MID2・HOMO)
  > 4. By Thales’ theorem on the parallel lines l1 and O1 Th, the segment joining their intersection points with any transversal is divided proportionally; in particular, line O3 Tc meets l1 at Th and meets O1 Th at the foot M of the perpendicular from O3 to Th (since O3 lies on the line joining the centers O1 and O2, the homothety centered at the intersection of l1 and O1 Th sends O1→O2 and Th→Tc). 5. Hence triangle Tc Th O3 is right isosceles at M, and M is the midpoint of Tc Th.

  L3: 「l1 ∥ O1Th」偽(直交)。定理の名(Thales・相似)で埋める。MID2 は最後に付くが結論が無い。
- **k1_0 opus_r3**(T 368・500 字・question・ANALYTIC・PB2 EQD・SYMM COLL)
  > 3) Points O1, O2, O3 are collinear in that order (O3 is the midpoint of segment O1O2). 4) The inner tangent l1 is parallel to the line through O1 and O2 (a standard result for two disjoint circles). 5) Thus the direction of l1 is the same as O1→O2. 6) From 2) and 5), the vector O1→Th is orthogonal to O1→O2. Hence ∠O1TcO2 = 90°. 7) By symmetry (O1O2 is the perpendicular bisector of TcTh), the distances O1Tc and O2Th are equal, and O3 lies on that perpendicular bisector. 8) Therefore O3Tc = O3Th.

  L3: 「l1 ∥ O1O2(a standard result)」偽・「O1O2 は TcTh の垂直二等分線」偽(olm113 の対称性の前提)。唯一の question。
- **k1_0 opus_r9**(T 110・299 字・hypothesis・OTHER・PB2 EQD・SYMM)
  > 2) The midpoint O3 of O1O2 is equidistant from O1 and O2. 3) By symmetry of the inner‐common‐tangent setup, the distances from O3 to Tc and from O3 to Th are equal. 4) Hence O3Tc = O3Th, making O3 lie on the perpendicular bisector of TcTh and forming an isosceles triangle Tc–O3–Th with apex at O3.

  L3: olm113 の「対称性」そのまま。設定(半径 ⊥ 接線・足)を与えても使わない。
- **k1_1 opus_r1**(T 167・312 字・none・OTHER・PB2 EQD)
  > 3) By the midpoint theorem (or by subtracting the two right‐angle relations), the line through O2 and O1 is parallel to TcTh. 4) A line parallel to TcTh intersects its perpendicular bisector in its midpoint. 5) O3 lies on O1O2, so by 3–4, O3 lies on the perpendicular bisector of TcTh. 6) Therefore O3Tc = O3Th.

  L3: 「O1O2 ∥ TcTh」偽。4 も偽。
- **k1_1 opus_r5**(T 89・177 字・hypothesis・OTHER・EQD・HOMO)
  > 4. Because O3 is the midpoint of O1O2, the line O3TcTh is the image of l1 under a homothety of factor 2 centered at O3. 5. Hence TcTh ⟂ O3TcTh. 6. Therefore O3Tc = O3Th, Q.E.D.

  L3: 意味を成さない(「O3TcTh」)。

### k = 2・満たした 5 本(19 本中)

- **k2_0 fable_r0**(T 71・206 字・PB2 EQD)
  > Step 5 (kernel of perpendicular projection): Any point on the perpendicular bisector of TcTh is equidistant from Tc and Th (namely M). Since O3 projects to M via the perpendicular, dist(O3,Tc)=dist(O3,Th).
- **k2_0 fable_r4**(T 126・124 字・MID2 PB2 USE_PROJ)
  > 6. Hence M = midpoint(Tc, Th), and the line O3M is perpendicular to TcTh, so O3 lies on the perpendicular bisector of TcTh.
- **k2_0 fable_r7**(T 136・170 字・MID2 PB2 EQD USE_PROJ)
  > Step 5 (perpendicular bisector): from M = midpoint(TcTh) and O3M ⟂ TcTh (by projection) it follows that O3 lies on the perpendicular bisector of TcTh, hence O3Tc = O3Th.
- **k2_0 fable_r8**(T 76・217 字・PB2 EQD)
  > 5. Therefore O3M ⊥ ThTc (because the projection of the midpoint of two points onto a line is perpendicular to the segment joining their images). 6. Hence O3 lies on the perpendicular bisector of ThTc, so O3Tc = O3Th.
- **k2_0 fable_r9**(T 125・147 字・PB2 EQD)
  > 5. Then O3M = π(O3) − M = 0, so O3 lies on the line through M perpendicular to l1, which is the perpendicular bisector of TcTh. Hence O3Tc = O3Th.

  L3(5 本): fable_r4・r7 は正しい閉じ方。r0・r8 は理由が崩れている(「射影は像を結ぶ線分に垂直」)。r9 の「O3M = 0」は退化の主張(偽)。

### k = 2・満たさなかった 5 本(21 本中・4 本おき)

- **k2_0 fable_r1**(T 73・165 字・MID2 EQD USE_PROJ)
  > 7. From 6, O3 M ⊥ Tc Th and M = midpoint(Tc, Th), which is equivalent to O3 being equidistant from Tc and Th, and to triangle Tc Th O3 being isosceles with apex O3.

  L3: 垂直二等分線の名を言わずに「等距離と同値」で閉じる = 内容は正しい閉じ方。PB2 ∨ CONG2 の語が無く Q2 は偽(計器の狭さ・§7)。
- **k2_0 fable_r6**(T 16・0 字・空の続き)
  > (空・JSON を即座に閉じた)
- **k2_0 opus_r7**(T 35・48 字・MID2)
  > Thus M is the midpoint of TcTh, and O3M ⟂ TcTh.

  L3: 与えた段の言い直しだけ。
- **k2_1 fable_r5**(T 40・63 字・MID2 EQD)
  > Step 5 (conclusion): O3Tc = O3Th because M = midpoint(Tc, Th).

  L3: 結論を言うが「O3M ⊥」を言わない(中点だけでは等距離にならない)。
- **k2_1 opus_r2**(T 90・75 字・MID2)
  > So M = (Tc + Th)/2. 5. Therefore O3M ⊥ TcTh and M is the midpoint of TcTh.

  L3: 言い直し。

## §5. 並べる(同じ計器・L1)

| 札 | model | 与えた物 | 読む欄 | 射影の段 / 結論 |
|---|---|---|---|---|
| [olm113](../2026-11-02/RESULT_olm113_moy2_projection_status_and_backing_20261102.md) | OLMo-3 32B base | M2A の文・書き出しなし | apex 16 / 60 の証明の欄 | 射影 **0 / 16**・前提は対称性 8 / 12 |
| **olm116 k = 1** | 同 | M2B + 半径 ⊥ 接線と足 / 平行の設定まで | 続き | MID2 ∧ (PB2 ∨ EQD) **21 / 40**・USE_PROJ 18 / 40・対称性 5 / 40 |
| **olm116 k = 2** | 同 | M2B + 足 = 中点の段まで | 続き | PB2 ∨ CONG2 **19 / 40**・EQD 32 / 40 |
| [prf5](../2026-11-02/RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md) | Opus 5.5 / Fable 5.1 xhigh | M2B・書き出しなし | apex 20 / 20 の証明の欄 | 射影 19 + 台形 1 |

- moy-1(olm114 / 115)との対: 段を与えた時の「語の続き」は moy-1 0.65・moy-2 0.525、「事実を使った」は moy-1 13 / 40(USE_PERP)・moy-2 18 / 40(USE_PROJ)。目で読んだ正しい推論は moy-1 で 10 本中 2〜3・moy-2 で 10 本中 4〜5(fable_r6・r7・opus_r7・r4・r5 の一部)。

## §6. 読み(L3・主 session)

1. **予想は二枚続けて同じ向きに外れた**(olm114 の Q1 0.25 → 0.65・この札の Q1 0.20 → 0.525)。主 session は「OLMo は段を与えても次の段を書けない」と見たが、設定を与えれば次の段の**語**は半分以上の行で出る。一方 k = 2(残りが短い)は、名を言わずに結論を言い直して閉じる行が多く(EQD 32 / 40・PB2 19 / 40)、予想の 0.55 より低い。計器(PB2 ∨ CONG2)が「正しい閉じ方」の一部(fable_r1 k2_0 の「等距離と同値」)を落とすことも効いている(§7)。
2. **語と事実の差は moy-1 と同じ形**: Q1 を満たした 10 本のうち、射影の推論(affine / 中点を保つ / 足の中点 = 中点の足)を正しく書いたのは fable_r6・fable_r7・opus_r7 と fable_r5・r4(言い方は崩れ)。残りは数値の確かめ(fable_r0)・**退化の主張 M = O3**(fable_r2・fable_r8 = olm117 の図でだけ真の文)・循環(opus_r2)・正誤の混在(fable_r3)。
3. **family の差は文の型**: Fable の `Step n (題):` の型では Q1 15 / 20、Opus の `n)` の型では 6 / 20 で、Opus の文の続きは対称性(5)・共線(4)・相似の中心(1)へ流れる = olm113 の前提の語が、設定を与えられても戻ってくる。olm115(moy-1)で見えなかった family 差が moy-2 では出た。文の型と知識は分けられない(PREREG §5)。
4. **退化の主張が続きに現れる**(fable_r2「TcTh passes through O3」・fable_r8「O3 is the midpoint of ThTc」・fable_r9 k2「O3M = 0」): 半径の違う図で、半径の等しい図の事実を言う。olm113 の「対称性」の前提と同じ出所に見える。三枚目(olm117 = 半径の等しい図)で、この主張が増えるかを見る。
5. **(B)** は olm114 と同じ形: 次の段の語が切れ目の後で上がり(k1 の後に中点 0.52 → 0.68・k2 の後に二等分線 0.53 → 0.68)、commit 方向の係数は証明の進みと共に単調に上がる(−7.6 → −5.7 → −3.6)。語の集合ごとの統制が無いので記述。ATTR(共線・対称)の語は frontier の証明に無く先読みは読めない。

## §7. 言えない

- 書き出しは frontier の文。続きが道を完成しても「OLMo が導いた」ではなく「与えられた段の続きを書けた」まで。apex は与えている。
- 計器の両極: Q1 の MID2 は M の定義(M = (Tc+Th)/2)でも付く(fable_r0・数値)・退化の主張(M = O3)でも付く(fable_r2・r8)。Q2 の PB2 ∨ CONG2 は「等距離と同値」の正しい閉じ方(fable_r1 k2_0)を落とす。EQD は conjecture の言い直しでも付く(32 / 40)。判定は凍結の述語の値のまま。
- family の差は文の型の差と混ざる。段の中身・長さは frontier の文ごとに違う(段 5〜9・P_k1 204〜461 字・P_k2 463〜824 字)。
- k = 0 の腕が無いので「同じ文で OLMo だけ」の値はこの札に無い。
- 両方の判定が境から 0.025。rep 2・frontier 20 本・温度 0.7・base model。
- (B) は語の集合ごとの陽性統制が無い。

## §8. 次

- 三枚目 olm117(半径の等しい対照)= 凍結 → 本走(約 2 時間)→ RESULT。§6-4 の退化の主張の出所を、等しい図で見る。
- 述語の v3(「等距離と同値」の閉じ方・M の定義と射影の推論の区別)は、先生の言葉で。
