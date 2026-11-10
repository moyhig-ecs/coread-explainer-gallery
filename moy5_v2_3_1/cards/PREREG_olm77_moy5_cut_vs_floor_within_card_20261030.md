HEAD(R1) = 3a3cef95(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm77`・凍結 2026-10-30 夜): moy-5(線 2・L2-1)— cut の行の手前の寄り > 床の行の手前(olm67 Q3)は、同じ札(同じ問題文)の中でも在るか

- 発注(逐語): 先生 10-30 夜「この順で進める。」(= 主 session の推しの順 L2-1 → S-1 → L2-2)。設計の元 = Opus 監査の `conversations/2026-10-29/audit_plan_line1_line2/entry_opus_xhigh/PLAN_own.md` の L2-1。
- G10 の欄: 比べる物 = 「cut の行」/「床の行」 / 計器 = olm67 の series の J-lens 層 48 の走り込み 32 の u_CUT − u_FLOOR を、札ごとの中央値の差の平均(札の中の層別の置換)で読む物 / 雛形 = いいえ
- runner = [olm77_…py](../../ConstructGap/exp/olm77_moy5_cut_vs_floor_within_card_20261030.py)。読む物 = olm67 の series(893 行)・olm67 / olm68 の read.json・olm68 の `pseudo_events.json`。forward なし・API なし・MacBook。

## §0. 凍結の前に見た物(開示)

- olm67 Q3(全行)= cut 363 中央値 +0.0320・床 526 −0.0219・差 +0.0539・perm_p 0(read.json と Opus 監査 r02)。
- olm68 の区間ごと(全行)= [1–8] 差 +0.0426・[9–16] +0.0564・[17–32] +0.0388・[33–64] +0.0313・[65–128] −0.0082。model 別は [1–8] の Opus(差 +0.0295・p 0.055)など一部を見た。
- 札ごとの cut / 床 の行の数(Opus 監査 r09): neq3 91 / 29・mnw1b 31 / 58・essay4 0 / 86・neq4 60 / 21・neq6 50 / 23 ほか。宇宙の 6 札は述語で数え直して同じ(cut 284・床 210)。
- olm74 の L 対 O の model 別(r02)。
- **札の中の差(札ごとの cut の中央値 − 床の中央値)は見ていない**。合成の自己検査は合成の data だけを使った。

## §1. 宇宙と計器(R5)

- 宇宙 = olm67 の series の行のうち、cut ≥ 10 かつ 床 ≥ 10 の札の行 = **mnw1b・moy5e・neq3・neq4・neq5・neq6**(cut 284・床 210)。
  - 除外 = 他の 12 札(片側が 10 行未満)。neq3 の L の行は含める(olm67 の定義のまま)・除いた値は記述。
  - 走り込みが収まらない行(t < 32)は、その量から除く(数を書く)。
- 計器 = olm67 と同じ: u = 行の中の百分位(r / n)・diff = u(lens_CUT) − u(lens_FLOOR)・s32 = 出来事の 1〜32 token 前の diff の平均。
- 札の中の量 **W** = 6 札の(cut の中央値 − 床の中央値)の平均。検定 = 札の中だけで label を入れ替える置換 2,000 回(seed 7777 + 番号)・片側。

## §2. 統制(R6・どれか落ちたら読まない)

- **C0(写し)**: 全行の s32 の cut 対 床 の中央値の差が olm67 Q3 の diff(0.053864951245…)と 1e−6 以内・n が同じ。
- **C1(陽性)**: 宇宙の [1–8] の区間で W > 0 かつ p < 0.05(全行で一番強い区間が、札の中でも立つか)。
- **C2(陰性)**: 偽の出来事(olm68)の手前 32 で「W > 0 かつ p < 0.05」にならない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| Q1 | 札の中でも cut の手前の寄りが大きいか | W > 0 かつ 層別の置換 片側 p < 0.05 | 0.60 |
| Q2 | 6 札のうち差 > 0 の札 | ≥ 5 / 6(R3: 1 札の反転を許す) | 0.45 |
| Q3 | model ごと(Opus・Fable 別に Q1 と同じ検定・その model の cut ≥ 3 かつ 床 ≥ 3 の札だけ) | model ごとに ✓ / ✗ を書く(総計しない) | Opus 0.35・Fable 0.45 |
| Q4 | 記述 = logit lens の版・neq3 の L を除いた版・宇宙の中の全体の差 | — | — |

- L3(読み・確率つき): 「olm67 Q3 の差は札の構成(cut の多い札・床の多い札)だけでは説明されない」p = 0.60(解ける条件: Q1 ✓ で真・Q1 ✗ で偽)。
- 動かす主張(Opus 監査の計画): Q1 ✓ ∧ Q2 ✓ → 線 2 の判定「cut の手前で寄りが大きい」を「札の中でも」に上げる / ✗ → 「札の違いを含む」と限り、外向けの一文から「床の文の手前と比べて」を外して olm74 Q2(行の中の対比)だけで書く。

## §4. 止める規則

- C0 ✗(series の読み方が違う)→ 止めて runner を確かめる(関門は下げない)。
- 走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- 因果は言わない。frontier の本文を OLMo が読む時の話で、Opus・Fable の中の話ではない。
- 宇宙は 6 札(片側 10 行以上)に限る。床だけの札(essay4・neq1)は宇宙の外 = その札の床の行の寄りについては言わない。

## §6. 走らせ方

```
cd ConstructGap
python3 -I exp/olm77_moy5_cut_vs_floor_within_card_20261030.py --selftest   # 合成(凍結の前に通した・5 / 5)
python3 -I exp/olm77_moy5_cut_vs_floor_within_card_20261030.py --control    # C0〜C2 → olm77/control.json
python3 -I exp/olm77_moy5_cut_vs_floor_within_card_20261030.py --read       # Q1〜Q4 → olm77/read.json
```
