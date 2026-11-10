# RESULT(札 `neq3`): 問いの点の集合 × 補助定理 XIV(名 / 本文)— 問いを cut の点に向けると答えの欄に cut が入る(Fable は何も足さずに 20 / 20・Opus は名か本文で 7 → 20)(2026-10-19・実行層)

- 札 = [PREREG neq3](PREREG_neq3_moy5_lemma14_question_set_2x2_opus_fable_xhigh_20261019.md)(凍結 `226271c4`)。書いた時の HEAD = `8a63bedc`(fetch 済み・origin の先 8・遅れ 0・`R1`)。
- 走行 = zebrashark・Claude Code 2.1.292・`claude -p`・effort xhigh・20:43:29 → 21:18:44。新しく引いたのは 210 本(Opus 140・Fable 70)で、誤り 0・permission の拒否 0。init の model は全行が指定どおり。
  - 費用 = Claude Code の枠。API の単価での換算は Opus $21.33・Fable $21.09(見込み $90 の半分以下)。
  - Opus の 3 本(K r7・A r1・A r16)は 2 turn・出力 13 万 token・約 880 s。neq2 の 860〜890 s の一本と同じ型で、3 本とも答えは Q1 の等長。
- 出力 = `ConstructGap/exp/results_neq3_moy5_20261019_claude-opus-5-5.jsonl`(md5 `b49fcad2`)・`…_claude-fable-5-1.jsonl`(md5 `8585a2a8`)。Fable の Q1 は neq2f の出力(md5 `f54d5897`)を runner が読んだ。
- 腕を伏せた読みの材料 = [data_neq3_reasonread/](data_neq3_reasonread/)。答えの欄 120 本の伏せた一覧 `f57ed1a6`・FV の固定の候補 `4a66bd4b`・鍵 `ffdc8bab`・分類 `ee1c8c37`(分類は伏せを解く前に書いた)。
- **身分**: §1 = 計器の写し(`L1`)。§2 = 腕と model を伏せた読み(逐語 = `L1`・分類 = `L3`)。§3 = 予想の当たり外れ。§4 = 記述(判定にしない)。§5 = 読み(`L3`・採否は先生)。

## §1. 関門・表・判定
- 読み取り器 v2 の較正 72 / 72。関門: Opus K 9 / 10・K/Q2 10 / 10、Fable K/Q2 10 / 10(K は neq2f の 9 / 10)→ 全部通過。

答えの欄の cut(主)/ 答え全体の bind / 答えの欄の等長 / 答えの欄の放物線(n = K 10・ほか 20):

| 腕 | Opus 5.5 | Fable 5.1 |
|---|---|---|
| K(Q1) | 6 / 9 / 9 / 0 | 7 / 9 / 9 / 0 |
| A(Q1) | **0** / 0 / 17 / 1 | **0** / 0 / 20 / 0 |
| L-name(Q1) | **0** / 0 / 19 / 1 | **0** / 7 / 20 / 9 |
| L-text(Q1) | **0** / 0 / 20 / 1 | **0** / 0 / 20 / 7 |
| K/Q2 | 10 / 10 / 1 / 4 | 10 / 10 / 0 / 0 |
| A/Q2 | **7** / 7 / 4 / **20** | **20** / 20 / 0 / 5 |
| L-name/Q2 | **20** / 20 / 0 / 2 | **20** / 20 / 0 / 0 |
| L-text/Q2 | **20** / 20 / 0 / 0 | **20** / 20 / 0 / 1 |

**判定(凍結の規則のまま・launcher の出力の逐語)**
- Opus 5.5: `QSET YES: A/Q2 7 vs A 0` / `NAME@Q2 YES: L-name/Q2 20 vs A/Q2 7` / `TEXT@Q2 YES: L-text/Q2 20 vs A/Q2 7` / `NAME×QSET YES … = 13` / `TEXT×QSET YES … = 13`
- Fable 5.1: `QSET YES: A/Q2 20 vs A 0` / `Q2 CEILING: A/Q2 = 20 >= 17; the name / text effect on Q2 is not measured` / `NAME×QSET NO … = 0` / `TEXT×QSET NO … = 0`
  - Fable の交互作用が NO なのは、A/Q2 が天井 20 で差が 0 になるため。効き目が無いという意味ではない。

## §2. 伏せた読み(Q2 の 3 腕 × 2 model = 120 本・答えの欄)
- 手順: 種 20261019 で混ぜ、Y001〜Y120 の名で答えの欄だけを並べた(model・腕・回は鍵の file へ)。分類を file に書いてから鍵を開けた。
- 分類(`L3`): **C** = cut(比例中項・FP_x² = FV·FP_y・相似 △FVP_x ∼ △FP_xP_y・角の二等分の言い換えを含む)/ **CP** = cut と「P_y は焦点 F・頂点 V の放物線の上」を両方 / **P** = 放物線だけ。

| | C | CP | P |
|---|---|---|---|
| Opus A/Q2 | 0 | 7 | **13** |
| Opus L-name/Q2 | 18 | 2 | 0 |
| Opus L-text/Q2 | 20 | 0 | 0 |
| Fable A/Q2 | 15 | 5 | 0 |
| Fable L-name/Q2 | 20 | 0 | 0 |
| Fable L-text/Q2 | 20 | 0 | 0 |

