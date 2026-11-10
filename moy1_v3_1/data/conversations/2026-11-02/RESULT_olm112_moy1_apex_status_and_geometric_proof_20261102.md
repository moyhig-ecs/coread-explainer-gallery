HEAD(R1) = 35397b3d(執筆時の HEAD・fetch / pull 済み = origin より 9 commit 先・遅れ 0)

# RESULT(札 `olm112`・2026-11-02): moy-1 の答えに「仮説か問いか」と座標を使わない幾何学的証明を求めた OLMo-3 32B base の 100 行 — 答えの欄が apex の 37 行で、二等分線 → 直角 → Thales の逆の鎖は 0(Q1 偽)・申告は apex 36 / 36・attractor 28 / 29 が hypothesis で正しさを追わない(Q2 追わない)・attractor の率は 0.30 対 0.255 で変わらない(Q3・境まで 0.005)

- 札 = [PREREG](PREREG_olm112_moy1_apex_status_and_geometric_proof_20261102.md)(凍結 cb12da8d)・runner `ConstructGap/exp/olm112_moy1_apex_status_and_geometric_proof_20261102.py`・共通の部品 `ConstructGap/exp/hq_moy12_status_proof_common_20261102.py`(olm113・prf4・prf5 と同じ計器)。
- 出力 = `ConstructGap/exp/olm112/gen.json`(md5 `82b3e44c…`)・`read.json`(md5 `bde01bdc…`)・`gen_run.log`・`read_run.log`。
- 生成 = zebrashark・12:23:53 → 16:38:23(15,265 s・5 batch × 20 行・seed 20261120〜24)。gen の provenance = commit 775c017d・dirty false。read の provenance = commit 35397b3d・dirty false。script / common / prereg / prompt の md5 は gen と read で一致(prompt `7898ebb3…`)。版 = mlx 0.32.0・mlx-lm 0.31.3・transformers 5.14.1。
- 較正 61 / 61 は runner の guard で通った(通らなければ走らない)。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G1 | label の無い行 ≤ 4 | 0 | ✓ |
| G2 | status が hypothesis / question の行 ≥ 70 | 79(hypothesis 77・question 2・other 2・none 19) | ✓ |
| G3 | B-bind で証明の欄が空でない ≥ 0.50 | 37 / 37 | ✓ |
| G4 | B-bind ≥ 20 | 37 | ✓ |
| G5 | B-bind と B-attractor で hypothesis / question ≥ 10 | 36・29 | ✓ |

## §2. 判定

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** | 答えの欄 B-bind 37 行のうち CHAIN 0 = 0.00 | **偽**(≤ 0.05) | 偽 0.55 |
| Q2 | P(hypothesis \| bind) = 36 / 36 = 1.000・P(hypothesis \| attractor) = 28 / 29 = 0.966・d = +0.034 | **追わない**(\|d\| < 0.10) | 追わない 0.45 |
| Q3 | 答えの欄 B-attractor = 30 / 100 = 0.300・比べる元 = 102 / 400 = 0.255・Δ = +0.045 | **変わらない**(\|Δ\| < 0.05) | 変わらない 0.35 |

- Q3 は境(0.05)まで 0.005 しかない。判定は凍結の境の通りに付けたが、「追記で attractor が増えなかった」とまでは言えても、「同じだった」と強くは言えない。
- 答えの欄の印の内訳: この札 = B-bind 37・B-attractor 30・B-flail 18・B-stuck-L1 15 / 比べる元 400 行 = 194・102・49・55。

## §3. Q4(記述・群ごとの述語の数・read_run.log の逐語)

| 答えの欄 | n | BIS | ADJ | RA | THC | CHAIN | COORD | radical | homothety | power | 証明の欄あり | status | T の中央値 | 答えが先 | 上限で切れた |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| B-bind | 37 | 1 | 1 | 4 | 13 | **0** | 0 | 11 | 9 | 6 | 37 | hyp 36・other 1 | 3,005 | 2 | 0 |
| B-attractor | 30 | 0 | 0 | 0 | 5 | 0 | 1 | 6 | 17 | 2 | 29 | hyp 28・question 1・none 1 | 824.5 | 4 | 0 |
| B-stuck-L1 | 15 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 3 | 1 | 15 | hyp 13・question 1・other 1 | 752 | 1 | 3 |
| B-flail | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | none 18 | 621.5 | 0 | 4 |

