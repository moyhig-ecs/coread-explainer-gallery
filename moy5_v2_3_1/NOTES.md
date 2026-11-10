# NOTES — entry_v2_3_received(駅 3 = moy-5 の受領版 v2.3・2026-11-09・作り手一人 = Opus 5.5 xhigh)

- **開始 = 2026-11-09 18:19:33**(最初の command の `date` の出力・zebrashark)。起こした時刻 = 18:19(主 session)。打ち切り 60 分 = 19:19。
- **依頼** = 依頼者 11-09 18:1x「今すぐでなくてもいいのですが、moy-5の円錐断面が直線FVDを鉛直に切る平面だとわかるように図示する。次回から。」→「順序でいうと、公開前に切断平面は図示したい」。依頼書 = `../../BRIEF_v2_3_moy5_cutting_plane_FVD_20261109.md`(頭の HEAD(R1) 67c07546)。
- **土台** = `../entry_v2_2_received/`(scratch `<scratch>` に `cp -R`・元は書き換えていない)。比べのために同じ土台をもう一つ写して build(`base22/`・頁の md5 6a4d444f ja · 9df3b0b2 en · widget.js 62a167d0 = v2.2 の NOTES の値と一致)。git は書いていない。
- 読んだ物: 依頼書・skill(coread-explainer の SKILL.md v0.2.2 は決まりだけ・殻への載せ替えはしない)・v2.2 の NOTES / README / config / figure.js(重ね描きの節)/ check_claims / make_anchors_v22 / make_check(V22)/ run_*.sh / pack_data の作図の節 / i18n の凡例の行・SOURCE 10-14 の座標(check_claims が読む行)。**読んでいない・使っていない物**: memory・実験の script(import も実行もしていない)・model・通信・install・subagent・Fable。
- 道具(zebrashark): bun `<home>/.bun/bin/bun`(1.3.0)・python `<home>/miniforge3/envs/py314/bin/python3`(-I)・Chrome headless(profile = scratch の `tools/chrome_tmp/`)・anatomy = `~/.claude/skills/anatomy` の 689dcf9(checkout は変えていない)。drive は kit の `drive.mjs`(+ `chrome-port.mjs` · `line-ends.mjs`)を scratch の `tools/anatomy/scripts/` に写し、2 か所(`DRIVE_PORT`・`DRIVE_TMP` を環境変数で)だけ替えた。port: drive 28701・JupyterLab 28780(kernel 28781〜28785)・marimo 28790(依頼書の 28700〜28799 の内)。

## v2.3-1. §1 の値と、三経路で計算し直した値(凍結の座標 SOURCE 10-14 から・作図 = data でない)

| 量 | 依頼書 §1 | ① pack(`pack_data.py` の assert・`construction.plane`) | ② 頁(`FIGURE.planeCheck(0)` = 描いた物) | ③ `check_claims.py` kind `plane`(別の code) |
|---|---|---|---|---|
| j の向きの単位 u(F → V → D) | (0.992546, 0.121874) | (0.9925455, 0.1218745) | 同じ | 同じ(K435 / K436) |
| V の j からの離れ(問いの V = 4 桁に丸めた座標) | 4.1e−05 | 4.0950e−05 | 4.0950e−05 | 4.0950e−05(K437) |
| D の j からの離れ(D = 弦 GE と j の交点) | 0 | 2.2e−16 | 2.2e−16 | 0.0(K438) |
| t_V / t_D(F から j に沿って) | 0.500007 | 0.5000066 | 0.5000066 | 0.5000066(K439) |
| \|FV\| · \|FD\| | 2.3094 · 4.6188 | 2.309421 · 4.618780 | 同じ | 同じ(K440 / K441) |
| A から j の距離(= 円 c の半径 r 4) | 4.000018 | 4.0000180 | 4.0000180 | 4.0000180(K442) |
| AF ⟂ j(\|unit AF · u\|) | 0 | 0.0 | 0 | 0.0(K443) |
| 描いた放物線の標本の数 | ≥ 20 | 41 | 41 | 41(K444) |
| 標本の面からの最大の離れ | ≤ 1e−6 | 1.8e−15 | 1.8e−15(t = −6〜6 でも同じ桁) | 0.0(K445) |
| 標本が円錐の上(\|軸との角 − 30°\| rad・依頼書の外の足し) | — | 5.5e−06 | 5.5e−06(t = −6〜6 の最大 7.1e−06) | 5.5e−06(K446) |
| 面の法線 · 板の法線(描いた長方形の二辺の外積から) | 0 | 0.0 | 0 | 0.0(K447) |

