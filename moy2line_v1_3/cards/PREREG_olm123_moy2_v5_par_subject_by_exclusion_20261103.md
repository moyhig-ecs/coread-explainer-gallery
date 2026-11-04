HEAD(R1) = 1ef817f4(凍結時の HEAD = olm122 の凍結の commit・fetch 済・origin より 21 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記(olm122)だけ = この file と runner を入れる commit の親)

# PREREG(札 `olm123`・凍結 2026-11-03): 述語 v5 — PAR の主語を除外で書く(f): v4(olm121)の PAR4 が主語を「接線」の語に限って本物の当たりを落とした(証明 1・本文 6)ので、「parallel to 中心線」の主語が **O3 から出る線でも半径でも作図の形でもなければ拾う**(除外で書く・先生の言葉)に書き直し、olm113 の M2A(60)・olm117(60)・prf5 の frontier(20)・olm116 の続き(80)に当て直す(+ olm119 の 60 行は参考)— v4 の落とし 7 本が戻り、正しい落とし 7 本が落ちたままで、olm118 / olm120 の判定が v3 と同じに戻るかを確かめる(読みだけ・model なし)

- 発注(逐語・先生 11-03 夜): 「**(d) (e) (f) へ順次進みます。**」= [RESULT olm119](RESULT_olm119_moy2_reflection_tool_line_symmetry_20261103.md) §6 の (f)「v5(PAR の主語を除外で書く・olm121 §6)」。(d) olm122 は本走中(18:46 発火・読みだけのこの札は並行)・(e) は (d) の RESULT の後。
- G10 の欄: 比べる物 = 「v4 の落とし 7 本(olm113 の証明の欄 b0_j16・本文 b0_j16 / b1_j12 / b2_j15・olm117 の本文 b1_j10 / b1_j11 / b2_j03)が v5 で当たりに戻り、正しい落とし 7 本(olm113 の本文 b0_j13 / b2_j07・olm117 の証明の欄 b1_j13・本文 b1_j06 / b1_j13 / b2_j05・olm116 の k1_1_j04)と prf5 の fable_r4(本文の PBIS・証明の否定の PAR)が落ちたままか(当たりの文の断片で)」/「olm118 の Q1〜Q3(線対称・点対称・外接線の印の olm117 − olm113 の差の帯)と olm120 の Q1〜Q2(k1 − olm113 の帯)の判定が v5 で v3 と同じか(v4 の判定も並べる)」/「v4 → v5 で PAR の当たりが変わった行(全部・逐語)・RETR / KEPT(本文)・olm119 の v5 の値(参考・記述)」 / 計器 = v3(olm118)の SYM_PT・SYM_LN・SYM_OTH・PERP3・asserted + v4(olm121)の PBIS4(→ PBIS5 の名)・RETR・KEPT(読み込むだけ)+ この札の PAR5(主語を除外で書く: O3 から出る線・半径・O3 からの垂線・作図の形「through X parallel to …」を除く・主語の窓はコンマ / 関係節 / 挿入句 / 並列で切る・目的語の窓 40 字)・較正 98 例(v4 の 74 を v5 の名で + 24)+ 陰性統制 = prf5 の証明 20 本 / 雛形 = いいえ
- runner = [olm123_…py](../../ConstructGap/exp/olm123_moy2_v5_par_subject_by_exclusion_20261103.py)(model なし・`--selftest` → `--read`)。読み込むだけの部品: [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(`426e2089…`)・[olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)(`ab678f30…`)・[olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(`136f72b9…`)・[olm121_…py](../../ConstructGap/exp/olm121_moy2_v4_instrument_fix_and_retraction_20261103.py)(`9c0b2b4e…`)。入力 = `olm113/gen.json`(`db0fde6e…`)・`olm117/gen.json`(`b5795850…`)・`results_prf5_20261102.jsonl`(`995650e5…`)・`olm116/gen.json`(`e66433f2…`)・`olm119/gen.json`(`781f0e70…`)・`olm118/read.json`(`bffeb826…`)・`olm120/read.json`(`bb3f10d9…`)・`olm121/read.json`(`84bd89e1…`)。

## §0. 起案の前に見た物(開示)

- v3 / v4 の値は全部既知(olm118・olm120・olm121 の RESULT)。olm119 の v3 の値と v4 の参考値(証明の欄 OUTER4 11・PAR4 2)も既知(RESULT olm119)。
- **較正の 14 例(m01〜m07・d01〜d07)は olm121 §3 の表の逐語**。だから Q1 は「盲検」でなく、**本文の中(窓の切り方・コンマ・並列)でも較正の文と同じに読めるかの回帰の検査**。Q3 の「v4 → v5 で変わった行」(較正に無い行)が未知の部分。
- v5 の窓の規則は主 session が較正の 24 例で作った(selftest で 2 例が落ちて直した: 並列「O1Th ∥ O2Tc and the segment TcTh is …」= 最後の and の後を取る / 挿入句「the line O3M, where M is …, is parallel」= コンマの後が空ならコンマの前を取る)。実値は印字していない。
- `--selftest` は guard と較正だけ(PASS・98 / 98)。

## §1. 計器(R5・R6)

- **PAR5**(主語を除外で書く):
  - (A) 主語 … (動詞)? parallel to 中心線(O1O2・line of centers …): 主語の窓(節の頭か 80 字前から当たりまで・最後のコンマの後・コンマの後が which / that / and … で始まるか空ならコンマの前・残りの最後の and / but / hence … の後に語があればそこから)に**除外の形**がなければ拾う。動詞なしで窓が「through / from / at X」で終わるか「Draw / a line」の形なら作図の線 = 拾わない。
  - (B) 中心線 (動詞)? parallel to 目的語: 目的語の窓(40 字・句読点か and / which … まで)に除外の形がなければ拾う。
  - (C) 「X and 中心線 are parallel」「中心線 and Y are parallel」: X / Y に除外の形がなければ拾う。
  - **除外の形** = O3 から出る線(O3Tc・O3Th・O3M・O3O3・TcO3・through / from / at O3・O3 to Tc)・半径(O1Tc・O1Th・O2Tc・O2Th・radius / radii)・O3 からの垂線。
- PT / LN / OTH / kind / PERP3 / asserted = v3 のまま。PBIS5 = v4 の PBIS4 のまま。RETR / KEPT = v4 のまま(窓 260 字)。OUTER5 = PAR5 ∨ PERP3 ∨ PBIS5。
- **較正** = v4 の 74 例(名を v5 に写して全部通る)+ 24 例(v4 の落とし 7 = 陽性・正しい落とし 7 = 陰性・窓の形 10 = 並列 / 関係節 / 作図 / 半径の目的語 / 向き / 否定 / 方向ベクトル)。陰性統制 = prf5 の証明 20 本(OUTER5_a ≤ 1・PT_a + LN_a ≤ 1)。
- 当てる文: olm113 / olm117 / olm119 = 証明の欄と本文、prf5 = 証明の欄と JSON の全文、olm116 = 続き(`cont`)だけ。

## §2. 関門

- **G0**: 入力 8 本・部品 4 本の md5 一致・較正 98 / 98・v3 54 / 54・v4 74 / 74。
- **G1**(陰性統制・証明の欄): prf5 で OUTER5_a ≤ 1・PT_a + LN_a ≤ 1。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | v4 の落とし 7 本が当たりに戻り(その文の断片を含む PAR5 の当たりがある)、正しい落とし 7 本は落ちたまま(その断片を含む当たりがない)、prf5 の fable_r4 は本文の PBIS なし・証明の PAR は否定のまま | **直った** = 16 項目とも期待どおり・ほか = **直らない** | 直った 0.80・直らない 0.20 |
| Q2 | olm118 の Q1〜Q3 と olm120 の Q1〜Q2 の判定が v5 で v3 と同じ | **v3 と同じ** = 5 つとも同じ・ほか = **違う** | v3 と同じ 0.80・違う 0.20 |
| Q3 | 記述: v4 → v5 で PAR の当たりが変わった行(全部・逐語・v4 の落とし 7 本以外に何が変わるか)・RETR / KEPT・PAR5 の数(証明の欄・本文・腕ごと)・olm119 の v5 の値 | — | — |

- 読みの軸(開示): Q1 と Q2 が通れば、v5 は v4 の落としを直して v3 の判定に戻る = 外接線の印の計器は v5 で据える(olm122 以降の読みの参考に)。Q1 が直らないなら、窓の規則が本文の中で較正の文と違う読みをした所を逐語で書く。Q2 が違うなら、違った Q の値と帯の境を書き、olm118 / olm120 の RESULT には追記しない(v4 と同じ扱い・本文は直さない)。
- 予想の根拠: Q1 は較正の逐語を本文の中で読み直すだけだが、本文では当たりの前 80 字に別の半径の語が入りうる(窓の規則が節の頭まで戻る形)ので 0.20 を外れに置く。Q2 は olm118 の Q3 が v4 で境を 0.003 越えただけで、b0_j16 の証明が戻れば +0.039 に戻る見込み(olm117 の証明 b1_j13 の O3Tc が落ちると Δ はさらに小さい)。

## §4. 読み方

- `--read` が `olm123/read.json` を書く(関門・Q1〜Q3・腕ごとの集計・行ごとの印と PAR5 の当たりの全部・v4 → v5 で変わった行)。判定は v5 の値だけで付ける。
- RESULT では、v4 → v5 で当たりが変わった行を全部逐語で引き(正しい拾い / 正しい落とし / v5 の落とし / v5 の拾いすぎ の札を付ける)、olm119 の v5 の値を v3 / v4 の参考値と並べる。

## §5. 主張しないこと

- v5 も語の印。窓の規則(80 字・コンマ・and)は、コンマなしで同じ節に半径の語がある時に真の主語を除外しうる(「Because O1Tc ⊥ l1 … the line TcTh is parallel to O1O2」= 落とす)。目的語の窓 40 字も粗い。
- RETR / KEPT の粗さは v4 のまま(退けた相手がその当たりとは限らない)。
- v5 で olm118 / olm120 / olm121 の RESULT の本文は書き換えない。olm119 の v5 の値は参考で、olm119 の判定(v3)は変えない。
- 新しい model の出力はない。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・98 / 98)→ G10 → 凍結 → `--read`(数秒)。model なし・smoke なし。olm122 の本走と並行(読みだけ)。
- 出力 = `ConstructGap/exp/olm123/read.json`・`read_run.log`。RESULT = `conversations/2026-11-03/RESULT_olm123_moy2_v5_par_subject_by_exclusion_20261103.md`。
