HEAD(R1) = 67c07546(起案の時・11-09 18:1x・zebrashark・push 前 = origin より 9 つ先)

# BRIEF v2.3 — 駅 3(moy-5)の受領版に、円錐の切り口の面(直線 FVD を通り板に鉛直な平面)を描き足す(2026-11-09)

- **発**(逐語・先生 11-09 18:1x): 「今すぐでなくてもいいのですが、moy-5の円錐断面が直線FVDを鉛直に切る平面だとわかるように図示する。次回から。」→「順序でいうと、公開前に切断平面は図示したい」= gallery の公開(A4 / B5)の前に v2.3 を作り、v2.3 で束を作り直してから公開する。
- **作り手** = 一人・Opus 5.5 xhigh(v2.1・v2.2 と同じ)。**土台** = v2.2 `/Users/manabu/lancedb-rag/conversations/2026-11-06/coread_station2_3/station3_moy5/receipt/entry_v2_2_received/`(最初に NOTES・README・figure.js の円錐の重ね描きの節(l.60〜 の `cone` / `Dandelin sphere` / 検査の `j_tangent_at_F` ほか)・config・check_claims を読む)。
- **置き場** = `/Users/manabu/lancedb-rag/conversations/2026-11-06/coread_station2_3/station3_moy5/receipt/entry_v2_3_received/`(土台を写してから直す)。**書き換えない** = v2.2 以前の entry・公開の束 `conversations/2026-11-09/publish_prep/gallery/moy5_v2_2/`・skill。
- scratch = `/private/tmp/claude-501/maker_v2_3_station3/`・port = 28700〜28799。

## §1 作図の事実(凍結の座標からの計算・L1・主 session が `generated/pack.json` の `construction` から出した値・作り手は計算し直して anchor に)

- 線 j = 直線 FVD: F(0.4875, −3.9702)を通り、f(G での接線)に平行。向きの単位 = (0.992546, 0.121874)。
- V・D は j の上(j からの離れ V 4.1e−05・D 0)。**V は FD の中点**(t_V / t_D = 0.500007・|FV| 2.3094・|FD| 4.6188)。
- A から j の距離 = 4.000018(= 円 c の半径 r)・AF ⟂ j(内積 0)= **j は円 c に F で接する**。
- 読み(L3・v2.2 の作図と同じ): 切り口の面は j を通り板に鉛直 → Dandelin 球(中心 A・半径 r)にこの面が F で接する = 焦点 F。準線 = 接触円の面とこの面の交わり = D を通る鉛直の線。頂点 V = FD の中点。**OLMo がこれを知っていたとは言わない**(v2.2 と同じ限定)。

## §2 やること

1. **切り口の面を描く**(重ね描きの層の中・既定 = 表示・今の「円錐を重ねる」切り替え / `?cone=0` / widget の trait `cone` に従う):
   - 板の上の線 j(F・V・D を名指す・点と名の札)に沿って、板から鉛直に立つ**半透明の面**(長方形・幅 = j の上で放物線が描かれる範囲を少し越える・高さ = 描いた放物線の最高点を少し越える)。面の縁は細い線、塗りは薄い一色(既存の色の意味を保つ・新しい色を足すなら dataviz の validator で ΔE を確かめる)。
   - 切り口の放物線がこの面の中にあること(面の上に乗って見える描き順)・焦点 F(面と球の接点)・準線(D を通る面の中の鉛直の線)・頂点 V を面の中で名指す。
   - 札(凡例の一行): 「切り口の面 = 直線 FVD(線 j)を通り、板に鉛直(作図・data でない)」。en も。
2. **数え直しと anchor**: §1 の値(V・D の離れ・中点の比・A から j の距離・AF ⟂ j)+ 描いた放物線の点が面の中にある(面からの離れ ≤ 1e−6・標本 20 点以上)+ 面が板に鉛直(面の法線と板の法線の内積 0)を、pack(python)と JS と check_claims の三経路で。anchor を K435〜 に足す。calibrate の陽性統制も足す(わざと違う値を入れて捕まる)。
3. **検査**: 土台の検査一式(状態 0・7 の重ね描きの 表示 / 非表示 の往復・1080 の枠と最下行・字の最小 px・ラベルの重なり 0・viewBox の外 0・console 0・JupyterLab / marimo)+ 面の追加で他の状態の頁が変わらないこと(重ね描きの無い状態の画面の文と数は v2.2 と同じ)。
4. **撮影**: 重ね描きの出る状態(0・7)の video ja / en と、P_x を動かした 2 枚(土台の `video_s0a/b` の型)を撮り直す。ほかの撮影は写し(撮り直さない)。何を撮り直したかを NOTES に。
5. **記録**: NOTES の頭に v2.3 の節(何を足したか・誰の依頼か・§1 の値と計算し直した値・撮り直した撮影)。README の版を v2.3 に。

## §3 守ること・打ち切り・返すもの

- install・通信・git の書き込みをしない。実験の script を import も実行もしない。model を動かさない。subagent を使わない。Fable を使わない。pkill / killall を使わない(自分の pid だけ止める)。Bash は単純な command に分ける。
- 道具: bun `/Users/manabu/.bun/bin/bun`(1.3.0)・python `/Users/manabu/miniforge3/envs/py314/bin/python3`(`-I`)・anatomy `~/.claude/skills/anatomy`(689dcf9・checkout を変えない)・Chrome の headless。
- **R16**: 20〜40 万 token・30〜60 分の見込み(v2.2 = 55 分・37 万 token)。**打ち切り 60 分**(120 分を越えたら主 session が止める)。開始の時刻を NOTES の頭に。
- 終わりの印 = `DONE`。commit しない。返すもの ≤ 10 行: 面の描き方(大きさ・色・描き順・既定)・§1 の値と計算し直した値・面の上の放物線の離れ・anchor / calibrate・検査・撮り直した撮影の枚数・所要・一番自信の無い点。
