HEAD(R1) = f04f52c0(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親・起案の時と同じ)

# PREREG(札 `olm94`・凍結 2026-11-01): moy-1(線 1・語でない構造を探す・② 合成の prompt)— 変数の束縛(circle P / Q)と添字(the first / second circle)で選んだ円を「this circle」と指す文で、語の袋が構造上読めない指す先を、OLMo-3 32B base の残差が J-lens を越えて持つか。名を書いた直後の形が this circle へ移り、同じ文の別の位置より多く移るか

- 発注(逐語): 先生 11-01「もうちょっとだけ。汎化した推論機構と代数 (指示語、変数、配列) のような構造って見つけられませんか？」→ olm93(① 指示語・自然な生成)= 語の袋が同じかそれ以上に移る・記述「指示語は偶の位置より名の形を多く持つ」→ 主 session の推し「② 合成の prompt(手前の語をそろえる)」→ 先生「**起案する**」→ 草稿を読んで先生「**凍結、発火**」。
- G10 の欄: 比べる物 = 「this circle の位置の層 32・48 の残差で読む、指す先の円の族(直径 O1O2 / HeHi)の AUC」/「同じ位置の J-lens の読み出しと語の袋(32 token・三語・256 token)の AUC(語の袋は文の組の作りで 0.5)」 / 計器 = 文の組(名の組)で分けた正則化つきの logistic の probe(olm84 の推定の型)・移しは olm93 の型 / 雛形 = いいえ
- runner = [olm94_…py](../../ConstructGap/exp/olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.py)。走らせる所 = **zebrashark**。**forward だけ**(生成しない)・API なし。
- 借りる物(写さずに import する):
  - forward = olm4(凍結)の `load_model`・`forward_capture`(olm87 の取り出しと同じ・model = `allenai/Olmo-3-1125-32B`・MLX)。
  - J-lens = olm91(凍結 423602e6)の `lens_tools`・`jfeat`。J の 512 語は、この札の全部の文の全部の位置の J-lens の一位の語の頻度の上位(label を見ない)。
  - 語の袋 = olm84(凍結 728cdca7)の `bow`・olm92(凍結 f396c69a)の `tri`・`bag`・`_index`。
  - 推定 = olm84 の `run_splits`・olm93(凍結 6c38eb97)の `transfer`・`surplus`。

## §0. 凍結の前に見た物(開示)

- olm93 の全部の出力([RESULT](RESULT_olm93_moy1_reference_code_name_to_demonstrative_transfer_20261101.md))。
  - とくに読み 3(名 → 指示語の移しが、名 → 偶の位置より L32 +0.186・J +0.137 高い・語の袋 +0.024)= この札の Q2 の元。
  - 読み 2(P が O の名の印の距離で label を持った)→ この札の W+ には P を入れない。
