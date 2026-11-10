# PREREG(札 `olm1`): moy-5 × 札 mnw1 の 7 腕 × OLMo-3-1125-32B(base・MLX bf16・zebrashark・費用ゼロ)— Opus 5.5 / Fable 5.1 との比較。二変種(natural / think = `Okay`(33413・空白なし)を最初の一語に固定)・二段(screen → 五腕)(2026-10-22 午後・実行層)

> **先生(10-22・逐語)**: 「olmoでの比較を取ります。」(直前の文脈 = mnw1 + mnw1b の表・Fable 5.5 が出たら比較表を埋める・Sol / Argon の見積り)
> **HEAD**(`R1`・fetch の後): `ff9691a3`(origin の先・push 待ち)。**凍結の実体**: 本書・runner [`ConstructGap/exp/olm1_moy5_olmo3_32b_mlx_mnw1_arms_20261022.py`](../../ConstructGap/exp/olm1_moy5_olmo3_32b_mlx_mnw1_arms_20261022.py)・疎通の記録 `ConstructGap/exp/results_olm1_smoke_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` を一つの commit に。runner は mnw1 の runner(凍結 `2c685fb2`)を import(PROMPT・score・table・verdict)。本書・runner・mnw1 の runner のどれかが commit と違えば走らない。読み取り器 v2 の較正 72 / 72 を assert。
> **凍結し直し #1(発火の直後・開示)**: 初版の凍結 `02e8f460` の runner は、固定する一語を「` Okay`(空白つき)」と書いて読み込み時の assert で止まった(行は一本も引いていない)。token 33413 は `Okay`(空白なし・問いの最後の改行の直後に来る字・cmt4 A31 / cmt5 と同じ id)なので、assert と本文の頭の字を `Okay` に直した。id・seed・設計・関門・予想は不変。
> **身分**: §0 = 開示(疎通の実出力)。§1〜§3 = 凍結の設計・関門・判定。§4 = 予想(発火の前)。採否と決め台詞は先生。

## §0. 開示(疎通・10-22 13:3x・凍結の前・`L1`)
- none/Q1(問いだけ)× 4 本・natural・max_new 4096・温度 0.7・seed 20262021: **床 0 / 4**。中身 = 2 本は即座に短い JSON(65・68 token・「P_y, A, J are collinear」「J, P_y, and K are collinear」= 誤り)/ 1 本は問いの指示文の続きを書いて止まる(43 token・JSON なし)/ 1 本は「Respond with JSON only: {…}」の template を繰り返して上限まで(4,096 token・loop)。速さ = 1 stream ≈ 9.5 token/s(4 本同時)。読み込み 5〜11 秒(file cache)。
- = **base model は raw prompt では moy-5 の床に届かない疑いが濃い**(09-20 NOTE「Olmo-3 32B が moy-5 の部品に届くかは未測定」への最初の数)。
- 家の道具(cmt5・10-20): 最初の一語に ` Okay`(id 33413)を固定して「考えの道」に入れると、moy-1 の bind が 8 / 40 → 40 / 40。本札の think 変種はこれを moy-5 に当てる。
- 07-28 の screen(ollama の `olmo-3:32b` = Think の流れ・Q4)は moy-1 で open stuck 9 / 9・blocked bind 7 / 7。本札はその変種を使わない(SilentHop の lens は base に張られている = 内側を読む道と同じ model にする)。
- cmt5 の cell(20 本 batch)は 23 分〜2 時間(MLX の batch 20 は ≈ 2 step/s)。本札は batch 5(≈ 9.5 step/s)で分ける。

