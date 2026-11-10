# PREREG(札 `prf2`): moy-5 — 焦点・準線の道を塞ぐと、証明は格子(比例中項・相似)を通って放物線の式へ進むか + 導出の向きの述語(ORDER)・Opus 5.5 / Fable 5.1・effort max・`claude -p`(MacBook)

- 発注(逐語): 先生 10-21「次へ進みます」(prf1 の RESULT §7 の二つの候補 = 焦点・準線の道を塞ぐ腕・導出の向きの述語)。
- 実行 = MacBook(Claude Code 2.1.299・`claude -p`・購読の経路)/ 実行層 = Opus 5.5。書き始めの HEAD = `a04fcf7c`(`R1`・fetch 済・origin と同じ)。
- **凍結の実体**: 本書と runner `ConstructGap/exp/prf2_moy5_proof_block_focus_directrix_claude_p_20261021.py` を一つの commit に。runner は prf1 の runner(凍結 `d492ac0b`)を import し、述語(`score5`・較正 29 項)・Bbp・K の hint・PROOF をそのまま使う。prf1 の file は触らない。`guard_frozen()` は本書・prf2 の runner・prf1 の runner のどれかが dirty なら走らない。
- 親 = [RESULT prf1](RESULT_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md)(証明を求めると焦点・準線の道で閉じる。格子は通らない: LATX Opus 2・Fable 0 / 比例中項を渡すと CHAIN 10・9)。
- 札: `L1` = 実出力 / `L3` = 読み。

## §0. 問い
1. 焦点・準線の等式を使えなくすると、**格子の関係を自分で持ち出して**放物線の式まで閉じるか(P5B)。
2. 塞いだ上で比例中項を渡すと、塞がれた証明が閉じるか(P5BK = 塞ぎの陽性統制)。
3. prf1 の CHAIN の行は、格子の関係から式を導いているか(式を先に書いて、格子を後から添えていないか)= ORDER(R1)。

## §1. 腕(新しい生成は P5B と P5BK・各 model n 10)
| 腕 | prompt | md5 |
|---|---|---|
| **P5B** | prf1 の P5(Bbp + PROOF)+ BLOCK | `d8172a5c…` |
| **P5BK** | prf1 の P5K(Bbp + K の hint + PROOF)+ BLOCK | `8d7e8b1d…` |
| **R1** | (生成しない)prf1 の 40 行を ORDER で読み直す | — |

- BLOCK(逐語): " Do not use the fact that P_y is equidistant from F and from the line e: do not use P_yF = P_yK, and do not use that m is the perpendicular bisector of FK. Derive the equation from other relations among the given points."
  - 中点(P_x は FK の中点)・長方形・相似は塞がない。頂点の道(相似 → VP_x² = FV·VH → HP_y = 2·VP_x → HP_y² = 4·FV·VH)は、塞いだ後も開いている(prf1 の Opus P5 r2 がこの形)。
- 経路・model・effort・timeout・workers・disallow は prf1 と同じ(`claude -p`・空の folder・`--setting-sources local`・MCP なし・38 の道具を disallow・`--effort max`)。

## §2. 数え方(`L1`)
- prf1 の述語をそのまま: cut3・END・LATX・CHAIN・FD・PARA・floor・答えの欄の版。
- 新しい述語:
  - **ORDER** = 「conjecture || reason」を `||` と「. ; の後の空白」で文に切り、LATX の関係が最初に出る文の番号 ≤ END の関係が最初に出る文の番号。
  - **CHAIN_ORD** = CHAIN ∧ ORDER。
  - **LAT_ROUTE(P5B の主)** = CHAIN ∧ ¬FD(格子を通って式に届き、焦点・準線の等式を書いていない)。
  - **END_NO_FD** = END ∧ ¬FD。
  - **PB_WORD** = 「perpendicular bisector」の語(記述)。
  - **MALFORMED** = JSON の答えが無い・本文に tool の呼び出しの書式(記述・prf1 §1 の型)。
- 較正: ORDER 6 項(正 3・負 3)+ MALFORMED 3 項 + prf1 の 29 項 = 全部通過(self-test・凍結前)。

## §3. 予想(実行層・発火の前・`R3` = margin)
- **Q1(塞ぎは守られる)**: P5B の FD ≤ 3 / 10(各 model)。
- **Q2(塞ぐと格子が増える)**: P5B の LATX ≥ prf1 の P5 の LATX + 3(Opus ≥ 5・Fable ≥ 3)。
- **Q3(主)**: P5B の LAT_ROUTE は Opus ≥ 3 / 10・Fable ≥ 1 / 10。
- **Q4(塞いでも、格子を渡せば閉じる)**: P5BK の LAT_ROUTE ≥ 7 / 10(各 model)。
- **Q5(R1・導出の向き)**: prf1 の P5K の CHAIN の行のうち ORDER が成り立つ行は、Opus ≥ 8 / 10・Fable ≥ 7 / 9。

## §4. 統制と読み方の約束
- **gate**: P5BK の LATX ≥ 8 / 10(渡した関係を読む)。下回った model の P5BK は読まない。
- **Q4 が外れた model**(P5BK の LAT_ROUTE < 7)では、P5B の低い LAT_ROUTE を「格子を持ち出せない」と読まない。塞ぎが証明そのものを難しくした可能性を先に書く。
- 止まる条件: guard の不通過・同じ err が 3 本。tool の呼び出し(init の tools は空のはず)が出たら記す。

## §5. 限界
- ⚠ **FD の述語は「書いたか」で、「使ったか」ではない**。BLOCK の文が P_yF = P_yK を含むので、「P_yF = P_yK を使わずに」と言及しただけでも FD が立つ。RESULT で FD の立った P5B / P5BK の行の本文を読み、使った / 言及だけを手で分ける(`L3`・数は凍結の述語のまま並記)。PB_WORD も同じ。
- ORDER は文の順の近似。一つの文に両方あれば成り立つ。文の切り方(小数点は切らない・略語は切る)に依る。
- n 10・一題・一つの BLOCK の文面・effort max だけ。prf1 とは同じ日・同じ CLI の版・同じ経路で、prompt の差は BLOCK の一文。

## §6. 手順
1. `--self-test`(済)→ 本書と runner を一つの commit に(凍結)→ push。
2. `--r1`(読むだけ)→ `--fire`(既定の units = opus:P5B:10・opus:P5BK:10・fable:P5B:10・fable:P5BK:10)→ `--read`。
3. RESULT = `conversations/2026-10-21/RESULT_prf2_moy5_proof_block_focus_directrix_claude_p_20261021.md`(`R1`)。
