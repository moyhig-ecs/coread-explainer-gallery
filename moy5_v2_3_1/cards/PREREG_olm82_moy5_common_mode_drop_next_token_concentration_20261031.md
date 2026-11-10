HEAD(R1) = 7cfd396a(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm82`・凍結 2026-10-31): moy-5(線 2・図解の共読の一巡)— 場面の行 S1 の t+1 で語の集合が揃って落ちるのは、次の語の分布が少数の語に集まる位置だからか(S1 の t+1 の分布の広がりを同じ行の他の位置と比べる・場面の 3 行の全位置で共通の高さと広がりの順位相関)

- 発注(逐語): 先生 10-31 夕、図解(Opus の作り手・状態 19)を見て「t=1で急降下するのはなぜだろう？」→ 主 session の読み(L3)と、さらに確かめる二案 → 「読みを確認し、必要ならさらにへ進む」。
- G10 の欄: 比べる物 = 「S1 の t+1」/「同じ行の他の位置」 / 計器 = J-lens 層 48 と最終層(層 63 → norm → unembed)の、位置ごとの次の語の分布のエントロピーと一位の確率 / 雛形 = いいえ
- runner = [olm82_…py](../../ConstructGap/exp/olm82_moy5_common_mode_drop_next_token_concentration_20261031.py)。forward = zebrashark(場面の 3 行・olm67 と同じ forward_capture・層 48 と 63)。API なし。

## §0. 凍結の前に見た物(開示)

- 場面の行 S1(`fable__cut__0fba255642de.npz`・prf3 行 33・t = 684)の t−2〜t+3 の保存の値:
  - t+1(token「perpendicular」)で、lens の CUT・FLOOR・ATTR の u が揃って底(0.058・0.027・0.064)。
  - log Σp で約 7 nat 下がる(CUT −11.0 → −18.3)。t+2(「segments」)で戻る。
  - 保存の `logit_*`(= 層 48 の恒等の lens・最終層ではない)も同じ位置で揃って下がる。
  - **10-31 の主 session の答えで、これを「最終層でも」と書いたのは誤り**(olm67 の `lens_sets(H48, None)` = 層 48 を J なしで unembed した物)。
- S2・S3 の t−4〜t+5 の保存の u(図解の棚卸しの scenes.json と同じ値)。
- **分布の広がり・一位の確率・最終層の値は、どの行も見ていない**。他の行の t+1 も見ていない。

## §1. 行と計器(R5)

- 行 = 図解の棚卸しの `scenes.json` の 3 行(S1 自力・S2 道筋を渡された・S3 式だけ)の全位置。
- 位置 i の分布 = 位置 i までを読んだ後の次の語の分布。
  - **J** = 層 48 → J-lens → norm → unembed(olm67 の lens と同じ)。
  - **F** = 層 63(最後の層)→ norm → unembed(model の実際の出力・olm78 の最終層と同じ)。
- 量:
  - エントロピー H(nat)・一位の確率 p1。
  - 共通の高さ c = 三つの集合(CUT・FLOOR・ATTR)の log Σp の、行の中の百分位の平均。J と F それぞれで作る。

## §2. 統制(R6)

- **C0(写し)**: forward の J の三集合の log Σp が保存の `lens_*` と、差の中央値 ≤ 0.05 nat かつ 0.2 nat 以内の位置 ≥ 95 %(3 行とも)。✗ なら読まない。
- **C1(最終層の読み出しが本物の次の語の分布か = 陽性統制)**: F の一位の語が本文の実際の次の token と一致する位置の割合 ≥ 0.35(3 行とも)。✗ なら読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| Q1a | S1 の t+1 で、最終層の分布は少数の語に集まるか | F の H が行の中の下から 5 % 以内 かつ F の p1 ≥ 0.5 | 0.75 |
| Q1b | 同じことが J-lens 層 48 でも在るか | J の H が下から 5 % 以内 かつ J の p1 ≥ 0.5 | 0.65 |
| Q2 | 共通の落ちは分布の集まりと連れ立つか(図の lens の側) | 3 行それぞれで、J の c と J の H の順位相関 ρ ≥ 0.3(3 行とも) | 0.70 |
| Q3 | 記述 | F の c と F の H の ρ(3 行)・S2・S3 の t+1 の H の順位・一位の語 | — |

- L3(読み・確率つき): 「図の語の集合ごとの u が位置ごとに揃って上下するのは、次の語の分布の集まりの共通の成分で、S1 の t+1 の急降下はその一例」p = 0.65。
  - 解ける条件: Q1b ✓ かつ Q2 ✓ で真 / Q2 ✗(ρ < 0.3 の行が在る)で偽 / Q1b ✗ かつ Q2 ✓ で解けない。
- 動かす主張:
  - **Q1b ✓ ∧ Q2 ✓** → 図解の v1.1 に札「語の集合ごとの線の揃った上下 = 次の語の分布の集まり(共通の成分・判定の d は CUT − FLOOR の差でこれを打ち消す)」。SCOPE の記述に一行。
  - **Q1a ✓ ∧ Q1b ✗** → 最終層では集まるが、層 48 の lens の落ちは別の理由 = 記述のまま。
  - **Q2 ✗** → 読みは偽 → 図の札は付けない。
- 「さらに」の二つ目(多くの行の t+1 に共通の形か)は、Q1b ✓ ∧ Q2 ✓ なら**しない**(仕組みで説明が付き、判定の d は t より前の 32 だけで t+1 を含まない)。Q2 ✗ の時だけ先生に伺う。

## §4. 止める規則

- C0 か C1 が ✗ → 読まない。1 回で打ち切る。線を見てから替えない。
- 走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- 3 行だけの話で、多くの行の t+1 の形は言わない。
- 分布の集まりの「理由」(なぜ「Two perpendicular」の次が決まるか)は言わない。
- 因果・中の状態は言わない。OLMo が frontier の本文を読む時の話。

## §6. 走らせ方(zebrashark)

```
cd ConstructGap
P=~/miniforge3/envs/py314/bin/python3
$P -I exp/olm82_moy5_common_mode_drop_next_token_concentration_20261031.py --selftest   # model なし(凍結の前に通した・4 / 4)
$P -I exp/olm82_moy5_common_mode_drop_next_token_concentration_20261031.py --fire       # forward 3 行 → olm82/series/*.npz
$P -I exp/olm82_moy5_common_mode_drop_next_token_concentration_20261031.py --control    # C0・C1 → olm82/control.json
$P -I exp/olm82_moy5_common_mode_drop_next_token_concentration_20261031.py --read       # Q1〜Q3 → olm82/read.json
```
