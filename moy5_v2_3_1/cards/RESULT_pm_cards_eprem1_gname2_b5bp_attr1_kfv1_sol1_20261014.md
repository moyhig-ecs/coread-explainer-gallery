# RESULT(午後の六つの小札): `eprem1`・`gname2`・`b5bp`・`attr1`・`kfv1`・`sol1`

- 執筆時 HEAD = `152f65dc30104bb69a75324558256c967d1632a7`(R1: fetch の後・origin に対し ahead 18 / behind 0 = pull する物なし)。2026-10-14(水)13 時台・実行層 = Opus 5.5 xhigh(zebrashark)。
- 札 = [PREREG](PREREG_pm_cards_eprem1_gname2_b5bp_attr1_kfv1_sol1_20261014.md)(凍結 `d530a409`)・修理 `152f65dc`(下 §7-1)。先生(逐語): 「APIで走らせられるものは走らせましょう。」
- 走行: 六つとも 12:55:49 までに終わった。HTTP の誤り 0(修理の後)。text の無い単位の取り直し = gname2 の Haiku で 1 回(規則どおり)。
- **判定と講評は先生。** 三値は札の規則のまま(n = 20 の割合の差 d・|d| ≤ 0.1 null・≥ 0.5 strong・間は weak)。下の「合 / 外」は予測の文面と数を並べただけ。
- 手の読み(kfv1)の全文 = [SOURCE](SOURCE_moy5_kfv1_kframe_hint_v1_140_answers_with_reading_labels_20261014.md)・鍵 = `ConstructGap/exp/kfv1_blind_reading_labels_20261014.json`。

## §0 費用(side log の見積もり・単価 = ROSTER)
| 札 | model | 呼び出し | 見積もり |
|---|---|---|---|
| eprem1 | Sonnet 4.6 | 40 | $1.231 |
| gname2 | Haiku 5.5 / Sonnet 5.5 | 21 / 20 | $0.035 / $0.359 |
| b5bp | Sonnet 5.5 / Opus 5.5 / Fable 5.1 | 40 / 40 / 40 | $1.266 / $3.201 / $9.629 |
| attr1 | Haiku 5.5(R-off) | 100 | $0.027 |
| kfv1 | Sonnet 5.5 / Opus 5.5 / Fable 5.1 / Haiku 5.5 | 40 / 40 / 40 / 20 | $0.417 / $0.917 / $4.280 / $0.008 |
| **Anthropic 計** | | | **$21.37**(PREREG の見積もり ≈ $28・上限の和 $53)|
| sol1 | GPT-6 Sol | 107 | $1.34(OpenAI) |
- 昼の Console の表示 $133.63 / $199 に足すと ≈ $155(見積もりの上で・Console の数は先生の画面で)。promo の失効 = 10-17 09:00 JST。

## §1 `eprem1`(H_ctx の門)
| 腕(Sonnet 4.6・n 20)| bind | 同定∨ | 答えの欄の He / Hi | 行き先 | thinking の中央値 |
|---|---|---|---|---|---|
| 基線 A(essay2・10-13)| 2 | — | — | — | — |
| **E-prem1**(段落 1 + 直角の補題)| **20** | 20 | 0 | B-bind 20 | 876 |
| **E-prem0**(段落 1 だけ)| **0** | 1 | 1 | B-attractor 14・B-stuck-L1 6 | 2141 |
- 門の規則: E-prem1 = 20 ≥ 19 → 天井 → E-prem0 で門をやり直す → **E-prem0 = 0 = 床**。規則は E-prem0 の ≤ 1 の先を書いていない → **ここで止めた**(Sonnet 5.5・Haiku 4.5・Haiku 5.5 は走らせていない・H_ctx の Δ は計算していない)。§7-3。
- d(記述): E-prem1 − A = +0.90(strong)・E-prem0 − A = −0.10(null)・E-prem1 − E-prem0 = +1.00。
- 二つの passage の差は一文(補題: "Bisectors of adjacent supplementary angles are perpendicular: ∠O1 QO2 = 90°." とその前の二文)。E-prem0 に残る段落 1 は相似の中心(Sex・Sin)を名指す文を含み、E-prem0 の行き先は attractor 14。
- 次の候補(先生の判断): Sonnet 5.5 × {E-prem1, E-prem0}(≈ $1)。4.6 と 5.5 の差の差を取るには、天井でも床でもない passage が要る(段落 1 + 補題の一部、等)= 新しい文面 = 先生と判断層。

## §2 `gname2`(名の条項を問いの末尾の注記に)
| model | G-name2 bind | run2 の A / B | 埋めた割合 (bind − A)/(B − A) | 同定∨ | 三点の円 | 答えの欄の行き先 |
|---|---|---|---|---|---|---|
| Haiku 5.5 | **10** / 20 | 2 / 20 | **0.44** | 10 | 1 | bind 10・名のない関係 10 |
| Sonnet 5.5 | **3** / 20 | 1 / 20 | **0.11** | 3 | 0 | 名のない関係 10・他の形 7・bind 3 |
- Sonnet の「他の形」7 本は全部「中心が直線 O1O2 の上に在る円」(逐語の例: "X1, X2, X3, X4 are concyclic (lie on one circle whose center is on line O1O2)")。注記の「与えられた記号で、データで名を付けよ」に、円そのものでなく中心の在処で応じた形。等脚台形か O1O2 についての対称を言う答えが 3 本(名のない関係に数えた)。
- 並べる既存の数: alt3 の Q-name2(一回目の答えの**後**に、退けの一文つきで同じ条項を返す)= Sonnet 2 → **13**(埋めた割合 0.61)・Haiku 4 → **14**(0.62)([RESULT 昼 §3](RESULT_adjudication_orders_1_to_5_sym5_circb1_alt3_run2_roff2_20261014.md))。gname2(答えの**前**・問いの末尾の注記・退けの一文なし)= Sonnet 3(0.11)・Haiku 10(0.44)。腕の作りが三点で違う(答えの前か後か・退けの一文・置き場所)ので、位置の効果を一つの数にはしていない。