- 本文全体(考えの部分を含む)の鎖 `body_chain` = 0 / 100。
- 語の数え(主 session・計器の外・正規表現は下・`gen.json` の `proof` と `content` に当てた):

| 語(正規表現・大小無視) | B-bind の証明の欄 / 37 | B-attractor の証明の欄 / 30 | 本文 / 100 |
|---|---:|---:|---:|
| 角の二等分線 `angle bisector\|bisector of (the\|an\|one) angle\|bisects the angle` | **0** | 0 | 2 |
| `right angle\|90` | 15 | 3 | 43 |
| `thales` | 4 | 2 | 8 |
| `dot product\|inner product` | 2 | 0 | 4 |
| `similitude\|apollon` | 2 | 3 | 19 |
| `monge` | 2 | 0 | 12 |
| `miquel` | 2 | 2 | 14 |

- 本文の角の二等分線の 2 行 = b3j8(下の §4 の最後)と b4j14(三角形の定理の一覧を繰り返して上限で切れた行・この問いの図形とは無関係)。

## §4. 逐語(PREREG §4 の通り)

- **CHAIN を満たした証明 = 0 本**(引く物がない)。
- **満たさなかった B-bind の行から 10 本**: PREREG の「行の名の順で 10 本おき」は 37 行だと 4 本にしかならず、同じ文の「10 本」と合わない。そこで、行の名を (batch, j) の数の順に並べ、**4 本おき(0・4・…・36 番目)で 10 本**を取った(この解釈は書いた後に決めたのではなく、引く前に決めた。ただし凍結の文とは違う)。

- **b0j0**(本文の印 B-bind・status hypothesis・述語 なし・129 字)
  > Each X_i forms a right angle with O1 and O2 (verified by zero dot product), confirming they lie on the circle with diameter O1O2.

- **b0j9**(本文の印 B-bind・status hypothesis・述語 ALT_radical・ALT_homothety・280 字)
  > By the properties of circle homotheties and the radical axis, the intersection points of the external and internal common tangents are always concyclic, lying on the circle of similitude whose center is the midpoint of O1O2 and whose radius is half the distance between O1 and O2.

- **b1j1**(本文の印 B-bind・status hypothesis・述語 なし・583 字)
  > Consider the circle with diameter O1O2. For any point X on this circle, the sum of the squares of the distances from X to O1 and O2 equals the square of the length of O1O2 (by the parallelogram law). Since each Xi is the intersection of a tangent to one circle and a tangent to the other, the power of Xi with respect to both circles satisfies a relation that places Xi on this circle. Specifically, the power of Xi with respect to K1 and K2 ensures that the distances from Xi to O1 and O2 conform to the circle’s defining property. Thus, all Xi lie on the circle with diameter O1O2.

- **b1j7**(本文の印 B-bind・status hypothesis・述語 ALT_radical・ALT_power・782 字)
  > The power of a point with respect to a circle is defined as the square of the length of the tangent from the point to the circle. For any common tangent of two circles, all points on the tangent have equal power with respect to both circles. Therefore, the intersections of common tangents (X1-X4) must lie on the radical axis of the two circles, which is the set of points with equal power. However, the radical axis is a line, and the four points are not collinear, indicating a different approach. Instead, consider the circle with diameter O1O2. The midpoint of O1O2 is equidistant from both centers, and any point on this circle has equal power with respect to both circles. Since X1-X4 are intersections of common tangents (which require equal power), they lie on this circle.

- **b1j17**(本文の印 B-bind・status hypothesis・述語 ALT_homothety・ALT_power・620 字)
  > For two disjoint circles, the four intersection points of their common tangents are concyclic. This is a classical result in geometry, known as the Miquel theorem for complete quadrilaterals. The circle passing through these four points (the Miquel circle) has its center at the midpoint of the segment joining the centers O1 and O2, and its diameter is the segment O1O2. This can be shown by considering the homothety centered at the external homothety center of the two circles, or by direct computation of the power of a point. Thus, X1, X2, X3, X4 always lie on this circle, regardless of the specific configuration.