- ② と ① は全部の量で 1e−9 以内(実測の最大 8.9e−16・`check_v23` の `pack_vs_page_max`)。③ は SOURCE から別の code で計算し直した(pack も figure も読まない)。
- 放物線は v2.2 と同じく **頂点 = j ∩ g(計算した V)** から描く。問いの V(4 桁に丸めた座標)は j から 4.1e−5 離れていて(§1)、そこから描くと面から 4.1e−5 離れる = 陽性統制の一つ(下)。§1 の「V は FD の中点」の 0.500007 は問いの V の値。
- **陽性統制**(三経路とも): ① pack は「丸めた V から描いた放物線」と「1e−3 rad 傾けた面」を assert で捕まえる ② 頁は「標本一つを 1e−4 ずらす」「丸めた V から描く」「1e−3 rad 傾ける」を捕まえる(1.0e−4 / 4.1e−5 / 1.0e−3 > 1e−6)③ `check_claims.py --calibrate` は kind `plane` の 13 本全部で「expect + 1 が落ち、正しい値が通る」+ 同じ三つの仕込みを捕まえる(3 / 3)。

## v2.3-2. 何を足したか(図の層の中に一枚 + 名 4 つ + 凡例の一行)

- **切り口の面**(`figure.js` の `cutPlane` → `coneOverlay` の中・既定 = 表示・v2.2 の切り替え(頁の「円錐を重ねる」/ `?cone=0` / widget の trait `cone`)に従う): 直線 FVD(線 j)の上に、板から鉛直に立つ半透明の長方形。
  - **大きさ**(座標の単位・t = 0): j に沿って s = −7.33〜+5.22(F から測る・放物線の端 H の s = −6.73 の 0.6 手前から、D の s = +4.62 の 0.6 先まで = 幅 12.54)、高さ 10.08(= 描いた放物線の最高点 HP_y 9.136 × 1.06 + 0.4)。P_x を動かすと H と HP_y が動くので、面の幅と高さも描いた放物線に合わせて動く。
  - **色**: 塗り = kit の灰 `--anatomy-hi` の 11 %・縁 = 同じ灰の 0.9 の細い線(新しい色は足していない = dataviz の ΔE の検査は要らない。青 = apex・橙 = Descartes・灰 = 床 の意味はそのまま)。
  - **描き順**: 円錐(膜・母線・輪郭)→ Dandelin 球 → 接触円 → **面** → 準線 → 切り口の放物線(膜 + 線)→ 倒す点線 → 名。球と接触円はこの camera(az 62°)では面の奥(面の法線の球の側は depth が小さい = 遠い)なので面より先に描き、放物線は面の上に乗るように後に描いた。
  - **準線** = D を通る面の中の鉛直の線(強い灰の破線・板から面の上端まで)。**焦点 F・頂点 V** = 板の上(面の下の縁)に小さな輪(半径 5.2)。
  - **面の中の名**(desk / video): 「切り口の面」(上の縁の下・真ん中)・「焦点 F」(F の上・放物線の内)・「頂点 V」(V の上・放物線の右 = E の名を避ける)・「準線」(準線の上の方の右)/ en: the cutting plane · focus F · vertex V · directrix。名ごとに候補の場所を並べ、板の点の名・線の名・v2.2 の重ね描きの名の箱(字の幅の見積り)と重ならず viewBox の内に入る最初の場所に置く(P_x を動かすと P_x の名が頂点 V の右へ来る・P_x を負へ大きく動かすと面の上端が枠の外へ出る = その時は下の候補へ)。phone は v2.2 と同じく重ね描きの名を描かない(FS 30 で重なる)= 凡例の行に名を足した。
