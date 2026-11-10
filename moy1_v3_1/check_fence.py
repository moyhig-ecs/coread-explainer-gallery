"""check_fence.py — the public fence: the body of the figure (pages, widget, the sources that build them) carries none of the lab's internal words (SKILL §8). Counts them; exit 1 if any.
The scan has its own control: a text with an internal word is caught, a clean text is not.
    python3 -I check_fence.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
import os
WORDS = [w for w in os.environ.get("FENCE_WORDS", "").split("|") if w]   # bundle: the internal word list is not shipped; set FENCE_WORDS="w1|w2|…" to arm the fence
if not WORDS:
    print("fence: FENCE_WORDS not set — the scan is not armed (0 words)"); sys.exit(0)
rx = re.compile("|".join(re.escape(w) for w in WORDS), re.I)
assert len(rx.findall("この" + "と".join(WORDS[:2]))) == min(2, len(WORDS)) and len(rx.findall("a clean sentence about circles")) == 0, "the fence scan fails its own control"
files = [p for p in sorted(HERE.glob("pages/*")) if p.suffix in (".html", ".js", ".css")] + [HERE / n for n in ("i18n.js", "figure.js", "scenes.js", "figure.css", "state_machine.js", "build.mjs", "widget.py", "widget_glue.js", "demo_marimo.py", "pack_moy1.py", "data.mjs", "i18n_after.js", "scenes_after.js", "pack_after.py")]
hits = {}
for p in files:
    n = len(rx.findall(p.read_text(encoding="utf-8")))
    if n:
        hits[p.name] = n
print(f"fence: {len(files)} files scanned · internal words: {sum(hits.values())} {hits if hits else ''}")
sys.exit(1 if hits else 0)
