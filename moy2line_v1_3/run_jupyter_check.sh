#!/bin/sh
# run_jupyter_check.sh — starts `jupyter lab` on 127.0.0.1:27541 only (inside this maker's band; no token; its own config and runtime dirs under checks/jupyter/), opens demo_jupyter.ipynb
# in headless Chrome (drive.mjs), runs the cells, checks both directions (kernel -> figure, figure -> kernel) and stops ONLY the server it started (its recorded PID; never by name or pattern).
# This machine's env has two JupyterLab extensions that are known to break front-end -> kernel sync for any anywidget (ggblab, webio-jupyterlab-provider): they are switched off
# for this run only, in this script's own throwaway config dir (nothing is installed or removed; the user's config is not touched).
cd "$(dirname "$0")" || exit 1
PY=${PY:-$(dirname "$(command -v python3)")}; BUN=${BUN:-bun}; PORT=${PORT:-27541}
T="$PWD/checks/jupyter"; mkdir -p "$T/runtime" "$T/config/labconfig" captures
echo '{"disabledExtensions": {"webio-jupyterlab-provider": true, "ggblab": true, "jupyterlab-myst": true}}' > "$T/config/labconfig/page_config.json"
cp demo_jupyter.ipynb "$T/demo_jupyter.clean.ipynb"
JUPYTER_CONFIG_DIR="$T/config" JUPYTER_RUNTIME_DIR="$T/runtime" "$PY/jupyter-lab" --no-browser --ip=127.0.0.1 --port="$PORT" --IdentityProvider.token= --ServerApp.password= --ServerApp.root_dir="$PWD" --expose-app-in-browser --LabApp.news_url= --LabApp.check_for_updates_class=jupyterlab.NeverCheckForUpdate > "$T/jupyter.log" 2>&1 &
PID=$!
echo "jupyter pid $PID (port $PORT)"
stop() {
  kill "$PID" 2>/dev/null
  n=0; while kill -0 "$PID" 2>/dev/null && [ $n -lt 60 ]; do sleep 0.25; n=$((n + 1)); done
  kill -0 "$PID" 2>/dev/null && echo "jupyter pid $PID still alive" || echo "jupyter pid $PID stopped"
  cp "$T/demo_jupyter.clean.ipynb" demo_jupyter.ipynb; rm -rf .ipynb_checkpoints
  echo "demo_jupyter.ipynb restored (clean copy) and .ipynb_checkpoints removed"
}
trap stop EXIT
i=0; until curl -s -o /dev/null "http://127.0.0.1:$PORT/api"; do i=$((i + 1)); [ $i -gt 150 ] && { echo "jupyter did not start"; tail -20 "$T/jupyter.log"; exit 1; }; sleep 0.4; done
"$PY/python" -I make_jupyter_check.py > /dev/null
"$BUN" drive.mjs "http://127.0.0.1:$PORT/lab/tree/demo_jupyter.ipynb" --actions checks/check_jupyter.json --width 1440 --height 2300
CODE=$?
echo "drive exit $CODE"
grep -i -E "traceback|exception" "$T/jupyter.log" | head -5
exit $CODE
