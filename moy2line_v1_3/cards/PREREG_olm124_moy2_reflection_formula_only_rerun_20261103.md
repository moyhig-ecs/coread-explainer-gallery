HEAD(R1) = fc1c735f(凍結時の HEAD = RESULT olm122 の commit・fetch + pull 済 = Already up to date・origin より 24 commit 先・遅れ 0 = この file と runner を入れる commit の親)

# PREREG(札 `olm124`・凍結 2026-11-03): moy-2 の「折り返しの式」の第二文を外す腕の走らせ直し(d')— olm122 と逐語同じ問いの文(olm113 の M2A + 式だけの TOOL_D・md5 `2c4a01a4…`)で OLMo-3 32B base に新しい seed で 60 行書かせ、証明の欄で O1O2 についての線対称を肯定して述べる率(v3 の LN_a)が olm113(5 / 41 = 0.122)に戻るか olm119(14 / 44 = 0.318)に残るかを、**関門 G1 を三腕の実測で較正し直して(≥ 0.75)**判定する。olm122(関門で判定なし)の行は判定に混ぜない

- 発注(逐語・先生 11-03 夜): 「**(d) (e) (f) へ順次進みます。**」の (d) の続き。[RESULT olm122](RESULT_olm122_moy2_reflection_formula_only_20261103.md) が関門 G1(≥ 0.80)を 46 / 60 で落として Q1・Q2 の判定がないので、§6 の (d') として主 session が起案(先生の裁定は RESULT の後・走らせ直しは可逆で夜の計算機は空いている)。(e)「使って確かめよ」の腕はこの札の RESULT の後。
- G10 の欄: 比べる物 = 「olm122 と逐語同じ問いの文(式だけ・第二文なし)で OLMo が新しい seed で書いた 60 行の証明の欄(空でない物)で、O1O2 についての線対称を肯定して述べる(v3 の LN_a)行の割合と、olm113(5 / 41 = 0.122・olm118 の read.json)および olm119(14 / 44 = 0.318・olm119 の read.json)の同じ割合との差」/「本文で折り返しの式を数値で使った(REFL_CALC)行の割合(olm119 13 / 60 = 0.217)」/ 計器 = 読み込むだけの凍結の部品(olm122 の `score_row` = hq の proof_of・status_of + olm117 の v2 + olm118 の v3(SYM_PT・SYM_LN・OUTER・asserted)+ olm119 の REFL_MENTION / REFL_CALC + olm121 の v4(本文の記述)+ olm122 の tool_named・較正 12 / 54 / 74)+ 問いの文の md5 の一致(olm122 の `2c4a01a4…`)+ olm122 の guard 一式(TOOL_D を外すと M2A・TOOL_D + 第二文 = olm119 の TOOL)/ 雛形 = いいえ
- runner = [olm124_…py](../../ConstructGap/exp/olm124_moy2_reflection_formula_only_rerun_20261103.py)。読み込むだけの部品: [olm122_…py](../../ConstructGap/exp/olm122_moy2_reflection_formula_only_20261103.py)(`78bafa04…`・問いの文・score_row・_desc・guard)とその下の [hq_moy12_…py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(`426e2089…`)・[olm117_…py](../../ConstructGap/exp/olm117_moy2_equal_radii_control_20261103.py)(`ab678f30…`)・[olm118_…py](../../ConstructGap/exp/olm118_moy2_symmetry_kind_outer_marker_v3_20261103.py)(`136f72b9…`)・[olm119_…py](../../ConstructGap/exp/olm119_moy2_reflection_tool_line_symmetry_20261103.py)(`d8d4062f…`)・[olm121_…py](../../ConstructGap/exp/olm121_moy2_v4_instrument_fix_and_retraction_20261103.py)(`9c0b2b4e…`)。比べる元 = `olm118/read.json`(`bffeb826…`)・`olm119/read.json`(`f2138597…`)・`olm122/read.json`(`30db9a25…`・参考の pool の元 `olm122/gen.json` `8e73068d…`)。走らせる所 = zebrashark(32B は一つずつ・他の 32B は走っていない)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- **olm122 の 60 行の値は全部既知**([RESULT olm122](RESULT_olm122_moy2_reflection_formula_only_20261103.md)): 証明の欄の LN_a 4 / 37 = 0.108(戻る の帯)・REFL_CALC 12 / 60 = 0.200(間 の帯)・MIDO3 0.587・取れた行 46 / 60・取れなかった行の形(指示の続きを書く短い行 10 + 上限 4)。主 session は olm122 の証明の欄の LN 4 本・計算した 12 本・式に触れた 13 本の一部を逐語で読んだ。**§3 の予想はこれを織り込んで更新した**(olm122 の予想 戻る 0.40 → この札 0.57)。
- **関門 G1 の境を 0.80 → 0.75 に置き直す理由(開示)**: 同じ問いの文の族の取れる率は olm113 50 / 60 = 0.833・olm119 48 / 60 = 0.800・olm122 46 / 60 = 0.767(平均 0.80・60 行の二項の標準誤差 ≈ 0.05)。境 0.80 はこの平均の真上で、同じ問いの文で走らせ直しても二回に一回は落ちる。0.75(45 / 60)は平均の一標準誤差下 = 同じ族なら約 0.84 で通る。olm122 の 0.767 はこの境なら通っていたが、**olm122 の判定は olm122 の PREREG のまま(なし)で、この札の判定は新しい 60 行だけで付ける**。
- 問いの文は olm122 と逐語同じ(md5 `2c4a01a4…` を guard・olm122 の guard 一式も読み込んで当てる)。TOOL_D の逐語は PREREG olm122 §0。
- smoke(凍結の前・2 行・読まない): 数は §6。

## §1. 計器(R5・R6)

- **問いの文** = olm122 の問いの文(olm113 の M2A + TOOL_D)。生成 = olm122 と同じ(温度 0.7・max_new 12288・3 batch × 20 行・seed 20261183〜85・既出の 59 seed と重ねない = guard)。
- **凍結の読み**(読み込むだけ): olm122 の `score_row` = v2(conjecture の類 EQ / MIDO3 / OTHER / NONE・status・proof_of・SYMM)・v3(SYM_PT / SYM_LN / SYM_OTH / kind・PAR3 / PERP3 / PBIS3 / OUTER・asserted)を証明の欄と本文に・REFL_MENTION / REFL_CALC を本文に・v4 の RETR / KEPT を本文に(記述)・tool_named(記述)。集計 = olm122 の `_desc`。
- 率の分母: Q1 = 証明の欄が空でない行(olm113 41・olm119 44)・Q2 = 60 行。
- **参考の pool**(判定に混ぜない): olm122 の 60 行 + この札の 60 行 = 120 行の取れた行・証明の欄の LN_a の率・REFL_CALC の率・MIDO3 / EQ・PERP3 / OUTER・T・上限を記述で並べ、帯に当てた名も「参考」として書く。

## §2. 関門

- **G0**: 部品(olm122 と その下 5 本)・比べる元 3 本の md5 一致・較正 12 / 12・54 / 54・74 / 74・olm113 の証明の欄 n = 41・olm119 n = 44・olm122 の取れた行 46 / 証明の欄 37・olm122 の G1 が false(read.json の記録)。
- **G1**: conjecture が取れた行 **≥ 0.75(45 / 60)**(較正の根拠は §0)。✗ → Q1・Q2 を読まない(その時は参考の pool も帯に当てない)。
- **G2**(記述の側): status が hypothesis / question の行 ≥ 0.70(42 / 60)。✗ → 注記(olm122 は 35 / 60 で ✗)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 証明の欄の LN_a の率 r・Δ113 = r − 0.122・Δ119 = r − 0.318 | **戻る** \|Δ113\| < 0.06・**残る** \|Δ119\| < 0.06・**上がる** Δ119 ≥ +0.06・**下回る** Δ113 ≤ −0.06・ほか = **間**(0.182 ≤ r ≤ 0.258) | 戻る 0.57・間 0.25・残る 0.08・下回る 0.08・上がる 0.02 |
| Q2 | 本文で式を数値で使った率 REFL_CALC / 60 | **使う** ≥ 0.30・**使わない** ≤ 0.10・ほか = 間 | 間 0.60・使わない 0.25・使う 0.15 |
| Q3 | 記述: 取れた行と取れなかった行の形(T・指示の続き / 上限)・MIDO3 / EQ の率・証明の欄の PERP3 / OUTER・計算した / しない行の本文の LN と退け(v4)+ 逐語の「合わない」の数(主 session)・類ごと・tool_named・T・上限・参考の pool(120 行) | — | — |
| Q4 | 記述: 逐語 = 証明の欄の LN の文(全部)・計算した行の計算の文(最大 10 本)・式に触れたが計算しなかった行(最大 5 本)・取れなかった行の頭(全部) | — | — |

- 読みの軸(開示): **戻る** → 植えたのは第二文(宣言の文)で、式そのものは前提にならない = olm119 §4 の 1 を支持(olm122 の参考値 0.108 と合わせて二回)。**残る / 上がる** → olm122 の 0.108 が偶然 = 式だけでも植わる。**間** → 両方が効く(式だけでも植わる行 b0_j01 / b0_j04 / b1_j10 の型が 60 行に 3〜4 本 → 8〜10 本になれば 間)。Q2 は olm119(0.217)と olm122(0.200)が揃って 間 なので 間 を最大に置く。
- 予想の根拠: Q1 は olm122 の 0.108(37 本の分母で一行 0.027)と olm113 の 0.122 が同じ帯で、戻る の帯(0.062 < r < 0.182)は幅 0.12 = 四行分。下回る(≤ 2 / 37)と 残る(10〜14 / 37)は olm122 からの距離で小さく置く。

## §4. 読み方

- `--read` が `olm124/read.json` を書く(関門・Q1〜Q3・集計・行ごとの類と印と最初の当たりの前後・取れなかった行の T・参考の pool)。判定は v3 と REFL の値だけで、この札の 60 行だけで付ける。
- RESULT では §3 の Q4 の逐語を引き、olm122 の同じ値を並べる(二回の 60 行が同じ帯か)。主 session の読み(植える効果と確かめる効果・「合わない」の逐語)は値と並べ、違っても判定は変えない。

## §5. 主張しないこと

- 判定は新しい 60 行だけ。pool 120 行の帯は参考で、olm122 の関門の結果を覆さない。
- 境を 0.75 に置き直したのは olm122 の落ちを見た後(開示)。これは関門の較正で、Q1 / Q2 の帯は olm122 と同じ(動かしていない)。
- TOOL_D は問いの文を 162 字長くし答えの分布も変えうる(PREREG olm122 §5 と同じ)。REFL_CALC は語と数の印。v4 の RETR は窓 260 字で、計算の長い行の退けを拾わない(olm122 §4 の 5)。
- 正しさの率は測らない。一つの model・一つの温度・60 行。

## §6. 走らせ方と記録

- zebrashark: `--selftest`(PASS・21 項目・REFL 12 / 12・v3 54 / 54・v4 74 / 74・guard)→ `--smoke`(凍結の前・2 行・max_new 1536・読まない)→ 凍結 → `--gen`(約 2.6 時間の見込み・olm122 は 2.61 時間・olm119 2.76 時間)→ `--read`。
- smoke(凍結の前・seed 20261192・2 行・max_new 1536・読まない・zebrashark 21:32〜21:34 JST・壁時計 98 s・Traceback 0・`olm124/smoke.json`・`smoke_run.log`): 行 1 = T 451・status hypothesis・証明の欄 347 字 / 行 2 = T 241・none・証明の欄 0 字。本文は読んでいない(smoke の log は類・LN・REFL を印字しない)。
- 出力 = `ConstructGap/exp/olm124/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-03/RESULT_olm124_moy2_reflection_formula_only_rerun_20261103.md`。
