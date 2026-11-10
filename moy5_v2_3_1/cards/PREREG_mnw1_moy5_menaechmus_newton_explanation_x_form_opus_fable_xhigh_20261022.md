# PREREG(札 `mnw1`): moy-5 × Menaechmus / Newton の説明 {なし / 配置の同定 / 円錐} × 問いの形 {Q1 / Q1 + 比例の形} — Opus 5.5 xhigh と Fable 5.1 xhigh を並走・API の経路(2026-10-22・実行層)

> **先生(10-22・逐語)**: 「MenaechmusとNewton (principia 一巻の補題) です。fable-5.1にどんな説明を足すとcutすると思いますか？」(GeoGebra の図 3 枚 = Menaechmus の円錐の切り口〔円の弦の半分が直径の二つの断片の比例中項・`coeff = FJ² / F v_p` が一定〕・双曲線の面積の適用・Newton の補助定理 XIV〔焦点から接線への垂線の足〕)→ 実行層の答え(chat・下 §0-3)→ **「札を凍結して発火してみましょう。opus-5.5-xhighも並行して。」**
> **HEAD**(`R1`・fetch の後): `d9af79f1`(origin/main `18f7a079` の 1 つ先 = 朝の MEMO の commit・push 待ち)。**凍結し直し(発火の前・開示)**: 初版の凍結 `0f30732b` はこの行に「origin/main と同じ」と誤記していた → 本 commit で直した。設計・足す文・述語・判定・予想は不変(md5 は §2-4 のまま)。**凍結の実体**: 本書・runner [`ConstructGap/exp/mnw1_moy5_menaechmus_newton_explanation_x_form_api_xhigh_20261022.py`](../../ConstructGap/exp/mnw1_moy5_menaechmus_newton_explanation_x_form_api_xhigh_20261022.py)・launcher [`ConstructGap/exp/launch_mnw1_20261022.sh`](../../ConstructGap/exp/launch_mnw1_20261022.sh) を一つの commit に入れてから走らせる(runner は札・launcher・script が commit と違えば走らない。読み取り器 v2 の較正 72 / 72 を呼ぶ前に assert)。
> **身分**: §0 = 開示(既知の数の写し)。§1〜§5 = 凍結の設計・述語・判定。§6 = 予想(発火の前に書く・当たり外れは RESULT に)。採否と決め台詞は先生。

## §0. 事前に知っていること(開示・数は各 RESULT の写し)
1. moy-5 の cut(読み取り器 v2 が CUT / SIM-CUT と読む関係が答え全体に一つでもある)は、問い Q1(焦点の集合 {E, J, K, P_y}・不変量を一つ)では、知識を足す腕でほぼ 0: エッセイ §11「縦座標は比例中項」0 / 317(essay4・10-14)・6 月の principle supply 0 / 90・「等長だけでは足りない」の注釈 NONE(neq1)。
2. **名だけ**(「Cf. Newton, Principia, Book I, Section III, Lemma XIV.」)で、Fable 5.1 xhigh は理由の欄に cut を 7 / 20(neq2f・`claude -p`)。**本文**(Motte 1846 の補助定理 XIV)では配置の対応を 16 / 20 で書くが、使うのは系 3 で cut 0。Opus 5.5 は名で誤って結ぶ 7 / 20。答えの欄は両 model とも 60 / 60 等長。
3. **問いの点の集合**を {F, V, P_x, P_y}(Q2)に向けると、何も足さなくても答えの欄で Fable 20 / 20(天井)・Opus は軌跡 20 のうち比例中項も 7 → 名か本文で 20 / 20(neq3)。effort で Opus 0 → 1 → 7 → 19(neq6)。= 答えの欄の族は問いの点の集合が限る([RECORD neq](../2026-10-19/RECORD_reading_neq2_to_neq5_answer_selected_by_point_set_20261019.md)・10-22 に狭めた版)。
4. 理由の欄に「等長でない関係」を求める一文(β′)で、API high の Fable は 0 / 20・Opus 6 / 20(+ r8 = 7)。Claude Code の max では Fable 6 / 10・Opus 10 / 10(SUMMARY 10-16)。
5. 証明を求めると焦点・準線の近道で閉じ、格子は Fable 0 / 10・Opus 2 / 10(prf1)。近道を塞ぐと自分で格子を持ち出す = Fable 4 / 8・Opus 10 / 10(prf3)。Fable が持ち出す形は**頂点の比例中項** VP_x² = FV·VH(Menaechmus の形)で、K が渡す**焦点の形** FP_x² = FV·FP_y(Newton の形)ではなかった。
6. 実行層の読み([MEMO 10-22](MEMO_moy5_cut_status_cognitive_form_position_and_moy1_activation_20261022.md)・`L3`): Fable には「説明」より「答えの座席」が足りない。説明で動くのは理由の欄で、答えの欄を動かすのは問いの点の集合・effort・封鎖。
7. **実行層が chat で先生に返した見立て(逐語の要旨・本札の予想の元)**: 効くと思う順 = (1) 答えの形の指定を Menaechmus / Newton の言葉で(答えの欄 10〜20 / 20・ただし指図)/ (2) 配置の同定だけを渡す(理由の欄 10〜15 / 20・答えの欄は等長のまま)/ (3) Menaechmus の円錐の説明(答えの欄 0〜2 / 20・理由の欄に頂点の形が増えうる)。
8. 本日の API の煙試験(10-22・一語の問い・両 model): `output_config.effort = "xhigh"` を受け、stop = end_turn・usage に `output_tokens_details.thinking_tokens`。

