HEAD(R1) = 2de07712(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm64`・凍結 2026-10-28 夜): moy-5 — Opus 5.5 / Fable 5.1 の本文(prf3 の 40 行)を OLMo-3 32B base に読ませ、olm4 の「答えて止まる」方向 d̂ への射影を、要の一文の前後と、apex(頂点の比例中項)/ 床(焦点・準線)の間で比べる。乱数の方向 2,000 本で較正(SAE を使わない)

- 発注(逐語): 先生 10-28「commit&push そして(a)」(= olm63 の RESULT §5-4 の (a)「方向の読み出し(olm4 の d̂・乱数の方向 2,000 本で較正・olm7 の型)で frontier の本文を読む」)。
- 親: [olm63](RESULT_olm63_moy5_sae_calibration_notation_context_position_20261028.md)(frontier の本文の SAE は使えない)・[olm60 停止](RESULT_olm60_moy5_frontier_routes_read_by_olmo_sae_STOPPED_at_C1_20261028.md)・[olm4](../2026-10-24/RESULT_olm4_commit_direction_and_public_sae_olmo3_32b_20261024.md)(方向・符号検定)・[olm7](../2026-10-24/RESULT_olm7_moy1_commit_direction_sae_lens_20261024.md)(乱数の方向の較正の型)・[olm6 (i)](../2026-10-24/RESULT_olm6_i_lens_readout_of_sae_latents_and_direction_20261024.md)(+d̂ = invariant・equality・relationships / −d̂ = approx・BUT・THEN)。読み方 = [ADJUDICATION 10-27](../2026-10-27/ADJUDICATION_reading_rule_frozen_text_literal_20261027.md)。
- runner = [olm64_…py](../../ConstructGap/exp/olm64_moy5_frontier_routes_direction_readout_20261028.py)(olm60 の rows / build / events_of を import)。

## §0. 凍結の前に見た物(開示)
- olm4 の read.json の `direction_norm`(層 32 = 19.647140502929688・層 48 = 25.967212677001953)と `sign_test`(L32 / L48 の test = 6 / 6)。方向の材料の行(think_b1 30 本)が在ること。方向そのものも、frontier の本文の射影も見ていない。

## §1. 宇宙(`L1`)
- 方向 = olm4 と同じ作り(think_b1 の閉じた行・seed 20261023 で半分 = train・d = commit 窓の平均 − mid 窓の平均・d̂ = d / ‖d‖・μ = 両窓の平均)。層 32 と 48。
- 行 = prf3 の 40 行・読ませ方は olm60 と同じ(問題文 + "\n\n" + 本文・生成なし・olm4 の `forward_capture`)。射影 = (h − μ)·d̂(本文の token ごと)。
- 出来事 = olm60 と同じ(prf3 の読み取り器の `fd` / `lat` / `sym` の最初の文の頭の token)。前 32 と後 32 の残差の平均。
- 較正 = 乱数の単位方向 2,000 本(seed 6464・5,120 次元の正規分布を正規化)で、同じ行・同じ窓の同じ統計量を作り、観測が乱数の何 % 点かを見る。
- 壊れた出力の行は予想から外す。

## §2. 統制(R6)
- **C1(方向の再現)**: 作り直した ‖d‖ が olm4 の記録と差 < 1e−3(層 32・48)。
- **C2(方向の陽性)**: olm4 の test の行で commit 窓の射影 > mid 窓の射影 = 全部(olm4 の 6 / 6)(層 32・48)。
- **C3(同じ計器)**: olm7 の 1 行の読み直しで cos 最小 ≥ 0.99。落ちたら発火しない。

## §3. 予想(凍結・`L3`・外れてよい)
- **Q1(apex を名指すと「答えて止まる」側へ)**: P5B × 壊れていない × `lat_sym` の行で、`lat` の後 32 − 前 32 の射影が正の行 ≥ 60 %・かつ その中央値が乱数の方向の中央値の 95 % 点より大きい(層 32)。
- **Q2(床では動かない = moy-1 の HeHi の形)**: P5 × 壊れていない × `fd_use` の行で、`fd` の前後の射影の差の中央値が乱数の 95 % 点を**超えない**(層 32)。
- **Q3(apex と床の間)**: 後 32 の射影の中央値で apex(P5B の `lat`)− 床(P5 の `fd`)> 0・かつ 乱数の方向の同じ差の 95 % 点より大きい(層 32)。
- **Q4(記述・閾なし)**: 層 48 の同じ量・model 別(Opus / Fable の本文)。
- **Q5(時間)**: ≤ 30 分。

## §4. 読み方・可読条件(R15)
- ADJUDICATION 10-27 を本札の凍結の文とする。Q1・Q2 の対象が **8 本未満なら「読まない」**(この文が凍結の文)。
- 「frontier の apex の文を読む時、OLMo の状態は『答えて止まる』側へ動く」と書けるのは Q1 ✓ の時だけ。「apex と床で違う」と書けるのは Q1・Q3 ✓ かつ Q2 ✓ の時だけ。
- 方向の符号の意味(+ = 関係を言い切る / − = 近似と逡巡)は olm6 (i) の lens の読みで、意味の同定ではない。

## §5. 主張しないこと
- **OLMo がその本文を読む時の状態**で、Opus・Fable の中身ではない。方向は moy-5 の OLMo の Think の行から作った一本の線形の読み出しで、frontier の本文での妥当性は乱数の較正で測るだけ。因果は言わない。prf3 の二次式は PROOF の一文が求めた物。

## §6. 費用(R14)
- 方向の作り直し(保存の窓だけ・forward なし)+ forward 40 本(層 32・48)+ C3 の 1 本 ≈ 10〜15 分。API なし。
