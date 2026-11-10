HEAD(R1) = e229c00e(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm63`・凍結 2026-10-28 夜): moy-5 の本文で公開 SAE(層 32)が使える条件の較正 — 書き方(Unicode / ASCII)× 問題文の有無 × JSON の有無 × token の位置の帯

- 発注(逐語): 先生 10-28「moy-5ではSAEが有効ではない、ということでしたが、そこもできるか検証を進めたい。」
- 親: [olm60 停止](RESULT_olm60_moy5_frontier_routes_read_by_olmo_sae_STOPPED_at_C1_20261028.md)(frontier の本文・FVE 0.343)・[olm61](RESULT_olm61_moy5_olmo_continues_frontier_route_C1_stop_sae_route_read_20261028.md)(OLMo の続き・0.309)・[olm4](../2026-10-24/RESULT_olm4_commit_direction_and_public_sae_olmo3_32b_20261024.md)(OLMo 自身の moy-5 の行・0.447)。読み方 = [ADJUDICATION 10-27](../2026-10-27/ADJUDICATION_reading_rule_frozen_text_literal_20261027.md)。
- runner = [olm63_…py](../../ConstructGap/exp/olm63_moy5_sae_calibration_notation_context_position_20261028.py)。

## §0. 凍結の前に見た物(開示)
- SAE の config(`ctx_len 2048`・`BatchTopKSAE`・k 160)。
- model なしの試し(`--dry`): prf3 の問題文は token の中央値 701・読む部分の中央値 約 960・読む部分の最後の位置の最大 2,969(問題文あり)/ 2,239(なし)= 読む token の多くは 2,048 より手前。書き換え(ASCII)の後に残る非 ASCII の文字 = 52(元 1,659)。活性も FVE も見ていない。

## §1. 宇宙(`L1`)
- S0(陽性統制・forward なし): olm4 の保存の残差 `olm4/rows/base__*.npz`(OLMo 自身の moy-5 の行・group base)の生成の部分から 1 行 10 token(seed 6363)。
- S1〜S5(prf3 の 40 行・生成なし・olm4 の `forward_capture` で層 32):
  - S1 = 問題文 + 本文 raw(Unicode のまま)= olm60 と同じ形
  - S2 = 問題文 + 本文(両方を ASCII に書き換え)
  - S3 = 本文 raw だけ(問題文なし・Unicode)
  - S4 = 本文だけ(ASCII)
  - S5 = 平文(JSON をほどいた「Conjecture: … / Reason: …」・ASCII・問題文なし)
- 書き換えの表 = runner の `ASCII_MAP`(² → ^2・· → *・× → x・√ → sqrt・⊥ → perp・→ → -> ・下付きの数字 → 数字 ほか 39 組)。
- 抜き取り: 読む部分から 1 行 32 token(seed 6364)・**最初の 8 位置は全条件で除く**。
- 量: FVE(threshold で encode → decode)・L0・**位置の帯ごとの FVE**(0〜512 / 512〜1024 / 1024〜2048 / 2048〜4096 / 4096〜・64 本未満の帯は値を出さない)。

## §2. 統制(R6)
- **C1(陽性)**: S0 の FVE ≥ 0.40(olm4 = 0.447)。落ちたら S1〜S5 を走らせない。
- **C2(再現)**: S1 の FVE が olm60 の 0.3426 の ± 0.03。外れたら Q1〜Q3 を読まない(計器の経路が olm60 と違う)。
- **C3(同じ計器)**: olm7 の 1 行の読み直しで cos 最小 ≥ 0.99。

## §3. 予想(凍結・`L3`・外れてよい)
- **Q1(書き方)**: S2 − S1 ≥ +0.03(ASCII に直すと上がる)。
- **Q2(文脈)**: S3 − S1 ≥ +0.03(問題文を外すと上がる)。
- **Q3(使えるか・判定の規則)**: S2〜S5 のどれかが FVE ≥ 0.40 なら、その条件を「moy-5 の frontier の本文を SAE で読む時の条件」として以後の札に使ってよい(書き換えた本文を読む、と札に書く)。どれも届かなければ、frontier の本文の SAE の読みは使わない(方向の読み出しへ)。
- **Q4(記述・閾なし)**: 位置の帯ごとの FVE(S0〜S5)・L0・書き換えの後に残る非 ASCII の文字の数。
- **Q5(時間)**: ≤ 30 分。

## §4. 読み方・可読条件(R15)
- ADJUDICATION 10-27 を本札の凍結の文とする。Q3 の 0.40 は olm59〜61 と同じ関門(下げない)。
- Q1・Q2 の差は抜き取りの揺れを含む(1,280 本の FVE の揺れは未較正)ので、+0.03 未満の差は「書き方 / 文脈で変わる」と書かない。

## §5. 主張しないこと
- 公開 SAE 層 32 の再構成の良し悪しで、OLMo が本文を「理解する」かは言わない。書き換えた本文を読む条件で FVE が戻っても、元の本文の活性を読んだことにはならない。

## §6. 費用(R14)
- S0 は forward なし。S1〜S5 = 200 forward(各 1〜3 千 token)+ C3 の 1 本 + SAE の全辞書の encode 約 7,700 本 ≈ 15〜25 分。API なし。
