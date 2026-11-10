HEAD(R1) = 246a8cc5(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)。起案の時の HEAD = 9f4c9784

# PREREG(札 `olm98`・凍結 2026-11-01): moy-1(線 1・語でない構造を探す・④ attention head)— olm94 の変数の束縛の文で、文の最後の位置の行い(指す先の直径の最初の token − 他方)を運ぶ head はどれか。その head は、指す先の直径の名・this circle・選びの語のどこを読むか。その head の出力を対の文の物に置くと行いが入れ替わるか

- 発注(逐語): 先生 11-01「attention patternとかattention headの組って具体的にはどうやってるんだろう？」→ 主 session の説明(注意の重み・DLA・head の patching・path patching)と推し(olm95 の結果の後に head の札)→ 先生「**attention head の札を起案する。**」→ 草稿の §4 の三つを伺った後、先生「**推しの順で進みます。**」= 草稿の案(Q1 と Q2 の両方・上位 10・最後の位置だけ・約 2,500 回)のまま凍結する(主 session がそう読んだ・凍結の前に先生に伝えた)
- G10 の欄: 比べる物 = 「文の最後の位置で直接の寄与が大きい上位 10 head の、指す先の直径の名への注意 / 他方の直径の名への注意 と、その 10 head の出力を対の文の物に置いた時の行いの動き」/「同じ数の乱数の head の組の出力を置いた時の動き・this circle と選びの語への注意」 / 計器 = 手で開いた forward(OLMo-3 の式)の、最後の位置の注意の重みと head ごとの直接の寄与(norm の大きさを固定した一次の分解)と、head の出力の置き換え / 雛形 = いいえ
- runner = [olm98_…py](../../ConstructGap/exp/olm98_moy1_heads_reading_the_referent_at_final_position_20261101.py)。走らせる所 = zebrashark。forward だけ・API なし。
- data = olm94 の V 型 640 文(capture.json・位置)。分け方 = olm95 と同じ(学習 V0・V1・V2・V5・V8 / 評価 V3・V4・V6・V7・V9)。対の文 = olm95 の `twins`(選びの文字だけが違う)。

## §0. 起案の前に見た物(開示)

- olm94(RESULT)・olm95(RESULT・C2 ✗ で読まない・fire.json は開けていない)。
- **olm97 の全部の出力**(凍結の前に終わった・統制 ✓ 全部・Q1 = 偽): this circle の一つの位置(層 32)の向きの差し替え・量 2 / 4 倍・層 48・一つの位置(dem・ctl・sel)をまるごと対の文の物に置く、のどれも行いの効きの中央値 0.0 logit。選びから最後までをまとめて置くと 308 / 308 で反転(4.40 logit)= 層 32 では、指す先は最後の位置まで運ばれ終わっている見込み。この札の head の置き換えは最後の位置で全層に当てるので、運ぶ head の層を問える。
- 札 cmt10〜15(F5a-2 の行の DLA で「O の組 = L57H33・L34H3・L52H26・L51H4」「He の組 = L50H23・L51H19・L43H24・L42H33」・RESULT_cmt13)。この札の文は合成の文で、cmt13 の行とは違う。
- MLX の OLMo-3 の式(mlx_lm `olmo3.py`): 64 層・40 head(key / value は 8 組 = 5 head ずつ共有)・head の次元 128・attention の出力は o_proj の後に post_attention_layernorm を通して残差へ・16 層ごとに全文の層・ほかは窓 4096(この札の文は 85 token 前後なので、どの層も全文を見る)。
- 先行の調べ(論理ゲートの共有・DAS と層ごとの比べ): head の水準の因果は patching で確かめる・DLA は一次で因果でない・解釈の錯覚(部分空間)。

## §1. 計器(R5)

- **手で開いた forward**(`forward_heads`): 各層で q / k の正規化 → RoPE → key / value を 5 head に写す → 注意の重み(float32 の softmax・因果の mask)→ head の出力 → o_proj → post_attention_layernorm → 残差。MLP の側は model の部品をそのまま呼ぶ。
  - 最後の位置で取る物: head の出力(40 × 128・o_proj の前)・最後の位置からの注意の重み(40 × T)・post_attention_layernorm の 1 / rms(層ごと)。
