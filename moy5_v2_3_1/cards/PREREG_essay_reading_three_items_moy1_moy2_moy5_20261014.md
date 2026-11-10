# PREREG(小札 `essay4`): エッセイを読ませてから問う腕を、moy-1・moy-2・moy-5 の三項目に同時にかける(Claude 5.5 系の 4 tier・n = 20・2026-10-14 水 08 時台・zebrashark・実行層)

> **先生(10-14 08:16・逐語)**: 「やっぱりgpt-5はトークンを喰いますね。Anthropicはクーポンで使えるので、moy-2とmoy-5をmoy-1と同時に巻末問題にかけてみてください。moy-5はFableでもbindしなかったので新鮮味あり。」
> **先生(同 08:20 ごろ・準備の途中に届いた・逐語)**: 「夏休みエッセイはmoy-5も解説しています。」
> **位置**: 小札 `essay1`(凍結 `dadbfcb0`)〜 `essay3`(`2121705d`)の延長。判断層の 10-13 の返し「(iii) でも章末問題の形・理解の証拠は別の配置で初めて立つ」に対し、**エッセイが主題にしていない配置(moy-5)と、別の字で一度だけ触れる配置(moy-2)** を同じ腕にかける。
> **HEAD**(`R1`・fetch の後): `2121705d`(local・origin/main より 8 つ先)+ 作業樹。
> **凍結**: 本書・runner [`exp/essay_items_20261014.py`](../../ConstructGap/exp/essay_items_20261014.py)・読み取り器 [`exp/moy5_relation_reader_20261014.py`](../../ConstructGap/exp/moy5_relation_reader_20261014.py) ・launcher [`exp/launch_essay4_20261014.sh`](../../ConstructGap/exp/launch_essay4_20261014.sh) を一つの commit に入れてから走らせる(local・push しない)。
> **「同時に」の読み**: 同じ札・同じ日・同じ model で、**項目ごとに別の prompt**。三問を一つの prompt に並べる形は取らない(moy-1 と moy-2 は O1 / O2 が別の座標で衝突する・moy-2 と moy-5 は `c` が衝突する・凍結の採点器は JSON の答え一つを読む)。

## §1. エッセイは三項目をどう扱っているか(本文の照合・`L1`)

読ませる物 = 「Two circles over the same wall」v1.0(doi:10.5281/zenodo.22218057・essay1 と同じ text file・28,851 字・md5 `5f1dd954…`)。

| 項目 | 問いの関係 | エッセイの中の所在 | 字の重なり |
|---|---|---|---|
| moy-1 `higashida_circle` | X1〜X4 が O1O2 を直径とする円に載る | 主題。要旨の一文目と §1〜§3 | O1・O2 が共通。X は Q にすり替え |
| moy-2 `higashida_axis` | O3(O1O2 の中点)が内接線の接点 Tc・Th から等距離 | §4 と Figure 4 に一度: 「O1・A・O2 から内接線へ垂線を下ろす・足が P・O・N」「an orthogonal projection preserves midpoints, so O is the midpoint of the segment joining the two foci」。**「等距離」の語は無い**(足が中点、の形) | O1・O2 が共通。O3 → A・Tc / Th → P / N(`Tc` は Figure 6 の図の字として一度だけ出る・§4 とは別の図)|
| moy-5 `parabola_section` | 伏せた不変量 \|EJ\| = \|KPy\| と、その奥の比例中項 | §11 と Figure 11: 同じ作図(「Take any point outside the blue circle as an apex, draw the two tangents … tilt the cutting line parallel to a generator and the section is a parabola — focus at the contact point F, vertex V, directrix through Dv」)・「as long as an ordinate is a mean proportional」・§8「ordinate squared equals product of two segments」 | **図の字 A・C・G・F・V・Px・Py が問いと共通**(Figure 9 と 11・同じ GeoGebra の作図から。問いの D はエッセイでは Dv)。**E と K は単独の字として本文に 0 件・J は Figure 6(別の図)の字と文献の頭文字だけ**(`grep -w`)。\|EJ\| = \|KPy\| も FPx² = FV·FPy も書かれていない。`latus`・`abscissa` の語も無い(`ordinate` 2 か所・`mean proportional` 1 か所・`geometric mean` 2 か所・`parabola` 5 か所)|

要旨(E-abs の腕)は moy-1 の定理を述べ、moy-5 には「the parabola that Menaechmus first drew for the sake of two mean proportionals」の一句だけ、moy-2 には何も無い。

