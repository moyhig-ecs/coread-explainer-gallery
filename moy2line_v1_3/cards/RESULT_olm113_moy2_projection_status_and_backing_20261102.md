HEAD(R1) = 3e2093a9(執筆時の HEAD・fetch 済み = origin より 10 commit 先・遅れ 0)

# RESULT(札 `olm113`・2026-11-02): moy-2(新規)で答えに「仮説か問いか」と裏付け(道は縛らない)を求めた OLMo-3 32B base の 60 + 60 行 — apex は追記なし 14 / 60・追記あり 16 / 60 で変わらない(Q2 Δ +0.033)・申告は apex 12 / 13・apex でない 29 / 29 が hypothesis で正しさを追わない(Q1 d = −0.077・追わない)・裏付けの道は射影 0 / 16・台形 1(語だけ)・ほか 15 = 「対称性」の誤った前提 8 本・平行の誤った前提 2 本・数値の確かめ 1 本・相似の中心 2 本 — 射影の道に着いた 1 本(b2j7)は本文で数値から見つけて reason に書き、status と proof の欄は書かなかった — frontier(prf5)は apex 20 / 20 が射影 19 + 台形 1

- 札 = [PREREG](PREREG_olm113_moy2_projection_status_and_backing_20261102.md)(凍結 cb12da8d・HEAD(R1) 5f793f86)・runner `ConstructGap/exp/olm113_moy2_projection_status_and_backing_20261102.py`・共通の部品 `ConstructGap/exp/hq_moy12_status_proof_common_20261102.py`(olm112・prf4・prf5 と同じ計器・較正 61 / 61 は runner の guard で通った)。
- 出力 = `ConstructGap/exp/olm113/gen.json`(md5 `db0fde6e…`)・`read.json`(md5 `24f43a85…`)・`gen_run.log`・`read_run.log`。
- 生成 = zebrashark・olm112 の read の直後 16:38:23 → 20:49:20(15,057 s・2 腕 × 3 batch × 20 行・seed 20261130〜32・二つの腕で同じ seed)。gen の provenance = commit 35397b3d・dirty false。read の provenance = commit 3e2093a9・dirty false。script / common / prereg / prompt の md5 は gen と read で一致(M2 `ddf4ba07…`・M2A `56182280…`)。版 = mlx 0.32.0・mlx-lm 0.31.3・transformers 5.14.1。
- 問いの文は moy-1 と同じ 37°(半径 3.6869 / 7.4607・**半径は等しくない**)。この事実は §4・§6 の読みの軸になる。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G1(M2) | conjecture が取れた行 ≥ 0.80 | 49 / 60 = 0.817 | ✓ |
| G1(M2A) | 同上 | 50 / 60 = 0.833 | ✓ |
| G2 | M2A で status が hypothesis / question ≥ 0.70 | 42 / 60 = 0.700(hypothesis 41・question 1・none 18) | ✓(境の上) |
| G3 | M2A の apex・apex でない行の両方で hypothesis / question ≥ 10 | 13・29 | ✓ |

- G2 は境(0.70)にちょうど乗った。none 18 のうち 10 は conjecture も空(JSON を閉じなかった・上限で切れた 5 行のうち 4 を含む)。

## §2. 判定

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** | M2A で P(hypothesis \| apex) = 12 / 13 = 0.923・P(hypothesis \| apex でない) = 29 / 29 = 1.000・d = −0.077 | **追わない**(\|d\| < 0.10) | 追わない 0.40 |
| Q2 | apex の率 M2A 16 / 60 = 0.267・M2 14 / 60 = 0.233・Δ = +0.033 | **変わらない**(\|Δ\| < 0.05) | 変わらない 0.40 |
| Q3 | 記述 | §3・§4 | — |

- 両方とも予想の最頻の側。Q1 の唯一の question(M2Ab2j4)は **apex の行**で、「apex でない行が問いと言う」向きではない。
- apex の率 0.23〜0.27 は、moy-1(olm112 の bind 0.37・比べる元 0.485)より低い。初めての moy-2 なので比べる元はこの札の M2 の腕だけ。

## §3. Q3(記述・read.json の `Q3_desc` の逐語)

