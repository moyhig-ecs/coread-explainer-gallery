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
  const S = { state: 0, lang: host.lang() === "en" ? "en" : "ja", t: 0, free: false, playing: false, cone: host.cone ? host.cone() !== false : true };   // v2.2: cone = the overlay on the board states (default on)
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
  const T = () => I18N[S.lang], Q = () => FIGURE.ctx(S), keysNow = () => (FIGURE.keysOf ? FIGURE.keysOf(S) : FIGURE.keys[STATES[S.state].mode] || []);
  // v2.1 (BRIEF v2.1 §2-8): the 1920 x 1080 frame. v2 measured the box of the page (.sh, height 100vh, overflow hidden = always inside) while the last line "what this figure does not say"
  //   ran below it and was clipped in the stills (s10, s24–s26). Now the picture gives way: when the last line would pass the bottom of the frame, the svg is made shorter by that much.
  //   The check measures the LAST LINE itself (make_check.py MEASURE); fit(false) turns this off, which the check's positive control uses (the old clipping must then be caught).
  let fitOn = true;
  // v2.1: the plate's title corner (title + stamp, HTML) may wrap to 2-3 lines and sit over the top of the svg (found by the corner check on desk / phone): the plate's top padding grows to clear it.
  function clearCorner() {
    const plate = $(".iso-plate"), c = $('[data-corner="title"]'); if (!plate || !c) return;
    plate.style.paddingTop = ""; const need = c.getBoundingClientRect().bottom - plate.getBoundingClientRect().top + 8, have = parseFloat(getComputedStyle(plate).paddingTop) || 0;
    if (need > have) plate.style.paddingTop = `${Math.ceil(need)}px`;
  }
  function fitVideo() {
    if (root.dataset.video !== "1") { clearCorner(); return; }
    const svg = el.svg; svg.style.height = "";
    if (!fitOn) return;
    const nc = $(".sh-notclaimed"), pad = parseFloat(getComputedStyle(root).paddingBottom) || 0, lim = Math.min(innerHeight, root.getBoundingClientRect().bottom - pad) - 2;
    const over = nc.getBoundingClientRect().bottom - lim;
    if (over > 0) svg.style.height = `${Math.max(200, svg.getBoundingClientRect().height - over)}px`;
  }
  // v2.1: the card pill = the cards this state reads (its texts in ja and en + its picture), recorded by the DATA wrapper (build.mjs trackData). Cached per state.
  const pillCache = {};
  function cardsOf(n) {
    if (pillCache[n]) return pillCache[n];
    const keepS = S.state, keepL = S.lang, scr = { svg: document.createElementNS("http://www.w3.org/2000/svg", "svg"), pic: document.createElementNS("http://www.w3.org/2000/svg", "g"), ledger: document.createElement("div") };
    READ.clear(); let got = [];
    try { S.state = n; for (const lg of ["ja", "en"]) { S.lang = lg; const st = I18N[lg].states[n], q = FIGURE.ctx(S); if (typeof st.q === "function") st.q(q); st.lead(q); st.readout(q); st.lim(q); st.chips(q); FIGURE.draw(S, A, scr, root); } got = [...READ]; }
    finally { S.state = keepS; S.lang = keepL; draw(); READ.clear(); }
    const rank = (c) => (/^(SOURCE|SUMMARY|RESULT|PREREG)/.test(c) ? 1 : 0);
    return (pillCache[n] = got.sort((a, b) => rank(a) - rank(b) || a.localeCompare(b, "en", { numeric: true })));
  }
  function render() {
    const tt = T(), st = tt.states[S.state], q = Q();
    const cards = cardsOf(S.state), pill = $("[data-pill]");
    if (pill) { pill.textContent = cards.length ? `${tt.pill}: ${cards.join(" · ")}` : tt.pillNone; pill.dataset.cards = cards.join(" "); }
    root.lang = S.lang; root.dataset.lang = S.lang; root.dataset.state = String(S.state); root.dataset.chapter = chapterOf(S.state);
    $(".sh-kicker").textContent = st.kicker; $(".sh-q").textContent = typeof st.q === "function" ? st.q(q) : st.q; $(".sh-lead").textContent = st.lead(q);
    $('[data-corner="fig"]').textContent = tt.ui.fig; $('[data-corner="title"] .t1').textContent = tt.ui.title; $('[data-corner="title"] .sh-corner2').textContent = st.stamp;
    $('[data-corner="hint"]').textContent = tt.ui.hint; $('[data-corner="readout"]').textContent = st.readout(q);
    $(".sh-panel").innerHTML = st.chips(q).map((c) => `<div class="sh-chip" data-tone="${c.tone || ""}"><span class="k">${c.k}</span><span class="v">${c.v}</span><span class="s">${c.s}</span></div>`).join("");
    $(".sh-head").dataset.state = String(S.state);
    $(".sh-keys").innerHTML = keysNow().map((k) => `<span class="sh-key"><i class="sw sw-${k}"></i>${tt.keys[k]}</span>`).join("");
    $(".sh-strip .sh-lim").innerHTML = `<b>${st.limTag}</b> ${st.lim(q)}<br><span class="sh-lim-all">${tt.ui.lim}</span>`; $(".sh-notclaimed").textContent = tt.notClaimed; $(".sh-caption").textContent = tt.ui.caption[chapterOf(S.state)] || "";
    $(".sh-foot").textContent = `${tt.ui.mit} · ${tt.ui.pack}`;
    $$(".sh-step").forEach((b, i) => { b.setAttribute("aria-current", i === S.state ? "step" : "false"); b.title = tt.states[i].kicker; });
    $$(".sh-chap").forEach((b) => { b.textContent = tt.ui.chapters[b.dataset.chap]; b.setAttribute("aria-pressed", String(b.dataset.chap === chapterOf(S.state))); b.title = tt.states[Number(b.dataset.go)].kicker; });
    $(".sh-lang").textContent = tt.other; $(".sh-prev").setAttribute("aria-label", tt.ui.prev); $(".sh-next").setAttribute("aria-label", tt.ui.next);
    const [lo, hi] = FIGURE.tRange(S), rg = $(".fig-range"); rg.min = String(lo); rg.max = String(hi); rg.value = String(S.t); $(".fig-tval").textContent = `${tt.ui.pos} = ${S.t}`;
    const cb = $(".sh-cone"); if (cb) { cb.textContent = tt.ui.cone; cb.setAttribute("aria-pressed", String(S.cone)); cb.title = S.cone ? tt.ui.coneOn : tt.ui.coneOff; }
    fitVideo();
    host.onReading && host.onReading({ state: S.state, chapter: chapterOf(S.state), lang: S.lang, t: S.t, kicker: st.kicker, readout: st.readout(q), chips: st.chips(q).map((c) => ({ k: c.k, v: c.v })) });
  }
  // ---- states
  const clearAuto = () => { clearTimeout(autoTimer); autoTimer = 0; };
  function apply(n, instant) {
    const pr = STATES[n], cam = pr.cam || [58, 24, 1, 0]; clearAuto(); S.t = pr.t === "focus" ? FIGURE.focus() : pr.t;
    if (!S.free || !instant || !pr.cam) { to("az", cam[0]); to("el", cam[1]); to("zoom", cam[2]); } to("px", cam[3]); if (pr.cam) S.free = false;
    if (pr.auto === "sweep" && !still.matches && !instant) { const [lo, hi] = FIGURE.tRange(S); let t = S.t; const step = () => { t = t >= hi ? lo : t + 1; S.t = t; wake(); render(); autoTimer = setTimeout(step, 700); }; autoTimer = setTimeout(step, 1600); }
    if (instant) Object.values(anims).forEach((a) => (a.cur = a.tgt));
  }
  function go(n, opt = {}) { n = clamp(Math.round(Number(n) || 0), 0, NSTATE - 1); const changed = n !== S.state; S.state = n; apply(n, !!opt.instant); wake(); draw(); render(); if (changed && !opt.silent && host.onState) host.onState(n); }
  function setT(t, silent) { const [lo, hi] = FIGURE.tRange(S); S.t = clamp(Math.round(t), lo, hi); clearAuto(); wake(); render(); if (!silent && host.onSync) host.onSync({ t: S.t }); }
  function setLang(l, silent) { S.lang = l === "en" ? "en" : "ja"; wake(); render(); if (!silent && host.onLang) host.onLang(S.lang); }
  function setCone(on, silent) { S.cone = on !== false; wake(); draw(); render(); if (!silent && host.onCone) host.onCone(S.cone); }   // v2.2: the overlay only adds a layer of the picture (texts and readout do not depend on it)
  function setTheme(th) { root.dataset.theme = th === "light" ? "light" : "dark"; if (host.onTheme) host.onTheme(root.dataset.theme); }
  function setView(v) { if (!v) return; S.free = true; if (v.az !== undefined) to("az", clamp(v.az, 3, 177)); if (v.el !== undefined) to("el", clamp(v.el, 3, 82)); if (v.zoom !== undefined) to("zoom", clamp(v.zoom, 0.5, 2.6)); render(); }
  // ---- the reader's hands: orbit, buttons, keys
  let drag = null; const svg = el.svg;
  svg.addEventListener("pointerdown", (e) => { if (e.button !== 0) return; if (e.target.closest && e.target.closest("[data-goto]")) return; if (STATES[S.state].mode !== "iso") return; /* a click on the map is a click, not an orbit (setPointerCapture would steal it); only the 3D states orbit */ drag = { x: e.clientX, y: e.clientY, az: anims.az.tgt, el: anims.el.tgt }; S.free = true; clearAuto(); try { svg.setPointerCapture(e.pointerId); } catch (_) {} });
  svg.addEventListener("pointermove", (e) => { if (!drag) return; const r = svg.getBoundingClientRect(); to("az", clamp(drag.az + ((e.clientX - drag.x) / r.width) * 140, 3, 177)); to("el", clamp(drag.el + ((e.clientY - drag.y) / r.height) * 80, 3, 82)); });
  svg.addEventListener("pointerup", () => { drag = null; });
  root.addEventListener("click", (e) => { const g = e.target.closest && e.target.closest("[data-goto]"); if (g && root.contains(g)) { go(Number(g.dataset.goto)); return; } const b = e.target.closest("button"); if (!b || !root.contains(b)) return;
    if (b.classList.contains("sh-step")) go(Number(b.dataset.n)); else if (b.classList.contains("sh-chap")) go(Number(b.dataset.go)); else if (b.classList.contains("sh-prev")) go(S.state - 1); else if (b.classList.contains("sh-next")) go(S.state + 1);
    else if (b.classList.contains("sh-cone")) setCone(!S.cone);
    else if (b.classList.contains("sh-lang")) setLang(S.lang === "ja" ? "en" : "ja"); else if (b.classList.contains("sh-theme")) setTheme(root.dataset.theme === "light" ? "dark" : "light"); });
  $(".fig-range").addEventListener("input", (e) => setT(Number(e.target.value)));
  root.addEventListener("keydown", (e) => { if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === "ArrowRight") go(S.state + 1); else if (e.key === "ArrowLeft") go(S.state - 1); else if (e.key === ",") setT(S.t - 1); else if (e.key === ".") setT(S.t + 1); else if (e.key === "l" || e.key === "L") setLang(S.lang === "ja" ? "en" : "ja"); });
  // ---- the first picture, and the handle the page / the widget / the checks use (window.__sh)
  setTheme(host.theme ? host.theme() : "dark"); go(host.state(), { instant: true, silent: true });
  return { goto: go, setT, setLang, setTheme, setView, setCone, get cone() { return S.cone; }, cards: (n) => cardsOf(n), fit: (on) => { fitOn = on !== false; fitVideo(); }, get state() { return S.state; }, get chapter() { return chapterOf(S.state); }, get lang() { return S.lang; }, get t() { return S.t; }, get nstate() { return NSTATE; },
           destroy() { alive = false; clearAuto(); if (frame) cancelAnimationFrame(frame); } };
}