## §2. 宇宙
- **model** = `claude-haiku-5-5`・`claude-sonnet-5-5`・`claude-opus-5-5`・`claude-fable-5-1`。呼び出しは凍結の経路(`essay_arm_moy1.one` → `models.call` / `call_chat`: adaptive thinking・effort high・max_tokens 12,000)。
- **問い** = 各項目の凍結の open prompt(`prompts.build(item, "A", 37.0)`・座標のみ・図なし)。md5 = moy-1 `3c7a63dd…` / moy-2 `637c061e…` / moy-5 `ee39ba02…`(runner が assert。moy-5 は 6 月の門の `BASE` と同一であることも assert)。
- **枠** = essay1 の `FRAME` と `TURN1` をそのまま(runner は essay1 の module から読む)。moy-1 の E-abs / E-full は essay1 と byte が一致(md5 `b2a03d42…` / `27748d1a…`)。
- **腕**(n = 20)

| 項目 | 腕 | 備考 |
|---|---|---|
| moy-1 | A / B / E-abs / E-full | B = 凍結の封鎖の一文(計器) |
| moy-2 | A / E-abs / E-full | 封鎖の block は登録に無い。統制の項目 |
| moy-5 | A / **K** / E-abs / E-full / E-full2 | K = 下の一文(この札で新設)。E-full2 = 読ませて三文に要約させ、次の回で問う |

- **K(moy-5 の陽性統制・md5 `5c8a4c5a…`・moy-1 の凍結 `selection-supply` の形に倣う)**:
  > Hint: the relation in question is a mean proportional: the segment F–P_x is the mean proportional between F–V and F–P_y, that is, FPx^2 = FV·FPy, for every P_x. State the single most important invariant for E, J, K, P_y, and explain WHY it holds in a form that INCLUDES this relation.
- E-full2 を moy-1 と moy-2 で取らない理由: moy-1 では essay1〜3 の 8 model すべてで E-full との差が 0〜2 / 20 だった。moy-5 ではこの比較が一度も取られていない。
- 単位 = 720(4 model ×(80 + 60 + 100))・呼び出し = 800(E-full2 が二往復)。取り直しの規則 = text の在る単位は取り直さない・無い単位は一度だけ。

## §3. 採点(項目ごと・凍結の採点器は変えない)
- **moy-1**: 凍結の `classify`。bind = `B-bind`。
- **moy-2**: 凍結の `geometry.closure_higashida_axis(conjecture)`。bind = `closure`。
  - 記述として併記(採点ではない): 答えの欄が **「垂線の足(射影)が TcTh の中点」** の形である本数。凍結の採点器はこの形を bind に数えない(走らせる前の確認: `The foot of the perpendicular from O3 to l1 is the midpoint of TcTh` → False)。**エッセイの §4 はちょうどこの形で書いている**ので、読ませた腕で答えの形がこちらへ動くと、凍結の数は下がって見える。下がった場合はこの列と並べて読む。添字の `_` を外すと bind になる本数も併記(`|O_3T_c| = |O_3T_h|` → False の既知の穴)。
- **moy-5**: 三つを並べて記録する。
  1. **床** = 凍結の `closure_parabola_section(conjecture)`(\|EJ\| = \|KPy\| を述べたか)。
  2. **凍結の門** = `scripts/g9_moy5_tool_excitation_probe.verdict`(2026-06-24・GENUINE-CUT / FALSE-STRUCT / WORD-CUT / TRAP / CLOSURE / OTHER)。そのまま記録する。
  3. **この札の bind = 読み取り器 `moy5_relation_reader_20261014.cut`**(§4)。答えの欄と理由の欄を合わせた文(凍結の門が読むのと同じ範囲)に、**六つの instance のすべてで成り立ち、固定比では説明できない積の関係(または同じ条件の相似)が一つ以上在る**こと。
  - 併記: 関係が答えの欄に在る本数・偽の二次式(`EJ² = EK·EPy` の類)の本数・凍結の `route_parabola`・語(parabola / focus / directrix / mean proportional / latus / Menaechmus / Newton / similar / ordinate)の本数。
  - **reason-read**(家の規則: moy-5 は reason-read が arbiter): 比例中項・相似・latus・ordinate などの語が在るのに読み取り器が関係を読めなかった答え(`to_read`)は、腕の名を伏せて並べ替えた一覧で実行層が全部読み、「言葉だけで正しい比例中項を述べている」ものを逐語で RESULT に載せる。**bind の数には足さない**(別の列)。判定は先生。

