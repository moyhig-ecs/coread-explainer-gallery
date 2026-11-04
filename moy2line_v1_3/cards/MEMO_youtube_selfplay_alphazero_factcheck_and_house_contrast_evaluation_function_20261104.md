HEAD(R1) = 63b7b3ad(執筆時の HEAD・origin より 34 commit 先・遅れ 0)

# MEMO: YouTube「AIはなぜ、人間の棋譜を1つも見ずに人間より強くなれるのか？｜自己対戦の正体」(_A1acg0ZTKs・AIゆっくり探究所・2026-10-09・39:33)— 裏取り(Opus 5.5 medium)+ 第二計器(Opus 5.5 xhigh)+ 家の手法(olmX の系列)との比較 + 先生の問い「olmX シリーズから評価関数を導出できますか」(2026-11-04)

- 発注(逐語・先生 11-04 朝): 「opus-5.5-mediumで裏どり。olmXシリーズから評価関数を導出できますか？」
- 部品: 字幕 = [SOURCE](SOURCE_youtube_selfplay_alphazero_transcript_ja_20261104.txt)(md5 `d627322c…`・531 文・章立て 13・10-14 の channel 一覧に載っただけで裏取りは未)/ 一便 = [BRIEF](BRIEF_factcheck_opus55_medium_20261104.md) → [RESULT](RESULT_factcheck_opus55_medium_20261104.md)(122 行・一次資料 38 本・`data/agentA/MANIFEST.tsv`)/ 第二計器 = [BRIEF](BRIEF_second_instrument_opus55_xhigh_20261104.md) → [RESULT](RESULT_second_instrument_opus55_xhigh_20261104.md)(26 点・§5)。
- 記号: L1 = 一次資料の逐語 / L2 = 二次(Wikipedia・報道)/ L3 = 読み(採否は先生)。**講評は先生のもの**(この MEMO には書かない)。

## §0. 一枚の表

| 項目 | 数 |
|---|---|
| 事実の照合(Q1) | 122 行 = 一致 **113** / **不一致 0** / 一次資料に無い 7 / 確かめられない 2 |
| 言い方(Q2) | 17 件 = 同じ強さ 11 / 原文より強い **4** / 原文に無い 2 |
| 作者の測定(Q3・概要欄 vs 本文) | 25 行 = 合う 22 / **合わない 1**(25:57「28 勝 2 敗」vs 概要欄「18 勝 2 敗」)/ 読めない 1 / 本文に無い 1 |
| 第二計器(26 点) | §5 に追記 |

- 一次資料に無い 7 のうち 2 は作者の測定(三目並べ 255,168 / 5,478 = Wikipedia 当日版は 765 / 26,830 の数え方)、残りは「平方根でしか縮まない」「Hoeffding と UCB の結び付き」「網で近似すると良くなり続ける保証はない」(AGZ には逆向きの "did not suffer from the oscillations or catastrophic forgetting" が在る)など**動画の説明の言葉**。確かめられない 2 = 3,000 万手(Nature 2016 の本文が取れず)・2,500 万ドル(Nature News が有料)— どちらも L2(Wikipedia)では一致。
- 一次資料が二つの値を持つ物: AlphaZero 対 Stockfish は arXiv 2017(100 局 28 勝 72 分 0 敗・8 万 vs 7,000 万局面 / 秒)と DeepMind blog(1,000 局 155 勝 6 敗・6 万 vs 6,000 万)で違い、動画は blog の値。

## §1. 裏取りの要点(一便・L1)

