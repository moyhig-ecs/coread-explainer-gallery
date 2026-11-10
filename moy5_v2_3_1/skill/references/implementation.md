# 実装の型(手本の entry を元にした骨組み)

題材に依らない書き方で書く。手本の題材の名前(He/Hi・apex など)は「例:」でだけ出す。動く最小の雛形は `assets/`(合成の data で build → 検査 → 撮影まで通る)。手本の実物は gallery の DOI(10.5281/zenodo.23992312・全版の concept DOI) の entry(読むだけ。書き換えない)。描き方そのもの(等角の camera・四段の陰影・部品)は `anatomy` skill の kit を使い、ここには写さない。

## 目次
1. 骨組みの全体 — file の役割と依存
2. 雛形 `assets/` の使い方と、動作確認の範囲
3. data の経路(数の数え直し五本)
4. 状態の機械(状態表・章の表・hash・番号の振り直し)
5. 立体の描き方(三軸・板・霧・stem・描き順の限界・二つの body を一つの camera に)
6. 平面・台帳・限定の札
7. i18n(文は data の関数・呼び名は一か所)
8. widget(traits・双方向・echo の守り)と demo
9. 隠しの層の読み込み
10. 検査の作り方
11. 枠(video / desk / phone)と撮影
12. 実際に起きた落とし穴

## 1. 骨組みの全体 — file の役割と依存

| 役割 | 雛形 `assets/` | 手本の entry での名前 |
|---|---|---|
| 状態数・章・頁・字の最小 px・枠の大きさ(**番号の唯一の置き場**) | `config.json` | build.mjs の `NSTATES` / `CHAPTERS` と各 file の定数(散らばっていた) |
| data → pack(第一の数え直し・assert) | `pack_data.py` → `generated/pack.json` | `pack_volume.py` → `generated/*` |
| pack を JS で数え直す(食い違えば build が止まる)・`DATA` を出す | `data.mjs` | `data.mjs` |
| 状態表と描画(題材に固有な所は全部ここ) | `figure.js`(`FIGURE.states`・`ctx`・`draw`) | `live.js` の `PRE[]` と `draw*` |
| 状態の機械(camera・軌道・button・key・hash・host API) | `state_machine.js`(`mountFigure(root, host)`) | `live.js` の前半 |
| ja / en の文(data の関数) | `i18n.js` | `i18n.js` |
| 見た目(kit の変数だけ使う・色は足さない) | `figure.css` | `figure.css` |
| 頁 4 本と widget の ESM / CSS を組む | `build.mjs` | `build.mjs` |
| anywidget(traits)と front-end の糊 | `widget.py` / `widget_glue.js` | `<題>_widget.py` / `widget_glue.js` |
| demo | `demo_marimo.py` | `demo_marimo.py` / `demo_jupyter.ipynb` |
| 検査 | `check_claims.py` + `claims_anchors.json` / `list_headings.py` / `make_check.py` / `run_checks.sh` | `check_claims.py` / `make_check.py` / `run_*.sh` |
| 書類の雛形 | `CLAIMS.md` / `NOTES.md` / `README.md` / `SCRIPT_yukkuri.md` | 同名 |
| 内部の層(別 file) | (雛形に無い。§9) | `internal_layer.js` / `.css` / `README_internal.md` |

```
card の JSON(凍結) ─ pack_data.py(assert) ─> generated/pack.json ─ data.mjs(JS で数え直す) ─> DATA ─┐
config.json(章・頁・px・枠) ──────────────────────────────────────────────────────────────────────────┤
i18n.js + figure.js + state_machine.js ──────────────────────────────────────────────────────────────┤
                                                                   build.mjs ─> dist/<4 頁>.html   (kit の pageHtml + 上の三つ)
                                                                              └> dist/widget.js / widget.css (+ widget_glue.js)
widget.py(traits) <-> widget_glue.js <-> mountFigure(root, host) <-> FIGURE(状態表・draw)
検査: check_claims.py(raw から数え直す) / make_check.py(頁 vs raw) / list_headings.py(番号) — どれも pack の結果を信用しない
```

HTML を手で直さない(生成物)。数を頁・台本・書類に手で写さない(全部 data から)。

