# RESULT_pc1_cue_invariance_20260731.md
## `CUE/P-C1` —— ★ **予測は失敗した。attractor 率は cue 不変だが、最頻ラベルは cue で動く**

> **実施**: 2026-07-30 14:24 → 19:04 JST（wall 4:40）、Claude Code（実行層）。判定は 2026-07-31。
> **事前登録**: [PREREG_pc1_cue_invariance_20260730](../2026-07-30/PREREG_pc1_cue_invariance_20260730.md)（★ commit **`6a32bb0`** で**実走前に凍結**）。
> **身分**: **実測（L1）**。判定は凍結された決定規則どおり**機械的に**行った。⛔ 見てから基準を選んでいない。
> **一行**: **主基準（attractor 率）は不変。副基準（最頻ラベル）は不一致。⇒ 凍結規則により「不変」は成立せず ——【諮問 A】再開・探検 B は cue 条件付きへ降格・Think fit 本命復帰・★ 予測失敗は drink。**
> ★ **札**: 本書の `P-C1` は **`CUE/P-C1`**（cue invariance 系列）である。裸札 `P-C1` は [PREREG_REGISTRY §2](../../PREREG_REGISTRY.md) により **`CE/P-C1`（closure erasure・公開済み）**に束縛されているので、**本書では必ず prefix 付きで読むこと**。


> # ⚠⚠ 二点の留保（2026-07-31・自宅 commit `3c5d120` 読了後に追補）
>
> **1. 札は `CUE/P-C1` に確定した**（先生裁可 2026-07-31「プレフィクスを付けてください」⇒ [PREREG_REGISTRY](../../PREREG_REGISTRY.md) 設置）。**執筆順の問題は残る:** 自宅が [DESIGN_prereg_id_scoping §6](../2026-07-30/DESIGN_prereg_id_scoping_20260730.md)
> で「**P-C1 の RESULT はこれが決まるまで書けない**」と決めた（07-31 00:08）。**本書はそれを知らずに書かれた**
> （pull 前）。⇒ 経緯と扱いは [FLAG_pc1_result_written_before_scoping](FLAG_pc1_result_written_before_scoping_20260731.md)。
> ⚠ **札 `P-C1` は 07-17 の closure erasure（Zenodo/論文表に公開済）とも衝突している。**
> ⇒ ⭕ **裁可済み。本書の札は `CUE/P-C1`**（裸札 `P-C1` は `CE/P-C1` = 公開済みの closure erasure に束縛）。
> **本書の測定・判定そのものは凍結手順どおりに成立している。**
>
> **2. 「base の lens = 最良（0.1301）」は誤読だった。** 自宅が式を同定した
> （[RESULT_identity_distance_identified](../2026-07-30/RESULT_identity_distance_identified_20260730.md)・**L1**）——
> `identity_distance = ‖J_L − I‖_F / √d` は **logit lens との一致度**であって fit 品質ではない。
> ⇒ **§4 の「探検 B は base の lens 0.1301 上で」という前提は根拠を失う。**
> ⭕ ただし **本書の判定は影響を受けない** —— P-C1 は行動 probe であり lens を一切使っていない。
> ⇒ **探検 B は二重に条件付き**（P-C1 による cue 条件付き降格 + 基質選択根拠の消失）。**着火保留。**

---

## §1. 実測（全 40 世代 + 参照点 20 世代）

`cue="\n"` は [07-29 の凍結 screen](../2026-07-29/RESULT_olmo3_base_bf16_screen_20260729.md) をそのまま参照点に使った（**再走なし・再採点なし**・PREREG §2 どおり）。
D 分母規約（裁可事項 3）を適用: **primary = `truncated(limit)` を除外 / 全行込みを並記**。

### blocked

| cue | primary attractor | 全行込み | **最頻ラベル** | 分布（primary） |
|---|---|---|---|---|
| `"\n"`（参照点） | **4/9** | 4/10 | ★ **`B-attractor`**(4) | bind 2 / flail 2 / **attr 4** / stuck 1 |
| `" "` | **3/10** | 3/10 | ★ **`B-bind`**(4) | **bind 4** / attr 3 / stuck 2 / flail 1 |
| `"\n\n"` | **3/10** | 3/10 | ★ **`B-bind`**(7) | **bind 7** / attr 3 |

### open

| cue | primary attractor | 全行込み | **最頻ラベル** | 分布（primary） |
|---|---|---|---|---|
| `"\n"`（参照点） | **5/10** | 5/10 | ★ **`B-attractor`**(5) | **attr 5** / stuck 4 / bind 1 |
| `" "` | **2/8** | 2/10 | ★ **`B-stuck-L1`**(3) | attr 2 / **stuck 3** / bind 1 / flail 2 |
| `"\n\n"` | **4/9** | 5/10 | ★ **`B-stuck-L1`**(5) | attr 4 / **stuck 5** |

⚠ cap 到達 **4 件**（参照点 1 + 新規 3）。⇒ primary の分母が 9 / 8 になっているセルがある。

## §2. 判定（[PREREG §3](../2026-07-30/PREREG_pc1_cue_invariance_20260730.md) の操作化どおり）

### 2-1. CUE/P-C1-a（主）—— **✅ 不変**

2×3 分割表（attractor / 非attractor）に Fisher の正確検定（対毎・両側）+ χ²:

| 条件 | 表 | χ² p | 対毎 Fisher（最小 p） | 判定 |
|---|---|---|---|---|
| blocked | `[[4,3,3],[5,7,7]]` | 0.751 | nl-space .650 / nl-nlnl .650 / space-nlnl 1.000 → **.650** | ★ **p > 0.05 ⇒ 不変** |
| open | `[[5,2,4],[5,6,5]]` | 0.541 | nl-space .367 / nl-nlnl 1.000 / space-nlnl .620 → **.367** | ★ **p > 0.05 ⇒ 不変** |

