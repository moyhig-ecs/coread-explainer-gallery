HEAD(R1) = 1cbd611a(執筆時の HEAD・origin の 5 commit〔自宅の Trajectory の記事 v0・証拠表・採点のまとめ・RECORD §5a の訂正 ほか〕を merge 済み・origin より 10 commit 先・遅れ 0)

# RESULT(札 `olm117`・2026-11-03): moy-2 の半径の等しい対照 — 中心はそのままに二円の半径を 5.5738 に揃えた図(内接線が O3 を通る)へ olm113 の M2A を当てると、conjecture の MIDO3(O3 = TcTh の中点 / Tc・O3・Th の共線)は 37 / 50 = **0.74**(olm113 0.34・Δ **+0.40**・Q1 **増える**・予想 0.45 で当たり)・**apex(等距離)の conjecture は 0 / 50**(olm113 16 / 50)= Q2 は読めない(EQ の証明の欄 0 本・条件 ≥ 8)— 言い方は共線 20 + 中点 16 + l1 上 1(olm113 は共線 17 だけ)・半径が等しいことへの言及 EQR = 本文 24 / 60・証明の欄 10 / 46(olm113 は 2 / 60・0 / 41)・MIDO3 の証明の欄の「対称性」16 / 33(olm113 2 / 15)だが、対称の種類は O3 についての点対称(正)5・O1O2 についての線対称(誤)5(重なり 2)・種類なし 8 — 退化の主張は図を読んで増え、前提の半分は記憶の図のまま

- 札 = [PREREG](PREREG_olm117_moy2_equal_radii_control_20261103.md)(凍結 1095102b・HEAD(R1) 63f8a35c・G10 の台帳 済)・runner `ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py`(md5 `ab678f30…`)・凍結の部品 `hq_moy12_status_proof_common_20261102.py`(`426e2089…`・guard で一致)・比べる元 `olm113/gen.json`(`db0fde6e…`・guard で一致)。
- 出力 = `ConstructGap/exp/olm117/gen.json`(md5 `b5795850…`)・`read.json`(`76942d75…`)・`smoke.json`(`343d87fc…`・凍結の前)・`gen_run.log`・`read_run.log`・`smoke_run.log`・`chain_olm117.log`。
- 走り = zebrashark・11-03 12:45:43 `--gen` → 14:38:08(6,741 s = 1.87 時間・batch 0 3,335 s〔上限 12288 の行が 2〕・batch 1 846 s・batch 2 2,560 s・seed 20261160〜62)→ `--read` 14:38:08。Traceback 0。gen の provenance = commit 1095102b・dirty false。read の provenance = commit 108e49ba(生成中に olm116 の RESULT を commit した後の HEAD)・dirty false。prompt md5 `7e52c06a…`・差し替えを外した元の文 `56182280…`(= olm113 の M2A・guard)・prereg md5 `590ac932…`。mlx 0.32.0・mlx-lm 0.31.3・transformers 5.14.1。
- 較正 = hq 61 / 61 + この札の v2 22 / 22 + 図の検算 7 / 7 + 問いの文の検査 3 / 3(guard・通らなければ走らない)。
- 問いの文の差分(olm113 の M2A との diff・座標は olm113 と同じ 37° の回転・O3 = (3.9524, −2.3865) は両方で同じ):
  ```
  -h1 = Circle(O1, 3.6869)
  +h1 = Circle(O1, 5.5738)
  -c = Circle(O2, 7.4607)
  -Tc = (2.7678, 1.2685)
  -Th = (7.6927, -3.2647)
  +c = Circle(O2, 5.5738)
  +Tc = (1.4899, -0.1199)
  +Th = (6.4148, -4.6530)
  ```
  検算: 問いの文の Tc・Th の中点 = ((1.4899 + 6.4148) / 2, (−0.1199 − 4.6530) / 2) = (3.95235, −2.38645) = O3(4 桁の丸めの内)。前提の文「general (non-special, non-degenerate)」は olm113 のまま(PREREG §5)。
