# PREREG(札 `prf1`): moy-5 — ひらめき(③ cut)の後に、複数の関係を束ねて「P_y は放物線の上を動く」の証明を推論鎖として組み直すか(⑤)・Opus 5.5 / Fable 5.1・effort max・`claude -p`(MacBook)

- 発注(逐語): 先生 10-21「LLMで「ひらめき」が通じるのはmoy-1までで、moy-5では、複数の「ひらめき」を束ねて証明として推論鎖を再構成する必要がある、でいいでしょうか？」→(実行層: 前半は家の数と合わない・後半は未測定、⑤ を測る札を提案)→「5の札を作る。zebrasharkはローカルLLMが回っているので、ここで凍結・発火しましょう。APIではなく、サブエージェントで。」
- 実行 = MacBook(Claude Code 2.1.299・`claude -p`・購読の経路・API でない)/ 実行層 = Opus 5.5。書き始めの HEAD = `4cf201c3`(`R1`・fetch 済・origin と同じ)。
- **凍結の実体**: 本書と runner `ConstructGap/exp/prf1_moy5_proof_chain_claude_p_20261021.py` を一つの commit に。runner は凍結済みの module を import するだけで、どれも触らない:
  - `moy5t_claude_p_tool_and_data_20261015`(`e9de3824`・BASE = b5bp の Bbp・MODELS・DISALLOW)
  - `moy5t_rescore_streams_20261015`(`ded6ebfe`・stream の解析)
  - `moy5_relation_reader_v2_20261014` と `moy5_symbol_map_20261014`(`e07c3abd`)
  - `pm_cards_common_20261014`(`152f65dc`)・`essay_items_20261014`(`2189bc95`・essay4 の K の hint)
  - R0 の読み元の一覧は `summary_moy5_cut_all_cards_20261016.py`(`9ed4b886`・md5 `523c3d0c`)の `SOURCES` と一致することを import 時に assert する。
  - `guard_frozen()` は本書か runner が dirty なら走らない。読み取り器 v2 の較正と ⑤ の較正(29 項)が一つでも外れたら走らない。
- 背景: [SUMMARY 10-16](../2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md)(cut は答え全体に CUT の関係が一つでもあれば・cut は理由の欄にあり答えの欄は floor のまま)・[RESULT E1](RESULT_opus55_deepresearch_cognitive_stages_of_conscious_access_20261021.md) / [RESULT E2](RESULT_opus55_deepresearch_math_discovery_incubation_proof_cognition_20261021.md)(③ = 思考実験・⑤ = 検証 / 正当化の文脈)・neq5 の symptoma(Menaechmus の頂点の式)。
- 札: `L1` = 実出力 / `L3` = 読み。

## §0. 問い
moy-5 で、ひらめき(③ = 比例中項や相似の格子 = 家の CUT)の後に、**別の族の関係と束ねて、放物線の定義の式(symptoma: 縦の線分² ∝ 横の線分)まで推論鎖を組み直すか**(⑤)。③ を渡した時(P5K)に ⑤ が立つかで、「束ねる」段を ③ から切り離して測る。

## §1. 腕(新しい生成は P5 と P5K・各 model n 10)
| 腕 | prompt | 足した物 | 何を測るか |
|---|---|---|---|
| **R0** | (生成しない) | — | 10-16 のまとめの SOURCES の全行(11 の glob)を ⑤ の述語で読み直す = 既存の行の基線 |
| **P5** | Bbp(md5 `be9c4007`)+ PROOF | PROOF = 下の一文 | ③ と ⑤ の両方 |
| **P5K** | Bbp + essay4 の K の hint(逐語)+ PROOF | 比例中項 `FPx^2 = FV·FPy` を渡す | ⑤ だけ(③ は渡してある) |

- PROOF(逐語): "Finally, in the reason field, also prove that, as P_x moves on h1, the point P_y moves on a parabola. Give the proof as a chain of relations among the given points, ending with an equation that every position of P_y satisfies."
  - 道(焦点・準線か、格子か)は名指さない。「放物線」の語は渡す(06-11 の裁定: F・V・準線が座標から読めるので、放物線の認識は given)。
- prompt の md5: P5 = `31387680…`・P5K = `db866363…`(self-test の出力)。
- 経路 = moy5c と同じ型: repo の外の空の folder ごとに `claude -p`、`--setting-sources local`、MCP なし、Bash を含む全部の道具を disallow(38 個)。凍結前の harness の確かめ(問いと無関係の一文)で init の `tools` = `[]`・`mcp_servers` = `[]`。
- model = `claude-opus-5-5` / `claude-fable-5-1`・`--effort max`・timeout 2700 s・workers 4。

