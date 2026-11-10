# SUMMARY: moy-5(放物線の切り口)の cut —— 腕・effort・経路・model の横断のまとめ(2026-10-16 時点・Gemini 4 Argon を加えた版)

- 日付: 2026-10-16(金)15 時台 / 実行層 = Opus 5.5。監査 = 判断層(judge-cold・Fable 5.1・effort xhigh)。講評は先生。
- 先生(逐語): 「moy-5のまとめを作成し、fable-5.1-xhighで監査」
- HEAD `8e048b2c`(書く前に `git pull --rebase` = Already up to date)。
- 身分: `L1` = 実出力(一つの計器で読み直した数)/ `L3` = 実行層の読み。
- 前の版: `conversations/2026-10-15/SUMMARY_moy5_cut_across_arms_effort_route_20261015.md`(judge-cold の監査 2 回で I1〜I8 合・§10 に rte1)。本版はそれに札 `arg5`(10-16)を足した。§2〜§4 の Claude の数は前の版と同じ(同じ file・同じ読み取り器)。
- 数の出所(M1): `ConstructGap/exp/summary_moy5_cut_all_cards_20261016.py --check`(読むだけ・API なし)の出力を `conversations/2026-10-16/data_moy5_summary/summary_table_moy5_cut_all_cards_20261016.txt`(md5 `556b9dfb`・script md5 `523c3d0c`)に置いた。監査(§11)の後に、script の使い方の行(docstring の file 名)を直して出し直し、r8 の述語の `--calibrate` の出力を末尾に足した(数は監査の前の版 md5 `fa40c729` と同じ)。
  - script は 10-15 の版(`summary_moy5_cut_all_cards_20261015.py`)の写しに、三つだけを足したもの = arg5 の読み元(`results_arg5_20261016_*.jsonl`・route API・effort high)・`gemini-4-argon` の短い名(Argon)・一本あたりの関係の数の中央値の二列(全部の関係 / CUT と SIM-CUT)。10-15 の版は変えていない。
  - r8 の述語(md5 `dfe5b0d0`)は 10-15 と同じ。較正の出力は M1 の末尾の節(b5bp 120 行で当たり 4・新しい cut は r8 だけ / essay4 A・E-full 157 行で 0)。走らせた時点で 10-16 の script は未 commit。
  - Argon の行ごとの関係の一覧 = `conversations/2026-10-16/data_moy5_summary/arg5_read_per_row_relations_20261016.txt`(arg5 の runner の `--read` の出力・md5 `59913db1`)。

## §0 moy-5 と数の定義
- 問い(凍結の `X.OPEN["moy5"]`):
  - 円 c・外の点 C からの接線・…・h1 の上の点 P_x から P_y を作る構成。
  - 役の束縛は {E, J, K, P_y}。「P_x がどこにあっても成り立つ不変量を一つ」答える。
- **床** = 凍結の不変量 |EJ| = |KP_y|。答えの欄で `closure_parabola_section` が閉じる。
- **cut** = 読み取り器 v2(`moy5_relation_reader_v2_20261014`)が CUT か SIM-CUT と読む関係が、答え全体(答えの欄 + 理由の欄)に一つでもあること。
  - CUT の定義 = 六つの位置で真・純粋な積と商の関係・区間の間の固定の比では説明できない。
  - 例: 比例中項 `FV·EJ = FP_x²`。
- **答えの欄の cut** = 同じ判定を答えの欄だけに。
- **cut + r8** = cut に、先生の r8 の裁定(10-14「1 cutに数えましょう。」)を機械にした述語を足したもの。
  - 述語 = v2 が ADDITIVE と読んだ `X·FV = FV² + VPx²` か `X = FV + VPx²/FV`(X ∈ {EJ, KPy})の形。
  - 実装 = `exp/moy5_r8_additive_predicate_20261015.py`。
  - 較正 = 10-14 の手の当てはめを再現した。
    - b5bp で当たるのは Opus Bbp の r6・r8・r16・r19 の 4 本で、新しく cut になるのは r8 だけ。
    - 基線は、10-14 の手の当てはめの 120 本(essay4 の A / E-full・三 model)を含む 157 本(Haiku 5.5 の 37 本を足した)で 0。
- **関係の数**(本版で足した列)= 読み取り器 v2 の `relations` が答え全体から拾った関係の数の、腕ごとの中央値。「CUT の関係の数」はそのうち CUT か SIM-CUT のもの。