- **凡例の一行**: 「切り口の面 = 直線 FVD(線 j)を通り、板に鉛直(作図・data でない)」/ "the cutting plane = through the line FVD (line j), perpendicular to the board (drawing, not data)"(依頼書の文のまま)。phone だけ「· 面の中に 焦点 F(球との接点)· 頂点 V · 準線(D を通る鉛直の線)」を足した行。**凡例の中の順**: 面の行を重ね描きの行の前に置いた(後ろに置くと en の video で最後の凡例の行が長くなり、板の右下の隅の字「作図の陽性統制: …」の下に入った = 下の検査で捕まえて並べを替えた)。
- **変えていない物**: 文(見出し・問い・lead・readout・chip・限定・最下行・札の pill・身分)・数・ほかの状態・v2.2 の重ね描きの部品と名の位置・camera・状態 29 の台帳。状態 0・7 の限定の行の「円錐・Dandelin 球の重ね描き(既定 = 表示)も作図」は、面も重ね描きの一部なのでそのまま。
- 変えた file: `figure.js`(`cutPlane`・`planeCheck`・`packPlane`・重ね描きの中の面と名・名の箱 `boxOf`・凡例の key)· `i18n.js`(key `cplane` / `cplane_ph` ja / en)· `figure.css`(`.cut-plane` · `.cut-dir` · `.cut-pt` · `.pl.planel` · 凡例の見本)· `pack_data.py`(第一経路)· `check_claims.py`(kind `plane` + calibrate)· `make_anchors_v23.py` → `claims_anchors.json` + `CLAIMS_v23.md`(新)· `make_check.py`(check_v23・撮影 v23・dump)· `compare_v22.py`(新)· `run_checks.sh`(check_v23 の段・`BASE22` の比べ・`capture23`)· `README.md`。

## v2.3-3. 検査(最後の通し = `checks/last_run.txt`・18:40:48〜18:56・頁の md5 482aa201 ja · d33999e5 en · widget.js 81f1f822)= `run_checks: PASS`

- 通しの command: `DRIVE=<scratch の drive.mjs> DRIVE_PORT=28701 … JUPYTER_PORT=28780 MARIMO_PORT=28790 BASE22=<v2.2 の build> caffeinate -i -m sh run_checks.sh capture23`。
- `check_claims.py`: anchors **447 / 447**(v2.2 の 434 + v2.3 の 13 = K435〜K447)· missing or different **0**。`--calibrate`: **19 kind で 19 / 19**(新しい kind `plane` を含む)+ kind `plane` の 13 本全部で 13 / 13 + 仕込みの誤り 3 / 3。list_headings ok・台本 23 行 146.7 s(v2.2 のまま)。
- v2.2 までの検査は全部そのまま通過: check_states(31 状態 × ja / en × video / desk / phone + 明 + reduced = 8 回 × 31 = 248 画面で MEASURE 失敗 0 = 1080 の枠と最下行・字の最小 px・viewBox の外の文字 0)· robust 6 回 × 496 通り 例外 0(重ね描きの 表示 / 非表示 × t = 0 / 3 / 99 / −5 = 面も通る)· 章の button 4 回 · 使わない語の走査 2 回(陽性統制つき・面の名と凡例の行を含む)· page-vs-raw(142 帯)· check_v21 2 回 · check_fit_control · **check_v22 5 回 × (MEASURE 6 + v22_ok 6)**(重ね描きの往復で文字が変わらない・部品・線の名 5・v2.2 の幾何)· check_v22_click 2 回。
- **check_v23**(依頼書 §2-2 / §2-3・video ja / en・desk ja / en・phone ja / en・明 desk の **7 回 × v23_ok 8 + geom23_ok 1**): 状態 0・7 × 重ね描き 表示 → 非表示 → 表示(状態 0 は t = −5 / +5 も)。① 幾何 = 上の表(t = −6〜6 の 13 点・pack と 1e−9 以内・仕込み 3 つを捕まえる)② 描いた物 = 表示の時だけ面 1・準線 1・輪 2(非表示で 0)/ 描き順(球・接触円の後、放物線の前)/ 描いた放物線の頂点 41 個が全部、描いた面の四角の中(画面の座標で 0.5 単位)/ 準線の両端が面の下の縁と上の縁の上 / 面の中の名 4 つ(phone 0・phone の凡例の行に「焦点 F」)/ 図の字の重なり 0(t = 0 は全部の字の組・t = ±5 は面の名を含む組)/ 面の凡例の行が板の隅の字の下に入らない / 陽性統制 = 面の外に置いた点・字とそれ自身・隅とそれ自身を捕まえる。
- **v2.2 と比べ**(`compare_v22.py`・`BASE22` = scratch で build した v2.2): 全 31 状態(+ 状態 0・7 の非表示)× ja / en × video / desk / phone = **6 回 × 33 の dump で、頁の文・svg・凡例の hash が同じ 31・違う 2 = 0/on と 7/on だけ**(違うのは面の svg と面の凡例の行)。= 重ね描きの無い状態と、状態 0・7 の非表示は v2.2 と文字も絵も同じ。
- **marimo**: 図 → kernel・kernel → 図(状態 10 の数え直し)・cone off → 図の重ね描きが消える・図の button → kernel の `cone` が True。**JupyterLab**: kernel → 図・状態 10 の数え直し(1 回目)・図 → kernel(状態 18・2 回目 = v2.2 と同じ型)・`w.cone = False` → 図・図の button → kernel `cone True`(1 回目)。止めた後の listener 0(28790 / 28780)・自分の pid の生き残り無し・notebook は出力の無い版に戻した。
- console: 42 回 clean(JupyterLab の warning 3 行 = 図と無関係な拡張の版の不一致・v2.2 と同じ)。

