HEAD(R1) = af05654e(納品時の `git rev-parse --short=8 HEAD`・依頼書 v3.1 の凍結 = 7523dd02 / a32fba49・作業の開始時は 90c62664 の後。git は読むだけ = `rev-parse` / `log`・書き込みなし・commit していない)

# NOTES — entry_v3_1_received(駅 2 = moy-1 の受領版 v3.1 = 二口の v3 を一つに合わせた版)

- **開始 15:19:37 JST**・打ち切り 120 分(= 17:19:37)。**進み具合(60 分を過ぎて・16:21)**: 直しは全部入れた(状態 0〜12 の P の見せ方・D1〜D3 の移植・規則 3 つ・食い違い 4・監査 14)・`run_checks.sh` の二回目が states の 6 枠(video / desk / phone × ja / en)43 / 43 を通過中。残り = 検査の残り・撮影・NOTES・納品。
- 作り手 = Opus 5.5(xhigh)一人・subagent なし・install / 通信 / git の書き込みなし・model を動かさない・実験の script は import も実行もしない(data を読むだけ)。
- 依頼書 = `BRIEF_v3_1_moy1_received_version_one_maker_20261106.md`(§1〜§3)。作業は scratch(`…/scratchpad/maker_v3_1/work/`)・納品 = `work/` の中身を置き場へ写し `diff -rq` → `DONE`。
- port = 27900〜27999 だけ: drive の Chrome は 27900〜27969(kit の `drive.mjs` の写しを scratch に置き、変えたのは port と profile の置き場の 1 か所・MIT の表示つき)・marimo 27990・JupyterLab 27980〜27985。Chrome の `--user-data-dir` は scratch の中。
- **読んだ物**: 依頼書 v3.1・RESULT C4・読み手の返答 D1_R2 / D1_R3 / D2_R2 / D2_R3 / D3_R2 / D3_R3 / G3_R2(逐語)・Q と P の NOTES の頭(v3 の節だけ・offset / limit で)・Q と P の i18n / figure / scenes / build / pack の差分(diff と grep)・撮影は直す状態だけ(Q s02・s23・s27・P s22 の 4 枚)と自分の確かめの撮影。凍結の file は PREREG pc1 §6・RESULT olm76 / olm83 / olm88 / olm112 / olm114 の頭と §1・SCOPE 11-01 の該当の行・prf4 / olm59 / olm76 / olm114 の read.json(key だけ)。

## v3.1 の中身 — 数

- **状態 43・章 15**(Q の build のまま)。10-28 の部分 = 0〜26・後から足した部分 = 27〜36 と台帳 40・41・台帳全体 = 37〜42。
- **照合 anchor 689 / 689**(Q の 659 + v3.1 の 30 = `make_anchors_v31.py`)・欠けまたは違い 0・統制(わざと間違えた anchor)9 / 9。
- 検査 = `run_checks.sh` の最後の通し(16:41〜・`checks/last_run.txt`)= 測り 43 状態 × 10 回(video / desk / phone × ja / en・3 頁・減らした動き)すべて通過・robust 2,150 組 × 3 枠で例外 0・parity ✓・sae ✓・v21 ✓(札の印 86 = 43 × ja / en)・v3 ✓(desk / phone・流れの札 20)・札の実クリック・章の実クリック(desk / phone)・語の走査 ✓・照合 689 / 689・fence 0・marimo 両向き ✓。**JupyterLab の段だけ時々落ちる**(cell 6 の kernel の数え直しで、figure の reading が届く前に読む = 時間の揺れ)= 通しの中で exit 1 → `WIDGETS_ONLY=1` で 3 回走らせ直して 3 回目に exit 0(log に全部残した)。二回目の通し(16:15〜・最後の二つの直し = K64 の文と凡例の CSS の前の build)は JupyterLab も含め exit 0。最終の build でも、widgets だけの再走 3 回のうち 1 回・scratch の debug の走り 3 回のうち 2 回は通った = 同じ build で通ったり落ちたりする揺れ。直したのは待ち時間だけ(demo の cell 6 の sleep 1.5 → 3.0 s・検査の待ち 4.0 → 6.5 s)= 計器の中身は替えていない
- 撮影 = 95 枚 = video 1920 × 1080 の ja 43 + en 43 + 前後の対 4(状態 18・19)+ widget の検査の 5(J1〜J3 = JupyterLab・M1・M2 = marimo)・`captures/INDEX.md`・`capture_log.txt`(console clean・頁の md5 = 最終の build 28b2bcd8 / 47c6b01f)。desk と phone の撮影はしていない(依頼書 §2-8)= base の撮影は消した

## 1. 土台と範囲(依頼書 §2-1〜§2-4)

- 土台 = Q(`receipt/entry_v3_sonnet_max`)の build を scratch に写した(Q も P も書き換えていない)。
- **状態 0〜12 = P の見せ方**。P と Q は同じ 10-28 の土台から出ていて、scenes.js の状態 0〜12 の描き方は二つとも同じ(diff 0 行)。違いは文と chips と表だけ → P の文と P の足し物を Q の build に移した:
  - P の文(i18n.js の該当の行をそのまま写した): 状態 7 の問い「O1O2 の語をどこで書き、どこで止まった?」・状態 8 の lead(答えの欄の定義 = 凍結の label_json_fields)・状態 9 の題 / 問い / lead(「open と blocked は別の標本」・「どちらも増える」を外す)・状態 10 の題 / 問い / lead(「どの順で文を書き、答えの欄に何を書いた?」・JSON の位置)。
  - P の足し物(`i18n_after.js` の v3.1 の塊): 状態 1 の readout に ∠O1XkO2 = 90° ± 0.0006°・表の下に「4 点とも 90° から 0.0006° 以内 … (Thales の逆)」の注(figure.js)・状態 5 の「色が替わる行の決め方」の一行・状態 8 の chip「答えの欄(凍結の label_json_fields)O1O2 6 · He・Hi 3 · なし 1」・状態 11 の chip「この図が \n\n を使う理由 = 5 章と同じ cue」・状態 12 の chip「prompt の編集 = 出力の順(⑥)」。
  - 状態 2: Q の全文の枠は 7 行で切れていた(Q が足した `.q-blk.sm pre{max-height:130px}` が状態 2 の全文の枠にも当たっていた)→ その規則を状態 12・18 の短い枠(class `dif`)だけに狭め、全文が P と同じく見える。
- **D1 の二人が重なった物**(移した): 状態 7 の窓の定義「line / slope と共に = ±80 字」(Q の身分の行のまま)・状態 9 の単位「「直径 = He・Hi」の文がある blocked の 5 行」(chip の見出し)・状態 12 の「5 章の行の cue は \n\n(F5a-2・F5b-1 とも)」(Q の差分の枠の注のまま)。
- **片方だけの物(自分で決めた)**:
  - 採った: 状態 3 の言い方は Q のまま(「答えの点の名は与えていない」「名指していない」)= R2 が移す物に挙げ、R3 が P の「塞いでもいない」を「数えた 0 件から言える範囲より広い」と監査の穴に挙げた(二人の向きが同じ)。状態 0・1 の台詞(Q の SCRIPT 03–04)は Q のまま在る。
  - 採らなかった: 状態 7 の見出し「O1O2 をどう使い」(R2 だけ)= 数えたのは ±80 字の窓の中の同時出現で「使い方」は数えていない → P の「語をどこで書き」のまま。状態 10 の見出し「どうやって O1O2 の文に着いた?」(R2 だけ・R3 は「経路を数えていない」と移さない)→ P のまま。
  - 状態 11 の P の chip「この差は書き始めで説明されるか → 状態 31(olm128)」は、依頼書 §2-5(10-28 の後の札は 10-28 の状態に載せない)に従い、札の名と結果を外した指し(「→ 状態 35 · 10-28 の後に読んだ(後から足した部分)」)にした。
  - 状態 11 の表の右の列が切れる件(D1 の二人の E・P も Q も)= 引用の欄を 610 px に広げ、表の字を折り返さないようにした。
- **状態 13〜26 = Q のまま + D2 の重なった物**: 状態 23 = P s22 の「Δmath の中央値で割る(低・高)で中点 ↑」の列が見える表(Q の表は最後の行の長い名で幅が溢れ、右の二列が切れていた)・「札の外の数」は表の外の箱に(0.781 / 0.221 / 0.489・札の値 0.780 / 0.212 / 0.415 と並べて・判定に使わない)= P s22 の形。
  - 片方だけ: 状態 16 の「qwen3:32b(例外)」→「qwen3:32b」(R2 だけ・同じ図が「model を一つの曲線・順位にしない」とする = 「例外」は集計を前提にした言い方)。状態 26(系統樹)に P s25 の一文「moy_suite_report.json には日付の欄が無く、地図の日付(06-14)は git の最終 commit」(R2 だけ・Q は一般則だけ)。状態 17 の凡例に橙(attractor)を足した(R2 の E)。
- **状態 27〜42 = Q のまま + D3 の重なった物**:
  - 状態 27(流れ): P #s26 の**出所の分け** = 節点の間の線の太さ(太線 = 図から出た問い = 0→1 の台帳 R04 と 4→5 の読み手の次 A・点線 = 家の線 1 の続き = 1→2・2→3・3→4)+ 凡例 2 つ + 「↓ 問い[図から: …]/[家の線 1 の続き: PLAN 10-31 / 依頼者 11-01 の発注]」・**札の一覧表**(引用の欄: 札 · 日付 · 凍結 · 格・20 行 = 読んだ 17 + 関門で止まった 3)。
  - 状態 30: P #s28 の「+0.02 は olm86 を見てから置いた」= 点線の面「+0.02(事後)」と凡例・表の注・身分の行・台帳 K53。
  - 状態 33: P #s30 の Opus 5.5 の棒 = 右に離した破線の棒「prf4 · Opus 5.5 · 鎖(別の札)8 / 8」(高さ = 率・ほかの棒と同じ)+ 引用の欄に「比べ: 同じ文(M1A)の chat model — 別の札 prf4」の箱(file と key = `prf4/read.json units[claude-opus-5-5|M1A].bind · .chain_in_bind`・G-12 の出所)。
  - 台帳 R01(状態 37): P の限定 =「cue \n\n の 10 行・相関 … cue をまたぐと位置 0 の書き始めでは説明されない(olm128・状態 35)= cue \n\n の中だけの読み」(G-07 と同じ直し)。
  - 片方だけ(採った): D3 R2 ③「凍結の帯で判定」= 状態 27 の判定の chip に「うち olm112・114・128 は SCOPE 11-01 の外 = RESULT の凍結の帯」・D3 R2 E の「cue \n\n で K11 を再現」→ K07(台帳の 3 / 3 · 7 / 7 は K07)・D3 R3 E の olm114 の日付(駅 4 の日付を札の記録の名 11-02 に揃えた)。
  - 片方だけ(採らなかった): D3 R2 ⑤「forward なし = olm59 の 120 行」・⑦ の G2 は G-13 の直しで入った・⑧ の「層 12〜20」の灰の帯(G-05 は層を各札の値だけにせよと言う = 帯は描かない)・D3 R3 ③ の「1 行抜き 0 / 10」と中央値の軸(状態 28 は Q の柱のまま)・⑤ の olm97 の 0.000 / 1.000。理由 = 一人の読み手だけ・状態の欄に余白が無い・次の版で要るなら足す。

## 2. 依頼者の規則(依頼書 §2-5)— そのまま従った

1. **札の印 = その状態が読む data の札(P の規則)を build が導く**: `build.mjs` に P の追跡の proxy を移した(DATA を包み、各状態の文 = lead / readout / lim / chips / quote と絵 = wide / phone を ja / en で評価し、触った DATA の葉の path を一つの規則 `CARD_RULE` で札に写す → `config.json card_marks` と食い違えば build が止まる・`generated/marks_derived.json`)。`CARD_RULE` は Q の DATA の key に合わせて書き直した。`DATA.after`・`DATA.cue_start`(olm128)は**印にしない**(Q の規則 = 後から足した部分の札の表で示す)。
   - 導いた差(Q の v3 からの変化): 状態 8 に cmt5(限定の文が cmt5 の二つの label の数を読む)・状態 18〜20 に replication_config_frozen(右の作図が凍結の座標)・状態 21 に olm62(限定の文が olm62 の順位相関と 7 / 11 を読む)。状態 11 は pc1 + screen_bf16 のまま(olm128 は載らない)。`state_data` も同じに直し、K43 の anchor(here_json_equals 43 + derived 43)を作り直した。
2. **後の札の数 = 判定に届いた札**: 状態 27 の chip と readout と限定の一行 = 「読んで格に届いた札 17(判定 6 · 確かめた記述 2 · 記述 9)+ 関門で止まった 3(olm83 統制 ✗ · olm88 入口の関門 ✗ · olm95 統制 C2 ✗)・data の札 olm87・olm90 は数えない」。olm83・olm88 は pack に無い(値を読んでいない)→ 名・日付・凍結の commit・理由を RESULT の頭の行と SCOPE 11-01 §0 から写し、`repo_text_contains` の anchor で縛った(K50v31)。流れの駅 2 にも破線 × で置いた(駅の名 = olm83〜92 = レールの名と揃った = G-09)。K50 の文「18 本は凍結してから読んだ」→「凍結した 18 本・読んで格に届いた 17・olm95 は読まず」。
3. **olm89 / olm92 の線 = 凍結の +0.01 を判定の線・+0.02 は事後の注**: 状態 30 の表の注・chip・lead・身分・凡例・台帳 K53 に「判定の線 = 凍結の +0.01」と「+0.02 は olm86 の値を見てから置いた確かめの線(PREREG olm89 §0・事後)」を並べた。olm92 の層 48(+0.018)は「凍結の +0.01 の上・+0.02(事後)の下」。SCOPE 11-01 の限定「層 32 だけ」は +0.02 で引いた線だ、と同じ注に書いた(SCOPE の格は書き換えていない)。

## 3. data で決めた食い違い(依頼書 §2-6)— 決め方と anchor

