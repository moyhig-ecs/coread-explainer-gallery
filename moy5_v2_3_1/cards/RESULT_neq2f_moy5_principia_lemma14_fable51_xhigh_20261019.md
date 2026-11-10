# RESULT(追い札 `neq2f`): 札 neq2 を Fable 5.1 xhigh で — 判定 NAME-ONLY(名だけが cut を引いた・本文は配置を移したが cut は書かない・答えの欄は 60 / 60 等長)(2026-10-19・実行層)

- 札 = [PREREG neq2f](PREREG_neq2f_moy5_principia_lemma14_fable51_xhigh_20261019.md)(凍結 `4634d512`)・親 = [RESULT neq2](RESULT_neq2_moy5_principia_lemma14_name_or_text_claude_p_20261019.md)(Opus 5.5)。書いた時の HEAD = `4634d512`(fetch 済み・origin の先 3・遅れ 0・`R1`)。
- 走行 = zebrashark・`claude -p`(空の folder・道具なし・`--model claude-fable-5-1 --effort xhigh`)・18:31:44 → 18:54:55・70 本・誤り 0・permission の拒否 0。費用 = Claude Code の枠(API の単価での換算 $28.64 = K 5.62・A 6.65・L-name 8.28・L-text 8.09)。wall の中央値 = K 108.5 s・A 49.1 s・L-name 72.7 s・L-text 67.7 s(最長 137 s)。thinking token の中央値 = K 8,569・A 3,707・L-name 5,125・L-text 5,095。
- 出力 = `ConstructGap/exp/results_neq2f_moy5_20261019.jsonl`(70 行・md5 `f54d5897`)。腕を伏せた読みの材料 = [data_neq2f_reasonread/](data_neq2f_reasonread/)(伏せた本文 `83c50079`・鍵 `fe80921c`・分類 `c8d1f3bd` = 伏せを解く前に書いた)。
- **身分**: §1 = 計器の写し(`L1`)。§2 = 腕を伏せた reason-read(逐語 = `L1`・分類 = 実行層の読み `L3`)。§3 = 事後の数え(`L2`・PREREG に無い)。§4 = 読み(`L3`・採否は先生)。
- ⚠ 親と **model・effort・機械が同時に違う**(PREREG §3)。差を model だけに帰さない。

## §1. 関門・表・判定
- 読み取り器 v2 の較正 72 / 72。**K = 9 / 10 → 関門通過**(≥ 8)。答えの欄に cut は 7 / 10(「EJ = KP_y = FP_y = FPx² / FV」の型)。
  - K r9 の 1 本は答えの代わりに道具の呼び出しの文面(Bash で数値の検算をしようとした・道具は切ってある)を返した = gate OTHER。その中の検算の式は FPx² と FV·FPy を比べていた(cut を知っている)。

| 腕 | bind(v2) | 答えの欄に cut | 床(等長) | 答えの欄に等長 | Newton の語・字 | to_read |
|---|---|---|---|---|---|---|
| K | 9 / 10 | 7 | 9 | 9 | 1 | 0 |
| A | 0 / 20 | 0 | 20 | 20 | 0 | 7 |
| L-name | **7** / 20 | 0 | 20 | 20 | 15 | 5 |
| L-text | 0 / 20 | 0 | 20 | 20 | 16 | 10 |

**判定 = NAME-ONLY**(凍結した規則のまま: 名は余白 3 / 20 を越えて床から動かし、本文は動かさない)。launcher の出力の文言「the name retrieves, the text does not add (unexpected — report as is)」。

## §2. reason-read(腕を伏せて 41 本 = to_read・Newton の語・bind のどれかに当たる答え)
- 手順: 41 本を種 20261019 で混ぜ、X01〜X41 の名で答えと理由だけを並べた(腕・回の番号は鍵の file へ)。分類を file に書いてから鍵を開けた。
- ⚠ **伏せは部分的**: 本 RESULT の前に L-name の bind 7 本の逐語を腕を知って読んでいた。bind の 7 本は中身で見分けられる。
- **答えの欄は 41 本すべて等長 |EJ| = |KP_y|**(多くは「= |FP_y|」= 焦点距離を添える)。
- 分類(`L3`・上から優先の排他)と、伏せを解いた後の腕:

