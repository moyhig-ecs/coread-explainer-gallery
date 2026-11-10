"""make_check.py — writes the action files that drive headless Chrome (the `anatomy` skill's scripts/drive.mjs) (template: the skeleton of the checks).
  check_states.json    every state: goto, wait, MEASURE  (a failing eval throws: drive.mjs exits non-zero; its own `console:` line reports console errors)
  check_robust.json    every state x a few positions x both languages in one page: any throw fails
  check_chapters.json  REAL clicks on the chapter buttons (not api calls): the state they land on, the chapter, the pressed button, the hash, the grouping of the numbered steps
  check_capture.json   one 1920 x 1080 frame of a state (the `video_` stills) and one desk frame
MEASURE = the smallest text on the plate in px on screen (font-size x the plate's scale) against config.json "minpx" for this frame, any text outside the viewBox, NaN in a path.
Usage:   python3 -I make_check.py <dir> [<capture state>]      then   sh run_checks.sh <dir>
Every number the checks need (states, groups, thresholds) comes from config.json: the numbers of the states exist in one place.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "checks").resolve()
OUT.mkdir(parents=True, exist_ok=True)
CAP_STATE = int(sys.argv[2]) if len(sys.argv) > 2 else 1
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
CH, MINPX = cfg["chapters"], cfg["minpx"]
NS = CH[-1][2] + 1
GROUPS = [b - a + 1 for _, a, b in CH]
goto = lambda i: ["eval", f"window.__sh.goto({i}); 'state {i}'"]

MEASURE = r"""(() => {
  const MIN = __MINPX__, sh = document.querySelector('.sh'), svg = sh.querySelector('.fig-svg'), bad = [];
  const video = sh.dataset.video === '1', layout = video ? 'video' : innerWidth <= 700 ? 'phone' : 'desk';
  const tx = [...svg.querySelectorAll('text')], m = svg.getScreenCTM().a, px = tx.map((t) => parseFloat(getComputedStyle(t).fontSize) * m), minpx = tx.length ? Math.min(...px) : null;
  if (minpx !== null && minpx < MIN[layout]) bad.push(['the smallest text is below the minimum for this frame', layout, +minpx.toFixed(2), MIN[layout]]);
  const vb = svg.viewBox.baseVal;
  tx.forEach((t) => { const b = t.getBBox(); if (b.x < vb.x - 1 || b.y < vb.y - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y + b.height > vb.y + vb.height + 1) bad.push(['text outside the viewBox', t.textContent.slice(0, 40)]); });
  if ([...svg.querySelectorAll('path')].some((p) => /NaN/.test(p.getAttribute('d') || ''))) bad.push(['NaN in a path']);
  const out = {measure_ok: bad.length === 0, state: sh.dataset.state, layout, texts: tx.length, minpx: minpx === null ? null : +minpx.toFixed(2), bad};
  if (bad.length) throw new Error('measure: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__MINPX__", json.dumps(MINPX))

ROBUST = r"""(() => { const api = window.__sh, out = {combos: 0, errors: 0, msgs: []};
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true});
    for (const lang of ['ja', 'en']) { api.setLang(lang, true); for (const t of [0, 3, 99, -5]) { try { api.setT(t, true); out.combos++; } catch (e) { out.errors++; out.msgs.push(n + ' ' + lang + ' ' + t + ': ' + e.message); } } } }
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true);
  if (out.errors) throw new Error('robust: ' + JSON.stringify(out)); return JSON.stringify(out); })()"""

def rec(label, want):
    chap = next(c for c, a, b in CH if a <= want <= b)
    return ("(() => { const api = window.__sh, b = [...document.querySelectorAll('.sh-chap')]; const r = {click: %s, want: %d, wantChapter: %s, state: api.state, chapter: api.chapter, pressed: b.filter((x) => x.getAttribute('aria-pressed') === 'true').map((x) => x.dataset.chap), hash: location.hash};"
            " (window.__chk = window.__chk || []).push(r); return JSON.stringify(r); })()") % (json.dumps(label), want, json.dumps(chap))

VERDICT = r"""(() => { const chk = window.__chk || [], bad = [], GROUPS = __GROUPS__, N = __N__, CH = __CH__;
  const btns = [...document.querySelectorAll('.sh-chap')]; if (btns.length !== CH.length) bad.push('chapter buttons: ' + btns.length);
  CH.forEach(([name, a]) => { const b = btns.find((x) => x.dataset.chap === name); if (!b) bad.push('missing ' + name); else { if (Number(b.dataset.go) !== a) bad.push('target of ' + name + ': ' + b.dataset.go); if (!b.textContent.trim()) bad.push('no label on ' + name); } });
  chk.forEach((r) => { if (r.state !== r.want) bad.push(r.click + ' -> state ' + r.state + ' (want ' + r.want + ')'); if (r.chapter !== r.wantChapter) bad.push(r.click + ' -> chapter ' + r.chapter); if (r.pressed.length !== 1 || r.pressed[0] !== r.wantChapter) bad.push('pressed after ' + r.click + ': ' + r.pressed.join(',')); if (r.hash !== '#s' + r.want) bad.push('hash after ' + r.click + ': ' + r.hash); });
  const grp = [...document.querySelectorAll('.sh-stepgrp')].map((g) => g.querySelectorAll('.sh-step').length); if (JSON.stringify(grp) !== JSON.stringify(GROUPS)) bad.push('step groups: ' + JSON.stringify(grp));
  if (document.querySelectorAll('.sh-step').length !== N) bad.push('numbered steps: ' + document.querySelectorAll('.sh-step').length);
  const out = {chapters_ok: bad.length === 0, clicks: chk.map((r) => r.click + ' -> ' + r.state), step_groups: grp, bad}; if (bad.length) throw new Error('chapters: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__GROUPS__", json.dumps(GROUPS)).replace("__N__", str(NS)).replace("__CH__", json.dumps([[c, a] for c, a, _ in CH]))

states = [["wait", 1500]]
for i in range(NS):
    states += [goto(i), ["wait", 1400], ["eval", MEASURE]]
write = lambda name, steps: (OUT / name).write_text(json.dumps(steps, ensure_ascii=False, indent=1), encoding="utf-8")
write("check_states.json", states)
write("check_robust.json", [["wait", 1500], ["eval", ROBUST], ["wait", 500], goto(0), ["wait", 800]])
# real clicks, in an order that changes the state every time (last chapter first, back to the first), then one click on a numbered step inside another chapter
order = [c for c, _, _ in reversed(CH)]            # last chapter first ... first chapter last: every click changes the state
chap = [["wait", 1500], ["eval", "window.__chk = []; 'chapter check: start'"], goto(0), ["wait", 600]]
for name in order:
    first = next(a for c, a, _ in CH if c == name)
    chap += [["click", f'.sh-chap[data-chap="{name}"]'], ["wait", 700], ["eval", rec(name, first)]]
mid = NS - 1 if NS > 1 else 0
chap += [["click", f'.sh-step[data-n="{mid}"]'], ["wait", 700], ["eval", rec(f"step {mid}", mid)], ["eval", VERDICT]]
write("check_chapters.json", chap)
cap = str(OUT.parent / "captures")
write("check_capture.json", [["wait", 2000], goto(CAP_STATE), ["wait", 2200], ["shot", f"{cap}/video_s{CAP_STATE}.png", "html", 1, [0, 0, cfg["frames"]["video"][0], cfg["frames"]["video"][1]]]])
write("check_desk_capture.json", [["wait", 2000], goto(CAP_STATE), ["wait", 2200], ["shot", f"{cap}/page_dark_s{CAP_STATE}.png", ".sh", 1]])
print(f"wrote check_states.json ({len(states)} steps), check_robust.json, check_chapters.json ({len(chap)} steps), check_capture.json, check_desk_capture.json -> {OUT} · {NS} states · groups {GROUPS}")