- **本題(第 6・7 章)は全部一次と一致**: 人の棋譜も特徴も使わない(抄録 "without human data, guidance, or domain knowledge beyond game rules")・ランダムな重みから・1 手 1,600 simulation・PUCT("a_t = argmax(Q(s_t, a) + U(s_t, a))")・ロールアウトなし・方策の正解 = 探索の訪問分布 π・価値の正解 = 勝敗 z("(p, v) = fθ(s) more closely match the improved search probabilities and self-play winner (π, z)")・**「AlphaGo becomes its own teacher」**(抄録)・生の網 Elo 3,055 / MCTS 付き 5,185・200 点差 = 勝率 75 %・方策改善 / 方策評価の演算子("MCTS may therefore be viewed as a powerful policy improvement operator"/ "Self-play with search … may be viewed as a powerful policy evaluation operator")・方策反復("an approximate policy iteration scheme")・490 万局・0.4 秒 / 手・36 時間で Lee 版を超え・72 時間で 100–0・40 日 2,900 万局で Master に 89–11・Elo 3,144 / 3,739 / 4,858 / 5,185・教師あり網は手の予測は上だが 24 時間以内に負ける・定石の再発見と新しい変化・シチョウは後から・対称性の利用・Marcus 2018「overstated」。
- 第 8〜11 章も一致: Tesauro 1995(決定的ゲームの自己対戦の病理・チェッカーと囲碁の先例・TD-Gammon 150 万局・Robertie にわずかに届かず・サイコロが状態空間を広げる・TD 学習・「偏見に縛られない自由」)・ディリクレノイズ・温度(最初の 30 手 τ = 1)・AlphaStar「chasing its tail」とリーグ(exploiter)・Wang ら 2023(KataGo に 97.3 %・計算 14 % 未満・輪の形・10^7 visit で 72 %(50 局))・Pelrine 14 / 15・Leela Zero にも・Russell(記者の間接話法 + 直接の引用 "far too hasty to ascribe superhuman levels of intelligence")・Tseng ら 2024(守りは新しい敵に耐えず・同じ輪の族)・イ・セドル引退 2019-11-19 と「priceless win」(L2)・樊麾(L2)・Shin ら 2023(580 万手・580 億の反実仮想・新規性と質)・AlphaZero(24 時間・4 h / 2 h)・MuZero(ルールなし)・Bitter Lesson(70 年・探索と学習・「efforts proved irrelevant, or worse, once search was applied effectively at scale」)・DeepSeek-R1(純粋な RL は R1-Zero・"aha moment"・"we do not explicitly teach the model how to reason")。
- 第 1〜5 章: 四目並べ 4,531,985,219,092・1988 年 Allen / Allis・先手必勝(中央)・Shannon 10^120・囲碁 2.08 × 10^170(Tromp 2016)・Deep Blue(2 億局面 / 秒・8,000 の特徴・1996 年 1 勝 2 分 3 敗)・Samuel 1959(IBM 701・rote learning)・Coulom 2006・UCT(Kocsis & Szepesvári 2006)・AlphaGo 2016(他のプログラムに 99.8 %・樊麾 5–0・イ・セドル 4–1・37 手目 1 / 10,000)= 一致(詳細は RESULT §1)。
- **動画の中の不一致 1**: 25:57「第 50 世代では同じ相手(1,000 回読むプログラム)に 28 勝 2 敗」は概要欄と 1:05 / 29:37 の「18 勝 2 敗」と合わず、20 局なので 28 + 2 = 30 にもならない(ASR の誤りか原稿の誤りかは音声を聞かないと分けられない)。

## §2. 言い方(Q2・L3 は一便)

- 原文より強い 4: (a)「読みの分だけ先生が**いつも** 1 段上」(原文 "**usually** select much stronger moves")/ (b) 章題「3 日で人間を追い越す」(論文の 72 時間の比較相手は AlphaGo Lee・人間との対局は論文に無い)/ (k) DeepSeek-R1(純粋な RL は R1-Zero・R1 は rejection sampling + RL + SFT)/ (o)「78 手目が **AlphaGo から見て** 1 万分の 1」(WIRED の文に主語の限定なし)。
- 原文に無い 2: (i) 結論「強くなる力は相手からでなく**読みと答え合わせから**」= 論文の二つの演算子(policy improvement / policy evaluation)の動画の言い換え / (j)「網で近似すると良くなり続ける保証はない」= AGZ に無く逆向きの記述が在る。
- 動画は自分で限りを付けている所が多い(「感想だから言い切れはしない」「測ってる物差しが AI 自身」「1 人の研究者の見方」)= 同じ強さ 11。

## §3. 家の手法(olmX の系列)との比較(L3・主 session)

動画の枠は「読み(探索)・答え合わせ(ルールの勝敗)・読みが先生(方策改善 → 方策評価)・練習で見ていない形(穴)」の四つ。家の moy-2 の系列(olm113〜127)の値を当てると:

| 動画の部品(L1 の定義) | AlphaGo Zero | moy-2 の OLMo-3 32B base(olmX の値) | 家に在るか |
|---|---|---|---|
| 答え合わせ = "The terminal position s_T is scored according to the rules of the game to compute the game winner z" | 対局の勝敗 | 座標で関係を数値で確かめる + 図を動かしても保つか(drag の不変 = metamorphic oracle・ggblab) | **在る**。model 自身も、式を数値で使った行では折り返しを退ける(olm125: 計算した 18 本のうち v6 の REJ6 15 本 = 15 / 15・olm124 11 / 14・olm119 11 / 12) |
| 読み = MCTS("a_t = argmax(Q + U)"・1,600 回) | 木を降りて価値を遡る | 無い。候補を一つ試し、退け、次の候補を出す(木が無い・候補の分布が無い) | 無い |
| 価値の勘 = "a scalar value v_t, representing the probability of the current player winning" | 価値網 | 無い。olmX の計器(v3 / v6 の線対称の印・外接線の印・退けの印)は**価値でなく「記憶の前提が出た印」** | 計器として在る |
| 読みが先生 = "MCTS … policy improvement operator"・"self-play … policy evaluation operator" | 探索の分布 π と勝敗 z を正解に | **退けが commit を支配しない**: 退けた後に証明の欄で線対称が戻る(b2_j07 の型・五腕で 0 / 3 / 2 / 1 / 3 本)・計算すると MIDO3(中点・偽)は 0 本になり EQ(等距離 = apex・**真**)9 本に着く(olm125)が、等距離を数値で確かめた行は 0 で、証明の欄の前提は記憶の線対称のまま(b2_j07 の型 3 本)= 結論は図に合い前提は記憶のまま(**訂正 11-04 昼**: 初版は EQ を「一般には偽」と書いた = 誤り・RESULT olm125 の訂正の節) | 欠けている環 |
| 練習で見ていない形 = 輪で囲む形(Wang 2023)/ "ensures a diverse set of positions"(ノイズ・温度) | exploiter・ディリクレノイズ | 半径の等しい図(olm117)= 記憶の前提「接点は O1O2 について対称」が**真になる形**(線対称 0.12 → 0.15・点対称 0 → 4 / 46)/ 一般の図 = 見ていない形(前提は偽・olm113 で 0.122 が残る) | drag oracle が敵対的方策の役(動かせば前提の偽が露れる) |

- 動画の三つの見方(39:05「答え合わせを誰がしているか / 読みが先生役をしているか / 練習で見ていない形はどこか」)を家の札に当てると: 答え合わせ = 座標と摂動(道具は在る・model は使えば退ける)/ 読みが先生 = **していない**(退けが証明の欄に届かない)/ 見ていない形 = 半径の異なる一般の図(記憶の前提は等半径の図から来る)。
- olm125 の読み「道具の段に文が増えるほど、道具の存在が『線対称が答えだ』の手掛かりとして読まれる」(b1_j09「Considering the provided reflection tool, it likely relates to the symmetry over the line O1O2」)は、動画の「読みが届かないところは力も届かない」(38:57〜39:02・動画の言葉)の家の側の形 = **答え合わせの道具が在っても、読み(候補の木)が無ければ、道具は使われるより読まれる**。

## §4. 先生の問い「olmX シリーズから評価関数を導出できますか」(L3・主 session の答え)

**短く**: 評価関数(AlphaGo Zero の意味の価値関数 v_θ = 確かめる前に勝ち目を出す学習した頭)は olmX からは**出ない**。出るのは**受領関数**(答え合わせ = 人の正解なしに行を受け入れるか決める述語)と、**評価が使われているかを測る計器**で、olmX の系列が示しているのは「答え合わせは在るのに読みが無く、退けが commit に届かない」という欠けた環そのもの。

1. **導出できるもの = 受領関数 A(row)**(二値か順序・人の正解を要しない):
   - A(row) = JSON が取れた ∧ 予想の関係が与えた座標で数値的に真 ∧ 図を動かしても真(drag の不変・k 回の摂動)∧ 証明の欄に記憶の前提の印(v6 の LN6_a / OUTER6_a で肯定かつ退けなし)が無い。
   - これは先生の「答えの前に受領の条件を書く」そのもので、動画の「ルールが勝ち負けを自動で判定してくれる答え合わせ」(37:19)に当たる。AlphaGo Zero の "scored according to the rules of the game" の「ルール」は幾何では**座標と摂動**。
   - これを報酬にすれば、DeepSeek-R1 型(検証可能な報酬の強化学習・動画 38:09)の輪は幾何の予想でも原理上回せる(摂動は ggblab で出せる)。
2. **導出できない理由**(正直に):
   - olmX の行には正しさの札を付けていない(規律として「正しさの率は測らない」)= 学習の教師信号(z に当たる物)が無い。
   - 60 行 × 約 15 札 ≈ 900 行で、類は偽の引力(MIDO3 = 共線 / 中点)と apex(EQ = 等距離・真)と JSON なしに偏り、行に正しさの札が無い = 価値の頭を学ぶ材料にならない(訂正 11-04 昼: 初版の「二つの偽の引力(MIDO3・EQ)」は誤り・EQ は真)。
   - drag oracle は**関係**を確かめるが**証明**は確かめない(証明の欄の印は代用)。評価関数が「証明の良さ」まで出すには、証明の段ごとの検証(formal か数値)が要る。