## §1 読みの規則
1. 対象は moy-5 の 9 札(と rte1 の 2 file)の、答えのある全行。
   - API の経路: essay4・sym5・kfv1・b5bp(Claude)・**arg5(Argon・10-16)**。
   - Claude Code の経路: moy5t・moy5e・moy5h・moy5c(と rte1 の Claude Code の側・§10)。
   - 答えが空の行は数えない。Haiku 5.5 の essay4 で A 1 本・E-full 2 本(どれも max_tokens・essay4 の RESULT)。**Argon の arg5 で E-full+Bbp 2 単位(r13・r17)が二度とも `MAX_TOKENS`**(arg5 の RESULT §1・n 18)。
   - moy5t の行は、読み直しの file `results_moy5t_20261015_rescored.jsonl` から読む(moy5t の RESULT §0)。
2. 計器は全行で一つ: 字を替えた腕(@U)は名の対応表で元の名に戻し(`moy5_symbol_map.to_task_names`)、読み取り器 v2 で読む。
   - 各札の記録した bind と食い違うのは 1 本だけ(essay4 の Fable K r17・v1 → v2 の既知の差)。M1 の「--check」(arg5 を足しても 1 のまま)。
3. 腕は (札・腕の名・prompt の md5) で区別する。arg5 の 5 腕の md5 は親の札と同じ(A `ee39ba02`・E-full `04ed287c`・K `b0b1d14b` = essay4 / Bbp `be9c4007`・E-full+Bbp `8c875982` = b5bp・arg5 の PREREG §1 の dry)。
4. 札をまたいだ合算はしない。腕ごとの率は札ごとに出す。§5-1 の「1 / 717」は記述の総数で、率の合算ではない(Claude の行だけ・Argon は入れていない)。
5. 6 月の `A1_construct` は本表に入れない(essay4 の RESULT が「読み直して cut 0」と記す)。
6. 本表の model = **Claude の四つ(Haiku 5.5・Sonnet 5.5・Opus 5.5・Fable 5.1)と Gemini 4 Argon**。Argon は arg5 の 5 腕だけ(@U・KF・E-abs・E-full2・Claude Code の経路は無い)。
   - Argon の thinking は `thinkingConfig.thinkingLevel = HIGH`・`maxOutputTokens 12000`(arg5 の PREREG §2)。§2 の Claude の API の行は adaptive thinking・effort high・`max_tokens 12000`(§10 の API max は 64,000)。§2 の上限の token 数は同じだが、thinking の段の目盛りは vendor ごとに違う(§6)。
   - 6 月の走行(gemma の式)は本表の外。他社の model は Argon だけ。

## §2 API の経路(上限 12,000 token・`L1`)
cut / n(答えの欄の cut)。「—」= 取っていない。Claude = adaptive thinking・effort high / Argon = thinking high(arg5)。

| 腕(札) | 名替え | 要旨 | 全文 | 二往復 | 円錐の枠 | β′ | 比例中項 | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.1 | **Argon** |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|---|---|---|---|
| A(essay4 / arg5) | | | | | | | | 0 / 19 | 0 / 20 | 0 / 20 | 0 / 20 | **0 / 20** |
| A@U(sym5) | ○ | | | | | | | — | 0 / 20 | 0 / 20 | 0 / 20 | — |
| E-abs(essay4) | | ○ | | | | | | 0 / 20 | 0 / 20 | 0 / 20 | 0 / 20 | — |
| E-full(essay4 / arg5) | | | ○ | | | | | 0 / 18 | 0 / 20 | 0 / 20 | 0 / 20 | **0 / 20** |
| E-full2(essay4) | | | ○ | ○ | | | | 0 / 20 | 0 / 20 | 0 / 20 | 0 / 20 | — |
| E-full@U(sym5) | ○ | | ○ | | | | | — | 0 / 20 | 0 / 20 | 1 / 20 | — |
| KF(sym5) | | | | | 旧 | | | 0 / 20 | 0 / 20 | 0 / 20 | 0 / 20 | — |
| KF@U(sym5) | ○ | | | | 旧 | | | — | 0 / 20 | 0 / 20 | 0 / 20 | — |
| KF(kfv1) | | | | | v1 | | | 0 / 20 | 0 / 20 | 0 / 20 | 0 / 20 | — |
| KF@U(kfv1) | ○ | | | | v1 | | | — | 0 / 20 | 0 / 20 | 0 / 20 | — |
| **Bbp**(b5bp / arg5) | | | | | | ○ | | — | **2 / 20** | **6 / 20(+ r8 = 7)** | **0 / 20** | **20 / 20** |
| E-full+Bbp(b5bp / arg5) | | | ○ | | | ○ | | — | 0 / 20 | 3 / 20 | 1 / 20 | **18 / 18** |
| K(essay4 / arg5・陽性統制) | | | | | | | ○ | 20 / 20(15) | 20 / 20 | 20 / 20 | 20 / 20(1) | **20 / 20** |
| K@U(sym5・陽性統制) | ○ | | | | | | ○ | — | 20 / 20 | 19 / 20(1) | 20 / 20 | — |

