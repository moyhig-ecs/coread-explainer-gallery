# NOTES — entry_opus_xhigh_v1(moy-5 の apex への道筋・2026-10-28・作り手 = Opus 5.5 xhigh)

依頼書 = `../BRIEF_v1_moy5_route_to_apex_two_makers_20261028.md`(依頼書を入れた commit = efabcb43・git log はそこまで)。skill = `.claude/skills/coread-explainer/`(SKILL.md と references を全部読み、`assets/` を写して始めた)。手本 = `conversations/2026-10-17/anatomy_silenthop/entry_Q_v5/` の NOTES・CLAIMS・README の頭と、前の競作の BRIEF(`2026-10-27/explainer_olm_line/BRIEF_…`)だけを読んだ。**他の entry の folder・`explainer_moy1/`・AUDIT の本文・memory・MEMO 10-22 の本文・OLMo の rows は読んでいない。** 実験の script は import も実行もしていない(b5bp の runner は β′ の定数の 3 行を text として読んだだけ)。model・通信・install・git の書き込み・subagent なし。ここは作りながらの記録(L1 = 実際に走らせて確かめた / L3 = 作り手の判断)。

## 1. 何を作ったか(状態 24・章 10 = BRIEF §0 のとおり)
- 芯の絵は二つ: **(a) 一つの点 = 一本の答え**(凍結の jsonl の一行・rep の順)の帯。塗りの青 = 答えの欄に cut / 青の輪 = 理由の欄にだけ cut / 小さな灰 = 床だけ / 灰の輪 = どちらも無し。これで「答えの欄の cut と全体の cut をいつも並べる」(BRIEF §3)が一つの記号で守れ、「apex はたいてい下段(理由の欄)にだけ出る」(BRIEF §2)が点の塗りと輪の比で一目に見える。n あたりの数(道の太さ)は点の数そのもの(L3: BRIEF の「道の太さ」をこの形にした)。**(b) 答えの板**(上 = 答えの欄・下 = 理由の欄の二層の slab)。入口(状態 1)と出口(状態 22)は同じ二行(prf3 · Opus · P5 r0 / P5B r0)。
- 立体は四つ: 作図の板(状態 0 · 6・凍結の座標・鏡像にならないよう y を反転)・三つの駅(状態 2)・effort の梯子(状態 9・Fable を奥・Opus を手前・数は柱の上)。回すのは立体の状態だけ(平面の状態で drag を拾うと地図の click が奪われる = 10-27 の落とし穴)。
- 経路は色でなく線の形(実線 API / 破線 `claude -p` / 点線 local)= BRIEF §8 の裁定。新しい色は足していない(青 = kit の `--anatomy-blue` = apex、橙 = 雛形の `--fig-b` = 二次式 / attractor の組。moy-1 の図解と同じ意味)。
- 駅の重さはそろえない(BRIEF §8): 二次式の駅には「読み(L3)の駅」の札を駅そのものに付け、橙が data に付くのは mnw1 cone/Q1 の Fable の頂点の形の 5 本の下線だけ。prf1 / prf3 の式は「式は PROOF が求めた」の札で、橙にしない。neq5 Q3 は足していない。
- 場面の行は BRIEF §1-3 の述語で pack が選び直し、rep が BRIEF と一致することを assert(11 行・句は raw に字のとおり在ることを assert)。

## 2. 数の経路(五本)と、BRIEF と data の食い違い
- ① `pack_data.py`: BRIEF §1-2 の md5 の前方一致(29 file + 3 doc)・BRIEF §6 の照合用の値を全部 assert(V1〜V9)。② `data.mjs`: jsonl を JS で開き、73 cell の点の列・n・rep の並びまで pack と一致しなければ build が止まる。③ `check_claims.py`: anchor 145(raw から・pack を通さない)。④ `make_check.py` の page-vs-raw: 頁の各状態が描いた点の列(`data-dots`)= raw から数えた点の列。⑤ `widget.kernel_check()`: 画面の readout を kernel が raw から数え直す。
- **BRIEF §6 の値で data と違ったものは無い**(全部一致)。
- 開示: SOURCE l.56〜84 の凍結の問いは、末尾の改行を含めて 1921 字で md5 `ee39ba02`(改行なしだと 1920 字・`8071db19`)。essay4 A の行の `prompt_md5` と一致することを assert した。
- 開示: β′ の Opus は欄の `bind` で 6 / 20。SUMMARY §5-3 の 7 / 20 は依頼者の r8 の裁定を含む数(SUMMARY の凍結の表の「cut + r8」の列から読んだ)。図は 6 を出し、7 を状態 11 の限定の行に名指した。
- 開示: essay4 Fable K の r17 は保存の `bind` が偽、SUMMARY の読み直しでは真(表の末尾)。図は保存の欄を使う(Fable K は状態 4 に出していない)。
- 開示: SUMMARY §5-1 の「1 / 717」は BRIEF §6 の注のとおり数え直してから出した: SUMMARY の凍結の表(md5 556b9dfb)の API high の Claude 行のうち K・K@U・Bbp・E-full+Bbp を除く 10 腕 36 行を、pack と check_claims で別々に parse して n 717・全体 1・答えの欄 0。この表は行ごとの点を持たないので、状態 5 は数の表で出した(点の帯にしない)。
- rte1 の 2 × 2(状態 12)は `results_rte1_*` の raw から数えた(照合用の値の外・SUMMARY §10 の値と一致: API max Opus 6 / 10・Fable 2 / 10、claude -p high Opus 2 / 10・Fable 3 / 10)。
- neq2f の行は effort の欄を持たない → RESULT neq2f の題の「Fable 5.1 xhigh」を anchor で縛って xhigh とした。経路は行の `num_turns`(Claude Code の結果)で `claude -p` / `req_opts` で API と、行から読んだ(手で置いていない)。
- olm1 の banner(10-27 監査 A1)は K の腕の think r3 の答えの欄の読み落とし。図は none/Q1 だけを使い、その答えの欄の cut は 0(banner の対象外)。