| 腕 | n | apex | conjecture 空 | status | T の中央値 | 上限で切れた | 答えが先 |
|---|---:|---:|---:|---|---:|---:|---:|
| M2(追記なし) | 60 | 14 | 11 | none 60(欄を求めていない) | 533.5 | 2 | 0 |
| M2A(追記あり) | 60 | 16 | 10 | hypothesis 41・question 1・none 18 | 1,068.5 | 5 | 1 |

- **apex の行の道の札**(計器の `route` = PROJ → TRAP → ANALYTIC → CONG → OTHER の順に最初に当たる物):

| 腕 | 当てる所 | n(欄あり) | PROJ | TRAP | ANALYTIC | CONG | OTHER | 語: PROJ / PERPT / TRAP / PB / MIDTT / COORD / ALG / CONG |
|---|---|---:|---:|---:|---:|---:|---:|---|
| M2A | **証明の欄** | 16(12) | **0** | 1 | 0 | 0 | 15 | 0 / 1 / 1 / 5 / 0 / 0 / 0 / 0 |
| M2A | reason の欄 | 16(16) | 1 | 0 | 0 | 0 | 15 | 1 / 0 / 0 / 7 / 0 / 0 / 0 / 0 |
| M2A | 本文全体 | 16(16) | 3 | 6 | 7 | 0 | 0 | 3 / 8 / 6 / 11 / 9 / 16 / 14 / 2 |
| M2 | reason の欄 | 14(14) | 0 | 0 | 0 | 0 | 14 | 0 / 0 / 0 / 2 / 0 / 0 / 0 / 0 |
| M2 | 本文全体 | 14(14) | 1 | 0 | 13 | 0 | 0 | 1 / 1 / 0 / 2 / 2 / 14 / 10 / 1 |

- 本文全体で射影の道の語が揃う行(PERPT ∧ (PROJ ∨ TRAP) ∧ MIDTT・主 session の数え・計器の外)= M2A の apex 16 のうち 6(b0j4・b0j11・b0j15・b2j7・b2j10・b2j19)・M2A 全 60 のうち 10・M2 の apex 14 のうち 0・M2 全 60 のうち 2。本文は座標(COORD 16 / 16)で探りながら、射影や台形の語を**通り過ぎる**。証明の欄に残るのは別の物(§4)。
- **証明の欄 12 本の前提の語**(主 session の正規表現・計器の外): `symmetr|reflect` **8**(b0j2・b0j4・b0j5・b0j8・b0j11・b1j0・b1j14・b2j2)/ `homothet` 2(b0j15・b2j4)/ `parallel` 2(b1j14・b2j19)/ 数値の確かめ(`almost|nearly|distance formula`)1(b0j9)/ `power of` 1(b1j0)/ `⊥|perpendicular to` 2(b0j8・b0j15)/ `perpendicular bisector` 5 / `midpoint of TcTh` **0** / `foot|project` **0**。
- **apex でない行の conjecture**(主 session の分類・計器の外): M2 46 行 = 共線(Tc・O3・Th が一直線)**23**・平行 6・中点 5・垂直 1・空 11 / M2A 44 行 = 共線 **24**・平行 4・中点 2・垂直 3・ほか 1(`TcTh || O1O2`)・空 10。moy-2 の誤アトラクタは「Tc・O3・Th の共線」で、両腕で apex でない行の半分。
- 長さ: 追記ありの腕は中央値で 2 倍(533.5 → 1,068.5 token)。上限 12,288 で切れた行 2 + 5。

## §4. 逐語(PREREG §4 = M2A の apex の行の証明の欄を道の札ごとに 3 本ずつ・無ければある分)

### TRAP(1 本 = ある分)

- **M2Ab1j0**(status hypothesis・本文の道 TRAP・T 1,282)
  > For any inner common tangent to two circles, the power of the midpoint of the segment joining the centers with respect to both circles is equal, thus the distances from the midpoint to each point of tangency are equal. This is a direct consequence of the symmetry and properties of the midline in the configuration.

  L3: 「中点の二つの円に対する方べきが等しい」は半径が等しい時だけ成り立つ(|O3O1|² − r1² と |O3O2|² − r2²・この問いは 3.6869 / 7.4607)。TRAP の札は `midline` の一語で付いた。中線の性質は名指しされるだけで、何の中線かは書かれない。