## §2. 数え方(機械の述語・runner の `score5`・`L1`)
- 読む文 = 答え全体(`parse_conj`・10-16 のまとめと同じ)。答えの欄だけの版も記す(`*_ans`)。
- 線分の類 = 読み取り器 v2 の凍結の六つの位置で計算: **縦の類** = HPy に比例(HPy・DK・VPx)/ **横の類** = VH に比例 / **定数** = 長さが変わらない(FV・VD・FD …)/ その他 = 変わる。
- **cut3** = CUT か SIM-CUT が一つでもある(10-16 の `cut` と同じ)。
- **END** = CUT の関係で、縦の類の指数が ±2・横の類の指数がその逆符号の半分・残りは定数 = symptoma の形(`HP_y^2 = 4·FV·VH`・`VP_x^2 = FV·VH`・`DK^2 = 4·VD·VH` …)。
- **LATX** = CUT か SIM-CUT で END でない関係(焦点の比例中項・相似・`KP_y·FV = FP_x²` …)。
- **CHAIN(主)** = END と LATX が同じ答えにある = 二つの族を束ね、放物線の定義の式で終わる。
- **FD** = 焦点・準線の等式: FPy と、六つの位置で KPy と同じ長さの線分(KPy・EJ)の EQUAL の関係、または言葉の「P_y is equidistant from F and e」型(正規表現 3 本)。
- **PARA** = 「parabola」の語。**floor** = 凍結の不変量 |EJ| = |KP_y|(答えの欄)。
- 道の分類(一つの行に一つ): CHAIN / END-only / LAT-only / none。FD は別の列(重なりを許す)。
- ⑤ の較正(29 項・合成の文・全部通過が発火の条件): END 5 正 4 負・LATX 3 正 2 負・CHAIN 2 正 3 負・FD 5 正 3 負・PARA 1 正 1 負。

## §3. 予想(実行層・発火の前に書く・`R3` = 小 n の比べは margin で)
- **P1(③ は届く)**: P5 で cut3 は Opus ≥ 7 / 10・Fable ≥ 4 / 10(moy5c の Bbp だけ・max は Opus 10・Fable 6。PROOF が道を焦点・準線へ寄せる分を引いた)。
- **P2(⑤ は ③ より少ない)**: P5 で CHAIN < cut3(両 model)。
- **P3(③ を渡すと ⑤ が増える)**: P5K の CHAIN ≥ P5 の CHAIN + 3(両 model)。
- **P4(焦点・準線の道)**: P5 で FD ≥ 3 / 10(少なくとも一つの model)。
- **P5(既存の行)**: R0 の各セル(card × arm × model × md5)で END ≤ cut3 / 3。ただし K 系の腕(比例中項を渡した腕)は除く。
- 当たり外れは数で書く。外れても述語は動かさない(`R4`)。

## §4. 統制と止まる条件
- **計器の陽性統制(gate)**: P5K の LATX ≥ 8 / 10(各 model)= 渡した関係を読み取り器が読む。下回れば、その model の P5K の CHAIN は読まない(書き方か読み取りの不調)。
- R0 は計器の側の基線(既存の行の CHAIN・FD の数)で、P5 の比べの相手ではない(prompt が違う)。
- 止まる条件: guard の不通過・CLI の失敗の連続(同じ err が 3 本)・tool の呼び出しが 1 本でも出た(記して止める)。

## §5. 限界
- n 10・一題(moy-5)・一つの PROOF の文面・effort max だけ。CHAIN は「二つの族が同じ答えにある」で、導出の向き(LATX から END を導いたか)は見ない。END だけ書いて LATX を後から添えた答えも CHAIN になる。
- 10-15 の moy5c と一対一に比べない(Claude Code の版が違う・prompt に PROOF がある)。
- FD の言葉の正規表現は較正した型だけを拾う。言い換えの FD は落ちうる(漏れの方向 = FD を少なく数える)。
- 答えの欄 / 理由の欄の分け方は凍結の parser(`parse_json_field`)に依る。

## §6. 手順
1. `--self-test`(凍結前・済: ⑤ の較正 29 / 29・読み取り器 v2 の較正の失敗 0・R0 の glob 11 本が全部ある・CLI の確かめ)。
2. 本書と runner を一つの commit に(凍結)→ push。
3. `--r0`(読むだけ)→ `--fire`(既定の units = opus:P5:10・opus:P5K:10・fable:P5:10・fable:P5K:10)→ `--read`。
4. RESULT = `conversations/2026-10-21/RESULT_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md`(`R1`: pull を先に・HEAD hash を記す)。
