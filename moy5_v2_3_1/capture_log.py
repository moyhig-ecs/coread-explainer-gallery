"""capture_log.py — writes captures/capture.log: every still with its pixel size and md5, and checks that the video stills are exactly 1920 x 1080 and that every state has its stills.
    python -I capture_log.py        (exit 1 if a still is missing or a video still is not 1920 x 1080)
"""
import hashlib
import json
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CAP = HERE / "captures"
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
NS = cfg["chapters"][-1][2] + 1
# v2.1 (BRIEF v2.1 §2-10): the stills are the video 1920 x 1080 in ja and en (+ state 0 with P_x moved) and the two widget checks; desk / phone are checked, not captured
want = [f"video_s{i}.png" for i in range(NS)] + ["video_s0a.png", "video_s0b.png"] + [f"video_s{i}_en.png" for i in range(NS)] + ["marimo_s10.png", "jupyterlab_s18.png"]
bad, lines = [], []
for f in sorted(CAP.glob("*.png")):
    w, h = Image.open(f).size
    if f.name.startswith("video_") and (w, h) != (1920, 1080):
        bad.append(f"{f.name}: {w} x {h}")
    lines.append(f"{f.name}\t{w} x {h}\t{hashlib.md5(f.read_bytes()).hexdigest()}")
missing = [n for n in want if not (CAP / n).exists()]
head = [f"# captures — {len(lines)} stills ({sum(1 for l in lines if l.startswith('video_'))} video 1920 x 1080 · {sum(1 for l in lines if l.startswith('page_dark'))} desk dark (ja {NS} + en 5) · {sum(1 for l in lines if l.startswith('page_light'))} desk light · {sum(1 for l in lines if l.startswith('phone_'))} phone dark · other {sum(1 for l in lines if not l.startswith(('video_', 'page_', 'phone_')))})",
        f"# expected {len(want)} · missing {len(missing)} · video not 1920 x 1080: {len(bad)}", "# file\tpixels\tmd5"]
(CAP / "capture.log").write_text("\n".join(head + lines) + "\n", encoding="utf-8")
print(head[0]); print(head[1])
for m in missing + bad:
    print("  !!", m)
sys.exit(1 if missing or bad else 0)
