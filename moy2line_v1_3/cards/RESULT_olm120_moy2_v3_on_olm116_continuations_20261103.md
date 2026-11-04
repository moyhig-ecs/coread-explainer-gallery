HEAD(R1) = 89047e90(執筆時の HEAD = 凍結の commit・fetch 済・origin より 15 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記だけ)

# RESULT(札 `olm120`・2026-11-03): 述語 v3 を olm116 の続きに当てる — frontier の証明を段で与えた後の OLMo-3 32B base の続き(k1・40 本)では、**O1O2 についての線対称を肯定して述べる行は 0 / 40**(olm113 の証明の欄 5 / 41 = 0.122・Δ −0.122・Q1 **下がる**・予想は間 0.35 で**外れ**〔下がる 0.30〕)、**外接線の記憶の印は 4 / 40 = 0.10**(olm113 0.244・Δ −0.144・Q2 **下がる**・予想 0.50 で当たり)、点対称 1 / 40(退化の主張「projections … are symmetric about the midpoint O3」)— k2(足 = 中点の段まで)の続き 38 本は全部 0 — 「対称」の語は Opus の文の続きにだけ 5 / 20(全部 種類なし「By symmetry」)・外接線の印は Fable の文の続きに 3 / 20・Opus 1 / 20 — 4 本の外接線の印のうち 2 本は計器の取りこぼし(「the line through O3 parallel to O1O2」を PAR3 が・「**th**e midpoint … lies on the perpendicular bisector of O1O2」の th を Th と読んで PBIS3 が拾う)で、実は 2 / 40 = 0.05・判定は変わらない

- 札 = [PREREG](PREREG_olm120_moy2_v3_on_olm116_continuations_20261103.md)(凍結 89047e90・HEAD(R1) 86af77f0・G10 通る・台帳 済)・runner `ConstructGap/exp/olm120_moy2_v3_on_olm116_continuations_20261103.py`(md5 `c89de4d5…`・model なし)・読み込むだけの部品 `olm118_…py`(`136f72b9…`・v3)・`hq_moy12_…py`(`426e2089…`)・入力 `olm116/gen.json`(`e66433f2…`)・`olm118/read.json`(`bffeb826…`)= guard で一致。
- 出力 = `ConstructGap/exp/olm120/read.json`(md5 `bb3f10d9…`)・`read_run.log`。走り = zebrashark 11-03 15:22 JST(`--read`・数秒・olm119 の本走と並行 = 読みだけ)・Traceback 0。provenance = commit 89047e90・dirty true(台帳の追記のみ)・prereg md5 `114f0d15…`。
- 較正 = v3 54 / 54(guard)。当てた文 = 各行の `cont`(OLMo の続きだけ・frontier の段は当てない)。
- 開示: PREREG §0 のとおり olm116 の v2 の値(k1 の SYMM 5・PAR 2)は既知。種類と OUTER は未知で読んだ。主 session は `--read` の印字を read.json と同時に見た。

## §1. 関門(read.json の値)

| 関門 | 条件 | 値 | |
|---|---|---|---|
| G0 | md5 一致・v3 の較正 54 / 54・olm113 の証明の欄 n = 41 | 一致・54 / 54・41 | ✓ |
| G1 | k1 の続きが空でない行 ≥ 32 / 40 | 40 / 40(k2 は 38 / 40) | ✓ |

## §2. 判定(k1 の続き 40 本・asserted の率・Δ = k1 − olm113 の証明の欄)

| Q | 数 | 判定 | 予想(凍結の p) |
|---|---|---|---|
| **Q1(主)** 線対称 LN_a | k1 **0 / 40 = 0**・olm113 5 / 41 = 0.122・Δ = **−0.122** | **下がる**(Δ ≤ −0.08・境まで 0.042) | 間 **0.35**・下がる 0.30・変わらない 0.30 → **外れ**(二番目の帯) |
| Q2 外接線の印 OUTER_a | k1 **4 / 40 = 0.10**・olm113 10 / 41 = 0.244・Δ = **−0.144** | **下がる**(Δ ≤ −0.12・境まで 0.024) | 下がる **0.50**・間 0.30 → 当たり |
| Q3 点対称 PT_a(記述) | k1 **1**・k2 0(olm113 0・olm117 4) | — | — |

