# RESULT(札 `mnw1` + 続き `mnw1b`): 役の対応だけでは cut は出ず(Opus 0 / 20・Fable 1 / 20)、「比例として述べよ」だけでは両 model とも**退化した比例 EJ : KP_y = KP_y : EJ** に逃げる(答えの欄 Opus 20 / 20・Fable 19 / 20)。**役の対応 + 比例の形**で Newton の焦点の形 FV : FP_x = FP_x : EJ が答えの欄に出る(Opus 19 / 20・Fable 13 / 20)。Menaechmus の円錐の説明だけでは Opus 0 / 20・Fable は理由の欄に頂点の形(symptoma HP_y² = 4·VF·VH)を 5 / 20(2026-10-22・実行層)

- 札: [PREREG mnw1](PREREG_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md)(凍結 `0f30732b` → 発火前に HEAD の行を直して `2c685fb2`)+ 続き [PREREG mnw1b](PREREG_mnw1b_moy5_continuation_after_usage_limit_opus_fable_xhigh_20261022.md)(凍結 `8a55f839`・mnw1 の runner を import・欠番の単位だけ・要の cell から)。書いた時の HEAD = `8a55f839`(`R1`・fetch 済み・origin の先)。
- **走行**: mnw1 = 12:09:19 発火 → **12:21 に API の月の使用上限で停止**(HTTP 400「You have reached your specified API usage limits. You will regain access on 2026-11-01 at 00:00 UTC.」)。先生が上限を $199 → $249 に上げ(「$199の上限に当たったので、+$50しました」)、mnw1b = 12:29:09 発火 → Opus 12:37:50 完(52 単位)・Fable 13:04:19 完(84 単位・cone/Q1f の残り 9 は費用の上限 $34 で欠番)。経路 = API(stream・adaptive thinking・effort xhigh・max_tokens 48000)。
- **費用**(側の log の見積り): mnw1 = Opus $6.19・Fable $13.56 / mnw1b = Opus $4.34・Fable $36.26(上限 $34 を越えたのは、越えた時点で走行中だった 4 単位の分)。計 ≈ $60。月の余裕は ≈ $5 残り。
- **身分**: §1 = `L1`(`--read` の合わせた表の写し・凍結の述語)。§2 = 判定(凍結の `verdict()`)。§3 = `L1`(逐語は data から機械で写した)+ `L2`(退化した比例の数 = 正規表現・事後)。§4 = 予想の当たり外れ。§5 = `L3`。**伏せ読みはしていない**(腕を見ながら読んだ = 開示)。
- data = `ConstructGap/exp/results_mnw1_moy5_20261022_<model>.jsonl`(text の無い行 = 400 も残す)+ `results_mnw1b_moy5_20261022_<model>.jsonl`(card の欄で見分ける)。側の log = `ConstructGap/exp/logs/mnw1{,b}_moy5_20261022_<model>_sidelog.jsonl`(repo の外)。
- この file の初版(`3914ceb5`・停止の時点の部分の表)は、本改版で置き換えた(初版の表は mnw1b の PREREG §0 に要約が残る)。

## §1. 表(合わせた表・`--read`)
cut = 読み取り器 v2(CUT / SIM-CUT が答え全体に一つでも)/ ans = 答えの欄だけ / 床 = 等長 / eq = 答えの欄が等長 / 退化 = 答えの欄が EJ : KP_y = KP_y : EJ か 1 : 1(正規表現・`L2`)/ focal・vertex = 形の分類(焦点の形 FP_x² = FV·FP_y 系 / 頂点の形 VP_x²・HP_y² 系)/ Newton = Newton の語 / thinking = 中央値(token)

