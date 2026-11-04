HEAD(R1) = 2c8d7e21(凍結時の HEAD・origin の 1 commit を merge 済み・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm116`・凍結 2026-11-03): frontier(Opus 5.5 / Fable 5.1・prf5)の **moy-2** の証明の欄を OLMo-3 32B base に順次喰わせる — 半径 ⊥ 接線の設定(k = 1)/ O3 の足 = TcTh の中点の段(k = 2)まで与えると残りの道(射影 → 垂直二等分線 → 等距離)を続けるか(A・生成)・段の語の先読みと commit 方向の係数(B・forward・記述)= olm114 の moy-2 版

- 発注(逐語・先生 11-03): 「**直交を使ったかの述語v2、moy-2へ適用、半径の等しい対照へ順次進みます。**」の二枚目。
- G10 の欄: 比べる物 = 「k = 1(半径 ⊥ 接線と、接点が足か平行であることまで与えた)の行で、OLMo の続きが MID2 ∧ (PB2 ∨ EQD)(O3 の足が TcTh の中点 → 垂直二等分線か等距離)を満たす割合」/「k = 2(O3 の足 = TcTh の中点の段まで与えた)の行で、続きが PB2 ∨ CONG2(垂直二等分線か合同 / Pythagoras)を満たす割合」/「k = 1 の続きで USE_PROJ(射影の事実 → 結論の順)を満たす数(記述)」 / 計器 = hq 共通の部品の凍結の述語 score_m2(PROJ・PERPT・TRAP・PB・MIDTT・COORD・ALG・CONG・route・較正 61 / 61)を**続きの文だけ**に当てる + この札の v2 の述語 MID2・PROJAFF・PB2・EQD・CONG2・USE_PROJ と段の切り方・続きの取り出し(較正 29 例)・(B)は olm67 / olm114 の計器(層 48 の J-lens / logit lens の語の集合の対数質量の百分位 u・層 32 の commit 方向 d̂ = olm64 directions) / 雛形 = いいえ
- runner = [olm116_…py](../../ConstructGap/exp/olm116_moy2_frontier_proof_prefix_ladder_20261103.py)・共通の部品 = [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(凍結 cb12da8d・触らない・md5 `426e2089…` を guard)・問いの文 = [prf5 runner](../../ConstructGap/exp/prf5_moy12_proof_field_jsononly_claude_p_20261102.py) の M2B(凍結 5f519216)・frontier の出力 = `ConstructGap/exp/results_prf5_20261102.jsonl`(md5 `995650e5…` を guard)。走らせる所 = zebrashark(32B は一つずつ)。`--gen`(A)→ `--fire`(B)→ `--read`。API なし。

## §0. 起案の前に見た物(開示)

- 主 session は prf5 の moy-2 の証明 20 本を全文読んだ(段の切り方の設計のため)。olm113 の apex 16 本の証明の欄(「対称性」8 / 12)と olm114 / olm115 の結果(moy-1 で、段を与えると直角と Thales は 26 / 40・直交の事実を使ったのは 13 / 40)も読んだ。**予想はこれらを見た上で付けた**。
- 段の切り方(k1 = 両方の半径 ⊥ 接線が揃った後で足 / 射影 / 平行を言った段・k2 = MID2 が初めて真になる段)と除外の規則は 20 本を見た後に書いたが、機械の判別条件(R5)で、`--selftest` の結果 **20 / 20 が k = 1 と k = 2 の両方に入った(除外 0)**。切れ目の位置は 20 本とも主 session が目で確かめた(k1 の末尾 = 足 / 射影 / 平行の文・k2 の末尾 = 「M は TcTh の中点」の文で、垂直二等分線と等距離はその後)。
- frontier の `reason` の欄は渡さない(olm114 と同じ・鎖を含む)。書き出しは `conjecture` と `proof` の二欄だけ。
- **k = 0 の腕は置かない**: olm114 で、JSON だけを求める文(M1B)を base model に当てると 21 / 40 が考えを書き続けて上限で切れ apex 5 / 40 だった。M2B も同じ形なので、OLMo 側の比べる元は olm113 の M2A(apex 16 / 60・射影 0 / 16)のままとする。
- smoke(凍結の前・2 行・読まない): 数は §6。

## §1. 計器(R5)

- **問いの文**(両腕共通)= prf5 の M2B(JSON だけ・証明と status を欄で求める・`First write your reasoning` の一行なし)+ cue。OLMo に渡す文の md5 `9960091f…`(cc 形 `33dcb6d1…` = prf5 の moy-2 の行の prompt_md5)。
- **書き出し(k = 1・2)** = `{"conjecture": <frontier の conjecture 逐語>, "proof": "<P_k 逐語>`(json.dumps で再直列化・証明の文字列の閉じの `"` を付けない)。P_k = frontier の証明の先頭から k の段の終わりまで(rstrip)。
  - **段** = frontier 自身の番号 `Step n` / `(n)` / `n)` / `n. ` を n = 1, 2, … の順に取る(参照「Steps 1–2」「by (1)」は飛ばす・小数「14.762」は `n. ` の形でない)。
  - **k1** = 累積の prefix に O1Th ⊥ と O2Tc ⊥ の両方(norm2 = ⟂ → ⊥)が揃った段以降で、最初に足 / 射影 / 平行(`project|foot|feet|∥|parallel`)の語を含む段(無ければ揃った段)。**k2** = 累積の prefix で MID2(O3 の足 / 射影 / M が TcTh の中点)が最初に真になる段。
  - **除外(機械)**: ok1 = P_k1 に MID2・PROJAFF(affine・preserves midpoints・intercept theorem・midline…)・PB2・EQD が無い。ok2 = k2 > k1 かつ k2 の段に PB2・EQD が無い。どちらも 20 / 20 で通った(§0)。
- **続きの取り出し** = olm114 と同じ(書き出し + 生成を JSON として decode・閉じていれば `proof` の欄から書き出しの分を除いた残り・閉じていなければ最初のエスケープされていない `"` まで)。
- **続きの述語**(続きだけ・与えた段の語は数えない):
  - 凍結の `score_m2`: PROJ・PERPT・TRAP・PB・MIDTT・COORD・ALG・CONG・route。
  - v2(この札): **MID2** = O3 の足 / 射影 / M が TcTh の中点(`foot|projection|image|π(O3)|M … is/= midpoint of TcTh`・`midpoint M of TcTh`・`midpoint(Tc,Th)`・`TcM = MTh`・`ThM : MTc = 1 : 1` など)/ **PROJAFF** = 射影は affine・中点を保つ・intercept theorem・midline・three parallel lines・`M − O3 =` / **PB2** = TcTh の垂直二等分線(O1O2 の垂直二等分線は除く)/ **EQD** = O3Tc = O3Th・equidistant from Tc / Th・O3Tc² = … = O3Th² / **CONG2** = congruent・SAS・RHS・HL・Pythagoras・O3Tc² = O3M² + … / **USE_PROJ** = MID2 か PROJAFF の事実があり、**その位置より後**に PB2 か EQD(事実 → 結論の順)。
  - 偽の前提などの印(記述)= SYMM(symmetr・reflect)・PAR(TcTh ∥ O1O2・tangent parallel to O1O2)・HOMO・POWER・COLL。
  - k = 1 の主 = **MID2 ∧ (PB2 ∨ EQD)**(設定は与えた・残り = 足が中点 → 垂直二等分線 / 等距離)。k = 2 の主 = **PB2 ∨ CONG2**(残り = 垂直二等分線か合同 / Pythagoras で閉じる)。
- **生成** = MLX batch_generate・温度 0.7・`allenai/Olmo-3-1125-32B` base。k = 1: 20 本 × 2 rep(seed 20261150・51・max_new 1536)/ k = 2: 20 本 × 2 rep(seed 20261152・53)。= 80 行。seed は olm87 / 90 / 112 / 113 / 114 と重ねない。
- **(B) forward**(記述)= olm114 と同じ型。語の集合(token id・先頭の sub-token)= PROJ {` project`, ` projection`, ` foot`} / PERPT {` perpendicular`} / MID {` midpoint`} / PB {` bis`} / ATTR {` coll`, ` symmetric`, ` symmetry`}。切れ目 = k1・k2・証明の終わり。統制 = C1・C3・round_trip(通らなければ (B) は RESULT に載せない)。
- **較正(R6)** = hq の 61 / 61 + この札の 29 例(段の分け方 3・切る規則 5・続きの取り出し 3・書き出し 1・v2 の述語 16 = 正と負・「O3 = midpoint of TcTh」は MID2 でない・「perpendicular bisector of O1O2」は PB2 でない)。runner の guard で、通らなければ走らない。

## §2. 関門

- **G1**: k = 1 の行(生成が空でない)≥ 24 / k = 2 の行 ≥ 24。✗ → その Q を読まない。
- **(B)**: C1・C3・round_trip。✗ → (B) を載せない。
- 較正(hq 61 / 61・この札 29 / 29)= runner の guard。prf5 の jsonl と hq の部品の md5 = guard。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | k = 1 の行で、続きが MID2 ∧ (PB2 ∨ EQD) を満たす割合 | **続ける** ≥ 0.50・**続けない** ≤ 0.10・ほか = 間 | 続ける 0.20・続けない 0.35・間 0.45 |
| Q2 | k = 2 の行で、続きが PB2 ∨ CONG2 を満たす割合 | **続ける** ≥ 0.50・**続けない** ≤ 0.10・ほか = 間 | 続ける 0.55・続けない 0.15・間 0.30 |
| Q3 | 記述: k = 1 の USE_PROJ の数・続きの route(凍結)・偽の前提の印(SYMM・PAR・HOMO・POWER・COLL)・family 別・closed・status・T・(B) の先読みと窓 | — | — |

- 予想の根拠(開示): olm113 で OLMo の moy-2 の証明の欄は「対称性」が 8 / 12 で射影 0 / 16。olm114 / 115 で moy-1 は、段を与えると語は続く(26 / 40)が事実を使うのは 13 / 40。moy-2 の鍵の段(射影は中点を保つ)は moy-1 の鍵の段(二等分線の直交)より OLMo の本文に少なかった(olm113 の本文で PERPT ∧ (PROJ ∨ TRAP) ∧ MIDTT は 10 / 60)ので、Q1 は moy-1 より低い側に置く。

## §4. 読み方

- `--read` が `olm116/read.json` を書く(関門・Q1〜Q3・行ごとの印・(B))。判定は述語の値だけで付ける。
- RESULT では、k = 1 の続きのうち Q1 を満たした物を行の名の順に最大 10 本、満たさなかった物を行の名の順に 4 本おきで最大 10 本、逐語で引く。k = 2 も同じ型で各 5 本。主 session の読み(L3)は述語の値と並べ、違っても判定は変えない(違いは開示する)。(B) は表だけ。

## §5. 主張しないこと

- 書き出しは frontier の文。続きが道を完成しても「OLMo が導いた」ではなく「与えられた段の続きを書けた」まで。apex(conjecture)は与えている。
- MID2 ∧ (PB2 ∨ EQD) と USE_PROJ は語の順で、推論の正しさの検証ではない(偽の文を挟んでも真)。
- k の段の中身は frontier の文ごとに違う(段 5〜9・P_k1 204〜461 字・P_k2 463〜824 字)。family の差は文の型の差(Fable の `Step n (題):` / Opus の `n)`)と混ざる(olm114 / 115)。
- k = 0 の腕が無いので、「同じ文で OLMo だけ」の値はこの札に無い(olm113 の M2A が比べる元・文が違う)。
- (B) の先読みは語の集合ごとの陽性統制が無い → 記述。` perpendicular` は設定の段にも出る・` coll`・` symmetr` は問いの文にも出うる。
- base model・一つの温度・rep 2・frontier 20 本(射影 19 + 台形 1)。

## §6. 走らせ方と記録

- zebrashark: `python ConstructGap/exp/olm116_moy2_frontier_proof_prefix_ladder_20261103.py --selftest`(PASS・plan ok1 20 / 20・ok2 20 / 20)→ `--smoke`(凍結の前・2 行・読まない)→ 凍結 → `--gen`(約 15 分の見込み・olm114 の k の腕は 13 分)→ `--fire`(forward 20 本・数分)→ `--read`。
- smoke(凍結の前・seed 20261196〜97・k = 1 / k = 2 各 1 行・max_new 512・読まない・zebrashark 12:24 JST・壁時計 36 / 45 s・Traceback 0・`olm116/smoke.json`・`smoke_run.log`): k = 1(fable_r0・与えた段 325 字)= T 261・JSON 閉じた・続き 474 字・status hypothesis / k = 2(fable_r0・与えた段 538 字)= T 52・閉じた・続き 115 字・status hypothesis。本文は読んでいない。
  - 開示: smoke の log は続きの Q1 / Q2 の数も印字する作りで、主 session は k = 2 の行(Q1 0・Q2 1)を目にした(k = 1 の行は見ていない)。§3 の予想は smoke の前に書いた物のままで、変えない。
- 出力 = `ConstructGap/exp/olm116/`(gen.json・series/*.npz・read.json・log)。RESULT = `conversations/2026-11-03/RESULT_olm116_moy2_frontier_proof_prefix_ladder_20261103.md`。
