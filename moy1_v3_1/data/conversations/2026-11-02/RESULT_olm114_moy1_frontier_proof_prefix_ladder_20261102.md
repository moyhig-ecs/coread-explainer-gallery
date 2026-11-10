HEAD(R1) = f27d2679(執筆時の HEAD・pull 済み = origin と一致・遅れ 0)

# RESULT(札 `olm114`・2026-11-03): frontier(Opus 5.5 / Fable 5.1・prf5)の証明の欄を OLMo-3 32B base に段で与えると、続きは書く — k = 1(O1・O2 を二等分線の上に置いた段まで)で続きが直角 ∧ Thales の逆を満たす 26 / 40 = 0.65(Q1 **続ける**・予想は 0.25 で最も低く置いた側)・k = 2(直角の段まで)で Thales の逆 23 / 40 = 0.575(Q2 続ける・予想 0.55)・k = 0(prf5 の M1B の文そのまま)は答えの欄が apex 5 / 40 で関門 ✗ → Q3 読まない(上限で切れた 18・flail 21 = JSON だけを求める文で base model は JSON に着かない)— ただし「直角」を二等分線の直交から導いた続きは 12 / 40(主 session の正規表現)で、残りは直角を**言う**が前提は共線・角の和・方べき — (B) forward は統制を通り、段の語(bis・converse・adjacent)の先読みは 3〜6 token 前まで・誤アトラクタの語(He・Hi・radical)は 1 token 前だけ・commit 方向の係数は k1 → k2 → 終わりで −7.6 → −5.4 → −3.7(記述)

- 札 = [PREREG](PREREG_olm114_moy1_frontier_proof_prefix_ladder_20261102.md)(凍結 c82642a5・HEAD(R1) fe3a016c・G10 の台帳 済)・runner `ConstructGap/exp/olm114_moy1_frontier_proof_prefix_ladder_20261102.py`(md5 `4d9a0fe9…`)・共通の部品 `hq_moy12_status_proof_common_20261102.py`(`426e2089…`・olm112 / 113 / prf4 / prf5 と同じ)・frontier の出力 = `results_prf5_20261102.jsonl`(`995650e5…`・guard で一致)。
- 出力 = `ConstructGap/exp/olm114/gen.json`(md5 `3d70d869…`)・`read.json`(`b55baf70…`)・`series/*.npz`(20 本・1.2 MB)・`gen_run.log`・`fire_run.log`・`read_run.log`・`chain_olm114.log`。
- 走り = zebrashark・11-03 10:54:28 `--gen` → 11:49:19(3,291 s・k1 229 + 199 s・k2 206 + 140 s・k0 1,247 + 1,264 s)→ `--fire` → 11:51:34(135 s)→ `--read` → 11:51:49。Traceback 0。gen の provenance = commit cc2df52d・dirty false。read の provenance = commit 78369149・dirty false。script / common / prereg / prompt / prf5 の md5 は gen と read で一致(prompt `15dec317…`・prereg `d28170ec…`)。版 = mlx 0.32.0・mlx-lm 0.31.3・transformers 5.14.1。
- 較正 = hq 61 / 61 + この札の 13 / 13(runner の guard)。書き出しは frontier の `conjecture` と `proof` の二欄だけ(`reason` は渡していない・PREREG §0)。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G1(k = 1) | 生成が空でない行 ≥ 24 | 40(閉じた 40・空の続き 0) | ✓ |
| G1(k = 2) | 同上 | 40(閉じた 40・空の続き 0) | ✓ |
| G2(k = 0) | label の無い行 ≤ 4 **かつ** 答えの欄 B-bind ≥ 8 | label なし 0 ✓・**B-bind 5** ✗ | **✗ → Q3 を読まない** |
| (B) C1 | J-lens の cos(J h48, h63) > cos(h48, h63) が行の 95 % 以上 | 20 / 20(中央値 0.701 対 0.521) | ✓ |
| (B) C3 | 方向のノルム = olm4 の記録 | 19.647 = 19.647 | ✓ |
| (B) round_trip | — | 通る | ✓ |

