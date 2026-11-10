HEAD(R1) = a32fba49(凍結の時)

# BRIEF v3.1 — 駅 2(moy-1)の受領版を一つに合わせる: 前半 = P・後半と後から足した部分 = Q + 監査 14 件の直し(2026-11-06・職場)

- 発(逐語・先生 11-06): 「1 推しで進めます」(= [RESULT C4](receipt_read/RESULT_C4_receipt_v3_read_with_yardstick_v2_20261106.md) §5-1 の受領 = 読み手の案「前半 P・後半 Q を土台に、他方から移す」)。受領条件 = 「次が見えるか」・二口 = バラツキの発見・勝者を選ぶのでなく差を見極めてより良いものを受領する。
- 作り手 = 一人: `entry_v3_1_received`(Opus 5.5・effort xhigh)。置き場 = `/Users/manabu/lancedb-rag/conversations/2026-11-06/coread_station2_3/station2_moy1/receipt/entry_v3_1_received/`。scratch = 依頼の文に書く。終わりの印 = 置き場に `DONE`。**commit しない**。
- **R16 の見積もり(先生「エージェントは上限を見積もって起動」)**: 前の作り手は Opus 97 分・83.5 万 token / Sonnet 144 分・45.9 万 token(状態 38〜43 の全部を作った)。この仕事は合わせる作業 = それ以下の見込み。**打ち切り 120 分**。撮影を一度に全部読まない(見るのは直す状態と検査の撮影だけ・NOTES / CLAIMS は節ごとに読む = Read の上限 2.5 万 token を越える file は offset で)。60 分を過ぎたら NOTES の頭に進み具合を一行。

## §1 材料(読むだけ)

- **P** = `receipt/entry_v3_opus_xhigh/`(38 状態)・**Q** = `receipt/entry_v3_sonnet_max/`(43 状態)。どちらも書き換えない。
- **土台 = Q の build**(43 状態・15 章)。状態 0〜12 の範囲は **P の見せ方を採る**(読み手は二人とも P を土台にした)。
- 読み手の返答(逐語・読むだけ・path は `receipt_read/reads/`): D1_R2・D1_R3(状態 0〜12 = P を土台に Q から移す物)・D2_R2・D2_R3(10-28 の部分の残り = Q を土台に P から移す物)・D3_R2・D3_R3(後から足した部分と台帳 = Q を土台に P から移す物 ①〜⑧)・G3_R2(監査 14 件)。
- skill = `/Users/manabu/lancedb-rag/.claude/skills/coread-explainer/SKILL.md` と `references/`。描き方 = `~/.claude/skills/anatomy` の kit(MIT・Copyright (c) 2026 Ryan の表示を残す)。

## §2 やること(順)

1. Q の build を scratch に写して v3.1 とする。
2. **状態 0〜12**: P の見せ方にする(P の該当の状態の描き方・文を Q の build に移す)+ D1 の二人が「Q から移す」とした物を足す(重なった物 = s07 の窓の定義「line / slope と共に = ±80 字」・s09 の単位「直径 = He・Hi の文がある blocked の 5 行」・s12 の「5 章の行の cue は \n\n」)。片方だけの物は自分で決めて NOTES に理由。
3. **状態 13〜26(10-28 の部分の残り)**: Q のまま + D2 の二人が重なった物(P s22 の「Δmath の中央値で割る」の列・P s22 の「札の外の数」の箱 0.781 / 0.221 / 0.489 を Q s23 の切れた行と置き換え)+ 片方だけの物は自分で決める。
4. **後から足した部分と台帳(Q 27〜42)**: Q のまま + D3 の二人が重なった物(P #s26 の出所の分け = 太線 / 点線と札の一覧表・P #s28 の「+0.02 は olm86 を見てから置いた」の注・P #s30 の Opus 8 / 8 の棒(別の札・chat model と明記)・P の R01 の限定)。
5. **決めておく規則**(依頼者の決め = この BRIEF):
   - 札の印 = その状態が読む data の札(P の規則・build が導く)。ただし **10-28 の後の札は 10-28 の状態に載せず、後から足した部分で示す**(Q の規則)。
   - 後の札の数 = 判定に届いた札。統制や関門で止まった札(olm83・olm88・olm95 など)は「関門で止まった」の欄に別に数える(数の規則を図に一行)。
   - olm89 / olm92 の線 = **凍結の +0.01 を判定の線**・+0.02 は「olm86 を見てから置いた(事後)」の注。
6. **data で決める食い違い**(決め方を NOTES と CLAIMS の anchor に): s17 の base open の attractor 5 か 4 か(上限で切れた行の扱いを凍結の規則で)・s18 の語の位置 k −20 か −19 か(数え直す)・olm76 の凍結 commit(git log で確かめる)・Q s23 で切れていた値と P の 0.781 / 0.221 / 0.489 の照合。
7. **監査 14 件の直し**(G3_R2): とくに G-01 = olm76 の「上がらない / 立たなかった」→「**線に届かない**(28 / 48 の行で上がった・中央値 +0.013・p 0.156)」(SCOPE 11-01 の言い方)を、見出し・台帳・言えない・受け入れの問いの全部で。
8. 検査: `check_claims.py` の anchor・`run_checks.sh` を全部通す。撮影は video の 1920 × 1080(ja / en)と検査に要る物だけ(phone・desk の全数は要らない)。

## §3 守ること

- install・通信・git の書き込みはしない。実験の script を import も実行もしない(data を読むだけ)。model を動かさない。subagent は使わない。
- Bash は単純な command に分け、cd を含む command を並べない。port は 27900〜27999 だけ。Chrome の `--user-data-dir` は自分の scratch。
- 道具: bun = `/Users/manabu/.bun/bin/bun`・node = `/Users/manabu/miniforge3/envs/py314/bin/node`・python = `/Users/manabu/miniforge3/envs/py314/bin/python`・Chrome = `/Applications/Google Chrome.app` の headless。
- 打ち切り 120 分。返すもの ≤ 10 行: 状態の数・P から採った範囲と移した物・決めた食い違い・直した監査の件数・撮影の枚数・anchor・検査の結果・所要と一番自信の無い点。
