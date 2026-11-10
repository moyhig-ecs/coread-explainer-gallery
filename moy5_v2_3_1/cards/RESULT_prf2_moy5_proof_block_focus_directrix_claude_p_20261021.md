# RESULT(札 `prf2`): 焦点・準線の道を塞ぐと、Opus は 10 本中 9 本、Fable は 10 本中 5 本が**頂点の比例中項(Menaechmus の格子)を自分で持ち出して** P_y の式まで束ねた(事後の読み)。凍結の主(LAT_ROUTE)は**計器の欠陥で全部 0**(FD の述語が「使わずに」という言及まで数えた)

- 札 = [PREREG](PREREG_prf2_moy5_proof_block_focus_directrix_claude_p_20261021.md)(凍結 `e8efe2a3`)。書いた時の HEAD = `947b875a`(`R1`・fetch 済・origin と同じ)。
- 走行 = MacBook・Claude Code 2.1.299・`claude -p`・effort max・workers 4。40 本とも ok・err 0・**実際の tool の呼び出し 0**。wall の中央値 265 s・最長 1005 s。見積りの費用は Opus 18.2・Fable 32.5 USD 相当(購読の経路)。
- 出力 = `ConstructGap/exp/results_prf2_20261021.jsonl`(md5 `aedb9fec`)・R1 = `results_prf2_20261021_r1_prf1_order.jsonl`(`6f0cf681`)。
- 事後の読み(凍結の述語ではない)の script = `ConstructGap/exp/prf2_posthoc_route_split_20261021.py`(md5 `cf4f56da`)・出力 = [data_prf2_posthoc/](data_prf2_posthoc/posthoc_route_split_output_20261021.txt)(`b8f1302e`)。
- 身分: §1〜§3 = `L1`(凍結の述語の実出力)/ §4 = 予想の当たり外れ / §5 = **事後の読み**(数は機械の分割の実出力・分け方を決めたのは prf2 の出力を見た後)/ §6 = `L3`。

## §1. 統制
- **gate**(P5BK の LATX ≥ 8 / 10): Opus 10・Fable 8 = 通過。
- guard と較正: 凍結の commit と一致・ORDER 6 + MALFORMED 3 + prf1 の 29 の較正が通過。
- 壊れた出力(MALFORMED)= Fable 4 本(P5B r8・P5BK r1・r2・r6)。どれも JSON の答えが無く、3 本は tool の呼び出しの書式(`<invoke`)を本文に書いた(prf1 §1 と同じ型)。Opus は 0。

## §2. 凍結の述語の結果(各 n 10・`L1`)

| model | 腕 | cut3 | END | LATX | CHAIN | ORDER | FD | **LAT_ROUTE(主)** | PB_WORD | floor | MALFORMED |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Opus 5.5 | P5B | 10 | 10 | 6 | 6 | 5 | 10 | **0** | 7 | 10 | 0 |
| Opus 5.5 | P5BK | 10 | 9 | 10 | 9 | 7 | 10 | **0** | 9 | 10 | 0 |
| Fable 5.1 | P5B | 9 | 9 | 1 | 1 | 1 | 9 | **0** | 4 | 9 | 1 |
| Fable 5.1 | P5BK | 8 | 6 | 8 | 6 | 3 | 8 | **0** | 3 | 7 | 3 |

- 道: Opus P5B = CHAIN 6・END-only 4 / Opus P5BK = CHAIN 9・LAT-only 1 / Fable P5B = END-only 8・CHAIN 1・none 1 / Fable P5BK = CHAIN 6・none 2・LAT-only 2。
- R1(prf1 の 40 行の ORDER): P5K の CHAIN の行で ORDER が成り立つのは Opus 10 / 10・Fable 9 / 9。多くは渡された hint を 1 文目前後で言い直しているので、中身なしに成り立つ。prf1 の Opus P5 r2 は補助点 Q の相似が読み取り器に読めず、ORDER 不成立。

## §3. 計器の欠陥(`L1`)
- **FD の述語は「書いたか」を数え、否定の言及も拾った。** FD の立った文を全部抜き出すと(事後の script):
  - P5B: 否定の言及(「Parabola proof (not using P_yF = P_yK …)」型)が Opus 10 文・Fable 13 文。
  - END より後の系・数値の確かめ(「Corollary (not used above): … so P_yF = HD = EJ = P_yK」)が Fable 2 文。
  - **END より前で否定でない FD の文**は Opus 0 行・Fable 1 行(r9「The same chain gives EJ = P_yF as well.」= 不変量の節)。