## 2. 雛形 `assets/` の使い方と、動作確認の範囲

1. `assets/` を `entry_<札>_v1/` に写す。`config.json` の `name`・`chapters`・`pages` を決める。`data/` を札の凍結 JSON に置き換える(**札の script は import も実行もしない**)。
2. `pack_data.py`(読む key と assert)・`data.mjs`(JS の数え直し)・`figure.js`(状態表と描画)・`i18n.js` を題材に合わせて書く。`claims_anchors.json` に anchor を足し、`CLAIMS.md` の id と対にする。
3. `PY=<python3> bun build.mjs` → `PAGE=dist/<頁>.html sh run_checks.sh checks`。環境: `anatomy` skill(kit と `scripts/drive.mjs`)・bun ≥ 1.3(古い node では Anatomy が動かない)・Chromium。
4. **動作確認した範囲**(`assets/_smoke/` の撮影 2 枚 = clean な環境の `run_checks.sh` の出力): 合成 data で build、`list_headings.py` ok、`check_claims.py` 9 anchor・欠け 0、`run_checks.sh` が三つの枠(video / desk / phone)で states(字の最小 px・はみ出し・NaN)・robust(32 通り・例外 0)・chapters(本物の click)・撮影まで全部通り console clean、`widget.py` の import と trait の clamp。**未確認**: 雛形の widget を marimo / JupyterLab で動かすこと(`demo_marimo.py` は構文のみ)。手本の entry では両方通した。

## 3. data の経路(数の数え直し五本)

同じ数を、**互いに独立な**経路で数える。どれかが食い違えば build か検査が止まる。

1. **pack(Python)**: raw の JSON から図に要る key だけを写し、写す時に assert(件数・範囲・照合用の値)。出力は `generated/`。大きい列は blob に圧縮して頁に入れる(手本: 1.4 MB → 0.36 MB)。
2. **`data.mjs`(JS)**: pack の出力を **JS で数え直す**(行数・位置の範囲・median・和)。`expect(条件, 説明)` が偽なら例外で build が止まる。照合用の値(BRIEF の「合わなければ data が正しい」の値)はここと pack の両方に置く(例: 依頼の整数が data では .5 の付いた値 → data を採り、依頼側に知らせる)。
3. **`check_claims.py`(Python・raw から)**: pack を読まず、raw の JSON を **自分で開いて**数え直す。anchor = (id・種類・file・key の path・期待値・注)。種類の例: `json_equals`(値)/ `json_len` / `derived`(raw から計算)/ `pack_equals_derived`(pack の値が raw からの計算と一致)/ `text_contains`(file を**文字列として**読む)。`CLAIMS.md` の主張 id と anchor の対応を双方向に照合し(主張に anchor が無い・anchor が主張に無い、をどちらも落とす)、`anchors checked: N · missing or different: M` を出す。
4. **`make_check.py`(頁 vs raw)**: 頁が実際に描いた readout・表のセル・カードの値を、script が raw の JSON から出した期待値と突き合わせる(例: 状態 22 の表の 24 のセル)。
5. **kernel 側**: widget の `reading`(頁が今映しているものの text と数)を Python で読み、Python の側の model(boolean の検査)と合わせる。

i18n の文は **data の関数**(§7)なので、数を手で書く場所が無い。例外が要る所(固定の注)は、その数が data のどれかを `check_claims.py` の anchor で縛る。

## 4. 状態の機械

**状態表**(`FIGURE.states` / 手本の `PRE[]`)の 1 行 = `{chapter, mode, cam: [az, el, zoom, px], t, auto, ...}`。`mode` は描画の型(`vol` 立体 / `pair` 二つの立体 / `plane` 平面 / `round` 流れ図 / `ledger` 台帳)。camera は状態ごとに持ち、移るとき補間する(`prefers-reduced-motion` では瞬間)。軌道は drag(az・el)。雛形の key: ← → = 状態・`,` `.` = 位置・`l` = 言語。手本は更に `[` `]` = 層・Ctrl/Cmd + wheel = zoom・視点の button(斜め / 横から / 上から)。

