# PREREG_pc1_cue_invariance_20260730.md
## `CUE/P-C1` —— cue 不変性 probe（**実走前に凍結**）

> **凍結**: 2026-07-30、Claude Code（実行層 / Opus 5 1M）。**★ 本書の commit をもって予測を凍結する。実走は commit 後。**
> **裁可**: [ADJUDICATION_throne_move0 §7](ADJUDICATION_throne_move0_20260730.md) 裁可事項 2（命名・事前登録）+ 5（推奨順 P-C1 → 探検 B）。先生一括裁可 2026-07-30（[RECORD](RECORD_ratification_throne_move0_20260730.md)）。
> **申し送り（拘束）**: **「P-C1 の予測は run 前に凍結済みの扱い。ログより先に走らせないこと —— 先に走ればアークは anecdote に落ちる」**
> **一行**: **cue `"\n"` が base の行動分布に中立であることを、`" "` と `"\n\n"` との比較で確かめる。動けば A は再開し、探検 B の結果は cue 条件付きへ降格する。**
> ★ **札**: 本書の `P-C1` は **`CUE/P-C1`**（cue invariance 系列）である。裸札 `P-C1` は [PREREG_REGISTRY §2](../../PREREG_REGISTRY.md) により **`CE/P-C1`（closure erasure・公開済み）**に束縛されているので、**本書では必ず prefix 付きで読むこと**。


---

## §1. 目的と身分

**目的**: [ADJUDICATION §0.5](ADJUDICATION_throne_move0_20260730.md) が指摘した単一致命傷の解消 ——
「文字列レベルの不変（命題・語彙を変えない）」と「**分布レベルの不変（継続分布を変えない）**」は別命題である。
`"\n"` は**段落頭の prior を立ち上げ得る**。⇒ **cue 中立性は現状 L2 仮定であり、これを実験的に扱う。**

**身分**: ⛔ **probe（事前登録つき）。screen ではない。** ただし **n=10/cell で検出力は低い**（§5）⇒
**「大きな移動が無いこと」の確認であって「不変の証明」ではない。**

## §2. 設計（**単一変数**）

| 項目 | 値 |
|---|---|
| 物体 | `allenai/Olmo-3-1125-32B`（**base**・bf16・mlx。lens が張られている当の物体） |
| payload | 凍結 prompt の `open` / `blocked` を **verbatim**。★ **payload md5 assert**（`open` = `3c7a63dd0d2b4393820e7836458e33cd` / `blocked` = `616682f531557c56d1103738b8d9dbda`）—— 裁可事項 1 の新規律どおり、assert は payload に置く |
| ★ **変える唯一の変数** | **cue** ∈ **{`"\n"`, `" "`, `"\n\n"`}**（payload の直後に後置。framing として腕別登録） |
| 固定 | `MAX_NEW=32768` / `CONDITIONS=["blocked","open"]` / `RUNS = temp0(seed 0) + temp0.7(seed 1..9)` = 10/cell / chat template なし（E1）/ 全文分類（E2）/ 分類器 `run_moy1_concyclic_blocked.classify` **verbatim** |
| 実装 | `probes/olmo3-pc1-cue-invariance/run_pc1.py` —— ⛔ **凍結 screen を再実装しない**（family #11）。`screen_base.py` の定数・`load_prompts` を **import して cue のみ差し替える** |
| 既存データの再利用 | ★ `cue="\n"` は **07-29 の凍結 screen をそのまま使う**（再走しない・再採点しない）。新規生成は `" "` と `"\n\n"` の **2 cue × 2 条件 × 10 = 40 世代** |
| 規模見積り | 07-29 実測 wall（blocked 3881s + open 1529s = 5410s/cue）から **約 3 時間**（±・cap 到達で伸びる） |

### 2-1. 既存 `"\n"` の値（**参照点・凍結**）

| 条件 | n | labels | attractor | `hit_cap` |
|---|---|---|---|---|
| **blocked** | 10 | `B-attractor` 4 / `B-bind` 3 / `B-flail` 2 / `B-stuck-L1` 1 | **4/10** | 1 |
| **open** | 10 | `B-attractor` 5 / `B-stuck-L1` 4 / `B-bind` 1 | **5/10** | 0 |

⇒ 最頻ラベルは **両条件とも `B-attractor`**。

## §3. ★ 予測（**run 前凍結**・[ADJUDICATION §1-5](ADJUDICATION_throne_move0_20260730.md) の文言どおり）