## 3. 通った検査(数で)
(run_checks.sh の log = `captures/run_checks.log`・marimo の log = `captures/marimo_check.log`)
- build: 頁 4 本・widget js 203 KB・css 20 KB・24 状態。pack 73 cell・1228 本。data.mjs: 73 cell・1228 本を JS で数え直し一致・BRIEF §6 の 32 値・作図の陽性統制 6.1e-4。
- `check_claims.py`: anchors checked 145 · claim rows 145 · missing or different 0。`--calibrate`: 10 kind で「壊れた値は落ち、正しい値は通る」10 / 10。
- 見出し: `list_headings.py` headings ok(24 状態・ja / en の kicker が 0..23)。
- 字の最小 px・はみ出し・NaN・平面の重なり・1080 の枠: 24 状態 × {ja / en × video / desk / phone + 明 + reduced motion} = 192 回の測定で失敗 0(全体の最小 10.05 px = phone・地図の video 10.3 px)。console は 26 回の drive で全部 clean。
- robust: 24 × ja / en × P_x {0, 3, 99, −5} = 192 通り × 6 回(ja / en × 3 枠)・例外 0。
- 章の button(本物の click・最後の章から順に)・番号の step・地図の群の click(状態 3 の G 群 → 状態 14): ja / en / 明 / phone で通過・hash と `aria-pressed` も一致。
- 使わない語の走査: 48 頁(24 × ja / en)で 0 件・走査の陽性統制(植えた語を捕まえ、きれいな文を通す)4 / 4。
- page-vs-raw: 全 24 状態で 128 本の帯(63 cell)の頁の点 = raw の点・readout 4 本・植えた誤り(prf3 P5B Opus)を捕まえる統制 ok。
- marimo 0.23.13: 図 → kernel(図の step 14 を click → kernel が state 14)/ kernel → 図(Python の button → 図が状態 9)/ `kernel_check()` ok・console clean。
- JupyterLab 4.5.6: Run の menu は合成の click で開かず、Shift+Enter の keydown で cell を順に実行した。kernel → 図(`w.state = 9` で図が状態 9・`kernel_check()` ok)/ 図 → kernel(図の step 14 を click → cell 4 を再実行して `14 True …`)。console の warning は jupyterlab-chat 拡張の版の不一致(図と無関係・記録だけ)。JupyterLab が demo_jupyter.ipynb を出力つきで自動保存したので、出力の無い版に書き戻した。log = `captures/jupyterlab_check.log`・撮影 = `captures/jupyterlab_s14.png`。

## 4. 作り手が決めたこと(L3)
- 「道の太さ」を点の数にした(n あたりの数が数え間違いなく読める・合算しない)。
- 状態 3 の地図は BRIEF §0 B1 のとおり章 C〜I の**全部の腕 × model = 63 本の帯**(一度は代表の 23 本で作ったが、BRIEF の「全部の腕を model・n つきで」に合わせて直した)。readout は帯の数だけを出し、本数の総計は出さない(札をまたいで足さない)。1080 の枠に収めるため video は 3 列・帯は一行の高さ(字の最小 10.3 px)。
- 状態 22(台帳 1/2)を「A1 に戻る」に充て、開いた 5 / 開かなかった 5 の手がかりを model・腕・n・出所つきで並べた(授業の受け入れの問い 2 の正答の基準がそのまま読める形)。
- video の枠は全幅・平面の viewBox を 1600 幅にして帯を一行に並べた(1080 に収まり、字は 13.6 px 以上)。
- 答えの板は回さない(字を水平に保つため)。成功と失敗の並べ(状態 1・10・18)は「同じ札・同じ model・同じ腕」でそろえ、そろえ方を lead に書いた。