### OTHER(15 本のうち欄のある 11 本から、行の名の順に 3 本)

- **M2Ab0j2**(status hypothesis・本文の道 ANALYTIC・T 8,263)
  > In an inner common tangent configuration, the midpoint O3 of O1O2 lies on the perpendicular bisector of TcTh by symmetry. This implies that O3 is equidistant from Tc and Th, as the perpendicular bisector consists of all points equidistant from Tc and Th. Therefore, |O3Tc| = |O3Th| holds universally for any such non-special configuration.

- **M2Ab0j4**(status hypothesis・本文の道 TRAP・T 5,830)
  > The midpoint O3 of O1O2 is equidistant from Tc and Th because the inner common tangent's symmetry ensures that O3 lies on the perpendicular bisector of TcTh, a property that holds universally in such configurations.

- **M2Ab0j5**(status hypothesis・本文の道 TRAP・T 2,418)
  > Since O3 is the midpoint of O1O2, reflecting Tc over O3 yields Th. This reflection symmetry ensures that O3Tc = O3Th, as reflections preserve distances from the midpoint.

  L3: 三本とも「対称性」が前提。O1O2 の線での鏡映は円を各々に写すが、内接線をもう一本の内接線に写す(Tc は Th でなく、もう一本の接線の接点に行く)。O3 での点対称(b0j5)は半径が等しい時だけ Tc を Th に写す。どれも**半径が違う**この問いでは成り立たない前提で、結論は正しい。

### 残り 8 本(PREREG の外・短いので全部・補)

- **M2Ab0j8**(hypothesis・本文 ANALYTIC・T 1,176)
  > Let O1 and O2 be the centers of circles c and h1, with inner common tangent points Tc (on c) and Th (on h1). Let O3 be the midpoint of O1 and O2. The line joining O1 and O2 is perpendicular to the tangent line at Tc and Th, and O3 is the midpoint of O1O2. Since the tangent points are symmetric with respect to the line joining the centers, their distances to O3 are equal. Thus, |O3-Tc| = |O3-Th|.

  L3: 「O1O2 が接線に垂直」は偽(垂直なのは半径 O1Th・O2Tc)。
- **M2Ab0j9**(hypothesis・本文 PROJ・T 2,171)
  > Calculate the distances TcO3 and ThO3 using the distance formula. The values are almost equal, confirming that O3 is equidistant from Tc and Th.

  L3: 数値の確かめを証明の欄に書いた。「almost equal」。本文の PROJ の語は「O3 は TcTh を O1O2 に射影した物の中点か」という探りの文で、道ではない。
- **M2Ab0j11**(hypothesis・本文 TRAP・T 6,532)
  > Since O3 is the midpoint of O1O2, and the inner common tangent's points of contact Tc and Th are symmetric with respect to the line O1O2, the distances from O3 to Tc and Th must be equal. This follows from the reflection symmetry across the line O1O2, which maps Tc to Th and vice versa, preserving distances.
- **M2Ab0j15**(hypothesis・本文 TRAP・PERPT と PB の語あり・T 8,513)
  > For the inner common tangent, O1T_h ⊥ l1 and O2T_c ⊥ l1, so O1T_h ∥ O2T_c. Homothety centered at the radical axis's intersection maps T_c to T_h, preserving midpoint properties. Since O3 is the midpoint of O1O2, it must lie on the perpendicular bisector of TcTh, enforcing O3Tc = O3Th.

  L3: 一文目は正しい出だし(半径 ⊥ 接線 → 平行)。二文目で「根軸の交点を中心とする相似」に跳び、三文目は結論。平行から垂直二等分線へ渡る段(射影か中線)が無い。
- **M2Ab1j14**(hypothesis・本文 ANALYTIC・T 2,125)
  > O3 is the midpoint of O1O2. The inner common tangent is parallel to O1O2, and Tc, Th are points of tangency on c and h1. The construction of the tangent ensures symmetry about the line O1O2, so the distances from O3 to Tc and Th are equal.

  L3: 「内接線は O1O2 に平行」は偽(内接線は O1O2 と交わる)。
