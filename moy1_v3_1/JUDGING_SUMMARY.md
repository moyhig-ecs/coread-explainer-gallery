# JUDGING_SUMMARY — how station 2 (moy-1) was read and received

This summary is written for the public bundle from three house records: the reading of station 2 under the acceptance form v2 (RESULT of 2026-11-06), the received version v3.1 (the maker's `NOTES.md` §4, in this bundle), and the main session's receipt check (2026-11-09). The readers' full replies, the rubric files, the sealed mapping of entries to makers and the tallies are house records and are **not** in this bundle; nothing below quotes a reader's reply verbatim.

## 0. The acceptance form (why this station was not judged like station 1)

Station 1 (moy-2) was judged on "can the figure be read correctly" (an editor's pass, a video, three questions, the instrument chain). For stations 2 and 3 the PI set a different purpose (2026-11-06): co-reading is a prototype for people reading what an AI produced, and **"can you see what comes next" is the most important acceptance condition**; two makers are there to **find the variation**, not to pick a winner. The form v2 therefore has three parts: **N** = is the next step visible (the condition), **D** = the difference between the two makers, **G** = an audit gate (the AI's job; it does not decide acceptance).

## 1. The reading of the two v2.1 entries (2026-11-06, 10:16–10:45)

- Material: the two entries of 2026-10-28 (v2.1, makers Opus 5.5 xhigh and Sonnet 5.5 max; sealed as P / Q for the readers). Readers: R1 = Fable 5.1 (xhigh), R2 = Opus 5.5 (xhigh); matcher = Fable 5.1 (xhigh). All ran as isolated `claude -p` sessions that could read only their input folder. Cost shown by `claude -p`: about $55.
- Matcher calibration (positive control): on the 12 moy-2 cards, 10 / 10 paraphrases matched to the right card as "same family" and 0 / 10 decoys did — the pre-set lines (≥ 8 / 10, ≤ 1 / 10) passed.
- Disclosed after freezing: the first launch stopped before any API call (the shell did not split the arguments) and was relaunched from a script; two arms could not open their material on the first try (a read-only reader cannot list a folder) and were re-run with the file names written into the request. Criteria, material and calibration lines were not changed.

**N — is the next step visible?** Each reader proposed next questions; the matcher compared them with the 30 moy-1 cards the house froze after the 10-28 figure.

| arm | proposals | same family | near | none |
|---|---:|---:|---:|---:|
| figure, entry P (R1 5 · R2 5) | 10 | **0** | 5 | 5 |
| figure, entry Q (R1 5 · R2 5) | 10 | **0** | 6 | 4 |
| text only (the three briefs; R1 5 · R2 5) | 10 | **0** | 3 | 7 |

- The PI's threshold (≥ 2 same-family cards, at least one from the figure itself) was **not reached by either entry**; the frozen rule stands.
- Borderline (reference, not counted): the matcher noted that four "near olm76" proposals ("does the commit group rise at the start of the answer field rather than at the naming token?") could be read as the same family; under that reading Q would reach 2 and P 1. The reading was not changed after freezing.
- Reading (L3): the "next" did come from the figure's own ledger — both entries' L3 line ("the commit group falls because the answer is not yet closed when O1O2 is named") leads to the question the house tested on 10-30 as olm76 (it did not stand: 28 / 48, p 0.156).
- The proposals the house had not made (16, after the matcher's "none") cluster into: cue × how often the answer starts with JSON × the blocked bind (6 proposals, from every arm and reader — this became olm128); robustness of windows / start points / labels (6); the heads and groups of cmt13's two moments (3); one on what the move to formula text after O1O2 is about (1).

**D — the difference between the makers.** Both readers took P as the base and named largely overlapping states to move over from Q (#s1, #s11 the reason for `\n\n`, #s12 the prompt-edit diff, #s17 the base column, #s18 the k −20 note, #s20, #s21, #s22). Questions only visible when the two are side by side: how to read blocked s8's answer field (the source of P 7 / 10 vs Q 6 / 10), the rule for the card marks, and the rule for dates of cards outside the tree.

**G — audit gate.** 16 findings (11 on mechanism wording, 2 dropped limits, 2 missing sources with limits, 1 seal placeholder). The largest: both entries' L3 line on the commit group disagreed with SCOPE 10-31's "cannot say" after olm76 → remove it or demote it with olm76's result beside it.

What is not said: zero matches with the house's later cards does not prove the figure has no "next" (the matcher counts only re-discoveries of the house's own next steps); figure vs text arms are two readers × 5 proposals and no rate difference is claimed; "the readers' next steps are mostly local" is an impression (L3), not a counted category.

## 2. The PI's decision and the received version

The PI chose a new pair of makers for a received version (v3: base P + the overlapping transplants + the G fixes + "show what came next", Opus 5.5 xhigh and Sonnet 5.5 max), then **v3.1 — one maker (Opus 5.5, effort xhigh)** — merging the two v3 entries under BRIEF v3.1 (`cards/BRIEF_v3_1_…`, `cards/BRIEF_v3_…`): states 0–12 shown as in P, the overlaps of the v3 readings moved over, three rules of the PI (card marks derived by the build; the count of later cards = cards that reached a grade; the olm89 / olm92 line = the frozen +0.01, the +0.02 marked post hoc), four disagreements settled from the data, and the 14 audit findings of the v3 reading fixed. The maker's table of the 14 fixes (G-01 … G-14, with where each was made) is `NOTES.md` §4; the disagreements and how they were settled are §3.

| G | fix (summary of `NOTES.md` §4) |
|---|---|
| G-01 | olm76 "does not rise" → "**does not reach the line**" (28 / 48 rows rose; median +0.013; p 0.156) — SCOPE 11-01's wording, in states 27–28, ledger R04, script, README |
| G-02 | the attractor median: read.json +0.0425 (3 digits +0.042) vs SCOPE +0.043 = rounding, noted |
| G-03 | +0.02 marked as the line set after seeing olm86 (post hoc) in table note, legend, status line, K53 |
| G-04 | "only k = 8" → "the surplus that appears consistently is only k = 8 (olm86's k = 16 vanishes at 400 rows)" |
| G-05 | layer statements replaced by the operation's name and each card's own layer (olm106 / olm108 / olm101) |
| G-06 | "continuations derived from orthogonality" → "continuations with a sentence that goes from orthogonality to a right angle" |
| G-07 | ledger R01 limited to the cue `\n\n` reading (olm128) |
| G-08 | olm128's post-hoc note separated from the description box; the reading marked L3 |
| G-09 | one line on how cards are counted; station 2 named olm83–92 |
| G-10 | state 27's title asks which questions came from the figure and which continued the house's line 1 |
| G-11 | source of 8 / 53 = `olm59/read.json` key named |
| G-12 | prf4's file and key named |
| G-13 | olm101's DAS key and olm114's k = 0 gate (G2 ✗) named |
| G-14 | "four questions" → "the acceptance questions" |

## 3. The main session's receipt check (2026-11-09, before this bundle)

On a scratch copy of the received entry: anchors **689 / 689**, the checker's positive control **9 / 9**, the whole check run (`run_checks.sh`) exit 0, console clean, internal words 0 (fence over 20 files), and **G-01 … G-14 = 14 / 14 confirmed in the page text** (headless, the innerText of states 27, 28, 30, 32–35, 37, 38, 41, 42 in ja / en: the new wording is present, the old wording is gone, the source key and the anchor exist). The JupyterLab step of the check run had been flaky (the figure's message arrives only after a cell finishes); the main session changed only the check's procedure to retry each cell until its own output matched (`checks/check_jupyter.json`, `checks/make_check_jupyter.py`, log `checks/last_run_20261109_jupyter_fix.txt`; the figure did not change: pages md5 28b2bcd8 / 47c6b01f, widget 8ce9d231). Absolute paths left in the entry were to be dropped when cutting the bundle (done here: `BUNDLE_BUILD.json`).
