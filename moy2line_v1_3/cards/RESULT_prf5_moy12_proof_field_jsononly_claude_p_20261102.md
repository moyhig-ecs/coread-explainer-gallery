HEAD(R1) = 259a5742(執筆時の HEAD・pull 済み・origin より 6 commit 先)

# RESULT(札 `prf5`・2026-11-02): 「考えを平文で先に書け」の一行を外し、裏付けを JSON の欄で求めると、Opus 5.5 / Fable 5.1 xhigh は 40 / 40 拒否されずに答えた(Q0 ✓)— moy-1 の apex 20 / 20 が二等分線 → 直角 → Thales の逆の鎖を座標なしで書き(Q1 ✓ × 2)、moy-2 の apex 20 / 20 の裏付けは射影(19)か台形の中線(1)・申告は 40 / 40 が hypothesis

- 札 = [PREREG](PREREG_prf5_moy12_proof_field_jsononly_claude_p_20261102.md)(凍結 5f519216・G10 台帳 59b0943d)。runner `ConstructGap/exp/prf5_moy12_proof_field_jsononly_claude_p_20261102.py`・共通の部品 `hq_moy12_status_proof_common_20261102.py`(cb12da8d のまま)。
- 出力 = `ConstructGap/exp/results_prf5_20261102.jsonl`(md5 `995650e5…`・40 行・試行 40 = 再試行なし)・`ConstructGap/exp/prf5/read.json`・stream 40 本 = `ConstructGap/exp/prf5/streams/`・log `fire_stage1.log` / `fire_stage2.log` / `read_run.log`。
- 発火: 段 1(Fable 2 本・並列 1)13:4x → 拒否 0 → 段 2(38 本・並列 2)→ 13:52:15 終了・`--read` 13:52:15。費用 $6.67(API 換算: Fable $5.02・Opus $1.65)。
- 発注(逐語・先生): 「上流と疑われる思考を取らずに証明の過程を結論として書かせられますか？」→「まず揃えずに通し、様子を見て揃える」「13:26を待って進みましょう。」

## §0. 開示

- PREREG §0 のとおり、prf4 の値(Opus × moy-1 = 鎖 8 / 8 ほか)と olm112 の最初の 20 行の集計を見てから予想を付けた。
- 段 1 の fire の log は status と label も印字する作り(PREREG は「ok と拒否だけ見る」)。主 session は 2 行の `status=hypothesis B-bind chain=True` / `apex PROJ` を目にした。段 2 の発火はこれに依らず PREREG の規則(拒否 0 → 段 2)で決めた。

## §1. 関門

| 関門 | 値 | 判定 |
|---|---|---|
| I(隔離) | init の tools `[]` = 40 / 40・道具の呼び出し 0 | ✓ |
| P(policy) | 拒否 0 / 40(category なし・`api_error_code` なし・`safety_stops` 0) | ✓ |
| K(単位ごと ok ≥ 8) | 4 単位とも 10 / 10 | ✓ |
| 較正 | 61 / 61(runner の guard) | ✓ |

## §2. 判定(凍結の述語の値だけで)

| Q | 値 | 判定 |
|---|---|---|
| **Q0(主)** 段 2 の拒否 | **0 / 38**(段 1 を含め 0 / 40) | **✓**(≤ 2) |
| **Q1 Opus** moy-1・B-bind の中の CHAIN | B-bind 10 / 10・**CHAIN 10 / 10**(BIS 10・ADJ 9・RA 10・THC 10・COORD 0) | **✓**(≥ 0.70) |
| **Q1 Fable** 同上 | B-bind 10 / 10・**CHAIN 10 / 10**(BIS 10・ADJ 10・RA 10・THC 10・COORD 0) | **✓** |
| Q2 status | 40 / 40 が hypothesis(question 0・none 0) | 記述 |
| Q3 moy-2 の裏付けの道(apex 20 / 20) | Opus: PROJ 9・TRAP 1 / Fable: PROJ 10。語の数(10 本中): Opus PERPT 9・PB 10・MIDTT 10・CONG 7・COORD 2 / Fable PERPT 8・TRAP 6・PB 10・MIDTT 9・CONG 3・COORD 5 | 記述 |

