# Co-reading explainer gallery

Audited, interactive figures of what a language model writes when it is asked to reason about a geometric configuration — each figure built only from the frozen outputs of a pre-registered measurement, with every number anchored to the data and the cards (the promise written before each run, and the read-out after it) included verbatim.

The gallery is read as **one line of three stations**:

| station | line | what it follows | entry |
|---|---|---|---|
| **1** | **moy-2** | *from algebraic analysis to elementary geometry* — a reflection formula is offered as a tool; does the model compute with it, and what does it then write in its proof field? | [`moy2line_v1_3/`](moy2line_v1_3/) — **[open the figure](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line.html#s0)** (ja, dark) · [en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-en.html#s0) · [light ja](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-light.html#s0) · [light en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-light-en.html#s0) |
| 2 | moy-1 | *elementary geometry* — binding the right object in a four-point configuration, and what opens or blocks the proof | to come |
| 3 | moy-5 | *how to make a model draw the auxiliary line* — the route to the apex (the mean proportional) splits by arm | to come |

The hash in a page's URL is the state (`#s8` = the rack of 420 rows, `#s9` = the Fisher card, `#s19` = the ledger of what is not said). Keys ← → move between states; dragging picks an arm or a row. `?video=1` gives the 1920×1080 frame used in the stills.

## What each entry contains

- `dist/` — the built pages (ja / en × dark / light), self-contained; they open from `file://` too. `widget.js` / `widget.css` are the same figure as an [anywidget](https://anywidget.dev) for Jupyter / marimo.
- `captures/` — 1920×1080 stills of every state, plus desk / phone shots.
- `cards/` — the cards of the line, verbatim (Japanese): PREREG (the frozen promise), RESULT (the read-out; corrections appended, never edited in), the closing RECORD, the briefs that ordered the figure, an English index (`INDEX_en.md`), and `PROMPT_PROVENANCE.md` (the question text traced to its public source with an md5 at every stage).
- `CLAIMS.md` + `check_claims.py` — every claim on the page and where its number comes from; the checker re-reads the data.
- `JUDGING_SUMMARY.md` — the sealed cold judging of the figure by readers from another model family.
- `MANIFEST.md` — path, bytes and md5 of every file (`python3 -I make_manifest.py --verify`).
- `README.md` — the entry's own guide, with reading glosses for the Japanese cards.

To run an entry offline: download the repository (or the Zenodo archive), open `<entry>/dist/<page>.html`, or serve the folder with `python3 -m http.server` and open it from there.

## Method

The figures are made with the [coread-explainer](https://github.com/moyhig-ecs/coread-explainer) skill for Claude Code, layered on the [Anatomy](https://github.com/wheresryan22/anatomy) kit (MIT, Copyright (c) 2026 Ryan). A figure is built from a card's data by a script, every number on it is anchored to that data by a checker with a positive control, and the finished figure is judged under seal by readers from a different model family than its maker; the judgments are not pooled. What the figure cannot say is written on it (the ledger state) and in `CLAIMS.md`.

The measurements themselves use the [ConstructGap](https://github.com/moyhig-ecs/ConstructGap) suite (v1.0.1, DOI 10.5281/zenodo.21617998) for the question text and the apex oracle; the proof-field instruments are the cards' own and are versioned in the cards.

## Versions

| gallery | date | entries |
|---|---|---|
| v1.0.0 | 2026-11-05 | station 1: moy-2 (entry v1.3; house commit `f77eb405`; bundle cut at `6e871959`) |

Each release is archived on Zenodo; the DOI is written here and in `CITATION.cff` once it exists.

## License and citation

MIT (`LICENSE`, Copyright (c) 2026 Manabu Higashida). The Anatomy kit's style sheet, page shell and camera formula used in the pages are MIT, Copyright (c) 2026 Ryan (notice in every page and in each entry's `LICENSE-Anatomy.txt`). The model outputs quoted in the entries are data and are not covered by the license.

Cite the gallery with `CITATION.cff`, or an entry with its own `CITATION.cff`.

---

## 日本語

言語モデルが幾何の問いに何を書くかを、凍結した札(走らせる前の約束 = PREREG・読み = RESULT)の出力だけから描いた、監査つきの図解の置き場。三駅を一連の流れで読む: **第一駅 moy-2 = 代数的解析から初等幾何学へ**(折り返しの式を道具として渡すと、証明の欄に何が植わるか)→ 第二駅 moy-1 = 初等幾何学 → 第三駅 moy-5 = どうやって補助線を引かせるか。各 entry は、頁(ja / en × dark / light・自己完結)・撮影・札の原本(日本語・逐語・英語の索引つき)・問いの文の由来(md5)・数の錨(`check_claims.py`)・封を守った冷間の審査の要約・MANIFEST を持つ。作り方は [coread-explainer](https://github.com/moyhig-ecs/coread-explainer) skill。