星取りの列(○ = 足した・空欄 = 足していない・どの腕も凍結の問い(moy-5)が土台):
- **名替え** = 問いの七つの名を替えた(@U・読む時に元の名へ戻す)。
- **要旨 / 全文** = 夏休みエッセイ(どちらも essay1 の FRAME で包んで問いの前に置く)。**二往復** = 全文を読ませて三文に要約させ、次の回で問う。
- **円錐の枠** = 円錐の枠のヒント(旧 = sym5 の版・v1 = kfv1 の版)。
- **β′** = 理由の欄に「等長でない関係」を求める一文。
- **比例中項** = 比例中項の関係そのものを渡す一文(陽性統制)。

- 答えの欄の cut は、K と K@U の陽性統制(Haiku 15・Fable 1・Opus K@U 1)を除き、どの腕でも 0。Argon は K を含む 5 腕すべてで 0。
- 床(答えの欄の |EJ| = |KP_y|)は、ほとんどの腕で n と同じ数。欠けるのは Haiku の K 7 / 20・E-full 13 / 18・E-full2 18 / 20・E-abs 19 / 20 と、Sonnet の E-abs 19 / 20。Argon は 5 腕とも n と同じ。
- KF の札(sym5・kfv1)が測ったのは、手で読む「枠の運び」の梯子で、cut ではない(各札の PREREG)。本表の 0 は、それとは別の数。

### §2-2 一本あたりの関係の数(中央値・全部 / CUT・`L1` = M1 の二列)

| 腕 | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.1 | **Argon** |
|---|---|---|---|---|---|
| A | 2.0 / 0 | 1.0 / 0 | 2.0 / 0 | 3.0 / 0 | **8.5 / 0** |
| E-full | 2.0 / 0 | 1.0 / 0 | 5.5 / 0 | 7.5 / 0 | **8.0 / 0** |
| Bbp | — | 11.0 / 0 | 19.5 / 0 | 19.5 / 0 | **36.0 / 4.0** |
| E-full+Bbp | — | 17.0 / 0 | 23.0 / 0 | 24.0 / 0 | **58.5 / 9.5** |
| K(陽性統制) | 3.0 / 3.0 | 3.0 / 2.0 | 9.0 / 1.0 | 11.5 / 2.0 | **19.0 / 4.0** |

## §3 Claude Code の経路(`claude -p`・repo の外の空の folder・Opus 5.5 / Fable 5.1・各 n 10・`L1`)
すべて b5bp の Bbp(md5 `be9c4007` = 凍結の問い + β′)が土台で、腕で足す物が違う。Argon の行は無い(Claude Code は Claude だけ)。

| 腕 | β′ | 道具 v1 | 道具 v2 | 数値の表 | model | high | xhigh | max |
|---|:-:|:-:|:-:|:-:|---|---|---|---|
| P-none(moy5c) | ○ | | | | Opus | — | — | **10 / 10** |
| | | | | | Fable | — | — | **6 / 10** |
| P-tool(moy5t / moy5e) | ○ | ○ | | | Opus | 1 / 10 | 5 / 10 | **10 / 10** |
| | | | | | Fable | 0 / 10 | 2 / 10 | 4 / 10 |
| P-tool2(moy5h) | ○ | | ○ | | Opus | 1 / 10 | — | — |
| | | | | | Fable | 3 / 10(+ r8 = 4) | — | — |
| P-data(moy5t / moy5e) | ○ | | | ○ | Opus | 0 / 10 | 1 / 10 | **10 / 10** |
| | | | | | Fable | 1 / 10 | 1 / 10 | 6 / 10(答えの欄 2) |
| 参照: Bbp(b5bp・API・n 20) | ○ | | | | Opus | 6 / 20(+ r8 = 7) | — | — |
| | | | | | Fable | 0 / 20 | — | — |

星取りの列: **β′** = §2 と同じ一文(全部の腕に在る)/ **道具 v1** = 関係を数値で確かめる道具 / **道具 v2** = 同じ道具に、成り立った時の注(TRIVIAL / STATIC / EQUAL / DEGENERATE)を足した版 / **数値の表** = P_x を動かした数値の表。エッセイ・名替え・円錐の枠・比例中項は、§3 のどの腕にも無い。

- 答えの欄の cut は Fable max P-data の 2 本だけ。ほかは 0。床は Fable max P-none の 9 / 10 を除き全部 10 / 10。

