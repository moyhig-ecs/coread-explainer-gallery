HEAD(R1) = 2260e31c(この file を入れた commit の親・実行層が commit 時に記入)

# RESULT(札 `olm3`): 事後学習済み Olmo-3-32B-Think を moy-5 の screen(K 10 + none/Q1 20)に二経路で — B1 = bf16 を MLX で / B2 = ollama Q4_K_M(2026-10-23 01:20 〜 14:12・実行層)

- PREREG: `PREREG_olm3_moy5_olmo3_32b_think_bf16_mlx_and_ollama_q4_screen_20261022.md`(凍結 `9e52c71a`)。runner = `ConstructGap/exp/olm3_moy5_olmo3_32b_think_bf16_mlx_and_ollama_q4_screen_20261022.py`。
- 実出力 = `ConstructGap/exp/results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl`(30 行)・`…_olmo-3-32b-think-ollama-q4km.jsonl`(30 行)。raw = thinking + 答え。log = `ConstructGap/exp/logs/olm3_20261022_B1B2.out`(gitignore)。
- 走行: B1 = 01:20:03 〜 08:47:09(6 sub-batch・各 68〜77 分・model 読み込み 5 秒)/ B2 = 08:47 〜 14:12:23(30 本・一本 6〜16 分・中央値 11 分)。費用ゼロ。
- 欄: `cut(本文)` = thinking を含む全文に切断の形 / `cut(答え)` = JSON の答えに / `床` = 答えが |EJ| = |KP_y| / `閉じた` = `</think>` が出て答えに進んだ / `打ち切り` = 16384。

## §0. 開示(発火の後に分かった事・`L1`)
- **B2 の template**: ollama の `olmo-3:32b` と `olmo-3:32b-np16384` の Modelfile は `TEMPLATE {{ .Prompt }}` + `RENDERER olmo3-32b-think` + `PARSER olmo3-think` = chat の形は ollama 組み込みの renderer が作る(その逐語は未照合)。raw は `<think>` で始まり、`</think>` の後に JSON が出る(例 r0: thinking 50,042 字・答え 308 字)。B1 は HF の `chat_template.jinja`(system「You are a helpful AI assistant.」+ user + `<|im_start|>assistant\n<think>`)。= 二経路は **prompt の描画が同一ではない**(PREREG §5 の「同じ目盛りではない」に加える)。
- **B2 の sampler**: 渡したのは temperature 0.6・top_p 0.95・seed・num_predict。ollama の既定の `top_k`(40)は渡しておらず既定のまま = B1(MLX・top_k なし)と違う(`L3` の候補 = §4)。
- 読み取り器 v2 の取りこぼし 1: B2 none/Q1 r6 の答え「distance(E,J) equals distance(K,P_y)」を床と読まなかった(CAL の語形に無い)。本書は**読みで床に数える**(規則の数と読みの数を両方書く)。
- Think は thinking の最初の語を自分で「Okay」と書く(B1・B2 とも・cmt5 の一語と同じ)。

## §1. 数(分母 = 引いた本数・打ち切りも分母に)
| 経路 | 腕 | n | 床(規則 / 読み) | cut(本文 / 答え) | 閉じた | 打ち切り | token 中央値 | 閉じた本の thinking(token・中央値 / 範囲) |
|---|---|---|---|---|---|---|---|---|
| B1 bf16・MLX | K | 10 | **8** / 8 | 10 / 0 | 8 | 2 | 14,457 | 11,203 / 9,411〜14,793 |
| B1 bf16・MLX | none/Q1 | 20 | **5** / 5 | 0 / 0 | 5 | 15 | 16,384 | 9,197 / 5,580〜11,226 |
| B2 Q4・ollama | K | 10 | **6** / 6 | 10 / 0 | 6 | 4 | 14,694 | (未計測・thinking の字数 ≈ 5 万) |
| B2 Q4・ollama | none/Q1 | 20 | **13** / **14** | 0 / 0 | 14 | 6 | 13,816 | 同上 |

