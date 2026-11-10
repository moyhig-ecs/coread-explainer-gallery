# PREREG: `rte1` —— moy-5 の経路と effort を分ける対照(問いだけ・Opus 5.5 / Fable 5.1)

- 日付: 2026-10-15(木)17 時台 / 実行層 = Opus 5.5 xhigh。走らせる前に書き、local の commit で凍結する。判定と講評は先生。
- 先生(逐語): 「Fable 5.5が出る前に、経路とeffortを分ける対照を採っておきましょうか。」
- 出所: SUMMARY_moy5_cut_across_arms_effort_route_20261015.md §6・§8(effort と経路の交絡)。

## §0 背景(`L1`・SUMMARY_moy5 §3)
b5bp の Bbp の問い(md5 `be9c4007`)だけを、二つの経路と二つの effort で並べる。

| | high | max |
|---|---|---|
| API | b5bp(10-14・n 20): Opus 6 / 20(r8 を足して 7)・Fable 0 / 20 | **新(本札)** |
| Claude Code | **新(本札)** | moy5c(10-15・n 10): Opus 10 / 10・Fable 6 / 10 |

## §1 作り
- runner = `ConstructGap/exp/rte1_route_effort_control_moy5_20261015.py`。
- **Claude Code × high**(`--part cc-high`): 凍結の moy5c の runner をそのまま使う。札の名・置き場・effort(high)・出力の file だけを差す。
  - `claude -p`・空の folder・`--setting-sources local`・MCP なし・道具なし(Bash も禁止)。
  - Opus / Fable × n 10。費用は subscription の枠(API の課金なし)。
- **API × max**(`--part api-max`): 凍結の `models._anthropic` の本文(adaptive thinking・同じ問い・同じ key と header)から、変えるのは二つだけ。
  - `output_config.effort = "max"`
  - `max_tokens = 64000`(12,000 では max の答えが切れる: moy5c の出力の中央値 約 12k・最大 130k)
  - 長考で 10 分を超えても切れないよう、stream で受ける。
  - Opus / Fable × n 10。自前の side log で費用を見張る。上限は Opus $5・Fable $12。
  - **先生の予算の裁可の後に走らせる**(下 §4)。
- 採点 = b5bp の凍結の score(読み取り器 v2 の cut)+ r8 の裁定の述語を隣に(moy-5 の SUMMARY と同じ)。答えの欄の cut・床も並べる。

## §2 読みの表(事前に固定・model ごと)
- 「近い」= 割合の差 ≤ 0.2。「離れる」= 割合の差 ≥ 0.4。その間は不定(R3 の margin・n 10)。

| API max と CC max | CC high と API high | 読み |
|---|---|---|
| 近い | 近い | effort が効いている(経路は効いていない) |
| 離れる(API max が低い) | 離れる(CC high が高い) | 経路が効いている |
| 近い | 離れる(CC high が高い) | 両方が効いている |
| ほか | ほか | 不定 |

## §3 予測(実行層 `L3`・「effort が主」とした時)
1. API max: Opus ≥ 8 / 10・Fable ≥ 3 / 10。
2. CC high: Opus ≤ 5 / 10・Fable ≤ 2 / 10。
3. 答えの欄の cut は四つの新しい cell の合計で ≤ 2。
- 外れる形: CC high が CC max に近い(経路の効き)/ API max が API high に近い。

## §4 費用(見込み)
- API × max: 出力の中央値を moy5c の 12k として、Opus 約 $0.26 / 本・Fable 約 $0.62 / 本。n 10 ずつで約 $9(Opus 約 $2.6・Fable 約 $6.2)。
  - 長い本が混じると増える。上限は Opus $5・Fable $12 で止める。
- Claude Code × high: subscription の枠。API の課金なし。

## §5 していない事
走行・凍結。API × max は先生の予算の裁可の後。Fable の改版が出た後の取り直し。
