HEAD(R1) = cea6cefa(この file を入れた commit の親・実行層が commit 時に記入)

> **訂正(全体の監査 10-27・Opus 5.5 xhigh・[AUDIT_RESULT A1](../2026-10-27/AUDIT_RESULT_olm_full_A1_olm1_8_opus55_xhigh_20261027.md)・裁定 [ADJUDICATION 10-27](../2026-10-27/ADJUDICATION_reading_rule_frozen_text_literal_20261027.md))**:
> - A1-olm1-01: 「答えの JSON にその形を書いた本は 0」(:32)→ think K r3 の答えの JSON は `{"conjecture": "FP_x^2 = FV \\cdot FP_y", …}` で、hint の切断の形を書いている。読み取り器は `\cdot` の不正な escape で conjecture を空にした(`cut_in_conjecture` False・`bind` True)。規則の数は 0 / 10、読みの数は 1 / 10(出所: `ConstructGap/exp/results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` の think・K・rep 3 の `raw` と `conjecture`・[data](../2026-10-27/data_banners_olm_full/A1/a1_banner_recount.out) (d))。同じ数は :16(表の cut(答え) 0)・:43「答えに書いた本は 0」・:51「/ 0 / 10」に在る。
> - 判定の計: 変わらない(関門は床 2 / 20 で FAIL のまま・P3・P4 は判定なしのまま)。
> - 本文は書き換えない。

# RESULT(札 `olm1`): moy-5 × mnw1 の腕 × OLMo-3-1125-32B(base・MLX bf16)— Stage 0(screen)で両変種とも関門に落ち、札は screen の記録として止める(2026-10-22 夕・実行層)