- Q1 の外れの向き: 主 session は olm116 の「対称」5 本の半分が種類を名指すと見たが、5 本とも「By symmetry」の名なし(§3)。足場の後の続きでは、対称を口にしても軸を言わない。
- v2 の値(olm116 の W_SYMM 5・W_PAR 2)は v3 の SYMM 5・PAR3 2 と一致(同じ語の印)。

## §3. Q4(記述・read.json の逐語)

| 腕 | n | SYMM | 種類 PT / LN / BOTH / OTH / NONE / — | PT_a | LN_a | OUTER_a | PAR3_a | PERP3_a | PBIS3_a |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| k1(設定まで与えた)全体 | 40 | 5 | 1 / 0 / 0 / 0 / 4 / 35 | 1 | **0** | **4** | 2 | 1 | 2 |
| k1 Opus の文の続き | 20 | **5** | 1 / 0 / 0 / 0 / 4 / 15 | 1 | 0 | 1 | 0 | 0 | 1 |
| k1 Fable の文の続き | 20 | 0 | 0 / 0 / 0 / 0 / 0 / 20 | 0 | 0 | 3 | 2 | 1 | 1 |
| k2(足 = 中点の段まで)全体 | 38 | **0** | 0 / 0 / 0 / 0 / 0 / 38 | 0 | 0 | **0** | 0 | 0 | 0 |
| (比べる元)olm113 の証明の欄 | 41 | 11 | 0 / 5 / 0 / 0 / 6 / 30 | 0 | 5 | 10 | 7 | 4 | 0 |
| (参考)olm117 の証明の欄 | 46 | 18 | 3 / 6 / 1 / 0 / 8 / 28 | 4 | 7 | 13 | 8 | 4 | 2 |

- 「対称」の語は **Opus の文の続きにだけ** 5 / 20(Fable 0 / 20)。olm116 の RESULT の family 差(Opus の続きは対称 5・共線 4 へ流れる)と同じ 5 本。v3 の種類は 4 本が名なし・1 本が点対称。
- 外接線の印は **Fable の文の続きに** 3 / 20・Opus 1 / 20。Fable の文(`Step n (題):`)の続きは段の語で埋まる(olm116: Q1 15 / 20)が、埋めた段の中に「O1O2 ∥ ThTc」「O1O2 ⊥ l1」が入る(k1_0_j03)。
- k2 は 38 本とも当たりなし。足 = 中点の段まで与えられると、残りは短く(olm116: 中央値 125 字)閉じるだけで、記憶の前提が入る余地がない。

### 当たりの文(k1・全部・逐語)

| 行 | 文 | 印 | 読み(L3) |
|---|---|---|---|
| k1_0_j03(fable_r3) | 「Now O1O2 is parallel to ThTc, because both are perpendicular to the same line l1 (from steps 1,2 and 3).」「… which is parallel to O1O2 (from 8), and O1O2 is perpendicular to l1 (since O1, O2 both project perpendicularly onto l1).」 | PAR3・PERP3 | 外接線の印(本物・偽)。段 1〜3(半径 ⊥ 接線)から「O1O2 ⊥ l1」を導く = 半径と中心線の取り違え |
| k1_0_j13(opus_r3) | 「7) By symmetry (O1O2 is the perpendicular bisector of TcTh), the distances O1Tc and O2Th are equal, and O3 lies on that perpendicular bisector.」 | PBIS3・SYMM(名なし) | 外接線の印(本物・偽)。括弧の中は O1O2 についての線対称と同じ意味だが、v3 の LN の形(`symmetric with respect to …`)ではないので NONE。**意味で数えれば LN 1 / 40 = 0.025 → 判定は下がるのまま** |
| k1_0_j15(opus_r5) | 「5. Reflecting the line through midpoints O1–O2 across l1 sends O2→O1, hence O1→O2, and the midpoint O3→itself. 6. Therefore O3 is fixed by that reflection, i.e. O3 lies on the perpendicular bisector of segment TcTh.」 | SYMM(名なし) | l1 についての折り返し(軸 = 接線・偽: l1 での折り返しは O2 を O1 に送らない)。v3 の OTH の形(`reflect … across l1` は `_OF` の句が合わず)に当たらず NONE。意味では「他の軸」 |
| k1_0_j18(opus_r8) | 「By symmetry, the projection of O3 onto l1 is the midpoint of TcTh.」 | SYMM(名なし) | 名なし。結論は真(射影の事実)で、理由だけ「対称」 |
| k1_0_j19(opus_r9) | 「3) By symmetry of the inner‐common‐tangent setup, the distances from O3 to Tc and from O3 to Th are equal.」 | SYMM(名なし) | 名なし。olm113 の EQ の証明の「by symmetry of the configuration」と同じ形 |
| k1_1_j04(fable_r4) | 「Equivalently, the midpoint M = midpoint(Tc, Th) of the tangent segment lies on the line through O3 parallel to O1O2, and O3Tc = O3Th.」 | PAR3 | **計器の取りこぼし**: 「the line through O3 parallel to O1O2」は作図の線で、接線 ∥ O1O2 の主張ではない(v2 の PAR の `parallel to O1O2` が主語を見ない) |
| k1_1_j08(fable_r8) | 「7. Since O3 is the midpoint of O1O2, it lies on the perpendicular bisector of segment O1O2.」「Hence O3, the midpoint of O1O2, is the unique point on both the perpendicular bisector of O1O2 and on l1; but Tc and Th also lie on l1.」 | PBIS3 | **計器の取りこぼし**: PBIS3 の主語 `Tc|Th` が大文字小文字を区別せず「**th**e midpoint」の th を Th と読んだ(`\b` なし)。文の中身は退化の主張 O3 ∈ l1(olm116 の M = O3 の型) |
| k1_1_j13(opus_r3) | 「5) Therefore the projections of O1 and O2 onto l1 coincide or are symmetric about the midpoint O3. 6) Consequently O3Tc = O3Th.」 | PT | 点対称(本物・この図では偽)。「coincide or are symmetric about O3」= 退化の主張(M = O3)を対称の語で言う |