## 5. 実際に起きた落とし穴(記録)
- zsh で `set -- $fr` が語に分かれず、幅の指定が落ちて三つの枠の測定が同じ値になった → 測定の script を bash で書き直した(計器の側の誤り・値を信じる前に気づいた)。
- 背の高い平面の状態を全幅の video に置くと 1080 の下が切れた(svg の高さが幅で決まる)→ video は svg の高さを固定し、viewBox を中身の高さに合わせ、帯を一行にした。
- 英文は和文より長く、phone で板の副題・帯の数・出所の行が viewBox を越えた → 全部折り返しに(ja と en の両方で測る = skill §12-14)。
- 見出し(q)・台帳・場面に戻る章に、手で書いた数(「Opus 7 / 20」「Haiku 19 / 19」「n 20」など)が残っていた → 全部 data の関数に直した(n は `nOf(cells)` が読み、同じ文の cell で n が違えば例外)。
- 全検査を走らせている最中に build を差し替え、後半の検査が壊れた頁で落ちた → 検査の間は dist に触れない、を守って走らせ直した(最終の log = `captures/run_checks.log`・PASS)。
- phone の effort の梯子(状態 9)は字の大きさは通るが、柱の上の数どうしが近く混んで見える(立体の札は重なりの検査の外)。
- 作図が鏡像だった(kit の床の軸は画面で左手系)→ y を反転。

## 6. 一番自信の無い点
- **BRIEF §2 の芯の絵(三つの駅の上を道が通り、道の上に着いた本の数)を、二つの状態に分けたこと**: 状態 2 の駅と道は説明用(data を載せない・二次式の駅は L3 の札)で、数は状態 3 の点の帯(一つの点 = 一本の答え・全部の腕 63 本)に置いた。数え間違いが起きず、札をまたいで足さない・答えの欄と全体を並べる、の規律は帯の方が守りやすいと判断した(L3)。ただし「一枚で芯が撮れるか」(E2)は、状態 1(答えの板の二行)と状態 3(63 本の帯)の二枚に頼っている。審査で突かれるならここ。
- Argon の thinking の比(Bbp で Claude の 3.8〜8.2 倍)は SUMMARY §6 の文の写し(anchor は text だけ)。本図では raw の `reasoning_tokens` から数え直していない(関係の数の中央値 36 対 11〜19.5 は SUMMARY の凍結の表から数え直した)。
- 答えの板(上 = 答えの欄・下 = 理由の欄)は固定の斜投影の slab で、立体の camera とは別。skill §4 の「二つの立体を一つの camera に」は、答えの板の並べ(状態 1・10・18)には当てていない(字を水平に保つため)。

## 7. 未了・次
- 審査(作り手と違う族の冷間の読み手)は依頼側。受け入れの問い 1〜3 の正答の基準は、状態 1(問い 1)・状態 22(問い 2 = 開いた 5 / 開かなかった 5 の手がかりを model・腕・n・出所つき)・状態 23 の × の行と状態 17 の限定(問い 3)で読める。
- neq5 Q3(symptoma の data の候補)は照合用の値に無いので足していない(BRIEF §8)。

## 8. 納品
- 置き場 = `<repo>/conversations/2026-10-28/explainer_moy5/entry_opus_xhigh_v1/`(scratch から `cp -R`・`diff -rq` で差 0 を確かめてから `DONE`)。worktree では commit していない。納品の直前に repo の HEAD の一行(aafd5e79・別の件)が目に入ったが、efabcb43 より後の commit の中身は読んでいない。

## 10-28 夜 主 session の直し: 章と状態の button を頁の頭へ(依頼者の依頼・作り手の手ではない)
- 依頼(逐語): 依頼者「今更なんですが、状態の選択ボタンが下にあるのですが、ボタンを押すとページの嵩の違いで見失うので、上下移動のない上の方に移動してください。」
- 直し: `build.mjs` の `inner()` で章と状態の button(`.sh-chaps`・`.sh-bar`)を `<div class="sh-nav">` に包み、見出し(`.sh-head`)の前へ移した。`figure.css` の末尾に `sh-nav` の規則を足した(幅 561 px 以上の頁 = `.iso-page` の中では sticky で画面の上に留める・動画の枠 `?video=1` では隠す・widget では sticky にしない)。skill `coread-explainer` の雛形(`assets/build.mjs`・`assets/figure.css`)も同じ直し。
- build: MacBook・bun 1.4.3・Anatomy の kit は zebrashark の `~/.claude/skills/anatomy` を session の scratch に写して `ANATOMY=` で指した(MacBook の skills には入れていない)。直す前の source で build し直すと頁 4 本と widget が zebrashark の物と byte で一致することを先に確かめた(moy-1 Opus v2.1)。dist/ は gitignore の外 = 直した頁はこの機械にだけある(zebrashark では source を pull して `bun build.mjs` で作り直す)。
- 確かめ: (1) 直す前の頁と比べ、違いは button の移動と CSS の規則だけ(頁 4 本・`widget.js`・`widget.css`・図・数・文は同じ = 規則と移動を外すと文字列が一致)。(2) headless Chrome で全 24 状態の帯の上端(頁座標)= 幅 1400 で **16 px 一定**(直す前は 724〜1,446 px(22 通り))・下へ scroll しても画面の上端 0 px に留まる・幅 390 では 30 px 一定(button が何段にも折り返すので sticky にしない)・横のはみ出しなし。
- してないこと: `captures/` と `checks/` は撮り直していない(直す前の配置のまま)。marimo / JupyterLab の widget は開いて確かめていない。