## §2. 判定

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** | k = 1 の続きが RA ∧ THC: 26 / 40 = **0.65** | **続ける**(≥ 0.50) | 続ける **0.25**・続けない 0.35・間 0.40 → **外れ(最も低く置いた側)** |
| Q2 | k = 2 の続きが THC: 23 / 40 = **0.575** | **続ける**(≥ 0.50) | 続ける 0.55 ✓ |
| Q3 | k = 0 の答えの欄 B-bind 5 / 40・その証明の欄の CHAIN 0 / 5 | **読まない**(G2 ✗)・記述のみ | 変わらない 0.65(判定なし) |

- Q1 の予想は、olm112(鎖 0 / 37・角の二等分線 0 / 37)を見て「二等分線の段を与えても次に進めない」側に置いた。外れた。ただし §4・§6 の通り、述語は「直角と Thales の逆を**言う**」を数えており、「二等分線の直交から導く」は別(12 / 40)。
- Q2 は予想の通り。k = 2 の続きは短く(中央値 161 字・T 65.5 token)、Thales の名か「直角 → 直径の円」の一文で閉じる。

## §3. Q4(記述・read.json の逐語)

### 続きの述語(続きだけに当てた)

| 腕 | n | BIS | ADJ | RA | THC | CHAIN | COORD | ALT radical / homothety / power | RA ∧ THC | thales_c | 閉じた | status | T 中央値 | 続きの字数 中央値 | 上限 |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|
| k = 1 | 40 | 33 | 7 | 29 | 30 | 21 | 0 | 2 / 2 / 3 | **26** | 7 | 40 | hyp 37・other 2・question 1 | 146 | 422.5 | 0 |
| k = 1 Opus の文 | 20 | 14 | 1 | 14 | 15 | 7 | 0 | 0 / 1 / 1 | 12 | 3 | 20 | hyp 19・question 1 | 132.5 | 362 | 0 |
| k = 1 Fable の文 | 20 | 19 | 6 | 15 | 15 | 14 | 0 | 2 / 1 / 2 | 14 | 4 | 20 | hyp 18・other 2 | 183 | 488.5 | 0 |
| k = 2 | 40 | 1 | 0 | 17 | 23 | 0 | 1 | 0 / 0 / 0 | 16 | 15 | 40 | hyp 34・none 2・other 4 | 65.5 | 161 | 0 |
| k = 2 Opus の文 | 20 | 1 | 0 | 4 | **7** | 0 | 0 | 0 / 0 / 0 | 3 | 5 | 20 | hyp 17・other 2・none 1 | 52 | 117 | 0 |
| k = 2 Fable の文 | 20 | 0 | 0 | 13 | **16** | 0 | 1 | 0 / 0 / 0 | 13 | 10 | 20 | hyp 17・none 1・other 2 | 67 | 168 | 0 |

- k = 1 の続きに BIS が 33 / 40(与えた段の後でも二等分線を言い直す)。CHAIN 21 は「続きの中だけで BIS ∧ RA ∧ THC」。
- given_perp(与えた段が二等分線の直交を先に言っている 7 本 = 14 行)別: k = 1 の RA ∧ THC = given_perp 12 / 14・それ以外 14 / 26 / k = 2 の THC = given_perp 6 / 14・それ以外 17 / 26。
- JSON の後の文字(tail)が 0 でない行 = k = 1 で 1・k = 2 で 0。

### k = 0(揃える腕・M1B の文そのまま・凍結の分類器)

| 欄の印 | n | 上限 4,096 で切れた | 答えが先 | status |
|---|---:|---:|---:|---|
| B-flail | 21 | **18** | 1 | — |
| B-attractor | 11 | 0 | 6 | hyp 9・other 1・none 1 |
| B-bind | **5** | 0 | 0 | hyp 4・none 1 |
| B-stuck-L1 | 3 | 0 | 1 | — |

