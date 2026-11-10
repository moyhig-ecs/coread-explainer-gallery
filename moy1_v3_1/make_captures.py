"""make_captures.py — every state in every frame, through the Anatomy skill's scripts/drive.mjs (headless Chrome, run with bun). Names follow the skill:
  captures/video_s<NN>.png            1920 x 1080 exactly (?video=1; ja, dark)             captures/video_en_s<NN>.png   (en, dark) with --en
  captures/page_dark_s<NN>.png        desk 1440 (the .sh element)       page_light_s<NN>.png   page_dark_s<NN>_en.png   page_light_s<NN>_en.png
  captures/phone_dark_s<NN>.png       phone 390 wide (the .sh element)  phone_light_s<NN>.png
A capture waits until the figure has stopped moving (a fixed wait after an instant goto). The log (captures/capture_log.txt) says what was shot and from which build (md5 of the page).
    python3 -I make_captures.py [--only video,desk,phone] [--states 0,1,2]
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
NS = cfg["chapters"][-1][2] + 1
import os
BUN = os.environ.get("BUN", str(pathlib.Path.home() / ".bun/bin/bun"))
DRIVE = str(pathlib.Path(os.environ.get("ANATOMY", str(pathlib.Path.home() / ".claude/skills/anatomy"))) / "scripts/drive.mjs")
args = sys.argv[1:]
only = (args[args.index("--only") + 1].split(",") if "--only" in args else ["video", "desk", "phone"])
states = [int(x) for x in args[args.index("--states") + 1].split(",")] if "--states" in args else list(range(NS))
CAP = HERE / "captures"
CAP.mkdir(exist_ok=True)
TMP = HERE / "checks"
TMP.mkdir(exist_ok=True)
log = []


def run(frame, page, name_of, W, H, selector=None):
    acts = [["wait", 1800]]
    for s in states:
        acts += [["eval", f"window.__sh.goto({s}, {{instant: true}}); 'state {s}'"], ["wait", 1100]]
        p = str(CAP / name_of(s))
        acts += [["shot", p, "html", 1, [0, 0, W, H]]] if selector is None else [["shot", p, selector, 1]]
    af = TMP / f"_cap_{frame}_{page}.json"
    af.write_text(json.dumps(acts), encoding="utf-8")
    url = f"file://{HERE}/pages/{page}.html" + ("?video=1" if frame == "video" else "")
    t0 = time.time()
    r = subprocess.run([BUN, DRIVE, url, "--actions", str(af), "--width", str(W), "--height", str(H)], capture_output=True, text=True)
    out = (r.stdout + r.stderr)
    ok = r.returncode == 0 and "console: clean" in out
    md5 = hashlib.md5((HERE / "pages" / f"{page}.html").read_bytes()).hexdigest()[:8]
    log.append(f"{time.strftime('%H:%M:%S')} {frame:5s} {page:20s} states {states[0]}..{states[-1]} ({len(states)}) · page md5 {md5} · {time.time() - t0:.0f} s · {'console clean' if ok else 'CHECK: ' + out[-300:]}")
    print(log[-1])
    af.unlink()


F = cfg["frames"]
if "--index-only" in args:
    only = []
if "video" in only:
    run("video", "moy1", lambda s: f"video_s{s:02d}.png", F["video"][0], F["video"][1])
    if "--en" in args:
        run("video", "moy1-en", lambda s: f"video_en_s{s:02d}.png", F["video"][0], F["video"][1])
def pairs():
    """v2 (skill §6: a state that shows a moment gets a before / after pair): states 18 and 19 — the cursor on the last token before the naming that no predicate hits (nothing lights: `a`), then on the first naming token (the circle lights: `b`)."""
    acts = [["wait", 1800]]
    for state, row in ((18, "S_O"), (19, "S_H")):
        for tag, expr in (("a", f"(() => {{ const D = window.__DATA.olm59.{row}; for (let i = D.event - 1; i >= 0; i--) if (D.mask[i] === 0) return i; return 0; }})()"), ("b", f"window.__DATA.olm59.{row}.event")):
            acts += [["eval", f"window.__sh.goto({state}, {{instant: true}}); window.__sh.setT({expr}, true); window.__sh.redraw(); 'state {state}{tag}'"], ["wait", 1100], ["shot", str(CAP / f"video_s{state:02d}{tag}.png"), "html", 1, [0, 0, F["video"][0], F["video"][1]]]]
    af = TMP / "_cap_pairs.json"
    af.write_text(json.dumps(acts), encoding="utf-8")
    t0 = time.time()
    r = subprocess.run([BUN, DRIVE, f"file://{HERE}/pages/moy1.html?video=1", "--actions", str(af), "--width", str(F["video"][0]), "--height", str(F["video"][1])], capture_output=True, text=True)
    out = r.stdout + r.stderr
    log.append(f"{time.strftime('%H:%M:%S')} pairs video moy1                 states 18a 18b 19a 19b · {time.time() - t0:.0f} s · {'console clean' if r.returncode == 0 and 'console: clean' in out else 'CHECK: ' + out[-300:]}")
    print(log[-1])
    af.unlink()


if "video" in only:
    pairs()
if "desk" in only:
    run("desk", "moy1", lambda s: f"page_dark_s{s:02d}.png", F["desk"][0], F["desk"][1], ".sh")
    run("desk", "moy1-light", lambda s: f"page_light_s{s:02d}.png", F["desk"][0], F["desk"][1], ".sh")
    run("desk", "moy1-en", lambda s: f"page_dark_s{s:02d}_en.png", F["desk"][0], F["desk"][1], ".sh")
    run("desk", "moy1-light-en", lambda s: f"page_light_s{s:02d}_en.png", F["desk"][0], F["desk"][1], ".sh")
if "phone" in only:
    run("phone", "moy1", lambda s: f"phone_dark_s{s:02d}.png", F["phone"][0], F["phone"][1], ".sh")
    run("phone", "moy1-light", lambda s: f"phone_light_s{s:02d}.png", F["phone"][0], F["phone"][1], ".sh")
if log:
    with open(CAP / "capture_log.txt", "a", encoding="utf-8") as fh:
        fh.write("\n".join(log) + "\n")

def write_index():
    # captures/INDEX.md — which file shows which state (for a reader who sees only the stills)
    import re
    import struct
    tbl = json.loads((HERE / "generated" / "states_table.json").read_text(encoding="utf-8"))          # the headings as the built page has them (build.mjs writes this)
    ja = {r["n"]: r["ja"].split(" · ", 1)[1] for r in tbl}
    en = {r["n"]: r["en"].split(" · ", 1)[1] for r in tbl}
    kinds = [("video_s{n:02d}.png", "video still, ja, dark", "1920 x 1080 frame"), ("video_en_s{n:02d}.png", "video still, en, dark", "1920 x 1080 frame"),
             ("page_dark_s{n:02d}.png", "desk, dark, ja", "1440-wide window"), ("page_light_s{n:02d}.png", "desk, light, ja", "1440-wide window"),
             ("page_dark_s{n:02d}_en.png", "desk, dark, en", "1440-wide window"), ("page_light_s{n:02d}_en.png", "desk, light, en", "1440-wide window"),
             ("phone_dark_s{n:02d}.png", "phone, dark, ja", "390-wide window"), ("phone_light_s{n:02d}.png", "phone, light, ja", "390-wide window")]

    def png_size(path):  # the pixel size, read from the PNG header (the value comes from the output)
        w, h = struct.unpack(">II", path.read_bytes()[16:24])
        return w, h

    def measured(pat):
        sizes = [png_size(CAP / pat.format(n=n)) for n in range(NS) if (CAP / pat.format(n=n)).exists()]
        if not sizes:
            return "not taken"
        ws = sorted({w for w, _ in sizes}); hs = [h for _, h in sizes]
        return f"image {'/'.join(str(w) for w in ws)} wide x {min(hs)}-{max(hs)} high" if min(hs) != max(hs) else f"image {ws[0]} x {hs[0]}"
    rows = ["# captures — which file shows which state", "", "State numbers come from config.json; the file names follow the coread-explainer skill (`video_s<NN>`, `page_<dark|light>_s<NN>[_en]`, `phone_<dark|light>_s<NN>`).",
            "`J1` / `J2` = JupyterLab (state 0; after the figure's own next button reached the kernel) · `J3` = JupyterLab (v2: state 18 after `goto_chapter(\"sae\")`, with the kernel's recount) · `M1` = marimo (state 4, after a Python button moved the figure) · `M2` = marimo (v2: state 18 after the Python button \"chapter sae\").", "", "| state | what it shows (ja) | what it shows (en) | files present |", "|---|---|---|---|"]
    for n in range(NS):
        have = [pat.format(n=n) for pat, _, _ in kinds if (CAP / pat.format(n=n)).exists()]
        rows.append(f"| {n} | {ja.get(n, '')} | {en.get(n, '')} | {len(have)}: " + ", ".join(f"`{h}`" for h in have) + " |")
    rows += ["", "v2 pairs (skill §6: a moment gets a before / after still; 1920 x 1080, ja, dark): `video_s18a.png` / `video_s18b.png` = state 18 with the cursor on the last token before the naming that no predicate hits (nothing lights) / on the first naming token (the O1O2 circle lights) · `video_s19a.png` / `video_s19b.png` = the same for state 19 (the He-Hi circle).", ""]
    rows += ["| pattern | what | taken in | measured (PNG header) |", "|---|---|---|---|"] + [f"| `{pat.replace('{n:02d}', 'NN')}` | {what} | {frame} | {measured(pat)} |" for pat, what, frame in kinds]
    rows += ["", "The desk and phone stills are of the figure element (the page's margins are outside the image, so the image is narrower than the window); a phone still is as tall as the content (the long ledger state is the tallest)."]
    (CAP / "INDEX.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print("captures/INDEX.md written")
write_index()
