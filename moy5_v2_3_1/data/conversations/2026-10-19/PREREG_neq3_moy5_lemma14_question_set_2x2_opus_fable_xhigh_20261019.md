# PREREG(札 neq3): 問いの点の集合 × 補助定理 XIV(名 / 本文)— moy-5・Opus 5.5 と Fable 5.1・同じ effort(xhigh)・同じ機械・`claude -p`

- 日付: 2026-10-19(月)夜・zebrashark(Claude Code 2.1.292)・実行層(Opus 5.5)/ 書き始めの HEAD = `4dd28348`
- 発注(逐語): 先生 10-19 夜「Fable 5.5が出ると信じてちょっと待つか、先に2×2の札を走らせて、5.5と比較するか？」→(実行層の推し = 先に凍結して走らせる)→「走らせます。あとFVが固定長だっていう記述がある出力はありますか？」
- 親 = [neq2](PREREG_neq2_moy5_principia_lemma14_name_or_text_claude_p_20261019.md)(Opus 5.5 high・MacBook)・[neq2f](PREREG_neq2f_moy5_principia_lemma14_fable51_xhigh_20261019.md)(Fable 5.1 xhigh・zebrashark)。読み = [RESULT neq2](RESULT_neq2_moy5_principia_lemma14_name_or_text_claude_p_20261019.md) §3-3・[RESULT neq2f](RESULT_neq2f_moy5_principia_lemma14_fable51_xhigh_20261019.md) §4・memory `project_name_retrieves_headline_text_retrieves_proof_part_neq2f_20261019`。
- **凍結の実体**: 本書・runner `ConstructGap/exp/l14_moy5_2x2_qset_claude_p_20261019.py`・launcher `ConstructGap/exp/launch_neq3_20261019.sh` を一つの commit に。runner の `guard_frozen()` は、本書・runner・本文の file のどれかが dirty なら走らない。
- Fable 5.5 が出たら、runner の `MODELS` に一行足す追い札(先生の合図で)。

## §0. 事前に知っていること(開示)
1. neq2 / neq2f の結果: 答えの欄は 120 本すべて等長 |EJ| = |KP_y|。cut は理由の欄だけ(Fable の名だけの腕 7 / 20・Opus の本文の腕 1 / 20)。読み = cut は問いの点の集合 {E, J, K, P_y} に入らないので、答えの欄に居場所が無い。
2. **先生の問い「FV が固定長だという記述はあるか」への答え**(本書の前に、neq2 / neq2f の 140 本を検索):
   - 文で「FV は固定・一定・与えられた長さ」と書いた出力は **0 本**。
   - Fable の 11 本(K 2・A 3・L-name 4・L-text 2)と Opus の 1 本(K)は、座標の計算で FV(= VE = VD)を a・d・v などの文字に置いた。暗に定数として扱っているが、言葉にはしていない。
   - 系 2 の形(SN² は PS に比例 = FP_x² ∝ FP_y・「SA は与えられている」)は **0 本**。本文を見せた L-text(本文に系 2 がある)でも 0 本。
   - この問いは本札の記述用の数え(§5)に入れる。
3. 6 月の `A1_construct`(問いの集合 {P_x, V, F})は P_y を含まない = cut を書けない集合だった(Opus n 10・genuine cut 0・[DATA](../2026-06-25/DATA_moy5_pconstruct_runs_20260625.md))。本札の Q2 は P_y を含む初めての集合。
4. 経路の確かめ(本書の前・各 1 回・moy-5 の問いは見せていない): Fable 5.1 xhigh(neq2f の §0)/ Opus 5.5 xhigh(空の folder・init の model = `claude-opus-5-5`・答え "OK"・換算 $0.22)。
5. `--dry` の値: Q1 md5 `ee39ba02`・**Q2 md5 `123ea1ac`**・K block2 md5 `ad9a50e1`・腕の prompt の md5 = K `b0b1d14b`・A `ee39ba02`・L-name `22fb0a29`・L-text `ef3fd8be`(この 4 つは neq2 / neq2f と同じ)・K/Q2 `eb6a33e7`・A/Q2 `123ea1ac`・L-name/Q2 `a1df0681`・L-text/Q2 `cd78f2d5`。読み取り器 v2 の較正 72 / 72(「∠FPxPy = 90° and ∠FVPx = 90°」と「Py lies on the parabola…」は cut でない = 較正の行に在る)。
6. Q2 の問いは、凍結の前にどの model にも見せていない。

## §1. 設計
- **問いの集合**: Q1 = 凍結した moy-5 の open prompt。Q2 = Q1 の一行「Focus on the relation that holds among the following objects: {E, J, K, P_y}.」の集合だけを **{F, V, P_x, P_y}** に替えた。座標・作図・前提・答えの型は同じ(E・J・K の座標も残る)。
- **腕**(K n 10・ほか n 20):

| | なし | 名だけ | 本文 | 陽性統制 |
|---|---|---|---|---|
| Q1 {E, J, K, P_y} | A | L-name | L-text | K |
| Q2 {F, V, P_x, P_y} | A/Q2 | L-name/Q2 | L-text/Q2 | K/Q2 |

  - 名 = 「Cf. Newton, Principia, Book I, Section III, Lemma XIV.」・本文 = Motte 1846 の英訳の補助定理 XIV(命題・証明・系 1〜3・md5 `06b869e5`)= neq2 / neq2f と同じ。
  - K/Q2 = Q2 + essay4 の K block の「for E, J, K, P_y」を「for F, V, P_x, P_y」に替えたもの。