### 検査で見つけて直したこと / 直していないこと

- **直した**: 面の凡例の行を重ね描きの行の後ろに置いた最初の版では、en の video で最後の凡例の行(「the cutting plane = …」)が板の右下の隅の字「Drawing control: …」(en は二行)の下に入った(撮影で見つけ、`check_v23` に「面の凡例の行 × 板の隅の字」の箱の重なりを足して捕まえた)→ 面の行を重ね描きの行の前へ移した(最後の行 = v2.2 と同じ「the cut …」)。また、面の中の名の最初の置き方では t = +5 で「頂点 V」が P_x の名に重なり、t = −5 で「切り口の面」「準線」が枠の外へ出た → 候補の場所 + 箱の重なりと viewBox の内の判定で置く形にした。
- **直していない(v2.2 からある・依頼の外)**: en の頁で、v2.2 の凡例の行が板の右下の隅の字に数 px 触れる所が二つある = desk en の重ね描き 表示(最後の行「the cut …」と「Drawing control: …」が約 7 px 重なる・v2.2 の desk でも同じ)と video en の状態 0 の 非表示(一行目「the lines h1, …」の右端と隅の字・`video_s0_off_en.png` に写っている)。v2.2 の検査(MEASURE は svg の字だけを見る)は HTML の凡例と隅を比べていなかった。直すと状態 0・7 の非表示の頁が v2.2 と変わる(依頼書 §2-3)ので直さず、`check_v23` では面の凡例の行だけを判定にし、ほかの行の触れは数だけ出す(`v22_key_lines_under_a_corner`: video en 1・desk en 5 = 状態 0・7 の段の数)。直すなら、板の状態で凡例の下に隅の字の高さの余白を取る CSS 一行(全状態の頁の比べを取り直す)。
- 板の点の名の重なり: phone の t = +5 で v2.2 の点の名同士(A | P_y・E | P_x)が重なる(面の名は phone では描かない = v2.3 と無関係)。`check_v23` は P_x を動かした時は面の名を含む組だけを判定にした。

## v2.3-4. 撮影(依頼書 §2-4)

- 撮り直した = **6 枚**: video ja = `video_s0.png`・`video_s7.png`・`video_s0a.png`(P_x = −5)・`video_s0b.png`(P_x = +5)/ video en = `video_s0_en.png`・`video_s7_en.png`(全部 1920 × 1080・`checks/check_capture_v23*.json` = `run_checks.sh capture23`)。md5: 8d34a197 · 63be1d52 · d90aeba9 · 4baa4118 · 665faa2b · 4da64c95(v2.2 は 44110a9a · 33571dc4 · 1de6cde3 · 4452bc06 · e0ec4c04 · 35a24705)。見たのは video ja の 0・0a(t = −5)・0b(t = +5)・7 と en の 0・7。
- **写し(撮り直していない)** = ほかの 63 枚(`video_s0_off*` · `video_s7_off` は面が出ない = v2.2 と同じ絵・状態 29 も v2.2 と同じ)。widget の段が毎回撮る `marimo_s10.png` · `jupyterlab_s18.png` は、通しで撮れた物を scratch(`work/widget_shots_v23/`)に退け、v2.2 の写しに戻した(md5 6424fd19 · 9d87ab8b = v2.2 と同じ)。`captures/capture.log` = 69 枚(video 67 枚は全部 1920 × 1080・missing 0)。

## v2.3-5. 作り手が決めたこと(L3)・所要・一番自信の無い点