## §3 `b5bp`(moy-5 (b) 版 β′)
| model | 腕 | cut(両欄)| 答えの欄の cut | 床 | 焦点–準線の道 | 座標の形 式 / 媒介 | FRAME-APPLY v1 | June の門 | thinking 中央値 |
|---|---|---|---|---|---|---|---|---|---|
| Sonnet 5.5 | Bbp | **2** | 0 | 20 | 0 | 0 / 0 | — | FALSE-STRUCT 3・CLOSURE 17 | 1030 |
| | E-full+Bbp | **0** | 0 | 20 | 11 | 0 / 0 | 0 | TRAP 11・CLOSURE 9 | 1740 |
| Opus 5.5 | Bbp | **7**(r8 を含む・§3-1)| 0 | 20 | 7 | 0 / 5 | — | TRAP 7・CLOSURE 5・GENUINE-CUT 8 | 1753 |
| | E-full+Bbp | **3** | 0 | 20 | 19 | 5 / 6 | 2 | TRAP 15・GENUINE-CUT 4・FALSE-STRUCT 1 | 2369 |
| Fable 5.1 | Bbp | **0** | 0 | 20 | 3 | 0 / 0 | — | TRAP 3・GENUINE-CUT 5・CLOSURE 12 | 2233 |
| | E-full+Bbp | **1** | 0 | 20 | 18 | 0 / 0 | 13 | TRAP 17・GENUINE-CUT 1・FALSE-STRUCT 1・CLOSURE 1 | 3525 |
- 基線(essay4・同じ model・同じ日): A cut 0 / 20・E-full cut 0 / 20(三つとも)。
- d(記述): Bbp − A = Sonnet +0.10(null)・Opus +0.35(weak)・Fable 0(null)/ E-full+Bbp − E-full = Sonnet 0・Opus +0.15(weak)・Fable +0.05(null)/ (E-full+Bbp) − Bbp = Sonnet −0.10(null)・Opus −0.20(weak)・Fable +0.05(null)。
- **答えの欄の cut は 6 腕とも 0。** cut は全部、理由の欄に書かれた関係(β′ が求めた場所)。
- cut の形(読み取り器 v2・全文は付-A): Opus Bbp = `FV·EJ = FPx²` 型 5 本(r3・r6・r16・r19 + 加法の形で書いた r8)・`VH = VD·VPx²/VF²` 型 1(r4)・`VPx² = VF·VH` 1(r11)/ Sonnet Bbp = `KPy = KPx·FK/FD` 2(r0・r15)/ Opus E-full+Bbp = `VH = PyH²/(4·FV)`(r1)・`FK² = 2·FD·KPy`(r6)・`VPx² = VF·VH`(r13)/ Fable E-full+Bbp = `PyH² = 4·VF·VH`(r12)。
- **June の門の GENUINE-CUT は読み取り器 v2 の cut より多い**(Opus Bbp 8 対 6・Opus E-full+Bbp 4 対 3・Fable Bbp 5 対 0・Fable E-full+Bbp 1 対 1 だが別の答え)。門が GENUINE-CUT と言い v2 が cut と読まなかった 11 本(Opus Bbp 2・Opus E-full+Bbp 3・Fable Bbp 5・Fable E-full+Bbp 1・付-B)は、どれも v2 が DEGENERATE / SIM-DEGEN(VD = VE なので恒等に潰れる比 `EJ·VD = DH·VE`・△VHJ ∼ △VDE 等)と読んだ関係を含む。逆に v2 の cut のうち Opus E-full+Bbp の r1・r6 と Fable E-full+Bbp の r12 は門が GENUINE-CUT と言っていない。
### 3-1 境の 1 本(r8)= cut に数える(先生 10-14 午後・逐語「1 cutに数えましょう。」)
- Opus Bbp r8 は `VF·EJ = VF² + VPx²`(= `EJ = VF + VPx²/VF`)を書き、v2 は ADDITIVE と読んだ。`VF² + VPx² = FPx²` を代入すれば r3 等の `FV·EJ = FPx²` と同じ関係。
- 裁定を述語にした(R5): **v2 が ADDITIVE と読んだ関係のうち、`X·FV = FV² + VPx²` か `X = FV + VPx²/FV`(X ∈ {EJ, KPy}・字の順と左右の入れ替えを含む)の形を cut に足す**。b5bp の 120 本と基線(essay4 の A・E-full・三 model・120 本)に当てた: 当たるのは Opus Bbp の r6・r8・r16・r19 の 4 本で、新しく cut になるのは **r8 だけ**(r6・r16・r19 は既に cut)。基線は 0。
- 凍結の読み取り器 v2 は変えていない(述語は本 RESULT の上で足した列)。座標の形を cut に数えるか(昼の §4-1)は別の問いとして残る。
- 座標の形(記述・下限): Opus は E-full+Bbp で式 5 / 媒介 6(昼の §4-1 の Opus E-full 4 / 3 と同じ向き)。Bbp でも媒介 5。

## §4 `attr1`(attractor-state・Haiku 5.5・R-off)
| 腕(n 20)| bind | 答えの欄の He / Hi | 同定∨ | 行き先 |
|---|---|---|---|---|
| A | 0 | 7 | 2 | B-attractor 18・B-stuck-L1 2 |
| B | 1 | **18** | 2 | B-attractor 19・B-bind 1 |
| **B-diam** | 1 | **19** | 1 | B-attractor 19・B-bind 1 |
| D-fc@v1 | 0 | **4** | 2 | B-attractor 14・B-stuck-L1 6 |
| **E-abs** | **20** | **0** | 20 | B-bind 20 |
- thinking = 0(全部・R-off の経路が効いている)。stop = end_turn 100。
- d(He / Hi・記述): B − A = +0.55(strong)・B-diam − A = +0.60(strong)・B-diam − B = +0.05(null)・D-fc − A = −0.15(weak)・E-abs − A = −0.35(weak)。bind: E-abs − A = +1.00。
- 「中心」と「半径」の語を抜いても(B-diam)、He–Hi を直径とする円への行き先は B と同じ(19 対 18)。

