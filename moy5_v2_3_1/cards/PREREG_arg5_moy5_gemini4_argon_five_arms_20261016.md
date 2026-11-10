# PREREG(凍結 v1.0): `arg5` —— moy-5 × Gemini 4 Argon・5 腕 × n 20・thinking high・上限 $10

- 日付: 2026-10-16(金)12 時台 / 草稿 = builder-opus-medium(Opus 5.5)/ 凍結 = main(Opus 5.5)。凍結の直前の HEAD `d4e71d11`(`git pull --rebase` = Already up to date の後)。
- **身分: 凍結**。本書と runner を一つの commit に入れ、その後に本走を起こす。凍結の前に取ったもの = dry と疎通 1 本(§8)。
- **main が凍結の時に足したこと**: §10 の起こし方を「直列・腕の順 K → Bbp → A → E-full → E-full+Bbp」に固定した。理由 = 共通部 `run_units` は腕を外側の loop で回す(`for arm in arms: for rep in range(n)`)ので、上限 $10 に当たった時に削られるのは並びの最後の腕になる。陽性統制 K を先頭に置けば、止まっても計器が立つかは読める。並走は上限を最大 $0.6 越えうる(草稿 §7)ので使わない。
- 先生(逐語): 10-15「Fable 5.5 の後、Argonでやってみてからですね。他は高すぎる。」→ 10-16「Fable 5.5を待たずに進めましょう。」
- 札の中身(10-16・先生の選択): 腕 =「API の表と同じ 5 腕(推奨)」/ thinking =「high(推奨)」/ 上限 =「$10(推奨)」。
- 身分の印: `L1` = 実出力・実測 / `L3` = 実行層の読み・見積もり。

## §0 親の札
- `essay4`: `conversations/2026-10-14/PREREG_essay_reading_three_items_moy1_moy2_moy5_20261014.md`(腕 A・E-full・K の出所・K の文面)/ runner `ConstructGap/exp/essay_items_20261014.py`。
- `b5bp`: `conversations/2026-10-14/PREREG_pm_cards_eprem1_gname2_b5bp_attr1_kfv1_sol1_20261014.md` §3(腕 Bbp・E-full+Bbp・β′ の文面)/ runner `ConstructGap/exp/b5bp_moy5_blocking_beta_prime_20261014.py`。
- 表と読みの規則: `conversations/2026-10-15/SUMMARY_moy5_cut_across_arms_effort_route_20261015.md` §0〜§2。
- Gemini の経路の前例: `gem1`(`conversations/2026-10-14/PREREG_gem1_gemini4_argon_moy1_open_blocked_20261014.md`・`ConstructGap/exp/gem1_gemini4_argon_moy1_open_blocked_20261014.py`)。

## §1 腕と md5(`L1`・`--dry` の出力)
腕は (札・腕の名・prompt の md5) で区別する(SUMMARY §1-3)。prompt は凍結の module の関数から作り、本 runner では一字も書かない。
「行の md5」= 親の札の results の行に記録された `prompt_md5`(全行で一種類)。

| 腕 | 親の札 | 作る関数 | 中身 | md5(今 = 行) | 字数 |
|---|---|---|---|---|---|
| A | essay4 | `essay_items.prompt_of("moy5","A")` | 凍結の問いだけ | `ee39ba02374a5b3fb6db8dafcef4704b` | 1,921 |
| E-full | essay4 | `essay_items.prompt_of("moy5","E-full")` | essay1 の FRAME + 全文 + 問い | `04ed287c079f6a7df5032686961ab4fc` | 30,833 |
| Bbp | b5bp | `b5bp.prompt_of("Bbp")` | 問い + β′ | `be9c40079e6e29c6ac5a5fe5f82efceb` | 2,187 |
| E-full+Bbp | b5bp | `b5bp.prompt_of("E-full+Bbp")` | FRAME + 全文 + 問い + β′ | `8c875982e94992afdeede30762e378da` | 31,099 |
| K(陽性統制) | essay4 | `essay_items.prompt_of("moy5","K")` | 問い + 比例中項を渡す一文(K block `5c8a4c5a…`) | `b0b1d14b12200dd901e4fc953dbc6f25` | 2,206 |

- 5 腕とも「今の md5 = 固定の値 = 行に記録された値」で一致(dry 12:38・`dry: all five prompts match the frozen md5`)。本走の起動時にも runner が assert する。

## §2 経路と thinking の指定
- model = `gemini-4-argon`(Gemini Developer API・REST `v1beta/models/gemini-4-argon:generateContent`・header `x-goog-api-key`・鍵は環境の `GEMINI_API_KEY` から読むだけ)。
- `generationConfig = {"maxOutputTokens": 12000, "thinkingConfig": {"thinkingLevel": "HIGH"}}`。
  - **12000** = essay4・b5bp の API の全行の `max_tokens`(行の `req_opts` = `{'thinking': {'type': 'adaptive'}, 'output_config': {'effort': 'high'}, 'max_tokens': 12000}`・`L1`)。SUMMARY §2 の見出し「上限 12,000 token」と同じ。Gemini でも上限は thinking を含む(下の docs の逐語)。b5bp の `CAP` は費用の上限(USD)で token の上限ではない。
  - gem1 は thinkingConfig を送らなかった(既定 medium)。本札は HIGH を送る。
