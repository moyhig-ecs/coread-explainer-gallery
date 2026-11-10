HEAD(R1) = fe3a016c(凍結時の HEAD・origin より 11 commit 先・遅れ 0 = この file と runner を入れる commit の親・RESULT olm113 の直後)

# PREREG(札 `olm114`・凍結 2026-11-02): frontier(Opus 5.5 / Fable 5.1・prf5)の証明の欄を OLMo-3 32B base に順次喰わせる — 二等分線の段(k = 1)/ 直角の段(k = 2)まで与えると残りの鎖を続けるか(A・生成)・段の語の先読みと commit 方向の係数(B・forward・記述)

- 発注(逐語・先生 11-02 夕): 「**フロンティアと比べるとOLMoの浅さが見えますが、moy-5でやったような、Fable/Opusの思考 (証明) の過程を順次喰わせてみたらどうでしょう？**」→「**思考の過程は語弊があるので、出力です。**」
  - 先生の選び(11-02・主 session の四つの問いへ): (A)(B) **両方** / k = **1・2** / 証明は **Opus 10 + Fable 10 の両方**(「Opusはまだ落ちているかもしれません」= frontier への新しい呼び出しはしない・prf5 の出力を使う)/ 走らせるのは **明日**。
- G10 の欄: 比べる物 = 「k = 1(O1・O2 を二等分線の上に置いた段まで与えた)の行で、OLMo の続きが RA ∧ THC を満たす割合」/「k = 2(∠O1XO2 = 90° の段まで与えた)の行で、続きが THC を満たす割合」/「k = 0(M1B の文・書き出しなし)の答えの欄が apex の行で、証明の欄が CHAIN を満たす割合」 / 計器 = hq 共通の部品の凍結の述語 score_m1(BIS・ADJ・RA・THC・COORD・較正 61 / 61)を**続きの文だけ**に当てる + この札の段の切り方・続きの取り出しの較正 13 例・(B)は olm67 の計器(層 48 の J-lens / logit lens の語の集合の対数質量の百分位 u・層 32 の commit 方向 d̂ = olm64 directions) / 雛形 = いいえ
- runner = [olm114_…py](../../ConstructGap/exp/olm114_moy1_frontier_proof_prefix_ladder_20261102.py)・共通の部品 = [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(凍結 cb12da8d・触らない)・問いの文 = [prf5 runner](../../ConstructGap/exp/prf5_moy12_proof_field_jsononly_claude_p_20261102.py) の M1B(凍結 5f519216)・frontier の出力 = `ConstructGap/exp/results_prf5_20261102.jsonl`(md5 `995650e5…` を guard で assert)。走らせる所 = zebrashark(32B は一つずつ・olm113 の後・明日)。`--gen`(A)→ `--fire`(B)→ `--read`。API なし。

## §0. 起案の前に見た物(開示)

- 主 session は prf5 の 20 本の証明と `reason` の欄を全文読んだ([RESULT prf5](RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md) の執筆と、この札の段の切り方の設計のため)。olm112 の 100 行(apex 37 行で鎖 0)も読んだ([RESULT olm112](RESULT_olm112_moy1_apex_status_and_geometric_proof_20261102.md))。**予想はこれらを見た上で付けた**。
- 段の切り方(k1 = O1・O2 を二等分線の上に置いた段・k2 = RA の段)と除外の規則は 20 本を見た後に書いたが、機械の判別条件(R5)で、`--plan` の結果 **20 / 20 が k = 1 と k = 2 の両方に入った(除外 0)**。
- frontier の `reason` の欄は鎖の全部を含む(20 本中 18 本で RA か THC が真・BIS は 19 本)。渡すと k = 0 相当の所で鎖が与えられてしまうので、**書き出しは `conjecture` と `proof` の二欄だけ**にする(`reason`・`closes_goal` は渡さない)。これは frontier の文の選択で、書き換えではない。
- smoke(凍結の前・3 行・読まない): 数は §6。

## §1. 計器(R5)

- **問いの文**(全腕共通)= prf5 の M1B(凍結の F5a-2 の置き換えを元の `Respond with JSON only:` に戻した物 + 証明と status を欄で求める追記・`First write your reasoning` の一行なし)+ cue。OLMo に渡す文の md5 `15dec317…`(cc 形 `ce8eac2b…` = prf5 の行の prompt_md5)。
- **書き出し(k = 1・2)** = `{"conjecture": <frontier の conjecture 逐語>, "proof": "<P_k 逐語>`(json.dumps で再直列化・証明の文字列の閉じの `"` を付けない)。P_k = frontier の証明の先頭から k の段の終わりまで(rstrip)。
  - **段** = frontier 自身の番号 `(n)` / `Step n` を n = 1, 2, … の順に取る(本文中の参照「By (2) and (3)」は飛ばす・「Steps 1–7」は段でない)。
  - **k1** = 最初に BIS(score_m1 の累積の prefix で真)になった段以降で、最初に O2 を含む段(= 両方の中心が二等分線の上に置かれた所)。**k2** = 最初に RA(累積の prefix で真)になった段。
  - **除外(機械)**: ok1 = P_k1 に RA が無く、Thales の語(`thales|converse|semi-?circle|angle in a semi`)も無い。ok2 = RA の段に Thales の語が無く、k2 > k1。どちらも 20 / 20 で通った(§0)。
  - 記述の印 given_perp = P_k1 が perpendicular / ⊥ を含む(二等分線が直交することを先に言っている文)= 7 / 20(fable_r8・opus_r1・r2・r3・r5・r6・r8)。
- **続きの取り出し** = 書き出し + 生成を JSON として先頭から decode。閉じていれば `proof` の欄から書き出しの分を除いた残り = 続き(closed = 真・`status` の欄も読む・JSON の後の文字数 = tail)。閉じていなければ最初のエスケープされていない `"` まで = 続き(closed = 偽)。
- **続きの述語** = score_m1(続き)の BIS・ADJ・RA・THC・COORD・ALT(hq の凍結の述語をそのまま・**続きだけ**に当てる = 与えた段の語は数えない)+ thales_c(Thales の狭い語)。
  - k = 1 の主 = **RA ∧ THC**(二等分線は与えた・残り = 隣り合う二等分線の直交 → 直角 → Thales の逆)。k = 2 の主 = **THC**(残り = Thales の逆)。
- **k = 0** = 書き出しなし(M1B の文を OLMo に)= 揃える腕。読み = olm112 と同じ(凍結の分類器 analyze → label_json_fields・status_of・proof_of・score_m1)。
- **生成** = MLX batch_generate・温度 0.7・`allenai/Olmo-3-1125-32B` base。k = 1: 20 本 × 2 rep(seed 20261140・41・max_new 1536)/ k = 2: 20 本 × 2 rep(seed 20261142・43・max_new 1536)/ k = 0: 2 batch × 20 行(seed 20261144・45・max_new 4096)。= 120 行。seed は olm87 / 90 / 112 / 113 と重ねない。
- **(B) forward**(記述)= 問いの文 + `{"conjecture", "proof"(全文)}` を閉じた JSON を forward(層 32・48・63・生成なし・BOS なし)。語の集合(token id・先頭の sub-token)= BIS {` bis`} / RA {` perpendicular`} / THC {` converse`} / ATTR {` He`, ` Hi`, ` radical`} / ADJ {` adjacent`, ` supplementary`}。読み = 層 48 の J-lens(olm65 の jac・層 48)と logit lens の log-mass の行内の百分位 u・証明の領域での集合の最初の出現 w の u(w − k)(k = 1〜8・olm67 Q2 の型・null = 無作為位置 1000 回)・段の切れ目(k1・k2・証明の終わり)の前後 32 token の窓の平均(u と層 32 の commit 方向の係数 proj32)。
  - 統制 = C1(J-lens の cos(J h48, h63) > cos(h48, h63)・行の 95 % 以上・olm67 と同じ)・C3(方向のノルム = olm4 の記録)・round_trip。通らなければ (B) は RESULT に載せない。
- **較正(R6)** = hq の 61 / 61 + この札の 13 例(段の分け方 2・切る規則 7・続きの取り出し 3・書き出し 1 = 正と負)。runner の guard で、通らなければ走らない。

## §2. 関門

- **G1**: k = 1 の行(生成が空でない)≥ 24 / k = 2 の行 ≥ 24。✗ → その Q を読まない。
- **G2**: k = 0 の label の無い行 ≤ 4、かつ答えの欄 B-bind ≥ 8。✗ → Q3 を読まない。
- **(B)**: C1・C3・round_trip。✗ → (B) を載せない。
- 較正(hq 61 / 61・この札 13 / 13)= runner の guard。prf5 の jsonl の md5 = guard。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | k = 1 の行で、続きが RA ∧ THC を満たす割合 | **続ける** ≥ 0.50・**続けない** ≤ 0.10・ほか = 間 | 続ける 0.25・続けない 0.35・間 0.40 |
| Q2 | k = 2 の行で、続きが THC を満たす割合 | **続ける** ≥ 0.50・**続けない** ≤ 0.10・ほか = 間 | 続ける 0.55・続けない 0.15・間 0.30 |
| Q3 | k = 0 の答えの欄が B-bind の行で、証明の欄が CHAIN を満たす割合(olm112 の 0 / 37 と prf5 の 20 / 20 の間に置く揃える腕) | **出る** ≥ 0.20・**変わらない** ≤ 0.05・ほか = 間 | 変わらない 0.65・出る 0.15・間 0.20 |
| Q4 | 記述: 群ごとの述語(BIS・ADJ・RA・THC・COORD・ALT)・closed・空の続き・tail・status・T・family 別(Opus の文 / Fable の文)・given_perp 別・k = 0 の答えの欄の内訳と apex の率(olm112 = 0.37)・(B) の先読みの表と窓の表 | — | — |

## §4. 読み方

- `--read` が `olm114/read.json` を書く(関門・Q1〜Q4・行ごとの印・(B))。判定は凍結の述語の値だけで付ける。
- RESULT では、k = 1 の続きのうち RA ∧ THC を満たした物を行の名の順に最大 10 本、満たさなかった物を行の名の順に 4 本おきで最大 10 本、逐語で引く。k = 2 も同じ型で各 5 本。主 session の読み(L3)は述語の値と並べ、違っても判定は変えない(違いは開示する)。(B) は表だけ。

## §5. 主張しないこと

- 書き出しは frontier の文なので、続きが鎖を完成しても「OLMo が導いた」ではなく「**与えられた段の続きを書けた**」まで。写しと導きの区別は、述語を続きだけに当てることで付ける(与えた段の語は数えない)。
- apex(conjecture)は与えている。この札は「apex に着くか」を測らない(k = 0 だけが測る)。
- k の段の中身は frontier の文ごとに違う(段の数 5〜9・P_k1 の長さ 442〜873 字・given_perp 7 / 20)。family(Opus / Fable)の差は文の差と混ざる。
- reason を外した書き出しは frontier の出力の一部で、全部ではない。
- (B) の先読みは olm67 の計器(moy-5 の cut の語)を moy-1 の段の語に移した物で、この札の中の陽性統制は C1・C3 だけ(語の集合ごとの統制は無い)→ 記述に留める。` perpendicular` は二等分線の段より前にも出る(「perpendiculars from O1」)・` He`・` Hi` は問いの文にも出る。
- base model・一つの温度・rep 2・frontier 20 本。CHAIN は語の鎖で、証明の正しさの検証ではない。

## §6. 走らせ方と記録

- zebrashark: `python ConstructGap/exp/olm114_moy1_frontier_proof_prefix_ladder_20261102.py --selftest`(PASS・plan ok1 20 / 20・ok2 20 / 20)→ `--smoke`(凍結の前・3 行・読まない)→ 凍結 → 明日 `--gen`(約 1〜2 時間の見込み)→ `--fire`(forward 20 本・数分)→ `--read`。
- smoke(凍結の前・seed 20261197〜99・k = 1 / k = 2 / k = 0 各 1 行・max_new 512 / 512 / 1024・読まない・zebrashark 20:55〜20:57・壁時計 58 / 69 / 106 s・Traceback 0・`olm114/smoke.json`・`smoke_run.log`): k = 1(fable_r0・与えた段 657 字)= T 437・JSON 閉じた・続き 1,241 字・status hypothesis / k = 2(fable_r0・与えた段 1,433 字)= T 63・閉じた・続き 178 字・status hypothesis / k = 0 = T 341・欄の印 B-flail・証明の欄 0 字・答えが先。本文は読んでいない。
  - 開示: smoke の log は続きの RA / THC の有無も印字する作りで、主 session はその 2 行を目にした(k = 1: RA 1・THC 1 / k = 2: RA 1・THC 1)。§3 の予想は smoke の前に書いた物のままで、変えない(prf5 の段 1 と同じ扱い)。
- 出力 = `ConstructGap/exp/olm114/`(gen.json・series/*.npz・read.json・log)。RESULT = `conversations/2026-11-02/RESULT_olm114_moy1_frontier_proof_prefix_ladder_20261102.md`。