## §4 cut の形と CAD の確定(`L1`・各 RESULT と CAD の RECORD から)
- 主な形(Claude):
  - 比例中項 `EJ·FV = FP_x²`・`KP_y·FV = FP_x²`・`FP_x² = FV·FP_y`。
  - V 側 `VH = VP_x²/VF`・`VJ·FV = VP_x²`。
  - D を使う形 `KP_y·FV² = DV·FP_x²`・`DH·DV = FP_x²`。
  - 相似の比 `KP_y = KP_x·FK/FD`。
  - 放物線の方程式の形 `HP_y² = 4·VF·VH`・`DK² = 4·VD·VH`・`VH = 2·VP_x²/FD`。
    - `HP_y² = 4·VF·VH` は 10-14 に既に出ている(b5bp の RESULT 付-A)。
    - moy5c(Opus r1・r3)では Bbp だけ(道具も表も無し)で出た。
- Argon(arg5 の `--read` の行ごとの関係の一覧・`L1`): Bbp と E-full+Bbp の行に `FPx² = FV·KPy`・`FPx² = EV·EJ`・`VPx² = FV·VH`・`HPy² = 4·FV·VH`・`△FVPx ∼ △KPxPy` などが並ぶ(どれも Claude の行に既にある形の族)。K の行では、`FPx² = FV·FPy` の形(・か * の書き方を含む)が 20 本とも読み取り器の関係に在る。読み取り器が `phrase: FPx = mean proportional of FV, FPy` を CUT か SIM-CUT の関係として拾ったのは 18 本(r10・r14 は除く)で、本文の字としての "mean proportional" は 20 本とも在る(行ごとの一覧 = §冒頭の `arg5_read_per_row_relations_20261016.txt`・行ごとの照合表 = `data_moy5_summary/arg5_K_rows_form_phrase_raw_check_20261016.tsv`(md5 `38ebe54b`・形 20 / phrase 何の種類でも 19 / phrase が CUT か SIM-CUT 18 / 本文の語 20)・10-16 の main の数え直し)。Argon の形を CAD で確かめることはしていない(§6)。
  - **例 = K の r10・r14**(先生 10-16 夕「置いて足す」・`L1`): 二本とも本文は「the mean proportional relation FPx^2 = FV·FPy」の言い方で、Argon の文は正しい。式の方は二本とも CUT として拾われている(cut は 20 / 20 のまま)。phrase の読みは、r10 では何も拾わず、r14 では中項を取り違えて `phrase: FPy = mean proportional of FPx, FV`(偽の形)と読み FALSE2 にした = **読み取り器の誤り**。`--read` の一覧は CUT・SIM-CUT・ADDITIVE の関係だけを載せる(runner l.124)ので、r14 の phrase は一覧に出ない。
- CAD の計器(Wolfram 15.0.1・`cad_verify_moy5_relations_20261015.wl`):
  - 較正 = 床と比例中項は ∀ で True・6 月の偽の式は False(成り立つ点 t = 0 と t ≈ 5.7815)。RECORD_cad_verifier §3。
  - moy5t の 2 形・moy5e の代表 6 形・moy5c の新しい 3 形が、どれも ∀ t で True・0 < r < d で恒等式。

## §5 言える事(記述・`L3` の読みは印をつける)
1. **API の effort high の Claude では、問いだけ・名を替えた問い・エッセイ・円錐の枠のヒントのどれでも、cut はほぼ 0。**
   - 該当する腕(K・K@U・Bbp・E-full+Bbp を除く API の 10 腕)の全部で 1 / 717(E-full@U の Fable 1 本)。Argon の A と E-full も 0 / 20 ずつ(この総数には入れていない)。
   - 床はほとんどの腕で 19〜20 / 20 で述べられる。
2. **関係そのものを渡すと(K・K@U)、五つとも答えの中で運ぶ(19〜20 / 20)。** 読み取り器の陽性統制。Argon も K で 20 / 20 = 計器は Argon の上でも立つ。
   - 答えの欄に書いたのは Haiku の K 15・Fable の K 1・Opus の K@U 1(§2)。Argon は 0。
   - ほかは理由の欄に書き、答えの欄は床のまま。
