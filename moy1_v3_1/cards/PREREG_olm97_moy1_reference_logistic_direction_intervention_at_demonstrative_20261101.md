HEAD(R1) = badd1485(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm97`・凍結 2026-11-01): moy-1(線 1・語でない構造を探す・③ 介入の作り直し)— olm95 の向きを olm94 Q2 と同じ logistic の向きに替え、this circle の位置で他方の族へ差し替えると行いが他方へ動くか。乱数の向き・this の直前の語への同じ差し込みより大きく動くか

- 発注(逐語): olm95 の RESULT(C2 ✗ = 平均の差の向きの射影 0.882 < 0.90・読まない)→ 主 session の案 (A) / (B) / (C) → 先生「**olm95 A で作り直す**」。
- G10 の欄: 比べる物 = 「this circle の位置で、名の直後の logistic の向き(層 32)の射影を他方の族の平均へ差し替えた時の、行いの margin の動き」/「同じ大きさの乱数の向き(this circle で)と、同じ差し込みを this の直前の語にした時の動き」 / 計器 = 文の最後の次の token の logit の差(指す先の直径の最初の token − 他方)・評価の名の組 5 組(320 文)の中央値と bootstrap の 5 % 点 / 雛形 = いいえ
- runner = [olm97_…py](../../ConstructGap/exp/olm97_moy1_reference_logistic_direction_intervention_at_demonstrative_20261101.py)。走らせる所 = **zebrashark**。forward だけ・API なし。
- **olm95(凍結 4502a4a6)の写し**。替えたのは**向きの推定だけ**:
  - olm95 = 名の直後の残差の平均の差。
  - olm97 = 名の直後の位置で、学習の行で標準化した logistic(olm84 の `logit_fit`・C 0.1・L2 = olm94 Q2 と同じ推定)の重み w を、残差の空間の向き w / σ に戻して長さ 1 にした物。
- 道具・分け方・対の文・介入の組・行い・数える文・統制・Q1〜Q5 の線は、olm95 の物を import して使う(`forward_edit`・`split_groups`・`twins`・`swap_vec`・`rand_dirs`・`boot_lo`・`margin`・`eff`・`control`・`read`)。`control`・`read` は、olm95 の `FIRE` をこの札の `fire.json` に向けてから呼ぶ。
- data = olm94(凍結 ae474dc3)の `capture.json` と `rows`(zebrashark・git の外)。V 型だけ。分け方 = olm95 と同じ(学習 V0・V1・V2・V5・V8 / 評価 V3・V4・V6・V7・V9)。

## §0. 凍結の前に見た物(開示)

- olm95 の `control.json` と `read.json`([RESULT](RESULT_olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.md))= 平均の差の向きの評価の組での射影 AUC 0.882・C0・C1・C3 の値。
- **olm95 の `fire.json`(評価の組の文ごとの介入の margin)は、主 session は開けていない**。この札の向きでの評価の組の値も、一度も見ていない。
- **C2 の較正(凍結の前・学習の組だけ・`--precal`)**: 学習の 5 組で 1 組を外し、残り 4 組の名の直後で logistic の向きを作り、外した組の this circle の射影の AUC を見た = V0 0.949・V1 0.962・V2 0.964・V5 0.979・V8 0.970(最小 0.949・中央値 0.964)= 線 0.90 の上。
- 自己検査(`--selftest` 4 / 4・zebrashark・runner の md5 `210634ca…`)。合成の例が弱くて一度 NG を出し(分ける次元の差が雑音に埋もれる作り)、作りを強めて通した。
- olm95 の道筋の確かめ(forward_edit が olm94 を差 0.0 で再現・C0 で 320 / 320)は、この札でもそのまま使う道具。

## §1〜§2(olm95 と同じ・違いだけ書く)

- 向き = 上の logistic の向き(層 32 と 48・学習の組の名の直後の位置 = post1・post2)。
- μ = this circle の位置のその向きへの射影の、族ごとの平均(学習の組)。
- 介入・行い・効き e・数える文・統制 C0〜C3・Q1〜Q5 の定義と線は、olm95 の PREREG §1〜§3 のまま([PREREG_olm95](PREREG_olm95_moy1_reference_direction_intervention_at_demonstrative_20261101.md))。
  - C0: 書き換え無しの forward の margin・残差が olm94 と 0.05 以内 ≥ 99 %。
  - C1: 選びから後をまるごと対の文に置いて反転 ≥ 0.90。
  - **C2: 評価の組の this circle の射影が、指す先の族を AUC ≥ 0.90 で分ける**(§0 の較正で、学習の組の中では 0.949〜0.979)。
  - C3: 乱数の向きの |効き| の中央値 ≤ 0.5 logit。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | this circle の位置で名の直後の logistic の向き(層 32)を他方へ差し替えると、行いが他方へ動くか。乱数の向きと、this の直前の語への同じ差し込みより大きく | olm95 と同じ: **✓** = e(dem_dir)の中央値 ≥ +0.5 logit・[e(dem_dir)− 乱数 4 本の e の平均] の中央値 ≥ +0.25 かつ bootstrap の 5 % 点 > 0・[e(dem_dir)− e(ctl_dir)] の中央値 ≥ +0.25 かつ 5 % 点 > 0。**偽** = e(dem_dir)の中央値 < +0.1。ほか =「間」 | ✓ 0.30・偽 0.35・間 0.35 |
| Q2〜Q5 | olm95 と同じ記述(一つの位置をまるごと置く・量・層 48・族ごと) | 記述 | — |

- C0 p 0.99・C1 p 0.95・C2 p 0.85(学習の組では 0.949〜0.979)・C3 p 0.90。
- L3:「this circle の位置の、名の直後と同じ logistic の向き(層 32)は、model の行い(どちらの直径を続けるか)に効く。差し替えで他方へ動き、その動きは同じ大きさの乱数の向きと、this の直前の語への同じ差し込みより大きい」p = 0.30。解ける条件 = Q1 が ✓ で真・偽で偽。
- 予想の理由(主 session): olm95 と同じ(選びの位置・this の直前の語にも指す先が在り、一つの位置の差し替えは補われうる)。
- 動かす主張: olm95 の PREREG §3 と同じ文(✓ = 機構の候補・偽 = 「この向きを this circle の一つの位置で差し替えても、行いは動かない(この介入で)」・間 = 記述)。

## §4. 止める規則

- C0〜C3 のどれかが ✗ → 読まない。作り直しは先生に伺ってから。
- 1 回で打ち切る。走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- olm95 の PREREG §5 のまま(機構はこの向き・位置・層・行いの組の因果まで・合成の文・一つの model・V 型だけ)。
- logistic の向きは、名の直後で族を分ける向きの一つで、名の直後の情報の全部ではない。平均の差の向き(olm95)との違いは、この札では比べない(olm95 は読んでいない)。

## §6. 走らせ方(zebrashark)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm97_moy1_reference_logistic_direction_intervention_at_demonstrative_20261101.py --selftest   # 凍結の前に通した・4 / 4
$P -I exp/olm97_moy1_reference_logistic_direction_intervention_at_demonstrative_20261101.py --precal     # 凍結の前に当てた(§0)
$P -I exp/olm97_moy1_reference_logistic_direction_intervention_at_demonstrative_20261101.py --fire       # 320 文 × 14 回(約 50 分)
$P -I exp/olm97_moy1_reference_logistic_direction_intervention_at_demonstrative_20261101.py --control
$P -I exp/olm97_moy1_reference_logistic_direction_intervention_at_demonstrative_20261101.py --read
```
