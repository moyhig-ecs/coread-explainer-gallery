"""summarize_checks.py — reads checks/run_checks.log and prints the numbers of the run (per section: states measured / failed, the smallest svg and html text px per frame, robust combos / errors,
chapter clicks, drag picks, name-scan hits and its positive control, console errors, drive exits). Writes checks/summary.json.
    python3 -I summarize_checks.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
log = (HERE / "checks" / "run_checks.log").read_text(encoding="utf-8").splitlines()
sec, out = None, {"sections": {}, "minpx": {}, "minhtml": {}, "console_errors": 0, "drive_fail": 0}
for line in log:
    if line.startswith("== "):
        sec = line[3:].strip(); out["sections"].setdefault(sec, {"ok": 0, "bad": 0}); continue
    if line.startswith("claims positive control"):
        out["claims_positive_control"] = line.strip(); continue
    if "axis labels clear of the blocks" in line: out["axis_labels_clear"] = out.get("axis_labels_clear", 0) + 1
    if line.startswith("headings") or line.startswith("anchors"):
        out[line.split()[0]] = line.strip(); continue
    m = re.search(r'"measure_ok":(true|false).*?"layout":"(\w+)".*?"minpx":([\d.]+|null),"htmlMin":([\d.]+|null)', line)
    if m:
        s = out["sections"][sec]; s["ok" if m.group(1) == "true" else "bad"] += 1
        lay = m.group(2)
        if m.group(3) != "null": out["minpx"][lay] = min(out["minpx"].get(lay, 99), float(m.group(3)))
        if m.group(4) != "null": out["minhtml"][lay] = min(out["minhtml"].get(lay, 99), float(m.group(4)))
    for key in ("combos", "chapters_ok", "drag_ok", "names_ok", "names_positive_control_ok", "nav_same"):
        if f'"{key}"' in line and sec:
            out["sections"][sec].setdefault("lines", []).append(line.replace("eval: ", "")[:160])
    if line.startswith("exception"):
        out["sections"][sec]["bad"] += 1
    m = re.match(r"console: (\d+) error", line)
    if m: out["console_errors"] += int(m.group(1))
    if "-> drive exit" in line: out["drive_fail"] += 1
    if line.startswith("internal words"): out["internal_words"] = int(line.split()[-1])
    if line.startswith("shot:"): out["shots"] = out.get("shots", 0) + 1
    if line.startswith("run_checks exit"): out["exit"] = int(line.split()[-1])
(HERE / "checks" / "summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
meas = [(k, v) for k, v in out["sections"].items() if k.startswith("check_states")]
print(f"states sections {len(meas)} · measured ok {sum(v['ok'] for _, v in meas)} · bad {sum(v['bad'] for _, v in meas)} · min svg px {out['minpx']} · min html px {out['minhtml']}")
print(f"console errors {out['console_errors']} · drive failures {out['drive_fail']} · internal words {out.get('internal_words')} · shots {out.get('shots', 0)} · exit {out.get('exit')}")
for k, v in out["sections"].items():
    if v.get("lines") and not k.startswith("check_states"):
        print(f"  {k}: " + " | ".join(v["lines"])[:300])
