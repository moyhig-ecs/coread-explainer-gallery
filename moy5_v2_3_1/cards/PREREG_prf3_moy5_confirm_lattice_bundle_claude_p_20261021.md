# PREREG(札 `prf3`): prf2 の事後の読みの確かめ — 焦点・準線を塞ぐと、格子(頂点の比例中項ほか)を持ち出して P_y の式まで束ねる・同じ prompt の新しい標本・Opus 5.5 / Fable 5.1・effort max・`claude -p`(MacBook)

- 発注(逐語): 先生 10-21「進めます」(prf2 の RESULT §6 の確かめの札)。
- 実行 = MacBook(Claude Code 2.1.299・`claude -p`・購読の経路)/ 実行層 = Opus 5.5。書き始めの HEAD = `927a81ca`(`R1`・fetch 済・origin と同じ)。
- **凍結の実体**: 本書と runner `ConstructGap/exp/prf3_moy5_confirm_lattice_bundle_claude_p_20261021.py` を一つの commit に。runner は prf2 の runner(凍結 `e8efe2a3`・その中で prf1 の runner `d492ac0b`)と prf2 の事後の script(`927a81ca`・否定の言及の NEG)を import し、読み取り器・線分の類・FD の関係を使う。どれも触らない。`guard_frozen()` は五つの file(本書・prf3・prf2・prf1・事後の script)のどれかが dirty なら走らない。
- 親 = [RESULT prf2](RESULT_prf2_moy5_proof_block_focus_directrix_claude_p_20261021.md) §5(事後の読み: 格子から P_y の式へ束ねた行 = prf1 P5 Opus 2・Fable 0 → prf2 P5B Opus 9・Fable 5)。
- 札: `L1` = 実出力 / `L3` = 読み。

## §0. 問い
prf2 §5 の事後の読み(「近道を塞ぐと格子を選び、式まで束ねる」)が、**分け方を先に凍結した上で、新しい標本でも出るか**。

## §1. 腕(同じ prompt・新しい標本・各 model n 10)
| 腕 | prompt | md5 | 前の札 |
|---|---|---|---|
| **P5** | Bbp + PROOF(塞がない) | `31387680…` | prf1 の P5 と同じ |
| **P5B** | Bbp + PROOF + BLOCK(焦点・準線を塞ぐ) | `d8172a5c…` | prf2 の P5B と同じ |
| **R2** | (生成しない)prf1 + prf2 の 80 行を prf3 の述語で読む | — | **述語を作った集合**(確かめには数えない) |

- 経路・model・effort・timeout・workers・disallow は prf1 / prf2 と同じ。

## §2. 述語(凍結・生成の前・`L1`)
- 文 = 理由の欄を prf2 の ORDER と同じ規則で切る(「. ; の後の空白」)。
- **VMP** = END の関係で、縦の類の線分が VP_x(頂点の比例中項: `VP_x² = FV·VH`・`VH/VP_x = VP_x/FV`)。
- **SYM_PY** = END の関係で、縦の類の線分が HP_y か DK(P_y の式: `HP_y² = 4·FV·VH`・`DK² = 4·VD·VH`)。
- **LAT** = VMP、または END でない CUT(焦点の比例中項 `FP_x² = FV·FP_y`・`KP_y·FV = FP_x²` …)、または SIM-CUT。
- **FD_USE** = 理由の欄の文で、FD の関係(prf1 の `is_fd`)か FD の言葉(prf1 の正規表現)を含み、**否定の言及(NEG: without / not using / neither / nor / not used …)を含まず**、最初の SYM_PY の文より前にある(SYM_PY の文が無ければどこでも)。
- **LAT_SYM(主)** = SYM_PY ∧ LAT ∧ ¬FD_USE。
- **ORDER2**(記述)= 最初の LAT の文 ≤ 最初の SYM_PY の文。
- 較正(凍結前・全部通過): 23 項 = FD_USE 6(**否定の言及の陰性統制 4**・陽性 2)・VMP 3・SYM_PY 3・LAT 4・LAT_SYM 5・ORDER2 2。prf2 の較正(ORDER・MALFORMED・prf1 の 29)も通過。
- 分母: 主の率は ok の行(全部)で数える。副として MALFORMED を除いた行の率も記す。

## §3. 予想(確かめ・`R3` = margin)
- **H1(主)**: P5B の LAT_SYM − P5 の LAT_SYM ≥ 4(Opus)・≥ 2(Fable)。
- **H2**: P5B の LAT_SYM ≥ 6 / 10(Opus)・≥ 3 / 10(Fable)。
- **H3**: P5 の FD_USE ≥ 7 / 10(両 model)= 塞がないと焦点・準線の道で証明する。
- **H4**: P5B の FD_USE ≤ 2 / 10(両 model)= 塞ぎは放物線の証明の中で守られる。
- 当たり外れは数で書く。外れても述語は動かさない(`R4`)。

## §4. 統制と止まる条件
- 計器: 凍結前の較正(§2)。R2(述語を作った集合)での数は記述として並べるだけ。
- 止まる条件: guard の不通過・同じ err が 3 本。

## §5. 限界
- n 10・一題・二つの文面・effort max だけ。同じ日・同じ CLI の版。
- FD_USE は「P_y の式より前」の文を見る。前半の「不変量の理由」の節に FD の等式を書いた行(prf2 の P5BK に多い)は FD_USE になる(保守側 = LAT_SYM を少なく数える方向)。
- NEG は否定の語の有無だけを見る。否定の語を含む文の中で FD を使った行は落ちる(LAT_SYM を多く数える方向)。
- ORDER2 は文の順の近似。

## §6. 手順
1. `--self-test`(済)→ 本書と runner を一つの commit に(凍結)→ push。
2. `--r2`(読むだけ)→ `--fire`(既定の units = opus:P5:10・opus:P5B:10・fable:P5:10・fable:P5B:10)→ `--read`。
3. RESULT = `conversations/2026-10-21/RESULT_prf3_moy5_confirm_lattice_bundle_claude_p_20261021.md`(`R1`)。