3. **理由の欄に「等長でない関係」を求める一文(β′)で、API の high でも Opus 7 / 20(r8 を含む)・Sonnet 2 / 20 になった。** Fable は 0 / 20。エッセイを前に置くと、Opus 3・Fable 1・Sonnet 0。
4. **Argon(thinking high)は β′ で Bbp 20 / 20・E-full+Bbp 18 / 18。** Claude の API の high の行(0〜7 / 20)より多い。この二つの腕の Argon の thinking の中央値は Claude の 2.6〜8.2 倍(§6 の表)で、数はこの量の差を含む。
   - ただし cut の定義は「答え全体に CUT が一つでもあれば」(§0)で、Argon は一本に並べる関係の数が、どの腕でも Claude より多い(§2-2: Bbp 36 対 11〜19.5・E-full+Bbp 58.5 対 17〜24)。一本の中の CUT の関係も中央値 4(Bbp)・9.5(E-full+Bbp)。
   - 同じ広さでも cut が割れる例が在る(`L3`): Fable の Bbp と Opus の Bbp は関係の数が同じ 19.5 で、cut は 0 / 20 と 6 / 20(+ r8 = 7)(§2-2・§2)。なので「関係を多く並べる model ほど cut になる」だけでは数を説明できない。Argon は β′ を足した時に列挙の中に CUT が入る、という記述まで(`L3`)。列挙の広さと CUT を見つけることを分けるには、関係の数あたりの率か、最初に挙げた関係だけを読む別の読みが要る(本版の読みの規則の外・§8)。
5. **Claude Code の経路では、effort を上げるほど cut が増えた。**
   - Opus: 道具 1 → 5 → 10・表 0 → 1 → 10(high → xhigh → max)。max は Bbp だけ(問い + β′・道具も表も無し)でも 10 / 10。
   - Fable: 道具 0 → 2 → 4・表 1 → 1 → 6。max の Bbp だけ 6 / 10。
   - max では、道具・表・何も無しの差は Opus で 0、Fable で 4〜6 の幅。
   - ⇒ この範囲で一番効いているのは effort(`L3`)。経路の交絡は rte1(§10)で一部を分けた。
6. **cut はほとんど理由の欄に書かれる。** 答えの欄は床(凍結の不変量)を答える。問いが「不変量を一つ」と求め、床がその答えだからと読める(`L3`)。答えの欄に cut を書いたのは、陽性統制を除くと Claude Code の Fable max P-data の 2 本と、rte1 の Fable の API max の 1 本(r2・rte1 の RESULT §1・§10)だけ。Argon も同じ形(答えの欄の cut は全腕 0・床は全行)。
7. xhigh と max では、Opus は Fable と同じか上(max の Bbp だけ 10 対 6)。
   - high では腕によって逆になる。P-data は Opus 0 対 Fable 1、P-tool2 は Opus 1 対 Fable 3(r8 を足して 4)。API の E-full@U も Opus 0 対 Fable 1。
   - Fable の一番高い数は 6 / 10(陽性統制を除く)。
8. **moy-1 との形の対応(`L3`・項目をまたぐ読み)**: moy-1 の Argon は「理由の欄では円を同定し(28 / 40)、答えの欄で約束しない(bind 0 / 40)」(10-15 の moy-1 の SUMMARY §2・API 既定の thinking)。moy-5 の Argon も「関係は理由の欄に厚く、答えの欄は床だけ」。答えの欄に置く物が最小、という向きは二つの項目で同じ。ただし moy-1 の Argon は thinking 既定(medium)、moy-5 は high で、条件が揃っていない(§6)。

## §6 限定
- **経路と effort の交絡**: §3 の Claude Code の札は、API と違う system の文脈で走った。rte1(§10)で Bbp だけの 2 × 2 を取ったが、ほかの腕(道具・表)は Claude Code だけ。
- **vendor をまたぐ effort の目盛り**: Argon の thinking high と Claude の effort high は同じ量ではない。thinking の中央値(token・Argon = arg5 の RESULT §2 / Claude = essay4 の RESULT §2-3・b5bp の RESULT §3):

  | 腕 | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.1 | Argon |
  |---|---|---|---|---|---|
  | A | 4,121 | 431 | 1,331 | 1,359 | 4,016 |
  | E-full | 8,233 | 1,522 | 2,282 | 3,367 | 3,284 |
  | Bbp | — | 1,030 | 1,753 | 2,233 | 8,494 |
  | E-full+Bbp | — | 1,740 | 2,369 | 3,525 | 9,110 |
  | K | 4,333 | 1,625 | 1,797 | 2,509 | 5,334 |

  Bbp と E-full+Bbp では Argon の thinking は Claude の 2.6〜8.2 倍(Bbp 3.8〜8.2・E-full+Bbp 2.6〜5.2)で、§5-4 の Argon の数はこの量の差を含む。E-full では Fable と同じ程度。token の数え方は vendor ごとに違う(比べられるのは桁まで)。
