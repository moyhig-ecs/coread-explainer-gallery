HEAD(R1) = 09ca2035(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `thk2`・凍結 2026-10-30 夜): moy-5 — Opus 5.5 / Fable 5.1 の思考の要約は返るか・要約は生の思考より短いか・答えに cut の関係が在る行で要約にも cut の関係の式が在るか(P2-1' の下見・thk1 の走らせ直し)

- 発注(逐語): 先生 10-30 夜「1 P2-1'の下見をする」「agent sdkは入れてください。」。thk1 は止める規則 §4 で止まった(`RESULT_thk1_moy5_q2_thinking_summary_pilot_20261030.md`)= この札はその直しの走らせ直し。
- G10 の欄: 比べる物 = 「要約の中の cut の関係」/「答えの cut の関係」 / 計器 = neq の reader v2(答え = N.score の cut_in_conjecture・要約 = RR2.relations の CUT / SIM-CUT)と、要約の字数 ÷ 思考の token / 雛形 = いいえ
- runner = [thk2_…py](../../ConstructGap/exp/thk2_moy5_q2_thinking_summary_pilot_20261030.py)(thk1 の runner の写しに二点の直し)。
  1. Agent SDK を呼ぶ前に、環境から `ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN` を外す(`models.py` の `_load_keys` が import の時に書き込むため)。
  2. 答えの印を neq の採点器(`N.score` の `cut_in_conjecture`)にし、要約にも同じ reader の `RR2.relations` を当てる。SIM / FD の語は記述で残す。
- 経路・option・問い・model・effort・n は thk1 と同じ: Agent SDK(0.2.175・CLI 2.1.314)・`--thinking-display summarized`・neq3 の A/Q2(md5 `123ea1ac`)・xhigh・各 4 回・`--setting-sources local`・MCP なし・neq3 の DISALLOW。
- 柵: 各行の `apiKeySource` を記録し、`none` でなければ止める。

## 0. 凍結の前に見た物(開示)

- thk1 の 2 行(API の鍵で呼ばれた・この札の数に入れない)の記述:
  - 要約は 2 行とも返った。思考の token・要約の字数 = Opus 2,724・2,762 / Fable 7,704・8,342(字 / token = 1.01・1.08)。
  - 二つの答えは、目で見て、どちらも「FP_x² = FV·FP_y」を含む。
  - 要約は頭の 300 字だけを見た。**要約に RR2 を当てた値は見ていない**。
- 自己検査の陽性統制 = thk1 の Opus の答え(`ConstructGap/exp/thk2_selftest_positive_answer_from_thk1_opus.txt`)→ `cut_in_conjecture` = True。陰性(焦点・準線だけの答え)→ False。要約の式つきの文 → CUT・式なしの文 → なし。
- Pell 方程式の下見(研究と無関係)= 1.35 字 / token。

## 1. 問い(全部 記述・n 4 / 4 = 判定に上げない)

- Q1: 要約は空でないか。
- Q2: 要約の字数 ÷ 思考の token の中央値は 2 より小さいか(英語の生の文なら 1 token ≈ 4 字)。
- Q3: 答えに cut の関係が在る行(`ans_cut`)で、要約にも cut の関係の式(`summ_cut`)が在るか。
- 記述: model ごとの `ans_cut`・`summ_cut`・SIM / FD の語・要約の中の最初の SIM の位置。

## 2. 予想(確率は 0〜1)

| Q | 予想 | p | 解ける条件 |
|---|---|---|---|
| Q1 | 8 / 8 で空でない | 0.90 | 空の行が 1 つでも在れば偽 |
| Q2 | 中央値 < 2 字 / token | 0.90 | 8 行の中央値(thk1 の 2 行を見た後の予想 = 開示) |
| Q3 | `ans_cut` の行の過半で `summ_cut` も在る | 0.50 | `ans_cut` の行が 0 なら解けない |

- 根: 要約は散文の一人称の作業の記述で、式を書き写すかは見ていない(thk1 の要約の頭 300 字には式が無かった)。

## 3. 止める規則

- `stop_reason: "refusal"` が 1 回でも出たら止める。
- `apiKeySource` が `none` でない行が出たら止める。
- 要約が 8 回とも空なら P2-1' は行わないと書いて閉じる。

## 4. 言えないこと

- 要約は思考そのものではない。要約を誰がどう書くかは文書に無い。「cut に導いた道」は言えない。
- `summ_cut` は「要約の文に cut の関係の式が書かれたか」で、思考の中で cut に着いた時点ではない。
- 経路(CLI 2.1.314)は neq3 と版が違う。答えの cut の率を neq3 と比べて言わない(n 4)。

## 5. 走らせ方

```
cd ConstructGap
python3 -I exp/thk2_moy5_q2_thinking_summary_pilot_20261030.py --dry          # 合成 + 陽性 / 陰性(凍結の前に通した・16 / 16)
python3 -I exp/thk2_moy5_q2_thinking_summary_pilot_20261030.py --fire --backend agent_sdk --model claude-opus-5-5 --n 4
python3 -I exp/thk2_moy5_q2_thinking_summary_pilot_20261030.py --fire --backend agent_sdk --model claude-fable-5-1 --n 4
python3 -I exp/thk2_moy5_q2_thinking_summary_pilot_20261030.py --read
```
