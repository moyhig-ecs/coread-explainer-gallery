# RESULT(札 `neq1`): moy-5 × 夏休みエッセイに「等長だけでは足りない」の注釈 — Opus 5.5 の事前検証 = 判定 NONE(2026-10-19 未明・実行層)

- 札 = [PREREG](PREREG_neq1_moy5_essay_not_equal_length_note_20261019.md)(凍結 `ec7cfa84`)・書いた時の HEAD = `ec7cfa84`(pull 済み・`R1`)。
- 走行 = zebrashark・`launch_neq1_20261019.sh claude-opus-5-5`・00:45:16 開始 → 01:09:53 終了(約 25 分)・呼び出し 110・HTTP の誤り 0・**見積り $9.25**(上限 $20)・入力 757,610 / 出力 310,738 token。出力 = `ConstructGap/exp/results_neq1_moy5_20261019_claude-opus-5-5_{k,a,b,c,d}.jsonl`(取り直しの回 `_r` は 0 行 = 全単位に text)。
- **身分**: §1〜§2 = 札の計器の写し(`L1`・runner の `--read` と同じ数を手元でも再計算)。§3 = 実行層の reason-read(腕を伏せて読んだ・`L1` の逐語 + 分類は `L3`)。§4 = 読み(`L3`・採否は先生)。

## §1. 関門と判定(凍結の `verdict()`)
- 読み取り器 v2 の較正 = 72 / 72(発火の前に assert)。
- **K(陽性統制)= bind 9 / 10 → 関門(≥ 8)を通過**。凍結の門 GENUINE-CUT 8。ただし **cut を答えの欄に書いたのは 1 / 10**(答えの欄は 10 / 10 が等長、cut は理由の欄)。
- **判定 = NONE: no arm reaches 4 / 20**(K 以外の五つの腕で bind 0 / 20)。

## §2. 表(K 以外は各 n 20・全単位に text)
| 腕 | bind(v2) | cut を答えの欄 | 床(等長) | 答えの欄に等長(式) | bind(v1) | to_read | 凍結の門 |
|---|---|---|---|---|---|---|---|
| K | **9** / 10 | 1 | 10 | 10 | 9 | 1 | GENUINE-CUT 8・FALSE-STRUCT 1・CLOSURE 1 |
| A | 0 | 0 | 20 | 13 | 0 | 19 | CLOSURE 16・TRAP 3・FALSE-STRUCT 1 |
| A-neq | 0 | 0 | 20 | 16 | 0 | 20 | TRAP 13・CLOSURE 6・FALSE-STRUCT 1 |
| E-full | 0 | 0 | 20 | 15 | 0 | 12 | TRAP 13・CLOSURE 4・WORD-CUT 2・FALSE-STRUCT 1 |
| E-neu | 0 | 0 | 20 | 19 | 0 | 16 | TRAP 19・CLOSURE 1 |
| E-neq | 0 | 0 | 20 | 12 | 0 | 16 | TRAP 10・CLOSURE 5・FALSE-STRUCT 3・WORD-CUT 2 |

記述(判定に使わない)= 答えの欄の語(正規表現・`L1` の数え):

| 腕 | parabola | F P_y / focal | directrix | 全文に mean proportional |
|---|---|---|---|---|
| A | 0 | 2 | 0 | 0 |
| **A-neq** | **10** | **12** | **10** | 0 |
| E-full | 7 | 9 | 7 | 2 |
| E-neu | 7 | 15 | 5 | 0 |
| E-neq | 3 | 8 | 3 | 1 |

## §3. reason-read(PREREG §3・腕を伏せて 83 本を全部読んだ・bind には足さない)
- **83 本すべてで、答えの欄は等長 \|EJ\| = \|KPy\|**(多くが「both also equal FPy」「P_y lies on the parabola with focus F and directrix e」を添える)。比例中項を不変量として答えの欄に書いたものは 0。
- 理由の欄で比例中項の仕組みに言葉で触れたもの = 3 本(伏せを解いた後の腕と逐語):
  - E-full r14: 「in local coordinates, the ordinate squared equals 4·FV times VH (the mean-proportional relation).」= 放物線の symptoma(縦線の平方 = 4·FV·VH)を理由の一段に置いた形。
  - E-full r15: 「Through P_x on h1, the right angle at P_x on the ray F→P_x gives a mean-proportional relation, the 'ordinate squared = product of segments' construction.」= エッセイの言い回し(§8「ordinate squared equals product of two segments」)の写し。
  - E-neq r15: 「With the vertex of that right angle at P_x, the altitude and mean-proportional relation gives s_K - s_{P_y} as a quadratic expression in the height of P_x.」
- 三本とも凍結の門は WORD-CUT(語はあるが式として読めない)。A・A-neq(エッセイ無し)には 0 本。

## §4. 読み(`L3`・採否は先生)
- **Opus 5.5 では、エッセイ・注釈・その両方のどれでも、答えは等長の床から動かなかった**(床 20 / 20 が全腕)。先生の仮説(文脈内学習で汎化された推論鎖を合成する)の形(H-ICL)は、この model・この配置では出なかった。
- **注釈は答えを動かしたが、行き先は cut ではなかった**: 問いの側の注釈(A-neq)で、答えの欄の半分(10 / 20)が「等長 + P_y は焦点 F・準線 e の放物線上(PyF = PyK)」に広がった。問いが挙げる関係の型(equal length / a distance relation / collinear / a right angle / **on a curve**)の中で、「等長だけでは足りない」→「on a curve を足す」と読んだ形。比例中項は、問いの型の一覧に無い。
- エッセイの中に埋めた注釈(E-neq)では、この広がりは小さい(parabola 3 / 20・E-full 7 / 20 より少ない)= 長い文脈の中の一文は効きが弱い。
- エッセイは比例中項の**語**を理由の欄に運んだ(E-full 2 本・E-neq 1 本・エッセイ無しは 0)が、不変量として答えの欄に上げるところまでは行かない。K でも答えの欄に cut を書いたのは 1 / 10 = Opus は「最も重要な不変量」を答えの欄に等長で書き、比例中項を理由に回す癖が強い。
- 否定の汚染(「等長」の語が等長を呼ぶ)の兆しは、答えの欄の等長の式の数では一様でない(A 13 → A-neq 16 / E-neu 19 → E-neq 12)= この札からは言えない。

## §5. 次(採否は先生)
- **Fable 5.5 が出たら、同じ札を追い札で**(runner の MODELS・PRICE・CAP_USD の 3 行だけ)。比べる物 = この Opus の表。
- 記録として気づいたこと(`L3`): 床から外す鍵は「注釈を置く場所」より、問いの**関係の型の一覧**にある可能性。一覧に無い型(比例中項)へは、注釈で床を塞いでも行かず、一覧の別の型(on a curve)へ移る。問いを替える線は、この札の約束(問いは替えない)の外なので、やるなら別の札で(arg5 の Bbp = 問いが cut を求める版で Argon 20 / 20 との対照になる)。
