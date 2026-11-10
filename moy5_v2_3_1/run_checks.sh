#!/bin/sh
# run_checks.sh [capture | capture22 | capture23] — (v2.3 adds check_v23 in every frame, the v2.2 comparison when BASE22 is set, and `capture23` = the stills with the plane) — the whole check run (v2.1; v2.2 adds check_v22 / check_v22_click and `capture22` = the board states only): build · headings · claims (+ calibration) · the action files · every check in three frames (video 1920 x 1080 with ?video=1, desk, phone)
#   and both themes / languages where it matters · the v2.1 checks (grade columns, pills, bundle ①, the 1080 last line with its positive control) · marimo · JupyterLab · captures when "capture" is given.
# Writes checks/last_run.txt. A failing eval inside the page throws, drive.mjs exits non-zero, and so does this script.
#   WIDGETS_ONLY=1 sh run_checks.sh   re-runs only the marimo and JupyterLab stages (appends to the log).
# Tools (env): PY = the python BINARY (default: the py314 env) · BUN (bun >= 1.3) · DRIVE = drive.mjs (default: the anatomy skill's; a copy whose Chrome port is fixed by DRIVE_PORT may be given)
#   DRIVE_PORT / DRIVE_TMP are read by such a copy only. The widget scripts take PYD = the env's bin DIRECTORY (derived here; v1 of station 2 mixed the two and hid two failing stages).
cd "$(dirname "$0")" || exit 1
DIR=checks; PY=${PY:-$(command -v python3)}; BUN=${BUN:-$(command -v bun)}; SK=${ANATOMY:-$HOME/.claude/skills/anatomy}; DRIVE=${DRIVE:-$SK/scripts/drive.mjs}
export BUN DRIVE; PYD=$(dirname "$PY"); export PYD
LOG="$DIR/last_run.txt"; mkdir -p "$DIR"; fail=0
say() { echo "$*" | tee -a "$LOG"; }
widgets() {
  say "== marimo (both directions + kernel recount)"; mo=$(mktemp); sh run_marimo_check.sh > "$mo" 2>&1; mc=$?
  grep -E "ok|^console|drive exit|listeners|own pid|^error|did not start|Error|until" "$mo" | sed -E 's/\\"/"/g' | cut -c1-300 | tee -a "$LOG"; rm -f "$mo"; [ $mc -eq 0 ] || { say "  -> marimo check exit $mc"; fail=1; }
  say "== JupyterLab (both directions + kernel recount)"; jo=$(mktemp); sh run_jupyter_check.sh > "$jo" 2>&1; jc=$?
  grep -E "ok|^console|drive exit|listeners|own pid|restored|^error|did not start|Error|until" "$jo" | sed -E 's/\\"/"/g' | cut -c1-300 | tee -a "$LOG"; rm -f "$jo"; [ $jc -eq 0 ] || { say "  -> JupyterLab check exit $jc"; fail=1; }
}
if [ "${WIDGETS_ONLY:-0}" = 1 ]; then
  say "== widgets only re-run · $(date '+%Y-%m-%d %H:%M:%S')"; widgets; rm -rf __pycache__; say "run_checks (widgets only): $( [ $fail -eq 0 ] && echo PASS || echo FAIL )"; exit $fail
