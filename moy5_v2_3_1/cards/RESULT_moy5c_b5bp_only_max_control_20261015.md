# RESULT: `moy5c` —— b5bp の問いだけ(道具なし・表なし)× effort max(moy5e の max の対照)

- 日付: 2026-10-15(木)午後 / 実行層 = Opus 5.5 xhigh。判定と講評は先生。`L1` = 実出力。
- PREREG = `PREREG_moy5c_b5bp_only_max_control_20261015.md`(凍結 `29b6ed82`)。走行 13:39:34 → 13:59:58(20 本・失敗 0)。
- 先生(逐語): 「b5bp maxで走らせる」。

## §1 数(`L1`)
| model | **問いだけ × max**(moy5c)| 道具 × max(moy5e)| 表 × max(moy5e)| 問いだけ × API・effort high(b5bp)|
|---|---|---|---|---|
| Opus 5.5 | **10 / 10** | 10 / 10 | 10 / 10 | 7 / 20 |
| Fable 5.1 | **6 / 10** | 4 / 10 | 6 / 10 | 0 / 20 |

- 答えの欄の cut: 0 / 20(答えの欄は床)。床(凍結の閉包): Opus 10・Fable 9。
- **所要時間と出力 token の中央値**: Opus 120 s・12,984 / Fable 154 s・12,324。どちらも、道具・表のある max より多い(moy5e の max: Opus 76〜88 s・8,235〜9,682 / Fable 105〜123 s・8,209〜9,392)。
- Opus r7 は 887 s。
- 費用の欄(API の単価での換算・実際は枠から): Opus $6.07・Fable $11.37。

## §2 cut の形と CAD(`L1`)
- moy5e と同じ比例中項の型(`EJ·VF = FP_x²`・`FP_x² = FV·FP_y`・`VH = VP_x²/VF`・`VJ·VE = VP_x²`)に加えて、新しい形が出た:
  - `HP_y² = 4·VF·VH`(Opus r1・r3)= 放物線の方程式(頂点 V・焦点までの距離 VF・縦座標 HP_y)
  - `DK² = 4·VD·VH`(Opus r6)
  - `VH = 2·VP_x²/FD`(Fable r0)
  - `EJ = FK²/(2·FD)`(Fable r4)
- 新しい三形(HP_y² = 4·VF·VH・DK² = 4·VD·VH・VH = 2·VP_x²/FD)を CAD にかけた: 三つとも ∀ t で True・0 < r < d で恒等式。

## §3 予測との照合(実行層 `L3`)
| # | 予測 | 結果 | 成否 |
|---|---|---|---|
| 1 | Opus の cut ≥ 8 / 10 | 10 | 合 |
| 2 | Fable の cut 2〜6 / 10 | 6 | 合 |
| 3 | 答えの欄の cut ≤ 1 | 0 | 合 |

## §4 言える事(記述)
1. 道具も表も無い b5bp の問いだけで、effort を max にすると Opus 10 / 10・Fable 6 / 10 が cut を書いた。max の道具の腕(10・4)・表の腕(10・6)と同じか上回る。
2. ⇒ この経路の moy-5 では、cut の数は effort でほぼ決まり、道具と表は数を足していない(`L3`・一項目・n 10)。
3. 答えの欄は 20 本とも床で、cut は理由の欄にだけ在る(moy5e と同じ)。
4. 出力 token は、道具・表のある max より多い(問いだけの方が長く推論した)。

## §5 限定
- 経路は Claude Code(API の b5bp と一対一には並べない)。b5bp の API の数(effort high)との差が、effort によるのか経路によるのかは、API で effort max を取らないと分けられない。
- 一項目・n 10・名の付け替えなし。
