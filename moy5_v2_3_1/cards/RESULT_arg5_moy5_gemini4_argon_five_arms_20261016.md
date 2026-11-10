# RESULT: 札 `arg5` —— moy-5 × Gemini 4 Argon・5 腕 × n 20・thinking high・上限 $10(2026-10-16 金 12:43〜14:3x・zebrashark)

- 札: [PREREG](PREREG_arg5_moy5_gemini4_argon_five_arms_20261016.md)(凍結 v1.0 = commit `587ade3f`・runner md5 `0a01daa99f0c4143af3e7cc6000acf09`)。
- 先生(逐語): 10-15「Fable 5.5 の後、Argonでやってみてからですね。他は高すぎる。」→ 10-16「Fable 5.5を待たずに進めましょう。」/ 札の中身 =「API の表と同じ 5 腕(推奨)」「high(推奨)」「$10(推奨)」。
- **HEAD**(`R1`・`git pull --rebase` の後): `587ade3f`。
- 記録: `ConstructGap/exp/results_arg5_20261016_gemini-4-argon_a.jsonl`(102 行 = 100 + 取り直し 2・md5 `1c7ee8be817f4b7bab6b866160d2aac0`)・side log `exp/logs/arg5_20261016_gemini-4-argon_a_sidelog.jsonl`(一呼び出し二行)・起動の出力 `exp/logs/arg5_20261016_main_run_a.out` / `…_retake.out`。
- 身分: 数 = 実出力(`L1`・runner の `--read` と、読み取り器 v2 で数えた関係の数)。読み = `L3`。**判定と講評は先生。** 予測の欄は空欄のまま凍結した(PREREG §5)。

## §1 取れた物
- 直列・腕の順 K → Bbp → A → E-full → E-full+Bbp(PREREG §10)。100 単位を一通り → text の無い 2 単位(E-full+Bbp r13・r17・どちらも `MAX_TOKENS`・thinking 11,997)を同じ命令で一度取り直し → 二度とも `MAX_TOKENS` = 規則どおりそのまま(E-full+Bbp は n 18)。
- HTTP の error 0。費用 = **$7.46**(疎通 1 本・本走 100 本・取り直し 2 本の計 103 呼び出し・入力 397,188・出力 667,006 token・単価 $2 / $10 per M の算術 `L3`)。上限 $10 の内側。

## §2 表(SUMMARY_moy5 10-15 §2 と同じ列・`L1`)

| 腕 | md5 | n | cut | 答えの欄の cut | 床 | cut + r8 | thinking の中央値 | 関係の数 / 本(中央値) | CUT の関係 / 本(中央値) |
|---|---|---|---|---|---|---|---|---|---|
| K(陽性統制) | `b0b1d14b` | 20 | **20** | 0 | 20 | 20 | 5,334 | 19.0 | 4 |
| Bbp | `be9c4007` | 20 | **20** | 0 | 20 | 20 | 8,494 | 36.0 | 4 |
| A | `ee39ba02` | 20 | 0 | 0 | 20 | 0 | 4,016 | 8.5 | 0 |
| E-full | `04ed287c` | 20 | 0 | 0 | 20 | 0 | 3,284 | 8.0 | 0 |
| E-full+Bbp | `8c875982` | 18 | **18** | 0 | 18 | 18 | 9,110 | 58.5 | 9.5 |

(関係の数 = 読み取り器 v2 の `relations` を答え全体に当てた数・中央値・集計 = `exp/summary_moy5_cut_all_cards_20261016.py`・出力 `conversations/2026-10-16/data_moy5_summary/summary_table_moy5_cut_all_cards_20261016.txt`)

## §3 並べる既存の数(SUMMARY_moy5 §2・API・adaptive thinking・effort high・上限 12,000・`L1`)

| 腕 | Sonnet 5.5 | Opus 5.5 | Fable 5.1 | **Argon(本札)** |
|---|---|---|---|---|
| A | 0 / 20 | 0 / 20 | 0 / 20 | **0 / 20** |
| E-full | 0 / 20 | 0 / 20 | 0 / 20 | **0 / 20** |
| Bbp | 2 / 20 | 6 / 20(+ r8 = 7) | 0 / 20 | **20 / 20** |
| E-full+Bbp | 0 / 20 | 3 / 20 | 1 / 20 | **18 / 18** |
| K(陽性統制) | 20 / 20 | 20 / 20 | 20 / 20(1) | **20 / 20** |

同じ読み取り器で数えた関係の数(中央値・`L1`): Bbp = Argon 36・Opus 19.5・Fable 19.5・Sonnet 11 / E-full+Bbp = Argon 58.5・Opus 23・Fable 24・Sonnet 17。CUT の関係 / 本の中央値は Claude の三つとも 0、Argon は 4(Bbp)と 9.5(E-full+Bbp)。

## §4 読み(`L3`)
1. **計器は Argon の上で立つ**: 陽性統制 K で cut 20 / 20。
2. **β′(理由の欄に「等長でない関係」を求める)で、Argon は理由の欄に CUT を出す**: Bbp 20 / 20・E-full+Bbp 18 / 18。Claude 4 tier の API の行(0〜6 / 20)より多い。
3. **ただし cut の定義は「答え全体に CUT が一つでもあれば」**(SUMMARY §0)で、Argon は一本に並べる関係の数が Claude の約 2 倍(Bbp)〜2.5 倍(E-full+Bbp)ある。一本の中の CUT も中央値 4〜9.5 で、一つの当たりではない。列挙の広さと CUT の見つけ方を分けるには、関係の数あたりの率か、最初に挙げた関係だけを読むなどの別の読みが要る(本札の読みの規則の外・二走目の候補)。
4. **答えの欄の cut は 0**(全腕)で、答えの欄には床(|EJ| = |KP_y|)を置く。moy-1 で Argon が「理由の欄では円を見つけ(28 / 40)、答えの欄で約束しない(0 / 40)」だった形と、**理由の欄に厚く・答えの欄は最小**という点で同じ向き。
5. **token の訂正**: moy-1 の Argon の「一回 約 530 token」は API の既定(thinking medium・gem1)の値。本札(thinking high)では thinking の中央値が 3,300〜9,100 token。memory `project_moy1_as_cross_model_yardstick_20261016` の「Argon = 少ない token で言い切らない」は既定の thinking の条件に限る(memory を直した)。

## §5 限定
- thinking の段の目盛りは vendor ごとに違う(Argon の high と Claude の effort high は同じ量ではない)。
- E-full+Bbp の 2 単位は上限 12,000 に二度張り付き、n 18。
- 関係の数は読み取り器 v2 が拾えた関係の数で、答えの文の数ではない。
- 走行中の 10-16 に、同じ zebrashark で札 bon1(llama-server・ollama)が並走していた(API の札なので経路の干渉は無い・`L3`)。

## §6 していないこと
二走目の読み(関係の数あたりの率・最初の関係だけ)・Argon の thinking medium での取り直し(moy-1 の gem1 と条件を揃える)・Claude Code の経路(Argon には無い)。
