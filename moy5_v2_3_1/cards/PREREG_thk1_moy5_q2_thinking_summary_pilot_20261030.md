HEAD(R1) = f9cf6eb2(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `thk1`・凍結 2026-10-30 夜): moy-5 — Opus 5.5 / Fable 5.1 の思考の要約(`display: "summarized"`)は返るか・要約は生の思考より短いか・答えに相似の道が在る行で要約にも相似の語が在るか(P2-1' の下見)

- 発注(逐語): 先生 10-30 夜「2 P2-1から再開」→(P2-1 の前提 = 思考の本文は取れない・`p21_prep/MEMO_p21_thinking_text_availability_20261030.md`)→「1 P2-1'の下見をする」→「agent sdkは入れてください。」。
- G10 の欄: 比べる物 = 「要約の中の道の語」/「答えの道」 / 計器 = 要約の文と答えの文に当てる neq6 の道の正規表現(SIM = 相似・比例中項・FD = 焦点・準線)と、要約の字数 ÷ 思考の token / 雛形 = いいえ
- runner = [thk1_…py](../../ConstructGap/exp/thk1_moy5_q2_thinking_summary_pilot_20261030.py)。経路 = **agent_sdk**(claude-agent-sdk 0.2.175・同梱の CLI 2.1.314・`--thinking adaptive --thinking-display summarized`)。
  - neq3 / neq6 と同じ option: `--setting-sources local`・MCP なし・`--disallowedTools` は neq3 の DISALLOW・session を残さない。
  - 認証 = claude.ai(subscription)。各行に `apiKeySource` を記録し、`none` でなければ止める(10 月の API の上限の柵)。
- 柵: API の鍵を使わない・forward なし・Wolfram なし。草稿 = `p21_prep/DRAFT_PREREG_thk1_summary_pilot_20261030.md`(md5 `a2f759ba…`・この版で置き換える)。

## 0. 凍結の前に見た物(開示)

- neq3〜neq6(A/Q2・xhigh ほか): 答えに比例中項 = Fable 99 / 100・Opus 36 / 100。Opus の残りは焦点・準線の道(neq6 の runner の頭の注)。
- 思考の本文は手元に無い(MEMO #1・#2)。API は生の思考の本文を返さず、`display: "summarized"` で要約を返す(MEMO #4)。
- **研究と無関係の問題での下見(10-30 夜)**:
  - Pell 方程式(Opus 5.5・effort high・Agent SDK)= 要約 409 字・思考の token 303(= 1.35 字 / token)。英語・一人称(「I'm checking …」)。
  - `17*23+19*21`(runner の呼び出しの道の通し・Opus 5.5・xhigh)= 要約 57 字・思考の token 20。
  - `claude -p`(既定の表示)では要約は空(MEMO #5)。
- moy-5 の A/Q2 で要約を見たことは無い。

## 1. 問い(全部 記述・n 4 / 4 = 判定に上げない)

- Q1: 要約(thinking の block の文字列)は空でないか。
- Q2: 要約の字数 ÷ 思考の token の中央値は 2 より小さいか。英語の生の文なら 1 token ≈ 4 字 = その半分より短い = 要約の目安(文書は「要約」としか書かない)。
- Q3: 答えに SIM(相似・比例中項)の道が在る行で、要約にも SIM の語が在るか(在れば、要約の中の最初の SIM の位置 = 百分位)。
  - 返答では要約の block が答えの block より前に並ぶので、「要約の中の SIM が答えより前か」は作りの上で常に真 = 問いにしない。

## 2. 腕と行

- prompt = neq3 の A/Q2(md5 `123ea1ac`・そのまま・`R3.PROMPT["A/Q2"]`)。
- effort = xhigh(neq3 と同じ)。
- model = claude-opus-5-5・claude-fable-5-1、各 4 回(計 8 回)。
- 返答の content の全部の block(thinking の文字列を含む)を、行の file `ConstructGap/exp/results_thk1_moy5_20261030_<model>.jsonl` に写す。

## 3. 予想(確率は 0〜1)

| Q | 予想 | p | 解ける条件 |
|---|---|---|---|
| Q1 | 8 / 8 で空でない | 0.85 | 空の行が 1 つでも在れば偽 |
| Q2 | 中央値 < 2 字 / token | 0.70 | 8 行の中央値で決まる |
| Q3 | 答えに SIM の在る行の過半で、要約にも SIM が在る | 0.60 | 答えに SIM の在る行が 0 なら解けない |

- 根: Pell の下見で要約は返った(1.35 字 / token)。moy-5 は長い問いで思考も長い(neq3 の出力 token の中央値 Opus 2,302・Fable 4,674)。要約は一人称の作業の記述で、道の名(similar triangles など)を書くかは見ていない。

## 4. 止める規則

- `stop_reason: "refusal"`(`reasoning_extraction` ほか)が 1 回でも出たら止めて、記述だけ書く。
- `apiKeySource` が `none` でない行が出たら止める(API の請求に乗ったことになる・最大 1 回分)。
- 要約が 8 回とも空なら、P2-1' は行わないと書いて閉じる(① 答えが出た)。

## 5. 言えないこと

- 要約は思考そのものではない。要約を誰がどう書くかは文書に無い。
- 「cut に導いた道」は言えない。言えるのは「要約の文の中で道の語が出るか・どこで出るか」まで。
- 経路(Agent SDK・CLI 2.1.314)は neq3(10-19 の CLI)と版が違う。答えの道の率を neq3 と比べて言わない(n 4)。

## 6. 走らせ方

```
cd ConstructGap
python3 -I exp/thk1_moy5_q2_thinking_summary_pilot_20261030.py --dry                                              # 合成(凍結の前に通した・11 / 11)
python3 -I exp/thk1_moy5_q2_thinking_summary_pilot_20261030.py --fire --backend agent_sdk --model claude-opus-5-5 --n 4
python3 -I exp/thk1_moy5_q2_thinking_summary_pilot_20261030.py --fire --backend agent_sdk --model claude-fable-5-1 --n 4
python3 -I exp/thk1_moy5_q2_thinking_summary_pilot_20261030.py --read
```