- apex の率 5 / 40 = 0.125(olm112 の M1A = 0.37・400 行の比べる元 0.485)。T の中央値 2,586。status none 22 / 40。
- B-bind 5 本の証明の欄: CHAIN 0・BIS 0・RA 1・THC 2。中身は方べき(j12)・「中点から等距離」の言い換え(j2・j10)・内積(j13)・相似(j9・「平行な半径と共通の角で相似 → 直角」)。
- flail 21 のうち 18 は「Okay, let's try to figure out this geometry problem…」と考えを書き続けて 4,096 token で切れ、JSON に着かない。**JSON だけを求める文(M1B)は base model に効かない** = この腕は「prf5 と同じ文で OLMo を読む」役を果たせない。

### (B) forward(記述・統制は §1)

- **先読み**(証明の領域で語の集合が最初に出る位置 w の k token 前の u(w − k) が行内の top 5 に入る行の割合・J-lens・層 48・null の p95 ≈ 0.2):

| 集合(n = 最初の出現がある行) | k = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BIS ` bis`(20) | 0.90 | 0.75 | 0.85 | 0.60 | 0.40 | 0.40 | 0.25 | 0.05 |
| RA ` perpendicular`(18) | 0.94 | 0.50 | 0.17 | 0.11 | 0.22 | 0.22 | 0.39 | 0.11 |
| THC ` converse`(9) | 1.00 | 0.78 | 1.00 | 0.56 | 0.44 | 0.67 | 0.00 | 0.33 |
| ATTR ` He`・` Hi`・` radical`(13) | 0.54 | 0.15 | 0 | 0 | 0 | 0 | 0 | 0 |
| ADJ ` adjacent`・` supplementary`(18) | 0.94 | 0.72 | 0.50 | 0.06 | 0.28 | 0.33 | 0.28 | 0.17 |

  logit lens も同じ形(BIS 0.90 / 0.80 / 0.85 / 0.45 / 0.40 / 0.45 / 0.10 / 0.05・ATTR 0.46 / 0.15 / 0 …)。
- **切れ目の前後 32 token の窓の中央値**(20 行):

| 切れ目 | proj32(commit 方向の係数)前 → 後 | u(BIS) | u(RA) | u(THC) | u(ATTR) | u(ADJ) |
|---|---|---|---|---|---|---|
| k1(二等分線の段の終わり) | −7.65 → −6.79 | 0.66 → 0.56 | 0.65 → 0.60 | 0.64 → 0.55 | 0.44 → 0.46 | 0.65 → 0.59 |
| k2(直角の段の終わり) | −5.41 → −4.14 | 0.58 → 0.54 | 0.62 → 0.58 | **0.50 → 0.65** | 0.40 → 0.40 | 0.52 → 0.44 |
| 証明の終わり(前だけ) | −3.66 | 0.53 | 0.56 | 0.50 | 0.48 | 0.45 |

- 最初の出現が無い行: THC(` converse`)11 / 20(frontier は Thales を名で書き converse の語を使わない物が多い)・RA 2(fable_r5・opus_r1 = 直角を ⊥ で書く)・ATTR 7・ADJ 2。

## §4. 逐語(PREREG §4 = k = 1: RA ∧ THC を満たした物を行の名の順に 10 本・満たさなかった物を 4 本おきに最大 10 本 / k = 2: 同じ型で各 5 本)

### k = 1・満たした 10 本(26 本中・行の名の順)

- **k1_0 fable_r0**(T 155・408 字・hypothesis・述語 BIS RA THC CHAIN)
  > (4) Since b1 and b2 are the two angle‐bisectors of the pair (e, i) at X, the lines O1X and O2X are perpendicular [bisectors are perpendicular]. Hence ∠O1 X O2 = 90°. (5) Conversely, if a point X satisfies ∠O1 X O2 = 90°, then X lies on the circle with diameter O1O2. (6) By symmetry the same perpendicularity holds for X2, X3, X4. (7) Therefore X1, X2, X3, X4 are concyclic on the circle with diameter O1O2.

  L3: **二等分線の直交 → 直角 → 逆 → 共円**。与えた段の続きとして正しい鎖。
