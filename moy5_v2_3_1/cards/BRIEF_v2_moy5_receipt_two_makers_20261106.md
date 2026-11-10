HEAD(R1) = 5591367b(凍結の時)。先生 11-06 17:2x「C5凍結」で凍結(起案 = `BRIEF_v2_moy5_receipt_two_makers_20261106_DRAFT.md`・未決を C4 と v3.1 の教訓で埋めた)。

# BRIEF v2 — 駅 3(moy-5)の受領版を新しい二口で作る: 土台 Q + P からの移植 + 監査の直し + 「次まで見せる」(2026-11-06・職場)

- 発(逐語・先生 11-06): 「1 両方 2 次まで見せる」(駅 2 の時の裁定・同じ形を駅 3 に)/「2 / 3 / 4 は今走っているものを含めてチェックリストを作って順次進めます」(2 = 駅 3 の受領版)/「C5凍結」。前段 = [RESULT 駅 3](RESULT_station3_moy5_next_visible_two_maker_variation_20261106.md)。
- 受領条件(先生 11-06): **「次が見えるか」**。二口 = バラツキの発見。勝者は選ばない。
- 作り手 = 新しい二口: `entry_v2_opus_xhigh`(Opus 5.5・effort xhigh)/ `entry_v2_sonnet_max`(Sonnet 5.5・effort max)。同じ土台から、互いを見ずに作る。
- 置き場 = `/Users/manabu/lancedb-rag/conversations/2026-11-06/coread_station2_3/station3_moy5/receipt/<あなたの entry>/`。scratch = 依頼の文に書く(あなた専用)。終わりの印 = 置き場に `DONE`。**commit しない**。
- **R16 の見積もり(先生「エージェントは上限を見積もって起動」)**: 駅 2 の同じ型の作り手 = Opus 97 分・83.5 万 token / Sonnet 144 分・45.9 万 token。**打ち切り 180 分**。撮影を一度に全部読まない(見るのは直す状態と検査の撮影だけ)。Read の上限 2.5 万 token を越える file は offset で節ごとに読む。開始の時刻を NOTES の頭に書き、90 分を過ぎたら進み具合を一行。

## §1 土台と材料(読むだけ)

- **土台 = entry Q** = `/Users/manabu/lancedb-rag/conversations/2026-10-28/explainer_moy5/entry_opus_xhigh_v1/`(冷間の読み手二人がともに土台に選んだ方)。scratch に写して v2 として作る。元の folder は書き換えない。
- **移植の元 = entry P** = `/Users/manabu/lancedb-rag/conversations/2026-10-28/explainer_moy5/entry_sonnet_max_v1/`(読むだけ)。
- 読み手の返答(逐語・読むだけ): `reads/D_R1/judge_reply.md`・`reads/D_R2/judge_reply.md`(差と移植の案・★ = 各 8)・`reads/G_R1/judge_reply.md`(監査の直し 24 件)・`reads/N_*/judge_reply.md`・`reads/T_*/judge_reply.md`(読み手が出した次の問い)。path はこの BRIEF の folder から。
- 「その後」の材料(読むだけ・値は RESULT の実出力から写す = R4):
  - `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md`(線 2 = moy-5 の言える / 言えない)
  - moy-5 の札の RESULT(10-28〜10-31): olm60・olm61・olm63・olm64・olm67〜74・olm77〜82(`conversations/2026-10-2*/RESULT_olm*_moy5_*.md`・`conversations/2026-10-3*/RESULT_olm*_moy5_*.md`)・thk1・thk2(`conversations/2026-10-30/RESULT_thk*_moy5_*.md`)。§1〜§2 と言えないだけでよい。
- skill = `/Users/manabu/lancedb-rag/.claude/skills/coread-explainer/SKILL.md` と `references/` を全部読む。描き方 = `~/.claude/skills/anatomy` の kit(MIT・Copyright (c) 2026 Ryan の表示を残す)。

## §2 やること(順)

