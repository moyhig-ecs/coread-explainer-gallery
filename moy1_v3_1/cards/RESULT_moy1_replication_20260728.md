# RESULT_moy1_replication_20260728.md
## moy-1 Claude 5 世代 窓外再測定（G1）— **再現した**

> **実行**: 2026-07-28、Claude Code（Opus 5 / 1M context、実行層）。M2 Ultra・API 直呼び。
> **事前登録**: [PREREG_moy1_replication_20260728](PREREG_moy1_replication_20260728.md)（commit `99e14d5` で**実走前に凍結**）。
> **身分**: **実測（L1）**。§4 の解釈は L2。§3 の判定は凍結された決定規則どおり機械的に行った。
> **一行**: **P-CL5a・P-CL5b とも 3/3 condition で HELD。窓外でも surfacing margin は 9〜10/10 で、窓内（7〜10）を帯基準で再現した。加えて、窓内では永久に取得不能だった refusal category が取れ、`cyber` だった —— 純粋な幾何 prompt に対する分類器の誤検知である。機序は追わず、観測と停止規則の較正のみ残した（§3-1b）。**

> # ⚠ 訂正 banner（2026-07-30・**計器欠陥 `center_mid`**・同一 retrieval unit に置く）
>
> ⭕ **P-CL5a / P-CL5b・M（9.0 / 9.0 / 10.0）は不変。** 判定は `thinking="on"` セルのみを読み、
> 該当する 19 依存行はすべて幾何的に正しい（[RESULT_pipeline_repro §4](../2026-07-30/RESULT_pipeline_repro_20260730.md) /
> [RESULT_sensitivity_relabel §3-3](../2026-07-30/RESULT_sensitivity_relabel_20260730.md)）。台帳上の身分は **監査不変（audited-invariant）**。
>
> ★ **訂正されるのは「bind = 89/89 = 天井」（§2 表・§5-2）である。** 凍結分類器 `bind_center_target` の `center_mid` 分岐が
> **「何の中点か」を見ずに** O1/O2 トークンの共在で O1O2 束縛と判定していたため
> （[FLAG_classifier_center_mid](../2026-07-29/FLAG_classifier_center_mid_20260729.md)）、`opus-5` / `thinking=off` の
> **4 行**（厳格）が誤アトラクタを答えながら `B-bind` と記録されていた。
>
> | 量 | 報告 | **監査済み** |
> |---|---|---|
> | bind / valid | **89 / 89**（飽和 **True**） | **85 / 89**（広義 82）⇒ 飽和 **False** |
>
> ⇒ **§5-2 の「bind は依然として天井（89/89）。したがって `S∧bind ≡ S` のままで caveat は解消していない」は撤回する。**
> **飽和が偽なら caveat は弱まる** —— この向きは **保守的**な誤り（limitation を過大に述べていた）。
> ⚠ 一方「bind = 天井」自体は **anti-conservative**（能力を過大評価）。**向きは claim ごとに違う**
> （[AUDIT_flip_direction §2](../2026-07-30/AUDIT_flip_direction_20260730.md)）。
>
> ⛔ **`replication_runs.json` のラベルは上書きしていない。** 更新は本 banner による**文書追補**である。

---

## §1. 実行条件

| 項目 | 値 |
|---|---|
| pre-flight | `status.claude.com` = **All Systems Operational**（Opus 5 の直近インシデントは 07-27 14:36 UTC 解決済）→ **窓外**を確認して凍結 |
| 実走 | 2026-07-28 15:07–15:30 JST・**90 呼び出し・err 0 件** |
| prompt md5 | 3 本とも**窓内と一致を assert**（`3c7a63dd…` / `616682f5…` / `a8186b8a…`） |
| lexicon | `lexicon_v2_frozen.json` md5 `e73e899f…` を assert |
| 分類器 | `run_moy1_concyclic_blocked.py::classify` verbatim |
| コスト | **$3.39**（事前見積り $3.14） |