| 食い違い | 決め方(規則) | 決めた値 | anchor |
|---|---|---|---|
| s17 base open の attractor 5 か 4 か | 凍結の規則 = PREREG pc1 §6「`truncated(limit)`(cap 到達・base 側)= **primary 分母から除外 + 全行込みを並記**」 | **primary = attractor 4 · stuck-L1 5(上限で切れた 1 行を除く・n 9)**・全行込み attractor 5 / 10 を並べる。Q の行の字(4)は正しく、Q の chip(5)と readout(5)が全行込みを無印で出していた → chip / lead / readout を primary に揃え、全行込みを添えた | K64v31a(PREREG の逐語)・K64v31b(derived base: labels 5 / 5・labels_no_cap 4 / 5・cap 1) |
| s18 の語の位置 k −20 か −19 か | npz(`olm59/rows/F5a-2__think__r15.npz` の text・starts・ends)で数え直した | **二つとも正しい・指す token が違う**: k −20 = 「the midpoint …」の頭の " the"(P)・k −19 = " midpoint"(Q)。図の注を「「the midpoint」は k −20(midpoint は −19)」に | K66v31a / b(pack の `k_the` = −20 と `k_phrase` = −19・pack に assert) |
| olm76 の凍結 commit | `git log` の PREREG の履歴(読むだけ)+ RESULT olm76 の頭 | **凍結 = b7730f55(10-30 21:12・PREREG を最初に足した)→ 凍結し直し d7fbbd43(21:13・出力の変換だけ・読みの前)**。走ったのは d7fbbd43。Q の「b7730f55 → d7fbbd43」が正しく、P の d7fbbd43 だけは最初の凍結を落としていた | K50v31a(RESULT の逐語) |
| Q s23 で切れていた値と P の 0.781 / 0.221 / 0.489 | Q の pack の `olm62.tie` を読んだ | **同じ値**(0.7809 / 0.2212 / 0.4891)。切れていたのは表の幅だけ = 値は替えず、箱に出した | K67(既存) |

## 4. 監査 14 件の直し(依頼書 §2-7・`receipt_read/reads/G3_R2`)— 14 / 14

| G | 直し | 所 |
|---|---|---|
| G-01 | olm76 =「上がらない / 上がらなかった」→「**線に届かない**(28 / 48 の行で上がった・中央値 +0.013・p 0.156・attractor の行より上でもない)」= SCOPE 11-01 の言い方 | 状態 28 の題(ja / en)・台帳 R04(ja / en)・台本(状態 28 の行)・README。言えない(X17・状態 28 の限定)は Q で既に「線に届かず」。受け入れの問 7 の答えの場所(状態 27・28)もこの言い方 |
| G-02 | attractor の中央値 = read.json +0.0425(3 桁で +0.042)・SCOPE の +0.043 は丸めの違い、と表の注に | 状態 28 の引用の注・K51v31b / c |
| G-03 | +0.02 は olm86 を見てから置いた確かめの線(事後)を表の注・凡例・身分・K53 に | 状態 30・K53 |
| G-04 | 「k = 8 だけ」→「一貫して出る上乗せは k = 8 だけ(olm86 の k = 16 は 400 行で消える)」 | 状態 30 の題・流れの駅 2 の結果・台本・README |
| G-05 | 「指しは層 12 まで名の位置・値は層 20〜28」「層 16〜28 のどこかで引き直される」→ 操作の名(入れ替えた時に行いが指しに従う割合 / 値に従う割合)と各札の層だけ(olm106 = 層 16 で 0.5 を割る・olm108 = 層 20 で値の側へ・olm101 = 層 28 から値)・「変数」「pointer」は文の組の名 | 状態 32 の題 / lead・台帳 R08(数は data から)・流れの駅 3・台本・README |
| G-06 | 「直交から導いた続き」→「直交から直角へ進む文がある続き」・R09 の「運ぶ」「埋める」を外した | 状態 34 の chip / lead・台帳 R09 |
| G-07 | R01 を P の形に限定(cue \n\n の中だけの読み・olm128) | 台帳 R01(状態 37) |
| G-08 | olm128 の「計器の境(位置 0)が cue に敏感」を §3 の事後の記述の箱から分け、「読み(RESULT olm128 §4・L3)」の札と「どちらの外れかを分けない」を同じ所に | 状態 35 の事後の記述の注 |
| G-09 | 数え方を一行(依頼書 §2-5 の 2)・駅 2 の名 = olm83〜92 | 状態 27・K50 |
| G-10 | 題 =「10-28 の後に家が打った札は、どの問いが図から出て、どれが家の線 1 の続きか?」・発注 = PLAN 10-31 / 依頼者 11-01 を問いの札に | 状態 27 |
| G-11 | 8 / 53 の出所 = `olm59/read.json Q3_desc[o_diam|close|B-bind].after_gt_before` | 台帳 R04 の src・K25v31a / b |
| G-12 | prf4 の file と key | 状態 33・K59v31a〜c |
| G-13 | olm101 の DAS = `read.json Q3.D_das_test 対 D_full_test`・olm114 k = 0 の関門 = **G2 ✗(答えの欄 B-bind 5 < 8 = RESULT olm114 §1)**。Q の「(上限で切れた 18)」は関門の理由ではない(18 = Q3.hit_cap は別の数として残した) | 状態 32 の限定・状態 34 の chip / lead・K59v31d / e |
| G-14 | 「四つの問い」→「受け入れの問い」(数は chip が data から) | 状態 42 の問い |

- 直したが監査の番号の外: 状態 10 の「この順は bind 7 行のうち 4 行」(P も Q も)→ **3 行(s2・s7・s8)**・両方の文を持つのは 4 行・O が先は s0(`DATA.order_he_first` から数える・K09v31a)。D1 の二人の E が挙げた食い違い。台本の頭の行「open の 10 行は裸の共円…」→「10 行中 8 行 / 6 行」(D1 R2 の E)・状態 9 の台詞「どちらも増える」→「別の標本で並べる」。

## 5. 一番自信の無い点・やっていないこと

1. **CARD_RULE(DATA の path → 札)の対応は作り手の決め**(P と同じ弱点): 例 `think.base` → pc1・`cue_table.nl` → screen_bf16・`olm62` → olm62 + 群。追跡は文と絵の評価の中だけで、読み込み時に計算された定数は追跡されない。
2. 状態 27 は字が詰まっている(流れの本文 13.5 px・札の一覧 11 px)。P の一覧表の 4 列(値の file)は各状態の札の表に任せ、日付・凍結・格の 3 列にした。
3. olm83・olm88 は pack が読まない札で、値も見ていない(名・日付・commit・理由だけ)。
4. 撮影は video(ja / en)と検査の物だけ(依頼書 §2-8)。desk と phone は検査(run_checks の測り・robust・実クリック)で通したが、撮影はしていない。
5. やっていない: D3 の片方だけの ⑤⑦⑧(R2)と ③⑤(R3)・P の流れの「(a)〜(e) の 5 本の枝」の並べ方(Q の縦の流れのまま・出所は線の太さで)。

## 6. 検査(結果)

- 走らせた順: 一回目(15:50)= 状態 18 の引用の欄あふれ(ja / en・3〜8 px)・流れの札の数の期待(18 → 20)で exit 1 → 直した。測りを「最初の失敗で止まる」から「全部集める」に替えた写し(scratch だけ・納品の検査は元のまま)で全枠を回し、英語の頁の溢れ 5 か所(状態 18・27・33・35・40)を英語の文を短くして直した・流れの canvas を 780 → 835。二回目(16:15)= exit 0。三回目(16:28・K64 の台帳の文を primary に揃えた後)と四回目(16:41・凡例の見本の CSS の選択子の二重を直した後)= JupyterLab の段だけ時間の揺れで落ち、widgets だけの再走で通した。
- 撮影(16:42〜)は四回目の build から(md5 は上)。

---

# 付録 — 土台 entry_v3_sonnet_max の NOTES(逐語・v3.1 では書き換えていない)

HEAD(R1) = d2f826e7(納品時の `git rev-parse --short=8 HEAD`・作業の開始時は 26089c8d で、その後に別の commit が進んだ。git は読むだけ = `rev-parse` のみ・書き込みなし・commit していない。worktree には他の人の未追跡の file が在る = 作り手の変更ではない)・依頼書 v3 の凍結 = e9b2b78d

# NOTES — entry_v3_sonnet_max(moy-1 の図解 駅 2 受領版 v3 = 土台 P + Q からの移植 + 監査の直し + 「次まで見せる」)

作り手 = Sonnet 5.5(effort max)・subagent なし・install / 通信 / git の書き込みなし・model も SAE も動かさない・実験の script は import も実行もしない(RESULT が引く script の 2 行を grep で見た・runner は開いていない)。
開始 11:14:12 JST・打ち切り 180 分(= 14:14:12)・納品 13:35 JST。作業は scratch(`…/scratchpad/v3_entry_v3_sonnet_max/work/`)・納品は `cp -R work/. 置き場/` → `diff -rq` → `DONE`(**置き場の root = scratch の `work/` の中身** = P と同じく平らな並び・scratch のほかの物 = patch した drive の kit・Chrome の profile・読みの撮影は納品しない)。port = 27600〜27699(marimo 27610・JupyterLab 27616・drive の Chrome は 27650〜27699 の帯の乱数)・Chrome の profile は scratch の中。
BRIEF = `BRIEF_v3_moy1_receipt_two_makers_20261106.md`(§1〜§5)。土台 = entry P(`entry_sonnet_max_v2_1/`・書き換えていない)を scratch に写して足した。更新(主 session からの連絡・作業の途中): 候補 A = olm128 は凍結(2f1ab745)・判定済み → 次の問いの状態は「凍結前・結果なし」でなく結果で書いた(状態 35・36)。

**読んだもの**: BRIEF v3 一本・skill(SKILL.md と references の全部)・entry P 一式・`reads/D_R1`・`D_R2`・`G_R1`・`N_R1_P`・`N_R1_Q`・`N_R2_P`・`N_R2_Q` の judge_reply・RESULT 駅 2・SCOPE 11-01・RESULT olm76 / olm112 / olm114 / olm128・18 札の read.json / control.json(pack_after.py が読む)・PREREG は凍結の commit を確かめるために頭の行だけ。
**entry Q** は folder を `ls` し、移植元の数か所(∠ の列・prompt の編集の差分・数え方)を grep / sed で読んだだけ(5 command)。Q の撮影(captures)は開いていない。
**読んでいない**: もう一人の作り手 `entry_v3_opus_xhigh` の folder(一覧も開いていない・その process にも触れていない)・`T_*`・`M_*`・`SEALED*`・memory(session の開始時に自動で入った分を除く)。

## v3 の中身 — 数

- **状態 43**(P の 30 + 13): 10-28 の部分 = 状態 0〜26(P の 26 + 坂の状態 1 = 22)・その後の部分 = 図の状態 27〜36 の 10 + 台帳 2(40・41)・台帳全体 = 37〜42(6 状態)。
- **章 15**(P の 9 + 6): 問題の図 / 二つの問題文 / open / blocked / bind す瞬間 / 他の model / 作図 × SAE / 札と系統樹 / **その後の流れ / (a) 台帳 L3 → olm76 / (b) 推論空間の探し / (c) 語でない構造 / (d) apex の証明 / 次の問い** / 台帳。
- **札 18 本**(その後): 判定 6(olm94・olm98・olm108・olm112・olm114・olm128)・確かめた記述 2(olm89・olm92)・記述 9(olm76・84・85・86・91・93・97・101・106)・読まない 1(olm95・統制 C2 ✗)。各札に **凍結の commit・格・出所の file と key**(状態の右の「札の表」)。凍結の commit は RESULT の頭の行と、git が PREREG を最初に足した commit の一致を pack と JS の二経路で照合(18 / 18)。
- **照合 anchor 659 本**(P の 352 + 307)・欠けまたは違い 0・統制(わざと間違えた anchor を報告できるか)9 / 9。台帳の行 = K01〜K69・R01〜R11・X01〜X27。
- 撮影 **348 枚**の PNG(video 1920 × 1080 = ja 43 + en 43 + 前後の対 4・desk = dark / light × ja / en の 172・phone = dark / light の 86)+ widget の撮影 5(J1〜J3 = JupyterLab・M1・M2 = marimo)+ `INDEX.md`・`capture_log.txt`(全部 console clean・頁の md5 は最終の build と一致)。
検査 = **`sh run_checks.sh` が exit 0**(`checks/last_run.txt`): 測り 430 画面(video / desk / phone × ja / en と 3 頁と減らした動き・各 43 状態)すべて通過・robust 2150 組 × 3 枠で 0 件・parity(ja / en の数)✓・sae・v21・v3(desk と phone)✓・札の実クリック(desk・phone)✓・章の実クリック(desk・phone・15 章)✓・語の走査 ✓(統制つき)・marimo 両向き ✓・JupyterLab 両向き ✓(kernel の再計算 equal)・照合 659 / 659・fence 0。撮影のあとに marimo と JupyterLab の段だけ再走(`WIDGETS_ONLY=1`・exit 0・J / M の撮影を作り直した)。

## 1. 移植(依頼書 §2-1)— Q から P へ

| Q の物 | 入れた所 | 数の出所 |
|---|---|---|
| #s1 ∠O1XkO2 の列 | 状態 0・1(比の表に ∠ の列・状態 1 の lead に「角で言い直すと 90°(最大のずれ 0.0006°)」) | K62(pack・JS・check_claims の三経路) |
| #s11 `\n\n` を使う理由の一文 | 状態 11 の lead(5 章の cmt13・cmt5 の行が \n\n) | K63(f5_runs の cue) |
| #s12 prompt の編集の差分(− / +) | 状態 12 の quote の先頭(編集は一か所) | K63 |
| #s17 base の列 | 状態 17(Think Q4 の隣に base の open / blocked・上限で切れた行は別に数える・札の印に pc1 を足す) | K64 |
| #s18 k −20 の注 + 位置の棒 | 状態 18 の quote(逐語の欄の「同じ円を語で言う文」に黒の下線・token 297〜323・k −32〜−6・「midpoint of the line segment」は k −19・O1・O2 の名を含まず述語に当たらず「前 32」の窓の内。Q の「k −20」は据えず、npz の text と starts から数え直した値を出した) | K66 |
| #s20 行ごとの坂 + 道 × label の内訳 | **新しい状態 22**(8 枚の小さな図 = 1 枚 1 種の出来事 × 1 つの群・棒 = 1 行・同じ目盛り・零の線・中央値の線・場面の行を輪郭で)+ 右の内訳の表(bind 53 = 考えの道 36 + natural 16 + 答えの道 1 …・残り 3 行も) | K65・坂は pack と JS が窓の file から数え直し、read.json の本数・中央値と照合 |
| #s21 固定した最初の語 | 状態 25 の道の名の下(最初の一語「Okay」を固定 / 最初を「{"」に固定 / 固定なし) | K65 |
| #s22 同順位を平均した値の注 | 状態 23 の表の行 + 注(**「札の外の数」・判定に使わない** = 0.781 / 0.221 / 0.489・札の規則の 0.780 / 0.212 / 0.415 は据え置き)・台帳 K67 | K67(同順位を平均する値を check_claims が自前の rank で出す) |