## §5 `kfv1`(K-frame を hint v1 で・手の読み)
### 5-1 梯子(返し 昼 §3-2・RECORD 昼 §4-3 と同じ畳み方: Yk・D は段 1 に入れて旗に数える)
| | 段 0(G)| 段 1(T + 旗)| 段 2(Y)| 旗(準線へ / 取り違え)| 梯子の外(B)| Dandelin の語 |
|---|---|---|---|---|---|---|
| Haiku 5.5 KF | 20 | 0 | **0** | 0 / 0 | 0 | 0 |
| Sonnet 5.5 KF | 11 | 9 | **0** | 0 / 0 | 0 | 0 |
| Sonnet 5.5 KF@U | 12 | 8 | **0** | 0 / 0 | 0 | 0 |
| Opus 5.5 KF | 0 | 11 | **8** | 1 / 2 | 1 | 4 |
| Opus 5.5 KF@U | 0 | 16 | **4** | 1 / 0 | 0 | 7 |
| Fable 5.1 KF | 0 | 0 | **20** | 0 / 0 | 0 | 19 |
| Fable 5.1 KF@U | 0 | 3 | **15** | 0 / 1 | 2 | 17 |

### 5-2 古い hint(sym5 の K-frame・RECORD 昼 §4-3)と並べる(段 2)
| | 古い hint | hint v1 | 古い(境を段 1 に)| v1(境を段 1 に)|
|---|---|---|---|---|
| Fable KF | 17 | **20** | 17 | 20 |
| Fable KF@U | 8 | **15** | 8 | 15 |
| Opus KF | 9 | **8** | 4 | **0** |
| Opus KF@U | 2 | **4** | 0 | 2 |
| Sonnet KF | 1 | **0** | 0 | 0 |
| Sonnet KF@U | 0 | 0 | 0 | 0 |
| Haiku KF | 0 | 0 | 0 | 0 |
- **境(是)** = 焦点を正しく述べ(球が切断面に触れる点 = F)、KPy は「作図がその焦点距離の実長を写した物」と置くだけで、焦点–準線の段を述べない Y(RECORD 昼 §4-2 の 8 本と同じ形)。hint v1 では **10 本・全部 Opus**(KF 8 = Opus KF の Y の全部・KF@U 2)。Opus の Y で準線を述べた物は KF@U の 2 本だけ。Fable の Y 35 本は全部 準線を述べる。
- 言える事(記述): hint v1 で Fable は KF・KF@U とも段 2 が増えた(17 → 20・8 → 15)。Opus の KF の段 2 は 9 → 8 で、境の読みを厳しくすると 4 → 0。Sonnet・Haiku の段 2 は 0。Sonnet は段 0 が増えた(KF 4 → 11)。
- 言えない事: 古い hint の読みと今日の読みは同じ実行層の別の時刻の読み(一人・別 session)。T と G の境で迷った物が 10 本在る(印「境(T/G)」・Sonnet KF 4・Sonnet KF@U 2・Opus KF@U 2・Haiku 1・Fable KF@U 1)。Sonnet の段 0 の増加は、hint v1 の文面が「平行円が g と J で交わる」を与えている(言い直すだけで EJ の在処が書ける)ことと、読みの揺れとを分けられない。
- 機械の FRAME-APPLY v1c(E-full 型の腕用・hint の腕には使わない取り決め)との突き合わせ: 偽陽性 0・偽陰性 13(Opus 11・Fable KF@U 2)。v1c を hint の腕に使わない取り決めの裏付けとして記録する。

## §6 `sol1`(答えの後の介入・GPT-6 Sol)
| | 一回目 → 最終 | 改稿率 | 埋めた割合 | 名のなかった一回目の行き先 | 三点の円 |
|---|---|---|---|---|---|
| A / B(器)| 4 / 20・20 / 20(器は立つ)| | | | |
| R-re2 | 4 → 3(得 0・失 1)| 2 / 16 = 0.12 | −0.06 | 名のない関係 15・別の関係 1 | 0 |
| R-quote2 | 4 → 5(得 2・失 1)| 11 / 16 = **0.69** | 0.06 | 別の関係 4・名のない関係 9・bind 2・他 1 | 0 |
| R-blindK | 4 → 5(得 1・失 0)| 4 / 16 = 0.25 | 0.06 | 名のない関係 13・別の関係 2・bind 1 | 0 |
- R-blindK の回ごとの bind: 7 / 6 / 5・止まり方 = 変わらず 18・kmax 2。
- 検定形 (2): R-quote2 = 前件(改稿率 ≥ 0.5)が立ち、(2) は立たない / R-blindK = 前件が立たず (2) は当てはまらない。
- 使った費用 $1.34(呼び出し 107・reasoning 109,694 token)。

