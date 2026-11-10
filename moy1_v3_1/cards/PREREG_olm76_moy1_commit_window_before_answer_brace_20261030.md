HEAD(R1) = 59871b51(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm76`・凍結 2026-10-30 夜): moy-1(線 1・P1-1)— 答えの欄 `{"` の直前の 64 token の窓で、結びの群(close)と COMMIT の語は上がるか・bind の行で attractor の行より上がるか

- 発注(逐語): 先生 10-30 夜「1 P2-1'の下見をする / 2 同時にすすめられれば進める」(= 主 session の推し「P2-1' の下見までの間に P1-1 を進める」への答え・`p21_prep/MEMO_p21_thinking_text_availability_20261030.md` §3)。P1-1 = `conversations/2026-10-29/PLAN_line1_line2_forward_and_claimable_scope_20261029.md` §3-1。
- G10 の欄: 比べる物 = 「bind の行」/「attractor の行」 / 計器 = olm75 の系列(SAE 層 32 の結びの群 close の係数・J-lens 層 48 の COMMIT の語の log Σ p)を、`{"` の直前の 64 token の窓の後半 32 − 前半 32 の行の中の百分位の差で読む物 / 雛形 = いいえ
- runner = [olm76_…py](../../ConstructGap/exp/olm76_moy1_commit_window_before_answer_brace_20261030.py)。読む物 = olm75 が保存した系列 `ConstructGap/exp/olm75/series/*.npz`(120 行)と olm75 の `read.json`(C1 の的・md5 `13ab2423e3f6cbced77bf03b8a74bb2a`)。
- **凍結し直し(10-30 夜・読みの前)**: 一回目の凍結 b7730f55 の runner は `--control` で numpy の bool を JSON に書けず落ちた(出力の file なし・値は表示される前に落ちた = 見ていない)。runner の `dump` と `print` に numpy の数を Python の数に直す変換を足しただけ(計算・seed・述語は同じ)。G10 の前向きの台帳の行は一回目の凍結のまま(欄は同じ)。
- 柵: forward なし・API なし・Wolfram なし。MacBook で走る。草稿 = `p21_prep/DRAFT_PREREG_p11_commit_window_before_answer_20261030.md`(この版で置き換える)。

## §0. 凍結の前に見た物(開示)

- **行の数**(10-30 夜・`p21_prep/p11_rows.out`): token 5018(`{"`・olm28 の `TOK_BRACE`)が最初に出る位置 p の前に 64 token が収まる行。
  - bind 48(natural 15・think 33)
  - attractor 10(natural 6・think 4)
  - answer の行・stuck の行・flail の行は 0
- **think の行に `</think>`(524・27963・29 の並び)は無い**(bind 36・attractor 4 の全部)。olm4 の commit の窓は think の行で `</think>` の前を使ったが、この 120 行では印は `{"` だけ。
- olm75 の `read.json` の Q2・Q3 の値(bind 53 / attractor 11・中央値・perm_p)は C1 の的として見た(olm75 の RESULT に既に在る)。
- olm75 の読み: 名指しの場面(最初の o_diam / h_diam の前後 32)では、結びの群と COMMIT の語は下がる(Q2 / Q3 ✗・逆向き)。「結び」は答えの欄の手前にしか立たない = 記述(olm4 の別の行から)。
- **系列の値を `{"` の窓で見たことは無い**。合成の自己検査(`--selftest`)は合成の data だけを使った。

## §1. 計器(olm75 の物を選び直さない)

- **u** = 行の中の百分位(olm66 の `pct` の写し・同順位は平均の順位)。
- **窓** = 最初の `{"` の直前の 64 token [p − 64, p)(olm4 の commit の窓と同じ幅)。p ≥ 64 の行だけ。
- **上がり** = 窓の後半 32 [p − 32, p) の u の平均 − 前半 32 [p − 64, p − 32) の u の平均(olm75 の delta と同じ形・答えの欄の中身を含めない)。
- **鍵**: close(SAE 層 32 の結びの群・olm7 / olm59 の凍結の群)と lens_COMMIT(J-lens 層 48・` invariant`・` equality`・` relationships`)。mid・HEDGE・logit の 4 つは記述。

## §2. 統制(R6)

- **C1(写し)**: 写した関数(`pct`・`delta`・`commit_event`・`perm_gt`)で、olm75 の Q2・Q3 の n・中央値・差・perm_p を系列から再現する(中央値は 1e−9 以内・perm_p は一致)。✗ なら読まない。
- **C2(偽の窓)**: 同じ bind の行で、本当の窓と重ならない無作為の位置 τ ∈ [64, p − 64](p ≥ 128 の行・seed 7678)の上がり。
  - 偽の窓で上がりが立つ(符号検定・片側 p < 0.05)鍵の Q1 / Q2 は判定に使わず、記述に下げる。
- **C3(COMMIT の陽性)**: 120 行で、最初の COMMIT の語の位置 h(h ≥ 64)の直前の窓の lens_COMMIT の上がりが正の行が 80 % 以上。
  - ✗ なら Q2・Q4 を判定に使わない(lens が語の手前の上がりを捉えない)。

## §3. 問いと予想(確率は 0〜1・解ける条件)

| Q | 問い | 通る条件(判定) | 予想 p |
|---|---|---|---|
| Q1 | bind の行で、close は `{"` の手前で上がるか | 上がりの中央値 > 0 かつ 符号検定 片側 p < 0.05(n 48)・C2 の close ✓ | 0.55 |
| Q2 | bind の行で、COMMIT の語は `{"` の手前で上がるか | 同上・C2 の COMMIT ✓・C3 ✓ | 0.45 |
| Q3 | close の上がりは bind > attractor か | 中央値の差 > 0・並べ替え検定(2,000 回・seed 7676)片側 p < 0.05・attractor を 1 行ずつ抜いた 10 回の全部で差 > 0(R3 の margin) | 0.30 |
| Q4 | COMMIT の語の上がりは bind > attractor か | Q3 と同じ型(seed 7677)・C3 ✓ | 0.25 |

- 予想の根: olm75 は名指しの場面で両方が下がった(逆向き)。「結びは答えの欄の手前」は olm4(32B・別の行)からの記述で、この 120 行では未測。attractor は 10 行 = Q3・Q4 は小 n で落ちやすい。
- L3(読み・確率つき): 「答えの欄の手前で結びの群が上がる形は、答えへ commit する場面の印として bind に固有」p = 0.30(解ける条件: Q1 ✓ かつ Q3 ✓ で真・Q1 ✗ か Q3 ✗ で偽)。

## §4. 止める規則

- C1 ✗ → 読まない(写しが計器を再現しない)。
- 走行の途中で PREREG と runner を書き換えない(runner の guard が dirty で止める)。

## §5. 言えないこと

- 因果は言わない(並びまで)。SAE は層 32・lens は層 48 = 層が違う。
- 行は olm59 の 120 行(OLMo-3 32B の自分の生成)だけ。frontier の本文では言わない。
- 窓の幅 64 と 32 / 32 の分け方は olm4 / olm75 から継いだ物で、ほかの幅は見ていない。

## §6. 走らせ方

```
cd ConstructGap
python3 -I exp/olm76_moy1_commit_window_before_answer_brace_20261030.py --selftest   # 合成(凍結の前に通した)
python3 -I exp/olm76_moy1_commit_window_before_answer_brace_20261030.py --control    # C1〜C3 → olm76/control.json
python3 -I exp/olm76_moy1_commit_window_before_answer_brace_20261030.py --read       # Q1〜Q4 + 記述 → olm76/read.json
```