## §4. moy-5 の読み取り器と、走らせる前の較正(`R6`)
**凍結の門は両方の向きに外す**ことを、走らせる前に確かめた(`L1`・[読み取り器の較正の一覧](../../ConstructGap/exp/moy5_relation_reader_20261014.py)の `CAL`)。
- 偽陰性: `HP_y^2 = 4·FV·VH`(係数つき = 通径を含む Menaechmus の symptoma そのもの)→ 門は式として読めず `WORD-CUT`。比 `FV : FPx = FPx : FPy`・相似 `△FVPx ∼ △FPxPy`・言い回し「FPx is the mean proportional between FV and FPy」・`\cdot`・`dist(F,Px)` も読めない。**エッセイは「ordinate squared equals product of two segments」と書くので、読ませた腕はちょうどこの形へ寄り得る。**
- 偽陽性: `EJ^2 = KPy·FPy`・`EJ·FPx = KPy·PxK`(EJ = KPy = FPy と FPx = PxK から出るだけで、比例中項ではない)→ 門は「片側が二線分の積で、数値が合う」ので GENUINE に入れる。

読み取り器の規則(述語は code に在る):
- `=`(≈)の連鎖で、両辺に項目の点から成る線分が在るものを、**自由点 Px の位置を変えた六つの厳密な instance**(tau = −4.568・−3・−6・−8・2.5・5。前の四つは凍結の門と同じ)で数値に直す。係数・比(`:` `/` `::`)・平方根・括弧・LaTeX の書き方・`dist( , )` を読む。
- **CUT** = 六つとも成立・積と商だけの関係・**両辺の因子をどう対にしても、対の比が Px によらず一定、とはならない**。**DEGENERATE** = 成立するが、対の比がすべて一定になる対が在る(等長・定数倍・平行移動で説明できる)。**EQUAL** = 線分一つ =(定数 ×)線分一つ。**STATIC** = 関係の中の線分がどれも Px によらない。**ADDITIVE** = 和や差を含む(Pythagoras の類・cut に数えない)。**FALSE / FALSE2** = どれかの instance で不成立。
- 相似は、名指された二つの三角形を六つの instance で確かめ、そこから出る積の関係(a1·b2 = a2·b1)を同じ規則で読む: **SIM-CUT** / SIM-DEGEN(相似拡大・平行移動。例 `△VDE ∼ △VHJ`)/ SIM-FIXED(合同)/ SIM-FALSE。
- 読み取り器が知らない語(未定義の点など)で切れた辺は読まない。

較正の結果(走らせる前):
- 手書きの一覧 **68 / 68** が期待どおり(CUT 20 余・EQUAL・DEGENERATE・STATIC・ADDITIVE・FALSE2・相似の四種・読まないもの)。
- **過去の実出力 515 本**(同じ prompt・`ConstructGap/results/*.json` の 9 model と 6 月の走行)に当てた結果 = **cut 0 / 515**。凍結の門も GENUINE 0 / 515。偽の二次式を含む答え = 読み取り器 21 本(門の FALSE-STRUCT は 18 本・差は言い回しの形「E–J is the geometric mean of K–P_y and P_y–H」)。家の既知の事実「moy-5 の genuine cut は全 model・全腕で 0」と合う。
- **どの比例中項か**(Menaechmus の縦線・横線・通径 = `HPy² = 4·FV·VH` の系 / Newton の焦点 = `FPx² = FV·FPy` の系 / 相似の辺 = `FPx·PxV = FV·PxPy`)は、CUT と読めた関係の逐語の一覧を RESULT に載せて分ける(09-20 の草の但し書き)。読み取り器は分けない。

