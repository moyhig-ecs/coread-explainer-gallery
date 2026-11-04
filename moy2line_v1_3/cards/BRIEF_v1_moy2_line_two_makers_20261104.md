HEAD(R1) = d4e2515b(この BRIEF と inventory を入れる commit の親 = RECORD の commit・fetch + pull 済 = Already up to date・遅れ 0)

# BRIEF v1 — moy-2 の「折り返しの道具」の系列の図解: 問いの文の Tool の段(式だけ / 宣言の文 / 指示の文)で、OLMo-3 32B base が証明の欄に書く「O1O2 についての線対称」(偽の前提)がどう動くか — 式だけでは植わらず(0.108・二回)、宣言の文は植え(0.318)、指示の文は一回目(olm125)で計算を増やさず名指しを増やし線対称を増やした(0.225)が、二回目(olm127)は関門 G1 落ち(40 / 60)で判定なし・参考 0.086 = 式だけの側で、一回目に見えた物は一つも再現しない。計算した行は折り返しを数値で退ける(四腕 43 / 47)が、退けた後に証明の欄で線対称が戻る行(b2_j07 の型・0〜3 本)と、退けた命題にそのまま戻り続けて上限に至る行(olm127 b2_j08 = 343 回)がある = 答え合わせは在るが読み(候補の木)が無く、退けが commit に届かない(anatomy × anywidget・競作 = Opus 5.5 xhigh / Sonnet 5.5 max・2026-11-04)

- 発注(逐語): 先生 11-04 朝「**一区切りつけましょう。区切りがついたらopus-5.5-xhighとsonnet-5.5-maxでcoread-explainerで図解。**」
  - 同じ message の先生の問い(G 章でだけ扱う・L3): 「**olmXシリーズから評価関数を導出できますか？**」。主 session の答え(MEMO §4・採否は先生)= 価値関数は出ない・出るのは受領関数(座標 + 摂動)と「評価が使われているか」の計器。
- **この図での語の約束**:
  - **OLMo** = OLMo-3-1125-32B base(open-weight・温度 0.7・max_new 12,288・60 行 = 3 batch × 20・seed は腕ごとに違う)。
  - **moy-2** = 二つの円 c(中心 O2)・h1(中心 O1)が離れて内側の共通接線 l1 を持ち、接点 Tc(c 上)・Th(h1 上)・O3 = O1O2 の中点。問い = {Tc, Th, O3} の間に常に成り立つ関係を一つ(JSON: conjecture / status / proof)。座標が与えられる(一般の図・半径 3.6869 / 7.4607)。
  - **Tool の段** = 問いの文の中の「# Tool (available if you need it)」の段。三種: **式だけ**(TOOL_D = 折り返しの式 P' = 2F − P・olm122 / olm124)・**式 + 宣言の文**(TOOL = 式 + SECOND「Two points are symmetric with respect to the line O1O2 exactly when each is the reflection of the other.」・olm119)・**式 + 指示の文**(TOOL_D + TOOL_U「Use it to check: compute the reflection with the given coordinates before you rely on it.」・olm125 / olm127)。道具なし = olm113 の M2A。逐語は inventory の `prompts`。
  - **線対称(LN)** = 証明の欄(JSON の proof)で「Tc と Th は O1O2 について対称 / Th を O1O2 で折り返すと Tc」と**肯定して**(否定・仮定でなく)述べること。一般の図では**偽**(半径が違う)。**v3** = 凍結の計器(olm118・判定に使う)/ **v6** = 直の目的語「reflect(ing) Tc across O1O2 yields Th」と入れ替えを足し式の写しを外した計器(olm126・参考)。
  - **外接線の印(OUTER)** = 証明の欄で「接線 ∥ O1O2」「O1O2 ⊥ 接線」「O1O2 が接点の垂直二等分線」= 外側の共通接線の記憶が内側の接線に貼られた印(一般の図では偽)。
  - **計算した行(REFL_CALC)** = 本文で折り返しの式を数値で使った行。**退け(REJ6)** = 折り返しを数値で出して「not the same / is not Th / ≠ / doesn't match」と書いた行(v6)。**b2_j07 の型** = 退けた後に、証明の欄で線対称を書く行(REJ6 ∧ 証明の欄 LN6_a)。
  - **類(cls)** = conjecture の種類: MIDO3(Tc, Th, O3 が共線 / O3 が中点)・EQ(O3 が Tc・Th から等距離)・OTHER・NONE(JSON が取れない)。**MIDO3 は一般の図では偽・EQ は一般の図で真**(= apex・O2Tc ⊥ l1・O1Th ⊥ l1 なので O3 は TcTh の垂直二等分線上)。**正しさの率は測っていない**(図では類の率を示すだけで、各行の証明の正しさは読まない。線対称・外接線の印は偽の前提の印)。
  - **関門 G1** = conjecture が取れた行 ≥ 0.75(45 / 60)。落ちた札(olm122・olm127)は判定なし(参考値だけ)。六腕の取れる率 0.833 / 0.800 / 0.767 / 0.750 / 0.750 / 0.667 = 境は揺れの中。
