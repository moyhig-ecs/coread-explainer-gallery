---
name: coread-explainer
description: Build an audited "co-reading" explainer — an interactive isometric figure (Anatomy kit) wrapped as an anywidget for Jupyter / marimo, with 1920×1080 stills, a short two-voice video script, and a ledger of what can / cannot be said — from the frozen outputs of a pre-registered measurement (a "card" = PREREG + script + JSON with provenance), so that a human reader and an AI read the same readout and align their understanding with what the instrument can read. Use this skill whenever the user asks for 図解 / 立体図 / 説明図 / 「anatomy*anywidget」/ an explainer or figure of an instrument readout (logit or tuned lens, probe, benchmark run, sensor log), a figure "for the editor / reviewers", material for ゆっくり動画, a side-by-side of a success and a failure case, or wants to turn a question raised by a figure into a frozen check ("この図で…を確かめたい", "どこから…が湧くのか") — even without saying "co-reading". Layered on the `anatomy` skill (MIT). Not for a quick one-off chart (use dataviz) or a decorative illustration with no data behind it.
license: MIT
compatibility: Claude Code. Needs the `anatomy` skill (its kit; MIT, Copyright (c) 2026 Ryan; https://github.com/wheresryan22/anatomy) at build time only, found at $ANATOMY or ~/.claude/skills/anatomy; bun ≥ 1.3 or Node ≥ 20.10 for the Anatomy scripts, Python 3.12+ with anywidget (marimo / jupyterlab optional), and Chromium (Playwright) for checks and captures.
metadata:
  author: Manabu Higashida
  version: "0.1.0"
---

# coread-explainer — 共読のための図解(監査つき)

この skill は二層でできている。**描き方**は `anatomy` の kit(等角の camera・四段の陰影・枠の card・部品)を使う。**この skill の中身は、その上の規律と仕組み**: 凍結した data だけを読み、数を数え直し、限定を全画面に出し、言える / 言えないを台帳にし、図から出た問いを札に変えて答える。図解は「AI の読み出しに、人間の理解をそろえる」ための面であって、飾りではない。だから一つの数でも出所が辿れないと、図全体の信用が落ちる。

最初の手本は、版を重ねた図解の entry(v1〜v5)。手本の entry は gallery の DOI(10.5281/zenodo.23992312・全版の concept DOI) から取れる。迷ったらその NOTES・CLAIMS・README を読む。

## 0. 始める前に決めること(BRIEF に書く)

図解の依頼は、毎回 BRIEF(発注書)に落としてから作る。BRIEF が無いと、作り手は材料の外を読み、数を手で置き、評価の軸を自分で決めてしまう。BRIEF に書くもの:

1. **発注の逐語**(依頼した人の言葉をそのまま・日付)。
2. **読み手と最終評価**(既定は三つ。別の読み手なら差し替える):
   - **E1 editor**: 図と文が論文(または報告)に忠実で、論文が主張しないことを主張していない。論文の図・補遺として出せる質。
   - **E2 動画の作者**: 1920 × 1080 の撮影と台本だけで、1〜2 分の一場面が作れる。最初の 10 秒で芯が見える。
   - **E4 「この計器だから、この読みが出た」**: 陽性統制・門(eligible の判定)・帯や条件を替えると読みが変わること、が根拠の鎖として撮影の上で見える。
   - **読み手を差し替えたら、その読み手で測る受け入れの試験も書く**(例: 授業の学生なら、図を見た後に答える問い 3 つと、正答の基準)。E1 / E2 / E4 の名前を残すだけでは、学生向けの図解を通す物差しにならない。
3. **材料の一覧**(絶対 path・これだけを読む)と **読まないもの**(他の作り手の folder・判定・memory)。
4. **照合用の値**(実行層が data から読んだ値を数個)。合わなければ data が正しい、と書く。
5. **置き場**(`entry_<札>_vN/`・前の版の folder は書き換えない)と **scratch**(作り手ごとに別の subdir)。
6. **打ち切り**(分)と **返すもの**(≤ 10 行: file・状態の数・撮影・照合の結果・一番自信の無い点)。

→ 雛形は `references/brief-template.md`。

## 1. 材料の契約(data contract)

- 読むのは **凍結した札の出力** だけ(JSON・npz・図の png)。札 = PREREG(問い・宇宙・統制・判定・主張しないこと)+ script + 出力(provenance = commit・dirty・md5)。札の外の数を図に出さない。
- **実験の script を import も実行もしない**(main の守りの無い集計 script は、import しただけで凍結した結果を書き換えることがある)。data の file を読むだけ。
- **数は script が data から出す**。手で HTML や台本に写さない。出した数は **二つ以上の独立した経路で数え直す**(例: pack の Python の assert / 頁の JS / kernel の側 / `check_claims.py` の anchor = file と key と期待値)。照合用の値と食い違えば、data を正として依頼側に知らせる。
- **潰した値の柵**: 上限で潰した順位(例: 1000 位より下 = 1001)は霧・一様な色で描き、「沈んだ」「抑えられた」と描かない・言わない。潰す順序(潰してから median か、median してから潰すか)を札の文と実装で揃え、偶数個の median で食い違うなら開示する。
- **eligible でない帯・条件の値**は、比べの片側として「監査を通っていない」札つきでだけ見せる。そこで null を「無い」と描かない。
- 同じ seed・同じ prompt の族から来た行は独立に数えない(「違う場面は 3 つ」のように数え方を明記)。
- **RESULT の読み(L3)は data ではない**。RESULT の文を図に写す前に、その文が data の数で成り立つかを確かめる。割合の話を数の話に取り違えた例がある(「上位の多くは予告とこだま」= 位置あたりの割合では正しいが、数では基線の位置が 8 割を占めた)。成り立たなければ図に写さず、台帳の「言えない」に回し、RESULT の側にも訂正を頼む。
- **伸びている file は凍結した写しにしてから渡す**(log・日々の記録): 行の範囲と md5 を BRIEF に書き、作り手はその範囲だけを読む。後から書き足された記録(例えば評価の答え)が材料に混ざるのを防ぐ。

→ 詳細と落とし穴は `references/data-contract.md`。

## 2. 作るもの(一つの entry folder)

```
entry_<札>_vN/
  build.mjs            kit から頁と widget の ESM / CSS を組む(HTML を手で直さない)
  pack_*.py            data → 図の pack(assert で数え直しの第一経路)
  data.mjs / live.js   頁の状態の機械・描画(第二経路の数え直し)
  i18n.js              ja / en の文
  *_widget.py/.js/.css anywidget(traits: state・row・t・layer・band・lang・theme ほか)
  demo_marimo.py  demo_jupyter.ipynb
  check_claims.py  make_check.py  run_*.sh   検査(§5)
  captures/            撮影(§6)
  CLAIMS.md  NOTES.md  README.md  SCRIPT_yukkuri.md
  (内部の層は別 file: *_layer.js / *.css / README_internal.md — §8)
```

- **章と状態**: 状態(0, 1, 2 …)を歩く図にし、章で束ねる(例: 場面 → 監査 → 本題の場面 → 共読の一巡 → 台帳)。状態の番号の列の上に **章の button** を置く(押すと章の最初の状態へ)。**章と状態の button は見出しより上(頁の頭)に置く**(`.sh-nav`・頁では sticky で画面の上に留める): 下に置くと、見出しの文の長さで状態ごとに button が上下に動き、押した後に見失う(依頼者 10-28 夜「ボタンを押すとページの嵩の違いで見失うので、上下移動のない上の方に」・直す前は状態によって 900 px 以上動いた)。検査に「全状態で帯の上端が同じ」を入れる。番号を振り直したら、見出しの一覧(状態番号 → 見出し)を出して自分で確かめる(振り直しの script の二重ずらしは実際に起きた)。
- **widget** は iframe で包まない。図の操作が Python に届き、Python から状態を書ける(双方向)。marimo と JupyterLab の両方で通す。
- **頁は 4 本**(暗 / 明 × ja / en)を build から。

→ 実装の型は `references/implementation.md`(手本の entry を元にした骨組み)。**最小の雛形は `assets/`**(合成の data で build・検査・撮影まで通した骨: `config.json` が状態・章・枠の番号の唯一の置き場 / `run_checks.sh` / `list_headings.py` / `_smoke/` に動作の証拠)。新しい図解はここから写して始める。

## 3. 言葉の規律(台帳: 言える / 読み / 言えない)

台帳は図の最後の章に置き、各行に出所(file と key)を付ける:
- **言える(L1)**: data の値の写し・凍結した判定。
- **読み(L3)**: 誰の読みか(実行層 / 作り手)を明記し、「採否は人間」と札を付ける。言い回しを依頼者が差し替える前提の文には、そう札を付ける。
- **言えない**: 平叙文で明言する(「〜とは言わない」)。小さな注や「〜かもしれない」で終える形にしない。少なくとも: 機構 / 同定(裁定が並置に留めたものを同じ物と呼ぶ)/ 量の判断(差が誤差帯より小さい)/ 計器の妥当域の外での読み / 読んでいない側(例: prompt の側)/ 一例から「だけ」/ 独立でない行を独立に数えること。

本文と台本で使わない語: 「model が考えた・迷った・気づいた・知っていた・本当は分かっていた」、「AI の心が見えた」「嘘を見抜く」類の誇張。lens の順位は lens の読み出しであって、model の中身の地図ではない、と図に書く。

**限定の札を、章の全画面に出す**(枠の下の一行 + 右上の身分の札): 妥当域・記述だけ・同定しない・読んでいない側・n。撮影に写っていない限定は、無いのと同じ。**ただし限定は、その画面の data に本当に当てはまるかを確かめてから貼る**。文例(`references/wording.md`)をそのまま全章に写さない。例: 「位置はすべて計器の fit 域の外」は、行ごとの位置で確かめる(手本では、ある条件の行は外だが、別の条件の行は prompt が短く内側だった)。当てはまる範囲が章の中で割れるなら、札を行ごとに分ける。

→ 文例と禁じ語の一覧は `references/wording.md`。

## 4. 見せ方の型(v1〜v5 で効いたもの)

- **入口は場面**: 最初の章は「何が起きた瞬間か」を一枚で(例: 答えを書く前の prompt の上で中間語が浮く・答えの板は空のまま)。数の監査はその後。
- **立体の三軸**: 横 = 位置(書いていく token)・縦 = 層・奥 = 計器の順位(手前 = 1 位・対数・上限より奥は霧)。統制の帯は厚板、帯の外は灰で「統制の外・参考」。
- **成功と失敗を並べる**: 二つの立体を **一つの投影・一つのカメラ・共通の目盛り** に置き、片方を回すと両方回る。video は左右 / desk と phone は縦積み(札の最小の字を保つため)。
- **そろえ方を宣言する**: 出力が違う二行は、どこでそろえたか(分かれ道 / 要の語 / 欄の頭)を明記し、**そろえた所から要の語までの距離が違う**なら「+1 token / +3 token」と書く。距離をそろえた見方(要の語の位置 k でそろえた small multiples)を並べる。
- **長さ 0 の部分も枠で描く**: 片方にだけ在る部分(例: 考える欄 <n> token / 0 token)は、両方に同じ幅の枠を立て、片方は点線の空の枠にする。余白だけだと描き損じに見え、突っ込まれる。
- **予告とこだま**: 計器が「これから書く語」「直前に書いた語」を上位に出すなら、その位置(F / E)を印で分け、静かな位置と分けて見せる。
- **data に無い所を補わない**: data が集計だけで行ごとの位置を持たないなら、入口の場面は「模式図(実在の行ではない)」と札を付ける。記録に無い途中の状態(例: 3 台 → 1 台の間に 2 台を挟む・一台ずつ消える順番)を描かない。記録の間隔(例: 2 分おき)の外の時刻は「この間のどこか」と幅で書く。
- **呼び名は一か所で決める**: 位置・行・面の呼び名(例: 「分かれ道」「そろえた位置」)は helper か config の一か所に置き、全画面の文が同じ物を同じ名で呼ぶ。旧い呼び名が残っていないかを走査する検査を足す(§5)。
- **色の意味は一つ**: 既に意味を持つ色(例: 橙 = He/Hi の組・青 = apex の組)を保ち、新しい色は足さない。data でない飾り(内部の層のたとえ)にだけ色を足すときは、dataviz の validator で既存の色と normal ΔE ≥ 15・CVD ΔE ≥ 8 を暗 / 明の両面で確かめる。第三者の character・画像・外部 font を使わない。

## 5. 検査(撮る前に全部通す)

- console が clean(頁 4 本・desk・phone・video・reduced motion・marimo・JupyterLab)。図と無関係な拡張の warning は記録して区別する。
- **robust**: 全状態 × 全行 × 層のいくつか で例外 0。
- **数の照合**: `check_claims.py` の anchor(file・key・期待値)が全部一致・欠け 0。照合用の値 N / N。
- **章の button**: 本物の click で各章の最初の状態へ着き、選ばれた見た目・hash・ラベル(ja / en)が合う。
- **字の大きさ**: 撮影の枠ごとに札の最小 px を測る(目安 video ≥ 10 px・desk ≥ 10 px・phone ≥ 9.5 px)。読めない札は無いのと同じ。
- **はみ出し**: viewBox の外に出る文字 0。
- **公開の柵**: 本体の file に内部の語(§8)が 0 件(grep で数える)。
- **呼び名の走査**: 全状態 × ja / en の頁の text を走査し、旧い呼び名・禁じた文脈が 0 件。走査そのものの陽性統制(旧い文言を混ぜた頁で検出できること)も取る。
- 道具の覚え書き: phone の札の最小 px は、viewBox を絞って字を大きくし、kit の四隅の文を縦の列に直して初めて 9.5 px に届く(雛形の初期値は 2.7 px だった)。`?video=1` は章の button を隠すので、click の検査は desk と phone で行う。

→ `references/checks-and-captures.md`。

## 6. 撮影と台本

- 各状態の **1920 × 1080**(video 用・ちょうどその大きさ)+ desk(暗 / 明)+ phone。瞬間を見せる状態は前後二枚(例: 位置 24 → 25)。
- `SCRIPT_yukkuri.md`: 掛け合い(A = 聞き手 / B = 解説)で ≤ 150 秒・行ごとに映す状態の cue・最初の 10 秒は場面。実在の character の名や絵を使わない。

## 7. 共読の一巡(この図解の一番の使い道)

図を見た人が問いを出したら(例: 「どこから He が湧いてくるのか」)、それを札に変えて答える。手順:
0. **問いの言葉を確かめる**: 問いが指す位置・行・語が図の中で一つに決まるかを見る。図の中で呼び名が揺れている(例: 同じ位置を、ある画面は「分かれ道」、別の画面は「分かれ道の一つ手前」と呼ぶ)なら、数を読む前に問いを出した人に一問で確かめ、図の呼び名の揺れも直しに回す。
1. **候補を挙げる(読み・L3)**: 問いに答えうる説明を二〜三。それぞれに三つの印を付ける: (a) 計器(lens)に依るか・依らないか / (b) その量が **persist(保存済みの data)に在るか・新しい forward が要るか・新しい生成が要るか**(「persist に無い」は「量が存在しない」ではない — 例: model 自身の出力の順位はどの位置にもあるが、保存したのは書いた token の順位だけ)/ (c) 稿の柵に触れるか(例: 統制の帯の外の層に述語を繋がない)。**順番は「lens に依らず・persist に在る」候補を先に**、次に forward が要る候補、lens に依る候補はその後。柵に触れる候補は外す。
2. **札を先に凍結する**: PREREG(問い・宇宙・統制 = 陽性統制を含む・読み方の言葉・主張しないこと・事前に見たものの開示)と script を一つの commit に入れ、dirty でないときだけ `--fire` が走るようにする。**値を見る前に凍結する**。
3. **読む → RESULT**: 数は出力の写し(L1)・読みは L3・主張しないことは PREREG のまま。
4. **統制が落ちたら止める**: 図の data を書かずに停止し、原因を本文の側だけで診断し、直した版を **新しい札** として凍結し直す(走った後に札の定義を動かさない)。例: token ごとの文字の復号が多 byte の文字の割れ目で U+FFFD に化け、位置と本文がずれた → 統制 C2 が捕まえた → byte で対応を取る新しい札。AI の読みにも統制が要る、の実例として記録する。
5. **図に一つの状態として戻す**: 「図から問いが出て、札で答える」= 図を見る → 人間の問い → AI の候補 → 札を凍結して読む → 答えと言えないこと → 次の問い。

→ `references/coread-loop.md`(札の雛形・統制の考え方)。

## 8. 内部の層(たとえ・内輪の語)

研究室の内輪のたとえ(例: 内部名・マスコット)を図に入れたいときは、**隠しの層** にする: 別 file(`*_layer.js` / `*.css` / `README_internal.md`)に置き、本体は「在れば読む・無ければ何もしない」だけ。出し入れは隠しコマンド(キーの並び)+ URL の flag + widget の trait。既定 off・日本語の頁だけ・英語の頁では何もしない。層が on のときの右上に「内部の層・外には出さない」。本体の file に内輪の語が 0 件であることを検査に入れる(公開の束から図解ごと外れないように)。たとえの絵は自前で描き、たとえが機構の主張に読めないよう、層の中でも「言えない」を明言する。

## 9. 審査と版

- 版ごとに置き場を分け(`_v1`…`_vN`)、前の版を書き換えない。小さな直しは `vN.1, vN.2 …` として NOTES に「何を直したか・誰の指摘か」を書く。
- 審査は **作り手と違う族の model** の冷間の読み手に、判定基準の file と撮影と CLAIMS / NOTES / README だけを渡す(互いの判定を見せない・作り手を推測させない)。物差しは E1 / E2 / E4(+ 参考の E3)。基準の雛形は `references/judging.md`。

## 10. 公開(論文に添えるとき)

- 動く頁は **GitHub Pages**(静的 site)で見せ、同じ repo の release を **Zenodo** で DOI 付きに凍結する(Zenodo は HTML を描画しないが、一式を落とせば `file://` で動く)。稿には両方を書く。
- 公開の束から内部の層(§8)を外す。Anatomy の MIT の表示(Copyright (c) 2026 Ryan)を README と頁の下に残す。
- **この SKILL.md 自体を束に入れる**: 完全な再現はできなくても、図解を作った手順(プロンプト)を示せる。
- md5 を MANIFEST に。→ `references/publishing.md`。
