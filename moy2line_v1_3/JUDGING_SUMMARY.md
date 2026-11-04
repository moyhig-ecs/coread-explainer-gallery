# JUDGING_SUMMARY — the cold (sealed) judging of this explainer, copied from the house records

This entry was judged by readers from a different model family than its maker, under a seal (the readers were not told which maker made which entry), and the judgments were not pooled. Three rounds: **v1** (two entries by two makers; the seal leaked through commit messages — disclosed below, so that round is not used to calibrate the rubric), **v1.1** and **v1.2** (the seal held; the readers read the entry only). **v1.3** was accepted without re-judging (five small fixes; no number changed).

The maker of this entry is **Opus 5.5 (effort xhigh)**; in the sealed rounds it was called *entry Q* (the other maker's entry, by Sonnet 5.5 max, was *P*). Readers: Fable 5.1 (the house's `judge-cold` role) and Sonnet 5.5 (a read-only reader); in v1 also Opus 5.5 for P. The rubric files (JUDGE_criteria v1 / v1.1 / v1.2) and the readers' full texts (JUDGE_*) are house records and are not in this bundle; the sections below are copied verbatim from the house RESULT files (Japanese), with house paths masked.

Rubric items: **E1** = would an editor pass the figure (facts and numbers match the cards; display rules) · **E2** = can a video be made from the script · **E3** = can the three questions Q1 / Q2 / Q3 be answered from the figure · **E4** = is the instrument chain (what the readout can and cannot say) stated.

---

## v1 (2026-11-04 afternoon) — the seal leaked; disclosed

## §0 封の破れ(先に書く・主 session の落ち度)

- 読み手の subagent は起動時に harness から「直近 5 commit の message」を受け取る。主 session は eb98bcc4(14:05)の message に封の対応「札 P = Sonnet max / Q = Opus xhigh」を、b2db2fa3(14:40)の message に Q の Sonnet の判定の要約(E1 / E2 / E4・直す点)を書いた。
- Sonnet(Q・14:10 発火)= eb98bcc4 が HEAD → 封の対応が見えた(開示なし)。Opus(P)と Fable(P + Q)= b2db2fa3 が HEAD → 封の対応 + Q の判定の要約が見えた。**二人とも自分から開示**し「根拠に使わず、見なかったものとして判定した・作り手は推測も記載もしない」。
- memory `feedback_eval_leak_via_commit_messages`(10-19・skill の試験で同じ漏れ)の再演。守るべきだった順 = 受領の commit(message に封・判定を書かない)→ 審査 → SEALED と判定の commit。
- 従ってこの審査は「盲検」ではない。**三人の一致率で物差し(基準 v1)を較正する用途には使わない**。個別の指摘は撮影で確かめられる事実なので、そのまま使う(§2 で主 session が確かめた物に ✓)。

---

## v1.1 (2026-11-04 afternoon) — RESULT_judging v1.1 §1 (verdict table) and §2 (remarks)

## §1 判定の表(合算しない)

| 読み手 | E1 editor | E2 動画 | E4 計器の鎖 | E3 Q1 / Q2 / Q3 |
|---|---|---|---|---|
| Sonnet | 直せば通る(中・照合 11 件 全部訂正後の値で一致) | 手を入れればできる(中) | 言えている(中) | 答えられる / 答えられる / 答えられる |
| Fable | 直せば通る(事実 高・境 中・照合 11 項目 全部一致・数の誤り 0) | できる(中〜高) | 言えている(高) | 答えられる / 答えられる / 答えられる |

- 一致: **E1 同じ**(直せば通る・二人とも「数の誤りは無く、残るのは表示と台本」)。**E4 同じ**(言えている)。**E3 同じ**(三問とも 答えられる・v1 の「ほぼ」が消えた)。**E2 は割れる**(Sonnet 手を入れれば / Fable できる)= v1 の Q と同じ割れ方。
- v1 → v1.1(同じ族の読み手で): Fable の E4 は「言えている(43 / 47 の札を除く・中)」→「言えている(高)」(F1 で旧分母が消えた)。Fable の E1 の確信度は 高 → 事実 高・境 中(残るのが表示だけになった)。Sonnet の E1 は 中〜高 → 中(状態 9 の p 0.014 と「分けられない」の緊張 = F4 で足した状態が新しい指摘を生んだ)。E3 Q2 は二人とも「ほぼ」→「答えられる」。

## §2 指摘(★ = 二人・✓ = 主 session が撮影で確かめた)