## §6′ 予測と並べる
**判断層**(返し 昼 §13・§11)
| # | 予測 | 出た数 | |
|---|---|---|---|
| 1 | E-prem1: Sonnet 4.6 は 6〜14 | 20 | 外 |
| 1 | Sonnet 5.5 ≥ 16・差の差 ≥ +0.3・Haiku 4.5 ≤ 4・Haiku 5.5 ≥ 12 | 走らせていない(§1) | — |
| 2 | G-name2: Haiku の埋めた割合 ≤ 0.2 | 0.44 | 外 |
| 2 | Sonnet 0.3〜0.5 | 0.11 | 外 |
| 3 | β′ 単独: Fable の cut ≥ 8 | 0 | 外 |
| 3 | β′ 単独: Opus の cut ≥ 8 | 7(r8 を含む)| 外 |
| 3 | β′ 単独: Sonnet ≤ 4 | 2 | 合 |
| 3 | (b)+E-full と単独の差 = null | Fable +0.05・Opus −0.20・Sonnet −0.10 | Fable 合・Opus 外(weak)・Sonnet 合 |
| 3 | 床は 20 | 20 × 6 | 合 |
| 3 | 焦点と準線の道が減る(Fable 20 → ≤ 12)| Fable E-full+Bbp 18 | 外 |
| §11 | B-diam ≤ 10(He / Hi)| 19 | 外 |
| §11 | D-fc v1 ≤ 5 | 4 | 合 |
| §11 | E-abs ≤ 3 | 0 | 合 |

**実行層**(PREREG §7)
| # | 予測 | 出た数 | |
|---|---|---|---|
| 1 | Sonnet 4.6 E-prem1 ≥ 12(19 以上は天井の恐れ)| 20(天井)| 合 |
| 1 | Sonnet 5.5 ≥ 16・Haiku 4.5 ≤ 8・Haiku 5.5 ≥ 10・差の差 ≤ +0.3 | 走らせていない | — |
| 2 | Haiku の埋めた割合 ≤ 0.3 | 0.44 | 外 |
| 2 | Sonnet 0.3〜0.7 | 0.11 | 外 |
| 3 | Bbp の cut: Fable ≥ 12・Opus ≥ 10・Sonnet ≥ 6 | 0・7・2 | 外・外・外 |
| 3 | E-full+Bbp と Bbp の差は null か weak | null・weak・null | 合 |
| 3 | 床は全部 18 以上 | 20 × 6 | 合 |
| 3 | 座標の形は Opus で増える | Opus のみ(Bbp 0 / 5・E-full+Bbp 5 / 6)| 合 |
| 4 | B の He / Hi ≥ 15 | 18 | 合 |
| 4 | B-diam ≥ 12 | 19 | 合 |
| 4 | D-fc v1 ≤ 8 | 4 | 合 |
| 4 | E-abs: bind ≥ 10 で He / Hi ≤ 5 | 20・0 | 合 |
| 5 | 段 2: Fable ≥ 16 | 20 | 合 |
| 5 | Opus 10〜16 | 8(境を段 1 に = 0)| 外 |
| 5 | Sonnet ≤ 5・Haiku 0 | 0・0 | 合・合 |
| 5 | KF@U で Fable ≤ 12 | 15 | 外 |
| 6 | 改稿率 0.5〜0.8 | 0.12・0.69・0.25 | R-quote2 のみ 合 |
| 6 | R-quote2 の最終 ≥ 10 | 5 | 外 |
| 6 | R-blindK の最終 ≥ 8 | 5 | 外 |

## §7 札からずれた事・開示
1. **経路の誤り(修理 `152f65dc`)**: 共通部の `run_units` が凍結の `RUN.vendor_of` を呼んでおらず、Sonnet 5.5・Haiku 5.5 が OpenAI の口へ行き HTTP 404(80 行・model に届いていない = 課金なし)。共通部に一行足して起動し直し、404 の行は `ConstructGap/exp/excluded_routing404_20261014/` へ移した。Opus・Sonnet 4.6・Haiku の R-off・kfv1・sol1 は影響なし(req_opts が前の札と同じことを確かめた)。凍結の file は変えていない。
2. **usage の読み**: `cards_common.usage` は Anthropic の key だけを読み、GPT-6 の費用の見張りが一走目・alt1・alt2 で働いていなかった。午後の共通部で両方の形を読むようにした(PREREG に開示済)。
   - **訂正(14 時台・RECORD 午後の受領 §3-2)**: 「一走目・alt1・alt2 の見張りが働いていなかった」は誤り。欠けの在る関数を import するのは 10-14 の札だけで、GPT を呼んだのは sol1(直した後に走らせた)だけ。一走目の見張りは両方の形を読んでいた・alt1 / alt2 の runner には見張りが無く、費用は両方の形を読む関数で事後に数えた。過去の RESULT の GPT の費用の数は全部一致した。
3. **eprem1 の門の先**: E-prem0 = 0 は規則の書いていない場合 → 止めた。走らせていない四つの腕は §1。
4. **gname2**: Haiku の text の無い単位 1 つを一回取り直した(規則どおり・`_p1r`)。
5. **attr1**: B-diam で "(or radius)" も抜いた(PREREG §4 に開示済)。
6. **kfv1 の読み**: 一人の読み(実行層)・model と腕を伏せた。T と G の境の印、「境(是)」の印は、読みの後に RECORD 昼 §4-2 の形に合わせて付けた(数が出た後の区分 = 記述)。Haiku 5.5 は KF だけ(PREREG どおり)。
7. **b5bp の r8**: 先生の裁定で cut に数えた(§3-1・述語で他に当たる物なし)。

## §8 していない事・先生の言葉が要る物
- eprem1 の続き(Sonnet 5.5 × E-prem1 / E-prem0・天井でも床でもない passage の文面)。
- 座標の形を cut に数えるか(昼の §4-1・r8 の裁定とは別の問い)。
- kfv1 の二人目の読み(境(是)10 本・境(T/G)10 本・RECORD 昼 §4-2 の 8 本と合わせて)。
- 判断層への諮問便(本 RESULT・SOURCE 二つ・RECORD 昼・前回 upload されなかった 13 点・REMAINING)= 一時フォルダは言われたら作る。
- open-weight(OLMo-3 base の driver が走っている・rh1 はその後に自動で起動)= 別便。
- **commit は未**(先生の「commit」を待つ)。