> **最頻ラベルと attractor 率は、cue 変種間で二項ノイズ内で不変である。**

**操作化**（実走前に固定する）:

| # | 判定量 | 不変の条件 |
|---|---|---|
| **CUE/P-C1-a**（主） | 条件ごとの **attractor 数**（`k/10`） | 3 cue の 2×3 分割表（attractor / 非attractor）に **Fisher の正確検定**（両側）→ **`p > 0.05`** |
| **CUE/P-C1-b**（副） | 条件ごとの **最頻ラベル** | **3 cue で同一**（`B-attractor`） |

**不変 = CUE/P-C1-a ∧ CUE/P-C1-b が両条件で成立。**

⚠ **同順位（tie）の扱いを先に決める**: 最頻ラベルが同数で並んだ場合は **`B-attractor` を含む tie は「同一」と数える**（保守的側 = 不変と判定しにくい方に倒さない、を明示的に選ぶ。事後の選択を作らない）。

## §4. 決定表（凍結・[ADJUDICATION §1-5](ADJUDICATION_throne_move0_20260730.md)）

| 結果 | 帰結 |
|---|---|
| **不変** | **【諮問 A】確定**（cue は計器の一部）。**探検 B の結果は通常昇格。** base 腕の「cue 条件付き」フラグを外す |
| **不変でない** | **【諮問 A】再開。** 探検 B の結果は **cue 条件付きへ降格**。**Think fit が本命復帰**（32B: 1.42 GPU 時間 = 復活条件 (α)）。★ **予測失敗は drink** |

## §5. ⚠ 限界（実走前に明記）

1. ★ **検出力が低い。** n=10/cell・p̂≈0.4–0.5 の二項では 95% 区間が広く、**中規模の移動を見逃す**。
   ⇒ 本 probe は「**大きな移動が無いこと**」の確認である。**「不変の証明」ではない**（**帯を切らない**）
2. **framing 種別間の介入強度差は測っていない**（[ADJUDICATION §6](ADJUDICATION_throne_move0_20260730.md) の自己申告どおり）。
   cue 3 種はいずれも「1〜2 文字の空白系終端」であり、**chat template との同格性は本 probe の射程外**
3. **token / likelihood レベルの腕間比較は射程外**（裁定 §1-4 (c) の限定を継承）
4. `temp=0.7` の 9 seed は**同一条件の反復**であって独立標本の増加ではない（既定の規律）

## §6. D 分母規約の適用（裁可事項 3・**本 probe にも適用**）

| カテゴリ | 扱い |
|---|---|
| `truncated(limit)`（cap 到達だが answer 形の続きが出ている・base 側） | **primary 分母から除外 + 全行込みを並記**（sensitivity） |
| `no-answer(limit)`（answer 不在） | **測定不成立**・分母外。**ラベル別建て・合算禁止** |

⇒ **CUE/P-C1-a は primary 分母（`truncated` 除外）で判定し、全行込みを並記する。**

## §7. ⛔ してはならないこと

- **本書の commit より先に走らせること**（申し送りの拘束）
- 既存 `cue="\n"` 行の**再走・再採点**
- 凍結 payload 文字列の改変（cue は**後置**であり payload に触れない）
- 分類器の変更（`classify` verbatim・O-14 は未実装）
- 結果を見てから判定量・tie 規則・分母規約を選ぶこと
- 「不変だった」から「cue は分布に中立」への **L1 昇格**（§5-1）

## §8. 成果物

`RESULT_pc1_cue_invariance_20260730.md`（生成 40 行 + 既存 10×2 行の並記表・Fisher の p・決定表の適用・限界）
生データ = `probes/olmo3-pc1-cue-invariance/results/pc1_runs.json`

## §9. 参照

[ADJUDICATION_throne_move0_20260730 §0.5・§1-5・§3・§6・§7](ADJUDICATION_throne_move0_20260730.md) /
[RECORD_ratification_throne_move0_20260730](RECORD_ratification_throne_move0_20260730.md)（一括裁可）/
[RESULT_olmo3_base_bf16_screen_20260729](../2026-07-29/RESULT_olmo3_base_bf16_screen_20260729.md)（`cue="\n"` の凍結 screen = 参照点）/
凍結計器 = `probes/olmo3-base-bf16-screen/screen_base.py`（**import して再利用**）
