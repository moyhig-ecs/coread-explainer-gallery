# PREREG(札 neq6・様子見): 問い Q2 {F, V, P_x, P_y} の何も足さない腕で effort を動かす — 比例中項は行動(探る量)で浮上するか・Opus 5.5 と Fable 5.1・`claude -p`

- 日付: 2026-10-19(月)夜・zebrashark(Claude Code 2.1.292)・実行層(Opus 5.5)/ 書き始めの HEAD = `b5154421`
- 発注(逐語): 先生 10-19 夜「比例中項は知識じゃなくて行動によって浮上しそう。opusとfableの行動観察の結果ではそう見えますよね？ codeのサブエージェーントで様子を見て、APIで論文用のデータを取りましょう。APIクレジットありがたい。」→(実行層が effort の量を動かす様子見を提案)→「1は進めてください。凍結・発火 / 2はFable 5.5が出て、1に加えてから走らせましょう。」
- **身分**: 様子見(Code のサブエージェント = `claude -p`)。論文用のデータは、Fable 5.5 が出てから API で取る(先生)。
- **凍結の実体**: 本書・runner `ConstructGap/exp/l14_moy5_q2_effort_dose_claude_p_20261019.py`・launcher `ConstructGap/exp/launch_neq6_20261019.sh` を一つの commit に。runner は neq4 / neq3 の runner を import する。`guard_frozen()` は四つのどれかが dirty なら走らない。

## §0. 事前に知っていること(開示)
1. Q2 の xhigh の 100 本ずつ(neq3〜neq5・何も足さない腕・一文の 3 腕・fixed points の腕):
   - 答えに比例中項 = Fable 99・Opus 36。
   - Opus の比例中項の無い 64 本は、理由の欄にも無い(64 / 64)。焦点と準線の道を書いた(64 / 64)。相似・比例中項の語は 1 / 64。
   - thinking の中央値 = Fable 4,159・Opus 1,887。
   - Opus を thinking の中央値で二分すると、答えに比例中項は上の半分 24 / 50・下の半分 12 / 50(腕の違いが混ざる)。
2. Opus は比例中項を知っている(K 10 / 10・名 / 本文で 20 / 20 = neq3)。
3. 経路の確かめ(本書の前・各 1 回・moy-5 の問いは見せていない): `--effort medium` と `--effort max` を両 model で。init の model は指定どおり、答えは "OK"。effort が効いているかは確かめていない(→ §4 の操作の確かめ)。
4. `--dry`: A/Q2 md5 `123ea1ac`(neq3 と同じ)・K/Q2 md5 `eb6a33e7`。A/Q2@xhigh(neq3 の行)= Opus 7 / 20・Fable 20 / 20。

## §1. 設計
- 問い = neq3 の A/Q2(一字も変えない)。変えるのは `--effort` だけ。
- 腕(model ごと):

| 腕 | effort | n |
|---|---|---|
| A/Q2@medium | medium | 20 |
| A/Q2@high | high | 20 |
| A/Q2@xhigh | xhigh | 20(**neq3 の行**・md5 を固定・引き直さない) |
| A/Q2@max | max | 20 |
| K/Q2@medium | medium | 10(陽性統制 = 一番低い effort でも経路と読み取り器が働く) |

- model = Opus 5.5・Fable 5.1、zebrashark、経路は neq3 と同じ。workers は model ごとに 4、並走。新しく引くのは 2 × 70 = 140 本。

## §2. 測るもの
- **主: 答えの欄の比例中項**(読み取り器 v2 の CUT / SIM-CUT が conjecture にある)。
- 副: 出力のどこかに比例中項(bind)/ 答えの欄の放物線 / 道の印(相似・比例中項の語 = SIM、焦点と準線の語 = FD・正規表現は runner に逐語)/ thinking の中央値。

## §3. 関門(`R6`)
K/Q2@medium の bind ≥ 8 / 10(model ごと)。落ちたら、その model の残りを引かずに止める。

## §4. 判定(凍結・model ごと・余白 3 / 20)
1. **MANIPULATION**: thinking の中央値が max > medium なら OK。そうでなければ FAILED(effort が効いていない → 2 は読まない)。
2. **DOSE**: 答えの欄の比例中項で max − medium ≥ 3 → UP、≤ −3 → DOWN、その間 → FLAT。
3. K 以外のどれかの腕が 18 本未満なら INCOMPLETE。

## §5. 予想(発火の前に書く)
- 「比例中項は行動(探る量)で浮上する」が正しければ:
  - Opus は UP(medium で xhigh の 7 より少なく、max で多い)。
  - Fable は medium で 20 から下がる(DOWN か、天井の近くで FLAT)。
- 対立(道の選び方が model ごとに固定)なら、両 model とも FLAT(Opus は 5〜9 のまま・Fable は 20 のまま)。
- 実行層の見込み: Opus は UP(max で 10〜14)・Fable は FLAT(medium でも 17 以上)。Fable の相似の道は、短い探りでも先に出ると見る。

## §6. 主張しないこと
- effort は「探る量」の操作で、道の選び方そのものではない。thinking の量と道の印は記述。
- 一つの問い(Q2)・何も足さない腕だけ。論文用の数は API で取り直す(Fable 5.5 を加えてから・先生)。

## §7. 手順(launcher)
model ごとに `--fire --units K/Q2@medium:10` → `--gate` → `--fire --units A/Q2@medium:20,A/Q2@high:20,A/Q2@max:20` を並走 → `--read`。
