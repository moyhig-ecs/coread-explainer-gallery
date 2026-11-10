# coread-explainer

An agent skill (Claude Code) for building **audited "co-reading" explainers**: an interactive isometric figure of a frozen instrument readout (a logit / tuned lens, a probe, a benchmark run, a sensor log), wrapped as a native anywidget for Jupyter / marimo, with 1920 × 1080 stills, a short two-voice video script, and a ledger of what can / cannot be said.

The figure is a surface where a human reader (an editor, a reviewer, a student, an explainer-video maker) and an AI read **the same readout** and align their understanding with what the instrument can actually read. So the skill is mostly discipline: read only frozen outputs of a pre-registered measurement (a "card" = PREREG + script + JSON with provenance), recount every number by independent routes, put the limits on every screen, keep a ledger (said / read / not said), and turn a question raised by the figure into a new frozen card before answering it.

The drawing itself (isometric camera, four-step shading, plate, parts) comes from the [`anatomy`](https://github.com/wheresryan22/anatomy) skill's kit; this skill does not copy the kit.

## Install

```sh
# 1. the anatomy skill first (MIT)
git clone https://github.com/wheresryan22/anatomy ~/.claude/skills/anatomy
# 2. this skill
git clone https://github.com/moyhig-ecs/coread-explainer ~/.claude/skills/coread-explainer
```

## Quickstart (the template in `assets/`, on synthetic data)

```sh
cd ~/.claude/skills/coread-explainer/assets
ANATOMY=~/.claude/skills/anatomy bun build.mjs     # pack_data.py → data.mjs (recount) → dist/*.html, dist/widget.js / .css, dist/build_report.json
sh run_checks.sh                                    # headings · claims · console / robust / chapter buttons / smallest px / overflow in three frames · captures/
```

`run_checks.sh` reads `PY` (default `python3`), `BUN` (default `~/.bun/bin/bun`) and `ANATOMY` from the environment. Open `dist/synthetic.html#s1` (the hash is the state); `?lang=en`, `?theme=light`, `?video=1`. To start a new explainer, copy `assets/` to a new entry folder and follow `SKILL.md` and `references/implementation.md`.

## Requirements

- The `anatomy` skill (MIT, https://github.com/wheresryan22/anatomy) at `~/.claude/skills/anatomy`, or anywhere with the env `ANATOMY` pointing to it. **Anatomy is needed only at build time; the built `dist/` is self-contained** (no external script or stylesheet; the Anatomy MIT notice is written into every page). `dist/build_report.json` records the md5 of the kit's `kit/iso-kit.mjs` and the first dated heading of its `CHANGELOG.md`.
- bun ≥ 1.3, or Node ≥ 20.10 (the Anatomy kit does not run on older Node).
- Python 3.12+ and anywidget; marimo / JupyterLab optional (for the widget demo).
- Chromium (for the checks and captures, driven by Anatomy's `scripts/drive.mjs`).

## Contents

- `SKILL.md` — the skill (frontmatter in English; body in Japanese).
- `references/` — data contract, implementation, wording, checks and captures, co-reading loop, judging, publishing, brief template (Japanese).
- `templates/JUDGE_criteria_template.md` — a skeleton of the criteria file for the cold review.
- `assets/` — the smallest runnable template (synthetic data → build → checks → captures); `assets/_smoke/` holds two captures (the 1920×1080 video frame and the dark page, state 1) from a clean-environment run of the template.

URLs that appear inside quoted model outputs in an explainer are verbatim quotes of the model's output, not references made by this skill.

## License

MIT — Copyright (c) 2026 Manabu Higashida (see `LICENSE`).
The pages built with this skill use the Anatomy kit's sheet, page shell and camera formula: **Anatomy — MIT, Copyright (c) 2026 Ryan**. Keep that notice in the pages and in the README of anything you publish.

## Citation

See `CITATION.cff` (the DOI is added after the release is archived).

---

## 日本語(概要)

凍結した計測の出力(札 = PREREG + script + provenance つきの JSON)から、監査つきの「共読」の図解を作る agent skill です。図解は、人間の読み手(編集者・査読者・学生・解説動画の作者)と AI が同じ読み出しを見て、計器が実際に読めることに理解をそろえるための面です。中身は規律です: 凍結した data だけを読む・数を独立な経路で数え直す・限定を全画面に出す・言える / 読み / 言えないを台帳にする・図から出た問いは札に凍結してから答える。描き方は `anatomy` skill(MIT)の kit を使い、kit は写しません(build の時だけ要り、できた `dist/` は自己完結)。導入は anatomy を先に `~/.claude/skills/anatomy`(または env `ANATOMY`)へ、次にこの skill を `~/.claude/skills/coread-explainer` へ。本文(`SKILL.md`・`references/`)は日本語です。License は MIT(Copyright (c) 2026 Manabu Higashida)・Anatomy は MIT(Copyright (c) 2026 Ryan)。
