HEAD(R1) = 98d50e26(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm89`・凍結 2026-10-31 夕): moy-1(線 1・推論空間を探す・olm86 の記述の確かめ)— 新しい 200 行で、O の名を新しく名指す 8 token 前の残差(層 32・48)が、同じ位置の J-lens の読み出しと語の袋を越えて「8 token 先に O の名」を読むか

- 発注(逐語): 先生 10-31 夕「1から順に進めましょう」→ 主 session の問いの中の一文「増やした行は、olm86 で記述に出た『k = 8 で残差が J-lens を +0.036 上回る』を、k = 8 を主にした別の data で確かめるのにも使えます」→ 先生の選び「F5a-2 natural 200 行 (Recommended)」。
- G10 の欄: 比べる物 = 「層 32 と 48 の残差」/「J-lens の読み出しと語の袋」 / 計器 = 行で分けた正則化つきの logistic の probe の AUC(O の名を新しく名指す 8 token 前の位置 対 同じ行の先 128 token に O の名が無い位置) / 雛形 = いいえ
- runner = [olm89_…py](../../ConstructGap/exp/olm89_moy1_inference_space_k8_lookahead_replication_new_rows_20261031.py)。走らせる所 = **zebrashark**。forward なし・API なし。
- data = **olm87 の新しい 200 行**(凍結 6e81795b・この札の凍結の時は生成の途中)。
- **olm86 から替えたのは data・主の k(32 → 8)・k の一覧(1・8・16・32)・seed だけ**。
  - 出来事と負の述語は olm86(凍結 38896688)の `fresh_events`・`neg_candidates` を import(前 95 token に名が無い・負 = 窓にも先 128 token にも名が無い・行ごとに出来事の 4 倍)。
  - 推定と分け直しは olm84(凍結 728cdca7)の `run_splits`。J-lens の道具は olm88(凍結 d7eba25d)。

## §0. 凍結の前に見た物(開示)

- olm86 の全部の出力(RESULT 1500b50e)。k = 8 で E(L32)+0.036(5 % 点 +0.017)・E(L48)+0.033(+0.013)。AUC: L32 0.944・L48 0.940・J 0.906・W 0.815。olm86 は think 40 行と natural 19 行を混ぜた数で、k = 8 の腕ごとの数は出していない。
  - → この札の線(+0.02)は、olm86 の k = 8 の値を見てから置いた。だから「確かめ」の線で、推論空間の候補の線(+0.05)とは分けて書く。
- **olm87 の出力は何も見ていない**(olm88 の PREREG §0 と同じ)。
- 自己検査(`--selftest` 4 / 4)。
- 道筋の確かめ(zebrashark・10-31 夕): 既存の 3 行(olm7 の残差 + olm66 の印 + olm65 の系列を一時に合わせた物)で、特徴の形と C0 の写しだけを見た(差は最大 7.6e−6)。label と値の組み合わせは見ていない。

## §1. 行・位置・表現(R5)

- 行 = olm87 の series の行で、出来事が 1 つ以上・負の候補が 1 つ以上の物(答えから始めた行も、述語が拾えば入る)。
- 出来事・正・負は olm86 §1 と同じ述語。正 = j − k(k = 1・**8**・16・32)。負は行ごとに出来事の数 × 4(seed 8901)。
- 表現 = olm86 と同じ式: L32・L48(olm87 の traj)・J(J-lens 層 48 の O の集合 + 512 語の log p・語は olm88 の `vocab_pool`)・W(直前 32 token の単語 + 二語・L1)。

## §2. 統制(R6・線は olm86 と同じ)

- **入口の関門**: olm87 の G1 と G2 が通り、k = 8 の出来事が 100 以上。
- **C0**: J の O の値が olm87 の `lens_O` と 1e−3 以内 ≥ 99 %。
- **C1**: 語で決まる label(k = 8 の位置の集合で窓に在る割合が 0.5 に一番近い単語の有無)で、W ≥ 0.95、かつ L32・L48 − W < 0.03。
- **C2**: k = 1 で L48 の AUC の中央値 ≥ 0.90。
- **C3**: 偽の正の零(各行の負から、その行の k = 8 の正の数だけ・seed 8902)で、全部の表現の中央値 0.40〜0.60。
- どれか ✗ → 読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(確かめ)** | k = 8 で、層 32 か 48 の残差が J と W の高い方を上回り続けるか | E = AUC(L)− max(AUC(J), AUC(W))。L32 か L48 で、E の中央値 ≥ **+0.02** かつ 5 % 点 > 0 | 0.40 |
| **Q1b(推論空間の線)** | 同じで、線 +0.05 | E の中央値 ≥ **+0.05** かつ 5 % 点 > 0 | 0.10 |
| Q2 | k = 1・16・32 の AUC と E | 記述 | — |

- 動かす主張:
  - **Q1b ✓** → 判定「線 1 で推論空間の候補が在る(新しい O の名の 8 token 前・層 X・J-lens の読み出しと語の袋を越える・二つの data で)」。
  - **Q1 ✓・Q1b ✗** → 「olm86 の k = 8 の上乗せは、新しい行でも出る(+0.02 以上・5 % 点 > 0)。ただし推論空間の候補の線(+0.05)には届かない」= 記述の格を上げるが、推論空間の候補とは書かない。
  - **Q1 ✗** で、L32・L48 とも E の中央値 ≤ +0.01 → 「olm86 の k = 8 の上乗せは、新しい行では出ない」= olm86 の記述は再現しない。
  - その間 → 記述。

## §4. 止める規則

- 入口の関門か C0〜C3 のどれかが ✗ → 読まない。作り直しは先生に伺ってから。
- 1 回で打ち切る。走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- Q1b ✓ でも「推論」の証明ではない(olm86 §5 と同じ: 二語より長い語順・書式・段の話題を残差が持つだけでも越えうる・J は 513 次元)。
- olm86 は think と natural を混ぜた数、この札は natural だけ。腕の違いで値が動いても、この札では分けて言えない。
- 一つの prompt(F5a-2)・OLMo-3 32B base の自分の生成。因果・中の状態は言わない。

## §6. 走らせ方(zebrashark・olm87 の `--series` の後)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm89_moy1_inference_space_k8_lookahead_replication_new_rows_20261031.py --selftest   # 凍結の前に通した・4 / 4
$P -I exp/olm89_moy1_inference_space_k8_lookahead_replication_new_rows_20261031.py --count
$P -I exp/olm89_moy1_inference_space_k8_lookahead_replication_new_rows_20261031.py --control
$P -I exp/olm89_moy1_inference_space_k8_lookahead_replication_new_rows_20261031.py --read
```