- 開示: (1) smoke(凍結の前・2 行)の log は conjecture の類を印字する作りで、主 session は 2 行とも MIDO3 であるのを目にした(PREREG §6 に記載済・予想は smoke の前のまま)。(2) gen の log も batch ごとに類の数を印字する作りで、主 session は chain の終了後・read.json を開く前にそれ(MIDO3 13・10・14)を目にした。判定は read.json の値で付けた。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | olm113 の M2A が 60 行読める(md5 一致) | 60・`db0fde6e…` | ✓ |
| G1 | conjecture が取れた行 ≥ 0.80 | 50 / 60 = 0.833 | ✓ |
| G2(記述の側) | status が hypothesis / question の行 ≥ 0.70 | (44 + 1) / 60 = 0.75 | ✓ |
| Q2 の追加条件 | 両腕で EQ の行の証明の欄(空でない)≥ 8 | 等しい図 **0**・olm113 12 | **✗ → Q2 を読まない** |

## §2. 判定

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** | MIDO3 の割合(parsed の中)= 37 / 50 = **0.74**・olm113 = 17 / 50 = 0.34・Δ = **+0.40** | **増える**(Δ ≥ 0.15・境まで 0.25) | 増える **0.45**・変わらない 0.30・間 0.15・減る 0.10 → **当たり** |
| Q2 | EQ の行の証明の欄の SYMM: 等しい図 0 / 0・olm113 8 / 12 | **読まない**(EQ の証明 0 本 < 8) | 変わらない 0.40・増える 0.30・間 0.20・減る 0.10 → 判定なし |
| Q3 | 記述 | §3 | — |

- Q1 は境から遠い(0.25)。この series で予想が当たったのは olm114・olm116 の二枚の外れ(段を与えた時の続きを低く見た)の後の一枚目。
- Q2 が読めない理由そのものが記述の主値: **等しい図では apex(|O3Tc| = |O3Th|)の conjecture が一本も出ない**(olm113 16 / 50 → 0 / 50)。等しい図では等距離は退化して真(O3 が中点)で、OLMo はより強い文(中点 / 共線)を書く。予想は EQ が ≥ 8 本出る前提で付けており、出ない形は見ていなかった(関門が受けた)。

## §3. Q3(記述・read.json の逐語)

### 類と status・長さ

| 腕 | n | cls EQ / MIDO3 / OTHER / NONE | parsed | MIDO3 率 | EQ 率 | status hyp / question / other / none | 証明の欄あり | T 中央値 | 上限 | 答えが先 |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| 等しい図(olm117) | 60 | **0 / 37 / 13 / 10** | 50 | **0.74** | **0.00** | 44 / 1 / 2 / 13 | 46 | **560** | 2 | 1 |
| olm113 の M2A(同じ v2) | 60 | 16 / 17 / 17 / 10 | 50 | 0.34 | 0.32 | 41 / 1 / 0 / 18 | 41 | 1068.5 | 5 | 1 |

- status(類ごと): 等しい図 MIDO3 = hypothesis 33・none 3・other 1(b1_j03 = 欄に雛形の `"hypothesis" or "question"` をそのまま写した)・OTHER = hypothesis 11・other 1(b1_j04 = `"proposition" or "lemma"`)・question 1(b2_j02 `right_angle(Tc, O3, Th)`)。olm113 は EQ hypothesis 12・none 3・question 1 / MIDO3 15・2 / OTHER 14・3。status は等しい図でも正しさを追わない(真の MIDO3 も偽の OTHER も hypothesis 一色)= olm112 / 113 と同じ。
- T(類ごとの中央値): 等しい図 MIDO3 673(37)・OTHER 527(13)・NONE 149.5(10)。olm113 EQ 2294.5(16)・MIDO3 459(17)・OTHER 506(17)・NONE 2061(10)。olm113 で長かった EQ の行(等距離を数値で確かめる)が等しい図では無く、全体の中央値が半分(1068.5 → 560)・上限 5 → 2。
- MIDO3 の言い方: 等しい図 = 共線 20(`Tc, Th, O3 are collinear` の類)・**中点 16**(`O3 is the midpoint of Tc and Th` の類)・`O3 lies on l1` 1。olm113 = 共線 17・中点 0。

