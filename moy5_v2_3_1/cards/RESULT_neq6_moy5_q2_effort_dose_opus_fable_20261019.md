# RESULT(札 `neq6`・様子見): effort を上げると比例中項が答えに浮上する — Opus 0 → 1 → 7 → 19 / 20・Fable 15 → 17 → 20 → 20(両 model DOSE UP)(2026-10-19・実行層)

- 札 = [PREREG neq6](PREREG_neq6_moy5_q2_effort_dose_opus_fable_20261019.md)(凍結 `0db9093d`)。書いた時の HEAD = `a6a666db`(origin の先 17・`R1`)。
- 走行 = zebrashark・Claude Code 2.1.292・`claude -p`・22:37:05 → 22:57:26。140 本・誤り 0・2 turn の行 0。
  - 換算: Opus $7.26・Fable $24.59。
  - wall の中央値(medium / high / max): Opus 17 / 21 / 81 s・Fable 38 / 43 / 102 s。
- 出力 = `ConstructGap/exp/results_neq6_moy5_20261019_claude-opus-5-5.jsonl`(md5 `a957c784`)・`…_claude-fable-5-1.jsonl`(md5 `37bd5ab7`)。xhigh は neq3 の行(runner が md5 を確かめた)。
- **身分**: §1 = `L1`。§2 = 記述(考えた量でそろえた数え・`L2`)。§3 = 予想。§4 = 読み(`L3`・採否は先生)。様子見であり、論文用の数は Fable 5.5 を加えて API で取る(先生 10-19)。

## §1. 関門・表・判定
- 関門: K/Q2@medium の bind = Opus 10 / 10・Fable 10 / 10 → 通過。

答えの欄の比例中項 / 出力のどこかに比例中項 / 相似の道の語 / 焦点と準線の語 / thinking の中央値(各 n 20):

| effort | Opus 5.5 | Fable 5.1 |
|---|---|---|
| medium | **0** / 0 / 0 / 20 / 1,039 | **15** / 16 / 11 / 10 / 2,365 |
| high | **1** / 1 / 0 / 20 / 1,371 | **17** / 17 / 12 / 11 / 2,722 |
| xhigh(neq3) | **7** / 7 / 1 / 20 / 1,735 | **20** / 20 / 20 / 16 / 4,144 |
| max | **19** / 19 / 15 / 20 / 8,507 | **20** / 20 / 20 / 20 / 7,858 |

**判定(凍結の規則・逐語)**:
- Opus: `MANIPULATION OK: thinking median medium 1038.5 / high 1371.0 / xhigh 1734.5 / max 8506.5`・`DOSE UP: … medium 0 / high 1 / xhigh 7 / max 19 (max − medium = 19)`
- Fable: `MANIPULATION OK: thinking median medium 2365.0 / high 2722.0 / xhigh 4144.0 / max 7858.0`・`DOSE UP: … medium 15 / high 17 / xhigh 20 / max 20 (max − medium = 5)`

- 目の確かめ(Opus の medium 20 本と max 20 本の答えの欄): 読み取り器と一致した。
  - medium は 20 本とも「P_y lies on the parabola with focus F and directrix e …」で、比例中項は無い。
  - max で比例中項の無い 1 本(r2)は、焦点と準線と接線だけ。

## §2. 考えた量でそろえた数え(記述・`L2`・effort の 4 段をまとめて thinking の量で分けた)
| thinking(token) | Opus: n / 答えに比例中項 / 相似の道 | Fable: n / 答えに比例中項 / 相似の道 |
|---|---|---|
| 1,500 未満 | 38 / **0** / 0 | 2 / 2 / 2 |
| 1,500〜2,500 | 21 / 8 / 1 | 15 / 10 / 8 |
| 2,500〜4,000 | 1 / 0 / 0 | 28 / 25 / 18 |
| 4,000〜8,000 | 9 / 8 / 7 | 26 / 26 / 26 |
| 8,000 以上 | 11 / **11** / 8 | 9 / 9 / 9 |

- Opus は、考えた量が少ないと比例中項が 0(38 本)。8,000 token を超えると 11 / 11。
- 同じ量の帯(1,500〜2,500)では、Fable 10 / 15・Opus 8 / 21 で、Fable の方がやや先に出る。
- 帯の中身は effort と model が混ざるので、記述だけ。

## §3. 予想(PREREG §5)の当たり外れ
- 「行動(探る量)で浮上する」の予想 = **当たり**。Opus は UP。Fable は medium で 20 から下がった(15)。
- 対立(道の選び方が model ごとに固定 = 両方 FLAT)= 外れ。
- 実行層の見込み = 半分外れ。
  - Opus の max は 10〜14 と見たが **19**。
  - Fable は FLAT(medium でも 17 以上)と見たが、15 で **UP**。

## §4. 読み(`L3`・採否は先生)
1. **比例中項は、探る量で浮上する**(先生の読みと合う)。同じ問い・同じ文面で effort だけを動かすと、Opus は 0 / 20 から 19 / 20 まで動いた。Opus に比例中項の知識が無いのではなく、短い探りでは焦点と準線の道(最短の証明)で止まり、比例中項を通らない。
2. **max では二つの model がそろう**(Opus 19・Fable 20)。neq3〜neq5 の「Fable 99 / 100 対 Opus 36 / 100」は、同じ「xhigh」でも探る量が model で違う(Opus 1,735・Fable 4,144)ことを大きく含んでいた。
3. **ただし、同じ量で比べても Fable の方がやや早く相似の道に入る**(1,500〜2,500 の帯で Fable 10 / 15・Opus 8 / 21)。道の選び方にも model の差が少し残る。
4. Fable 5.5 の腕の候補(MEMO §1 の B1「答えに比例中項を選ぶ」)は、軸を「行動」に置くことを支持する。ただし B1 は effort に強く依存するので、5.5 の位置を測るなら **effort を何段か並べて、曲線(effort → 比例中項)ごと比べる**方がよい。論文用の API の設計に入れる。

## §5. 主張しないこと
- effort は探る量の操作で、thinking の量は結果として測った記述。道を直接操作してはいない。
- 一つの問い(Q2)・何も足さない腕だけ・様子見(`claude -p`)。論文用の数は API で取り直す。
