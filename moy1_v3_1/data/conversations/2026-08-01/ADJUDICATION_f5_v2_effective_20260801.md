# ADJUDICATION_f5_v2_effective_20260801.md
## `F5` DESIGN v2 発効 — 英文 3 件裁可・中止条件 3 の二段化・`G-pair` field 水準注記・判断層自己訂正 1 件・走行 green light

> **発行**: 2026-08-01、判断層（claude.ai / Fable）
> **契機**: [DESIGN_f5_two_axis_v2_20260801](DESIGN_f5_two_axis_v2_20260801.md)（HEAD `0ed2e06`・差分 8 点）+ [RESULT_f5_l1_checks_oracle_binding_20260801](RESULT_f5_l1_checks_oracle_binding_20260801.md)（HEAD `8f7a4df`）。
> **一行**: ★★★ **v2 発効。英文 3 件裁可。中止条件 2 は公式 `label` 列で凍結（+ 波報告に 3 列分布併記）。中止条件 3 は二段化 — 報告 trigger は公式列 split のまま、第二の対の適格判定は「結論部での He/Hi commit」を要件とする別裁定（基準は当該 PREREG 凍結時に固定）。driver が全文を oracle に渡していた発見により、F5a 下の公式 attractor 膨張は既知の機械的経路になった。判断層は致命傷の機序を自己訂正する（不良設定 → 情報経路の交絡）。F5a-2 波 1 は green light。**

---

## §0. 受理・発効

- v2 差分表 8 点を確認 — redline §1・§2-a〜d・§3-1/4/5 のすべてに対応 ⭕。**「上記以外に変更無し」の宣言を発効の前提として受理**。
- [RESULT_f5_l1_checks](RESULT_f5_l1_checks_oracle_binding_20260801.md) §1〜§2・§5 を **L1 受理**（§3 は L2）。
- ★ **DESIGN_f5 v2 を発効する**（v1 §1・§2 は正典のまま）。
- 記録: redline §2-b の懸念（`s` の束縛）に対し、実行層は一段深い実体（`classify(gen,"")` — **全文入力**）まで掘った。計器の解剖として本 turn の白眉。

---

## §1. 裁可 3 件（v2 §8-1/3/4）

| # | 件 | 裁定 |
|---|---|---|
| 1 | **`F5b-1` / `F5b-2` 英文**（§1-2） | ⭕ **裁可**。幾何 ①②（分離 ⇔ 内接線・割当完全保存）の L1 検算を根拠として受理。★ **「He と Hi のどちらが同種のどちらか」を原文同様に言わない**規律（情報を足さない）を守った点 — 初稿で足しかけて自分で止めた記録ごと ⭕ |
| 2 | **`F5a-2` の ⑥ 置換文**（§2） | ⭕ **裁可**。単一変数 = 出力順序指定、矛盾 prompt を作らない |
| 3 | **累積構成**（`F5b-2` ⊇ `F5b-1`・④ 同時修正） | ⭕ **承認**。帰属は隣接段の差分で読む |

---

## §2. 中止条件の裁定（v2 §8-2 + RESULT §3-3）

### 2-1. 中止条件 2（flail ≥ 3/9）の列

⭕ **公式 `label`（`classify(gen,"")`）で数える** — 基準線（母体 flail 0/9）と**同列で数える原則**。⛔ 事後に緩めない — 不変。
★ **追補**: 波報告に **3 列分布（`label` / `label_json_fields` / `label_conj_only`）を併記**する。全文入力は最も当たりやすい列であり、剥ぎすぎが stuck / attractor に化けて公式列で隠れる経路があるため — 併記は検出口を増やすだけで条件は増やさない。

### 2-2. ★★ 中止条件 3（Track-B ヒット）の二段化

**背景（L1）**: F5a の誘発する reasoning は He/Hi + center 語に自然に触れる。全文入力の公式 oracle では、**非 closure trace が reasoning 言及だけで attractor に落ちる** — F5a 下の公式 attractor 膨張は**既知の機械的経路**である（`R6`: 計器の有効域）。

> **裁定**:
> ① **報告 trigger は公式列の split のまま**（漏らさない・報告は安い）。報告には 3 列表 + 当該行の `conjecture` 抜粋 verbatim を添える。
> ② ★ **第二の対（`G-pair-2` 候補）としての適格判定は別裁定** — 要件は「**結論部での He/Hi commit**」（reasoning 言及のみでは不適格）。操作化基準（どの列・どの抽出法か）は、**当該条件の PREREG 凍結時に固定**する — `parse_json_field` の F5a 配置（reasoning 先行 + 末尾 JSON）での挙動が未較正のため、いま列を凍結しない。
> ③ INSTR v2 §1「split の型は発見された実体を見て個別裁定」と整合 — 適格判定は判断層。

### 2-3. 中止条件 1 の読みの注意（設計変更ではない）

`tau_brace` の移動は軸ごとに意味が違う: **F5a では τ 移動 ≈ 指示追従**（順序指示に従えば全行 τ>0 になる — retrieval 仮説への証拠力は弱い）。**F5b でこそ τ=0 跳躍の除去が retrieval 仮説の検定**になる。条件 1 の一報はこの区別を添えて読む。

---

## §3. `G-pair` への field 水準注記（RESULT §2-2 の帰結）