- 予想との照合: Q0 ✓(p 0.70)・Q1 Opus ✓(p 0.80)・Q1 Fable ✓(p 0.55)・Q2 hypothesis 多数(p 0.8)・Q3 PROJ 多数(p 0.8)。全部予想の側。
- 長さと時間: 証明の欄の中央値 = moy-1 Opus 1,791 字・Fable 1,858 字 / moy-2 Opus 1,050 字・Fable 1,004 字。壁時計の中央値 = Opus 22 / 18 s・Fable 33 / 45 s。

## §3. 記述(L3・主 session・採否は先生)

- **一行の差で拒否が 22 / 40 → 0 / 40**。prf4 と prf5 の文の差は、その一行と追記の文だけ(runner の自己検査で assert)。追記の中身(status・座標を使わない幾何の証明)は同じなので、引き金は「考えを平文で先に書け」の側と読む(対照は 1 つ・§5)。
- **moy-1 の鎖は 20 / 20 で、手数も揃っている**: (1) 接線までの距離 = 半径 → (2) 二本の接線の角の二等分線の上に中心 → (3) 外接線は同じ側・内接線は反対側 → (4) 隣り合う角 → (5) 二等分線は直交 → ∠O1XO2 = 90° → (6) Thales の逆。Opus r0 は He・Hi が除かれる理由(O1・O2 が同じ二等分線 = 線 O1O2 の上)まで書いた。ADJ を欠いた Opus r1 も、二つの二等分線が直交する事実を (2) で先に置いて、同じ側 / 反対側の論法で「違う二等分線」を示している(述語が「adjacent / supplementary」の語を拾わなかっただけ)。
- **座標は一度も使っていない**(COORD 0 / 20)。olm112 の最初の 20 行(集計だけ・走行中)では bind 8 本の中に鎖が 0 で、HANDOFF 11-02 §3 の事後の数え(作図で直角を導いた行 0 / 194)とも向きが合う。frontier と OLMo の差は olm112 / olm113 の RESULT で並べる(Q4・経路と文が違う・同じ計器)。
- **moy-2 は射影が既定の道**: 「半径 ⊥ 接線 → Tc・Th は O2・O1 の足 → 射影は affine で中点を保つ → O3 の足は TcTh の中点 → 垂直二等分線」。Opus r8 だけ単位法線で書いた台形の中線(TRAP)。Fable の 5 本は証明の中に数値の確かめ(≈ 0・中点の座標)を添えている(道は縛っていないので記録だけ)。
- **status は 40 / 40 が hypothesis**。正しい答えしか無い(apex 40 / 40)ので、申告が正しさを追うかはこの札では分からない(分かれるのは OLMo の側 = olm112 / olm113 の Q2 / Q1)。
- prf4 の読めた単位(Opus × moy-1・文が一行違う)= 鎖 8 / 8 → prf5 で 10 / 10。一行を外しても証明の中身は変わらない。

## §4. 逐語(証明の欄)

### moy-1(CHAIN の行から各 model 2 本・CHAIN でない B-bind は 0 本)