| model | 腕 | n | cut | ans | 床 | eq | 退化 | focal | vertex | Newton | thinking |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Opus 5.5 | K | 10 | **9** | **1** | 10 | 6 | 0 | 9 | 0 | 1 | 3,355 |
| Opus 5.5 | none/Q1 | 20 | **0** | **0** | 20 | 19 | 0 | 0 | 0 | 0 | 3,135 |
| Opus 5.5 | none/Q1f | 20 | **1** | **1** | 20 | 20 | 20 | 0 | 1 | 0 | 3,408 |
| Opus 5.5 | conf/Q1 | 20 | **0** | **0** | 20 | 20 | 0 | 0 | 0 | 12 | 2,602 |
| Opus 5.5 | conf/Q1f | 20 | **19** | **19** | 20 | 20 | 12 | 19 | 0 | 19 | 3,491 |
| Opus 5.5 | cone/Q1 | 20 | **0** | **0** | 20 | 19 | 0 | 0 | 0 | 1 | 2,746 |
| Opus 5.5 | cone/Q1f | 20 | **8** | **4** | 20 | 19 | 17 | 1 | 7 | 16 | 3,819 |
| Fable 5.1 | K | 10 | **10** | **4** | 10 | 10 | 0 | 10 | 1 | 0 | 7,775 |
| Fable 5.1 | none/Q1 | 20 | **0** | **0** | 20 | 20 | 0 | 0 | 0 | 1 | 4,819 |
| Fable 5.1 | none/Q1f | 20 | **3** | **3** | 19 | 19 | 19 | 2 | 2 | 0 | 9,900 |
| Fable 5.1 | conf/Q1 | 20 | **1** | **0** | 20 | 19 | 0 | 1 | 0 | 3 | 4,095 |
| Fable 5.1 | conf/Q1f | 20 | **17** | **13** | 20 | 20 | 13 | 17 | 1 | 18 | 9,054 |
| Fable 5.1 | cone/Q1 | 20 | **5** | **0** | 20 | 20 | 0 | 0 | 5 | 2 | 6,866 |
| Fable 5.1 | cone/Q1f | 11 | **9** | **6** | 10 | 10 | 10 | 1 | 8 | 1 | 11,108 |

- 関門 = 通過(Opus K 9 / 10・Fable K 10 / 10)。`max_tokens` で切れた行 0。HTTP の誤り(mnw1b)0。

## §2. 判定(凍結の規則・余白 3 / 20・天井 17)
- **Opus 5.5(7 腕とも n 20)**: FORM **NO**(none/Q1f 1 対 none/Q1 0)/ CONF@Q1 **NO**(0 対 0)・CONF-ANS@Q1 NO / CONE@Q1 **NO**(0 対 0)・CONE-ANS@Q1 NO / CONF@Q1f **YES**(19 対 1)/ CONE@Q1f **YES**(4 対 1)/ **CONF×FORM YES**(18)/ **CONE×FORM YES**(3 = 余白ちょうど)。
- **Fable 5.1**: **INCOMPLETE**(cone/Q1f が 11 / 20・費用の上限)。他の規則を記述として当てると: FORM NO(3 対 0・4 に届かない)/ CONF@Q1 NO(1)・CONF-ANS@Q1 NO / **CONE@Q1 YES**(5 対 0・答えの欄は 0 = CONE-ANS@Q1 NO)/ CONF@Q1f YES(13 対 3)/ CONE@Q1f(6 / 11・判定せず)/ CONF×FORM YES((13 − 3) − (1 − 0) = 9)/ CONE×FORM NO((6 − 3) − (5 − 0) = −2・n 11)。

## §3. 中身(逐語 = `L1`・data から機械で写した)
1. **none/Q1f(比例の形の一文だけ)**: 答えの欄は Opus 20 / 20・Fable 19 / 20 が **退化した比例**。model は「この四点では真の比例中項は組めない」と自分で書く(Opus r4「the configuration supplies no third length for a true mean proportional among these four points」・r11「with only E, J, K, P_y in play, the requested 'mean proportional' form reduces to this degenerate ratio of 1」)。cut の在る行(Opus 1・Fable 3)は自力の格子:
   - r3「EJ : KP_y = 1 : 1, i.e. |EJ| = |K P_y| (= |F P_y|). In mean‑proportional form: VE : VP_x = VP_x : VJ (VP_x² = VE·VJ), whence EJ = VE + VJ = VD + VH = 」 読み取り = [':VE:VPx = VPx:VJ', 'VPx² = VE·VJ']
   - r7「EJ = KP_y, i.e. EJ : KP_y = 1 : 1; as a mean proportional, VE : VP_x = VP_x : VJ (equivalently EJ : FP_x = FP_x : VE), so that the segment EJ cut on t」 読み取り = ['VE:VPx = VPx:VJ', 'EJ:FPx = FPx:VE']
   - r17「EJ : KP_y = 1 : 1  —  more precisely both segments are the same third proportional of FV and FP_x:  FV : FP_x = FP_x : KP_y  and  FV : FP_x = FP_x : E」 読み取り = ['FV:FPx = FPx:EJ', 'FV:FPx = FPx:KPy']
