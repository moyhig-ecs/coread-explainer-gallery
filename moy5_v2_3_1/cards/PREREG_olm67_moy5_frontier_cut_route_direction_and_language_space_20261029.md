HEAD(R1) = 14450faa(凍結時の HEAD = この file と runner を入れる commit の親)

# PREREG(札 `olm67`・凍結 2026-10-29 午後): moy-5 — Opus 5.5 / Fable 5.1 が cut に着いた本文(B1 の 366 行)と床だけの本文(527 行)を OLMo-3 32B base に読ませ、(Q1)方向 d̂ の係数が cut の文の前後で + 側へ動くか(olm64 の再現・拡大)、(Q2)lens が cut の語を先読みするか、(Q3)cut の文に至る道の言語空間が床の文に至る道と違うか

- 発注(逐語): 先生 10-29「moy-5についてはOpus-5.5やFable-5.1をカットに導いた道がOLMoの係数の励起や言語空間でどう見えるか解析する。」→「線2へ進みます。」
- 行 = [B1 の RECORD](RECORD_b1_moy5_frontier_cut_rows_collection_20261029.md)(14450faa)の `rows.jsonl` のうち cls = cut(Fable 214・Opus 152)と floor_only(Fable 257・Opus 270)・K の腕を除く = **893 行**。
- 親: [olm64](../2026-10-28/RESULT_olm64_moy5_frontier_routes_direction_readout_20261028.md)(方向 d̂・乱数の方向 2,000 本)・[olm63](../2026-10-28/RESULT_olm63_moy5_sae_calibration_notation_context_position_20261028.md)(frontier の本文の SAE は使わない)・[olm66](RESULT_olm66_moy1_aligned_onset_lookahead_he_separation_20261029.md)(行の中の百分位・先読み・1 token 前の陽性統制)。

## §0. 凍結の前に見た物(開示)
- B1 の数(RECORD)。本文の長さ(各組 30 本の抜き取り・中央値 353〜434 token・最大 1,207)。tokenizer で語の集合を確かめた(§2)。olm64 の runner(方向・乱数の較正)・olm60 の `events_of`・olm63 の「問題文なし」の作り。
- **OLMo の状態・lens の値は一つも見ていない。**

## §1. 読ませ方
- 入力 = 本文(`raw`・答えの JSON)だけ。**問題文は付けない**(札ごとに問題文が違うため・olm63 の S3 と同じ・olm64 は問題文 + 本文だった = 違いとして開示)。BOS は無い(`tok("")` = 空)。
- forward = olm4 の `forward_capture`(MLX・bf16)で層 32・48・63 を取る。生成はしない。
- 出来事 = olm60 の `events_of`(prf3 の読み取り器の文の切り方)で、cut の行は `lat`(最初の頂点の比例中項の文の頭の token)、床の行は `fd`(最初の焦点・準線の文の頭)。窓 = 前後 32(収まる行だけ)。

## §2. 計器
- **係数(Q1)** = olm64 と同じ方向 d̂(olm4 の think_b1 の train・層 32)への射影。後 32 の平均 − 前 32 の平均を d̂ に射影し、乱数の方向 2,000 本(seed 6464)の中央値の分布の 95 % 点で較正。
- **言語空間(Q2・Q3)** = J-lens(L-ref・層 48)→ RMSNorm → unembed → 集合の log Σ p を行の中の百分位 u に直す(olm66 と同じ)。logit lens は記述。集合(単一 token):
  - CUT = ` proportional`(55272)・` proportion`(21801)・` geometric`(53584)・` similar`(4528)・` similarity`(38723)
  - FLOOR = ` focus`(5357)・` focal`(42199)(` directrix` は複数 token で ` direct` が曖昧 = 入れない)
  - ATTR(Descartes)= ` coordinates`(14259)・` coordinate`(16580)・` quadratic`(80251)
  - ` mean` は平均と混じるので入れない。
- **先読み(Q2)**: w = cut の文の頭から後ろで最初の CUT の語の token。u(w − k)(k = 1..8)。乱数の位置 = 同じ行で後ろ 8 token に CUT の語が無い位置から各行 1 つ × 1,000 回。
- **道(Q3)**: 走り込みの窓 = cut の行は [t_lat − 32, t_lat)・床の行は [t_fd − 32, t_fd)。量 s = 窓の中の平均(u_CUT − u_FLOOR)。

## §3. 統制(R6)
- C1(lens): 全行の位置をまとめた中央値で 輸送の cos(J₄₈ h₄₈, h₆₃)> 恒等(h₆₃ は同じ forward の層 63)。Opus・Fable 別にも成り立つこと。落ちたら Q2・Q3 を読まない。
- C2(位置): cut の行の lat・床の行の fd が本文の token に位置づく ≥ 95 %・decode(ids) = raw ≥ 95 %。
- C3(方向): ‖d‖(層 32)が olm4 の 19.647 と 1e-3 以内(olm64 の C1 と同じ)。落ちたら Q1 を読まない。
- C4(先読みの陽性統制): u_CUT(w − 1) の中央値 ≥ 0.95。落ちたら Q2 を読まない。

## §4. 予想(`L3`・外れてよい・10-29 裁可「Q1-4裁可、凍結、発火」)
- **Q1**(係数・olm64 の拡大): cut の行の lat の前後で d̂ の射影が + 側へ動く行 ≥ 60 % **かつ** 中央値が乱数の方向の 95 % 点を超える(olm64 = 11 / 13・Opus 9 本 / Fable 4 本 → 366 本で)。Opus・Fable 別は記述。
- **Q2**(言語空間・先読み): u_CUT(w − 3) > 0.95 の行 ≥ 30 % **かつ** 乱数の位置の 95 % 点超え。
- **Q3**(道): 走り込みの s の中央値が cut の行 > 床の行、行の label を入れ替えた 2,000 回(seed 6767)で p < 0.05。Opus・Fable 別は記述。
- **Q4(記述)**: k = 1..8 の先読みの表(CUT・FLOOR・ATTR × J-lens / logit lens)・走り込みの窓の u の三つの集合の中央値(cut / 床 × Opus / Fable)・札ごとの Q1 の内訳。

## §5. 主張しないこと
- OLMo がその本文を読む時の状態で、Opus・Fable の中の状態ではない。本文は答えの JSON(思考の本文ではない)= 「導いた道」は答えの理由の欄の中の道。行は札ごとに問題文・effort が違う寄せ集め(均質な標本ではない)。方向は一本の線形の読み出し・lens は記述の読み・因果は言わない。

## §6. 費用
- API なし。forward 893 本 × 約 400 token(MLX・層 3 つ)= 数十分の見込み。`--read` = 乱数の方向 2,000・乱数の位置 1,000・入れ替え 2,000 で数分。
