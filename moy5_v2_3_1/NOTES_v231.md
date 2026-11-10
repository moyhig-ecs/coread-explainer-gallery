# NOTES — entry_v2_3_1(駅 3 = moy-5 の v2.3.1・2026-11-09・作り手 = 主 session・自宅 MacBook)

- **発**(逐語・依頼者 11-09): 19:36「切断平面が育つのがかえって分かりにくいかもしれない。」→ 主 session の案 1(面と放物線を固定し、点だけが動く)→ 19:4x「それで進めます」。
- **開始** = 19:44:23(`cp -R` の時刻)。土台 = `../entry_v2_3_received/`(写しただけ・元は無傷)。`DONE` は写さない。この entry の `NOTES.md` は v2.3 の作り手の記録のまま(書き換えない)。
- 道具(MacBook): bun `~/.local/bin/bun` 1.4.3・python `~/miniforge3/envs/py314/bin/python`・drive = `~/.claude/skills/anatomy/scripts/drive.mjs`。比べの土台 `BASE22` = `../entry_v2_2_received/`(この MacBook に dist が在る)。

## 1. 何が「育って」いたか(v2.3 の `cutPlane` を同じ code で計算・node)

v2.3 は P_x を動かすたびに、面の長さを放物線の端 H まで、高さを持ち上げた P_y まで取り直していた。

| t | 面の長さ(j に沿って) | 面の高さ |
|---|---|---|
| −6 | 30.31 | 17.08 |
| −1 | 14.85 | 11.25 |
| 0(凍結の P_x) | 12.54 | 10.08 |
| 2 | 8.72 | 7.75 |
| 6 | 5.82 | 3.09 |

面積で約 29 倍。点を動かすと、一枚の固定した平面が伸び縮みして見える。

## 2. 変えた所(全部 作図 = data でない)

- `figure.js`
  - `cutPlane(g)`: 面の長方形・準線・放物線の標本を **凍結の P_x(t = 0)で一度だけ** 決める(`G0 = construct(Pt.P_x)`)。動くのは持ち上げた P_y(`lift`)だけ。t < 0 で点が面の縁を越えた分は、同じ放物線の標本 25 点(`ext`)。
    - t = 0 の大きさ = 描いた円錐の切り口(円錐は凍結の J を通る円まで描いてあり、t = 0 の持ち上げた P_y はその縁に乗る = v2.2 の `Py_on_circle_through_J`)。
  - `coneOverlay`: 放物線(`cut-line`)と膜(`cut-film`)は固定の物。点(`lift`)と倒す弧(`fold`)は P_x に連れて動く。面の外の続きは `cut-ext`(細い破線)。
  - `planeCheck`: 面の外の続きと動く点も「面の上・円錐の上」に含めて測る。足した量 = `plane_fixed`(t = 0 の面・放物線との差)・`lift_on_par`(|HPy² − 4p·VH| / HPy²)・`ext_n`・`lift_inside`。仕込みの誤り `grow`(面を 0.1 % 育てる)を足した。
- `figure.css`: `.cut-ext`(破線 4 3・不透明度 .75・家の色のまま)。
- `i18n.js`: 凡例 `ccut` に一句(ja「面と放物線は動かない(P_x を動かすと、持ち上げた P_y だけが同じ放物線の上を動く・面の外は破線)」/ en 同じ意味)。
- `make_check.py`:
  - GEOM23: 許容に `plane_fixed ≤ 1e−12`・`lift_on_par ≤ 1e−3`。統制 `grow` を捕まえること。t = −6・−1 で `ext` が在り、t = 0・2・6 で無いこと。
  - DRAWN23: 描いた面の四隅と放物線の頂点が、同じ状態の t = 0 の物から 0.15 px 以上動かないこと(t = ±5)。`cut-ext` は t < 0 の時だけ一本で、放物線の端から始まること。

## 3. 検査(`BASE22=… sh run_checks.sh capture23`・19:46〜20:0x・PASS)

- build: 4 頁・31 状態・頁の md5 `03e6408d` ja · `d2515fad` en · widget.js `5761d49f`。
- 照合 447 / 447(違い 0)・較正 19 種 19 / 19・面の anchor 13 / 13 + 仕込み 3 / 3(`check_claims.py` = 別の code・t = 0 の値は v2.3 と同じ)。
- 頁の面の幾何(GEOM23): video / desk / phone × ja / en で `geom23_ok`。描いた物(DRAWN23): `v23_ok` × 8 の段 × 各枠。
- 他の頁は変わらない: v2.2 の build との比べ = 33 の dump のうち 31 が同じ・違うのは `0/on`・`7/on`(重ね描きの在る二つ)だけ・予期しない違い 0(video / desk / phone × ja / en)。
- marimo・JupyterLab: 両方向 + kernel の数え直し 通過。JupyterLab の console の警告 4 行は MacBook の JupyterLab の拡張(lumino の版・WebIO)から出た物で、図解の側ではない(v2.3 の職場の記録の警告は別の拡張の物)。
- 撮り直し(capture23): `video_s0.png`・`video_s7.png`・`video_s0_en.png`・`video_s7_en.png`・`video_s0a.png`(t = −5)・`video_s0b.png`(t = +5)。ほかは v2.3 の写し。
- 目で見た: s0a = 面は t = 0 と同じ所・放物線は面の左上の縁から破線で延び、持ち上げた P_y へ / s0b = 持ち上げた P_y が面の中の放物線の上・倒す弧は板の P_y へ。

## 4. 残り(直していない)

- v2.3 の作り手の一番自信の無い点(en の頁で凡例の行が板の右下の隅の字に約 7 px 触れる)はそのまま。
- s0b(t = +5)で、点の名 P_y が A に近づく(v2.2 から在る・検査は「動かした時は面の名だけを重なりの対象にする」= v2.3 の決め)。