- docs の逐語(2026-10-16 12:37 に取得・`L1`):
  - `ai.google.dev/api/generate-content`(取得 file md5 `bf0b072d…`)の ThinkingConfig: 「thinkingLevel enum ( ThinkingLevel ) Optional. Controls the maximum depth of the model's internal reasoning process before it produces a response. The default value is model-dependent. … Recommended for Gemini 3 or later models.」・JSON 表現 `{ "includeThoughts" : boolean , "thinkingBudget" : integer , "thinkingLevel" : enum ( ThinkingLevel ) }`・Enums「THINKING_LEVEL_UNSPECIFIED Default value. MINIMAL Little to no thinking. LOW Low thinking level. MEDIUM Medium thinking level. HIGH High thinking level.」
  - 同頁の UsageMetadata: 「thoughtsTokenCount … Output only. Number of tokens of thoughts for thinking models.」
  - `ai.google.dev/gemini-api/docs/thinking`(md5 `1afb9a47…`・頁の例は Interactions API の `thinking_level`)の表: 「gemini-4-argon On (medium) low, medium, high」。
  - 同頁: 「The max_output_tokens generation parameter sets the maximum number of tokens a response can generate, including thought tokens. … If the model hits this limit while reasoning, it stops generating with status "incomplete" and returns truncated or empty output (while still billing for any thinking tokens generated).」/「Default synchronous output cap (64K): … the default and maximum max_output_tokens cap is 65,536 tokens.」
  - 写し: `/private/tmp/claude-501/-Users-manabu-lancedb-rag/2a28dd87-d1fc-4139-b121-30cd09ffd7ca/scratchpad/agent_arg5/docs/{gc,thinking}.html`(scratch・凍結の前に main が要れば repo に写す)。
- text = `thought` でない part を連ねる(gem1 と同じ)。side log は Anthropic の usage の形(`input_tokens` = promptTokenCount・`output_tokens` = candidatesTokenCount + thoughtsTokenCount)に写し、元の `usageMetadata` も `usage.gemini` に残す。
- 単価 $2.00 / $10.00 per MTok(出力は thinking を含む・gem1 の PREREG の記載・2026-11-30 まで)。

## §3 上限・取り直し・files
- 上限 = 札で **$10**(model は一つ)。共通部 `PM.run_units` の見張り(side log の見積もり > 上限で次の単位を起こさない)に任せる。
- 取り直し = 共通部の規則のまま: text の在る単位は取り直さない・text の無い単位は一回だけ(`tries_max=2`)。
- 共通部は一行も変えない。runner は `PM.STAMP` を本札の日付 `20261016` に差し替えてから `run_units` を呼ぶ(module 変数の差し替え・file は不変)。
  - results = `ConstructGap/exp/results_arg5_20261016_gemini-4-argon_<part>.jsonl` / side log = `ConstructGap/exp/logs/arg5_20261016_gemini-4-argon_<part>_sidelog.jsonl`。
  - 注: 名前の頭が `results_` になるのは凍結の `run_units` の形(gem1 と同じ)。BRIEF の「`arg5_*`」に揃わないのはこの一点。
  - 共通部の記録係 `X.TEE` も本札の side log に要求を書く(usage は空)。費用の数には影響しない(gem1 の RESULT と同じ)。

## §4 採点と読みの規則(SUMMARY §0・§1 と同じ)
- 行の採点 = `b5bp.score`(凍結)= 読み取り器 v2 を「conjecture || reason」に・答えの欄だけの cut・凍結の床・道・座標の形。腕 A・E-full・K にも同じ採点を当てる(essay4 の行に記録された bind は v1 だが、SUMMARY の表は全行を v2 で読み直している)。
- `--read` の列 = SUMMARY §2 と同じ:
  - **cut** = v2 の CUT / SIM-CUT が答え全体に一つ以上。
  - **答えの欄の cut** = 同じ判定を答えの欄だけに。
  - **床** = 答えの欄で `closure_parabola_section`(|EJ| = |KP_y|)。
  - **cut + r8** = cut ∨ r8 の述語(`moy5_r8_additive_predicate_20261015.hits`)。
- 計器の較正(R6・`L1`・12:4x): 本 runner の `read_row` を essay4・b5bp の Claude の行に当てると、SUMMARY §2 の該当 18 cell(cut・答えの欄・床・r8)がすべて一致した(例: Opus Bbp 6 / 20・r8 で 7・Haiku K 20 / 20(答えの欄 15・床 7)・Haiku E-full 床 13 / 18・Fable K 答えの欄 1)。
- 答えが空の行は数えない(SUMMARY §1-1)。`stop_reason` が `MAX_TOKENS` の行・空の行は本数を並べて書く。
- 札をまたいだ合算はしない。Claude 4 tier の行は並べるだけ。
- 計器: K の cut ≥ 16 / 20 で計器が立つ(essay4 の PREREG の線)。立たなければ他の腕の数は記述のみ。