**章の表**(`config.json` の `chapters`: `[名前, 最初, 最後]` の並び): 0..N−1 を隙間なく重なりなく覆う(build が検査)。ここから次を**生成**する。型を手で打たない。
- `NSTATE`(= 最後の章の最後 + 1)・`chapterOf(n)`・章の button(`data-go` = 章の最初の状態)・番号の button の群(章ごとに隙間と細線。色は付けない)。
- hash: `^#s?(23|22|…|0)$`(**長い数を先に**。`#s1` が `#s10` に化けない)を N から作る。状態を動かすと `history.replaceState` で `#s<N>`。
- 検査の `CH_GROUPS`(各章の状態数。例 5/10/8/2)・robust の走査範囲・marimo の待ち条件も config から読む。

**番号の振り直し**(状態を挿す・消す)の手順。手本では手作業で 2 回やり、二重ずらしと取り残しが実際に出た。
1. 挿す位置を決め、状態表・i18n の states 配列・章の表を **一度に**直す。各 file で「同時に二重に動かない」ように、置換は file ごとに一回だけ。
2. 状態番号が**文字どおり**書かれている所を grep で全部出す: 描画の `S.state === 24` / 範囲の `>= 15 && <= 22`・fitView の平面の一覧・hash の regex・widget の STATES・検査の NS / CHAPS / CH_GROUPS・robust の `n <= 23`・marimo の `until '22'`・**層の file の状態番号**・URL の例(`#s18`)・README / NOTES / CLAIMS / 台本の表。
3. **見出しの一覧**を出して目で確かめる(`list_headings.py`): 状態番号 → kicker(ja / en が 0..N−1)・状態表の章の並び・`NSTATE`・`CHAPTERS`・`chapterOf` の境・hash regex・widget の STATES。**一つでも合わなければ撮る前に戻る**。
4. build → 全検査 → full run で撮り直し、**古い番号の撮影を捨てる**(`captures/` に別の状態の絵が残ると、審査で取り違えられる)。

## 5. 立体の描き方

- **三軸**: 横 = 位置(書いていく token・1 位置 = 1 slot)/ 縦 = 層(下 → 上)/ 奥 = 計器の順位(**対数**・手前 = 1 位・上限より奥は霧)。`depthY(rank) = DM · log10(min(rank, 1000)) / 3` のような単調な写しを **一か所**に置き、描画と札の両方がそれを使う。
- **板と面**: 統制の帯(eligible)は厚板、帯の外は灰(「統制の外・参考」)。床と奥の壁は細線。カーソルの位置に focus plane(板)を立て、基準の位置(そろえた位置・要の語)に点線の面を立てる。面は `quad(P, [x,0,0], [x,−YT,0], [x,−YT,ZL], [x,0,ZL])`、線は `seg` / `runs`(null で区切る)/ `dots`。
- **霧**: 潰した値(上限超え)は一様な色の板 + 「1000 位より下(潰した値・描き分けない)」の札。個々の値を描き分けない。
- **stem**: 各点から床へ垂線を引く。奥行きは目で読みにくいので、stem と対数の目盛り(1 / 10 / 100 / 1000)で補う。
- **投影**: kit の camera 式(az・el・zoom)で `P.p(x, y, z) → 画面`。`setD(pathName, d, opacity)` が class ごとの `<path>` に `d` を入れ、不透明度は**補間する scalar** `A(name)` で出入りさせる。
- **描き順の限界**: 要素ごとの depth sort はしない。class ごとに「床 → 壁 → 板 → 霧 → stem → 線 → 点 → 札」の固定順で描く。camera が既定の範囲(el 15〜35・az 50〜80 くらい)にある間は正しく、**下から・真後ろから回すと前後が逆になる**。限界は el の clamp で抑え、遮蔽の代わりに半透明(fill-opacity 0.25〜0.7)を使う。この限界は README に書く。
- **二つの body を一つの camera に**(成功と失敗の並べ): 描画を `drawBody(o)` に切り、`setD` を**足し合わせ**(accumulator `ACC` / `TAGS_ACC`・frame の頭で空にする)にして、二つの body を**同じ `P`**で同じ `<path>` へ描く。二つ目の body は投影の傾きの補正 `x · cos az · sin el · k` だけずらして**同じ地面**に置く(回すと両方回る)。body 同士の depth sort はしない(配置で重ならないようにする)。layout は枠ごとに: video は左右(板が高さで決まる)/ desk・phone は縦積み(板が幅で決まる)。canvas の viewBox も layout ごと(`pairVB()`: video は横長・desk は縦長・phone は更に絞って zoom を下げる)。左の目盛りと帯の札は一つの body に付ける。
- **片方にだけ在る部分**(例: 考える欄 <n> token / 0 token): 両方に同じ幅・同じ高さの枠を立て、無い方は点線の空の枠にする(札は同じ位置・同じ大きさ)。幅が縮尺どおりでないなら、その旨を札と凡例に書く。
- **札(tag)**: `mkTag` は端の余白(layout ごとの縮尺 `ms`)を越える札を寄せるか落とす。題の札(`title`)は落とさず端へ寄せる。重なる札は上から順に一行ずつ下げる(de-clutter)。字の大きさは枠ごとに単位が違う(video 13.5・desk 11・phone 17 など)。**実際の px = 字の単位 × `svg.getScreenCTM().a`** で測る(板の縮尺を仮定しない: 平面の図で 1.44 と思い込み、実測 0.8935 だった)。一つの札に二行を足すと、phone で隣の札とぶつかる(§12)。