- **model**: `claude-opus-5-5` と `claude-fable-5-1`。effort は両方 **xhigh**。機械は両方 zebrashark。
  - Opus は 8 腕すべてを引く(140 本)。
  - **Fable の Q1 の 4 腕は引かない**。neq2f の出力(md5 `f54d5897`・同じ model・effort・機械・経路・prompt)を読む。runner が md5 と prompt の md5 を確かめる。Fable が新しく引くのは Q2 の 4 腕(70 本)。
- 経路 = neq2 / neq2f と同じ(空の folder・道具はすべて切る・MCP なし・`--setting-sources local`・`--no-session-persistence`)。workers は model ごとに 4、二つの model を並走。

## §2. 測るもの
- **主: 答えの欄の cut(`cut_ans`)** = 読み取り器 v2 が conjecture の欄に CUT か SIM-CUT を読んだ行の数。
- 副: bind(答え全体に CUT / SIM-CUT)・答えの欄の等長(`equal_ans`)。
- 記述用(判定に使わない・§5): 放物線の語(全体 / 答えの欄)・**FV の固定の記述**(正規表現で候補を拾い、目で裁く)・系 2 の形・Newton の語。

## §3. 関門(陽性統制・`R6`)
- K/Q2 の bind ≥ 8 / 10(両 model)。Opus は K の bind ≥ 8 / 10 も(Fable の K は neq2f の 9 / 10)。
- 関門で落ちた model は残りの腕を引かずに止め、報告して新しい札にする。

## §4. 判定(凍結・model ごと・余白 3 / 20 = `R3`)
1. **QSET**: A/Q2 の cut_ans ≥ 4 かつ A/Q2 − A ≥ 3 → YES(問いの集合を cut の点に向けるだけで、cut が答えの欄に入る)。
2. A/Q2 ≥ 17 なら **Q2 CEILING**(Q2 の上で名・本文の効き目は測らない)。そうでなければ:
   - **NAME@Q2**: L-name/Q2 ≥ 4 かつ L-name/Q2 − A/Q2 ≥ 3 → YES。
   - **TEXT@Q2**: L-text/Q2 ≥ 4 かつ L-text/Q2 − A/Q2 ≥ 3 → YES。
3. **NAME×QSET / TEXT×QSET**(交互作用): (Q2 の腕 − A/Q2) − (Q1 の腕 − A) ≥ 3 → YES。
4. どれかの腕(K 以外)が 18 本未満なら INCOMPLETE。

## §5. 判定の後の読み(記述・`L2` / `L3`)
- 腕を伏せた reason-read(neq2f と同じ手順: 種で混ぜ・鍵を別の file に・分類を書いてから開ける)。対象 = Q2 の腕で、cut_ans・bind・放物線の答え・Newton の語・FV の固定の候補のどれかに当たる行。分類 = 答えの欄の cut の形 / 自明な直角(∠FVP_x・∠FP_xP_y は作図で与えられている)/ 放物線(曲線の上)/ その他。
- FV の固定の記述: 候補の文を全部写し、「FV が P_x によらない長さだと述べたか」を目で裁いて数える。
- Opus の Q1(xhigh・zebrashark)と neq2(high・MacBook)の差は、effort と機械の差として記述だけ(判定にしない)。

## §6. 予想(発火の前に書く・当たり外れは RESULT に)
- P1: QSET は両 model で YES。Q2 では ∠FVP_x = ∠FP_xP_y = 90° が作図で与えられていて、△FVP_x ∼ △FP_xP_y(= cut)は一段で出る。
- P2: Fable は Q2 CEILING になりうる(五分五分)。
- P3: Q2 で cut と答えの欄を争うのは「P_y は焦点 F・頂点 V の放物線の上」(曲線の上)と、自明な直角。名は neq2f で放物線を 20 / 20 で呼んだので、**L-name/Q2 は答えの欄が放物線に寄り、cut_ans が A/Q2 より下がる**かもしれない。
- P4: TEXT×QSET は分からない(本文は証明に要る部分を引く、という読みが当たるなら、Q2 では比例中項が証明に要るので本文が効く側に出る)。

## §7. 主張しないこと
- Q2 は問いを替えた別の項目で、moy-5 そのものではない。
- 一つの作図・一つの本文(Motte 1846)。
- Fable の Q1 は neq2f の出力(同じ条件・約 1 時間前)。引き直していない。
- 費用は Claude Code の枠(Max 20x)。API の単価の換算は参考(見込み 210 本 ≈ $90)。

## §8. 手順(launcher)
- Opus: `--fire K:10,K/Q2:10` → `--gate --arm K` と `--gate --arm K/Q2`(どちらかが落ちたら止まる)→ `--fire A,L-name,L-text,A/Q2,L-name/Q2,L-text/Q2` 各 20。
- Fable: `--fire K/Q2:10` → `--gate --arm K/Q2` → `--fire A/Q2,L-name/Q2,L-text/Q2` 各 20。
- 二つを並走 → 両方が終わったら `--read`。