- **moy-1 との条件の違い**(§5-8): moy-1 の Argon(gem1・syc1)は thinkingConfig を送らない API の既定(medium)、moy-5 の Argon(arg5)は HIGH。
- **cut の定義と列挙の広さ**: §5-4。一本に多く並べる model ほど「一つでもあれば」に当たりやすい。本版は二つの数(関係の数・CUT の関係の数)を並べるまでで、補正はしていない。
- Claude Code の cell は n 10。§2 の API の cell は n 20(Haiku の A 19・E-full 18・Argon の E-full+Bbp 18)。§10 の API max の cell は n 10。
- 本表の model は Claude の四つと Argon。Argon は 5 腕だけ。ほかの他社の model と Claude 4.x の行は無い。
- 読み取り器 v2 は線分の関係しか読まない。
  - 言葉の形の比例中項(phrase)の読みは、「the mean proportional relation <式>」の言い方では、拾わない(Argon K r10)か、中項を取り違えて偽と読む(同 r14・FALSE2)ことがある(§4 の例)。二本とも同じ文の式が CUT として拾われるので、cut の数は変わらない。phrase だけで比例中項を書いた本では、cut を数え落とす向きに壊れうる(未確認)。
  - 座標の式(例: `y² = 4a(a − x)`)は cut に入らない。
  - b5bp の RESULT §3 には「座標の形」の記述の数(Opus Bbp で媒介 5・E-full+Bbp で式 5 / 媒介 6)がある。
  - 先生の r8 の裁定のほかに、座標の形を cut に数えるかは未決(b5bp の RESULT §3-1)。
- KF の腕の 0 は、その札の本来の測り物(手の読みの梯子)の数ではない。
- essay4 の RESULT の表は読み取り器 v1 の数。本表は v2(差は Fable K の 1 本)。
- Argon の形の CAD の確定はしていない(§4)。
- arg5 は bon1(local の llama-server・ollama)と同じ時間に zebrashark で走った。arg5 は API の札で、経路の干渉は無い(`L3`)。

## §7 前の記録との差
- 前の版(10-15 SUMMARY)との差: Argon の列(§2)・関係の数の表(§2-2・新しい列)・§5-4・§5-8・§6 の新しい限定(vendor をまたぐ effort の目盛り と thinking の表・moy-1 との条件の違い・cut の定義と列挙の広さ・Argon の形の CAD 未・bon1 の並走)・§1 の札と model の範囲。Claude の数は一つも変わっていない(M1 の 10-15 版と 10-16 版の Claude の行は同じ値・同じ script の写し)。
- arg5 の RESULT の訂正(10-16・本版を書く時): E-full+Bbp の CUT の関係の中央値は 9.5(RESULT の初稿の「10」は表示の丸め)・E-full の関係の数 8.0 を足した。
- 10-16 夕(先生「「何を足したか」の部分を星取り形式に分割できますか？」): §2・§3 の「何を足したか」「足した物」を星取りの列に分けた。§4・§5・§6・§8・§10 で「問いだけ」と書いていた所は Bbp(凍結の問い + β′)のことなので「Bbp だけ」に言い替えた(§5-1 の「問いだけ」= A はそのまま)。数は一つも変えていない。
- moy5h の Fable P-tool2: 読み取り器 v2 だけなら 3 / 10。r8 の述語を足すと r3 が加わって **4 / 10**(逐語:「HD = VD + VH = FV + VP_x^2/FV = KP_y」)。
- b5bp の Opus Bbp: v2 だけなら 6 / 20、r8 を足して 7 / 20(10-14 の RESULT は 7 と記す)。
- essay4 の Fable K: v1 で 19、v2 で 20(essay4 の RESULT に既に訂正がある)。

## §8 次に取れる物(採否は先生)
- arg5 の二走目の読み: 関係の数あたりの CUT の率・答えの理由の欄の最初の関係だけを読む(読みの規則を札に書いてから)。
- Argon の thinking を既定(medium)にして Bbp・K を取り直す(moy-1 の gem1 と条件を揃える)。 → **取った(札 arg5d・§12)**。
- Argon の形の CAD の確定(代表の形を Wolfram の計器で)。
- Fable の改版が出たら、moy5c(Bbp だけ × max)と b5bp(API high)で取り直す。

- **thinking の量の差を揃えた比較**(§5-4 の「Claude より多い」の言い方を、量の差 2.6〜8.2 倍を並べた上でどうするか)= **Fable 5.5 が出た時の課題**(先生 10-16 夕「量の差はFable 5.5が出たときの課題にしましょう。」)。本版の §5-4 の言い方はそのまま。

## §9 監査(10-15 版・judge-cold・Fable 5.1)
10-15 版の監査の記録(I1〜I8・指摘 9 点・再監査で全部合)は、前の版の §9 に在る。本版の監査は §11。

