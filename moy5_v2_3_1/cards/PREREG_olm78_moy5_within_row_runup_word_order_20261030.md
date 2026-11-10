HEAD(R1) = affbcd1c(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm78`・凍結 2026-10-30 夜): moy-5(線 2・S-1 の行の中の版)— 同じ行の「cut の文の手前 32 − 偽の出来事の手前 32」の寄り d は、窓の中の語の順を入れ替えても残るか(語の積み上がり 対 語順)・最終層(model の実際の出力)でも d は立つか

- 発注(逐語): 先生 10-30 夜「この順で進める。」→(olm77 の結果)→「1 OK」(= S-1 を行の中の対比に替えて草稿を書き、zebrashark で回す)。設計の元 = Sonnet 監査の `conversations/2026-10-29/audit_plan_line1_line2/entry_sonnet_max/PLAN_own.md` の S-1。比べを cut の行 対 床の行から、**行の中の対比**(olm74 Q2 の型)に替えた。理由 = olm77 で、全行の cut 対 床 の差が札の構成から来ている見込みが出た(記述)。
- G10 の欄: 比べる物 = 「語の順をそのままにした窓」/「語の順を入れ替えた窓」 / 計器 = 同じ行の本当の出来事の手前 32 と偽の出来事の手前 32 の、J-lens 層 48 と最終層の CUT 対 FLOOR の語の集合の log Σ p の行の中の百分位の差(d) / 雛形 = いいえ
- runner = [olm78_…py](../../ConstructGap/exp/olm78_moy5_within_row_runup_word_order_20261030.py)。forward = **zebrashark**(OLMo-3 32B・mlx・olm67 と同じ `forward_capture`)。読み = MacBook でも zebrashark でも(torch が要る = zebrashark)。API なし・Wolfram なし。

## §0. 凍結の前に見た物(開示)

- olm74 Q2(保存の系列・O の行): 288 行・d > 0 が 192(0.667)・中央値 +0.0522。model 別(Opus 監査 r02): Opus O の d 中央値 +0.0562・Fable O +0.0470。
- Sonnet 監査の S-1 の見込み = 「語順に依らない」(根拠 = 語の袋の AUC 0.81・rc10)。
- olm77 の RESULT(札の中では cut 対 床 が立たない・記述)。
- この札の行の数(`--count`・値は読まない): **288 行**(Fable 174・Opus 114)・前置きの最長 1,108 token。
- **入れ替えた窓の値・最終層の値は見ていない**。合成の自己検査(`--selftest` 11 / 11)は model を使っていない。

## §1. 行と計器(R5)

- 行 = olm67 の series の cut の行のうち、neq3 の L の腕(L-name/Q2・L-text/Q2)を除き、本当の出来事 t と偽の出来事 tp(olm68)の手前 32 が両方収まり、二つの窓が重ならない(|t − tp| ≥ 32)物 = 288 行(olm74 の O と同じ)。
- 条件:
  - **intact** = 系列の ids そのまま。
  - **shuf** = 二つの窓 [t − 32, t)・[tp − 32, tp) の中だけ token の順を入れ替える(窓の外と、窓の中の語の多重集合は同じ)。seed 2 つ(7801・7802 × 1000 + 行の番号)の平均。
- forward = ids の [0, max(t, tp)) を teacher-forced で(因果の model = 窓の位置の値はそれより後に依らない)。
- 読み:
  - **層 48** = J-lens(olm67 と同じ)の CUT / FLOOR の語の集合の log Σ p。百分位の物差し = その行の**保存の系列**(olm67)の値。
  - **最終層** = 層 63 の出力 → norm → unembed(model の実際の次の語の分布)。物差し = intact の forward の前置きの全位置の値。
- d = s(本当の窓) − s(偽の窓)、s = 窓の 32 位置の(u_CUT − u_FLOOR)の平均。

## §2. 統制(R6)

- **C0(写し)**: intact の forward の層 48 の s が、保存の系列の s と 0.003 以内の行 ≥ 95 %(本当の窓・偽の窓の両方)。✗ なら読まない(runner を確かめる)。
- **C1(入れ替えが効く)**: 最終層で、窓の位置の「次の token の log p」の平均が、入れ替え(seed 7801)で intact より下がる行 ≥ 90 %。✗ なら読まない(入れ替えが文脈を壊していない)。
- **C2(読む効果が在る)**: intact の層 48 の d > 0 の行 ≥ 60 % かつ 符号検定 p < 0.05(olm74 Q2 の再現の型)。✗ なら Q1 を読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | 予想 |
|---|---|---|---|
| Q1 | 層 48 の d は語順を入れ替えても残るか | r_W = 中央値(shuf の d)÷ 中央値(intact の d)。r_W ≥ 0.5 かつ shuf の d の中央値の 90 % 区間(boot 2,000・seed 7803)の下限 > 0 →「語順に依らない(語の積み上がり)」/ r_W ≤ 0.25 →「語順に依る」/ その間 →「混合」(記述) | 「依らない」p 0.45・「依る」0.20・「混合」0.35 |
| Q2 | 最終層でも intact の d が立つか | d > 0 の行 ≥ 60 % かつ 符号検定 p < 0.05 | p 0.55 |
| Q3 | 最終層の d の語順 | Q2 ✓ の時だけ Q1 と同じ型で判定・✗ なら記述 | — |
| Q4 | model 別(Opus・Fable)の中央値 | 記述(並べる・総計しない) | — |

- L3(読み・確率つき): 「行の中の前触れ(d)は、窓の語の積み上がりで、語順の構造に依らない」p = 0.45(解ける条件: Q1 の類 = 依らない で真・依る で偽・混合 で解けない)。

## §4. 止める規則

- C0 か C1 が ✗ → 読まない。C2 ✗ → Q1 を読まない(Q2〜Q4 は記述)。
- 走行の途中で PREREG と runner を書き換えない(dirty で `--fire` 以降が止まる)。
- 1 回で打ち切る(条件を足さない・同じ型の作り直しをしない = Sonnet 監査のやめる条件)。

## §5. 言えないこと

- 因果・中の状態は言わない。frontier の本文を OLMo が読む時の話で、Opus・Fable の中の話ではない。
- 窓の中の入れ替えは、語の積み上がりと語順を分けるが、窓の外の文脈(前の文)は同じ = 「前の文の内容」の効き目は分けない。
- 行は cut の行(O)だけ。床の行と比べる話はしない(olm77)。

## §6. 走らせ方(zebrashark)

```
cd ConstructGap
python3 -I exp/olm78_moy5_within_row_runup_word_order_20261030.py --selftest   # model なし(凍結の前に通した・11 / 11)
python3 -I exp/olm78_moy5_within_row_runup_word_order_20261030.py --fire       # forward 288 行 × 3 条件 → olm78/rows/*.npz
python3 -I exp/olm78_moy5_within_row_runup_word_order_20261030.py --control    # C0〜C2 → olm78/control.json
python3 -I exp/olm78_moy5_within_row_runup_word_order_20261030.py --read       # Q1〜Q4 → olm78/read.json
```
