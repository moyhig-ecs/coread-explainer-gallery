# 検査と撮影

## 検査(script にして、版ごとに走らせる)
| 検査 | 通過の条件 | 例の script(手本の entry) |
|---|---|---|
| console | 頁 4 本・desk・phone・video・reduced・marimo・JupyterLab で error 0(無関係な拡張の warning は記録) | `run_check.sh`・`make_check.py` |
| robust | 全状態 × 全行 × 層 4 つほどで例外 0 | `make_check.py`(robust) |
| 数の照合 | `check_claims.py` の anchor が全部一致・欠け 0 | `check_claims.py` |
| 章の button | 本物の click で各章の最初の状態・選ばれた見た目・hash・ja / en のラベル | `run_chapters.sh` |
| 並べ | 二つの立体が同じ尺・同じ camera・回すと両方動く・枠の大きさ・札の位置 | `run_pair.sh` |
| 内部の層 | 既定 off・コマンドで on / off・英語で何も起きない・層の file を消しても本体が動く・本体の柵の語 0 件 | `run_layer.sh` |
| 字の大きさ | 枠ごとの札の最小 px(video ≥ 10・desk ≥ 10・phone ≥ 9.5) | `make_check.py` |
| はみ出し | viewBox の外の文字 0 | `make_check.py` |

## 撮影
- `captures/video_s<N>[a|b].png` = 1920 × 1080 ちょうど(`sips -g pixelWidth -g pixelHeight` で確かめる)。
- `page_<dark|light>_s<N>[_en].png`(desk)・`phone_dark_s<N>.png`(390 幅)。
- 状態の番号を振り直したら full run で撮り直す(古い名前の撮影は捨てる)。小さな直しは影響する状態だけ撮り直し、何を撮り直したかを NOTES と `capture.log` に。
- 撮影の PNG に写っていない限定・札は、審査では「無い」と数えられる。

## 道具の事情(覚え書き)
- Anatomy の script は Node 20.10+ が要る。古い Node の機械では bun で走らせる(`~/.bun/bin/bun` / `~/.local/bin/bun`)。
- JupyterLab に ggblab と webio-jupyterlab-provider が在ると、最小の anywidget でも「図 → kernel」が届かないことがあった(kernel → 図は動く)。検査で双方向を確かめる。
- jupyterlab-myst が exception を出すことがある(図と無関係・環境変数で外せる)。