| 分類 | 計 | A | L-name | L-text |
|---|---|---|---|---|
| cut を問いの字で書いた(bind) | 7 | 0 | **7** | 0 |
| (a) 補助定理 XIV の配置を問いの字へ移した(P_x = 焦点からの垂線の足・h1 = 頂点の接線・m = 接線・系 3) | 21 | 0 | 5 | **16** |
| (p) 放物線(焦点 F・準線 e・頂点 V)とは言うが補助定理 XIV は言わない | 6 | 0 | 5 | 1 |
| 放物線も言わない(相似・座標だけの証明) | 7 | **7** | 0 | 0 |
| (b) 比例中項を Newton の字のまま書いた | 0 | 0 | 0 | 0 |
| (c) 補助定理 XIV が等長を生むと誤って結んだ | **0** | 0 | 0 | 0 |

- 横断の印(上の排他とは別に数えた):
  - Newton の字との対応を明示(S = F・A = V・N = P_x・P = P_y・O = H の全部か一部): **5**(すべて L-text)。
  - cut を EJ に繋いだ: 3(すべて L-name・bind の中)。例「FP_x² = FV·FP_y = VE·EJ」。EJ = FP_y と FV = VE から正しく出る式で、(c) の誤りではない。
  - (c) の境目: 1 本(L-name r11)が等長を「Newton の補助定理 XIV(FP_x² = FV·FP_y)の背後にある焦点距離の関係」と呼んだ。cut は正しく書いており、親の (c)(「補助定理 XIV が等長を生む」)とは違う。0 に数えた。