---

## 付-A・付-B(b5bp)
### 付-A cut の答えの全文(12 本・PREREG §3「cut の全文は集合に依らず」)

#### Sonnet 5.5・Bbp・r0(June の門 = FALSE-STRUCT)
- 読み取り器 v2 の CUT: `KPy = KPx·FK/FD` CUT; `KPy = FK²·VD/FD²` CUT
- conjecture: |EJ| = |K P_y| (segments EJ and K P_y have equal length)
- reason: I found this by computing from the given coordinates, not by a full proof. EJ² ≈ 128.71 and KP_y² ≈ 128.71, so the two lengths agree to the precision given (≈11.345). The segments are not parallel, so this is not a parallelogram relation.

The structure behind it is as follows. In the right triangle K P_x P_y (right angle at P_x), K P_y is parallel to j, so the angle at K equals the angle between line FK and j. That is the angle at F in the right triangle F D K, which is right-angled at D because e ⟂ j. Hence K P_y = K P_x · FK / FD. Since h1 ⟂ j at V, we also have FP_x/FK = FV/FD. Combining these gives K P_y = FK·(FK − FP_x)/FD = FK²·(1 − FV/FD)/FD = FK²·VD/FD². Here FK²/FD² = 1 + DK²/FD², and DK = FD·(P_xV/FV), so it equals 1 + (P_xV/FV)², which is the P_x-dependent factor.

The point J is built from P_y by the chain H (the foot of P_y on j), then the parallel to GE, then the tangent g. This chain is a similarity from the P_x-dependent segment K P_y onto EJ. The construction therefore sends the P_x-dependence on both sides to the same scale factor. That gives EJ = K P_y for every position of P_x on h1. I verified this only numerically at the given P_x.

#### Sonnet 5.5・Bbp・r15(June の門 = CLOSURE)
- 読み取り器 v2 の CUT: `KPy = KPx·FK/FD` CUT
- conjecture: EJ = K P_y (segments E–J and K–P_y have equal length)
- reason: Numerical check from the given coordinates: EJ = sqrt(4.4328² + 10.4431²) ≈ 11.345 and K P_y = sqrt(11.2604² + 1.3826²) ≈ 11.345. I have not derived a proof, so the following is only a sketch of why it should hold for every P_x. In right triangle K P_x P_y, the right angle is at P_x and the hypotenuse K P_y is parallel to j. If θ is the angle between ray F K and j, then K P_y = K P_x / cos θ. Since K lies on e, which is perpendicular to j at D, we have FK·cos θ = FD. So K P_y = K P_x · FK / FD, which is a relation among lengths of segments between the given points. On the other side, the chain P_y → H (parallel to h1, which is parallel to e) → J (parallel to chord GE, meeting tangent g) makes triangle H J E similar to a triangle built from F, D, K, P_y. This chain gives EJ the same length K P_x · FK / FD. The two segments are therefore equal for every position of P_x.

#### Opus 5.5・Bbp・r3(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `:JE = FPx²/FV` CUT; `KPy = FPx²/FV` CUT; `JE·FV = FPx²` CUT; `KPy·FV = FPx²` CUT; `JE = FPx²/FV` CUT
- conjecture: JE = KP_y (segment JE is always equal in length to segment KP_y)
- reason: Claim: JE = KP_y = FP_x^2/FV, i.e. JE·FV = KP_y·FV = FP_x^2 for every P_x on h1.
(1) GF is a diameter and j ∥ f, so j is the tangent at F. Then VF and VE are both tangents from V, so VF = VE. Since j ∥ CG and CG = CE, angle VDE = angle CGE = angle CEG = angle VED. Hence VD = VE = VF.
(2) Put F at the origin with j as the x-axis. Then e is x = d, h1 is x = v, and P_x = (v, t). K lies on line FP_x with x = d, so K = (d, dt/v). P_y lies on y = dt/v and on m: v(x - v) + t(y - t) = 0. This gives x(P_y) = v + t^2(v - d)/v^2. Because h1 ⊥ j, H is the foot of P_y on j. So KP_y = DH = DV(1 + VP_x^2/FV^2) = DV·FP_x^2/FV^2.
(3) HJ ∥ DE, so triangle VHJ is similar to triangle VDE. Therefore JE/HD = VE/VD = 1, so JE = DH.
Combining with VD = FV gives JE = KP_y = FP_x^2/FV. Numerically FP_x^2 ≈ 26.20, FV ≈ 2.309, and JE ≈ KP_y ≈ 11.345.

#### Opus 5.5・Bbp・r4(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `VH = VD·VPx²/VF²` CUT; `VJ = VE·VPx²/VF²` CUT
- conjecture: EJ = KP_y (the segments EJ and KP_y are always equal in length)
- reason: Key relation: EJ/VE = KP_y/VD = 1 + VP_x²/VF², and VE = VD.

1. Setup. GF is a diameter, so line j through F parallel to tangent f is the tangent to c at F. Then VF = VE, since both are tangent lengths from V.

2. Isosceles triangle. Since j ∥ f, angle(j, GE) = angle(f, GE). Since CG = CE, angle(f, GE) = angle(g, GE). So triangle VDE is isosceles and VD = VE = VF.

3. Coordinates. Take F as the origin and j as the x-axis. Then V = (v,0), D = (d,0), e is the line x = d, h1 is the line x = v, and P_x = (v,t). Here v = VF and t = VP_x.

4. Length KP_y. Line F→P_x meets e at K = (d, td/v). The perpendicular m at P_x meets the horizontal line through K at P_y = (v − t²(d−v)/v², td/v). Hence KP_y = |d−v|(1 + t²/v²) = VD(1 + VP_x²/VF²).

