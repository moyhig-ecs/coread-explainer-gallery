"""make_check.py — writes the action files that drive headless Chrome (drive.mjs, this entry's DevTools driver) for every check of the moy-2 line explainer.
  check_states.json    every state: goto, wait, MEASURE (smallest SVG text px vs config minpx, smallest HTML text px vs minpx_html, text outside the viewBox, NaN in a path, SVG text overlaps on plane charts,
                       horizontal overflow of the HTML panels, the 1920 x 1080 frame holds the whole page, the nav band does not move between states)
  check_robust.json    every state x ja/en x every row of the rack states x every arm of the scale state + out-of-range inputs: any throw fails
  check_chapters.json  REAL clicks on the chapter buttons (last chapter first), then a numbered step, then the verdict (state, pressed button, hash, step groups, labels)
  check_drag.json      REAL mouse drags: on the rack (state 8, 11, 12, 13) the picked row changes and the side panel / the lit block follow; on the scale (state 6) the arm changes and its Tool text follows
  check_names.json     the name scan over every state x ja/en: forbidden words outside a negated sentence, old / wrong names, the evaluation-function words outside chapter G / H; plus its POSITIVE control
  capture_*.json       the stills (video 1920 x 1080 for every state + the drag moment; desk dark for every state; phone for every state; desk light and English for chosen states)
Usage:   python3 -I make_check.py <dir>      then   sh run_checks.sh
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "checks").resolve()
OUT.mkdir(parents=True, exist_ok=True)
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
CH, MINPX, MINHTML = cfg["chapters"], cfg["minpx"], cfg["minpx_html"]
NS = CH[-1][2] + 1
GROUPS = [b - a + 1 for _, a, b in CH]
ROWSTATES, ARMSTATES = cfg["rowStates"], cfg["armStates"]
goto = lambda i: ["eval", f"window.__sh.goto({i}); 'state {i}'"]
write = lambda name, steps: (OUT / name).write_text(json.dumps(steps, ensure_ascii=False, indent=1), encoding="utf-8")

MEASURE = r"""(() => {
  const MIN = __MINPX__, MINH = __MINHTML__, sh = document.querySelector('.sh'), svg = sh.querySelector('.fig-svg'), bad = [], warn = [];
  const video = sh.dataset.video === '1', layout = video ? 'video' : innerWidth <= 700 ? 'phone' : 'desk', view = sh.dataset.view, mode = (window.__sh && window.__fig.states[window.__sh.state].mode);
  const svgShown = view === 'svg' || view === 'split' || view === 'stack';
  const tx = svgShown ? [...svg.querySelectorAll('text')] : [], m = svg.getScreenCTM() ? svg.getScreenCTM().a : 0, px = tx.map((t) => parseFloat(getComputedStyle(t).fontSize) * m), minpx = tx.length ? Math.min(...px) : null;
  if (minpx !== null && minpx < MIN[layout]) bad.push(['smallest svg text below the minimum', layout, +minpx.toFixed(2), MIN[layout]]);
  const vb = svg.viewBox.baseVal;
  tx.forEach((t) => { const b = t.getBBox(); if (b.x < vb.x - 1 || b.y < vb.y - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y + b.height > vb.y + vb.height + 1) bad.push(['text outside the viewBox', t.textContent.slice(0, 40)]); });
  if ([...svg.querySelectorAll('path')].some((p) => /NaN/.test(p.getAttribute('d') || ''))) bad.push(['NaN in a path']);
  // overlaps between svg texts (plane charts fail on any; the kit's art reports them)
  const boxes = tx.map((t) => { const r = t.getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom, t.textContent]; }); let ov = 0, ovs = [];
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) { const a = boxes[i], b = boxes[j]; const w = Math.min(a[2], b[2]) - Math.max(a[0], b[0]), h = Math.min(a[3], b[3]) - Math.max(a[1], b[1]); if (w > 2 && h > 3) { ov++; if (ovs.length < 4) ovs.push(a[4].slice(0, 24) + ' | ' + b[4].slice(0, 24)); } }
  if (ov && mode !== 'rack' && mode !== 'board') bad.push(['svg texts overlap', ov, ovs]); else if (ov) warn.push(['art tags overlap', ov, ovs]);
  // v1.1 F6: on the rack, the height-axis labels (12,288 cap / 1,000 / 100 / 10) must not meet any block's rectangle (selected by their text, so the same check runs on the v1 build = its positive control)
  if (mode === 'rack') { const TICK = /^(10|100|1,000|12,288 上限|12,288 cap)$/, tl = tx.filter((t) => TICK.test(t.textContent.trim())), blocks = [...svg.querySelectorAll('.rk')].map((g) => g.getBoundingClientRect()); let meet = [];
    if (tl.length !== 4) bad.push(['axis labels on the rack', tl.length, 'expected 4']);
    for (const t of tl) { const a = t.getBoundingClientRect(); for (const b of blocks) { const w = Math.min(a.right, b.right) - Math.max(a.left, b.left), h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top); if (w > 0.5 && h > 0.5) { meet.push(t.textContent.trim()); break; } } }
    if (meet.length) bad.push(['axis label meets a block', meet]); else warn.push(['axis labels clear of the blocks', tl.length, blocks.length]); }
  const cross = (a, b) => Math.min(a.right, b.right) - Math.max(a.left, b.left) > 0.5 && Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 0.5;
  // v1.2 G3: no text sits on a gate line (the dashed 0.75 / 0.80 of state 4): the line's x inside the text's box and the two overlap in height
  const gl = svgShown ? [...svg.querySelectorAll('.fig-gate')].map((g) => g.getBoundingClientRect()) : [], onLine = [];
  for (const t of tx) { const r = t.getBoundingClientRect(); for (const g of gl) { const x = (g.left + g.right) / 2; if (r.left + 0.5 < x && x < r.right - 0.5 && Math.min(r.bottom, g.bottom) - Math.max(r.top, g.top) > 0.5) { onLine.push(t.textContent.slice(0, 30)); break; } } }
  if (onLine.length) bad.push(['text on a gate line (G3)', onLine]); else if (gl.length) warn.push(['texts clear of the gate lines', tx.length, gl.length]);
  // v1.2 G4: on the rack, a row's name tag (b0_j00 / ◇ b2_j09 …, picked by its text so the v1.1 build runs the same check) meets no block and no other text
  if (mode === 'rack') { const NMR = /^(◇ )?b\d_j\d\d$/, nt = tx.filter((t) => NMR.test(t.textContent.trim())), blocks = [...svg.querySelectorAll('.rk')].map((g) => g.getBoundingClientRect()), meet = [];
    for (const t of nt) { const a = t.getBoundingClientRect(); if (blocks.some((b) => cross(a, b))) meet.push(t.textContent.trim() + ' | a block');
      for (const u of tx) if (u !== t && cross(a, u.getBoundingClientRect())) meet.push(t.textContent.trim() + ' | ' + u.textContent.trim().slice(0, 20)); }
    if (meet.length) bad.push(['name tag meets a block or a text (G4)', meet]); else warn.push(['name tags clear of blocks and texts', nt.length]); }
  // v1.3 H4: on the drafting board (state 1), no tag's box meets a line drawn on the board (the circles, l1, O1O2, the radii, the blue apex segments, the reflection dashes, the rings; points sampled along each path every ≤ 0.75 screen px), and no two tags meet
  if (mode === 'board') { const BDL = /(^|\s)bd-(circ|line|thin|eq|refl|ghost|mid)(\s|$)/, bl = [...svg.querySelectorAll('path')].filter((p) => BDL.test(p.getAttribute('class') || '')), pts = [], hitB = [];
    for (const p of bl) { const n = p.getTotalLength(), ctm = p.getScreenCTM(); if (!ctm) continue; const step = 0.75 / Math.max(ctm.a, 0.01); for (let s = 0; s <= n + 1e-6; s += step) { const q = p.getPointAtLength(Math.min(s, n)), sp = new DOMPoint(q.x, q.y).matrixTransform(ctm); pts.push([sp.x, sp.y, (p.getAttribute('class') || '').replace(/\s+/g, '.')]); } }
    for (const t of tx) { const r = t.getBoundingClientRect(), h = pts.find(([x, y]) => x > r.left + 0.5 && x < r.right - 0.5 && y > r.top + 0.5 && y < r.bottom - 0.5); if (h) hitB.push(t.textContent.trim().slice(0, 24) + ' | ' + h[2]);
      for (const u of tx) if (u !== t && t.compareDocumentPosition(u) & 4 && cross(r, u.getBoundingClientRect())) hitB.push(t.textContent.trim().slice(0, 24) + ' | ' + u.textContent.trim().slice(0, 24)); }
    if (!bl.length) bad.push(['no board lines found (H4)']); else if (hitB.length) bad.push(['board tag meets a board line or a tag (H4)', hitB]); else warn.push(['board tags clear of the board lines and of each other', tx.length, bl.length, pts.length]); }
  // v1.2 G8: the band edges of the PREREGs are printed on the bands (state 5) and beside the short ticks (state 6)
  if (mode === 'bands' || mode === 'scale') { const have = new Set(tx.map((t) => t.textContent.trim())), miss = ['0.062', '0.182', '0.048', '0.168', '0.165〜0.168', '0.285'].filter((w) => !have.has(w)); if (miss.length) bad.push(['band edges not printed (G8)', miss]); }
  // html text: the smallest visible font, and horizontal overflow of the panels
  const vis = (e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const htmlEls = [...sh.querySelectorAll('.fig-side *, .fig-html *, .fig-ledger *, .sh-panel *, .sh-strip *, .sh-head *, .iso-plate-corner, .sh-keys *')].filter((e) => [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()) && vis(e));
  const hpx = htmlEls.map((e) => parseFloat(getComputedStyle(e).fontSize)), minh = hpx.length ? Math.min(...hpx) : null;
  if (minh !== null && minh < MINH[layout]) bad.push(['smallest html text below the minimum', layout, minh, MINH[layout], htmlEls[hpx.indexOf(minh)].className]);
  // v1.2 G5: the status line (身分) meets no panel and not the figure, and takes at most two lines (video / desk; on the phone it is not shown)
  const stamp = sh.querySelector('.sh-corner2');
  if (stamp && vis(stamp)) { const a = stamp.getBoundingClientRect(), panes = [...sh.querySelectorAll('.fig-side, .fig-html > *, .fig-ledger > section')].filter(vis); if (svgShown) panes.push(svg);
    const met = panes.filter((e) => cross(a, e.getBoundingClientRect())), lh = parseFloat(getComputedStyle(stamp).lineHeight), lines = lh ? Math.round(a.height / lh) : 0;
    if (met.length) bad.push(['status line meets a panel / the figure (G5)', met.map((e) => String(e.className.baseVal ?? e.className).slice(0, 30))]);
    if (lines > 2) bad.push(['status line takes more than two lines (G5)', lines]); }
  for (const sel of ['.fig-side', '.fig-html', '.fig-ledger', '.sh-panel', '.sh-strip']) { const e = sh.querySelector(sel); if (e && vis(e) && e.scrollWidth > e.clientWidth + 1) bad.push(['horizontal overflow', sel, e.scrollWidth, e.clientWidth]); }
  if (video) { const H = document.documentElement.scrollHeight; if (H > innerHeight + 1) bad.push(['the video frame scrolls', H, innerHeight]);
    for (const sel of ['.fig-side', '.fig-html', '.fig-ledger']) { const e = sh.querySelector(sel); if (e && vis(e) && e.scrollHeight > e.clientHeight + 2) bad.push(['cut in the still', sel, e.scrollHeight, e.clientHeight]); } }
  const nav = sh.querySelector('.sh-nav'), navTop = nav && vis(nav) ? Math.round(nav.getBoundingClientRect().top + scrollY) : null;
  (window.__navTops = window.__navTops || []).push(navTop);
  const out = {measure_ok: bad.length === 0, state: sh.dataset.state, layout, view, svgTexts: tx.length, minpx: minpx === null ? null : +minpx.toFixed(2), htmlMin: minh, overlaps: ov, warn, bad};
  if (bad.length) throw new Error('measure: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__MINPX__", json.dumps(MINPX)).replace("__MINHTML__", json.dumps(MINHTML))
NAVSAME = r"""(() => { const t = (window.__navTops || []).filter((v) => v !== null); const same = t.every((v) => v === t[0]); if (!same) throw new Error('nav band moves: ' + JSON.stringify(t)); return JSON.stringify({nav_same: same, n: t.length, top: t[0]}); })()"""

states = [["wait", 1200], ["eval", "scrollTo(0, 0); 'top'"]]
for i in range(NS):
    states += [goto(i), ["wait", 350], ["eval", "scrollTo(0, 0); 'top'"], ["eval", MEASURE]]
states += [["eval", NAVSAME]]
write("check_states.json", states)

ROBUST = r"""(() => { const api = window.__sh, out = {combos: 0, errors: 0, msgs: []};
  const tryit = (label, f) => { try { f(); out.combos++; } catch (e) { out.errors++; if (out.msgs.length < 8) out.msgs.push(label + ': ' + e.message); } };
  for (let n = 0; n < api.nstate; n++) for (const lang of ['ja', 'en']) { tryit(`goto ${n} ${lang}`, () => { api.goto(n, {silent: true}); api.setLang(lang, true); });
    if (__ROWS__.includes(n)) for (const id of api.rowsNow()) tryit(`row ${n} ${id}`, () => api.setRow(id, true));
    if (__ARMS__.includes(n)) for (const a of window.__fig.armIds) tryit(`arm ${n} ${a}`, () => api.setArm(a, true)); }
  for (const bad of [-5, 99, 3.7, 'x', null]) tryit('goto ' + bad, () => api.goto(bad, {silent: true}));
  for (const bad of ['', 'olm999:b0_j00', 'olm125:b9_j99', null]) tryit('row ' + bad, () => api.setRow(bad, true));
  tryit('arm bogus', () => api.setArm('olm000', true));
  api.goto(0, {silent: true}); api.setLang(document.documentElement.lang === 'en' ? 'en' : 'ja', true);
  if (out.errors) throw new Error('robust: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__ROWS__", json.dumps(ROWSTATES)).replace("__ARMS__", json.dumps(ARMSTATES))
write("check_robust.json", [["wait", 1200], ["eval", ROBUST], ["wait", 300]])


def rec(label, want):
    chap = next(c for c, a, b in CH if a <= want <= b)
    return ("(() => { const api = window.__sh, b = [...document.querySelectorAll('.sh-chap')]; const r = {click: %s, want: %d, wantChapter: %s, state: api.state, chapter: api.chapter, pressed: b.filter((x) => x.getAttribute('aria-pressed') === 'true').map((x) => x.dataset.chap), hash: location.hash, label: (b.find((x) => x.dataset.chap === %s) || {}).textContent};"
            " (window.__chk = window.__chk || []).push(r); return JSON.stringify(r); })()") % (json.dumps(label), want, json.dumps(chap), json.dumps(chap))


VERDICT = r"""(() => { const chk = window.__chk || [], bad = [], GROUPS = __GROUPS__, N = __N__, CH = __CH__;
  const btns = [...document.querySelectorAll('.sh-chap')]; if (btns.length !== CH.length) bad.push('chapter buttons: ' + btns.length);
  CH.forEach(([name, a]) => { const b = btns.find((x) => x.dataset.chap === name); if (!b) bad.push('missing ' + name); else { if (Number(b.dataset.go) !== a) bad.push('target of ' + name + ': ' + b.dataset.go); if (!b.textContent.trim()) bad.push('no label on ' + name); } });
  chk.forEach((r) => { if (r.state !== r.want) bad.push(r.click + ' -> state ' + r.state + ' (want ' + r.want + ')'); if (r.chapter !== r.wantChapter) bad.push(r.click + ' -> chapter ' + r.chapter); if (r.pressed.length !== 1 || r.pressed[0] !== r.wantChapter) bad.push('pressed after ' + r.click + ': ' + r.pressed.join(',')); if (r.hash !== '#s' + r.want) bad.push('hash after ' + r.click + ': ' + r.hash); });
  const grp = [...document.querySelectorAll('.sh-stepgrp')].map((g) => g.querySelectorAll('.sh-step').length); if (JSON.stringify(grp) !== JSON.stringify(GROUPS)) bad.push('step groups: ' + JSON.stringify(grp));
  if (document.querySelectorAll('.sh-step').length !== N) bad.push('numbered steps: ' + document.querySelectorAll('.sh-step').length);
  const out = {chapters_ok: bad.length === 0, clicks: chk.map((r) => r.click + ' -> ' + r.state + ' ' + r.label), step_groups: grp, bad}; if (bad.length) throw new Error('chapters: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__GROUPS__", json.dumps(GROUPS)).replace("__N__", str(NS)).replace("__CH__", json.dumps([[c, a] for c, a, _ in CH]))
chap = [["wait", 1200], ["eval", "window.__chk = []; 'chapter check: start'"], goto(0), ["wait", 300]]
for name in [c for c, _, _ in reversed(CH)]:
    first = next(a for c, a, _ in CH if c == name)
    chap += [["click", f'.sh-chap[data-chap="{name}"]'], ["wait", 400], ["eval", rec(name, first)]]
mid = 9
chap += [["click", f'.sh-step[data-n="{mid}"]'], ["wait", 400], ["eval", rec(f"step {mid}", mid)], ["click", ".sh-next"], ["wait", 300], ["eval", rec("next", mid + 1)], ["eval", VERDICT]]
write("check_chapters.json", chap)

# drag: the reader's hand picks a row / an arm (REAL mouse events from drive.mjs)
SNAP = r"""(() => { const api = window.__sh, side = document.querySelector('.fig-side'); const lit = document.querySelector('.rk[data-sel]'); return JSON.stringify({state: api.state, row: api.row, arm: api.arm, lit: lit ? lit.dataset.r : null, side: (side.querySelector('.fx-h') || {}).textContent || '', pre: ((side.querySelector('.fx-pre') || {}).textContent || '').slice(0, 60)}); })()"""
CMP = r"""((tag) => { const api = window.__sh, side = document.querySelector('.fig-side'), lit = document.querySelector('.rk[data-sel]'), prev = window.__prev || {}; const now = {state: api.state, row: api.row, arm: api.arm, lit: lit ? lit.dataset.r : null, side: (side.querySelector('.fx-h') || {}).textContent || '', pre: ((side.querySelector('.fx-pre') || {}).textContent || '').slice(0, 60)};
  const bad = []; const pick = window.__fig.states[api.state].pick;
  if (pick === 'row') { if (now.row === prev.row) bad.push('row did not change'); if (now.lit !== now.row) bad.push('lit block ' + now.lit + ' != row ' + now.row); const [a, k] = now.row.split(':'); if (!now.side.includes(a) || !now.side.includes(k)) bad.push('side panel shows ' + now.side); if (!api.rowsNow().includes(now.row)) bad.push('picked a row outside the filter'); }
  if (pick === 'arm') { if (now.arm === prev.arm) bad.push('arm did not change'); if (!now.side.includes(now.arm)) bad.push('side panel shows ' + now.side); const kind = (id) => (window.__data.arms.find((a) => a.id === id) || {}).tool; if (kind(now.arm) !== kind(prev.arm) && now.pre === prev.pre) bad.push('Tool text did not follow'); if (kind(now.arm) === kind(prev.arm) && now.pre !== prev.pre) bad.push('same Tool kind, different text'); }
  const out = {drag_ok: bad.length === 0, tag, from: prev.row || prev.arm, to: pick === 'row' ? now.row : now.arm, bad}; if (bad.length) throw new Error('drag: ' + JSON.stringify(out)); return JSON.stringify(out); })"""
drag = [["wait", 1200]]
for st, path in [(8, [0.25, 0.45, 0.62, 0.62]), (11, [0.55, 0.55, 0.3, 0.5]), (12, [0.4, 0.5, 0.7, 0.65]), (13, [0.75, 0.62, 0.665, 0.69]), (6, [0.5, 0.2, 0.5, 0.93])]:
    drag += [goto(st), ["wait", 400], ["eval", f"window.__prev = JSON.parse({SNAP}); 'snap'"], ["drag", ".fig-svg", *path, 14], ["wait", 300], ["eval", f"{CMP}('state {st}')"]]
write("check_drag.json", drag)

# the name scan: every state x ja / en; forbidden words must sit in a sentence that says it is NOT said; old / wrong names 0; evaluation-function words only in G / H
SCAN = r"""((inject) => { const api = window.__sh, hits = [], N = api.nstate;
  const NEG_JA = /(言わない|言わないこと|とは言わない|読まない|測っていない|ではない|しない)/, NEG_EN = /(not|never|does not say|is not said|no )/i;
  const BAN_JA = /(考えた|分かった|わかった|気づいた|理解した|思い出した|知っていた|迷った|計算して確かめた|前提が呼ばれた|正しい証明|心が見えた)/, BAN_EN = /\b(thought|understood|noticed|realized|realised|knew|hesitat\w*|correct proof|mind)\b/i, MEM = /(記憶|remember)/i, MEM_OK = [14, 17, 18, 19];
  const WRONG = [/olm124 の 0\.048/, /EQ[^。.]{0,24}一般には偽/, /EQ[^.]{0,30}false in general/i, /model (thinks|knows)/i];
  // v1.1 F1: the old denominators (RECORD §4 / RESULT olm127 §4) are wrong names, except in a sentence that says they are not reproduced / not kept
  const OLD = [/(?<!\d|\d\.)43\s?\/\s?47(?!\d|\.\d)/, /(?<!\d|\d\.)15\s?\/\s?15(?!\d|\.\d)/, /(?<!\d|\d\.)11\s?\/\s?14(?!\d|\.\d)/, /(?<!\d|\d\.)11\s?\/\s?12(?!\d|\.\d)/], OLD_OK = /(再現でき|据えない|not reproduced|not kept)/;
  const G = /(導出でき|derive[ds]? an evaluation|can be derived|cannot be derived)/i;
  // v1.2 G2 / G7: "この図では偽" (the legend of v1.1, wrong on the equal-radii figure) and a flat "分けられない" (state 9 and the script; 1 of 7 pairs is below 0.05) are old wordings
  const OLD12 = [/この図では偽/, /false here/i], SEP = /(分けられない|分けられず|told apart|cannot separate|can't separate)/i, SEP_OK = /(言い切らない|とは言わない|not asserted|not claimed)/i;
  for (let n = 0; n < N; n++) for (const lang of ['ja', 'en']) { api.goto(n, {silent: true}); api.setLang(lang, true);
    let text = document.querySelector('.sh').innerText; if (inject && n === 3 && lang === inject.lang) text += '\n' + inject.text;
    const sents = text.split(/(?<=[。．!?])|\n| · |(?<=\.)\s/);
    for (const s of sents) { const ban = lang === 'ja' ? BAN_JA : BAN_EN, neg = lang === 'ja' ? NEG_JA : NEG_EN; const m = ban.exec(s); if (m && !neg.test(s)) hits.push([n, lang, 'forbidden word', m[0], s.slice(0, 80)]);
      for (const w of WRONG) if (w.test(s)) hits.push([n, lang, 'wrong / old name', String(w), s.slice(0, 80)]);
      for (const w of OLD) if (w.test(s) && !OLD_OK.test(s)) hits.push([n, lang, 'old denominator (v1.1 F1)', String(w), s.slice(0, 80)]);
      for (const w of OLD12) if (w.test(s)) hits.push([n, lang, 'old wording (v1.2 G2)', String(w), s.slice(0, 80)]);
      if (SEP.test(s) && !SEP_OK.test(s)) hits.push([n, lang, 'flat "cannot be told apart" (v1.2 G7)', s.slice(0, 80)]);
      if (G.test(s) && n < 17 && !neg.test(s)) hits.push([n, lang, 'evaluation-function words outside G / H', s.slice(0, 80)]);
      if (MEM.test(s) && !MEM_OK.includes(n)) hits.push([n, lang, 'memory words outside the L3 screens (E0 / G / H)', s.slice(0, 80)]); } }
  api.goto(0, {silent: true}); api.setLang(document.documentElement.lang === 'en' ? 'en' : 'ja', true);
  return hits; })"""
names = [["wait", 1200],
         ["eval", f"(() => {{ const h = {SCAN}(null); if (h.length) throw new Error('names: ' + JSON.stringify(h.slice(0, 6))); return JSON.stringify({{names_ok: true, hits: 0, scanned: window.__sh.nstate * 2}}); }})()"],
         ["eval", f"(() => {{ const a = {SCAN}({{lang: 'ja', text: 'OLMo が考えた。'}}), b = {SCAN}({{lang: 'en', text: 'The model understood the figure.'}}), c = {SCAN}({{lang: 'ja', text: 'EQ(等距離)は一般には偽'}}), d = {SCAN}({{lang: 'ja', text: '評価関数は導出できる。'}}), e = {SCAN}({{lang: 'en', text: 'It comes from memory, as remembered.'}}), f = {SCAN}({{lang: 'ja', text: '四腕の折り返しの退け 43 / 47。'}}), g = {SCAN}({{lang: 'en', text: 'rejects olm125 15 / 15 · olm124 11 / 14 · olm119 11 / 12.'}}), h = {SCAN}({{lang: 'ja', text: 'RESULT の 43 / 47 は棚卸しの述語で再現できず、据えない。'}}), i = {SCAN}({{lang: 'ja', text: '橙 = MIDO3(共線・中点・この図では偽)'}}), j = {SCAN}({{lang: 'ja', text: '60 行ずつでは隣と分けられない。'}}), k = {SCAN}({{lang: 'en', text: 'With 60 rows, neighbours cannot be told apart.'}}), l = {SCAN}({{lang: 'ja', text: '「分けられない」とは言い切らない。'}}), m = {SCAN}({{lang: 'en', text: 'MIDO3 (collinear; false here)'}}); const base = {SCAN}(null).length, ok = [a, b, c, d, e, f, i, j, k, m].every((x) => x.length > base) && g.length >= base + 3 && h.length === base && l.length === base; if (!ok) throw new Error('positive control missed: ' + JSON.stringify([a.length, b.length, c.length, d.length, e.length, f.length, g.length, h.length, i.length, j.length, k.length, l.length, m.length, base])); return JSON.stringify({{names_positive_control_ok: true, caught: [a.length, b.length, c.length, d.length, e.length, f.length, g.length, i.length, j.length, k.length, m.length], negated_passes: h.length === base && l.length === base, baseline: base}}); }})()"]]
write("check_names.json", names)

cap = (HERE / "captures").as_posix()
V = cfg["frames"]["video"]
video = [["wait", 1500]]
for i in range(NS):
    video += [goto(i), ["wait", 450], ["shot", f"{cap}/video_s{i}.png", "html", 1, [0, 0, V[0], V[1]]]]
video += [goto(8), ["wait", 300], ["eval", "window.__sh.setRow('olm125:b1_j17'); 's8a'"], ["wait", 300], ["shot", f"{cap}/video_s8a.png", "html", 1, [0, 0, V[0], V[1]]],
          ["drag", ".fig-svg", 0.3, 0.45, 0.62, 0.6, 14], ["wait", 400], ["shot", f"{cap}/video_s8b.png", "html", 1, [0, 0, V[0], V[1]]]]
write("capture_video.json", video)
write("capture_video_en.json", [["wait", 1500]] + [x for i in (0, 1, 6, 8, 9, 13, 19) for x in (goto(i), ["wait", 450], ["shot", f"{cap}/video_en_s{i}.png", "html", 1, [0, 0, V[0], V[1]]])])
desk = lambda tag, sts: [["wait", 1500]] + [x for i in sts for x in (goto(i), ["wait", 450], ["eval", "scrollTo(0, 0); 'top'"], ["shot", f"{cap}/{tag}_s{i}.png", ".sh", 1])]
write("capture_desk_dark.json", desk("page_dark", range(NS)))
write("capture_desk_light.json", desk("page_light", [0, 1, 6, 8, 9, 12, 15, 19]))
write("capture_desk_en.json", [["wait", 1500]] + [x for i in (0, 1, 6, 8, 9, 15, 19) for x in (goto(i), ["wait", 450], ["eval", "scrollTo(0, 0); 'top'"], ["shot", f"{cap}/page_dark_s{i}_en.png", ".sh", 1])])
write("capture_phone.json", desk("phone_dark", range(NS)))
print(f"wrote check_states ({len(states)} steps) · check_robust · check_chapters ({len(chap)} steps) · check_drag · check_names · captures → {OUT} · {NS} states · groups {GROUPS}")
