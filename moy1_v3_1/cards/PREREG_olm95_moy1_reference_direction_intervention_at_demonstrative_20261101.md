HEAD(R1) = 14b755ee(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm95`・凍結 2026-11-01): moy-1(線 1・語でない構造を探す・③ 介入)— olm94 の変数の束縛の文で、名を書いた直後の向き(層 32)を this circle の位置で他方の族へ差し替えると、model の行い(どちらの直径を続けるか)が他方へ動くか。同じ大きさの乱数の向き・this の直前の語への同じ差し込みより大きく動くか

- 発注(逐語): olm94 の RESULT(Q2 ✓ = this circle の位置で名の直後と同じ形が出し直される)→ 主 session の推し「③ 介入」→ 先生「**介入してみましょう**」。
- G10 の欄: 比べる物 = 「this circle の位置で、名の直後の向き(層 32)の射影を他方の族の平均へ差し替えた時の、行いの margin の動き」/「同じ大きさの乱数の向き(this circle で)と、同じ差し込みを this の直前の語にした時の動き」 / 計器 = 文の最後の次の token の logit の差(指す先の直径の最初の token − 他方)・評価の名の組 5 組(320 文)の中央値と bootstrap の 5 % 点 / 雛形 = いいえ
- runner = [olm95_…py](../../ConstructGap/exp/olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.py)。走らせる所 = **zebrashark**。forward だけ・API なし。
- data = olm94(凍結 ae474dc3)の `capture.json`(文・位置・行いの margin)と `rows`(層 32・48 の全位置・zebrashark・git の外)。V 型だけ。
- forward = olm4(凍結)の `forward_capture` と同じ流れに、層 L の block の出力への書き換え(足す / 置く)を足した `forward_edit`。

## §0. 凍結の前に見た物(開示)

- olm94 の全部の出力([RESULT](RESULT_olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.md))。とくに Q2(名の直後 → this circle の移し L32 0.970・this の直前の語へ 0.603)と、this の直前の語・選びの位置でもその場で読めば 1.000(Q4・Q7)。
- 自己検査(`--selftest` 9 / 9・runner の md5 `f46b0a96…`)。
- zebrashark の道筋の確かめ(11-01 昼・評価の組の 3 文): 書き換え無しの forward は olm94 の margin と層 32 の this circle の残差を差 0.0 で再現・0 を足す書き換えは logits を変えない(差 0.0)・forward 1 回 0.6 s。
- **介入した時の margin は、どの文でも一度も見ていない**。向き(平均の差)と平均の値も、まだ計算していない。

## §1. 分け方・向き・介入(R5)

- **分け方**: V 型の名の組 10 を一度だけ分ける(seed 9501)= 学習 V0・V1・V2・V5・V8 / 評価 V3・V4・V6・V7・V9(各 64 文・評価 320 文)。
- **向き**(層 L = 32・48、学習の組だけ): 名の直後の位置(post1・post2)の残差の平均の差(ATTR − BIND)を長さ 1 にした d̂_L。
  - this circle の位置の d̂_L への射影の、族ごとの平均 μ_L(BIND)・μ_L(ATTR)(学習の組)。
- **対の文**: 選びだけが違う文(本文の違いは選びの文字一つ・指す先が逆)。
- **介入**(評価の各文・層 L の block の出力に当てる・一回に一つ):
  - `dem_dir`(主): this circle の位置で、d̂_32 への射影を他方の族の μ へ置く(足す vector = (μ_他方 − h·d̂) d̂)。
  - `ctl_dir`: 同じ vector を this の直前の語の位置に足す。
  - `dem_rand0〜3`: this circle の位置に、同じ長さの乱数の向き(seed 9502・4 本)を足す。
  - `dem_dir_x2`・`dem_dir_x4`: dem_dir の vector の 2・4 倍(記述)。
  - `dem_full`・`ctl_full`・`sel_full`: その一つの位置の層 32 の残差を、対の文の物にまるごと置く(記述)。
  - `pos_ctrl`: 選びの位置から文の最後までの層 32 の残差を、対の文の物にまるごと置く(陽性統制)。
  - `dem_dir_L48`: 層 48 で同じ射影の差し替え(記述)。
- **行い**: 文の最後(「…this circle, whose diameter is」)の次の token の logit で、margin = 指す先の直径の最初の token(` O` 507 / ` He` 1283)− 他方。
- **効き** e = margin(書き換え無し)− margin(介入)。正 = 他方の円へ動いた。**反転** = 介入の後の margin < 0。
- **数える文**: 評価の文のうち、書き換え無しの margin > 0 で、対の文の olm94 の margin も > 0 の物(行いが両方で正しい文)。

## §2. 統制(R6)

- **C0(再現)**: 書き換え無しの forward の margin が olm94 の margin と 0.05 以内・層 32 の this circle の残差が olm94 の rows と 0.05 以内、がどちらも ≥ 99 % の文。
- **C1(陽性統制)**: `pos_ctrl` で反転する割合 ≥ 0.90(数える文の中)。
- **C2(向きが評価の文でも分ける)**: 評価の文の this circle の層 32 の残差の d̂_32 への射影が、指す先の族を AUC ≥ 0.90 で分ける(学習なし)。
- **C3(乱数の向きが壊さない)**: 乱数の向きの効き |e| の中央値 ≤ 0.5 logit。
- どれか ✗ → 読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | this circle の位置で名の直後の向き(層 32)を他方へ差し替えると、行いが他方へ動くか。乱数の向きと、this の直前の語への同じ差し込みより大きく | **✓** = e(dem_dir)の中央値 ≥ +0.5 logit・[e(dem_dir)− 乱数 4 本の e の平均] の中央値 ≥ +0.25 かつ bootstrap の 5 % 点 > 0・[e(dem_dir)− e(ctl_dir)] の中央値 ≥ +0.25 かつ 5 % 点 > 0(文ごとの対の差)。**偽** = e(dem_dir)の中央値 < +0.1。ほか =「間」 | ✓ 0.30・偽 0.35・間 0.35 |
| Q2 | 一つの位置をまるごと対の文の物に置く(dem・ctl・sel)と pos_ctrl の効きと反転 | 記述 | — |
| Q3 | 量: dem_dir の 1・2・4 倍の効きと反転 | 記述 | — |
| Q4 | 層 48 の射影の差し替え | 記述 | — |
| Q5 | 指す先の族ごとの e(dem_dir) | 記述 | — |

- C0 p 0.99(§0 で差 0.0)・C1 p 0.95・C2 p 0.90・C3 p 0.90。
- L3:「this circle の位置の、名の直後と同じ向き(層 32)は、model の行い(どちらの直径を続けるか)に効く。差し替えで他方へ動き、その動きは同じ大きさの乱数の向きと、this の直前の語への同じ差し込みより大きい」p = 0.30。解ける条件 = Q1 が ✓ で真・偽で偽。
- 予想の理由(主 session): olm94 では、選びの位置・this の直前の語でも指す先がその場で 1.000 読めた。文の最後はそれらの位置からも指す先を取れるので、this circle の一つの位置・一つの向きの差し替えは、ほかの位置に補われて小さく出る見込みが大きい。
- 動かす主張:
  - **✓** → 「this circle の位置の、名の直後と同じ向き(層 32)を差し替えると、行いが他方の円へ動く(乱数の向き・this の直前の語より大きく)= 指示語の位置の先行詞の形は、行いに効く(合成の文・一つの位置の介入)」= 機構の候補。
  - **偽** → 「この向きを this circle の一つの位置で差し替えても、行いは動かない(この介入で)」。形が行いに使われていないとは言わない(ほかの位置が補いうる・Q2 を並べて読む)。
  - **間** → 記述。

## §4. 止める規則

- C0〜C3 のどれかが ✗ → 読まない。作り直しは先生に伺ってから。
- 1 回で打ち切る。走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- 「機構」は、この向き・この位置・この層・この行いの組での因果の効きまで。回路(どの head が読むか)は言わない。
- 向きは平均の差で、probe の重みではない。olm94 の Q2 の logistic の向きと同じとは言わない(C2 は分けることだけを確かめる)。
- 乱数の向きは 4 本。量は射影の差し替え(1 倍)を主にした。ほかの量は記述。
- 合成の文・一つの model・V 型だけ。自然な生成と O 型(序数)への一般化は言わない。
- 行いは文の最後の一つの位置の logit の比べで、model が「分かっている」とは言わない。

## §6. 走らせ方(zebrashark)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.py --selftest   # 凍結の前に通した・9 / 9
$P -I exp/olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.py --count
$P -I exp/olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.py --fire      # 320 文 × 14 回の forward(約 45 分)
$P -I exp/olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.py --control
$P -I exp/olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.py --read
```

- 出力: `olm95/fire.json`(文ごとの margin・介入ごと・向きの md5・平均)・`control.json`・`read.json`・log。
