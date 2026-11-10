HEAD(R1) = 6e92d6aa(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm60`・凍結 2026-10-28 午後): moy-5 — Opus 5.5 / Fable 5.1 が辿った道(prf3 の本文)を OLMo-3 32B base に読ませ、作図で着目している部分(焦点・準線 / 頂点の比例中項 / 二次式の文)と、層 32 の SAE の推移を token で揃える

- 発注(逐語): 先生 10-28「並行して、札を起草しながら Opus・Fable で辿った道が、OLMoでどう活性化するか読んでいきましょう。」(前段 =「作図で着目している部分と…対比的に図解する」→「SAEによる活性の推移で通じますか？」)
- 親: [olm59](RESULT_olm59_moy1_sae_trajectory_by_construction_mentions_20261028.md)(moy-1: O1O2 を名指した後に「考えの中点」の群が上がる 48 / 59・HeHi では動かない 18 / 34)・[olm4](../2026-10-24/RESULT_olm4_commit_direction_and_public_sae_olmo3_32b_20261024.md)(moy-5 の群・SAE)・[prf3](../2026-10-21/RESULT_prf3_moy5_confirm_lattice_bundle_claude_p_20261021.md)(行・読み取り器の欄)。読み方 = [ADJUDICATION 10-27](../2026-10-27/ADJUDICATION_reading_rule_frozen_text_literal_20261027.md)。
- runner = [olm60_…py](../../ConstructGap/exp/olm60_moy5_frontier_routes_read_by_olmo_sae_20261028.py)。

## §0. 凍結の前に見た物(開示)
- 要の一文を本文の位置に戻す部分だけを試した(model・SAE なし): 最初の実装は本文を `json.loads` で読み、```json の囲みのある 8 行で 18 / 69 の文を見失った → prf3 の読み取り器自身の取り出し(`parse_conj`)に替えて 69 / 69。活性の値は見ていない。
- olm59 の結果(上の親)を見てから予想を立てた。

## §1. 宇宙(`L1`)
- 行 = `results_prf3_20261021.jsonl` の 40 行(Opus 5.5 / Fable 5.1 × P5(問い + PROOF・近道が開いている)/ P5B(+ BLOCK・近道を塞ぐ)× r0〜r9・claude -p・max)。
- 読ませ方 = **OLMo は生成しない**。ids = tok(prf3 の問題文 `PROMPT[arm]`(prf3 の module が md5 31387680 / d8172a5c を assert)+ "\n\n")+ tok(本文 raw・special なし)。olm4 の `forward_capture`(olm7 が残差を取ったのと同じ部品)で層 32 の残差を全 token で取り、本文の部分(g0 から)を読む。
- SAE = 公開 SAE 層 32・threshold(olm59 と同じ)。群 = **olm4 が凍結した moy-5 の 3 組**(選び直さない): `close5` = commit − mid 上位 20・`mid5` = mid − commit 上位 20・`dir5` = 方向と cos の上位 20(`olm4/read.json` の `sae_top_latents`)。群の値 = 群の latent の平均。
- 作図で着目している部分 = prf3 の読み取り器が凍結した欄(本文を prf2 の `_SPLIT` で切った文の番号): `fd` = 最初の焦点・準線の文(`fd_use_sents[0]`)・`lat` = 最初の頂点の比例中項の文(`first_lat_sent`)・`sym` = 最初の二次式の文(`first_sym_sent`)。出来事 = その文の最初の token。前 32 と後 32 の群の平均を比べる。
- 壊れた出力(`malformed`)の行は予想の対象から外す(記述には件数を書く)。

## §2. 統制(R6)
- **C1(計器が frontier の本文に合うか)**: 本文の token 640 本(20 行 × 32・seed 6060)で FVE ≥ 0.40・L0 100〜280。落ちたら発火しない(SAE は OLMo の本文で学習したので、外の本文で落ちうる)。
- **C2(写し)**: 出来事の文が本文の中で見つかる ≥ 95 %・本文の token の decode が本文と一致 ≥ 38 / 40。
- **C3(同じ計器)**: olm7 の 1 行(F5a-2 think r0)を同じ部品で読み直し、保存の `traj32` と token ごとの cos の最小 ≥ 0.99。

## §3. 予想(凍結・`L3`・外れてよい)
- **Q1(apex を名指すと中点が上がる = moy-1 の O1O2 の形が写る)**: P5B × 壊れていない × `lat_sym` の行で、`lat` の後に `mid5` の群が上がる(後 > 前)≥ 60 %。
- **Q2(床を名指しても動かない = moy-1 の HeHi の形)**: P5 × 壊れていない × `fd_use` の行で、`fd` の後に `mid5` が上がる行が **≤ 55 %**。
- **Q3(記述・閾なし)**: 出来事 3 種 × 群 3 組 × model(全部 / Opus / Fable)。
- **Q4(記述の統制・閾なし)**: Q1・Q2 の行で、出来事の前後の「数式の文字(数字・²・·・× ・= ほか)の割合」の差。中点の群の上がりが本文の計算への移りの写しかを見る材料(olm59 §5-2 の宿題)。
- **Q5(時間)**: 統制 + 発火 + 読み ≤ 30 分。

## §4. 読み方・可読条件(R15)
- ADJUDICATION 10-27 を本札の凍結の文とする。Q1・Q2 は対象が **8 本未満なら「読まない」**(この文が凍結の文)。
- 「moy-1 の非対称(apex を名指すと中点が上がり、もう一方では動かない)が moy-5 でも見える」と書けるのは Q1・Q2 が両方 ✓ の時だけ。
- Q4 で数式の文字の割合が後で増える行が多ければ、Q1 の ✓ を「計算への移り」と分けて書けない(読みの限定として RESULT に書く)。

## §5. 主張しないこと
- **これは OLMo-3 32B base がその本文を読む時の活性で、Opus・Fable の中身ではない**。一つの model・一つの層・prf3 の 2 腕 × 2 model × 10 行。活性は相関。群の名は unembed の語からの名付け。prf3 の二次式は PROOF の一文が求めた物で、attractor(Descartes)の証拠にしない(prf3 §4-3)。

## §6. 費用(R14)
- 32B の読み込み 1〜2 分 + forward 40 行(問題文 + 本文 ≈ 1.5〜2 千 token)+ C1 の 20 行 + C3 の 1 行 ≈ 60 本 ≈ 10〜15 分。API なし(週枠を使わない)。
