HEAD(R1) = 63f8a35c(凍結時の HEAD・origin の 1 commit を merge 済み・origin より 7 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm117`・凍結 2026-11-03): moy-2 の半径の等しい対照 — 中心はそのまま、二円の半径を等しくした図(内接線が O3 を通る)に olm113 の M2A(考えを先に + 仮説か問い + 裏付け)を当て、「対称性」の前提と「Tc・O3・Th の共線」の答えが図を読んだ物か記憶かを分ける(OLMo-3 32B base・60 行)

- 発注(逐語・先生 11-03): 「**直交を使ったかの述語v2、moy-2へ適用、半径の等しい対照へ順次進みます。**」の三枚目。olm113 の §6-2「『対称性』は半径が等しい図の記憶」と §8「半径の等しい問いの文(対照)で分けられる」への対照。
- G10 の欄: 比べる物 = 「半径の等しい図で conjecture が MIDO3(O3 = TcTh の中点 / Tc・O3・Th が共線 / O3 ∈ l1)である行の割合(conjecture が取れた行の中)と、olm113 の M2A の同じ割合(0.34)の差」/「conjecture が apex(等距離)の行の証明の欄で SYMM(symmetr・reflect)の割合と、olm113 の同じ割合(8 / 12)の差」/「半径が等しいことへの言及 EQR の数(証明の欄・本文・記述)」 / 計器 = 凍結の hq 共通の部品(apex_m2・status_of・proof_of・score_m2・較正 61 / 61)+ この札の v2(conjecture の類 MIDO3・前提の語 SYMM・PAR・HOMO・POWER・COLL・EQR・較正 22 例)+ 図の検算 7 項 + 問いの文の差分の検査(olm113 の M2A と違う行は座標 4 行だけ)/ 雛形 = いいえ
- runner = [olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)・凍結の部品 [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(md5 `426e2089…` を guard・触らない)・問いの文の作り = `prompts.build("higashida_axis", "A", 37)` の geom を process 内で差し替えて `H.olmo_prompt("M2A")`(prompts.py・geometry.py は触らない・差し替えを外すと olm113 の M2A の md5 `56182280…` に戻ることを guard)。比べる元 = `olm113/gen.json`(md5 `db0fde6e…` を guard)の M2A 60 行に**同じ v2 を当てる**。走らせる所 = zebrashark(32B は一つずつ・olm116 の後)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- 主 session は olm113 の RESULT(apex 16 / 60・証明の欄の「対称性」8 / 12・apex でない行の半分が「Tc・O3・Th の共線」)を書いた。この札の v2 を olm113 の M2A 60 行に当てた値(`--selftest` が印字): MIDO3 17 / 50(parsed)= **0.34**・EQ 16 / 50 = 0.32・EQ の証明の欄の SYMM **8 / 12**・本文の EQR 2 / 60。**予想はこれを見た上で付けた**。MIDO3 の正規表現は olm113 の conjecture の言い方(「O3 is collinear with Tc and Th」「collinear(Tc, O3, Th)」)を見て広げた(両腕に同じ物を当てる)。
- 図の事実(主 session の計算・runner の検算 7 項): 中心 O1・O2・O3 は olm113 と同じ(|O1O2| = 13.003)。半径 r = (7.4607 + 3.6869) / 2 = **5.5738**(両方)。二円は離れている(2r = 11.15 < 13.00)。内接線 l1 は O3 を通り、Tc・Th は O3 について点対称 = **O3 は TcTh の中点・Tc・O3・Th は共線**。apex(|O3Tc| = |O3Th|)は退化して成り立つ。二本の内接線のうち olm113 の l1 に近い方(Th の距離 1.887)を取った。37° の回転は同じ。
- 問いの文は olm113 の M2A と**座標の 4 行(h1・c の半径・Tc・Th)だけ違う**(guard で検査)。前提の文「general (non-special, non-degenerate)」はそのまま(§5)。
- smoke(凍結の前・2 行・読まない): 数は §6。

## §1. 計器(R5・R6)

- **問いの文** = olm113 の M2A の文で座標だけ半径の等しい図に置き換えた物(md5 `7e52c06a…`)。生成 = olm113 と同じ(温度 0.7・max_new 12288・3 batch × 20 行・seed 20261160〜62・olm87 / 90 / 112 / 113 / 114 / 116 と重ねない)。
- **凍結の読み**(hq 共通の部品): conjecture(JSON の欄)・apex_m2(等距離)・status_of・proof_of・score_m2(道の札)。
- **v2(この札)**:
  - conjecture の類 **cls** = EQ(凍結の apex)/ **MIDO3**(apex でなく、O3 = TcTh の中点・Tc・O3・Th 共線・O3 ∈ l1 / TcTh・`collinear(Tc, O3, Th)`・`O3 is collinear with Tc and Th`)/ OTHER / NONE(空)。順に最初に当たる物。「collinear」だけ・「O1, O3, O2 collinear」・「O3 is collinear with the midpoint of Tc and Th」は OTHER。
  - 前提の語(証明の欄と本文・記述)= SYMM(`symmetr|reflect`)・PAR(TcTh ∥ O1O2 など)・HOMO・POWER(凍結の ALT_power)・COLL・**EQR**(`equal radii|radii are equal|same radius|r_c = r_h|radius 5.5738|equal circles|congruent circles` など)。
- **較正** = hq 61 / 61 + v2 22 例(cls 16・前提 6)+ 図の検算 7 + 問いの文の検査 3(等しい図の文に `Circle(O1, 5.5738)` と `Circle(O2, 5.5738)`・元の文に 3.6869 / 7.4607・差分は 4 行)。guard で通らなければ走らない。
- 同じ v2 を olm113 の M2A 60 行にも当てる(比べる元・同じ計器・図だけ違う)。

## §2. 関門

- **G0**: olm113 の M2A が 60 行読める(md5 一致)。
- **G1**: conjecture が取れた行 ≥ 0.80(48 / 60)。✗ → Q1・Q2 を読まない。
- **G2**(記述の側): status が hypothesis / question の行 ≥ 0.70。✗ → status の記述に注記。
- Q2 の追加条件: 両腕で EQ の行の証明の欄(空でない)≥ 8。✗ → Q2 を読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | MIDO3 の割合(parsed の中)の差 Δ = 等しい図 − olm113(0.34) | **増える** Δ ≥ 0.15・**減る** Δ ≤ −0.15・**変わらない** \|Δ\| < 0.10・ほか = 間 | 増える 0.45・変わらない 0.30・間 0.15・減る 0.10 |
| Q2 | EQ の行の証明の欄で SYMM の割合の差 Δ = 等しい図 − olm113(8 / 12 = 0.667) | **増える** Δ ≥ 0.20・**減る** Δ ≤ −0.20・**変わらない** \|Δ\| < 0.10・ほか = 間 | 変わらない 0.40・増える 0.30・間 0.20・減る 0.10 |
| Q3 | 記述: EQR(半径が等しいことへの言及)の数(証明の欄・本文)・EQ の率・status(類ごと)・道の札・T・上限・答えが先・olm113 との並び | — | — |

- 読みの軸(開示): olm113 の「対称性」の前提と「共線」の答えが**図の記憶**なら、半径を等しくしても率は変わらないか増える(記憶が図と一致する)。もし OLMo が座標から図を読んでいるなら、等しい図では O3 ∈ l1 が数値で出るので MIDO3 が増え、EQR の言及が出る。**減る**なら、olm113 の共線は等しい図の記憶ではない。

## §4. 読み方

- `--read` が `olm117/read.json` を書く(関門・Q1〜Q3・行ごとの類と印・olm113 の同じ値)。判定は v2 の値だけで付ける。
- RESULT では、MIDO3 の行の conjecture と証明の欄を行の名の順に最大 10 本、EQ の行の証明の欄を最大 5 本、EQR を含む本文の文を最大 5 本、逐語で引く。主 session の読み(L3)は値と並べ、違っても判定は変えない。

## §5. 主張しないこと

- 等しい図では MIDO3 は**真**(退化)で、apex と同値ではない。この札は「正しさ」の率を測らない。olm113 と並べる率は、同じ v2 の類の率。
- 前提の文「general (non-special, non-degenerate)」は等しい図でも残してある(語を変えないため)。等しい図は特別な図で、文と図が食い違う。OLMo がそれに気付くかは EQR で記述するだけ。
- 一つの model・一つの温度・60 行・一つの図(半径は平均で揃えた)。半径をどう揃えるか(平均 / 大きい方 / 小さい方)は一つしか試さない。
- SYMM は語の印で、対称性を正しく使ったかの検証ではない(等しい図では対称性の前提は真)。

## §6. 走らせ方と記録

- zebrashark: `python ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py --selftest`(PASS)→ `--smoke`(凍結の前・2 行・max_new 1536・読まない・olm116 の後)→ 凍結 → `--gen`(約 2 時間の見込み・olm113 の M2A は 1.9 時間)→ `--read`。
- smoke(凍結の前・seed 20261195・2 行・max_new 1536・読まない・zebrashark 12:42 JST・壁時計 170 s・Traceback 0・`olm117/smoke.json`・`smoke_run.log`・問いの文 417 token): 行 1 = T 1,169・status hypothesis・証明の欄 168 字 / 行 2 = T 275・hypothesis・証明の欄 133 字。本文は読んでいない。
  - 開示: smoke の log は conjecture の類(cls)も印字する作りで、主 session は 2 行とも **MIDO3** であることを目にした。§3 の予想は smoke の前に書いた物のままで、変えない。
- 出力 = `ConstructGap/exp/olm117/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-03/RESULT_olm117_moy2_equal_radii_control_20261103.md`。