**Opus r0**(status hypothesis):
> Let X be any of X1..X4. Then X = t ∩ s, where t is an external common tangent and s is an internal common tangent. (1) [Tangent line is at distance r from the center] K1 is tangent to t and s, so d(O1,t) = d(O1,s) = r1. Likewise d(O2,t) = d(O2,s) = r2. (2) [The locus of points equidistant from two intersecting lines is the pair of angle bisectors at their intersection] O1 lies on an angle bisector of (t,s) at X, and so does O2. (…) (3) [Definition of external and internal tangent] t is external, so K1 and K2, and hence O1 and O2, lie on the same side of t. s is internal, so O1 and O2 lie on opposite sides of s. (4) [The four regions cut out by two crossing lines: points on the same side of one line and opposite sides of the other lie in adjacent regions] O1 and O2 lie in adjacent angular regions at X, with angles α and 180° − α. (5) [Bisectors of supplementary adjacent angles are perpendicular: α/2 + (180° − α)/2 = 90°] The bisector through O1 is perpendicular to the bisector through O2, so XO1 ⊥ XO2. (…) Hence ∠O1XO2 = 90°. (6) [Converse of Thales' theorem] Every point P with ∠O1PO2 = 90° lies on the circle with diameter O1O2. (…) The same-type points He and Hi are excluded: there O1 and O2 lie on the same bisector, the line O1O2 through the homothety centers, so no right angle arises.

**Opus r3**(status hypothesis):
> (3) The points equidistant from two crossing lines e and i are exactly the two angle bisectors b and b' of e and i at X, and b ⊥ b'. So O1 lies on b or b'. [fact: angle-bisector locus; adjacent bisectors are perpendicular because the half-angles add up to 180°/2 = 90°] (4) Likewise, by (2) applied to K2, O2 lies on b or b'. (5) O1 and O2 are not on the same bisector. (…) If O1 and O2 were on the same ray, they would be on the same side of i. That contradicts i being an internal tangent, which separates O1 from O2. If they were on opposite rays of the same bisector, they would be on opposite sides of e. That contradicts e being an external tangent (…) (6) From (3) to (5), XO1 and XO2 lie along the perpendicular lines b and b', so ∠O1XO2 = 90°. (7) By the converse of Thales' theorem, X lies on the circle with diameter O1O2 (…) ∎

**Fable r0**(status hypothesis):
> (1) e and i are both tangent to K1, so O1 is at distance r1 from both lines e and i [tangent line is at distance equal to the radius from the center]. (2) A point equidistant from two intersecting lines lies on one of their two angle bisectors, so O1 lies on a bisector b1 of the angle pair formed by e and i at X [locus of points equidistant from two lines]. (3) Likewise (…) O2 lies on a bisector b2 (…). (4) e is an external tangent, so K1 and K2 (hence O1, O2) lie on the same side of e [definition of external common tangent]; i is an internal tangent, so O1 and O2 lie on opposite sides of i [definition of internal common tangent]. Therefore O1 and O2 lie in two adjacent (supplementary) angular sectors determined by e and i (…) (5) (…) b1 ≠ b2 (…) (6) The two angle bisectors of a pair of intersecting lines are perpendicular [the bisectors of supplementary adjacent angles are perpendicular]. Hence XO1 ⟂ XO2, i.e. ∠O1 X O2 = 90°. (7) By the converse of Thales' theorem (inscribed right angle), X lies on the circle with diameter O1O2 (…) its center M and diameter O1O2 are determined solely by O1 and O2, identifying the circle uniquely.

**Fable r6**(status hypothesis):
> Step 1 (equal tangents / angle-bisector property of a circle center): since e and i are both tangent to K1, the center O1 is equidistant (distance r1) from the lines e and i, so O1 lies on one of the two angle bisectors of the pair of lines e, i at X. (…) Step 5 (which bisector): the two lines e, i divide the plane into four angular sectors; by Steps 3–4, O1 and O2 lie in sectors that share the side e but are separated by i, i.e. in two adjacent sectors, so the bisectors from Steps 1–2 are the bisectors of two adjacent (supplementary) angles. Step 6 (perpendicular bisectors): the bisectors of two adjacent supplementary angles are perpendicular (each makes half of the two angles, and the halves sum to 90°), so the line XO1 is perpendicular to the line XO2, i.e. ∠O1XO2 = 90°. Step 7 (Thales / converse of the inscribed right angle theorem): a point X with ∠O1XO2 = 90° lies on the circle with diameter O1O2 (…) (Non-degeneracy: the circles are disjoint with unequal radii, so all four common tangents exist (…) and X ≠ O1, O2 since X lies outside both circles.)

**ADJ の語を欠いた 1 本(Opus r1・CHAIN は満たす)**:
> (2) [Locus of points equidistant from two intersecting lines] The points equidistant from te and ti form the two angle bisectors b and b' at Xi, and b ⊥ b'. By (1), O1 lies on b or b', and so does O2. (3) [Definition of external and internal tangent] te does not separate O1 and O2, while ti does. (…) (4) (…) Two points on the same bisector are either in the same angle, so on the same side of both lines, or in vertical angles, so on opposite sides of both lines. Neither case matches (3). So O1 and O2 lie on different bisectors. (5) [From (2) and (4)] XiO1 ⊥ XiO2, so ∠O1XiO2 = 90°. (6) [Converse of Thales' theorem] (…)

### moy-2(道の札ごと)

