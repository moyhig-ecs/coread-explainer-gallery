# PREREG(凍結 v1.0): `arg5d` —— moy-5 × Gemini 4 Argon・K と Bbp × n 20・thinking の指定を送らない(既定)・上限 $3

- 日付: 2026-10-16(金)夕 / 実行層 = Opus 5.5。凍結の直前の HEAD `9ed4b886`(`git fetch` で origin との差 0 を確かめた後)。
- **身分: 凍結**。本書と runner を一つの commit に入れ、その後に本走を起こす。凍結の前に取ったもの = dry と疎通 1 本(§8)。
- 出所: SUMMARY_moy5 10-16 §8「Argon の thinking を既定(medium)にして Bbp・K を取り直す(moy-1 の gem1 と条件を揃える)」・判断層(judge-cold)の「先生が読む時に確かめる点」の三つ目。
- 先生(逐語・10-16 夕): 「3 残高的には取れますよね？」→ 札の中身 = 腕「K・Bbp × n 20(推奨)」/ thinking「送らない(推奨)」/ 上限「$3(推奨)」。
- 身分の印: `L1` = 実出力・実測 / `L3` = 実行層の読み・見積もり。

## §0 親の札
- `arg5`(凍結 `587ade3f`・runner `ConstructGap/exp/arg5_moy5_gemini4_argon_20261016.py` md5 `0a01daa9…`・RESULT `conversations/2026-10-16/RESULT_arg5_moy5_gemini4_argon_five_arms_20261016.md`)。本札の runner はその写しで、変えたのは §2 の表の 6 か所だけ。
- 腕の出所: K = `essay4`・Bbp = `b5bp`(arg5 の PREREG §0 と同じ)。
- thinking の条件の出所: `gem1`(moy-1・`ConstructGap/exp/gem1_gemini4_argon_moy1_open_blocked_20261014.py`)と `syc1`(`ConstructGap/exp/syc1_gemini_after_answer_and_false_rejection_20261014.py`)。どちらも thinkingConfig を送らない。

## §1 腕と md5(`L1`・`--dry` の出力・17 時台)

| 腕 | 親の札 | 中身 | md5(今 = 固定 = 行) | 字数 |
|---|---|---|---|---|
| K(陽性統制) | essay4 | 問い + 比例中項を渡す一文 | `b0b1d14b12200dd901e4fc953dbc6f25` | 2,206 |
| Bbp | b5bp | 問い + β′ | `be9c40079e6e29c6ac5a5fe5f82efceb` | 2,187 |

- `dry: all 2 prompts match the frozen md5`。本走の起動時にも runner が assert する(arg5 と同じ code)。

## §2 arg5 の runner から変えた所(全部・`diff` の出力)

| 所 | arg5 | arg5d |
|---|---|---|
| `CARD` | `"arg5"` | `"arg5d"` |
| `CAP`(USD) | 10.0 | **3.0** |
| `ARMS` | A・E-full・Bbp・E-full+Bbp・K | **K・Bbp** |
| `FROZEN` | 5 腕 | K・Bbp の 2 行(md5 は同じ値) |
| `GEN` | `{"maxOutputTokens": 12000, "thinkingConfig": {"thinkingLevel": "HIGH"}}` | **`{"maxOutputTokens": 12000}`** |
| 疎通の記録の file 名 | `arg5_plumb_…` | `arg5d_plumb_…`(`CARD` から作る) |

(ほかに dry の表示の一文。経路・text の取り出し・side log・`read_row`・`read`・`run_units`・採点は arg5 の code のまま。)

- **thinking**: thinkingConfig を送らない = gem1・syc1 と同じ要求。docs の表は「gemini-4-argon On (medium)」(arg5 の PREREG §2 の逐語)。
- **上限の token**: 12,000 のまま(arg5 と、SUMMARY_moy5 §2 の Claude の API の行と同じ)。gem1・syc1 は 16,000 で、ここは揃えていない。
- **既定の thinking の実際**(`L1`・各札の results の `reasoning_tokens`):
  - gem1(40 本)は 0 の本が 0 本・中央値 381・最大 1,296。
  - syc1(140 本)は 0 の本が 58 本(part a 2 / 40・b 37 / 60・c 19 / 40)。
  - 本札の疎通の 1 本も 0(§8)。既定は「必ず考える」ではない。本札はこの既定をそのまま測る(thinking の量は行ごとに記録して並べる)。

