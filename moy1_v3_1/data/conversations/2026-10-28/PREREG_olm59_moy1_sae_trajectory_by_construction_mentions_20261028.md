HEAD(R1) = cc9f4b71(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm59`・凍結 2026-10-28 午後): moy-1 — 作図で着目している部分(本文が名指す O1O2 / He・Hi)と、SAE の活性の推移を token で揃える

- 発注(逐語): 先生 10-28「作図で着目している部分と係数の変化を対比的に図解する」→「係数って誤解されそうな表現でした。SAEによる活性の推移で通じますか？」→「まず、moy-1に対して、対比的な図解を追加要求して描いてもらいます。並行して、札を起草しながら Opus・Fable で辿った道が、OLMoでどう活性化するか読んでいきましょう。」
- 目的: moy-1 の図解(10-28 の競作・moy-1 の 2 本)に足す章の data。図の作り手は SAE を走らせない(BRIEF の柵)ので、本札が token ごとの値を作る。
- 親: [olm7](../2026-10-24/RESULT_olm7_moy1_commit_direction_sae_lens_20261024.md)(残差・latent の群)・[olm6 (ii)](../2026-10-24/RESULT_olm6_ii_trajectory_triple_readout_base_rows_20261024.md)(読み方 = threshold)・[olm4](../2026-10-24/RESULT_olm4_commit_direction_and_public_sae_olmo3_32b_20261024.md)(SAE・FVE 0.447 / 0.475)・[cmt5](../2026-10-20/RESULT_cmt5_first_token_fixed_sampling_two_stages_20261020.md)(行)・述語 = 棚卸し M1 の `inv_m1.py` / `inv_m1_d.py`(`explainer_moy1/inventory/`)。読み方 = [ADJUDICATION 10-27](../2026-10-27/ADJUDICATION_reading_rule_frozen_text_literal_20261027.md)。
- runner = [olm59_…py](../../ConstructGap/exp/olm59_moy1_sae_trajectory_by_construction_mentions_20261028.py)。

## §0. 凍結の前に見た物(開示)
- 一行(F5a-2 think r0)の本文の写し(token の位置と述語の当たり)だけを試した: 述語 `PRED_O` は 0 回・`PRED_HEHI_DIAM` は token 409 から。本文の結びは「concyclic with HeHi as the diameter」で、全文の label は `B-bind`・答えの欄の label(`label_json_fields`)は `B-attractor`。活性の値は見ていない。
- これを受けて 120 行の二つの label を数えた(cmt5 の json・活性ではない): 考えの道 = 全文 bind 40 / 40・**答えの欄 bind 36 / 40(attractor 4)**・答えの道 = 全文 bind 8 / 40・**答えの欄 bind 4 / 40**。→ 本札の outcome は**答えの欄の label** にする(全文の label は並べるだけ)。cmt5 の RESULT への訂正の札は先生に確かめてから(本札では書き換えない)。

## §1. 宇宙(`L1`)
- 行 = olm7 の 120 行(cmt5: F5a-2 / F5b-1 × natural / think(` Okay` 固定)/ answer(`{"` 固定)× 20・Olmo-3-1125-32B base・温度 0.7)。読む物 = 生成した部分(g0 から)の層 32 の残差(`olm7/rows/*.npz` の `traj32`)。**model は動かさない**。
- SAE = 公開 `bcywinski/Olmo-3-32B-Base-SAE` の層 32・threshold で読む(olm6 (ii) と同じ)。読む latent = **olm7 の RESULT が凍結した群だけ**(選び直さない): 結び(close)= 4058・33874・41939・62051・62610・99515・111377 / 考えの中点(mid)= 47156・122221・82816・88569・104829・127364 / 答えの側(ans・first 窓 answer − think 上位 10)= 58663・63972・66035・6095・104152・9975・106598・16865・98793・56001 / 考えの側(think・同 think − answer 上位 6)= 76179・24969・58801・33562・18171・41939。群の値 = 群の latent の平均。
- 作図で着目している部分(本文の述語・token に写す): `o_diam` = 「直径 / 中点 / 中心 … O1O2」(`PRED_O`)・`h_diam` = 「直径 … HeHi / He and Hi」(`PRED_HEHI_DIAM`)・`o_name` = O1・O2 の名・`h_name` = He・Hi の名・`circle`・`json`(答えの欄)。token の文字の範囲は、生成の id の前置きを一つずつ decode した長さで取る。
- 出来事 = 最初の `o_diam` の先頭の token・最初の `h_diam` の先頭の token。その前の 32 token と後の 32 token で群の平均を比べる(両側が生成の内に収まる行だけ)。
- outcome = 答えの欄の label(`label_json`)。全文の label(`label`)は並べる。

## §2. 統制(R6)
- **C1(計器)**: 生成した token の残差 4,080 本(seed 5959・1 行 34 本 × 120)で SAE の FVE ≥ 0.40・L0 が 100〜280(olm4 の実測 = base 199〜201・Think 261・FVE 0.447 / 0.475)。落ちたら発火しない。(凍結し直し #1 で直した・§7)
- **C2(写し)**: 生成の id を decode した本文が cmt5 の本文と一致(前後の空白を除く)≥ 118 / 120。落ちたら述語の位置を読まない。
- **C3(再現)**: 答えの側の群の first 窓の平均が、答えから始めた行で考えの道の中央値より大きい ≥ 15 / 20(各 variant)。群は同じ data で選んだので**外れたら pipeline の誤り**(読みの根拠にはしない)。

## §3. 予想(凍結・`L3`・外れてよい)
- **Q1(O を名指すと結びが立つ)**: 考えの道で答えの欄が bind の行のうち `o_diam` の出来事を持つ行で、結びの群は後 32 > 前 32 が ≥ 70 %。
- **Q2(He・Hi を名指しても結びが立つ)**: `h_diam` の出来事を持つ全行で、結びの群は後 32 > 前 32 が ≥ 60 %(= 結びの群は「どの円か」でなく「円を名指して言い切る」に応じる、の予想)。
- **Q3(記述・閾なし)**: 出来事 2 種 × 群 4 種 × outcome(全行 / bind / attractor)の前後の差の中央値と本数。
- **Q4(時間)**: 発火 ≤ 20 分。

## §4. 読み方・可読条件(R15)
- ADJUDICATION 10-27 を本札の凍結の文とする。Q1・Q2 は対象の行が **8 本未満なら「読まない」**(この文が凍結の文)。
- Q1 と Q2 が両方 ✓ の時だけ「結びの群は円を名指す所で立ち、O1O2 と He・Hi を分けない」と書ける。Q1 だけ ✓ なら「O1O2 を名指す所で立つ(He・Hi では言えない)」。
- 群の名(結び・中点・答えの側・考えの側)は olm7 の unembed の上位の語からの名付けで、意味の同定ではない。

## §5. 主張しないこと
- OLMo-3 32B base の層 32・moy-1 の F5 の 2 prompt・cmt5 の 120 行。frontier の model の中身ではない。活性は相関で、因果(活性が bind を起こす)は言わない。述語は本文の正規表現で、作図の意味の全部ではない(`HeHi` の綴り以外の言い換えを取りこぼしうる)。

## §6. 費用(R14)
- model なし。SAE の選んだ 28 本(41939 は結びと考えの側の両方に在る)の encode(120 行 × 平均 約 1,500 token)+ C1 の全辞書の encode 4,080 本 + 本文の写し(1 行 約 5 秒)≈ 15 分。

## §7. 凍結し直し #1(2026-10-28 15:04・発火の前・開示)
- 最初の凍結(`fe7a8ced`)の統制の実出力: **C1 = FVE 0.4394・L0 235.4(n 4,080)→ 落ち**(L0 が凍結の範囲 100〜220 の外)/ C2 = 120 / 120 / C3 = F5a-2 20 / 20・F5b-1 20 / 20。鎖は C1 の落ちで止まり、発火(行ごとの値)も読み(Q1〜Q3)も走っていない。
- 診断: 100〜220 は実測を見ずに置いた範囲(k = 160 の周りを想定)。threshold で読む L0 は文章で変わり、家の実測は olm4 の base 199〜201・Think 261(`olm4/control.json`・RESULT olm4 §3)。今回の 235 はその内側。FVE は olm4 と同じ水準。= 計器の不調ではなく、範囲の書き損じ。
- 直した物: C1 の L0 の範囲を 100〜280(家の実測 199〜261 を含む)に。本数の記述を実装の 4,080(1 行 34 本 × 120)に合わせた(4,096 と書いていた)。予想・読み方・群・述語は変えていない。
- 見た物: 上の統制の実出力だけ(C3 は答えの側の群の first 窓の平均 = 群を選んだ data と同じ集計で、Q1・Q2 の出来事の前後の値は見ていない)。