fi
: > "$LOG"
say "run_checks.sh · $(date '+%Y-%m-%d %H:%M:%S') · bun $("$BUN" --version) · $("$PY" --version) · drive $DRIVE"
PY="$PY" "$BUN" build.mjs 2>&1 | tail -1 | tee -a "$LOG"
say "pages md5: $(md5 -q dist/moy5_route.html | cut -c1-8) ja · $(md5 -q dist/moy5_route-en.html | cut -c1-8) en · $(md5 -q dist/widget.js | cut -c1-8) widget.js"
"$PY" -I list_headings.py | tail -1 | tee -a "$LOG" || fail=1
"$PY" -I check_claims.py | head -1 | tee -a "$LOG"; "$PY" -I check_claims.py > /dev/null || fail=1
"$PY" -I check_claims.py --calibrate | tee -a "$LOG" || fail=1
"$PY" -I make_script.py | tee -a "$LOG" || fail=1
"$PY" -I make_check.py "$DIR" > /dev/null || exit 1
drive() { out=$(mktemp); "$BUN" "$DRIVE" "$@" > "$out" 2>&1; code=$?; n=$(grep -c 'measure_ok[^:]*:true' "$out"); [ "$n" -gt 0 ] && say "  measure_ok x $n"; n2=$(grep -c 'v22_ok[^:]*:true' "$out"); [ "$n2" -gt 0 ] && say "  v22_ok x $n2"; n3=$(grep -c 'v23_ok[^:]*:true' "$out"); [ "$n3" -gt 0 ] && say "  v23_ok x $n3"; grep -E "chapters_ok|combos|pagevraw|scan|pages|v21_ok|v22_text|v22_click|v22_hidden|geom_ok|geom23_ok|v23: |fit_|^console|^exception|^error" "$out" | sed -E 's/\\"/"/g' | cut -c1-300 | tee -a "$LOG"; rm -f "$out"; [ $code -eq 0 ] || { say "  -> drive exit $code"; fail=1; }; }
P=dist/moy5_route.html
for f in check_states check_robust; do
  for pg in moy5_route moy5_route-en; do
    say "== $f · $pg · video";  drive "file://$(pwd)/dist/$pg.html?video=1" --actions "$DIR/$f.json" --width 1920 --height 1080
    say "== $f · $pg · desk";   drive "dist/$pg.html" --actions "$DIR/$f.json" --width 1440 --height 1800
    say "== $f · $pg · phone";  drive "dist/$pg.html" --actions "$DIR/$f.json" --width 390 --height 3000
  done
done
say "== check_states · light · desk"; drive "dist/moy5_route-light.html" --actions "$DIR/check_states.json" --width 1440 --height 1800
say "== check_states · reduced motion · desk"; drive "$P" --actions "$DIR/check_states.json" --width 1440 --height 1800 --reduced
for pg in moy5_route moy5_route-en moy5_route-light; do say "== check_chapters · $pg · desk"; drive "dist/$pg.html" --actions "$DIR/check_chapters.json" --width 1440 --height 1800; done
say "== check_chapters · phone"; drive "$P" --actions "$DIR/check_chapters.json" --width 390 --height 3000
say "== check_scan · desk"; drive "$P" --actions "$DIR/check_scan.json" --width 1440 --height 1800
say "== check_scan · phone"; drive "$P" --actions "$DIR/check_scan.json" --width 390 --height 3000
say "== check_pagevraw · desk"; drive "$P" --actions "$DIR/check_pagevraw.json" --width 1440 --height 1800
say "== check_v21 (grade columns · pills · bundle ① · road others) · desk"; drive "$P" --actions "$DIR/check_v21.json" --width 1440 --height 1800
say "== check_v21 · video"; drive "file://$(pwd)/$P?video=1" --actions "$DIR/check_v21.json" --width 1920 --height 1080
say "== check_fit_control (the 1080 last line: OFF must be caught, ON must pass) · video ja / en"
drive "file://$(pwd)/$P?video=1" --actions "$DIR/check_fit_control.json" --width 1920 --height 1080
drive "file://$(pwd)/dist/moy5_route-en.html?video=1" --actions "$DIR/check_fit_control.json" --width 1920 --height 1080
# v2.2 (BRIEF v2.2 §2-4): the overlay on the board states 0 and 7, on and off: MEASURE (the 1080 frame and its last line on video) · texts unchanged by the toggle · geometry of §1 · real clicks on the button
say "== check_v22 (overlay on / off · 1080 frame · last line · texts unchanged · geometry) · video ja"; drive "file://$(pwd)/$P?video=1" --actions "$DIR/check_v22.json" --width 1920 --height 1080
say "== check_v22 · video en"; drive "file://$(pwd)/dist/moy5_route-en.html?video=1" --actions "$DIR/check_v22.json" --width 1920 --height 1080
say "== check_v22 · desk"; drive "$P" --actions "$DIR/check_v22.json" --width 1440 --height 1800
say "== check_v22 · light · desk"; drive "dist/moy5_route-light.html" --actions "$DIR/check_v22.json" --width 1440 --height 1800
say "== check_v22 · phone"; drive "$P" --actions "$DIR/check_v22.json" --width 390 --height 3000
say "== check_v22_click (real clicks on the button) · desk"; drive "$P" --actions "$DIR/check_v22_click.json" --width 1440 --height 1800
say "== check_v22_click · phone"; drive "dist/moy5_route-en.html" --actions "$DIR/check_v22_click.json" --width 390 --height 3000
# v2.3 (BRIEF v2.3 §2-2 / §2-3): the cutting plane — its numbers on the page against BRIEF v2.3 §1 and the pack (+ planted faults), what is drawn (parts · painter's order · parabola inside the plane ·
#   the directrix · names · no overlapping texts · no key line under a corner), overlay on / off, in every frame; and (when BASE22 = a built v2.2 entry is given) no other page changed
for pg in moy5_route moy5_route-en; do
  say "== check_v23 (the cutting plane) · $pg · video"; drive "file://$(pwd)/dist/$pg.html?video=1" --actions "$DIR/check_v23.json" --width 1920 --height 1080
  say "== check_v23 · $pg · desk"; drive "dist/$pg.html" --actions "$DIR/check_v23.json" --width 1440 --height 1800
  say "== check_v23 · $pg · phone"; drive "dist/$pg.html" --actions "$DIR/check_v23.json" --width 390 --height 3000