- **M2Ab2j2**(hypothesis・本文 ANALYTIC・T 1,150)
  > O3 as the midpoint of O1O2, and the inner tangent points Tc and Th being symmetric with respect to O1O2, implies O3Tc = O3Th.
- **M2Ab2j4**(**question**・本文 ANALYTIC・T 2,016・conjecture「O3 lies on the perpendicular bisector of TcTh」)
  > Let's consider the homothety center mapping circle c to h1. The homothety maps O2 to O1, and the common inner tangent maps to itself. The points Tc and Th are mapped to each other by this homothety. The center O3 of homothety is the midpoint of O1O2. The perpendicular bisector of TcTh passes through the center of homothety, so O3 lies on it.

  L3: 内相似の中心が O1O2 の中点になるのは半径が等しい時だけ。唯一の question の行で、証明の欄は仮定を重ねている。
- **M2Ab2j19**(hypothesis・本文 PROJ・PB の語あり・T 1,511)
  > Given that O3 is the midpoint of O1O2 and TcTh is parallel to O1O2, the perpendicular bisector of O1O2 is also the perpendicular bisector of TcTh. Therefore, O3 is equidistant from Tc and Th.

  L3: 「TcTh ∥ O1O2」は偽。本文の PROJ の語は「TcTh の中点は Tc・Th を O1O2 に射影した物の中点」という文で、向きが逆(O1・O2 を接線に射影するのが道)。

### 射影の道に着いた 1 本(証明の欄なし・PREREG の外・補)

- **M2Ab2j7**(status **none**・証明の欄 **なし**・本文の道 PROJ・T 8,672・上限で切れていない)。本文は座標で O3 の足を計算し「the projection of O3 onto l1 is approximately the midpoint of Tc and Th」と見つけ、そこから言い直しを十数回繰り返して JSON に着く。JSON は追記の二つの欄(status・proof)を書かずに閉じた:
  > {"conjecture": "O3 lies on the perpendicular bisector of Tc and Th", "reason": "The midpoint M of Tc and Th is the foot of the perpendicular from O3 to the line TcTh. Since O3 projects orthogonally onto M, O3 must lie on the perpendicular bisector of TcTh.", "closes_goal": true}

  L3: reason は射影の道の**結論の形**(O3 の足が TcTh の中点)を正しく書いている。しかし「足が中点になる」ことは本文で数値(≈)から見つけた物で、「Tc・Th は O2・O1 の足 → 射影は中点を保つ」の段は本文にも無い(本文に「Tc is the projection of O2 onto l1, and Th is the projection of O1 onto l1」の文はあるが、そこから O3 の足へ渡る文は数値)。frontier(prf5)が 19 / 20 で書いた段が、OLMo では数値の確かめに置き換わる。

## §5. frontier と並べる(同じ計器・L1)

| 札 | model | 問いの文 | 答えの欄 apex | 証明の欄の道(apex) | status |
|---|---|---|---:|---|---|
| **olm113(この札)** | OLMo-3 32B base | M2A(考えを先に + 追記・道は縛らない) | 16 / 60 | **PROJ 0・TRAP 1(語だけ)・OTHER 15**(欄なし 4) | hypothesis 41 / 60・question 1 |
| olm113 | OLMo-3 32B base | M2(追記なし) | 14 / 60 | —(欄を求めていない) | — |
| [prf4](RESULT_prf4_moy12_status_proof_claude_p_20261102.md) | Opus / Fable | M2A(同じ文) | —(moy-2 は読める単位なし・拒否) | — | — |
| [prf5](RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md) | Opus 5.5 xhigh | M2B(JSON だけ + 欄で求める) | 10 / 10 | **PROJ 9・TRAP 1** | hypothesis 10 / 10 |
| prf5 | Fable 5.1 xhigh | M2B | 10 / 10 | **PROJ 10** | hypothesis 10 / 10 |

