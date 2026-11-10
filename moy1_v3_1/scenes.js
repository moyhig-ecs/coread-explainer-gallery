// scenes.js — the drawing helpers and the scene functions of the moy-1 figure (inlined after I18N and before figure.js by build.mjs).
// Every number is read from DATA (generated/pack.json, written by pack_moy1.py and recounted by data.mjs); nothing is typed here except layout constants (units of the drawing, never a data value).
// A scene = (S, A, cv, st) -> svg markup.  S = the state of the machine (S.t = the focus index, S.lang), A = the animated camera scalars, cv = the canvas {W, H, narrow, video, fs}, st = the state's row of the table.
const SCENES = (() => {
  const PI = Math.PI;
  let PS = 1;                                                              // the scale of marks (pins, pegs): the phone draws them larger; set at the top of every scene by `begin`
  const begin = (cv) => { PS = cv.u || 1; };
  const n1 = (v) => Math.round(v * 10) / 10;
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const TX = () => I18N;                                                    // the words of the tags (per language) live in i18n.js: I18N[lang].tags

  // ---- the camera: the kit's isometric formula (azimuth / elevation), fitted to a world box so that the picture fills the canvas; zoom is relative to that fit
  function camera(az, el, zoom, px, box, W, H, padx = 0.94, pady = 0.86) {
    const a = (az * PI) / 180, e = (el * PI) / 180, sA = Math.sin(a), cA = Math.cos(a), sE = Math.sin(e), cE = Math.cos(e);
    const f = (x, y, z) => [x * sA - y * cA, (x * cA + y * sA) * sE - z * cE];
    const xs = [], ys = [];
    for (const x of [box[0], box[3]]) for (const y of [box[1], box[4]]) for (const z of [box[2], box[5]]) { const q = f(x, y, z); xs.push(q[0]); ys.push(q[1]); }
    const x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys), k = Math.min((W * padx) / (x1 - x0), (H * pady) / (y1 - y0)) * zoom, cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    return { k, sA, cA, sE, cE, p: (x, y, z) => { const q = f(x, y, z); return [W / 2 + px + (q[0] - cx) * k, H / 2 + (q[1] - cy) * k]; }, depth: (x, y) => x * cA + y * sA };
  }
  const P2 = (Pj, v) => Pj.p(v[0], v[1], v[2]).map(n1).join(" ");
  const path = (Pj, vs, close = false) => "M" + vs.map((v) => P2(Pj, v)).join("L") + (close ? "Z" : "");
  const newScene = () => ({ boxes: [], flat: [], over: [], tags: [] });
  const flush = (sc) => sc.boxes.sort((a, b) => a.key - b.key).map((b) => b.svg).join("") + sc.flat.join("") + sc.over.join("") + sc.tags.join("");

  // ---- solids: a box with the kit's four tones (top lightest, the +y face, the side face) drawn as three paths; tone classes t-b (apex blue) t-o (attractor orange) t-g (bare grey) t-x (other) t-l (lit) t-p (plate)
  function box(sc, Pj, x, y, w, d, h, tone, z0 = 0, o = {}) {
    const top = [[x, y, z0 + h], [x + w, y, z0 + h], [x + w, y + d, z0 + h], [x, y + d, z0 + h]];
    const fr = [[x, y + d, z0], [x + w, y + d, z0], [x + w, y + d, z0 + h], [x, y + d, z0 + h]];
    const sd = Pj.cA >= 0 ? [[x + w, y, z0], [x + w, y + d, z0], [x + w, y + d, z0 + h], [x + w, y, z0 + h]] : [[x, y, z0], [x, y + d, z0], [x, y + d, z0 + h], [x, y, z0 + h]];
    sc.boxes.push({ key: o.key !== undefined ? o.key : Pj.depth(x + w / 2, y + d / 2) + z0 * 0.001, svg: `<g class="bx t-${tone}${o.cls ? " " + o.cls : ""}"><path class="bx-sd" d="${path(Pj, sd, true)}"/><path class="bx-fr" d="${path(Pj, fr, true)}"/><path class="bx-top" d="${path(Pj, top, true)}"/></g>` });
  }
  // a planar quad face drawn as one path (used by the tilted beam)
  function face(sc, Pj, vs, part, tone, key) { sc.boxes.push({ key, svg: `<g class="bx t-${tone}"><path class="${part}" d="${path(Pj, vs, true)}"/></g>` }); }
  const line = (sc, Pj, vs, cls, layer = "flat") => sc[layer].push(`<path class="ln ${cls}" d="${path(Pj, vs)}"/>`);
  const ring = (c, r, z = 0.05, n = 160, flip = true) => Array.from({ length: n + 1 }, (_, i) => [c[0] + r * Math.cos((2 * PI * i) / n), (flip ? -1 : 1) * (c[1] + r * Math.sin((2 * PI * i) / n)), z]);

  // ---- tags (screen-space text) with a greedy de-clutter inside the canvas; the font size comes from the canvas (video / desk / phone)
  const estW = (s) => [...String(s)].reduce((a, c) => a + (c.charCodeAt(0) > 0x2e80 ? 1.04 : 0.66), 0);
  function tagger(sc, cv) {
    const placed = [], W = cv.W, M = 7;
    const hit = (a, b) => a[0] < b[2] && b[0] < a[2] && a[1] < b[3] && b[1] < a[3];
    return (pt, text, cls = "", dx = 0, dy = 0, anchor = "start", o = {}) => {
      const fs = o.fs || cv.fs, w = estW(text) * fs * (cls.includes("title") ? 1.04 : 1), h = fs * 1.2, u = fs / 12;      // offsets are written for a 12-unit font and scale with the font
      let x = pt[0] + dx * u, y = pt[1] + dy * u;
      const r = () => { const x0 = anchor === "start" ? x : anchor === "end" ? x - w : x - w / 2; return [x0, y - h * 0.8, x0 + w, y + h * 0.28]; };
      let b = r();
      if (b[0] < M) { x += M - b[0]; b = r(); }
      if (b[2] > W - M) { x -= b[2] - (W - M); b = r(); }
      if (!o.fixed) { let k = 0; while (k++ < 9 && placed.some((q) => hit(q, b))) { y += h * 1.04; b = r(); } }
      if (b[1] < M) { y += M - b[1]; b = r(); }
      if (b[3] > cv.H - M) { y -= b[3] - (cv.H - M); b = r(); }
      placed.push(b);
      sc.tags.push(`<text class="fig-tag ${cls}" style="font-size:${fs}px" x="${n1(x)}" y="${n1(y)}" text-anchor="${anchor}">${esc(text)}</text>`);
    };
  }
  // ---- pins: a stem with a head (he = orange diamond, o = blue square, a = flag, ot = hollow blue circle)
  function pin(sc, Pj, x, y, z0, h, kind, big = true) {
    const b = Pj.p(x, y, z0), t = Pj.p(x, y, z0 + h), s = (big ? 5.6 : 3.2) * PS;
    sc.over.push(`<path class="pin-stem ${kind}" d="M${b.map(n1).join(" ")}L${t.map(n1).join(" ")}"/>`);
    const [cx, cy] = t;
    if (kind === "he") sc.over.push(`<path class="pin-head he" d="M${n1(cx)} ${n1(cy - s)}L${n1(cx + s)} ${n1(cy)}L${n1(cx)} ${n1(cy + s)}L${n1(cx - s)} ${n1(cy)}Z"/>`);
    else if (kind === "o") sc.over.push(`<rect class="pin-head o" x="${n1(cx - s * 0.85)}" y="${n1(cy - s * 0.85)}" width="${n1(s * 1.7)}" height="${n1(s * 1.7)}"/>`);
    else if (kind === "a") sc.over.push(`<path class="pin-head a" d="M${n1(cx)} ${n1(cy - s)}L${n1(cx + s * 1.5)} ${n1(cy - s * 0.4)}L${n1(cx)} ${n1(cy + s * 0.2)}Z"/>`);
    else sc.over.push(`<circle class="pin-head ot" cx="${n1(cx)}" cy="${n1(cy)}" r="${n1(s * 0.8)}"/>`);
  }
  const toneOf = { bare: "g", o1o2: "b", hehi: "o", other: "h" };            // h = the hatched tone of the "other" category (no invariant / no JSON)
  const toneFrozen = { "B-bind": "b", "B-attractor": "o", "B-stuck-L1": "g", "B-flail": "h" };
  const LAYOUT = (cv) => (cv.narrow ? { pitch: 24, XM: 300, dep: 15 } : { pitch: 25, XM: 540, dep: 16 });
  const unit = (S) => I18N[S.lang].unit;
  const pad = (v) => (v < 10 ? "0" + v : "" + v);

  // =============================================================================================== the scenes
  const S = {};

  // ---- 0 / 1: the problem figure, drawn from the prompt's coordinates (the board is the plane of the figure)
  S.geom = (S_, A, cv, st) => {
    begin(cv);
    const G = DATA.geometry, T = I18N[S_.lang].tags, pt = (k) => G.pts[k], sc = newScene(), tag = tagger(sc, cv), named = st.opt.show === "named";
    const X0 = -13.5, X1 = 26, Y0 = -12.5, Y1 = 15, wy = (y) => -y;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [X0, Y0, -1.4, X1, Y1, 6], cv.W, cv.H, 0.9, 0.84);
    box(sc, Pj, X0, Y0, X1 - X0, Y1 - Y0, 1.4, "p", -1.4, { key: -1e9, cls: "board" });
    for (let x = -10; x <= 25; x += 5) line(sc, Pj, [[x, Y0, 0], [x, Y1, 0]], x === 0 ? "mid" : "faint");
    for (let y = -10; y <= 10; y += 5) line(sc, Pj, [[X0, wy(y), 0], [X1, wy(y), 0]], y === 0 ? "mid" : "faint");
    for (const x of [-10, 0, 10, 20]) tag(Pj.p(x, Y1, 0), String(x), "muted", 0, 15, "middle");
    for (const y of [-10, 0, 10]) tag(Pj.p(X0, wy(y), 0), String(y), "muted", -6, 4, "end");
    // the two given circles
    line(sc, Pj, ring(pt("O1"), G.rad.K1), "thin g"); line(sc, Pj, ring(pt("O2"), G.rad.K2), "thin g");
    const ringX = ring(G.cO, G.rO);                                                              // the circle through X1..X4 (its centre and radius are those of the circle with diameter O1O2)
    if (!named) { line(sc, Pj, ringX, "thick bare"); }
    else {
      line(sc, Pj, ringX, "thick b");
      line(sc, Pj, ring(G.cH, G.rH), "thick o dash");
      line(sc, Pj, [[pt("O1")[0], wy(pt("O1")[1]), 0.1], [pt("O2")[0], wy(pt("O2")[1]), 0.1]], "seg b");
      line(sc, Pj, [[pt("He")[0], wy(pt("He")[1]), 0.1], [pt("Hi")[0], wy(pt("Hi")[1]), 0.1]], "seg o");
      DATA.geometry.gap_H.forEach((g, i) => {                                                      // each X to the nearest point of the HeHi circle (how far it is off)
        const x = pt("X" + (i + 1)), d = Math.hypot(x[0] - G.cH[0], x[1] - G.cH[1]), nx = [G.cH[0] + ((x[0] - G.cH[0]) / d) * G.rH, G.cH[1] + ((x[1] - G.cH[1]) / d) * G.rH];
        line(sc, Pj, [[x[0], wy(x[1]), 0.1], [nx[0], wy(nx[1]), 0.1]], "gap o");
      });
      const m = G.cO; sc.over.push(`<circle class="mid-dot" cx="${n1(Pj.p(m[0], wy(m[1]), 0.1)[0])}" cy="${n1(Pj.p(m[0], wy(m[1]), 0.1)[1])}" r="${n1(4.4 * PS)}"/>`);
    }
    const peg = (k, h, kind, lab, dx, dy) => { const p = pt(k); const b = Pj.p(p[0], wy(p[1]), 0), t = Pj.p(p[0], wy(p[1]), h);
      sc.over.push(`<path class="pin-stem ${kind}" d="M${b.map(n1).join(" ")}L${t.map(n1).join(" ")}"/><circle class="peg ${kind}" cx="${n1(t[0])}" cy="${n1(t[1])}" r="${n1(5 * PS)}"/>`); tag(t, lab, "pt " + kind, dx, dy); };
    peg("O1", 2.4, "b", "O1", -12, -7); peg("O2", 2.4, "b", "O2", 10, -9);
    peg("X1", 3.2, "w", "X1", -4, -12); peg("X2", 3.2, "w", "X2", 8, -10); peg("X3", 3.2, "w", "X3", 10, 10); peg("X4", 3.2, "w", "X4", -4, 22);
    peg("He", 2.4, "o", "He", 9, -9); peg("Hi", 2.4, "o", "Hi", 8, 18);
    if (!named) tag(Pj.p(G.cO[0], wy(G.cO[1] - G.rO), 0), T.ringBare, "title", 0, 34, "middle");
    else {
      tag(Pj.p(G.cO[0], wy(G.cO[1] - G.rO), 0), T.ringO, "title b", 0, 36, "middle");
      tag(Pj.p(G.cH[0], wy(G.cH[1] + G.rH), 0), T.ringH, "title o", 0, -14, "middle");
      tag(Pj.p(G.cO[0], wy(G.cO[1]), 0), "M", "pt b", 7, 17);
    }
    return flush(sc);
  };

  // ---- 2 / 3: the prompts as tapes cut at their own headings (the tape's length = the number of characters)
  S.sheets = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, sc = newScene(), tag = tagger(sc, cv), both = st.opt.both, SEG = DATA.seg, KC = cv.narrow ? 0.2 : 0.34;
    const lenO = DATA.prompts.open_len, lenB = DATA.prompts.blocked_len, DEP = 52, H = 9, GAP = both ? 110 : 0;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-48, -44, -6, lenB * KC + 40, GAP + DEP + 60, 46], cv.W, cv.H, 0.96, 0.9);
    box(sc, Pj, -40, -34, lenB * KC + 60, GAP + DEP + 62, 6, "p", -6, { key: -1e9 });
    const tape = (y, segs, lbl, tail) => {
      segs.forEach((s, i) => box(sc, Pj, s.a * KC, y, (s.b - s.a) * KC - 0.8, DEP, H, i % 2 ? "x" : "g", 0));
      if (tail) box(sc, Pj, lenO * KC, y, (lenB - lenO) * KC, DEP, H, "l", 0);
      tag(Pj.p(0, y, 0), lbl, "title", -4, 4, "end");
    };
    tape(0, SEG, `${T.open}`, false);
    SEG.forEach((s, i) => tag(Pj.p(((s.a + s.b) / 2) * KC, 0, H), `${T.seg[i]} ${s.b - s.a}`, "muted", 0, i % 2 ? -26 : -12, "middle"));
    if (both) { tape(GAP, SEG, `${T.blocked}`, true);
      tag(Pj.p(((lenO + lenB) / 2) * KC, GAP + DEP, H), `+${DATA.prompts.tail_len} ${unit(S_)}`, "title", 0, 24, "middle");
      tag(Pj.p((lenO / 2) * KC, GAP + DEP, 0), `${T.same} ${lenO} ${unit(S_)}`, "muted", 0, 24, "middle");
      sc.flat.push(`<path class="ln lit" d="${path(Pj, [[lenO * KC, GAP - 6, 0.1], [lenO * KC, GAP + DEP + 6, 0.1]])}"/>`); }
    else tag(Pj.p((lenO / 2) * KC, DEP, 0), `${lenO} ${unit(S_)}`, "title", 0, 28, "middle");
    return flush(sc);
  };

  // ---- 4 / 6 / 7 / 8 / 10: the bands — one slab per row (length = number of characters, log scale), pins on it, a tile for the frozen (whole-text) label at its left.
  //      opt.conds = ["open", "blocked"] draws all 20 rows in one picture (the core picture); the condition that is not `focusCond` is drawn faded as a reference.
  S.bands = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, o = st.opt, conds = o.conds || [o.cond], multi = conds.length > 1, focusCond = o.focusCond || conds[0], sc = newScene(), tag = tagger(sc, cv);
    const rowsAll = conds.flatMap((c) => DATA.rows.filter((r) => r.cond === c));
    const pitch = cv.narrow ? 25 : multi ? 23 : 27, GG = multi ? (cv.narrow ? 40 : 40) : 0, XM = cv.narrow ? 300 : 520, dep = cv.narrow ? 16 : multi ? 15 : 18, TH = 7, LX = (n) => (XM * Math.log10(1 + n)) / Math.log10(1 + DATA.logmax);
    const yOf = (r) => (conds.indexOf(r.cond) * 10 + r.seed) * pitch + conds.indexOf(r.cond) * GG + 2, YB = rowsAll.length * pitch + (conds.length - 1) * GG;
    const emph = new Set([...(o.emph || []), S_.t]), LABX = XM + 16;
    const HY = multi ? -34 : -14;                                                                     // the column headers sit higher when a group title takes the row above the first slab
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-66, HY - 16, -6, XM + (cv.narrow ? 74 : 150), YB + 24, 50], cv.W, cv.H, 0.97, 0.92);
    box(sc, Pj, -56, HY - 2, XM + 76 + (cv.narrow ? 0 : 76), YB + 14 - HY, 5, "p", -5, { key: -1e9 });
    [10, 100, 1000, 10000, 100000].forEach((v, i) => { line(sc, Pj, [[LX(v), -12, 0], [LX(v), YB + 10, 0]], "faint"); tag(Pj.p(LX(v), YB + 10, 0), ["10", "100", "1k", "10k", "100k"][i], "muted", 0, 15, "middle"); });
    tag(Pj.p(XM / 2, YB + 10, 0), T.axisLog, "muted", 0, 32, "middle");
    tag(Pj.p(-28, HY, 0), T.colFrozen, "muted", 0, -6, "middle"); tag(Pj.p(XM * (multi ? 0.66 : 0.4), HY, TH), T.colAnswer, "muted", 0, -10, "middle");
    tag(Pj.p(LABX, HY, 0), cv.narrow ? "n" : (S_.lang === "en" ? "chars · He · O sentences" : "字数 · He文 · O文"), "muted", 0, -6, "start", { fixed: true });
    if (multi) conds.forEach((c) => { const first = rowsAll.find((r) => r.cond === c); tag(Pj.p(-44, yOf(first) - 10, 0), c === focusCond || cv.narrow ? c : `${c} (${T.ghost})`, c === focusCond ? "title" : "muted", 0, 0, "start", { fixed: true }); });
    rowsAll.forEach((r) => {
      const y = yOf(r), ghost = multi && r.cond !== focusCond, on = !ghost && emph.has(r.seed), tone = toneOf[r.reading], cls = ghost || (o.fade && !on) ? "dim" : "", tg = ghost ? " dimtag" : "";
      if (on) line(sc, Pj, [[-48, y - 3, 0.1], [LABX - 6, y - 3, 0.1], [LABX - 6, y + dep + 3, 0.1], [-48, y + dep + 3, 0.1], [-48, y - 3, 0.1]], "lit");
      box(sc, Pj, -38, y + 2, 17, dep - 4, 3.5, toneFrozen[r.label], 0, { cls });                  // the frozen label (the whole text went through the classifier)
      box(sc, Pj, 0, y, LX(r.n_chars), dep, TH, tone, 0, { cls });
      tag(Pj.p(-40, y + dep / 2, 0), `s${r.seed}`, (on ? "pt strong" : "pt") + tg, -2, 4, "end");
      const g = ghost ? 0.4 : 1;
      if (!ghost) {
        r.he_diam.forEach((p) => line(sc, Pj, [[LX(p), y + dep * 0.1, TH + 0.06], [LX(p), y + dep * 0.46, TH + 0.06]], "tk he"));          // every hit of the predicate, flat on the slab's top (a barcode)
        r.o_name.forEach((p) => line(sc, Pj, [[LX(p), y + dep * 0.54, TH + 0.06], [LX(p), y + dep * 0.9, TH + 0.06]], "tk o"));
      }
      if (r.ans_start >= 0) pin(sc, Pj, LX(r.ans_start), y + dep / 2, TH, ghost ? 12 : 17, "a", !ghost);
      if (r.he_diam.length) pin(sc, Pj, LX(r.he_diam[0]), y + dep * 0.28, TH, ghost ? 12 : 22, "he", !ghost);
      if (r.o_name.length) pin(sc, Pj, LX(r.o_name[0]), y + dep * 0.72, TH, ghost ? 12 : 22, "o", !ghost);
      if (!cv.narrow && o.otok && !ghost && r.o_tok_first !== null && !r.o_name.length) pin(sc, Pj, LX(r.o_tok_first), y + dep * 0.72, TH, 20, "ot");
      const lab = cv.narrow ? `${r.n_chars}` : `${r.n_chars}${r.hit_cap ? " cap" : ""} · ${r.he_diam.length} · ${r.o_name.length}`;
      tag(Pj.p(LABX, y + dep / 2, 0), lab, (on ? "pt strong" : "pt muted") + tg, 0, 5, "start", { fixed: true });
    });
    return flush(sc);
  };

  // ---- 5: three tiers (the frozen whole-text label / does the text contain a He or Hi word / the answer field), one column per row; the tiers that disagree are threaded
  S.tiers = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, rows = DATA.rows.filter((r) => r.cond === "open"), sc = newScene(), tag = tagger(sc, cv), CP = cv.narrow ? 25 : 40, TL = cv.narrow ? 70 : 78, W0 = cv.narrow ? 19 : 29, DP = cv.narrow ? 19 : 29;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-70, -26, -6, rows.length * CP + 60, TL * 2 + DP + 40, 40], cv.W, cv.H, 0.96, 0.9);
    box(sc, Pj, -62, -16, rows.length * CP + 82, TL * 2 + DP + 30, 5, "p", -5, { key: -1e9 });
    const ys = [0, TL, TL * 2], on = S_.t;
    ys.forEach((y, ti) => tag(Pj.p(-14, y + DP / 2, 0), T.tier[ti], "title", 0, 4, "end"));
    rows.forEach((r, i) => {
      const x = i * CP, c1 = toneFrozen[r.label], c3 = toneOf[r.reading], cls = r.seed === on ? "hot" : "";
      box(sc, Pj, x, ys[0], W0, DP, 6, c1, 0, { cls });
      box(sc, Pj, x, ys[1], W0, DP, 2.5, "p", 0);
      if (r.has_hehi_word) pin(sc, Pj, x + W0 / 2, ys[1] + DP / 2, 2.5, 16, "he");
      box(sc, Pj, x, ys[2], W0, DP, 6, c3, 0, { cls });
      if (c1 !== c3 || (r.label === "B-attractor" && r.reading !== "hehi")) { sc.flat.push(`<path class="ln thread" d="${path(Pj, [[x + W0 / 2, ys[0] + DP, 0.1], [x + W0 / 2, ys[2], 0.1]])}"/>`); }
      tag(Pj.p(x + W0 / 2, ys[2] + DP, 0), `s${r.seed}`, r.seed === on ? "pt strong" : "pt", 0, 16, "middle");
    });
    tag(Pj.p(rows.length * CP + 14, ys[0] + DP / 2, 0), T.tier1sum, "pt", 8, 4);
    tag(Pj.p(rows.length * CP + 14, ys[2] + DP / 2, 0), T.tier3sum, "pt", 8, 4);
    return flush(sc);
  };

  // ---- 9: two sentences x two conditions: which rows contain the sentence (a raised cube) and where the row ends up
  S.hyp = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, sc = newScene(), tag = tagger(sc, cv), CW = cv.narrow ? 24 : 30, CD = cv.narrow ? 17 : 22, RL = 10 * CW, GX = cv.narrow ? 0 : RL + 84, GY = cv.narrow ? 170 : 0;
    const YT = (cv.narrow ? GY : 0) + 56 + CD + 66, XT = cv.narrow ? RL + 20 : GX + RL + 40;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-60, -44, -6, XT, YT, 40], cv.W, cv.H, 0.94, 0.88);
    box(sc, Pj, -54, -38, XT + 50, YT + 40, 5, "p", -5, { key: -1e9 });
    const groups = [{ tone: "b", title: T.hypO, field: "o_name", gx: 0, gy: 0 }, { tone: "o", title: T.hypHe, field: "he_diam", gx: GX, gy: GY }];
    for (const g of groups) {
      tag(Pj.p(g.gx + RL / 2, g.gy - 22, 0), g.title, "title " + g.tone, 0, -2, "middle");
      ["open", "blocked"].forEach((cond, ci) => {
        const y = g.gy + ci * 56, rs = DATA.rows.filter((r) => r.cond === cond), n = rs.filter((r) => r[g.field].length).length;
        tag(Pj.p(g.gx - 4, y + CD / 2, 0), cond, "pt", 0, 4, "end");
        rs.forEach((r, i) => { const has = r[g.field].length > 0; box(sc, Pj, g.gx + i * CW, y, CW - 5, CD, has ? 15 : 1.4, has ? g.tone : "x", 0, { cls: r.seed === S_.t ? "hot" : "" }); if (ci === 1) tag(Pj.p(g.gx + i * CW + CW / 2 - 2, y + CD, 0), `${i}`, "pt muted", 0, 14, "middle"); });
        tag(Pj.p(g.gx + RL, y + CD / 2, 0), `${n} / 10`, "title " + (n ? g.tone : ""), 6, 6);
      });
    }
    const hy = groups[1];                                                                                // where the five rows with a He-Hi sentence end up (the answer field's reading)
    DATA.rows.filter((r) => r.cond === "blocked" && r.he_diam.length).forEach((r) => {
      const x = hy.gx + r.seed * CW, y = hy.gy + 56 + CD + 24;
      line(sc, Pj, [[x + CW / 2 - 2, hy.gy + 56 + CD, 0.1], [x + CW / 2 - 2, y, 0.1]], "thread");
      box(sc, Pj, x, y, CW - 5, 12, 3.5, toneOf[r.reading], 0);
    });
    tag(Pj.p(hy.gx - 4, hy.gy + 56 + CD + 30, 0), T.hypEnd, "pt muted", 0, 6, "end");
    return flush(sc);
  };

  // ---- 11: the three cues (stacks of the frozen labels, cap rows removed), open behind and blocked in front
  S.cue = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, sc = newScene(), tag = tagger(sc, cv), CU = DATA.cue_table, keys = ["nl", "sp", "nn"], order = ["B-bind", "B-attractor", "B-stuck-L1", "B-flail"], CP = cv.narrow ? 100 : 170, SZ = cv.narrow ? 40 : 62, UH = cv.narrow ? 6.5 : 8.5, RG = cv.narrow ? 150 : 175;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-90, -40, -6, keys.length * CP + 40, RG + SZ + 50, 100], cv.W, cv.H, 0.95, 0.9);
    box(sc, Pj, -80, -34, keys.length * CP + 100, RG + SZ + 70, 5, "p", -5, { key: -1e9 });
    ["open", "blocked"].forEach((cond, ci) => {
      const y = ci * RG;
      tag(Pj.p(-14, y + SZ / 2, 0), cond, "title", 0, 4, "end");
      keys.forEach((k, i) => {
        const x = i * CP, c = CU[k][cond], lab = c.labels_primary; let z = 0;
        order.forEach((L) => { for (let u = 0; u < (lab[L] || 0); u++) { box(sc, Pj, x, y, SZ, SZ, UH - 0.7, toneFrozen[L], z, {}); z += UH; } });
        tag(Pj.p(x + SZ / 2, y + SZ / 2, z), `${CU[k].cue === "' '" ? T.space : CU[k].cue}`, "title", 0, -10, "middle", { fixed: true });
        const txt = cv.narrow ? (cond === "blocked" ? `${lab["B-bind"] || 0}/${c.n_primary}` : `n${c.n_primary}`) : cond === "blocked" ? `bind ${lab["B-bind"] || 0} / ${c.n_primary}${c.cap ? ` (cap ${c.cap})` : ""}` : `n ${c.n_primary}${c.cap ? ` (cap ${c.cap})` : ""}`;
        tag(Pj.p(x + SZ + 4, y + SZ / 2, 0), txt, cond === "blocked" ? "pt strong" : "pt muted", 8, 6, "start", { fixed: true });
      });
    });
    return flush(sc);
  };

  // ---- 12: one row (F5a-2 s1) laid out as a linear band with the two decision sites and the answer's start
  S.timeline = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, F = DATA.f5, sa = DATA.cmt13.sites.find((s) => s.key === "att|F5a-2|s1"), sb = DATA.cmt13.sites.find((s) => s.key === "cut|F5a-2|s1"), sc = newScene(), tag = tagger(sc, cv);
    const XM = cv.narrow ? 330 : 700, LX = (n) => (XM * n) / F.n_chars, DEP = 46, H = 10;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-40, -60, -6, XM + 60, DEP + 90, 80], cv.W, cv.H, 0.95, 0.88);
    box(sc, Pj, -30, -50, XM + 70, DEP + 110, 5, "p", -5, { key: -1e9 });
    [0, 2000, 4000, 6000, 8000].forEach((v) => { line(sc, Pj, [[LX(v), -8, 0], [LX(v), DEP + 8, 0]], "faint"); tag(Pj.p(LX(v), DEP + 8, 0), v === 0 ? "0" : `${v / 1000}k`, "muted", 0, 15, "middle"); });
    box(sc, Pj, 0, 0, LX(F.ans_start), DEP, H, "g", 0);
    box(sc, Pj, LX(F.ans_start), 0, XM - LX(F.ans_start), DEP, H, "b", 0);
    pin(sc, Pj, LX(F.att_at), DEP * 0.3, H, 40, "he"); pin(sc, Pj, LX(F.cut_at), DEP * 0.7, H, 40, "o"); pin(sc, Pj, LX(F.ans_start), DEP / 2, H, 30, "a");
    tag(Pj.p(LX(F.att_at), DEP * 0.3, H + 40), `① t ${sa.t} ${sa.written.trim()} · Δ ${sa.delta_out.toFixed(2)}`, "title o", -8, -16, "end");
    tag(Pj.p(LX(F.cut_at), DEP * 0.7, H + 40), `② t ${sb.t} ${sb.written.trim()} · Δ +${sb.delta_out.toFixed(2)}`, "title b", 10, -16, "start");
    tag(Pj.p(LX(F.ans_start), DEP / 2, H + 30), T.ansStart, "pt", 0, -14, "middle");
    tag(Pj.p(XM / 2, 0, 0), `${F.row} · ${F.n_chars} ${unit(S_)} · ${T.linear}`, "muted", 0, -42, "middle");
    return flush(sc);
  };

  // ---- 13 / 14: the balance — two pans (the two pairs of heads that came in the top 10), the beam tips toward the heavier pan; a gauge reads the output's own difference
  S.balance = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, site = DATA.cmt13.sites[clamp(S_.t, 0, DATA.cmt13.sites.length - 1)], sc = newScene(), tag = tagger(sc, cv);
    const BW = 112, POST = 150, HANG = 92, BS = 4.6, PW = 62, PD = 44, BK = 38;
    const diff = site.o_sum + site.he_sum, th = clamp(diff * 3.4, -26, 26) * (PI / 180), dz = BW * Math.sin(th), zc = POST, zl = zc - dz, zr = zc + dz;     // diff > 0: the O pan (left) is heavier and goes down
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-BW - 70, -60, -6, BW + (cv.narrow ? 240 : 200), 60, POST + (cv.narrow ? 80 : 30)], cv.W, cv.H, 0.92, 0.86);
    box(sc, Pj, -BW - 56, -40, 2 * BW + (cv.narrow ? 260 : 220), 80, 7, "p", -7, { key: -1e9 });
    box(sc, Pj, -7, -7, 14, 14, POST, "x", 0, { key: -5e8 });                                            // the post
    const yF = 5, yB = -5, tt = 3.2;
    face(sc, Pj, [[-BW, yB, zl + tt], [BW, yB, zr + tt], [BW, yF, zr + tt], [-BW, yF, zl + tt]], "bx-top", "x", 5e8);
    face(sc, Pj, [[-BW, yF, zl - tt], [BW, yF, zr - tt], [BW, yF, zr + tt], [-BW, yF, zl + tt]], "bx-fr", "x", 5e8 + 1);
    sc.over.push(`<circle class="peg w" cx="${n1(Pj.p(0, 0, zc)[0])}" cy="${n1(Pj.p(0, 0, zc)[1])}" r="${n1(5.4 * PS)}"/>`);
    const pans = [{ side: "O", x: -BW, z: zl, tone: "b", val: site.o_sum, heads: site.heads.filter((h) => h.grp === "O") }, { side: "He", x: BW, z: zr, tone: "o", val: site.he_sum, heads: site.heads.filter((h) => h.grp === "He") }];
    for (const p of pans) {
      const pz = p.z - HANG;
      for (const dx of [-PW / 2 + 4, PW / 2 - 4]) line(sc, Pj, [[p.x, 0, p.z], [p.x + dx, 0, pz + 4]], "string", "over");
      box(sc, Pj, p.x - PW / 2, -PD / 2, PW, PD, 4, "g", pz, { key: Pj.depth(p.x, 0) * 10 + 1e6 });
      let zz = pz + 4; const hs = [...p.heads].sort((a, b) => Math.abs(b.contrib) - Math.abs(a.contrib));
      hs.forEach((h) => { const bh = Math.abs(h.contrib) * BS; box(sc, Pj, p.x - BK / 2, -BK / 2, BK, BK, bh - 0.6, p.tone, zz, { key: Pj.depth(p.x, 0) * 10 + 1e6 + zz, cls: h.head === "L50H23" ? "lit50" : "" });
        if (!cv.narrow || h.head === "L50H23") tag(Pj.p(p.x + BK / 2, 0, zz + bh / 2), `${h.head} ${(h.contrib >= 0 ? "+" : "") + h.contrib.toFixed(2)}`, "pt " + (h.head === "L50H23" ? "strong" : ""), 8, 4, "start");      // the phone labels only L50H23 (the list of all heads is in the text under the figure)
        zz += bh; });
      if (!hs.length) tag(Pj.p(p.x, 0, pz + 4), T.noHead, "pt muted", 0, -6, "middle");
      tag(Pj.p(p.x, 0, pz), `${p.side === "O" ? T.panO : T.panHe} ${(p.val >= 0 ? "+" : "") + p.val.toFixed(2)}`, "title " + p.tone, 0, 30, "middle");
    }
    // the output's own difference: a gauge on the right of the base (the card's delta_out; it is not computed from the pans). Positive (O) is on the left, like the O pan.
    const gx = BW + (cv.narrow ? 150 : 128), gz = cv.narrow ? 150 : 74, gr = 42, ang = (v) => ((10 - clamp(v, -10, 10)) / 20) * PI, at = (v, r) => [gx - r * Math.cos(ang(v)), 0, gz + r * Math.sin(ang(v))];
    line(sc, Pj, Array.from({ length: 41 }, (_, i) => at(10 - i * 0.5, gr)), "gauge", "over");
    for (const v of [-10, -5, 0, 5, 10]) line(sc, Pj, [at(v, gr - 6), at(v, gr)], "gauge", "over");
    box(sc, Pj, gx - 5, -5, 10, 10, gz - 2, "x", 0, { key: -4e8 });
    line(sc, Pj, [[gx, 0, gz], at(site.delta_out, gr - 4)], "needle", "over");
    sc.over.push(`<circle class="peg w" cx="${n1(Pj.p(gx, 0, gz)[0])}" cy="${n1(Pj.p(gx, 0, gz)[1])}" r="${n1(4.4 * PS)}"/>`);
    tag(Pj.p(gx, 0, gz + gr), T.gauge, "pt", 0, -12, "middle");
    tag(Pj.p(gx, 0, gz), `${site.delta_out >= 0 ? "+" : ""}${site.delta_out.toFixed(2)}`, "title", 0, 28, "middle");
    tag(Pj.p(gx - gr, 0, gz), T.gaugeO, "pt b", -2, -6, "end", { fixed: true }); tag(Pj.p(gx + gr, 0, gz), T.gaugeHe, "pt o", 2, -6, "start", { fixed: true });
    return flush(sc);
  };

  // ---- 15: the 16 sites x the 10 heads that came in each site's top 10 (x = layer, y = site, height = contribution from a zero plane)
  S.pillars = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, sites = DATA.cmt13.sites.slice().sort((a, b) => (a.kind === b.kind ? a.variant.localeCompare(b.variant) || a.seed - b.seed : a.kind === "att" ? -1 : 1)), sc = newScene(), tag = tagger(sc, cv);
    const layers = sites.flatMap((s) => s.heads.map((h) => h.layer)), L0 = Math.min(...layers), L1 = Math.max(...layers), PX = cv.narrow ? 8.4 : 16, PY = cv.narrow ? 14 : 24, Z0 = 38, ZS = cv.narrow ? 5.6 : 8.4, W0 = PX * 0.62, GAPY = 16;
    const yOf = (i) => i * PY + (sites[i].kind === "cut" ? GAPY : 0), YT = yOf(sites.length - 1) + PY;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-70, -30, -50, (L1 - L0 + 2) * PX + 30, YT + 40, Z0 + 46], cv.W, cv.H, 0.95, 0.88);
    box(sc, Pj, -60, -20, (L1 - L0 + 2) * PX + 70, YT + 40, 5, "p", -50, { key: -1e9 });
    sc.flat.push(`<path class="ln zero" d="${path(Pj, [[-8, -8, Z0], [(L1 - L0 + 2) * PX + 6, -8, Z0], [(L1 - L0 + 2) * PX + 6, YT + 4, Z0], [-8, YT + 4, Z0]], true)}"/>`);
    for (let L = Math.ceil(L0 / 5) * 5; L <= L1; L += 5) { line(sc, Pj, [[(L - L0) * PX + PX / 2, -8, Z0], [(L - L0) * PX + PX / 2, YT + 4, Z0]], "faint"); tag(Pj.p((L - L0) * PX + PX / 2, YT + 4, Z0), String(L), "muted", 0, 15, "middle"); }
    tag(Pj.p(((L1 - L0) * PX) / 2, YT + 4, Z0), T.layer, "muted", 0, 31, "middle");
    sites.forEach((s, i) => {
      const y = yOf(i), key = s.key, mom = key === "att|F5a-2|s1" || key === "cut|F5a-2|s1";
      const nth = s.kind === "att" ? sites.slice(0, i + 1).filter((q) => q.kind === "att").length : sites.slice(0, i + 1).filter((q) => q.kind === "cut").length, nOf = sites.filter((q) => q.kind === s.kind).length;
      if (!cv.narrow || mom || nth === 1 || nth === nOf) tag(Pj.p(-8, y + PY / 2, Z0), `${s.kind === "att" ? "A" : "C"}${nth}${mom ? (s.kind === "att" ? " ①" : " ②") : ""}`, mom ? "pt strong" : "pt", 0, 4, "end");
      const slot = {};
      s.heads.forEach((h) => {
        const k = h.layer, c = (slot[k] = (slot[k] || 0) + 1) - 1, x = (k - L0) * PX + (PX - W0) / 2, yy = y + c * (PY * 0.32), hh = Math.max(0.6, Math.abs(h.contrib) * ZS), tone = h.grp === "O" ? "b" : h.grp === "He" ? "o" : "g";
        box(sc, Pj, x, yy, W0, PY * 0.3, hh, tone, h.contrib >= 0 ? Z0 : Z0 - hh, { cls: (h.head === "L50H23" ? "lit50 " : "") + (mom ? "" : "") });
      });
    });
    return flush(sc);
  };

  // ---- 16 / 17: flat charts (plane): stacks of unit cells by label
  const CELL = { "B-bind": "b", "B-attractor": "o", "B-stuck-L1": "g", "B-flail": "h", "length": "len" };
  const cells = (x, y, w, h, counts, order) => { let s = "", cx = x; for (const L of order) for (let i = 0; i < (counts[L] || 0); i++) { s += `<rect class="cell c-${CELL[L]}" x="${n1(cx)}" y="${n1(y)}" width="${n1(w - 2)}" height="${n1(h)}"/>`; cx += w; } return s; };
  S.models = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, sc = newScene(), tag = tagger(sc, cv), ms = DATA.models, order = ["B-bind", "B-attractor", "B-stuck-L1", "B-flail"], key = { "B-bind": "bind", "B-attractor": "attractor", "B-stuck-L1": "stuck_L1", "B-flail": "flail" };
    const nar = cv.narrow, CWd = nar ? 16 : 24, CHt = nar ? 18 : 22, RH = nar ? 76 : 46, NX = nar ? 12 : 24, X0 = nar ? 14 : 250, X1 = nar ? 14 + 10 * CWd + 170 : X0 + 10 * CWd + 110, Y0 = nar ? 100 : 80, GAP = nar ? 44 : 24;
    let s = "";
    tag([X0, Y0 - (nar ? 56 : 40)], T.mOpen, "title", 0, 0); tag([X1, Y0 - (nar ? 56 : 40)], T.mBlocked, "title", 0, 0);
    ms.forEach((m, i) => {
      const y = Y0 + i * RH + (i >= 5 ? GAP : 0) + (i >= 0 ? (nar ? GAP : 0) : 0);
      if (i === 0) tag([NX, y - (nar ? 14 : 14)], T.mApi, "muted", 0, 0); if (i === 5) tag([NX, y - 14], T.mOllama, "muted", 0, 0);
      tag([NX, y + (nar ? 20 : 18)], m.model.replace("-20251001", "") + (m.model === "qwen3:30b-a3b" ? " (MoE)" : ""), "pt strong", 0, 0);
      const by = y + (nar ? 32 : 0), cnt = (c) => Object.fromEntries(order.map((L) => [L, c[key[L]]]));
      s += cells(X0, by, CWd, CHt, cnt(m.open), order) + cells(X1, by, CWd, CHt, cnt(m.blocked), order);
      tag([X0 + m.open.n * CWd + 6, by + (nar ? 16 : 17)], `bind ${m.open.bind}/${m.open.n}`, "pt muted", 0, 0, "start", { fixed: true });
      tag([X1 + m.blocked.n * CWd + 6, by + (nar ? 16 : 17)], `bind ${m.blocked.bind}/${m.blocked.n}${m.model === "qwen3:32b" ? (nar ? " a7" : " · att 7") : ""}`, "pt " + (m.model === "qwen3:32b" ? "strong" : "muted"), 0, 0, "start", { fixed: true });
    });
    return `<rect class="chartbg" x="2" y="2" width="${cv.W - 4}" height="${cv.H - 4}" rx="6"/>` + s + sc.tags.join("");
  };
  // wrap a long tag into lines that fit a width (by the same width estimate the tagger uses); used where the phone cannot hold one long line
  const lines = (text, maxW, fs) => { const out = []; let cur = ""; for (const ch of [...String(text)]) { if (estW(cur + ch) * fs > maxW && cur && !"。、」)・.,".includes(ch)) { const k = cur.lastIndexOf(" "); if (ch !== " " && ch.charCodeAt(0) < 0x2e80 && k > 0) { out.push(cur.slice(0, k)); cur = cur.slice(k + 1) + ch; } else { out.push(cur); cur = ch.trim() ? ch : ""; } } else cur += ch; } if (cur) out.push(cur); return out; };
  S.think = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, sc = newScene(), tag = tagger(sc, cv), th = DATA.think, nar = cv.narrow, CWd = nar ? 26 : 40, X0 = nar ? 14 : 250, order = ["B-bind", "B-attractor", "B-stuck-L1", "B-flail", "length"], LX = nar ? 12 : 24, maxW = cv.W - 2 * LX;
    let s = "", y = nar ? 60 : 70;
    const put = (text, cls, dy = 0) => { for (const ln of nar ? lines(text, maxW * (cls.includes("title") ? 0.86 : 0.94), cv.fs) : [text]) { tag([LX, y + dy], ln, cls, 0, 0, "start", { fixed: true }); y += cv.fs * 1.35; } };
    put(T.thinkTitle, "title"); y += nar ? 16 : 12;
    // v3: the base model's rows (the 10 + 10 rows of chapters 3-4) beside Think: a row that hit the cap is drawn as a cut row (its whole-text label is told in the text)
    const rowsOf = (cond) => [[T.thinkRowTh, { ...th[cond].labels, length: th[cond].length }, th[cond].labels, th[cond].length], [T.thinkRowBase, { ...th.base[cond].labels_no_cap, length: th.base[cond].cap }, th.base[cond].labels_no_cap, th.base[cond].cap]];
    ["open", "blocked"].forEach((cond) => {
      tag([LX, y + (nar ? 4 : 4)], cond, "title", 0, 0, "start", { fixed: true }); y += nar ? 24 : 6;
      rowsOf(cond).forEach(([nm, counts, labels, cut]) => {
        const txt = `${Object.entries(labels).map(([k, v]) => `${k.replace("B-", "")} ${v}`).join(" · ")} · ${T.capCut} ${cut}`;
        if (nar) { tag([LX, y + 16], nm, "pt muted", 0, 0, "start", { fixed: true }); y += cv.fs * 1.5; }
        else tag([LX + 14, y + 20], nm, "pt muted", 0, 0, "start", { fixed: true });
        s += cells(X0, y, CWd, 30, counts, order);
        if (nar) { y += 30 + 8; put(txt, "pt muted"); y += 8; } else { tag([X0 + 10 * CWd + 16, y + 20], txt, "pt muted", 0, 0, "start", { fixed: true }); y += 30 + 14; }
      });
      y += nar ? 14 : 14;
    });
    put(T.thinkNote, "muted");
    return `<rect class="chartbg" x="2" y="2" width="${cv.W - 4}" height="${cv.H - 4}" rx="6"/>` + s + sc.tags.join("");
  };
  // =============================================================================================== v2: the olm59 chapter (the construction predicates x the SAE trajectory)
  const GN = ["close", "mid", "ans", "think"];                                      // the order of the four groups (olm7's names; the words are in I18N[lang].tags.grp)
  const sgn2 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(2);
  const runsOf = (mask, bit, lo, hi) => { const out = []; let a = -1; for (let i = lo; i <= hi; i++) { const on = i >= 0 && i < mask.length && ((mask[i] >> bit) & 1) === 1; if (on && a < 0) a = i; if (!on && a >= 0) { out.push([a, i - 1]); a = -1; } } if (a >= 0) out.push([a, hi]); return out; };
  // ---- 18 / 19 / 20: one token axis. Above: the marks of the construction predicates (what the text names). Below: the four groups' values (the mean of each group's SAE latents, layer 32).
  //      opt.row = "O" (S_O, the whole row) | "H" (S_H, the whole row) | "both" (S_O above S_H, aligned at the event, the same scale, 32 tokens each side). S.t = the cursor token (both: 0..63, 32 = the event).
  S.traj = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, D = DATA.olm59, HF = D.half, both = st.opt.row === "both", sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow;
    const blocks = both ? [["O", D.S_O, "b"], ["H", D.S_H, "o"]] : st.opt.row === "O" ? [["O", D.S_O, "b"]] : [["H", D.S_H, "o"]];
    const XM = nar ? 300 : 600, ZS = nar ? (both ? 14 : 18) : both ? 12 : 15, LP = both ? (nar ? 56 : 46) : (nar ? 84 : 64), MP = nar ? 22 : 20, nM = both ? 1 : 4, GM = both ? (nar ? 16 : 12) : (nar ? 26 : 18), BG = both ? (nar ? 84 : 92) : 0, XL = nar ? -150 : -196, XR = nar ? 44 : 40;
    const blkH = nM * MP + GM + 4 * LP, YT = blocks.length * blkH + (blocks.length - 1) * BG;
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [XL - 12, nar ? -76 : -64, -6, XM + XR + 10, YT + 56, 4.2 * ZS + 12], cv.W, cv.H, 0.97, 0.93);
    box(sc, Pj, XL - 8, nar ? -70 : -58, XM - XL + XR + 14, YT + (nar ? 124 : 112), 5, "p", -5, { key: -1e9 });
    const flat = [];                                                                             // flat layer in insertion order: windows first, then the ribbons, then the lines
    blocks.forEach(([key, R, tone], bi) => {
      const N = R.n, e = R.event, y0 = bi * (blkH + BG), lo = both ? e - HF : 0, hi = both ? e + HF - 1 : N - 1, xOf = (i) => ((i - lo) * XM) / (hi - lo), cur = both ? e - HF + clamp(S_.t, 0, 2 * HF - 1) : clamp(S_.t, 0, N - 1);
      const yG = (gi) => y0 + nM * MP + GM + gi * LP + LP - 6;                                    // the baseline of the group lane gi (the ribbon stands on it, facing the viewer)
      tag(Pj.p(XL, y0 - (nar ? 46 : 38), 0), nar ? (key === "O" ? T.rowOs : T.rowHs) : (key === "O" ? T.rowO : T.rowH), "title " + tone, 0, 0, "start", { fixed: true });
      const xb0 = xOf(e - HF), xe = xOf(e), xa1 = xOf(e + HF - 1);                                 // the windows: [e-32, e) and [e, e+32)
      flat.push(`<path class="win before" d="${path(Pj, [[xb0, y0 - 6, 0.05], [xe, y0 - 6, 0.05], [xe, y0 + blkH + 2, 0.05], [xb0, y0 + blkH + 2, 0.05]], true)}"/>`);
      flat.push(`<path class="win after" d="${path(Pj, [[xe, y0 - 6, 0.05], [xa1, y0 - 6, 0.05], [xa1, y0 + blkH + 2, 0.05], [xe, y0 + blkH + 2, 0.05]], true)}"/>`);
      // marks lanes (what the text names): the thin lanes above the groups
      const lanes = both ? [[2, "d"]] : [[0, "O"], [1, "H"], [2, "d"], [5, "J"]];
      lanes.forEach(([bit, nm], li) => {
        const y = y0 + li * MP;
        box(sc, Pj, 0, y + 2, XM, MP - 6, 0.8, "x", 0, {});
        if (nm === "d") { for (const [b2, tn] of [[2, "b"], [3, "o"]]) for (const [a, b] of runsOf(R.mask, b2, lo, hi)) box(sc, Pj, xOf(a), y + 1, Math.max(1.8, xOf(b + 1) - xOf(a)), MP - 4, 6, tn, 0.8, {}); }
        else for (const [a, b] of runsOf(R.mask, bit, lo, hi)) box(sc, Pj, xOf(a), y + 1, Math.max(1.5, xOf(b + 1) - xOf(a)), MP - 4, nm === "J" ? 2.4 : 3.6, nm === "O" ? "b" : nm === "H" ? "o" : "g", 0.8, {});
        tag(Pj.p(-10, y + MP / 2, 0), both ? T.mk[2] : T.mk[li], "pt" + (nm === "d" ? " strong" : ""), 0, 4, "end", { fixed: true });
      });
      // group lanes: the ribbon (area + top edge), the two window means, the cursor's value, the name and the before -> after at the left
      GN.forEach((g, gi) => {
        const yb = yG(gi), ser = R.series[g], pts = [];
        for (let i = lo; i <= hi; i++) pts.push([xOf(i), yb, ser[i] * ZS]);
        flat.push(`<path class="ln faint" d="${path(Pj, [[0, yb, 0.1], [XM, yb, 0.1]])}"/>`);
        flat.push(`<g class="rib t-${tone}"><path class="rib-a" d="${path(Pj, [[pts[0][0], yb, 0], ...pts, [pts[pts.length - 1][0], yb, 0]], true)}"/><path class="rib-l" d="${path(Pj, pts)}"/></g>`);
        const bf = R.before[gi], af = R.after[gi];
        sc.over.push(`<path class="ln mean" d="${path(Pj, [[xb0, yb, bf * ZS], [xe, yb, bf * ZS]])}"/><path class="ln mean" d="${path(Pj, [[xe, yb, af * ZS], [xa1, yb, af * ZS]])}"/>`);
        const cx = xOf(cur), cvl = ser[cur];
        sc.over.push(`<circle class="peg w" cx="${n1(Pj.p(cx, yb, cvl * ZS)[0])}" cy="${n1(Pj.p(cx, yb, cvl * ZS)[1])}" r="${n1(3.6 * PS)}"/>`);
        if (both) { tag(Pj.p(-10, yb, 0), T.grp[gi], "title", 0, -8, "end", { fixed: true }); tag(Pj.p(XM + 8, yb, 0), sgn2(af - bf), "pt " + (Math.abs(af - bf) >= 0.5 ? "strong" : "muted"), 0, -4, "start", { fixed: true }); }
        else { tag(Pj.p(-10, yb, 0), T.grp[gi], "title", 0, -14, "end", { fixed: true }); tag(Pj.p(-10, yb, 0), nar ? `${bf.toFixed(2)}→${af.toFixed(2)}` : `${bf.toFixed(2)} → ${af.toFixed(2)}(${sgn2(af - bf)})`, "pt " + (Math.abs(af - bf) >= 0.5 ? "strong" : "muted"), 0, 3, "end", { fixed: true }); }
      });
      flat.push(`<path class="ln evt" d="${path(Pj, [[xe, y0 - 8, 0.2], [xe, y0 + blkH + 2, 0.2]])}"/>`);
      flat.push(`<path class="ln cur" d="${path(Pj, [[xOf(cur), y0 - 8, 0.25], [xOf(cur), y0 + blkH + 2, 0.25]])}"/>`);
      if (bi === 0) { const ys = both ? y0 + MP : yG(0); line(sc, Pj, [[XM + 8, ys, 0], [XM + 8, ys, ZS]], "gauge", "over"); tag(Pj.p(XM + 8, ys, ZS / 2), "1.0", "pt muted", 5, 4, "start", { fixed: true }); }
      const last = bi === blocks.length - 1;
      if (last) {
        const ticks = both ? [-30, -20, -10, 0, 10, 20, 30] : N > 400 ? [0, 200, 400, 600, 800, 1000, 1200] : [0, 20, 40, 60, 80, 100];
        ticks.forEach((tk) => { const i = both ? e + tk : tk; if (i < lo || i > hi) return; flat.push(`<path class="ln faint" d="${path(Pj, [[xOf(i), y0 + blkH - 2, 0.1], [xOf(i), y0 + blkH + 3, 0.1]])}"/>`); tag(Pj.p(xOf(i), y0 + blkH + 3, 0), both ? (tk > 0 ? "+" : "") + tk : String(tk), "muted", 0, 13, "middle", { fixed: true }); });
        tag(Pj.p(XM / 2, y0 + blkH + 3, 0), both ? T.axisRel : T.axisTok, "muted", 0, 30, "middle", { fixed: true });
      }
      tag(Pj.p(xe, y0 - 8, 0), `${both ? T.evtShort : `${T.evt} ${e}`} · ${T.winTag}`, "pt " + tone, 0, -6, "middle", { fixed: true });
    });
    sc.flat.push(...flat);
    return flush(sc);
  };

  // ---- 21: the aggregate. columns = the share of rows whose after-mean exceeds the before-mean, per group, for the O1O2 events (blue, 59 rows) and the He-Hi events (orange, 34 rows); the preregistered predictions Q1 / Q2 at the right
  S.agg = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, D = DATA.olm59, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, CW = nar ? 28 : 46, CD = nar ? 28 : 40, PAIR = 2 * CW + (nar ? 8 : 12), CP = PAIR + (nar ? 30 : 44), HS = nar ? 380 : 210, XQ = 4 * CP + (nar ? 20 : 40), QG = nar ? 84 : 120, YC = 0, XEND = XQ + QG + CW + (nar ? 60 : 118);
    const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), [-86, -60, -6, XEND, CD + 74, HS + 50], cv.W, cv.H, 0.97, 0.92);
    box(sc, Pj, -76, -54, XEND + 66, CD + 118, 5, "p", -5, { key: -1e9 });
    sc.flat.push(`<path class="ln zero" d="${path(Pj, [[-14, YC - 10, HS * 0.5], [4 * CP - 24, YC - 10, HS * 0.5], [4 * CP - 24, YC + CD + 10, HS * 0.5], [-14, YC + CD + 10, HS * 0.5]], true)}"/>`);
    tag(Pj.p(-14, YC + CD + 10, HS * 0.5), "50 %", "pt muted", -4, 4, "end", { fixed: true });
    GN.forEach((g, gi) => {
      const x0 = gi * CP;
      [["o_diam", "b", 0], ["h_diam", "o", CW + (nar ? 8 : 12)]].forEach(([ev, tone, dx]) => {
        const c = D.agg[ev].groups[g].all, fr = c.up / c.n, h = Math.max(0.8, fr * HS);
        box(sc, Pj, x0 + dx, YC, CW, CD, h, tone, 0, {});
        tag(Pj.p(x0 + dx + CW / 2, YC + CD / 2, h), `${c.up}/${c.n}`, "title " + tone, 0, -7, "middle", { fixed: true });
        if (!nar) tag(Pj.p(x0 + dx + CW / 2, YC + CD, 0), sgn3(c.med), "pt muted", 0, 14, "middle", { fixed: true });
      });
      tag(Pj.p(x0 + PAIR / 2, YC + CD, 0), nar ? T.grpS[gi] : T.grp[gi], "title", 0, 34, "middle", { fixed: true });
    });
    if (!nar) tag(Pj.p(-14, YC + CD + 10, 0), T.medRow, "pt muted", -4, 14, "end", { fixed: true });
    [["Q1", "b", XQ], ["Q2", "o", XQ + CW + QG]].forEach(([q, tone, x0]) => {
      const c = D[q], fr = c.up / c.n;
      box(sc, Pj, x0, YC, CW, CD, Math.max(0.8, fr * HS), tone, 0, {});
      box(sc, Pj, x0 - 5, YC - 5, CW + 10, CD + 10, 0.9, "l", c.thr * HS, {});
      tag(Pj.p(x0 + CW / 2, YC + CD, 0), `${c.up}/${c.n}`, "title " + tone, 0, 14, "middle", { fixed: true });
      if (nar) tag(Pj.p(x0 + CW / 2, YC + CD / 2, c.thr * HS), `≥${Math.round(c.thr * 100)} %`, "pt strong", 0, -10, "middle", { fixed: true });
      else tag(Pj.p(x0 + CW + 16, YC + CD / 2, c.thr * HS), `${T.thr} ≥ ${Math.round(c.thr * 100)} %`, "pt strong", 0, 4, "start", { fixed: true });
      tag(Pj.p(x0 + CW / 2, YC + CD, 0), `${q} ${fr >= c.thr ? "✓" : "✗"}`, "title " + tone, 0, 34, "middle", { fixed: true });
    });
    return flush(sc);
  };
  const sgn3 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3);

  // ---- 22: a flat chart. cmt5's 120 rows: the whole-text label and the answer-field label, per path (the cells = the rows; 40 per path)
  S.lab2 = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, D = DATA.olm59.cmt5_two, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, order = ["B-bind", "B-attractor", "B-stuck-L1", "B-flail"];
    const CWd = nar ? 15 : 13.5, CHt = nar ? 20 : 21, X0 = nar ? 16 : 200, LX = nar ? 14 : 22, FX = nar ? 30 : 17;
    let s = "", y = nar ? 60 : 72;
    tag([LX, y - (nar ? 14 : 34)], T.lab2Head, "muted", 0, 0, "start", { fixed: true });
    if (nar) y += 24;
    ["think", "answer", "natural"].forEach((p) => {
      const d = D[p];
      tag([LX, y + (nar ? 6 : 2)], T.paths[p], "title", 0, 0, "start", { fixed: true }); tag([LX, y + (nar ? 6 : 2) + cv.fs * 1.3], T.pathsFixed[p], "pt muted", 0, 0, "start", { fixed: true });
      [["full", T.lab2Full], ["field", T.lab2Field]].forEach(([k, nm], ri) => {
        const counts = d[k], nb = counts["B-bind"] || 0, yy = nar ? y + 46 + FX + ri * (CHt + 44) : y + 8 + FX + ri * (CHt + 10);
        s += cells(X0, yy, CWd, CHt, counts, order);
        if (nb) s += `<rect class="bindbox" x="${n1(X0 - 1)}" y="${n1(yy - 1.5)}" width="${n1(nb * CWd)}" height="${CHt + 3}"/>`;
        if (nar) tag([LX + 6, yy - 8], `${nm}: bind ${nb} / ${d.n}`, "pt " + (k === "field" ? "strong" : "muted"), 0, 0, "start", { fixed: true });
        else { tag([LX, yy + CHt - 5], nm, "pt", 8, 0, "start", { fixed: true }); tag([X0 + 40 * CWd + 10, yy + CHt - 5], `bind ${nb} / ${d.n}`, "pt " + (k === "field" ? "strong" : "muted"), 0, 0, "start", { fixed: true }); }
      });
      y += (nar ? 2 * CHt + 44 + 46 + 40 : 62 + CHt + 16) + FX;
    });
    return `<rect class="chartbg" x="2" y="2" width="${cv.W - 4}" height="${cv.H - 4}" rx="6"/>` + s + sc.tags.join("");
  };

  // =============================================================================================== v2.1 (A): olm62 — does the mid group's rise follow the text's move into formulas? (states `scat` and `flat`)
  const nice = (lo, hi, step) => [Math.round(Math.floor((lo - 0.02) / step) * step * 100) / 100, Math.round(Math.ceil((hi + 0.02) / step) * step * 100) / 100];
  const dia = (cx, cy, r) => `M${n1(cx)} ${n1(cy - r)}L${n1(cx + r)} ${n1(cy)}L${n1(cx)} ${n1(cy + r)}L${n1(cx - r)} ${n1(cy)}Z`;
  const sg3 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3);
  // one scatter of both kinds of events on ONE scale (x = the formula-character share, after − before · y = the mid group, after − before) + the two bars of the behaviour (the share of events whose text moves into formulas)
  S.scat = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, D = DATA.olm62, R = D.read, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, W = cv.W, H = cv.H, fs = cv.fs;
    const [xa, xb] = nice(D.extent.x[0], D.extent.x[1], 0.2), [ya, yb] = nice(D.extent.y[0], D.extent.y[1], 0.2);
    const PX0 = nar ? 92 : 340, PX1 = W - (nar ? 26 : 30), PY0 = nar ? 410 : 92, PY1 = H - (nar ? 140 : 84);
    const X = (v) => PX0 + ((v - xa) / (xb - xa)) * (PX1 - PX0), Y = (v) => PY1 - ((v - ya) / (yb - ya)) * (PY1 - PY0);
    let s = `<rect class="chartbg" x="2" y="2" width="${W - 4}" height="${H - 4}" rx="6"/>`;
    s += `<rect class="axbox" x="${n1(PX0)}" y="${n1(PY0)}" width="${n1(PX1 - PX0)}" height="${n1(PY1 - PY0)}"/>`;
    for (let k = Math.ceil(xa / 0.2 - 1e-9); k * 0.2 <= xb + 1e-9; k++) { const x = X(k * 0.2); s += `<path class="axtick" d="M${n1(x)} ${n1(PY0)}V${n1(PY1)}"/>`; tag([x, PY1 + fs * 1.5], (k * 0.2).toFixed(1).replace("-", "−"), "pt muted", 0, 0, "middle", { fixed: true }); }
    for (let k = Math.ceil(ya / 0.4 - 1e-9); k * 0.4 <= yb + 1e-9; k++) { const y = Y(k * 0.4); s += `<path class="axtick" d="M${n1(PX0)} ${n1(y)}H${n1(PX1)}"/>`; tag([PX0 - 8, y + 4], (k * 0.4).toFixed(1).replace("-", "−"), "pt muted", 0, 0, "end", { fixed: true }); }
    s += `<path class="axzero" d="M${n1(X(0))} ${n1(PY0)}V${n1(PY1)}"/><path class="axzero" d="M${n1(PX0)} ${n1(Y(0))}H${n1(PX1)}"/>`;
    for (const [ev, k] of [["h_diam", "h"], ["o_diam", "o"]]) for (const p of D.events[ev]) s += k === "o" ? `<circle class="pt62 o" cx="${n1(X(p.dmath))}" cy="${n1(Y(p.dmid))}" r="${nar ? 7 : 4.6}"/>` : `<path class="pt62 h" d="${dia(X(p.dmath), Y(p.dmid), nar ? 9 : 5.6)}"/>`;
    for (const [k, cls] of [["S_O", "b"], ["S_H", "o"]]) { const p = D.scene[k], x = X(p.dmath), y = Y(p.dmid); s += `<circle class="pt62 ring" cx="${n1(x)}" cy="${n1(y)}" r="${nar ? 17 : 10.5}"/>`; tag([x, y], k, "title " + cls, nar ? 20 : 15, nar ? -18 : -13, "start", { fixed: true }); }
    lines(T.sx, W - 40, fs).forEach((ln, i) => tag([nar ? W / 2 : (PX0 + PX1) / 2, PY1 + fs * 3.1 + i * fs * 1.3], ln, "pt", 0, 0, "middle", { fixed: true }));
    tag([PX0, PY0 - fs * 0.9], T.sy, "pt strong", 0, 0, "start", { fixed: true });
    const rho = (v) => v.toFixed(3);
    tag([PX0 + 12, PY0 + fs * 1.7], `${T.rho} ${rho(R.o_diam.spearman_mid_math)}  (O1O2 · n ${R.o_diam.n})`, "title b", 0, 0, "start", { fixed: true });
    tag([PX0 + 12, PY0 + fs * 3.2], `${T.rho} ${rho(R.h_diam.spearman_mid_math)}  (He・Hi · n ${R.h_diam.n})`, "title o", 0, 0, "start", { fixed: true });
    tag([PX0 + 12, PY0 + fs * 4.7], `${T.rhoAll(R.n_tokens)} ${rho(R.Q3_pooled_token_spearman_mid_math)}`, "pt muted", 0, 0, "start", { fixed: true });
    // the bars: the share of events after which the text moves into formulas (Δmath > 0)
    const BARS = [["o", R.o_diam, "O1O2", "b"], ["h", R.h_diam, "He・Hi", "o"]];
    if (!nar) {
      const base = PY1, top = PY0 + 40, hb = base - top, BW = 70, XS = [60, 168];
      lines(T.barHead, 270, fs).forEach((ln, i) => tag([24, 36 + i * fs * 1.35], ln, i ? "pt muted" : "title", 0, 0, "start", { fixed: true }));
      s += `<path class="axzero" d="M30 ${n1(base - hb / 2)}H270"/>`; tag([272, base - hb / 2 + 4], "50 %", "pt muted", 0, 0, "start", { fixed: true });
      BARS.forEach(([k, r, nm, cls], i) => { const fr = r.math_up / r.n, h = fr * hb, x = XS[i]; s += `<rect class="bar62 ${k}" x="${x}" y="${n1(base - h)}" width="${BW}" height="${n1(h)}"/>`; tag([x + BW / 2, base - h - 10], `${r.math_up} / ${r.n}`, "title " + cls, 0, 0, "middle", { fixed: true }); tag([x + BW / 2, base - h + 22], `${Math.round(fr * 100)} %`, "pt strong", 0, 0, "middle", { fixed: true }); tag([x + BW / 2, base + fs * 1.5], nm, "pt strong", 0, 0, "middle", { fixed: true }); });
    } else {
      lines(T.barHead, W - 48, fs).forEach((ln, i) => tag([24, 40 + i * fs * 1.3], ln, i ? "pt muted" : "title", 0, 0, "start", { fixed: true }));
      BARS.forEach(([k, r, nm, cls], i) => { const fr = r.math_up / r.n, y = 130 + i * 112, bw = (W - 48) * 0.7 * fr; tag([24, y], nm, "pt strong", 0, 0, "start", { fixed: true }); s += `<rect class="bar62 ${k}" x="24" y="${y + 12}" width="${n1(bw)}" height="40"/>`; tag([24 + bw + 12, y + 42], `${r.math_up} / ${r.n}  (${Math.round(fr * 100)} %)`, "title " + cls, 0, 0, "start", { fixed: true }); });
      s += `<path class="axzero" d="M${n1(24 + (W - 48) * 0.35)} 128V${130 + 112 + 62}"/>`; tag([24 + (W - 48) * 0.35 + 6, 126], "50 %", "pt muted", 0, 0, "start", { fixed: true });
    }
    return s + sc.tags.join("");
  };
  // the 11 O1O2 events whose text does NOT move into formulas (Δmath ≤ 0): their mid-group change, the margin of the preregistered threshold, and the size of the rise
  S.flat = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, D = DATA.olm62, R = D.read.o_diam, F = D.flat_o, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, W = cv.W, H = cv.H, fs = cv.fs;
    const n = F.length, up = F.filter((z) => z.dmid > 0).length, thr = D.thr_q2, need = Math.ceil(thr * n - 1e-9), pctOf = (k) => Math.round((k / n) * 100);
    let s = `<rect class="chartbg" x="2" y="2" width="${W - 4}" height="${H - 4}" rx="6"/>`;
    const LX = nar ? 24 : 30, AX0 = nar ? 56 : 70, AX1 = W - (nar ? 40 : 44), va = -0.2, vb = 0.3, X = (v) => AX0 + ((v - va) / (vb - va)) * (AX1 - AX0);
    let y = nar ? 40 : 40;
    lines(T.flatHead, W - 2 * LX, fs).forEach((ln, i) => tag([LX, y + i * fs * 1.35], ln, i ? "pt muted" : "title", 0, 0, "start", { fixed: true })); y += lines(T.flatHead, W - 2 * LX, fs).length * fs * 1.35 + (nar ? 34 : 26);
    // (1) the strip: one dot per event (sorted; stacked where they would touch)
    const base = y + (nar ? 150 : 128), gap = nar ? 21 : 12.5, lvl = [];
    s += `<path class="axbase" d="M${n1(AX0)} ${n1(base)}H${n1(AX1)}"/>`;
    for (let v = -0.2; v <= 0.3 + 1e-9; v += 0.1) { const x = X(v), t = (Math.round(v * 10) / 10).toFixed(1).replace("-", "−"); s += `<path class="axtick" d="M${n1(x)} ${n1(base - (nar ? 150 : 130))}V${n1(base)}"/>`; tag([x, base + fs * 1.5], t, "pt muted", 0, 0, "middle", { fixed: true }); }
    s += `<path class="axzero" d="M${n1(X(0))} ${n1(base - (nar ? 150 : 130))}V${n1(base)}"/>`;
    const r = nar ? 8 : 5.6;
    F.forEach((z) => { const x = X(z.dmid); let l = 0; while (lvl[l] !== undefined && x - lvl[l] < gap) l++; lvl[l] = x; const yy = base - r - 3 - l * (r * 2 + 2); s += `<circle class="pt62 flat ${z.dmid > 0 ? "up" : "dn"}" cx="${n1(x)}" cy="${n1(yy)}" r="${r}"/>`; });
    const mF = D.read.o_diam.mid_median_when_math_flat, mA = D.all_o_mid_median;
    for (const [v, txt, cls, dy] of [[mF, `${T.medFlat} ${sg3(mF)}`, "strong", 0], [mA, `${T.medAll} ${sg3(mA)}`, "muted", 1]]) { s += `<path class="ln ${dy ? "cur" : "mean"}" d="M${n1(X(v))} ${n1(base - (nar ? 150 : 130))}V${n1(base)}"/>`; tag([X(v) + (dy ? 6 : -6), base - (nar ? 150 : 130) + 10 + dy * fs * 1.5 + (nar ? 8 : 0)], txt, "pt " + cls, 0, 0, dy ? "start" : "end", { fixed: true }); }
    tag([AX0, base + fs * 3.0], T.flatAxis, "pt", 0, 0, "start", { fixed: true });
    tag([X(0) + 8, base + fs * 4.6], `↑ ${up} / ${n}   ↓ ${n - up} / ${n}`, "title b", 0, 0, "start", { fixed: true });
    y = base + fs * 6.4 + (nar ? 20 : 14);
    // (2) the margin of the threshold: 11 cells = 11 events; the line = 60 %
    const putL = (text, cls) => { for (const ln of lines(text, W - 2 * LX, fs)) { tag([LX, y], ln, cls, 0, 0, "start", { fixed: true }); y += fs * 1.35; } };
    putL(T.marginHead, "title"); y += fs * 1.2 + (nar ? 16 : 10);
    const cw = nar ? 40 : 30, ch = nar ? 34 : 26, cx0 = LX;
    F.slice().sort((a, b) => b.dmid - a.dmid).forEach((z, i) => { s += `<rect class="cell ${z.dmid > 0 ? "c-b" : "c-x"}" x="${n1(cx0 + i * cw)}" y="${n1(y)}" width="${cw - 3}" height="${ch}"/>`; });
    s += `<path class="ln evt" d="M${n1(cx0 + (need - 0.5) * cw + 1)} ${n1(y - 10)}V${n1(y + ch + 10)}"/>`; tag([cx0 + (need - 0.5) * cw + 8, y - 14], T.thrTag(thr, need, n), "pt strong", 0, 0, "start", { fixed: true });
    y += ch + fs * 1.9; putL(T.marginNote(up, n, need, pctOf(up), pctOf(need - 1)), "pt"); y += nar ? 30 : 22;
    // (3) the other groups in the same 11 events (cells = events; filled = the group rises)
    tag([LX, y], T.byGroupHead, "title", 0, 0, "start", { fixed: true }); y += fs * 0.6 + (nar ? 20 : 12);
    const GNm = T.grp, GKEY = ["close", "mid", "ans", "think"], cw2 = nar ? 26 : 19, lab = nar ? 190 : 150;
    GKEY.forEach((g, gi) => { const k = Number(R.by_group_math_flat[g].split(" / ")[0]), yy = y + gi * (nar ? 40 : 28); tag([LX, yy + (nar ? 24 : 17)], GNm[gi], "pt" + (g === "mid" ? " strong" : ""), 0, 0, "start", { fixed: true }); for (let i = 0; i < n; i++) s += `<rect class="cell ${i < k ? (g === "mid" ? "c-b" : "c-g") : "c-x"}" x="${n1(LX + lab + i * cw2)}" y="${n1(yy + 2)}" width="${cw2 - 2.5}" height="${nar ? 28 : 20}"/>`; tag([LX + lab + n * cw2 + 8, yy + (nar ? 24 : 17)], `${k} / ${n}`, "pt" + (g === "mid" ? " strong" : " muted"), 0, 0, "start", { fixed: true }); });
    return s + sc.tags.join("");
  };

  // =============================================================================================== v2.1 (B): the map — the 9 clusters of the card tree v2.2.1 (grey boxes) + the two boxes outside it, the cards this figure uses outlined
  const usedStates = (id) => DATA.config.card_marks.flatMap((a, i) => (a.includes(id) ? [i] : []));
  const rangeText = (xs) => { if (!xs.length) return ""; const out = []; let a = xs[0], b = a; for (const x of xs.slice(1)) { if (x === b + 1) b = x; else { out.push(a === b ? `${a}` : `${a}–${b}`); a = b = x; } } out.push(a === b ? `${a}` : `${a}–${b}`); return out.join(" · "); };
  const SNAKE = [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [0, 1], [0, 2], [1, 2], [2, 2]];           // the tree's own reading order: 1 2 3 / 6 5 4 / 7 8 9 drawn as a snake (the number sits in the box)
  S.tree = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, TR = DATA.tree, sc = newScene(), nar = cv.narrow, W = cv.W, H = cv.H, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), sel = S_.card || null;      // the map is laid out for a 12-unit font in every frame (the video frame scales the whole canvas)
    const cname = (c) => (S_.lang === "en" ? T.cl[c.id] : c.name), csub = (c) => (S_.lang === "en" ? T.clSub[c.id] : c.sub), C = Object.fromEntries(TR.clusters.map((c) => [c.id, c]));
    const cardsOf = (zone) => Object.keys(TR.cards).filter((id) => TR.cards[id].zone === zone).sort((a, b) => (TR.cards[a].date < TR.cards[b].date ? -1 : 1) || (a < b ? -1 : 1));
    const disp = (id) => T.card[id][0], lab = (id) => (S_.lang === "ja" && TR.cards[id].label) || T.card[id][1];
    let s = `<rect class="chartbg" x="2" y="2" width="${W - 4}" height="${H - 4}" rx="6"/>`;
    const L = fs * 1.3;
    // a card chip: id · label / date (+ the tree's own outcome word) / the states of this figure that draw on it
    const chipLines = (id) => { const c = TR.cards[id], inTree = c.zone[0] === "C"; return [[disp(id), "strong"], [`${lab(id)} · ${c.date}`, "muted"], ...(inTree ? [[(S_.lang === "en" && T.outcome[c.outcome]) || c.outcome, "muted"]] : []), [`${T.usedBy} ${rangeText(usedStates(id))}`, "strong"]]; };
    const chip = (x, y, w, id) => { const ls = chipLines(id), h = ls.length * L + 12, on = sel === id; s += `<rect class="tchip${on ? " sel" : ""}" x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(h)}" rx="5"/>`; ls.forEach(([t, cls], i) => tag([x + 8, y + 6 + (i + 0.85) * L], t, "pt " + cls + (i === 0 ? " strong" : ""), 0, 0, "start", { fixed: true })); return h; };
    const head = (x, y, w, t1, t2, t3) => { tag([x + 10, y + fs * 1.7], t1, "title", 0, 0, "start", { fixed: true }); let k = 0; for (const ln of lines(t2, w - 20, fs)) { tag([x + 10, y + fs * 3.1 + k * L], ln, "pt muted", 0, 0, "start", { fixed: true }); k++; } if (t3) tag([x + 10, y + fs * 3.1 + Math.max(k, 1) * L + 2], t3, "pt muted", 0, 0, "start", { fixed: true }); return fs * 3.1 + Math.max(k, 1) * L + (t3 ? L : 0) + 6; };
    const note = (x, y, w, t, cls = "muted") => { let k = 0; for (const ln of lines(t, w, fs)) { tag([x, y + k * L], ln, "pt " + cls, 0, 0, "start", { fixed: true }); k++; } return k * L; };
    if (!nar) {
      tag([24, 34], T.treeHead(TR), "title", 0, 0, "start", { fixed: true }); tag([24, 34 + L + 2], T.treeSub, "pt muted", 0, 0, "start", { fixed: true });
      const Y0 = 84, BW = 268, GX = 316, CWd = 262, CG = 14, RH = [236, 106, 106], RG = 14, rowY = (r) => Y0 + RH.slice(0, r).reduce((a, b) => a + b + RG, 0), GH = RH.reduce((a, b) => a + b, 0) + 2 * RG;
      // the box before the tree
      s += `<rect class="tbox out" x="24" y="${Y0}" width="${BW}" height="${GH}" rx="8"/>`; let yy = Y0 + head(24, Y0, BW, T.zoneBefore, T.zoneBeforeSub(TR), "");
      for (const id of cardsOf("before")) yy += chip(34, yy, BW - 20, id) + 7;
      // the grid: the nine clusters (neutral grey); the cards that this figure uses sit inside as outlined chips
      TR.clusters.forEach((c, i) => {
        const [col, row] = SNAKE[i], x = GX + col * (CWd + CG), y = rowY(row), h = RH[row], mine = cardsOf(c.id), sub = csub(c);
        s += `<rect class="tbox${mine.length ? " mine" : ""}" x="${x}" y="${y}" width="${CWd}" height="${h}" rx="8"/>`;
        let yy = y + head(x, y, CWd, `${"①②③④⑤⑥⑦⑧⑨"[i]} ${cname(c)}`, sub, `${T.cardsN(c.n)} · ${c.span[0] === c.span[1] ? c.span[0] : c.span[0] + "〜" + c.span[1]}`);
        if (!mine.length) tag([x + 10, y + h - 12], T.notUsed, "pt muted dimtag", 0, 0, "start", { fixed: true });
        for (const id of mine) yy += chip(x + 10, yy, CWd - 20, id) + 6;
      });
      // the box after the tree + the proposed place (L3)
      const AX = GX + 3 * CWd + 2 * CG + 20, AW = W - 24 - AX;
      s += `<rect class="tbox out" x="${AX}" y="${Y0}" width="${AW}" height="${GH * 0.62}" rx="8"/>`; yy = Y0 + head(AX, Y0, AW, T.zoneAfter, T.zoneAfterSub(TR), "");
      for (const id of cardsOf("after")) yy += chip(AX + 10, yy, AW - 20, id) + 7;
      const nh = note(AX + 6, Y0 + GH * 0.62 + 24, AW - 12, T.proposal);
      s += `<path class="ln tarrow" d="M${AX} ${Y0 + 36}H${GX + 3 * CWd + 2 * CG + 3}"/><path class="ln tarrow" d="M${GX - 3} ${Y0 + 36}H${24 + BW}" marker-end=""/>`;
      tag([AX - 2, Y0 + 30], "L3", "pt strong", 0, 0, "end", { fixed: true });
    } else {
      let y = 34; for (const ln of lines(T.treeHead(TR), W - 48, fs)) { tag([24, y], ln, "title", 0, 0, "start", { fixed: true }); y += L; } y += 8;
      const block = (title, sub, ids, cls = "") => { const h0 = y; let yy = y + head(0, y, W - 20, title, sub, ""), hh = 0; const tmp = []; for (const id of ids) { const ls = chipLines(id), h = ls.length * L + 12, on = sel === id; tmp.push(`<rect class="tchip${on ? " sel" : ""}" x="24" y="${n1(yy)}" width="${W - 48}" height="${n1(h)}" rx="6"/>`); ls.forEach(([t, c2], i) => tag([34, yy + 6 + (i + 0.85) * L], t, "pt " + c2 + (i === 0 ? " strong" : ""), 0, 0, "start", { fixed: true })); yy += h + 8; } s += `<rect class="tbox ${cls}" x="10" y="${h0}" width="${W - 20}" height="${yy - h0 + 2}" rx="10"/>` + tmp.join(""); y = yy + 18; };
      block(T.zoneBefore, T.zoneBeforeSub(TR), cardsOf("before"), "out");
      for (const c of TR.clusters) { const mine = cardsOf(c.id); if (mine.length) block(`${c.id} ${cname(c)}`, `${csub(c)} · ${T.cardsN(c.n)} · ${c.span[0] === c.span[1] ? c.span[0] : c.span[0] + "〜" + c.span[1]}`, mine, "mine"); }
      const rest = TR.clusters.filter((c) => !cardsOf(c.id).length);
      s += `<rect class="tbox" x="10" y="${y}" width="${W - 20}" height="${(lines(T.restTxt(rest), W - 52, fs).length) * L + 22}" rx="10"/>`; y += 24; y += note(24, y, W - 48, T.restTxt(rest)) + 24;
      block(T.zoneAfter, T.zoneAfterSub(TR), cardsOf("after"), "out"); y += note(24, y, W - 48, T.proposal, "muted");
    }
    return s + sc.tags.join("");
  };

  S.__h = { begin, n1, esc, clamp, camera, newScene, flush, box, line, ring, tagger, estW, lines, pin, cells, CELL, path, sgn3, nice, dia };           // v3: the helpers that scenes_after.js (the part added after the 10-28 figure) draws with
  return S;
})();
