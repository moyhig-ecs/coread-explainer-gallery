HEAD(R1) = acf991c1(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm79`・凍結 2026-10-30 夜): moy-5(線 2・L2-2)— 一語ずつの lens の系列は行の中の前触れ(d)を拾えるか(計器の感度)・拾えるなら、cut の文に出る CUT の語(一語)の前触れは自分の語(BODY)より大きいか

- 発注(逐語): 先生 10-30 夜「この順で進める。」(L2-1 → S-1 → L2-2 の 3 番目)。設計の元 = Opus 監査の `conversations/2026-10-29/audit_plan_line1_line2/entry_opus_xhigh/PLAN_own.md` の L2-2(= PLAN P2-2「前触れは概念の語に出る」を判定にかける)。
- G10 の欄: 比べる物 = 「cut の文に出る CUT の語(一語)」/「cut の文の自分の語(BODY)」 / 計器 = 層 48 の J-lens の一語ずつの log p の行の中の百分位で、同じ行の本当の出来事の手前 32 − 偽の出来事の手前 32(d) / 雛形 = いいえ
- runner = [olm79_…py](../../ConstructGap/exp/olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.py)。forward = **zebrashark**(cut の行 366・層 48 だけ・CUT の 5 語を一語ずつの系列にする)。自分の語の系列 = olm72 の保存の `lens_B0〜B2`(同じ model・同じ層の lens)。API なし。

## §0. 凍結の前に見た物(開示)

- 行の数(olm72 の series から・値は見ていない):
  - O の行(neq3 の L を除く cut の行)で、cut の文に CUT の語が在り、本当と偽の出来事の手前 32 が収まる行 = **77**(Fable 60・Opus 17)。77 行とも BODY の語も在る。
  - L の行 = 52(BODY も在る 50)。
  - 最初に出る CUT の語 = similar 101・proportional 23・geometric 2・proportion 2・similarity 1(O と L の計)。
- olm74 Q2(集合の d・O 288 行)= d > 0 が 192(0.667)・中央値 +0.0522。olm78 = その d の過半は語の積み上がり(r_W 0.575)・最終層では立たない。
- olm73 Q2 ✗(自分の語の計器)。olm71〜72 の一語の精度は 0.994〜0.997。
- **Sonnet 監査の P2-2 の行(10-29)のパイロット**: 「CUT 単独の d と比べると差が出ない(パイロット: 対の差 −0.0006)」= この札の Q1 にほぼ当たる量を、監査の文で読んだ(計算の中身・行の範囲は確かめていない)。
- この札の一語の系列の値は見ていない。

## §1. 計器

- 一語の系列 = 層 48 の J-lens の log p(CUT の語の id ごと)。行の中の百分位 u(olm66 の pct)。
- d(語)= u の本当の出来事(lat = cut の文の頭)の手前 32 の平均 − 偽の出来事(olm68)の手前 32 の平均(olm71 の `lean` と同じ型)。
- CUT の語 = cut の文の範囲で最初に出る CUT の id(5 語のどれか)。自分の語 = olm72 の BODY(最大 3 語・d は語の平均)。

## §2. 統制(R6)

- **C0(一語の精度)**: CUT の語の位置の 1 token 前の u の中央値 ≥ 0.95・その語が次に来ない無作為の位置で u > 0.95 の割合 ≤ 0.10(olm71 と同じ型・O と L の CUT の語の在る行)。✗ なら読まない。
- **C1(感度の陽性統制)**: O の行(77)で、CUT の語(一語)の d > 0 の行 ≥ 60 % かつ 符号検定 p < 0.05(= 集合で ✓ だった olm74 Q2 を一語で再現できるか)。
  - ✗ なら Q1〜Q3 を読まず、「一語ずつの計器は 32 token の走り込みを拾わない」と書き、olm73 Q2 ✗ を「言えない」に確定する(Opus 監査の計画の枝)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| C1 | 一語でも d が立つか(感度) | 上の通り | 0.55 |
| Q1 | O の行(77)で d(CUT の語)− d(自分の語)> 0 か | > 0 の行 ≥ 60 % かつ 符号検定 p < 0.05 | 0.20(Sonnet 監査のパイロット −0.0006 を見た後) |
| Q2 | model ごと(Opus 17・Fable 60) | Q1 と同じ型で model ごとに ✓ / ✗(総計しない・Opus は小 n) | Opus 0.15・Fable 0.20 |
| Q3 | L の行(記述) | — | — |

- L3(読み・確率つき): 「前触れは概念の語(CUT)に出て、自分の語には出ない」p = 0.20(解ける条件: C1 ✓ かつ Q1 ✓ で真・C1 ✓ かつ Q1 ✗ で偽・C1 ✗ で解けない)。
- 動かす主張: C1 ✓ ∧ Q1 ✓ → 「同じ行で、cut の文の中身の語より CUT の語に前触れが大きい」を判定に / C1 ✓ ∧ Q1 ✗ → 言えない / C1 ✗ → 一語の計器の線を閉じる。

## §4. 止める規則

- C0 ✗ → 読まない。C1 ✗ → Q1〜Q3 を読まない。
- この問いの計器は、どの結果でもこれ以上作り直さない(5 札 + 本札 = 6 札目で閉じる = Opus 監査の計画)。
- 走行の途中で PREREG と runner を書き換えない。

## §5. 言えないこと

- 因果・中の状態は言わない。frontier の本文を OLMo が読む時の話。
- CUT の語は cut の文で最初に出る一語だけ(5 語の集合ではない)。自分の語は olm72 の BODY の規則の語だけ。
- 一語の系列(この札の forward)と自分の語の系列(olm72 の forward)は別の forward だが、同じ model・同じ層の lens・同じ ids。

## §6. 走らせ方(zebrashark)

```
cd ConstructGap
python3 -I exp/olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.py --selftest   # model なし(凍結の前に通した・7 / 7)
python3 -I exp/olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.py --fire       # forward 366 行 → olm79/series/*.npz
python3 -I exp/olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.py --control    # C0・C1 → olm79/control.json
python3 -I exp/olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.py --read       # Q1〜Q3 → olm79/read.json
```