- PREREG: `PREREG_olm1_moy5_olmo3_32b_mnw1_arms_20261022.md`(凍結 `02e8f460` → 凍結し直し #1 `a3eee055`・開示済)。runner = `ConstructGap/exp/olm1_moy5_olmo3_32b_mlx_mnw1_arms_20261022.py`。
- 実出力 = `ConstructGap/exp/results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl`(60 行・raw を全部保持)。log = `ConstructGap/exp/logs/olm1_20261022_stage0.out`。
- 走行: 2026-10-22 13:39:42 〜 18:28:50 JST(4 時間 49 分・zebrashark・batch 5・温度 0.7・max_new 6144・seed は §1 の式)。費用ゼロ。
- 計器 = mnw1 の読み取り器(v2・CAL 72/72)をそのまま import。**欄の意味**: `bind` = 本文に平均比例(切断)の形が在る / `cut_in_conjecture` = JSON の答えにその形が在る / `closure` = 床(|EJ| = |KP_y| を答えに書く)/ `truncated` = 6144 に当たった / 0 token の行 = model が最初の一語で EOS を出した(`ok=False`・`route=MLX`)。

## §1. Stage 0 の数(変種 × 腕・分母は引いた本数・空の行も打ち切りも分母に残す = PREREG §1-4)

| 変種 | 腕 | n | cut(本文) | cut(答え) | 床 | 打ち切り 6144 | 0 token | JSON なし | token 中央値 |
|---|---|---|---|---|---|---|---|---|---|
| natural | K | 10 | **2** | 1 | 0 | 1 | **5** | 8 | 2.5(空を含む)|
| natural | none/Q1 | 20 | 0 | 0 | **0** | 8 | 0 | 9 | 224 |
| think(`Okay` 固定) | K | 10 | **10** | **0** | 2 | 7 | 0 | 7 | 6144 |
| think | none/Q1 | 20 | 0 | 0 | **2** | 14 | 0 | 14 | 6144 |

- runner の `--read` は natural K を n = 5 と表示する(0 token の行を raw なしとして落とす)。本書は PREREG どおり分母 10 で書く(関門の結論は変わらない)。

## §2. 関門(`R6`・変種ごと・K の cut ≥ 8 / 10 かつ none/Q1 の床 ≥ 16 / 20)
- **natural: FAIL**(K 2 / 10・床 0 / 20)。
- **think: FAIL**(K 10 / 10 は通るが、床 2 / 20)。
- → PREREG §2 の最後の規則どおり **Stage 1(五腕 × 100 本)は引かない**。比較表の OLMo の列は「部品に届かない」。

## §3. 実出力が示す中身(`L1`・jsonl の行から)
**natural**
- K: 10 本のうち 5 本は 0 token(prompt の直後に EOS)、2 本は 5 token。残り 3 本 = r2(78 token)は hint の「FPx^2 = FV·FPy, for every P_x」を JSON に写しただけ(bind True・床 False)、r8(1,115 token)は「E, J, K, P_y are concyclic」、r1 は 6144 まで JSON なし。
- none/Q1: 床 0 / 20。短い JSON(12〜861 token)の答えは **共線**(「P_y, K, J are collinear」の変種 4・「E, J, K, P_y are collinear」1)と **円周上**(「P_y lies on the circle c」3)に集まる。8 本は 6144 まで JSON を出さない(指示文の反復 = 疎通 §0 と同じ loop)。

**think(最初の一語 `Okay`)**
- K: 本文は 10 / 10 で hint の平均比例を復唱する(「The hint mentions that the relation is a mean proportional: FP_x² = FV·FP_y」の形)が、**答えの JSON にその形を書いた本は 0**。JSON まで到達した 3 本の答え = 「EJ = KP_y」(r1・5,905 token)・「EJ = KPy」(r5・5,871 token)・「FP_x^2 = FV·FP_y」(r3・hint の写し)。7 本は 6144 で切れて JSON なし。
- none/Q1: 床 2 / 20(r10「EJ = KP_y」1,003 token・r15「EJ = KPy」6,055 token)。他の JSON = 「EJ is perpendicular to GE」「KJ ⟂ GE」「E, J, K, P_y are collinear」「K, P_y, J are collinear」。14 本は 6144 で切れて JSON なし(座標計算を延々と続ける)。
- = `Okay` の一語は moy-1(cmt5: bind 8 / 40 → 40 / 40)と違い、moy-5 では**床に届く本を 0 → 2 にするだけ**で、代わりに打ち切りを 8 → 14 に増やす。

## §4. 予想(PREREG §4)との照合
| 予想 | 実 | 当否 |
|---|---|---|
| P1 natural: 床 ≤ 4 / 20・K の cut ≤ 3 / 10 → FAIL | 床 0・K 2 → FAIL | 当たり |
| P2 think: 床 4〜12 / 20・K 3〜8 / 10・打ち切り ≥ 1 割 | 床 **2**(下に外れ)・K **10**(上に外れ)・打ち切り 21 / 30 | 床と K は外れ・打ち切りは当たり(予想より桁が大きい)|
| P3・P4(think が通った場合の Stage 1) | 引いていない | 判定なし |

- K の 10 / 10 の読み(`L3`): K は hint に形を書いた腕(陽性統制)なので、「本文で復唱する」だけで bind が立つ。**復唱と commit は別**で、答えに書いた本は 0。関門の K の条件は「読み取り器がこの model の文でも形を拾える」ことの確認としては成り立ち、「model が切断を自分で作れる」ことの証拠にはならない。

## §5. 比較表の OLMo の列(mnw1 / mnw1b の表に足す行)
| model | none/Q1 床 | K cut(本文 / 答え) | 打ち切り | 備考 |
|---|---|---|---|---|
| Opus 5.5(xhigh・API) | 20 / 20 | — | 0 | mnw1 RESULT §1 |
| Fable 5.1(xhigh・API) | 20 / 20 | — | 0 | 同 |
| OLMo-3 32B base・natural | **0 / 20** | 2 / 10(5 本は空) | 8 / 20 | 本書 |
| OLMo-3 32B base・think | **2 / 20** | 10 / 10 **/ 0 / 10** | 14 / 20 | 本書 |

## §6. 朝の MEMO §4 の門(「moy-5 で励起・活性化は分析の範囲内か」)への答え(`L3`・札の規則どおり)
- moy-1 では cmt5 の一語(`Okay`)で「考えの道」に入り bind 40 / 40 になったので、lens で内側を読む入口があった。
- moy-5 では同じ一語で床が 2 / 20。**読む対象の「床に届いた行」がほぼ無い**ので、P-compose(床の後の切断の合成)の読みは Olmo-3 32B base では**立てられない**。活性化の分析は、この model・この大きさ・事後学習なしでは「入口が無い」が答え。
- 入口を作る候補(札にしていない・先生の裁定): (a) 床を prompt で与えて(K の形)切断の有無だけを読む = conf/Q1f の形(Claude では cut 13〜19 / 20)、(b) 事後学習済みの Olmo-3 Think(07-28 の screen は moy-1 で open stuck 9 / 9)で床を測る、(c) max_new を上げて loop を切り分ける(14 / 20 の打ち切りが座標計算の途中なのか反復なのかを分ける)。

## §7. 主張しないこと(PREREG §6 のまま)
- base model と API の adaptive thinking は同じ系ではない。温度 0.7 の抽選と API の抽選は同じ目盛りではない。一つの作図・一つの配置・一つの open-weight model。MLX の batch 生成の数値。
