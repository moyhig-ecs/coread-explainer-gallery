# Co-reading explainer — the moy-2 reflection-tool line (olm113 → olm127)

**Station 1 of 3** in the gallery: *moy-2 — from algebraic analysis to elementary geometry*. (Station 2: moy-1 — elementary geometry; station 3: moy-5 — how to make a model draw the auxiliary line. Links are added as each station is published.)

An audited, interactive figure of what **OLMo-3 32B base** writes in its *proof field* when a reflection formula is offered to it as a tool. Twenty states, Japanese / English, dark / light, also an anywidget for Jupyter / marimo; 1920×1080 stills; a two-voice script; and a ledger of what the figure can and cannot say. Every number on the page is anchored to the data (`check_claims.py`, 129 anchors), the question text is traced to the public ConstructGap suite with an md5 at every stage, and the cards (the frozen promise before each run and the read-out after it) are included verbatim.

## Open it

- **Published** (GitHub Pages, gallery v1.0.0, 2026-11-05): [ja dark](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line.html#s0) · [en dark](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-en.html#s0) · [ja light](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-light.html#s0) · [en light](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-light-en.html#s0) — gallery index <https://moyhig-ecs.github.io/coread-explainer-gallery/>, repository <https://github.com/moyhig-ecs/coread-explainer-gallery>. The published files were fetched back and compared with `MANIFEST.md`: 231 / 231 md5 identical.
- **Pages** (local): `dist/moy2line.html#s0` (dark, ja) · `dist/moy2line-en.html#s0` (dark, en) · `dist/moy2line-light.html#s0` · `dist/moy2line-light-en.html#s0`. The `#sN` hash is the state (`#s8` = the rack of 420 rows, `#s9` = the Fisher card, `#s19` = the ledger). The pages embed their data, so they open from `file://` as well as from a web server. Keys: ← → states; drag picks an arm (state 6) or a row (states 8, 11–13). `?video=1` gives the 1920×1080 frame.
- **Widget**: `moy2line_widget.py` (anywidget) with `demo_marimo.py` / `demo_jupyter.ipynb`.
- **Stills**: `captures/` (89 PNG: `video_*` 1920×1080, `page_*` desk, `phone_*`, and the marimo / JupyterLab shots) with `captures/capture.log`.
- **Script**: `SCRIPT_yukkuri.md` (two voices, 21 lines, ≈149 s), generated from the pack by `make_script.py`.
- **The maker's own README**: `ENTRY_README.md` — the 20 states one by one, the build and check commands, and what changed between v1 and v1.3.

## What is in the bundle

| path | what |
|---|---|
| `dist/` | the four built pages, `widget.js` / `widget.css`, `build_report.json` |
| `data/` | the frozen inventory (`moy2_line_inventory.json`, md5 `3190663e…`, plus the inventory script's stdout `moy2_line_inventory.out`) and the seven `read/olmNNN.json` read-outs the inventory was counted from |
| `generated/pack.json` | the pack the pages are built from (`pack_moy2.py`; regenerated inside this bundle and byte-identical to the frozen one) |
| `cards/` | the **cards of the line, verbatim** (PREREG = the promise frozen before each run; RESULT = the read-out; corrections are appended at the end, never edited in), the closing RECORD, the four BRIEFs that ordered the figure, the fact-check MEMO the figure quotes, the inventory script, `PROMPT_PROVENANCE.md` (the question text and its md5 chain), `INDEX_en.md` (an English index — a guide, not a translation), `SOURCES.tsv` (house path and md5 of each file) |
| `CLAIMS.md` | every claim on the page with where its number comes from (§A–§K); §G is the ledger of what is **not** said |
| `claims_anchors.json` + `check_claims.py` | the 129 anchors and the checker (`python3 -I check_claims.py` → `anchors checked: 129 · missing or different: 0`); its positive control `make_anchors_broken.py` + `--anchors checks/anchors_broken.json` reports 12 broken anchors |
| `checks/` | the maker's check logs (console, robustness, chapter buttons, drag, overflow, marimo, JupyterLab) and the two logs of the checker run inside this bundle |
| `JUDGING_SUMMARY.md` | the sealed cold judging (two reader families, judgments not pooled), copied verbatim from the house records |
| `skill/` | the skill the figure was made with (coread-explainer, public form v0.1.0 = the house version of 2026-11-04 with house-specific paths and names generalized) |
| `NOTES.md`, `config.json`, `i18n.js`, `figure.js`, `state_machine.js`, `art.mjs`, `data.mjs`, `build.mjs`, `drive.mjs`, `make_*.py`, `run_*.sh` | the maker's sources and tools; `build.mjs` needs the Anatomy kit (`$ANATOMY` or `~/.claude/skills/anatomy`) and bun ≥ 1.3 — **only to rebuild**; the built pages need nothing |
| `MANIFEST.md` | path, bytes and md5 of every file (`python3 -I make_manifest.py --verify`) |
| `BUNDLE_BUILD.json` | how this bundle was cut from the house entry: what was copied, what was left out, every path rewrite |

## Provenance

- **Model**: OLMo-3 32B base (the olm cards; 60 rows per arm, three seeds, temperature and length cap as in each PREREG). **Frontier controls**: the prf4 / prf5 cards (Opus 5.5 / Fable 5.1 through `claude -p`, JSON only), 20 / 20 apex, 0 / 20 line symmetry.
- **Question text**: `cards/PROMPT_PROVENANCE.md` — `prompts.build("higashida_axis", "A", 37)` of ConstructGap **v1.0.1** (`prompts.py` md5 `abf43cfc…`) → the "reasoning first" edit → `APPEND_M2` (status / proof) → the Tool section inserted after the premises; md5 reproduced at every stage inside the bundle (`make_prompt_provenance.py`).
- **Instruments**: regex / predicate read-outs of the proof field, versioned v3 → v6 (RECORD §3 "計器の系譜"); the frozen verdicts use v3, v6 is shown as reference. The apex verdict is the suite's own `closure_higashida_axis` oracle, unchanged.
- **Cards and corrections**: 13 olm cards (olm113, 116–127), prf4, prf5, the RECORD. Corrections found after freezing are appended at the end of the affected RESULT / RECORD files (dated); the page uses the corrected values (CLAIMS §H and §I–§K list them).
- **Versions of this figure**: v1 (two makers, `eb98bcc4`) → v1.1 (`03318c59`) → v1.2 (`c5a294a6`) → **v1.3** (`f77eb405`, 2026-11-04 16:38 JST). The numbers did not change after v1.1; v1.2 / v1.3 changed display and script only. House HEAD when this bundle was cut: `6e871959`.
- **Maker and readers**: made by **Claude Opus 5.5 (effort xhigh)** from BRIEF v1 → v1.3; judged under seal by Fable 5.1 and Sonnet 5.5 (`JUDGING_SUMMARY.md`). In the sealed rounds this entry was called *entry Q*; the name stays in the maker's files.

## What is not said (the ledger — page state `#s19`, CLAIMS §G)

- ×: an order of the three sentences (declaration > instruction > formula only); that olm125's 0.225 is noise or the instruction's effect; putting a rise on the instruction's meaning alone; that the b2_j07-type rows are the same proposition rejected and revived; that olm127's zero means "fixed"; "the model hesitated" for the S8 / S10 repeats; a mechanism for "no reading ahead"; mixing "landed on the apex" with "checked it"; correctness rates; learnability of an evaluation function from this data; the inside of frontier models.
- L3 (main session; the teacher decides): RESULT olm125 §4 (the Tool section's text read as a cue) · RESULT olm127 §4 (the reject does not reach the commit) · RECORD §4 · MEMO §3 / §4.

(copied from `CLAIMS.md` §G; the page's state 19 prints the same ledger.)

## Reading glosses (for the verbatim Japanese cards)

- **先生** (*sensei*) — the principal investigator; it is how the assistant that wrote the cards addresses its principal, and it is left as written (on the page it appears in the sentences quoted from the RECORD and the MEMO, states 17–18).
- **主 session** — the main Claude Code session that wrote the cards; sub-agents are named by role (maker, reader, auditor).
- **札** card · **腕** arm · **帯** band (the pre-registered verdict bands) · **関門** gate (G1 = parsed rows ≥ 0.75) · **計器** instrument · **証明の欄** the proof field · **線対称** line symmetry (the false premise on the general figure) · **外接線の印** the outer-tangent marker · **退け** reject.
- **zebrashark** — the lab's build host (an M2 Ultra) named in the cards' run notes.
- **olmNNN** — a card run on OLMo-3 32B base; **prfN** — a frontier control run through `claude -p`.
- URLs inside quoted model output (one, `mathpix.com/…`, in a row's text) are the model's words, not references of ours.

## How this bundle was cut (and what differs from the house entry)

- Copied from the house entry `entry_Q_v1.3` (its pages, captures, data, checks, sources and tools); left out: the sealed judging files, the positive-control runs on older builds, the JupyterLab runtime folder, the browser profile.
- Rewrites (all listed in `BUNDLE_BUILD.json`): the cards' house paths → `cards/…` (106 strings in the anchors, the quoted literals, the pack and the four pages: the pages carry the pack, so the same four provenance strings appear in each); absolute paths in the scripts → `python3` / `bun` / env; the Chrome DevTools port band → env `DRIVE_BAND`; the driver's URL test accepts `https:` (one character; the maker's driver read an https target as a file path), so the same checks can be run against the published pages; absolute paths in the maker's logs → `<ENTRY>` / `<REPO>` / `<TMP>`. The cards themselves are **not** rewritten (three of them mention house paths; `cards/SOURCES.tsv` has their md5).
- `data/read/olm118.json` and `data/read/olm126.json` carry, beside the OLMo rows, the prf5 rows of the frontier control (Opus 5.5 / Fable 5.1); the model names stay as the read-out wrote them.
- `data/moy2_line_inventory.out` is the inventory script's stdout from the build host (the house keeps it untracked); re-running the script on another machine reproduces the inventory JSON except its `made` / `commit` fields.
- Checks run inside this bundle on 2026-11-04: `check_claims.py` 129 / 129 (`checks/check_claims_bundle.log`), positive control 12 / 12 (`checks/positive_control_bundle.log`), `pack_moy2.py` regenerates `generated/pack.json` byte-identically; the page checks (`run_checks.sh checks`: every state of the four pages in video / desk / phone layouts, reduced motion, chapter buttons, drag, overflow, smallest text) run on a copy of this bundle on another machine (a MacBook, Chrome, bun 1.4.3): 260 / 260 ok, 0 bad, console 0 errors on all 25 page loads (`checks/run_checks_bundle_macbook.log`, `checks/summary_bundle_macbook.json`; the maker's original logs are the other `checks/*.log` / `*.json`).

## License and citation

- This bundle: **MIT** (`LICENSE`, Copyright (c) 2026 Manabu Higashida). The pages use the Anatomy kit's style sheet, page shell and camera formula — **MIT, Copyright (c) 2026 Ryan** (`LICENSE-Anatomy.txt`; the notice is in every page). The quoted model outputs are data, not covered by the license.
- Cite: `CITATION.cff` (the DOI is filled in after the first Zenodo release of the gallery). Related: ConstructGap v1.0.1, DOI 10.5281/zenodo.21617998.

---

## 日本語の一段

moy-2(二円の内共通接線の接点 Tc・Th と第三の円の中心 O3 の関係)で、折り返しの式を「道具」として問いの文に添えたとき、OLMo-3 32B base が証明の欄に何を書くか(一般の図では偽の前提「Tc と Th は O1O2 について線対称」が植わるか)を、凍結した札(PREREG = 走らせる前の約束・RESULT = 読み・末尾の訂正)の出力だけから描いた図解。七腕(道具なし・等半径の対照・式 + 宣言・式だけ ×2・式 + 指示 ×2)+ frontier の陰性統制。頁の数は全部 data に錨(129 本・`check_claims.py`)、問いの文は公開 ConstructGap v1.0.1 から md5 の鎖で辿れる(`cards/PROMPT_PROVENANCE.md`)、札は `cards/` に逐語(日本語のまま・英語は索引 `INDEX_en.md`)。言えないことは状態 19 の台帳(`CLAIMS.md` §G)。作り手 = Claude Opus 5.5(xhigh)・冷間の審査 = Fable 5.1 / Sonnet 5.5(`JUDGING_SUMMARY.md`)。