### 前提の語(SYMM / PAR / HOMO / POWER / COLL / EQR)

| 腕 | 当てた所 | n | SYMM | PAR | HOMO | POWER | COLL | EQR |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 等しい図 | 証明の欄(空でない) | 46 | 18 | 4 | 7 | 0 | 16 | **10** |
| 等しい図 | MIDO3 の証明の欄 | 33 | **16** | 1 | 6 | 0 | 13 | 10 |
| 等しい図 | EQ の証明の欄 | 0 | — | — | — | — | — | — |
| 等しい図 | 本文(60 行) | 60 | 27 | 13 | 14 | 1 | 40 | **24** |
| olm113 | 証明の欄(空でない) | 41 | 11 | 6 | 6 | 0 | 15 | 0 |
| olm113 | MIDO3 の証明の欄 | 15 | 2 | 1 | 3 | 0 | 10 | 0 |
| olm113 | EQ の証明の欄 | 12 | 8 | 2 | 2 | 0 | 0 | 0 |
| olm113 | 本文(60 行) | 60 | 26 | 20 | 20 | 0 | 50 | 2 |

- **本文の SYMM は 27 対 26 で同じ・証明の欄では 18 対 11**。考えの本文で「対称」を口にする率は図で変わらず、証明の欄に持ち込む率が上がった(等しい図では対称性の前提が真)。
- EQR(半径が等しいことへの言及)= 本文 24 / 60(olm113 2 / 60 = 「radii are equal」を否定する文脈など)。証明の欄 10 本(全部 MIDO3 の行)。
- 道の札(凍結の score_m2・本文): 等しい図 OTHER 34・ANALYTIC 18・TRAP 4・PROJ 4。olm113 OTHER 25・ANALYTIC 18・TRAP 10・PROJ 7。射影の語は等しい図でも増えない(4 本・いずれも「projection of O1O2 onto l1」の途中の語で、射影の道で中点に着いた行はない)。

### SYMM の種類(主 session の読み・MIDO3 の証明の欄 16 本・正規表現で二つに分けた = 記述)

| 種類 | n | 真偽(等しい図) | 例 |
|---|---:|---|---|
| O3 についての点対称(`symmetric with respect to O3`・`reflection over O3`) | 3(+ 両方 2) | 真 | b1_j05「the inner common tangent is symmetric with respect to the midpoint O3, so Tc and Th are symmetric about O3」・b2_j09「The tangent points Tc and Th are images of each other under reflection over O3」 |
| O1O2 についての線対称(`symmetric with respect to the line O1O2`・`reflections across the line connecting the centers`) | 3(+ 両方 2) | **偽**(内接線 l1 を O1O2 で折り返すと もう一本の内接線に移る・Tc は Th に移らない) | b0_j01「the symmetry of the tangent line with respect to the line O1O2」・b0_j12「the tangent's contact points are reflections across the line connecting the centers」・b2_j17「the tangent points Tc and Th are symmetric with respect to the line joining the centers」 |
| 種類を言わない(`by symmetry of the configuration`) | 8 | — | b0_j08「By symmetry of the configuration, O3 must lie on l1」・b2_j19「This is due to the symmetry of the setup and the properties of common tangents」 |

- 他の偽の前提(MIDO3 の証明の欄 33 本・正規表現・記述): 「l1(TcTh)∥ O1O2」**5**(外接線の性質・内接線では偽)・「O1O2 ⊥ l1」1・「O1O2 は TcTh の垂直二等分線」1。真の前提: 「半径が等しい → 相似の中心は O3(比 −1)」の homothety 6(b0_j03「By homothety centered at the intersection of the inner common tangents … O3 is the center of homothety」= 等しい図では正しい)。

### NONE 10 行と OTHER 13 行