1. **移植**(二人の読み手が重なった物は必ず・片方だけの物は自分で決めて NOTES に理由): P の状態 7・8 の軌跡を答えにした本の数(両 model・Q2 + 名 / 本文まで)・状態 7 の Q1 の陽性統制 K・状態 13 の thinking の中央値(jsonl から数えた値)・状態 3 の手がかりごとの要約の道・状態 21 の OLMo の K(olm1 の訂正の banner を確かめてから)。
2. **食い違いを data で決める**(決め方を NOTES に・CLAIMS の anchor に): ① Argon の thinking の比(8.2 対 8.3)と中央値の出所(data 対 SUMMARY)② 陽性統制 K の札(mnw1 n 10 対 essay4 n 20・essay4 Fable K r17 の保存値と SUMMARY の食い違い)③ olm1 の訂正の banner が OLMo の K に効くか ④ prf1 P5 の apex の述語(latx 対 CHAIN / LAT-only)。
3. **監査の直し**(`reads/G_R1` の 24 件): とくに G-03 = 台帳(状態 23)の言えないの 1 行目「欠如として説明しない: 渡せば束ねる・塞げば持ち出す・effort max 19 / 20」を「**欠如とも保有とも言わない**」に(中の状態の含意を言えないの欄から外す)。G-02(P の全画面の頭の「誘導」)は、P から移植する部分に当たる時だけ直す。機構の語・因果の語は SCOPE 10-31 の言えないに合わせる。
4. **「次まで見せる」の章を足す**(新しい章・状態の数は自分で決める): 10-28 の図(frontier の出力の側 = effort・経路・thinking の量・読み取り器)が見せていた問いと、家がその後に打った札(**OLMo の内側で frontier の道を読む側**)とその結果を、図の上で一本の流れとして見せる。
   - (a) frontier の道を OLMo に読ませる(olm60・61・64・67): 方向 d̂・SAE の群・言語空間。
   - (b) cut の文の前触れ(olm68〜74・77〜79・81・82): 何 token 前から寄るか・補助定理の腕・自分の語の計器の較正・語順・一語ずつ。
   - (c) 層 32 の残差は語を越えるか(olm80)・SAE が使える条件(olm63)。
   - (d) frontier の思考の要約(thk1・thk2)。
   - 各札に、凍結の commit・判定の格(判定 / 確かめた記述 / 記述 / 言えない)・出所の file と key。**図の 10-28 の部分と、その後の部分を見た目で分ける**。
5. **次の問いの状態**(§5)を最後の章の前に置く。
6. 台帳を SCOPE 10-31 の「言えない」で更新する。
7. **決めておく規則**(依頼者の決め・駅 2 の v3.1 と同じ): 札の印 = その状態が読む data の札(build が導く)。ただし **10-28 の後の札は 10-28 の状態に載せず、後から足した部分で示す**。後の札の数 = 判定に届いた札。統制や関門で止まった札は「関門で止まった」の欄に別に数える(規則を図に一行)。事後に置いた線は、凍結の線と別の線種で「事後」と書く。
8. **読まれ方への配慮(11-06 の読み手の暴走の教訓)**: NOTES.md と CLAIMS.md は**一本 60 KB 以下**にする(越えるなら章ごとの file に分け、README に一覧)。冷間の読み手が Read の上限の内で読めるように。

## §3 受領の物差し(あなたの図はこう読まれる)

- 物差し v2([FREEZE](../yardstick_v2/FREEZE_yardstick_v2_20261106.md)): 冷間の読み手(Opus / Sonnet・章ごとに分けて読む)が図だけを見て、次の問いを **A1 図の中の確かめ / A2 図の外へ出る次** の二つの欄に書く。図が自分で書いている次(§5 の候補を含む)は数えない。読み手の次は前向きの台帳に登録し、納品の後に家が凍結する moy-5 の札と後日照らす(駅 2 の C4 と同じ)。+ 二つの v2 を並べて差を読む(D)。
- 監査(数・出所・言えない)は AI の関門で、受領を決めない。ただし `check_claims.py` の anchor・`run_checks.sh` は全部通すこと。

## §4 守ること

- install・通信・git の書き込みはしない。実験の script を import も実行もしない(data を読むだけ・数え直しは自分の pack で)。model を動かさない。subagent は使わない。
- Bash は単純な command に分け、cd を含む command を並べて走らせない。
- port は自分の帯だけ: `entry_v2_opus_xhigh` = 27700〜27799・`entry_v2_sonnet_max` = 27800〜27899。Chrome の `--user-data-dir` は自分の scratch。
- 道具: bun = `/Users/manabu/.bun/bin/bun`(1.3.0)・node = `/Users/manabu/miniforge3/envs/py314/bin/node`(v26.2.0)・python = `/Users/manabu/miniforge3/envs/py314/bin/python`(anywidget 0.11.0・marimo 0.23.13)・Chrome = `/Applications/Google Chrome.app` の headless。
- 打ち切り 180 分。撮影は video の 1920 × 1080(ja / en)と検査に要る物だけ。返すもの ≤ 10 行: 状態の数・章・移植した物・決めた食い違い・直した監査の件数・撮影の枚数・照合の結果(N / N)・検査の結果・所要・一番自信の無い点。

## §5 次の問いの状態(先生の選択 = まだ無い・C7)

- 読み手が出し、家がまだ打っていない次(駅 3 の N4・RESULT §1 の束)を図の上に並べる。図は推さない(採否は先生と書く)。
  - ① thinking の量で行を分ける(同じ札・同じ effort の中で cut の行と無い行・model を thinking の一本の軸に)= 8 問
  - ② 経路 × effort の 2 × 2(β′ の全体の cut を動かすのは経路か effort か)= 4 問
  - ③ 点の集合 × 足した文(Q1 の {E, J, K, P_y} と Q2 の {F, V, P_x, P_y})= 5 問
  - ④ 塞ぎの一文を禁止と指図に分ける = 3 問
  - ⑤ 読み取り器の割れ(v1 / v2 / 人)= 4 問
- 先生の選択はまだ無い(C7)= 図は五つの束を並べるだけで、強調しない。
