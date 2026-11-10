# RESULT: 小札 `essay4` —— エッセイを読ませてから問う腕を、moy-1・moy-2・moy-5 の三項目に同時にかけた(Claude 5.5 系の 4 tier・n = 20・2026-10-14 水 08:36〜09:12・zebrashark)

> **札**: [PREREG](PREREG_essay_reading_three_items_moy1_moy2_moy5_20261014.md)(凍結 = commit `2189bc95`・local)。
> **先生(10-14 08:16・逐語)**: 「やっぱりgpt-5はトークンを喰いますね。Anthropicはクーポンで使えるので、moy-2とmoy-5をmoy-1と同時に巻末問題にかけてみてください。moy-5はFableでもbindしなかったので新鮮味あり。」
> **先生(同 08:20 ごろ・逐語)**: 「夏休みエッセイはmoy-5も解説しています。」
> **HEAD**(`R1`・fetch の後): `2189bc95`(local・origin/main より 9 つ先)+ 作業樹。
> **身分**: 数は実出力から。読みは札 §5 のとおり。**判定と講評は先生。** 名乗れるのは「この四つの model・この三項目・このエッセイ・座標のみの prompt」まで。
> **記録**: `ConstructGap/exp/results_essay4_<項目>_20261014_<model>_<part>.jsonl`・usage = `exp/logs/essay4_<項目>_20261014_<model>_<part>_sidelog.jsonl`・集計 = `exp/essay_items_20261014.py --read` と `exp/report_essay4_20261014.py`(後者は凍結の外・記述用)。

## §1. 取れた物
- 720 単位のうち **text の在る単位 717**。無いのは Haiku 5.5 の moy-5 の 3 本(A 1・E-full 2)で、どれも thinking が出力の上限 12,000 token に達して本文が出なかった(`stop_reason = max_tokens`)。Haiku の moy-5 は一回目で 18 本が同じ形で落ち、取り直しの通しで 15 本が取れた。ほかの三つの model は一回目で全部取れた。
- API の error 0・refusal 0。**見張りは一度も作動していない。**
- 費用(side log を単価で見積もり)= **$54.48**(Haiku $0.71・Sonnet $5.63・Opus $12.28・Fable $35.85)。札の見積もりは $64。10-13 からの記録上の合計は $100.88。

## §2. 表

### 2-1. moy-1(`higashida_circle`・bind = 凍結の `classify`)

| model | A | B(封鎖の一文)| E-abs | E-full | 計器 | thinking の中央値 A → E-full |
|---|---|---|---|---|---|---|
| Haiku 5.5 | 6 | 20 | **20** | **20** | 立つ | 1,620 → 678 |
| Sonnet 5.5 | 0 | 20 | **20** | **20** | 立つ | 837 → 294 |
| Opus 5.5 | 20 | 20 | 20 | 20 | 立つ | 328 → 241 |
| Fable 5.1 | 20 | 20 | 20 | 20 | 立つ | 549 → 369 |

- 三値: Haiku +0.70 strong・Sonnet +1.00 strong(E-abs・E-full とも)。Opus と Fable は A が 20 で、差は 0(null)。
- essay1(10-13・同じ byte)の数 = Haiku A 2・Sonnet A 2・読ませた腕は 20。今日の Haiku の A は 6。

### 2-2. moy-2(`higashida_axis`・bind = 凍結の `closure_higashida_axis`)

| model | A | E-abs | E-full | 答えの欄に「垂線の足が中点」の形が在る本数 A → E-abs → E-full | 答えの長さの中央値(字)A → E-full |
|---|---|---|---|---|---|
| Haiku 5.5 | 20 | 20 | 20 | 3 → 7 → 14 | 104 → 174 |
| Sonnet 5.5 | 20 | 20 | 20 | 5 → 20 → 20 | 140 → 210 |
| Opus 5.5 | 20 | 20 | 20 | 4 → 10 → 17 | 119 → 180 |
| Fable 5.1 | 20 | 20 | 20 | 11 → 13 → 19 | 163 → 219 |

- 12 の cell が全部 20 / 20。差は全部 0(null)。統制の項目は統制のまま。
- 「足が中点」の形は、凍結の採点が bind に数えない形だが、**この形を含む答えは全部 bind**(「足の形で、bind でない」は 0 本)= 等距離か垂直二等分線の言明に「Equivalently, the foot of the perpendicular from O3 to l1 is the midpoint of TcTh」を足す書き方(Sonnet と Fable の各 9 本を目視)。
- この形は **要旨だけの腕でも増える**(Sonnet 5 → 20)。要旨は moy-2 に触れていないので、§4 の中身に帰属はできない。読ませた腕では答えが長くなる。

