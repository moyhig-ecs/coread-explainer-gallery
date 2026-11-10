HEAD(R1) = 05e6c131(pull の後・origin と同じ)。走行の時の zebrashark の HEAD = 27ad790c(凍結 d7eba25d の後に olm89 の凍結と台帳の行・dirty なし・script と PREREG の md5 は MacBook の file と一致)

# RESULT(札 `olm88`・2026-10-31 夜・zebrashark): moy-1(線 1・推論空間・立て方 A = 行き先)— 入口の関門 ✗(attractor 29 行・線 30 に 1 足りない)= 読まない(PREREG §4)。probe の値は出していない・見ていない

- 凍結 = [PREREG](PREREG_olm88_moy1_inference_space_outcome_from_first_tokens_20261031.md)(d7eba25d)・runner = [olm88_…py](../../ConstructGap/exp/olm88_moy1_inference_space_outcome_from_first_tokens_20261031.py)(md5 `d8f718cc…`)。
- 出力:
  - `ConstructGap/exp/olm88/control.json`(md5 `0c400a7f…`)
  - `read.json`(md5 `a9a0b230…` = `"stopped": "統制 ✗ = 読まない(min_class)"` だけ)
  - `control_run.log`(`d5f74b39…`)・`read_run.log`(`92ae1157…`)
- runner は関門で返す作りで、C0〜C3 と Q1・Q2 の計算はしていない(`control.json` に C の欄が無い)。

## 統制

| | 判 | 実出力(`control.json`) |
|---|---|---|
| olm87 の G1・G2 | ✓ | label 無し 0・rows 200・series 200・`lens_O` 200 |
| **入口の関門** attractor と bind がどちらも 30 行以上 | **✗** | 行 116 = **attractor 29**・bind 87 |
| C0〜C3 | — | 計算していない |

## 行が減った所(述語の側だけで数えた・label と特徴の組み合わせは見ていない)

olm87 の series の meta で、`rows_A` の述語を順に当てた。合計は `control.json` と一致する(attractor 29・bind 87)。

| 述語 | 落ちた行 |
|---|---|
| (i) 答えから始めた | 26 |
| (ii) 答えの欄の結末が bind / attractor でない(flail・stuck-L1) | 42 |
| (iii) 答えの欄の頭 `{"` が見つからない(`json_begin` が無い) | attractor 2・bind 8 |
| (iii) 答えの欄の頭が生成の頭から 80 token より手前 | attractor 6(位置 3・3・6・22・32・36)・bind 0 |
| 残った行 | attractor **29**・bind 87 |

- olm87 の §3 の予想(考えてから答えた行の attractor 37 ≥ 30)は、(iii) の前で数えていた。読む札の述語で数えていれば、凍結の前に線を割りうると分かった。設計の側の落ちである([RESULT_olm87](RESULT_olm87_moy1_f5a2_natural_200_rows_generation_capture_20261031.md) 読み 3)。
- 位置 3・6 の 3 行は、生成の分類では「考えてから答えた」行だが、欄の頭がほぼ生成の頭に在る。欄の前に数 token の前置きが在る形と見られるが、本文は読んでいない。

## 伺うこと(PREREG §4「作り直しは先生に伺ってから」)

関門は凍結のまま ✗ で、この札はここで閉じる。続けるなら新しい札になる。候補は三つ。

- **(a) 行を足す新しい札**: olm87 と同じ手順(seed だけ新しい)で F5a-2 natural をもう 100〜200 行引く。olm88 の述語と関門(30)は替えない。
  - 見込み: olm87 の率なら、100 行で attractor +15 前後(L3)。
  - zebrashark で約 2〜4 時間 + 取り出し 15〜30 分。
- **(b) 関門か窓を緩める新しい札**: 線を 25 に下げる、窓を [0, 32) にする、など。
  - 29 を見た後に線を動かすことになる。値(probe の AUC)は見ていないが、行の数を見てから選んだ線だと書く必要がある。
- **(c) 立て方 A はここで止める**: 「この規模では関門に届かない」と記録し、② の次の札へ進む。
