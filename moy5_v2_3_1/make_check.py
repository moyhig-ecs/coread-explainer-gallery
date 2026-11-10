"""make_check.py — writes the action files that drive headless Chrome (the `anatomy` skill's scripts/drive.mjs). Everything is read from config.json (the numbers of the states live there).
  check_states.json    every state: goto, wait, MEASURE (smallest text in px vs config minpx for this frame · text outside the viewBox · NaN in a path · overlapping texts)
  check_robust.json    every state x both languages x P_x positions in {0, 3, 99, -5}: any throw fails
  check_chapters.json  REAL clicks on the chapter buttons, last chapter first; then a numbered step; then a click on a group of the map (state 3) that must open its chapter
  check_scan.json      every state x ja / en: the page's whole text is scanned for the words this figure does not use (README §Words), with a positive control (a planted phrase must be caught, a clean one must not)
  check_pagevraw.json  every state: the dots each strip DRAWS (data-dots) must equal the dots recounted from the raw jsonl by check_claims.expected_dots (route 4: page vs raw), and a few readouts must carry the raw numbers
  check_capture_<frame>.json  the stills (video 1920 x 1080 · desk dark / light · phone dark), every state; state 0 also with P_x moved (a / b)
Usage:   python -I make_check.py <dir>      then   sh run_checks.sh
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_claims  # noqa: E402  (our own file: its main does not run on import)

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "checks").resolve()
OUT.mkdir(parents=True, exist_ok=True)
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
CH, MINPX = cfg["chapters"], cfg["minpx"]
NS = CH[-1][2] + 1
GROUPS = [b - a + 1 for _, a, b in CH]
goto = lambda i: ["eval", f"window.__sh.goto({i}); 'state {i}'"]
write = lambda name, steps: (OUT / name).write_text(json.dumps(steps, ensure_ascii=False, indent=1), encoding="utf-8")

MEASURE = r"""(() => {
  const MIN = __MINPX__, sh = document.querySelector('.sh'), svg = sh.querySelector('.fig-svg'), bad = [];
  const video = sh.dataset.video === '1', layout = video ? 'video' : innerWidth <= 700 ? 'phone' : 'desk';
  if (sh.dataset.mode === 'ledger') { const arts = [...sh.querySelectorAll('.fig-ledger article')], px = arts.map((a) => parseFloat(getComputedStyle(a).fontSize)); const r = sh.querySelector('.fig-ledger').getBoundingClientRect();
    if (!arts.length) bad.push('empty ledger'); if (Math.min(...px) < MIN[layout]) bad.push(['ledger text below the minimum', Math.min(...px)]); if (video && r.bottom > innerHeight + 1) bad.push(['the ledger runs below the 1080 frame', Math.round(r.bottom)]);
    const out = {measure_ok: bad.length === 0, state: sh.dataset.state, layout, ledger_items: arts.length, minpx: Math.min(...px), bad}; if (bad.length) throw new Error('measure: ' + JSON.stringify(out)); return JSON.stringify(out); }
  const tx = [...svg.querySelectorAll('text')], m = svg.getScreenCTM().a, px = tx.map((t) => parseFloat(getComputedStyle(t).fontSize) * m), minpx = tx.length ? Math.min(...px) : null;
  if (minpx !== null && minpx < MIN[layout]) bad.push(['the smallest text is below the minimum for this frame', layout, +minpx.toFixed(2), MIN[layout], tx[px.indexOf(minpx)].textContent.slice(0, 30)]);
  const vb = svg.viewBox.baseVal;
  tx.forEach((t) => { const b = t.getBBox(); if (b.width && (b.x < vb.x - 1 || b.y < vb.y - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y + b.height > vb.y + vb.height + 1)) bad.push(['text outside the viewBox', t.textContent.slice(0, 40)]); });
  if ([...svg.querySelectorAll('path')].some((p) => /NaN/.test(p.getAttribute('d') || ''))) bad.push(['NaN in a path']);
  // overlapping texts (bounding boxes that intersect by more than 2 px both ways), plane states only (the 3D states' tags move with the camera)
  if (sh.dataset.mode === 'plane') { const bx = tx.map((t) => t.getBBox()).filter((b) => b.width > 0); let ov = 0, ex = '';
    for (let i = 0; i < bx.length; i++) for (let j = i + 1; j < bx.length; j++) { const a = bx[i], b = bx[j]; if (a.x + a.width - 2 > b.x && b.x + b.width - 2 > a.x && a.y + a.height - 2 > b.y && b.y + b.height - 2 > a.y) { ov++; ex = ex || (tx[i].textContent.slice(0, 24) + ' | ' + tx[j].textContent.slice(0, 24)); } }
    if (ov) bad.push(['overlapping texts', ov, ex]); }
  const plate = sh.querySelector('.iso-plate').getBoundingClientRect(), page = sh.getBoundingClientRect();
  if (video && page.bottom > innerHeight + 1) bad.push(['the page runs below the 1080 frame', Math.round(page.bottom)]);
  // v2.1 (BRIEF v2.1 §2-8): the box of the page is always inside (height 100vh, overflow hidden) = v2's check could not see the clipped last line. Measure the LAST LINE itself.
  const nc = sh.querySelector('.sh-notclaimed').getBoundingClientRect(); if (video && nc.bottom > Math.min(innerHeight, page.bottom) + 1) bad.push(['the last line ("what this figure does not say") is clipped by the 1080 frame', Math.round(nc.bottom), Math.round(Math.min(innerHeight, page.bottom))]);
  // v2.1: the plate's corner stamp (HTML over the svg) must not sit on a text of the figure or on the top line of a band (found on the stills of 23 · 25 · 26 while making v2.1)
  if (sh.dataset.mode === 'plane') { const c = sh.querySelector('[data-corner="title"]').getBoundingClientRect();
    tx.forEach((t) => { const r = t.getBoundingClientRect(); if (r.width > 0 && r.left < c.right && r.right > c.left && r.top < c.bottom - 1 && r.bottom > c.top + 1) bad.push(['a text under the corner stamp', t.textContent.slice(0, 30)]); });
    svg.querySelectorAll('.after-band, .next-band').forEach((e) => { const r = e.getBoundingClientRect(); if (r.left < c.right && r.right > c.left && r.top > c.top && r.top < c.bottom - 1) bad.push(['a band line crosses the corner stamp', Math.round(r.top)]); }); }
  // v2.1: the card pill: present on every state, and the 10-28 states (0-22) read no card frozen after 10-28
  const pill = sh.querySelector('[data-pill]'), pc = (pill && pill.dataset.cards || '').split(' ').filter(Boolean); if (!pill || !pill.textContent.trim()) bad.push('no card pill');
  if (Number(sh.dataset.state) <= 22 && pc.some((c) => /^(olm6[0-9]|olm7[0-9]|olm8[0-9]|thk[0-9])$/.test(c))) bad.push(['a card after 10-28 on a 10-28 state', pc.join(' ')]);
  const out = {measure_ok: bad.length === 0, state: sh.dataset.state, layout, texts: tx.length, minpx: minpx === null ? null : +minpx.toFixed(2), bad};
  if (bad.length) throw new Error('measure: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__MINPX__", json.dumps(MINPX))

ROBUST = r"""(() => { const api = window.__sh, out = {combos: 0, errors: 0, msgs: []};
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true});
    for (const lang of ['ja', 'en']) { api.setLang(lang, true); for (const cone of [true, false]) { api.setCone(cone, true); for (const t of [0, 3, 99, -5]) { try { api.setT(t, true); out.combos++; } catch (e) { out.errors++; out.msgs.push(n + ' ' + lang + ' ' + cone + ' ' + t + ': ' + e.message); } } } } }
  api.goto(0, {instant: true, silent: true}); api.setLang('ja', true); api.setCone(true, true);
  if (out.errors) throw new Error('robust: ' + JSON.stringify(out)); return JSON.stringify(out); })()"""


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
  const out = {chapters_ok: bad.length === 0, clicks: chk.map((r) => r.click + ' -> ' + r.state + ' [' + r.label + ']'), step_groups: grp, bad}; if (bad.length) throw new Error('chapters: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__GROUPS__", json.dumps(GROUPS)).replace("__N__", str(NS)).replace("__CH__", json.dumps([[c, a] for c, a, _ in CH]))

# ---- the words this figure does not use (BRIEF v1 §3 + the skill's wording.md). "誘導" may appear only in the label of chapter B (the PI's word, as a chapter title).
FORBID = {
    "ja": ["看破", "知らない", "知っている", "知って", "ひらめ", "気づ", "気付", "考えた", "迷っ", "理解した", "理解を", "model の心", "モデルの心", "の心が", "誘導に成功", "全 model", "全model", "全モデル", "作図を再現", "沈んだ", "見抜", "判定に届", "冷間"],   # v2.1: G-08 and BRIEF v2.1 §2-8
    "en": [r"\bknows?\b", r"\bknew\b", r"\brealiz", r"\bunderst(ood|ands?)\b", r"\bthought\b", r"\binsight", r"\bhesitat", r"\bnoticed\b", r"\bmind\b", r"\ball models\b", r"\breproduc\w* (the )?Menaechmus", r"\bsuccessfully guided\b", r"\bguided\b", r"\bsees? through\b", r"\breached a verdict\b", r"\bcold readers?\b"],
}
SCAN = r"""(() => { const api = window.__sh, F = __FORBID__, out = {pages: 0, hits: [], control: null};
  const re = { ja: F.ja.map((w) => new RegExp(w)), en: F.en.map((w) => new RegExp(w, 'i')) };
  const scan = (txt, lang) => re[lang].filter((r) => r.test(txt)).map((r) => r.source);
  // positive control of the scanner itself: planted phrases must be caught, clean ones must not
  const ctl = { ja_hit: scan('Opus は比例中項を知らないので床で止まる', 'ja').length > 0, en_hit: scan('the model knew the mean proportional', 'en').length > 0, ja_clean: scan('答えの欄は床のまま。理由の欄に cut。', 'ja').length === 0, en_clean: scan('the answer field stays on the floor; knowledge arms', 'en').length === 0 };
  out.control = ctl; if (!Object.values(ctl).every(Boolean)) throw new Error('scan control failed: ' + JSON.stringify(ctl));
  const sh = document.querySelector('.sh');
  for (const lang of ['ja', 'en']) { api.setLang(lang, true);
    for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true}); out.pages++;
      const chapB = sh.querySelector('.sh-chap[data-chap="B"]'), keep = chapB.textContent; chapB.textContent = '';
      const txt = sh.innerText + ' ' + [...sh.querySelectorAll('svg text')].map((t) => t.textContent).join(' ');
      chapB.textContent = keep;
      const h = scan(txt, lang); if (lang === 'ja' && /誘導/.test(txt)) h.push('誘導 outside chapter B');
      if (h.length) out.hits.push([lang, n, h]); } }
  api.setLang('ja', true); api.goto(0, {instant: true, silent: true});
  if (out.hits.length) throw new Error('scan: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__FORBID__", json.dumps(FORBID, ensure_ascii=False))

# ---- page vs raw (route 4): the dots each strip draws vs the dots recounted from the raw jsonl here; and readouts that must carry raw numbers
pack = json.loads((HERE / "generated" / "pack.json").read_text(encoding="utf-8"))
EXPECT = {cid: check_claims.expected_dots(c) for cid, c in pack["cells"].items()}
def cnt(files, model, arm, field):
    return sum(bool(r.get(field)) for f in files for r in check_claims.rows_of(f) if r.get("model") == model and r.get("arm") == arm and r.get("raw"))
N6O = ["results_neq6_moy5_20261019_claude-opus-5-5.jsonl"]; N3O = ["results_neq3_moy5_20261019_claude-opus-5-5.jsonl"]; N3F = ["results_neq3_moy5_20261019_claude-fable-5-1.jsonl"]
P3 = ["results_prf3_20261021.jsonl"]
READOUTS = {
    "10": f"medium {cnt(N6O, 'claude-opus-5-5', 'A/Q2@medium', 'cut_in_conjecture')} · high {cnt(N6O, 'claude-opus-5-5', 'A/Q2@high', 'cut_in_conjecture')} · max {cnt(N6O, 'claude-opus-5-5', 'A/Q2@max', 'cut_in_conjecture')} ‖ xhigh {cnt(N3O, 'claude-opus-5-5', 'A/Q2', 'cut_in_conjecture')}",
    "8": f"Opus {cnt(N3O, 'claude-opus-5-5', 'A', 'cut_in_conjecture')} → {cnt(N3O, 'claude-opus-5-5', 'A/Q2', 'cut_in_conjecture')}",
    "18": f"Opus {cnt(P3, 'claude-opus-5-5', 'P5', 'lat_sym')} → {cnt(P3, 'claude-opus-5-5', 'P5B', 'lat_sym')} · Fable {cnt(P3, 'claude-fable-5-1', 'P5', 'lat_sym')} → {cnt(P3, 'claude-fable-5-1', 'P5B', 'lat_sym')}",
    "1": f"P5B: LAT_SYM {cnt(P3, 'claude-opus-5-5', 'P5B', 'lat_sym')} / 10",
}
import statistics
MED = {cid: statistics.median(r["reasoning_tokens"] for f in c["files"] for r in check_claims.rows_of(f) if r.get("arm") == c["arm"] and r.get("raw")) for cid, c in pack["cells"].items() if cid.startswith(("b5bp.Bbp", "arg5.Bbp", "arg5d.Bbp"))}
THK = [[bool(r["ans_cut"]), bool(r["summ_cut"])] for m in ("opus-5-5", "fable-5-1") for r in check_claims.rows_of(f"results_thk2_moy5_20261030_claude-{m}.jsonl")]
PAGEVRAW = r"""(() => { const api = window.__sh, E = __EXPECT__, R = __READ__, MED = __MED__, THK = __THK__, seen = {}, bad = [];
  api.setLang('ja', true);
  for (let n = 0; n < api.nstate; n++) { api.goto(n, {instant: true, silent: true});
    document.querySelectorAll('.strip[data-cell]').forEach((g) => { const id = g.dataset.cell, d = g.dataset.dots, drawn = g.querySelectorAll('.dt:not(.hl)').length; seen[id] = (seen[id] || 0) + 1; if (E[id] !== d) bad.push(['dots differ', n, id, d, E[id]]); if (!drawn) bad.push(['no dot drawn', n, id]); });
    document.querySelectorAll('.tm[data-cell]').forEach((g) => { seen['med:' + g.dataset.cell] = 1; if (Number(g.dataset.med) !== MED[g.dataset.cell]) bad.push(['thinking median', n, g.dataset.cell, g.dataset.med, MED[g.dataset.cell]]); });
    const tk = [...document.querySelectorAll('.thk-row')].map((g) => [g.dataset.ans === 'true', g.dataset.summ === 'true']); if (tk.length && JSON.stringify(tk) !== JSON.stringify(THK)) bad.push(['thk2 rows', n, JSON.stringify(tk)]);
    const ro = document.querySelector('[data-readout]').textContent; if (R[String(n)] && !ro.includes(R[String(n)])) bad.push(['readout', n, ro, R[String(n)]]); }
  api.goto(0, {instant: true, silent: true});
  const out = {pagevraw_ok: bad.length === 0, strips_checked: Object.values(seen).reduce((a, b) => a + b, 0), cells_seen: Object.keys(seen).length, readouts: Object.keys(R).length, bad: bad.slice(0, 6)};
  if (bad.length) throw new Error('page vs raw: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__EXPECT__", json.dumps(EXPECT)).replace("__READ__", json.dumps(READOUTS, ensure_ascii=False)).replace("__MED__", json.dumps(MED)).replace("__THK__", json.dumps(THK))
# the page-vs-raw instrument is calibrated too: a planted wrong expectation must be caught
PAGEVRAW_CTL = PAGEVRAW.replace("const api = window.__sh, E = ", "const api = window.__sh, E0 = ").replace(", R = ", ", E = Object.assign({}, E0, {'prf3.P5B.opus': 'SSSSSSSSSS'}), R = ", 1).replace("if (bad.length) throw new Error('page vs raw: ' + JSON.stringify(out)); return JSON.stringify(out);", "if (!bad.some((b) => b[2] === 'prf3.P5B.opus')) throw new Error('page vs raw control: the planted wrong value was not caught'); return JSON.stringify({pagevraw_control_ok: true, caught: bad.length});")

SETTLE = ["eval", "window.__sh.goto(window.__sh.state, {instant: true, silent: true}); 'settled'"]
states = [["wait", 1500]]
for i in range(NS):
    states += [goto(i), ["wait", 1300], SETTLE, ["wait", 150], ["eval", MEASURE]]   # v2.1: settle the camera before measuring (under load the 0.6 s follow had not ended at 1.3 s: state 10's axis labels were read mid-turn)
write("check_states.json", states)
write("check_robust.json", [["wait", 1500], ["eval", ROBUST], ["wait", 500], goto(0), ["wait", 800]])
write("check_scan.json", [["wait", 1500], ["eval", SCAN]])
write("check_pagevraw.json", [["wait", 1500], ["eval", PAGEVRAW], ["eval", PAGEVRAW_CTL]])
order = [c for c, _, _ in reversed(CH)]
chap = [["wait", 1500], ["eval", "window.__chk = []; 'chapter check: start'"], goto(0), ["wait", 600]]
for name in order:
    first = next(a for c, a, _ in CH if c == name)
    chap += [["click", f'.sh-chap[data-chap="{name}"]'], ["wait", 700], ["eval", rec(name, first)]]
mid = NS - 1
chap += [["click", f'.sh-step[data-n="{mid}"]'], ["wait", 700], ["eval", rec(f"step {mid}", mid)]]
chap += [goto(3), ["wait", 900], ["click", '.mapgrp[data-goto="15"] .pl.h'], ["wait", 800], ["eval", rec("map group G (state 3)", 15)]]
chap += [goto(23), ["wait", 900], ["click", '.flow-grp[data-goto="25"] .pl.h'], ["wait", 800], ["eval", rec("flow group b (state 23)", 25)]]
chap += [goto(27), ["wait", 900], ["click", '.n4[data-goto="13"] .pl.h'], ["wait", 800], ["eval", rec("next bundle 2 (state 27)", 13)], ["eval", VERDICT]]
write("check_chapters.json", chap)
cap = str(HERE / "captures")
FR = cfg["frames"]
def capture(frame, fname, extra=()):
    steps = [["wait", 2200]]
    for i in range(NS):
        steps += [goto(i), ["wait", 1500], SETTLE, ["wait", 200], ["shot", f"{cap}/{fname(i)}", "html" if frame == "video" else ".sh", 1] + ([[0, 0, FR["video"][0], FR["video"][1]]] if frame == "video" else [])]
    steps += list(extra)
    return steps
mv = lambda t, nm, frame: [goto(0), ["wait", 900], ["eval", f"window.__sh.setT({t}); 't {t}'"], ["wait", 900], ["shot", f"{cap}/{nm}", "html" if frame == "video" else ".sh", 1] + ([[0, 0, FR["video"][0], FR["video"][1]]] if frame == "video" else [])]
write("check_capture_video.json", capture("video", lambda i: f"video_s{i}.png", mv(-5, "video_s0a.png", "video") + mv(5, "video_s0b.png", "video")))
write("check_capture_desk.json", capture("desk", lambda i: f"page_dark_s{i}.png"))
write("check_capture_light.json", capture("desk", lambda i: f"page_light_s{i}.png"))
write("check_capture_phone.json", capture("phone", lambda i: f"phone_dark_s{i}.png"))
# ---- v2.1: the fit of the 1080 frame has a positive control (the v2 clipping must be caught when the fit is off), and the parts this version added are checked on the page
LASTLINE = "(() => { const sh = document.querySelector('.sh'), nc = sh.querySelector('.sh-notclaimed').getBoundingClientRect(), pb = sh.getBoundingClientRect().bottom; return {state: sh.dataset.state, bottom: Math.round(nc.bottom), limit: Math.round(Math.min(innerHeight, pb)), clipped: nc.bottom > Math.min(innerHeight, pb) + 1}; })()"
FITCTL = [["wait", 1500], ["eval", "window.__sh.fit(false); window.__sh.goto(24, {instant: true}); 'fit off'"], ["wait", 900],
          ["eval", f"(() => {{ const r = {LASTLINE}; if (!r.clipped) throw new Error('fit control: with the fit OFF the v2 clipping of state 24 was not caught ' + JSON.stringify(r)); return JSON.stringify({{fit_control_caught: true, off: r}}); }})()"],
          ["eval", "window.__sh.fit(true); window.__sh.goto(25, {instant: true}); window.__sh.goto(24, {instant: true}); 'fit on'"], ["wait", 900],
          ["eval", f"(() => {{ const r = {LASTLINE}; if (r.clipped) throw new Error('fit: state 24 is still clipped ' + JSON.stringify(r)); return JSON.stringify({{fit_ok: true, on: r}}); }})()"]]
write("check_fit_control.json", FITCTL)
G = pack["post_tally"]["grade"]
V21 = r"""(() => { const api = window.__sh, bad = [], G = __G__, out = {};
  api.setLang('ja', true); api.goto(23, {instant: true, silent: true});
  const ro = document.querySelector('[data-readout]').textContent, want = `判定 ${G['判定']} · 記述 ${G['記述']} · 較正 ${G['較正']} · 言えない ${G['言えない']} · 関門で止まった ${G['関門']}`;
  if (!ro.includes(want)) bad.push(['state 23 readout', ro]); const sum = Object.values(G).reduce((a, b) => a + b, 0); if (sum !== 20) bad.push(['the five columns do not sum to 20', sum]);
  const chips = [...document.querySelectorAll('.fig-svg rect.chip')].map((r) => r.getAttribute('class').split('chip-')[1]); out.flow_chips = chips.length; if (chips.length !== 20) bad.push(['flow chips', chips.length]);
  const byS = {}; chips.forEach((c) => (byS[c] = (byS[c] || 0) + 1)); const want5 = {verdict: G['判定'], desc: G['記述'], cal: G['較正'], cannot: G['言えない'], gate: G['関門']};
  for (const [k, v] of Object.entries(want5)) if ((byS[k] || 0) !== v) bad.push(['flow marks of ' + k, byS[k] || 0, v]);
  if (/判定に届/.test(document.querySelector('.sh').innerText)) bad.push('the word 判定に届いた is back (G-08)');
  let rowsN = 0; const rs = {}; for (const n of [24, 25, 26]) { api.goto(n, {instant: true, silent: true}); document.querySelectorAll('.post-row').forEach((g) => { rowsN++; rs[g.dataset.status] = (rs[g.dataset.status] || 0) + 1; }); }
  out.post_rows = rowsN; if (rowsN !== 20) bad.push(['post rows over states 24-26', rowsN]); for (const [k, v] of Object.entries(want5)) if ((rs[k] || 0) !== v) bad.push(['post rows of ' + k, rs[k] || 0, v]);
  api.goto(24, {instant: true, silent: true}); if (!document.querySelector('.posthoc-line')) bad.push('state 24: no post-hoc dashed line (olm67 Q2)');
  api.goto(27, {instant: true, silent: true}); const home = [...document.querySelectorAll('.n4[data-home="1"]')]; out.home = home.map((g) => g.dataset.n);
  if (home.length !== 1 || home[0] !== document.querySelector('.n4')) bad.push(['bundle 1 must be the only one marked', home.length]);
  if (/冷間/.test(document.querySelector('.sh').innerText)) bad.push('state 27: the word 冷間 (BRIEF v2.1 §2-8)');
  api.goto(4, {instant: true, silent: true}); out.road_others = document.querySelectorAll('.road-others').length; if (out.road_others !== 2) bad.push(['state 4 other-model lines', out.road_others]);
  if (!/10-28 の entry P/.test(document.querySelector('[data-corner="title"] .sh-corner2').textContent)) bad.push('state 4 stamp: 10-28 の entry P');
  out.pill17 = api.cards(17).join(' '); if (out.pill17 !== 'prf1 SOURCE 10-14') bad.push(['state 17 pill (decision 3)', out.pill17]);
  for (let n = 0; n <= 22; n++) if (api.cards(n).some((c) => /^(olm6|olm7|olm8|thk)/.test(c))) bad.push(['a card after 10-28 on state', n]);
  api.setLang('en', true); api.goto(23, {instant: true, silent: true}); if (/reached a verdict/.test(document.querySelector('.sh').innerText)) bad.push('en: reached a verdict');
  api.setLang('ja', true); api.goto(0, {instant: true, silent: true});
  out.v21_ok = bad.length === 0; out.bad = bad; if (bad.length) throw new Error('v21: ' + JSON.stringify(out)); return JSON.stringify(out); })()""".replace("__G__", json.dumps(G, ensure_ascii=False))
write("check_v21.json", [["wait", 1500], ["eval", V21]])
# ---- v2.2 (BRIEF v2.2 §2-4): the overlay on the board states (0 and 7), shown and hidden. Each side passes MEASURE (the 1080 frame and its last line on video); the toggle there and back changes
#      no text (kicker, question, lead, readout, chips, limits, the last line, the card pill); the overlay is drawn when on and absent when off; at t = 0 it stays inside the viewBox;
#      the geometry of BRIEF v2.2 §1 holds on the coordinates (FIGURE.coneCheck, t = -6 .. 6). Positive controls: the text comparator must see the difference between states 0 and 7,
#      and the cone test must REJECT the board's P_y (folded, height 0) while it accepts the lifted one.
TXT = "(() => { const sh = document.querySelector('.sh'), q = (s) => (sh.querySelector(s) || {}).textContent || ''; return JSON.stringify([q('.sh-kicker'), q('.sh-q'), q('.sh-lead'), q('[data-readout]'), q('.sh-panel'), q('.sh-lim'), q('.sh-notclaimed'), q('[data-pill]'), q('.sh-corner2')]); })()"
OVL = "(() => { const g = document.querySelector('.cone-overlay'); if (!g) return {on: false}; const b = g.getBBox(), v = document.querySelector('.fig-svg').viewBox.baseVal; return {on: true, parts: g.children.length, inside: b.x >= v.x - 1 && b.y >= v.y - 1 && b.x + b.width <= v.x + v.width + 1 && b.y + b.height <= v.y + v.height + 1, bb: [b.x, b.y, b.x + b.width, b.y + b.height].map(Math.round)}; })()"
GEOM = r"""(() => { const F = window.__figure, bad = window.__sh.cone === true ? [] : [['the overlay is not on by default', window.__sh.cone]], tol = {C_on_f: 1e-3, C_on_g: 1e-3, F_antipode_of_G: 1e-3, GE_perp_axis: 1e-3, j_tangent_at_F: 1e-3, Py_on_cone: 1e-4, Py_on_circle_through_J: 1e-3, symptoma: 1e-3}; let worst = {};
  for (let t = -6; t <= 6; t++) { const r = F.coneCheck(t); for (const [k, v] of Object.entries(tol)) { worst[k] = Math.max(worst[k] || 0, r[k]); if (!(r[k] < v)) bad.push([t, k, r[k]]); } if (Math.abs(r.half_angle_deg - 30) > 1e-4) bad.push([t, 'half angle', r.half_angle_deg]); }
  const K = F.CONE, g = F.construct(F.PxAt(0)), w = [g.P_y[0] - K.C[0], g.P_y[1] - K.C[1]], along = w[0] * K.ax[0] + w[1] * K.ax[1], rad = Math.hypot(w[0] - K.ax[0] * along, w[1] - K.ax[1] * along), folded = Math.abs(Math.atan2(rad, along) - K.al);
  if (!(folded > 1e-2)) bad.push(['control: the board P_y (folded, height 0) was accepted as on the cone', folded]);
  const out = {geom_ok: bad.length === 0, worst, half_angle_deg: F.coneCheck(0).half_angle_deg, control_folded_Py_off_cone: +folded.toFixed(4), bad}; if (bad.length) throw new Error('v22 geometry: ' + JSON.stringify(out)); return JSON.stringify(out); })()"""
def v22_state(n):
    chk = lambda want, tag: f"(() => {{ const o = {OVL}, t = {TXT}, k = [...document.querySelectorAll('.sh-key')].map((e) => e.textContent).join(' | '), base = window.__v22txt[{n}], bad = [];"\
          f" if (o.on !== {str(want).lower()}) bad.push(['overlay drawn', o.on]); if (o.on && !o.inside) bad.push(['the overlay leaves the viewBox at t = 0', o.bb]); if (o.on && o.parts < 12) bad.push(['overlay parts', o.parts]);"\
          f" if (t !== base) bad.push(['a text changed with the toggle', t.slice(0, 200)]); if (document.querySelectorAll('.pl.linel').length !== 5) bad.push(['line names', document.querySelectorAll('.pl.linel').length]);"\
          f" if ({str(want).lower()} !== /Dandelin/.test(k)) bad.push(['overlay keys', k.slice(0, 120)]); if (window.__sh.cone !== {str(want).lower()}) bad.push(['api.cone', window.__sh.cone]);"\
          f" const out = {{v22_ok: bad.length === 0, state: {n}, step: {json.dumps(tag)}, overlay: o, bad}}; if (bad.length) throw new Error('v22: ' + JSON.stringify(out)); return JSON.stringify(out); }})()"
    return [goto(n), ["wait", 1300], ["eval", "window.__sh.setCone(true, true); window.__sh.setT(0, true); 'cone on'"], SETTLE, ["wait", 300], ["eval", f"(window.__v22txt = window.__v22txt || {{}})[{n}] = {TXT}; 'texts kept'"],
            ["eval", chk(True, "on")], ["eval", MEASURE],
            ["eval", "window.__sh.setCone(false); 'cone off'"], ["wait", 400], ["eval", chk(False, "off")], ["eval", MEASURE],
            ["eval", "window.__sh.setCone(true); 'cone on again'"], ["wait", 400], ["eval", chk(True, "on again")], ["eval", MEASURE]]
TXTCTL = f"(() => {{ window.__sh.goto(0, {{instant: true, silent: true}}); const a = {TXT}; window.__sh.goto(7, {{instant: true, silent: true}}); const b = {TXT}; if (a === b) throw new Error('v22 control: the text comparator did not see states 0 and 7 differ'); window.__sh.goto(0, {{instant: true, silent: true}}); return JSON.stringify({{v22_text_control_ok: true}}); }})()"
V22 = [["wait", 1500], ["eval", GEOM], ["eval", TXTCTL]] + v22_state(0) + v22_state(7) + [goto(0), ["wait", 600]]
write("check_v22.json", V22)
# real clicks on the page's button (desk / phone; the video frame hides the bar): shown on states 0 and 7 only, and it flips the overlay
CLK = lambda want: f"(() => {{ const b = document.querySelector('.sh-cone'), on = !!document.querySelector('.cone-overlay'); if (on !== {str(want).lower()} || b.getAttribute('aria-pressed') !== '{str(want).lower()}') throw new Error('v22 click: overlay ' + on + ' pressed ' + b.getAttribute('aria-pressed')); return JSON.stringify({{v22_click_ok: true, overlay: on, pressed: b.getAttribute('aria-pressed'), label: b.textContent}}); }})()"
HID = "(() => { const b = document.querySelector('.sh-cone'); if (getComputedStyle(b).display !== 'none') throw new Error('v22: the cone button shows on state ' + window.__sh.state); return JSON.stringify({v22_hidden_ok: true, state: window.__sh.state}); })()"
write("check_v22_click.json", [["wait", 1500], goto(0), ["wait", 900], ["eval", CLK(True)], ["click", ".sh-cone"], ["wait", 500], ["eval", CLK(False)], ["click", ".sh-cone"], ["wait", 500], ["eval", CLK(True)],
                               goto(7), ["wait", 900], ["click", ".sh-cone"], ["wait", 500], ["eval", CLK(False)], ["click", ".sh-cone"], ["wait", 500], ["eval", CLK(True)], goto(1), ["wait", 600], ["eval", HID], goto(10), ["wait", 600], ["eval", HID]])
# the stills this version re-shoots: only the board states (0, 7; 0 with P_x moved), with the overlay on (default) and off
def cap22(suffix, extra_off=True, moved=True):
    shot = lambda nm: ["shot", f"{cap}/{nm}", "html", 1, [0, 0, FR["video"][0], FR["video"][1]]]
    st = [["wait", 2200]]
    for n in (0, 7):
        st += [goto(n), ["eval", "window.__sh.setCone(true, true); 'on'"], ["wait", 1500], SETTLE, ["wait", 200], shot(f"video_s{n}{suffix}.png")]
        if extra_off and (n == 0 or suffix == ""):
            st += [["eval", "window.__sh.setCone(false, true); 'off'"], ["wait", 600], shot(f"video_s{n}_off{suffix}.png"), ["eval", "window.__sh.setCone(true, true); 'on'"]]
    st += [goto(29), ["wait", 1500], SETTLE, ["wait", 200], shot(f"video_s29{suffix}.png")]   # the ledger 2/3: its 'cannot say' row got one sentence about the overlay (no row added)
    if moved:
        st += mv(-5, "video_s0a.png", "video") + mv(5, "video_s0b.png", "video")
    return st
write("check_capture_v22.json", cap22(""))
write("check_capture_v22_en.json", cap22("_en", moved=False))
# ---- v2.3 (BRIEF v2.3 §2-2 / §2-3): the cutting plane (through the line FVD = line j, perpendicular to the board) on the board states 0 and 7, inside the overlay (on / off with it).
#      GEOM23 = route 2 of the plane's numbers: FIGURE.planeCheck on what the page draws (cutPlane), t = -6 .. 6, against BRIEF v2.3 §1 and against the pack (route 1, DATA.construction.plane);
#        positive controls: three planted faults (one sample 1e-4 off the plane · the parabola from the question's rounded V · the plane leaned by 1e-3 rad) must be caught.
#      v23_state = what is DRAWN: one plane, one directrix, two rings (F, V) when on and none when off; the plane after the sphere and the contact circle and before the parabola (painter's order);
#        every vertex of the drawn parabola inside the drawn plane (screen, 0.5 unit) and the directrix from the bottom edge to the top edge; the four names in the plane (desk / video; none on the phone,
#        whose key line names them); no two texts of the figure overlap (t = 0; state 0 also at t = -5 / +5 = the stills 0a / 0b); no key line runs under a corner of the plate (HTML);
#        the key line of the plane present only while on. Positive controls: a planted point outside the plane, a planted copy of a name, and a corner against itself must be caught.
PLANE_KEY = {"ja": "切り口の面 = 直線 FVD(線 j)を通り、板に鉛直(作図・data でない)", "en": "the cutting plane = through the line FVD (line j), perpendicular to the board (drawing, not data)"}
GEOM23 = r"""(() => { const F = window.__figure, bad = [], worst = {}, tol = {V_off_j: [4.1e-5, 1e-6], D_off_j: [0, 1e-9], tV_over_tD: [0.500007, 1e-6], FV: [2.3094, 1e-4], FD: [4.6188, 1e-4], A_to_j: [4.000018, 1e-6], AF_dot_j: [0, 1e-9],
    par_off_plane: [0, 1e-6], par_on_cone: [0, 1e-4], plane_dot_board: [0, 1e-9], corners_off: [0, 1e-9], directrix_off: [0, 1e-9], plane_fixed: [0, 1e-12], lift_on_par: [0, 1e-3]};   // v2.3.1: the plane and the parabola do not move with P_x; P_y lifted stays on the parabola
  for (let t = -6; t <= 6; t++) { const r = F.planeCheck(t); for (const [k, [e, d]] of Object.entries(tol)) { const v = Math.abs(r[k] - e); worst[k] = Math.max(worst[k] || 0, k === 'tV_over_tD' || k === 'FV' || k === 'FD' || k === 'A_to_j' || k === 'V_off_j' ? r[k] : v); if (!(v <= d)) bad.push([t, k, r[k]]); }
    if (!(r.par_n >= 20)) bad.push([t, 'samples', r.par_n]); if (!r.par_inside) bad.push([t, 'a sample outside the drawn rectangle']); if (Math.abs(r.u[0] - 0.992546) > 1e-6 || Math.abs(r.u[1] - 0.121874) > 1e-6) bad.push([t, 'u', r.u]); }
  const r0 = F.planeCheck(0), pk = F.packPlane(), agree = {}; for (const k of Object.keys(pk)) { const a = k === 'u' ? Math.hypot(r0.u[0] - pk.u[0], r0.u[1] - pk.u[1]) : Math.abs(r0[k] - pk[k]); agree[k] = a; if (!(a < 1e-9)) bad.push(['the page and the pack differ', k, r0[k], pk[k]]); }
  const c1 = F.planeCheck(0, 'shift').par_off_plane, c2 = F.planeCheck(0, 'frozenV').par_off_plane, c3 = F.planeCheck(0, 'tilt').plane_dot_board, c4 = F.planeCheck(-5, 'grow').plane_fixed;
  if (!(c4 > 1e-12)) bad.push(['control (v2.3.1): a plane grown by 0.1 % was not caught', c4]); for (const t of [-6, -1]) if (!(F.planeCheck(t).ext_n > 0)) bad.push([t, 'no dashed run past the edge']); for (const t of [0, 2, 6]) if (F.planeCheck(t).ext_n !== 0) bad.push([t, 'a dashed run inside the plane']);
  if (!(c1 > 1e-6)) bad.push(['control: a sample 1e-4 off the plane was not caught', c1]); if (!(c2 > 1e-6)) bad.push(['control: the parabola from the rounded V was not caught', c2]); if (!(c3 > 1e-6)) bad.push(['control: a leaned plane was not caught', c3]);
  const out = {geom23_ok: bad.length === 0, at_t0: {u: r0.u, V_off_j: r0.V_off_j, D_off_j: r0.D_off_j, tV_over_tD: r0.tV_over_tD, FV: r0.FV, FD: r0.FD, A_to_j: r0.A_to_j, AF_dot_j: r0.AF_dot_j, par_n: r0.par_n, par_off_plane: r0.par_off_plane, par_on_cone: r0.par_on_cone, plane_dot_board: r0.plane_dot_board},
    worst_t: worst, pack_vs_page_max: Math.max(...Object.values(agree)), controls: {shift: c1, frozenV: c2, tilt: c3, grow: c4}, bad};
  if (bad.length) throw new Error('v23 geometry: ' + JSON.stringify(out)); return JSON.stringify(out); })()"""
DRAWN23 = r"""((want, tag) => { const sh = document.querySelector('.sh'), svg = sh.querySelector('.fig-svg'), g = svg.querySelector('.cone-overlay'), bad = [], ph = innerWidth <= 700 && sh.dataset.video !== '1', L = sh.dataset.lang || (document.documentElement.lang || 'ja');
  const nums = (d) => (d.match(/-?[\d.]+/g) || []).map(Number), pts = (d) => { const a = nums(d), o = []; for (let i = 0; i + 1 < a.length; i += 2) o.push([a[i], a[i + 1]]); return o; };
  const quadIn = (q, p, tol) => { let sgn = 0; for (let i = 0; i < 4; i++) { const a = q[i], b = q[(i + 1) % 4], c = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]), d = c / Math.hypot(b[0] - a[0], b[1] - a[1]); if (d > tol) { if (sgn < 0) return false; sgn = sgn || 1; } else if (d < -tol) { if (sgn > 0) return false; sgn = sgn || -1; } } return true; };
  const keys = [...sh.querySelectorAll('.sh-key')].map((e) => e.textContent).join(' | '), KEY = __KEY__;
  const out = {state: Number(sh.dataset.state), step: tag, t: window.__sh.t || 0};
  if (!want) { if (g && g.querySelector('.cut-plane')) bad.push('the plane is drawn while the overlay is off'); if (svg.querySelector('.cut-plane, .cut-dir, .cut-pt, .pl.planel')) bad.push('a part of the plane outside the overlay'); if (keys.includes(KEY.ja) || keys.includes(KEY.en)) bad.push('the plane key line while off'); }
  else { const kids = [...g.children], ix = (c) => kids.findIndex((e) => e.classList.contains(c)), n = (c) => g.querySelectorAll('.' + c).length;
    if (n('cut-plane') !== 1 || n('cut-dir') !== 1 || n('cut-pt') !== 2) bad.push(['parts', n('cut-plane'), n('cut-dir'), n('cut-pt')]);
    if (!(ix('cut-plane') > ix('sphere-film') && ix('cut-plane') > ix('touch') && ix('cut-plane') < ix('cut-film') && ix('cut-plane') < ix('cut-line'))) bad.push(['painter order', ix('sphere-film'), ix('touch'), ix('cut-plane'), ix('cut-film'), ix('cut-line')]);
    const quad = pts(g.querySelector('.cut-plane').getAttribute('d')).slice(0, 4), par = pts(g.querySelector('.cut-line').getAttribute('d')), dir = pts(g.querySelector('.cut-dir').getAttribute('d'));
    const outside = par.filter((p) => !quadIn(quad, p, 0.5)); if (outside.length) bad.push(['parabola vertices outside the drawn plane', outside.length, outside[0]]);
    if (quadIn(quad, [quad[2][0] + 25, quad[2][1] - 25], 0.5) && quadIn(quad, [quad[0][0] - 25, quad[0][1] + 25], 0.5)) bad.push('control: points planted outside the plane were not caught');
    const onSeg = (p, a, b) => Math.abs((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])) / Math.hypot(b[0] - a[0], b[1] - a[1]) < 0.6; if (!(onSeg(dir[0], quad[0], quad[1]) && onSeg(dir[1], quad[3], quad[2]))) bad.push(['the directrix does not run from the bottom edge to the top edge', dir]);
    const names = [...svg.querySelectorAll('.pl.planel')].map((t) => t.textContent), want4 = L === 'en' ? ['the cutting plane', 'focus F', 'vertex V', 'directrix'] : ['切り口の面', '焦点 F', '頂点 V', '準線'];
    if (ph ? names.length !== 0 : names.sort().join('|') !== want4.slice().sort().join('|')) bad.push(['the names in the plane', names]);
    if (!keys.includes(KEY[L]) || (ph && !keys.includes(L === 'en' ? 'focus F' : '焦点 F'))) bad.push(['the plane key line', keys.slice(-200)]); out.quad = quad.map((p) => p.map(Math.round)); out.parabola_vertices = par.length; out.names = names;
    // v2.3.1: the drawn plane does not move with P_x (screen quad against the one drawn at t = 0 in the same state); the dashed run past the edge only at t < 0, starting where the parabola ends
    const tt = window.__sh.t || 0, ext = g.querySelectorAll('.cut-ext'); if (ext.length !== (tt < 0 ? 1 : 0)) bad.push(['the dashed run past the edge', ext.length, tt]);
    if (ext.length) { const e = pts(ext[0].getAttribute('d')), last = par[par.length - 1]; if (Math.hypot(e[0][0] - last[0], e[0][1] - last[1]) > 0.6) bad.push(['the dashed run does not start where the parabola ends', e[0], last]); out.ext_vertices = e.length; }
    if (tt === 0) { window.__quad0 = quad; window.__par0 = par; } else if (window.__quad0) { const d = Math.max(...quad.map((p, i) => Math.hypot(p[0] - window.__quad0[i][0], p[1] - window.__quad0[i][1])), ...par.map((p, i) => Math.hypot(p[0] - window.__par0[i][0], p[1] - window.__par0[i][1]))); out.moved_vs_t0 = d; if (d > 0.15) bad.push(['the plane or the parabola moved with P_x', d]); } }
  const tx = [...svg.querySelectorAll('text')].filter((t) => t.getBBox().width > 0), bx = tx.map((t) => t.getBBox()), ovl = (a, b) => a.x + a.width - 2 > b.x && b.x + b.width - 2 > a.x && a.y + a.height - 2 > b.y && b.y + b.height - 2 > a.y; let ov = [];
  const moved = (window.__sh.t || 0) !== 0, mine = (t) => t.classList.contains('planel');   // at a moved P_x only the plane's names are held to it (v2.2's point names already meet there on the phone: A | P_y, E | P_x at t = 5)
  for (let i = 0; i < bx.length; i++) for (let j = i + 1; j < bx.length; j++) if (ovl(bx[i], bx[j]) && (!moved || mine(tx[i]) || mine(tx[j]))) ov.push(tx[i].textContent.slice(0, 20) + ' | ' + tx[j].textContent.slice(0, 20));
  if (ov.length) bad.push(['overlapping texts in the figure', ov]); if (!(tx.length && ovl(bx[0], bx[0]))) bad.push('control: the overlap test did not catch a text against itself');
  const corners = [...sh.querySelectorAll('.iso-plate-corner')].map((e) => e.getBoundingClientRect()).filter((r) => r.width > 0 && r.height > 0), kr = [...sh.querySelectorAll('.sh-key')].map((e) => e.getBoundingClientRect()), hit = (a, b) => a.left < b.right - 1 && b.left < a.right - 1 && a.top < b.bottom - 1 && b.top < a.bottom - 1;
  const pk = [...sh.querySelectorAll('.sh-key')].filter((e) => e.querySelector('.sw-cplane, .sw-cplane_ph')).map((e) => e.getBoundingClientRect());   // the plane's key line (v2.2's own en lines touch the readout corner: desk 'on' / video 'off' = NOTES)
  const under = pk.filter((k) => corners.some((c) => hit(k, c))).length; if (under) bad.push(['the plane key line under a corner of the plate', under]); out.v22_key_lines_under_a_corner = kr.filter((k) => corners.some((c) => hit(k, c))).length; if (corners.length && !hit(corners[0], corners[0])) bad.push('control: the corner test did not catch a corner against itself');
  out.texts = tx.length; out.v23_ok = bad.length === 0; out.bad = bad; if (bad.length) throw new Error('v23: ' + JSON.stringify(out)); return JSON.stringify(out); })""".replace("__KEY__", json.dumps(PLANE_KEY, ensure_ascii=False))
def v23_state(n, moved=()):
    st = [goto(n), ["wait", 1300], ["eval", "window.__sh.setCone(true, true); window.__sh.setT(0, true); 'cone on'"], SETTLE, ["wait", 300], ["eval", DRAWN23 + "(true, 'on')"],
          ["eval", "window.__sh.setCone(false); 'cone off'"], ["wait", 400], ["eval", DRAWN23 + "(false, 'off')"], ["eval", "window.__sh.setCone(true); 'cone on again'"], ["wait", 400], ["eval", DRAWN23 + "(true, 'on again')"]]
    for t in moved:
        st += [["eval", f"window.__sh.setT({t}); 't {t}'"], ["wait", 700], ["eval", DRAWN23 + f"(true, 't {t}')"]]
    return st + [["eval", "window.__sh.setT(0, true); 't 0'"]]
write("check_v23.json", [["wait", 1500], ["eval", GEOM23]] + v23_state(0, moved=(-5, 5)) + v23_state(7) + [goto(0), ["wait", 600]])
# the stills v2.3 re-shoots (BRIEF v2.3 §2-4): the board states with the overlay (default = on) in video ja / en, and state 0 with P_x moved (0a / 0b, ja) — the others are copied from v2.2
def cap23(suffix, moved=True):
    shot = lambda nm: ["shot", f"{cap}/{nm}", "html", 1, [0, 0, FR["video"][0], FR["video"][1]]]
    st = [["wait", 2200]]
    for n in (0, 7):
        st += [goto(n), ["eval", "window.__sh.setCone(true, true); 'on'"], ["wait", 1500], SETTLE, ["wait", 200], shot(f"video_s{n}{suffix}.png")]
    if moved:
        st += mv(-5, "video_s0a.png", "video") + mv(5, "video_s0b.png", "video")
    return st
write("check_capture_v23.json", cap23(""))
write("check_capture_v23_en.json", cap23("_en", moved=False))
# v2.3 §2-3 "the plane changes no other page": a dump of every state x {cone on, and off on the board states} = a hash of the page's text and of the figure's svg, compared with a v2.2 build (compare_v22.py)
HASH = "((s) => { let h = 2166136261 >>> 0; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h.toString(16); })"
DUMP = lambda tag: ["eval", f"(() => {{ const sh = document.querySelector('.sh'), H = {HASH}; return 'dump23 ' + JSON.stringify({{state: Number(sh.dataset.state), cone: window.__sh.cone, tag: '{tag}', text: H(sh.innerText), svg: H(sh.querySelector('.fig-svg').outerHTML), keys: H([...sh.querySelectorAll('.sh-key')].map((e) => e.textContent).join('|'))}}); }})()"]
DUMPS = [["wait", 1500]]
for n in range(NS):
    DUMPS += [["eval", f"window.__sh.goto({n}, {{instant: true, silent: true}}); window.__sh.setCone(true, true); 'state {n}'"], ["wait", 350], SETTLE, ["wait", 150], DUMP("on")]
    if n in (0, 7):
        DUMPS += [["eval", "window.__sh.setCone(false, true); 'off'"], ["wait", 350], DUMP("off"), ["eval", "window.__sh.setCone(true, true); 'on'"]]
write("check_v23_dump.json", DUMPS)
# ---- v2.1: the two widget hosts, both directions + the kernel's recount. No fixed sleep decides a pass: every wait is an `until` on what the page shows, and a cell whose
#      output is not there yet is RUN AGAIN (a kernel cannot take the figure's message while one of its cells runs = the timing that made station 2 v3.1's JupyterLab stage flaky).
JHELP = ("(() => { window.__p = window.jupyterapp.shell.currentWidget; window.__nb = () => window.__p.content; window.__run = (i) => { const nb = window.__nb(); nb.activeCellIndex = i; return window.jupyterapp.commands.execute('notebook:run-cell'); };"
         " window.__out = (i) => { const c = window.__nb().widgets[i]; const o = c && c.node.querySelector('.jp-OutputArea'); return o ? o.textContent : ''; }; window.__last = {}; window.__tries = {};"
         " window.__retry = (i, src, every) => { if (new RegExp(src).test(window.__out(i))) return true; const now = Date.now(); if (!window.__last[i] || now - window.__last[i] > every) { window.__last[i] = now; window.__tries[i] = (window.__tries[i] || 0) + 1; window.__run(i); } return false; };"
" window.__fig = () => document.querySelector('.jp-OutputArea .sh'); return 'helpers'; })()")
FIGJ = "(() => { const f = window.__fig(); return f ? {state: f.dataset.state, chapter: f.dataset.chapter, lang: f.dataset.lang, readout: (f.querySelector('[data-readout]') || {}).textContent} : null; })()"
JUP = [["until", "!!window.jupyterapp && document.querySelectorAll('.jp-Notebook .jp-Cell').length === 7", 90000], ["wait", 1500],
       # headless Chrome gives the page no focus: JupyterLab's current notebook stays null and its run commands are disabled until a REAL click lands in the notebook (measured 11-07)
       ["click", ".jp-Notebook .jp-Cell:nth-of-type(2) .jp-InputArea-editor"], ["until", "!!window.jupyterapp.shell.currentWidget && window.jupyterapp.commands.isEnabled('notebook:run-cell')", 20000],
       ["eval", JHELP], ["until", "!!(window.__p.sessionContext.session && window.__p.sessionContext.session.kernel && window.__p.sessionContext.session.kernel.connectionStatus === 'connected')", 60000],
       ["eval", "window.__run(0).then(() => 'cell 0 (markdown)')"],
       ["until", "window.__fig() || window.__retry(1, '.', 15000) && false", 90000],
       ["until", "window.__fig() && window.__fig().dataset.state === '1'", 30000],
       ["eval", f"JSON.stringify({{after_cell_1_widget: {FIGJ}}})"],
       ["eval", "window.__run(2).then(() => 'cell 2: w.state = 10 (kernel -> figure)')"],
       ["until", "window.__fig().dataset.state === '10'", 30000],
       ["eval", f"JSON.stringify({{kernel_to_figure_ok: true, figure: {FIGJ}}})"],
       ["until", "window.__retry(3, \"'state': 10, 'checked': True, 'ok': True\", 2500)", 40000],
       ["eval", "JSON.stringify({recount_state10_ok: true, tries: window.__tries[3], out: window.__out(3).slice(0, 220)})"],
       ["eval", "window.__fig().querySelector('.sh-step[data-n=\"18\"]').click(); 'figure -> kernel: pressed step 18 in the figure'"],
       ["until", "window.__fig().dataset.state === '18'", 20000],
       ["until", "window.__retry(4, \"kernel sees state 18 .*'ok': True\", 2500)", 40000],
       ["eval", "JSON.stringify({figure_to_kernel_ok: true, tries: window.__tries[4], out: window.__out(4).slice(0, 260)})"],
       ["shot", f"{cap}/jupyterlab_s18.png", ".jp-LabShell", 1],
       # v2.2: the overlay switch as a Python value (trait `cone`): kernel -> figure (cell 5: w.state = 0; w.cone = False) and figure -> kernel (the figure's button, then cell 6 prints w.cone)
       ["eval", "window.__run(5).then(() => 'cell 5: w.state = 0; w.cone = False (kernel -> figure)')"],
       ["until", "window.__fig().dataset.state === '0' && !window.__fig().querySelector('.cone-overlay')", 30000],
       ["eval", f"JSON.stringify({{cone_kernel_to_figure_ok: true, figure: {FIGJ}}})"],
       ["eval", "window.__fig().querySelector('.sh-cone').click(); 'figure -> kernel: pressed the cone button in the figure'"],
       ["until", "!!window.__fig().querySelector('.cone-overlay')", 20000],
       ["until", "window.__retry(6, 'kernel sees cone True', 2500)", 40000],
       ["eval", "JSON.stringify({cone_figure_to_kernel_ok: true, tries: window.__tries[6], out: window.__out(6).slice(0, 120)})"]]
write("check_jupyter.json", JUP)
MO = "(() => { const w = document.querySelector('marimo-anywidget'); return w && w.shadowRoot ? w.shadowRoot.querySelector('.sh') : null; })()"
KS = "(() => { const m = document.body.innerText.match(/kernel sees: state = (\\d+) · lang = (\\w+)/); return m ? {state: Number(m[1]), lang: m[2]} : null; })()"
MAR = [["until", f"!!{MO}", 90000], ["wait", 1200],
       ["eval", f"JSON.stringify({{start_figure: {MO}.dataset.state, start_kernel: {KS}}})"],
       ["eval", f"{MO}.querySelector('.sh-next').click(); 'figure -> kernel: pressed next in the figure (1 -> 2)'"],
       ["until", f"({KS} || {{}}).state === 2", 30000],
       ["eval", f"JSON.stringify({{figure_to_kernel_ok: true, kernel: {KS}}})"],
       ["eval", "(() => { const b = [...document.querySelectorAll('marimo-button')].find((x) => x.shadowRoot && x.shadowRoot.textContent.includes('go E → 10')); if (!b) throw new Error('no python button go E'); b.shadowRoot.querySelector('button').click(); return 'kernel -> figure: python button go E → 10'; })()"],
       ["until", f"{MO}.dataset.state === '10' && ({KS} || {{}}).state === 10", 30000],
       ["until", "/kernel check \\(route 5\\): \\{'state': 10, 'checked': True, 'ok': True/.test(document.body.innerText)", 30000],
       ["eval", "JSON.stringify({kernel_to_figure_ok: true, recount: (document.body.innerText.match(/kernel check \\(route 5\\)[^\\n]*/) || [''])[0].slice(0, 200)})"],
       ["shot", f"{cap}/marimo_s10.png", "html", 1, [0, 0, 1440, 1500]]]
# v2.2: the overlay switch as a Python value (trait `cone`), both directions: kernel -> figure (python button "cone off") and figure -> kernel (the figure's own button), on state 0; the readout does not change
PYB = lambda label: "(() => { const b = [...document.querySelectorAll('marimo-button')].find((x) => x.shadowRoot && x.shadowRoot.textContent.includes(%s)); if (!b) throw new Error('no python button ' + %s); b.shadowRoot.querySelector('button').click(); return 'python button ' + %s; })()" % ((json.dumps(label),) * 3)
KC = "((document.body.innerText.match(/cone = (True|False)/) || [])[1])"
MAR += [["eval", PYB("go A → 0")], ["until", f"{MO}.dataset.state === '0' && !!{MO}.querySelector('.cone-overlay') && {KC} === 'True'", 30000],
        ["eval", f"(window.__ro0 = {MO}.querySelector('[data-readout]').textContent, JSON.stringify({{state0_overlay_on: true, kernel_cone: {KC}}}))"],
        # kernel -> figure: a trait set in Python does not re-run marimo's display cell (only a change that starts in the figure does), so this direction is read on the figure
        ["eval", PYB("cone off")], ["until", f"!{MO}.querySelector('.cone-overlay')", 30000],
        ["eval", f"(() => {{ if ({MO}.querySelector('[data-readout]').textContent !== window.__ro0) throw new Error('marimo: the readout changed with the overlay'); return JSON.stringify({{cone_kernel_to_figure_ok: true, overlay: false}}); }})()"],
        ["eval", PYB("cone on")], ["until", f"!!{MO}.querySelector('.cone-overlay')", 30000],
        # figure -> kernel: the figure's own button; the kernel's display must turn to False, then back to True
        ["eval", f"{MO}.querySelector('.sh-cone').click(); 'figure -> kernel: pressed the cone button in the figure (off)'"], ["until", f"!{MO}.querySelector('.cone-overlay') && {KC} === 'False'", 30000],
        ["eval", f"{MO}.querySelector('.sh-cone').click(); 'figure -> kernel: pressed the cone button in the figure (on)'"], ["until", f"!!{MO}.querySelector('.cone-overlay') && {KC} === 'True'", 30000],
        ["eval", f"(() => {{ if ({MO}.querySelector('[data-readout]').textContent !== window.__ro0) throw new Error('marimo: the readout changed with the overlay'); return JSON.stringify({{cone_figure_to_kernel_ok: true, kernel_cone: {KC}}}); }})()"]]
write("check_marimo.json", MAR)
write("check_capture_video_en.json", capture("video", lambda i: f"video_s{i}_en.png"))
write("check_capture_en.json", [["wait", 2000]] + sum([[goto(i), ["wait", 1500], ["shot", f"{cap}/page_dark_s{i}_en.png", ".sh", 1]] for i in (1, 3, 4, 10, 18, 23, 25, 27, 29, 30)], []))
print(f"wrote check_states ({len(states)} steps), check_robust, check_scan, check_pagevraw ({len(EXPECT)} cells, {len(READOUTS)} readouts), check_chapters ({len(chap)} steps), 5 capture files -> {OUT} · {NS} states · groups {GROUPS}")
