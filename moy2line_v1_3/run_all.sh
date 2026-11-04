#!/bin/sh
# run_all.sh — the final run of this entry, in one go after the last build: build · every check · every still · marimo · JupyterLab · capture.log · summary. Logs in checks/.
cd "$(dirname "$0")" || exit 1
PY=${PY:-python3}
rm -f captures/*.png captures/capture.log
PY="$PY" bun build.mjs > checks/build.log 2>&1 || { echo "build failed"; exit 1; }
"$PY" -I make_script.py > checks/script.log 2>&1
sh run_checks.sh all > checks/run_checks.log 2>&1; c1=$?; echo "run_checks exit $c1" >> checks/run_checks.log
sh run_marimo_check.sh > checks/run_marimo.log 2>&1; c2=$?
sh run_jupyter_check.sh > checks/run_jupyter.log 2>&1; c3=$?
"$PY" -I make_capture_log.py > checks/capture_log.log 2>&1; c4=$?
"$PY" -I summarize_checks.py > checks/summary.log 2>&1
rm -rf __pycache__
echo "run_all: checks $c1 · marimo $c2 · jupyter $c3 · capture log $c4"
exit $((c1 + c2 + c3 + c4))