記録 = `probes/moy1-claude5-replication/results/replication_runs.json`

## §2. 判定（凍結された決定規則どおり）

```
M = (S_prompted ∧ bind)[opus-5] − (S_prompted ∧ bind)[fable-5]
P-CL5a (主): M ≥ 4/10      P-CL5b (副): (S_prompted∧bind)[fable-5] ≤ 3/10
再現 = 全 condition で P-CL5a ∧ P-CL5b（主基準のみ）
```

| condition | opus-5 | fable-5 | **M(/10)** | P-CL5a | P-CL5b |
|---|---|---|---|---|---|
| open | 0.90 | 0.00 | **9.0** | **HELD** | **HELD** |
| blocked | 1.00 | 0.10 | **9.0** | **HELD** | **HELD** |
| selection-supply | 1.00 | 0.00 | **10.0** | **HELD** | **HELD** |

**P-CL5a: 3/3 HELD ／ P-CL5b: 3/3 HELD ／ 再現 = ✅**

### 2-1. 窓内との対照

| condition | 窓内 M | 窓外 M |
|---|---|---|
| open | 7.0 | **9.0** |
| blocked | 10.0 | **9.0** |
| selection-supply | 10.0 | **10.0** |

**帯 4 に対し、両標本とも最小 7.0。** 二モデルの解離は窓の内外で保存された。

| | 窓内 | 窓外 |
|---|---|---|
| refusal | **3 件**（全て Opus 5・走行末尾 5 分に集中） | **1 件** |
| refusal の cell 別最大 | 1 | 1（**停止閾値 k=2 は発火せず**） |
| bind | ~~87/87 = 天井~~ ⇒ **82/87**（監査済み・2026-07-30） | ~~**89/89 = 天井**~~ ⇒ ★ **85/89**（広義 82）**= 天井でない** |
| stop_reason | end_turn 87 / refusal 3 | end_turn 89 / refusal 1 |

## §3. 登録済み逸脱の成果

### 3-1. D2 —— **窓内で永久に失われたものが取れた**

窓内では `stop_details` を runner に後付けしたが resume ガードが既存行に届かず、**refusal 3 件の category は永久に取得不能**になっていた（[FLAG §5-A-4](../2026-07-27/FLAG_table4_moy1_claude5_baseline_20260727.md)）。行 schema を全列凍結し書込時に assert する前方修正の結果、今回は取れた:

```
claude-opus-5 | selection-supply | think=on | rep=2
  stop_details = {'type': 'refusal', 'category': 'cyber',
                  'explanation': "This request triggered restrictions on violative
                   cyber content and was blocked under Anthropic's Usage Policy. …"}
  content_len=0  thinking_tokens=90  output_tokens=167
```

> **⚠ category = `cyber`。** 対象は**二円の共通接線と交点の共円性**を問う純粋な幾何 prompt であり、cyber 要素は一切含まれない。**分類器の誤検知（false positive）**である。
>
> これは窓内の provenance の読みを**変える**: 窓内の refusal 3 件を「インシデント窓の内側で起きた」と記録したが、**category が cyber である以上、elevated errors とは別系統**の可能性が高い。窓内では category が取れなかったため、この切り分け自体が不可能だった。
>
> **今回も窓外（All Systems Operational）で 1 件出ている**ことが傍証になる。refusal はインシデントの関数ではなく、**この prompt に対する分類器の定常的な誤検知率**（窓内 3/90・窓外 1/90）と読むほうが素直。

⚠ ただし**因果は立てない**。n が小さく、両標本とも同一 item・同一 prompt である。

**schema 完全性**: 全 90 行の key 集合は **1 種類・18 列**。D2 の assert が通っている。

### 3-1b. 考察 —— 追わないと決めた上での所見（先生判断 2026-07-28「そこは追いたくない」）

#### (a) refusal は **二重に不可視**である

`refusal` は HTTP 200 で返るため、**status page の error 指標にも、harness の例外ハンドラにも載らない**。見えるのは `stop_reason` だけである。