5. Length EJ. H is the foot of P_y on j, so VH = VD·VP_x²/VF², with H on the opposite side of V from D. Because HJ ∥ DE, triangles VHJ and VDE are similar, so VJ = VE·VP_x²/VF², with J on the opposite side of V from E. Therefore EJ = VE + VJ = VE(1 + VP_x²/VF²).

6. Conclusion. This gives the stated relation EJ/VE = KP_y/VD = 1 + VP_x²/VF², equivalently EJ·VD = KP_y·VE, for every P_x. Since VE = VD, it follows that EJ = KP_y.

Numeric check with the given coordinates: EJ ≈ 11.345 and KP_y ≈ 11.345.

#### Opus 5.5・Bbp・r6(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `KPy·FV = FPx²` CUT; `VH = VPx²/FV` CUT; `EJ·FV = FPx²` CUT
- conjecture: EJ = KP_y
- reason: Since FG is a diameter, j is the tangent at F. This makes e and h1 both perpendicular to j. V is the pole of FE, so VE = VF. Let a = FV and s = VP_x. Then FP_x^2 = a^2 + s^2, because P_x lies on h1, which is perpendicular to j at V. The polar of C through G and E meets j at D with VD = VF = a, so FD = 2a. Because e and h1 are parallel, K is the reflection-type double of P_x: FK = 2FP_x. So K is at height 2s above j, and P_y has that same height. In the right angle at P_x, the line P_xP_y is perpendicular to FP_x. Its direction (s, -a) runs s/a times the vertical rise s horizontally, so P_y sits horizontally VP_x^2/FV behind P_x. This gives KP_y = FV + VP_x^2/FV, i.e. KP_y·FV = FP_x^2. Next, H is the foot of P_y on j, so VH = VP_x^2/FV and H lies on the side of V opposite D. Since HJ is parallel to DE, the triangles VHJ and VDE are similar: VJ/VE = VH/VD. With VE = VD = FV this gives VJ = VH, and J lies on the opposite side of V from E. Therefore EJ = EV + VJ = FV + VP_x^2/FV. The key relation, valid for every P_x on h1, is EJ = KP_y = FV + VP_x^2/FV (equivalently EJ·FV = KP_y·FV = FP_x^2). This explains the equality. Numerically both lengths are about 11.345.

#### Opus 5.5・Bbp・r11(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `VPx² = VF·VH` CUT; `VJ = VPx²/VF` CUT; `VH = VPx²/VF` CUT
- conjecture: K P_y = E J (segment KP_y is always equal in length to segment EJ)
- reason: Use coordinates along j: s is measured from F along j, and t is measured perpendicular to j. These are a guided derivation plus a numerical check, not a full proof. (1) GF is a diameter, so j (parallel to f through F) is the tangent at F. V is then the meeting point of the tangents at E and F, so VE = VF; call this a. (2) GE is the polar of C, and D = GE ∩ j works out to the mirror point of F across V, so VD = VF = a. Triangle VDE is therefore isosceles with VD = VE = a. (3) Write P_x = (a, t0) on h1, where s = a. The ray F P_x meets e (at s = 2a) at K = (2a, 2t0). The perpendicular m at P_x gives P_y = (a − t0²/a, 2t0). So P_y has the same t as K, and H = (a − t0²/a, 0) has the same s as P_y. This gives VH = t0²/a, i.e. VP_x² = VF·VH, and K P_y = D H = DV + VH. (4) HJ is parallel to DE, and E, V, J lie on g while D, V, H lie on j. So triangles VDE and VHJ are similar, and VJ/VE = VH/VD, hence VJ = VH. Combining: E J = EV + VJ = DV + VH = DH = K P_y. The relation that holds for every P_x is therefore K P_y = DH = EV + VJ, with VJ = VH = VP_x²/VF = t0²/a. Numerical check: K P_y ≈ 11.345 and EJ ≈ 11.345.

#### Opus 5.5・Bbp・r16(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `FV·KPy = FPx²` CUT; `VH = VPx²/FV` CUT; `FV·EJ = FPx²` CUT; `EJ·FV = FPx²` CUT; `FPx² = KPy·FV` CUT
- conjecture: EJ = KP_y (segment E–J on the tangent g has the same length as segment K–P_y)
- reason: The numeric check works out: EJ ≈ 11.35 ≈ KP_y. The general argument follows. Since F is antipodal to G, j is the tangent at F. So V is the intersection of the tangents at F and E, which gives VF = VE. With A as origin and u the unit vector from G toward F, the radius is 4 and E·u = 2 here, so D divides GE with GD/GE = 4/3. Measured along j, V lies exactly midway between F and D, so VD = VF = VE. Line e is perpendicular to j at D and h1 is perpendicular to j at V, so the projection of P_x onto j is V. Hence FV is the leg of the right triangle F V P_x, and FP_x² = FV² + VP_x². K lies on e, which is twice as far from F (along j) as h1, so K is the point 2·P_x as seen from F. P_y lies on the line through K parallel to j, and P_xP_y ⟂ FP_x. Using this right angle, KP_y = FV + VP_x²/FV, that is FV·KP_y = FP_x². Also H is the foot of P_y on j, so VH = VP_x²/FV. Next, HJ ∥ GE = DE, so triangle VHJ is similar to triangle VDE. Because VD = VE, this gives VJ = VH. J and E lie on opposite sides of V on g, so EJ = VE + VJ = FV + VH = FV + VP_x²/FV. The relation that holds for every P_x on h1 is therefore FV·EJ = FV·KP_y = FP_x², i.e. EJ·FV = FP_x² = KP_y·FV. In particular EJ = KP_y.

#### Opus 5.5・Bbp・r19(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `EJ = FPx²/FV` CUT; `KPy = FPx²/FV` CUT; `EJ·FV = FPx²` CUT; `KPy·FV = FPx²` CUT; `VJ·VE = VPx²` CUT
- conjecture: EJ = KP_y (segment E–J is equal in length to segment K–P_y)
- reason: Use coordinates with F as the origin, j as the x-axis, and the normal to j as the y-axis.