done
say "== check_v23 · light · desk"; drive "dist/moy5_route-light.html" --actions "$DIR/check_v23.json" --width 1440 --height 1800
if [ -n "${BASE22:-}" ]; then
  for pg in moy5_route moy5_route-en; do for fr in video desk phone; do
    case $fr in video) W=1920; H=1080; Q="?video=1";; desk) W=1440; H=1800; Q="";; phone) W=390; H=3000; Q="";; esac
    a=$(mktemp); b=$(mktemp)
    "$BUN" "$DRIVE" "file://$BASE22/dist/$pg.html$Q" --actions "$DIR/check_v23_dump.json" --width $W --height $H > "$a" 2>&1
    "$BUN" "$DRIVE" "file://$(pwd)/dist/$pg.html$Q" --actions "$DIR/check_v23_dump.json" --width $W --height $H > "$b" 2>&1
    c=$(mktemp); "$PY" -I compare_v22.py "$a" "$b" "$pg · $fr" > "$c"; cc=$?; cat "$c" | tee -a "$LOG"; [ $cc -eq 0 ] || fail=1; rm -f "$a" "$b" "$c"
  done; done
fi
widgets
if [ "$1" = capture23 ]; then
  mkdir -p captures
  say "== capture v2.3 (the board states with the plane) · video ja"; drive "file://$(pwd)/$P?video=1" --actions "$DIR/check_capture_v23.json" --width 1920 --height 1080
  say "== capture v2.3 · video en"; drive "file://$(pwd)/dist/moy5_route-en.html?video=1" --actions "$DIR/check_capture_v23_en.json" --width 1920 --height 1080
fi
if [ "$1" = capture22 ]; then
  mkdir -p captures
  say "== capture v2.2 (board states only) · video ja"; drive "file://$(pwd)/$P?video=1" --actions "$DIR/check_capture_v22.json" --width 1920 --height 1080
  say "== capture v2.2 (board states only) · video en"; drive "file://$(pwd)/dist/moy5_route-en.html?video=1" --actions "$DIR/check_capture_v22_en.json" --width 1920 --height 1080
fi
if [ "$1" = capture ]; then
  mkdir -p captures
  say "== capture · video ja"; drive "file://$(pwd)/$P?video=1" --actions "$DIR/check_capture_video.json" --width 1920 --height 1080
  say "== capture · video en"; drive "file://$(pwd)/dist/moy5_route-en.html?video=1" --actions "$DIR/check_capture_video_en.json" --width 1920 --height 1080
fi
rm -rf __pycache__
say "run_checks: $( [ $fail -eq 0 ] && echo PASS || echo FAIL )"
exit $fail
