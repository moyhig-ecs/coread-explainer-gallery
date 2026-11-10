"""list_headings.py — print the headings of every state and check the renumbering (template). Run it after every change of config.json's chapters or of the states' order, and read the list.
A renumbering script that shifts numbers file by file can shift one twice (it really happened); this reads the numbers from where they live and says what does not line up.
    python3 -I list_headings.py        (exit 1 if a heading is out of order, chapters do not tile the states, or figure.js / i18n.js disagree with config.json)
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
chapters, n_states = cfg["chapters"], cfg["chapters"][-1][2] + 1
bad = []
if any(b < a or (i == 0 and a != 0) or (i > 0 and a != chapters[i - 1][2] + 1) for i, (_, a, b) in enumerate(chapters)):
    bad.append("config.json chapters do not tile the states 0..N-1")
chapter_of = lambda n: next(c for c, a, b in chapters if a <= n <= b)
TBL = json.loads((HERE / "generated" / "states_table.json").read_text(encoding="utf-8"))          # the headings as the built page has them (build.mjs evaluates i18n.js + figure.js and writes this)
split = lambda t, word: (int(re.match(word + r" (\d+) · ", t).group(1)), t.split(" · ", 1)[1])
ja, en = [split(r["ja"], "状態") for r in TBL], [split(r["en"], "State") for r in TBL]
fig_chapters = [(r["chapter"], r["mode"]) for r in TBL]
for lang, lst in (("ja", ja), ("en", en)):
    if [n for n, _ in lst] != list(range(n_states)):
        bad.append(f"{lang} kickers are {[n for n, _ in lst]}, expected 0..{n_states - 1} in order")
if len(fig_chapters) != n_states:
    bad.append(f"figure.js has {len(fig_chapters)} states, config.json has {n_states}")
else:
    for n, (c, _) in enumerate(fig_chapters):
        if c != chapter_of(n):
            bad.append(f"state {n}: figure.js says chapter {c}, config.json says {chapter_of(n)}")
print(f"states: {n_states} · chapters: " + " / ".join(f"{c} {a}-{b}" for c, a, b in chapters) + " · step groups: " + str([b - a + 1 for _, a, b in chapters]))
for n in range(n_states):
    j = next((t for k, t in ja if k == n), "?"); e = next((t for k, t in en if k == n), "?"); c, m = fig_chapters[n] if n < len(fig_chapters) else ("?", "?")
    print(f"  {n:>2}  {chapter_of(n):<8} {m:<7} ja: {j[:36]:<36} | en: {e[:44]}")
for b in bad:
    print("  !!", b)
print("headings ok" if not bad else "headings NOT ok")
sys.exit(1 if bad else 0)