我々自身がこの盲点を踏んでいる —— 窓内の訂正 1 は「runner が `stop_reason` を見ずに `content` を分類し、部分出力の残った refusal を `B-bind` と数えていた」だった。**status page が refusal を error として数えないのと、我々の runner が refusal を成功として数えたのは、同じ構造の見落とし**である。`claude-api` 正典が「`content` を読む前に `stop_reason` を確認せよ」と書いているのは、この二重不可視性ゆえと読める。

#### (b) 「インシデント窓の傷」は事実だが、**中身が空だった**

窓内標本は monitoring 窓の内側で取得された —— これは時刻の事実として動かない。しかし今回、**両標本とも HTTP エラー 0 件**であり、**窓内でも障害の症状を一度も観測していない**。さらに帯基準で再現が成立した（M 7〜10 → 9〜10）。

→ **provenance の傷は真だが、測定への影響は一度も示されていない。** 窓内標本を「汚染された標本」として扱う根拠は無い。対照として並置するという先生裁定（2026-07-26）が、結果的に正しい扱いだった。

#### (c) 誤検知は実在するが、**機序は不明のまま閉じる**

- 条件 append を精査したが、cyber 判定を引きうる語は**一つも無い**（`blocked` = 円の一意同定要求 / `selection-supply` = 直径のヒント）。base も座標と円のみ
- **条件依存は立たない**。両標本あわせた refusal 4 件は `selection-supply` 3 / `blocked` 1 / `open` 0 だが、条件を事後に選んだ補正込みで **偶然確率 0.33**（= 3 回に 1 回起きる）。⚠ 実行層が一度「prompt の中身に紐づく」と読んだのは**過剰読み**であり、ここで撤回する
- モデル別は fable-5 **0/60**・opus-5 **4/120**（区別はつかない・記述のみ）

→ **「純粋な幾何 prompt に cyber 誤検知が定常的に出る」という観測だけを残し、機序は追わない。** 追うなら base 単独と append つきを分けて n を積む切り分けになるが、率 ~2% では数十件では決着しない。**割に合わないという判断**（先生）。

#### (d) **凍結した停止規則 k=2 の較正** —— 1 走あたり約 1/6 で偶然発火する

両標本あわせた定常率 p = 4/180 = **0.0222** を使うと:

| | 確率 |
|---|---|
| 1 cell（n=10）で refusal ≥ 2 | 0.0197 |
| **1 走（9 cell）でどこかの cell が k=2 に達する** | **0.164** |

→ **k=2 の停止規則は、異常が無くても約 6 走に 1 回発火する。** これは規則の欠陥ではない（停止は「判断を仰ぐ」であって「異常の断定」ではない）が、**発火したときの第一仮説は「偶然」であって「インシデント」ではない**と読み方を固定しておく。

⛔ **凍結規則そのものは変更しない**（実走後に決定規則を動かさない）。本項は**読み方の記録**である。次回 PREREG で k を見直す場合は、この較正値を根拠として実走前に凍結する。

### 3-2. D1 —— thinking domain が **summary として** 取れた

`thinking.display="summarized"` の明示指定により、**60/90 行**（= think=on の全行）で thinking 本文が取れた。**窓内は 0 行**（display 未指定＝既定 `omitted` で空だった）。

```
例: "I'm verifying that the four intersection points of the common tangents are
     concyclic, centered at the midpoint of the two circle centers. Computing the
     distances from the midpoint to each intersection point confirms they're all
     equidistant, …"
```

`thinking_tokens` = 90〜3466。

⛔ **これは rollout ではなく summary である**（先生裁可の名札）。生の chain of thought は closed API のどのモデルでも露出しない。**`thinking-rollout` という名札は使わない。**

## §4. 記述登録（帯を切らない）

### 4-1. `S_unprompted ∧ bind`