- 計器の取りこぼし 2 本を除くと OUTER_a = **2 / 40 = 0.05**(Δ −0.194)で判定は変わらない。取りこぼしの形は二つとも v4((c))で直す: PAR3 の主語(接線 / TcTh / l1 に限る)・PBIS3 の `Tc|Th` に `\b`。

## §4. 主 session の読み(L3・値と並べる・判定は変えない)

1. **足場は記憶の前提を抑える**: 設定の段(半径 ⊥ 接線・足・平行)の後では、線対称 0 / 40(意味で数えても 1 / 40)・外接線の印 2〜4 / 40、足 = 中点の段の後では全部 0。olm113 の証明の欄(足場なし・同じ図)の 0.122 / 0.244 と比べて、どちらも下がる。olm118 の「確かめない前提は記憶のまま残る」は、**前提を自分で持ち込む場面**(足場なし)の話で、段が与えられれば持ち込む余地が減る。
2. **残るのは「By symmetry」の名なし(Opus の文)と、段の語の取り違え(Fable の文)**: Opus の `n)` の文の続きは理由を「対称」で済ませ(5 / 20・軸は言わない)、Fable の `Step n (題):` の続きは段を埋めながら「O1O2 ⊥ l1」「O1O2 ∥ ThTc」を段 1〜3 から誤って導く(k1_0_j03)。退化の主張 M = O3 は点対称の語でも出る(k1_1_j13)。
3. 予想の外れ(Q1): 「対称」5 本の半分は軸を名指すと見たが、名指した本数は 0(括弧の中で O1O2 を垂直二等分線と言った 1 本を除く)。足場の後の「対称」は軸を持たない語。
4. 計器(v3)の取りこぼしを二つ見つけた(PAR3 の主語・PBIS3 の `\b`)。olm118 で見つけた PBIS3 の主語(「perpendicular from O3 to l1 is …」)と合わせて三つ。(c) の v4 の材料。olm118 の判定(Q1〜Q3)への影響は、olm118 の当たりの文を読んだ範囲では無い(olm118 §4・§6)が、v4 で当て直して確かめる。

## §5. 主張しないこと(PREREG §5 のまま)

- 続きは frontier の段の後の文で、olm113 の証明の欄(一から書いた)と文脈も長さも違う。差を「足場」だけに帰さない。
- v3 の限界(語の印・asserted の粗さ・取りこぼし 3 種)は上のとおり。
- 一つの model・一つの温度・40 + 38 本。一行 = 0.025。

## §6. 次

- (c) = v4(PBIS3 の主語・`\b`・PAR3 の主語の修正 + 本文の「口にして退けた」RETR の述語)を olm113 / olm117 / prf5 / olm116 の続きに当て直し、olm118 と この札の判定が変わらないことを確かめる(次の札・先生の「a / b / c を順に」の (c))。
- (a) = olm119(折り返しの式)は本走中(15:20 発火・約 2 時間)。