- **head ごとの直接の寄与(DLA)**: c_h = w_post ⊙ s_post · W_o[:, h] o_h を、最後の norm(大きさを最後の位置で固定)を通して unembed の差(指す先の直径の最初の token − 他方)へ。cmt10〜15 と同じ一次の分解。
- **区間**(文字の区間に掛かる token): 指す先の直径の名(ref)・他方の直径の名(oth)・this circle(dem)・選びの文字(sel)・this の直前の語(ctl)・定義の中の二つの変数の文字(v_letters)・最後の位置(self)・残り(rest)。注意の重みを区間ごとに足す。
- **上位の head**: 学習の組で、DLA の中央値(指す先の側を正)の上位 10 head。評価の組はこの選びに使わない。
- **head の置き換え**(評価の組): 最後の位置の、その head の出力(o_proj の前)を、対の文の同じ head の出力に置く。上位 10 head をまとめて / 乱数の 10 head の組 × 3(seed 9801)/ 下位 10 head。効き e = margin(置かない)− margin(置く)。

## §2. 統制

- **C0(再現)**: 手で開いた forward の margin が olm94 の margin と 0.25 logit 以内 ≥ 95 %(float32 の softmax と model の bf16 の SDPA の違いを見込む・凍結の前に 3 文で見る)。
- **C0b(分解)**: 各層の head の寄与の和 = その層の attention の出力(最後の位置・norm の大きさを固定)が 1e−2 以内。
- **C1(陽性統制)**: 最後の位置の全 head(64 層 × 40)の出力を対の文の物に置くと反転 ≥ 0.90(§4b で、対の文の logits を差 0.0 で再現することを見た)。
- **C2(零)**: 乱数の 10 head の組の効きの中央値 |e| ≤ 0.5 logit。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1** | 上位 10 head(学習の組で選ぶ)は、評価の組で、指す先の直径の名を他方の直径の名より多く読むか | 10 head の注意の和の比(ref / oth)の中央値 ≥ 2.0 かつ、文ごとの対の差(ref − oth)の 5 % 点 > 0 | 0.55 |
| **Q2** | 上位 10 head の出力を対の文の物に置くと、行いが他方へ動くか(乱数の 10 head の組より大きく) | e の中央値 ≥ +0.5 logit・[e(上位)− 乱数 3 組の e の平均] の中央値 ≥ +0.25 かつ bootstrap の 5 % 点 > 0 | 0.45 |
| Q3 | 上位の head が this circle・選びの語・名の文字を読む割合(記述) | 記述 | — |
| Q4 | 上位の head の層の分布と、cmt13 の head(L57H33・L50H23 ほか)との重なり(記述) | 記述 | — |
| Q5 | this circle を一番多く読む head はどれで、その DLA はどれだけか(記述) | 記述 | — |

- 予想の理由(主 session): 先行の「取り出しは位置・語・直接の pointer の混合」(Gur-Arieh ら)と lookback(Prakash ら)の型なら、最後の位置の取り出しの head は、束縛を解いた上で指す先の値(直径の名)を直接読む見込みが大きい(Q1)。ただし行いを運ぶ head は複数の組に分かれうるので、10 head の置き換えだけでは補われうる(Q2)。

## §4. 決めたこと・止める規則

- 主の問い = Q1 と Q2 の両方(どちらも判定)。上位 = 10・置き換えは最後の位置だけ(全層の head)。
- 予算 = 記録 640 回(1 回 約 2.5 s)+ 置き換え 320 文 × 6 回(上位・下位・乱数 3 組・全 head = 陽性統制・1 回 約 1.3 s)= 2,560 回・約 70 分。
- 統制(C0・C0b・C1・C2)のどれかが ✗ → 読まない。作り直しは先生に伺ってから。1 回で打ち切る。

## §4b. 凍結の前の確かめ(zebrashark・3 文・効きと上位の head は見ていない)

- config: o_proj の bias なし(attention_bias = False)・unembed は lm_head(tie なし)。
- 手で開いた forward の margin と olm94 の margin の差: 0.031・0.000・0.094 logit(C0 の線 0.25 の内)。
- head の寄与の和と o_proj の出力(最後の位置)の相対差: 0.0024・0.0024・0.0023(C0b の線 0.01 の内)。
- 全 head を対の文の物に置いた最後の logits と、対の文の logits の差: 0.0(C1 の作りが正しい)。
- 自己検査 7 / 7。

## §5. 言えないこと

- DLA は一次の分解で因果でない(Q2 の置き換えで因果を見る)。注意の重みは「どこを読むか」で「何を写すか」ではない(OV は見ない)。
- 上位 10 head を「回路」とは言わない(head の間の道は path patching をしていない)。
- 合成の文・一つの model・V 型だけ。
