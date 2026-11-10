// state_machine.js — the engine of a co-reading figure (template; no domain content). Inlined after DATA, I18N and FIGURE by build.mjs; used by the page and by the widget.
//   what it owns: the state table + the chapters (from config.json), the hash, the chapter buttons and the numbered steps, the language / theme, the animated camera (exponential follow), the orbit by pointer drag,
//   the keys, the texts of each state (kicker, question, lead, stamp, readout, cards, legend, limits), and the host API for the page / the widget (onState, onSync, onReading, onDone).
//   what it asks of figure.js:  FIGURE.states · FIGURE.ctx(S) · FIGURE.draw(S, A, el, root) · FIGURE.keys[mode] · FIGURE.tRange(S) · FIGURE.focus()
// The numbers of the states exist in ONE place: config.json "chapters" (build.mjs writes the buttons from it; make_check.py and list_headings.py read it). Renumber there, then run list_headings.py.
function mountFigure(root, host) {
  const $ = (s) => root.querySelector(s), $$ = (s) => [...root.querySelectorAll(s)];
  const CH = DATA.config.chapters, NSTATE = CH[CH.length - 1][2] + 1, STATES = FIGURE.states;
  if (STATES.length !== NSTATE) throw new Error(`FIGURE.states has ${STATES.length} entries but config.json has ${NSTATE} states`);
  STATES.forEach((s, n) => { if (s.chapter !== chapterOf(n)) throw new Error(`state ${n}: chapter "${s.chapter}" is not the one of config.json ("${chapterOf(n)}")`); });
  function chapterOf(n) { return (CH.find(([, a, b]) => n >= a && n <= b) || [])[0]; }
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const S = { state: 0, lang: host.lang() === "en" ? "en" : "ja", t: 0, free: false, playing: false };
  // ---- animated scalars: each follows its target exponentially (time constant tau in seconds); a frame is drawn only while something moves
  const anims = {}, mk = (name, init, tau) => (anims[name] = { cur: init, tgt: init, tau });
  mk("az", 58, 0.6); mk("el", 24, 0.6); mk("zoom", 1, 0.6); mk("px", 0, 0.6);
  const A = (name) => anims[name].cur, to = (name, v) => { anims[name].tgt = v; wake(); };
  let dirty = true, frame = 0, last = 0, alive = true, autoTimer = 0;
  const still = matchMedia("(prefers-reduced-motion: reduce)");
  function wake() { dirty = true; if (!frame && alive) frame = requestAnimationFrame(tick); }
  function tick(now) {
    frame = 0; if (!alive) return; const dt = Math.min(0.05, (now - (last || now)) / 1000); last = now; let moving = false;
    for (const a of Object.values(anims)) { const d = a.tgt - a.cur; if (Math.abs(d) > 1e-3) { a.cur += d * (1 - Math.exp(-dt / a.tau)); moving = true; } else a.cur = a.tgt; }
    if (dirty || moving) { draw(); dirty = false; } if (moving) frame = requestAnimationFrame(tick); else { last = 0; host.onDone && host.onDone(true); }
  }
  // ---- the picture and the texts
  const el = { svg: $(".fig-svg"), pic: $(".fig-svg [data-g=picture]"), ledger: $(".fig-ledger") };
  const draw = () => FIGURE.draw(S, A, el, root);
  const T = () => I18N[S.lang], Q = () => FIGURE.ctx(S), keysNow = () => FIGURE.keys[STATES[S.state].mode] || [];
  function render() {
    const tt = T(), st = tt.states[S.state], q = Q();
    root.lang = S.lang; root.dataset.lang = S.lang; root.dataset.state = String(S.state); root.dataset.chapter = chapterOf(S.state);
    $(".sh-kicker").textContent = st.kicker; $(".sh-q").textContent = st.q; $(".sh-lead").textContent = st.lead(q);
    $('[data-corner="fig"]').textContent = tt.ui.fig; $('[data-corner="title"] .t1').textContent = tt.ui.title; $('[data-corner="title"] .sh-corner2').textContent = st.stamp;
    $('[data-corner="hint"]').textContent = tt.ui.hint; $('[data-corner="readout"]').textContent = st.readout(q);
    $(".sh-panel").innerHTML = st.chips(q).map((c) => `<div class="sh-chip" data-tone="${c.tone || ""}"><span class="k">${c.k}</span><span class="v">${c.v}</span><span class="s">${c.s}</span></div>`).join("");
    $(".sh-keys").innerHTML = keysNow().map((k) => `<span class="sh-key"><i class="sw sw-${k}"></i>${tt.keys[k]}</span>`).join("");
    $(".sh-strip .sh-lim").innerHTML = `<b>${st.limTag}</b> ${st.lim(q)} · ${tt.ui.lim}`; $(".sh-notclaimed").textContent = tt.notClaimed; $(".sh-caption").textContent = tt.ui.caption[chapterOf(S.state)] || "";
    $(".sh-foot").textContent = `${tt.ui.mit} · ${tt.ui.pack}`;
    $$(".sh-step").forEach((b, i) => { b.setAttribute("aria-current", i === S.state ? "step" : "false"); b.title = tt.states[i].kicker; });
    $$(".sh-chap").forEach((b) => { b.textContent = tt.ui.chapters[b.dataset.chap]; b.setAttribute("aria-pressed", String(b.dataset.chap === chapterOf(S.state))); b.title = tt.states[Number(b.dataset.go)].kicker; });
    $(".sh-lang").textContent = tt.other; $(".sh-prev").setAttribute("aria-label", tt.ui.prev); $(".sh-next").setAttribute("aria-label", tt.ui.next);
    const [lo, hi] = FIGURE.tRange(S), rg = $(".fig-range"); rg.min = String(lo); rg.max = String(hi); rg.value = String(S.t); $(".fig-tval").textContent = `${tt.ui.pos} = ${S.t}`;
    host.onReading && host.onReading({ state: S.state, chapter: chapterOf(S.state), lang: S.lang, t: S.t, kicker: st.kicker, readout: st.readout(q), chips: st.chips(q).map((c) => ({ k: c.k, v: c.v })) });
  }
  // ---- states
  const clearAuto = () => { clearTimeout(autoTimer); autoTimer = 0; };
  function apply(n, instant) {
    const pr = STATES[n]; clearAuto(); S.t = pr.t === "focus" ? FIGURE.focus() : pr.t;
    if (!S.free || !instant) { to("az", pr.cam[0]); to("el", pr.cam[1]); to("zoom", pr.cam[2]); } to("px", pr.cam[3]);
    if (pr.auto === "sweep" && !still.matches && !instant) { const [lo, hi] = FIGURE.tRange(S); let t = S.t; const step = () => { t = t >= hi ? lo : t + 1; S.t = t; wake(); render(); autoTimer = setTimeout(step, 700); }; autoTimer = setTimeout(step, 1600); }
    if (instant) Object.values(anims).forEach((a) => (a.cur = a.tgt));
  }
  function go(n, opt = {}) { n = clamp(Math.round(Number(n) || 0), 0, NSTATE - 1); const changed = n !== S.state; S.state = n; apply(n, !!opt.instant); wake(); draw(); render(); if (changed && !opt.silent && host.onState) host.onState(n); }
  function setT(t, silent) { const [lo, hi] = FIGURE.tRange(S); S.t = clamp(Math.round(t), lo, hi); clearAuto(); wake(); render(); if (!silent && host.onSync) host.onSync({ t: S.t }); }
  function setLang(l, silent) { S.lang = l === "en" ? "en" : "ja"; wake(); render(); if (!silent && host.onLang) host.onLang(S.lang); }
  function setTheme(th) { root.dataset.theme = th === "light" ? "light" : "dark"; if (host.onTheme) host.onTheme(root.dataset.theme); }
  function setView(v) { if (!v) return; S.free = true; if (v.az !== undefined) to("az", clamp(v.az, 3, 177)); if (v.el !== undefined) to("el", clamp(v.el, 3, 82)); if (v.zoom !== undefined) to("zoom", clamp(v.zoom, 0.5, 2.6)); render(); }
  // ---- the reader's hands: orbit, buttons, keys
  let drag = null; const svg = el.svg;
  svg.addEventListener("pointerdown", (e) => { if (e.button !== 0) return; drag = { x: e.clientX, y: e.clientY, az: anims.az.tgt, el: anims.el.tgt }; S.free = true; clearAuto(); try { svg.setPointerCapture(e.pointerId); } catch (_) {} });
  svg.addEventListener("pointermove", (e) => { if (!drag) return; const r = svg.getBoundingClientRect(); to("az", clamp(drag.az + ((e.clientX - drag.x) / r.width) * 140, 3, 177)); to("el", clamp(drag.el + ((e.clientY - drag.y) / r.height) * 80, 3, 82)); });
  svg.addEventListener("pointerup", () => { drag = null; });
  root.addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b || !root.contains(b)) return;
    if (b.classList.contains("sh-step")) go(Number(b.dataset.n)); else if (b.classList.contains("sh-chap")) go(Number(b.dataset.go)); else if (b.classList.contains("sh-prev")) go(S.state - 1); else if (b.classList.contains("sh-next")) go(S.state + 1);
    else if (b.classList.contains("sh-lang")) setLang(S.lang === "ja" ? "en" : "ja"); else if (b.classList.contains("sh-theme")) setTheme(root.dataset.theme === "light" ? "dark" : "light"); });
  $(".fig-range").addEventListener("input", (e) => setT(Number(e.target.value)));
  root.addEventListener("keydown", (e) => { if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === "ArrowRight") go(S.state + 1); else if (e.key === "ArrowLeft") go(S.state - 1); else if (e.key === ",") setT(S.t - 1); else if (e.key === ".") setT(S.t + 1); else if (e.key === "l" || e.key === "L") setLang(S.lang === "ja" ? "en" : "ja"); else if (/^[0-9]$/.test(e.key) && Number(e.key) < NSTATE) go(Number(e.key)); });
  // ---- the first picture, and the handle the page / the widget / the checks use (window.__sh)
  setTheme(host.theme ? host.theme() : "dark"); go(host.state(), { instant: true, silent: true });
  return { goto: go, setT, setLang, setTheme, setView, get state() { return S.state; }, get chapter() { return chapterOf(S.state); }, get lang() { return S.lang; }, get t() { return S.t; }, get nstate() { return NSTATE; },
           destroy() { alive = false; clearAuto(); if (frame) cancelAnimationFrame(frame); } };
}
