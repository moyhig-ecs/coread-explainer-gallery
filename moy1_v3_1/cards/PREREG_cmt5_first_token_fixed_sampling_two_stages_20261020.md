# PREREG(札 cmt5): 一段目(最初の一語)と二段目(答えの道の上の結論の入口)を分けて数える — 温度 0.7 で最初の一語を固定して n 20 ずつ

- 日付: 2026-10-20(火)朝・zebrashark(M2 Ultra 192 GB)・実行層(Opus 5.5)/ 書き始めの HEAD = `ce3ec74f`
- 発注(逐語): 先生 10-20「1 / 2 / 3順に進めます」(2 = 本札。1 = 図解 v5.13 は札 Q が並行で作業中・本札と file は重ならない)
- 親 = [RESULT cmt4](RESULT_cmt4_first_token_answer_or_think_swap_20261020.md) §7。
- **凍結の実体**: 本書と script `probes/olmo3-f5-think-prefix/tsd_r5/replay_cmt5_first_token_fixed_sampling_20261020.py` を一つの commit に。script は cmt3 の script(凍結 `c5551abc`)を import し、cmt4 の A31 の出力(md5 `2e30fe73`)を読む。dirty なら走らない。

## §0. 事前に知っていること(開示)
1. cmt4: F5a-2 の最初の位置は ` Okay` と `{"` が同点(0.139 / 0.139・温度 0.7)。F5b-1 は ` Okay` 0.476・`{"` 0.304。
   - 温度 0 の反実: F5a-2 + Okay → B-bind・F5b-1 + `{"` → B-bind。
   - 温度 0 の自然: F5a-2 = 答えから B-attractor・F5b-1 = 考えから B-bind。
2. 温度 0.7 の 18 本(f5_runs): 答えから始めた 5 本 = すべて B-attractor(F5a-2 2・F5b-1 3)。考えから始めた 13 本 = B-bind 12・B-flail 1。
3. 生成は f5_runs と同じ温度 0.7・同じ sampler(`make_sampler(temp=0.7)`)。ただし本札は MLX の `batch_generate`(20 本を一度に)で、f5_runs の一本ずつの `generate` と数値は同じではない(sampler の分布は同じ)。⇒ C1 で較正する。
4. self-test ⭕。二項の 95% 区間: F5a-2 の自然の答えから = 0〜6 本 / 20(p 0.146)・F5b-1 = 2〜10 本 / 20(p 0.308)。

## §1. 設計
- cells(各 n 20・温度 0.7・最大 12,288 token・seed は cell ごとに固定 = 20261020 + 10·prompt + kind):

| prompt | natural | think | answer |
|---|---|---|---|
| F5a-2 | 最初の一語も抽選 | ` Okay`(id 33413)を固定 | `{"`(id 5018)を固定 |
| F5b-1 | 同 | 同 | 同 |

- label = 凍結の分類器(`run_f5.analyze`)。数えるもの = B-attractor の数・B-bind の数(Wilson の 95% 区間を並べる)・答えから始めた本数(natural)・τ。

## §2. 統制
- **C1(sampler の較正)**: natural の答えから始めた本数が、cmt4 A31 の p_brace(温度 0.7)の二項の 95% 区間に入る(両 prompt)。
- **C2**: label が付かない行 ≤ 2 / 120。
- 落ちたら、読みは保留して報告する。

## §3. 読みの規則(凍結・余白 6 / 20 = 0.3)
1. **一段目(STAGE1)**: prompt ごとに、attractor(answer)− attractor(think)≥ 6 → YES = 「最初の一語(答えか考えか)が attractor の率を動かす」。
2. **二段目(STAGE2)**: prompt ごとに、answer の cell の attractor が 3〜17 本 → 「答えの道の上でも、結論の入口でまだ分かれる」。≥ 18 →「答えの道 ≈ attractor」・≤ 2 →「答えの道でも attractor にならない」。
3. **prompt が二段目を形作るか**: |attractor(F5a-2 answer)− attractor(F5b-1 answer)| ≥ 6 → YES。
4. natural の cell は、答えから始めた行と考えから始めた行に分けて label を記述する(18 本の「答えから 5 / 5 が attractor」と並べる)。

## §4. 予想(発火の前に書く)
- P1: 考えの道の bind は両 prompt で ≥ 17 / 20。
- P2: F5a-2 の答えの道の attractor は ≥ 12 / 20(温度 0 でも attractor・温度 0.7 で 2 / 2)。
- P3: F5b-1 の答えの道の attractor は 6〜14 / 20(温度 0 では bind・温度 0.7 では 3 / 3 が attractor = 中間)。
- ⇒ STAGE1 は両方 YES・STAGE2 は F5b-1 で「まだ分かれる」・prompt が二段目を形作る = YES。

## §5. 主張しないこと
- 機構。
- 最初の一語の固定は反実の操作。
- batch と一本ずつの数値の違い(C1 で較正)。
- 一つの model・prompt 2 つ・n 20。

## §6. 手順
`--fire`(MLX・6 cells × 20 本・数十分)→ RESULT。