### 2-3. moy-5(`parabola_section`・bind = この札の読み取り器の cut)

| model | 腕 | n | **cut** | 床 \|EJ\| = \|KPy\| | 理由が焦点・準線の道(凍結の route `TRAP-FOCDIR`)| Dandelin の円錐の議論で EJ を説明 | 放物線を座標で書く | thinking の中央値 |
|---|---|---|---|---|---|---|---|---|
| Haiku 5.5 | A | 19 | **0** | 19 | 0 | 0 | 1 | 4,121 |
| | K | 20 | 20 | 7 | 0 | 0 | 0 | 4,333 |
| | E-abs | 20 | **0** | 19 | 1 | 0 | 0 | 6,204 |
| | E-full | 18 | **0** | **13** | 7 | 0 | 2 | 8,233 |
| | E-full2 | 20 | **0** | 18 | 1 | 0 | 2 | 6,537 |
| Sonnet 5.5 | A | 20 | **0** | 20 | 0 | 0 | 0 | 431 |
| | K | 20 | 20 | 20 | 0 | 0 | 0 | 1,625 |
| | E-abs | 20 | **0** | 19 | 1 | 0 | 0 | 846 |
| | E-full | 20 | **0** | 20 | 14 | 0(語だけ 7)| 0 | 1,522 |
| | E-full2 | 20 | **0** | 20 | 11 | 0(語だけ 7)| 1 | 772 |
| Opus 5.5 | A | 20 | **0** | 20 | 5 | 0 | 1 | 1,331 |
| | K | 20 | 20 | 20 | 1 | 0 | 1 | 1,797 |
| | E-abs | 20 | **0** | 20 | 5 | 0 | 10 | 1,351 |
| | E-full | 20 | **0** | 20 | 16 | 3 | 7 | 2,282 |
| | E-full2 | 20 | **0** | 20 | 18 | 3 | 10 | 2,583 |
| Fable 5.1 | A | 20 | **0** | 20 | 0 | 0 | 0 | 1,359 |
| | K | 20 | 19 | 20 | 0 | 0 | 0 | 2,509 |
| | E-abs | 20 | **0** | 20 | 18 | 0 | 9 | 3,356 |
| | E-full | 20 | **0** | 20 | 20 | **12** | 0 | 3,367 |
| | E-full2 | 20 | **0** | 20 | 20 | **11** | 0 | 2,683 |

- **計器**: K は 20・20・20・19 で、四つとも立つ(≥ 16)。
- **cut は、K を除く 16 の cell の全部で 0**(text の在る 317 本のうち 0 本)。差は全部 0(null)。(K − A)の半分を埋めた腕は無い。
- 「Dandelin の円錐の議論」と「放物線を座標で書く」の二列は、走らせた後に置いた記述の述語(札に無い・§4-3 と §4-4)。

## §3. 規則が言うこと(機械の読み)
- **moy-1**: Haiku と Sonnet は読ませた腕が strong。Opus と Fable は天井どうしで null(下がらない)。
- **moy-2**: 全部 null。A が四つとも 20 で、統制は立っている。
- **moy-5**: 計器が四つとも立った上で、**読ませた腕は 12 の cell の全部で null**。要旨だけ・全文・二往復のどれでも、四つの tier のどれでも、cut は 0。

## §4. 記述(moy-5)

### 4-1. 読ませた腕で動いたのは理由の欄の道筋
- 理由の欄が「Py は焦点 F・準線 e の放物線に載る → PyF = PyK」を使う答え(凍結の route = `TRAP-FOCDIR`)は、A で 0・0・5・0(Haiku・Sonnet・Opus・Fable)、**全文を読ませた腕で 7 / 18・14・16・20**。Fable は要旨だけで 18。
- parabola・focus・directrix の語が理由の欄に在る本数も同じ向き(Fable: A 0 → E-abs 18 → E-full 20)。
- 読ませた腕の理由の典型(Fable E-full r1 など・複数): (1) V が FD の中点 → h1 が F と e の中線 → Px が FK の中点 → m が FK の垂直二等分線 → PyF = PyK。(2) PyKDH が長方形 → KPy = HD。(3) HJ ∥ DE で △VHJ ∼ △VDE・VD = VE → EJ = HD。**伏せた不変量 \|EJ\| = \|KPy\| の証明として閉じていて、二次の関係を一度も使わない。**

