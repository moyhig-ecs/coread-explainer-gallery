HEAD(R1) = d7fbbd43(走行の時の HEAD = 凍結し直しの commit・dirty なし)

# RESULT(札 `olm76`・2026-10-30 夜・MacBook): moy-1(線 1・P1-1)— 答えの欄 `{"` の直前の 64 token の窓で、結びの群は bind の行で上がらず、attractor の行より上がらない(Q1 ✗・Q3 ✗)・COMMIT の語は統制 C3 が 1 行足りず記述

- 凍結 = [PREREG](PREREG_olm76_moy1_commit_window_before_answer_brace_20261030.md)(b7730f55 → 凍結し直し d7fbbd43 = 出力の変換だけ・読みの前)・runner = [olm76_…py](../../ConstructGap/exp/olm76_moy1_commit_window_before_answer_brace_20261030.py)(md5 `a07fd5ef…`)。
- 出力 = `ConstructGap/exp/olm76/control.json`(md5 `d549184e…`)・`ConstructGap/exp/olm76/read.json`(md5 `1d39c27a…`)。prov = commit d7fbbd43・dirty false・prereg md5 `509fd5dc…`・olm75 の read.json md5 `13ab2423…`。
- forward なし・API なし(olm75 が保存した系列を読むだけ)。

## 判定のまとめ

| | 判定 | 実出力 |
|---|---|---|
| C1 写し | ✓ | olm75 の Q2(53 / 11・中央値 −0.1335 / −0.0062・差 −0.1273・perm_p 0.9875)と Q3(−0.0520 / +0.0113・差 −0.0634・perm_p 0.9635)を全部の桁で再現 |
| C2 偽の窓 | ✓(close・COMMIT とも) | bind 48 行の無作為の窓: close 21 / 48 正・中央値 −0.0335・符号検定 p 0.844 / COMMIT 24 / 48・+0.0006・p 0.557 |
| C3 COMMIT の陽性 | **✗** | 最初の COMMIT の語の手前の窓で上がる行 14 / 18 = 77.8 %(線 80 % = 15 / 18 に 1 行足りない)→ Q2・Q4 は判定に使わない |
| **Q1** bind で close が上がる | **✗**(予想 p 0.55) | 28 / 48 正・中央値 +0.0127・符号検定 片側 p 0.156 |
| Q2 bind で COMMIT が上がる | 記述(C3 ✗) | 18 / 48 正・中央値 −0.0244・p 0.970 |
| **Q3** close: bind > attractor | **✗**(予想 p 0.30) | 中央値 bind +0.0127 / attractor +0.0425・差 −0.0298・perm_p 0.834・1 行抜き 0 / 10 で差 > 0 |
| Q4 COMMIT: bind > attractor | 記述(C3 ✗) | bind −0.0244 / attractor +0.0146・差 −0.0390・perm_p 0.718・1 行抜き 0 / 10 |
| L3「答えの欄の手前で結びの群が上がる形は bind に固有」 | **偽**(p 0.30・解ける条件 = Q1 ✓ かつ Q3 ✓) | Q1 ✗ |

## 記述(判定に使わない)

- 全部の鍵の上がりの中央値(bind 48 / attractor 10・正の行の数):
  - close: +0.0127(28)/ +0.0425(7)
  - mid: +0.0006(24)/ +0.0042(5)
  - lens COMMIT: −0.0244(18)/ +0.0146(6)
  - lens HEDGE: −0.0391(14)/ −0.0502(2)
  - logit COMMIT: −0.0066(23)/ +0.0307(6)
  - logit HEDGE: −0.0121(21)/ −0.0209(4)
- 腕ごと(close の中央値 / COMMIT の中央値):
  - natural: bind 15 行 +0.0014 / −0.0587・attractor 6 行 +0.0548 / −0.0655
  - think: bind 33 行 +0.0254 / −0.0221・attractor 4 行 +0.0262 / +0.0309

## 読み

1. **答えの欄の手前の窓でも、結びの群は bind の行で立たない**(Q1 ✗・偽の窓と同じ幅の中)。olm75 の名指しの場面(下がる)に続いて、答えの欄の手前でも「結び」の印は bind の行に出ない。olm75 の記述「結びは答えの欄の手前にしか立たない」は、この 120 行では判定に上がらない(olm4 の別の行の記述のまま)。
2. bind と attractor の差(上がりの中央値):
   - 結び・中点・COMMIT(lens・logit)の 4 鍵では bind の方が小さい。
   - HEDGE(lens・logit)の 2 鍵では bind の方が大きい(−0.0391 対 −0.0502・−0.0121 対 −0.0209 = どちらも下がりの幅が bind で小さい)。
   - 判定は Q3(close)だけで ✗。attractor は 10 行で、close の差の向き(bind < attractor)は 1 行抜きの 10 回の全部で変わらない。
3. COMMIT の語は、語の手前で lens が上がる陽性統制が 14 / 18 で線に届かない = この lens の語の集合は「語の手前の上がり」を測る計器として 80 % の線を越えない。Q2・Q4 は記述まで。

## 言えないこと

- 因果は言わない。層 32 の SAE と層 48 の lens は層が違う。
- 行は olm59 の 120 行(OLMo-3 32B の自分の生成)だけ。窓の幅と 32 / 32 の分け方はほかの値で見ていない。
- C3 は 1 行の差で落ちた(14 / 18 対 15 / 18)。線を下げて読み直すことはしない(R3・凍結の規則)。

## 次(主 session の推し・採否は先生)

- 線 1 の「結び」の場面は、名指しの場面(olm75)でも答えの欄の手前(olm76)でも、bind の行の印として立たなかった。P1-2(順の札の較正)は、COMMIT の語の lens の陽性統制(C3 = 77.8 %)が弱い所から始める。lens の語の集合を足すなら、新しい札で凍結の前に決める。