## §10 経路と effort を分ける対照(札 `rte1`・10-15 17 時台・前の版の §10 と同じ)
- RESULT = `conversations/2026-10-15/RESULT_rte1_route_effort_control_moy5_20261015.md`(凍結 `5fd3505d`・実費 $8.35)。
- Bbp だけ(問い + β′・md5 `be9c4007`)の 2 × 2(`L1`):

  | model | API high | API max | Claude Code high | Claude Code max |
  |---|---|---|---|---|
  | Opus 5.5 | 7 / 20 | **6 / 10** | **2 / 10** | 10 / 10 |
  | Fable 5.1 | 0 / 20 | **2 / 10**(答えの欄 1) | **3 / 10** | 6 / 10 |
  | 参照: Argon(arg5・API・thinking high) | **20 / 20** | — | — | — |

- 記述: effort を上げると二つの経路とも増え、max では Claude Code が API より 0.4 高い(交互作用の形・`L3`)。
- Opus の API high の 7 は r8 を含む数(v2 だけなら 6)。
- API max の cell は上限 64,000 token(stream)で、API high の 12,000 と上限も違う。rte1 の RESULT は「どの本も上限に届いていない」と書く。Argon の参照の行は上限 12,000(arg5)。

## §11 監査(10-16 版・judge-cold・Fable 5.1・effort xhigh)
- 基準 = `ConstructGap/judge_rubrics/audit_moy5_summary_v2.md`(v1 の I1〜I8 + Argon の分の I9・材料 M1〜M16)。
- 判定: **I1〜I9 すべて合**(既定の保留から)。数の転記は不一致 0(§2・§2-2・§3・§10・床と括弧の数・「1 / 717」= 317 + 260 + 140)。M1(10-16)と M1′(10-15)の Claude の 69 行は全部同値。
- 判断層の開示: 材料の中に前の監査の判定(10-15 版)が書かれていたが、見なかったものとして判定した。
- 直した点(監査の指摘 8 つ・重い順):
  1. §6「Claude の thinking の量は材料に無い」→ 誤り。essay4 と b5bp の RESULT の中央値を引いて表にした(Bbp・E-full+Bbp で Argon は Claude の 3〜8 倍)(→ 正しくは 2.6〜8.2・下の再監査の軽い指摘 1)。
  2. §4「K の行には … 20 本とも在る」→ 数え直して書き分けた(形は 20 本・読み取り器の phrase は 18 本・本文の語は 20 本)。行ごとの一覧を data に置いて指した。
  3. 冒頭・§0 の r8 の較正の出力 → M1 を出し直して末尾に節を足した。
  4. §7「§6 の三つの限定」→ 実際は五つ。列挙した。
  5. §5-8 の「(§6)」の指す文が無かった → §6 に moy-1 との条件の違いの一行を足した。
  6. §5-4 の「列挙の広さだけでは cut にならない」の支え → 同じ広さで割れる例(Fable と Opus の Bbp・19.5 で 0 対 6)に替えて `L3` を付けた。Argon の A(8.5)は「広い」例ではないので外した。
  7. §10 の API max の上限 64,000 → 一行足した。
  8. §1-1「9 札」と script の 10 の読み元(rte1 の 2 file)→「9 札(と rte1 の 2 file)」に。script の使い方の行も直した。
- 監査で確かめられなかった点(材料の外): txt と script の md5 の値・読み取り器 v2 の CUT の定義の中身・prompt の中身(md5 だけ)・§6「経路の干渉は無い」(`L3`)。
- 先生が読む時に確かめる点(判断層の挙げた三つ): §5-4 の「Claude より多い」を thinking の量の差を並べた上でも同じ言い方にするか・§4 の Argon の形の裏取りの置き場・§8 の二走目の読み(関係の数あたりの率・最初の関係だけ)の採否。
- 再監査(同じ基準・同じ agent・effort xhigh): 直した 8 点は全部「直った」。**I5 = 否**、ほかの I1〜I4・I6〜I9 は合。
  - 否の理由: §5-6「答えの欄に cut を書いたのは、陽性統制を除くと Fable max P-data の 2 本だけ」が §10 の「**2 / 10**(答えの欄 1)」(rte1 の Fable の API max r2)と食い違う。10-15 版の §5-5 から在った誤り(§10 を追補した時に §5 を直さなかった)。→ 「Claude Code の Fable max P-data の 2 本と、rte1 の Fable の API max の 1 本(r2・§10)だけ」に直した。10-15 版の §5-5 にも訂正の行を足した(元の文は残した)。
  - 軽い指摘 4 つ → 直した:
    1. §5-4・§6「3〜8 倍」→ 表から算すと 2.6〜8.2 倍(Bbp 3.8〜8.2・E-full+Bbp 2.6〜5.2)。上の直した点 1 の「3〜8 倍」も同じ誤り。
    2. §6「API の cell は n 20」と §1-6 の `max_tokens 12000` → §10 の API max(n 10・上限 64,000)を含まないので「§2 の API の」と範囲を書いた。
    3. §6 の moy-1 の Argon「(gem1)」→ moy-1 の SUMMARY の 0 / 40 は gem1 と syc1 の二札(どちらも thinking 既定)なので「(gem1・syc1)」に。
    4. §4 の「本文の字としての "mean proportional" は 20 本とも在る」の証拠が材料に無い → 行ごとの照合表(tsv・md5 `38ebe54b`)を置いて指した。数え直すと、phrase を CUT か SIM-CUT として拾ったのは 18 本(r10 は phrase 無し・r14 は FALSE2 と読んだ)・何の種類でも 19 本。
