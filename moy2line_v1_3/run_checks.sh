#!/bin/sh
# run_checks.sh [checks|captures|all] — the check run of this entry: headings · claims · the action files · each check in the frames (video 1920 x 1080 with ?video=1, desk 1440, phone 390) · the stills.
# Chrome is driven by drive.mjs (this entry's DevTools driver; port 27511 inside this maker's band 27500–27599; its profile lives in .chrome/ and is removed after each run).
# A failing eval inside the page throws, drive.mjs exits non-zero, and so does this script. Output lines are kept in checks/run_<what>.log.
cd "$(dirname "$0")" || exit 1
WHAT=${1:-all}; PY=${PY:-python3}; BUN=${BUN:-bun}
fail=0
mkdir -p checks captures
drive() { out=$(mktemp "$PWD/.chrome/out.XXXXXX"); "$BUN" drive.mjs "$@" > "$out" 2>&1; code=$?; grep -E "measure_ok|chapters_ok|combos|drag_ok|names_ok|names_positive|nav_same|^console|^exception|^error|^shot" "$out" | cut -c1-300; rm -f "$out"; [ $code -eq 0 ] || { echo "  -> drive exit $code"; fail=1; }; }
mkdir -p .chrome
if [ "$WHAT" = checks ] || [ "$WHAT" = all ]; then
  "$PY" -I list_headings.py | tail -1 || fail=1
  "$PY" -I check_claims.py | head -1; "$PY" -I check_claims.py > /dev/null || fail=1
  "$PY" -I make_anchors_broken.py > /dev/null || fail=1; pc=$("$PY" -I check_claims.py --anchors checks/anchors_broken.json | head -1); echo "claims positive control (12 broken on purpose): $pc"; echo "$pc" | grep -q "missing or different: 12$" || fail=1
  "$PY" -I make_check.py checks > /dev/null || exit 1
  for P in dist/moy2line.html dist/moy2line-en.html dist/moy2line-light.html dist/moy2line-light-en.html; do
    echo "== check_states: video $P"; drive "$P?video=1" --actions checks/check_states.json --width 1920 --height 1080
    echo "== check_states: desk $P";  drive "$P" --actions checks/check_states.json --width 1440 --height 1800
    echo "== check_states: phone $P"; drive "$P" --actions checks/check_states.json --width 390 --height 3200
  done
  echo "== check_states: reduced motion (desk)"; drive dist/moy2line.html --actions checks/check_states.json --width 1440 --height 1800 --reduced
  for P in dist/moy2line.html dist/moy2line-en.html; do
    echo "== check_robust: $P"; drive "$P" --actions checks/check_robust.json --width 1440 --height 1800
    echo "== check_chapters: desk $P"; drive "$P" --actions checks/check_chapters.json --width 1440 --height 1800
    echo "== check_chapters: phone $P"; drive "$P" --actions checks/check_chapters.json --width 390 --height 3200
    echo "== check_drag: desk $P"; drive "$P" --actions checks/check_drag.json --width 1440 --height 1800
    echo "== check_drag: video $P"; drive "$P?video=1" --actions checks/check_drag.json --width 1920 --height 1080
    echo "== check_names: $P"; drive "$P" --actions checks/check_names.json --width 1440 --height 1800
  done
  echo "== public fence: internal words in the body files (expect 0)"; n=$(grep -c -E "${FENCE_WORDS:-@@fence-words-not-set@@}" figure.js i18n.js state_machine.js figure.css build.mjs art.mjs | awk -F: '{s+=$2} END {print s}'); echo "internal words: $n"; [ "$n" -eq 0 ] || fail=1
fi
if [ "$WHAT" = captures ] || [ "$WHAT" = all ]; then
  "$PY" -I make_check.py checks > /dev/null || exit 1
  echo "== capture: video";      drive "dist/moy2line.html?video=1" --actions checks/capture_video.json --width 1920 --height 1080
  echo "== capture: video en";   drive "dist/moy2line-en.html?video=1" --actions checks/capture_video_en.json --width 1920 --height 1080
  echo "== capture: desk dark";  drive dist/moy2line.html --actions checks/capture_desk_dark.json --width 1440 --height 1800
  echo "== capture: desk light"; drive dist/moy2line-light.html --actions checks/capture_desk_light.json --width 1440 --height 1800
  echo "== capture: desk en";    drive dist/moy2line-en.html --actions checks/capture_desk_en.json --width 1440 --height 1800
  echo "== capture: phone";      drive dist/moy2line.html --actions checks/capture_phone.json --width 390 --height 3200
fi
rm -rf __pycache__
exit $fail
