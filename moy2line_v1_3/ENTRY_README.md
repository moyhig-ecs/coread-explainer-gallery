# 札 Q v1.3 — co-reading the moy-2 reflection-tool line (olm113 → olm127)

> **v1.3 (2026-11-04 夕)** = the small fixes H1–H7 of BRIEF v1.3 (`cards/BRIEF_v1_3_entry_Q_small_fixes_20261104.md`) on v1.2; **no number changed**; still **20 states**; no re-judging. H1 state 13's two senses of 退け · H2 state 12 shows "5 of the 6 rejecting rows hit the cap" · H3 the band words in the script (state 6) · H4 the drafting board's tags clear of the board's lines (a new check) · H5 state 18's candidates name their sources (RECORD §6 (a)–(d) / MEMO §4 item 3) · H6 the ledger names b2_j08 · b1_j19 · H7 state 17 "記憶の前提(等半径の図で真になる文)". What changed, before / after and the added checks: `NOTES.md` § v1.3.
> v1.2 (2026-11-04 夕) = the display and script fixes G1–G12 of BRIEF v1.2 (`cards/BRIEF_v1_2_entry_Q_display_script_fixes_20261104.md`) on v1.1; **no number changed**; still **20 states** (the ledger fits one 1920 × 1080 frame at ≥ 14 px, so it was not split). What changed, before / after and the added checks: `NOTES.md` § v1.2.
> v1.1 (2026-11-04) = F1–F8 of BRIEF v1.1 on v1 (19 → 20 states): `NOTES.md` § v1.1.

An audited co-reading explainer (coread-explainer skill) of the moy-2 "reflection tool" line: how the line symmetry "Tc and Th are symmetric about O1O2" (a false premise on the general figure) in OLMo-3-1125-32B base's proof field moves when the prompt's `# Tool` section is the formula only / formula + declaration / formula + instruction — read from the frozen outputs only (the main session's inventory + each card's `read.json` + PREREG / RESULT / RECORD / MEMO sentences).
Pages (dark / light × ja / en) and a native anywidget (Jupyter / marimo), 1920 × 1080 stills, a two-voice script and a ledger of what can / cannot be said.
Built on the `anatomy` skill's kit (MIT, Copyright (c) 2026 Ryan; read from `~/.claude/skills/anatomy` at build time; see `LICENSE-Anatomy.txt`): its camera, solids, four-tone shading, CSS and page shell. The MIT notice is in every page.

## Run
```sh
PY=~/miniforge3/envs/py314/bin/python bun build.mjs   # pack_moy2.py (assert) → data.mjs (JS recount) → art.mjs (kit) → dist/*.html, dist/widget.js / .css, dist/build_report.json
python3 -I list_headings.py         # the 20 headings, the chapters, the step groups
python3 -I check_claims.py          # 129 claim rows ↔ anchors (raw data, independent of the build); make_anchors_broken.py + --anchors checks/anchors_broken.json is its positive control (12 broken → 12 caught)
sh run_checks.sh checks             # console · robust · chapter buttons (real clicks) · drag picks (real mouse) · smallest px (video html ≥ 14) · overflow · gate lines (G3) · rack name tags (G4) · status line (G5) · band edges (G8) · board tags clear of the board's lines (H4) · name scan (+ positive control) · public fence
sh run_checks.sh captures           # the stills
sh run_marimo_check.sh              # marimo on 127.0.0.1:27531 (two ways)
sh run_jupyter_check.sh             # JupyterLab on 127.0.0.1:27541 (two ways)
sh run_all.sh                       # all of the above after one build, logs in checks/ (capture.log, summary.json)
python3 -I make_script.py           # SCRIPT_yukkuri.md from the pack
```
Open `dist/moy2line.html#s0` (the hash is the state; `#s8` = the rack, `#s9` = the Fisher card). `?video=1` = the 1920 × 1080 frame · `?row=olm125:b0_j16` · `?arm=olm119`. Keys: ← → states · `,` `.` previous / next row (rack) or arm (scale) · `l` language.