## §1. 問い(何を分けるか)
- 名(看板)→ **配置の同定**(役の対応)→ K(関係そのもの)の梯子で、「説明」のどの段で cut が出るかを、**答えの欄**(問いが族を限る)と**理由の欄**(説明が動かしうる)に分けて測る。
- 同時に、**問いの形**(「比例として述べよ」の一文 = 指図)が答えの欄をどれだけ動かすかを、説明と直交させて測る(3 × 2)。
- 腕の設計:

| | Q1(凍結の問い) | Q1f(Q1 + 比例の形の一文) |
|---|---|---|
| none(何も足さない) | **none/Q1** = essay4 の A と byte 一致 | **none/Q1f** |
| conf(Newton の補助定理 XIV の名 + 役の対応・関係は言わない) | **conf/Q1** | **conf/Q1f** |
| cone(Menaechmus の円錐の説明・問いの字を使わない) | **cone/Q1** | **cone/Q1f** |

- **K**(Q1 + essay4 の K block = 関係そのもの)= 陽性統制・関門(n 10・両 model)。essay4 の K と byte 一致(md5 `b0b1d14b…`)。

## §2. 宇宙
1. **model** = `claude-opus-5-5`・`claude-fable-5-1`。**経路 = API**(`https://api.anthropic.com/v1/messages`・stream・adaptive thinking・`output_config.effort = "xhigh"`・`max_tokens 48000`・timeout 3600 s・鍵は家の keys.env)。rte1 の API max の本体を effort だけ替えた。Fable の壊れた出力(`claude -p` の harness で道具を呼ぼうとして JSON を出さずに終わる・prf1〜prf3)を避けるため API にした。**⚠ neq2f・neq3 の xhigh は `claude -p` の経路**で、API の xhigh と同じ目盛りとは限らない(§8)。
2. **問い** = moy-5 の凍結の open prompt(md5 `ee39ba02…`・問いの文は替えない)。
3. **足す文**(逐語・runner の定数):
   - **FORM_NOTE**(Q1 の末尾・JSON の指示の後に一行・neq1 の Q_NEQ と同じ置き方・md5 `035d58b0…`・136 字): `\nNote: in the manner of Menaechmus and Newton, state the invariant as a PROPORTION (a mean proportional), not as an equality of lengths.` — 「放物線」の語は使わない(Opus の放物線の同定に効かせない)。
   - **CONF**(Q1 の前に置く・md5 `c82bde14…`・334 字): `Cf. Newton, Principia, Book I, Section III, Lemma XIV. In the configuration below, the roles of that lemma are taken as follows: F is the focus, V is the principal vertex, h1 is the tangent at the vertex, P_y is a point of the curve, m is the tangent at P_y, and P_x is the foot of the perpendicular let fall from F on that tangent.` — 名(neq2 と同じ一文)+ 役の対応。**比例中項の語も式も無い**。
   - **CONE**(Q1 の前に置く・md5 `f4ca35c6…`・926 字): Menaechmus の直角円錐の切り口 — 点を通り底面に平行な平面の円で、直径に垂直な弦の半分は直径の二つの断片の比例中項(直角三角形の斜辺への垂線と同じ)。断片の一方は頂点からの距離に比例し他方は一定。ゆえに縦座標の平方は横座標に比例し、定数は latus rectum。この比例(等長ではない)が曲線の定義の性質(symptoma)。**問いの字(E・J・K・P_y・F・V・P_x・h1・m)は一つも使わない** = 原理の供給。