- 三度目の監査(直した所だけ・同じ基準・同じ agent・effort xhigh・材料に M17 = K の行の照合表 tsv と syc1 の RESULT を足した): **I5 = 合**。直した 5 点は全部「直った」で、新しい誤りは無し。§4 の K の行の文(M17)・10-15 版の §5-5 の訂正の行(M15 と照合)・moy-1 の「gem1・syc1・どちらも thinking 既定」も合。否・保留は 0。
  - 軽い指摘 4 つ → 直した: 上の直した点 1 の「3〜8 倍」に正しい数への指しを添えた / §4 の r14 が `--read` の一覧に出ない理由(一覧は CUT・SIM-CUT・ADDITIVE だけ = runner l.124)を書いた / §5-7「6 / 10」に「陽性統制を除く」/ §5-6 の r2 の出所を「rte1 の RESULT §1」に。
  - 判断層の開示: 依頼文と §11 に前の監査の判定が書かれていたが、見なかったものとして判定した。
  - 確かめられなかった点: md5 の値・tsv の本文の語の列の元の jsonl・arg5 の PREREG の `thinkingLevel = HIGH` の原本(依頼の範囲外)。
  - 先生が読む時に確かめる点(判断層の挙げた三つ): §5-4「Claude より多い」を thinking の量の差(2.6〜8.2 倍)を並べた上でも同じ言い方にするか / r14(本文の語は在るが読み取り器は FALSE2)を例として置くか、§6 の読み取り器の射程の限定に足すか / §8「Argon を thinking 既定で取り直す」の採否。
- **先生の裁定(10-16 夕・逐語)**: 「1 量の差はFable 5.5が出たときの課題にしましょう。2 置いて足す 3 残高的には取れますよね？」
  1. → §8 に置いた(§5-4 の言い方は今の版のまま)。TODO の Fable 5.5 の項にも足した。
  2. → r10・r14 を §4 に例として置き、§6 の読み取り器の限定に足した。読み直すと、r14 は Argon の誤りではなく読み取り器の取り違え(phrase の中項の役)だった。§4 の照合表(tsv)の数は変わらない。
  3. → Argon を thinking 既定で取り直す札(§8)の見積りを先生に出した(採否と上限は先生)。

## §12 追補(監査の後・10-16 夕): 札 `arg5d` = Argon の thinking の指定を送らない(既定)・K と Bbp × n 20
- RESULT = `conversations/2026-10-16/RESULT_arg5d_moy5_gemini4_argon_thinking_default_K_Bbp_20261016.md`(凍結 `78b722f9`・$0.40)。本節は judge-cold の監査(§11)の後に足した。§2〜§10 の数は変えていない。
- 数(`L1`): **K 20 / 20・Bbp 8 / 20**(答えの欄の cut 0・床 20 / 20・全部 `STOP`)。thinking の中央値 K 363・Bbp 1,005(high の arg5 は 5,334・8,494)。関係の数 / CUT の中央値 K 7.0 / 2.0・Bbp 15.5 / 0(arg5 は 19.0 / 4.0・36.0 / 4.0)。
- 読み(`L3`): §5-4 の Argon の Bbp 20 / 20 は thinking high の条件の数。既定では 8 / 20 で、Claude の API の high の Opus(6〜7 / 20)と同じ桁。thinking の量(1,005)は Sonnet の Bbp(1,030)と同じ程度。§6 の「vendor をまたぐ effort の目盛り」の限定は、この札で一部が数になった。
- §5-8 の moy-1 との対応(理由の欄に厚く・答えの欄は最小)は、thinking の条件を gem1・syc1 と揃えても同じ形(答えの欄の cut 0)。
