HEAD(R1) = dbdd59c4(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm88`・凍結 2026-10-31 夕): moy-1(線 1・推論空間を探す・立て方 A = 行き先)— 答えを書く前の最初の 64 token の残差(層 32・48)に、答えの欄の結末(bind / attractor)が、同じ窓の J-lens の読み出しと語の袋を越えて読めるか

- 発注(逐語): 先生 10-31 夕「1から順に進めましょう」(候補の 3「立て方 A」)→ 規模の選び「F5a-2 natural 200 行 (Recommended)」。
- G10 の欄: 比べる物 = 「層 32 と 48 の残差(最初の 64 token の平均)」/「J-lens の読み出しと語の袋(同じ窓)」 / 計器 = 行を半分に分けた正則化つきの logistic の probe の AUC(答えの欄の結末 attractor 対 bind・一行一標本) / 雛形 = いいえ
- runner = [olm88_…py](../../ConstructGap/exp/olm88_moy1_inference_space_outcome_from_first_tokens_20261031.py)。走らせる所 = **zebrashark**。forward なし・API なし。
- data = **olm87 の新しい 200 行**(凍結 6e81795b・この札の凍結の時は生成の途中)。cmt5 の 120 行は使わない。
- 推定は olm84(凍結 728cdca7)の logistic をそのまま使う(語の袋 = L1・ほか = L2・C 0.1)。
- 語の約束は olm83〜86 と同じ: **推論空間の候補** = 残差が持つ情報のうち、同じ位置の J-lens の読み出しと語の袋で読めない物(働きで決める)。

## §0. 凍結の前に見た物(開示)

- **olm87 の出力は何も見ていない**。生成の log は、落ちていないか(Traceback・Error の数 = 0)と process の有無だけを見た(batch ごとの label の数の行は読んでいない)。
- cmt5(10-20)の F5a-2 natural: 考えてから答えた 19 行の答えの欄 = bind 10・attractor 6・flail 3(olm87 の PREREG §0)。
- DRAFT(10-31・`i_space_prep/DRAFT_PREREG_line1_inference_space_20261031.md`)の立て方 A の案。主 session は B を推し、A は「attractor が少なく弱い」と書いた → この札は行を増やした版。
- 自己検査(`--selftest` 4 / 4・zebrashark・sklearn が要る)。
- 道筋の確かめ(zebrashark・10-31 夕): 既存の F5a-2 natural の 3 行(olm7 の残差 + olm65 の系列)で、特徴の形と C0 の写しだけを見た(J の O の値と保存の系列の差は最大 7.6e−6)。label と値の組み合わせは見ていない。

## §1. 行・窓・表現(R5)

- 行 = olm87 の行で、(i) 答えから始めていない、(ii) 答えの欄の結末(`label_json` = 凍結の分類器 `run_f5.analyze` の `label_json_fields`)が bind か attractor、(iii) 答えの欄の頭 `{"` が生成の頭から 80 token 以上先(主の窓の終わり 64 + 16)。
  - label: attractor = 1・bind = 0。flail・stuck・label 無しは入れない。
- **主の窓** = 生成の頭からの位置 [0, 64)。
- 表現(窓の平均):
  - **L32**・**L48** = 層 32・48 の残差の 64 位置の平均。
  - **J** = J-lens 層 48 の読み出し(O の集合の log Σp + 512 語の log p)の 64 位置の平均。512 語 = この札の行の生成の 4 位置おきの J-lens の一位の語の頻度の上位(label を見ない)。
  - **W** = 窓の 64 token の単語と二語の並びの数え(語彙 = 窓に出る行が 3 以上・label を見ない)。
- 推定 = 学習の行で標準化した logistic(L32・L48・J = L2・W = L1・C 0.1)。行を無作為に半分に分けて 200 回(seed 8801)、試す半分で AUC。

## §2. 統制(R6)

- **入口の関門**: olm87 の G1 と G2 が通り、attractor と bind がどちらも 30 行以上。どれか ✗ → 読まない。
- **C0**: J の O の値が olm87 の series の `lens_O` と 1e−3 以内の位置 ≥ 99 %。
- **C1**: 語で決まる label(主の窓に在る割合が 0.5 に一番近い単語の有無)で、W の AUC の中央値 ≥ 0.95、かつ L32・L48 − W < 0.03。
- **C2(陽性統制)**: 答えの欄の窓(`{"` から 64 token か欄の終わりまで)の平均で、同じ結末の label を L48 が AUC の中央値 ≥ 0.90 で読む(結末を書いている所 = 読めるはずの所)。
- **C3(零)**: 学習の半分の label を行の間で入れ替える(seed 8802・試す半分は本物)。全部の表現で中央値 0.40〜0.60。
- どれか ✗ → 読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1** | 最初の 64 token で、層 32 か 48 の残差が結末を J と W の高い方を越えて読むか | E = AUC(L)− max(AUC(J), AUC(W))。L32 か L48 で、E の中央値 ≥ +0.05 かつ 5 % 点 > 0 | 0.15 |
| Q2 | 窓 [0, 16)・[0, 32)・[0, 128)・答えの欄の直前 64 token の AUC と E | 記述(行は窓ごとに使える物だけ) | — |

- L3: 「線 1 の生成の残差は、答えを書く前の最初の 64 token で、答えの欄の結末を、言語化空間(J-lens の読み出し)と語の袋を越えて持つ = 推論空間の候補(行き先)」p = 0.15。
  - 解ける条件: Q1 ✓ で真 / L32・L48 とも E の中央値 ≤ +0.01 で偽 / その間は解けない。
- 動かす主張:
  - **Q1 ✓** → 判定「線 1 で推論空間の候補が在る(行き先・最初の 64 token・層 X・J-lens の読み出しと語の袋を越える)」。
  - **偽** で、J か W の AUC の中央値 ≥ 0.60 → 「結末は最初の 64 token の言語化空間か語の袋で読める = 推論空間はこの形では見えない」。
  - **偽** で、L32・L48・J・W の AUC の中央値がどれも < 0.60 → 「最初の 64 token では、結末は残差でも読めない(この計器で)」。「行き先がまだ決まっていない」とは言わない(読めないだけ)。
  - **間** → 記述。

## §4. 止める規則

- 入口の関門か C0〜C3 のどれかが ✗ → 読まない。この問いの計器の作り直しは、先生に伺ってから。
- 1 回で打ち切る。走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- Q1 ✓ でも「推論」の証明ではない。二語より長い語順・書式・窓の外の位置の性質を残差が持つだけでも越えうる。J は 513 次元の平均で、J-lens の分布の全部ではない。
- 結末は凍結の分類器の答えの欄の label で、model が「決めた」時点は言わない。
- 一つの prompt(F5a-2)・一つの腕(natural)・OLMo-3 32B base の自分の生成。因果・中の状態は言わない。

## §6. 走らせ方(zebrashark・olm87 の `--series` の後)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm88_moy1_inference_space_outcome_from_first_tokens_20261031.py --selftest   # 凍結の前に通した・4 / 4
$P -I exp/olm88_moy1_inference_space_outcome_from_first_tokens_20261031.py --count      # 行と label の数(凍結の後)
$P -I exp/olm88_moy1_inference_space_outcome_from_first_tokens_20261031.py --control
$P -I exp/olm88_moy1_inference_space_outcome_from_first_tokens_20261031.py --read
```