- P5BK で END より前の FD の文がある 5 行(Opus r1・r2・r5・r6・r9)は、どれも前半の「不変量の理由」の節で、渡された比例中項を床につなぐ式(「EJ = KP_y = FP_y = FP_x²/FV」)。放物線の節はどの行も「(using neither P_yF = P_yK nor …)」と宣言して始まる(本文の逐語)。
- ⇒ LAT_ROUTE = CHAIN ∧ ¬FD は、塞ぎの文に従った行ほど 0 になる形だった。PREREG §5 に書いた限界がそのまま主の数を消した。⑤ の較正(29 項)に「否定の言及」の陰性統制を入れていなかった(`R6` の不足)。

## §4. 予想(PREREG §3)の当たり外れ(凍結の述語の数で)
- **Q1**(P5B の FD ≤ 3)= **外れ**(Opus 10・Fable 9)。数の中身は §3 のとおり言及。
- **Q2**(P5B の LATX ≥ prf1 P5 + 3)= Opus **当たり**(6 ≥ 5)・Fable **外れ**(1 < 3)。
- **Q3**(P5B の LAT_ROUTE: Opus ≥ 3・Fable ≥ 1)= **外れ**(0・0)。§3 の欠陥による。
- **Q4**(P5BK の LAT_ROUTE ≥ 7)= **外れ**(0・0)。§3 の欠陥による。PREREG §4 の約束どおり、Q4 が外れた以上、P5B の低い LAT_ROUTE を「格子を持ち出せない」とは読まない。
- **Q5**(R1・ORDER)= **当たり**(Opus 10 / 10・Fable 9 / 9)。

## §5. 事後の読み(凍結の述語ではない・prf2 の出力を見た後に分け方を決めた)
凍結の END は縦の類に VP_x を含むので、**頂点の比例中項 `VP_x² = FV·VH`(Menaechmus の格子)が END の側に入り、LATX に数わらない**(prf1 RESULT §6 の限界)。END を縦の類の線分で二つに分けた: VMP = VP_x を含む(頂点の比例中項)/ SYM_Py = HP_y か DK を含む(P_y の式)。

| 札・腕 | Opus: VMP | Opus: **VMP ∧ SYM_Py** | Fable: VMP | Fable: **VMP ∧ SYM_Py** |
|---|---|---|---|---|
| prf1 P5(塞がない) | 2 | **2** | 1 | **0** |
| **prf2 P5B(焦点・準線を塞ぐ)** | 10 | **9** | 5 | **5** |
| prf1 P5K(比例中項を渡す) | 8 | 6 | 5 | 5 |
| prf2 P5BK(塞いで渡す) | 8 | 8 | 6 | 6 |

- 「何かの格子(VMP・焦点の比例中項・相似)から P_y の式へ束ねた」行: prf1 P5 = Opus 2・Fable 0 → **prf2 P5B = Opus 9・Fable 5**(Fable の P5B の実質の答えは 9 本)。
- 道の中身(本文の逐語・`L1`):
  - Fable P5B r4: "by the altitude (geometric mean) theorem VP_x^2 = FV*VM" → 相似で MH / MV = HP_y / VP_x → 式。
  - Opus P5B r1: "Hence VH/VP_x = tan(angle P_xFV) = VP_x/FV, so VP_x^2 = FV*VH" → "(4) Therefore P_yH^2 = 4*VP_x^2 = 4*FV*VH"。
  - 共通の前段 = 中線(切片)の定理で DK = 2·VP_x → 長方形で HP_y = DK。
- 読み(`L3`): 近道(焦点・準線)が開いていると格子は通らない(prf1)。塞ぐと、Opus はほぼ全部・Fable は半分が、頂点の比例中項を自分で持ち出し、式まで束ねて証明を閉じた。**moy-5 の壁は「束ねられない」でも「格子を持ち出せない」でもなく、近道がある時に格子を選ばない(満足停止)**と読める。moy-1 の closure-forcing(楽な出口を塞ぐと束縛が出る)と同じ型。
- ⚠ これは事後の分け方で、確かめの札ではない。

## §6. 次の候補(先生の判断)
1. **確かめの札(prf3)**: 事後の二つの直しを凍結してから、新しい生成で確かめる。
   - FD の述語に否定の言及の除外と、陰性統制の較正(「without using P_yF = P_yK」= FD でない)を足す。
   - END を VMP / SYM_Py に分け、主 = 「格子(VMP・焦点の比例中項・相似)∧ SYM_Py ∧ 放物線の節に否定でない FD が無い」にする。
   - 腕 = P5B の再現(新しい n 10)+ P5(塞がない)の再現。
2. 読み直しだけの札として、R0(既存の 1275 行)にも VMP / SYM_Py の分割を掛ける(記述)。