1. Locate V and D. j is the tangent at F, because GF is a diameter and j is parallel to the tangent at G. So VF = VE, since both are tangent lengths from V. Angle GEF = 90°, since it is inscribed in a semicircle. Hence triangle FED has a right angle at E. V lies on FD and is equidistant from F and E, so V is the midpoint of FD. Write FV = VE = VD = a, so D = (2a, 0) and V = (a, 0).

2. Locate K and P_y. h1 and e are perpendicular to j, so P_x = (a, t). The ray from F through P_x meets e (the line x = 2a) at K = (2a, 2t). The line m is perpendicular to FP_x at P_x. Intersecting m with the line y = 2t through K gives P_y = (a − t²/a, 2t). Therefore KP_y = a + t²/a.

3. Locate J. H is the foot of P_y on j, so VH = t²/a. HJ is parallel to DE, so in triangle VDE we get VJ/VE = VH/VD. Hence VJ = t²/a, with J on line g on the opposite side of V from E. So EJ = EV + VJ = a + t²/a.

The length relation that holds for every P_x is EJ = KP_y = FP_x²/FV. Equivalently, EJ·FV = KP_y·FV = FP_x² = FV² + VP_x², which is the same as VJ·VE = VP_x². Hence EJ = KP_y.

#### Opus 5.5・E-full+Bbp・r1(June の門 = TRAP)
- 読み取り器 v2 の CUT: `VH = PyH²/(4·FV)` CUT
- conjecture: EJ = KP_y. Equivalently, EJ = P_yF: P_y runs on the parabola with focus F, vertex V and directrix e, and EJ equals the focal radius of P_y.
- reason: Use coordinates along j with F as origin. Let a = FV and R = AF. The circle is tangent to j at F, and V = g ∩ j. GE is parallel to AV, because both are perpendicular to FE. Hence D = (2a,0) and FD = 2a, so V is the midpoint of FD and FV = VD = a. Write P_x = (a,t). Then K = (2a, 2t), since K lies on e (u = 2a). The perpendicular m at P_x gives P_y = (a − t²/a, 2t). So with v = P_yH we get VH = v²/(4a), where H is the foot of P_y on j. This means P_y lies on the parabola with focus F and directrix e, so P_yF = P_yK. Now take the tangent line g. The tangent lengths from V are equal: VE = VF = a. HJ is parallel to GE, which is parallel to AV, the bisector of angle FVE. So triangle VHJ is isosceles with VJ = VH, and J lies on the opposite side of V from E. Hence EJ = EV + VJ = VD + VH = HD. P_yHDK is a rectangle, so HD = KP_y. The length relation, valid for every P_x, is EJ = EV + VJ = FV + VH = HD = KP_y = FP_y, with VH = P_yH²/(4·FV). Therefore EJ = KP_y.

#### Opus 5.5・E-full+Bbp・r6(June の門 = TRAP)
- 読み取り器 v2 の CUT: `FK² = 2·FD·KPy` CUT
- conjecture: EJ = P_yK. Equivalently, P_y is equidistant from F and from line e (P_yF = P_yK), and the segment EJ reproduces that common length on the tangent g.
- reason: 1) Setup. Line j is the tangent at F, because it is parallel to the tangent f at the antipode G. So V = g ∩ j is where the tangents at E and F meet, and VE = VF. Since GF is a diameter, angle GEF = 90°. D lies on line GE and on j, so triangle FED has a right angle at E. V lies on its hypotenuse FD with VF = VE, so V is the midpoint of FD. Hence VD = VE = VF = a, and FD = 2a.

2) Coordinates. Take F as origin and j as the x-axis. Then V = (a, 0), D = (2a, 0), h1 is x = a and e is x = 2a. Write P_x = (a, t). The ray FP_x meets e at K = (2a, 2t), so DK = 2t. Line m is a(x−a) + t(y−t) = 0. Meeting it with y = 2t gives P_y = (a − t²/a, 2t).

3) Parabola. It follows that KP_y = a + t²/a. This gives the length relation FK² = 2·FD·KP_y, which holds for every P_x. Also P_yF² = (a − t²/a)² + 4t² = (a + t²/a)², so P_yF = P_yK. Thus P_y runs on the parabola with focus F, vertex V and directrix e, and K is the foot of the perpendicular from P_y to e.

4) Transfer to EJ. H is the foot of P_y on j, so HD = KP_y. Line HJ is parallel to DE, so triangles VHJ and VDE are similar. Since VD = VE, this gives VH = VJ. H and D lie on opposite sides of V, and so do J and E. Therefore EJ = VE + VJ = VD + VH = HD = KP_y (= P_yF).

Numerical check: EJ ≈ 11.345 ≈ P_yK.

#### Opus 5.5・E-full+Bbp・r13(June の門 = GENUINE-CUT)
- 読み取り器 v2 の CUT: `VPx² = VF·VH` CUT
- conjecture: EJ = P_yK. Equivalently, P_y lies on the parabola with focus F, vertex V and directrix e, and EJ equals the focal radius P_yF.
- reason: Take j as the axis, with F at the origin. V = g∩j is where the tangents at F and E meet, so VF = VE =: a. The line j is the tangent at F, because F is antipodal to G and j is parallel to f. The point D = GE∩j satisfies VD = a, since D lies at distance 2a from F; this matches the coordinates (x_D = 4.619 = 2·x_V). Write P_x = (a, s). The ray F→P_x meets e (x = 2a) at K = (2a, 2s). The perpendicular m at P_x meets y = 2s at P_y = (a − s²/a, 2s). So P_y² satisfies y² = 4a(a − x): P_y lies on the parabola with focus F, vertex V and directrix e. Hence P_yK = P_yF = HD = HV + VD = s²/a + a. Here H is the foot of P_y on j, and VH = s²/a. This comes from the mean-proportional relation VP_x² = VF·VH, the right angle at P_x. Since HJ ∥ DE, triangles VHJ and VDE are similar, so VJ/VE = VH/VD. Because VE = VD, this gives VJ = VH, with J on the opposite side of V from E. Therefore EJ = EV + VJ = VD + VH = HD = P_yK. The explicit length relation is EJ = EV + VJ = VD + VH = P_yK (= P_yF), with VP_x² = VF·VH, for every P_x on h1. Numerically, EJ ≈ 11.345 and P_yK ≈ 11.346.