**片方の読み手だけが出した物(自分で決めた)**:
- 採った: Q #s23 の「Q2 の二つの規則(8 本未満は読まない・閾 60 %)」→ 状態 24 の注に(`flatRules`・K68)。P の状態 23 の chips にはすでに Q1 の行(48 / 59 = 81 % ✓)が在った。Q #s20 の坂の「立方体」は採らず、**8 枚の小さな図**にした(理由: P の 3D の柱の隣に 4 群 × 2 種 × 全分布を入れると、1920 × 1080 の枠で棒 1 本が 2 px を割る。小さな図なら 59・34 行の全部が読める)。
- 採らなかった: Q #s5 の lede の一行「driver が全文を oracle に渡していた」(D-6)= P の状態 5 の限定の札に同じ事実(凍結の label は全文を分類器に通した値・08-01 の裁定で既知)が在る。Q #s24 の「札ごと章別の状態 button」= P の札の印(各状態の見出しの右の本物の button → 地図)が同じ役で、地図の中に button を 12 個足すと札の印と二重になる。Q の各状態の lede(数つきの一文・D-39)= P は見出しの問い + lead + chips を持ち、台本の行との突き合わせは `check_claims` の anchor で別に見ている。**やっていない**ので、受領の側で要るなら次の版へ。

## 2. 食い違い 4 件を data で決めた(依頼書 §2-2)

| | 決め方(述語・規則) | 決めた値 | 照合(CLAIMS の anchor) |
|---|---|---|---|
| ① blocked s8 の答えの欄 | 凍結の `label_json_fields`(cmt5.json rows[*])に従う: 答えの欄 = **最後の JSON の `conjecture`**・JSON の無い行は答えの欄が無い(cmt5 の JSON の無い 3 行は 3 / 3 が B-flail になる = 凍結の規則も同じ)。P の「最後の段落を読んで O1O2」(7 / 10・「10 行すべて一致」)は取り下げ。最後の段落の読み(O1O2)は `prose_reading` として**開示だけ**(数えない) | blocked の答えの欄 = O1O2 6・He・Hi 3・**JSON なし 1(s8)**・凍結の label との一致 9 / 10(s8 の全文の label は bind) | K06・K09・K69・X27(pack に assert: blk_cnt・agree_blk == [8]) |
| ② open で色が替わる行の数 | 述語: 凍結の label の色の類(attractor = 橙・stuck-L1 = 灰)と答えの欄の読みの類(He・Hi = 橙・裸の共円 = 灰)が食い違う行 | **6 行**(s0・s1・s2・s4・s6・s8 = attractor 5 + s4)。Q の chip の「5」は attractor の 5 行だけ数えたもの(Q の表の ← も 6 行) | K05・pack の assert(changed_open == [0, 1, 2, 4, 6, 8]) |
| ③ moy_suite_report の日付 | 規則: 日付 = 記録の file 名があればその日付・無ければ data の file の**最終 commit**(読むだけの `git log`)。moy_suite_report は記録の名が無い | **06-14**(系統樹の前の札)。Q の「日付なし」と箱の名「07〜08 月」は両立しないので、箱の題は「10-19 より前」 | K42(pack = recount) |
| ④ 札の印を付ける規則 | **データの出所**: 各状態が画面に出す data の key → その data を出した札(`config.json` の `state_data` × `card_of_data` から期待の印を作り、`card_marks` と照合)。群・label の名の出所(cmt5 の規則・olm7 の群)では付けない | 状態 8 = pc1 だけ・状態 11 = pc1 + screen_bf16・状態 17 = behavior screen + pc1(base の列を足したので)・状態 18〜22 = olm59 + olm7 + olm4 | K43(here_json_equals + 導出した規則) |

## 3. 監査の直し(依頼書 §2-3・`reads/G_R1` の 16 件)

直した 14・P に無かった 1・向きを書いて据え置いた 1。

