
> **訂正(10-28・olm59 の凍結の前に実行層が cmt5 の json で数えた)**: 題と §3 の「考えの道 bind 40 / 40・答えの道 bind 8 / 40」は**全文の label**(`label`)の数。**答えの欄の label**(`label_json_fields`)では 考えの道 = bind **36 / 40**(attractor 4)・答えの道 = bind **4 / 40**(stuck-L1 3・attractor 1)・natural = 全文 bind 25 のうち答えの欄 bind 18(attractor 6・flail 1)。全文の label は、本文の「the line through the centers O1O2」のような語や、`\bHe\b` に当たらない綴り `HeHi` で bind に倒れる行がある(例: F5a-2 think r0 の答えの欄は「concyclic with HeHi as the diameter」)。向き(考えの道 > 答えの道)は変わらない。本文は書き換えない。出所: [PREREG olm59](../2026-10-28/PREREG_olm59_moy1_sae_trajectory_by_construction_mentions_20261028.md) §0・[RESULT olm59](../2026-10-28/RESULT_olm59_moy1_sae_trajectory_by_construction_mentions_20261028.md) §3。伝播(R9): この二つの数を引く file は 54(一覧 = [RECORD 10-28](../2026-10-28/RECORD_cmt5_label_full_vs_answer_field_propagation_20261028.md))。

> **訂正(10-26・可視化の二口の Opus medium が指摘・実行層が cmt5 の json で確認)**: §2 の「結論の前の長さ(token の中央値): 考えの道 = F5a-2 2,230・F5b-1 2,264 / 答えの道 = 136・136.5」は **T_tokens(生成した全長)の中央値**で、§5 の定義(結論の `{` の前の token 数 = τ × T)で数えると 考えの道 2,141 / 2,187・**答えの道 0 / 0**(答えから始めた行は `{` が位置 0)。数そのものは正しく、ラベルが「全長」であるべき所を「結論の前の長さ」と書いていた。本文は書き換えない。

# RESULT(札 cmt5): 考えの道は bind 40 / 40、答えの道は bind 8 / 40(誤り 32・統制 C1 が落ちて保留)— 統制 C1(sampler の較正)が F5b-1 で落ちて、読みは保留(2026-10-20・実行層)

- 札 = [PREREG](PREREG_cmt5_first_token_fixed_sampling_two_stages_20261020.md)(凍結 `65ce8c34`)。書いた時の HEAD = `65ce8c34`(`R1`)。
- 走行 = zebrashark・py314・MLX `batch_generate`(20 本ずつ)・温度 0.7。09:49:39 → 11:47:24(約 2 時間・考えの cell が各 45 分)。120 本・label の無い行 0・上限に当たった行 0。
- 出力 = `probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt5_first_token_fixed_sampling.json`(md5 `c5d64f9f`・本文の全文を含む)。provenance = commit `65ce8c34`・dirty False。
- **身分**: §1〜§2 = `L1`。§3 = 判定(凍結の規則)。§4 = 予想。§5 = 事後の数え(`L2`・PREREG に無い)。§6 = 読み(`L3`・採否は先生)。

## §1. 統制
- **C1(sampler の較正)= 落ち**。抽選のままの cell で答えから始めた本数を、cmt4 A31 の p_brace(温度 0.7)の二項 95% 区間と比べた。
  - F5a-2 = 1 / 20(区間 0〜6)→ 通過。
  - F5b-1 = **12 / 20**(区間 2〜10)→ 外れ。
  - 考えられる理由(どれかは分けられない): MLX と torch の logit の違い(cmt4 で最初の位置の同点の崩れ方が違った)/ batch 生成の数値。
- **C2(label の無い行 ≤ 2)= 0 → 通過**。

## §2. cell ごとの label(n 20 ずつ)
| prompt | 抽選のまま(natural) | ` Okay` を固定(考えの道) | `{"` を固定(答えの道) |
|---|---|---|---|
| F5a-2 | bind 15・attractor 5(答えから始めたのは 1 本 = attractor) | **bind 20** | attractor 7・B-stuck-L1 7・**bind 5**・flail 1 |
| F5b-1 | bind 10・attractor 7・stuck-L1 3(答えから 12 本 = attractor 7・stuck-L1 3・bind 2 / 考えから 8 本 = bind 8) | **bind 20** | attractor 12・stuck-L1 5・**bind 3** |