- 逐語(腕は伏せを解いた後):
  - L-name(bind): 「(This is Newton's Lemma XIV setting: FP_x^2 = FV·FP_y = VE·EJ.)」/「P_y lies on the parabola with focus F, directrix e, axis j, vertex V (and m is its tangent, Px the foot of the focal perpendicular, giving Newton's Lemma XIV relation FPx² = FP_y·FV).」— 答えの欄はどちらも |EJ| = |KP_y|。
  - L-text(a・字の対応): 「P_y is on the parabola with focus F, directrix e, axis j, vertex V (Newton's Lemma XIV configuration with S=F, A=V, N=P_x, P=P_y, O=H).」/「(Newton's Lemma XIV setting: F = S, V = A, P_x = N, P_y = P, H = O)」
  - L-text(a・系 3): 「(Newton's Lemma XIV: the foot P_x of the focal perpendicular on a tangent lies on the vertex tangent h1)」
  - A(放物線なし): 「Because HJ ∥ DE with H on j and J on g, triangle VHJ is similar to the isosceles triangle VDE, hence VH = VJ and therefore EJ = VE + VJ = VD + VH = DH.」

## §3. 事後の数え(`L2`・PREREG に無い・正規表現 `parabol|directrix|focal (radius|distance|perpendicular)` と `Lemma\s*XIV` を全 70 本の出力に)
| 腕 | 放物線の語(Fable / 親 Opus) | 「Lemma XIV」(Fable / 親 Opus) |
|---|---|---|
| K | 0 / 1 | 0 / 0 |
| A | 1 / 3 | 0 / 0 |
| L-name | **20** / 7 | 12 / 15 |
| L-text | 18 / 16 | 16 / 18 |

- 名だけで、Fable は 20 本すべてが作図を放物線(焦点 F・準線 e・頂点 V)と見た。名が無いと 1 / 20。親の Opus は名だけで 7 / 20。
- 親の数は親の RESULT に無かった数え。同じ正規表現をこの場で二つの jsonl にかけた。

### §3b. 事後の数え(`L2`): FV の固定と二次式(先生 10-19 夜「FVが固定長だっていう記述がある出力はありますか？」「FVが固定長だと認識できないと、等比中項から二次式は出ませんよね？」)
- **文で書いた出力は 0 本**: 「FV は固定・一定・与えられた長さ」も、系 2 の形(FP_x² ∝ FP_y・「SA is given」)も無い。Fable・Opus とも同じで、本文に系 2 がある L-text でも 0 本。
- **座標で FV を文字に置き、二次式を書いた出力はある**: Fable 12 本(K 0・4・6 / A 3・4・12・15・17・18 / L-name 1・5 / L-text 9)、Opus 1 本(K 0)。
  - 型は「P_x = (a, p) と置く → P_y = (a − p²/a, 2p)・VH = p²/a」。
  - L-name r5 は「y² = 4a(a − x)」と書いた。
  - L-text r9 は「a = FV と t = HP_y と置くと、VH = t²/(4a)」と書いた。これは HP_y² = 4·FV·VH、つまり Menaechmus の symptoma(latus rectum = 4FV)そのもの。
  - ただし読み取り器 v2 には見えない(a・p・t は点の名でない)。
  - Opus の他の当たりは、座標の数値の検算(KP_y² ≈ 128.71)だった。
- ⇒ 「固定」は、座標の文字を選んだ時点で黙って済んでいる(Descartes の道)。「SA は与えられている」と言葉で判断し、比例を曲線の symptoma として読む道(Menaechmus・Newton の系 2)は、言葉としては出てこない。

## §4. 読み(`L3`・採否は先生)
1. **名だけで cut が理由の欄に出た(7 / 20)。中身は正しい**。親の Opus は名だけで「補助定理 XIV が等長を生む」と誤って結んだ(7 / 20)。Fable は同じ名で、放物線の同定(20 / 20)→ 補助定理 XIV の関係を問いの字で(7 / 20)まで進み、誤った結び付けは 0。ただし model・effort・機械が同時に違う。
2. **本文は配置を移したが、cut は書かなかった**(L-text: (a) 16 / 20・字の対応の明示 5・bind 0)。本文を見せた答えが使ったのは系 3(焦点からの垂線の足は頂点の接線の上にある)。これは m が接線であること、つまり等長の証明に要る部分。比例中項(cut)は等長の証明に要らないので書かれない。名だけだと、補助定理 XIV の看板の中身(比例中項)が同定の札として出てくる。この二つの差が NAME-ONLY という判定の中身、と読む。
3. **答えの欄は 60 / 60 で等長**。親の §3-3 の読み(cut は問いの点の集合 {E, J, K, P_y} に入らない)がそのまま当てはまる。Fable の 3 本は cut を EJ に繋いだ式(FP_x² = FV·EJ)まで書いた。cut と答えの等長が一つの式に入った最も近い形だが、理由の欄の中に留まった。
4. **本文が足さなかったことを「本文は効かない」とは読まない**。L-text の 16 本は本文の配置を正しく問いへ写し、5 本は字の対応表まで書いた(写像は起きている)。判定の物差し(bind = cut を問いの字で)が測るのは cut だけ。本文の効き目は (a) の側に出た。
5. ⇒ 親の §4 の 2 × 2(本文の有無 × 問いの集合 {E, J, K, P_y} / {F, V, P_x, P_y})は、Fable でも同じく要る。今回、答えの欄は model を替えても動かなかった。

## §5. 次(採否は先生)
- 2 × 2 の札(問いの集合を cut の点に向ける)を Opus と Fable の両方で。
- 親との差を model に帰すなら、effort と機械を揃えた札が要る(Opus 5.5 xhigh を zebrashark で、または Fable 5.1 high を)。
- 「名は同定の札として看板の中身を、本文は証明に要る部分を引く」(§4-2)は、ConstructGap の「名前の飛び込み」の反対側の実例の候補。→ 先生 10-19 夜「読みは記録してください」→ memory `project_name_retrieves_headline_text_retrieves_proof_part_neq2f_20261019` に記録した。