## §5 予測(走行前に書く欄・空欄)
- 先生: (書くなら走行前に)
- 判断層: (空欄)
- 実行層: 書かない(BRIEF が予測の欄を空欄と指定)。

## §6 並べる既存の数(SUMMARY §2・API・adaptive thinking・effort high・上限 12,000・`L1`)
cut / n(答えの欄の cut)。

| 腕(札) | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.1 |
|---|---|---|---|---|
| A(essay4) | 0 / 19 | 0 / 20 | 0 / 20 | 0 / 20 |
| E-full(essay4) | 0 / 18 | 0 / 20 | 0 / 20 | 0 / 20 |
| Bbp(b5bp) | — | 2 / 20 | 6 / 20(+ r8 = 7) | 0 / 20 |
| E-full+Bbp(b5bp) | — | 0 / 20 | 3 / 20 | 1 / 20 |
| K(essay4・陽性統制) | 20 / 20(15) | 20 / 20 | 20 / 20 | 20 / 20(1) |

床の欠け: Haiku の K 7 / 20・E-full 13 / 18(ほかは n と同じ)。

## §7 費用の見積もり(`L3`・疎通の 1 本から)
- 疎通(Bbp・12:38:42〜12:39:53・`L1`): 入力 724・出力 286・thoughts 5,408(出力の数 = 5,694)・`STOP`・71.1 s・$0.058。
- 入力の token は字数 × 0.331(Bbp の 724 / 2,187 字)で置く: A・Bbp・K ≈ 0.7k、E-full・E-full+Bbp ≈ 10.2k〜10.3k。
- 出力を全腕で疎通と同じ 5.7k と置くと: 出力 100 × $0.057 = $5.69・入力 60 × $0.0014 + 40 × $0.0205 ≈ $0.90 → **≈ $6.6**。
- 上振れ: 全行が上限 12,000 に張り付くと出力だけで $12 → **$10 の見張りで 80 本台で止まりうる**。E-full の腕は読む分 thinking が伸びる可能性がある(Claude の E-full の thinking の中央値は未確認)。
- 時間: 1 本 ≈ 70 s として逐次で ≈ 2 時間。腕ごとに part を分けて 5 process 並走なら ≈ 25 分(見張りは全 part の side log を読む・並走の分だけ最大 5 本 ≈ $0.6 の超過がありうる)。

## §8 凍結の前に取ったもの(`L1`)
1. `--dry`(12:38:37): 5 腕の md5 が固定の値と行の値に一致(§1)。
2. `--plumb --arm Bbp`(12:38:42・腕の数に入れない・side log の part = plumb・記録 `ConstructGap/exp/arg5_plumb_20261016.jsonl`): `thoughtsTokenCount` 5,408 が返った(= thinkingConfig HIGH が受け付けられ、thinking が数えられる)。`modelVersion` = `gemini-4-argon`。
   - 答えの欄 `EJ = KP_y`(床 ⭕)・v2 の cut ⭕(理由の欄の `KP_y * VF = … = FP_x^2`・`EJ = FP_x^2 / VF`・相似 `△FVPx ∼ △KPxPy`)・答えの欄の cut ✗・r8 の形 `KPy*VF = VF²+VPx²` も在る。
   - 疎通の 1 本は n に入れない。費用の数(見張り)には入る($0.058)。
3. 計器の較正(§4)。

## §9 していない事
- 本走(100 draw)。凍結の commit。
- medium(gem1 と同じ既定)の対照・Gemini 3.8 Flash・他社の model。
- Claude Code の経路(SUMMARY §3)にあたる Gemini の経路(CLI・道具)。
- 座標の形を cut に数えるかの裁定(SUMMARY §6・未決のまま)。

## §10 本走の起こし方(凍結の後に main が使う)
**本走 = 直列(1 process)・腕の順 K → Bbp → A → E-full → E-full+Bbp**(main が凍結の時に固定):
```
cd /Users/manabu/lancedb-rag/ConstructGap && set -a && . ~/.config/reverse_turing/keys.env && set +a && python3 exp/arg5_moy5_gemini4_argon_20261016.py --arms K,Bbp,A,E-full,E-full+Bbp --n 20 --part a
```
text の無い単位の取り直しは、同じ命令をもう一度起こす(共通部の規則 = 一単位 2 回まで)。並走は使わない(上限を越えうる)。読み: `python3 exp/arg5_moy5_gemini4_argon_20261016.py --read`。

- runner md5(12:38 時点): `0a01daa9…`(凍結の時に取り直す)。
