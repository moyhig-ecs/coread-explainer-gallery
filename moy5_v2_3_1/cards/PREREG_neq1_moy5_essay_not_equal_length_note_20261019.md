# PREREG(札 `neq1`): moy-5 × 夏休みエッセイに「等長だけでは足りない」の注釈 — cut は問いではなくエッセイの側から来るか(Opus 5.5 で事前検証・2026-10-19)

> **先生(10-19・逐語)**: 「夏休みエッセイに「等長ではない」という注釈を埋め込むとmoy-5がcutするのか確かめるアイデア。」→「お願いします。来週は、もう日本だと今週か、Fable 5.5が出ると言われていますので、Opus 5.5で事前検証の準備をしましょう。」
> **仮説(先生・逐語)**: 「既存のLLMの推論は般化が高レベルに達しつつあり、文脈内学習によって、汎化された推論鎖による合成を行うる仮説」
> **HEAD**(`R1`・fetch の後): `39e21c49`。**凍結の実体**: 本書・runner [`ConstructGap/exp/essay_neq_moy5_20261019.py`](../../ConstructGap/exp/essay_neq_moy5_20261019.py)・launcher [`ConstructGap/exp/launch_neq1_20261019.sh`](../../ConstructGap/exp/launch_neq1_20261019.sh) を一つの commit に入れてから走らせる(runner は札と script が commit と違えば走らない)。
> **先生の裁定(10-19・逐語)**: 「Aで。notではなくinsufficientで。」= §2-3 の注釈は **案 A**(「〜だけでは不十分」の型)。

## §0. 事前に知っていること(開示)
- 札 essay4(10-14・凍結 `2189bc95`)の RESULT の要約: moy-5 の cut は K を除く 16 cell で **0 / 317**(Opus 5.5 の A・E-abs・E-full・E-full2 も 0)・K(関係を渡す統制)は 20・20・20・19・床 \|EJ\| = \|KPy\| は 19〜20 / 20。判断層 10-14「問いが {E, J, K, Py} の等長を指す限り、cut を書く動機が無い。これを分けるには、問いの側で cut を要求する腕が要る」。
- 札 arg5(10-16): 問いが cut を求める Bbp で Gemini 4 Argon が 20 / 20。
- moy-5 の凍結の open prompt は、関係の型の例を「equal length / a distance relation / collinear / a right angle / on a curve」と挙げる(等長が先頭)。
- エッセイ §11 は同じ作図を説明し、「as long as an ordinate is a mean proportional」と書くが、E・J・K の字は出ない。
- essay4 の Opus の答えの本文は、この session では読んでいない(要約と表だけ)。

## §1. 仮説を測れる形に
先生の仮説が成り立つなら、**エッセイ(文脈の材料 = 作図と「縦線は比例中項」)を読み、床(等長)を注釈で塞がれた model は、問いの字(E・J・K・Py はエッセイに無い)で比例中項(cut)を合成する**。そこで 2 × 2 で、エッセイの寄与と注釈の寄与を分ける:

| | 注釈なし / 中立 | 注釈 NEQ(床を塞ぐ) |
|---|---|---|
| エッセイなし | **A**(凍結の open prompt) | **A-neq**(問いの側に注釈) |
| エッセイあり | **E-full**(essay4 と同一)・**E-neu**(中立の注釈を同じ所に) | **E-neq**(注釈をエッセイ §11 に) |

- E-neq が A-neq より多く cut する = エッセイ(文脈)が要る。E-neq が E-neu・E-full より多い = 注釈が要る。両方 = 仮説の形(H-ICL)。

## §2. 宇宙
1. **model** = `claude-opus-5-5`(事前検証)。呼び出しは凍結の経路(`essay_arm_moy1.one` → `models.call`: adaptive thinking・effort high・max_tokens 12,000)。**Fable 5.5 は、公開されたら追い札で足す**: 変えるのは runner の 3 行(MODELS・PRICE・CAP_USD)だけ・先生の合図が要る。
2. **問い** = moy-5 の凍結の open prompt(md5 `ee39ba02…`・問いは替えない)。エッセイ = v1.0(zenodo.22218057・md5 `5f1dd954…`)。枠 = essay1 の FRAME。
3. **注釈**(エッセイ §11「…all drawn by the same construction that sold me the conics book [1].」の直後に一つだけ挿す・anchor は本文に一回だけ):
   - **案 A(採用・moy-1 の凍結の封鎖の一文と同じ型)**:
     - E-neq: `(Note: merely stating an equality of lengths is insufficient.)`(md5 `746e34f0…`)
     - A-neq(問いの末尾): `Note: merely stating an equality of lengths is INSUFFICIENT.`(md5 `2d3b24ea…`)
     - E-neu(中立・同じ所・同じ形): `(Note: merely redrawing this figure with another apex is unnecessary.)`(md5 `90d3b5e5…`)
     - 推す理由: moy-5 では等長 \|EJ\| = \|KPy\| は**成り立つ**。「等長ではない」と書くと偽の文を読ませることになる。moy-1 の封鎖も「〜だけでは不十分」の型。
   - **案 B(不採用・先生「notではなくinsufficientで」)**: `(Note: the invariant here is not an equality of lengths.)` ほか。偽の文になる点と、否定の汚染(下)の両方が強く出うる。
   - **否定の汚染**(memory 対偶汚染・RTA の N0): 「等長」の語そのものが等長を呼び込む向きがありうる → E-neu と A を対照に置き、`equal_in_conjecture`(答えの欄に等長)を記述として並べる。
