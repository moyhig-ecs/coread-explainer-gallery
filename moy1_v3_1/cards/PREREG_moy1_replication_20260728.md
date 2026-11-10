# PREREG_moy1_replication_20260728.md
## moy-1 Claude 5 世代 **窓外再測定**（G1）— 実走前の凍結

> **起草**: 2026-07-28、Claude Code（Opus 5 / 1M context、実行層）。**先生 go**: 2026-07-28「G1 を走らせましょう」。
> **正準の指示**: [INSTR_from_claudeai_20260726d](../2026-07-26/INSTR_from_claudeai_20260726d.md) §1-1〜1-3 / [ADJUDICATION_table4_contamination_20260728](ADJUDICATION_table4_contamination_20260728.md) §4-2（行 schema 全体凍結）/ 帯・k・再現基準の裁定 = [RECORD §3-3](RECORD_pcl5_prereq_lexicon_textdomain_20260728.md)。
> **身分**: 本書は **実走前に凍結**する（commit hash が凍結の証拠）。§5 の決定規則は実走後に変更しない。
> **一行**: **窓内標本（Opus 5 のインシデント窓の内側で取得）に対する「再現」測定。恒等は要求しない。主量は surfacing margin M で、帯は先生裁定済み。**

---

## §1. 目的と意味論

窓内標本（2026-07-26・[RESULT](../2026-07-26/RESULT_moy1_claude5_baseline_20260726.md)）は **Opus 5 の incident monitoring 窓の内側**で取得された。先生方針により標本は破棄せず「傷つきの記録」として保持し、**本番掲載用に窓外で再測定**する。

**意味論は「再現（replication）」**。三名札（恒等 / 忠実な埋め込み / 修復）は **適用しない** —— これらは index 保守の検定意味論であり、その適用可能性は arm の順序保証の型から演繹される。**決定論保証を一切持たない closed API 標本は BM25 より下の保証階級**にあり、恒等を要求すれば検定が自壊する（INSTR d §1-3）。

## §2. Pre-flight（実走前の確認・記録）

| 項目 | 実測 |
|---|---|
| `status.claude.com` | **All Systems Operational**（2026-07-28 確認） |
| Opus 5 の直近インシデント | **2026-07-27 14:36 UTC に解決済**（他に 07-27 12:30 UTC、07-26 10:44 UTC） |
| 判定 | **窓外**。窓内標本の訂正 3（実走が monitoring 窓の内側だった）に対する前方修正 |

## §3. 測定設計（窓内と同一）

| 項目 | 値 |
|---|---|
| item / arm / deg | `higashida_circle` / A / 37.0 |
| conditions | `open` / `blocked` / `selection-supply` |
| cells | fable-5 ×3条件×{on} ×10 = 30 / opus-5 ×3条件×{on,off} ×10 = 60 = **計 90** |
| max_tokens | 16,000 / effort 未指定（既定 high） |
| sampling | temperature・seed とも API 非対応 → n=10 は同一条件の反復 |
| system prompt | 空 |
| prompt | ConstructGap `P.build` + `ARMS_APPEND` を verbatim。**md5 3 本とも窓内と一致を assert 済**（`3c7a63dd…` / `616682f5…` / `a8186b8a…`） |
| 分類器 | `run_moy1_concyclic_blocked.py::classify` verbatim（family #11） |
| lexicon | `lexicon_v2_frozen.json` md5 `e73e899f…` を assert してから読む |

⚠ **fable-5 の think=off は構成不能**（API が `{"type":"disabled"}` を 400 で拒否）。窓内と同じく**片側構成**であり、FAILED として数えない。

## §4. 窓内からの登録済み逸脱（3 件）

| # | 逸脱 | 理由 | 比較可能性への影響 |
|---|---|---|---|
| **D1** | `thinking.display="summarized"` を**明示指定** | 窓内は未指定＝既定 `"omitted"` で thinking 本文が空だった。thinking domain を **summary として登録する**（先生裁可）ために必要 | **無し**。`display` は**可視性のみ**を制御し、thinking の発生も課金も変えない（claude-api 正典）。計算内容は不変 |
| **D2** | 行 schema 全列を凍結し、**書込時と resume 時に assert** | 窓内で `stop_details` を後付けしたとき resume ガードが既存行に届かず、**refusal 3 件の category が永久に取得不能**になった。列を変えて同じ欠陥を作らないため、クラスごと閉じる（裁定 §4-2 条件 A） | 無し（記録側の強化） |
| **D3** | SDK = **anthropic 0.111.0**（窓内 0.120.0） | 共有 conda env（ingest / MCP が乗る）を実験のために動かさない判断。`display` は 0.111.0 でも型付き対応済みを確認 | **provenance 差として記録**。属性は defensive に取り、取れない列は D2 の assert で落ちる |

## §5. 決定規則（**凍結・実走後に変更しない**）

先生裁定 2026-07-28。register と主量の命名も同日裁可（`prompted` / `unprompted` / `surfacing margin`）。

```
S_prompted   = 凍結 lexicon の prompted register（\bHe\b \bHi\b \bHeHi\b・大小区別・語境界）
S_unprompted = 同 unprompted register（homothet similitude similicenter・大小無視・部分一致）
M = (S_prompted ∧ bind)[claude-opus-5] − (S_prompted ∧ bind)[claude-fable-5]   … surfacing margin
```