- **面の幅**: 依頼書の「j の上で放物線が描かれる範囲を少し越える」を、放物線の範囲(H〜V)に **D まで**を足して読んだ(準線 = D を通る面の中の鉛直の線を面の中に描くため)。面は放物線の範囲より D の側へ 2.9 単位長い。
- **面の高さと P_x**: 面は描いた放物線に合わせて P_x と一緒に伸び縮みする(t = −5 で上端が枠の外へ出る = v2.2 の P_y と同じ)。固定の大きさの面にする読みもありうる。
- **球・接触円は面の奥・円錐の膜は区別しない**: 半透明の重ねで depth sort はしない(README の限界に一行)。
- **phone**: 面の中の名を描かず、凡例の行(phone だけの長い版)に名を書いた(v2.2 の phone の決めに合わせた)。
- **所要**: 開始 18:19:33 → 最後の通し PASS 18:56 → 置き場への写し 18:57:36 → 置き場で check_claims 447 / 447・calibrate 再確認 18:57:41 → DONE 18:57:51(約 38 分)。打ち切り 60 分の内。token の量は測っていない。
- **一番自信の無い点**: en の頁の凡例と板の右下の隅の字が触れる所(v2.2 からの二つ・上)を直さずに残したこと。v2.3 の撮り直した 6 枚には写っていないが、写しの `video_s0_off_en.png` と desk en の頁には在る。次点: 面の幅に D までを入れた読み(依頼書の「放物線が描かれる範囲を少し越える」より広い)。

---

(以下は v2.2 の NOTES をそのまま残す)

# NOTES — entry_v2_2_received(駅 3 = moy-5 の受領版 v2.2・2026-11-07・作り手一人 = Opus 5.5 xhigh)

- **開始 = 2026-11-07 22:50:16**(`date` の出力)。打ち切り 90 分 = 00:20。45 分の目安 = 23:35。
- **進み具合(42 分・23:32・45 分の少し手前に書いた)**: 重ね描き・線の延長・切り替え(頁 / widget)・§1 の幾何の anchor 6 本・check_v22 / check_v22_click は済み。一回目の通しは MacBook の短い sleep(pmset 23:13)で drive の CDP が切れて止まり、二回目(caffeinate -i)は頁の段が全部通過・marimo の cone の段だけ検査の組み方の誤りで落ちた(直して widget の段は通過)。残り = 最後の通し(撮影つき)と widget の段 二回・置き場への写し。
- 依頼書 = `../../BRIEF_v2_2_moy5_board_cone_overlay_20261107.md`(頭の HEAD(R1) 758ac5d0)。土台 = `../entry_v2_1_received/`(scratch `<scratch>` に `cp -R`・元は書き換えていない)。git は書いていない(読みは、納品の前に置き場の folder の状態を `git status --porcelain` で一度だけ見た)。
- 読んだ物: 依頼書・skill(coread-explainer の SKILL.md・references/checks-and-captures)・v2.1 の NOTES / code(figure.js · state_machine.js · build.mjs · widget · make_check.py · check_claims.py · run_*.sh · i18n.js の該当行)・SOURCE 10-14 の座標(check_claims が読む行)。**読んでいない物**: memory・実験の script(import も実行もしていない)・model・通信・install・subagent: なし。
- 道具(この MacBook): bun = `<home>/.local/bin/bun`(1.4.3)・python = `<home>/miniforge3/envs/py314/bin/python3`(-I)・Chrome headless(profile = scratch の `tools/chrome_tmp/`)・anatomy = `~/.claude/skills/anatomy` の 689dcf9(checkout は変えていない)。drive は kit の `drive.mjs` を scratch の `tools/anatomy/scripts/` に写し、v2.1 と同じ 2 か所(`DRIVE_PORT`・`DRIVE_TMP`)だけ替えた(v2.1 の写しと diff 0 を確かめた)。port: drive 27901(下見 27911〜27918)・JupyterLab 27980(kernel 27981〜27985)・marimo 27990。node は使っていない。

## 1. §1 の読みは座標と合ったか(二経路)