## States (from config.json; the numbers live only there) — v1.3 (the same 20 as v1.1; the last column = what v1.2 / v1.3 changed there)
| n | chapter | what it shows | v1 | v1.2 · v1.3 |
|---|---|---|---|---|
| 0 | A scene | **the first 10 seconds**: S1 olm125 b1_j17 / S2 b0_j16: same prompt, both reject the reflection; S1's proof field writes the line symmetry (its subject is the tangent: "the inner common tangent is symmetric with respect to O1O2"), S2's does not (verbatim) — **v1.2**: one grid row per stage (header · conjecture · reject sentence · proof field · the reader's frame), so the two rows line up at the reject sentence; the words v3 caught are framed + underlined in S1's proof field, S2 has an empty dotted frame of the same width; under them the kit's band (body / reject / proof field × S1 / S2; S1 a solid pin, S2 a dotted empty pin); kicker "同じ種類の計算(… S1 は Th を、S2 は Tc を折り返した)" | 1 (F2) | G1 · G5 |
| 1 | A scene | the moy-2 figure to its coordinates on a drafting board (kit art): EQ = apex true (3.842 / 3.842), MIDO3 false (M ≠ O3), line symmetry false (Th′ ≠ Tc) + the four steps of reading | 0 (F2) | G6 · H4 (every tag clear of the board's lines; leaders) |
| 2 | B tool | the three Tool sections verbatim (lengths 162 / 267 (declaration 106) / 252 (instruction 90), prompt md5) | 2 | G6 |
| 3 | B tool | the instruments (word marks), calibration 54 / 144, negative control 0 / 20 + **the Q3 row of RESULT olm126 §2 copied (L1)**; the outer marker "一般の図では偽" | 3 (F7) | G2 · G6 (the Q3 row ≥ 14 px in the video) |
| 4 | B tool | gate G1 (parsed ≥ 0.75; old 0.80): olm124 / olm125 exactly on the line, olm122 / olm127 fail; the value and its message start right of both dashed lines | 4 | G3 · G2 (hatched bars) |
| 5 | B tool | each card's frozen verdict band (PREREG rule) with its value; G1-failed arms = reference position only; **every edge printed above its band** (olm127: 0.165〜0.168, the overlap goes to 戻る) | 5 | G8 · G5 |
| 6 | C arms | the seven arms on ONE scale 0–0.4 (v3 filled = verdict, v6 ring = reference, each arm's band edges); **drag picks an arm** → its Tool section verbatim; each edge printed beside its short tick | 6 | G8 · G7 (no flat "分けられない") · H3 (script: the band words) |
| 7 | C arms | the other columns: REFL_CALC, naming, MIDO3 / EQ, outer marker | 7 | G2 (hatched bars) · G5 |
| 8 | C arms | the rack (kit art): 7 trays × 60 blocks (height = log10 T, cap = lid, colour = class, top marks = proof-field instruments, collar = reject); **drag picks a row** → class, T, full proof field, reject sentence; the height-axis labels sit left of the post, clear of the blocks; the picked row's name in a free place with a leader | 8 (F6) | G4 |
| 9 | C arms | **new**: two-sided Fisher exact p between neighbouring arms (7 pairs, from the row counts, set against RESULT olm125 §2 / olm127 §2) — reference, not frozen, no correction for multiple comparisons, 0.05 = a reference tick; **one line: 7 対のうち 6 対は 0.05 の上・1 対(olm127 3 / 35 対 olm119 14 / 44)は下** (reference, no correction) | — (F4) | G7 · G2 · G5 |
| 10 | D calc | calc vs non-calc rows: proof-field line symmetry, rejects among calc rows, median T; card "四腕 42 / 56 (L2) — RESULT の 43 / 47 は再現できず、据えない" | 9 (F1) | G12 (a script line) |
| 11 | D calc | the rack, calc rows lit: olm125 18 calc rows, 15 reject; final conjecture classes equidistant 9 · OTHER 4 · no JSON 5 · collinear 0; 8 of the 15 rejecting rows reach a proof field | 10 (F3, F6) | G4 |
| 12 | D calc | the rack, rejecting rows lit; the b2_j07 type (0 / 3 / 2 / 1 / 3 / 0) | 11 (F6) | G4 · H2 ("退けた 6 本のうち 5 本が上限で JSON に至らず・1 本は証明の欄に至り線対称なし" on the chip and side panel) |
| 13 | D calc | the rack, olm127 lit: S8 × 343, S10 × 542, S9 numbers-only proof; **◇ b0_j00 · ◇ b2_j09** = reached the equidistance with numbers (RESULT olm127 §3.4 / §4) | 12 (F5, F6) | G4 (names out of the corner, leaders) · H1 (title "数値で退けた命題が…"; "ここの「退け」は本文の数値の退け … この二行は REJ6 なし") |
| 14 | E shape | equal radii (olm117) vs general (olm113) with the olm118 verdicts; **MIDO3 orange for both arms**, the other rates hatched (grey = NONE only); legend "一般の図では偽・等半径の図(olm117)では真"; title "…(読み・L3)" | 13 | G2 |
| 15 | F lineage | v3 → v6 calibration and the olm118 Q3 band round trip (変わらない → 間 → 間 → 変わらない) + the four verbatim fixes | 14 | G12 (a script line) · G6 |
| 16 | F lineage | v3 vs v6 rates (+0.000 … +0.054) and the 7 frozen verdicts (7 / 7 the same) | 15 | — |
| 17 | G next | the teacher's question verbatim + MEMO §3 / §4 (L3, the teacher decides); the checking row now reads 10 / 13 · 11 / 15 · 15 / 18 · 6 / 10 = 42 / 56; **the b2_j07 row = 六腕 0 / 3 / 2 / 1 / 3 / 0 (olm113 / 119 / 122 / 124 / 125 / 127)** and a source on every row | 16 (F1) | G9 · H7 ("記憶の前提(等半径の図で真になる文)の線対称 3 本(読み・L3)") |
| 18 | G next | the candidates of RECORD §6 (no recommendation mark), back to A0 (state 0) | 17 (F2) | H5 (1–4 = RECORD §6 (a)–(d) · 5 = MEMO §4 item 3, not in RECORD §6 · (e) = this figure) |
| 19 | H ledger | can say (L1) / descriptive / reading (L3) / cannot say, each with its source (42 / 56 and the Fisher row in "descriptive"); one frame, body 16 px / sources 14 px in the video | 18 (F1, F4) | G6 · G7 · H6 ("(b2_j08・b1_j19)") |

## Stills by state (file names; written by `make_script.py`; v1.1 F8)
Folder `captures/`. Every state has a video still (1920 × 1080, `?video=1`), a desk still (1440 wide, dark, ja) and a phone still (390 wide, dark, ja); some also have light / English stills. marimo: `M1_marimo_open_state0.png` · `M2_marimo_drag_reached_kernel.png` · `M3_marimo_python_wrote_state8_row_en.png`; JupyterLab: `J1_jupyterlab_open_state0.png` · `J2_jupyterlab_python_wrote_state8_figure_pressed_11.png`. `captures/capture.log` = name · pixels · bytes · md5 of every still.
<!-- stills:begin (written by make_script.py) -->
| state | heading | video | desk dark | phone dark | also |
|---|---|---|---|---|---|
| 0 | A0 場面 — 同じ種類の計算(折り返しを数値で出して退けた・S1 は Th を、S2 は Tc を折り返した)・違う証明の欄 | `video_s0.png` | `page_dark_s0.png` | `phone_dark_s0.png` | `page_light_s0.png` · `page_dark_s0_en.png` · `video_en_s0.png` |
| 1 | A1 場面 — 問いの図と読み方 | `video_s1.png` | `page_dark_s1.png` | `phone_dark_s1.png` | `page_light_s1.png` · `page_dark_s1_en.png` · `video_en_s1.png` |
| 2 | B0 道具の段 — 三種の文(逐語) | `video_s2.png` | `page_dark_s2.png` | `phone_dark_s2.png` | — |
| 3 | B1 計器 — 語の印と較正 | `video_s3.png` | `page_dark_s3.png` | `phone_dark_s3.png` | — |
| 4 | B2 関門 G1 — 取れた行 ≥ 0.75 | `video_s4.png` | `page_dark_s4.png` | `phone_dark_s4.png` | — |
| 5 | B3 判定の帯 — 札ごとの規則 | `video_s5.png` | `page_dark_s5.png` | `phone_dark_s5.png` | — |
| 6 | C0 七腕の表 — 一つの目盛り | `video_s6.png` | `page_dark_s6.png` | `phone_dark_s6.png` | `page_light_s6.png` · `page_dark_s6_en.png` · `video_en_s6.png` |
| 7 | C1 七腕の表 — ほかの列 | `video_s7.png` | `page_dark_s7.png` | `phone_dark_s7.png` | — |
| 8 | C2 七腕の表 — 積み木の棚(行を選ぶ) | `video_s8.png` | `page_dark_s8.png` | `phone_dark_s8.png` | `page_light_s8.png` · `page_dark_s8_en.png` · `video_en_s8.png` · `video_s8a.png` · `video_s8b.png` (the drag) |
| 9 | C3 七腕の表 — 隣り合う腕の Fisher(参考) | `video_s9.png` | `page_dark_s9.png` | `phone_dark_s9.png` | `page_light_s9.png` · `page_dark_s9_en.png` · `video_en_s9.png` |
| 10 | D0 計算した行 — 分けて数える | `video_s10.png` | `page_dark_s10.png` | `phone_dark_s10.png` | — |
| 11 | D1 計算した行 — 退けた後の類 | `video_s11.png` | `page_dark_s11.png` | `phone_dark_s11.png` | — |
| 12 | D2 計算した行 — b2_j07 の型 | `video_s12.png` | `page_dark_s12.png` | `phone_dark_s12.png` | `page_light_s12.png` |
| 13 | D3 計算した行 — 戻り続ける行(olm127) | `video_s13.png` | `page_dark_s13.png` | `phone_dark_s13.png` | `video_en_s13.png` |
| 14 | E0 見た形 / 見ていない形 — 等半径の対照 | `video_s14.png` | `page_dark_s14.png` | `phone_dark_s14.png` | — |
| 15 | F0 計器の系譜 — v3 → v6 | `video_s15.png` | `page_dark_s15.png` | `phone_dark_s15.png` | `page_light_s15.png` · `page_dark_s15_en.png` |
| 16 | F1 計器の系譜 — 判定は計器の形に依らない | `video_s16.png` | `page_dark_s16.png` | `phone_dark_s16.png` | — |
| 17 | G0 次の問い — 先生の問い | `video_s17.png` | `page_dark_s17.png` | `phone_dark_s17.png` | — |
| 18 | G1 次の問い — 候補(採否は先生) | `video_s18.png` | `page_dark_s18.png` | `phone_dark_s18.png` | — |
| 19 | H 台帳 — 言える / 記述 / 読み / 言えない | `video_s19.png` | `page_dark_s19.png` | `phone_dark_s19.png` | `page_light_s19.png` · `page_dark_s19_en.png` · `video_en_s19.png` |
<!-- stills:end -->

## Files
| file | role | hand / generated |
|---|---|---|
| `config.json` | chapters (= the state numbers), pages, min px (svg / html), frames, the port band | hand |
| `data/moy2_line_inventory.json` · `.out` · `data/read/olm1NN.json` | the frozen material, copied unchanged (md5 in `generated/pack.json`) | copied |
| `quoted.json` | the PREREG / RESULT / RECORD / MEMO literals the figure quotes (each checked to occur in its file) | hand |
| `pack_moy2.py` · `data.mjs` | the first (Python, asserts vs inventory agg, read.json and the BRIEF) and second (JS, from the raw rows) routes | hand |
| `art.mjs` | the kit's static art: the board, the rack (with each block's screen rectangle for the name tags) and the state-0 band | hand |
| `figure.js` · `i18n.js` · `figure.css` · `state_machine.js` | the states and drawing · the words · the style · the engine | hand |
| `build.mjs` | pages + widget | hand |
| `moy2line_widget.py` · `widget_glue.js` · `demo_marimo.py` · `demo_jupyter.ipynb` | the anywidget (traits state / lang / theme / row / arm / done / reading + `kernel_recount()` = the third route), its glue, two demos | hand |
| `check_claims.py` · `claims_anchors.json` · `CLAIMS.md` · `make_anchors_broken.py` | the fourth route, the claim rows, and its positive control (9 anchors broken on purpose) | hand |
| `make_check.py` · `run_checks.sh` · `list_headings.py` · `make_marimo_check.py` · `run_marimo_check.sh` · `make_jupyter_check.py` · `run_jupyter_check.sh` · `run_all.sh` · `make_capture_log.py` · `summarize_checks.py` · `drive.mjs` | the checks; `drive.mjs` is a small DevTools driver (port inside 27500–27599, profile in `.chrome/`) | hand |
| `make_script.py` · `SCRIPT_yukkuri.md` | the two-voice script (≤ 150 s), its switching table and the stills-by-state table (also written into this README) | generated |
| `dist/` · `generated/` · `checks/` · `captures/` | outputs | generated |

## Limits of the drawing
- The art is static (built once with the kit's camera at azimuth 62° / elevation 36° for the rack, 52° / 36° for the board, 80° / 22° for the state-0 band): the reader's drag **picks** (a row, an arm); it does not orbit.
- The state-0 band's stages are not to scale (the token position inside the body is not in the inventory); it shows only which stage carries which mark.
- A rate bar that is not a class is hatched (a shape), so grey keeps one meaning (NONE) in the 2D charts too (v1.2 G2).
- The rack's blocks are painted column by column then job by job: in a uniform grid every overlapping pair is separated along x or y, so this order is a valid painter's order for these boxes (no per-pixel sort).
- The block height is the number of tokens written (log10, the cap 12,288 = the lid) — not correctness, not confidence.