- 作り手 = **あなたの entry**(依頼文に書いてある: `entry_moy2line_opus_xhigh_v1` か `entry_moy2line_sonnet_max_v1`)。**他の entry の folder は読まない**。git log は本 BRIEF を入れた commit まで。
- skill:
  - **最初に** `/Users/manabu/lancedb-rag/.claude/skills/coread-explainer/SKILL.md` と、その `references/`(brief-template・data-contract・implementation・checks-and-captures・coread-loop・wording)を全部読み、`assets/`(合成の data で build・検査・撮影まで通した骨)を写して始める。
  - 描き方は `anatomy` の kit(この機 zebrashark には `/Users/manabu/.claude/skills/anatomy` が在る)。手本 `conversations/2026-10-17/anatomy_silenthop/entry_Q_v5/`(NOTES・CLAIMS・README・生成した頁・LICENSE)は全部読んでよい。MIT の表示(Copyright (c) 2026 Ryan)を残す。
  - BRIEF の形の前例 = `conversations/2026-11-02/explainer_dow_thales/BRIEF_v1_thales_two_makers_20261102.md`(その entry の folder は読まない。**例外**: 道具として `conversations/2026-10-31/explainer_outward_line2/entry_opus_xhigh_v1/drive.mjs`(DevTools の口で Chrome を動かす約 70 行)が在れば読んで写してよい。図の中身には使わない)。