| ID | 予測 | 帯 | 判定単位 |
|---|---|---|---|
| **P-CL5a**（主） | `M ≥ 4/10` | 窓内の最小 7.0 に対し 3 の余裕 | condition 別（think=on の対） |
| **P-CL5b**（副） | `(S_prompted∧bind)[fable-5] ≤ 3/10` | 窓内の最大 1 に対し 2 の余裕 | condition 別 |
| **停止規則** | cell 内 `refusal ≥ 2` で**一時停止** | 窓内の cell 別最大は 1 | cell 別・分母 10 |
| **再現** | **全 condition で P-CL5a ∧ P-CL5b が成立** | **主基準のみ**。率の一致は判定に使わない | 全体 |

**併記量（記述登録のみ・帯を切らない）**: `S_unprompted ∧ bind` / `thinking_summary` の取得率 / `thinking_tokens` 分布 / `bind` 飽和の有無。

### 5-1. 帯を読むときの caveat（2 件・実走前に明記）

> ⚠ **前提改訂の pointer（2026-07-30 追補・本文は凍結のまま）**: 下の「87/87 = 天井」は計器欠陥（`center_mid`）を含む値だった。監査済みラベルでは **82/87** で **飽和は偽**（[RECONCILE_87_88](../2026-07-30/RECONCILE_87_88_ledger_20260730.md) / [RESULT_sensitivity_relabel](../2026-07-30/RESULT_sensitivity_relabel_20260730.md)）。⇒ **`S∧bind ≡ S` の caveat はこの標本では解消しうる**（この向きの誤りは *保守的* —— limitation を過大に述べていた）。⛔ 本 PREREG の判定規則は動かさない。

1. **`bind` は窓内で 87/87 = 天井**だった。天井が続くなら **`S∧bind ≡ S`** で、結合事象は S に潰れる。帯を結合事象に置くこと自体は正しい（窓外で bind が落ちれば結合が効く）が、**天井のままなら数値は S 単独と区別できない**。
2. **M は think=on の対でのみ定義可能**。fable-5 の think=off が構成不能なため、opus-5 の think=off 3 cell は M に入らず**記述に留まる**。

### 5-2. 窓内の参照値（対照・本測定の判定には使わない）

| condition | opus-5 | fable-5 | M(/10) |
|---|---|---|---|
| open | 0.80 | 0.10 | 7.0 |
| blocked | 1.00 | 0.00 | 10.0 |
| selection-supply | 1.00 | 0.00 | 10.0 |

## §6. 置き場所（意図的な逸脱・記録）

本測定は **`experiments/` ではなく `probes/moy1-claude5-replication/`** に置く。

`gen_appendix.py` は `experiments/*/results/*config*frozen*.json` を glob して**論文付録 Table 4** の行を作るため、house 規約どおりに凍結 config を `experiments/` へ置くと**論文付録表へ自動登録される**（2026-07-28 に機序を確定 = [FLAG §5-A](../2026-07-27/FLAG_table4_moy1_claude5_baseline_20260727.md)）。本測定は CommitStage の claims の外なので、収載対象外の木に置く。

**命名で glob を回避する小細工はしない** —— config は house 規約どおり `replication_config_frozen.json` と名付ける。回避を命名で行うと、脚注 v2 が主張する「the table reports the repository as it stands」を空洞化させる。**分けるのは場所であって名前ではない。**

→ `table4_watch.py` で drift 0 のままであることを実走前後に確認する。

## §7. 中止・停止条件

- cell 内 `refusal ≥ 2` → **一時停止**（凍結された停止規則）。行は保存済みで `run` 再実行により resume
- `ROW_SCHEMA` 違反 → **行を書かずに停止**（D2）
- prompt md5 が窓内と不一致 → **config 段で停止**（再現測定にならない）
- lexicon md5 不一致 → **verdict 段で停止**

## §8. 本 PREREG が射程に入れないもの（明示）

- **moy-5**。[PLAN §1](../2026-07-26/PLAN_post_submission_20260726.md) の G1 は「moy-1 90 件 **+ moy-5**」だが、**moy-5 には批准された帯が無く**、窓内 moy-5 は n=3 の暫定 L1（reason-read の正式判定も未了）。かつ窓内 moy-5 を書いた runner は repo に無く、標本 JSON に prompt が埋め込まれている形。**帯無しで走らせても再現の判定ができない**ため、本測定から外す。moy-5 の再測定は別 PREREG を要する
- P-CL5 の**縦断 readout 階層の命名**（先生留保のまま）
- Gate B ── そもそも P-CL5 側に登録された関門ではない（2026-07-28 に語の誤用を撤回済）

## §9. 参照

[INSTR_from_claudeai_20260726d](../2026-07-26/INSTR_from_claudeai_20260726d.md)（refusal / 結合事象 / 再現の意味論）/ [RECORD_pcl5_prereq §3-3](RECORD_pcl5_prereq_lexicon_textdomain_20260728.md)（帯・k・再現基準・命名の裁定と実測）/ [ADJUDICATION §4-2](ADJUDICATION_table4_contamination_20260728.md)（行 schema 全体凍結）/ [RESULT 窓内](../2026-07-26/RESULT_moy1_claude5_baseline_20260726.md)（対照）/ 計器 = `probes/moy1-claude5-replication/run_replication.py`