### 2-2. CUE/P-C1-b（副）—— ★ **❌ 不一致**

| 条件 | `"\n"` | `" "` | `"\n\n"` | 判定 |
|---|---|---|---|---|
| blocked | **`B-attractor`** | **`B-bind`** | **`B-bind`** | ❌ **不一致** |
| open | **`B-attractor`** | **`B-stuck-L1`** | **`B-stuck-L1`** | ❌ **不一致** |

⚠ **tie 規則の適用は不要**（すべて単独最頻。blocked/space は 4>3、open/space は 3>2）。⇒ **事前に決めた tie 規則では救われない。**

### 2-3. ⇒ 凍結規則の適用

> **PREREG §3: 「不変 = CUE/P-C1-a ∧ CUE/P-C1-b が両条件で成立」**
> ⇒ **CUE/P-C1-b が両条件で不成立 ⇒ ★ 「不変」は成立しない。**

## §3. ★★ 何が動いて、何が動かなかったか（**これが本結果の中身**）

| 量 | cue 依存性 |
|---|---|
| **attractor 率** | ⭕ **不変**（blocked 4/9・3/10・3/10 / open 5/10・2/8・4/9。有意差なし） |
| ★ **非アトラクタ側の質量の行き先** | ★ **cue 依存** —— `"\n"` では **flail / stuck** に散り、`" "`・`"\n\n"` では **bind** に寄る（blocked: bind 2 → 4 → **7**） |

> ### ⇒ **cue は「アトラクタを産むか」を動かさない。「産まなかったときに何になるか」を動かす。**
> ⇒ **`"\n"` は最も bind から遠い cue だった。** `"\n\n"`（段落境界として最も自然）では blocked の bind が **7/10** —— これは Think の `7/7` に**近い形**である。

## §4. 決定表の適用（[PREREG §4](../2026-07-30/PREREG_pc1_cue_invariance_20260730.md)・凍結）

| 帰結 | 状態 |
|---|---|
| **【諮問 A】** | ★ **再開**（cue は「同じ土俵に載る」と言い切れない） |
| **探検 B** | ★ **cue 条件付きへ降格**（base lens 上の結果は cue を明示して読む） |
| **Think fit** | ★ **本命復帰**（[ADJUDICATION §2 復活条件 (α)](../2026-07-30/ADJUDICATION_throne_move0_20260730.md)。32B = **1.42 GPU 時間**） |
| ★ **drink** | ★ **予測失敗** —— 台帳に計上（適用は先生） |

## §5. ⚠ 波及 —— **07-29 の見出しは cue 条件付きになる**

[RESULT_olmo3_base_bf16_screen](../2026-07-29/RESULT_olmo3_base_bf16_screen_20260729.md) の一行:

> 「base は probe に乗り、**両腕とも `B-attractor` が最頻**だった。…**呪縛は事前学習側に在り、post-training が外している**」

| 主張 | 本結果後 |
|---|---|
| 「**両腕とも `B-attractor` が最頻**」 | ★ **cue `"\n"` に固有**。`" "`・`"\n\n"` では blocked の最頻は **`B-bind`** ⇒ **限定が要る** |
| 「base は attractor を産む」 | ⭕ **維持**（率は cue 不変・3〜5/10） |
| 「呪縛は事前学習側に在り post-training が外している」 | ⚠ **L2 のまま**（[ADJUDICATION §2](../2026-07-30/ADJUDICATION_throne_move0_20260730.md) の L1 昇格禁止は継続）。★ **さらに弱まる** —— `"\n\n"` の base は blocked で bind 7/10 であり、**Think の 7/7 と近い形**になる |

⇒ **07-29 の RESULT に retraction-banner を設置する**（§7 で実施）。

## §6. ⛔ 立てていないもの

- **「`"\n\n"` が正しい cue である」**とは言わない。**どれが正しいかを決める基準を我々は持っていない**（それが【諮問 A】の中身）
- **cue → 分布の機序**（段落頭 prior の強さ等）は測っていない。⛔ welding しない
- **n=10/cell の検出力は低い**（PREREG §5-1 に実走前から明記）。⇒ **CUE/P-C1-a の「不変」も「大きな移動が無い」までである。証明ではない**
- **Think との直接比較**は [ADJUDICATION §1-4 (c)](../2026-07-30/ADJUDICATION_throne_move0_20260730.md) の射程限定どおり、token / likelihood レベルでは行わない

## §7. 実施した文書追補

| 対象 | 追補 |
|---|---|
| [RESULT_olmo3_base_bf16_screen_20260729](../2026-07-29/RESULT_olmo3_base_bf16_screen_20260729.md) | **retraction-banner**（「両腕とも attractor が最頻」は cue `"\n"` 固有・率は不変） |

## §8. 参照

[PREREG_pc1_cue_invariance_20260730](../2026-07-30/PREREG_pc1_cue_invariance_20260730.md)（凍結・`6a32bb0`）/
[ADJUDICATION_throne_move0_20260730 §1-5・§2・§3](../2026-07-30/ADJUDICATION_throne_move0_20260730.md)（決定表・復活条件・分母規約）/
[RECORD_ratification_throne_move0_20260730](../2026-07-30/RECORD_ratification_throne_move0_20260730.md)（一括裁可と申し送り）/
[RESULT_olmo3_base_bf16_screen_20260729](../2026-07-29/RESULT_olmo3_base_bf16_screen_20260729.md)（参照点 `cue="\n"`）/
生データ = `probes/olmo3-pc1-cue-invariance/results/pc1_runs.json`（40 行・`frozen_commit: 6a32bb0` を刻印）
