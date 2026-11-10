HEAD(R1) = 05ed6d84(凍結時の HEAD = この file と runner を入れる commit の親)

# PREREG(札 `olm69`・凍結 2026-10-29 午後): moy-5 — 補助定理 XIV を見せた腕(neq3 の L-name / L-text)で cut の文の手前の寄りが逆向きだった(olm68)のは、(語)cut の文の書き方が違い CUT の語の集合で捉えられないからか、(道)外から道筋を渡され前触れが立たないからか

- 発注(逐語): 先生 10-29「札の起草に進む」(= olm68 の RESULT §4-3・§5 の「cut の文の書き方の違いを分けていない」)。
- runner = [olm69_…py](../../ConstructGap/exp/olm69_moy5_neq3_lemma_arms_cut_sentence_words_20261029.py)。親 = [olm68](RESULT_olm68_moy5_cut_runup_time_profile_and_conditions_20261029.md)・[olm67](RESULT_olm67_moy5_frontier_cut_route_direction_and_language_space_20261029.md)。

## §0. 凍結の前に見た物(開示)
- olm68 の札 × 腕の表(neq3: A/Q2 +0.040・L-name/Q2 −0.067・L-text/Q2 −0.066)。行の数(A 16 = Opus 4・Fable 12 / L 75 = L-name 36・L-text 39)。tokenizer で補助定理の語(` Lemma` 86910・` lemma` 19340・` Newton` 21324・` XIV` 94515)。
- **neq3 の cut の文の本文・語は見ていない**(Q1 の答えになるため)。

## §1. 行と読ませ方
- 行 = B1 の neq3 の cut の行(K の腕を除く)= **91 行**。群 A = A/Q2(16)・群 L = L-name/Q2 + L-text/Q2(75)。
- olm67 と同じ読ませ方(本文だけ・MLX・J-lens 層 48)で forward し直す(層 48 だけ)。
- **自分の語(OWN)** = その行の cut の文(`first_lat_sent`)の中の単一 token の語で、英字 4 字以上・止め語(runner の STOP)でない・cut の文の前 64 token に出ていない物。行ごとに集合が違う。
- CUT = olm67 と同じ 5 語・LEMMA = ` Lemma`・` lemma`・` Newton`・` XIV`。
- 寄り = 行の中の百分位 u で、本当の出来事(cut の文の頭)の前 32 の平均 − 偽の出来事(olm68 の `pseudo_events.json` = 同じ行の別の文の頭)の前 32 の平均。

## §2. 統制(R6)
- C1(写し): 同じ行の lens_CUT が olm67 の series と一致(最大の差 < 1e-3)。
- C2(自分の語が在る): 群ごとに OWN が空でない行 ≥ 80 %。
- C3(陽性): cut の文の中の最初の OWN の語の 1 token 前で u_OWN の中央値 ≥ 0.95。落ちたら Q2・Q3 を読まない。

## §3. 予想(`L3`・外れてよい・10-29 裁可「Q1-4裁可、凍結、発火」)
- **Q1**(語・本文だけ): cut の文に CUT の語(similar・proportional …)が在る行の割合が、群 A − 群 L ≥ 0.20(= 補助定理を見せると cut の文の言い方が変わる)。
- **Q2**(群 L の自分の語の前触れ): 寄り(本当 − 偽)> 0 の行 ≥ 60 % かつ 片側の符号検定 p < 0.05(= 自分の語で測れば、補助定理の腕にも前触れは在る → olm68 の逆向きは「語」のせい)。
- **Q3**(群 A の自分の語の前触れ): 同じ関門(群 A は 16 行)。
- **Q4(記述)**: CUT・LEMMA の寄り(群 × 本当 − 偽)・Opus / Fable 別・cut の文に補助定理の語が在る行の数。
- 読み方: Q1 ✓ かつ Q2 ✓ →「語」の説明。Q1 ✗ かつ Q2 ✗ →「道」の説明に寄る。それ以外は混合として記述。

## §4. 主張しないこと
- olm67・68 と同じ(OLMo が読む時の状態・答えの JSON・lens は記述・因果なし)。OWN は行ごとに違う集合で、語の数・頻度が群で揃っていない(群 A は 16 行と小さい)。補助定理を見せた事と「外から渡された道」を同一視しない(読みの仮説)。

## §5. 費用
- API なし。forward 91 本(層 48 だけ・約 400 token)= 数分。