- **k1_0 fable_r1**(T 92・234 字・hypothesis・BIS RA THC CHAIN)
  > Step 4 (angle sum at X): The two bisectors at X (for K1 and K2) together make up the full angle at X, so angle O1XO2 is 90 degrees. Thus XO1 and XO2 are perpendicular, so X lies on the circle with diameter O1O2. Repeat for k = 2,3,4.

  L3: 「二つの二等分線が X の全角を成す → 90°」は言い方が崩れている(全角 180° の半分、の意なら正しい)。結論は正しい。
- **k1_0 fable_r2**(T 135・348 字・other・BIS ADJ RA THC CHAIN)
  > Step 3 (angle sum): the two bisectors from O1 and O2 of the same angle between the same lines e, i meet at X, so the directed angles (X O1 O2) and (O1 O2 X) together equal 180°. Step 4 (right angle): hence ∠O1 X O2 = 90°, so X lies on the circle with diameter O1O2. Since X1,X2,X3,X4 all satisfy ∠O1 X O2 = 90°, they are concyclic on that circle.

  L3: 角の和の前提が誤り(三角形の二角の和が 180° なら残りは 0°)。直角は言うが導いていない。
- **k1_0 fable_r3**(T 157・351 字・hypothesis・BIS RA THC CHAIN)
  > Step 3 (union of bisectors = perpendicular bisector): the two bisectors at X coincide in the two-line case, so O1X ⟂ ℓe and O2X ⟂ ℓi, hence ∠O1XO2 = 90°. Step 4 (power of a point): for any X on that circle with diameter O1O2, |XO1|² = |XO2|² = (|O1O2|/2)², so X lies on the circle. Therefore all four X1, X2, X3, X4 satisfy |XOi|² = (|O1O2|/2)², QED.

  L3: 「二等分線が一致」「O1X ⟂ e」は偽。方べきの段も偽(|XO1| = |O1O2| / 2 ではない)。
- **k1_0 fable_r4**(T 237・668 字・hypothesis・BIS ADJ RA THC CHAIN)
  > Step 4 (collinearity of centers): O1, M, O2 are collinear with M = midpoint(O1O2). Step 5 (angle sum to 180°): the two angle bisectors (XO1 and XO2) together cut the angle between e and i into two equal parts, and since O1, M, O2 are collinear, the sum of the two angles between XO1 and XO2 (in the two halves of the plane) is 180°. Step 6 (right angle at X): hence angle O1 X O2 = 90°. Step 7 (cyclic quadrilateral): in any triangle O1 X O2, if angle at X is 90°, then X lies on the circle with diameter O1O2. Step 8 (all four points): this applies to each of X1, X2, X3, X4, so all four lie on the same circle: the one with diameter O1O2, center M, radius |O1O2|/2.

  L3: 「二つの角の和が 180° → 90°」は、隣り合う角(e と i の成す角とその補角)の半分ずつの和が 90° の意なら正しい。言い方は崩れている。Step 7 は Thales の逆を名なしで言う。
- **k1_0 fable_r6**(T 163・501 字・hypothesis・BIS RA THC CHAIN)
  > Step 3 (X, O1, O2 collinearity): X is the intersection of e and i, so the angle bisectors at X of e,i coincide with the angle bisector(s) of the angle between e and i. Hence O1, X, O2 are collinear. Step 4 (right angle): In the triangle O1-X-O2, the angle at X is half the angle between e and i (i.e. a straight angle minus twice the tangent angle), so the angle at X is 90°. Therefore ∠O1XO2 = 90° for every mixed intersection X. That is equivalent to saying X lies on the circle with diameter O1O2.

  L3: 「O1・X・O2 が共線」(偽)の直後に「三角形 O1XO2 の X の角は 90°」。矛盾したまま結論に着く。
