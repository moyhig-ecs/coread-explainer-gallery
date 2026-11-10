#!/bin/sh
# run_jupyter_check.sh — JupyterLab, both directions + the kernel's recount (v2.1; adapted from station 2 v3.1's script, the waits replaced by `until` + re-run of a cell).
# Starts `jupyter lab` on 127.0.0.1 only (no token, its own config and runtime dirs under $SH_TMP), opens demo_jupyter.ipynb in headless Chrome (drive.mjs with bun), and ALWAYS stops the server it started:
# it signals only its own pid ($!) and then reports who still listens on its port. It never kills by pattern.
cd "$(dirname "$0")" || exit 1
PYD=${PYD:-$(dirname "$(command -v python3)")}; BUN=${BUN:-$(command -v bun)}; DRIVE=${DRIVE:-${ANATOMY:-$HOME/.claude/skills/anatomy}/scripts/drive.mjs}
T=${SH_TMP:-${TMPDIR:-/tmp}/moy5_jupyter_check}; PORT=${JUPYTER_PORT:-27980}; ACT=${ACT:-checks/check_jupyter.json}
mkdir -p "$T/runtime" "$T/config/labconfig" captures
# ggblab and webio-jupyterlab-provider break front-end -> kernel sync for any anywidget on this env; jupyterlab-myst throws on the first markdown cell. Switched off in this script's own config dir only.
echo '{"disabledExtensions": {"webio-jupyterlab-provider": true, "ggblab": true, "jupyterlab-myst": true}}' > "$T/config/labconfig/page_config.json"
cp demo_jupyter.ipynb "$T/demo_jupyter.clean.ipynb"
JUPYTER_CONFIG_DIR="$T/config" JUPYTER_RUNTIME_DIR="$T/runtime" "$PYD/jupyter-lab" --no-browser --ip=127.0.0.1 --port="$PORT" --IdentityProvider.token= --ServerApp.password= --ServerApp.root_dir="$(pwd)" --KernelManager.shell_port=$((PORT + 1)) --KernelManager.iopub_port=$((PORT + 2)) --KernelManager.stdin_port=$((PORT + 3)) --KernelManager.control_port=$((PORT + 4)) --KernelManager.hb_port=$((PORT + 5)) --expose-app-in-browser > "$T/jupyter.log" 2>&1 &
PID=$!
stop() {
  kill "$PID" 2>/dev/null
  n=0; while kill -0 "$PID" 2>/dev/null && [ $n -lt 60 ]; do sleep 0.2; n=$((n + 1)); done
  echo "own pid $PID still alive after stop: $(kill -0 "$PID" 2>/dev/null && echo yes || echo no)"
  echo "listeners on port $PORT after stop: [$(lsof -ti "tcp:$PORT" 2>/dev/null | tr '\n' ' ')]"
  cp "$T/demo_jupyter.clean.ipynb" demo_jupyter.ipynb; rm -rf .ipynb_checkpoints
  echo "demo_jupyter.ipynb restored (clean copy) and .ipynb_checkpoints removed"
}
trap stop EXIT
i=0; until curl -s -o /dev/null "http://127.0.0.1:$PORT/api"; do i=$((i + 1)); [ $i -gt 150 ] && { echo "jupyter did not start"; cat "$T/jupyter.log"; exit 1; }; sleep 0.4; done
START=$(date +%s)
"$BUN" "$DRIVE" "http://127.0.0.1:$PORT/lab/tree/demo_jupyter.ipynb" --actions "$ACT" --width 1440 --height 2300
CODE=$?
echo "drive exit $CODE · wall $(( $(date +%s) - START )) s"
grep -i -E "error|traceback|exception" "$T/jupyter.log" | head -10
exit $CODE