#### Fable 5.1・E-full+Bbp・r12(June の門 = CLOSURE)
- 読み取り器 v2 の CUT: `PyH² = 4·VF·VH` CUT
- conjecture: EJ = P_y K  (equivalently EJ = P_y K = P_y F for every position of P_x on h1)
- reason: The figure is the meridian section of a Dandelin diagram: f and g are two generators of a cone with apex C, c is the inscribed (Dandelin) sphere touching the generators at G, E, and j (the tangent to c at F, parallel to the generator f) is a cutting plane parallel to a generator, so the section is a parabola with focus F, vertex V = j∩g, axis j, and directrix e (the line where the plane of the contact circle GE meets the cutting plane, perpendicular to j at D). Because VF = VE = VD (tangent lengths from V to c, and V is the vertex, midway between focus and directrix), the line h1 through V perpendicular to the axis is the vertex tangent; for P_x on it the ray F P_x reaches e at K with F P_x = P_x K, so K is the reflection of F in the line m ⟂ F P_x at P_x, and m is a tangent of the parabola. P_y ∈ m with P_y K ∥ j (perpendicular to the directrix) therefore satisfies P_y F = P_y K = dist(P_y, e): P_y lies on the parabola and H is the foot of its ordinate on the axis. Revolving about the axis of the cone, the plane through H parallel to the contact circle (line HJ ∥ GE) cuts the cone in a circle through P_y and J; the generator through P_y meets the contact circle at a point T with P_y T = P_y F (two tangent lengths from P_y to the sphere), and all generator segments between the two parallel circles are equal, P_y T = EJ. Hence EJ = P_y F = P_y K. The same fact is Apollonius' symptom of the parabola, a product relation that holds for every P_x: P_y H^2 = HJ · HJ' where J' is the point of f on the line HJ, and HJ' is the constant VD + VF = 2·VF (since j ∥ f), i.e. P_y H^2 = 4·VF·VH with VF = VE = VD; the ordinate is the mean proportional between the abscissa VH and the latus rectum 4·VF, and EJ = EV + VJ = VF + VJ grows exactly so that EJ^2 = (VH + VF)^2 = P_y H^2 + (VH − VF)^2 = P_y F^2 = P_y K^2.

### 付-B June の門が GENUINE-CUT と言い、読み取り器 v2 が cut と読まなかった物(記述)

- Opus 5.5・Bbp・r8(**§3-1 で cut に数えた**): DEGENERATE = `△VHJ ∼ △VDE` SIM-DEGEN / ADDITIVE(抜粋)= `VF·EJ = VF²+VPx²` ADDITIVE; `VF·KPy = VF²+VPx²` ADDITIVE; `EJ = VF+VPx²/VF` ADDITIVE; `KPy = VF+VPx²/VF` ADDITIVE; `EJ = EV+VJ` ADDITIVE
- Opus 5.5・Bbp・r12: DEGENERATE = `JE/VE = DH/VD` DEGENERATE; `JE·VD = VE·DH` DEGENERATE; `JE·VD = VE·KPy` DEGENERATE; `JE = VE·KPy/VD` DEGENERATE
- Opus 5.5・E-full+Bbp・r5: DEGENERATE = `EJ·VD = DH·VE` DEGENERATE; `△VDE ∼ △VHJ` SIM-DEGEN
- Opus 5.5・E-full+Bbp・r12: DEGENERATE = `EJ/DH = VE/VD` DEGENERATE; `EJ·VD = DH·VE` DEGENERATE; `△VDE ∼ △VHJ` SIM-DEGEN
- Opus 5.5・E-full+Bbp・r18: DEGENERATE = `VJ/VE = VH/VD` DEGENERATE; `VJ·VD = VH·VE` DEGENERATE; `△VHJ ∼ △VDE` SIM-DEGEN
- Fable 5.1・Bbp・r1: DEGENERATE = `VJ/VE = VH/VD` DEGENERATE; `VJ·VD = VH·VE` DEGENERATE
- Fable 5.1・Bbp・r4: DEGENERATE = `EJ/DH = VE/VD` DEGENERATE; `EJ·VD = DH·VE` DEGENERATE; `△VJH ∼ △VED` SIM-DEGEN
- Fable 5.1・Bbp・r9: DEGENERATE = `EJ/DH = VE/VD` DEGENERATE; `EJ·VD = DH·VE` DEGENERATE; `EJ·VD = KPy·VE` DEGENERATE
- Fable 5.1・Bbp・r10: DEGENERATE = `VJ·VD = VH·VE` DEGENERATE; `VJ/VE = VH/VD` DEGENERATE
- Fable 5.1・Bbp・r19: DEGENERATE = `:VJ/VE = VH/VD` DEGENERATE; `EJ/DH = VE/VD` DEGENERATE; `EJ·VD = DH·VE` DEGENERATE
- Fable 5.1・E-full+Bbp・r3: DEGENERATE = `HD:VD = JE:VE` DEGENERATE; `JE = HD·VE/VD` DEGENERATE; `JE·VD = HD·VE` DEGENERATE; `△VHJ ∼ △VDE` SIM-DEGEN
