#!/bin/sh
# run_checks.sh [dir] — the whole check run of the moy-1 entry; writes <dir>/last_run.txt (what ran, what it said).
#   build · headings · claims (anchors) · CLAIMS.md / SCRIPT regenerated · states (video / desk / phone x ja / en) · robust · chapters (real clicks) · the word scan · marimo · JupyterLab
# Needs the `anatomy` skill's scripts/drive.mjs (headless Chrome driver) and bun. A failing eval inside the page throws, drive.mjs exits non-zero, and this script reports it.
cd "$(dirname "$0")" || exit 1
DIR=${1:-checks}; PY=${PY:-$(command -v python3)}; BUN=${BUN:-$(command -v bun)}; SK=${ANATOMY:-$HOME/.claude/skills/anatomy}
LOG="$DIR/last_run.txt"; mkdir -p "$DIR"; WIDGETS_ONLY=${WIDGETS_ONLY:-0}; [ "$WIDGETS_ONLY" = 1 ] || : > "$LOG"; fail=0
say() { echo "$*" | tee -a "$LOG"; }
# marimo and JupyterLab (their scripts read PY as the *directory* of the python env, run_checks.sh reads it as the python binary: the dirname below keeps them apart; an exported binary path made both steps fail silently in the first runs of v2): each runs on its own port (MARIMO_PORT / JUPYTER_PORT; the defaults of the two scripts can be held by another job that runs the same scripts), the exit code of the script counts, and error lines are shown (v1's pipe hid both).
widgets() {
  echo "== marimo (both directions)" | tee -a "$LOG"; mo=$(mktemp); PY="$(dirname "$PY")" PORT=${MARIMO_PORT:-27481} sh run_marimo_check.sh > "$mo" 2>&1; mc=$?
  grep -E "console|drive exit|kernel and figure agree|equal|listeners|own pid|^error|did not start|Error" "$mo" | cut -c1-300 | tee -a "$LOG"; rm -f "$mo"; [ $mc -eq 0 ] || { echo "  -> marimo check exit $mc" | tee -a "$LOG"; fail=1; }
  echo "== JupyterLab (both directions)" | tee -a "$LOG"; jo=$(mktemp); PY="$(dirname "$PY")" PORT=${JUPYTER_PORT:-27483} sh run_jupyter_check.sh > "$jo" 2>&1; jc=$?
  grep -E "console|drive exit|equal|listeners|own pid|restored|^error|did not start|Error" "$jo" | cut -c1-300 | tee -a "$LOG"; rm -f "$jo"; [ $jc -eq 0 ] || { echo "  -> JupyterLab check exit $jc" | tee -a "$LOG"; fail=1; }
}
if [ "$WIDGETS_ONLY" = 1 ]; then          # re-run of the two widget steps only (appends to the log of the whole run)
  say "== widgets only re-run · $(date '+%Y-%m-%d %H:%M:%S')"; widgets; rm -rf __pycache__; say "run_checks.sh (widgets only) done · exit $fail"; exit $fail
fi
say "run_checks.sh · $(date '+%Y-%m-%d %H:%M:%S') · bun $("$BUN" --version) · $($PY --version)"
PY="$PY" "$BUN" build.mjs 2>&1 | tail -1 | tee -a "$LOG"
say "pages md5: $(cd pages && md5 -q moy1.html | cut -c1-8) moy1 · $(cd pages && md5 -q moy1-en.html | cut -c1-8) moy1-en · $(cd pages && md5 -q widget.js | cut -c1-8) widget.js"
"$PY" -I list_headings.py | tail -1 | tee -a "$LOG" || fail=1
"$PY" -I make_claims.py | tee -a "$LOG"
"$PY" -I check_claims.py | head -1 | tee -a "$LOG" || fail=1
"$PY" -I make_script.py | tee -a "$LOG"
"$PY" -I check_fence.py | tee -a "$LOG" || fail=1
"$PY" -I make_check.py "$DIR" > /dev/null || exit 1
W=$("$PY" -I -c "import json;c=json.load(open('config.json'))['frames'];print(c['video'][0],c['video'][1],c['desk'][0],c['desk'][1],c['phone'][0],c['phone'][1])")
set -- $W
drive() { out=$(mktemp); "$BUN" "$SK/scripts/drive.mjs" "$@" > "$out" 2>&1; code=$?; n=$(grep -c 'measure_ok[^:]*:true' "$out"); [ "$n" -gt 0 ] && echo "  measure_ok x $n" | tee -a "$LOG"; grep -E "chapters_ok|combos|words_ok|parity_ok|sae_ok|v21_ok|v3_ok|^eval: \"click: |orbit: the|key: |slider: |^console|^error" "$out" | cut -c1-300 | tee -a "$LOG"; rm -f "$out"; [ $code -eq 0 ] || { echo "  -> drive exit $code" | tee -a "$LOG"; fail=1; }; }
for f in check_states check_states_en check_robust; do
  echo "== $f: video" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html?video=1" --actions "$DIR/$f.json" --width "$1" --height "$2"
  echo "== $f: desk" | tee -a "$LOG";  drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/$f.json" --width "$3" --height "$4"
  echo "== $f: phone" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/$f.json" --width "$5" --height "$6"
done
echo "== the four pages (dark / light x ja / en), desk" | tee -a "$LOG"
for pg in moy1-light moy1-en moy1-light-en; do echo "-- $pg" | tee -a "$LOG"; drive "file://$(pwd)/pages/$pg.html" --actions "$DIR/check_states.json" --width "$3" --height "$4"; done
echo "== reduced motion (prefers-reduced-motion: reduce), desk" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_states.json" --width "$3" --height "$4" --reduced
echo "== check_parity (ja / en numbers) and check_interaction (drag, keys, slider)" | tee -a "$LOG"
drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_parity.json" --width "$3" --height "$4"
drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_interaction.json" --width "$3" --height "$4"
echo "== check_sae (v2: the inset lights where a predicate hits · keys / slider · the aggregate · the two labels of cmt5's bind in every state)" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_sae.json" --width "$3" --height "$4"
echo "== check_v21 (v2.1: olm62's two states · the card marks of every state in ja / en · the map)" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_v21.json" --width "$3" --height "$4"
echo "== check_v3 (v3: the part added after the 10-28 figure · the slope state · the ledger states of the added part) — desk and phone" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_v3.json" --width "$3" --height "$4"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_v3.json" --width "$5" --height "$6"
for fr in "desk $3 $4" "phone $5 $6"; do set -- $fr $W; echo "== check_cards: $1 (a real click on a card mark opens the map)" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_cards.json" --width "$2" --height "$3"; done
set -- $W
for fr in "desk $3 $4" "phone $5 $6"; do set -- $fr $W; echo "== check_chapters: $1" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_chapters.json" --width "$2" --height "$3"; done
set -- $W
echo "== check_words" | tee -a "$LOG"; drive "file://$(pwd)/pages/moy1.html" --actions "$DIR/check_words.json" --width "$3" --height "$4"
widgets
rm -rf __pycache__
say "run_checks.sh done · exit $fail"
exit $fail
