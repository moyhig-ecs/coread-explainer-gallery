HEAD(R1) = a7dddb74(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm61`・凍結 2026-10-28 午後): moy-5 — Opus 5.5 / Fable 5.1 の本文を「要の一文」まで前置きにして OLMo-3 32B base に続きを書かせ、OLMo 自身の続きの層 32 の SAE の推移と、続きが辿る道を、apex(頂点の比例中項)の前置き / 床(焦点・準線)の前置きで比べる

- 発注(逐語): 先生 10-28「1で進みます」(olm60 の停止の後に主 session が挙げた候補 1「要の一文までを前置きにして、OLMo に続きを書かせる」)。前段 =「Opus・Fable で辿った道が、OLMoでどう活性化するか読んでいきましょう。」
- 親: [olm60 停止](RESULT_olm60_moy5_frontier_routes_read_by_olmo_sae_STOPPED_at_C1_20261028.md)(frontier の本文では FVE 0.343)・[olm59](RESULT_olm59_moy1_sae_trajectory_by_construction_mentions_20261028.md)(moy-1: O1O2 を名指した後に「考えの中点」が上がる 48 / 59)・[prf3](../2026-10-21/RESULT_prf3_moy5_confirm_lattice_bundle_claude_p_20261021.md)。読み方 = [ADJUDICATION 10-27](../2026-10-27/ADJUDICATION_reading_rule_frozen_text_literal_20261027.md)。
- runner = [olm61_…py](../../ConstructGap/exp/olm61_moy5_olmo_continues_frontier_route_sae_20261028.py)(olm60 の runner の rows / 文の位置 / 群を import)。

## §0. 凍結の前に見た物(開示)
- model なしで: 前置きの本数(apex 13 = Opus 9・Fable 4 / 床 15 = Opus 10・Fable 5)・前置きの末尾の文字(apex は「VP_x² = VD·VH = FV·VH」の文・床は「P_yF = P_yK」の文で終わる)・道の判定を作った文 2 つに当てた結果(lat True・fd True)。OLMo の生成も活性も見ていない。

## §1. 宇宙(`L1`)
- 前置き = prf3 の問題文 `PROMPT[arm]` + "\n\n" + frontier の本文 raw の**要の一文の終わりまで**。apex = P5B × 壊れていない × `lat_sym` の行・最初の `lat` の文まで / 床 = P5 × 壊れていない × `fd_use` の行・最初の `fd` の文まで(文の位置は olm60 の `sentence_spans` = prf3 の読み取り器と同じ切り方)。
- 続き = OLMo-3-1125-32B base(MLX bf16)・`mlx_lm` の `batch_generate`・温度 0.7・最大 256 token・前置きごとに 2 本(seed 6100 + 束の番号)。
- SAE = 公開 SAE 層 32・threshold で、**OLMo が書いた続きの token だけ**を読む(前置きの frontier の本文は読まない = olm60 の停止の理由)。群 = olm4 の moy-5 の 3 組(`close5` / `mid5` / `dir5`・各 20)。量 = 続きの最初の 64 token の群の平均(32 token 未満の続きは除く)。
- 続きの道 = 続きの文(prf2 の `_SPLIT`)に prf3 の読み取り器の判定をそのまま当てる: `lat`(頂点の比例中項・格子)/ `sym`(二次式)/ `fd`(焦点・準線)。

## §2. 統制(R6)
- **C1(計器)**: 続きの token(1 本あたり 16 本まで・seed 6161)で FVE ≥ 0.40・L0 100〜280。落ちたら読み出しをしない。
- **C2(写し)**: 続きの token の decode が続きの本文と一致 ≥ 90 %・空でない続き ≥ 90 %。
- **C3(同じ計器)**: olm7 の 1 行の読み直しで cos 最小 ≥ 0.99。

## §3. 予想(凍結・`L3`・外れてよい)
- **Q1(apex の前置きの後は「中点」が高い = olm59 の O1O2 の形)**: apex の続きのうち、`mid5` の最初の 64 token の平均が床の続きの中央値より大きい物が ≥ 60 %。
- **Q2(道に乗り続ける)**: (a) apex の続きのうち `lat` の文を持つ物 ≥ 50 % / (b) 床の続きのうち `fd` の文を持つ物 ≥ 50 %。
- **Q3(記述・閾なし)**: `close5`・`dir5` の同じ比べ・model 別(Opus / Fable の前置き)・道の乗り換え(apex の続きの `fd`・床の続きの `lat`・両方の `sym`)の本数。
- **Q4(記述の統制)**: 続きの最初の 64 token の数式の文字の割合の中央値を apex / 床で並べる。
- **Q5(時間)**: 生成 + 統制 + 読み出し + 読み ≤ 45 分。

## §4. 読み方・可読条件(R15)
- ADJUDICATION 10-27 を本札の凍結の文とする。前置きの行が条件ごとに **8 本未満なら「読まない」**(apex 13・床 15 の予定)。
- Q4 で apex の続きの数式の文字の割合が床より高ければ、Q1 の ✓ を「本文の中身(計算)の違い」と分けて書けない(読みの限定として RESULT に書く)。
- 「apex の道に置かれた OLMo は、床の道に置かれた時より『中点』の側に居る」と書けるのは Q1 ✓ の時だけ。

## §5. 主張しないこと
- **OLMo が frontier の前置きの後に書いた続きの活性**で、Opus・Fable の中身ではない。前置きの frontier の本文の活性は読まない。一つの model・一つの層・温度 0.7・256 token・前置き 28 行 × 2 本。活性は相関。群の名は unembed の語からの名付け。prf3 の二次式は PROOF の一文が求めた物(attractor の証拠にしない)。

## §6. 費用(R14)
- 32B の読み込み + 生成 56 本 × 256 token(8 本ずつの束)+ 読み出しの forward 56 本 + C1 の forward 56 本 ≈ 30〜40 分。API なし。
