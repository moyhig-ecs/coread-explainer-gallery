HEAD(R1) = e6f3e3a7(凍結時の HEAD・fetch + pull 済 = 自宅の 2 commit(YouTube の裏取り)を merge・origin より 20 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm122`・凍結 2026-11-03): moy-2 の「折り返しの式」の第二文を外す腕(d)— olm119 の TOOL の段から説明の文「Two points are symmetric with respect to the line O1O2 exactly when each is the reflection of the other.」を外し、式(第一文)だけを olm113 の M2A の問いの文に足して OLMo-3 32B base に 60 行書かせ、証明の欄で O1O2 についての線対称を肯定して述べる率(v3 の LN_a)が olm113(5 / 41 = 0.122)に戻るか、olm119(14 / 44 = 0.318)の水準に残るかを見る(植える効果の分離)

- 発注(逐語・先生 11-03 夜): 「**(d) (e) (f) へ順次進みます。**」= [RESULT olm119](RESULT_olm119_moy2_reflection_tool_line_symmetry_20261103.md) §6 の (d)「第二文を外す腕」の一枚目。(e)「使って確かめよ」の腕は (d) の RESULT の後に凍結(32B は一つずつ)、(f) v5 は読みだけ。
- G10 の欄: 比べる物 = 「式だけ(第二文なし)の問いの文で OLMo が書いた 60 行の証明の欄(空でない物)で、O1O2 についての線対称を肯定して述べる(v3 の LN_a)行の割合と、olm113(5 / 41 = 0.122・olm118 の read.json)および olm119(14 / 44 = 0.318・olm119 の read.json)の同じ割合との差」/「本文で折り返しの式を数値で使った(REFL_CALC)行の割合(olm119 は 13 / 60 = 0.217)」/ 計器 = 読み込むだけの凍結の部品(hq の proof_of・status_of・olm117 の v2 = conjecture の類と SYMM・olm118 の v3 = SYM_PT・SYM_LN・OUTER・asserted・較正 54 / 54・olm119 の REFL_MENTION / REFL_CALC と score_row・較正 12 / 12・olm121 の v4 = RETR / KEPT は本文の記述だけ・較正 74 / 74)+ 問いの文の差分の検査(TOOL_D を外すと olm113 の M2A の md5 に戻る・TOOL_D + 第二文 = olm119 の TOOL の逐語)/ 雛形 = いいえ
- runner = [olm122_…py](../../ConstructGap/exp/olm122_moy2_reflection_formula_only_20261103.py)。読み込むだけの部品: [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(`426e2089…`)・[olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)(`ab678f30…`)・[olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(`136f72b9…`)・[olm119_…py](../../ConstructGap/exp/olm119_moy2_reflection_tool_line_symmetry_20261103.py)(`d8d4062f…`)・[olm121_…py](../../ConstructGap/exp/olm121_moy2_v4_instrument_fix_and_retraction_20261103.py)(`9c0b2b4e…`)・比べる元 `olm118/read.json`(`bffeb826…`・olm113 の v3 の集計)・`olm119/read.json`(`f2138597…`・式ありの集計)。走らせる所 = zebrashark(32B は一つずつ)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- olm119 の値は全部既知([RESULT](RESULT_olm119_moy2_reflection_tool_line_symmetry_20261103.md))。主 session は olm119 の 60 行のうち、計算した 13 本の計算の文、証明の欄の線対称 14 本、式に触れたが計算しない 18 本の一部(5 本 + 一覧)を読んだ。olm113 の線対称 5 本の言い回しも読んだ(4 本が「symmetric with respect to O1O2」)。
- 問いの文に足す段(TOOL_D・逐語・olm119 の TOOL の第一文まで):
  ```
  # Tool (available if you need it)
  Reflection of a point P across the line O1O2: P' = 2F − P, where F = O1 + t(O2 − O1) and t = ((P − O1)·(O2 − O1)) / |O2 − O1|².
  ```
  外す第二文(逐語): 「 Two points are symmetric with respect to the line O1O2 exactly when each is the reflection of the other.」(olm119 の TOOL = TOOL_D + 第二文であることを guard)。置き場 = olm119 と同じ(「# Premises」の後・「State the SINGLE …」の直前)。**使えとは書かない**(olm119 と同じ)。TOOL_D を外すと olm113 の M2A の md5 `56182280…` に戻る(guard)。問いの文の md5 = `2c4a01a4…`(olm119 は `d4c07f24…`)。
- 読みは olm119 の `score_row`(v2 + v3 + REFL)を読み込むだけ。この札の述語は `tool_named`(道具・式を名指す語の有無・記述)だけ。v4(olm121)の RETR / KEPT は本文の記述に使い、判定には使わない。
- smoke(凍結の前・2 行・読まない): 数は §6。

## §1. 計器(R5・R6)

- **問いの文** = olm113 の M2A + TOOL_D(上)。生成 = olm119 と同じ(温度 0.7・max_new 12288・3 batch × 20 行・seed 20261180〜82・既出の seed と重ねない)。
- **凍結の読み**(読み込むだけ): v2(conjecture の類 EQ / MIDO3 / OTHER / NONE・status・proof_of・SYMM)・v3(SYM_PT / SYM_LN / SYM_OTH / kind・PAR3 / PERP3 / PBIS3 / OUTER・asserted)を証明の欄と本文に・REFL_MENTION / REFL_CALC を本文に(olm119 §1 の定義のまま)。v4 の LN_r / LN_k・PERP3_r・OUTER4_r などを本文に(記述)。
- **tool_named**(記述) = `the tool / tool provided / given formula / formula given / formula provided / reflection formula / available if you need` の有無。
- 率の分母: Q1 = 証明の欄が空でない行(olm113 41・olm119 44)・Q2 = 60 行。

## §2. 関門

- **G0**: 部品 5 本・比べる元 2 本の md5 一致・較正 12 / 12・54 / 54・74 / 74・olm113 の証明の欄 n = 41・olm119 の証明の欄 n = 44。
- **G1**: conjecture が取れた行 ≥ 0.80(48 / 60)。✗ → Q1・Q2 を読まない。
- **G2**(記述の側): status が hypothesis / question の行 ≥ 0.70。✗ → 注記。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 証明の欄の LN_a の率 r・Δ113 = r − 0.122・Δ119 = r − 0.318 | **戻る** \|Δ113\| < 0.06・**残る** \|Δ119\| < 0.06・**上がる** Δ119 ≥ +0.06・**下回る** Δ113 ≤ −0.06・ほか = **間**(0.182 ≤ r ≤ 0.258) | 戻る 0.40・間 0.30・残る 0.20・下回る 0.05・上がる 0.05 |
| Q2 | 本文で式を数値で使った率 REFL_CALC / 60 | **使う** ≥ 0.30・**使わない** ≤ 0.10・ほか = 間 | 使わない 0.45・間 0.40・使う 0.15 |
| Q3 | 記述: MIDO3 / EQ の率(olm119 0.60 / 0.17・olm113 0.34 / 0.32)・証明の欄の PERP3(olm119 10 / 44・olm113 4 / 41)と OUTER・計算した / しない行の本文の LN と退け(v4)・証明の欄の LN・類・tool_named・T・上限 | — | — |
| Q4 | 記述: 逐語 = 証明の欄の LN の文(全部)・計算した行の計算の文(最大 10 本)・式に触れたが計算しなかった行(最大 5 本) | — | — |

- 読みの軸(開示): **戻る** → 植えたのは第二文(宣言の文)で、式そのものは前提にならない = olm119 §4 の 1「宣言の文は前提として効く」を支持。**残る** → 式(「Reflection … across the line O1O2」の語)だけで線対称の記憶が呼ばれる = 植えるのは「道具の存在」で、文の形ではない。**間** → 両方が効く。Q2 は、第二文の「exactly when each is the reflection of the other」が「Th に落ちるか」という確かめる問いを与えていたなら、第二文なしでは計算は減る(使わない)。
- 主 session の見込み: 第二文が植えた(olm119 の線対称の文の多くが「symmetric … exactly when」の形の言い換え)と見て 戻る を最大に置くが、olm119 の b2_j13「Given the tool for reflection across the line O1O2 … it is natural to suspect that the points Tc and Th are symmetric」は道具の存在だけから対称を疑っているので、式だけでも植わる可能性は残す(間 + 残る = 0.50)。

## §4. 読み方

- `--read` が `olm122/read.json` を書く(関門・Q1〜Q3・集計・行ごとの類と印と最初の当たりの前後)。判定は v3 と REFL の値だけで付ける。
- RESULT では §3 の Q4 の逐語を引く。主 session の読み(植える効果と確かめる効果)は値と並べ、違っても判定は変えない。

## §5. 主張しないこと

- TOOL_D は問いの文を 162 字長くし(olm119 の TOOL は 267 字・第二文 106 字)、答えの分布も変えうる。差を第二文の有無だけに帰さない(同じ seed で走らせ直す腕はない = olm113 と olm119 の差と同じ粗さ・一行 = 0.023)。
- REFL_CALC は語と数の印で計算の正しさは見ない。v4 の RETR / KEPT は参考。
- 正しさの率は測らない。一つの model・一つの温度・60 行。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・REFL 12 / 12・v3 54 / 54・v4 74 / 74・guard)→ `--smoke`(凍結の前・2 行・max_new 1536・読まない)→ 凍結 → `--gen`(約 2.8 時間の見込み・olm119 は 2.76 時間)→ `--read`。
- smoke(凍結の前・seed 20261193・2 行・max_new 1536・読まない・zebrashark 18:42〜18:45 JST・壁時計 183 s・Traceback 0・`olm122/smoke.json`・`smoke_run.log`): 行 1 = T 1,536(上限)・status none・証明の欄 0 字 / 行 2 = T 98・none・証明の欄 0 字。本文は読んでいない(smoke の log は類・LN・REFL を印字しない)。
- 出力 = `ConstructGap/exp/olm122/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-03/RESULT_olm122_moy2_reflection_formula_only_20261103.md`。
