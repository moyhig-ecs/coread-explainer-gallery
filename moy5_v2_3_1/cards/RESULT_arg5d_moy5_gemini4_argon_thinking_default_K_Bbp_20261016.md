# RESULT: 札 `arg5d` —— moy-5 × Gemini 4 Argon・K と Bbp × n 20・thinking の指定を送らない(既定)・上限 $3(2026-10-16 金 夕・zebrashark)

- 札: [PREREG](PREREG_arg5d_moy5_gemini4_argon_thinking_default_K_Bbp_20261016.md)(凍結 v1.0 = commit `78b722f9`・runner md5 `dcc24e9389d213dc12769043f6e602ef`)。
- 先生(逐語・10-16 夕): 「3 残高的には取れますよね？」→ 腕「K・Bbp × n 20(推奨)」/ thinking「送らない(推奨)」/ 上限「$3(推奨)」。
- **HEAD**(`R1`・`git fetch` で origin との差 0 の後): `78b722f9`。
- 記録: `ConstructGap/exp/results_arg5d_20261016_gemini-4-argon_a.jsonl`(40 行・md5 `04af6068886b2dedce418e1b87f3c6b6`)・起動の出力 `exp/logs/arg5d_20261016_main_run_a.out`・`--read` の出力 = `conversations/2026-10-16/data_moy5_summary/arg5d_read_per_row_relations_20261016.txt`(md5 `d5ea3488`)・関係の数と費用 = `exp/arg5d_relation_counts_20261016.py`(md5 `7d031538`・読むだけ)の出力 `data_moy5_summary/arg5d_relation_counts_20261016.txt`(md5 `b183db8b`)。
- 身分: 数 = 実出力(`L1`)。読み = `L3`。**判定と講評は先生。** 予測の欄は空欄のまま凍結した(PREREG §5)。

## §1 取れた物
- 直列・K → Bbp。40 単位が一通りで全部 text あり・全部 `STOP`(`MAX_TOKENS` 0・取り直し 0)。HTTP の error 0。
- 費用 = 見張りの値 **$0.405**(疎通 1 本 $0.006 を含む・本走 K $0.131・Bbp $0.268・単価 $2 / $10 per M の算術 `L3`)。上限 $3 の内側。
  - 見張りの「calls 81」は、本走 40 + 疎通 1 の usage 行と、共通部の記録係 `X.TEE` の要求の行 40(usage 空・`http None`)の和(arg5 の PREREG §3 の注と同じ)。

## §2 表(`L1`)

| 腕 | md5 | n | cut | 答えの欄の cut | 床 | cut + r8 | thinking の中央値 | 関係の数 / 本 | CUT の関係 / 本 |
|---|---|---|---|---|---|---|---|---|---|
| K(陽性統制) | `b0b1d14b` | 20 | **20** | 0 | 20 | 20 | 363 | 7.0 | 2.0 |
| Bbp | `be9c4007` | 20 | **8** | 0 | 20 | 8 | 1,005 | 15.5 | 0 |

- thinking の中央値 = runner の `--read`(共通部の `med` = 並べて 11 番目)。関係の数 = 読み取り器 v2 の `relations` を答え全体に当てた数の中央値(`statistics.median`・SUMMARY_moy5 10-16 の集計 script と同じ定義)。
- thinking の幅: K 0〜511・Bbp 0〜3,051。**thinking 0 の本** = K 8 本(8 本とも cut)・Bbp 6 本(cut 1)/ thinking > 0 = K 12 本(12 本とも cut)・Bbp 14 本(cut 7)。
- Bbp の cut の 8 本 = r1・r2・r4・r6・r12・r15・r17・r18(関係の一覧は `--read` の出力)。

## §3 並べる既存の数(`L1`)

| 腕 | **Argon・既定(本札)** | Argon・high(arg5) | Sonnet 5.5 | Opus 5.5 | Fable 5.1 |
|---|---|---|---|---|---|
| K | **20 / 20** | 20 / 20 | 20 / 20 | 20 / 20 | 20 / 20(1) |
| Bbp | **8 / 20** | 20 / 20 | 2 / 20 | 6 / 20(+ r8 = 7) | 0 / 20 |
| Bbp の thinking の中央値 | 1,005 | 8,494 | 1,030 | 1,753 | 2,233 |
| Bbp の関係の数 / CUT(中央値) | 15.5 / 0 | 36.0 / 4.0 | 11.0 / 0 | 19.5 / 0 | 19.5 / 0 |

(Claude = API・adaptive thinking・effort high・上限 12,000・SUMMARY_moy5 10-16 §2・§2-2・§6。arg5 = thinking high・上限 12,000。)

## §4 読み(`L3`)
1. **計器は既定の thinking の Argon の上でも立つ**: K 20 / 20(thinking 0 の 8 本も全部 cut)。
2. **Argon の Bbp 20 / 20 は thinking high の条件の数だった**: 同じ問い・同じ上限で、指定を送らないと 8 / 20。thinking の中央値は 8,494 → 1,005、関係の数は 36.0 → 15.5。
3. **既定の Argon の Bbp(8 / 20)は、Claude の API の high の Opus(6〜7 / 20)と同じ桁**。thinking の中央値は Sonnet(1,030)と同じ程度、関係の数(15.5)は Sonnet(11.0)と Opus(19.5)の間。
4. Bbp で thinking 0 の 6 本は cut 1、thinking > 0 の 14 本は cut 7(記述だけ・n が小さい)。
5. SUMMARY_moy5 §5-8 の moy-1 との対応(理由の欄に厚く・答えの欄は最小)は、本札でも同じ形: 答えの欄の cut 0・床 20 / 20(両腕)。thinking の条件は gem1・syc1 と揃った(上限 token は 12,000 対 16,000 で違うが、本札では上限に届いた本は無い)。
6. **費用**(Bbp・算術): 一本 $0.013・cut 一本あたり $0.034(Argon の導入価格・11-30 まで)。同じ Bbp の API high で Opus は cut 一本あたり $0.17(授業資料の MEMO §2-2)。

## §5 限定
- thinking の目盛りは vendor ごとに違う。既定の thinking は「必ず考える」ではない(本札でも thinking 0 が K 8 本・Bbp 6 本)。
- n 20・腕は二つ・一項目。
- 関係の数は読み取り器 v2 が拾えた関係の数(SUMMARY_moy5 §6 の読み取り器の限定がそのまま掛かる)。
- 集計 script(`summary_moy5_cut_all_cards_20261016.py`)には本札の読み元を足していない。関係の数は同じ定義を小さな script(上の記録)で数えた(PREREG §4 の「足した事を RESULT に書く」に当たる変更は無し)。
- 走行中、同じ zebrashark で札 bon1(llama-server・ollama)が並走していた(API の札なので経路の干渉は無い・`L3`)。

## §6 していないこと
A・E-full・E-full+Bbp の既定 thinking / thinkingLevel MEDIUM・LOW の明示 / 上限 token を 16,000 に揃えること / CAD での形の確定。