3. **olmX が自己対戦の輪に対して持つ意味**(動画の枠で):
   - 読み(探索)の不在が主症状で、答え合わせの不在ではない。計算した行は折り返しを退ける(15 / 15)が、退けた後の次の候補は木からでなく記憶から出る(olm125 の EQ 9 本は apex = 真に着くが、数値で確かめた行は 0 で、証明の欄は記憶の線対称で埋まる 3 本。olm127 では b0_j00・b2_j09 の 2 本が等距離を数値で確かめる)。AlphaGo Zero では「探索の分布 π が次の方策の正解」になる所が、OLMo では「記憶の分布がそのまま次の候補」。
   - だから評価関数を学ばせる前に要るのは、**退けが commit を支配する仕組み**(CommitStage の側)と、候補の木(読み)。olmX の計器は、その仕組みを入れた後に「学んだ価値が図を読んでいるか記憶を読んでいるか」を検査する側に回る(穴の検出 = 等半径の図で真になる前提が一般の図に残っているか)。
4. **言えないこと**: 60 行ずつの札で、評価関数の「学習可能性」は測っていない。上の 1〜3 は olmX の値(退けの率・b2_j07 の型・MIDO3 → EQ・等半径の対照)から引いた読みで、自己対戦の輪を実際に回した結果ではない。

## §5. 第二計器(Opus 5.5 xhigh・26 点 → 79 項目・[RESULT](RESULT_second_instrument_opus55_xhigh_20261104.md))

- 取れない物 **0**(15 URL すべて HTTP 200・自分で取り直し・`data/second_instrument/MANIFEST.tsv`)。**語・数・単位の食い違い 0**。
- 一致の内訳: 文字どおり(改行と空白だけ違う)66 / 正規化で一致 7(撇号の曲がり・二重の曲がった引用符を一重で書いた 'chasing its tail'・'loop'・PDF の下付きと行末のハイフンの抽出 "fθ (s)"・"sT"・"finetuning")/ 画像を目で読んで一致 5(損失と PUCT の式・10^7 visit・TD-Gammon の表の gif・AlphaZero の Table 1)。
- 食い違い **1**(引用の形): 一便 "Policy iteration is a classic algorithm" ← 原文 "Policy iteration 20, 21 is a classic algorithm"(agz_ucl 412 行)= 引用番号を「…」なしで落とした(語の違いではない)。
- 行番号のずれ 2(#78 174 → 173・#122 296 → 298 = 一便の行番号は pdftotext 既定の text の行で、MANIFEST が書く -layout の text の行と合わない)。
- SOURCE の二つの数は逐語で在る: [25:57]「28勝2敗」(435 行)・概要欄「18勝2敗」(29 行)= 動画の中の不一致は字幕の file で確か。Wikipedia「Tic-tac-toe」に 255,168 / 5,478 は無く 765 / 26,830 は在る・「AlphaGo Zero」の $25 million の注 [15] = Gibney(doi:10.1038/nature.2017.22858)。
- 言えないこと(第二計器): ars2023 と wp_AlphaGo_Zero は一便と md5 が違う(生きた頁・逐語はどちらにも在り・差の中身は見ていない)。HTML の行番号は変換が違うので比べていない。音声は聞いていない。

## §6. 言えないこと

- Nature 2016 の本文・Science 2018・Nature News 2017 は取れず(3,000 万手・2,500 万ドルは L2 のみ)。第 10 章の人物の発言は Wikipedia 止まり(元の記事は取っていない)。
- 作者の測定(四目並べの AlphaZero 型・MCTS の 5 条件・三目並べ)は一次資料に無く、概要欄と本文の照合だけ。再現はしていない(先生の発注に無い)。
- 28 勝 2 敗(25:57)が ASR か原稿かは音声を聞かないと分けられない。
- §3・§4 は主 session の読み(L3)。動画の結論「読みと答え合わせから」は動画の言葉(論文の演算子の言い換え)で、論文の逐語ではない(Q2 i)。

## §7. 置き場

- この folder: SOURCE・BRIEF 二本・RESULT 二本・`data/agentA/`(一次 38 本 + text 化・MANIFEST.tsv・3 MB 超の PDF 3 本は .gitignore)・`data/agentA_queries/`・`data/agentA_scripts/`・`data/agentA_meta/`・`data/second_instrument/`・`data/second_instrument_scripts/`。
