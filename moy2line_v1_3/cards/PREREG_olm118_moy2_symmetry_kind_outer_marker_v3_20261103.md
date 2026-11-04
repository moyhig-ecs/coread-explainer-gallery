HEAD(R1) = 46f8fca8(凍結時の HEAD・origin の 5 commit を merge 済み・origin より 11 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm118`・凍結 2026-11-03): moy-2 の述語 v3 — 「対称」の種類(O3 についての点対称 / O1O2 についての線対称 / 名なし)と「外接線の記憶」の印(接線 ∥ O1O2・O1O2 ⊥ 接線・O1O2 が垂直二等分線)を、olm113 の M2A(半径 3.6869 / 7.4607)と olm117(半径 5.5738 ×2)の 120 行の証明の欄と本文に当て直す(読みだけ・model なし・陰性統制 = prf5 の frontier の moy-2 20 本)

- 発注(逐語・先生 11-03): 「**v3へ進みます**」= [RESULT olm117](RESULT_olm117_moy2_equal_radii_control_20261103.md) §7 の候補「対称の種類(点対称 / 線対称)と外接線の記憶の印(`∥ O1O2`)を v3 の述語にして olm113・olm117 の両方に当て直す」への裁可。
- G10 の欄: 比べる物 = 「olm113 の M2A と olm117 の証明の欄(空でない物)で、O1O2 についての線対称を肯定して述べる(LN_a)行の割合の差」/「同じく O3 についての点対称(PT_a)の割合の差」/「同じく外接線の記憶の印(OUTER_a = 接線 ∥ O1O2・O1O2 ⊥ 接線・O1O2 が垂直二等分線)の割合の差」 / 計器 = この札の v3 の述語(SYM_PT・SYM_LN・SYM_OTH・kind・PAR3・PERP3・PBIS3・OUTER・asserted = 否定と反実仮想の語の除外・較正 54 例)+ 読み込むだけの凍結の部品(hq の proof_of・status_of・olm117 の v2 の norm2・PAR・SYMM・conjecture の類)+ 陰性統制 = prf5 の moy-2 の証明 20 本 / 雛形 = いいえ
- runner = [olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(model なし・`--selftest` → `--read`)。凍結の部品 [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(md5 `426e2089…`)と [olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)(`ab678f30…`)は読み込むだけで触らない。入力は md5 で固定: `olm113/gen.json`(`db0fde6e…`・M2A 60 行)・`olm117/gen.json`(`b5795850…`・60 行)・`results_prf5_20261102.jsonl`(`995650e5…`・moy-2 M2B 20 本)。API なし・model なし。

## §0. 起案の前に見た物(開示)

- 主 session は RESULT olm117 の執筆で、**olm117 の MIDO3 の証明の欄 33 本**に計器の外の粗い正規表現を当て、「対称」16 本のうち O3 についての点対称 3 + 両方 2・O1O2 についての線対称 3 + 両方 2・種類なし 8、「l1 ∥ O1O2」5・「O1O2 ⊥ l1」1・「O1O2 が垂直二等分線」1 を数えた(RESULT §3)。olm117 の証明の欄 46 本のうち 10 本と、本文の EQR の文 7 本・SYMM の文 16 本を逐語で読んだ。
- olm113 の側は RESULT olm113(11-02)で引いた EQ の証明の欄(5 本)を書いた時に読んだきりで、**対称の種類は数えていない**。凍結の前に olm113 の行を読み直さない。両腕の本文の種類も数えていない。
- v2 の値(olm117 の read.json): 証明の欄の SYMM = olm113 11 / 41(EQ 8 / 12)・olm117 18 / 46・PAR = 6 / 41・4 / 46・本文の SYMM = 26 / 60・27 / 60・PAR = 20 / 60・13 / 60。
- 較正 54 例のうち 17 例(p01〜p03・l01〜l03・l09・n01〜n03・u01・u04〜u07・u10・g02)は olm117 の行から引いた逐語(RESULT §3・§4 に載せた文)。olm113 の行からは引いていない。
- `--selftest` は guard と較正だけで、実値は印字しない(走らせた = PASS・54 / 54)。予想は上を見た上で付けた。

## §1. 計器(R5・R6)

- 当てる文 = 凍結の `proof_of`(証明の欄)と本文(`content` = 生成の全文)。正規化 = olm117 の `norm2`(⟂ → ⊥)。
- **対称の種類**(語の印・正規表現・順序なし・重なり可):
  - **SYM_PT** = O3 についての点対称: `symmetric / symmetry (of …) with respect to / about / around / … (the point / midpoint) O3` / `… the midpoint of O1O2` / `reflection / mirror (of …) over / through / about / in / across O3` / `point symmetry` / `centrally symmetric` / `half-turn` / `rotation by 180` / `O3 is the center of symmetry`。
  - **SYM_LN** = O1O2(中心線・line connecting / joining / through the centers・line of centers・O1O2 の垂直二等分線)についての線対称: 同じ前置詞の形 + `axis of symmetry`。
  - **SYM_OTH** = 他の名指しの軸(l1・TcTh・TcTh の垂直二等分線・接線・O1 and O2・O1・O2・x / y 軸・O3 を通る直線)。
  - **kind** = BOTH(PT ∧ LN)/ PT / LN / OTH / NONE(`symmetr|reflect|mirror` はあるが種類なし)/ —(語なし)。
- **外接線の記憶の印**(内接線では偽・外接線か別の図でだけ成り立つ前提):
  - **PAR3** = v2 の PAR(`TcTh / l1 / tangent ∥ O1O2`・`parallel to (the line) O1O2`・`O1O2 ∥`)+ `parallel to the line connecting / joining / through their centers` + `O1O2 and l1 are parallel` + `the (inner common) tangent is parallel to …`。
  - **PERP3** = `O1O2 is (not / always) perpendicular to the (inner common) tangent / l1 / TcTh` / `l1 / tangent / TcTh is perpendicular to O1O2` / `perpendicular to the line joining their centers`(直前 40 字に `bisector` があれば除く = 垂直二等分線の文は真)。
  - **PBIS3** = `O1O2 is the perpendicular bisector` / `Tc, Th (must) lie on the perpendicular bisector of O1O2` / `perpendicular bisector of O1O2 contains / passes through Tc` / `the tangent is / was the perpendicular bisector`。
  - **OUTER** = PAR3 ∨ PERP3 ∨ PBIS3。
- **asserted(_a)** = 当たりの前(同じ節の中・70 字)か当たりの中に否定・反実仮想の語(`not / n't / never / cannot / would be / would have / unless / false / wrong / incorrect / impossible / neither / nor`)がない。判定は asserted の率で付ける(証明の欄)。本文は「口にした」(否定した物も含む)として記述。
- **較正** = 54 例(PT 10・LN 9・BOTH 1・OTH 3・NONE 4・語なし 2・OUTER 陽性 10・OUTER 陰性 7・否定 8)全部通ること(guard・通らなければ走らない)。陽性統制 = 較正の陽性例。**陰性統制 = prf5 の frontier の moy-2 の証明 20 本**(射影の道・対称も外接線の前提も使わない)。
- 率の分母 = 証明の欄が空でない行(olm113 41・olm117 46 = v2 の値で既知)。一行 = 0.022〜0.024。

## §2. 関門

- **G0**: 入力 3 本と部品 2 本の md5 が一致・較正 54 / 54(guard)。
- **G1**(陰性統制): prf5 の 20 本の証明の欄で OUTER_a ≤ 1 かつ PT_a + LN_a ≤ 1。✗ → 計器が frontier の正しい証明に反応する = Q1〜Q3 を読まない(値は記述)。

## §3. 問いと予想(確率は 0〜1・Δ = olm117 − olm113・証明の欄・asserted の率)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 線対称 LN_a の率の差 Δ | **変わらない** \|Δ\| < 0.06・**増える** Δ ≥ 0.12・**減る** Δ ≤ −0.12・ほか = 間 | 変わらない 0.45・間 0.25・増える 0.15・減る 0.15 |
| Q2 | 点対称 PT_a の率の差 Δ | **増える** Δ ≥ 0.08・**減る** Δ ≤ −0.08・**変わらない** \|Δ\| < 0.04・ほか = 間 | 増える 0.50・間 0.30・変わらない 0.15・減る 0.05 |
| Q3 | 外接線の印 OUTER_a の率の差 Δ | **変わらない** \|Δ\| < 0.06・**増える** Δ ≥ 0.12・**減る** Δ ≤ −0.12・ほか = 間 | 変わらない 0.40・間 0.25・減る 0.25・増える 0.10 |
| Q4 | 記述: 本文の種類の分布(口にした)・類(EQ / MIDO3 / OTHER)ごと・asserted でない当たりの一覧・SYM_OTH の軸・陰性統制の値・種類を名指す率(SYMW の中) | — | — |

- 読みの軸(開示): **Q1 変わらない ∧ Q2 増える** → 結論は図に合い、線対称の前提は図に依らない(olm117 §5 の L3 の支持)。**Q1 減る** → 等しい図では誤った線対称が正しい点対称に置き換わる(前提も図を読んで直る)。**Q1 増える** → 「等しい円」の語が線対称の記憶を強く呼ぶ(記憶は図の語に鍵がかかる)。**Q3 変わらない** → 外接線の印は図に依らない(記憶)。**Q3 減る** → 等しい図で消える(読み)。
- 粗い数で見た olm117 の側(PT 5・LN 5・OUTER 7 前後 / 46)は §0 のとおり既知で、Δ の片腕(olm113)だけが未知。

## §4. 読み方

- `--read` が `olm118/read.json` を書く(関門・Q1〜Q3・腕ごと × 証明 / 本文の集計・行ごとの印と最初の当たりの前後の文)。判定は v3 の値だけで付ける。
- RESULT では、腕ごとに LN の行の当たりの文(最大 6 本)・PT の行(最大 6 本)・OUTER の行(最大 6 本)・asserted でない当たり(全部・最大 8 本)・SYM_OTH の軸(全部)・陰性統制の当たり(全部)を逐語で引く。主 session の読み(L3)は値と並べ、違っても判定は変えない。

## §5. 主張しないこと

- 正規表現は語の印で、対称性や平行を正しく使ったかの検証ではない。asserted は粗い極性(同じ節の 70 字の否定語)で、文脈の「だがこれは一般には成り立たない」(次の文)は拾わない。
- 線対称(O1O2)は両方の図で偽、点対称(O3)は等しい図でだけ真。この札は正しさの率を測らない。
- 本文の値は「口にした」で、却下した案も数える。
- 一つの model・一つの温度・各 60 行。率の一行の幅は 0.022〜0.024 で、帯はそれに合わせて置いた(olm117 の帯より狭い)。
- olm117 の側の値は粗く既知(§0)。Δ の予想は olm113 の側の未知に掛かる。

## §6. 走らせ方と記録

- zebrashark: `python3 ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py --selftest`(PASS・54 / 54・実値は印字しない)→ G10 → 凍結 → `--read`(数秒)。model なし・smoke なし。
- 出力 = `ConstructGap/exp/olm118/read.json`・`read_run.log`。RESULT = `conversations/2026-11-03/RESULT_olm118_moy2_symmetry_kind_outer_marker_v3_20261103.md`。