- ★ 状態 0(最初の 10 秒)は二行の対比で瞬間は見えるが、差が chip の文字と段の有無だけで形や色の差が無く、画面の下半分が空(Sonnet・Fable)。
- ★ 状態 14(等半径の対照)の色: Sonnet = olm113 の MIDO3 の棒が灰(NONE の色)/ Fable = 橙が olm117 の 0.740 に在り凡例「この図では偽」と題「記憶の前提が真になる図」が食い違う。同じ画面の同じ欠けを別の側から(二人)。
- ★ 状態 4 の数字(46 / 60・40 / 60)が破線(0.75 / 0.80)の上に乗る(二人)。
- ★ 状態 13 の olm127 の角(◇ b2_j09・b2_j08・◇ b0_j00)が混む(二人・作り手自身の NOTES)。
- ★ 状態 0 の右上の身分の行が三行に折れて「逐語」が panel の縁に触れる(二人)。
- ★ 状態 19 の台帳と 12 px 級の札は動画で読めない(二人)。状態 8 の 420 本の全点灯は森(二人)。
- Sonnet だけ: 状態 9 の題「分けられるか」と台本「隣と分けられない」が、同じ画面の olm127 対 olm119 p 0.0142(参考の目盛りの内側)と緊張する → 「7 本のうち 1 本は参考の目盛りの下」の一行が要る / 状態 0 の「同じ計算」は折り返す点が違う(S1 は Th・S2 は Tc)ので「同じ種類の計算」に / 状態 3 の olm126 Q3 の一行(F7)が小さく淡い / 台本が cue しない状態が 9 つ(3・5・7・8・10・14・15・17・18)で E4 の鎖の一部が声に乗らない。
- Fable だけ: ✓ 帯の境の数(0.062 / 0.182・0.048 / 0.168・0.165 / 0.285)が video の撮影に無い(CLAIMS K33〜K35 は「印字する」と書く)/ 状態 17 の表「b2_j07 の型 3 / 2 / 1 / 3 / 0」は五つの数で腕の名が無く状態 12 の六腕と並びが違う / 台本 19 行目の「まで」(olm125 の 上がる も凍結の判定)/ 台本 02 行目の「だけ」は「二行のうち」が無いと olm125 全体に読める(**= BRIEF v1.1 F3 の指定そのもの・主 session の責任**)。
- 主 session の責任の切り分け: F3 の文(台本 02 行目)と台本 19 行目の「まで」(v1 から)は発注と RECORD §4 の読みに由来。状態 9 の緊張は F4(Fisher の追加)が生んだ。

---

## v1.2 (2026-11-04 evening) — RESULT_judging v1.2 §1 and §2

## §1 判定の表(合算しない)

| 読み手 | E1 editor | E2 動画 | E4 計器の鎖 | E3 Q1 / Q2 / Q3 |
|---|---|---|---|---|
| Sonnet | 直せば通る(0.6・照合 11 件 全部一致・「基準を緩く読むなら通る」) | 手を入れればできる(0.65) | 言えている(0.65) | 答えられる / ほぼ / 答えられる |
| Fable | **通る**(high・照合 10 群 全部一致・不一致 0) | できる(medium) | 言えている(high) | 答えられる / 答えられる(一点だけ一部) / 答えられる |

- 一致: **E4 同じ**(言えている)。**E3 同じ**(三問・Q2 は二人とも「退けた 6 本のうち 5 本が上限」が台本にしか無い点を挙げる)。**E1 割れ**(Fable 通る / Sonnet 直せば通る)= Sonnet も「事実と数の面では通る・表示の違反を厳密に取ると直せば通る」と書き、割れは「字が線に乗らない」「色の意味が一つ」の厳密さの差。**E2 割れ**(Sonnet 手を入れれば / Fable できる)= v1・v1.1・v1.2 の三回とも同じ向き。
- 動き(同じ族の読み手で・v1 → v1.1 → v1.2): Fable E1 直せば通る(高)→ 直せば通る(事実 高・境 中)→ **通る**(high)/ E2 できる → できる → できる / E4 言えている(中・43 / 47 を除く)→ 高 → high。Sonnet E1 直せば通る(中〜高)→ 中 → 0.6(緩く読めば通る)/ E2 手を入れれば ×3 / E4 高 → 中 → 0.65 / E3 Q2 ほぼ → 答えられる → ほぼ(「5 / 6 が上限」が台本だけ)。

## §2 指摘(★ = 二人・✓ = 主 session が撮影か出所で確かめた)