- **b2j16**(本文の印 B-bind・status hypothesis・述語 RA・THC・193 字)
  > For any point Xi, the external and internal tangents to the circles imply that the vectors O1Xi and O2Xi are perpendicular. Hence, ∠XiO1O2 = 90°, making Xi lie on the circle with diameter O1O2.

- **b3j9**(本文の印 B-bind・status hypothesis・述語 ALT_radical・ALT_power・579 字)
  > Each intersection of external and internal tangents of two circles lies on the circle with diameter connecting the centers. Since X1-X4 are such intersections, they must lie on the circle centered at the midpoint of O1O2 with radius |O1O2|/2. This follows from the power of a point theorem: for any common tangent intersection, the power with respect to both circles is equal, placing it on the radical axis. However, in this configuration, the radical axis (a line) is orthogonal to O1O2, while the circle here is orthogonal to both circles and centered at the midpoint of O1O2.

- **b3j17**(本文の印 B-bind・status hypothesis・述語 ALT_radical・447 字)
  > By properties of tangents and the radical axis, the four intersection points of the external and internal common tangents of two disjoint circles are concyclic. The center of this circle is the midpoint of the centers of the two circles, and its radius is the distance from this midpoint to any of the intersection points. This follows from the symmetry of the configuration and the relationship between the tangent lines and the circles' centers.

- **b4j6**(本文の印 B-bind・status hypothesis・述語 THC・572 字)
  > By the properties of common tangents to two disjoint circles, each external tangent and internal tangent intersect at points forming right angles with the line connecting the centers. Specifically, for any point where an external tangent meets an internal tangent, the angle ∠O1PX = 90° (where P is the intersection point). This follows because the tangent at P to the circle with diameter O1O2 is perpendicular to O1O2, and the original tangents to K1 and K2 inherit this orthogonality. Thus, all four points X1–X4 lie on the circle with diameter O1O2 by Thales’ theorem.

- **b4j16**(本文の印 B-bind・status hypothesis・述語 ALT_power・275 字)
  > The four intersection points of the common tangents of two disjoint circles are always concyclic on a circle whose center is the midpoint of the segment joining the centers and whose radius is (R1*R2)/|O1O2|. This follows from the power of a point and properties of tangents.

- **追加の 1 本(PREREG の引き方の外・主 session が選んだ)**: b3j8 = 100 行で唯一、本文に鎖の一歩目(中心と交点を結ぶ線は二本の接線の角を二等分する)が出た行。答えの欄の印は B-attractor・本文の印は B-bind・T 4,768。本文(逐語・抜粋):
  > For a point outside a circle, the two tangent lines are equal in length, and the line from the center to the external point bisects the angle between the two tangents. Similarly for internal points, but internal tangents would require the point to be inside the circle, … Now, there's a theorem that says that the four mixed points (X1-X4) lie on a circle called the "midcircle" or the "homothetic circle," … Alternatively, the circle through X1-X4 is the circle with diameter HeHi.

  証明の欄(逐語): 「… This invariance implies that Xi must lie on the circle with diameter HeHi, as this circle is the set of points maintaining the homothety ratio between He and Hi. Thus, all four Xi are concyclic on this circle.」

## §5. frontier と並べる(同じ計器・L1)

| 札 | model | 問いの文 | 答えの欄 apex | CHAIN / apex | COORD | status |
|---|---|---|---:|---:|---:|---|
| **olm112(この札)** | OLMo-3 32B base | M1A(考えを先に + 追記) | 37 / 100 | **0 / 37** | 0 | hypothesis 77 / 100 |
| [prf4](RESULT_prf4_moy12_status_proof_claude_p_20261102.md) | Opus 5.5 xhigh | **M1A(同じ文)** | 8 / 8(ok 8 / 10) | **8 / 8** | 0 | hypothesis 8 / 8 |
| prf4 | Fable 5.1 xhigh | M1A(同じ文) | —(10 / 10 拒否) | — | — | — |
| [prf5](RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md) | Opus 5.5 xhigh | M1B(JSON だけ + 欄で求める) | 10 / 10 | 10 / 10 | 0 | hypothesis 10 / 10 |
| prf5 | Fable 5.1 xhigh | M1B | 10 / 10 | 10 / 10 | 0 | hypothesis 10 / 10 |

