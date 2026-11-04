HEAD(R1) = 86af77f0(凍結時の HEAD・fetch 済・origin より 14 commit 先・遅れ 0・tracked の変更は G10 の台帳の追記だけ = この file と runner を入れる commit の親)

# PREREG(札 `olm120`・凍結 2026-11-03): 述語 v3 を olm116 の続きに当てる — frontier の証明を段で与えた後に OLMo-3 32B base が書いた続き(k1 = 設定まで与えた 40 本・k2 = 足 = 中点の段まで 40 本)で、対称の種類(O3 の点対称 / O1O2 の線対称)と外接線の記憶の印(接線 ∥ O1O2・O1O2 ⊥ 接線・O1O2 が垂直二等分線)が、足場なし(olm113 の M2A の証明の欄)より抑えられるかを見る(読みだけ・model なし)

- 発注(逐語・先生 11-03): 「**a / b / c を順に**」= [RESULT olm118](RESULT_olm118_moy2_symmetry_kind_outer_marker_v3_20261103.md) §7 の (b)「olm116 の続き(frontier の段 + OLMo)に v3 を当て、足場が外接線の印と線対称を抑えるか」の二枚目((a) = olm119 は凍結 86af77f0・本走中)。
- G10 の欄: 比べる物 = 「olm116 の k1(半径 ⊥ 接線と足 / 平行の設定まで与えた)の続き 40 本で、O1O2 についての線対称を肯定して述べる(v3 の LN_a)行の割合と、olm113 の M2A の証明の欄の同じ割合(5 / 41 = 0.122)の差」/「同じ 40 本で外接線の記憶の印(v3 の OUTER_a)の割合と olm113 の同じ割合(10 / 41 = 0.244)の差」/「O3 についての点対称(PT_a)の数(k1・k2・記述)」 / 計器 = 読み込むだけの凍結の述語 v3(olm118・SYM_PT・SYM_LN・SYM_OTH・kind・PAR3・PERP3・PBIS3・OUTER・asserted・較正 54 / 54)を続きの文(`cont`)だけに当てる + 比べる元 = olm118 の read.json の olm113 / olm117 の集計 / 雛形 = いいえ
- runner = [olm120_…py](../../ConstructGap/exp/olm120_moy2_v3_on_olm116_continuations_20261103.py)(model なし・`--selftest` → `--read`)。読み込むだけの部品 [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(`426e2089…`)・[olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(`136f72b9…`)。入力 = `olm116/gen.json`(`e66433f2…`・k1_0 / k1_1 / k2_0 / k2_1 各 20 本 = Opus 10 + Fable 10)・`olm118/read.json`(`bffeb826…`)。

## §0. 起案の前に見た物(開示)

- 主 session は [RESULT olm116](RESULT_olm116_moy2_frontier_proof_prefix_ladder_20261103.md) で k1 の続き 40 本の v2 の前提の語を見た: **SYMM 5(全部 Opus の文)・PAR 2・HOMO 2・COLL 4**、k2 は小さい。続き 25 本を逐語で読んだ。**対称の種類は数えていない**(v3 は olm116 の後に作った)。
- v3 の olm113 / olm117 の値(olm118): 証明の欄 LN_a 0.122 / 0.152・PT_a 0 / 0.087・OUTER_a 0.244 / 0.283。
- 続きの前にある frontier の段(prefix)は prf5 の証明の一部で、prf5 の証明 20 本は olm118 で v3 の当たり 0(証明の欄)。prefix は当てない(続きだけ)。
- `--selftest` は guard と較正だけ(PASS)。予想は上を見た上で付けた。

## §1. 計器(R5・R6)

- 当てる文 = olm116 の各行の `cont`(続き = OLMo が書いた部分だけ・JSON の proof の欄を閉じるまで)。v3 の述語をそのまま(正規化 norm2・asserted を含む)。
- 分母 = 続きが空でない行(k1 40・k2 38 = 閉じただけの行 2 を除く)。一行 = 0.025。
- 比べる元 = olm113 の M2A の証明の欄 41 本(足場なし・同じ図)。olm117 は参考。
- 統制: 陽性 / 陰性の較正 54 例(v3)。frontier の prefix は当てないが、prf5 の証明 20 本で 0(olm118 G1)。

## §2. 関門

- **G0**: md5 一致・v3 の較正 54 / 54・olm113 の証明の欄 n = 41。
- **G1**: k1 の続きが空でない行 ≥ 32 / 40。✗ → 読まない。

## §3. 問いと予想(確率は 0〜1・Δ = k1 の続き − olm113 の証明の欄)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 線対称 LN_a の率の差 Δ(olm113 0.122) | **下がる** Δ ≤ −0.08(≤ 1 / 40)・**上がる** Δ ≥ +0.08・**変わらない** \|Δ\| < 0.04(4〜6 / 40)・ほか = 間(2〜3 か 7 / 40) | 間 0.35・下がる 0.30・変わらない 0.30・上がる 0.05 |
| Q2 | 外接線の印 OUTER_a の率の差 Δ(olm113 0.244) | **下がる** Δ ≤ −0.12(≤ 4 / 40)・**上がる** Δ ≥ +0.12・**変わらない** \|Δ\| < 0.06(8〜12 / 40)・ほか = 間 | 下がる 0.50・間 0.30・変わらない 0.15・上がる 0.05 |
| Q3 | 記述: 点対称 PT_a の数(k1・k2)・種類の分布・family(Opus / Fable の文)ごと・k2・v2 の W_SYMM / W_PAR との照合 | — | — |

- 読みの軸(開示): 足場(射影の道の段)が与えられると、続きは段の語で埋まり(olm116)、記憶の図の前提(線対称・外接線)は入りにくいはず。**Q2 下がる** → 足場は外接線の記憶を抑える。**Q1 が 変わらない** → 線対称は足場があっても入る(olm116 の SYMM 5 が全部線対称なら 0.125 = olm113 と同じ)。family 差(olm116 で Opus の文に SYMM 5・Fable 0)は記述。
- 主 session の見込み: SYMM 5 のうち種類を名指すのは半分ほど → LN 2〜3 / 40 = 間。OUTER は PAR 2 + PERP3 で 2〜4 → 下がる。

## §4. 読み方

- `--read` が `olm120/read.json` を書く(関門・Q1〜Q3・k1 / k2 / family ごとの集計・行ごとの印と最初の当たり)。判定は v3 の値だけで付ける。
- RESULT では、k1 の LN / PT / OUTER の当たりの文(全部・最大 8 本ずつ)と k2 の当たり(全部)を逐語で引き、olm116 の RESULT の逐語(退化の主張 M = O3 など)と並べる。L3 は値と並べ、判定は変えない。

## §5. 主張しないこと

- 続きは frontier の段の後に来る文で、olm113 の証明の欄(OLMo が一から書いた)と文脈が違う。率の差を「足場」だけに帰さない(長さ・型の差も含む)。
- v3 の限界(語の印・asserted の粗さ・PBIS3 の取りこぼし)は olm118 §6 のまま。
- 一つの model・一つの温度・40 + 40 本。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS)→ G10 → 凍結 → `--read`(数秒)。model なし・smoke なし。olm119 の本走と重ならない(読みだけ)。
- 出力 = `ConstructGap/exp/olm120/read.json`・`read_run.log`。RESULT = `conversations/2026-11-03/RESULT_olm120_moy2_v3_on_olm116_continuations_20261103.md`。
