# RESULT_olmo3_base_bf16_screen_20260729.md
## OLMo-3 **base bf16** —— **呪縛は事前学習の重みの中に在る**（gate 出口 (ii)）

> **実施**: 2026-07-29 10:42–12:12 JST（総 wall 1.50 時間）、Claude Code（実行層）。
> **指示**: [`handoff_home_to_office/2026-07-28_olmo_jlens_directive.md`](../../handoff_home_to_office/2026-07-28_olmo_jlens_directive.md) §2（先生裁定・手 2）。
> **計器**: `probes/olmo3-base-bf16-screen/screen_base.py`（凍結 prompt md5 assert / 分類器 verbatim / mlx bf16 / `MAX_NEW=32768`）。
> **身分**: ⛔ **スクリーニングであって測定ではない。帯を切らない。事前登録もしていない。**
> **一行**: **base は probe に乗り、両腕とも `B-attractor` が最頻だった。Think（07-28）は attractor ゼロ。呪縛は事前学習側に在り、post-training が外している。**

> # ⚠⚠ retraction-banner（2026-07-31 設置・[RESULT_pc1_cue_invariance](../2026-07-31/RESULT_pc1_cue_invariance_20260731.md)）
>
> ★ **「両腕とも `B-attractor` が最頻」は cue `"\n"` に固有である。**
> 事前登録した cue 不変性 probe（P-C1・`6a32bb0` で実走前凍結）で、cue ∈ {`"\n"`, `" "`, `"\n\n"`} を単一変数として比較した:
>
> | cue | blocked の最頻 | blocked の bind |
> |---|---|---|
> | `"\n"`（本 screen） | **`B-attractor`**(4) | 2/9 |
> | `" "` | **`B-bind`**(4) | 4/10 |
> | `"\n\n"` | **`B-bind`**(7) | ★ **7/10** |
>
> ⭕ **attractor 率は cue 不変**（3〜5/10・Fisher 最小 p=.367）⇒ ★ **「base は attractor を産む」は cue-robust に強化された**（**`attractor 9/19`** は 3 cue を跨いで保たれる。⛔ 維持ではなく強化と読む・[裁定 §0 #2](../2026-07-31/INSTR_convergence_execution_20260731.md)）。
> ❌ **最頻ラベルは cue 依存**（P-C1-b 不成立）⇒ **本一行の「最頻」の主張は限定が要る。**
> ⚠ さらに `"\n\n"` の base は blocked で bind **7/10** であり、**Think の 7/7 と近い形**になる。
> ⇒ 「**呪縛は事前学習側に在り post-training が外している**」は **L2 のまま**であり、**本結果でさらに弱まる**。
> ⇒ 【諮問 A】再開・探検 B は cue 条件付きへ降格・Think fit 本命復帰・★ **予測失敗は drink**。

> # ⚠⚠ retraction-banner（2026-07-31 設置・C2 一括差し替え）
>
> ★ **`identity_distance` は fit 品質ではない。** [RESULT_identity_distance_identified_20260730](../2026-07-30/RESULT_identity_distance_identified_20260730.md) が逆問題で同定したとおり
> `identity_distance = ‖J_L − I‖_F / √d`（L = **最深 source layer**）であり、**小さいほど Jacobian lens が plain logit lens に近い**（polarity (β)）。
> ⇒ ★ **本文書中の「最良の計器 / 最良の fit / 最も良く合う」は誤読である。**
> ⇒ lens 選択の根拠は「**base に lens が張られている唯一の候補**」+「**fit が収束している**（`mean_rel_change 0.001781 < 0.002`・n=470）」へ置き換える。
> ⛔ **`identity_distance` を収束の根拠に引用しない**（規律 [`R2`](../../SPEC/disciplines.md)）。
> ⚠ **測定値そのものは不変**（`0.130071` 等は上流 config verbatim・[職場で再現済](../2026-07-31/RESULT_olmo32b_identity_reproduced_20260731.md) +0.24%・精度の範囲内）。


---

## §1. 実測（**L1**）

`allenai/Olmo-3-1125-32B`（**base**・bf16・mlx）、凍結 `open`/`blocked` verbatim + cue `"\n"`（E5）、従来鏡映 n=10。

| arm | 全 n | 上限到達 | **分母** | label |
|---|---|---|---|---|
| `blocked` | 10 | **1** | **9** | **`B-attractor` 4** / `B-bind` 2 / `B-flail` 2 / `B-stuck-L1` 1 |
| `open` | 10 | 0 | **10** | **`B-attractor` 5** / `B-stuck-L1` 4 / `B-bind` 1 |
| **両腕合計** | 20 | 1 | **19** | **`B-attractor` 9** / `B-stuck-L1` 5 / `B-bind` 3 / `B-flail` 2 |

**`B-attractor` が最頻（9/19）。** 両腕とも出現する。

## §2. gate 判定 —— **出口 (ii)**

指示書 §2 の三分岐に照らす:

| 出口 | 条件 | 判定 |
|---|---|---|
| (i) | 呪縛非該当（bind 優勢・attractor ≈ 0） | ❌ |
| **(ii)** | **outcome が割れる（attractor 出現）** | ✅ **該当** |
| (iii) | base が probe に乗らない | ❌（§3） |

指示書の (ii) の帰結: 「**完全代替候補**: 玉座の手（0 手目・将来の探検 B）を最良 lens（0.1301）の上で立てられる。qwen3-32b lens（n=80・最浅）への依存が解ける」。⚠ **[C2 訂正 2026-07-31]** 「最良」は誤読 —— `identity_distance` は lens が logit lens にどれだけ近いかであって fit 品質ではない（冒頭 banner）。

**しかも lens が張られているのは base、すなわち呪縛が出る当の物体である。** lens と現象が同一物体上で揃う。

## §3. 「乗らない」の否定（**L1**・[RECORD §3-2](RECORD_olmo_lens_provenance_20260729.md) 再掲）

試走は 0 字を返したが、計器を疑って切り分けた結果、**prompt 境界の artifact** と判明した:

- 素朴な continuation は正常生成（計器は動く）
- 凍結 prompt は `…that circle.` と**文末ピリオド**で終わる → base は文書終端と読み即 `<|endoftext|>`
- 末尾に **`"\n"` 1 個**で生成する

⚠ **cue の選択は研究者の自由度**であり、**E5 として登録**（`cue` 列を全行に記録・取り消し可能）。
**【諮問 A】として判断層へ差し戻し中**（[HANDOFF §3-1](HANDOFF_to_claudeai_20260729.md)）。本 RESULT の判定は cue の身分が確定するまで**暫定**である。

## §4. 対比 —— Think（07-28）との差

⛔ **数値比較ではない。label の有無としての対比。**

| | **base** bf16（本日） | **Think** Q4_K_M（[07-28](../2026-07-28/RESULT_olmo3_behavior_screen_20260728.md)） |
|---|---|---|
| `blocked` の attractor | **4/9** | **0/7** |
| `open` の attractor | **5/10** | **0/9** |
| `blocked` の bind | 2/9 | **7/7** |
| `open` の stuck | 4/10 | **9/9** |
| **attractor 合計** | **9/19** | **0/16** |

**同じ事前学習コーパス（Dolma 3）・同じアーキテクチャ（64 層 / 5120 / vocab 100278）。**

> **⇒ 誤アトラクタは事前学習の重みの中に在り、post-training が外している。**

### 4-1. ⚠ ただし単一変数ではない

| 軸 | base | Think |
|---|---|---|
| **post-training** | 無 | **有**（本命の候補） |
| 量子化 | bf16 | Q4_K_M |
| flow | raw + cue `"\n"` | chat template + thinking チャネル |
| 生成上限 | 32768 | 16384 |

**統制するには `allenai/Olmo-3-32B-Think` を bf16・同一 harness で走らせる。** 計器は既にある（60 GB の DL + 20 本）。
傍証: qwen3:32b の robustness で **Q8_0 が base と同値**（1/10 = 1/10）＝量子化はラベルを動かさなかった。⚠ **別族なので OLMo には移せない**。

⛔ **本 RESULT は「post-training が外した」を主張しない。** 交絡が残っている。**locate されたという以上には出ない。**

## §5. 上限到達 1 本の扱い（**【諮問 D】**）

`blocked` s=7 が **115,475 字・3,603.3 秒**で `MAX_NEW=32768` に到達。label は `B-bind` と付いたが、
**全文を `classify` に通しているため 32,768 token 分の continuation が混ざっており、label は信用できない**。→ 分母から外した。

⚠ **Think 側の除外（answer 0 字 = 分類不能）とは性質が違う**（base 側は「分類はできるが汚染」）。同型扱いの可否を判断層へ差し戻し中。

**これは base の性質でもある**: post-trained なら EOS で止まるところ、**base は答えを書いた後も文書の続きを書き続ける**。

## §6. 計器申し送り

- `MAX_NEW = 32768` は妥当（20 本中 1 本のみ到達。Q4 screen の 16384 は 4/20 が不足だった）
- 総 wall **1.50 時間**（Q4 screen の 4h55m より速い。base は長考しない）
- 生成長の分散が極端: 74 字（3.8 秒）〜 115,475 字（3,603 秒）
- ⚠ 生成上限が違うため **Q4 screen と数値比較不可**

## §7. 射程外

- **「post-training の何が外したか」** —— §4-1 の統制実験が先
- **順位水準（J-space）** —— 本 screen は行動水準のみ
- **cue の身分が確定するまでの判定の最終性**（§3）
- **Qwen との集計・曲線**（判断層 G2 / [KAIME](../2026-07-28/KAIME_scale_axis_curve_20260728.md)）

## §8. 参照

計器 = `probes/olmo3-base-bf16-screen/screen_base.py` / 成果物 = `results/screen_olmo3_base_bf16.json` /
[RECORD_olmo_lens_provenance_20260729](RECORD_olmo_lens_provenance_20260729.md) / [HANDOFF_to_claudeai_20260729](HANDOFF_to_claudeai_20260729.md) /
[RESULT_olmo3_behavior_screen_20260728](../2026-07-28/RESULT_olmo3_behavior_screen_20260728.md) /
[NOTE_similitude_circle_is_apollonius](NOTE_similitude_circle_is_apollonius_20260729.md)（誤アトラクタの候補機序）