## 6. 平面・台帳・限定の札

- **平面**(`plane` / `round`): 縦 = 順位の対数(1 位が上)・霧の行・位置の列。行を識別する色は足さない。同じ seed の対は括弧や注で「独立な 2 例ではない」と示す。
- **台帳**(最後の章): HTML(`.fig-ledger`)を `data-chapter="ledger"` のとき出し、svg を隠す。三つの列 = 言える(L1)/ 読み(L3)/ 言えない。各行に出所(file と key)。**言えない**は平叙文で、省かない。
- **限定の札**は章の全画面に出す(枠の下の一行 + 右上の身分の札)。文は `i18n` の `lim()`(data の関数)で、その画面の data に当てはまる範囲だけ書く。
- **カード**(chip の列): 画面に出る値を data から。`k` = 見出し・`v` = 数・`s` = 補足・`tone`(色は既存の変数だけ)。

## 7. i18n(文は data の関数・呼び名は一か所)

- `I18N = { ja: { states: [...], ui, ledger }, en: { … } }`。状態の 1 項 = `kicker`(`状態 N · …` / `State N · …`)・`q`(問い)・`lead()`・`stamp`・`readout(Q)`・`limTag`・`lim()`・`chips()`。数は template 文字列の中で data から出す(`${rank(row, t)}` など)。ja と en で **key と数が同じ**であることを検査する(en だけ数が古い、が起きる)。
- **位置・行・語の呼び名は helper に一か所**で定義する(例: `CMPOS(p, f, cp, en)` = 「そろえた位置 / 分かれ道 / commit の語」)。同じ位置を、ある状態は「分かれ道」、別の状態は「分かれ道の一つ手前」と呼んだ誤りが v5.5〜v5.9 に残った(§12)。呼び名を替えたら、頁の全 text を走査して**旧い呼び名の文脈**が残っていないことを検査する(陽性統制 = 旧い文言が引っかかる / 正しい文言は引っかからない)。
- 禁じ語(「model が考えた・迷った・気づいた・知っていた」など)は `references/wording.md`。頁の text を機械で走査する。

## 8. widget(traits・双方向・echo の守り)と demo

- `widget.py` は `anywidget.AnyWidget`(iframe で包まない)。`_esm` / `_css` は `dist/` の生成物。traits(`sync=True`): `state`(Int・範囲を clamp する validator)/ `lang`(Enum ja・en)/ `t`(Int・−1 = 状態に従う)/ `theme`(dark・light・auto)/ `done`(図が止まった = 撮影・検査が待つ)/ `reading`(Dict = 画面の text と数)。題材に応じて `row`・`layer`・`band` などを足す。状態数は `config.json` から読む(手で打たない)。
- 方向: kernel → 図 = `state` `lang` `t` `theme` / 図 → kernel = 同じ四つ + `done` + `reading`。**両方向を検査する**: 図で押した値が Python に数で戻り、Python で書いた値が図を動かす。
- **echo の守り**(`widget_glue.js` の `stale`): 図が送って既に先へ進んだ値が kernel から戻ってきても、命令として扱わない。marimo は値が変わらない trait にも `change:<name>` を出すので、これが無いと状態が行ったり来たりする。実装 = 送った値と時刻を短い履歴に持ち、1.5 秒以内に同じ値が戻ったら捨てる。
- `render` が返す関数で listener を外し `api.destroy()`(marimo の再描画で積み上がらない)。
- demo: marimo は `mo.ui.anywidget(w)`・JupyterLab は cell の最後に `w`。JupyterLab に別の widget 拡張(例: ggblab)が在ると「図 → kernel」が届かないことがあるので、実機で双方向を確かめる。