### 4-2. Haiku では答えの欄そのものが動いた
- Haiku の E-full は床が 13 / 18。床を外した 5 本の答えの欄は全部 **「\|PyF\| = \|PyK\|・Py は焦点 F・準線 e の放物線に載る」**(同じ形が E-abs に 1 本・E-full2 に 1 本・A には 0 本。E-full2 のもう 1 本は答えの欄が空)。問いが指す {E, J, K, Py} の関係から、エッセイが名指す性質の方へ答えが移った。ほかの三つの model の床は 19〜20 のまま。
- (K の腕の Haiku の床 7 は別の事情 = 渡した関係 `FPx^2 = FV·FPy` をそのまま答えの欄に書いた答えが 13 本。)

### 4-3. Fable と Opus は、エッセイの Dandelin の読みを、エッセイに無い線分へ当てた
- 「Dandelin」の語は A・K・E-abs では四つの model とも 0 本。全文を読ませた二つの腕で Sonnet 7・7 / Opus 5・4 / Fable 13・13。
- そのうち **円錐の語(generator・contact circle・sphere・meridian・parallel circle)を伴い、EJ を「母線の上の、接触円から Py の高さの平行円までの区間 = 球への接線の長さ = 焦点距離」と説明する答え**は **Fable 12 / 20 と 11 / 20・Opus 3 / 20 と 3 / 20**・Sonnet と Haiku は 0(Sonnet は語だけ)。述語 = Dandelin の語 ∧ 円錐の語 ∧ 一文の中に(generator または tangent length)と EJ。本数は述語で数えた。全文を読んだのは Fable 2 本と Opus 1 本・Opus の残り 5 本は該当の文だけを読んだ。
- 逐語(Fable E-full r0):
  > … so P_y lies on the parabola with focus F, directrix e, vertex V, axis j (the Dandelin section of the cone with generators f, g and inscribed sphere c cut by the line j ∥ f). H is the axial projection of P_y, and the line through H parallel to the contact chord GE is the plane of the parallel circle of the cone through the conic point; it meets the generator g at J. In Dandelin's argument the tangent length from the conic point to the sphere equals the focal distance, and along the generator that tangent length is the segment between the parallel circle and the contact circle, i.e. |J E|. Hence |J E| = |P_y F| = |P_y K| for every P_x on h1 …
- エッセイの §11 は「the blue circle is the meridian section of a sphere inscribed in the resulting cone; tilt the cutting line parallel to a generator and the section is a parabola」と書くが、**E も J も、EJ が母線の区間であることも書いていない**。この議論は A の腕には 1 本も無い。
- 実行層の検算(`L2`・1 本を追った): 議論は成り立つ(子午面で、Py の高さの平行円の跡は H を通り GE に平行な線・それが母線 g と交わる点が J・円錐の上の点から球への接線の長さは母線に沿って接触円までの距離に等しい)。数値でも \|EJ\| = \|PyF\| = \|KPy\| は六つの配置で一致。

### 4-4. 要旨だけの腕では、Opus と Fable が放物線を座標で書いた
- 放物線を座標の式か媒介表示で書いた答え(`y² = −4v(x − v)`・`P_y = (a − t²/a, 2t)` の類)は、A で 0〜1 本、**E-abs で Opus 10・Fable 9**、E-full で Opus 7・**Fable 0**、E-full2 で Opus 10・Fable 0。
- `y² = 4a(a − x)` は、F を原点・j を軸に取れば `HPy² = 4·FV·VH`(Menaechmus の symptoma)と同じ関係だが、**問いの線分では書かれていない**(座標の変数 a・x・y・t のまま)。読み取り器は線分の式しか読まないので cut に入れていない。家の route の段では Descartes の道に当たる(凍結の `route_parabola` は準線の語が先に立つので `TRAP-FOCDIR` と出す)。
- Fable は、要旨だけだと座標(9 / 20)、全文だと座標 0 で Dandelin の議論(12 / 20)。

