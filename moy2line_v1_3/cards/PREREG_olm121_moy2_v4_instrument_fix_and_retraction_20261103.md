HEAD(R1) = efd421a4(凍結時の HEAD・fetch 済・origin より 16 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm121`・凍結 2026-11-03): 述語 v4 — v3(olm118)の取りこぼし 3 種(PBIS3 の主語「the perpendicular from O3 to l1 is …」・PBIS3 の `Tc|Th` に `\b` なし = 「the」の th・PAR3 の主語なし「the line through O3 parallel to O1O2」)を直し、「口にして退けた」(RETR)を足して、olm113 の M2A(60)・olm117(60)・prf5 の frontier(20)・olm116 の続き(k1 40・k2 40)に当て直す — 取りこぼしが消えること、olm118 / olm120 の判定が変わらないことを確かめ、本文の「退けた / 残した」を計器の値にする(読みだけ・model なし)

- 発注(逐語・先生 11-03): 「**a / b / c を順に**」= [RESULT olm118](RESULT_olm118_moy2_symmetry_kind_outer_marker_v3_20261103.md) §7 の (c)「PBIS3 の主語を直す v4」の三枚目((a) olm119 = 本走中・(b) olm120 = [RESULT](RESULT_olm120_moy2_v3_on_olm116_continuations_20261103.md) 済)。olm120 で見つけた取りこぼし 2 種(`\b`・PAR3 の主語)と、olm118 §5 の L3 の粗い「退けた」の数を計器に入れる分を足した。
- G10 の欄: 比べる物 = 「v3 で見つけた取りこぼし 3 本(prf5 の fable_r4 の本文の PBIS・olm116 の k1_1_j04 の PAR・k1_1_j08 の PBIS)が v4 で当たりでなくなり、本物の当たり 3 本(olm116 の k1_0_j03 の PAR ∧ PERP・k1_0_j13 の PBIS・olm117 の b0_j04 の PBIS)が残るか」/「olm118 の Q1〜Q3(線対称・点対称・外接線の印の olm117 − olm113 の差の帯)と olm120 の Q1〜Q2(k1 − olm113 の帯)の判定が v4 でも同じか」/「本文で外接線の印・点対称・線対称を口にして退けた(RETR)/ 残した(KEPT)行の数(olm113・olm117・記述)」 / 計器 = v3 の述語(olm118・SYM_PT・SYM_LN・SYM_OTH・PERP3・asserted・読み込むだけ)+ この札の PAR4(主語と目的語 = 接線と中心線)・PBIS4(主語に `\b`・垂線の主語を除く)・OUTER4・RETR(当たりの後 260 字の退ける句)・KEPT(asserted ∧ ¬RETR)・較正 74 例(v3 の 54 + 20)+ 陰性統制 = prf5 の証明 20 本 / 雛形 = いいえ
- runner = [olm121_…py](../../ConstructGap/exp/olm121_moy2_v4_instrument_fix_and_retraction_20261103.py)(model なし・`--selftest` → `--read`)。読み込むだけの部品: [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(`426e2089…`)・[olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)(`ab678f30…`)・[olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(`136f72b9…`)。入力 = `olm113/gen.json`(`db0fde6e…`)・`olm117/gen.json`(`b5795850…`)・`results_prf5_20261102.jsonl`(`995650e5…`)・`olm116/gen.json`(`e66433f2…`)・`olm118/read.json`(`bffeb826…`)・`olm120/read.json`(`bb3f10d9…`)。

## §0. 起案の前に見た物(開示)

- v3 の値は全部既知(olm118・olm120 の RESULT)。取りこぼし 3 本の文と本物の当たり 3 本の文も読んだ(較正 f01〜f07 はそれらの逐語)。
- RETR の粗い数(olm118 §5・計器の外の正規表現): olm113 の本文 PAR3 23 本中 6 退け・PERP3 22 本中 8・PT 7 本中 3・LN 11 本中 0 / olm117 PAR3 20 本中 8・PERP3 24 本中 7・PT 11 本中 1・LN 11 本中 1。v4 の RETR は語の集合を少し広げた(`but wait`・`that's (more) for external / outer`)ので値は動きうる。
- v3 の olm117 の PAR3 の当たり 8 本(証明の欄)のうち主語が接線でない物があるかは**読んでいない**(olm118 §4 で 6 本は引いた = 全部 接線か TcTh が主語)。olm113 の 7 本も 6 本を引いた(同じ)。
- `--selftest` は guard と較正だけ(PASS・74 / 74)。

## §1. 計器(R5・R6)

- **PAR4**: 「接線(l1・(inner common) tangent (line)・TcTh / ThTc / Th-Tc・points of tangency / tangent points を結ぶ線)∥ 中心線(O1O2・line connecting / joining / through / of the centers・line of centers)」を、主語 → 目的語と目的語 → 主語の両方の向きと「X and Y are parallel」で。動詞に `might be / may be / could be / isn't` を許す。**主語が接線でない「parallel to O1O2」(作図の線・O3M)は拾わない**。
- **PBIS4**: v3 の 4 形のうち (ii) の主語 `Tc|Th|tangent points|contact points|points of tangency` に `\b`、(iv)「tangent / l1 is the perpendicular bisector」は直前 40 字が「perpendicular / line / segment / foot / projection + from / through / at / to …」(主語が垂線・作図の線)なら除く。
- **OUTER4** = PAR4 ∨ PERP3(v3 のまま)∨ PBIS4。SYM_PT / SYM_LN / SYM_OTH / kind / asserted は v3 のまま(読み込むだけ)。
- **RETR**(退けた)= 当たりの後 260 字に `wait, no / but wait / no, actually / that's not / that's (more) for external / outer / not it / isn't / is not / are not / not the case / doesn't hold / not necessarily / not true / false / hmm, no / no. / contradict / so no / not parallel / not perpendicular / not symmetric / not collinear / doesn't work / match / hold`。**KEPT** = asserted ∧ ¬RETR。行の値 = その印の当たりのどれかが RETR / KEPT。
- **較正** = v3 の 54 例(名を v4 に写して全部通る)+ 20 例(取りこぼしの形 3・本物の当たり 4・主語の違い 2・向き 2・RETR 8・否定 1)。陰性統制 = prf5 の証明 20 本(OUTER4_a ≤ 1・PT_a + LN_a ≤ 1)。
- 当てる文: olm113 / olm117 = 証明の欄と本文、prf5 = 証明の欄と JSON の全文、olm116 = 続き(`cont`)だけ。

## §2. 関門

- **G0**: 入力 6 本・部品 3 本の md5 一致・較正 74 / 74。
- **G1**(陰性統制・証明の欄): prf5 で OUTER4_a ≤ 1・PT_a + LN_a ≤ 1。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 取りこぼし 3 本が消え、本物の当たり 3 本が残る | **直った** = 6 本とも期待どおり・ほか = **直らない** | 直った 0.85・直らない 0.15 |
| Q2 | olm118 の Q1〜Q3 と olm120 の Q1〜Q2 の判定(同じ帯の規則)が v4 でも同じ | **変わらない** = 5 つとも同じ・ほか = **変わる** | 変わらない 0.85・変わる 0.15 |
| Q3 | 記述: 本文の RETR / KEPT の数(olm113・olm117・印ごと)・v4 の率(証明の欄・本文)・olm116 の k1 / k2 / family・prf5 | — | — |

- 読みの軸(開示): Q1 と Q2 が通れば、olm118 / olm120 の値は v4 で読み直しても同じ帯で、取りこぼしは判定に効いていなかったと言える。Q2 が変わるなら、変わった Q の値と帯の境を RESULT に書き、olm118 / olm120 の RESULT に追記で注記する(本文は直さない)。RETR は olm118 §5 の L3(点対称は退けられ線対称は退けられない)を計器の値にする。
- 予想の根拠: v3 の当たりの文は olm118 / olm120 で大半を読んでおり、取りこぼしの形は 3 本だけだった。olm118 の Q3(外接線の印・Δ +0.039・境まで 0.021)は一本の違いで帯が動きうる(一行 0.022〜0.024)ので、変わる 0.15 はそこに置く。

## §4. 読み方

- `--read` が `olm121/read.json` を書く(関門・Q1〜Q3・腕ごとの集計・行ごとの印と最初の当たり)。判定は v4 の値だけで付ける。
- RESULT では、v3 と v4 で当たりが変わった行を全部逐語で引き、RETR の当たり(olm113・olm117 の本文)を印ごとに最大 4 本引く。L3 は値と並べ、判定は変えない。

## §5. 主張しないこと

- v4 も語の印。RETR は当たりの後の 260 字の句で、退けた相手がその当たりとは限らない(別の案を退けた句を拾う)。KEPT も同じ粗さ。
- v4 で olm118 / olm120 の RESULT の本文は書き換えない(判定が変わった時だけ追記で注記)。
- 新しい model の出力はない。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・74 / 74)→ G10 → 凍結 → `--read`(数秒)。model なし・smoke なし。olm119 の本走と並行(読みだけ)。
- 出力 = `ConstructGap/exp/olm121/read.json`・`read_run.log`。RESULT = `conversations/2026-11-03/RESULT_olm121_moy2_v4_instrument_fix_and_retraction_20261103.md`。