- 置き場 = `/Users/manabu/lancedb-rag/conversations/2026-11-04/explainer_moy2_line/<あなたの entry>/`(絶対 path)。scratch = `/private/tmp/claude-501/-Users-manabu-lancedb-rag/d6b4071d-1e54-45d7-ba1a-5d3d7ef16e29/scratchpad/explainer_moy2line_<あなたの entry>/`。終わりの印 = 置き場に `DONE`。
- **書き込みの手順**: 作業は全部 scratch で行う(build・headless Chrome・marimo / JupyterLab の localhost まで)。納品だけ: `mkdir -p <置き場>` → `cp -R <scratch>/. <置き場>/` → `diff -rq <scratch> <置き場>` → 最後に `DONE` を別に置く。**commit しない**(主 session が受領の後に入れる)。Bash は単純な command に分け、合成が拒否されたら script file にして呼ぶ。止める process は PID を確かめてから `kill <PID>`(pkill / killall は使わない)。
- **同時に 2 人の作り手が同じ機で走る**: localhost の port は **あなたの帯だけ**を使う(`entry_moy2line_opus_xhigh_v1` = 27500〜27599・`entry_moy2line_sonnet_max_v1` = 27600〜27699)。Chrome の `--user-data-dir` は自分の scratch の中に置く。
- 機械と道具(zebrashark = `zebrashark.local`・M2 Ultra 192 GB):
  - bun = `/opt/homebrew/bin/bun`(1.4.3)・node = `/Users/manabu/miniforge3/envs/py314/bin/node`・python = `/Users/manabu/miniforge3/envs/py314/bin/python`(anywidget 0.11.0・marimo 0.23.13・jupyterlab 4.5.6・numpy)・ブラウザ = `/Applications/Google Chrome.app` の headless(Playwright は無い)。版は NOTES に書く。
  - JupyterLab で figure → kernel が通らない時は、他の widget の拡張(ggblab・webio-jupyterlab-provider)を**その走行だけ**使い捨ての設定で切ってよい(install も削除もしない)。
  - **install・通信・git の書き込みはしない。実験の script(ConstructGap/exp/*.py・inventory/*.py)を import も実行もしない・data の file を読むだけ。model を動かさない(GPU では別の仕事が走っている)。subagent は使わない。**
- 打ち切り 180 分(足りなければ、できた章までを検査と撮影まで通して返す)。返すもの ≤ 10 行: file・状態の数・章・撮影の枚数・照合の結果(N / N)・検査の結果・一番自信の無い点。

## 読み手と最終評価

- **E1 editor**: ConstructGap 線(OLMo の証明の欄の前提の読み出し)の稿の付図・補遺として出せる質。RESULT(olm118・119・122・124・125・126・127)が主張しないことを主張しない。凍結の判定(v3)・参考(v6・pool・Fisher)・G1 落ち(olm122・olm127 = 参考値だけ)・記述(等半径の対照)の区別が全画面で見える。
- **E2 動画の作者**: 1920 × 1080 の撮影と台本だけで 1〜2 分の一場面が作れる。最初の 10 秒で芯が見える。
  - 芯 = 「**同じ問いの文に折り返しの道具を足すと、式だけでは OLMo の証明の欄に偽の前提(接点は O1O2 について対称)は植わらない(二回とも 0.108)。宣言の文は植える(0.318)。指示の文は計算をほとんど増やさず(15 → 18 本)、道具の名指しを増やし(11 → 18)、計算しない行の証明の欄に線対称を増やした(0.225)— が、同じ問いの文の二回目(olm127)は G1 落ちで判定なし・参考 0.086 で、一回目に見えた物は再現しない。式を数値で使った行は折り返しを退ける(四腕 43 / 47)— だが退けた後は、上限で回る(olm127 5 / 6)か、記憶の線対称に戻る(b2_j07 の型・olm125 3 本)か、apex(等距離・真)に数値で着く(olm127 2 本)かで、退けた命題がそのまま次の候補に戻り続ける行(b2_j08・343 回)もある。答え合わせは在る。読みが無い。退けが commit に届かない。**」
- **E4**「この計器だから、この読みが出た」: 撮影の上で次が見えること。
  - 計器の系譜 v3 → v4 → v5 → v6(較正 54 → 74 → 98 → 144・陰性統制 = frontier の証明 20 本で 0 / 20)と、**olm118 の Q3(外接線の印の 等半径 − 一般 の差)の帯が v3 変わらない → v4 間 → v5 間 → v6 変わらない に戻った**こと(窓の規則の落とし 1 本の有無で境 0.06 を 0.003 越えていた)。
  - **凍結の判定は計器の形に依らない**: 五腕の線対称の率は v3 → v6 で +0.000〜+0.054 動くが、olm118 Q1 / Q2・olm120 Q1 / Q2・olm119 / olm124 / olm125 の Q1 の判定 7 / 7 は同じ(olm126 Q2)。
  - **関門 G1 が境ちょうど**(45 / 60 = 0.750・olm124 / olm125)で、一行少なければ判定が無かったこと。olm127 は 40 / 60 で落ち、判定なし(PREREG で「半分近い」と開示)。olm122 は 46 / 60 で当時の境 0.80 に落ち、G1 を三腕の実測で 0.75 に較正し直した(開示・PREREG olm124 §0)。
  - **60 行ずつでは隣と分けられない**(Fisher 参考: olm125 0.225 対 olm124 0.108 p 0.23・対 式だけ pool 120 行 p 0.11・対 olm119 p 0.46)= 判定は凍結の帯・大きさは走らせ直しで。
- **先生の決め(この図の一番の読み手)**: 図を見た後に答える三つの問い(正答の基準つき)。
  1. **式だけ・宣言の文・指示の文で、証明の欄の線対称の率はどう違うか。何が同じで、何が違うか。**
     - 基準: 同じ = model・温度・座標・問いの文の Tool の段以外・計器 v3・G1 0.75。違う = Tool の段の文(逐語)と seed。値 = 道具なし 0.122・式だけ 0.108 / 0.108・宣言 0.318・指示 0.225 / 二回目 0.086(G1 落ち・判定なし)。帯 = olm124 戻る(|Δ113| < 0.06)・olm125 上がる(Δ124 ≥ +0.06・境の上 2 行)・olm127 判定なし(参考値は 戻る の帯)。隣と統計的に分けられないことも言う。
  2. **式を数値で使った行は折り返しを退けるか。退けた後、証明の欄はどうなるか。**
     - 基準: olm125 の計算した 18 本のうち REJ6 15 本(= 15 / 15 の折り返しの計算)・次の候補は共線 0 本・等距離 9 本・JSON なし 5 本(上限)・退けた後に証明の欄で線対称 3 本(b1_j11・b1_j17・b2_j19)。六腕の b2_j07 の型 = 0 / 3 / 2 / 1 / 3 / 0 本(olm127 の 0 本は退けた 6 本のうち 5 本が上限で証明の欄に至らなかった分 = 「直った」ではない)。olm127 では退けた命題にそのまま戻り続ける行 2 本(b2_j08 343 回・b1_j13 542 回)。等距離(= apex・真)は olm125 では数値で確かめられていない(退けたのは折り返しだけ)。olm127 では b0_j00・b2_j09 が数値で確かめる。
  3. **計器を替えると判定は変わるか。**
     - 基準: v3 → v6 で五腕の率は +0.000 / +0.023 / +0.027 / +0.054 / +0.050。凍結の判定 7 / 7 同じ。olm118 Q3 は v4 / v5 の「間」が v6 で「変わらない」(v3 と同じ値 +0.0387)= 計器の窓の落としで帯の名が動いていた。「同じ」と「落とし」を分けて言えること。

## §0. 一本の筋(章の順・状態は 18〜22 を目安に・作り手が決める)

| 章 | 中身 | 主な data |
|---|---|---|
| A 場面 | A0: 読み方(問いの文 → OLMo が JSON を書く → 証明の欄を計器 v3 / v6 で読む → 本文の計算と退けを読む)。A1: **実在の二行**を並べる(同じ問いの文 olm125・同じ座標・どちらも折り返しを計算して退けた): S1 = olm125 `b1_j17`(退けた後に証明の欄で「the inner common tangent is symmetric with respect to O1O2」= 退けが commit に届かない)と S2 = olm125 `b0_j16`(退けた後の証明の欄に線対称なし)。本文の退けの文(rej6_first)と証明の欄の逐語を並べる | inventory の `scenes`・`arms.olm125.rows` |
| B 道具の段と計器 | B0: 三種の Tool の段(逐語・字数・問いの文の md5)。B1: 計器 = 線対称の印・外接線の印・退け(述語の名と較正の数・陰性統制 0 / 20)。B2: 関門 G1(0.75・六腕 0.833 / 0.800 / 0.767 / 0.750 / 0.750 / 0.667 = olm122 と olm127 が落ち)。B3: 判定の帯(olm124 の 戻る / 残る・olm125 の 変わらない / 上がる・olm127 の 残る / 戻る は G1 落ちで判定なし = 参考値 0.086 を帯の上に「判定なし」の札で) | inventory の `prompts`・`instrument_lineage`・`frozen` |
| C 六腕の表(本題) | 証明の欄の線対称の率(v3 = 判定・v6 = 参考)を **一つの目盛り**に七腕(道具なし・等半径の対照・宣言・式だけ ×2・指示 ×2・G1 落ちの二腕は「判定なし」の札)。帯の境を線で。計算した率(REFL_CALC)・道具の名指し(tool_named)・MIDO3 / EQ の率・外接線の印(0.24〜0.27 で不変)を並べる。**行の点を drag で選ぶと、その行の証明の欄と退けの文が出る** | inventory の `arms.*.agg`・`rows` |
| D 計算した行 | 計算した行 / しない行で割った証明の欄の線対称(olm125 2 / 9 対 7 / 31・olm124 1 / 7 対 3 / 30)・退けの率(REJ6 / 計算した行 = olm125 15 / 18・olm124 11 / 15・olm119 11 / 13・olm122 6 / 12・olm127 6 / 10)・退けた後の類(olm125: MIDO3 0・EQ 9・NONE 5)・b2_j07 の型(六腕 0 / 3 / 2 / 1 / 3 / 0)・退けた命題に戻り続ける行(S8 olm127 b2_j08・S10 b1_j13)・証明の欄が数値だけの行(S9 olm127 b2_j09)。T の中央値(olm125 計算した 8,749 対 しない 255・olm127 12,288 対 397)と上限 | `arms.*.agg.calc_split` / `noncalc_split` / `calc_cls` / `REJ6_then_proof_LN6`・rows |
| E 見た形 / 見ていない形 | 等半径の対照(olm117): 線対称 0.122 → 0.152(変わらない)・点対称 0 → 4 / 46(増える)・MIDO3 0.34 → 0.74・外接線 0.244 → 0.283(変わらない)= 記憶の前提が**真になる図**では類が共線に寄る。一般の図 = 前提が偽。**判定は olm118 の帯(v3)**・v6 の値は参考 | `arms.olm113` / `arms.olm117`・`frozen["olm118(olm117 vs olm113)"]` |
| F 計器の系譜 | v3 → v4 → v5 → v6 の直し(取りこぼし・拾いすぎの逐語 = olm124 b1_j01 の式の写し・olm124 b0_j00 の直の目的語・olm113 b2_j03「, so the line TcTh is thus parallel」)と olm118 Q3 の帯の往復(変わらない → 間 → 間 → 変わらない)。凍結の判定 7 / 7 同じ | `instrument_lineage`・`frozen["olm126(v6)"]`・rows の `proof_v6_ln_hits` |
| G 次の問い(共読の一巡) | 先生の問い(逐語)「olmXシリーズから評価関数を導出できますか？」と主 session の答え(L3・採否は先生): 自己対戦の四つの部品(答え合わせ / 読み / 読みが先生 / 見ていない形)に当てた表(MEMO §3)。次の札の候補(採否は先生・推しの印は付けない): 対照の一行(reflection の語だけ置く)・v7(退けの語 not obvious(ly))・G1 の較正の引き直し・退けの直後の候補を数える計器(S8 / S10 の型)・退けが commit を支配する仕組み。最後に A1 に戻る | `conversations/2026-11-04/factcheck_yt__A1acg0ZTKs/MEMO_…md` の §3・§4(文だけ・数はこの表の材料から) |
| H 台帳 | 言える / 記述 / 読み(L3)/ 言えない | §3・§4 |

- 入口(A1)は実在の行で(模式図にしない)。成功と失敗を並べる型: S1 と S2 は同じ問いの文・同じ座標・同じ計算・同じ退け・同じ目盛り。そろえ方 = 退けの文(rej6_first)の位置。**計器と証明が別**であることを A1 の札に書く。

## §1. data(読むだけ・この表の外は読まない)

### 1-1. 凍結の出力(主)
| file | 中身 |
|---|---|
| `/Users/manabu/lancedb-rag/conversations/2026-11-04/explainer_moy2_line/inventory/moy2_line_inventory.json`(md5 = §2) | 主 session の棚卸し: `prompts`(三種の Tool の段の逐語・問いの文の md5)/ `arms.<腕>` = `label`・`agg`(n・parsed・status・cls・n_proof・proof_v3 / proof_v6 の数と率・REFL_CALC・tool_named・REJ6・REJ6_then_proof_LN6・calc_split / noncalc_split・unparsed の頭・T の中央値・hit_cap)・`rows`(行ごと: key・seed・cls・status・T・hit_cap・conjecture・**proof(証明の欄の全文)**・calc・mention・first_calc・tool_named・proof_v3・proof_v6・proof_v6_ln_hits(形と逐語)・body_v4・rej6・**rej6_first(退けの文)**・head(本文の頭 240 字))/ `frozen`(各 read.json の判定の記録)/ `scenes`(述語つきの場面 S1〜S10・S8 / S10 は loop_count つき)/ `instrument_lineage` / `recount_vs_read_json`(照合 N / N) |
| 同 `moy2_line_inventory.out`・`moy2_line_inventory.py` | 照合の値と材料の md5(script は読むだけ・走らせない) |
| `/Users/manabu/lancedb-rag/ConstructGap/exp/olm118/read.json`・`olm119/read.json`・`olm122/read.json`・`olm124/read.json`・`olm125/read.json`・`olm126/read.json`・`olm127/read.json` | 凍結の判定と帯。**第二経路**: あなたの pack が inventory の rows から率と数を数え直し、各 read.json の値(Q1 / Q2 / gates / proof_count)に合わせる |

### 1-2. 札の記録(説明・数は 1-1 から)
- `conversations/2026-11-03/` の PREREG・RESULT olm118(v3)・olm119・olm121(v4)・olm122・olm123(v5)・olm124 / `conversations/2026-11-04/` の olm125・olm126(v6)・olm127・系列の RECORD `conversations/2026-11-04/RECORD_moy2_reflection_tool_line_olm113_127_closure_20261104.md`(一枚の表・凍結の判定・計器の系譜・読み・言えないこと)。
- `conversations/2026-11-04/factcheck_yt__A1acg0ZTKs/MEMO_youtube_selfplay_alphazero_factcheck_and_house_contrast_evaluation_function_20261104.md` の §3・§4 = G 章の文(数は inventory から)。
- **読まない物**: 他の entry の folder・memory・ConstructGap/exp の gen.json(本文の全文は inventory の head と proof だけで足りる・読まない)・script。

## §2. 照合用の値(主 session が data から読んだ値・合わなければ data が正しい)

出力 = `inventory/moy2_line_inventory.out`(inventory の JSON の md5 = `3190663eadc56b6ea426472b0551624e`・.out の末尾と一致)。
1. 証明の欄の線対称 v3(判定): olm113 5 / 41 = 0.122・olm117 7 / 46 = 0.1522・olm119 14 / 44 = 0.3182・olm122 4 / 37 = 0.1081・olm124 4 / 37 = 0.1081・olm125 9 / 40 = 0.225・olm127 3 / 35 = 0.0857(G1 落ち・参考)。
2. 同 v6(参考): 5 / 41 = 0.122・7 / 46 = 0.1522・15 / 44 = 0.3409・5 / 37 = 0.1351・6 / 37 = 0.1622・11 / 40 = 0.275・olm127 3 / 35 = 0.0857。
3. 取れた行: 50 / 50 / 48 / 46 / 45 / 45 / 40(/ 60)。関門 G1 = 0.75(olm124 以降)・olm122 は当時の境 0.80 で落ち(判定なし)・olm127 は 0.75 で落ち(判定なし)。
4. 計算した行(REFL_CALC): olm113 6・olm117 0・olm119 13・olm122 12・olm124 15・olm125 18・olm127 10。退け REJ6: 0・0・11・6・11・15・6。b2_j07 の型: [] / [] / [b0_j13, b1_j06, b2_j08] / [b1_j11, b2_j07] / [b2_j07] / [b1_j11, b1_j17, b2_j19] / []。
5. 計算した行 / しない行の証明の欄の線対称(v3): olm125 2 / 9 と 7 / 31・olm124 1 / 7 と 3 / 30・olm119 3 / 10 と 11 / 34・olm122 1 / 9 と 3 / 28・olm113 0 / 3 と 5 / 38・olm127 0 / 3 と 3 / 32。
6. MIDO3 の率(取れた行): 0.34・0.74・0.6042・0.587・0.5111・0.4444・0.5。EQ: 0.32・0.0・0.1667・0.2609・0.2667・0.3111・0.125。
7. 外接線の印 v3(証明の欄): 10 / 41・13 / 46・12 / 44・9 / 37・9 / 37・10 / 40・6 / 35。v6: 10・13・12・8・9・10・6。
8. 凍結の判定: olm118 Q1 変わらない(+0.0302)/ Q2 増える(+0.087)/ Q3 変わらない(+0.0387)・olm119 Q1 上がる(+0.1962)・olm124 Q1 戻る(Δ113 −0.014)/ Q2 間(0.25)・olm125 Q1 上がる(Δ124 +0.117)/ Q2 変わらない(0.30)・olm126 Q1 直った / Q2 同じ / Q3 通らない・olm127 G1 ✗(40 / 60)/ Q1 判定なし(参考 0.0857)/ Q2 変わらない(0.1667)。
9. 計器の系譜: 較正 54 / 74 / 98 / 144・olm118 Q3 の帯 v3 変わらない(+0.0387)→ v4 間(+0.0631)→ v5 間(+0.0631)→ v6 変わらない(+0.0387)。陰性統制 prf5 OUTER6_a 0 / 20・PT_a + LN6_a 0 / 20。
10. 場面: S1 = olm125 `b1_j17`(EQ・T 4,315・rej6 true・証明の欄 LN6 true)/ S2 = olm125 `b0_j16`(EQ・T 7,335・rej6 true・証明の欄 LN6 false)/ S3 = olm125 `b1_j16`(NONE・上限・「not necessarily true unless the circles are congruent」)/ S4 = olm125 `b1_j09`(MIDO3・T 1,000・計算なし・「it likely relates to the symmetry over the line O1O2」)/ S5 = olm125 `b0_j18`(問いの文の丸写し)/ S6 = olm124 `b2_j07` / S7 = olm119 `b1_j06` / S8 = olm127 `b2_j08`(NONE・上限・計算なし・「But as above, the determinant is not zero」343 回)/ S9 = olm127 `b2_j09`(EQ・T 3,570・計算あり・退けの語なし・証明の欄「both are sqrt(14.764) ≈ 3.838」= 数値だけ)/ S10 = olm127 `b1_j13`(NONE・上限・計算あり・「but already checked」542 回)。
11. 照合 `recount_vs_read_json` = 20 / 20 ok(数は .out)。

## §3. 言い方と限定(全画面の札・台帳の言えない)

- **全画面の限定の札**(その画面の data に当てはまる物だけ・行ごとに確かめてから):
  - OLMo-3 32B base・温度 0.7・一つの問い(moy-2)・一つの座標・60 行ずつ・腕ごとに seed が違う。
  - 計器は語の印(正規表現)。証明の正しさは読まない。線対称・外接線の印・退けは「書いた語」の印であって、model の中身ではない。
  - 判定は v3 と凍結の帯。v6・pool・Fisher は参考。olm122・olm127 は G1 落ちで判定なし。
  - 小 n: 証明の欄 35〜46 行・計算した行 6〜18 本・b2_j07 の型 0〜3 本。
  - 等半径の対照(olm117)は olm118 の判定。v6 の値は参考。
- **使わない語**: 「model が考えた・分かった・気づいた・理解した・思い出した・知っていた・計算して確かめた(主語が model の心)」。「前提が呼ばれた」は「証明の欄に線対称が出た」に。「記憶」は「記憶の前提(等半径の図で真になる文)」の形でだけ、L3 の札つきで。類の正誤は配置の事実としてだけ(MIDO3 偽・EQ 真・線対称 偽・外接線の印 偽)。各行の証明の正しさは読まない(「正しい証明」と書かない)。「評価関数を導出できる / できない」は G 章の L3 の中でだけ。
- **言えない(平叙文で)**:
  - 三種の文の順(宣言 > 指示 > 式だけ)は 60 行ずつの Fisher では隣と分けられず、指示の文の二回目(olm127)で一回目に見えた物は再現しない。順は読み。olm125 の 0.225 が一回の揺れとも指示の効果とも言わない。
  - olm125 の上がりを指示の文だけに帰さない(reflection の語が一度多い・問いの文が 90 字長い)。
  - 退けた後に証明の欄で線対称が戻る 3 本は、同じ命題の退けと復活とは限らない(REJ6 ∧ LN6 の共起)。
  - olm127 の b2_j07 の型 0 本を「直った」と言わない(退けた 6 本のうち 5 本が上限で証明の欄に至っていない)。b2_j08 / b1_j13 の繰り返しを「model が迷った」と言わない(退けの文の直後に同じ候補の文が出る、という本文の記述)。
  - EQ(等距離)は配置の事実として真(apex)だが、各行の証明の正しさは読まない。等距離を数値で確かめた行は olm125 に 0・olm127 に 2(b0_j00・b2_j09)= 「apex に着いた」と「確かめた」を混ぜない。
  - OLMo が「読みをしていない」とは機構として言わない(候補の木が本文に無い、という記述)。
  - 評価関数が「導出できない」は主 session の読み(L3)で、data の判定ではない。frontier の中は見ていない(この図に frontier の data は無い・陰性統制の prf5 の証明 20 本を除く)。
  - 正しさの率は測っていない。
- **先生の問い**(G 章でだけ・逐語・L3): 「olmXシリーズから評価関数を導出できますか？」。並べてよい事実 = 計算した行の退けの率・b2_j07 の型・MIDO3 0 → EQ 9(apex に着くが証明の欄は記憶の線対称 3 本)・等半径の対照。言えない = この図の data から評価関数の学習可能性は言わない。

## §4. 台帳(下書き・各行に出所 = file と key)

- **言える(L1)**: 式だけの二回は 0.108 / 0.108(olm122 参考・olm124 戻る)。宣言の文は 0.318(olm119 上がる・Δ113 +0.196)。指示の文は 0.225(olm125 上がる・Δ124 +0.117)、二回目 olm127 は G1 落ち(40 / 60)で判定なし(参考 0.086・olm127 Q1)。olm127 Q2 変わらない(0.167)。計算した行は 15 → 18(olm125 Q2 変わらない)→ 10(olm127)。道具の名指し 11 → 18 → 7。退け 15 / 15(olm125)・6 / 6(olm127)(v6・参考)。olm118: 等半径で線対称 変わらない・点対称 増える・外接線 変わらない。olm126: 凍結の判定 7 / 7 同じ・olm118 Q3 は v6 で 変わらない に戻る。
- **記述(凍結の判定でない)**: v6 の値・pool 120 行・Fisher・計算した行 / しない行の分け・MIDO3 → EQ・T の中央値・取れなかった行の形。
- **統制 ✗ / 判定なし**: olm122(G1 46 / 60 < 0.80)・olm127(G1 40 / 60 < 0.75)= 参考値だけ。
- **読み(L3・採否は先生)**: RESULT olm125 §4(道具の段の文が「線対称が答えだ」の手掛かりとして読まれる・計算は試した命題だけ退け次は記憶から)・RESULT olm126 §4(三つの直しは較正の外でも同じ向き)・RESULT olm127 §4(退けた後の行き先は三つ・退けた命題が次の候補に戻り続ける)・RECORD §4・MEMO §4(評価関数)。誰の読みか(主 session)を書く。
- **言えない**: §3 の言えないを全部、平叙文で。

## §5. 色

- skill §4 の既存の意味を保つ: 青 = 正しい結びの組・橙 = 引き寄せ(attractor)の組は moy-1 の図解の意味。この図では **MIDO3 = 橙(共線 / 中点の引き寄せ・偽)**・**EQ = 青(apex・真の結び)**・NONE = 灰・OTHER = 中立。線対称の印・外接線の印は形(塗り / 輪・実線 / 破線)で分け、色を足さない。
- 退けの線(REJ6)は中立の灰。帯の境は灰の破線。

## §6. 作るもの・進め方

- skill §2 の entry の一式(build.mjs・pack_*.py・data.mjs・i18n.js・widget・demo_marimo.py・demo_jupyter.ipynb・check_claims.py・captures/・CLAIMS.md・NOTES.md・README.md・SCRIPT_yukkuri.md)。頁 4 本(暗 / 明 × ja / en)。
- **drag の軸(必須)**: C 章と D 章で **行の点を drag で選ぶ**と、その行の証明の欄(全文)・退けの文・類・T が連れて動く。C 章の七腕は **一つの目盛り**(0〜0.4)に並べ、帯の境(olm124 の 0.048 / 0.168・olm125 の 0.168 / 0.285)を線で。腕を drag で選ぶと、その腕の Tool の段の逐語が出る。
- 検査(skill §5)・撮影(skill §6)・台本(≤ 150 秒・A = 聞き手 / B = 解説・実在の character の名や絵を使わない)。
- 返すもの ≤ 10 行。

## 訂正(2026-11-04 午後・図解の作り手の照合で見つかった発注書の誤り・上の本文は書き換えない・data が正)

1. §6 / C 章の「帯の境(olm124 の 0.048 / 0.168・olm125 の 0.168 / 0.285)」は誤り。PREREG のとおり 0.048 / 0.168 は **olm125** の Q1 の帯の境(|Δ124| < 0.06・0.108 を挟む)、0.165 / 0.285 は **olm127** の帯の境(残る の下端・上がる の下端)、**olm124** の 戻る の帯は 0.062 / 0.182(|Δ113| < 0.06・0.122 を挟む・間 0.182〜0.258・残る 0.258〜0.378)。各腕の境はその札の PREREG から引く。
2. D 章の「退けの率(REJ6 / 計算した行 = … olm119 11 / 13・olm122 6 / 12 …)」は、全行の退け(REJ6)を計算した行の分母に載せた誤り。計算した行の中の退けは olm119 **10 / 13**(b2_j08 は計算しない行の退け)・olm122 **5 / 12**(b1_j19 も同じ)。全行の退け 11・6(§2 の 4)は正しい。
3. D 章の T の中央値「olm125 計算した 8,749 対 しない 255」は丸め。data は 8,748.5 / 254.5。
4. 主 session が inventory の行(`arms.*.rows` の `rej6`・`calc`・`seed`・`hit_cap`)で確かめた。RECORD §1 の seed と olm113 の上限の誤りは RECORD の訂正に書く。
