HEAD(R1) = e467c70c(凍結時の HEAD・origin と同じ = この file と runner と MEMO を入れる commit の親)

# PREREG(札 `olm74`・凍結 2026-10-29 夜): moy-5 — 補助定理 XIV を見せた腕(neq3 の L-name / L-text = L・75 行)と他の cut の行(O・288 行 = 291 のうち cut の文の頭が 32 token 以上の行)を、CUT の語の集合の走り込み(cut の文の前 32 token の u_CUT − u_FLOOR)で比べ、「補助定理を渡すと前触れが消える」を olm68 の記述から凍結の判定に上げる。行ごとの統制 = 偽の出来事との差

- 発注(逐語): 先生 10-29「考察を記録し、次の札を起草。」(考察 = [MEMO](MEMO_consideration_line1_line2_after_olm73_20261029.md) §3)。
- runner = [olm74_…py](../../ConstructGap/exp/olm74_moy5_lemma_arms_vs_other_cut_rows_cut_word_set_20261029.py)。読む物 = [olm67](RESULT_olm67_moy5_frontier_cut_route_direction_and_language_space_20261029.md) の series(凍結の出力)+ [olm68](RESULT_olm68_moy5_cut_runup_time_profile_and_conditions_20261029.md) の `pseudo_events.json`。model なし・API なし・数分。

## §0. 凍結の前に見た物(開示)
- **向きは既に見えている**: olm68 §3 の札 × 腕(neq3 L-name −0.067・L-text −0.066・A +0.040・cut の行の全体 +0.032)/ olm69 §3 の CUT の寄り(本当 − 偽: A 8 / 16 +0.030・L 34 / 75 −0.022)。= 本札の Q1 は「記述を凍結の判定に上げる」札で、新しい発見の札ではない。
- **未計算**: L 対 O(291 行)の置換検定・行ごとの偽の出来事との差 d の L 対 O の比較(Q3)・O の d の符号検定(Q2)。
- 行の数: L 75・O 288(t ≥ 32 で 291 → 288)・偽の出来事は両群とも全行に在る(runner の試し = 数だけ・値は見ていない)。

## §1. 量と群
- 行 = olm67 の cut の行(366・K の腕は B1 で除外済み)のうち、cut の文の頭 t ≥ 32 の行。L = card が neq3 かつ arm が L-name/Q2・L-text/Q2。O = それ以外の cut の行(neq3 の A/Q2 16 を含む)。
- s_real = [t − 32, t) の (u_CUT − u_FLOOR) の平均(olm67 の `runup` と同じ・u = 行の中の百分位・J-lens 層 48)。s_pseudo = 偽の出来事(同じ行の別の文の頭・olm68)の前 32 で同じ量。d = s_real − s_pseudo。

## §2. 統制(R6)
- C0(再現): olm68 の `Q3_arms` の neq3 L-name / L-text の cut の行の s の中央値を同じ series から 1e-9 以内で再現。
- C1(陽性): cut の語を書く 1 token 前の u_CUT の中央値 ≥ 0.95(olm67 の C4 = 0.994 の再現)。
- C2(偽の出来事): 両群とも d が定義できる行 ≥ 95 %。
- 一つでも落ちたら読まない。

## §3. 予想(`L3`・外れてよい・10-29 裁可「裁可、凍結・発火」)
- **Q1**(群の差・本当の出来事): median s_real(L) < median s_real(O)、label の入れ替え 2,000 回(seed 7474)の片側 p < 0.05。
- **Q2**(O の前触れ・行ごとの統制つき): O で d > 0 の行 ≥ 60 % かつ 片側の符号検定 p < 0.05(= 自力の道の前触れは、同じ行の別の文の頭と比べても在る)。
- **Q3**(群の差・行ごとの統制つき): median d(L) < median d(O)、入れ替え 2,000 回(seed 7475)の片側 p < 0.05(= 行ごとの基準を引いても L は O より前触れが弱い)。
- **Q4(記述)**: Opus / Fable 別・L-name 対 L-text・neq3 の A(16)・neq3 を除いた O・L 対 neq3 を除いた O の Q1。
- 読み方: Q1 ✓ かつ Q3 ✓ →「補助定理を渡した腕では、cut の語の前触れが他の cut の行より弱い」と書ける(「消える」は L の d の符号検定が + に届かない時だけ添える・記述)。Q2 ✓ → 自力の前触れを行ごとの統制つきで言える。Q1 だけ ✓ → 行ごとの基準の違い(本文全体の性質)を除けない = 記述に留める。

## §4. 主張しないこと
- olm67・68 と同じ(OLMo が読む時の状態・答えの JSON・lens は記述・因果なし・差は百分位で数 %)。L は 2 腕 × 2 model の寄せ集め・O は札ごとに問題文・effort が違う。「補助定理を見せた」と「道筋を渡した」を同一視しない(読みの仮説)。O に neq3 の A(同じ問題文で見せない腕)が 16 行含まれる = Q4 で分けて出す。
