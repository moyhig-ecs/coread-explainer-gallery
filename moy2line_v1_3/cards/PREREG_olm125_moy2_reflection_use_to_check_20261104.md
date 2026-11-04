HEAD(R1) = 3beeee93(凍結時の HEAD = RESULT olm124 の commit・fetch + pull 済 = Already up to date・origin より 27 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm125`・凍結 2026-11-04): moy-2 の「使って確かめよ」の腕(e)— olm124(式だけ・第二文なし)の問いの文の Tool の段の式の直後に**指示の一行**「Use it to check: compute the reflection with the given coordinates before you rely on it.」を足して OLMo-3 32B base に 60 行書かせ、本文で式を数値で使う率(REFL_CALC・olm124 15 / 60 = 0.250)が上がるか、証明の欄で O1O2 についての線対称を肯定して述べる率(v3 の LN_a・olm124 4 / 37 = 0.108)が動くかを見る。olm119 の第二文は**宣言の文**(「Two points are symmetric … exactly when …」= 前提として植わり +0.196)、この一行は**指示の文**(配置も関係も名指さない)= 植える文と使わせる文の対

- 発注(逐語・先生 11-03 夜): 「**(d) (e) (f) へ順次進みます。**」の (e)。(d') [RESULT olm124](../2026-11-03/RESULT_olm124_moy2_reflection_formula_only_rerun_20261103.md) が 戻る(式そのものは植わらない)だったので、土台は PREREG olm124 §6 のとおり**式だけ + 指示**(残る なら olm119 の TOOL + 指示だった)。主 session の起案・先生の裁定は RESULT の後。
- G10 の欄: 比べる物 = 「式だけ + 指示の一行の問いの文で OLMo が書いた 60 行の本文で、折り返しの式を数値で使った(REFL_CALC)行の割合と、olm124(15 / 60 = 0.250・olm124 の read.json)の同じ割合との差」/「同じ 60 行の証明の欄(空でない物)で、O1O2 についての線対称を肯定して述べる(v3 の LN_a)行の割合と、olm124(4 / 37 = 0.108)の同じ割合との差」/ 計器 = 読み込むだけの凍結の部品(olm122 の `score_row` = hq の proof_of・status_of + olm117 の v2 + olm118 の v3(SYM_PT・SYM_LN・OUTER・asserted)+ olm119 の REFL_MENTION / REFL_CALC + olm121 の v4(本文の記述)+ olm122 の tool_named・較正 12 / 54 / 74)+ 問いの文の guard(TOOL_U を外すと olm124 の md5 `2c4a01a4…`・TOOL_U は TOOL_D の直後に一回・TOOL_U は Tc / Th / O3 / symmetr / collinear / midpoint / parallel / perpendicular / equal を含まない)+ 記述の補助 SUPP_LN / REJ(olm124 の逐語で較正 15 / 15・判定に使わない)/ 雛形 = いいえ
- runner = [olm125_…py](../../ConstructGap/exp/olm125_moy2_reflection_use_to_check_20261104.py)。読み込むだけの部品: [olm122_…py](../../ConstructGap/exp/olm122_moy2_reflection_formula_only_20261103.py)(`78bafa04…`・TOOL_D・score_row・_desc・guard)・[olm124_…py](../../ConstructGap/exp/olm124_moy2_reflection_formula_only_rerun_20261103.py)(`06061244…`・USED_SEEDS・_verdict1 = 参考の帯)とその下の hq(`426e2089…`)・olm117(`ab678f30…`)・olm118(`136f72b9…`)・olm119(`d8d4062f…`)・olm121(`9c0b2b4e…`)。比べる元 = `olm124/read.json`(`ab5250a8…`)・`olm124/gen.json`(`de43caa9…`)・`olm122/read.json`(`30db9a25…`)・`olm118/read.json`(`bffeb826…`)・`olm119/read.json`(`f2138597…`)。走らせる所 = zebrashark(32B は一つずつ・Qwen 0.8B の R3〜R5 の鎖が終わってから発火)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- **olm124 の 60 行の値は全部既知**(RESULT olm124): 証明の欄の LN_a 4 / 37 = 0.108・REFL_CALC 15 / 60 = 0.250・取れた行 45 / 60(境ちょうど)・計算した 15 本のうち折り返しを数値で出した 13 本の 12 本が「Not the same」と書く・b2_j07 = 退けた後に証明の欄で線対称・上限 9 本・短い指示の続き 6 本。主 session は olm124 の証明の欄の LN 4 本・形に無い 3 本・計算した 15 本・式に触れた 13 本の一部を逐語で読んだ。**§3 の予想はこれを織り込む**。
- **指示の一行(TOOL_U・逐語)**: 「Use it to check: compute the reflection with the given coordinates before you rely on it.」(90 字・改行 1)。置き場 = TOOL_D の式の直後(Tool の段の三行目)。**配置も関係も名指さない**(guard)= olm119 の第二文(O1O2 についての対称を定義する宣言の文)と違い、何が対称かは言わない。問いの文の md5 = `718d1601…`(土台 olm124 `2c4a01a4…`・1,633 → 1,723 字)。
- **Q2 は G1 で止めない**(開示): REFL_CALC は 60 行全部に定義される(取れなかった行・上限の行でも数える = olm124 の計算した 15 本のうち 5 本は NONE)。指示が計算を増やせば行が長くなり上限 → 取れる率が下がる(olm124 の計算した行の上限 4 / 15)。G1 で Q2 まで止めると「指示が効いたせいで判定がない」になるので、Q2 は G0 だけ、Q1(証明の欄の率)は G1 で止める。
- 記述の補助(判定に使わない): SUPP_LN = v3 の形に無い「reflect(ing) <Tc|Th|O3> across / over O1O2」(目的語に of 無し・olm124 で 3 本)を証明の欄に / REJ = Tc / Th を O1O2 で折り返す計算の始まりから 700 字の中で「not the same / is not Th / doesn't match / not exact / different」と書く行(本文)。**較正 = olm124 の逐語**(SUPP 陽性 3 / 陰性 3 = 式の写し・軸 l1・O3 での折り返し / REJ 陽性 5 / 陰性 4 = 中点の計算・O3 の折り返し・O3 での点対称・退けの語なし)= 15 / 15。
- smoke(凍結の前・2 行・読まない): 数は §6。

## §1. 計器(R5・R6)

- **問いの文** = olm124 の問いの文 + TOOL_U。生成 = olm124 と同じ(温度 0.7・max_new 12288・3 batch × 20 行・seed 20261186〜88・既出の 63 seed と重ねない = guard)。
- **凍結の読み**(読み込むだけ): olm122 の `score_row`(v2・v3・REFL・v4 の RETR / KEPT・tool_named)。集計 = olm122 の `_desc`。帯はこの札(§3)。
- 率の分母: Q1 = 証明の欄が空でない行(olm124 37)・Q2 = 60 行。
- 記述の補助: `supp_ln`(証明の欄)・`rej`(本文)・REJ かつ証明の欄 LN_a(b2_j07 の型)・指示の一行の写し(「rely on it」「use it to check」の逐語)。

## §2. 関門

- **G0**: 部品(olm122・olm124 とその下 5 本)・比べる元 5 本の md5 一致・較正 12 / 54 / 74 + SUPP / REJ 15 / 15・olm113 n_proof 41・olm119 n_proof 44・olm124 の取れた 45 / 証明 37 / LN 0.1081 / RC 0.25 / G1 true / 判定 戻る(read.json の記録)。
- **G1**(Q1 だけ): conjecture が取れた行 **≥ 0.75(45 / 60)**(olm124 と同じ較正・四腕 0.833 / 0.800 / 0.767 / 0.750)。✗ → Q1 を読まない(Q2 は読む・§0)。
- **G2**(記述の側): status が hypothesis / question の行 ≥ 0.70(42 / 60)。✗ → 注記(olm124 は 32 / 60 で ✗)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q2(主)** | 本文で式を数値で使った率 rc = REFL_CALC / 60(olm124 0.250) | **上がる** rc ≥ 0.40(24 / 60)・**下がる** rc ≤ 0.10・ほか = **変わらない** | 上がる 0.60・変わらない 0.37・下がる 0.03 |
| Q1 | 証明の欄の LN_a の率 r・Δ124 = r − 0.108 | **変わらない** \|Δ124\| < 0.06・**下がる** Δ124 ≤ −0.06(r ≤ 0.048 = 1 / 37 以下)・**上がる** Δ124 ≥ +0.06(r ≥ 0.168 = 7 / 37 以上) | 変わらない 0.50・下がる 0.35・上がる 0.15 |
| Q3 | 記述: 取れた行と取れなかった行の形(T・指示の続き / 上限・olm124 と並べる)・計算した行の数と REJ(数値で出して「違う」と書いた)の数・REJ かつ証明の欄 LN_a(b2_j07 の型)の数・SUPP_LN の数(四腕と並べる)・MIDO3 / EQ・証明の欄の PERP3 / OUTER・v4 の RETR・類ごと・tool_named・指示の一行を写した行の数・T・上限 | — | — |
| Q4 | 記述: 逐語 = 証明の欄の LN(全部)・REJ かつ証明の欄 LN の行(全部)・計算した行の計算の文と結果の文(最大 10 本)・式に触れたが計算しなかった行(最大 5 本)・指示の一行に触れた行(最大 5 本)・取れなかった行の頭(全部) | — | — |

- 読みの軸(開示): **Q2 上がる** → 指示の文は base に効く(計算させる)= olm114 の「JSON だけの文は効かない」と olm119 の「宣言の文は植わる」の間に「指示の文は使わせる」が置ける。**Q2 変わらない** → 指示の一行も読まれるだけ(道具は使われるより読まれる・olm119 §4)。**Q1 下がる** → 使わせれば退けが増え、証明の欄の記憶が減る(olm119 で「使った行では L3 のとおり直る」)。**Q1 変わらない** → 計算して退けても証明の欄は記憶で埋まる(b2_j07 の型)か、計算した行が上限で証明の欄に至らず分母から消える。**Q1 上がる** → 指示が「reflection」の語を一度多く置くことで線対称の記憶が増える(植える効果の別経路)。
- 予想の根拠: Q2 = olm113 の JSON の指示は約 0.75 で従われる(取れる率)ので、計算の指示も半分前後は従われると見る(0.25 → 0.40〜0.60)。ただし base は指示を「続ける」ことがある(olm124 b0_j01「Does it use the reflection tool?」)ので 変わらない を 0.37 残す。Q1 = olm124 の証明の欄の LN 4 本のうち 3 本は計算しない行なので、計算する行が増えれば分子は減るが、計算した行は上限で分母からも消える = 率は動きにくい(変わらない 0.50)。
- Q2 の帯の根拠: 60 行の一行 = 0.017・0.25 の SE ≈ 0.056。+0.15(9 行)は約 2.7 SE。

## §4. 読み方

- `--read` が `olm125/read.json` を書く(関門・Q1〜Q3・集計・行ごとの類と印・supp_ln / rej・取れなかった行の T)。判定は v3 の LN_a と REFL_CALC の値だけで、この札の 60 行だけで付ける。
- RESULT では §3 の Q4 の逐語を引き、olm124 の同じ値を並べる。主 session の読み(使わせる効果と植える効果・REJ の逐語)は値と並べ、違っても判定は変えない。olm124 の帯(olm113 / olm119 との距離・`_verdict1`)は参考として書く。

## §5. 主張しないこと

- 判定は新しい 60 行だけ。olm124 との差は問いの文の一行の有無だが、seed も違う(同じ seed で走らせ直す腕はない = olm122 → olm124 の 0.108 / 0.108・0.200 / 0.250 の幅が「同じ問いの文の二回」の目安)。
- TOOL_U は問いの文を 90 字長くし、「reflection」の語を一度多く置く。Q1 の動きを指示の効果だけに帰さない(§3 の軸の三つ目)。
- SUPP_LN / REJ は記述の補助で、較正は olm124 の逐語 15 例(陽性統制は olm124 の行 = 同じ model の文)。判定に使わない。v6 で正式に足すかは別の札。
- Q2 を G1 で止めないのは §0 の理由による設計で、olm124 までの札(両方 G1)と違う(開示)。
- 正しさの率は測らない。一つの model・一つの温度・60 行。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・27 項目・較正 SUPP / REJ 15 / 15・REFL 12 / 12・v3 54 / 54・v4 74 / 74・guard)→ `--smoke`(凍結の前・2 行・max_new 1536・読まない)→ 凍結 → Qwen の R3〜R5 の鎖(0.8B・別件)が終わってから `--gen`(約 3 時間の見込み・olm124 は 2.90 時間)→ `--read`。
- smoke(凍結の前・seed 20261189・2 行・max_new 1536・読まない・zebrashark 11-04 00:47:06〜00:48:53 JST・壁時計 102 s・Traceback 0・Qwen 0.8B の鎖と同時・`olm125/smoke.json`・`smoke_run.log`): 行 1 = T 348・status hypothesis・証明の欄 277 字 / 行 2 = T 196・hypothesis・証明の欄 310 字。本文は読んでいない(smoke の log は類・LN・REFL を印字しない)。runner の md5 = `e1c2f85d…`(selftest PASS 27 項目・較正 15 / 15)。
- 出力 = `ConstructGap/exp/olm125/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-04/RESULT_olm125_moy2_reflection_use_to_check_20261104.md`。
