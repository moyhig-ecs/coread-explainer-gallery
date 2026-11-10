# PREREG(追い札 neq2f): 札 neq2 を Fable 5.1 xhigh で — moy-5 × Principia 第 I 巻 補助定理 XIV(名だけ / 本文)・`claude -p`

- 日付: 2026-10-19(月)夜・zebrashark・実行層(Opus 5.5)/ 書き始めの HEAD = `1a87e346`
- 発注(逐語): 先生 10-19 夜「Newtonのプリンキピアを読んだopusはmoy-5を解けていないですよね？」→(実行層が neq2 の結果を答えた)→「fable-5.1-xhighでサブエージェントにかけてみます。」
- 親 = [PREREG neq2](PREREG_neq2_moy5_principia_lemma14_name_or_text_claude_p_20261019.md)(凍結 `232cd2d1`)。**§1〜§7(腕・本文・問い・読み取り器・関門・判定・余白)はすべて親のまま。** 違いは下の §1 だけ。
- **凍結の実体**: 本書と runner `ConstructGap/exp/l14_moy5_claude_p_fable51_xhigh_20261019.py`(親の runner の写し・違いは 5 行 = 札の名・本書の path・MODEL・RUNROOT・`--effort`)を一つの commit に。runner の `guard_frozen()` が dirty なら走らない。

## §0. 事前に知っていること(開示)
- 親の結果(Opus 5.5・effort high・MacBook)= 判定 NONE / K 10 / 10・A 0・L-name 0・L-text 1(/ 20)/ 答えの欄の cut 0 / reason-read 55 本 = 答えの欄は全部等長・本文は配置を移した(L-text 9 / 20)・名だけは補助定理 XIV が等長を生むと誤って結んだ(L-name 7 / 20)= [RESULT neq2](RESULT_neq2_moy5_principia_lemma14_name_or_text_claude_p_20261019.md)。
- 経路の確かめ(本書の前・1 回): 空の folder で `claude -p "Reply with the single word OK." --model claude-fable-5-1 --effort xhigh …` → init の model = `claude-fable-5-1`・答え "OK"・API の単価で換算 $0.59(Claude Code の起動の文脈の費用が大きい)。moy-5 の問いは見せていない。

## §1. 親からの違い(これだけ)
| 項 | 親 neq2 | 本札 neq2f |
|---|---|---|
| model | `claude-opus-5-5` | **`claude-fable-5-1`** |
| effort | high | **xhigh** |
| 機械 | 自宅 MacBook | **zebrashark**(Claude Code 2.1.292) |
| 出力 | `results_neq2_moy5_20261019.jsonl` | `results_neq2f_moy5_20261019.jsonl` |
| 一時の置き場 | `/private/tmp/claude-501/neq2_run` | `/private/tmp/claude-501/neq2f_run` |

腕と本数(K 10 → 関門 ≥ 8 → A・L-name・L-text 各 20)・workers 4・読み取り器 v2(較正 72 / 72)・判定の規則(余白 3 / 20)は親のまま。

## §2. 手順(launcher が順に)
`--fire --units K:10 --workers 4` → `--gate`(落ちたら止まる)→ `--fire --units A:20,L-name:20,L-text:20 --workers 4` → `--read`。その後、親と同じ型で腕を伏せた reason-read(分類 = 実行層の読み `L3`)。

## §3. 主張しないこと
- 親と本札は model・effort・機械が同時に違う = 差を model だけに帰さない。
- 費用は Claude Code の枠(Max 20x・Fable の週の枠)で、API の単価の換算は参考。
- 一つの問い(moy-5)・一つの本文(Motte 1846 の英訳の補助定理 XIV)。
