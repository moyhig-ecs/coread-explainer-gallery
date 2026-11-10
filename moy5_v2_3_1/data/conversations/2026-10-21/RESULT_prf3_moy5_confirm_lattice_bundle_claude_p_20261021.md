# RESULT(札 `prf3`): 確かめた — 焦点・準線を塞ぐと、格子(頂点の比例中項)を持ち出して P_y の式まで束ねる。新しい標本で Opus 0 / 10 → **10 / 10**・Fable 0 / 10 → **4 / 10**(主 LAT_SYM)。予想 H1・H2・H4 は両 model で当たり・H3 は Fable で外れ(壊れた出力 5 本)

- 札 = [PREREG](PREREG_prf3_moy5_confirm_lattice_bundle_claude_p_20261021.md)(凍結 `8a830667`)。書いた時の HEAD = `8a830667`(`R1`・fetch 済・origin と同じ)。
- 走行 = MacBook・Claude Code 2.1.299・`claude -p`・effort max・workers 4。40 本とも ok・err 0・**実際の tool の呼び出し 0**(init の tools = `[]`)。wall の中央値 232 s・最長 1411 s。見積りの費用は Opus 15.3・Fable 32.0 USD 相当(購読の経路)。
- 出力 = `ConstructGap/exp/results_prf3_20261021.jsonl`(md5 `3fa335be`)・R2(述語を作った集合)= `results_prf3_20261021_r2_derivation_set.jsonl`(`4f08c5d2`)。
- 身分: §1 = `L1`(凍結の述語の実出力・本文の逐語)/ §2 = 予想の当たり外れ / §3 = R2(述語を作った集合の記述・確かめに数えない)/ §4 = `L3` / §5 = 限界。訂正(10-22・監査 A8b の指摘): 初版は「§1〜§3 = L1 / §4 = 予想 / §5 = L3」と節番号がずれていた(prf1 の型の写し)。

## §1. 結果(新しい標本・凍結の述語・各 n 10)

| model | 腕 | VMP | SYM_PY | LAT | FD_USE | **LAT_SYM(主)** | ORDER2 | 壊れた出力 | 主(壊れた出力を除く) |
|---|---|---|---|---|---|---|---|---|---|
| Opus 5.5 | P5(塞がない) | 5 | 9 | 5 | 10 | **0** | 4 | 0 | 0 / 10 |
| Opus 5.5 | **P5B(塞ぐ)** | 10 | 10 | 10 | 0 | **10** | 10 | 1 | 9 / 9 |
| Fable 5.1 | P5(塞がない) | 2 | 5 | 2 | 5 | **0** | 2 | 5 | 0 / 5 |
| Fable 5.1 | **P5B(塞ぐ)** | 5 | 6 | 5 | 2 | **4** | 4 | 2 | 4 / 8 |

- Fable P5 の壊れていない 5 本は、5 本とも FD_USE(焦点・準線の道で証明した)。
- 壊れた出力 8 本:
  - Fable 7 本(P5 r0・r1・r3・r6・r9 / P5B r4・r7)は、どれも「I'll verify … numerically」と書いて tool の呼び出しの書式(`<invoke` / `Bash`)を本文に書き、JSON の答えが無い。
  - Opus P5B r4 は書式の跡があるが、JSON の答えは揃っていて主は成り立つ(全部の行の分母に入れた。除くと 9 / 9)。

### §1-1. 道の逐語(`L1`)
- Opus P5B r0(塞ぐ・LAT_SYM): "(P5) Substituting gives (VD + VH)² = VD² + VH² + 2·VP_x², so VP_x² = VD·VH = FV·VH" → "(P6) Therefore HP_y² = 4·VP_x² = 4·FV·VH for every P_x."
- Fable P5B r0(塞ぐ・LAT_SYM): "VH = VP_x^2/VF >= 0" → "every position of P_y satisfies the equation P_yH^2 = 4·VF·VH … the locus of P_y is the parabola with vertex V, axis j and parameter p = VF"。
- Opus P5 r0(塞がない・FD_USE): "(4) m ⊥ FK at its midpoint P_x is the perpendicular bisector of FK, so P_yF = P_yK."

## §2. 予想(PREREG §3)の当たり外れ
- **H1(主)**(P5B − P5 の LAT_SYM: Opus ≥ 4・Fable ≥ 2)= **当たり**(Opus 10 − 0 = 10・Fable 4 − 0 = 4)。
- **H2**(P5B の LAT_SYM: Opus ≥ 6・Fable ≥ 3)= **当たり**(10・4)。
- **H3**(P5 の FD_USE ≥ 7)= Opus **当たり**(10)・Fable **外れ**(5)。Fable の残りの 5 本は壊れた出力で、壊れていない 5 本は 5 本とも FD_USE。
- **H4**(P5B の FD_USE ≤ 2)= **当たり**(Opus 0・Fable 2)。

## §3. 述語を作った集合(R2・prf1 + prf2・確かめに数えない・記述)

| 札・腕 | Opus LAT_SYM | Fable LAT_SYM | Opus FD_USE | Fable FD_USE |
|---|---|---|---|---|
| prf1 P5(塞がない) | 0 | 0 | 9 | 8 |
| prf2 P5B(塞ぐ) | 9 | 4 | 0 | 2 |
| prf1 P5K(比例中項を渡す) | 0 | 0 | 10 | 10 |
| prf2 P5BK(塞いで渡す) | 2 | 5 | 8 | 2 |

