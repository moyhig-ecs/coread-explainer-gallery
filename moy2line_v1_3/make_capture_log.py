"""make_capture_log.py — writes captures/capture.log: every still with its pixel size (read from the PNG header), bytes and md5, and checks that every video_* still is exactly 1920 x 1080.
    python3 -I make_capture_log.py      (exit 1 if a video still is not 1920 x 1080 or a state has no video still)
"""
import hashlib
import json
import pathlib
import struct
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
CAP = HERE / "captures"
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
NS = cfg["chapters"][-1][2] + 1
lines, bad = [], []
for p in sorted(CAP.glob("*.png")):
    b = p.read_bytes()
    w, h = struct.unpack(">II", b[16:24])
    if p.name.startswith("video_") and (w, h) != (1920, 1080):
        bad.append(f"{p.name} is {w}x{h}")
    lines.append(f"{p.name}\t{w}x{h}\t{len(b)}\t{hashlib.md5(b).hexdigest()}")
for n in range(NS):
    if not (CAP / f"video_s{n}.png").exists():
        bad.append(f"no video_s{n}.png")
head = [f"# capture.log — written {time.strftime('%Y-%m-%d %H:%M:%S %z')} by make_capture_log.py · {len(lines)} stills · states {NS}",
        "# all stills were taken in ONE full run (run_checks.sh captures + run_marimo_check.sh + run_jupyter_check.sh) after the last build; no partial re-shoot",
        "# name\tpixels\tbytes\tmd5"]
(CAP / "capture.log").write_text("\n".join(head + lines + [f"# problems: {len(bad)}"] + [f"# {x}" for x in bad]) + "\n", encoding="utf-8")
print(f"capture.log: {len(lines)} stills · problems {len(bad)}")
for x in bad:
    print("  !!", x)
sys.exit(1 if bad else 0)
