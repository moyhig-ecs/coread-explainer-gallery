# <name> — an audited co-reading explainer (template)

An interactive isometric figure of a frozen readout, as a page (dark / light × ja / en) and as a native anywidget (Jupyter / marimo), with 1920 × 1080 stills, a two-voice script and a ledger of what can / cannot be said.
Built on the `anatomy` skill's kit (MIT, Copyright (c) 2026 Ryan; not copied here: build.mjs reads it from `$ANATOMY`, else `~/.claude/skills/anatomy`; it is needed only at build time, `dist/` is self-contained). The MIT notice stays in every page and in this file.

## Run
```sh
~/.bun/bin/bun build.mjs                 # pack_data.py → data.mjs (recount) → dist/*.html, dist/widget.js, dist/widget.css, dist/build_report.json
python3 -I list_headings.py              # the headings of the states, the chapters, the step groups: read it after any renumbering
python3 -I check_claims.py               # every claim row ↔ an anchor, every anchor looks at its place
python3 -I make_check.py checks && sh run_checks.sh   # console · robust · chapter buttons · smallest px · overflow · one capture
```
Open `dist/synthetic.html#s1` (the hash is the state). `?lang=en`, `?theme=light`, `?video=1` (the 1920 × 1080 frame).

## States (from config.json; the numbers live only there)
| n | chapter | what it shows |
|---|---|---|
| 0 | scene | ... |

## Files
| file | role | hand-written / generated |
|---|---|---|
| `config.json` | chapters (= the numbers of the states), pages, min px, frames | hand |
| `pack_data.py` · `data.mjs` | the first and second route of every number | hand |
| `figure.js` · `i18n.js` · `figure.css` | what to draw per state · the words · the style | hand (replace for a new subject) |
| `state_machine.js` | the engine (states, chapters, hash, buttons, camera, texts, host API) | hand (does not change per subject) |
| `build.mjs` | pages + widget from the above and the kit | hand |
| `widget.py` · `widget_glue.js` · `demo_marimo.py` | the anywidget, its two-way glue, a marimo app | hand |
| `check_claims.py` · `claims_anchors.json` · `make_check.py` · `list_headings.py` | the checks | hand |
| `CLAIMS.md` · `NOTES.md` · `SCRIPT_yukkuri.md` | sources of each sentence · history · the two-voice script | hand |
| `dist/` · `generated/` · `checks/` · `captures/` | outputs | generated |