- **同じ文で並ぶのは Opus 5.5 × moy-1 の 8 本だけ**(prf4)。M1B は求める文が違う(考えを先に書かせない・「鎖を、使う事実の名を添えて」と求める)ので、OLMo との差には文の差が混ざる。OLMo に M1B を当てる腕(olm114 = 揃える腕)は走らせていない。

## §6. 読み(L3・主 session)

1. **求めても書けない**: 朝の事後の数え(答えの欄が O1O2 の 194 行で、作図で直角を導いた行 0・角の二等分線 0)は、証明を求めていない文での数だった。この札で証明を明示して求めても、apex の 37 行で鎖 0・角の二等分線 0 / 37。「求めていないから書かなかった」という説明は、この model・この文では消える。
2. **直角は「言う」が「導かない」**: B-bind の証明の欄で直角(`right angle|90`)を言う行は 15 / 37、Thales の逆の側(THC)は 13 / 37。けれども直角の出どころは、内積で確かめた(b0j0)、接線が O1Xi に垂直という誤った前提(b2j14)、直角三角形だから三平方(b4j4 = 循環)、「直交を受け継ぐ」(b4j6)のどれかで、二等分線から導いた行は無い。鎖の最後の一段(Thales の逆)だけがあり、前の二段が空。
3. **定理の名で埋める**: Monge・Miquel・circle of similitude・radical circle などの名が、実際にはその名の定理が言わない内容の根拠として使われる(b0j5・b0j7・b1j17 など)。B-bind の証明の欄で homothety の語は 9 / 37 で、attractor(HeHi の円)の側の語彙で apex を裏付けている。memory `project_name_retrieves_headline_text_retrieves_proof_part_neq2f_20261019`(名は看板を引き、証明に要る部分は引かない)と同じ形に見える(家の中の札どうしの照合)。
4. **一歩目には一度届いた**: b3j8 は本文で一歩目(中心と交点を結ぶ線は接線の角を二等分する)を書いたが、次の文で離れ、「there's a theorem that says…」と名を探しに行って HeHi に着いた。1 行の観察。
5. **申告は既定の札**: hypothesis は apex でも attractor でもほぼ全部で、question は 100 行で 2。frontier も 28 / 28 が hypothesis。この問いの立て方では、status の欄は「当てずっぽうかどうか」を分けない。分けるのは裏付けの欄(CHAIN)の方で、OLMo 0 / 37 と Opus 8 / 8(同じ文)で割れた。

## §7. 言えない

- CHAIN は語の鎖で、証明の正しさの検証ではない(prf5 の frontier の証明が正しいことは主 session が読んだだけ)。CHAIN でないことは、証明できないことの証明ではない。
- 求めて書かせた証明は事後の物で、導いた順は見えない。frontier が先に二等分線から円に着いたのか、円を知っていて後から証明を組んだのかは、どの札でも区別できない。
- **base model と chat model の比べ**: OLMo-3 32B は base(指示の調整なし)で、証明の欄は文書の続きとして書かれる。Opus / Fable は指示に従うよう調整された model。差には能力の差と、後からの調整の差が混ざる。
- 一つの model・一つの文・一つの温度(0.7)。同じ文の frontier 側は Opus × moy-1 の 8 本だけ。
- 計器の誤り(R4・判定は変えない): BIS が「diagonals … bisect each other」(b1j3・角の二等分線でない)に当たった。COORD は「verified by zero dot product」(b0j0)・「dot product is zero」(b3j1)を拾わない(小数と ≈ だけを見る)。どちらも RA と THC がそろわないので Q1 には効かない。
- Q3 の比べる元(olm87・olm90)とは、追記のほかに JSON の欄の数と文の長さも違う(PREREG §5)。

## §8. 次

- olm113(moy-2・M2 / M2A 各 60 行)は 16:38 に生成を始めた。終わったら RESULT。
- 揃える腕 olm114(OLMo に prf5 の M1B / M2B の文)は先生の言葉で。
