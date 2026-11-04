# CLAIMS — what the figure says, where each number comes from (札 Q v1.3, 2026-11-04 夕; v1 / v1.1 / v1.2 rows kept; 20 states as in v1.1; v1.2 rows in §J, v1.3 rows in §K)

Every sentence the figure prints about the data is a row here, with its source (file + key) and its level. `check_claims.py` looks at each place: an anchor id (K..) in `claims_anchors.json` must have a row here, and a row here must have an anchor (`anchors checked: N · missing or different: 0`).
Levels: **L1** = a copy of a value in a card's frozen output / a frozen verdict · **L2** = a number counted from the frozen output (recounted by `check_claims.py` from the raw inventory rows, independent of the build) · **L3** = a reading (whose; the teacher decides) · **×** = not said.
Voice: nothing says what the model "thought / understood / noticed / hesitated over"; a mark is a word mark of the instrument, not the model's inside. "記憶の前提" is used only as "a sentence that becomes true on the equal-radii figure", with the L3 tag (E0, G, H).
Files: `data/moy2_line_inventory.json` (= the main session's inventory, md5 3190663e…, copied unchanged), `data/read/olm1NN.json` (= `ConstructGap/exp/olm1NN/read.json`, copied unchanged; md5 in `generated/pack.json` `read_prov`), `repo:` = a path in the repository.

## A. The material (states 0–3)
| id | claim (as the figure prints it) | source (file · key) | level |
|---|---|---|---|
| K01 | "棚卸し moy2_line_inventory.json (md5 3190663e)" (foot of every page) | `data/moy2_line_inventory.json` md5 | L1 |
| K02 | the inventory's own `.out` ends with the same md5 and size | `data/moy2_line_inventory.out` | L1 |
| K03 | "照合 recount_vs_read_json 20 / 20" (state 19, ledger) | `inventory.recount_vs_read_json` | L2 |
| K83 | the instruction sentence "Use it to check: compute the reflection with the given coordinates before you rely on it." (state 2, verbatim) | `inventory.prompts["TOOL_U(指示の文・olm125/127)"]` | L1 |
| K84 | "問いの文の md5 718d1601 (二回とも逐語同じ)" (state 2) | `inventory.prompts.prompt_md5["olm125/127"]` | L1 |
| K85 | "陰性統制 = frontier の証明 20 本" (states 3, 15) | `read/olm118.json` `gates.n_prf5` | L1 |
| K60 | "較正 54 → 74 → 98 → 144" (states 3, 15) | `inventory.instrument_lineage.calibration` | L1 |

## B. The configuration (state 1; v1 state 0) — computed by this page from the coordinates written in olm125 b1_j17's text
| id | claim | source | level |
|---|---|---|---|
| K71 | "|O3Tc| = 3.8421 · |O3Th| = 3.8420 → EQ 真 (apex)" | recount from S1's `head` + `rej6_first` coordinates (`DERIVED geo apex`) | L2 |
| K72 | "Th を O1O2 で折り返す = (6.6217, 0.3769)" (S1 itself writes (6.6167, 0.3767): within 0.01) | same (`geo refl_Th`) | L2 |
| K73 | "Th′ ≠ Tc (距離 3.9557) → 線対称 偽" | same (`geo gap_refl`) | L2 |
| K74 | "M ≠ O3 (距離 1.8869) → MIDO3 偽" | same (`geo gap_mid`) | L2 |
| K75 | what the page carries for the reflection gap = the recount | `generated/pack.json` `geo.gap_refl` | L2 |

## C. The seven arms (states 4–9)
| id | claim | source | level |
|---|---|---|---|
| K04 | "道具なし 5 / 41 = 0.122" | recount from `arms.olm113.rows` (has_proof ∧ proof_v3.LN_a) | L2 |
| K05 | "等半径 7 / 46 = 0.152" | `arms.olm117.rows` | L2 |
| K06 | "宣言の文 14 / 44 = 0.318" | `arms.olm119.rows` | L2 |
| K07 | "式だけ(一回目)4 / 37 = 0.108 · G1 ✗ 判定なし" | `arms.olm122.rows` | L2 |
| K08 | "式だけ(二回目)4 / 37 = 0.108" | `arms.olm124.rows` | L2 |
| K09 | "指示の文 9 / 40 = 0.225" | `arms.olm125.rows` | L2 |
| K10 | "二回目 3 / 35 = 0.086 · G1 ✗ 判定なし" | `arms.olm127.rows` | L2 |
| K11 | "v6 olm119 0.341" | `arms.olm119.rows` (proof_v6.LN6_a) | L2 |
| K12 | "v6 olm124 0.162" | `arms.olm124.rows` | L2 |
| K13 | "v6 olm125 0.275" | `arms.olm125.rows` | L2 |
| K14 | "olm124 / olm125 は 45 / 60 の境ちょうど" | `arms.olm124.rows` (cls ≠ NONE) | L2 |
| K15 | "olm127 は 40 / 60 で落ち" | `arms.olm127.rows` | L2 |
| K16 | "olm122 は 46 / 60 で当時の境 0.80 に落ちた" | `arms.olm122.rows` | L2 |
| K17 | "olm127 G1 ✗" | `read/olm127.json` `gates["G1_conj_parsed>=0.75"]` = false | L1 |
| K18 | "olm122 G1 ✗(当時 0.80)" | `read/olm122.json` `gates["G1_conj_parsed>=0.80"]` = false | L1 |
| K19 | "olm125 G1 通る" | `read/olm125.json` `gates["G1_conj_parsed>=0.75"]` = true | L1 |
| K20 | "olm119 上がる" | `read/olm119.json` `Q1.verdict` | L1 |
| K21 | "olm124 戻る" | `read/olm124.json` `Q1.verdict` | L1 |
| K22 | "olm125 上がる" | `read/olm125.json` `Q1.verdict` | L1 |
| K23 | "olm125 Q2 変わらない" | `read/olm125.json` `Q2.verdict` | L1 |
| K24 | "olm127 判定なし" | `read/olm127.json` `Q1.verdict` = null | L1 |
| K25 | "olm127 Q2 変わらない" | `read/olm127.json` `Q2.verdict` | L1 |
| K86 | "olm127 計算した 10 / 60 = 0.167" | `read/olm127.json` `Q2.REFL_CALC_rate` | L1 |
| K29 | the band of olm124 recomputed from its PREREG rule = 戻る (= read.json) | PREREG olm124 Q1 rule · `DERIVED band` | L2 |
| K30 | the band of olm125 recomputed = 上がる | PREREG olm125 Q1 rule | L2 |
| K31 | the band of olm119 recomputed = 上がる | PREREG olm119 Q1 rule | L2 |
| K32 | the band of olm117 (card olm118) recomputed = 変わらない | PREREG olm118 Q1 rule | L2 |
| K33 | olm124's band edges "|Δ113| < 0.06 = 戻る (0.062〜0.182)" — printed as 0.062 / 0.182 / 0.258 / 0.378 on state 5 (above the band) and state 6 (beside the short ticks) (v1.2 G8) | `repo:…/PREREG_olm124…md` literal | L1 |
| K34 | olm125's band edges "Δ124 ≥ +0.06 (r ≥ 0.168) = 上がる" — printed as 0.048 / 0.168 on states 5, 6 (v1.2 G8) | `repo:…/PREREG_olm125…md` literal | L1 |
| K35 | olm127's bands "残る 0.165 ≤ r < 0.285 · 戻る 0.048 < r < 0.168" — printed as 0.048 / 0.165〜0.168 / 0.285 on states 5, 6, and state 5 names the overlap (v1.2 G8) | `repo:…/PREREG_olm127…md` literal | L1 |
| K79 | "olm125 と隣の比べ(Fisher・参考)は p 0.23 / 0.11 / 0.46" (states 6, 9; v1.2 G7: no flat "分けられない") | `repo:…/RESULT_olm125…md` §2 literal | L1 |
| K57 | "名指し olm125 18" | `arms.olm125.rows` (tool_named) | L2 |
| K58 | "名指し olm127 7" | `arms.olm127.rows` | L2 |
| K51 | "MIDO3 olm113 0.34" | `arms.olm113.rows` (cls / parsed) | L2 |
| K52 | "MIDO3 olm117 0.74" | `arms.olm117.rows` | L2 |
| K53 | "EQ olm125 0.311" | `arms.olm125.rows` | L2 |
| K54 | "外接線の印 v3 olm113 10 / 41" | `arms.olm113.rows` (proof_v3.OUTER_a) | L2 |
| K55 | "外接線の印 v3 olm117 13 / 46" | `arms.olm117.rows` | L2 |
| K56 | "外接線の印 v6 olm122 8" | `arms.olm122.rows` (proof_v6.OUTER6_a) | L2 |
| K59 | "上限に至った行 5 / 2 / 6 / 5 / 9 / 6 / 7" (state 8; olm113 = 5) | `arms.olm113.rows` (hit_cap) | L2 |
| K77 | what the page carries for olm127's parsed rows = the recount | `generated/pack.json` `arms.6.agg.parsed` | L2 |

## D. The calc rows (states 10–13)
| id | claim | source | level |
|---|---|---|---|
| K36 | "計算した行 olm125 18" | `arms.olm125.rows` (calc) | L2 |
| K37 | "olm124 15" | `arms.olm124.rows` | L2 |
| K38 | "olm127 10" | `arms.olm127.rows` | L2 |
| K39 | "退け REJ6 olm125 15 (= 15 / 18)" | `arms.olm125.rows` (rej6) | L2 |
| K40 | "olm119 退け 11(全行)" | `arms.olm119.rows` | L2 |
| K41 | "olm119 退け / 計算した行 = 10 / 13" | `arms.olm119.rows` (rej6 ∧ calc) | L2 |
| K42 | "olm122 退け / 計算した行 = 5 / 12" | `arms.olm122.rows` | L2 |
| K76 | what the page carries for olm125's rejects among calc rows = the recount | `generated/pack.json` `arms.5.agg.REJ_calc` | L2 |
| K43 | "b2_j07 の型 olm125 = b1_j11 · b1_j17 · b2_j19" | `arms.olm125.rows` (rej6 ∧ proof LN6) | L2 |
| K44 | "olm119 = b0_j13 · b1_j06 · b2_j08" | `arms.olm119.rows` | L2 |
| K45 | "olm127 = 0 本" | `arms.olm127.rows` | L2 |
| K87 | "退けた 6 本のうち 5 本が上限(12,288 token)で JSON に至らず" — **v1.3 H2: on state 12 in the figure** (the chip "olm127 の退け" and, short, beside "olm127 0" in the side panel), also script line 16 | `arms.olm127.rows` (rej6 ∧ hit_cap) | L2 |
| K46 | "olm125: 計算した行の証明の欄 2 / 9 · しない行 7 / 31" | `arms.olm125.rows` | L2 |
| K47 | "olm124: 1 / 7 · 3 / 30" | `arms.olm124.rows` | L2 |
| K48 | "olm125 計算した行の類 EQ 9" | `arms.olm125.rows` (calc ∧ cls) | L2 |
| K49 | "MIDO3 0" | same | L2 |
| K50 | "NONE 5" | same | L2 |
| K78 | "四腕の退け / 計算した行 42 / 56(行から数えた値・L2)" (state 10 card, state 17 table, state 19 ledger; v1.1 F1 — was "43 / 47 — RECORD §4 の数" (L1) in v1) | recount from `arms.olm119/124/125/127.rows` (rej6 ∧ calc / calc) = `agg.REJ6_in_calc` / `REFL_CALC` = RECORD 訂正 3 | L2 |
| K88 | what the page carries for the four arms (42) = the recount | `generated/pack.json` `four.num` | L2 |
| K92 | "RESULT の 43 / 47 は棚卸しの述語で再現できず、据えない(RECORD 訂正 3)" (state 10 card, ledger; the only place the old number is printed, in a negated sentence) | `repo:…/RECORD…md` 訂正 3 literal | L1 |
| K66 | "S8 b2_j08 × 343" | `inventory.scenes["S8_…(olm127 b2_j08)"].loop_count` | L1 |
| K67 | "S10 b1_j13 × 542" | `inventory.scenes["S10_…(olm127 b1_j13)"].loop_count` | L1 |
| K68 | "S1 b1_j17 · T 4,315" | `arms.olm125.rows[b1_j17].T` | L1 |
| K69 | "S2 b0_j16 · T 7,335" | `arms.olm125.rows[b0_j16].T` | L1 |
| K70 | "S9 b2_j09 の証明の欄 = 数値だけ「both are sqrt(14.764) ≈ 3.838」" | `arms.olm127.rows[b2_j09].proof` | L1 |

## E. The seen / unseen shape (state 14) and the instrument lineage (states 15–16)
| id | claim | source | level |
|---|---|---|---|
| K26 | "olm118 Q1 線対称 変わらない" | `read/olm118.json` `Q1.verdict` | L1 |
| K27 | "olm118 Q2 点対称 増える" | `read/olm118.json` `Q2.verdict` | L1 |
| K28 | "olm118 Q3 外接線 +0.0387" | `read/olm118.json` `Q3.diff` | L1 |
| K61 | "olm118 Q3: v3 変わらない → v4 間 (+0.0631) → v5 間 (+0.0631) → v6 変わらない" | `repo:…/RESULT_olm126…md` Q1 literal | L1 |
| K62 | "凍結の判定 7 / 7 同じ" | `read/olm126.json` `Q2.frozen` vs `Q2.v6` | L2 |
| K63 | "最も動いた率 olm124 +0.054" | `arms.olm124.rows` (v6 − v3) | L2 |
| K64 | "olm113 +0.000" | `arms.olm113.rows` | L2 |
| K65 | "olm126 Q3 通らない" | `read/olm126.json` `Q3.verdict` | L1 |

## F. Chapter G (states 17–18): sentences of the MEMO and the RECORD (the numbers come from the rows above)
| id | claim | source | level |
|---|---|---|---|
| K80 | the teacher's question verbatim 「olmXシリーズから評価関数を導出できますか？」 | `repo:…/BRIEF_v1…md` literal | L1 (the question) |
| K81 | "出るのは受領関数 …" (the main session's answer; L3; the teacher decides) | `repo:…/MEMO…md` §4 literal | L3 |
| K82 | the candidate "対照の一行(reflection の語だけ置き宣言も指示もしない)" (state 18: "RECORD §6 の (b)"; v1.3 H5: candidates 1–4 = RECORD §6 (a)–(d), 5 = MEMO §4 item 3 — see K126–K128) | `repo:…/RECORD…md` §6 literal | L3 |

## G. What is not said (the ledger, state 19 — plain statements)
- ×: an order of the three sentences (declaration > instruction > formula only); that olm125's 0.225 is noise or the instruction's effect; putting a rise on the instruction's meaning alone; that the b2_j07-type rows are the same proposition rejected and revived; that olm127's zero means "fixed"; "the model hesitated" for the S8 / S10 repeats; a mechanism for "no reading ahead"; mixing "landed on the apex" with "checked it"; correctness rates; learnability of an evaluation function from this data; the inside of frontier models.
- L3 (main session; the teacher decides): RESULT olm125 §4 (the Tool section's text read as a cue) · RESULT olm127 §4 (the reject does not reach the commit) · RECORD §4 · MEMO §3 / §4.

## H. Corrections between the BRIEF and the data (the data was used; to be relayed to the main session)
1. **Band edges in §6 / C**: the BRIEF writes "帯の境(olm124 の 0.048 / 0.168・olm125 の 0.168 / 0.285)". In the PREREGs, 0.048 / 0.168 are **olm125's** edges (|Δ124| < 0.06 around 0.108) and 0.165(0.168) / 0.285 are **olm127's**; **olm124's** band is |Δ113| < 0.06 around 0.122 = 0.062 / 0.182 (間 0.182〜0.258, 残る 0.258〜0.378). The figure draws each arm's own edges from its PREREG (K33–K35).
2. **Reject rates in D**: the BRIEF writes "olm119 11 / 13・olm122 6 / 12". One reject of each arm lies outside the calc rows (olm119 b2_j08, olm122 b1_j19): the rejects among calc rows are 10 / 13 and 5 / 12 (K41, K42). The figure prints "10 / 13 (全行 11)" and "5 / 12 (全行 6)".
3. **T medians in D**: the BRIEF rounds "olm125 8,749 対 255"; the data are 8,748.5 / 254.5 (shown as such).
4. **RECORD §1 the cap of olm113 = 4**: the rows have 5 `hit_cap` (K59). The figure uses 5.
5. **RECORD §1 seeds of olm113 / olm117 / olm119** (20261150〜52 / 20261159〜61 / 20261165〜67): the rows carry 20261130〜32 / 20261160〜62 / 20261170〜72. The figure prints the rows' seeds.
6. **"四腕 43 / 47"** (BRIEF A / D, RECORD §4) has a denominator (rows that output the reflection of Tc / Th) that is not a field of the inventory. v1 quoted it as the RECORD's number; **v1.1 (F1)** prints the inventory's predicate instead (REJ6 ∧ REFL_CALC / REFL_CALC = olm119 10 / 13 · olm124 11 / 15 · olm125 15 / 18 · olm127 6 / 10 = 42 / 56, K78 · K88) and names 43 / 47 only as not kept (RECORD 訂正 3, K92). The name scan treats 43 / 47 · 15 / 15 · 11 / 14 · 11 / 12 as old names outside a negated sentence.
7. **Provenance**: `read/olm118.json` and `read/olm124.json` carry `provenance.dirty = true` (as frozen). The figure copies their values and does not re-judge the provenance (noted in NOTES).

## I. v1.1 rows (BRIEF v1.1 F3 / F4 / F5 / F7 and §2 items 12–18)
| id | claim | source | level |
|---|---|---|---|
| K89 | "18 本の最終の conjecture の類は 等距離 9・OTHER 4・JSON なし 5・共線 0(退けた 15 本の行き先ではない)" (state 11 lead / side / card, script line 13; F3) | `arms.olm125.rows` (calc ∧ cls) | L2 |
| K107 | "計算した 18 本のうち証明の欄に至った行 9" (item 13) | `arms.olm125.rows` (calc ∧ has_proof) | L2 |
| K93 | "退けた 15 本のうち証明の欄に至った行 8"(b0_j01 · b0_j08 · b0_j09 · b0_j16 · b1_j11 · b1_j17 · b2_j06 · b2_j19) (state 11 side / card; item 13) | `arms.olm125.rows` (rej6 ∧ has_proof) = RESULT olm127 訂正の追記 | L2 |
| K90 | "二行のうち、証明の欄に O1O2 についての対称を書いたのは b1_j17 だけ(主語は接線)" (script line 02; F3 + v1.2 G10 "二行のうち"; state 0 frames the same words) — the verbatim subject "the inner common tangent is symmetric with respect to O1O2" | `arms.olm125.rows[b1_j17].proof` | L1 |
| K91 | the seven Fisher p (two-sided, reference) 0.2284 · 0.1062 · 0.4631 · 1.0 · 0.124 · 0.0142 · 0.472 (state 9 chart, ledger; F4) | recount from `arms.*.rows` (LN v3 / proof rows; pools 122 + 124 = 8 / 74 and 125 + 127 = 12 / 75) | L2 |
| K96 | what the page carries for the seven p = the recount | `generated/pack.json` `fisher_p` | L2 |
| K94 | "olm127 対 olm124 p 1.0・対 olm125 p 0.12・対 olm119 p 0.014" (state 9, set against the recount) | `repo:…/RESULT_olm127…md` §2 literal | L1 |
| K95 | "指示 pool 対 式だけ pool p 0.47" (state 9) | `repo:…/RESULT_olm127…md` §2 literal | L1 |
| K97 | "◇ b0_j00・b2_j09 = 等距離に数値で着いた二行" (state 13 marks, side, card; F5) | `repo:…/RESULT_olm127…md` §4 literal (no inventory predicate) | L1 |
| K98 | b0_j00 "Yes! So TcO3 = ThO3" (state 13 side) | `repo:…/RESULT_olm127…md` §3.4 literal | L1 |
| K99 | "b0_j00 = status に至らない" | `arms.olm127.rows[b0_j00].status` = none | L1 |
| K100 | "b0_j00 = 証明の欄に至らない" | `arms.olm127.rows[b0_j00].has_proof` = false | L1 |
| K101 | the Q3 row of RESULT olm126 §2 copied in state 3: "… olm124 の 12 本のうち b2_j03 が落ちた ✗ …" (F7) | `repo:…/RESULT_olm126…md` §2 table literal | L1 |
| K102 | "… | 通らない(1 項目)" (the end of the same row) | same | L1 |
| K103 | "T の中央値 olm122 7,331.5 / 383.5" (state 10 readout family; item 14) | `arms.olm122.rows` (T of calc / non-calc rows) | L2 |
| K104 | "式だけ 162 字 · 式 + 宣言 267 字(宣言の文 106)· 指示の文 90 字" (state 2 readout; item 15) | `inventory.prompts` (string lengths) | L2 |
| K105 | "olm118 Q1 Δ +0.0302 変わらない" (state 14; item 16) | `read/olm118.json` `Q1.diff` | L1 |
| K106 | "olm118 Q2 Δ +0.087 増える" (state 14; item 16) | `read/olm118.json` `Q2.diff` | L1 |

## J. v1.2 rows (BRIEF v1.2 G1 / G2 / G7 / G8 / G9 / G11 and §2 items 19–21)
| id | claim (as the figure / the script says it) | source (file · key) | level |
|---|---|---|---|
| K115 | "S1 は Th を … 折り返した" (state 0 kicker, lead, the reject stage of the grid and the band; G1) | `arms.olm125.rows[b1_j17].rej6_start` begins "2F - Th" | L1 |
| K116 | "S2 は Tc を折り返した" (same places; G1) | `arms.olm125.rows[b0_j16].rej6_start` begins "2F - Tc" | L1 |
| K117 | "MIDO3 olm113 17 / 50 = 0.340 · olm117 37 / 50 = 0.740", both bars orange; legend "一般の図では偽・等半径の図(olm117)では真" (state 14; G2; item 21) | `arms.olm113 / olm117.rows` (cls, parsed) | L2 |
| K108 | "7 対のうち 6 対は参考の目盛り(0.05)の上・1 対(olm127 3 / 35 対 olm119 14 / 44)は下。参考であって判定ではなく、多重比較は補正していない" (state 9 chart and card, ledger, script line 11; G7; item 20) | recount from `arms.*.rows` (the seven pairs) | L2 |
| K109 | the pair below 0.05 the page names = the recount | `generated/pack.json` `fisher_below` | L2 |
| K110 | "0.165〜0.168" (olm127's overlap; states 5, 6) and "重なり 0.165〜0.168 は 戻る が先" (state 5; G8; item 19) | `repo:…/PREREG_olm127…md` literal | L1 |
| K111 | olm124's edges 0.062 / 0.182 / 0.258 / 0.378 printed on states 5, 6 (G8; item 19) | recount of the PREREG olm124 rule (0.122 / 0.318 ± 0.06) | L2 |
| K112 | olm125's edges 0.048 / 0.168 printed on states 5, 6 (G8; item 19) | recount of the PREREG olm125 rule (0.108 ± 0.06) | L2 |
| K113 | "b2_j07 の型 六腕 0 / 3 / 2 / 1 / 3 / 0 = olm113 / 119 / 122 / 124 / 125 / 127" (state 17's table, the same order as state 12; G9) | `arms.*.rows` (rej6 ∧ has_proof ∧ LN6_a) | L2 |
| K114 | script line 21: "式だけは戻る(一回目は参考)、宣言の文は上がる、指示の文は一回目 上がる・二回目は関門に落ちて判定なし = 二回で立たない、まで" (G11) | `read/olm124.json` / `olm119` / `olm125` `Q1.verdict`; `read/olm127.json` `gates.G1_conj_parsed>=0.75` = false | L1 |

## K. v1.3 rows (BRIEF v1.3 H1 / H2 / H5 / H6 and §2 items 22–23)
| id | claim (as the figure / the script says it) | source (file · key) | level |
|---|---|---|---|
| K118 | state 13: "ここの「退け」は本文の数値の退け(b2_j08 = 共線を行列式で …)… この二行は REJ6 なし" — b2_j08 has no REJ6 (H1) | `arms.olm127.rows` b2_j08 `rej6` = false | L1 |
| K119 | the same sentence: b1_j13 (共線を媒介変数 t で) has no REJ6 (H1) | `arms.olm127.rows` b1_j13 `rej6` = false | L1 |
| K120 | the two rows reject collinearity with numbers (determinant ≠ 0 / the parameter t) — the source of H1's sentence | `repo:…/RESULT_olm127…md` §4 item 5 literal "共線を行列式 ≠ 0 / 媒介変数の不一致で数値で退けた直後に" | L1 |
| K121 | the H1 sentence is on state 13 (side panel and the limit line), the row names read from the scenes | `i18n.js` literal (REJ_NOTE) | L1 (the page's text) |
| K122 | state 13's title "数値で退けた命題が、そのまま次の候補として戻り続ける行はあるか?" (H1: the title and the chip "退け REJ6 なし" no longer use 退け for two predicates) | `i18n.js` literal | L1 (the page's text) |
| K123 | state 12: "退けた 6 本のうち 5 本が上限(12,288 token)で JSON に至らず・1 本は証明の欄に至り線対称なし" (H2; BRIEF v1.3 §2 item 22) | `arms.olm127.rows`: rej6 = 6 · rej6 ∧ hit_cap = 5 · rej6 ∧ has_proof = 1 (b2_j11) · of which LN6_a = 0 | L2 |
| K124 | the source of K123 | `repo:…/RESULT_olm127…md` §3.3 literal "退けた 6 本のうち証明の欄に至ったのは b2_j11 の 1 本だけ(残り 5 本は上限)" | L1 |
| K125 | the K123 sentence is on state 12 (chip and side panel), its numbers counted from the rows at run time | `i18n.js` literal (CAP127) | L1 (the page's text) |
| K126 | state 18: candidates 1–4 = RECORD §6 (a)–(d); RECORD §6 (e) = the explainer = this figure; candidate 5 is not in RECORD §6 (H5; item 23) | `repo:…/RECORD…md` §6 (the "- (a)" … "- (e)" items) and `repo:…/MEMO…md` §4 item 3, recounted | L1 |
| K127 | candidate 5 "退けが commit を支配する仕組み" = MEMO §4 item 3 | `repo:…/MEMO…md` §4 literal | L3 (the main session's reading) |
| K128 | state 18 prints "MEMO §4 の 3(RECORD §6 には無い): 退けが commit を支配する仕組み" and the limit "候補は RECORD §6 の (a)〜(d) と MEMO §4 の文の写し・(e) 図解 = この図" | `i18n.js` literal | L1 (the page's text) |
| K129 | the ledger (state 19): "olm119・olm122 は全行の退けが一本多い(b2_j08・b1_j19)" (H6) | `arms.olm119.rows` / `arms.olm122.rows` (rej6 ∧ ¬calc) | L2 |