4. **腕と n**: K 10 / 六腕 各 20 = model あたり 130 回・計 260 回。prompt の md5(dry): K `b0b1d14b…`・none/Q1 `ee39ba02…`・none/Q1f `f4522117…`・conf/Q1 `bb82c97e…`・conf/Q1f `f32c88a9…`・cone/Q1 `ec464241…`・cone/Q1f `2c50d183…`。
5. **取り直しの規則** = text の在る単位は取り直さない・無い単位(HTTP の誤り・空)は一度だけ取り直す(2 回目も無ければ欠番)。`stop_reason = max_tokens` の行は text が在れば数える(記述に本数を載せる)。
6. **並走** = model ごとに別の process(launcher)・各 4 worker。順 = K 10 → 関門 → 六腕 → 取り直し → `--read`。
7. **費用の見張り** = 側の log(usage の input / output)から単位ごとに見積もり、上限に達したら以後の単位を引かない(Opus $25・Fable $70・§7)。

## §3. 採点(計器 = 一つ・凍結の読み取り器)
- **主の量 = `cut`** = 読み取り器 v2(`moy5_relation_reader_v2_20261014.py`・凍結 `e07c3abd`・CAL 72 / 72 を assert)が答え全体(答えの欄 + 理由の欄)に CUT か SIM-CUT を一つでも読む。= neq1 の bind と同じ定義。
- **副の量 = `cut_ans`** = 答えの欄(`conjecture`)だけに同じ判定。
- 併記(記述・判定に使わない): 床 = 凍結の `closure_parabola_section`(等長)/ `equal_ans`(答えの欄が等長)/ `cut_or_r8`(r8 の述語を足した数・10-15 と同じ)/ **形の分類**(CUT の関係の `net` の鍵で、焦点の形 = `FPx` を含む・頂点の形 = `PxV` か `HPy` を含む・`L2`・dry で陽性 / 陰性の自己試験)/ 放物線・Newton・Menaechmus の語(正規表現・neq3 と同じ)/ thinking token(usage)/ `to_read`(比例中項の語があるのに関係が読めない答え → 腕を伏せて実行層が読み、逐語を RESULT に載せる・**数には足さない**)/ 凍結の門(2026-06-24)と v1 の bind(essay4 の数と並べる)。

## §4. 関門(陽性統制・`R6`)
1. 走る前に読み取り器 v2 の較正 72 / 72 を runner が assert(落ちたら一回も呼ばない)。形の分類の自己試験は dry で通した(焦点 / 頂点 / 両方 / なし)。
2. **K を先に 10 回・model ごと**。**K の cut ≥ 8 / 10 でなければ、その model の他の腕は走らせない**(計器か書き手が今日は働いていない)。
3. API の誤り(HTTP・timeout)は取り直し一回。側の log に `http_error` を残す。