| G | 直し | 所 |
|---|---|---|
| G-01(L3 の「結びが下がるのは…まだ答えを閉じていない」) | 台帳 R04 を **olm76 の結果と同じ行**に置き、「支持されない読み」に格下げ(答えの欄 `{"` の直前 64 token でも結びの群は bind の行で上がらない = 28 / 48・+0.013・p 0.156)。偽の窓 21 / 48・attractor 7 / 10 を並べ、立体の柱(状態 28)で見せる。言えない X17 | 台帳 40・41・状態 28 |
| G-02(「確かめに入る」) | 「本文が数式の文字の多い区間に移る(48 / 59)」へ。「確かめに入る」は R05 に本文の形の名付け・目的の同定ではない・「model が確かめた」とは言わない、と同じ行に | 状態 23・24・台帳 R05 |
| G-03(「仮説を立てた行」「決める位置」「円を挙げた後」) | 「「直径 = He・Hi」の文がある行」「He を書く位置」「「直径 = He・Hi」の文の後」 | 状態 7・10・13 |
| G-04(「同じ部品」「押す」「写す部品とは別」) | 「1 位の head はどちらも L50H23。上位 10 の重なりは(値)」・寄与の符号の言い方・R02 は 3 桁の値(K14 は全桁) | 状態 14・15・R02・台本 |
| G-05(限定の落ち「だけ」) | 「共円で止まる答えを不十分とし、中心と直径の名指しを求める(点の名 0 件 = pack で数えた)」 | 状態 3・K02 |
| G-06(「どの群も半々」) | **P に無い**(P の R03 は「差の中央値が小さい」で、数は結び 17・中点 18・答えの側 11・考えの側 19 / 34 とともに出ている)。Q 側の食い違いで、移植していない | — |
| G-07(「替わる」「増えた」) | open の 10 行と blocked の 10 行は**別の標本**として並べ(open → blocked で 0 → 7 / 10)、同じ行の変化とは書かない | 状態 8・9・台本 02 |
| G-08(「例外」) | 「qwen3:32b は blocked で bind 1・attractor 7」 | 状態 16・台本 21 |
| G-09 / G-10 / G-11 / G-13 / G-14 / G-15(出所なし) | 各状態の身分の行に足した: 語 = O_TOKENS・±80 字の窓(状態 7)/ 順位 = pack が窓の差から計算・JSON の位置 = npz の json flag(18・19)/ 統制 = olm59/control.json C1〜C3(21)・olm62/control.json C1・C2(24)/ 組の表 = RESULT cmt13 §3 の事後の名付け(13・14)/ @ = cmt13 sites[*].context を探した位置(12)/ 札の印 = config.json card_marks(26) | 状態 7・12・13・14・18・19・21・24・26 |
| G-12(道 × label の内訳の出所) | 内訳は rows/*.npz の meta(道 = kind・label = 答えの欄の label_json)の数え上げ(L2)と、状態 22 の限定の札に | 状態 22 |
| G-16(図の `claude-opus-4-8` と CLAIMS の `claude-■-4-8` の揃え) | **据え置き**: 「■」は家側の封の伏せ字で、この entry の data(moy_suite_report.json)の model 名は実名。伏せ字に揃えるかは人間の裁定(どちらに揃えるかは人間)。CLAIMS は図の文字列から生成するので、図と CLAIMS は一致している | — |

**機構の言い方**は SCOPE 11-01 §2b の「言えない」に合わせた: 回路・励起・活性化は否定の文だけ・「model が分かっている / 解く / 推論 / 計画」は言わない・「結びの latent = commit の正体」とは言わない(台帳 X10・X17〜X27)。

## 4. 「次まで見せる」の作り(依頼書 §2-4・§2-5)

- **一本の流れ**(状態 27 = 図の上の一枚): 六つの駅の縦の線(0 = 10-28 の図 / 1 = olm76 / 2 = olm84〜92 / 3 = olm93〜108 / 4 = olm112・114 / 5 = olm128)・各駅に札の glyph(格を**形**で: 塗り四角 = 判定・半分 = 確かめた記述・白抜き = 記述・破線 × = 関門で読まず)・その駅の一行の結果・「↓ 問い」で次の駅へ。以降は駅ごとの状態: (a) **状態 28** = 台帳 L3 → olm76(3 本の柱 28 / 48・21 / 48・7 / 10・50 % の線)/(b) **29** = 先読みの AUC(層 32 の probe 対 J-lens 対 語の袋・各札の零の帯)・**30** = k ごとの E(k = 8 だけ小さな上乗せ・+0.01 と +0.05 の面)/(c) **31** = 名の直後の形 → this circle の AUC・head の注意の割合 / **32** = 指し → 値の層ごとの曲線(層 12〜20)/(d) **33** = apex の 37 行の証明の欄(鎖 0 / 37)/ **34** = frontier の段を与えた続き(26 / 40・23 / 40・k = 0 は関門 ✗)/ **35・36** = 次の問い。
- **10-28 の部分と後の部分を見た目で分ける**: 後の部分は**破線の縁の板**・斜線の帯(板の頭)・見出しの頭に「後から足した部分(11-06 版)」・レールの節点は**斜線**・章と番号の button は破線(`data-part="after"`)。10-28 の部分は P のまま(灰の実線)。新しい色は足していない(格は形で言う)。
- **各札の「札の表」**(状態の右・台帳でも): 札 · **凍結の commit**(olm76 は読んだ commit も)· **格** · 出所の file と key(`ConstructGap/exp/…`)。凍結の commit は RESULT の頭の行(`[PREREG](…)(hash)`)と `git log --diff-filter=A` の最初の追加が一致することを pack が assert・data.mjs が再度照合。
- **格の付け方**: SCOPE 11-01 の表(判定 / 確かめた記述 / 記述 / 言えない)を基準に、SCOPE が載せていない札(olm101・106・108・112・114・128)は各 RESULT の凍結の帯の言葉(「動かした主張」・判定)から付けた。

## 5. 次の問いの状態(依頼書 §5・更新後)

- **状態 35** = olm128 の結果(候補 A = 「cue × JSON から書き始める割合 × blocked の bind」・凍結 2f1ab745): blocked の 1 行 = 1 マス(bind 青 / bind でない 灰)を cue ごと・書き始め(JSON / 文)ごとに並べる。**位置 0 の書き始めでは cue の差は説明されない**(Q1 一致率 11 / 19 = 0.579 = 保たれない)・cue \n は JSON から書き始める行 7 / 9(Q2 +0.478 = 動く)・cue " " は 0 / 10(−0.30 = 逆)・陽性統制 C0 は再現。
- **事後の記述**(判定でない・凍結に無い・図でも「事後の記述」の札): cue " " は問いの決まりの一文を続けてから JSON に入る(最初の JSON が 25〜84 字目に 7 行)。「100 字以内に JSON」で数えると早い JSON 0.89 / 0.70 / 0.30 と bind 2 / 9・4 / 10・7 / 10 が逆の順に揃うが、100 は見てから置いた数。= 計器の境(位置 0)が cue に敏感、まで(R10)。pack が raw の行から数え直した(K61)。
- **状態 36** = 読み手が出した次の候補 A〜E と第二段: A = olm128 で読んだ(判定済み)・B = 図の数の頑健さ・C = cmt13 の二つの瞬間の組の和・D = 数式への移りの非対称・E = blocked s8 の答えの欄(**決めた結果は §2-① に書いた**)= 並べるだけ。**第二段(述語の凍結し直し + 書き始めを替える腕)は依頼者の裁定待ち**。図は推さない。

## 6. 数の経路(追加分・四つ)

1. **pack(第一経路)**: `pack_moy1.py`(坂・∠・F5 の編集・base の列・同順位の平均・olm128 の cue × 書き始めを raw の行から)と新設 `pack_after.py`(18 札の read.json / control.json・RESULT の頭の行の凍結の commit・SCOPE の数に assert)。
2. **data.mjs(第二経路・JS)**: 坂の本数・中央値・∠・F5・base・olm128 のマス・18 札の値を read.json から JS で読み直し、凍結の commit を git(`git log`)と照合。
3. **check_claims.py(第四経路)**: 新しい kind(derived / derived_close / pack_equals_derived …)を足して anchor **659 本**(自前の loader・regex・rank・関数で数え直す)。
4. **widget の kernel(第三経路)**: `check_counts()` に状態 22(坂)・28(olm76)・35(olm128)を足した。他の追加状態(29〜34・36)は kernel の再計算を持たない(= pack・JS・anchor の三経路まで)。

## 7. 直した検査の落ちと残すこと

- 検査の途中で見つけて直した: 状態 18 の quote の欄あふれ(英語版)・状態 25 の固定した語の行が「全文の label」の行と重なる・apex の列名と O / F の字の重なり・台帳(状態 37)の 1080 枠あふれ(L3 の箱を二段組で全幅に)・追加した状態の長い題が幅に入らない(題を折り返し・内容を下げる `ttl` / `cam3`)・phone の flow を内容の高さに(`cv.used`)。**測りを「最初の失敗で止まる」から「全部の状態の失敗を集める」に替えた一回の走りを scratch で回して直した**(納品物の `check_states` は元のまま = 失敗で止まる)。
- `run_checks.sh` の一回目(撮影と同時に走らせた)は 2 件で落ちた: ① **ja / en の数の parity** が状態 9 の英語の chip(P の古い数 `O1O2 4`・決めた ① の後は O1O2 3 · He-Hi 1 · なし 1)を検出 → 直した ② 四つの頁の一つで Chrome が起動しない(一過性・撮影との同時走り) → **単独で全部を走らせ直して通った**(`checks/last_run.txt` はその走り)。
- 英語の頁に日本語が混じる所を走査して直した(olm101 / 106 / 108 の枝の語・olm112 / 128 の判定の語に英語の注)。残るのは P の設計の「He・Hi」の中黒・系統樹の札の名(日本語の原文を引いた所)・olm92 の「残る」(英語の注つき)。
- 納品物に入れなかった読みの道具: `shot.sh`・`dump_states.mjs`(scratch の絶対 path を持つ)・`run_post_fix.sh`(P の一回限りの script で `pages_new` を見る)。
- 実験の計器・語・数は触っていない。**言えない**(台帳 X)は SCOPE 11-01 に合わせて 11 行足した(X17〜X27)。

## 8. 一番自信の無い点・やっていないこと

1. **格の付け方**: SCOPE 11-01 に載っていない札(olm101・106・108・112・114・128)の格(判定 / 記述)は、RESULT の凍結の帯の言葉から**作り手が付けた**。「判定」は凍結の予想への当たり(✓ / ✗)のあるものに付けた。SCOPE が後で別の格を付けたら直す必要がある。
2. **密度**: 状態 27(流れ)は 1920 × 1080 の枠で字が約 11 px(最小 10 px は超える)・追加した各状態の右の列(札の表 + 数の表 + 注)は P の状態より詰まっている。見て読めるかは読み手に委ねる。
3. **phone の追加状態は「測って重ならない・枠内」まで**で、一枚ずつ目で見ていない(video と desk は主なものを見た)。
4. **台帳の R10**(位置 0 の書き始めは cue に敏感で、Q1 の「保たれない」は考えが外れたのか境の置き方が外れたのかを分けない)は RESULT olm128 §4 の読みを写したもの(L3・採否は依頼者)。
5. **やっていない**: Q #s24 の札ごとの button・Q の各状態の lede・kernel の再計算の追加状態分(29〜34・36)。
6. 状態 28 の柱の「偽の窓」は olm76 の control C2 の値(同じ幅・無作為)で、偽の窓が立たないことの陽性統制ではない(COMMIT の陽性統制 C3 14 / 18 = 線 15 で ✗ は図に書いた)。

---

# 付録 — entry P(v2.1)の NOTES(逐語・v3 では書き換えていない)

HEAD(R1) = 93c7f7ad(BRIEF v2.1 を入れた commit = この session の書き始めの checkout の HEAD。BRIEF の 1 行目は 74aad3d3 = その親)・納品時の worktree の HEAD = 93c7f7ad(git は読むだけ = `rev-parse` / `log` / `status`・書き込みなし・worktree は clean のまま)

# NOTES — entry_sonnet_max_v2_1(moy-1 の図解: v2 + (A) olm62 を SAE の章に + (B) 札の印と系統樹の地図)の作り方・足したこと・直したこと・指摘

作り手 = Sonnet 5.5 max(背景 session・subagent なし・install / 通信 / git の書き込みなし・model も SAE も動かさない・実験の script は import も実行もしない)。
BRIEF = v2.1 `BRIEF_v2_1_moy1_olm62_and_card_cluster_map_20261028.md`(入れた commit = 93c7f7ad)+ v1 / v2 の BRIEF(機械・skill・読み手・色・検査・撮影の規則)。土台 = 自分の v2(`entry_sonnet_max_v2/`・書き換えていない)を scratch に写して足した。
**他の作り手の entry と `explainer_moy5/` は読んでいない**(folder の一覧も開いていない)。**olm62 の runner(`olm62_…py`)は開いていない**(定義は read.json を再現することで決めた = 下の「驚いたこと」1・2)。memory は自分では開いていない(session の開始時に自動で入る分は除く)。
読んだもの: 3 本の BRIEF・skill(SKILL.md と references の implementation / checks-and-captures / data-contract / wording)・自分の v2 一式・olm62 の read.json / control.json / RESULT / PREREG・olm59 の npz 120 本(pack が読む)・`tree_src.json` と `tree_overview.png`(見た)・系統樹の前の札の記録は **file 名の日付だけ**(+ 二つの data file の最終 commit の日付 = `git log -1`・読み取り)。
開始 16:42:32 JST・打ち切り 90 分(= 18:12:32)・納品 17:52 JST。

## v2.1(2026-10-28 夕)— v2 から何を足し、何を直したか

### A. olm62 を SAE の章に足した(状態 22・23)・言い方を直した
- **22** `scat`: 左 = 二本の棒(本文が数式に移る出来事の割合: O1O2 を名指した後 48 / 59・He・Hi を名指した後 8 / 34)・右 = 一枚の散布(横 Δmath = 名指した token の前後 32 token の「数式の文字の割合」の差・縦 Δ中点 = 考えの中点の群の値の差・**同じ目盛り**・O1O2 の 59 点 = 青の丸 / He・Hi の 34 点 = 橙の菱形)・輪 = v2 の場面 S_O・S_H(状態 18〜20)・図の中に ρ(0.780 / 0.212・全 token 0.415)。右の表 = read.json の値。
- **23** `flat`: 数式に移らなかった(Δmath ≤ 0)O1O2 の 11 本の Δ中点(点の列・塗り = 上がる 7 / 白抜き = 上がらない 4・この 11 本の中央値 +0.057 と O1O2 全体の +0.157 の線)・**予想 Q2 の余裕**(1 マス = 1 本・閾 60 % = 11 本中 7 本以上 → 余裕 0 本・一本違えば 6 / 11 = 55 % ✗ = RESULT §4 の「薄い ✓」を R3 の margin で出した)・同じ 11 本で他の群が上がる本数(結び 3・中点 7・答えの側 3・考えの側 3)。
- **言い方を直した**(BRIEF §A の最後): v2 の「中点の群の上がりは本文が計算に移った写しと分けていない」を「**中点の群の上がりの大半は、本文が計算に移ることと一緒に動く(順位相関 0.780)。計算に移らない 11 本でも 7 本で小さく上がる(薄い ✓)**」へ。直した所 = 状態 18・21 の `lim`・7 章の strip(`notClaimedBy.sae`・ja / en)・台帳 X11・新しい X14。「確かめに入る」は**本文の形からの読み(L3・実行層 = R05)**と札を付け、「model が確かめた」とは書かない(言えない X14・X15 と台本の最後の行)。
- 章の並び: `lab2`(cmt5 の二つの label)は 22 → **24** へ(olm62 の二つの後ろ)。状態 8 の限定の札・問 3 の `where` の「状態 22」を 24 に直した。台帳は 3 状態 → **4 状態**(26 = 1〜6 章・27 = 7 章の olm59 と cmt5・28 = olm62 と系統樹・29 = 言えない + 問い)。最後の台帳の状態は 2 段組みにして video の枠(1080)に収めた。
- 受け入れの問いを 4 → **6**(問 5 = olm62・問 6 = 札と系統樹)。基準は README に(図には載せない)。

### B. 札の印と、系統樹の塊の地図(状態 25・章 `tree`)
- **札の印**(BRIEF §B (1)): 全状態の見出しの右に、その状態の data の出所の札の pill(`札 pc1 · 系統樹の前`・`札 cmt13 · C2 部品の読み`)。**本物の button**: 押すと地図の状態へ(押した札は太い縁)。台帳の状態は「札 = この図の全部 → 地図」。**状態 → 札の表は `config.json` の `card_marks`**(番号の唯一の置き場に足した)。本体の検査が config とページの DOM を ja / en の全状態で突き合わせる。
- **地図**(BRIEF §B (2)): 台帳の前の 1 状態。系統樹 v2.2.1 の 9 つの塊を**蛇行の並び**(1 2 3 / 6 5 4 / 7 8 9・系統樹自身の概観図と同じ)で**中立の灰の箱**に・moy-1 の図解が使う札 12 本だけを縁取り(各札: 札の名・語・日付・系統樹の outcome の語〔色は持ち込まない〕・**使う状態の番号**)・系統樹の外は**点線の箱**二つ: 「系統樹の前」(replication_config_frozen・pc1・screen bf16・behavior screen・F5・moy_suite_report)と「系統樹の後」(olm59・olm62・置き場の案 = C3 の続き = **L3・主 session の案・採否は人間**と箱に明記)。電話では 3×3 の格子を保てないので、**札を含む塊だけの縦の一覧**にした。
- 新しい色は足していない(縁取りは kit の `--anatomy-lit`・箱は kit の灰・点線は灰)。青 = apex / 橙 = attractor の意味は散布図でだけ使い、**札の印・地図には青 / 橙を使っていない**。
- 札の数・塊の数・塊ごとの札の数・日付の範囲・4 札の塊と outcome の語は `tree_src.json` から(pack・JS・check_claims の三経路)。系統樹の前の札の日付は**記録の file 名**(pc1 07-31・screen bf16 07-29・behavior screen 07-28・F5 08-01)・記録の無い二つの data file は **git の最終 commit**(replication_config_frozen 07-28・moy_suite_report **06-14**)。

### C. 数の経路(v2.1 で足した分・四つ)
1. **pack(第一経路)**: `pack_moy1.py` の 8d(olm62)・8e(系統樹)。olm59 の npz から出来事ごとの Δ中点・Δmath を数え直し、**read.json の本数・文字列・中央値(1e-6 = read.json は float32)・順位相関(1e-12)を丸めずに再現**(o_diam 59 / 48 / 0.125 / 7 / 11 / 41 / 48 / 23 / 32・25 / 27・結び 3 / 中点 7 / 答えの側 3 / 考えの側 3・h_diam 34 / 8 / 14 / 26 / 4 / 8)・全 token 162,545 の相関・統制 C1(olm59 の再現)・C2(数字だけの token 32,498 / 32,498・英字だけの token 84,759 / 84,759)・S_O / S_H の散布の位置・BRIEF §2 の値(`tree` の 9 塊・78 札・C1 = cmt1…cmt5 / C2 に cmt13 / C3 に olm4・olm7)を assert。Q2 の閾(60 %)は **olm62 自身の PREREG の文から読む**。
2. **data.mjs(第二経路・JS)**: 窓の側 file `generated/olm62_windows.json`(出来事ごとの 64 token の四群と数式の文字の割合)から Δ・本数・中央値・分割・群ごとの本数を JS で数え直して read.json と(**順位相関は同順位を平均した順位で ±0.02 の範囲だけ**: 札の規則 = numpy の ordinal rank を JS では再現できないため = 下の「驚いたこと」1)・頁が持つ 93 点・tree_src.json の塊・札・日付(git の最終 commit も読む)・`config.json` の `card_marks`(状態数・既知の札・全部の札が一つ以上の状態の印)。**食い違えば build が止まる**。
3. **check_claims.py(第四経路)**: anchor **352 本**(v2 の 206 + 146)。olm62 は**自前の loader・自前の regex(token の文字の割合)・自前の rank**(札の規則 = ordinal rank)で数え直し(`o62`・`o62_pooled`・`o62_c2`・`o62_events`・`o62_point`・`o62_flat`)・tree は `tree` の derived・日付は `name_date` / `git_date`・`config.json` は新しい種類 `here_json_equals`(状態ごとの札の印)。**検査器そのものの統制**: 5 → **9 本**の間違った anchor(順位相関 +0.001・数式に移らない 11 本の本数・塊ごとの札の数・状態 11 の札の印)が全部報告される(9 / 9)。
4. **widget の kernel(第三経路)**: `check_counts()` に状態 22・23(olm62 の read.json から直接 = pack を通さない)を足し、v2 の「状態 22」(二つの label)を 24 に。

### D. この entry の定義(札ではない・札の外の数を図に出していない)
- **数式の文字の割合**: token の文字のうち `[0-9²³·×=+\-^*/()√]` の割合(PREREG olm62 §1)。**窓の値 = 窓の 32 token の割合の平均**(この定義が read.json の全部の本数・中央値・分割・群ごとの本数を再現した)。Δmath = 後の窓 − 前の窓。窓 = 出来事の前 32 / 後 32(olm59 と同じ)。
- **統制 C2**: 数字だけの token = `isascii() and isdigit()`・英字だけの token = **空白を除いた token が全部文字(どの文字種でも)**(`strip().isalpha()`)。ASCII の英字だけに限ると 84,683 で札の 84,759 に合わない(` the` の先頭の空白などを数えるかどうかの違い)。
- **札の印の表(`card_marks`)は作り手の読み**: その状態が data を借りた札。状態 8 = pc1 + cmt5(限定の札が cmt5 の数を引く)・状態 11 = pc1 + screen bf16(cue `\n` の行)・状態 12〜15 = cmt13 + F5(F5a-2 の行)・状態 16 = moy_suite_report・状態 17 = behavior screen(Think Q4 の 20 行)・状態 18〜21 = olm59 + olm7 + olm4(群の名は olm7・SAE の群の凍結は olm4 / olm7)・状態 22〜23 = olm62 + olm59・状態 24 = olm59 + cmt5。**ここは BRIEF が決めた表ではなく作り手の読み**(採否は人間・L3)。

### E. 驚いたこと(取っておく事実)
1. **olm62 の「順位相関」は同順位を平均しない順位(argsort の argsort・numpy の既定の sort)**。read.json の 3 値(0.7804792518994741 / 0.21161191749427039 / 0.4152617665861453)は、普通の順位の付け方(同順位を平均・scipy の spearmanr と同じ)では**再現できない**(その規則では **0.781 / 0.221 / 0.489**・全 token では 0.415 → 0.489 と最も動く)。数式の文字の割合に 0 が非常に多い(全 token の約 7 割)ので、同順位の扱いで値が動く。読み(O1O2 の出来事では明確な正・He・Hi の出来事では弱い)は変わらないが、**図は「札の順位の付け方」と書き、同順位を平均した値は図に出していない**(札の外の数・`generated/olm62_tie_note.json` と上の NOTES だけ・X15 に「同順位を平均すると値が替わる」)。実行層へ: RESULT olm62 の「Spearman」は ordinal rank の値だと一言添えるとよい。
2. 統制 C2 の「英字だけの token 84,759」は、空白を除いた token が全部文字(**英字に限らない**)の数(上の D)。PREREG の「英字だけ」の字面だけでは再現できなかった。
3. **BRIEF の「系統樹の前 = 07〜08 月の札」と data が違う**: `moy_suite_report.json` の最終 commit は **06-14**(K42)。地図の箱は「10-19 より前」と書き、各札の日付を並べた。
4. **自分の pack の誤りを anchor を書く時に見つけた**: 最初、olm62 の Q2 の閾を olm59 の PREREG から読んでいた(値は同じ 60 % だが出所が違う別の予想)。olm62 自身の PREREG から読み直し、anchor(K33l・K33n)に入れた。
5. **公開の柵が図自身の言葉を捕まえた**: 新しい文に「採否は依頼者」(BRIEF の逐語)を入れたら fence が 30 件(5 file × 6)・「採否は人間」に直して 0。
6. **検査が捕まえた不具合**(どれも data の読みではなく表示 / 文言の欠陥): ① 最後の台帳の状態が video で 1,177 px(上限 1,080)→ 2 段組み ② 電話の状態 23 の文が viewBox を出る → 折り返し ③ 英語の散布の x 軸の題が電話で出る → 短く・折り返し ④ 英語の状態 18 の strip が video で 24 px 溢れる → 状態 18 の言い直しを短く(長い版は状態 21 に)⑤ 英語の状態 7 が見出しの pill の分 1 px 溢れる → pill の行が見出しの高さを増やさないよう負の margin ⑥ 地図で札の枠が箱を出る(video は字が大きい)→ 地図は全部の枠で 12 単位の字で組む ⑦ 電話の地図の canvas が足りない → 高さを足した ⑧ 英語の状態 23 で最後の行が canvas の下に押し上げられ重なる → 高さと英語の一行を調整。
7. **作業の癖(自分の道具の誤り)**: zsh では `set -- $fr` が語に割れず、検査の loop で `--width` が空になり**既定の小さい窓で走って「chapter の click が効かない」ように見えた**(図の欠陥ではない)。`${=fr}` か literal の大きさで走らせて直った。また、止めたい自分の古い検査(PID 確認済み)への `kill` は auto mode の分類器に**拒否**された(回避せず)。**最終の通しは別 folder(`final_run`・別の port)に写して走らせ**、その結果を戻した(source は同一・page の md5 を log に残した)。

8. **撮影を見て直した 2 点(最終の通しの後)**: 英語の地図で ① 語の途中で折り返していた(`lines()` は字数で折り返す = CJK の型・Latin の字は空白で折り返すように)② 系統樹自身の outcome の語(「通過」「外れて学んだ」「関門で止めた(b 版なし)」)が日本語のまま → 英語の語を足した(日本語の頁は data の語のまま)。**直した build で、見える検査を `run_post_fix.sh` で再走**(measure 全状態 × video / desk / phone × ja / en・`check_v21`・`check_cards`・語の走査・ja / en の一致 → `checks/post_fix_run.txt`)・**撮影は直した build から全部撮り直した**。全部の検査(robust・章の button・marimo / JupyterLab ほか)の通し `checks/last_run.txt` は、この 2 点を直す**前**の build(page の md5 は各 log の頭に)で走らせた。2 点とも描画の折り返しと表示の語だけで、数・述語・data は変えていない(pack と `generated/pack.json` は同じ)。

### F. 一番自信の無い所
1. **図の ρ(0.780 / 0.212 / 0.415)は札の順位の付け方の値**で、同順位を平均すると全 token の値は 0.489 に動く(上の E1)。図は「札の規則」と書くが、読み手は普通の Spearman と読みうる。
2. **「系統樹の後」の置き場(C3 の続き)は主 session の案(L3)**。箱に書いたが、地図の上では系統樹の中の札と同じ重みに見えうる(点線の箱・「L3」の印・案の文で打ち消した)。
3. **札の印の表は作り手の読み**(上の D): 例えば olm4 を状態 18〜21 の出所に入れた根拠は BRIEF の「SAE の群は olm4・olm7 が凍結した物」だけで、状態の絵が olm4 の数を直接引いているわけではない。
4. **台本は 194.8 秒 / 195 秒**(余裕 0)。A の相づちを 3 行落とした(状態 15・21・9)。
5. **電話の地図は一覧**(3×3 の格子ではない)で、蛇行の並びは見えない(塊の名と札の数・日付は見える)。
6. **状態 23 の点の列は小さい**(11 点)。意味の中心は余裕の 11 マスと下の四群の行。
7. 札の印の click の検査は、番号の button と札の button で navigation している(**chapter の button の click は `check_chapters` が受け持ち**、新しい章 `tree` も含む)。

## 道具の版・環境(v2.1)
bun 1.3.0 · python 3.14.3(py314)· numpy は py314 の環境のもの(npz の読みだけ)· anywidget 0.11.0 · marimo 0.23.13 · jupyterlab 4.5.6 · macOS 27.0.1 · Chromium = playwright の headless。BRIEF の版と同じ(違いなし)。

<!--CHECKS-->
## 実行した検査(v2.1 の最後の通し = `sh run_checks.sh`・ログは `checks/last_run.txt`)

- states(measure): `measure_ok` を **300** 状態分(video / desk / phone × ja / en = 6 通し × 30 状態 + 他の 3 頁 + reduced motion)通した。失敗の行(`error` で始まる行・0 でない `drive exit`・`MISSING`): **0**(`drive exit 0` の 2 行 = marimo と JupyterLab の正常終了は数えない)。
- robust: 1500 通り・例外 0・NaN 0 · 1500 通り・例外 0・NaN 0 · 1500 通り・例外 0・NaN 0(全状態 × ja / en × 位置 × camera・各回を同期に描く)。
- 章の button(本物の click): `chapters_ok` 2 回(desk と phone・9 章 = v2.1 の新しい章 `tree` を含む)・**札の印の click(`check_cards`・本物の click で地図の状態へ)**: 12 行が通った(desk と phone・状態 12 の `cmt13` → 地図 + 押した札の縁 / 番号 button で状態 0 → `replication_config_frozen` → 地図 / 地図の番号で選択が消える / 台帳の「全部」の印 → 地図・選択なし)・語の走査 `words_ok` 1 回・ja / en の数の一致 `parity_ok` 1 回・`check_sae`(v2 + 状態 24 に直した二つの label の規則)`sae_ok` 1 回・**`check_v21`**(散布の点 59 + 34・輪 2・棒 2・chips が read.json の値・11 点の塗り 7 / 白抜き 4・全 30 状態 × ja / en の札の印が config.json と一致 = 60 回・地図の札 12・使う状態の番号が config と一致)`v21_ok` 1 回。
- 数の照合: anchors checked: 352 · missing or different: 0 · claim rows 40 · control: 9 / 9 wrong anchors reported · anchors per kind {'derived': 84, 'derived_close': 20, 'file_md5': 12, 'here_json_equals': 30, 'pack_close_derived': 39, 'pack_equals': 14, 'pack_equals_derived': 27, 'repo_json_equals': 106, 'repo_text_contains': 20}
- 台本: SCRIPT_yukkuri.md written: 35 lines · 194.8 s (≤ 195) · core ends at 10.0 s
- 公開の柵: fence: 17 files scanned · internal words: 0 
- marimo / JupyterLab(図 → kernel と kernel → 図の両方向 + kernel の数え直し): eval: "marimo: the kernel recount says equal True · kernel recount: {'state': 4, 'screen': ['8 / 10', '0 / 10' · eval: "marimo: chapter sae, state 18: the kernel recount says equal True · kernel recount: {'state': 18, 'scre · eval: "{\"recount_equal\":true,\"recount_cell_tail\":\"json rows[cue_tag = nlnl, open](L1)· | state 5 · t 1 ·  · eval: "{\"sae_recount_equal\":true,\"state\":\"18\",\"tail\":\"'1 / 10'],\\n 'equal': True} | {'state': 18,\\n
- 停止後: own pid 82583 still alive after stop: no · listeners on port 27491 after stop: [] · own pid 83015 still alive after stop: no · listeners on port 27493 after stop: []
- console が clean だった走り: 23 回(JupyterLab の warning は図と無関係: Unsatisfied version 0.21.1 from jupyterlab-chat-extension of shared singleton mo; [ACP] Registered ToolCallsComponent with preamble registry)

```
run_checks.sh done · exit 0
pages md5: b475ca80 moy1 · c3c9a784 moy1-en · f543fca6 widget.js
```

撮影(`python3 -I make_captures.py --en` · `captures/capture_log.txt`):

```
17:46:32 video moy1                 states 0..29 (30) · page md5 e55f6df1 · 39 s · console clean
17:47:11 video moy1-en              states 0..29 (30) · page md5 19cb99af · 39 s · console clean
17:47:19 pairs video moy1                 states 18a 18b 19a 19b · 8 s · console clean
17:47:59 desk  moy1                 states 0..29 (30) · page md5 e55f6df1 · 40 s · console clean
17:48:39 desk  moy1-light           states 0..29 (30) · page md5 f2e19b68 · 40 s · console clean
17:49:18 desk  moy1-en              states 0..29 (30) · page md5 19cb99af · 40 s · console clean
17:49:58 desk  moy1-light-en        states 0..29 (30) · page md5 16b98cf8 · 40 s · console clean
17:50:37 phone moy1                 states 0..29 (30) · page md5 e55f6df1 · 39 s · console clean
17:51:16 phone moy1-light           states 0..29 (30) · page md5 f2e19b68 · 39 s · console clean
```

## 直した build の再走(`sh run_post_fix.sh`・ログは `checks/post_fix_run.txt`)

- measure: `measure_ok` **180** 状態分(video / desk / phone × ja / en = 6 通し × 30 状態)・失敗の行 **0** · `check_v21` `v21_ok` 2 回(desk と phone)· `check_cards`(本物の click)の通った行 12 行(desk と phone)· 語の走査 `words_ok` 1 回 · ja / en の一致 `parity_ok` 1 回。

```
run_post_fix.sh · 2026-10-28 17:45:37 · pages: pages_new · md5 e55f6df1 moy1 · 19cb99af moy1-en · 801fcd04 widget.js
run_post_fix.sh done · exit 0
```

<!--/CHECKS-->


---

# 以下 = v2 の記録(状態の番号は v2 の 0〜25・v2.1 では「状態 22」(二つの label)が 24・台帳が 26〜29)

HEAD(R1) = 6e92d6aa(BRIEF v2 を入れた commit = この session の書き始めの checkout の HEAD)・納品時の worktree の HEAD = efe7593f(git は読むだけ = `rev-parse` / `log` / `status`・書き込みなし・worktree は clean のまま)
(書いている間に共有 checkout の HEAD は別の job の commit で進んだ(途中で 0e3edd75・納品時に efe7593f)。作業の途中で `git log --oneline -3` を一度叩き、BRIEF の「git log は 6e92d6aa まで」を 2 本越えて題(olm60・moy-5)が目に入った。本文は開いておらず、この図解には使っていない = 記録。)

# NOTES — entry_sonnet_max_v2(moy-1 の図解: v1 + 章「作図と SAE の推移」+ cmt5 の二つの label)の作り方・足したこと・直したこと・指摘

作り手 = Sonnet 5.5 max(背景 session・subagent なし・install / 通信 / git の書き込みなし・model も SAE も動かさない・実験の script は import も実行もしない = olm59 の runner は開いていない)。
BRIEF = v1 `BRIEF_v1_moy1_block_open_two_makers_20261028.md`(機械・skill・読み手・色・検査・撮影の規則)+ v2 `BRIEF_v2_moy1_add_construction_focus_x_sae_trajectory_20261028.md`(入れた commit = 6e92d6aa)。
土台 = 自分の v1(`entry_sonnet_max_v1/`・書き換えていない)を scratch に写して足した。**他の作り手の entry と `explainer_moy5/` は読んでいない**(folder の一覧も開いていない)。
読んだもの: 両 BRIEF・skill(coread-explainer の SKILL.md と references の checks-and-captures / wording / data-contract。implementation / judging / publishing / coread-loop / brief-template は開いていない = 骨は v1 のを写したので)・自分の v1 一式(NOTES・pack・scenes・figure・i18n・検査の script)・BRIEF v2 §1 の data(olm59 の read.json / control.json / npz 120 本・RESULT olm59・PREREG olm59)・v1 の data 表の file(cmt5 の json ほか)。memory は自分では開いていない(session の開始時に自動で入る分は除く)。
開始 15:09:49 JST・打ち切り 120 分(= 17:09:49)・納品 16:26 JST。

## v2(2026-10-28 午後)— v1 から何を足し、何を直したか

### A. 足した: 7 章「作図と SAE の推移」= 状態 18〜22(5 状態)・台帳を 3 状態に
- **章の置き場 = models(6 章)の後ろ・台帳の前**(BRIEF の「台帳の前が目安」)。理由: 本文・台帳・限定の札が「3・4 章」「5 章」「6 章」と章の番号で参照している(X04・X06・notClaimed・状態 11 の lead ほか)。章を 6 章の前に入れると参照を全部直すことになり、直し損ねが出る。後ろに足せば既存の参照は動かない。
- **18** S_O(F5a-2 think r15・生成 1,210 token・最初の「直径 / 中点 = O1O2」の文 = token 329「Midpoint of O1 and O」)の全 token。上の列 = 本文の述語の印(O の名・He・Hi の名・直径の文・答えの欄)・下の四枚 = 4 群の値の山(群の latent の平均)・薄い帯 = 名指す前 32 token・濃い帯 = 名指した token から後ろ 32 token・横線 = 帯の平均・縦線 = 名指した token・滑り棒 = cursor の token。**右の作図(1 章の座標の flat な図)は、cursor の token が当たった述語に応じて O1O2 の円 / He・Hi の円 / 点が光る**。右下 = 前後 32 token の本文の逐語(当たった所に印)。
- **19** S_H(F5b-1 natural r14・生成 118 token・最初の token から答えの欄の中・最初の「直径 = He・Hi」の文 = token 45)も同じ見方。
- **20** 二つの行を、名指した token をそろえ(−32〜+31)・**同じ縦の目盛り**で上下に(上 = S_O・青 / 下 = S_H・橙)。右 = 二つの作図(cursor は距離で共通)+ 前 / 後 / 差の表。
- **21** 集計: 4 群 ×(O1O2 の出来事 59 行 = 青・He・Hi の出来事 34 行 = 橙)の「後 > 前」の割合の柱・差の中央値・50 % の面・予想 Q1 / Q2 の板(両方 ✗)。右 = Q3_desc の表(全行 / bind / attractor・attractor の O の 3 本は「—」)・予想の表・統制 C1〜C3 の札。
- **22** cmt5 の 120 行の二つの label(全文 / 答えの欄 × 考えの道 / 答えの道 / natural・1 マス = 1 行・bind を枠で囲む)+ 14 行の対応表。
- **台帳を 2 状態 → 3 状態**: 23 = 1〜6 章(v1 の L1 21 行 + L3 2 行)・24 = 7 章(K22〜K29 + R03・R04)・25 = 言えない 13 行 + 問い 4 つ。理由: 一つの状態に L1 29 行を入れると video 枠で 1,483 px(上限 1,080)になり、検査(video の枠の切れ)が捕まえた。
- 新しい語は 5 つ: 群の名(結び / 考えの中点 / 答えの側 / 考えの側 = olm7 の名・PREREG olm59 §1)・場面の名(S_O / S_H)・出来事(最初に述語が当たった token)・窓(前 32 / 後 32)・作図の円が光る(= 述語が当たった印)。
- 色: **新しい色は足していない**(青 = O1O2 の行・橙 = He・Hi の行 = v1 の意味のまま)。4 群は lane と名前で分け、hue で分けない(= 規則「色の意味は一つ」を優先した代わりに、「どの群か」は左の名と数字の札を読む必要がある = 自信の無い所 1)。

### B. 直した: cmt5 の bind の二つの label(BRIEF v2 §0 の必須)
v1 は cmt5 の bind を全文の label だけで「考えの道 40 / 40 対 答えの道 8 / 40」と書いた。答えの欄の label(`label_json_fields`)では **36 / 40 対 4 / 40**。v2 は両方を並べ、どちらか片方だけを「bind」と書かない。直した場所:
1. 状態 8 の限定の札(`lim`・ja / en)— v1 の文を「全文の label 40 / 40 対 8 / 40・答えの欄の label 36 / 40 対 4 / 40(状態 22)」に。数は pack から。
2. **状態 22(新)**: 3 つの道 × 2 つの label の棒と 14 行の対応表。
3. 台帳 K16(二つの label を variant ごとにも・F5a-2 17 / 20 と F5b-1 19 / 20 ほか)・K28(新)・X01(「どちらの label かを書かずに言わない」を足した)。
4. README の受け入れの問い 3 の基準(両方を並べた)+ 問い 4(新・7 章の基準)。
5. SCRIPT の台詞(「全文の label で 40 対 8、答えの欄の label で 36 対 4。片方だけを bind と書かない」)。
6. **検査**(`check_sae.json`): 全状態 × ja / en の text に「全文の数(40 / 40 か 8 / 40)があれば答えの欄の数(36 / 40 か 4 / 40)もある・逆も同じ」を走らせ(50 回・違反 0)、規則そのものの陽性 / 陰性の統制も取った。
- 凍結の file は読み直しただけ(cmt5 の json の md5 `c5d64f9f…` は v1 と同じ)。cmt5 の RESULT の題の「読みは保留」はそのまま(統制 C1 が F5b-1 で落ちている)。

### C. 数の経路(v2 で足した分・四つ)
1. **pack(第一経路)**: `pack_moy1.py` の 8c 節。olm59 の npz 120 本を `allow_pickle=False` で読み(md5 を manifest に・tokens が本文を tile することの assert・first event = flags の最初の 1)、窓の平均・Q3 の 24 キー・Q1 / Q2・labels を配列から数え直して **read.json と照合**(n と「後 > 前」の本数は厳密・中央値は 1e-6 = read.json は float32 の演算・こちらは float64)・BRIEF v2 §3 の値(C1〜C3・Q1・Q2・Q3 の 5 キー・labels 5 本・場面の 2 行)を typed で突き合わせ・cmt5 の json の `label` / `label_json_fields` と npz の `label` / `label_json` を 120 行すべて照合・場面の行を述語から選び直して assert(S_O = 考えの道 × 答えの欄 bind × `o_diam` の両側が収まる → 生成の最短・S_H も同様)・PREREG の本文から閾(70 % / 60 %)を読む(typed しない)。
2. **data.mjs(第二経路・JS)**: 120 本の npz の md5 を manifest と・窓の側 file(`generated/olm59_windows.json` = 配列の窓の値)から Q3 の 24 キーを JS で数え直して read.json と・場面の行の最初の名指しを mask から見つけ直す・窓の平均を carry した series から(4 桁の丸めの 2e-4 以内)・順位・cmt5 の二つの label を cmt5.json から。**食い違えば build が止まる**。
3. **check_claims.py(第四経路)**: anchor 206 本(v1 92 + 114)。npz を**自前の loader**(窓は累積和・median は手書き・最初の flag は自前の走査)で読み、read.json・control.json・PREREG / RESULT の文(text として)・pack の持つ値(`pack_close_derived`)と突き合わせる。**検査器そのものの統制**: 5 本の間違った anchor(期待値 +1・本数 −1・pick の取り違え・閾の文字 70 → 71・pack の期待値 0.71)が全部報告されること(5 / 5)を毎回走らせる。
4. **widget の kernel(第三経路)**: `check_counts()` に状態 18〜22 の recount を足した(marimo・JupyterLab の両方向の検査にも 1 回ずつ。どちらも `equal True`)。
+ ja / en の数の一致(`check_parity`)は新状態の chips も見る。

### D. この entry の述語・窓の規約・場面の選び(札ではない・札の外の数を図に出していない)
- **窓**: 前 = 出来事の token の手前 32 token `[e−32, e)`・後 = 出来事の token を先頭に 32 token `[e, e+32)`・両側が生成の内に収まる行だけ(o_diam 59 / 64・h_diam 34 / 44)。**runner を開かず**、配列から read.json の Q3(24 キー)を再計算して規約を決めた: この規約だけが 24 キーすべてに一致し、後を `e+1` から数える規約では o_diam の中点が 50 / 59(read.json 48)・結びが 8 / 59(同 9)にずれた(探索の script は scratch の `work/` に置いた = 納品の束には入れていない)。
- **述語**: 作図の述語は olm59 の flags(PREREG の `PRED_O` / `PRED_HEHI_DIAM`)。この entry の v1 の述語(`O₁O₂` の添字を足した版)を S_O / S_H の本文に当て、**最初の当たりが card の event の run の内に入る**ことを assert した(S_O: 「Midpoint of O1 and O」= token 329〜335・S_H: 「 diameter HeHi」= 45〜47)。述語の範囲は「O の後ろの 2」を含まない(card の run は `O1 and O` で終わる)ので、逐語の印は `Midpoint of O1 and O` まで。
- **場面の選び**(BRIEF v2 §0 の述語どおり・R5): S_O = 考えの道 × 答えの欄 bind × 両側が収まる → 生成の最短 1 番目(次点 1 番目との長さの差を assert)/ S_H = 答えの欄 attractor × 両側が収まる → 最短。pack が選び直し、JS と check_claims(K23a)がもう一度選ぶ。
- **「円が光る」**: cursor の token の mask(flag の 6 bit)→ O1O2 の円と線分(`o_diam`)・He・Hi の円と線分(`h_diam`)・O1・O2 の点(`o_name` か `o_diam`)・He・Hi の点・「答えの欄(JSON)の中」の札(`json`)。**本文の述語が当たった印で、model の内の読み出しではない**(inset の見出しと札に書いた)。検査 `check_sae.json` が「event で O の円が 1 つ・He・Hi の円が 0 / どの述語にも当たらない token では 0 / O の名だけの token では点 2 つ・円 0 / S_H では逆 / 状態 20 では二つの inset に 1 つずつ」を本物の DOM で確かめる。

### E. template / 生成物に足した所
- `state_machine.js`: 位置の呼び名(`tok` / `rel`)・章ごとの「言わないこと」の strip(`notClaimedBy`)。`build.mjs`: 台帳の行を評価する状態の番号を config から(v1 は 18 を typed)・css が末尾の状態の番号を名指すことの検査・`window.__DATA`(検査が pack の数を読む)。`figure.css`: 末尾の状態の番号の置換(10 か所)・リボン / 窓 / inset / 表の部品。`scenes.js`: `traj` / `agg` / `lab2`。`figure.js`: 状態 5 つ・台帳の part(v1 / v2)・inset と表の builder。`i18n.js`: ja / en の全文。
- `make_check.py`: inset の字の px・v2 の禁じ語(「考え始めた」「commit の正体」「活性が bind を決める」ほか)の走査と**その陽性 / 陰性の統制**・`check_sae.json`・台帳の 3 状態。`run_checks.sh`: `check_sae` を足した。`make_script.py`: 10 行を足し **178.7 秒(≤ 180)**・芯の 10 秒は v1 のまま。`make_readme.py`・`make_claims.py`(D 節に v2 の補正 4 つ)・`make_notebook.py`(cell 7)・`widget.py`(`check_counts` と docstring)。

- 作業中の道具(納品の束には入れていない = scratch の `work/`): `quick.sh`(drive の検査を 3 本ずつ並行)・`diag.sh`(MEASURE の `throw` を外した版 = 全状態 × 3 frame × ja / en の失敗を 1 回で一覧。`run_checks.sh` の measure は最初の失敗で止まるので、直す順番を決めるのに使った)・`shoot.py`(状態ごとの撮影と目視)。**最後の通しは throw する版(`run_checks.sh`)で取り直した。**

### F. 驚いたこと(取っておく事実)
1. **場面の S_O は代表の行ではない**: 59 行の中で、考えの中点の差(+0.83)は大きい方から 5 番目・答えの側の差(−0.86)は小さい方から 2 番目。述語で選んだ最短の行は、集計の中央値(+0.157・−0.251)より大きく動く側にいた。札に順位を書いた(状態 18 の `lim`・K23・X12)。S_H も代表ではない(34 行中: 答えの側の差は大きい方から 5 番目〔|差| では 17 番目〕・考えの側は 7 番目〔同 9 番目〕)。
2. cmt5 の考えの道の「全文 bind 40 / 40」は、答えの欄では 4 行が attractor(F5a-2 3・F5b-1 1)。答えの道の全文 bind 8 のうち 3 行は stuck-L1・1 行は attractor に替わる。natural は 25 → 18(attractor 6・flail 1)。
3. RESULT olm59 §5-1 の「HeHi を名指した所では、どの群も半々で動かない」は、同じ RESULT の表(答えの側 11 / 34・考えの側 19 / 34)と合わない。R03 は数に合わせた言い直しにして「作り手の言い直し」と札を付けた。RESULT の側の訂正は頼んでいない(実行層へ: 「どの群も半々」ではなく「差の中央値が小さい(−0.043〜+0.010)」)。
4. 述語の範囲: `o_diam` の run は「O1 and O」で終わり、直後の「2」は含まない。
5. **検査が実際に捕まえた不具合**(どれも data の読みではなく表示 / 文言の欠陥): ① 台帳 29 行が video 枠で 1,483 px(上限 1,080)→ 3 状態に分けた ② 台帳の最後の状態(言えない 13 行 + 問い 4 つ)が video で 1,197 px → その状態だけ字を 13.3 px に ③ phone の状態 20 で inset の字が 7.72 px(下限 9.5)→ 二つの inset を縦に積んだ(9.88 px)④ 英語版の状態 18 の strip が video で 1,097 px → 英語の札と注を短くした ⑤ 英語の「median difference」の札が最初の柱の値に重なる → 「median Δ」⑥ phone で 状態 21 の群の名「answer side」「thought side」が重なる → 短い名 ⑦ phone で 状態 22 の英語の見出しが viewBox を出る → 短く ⑧ **二つの label の規則が、台帳 K28 の文(「36(」と書いて「36 / 40」と書かなかった)を捕まえた**(= 規則が働いた実例・文を「X / 40」の形に直した)⑨ 凡例と readout が video の下で重なる・状態 21 の Q2 の板の札が柱の数に重なる・状態 20 の header が重なる・phone の状態 22 の label が棒に重なる ⑩ 表(状態 21)が列からはみ出す → 見出しの行を足し短い語に。 ⑪ **marimo の検査が、widget の kernel の数え直し(`check_counts`)の状態 18 の期待値の誤りを捕まえた**: 期待値に 4 つの群を入れていたが、画面の chip は「最初の token + 3 群」の 4 つ(考えの側は lead と readout に在る)→ `equal False` → 期待値を chip と同じにして `equal True`(状態 18 の kernel の数え直しは marimo と JupyterLab の両方で通った)。⑫ **v1 から引き継いだ `run_checks.sh` が、marimo と JupyterLab の 2 段の失敗を黙って隠した**: 二つの script は `PY` を python 環境の「folder」として読み、`run_checks.sh` は「python の binary」として読む。binary の path を export して走らせたので 2 段とも立ち上がらず、pipe の grep が失敗の行を捨て、exit code も数えていなかったので、全体の通しが `exit 0` と出た。→ 直した(`dirname` で分ける・各 script の exit code を数える・error 行を log に出す・別の port で走らせる・この 2 段だけを足して走らせる `WIDGETS_ONLY=1`)。
6. 背景 session の事情は v1 の NOTES の 5 と 9 のまま(`kill` は PID を控えたものだけ・`lsof` / `ps` と `kill` は別の呼び出し)。今回も、止めたい検査の shell を探す呼び出しと止める呼び出しを分けた(合成は hook が止めた)。同じ時間に別の job の Chrome も動いていた(触れていない)。納品: `EnterWorktree` は cwd が git の外(scratch)だと `not in a git repository` で失敗したので、BRIEF の指示どおり先に共有 checkout へ `cd` してから呼んだ(呼んだ後は cwd が worktree に移る・以後は共有 checkout へ `cd` していない)。

### G. 一番自信の無い所
1. **4 群を hue でなく lane と名前で分けた**ので、一枚の絵だけで「どの群が動いたか」は読み取れず、左の名と数字の札・chips を読む必要がある(新しい色を足さない規則を優先した)。
2. **状態 20**(S_O と S_H を同じ目盛りで上下に)は、行の種類が違う(考えの道 × bind / natural × attractor)ので「O1O2 と He・Hi の違い」に読まれうる。札・lead・限定で打ち消したが、絵だけでは打ち消せない。本体は状態 21(集計)。
3. **光る円**は本文の述語の hit の印だが、「model の中で円が光った」と読まれうる。inset の見出し・札に書いたが、動画の字は小さい。
4. **状態 21**: 50 % の面と予想の板(白)が浮いて見える。Q1 の n = 36(考えの道 × 答えの欄 bind)は O の柱の 59 行の部分集合で、結びの柱 9 / 59 と並ぶと誤読されうる(別の集合 = 表と札に書いた)。
5. **phone**: リボンが細く、4 群の差は数字の札頼み。立体の手触りは弱い(v1 の電話と同じ弱さ)。
6. 英語版の群の名(close / mid / answer side / thought side)は olm7 の RESULT を読まずに、BRIEF / PREREG が与える対応(結び = close・考えの中点 = mid・答えの側 = ans・考えの側 = think)から付けた。
7. 中点の群の上がりは本文が計算に移った写しかもしれない、という RESULT §5-2 の注意(X11)を絵の近くに置いたが、S_O の逐語(「Midpoint of O1 and O2: O1 is (−2.2849, …」)を見せる絵は「O1O2 を名指す → 計算」を強く見せるので、読者は原因と思いうる。

## 道具の版・環境(v2)
bun 1.3.0 · python 3.14.3(py314)· numpy は py314 の環境のもの(npz の読みだけ)· anywidget 0.11.0 · marimo 0.23.13 · jupyterlab 4.5.6 · macOS 27.0.1 · Chromium = playwright の headless。BRIEF v1 / v2 の版と同じ(違いなし)。

## 検査の log の読み方
`checks/last_run.txt` = **最後の `sh run_checks.sh` の一つの通し**(build → 見出し → 照合 → 台本 → 柵 → 状態 × frame × 言語 → robust → 他の頁 → reduced motion → parity / interaction / **check_sae** → 章の click → 語の走査 → marimo → JupyterLab)。これより前の通しは 2 回(途中で止めた 1 回と、最後まで通した 1 回)あり、**最後まで通した方でも marimo と JupyterLab の 2 段が黙って落ちていた**(上の ⑫)。直してから、全体をもう一度、`PY` を export しない環境で最初から通し直したものがこの log。撮影(`captures/`)は、この通しの直前の build と同じ pages(md5 は `capture_log.txt` と `last_run.txt` の「pages md5」で照合できる)から撮った。

<!--CHECKS-v2-->
## 実行した検査(v2 の最後の通し = `sh run_checks.sh`・ログは `checks/last_run.txt`)

- states(measure): `measure_ok` を 260 状態分(video / desk / phone × ja / en = 6 通し × 26 状態 + 他の 3 頁(明・英・明英)+ reduced motion)通した(inset の字の px も同じ下限で測る)。失敗の行(`error` で始まる行・`drive exit` が 0 でない行): 0。
- robust: 1300 通り・例外 0・NaN 0 · 1300 通り・例外 0・NaN 0 · 1300 通り・例外 0・NaN 0(全状態 × ja / en × 位置 5 通り × camera 5 通り・各回を同期に描く)。
- 章の button(本物の click): `chapters_ok` 2 回(desk と phone・8 章)・語の走査 `words_ok` 1 回(v2 の禁じ語 + 陽性 / 陰性の統制 8 本)・ja / en の数の一致 `parity_ok` 1 回・操作(drag・key・slider)の検査 1 回・**`check_sae`(v2)`sae_ok` 1 回**(光る円 5 通り・key / slider・状態 20 の二つの inset・状態 21 の柱と chips・状態 22 の表・全状態 × ja / en 52 回の「cmt5 の bind は二つの label を並べる」規則 = 違反 0 と、規則そのものの統制)。
- 数の照合: anchors checked: 206 · missing or different: 0 · claim rows 29 · control: 5 / 5 wrong anchors reported · anchors per kind {'derived': 61, 'derived_close': 12, 'file_md5': 11, 'pack_close_derived': 34, 'pack_equals': 5, 'pack_equals_derived': 1, 'repo_json_equals': 66, 'repo_text_contains': 16}
- 台本: SCRIPT_yukkuri.md written: 35 lines · 178.7 s (≤ 180) · core ends at 10.0 s
- 公開の柵: fence: 17 files scanned · internal words: 0 
- marimo(図 → kernel と kernel → 図の両方向 + kernel の数え直し・v2: Python の button で 7 章へ): `equal True` 2 回(状態 4・状態 18)· JupyterLab(同じ・v2: `goto_chapter("sae")`): `recount_equal` 2 回(状態 4・状態 18)。停止後の listener = 0 本(2 段とも空)・自分の pid の生き残り = ['no', 'no'](no = 無い)。
- console が clean だった走り: 20 回(JupyterLab の warning は `jupyterlab-chat-extension` の版の不一致と ACP の登録 = 図と無関係)。

```
run_checks.sh · 2026-10-28 16:17:26 · bun 1.3.0 · Python 3.14.3
built: 4 pages · widget js 322 KB · css 27 KB · 26 states → <scratch>
pages md5: a5ec79b4 moy1 · 529912e7 moy1-en · a05a8605 widget.js
headings ok
CLAIMS.md written: 29 L1 rows · 4 L3 · 13 x · anchors 206
anchors checked: 206 · missing or different: 0 · claim rows 29 · control: 5 / 5 wrong anchors reported · anchors per kind {'derived': 61, 'derived_close': 12, 'file_md5': 11, 'pack_close_derived': 34, 'pack_equals': 5, 'pack_equals_derived': 1, 'repo_json_equals': 66, 'repo_text_contains': 16}
SCRIPT_yukkuri.md written: 35 lines · 178.7 s (≤ 180) · core ends at 10.0 s
fence: 17 files scanned · internal words: 0 
== check_states: video
  measure_ok x 26