- 目の分類の P(13 本)は、読み取り器が cut を読まなかった 13 本と一致した。目の放物線は 27 本、読み取り器は 28 本。差の 1 本は「focal distances」の語に当たっただけの C。
- 自明な直角(∠FVP_x・∠FP_xP_y = 90°)だけを答えた行は 0。直角は相似の理由として書かれた。
- Opus A/Q2 r16(P)は答えの欄に「P_yF = dist(P_y, e) = |FV| + |VP_x|²/|FV|」と書いた。これは FV·FP_y = FV² + VP_x² = FP_x² = 足し算の形の cut。読み取り器は ADDITIVE に分けたので cut に数えていない。同じ行は「軸は F を通り j に垂直」とも書いた(誤り・軸は j)。
- **FV の固定**(先生の問い): 候補 4 本のうち、目で裁いて **2 本**。2 本とも **L-text/Q2**(本文あり × 問いを cut の点へ)で、model は一つずつ。どちらも系 2 を問いの字に写したもの。
  - Opus L-text/Q2 r13: 「The lemma gives PS : SN = SN : SA, which here is FP_y : FP_x = FP_x : FV. … Equivalently (Cor. 2), FP_x² is proportional to FP_y because FV is fixed.」
  - Fable L-text/Q2 r8: 「Corollary: |FP_x|^2 is proportional to |FP_y| as P_x varies on h1, since |FV| is fixed.」
  - 外した 2 本(Fable A/Q2 r13・r17)は「FP_x² = FV·FP_y, independent of the choice of P_x on h1」= 関係が P_x によらないと言っただけ。

## §3. 予想(PREREG §6)の当たり外れ
- P1(QSET は両 model で YES)= **当たり**。
- P2(Fable は Q2 CEILING になりうる)= **当たり**(20 / 20)。
- P3(名は答えを放物線に寄せ、cut を減らす)= **外れ・逆向き**。Opus は何も足さないと答えが放物線(20 / 20 = P 13・CP 7)で、名を足すと cut 20 / 20・放物線 2 になった。
- P4(TEXT×QSET)= Opus で YES(13)。Fable は天井のため測れない。

## §4. 記述(判定にしない)
- **Opus の Q1(xhigh・zebrashark)と neq2(high・MacBook)**: 答えの欄の cut は 0 のまま(3 腕とも)。bind も 0(neq2 の L-text 1 → 0)。名の腕で放物線を口にしたのは 6 / 20(neq2 は 7 / 20)。
  - 同じ effort・同じ機械で Fable は 20 / 20・bind 7。neq2f で見た名の腕の差(放物線の同定・cut を理由の欄に書く)は、effort と機械ではなく model の側にある。
  - neq2 の (c) の型(補助定理 XIV が等長を生むと結ぶ)は、Opus の xhigh でも名の腕に出た。逐語で確かめたのは 2 本(r2「By the mean-proportional relation of Lemma XIV, the offset … are tied to FV … carries this length onto g」・r19「as in Newton's Lemma XIV parabola construction, where the tangent and the parallels to the chord carry equal segments」)。全数の分類はしていない。

## §5. 読み(`L3`・採否は先生)
1. **答えの欄を決めるのは問いの点の集合**。Q1 では 2 model × 3 腕 × 20 = 120 本のすべてで答えの欄に cut が 0(名・本文があっても)。Q2 では何も足さなくても Opus 7・Fable 20。neq2 / neq2f の読み(cut は {E, J, K, P_y} に入らないので答えの欄に居場所が無い)は、問いを替えた側から確かめられた。
2. **Fable は、問いが cut の点を指せば、名も本文も無しに比例中項を答えに選ぶ**(20 / 20)。Opus は同じ問いで、同じ事実を**軌跡(放物線)として答える**(20 / 20)。7 本は比例中項も添えた。
3. **Opus では、名か本文が「どちらを主張にするか」を比例中項の側に倒した**(7 → 20・放物線 20 → 2 / 0)。記録した読み(名は看板の中身を引く)と同じ向き。補助定理 XIV の看板は比例中項で、Q2 ではそれが答えの点の集合に入る。ただし Q2 では看板の中身と証明に要る部分が同じなので、この札は名と本文の差を分けない(どちらも 20)。
4. **FV の固定を言葉で書いた最初の 2 本は、本文(系 2)を見て、かつ問いが cut の点を指した時だけに出た**(L-text/Q2 の 40 本中 2 本)。neq3 で新しく引いた残りの 170 本では 0(伏せた外の候補 2 本 = Opus L-text r1「KP_y is fixed …」・Fable K/Q2 r7「The relation is independent …」は目で外した)。neq2 / neq2f の 140 本でも 0。「SA は与えられている」の言葉は、本文を写すことで、ごく稀に出る。
5. Fable 5.5 との比較に向けて: Fable 5.1 は Q2 で天井。5.5 で差が出うるのは、Q1 の名の腕(bind 7 / 20・放物線 20 / 20)、答えの型(比例中項か軌跡か)、FV の固定の言葉。

## §6. 主張しないこと
- Q2 は問いを替えた別の項目。一つの作図・一つの本文。
- 放物線の答え(P)は誤りではない(P_y の軌跡は実際に焦点 F・頂点 V の放物線)。判定の物差しが cut を数えるので、P は cut 0 に入る。
- 費用は Claude Code の枠で、換算は参考。