## §5. 判定(凍結・runner の `verdict()`・model ごと・余白 3 / 20 = `R3`・天井 17)
- どれかの腕(K 以外)が 18 本未満なら INCOMPLETE。
1. **FORM**: none/Q1f の cut_ans ≥ 4 かつ none/Q1f − none/Q1 ≥ 3 → YES(比例の形の一文だけで答えの欄が動く)。
2. **CONF@Q1 / CONE@Q1**(主 = cut・答え全体): X/Q1 の cut ≥ 4 かつ X/Q1 − none/Q1 ≥ 3 → YES(説明が理由の欄を含めて cut を連れてくる)。
3. **CONF-ANS@Q1 / CONE-ANS@Q1**(副 = cut_ans): 同じ形で答えの欄。
4. none/Q1f の cut_ans ≥ 17 なら **FORM CEILING**(Q1f の上で説明の効き目は測らない)。そうでなければ **CONF@Q1f / CONE@Q1f**: X/Q1f の cut_ans ≥ 4 かつ X/Q1f − none/Q1f ≥ 3 → YES。
5. **CONF×FORM / CONE×FORM**(交互作用・cut_ans): (X/Q1f − none/Q1f) − (X/Q1 − none/Q1) ≥ 3 → YES。
- 判定の後の読み(記述・`L2` / `L3`): 形の分類(conf は焦点の形・cone は頂点の形に寄るか)/ 伏せ読み(to_read の行)/ 「指図」の但し書き = FORM が YES でも「説明で cut した」とは読まない(問いの族を替えている)。

## §6. 予想(発火の前に書く・§0-7 の見立てをそのまま数に)
- **P1(FORM)**: 両 model で YES。none/Q1f の cut_ans は Fable ≥ 10 / 20・Opus ≥ 10 / 20。Fable は FORM CEILING(≥ 17)になりうる(五分五分)。
- **P2(CONF@Q1)**: Fable は YES で cut ≥ 10 / 20(名だけの 7 / 20 より上)。CONF-ANS@Q1 は NO(cut_ans ≤ 2 / 20)。Opus は CONF@Q1 YES(cut ≥ 5 / 20)・CONF-ANS@Q1 NO。
- **P3(CONE@Q1)**: 両 model で NO(Fable cut ≤ 6 / 20・cut_ans ≤ 2 / 20)。
- **P4(none/Q1 = 基線・API xhigh)**: 両 model で cut ≤ 2 / 20(essay4 の A は high で 0 / 20)。
- **P5(形・記述)**: conf の腕の CUT は焦点の形(FP_x² = FV·FP_y)が多数、cone の腕の CUT は頂点の形(VP_x² = FV·VH・HP_y² = 4·FV·VH)が多数。
- **P6(交互作用)**: CONF×FORM・CONE×FORM とも NO(説明と形の効き目は足し算で、掛け算ではない)。

## §7. 費用
見積り: 一回あたり出力 ≈ Opus 2.5k token・Fable 5k token(neq6 の xhigh の thinking の中央値 1.7k / 4.1k + 答え)・入力 0.6〜0.9k。Opus ≈ $0.06 × 130 ≈ $8・Fable ≈ $0.26 × 130 ≈ $35。**上限 = Opus $25・Fable $70**(側の log から単位ごとに見積もって止める)。経路 = API(月の API credit の枠)。

## §8. 主張しないこと
- conf は「知識」ではなく「役の対応」の供給で、名 → 関係の梯子の中段。cut が出ても「説明で看破した」とは読まない(対応を渡せば補助定理の形が一段で出る)。
- Q1f は問いの族を替える**指図**。FORM が YES でも Q2・Q3 の天井と同じ物を見ている。
- 一つの作図・一つの配置・二つの model(同じ社)。API の xhigh と `claude -p` の xhigh は同じ目盛りとは限らない(neq2f・neq3 との比べは記述まで)。
- 形の分類(焦点 / 頂点)は `net` の鍵の正規表現で、SIM-CUT は `src` の字で分ける = `L2`。06-25 の CUT(幾何平均の格子)との同一性は本札では決めない。
- model の内側は言わない(振る舞いの数だけ)。

## §9. 手順
- 凍結の commit の後、zebrashark で `bash /Users/manabu/lancedb-rag/ConstructGap/exp/launch_mnw1_20261022.sh claude-opus-5-5` と `… claude-fable-5-1` を別 process で背景に(絶対 path・`bash -c`)。
- 出力 = `ConstructGap/exp/results_mnw1_moy5_20261022_<model>.jsonl`・側の log = `ConstructGap/exp/logs/mnw1_moy5_20261022_<model>_sidelog.jsonl`・launcher の log = `ConstructGap/exp/logs/mnw1_20261022_<model>_{k,arms,redraw}.out`。
- RESULT = `conversations/2026-10-22/RESULT_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md`(両 model がそろってから・`--read` の表の写し・予想の当たり外れ・伏せ読み)。
