HEAD(R1) = e9b2b78d(凍結の時)。先生 11-06「3 推しのAで進む」で §5 を埋めて凍結(起案 = `BRIEF_v3_moy1_receipt_two_makers_20261106_DRAFT.md`)。

# BRIEF v3 — 駅 2(moy-1)の受領版を新しい二口で作る: 土台 P + Q からの移植 + 監査の直し + 「次まで見せる」(2026-11-06・職場)

- 発(逐語・先生 11-06): 「1 両方 2 次まで見せる」(= 受領版を新しい二口で作り、物差しも直す / 受領版は 10-28 の図の後に家が打った札まで足して「次がどうなったか」まで見せる)。前段 = [RESULT 駅 2](RESULT_station2_moy1_next_visible_two_maker_variation_20261106.md)。
- 受領条件(先生 11-06): **「次が見えるか」**。二口 = バラツキの発見。勝者は選ばない。
- 作り手 = 新しい二口: `entry_v3_opus_xhigh`(Opus 5.5・effort xhigh)/ `entry_v3_sonnet_max`(Sonnet 5.5・effort max)。同じ土台から、互いを見ずに作る。
- 置き場 = `/Users/manabu/lancedb-rag/conversations/2026-11-06/coread_station2_3/station2_moy1/receipt/<あなたの entry>/`。scratch = 依頼の文に書く(あなた専用)。終わりの印 = 置き場に `DONE`。**commit しない**。

## §1 土台と材料(読むだけ)

- **土台 = entry P** = `/Users/manabu/lancedb-rag/conversations/2026-10-28/explainer_moy1/entry_sonnet_max_v2_1/`(冷間の読み手二人がともに土台に選んだ方)。scratch に写して v3 として作る。元の folder は書き換えない。
- **移植の元 = entry Q** = `/Users/manabu/lancedb-rag/conversations/2026-10-28/explainer_moy1/entry_opus_xhigh_v2_1/`(読むだけ)。
- 読み手の返答(逐語・読むだけ): `reads/D_R1/judge_reply.md`・`reads/D_R2/judge_reply.md`(差と移植の案)・`reads/G_R1/judge_reply.md`(監査の直し 16 件)・`reads/N_*/judge_reply.md`(読み手が出した次の問い)。path はこの BRIEF の folder から。
- 「その後」の材料(読むだけ・値は RESULT の実出力から写す = R4):
  - `conversations/2026-10-30/RESULT_olm76_moy1_commit_window_before_answer_brace_20261030.md`
  - `conversations/2026-11-01/SCOPE_line1_inference_space_after_olm83_92_20261101.md`(§0・§2・§2b・言えない)
  - `conversations/2026-11-02/RESULT_olm112_moy1_apex_status_and_geometric_proof_20261102.md`
  - `conversations/2026-11-02/RESULT_olm114_moy1_frontier_proof_prefix_ladder_20261102.md`
  - 必要なら SCOPE 11-01 が引く RESULT(olm84〜92・olm93〜98・olm101・olm106・olm108)の §1〜§2 だけ。
- skill = `/Users/manabu/lancedb-rag/.claude/skills/coread-explainer/SKILL.md` と `references/` を全部読む。描き方 = `~/.claude/skills/anatomy` の kit(MIT・Copyright (c) 2026 Ryan の表示を残す)。

## §2 やること(順)

