# RESULT_olmo3_behavior_screen_20260728.md
## OLMo-3:32b 挙動スクリーニング —— **呪縛に掛からない 32B が在る**

> **実施**: 2026-07-28 16:05–21:00 JST（約 4h55m）、Claude Code（実行層）。**計器**: `probes/olmo3-behavior-screen/screen_moy1.py`
> **位置**: 判断層 **G3**（表現空間を掘る前に行動 probe）に従う。[REPORT_olmo3_G0_to_claudeai_20260728](REPORT_olmo3_G0_to_claudeai_20260728.md) §4-1 で起動を報告済み。
> **身分**: ⛔ **スクリーニングであって測定ではない。帯を切らない。事前登録もしていない。** 出るのは label 分布のみで、CommitStage のいかなる判定にも影響しない。
> **一行**: **blocked 7/7 bind（全て O1O2）／open 9/9 stuck、attractor は 20 本中 0 本。He/Hi を 1 本あたり最大 122 回唱えながら、一度も落ちない。**

> # ⚠⚠ retraction-banner（2026-07-31 設置・C2 一括差し替え）
>
> ★ **`identity_distance` は fit 品質ではない。** [RESULT_identity_distance_identified_20260730](../2026-07-30/RESULT_identity_distance_identified_20260730.md) が逆問題で同定したとおり
> `identity_distance = ‖J_L − I‖_F / √d`（L = **最深 source layer**）であり、**小さいほど Jacobian lens が plain logit lens に近い**（polarity (β)）。
> ⇒ ★ **本文書中の「最良の計器 / 最良の fit / 最も良く合う」は誤読である。**
> ⇒ lens 選択の根拠は「**base に lens が張られている唯一の候補**」+「**fit が収束している**（`mean_rel_change 0.001781 < 0.002`・n=470）」へ置き換える。
> ⛔ **`identity_distance` を収束の根拠に引用しない**（規律 [`R2`](../../SPEC/disciplines.md)）。
> ⚠ **測定値そのものは不変**（`0.130071` 等は上流 config verbatim・[職場で再現済](../2026-07-31/RESULT_olmo32b_identity_reproduced_20260731.md) +0.24%・精度の範囲内）。


---

## §1. 実測（L1）

`olmo-3:32b`（ollama・**Q4_K_M**・32.2B・thinking flow）、prompt = 凍結 `open`/`blocked` verbatim（md5 assert 済）、
分類器 = `run_moy1_concyclic_blocked.py::classify` verbatim、従来鏡映 n=10（temp0 ×1 + temp0.7 seed 1..9）、`NUM_PREDICT=16384`。

| arm | 全 n | 打ち切り | **分母** | label | bind の target |
|---|---|---|---|---|---|
| **`blocked`** | 10 | 3 | **7** | **`B-bind` 7/7** | **`O1O2` 7/7** |
| **`open`** | 10 | 1 | **9** | **`B-stuck-L1` 9/9** | — |

- **`B-attractor` = 0 / 20**（両腕・打ち切り含む全 trace）
- **`B-flail` = 0 / 20**

## §2. 打ち切りの扱い —— 除外は結果を有利に歪めていない（**検算済み**）

打ち切り 4 本は `done_reason == length` かつ answer 0 字。**thinking で 47,791〜55,682 字を使い切っており、計器の容量不足であってモデルの失敗ではない**（screen の設計時に登録済みの扱い）。

⚠ しかし「長い trace ほど attractor に迷い込む」なら、除外そのものが結果を bind 側に偏らせる。**そこで打ち切り 4 本の thinking 末尾を開いた**:

| trace | 末尾で何をしていたか | 向き |
|---|---|---|
| `blocked` s=3 | 「Conjecture: The four points X form a circle with **diameter O1O2**」 | **bind に到達済み**・整形中に切断 |
| `blocked` s=8 | 「thus lying on that circle. So the answer must be they are **concyclic with center at midpoint of O1O2**」（内積 ≈ −0.004 で数値検算済み） | **bind に到達済み**・切断 |
| `blocked` s=2 | 「let's see if **He is on the X-circle**. Compute distance…」 | He を**候補として検査中**（棄却も採用もしていない） |
| `open` s=7 | 円の方程式の係数を検算中 | 判定不能 |

**→ attractor に向かっていた trace は 1 本も無い。むしろ 2 本は bind に届いていた。** 除外は 7/7 を甘くしていない（むしろ厳しめ）。

## §3. 所見 —— **語彙は濃厚、commit は不動**

全 20 本が He / Hi / homothety / Monge に言及する。`blocked` の言及回数は 1 本あたり **18〜122 回**（`he` + `hi` の合計）。
`open` の 1 本目は "…are always concyclic according to **Monge's theorem**" と、**相似中心の理論を名指しで引きながら L1 で止まる**。

つまり OLMo-3:32b は **Apollonius/Monge の理論体系の内側に深く居て、そのうえで O1O2 に commit する**。

