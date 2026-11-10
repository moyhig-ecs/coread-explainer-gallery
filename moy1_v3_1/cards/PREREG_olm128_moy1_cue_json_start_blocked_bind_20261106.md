HEAD(R1) = 2096bc82(凍結の前の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm128`・凍結 2026-11-06): moy-1 の blocked で、「cue \n の blocked の行」/「cue " " の blocked の行」/「cue \n\n の blocked の行」の bind の差(2 / 9・4 / 10・7 / 10)は、JSON から書き始める行の割合の差で説明されるか(読むだけ・model なし・第一段)

- 発注(逐語・先生 11-06): 「3 推しのAで進む」(= 駅 2 の冷間の読み手が出し、家がまだ打っていない次の候補 A。図の腕・文の腕・両読み手から 6 問 = [RESULT 駅 2](coread_station2_3/station2_moy1/RESULT_station2_moy1_next_visible_two_maker_variation_20261106.md) §2)。
- G10 の欄: 比べる物 = 「cue \n の blocked の行」/「cue " " の blocked の行」/「cue \n\n の blocked の行」 / 計器 = 最初の {"conjecture" の位置(書き始め = JSON か文か)× 凍結の label(B-bind) / 雛形 = いいえ
- runner = [olm128_…py](../../ConstructGap/exp/olm128_moy1_cue_json_start_blocked_bind_20261106.py)(この file と同じ commit・`--selftest` は合成の行で PASS)。出力 = `ConstructGap/exp/olm128/read.json`。

## §0. 起案の前に見た物(開示)

- **既知**: 図(駅 2 の entry・CLAIMS K06 / K10 / K11 / K20)が出していた値 = cue `\n\n` の blocked 10 行で、JSON から書き始めた 3 行は attractor 3 / 3・文から書き始めた 7 行は bind 7 / 7(K11)/ blocked の bind は cue `\n` 2 / 9・`" "` 4 / 10・`\n\n` 7 / 10(上限の行を除く・K20)。
- **見ていない**: cue `\n` と `" "` の blocked の行の、書き始め(JSON か文か)と、書き始め × label の表。open の行の書き始め。
- 起案の前に見たのは、二つの file の構造(key・行の数 = 3 cue × 2 条件 × 10 行・1 本は温度 0・9 本は 0.7)・label の語彙(B-attractor / B-bind / B-flail / B-stuck-L1)・md5 だけ。

## §1. 材料と計器

- 材料(凍結の出力・読むだけ): `probes/olmo3-base-bf16-screen/results/screen_olmo3_base_bf16.json`(md5 `63f4148d…`・cue `\n` 20 行)/ `probes/olmo3-pc1-cue-invariance/results/pc1_runs.json`(md5 `af884e14…`・cue `" "` と `\n\n` 各 20 行・凍結 `6a32bb0`)。OLMo-3 32B base・bf16・chat の型なし。
- 書き始め = `content.find('{"conjecture"') == 0` なら JSON・そうでなければ文(図の K10 と同じ定義・JSON が無い行は文の側)。参考に「先頭の空白と ``` を除いて `{"conjecture"`」の緩い定義も数える(判定に使わない)。
- bind = 凍結の label が `B-bind`。上限(`hit_cap`)の行は除く(図の K20 と同じ)。

## §2. 関門

- **G0**: 二つの file の md5 が §1 と一致。
- **C0(陽性統制)**: cue `\n\n` の blocked 10 行が、この計器で K11 を再現する(JSON 3・文 7・JSON ∧ bind でない 3・文 ∧ bind 7)。✗ → 計器が図と違う = 読まない。
- **G1**: cue `\n` と `" "` の blocked の、上限を除いた行がそれぞれ 8 以上。

## §3. 問いと帯(判定は cue `\n` と `" "` の blocked = 見ていない 19 行前後で)

- **Q1(書き始めと label の対応は、見ていない cue でも保たれるか)**: 一致率 = (文 ∧ bind + JSON ∧ bind でない)/ 行の数。**≥ 0.80 = 保たれる / ≤ 0.60 = 保たれない / その間 = 間**。予想: 保たれる 0.55・間 0.25・保たれない 0.20。
- **Q2(cue は書き始めを動かすか)**: JSON から書き始めた割合の差 = cue `\n`(または `" "`)− cue `\n\n`(3 / 10)。**≥ +0.20 = 動く(説明の向き = bind の少ない cue ほど JSON が多い)/ ≤ −0.20 = 逆 / その間 = 動かない**(R3: 10 行の小さい n なので差は 2 行以上を要る)。主は cue `\n`(bind の差が一番大きい)・`" "` は同じ帯で記述に近い扱い。予想(`\n`): 動く 0.50・動かない 0.35・逆 0.15。
- **Q3(まとめ)**: Q1 保たれる ∧ Q2(`\n`)動く → 「書き始めで説明される(記述の範囲)」/ Q1 保たれる ∧ Q2 動かない・逆 → 「書き始めは label と対応するが、cue の差は書き始めの外」/ Q1 保たれない → 「書き始めでは説明されない」/ Q1 間 → 「決まらない」。

## §4. 記述(判定に使わない)

- open の行の書き始めと bind・温度 0 の行(cue × 条件で 1 本ずつ)の書き始めと label・緩い定義の数。

## §5. 言えないこと

- 因果(書き始めが bind を起こす)は言わない。この札は既存の 60 行の対応の記述で、書き始めを替えた腕は無い。
- 一つの prompt(凍結の replication config)・一つの model・cue ごとに 10 行(温度 0 の 1 本を含む)。
- 「説明される」は、cue の差の向きが書き始めの割合の差と揃う、までの意味で、量の分解(どれだけが書き始めで説明されるか)は言わない。

## §6. 次の段(この札では凍結しない・先生の裁定)

- 第二段の案: 書き始めを替える腕(`{"conjecture"` を先に置く / 文を先に置く)× cue 三種 × blocked を各 20〜30 行、zebrashark で生成し、書き始めを揃えた時に cue の差が残るかを見る(因果の側)。Q3 の結果で起案する。