- **k1_0 fable_r8**(T 345・857 字・hypothesis・BIS RA THC CHAIN)
  > Step 3 (bisectors ⟂ radii): since e and i are the tangent directions to K2, the angle between e and i at X is 2·angle(O2–X–tangent). The bisector of that angle is ⟂ the radius O2–X, so XO2 ⟂ the tangent direction e (and similarly XO1 ⟂ e). Step 4 (power of a point): for any external tangent e, the power of X w.r.t. K1 equals (XT)^2 where T = e ∩ K1, and similarly for K2. Since e and i are different lines, these two powers are equal, so X has equal power to K1 and K2. Step 5 (equal power ⇒ concyclic): two circles have a point X with the same power iff X lies on their radical axis — which is a line. But this common tangent‐intersection property in fact forces that radical axis to be the circle with diameter O1O2. Equivalently, from XO1 ⟂ e and XO2 ⟂ e, the four points X1,X2,X3,X4 all satisfy ∠O1XO2=90°, so they lie on the circle on diameter O1O2.

  L3: 方べき・根軸(「根軸が円になる」)で埋め、最後に「XO1 ⟂ e かつ XO2 ⟂ e → ∠O1XO2 = 90°」(前提も推論も偽)。olm112 の B-bind と同じ埋め方。
- **k1_0 opus_r1**(T 151・436 字・hypothesis・BIS RA THC CHAIN)
  > But O1 and O2 are not collinear with Xi (else the circles would intersect), so O1 and O2 lie on opposite bisectors. Hence b is the line O1Xi and b' is O2Xi. (3) [Right angle at intersection of bisectors] Since b ⊥ b', we get ∠O1XiO2 = 90°. (4) [All four Xi lie on the same circle] The locus of points X satisfying ∠O1XO2 = 90° is the circle with diameter O1O2. Since Xi each satisfy this right‐angle, they are concyclic on that circle.

  L3: **正しい鎖**(O1・O2 が別の二等分線の上 → b ⊥ b' → 直角 → 軌跡の円)。Opus の `(n) [題]` の型をそのまま続けている。
- **k1_0 opus_r2**(T 100・214 字・hypothesis・BIS RA THC CHAIN)
  > Hence O1O2 cuts both bisectors at X, and by (1) again it is perpendicular to them. Thus O1O2 ⟂ e and O1O2 ⟂ i at X. That shows ∠O1XO2 = 90°, so X lies on the circle with diameter O1O2. It holds for X1, X2, X3, X4.

  L3: 「O1O2 が e と i に垂直」は偽。直角は言うが導いていない。
- **k1_0 opus_r3**(T 143・367 字・hypothesis・RA THC・thales_c)
  > (5) Thus O1, O2, b, b' are concurrent at X: X = b ∩ b'. (6) Therefore ∠O1XO2 = 90°, so X lies on the circle with diameter O1O2. [fact: angle in a semicircle is right] (7) By symmetry the same holds for the other mixed point X3, and for X2, X4 by repeating the argument with the other pair of lines. (8) Hence X1, X2, X3, X4 are concyclic on that circle. [synthesis]

  L3: (5) → (6) に段が無い(「したがって 90°」)。Opus の `[fact: …]` の札の型を続けている。

### k = 1・満たさなかった 4 本(14 本中・4 本おき = 0・4・8・12 番目)

- **k1_0 fable_r5**(T 131・409 字・other・BIS ADJ THC)
  > Step 4 (sum of angles around X): the full angle between e and i around point X is 180°, and the two bisected angles at X sum to 90°. Step 5 (central angle over an arc): the locus of points from which a fixed segment (here O1O2) subtends a right angle is the circle with O1O2 as diameter. Hence X lies on that circle. Repeating for X1, X2, X3, X4 shows they are all concyclic on the circle with diameter O1O2.

  L3: 「二等分された角の和が 90°」= 直角の中身を**言っている**が、`∠O1XO2 = 90°` / `right angle` の形でないので RA が偽。計器の取りこぼし(§7)。
- **k1_0 opus_r5**(T 255・734 字・hypothesis・BIS)
  > Step 3 (if two points lie on the same bisector of two intersecting lines, then the line joining them makes equal angles to those lines): O1X and O2X lie on two bisectors, one for O1 and one for O2. Hence ∠(O1X,e) = ∠(O1X,i) and ∠(O2X,e) = ∠(O2X,i), but these are precisely the right angles from O1 to the tangent e and from O2 to the tangent i. Thus O1X ⊥ e and O2X ⊥ i. Step 4 (power of a point on a circle): since X lies on both tangents, X is the foot from O1 to e and the foot from O2 to i. Hence O1O2 is the diameter of the circle with center M = midpoint(O1O2) and radius |O1O2|/2, and X lies on that circle. Step 5 (repeat for k = 1..4): each Xk satisfies the same properties, so all four lie on the circle with diameter O1O2.

  L3: 「O1X ⊥ e」(X が O1 から e への足)は偽(足は接点)。直角を言わずに結論に着く。
- **k1_1 fable_r3**(T 203・601 字・hypothesis・BIS)
  > Step 3 (bisectors coincide): two intersecting lines have exactly two bisectors, and O1, O2 lie on the two lines ℓe, ℓi; in the general position of two disjoint circles with two external and two internal tangents, the bisector through O1 contains O2 (one checks by symmetry that the “wrong” bisector would force a degenerate configuration). Hence the bisectors coincide, so O1, X, O2 are collinear. Step 4: the same argument with X2, X3, X4 shows O1–X2–O2, O1–X3–O2, O1–X4–O2 collinear. Therefore all four X’s lie on the circle with diameter O1O2, whose center is M=(O1+O2)/2 and radius |O1O2|/2.

  L3: 「二等分線が一致 → O1・X・O2 が共線」(偽)から直接「直径 O1O2 の円の上」。
- **k1_1 opus_r4**(T 82・212 字・hypothesis・BIS THC・thales_c)
  > (3) Xk is on the line through O1 and O2. Fact: the two angle bisectors of two intersecting lines are perpendicular. Hence O1Xk ⟂ O2Xk. (4) Therefore Xk lies on the circle with diameter O1O2 (by Thales’ theorem).

  L3: 一文目は偽だが、**「二本の二等分線は直交する → O1Xk ⟂ O2Xk → Thales」は正しい鎖**。`O1Xk ⟂ O2Xk` が RA の正規表現に掛からず、満たさなかった側に入った(§7)。

### k = 2・満たした 5 本(23 本中)

- **k2_0 fable_r0**(T 81・222 字・RA THC)
  > (7) Therefore the four points X1, X2, X3, X4 all satisfy ∠O1 X_k O2 = 90°, so they all lie on the circle with diameter O1O2 [circle with diameter as the locus of points subtending a right angle at the diameter endpoints].
- **k2_0 fable_r1**(T 55・141 字・RA THC・thales_c)
  > Step 8 (circle with diameter O1O2): By the converse of Thales' theorem, any point X with ∠O1XO2 = 90° lies on the circle with diameter O1O2.
- **k2_0 fable_r2**(T 62・162 字・THC・thales_c)
  > Step 6 (Thales' theorem): therefore X lies on the circle with diameter O1O2. Since X1, X2, X3, X4 all satisfy the same construction, they all lie on that circle.
- **k2_0 fable_r3**(T 79・184 字・RA THC・thales_c)
  > Step 6 (Thales’ theorem): any X satisfying ∠O1XO2 = 90° lies on the circle with diameter O1O2, whose center M is the midpoint of O1O2. Therefore X1, X2, X3, X4 all lie on that circle.
- **k2_0 fable_r4**(T 58・154 字・THC・thales_c)
  > Step 8 (circle with diameter O1O2): by Thales' theorem, X lies on the circle with diameter O1O2. Hence all four points X1, X2, X3, X4 lie on that circle.

  L3(5 本): 全部 Fable の `Step n (題):` の型で、題に Thales を置いて一文で閉じる。正しい閉じ方(逆の名を書くのは r1 だけ)。

### k = 2・満たさなかった 5 本(17 本中・4 本おき)

- **k2_0 fable_r6**(T 80・168 字・述語なし)
  > Step 7 (conclusion): since X was arbitrary, O1O2 is perpendicular to each of O1X1, O1X2, O1X3, O1X4; therefore X1, X2, X3, X4 all lie on the circle with diameter O1O2.

  L3: 「O1O2 ⊥ O1X」は偽。
- **k2_0 opus_r5**(T 39・62 字・述語なし)
  > Thus X1, X2, X3, X4 all lie on the circle with diameter O1O2.

  L3: 結論だけ(直角の段の直後なので、閉じ方としては成り立つ)。
- **k2_1 fable_r6**(T 19・7 字・other)
  > Q.E.D.
- **k2_1 opus_r4**(T 67・182 字・述語なし)
  > (6) Fact: three points A,B,C are concyclic if and only if ∠ABC = 90° implies that A and C are endpoints of a diameter. Hence O1O2 is a diameter of the circle through X1, X2, X3, X4.

  L3: Thales の逆の中身を名なしで言う(文は崩れている)。THC が偽になった取りこぼし(§7)。
- **k2_1 opus_r9**(T 46・102 字・述語なし)
  > (6) Therefore O1 X = O2 X (right triangle hypotenuse). Hence X lies on the circle with diameter O1O2.

  L3: 「O1X = O2X」は偽。

- 満たさなかった 17 本のうち 9 本は「circle with diameter O1O2」の一文を含み(中央値 85 字)、Thales の名も逆の中身も無い。

## §5. 並べる(同じ計器・L1)

| 札 | model | 与えた物 | 読む欄 | 鎖 / 直角 + Thales |
|---|---|---|---|---|
| [olm112](RESULT_olm112_moy1_apex_status_and_geometric_proof_20261102.md) | OLMo-3 32B base | M1A の文(考えを先に + 追記)・書き出しなし | 答えの欄 apex 37 / 100 の証明の欄 | CHAIN **0 / 37**・角の二等分線 0 / 37 |
| **olm114 k = 0** | 同 | M1B の文(JSON だけ)・書き出しなし | apex **5 / 40** の証明の欄 | CHAIN 0 / 5(関門 ✗) |
| **olm114 k = 1** | 同 | M1B + frontier の証明の二等分線の段まで | 続き | RA ∧ THC **26 / 40**・二等分線の直交を使った 12 / 40(正規表現) |
| **olm114 k = 2** | 同 | M1B + 直角の段まで | 続き | THC **23 / 40** |
| [prf5](RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md) | Opus 5.5 / Fable 5.1 xhigh | M1B・書き出しなし | apex 20 / 20 の証明の欄 | CHAIN 20 / 20 |

- 二等分線の直交の数え(主 session・計器の外・`bisectors (are|…) perpendicular|b ⊥ b'|bisectors…⊥`): k = 1 の続き 40 本のうち 12(満たした 26 のうち 7・満たさなかった 14 のうち 5)。同じ続きで「O1・X・O2 が共線」の偽の前提 8・角の和 6・方べき 3・軌跡 / 半円 9・Thales の名 5。

## §6. 読み(L3・主 session)

1. **Q1 の予想は外れた**。olm112 の「角の二等分線 0 / 37」から、二等分線の段を与えても次に進めないと見たが、65 % が直角と円まで書いた。ただし §4 の 10 本で、直角を二等分線の直交から導いているのは fable_r0・opus_r1(+ 満たさなかった側の opus_r4 k1_1)で、残りは直角を**言う**。前提は共線(偽)・角の和(崩れ)・方べき(偽)・「O1O2 ⊥ e」(偽)。olm112 の「直角は言うが導かない」が、ここでは「言う所まで文脈が運ぶ」形で現れた。全 40 本では二等分線の直交を使った続きが 12 本。
2. **frontier の文の型が足場になる**。Fable の `Step n (題):` は題の欄に「Thales' theorem」「right angle」を置けば一文で段が埋まり、k = 2 の THC は Fable の文 16 / 20・Opus の文 7 / 20。Opus の `(n) [事実]` の型では短く閉じる(T 中央値 52・「Thus … lie on the circle」)。この差は文の型の差で、model の知識の差と分けられない(PREREG §5)。
3. **揃える腕は役を果たせなかった**。M1B(JSON だけ・考えを書かせない)を OLMo base に当てると、21 / 40 が「Okay, let's try…」と考えを書き続けて上限で切れ、apex は 5 / 40。prf5 と同じ文で OLMo を読む、は base model には成り立たない。olm112(M1A)が OLMo 側の比べる元のまま。olm115 の候補(JSON だけの文)はこの腕で答えが出た = 不可。
4. **k = 1 → k = 2 の段(二等分線の直交 → 直角)が細い所**。与えた段が直交を先に言っている 14 行(given_perp)では RA ∧ THC 12 / 14、言っていない 26 行では 14 / 26。直交の事実が文脈に在ると続きが運び、無いと半分。
5. **(B) は記述に留める**。frontier の文を読む間、層 48 の lens は段の語(bis・converse・adjacent)を 3〜6 token 前から top 5 に入れ、誤アトラクタの語(He・Hi・radical)は 1 token 前だけ。commit 方向の係数は k1 の窓(−7.6)→ k2(−5.4)→ 終わり(−3.7)と単調に上がる。語の集合ごとの陽性統制が無いので、「段を先読みしている」とは言わない。olm67(moy-5・cut の 33〜64 token 前から寄る)と目盛りが違う(ここは ±8 token)。
6. 先生の発注(「思考ではなく出力を順次喰わせる」)への答え: **与えられた段の続きは書ける。書けるのは語で、導きは 12 / 40**。frontier の出力は「どこへ向かうか」(apex と二等分線の設定)を運び、OLMo は型の語で埋める。

## §7. 言えない

- 書き出しは frontier の文。続きが鎖を完成しても「OLMo が導いた」ではなく「与えられた段の続きを書けた」まで(PREREG §5)。apex は与えている。
- 計器の取りこぼし(両極): RA は `O1Xk ⟂ O2Xk`(opus_r4 k1_1)と「二等分された角の和が 90°」(fable_r5)を拾わず、THC は「∠ABC = 90° なら A・C は直径の端」(opus_r4 k2_1)を拾わない。逆に、偽の前提から「∠O1XO2 = 90°」を言う行は RA を満たす。述語は語の鎖で、正しさの検証ではない。判定は凍結の述語の値のまま。
- family の差は文の型の差と混ざる。段の中身・長さも frontier の文ごとに違う(段 5〜9・P_k1 442〜873 字)。
- k = 0 の腕は関門 ✗。「M1B で OLMo は apex に着かない」は記述で、判定ではない(rep 2・40 行)。
- (B) の語の集合は先頭の sub-token 一つずつ。` perpendicular` は二等分線の段より前にも出る・` He`・` Hi` は問いの文にも出る。null は無作為位置 1,000 回で p95 ≈ 0.2。
- base model・温度 0.7・rep 2・frontier 20 本。

## §8. 次(先生の言葉で)

- 続きの「二等分線の直交を使ったか」を述語にした v2(計器の取りこぼしの修正を含む)。この札の値は凍結のまま。
- moy-2 版(射影の証明を段で与える・olm113 の対)。半径の等しい問いの対照(olm113 の「対称性」の出所)。
- 与えた段が直交を先に言う / 言わないを揃えた対照(given_perp を機械で付け外しする = frontier の文の書き換えになるので、やるなら設計から)。
