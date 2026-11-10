"""make_check.py — writes the action files that drive headless Chrome (the `anatomy` skill's scripts/drive.mjs) for the moy-1 figure.
  check_states.json    every state: goto, wait, MEASURE  (a failing eval throws: drive.mjs exits non-zero; its own `console:` line reports console errors)
  check_robust.json    every state x both languages x positions x camera extremes, each drawn synchronously: any throw / NaN fails
  check_chapters.json  REAL clicks on the chapter buttons (not api calls): the state they land on, the chapter, the pressed button, the hash, the grouping of the numbered steps
  check_words.json     every state x both languages: the words that must not be used (BRIEF §3), allowed only inside a sentence that negates them; with a positive control of the scan itself
  check_capture*.json  one frame of a state
MEASURE = per state: the smallest svg text in px on screen (font-size x the plate's scale) and the smallest html text, against config.json "minpx"; any svg text outside the viewBox;
          overlapping svg texts; NaN in a path; (video) nothing cut off at the bottom of the 1080 frame; (quote states) the quote column is not clipped.
Usage:   python3 -I make_check.py <dir> [<capture state>]      then   sh run_checks.sh <dir>
Every number the checks need (states, groups, thresholds) comes from config.json: the numbers of the states exist in one place.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "checks").resolve()
OUT.mkdir(parents=True, exist_ok=True)
CAP_STATE = int(sys.argv[2]) if len(sys.argv) > 2 else 8
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
CH, MINPX = cfg["chapters"], cfg["minpx"]
NS = CH[-1][2] + 1
GROUPS = [b - a + 1 for _, a, b in CH]
goto = lambda i: ["eval", f"window.__sh.goto({i}, {{instant: true}}); 'state {i}'"]

MEASURE = r"""(() => {
  const MIN = __MINPX__, sh = document.querySelector('.sh'), svg = sh.querySelector('.fig-svg'), bad = [];
  const video = sh.dataset.video === '1', layout = video ? 'video' : innerWidth <= 700 ? 'phone' : 'desk', ledger = sh.dataset.chapter === 'ledger';
  const out = {state: sh.dataset.state, layout, lang: sh.dataset.lang};
  if (!ledger) {
    const tx = [...svg.querySelectorAll('text')], m = svg.getScreenCTM().a, px = tx.map((t) => parseFloat(getComputedStyle(t).fontSize) * m), minpx = tx.length ? Math.min(...px) : null;
    if (minpx !== null && minpx < MIN[layout]) bad.push(['the smallest svg text is below the minimum for this frame', layout, +minpx.toFixed(2), MIN[layout], tx[px.indexOf(minpx)].textContent.slice(0, 30)]);
    const vb = svg.viewBox.baseVal;
    tx.forEach((t) => { const b = t.getBBox(); if (b.x < vb.x - 1 || b.y < vb.y - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y + b.height > vb.y + vb.height + 1) bad.push(['text outside the viewBox', t.textContent.slice(0, 40)]); });
    if ([...svg.querySelectorAll('path')].some((p) => /NaN/.test(p.getAttribute('d') || '')) || /NaN/.test(svg.innerHTML)) bad.push(['NaN in the svg']);
    const rects = tx.map((t) => t.getBoundingClientRect()); let ov = 0;
    for (let i = 0; i < rects.length; i++) for (let j = i + 1; j < rects.length; j++) { const a = rects[i], b = rects[j], w = Math.min(a.right, b.right) - Math.max(a.left, b.left), h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top); if (w > 2 && h > 3.5) { ov++; if (ov <= 3) bad.push(['overlapping svg texts', tx[i].textContent.slice(0, 24), tx[j].textContent.slice(0, 24), +w.toFixed(1), +h.toFixed(1)]); } }
    out.texts = tx.length; out.minpx = minpx === null ? null : +minpx.toFixed(2); out.overlaps = ov;
  }
  // v2: the construction inset (an svg in the quote column): its smallest text against the same minimum
  sh.querySelectorAll('.fig-quote svg.fig-inset').forEach((isv) => { const m2 = isv.getScreenCTM().a, t2 = [...isv.querySelectorAll('text')].map((t) => parseFloat(getComputedStyle(t).fontSize) * m2); if (t2.length) { const mn = Math.min(...t2); out.inset_minpx = +mn.toFixed(2); if (mn < MIN[layout]) bad.push(['the smallest inset text is below the minimum for this frame', layout, +mn.toFixed(2), MIN[layout]]); } });
  // html text: the smallest font on the screen (visible elements with their own text)
  let hmin = 1e9, hwho = '';
  sh.querySelectorAll('*').forEach((el) => { if (el.closest('svg')) return; const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') return; const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()); if (!own) return; const r = el.getBoundingClientRect(); if (!r.width || !r.height) return; const f = parseFloat(cs.fontSize); if (f < hmin) { hmin = f; hwho = el.className + ':' + el.textContent.trim().slice(0, 24); } });
  out.htmlmin = hmin === 1e9 ? null : +hmin.toFixed(2); if (hmin < MIN[layout]) bad.push(['the smallest html text is below the minimum', layout, hmin, MIN[layout], hwho]);
  const q = sh.querySelector('.fig-quote'); if (q && getComputedStyle(q).display !== 'none') { out.quote_clipped = q.scrollHeight > q.clientHeight + 2; if (out.quote_clipped) bad.push(['the quote column is clipped', q.scrollHeight, q.clientHeight]); }
  if (video) { const strip = sh.querySelector('.sh-strip').getBoundingClientRect(); out.strip_bottom = Math.round(strip.bottom); if (strip.bottom > innerHeight - 2) bad.push(['the strip is cut off at the bottom of the frame', Math.round(strip.bottom), innerHeight]); if (sh.scrollHeight > sh.clientHeight + 2) bad.push(['the video frame has clipped content', sh.scrollHeight, sh.clientHeight]); }
  if (document.documentElement.scrollWidth > innerWidth + 1) bad.push(['horizontal page scroll', document.documentElement.scrollWidth, innerWidth]);
  out.measure_ok = bad.length === 0; out.bad = bad;
  if (bad.length) throw new Error('measure: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__MINPX__", json.dumps(MINPX))

ROBUST = r"""(() => { const api = window.__sh, out = {combos: 0, errors: 0, nan: 0, msgs: []}, svg = document.querySelector('.fig-svg');
  const views = [null, {az: 3, el: 3, zoom: 0.5}, {az: 177, el: 82, zoom: 2.6}, {az: 90, el: 50, zoom: 1.4}, {az: 30, el: 20, zoom: 1}];
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true});
    const rg = document.querySelector('.fig-range'), lo = Number(rg.min), hi = Number(rg.max);
    for (const lang of ['ja', 'en']) { api.setLang(lang, true);
      for (const t of [lo, Math.round((lo + hi) / 2), hi, hi + 50, -5]) { for (const v of views) {
        try { api.setT(t, true); if (v) api.setView(v, true); api.redraw(); out.combos++; if (/NaN|undefined|Infinity/.test(svg.innerHTML)) { out.nan++; out.msgs.push(n + ' ' + lang + ' ' + t + ': NaN/undefined in the svg'); } } catch (e) { out.errors++; out.msgs.push(n + ' ' + lang + ' ' + t + ' ' + JSON.stringify(v) + ': ' + e.message); } } } } }
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true);
  if (out.errors || out.nan) throw new Error('robust: ' + JSON.stringify(out).slice(0, 1500)); return JSON.stringify(out); })()"""

def rec(label, want):
    chap = next(c for c, a, b in CH if a <= want <= b)
    return ("(() => { const api = window.__sh, b = [...document.querySelectorAll('.sh-chap')]; const r = {click: %s, want: %d, wantChapter: %s, state: api.state, chapter: api.chapter, pressed: b.filter((x) => x.getAttribute('aria-pressed') === 'true').map((x) => x.dataset.chap), hash: location.hash, label: b.map((x) => x.textContent.trim())};"
            " (window.__chk = window.__chk || []).push(r); return JSON.stringify(r); })()") % (json.dumps(label), want, json.dumps(chap))

VERDICT = r"""(() => { const chk = window.__chk || [], bad = [], GROUPS = __GROUPS__, N = __N__, CH = __CH__;
  const btns = [...document.querySelectorAll('.sh-chap')]; if (btns.length !== CH.length) bad.push('chapter buttons: ' + btns.length);
  CH.forEach(([name, a]) => { const b = btns.find((x) => x.dataset.chap === name); if (!b) bad.push('missing ' + name); else { if (Number(b.dataset.go) !== a) bad.push('target of ' + name + ': ' + b.dataset.go); if (!b.textContent.trim()) bad.push('no label on ' + name); } });
  chk.forEach((r) => { if (r.state !== r.want) bad.push(r.click + ' -> state ' + r.state + ' (want ' + r.want + ')'); if (r.chapter !== r.wantChapter) bad.push(r.click + ' -> chapter ' + r.chapter); if (r.pressed.length !== 1 || r.pressed[0] !== r.wantChapter) bad.push('pressed after ' + r.click + ': ' + r.pressed.join(',')); if (r.hash !== '#s' + r.want) bad.push('hash after ' + r.click + ': ' + r.hash); });
  const grp = [...document.querySelectorAll('.sh-stepgrp')].map((g) => g.querySelectorAll('.sh-step').length); if (JSON.stringify(grp) !== JSON.stringify(GROUPS)) bad.push('step groups: ' + JSON.stringify(grp));
  if (document.querySelectorAll('.sh-step').length !== N) bad.push('numbered steps: ' + document.querySelectorAll('.sh-step').length);
  const out = {chapters_ok: bad.length === 0, clicks: chk.map((r) => r.click + ' -> ' + r.state), labels: chk.length ? chk[chk.length - 1].label : [], step_groups: grp, bad}; if (bad.length) throw new Error('chapters: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__GROUPS__", json.dumps(GROUPS)).replace("__N__", str(NS)).replace("__CH__", json.dumps([[c, a] for c, a, _ in CH]))

# the words the figure must not use (BRIEF §3). A hit is allowed only inside a sentence that also negates it (the "cannot say" sentences name them in order to refuse them).
WORDS = r"""(() => { const api = window.__sh, root = document.querySelector('.sh');
  const BAD = [/考え始めた/, /考えなかった/, /commit の正体/, /(?:SAE|活性)が\s*bind を決める/, /\bbegan to think\b/i, /\bdid not think\b/i, /\bsubstance of the commit\b/i, /\bdecides the bind\b/i, /励起/, /活性化/, /回路/, /(?:model|モデル|AI)が(?:考えた|迷った|気づいた|気付いた|本当は分かっていた|知っていた)/, /AI の心/, /open は He・Hi に引かれた/, /block が答えを教えた/, /\bexcit(?:ed|ation)\b/i, /\bactivation\b/i, /\bcircuit\b/i, /\b(?:the )?model (?:thought|hesitated|noticed|really knew|was pulled)\b/i, /\bit (?:thought|hesitated|noticed)\b/i, /the block taught/i, /open was pulled to He/i, /the AI's mind/i];
  const NEG = /言わない|言えない|とは言わ|ではない|ではなく|しない|無い|not said|is not|are not|not called|cannot|never|does not say|not say|do not|did not|not claim|no |[?？]/i;
  const scan = (text) => { const hits = []; for (const s of text.split(/(?<=[。.!?!?\n])/)) for (const rx of BAD) { const m = s.match(rx); if (m && !NEG.test(s)) hits.push(m[0] + ' @ ' + s.trim().slice(0, 60)); } return hits; };
  // the positive control of the scan itself: an un-negated bad sentence is caught, a negated one is let through
  const pc1 = scan('このモデルが考えたから bind した。'), pc2 = scan('「model が考えた」とは言わない。'), pc3 = scan('The model thought about it. It was a circuit.'), pc4 = scan('The "O pair" is not called a circuit.');
  const pc5 = scan('モデルが O1O2 で考え始めた。'), pc6 = scan('「model が O1O2 で考え始めた」とは言わない。'), pc7 = scan('The model began to think in O1O2.'), pc8 = scan('That \"the model began to think in O1O2\" is not said.');
  if (!(pc1.length === 1 && pc2.length === 0 && pc3.length >= 1 && pc4.length === 0 && pc5.length === 1 && pc6.length === 0 && pc7.length === 1 && pc8.length === 0)) throw new Error('the word scan fails its own control: ' + JSON.stringify([pc1, pc2, pc3, pc4, pc5, pc6, pc7, pc8]));
  const found = [];
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true}); for (const lang of ['ja', 'en']) { api.setLang(lang, true); api.redraw(); const svg = [...root.querySelectorAll('.fig-svg text')].map((t) => t.textContent).join('\n'), txt = root.innerText + '\n' + svg;
    for (const h of scan(txt)) found.push(n + ' ' + lang + ': ' + h); } }
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true);
  const out = {words_ok: found.length === 0, found: found.slice(0, 12), control: [pc1.length, pc2.length, pc3.length, pc4.length, pc5.length, pc6.length, pc7.length, pc8.length]}; if (found.length) throw new Error('words: ' + JSON.stringify(out)); return JSON.stringify(out); })()"""

states = [["wait", 1500]]
for i in range(NS):
    states += [goto(i), ["wait", 1300], ["eval", MEASURE]]
write = lambda name, steps: (OUT / name).write_text(json.dumps(steps, ensure_ascii=False, indent=1), encoding="utf-8")
write("check_states.json", states)
# the same measure in English (the texts are longer in places): a second pass per state with the language switched
en = [["wait", 1500], ["eval", "window.__sh.setLang('en', true); 'lang en'"]]
for i in range(NS):
    en += [goto(i), ["wait", 1300], ["eval", MEASURE]]
write("check_states_en.json", en)
write("check_robust.json", [["wait", 1500], ["eval", ROBUST], ["wait", 500], goto(0), ["wait", 800]])
write("check_words.json", [["wait", 1500], ["eval", WORDS], ["wait", 300]])
order = [c for c, _, _ in reversed(CH)]            # last chapter first ... first chapter last: every click changes the state
chap = [["wait", 1500], ["eval", "window.__chk = []; 'chapter check: start'"], goto(0), ["wait", 600]]
for name in order:
    first = next(a for c, a, _ in CH if c == name)
    chap += [["click", f'.sh-chap[data-chap="{name}"]'], ["wait", 700], ["eval", rec(name, first)]]
mid = 13
chap += [["click", f'.sh-step[data-n="{mid}"]'], ["wait", 700], ["eval", rec(f"step {mid}", mid)], ["eval", VERDICT]]
write("check_chapters.json", chap)

# ja / en parity: the numbers that a state shows (the readout and every card) are the same in both languages (the words are not)
PARITY = r"""(() => { const api = window.__sh, root = document.querySelector('.sh'), num = (s) => (s.match(/-?\d+(?:[.,]\d+)?/g) || []).map((x) => x.replace(',', '')).sort().join(' '), bad = [];
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true}); const get = (lang) => { api.setLang(lang, true); api.redraw(); return {readout: num(root.querySelector('[data-readout]').textContent.replace(/^.*?(?=\d)/, '')), chips: [...root.querySelectorAll('.sh-chip')].map((c) => num(c.querySelector('.v').textContent)).join(' | ')}; };
    const ja = get('ja'), en = get('en'); if (ja.chips !== en.chips) bad.push(['chips', n, ja.chips, en.chips]); }
  // the control of the comparison itself: ja's cards of one state against en's cards of another state must DIFFER (a check that cannot tell them apart would pass everything)
  api.goto(4, {instant: true, silent: true}); api.setLang('ja', true); api.redraw(); const a4 = [...root.querySelectorAll('.sh-chip .v')].map((c) => num(c.textContent)).join(' | ');
  api.goto(9, {instant: true, silent: true}); api.setLang('en', true); api.redraw(); const b9 = [...root.querySelectorAll('.sh-chip .v')].map((c) => num(c.textContent)).join(' | ');
  if (a4 === b9) throw new Error('parity control failed: different states compare equal'); 
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true);
  const out = {parity_ok: bad.length === 0, control_differs: a4 !== b9, bad}; if (bad.length) throw new Error('parity: ' + JSON.stringify(out).slice(0, 1200)); return JSON.stringify(out); })()"""
write("check_parity.json", [["wait", 1500], ["eval", PARITY]])
# interaction: a real drag orbits the picture, the arrow keys walk the states, the slider moves the focus row
ORBIT_BEFORE = "window.__orbit0 = document.querySelector('.fig-svg').innerHTML.length + ':' + document.querySelector('.fig-svg').innerHTML.slice(2000, 2200); 'orbit: before'"
ORBIT_AFTER = "(() => { const a = document.querySelector('.fig-svg').innerHTML.length + ':' + document.querySelector('.fig-svg').innerHTML.slice(2000, 2200); if (a === window.__orbit0) throw new Error('a drag did not change the picture'); return 'orbit: the drag changed the picture'; })()"
write("check_interaction.json", [["wait", 1500], goto(8), ["wait", 1200], ["eval", ORBIT_BEFORE], ["drag", ".fig-svg", 0.3, 0.5, 0.6, 0.4, 14], ["wait", 1500], ["eval", ORBIT_AFTER],
    ["key", "ArrowRight"], ["wait", 900], ["eval", "(() => { if (window.__sh.state !== 9) throw new Error('ArrowRight did not walk to state 9: ' + window.__sh.state); return 'key: ArrowRight -> 9'; })()"],
    ["key", "ArrowLeft"], ["wait", 900], ["eval", "(() => { if (window.__sh.state !== 8) throw new Error('ArrowLeft did not walk back to 8'); return 'key: ArrowLeft -> 8'; })()"],
    ["key", "."], ["wait", 700], ["eval", "(() => { const t = window.__sh.t; if (t !== 4) throw new Error('the . key did not move the focus row from 3 to 4: ' + t); return 'key: . -> t ' + t; })()"],
    ["eval", "(() => { const r = document.querySelector('.fig-range'); r.value = '7'; r.dispatchEvent(new Event('input', {bubbles: true})); return 'slider -> 7'; })()"], ["wait", 800],
    ["eval", "(() => { if (window.__sh.t !== 7) throw new Error('the slider did not set t to 7: ' + window.__sh.t); const ro = document.querySelector('[data-readout]').textContent; if (!/s7/.test(ro)) throw new Error('the readout does not name row s7: ' + ro); return 'slider: the readout says ' + ro.slice(0, 40); })()"],
    ["key", "l"], ["wait", 700], ["eval", "(() => { if (window.__sh.lang !== 'en') throw new Error('the l key did not switch the language'); return 'key: l -> en'; })()"]])


# v2: the chapter "construction x SAE trajectory": the construction inset lights up where the text under the cursor hits a predicate; the keys / slider move the cursor; the aggregate and the two labels are on the screen; and the rule
# "cmt5's bind is never written with one label only": every state (ja / en) that gives the whole-text count (40 / 40 or 8 / 40) also gives the answer-field count (36 / 40 or 4 / 40), and the other way round.
SAE = r"""(() => { const api = window.__sh, root = document.querySelector('.sh'), out = {}, bad = [];
  const lit = (sel) => root.querySelectorAll('.fig-quote ' + sel + '.on').length;
  const settle = (n, t) => { api.goto(n, {instant: true, silent: true}); if (t !== undefined) api.setT(t, true); api.redraw(); };
  const D = window.__DATA.olm59;
  // S_O: the event token lights the O1O2 circle (and its segment), not the He-Hi circle; a token far from any predicate lights nothing; an O-name token lights the points only
  settle(18, D.S_O.event); out.s18_event = {t: api.t, ringO: lit('.in-ring-o'), ringH: lit('.in-ring-h'), segO: lit('.in-seg-o')};
  if (!(api.t === D.S_O.event && out.s18_event.ringO === 1 && out.s18_event.ringH === 0 && out.s18_event.segO === 1)) bad.push(['state 18 at the event token: the O1O2 circle must light, the He-Hi circle must not', out.s18_event]);
  const none = D.S_O.mask.findIndex((m) => m === 0), onlyName = D.S_O.mask.findIndex((m) => (m & 0b001111) === 1);
  settle(18, none); out.s18_none = {t: api.t, ringO: lit('.in-ring-o'), ringH: lit('.in-ring-h'), pts: lit('.in-pt')}; if (!(out.s18_none.ringO === 0 && out.s18_none.ringH === 0 && out.s18_none.pts === 0)) bad.push(['state 18 at a token no predicate hits: nothing may light', out.s18_none]);
  settle(18, onlyName); out.s18_name = {t: api.t, ringO: lit('.in-ring-o'), ptsO: lit('.in-pt-o')}; if (!(out.s18_name.ringO === 0 && out.s18_name.ptsO === 2)) bad.push(['state 18 at an O-name token: the two O points light, the ring does not', out.s18_name]);
  // keys and the slider move the cursor
  settle(18, D.S_O.event); root.focus(); root.dispatchEvent(new KeyboardEvent('keydown', {key: '.', bubbles: true})); out.key_dot = api.t; if (api.t !== D.S_O.event + 1) bad.push(['the . key moves the cursor token by one', api.t]);
  const rg = root.querySelector('.fig-range'); rg.value = '200'; rg.dispatchEvent(new Event('input', {bubbles: true})); out.slider = {t: api.t, readout: root.querySelector('[data-readout]').textContent.slice(0, 40)}; if (!(api.t === 200 && /token 200 \//.test(out.slider.readout))) bad.push(['the slider moves the cursor token', out.slider]);
  // S_H: the He-Hi circle lights, the O1O2 circle does not
  settle(19, D.S_H.event); out.s19_event = {ringO: lit('.in-ring-o'), ringH: lit('.in-ring-h')}; if (!(out.s19_event.ringH === 1 && out.s19_event.ringO === 0)) bad.push(['state 19 at the event token: the He-Hi circle must light, the O1O2 circle must not', out.s19_event]);
  // state 20: two insets; at the event (t = half) the O1O2 circle of the first and the He-Hi circle of the second light
  settle(20, D.half); out.s20 = {insets: root.querySelectorAll('.fig-quote svg.fig-inset').length, ringO: lit('.in-ring-o'), ringH: lit('.in-ring-h')}; if (!(out.s20.insets === 2 && out.s20.ringO === 1 && out.s20.ringH === 1)) bad.push(['state 20: two insets, one ring each at the event', out.s20]);
  // state 21: ten columns (4 groups x 2 + Q1 + Q2) and the two missed predictions on the chips; state 25 (22 in v2, 24 in v2.1): the 14-row label table with 6 rows that change
  settle(21); out.s21 = {boxes: root.querySelectorAll('.fig-svg .bx.t-b, .fig-svg .bx.t-o').length, chips: [...root.querySelectorAll('.sh-chip .v')].map((c) => c.textContent).slice(0, 3)};
  if (!(out.s21.chips[0] === D.Q1.up + ' / ' + D.Q1.n && out.s21.chips[1] === D.Q2.up + ' / ' + D.Q2.n)) bad.push(['state 21 chips: Q1 and Q2', out.s21.chips]);
  if (out.s21.boxes < 10) bad.push(['state 21: fewer than 10 coloured columns', out.s21.boxes]);
  settle(25); out.s24 = {rows: root.querySelectorAll('.fig-quote table.lab tr').length - 1, changed: root.querySelectorAll('.fig-quote table.lab tr.chg').length}; if (!(out.s24.rows === 14 && out.s24.changed === 6)) bad.push(['state 25: the label table has 14 rows, 6 of them change', out.s24]);
  // the two-labels rule over every state and both languages
  const hits = []; const W = /(?<![\d.])(?:40|8) \/ 40/, F = /(?<![\d.])(?:36|4) \/ 40/;
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true}); for (const lang of ['ja', 'en']) { api.setLang(lang, true); api.redraw();
    const txt = root.innerText + '\n' + [...root.querySelectorAll('.fig-svg text')].map((t) => t.textContent).join('\n'); const w = W.test(txt), f = F.test(txt); if (w !== f) hits.push(n + ' ' + lang + ': whole-text count ' + w + ' / answer-field count ' + f); } }
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true);
  // the positive control of the rule: a text with one count only is caught, a text with both is not
  const rule = (t) => W.test(t) !== F.test(t); if (!(rule('bind 40 / 40 vs 8 / 40') && !rule('bind 40 / 40 vs 8 / 40 and 36 / 40 vs 4 / 40') && rule('36 / 40 only') && !rule('nothing'))) bad.push(['the two-labels rule fails its own control']);
  out.two_labels = {states_checked: api.nstate * 2, violations: hits}; if (hits.length) bad.push(['a state writes only one label of cmt5\'s bind', hits.slice(0, 6)]);
  const res = Object.assign({sae_ok: bad.length === 0, bad: bad, two_labels: out.two_labels}, out); if (bad.length) throw new Error('sae: ' + JSON.stringify(res)); return JSON.stringify(res); })()"""
write("check_sae.json", [["wait", 1500], ["eval", SAE]])


# ---------------------------------------------------------------------------------------------------- v2.1: olm62's two states · the card marks (a REAL click opens the map) · the map. Expected values are read from the raw files here, not from the page.
import os
REPO = pathlib.Path(os.environ.get("MOY1_REPO", HERE / "data"))   # bundle: the frozen files are copied under data/
R62 = json.loads((REPO / "ConstructGap/exp/olm62/read.json").read_text(encoding="utf-8"))
TS = json.loads((REPO / "conversations/2026-10-27/card_tree_v2/entry_merged_v2_2_1/tree_src.json").read_text(encoding="utf-8"))
CLN = {c["id"]: c["name"] for c in TS["clusters"]}
ZONE = {"cmt5": "C1", "cmt13": "C2", "olm4": "C3", "olm7": "C3", "replication_config_frozen": "before", "pc1": "before", "screen_bf16": "before", "behavior_screen": "before", "F5": "before", "moy_suite_report": "before", "olm59": "after", "olm62": "after"}
DISP = {"screen_bf16": "screen bf16", "behavior_screen": "behavior screen"}
sae0 = next(a for c, a, b in CH if c == "sae"); sae1 = next(b for c, a, b in CH if c == "sae"); tree0 = next(a for c, a, b in CH if c == "tree"); led0 = next(a for c, a, b in CH if c == "ledger")
EXP = {"scat": sae0 + 5, "flat": sae0 + 6, "lab": sae1, "tree": tree0, "led": led0,
       "marks": cfg["card_marks"], "mark_ja": {k: f"札 {DISP.get(k, k)} · " + ("系統樹の前" if z == "before" else "系統樹の後" if z == "after" else f"{z} {CLN[z]}") for k, z in ZONE.items()},
       "o_n": R62["o_diam"]["n"], "h_n": R62["h_diam"]["n"], "chip_o": f"{R62['o_diam']['math_up']} / {R62['o_diam']['n']}", "chip_h": f"{R62['h_diam']['math_up']} / {R62['h_diam']['n']}",
       "flat_up": int(R62["o_diam"]["mid_up_when_math_flat"].split(" / ")[0]), "flat_n": int(R62["o_diam"]["mid_up_when_math_flat"].split(" / ")[1]), "q2_chip": R62["Q2"]["o_diam_mid_up_when_math_flat"],
       "n_cards": len(ZONE), "n_clusters": len(TS["clusters"]), "cluster_names": [c["name"] for c in TS["clusters"]], "cluster_names_used": [CLN[z] for z in sorted({z for z in ZONE.values() if z[0] == "C"})], "used": {k: [i for i, a in enumerate(cfg["card_marks"]) if k in a] for k in ZONE}}
V21 = r"""(() => { const api = window.__sh, root = document.querySelector('.sh'), E = __EXP__, bad = [], out = {};
  const settle = (n, lang) => { api.goto(n, {instant: true, silent: true}); api.setLang(lang || 'ja', true); api.redraw(); };
  const cnt = (sel) => root.querySelectorAll('.fig-svg ' + sel).length, chips = () => [...root.querySelectorAll('.sh-chip .v')].map((c) => c.textContent.trim());
  // state scat: one dot per event on one scale (59 + 34), two rings (S_O, S_H), two bars; the chips are read.json's own counts
  settle(E.scat); out.scat = {o: cnt('.pt62.o'), h: cnt('.pt62.h'), ring: cnt('.pt62.ring'), bars: cnt('.bar62'), chips: chips().slice(0, 2)};
  if (!(out.scat.o === E.o_n && out.scat.h === E.h_n && out.scat.ring === 2 && out.scat.bars === 2 && out.scat.chips[0] === E.chip_o && out.scat.chips[1] === E.chip_h)) bad.push(['the scatter state', out.scat, E.o_n, E.h_n, E.chip_o, E.chip_h]);
  // state flat: 11 dots, 7 filled (mid rises) and 4 hollow; the chip is Q2's own count; the cells of the margin row are the 11 events
  settle(E.flat); out.flat = {up: cnt('.pt62.flat.up'), dn: cnt('.pt62.flat.dn'), chip: chips()[0], cells: cnt('.cell.c-b') + cnt('.cell.c-x')};
  if (!(out.flat.up === E.flat_up && out.flat.dn === E.flat_n - E.flat_up && out.flat.chip === E.q2_chip && out.flat.cells >= E.flat_n)) bad.push(['the flat state', out.flat, E.flat_up, E.flat_n, E.q2_chip]);
  // the card marks of every state, in both languages: the DOM is config.json's list (read here from the file), the text names the card and where it sits
  const wrong = [];
  for (let n = 0; n < api.nstate; n++) for (const lang of ['ja', 'en']) { settle(n, lang); const got = [...root.querySelectorAll('.sh-head .sh-card')].map((b) => b.dataset.card), want = E.marks[n].length ? E.marks[n] : (n >= E.led ? ['*'] : []);
    if (JSON.stringify(got) !== JSON.stringify(want)) wrong.push([n, lang, got, want]);
    if (lang === 'ja') for (const b of root.querySelectorAll('.sh-head .sh-card')) { const w = b.dataset.card === '*' ? '札 = この図の全部 → 地図' : E.mark_ja[b.dataset.card]; if (b.textContent !== w) wrong.push([n, lang, 'text', b.textContent, w]); } }
  out.marks = {states: api.nstate * 2, wrong: wrong.slice(0, 5)}; if (wrong.length) bad.push(['the card marks differ from config.json / the tree', wrong.slice(0, 5)]);
  // the map: 12 chips (one per card), 12 "used in states" lines, the nine cluster names; the numbers of a card's "used in states" are the states whose mark lists it
  settle(E.tree); const txt = [...root.querySelectorAll('.fig-svg text')].map((t) => t.textContent), joined = txt.join('\n');
  const narrow = innerWidth <= 700, want = narrow ? E.cluster_names_used : E.cluster_names;           // the phone draws the map as a list: only the clusters that hold a card are named
  out.tree = {chips: cnt('.tchip'), used: txt.filter((t) => t.startsWith('使う状態')).length, boxes: cnt('.tbox'), names: want.filter((nm) => joined.includes(nm)).length, layout: narrow ? 'list' : 'grid'};
  if (!(out.tree.chips === E.n_cards && out.tree.used === E.n_cards && out.tree.names === want.length && (narrow || out.tree.boxes === E.n_clusters + 2))) bad.push(['the map', out.tree, E.n_cards, want.length]);
  const rng = (xs) => { const o = []; let a = xs[0], b = a; for (const x of xs.slice(1)) { if (x === b + 1) b = x; else { o.push(a === b ? '' + a : a + '–' + b); a = b = x; } } o.push(a === b ? '' + a : a + '–' + b); return o.join(' · '); };
  const usedBad = Object.entries(E.used).filter(([k, xs]) => !txt.includes('使う状態 ' + rng(xs))).map(([k, xs]) => [k, rng(xs)]); out.tree.used_bad = usedBad; if (usedBad.length) bad.push(['a card\'s "used in states" numbers differ from config.json', usedBad]);
  const res = Object.assign({v21_ok: bad.length === 0, bad: bad}, out); if (bad.length) throw new Error('v21: ' + JSON.stringify(res)); return JSON.stringify(res); })()""".replace("__EXP__", json.dumps(EXP, ensure_ascii=False))
write("check_v21.json", [["wait", 1500], ["eval", V21]])
# the real click on a card mark: from state 12 the mark `cmt13` opens the map with that card selected; from a ledger state the "all" mark opens the map with none; the chapter button clears the selection
CLK = lambda tag, expr: ["eval", "(() => { const api = window.__sh, root = document.querySelector('.sh'), E = " + json.dumps({"tree": EXP["tree"]}) + "; " + expr + " })()"]
clk = [["wait", 1500], goto(12), ["wait", 700],
       CLK("a", "const got = [...root.querySelectorAll('.sh-head .sh-card')].map((b) => b.dataset.card); if (JSON.stringify(got) !== JSON.stringify(['cmt13', 'F5'])) throw new Error('marks of state 12: ' + got); return 'click: state 12 shows the marks ' + got;"),
       ["click", '.sh-head .sh-card[data-card="cmt13"]'], ["wait", 900],
       CLK("b", "const sel = [...root.querySelectorAll('.fig-svg .tchip.sel')]; if (api.state !== E.tree) throw new Error('the card mark did not open the map: state ' + api.state); if (sel.length !== 1) throw new Error('selected chips: ' + sel.length); const lead = root.querySelector('.sh-lead').textContent; if (!lead.includes('押した札: cmt13')) throw new Error('the lead does not name the pressed card'); return 'click: cmt13 -> map (state ' + api.state + ') · the pressed card is outlined · ' + lead.slice(0, 20);"),
       ["click", '.sh-step[data-n="0"]'], ["wait", 1000], ["eval", "(() => { const n = document.querySelectorAll('.sh-head .sh-card').length; if (window.__sh.state !== 0 || n !== 2) throw new Error('state 0 must show two card marks: state ' + window.__sh.state + ', marks ' + n); return 'click: the step button -> state 0, two marks'; })()"],
       ["click", '.sh-head .sh-card[data-card="replication_config_frozen"]'], ["wait", 900],
       CLK("c", "if (api.state !== E.tree) throw new Error('a mark of state 0 did not open the map'); const sel = root.querySelectorAll('.fig-svg .tchip.sel').length; if (sel !== 1) throw new Error('selected chips: ' + sel); return 'click: replication_config_frozen -> map';"),
       ["click", f'.sh-step[data-n="{EXP["tree"]}"]'], ["wait", 900],
       CLK("d", "if (api.state !== E.tree || root.querySelectorAll('.fig-svg .tchip.sel').length !== 0) throw new Error('the map opened by its number must have no card selected'); return 'click: the number of the map clears the selection';"),
       ["click", f'.sh-step[data-n="{led0}"]'], ["wait", 900], ["click", '.sh-head .sh-card[data-card="*"]'], ["wait", 900],
       CLK("e", "if (api.state !== E.tree) throw new Error('the ledger mark did not open the map'); const sel = root.querySelectorAll('.fig-svg .tchip.sel').length; if (sel !== 0) throw new Error('the ledger mark must not select a card: ' + sel); return 'click: the ledger mark -> map, no card selected';")]
write("check_cards.json", clk)
# ---------------------------------------------------------------------------------------------------- v3: the part added after the 10-28 figure (states 27-36 + the two ledger states 40-41) and the slope state 22 · expected values are read from the raw files here, not from the page
R59 = json.loads((REPO / "ConstructGap/exp/olm59/read.json").read_text(encoding="utf-8"))
R128 = json.loads((REPO / "ConstructGap/exp/olm128/read.json").read_text(encoding="utf-8"))
R101 = json.loads((REPO / "ConstructGap/exp/olm101/read.json").read_text(encoding="utf-8"))
CARDS_V3 = ["olm76", "olm84", "olm85", "olm86", "olm89", "olm91", "olm92", "olm93", "olm94", "olm95", "olm97", "olm98", "olm101", "olm106", "olm108", "olm112", "olm114", "olm128"]
AFTER_STATES = [a for a, b in cfg["parts"]["after"] for a in range(a, b + 1)] if False else [n for a, b in cfg["parts"]["after"] for n in range(a, b + 1)]
EXP3 = {"slope": sae0 + 4, "flow": next(a for c, a, b in CH if c == "flow"), "l3": next(a for c, a, b in CH if c == "l3"), "space1": next(a for c, a, b in CH if c == "space"), "struct2": next(a for c, a, b in CH if c == "struct") + 1,
        "next1": next(a for c, a, b in CH if c == "next"), "led_a": led0 + 3, "led_b": led0 + 4, "after": AFTER_STATES, "n_states": NS,
        "o_n": R59["Q3_desc"]["o_diam|close|all"]["n"], "h_n": R59["Q3_desc"]["h_diam|close|all"]["n"], "cards": len(CARDS_V3) + 2,      # v3.1: + olm83 · olm88 (stopped at a control / gate; not in the pack) drawn in station 2 of the flow
        "cells_n": sum(R128["blocked_cells"][k]["n"] for k in ("nl", "space", "nlnl")), "cells_bind": sum(R128["blocked_cells"][k]["bind"] for k in ("nl", "space", "nlnl")), "cells_json": sum(R128["blocked_cells"][k]["json"] for k in ("nl", "space", "nlnl")),
        "layers_end": len(R101["Q1_curve_full_end"])}
V3 = r"""(() => { const api = window.__sh, root = document.querySelector('.sh'), E = __EXP3__, bad = [], out = {};
  const settle = (n, lang) => { api.goto(n, {instant: true, silent: true}); api.setLang(lang || 'ja', true); api.redraw(); };
  const cnt = (sel) => root.querySelectorAll('.fig-svg ' + sel).length, texts = () => [...root.querySelectorAll('.fig-svg text')].map((t) => t.textContent);
  // the look of the added part: data-part = after on exactly the states of config.json parts, base elsewhere; the step buttons and the chapter buttons carry the same mark
  const wrong = [];
  for (let n = 0; n < api.nstate; n++) { settle(n); const want = E.after.includes(n) ? 'after' : 'base', btn = root.querySelector('.sh-step[data-n="' + n + '"]'); if (root.dataset.part !== want || btn.dataset.part !== want) wrong.push([n, root.dataset.part, btn && btn.dataset.part, want]); }
  out.part = {states: api.nstate, wrong: wrong.slice(0, 4)}; if (wrong.length) bad.push(['data-part of the states', wrong.slice(0, 4)]);
  // the slope state: 8 panels (2 kinds x 4 groups); one bar per row: 4 x 59 blue + 4 x 34 orange; the scene rows are outlined (S_O and S_H: 4 groups each)
  for (const lang of ['ja', 'en']) { settle(E.slope, lang); out['slope_' + lang] = {panels: cnt('.af-panel'), o: cnt('.bar62.o'), h: cnt('.bar62.h'), scene: cnt('.bar62.scene')};
    const q = out['slope_' + lang]; if (!(q.panels === 8 && q.o === 4 * E.o_n && q.h === 4 * E.h_n && q.scene === 8)) bad.push(['the slope state ' + lang, q, E.o_n, E.h_n]); }
  // the flow: six nodes (the 10-28 node solid, five later nodes hatched) and one tile per card
  settle(E.flow); out.flow = {nodes: cnt('.af-node'), base: cnt('.af-node.base'), later: cnt('.af-node.later'), cards: texts().filter((t) => /^olm\d+$/.test(t)).length};
  if (!(out.flow.nodes === 6 && out.flow.base === 1 && out.flow.later === 5 && out.flow.cards === E.cards)) bad.push(['the flow state', out.flow, E.cards]);
  // (a) three bars; the verdict text names Q1 as not met
  settle(E.l3); out.l3 = {bars: cnt('.bx.t-b') + cnt('.bx.t-g') + cnt('.bx.t-o'), quote_struck: root.querySelectorAll('.fig-quote .af-old').length, rail_on: cnt('.af-node.on')}; if (!(out.l3.bars === 3 && out.l3.quote_struck === 1 && out.l3.rail_on === 1)) bad.push(['the L3 state', out.l3]);
  // (b1) four rows of markers: layer 32 / layer 48 / J / bag of words each four times
  settle(E.space1); out.space1 = {l32: cnt('.af-mk.l32'), l48: cnt('.af-mk.l48'), j: cnt('.af-mk.j'), w: cnt('.af-mk.w'), null: cnt('.af-null')}; if (!(out.space1.l32 === 4 && out.space1.l48 === 4 && out.space1.j === 4 && out.space1.w === 4 && out.space1.null === 4)) bad.push(['the inference-space state', out.space1]);
  // (c2) three panels, two curves each; the layers of olm101's curve are the card's own (10)
  settle(E.struct2); out.struct2 = {po: cnt('.af-curve.po'), vo: cnt('.af-curve.vo'), vlines: cnt('.af-vline')}; if (!(out.struct2.po === 3 && out.struct2.vo === 3 && out.struct2.vlines === 3)) bad.push(['the layers state', out.struct2]);
  // (next 1) one cell per blocked row of olm128 (29), blue = bind (13)
  settle(E.next1); out.next1 = {cells: cnt('.cell.c-b') + cnt('.cell.c-g'), bind: cnt('.cell.c-b')}; if (!(out.next1.cells === E.cells_n && out.next1.bind === E.cells_bind)) bad.push(['the olm128 state', out.next1, E.cells_n, E.cells_bind]);
  // the two ledger states of the added part: L1 rows (K50-K69) / L3 rows (R07-R11) and cannot-say rows (X17-X27)
  settle(E.led_a); out.led_a = {articles: root.querySelectorAll('.fig-ledger article').length, ids: [...root.querySelectorAll('.fig-ledger .src')].map((x) => x.textContent.split(' · ')[0]).slice(0, 2)};
  settle(E.led_b); out.led_b = {l3: root.querySelectorAll('.fig-ledger section[data-lv="L3"] article').length, x: root.querySelectorAll('.fig-ledger section[data-lv="x"] article').length};
  if (!(out.led_a.articles === 20 && out.led_b.l3 === 5 && out.led_b.x === 11)) bad.push(['the ledger states of the added part', out.led_a, out.led_b]);
  // the card of the next question A is shown as READ (olm128) with its verdict, and the candidates B-E as listed only: the words of the state
  settle(E.next1 + 1); const t36 = root.querySelector('.fig-quote').textContent + texts().join(' '); out.next2 = {a_read: /olm128/.test(t36), second: /第二段|Second stage/.test(t36)}; if (!(out.next2.a_read && out.next2.second)) bad.push(['the candidates state', out.next2]);
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true);
  const res = Object.assign({v3_ok: bad.length === 0, bad: bad}, out); if (bad.length) throw new Error('v3: ' + JSON.stringify(res)); return JSON.stringify(res); })()""".replace("__EXP3__", json.dumps(EXP3, ensure_ascii=False))
write("check_v3.json", [["wait", 1500], ["eval", V3]])
cap = "captures"            # relative: the run scripts cd to the entry folder
write("check_capture.json", [["wait", 2000], goto(CAP_STATE), ["wait", 2200], ["shot", f"{cap}/video_s{CAP_STATE:02d}.png", "html", 1, [0, 0, cfg["frames"]["video"][0], cfg["frames"]["video"][1]]]])
write("check_desk_capture.json", [["wait", 2000], goto(CAP_STATE), ["wait", 2200], ["shot", f"{cap}/page_dark_s{CAP_STATE:02d}.png", ".sh", 1]])
print(f"wrote check_v3.json, check_v21.json, check_cards.json, check_parity.json, check_interaction.json, check_states.json ({len(states)} steps), check_states_en.json, check_robust.json, check_words.json, check_chapters.json ({len(chap)} steps), check_capture.json, check_desk_capture.json -> {OUT} · {NS} states · groups {GROUPS}")