2. **conf/Q1(役の対応だけ)**: Opus 0 / 20(比例中項の語も式も 0 本)。Fable 1 / 20(理由の欄に焦点の形):
   - r5「EJ = KP_y (equivalently EJ = P_yK = P_yF): the segment cut on the tangent g from E to J equals the segment P_yK, i.e. the distance of P_y from the lin」 読み取り = [':FPx² = FV·FPy']
3. **conf/Q1f(役の対応 + 比例の形)**: 答えの欄に Newton の形に問いの字を代入した三項の比例(= 06-25 の CUT の定義の形 FV·EJ = FP_x²)。Opus 19 / 20(焦点の形 19)・Fable 13 / 20(cut 17・焦点の形 17)。Fable の例:
   - r1「EJ = KP_y, i.e. KP_y : EJ :: 1 : 1 (the segment EJ cut off on the tangent g equals the distance of P_y from the directrix e, which is also FP_y); equi」 読み取り = ['FV:FPx = FPx:EJ', 'FPx² = FV·FPy']
   - r3「EJ = KP_y, i.e. EJ : KP_y :: 1 : 1 — the segment EJ cut off on the tangent g equals the distance of P_y from the line e (= FP_y, the focal distance). 」 読み取り = ['FV:FPx = FPx:EJ', 'FV:FPx = FPx:EJ']
   - r4「KP_y = EJ, i.e. KP_y : EJ :: 1 : 1 — both segments equal the focal distance FP_y (= VF + VH); equivalently, with Lemma XIV, VE : KP_x = KP_x : EJ (the」 読み取り = ['VE:KPx = KPx:EJ', 'FPx² = FV·FPy']
4. **cone/Q1(Menaechmus の円錐の説明だけ)**: Opus 0 / 20。Fable 5 / 20 = 答えの欄は等長のまま、理由の欄に **symptoma HP_y² = 4·VF·VH**(頂点の形 5 / 5):
   - r6「|EJ| = |K P_y| (equivalently |EJ| = |F P_y|, since P_y F = P_y K)」 読み取り = ['PyH² = 4·VF·VH']
   - r9「EJ = KP_y (and both equal FP_y): the segment of the tangent g from E to J has the same length as the segment P_yK, i.e. |EJ| = |P_yK| = |P_yF|.」 読み取り = [':PyH² = 4·VF·VH']
   - r15「|EJ| = |KP_y|  (and both equal |P_yF|): the segment EJ on the tangent g always equals the segment KP_y, i.e. EJ = KP_y = P_yF for every choice of P_x」 読み取り = [':PyH² = 4·FV·VH']
   - r16「|EJ| = |KP_y| (equivalently |EJ| = |FP_y| = |KP_y|: the segment EJ cut on the tangent g equals the distance from P_y to the line e)」 読み取り = ['HPy² = 4·VF·VH']
   - r19「|EJ| = |KP_y| (the segment cut on the tangent g from E to J equals the segment K P_y, for every position of P_x on h1)」 読み取り = ['HPy² = 2·FD·HV']
5. **cone/Q1f(円錐の説明 + 比例の形)**: 答えの欄は退化した比例が大半(Opus 17 / 20・Fable 10 / 11)で、横に symptoma を添える。形は頂点が多数(Opus 7 / 8・Fable 8 / 9)。Opus の例:
   - r6「EJ = KP_y: the segments EJ and KP_y are always equal. This is genuinely an equality of lengths. The only way to write it as a proportion is EJ : KP_y 」 読み取り = ['PyH² = 4·VE·VH']
   - r7「EJ = KP_y. As a proportion this is only EJ : KP_y = 1 : 1. The mean-proportional form needs points outside the focus set: FP_x is the mean proportiona」 読み取り = ['FPx² = VF·EJ', 'FPx² = VF·KPy']
   - r12「EJ = KP_y, i.e. EJ : KP_y = 1 : 1. This is an equality of lengths. Among E, J, K, P_y alone, no genuine mean proportional holds; the mean proportional」 読み取り = ['HPy² = 4·VE·VJ', 'HPy² = 4·VE·VJ']
6. **none/Q1(基線・API xhigh)**: 両 model 0 / 20・床 20 / 20(essay4 の A = high と同じ)。

## §4. 予想の当たり外れ
mnw1 §6(発火の前):
- **P1(FORM 両 model YES・≥ 10 / 20)= 外れ**(Opus 1・Fable 3)。形の指図は点の集合に負け、等長が比例の形に言い換えられた。
- **P2(CONF@Q1 Fable ≥ 10・Opus ≥ 5)= 外れ**(Fable 1・Opus 0)。
- **P3(CONE@Q1 両 model NO)= Opus 当たり(0)・Fable 外れ(5 / 20 = 規則で YES)**。
- **P4(none/Q1 ≤ 2)= 当たり**(0・0)。
- **P5(形: conf → 焦点・cone → 頂点)= 当たり**(conf/Q1f 焦点 19 / 19・17 / 17 / cone の cut は頂点 7 / 8・5 / 5・8 / 9)。
- **P6(交互作用なし)= 外れ**(CONF×FORM Opus 18・Fable 9)。
mnw1b §3(部分を見た後・`L2`):
- Q1(Fable conf/Q1 ≤ 3)= 当たり(1)。Q2(Fable conf/Q1f cut_ans ≥ 15・焦点)= 外れ(13・焦点の形は当たり)。Q3(none/Q1f の残り ≤ 3)= 当たり(3)。Q4(cone/Q1 ≤ 2)= Opus 当たり・Fable 外れ(5)。Q5(cone/Q1f = 退化が多数・頂点 > 焦点・cut_ans ≤ 5)= 退化と形は当たり・cut_ans は Fable 6 / 11 で外れの方向。

## §5. 読み(`L3`・採否は先生)
1. **「比例として述べよ」は点の集合に負ける**。両 model とも指図の字面を最も安い形で満たし、四点の間に比例中項が無いことを自分で述べる。答えの欄の族を限るのは問いの点の集合(RECORD neq)で、形の指図より強い。満足停止の形そのもの。
2. **役の対応は、形の指定と組になって初めて効く**(CONF×FORM)。役だけでは補助定理の関係は書かれず(0・1)、形だけでは退化し、二つそろうと FV : FP_x = FP_x : EJ が一段で出る。これは「補助定理の形に問いの字を代入した」= K の一段手前で、説明で看破したのではない。先生の問い「Fable にどんな説明を足すと cut するか」への答え(本札の範囲): **役の対応 + 比例の形の指定**(Fable 13 / 20)。
3. **Menaechmus の説明は、model の格子の形を頂点の symptoma に寄せる**(頂点 7 / 8・5 / 5・8 / 9)。焦点の語を与えていないのに、係数は 4·VF(焦点距離)で書かれる = 先生 10-22「焦点は本質的ではない … それでも二次式に辿り着くのが attractor として本領発揮」。Fable は説明だけで理由の欄に 5 / 20 書き、Opus は 0 = Fable の方が Menaechmus の層に手が届く(ただし答えには置かない)。
4. 三層を体制で言えば、床 = Pappus(焦点・準線)/ cut = Menaechmus(断片の比例中項)/ attractor = Descartes(座標の二次式)。model は Pappus から Descartes へ跳び、Menaechmus の層は役(Newton)か説明(Fable)で指された時だけ現れる(memory `project_moy5_three_regimes_menaechmus_pappus_descartes_20261022`)。

## §6. 主張しないこと
- Fable の cone/Q1f は 11 / 20(INCOMPLETE)。CONE×FORM(Fable)は判定しない。
- 退化した比例の数は事後の正規表現(`L2`)。形の分類は `net` の鍵と `src` の正規表現(`L2`)。伏せ読みはしていない。
- 二つの走行(mnw1・mnw1b)は同じ日・同じ経路・同じ鍵だが、間に上限の出来事を挟む。
- API の xhigh と `claude -p` の xhigh は同じ目盛りとは限らない。一つの作図・一つの配置・二つの model。
- 「役の対応」は指図の一種で、「説明」が効いたとは読まない(§5-2)。

## §7. 次(先生の判断)
1. Fable の cone/Q1f の残り 9 単位(≈ $4・月の余裕 ≈ $5)を引くか(小さな続きの札・上限に当たれば止まる)。11-01 まで待つ手もある。
2. 焦点を作図から消した Menaechmus 版の札(先生・後日)。予想: 焦点を消しても座標を置いて y² = (係数)·x に着く。
3. ConstructGap README の moy-5 の行に「開いた条件での数」の注(prf3 §6-1)と、本札の「形の指図は点の集合に負ける」を足すか。
