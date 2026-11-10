# PREREG(午後の六つの小札): `eprem1`・`gname2`・`b5bp`・`attr1`・`kfv1`・`sol1` —— 判断層の返し(昼)の順 1〜6 のうち API で走る物

- 日付: 2026-10-14(水)午後 / 実行層 = Opus 5.5 xhigh(zebrashark)。走らせる前に書き、local の commit で凍結する(push しない)。
- 先生(逐語): 「APIで走らせられるものは走らせましょう。」(前段 = [REMAINING](REMAINING_items_runs_and_new_cards_excluding_open_weight_20261014.md) §1 の表)。
- 返し(昼)の先生スロットのうち、この言葉で走らせる側に置いた物: (b) moy-5 (b) は版 β′ / (c) 「枠の運び」を測り物に(K-frame を hint v1 で)/ (d) H_ctx を E-prem1 で。**名と登記の採否は先生のまま**(走らせた数は先生の判断の材料)。
- 判定と講評は先生。三値は札の規則のまま(|d| ≤ 0.1 null・≥ 0.5 strong・間は weak・n = 20 の記述)。
- 共通の作り(`ConstructGap/exp/pm_cards_common_20261014.py`・md5 `08034159…`): 凍結の部品だけを import し、凍結の file は一行も変えない。text の在る単位は取り直さず、text の無い単位は一回だけ取り直す。model ごとの費用の上限で止まる(side log の見積もり・**OpenAI の usage の形も読むように直した**: cards_common の `usage` は Anthropic の key だけを読み、GPT-6 では 0 と数えていた = 一走目と alt1・alt2 の GPT-6 の見張りは働いていなかった)。

## §1 `eprem1`(順 1・H_ctx)—— 答えの文を抜いた前提だけの passage
- 文面: 返し §7-2 の指定どおりエッセイの text から byte のまま切った。**E-prem1** = §1 の段落 1(答えの文の前で切る)+ 直角の補題(613 字・md5 `1d0b7f55…`)/ **E-prem0** = 段落 1 だけ(`92d6085f…`)。級の門 = 二つとも pointer。枠 = essay1 の `FRAME`、問い = 凍結の open の A(moy-1)。prompt md5 = E-prem1 `9df5cd4b…`・E-prem0 `a8774850…`。
- 注: 段落 1 は相似の中心(Sex・Sin = 問いの He・Hi と同じ点・名は違う)を名指す文を含む(切り方の指定どおり残した)。
- **門**: Sonnet 4.6 × E-prem1(n 20)。2 ≤ bind ≤ 18 → 開: Sonnet 5.5・Haiku 4.5・Haiku 5.5 × E-prem1。≥ 19 → Sonnet 4.6 × E-prem0 で門をやり直す(開けば三つも E-prem0)。≤ 1 → Sonnet 5.5 × E-prem1 だけ。
- 基線 A・B: 同じ凍結の prompt の既存の記録(4.x = essay2・5.5 = 今日の run2 / alt3 と essay1)。読み = 返し §7-2: Δ = (E-prem1 − A)_5.5 − (E-prem1 − A)_4.6・三値・両側・同定∨を隣に・thinking の中央値を併記。
- runner = `exp/eprem1_premises_passage_moy1_20261014.py`(`a2c51ad0…`)。上限: Sonnet 4.6 $3・Sonnet 5.5 $3・Haiku 4.5 $2・Haiku 5.5 $0.5。

## §2 `gname2`(順 2・位置の効果)—— 名の条項を問いの末尾の注記に
- 文面: alt3 の Q-name2 の名の条項(逐語)から、退けの一文("Your conjecture mentions an object that you have not named.")と言い直しの指示を抜き、`\nNote: name every object …` として凍結の A の末尾に置く(返し §8-2 の案の書き出しどおり)。注記の md5 `fc865c8a…`・prompt `80dfc73b…`。漏れの検査(alt1 の `LEAK`)= 通る。
- Haiku 5.5・Sonnet 5.5・n 20。基線 = run2 の A・B(同じ日・同じ凍結の prompt)。読み = 埋めた割合 (bind − A) / (B − A)・三点の円・答えの欄の行き先。
- runner = `exp/gname2_name_clause_note_moy1_20261014.py`(`42db9fd1…`)。上限: Haiku $0.5・Sonnet $2。

## §3 `b5bp`(順 3)—— moy-5 (b) 版 β′
- 文面(返し §6 の逐語): `In the reason field, explain WHY the equality you stated holds, by a relation among lengths of segments between the given points that holds for every position of P_x and is not merely an equality of two lengths. State that relation explicitly, in the given symbols.`(md5 `7c32fd1d…`・"mean proportional"・"square"・"product"・"parabola" を含まない)。
- 腕: **Bbp** = 凍結の moy-5 の open + β′(`be9c4007…`)/ **E-full+Bbp** = essay1 の FRAME + 全文 + open + β′(`8c875982…`)。Sonnet 5.5・Opus 5.5・Fable 5.1(Fable は他の二つの後に起動)・n 20。
- 採点 = sym5 と同じ(読み取り器 v2 を「conjecture || reason」に当てた cut・凍結の床と道)+ 答えの欄だけの cut の列・E-full 型の腕の FRAME-APPLY v1(= v1c)・座標の形の列(記述)。基線 = essay4 の A・E-full(同じ model・同じ日)。cut の全文は集合に依らず RESULT に。
- runner = `exp/b5bp_moy5_blocking_beta_prime_20261014.py`(`58bf4c46…`)。上限: Sonnet $3・Opus $6・Fable $16。

