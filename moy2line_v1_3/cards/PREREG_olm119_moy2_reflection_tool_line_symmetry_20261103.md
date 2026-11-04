HEAD(R1) = 8ba1a5bf(凍結時の HEAD・fetch 済・origin より 13 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm119`・凍結 2026-11-03): moy-2 の「折り返しの式」— olm113 の M2A の問いの文(半径 3.6869 / 7.4607・考えを先に + 仮説か問い + 裏付け)に「O1O2 での折り返しの式」を一段(# Tool)足して OLMo-3 32B base に 60 行書かせ、証明の欄で O1O2 についての線対称を肯定して述べる率(v3 の LN_a・olm113 = 5 / 41 = 0.122)が下がるか、式を数値で使うかを見る

- 発注(逐語・先生 11-03): 「**a / b / c を順に**」= [RESULT olm118](RESULT_olm118_moy2_symmetry_kind_outer_marker_v3_20261103.md) §7 の候補 (a)「『確かめられる前提は直る』を測る = 線対称を数値で確かめる手(O1O2 での折り返しの式)を問いの文に与えた時に線対称の率が下がるか」の一枚目。
- G10 の欄: 比べる物 = 「折り返しの式を足した問いの文で OLMo が書いた 60 行の証明の欄(空でない物)で、O1O2 についての線対称を肯定して述べる(v3 の LN_a)行の割合と、olm113 の M2A の同じ割合(5 / 41 = 0.122・olm118 の read.json)の差」/「本文で折り返しの式を数値で使った(REFL_CALC)行の割合」/「数値で使った行の証明の欄の LN_a の数(記述)」 / 計器 = 読み込むだけの凍結の部品(hq の proof_of・status_of・olm117 の v2 = conjecture の類と SYMM・olm118 の v3 = SYM_PT・SYM_LN・OUTER・asserted・較正 54 / 54)+ この札の REFL_MENTION / REFL_CALC(折り返しの式の言及 / 数値の計算・較正 12 例)+ 問いの文の差分の検査(TOOL の段を外すと olm113 の M2A の md5 に戻る)/ 雛形 = いいえ
- runner = [olm119_…py](../../ConstructGap/exp/olm119_moy2_reflection_tool_line_symmetry_20261103.py)。読み込むだけの部品: [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(`426e2089…`)・[olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)(`ab678f30…`)・[olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(`136f72b9…`)・比べる元 `olm118/read.json`(`bffeb826…`・olm113 の v3 の集計)。走らせる所 = zebrashark(32B は一つずつ)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- 主 session は olm118 の RESULT で olm113 の線対称 5 本・点対称 0・外接線の印 10 本の証明の欄と、本文の折り返し(O3 についての点対称)の計算の文(b0_j15「The reflection of Th over O3 would be (2*3.9524 −7.6927, …」)を読んだ。olm113 の本文で O1O2 での折り返しを計算した行があるかは**数えていない**(v3 の REFL は無い)。
- 問いの文に足す段(TOOL・267 字・逐語):
  ```
  # Tool (available if you need it)
  Reflection of a point P across the line O1O2: P' = 2F − P, where F = O1 + t(O2 − O1) and t = ((P − O1)·(O2 − O1)) / |O2 − O1|². Two points are symmetric with respect to the line O1O2 exactly when each is the reflection of the other.
  ```
  置き場 = 「# Premises」の段の後・「State the SINGLE most important invariant …」の直前。**使えとは書かない**(「available if you need it」だけ)。prompt md5 `d4c07f24…`・TOOL を外すと `56182280…`(olm113 の M2A・guard)。
- smoke(凍結の前・2 行・読まない): 数は §6。
- REFL の較正 12 例は主 session が書いた文(olm113 / 117 の行からは引いていない)。負号は ASCII と U+2212 の両方を数に数える(olm116 の出力で U+2212 を見た)。

## §1. 計器(R5・R6)

- **問いの文** = olm113 の M2A + TOOL の段(上)。生成 = olm113 / 117 と同じ(温度 0.7・max_new 12288・3 batch × 20 行・seed 20261170〜72・既出の seed と重ねない)。
- **凍結の読み**(読み込むだけ): v2(conjecture の類 EQ / MIDO3 / OTHER / NONE・status・proof_of・SYMM)・v3(SYM_PT / SYM_LN / SYM_OTH / kind・PAR3 / PERP3 / PBIS3 / OUTER・asserted)を証明の欄と本文に。
- **この札の REFL**(本文に当てる):
  - **REFL_MENTION** = O1O2 での折り返し・鏡映への言及(`reflect / mirror … across / over / in / about / with respect to (the line) O1O2 / the line joining the centers`・`the tool`・式の形 `P' = 2F`・`F = O1 + t`・`using the (given) formula / tool`)。
  - **REFL_CALC** = 折り返しを**数値で**計算した(`P' / Tc' / Th' / reflection of Tc / F = / t =` の後 220 字以内に座標の対 `(x, y)`・`t = 数` の後に `F = / P' = / reflect`・`reflect … across O1O2 … (x, y)`)。
  - 較正 12 例(陽性 7・陰性 5・O3 についての折り返しの数値(c06)と中点の数値(c08)は陰性)。
- 率の分母: Q1 = 証明の欄が空でない行(olm113 は 41)・Q2 = 60 行。

## §2. 関門

- **G0**: olm118 の read.json の olm113 の証明の欄 n = 41(md5 一致)。
- **G1**: conjecture が取れた行 ≥ 0.80(48 / 60)。✗ → Q1・Q2 を読まない。
- **G2**(記述の側): status が hypothesis / question の行 ≥ 0.70。✗ → 注記。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 証明の欄の LN_a の率の差 Δ = 式あり − olm113(0.122) | **下がる** Δ ≤ −0.08・**上がる** Δ ≥ +0.08・**変わらない** \|Δ\| < 0.04・ほか = 間 | 変わらない 0.40・間 0.30・下がる 0.25・上がる 0.05 |
| Q2 | 本文で式を数値で使った率 REFL_CALC / 60 | **使う** ≥ 0.30・**使わない** ≤ 0.10・ほか = 間 | 使わない 0.40・間 0.35・使う 0.25 |
| Q3 | 記述: 数値で使った行の証明の欄の LN_a の数と、その行の conjecture の類・本文の LN_a | — | — |
| Q4 | 記述: PT_a・OUTER_a・類(EQ / MIDO3)の率・status・T・上限・REFL_MENTION・olm113 との並び・TOOL の段が答えの分布を変えたか | — | — |

- 読みの軸(開示): olm118 の L3「数値で確かめられる前提は図で直り、確かめない前提は記憶のまま残る」の検証。**式を使って(Q2 使う)線対称が下がる(Q1 下がる)** → 支持。**式を使わず(使わない)変わらない** → 式を与えるだけでは base は確かめない(記憶が先に立つ)= L3 は検証されず、道具の有無でなく「確かめる習慣」の問題。**式を使っても変わらない** → 計算しても結論を直さない(olm113 の b0_j15 型の「確かめて退ける」が線対称には働かない)= L3 の反証。
- 主 session の見込み: base は与えた式を見ても自発的には使わない方に寄る(JSON だけの文が効かなかった olm114 の k = 0・指示の段を写すだけの行が 6 / 60 あった olm117)。使うなら使った行では線対称が消えるだろう。

## §4. 読み方

- `--read` が `olm119/read.json` を書く(関門・Q1〜Q3・集計・行ごとの類と印・最初の当たりの前後)。判定は v3 と REFL の値だけで付ける。
- RESULT では、REFL_CALC の行の計算の文(全部・最大 10 本)・証明の欄の LN の文(全部)・式に触れたが計算しなかった行(最大 5 本)を逐語で引く。主 session の読み(L3)は値と並べ、違っても判定は変えない。

## §5. 主張しないこと

- TOOL の段は問いの文を 267 字長くし、答えの分布(EQ / MIDO3 の率)も変えうる。線対称の率の差を TOOL の中身だけに帰さない(同じ長さの中立の段の腕は置かない = 一つの腕・60 行)。
- REFL_CALC は語と数の印で、計算が正しいかは見ない(間違えて「対称」を確かめた行も数える・§4 で逐語)。
- 正しさの率は測らない。一つの model・一つの温度・60 行。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・REFL 12 / 12・v3 54 / 54・guard)→ `--smoke`(凍結の前・2 行・max_new 1536・読まない)→ 凍結 → `--gen`(約 2 時間の見込み・olm117 は 1.87 時間)→ `--read`。
- smoke(凍結の前・seed 20261194・2 行・max_new 1536・読まない・zebrashark 15:16〜15:18 JST・壁時計 125 s・Traceback 0・`olm119/smoke.json`・`smoke_run.log`): 行 1 = T 44・status none・証明の欄 0 字 / 行 2 = T 1,018・hypothesis・証明の欄 188 字。本文は読んでいない。smoke の log は類・LN・REFL を印字しない作りにした。
- 出力 = `ConstructGap/exp/olm119/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-03/RESULT_olm119_moy2_reflection_tool_line_symmetry_20261103.md`。
