# Co-reading explainer — moy-1, received version v3.1

**Station 2 of 3** in the gallery: *moy-1 — elementary geometry*. (Station 1: [moy-2 — from algebraic analysis to elementary geometry](../moy2line_v1_3/README.md); station 3: [moy-5 — how to make a model draw the auxiliary line](../moy5_v2_3_1/README.md).)

An audited, interactive figure of how **OLMo-3 32B** answers one two-circle problem (moy-1: the four mixed tangent intersections X1…X4 lie on the circle with diameter O1O2) when the question is asked **open**, and when one added sentence **blocks** the easy answer "they are concyclic" — and of what the house tested **after** the first figure (20 frozen cards, olm76 → olm128), told as one flow up to the next question. **43 states in 15 chapters**, Japanese / English, dark / light, also an anywidget for Jupyter / marimo; 95 stills at 1920 × 1080; a two-voice script; a ledger of what the figure can and cannot say. Every number on the page is anchored to the frozen data (`check_claims.py`, **689 anchors**); the frozen files the figure reads are **copied into this bundle** (`data/`), so the numbers can be recounted here without the house repository.

## Open it

- **Published** (GitHub Pages, gallery v1.1.0, 2026-11-10): [ja dark](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1.html#s0) · [en dark](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1-en.html#s0) · [ja light](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1-light.html#s0) · [en light](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1-light-en.html#s0) — gallery index <https://moyhig-ecs.github.io/coread-explainer-gallery/>, repository <https://github.com/moyhig-ecs/coread-explainer-gallery>. The published files were fetched back and compared with `MANIFEST.md`: 472 / 472 md5 identical (and `MANIFEST.md` itself); every page opened with a clean console at desk, phone and `?video=1` sizes.
- **Pages** (local): `pages/moy1.html#s0` (dark, ja) · `pages/moy1-en.html#s0` (dark, en) · `pages/moy1-light.html#s0` · `pages/moy1-light-en.html#s0`. The `#sN` hash is the state (`#s8` blocked, `#s18` the moment of naming in the SAE trajectory, `#s27` the flow of the later cards, `#s37` the ledger). The pages embed their data and open from `file://` as well as from a web server. Keys: ← → states; `?video=1` gives the 1920 × 1080 frame.
- **Widget**: `widget.py` (anywidget) with `demo_marimo.py` / `demo_jupyter.ipynb`; it reads `generated/pack.json` and, for its recount, `data/`.
- **Stills**: `captures/` (95 PNG: 43 `video_sNN` (ja), 43 `video_en_sNN`, four before / after frames of states 18–19, and five JupyterLab / marimo shots; `captures/INDEX.md`, `captures/capture_log.txt`).
- **Script**: `SCRIPT_yukkuri.md` (two voices, 46 lines, ≈ 285 s), generated from the pack by `make_script.py`.
- **The maker's own README**: `ENTRY_README.md` — the 43 states one by one, the build and check commands, and what changed from v2.1 → v3 → v3.1.

## What is in the bundle

| path | what |
|---|---|
| `pages/` | the four built pages, `widget.js` / `widget.css`, `build_report.json` |
| `data/` | **the frozen files the figure reads**, at their repository paths (192 files, 11.9 MB): the read-outs of the olm cards (`ConstructGap/exp/olmNN/read.json`, `control.json`, the two `gen.json` of olm112 / olm114), olm59's 120 row files (`rows/*.npz`), the probe results (pc1, the two screens, the two F5 runs, cmt5 / cmt13, the frozen replication config), `moy_suite_report.json`, the card tree, the inventory's check values, and the cards' PREREG / RESULT / SCOPE files the scripts read. `data/SOURCES.tsv` = md5 and bytes of each; `data/git_facts.json` = the answers of `git log` the scripts ask (freeze commits, file dates), recorded when the bundle was cut |
| `generated/pack.json` | the pack the pages are built from (`pack_moy1.py` + `pack_after.py`; rebuilt inside this bundle and byte-identical to the received one) |
| `cards/` | the **cards, verbatim** (61 files: PREREG / RESULT of the 20 later cards and of olm59 / olm62 / prf4, the records of the earlier probe cards, the two SCOPE notes, BRIEF v3 / v3.1), `INDEX_en.md` (an English index — a guide, not a translation), `SOURCES.tsv` (house path, md5, bytes), `PROMPT_PROVENANCE.md` (the question texts and their md5 chain), `public_constructgap_v1_0_1_literals.json` |
| `CLAIMS.md` | every claim on the page with where its number comes from; the ledger of what is **not** said |
| `claims_anchors.json` + `check_claims.py` | the 689 anchors and the checker (`python3 -I check_claims.py` → `anchors checked: 689 · missing or different: 0 · … control: 9 / 9 wrong anchors reported`) |
| `checks/` | the maker's check files and logs, the 11-09 JupyterLab fix, and `run_checks_bundle_20261109.txt` = the whole check run on a copy of this bundle |
| `JUDGING_SUMMARY.md` | how the station was read (acceptance form v2: is the next step visible · the two makers' difference · audit gate) and received (v3.1, 14 / 14 audit fixes checked) |
| `skill/` | the skill the figure was built with: `coread-explainer` as of house commit `674b789f` (SKILL.md md5 `1f76664d2a856df62e747930ccd6a94a`) |
| `NOTES.md`, `config.json`, `i18n*.js`, `scenes*.js`, `figure.*`, `state_machine.js`, `data.mjs`, `build.mjs`, `widget*.{py,js}`, `pack_*.py`, `make_*.py`, `run_*.sh`, `check_fence.py`, `list_headings.py` | the maker's sources and tools; `build.mjs` needs the Anatomy kit (`$ANATOMY` or `~/.claude/skills/anatomy`) and bun — **only to rebuild**; the built pages need nothing |
| `MANIFEST.md` | path, bytes and md5 of every file (`python3 -I make_manifest.py --verify`) |
| `BUNDLE_BUILD.json`, `BUNDLE_NOTES.md` | how this bundle was cut from the house entry (what was copied, what was left out, every rewrite, the data predicate, the scans) and the cutter's notes |

## Recount and rebuild inside the bundle

- `python3 -I check_claims.py` — 689 / 689 against `data/` (the default of `MOY1_REPO` is now this bundle's `data/`; set `MOY1_REPO` to read the frozen files from elsewhere; when `MOY1_REPO` is a git checkout the scripts ask git itself instead of `data/git_facts.json`).
- `PY=python3 bun build.mjs` — reruns the pack and the JS recount and rebuilds the pages; on 2026-11-09 the rebuild inside a copy of this bundle gave the same bytes as the received pages (`moy1.html` 28b2bcd8…, `moy1-en.html` 47c6b01f…, `widget.js` 8ce9d231…; every file of `pages/` and `generated/` identical).
- `sh run_checks.sh checks` — the whole check run (build · headings · claims · script · fence · all 43 states in video / desk / phone × ja / en · robustness · reduced motion · parity · drag / keys / slider · the SAE inset · card marks · chapters (real clicks) · words · marimo and JupyterLab in both directions). Ports: `MARIMO_PORT`, `JUPYTER_PORT`. The internal-word fence is armed only when `FENCE_WORDS="w1|w2|…"` is set (the list is not shipped).
- `python3 -I make_prompt_provenance.py` — rewrites `cards/PROMPT_PROVENANCE.md` and checks every frozen md5 of the question texts (0 mismatches).

## Provenance

- **Models**: OLMo-3-1125-32B base (bf16, no chat template) for the olm and most probe cards, and the OLMo-3 32B behaviour screen (the figure's "Think" column); the "models" chapter (states 16–17) shows the screen of several open models from `moy_suite_report.json`. **Frontier model names stay in the data copies** as the read-outs wrote them: `prf4/read.json` (Opus 5.5 / Fable 5.1 through `claude -p`), the frozen replication config (Fable 5 / Opus 5), `olm114` (prefixes taken from frontier proofs), and the suite report.
- **Question texts**: `cards/PROMPT_PROVENANCE.md` — the open text is ConstructGap's `prompts.build('higashida_circle', 'A', 37)` as frozen on 2026-07-28 (`replication_config_frozen.json`, md5 of the file `c75122018f12b9031a4354b388be9a6d`; open `3c7a63dd…`, blocked `616682f5…`); blocked = open + the public literal `ARMS_APPEND['higashida_circle']['closure-forcing']` of ConstructGap **v1.0.1** (byte-identical); the cues `\n` / `" "` / `\n\n` and the F5a-2 / F5b-1 edits reproduce the frozen md5 of what OLMo received (`03938930…`, `c79980dc…`, `cc05d498…`). The open text itself **cannot be rebuilt here without running the suite's code** (its coordinates are computed), and the bundle does not run it.
- **Versions of this figure**: v1 / v2 / v2.1 (two makers, 2026-10-28) → read under the acceptance form v2 (2026-11-06) → v3 (two makers) → **v3.1** (one maker, 2026-11-06) → two fixes by the main session that did not change the figure's content (10-28 evening: the chapter and state buttons moved to the top of the page; 11-09: the JupyterLab check retries each cell until its own output matches). House HEAD when this bundle was cut: `674b789f`.
- **Makers**: v3 = **Opus 5.5 (effort xhigh)** and **Sonnet 5.5 (effort max)**; **v3.1 = Opus 5.5 (effort xhigh)**, one maker. Readers of the v2.1 pair: Fable 5.1 and Opus 5.5 (xhigh); matcher Fable 5.1 (`JUDGING_SUMMARY.md`). This bundle was cut by Opus 5.5 (`BUNDLE_NOTES.md`).

## What is not said

The figure's ledger is states 37–42 and `CLAIMS.md` (the × rows and the L3 rows). In short: the readings of the main session are marked L3 and adoption is the PI's; no mechanism or circuit is claimed for the SAE / lens curves; models are not put on one curve or ranking; the later cards' grades are SCOPE 11-01's or the RESULT's frozen bands, and "+0.02" is a line set after seeing olm86.

## Reading glosses (for the verbatim Japanese cards and the maker's notes)

- *sensei* (the Japanese word for "teacher", written in kanji in the cards and in the card copies under `data/`) — the principal investigator (PI); it is how the assistant that wrote the cards addresses its principal, and it is left as written there. The pages do not use the word; in the maker's notes, script and README outside `cards/` and `data/` it was rewritten as 依頼者 (the requester) when the bundle was cut.
- **主 session** — the main Claude Code session that wrote the cards; sub-agents are named by role (maker, reader, auditor).
- **札** card · **腕** arm · **帯** band · **関門** gate · **計器** instrument · **判定** verdict · **記述** description — see `cards/INDEX_en.md`.
- **zebrashark** — the lab's build host (an M2 Ultra) named in the cards' run notes.
- `<entry>`, `<repo>`, `<scratch>`, `<home>` in the maker's notes and logs stand for the house paths that were masked when the bundle was cut.

## License and citation

- This bundle: **MIT** (`LICENSE`, Copyright (c) 2026 Manabu Higashida). The pages use the Anatomy kit's style sheet, page shell and camera formula — **MIT, Copyright (c) 2026 Ryan** (`LICENSE-Anatomy.txt`; the notice is in every page). The model outputs quoted in `data/` and `cards/` are data, not covered by the license.
- Cite: `CITATION.cff` (gallery concept DOI [10.5281/zenodo.23992312](https://doi.org/10.5281/zenodo.23992312)). Related: ConstructGap v1.0.1, DOI 10.5281/zenodo.21617998.

---

## 日本語の一段

moy-1(二円の四つの混合の接線の交点 X1〜X4 は O1O2 を直径とする円の上にある)を、問いを開いたまま(open)と、「共円と言うだけでは足りない」の一文で易しい答えを塞いだ時(blocked)に、OLMo-3 32B がどう答えるかを、凍結した札の出力だけから描いた図解の受領版 v3.1。10-28 の図の後に家が打った札 20 本(olm76〜olm128)を一つの流れにして、次の問いまで見せる。43 状態・15 章・頁の数は全部 data に錨(689 本・`check_claims.py`)。図が読む凍結の file は `data/` に repo の相対 path のまま写した(192 file)ので、家の repo なしで数え直せる。札は `cards/` に逐語(日本語のまま・英語は索引 `INDEX_en.md`)。問いの文の由来は `cards/PROMPT_PROVENANCE.md`。作り手 = v3 は Opus 5.5(xhigh)と Sonnet 5.5(max)の二口・v3.1 は Opus 5.5(xhigh)一人。受領の読み = `JUDGING_SUMMARY.md`。