## §4 `attr1`(順 5)—— attractor-state の札(返し §11 の草を札に)
- Haiku 5.5・thinking を止めて(一走目の R-off の経路 `_anthropic_off`)・n 20。腕: A・B(凍結)/ **B-diam** = B の block から "which known point is its center, and" と "(or radius)" を抜き "which segment is its diameter?" だけ(`71e12a42…`・"center" と "radius" の語 0)/ **D-fc@v1**(run2 と同じ置き方・`97bd6ea1…`)/ **E-abs**(要旨 + A・`b2a03d42…`)。
- 読み: 答えの欄の He / Hi(roff2 の凍結の正規表現)・bind・同定∨。
- 注: "(or radius)" も抜いた(返しの「which segment is its diameter だけ」を半径の語にも当てた・実行層の読み)。
- runner = `exp/attr1_attractor_state_roff_haiku55_20261014.py`(`929ea472…`)。上限 $0.5。

## §5 `kfv1`(順 6)—— K-frame を hint v1 で(「枠の運び」)
- 文面(返し §4-4 の逐語): `Hint: read the figure as the meridian section of a cone with apex C; the circle c is the section of a sphere inscribed in the cone, and g is a generator. E is where g meets the contact circle of the sphere; the parallel circle of the cone at the height of P_y meets g at J. Explain |EJ| = |KP_y| using the sphere.` 字替えの版は sym5 の写像(C → U・P_y → W_y)。prompt md5 = KF `c5435951…`・KF@U `cc472298…`。
- 凍結の sym5 の runner をそのまま呼ぶ(札の名・hint・腕の一覧を外から差す)。Sonnet 5.5・Opus 5.5・Fable 5.1 × {KF, KF@U}・Haiku 5.5 × KF・n 20。
- 読み = 返し §3-2 の梯子(段 0 言い直し / 段 1 接線の長さ(旗: 準線へ・焦点の取り違え)/ 段 2 焦点)を、model と腕を伏せて手で読む。sym5 の K-frame(古い hint)と並べる。
- runner = `exp/kfv1_kframe_hint_v1_20261014.py`(`f7053cec…`)。上限: Haiku $0.5・Sonnet $2・Opus $4・Fable $10。

## §6 `sol1`(順 4・OpenAI)—— 答えの後の介入を GPT-6 Sol で
- 凍結の alt3 の runner をそのまま呼ぶ(札の名・model・上限を外から差す)。腕: A・B → 同じ一回目の答えから R-re2・R-quote2・R-blindK。n 20。
- 読み = alt3 と同じ(一回目 → 最終・改稿率・埋めた割合・検定形 (2) の前件)。
- runner = `exp/sol1_after_answer_gpt6_sol_20261014.py`(`51354a3f…`)。上限 $8(朝の残高 $12.28)。単価 = ROSTER の $2 / $10。

## §7 予測(走らせる前)
**判断層**(返し 昼 §13・§11 の逐語の要約): 1 = E-prem1: Sonnet 4.6 は 6〜14 / 20(門は開く)・Sonnet 5.5 ≥ 16・差の差 ≥ +0.3・Haiku 4.5 ≤ 4・Haiku 5.5 ≥ 12 / 2 = G-name2: Haiku の埋めた割合 ≤ 0.2・Sonnet 0.3〜0.5 / 3 = β′: 単独で Fable・Opus の cut ≥ 8 / 20・Sonnet ≤ 4・(b)+E-full は単独と null の差・床は 20・焦点と準線の道が減る(Fable 20 → ≤ 12)/ §11 = attractor: B 20 → B-diam ≤ 10・D-fc v1 ≤ 5・E-abs ≤ 3(He / Hi)。
**実行層**(`L3`・当否は数を並べるだけ)
1. eprem1: Sonnet 4.6 の E-prem1 は 12 以上(19 以上 = 天井で E-prem0 に回る恐れ)。Sonnet 5.5 ≥ 16。Haiku 4.5 ≤ 8・Haiku 5.5 ≥ 10。差の差は ≤ +0.3。
2. gname2: Haiku の埋めた割合 ≤ 0.3・Sonnet 0.3〜0.7。
3. b5bp: Bbp の cut = Fable ≥ 12・Opus ≥ 10・Sonnet ≥ 6。E-full+Bbp と Bbp の差は null か weak。床は全部 18 以上。座標の形の答えは Opus で増える。
4. attr1: B の He / Hi ≥ 15(roff2 は 20 / 20)・**B-diam ≥ 12**(判断層と逆: 「中心」の語より He–Hi を直径に取る形が引く)・D-fc v1 ≤ 8・E-abs は bind ≥ 10 で He / Hi ≤ 5。
5. kfv1: 段 2 = Fable ≥ 16・Opus 10〜16(古い hint の 9 から上がる)・Sonnet ≤ 5・Haiku 0。字替え(KF@U)では Fable が 12 以下。
6. sol1: 改稿率 0.5〜0.8・R-quote2 の最終 ≥ 10・R-blindK の最終 ≥ 8。

## §8 費用
| 札 | 見積もり | 上限の和 |
|---|---|---|
| eprem1 | ≈ $4 | $8.5 |
| gname2 | ≈ $1 | $2.5 |
| b5bp | ≈ $16 | $25 |
| attr1 | ≈ $0.3 | $0.5 |
| kfv1 | ≈ $7 | $16.5 |
| **Anthropic 計** | **≈ $28** | **$53**(上限までの残り $65.37 の内)|
| sol1(OpenAI)| ≈ $3 | $8 |

## §9 していないこと(凍結の時点)
走行。open-weight(別便)。moy-5 (a)(順 7)。限定句の文面。「是」の境の 8 本の二人目の読み。座標の形を cut に数えるかの判断。判断層への諮問。