- **合った(合わない所なし)**。凍結の座標(SOURCE 10-14: A (0, 0)・r 4・C (6.3891, 4.8145)・G・E・F)で:
  - C は G の接線 f と E の接線 g の上(距離 7.6e−5・丸めの桁)= **C = 円錐の頂点**。|CA| = 8 = 2r → **半頂角 30°**(29.999998°)。J は g の上 = **CJ は母線**。
  - F = −G(G の対蹠点・差 0)→ AF ⟂ j・|AF| = r = **j は円に F で接する**(切断面は球に F で接する = 焦点)。
  - GE ⟂ CA(内積 4.4e−6)・GE の中点 = C + (3/4)(A − C) = 接触円の中心(半径 2√3)。D = GE ∩ j = 接触円の面と切断面の交わりの足 = 準線は D を通り画板に垂直、e はそれを画板に倒した物。V は FD の中点(VF = VD = 2.309)。
  - 切断面(j を通り画板に垂直)の放物線を H の上に HP_y だけ持ち上げた点は**円錐の上**(軸との角 − 30° = 4e−6 rad)で、凍結の J を通る軸に垂直な円の上(H はその面の上・|P − M| = ρ)= Menaechmus の円。画板の P_y は、その点を j の周りに倒した物。
- 経路: ① 作り手の下見(scratch の `work/geom.py`・置き場に入れない)② 頁の JS `FIGURE.coneCheck(t)`(t = −6〜6・`check_v22` の GEOM)③ `check_claims.py` の kind `cone`(SOURCE から別の code で計算し直す・anchor K429〜K434・CLAIMS_v22.md)。②と③の値は桁まで一致(C_on_f 7.566e−5・GE ⟂ 4.375e−6・半頂角 29.99999765857537)。

## 2. 何を足したか(図の層一つ + 線の延長 + 切り替え一つ)

- **重ね描き**(`figure.js` の `coneOverlay`・既定 = 表示): 画板の上の半分に、円錐(頂点 C・軸 C → A・凍結の J を通る軸に垂直な面まで = CJ が母線一本まるごと・母線を 30° ごと・見かけの輪郭の母線二本を少し濃く・底の円は破線 = 描くのを止めた所)・Dandelin 球(この camera は正射影なので輪郭は半径 r·SCL·k の円 = その上半分 + 画板の大円の手前半分)・接触円(G から E へ上半分)・切り口の放物線(V から H の上の P_y まで・薄い膜で j まで)・倒す点線(j の周りの四分円 = 持ち上げた P_y → 画板の P_y)。名(円錐(頂点 C)・Dandelin 球(中心 A)・接触円・切り口の放物線)は desk / video だけ(phone は FS 30 で重なるので凡例に)。色は足していない(kit の灰の段だけ)。
- **凡例**: 「線 h1・e(準線)・j・f・g は画板の端まで」(常に)・「重ね描き(作図・data でない): 画板 = 円錐(頂点 C・母線 f · g)の軸を通る面 · Dandelin 球(中心 A)· 接触円(G · E)」「切り口(j を通り画板に垂直)の放物線 · 点線 = 画板に倒す(P_y)」(表示の時だけ)。限定の行(状態 0・7)に「円錐・Dandelin 球の重ね描き(既定 = 表示)も作図」。台帳 2/3(状態 29)の既存の「言えない」の行に一文(「状態 0・7 の円錐・Dandelin 球の重ね描き(既定 = 表示・切り替えで非表示)は凍結の座標から計算した作図で、model の振る舞いについて何も言わない」)= 行は足さない(言えない の数 = readout を変えない)。
- **線の延長**(依頼書 §2-2): h1(V を通り e に平行・P_x はこの上)・e(D を通り j に直交 = 準線)・j を画板の端まで(板の縁の 3 単位内で切る)、f・g は頂点 C から画板の端まで(C の向こう = 別の nappe は描かない)。どの線も自分の上の点(g の J・e の K・j の H・h1 の P_x)が板の外へ出たらそこまで延ばす(P_x を動かした時)。線の名 = h1・e(準線)/ e (directrix)・j・f・g(phone は「e」だけ・凡例に「e(準線)」)。v2.1 は h1 を V の周り 7 単位・e を 11 単位・j を H〜D・f を C〜G の 2.5 先・g を C〜J で描いていた。
- **切り替え**: 頁の操作列に button「円錐を重ねる」/ "cone overlay"(aria-pressed・状態 0 / 7 だけに出る = P_x の slider と同じ扱い)・頁の `?cone=0`・engine の `setCone`・widget の trait `cone`(Bool・既定 True・両方向)。重ね描きは絵の層だけで、文字(見出し・lead・readout・chip・限定)は切り替えに依らない(検査した)。
- **camera の小さな直し**: 円錐の上端が viewBox の上で切れたので、状態 0・7 の camera の中心を板の上 22 単位に(板が枠の中で約 32 px 下がる)・phone の切り出しを 36 単位上に。表示 / 非表示で板は動かない(同じ camera)。重ね描きの bbox(t = 0)= desk / video [156, 29, 789, 505] ⊂ [0, 0, 1180, 700]・phone [355, 46, 922, 498] ⊂ [210, 28, 970, 628]。

