# PREREG(札 `olm3`): 候補 b = 事後学習済み Olmo-3-32B-Think を moy-5 の screen(K 10 + none/Q1 20)に当てる — 二経路(B1 = bf16 を MLX で・推奨 / B2 = ollama の Q4_K_M)(2026-10-22 夕・実行層)

> **先生(10-22 夕・逐語)**: 「olmoは推奨の経路で。両方でもいいです。」(実行層の推奨 = bf16 を MLX で = a / c と同じ数値の経路。両方取る)
> **HEAD**(`R1`): `61dc54de`(origin の先・push 待ち)。**凍結の実体**: 本書・runner [`ConstructGap/exp/olm3_moy5_olmo3_32b_think_bf16_mlx_and_ollama_q4_screen_20261022.py`](../../ConstructGap/exp/olm3_moy5_olmo3_32b_think_bf16_mlx_and_ollama_q4_screen_20261022.py) を一つの commit に。prompt・seed の式・読み取り器は olm1 の runner(`a3eee055`)経由で mnw1(`2c685fb2`)から import。
> **身分**: §0 = 開示。§1〜§2 = 凍結の設計・読み方。§3 = 予想(発火の前)。採否と決め台詞は先生。

## §0. 開示(`L1`)
- bf16 の重み(`allenai/Olmo-3-32B-Think`・safetensors 14 shard・64.5 GB)は 10-22 18:5x に取り寄せを開始(HF cache・log = `ConstructGap/exp/logs/olm3_download_20261022.out`)。小物(config・tokenizer・`chat_template.jinja`)は先に取得済。
- chat template(逐語の要点): system が無ければ「You are a helpful AI assistant.」を補い、user の後に **`<|im_start|>assistant\n<think>`** を付けて生成を始める = model は `<think>…</think>` の後に答えを書く。
- ollama の `olmo-3:32b-np16384`(Q4_K_M・context 65536・capabilities completion + thinking・Modelfile の temperature 0.6 / top_p 0.95・先生が 10-16 頃に num_predict 16384 で作った版)が手元に在る。07-28 の screen(`olmo-3:32b`)は moy-1 で open stuck 9 / 9。
- olm1 / olm2 と違う所 = **chat template あり・事後学習済み・温度 0.6 / top_p 0.95(model card = Modelfile の既定)・max_new 16384**。raw prompt でない理由 = 事後学習済み model の意図された入口で測るため(base の lens の条件とは別の問い)。

## §1. 宇宙
1. **B1**(推奨): `allenai/Olmo-3-32B-Think` bf16 を mlx_lm で読み(olm1 / olm2 と同じ数値の経路)、model 自身の chat template で prompt を描画(user = mnw1 の prompt そのまま・md5 は olm1 経由で assert)、`batch_generate`・batch 5・温度 0.6 / top_p 0.95・max_new 16384。seed = olm1 の `seed_of(arm,'natural')` + 100000 + 1000 × sub-batch。
2. **B2**: ollama `olmo-3:32b-np16384`(Q4_K_M)の `/api/chat`・`think: true`・温度 0.6 / top_p 0.95・`num_predict` 16384(ollama は max_completion_tokens を無視する = 10-14 の記録)・一本ずつ・seed = B1 の sub-batch の seed + 行の番号。raw = `<think>` + thinking + `</think>` + content。
3. 腕 = K(n 10)・none/Q1(n 20)。prompt は mnw1 と byte 一致。
4. 読み取り器 = mnw1 v2(CAL は guard で毎回)。欄 = cut(本文)・cut(答え)・床・打ち切り・**`</think>` が閉じたか**・thinking の token 数(B1)。

## §2. 読み方
- 関門は置かない(測定)。比較表の行 = Opus / Fable / OLMo base natural / base think / **Think B1 / Think B2**。
- B1 と B2 の差 = 量子化と sampler と template の差(同じ model の二つの入口)。床の数の差が 4 / 20 を超えたら「経路で変わる」と書く。
- 評価語は書かない。

## §3. 予想(発火の前・`L3`)
- PB1-1: B1 の none/Q1 の床 = 4〜12 / 20(base think の 2 より上・Claude の 20 より下)。
- PB1-2: B1 の K の cut(答え)≥ 5 / 10(事後学習済みは JSON の指示に従う → hint の形を答えに写す)。
- PB1-3: B1 の 16384 の打ち切り ≤ 6 / 30・`</think>` が閉じる ≥ 24 / 30。
- PB2-1: B2 の床は B1 の ±4 / 20 の中。
- PB2-2: B2 の打ち切りは B1 より多い(Q4 は loop しやすい・07-28 の open stuck)。

## §4. 時間・順
- olm2(A → C)の後に流す(GPU を分ける)。B1 = 6 sub-batch × ≤ 72 分 ≈ ≤ 7 時間(短ければ 1〜2 時間)。B2 = 30 本 × ≤ 16384 / 約 15 tok/s ≈ ≤ 9 時間(典型 2〜4k token なら 1〜2 時間)。順 = B1 → B2(重みの取り寄せが olm2 の終わりに間に合わなければ B2 → B1)。
- 背景の一つの job: olm2 の process が消えるまで待つ → 重みの完了(`exit 0`)を確かめて B1 → B2。

## §5. 主張しないこと
- base(olm1 / olm2)と Think(本札)は同じ model の系ではない(事後学習・template・温度が違う)。一つの作図・一つの配置。MLX bf16 と llama.cpp Q4 の数値は同じ目盛りではない。

## §6. 手順
- 凍結の commit → `--dry` → 背景 job(待ち → `--fire --path B1` → `--fire --path B2`)→ `--read` → RESULT = `conversations/2026-10-22/RESULT_olm3_moy5_olmo3_32b_think_bf16_mlx_and_ollama_q4_screen_20261022.md`。出力 = `ConstructGap/exp/results_olm3_moy5_20261022_<tag>.jsonl`・log = `ConstructGap/exp/logs/olm3_20261022_B1B2.out`。