**PROJ・Opus r0**:
> 1) Tc lies on c and l1 is tangent to c at Tc, so O2Tc ⊥ l1 (a radius is perpendicular to the tangent at its point of contact). 2) Likewise (…) O1Th ⊥ l1. 3) By (1) and (2), Tc is the orthogonal projection of O2 onto l1 and Th is the orthogonal projection of O1 onto l1. 4) Orthogonal projection onto a line is an affine map, and affine maps preserve midpoints. O3 is the midpoint of O1O2, so its projection onto l1 is the midpoint M of TcTh. 5) Therefore O3M ⊥ l1 (…) this puts O3 on the perpendicular bisector of TcTh. 6) A point on the perpendicular bisector of a segment is equidistant from its endpoints, so O3Tc = O3Th. (…) Note: this holds for the inner tangent even though O1 and O2 lie on opposite sides of l1; the projection argument does not depend on which side they are on.

**PROJ・Fable r0**(数値の確かめ付き = COORD):
> Step 3 (two lines perpendicular to the same line are parallel): O1Th ∥ O2Tc, and Th, Tc are the feet of the perpendiculars from O1, O2 to l1 (numerically: O1Th·(Th−Tc) ≈ 0 and O2Tc·(Th−Tc) ≈ 0). Step 4 (midline of a trapezoid / projection is affine): O3 is the midpoint of O1O2, so the foot M of the perpendicular from O3 to l1 is the midpoint of the feet Th and Tc (…) Step 5 (perpendicular bisector / Pythagoras): O3Tc^2 = O3M^2 + MTc^2 = O3M^2 + MTh^2 = O3Th^2, hence O3Tc = O3Th. Step 6 (non-degeneracy remark): O1 and O2 lie on opposite sides of the inner tangent l1, so dist(O3,l1) = |r_c − r_h1|/2, which is nonzero for unequal radii; therefore O3 lies strictly off l1 and is equidistant from Tc and Th without being their midpoint.

**TRAP・Opus r8**(唯一):
> Step 2 (two lines perpendicular to the same line are parallel): O2Tc ∥ O1Th, and both are normal to TcTh. Let n be a unit normal to TcTh. Then Tc − O2 = a·n and Th − O1 = b·n for some reals a and b. For an inner tangent, a and b have opposite signs. Step 3 (definition of midpoints): let M be the midpoint of TcTh. O3 is the midpoint of O1O2. Then M − O3 = ½[(Tc + Th) − (O2 + O1)] = ½[(Tc − O2) + (Th − O1)] = ½(a + b)·n. This is the midline of the (possibly crossed) trapezoid O2 Tc Th O1. Step 4: M − O3 is a multiple of n, so O3M ⟂ TcTh. If a + b = 0, then O3 = M (…) Step 5 (…) O3 lies on the perpendicular bisector of TcTh. (…) ∎

## §5. 言えない

- 「一行が引き金」は prf4 との対照 1 つ。追記の文の言い回し(prf4「Then answer two more questions」→ prf5「Also include two more fields」)も同時に変えたので、厳密には「一行 + 言い回し」の差。語を一つずつ替える札は立てていない。
- `claude -p` の答えは Claude Code の system prompt の下の物。API の札と一対一に並べない。effort xhigh だけ。
- frontier の文は OLMo(F5a-2)と一行違う。測る対象は `proof` の欄。揃えるなら OLMo に JSON だけの腕を足す(先生「様子を見て揃える」)。
- CHAIN は語の鎖。証明の正しさは検証していない(§4 の逐語は主 session の読みでは正しい道筋だが、一人の読み)。status は申告で、この札では正しい答えしか無いので申告が正しさを追うかは測れない。
- n = 10 × 4 単位。model の間の差(時間・長さ・道の語)は検定しない。

## §6. 次(採否は先生)

- olm112(走行中・16:30 ごろ)/ olm113(その後)の RESULT で、同じ計器の値を prf5 と並べる(Q4)。
- 「揃える」腕 = OLMo に prf5 と同じ JSON だけの文(olm114 候補・2 時間)。結果が面白ければ(先生の言葉)。
- prf4 の 22 本の拒否は費用 $1.5 の記録として残す([RESULT prf4](RESULT_prf4_moy12_status_proof_claude_p_20261102.md))。