- **L1**: 現行対の `B-attractor` 3 本は field 水準で不均質 — `s9` = conjecture 水準 / `s3`・`s5` = reason フィールド水準（He/Hi + center が結論の外）。
- **裁定**: ⛔ **認定は不変** — outcome は凍結 oracle の label 水準で定義されており、oracle はその定義どおりに動いている。τ 所見も不変（`{` の位置は動かない）。**動いたのは attractor の語の含みであり、認定の根拠ではない**。
- ★ **注記 banner を同一検索単位へ**: [ADJUDICATION_gpair_certified_9](ADJUDICATION_gpair_certified_9_20260801.md) に ADDENDUM を挿入 — 「attractor 3 本の field 水準内訳（conj 1 / reason 2）は [RESULT_f5_l1_checks §2] 参照。認定は凍結 oracle の label 水準で不変。」

---

## §4. 判断層の自己訂正 — 致命傷の**機序**の言い直し

- redline §1 は「割当が**文章から決定不能**になる（不良設定）」とした。⚠ **③ が数値座標を与えているなら、これは過大** — 座標が割当を数値的に個別化するため、削除でも問題は解ける。
- **正しい機序**: 削除は「**register の変更 + 構造情報の経路移動（本文 → 座標）」の二重変化 = 交絡**。置換は register のみの単一変化。⇒ ★ **指示（register 置換）は不変であり、むしろ L1 検算で強化された** — 変わるのは理由の書き方だけ。
- **確認依頼（1 行）**: §5 の検算座標（O1=(-2.2849,…) 等）が prompt ③ の verbatim 値であることの確認。
- ⭕ **確認到着・訂正確定（2026-08-01、同 session）**: ★ **③ は 10 記号すべてに数値座標を与えている** ⇒ 割当は ③ 単独で決定。⇒ **② が運ぶのは割当ではなく構造的特徴づけ**（接線交点であること・X 群 = 混合型・He/Hi = 同型）。⇒ 本訂正（交絡機序）が正確と確定。★ 併せて §5-2 の意味も一段明確化: 示されたのは「割当の復元」ではなく「**構造的特徴づけが『分離する/しない』でも同一に復元される**」こと — F5b は数値的個別化を固定したまま**古典的概念枠だけ**を操作する、という最も清潔な形が確定した。
- **minor flag として記録**（性質断定を ③ の実体を開かずに書いた — 判断層起源）。系譜本則への計上は見送り、先生の裁定で覆せる。

---

## §5. 実行層の自己申告 3 件 — 受理

| # | 件 | 裁定 |
|---|---|---|
| 1 | 自作 regex parser で `s8` を誤判定 → `parse_json_field` verbatim import で取り直し | ⭕ 受理。★ **`family #11`（計器を書き直さない）は解析・検分側にも掛かる**を運用として記録（⛔ 新規律にしない） |
| 2 | ★ **print 文を実測前に書き、実測と矛盾する結論文を印字**（`R7`） | ⭕ **同型 9 例目・実行層起源 6 例目として受理**。★ 機序に名を置く: 見てから決めるの鏡像 = **決めてから見る**（結論文の事前テンプレ化）。自己捕獲 ⭕ |
| 3 | 符号反転直線の重複を数えた（`R5` — 同一性述語なしの計数） | ⭕ minor flag として記録。自己捕獲 ⭕ |

---

## §6. 走行指示（★ green light）

1. **F5a-2 波 1 を green light**（`blocked` / seeds 1..9 / lens 全行 / 記録様式 v2 §4-1 / 中止条件 v2 §5 + 本裁定 §2）。`R7-a` 遵守（clean tree・manifest）。
2. 波報告様式: 3 列分布 + `tau_brace` / `n_brace` 分布 + 条件 1 の軸別読み（§2-3）。
3. **DESIGN v2 §5 に pointer 1 行**: 「中止条件 3 の適格判定は [ADJUDICATION_f5_v2_effective §2-2] による二段化」— 本文改変不可・pointer のみ。
4. **ADDENDUM banner** を [ADJUDICATION_gpair_certified_9](ADJUDICATION_gpair_certified_9_20260801.md) へ（§3 の雛形）。
5. **③ の実体確認 1 行**（§4 — 検算座標 = prompt verbatim か）。`R8-a` どおり文書で。
6. 以降の順序は v2 §7 のまま: F5a 単軸 → F5b 単軸 → F5c。

---

## §7. 参照

[DESIGN_f5_two_axis_v2_20260801](DESIGN_f5_two_axis_v2_20260801.md)（発効対象）/
[DESIGN_f5_two_axis_20260801](DESIGN_f5_two_axis_20260801.md)（v1 §1 §2 正典）/
[RESULT_f5_l1_checks_oracle_binding_20260801](RESULT_f5_l1_checks_oracle_binding_20260801.md)（L1 一次）/
[REDLINE_f5_design_20260801](REDLINE_f5_design_20260801.md)（§1 機序は本 §4 で訂正）/
[ADJUDICATION_gpair_certified_9_20260801](ADJUDICATION_gpair_certified_9_20260801.md)（§3 の banner 先）/
[INSTR_b3_v2_gpair_tripwire_and_unified_p0_20260801](INSTR_b3_v2_gpair_tripwire_and_unified_p0_20260801.md)（§1 個別裁定条項）/
[SPEC/disciplines.md `R5` `R6` `R7` `R7-a` `R8-a`](../../SPEC/disciplines.md)

**発行**: claude.ai（判断層）2026-08-01。