- **moy-2 では同じ文で並ぶ frontier の行が無い**(prf4 の moy-2 は Opus・Fable とも拒否)。M2B は求める文が違う(考えを先に書かせない)ので、OLMo との差には文の差が混ざる。moy-1 の olm114(frontier の証明の欄を書き出しに与える・凍結はこの後)の moy-2 版は先生の言葉で。
- 同じ計器で読める差: 道の札 PROJ は frontier 19 / 20・OLMo 0 / 16。語 MIDTT(TcTh の中点)は frontier の証明の欄 19 / 20・OLMo の証明の欄 0 / 16(本文には 9 / 16)。

## §6. 読み(L3・主 session)

1. **道の有無は moy-1 と同じ形で割れた**: moy-1(olm112)は「直角は言うが導かない」、moy-2 は「垂直二等分線は言うが導かない」。渡りの段(moy-1 = 角の二等分線・moy-2 = 射影か中線)が証明の欄に無い点が共通で、どちらも定理や性質の**名**(対称性・相似の中心・方べき・中線)で段を埋める。
2. **「対称性」は半径が等しい図の記憶**: 12 本中 8 本の前提。等しい半径なら O1O2 の線での鏡映でも O3 での点対称でも正しいので、この前提は「よくある図」から来た物に見える。問いの文には半径 3.6869 / 7.4607 が数字で書いてあり、本文は座標でその数字を使っている(COORD 16 / 16)のに、証明の欄に戻る時には対称な図に戻る。先生の 11-02 朝の言葉「幾何学的に証明を要求すると、共通接線の作図手順に遡らないといけない」に照らすと、OLMo は作図(半径 ⊥ 接線)に遡らず、図の記憶に遡る。
3. **射影の道は本文に在って欄に残らない**: 本文で PERPT ∧ (PROJ ∨ TRAP) ∧ MIDTT が揃う apex の行は 6 / 16。しかしその 6 本の証明の欄は対称性 2(b0j4・b0j11)・相似 1(b0j15)・平行 1(b2j19)・欄なし 2(b2j7・b2j10)。b2j7 は reason に射影の結論を書いたが、status と proof の欄を書かなかった(追記の二つの欄を落とした行 18 のうちの一つ)。
4. **申告は既定の札(moy-1 と同じ)**: hypothesis は apex 12 / 13・apex でない 29 / 29。question は 1 で、それは apex の行。誤アトラクタ(共線 24 / 44)も 100% hypothesis。olm112 の「status の欄は当てずっぽうかどうかを分けない」が moy-2 でも同じ。
5. **追記は apex を動かさない(moy-1 と同じ)**: Δ = +0.033(olm112 は +0.045)。長さは 2 倍になるが、答えの欄の着く先は変わらない。
6. **moy-2 の誤アトラクタは共線**: 「Tc・O3・Th が一直線」が apex でない行の半分(23 / 46・24 / 44)。これは O3 が接線上に在ると言っており、距離 (r1 − r2) / 2 ≈ 1.887 の分だけ外れている。moy-1 の誤アトラクタ(HeHi・radical)と違い、一つの命題に集まる。

## §7. 言えない

- 道の札は語の印で、証明の正しさの検証ではない。「対称性」の前提が偽であることは主 session が読んで言った物(半径の違いから機械的に言えるが、計器には無い)。
- status は申告。apex でない行が hypothesis と言うことは、誤りに気付かなかったことの証拠ではない。
- 一つの model・一つの文(37°)・一つの温度(0.7)。moy-2 の F5a-2 の形はこの札が初めてで、比べる元は同じ札の M2 の腕だけ。
- G2 は境の上(0.700)。追記の欄を落とす行が 18 / 60 あり、その中に射影の道に着いた b2j7 が入っている。欄を落とした行の中身は Q1 に入らない。
- 同じ文の frontier の行は moy-2 には無い(prf4 は拒否)。§5 の差には文の差が混ざる。

## §8. 次

- moy-1 の olm114(frontier の証明の欄を k 段まで書き出しに与えて続きを読む・JSON だけの文の揃える腕を含む)= この後に smoke → 凍結・本走は明日。
- moy-2 の同じ形(frontier の射影の証明を段で与える)は先生の言葉で。
- 「対称性」の前提が半径の等しい図から来るかは、半径を等しくした問いの文(対照)で分けられる(未着手・先生の言葉で)。
