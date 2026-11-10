# RESULT: `rte1` —— moy-5 の経路と effort を分ける対照(問いだけ・Opus 5.5 / Fable 5.1)

- 日付: 2026-10-15(木)17 時台 / 実行層 = Opus 5.5 xhigh。判定と講評は先生。`L1` = 実出力 / `L3` = 読み。
- PREREG = `PREREG_rte1_route_effort_control_moy5_20261015.md`(凍結 `5fd3505d`)。HEAD `5fd3505d`。
- 先生(逐語): 「Fable 5.5が出る前に、経路とeffortを分ける対照を採っておきましょうか。」→(予算の問い)→「走らせる(両方)」。
- 走行:
  - Claude Code × high: 16:51〜16:5x・20 本・失敗 0。subscription の枠。
  - API × max: 16:54〜17:05・20 本・失敗 0・どれも `end_turn`(上限 64,000 に届いた本なし)。
  - 実費(見張り)= Opus $2.76・Fable $5.59・計 $8.35(上限 Opus $5・Fable $12 に届かず)。
- 出力の token の中央値(API max): Opus 13,546・Fable 10,434(moy5c の Claude Code max の中央値 Opus 12,691・Fable 12,142 と同じ程度)。

## §1 数(`L1`・cut = 読み取り器 v2・r8 の述語を足しても同じ)
| model | API × high(b5bp・n 20) | **API × max** | **Claude Code × high** | Claude Code × max(moy5c) |
|---|---|---|---|---|
| Opus 5.5 | 7 / 20 = 0.35(r8 を含む) | **6 / 10 = 0.6** | **2 / 10 = 0.2** | 10 / 10 = 1.0 |
| Fable 5.1 | 0 / 20 = 0 | **2 / 10 = 0.2**(答えの欄 1) | **3 / 10 = 0.3** | 6 / 10 = 0.6 |

- 床(答えの欄の |EJ| = |KP_y|)は、新しい四つの cell で全部 10 / 10。
- 答えの欄の cut は Fable の API max の 1 本(r2)だけ。

## §2 事前の読みの表への当てはめ(PREREG §2)
「近い」= 差 ≤ 0.2、「離れる」= 差 ≥ 0.4。

| model | API max と CC max | CC high と API high | 表の読み |
|---|---|---|---|
| Opus | 0.6 対 1.0 = 0.4 → 離れる(API が低い) | 0.2 対 0.35 = 0.15 → 近い | **不定**(表に無い組) |
| Fable | 0.2 対 0.6 = 0.4 → 離れる(API が低い) | 0.3 対 0 = 0.3 → 間 | **不定** |

## §3 予測との照合(実行層 `L3`)
| # | 予測 | 結果 | 成否 |
|---|---|---|---|
| 1 | API max: Opus ≥ 8・Fable ≥ 3 | 6・2 | 外・外 |
| 2 | CC high: Opus ≤ 5・Fable ≤ 2 | 2・3 | 合・外 |
| 3 | 答えの欄の cut ≤ 2(新しい 4 cell の計) | 1 | 合 |

## §4 言える事(記述)
1. **effort を上げると、二つの経路とも cut が増えた。**
   - Opus: API 0.35 → 0.6・Claude Code 0.2 → 1.0。
   - Fable: API 0 → 0.2・Claude Code 0.3 → 0.6。
2. **max では、二つの model とも Claude Code が API より 0.4 高い。** 出力の量は同じ程度(Opus は API max 13.5k・Claude Code max 12.7k・Fable は 10.4k と 12.1k)。
3. high では、Opus は経路の差が小さく(0.15)、Fable は Claude Code が 0.3 高い。
4. ⇒ effort が効いており、経路の差は max で大きく出る、という交互作用の形(`L3`)。事前の表は交互作用の組を持っていなかったので、表の読みは「不定」。
   - 経路の差の源(Claude Code の system の文脈・既定の上限・呼び出しの形のどれか)は、この札では分けられない(`L3`)。
5. moy-5 の SUMMARY §5-4 の「一番効いているのは effort」は、API の側でも effort で増えたので支えが増えた。ただし「Claude Code の max の 10 / 10」は、経路の分も含んだ数。

## §5 限定
- n 10(API high だけ n 20)。差 0.4 は n 10 の Wilson の区間が重なる幅(例: Opus API max 6 / 10 = 0.31〜0.83・CC max 10 / 10 = 0.72〜1.0)。
- 日付が違う cell を並べた(API high = 10-14・CC max = 10-15 昼・新しい二つ = 10-15 夕)。
- API max の上限は 64,000 token・stream。API high の 12,000 とは上限も違う(どの本も上限に届いていないので、切れによる差は無い)。
- 一項目・Claude の二つの model だけ。