## §1. 宇宙
1. **model** = `allenai/Olmo-3-1125-32B`(base・snapshot `c2b61dae…`・cmt 札と同じ)。経路 = mlx_lm 0.31.3 の `batch_generate`(bf16)・transformers 5.14.1 の tokenizer で **raw prompt を token に**(chat template なし = cmt 札と同じ)・温度 0.7(cmt5 / cmt9)・macOS 27.0.1。費用ゼロ。
2. **prompt** = mnw1 の 7 腕と byte 一致(md5 = K `b0b1d14b…`・none/Q1 `ee39ba02…`・none/Q1f `f4522117…`・conf/Q1 `bb82c97e…`・conf/Q1f `f32c88a9…`・cone/Q1 `ec464241…`・cone/Q1f `2c50d183…`・runner が import 時に assert)。
3. **変種**: natural = prompt のまま / think = 生成の最初の token を ` Okay`(33413・読み込み時に decode を assert)に固定(cmt5 の "think" cell と同じ形・本文の頭に " Okay" を残す)。
4. **seed** = 20261022 + 10 × 腕の番号 + 変種の番号 + 1000 × sub-batch の番号(再開しても同じ seed・5 本ずつ)。**max_new 6144**(上限に当たった行 = 打ち切りとして残し、数に載せる・分母から外さない)。
5. **n** = K 10・他 20(mnw1 と同じ)。

## §2. 段と関門(`R6`)
- **Stage 0(screen)**: natural と think の二変種で K 10 + none/Q1 20 = 計 60 本。
- **関門(変種ごと)**: **K の cut ≥ 8 / 10 かつ none/Q1 の床 ≥ 16 / 20**。落ちた変種は Stage 1 を引かない。
- **Stage 1**: 関門を通った変種で none/Q1f・conf/Q1・conf/Q1f・cone/Q1・cone/Q1f × n 20(100 本)。
- 両変種が落ちたら、本札は screen の記録として止め、比較表の OLMo の列に「部品に届かない(床・K の数)」と書く(朝の MEMO §4 の門の答え = P-compose は立たない・moy-5 の内側の読みは Olmo-3 base では入口が無い)。

## §3. 採点・判定
- 計器 = mnw1 §3 のまま(読み取り器 v2 の cut・cut_ans・床・退化した比例・形の分類・to_read)。追加 = 打ち切り(上限)の本数・token の中央値・非準拠(JSON が無い・問いの字でない)の本数は記述。
- 判定 = mnw1 §5 の `verdict()` を変種ごとに(Stage 1 がそろった変種だけ)。
- 比較表 = Opus 5.5 / Fable 5.1(mnw1 + mnw1b)/ OLMo-3 32B base(natural・think)の列。

## §4. 予想(発火の前・`L3`)
- P1(natural): 床 ≤ 4 / 20・K の cut ≤ 3 / 10 → 関門 FAIL。
- P2(think): 床 4〜12 / 20・K の cut 3〜8 / 10 → 五分五分。打ち切り(loop)は 1 割以上。
- P3(think が通った場合): conf/Q1f の cut_ans ≤ 5 / 20(Claude の 13〜19 より下)・cone/Q1 の cut ≤ 2・none/Q1f の退化した比例は Claude より少ない(形の指図に従わない行が多い)。
- P4: 「比例として述べよ」に従う行でも、Newton の焦点の形(FV : FP_x = FP_x : EJ)は ≤ 2 / 20。

## §5. 時間
- sub-batch 5 本 = 最長 6144 / 9.5 ≈ 650 秒(loop の行が在る時)。Stage 0 = 12 sub-batch ≈ ≤ 2.2 時間。Stage 1 = 変種あたり 20 sub-batch ≈ ≤ 3.6 時間。短い行が多ければずっと速い。

## §6. 主張しないこと
- base model(事後学習なし)と Claude の API(adaptive thinking)は同じ種類の系ではない。raw prompt・chat template なしは「lens で内側を読む時の model と同じ条件」を優先した結果。
- think 変種は一 token の介入(開示)。温度 0.7 の抽選と API の抽選は同じ目盛りではない。MLX の batch 生成の数値(cmt5 §1: MLX と torch の差)。
- 一つの作図・一つの配置・一つの open-weight model。

## §7. 手順
- 凍結の commit → `--fire --stage 0`(背景)→ `--gate --variant natural` / `think` → 通った変種で `--fire --stage 1 --variants <変種>`(背景)→ `--read` → RESULT = `conversations/2026-10-22/RESULT_olm1_moy5_olmo3_32b_mnw1_arms_20261022.md`。出力 = `ConstructGap/exp/results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl`・log = `ConstructGap/exp/logs/olm1_20261022_stage{0,1}.out`。
