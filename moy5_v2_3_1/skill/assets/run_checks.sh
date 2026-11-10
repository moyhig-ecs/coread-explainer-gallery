#!/bin/sh
# run_checks.sh <dir> — the whole check run of the template: headings · claims · the action files · every action file in three frames (video 1920 x 1080 with ?video=1, desk, phone) · one capture.
# Needs the `anatomy` skill's scripts/drive.mjs (headless Chrome driver) and bun (or Node >= 20.10). A failing eval inside the page throws, drive.mjs exits non-zero, and so does this script.
cd "$(dirname "$0")" || exit 1
DIR=${1:-checks}; PY=${PY:-python3}; BUN=${BUN:-bun}; SK=${ANATOMY:-$HOME/.claude/skills/anatomy}
PAGE=${PAGE:-dist/synthetic.html}
fail=0
"$PY" -I list_headings.py | tail -1 || fail=1
"$PY" -I check_claims.py | head -1 || fail=1
"$PY" -I make_check.py "$DIR" > /dev/null || exit 1
drive() { out=$(mktemp); "$BUN" "$SK/scripts/drive.mjs" "$@" > "$out" 2>&1; code=$?; grep -E "measure_ok|chapters_ok|combos|^console|^exception|^error|^shot" "$out" | cut -c1-260; rm -f "$out"; [ $code -eq 0 ] || { echo "  -> drive exit $code"; fail=1; }; }
W=$(python3 -I -c "import json;c=json.load(open('config.json'))['frames'];print(c['video'][0],c['video'][1],c['desk'][0],c['desk'][1],c['phone'][0],c['phone'][1])")
set -- $W
for f in check_states check_robust check_chapters; do
  # the 1920 x 1080 frame hides the buttons (its chrome is not part of a still): the real clicks of check_chapters run on the desk and the phone only
  [ "$f" = check_chapters ] || { echo "== $f: video";  drive "file://$(pwd)/$PAGE?video=1" --actions "$DIR/$f.json" --width "$1" --height "$2"; }
  echo "== $f: desk";   drive "$PAGE" --actions "$DIR/$f.json" --width "$3" --height "$4"
  echo "== $f: phone";  drive "$PAGE" --actions "$DIR/$f.json" --width "$5" --height "$6"
done
mkdir -p captures
echo "== capture";  drive "file://$(pwd)/$PAGE?video=1" --actions "$DIR/check_capture.json" --width "$1" --height "$2"; drive "$PAGE" --actions "$DIR/check_desk_capture.json" --width "$3" --height "$4"
rm -rf __pycache__
exit $fail