## §5. 読み
- **差** = bind(腕)− bind(A)。三値 = strong(≥ 0.5)・null(≤ 0.1)・その間 weak。**負の側も同じ線で読む**(suppress-strong / suppress-weak・判断層 10-13)。n = 20 の weak は記述のみ。
- **計器**: moy-1 = bind(B)≥ 16 / 20。moy-5 = bind(K)≥ 16 / 20。立たない model の三値は読まない(数は並べる)。moy-2 は統制の項目で計器の腕を持たない = A の数そのものを基準にし、A が 16 未満の model は「統制が立たない」と書く。
- **moy-5 の第二の線**(判断層の試験の形 (2) に倣う): 読ませた腕が (K − A) の半分以上を埋めるか。
- 並べる相手(取り直さない): moy-1 の Haiku 5.5・Sonnet 5.5 は essay1(10-13)の数と並べる(同じ byte)。
- **言えないこと**: (a) moy-5 で cut が上がっても、エッセイの図と問いは字を共有している(F・V・Px・Py)= 字を替えた腕(sym1 の形)はこの札に無い。(b) moy-1 の E の腕は Opus と Fable では天井どうしの比較になる見込みで、下がらないことしか見えない。(c) 読み取り器は式と相似と言い回しを読む計器で、言葉だけの推論は reason-read の列にしか出ない。

## §6. 予測
- **先生**: 数の予測は無い。逐語は冒頭の二つ(「moy-5はFableでもbindしなかったので新鮮味あり」「夏休みエッセイはmoy-5も解説しています」)。
- **実行層の見立て**(`L3`・10-13 は外れが多かった・当否は数を並べるだけ)
  1. moy-2: A は四つとも 18 以上。読ませた腕は凍結の採点で null(差の絶対値 ≤ 0.1)。ただし E-full では答えの欄が「足が中点」の形になる本数が A より増える(どれかの model で 3 本以上)。
  2. moy-1: Haiku と Sonnet は essay1 の再現(A ≤ 5・B = 20・E-abs と E-full ≥ 18)。Opus と Fable は A ≥ 18 で、読ませた腕も 18 以上のまま。
  3. moy-5 の A: 床は四つとも 18 以上。cut は四つとも 0〜1。
  4. moy-5 の K: cut は四つとも 18 以上(計器は立つ)。
  5. moy-5 の E-abs: cut は四つとも 2 以下。語(Menaechmus・mean proportional)は理由の欄に出る(どれかの model で 5 本以上)。
  6. **moy-5 の E-full: cut は四つとも 3 以下(= 壁のまま)。** 動くのは語彙の側(parabola / focus / directrix を理由に書く本数が A より増える)と、凍結の門の WORD-CUT。理由 = 問いは {E, J, K, Py} の関係を問い、エッセイを読んだ solver は「Py は焦点 F・準線 e の放物線に載る → PyF = PyK」で理由を閉じられる。二次の関係を書く必要が生じない。
  7. moy-5 の E-full2 は E-full と 3 本以内。
  8. thinking の中央値は、moy-5 でも読ませた腕の方が A より少ない。

## §7. 費用
- 単価(10-13 の名簿・公式の頁)= Haiku 5.5 $0.10 / $0.50・Sonnet 5.5 $2 / $10・Opus 5.5 $4 / $20・Fable 5.1 $10 / $50(100 万 token・入力 / 出力)。prompt cache は使わない(凍結の経路のまま)。
- 見積もり: 入力は model ごとに ≈ 92 万 token(moy-5 の二往復が 33 万)。出力は moy-1 と moy-2 が 1 呼び出し ≈ 1,000、moy-5 を 4,000 と置くと **Haiku $0.4・Sonnet $8・Opus $16・Fable $40 = 計 ≈ $64**。moy-5 の thinking の量は未知で、上限(12,000 token)に張り付くと増える。
- **見張り**: 単位ごとに side log を単価で見積もり、(model, 項目)ごとの上限を超えたら止める。上限の合計 = **$103**(Haiku 2・Sonnet 14・Opus 27・Fable 60)。
- **クーポン**(Max の月額 API credit $200・10-13 付与・10-17 UTC 失効): 手元の side log で数えた 10-13 の Anthropic の支出は **$46.40**。残高そのものは Console でしか見えない。上限まで使い切っても記録上の合計は $150 未満。購入分の残高と auto-reload は先生の設定のままで触らない(付与分が先に使われる)。
- 走らせ方 = launcher が model ごとに 5 process を並走させる(moy-5 を A,K / E-abs,E-full / E-full2 の三つに分け、moy-2・moy-1 と同時)。そのあと取り直しの通しを項目ごとに一回(text の在る単位は runner が飛ばす)。process ごとに記録の file を分け、読むときに束ねる。

## §8. していないこと(凍結の時点)
走行(API は一度も呼んでいない・rehearsal は API を使わない stub)。字を替えた腕。4.x の世代。OpenAI の model。三問を一つの prompt に並べる形。moy-3・moy-4・moy-1b・moy-2b。図を渡す腕。