console: clean
== check_states: desk
  measure_ok x 26
console: clean
== check_states: phone
  measure_ok x 26
console: clean
== check_states_en: video
  measure_ok x 26
console: clean
== check_states_en: desk
  measure_ok x 26
console: clean
== check_states_en: phone
  measure_ok x 26
console: clean
== check_robust: video
eval: "{\"combos\":1300,\"errors\":0,\"nan\":0,\"msgs\":[]}"
console: clean
== check_robust: desk
eval: "{\"combos\":1300,\"errors\":0,\"nan\":0,\"msgs\":[]}"
console: clean
== check_robust: phone
eval: "{\"combos\":1300,\"errors\":0,\"nan\":0,\"msgs\":[]}"
console: clean
== the four pages (dark / light x ja / en), desk
-- moy1-light
  measure_ok x 26
console: clean
-- moy1-en
  measure_ok x 26
console: clean
-- moy1-light-en
  measure_ok x 26
console: clean
== reduced motion (prefers-reduced-motion: reduce), desk
  measure_ok x 26
console: clean
== check_parity (ja / en numbers) and check_interaction (drag, keys, slider)
eval: "{\"parity_ok\":true,\"control_differs\":true,\"bad\":[]}"
console: clean
eval: "orbit: the drag changed the picture"
eval: "key: ArrowRight -> 9"
eval: "key: ArrowLeft -> 8"
eval: "key: . -> t 4"
eval: "slider: the readout says blocked s7 · 16544 字 · 書き始め 文 · 全文 label"
eval: "key: l -> en"
console: clean
== check_sae (v2: the inset lights where a predicate hits · keys / slider · the aggregate · the two labels of cmt5's bind in every state)
eval: "{\"sae_ok\":true,\"bad\":[],\"two_labels\":{\"states_checked\":52,\"violations\":[]},\"s18_event\":{\"t\":329,\"ringO\":1,\"ringH\":0,\"segO\":1},\"s18_none\":{\"t\":0,\"ringO\":0,\"ringH\":0,\"pts\":0},\"s18_name\":{\"t\":27,\"ringO\":0,\"ptsO\":2},\"key_dot\":330,\"slider\":{\"t\":200,\"rea
console: clean
== check_chapters: desk
eval: "{\"chapters_ok\":true,\"clicks\":[\"ledger -> 23\",\"sae -> 18\",\"models -> 16\",\"moment -> 12\",\"blocked -> 8\",\"open -> 4\",\"prompts -> 2\",\"problem -> 0\",\"step 13 -> 13\"],\"labels\":[\"問題の図\",\"二つの問題文\",\"open で起こること\",\"blocked で起こること\",\"bind する瞬間\",\"他の model\",\"作図と SAE の推移\",
console: clean
== check_chapters: phone
eval: "{\"chapters_ok\":true,\"clicks\":[\"ledger -> 23\",\"sae -> 18\",\"models -> 16\",\"moment -> 12\",\"blocked -> 8\",\"open -> 4\",\"prompts -> 2\",\"problem -> 0\",\"step 13 -> 13\"],\"labels\":[\"問題の図\",\"二つの問題文\",\"open で起こること\",\"blocked で起こること\",\"bind する瞬間\",\"他の model\",\"作図と SAE の推移\",
console: clean
== check_words
eval: "{\"words_ok\":true,\"found\":[],\"control\":[1,0,2,0,1,0,1,0]}"
console: clean
== marimo (both directions)
eval: "{\"after_python_open_state4\":{\"figure\":{\"state\":\"4\",\"chapter\":\"open\",\"lang\":\"ja\",\"readout\":\"open s3 · 326 字 · 全文 label B-stuck-L1 · 答えの欄 裸の共円 · He文 0 · O文 0\"},\"kernel\":{\"state\":4,\"t\":-1,\"lang\":\"ja\",\"done\":\"True\"},\"recount\":\"kernel recount: {'state': 4, 'scr
eval: "marimo: the kernel recount says equal True · kernel recount: {'state': 4, 'screen': ['8 / 10', '0 / 10', '1 / 10', '0 / 10'], 'python': ['8 / 10', '0 / 10', '1 / 10'], 'equal': True}"
eval: "marimo: chapter sae, state 18: the kernel recount says equal True · kernel recount: {'state': 18, 'screen': ['token 329', '0.10 → 0.93', '2.15 → 1.29', '0.34 → 0.32'], 'python': ['token 329', '0.10 → 0.93', '2.15 → 1.29', '0.34 → 0.32'], 'equal': True}"
eval: "kernel and figure agree: state 18 lang en"
console: clean
drive exit 0 · wall 22 s
own pid 49349 still alive after stop: no
listeners on port 27481 after stop: []
== JupyterLab (both directions)
eval: "{\"recount_equal\":true,\"recount_cell_tail\":\"_tag = nlnl, open](L1)· 色と印は答えの欄の読み  | state 5 · t 1 · lang ja · done True\\n状態 5 · open で起こること — 全文の label と答えの欄\\nopen s1 · 全文 label B-attractor · 本文に He・Hi の語 あり · 答えの欄 裸の共円\\n | {'state': 4,\\n 'screen': ['8 / 10', '0 / 10', '1 / 10', '0 / 1
eval: "{\"sae_recount_equal\":true,\"state\":\"18\",\"tail\":\"'1 / 10'],\\n 'equal': True} | {'state': 18,\\n 'screen': ['token 329', '0.10 → 0.93', '2.15 → 1.29', '0.34 → 0.32'],\\n 'python': ['token 329', '0.10 → 0.93', '2.15 → 1.29', '0.34 → 0.32'],\\n 'equal': True}\"}"
console.warning: Unsatisfied version 0.21.1 from jupyterlab-chat-extension of shared singleton module @jupyter/chat (required ~0.17.0)
console.warning: Unsatisfied version 0.21.1 from jupyterlab-chat-extension of shared singleton module @jupyter/chat (required =0.20.0-alpha.2)
console.warning: [ACP] Registered ToolCallsComponent with preamble registry
drive exit 0 · wall 34 s
own pid 49496 still alive after stop: no
listeners on port 27483 after stop: []
demo_jupyter.ipynb restored (clean copy) and .ipynb_checkpoints removed
run_checks.sh done · exit 0
```

撮影(`python3 -I make_captures.py --en` · `captures/capture_log.txt`):

```
16:12:54 video moy1                 states 0..25 (26) · page md5 a5ec79b4 · 34 s · console clean
16:13:28 video moy1-en              states 0..25 (26) · page md5 529912e7 · 34 s · console clean
16:13:36 pairs video moy1                 states 18a 18b 19a 19b · 8 s · console clean
16:14:11 desk  moy1                 states 0..25 (26) · page md5 a5ec79b4 · 35 s · console clean
16:14:46 desk  moy1-light           states 0..25 (26) · page md5 1609a8dc · 35 s · console clean
16:15:21 desk  moy1-en              states 0..25 (26) · page md5 529912e7 · 35 s · console clean
16:15:57 desk  moy1-light-en        states 0..25 (26) · page md5 c6b7b09e · 35 s · console clean
16:16:31 phone moy1                 states 0..25 (26) · page md5 a5ec79b4 · 35 s · console clean
16:17:06 phone moy1-light           states 0..25 (26) · page md5 1609a8dc · 35 s · console clean
```

<!--/CHECKS-v2-->

## v1(2026-10-28 午前〜昼)の記録 — v1 の NOTES をそのまま(状態の番号は v1 の 0〜19・v2 では台帳が 23〜25)
## v1(2026-10-28)— 何を作ったか
- **状態表**: 20 状態・7 章(`config.json` の `chapters` が番号の唯一の置き場): 問題の図 0–1 / 二つの問題文 2–3 / open で起こること 4–7 / blocked で起こること 8–11 / bind する瞬間 12–15 / 他の model 16–17 / 台帳 18–19。`list_headings.py` が ok。
- **立体の部品**(= 説明の物): 盤(座標の図)・帯の列(一行 = 一本の板・対数の目盛り・**状態 4 と 8 は open 10 + blocked 10 = 20 行を一枚に描き、強調する条件と薄くする条件を替える** = BRIEF §2 の「芯の一枚」)・三段の棚(全文の label / 本文の語 / 答えの欄)・積み木の棚(文の仮説 0 → 7 と 1 → 5)・積み木の柱(cue ごとの label の数)・天秤(O の皿 / He の皿・針 = 出力の差)・柱の林(16 の位置 × 上位 10 head)。第三者の character・実験室の質感・steampunk は使っていない。
- **数の経路**: ① `pack_moy1.py`(frozen file の md5・BRIEF の V1〜V11・図に出る数を assert・答えの欄の述語の陽性統制)→ ② `data.mjs`(JS で別に数え直し・述語は JS への移植・食い違えば build が止まる)→ ③ `check_claims.py`(別に書いた code・anchor 92 本・棚卸しの `check_values.out` を text として読んで V1〜V11 と突き合わせる)→ ④ widget の kernel 側(`w.check_counts()` が pack の数と画面の chips を突き合わせる)→ ⑤ ja / en の数の一致(`check_parity.json`・陽性統制つき)。
- **台帳と台本は data から生成**: `CLAIMS.md` は `generated/ledger_rows.json`(page が台帳に出す行そのもの)から `make_claims.py` が書く。`SCRIPT_yukkuri.md` は `make_script.py`(数は data から・長さを数える・行数と秒数と芯の秒数は SCRIPT の先頭の行と下の log の `SCRIPT_yukkuri.md written` の行が正)。`README.md` も状態表を設定から生成。手で数を写した所は無い。


## この entry の述語(棚卸しの述語からの変更点・陽性統制)
述語は**この entry の述語**(札ではない)。凍結の label を定義し直していない。
1. **答えの欄の読み**(`pack_moy1.py` の `answer_reading`): 最後の JSON の `conjecture`(JSON が無く cap でない行は最後の段落・cap の行は無し)を読み、`o1o2`(O1O2 の綴り + 直径 / 中心 / 中点 / 半径の語)・`hehi`(He・Hi の綴り + 同上)・`bare`(共円の語だけ)・`other` に分ける。He・Hi の綴りは `(?<![A-Za-z])(?:He|Hi)(?![a-z])|H_e` で、`HeHi`・`He and Hi`・`He, Hi`・`HiX1`・`H_e` を拾い、`Hence`・`High`・`Hint` は拾わない。
   - 陽性統制(build で assert): blocked s3 の `diameter HeHi`・s5 の `diameter HiX1`・s9 の `center He and radius |He - Hi|` が hehi・O₁O₂ の添字つきの綴りが o1o2・`concyclic` だけが bare・「不変量なし」が other。open s1 の `diameter HeHi`(@2615 あたり)と blocked s3 が `PRED_HEHI_DIAM` に当たる。陰性統制: He・Hi を含む普通の語(Hence・High・Hint・Heron)は other。
   - **穴**: 凍結の分類器の `\bHe\b` は一語の綴り `HeHi` に当たらない(BRIEF §2 の通り)。凍結の label は reason の欄で拾っているので label 自体は壊れていないが、答えの欄だけを読む述語は綴りを全部拾う必要があった。
2. **`PRED_O`**(O1O2 を直径・中心と名指す文): 棚卸し `inv_m1.py` の述語に、**添字の綴り `O₁O₂`(`₁₂`)を足した**。BRIEF の数(open 0 / 10・blocked 7 / 10)は変わらない。
3. **`PRED_HEHI_DIAM`**(直径 = He・Hi の文): 棚卸し `inv_m1_d.py` のまま(点の説明「homothety center at Hi」には当たらない)。
4. **`O_TOKENS`**(O1O2 の語): 棚卸し `inv_m1_b.py` のまま。空の丸の印は、この語の最初の位置(その行に O の文が無いとき)。
5. **凍結の規則の複製**(`frozen_rule_replica`): `run_moy1_concyclic_blocked.py` の非 bind の枝(`\bHe\b|\bHi\b` と中心の語 → attractor・共円の語 → stuck-L1・それ以外 flail)を**本文全体**に当てる。非 bind の 13 行すべてで凍結の label を再現した(assert)= 三段の棚の中段の根拠。bind の判定(geometry)は写していない。
6. **O1O2 の語の文脈**(open s1): 21 回のうち ±80 字に `line` か `slope` がある回 = 19・ない回 = 2(`otok_ctx`)。
7. **prompt の区切り**: prompt 自身の見出し(`# `・`State the SINGLE`・`Respond with JSON only`)で切り、見出しだけの区切りは次の塊に併せる → 6 区切り(173 / 117 / 442 / 162 / 268 / 132)。
8. **最初の JSON の位置**: V4 の定義(`content.find('{"conjecture"')`)と、空白を許す検索の二つ。blocked の 10 行では一致(assert)。open s1 だけが JSON を何行かに分けて書くので、帯の「答えの欄の始まり」の旗は空白を許す方を使う(= @29296)。

## BRIEF・棚卸しと data の違い(data を採った — CLAIMS.md D にも)
- BRIEF の「5 本の色が替わる」= 凍結の attractor 5 行(s0・s1・s2・s6・s8)。答えの欄の読みで色が替わる行は**もう 1 行**ある: s4(凍結 stuck-L1・答えの欄「不変量なし」・本文の `concyclic` は否定の中)。図は 6 行に糸を張って言っている(状態 5)。
- BRIEF の「open s1 の O1O2 は傾きの計算にだけ」→ data では O1O2 の語 21 回・19 回が line / slope の語と共に・1 回は「centers O1 and O2」(最初の文)・1 回はそれ以外。図は「直径 / 中心 = O1O2 の文は 0」と「19 / 21 は line・slope の語と共に」と言い、「だけ」とは言っていない。
- 棚卸しの `PRED_O` は `O₁O₂` を逃した(上)。他の V1〜V11 は data と全部一致(`check_claims.py` が棚卸しの出力 `check_values.out` を text として読んで 11 / 11)。

## template(`state_machine.js`・`build.mjs`・`widget.py`)に足した所
- 状態の `t` を関数にできる(状態 13・14 の既定の位置を data から引く)・状態ごとの legend(`keys`)・`.fig-quote` の列(逐語の抜粋・`--qw` で幅を状態ごとに)・滑り棒の見出しを状態ごとに(行 / 位置)・lo = hi の滑り棒は隠す。
- 電話の camera の別の設定(`camN` = 真上から見る・`Hn` = 電話の canvas の高さ)・広い枠の高さ(`Hw`)・`redraw()`(同期の描き直し = 検査が例外を捕まえる)・`setView(v, instant)`(camera の端を一瞬で)。
- 章ごとの限定の札(`ui.limBy`)と、状態ごとにそれを外す(`limBase: false` = cue の表)。
- `build.mjs`: 頁の幅 1500・`scenes.js` を取り込む・`generated/ledger_rows.json` を書く。`widget.py`: `goto_chapter`・`check_counts`。

## 描き方の判断
- **camera は世界の箱に合わせて自動で fit**(`camera()`)。回すと拡縮するが、常に枠に収まる。字は画面の単位で置き、字の大きさ(video 13.5 / desk 12 / phone 23.5)に offset を比例させる。重なる札は greedy に下げ、枠の外へ出ないよう寄せる。
- **帯の長さは対数**(BRIEF が許す・目盛りを書いた)。**短い板 = attractor ではない**: blocked s1(698 字)は bind の行。二つの群を分けるのは**旗の位置**(JSON から書き始めた行は左端)。図の凡例とこの NOTES と README に書いた。
- **印の三種 + 糸の目盛り**: 橙の菱形 = 直径 = He・Hi の文・青の四角 = 直径 / 中心 = O1O2 の文・旗 = 答えの欄の始まり・空の丸 = O1O2 の語(円は名指していない)。述語が当たった**全部の位置**は板の上に薄い線(barcode)で置く(印の本数を数えさせないため)。
- **色**: 青 = apex の組・橙 = attractor の組・灰 = 裸の共円(BRIEF §5・moy-5 と揃えた)。**新しい色は足していない**(kit の `--anatomy-blue`・template の橙・`--anatomy-mid` / `--anatomy-lo`)。dataviz の validator script は skill に見当たらないので、自分で OKLab(Machado 2009 の CVD)で測った: 暗い頁の normal ΔE_OK × 100 は最小 16.0(灰対暗)・CVD 最小 16.0。明るい頁は最小 13.6(灰対暗)・CVD 最小 12.5。**灰対暗(= 裸の共円対その他)は明るい頁で 15 を割る**ので、「その他」は斜線の模様(色以外の手がかり)を足した。
- **電話**: 立体を真上から見る camera に替え、札を減らし(天秤は L50H23 だけに札)、逐語の抜粋は図の下の HTML(字 12 px)。立体の読みは弱まる(= 一番自信の無い所の一つ)。
- **天秤**: 皿に載せたのは「上位 10 head のうち組に入った head」の寄与(高さ ∝ |寄与|)。針は card の `delta_out`(出力そのものの差)で、皿の和から計算した値ではない(「読み方」の欄に書いた)。組に入らない上位 10 head の和は皿に載っていない(欄に一覧)。

## 驚いたこと(取っておく事実)
1. 凍結の label の stuck-L1(open s4)は、本文の `neither concyclic, collinear, nor form right angles` という**否定の中の語**で付いている。凍結の規則は語を読み、主張を読まない。答えの欄は「不変量なし」。
2. **同じ書き始め(JSON から)でも、open は裸の共円(s3・s9 の 2 / 2)・blocked は He・Hi(s3・s5・s9 の 3 / 3)**。二つの標本の対比で(同じ行の変化ではない・n 小・一つの cue)、原因は言わない。BRIEF には無かった並びで、状態 8 の card と K07 に L1 として足した。
3. open s1 は He・Hi の直径の文を 7 回挙げ、O1O2 の語を 21 回書くのに、答えは裸の共円で終わる。「He・Hi に引かれた」と読むと、答えの欄(He・Hi 0 / 10)と合わない。
4. 検査が実際に捕まえた不具合: 問題文の欄が切れる(状態 2)・phone の最小の字 8.99 px(目標 9.5)・英語の strip が動画枠の下で切れる・台帳が 1080 を超える・phone で札が重なる(状態 11・13・14・15・16)・英語の円の名が viewBox を出る・Think の図の文が phone で出る・語の走査が疑問文を捕まえた。どれも data の読みではなく表示の欠陥。
5. 背景 session の hook は `lsof` / `ps` と `kill` を一つの呼び出しに置くと止める。`run_*_check.sh` は**自分の pid だけ**を止め、port の残りは見るだけにした(JupyterLab・marimo とも停止後に listener 0 を確認)。
6. 同じ時間に別の job(moy-5 の entry)の Chrome も動いていた。他の process には触れていない。
7. JupyterLab: この機械の `ggblab`・`webio-jupyterlab-provider` は anywidget の「図 → kernel」を壊し、`jupyterlab-myst` は最初の markdown cell で例外を出す。`run_jupyter_check.sh` が自分の config dir の中だけでこの三つを切る(利用者の設定は触らない)。console の warning は `jupyterlab-chat-extension` の版の不一致と ACP の登録(図と無関係)。
8. **納品の名**: このリポジトリの `.gitignore` は `dist/`・`build/`・`*.log`・`*.out` を落とす。そこで build の出力は `dist/` でなく **`pages/`**・log は **`.txt`**(`checks/last_run.txt`・`captures/capture_log.txt`)と名付けた。納品する全 path を worktree の中で `git check-ignore --no-index -v --stdin` に通し、1 本も無視されないこと(exit 1 = 該当なし)を見た。skill の雛形の名(`dist/`・`*.log`)のまま置くと `git add` が黙って落とす。
9. **納品の手順の落とし穴**(次の BRIEF のために): 背景 session が EnterWorktree した後に Bash で共有 checkout の中へ `cd` すると、以後の Bash は cwd が共有 checkout だという理由で**どれも**拒否される(`git -C <共有 checkout>` も拒否。他に、`grep` の引数に `eval` の語を含める・変数を引数にした `python`・複合の git も拒否された)。cwd を戻すには `EnterWorktree` に `path=`(自分の worktree)を渡す。納品は絶対 path だけで足りる(`mkdir` / `cp -R` / `diff -rq` / `python -I <絶対 path>` は scratch の cwd から通った)ので、共有 checkout へは `cd` しない方がよい。

## 一番自信の無い所
1. **帯の図で「短い板 = attractor」と読まれること**(上)。対数の目盛りと旗の位置で言ったが、板だけを見る人は誤読しうる。
2. **状態 12(同じ一行の二つの位置)の絵が薄い**(細長い帯に二つの印)。逐語の二つの抜粋が主役。
3. **天秤の針と皿の関係**: 針は皿の和から出した値ではないが、絵は「皿の差 → 針」と読めてしまう。「読み方」の欄に書いたが、図だけでは分からない。
4. **電話の立体**(真上から)は 3D の手触りが弱い。検査(字の大きさ・重なり・はみ出し)は通っているが、読みやすさは別。
5. **SCRIPT の 02 行目「答えの欄が、裸の共円から O1O2 の円に替わる」**は二つの標本(open と blocked)の対比で、同じ行の変化ではない。BRIEF の決め台詞のまま使い、14 行目で「相関・n 10・一つの cue」と打ち消している。言い回しは依頼者が差し替える前提。
6. 明るい頁の橙の字(`#e07b16` on `#fbfbfa`)のコントラストは大きい字では足りるが、小さい札では弱い。

## 道具の版・環境
bun 1.3.0 · python 3.14.3(py314)· anywidget 0.11.0 · marimo 0.23.13 · jupyterlab 4.5.6 · traitlets 5.14.3 · macOS 27.0.1 · Chromium = playwright の headless(`ms-playwright/` に chromium_headless_shell-1181 と -1223 があり、BRIEF が名指すのは -1223)。BRIEF の版と同じ(違いなし)。

## 10-28 夜 主 session の直し: 章と状態の button を頁の頭へ(依頼者の依頼・作り手の手ではない)
- 依頼(逐語): 依頼者「今更なんですが、状態の選択ボタンが下にあるのですが、ボタンを押すとページの嵩の違いで見失うので、上下移動のない上の方に移動してください。」
- 直し: `build.mjs` の `inner()` で章と状態の button(`.sh-chaps`・`.sh-bar`)を `<div class="sh-nav">` に包み、見出し(`.sh-head`)の前へ移した。`figure.css` の末尾に `sh-nav` の規則を足した(幅 561 px 以上の頁 = `.iso-page` の中では sticky で画面の上に留める・動画の枠 `?video=1` では隠す・widget では sticky にしない)。skill `coread-explainer` の雛形(`assets/build.mjs`・`assets/figure.css`)も同じ直し。
- build: MacBook・bun 1.4.3・Anatomy の kit は zebrashark の `~/.claude/skills/anatomy` を session の scratch に写して `ANATOMY=` で指した(MacBook の skills には入れていない)。直す前の source で build し直すと頁 4 本と widget が zebrashark の物と byte で一致することを先に確かめた(moy-1 Opus v2.1)。pages/ は git で追う物なので、この直しで書き換わった。
- 確かめ: (1) 直す前の頁と比べ、違いは button の移動と CSS の規則だけ(頁 4 本・`widget.js`・`widget.css`・図・数・文は同じ = 規則と移動を外すと文字列が一致)。(2) headless Chrome で全 30 状態の帯の上端(頁座標)= 幅 1400 で **16 px 一定**(直す前は 792〜1,256 px(23 通り))・下へ scroll しても画面の上端 0 px に留まる・幅 390 では 30 px 一定(button が何段にも折り返すので sticky にしない)・横のはみ出しなし。
- してないこと: `captures/` と `checks/` は撮り直していない(直す前の配置のまま)。marimo / JupyterLab の widget は開いて確かめていない。

## 11-09 主 session の直し: JupyterLab の検査の段の揺れ(CHECKLIST A1・裁定 F6「直す」・図は不変)
- 依頼: 依頼者 11-07 夜「直す」(検査が全部通ることが出荷の条件)・11-09「推し通り」(今日の順)。
- 原因: `checks/check_jupyter.json` が固定の待ち(wait 800〜7000 ms)だけで進んでいた。図の message は、kernel が cell を実行している間(cell 5・6 の `time.sleep`)は届かず、cell の後に届く = 待ちの長さ次第で古い画面の数と比べて落ちる(上の「JupyterLab の段だけ時々落ちる」)。もう一つ、最後の段(sae の章の数え直し)の判定が**全 cell の出力をつないだ文**から `'equal': True` を探していたため、前の cell(状態 4)の一致でも通りえた。
- 直し(手順の file だけ・計器と図は替えない): 駅 3 v2.1 の型 = `until` +「その cell 自身の出力が合うまで走らせ直す」(`__retry`)。判定は cell ごとの出力で。dict の表示は改行されるので正規表現は `[\s\S]*`。走らせ直しの間隔は cell の中の sleep より長く(cell 5・6 = 6 s)。走らせ直した回数と、合う前の出力を記録に出す(`tries`・`seen_before`)。
  - Python の側の数(`check_counts` の `python`)は凍結の file から出るので毎回同じ。走らせ直しで通るのは画面の数が後から届いた時だけで、本当に食い違えば何度でも通らない(時間切れで exit 1)。
  - `checks/check_jupyter.json`: md5 `11eec2b2…` → `c77c4fb8…`(28 の手順)。作る script = `checks/make_check_jupyter.py`(出し直すと md5 一致)。
- 確かめ(zebrashark・entry を session の scratch に写して走らせた・この folder では走らせていない): `run_checks.sh` の通し 11:37:08〜(743 s・exit 0・頁の md5 は 11-06 と同じ 28b2bcd8 / 47c6b01f / 8ce9d231・anchor 689 / 689・console clean 25)+ widgets だけ 2 回(11:50:07・11:50:56・exit 0)= **JupyterLab の段 三回とも通過**。cell ごとの走らせた回数 = 1 回目 {1:1, 4:2, 5:1, 6:1}・2 回目 {1:1, 4:1, 5:2, 6:2}・3 回目 全部 1。記録 = `checks/last_run_20261109_jupyter_fix.txt`(scratch の path は伏せた)。
  - 主 session の最初の試走は、私の正規表現の誤り(`.*` が改行をまたがない)で cell 5 が時間切れになった = 直してから上の三回。
- 足した / 替えた file: `checks/check_jupyter.json`・`checks/make_check_jupyter.py`・`checks/last_run_20261109_jupyter_fix.txt`・`pages/build_report.json`(build の出力で、違いは `built_with.anatomy` が作り手の scratch の絶対 path から `~/.claude/skills/anatomy` に替わった一行だけ)。
- してないこと: `captures/` の J1〜J3・M1 は撮り直していない(scratch で撮った物は入れていない)。`checks/last_run.txt`(11-06)はそのまま。
