#!/bin/sh
# run_marimo_check.sh — starts `marimo run demo_marimo.py` on 127.0.0.1:27531 (inside this maker's band; headless, no token), drives it with drive.mjs (both directions + three stills),
# and stops ONLY the server it started (its recorded PID; never by name or pattern).
cd "$(dirname "$0")" || exit 1
PY=${PY:-$(dirname "$(command -v python3)")}; BUN=${BUN:-bun}; PORT=${PORT:-27531}
mkdir -p checks captures
MARIMO_SKIP_UPDATE_CHECK=1 "$PY/marimo" run demo_marimo.py --headless --no-token --port "$PORT" --host 127.0.0.1 > checks/marimo.log 2>&1 &
PID=$!
echo "marimo pid $PID (port $PORT)"
stop() { kill "$PID" 2>/dev/null; n=0; while kill -0 "$PID" 2>/dev/null && [ $n -lt 60 ]; do sleep 0.25; n=$((n + 1)); done; kill -0 "$PID" 2>/dev/null && echo "marimo pid $PID still alive" || echo "marimo pid $PID stopped"; }
trap stop EXIT
i=0; until curl -s -o /dev/null "http://127.0.0.1:$PORT/"; do i=$((i + 1)); [ $i -gt 150 ] && { echo "marimo did not start"; tail -20 checks/marimo.log; exit 1; }; sleep 0.4; done
"$PY/python" -I make_marimo_check.py > /dev/null
"$BUN" drive.mjs "http://127.0.0.1:$PORT/" --actions checks/check_marimo.json --width 1440 --height 1400
CODE=$?
echo "drive exit $CODE"
exit $CODE