- **閉じた本は全部 床に着いた**: B1 K 8 / 8・B1 none/Q1 5 / 5・B2 K 6 / 6・B2 none/Q1 14 / 14(読み)。落ちた本は全部「`</think>` が 16384 までに出なかった」本。
- K(hint に平均比例を書いた腕)でも答えは床の等式(「EJ = KP_y」)で、hint の形を答えに写した本は 0。= Think は切断でなく床へ commit する(Claude の none/Q1 と同じ答えの欄)。
- 答えの語形(B2): 「EJ = KP_y」「|EJ| = |KP_y|」「EJ equals KP_y」「EJ equals KPy」「EJ = PyK」「distance(E,J) equals distance(K,P_y)」。

## §2. 予想(PREREG §3)との照合
| 予想 | 実 | 当否 |
|---|---|---|
| PB1-1 B1 none/Q1 の床 4〜12 / 20 | 5 | 当たり |
| PB1-2 B1 K の cut(答え)≥ 5 / 10 | 0(答えは床) | **外れ** |
| PB1-3 B1 打ち切り ≤ 6 / 30・閉じる ≥ 24 / 30 | 17 / 30・13 / 30 | **外れ**(思考が長い) |
| PB2-1 B2 の床 = B1 ± 4 | K 6 対 8(内)・none/Q1 13 対 5(**外**) | **外れ**(経路で変わる) |
| PB2-2 B2 の打ち切りは B1 より多い | B2 10 / 30 対 B1 17 / 30 | **外れ**(逆) |

## §3. 比較表(OLMo の列・olm1〜olm3 の統合)
| model・条件 | none/Q1 床 | K 床 | 打ち切り(none/Q1) | 答えて止まる |
|---|---|---|---|---|
| Opus 5.5(xhigh・API) | 20 / 20 | — | 0 | 止まる |
| Fable 5.1(xhigh・API) | 20 / 20 | — | 0 | 止まる |
| OLMo-3 32B base・natural(6144) | 0 / 20 | 0 / 10 | 8 / 20 | 半分は即 EOS・残りは短い誤答か打ち切り |
| OLMo-3 32B base・think `Okay`(6144) | 2 / 20 | 2 / 10 | 14 / 20 | 止まらない(olm2 C: 16384 でも 9 / 20) |
| OLMo-3 32B base・think `Okay`(16384) | 3 / 20 | — | 9 / 20 | 同上 |
| **OLMo-3 32B Think・bf16 MLX(16384)** | **5 / 20** | 8 / 10 | 15 / 20 | 考え終えれば止まり床に着く |
| **OLMo-3 32B Think・Q4 ollama(16384)** | **13〜14 / 20** | 6 / 10 | 6 / 20 | 同上・思考が短い |

## §4. 読み(`L3`・札の範囲で)
- **事後学習が入れたのは「答えて止まる」**: base(olm1 / olm2)は語も計算も出すが commit しない。Think は `</think>` を閉じた本が例外なく床に着く。落ちるのは思考の長さ(5.6k〜11k token で閉じる本と、16384 でも閉じない本の二山)。
- **B1 と B2 の差(none/Q1 の床 5 対 13)は model でなく経路に由来する部分が大きい**: 閉じた本の床は両方 100% で、差は「16384 までに閉じるか」の差。候補 = (a) ollama の既定 `top_k 40`(尾を切り、彷徨いを短くする)対 MLX の top_k なし、(b) renderer の違い(system の有無・token の並び)、(c) Q4 の量子化。どれかは本札では決められない(切り分ける札 = B1 に top_k 40 を入れる / B2 に top_k 0 を入れる)。
- **朝の門(moy-5 の活性化の分析)への答えの更新**: base には入口が無い(olm1 / olm2)が、**Think には床に着く行が在る**(B1 5 本・B2 14 本)。lens を張った model が base なので、内側を読む道は「Think の床の行を base で再生する」のではなく、Think 自身に lens を張り直すか、Think の床の行の prefix(thinking)を base に与えて続きを読む、のどちらか(先生の裁定)。
- K で hint の切断を答えに写さず床へ行くのは、moy-5 の答えの欄が床に閉じている(neq 札「問いの点の集合が答えの欄の関係の族を限る」)の Think での instance。

## §5. 主張しないこと
- PREREG §5 のまま + §0 の開示(描画と sampler が二経路で同一でない)。一つの作図・一つの配置・温度 0.6 の抽選・各 n 20。