### 4-5. 比例中項の語は出たが、関係は出なかった(reason-read)
- 比例中項・相似・ordinate などの語が在って読み取り器が cut を読まなかった答え **71 本を、腕の名を伏せて並べ替えた一覧で全部読んだ**。
- **K の腕の 1 本を除き、問いの線分で正しい比例中項(二次の関係)を述べた答えは 0 本。**
- 「mean proportional」「geometric mean」の語を含む答えは 7 本(Sonnet E-abs 2・Opus E-abs 3・Opus E-full 2)。どれも語だけ、または当て推量:
  - 「The equality probably expresses the mean-proportional (Newton-type) relation of the figure.」(Sonnet E-abs r13)
  - 「… makes |KP_y| a mean proportional of two fixed segments, which is the parabola relation 'ordinate squared equals product'.」(Opus E-full r15。KPy は Px とともに動くので、二つの固定の線分の比例中項ではない)
  - 「I would expect it to come from the mean-proportional (ordinate² = product of segments) structure of the construction … but this is a conjecture.」(Opus E-full r6。同じ答えが「this is the Dandelin/parabola construction of the essay's Figure 11」と書く)
  - 「So P_y traces a parabola with axis along j, which is the Menaechmus-type mean-proportional construction.」(Opus E-abs r10・座標の導出の後に名だけ)
- 残りの 63 本は、△VHJ ∼ △VDE(相似拡大・読み取り器の `SIM-DEGEN`)で \|EJ\| = HD を運ぶ議論か、`squared length`・`abscissa`・`proportional` の語が当たっただけの答え。

### 4-6. thinking の量は、moy-1 と逆の向きに動いた
- moy-1 は読ませると減る(§2-1)。**moy-5 は読ませると増える**: A → E-full の中央値 = Haiku 4,121 → 8,233・Sonnet 431 → 1,522・Opus 1,331 → 2,282・Fable 1,359 → 3,367。
- Sonnet は腕によらず「numerically, not proved」の類の断りを 17〜20 / 20 で書く。Fable は 0。

## §5. 計器について(`R6`)

### 5-1. 凍結の門(2026-06-24)がこの札の実出力で見せた外れ
- **偽の「偽」**: 門の `FALSE-STRUCT` は 12 本。**12 本とも、真の関係 `EJ = VE·HD/VD` の類(相似拡大の比)を `/` の手前で切って `EJ = VE·HD` と読んだもの**(Fable 8・Opus 3・Haiku 1)。偽の二次式を書いた答えではない。読み取り器は同じ式を `DEGENERATE` と読む。
- **偽陰性**: K の腕で門が GENUINE としたのは 20・20・20・18。Fable の 2 本を落としている。
- 走らせる前に確かめた二つ(係数・比・相似を読めない / 等長から出る式を GENUINE に入れる)は、この札の A と E の腕には該当する答えが出なかった(cut が 0 なので)。

### 5-2. この札の読み取り器の外れ(凍結の後に判明・1 本)
- Fable K r17 = 「… this gives the mean-proportional relation FP_x^2 = FV·FP_y (FP_x = FK/2, FV = FD/2, and FK^2 = …」。**式の直後に、それ自身が `=` を含む括弧書きが続くと、辺 `FV·FPy(FPx` が式として読めず、手前の関係を落とす。** K が 19 なのはこの 1 本。
- 直した読み取り器(括弧書きで連鎖を切る + `a = b = c` を `a = c` としても読む・`report_essay4_20261014.py` の `relations_v2`・較正の一覧は 68 / 68 のまま)を 397 本の全部に当てた結果: **変わるのは Fable K r17 の 1 本だけ**(K 19 → 20)。**A と E の 16 の cell は 0 のまま。**
- 表の数は凍結した読み取り器のもの。

### 5-3. 記述用の正規表現の欠陥(採点には無関係)
- runner の語の検出 `ordinate` と reason-read の旗 `to_read` が「co**ordinate**」に当たっていた(語境界なし)。旗が立った答えは 223 本になった。**reason-read の一覧は raw から `\bordinate` で作り直した 71 本**で行った。語の列も作り直した値。bind・床・門・route には関係しない。

## §6. 予測との対応(数を並べるだけ・当否は先生)

| # | 実行層の見立て(`L3`・走らせる前)| 数 |
|---|---|---|
| 1 | moy-2: A は四つとも 18 以上・読ませた腕は null・E-full で「足が中点」の形が増える model がある | A 20・20・20・20 / 全部 null / 四つとも増えた(+11・+15・+13・+8)。ただし要旨だけでも増える |
| 2 | moy-1: Haiku と Sonnet は essay1 の再現(A ≤ 5・B = 20・E ≥ 18)・Opus と Fable は A ≥ 18 のまま | Sonnet A 0・Haiku A **6**(5 を 1 本超えた)・B と E は全部 20 / Opus・Fable は全部 20 |
| 3 | moy-5 の A: 床 ≥ 18・cut 0〜1 | 床 19(/ 19)・20・20・20 / cut 0・0・0・0 |
| 4 | moy-5 の K: cut ≥ 18 | 20・20・20・19 |
| 5 | moy-5 の E-abs: cut ≤ 2・語は出る(どれかで 5 本以上)| cut 0・0・0・0 / Menaechmus の語 = Opus 5・Sonnet 2 |
| 6 | **moy-5 の E-full: cut は四つとも 3 以下(壁のまま)・動くのは語彙と門の WORD-CUT** | cut **0・0・0・0** / 語彙は動いた(§4-1)/ WORD-CUT は Opus 3 だけ |
| 7 | E-full2 は E-full と 3 本以内 | 差 0 |
| 8 | thinking は moy-5 でも読ませた方が少ない | **外れ**(四つとも読ませた方が多い・1.7〜3.5 倍)|

- 見立てに無かったもの: Fable と Opus が Dandelin の議論を EJ に当てたこと(§4-3)・Haiku の答えの欄が焦点・準線へ移ったこと(§4-2)・要旨だけで Opus と Fable が座標に出たこと(§4-4)。

## §7. 言えること・言えないこと
- 言える: この四つの model は、エッセイを読んだ後、moy-5 の伏せた不変量を(Haiku を除き)20 / 20 で述べ、理由の欄はエッセイの語彙(放物線・焦点・準線・Dandelin)へ移った。Fable の 55〜60 % と Opus の 15 % は、エッセイが書いていない線分 EJ に Dandelin の読みを当てて等式を説明した。**比例中項(家の言う cut)を問いの線分で書いた答えは、317 本の中に 1 本も無い。**
- 言えない: (a) エッセイの図と問いは字を共有している(A・C・G・F・V・Px・Py)。字を替えた腕は取っていない = Dandelin の当てはめが字の一致に支えられているかは分からない。(b) 「cut が出ない」は「理由を閉じるのに cut が要らない」と区別できない(§4-1 の証明は二次の関係なしに閉じる)。問いが {E, J, K, Py} の等長を指す限り、cut を書く動機が無い。(c) Dandelin の議論の本数は語と一文の述語で数えた。全文を読んだのは 3 本。(d) n = 20・一つのエッセイ・座標のみの prompt。

## §8. していないこと
字を替えた腕(sym1 の形)を moy-5 で。focus を {Px, V, F} に替えた問い(6 月の `A1_construct`)にエッセイを足す腕。4.x の世代と OpenAI の model。図を渡す腕。Dandelin の議論 29 本のうち残り 26 本の全文の読み。判断層への便。commit(記録の file は作業樹に在る)。

**宇宙タグ**(`R5-a`): 2026-10-14 水 09 時台・zebrashark・HEAD `2189bc95` + 作業樹。

## §9. 追記(10-14 10 時台・判断層の返しを受けた読み直し・数の訂正 1 件)
- **訂正**: §2-3 の表と §4-3 の「Fable 5.1・E-full・Dandelin の円錐で EJ を説明 = 12」は、**全文の読みで 11**。朝の数は正規表現で数えた物で、1 本(r18)は「unfolded Dandelin picture」と書いた上で相似の二等辺三角形で運ぶ議論だった。E-full2 の 11・Opus の 3 と 3 は読みでも同じ。読んだ範囲は 57 本(Dandelin の語・判断層の述語 v0・朝の正規表現のどれかが拾った答え・腕の名を伏せて)で、読みで是は 28 本。全文と読み = [SOURCE](SOURCE_moy5_frame_apply_57_answers_with_reading_labels_20261014.md)。
- **読み取り器 v2**(直し二つ・`exp/moy5_relation_reader_v2_20261014.py`): 較正 70 / 70・この札の 397 本で変わるのは Fable K r17 の 1 本だけ(K 19 → 20)・過去の 515 本は cut 0。**この札の表は v1 の数のまま。**
- 6 月の `A1_construct` の実出力(Opus n = 10 ほか)を読み取り器で読み直した結果は cut 0。
- 詳細 = [RECORD](RECORD_adjudication_receipt_verification_moy1_second_lap_and_three_items_20261014.md) §4。