1. **移植**(二人の読み手が重なった物は必ず・片方だけの物は自分で決めて NOTES に理由): Q の #s1(∠O1XkO2 の列)・#s11(`\n\n` を使う理由の一文)・#s12(prompt の編集の差分)・#s17(base の列)・#s18(k −20 の注)・#s20(行ごとの坂と道 × label の内訳)・#s21・#s22(同順位を平均した値の注・出すなら「札の外の数」の札)。
2. **食い違いを data で決める**(決め方を NOTES に・CLAIMS の anchor に): ① blocked s8 の答えの欄(凍結の `label_json_fields` に従う)② open で色が替わる行の数 ③ moy_suite_report の日付の規則 ④ 札の印を付ける規則(data の出所か群の出所か)。
3. **監査の直し**(`reads/G_R1` の 16 件): とくに G-01 = 台帳の L3「結びが下がるのは…まだ答えを閉じていない、と読める」を、olm76 の結果(答えの欄 `{"` の直前 64 token でも結びの群は bind の行で上がらない・28 / 48・+0.013・p 0.156)と同じ行に置き「支持されない読み」に格下げする。機構の言い方(G-02〜G-04 ほか)は SCOPE 11-01 §2b の言えないに合わせる。
4. **「次まで見せる」の章を足す**(新しい章・状態の数は自分で決める): 10-28 の図が見せていた問いと、家がその後に打った札とその結果を、**図の上で一本の流れ**として見せる。
   - (a) 台帳の L3 →「答えの欄の始まりで結びは上がるか」→ olm76 → 上がらない(読みは支持されない)。
   - (b) 推論空間の探し(olm83〜92): 先読みの残差は J-lens の読み出しでほぼ全部読める・k = 8 だけ小さな上乗せ(層 32)= SCOPE 11-01 の判定 / 確かめた記述 / 言えないの段のまま。
   - (c) 語でない構造(olm93〜98・olm101・olm106・olm108): 指示語・束縛・head・入れ替え(指し → 値は層 12〜20)。
   - (d) apex の証明(olm112: 鎖 0 / 37 / olm114: frontier の段を与えると続きを書く 26 / 40)。
   - 各札に、凍結の commit・判定の格(判定 / 確かめた記述 / 記述 / 言えない)・出所の file と key。**図の 10-28 の部分と、その後の部分を見た目で分ける**(後から足したことが一目で分かる)。
5. **次の問いの状態**(§5)を最後の章の前に置く。
6. 台帳を SCOPE 11-01 の「言えない」で更新する。

## §3 受領の物差し(あなたの図はこう読まれる)

- 冷間の読み手(作り手と違う model)が図だけを見て「次に確かめたい問い」を書き、家が後で打った札と照らす(駅 2 の N)+ 二つの v3 を並べて差を読む(D)。**読み手が図の中の数の頑健さだけでなく、図の外へ出る次を書けるか**を見る。
- 監査(数・出所・言えない)は AI の関門で、受領を決めない。ただし `check_claims.py` の anchor・`run_checks.sh` は全部通すこと。

## §4 守ること

- install・通信・git の書き込みはしない。実験の script を import も実行もしない(data を読むだけ・数え直しは自分の pack で)。model を動かさない。subagent は使わない。
- Bash は単純な command に分け、cd を含む command を並べて走らせない(作業 folder を共有するため)。
- port は自分の帯だけ: `entry_v3_opus_xhigh` = 27500〜27599・`entry_v3_sonnet_max` = 27600〜27699。Chrome の `--user-data-dir` は自分の scratch。
- 道具: bun = `/Users/manabu/.bun/bin/bun`(1.3.0)・node = `/Users/manabu/miniforge3/envs/py314/bin/node`(v26.2.0)・python = `/Users/manabu/miniforge3/envs/py314/bin/python`(anywidget 0.11.0・marimo 0.23.13)・Chrome = `/Applications/Google Chrome.app` の headless。
- 打ち切り 180 分。返すもの ≤ 10 行: 状態の数・章・移植した物・決めた食い違い・直した監査の件数・撮影の枚数・照合の結果(N / N)・検査の結果・一番自信の無い点。

## §5 次の問いの状態(先生の選択 = A・11-06「3 推しのAで進む」)

- 読み手が出し、家がまだ打っていない次(駅 2 の N4・RESULT §2 の表)を図の上に並べる。図は推さない(採否は先生と書く)。
- **先生が選んだ候補(強調)= A: cue × JSON からの書き始め × blocked の bind** — 問い = 「blocked で cue を替えた時の bind の差(`\n` 2 / 9・`" "` 4 / 10・`\n\n` 7 / 10)は、cue によって JSON から書き始める行の割合が変わることで説明されるか」。比べる物 = cue 三種の blocked の行の「JSON から書き始めた行」/「文から書き始めた行」。計器 = 最初の `{"conjecture"` の位置 × 凍結の label。出所 = 図の状態(cue の表・書き始めの chips)と、読み手の返答(図の腕・文の腕の両方・両読み手から 6 問)。現状 = 書き始めと label の対応(3 / 3・7 / 7)は `\n\n` の 10 行でしか数えていない。家はこの問いを次の札として起こしている(番号・凍結は依頼の文で知らせる・まだ結果は無い = 「結果は無い」と書く)。
- 選ばれなかった候補(読み手が出した次・並べるだけ): B 図の数の頑健さ(起点・窓・label)/ C cmt13 の二つの瞬間の組の和 / D 数式への移りの非対称(対象か二番目の候補か)/ E blocked s8 の答えの欄の定義(これは §2 の 2 で data から決めるので、図では決めた結果を書く)。