## 3. 作り手が決めたこと(L3)

- **円錐をどこで切って描くか**: 凍結の J を通る軸に垂直な面まで(= CJ が頂点から縁までの母線一本)。この面は H も通り(H − J は GE に平行 = 軸に垂直)、持ち上げた P_y もこの円の上 = 図の P_y と J が同じ一つの円(Menaechmus の円)に乗る。P_x を動かしても円錐は動かさない(円錐は C・A・r だけで決まる・切る高さは描き方の決め)。P_x を動かすと切り口の放物線と倒す点線だけが動く。J を動く J に合わせて切ると、t = −6 で母線 36 単位(円錐が枠の数倍)・t = +6 で 10 単位(球を切る)になり、何を見ているかが揺れる。
- **切り口の放物線を描いた**(依頼書 §2-1 の任意): 身分は凡例で「作図・data でない」・名は「切り口の放物線」。倒す点線(j の周りの四分円)は「画板の P_y = 切り口の P_y を画板に倒した物」を見せるため。準線を立てた位置(D を通る画板に垂直な線)は描いていない(線が混むため・凡例の「e(準線)」と §1 の読みで足りると見た)。
- **phone では重ね描きの名を描かない**(FS 30 で絵の上に重なる)。凡例(HTML)に同じ名が在る。線の名は phone でも描く(e は「e」だけ)。
- **台帳**: 依頼書の「README と台帳に一行」= README の頭と「見方」・CLAIMS_v22.md の頭・図の台帳 2/3(状態 29)の既存の「言えない」の行の末に一文。図の台帳は行を足さず既存の行に足した(行を足すと状態 29 の readout「言えない N」が変わる = 依頼書 §2-3「既存の数は変えない」)。
- **camera**: 状態 0・7 の camera の中心を板の上 22 単位へ(円錐の上端を枠に入れるため)。v2.1 の非表示の絵とも板の位置が約 32 px 違う(切り替えの往復では動かない)。

## 4. 検査(最後の通し = `checks/last_run.txt`・23:32:46〜23:43・頁の md5 6a4d444f ja · 9df3b0b2 en · widget.js 62a167d0)= `run_checks: PASS`