- NONE(conjecture の欄が取れない)10: 上限 12288 で役割の暴走 2(b0_j00「Then, change your mind. Pretend you are a different person who considers the same configuration…」・b0_j17「I am a student of mathematics. I am learning to make conjectures. You are my teacher…」)・問いの文の指示を続けて書いただけ 6(T 7〜207: b0_j18「Do not respond with anything else.」・b1_j12「The answer is withheld to let you focus on the reasoning.\nAnswer with JSON only, no prose.」・b1_j08 / b1_j09 / b1_j15 / b0_j06 = 架空の追加の設問)・JSON なしの平文 1(b2_j03「The most important invariant in this configuration is that the points Tc, Th, and O3 are collinear. This follows from the fact that O3 is the midpoint of O1 and O2, and the tangent line l1 is … perpendicular to the line joining their centers.」= 意味は MIDO3 だが欄がないので v2 は数えない・R5)・長い暴走 1(b2_j10 T 7,873)。olm113 の NONE 10 は長い暴走(T 中央値 2061)で、等しい図では短い写し(149.5)に形が変わった(数は同じ 10)。
- OTHER 13: 意味は MIDO3 だが正規表現の外 **2**(b0_j10「Th and Tc are symmetric with respect to O3」・b0_j16「O3Tc is parallel to O3Th」= 共線の退化した言い方)・裸の `collinear` 3(b0_j13・b1_j04・b2_j14)・問いの文の定義の写し `O1, O3, O2 are collinear` 2(b1_j00・b1_j06)・記号の外 1(b1_j17「A, B, C are collinear」)・**偽** 5 = b1_j07「The points O1, O3, and Th are collinear.」・b1_j13「O3Tc is parallel to O1O2」・b2_j18「TcTh is parallel to O1O2」・b2_j06「O1O2 is perpendicular to ThTc」・b2_j02「right_angle(Tc, O3, Th)」(question)。2 本を MIDO3 に数えても 39 / 50 = 0.78 で判定は変わらない(数えない = 凍結の v2 のまま)。
- 「TcTh ∥ O1O2」「O1O2 ⊥ TcTh」は olm113 の誤アトラクタ(RESULT olm113 §6)と同じ語で、等しい図でも 3 本の conjecture と 6 本の前提に残る(外接線か対称な図の記憶・座標は見ていない)。

## §4. 逐語(PREREG §4)

### MIDO3 の行の conjecture と証明の欄(行の名の順・最初の 10 本)

| 行 | T | status | conjecture | proof(逐語) |
|---|---:|---|---|---|
| b0_j01 | 2,153 | hypothesis | O3 is the midpoint of Tc and Th | In the configuration of two disjoint circles with an inner common tangent, the line connecting the points of tangency (Tc and Th) is bisected by the midpoint of the line connecting the centers (O3). This follows from the symmetry of the tangent line with respect to the line O1O2, ensuring that O3 serves as the midpoint for both O1O2 and TcTh. |
| b0_j02 | 1,129 | hypothesis | Tc, Th, O3 are collinear | Since O1Tc and O2Th are both perpendicular to the inner tangent line l1, they are parallel. The line TcTh is thus parallel to l1. The midpoint O3 of O1O2 lies on the line TcTh because the symmetry of the configuration ensures that O3 is equidistant from both centers and the inner tangent's geometry forces the line TcTh to pass through O3. |
| b0_j03 | 313 | hypothesis | Tc, Th, and O3 are collinear | By homothety centered at the intersection of the inner common tangents, the line connecting the points of tangency Tc and Th passes through the midpoint O3 of the segment O1O2, since O3 is the center of homothety mapping one circle to the other and the tangents are preserved under homothety. |
| b0_j04 | 357 | hypothesis | O3 is collinear with Tc and Th | Since the circles have equal radii and are disjoint with an inner common tangent, the line O1O2 is the perpendicular bisector of the tangent segment TcTh. As O3 is the midpoint of O1O2, it lies on this perpendicular bisector, thereby making O3 collinear with Tc and Th. |
| b0_j05 | 281 | hypothesis | Tc, Th, O3 are collinear. O3 is the midpoint of O1 and O2. | The inner common tangent of two circles is parallel to the line through their centers. The line through O1 and O2 is the perpendicular bisector of the segment connecting their midpoints, and O3 is the midpoint of O1 and O2. Therefore, Tc, Th, and O3 are collinear. |
| b0_j07 | 363 | hypothesis | O3 lies on l1 | For two circles, the midpoint of the line joining their centers lies on their inner common tangent. |
| b0_j08 | 446 | hypothesis | Tc, Th, O3 are collinear | For two disjoint circles, the line joining centers O1O2 is perpendicular to inner common tangent l1. O3 is the midpoint of O1O2. By symmetry of the configuration, O3 must lie on l1. Since Tc and Th are on l1, Tc, Th, O3 are collinear. |
| b0_j09 | 1,094 | hypothesis | O3 is the midpoint of Tc and Th | Since O3 is the midpoint of O1 and O2, and the inner common tangent line l1 is parallel to the line connecting the centers (as the radii O1Th and O2Tc are perpendicular to l1), the contact points Tc and Th are symmetric with respect to O3. Calculating the midpoint of Tc and Th yields O3, confirming the invariant. |
| b0_j11 | 1,319 | none | O3 is the midpoint of TcTh | (空) |
| b0_j12 | 1,184 | hypothesis | O3 is the midpoint of Th and Tc | Given the inner common tangent, the radii O1Th and O2Tc are parallel and perpendicular to the tangent line. The midpoint O3 of O1O2 must also be the midpoint of Th and Tc due to the symmetry of the configuration, as the tangent's contact points are reflections across the line connecting the centers. |