## 9. 隠しの層の読み込み

内輪のたとえ(別 file)は、本体が **在れば読む・無ければ何もしない** だけにする。
- file: `*_layer.js` / `*_layer.css` / `README_internal.md`。本体の file に層の語が 0 件(grep で数える)。
- 読み込み: 頁は URL の flag か隠しコマンド(キーの並び)で `host.loadLayer()` が script / link を足す。widget は Python が**求められたときだけ**層の file を読んで `_layer_js` / `_layer_css` の trait に載せる(file が無ければ空 = 本体だけで動く)。層は **classic script**(`file://` でも読める)で、`(window.SHLayers = window.SHLayers || []).push(factory)` と登録する(`factory.layerName` で名指し)。本体は `factory({root, svg})` を呼び、返った `{update(ctx), off(), destroy()}` に状態・言語・位置を渡す。
- 出る状態は層の file の中で決める(例: 17 / 21 / 24)。**番号は file の中に文字で書かれる**ので、振り直しの対象(§4)。層が on のとき、層の乗らない状態には badge だけ。既定 off・日本語の頁だけ・英語の頁は何もしない。右上に「内部の層・外には出さない」。
- 検査(`run_layer.sh` の型): 既定 off / コマンドで on・off / 英語で無反応 / 層の file を消しても本体が動く / 層の乗らない状態で panel が出ない / **陽性統制** = 乗る状態では出る。

## 10. 検査の作り方

- **一つの config から作る**: `make_check.py` が `config.json` から action file(`check_states` / `check_robust` / `check_chapters` / `check_capture` …)を書き、`anatomy` の `scripts/drive.mjs`(headless Chrome: `eval` `click` `key` `wait` `shot`)で走らせる。頁の中の `eval` が throw すれば drive が非 0 で終わり、`console:` の行が console error を数える。
- **MEASURE**(状態ごと): 札の最小 px = 字の単位 × svg の縮尺 を `config.json` の `minpx[枠]` と比べる / viewBox の外の文字 0 / path に NaN 無し。目安 video ≥ 10・desk ≥ 10・phone ≥ 9.5。**閾値は較正する**(phone は板が 290〜330 px しかない。viewBox を絞り、字を大きくし、kit の四隅の文を縦の列に直して初めて通る)。
- **robust**: 全状態 × ja / en × t ∈ {0, 3, 99, −5}(範囲外も)で例外 0。題材が増えたら行・層・帯の軸を足す。
- **章の button は本物の click**: api 呼び出しでなく `click` で、着いた状態・選ばれた見た目(`aria-pressed`)・hash・ラベル・番号の群の大きさを確かめる。**click の順は「最後の章 → … → 最初の章」**(どの click も状態が変わる)。`?video=1` は button を隠すので、この検査は desk と phone で走らせる。theme の `◐` の click は頁が viewport より長いと外に出るので、明るい頁(`-light`)を開いて撮る。
- **計器は較正してから使う**: 新しい検査は、壊した入力で落ちること(陽性統制)と、正しい入力で通ること(陰性統制)を一度見る。`text_contains` が JSON を文字列でなく dict と比べて黙って落ちた、が実際にあった。
- **番号**: `list_headings.py`(§4)を `run_checks.sh` の頭に置く。
- **公開の柵**: 本体の file の内部の語を grep で数える(0 件)。層の file は除く。
- 返す前に、通った検査を**数で**書く(anchor N・missing 0 / robust の combos・errors / 枠ごとの最小 px)。

## 11. 枠(video / desk / phone)と撮影