4. **腕と n**: K 10(陽性統制・関門)/ A・A-neq・E-full・E-neu・E-neq 各 20 = 110 回。prompt の md5(dry): K `b0b1d14b…`・A `ee39ba02…`・A-neq `fff2c7c7…`・E-full `04ed287c…`(essay4 と byte 一致)・E-neu `166ab678…`・E-neq `115f5a39…`。
5. **取り直しの規則** = text の在る単位は取り直さない・無い単位は一度だけ(essay4 と同じ)。

## §3. 採点
- **この札の bind = 読み取り器 v2 の `cut`**(`exp/moy5_relation_reader_v2_20261014.py`・凍結 `e07c3abd`・答えの欄と理由の欄を合わせた文 = 凍結の門が読む範囲)。
- 併記: `cut_in_conjecture`(答えの欄だけ)・床 = 凍結の `closure_parabola_section`(等長)・`equal_in_conjecture`・凍結の門(2026-06-24)・読み取り器 v1 の bind(essay4 の数と並べる)・FALSE2・語の数。
- reason-read: 比例中項の語があるのに読み取り器が関係を読めなかった答え(`to_read`)は、腕を伏せて実行層が全部読み、逐語を RESULT に載せる。**bind の数には足さない**。

## §4. 陽性統制と関門(R6)
1. 走る前に、読み取り器 v2 の較正(CAL 72 / 72)を runner が assert(落ちたら一回も呼ばない)。
2. **K を先に 10 回**。**K の bind ≥ 8 / 10 でなければ、他の腕は走らせない**(計器か書き手が今日は働いていない)。

## §5. 判定(凍結・runner の `verdict()`・余白 = 3 / 20・R3)
- **H-ICL**(仮説の形): E-neq ≥ 4 / 20 ∧ E-neq − A-neq ≥ 3 ∧ E-neq − E-neu ≥ 3 ∧ E-neq − E-full ≥ 3。
- **NOTE-ONLY**: A-neq ≥ 4 / 20 ∧ \|A-neq − E-neq\| < 3(注釈だけで足り、エッセイの寄与は余白に届かない)。
- **NONE**: どの腕も 4 / 20 に届かない。
- **MIXED**: 上のどれでもない → 表をそのまま報告し、読みを足さない。
- いずれかの腕が 18 行未満なら INCOMPLETE。記述(判定に使わない): 否定の汚染(`equal_in_conjecture`・床の数を A / E-neu と A-neq / E-neq で並べる)・注釈の場所の差(A-neq 対 E-neq)・v1 と v2 の差。

## §6. 費用
見積り ≈ $14(Opus 5.5 = $4 / $20 per MTok・エッセイの腕 60 回 × 約 $0.15・エッセイなし 50 回 × 約 $0.1)。**上限 $20**(単位ごとに側の log から見積もって止める)。

## §7. 主張しないこと
model の内部で何が起きたかは言わない(振る舞いの数だけ)/ 1 項目・1 model(事前検証)で、一般化しない / エッセイは 2026-09-01 から公開(後の学習に入りうる)/ 「文脈内学習による合成」は、H-ICL の形が出ても**振る舞いの上での一致**であって、機構の証明ではない。

## §8. 走らせ方
zebrashark: `bash ConstructGap/exp/launch_neq1_20261019.sh claude-opus-5-5`(K → 関門 → 四つ並走 → 取り直し → `--read`)。出力 = `ConstructGap/exp/results_neq1_moy5_20261019_claude-opus-5-5_*.jsonl`・側の log = `ConstructGap/exp/logs/neq1_*`。RESULT = `conversations/2026-10-19/RESULT_neq1_moy5_essay_not_equal_length_note_20261019.md`。