- 先行の裏取り([RESULT](survey_binding_reference/RESULT_deepresearch_binding_reference_variables_arrays_20261101.md))。束縛の方向(#1)・token 集合の入れ替え(#8)・統語だけの対(#17)の統制の考えを、文の組の作り(名・直径・選びの全部の組の入れ替え)として取り入れた。
- 文の組(runner の `prompts()`)と自己検査:
  - V 型 640・O 型 128。指す先の BIND / ATTR はどちらの型でも、各 group の中でも同数。
  - 全文の単語・二語・三語の数は、group ごとに label と無相関(漏れ 0・`--selftest`)。
- zebrashark(11-01 昼・残差の値と label の組は見ていない):
  - 自己検査 14 / 14(runner の md5 `b281b17f…`)。
  - token の位置の合い 768 / 768。token の数 74〜90・合計 61,504。直径の名の最初の token = ` O`(507)/ ` He`(1283)。
  - forward 3 文で形を見た(層 32・48 = T × 5,120・logits = T × 100,278)。3 文 1.9 s。
  - **設計の確かめ**(残差を使わない・本当の token の語の袋で、V 型の this circle の位置の指す先を読む・統制 C4 と同じ計算): W・W3・T・W+ とも AUC の中央値 0.500 [0.500, 0.500](L1 の罰則がどの重みも残さない)。
- **残差・J-lens・model の出力(行い)の値は、この札の文の上で一度も見ていない**。

## §1. 文・位置・label・表現(R5)

- **文の組**(runner の `prompts()` が唯一の置き場):
  - 共通の頭 = 問題の文脈(K1・K2・O1・O2・He・Hi を入れた 4 通りの言い方)。
  - **V 型(変数の束縛)**: 「Let circle {V1} be the circle with diameter {D1}, and let circle {V2} be the circle with diameter {D2}. Now consider circle {Vs}. {確かめの文} this circle, whose diameter is」。
    - 文脈 2 × 名の組 10(P/Q・A/B・M/N・R/S・U/V・Y/Z・C/D・F/G・L/T・E/W)× 名の順 2 × 直径の順 2 × 選び 2 × 確かめの文 4 = 640。
  - **O 型(添字)**: 「Let the first circle be … {D1}, and let the second circle be … {D2}. {Now consider / We focus on} the {first / second} circle. {確かめの文} this circle, whose diameter is」。
    - 文脈 4 × 直径の順 2 × 選び 2 × 言い方 2 × 確かめの文 4 = 128。
  - {D1, D2} = O1O2(BIND)と HeHi(ATTR)の順の入れ替え。指す先の族 = 選んだ方の直径の族 = 直径の順 xor 選び。
  - 確かめの文 = 「We check whether X1 lies on」「Let us test if X2 is on」「Next we verify that X3 lies on」「We compute the distance from X4 to the center of」。
- **位置**(印の文字を含む token):
  - name = 直径の名の最後の文字(label = その族)。post = 名の直後の `,` / `.`(同じ label)。
  - sel = 選び(V = 変数の名・O = first / second)。ctl = this の直前の語の最後の文字。dem = this circle の circle の最後の文字。この三つの label = 指す先の族(y = 1 ⇔ HeHi)。
  - end = 文の最後(`is`)。行い(Q0)= ここの次の token の logit で、指す先の直径の最初の token(` O` / ` He`)が他方より上か。
- **行**(分け方の単位)= group: V 型 = 名の組(10)・O 型 = 文脈 × 言い方(8)。分け方は group を無作為に半分に分ける(seed 9402・200 回)= 評価の文は、学習で見ていない名の組。
- **表現**: L32・L48 = 層 32・48 の残差。J = J-lens 層 48 の O の集合 + 512 語の log p。W = 直前 32 token の単語 + 二語(L1)。W3 = W + 三語(L1)。T = 直前 256 token(= 文の全体)の単語の袋(L1)。W+ = [W3, T](L1)。**P は入れない**(olm93 の読み 2)。
- **推定**: その場で読む = olm84 の `run_splits`(学習の行で標準化した logistic・C 0.1)。移し = olm93 の `transfer`(一つの半分の group の src の位置で学び、別の半分の group の dst の位置で AUC)。

## §2. 統制(R6)

- **入口の関門**: 768 文が全部取れている。指す先の BIND / ATTR が型ごとに同数。
- **C0(位置の写し)**: 全部の文で、印の token の decode が本文の該当の切れと同じ(空白を除いて)・dem の token が circle の終わり。
- **C1(語の袋の較正・olm93 と同じ型)**: V 型の dem の位置で、窓の単語の有無(在る割合が 0.5 に一番近い単語)を W が読む ≥ 0.95・L32・L48 − W < 0.03。
- **C2(陽性統制)**: V 型の name の位置の中で、名の族を L48 が読む ≥ 0.95。
- **C3(零)**: V 型の dem の位置で、学習の label を group の中で入れ替える(olm84 の perm)。七つの表現の中央値がどれも 0.40〜0.60。
- **C4(作りの確かめ)**: V 型の dem の位置の中で、W・W3・T・W+ の AUC の中央値がどれも ≤ 0.60(語の袋は構造上読めない・§0 で 0.500 を見た)。
- どれか ✗ → 読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | V 型の this circle の位置で、残差は指す先の族を読むか(J と語の袋を越えて) | E = AUC(L)− max(AUC(J), AUC(W), AUC(W+))。L32 か L48 で、AUC の中央値 ≥ 0.70 かつ E の中央値 ≥ +0.05 かつ 5 % 点 > 0。**偽** = L32・L48 とも E の中央値 ≤ +0.01 | 0.50 |
| **Q2** | V 型で、名の直後(post)で学んだ形が this circle へ移り、this の直前の語(ctl)へより多く移るか | L32 か L48 で: post → dem の AUC の中央値 ≥ 0.70・その E ≥ +0.05(5 % 点 > 0)・(post → dem)−(post → ctl)の中央値 ≥ +0.05 かつ 5 % 点 > 0(同じ分け方の差) | 0.20 |
| Q0 | 行い: 文の最後の次の token で、指す先の直径の最初の token が他方より上の割合(V・O) | 記述 | — |
| Q3 | 型を越えた移し(V の dem → O の dem・O → V) | 記述 | — |
| Q4 | sel の位置の中で読む(V・O) | 記述 | — |
| Q5 | name の位置 → dem(名の token そのものから) | 記述 | — |
| Q6 | O 型: dem の中で読む・post → dem / ctl | 記述 | — |
| Q7 | V 型の ctl の位置の中で読む | 記述 | — |

- 関門 p 0.99・C0 p 0.99・C1 p 0.95・C2 p 0.95・C3 p 0.90・C4 p 0.99(§0)。
- L3(Q1):「変数の名で選んだ円を this circle と指す時、OLMo-3 32B base の層 32 か 48 の残差は、指す先の円(直径の族)を線形に持ち、J-lens の読み出しと語の袋を越える」p = 0.50。解ける条件 = Q1 が ✓ で真・偽の線で偽。
- 予想の理由(主 session): 束縛の方向の先行(#1・#5)は、もっと小さい model でも実体と属性の束縛を内部に持つと報告している。ただし dem の位置は「whose diameter is」の前で、model が直径をここで取り出す必要は無い。J-lens は次の一語(`,` など)の分布なので、指す先を持ちにくい見込み。Q2 は、名の直後の形と指示語の形が同じ向きとは限らない(olm93 Q5 の 0.925 は語の袋の効く data の上)。
- 動かす主張:
  - **Q1 ✓** → 「変数の束縛で選んだ円を this circle と指す時、残差は指す先を線形に持つ(語の袋は構造上 0.5・J-lens を越える)= 語でない構造の候補(合成の文・OLMo-3 32B base)」。機構とは書かない。
  - **Q1 偽** → 「この合成の文では、this circle の位置の残差は指す先を J-lens を越えて線形には持たない」。Q0(行い)と並べて読む。
  - **Q2 ✓** → 「名を書いた直後の形が this circle に移り、同じ文の別の位置より多く移る = 指示語の位置で先行詞の形が出し直される候補」(olm93 の読み 3 を判定にする)。
  - Q2 ✗ → 記述。

## §4. 止める規則

- 入口の関門か C0〜C4 のどれかが ✗ → 読まない。作り直しは先生に伺ってから。
- 1 回で打ち切る。走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- 機構とは言わない(介入をしていない)。「変数」「添字」「pointer」は文の組の名で、model の中の型の主張ではない。
- 合成の文は自然な生成と違う(短い・型どおり・model が書いた文ではない)。olm93 の自然な生成への一般化は言わない。
- 一つの model(OLMo-3 32B base)・一つの問題の語彙(O1O2 / HeHi)・層 32 と 48 だけ。「汎化した推論機構」は、この札からは言えない(Q3 は記述・code の変数や配列への移しは別の札)。
- 語の袋が 0.5 なのは、窓の中の三語までの並びと語の数についてだけ。四語より長い並び(「circle Q be the circle with diameter HeHi」)は語の袋に入らない。残差が読む物は、その長い並びの写しでもありうる(それを「束縛」と呼ぶかは定義の問題)。
- J は 513 次元で、J-lens の分布の全部ではない。
- 行い(Q0)は文の最後の一つの位置の logit の比べで、model が「分かっている」とは言わない。

## §6. 走らせ方(zebrashark)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.py --selftest   # 凍結の前に通した・14 / 14
$P -I exp/olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.py --count
$P -I exp/olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.py --capture   # 768 文の forward(約 8〜15 分)・rows は git の外(約 1.3 GB)
$P -I exp/olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.py --control
$P -I exp/olm94_moy1_variable_binding_reference_synthetic_prompts_20261101.py --read
```

- 出力: `olm94/capture.json`(文・位置・decode・行いの margin)・`control.json`・`read.json`・log。`olm94/rows/*.npz`(層 32・48 の全位置)は git の外。
- 時間の見積もり: forward 約 10 分 + 特徴(5,376 位置)+ 推定で、全部で 30 分〜1 時間。