- 枠は `config.json` の `frames`: video 1920 × 1080(`?video=1` で chrome を隠す。**ちょうどその大きさ**)/ desk 1440 幅 / phone 390 幅。layout の規則: **video は横**(板が高さで決まる)・**desk と phone は縦**(板が幅で決まる)。
- 撮影の名前: `video_s<N>[a|b].png`・`page_<dark|light>_s<N>[_en].png`・`phone_dark_s<N>.png`。瞬間を見せる状態は前後二枚。小さな直しは影響する状態だけ撮り直し、何を撮り直したかを `captures/capture.log` と NOTES に残す。
- 撮影は `shot` の action(selector `.sh` か `html` + clip)。撮る前に `done` が立つまで待つ(補間中の絵を撮らない)。
- 台本(`SCRIPT_yukkuri.md`)は script(`make_script.py` の型)が data から作り、長さを数える(≤ 150 秒・1 秒あたりの字数 + 行間)。台本の数も data から。

## 12. 実際に起きた落とし穴

1. **板の縮尺の仮定**: 平面の図の縮尺を幅 / viewBox 幅 = 1.44 と思い込んだが、高さで決まって 0.8935。px は CTM で測る。
2. **CSS の順**: phone 用の `@media` を基の規則より前に書くと、同じ特異性で後の基の規則が勝って効かない。media は基の規則の**後**に置く。
3. **kit の四隅の文**(title / readout / hint)は絶対配置。phone では重なるので `position: static` の縦の列にし、hint は隠す。
4. **viewBox に 5 つ目の数**を混ぜて(余白の倍率)無効になった → 文字列にするとき先頭 4 つだけ。
5. **振り直しの取り残し**: robust の走査範囲・marimo の待ち条件・層の file の状態番号・`ctx.state !== N`。§4 の grep を使う。
6. **呼び名の揺れ**: 同じ位置を二つの名で呼んだ(§7)。呼び名は helper に一つ + 走査の検査。
7. **brief の数が data と違う**(整数と .5 の値・依頼の値と data の値の食い違い): data を採り、依頼側に知らせ、`data.mjs` の期待値を直す。
8. **phone の札の二行**: 札に二行目を足すと、隣の body の札(考える欄など)とぶつかる。phone だけ一行にし、言い足りない分は凡例とカードに置く。
9. **ledger の枠はみ出し**: 1920 × 1080 の台帳は文が長いと溢れる。詳細は出所の行(`src`)へ回し、本文の一行は短く。
10. **chapter button が video で隠れる**ので click の検査が落ちた(§10)。
11. **theme の click が viewport の外**(背の高い頁)。明るい頁を直接撮る。
12. **echo の往復**(§8)・**clamp**(範囲外の `state` を Python から書いたとき)。
13. **但し書きが根拠の計器の測った範囲を越える**: 「予告が混ざりうる」と書いたが、その計器(札の名は伏せる)が測ったのは「次に書く語」だけで、説明したい語はその次だった。但し書きは、根拠の計器の定義(どの語までを測ったか)を data で確かめて書き、範囲外は「未測」と書く。**距離の数え方は図全体で一つ**にする(読みの位置の距離 = その位置の読みが次に書く語を決める)。「N token 先」のような書かれる token の数え方を混ぜると、同じ語が +1 と 2 token 先に見える。凡例に定義を一行、頁の text の走査で「N token 先」を禁じる(v5.12)。「次に」「これから」の相対語は基準の位置を data から出す。
14. **文の重なり・はみ出しを ja だけで確かめた**: 平面の文が en で viewBox の右端をはみ出していた。重なり(bbox の交わり)とはみ出しの検査は、ja・en と全部の枠で走らせる(§10)。

## 付記: 手本との差(雛形が省いたもの)

雛形は「動く最小」で、次を持たない: 実際の計器の data・成功と失敗の立体のそろえ方の細部(`pairLayout`・`mkTag` の端の定数・補間)・台帳の本文・隠しの層の実物・JupyterLab の検査・台本の長さの計算。必要になったら 手本の entry の該当 file を読む(`live.js` の `drawBody` / `drawCommitPair` / `pairVB`・`internal_layer.js`・`run_layer.sh`・`make_script.py`・`<題>_model.py`)。
