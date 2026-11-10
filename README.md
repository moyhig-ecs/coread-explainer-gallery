# Co-reading explainer gallery

Audited, interactive figures of what a language model writes when it is asked to reason about a geometric configuration — each figure built only from the frozen outputs of a pre-registered measurement, with every number anchored to the data and the cards (the promise written before each run, and the read-out after it) included verbatim.

**What co-reading is for.** Co-reading is a prototype for people reading together what an AI has generated — in course material as well as in research with AI. The most important acceptance condition is **can the next step be seen?** Two makers are there to find the variation: a competition between them is not for picking a winner, but for seeing the difference between the two and receiving the better result.

The gallery is read as **one line of three stations**:

| station | line | what it follows | entry |
|---|---|---|---|
| **1** | **moy-2** | *from algebraic analysis to elementary geometry* — a reflection formula is offered as a tool; does the model compute with it, and what does it then write in its proof field? | [`moy2line_v1_3/`](moy2line_v1_3/) — **[open the figure](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line.html#s0)** (ja, dark) · [en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-en.html#s0) · [light ja](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-light.html#s0) · [light en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy2line_v1_3/dist/moy2line-light-en.html#s0) |
| **2** | **moy-1** | *elementary geometry* — OLMo-3 32B answers one two-circle problem asked open, and with one added sentence that blocks the easy answer "they are concyclic"; then the 20 cards frozen after the first figure (olm76 → olm128) | [`moy1_v3_1/`](moy1_v3_1/) — **[open the figure](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1.html#s0)** (ja, dark) · [en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1-en.html#s0) · [light ja](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1-light.html#s0) · [light en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy1_v3_1/pages/moy1-light-en.html#s0) |
| **3** | **moy-5** | *how to make a model draw the auxiliary line* — where the apex (a mean proportional) appears when frontier models answer one parabola problem: mostly in the reason field, in the answer field only under some arms; then 20 later cards reading the road inside OLMo-3 32B. The board is drawn as a section of a cone, with the cutting plane through the line FVD | [`moy5_v2_3_1/`](moy5_v2_3_1/) — **[open the figure](https://moyhig-ecs.github.io/coread-explainer-gallery/moy5_v2_3_1/dist/moy5_route.html#s0)** (ja, dark) · [en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy5_v2_3_1/dist/moy5_route-en.html#s0) · [light ja](https://moyhig-ecs.github.io/coread-explainer-gallery/moy5_v2_3_1/dist/moy5_route-light.html#s0) · [light en](https://moyhig-ecs.github.io/coread-explainer-gallery/moy5_v2_3_1/dist/moy5_route-light-en.html#s0) |

The hash in a page's URL is the state (the ledger of what is not said: station 1 `#s19`, station 2 `#s37`, station 3 `#s28`–`#s30`). Keys ← → move between states; dragging picks an arm or a row. `?video=1` gives the 1920×1080 frame used in the stills.

## What each entry contains

- `dist/` (station 2: `pages/`) — the built pages (ja / en × dark / light), self-contained; they open from `file://` too. `widget.js` / `widget.css` are the same figure as an [anywidget](https://anywidget.dev) for Jupyter / marimo.
- `captures/` — 1920×1080 stills of every state, plus desk / phone shots.
- `cards/` — the cards of the line, verbatim (Japanese): PREREG (the frozen promise), RESULT (the read-out; corrections appended, never edited in), the closing RECORD, the briefs that ordered the figure, an English index (`INDEX_en.md`), and `PROMPT_PROVENANCE.md` (the question text traced to its public source with an md5 at every stage).
- `CLAIMS.md` + `check_claims.py` — every claim on the page and where its number comes from; the checker re-reads the data.
- `JUDGING_SUMMARY.md` — how the figure was judged and received (see *Method*).
- `MANIFEST.md` — path, bytes and md5 of every file (`python3 -I make_manifest.py --verify`).
- `README.md` — the entry's own guide, with reading glosses for the Japanese cards.

To run an entry offline: download the repository (or the Zenodo archive), open `<entry>/dist/<page>.html`, or serve the folder with `python3 -m http.server` and open it from there.

## Method

The figures are made with the [coread-explainer](https://github.com/moyhig-ecs/coread-explainer) skill for Claude Code, layered on the [Anatomy](https://github.com/wheresryan22/anatomy) kit (MIT, Copyright (c) 2026 Ryan). A figure is built from a card's data by a script, and every number on it is anchored to that data by a checker with a positive control. What the figure cannot say is written on it (the ledger state) and in `CLAIMS.md`.

- **Station 1** was judged on whether the figure can be read correctly: under seal, by readers from a different model family than its maker; the judgments are not pooled.
- **Stations 2 and 3** were judged under the acceptance form v2, which follows the purpose above. Two makers built each station in parallel. Readers then gave three readings: **N**, is the next step visible (their proposed next questions were matched against the cards the house froze after the first figure); **D**, the difference between the two makers; **G**, an audit gate (it does not decide acceptance). A received version was then made by one maker from the readers' choices and the audit's findings. At both stations neither of the first two entries reached the pre-set mark for N; each entry's `JUDGING_SUMMARY.md` gives the counts as they came out.

The measurements themselves use the [ConstructGap](https://github.com/moyhig-ecs/ConstructGap) suite (v1.0.1, DOI 10.5281/zenodo.21617998) for the question text and the apex oracle; the proof-field instruments are the cards' own and are versioned in the cards.

## Versions

| gallery | date | entries |
|---|---|---|
| v1.0.0 | 2026-11-06 | station 1: moy-2 (entry v1.3; house commit `f77eb405`; bundle cut at `6e871959`) — DOI [10.5281/zenodo.23992313](https://doi.org/10.5281/zenodo.23992313) |
| v1.0.1 | 2026-11-06 | the DOI written into README and CITATION.cff (no change to the figures) — DOI [10.5281/zenodo.23992395](https://doi.org/10.5281/zenodo.23992395) |
| v1.1.0 | 2026-11-10 | station 2: moy-1 (received version v3.1; bundle cut at house commit `674b789f`) · station 3: moy-5 (received version v2.3.1; bundle cut at house commit `338726f5`) · the purpose of co-reading and the acceptance form v2 in this README — DOI [10.5281/zenodo.24096885](https://doi.org/10.5281/zenodo.24096885) |

Each release is archived on Zenodo. **Concept DOI (all versions): [10.5281/zenodo.23992312](https://doi.org/10.5281/zenodo.23992312)**.

## License and citation

MIT (`LICENSE`, Copyright (c) 2026 Manabu Higashida). The Anatomy kit's style sheet, page shell and camera formula used in the pages are MIT, Copyright (c) 2026 Ryan (notice in every page and in each entry's `LICENSE-Anatomy.txt`). The model outputs quoted in the entries are data and are not covered by the license.

Cite the gallery with `CITATION.cff` (DOI 10.5281/zenodo.23992312, all versions), or an entry with its own `CITATION.cff`.

---

## 日本語

言語モデルが幾何の問いに何を書くかを、凍結した札(走らせる前の約束 = PREREG・読み = RESULT)の出力だけから描いた、監査つきの図解の置き場。coread の目的は、授業資料を含めて、AI との研究活動においても、人間が AI の「生成物」を共有読解するための原型であること。「次が見えるか」が最も重要な受領条件。二口はバラツキの発見であり、競作は勝者を選ぶのではなく、双方の差を見極めてより良いものを受領する。三駅を一連の流れで読む: **第一駅 moy-2 = 代数的解析から初等幾何学へ**(折り返しの式を道具として渡すと、証明の欄に何が植わるか)→ **第二駅 moy-1 = 初等幾何学**(二円の問いを開いて聞く時と、「共円」の易しい答えを一文で塞ぐ時・その後の札 20)→ **第三駅 moy-5 = どうやって補助線を引かせるか**(頂点 = 比例中項が答えの欄に出る腕・円錐の切り口の面)。第一駅は「正しく読めるか」で封を守って審査し、第二駅・第三駅は受領の型 v2(N 次が見えるか・D 二口の差・G 監査の関門)で読んで受領版を作った。各 entry は、頁(ja / en × dark / light・自己完結)・撮影・札の原本(日本語・逐語・英語の索引つき)・問いの文の由来(md5)・数の錨(`check_claims.py`)・審査と受領の要約(`JUDGING_SUMMARY.md`)・MANIFEST を持つ。作り方は [coread-explainer](https://github.com/moyhig-ecs/coread-explainer) skill。