- 10 本のうち、等しい図で真の前提だけで閉じるのは b0_j03(相似の中心)と b0_j09 の後半(点対称 + 数値)の 2 本。b0_j04・b0_j05・b0_j08・b0_j12 は偽の前提(O1O2 が垂直二等分線 / l1 ∥ O1O2 / O1O2 ⊥ l1 / O1O2 での折り返し)から真の結論へ。b0_j07 は一般の二円に言う(偽・等しい図だけで真)。

### EQ の行の証明の欄(最大 5 本)

- **0 本**(EQ の行がない)。

### EQR を含む本文の文(最大 5 本・行の名の順)

| 行 | cls | 文(逐語) |
|---|---|---|
| b0_j04 | MIDO3 | Reasoning: The circles c and h1 are of equal radii, and their centers O2 and O1 are equidistant from O3. |
| b0_j10 | OTHER | Their radii are the same since both are 5.5738. They have an inner common tangent line l1, which touches c at Tc and h1 at Th |
| b0_j11 | MIDO3 | But the radii are equal here (both 5.5738), so the ratio is 1. Therefore, the homothety center would be the midpoint O3. So the homothety with center O3 mapping h1 to c would send O1 to O2 (since O3 is midpoint) and Th to Tc |
| b0_j14 | MIDO3 | **Answer**: The homothety centered at O3 that maps O1 to O2 (since O3 is the midpoint of O1O2) also maps circle c (center O2, radius 5.5738) to circle h1 (center O1, same radius) |
| b0_j15 | MIDO3 | A homothety that maps one circle to the other would have its center along the line connecting O1 and O2. But since the circles are equal in radius (both 5.5738), the homothety center would be the midpoint O3. Wait, if the radii are equal, then the homothety center would be the midpoint |

- 文と図の食い違い(「general (non-special, non-degenerate)」と等しい半径)に触れた行(記述・EQR ∧ `degenerate|special|contradict` は 13 本だが、大半は問いの文の「non-degenerate」の写しで、食い違いに自分で触れた〔Wait など〕のは主 session の読みで 3 本): b1_j10「But wait, in the problem statement, it's mentioned that the configuration is general (non-special, non-degenerate). So this should hold in general for two congruent circles with an inner common tangent.」(等しい図を一般と見なす)・b1_j16「Wait, the problem says "the two circles are disjoint and have an inner common tangent; the configuration is general (non-degenerate)." So the radii are equal? Because both circles have the same radius (5.5738).」・b2_j07「That would be the case if the circles were congruent and the tangent was the perpendicular bisector, but that's not generally the case.」→ それでも conjecture は `O3 is the midpoint of Tc and Th`・証明の欄「By computation, the midpoint of Tc and Th is O3; the configuration's symmetry ensures that O3 remains the midpoint of the tangent points for two circles of equal radius … Therefore, O3 is always the midpoint of Tc and Th in the general (non-degenerate) case.」= 気付いた上で等しい図の文を「一般」と書き直す。
- 数値で中点を確かめた文(記述): b0_j09「Calculating the midpoint of Tc and Th yields O3」・b2_j07「By computation, the midpoint of Tc and Th is O3」・b2_j08「the coordinate calculation shows that O3 is the midpoint of Th and Tc」。`calculat|comput|verif|check` が `midpoint` の近くにある本文 10 / 60。