| cell | 窓内 | 窓外 |
|---|---|---|
| opus-5 / open / on・off | 5/10・5/10 | 4/10・6/10 |
| opus-5 / blocked / on・off | 4/10・9/9 | 6/10・10/10 |
| opus-5 / selection-supply / on・off | 4/9・5/9 | 8/9・3/10 |
| fable-5（3 条件とも） | 1/10・0/10・0/10 | 0/10・0/10・0/10 |

### 4-2. 0.5 手目 seed の追試（[PLAN §4](PLAN_shinpan_kukan_exploration_20260728.md)）

密度 = unprompted 出現数 / 応答文字数 × 1000（**長さ交絡を除いた量**）:

| condition | 窓内 on → off | 窓内 比 | 窓外 on → off | 窓外 比 |
|---|---|---|---|---|
| open | 0.52 → 0.51 | 0.98× | 0.34 → 0.44 | 1.30× |
| **blocked** | **0.34 → 1.32** | **3.93×** | **0.58 → 1.43** | **2.47×** |
| selection-supply | 0.34 → 0.49 | 1.42× | 0.66 → 0.23 | **0.34×** |

- **`blocked` は両標本で同方向・同程度**（3.93× / 2.47×）→ **seed は追試された**
- **`open` は両標本とも差が立たない**（0.98× / 1.30×）→ **closure-forcing 特異性を支持**
- **`selection-supply` は符号が反転**（1.42× → 0.34×）→ **不安定。この条件は seed の射程外**

⛔ **これは確認であって検定ではない。** PREREG は `S_unprompted` を記述登録としてのみ凍結しており、帯を切っていない。**事後に予測として読み替えない。**

## §5. 解釈（L2）

1. **二モデルの解離は窓の内外で保存された。** M は 7〜10 の帯に収まり、帯 4 に対して余裕がある。窓内標本がインシデント窓で取得されたことは、**この解離の観測を汚していなかった**
2. ~~**bind は依然として天井**（89/89）。したがって **S∧bind ≡ S** のままで、結合事象は S に潰れている。[PREREG §5-1](PREREG_moy1_replication_20260728.md) の caveat は解消していない~~
   ⇒ ## ⚠⚠ **撤回（2026-07-30）**: 監査済みラベルでは **85/89**（広義 82）で **飽和は偽**。⇒ **caveat はこの標本では解消しうる**。冒頭 banner と [RESULT_sensitivity_relabel §3-1](../2026-07-30/RESULT_sensitivity_relabel_20260730.md) 参照。**この撤回は台帳を強める向きである**（limitation を過大に述べていた）
3. **refusal の正体が変わった。** 窓内では「インシデント窓の傷」と読んだが、category が `cyber` かつ窓外でも発生する以上、**この prompt に対する分類器の定常的誤検知**と読むほうが素直。ただし n が小さい
4. **⚠ 本測定の射程**: 1 item・1 角度・n=10・2 モデル。「呪いが世代的に解けた」と一般化しない

## §6. やらないこと / 未了

- **moy-5 は射程外**（PREREG §8）。帯が無く、窓内は n=3 の暫定 L1 で runner も repo に無い。別 PREREG を要する
- **窓内標本は破棄しない。** 対照として並置する（先生裁定 2026-07-26）
- 本測定は `probes/` 配下 —— 論文付録 Table 4 の glob 対象外。`table4_watch` で drift 0 を実走前後に確認済

## §7. 参照

[PREREG_moy1_replication_20260728](PREREG_moy1_replication_20260728.md)（凍結 = commit `99e14d5`）/ [RESULT 窓内](../2026-07-26/RESULT_moy1_claude5_baseline_20260726.md)（対照）/ [RECORD_pcl5_prereq §3-3](RECORD_pcl5_prereq_lexicon_textdomain_20260728.md)（帯・命名の裁定）/ [PLAN_shinpan_kukan_exploration](PLAN_shinpan_kukan_exploration_20260728.md) §4（0.5 手目）/ 計器 = `probes/moy1-claude5-replication/run_replication.py`