- 結論の前の長さ(token の中央値): 考えの道 = F5a-2 2,230・F5b-1 2,264 / 答えの道 = 136・136.5。
- F5a-2 の抽選のままで「考えから」始めた 19 本のうち 4 本は attractor。4 本とも短い前置き(91〜339 token)の後に結論を書いた。
  - 前置きの例: 「Do not revise. Do not correct. …」・「Here is my reasoning: …」・「Key insight: …」・「The four intersection points X1, X2, X3, X4 are concyclic. The center of this circle is the midpoint of the segment connecting He and Hi …」。

## §3. 判定(凍結の規則・**C1 が落ちたので保留**)
計算上の読み(保留つき):
1. **一段目**: attractor(答え)− attractor(考え)= F5a-2 7 − 0 = 7・F5b-1 12 − 0 = 12 → 両方 **YES**(≥ 6)。
2. **二段目**: 答えの cell の attractor = F5a-2 7・F5b-1 12 → 両方「答えの道の上でも、結論の入口でまだ分かれる」(3〜17)。
3. **prompt が二段目を形作るか**: |7 − 12| = 5 → **NO**(< 6)。

- 保留の範囲: C1 は「抽選のまま」の cell の最初の一語の分布の較正。固定した二つの cell(考え・答え)は最初の一語を抽選していないが、凍結の規則は札全体の読みを保留とする。

## §4. 予想(PREREG §4)の当たり外れ
- P1(考えの道の bind は両方 ≥ 17)= **当たり**(20 / 20・20 / 20)。
- P2(F5a-2 の答えの道の attractor ≥ 12)= **外れ**(7。stuck-L1 が 7)。
- P3(F5b-1 の答えの道の attractor 6〜14)= **当たり**(12)。
- 「prompt が二段目を形作る = YES」= **外れ**(差 5)。

## §5. 事後の数え(`L2`・PREREG に無い・120 本)
結論の `{` の前の token 数(τ × T・括弧の無い行は T)で分けた:

| 結論の前の token | n | label |
|---|---|---|
| 0(答えから) | 53 | attractor 27・stuck-L1 15・**bind 10**・flail 1 |
| 1〜349 | 9 | **bind 5**・attractor 4 |
| 350〜999 | 6 | **bind 6** |
| 1,000 以上 | 52 | **bind 52** |

- **350 token 以上考えてから結論を書いた 58 本は、58 本すべて bind**。
- label ごとの中央値: bind 1,825 token・attractor 0・stuck-L1 0。

## §6. 読み(`L3`・採否は先生・**統制 C1 が落ちて保留**の量を読む = 以下の数は全部保留つき。この札を引く時は「(統制 C1 が落ちて保留)」を添える。札 10-22・監査 A3 の指摘)
1. **考えの道は 40 / 40 が bind、答えの道は 8 / 40(統制 C1 が落ちて保留)**。答えの道の 32 本の内訳 = attractor 19・stuck-L1 12・flail 1。最初の一語(考えるか答えるか)の差は、結論の正しさの差としてとても大きい。
2. **答えの道の上でも、結論の入口でまだ分かれる**(attractor・stuck-L1・bind)。cmt3 の「入口の分布は割れている」と同じ形。
3. **効いているのは最初の一語そのものより、結論の前にどれだけ考えたか**。
   - 抽選のままの「考えから」でも、短い前置きの後に結論を書いた行は attractor に着いた。
   - 事後の数えでは 350 token 以上で 58 / 58 が bind。
   - 最初の一語(` Okay`)は、長く考える道に入るかどうかの入口として効いている、と読む。
4. moy-5 の札 neq6(effort を上げると比例中項が答えに浮上)と同じ形: **commit の前の探りが短いと、目立つ attractor か別の誤りに止まる。長いと正しい対象に着く**。
5. C1 の外れ(F5b-1 の抽選のままで答えから 12 / 20・torch の確率から見込む 6 本前後より多い)は、生成の経路(MLX)では F5b-1 の最初の位置の答えの側が torch より重い可能性を示す。cmt4 の同点の崩れ方の違いと同じ向き。経路ごとの最初の位置の確率を MLX で直接取れば分けられる(新しい札)。

## §7. 主張しないこと
- 機構。
- 「考える長さが bind の原因」(§5 は事後の数えで、長さと label の並びを見ただけ・長く考える行が別の理由で bind になりやすい可能性を分けていない)。
- 最初の一語の固定は反実の操作。
- prompt 2 つ・n 20・一つの model。

## §8. 次(採否は先生)
- 札 B(励起の地図)の位置は、一段目 = **最初の位置**(長く考える道に入るか)に絞るのが最も効く(40 / 40 対 8 / 40 の分かれ目・統制 C1 が落ちて保留)。二段目(答えの道の結論の入口)は位置が行ごとに違うので後で。
- C1 の外れを分けるなら、MLX の logit で最初の位置の確率を直接取る(安い・数秒)。