> ★ これは 8b の J-lens 所見（[RESULT_jlens_8b_p7](RESULT_jlens_8b_p7_20260728.md) §4-4）と**同じ形**である —— 本文では He/Hi を 10/10 で唱えるが、順位では中央 25,000 位で一度も候補にならない。
> **ただし OLMo については語彙水準しか見ていない。**順位水準が同型かは未測。それを測るのが次の一手であり、OLMo の lens は **base に張られている唯一の候補**であり、**fit は収束している**（`mean_rel_change 0.001781 < 0.002`・n=470）。⚠ **[C2 訂正 2026-07-31]** 「最良」は誤読 —— `identity_distance` は lens が logit lens にどれだけ近いかであって fit 品質ではない（冒頭 banner）。

## §4. 対照 —— **同一セルで結果が逆転する**

| | `olmo-3:32b` | `qwen3:32b` |
|---|---|---|
| パラメータ | 32.2B dense | 32.8B dense |
| 量子化 | **Q4_K_M** | **Q4_K_M** |
| flow | ollama thinking | ollama thinking |
| **`blocked` の bind** | **7/7** | **1/10** |
| **`blocked` の attractor** | **0/7** | **7/10** |

**規模・量子化・提供経路を揃えても、族が違えば結果が反転する。**

⛔ **本節から曲線を引かない。** これは per-model の記述であって、族を跨ぐ機構の主張ではない。
✅ **本節が言えるのは否定形のみ**: 「パラメータが増えると Apollonius の呪縛に掛かる」は、**規模の法則としては成り立たない**。
32B-dense というセルに、呪縛される族と呪縛されない族が同居している。

> 本日の [KAIME_scale_axis_curve_20260728](KAIME_scale_axis_curve_20260728.md) 戒め 2（「反例を探してから引く」）の、**同日中の適用例**。
> 反例を探しに行ったら、同じセルに居た。

## §5. 玉座捜しの基質としての適格性

[PLAN_shinpan_kukan_exploration_20260728](PLAN_shinpan_kukan_exploration_20260728.md) の基質条件は **「outcome が割れること」**（bind するだけでは足りない）。

| 条件 | OLMo-3:32b | 判定 |
|---|---|---|
| `blocked` で bind が立つ | 7/7 | ✅ |
| `open` と `blocked` で outcome が割れる | stuck 9/9 ↔ bind 7/7 | ✅ **完全に割れる** |
| lens が公開されている | `neuronpedia/jacobian-lens` に実在 | ✅ |
| lens の fit 収束 | `mean_rel_change` **0.001781** < 0.002 / n=470（★ **収束**。⚠ `identity_distance 0.1301` は fit 品質ではない = 冒頭 banner） | ✅ |
| 学習データが辿れる | Dolma 公開 | ✅ |

**→ 五条件すべてを満たす。qwen3:8b と同じ outcome の割れ方を、はるかに良い計器と公開データの上で持っている。**

## §6. 残る交絡 —— **flow の非同一は埋まっていない**

[REPORT §4-2](REPORT_olmo3_G0_to_claudeai_20260728.md) の指摘は本結果でも有効:

| | lens が張られている物体 | 本スクリーニングが走った物体 |
|---|---|---|
| checkpoint | `allenai/Olmo-3-1125-32B`（**base**） | ollama `olmo-3:32b`（**thinking flow**） |
| 量子化 | **bf16** | **Q4_K_M** |

**二重に別物。本結果は base bf16 の J-space について何も licence しない。**
lens 作業に進むなら、bf16 で行動 probe が走るかを先に確かめる（REPORT §5-1／§5-2）。

## §7. 計器側の申し送り

- `NUM_PREDICT = 16384` は **OLMo には足りない**（4/20 が thinking で使い切り）。次走は **32768** を検討。⚠ ただし本 screen との数値比較は不可（生成上限が変わる = 計器変更）
- 1 件あたり最大 **2,987 秒**。20 件で 4h55m。PLAN の所要見積りに反映が要る
- thinking が別チャネルである件（本日 OLMo で踏んだ）は計器 docstring に記録済み

## §8. 射程外

- **base bf16 の挙動**（§6）
- **順位水準（J-space）の所見** —— 未測
- **なぜ族で分かれるのか** —— 機構を要する。本 screen は答えない
- **族を跨ぐ集計・曲線**（§4・[KAIME](KAIME_scale_axis_curve_20260728.md)）

## §9. 参照

計器 = `probes/olmo3-behavior-screen/screen_moy1.py` / 成果物 = `probes/olmo3-behavior-screen/results/screen_olmo-3_32b.json` /
[REPORT_olmo3_G0_to_claudeai_20260728](REPORT_olmo3_G0_to_claudeai_20260728.md)（G0 の L1 確定・lens 品質表）/
[PLAN_shinpan_kukan_exploration_20260728](PLAN_shinpan_kukan_exploration_20260728.md) / [KAIME_scale_axis_curve_20260728](KAIME_scale_axis_curve_20260728.md) /
`ConstructGap/exp/moy_suite_report.json`（qwen3:32b の凍結値）