- P5BK の Opus の FD_USE 8 は、前半の「不変量の理由」の節で、渡された比例中項を床につなぐ等式(EJ = KP_y = FP_y)を P_y の式より前に書いたもの(PREREG §5 の保守側の限界・prf2 RESULT §3)。

## §4. 三つの札(prf1・prf2・prf3)を合わせた読み(`L3`)
1. **近道(焦点・準線)が開いていると、両 model とも近道で証明を閉じ、格子で閉じない**(塞がない腕 P5 の LAT_SYM は 2 札〔prf1 の読み直し §3・prf3 §1〕× 2 model = 4 cell で全部 0。prf1 の P5K を含めれば 6 cell で 0)。「格子は通らない」とは書かない: prf3 の Opus P5 は VMP 5・LAT 5 = 半数が頂点の比例中項を書いており、LAT_SYM 0 は FD_USE 10(焦点・準線で閉じた)のため。訂正(10-22・監査 A8b の指摘): 初版は「格子は通らない(… 4 回の標本で全部 0)」。
2. **近道を塞ぐと、格子(主に頂点の比例中項 VP_x² = FV·VH)を自分で持ち出し、P_y の式 HP_y² = 4·FV·VH まで束ねて閉じる**。Opus は 2 回の標本で 9 / 10・10 / 10。Fable は 4 / 10・4 / 10(壊れた出力を除くと 4 / 9・4 / 8)。prf2 の 9 / 10・4 / 10 は R2 の集合(述語を作った標本・§3)で、確かめの数は prf3 の側だけ。限定(10-22・監査 A8b の指摘): 「束ねる力は在る」は Opus では無限定(10 / 10)、Fable では壊れていない 8 本中 4 本 = 半分(できない可能性が残る)。二つの標本は同じ日・同じ CLI・同じ md5 の文面の再標本で、条件の独立な再現ではない。
3. ⇒ 先生の仮説「moy-5 では、複数のひらめきを束ねて証明として推論鎖を再構成する必要がある」について:
   - **束ねる力は在る**(塞げば束ねる)。
   - **格子を持ち出す力も在る**(渡さなくても、塞げば持ち出す)。
   - 束ねないのは、**近道がある時に格子を選ばない**(満足停止)と読む(`L3`)。開いた条件の 0 は不能ではない(P5B が示す)。ただし選択(won't)か引き金の不在かは、本札の腕では分けていない: BLOCK の文「Derive the equation from other relations among the given points」は塞ぐと同時に「他の関係から導け」と指図するので、P5B が測るのは「指示されれば格子で導ける」であって「格子を選ぶ」ではない。moy-1 の closure-forcing(楽な出口を塞ぐと束縛が出る)との同型は `L3` の類推(moy-1 の数は本札の材料に無い)。訂正(10-22・監査 A8b の指摘): 初版は「can't でなく won't」と言い切っていた。
4. moy-5 の家の CUT(幾何平均の格子)で塞ぐ前に出ていた 0 は、「格子の看破ができない」ではなく「看破しなくても証明が閉じる道を選んだ」と読み直せる。⇒ ConstructGap の moy-5 の記述(「Fable すら CUT 0 = frontier」06-25)は、**近道が開いた条件での数**として注を付ける候補。ただし prf3 で持ち出された LAT はほぼ VMP(頂点の比例中項)で、prf1 では END の側に数えていた関係でもある(RESULT prf1 §6)。06-25 の家の CUT(幾何平均の格子)と同じ「格子」かは本材料では確かめていない = 候補の hedge を保つ(10-22・監査 A8b の指摘)。

## §5. 限界と注意
- n 10 × 2 回の標本(prf2・prf3)・一題・二つの文面・effort max・Claude Code の経路だけ。
- **Fable の壊れた出力が多い**(prf1 2・prf2 4・prf3 7 / 各 40 本中の Fable 20 本。prf1 は MALFORMED の述語〔prf2 で定義 = JSON の答えが無い、または本文に tool の呼び出しの書式〕で数えれば 3 = P5 r1・r7 + P5K r4 だが、P5K r4 は JSON の答えが揃っている〔RESULT prf1 §1〕。訂正 10-22・監査 A8b の指摘: 初版は「prf1 3」)。prf1 の P5K r4 を除き、どれも「数値で確かめてから答える」と書き、無い tool を呼ぼうとして JSON を出さずに終わる。Claude Code の harness の system prompt が scratchpad と道具を案内することと、`--disallowedTools` で道具を全部外したことの組み合わせで起きると読める(`L3`)。Fable の率はこの分だけ低く出る(壊れていない行での率を並記した)。経路を API に替えるか、「道具は無い」と明記する文を足すかは別の札の判断。
- FD_USE の保守側の限界(前半の不変量の節の等式も数える)と、NEG の多く数える側の限界(PREREG §5)。

## §6. 次の候補(先生の判断)
- ConstructGap の moy-5 の記述(「CUT 0」の条件)に、近道が開いているという条件の注を足す。
- moy-1 と moy-5 を同じ型(「楽な出口を塞ぐと出る」)として、co-lead 稿(C1 / C2 selection-gap)の一節にまとめる。
- Fable の壊れた出力への手当て(API の経路で同じ腕を回す・または「道具は無い」の一文)。
