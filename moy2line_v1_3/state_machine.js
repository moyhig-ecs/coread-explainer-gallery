// state_machine.js — the engine of the co-reading figure (no domain content). Inlined after DATA, I18N and FIGURE by build.mjs; used by the page and by the widget.
//   owns: the state table + the chapters (from config.json), the hash, the chapter buttons and the numbered steps, language / theme, the reader's hands (drag to pick a row or an arm, keys),
//   the texts of each state (kicker, question, lead, stamp, readout, cards, legend, limits), and the host API for the page / the widget (onState, onRow, onArm, onLang, onReading, onDone).
//   asks of figure.js:  FIGURE.states · FIGURE.ctx(S) · FIGURE.draw(S, el, root) · FIGURE.keys[mode] · FIGURE.pick(S, x, y) · FIGURE.rowsOf(S) · FIGURE.armIds
// The art is static (built once with the Anatomy kit), so there is no camera to animate: the drag of the reader PICKS (a row of the rack, an arm of the scale), it does not orbit.
function mountFigure(root, host) {
  const $ = (s) => root.querySelector(s), $$ = (s) => [...root.querySelectorAll(s)];
  const CH = DATA.config.chapters, NSTATE = CH[CH.length - 1][2] + 1, STATES = FIGURE.states;
  if (STATES.length !== NSTATE) throw new Error(`FIGURE.states has ${STATES.length} entries but config.json has ${NSTATE} states`);
  STATES.forEach((s, n) => { if (s.chapter !== chapterOf(n)) throw new Error(`state ${n}: chapter "${s.chapter}" is not the one of config.json ("${chapterOf(n)}")`); });
  function chapterOf(n) { return (CH.find(([, a, b]) => n >= a && n <= b) || [])[0]; }
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const S = { state: 0, lang: host.lang() === "en" ? "en" : "ja", row: "", arm: "" };
  let alive = true, frame = 0;
  const el = { svg: $(".fig-svg"), art: $(".fig-svg [data-g=art]"), pic: $(".fig-svg [data-g=picture]"), side: $(".fig-side"), ctitle: $(".fig-ctitle"), html: $(".fig-html"), ledger: $(".fig-ledger") };
  const T = () => I18N[S.lang], Q = () => FIGURE.ctx(S), keysNow = () => FIGURE.keys[STATES[S.state].mode + "_" + (STATES[S.state].filter || "")] || FIGURE.keys[STATES[S.state].mode] || [];   // a filtered state may carry its own legend (v1.1: rack_o127 adds ◇)
  function draw() { FIGURE.draw(S, el, root); if (frame) cancelAnimationFrame(frame); host.onDone && host.onDone(false); frame = requestAnimationFrame(() => { frame = 0; if (alive && host.onDone) host.onDone(true); }); }
  function render() {
    const tt = T(), st = tt.states[S.state], q = Q();
    root.lang = S.lang; root.dataset.lang = S.lang; root.dataset.state = String(S.state); root.dataset.chapter = chapterOf(S.state);
    root.dataset.view = STATES[S.state].view; root.dataset.mode = STATES[S.state].mode; root.dataset.filter = STATES[S.state].filter || ""; root.dataset.pick = STATES[S.state].pick || "";
    $(".sh-kicker").textContent = st.kicker; $(".sh-q").textContent = st.q; $(".sh-lead").textContent = st.lead(q);
    $('[data-corner="fig"]').textContent = tt.ui.fig; $('[data-corner="title"] .t1').textContent = tt.ui.title; $('[data-corner="title"] .sh-corner2').textContent = st.stamp;
    $('[data-corner="hint"]').textContent = STATES[S.state].pick ? tt.ui.hintPick[STATES[S.state].pick] : tt.ui.hint; $('[data-corner="readout"]').textContent = st.readout(q);
    $(".sh-panel").innerHTML = st.chips(q).map((c) => `<div class="sh-chip" data-tone="${c.tone || ""}"><span class="k">${c.k}</span><span class="v">${c.v}</span><span class="s">${c.s}</span></div>`).join("");
    $(".sh-keys").innerHTML = keysNow().map((k) => `<span class="sh-key"><i class="sw sw-${k}"></i>${tt.keys[k]}</span>`).join("");
    $(".sh-strip .sh-lim").innerHTML = `<b>${st.limTag}</b> ${st.lim(q)}`; $(".sh-notclaimed").textContent = tt.notClaimed; $(".sh-caption").textContent = tt.ui.caption[STATES[S.state].mode] || "";
    $(".sh-foot").textContent = `${tt.ui.mit} · ${tt.ui.pack}`;
    $$(".sh-step").forEach((b, i) => { b.setAttribute("aria-current", i === S.state ? "step" : "false"); b.title = tt.states[i].kicker; });
    $$(".sh-chap").forEach((b) => { b.textContent = tt.ui.chapters[b.dataset.chap]; b.setAttribute("aria-pressed", String(b.dataset.chap === chapterOf(S.state))); b.title = tt.states[Number(b.dataset.go)].kicker; });
    $(".sh-lang").textContent = tt.other; $(".sh-prev").setAttribute("aria-label", tt.ui.prev); $(".sh-next").setAttribute("aria-label", tt.ui.next);
    host.onReading && host.onReading({ state: S.state, chapter: chapterOf(S.state), lang: S.lang, row: S.row, arm: S.arm, kicker: st.kicker, readout: st.readout(q), chips: st.chips(q).map((c) => ({ k: c.k, v: c.v })), side: el.side.textContent.slice(0, 600) });
  }
  const full = () => { draw(); render(); };
  function go(n, opt = {}) {
    n = clamp(Math.round(Number(n) || 0), 0, NSTATE - 1); const changed = n !== S.state; S.state = n;
    const pr = STATES[n];
    // each row state opens on its own scene row (and the scale on its arm), unless the same write carries a row / an arm (the widget passes the kernel's values with the state)
    if (pr.sel) S.row = opt.row && FIGURE.rowsOf(S).includes(opt.row) ? opt.row : pr.sel;
    if (pr.arm) S.arm = opt.arm && FIGURE.armIds.includes(opt.arm) ? opt.arm : pr.arm;
    full(); if (changed && !opt.silent && host.onState) host.onState(n);
  }
  function setRow(id, silent) { if (!FIGURE.allRows.includes(id)) return; S.row = id; full(); if (!silent && host.onRow) host.onRow(id); }
  function setArm(id, silent) { if (!FIGURE.armIds.includes(id)) return; S.arm = id; full(); if (!silent && host.onArm) host.onArm(id); }
  function stepRow(d) {
    const pk = STATES[S.state].pick;
    if (pk === "row") { const list = FIGURE.rowsOf(S); const i = list.indexOf(S.row); setRow(list[(i + d + list.length) % list.length]); }
    else if (pk === "arm") { const list = FIGURE.armIds; const i = list.indexOf(S.arm); setArm(list[(i + d + list.length) % list.length]); }
  }
  function setLang(l, silent) { S.lang = l === "en" ? "en" : "ja"; full(); if (!silent && host.onLang) host.onLang(S.lang); }
  function setTheme(th) { root.dataset.theme = th === "light" ? "light" : "dark"; if (host.onTheme) host.onTheme(root.dataset.theme); }
  // ---- the reader's hands: drag picks (a row of the rack, an arm of the scale), buttons, keys
  let drag = false; const svg = el.svg;
  const vbPoint = (e) => { const m = svg.getScreenCTM(); if (!m) return null; const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse()); return [p.x, p.y]; };
  const pickAt = (e) => {
    const pk = STATES[S.state].pick; if (!pk) return; const p = vbPoint(e); if (!p) return; const hit = FIGURE.pick(S, p[0], p[1]); if (!hit) return;
    if (pk === "row" && hit !== S.row) setRow(hit); else if (pk === "arm" && hit !== S.arm) setArm(hit);
  };
  svg.addEventListener("pointerdown", (e) => { if (e.button !== 0 || !STATES[S.state].pick) return; drag = true; try { svg.setPointerCapture(e.pointerId); } catch (_) {} pickAt(e); e.preventDefault(); });
  svg.addEventListener("pointermove", (e) => { if (drag) pickAt(e); });
  svg.addEventListener("pointerup", () => { drag = false; }); svg.addEventListener("pointercancel", () => { drag = false; });
  root.addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b || !root.contains(b)) return;
    if (b.classList.contains("sh-step")) go(Number(b.dataset.n)); else if (b.classList.contains("sh-chap")) go(Number(b.dataset.go)); else if (b.classList.contains("sh-prev")) go(S.state - 1); else if (b.classList.contains("sh-next")) go(S.state + 1);
    else if (b.classList.contains("sh-lang")) setLang(S.lang === "ja" ? "en" : "ja"); else if (b.classList.contains("sh-theme")) setTheme(root.dataset.theme === "light" ? "dark" : "light");
    else if (b.dataset.goState) go(Number(b.dataset.goState)); else if (b.dataset.row) setRow(b.dataset.row); });
  root.addEventListener("keydown", (e) => { if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === "ArrowRight") go(S.state + 1); else if (e.key === "ArrowLeft") go(S.state - 1); else if (e.key === ",") stepRow(-1); else if (e.key === ".") stepRow(1); else if (e.key === "l" || e.key === "L") setLang(S.lang === "ja" ? "en" : "ja"); });
  setTheme(host.theme ? host.theme() : "dark");
  go(host.state(), { silent: true, row: host.row ? host.row() : "", arm: host.arm ? host.arm() : "" });
  return { goto: go, setRow, setArm, setLang, setTheme, get state() { return S.state; }, get chapter() { return chapterOf(S.state); }, get lang() { return S.lang; }, get row() { return S.row; }, get arm() { return S.arm; }, get nstate() { return NSTATE; },
           rowsNow: () => FIGURE.rowsOf(S), destroy() { alive = false; if (frame) cancelAnimationFrame(frame); } };
}
