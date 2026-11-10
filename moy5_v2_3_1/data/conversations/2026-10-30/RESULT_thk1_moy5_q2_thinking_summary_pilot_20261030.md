HEAD(R1) = edd7a0be(発火の時の HEAD = 凍結 f2ccf1be + 台帳の一行・dirty なし)

# RESULT(札 `thk1`・2026-10-30 夜・MacBook): 止める規則 §4 で各 model 1 行で止まった — Agent SDK の CLI が API の鍵で呼んだ(runner が import した `ConstructGap/models.py` が鍵を process の環境に書き込んだ)・要約は 2 行とも返った(記述)

- 凍結 = [PREREG](PREREG_thk1_moy5_q2_thinking_summary_pilot_20261030.md)(f2ccf1be)・runner = `ConstructGap/exp/thk1_moy5_q2_thinking_summary_pilot_20261030.py`。
- 出力 = `ConstructGap/exp/results_thk1_moy5_20261030_claude-opus-5-5.jsonl`・`…_claude-fable-5-1.jsonl`(各 1 行)・発火の log `/private/tmp/claude-501/thk1_run/fire_*.log`(21:35:15〜21:36:56)。

## 何が起きたか

- 各 model の最初の行の `apiKeySource` = **`ANTHROPIC_API_KEY`**。§4「`apiKeySource` が `none` でない行が出たら止める」で、2 本とも 1 行目の後に止まった(exit 1)。
- 原因(10-30 夜に確かめた):
  - runner は問いの文を読むために neq3 の module を import する。その連鎖で `ConstructGap/models.py` が import される。
  - `models.py` の `_load_keys()`(39〜50 行)は、`~/.config/reverse_turing/keys.env` の鍵を `os.environ` に書き込む(import の前 `ANTHROPIC_API_KEY` なし → 後 あり)。
  - Agent SDK は `os.environ` を CLI に受け継がせるので、同梱の CLI 2.1.314 は API の鍵で呼んだ。
  - 鍵の無い process から SDK を呼んだ確かめ(Haiku・研究と無関係)では `apiKeySource = none` だった。
- **API の請求に乗った = 2 行**(CLI の見積もり: Opus 0.071 USD・Fable 0.432 USD)。加えて、凍結の前の呼び出しの道の通し(`17*23+19*21`・Opus)1 回も、同じ import の後だったので API に乗った見込み(CLI の見積もり 0.002 USD)。
- 10 月の `claude -p` の走行(neq2〜neq6・prf1〜3 など)は、同じ module を import していたが、API の請求に乗っていない。`est_usd` の計(10-19 = 173 USD・10-21 = 146 USD)が、Console の棒(約 10 USD・ほぼ 0)に表れていない。系の `claude` は環境の鍵を使わず、SDK の同梱の CLI は使った、という違いになる(L3 = 二つの経路の観察からの読み)。

## 2 行の記述(判定しない・n 1 / 1)

| model | 思考の token | 要約の字数 | 字 / token | 答えの SIM の語 | 答えの FD の語 | 要約の SIM の語 | 要約の FD の語 |
|---|---:|---:|---:|---|---|---|---|
| Opus 5.5 | 2,724 | 2,762 | 1.01 | なし | あり | なし | あり |
| Fable 5.1 | 7,704 | 8,342 | 1.08 | なし | あり | あり | あり |

- 要約は 2 行とも返った。英語・一人称(Opus「I need to work out where P_y traces …」・Fable「I'm working through the geometry …」)。
- **計器の弱さ(見つかった事)**: 二つの答えは、どちらも「FP_x² = FV·FP_y」(FP_x は FV と FP_y の比例中項 = cut の関係)を書いている。この札の答えの印(SIM = similar・mean proportional などの語の正規表現)はそれを拾わない。neq の正式の採点器(`N.score` の `cut_in_conjecture` = 関係の式の reader v2)が、この問いの答えの印。
- 要約の中身の読み(cut の関係の式が要約に在るか)は、次の札の予想を見ないで凍結するため、ここでは行わない。

## 判定

- Q1〜Q3 は判定しない(§4 で止まった・n 1 / 1)。
- 次の札 `thk2` = 同じ問い・同じ経路。直す点は二つ。
  1. Agent SDK を呼ぶ前に、環境から `ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN` を外す。
  2. 答えの印を neq の採点器(`cut_in_conjecture`)にし、要約にも同じ reader の関係の式(`RR2.relations`)を当てる。
- `thk1` の 2 行は `thk2` の数に入れない(経路の認証と答えの印が違う)。
