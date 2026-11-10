# PREREG(札 cmt13): block した moy-1 で bind する瞬間 — 考えの中で、円の直径 / 中心の指す先を O1…O2 と書く位置と、He…Hi と書く位置を、同じ計器で比べる

- 日付: 2026-10-21(水)未明・zebrashark・実行層(Opus 5.5)/ 書き始めの HEAD = `15b2b6df`
- 発注(逐語): 先生 10-21「もう一点。moy-1woblockしてcutする時に、どこが励起・活性化するか読み出せますか？」「moy-1をblockして」「cutはbindです」→(実行層: 案 = 札 cmt13)→「OLMoなのでblockしないとbindしない？ 凍結・発火」
- 親 = [RESULT cmt12](../2026-10-20/RESULT_cmt12_prose_vs_moy1_component_sites_20261020.md)(結論の欄の commit の位置 = 考えの中の語を写す head)・[RESULT cmt10](../2026-10-20/RESULT_cmt10_first_position_direct_logit_attribution_20261020.md)
- **凍結の実体**: 本書と script `probes/olmo3-f5-think-prefix/tsd_r5/replay_cmt13_blocked_bind_moment_in_thinking_20261021.py` を一つの commit に。dirty なら走らない。forward だけ(重みは触らない)。

## §0. 事前に知っていること(開示)
1. Olmo の moy-1 の行(F5a-2・F5b-1)の prompt には block の一文(「Note: merely stating that the four points are 'concyclic' … is INSUFFICIENT. Identify that circle UNIQUELY: which known point is its center, and which segment is its diameter (or radius)? …」)が入っている = blocked。B-bind は 12 行(F5a-2 6・F5b-1 6)。
2. 結論の欄で apex の語を書く位置(cmt12)では、層 43〜56 の head が考えの中で前に書いた同じ語を読んで apex の側へ押していた(写し)。He/Hi の側へは L50H23(prompt の He・Hi を読む)。
3. 考えの中で最初に出る diameter / midpoint は、12 行中 6 行が block の一文の言い直し(「which segment is the diameter」)・1 行が attractor の仮説・1 行が別の意味の midpoint。⇒ 瞬間は**述語**で決める(§1)。述語で数えると、cut の文は bind の 11 / 12 行に、attractor の文は bind の 5 / 12 行の考えの中にある(数えたのは本書の前・文の数だけ)。
4. 指す先の最初の token は、cut で ` O`(507)10 / 11・LaTeX の ` \(` の次の `O`(46)1 / 11、attractor で ` He`(1283)5 / 5(確かめた)。
5. どちらの文も「maybe / perhaps / Alternatively」の仮説として出ることが多い。比べは「O1O2 を初めて名指す瞬間」対「He・Hi を初めて名指す瞬間」。
6. self-test ⭕(部位 cut 11 / att 5・述語の陽性 / 陰性統制・要約の式)。

## §1. 部位と対
- 述語(凍結): 「diameter / midpoint (is / of) (the) (line) (segment) (joining / connecting / between) (the) (two) (centers)」の直後に、指す先 O1…O2(cut)または He…Hi(attractor)が来る、生成の本文の中の最初の所。
- **cut**: 各 bind 行の最初の cut の文(11 部位)。**att**: 各 bind 行の最初の attractor の文(5 部位: F5a-2 s1・s6・F5b-1 s2・s6・s8)。
- 決定の位置 P = 指す先の最初の文字の token の一つ手前(その位置の出力が指す先を決める)。
- 対(Δ = O の側 − He の側・正 = cut の側): ` O`(507)↔ ` He`(1283)/ LaTeX の形 `O`(46)↔ `H`(39)。

## §2. 計器(札 cmt12 と同じ)
- 大きさ(残差・attention の出力・MLP の出力の、同じ層の他の位置の中央値との比)・logit lens(Δ と全語彙の順位)・直接の logit 寄与(層ごとの attention / MLP・head ごと)・上位 10 head(と L50H23)の注意の先(prompt の区間 / 生成の本文・上位 5 token)。
- 要約: 寄与の重心の層・帯・後ろの MLP の逆向き・L50H23 と L49H20 の順位と寄与・上位 3 head の注意の prompt への割合。
- 群の比べ: 上位 10 head の Jaccard(cut・att・cmt12 の結論の bind・cmt12 の分かれ道)・重心(cut / att / cmt12 の結論の bind)。

## §3. 統制
- **C0**: 部位の数 = cut 11・att 5。**C1**: 寄与の和 = 出力の Δ(bf16 の目盛り 2 つ分)。**C2**: head の和 = 層の attention。**C3**: attention の行の和 1 ± 0.02。
- **C4(陽性統制)**: 札 cmt12 の commit の 2 部位(F5a-2 s5 apex・F5b-1 s9 hehi)を同じ関数で読み直し、部品ごとの寄与の差の最大 ≤ 0.02・上位 10 head が同じ。
- 落ちた統制があれば、その量は読まない(C4 が落ちたら全部を読まない)。

## §4. 予想(発火の前に書く・`L3` の見込み)
- **P1**(cut は prompt を読む): cut の部位で、上位 3 head の注意の prompt の区間への割合の平均が 0.5 以上の部位が 11 のうち 6 以上(まだ考えの中に写す語が無いので、O1・O2 が定義された prompt を読む)。
- **P2**(attractor は L50H23): att の部位の 5 のうち 3 以上で、L50H23 が上位 10 に入り、He の側へ押す(寄与 < 0)。
- **P3**(違う部品): 上位 10 head の Jaccard の平均は、cut ~ att のほうが cut ~ cut より小さい。
- **P4**(大きさ): 16 部位すべてで、層 1 から後の残差の比の最大 ≤ 2.0(大きさの突出は無い)。
- **P5**(どこで): cut の部位の attention の重心の層の平均は、cmt12 の結論の bind の部位(10)の平均より早い。
- **P6**(綱引き): 後ろの MLP(59–63)が attention の和と逆向きなのは、16 部位のうち 8 以上。

## §5. 主張しないこと
- 機構・因果(寄与は一次の分解・重みは触らない)。「励起・活性化」とは書かない(大きさと寄与を分ける)。
- 述語は文の形で瞬間を決める(意味の同定ではない)。仮説として名指す瞬間を含む。
- 一つの model・blocked の F5 の 2 変種・bind の 12 行のうち述語が当たった行。

## §6. 手順
`--self-test` ⭕ → 凍結 → `--fire`(model の読み込み + forward 18 回・数分)→ RESULT。