## §5. 主 session の読み(L3・値と並べる・判定は変えない)

1. **退化の主張は図を読んで増える**: olm113 で偽だった「Tc・O3・Th の共線」は、等しい図(真)で 0.34 → 0.74 に増え、言い方が「中点」(0 → 16)に移り、半径が等しいことへの言及が 2 → 24 に出て、数値で中点を確かめる行がある。PREREG §3 の読みの軸では「座標から図を読んでいる」側の形(増える + EQR)。olm113 の 17 本(偽の図で言った共線)が図を見ない記憶だけなのかは、この札では分けられない(減らなかった = 「記憶でない」の証拠は出なかった)。言えるのは、**この主張の率は図に感応する**(真の図で倍)ということ。
2. **apex(等距離)は等しい図で消える(16 → 0)**: 等距離は退化して真だが、OLMo はより強い中点 / 共線を書く。olm113 の EQ の行が長かった(T 2294.5)のは等距離を数値で確かめていたからで、等しい図ではその手間が消え(中点は一目)、全体が短く(1068.5 → 560)上限も減る(5 → 2)。Q2(EQ の証明の「対称性」の差)はこの形では測れない。
3. **「対称性」の前提は本文では図に依らず(27 対 26)・証明の欄で増える(11 → 18)**: 考えの本文で対称を口にする率は記憶で一定、それを証明に持ち込むかが図で変わる。ただし持ち込んだ対称の**種類**は半分が偽(O1O2 についての線対称 5 / 16・内接線では成り立たない)で、真の点対称(O3 について)は 5 / 16。等しい図でも「l1 ∥ O1O2」(外接線の性質)が 5 / 33 の前提と 3 / 13 の conjecture に残る。**前提は記憶の図(外接線か線対称の図)のまま、結論だけが真の図に合う** — これが olm113 §6-2「対称性は半径の等しい図の記憶」の、半分の肯定(等しい図で対称性は増える)と半分の訂正(その対称は内接線の対称でなく、別の図の対称)。
4. frontier との差(olm113 の prf5・射影 19 / 20)は等しい図でも同じ向き: 射影の道は 4 本の本文の途中の語だけで、中点に着いた道は数値(10)・相似(6)・対称(16)。
5. 予想: Q1 は当たり(0.45)。olm114・olm116 の二枚で「段を与えた時の続き」を低く見た後、この札は「図の記憶」の向きを高く置いて当たった。Q2 が読めない形(EQ 0 本)は PREREG の関門が受けたが、予想の分布はそれを見ていない。

## §6. 主張しないこと(PREREG §5 のまま)

- 等しい図では MIDO3 は真(退化)で、この札は正しさの率を測らない。並べる率は同じ v2 の類の率。
- 前提の文「general (non-special, non-degenerate)」は等しい図でも残した。文と図の食い違いに OLMo が気付くかは EQR と §4 の 3 本の記述だけ。
- 一つの model・一つの温度・60 行・一つの図(半径は平均 5.5738 で揃えた・他の揃え方は試していない)。
- SYMM と §3 の「種類」の正規表現は語の印で、対称性を正しく使ったかの検証ではない。OTHER の 2 本(点対称・O3Tc ∥ O3Th)を MIDO3 に数えない(凍結の v2)。

## §7. 次(先生の言葉で)

- 三枚(olm115 = v2 USE_PERP・olm116 = moy-2 の段の梯子・olm117 = 半径の等しい対照)はこれで揃った。
- 候補(起案はしない): 対称の種類(点対称 / 線対称)と外接線の記憶の印(`∥ O1O2`)を v3 の述語にして olm113・olm117 の両方に当て直す / 半径の等しくない図で「対称性」の語を本文からも消す条件(座標を与えない文)で率を見る。
