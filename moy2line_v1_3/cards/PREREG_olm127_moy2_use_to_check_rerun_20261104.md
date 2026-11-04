HEAD(R1) = ef1ea105(凍結時の HEAD = RESULT olm126 の commit・fetch + pull 済 = Already up to date・origin より 32 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm127`・凍結 2026-11-04): moy-2 の「使って確かめよ」の腕の走らせ直し(e')— olm125(式だけ + 指示の一行「Use it to check: compute the reflection with the given coordinates before you rely on it.」・問いの文 md5 `718d1601…`)と**逐語同じ問いの文**で OLMo-3 32B base に新しい seed 20261200〜02 の 60 行を書かせ、証明の欄で O1O2 についての線対称を肯定して述べる率(v3 の LN_a)が olm125(9 / 40 = **0.225**)に残るか olm124(4 / 37 = **0.108**)に戻るかを見る(olm122 → olm124 の走らせ直しの型)。olm125 の「上がる」(Δ124 +0.117・Fisher 参考 0.23)が一回の揺れか二回で立つかの判定

- 発注(逐語・先生 11-04 朝): 「**進みます**」(= RESULT olm126 の「先生の裁定待ち: 同じ問いの文(olm125)の走らせ直し / 対照の一行 / v7」の先頭から)。対照の一行と v7 はこの札の後(起案は先生の裁定の後)。
- G10 の欄: 比べる物 = 「olm125 と逐語同じ問いの文で OLMo が新しい seed で書いた 60 行の証明の欄(空でない物)で、O1O2 についての線対称を肯定して述べる(v3 の LN_a)行の割合と、olm124(4 / 37 = 0.108・olm124 の read.json)および olm125(9 / 40 = 0.225・olm125 の read.json)の同じ割合との差」/「同じ 60 行の本文で、折り返しの式を数値で使った(REFL_CALC)行の割合と、olm125(18 / 60 = 0.300)の同じ割合との差(帯は olm124 の 0.25 を挟む olm125 の帯)」/ 計器 = 読み込むだけの凍結の部品(olm122 の `score_row` = hq の proof_of・status_of + olm117 の v2 + olm118 の v3(SYM_PT・SYM_LN・OUTER・asserted)+ olm119 の REFL_MENTION / REFL_CALC + olm121 の v4(本文の記述)+ olm122 の tool_named・較正 12 / 54 / 74)+ olm124 の `_verdict1` を(olm124, olm125)の対で(戻る / 残る / 上がる / 下回る)+ olm125 の `_band2`(Q2)+ 問いの文の guard(md5 = olm125 の `718d1601…`・olm125 の guard 一式)+ 記述の補助(olm125 の `_extra` = SUPP_LN / REJ / 写し・olm126 の v6 = `score_v6` の LN6_a / OUTER6_a・`rej6`・較正 144 / 144・判定に使わない)/ 雛形 = いいえ
- runner = [olm127_…py](../../ConstructGap/exp/olm127_moy2_use_to_check_rerun_20261104.py)。読み込むだけの部品: [olm125_…py](../../ConstructGap/exp/olm125_moy2_reflection_use_to_check_20261104.py)(`e1c2f85d…`・問いの文・`_extra`・`_band2`・USED_SEEDS)・[olm126_…py](../../ConstructGap/exp/olm126_moy2_v6_par_window_ln_object_rej_20261104.py)(`d180725d…`・v6・参考)・[olm124_…py](../../ConstructGap/exp/olm124_moy2_reflection_formula_only_rerun_20261103.py)(`06061244…`・`_verdict1`)・[olm122_…py](../../ConstructGap/exp/olm122_moy2_reflection_formula_only_20261103.py)(`78bafa04…`・`score_row`・`_desc`)とその下(hq・olm117・olm118・olm119・olm121 = olm125 の guard が確かめる)。比べる元 = `olm125/gen.json`(`32a0298a…`)・`olm125/read.json`(`d0171213…`)・`olm124/read.json`(`ab5250a8…`)・`olm126/read.json`(`862327c3…`)。走らせる所 = zebrashark(32B は一つずつ・他の 32B の仕事なし)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- **olm125 の 60 行の値は全部既知**(RESULT olm125): 証明の欄の LN_a 9 / 40 = 0.225・REFL_CALC 18 / 60 = 0.300・取れた 45 / 60(境ちょうど)・線対称が増えたのは計算しない行(3 / 30 → 7 / 31)・計算した 18 本のうち 13 本が数値で退け・MIDO3 0.444・tool_named 18・指示の写し 1・短い指示の続き 10・上限 5。v6 の参考値(olm126): LN6_a 11 / 40 = 0.275・REJ6 15・b2_j07 の型 3。主 session は olm125 の証明の欄の LN 9 本・計算した 18 本の大半・取れなかった 15 本を逐語で読んだ。**§3 の予想はこれを織り込む**。
- 同じ問いの文の二回の目安 = olm122 → olm124(式だけ)の 0.108 / 0.108・0.200 / 0.250(線対称は同じ値・計算は +0.05)。
- 帯(olm124 の `_verdict1` を (0.108, 0.225) の対で): **戻る** |r − 0.108| < 0.06(0.048 < r < 0.168)・**残る** |r − 0.225| < 0.06(0.165 ≤ r < 0.285)・**上がる** r ≥ 0.285・**下回る** r ≤ 0.048。二つの元の差 0.117 < 0.12 なので **間 は無く**、0.165〜0.168 は重なり(戻る が先・n_proof 36〜44 でこの幅に落ちる分数は 6 / 36 = 0.167 だけ = 戻る・開示)。
- **Q2 は G1 で止めない**(olm125 §0 と同じ理由: 60 行全部に定義・計算が増えると取れる率が下がる)。
- smoke(凍結の前・2 行・読まない): 数は §6。

## §1. 計器(R5・R6)

- **問いの文** = olm125 の問いの文(逐語・md5 `718d1601…`・guard)。生成 = olm125 と同じ(温度 0.7・max_new 12288・3 batch × 20 行・seed 20261200〜02・既出の 67 seed と重ねない = guard)。
- **凍結の読み**(読み込むだけ): olm122 の `score_row`(v2・v3・REFL・v4 の RETR / KEPT・tool_named)。集計 = olm122 の `_desc`。帯 = olm124 の `_verdict1`(対を替える)・olm125 の `_band2`。
- 率の分母: Q1 = 証明の欄が空でない行(olm125 40・olm124 37)・Q2 = 60 行。
- 記述の補助(判定に使わない): olm125 の `_extra`(SUPP_LN・REJ・REJ かつ証明の欄 LN_a・指示の写し)・olm126 の v6(証明の欄 LN6_a / OUTER6_a・本文 REJ6・REJ6 ∧ 証明の欄 LN6_a)・pool 120 行(olm125 + この札)の LN_a と REFL_CALC の率(参考・判定に混ぜない)。

## §2. 関門

- **G0**: 部品(olm125・olm126・olm124・olm122 とその下 5 本)の md5・比べる元 4 本の md5・較正 12 / 54 / 74 + olm125 の 15 / 15 + v6 の 144 / 144・olm125 の取れた 45 / 証明 40 / LN 0.225 / RC 0.30 / G1 true / Q1 上がる / Q2 変わらない・olm124 の LN 0.1081 / RC 0.25 / 戻る・olm126 の Q2 同じ / LN6(olm125)0.275(read.json の記録)。
- **G1**(Q1 だけ): conjecture が取れた行 **≥ 0.75(45 / 60)**(olm124 / olm125 と同じ較正・五腕 0.833 / 0.800 / 0.767 / 0.750 / 0.750)。✗ → Q1 を読まない(Q2 は読む)。**二回続けて境ちょうどなので落ちる確率も半分近い**(開示・olm125 §1)。
- **G2**(記述の側): status が hypothesis / question の行 ≥ 0.70(42 / 60)。✗ → 注記(olm125 は 37 / 60 で ✗)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 証明の欄の LN_a の率 r | **残る** 0.165 ≤ r < 0.285(olm125 の側)・**戻る** 0.048 < r < 0.168(olm124 の側・重なりは 戻る が先)・**上がる** r ≥ 0.285・**下回る** r ≤ 0.048 | 残る 0.45・戻る 0.40・上がる 0.08・下回る 0.07 |
| Q2 | 本文で式を数値で使った率 rc = REFL_CALC / 60(olm125 0.300・olm124 0.250) | **上がる** rc ≥ 0.40・**下がる** rc ≤ 0.10・ほか = **変わらない** | 変わらない 0.82・上がる 0.13・下がる 0.05 |
| Q3 | 記述: v6 の参考値(LN6_a・OUTER6_a・REJ6・b2_j07 の型)と olm125 の同じ値・MIDO3 / EQ・証明の欄の PERP3 / OUTER・計算した行 / しない行の証明の欄の LN(olm125 の 7 / 31 と 2 / 9 と並べる)・tool_named・指示の写し・取れなかった行の形(短い指示の続き / 上限)・pool 120 行の LN_a と REFL_CALC(参考・olm124 の帯で) | — | — |
| Q4 | 記述: 逐語 = 証明の欄の LN(全部)・REJ6 かつ証明の欄 LN6 の行(全部)・計算した行の計算の文と結果の文(最大 8 本)・式に触れたが計算しなかった行(最大 5 本)・指示の一行に触れた行(最大 5 本)・取れなかった行の頭(全部) | — | — |

- 読みの軸(開示): **Q1 残る** → 指示の文は二回で植える(宣言の文 0.318 より弱く式だけ 0.108 より強い)= 三種の文の並びが二回で立つ。**Q1 戻る** → olm125 の 0.225 は一回の揺れで、指示の文は式だけと同じ側(0.108〜0.16)= 「文が言う量」の読みは落ちる。**上がる / 下回る** → 60 行の揺れの外(二回の差 ≥ 0.12 は olm122 / olm124 の 0.000 と並べて記す)。**Q2 変わらない** → 計算の指示は二回とも +0.05 程度(0.25 → 0.30 前後)。
- 予想の根拠: Q1 = olm125 の 0.225 は Fisher(参考)で pool 120 行の 0.108 と p 0.11 の差(分けられない)なので、一回の揺れの可能性を 0.40 残す。だが増えた 4 本は計算しない短い行の「symmetric with respect to the line joining the centers」の型で、問いの文の Tool の段に文が増えたことが「線対称が答えだ」の手掛かりになる機構(b1_j09「Considering the provided reflection tool, it likely relates to the symmetry over the line O1O2」)は olm119(0.318)と同じ側なので 残る を 0.45。Q2 = 式だけの二回(0.200 / 0.250)と olm125(0.300)から、帯(0.10 < rc < 0.40)の中に落ちる確率が高い(0.82)。
- 帯の根拠: 証明の欄 40 行の一行 = 0.025・0.225 の SE ≈ 0.066。残る / 戻る の境 0.165〜0.168 は olm124 と olm125 の中点(0.167)に当たる = 二つの元のどちらに近いかの判定。

## §4. 読み方

- `--read` が `olm127/read.json` を書く(関門・Q1〜Q3・集計・行ごとの類と印・supp_ln / rej / rej6 / LN6・取れなかった行の T・pool 120 行)。判定は v3 の LN_a と REFL_CALC の値だけで、この札の 60 行だけで付ける。
- RESULT では §3 の Q4 の逐語を引き、olm125 / olm124 の同じ値を並べる。主 session の読み(残る / 戻る の機構)は値と並べ、違っても判定は変えない。v6 の値は参考として書く。pool 120 行は参考(判定に混ぜない)。

## §5. 主張しないこと

- 判定は新しい 60 行だけ。olm125 と同じ問いの文・違う seed。残る / 戻る は「olm124 と olm125 のどちらに近いか」で、三種の文の順の統計的な分離ではない(60 行ずつ)。
- 指示の効果を語の数(reflection が一度多い)と分けない(olm125 §5)。
- SUPP_LN / REJ / v6 は記述の補助。判定は凍結の v3。
- 正しさの率は測らない。一つの model・一つの温度・60 行。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・39 項目・帯の自己検査 9 / 9)→ `--smoke`(凍結の前・2 行・max_new 1536・読まない)→ 凍結 → `--gen`(約 3 時間の見込み・olm125 は 2.84 時間)→ `--read`。
- smoke(凍結の前・seed 20261203・2 行・max_new 1536・読まない・zebrashark 11-04 08:46:26〜08:51:28 JST・壁時計 302 s(model の読み込み込み・生成 298 s)・Traceback 0・`olm127/smoke.json`・`smoke_run.log`): 行 1 = T 814・status none / 行 2 = T 1,536(上限)・status none。本文は読んでいない(smoke の log は類・LN・REFL を印字しない)。runner の md5 = `53f6b9ff…`(selftest PASS 39 項目・帯の自己検査 9 / 9)。
- 出力 = `ConstructGap/exp/olm127/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-04/RESULT_olm127_moy2_use_to_check_rerun_20261104.md`。
