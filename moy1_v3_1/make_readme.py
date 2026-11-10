"""make_readme.py — writes README.md (the states table is read from generated/states_table.json = the headings as the built page has them; the numbers are read from generated/pack.json). Run after any change of the states.
    python3 -I make_readme.py
"""
import json
import os
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(os.environ.get("MOY1_REPO", HERE / "data"))   # bundle: the frozen files are copied under data/
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
chapters = cfg["chapters"]
chap_of = lambda n: next(c for c, a, b in chapters if a <= n <= b)
TBL = json.loads((HERE / "generated" / "states_table.json").read_text(encoding="utf-8"))
ja = [(r["n"], r["ja"].split(" · ", 1)[1]) for r in TBL]
en = [(r["n"], r["en"].split(" · ", 1)[1]) for r in TBL]
modes = [(r["chapter"], r["mode"]) for r in TBL]
NS = len(ja)
assert len(ja) == len(en) == len(modes) == chapters[-1][2] + 1
is_after = lambda n: any(a <= n <= b for a, b in cfg["parts"]["after"])
rows = "\n".join(f"| {n} | {chap_of(n)} | {'added later' if is_after(n) else '10-28 part'} | {modes[n][1]} | {ja[n][1]} | {en[n][1]} |" for n in range(NS))
P = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
AF = P["after"]
bc, oc = P["blk_cnt"], P["open_cnt"]
O, T5 = P["olm59"], P["olm59"]["cmt5_two"]
R62 = P["olm62"]["read"]
ag = O["agg"]
up = lambda ev, g: ag[ev]["groups"][g]["all"]["up"]
head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short=8", "HEAD"], capture_output=True, text=True).stdout.strip()
gr = lambda g: sum(1 for c in AF["cards"] if c["grade"] == g)
l3, nx, ap = AF["l3"], AF["next"], AF["apex"]
txt = f"""HEAD(R1) = {head} (the checkout's HEAD when this README was generated; git was only read: `rev-parse` / `log` / `status`, nothing was committed or written to the repo).

# moy-1 co-reading explainer — the received version v3.1: one figure from the two makers of v3 (entry_v3_1_received)

An interactive isometric figure of the frozen readouts of the moy-1 experiment (OLMo-3-1125-32B base, one two-circle problem, two prompts that differ by one sentence), as a page (dark / light × ja / en) and as a native anywidget (Jupyter / marimo),
with 1920 × 1080 stills, a two-voice script and a ledger of what can / cannot be said. **{NS} states, {len(chapters)} chapters.**
**What v3.1 is (BRIEF v3.1, 11-06).** One maker joined the two figures of v3 into one: the base is the build of the v3 figure with 43 states (`receipt/entry_v3_sonnet_max`); states 0-12 take the way of showing of the other v3 figure (`receipt/entry_v3_opus_xhigh`), as both cold readers of that range chose;
what the readers' D1-D3 replies named in both copies was moved across (the ±80-character window, the unit "rows with a 'diameter = He-Hi' sentence", the cue `\\n\\n` of chapter 5, the Δmath median split and the numbers outside the card in their own box, the provenance of each later question as thick / dotted rails with one list of the later cards, the +0.02 line told as set after seeing olm86, the chat-model bar of prf4 as another card, R01 limited to cue `\\n\\n`);
the requester's rules were followed as written (card marks = the cards whose data a state reads, **derived by build.mjs**, never a card after 10-28 on a 10-28 state · the number of later cards = the cards read and graded, the ones stopped at a control / gate counted apart · the judgment line of olm89 / olm92 = the frozen +0.01, the +0.02 told as after the fact);
four disagreements were decided from the data (s17 base open = attractor {P["think"]["base"]["open"]["labels_no_cap"]["B-attractor"]} by the frozen rule PREREG pc1 §6, all rows listed beside it · s18: " the" is k −20, " midpoint" k −19 · olm76: frozen b7730f55, re-frozen d7fbbd43 before reading · the values cut in state 23 = 0.781 / 0.221 / 0.489) and the audit's 14 findings (`receipt_read/reads/G3_R2`) were repaired. NOTES.md says what and why, item by item.

**What v3 was.** The base is the 10-28 figure (entry P = `entry_sonnet_max_v2_1`, which two cold readers chose as the base). On it v3 (1) transplants what the other 10-28 figure had and both readers asked for, (2) decides four disagreements between the two 10-28 figures from the data,
(3) repairs the audit's 16 findings, and (4) adds a part for what the home struck **after** the 10-28 figure — {len(AF["cards"])} frozen cards, olm76 to olm128 — told as one flow, then the next question the readers raised, then the ledger.
The part added later **looks different** (hatched nodes, a dashed frame, a ribbon "added later (11-06 version)", dashed buttons) so that it is seen at once; no new hue (grades are told by shape).
Built on the `anatomy` skill's kit (MIT, Copyright (c) 2026 Ryan; not copied here: `build.mjs` reads it from `~/.claude/skills/anatomy` or `$ANATOMY`). The MIT notice stays in every page and in this file.

## What it says in one breath
The two prompts differ by one sentence at the end (blocked = open + {P["prompts"]["tail_len"]} characters; the sentence names neither O1O2 nor He-Hi: it marks a bare concyclic answer as not enough and asks for the centre and the diameter to be named). In blocked the answer field names the circle with diameter O1O2 in **{bc["o1o2"]}** of 10 rows
(open: 0 of 10; open's answer field is a bare "concyclic" in {oc["bare"]} of 10), He-Hi in {bc["hehi"]}, and **one row (s8) has no JSON, so no answer field** (decision 1 below; v2 read its last paragraph and said 7). The {len(P["json_first"]["blocked"])} blocked rows that started by writing the JSON name He-Hi; the {10 - len(P["json_first"]["blocked"])} that started with a sentence are bind (whole-text label).
Around the token where the text names O1O2 as a diameter / midpoint, the layer-32 SAE's "mid" group rises in {up("o_diam", "mid")} of {ag["o_diam"]["n"]} rows (close {up("o_diam", "close")}); the move is mostly with the text moving into formulas ({R62["o_diam"]["math_up"]} / {R62["o_diam"]["n"]}; rank correlation {R62["o_diam"]["spearman_mid_math"]:.3f}).
**After the figure** (the added part): the ledger's reading "close falls because the answer is not yet closed" was measured at the start of the answer field by olm76 and **not supported** (the close group does not reach the line: it rose in {l3["q1"]["pos"]} / {l3["q1"]["n"]} bind rows, median +0.013, p 0.156; false window {l3["pseudo"]["pos"]} / {l3["pseudo"]["n"]}); the look-ahead in the residual is almost all readable from the J-lens readout (the only surplus that shows consistently is a small one at k = 8, layer 32);
when positions are swapped, the share of the behaviour that follows the pointer drops below 0.5 at layer {AF["struct"]["layers"]["sel_drop"]} (olm106) and the set switches to the value at layer {AF["struct"]["layers"]["tail_switch"]} (olm108; synthetic sentences); when asked, the apex proof's chain is {ap["olm112"]["Q1"]["chain"]} / {ap["olm112"]["Q1"]["bind"]} and given the frontier's steps the base model continues in {ap["olm114"]["Q1"]["RA_and_THC"]} / {ap["olm114"]["Q1"]["k1_rows"]} and {ap["olm114"]["Q2"]["THC"]} / {ap["olm114"]["Q2"]["k2_rows"]} continuations;
and the next question the teacher chose from the readers' list (cue × the share of rows starting with the JSON) was frozen and read as olm128: **the start at position 0 does not explain the cue difference** (concordance 11 / {nx["verdicts"]["Q1_N"]} = {nx["verdicts"]["Q1_concordance"]:.3f}); an after-the-fact description is tagged as such and the second stage waits for the teacher.
It does **not** say that the model bound *because* it thought, that the contrast holds across cues (blocked bind: 2 / 9, 4 / 10, 7 / 10), that a head or a layer "is" a mechanism, or which next question to strike (CLAIMS.md C; the ledger, states {[n for n in range(NS) if chap_of(n) == "ledger"][0]}-{NS - 1}).

## What changed from the 10-28 figure (v3 vs `entry_sonnet_max_v2_1`)
1. **Transplants** (from the other 10-28 figure `entry_opus_xhigh_v2_1`; the ones both readers named are all done): the angle ∠O1 Xk O2 beside the distances (state 1) · the reason for cue `\\n\\n` with its source (state 11) · the prompt-edit diff (state 12) · the base model's rows beside Think (state 17) · the sentence that says the circle in words, underlined inside the window (state 18) ·
   a new state of the row-by-row slopes with the path × label breakdown (state 22) · what each path fixes as its first token (state 25's rows) · the tie-averaged rank values tagged "a number outside the card" (state 23) · olm62's Q2 holds two rules (state 24) · the balance metaphor as an L3 row of the ledger.
   Not transplanted: the other figure's per-card chapter buttons on the map (the map already lists the states that use each card) and its 3-D recording table (the slope state carries the same distribution, flat); reasons in NOTES.md.
2. **Disagreements decided from the data** (how, in NOTES.md and in the K anchors): (1) blocked s8's answer field → "no JSON, no answer field" (K69; the frozen `label_json_fields` gives B-flail to 3 / 3 rows without JSON in cmt5) · (2) the rows whose colour changes in open → 6 (five frozen attractor rows + s4), by the predicate "frozen-label colour ≠ answer-field colour" ·
   (3) the date of a card with only a data file → git's last commit of the file (moy_suite_report 06-14), never a month range · (4) card marks → "the cards whose data the state draws" (a number a limit note quotes is not a mark), made a predicate in `config.json` (`state_data` → `card_of_data`) and checked (K43).
3. **The audit's 16 findings** (G-01 to G-16; NOTES.md lists each): G-01 the ledger's L3 now sits in the same row as olm76's result and is demoted to "not supported" (R04) · the others are wording against SCOPE 11-01's "cannot say" and sources added to the status lines.
4. **The added part** (states 27-36 + ledger 40-41): the flow (27) · (a) ledger L3 → olm76 (28) · (b) the inference-space search (29-30) · (c) structure that is not words (31-32) · (d) the apex proof (33-34) · the next question (35-36). Each card shows its frozen commit, its grade (verdict / confirmed description / description / not read) and its source file and keys.

## States
| n | chapter | part | mode | ja | en |
|---|---|---|---|---|---|
{rows}

## Run
```sh
PY=~/miniforge3/envs/py314/bin/python ~/.bun/bin/bun build.mjs      # pack_moy1.py (route 1, asserts; runs pack_after.py) → data.mjs (route 2, JS recount; stops the build) → pages/*.html, pages/widget.js, pages/widget.css
python3 -I list_headings.py              # the headings of the states, the chapters, the step groups: read it after any renumbering
python3 -I make_anchors_v3.py && python3 -I make_anchors_v31.py   # (once, in this order) the v3 anchors, then the v3.1 anchors (make_anchors_v3.py alone would drop the v3.1 ids of K43 / K50-K69)
python3 -I make_claims.py && python3 -I check_claims.py   # CLAIMS.md is generated from the page's ledger rows; every anchor looks at its place in the frozen files (route 4)
python3 -I make_script.py && python3 -I make_readme.py   # SCRIPT_yukkuri.md (numbers read from the data, the length counted) · this file
sh run_checks.sh                         # everything below, in every frame; writes checks/last_run.txt
python3 -I make_captures.py [--en]       # captures/ (1920 × 1080 video stills, desk dark / light × ja / en, phone dark / light)
```
`MOY1_REPO=/path/to/frozen-files` to read the frozen files from elsewhere (the default is this bundle's `data/`). Open `pages/moy1.html#s27` (the hash is the state). `?lang=en`, `?theme=light`, `?video=1` (the 1920 × 1080 frame).
Keys: ← → states · `,` `.` the focus row / position · `l` language · drag = orbit · the slider picks a row, a position or a token. A card mark (the small pill above a headline) is a real button that opens the map of the card tree. The added part's cards are not on that map (it is the tree v2.2.1's).

## Where to look first (for a cold reader who sees only the stills and the documents)
- `captures/INDEX.md` says which file shows which state. The stills of the video frame are `captures/video_sNN.png` (1920 × 1080, ja) and `video_en_sNN.png`.
- **The core of the 10-28 part**: `video_s08.png` (all 20 rows: blocked in focus, open faded) and `video_s04.png`. **The added part**: `video_s27.png` (the flow) then `video_s28.png` … `video_s36.png`; the ledger of it: `video_s40.png`, `video_s41.png`.
- `CLAIMS.md` (every number with its source and the anchors that look at it) · `NOTES.md` (what was done, decided and repaired; what is least certain) · `SCRIPT_yukkuri.md` (the two-voice script with a cue per line).

## Acceptance questions (to answer after looking at the figure; the criteria are here, not in the figure)
{{QUESTIONS}}

## Limits
- One model, one prompt, one cue for chapters 3-4; the cards of the added part use their own rows (cmt5's 120, F5a-2 natural's 400, synthetic sentences, 100 + 120 generations) — each state's strip names them.
- Positions of marks (flags, diamonds, squares) are positions of predicates in the text, not token positions. The pillars (state 15) show the top-10 heads of 16 positions only. The 3-D parts draw back to front by class, not by element: below or behind the camera range the order is wrong (el 15-35, az 50-90 is right).
- "Grades" follow SCOPE 11-01's tiers; from olm101 on the SCOPE does not list the cards, so the grade is the RESULT's own words (stated in the ledger and in each state).

## Files
| file | what |
|---|---|
| `config.json` | the states, chapters, parts (the added part), card marks and the rule of the marks (one place for the numbers) |
| `pack_moy1.py` + `pack_after.py` → `generated/pack.json` | route 1: the numbers, with asserts (the added part's values are read.json keys; the freeze commits are checked against git) |
| `data.mjs` | route 2: a JS recount (also the freeze commits against git) |
| `check_claims.py` + `claims_anchors.json` (+ `make_anchors_v3.py`) | route 4: anchors that look at the frozen files, recounted with separate code |
| `figure.js` · `scenes.js` · `scenes_after.js` · `i18n.js` · `i18n_after.js` · `state_machine.js` · `figure.css` | the figure |
| `build.mjs` | the pages and the widget |
| `make_check.py` · `run_checks.sh` · `make_captures.py` | the checks and the stills |
| `widget.py` · `demo_marimo.py` · `demo_jupyter.ipynb` | the anywidget and its demos |

MIT notice: the pages use the Anatomy kit's sheet, page shell and camera formula — Anatomy, MIT, Copyright (c) 2026 Ryan.
"""
qs = json.loads((HERE / "generated" / "ledger_rows.json").read_text(encoding="utf-8"))["ja"]["questions"]
crit = {
    "問 1": "足した文は末尾の一文(+324 字)で、O1O2 も He・Hi も名指さない。共円で止まる答えを不十分とし、中心と直径の名指しを求める(答えの点の名は与えない)。",
    "問 2": "open の 10 行の答えの欄は 8 行が裸の共円・O1O2 / He・Hi を名指す行は 0。O1O2 を円の直径・中心と名指す文がある行は 0 / 10。",
    "問 3": "JSON から書き始めた 3 行は attractor 3 / 3・文から書き始めた 7 行は bind 7 / 7(全文の label)。「考えたから bind した」とは言えない(相関・n 10・一つの cue)。blocked の答えの欄は O1O2 6・He・Hi 3・JSON なし 1(s8)。",
    "問 4": "O1O2 を名指す所で考えの中点が 48 / 59 で上がり、結びは 9 / 59。事前の予想(結びが立つ)は 6 / 36 と 17 / 34 で外れた。",
    "問 5": "O1O2 を名指した後に本文は数式に移る(48 / 59)。中点の上がりの大半はその移りと一緒に動く(順位相関 0.780)。移らない 11 本でも 7 本が小さく上がる(薄い ✓)。",
    "問 6": "5 章の data は cmt13(系統樹の C2)と F5(系統樹の前)。",
    "問 7": "olm76: 答えの欄の手前でも結びが上がる行は bind の 28 / 48(偽の窓 21 / 48)で、台帳の読みは支持されない。測ったのは結びの群の上がり、言えないのは「結びが答えの欄の手前で立つ」こと。",
    "問 8": "依頼者が選んだ A は olm128 で「書き始めでは説明されない」(11 / 19)。他の候補(B〜E)は並べるだけでまだ凍結していない・結果は無い(E の blocked s8 の答えの欄は図の中で data から決めた = NOTES §2-①)。第二段は依頼者の裁定待ち。",
}
rowsq = "\n".join(f"{i + 1}. **{q['k']}** {q['q']} (state {q['where'].replace('状態 ', '')})\n   Criterion: {crit.get(q['k'], '')}" for i, q in enumerate(qs))
(HERE / "README.md").write_text(txt.replace("{QUESTIONS}", rowsq), encoding="utf-8")
print(f"README.md written: {NS} states · {len(qs)} questions · HEAD {head}")
