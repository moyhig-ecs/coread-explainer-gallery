HEAD(R1) = 84931c28(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm91`・凍結 2026-10-31 夜): moy-1(線 1・推論空間を探す・立て方 A = 行き先・olm88 の再走)— olm87 + olm90 の 400 行で、答えを書く前の最初の 64 token の残差(層 32・48)に、答えの欄の結末(bind / attractor)が、同じ窓の J-lens の読み出しと語の袋を越えて読めるか

- 発注(逐語): 主 session の問い「(a) 行を足す新しい札(推し)…(b) 関門か窓を緩める…(c) 立て方 A はここで止めて、次へ進む」→ 先生 10-31 夜「**a 足して再走**」。
- G10 の欄: 比べる物 = 「層 32 と 48 の残差(最初の 64 token の平均)」/「J-lens の読み出しと語の袋(同じ窓)」 / 計器 = 行を半分に分けた正則化つきの logistic の probe の AUC(答えの欄の結末 attractor 対 bind・一行一標本・olm88 と同じ計器) / 雛形 = いいえ
- runner = [olm91_…py](../../ConstructGap/exp/olm91_moy1_inference_space_outcome_from_first_tokens_400_rows_20261031.py)。走らせる所 = **zebrashark**。forward なし・API なし。
- data = **olm87 の 200 行 + olm90 の 200 行**(olm90 は凍結 dc70c5f6・この札の凍結の時は未走行)。
- **olm88(凍結 d7eba25d)の写し**。
  - 替えたのは data の出所と、それに触れる 5 つの関数(`src_gates`・`rows_A`・`vocab_pool`・`features`・`count`)だけ。あとは control / read の中の呼び出しの名と、自己検査。
  - 窓・行の述語・入口の関門(30)・J の語の選び方・推定・seed(8801・8802)・統制 C0〜C3 の線・問い Q1・Q2 の線は、olm88 と同じ。
  - 同じ本文の関数 11 個と定数 19 個が olm88 と一致することを `--selftest` で確かめる。陽性統制として、`run_rows` の一字を替えた写しで NG が出ることを見た。

## §0. 凍結の前に見た物(開示)

- **olm90 の出力は何も見ていない**(未走行)。
- olm87 の出力の全部([RESULT](RESULT_olm87_moy1_f5a2_natural_200_rows_generation_capture_20261031.md))。olm87 の行で、olm88 の述語で残る行 = attractor 29・bind 87。
- olm88 の出力([RESULT](RESULT_olm88_moy1_inference_space_outcome_from_first_tokens_20261031.md))は入口の関門 ✗ だけ。
  - **olm87 の行の上でも、この問いの probe の値(AUC・E)は一度も計算していない**(olm88 の runner は関門で返す)。
  - 行が述語で落ちた数(欄の頭が無い・80 token より手前)は数えた。label と特徴の組み合わせは見ていない。
- olm89 の出力(olm87 の行の残差で、O の名の 8 token 前の問い・[RESULT](RESULT_olm89_moy1_inference_space_k8_lookahead_replication_new_rows_20261031.md))。
  - 同じ残差の別の問い(O の名の先読み)の値を見た。結末の label との組み合わせは見ていない。
- 自己検査(`--selftest` 7 / 7・zebrashark・sklearn が要る)。

## §1. 行・窓・表現(R5・olm88 §1 と同じ)

- 行 = olm87 と olm90 の行で、次の三つを満たす物。同じ名の行は出所で分ける(`src` = olm87 / olm90)。
  - (i) 答えから始めていない。
  - (ii) 答えの欄の結末(`label_json`)が bind か attractor。
  - (iii) 答えの欄の頭 `{"` が、生成の頭から 80 token 以上先。
  - label: attractor = 1・bind = 0。flail・stuck・label 無しは入れない。
- **除外も書く**: (iii) で落ちる行(欄の頭が無い・80 token より手前)の数は、出所ごとに RESULT に書く(olm87 = attractor 8・bind 8)。
- **主の窓** = 生成の頭からの位置 [0, 64)。
- 表現(窓の平均・olm88 と同じ式):
  - L32・L48 = 層 32・48 の残差。
  - J = J-lens 層 48 の O の集合の log Σp + 512 語の log p。512 語 = 400 行の中の行の生成の 4 位置おきの一位の語の頻度の上位(label を見ない)。
  - W = 窓の単語と二語の並び(語彙 = 窓に出る行が 3 以上)。
- 推定 = 学習の行で標準化した logistic(L32・L48・J = L2・W = L1・C 0.1)。行を無作為に半分に分けて 200 回(seed 8801)、試す半分で AUC。

## §2. 統制(R6・olm88 §2 と同じ線)

- **入口の関門**: olm87 と olm90 の G1・G2 がどちらも通り、attractor と bind がどちらも 30 行以上。どれか ✗ → 読まない。
- **C0**: J の O の値が、保存の series の `lens_O` と 1e−3 以内の位置 ≥ 99 %。
- **C1**: 語で決まる label(主の窓に在る割合が 0.5 に一番近い単語の有無)で、W の AUC の中央値 ≥ 0.95。かつ L32・L48 − W < 0.03。
- **C2(陽性統制)**: 答えの欄の窓(`{"` から 64 token か欄の終わりまで)の平均で、同じ結末の label を L48 が AUC の中央値 ≥ 0.90 で読む。
- **C3(零)**: 学習の半分の label を行の間で入れ替える(seed 8802・試す半分は本物)。全部の表現で中央値 0.40〜0.60。
- どれか ✗ → 読まない。

## §3. 問いと予想(確率は 0〜1・olm88 と同じ線と確率)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1** | 最初の 64 token で、層 32 か 48 の残差が結末を J と W の高い方を越えて読むか | E = AUC(L)− max(AUC(J), AUC(W))。L32 か L48 で、E の中央値 ≥ +0.05 かつ 5 % 点 > 0 | 0.15 |
| Q2 | 窓 [0, 16)・[0, 32)・[0, 128)・答えの欄の直前 64 token の AUC と E | 記述(行は窓ごとに使える物だけ) | — |

- 入口の関門が通る見込み: p 0.99(olm90 PREREG §3)。
- L3: 「線 1 の生成の残差は、答えを書く前の最初の 64 token で、答えの欄の結末を、言語化空間(J-lens の読み出し)と語の袋を越えて持つ = 推論空間の候補(行き先)」p = 0.15。
  - 解ける条件: Q1 ✓ で真。L32・L48 とも E の中央値 ≤ +0.01 で偽。その間は解けない。
- 動かす主張(olm88 §3 と同じ):
  - **Q1 ✓** → 判定「線 1 で推論空間の候補が在る(行き先・最初の 64 token・層 X・J-lens の読み出しと語の袋を越える)」。
  - **偽** で、J か W の AUC の中央値 ≥ 0.60 → 「結末は最初の 64 token の言語化空間か語の袋で読める = 推論空間はこの形では見えない」。
  - **偽** で、L32・L48・J・W の AUC の中央値がどれも < 0.60 → 「最初の 64 token では、結末は残差でも読めない(この計器で)」。「行き先がまだ決まっていない」とは言わない。
  - **間** → 記述。
- 出所ごとの値(olm87 だけ・olm90 だけ)は、この札では出さない。二つは同じ手順・違う seed の行で、一つの母集団として読む。

## §4. 止める規則

- 入口の関門か C0〜C3 のどれかが ✗ → 読まない。作り直しは先生に伺ってから。
- 1 回で打ち切る。走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと(olm88 §5 と同じ)

- Q1 ✓ でも「推論」の証明ではない。二語より長い語順・書式・窓の外の位置の性質を、残差が持つだけでも越えうる。J は 513 次元の平均で、J-lens の分布の全部ではない。
- 結末は凍結の分類器の答えの欄の label で、model が「決めた」時点は言わない。
- 一つの prompt(F5a-2)・一つの腕(natural)・OLMo-3 32B base の自分の生成。因果・中の状態は言わない。

## §6. 走らせ方(zebrashark・olm90 の `--series` の後に鎖で)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm91_moy1_inference_space_outcome_from_first_tokens_400_rows_20261031.py --selftest   # 凍結の前に通した・7 / 7
$P -I exp/olm91_moy1_inference_space_outcome_from_first_tokens_400_rows_20261031.py --count
$P -I exp/olm91_moy1_inference_space_outcome_from_first_tokens_400_rows_20261031.py --control
$P -I exp/olm91_moy1_inference_space_outcome_from_first_tokens_400_rows_20261031.py --read
```
