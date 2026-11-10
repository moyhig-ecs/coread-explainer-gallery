# PREREG: `moy5c` —— b5bp の問いだけ(道具なし・表なし)× effort max(moy5e の max の対照)

- 日付: 2026-10-15(木)午後 / 実行層 = Opus 5.5 xhigh。走らせる前に書き、local の commit で凍結する。判定と講評は先生。
- 先生(逐語): 「b5bp maxで走らせる」。
- 動機(moy5e の RESULT §5): max で Opus が P-tool・P-data とも 10 / 10 = 道具・表の効き目と effort の効き目が分けられない。

## §1 作り
- 問い = b5bp の凍結の Bbp(md5 `be9c4007`)そのまま。道具なし(Bash も止める)・表なし。
- `--effort max`・Opus 5.5 / Fable 5.1・n 10・経路は moy5t / moy5e と同じ(空の folder・user の設定なし・MCP なし・道具はすべて止める)。並列 4。
- runner = `ConstructGap/exp/moy5c_b5bp_only_max_20261015.py`。採点 = b5bp の凍結の `score`。
- 比べる相手 = moy5e の max の P-tool / P-data(Opus 10・10 / Fable 4・6)と、b5bp の API(effort high・Opus 7 / 20・Fable 0 / 20)。

## §2 予測(実行層 `L3`)
1. Opus P-none max の cut ≥ 8 / 10(effort が主・道具や表の寄与は小さい)。
2. Fable P-none max の cut 2〜6 / 10。
3. 答えの欄の cut ≤ 1(20 本)。

## §3 限定
moy5e と同じ(経路・一項目・n 10)。

## §4 していない事
走行・凍結。
