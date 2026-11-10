# PREREG(札 `mnw1b`): 札 mnw1 の続き — API の月の使用上限で欠番になった単位を、同じ prompt・同じ読み取り器・同じ判定で、要の cell から順に引く(Opus 5.5 xhigh・Fable 5.1 xhigh・API・2026-10-22 午後)

> **先生(10-22・逐語)**: 「$199の上限に当たったので、+$50しました」(console の写し: Monthly spend limit **$249**・**$202.93 spent**・Resets Nov 1 → 余裕 ≈ **$46**。promotional credit $171.49 / $200・11-17 まで)。
> **HEAD**(`R1`・fetch の後): `3914ceb5`(origin の先・push 待ち)。**凍結の実体**: 本書・runner [`ConstructGap/exp/mnw1b_moy5_continuation_after_usage_limit_20261022.py`](../../ConstructGap/exp/mnw1b_moy5_continuation_after_usage_limit_20261022.py)・launcher [`ConstructGap/exp/launch_mnw1b_20261022.sh`](../../ConstructGap/exp/launch_mnw1b_20261022.sh) を一つの commit に。runner は mnw1 の runner(凍結 `2c685fb2`)を **import して使うだけ**(PROMPT・score・call・table・verdict は mnw1 の物・md5 を pin)。mnw1 の札・runner・launcher と本札の三つのどれかが commit と違えば走らない。
> **身分**: 設計は mnw1 の [PREREG](PREREG_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md) のまま。本書は「何を・どの順で・いくらまで引くか」と、**開示**(mnw1 の部分の結果を見た後に書いている)だけ。

## §0. 開示
- mnw1 は 12:21 に API の月の使用上限(HTTP 400「You have reached your specified API usage limits …」)で止まった。取れた分 = [RESULT mnw1(部分・INCOMPLETE)](RESULT_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md)。mnw1 の取り直しの規則(無い単位は一度だけ)は、取り直しの回でも 400 を引いたので欠番が出た。
- **本書は mnw1 の部分の結果を見た後に書いている**(Opus: conf/Q1 0 / 20・none/Q1f 1 / 20・conf/Q1f 8 / 8 / Fable: none/Q1 0 / 20・none/Q1f 1 / 7)。mnw1 の予想 P1〜P6 は変えない(当たり外れは全部そろってから mnw1 の RESULT の改版に)。見た後の予想は §3 に**別の札**で書く。

## §1. 宇宙(mnw1 と同じ・引く単位だけ違う)
1. model・経路・effort・max_tokens・読み取り器・形の分類・費用の単価 = mnw1 §2〜§3 のまま。prompt の md5 = K `b0b1d14b…`・none/Q1 `ee39ba02…`・none/Q1f `f4522117…`・conf/Q1 `bb82c97e…`・conf/Q1f `f32c88a9…`・cone/Q1 `ec464241…`・cone/Q1f `2c50d183…`(runner が import 時に assert)。
2. **引く単位** = mnw1 の出力に text の無い (腕, rep)(dry): Opus 52 = conf/Q1f 12・cone/Q1 20・cone/Q1f 20 / Fable 93 = conf/Q1 20・conf/Q1f 20・none/Q1f 13・cone/Q1 20・cone/Q1f 20。rep の番号は mnw1 のまま(表は mnw1 + mnw1b の行を (腕, rep) で合わせる・同じ単位に両方の text が在ることは無い)。
3. **順**(先生の問いの要 = Fable の conf から): Fable = conf/Q1 → conf/Q1f → none/Q1f → cone/Q1 → cone/Q1f / Opus = conf/Q1f → cone/Q1 → cone/Q1f。各 4 worker・両 model は別 process で並走。
4. **上限** = Fable $34・Opus $5(合計 $39 < 余裕 $46・側の log の見積り・単価は list price)。上限に達した model は以後の単位を引かない。
5. **usage limit の 400**(文に "specified API usage limits")が返ったら、**その model は取り直さずに止まる**(mnw1 の規則の修正 = 一時の誤りと上限を分ける)。他の誤り(timeout・5xx)は一度だけ取り直す。引けなかった単位は欠番のまま。
6. 見積り: Fable は mnw1 の実測 ≈ $0.37 / 回(thinking 中央値 5k〜10k)→ 93 回 ≈ $34(上限と同額 = cone の後半が欠番になりうる)。Opus ≈ $0.06 / 回 → 52 回 ≈ $3。

## §2. 採点・判定
- mnw1 §3・§5 のまま(主 = cut・副 = cut_ans・余白 3・天井 17・関門は mnw1 で通過済み = Opus 9 / 10・Fable 10 / 10 を引き継ぐ)。`--read` は合わせた表に mnw1 の `verdict()` を当てる。
- RESULT = mnw1 の RESULT を**改版**(§1 の表を合わせた表に・§3 の当たり外れを全部の腕で)し、本札の走行(時刻・費用・欠番)を頭に足す。別 file にはしない。

## §3. 見た後の予想(`L2`・開示つき・mnw1 の P1〜P6 とは別に数える)
- **Q1(Fable conf/Q1)**: Opus と同じく cut ≤ 3 / 20(理由の欄にも補助定理の関係は書かれない)。ただし neq2f の名だけ 7 / 20 が在るので、Fable は Opus より上に出る余地がある(余白 3 で Opus を越えるかは五分五分)。
- **Q2(Fable conf/Q1f)**: cut_ans ≥ 15 / 20・焦点の形(FV : FP_x = FP_x : EJ)。
- **Q3(Fable none/Q1f の残り)**: 退化した比例が大半(cut_ans ≤ 3 / 20 で終わる)。
- **Q4(cone/Q1・両 model)**: cut ≤ 2 / 20・cut_ans 0〜1。
- **Q5(cone/Q1f・両 model)**: 退化した比例が多数。cut が出るなら頂点の形(VP_x²・HP_y²)が焦点の形より多い。cut_ans ≤ 5 / 20。

## §4. 主張しないこと
- mnw1 と mnw1b は同じ日・同じ経路・同じ鍵だが、間に上限の出来事を挟む二つの走行。表では card の欄で見分けられる。
- Fable の cone は上限で欠番になりうる(その時は INCOMPLETE のまま・cone は別の札)。
- mnw1 §8 の限定はそのまま。

## §5. 手順
- 凍結の commit の後、`bash /Users/manabu/lancedb-rag/ConstructGap/exp/launch_mnw1b_20261022.sh claude-fable-5-1` と `… claude-opus-5-5` を別 process で背景に。出力 = `ConstructGap/exp/results_mnw1b_moy5_20261022_<model>.jsonl`・側の log = `ConstructGap/exp/logs/mnw1b_moy5_20261022_<model>_sidelog.jsonl`。
