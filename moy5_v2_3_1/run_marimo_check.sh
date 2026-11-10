#!/bin/sh
# run_marimo_check.sh — marimo, both directions + the kernel's recount (v2.1). Starts `marimo run demo_marimo.py` on 127.0.0.1 only, drives it in headless Chrome, ALWAYS stops the server it started
# (its own pid only; then reports who still listens on its port; never kills by pattern).
cd "$(dirname "$0")" || exit 1
PYD=${PYD:-$(dirname "$(command -v python3)")}; BUN=${BUN:-$(command -v bun)}; DRIVE=${DRIVE:-${ANATOMY:-$HOME/.claude/skills/anatomy}/scripts/drive.mjs}
PORT=${MARIMO_PORT:-27990}; T=${SH_TMP:-${TMPDIR:-/tmp}/moy5_marimo_check}; ACT=${ACT:-checks/check_marimo.json}
mkdir -p "$T" captures
"$PYD/marimo" run demo_marimo.py --headless --no-token --host 127.0.0.1 --port "$PORT" > "$T/marimo.log" 2>&1 &
PID=$!
stop() {
  kill "$PID" 2>/dev/null
  n=0; while kill -0 "$PID" 2>/dev/null && [ $n -lt 60 ]; do sleep 0.2; n=$((n + 1)); done
  echo "own pid $PID still alive after stop: $(kill -0 "$PID" 2>/dev/null && echo yes || echo no)"
  echo "listeners on port $PORT after stop: [$(lsof -ti "tcp:$PORT" 2>/dev/null | tr '\n' ' ')]"
}
trap stop EXIT
i=0; until curl -s -o /dev/null "http://127.0.0.1:$PORT/"; do i=$((i + 1)); [ $i -gt 150 ] && { echo "marimo did not start"; cat "$T/marimo.log"; exit 1; }; sleep 0.4; done
START=$(date +%s)
"$BUN" "$DRIVE" "http://127.0.0.1:$PORT/" --actions "$ACT" --width 1440 --height 1800
CODE=$?
echo "drive exit $CODE · wall $(( $(date +%s) - START )) s"
grep -i -E "error|traceback|exception" "$T/marimo.log" | head -10
exit $CODE