- ★ 状態 13 の「退け」の二義: 選んだ b2_j08 の chip「計算 なし・退け REJ6 なし」と題「退けた命題が、そのまま次の候補として戻り続ける行」の「退け」が別の述語(行列式で共線を退けた・REJ6 は折り返しの退けだけ)。一行の注が要る(二人)。出所 = RECORD §4 / RESULT olm127 §3.4 の言い方(主 session の責任半分)。
- ★ 「退けた 6 本のうち 5 本が上限」が video に無い(CLAIMS K87 は state 12 と書くが台本 16 行目にだけ)(二人)。
- ★ 帯(状態 5)が台本に cue されず、「帯・境」の語が声に乗るのは 21 行目まで無い(二人・Fable は読み A で「できる」、読み B なら「手を入れれば」と開示)。
- ✓ Sonnet だけ(Fable は「線乗りは見当たらない」と書いた): **状態 1 の製図板の字が線に乗る**(「M = TcTh の中点 ≠ O3」が接線と円の線をまたぐ・「3.842」に青い線が触れる・「O1O2」が円の輪郭に乗る)。主 session が video_s1 で確認 = Sonnet が正・Fable は見落とし。kit の板は重なり検査の射程の外。
- ✓ Fable だけ: **状態 18 の候補 5 番「退けが commit を支配する仕組み(MEMO §4 の 3)」は RECORD §6 に無い**(RECORD §6 は (a)〜(e)・(e) は図解)。限定「候補は RECORD §6 の文の写し」と食い違う。主 session が video_s18 と RECORD §6 で確認 = Fable が正(v1 から在った・v1 / v1.1 の読み手は触れず)。
- Sonnet だけ: 状態 7 の暗い青(olm122 / olm127 の EQ)だけ淡く橙は淡くない・凡例に無い / 状態 6 の格子線が字を貫く / 台本 147.3 秒は「1〜2 分」を超え読み下しで延びる / 状態 5 に 0.108 の印が olm125 の帯に無い / 状態 17 の「記憶の線対称」の語 / 状態 1 の O が 0 に見える。
- Fable だけ: 台帳の括弧「olm122 は全行の退けが一本多い」が olm119 を落とす / 状態 7 の名指し olm113 1・olm119 12 に「遡って当てた」の注が無い(RECORD §1 は —)/ 状態 14 の MIDO3 行「凍結の判定は olm117 の札(記述)」で olm117 Q1 = 増える の名が出ない / 棚の olm117 の札が「等半径の」で切れる / 状態 5 の olm117 / 119 / 122 の境は照合用の値に無い。
- 動画の作者(二人): 状態 0 の kit の帯は 180 px で柱の差が小さく、瞬間を担うのは上の枠(実線 + ● / 点線 + ○)/ 状態 0 の panel は逐語が密で 10 秒で読めるのは枠の語だけ / 3D の棚は数を担わない。

---

## v1.3 — acceptance (RESULT_judging v1.2 §7)

## §7 v1.3 の受領(据える・再審査なし・2026-11-04 夕・先生「(b) に進んだ方が良いでしょうか?」→ 主 session「(b) 小直し 5 点・再審査なし」→ 先生「進めます」)

- [BRIEF v1.3](../BRIEF_v1_3_entry_Q_small_fixes_20261104.md)(e9eb84e1・H1〜H5 必須 + H6 / H7 任意・数と状態の数は変えない)→ 同じ作り手(Opus 5.5 xhigh・60 分)→ `entry_Q_v1.3/`(受領 f77eb405)。
- 受領(主 session): check_claims **129 / 129** 再走(足した anchor K118〜K129・壊した 12 本は 12 本とも検出 = 作り手)・検査 260 / 260・video の HTML の字 ≥ 14 px・BRIEF §2 の照合 23 / 23・**pack の数値 2,196 個は v1.2 と同一**(違いは brief_check の個数 21 → 23 だけ)・台本 21 行 149.2 秒(≤ 150)・listen 0・伏せ字 0。
- 撮影で確かめた物(video): H1 状態 13 = 題「数値で退けた命題が、そのまま次の候補として戻り続ける行はあるか?」+ 側 panel と限定の行に「ここの『退け』は本文の数値の退け(b2_j08 = 共線を行列式で・b1_j13 = 共線を媒介変数 t で)。REJ6 は折り返しの退けの計器なので、この二行は REJ6 なし」/ H2 状態 12 = 札「6 本・型 0 本 = 届かなかった — 退けた 6 本のうち 5 本が上限(12,288 token)で JSON に至らず・1 本は証明の欄に至り線対称なし」+ 側 panel の olm127 の行 / H4 状態 1 = 名札(Tc′・Th′・M・3.842・O1O2)が引き出し線で板の線から離れた(検査 = v1.2 の build で状態 1 が落ちる陽性統制つき)/ H5 状態 18 = 1〜4 を「RECORD §6 の (a)〜(d)」・5 を「MEMO §4 の 3(RECORD §6 には無い)」・限定に「(e) 図解 = この図」/ H6 状態 19 = 「olm119・olm122 は全行の退けが一本多い(b2_j08・b1_j19)」/ H7 状態 17 = 「記憶の前提(等半径の図で真になる文)の線対称 3 本(olm125・読み・L3)」+ 各行に出所の列。H3 = 台本 08 行に帯の語(切り替え表で確認は作り手・秒数 149.2 は SCRIPT の頭)。
- 作り手の一番自信の無い点(そのまま記す): 引き出し線そのものが板の線をまたぐことがあり検査の射程の外 / 状態 13 の chip「計算 なし」(= 折り返しの式を使っていない)と新しい一行の「数値で退けた」の差は言葉で説明していない。
- **据える = v1.3**(`entry_Q_v1.3/`)。再審査はしない(§6 (b) の後半は取らない)。v1 / v1.1 / v1.2 の folder は書き換えず残す。公開の束(§6 (c))は別の裁定。
