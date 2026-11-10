HEAD(R1) = 556c38fb(凍結時の HEAD = olm80 の凍結 32e1b4ad + 台帳の一行 = この file と runner を入れる commit の親)

# PREREG(札 `olm81`・凍結 2026-10-31): moy-5(線 2・P2-5)— 式だけで書かれた cut の文の手前は、同じ行の偽の出来事の手前より、層 48 の言語空間で cut の概念の語の集合へ寄るか(関係の名の側の計器で、式の行に届くか)

- 発注(逐語): 先生 10-31「zebrasharkの残件を勧めます。」「進めます。」(= 10-30 夜の報告の zebrashark の残り P2-4・P2-5)。P2-5 = `conversations/2026-10-29/PLAN_line1_line2_forward_and_claimable_scope_20261029.md` §2-5「式だけの cut の文(3 割)に届く計器」。
- G10 の欄: 比べる物 = 「式だけで書かれた cut の文の手前」/「同じ行の偽の出来事の手前」 / 計器 = olm74 Q2 と同じ d(J-lens 層 48 の CUT 対 FLOOR の語の集合の log Σ p の行の中の百分位の、本当の出来事の手前 32 − 偽の出来事の手前 32) / 雛形 = いいえ
- runner = [olm81_…py](../../ConstructGap/exp/olm81_moy5_formula_only_cut_rows_concept_set_runup_20261031.py)。保存の series を読むだけ(model なし・forward なし・API なし)。走らせる所 = zebrashark(MacBook でも同じ)。
- **形の選び(主 session・開示)**:
  - 下調べ(`conversations/2026-10-30/p25_prep/`)で、式の token の約 8 割は cut の文より前に出た token の写しだった → token 単位の式の計器は写しを測る見込みなので、**作らない**(将来の課題 = Opus 監査の E3)。
  - 代わりに、cut の関係の**名**(proportional・similar …= olm67 の CUT の集合)の側の計器が、式だけで書かれた cut の行に届くかを問う。これは語の計器と違い、cut の文に語が在ることを要らない。

## §0. 凍結の前に見た物(開示)

- olm74 Q2(O の 288 行の d): d > 0 が 192(0.667)・中央値 +0.0522。
  - model 別(olm74 Q4): Opus 79 / 114・+0.056 / Fable 113 / 174・+0.047。
  - 本札の C0 はこれを再現する。
- olm78 = その d の過半は語の積み上がり(r_W 0.575)・最終層では立たない / olm79 = 一語の計器は感度が足りない。
- p25 の下調べ:
  - 語の残らない行 118 / 366 の内訳。
  - 式の token の種類と写しの割合(81 % など)。
  - 例の cut の文(「Hence FP_x² = FV · FP_y for every t.」など)。
- 行の数(`--count`・値は読んでいない):
  - O の行 288 = **式だけ(F)98**(Opus 53・Fable 45)/ 語の在る行(W)190(Opus 61・Fable 129)。
  - L の行 75 = F 18・W 57。
  - F の札 × 腕(O): neq4 の W の 3 腕 25・moy5e 15・neq6 12・mnw1b 8・prf3 8・ほか 30。
- **F と W に分けた d の値は見ていない。**
  - 足し算の縛りは在る: pos_F + pos_W = 192(O の全体が既知なので)。
- 合成の自己検査(`--selftest` 5 / 5)は model も series の値も使っていない。

## §1. 行と計器(R5)

- 行 = olm67 の series の cut の行で、本当の出来事 t(cut の文の頭)と偽の出来事 q(olm68)の手前 32 が収まる物(= olm74 の行)。
  - 群: O = neq3 の L の腕(L-name/Q2・L-text/Q2)を除く / L = その腕。
- **F(式だけ)** = olm72 の series の meta で BODY の語(B0〜B2)が一つも無い行(olm72 §3 の「語の残らない行」の述語・raw_md5 で突き合わせる)。W = BODY の語が在る行。
- d = s(t) − s(q)。s = 窓の 32 位置の(u_CUT − u_FLOOR)の平均。u = 行の中の百分位(olm66 の pct)。

## §2. 統制(R6)

- **C0(写し)**: O の行の n・d > 0 の数・中央値が olm74 Q2(288・192・+0.05224254)と一致(1e−9)・olm72 と突き合わない行 0。✗ なら読まない。
- **C1(計器が立つ行の陽性統制)**: O の W の行(190)で d > 0 の行 ≥ 60 % かつ 符号検定 p < 0.05。✗ なら読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | 予想 |
|---|---|---|---|
| C1 | 語の在る行で d が立つか | 上の通り | 0.75 |
| Q1 | 式だけの cut の行(O の F・98)で d が立つか | d > 0 の行 ≥ 60 % かつ 符号検定 p < 0.05 | 0.50 |
| Q2 | model ごと(Opus 53・Fable 45) | Q1 と同じ型で model ごとに ✓ / ✗(総計しない) | Opus 0.40・Fable 0.35 |
| Q3 | F 対 W の中央値の差(置換 2,000・seed 8101・両側)・W の model 別・L の F / W | 記述 | — |

- L3(読み・確率つき): 「cut の概念の語への前触れは、cut を語で書くか式で書くかに依らない(式だけの行でも立つ)」p = 0.50。
  - 解ける条件: Q1 ✓ で真 / Q1 ✗ かつ Q3 の F < W(置換 p < 0.05)で偽。
  - それ以外は解けない。
- 動かす主張:
  - **Q1 ✓** → PLAN の記述「cut の文の約 3 割は式だけで書かれ、語の計器の射程の外」に、判定「概念の語の集合の前触れは、式だけで書かれた cut の文の手前でも立つ」を足す。線 2 の判定の一文の射程は式の行を含む。
  - **Q1 ✗** → 「式だけの行では線に届かない」。式の行は言えないのまま。Q3 で F < W なら、「線 2 の判定は主に語で書いた行に支えられる」を記述に足す。
  - token 単位の式の計器は、どの結果でも作らない(将来の課題)。

## §4. 止める規則

- C0 ✗ か C1 ✗ → 読まない。
- 1 回で打ち切る。F の述語・線を、結果を見てから替えない。
- 走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- F は「BODY の語が残らない」行(olm72 の規則)で、式を構文で読んだ物ではない(113 / 118 は 6 token 目以降に内容語が無い・5 は内容語が全部前 64 token に在る)。
- 前触れの語は、cut の文の前の本文に出た CUT の語の写しを含みうる(olm78 = 語の積み上がり)。式の行でも同じで、分けない。
- 因果・中の状態は言わない。frontier の本文を OLMo が読む時の話で、Opus・Fable の中の話ではない。
- Opus の F 53・Fable の F 45 は小さめ(R3 = 線の近くは境界として書く)。

## §6. 走らせ方

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm81_moy5_formula_only_cut_rows_concept_set_runup_20261031.py --selftest   # 凍結の前に通した・5 / 5
$P -I exp/olm81_moy5_formula_only_cut_rows_concept_set_runup_20261031.py --control    # C0・C1 → olm81/control.json
$P -I exp/olm81_moy5_formula_only_cut_rows_concept_set_runup_20261031.py --read       # Q1〜Q3 → olm81/read.json
```