## §3 上限・取り直し・files
- 上限 = 札で **$3**(model は一つ)。共通部 `PM.run_units` の見張りに任せる(arg5 と同じ)。
- 取り直し = 共通部の規則のまま(text の在る単位は取り直さない・text の無い単位は一回だけ)。
- results = `ConstructGap/exp/results_arg5d_20261016_gemini-4-argon_<part>.jsonl` / side log = `ConstructGap/exp/logs/arg5d_20261016_gemini-4-argon_<part>_sidelog.jsonl`。

## §4 採点と読みの規則(arg5 の PREREG §4 と同じ)
- 行の採点 = `b5bp.score`(凍結)。`--read` の列 = cut・答えの欄の cut・床・cut + r8・stop・thinking の中央値。
- 答えが空の行は数えない。`MAX_TOKENS` の行・空の行は本数を並べて書く。
- 計器: K の cut ≥ 16 / 20 で計器が立つ(essay4 の PREREG の線)。立たなければ Bbp の数は記述のみ。
- 並べるのは arg5(thinking high)の同じ腕と、SUMMARY_moy5 §2 の Claude の API の行。札をまたいだ合算はしない。
- 一本あたりの関係の数(全部 / CUT)は、SUMMARY_moy5 10-16 の集計 script(`summary_moy5_cut_all_cards_20261016.py`)の読み方で並べる(script に本札の読み元を足すのは走行の後・足した事を RESULT に書く)。

## §5 予測(走行前に書く欄・空欄)
- 先生: (書くなら走行前に)
- 判断層: (空欄)
- 実行層: 書かない。

## §6 並べる既存の数(`L1`)

| 腕 | arg5(Argon・thinking high) | Sonnet 5.5 | Opus 5.5 | Fable 5.1 |
|---|---|---|---|---|
| K | 20 / 20(thinking 中央値 5,334) | 20 / 20 | 20 / 20 | 20 / 20(1) |
| Bbp | 20 / 20(thinking 中央値 8,494) | 2 / 20 | 6 / 20(+ r8 = 7) | 0 / 20 |

(Claude = API・adaptive thinking・effort high・上限 12,000・SUMMARY_moy5 §2。)

## §7 費用の見積もり(`L3`)
- 疎通(Bbp・`L1`): 入力 724・出力 429・thinking 0・`STOP`・20.5 s・**$0.006**。
- 40 本 × $0.006 ≈ $0.25(thinking 0 の場合)。thinking が gem1 の中央値 381 くらい付けば 1 本 ≈ $0.01 で計 ≈ $0.4。
- 上振れ: arg5 の high と同じ量なら K $1.17 + Bbp $1.76 = $2.93(arg5 の results から算)。見張り $3 の内側。
- Gemini の画面は見張りの値と食い違うことがある(memory: 10-15 は画面の方が 1.3〜2 倍)。
- 時間: 1 本 ≈ 20 s として直列で ≈ 15 分。

## §8 凍結の前に取ったもの(`L1`)
1. `--dry`: 2 腕の md5 が固定の値と行の値に一致(§1)。
2. `--plumb --arm Bbp`(腕の数に入れない・記録 `ConstructGap/exp/arg5d_plumb_20261016.jsonl`・side log の part = plumb): `STOP`・`thoughtsTokenCount` の欄なし(= 0)・`modelVersion` = `gemini-4-argon`。
   - 答えの欄 `KP_y = EJ`(床 ⭕)・v2 の cut ✗・答えの欄の cut ✗・r8 ✗。疎通の 1 本は n に入れない(費用の数には入る)。

## §9 していない事
- A・E-full・E-full+Bbp の thinking 既定(先生の選択 = K と Bbp だけ)。
- thinkingLevel = MEDIUM を明示する腕(先生の選択 = 送らない)。
- 上限 token を gem1・syc1 の 16,000 に揃えること。

## §10 本走の起こし方
**直列(1 process)・腕の順 K → Bbp**:
```
cd /Users/manabu/lancedb-rag/ConstructGap && set -a && . ~/.config/reverse_turing/keys.env && set +a && python exp/arg5d_moy5_gemini4_argon_thinking_default_20261016.py --arms K,Bbp --n 20 --part a
```
text の無い単位の取り直しは同じ命令をもう一度(一単位 2 回まで)。読み: `python exp/arg5d_moy5_gemini4_argon_thinking_default_20261016.py --read`。

- runner = `ConstructGap/exp/arg5d_moy5_gemini4_argon_thinking_default_20261016.py`・md5 `dcc24e9389d213dc12769043f6e602ef`。