- `check_claims.py`: anchors **434 / 434**(v2.1 の 428 + v2.2 の幾何 6 = K429〜K434)· missing or different **0**。`--calibrate`: **18 kind で 18 / 18**(新しい kind `cone` を含む)。list_headings ok・台本 23 行 146.7 s(v2.1 のまま)。
- v2.1 からの検査は全部そのまま通過: MEASURE 31 状態 × {ja / en × video / desk / phone} + 明 + reduced = 248 画面で失敗 0(状態 0・7 は重ね描き 表示 = 既定)・robust は重ね描きの 表示 / 非表示 も回して **496 通り × 6 回・例外 0**(v2.1 は 248)・章の button 4 回・使わない語の走査 62 頁 × 2(陽性統制つき)・page-vs-raw・check_v21(desk / video)・check_fit_control(切ると 1110 / 1107 > 1072 で捕まり、入れると 1060)。
- **check_v22**(依頼書 §2-4・video ja / video en / desk / 明 desk / phone の 5 回): 状態 0・7 × 表示 → 非表示 → 表示 の各側で MEASURE(video では **1080 の枠と最下行**・字の最小 px = 状態 0 で 11.5 / 11.7 px・状態 7 で 10.95 / 11.14 px(表示 / 非表示)・viewBox の外の文字 0)= **measure_ok 6 × 5 回**、往復で 見出し・問い・lead・**readout**・chip・限定・最下行・札の pill・身分の札の文字が**変わらない**・表示の時だけ重ね描きが在る(部品 20)・t = 0 で viewBox の内・線の名 5・凡例の切り替え・`api.cone` = **v22_ok 6 × 5 回**。既定 = 表示(頁を開いた直後の `cone`)。幾何: t = −6〜6 の 13 点で §1 の残差が許容の内(最大: C が f / g の上 7.6e−5・GE ⟂ 軸 4.4e−6・持ち上げた P_y が円錐の上 6.8e−6 rad・J を通る円の上 1.7e−4・symptoma HP_y² = 4·VF·VH の相対差 1.5e−4)・半頂角 30°。**陽性統制**: 文字の比べが状態 0 と 7 の違いを捕まえる・画板に倒した P_y(高さ 0)は円錐の上と判じない(角の差 0.06 rad 以上で落とす)。
- **check_v22_click**(desk ja / phone en): 本物の click で 表示 → 非表示 → 表示(状態 0・7・aria-pressed)・状態 1 / 10 では button が出ない。
- **marimo**(三回): v2.1 の両方向 + kernel の数え直しに加えて、Python の button「cone off」→ 図の重ね描きが消える(kernel → 図・readout 不変)・「cone on」→ 戻る・図の button → kernel の `cone` が False → True(図 → kernel)。落とし穴: marimo の表示の cell は、kernel の側で値を替えても走り直さない(図の側から始まった変化だけで走る)= 最初の組み方(kernel → 図の後に kernel の表示が False になるのを待つ)は図と無関係に落ちた(二回目の通し)→ kernel → 図 は図の上で、図 → kernel は kernel の表示で読む形に直した。
- **JupyterLab**(三回・揺れ 0): notebook に cell 二つを足した(5 → 7: `w.state = 0; w.cone = False` と、図の button を押した後の `print('kernel sees cone', w.cone, …)`)。毎回 kernel → 図(状態 0 で重ね描きが消える)・図 → kernel(`kernel sees cone True`・1 回目で一致)。v2.1 の段(状態 10 の数え直し・状態 18 の図 → kernel は 2 回目で一致 = v2.1 と同じ型)も通過。止めた後の listener 0・自分の pid の生き残り無し・notebook は出力の無い版に戻した。三回 = 最後の通しの段 + `WIDGETS_ONLY=1` の 2 回(23:43:56・23:44:09)。
- console: 全部の drive で clean(JupyterLab の warning = 図と無関係な拡張の版の不一致と WebIO・v2.1 と同じ)。
- **通しの記録**: 一回目(23:12〜)は check_states の video の状態 13 で drive が止まった = MacBook が 23:13 に短く sleep し(`pmset -g log` の Wake 23:13:33)、drive.mjs の CDP の websocket が切れて応答を待ち続けた(drive.mjs は切れた socket を扱わない)。自分の起こした process だけを止め、二回目からは `caffeinate -i -m`(macOS の内蔵)で包んだ。二回目(23:21〜23:30)は頁の段が全部通過・marimo の cone の段だけ上の組み方の誤りで落ちた。三回目 = 最後の通し。

## 5. 撮影(依頼書 §1 「直した状態の分だけ撮り直す」)

- 撮り直した = **13 枚**: video ja = 状態 0(既定 = 表示)・**0_off**(新)・7・**7_off**(新)・0a / 0b(P_x = −5 / +5)・29(台帳 2/3 の言えない の行に一文を足した)= 7 / video en = 0・**0_off_en**(新)・7・29 = 4 / widget = `marimo_s10.png`・`jupyterlab_s18.png`(widget の段が毎回撮る)= 2。新しい file は 3 枚(`_off`)。ほかの 56 枚は v2.1 の撮影のまま(状態 0・7・29 のほかは絵も文字も v2.1 と同じ = 足した文字は状態 0・7 の凡例と限定・状態 29 の台帳だけ)。`captures/capture.log` = 69 枚(video 67 枚は全部 1920 × 1080)。
- 撮影の action = `checks/check_capture_v22.json` / `_en.json`(`run_checks.sh capture22` = 作図の板の状態だけ)。見たのは video ja / en の状態 0・7(表示 / 非表示)・0b・29。

## 6. 所要・一番自信の無い点

- **所要**: 開始 22:50:16 → 最後の通し PASS 23:43 → widget 二回 23:44 → 納品 23:45(約 55 分)。打ち切り 90 分の内。token の量は測っていない。
- **一番自信の無い点**: 円錐を**凍結の J の高さで切って固定**した決め(§3)。依頼の「C を頂点として CJ を母線とする円錐」を凍結の座標で読んだ形で、P_x を動かすと J は描いた円錐の縁から外れる(t < 0 で縁の外・t > 0 で内側 = g の線は画板の上でそのまま J まで延ばした)。動く J に合わせて切る読みもありうる。次点: 「台帳」を図の台帳 2/3 の既存の行への一文 + CLAIMS_v22.md の頭と読んだこと(図の台帳に行を足すと readout の数が変わる)。
