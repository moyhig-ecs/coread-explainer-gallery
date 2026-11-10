// figure.js — what each state draws (moy-5: the roads to the apex = the mean proportional, on the same floor). Every number comes from DATA (pack.json via data.mjs); nothing is typed here.
// Contract with the engine (state_machine.js): FIGURE.states · FIGURE.ctx(S) · FIGURE.draw(S, A, el, root) · FIGURE.keysOf(S) · FIGURE.tRange(S) · FIGURE.focus(S)
// The unit of every plane chart: ONE DOT = ONE ANSWER (one row of the frozen jsonl, in rep order). Filled blue = a cut in the answer field · blue ring = a cut only in the reason field · small grey = the floor only · grey ring = neither.
// Isometric (orbit) states: the drafting board of the construction (A0, D0), the three stations (B0), the effort ladder (E0). The answer boards are drawn as solid slabs in a fixed oblique view so that their text stays level.
const FIGURE = (() => {
  const VW = 1180, VH = 700, K0 = 1.7, PI = Math.PI;
  const n1 = (v) => Math.round(v * 10) / 10;
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const narrow = () => matchMedia("(max-width:560px)").matches;
  const C = (id) => { const c = DATA.cells[id]; if (!c) throw new Error("no cell " + id); return c; };
  const SC = (id) => DATA.scenes[id];
  let LANG = "ja", VIDEO = false;
  const PW = () => (narrow() ? 600 : VIDEO ? 1600 : VW);   // the width of a plane layout: phone 600 · desk 1180 · video 1600 (one line per strip, so the 1080 frame holds it)
  const L = (ja, en) => (LANG === "en" ? en : ja);
  // ---- type sizes (viewBox units) per frame: measured in px by the checks (video ≥ 10 · desk ≥ 10 · phone ≥ 9.5)
  let FS = 12.5;
  const fsOf = (root, mode) => (root.dataset.video === "1" ? 14 : narrow() ? (mode === "iso" ? 30 : 21.5) : 13.5);
  const T = (x, y, s, o = {}) => `<text class="pl ${o.c || ""}" x="${n1(x)}" y="${n1(y)}" font-size="${n1(o.fs || FS)}"${o.a ? ` text-anchor="${o.a}"` : ""}${o.w ? ` font-weight="${o.w}"` : ""}>${esc(s)}</text>`;
  // width estimate of a string in units (CJK = 1 em, latin ≈ 0.56 em): used to wrap and to keep text inside the viewBox
  const tw = (s, fs = FS, mono = false) => [...String(s)].reduce((a, ch) => a + (/[　-鿿＀-￯]/.test(ch) ? 1 : mono ? 0.62 : /[A-Z0-9_]/.test(ch) ? 0.64 : /[mwMW]/.test(ch) ? 0.8 : 0.56), 0) * fs;
  // v2.3: the estimated box of a text drawn by T (the same width estimate) = [x0, y0, x1, y1] in viewBox units
  const boxOf = (x, y, s, fs = FS, a) => { const w = tw(s, fs), x0 = a === "end" ? x - w : a === "middle" ? x - w / 2 : x; return [x0, y - fs * 0.85, x0 + w, y + fs * 0.25]; };
  function wrap(s, width, fs = FS, mono = false) {
    const out = []; let line = "";
    const toks = String(s).match(/[　-鿿＀-￯]|[^\s　-鿿＀-￯]+\s*|\s+/g) || [];
    for (const t of toks) { if (tw(line + t, fs, mono) > width && line.trim()) { out.push(line.trim()); line = t.trimStart(); } else line += t; }
    if (line.trim()) out.push(line.trim());
    return out;
  }
  const lines = (x, y, arr, o = {}) => arr.map((s, i) => T(x, y + i * (o.lh || (o.fs || FS) * 1.38), s, o)).join("");

  // ---- the camera (the kit's isometric formula, free azimuth / elevation / zoom; c = the world point kept at the centre)
  function proj(az, el, zoom, px, c, vw = VW, vh = VH) {
    const a = (az * PI) / 180, e = (el * PI) / 180, sA = Math.sin(a), cA = Math.cos(a), sE = Math.sin(e), cE = Math.cos(e), k = K0 * zoom;
    const ox = vw / 2 + px - (c[0] * sA - c[1] * cA) * k, oy = vh / 2 + 14 - ((c[0] * cA + c[1] * sA) * sE - c[2] * cE) * k;
    return { p: (x, y, z) => [ox + (x * sA - y * cA) * k, oy + ((x * cA + y * sA) * sE - z * cE) * k], depth: (x, y, z) => x * cA + y * sA + z * 0.01, cA, sA, k };
  }
  const poly = (Pj, pts) => "M" + pts.map((v) => Pj.p(...v).map(n1).join(" ")).join("L") + "Z";
  const seg = (Pj, a, b) => "M" + Pj.p(...a).map(n1).join(" ") + "L" + Pj.p(...b).map(n1).join(" ");
  // a solid box with the kit's tones: top (iso-top), the two faces turned to the viewer (iso-shade 1 / 2), and the outline (iso-line). `tint` adds a coloured film on the top (apex = blue, Descartes = orange).
  function box(Pj, x, y, z, w, d, h, o = {}) {
    const X0 = x, X1 = x + w, Y0 = y, Y1 = y + d, Z0 = z, Z1 = z + h, s = [];
    const fx = Pj.cA >= 0 ? X1 : X0, fy = Pj.sA >= 0 ? Y1 : Y0;
    s.push(`<path class="iso-shade" data-shade="1" d="${poly(Pj, [[fx, Y0, Z0], [fx, Y1, Z0], [fx, Y1, Z1], [fx, Y0, Z1]])}"/>`);
    s.push(`<path class="iso-shade" data-shade="2" d="${poly(Pj, [[X0, fy, Z0], [X1, fy, Z0], [X1, fy, Z1], [X0, fy, Z1]])}"/>`);
    s.push(`<path class="iso-top" d="${poly(Pj, [[X0, Y0, Z1], [X1, Y0, Z1], [X1, Y1, Z1], [X0, Y1, Z1]])}"/>`);
    if (o.tint) s.push(`<path class="tint ${o.tint}" d="${poly(Pj, [[X0, Y0, Z1], [X1, Y0, Z1], [X1, Y1, Z1], [X0, Y1, Z1]])}"/>`);
    if (o.tintSide) s.push(`<path class="tint ${o.tintSide} side" d="${poly(Pj, [[X0, fy, Z0], [X1, fy, Z0], [X1, fy, Z1], [X0, fy, Z1]])}"/><path class="tint ${o.tintSide} side" d="${poly(Pj, [[fx, Y0, Z0], [fx, Y1, Z0], [fx, Y1, Z1], [fx, Y0, Z1]])}"/>`);
    const edge = o.edge || "mid";
    s.push(`<path class="iso-line" data-tone="${edge}" d="${poly(Pj, [[X0, Y0, Z1], [X1, Y0, Z1], [X1, Y1, Z1], [X0, Y1, Z1]])}${seg(Pj, [fx, Y0, Z0], [fx, Y0, Z1])}${seg(Pj, [fx, Y1, Z0], [fx, Y1, Z1])}${seg(Pj, [X0, fy, Z0], [X0, fy, Z1])}${seg(Pj, [fx, Y0, Z0], [fx, Y1, Z0])}${seg(Pj, [X0, fy, Z0], [X1, fy, Z0])}"/>`);
    return { d: Pj.depth(x + w / 2, y + d / 2, z), svg: s.join("") };
  }
  const screws = (Pj, x, y, z, w, d, inset = 6) => [[x + inset, y + inset], [x + w - inset, y + inset], [x + w - inset, y + d - inset], [x + inset, y + d - inset]].map(([a, b]) => { const q = Pj.p(a, b, z); return `<circle class="screw" cx="${n1(q[0])}" cy="${n1(q[1])}" r="1.3"/>`; }).join("");

  // ---- the construction (A0 / D0): the frozen coordinates; D and H and a moved P_x are computed here FOR DRAWING ONLY (not data). data.mjs asserts that this recomputes the frozen K, P_y, J within 1e-3.
  const Pt = DATA.construction.coords;
  const sub = (a, b) => [a[0] - b[0], a[1] - b[1]], add = (a, b) => [a[0] + b[0], a[1] + b[1]], mul = (a, k) => [a[0] * k, a[1] * k], perp = (v) => [-v[1], v[0]];
  const meet = (p, u, q, v) => { const d = u[0] * v[1] - u[1] * v[0], t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / d; return add(p, mul(u, t)); };
  function construct(Px) {
    const A = Pt.A, G = Pt.G, E = Pt.E, F = Pt.F, fd = perp(sub(G, A)), gd = perp(sub(E, A)), V = meet(F, fd, E, gd), D = meet(G, sub(E, G), F, fd), ed = perp(fd);
    const K = meet(F, sub(Px, F), D, ed), Py = meet(Px, perp(sub(Px, F)), K, fd), H = meet(Py, ed, F, fd), J = meet(H, sub(E, G), E, gd);
    return { A, B: Pt.B, C: Pt.C, G, E, F, V, D, K, P_y: Py, H, J, P_x: Px, fd, gd, ed };
  }
  const h1dir = (() => { const fd = perp(sub(Pt.G, Pt.A)), ed = perp(fd), n = Math.hypot(...ed); return [ed[0] / n, ed[1] / n]; })();
  const PxAt = (t) => add(Pt.P_x, mul(h1dir, t * 0.55));         // the slider moves P_x along h1 (t = 0 = the frozen P_x). Drawing only: no number of a moved position is shown.
  // ---- v2.2 (BRIEF v2.2 §2-1): the overlay = the board read as the plane through the axis of a cone. DRAWING ONLY: computed from the frozen A, G, E, F, C and r (not data; it says nothing about a model).
  //      cone: apex C, axis C -> A, half-angle asin(r / CA) (= 30° on these coordinates); drawn up to the plane through the frozen J perpendicular to the axis, so that CJ is a whole generatrix; the upper half (above the board).
  //      Dandelin sphere: centre A, radius r (the board's circle is its great circle); the contact circle through G and E; F = where the sphere touches the cut (F lies on the board).
  //      the cut: the plane through j perpendicular to the board; its parabola (vertex V, focus F) runs up to P_y lifted above H; the dotted quarter arc folds that point down onto the board's P_y (rotation about j).
  const dot2 = (a, b) => a[0] * b[0] + a[1] * b[1], unit2 = (v) => { const n = Math.hypot(...v); return [v[0] / n, v[1] / n]; };
  const CONE = (() => {
    const A = Pt.A, Cc = Pt.C, r = DATA.construction.radius, CA = Math.hypot(...sub(A, Cc)), ax = unit2(sub(A, Cc)), al = Math.asin(r / CA);
    const J0 = construct(Pt.P_x).J, L0 = Math.hypot(...sub(J0, Cc)), M0 = add(Cc, mul(ax, L0 * Math.cos(al))), rho0 = L0 * Math.sin(al), nn = unit2(sub(J0, M0));   // nn points from the base centre to the frozen J
    return { A, C: Cc, r, CA, ax, al, L0, M0, rho0, nn };
  })();
  function coneCheck(t) {   // for the page check (make_check.py V22): §1 of BRIEF v2.2 on the coordinates, and P_y lifted above H lies on the cone and on the cut's parabola (residuals; drawing only)
    const g = construct(PxAt(t)), K = CONE, off = (p, q, u) => Math.abs((p[0] - q[0]) * u[1] - (p[1] - q[1]) * u[0]) / Math.hypot(...u);
    const HPy = Math.hypot(...sub(g.P_y, g.H)), w = sub(g.H, K.C), along = dot2(w, K.ax), radial = Math.hypot(Math.hypot(...sub(w, mul(K.ax, along))), HPy);
    const VF = Math.hypot(...sub(g.F, g.V)), VH = Math.hypot(...sub(g.H, g.V)), M = add(K.C, mul(K.ax, along));
    return { C_on_f: off(K.C, g.G, g.fd), C_on_g: off(K.C, g.E, g.gd), F_antipode_of_G: Math.hypot(g.F[0] + g.G[0] - 2 * K.A[0], g.F[1] + g.G[1] - 2 * K.A[1]),
             GE_perp_axis: Math.abs(dot2(unit2(sub(g.E, g.G)), K.ax)), j_tangent_at_F: Math.abs(dot2(unit2(sub(g.F, K.A)), unit2(g.fd))), half_angle_deg: (K.al * 180) / PI,
             Py_on_cone: Math.abs(Math.atan2(radial, along) - K.al), Py_on_circle_through_J: Math.abs(Math.hypot(Math.hypot(...sub(g.H, M)), HPy) - Math.hypot(...sub(g.J, M))), symptoma: Math.abs(HPy * HPy - 4 * VF * VH) / (HPy * HPy) };
  }
  // ---- v2.3 (BRIEF v2.3 §2-1, 先生 11-09): the cutting plane = the plane through the line FVD (line j) perpendicular to the board. DRAWING ONLY (computed from the frozen coordinates; not data).
  //      One function gives what is drawn AND what is checked (planeCheck below): the rectangle standing on j (from a little before the parabola's end H to a little past D, so that the directrix is in it;
  //      up to a little above the parabola's highest point), the directrix (the vertical line through D), and the parabola's samples (vertex V, focus F; [point on the board, height] in coordinate units).
  const cross2 = (a, b) => a[0] * b[1] - a[1] * b[0];
  // v2.3.1 (先生 11-09 19:3x「切断平面が育つのがかえって分かりにくいかもしれない」→「それで進めます」): the plane and the parabola no longer follow the slider.
  //      Both are fixed at the frozen P_x (t = 0) = the cut of the drawn cone (its base rim passes through the frozen J, so P_y lifted at t = 0 sits on the rim).
  //      Only P_y lifted (and its fold) moves along the same parabola; where it runs past the plane's edge (t < 0) the parabola goes on as a thin dashed line (ext).
  const G0 = construct(Pt.P_x);
  function cutPlane(g) {
    const g0 = G0, u = unit2(mul(g0.fd, -1)), sOf = (q) => dot2(sub(q, g0.F), u), at = (s) => add(g0.F, mul(u, s));   // u = along j from F towards V and D (BRIEF v2.3 §1: (0.992546, 0.121874))
    const ju = unit2(sub(g0.F, g0.V)), p = Math.hypot(...sub(g0.F, g0.V)), VH0 = dot2(sub(g0.H, g0.V), ju), HPy0 = Math.hypot(...sub(g0.P_y, g0.H)), par = [];
    for (let i = 0; i < 40; i++) { const aa = VH0 * (i / 40) ** 2; par.push([add(g0.V, mul(ju, aa)), Math.sqrt(Math.max(0, 4 * p * aa))]); }
    par.push([g0.H, HPy0]);   // the fixed top = P_y lifted at the frozen P_x
    const VH = dot2(sub(g.H, g.V), ju), HPy = Math.hypot(...sub(g.P_y, g.H)), lift = [g.H, HPy], ext = [];   // the moving point = P_y lifted above H (v2.2)
    if (VH > VH0 + 1e-9) for (let i = 0; i <= 24; i++) { const aa = VH0 + (VH - VH0) * (i / 24); ext.push([add(g0.V, mul(ju, aa)), Math.sqrt(Math.max(0, 4 * p * aa))]); }
    const ss = [g0.H, g0.V, g0.F, g0.D].map(sOf), s0 = Math.min(...ss) - 0.6, s1 = Math.max(...ss) + 0.6, top = Math.max(HPy0, 1) * 1.06 + 0.4;
    return { u, ju, p, VH, HPy, VH0, HPy0, H0: g0.H, par, ext, lift, s0, s1, top, rect: [[at(s0), 0], [at(s1), 0], [at(s1), top], [at(s0), top]], dir: [[g0.D, 0], [g0.D, top]] };
  }
  function planeCheck(t, ctl) {   // for the page check (make_check.py V23): BRIEF v2.3 §1 on the frozen coordinates + the plane and the parabola AS DRAWN (cutPlane). ctl = a planted fault (positive control)
    const g = construct(PxAt(t)), q = cutPlane(g), K = CONE, V0 = Pt.V, off = (p) => Math.abs(cross2(sub(p, g.F), q.u));
    if (ctl === "shift") q.par[20] = [add(q.par[20][0], mul(perp(q.u), 1e-4)), q.par[20][1]];               // one sample moved 1e-4 off the plane
    if (ctl === "frozenV") q.par.forEach((s, i) => { if (i < 40) s[0] = add(s[0], sub(V0, g.V)); });         // the parabola drawn from the question's rounded V (off j by 4.1e-5)
    if (ctl === "tilt") q.rect[3] = [add(q.rect[3][0], mul(perp(q.u), 1e-3 * q.top)), q.rect[3][1]];         // the plane leaned by 1e-3 rad
    if (ctl === "grow") q.rect = q.rect.map(([p, h]) => [p, h * 1.001]);                                         // v2.3.1: the plane grown by 0.1 % (the old v2.3 grew with P_x)
    const e1 = [...sub(q.rect[1][0], q.rect[0][0]), q.rect[1][1] - q.rect[0][1]], e2 = [...sub(q.rect[3][0], q.rect[0][0]), q.rect[3][1] - q.rect[0][1]];
    const n = [e1[1] * e2[2] - e1[2] * e2[1], e1[2] * e2[0] - e1[0] * e2[2], e1[0] * e2[1] - e1[1] * e2[0]];
    const onCone = ([p, h]) => { const w = sub(p, K.C), along = dot2(w, K.ax); return Math.abs(Math.atan2(Math.hypot(Math.hypot(...sub(w, mul(K.ax, along))), h), along) - K.al); };
    const tV = dot2(sub(V0, g.F), q.u), tD = dot2(sub(g.D, g.F), q.u);
    const all = [...q.par, ...q.ext, q.lift], q0 = cutPlane(G0);   // v2.3.1: the moving point and the dashed run past the edge are held to the same plane and cone
    const plane_fixed = Math.max(...q.rect.map(([p, h], i) => Math.hypot(p[0] - q0.rect[i][0][0], p[1] - q0.rect[i][0][1], h - q0.rect[i][1])), ...q.par.map(([p, h], i) => Math.hypot(p[0] - q0.par[i][0][0], p[1] - q0.par[i][0][1], h - q0.par[i][1])));
    return { u: q.u, V_off_j: off(V0), D_off_j: off(g.D), tV_over_tD: tV / tD, FV: Math.hypot(...sub(V0, g.F)), FD: Math.hypot(...sub(g.D, g.F)), A_to_j: off(K.A), AF_dot_j: Math.abs(dot2(unit2(sub(g.F, K.A)), q.u)),
             par_n: q.par.length, par_off_plane: Math.max(...all.map(([p]) => off(p))), par_on_cone: Math.max(...all.map(onCone)), plane_dot_board: Math.abs(n[2]) / Math.hypot(...n),
             corners_off: Math.max(...q.rect.map(([p]) => off(p))), directrix_off: off(q.dir[0][0]), par_inside: q.par.every(([p, h]) => { const s = dot2(sub(p, g.F), q.u); return s >= q.s0 && s <= q.s1 && h >= 0 && h <= q.top; }),
             plane_fixed, lift_on_par: Math.abs(q.HPy * q.HPy - 4 * q.p * q.VH) / (q.HPy * q.HPy), ext_n: q.ext.length, lift_inside: q.VH <= q.VH0 + 1e-9 };
  }
  function coneOverlay(Pj, g, X3, SCL, ph, avoid = []) {
    const K = CONE, s = [], P = (p, h = 0) => Pj.p(...X3(p, h)), pth = (pts) => pts.map((q, i) => (i ? "L" : "M") + n1(q[0]) + " " + n1(q[1])).join("");
    const rim = (phi) => [add(K.M0, mul(K.nn, K.rho0 * Math.cos(phi))), K.rho0 * Math.sin(phi)];
    const N = 48, arc = []; for (let i = 0; i <= N; i++) arc.push(P(...rim((i / N) * PI)));
    const c = P(K.C), m0 = P(K.M0), d0 = [m0[0] - c[0], m0[1] - c[1]];
    // the cone: a faint film, generators every 30°, the base rim (where the drawing stops), and the two outline generators (extreme directions seen from the apex) a little stronger
    s.push(`<path class="cone-film" d="${pth([c, ...arc])}Z"/>`);
    for (let i = 0; i <= N; i += 8) s.push(`<path class="cone-gen" d="${pth([c, arc[i]])}"/>`);
    const ang = arc.map((q) => Math.atan2(d0[0] * (q[1] - c[1]) - d0[1] * (q[0] - c[0]), d0[0] * (q[0] - c[0]) + d0[1] * (q[1] - c[1])));
    const iMin = ang.indexOf(Math.min(...ang)), iMax = ang.indexOf(Math.max(...ang));
    s.push(`<path class="cone-sil" d="${pth([c, arc[iMin]])}${pth([c, arc[iMax]])}"/>`, `<path class="cone-rim" d="${pth(arc)}"/>`);
    // the Dandelin sphere: in this orthographic camera its outline is a circle of radius r·SCL·k; the upper half of that circle + the near half of its great circle on the board
    const a = P(K.A), R = K.r * SCL * Pj.k, eq = [];
    for (let i = 0; i < 144; i++) { const th = (i / 144) * 2 * PI, q = P([K.A[0] + K.r * Math.cos(th), K.A[1] + K.r * Math.sin(th)]); if (q[1] >= a[1] - 1e-6) eq.push(q); }
    eq.sort((u, v) => v[0] - u[0]);
    s.push(`<path class="sphere-film" d="M${n1(a[0] - R)} ${n1(a[1])}A${n1(R)} ${n1(R)} 0 0 1 ${n1(a[0] + R)} ${n1(a[1])}${eq.map((q) => "L" + n1(q[0]) + " " + n1(q[1])).join("")}Z"/>`);
    // the contact circle (sphere and cone touch along it): centre = the midpoint of GE, in the plane through GE perpendicular to the axis; upper half from E over to G
    const Mc = mul(add(g.G, g.E), 0.5), rc = Math.hypot(...sub(g.E, g.G)) / 2, ue = unit2(sub(g.E, g.G)), tc = [];
    for (let i = 0; i <= N; i++) { const phi = (i / N) * PI; tc.push(P(add(Mc, mul(ue, rc * Math.cos(phi))), rc * Math.sin(phi))); }
    s.push(`<path class="touch" d="${pth(tc)}"/>`);
    // v2.3: the cutting plane (through j, perpendicular to the board) — drawn after the sphere and the contact circle (both lie behind it seen from this camera) and BEFORE the parabola, so the curve sits on it;
    //      its edge a thin line, its fill one faint grey (the kit's tones; no new colour); the directrix = the vertical line through D inside it
    const pl = cutPlane(g), HPy = pl.HPy;
    s.push(`<path class="cut-plane" d="${pth(pl.rect.map(([q, h]) => P(q, h)))}Z"/>`, `<path class="cut-dir" d="${pth(pl.dir.map(([q, h]) => P(q, h)))}"/>`);
    // the cut: the parabola (vertex V, focus F) in the plane through j perpendicular to the board, up to P_y lifted above H; a film down to j; the fold (quarter arc about j) to the board's P_y
    // v2.3.1: the parabola is the fixed one (up to P_y lifted at the frozen P_x); the moving point = P_y lifted at this P_x; past the plane's edge the same parabola goes on dashed (cut-ext)
    const par = pl.par.map(([q, h]) => P(q, h)), top = P(...pl.lift);
    s.push(`<path class="cut-film" d="${pth([...par, P(pl.H0), P(g.V)])}Z"/>`, `<path class="cut-line" d="${pth(par)}"/>`);
    if (pl.ext.length) s.push(`<path class="cut-ext" d="${pth(pl.ext.map(([q, h]) => P(q, h)))}"/>`);
    // the focus F (where the plane touches the sphere) and the vertex V: small rings on the board where the plane stands
    for (const k of ["F", "V"]) { const q = P(g[k]); s.push(`<circle class="cut-pt" cx="${n1(q[0])}" cy="${n1(q[1])}" r="5.2"/>`); }
    const eb = unit2(sub(g.P_y, g.H)), fold = []; for (let i = 0; i <= 16; i++) { const psi = (i / 16) * (PI / 2); fold.push(P(add(g.H, mul(eb, HPy * Math.cos(psi))), HPy * Math.sin(psi))); }
    s.push(`<path class="fold" d="${pth(fold)}"/>`, `<circle class="lift" cx="${n1(top[0])}" cy="${n1(top[1])}" r="3.4"/>`);
    if (!ph) {   // the names (desk / video); the phone carries them in the keys under the figure
      const TN = (x, y, txt, o) => { avoid.push(boxOf(x, y, txt, o.fs, o.a)); return T(x, y, txt, o); };   // v2.2's names, at v2.2's places (their boxes join the list the plane's names avoid)
      const rt = arc[Math.round(N / 2)];   // the top of the base rim
      s.push(TN(rt[0] - 12, rt[1] + FS * 1.2, L("円錐(頂点 C)", "cone (apex C)"), { c: "conel", fs: FS * 0.92, a: "end" }));
      s.push(TN(a[0], a[1] - R - 7, L("Dandelin 球(中心 A)", "Dandelin sphere (centre A)"), { c: "conel", fs: FS * 0.92, a: "middle" }));
      const ct = tc[Math.round(N / 2)]; s.push(TN(ct[0] + 8, ct[1] - 6, L("接触円", "contact circle"), { c: "conel", fs: FS * 0.92 }));
      const pm = par[Math.round(par.length * 0.88)]; s.push(TN(pm[0] - 10, pm[1] + FS * 1.1, L("切り口の放物線", "the cut's parabola"), { c: "conel", fs: FS * 0.92, a: "end" }));   // left of the curve's upper part (clear of the sphere's name)
      // v2.3: the names inside the cutting plane (desk / video; the phone carries them in the key line): the plane, the focus F, the vertex V, the directrix through D.
      //       Each goes to the first of its candidate places whose box is clear of every name already there (the board's points and lines, the overlay's names); P_x moves, so the place can change with t.
      const fsn = FS * 0.92, hit = (b) => avoid.some((q) => q[0] < b[2] - 1 && b[0] < q[2] - 1 && q[1] < b[3] - 1 && b[1] < q[3] - 1), inVB = (b) => b[0] >= 2 && b[1] >= 2 && b[2] <= VW - 2 && b[3] <= VH - 2;   // desk / video viewBox = [0, 0, VW, VH]
      const put = (txt, cands) => { const c = cands.find(([x, y, an]) => { const b = boxOf(x, y, txt, fsn, an); return inVB(b) && !hit(b); }) || cands[0]; avoid.push(boxOf(c[0], c[1], txt, fsn, c[2])); return T(c[0], c[1], txt, { c: "planel", fs: fsn, a: c[2] }); };
      const at = (q, h) => P(q, h), on = (sr, h) => at(add(g.F, mul(pl.u, pl.s0 + (pl.s1 - pl.s0) * sr)), h);
      const cT = [[0.5, 1], [0.3, 1], [0.7, 1], [0.15, 1], [0.5, 0.7], [0.5, 0.45]].map(([r, k]) => on(r, pl.top * k)), cF = at(g.F, 1.15), cF2 = at(g.F, 0.5), cD = at(g.D, pl.top * 0.93), cD2 = at(g.D, pl.top * 0.6), cD3 = at(g.D, pl.top * 0.35);   // lower places too: at a P_x moved far the plane's top leaves the frame
      const cV = at(g.V, 1.5), cV2 = at(g.V, 0.35), cV3 = at(g.V, 2.6);
      s.push(put(L("切り口の面", "the cutting plane"), cT.map((q) => [q[0], q[1] + FS * 1.35, "middle"])));                         // under the top edge (middle first)
      s.push(put(L("焦点 F", "focus F"), [[cF[0], cF[1], "middle"], [cF2[0] - 8, cF2[1], "end"], [cF2[0] + 8, cF2[1]]]));           // above F (inside the curve) first
      s.push(put(L("頂点 V", "vertex V"), [[cV[0] + 6, cV[1]], [cV2[0] - 8, cV2[1], "end"], [cV3[0] + 6, cV3[1]], [cV2[0] + 8, cV2[1]]]));   // above V, right of the curve first
      s.push(put(L("準線", "directrix"), [[cD[0] + 6, cD[1]], [cD[0] - 6, cD[1], "end"], [cD2[0] + 6, cD2[1]], [cD3[0] + 6, cD3[1]]]));                 // right of the directrix, near its top first
    }
    return `<g class="cone-overlay" data-overlay="cone">${s.join("")}</g>`;
  }
  function drawBoard(S, A, Pj, focus) {
    // the drafting board: a plate on four feet; the construction is drawn on its top face (z = ZT). World units: 1 coordinate unit = SCL.
    const g = construct(PxAt(S.t)), SCL = 21, cx = -0.6, cy = -3.3, ZT = 16, X = (p) => [(p[0] - cx) * SCL, -(p[1] - cy) * SCL, ZT + 0.3];   // y is flipped: the kit's floor axes are left-handed on screen, so this keeps the figure un-mirrored
    const BW = 330, BD = 420, s = [];
    const solids = [box(Pj, -BW / 2 - 10, -BD / 2 - 10, 0, 18, 18, 6), box(Pj, BW / 2 - 8, -BD / 2 - 10, 0, 18, 18, 6), box(Pj, BW / 2 - 8, BD / 2 - 8, 0, 18, 18, 6), box(Pj, -BW / 2 - 10, BD / 2 - 8, 0, 18, 18, 6)].sort((a, b) => a.d - b.d);
    s.push(...solids.map((o) => o.svg));
    s.push(box(Pj, -BW / 2 - 12, -BD / 2 - 12, 6, BW + 24, BD + 24, 10, { edge: "mid" }).svg);
    s.push(screws(Pj, -BW / 2 - 12, -BD / 2 - 12, ZT, BW + 24, BD + 24, 7));
    // ruler strip with ticks along the near x edge (every 1 coordinate unit; a major every 5)
    for (let u = -7; u <= 6; u++) { const xx = (u - cx) * SCL; if (Math.abs(xx) > BW / 2) continue; const a = Pj.p(xx, BD / 2 + 8, ZT), b = Pj.p(xx, BD / 2 + (u % 5 === 0 ? 1 : 4), ZT); s.push(`<path class="iso-line" data-tone="${u % 5 === 0 ? "mid" : "lo"}" d="M${n1(a[0])} ${n1(a[1])}L${n1(b[0])} ${n1(b[1])}"/>`); }
    const line = (p, q, cls = "cons") => { const a = Pj.p(...X(p)), b = Pj.p(...X(q)); return `<path class="${cls}" d="M${n1(a[0])} ${n1(a[1])}L${n1(b[0])} ${n1(b[1])}"/>`; };
    const ext = (p, dir, t0, t1, cls) => line(add(p, mul(dir, t0)), add(p, mul(dir, t1)), cls);
    const unit = (v) => { const n = Math.hypot(...v); return [v[0] / n, v[1] / n]; };
    // circle c
    let d = ""; for (let i = 0; i <= 72; i++) { const a = (i / 72) * 2 * PI, q = Pj.p(...X([g.A[0] + DATA.construction.radius * Math.cos(a), g.A[1] + DATA.construction.radius * Math.sin(a)])); d += (i ? "L" : "M") + n1(q[0]) + " " + n1(q[1]); }
    s.push(`<path class="cons circ" d="${d}"/>`);
    // v2.2 (BRIEF v2.2 §2-2): h1 (P_x rides on it), e (the directrix), j and the generatrices f, g run to the edges of the plate (and on to the points they carry if those lie beyond it); their names are on the board.
    //   v2.1 drew h1 and e as short pieces around V and D (and j only from H to D), so that what P_x moves on was hard to see (先生 11-07).
    const PL = [cx - (BW / 2 + 9) / SCL, cx + (BW / 2 + 9) / SCL, cy - (BD / 2 + 9) / SCL, cy + (BD / 2 + 9) / SCL];   // the plate's top face in coordinate units (3 units inside its rim)
    const span = (p, u, ...on) => { let lo = -Infinity, hi = Infinity; for (const [k, a, b] of [[0, PL[0], PL[1]], [1, PL[2], PL[3]]]) { if (Math.abs(u[k]) < 1e-12) continue; const t0 = (a - p[k]) / u[k], t1 = (b - p[k]) / u[k]; lo = Math.max(lo, Math.min(t0, t1)); hi = Math.min(hi, Math.max(t0, t1)); }
      const ts = on.map((q) => dot2(sub(q, p), u)); return [Math.min(lo, ...ts), Math.max(hi, ...ts), lo, hi]; };
    const fU = unit(sub(g.G, g.C)), gU = unit(sub(g.E, g.C)), jU = unit(g.fd), eU = unit(g.ed);
    const sf = span(g.C, fU, g.G), sg = span(g.C, gU, g.E, g.J), sj = span(g.F, jU, g.V, g.D, g.H), se = span(g.D, eU, g.K), sh = span(g.V, eU, g.P_x);
    s.push(ext(g.C, fU, 0, sf[1], "cons"), ext(g.C, gU, 0, sg[1], "cons"), line(g.G, g.F, "cons thin"));                            // the tangents f (at G) and g (at E) from the apex C to the plate's edge, the diameter GF
    s.push(line(g.G, g.D, "cons thin"));                                                                                             // the chord GE to D
    s.push(ext(g.F, jU, sj[0], sj[1], "cons"), ext(g.D, eU, se[0], se[1], "cons"), ext(g.V, eU, sh[0], sh[1], "cons"));             // j, e (through D, perpendicular to j), h1 (through V, parallel to e)
    const avoid = [];   // v2.3: the boxes of the board's names (line names, point names), so that the cutting plane's names are put where they do not sit on one (P_x moves)
    const lineName = (p, u, tEnd, back, txt, dx, dy) => { const q = Pj.p(...X(add(p, mul(u, tEnd - back)))); avoid.push(boxOf(q[0] + dx, q[1] + dy, txt, FS * 0.92)); return T(q[0] + dx, q[1] + dy, txt, { c: "linel", fs: FS * 0.92 }); };
    const lineNames = [lineName(g.V, eU, sh[3], 0.9, "h1", -26, 4), lineName(g.D, eU, se[3], 0.9, narrow() ? "e" : L("e(準線)", "e (directrix)"), 9, 6), lineName(g.F, jU, sj[3], 0.5, "j", -4, -9),
                       lineName(g.C, fU, sf[3], 0.8, "f", -2, 16), lineName(g.C, gU, sg[3], 0.9, "g", -18, 2)];
    s.push(line(g.F, g.K, "cons"), ext(g.P_x, unit(perp(sub(g.P_x, g.F))), -1.2, 10.6, "cons thin"));                              // the ray F P_x K, the line m
    s.push(line(g.K, g.P_y, "cons"), line(g.P_y, g.H, "cons"), line(g.H, g.J, "cons"));                                               // K -> P_y (parallel to j), P_y -> H (parallel to h1), H -> J (parallel to GE)
    const named = ["A", "C", "G", "E", "F", "V", "D", "K", "P_y", "H", "J", "P_x"];
    const lab = { A: "A", C: "C", G: "G", E: "E", F: "F", V: "V", D: "D", K: "K", P_y: "P_y", H: "H", J: "J", P_x: "P_x" };
    const off = { A: [-14, -6], C: [8, -6], G: [-16, -6], E: [9, 4], F: [-16, 12], V: [10, 14], D: [10, 4], K: [9, -6], P_y: [-30, -8], H: [-16, 14], J: [8, 14], P_x: [9, -8] };
    const tags = [];
    for (const k of named) {
      const q = Pj.p(...X(g[k])), on = focus.includes(k), dim = focus.length && !on;
      avoid.push(boxOf(q[0] + off[k][0], q[1] + off[k][1], lab[k], FS * (on ? 1.15 : 1)), [q[0] - 5, q[1] - 5, q[0] + 5, q[1] + 5]);   // the name and the dot
      tags.push(`<circle class="cpt${on ? " on" : ""}${dim ? " dim" : ""}" cx="${n1(q[0])}" cy="${n1(q[1])}" r="${on ? 4.2 : 2.6}"/>`);
      tags.push(T(q[0] + off[k][0], q[1] + off[k][1], lab[k], { c: on ? "cptl on" : dim ? "cptl dim" : "cptl", fs: FS * (on ? 1.15 : 1) }));
    }
    const over = S.cone !== false ? coneOverlay(Pj, g, (p, h = 0) => [(p[0] - cx) * SCL, -(p[1] - cy) * SCL, ZT + 0.3 + h * SCL], SCL, narrow(), avoid) : "";
    return s.join("") + over + lineNames.join("") + tags.join("");
  }

  // ---- the answer board (a solid slab of two layers, fixed oblique view): upper = the answer field (conjecture) · lower = the reason field. Text stays level.
  //      tone: "floor" (grey) · "apex" (blue edge) · "empty" (dashed frame: a part with no content is still drawn as a frame) · "locus" (grey, dashed underline = not the floor)
  function slab(x, y, w, h, tone, title, body, o = {}) {
    const dx = 14, dy = 10, s = [];
    s.push(`<path class="iso-shade" data-shade="2" d="M${n1(x + w)} ${n1(y)}L${n1(x + w + dx)} ${n1(y - dy)}L${n1(x + w + dx)} ${n1(y + h - dy)}L${n1(x + w)} ${n1(y + h)}Z"/>`);
    s.push(`<path class="iso-top" d="M${n1(x)} ${n1(y)}L${n1(x + dx)} ${n1(y - dy)}L${n1(x + w + dx)} ${n1(y - dy)}L${n1(x + w)} ${n1(y)}Z"/>`);
    s.push(`<rect class="slab ${tone}" x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(h)}"/>`);
    s.push(T(x + 10, y + FS * 1.35, title, { c: "muted", fs: FS * 0.92 }));
    s.push(lines(x + 10, y + FS * 2.75, body, { c: tone === "empty" ? "muted" : "strong" }));
    return s.join("");
  }
  // one board = header + the answer field + the reason field. `sc` = a scene row (or null for the empty board of A0). Returns {svg, h}.
  function board(x, y, w, sc, o = {}) {
    const fsb = FS, padT = fsb * 2.4, s = [];
    const head = o.head || (sc ? `${sc.model} · ${o.card || sc.card || ""} · ${sc.arm} · r${sc.rep}` : L("答えの板(空)", "the answer board (empty)"));
    s.push(T(x, y + fsb, head, { c: "strong", w: 700 }));
    const subL = o.sub ? wrap(o.sub, w, fsb * 0.92) : [];
    if (subL.length) s.push(lines(x, y + fsb * 2.25, subL, { c: "muted", fs: fsb * 0.92, lh: fsb * 1.2 }));
    const top = y + padT + (subL.length ? fsb * 0.9 + (subL.length - 1) * fsb * 1.2 : 0) + 10;
    const ans = sc ? wrap(o.ans || sc.conjecture, w - 24, fsb) : [L("(空)", "(empty)")];
    const ansShow = ans.slice(0, o.maxAns || 4); if (ans.length > ansShow.length) ansShow[ansShow.length - 1] += " …";
    const hA = fsb * 3.1 + ansShow.length * fsb * 1.38;
    s.push(slab(x, top, w, hA, o.ansTone || (sc ? "floor" : "empty"), L("答えの欄(conjecture)", "answer field (conjecture)"), ansShow));
    const rs = o.reason ? o.reason.flatMap((r, i) => wrap((i ? "→ " : "") + r, w - 24, fsb)) : wrap(o.reasonEmpty || L("(空)", "(empty)"), w - 24, fsb);
    const mk = o.mark ? wrap(o.mark, w - 24, fsb * 0.86) : [];
    const hR = fsb * 3.1 + rs.length * fsb * 1.38 + mk.length * fsb * 1.1, top2 = top + hA + 12;
    s.push(slab(x, top2, w, hR, o.reasonTone || "empty", L("理由の欄(reason)", "reason field (reason)"), rs));
    if (mk.length) s.push(lines(x + w - 8, top2 + hR - 8 - (mk.length - 1) * fsb * 1.1, mk, { c: "muted", fs: fsb * 0.86, a: "end", lh: fsb * 1.1 }));
    return { svg: s.join(""), h: top2 + hR - y };
  }

  // ---- the unit chart: one strip of dots per cell (model x arm of one card). The path is the line under the dots: solid = API, dashed = `claude -p`, dotted = local MLX.
  const pathName = (p) => (p === "api" ? "API" : p === "cc" ? "claude -p" : "MLX");
  function dot(cx, cy, r, code, o = {}) {
    const c = `cx="${n1(cx)}" cy="${n1(cy)}"`;
    switch (code) {
      case "A": return `<circle class="dt dA" ${c} r="${r}"/>`;
      case "R": return `<circle class="dt dR" ${c} r="${r - 0.8}"/>`;
      case "F": case "E": case "D": return `<circle class="dt dF" ${c} r="${r * 0.62}"/>`;
      case "C": case "S": return `<circle class="dt dR" ${c} r="${r - 0.8}"/><circle class="dt dA" ${c} r="${r * 0.38}"/>`;
      case "Sm": return `<circle class="dt dR" ${c} r="${r - 0.8}"/><circle class="dt dA" ${c} r="${r * 0.38}"/><path class="dt dX" d="M${n1(cx + r * 0.5)} ${n1(cy - r * 1.3)}l${n1(r * 0.7)} ${n1(r * 0.7)}m0 ${n1(-r * 0.7)}l${n1(-r * 0.7)} ${n1(r * 0.7)}"/>`;
      case "L": return `<circle class="dt dR" ${c} r="${r - 0.8}"/>`;
      case "M": return `<path class="dt dX" d="M${n1(cx - r * 0.7)} ${n1(cy - r * 0.7)}L${n1(cx + r * 0.7)} ${n1(cy + r * 0.7)}M${n1(cx + r * 0.7)} ${n1(cy - r * 0.7)}L${n1(cx - r * 0.7)} ${n1(cy + r * 0.7)}"/>`;
      case "Z": return `<circle class="dt dZ" ${c} r="${r - 0.8}"/>`;
      default: return `<circle class="dt dN" ${c} r="${r - 1}"/>`;
    }
  }
  const countText = (c) => {
    if (c.kind === "cut") return L(`答えの欄 ${c.ans} / ${c.n} · 全体 ${c.bind} / ${c.n} · 床 ${c.floor}`, `answer field ${c.ans} / ${c.n} · whole ${c.bind} / ${c.n} · floor ${c.floor}`);
    if (c.kind === "prf1") return `END-only ${c["END-only"]} · CHAIN ${c.CHAIN} · LAT-only ${c["LAT-only"]} · none ${c.none} / ${c.n}`;
    if (c.kind === "prf3") return L(`LAT_SYM ${c.lat_sym} / ${c.n}(壊れを除き ${c.lat_sym_ok} / ${c.n_ok})· FD_USE ${c.fd_use} · 壊れ ${c.malformed}`, `LAT_SYM ${c.lat_sym} / ${c.n} (${c.lat_sym_ok} / ${c.n_ok} without malformed) · FD_USE ${c.fd_use} · malformed ${c.malformed}`);
    if (c.kind === "olmk") return L(`答えの欄 ${c.ans} / ${c.n} · 全体 ${c.bind} / ${c.n} · 床 ${c.floor} · 空の行 ${c.empty}`, `answer field ${c.ans} / ${c.n} · whole ${c.bind} / ${c.n} · floor ${c.floor} · empty rows ${c.empty}`);
    return L(`床 ${c.floor} / ${c.n} · 答えの欄の cut ${c.ans} · 空の行 ${c.empty}`, `floor ${c.floor} / ${c.n} · answer-field cut ${c.ans} · empty rows ${c.empty}`);
  };
  // one strip: label (model · arm), the dots, the counts, the path and effort. `w` = the width available. Returns {svg, h}.
  function strip(x, y, id, w, o = {}) {
    const c = C(id), r = o.r || (FS * 0.42), gap = r * 2.55, s = [];
    const label = o.label || `${c.model} · ${c.label}`;
    const tag = `${pathName(c.path)} · ${c.effort}${c.card ? " · " + c.card : ""}`;
    const twoLine = w < 640 || o.stack;
    s.push(`<g class="strip" data-cell="${esc(id)}" data-dots="${c.dots.join("")}"${o.go !== undefined ? ` data-goto="${o.go}"` : ""}>`);
    if (o.go !== undefined) s.push(`<rect class="hit" x="${n1(x - 4)}" y="${n1(y - FS * 1.1)}" width="${n1(w + 8)}" height="${n1(twoLine ? FS * 3.9 : FS * 2.6)}"/>`);
    s.push(T(x, y, label, { c: "strong", w: 600 }));
    const labW = twoLine ? 0 : Math.min(o.labW || 250, w * 0.34);
    const x0 = x + labW + (twoLine ? 0 : 6), y0 = twoLine ? y + FS * 1.15 : y - FS * 0.36;
    const per = Math.max(10, Math.floor((w - labW - 8) / gap)), rowsN = Math.ceil(c.dots.length / per);
    c.dots.forEach((code, i) => { const col = i % per, row = Math.floor(i / per); s.push(dot(x0 + r + col * gap, y0 + row * gap * 1.1, r, code)); if (o.marks && o.marks[i]) s.push(`<path class="mk ${o.marks[i]}" d="M${n1(x0 + col * gap)} ${n1(y0 + row * gap * 1.1 + r + 3)}h${n1(r * 2)}"/>`); if (o.hl && o.hl.includes(c.reps[i])) s.push(`<circle class="dt hl" cx="${n1(x0 + r + col * gap)}" cy="${n1(y0 + row * gap * 1.1)}" r="${n1(r + 3.2)}"/>`); });
    const dotsW = Math.min(c.dots.length, per) * gap, yl = y0 + (rowsN - 1) * gap * 1.1 + r + 5;
    s.push(`<path class="pathline ${c.path}" d="M${n1(x0)} ${n1(yl)}h${n1(dotsW)}"/>`);
    const ty = yl + FS * 1.15;
    const cl = wrap(countText(c) + (c.incomplete ? L(` · INCOMPLETE(raw の在る ${c.n} 本)`, ` · INCOMPLETE (${c.n} rows with raw)`) : ""), w - (x0 - x), FS * 0.93);
    s.push(lines(x0, ty, cl, { c: "", fs: FS * 0.93, lh: FS * 1.2 }));
    const ty2 = ty + (cl.length - 1) * FS * 1.2;
    s.push(T(x0, ty2 + FS * 1.2, tag, { c: "muted", fs: FS * 0.86 }));
    s.push(`</g>`);
    return { svg: s.join(""), h: ty2 + FS * 1.2 - y + FS * 1.1 };
  }
  // the map's one-line strip: label · dots · counts; the path is the line under the dots (solid API / dashed claude -p / dotted local)
  function mini(x, y, id, w) {   // the map's strip: label · dots · counts (+ path · effort · card). The path is the line under the dots (solid API / dashed claude -p / dotted local).
    const c = C(id), ph = narrow(), r = FS * 0.3, gap = r * 2.4, labW = ph ? 0 : Math.min(175, w * 0.33), s = [];
    const cnt = c.kind === "cut" ? L(`答 ${c.ans} · 全 ${c.bind} / ${c.n}`, `ans ${c.ans} · whole ${c.bind} / ${c.n}`) + (c.incomplete ? " · INCOMPLETE" : "") : c.kind === "prf3" ? `LAT_SYM ${c.lat_sym} / ${c.n}` : c.kind === "prf1" ? `END ${c["END-only"]} · CHAIN ${c.CHAIN} / ${c.n}` : L(`床 ${c.floor} / ${c.n}`, `floor ${c.floor} / ${c.n}`);
    const tag = `${pathName(c.path)} · ${c.effort} · ${c.card}`;
    s.push(`<g class="strip" data-cell="${esc(id)}" data-dots="${c.dots.join("")}">`);
    if (ph) {   // the phone: label + counts on one line, the dots under it
      s.push(T(x, y, `${c.model} · ${c.label} — ${cnt}`, { c: "strong", fs: FS * 0.86 }));
      c.dots.forEach((code, i) => s.push(dot(x + r + i * gap, y + FS * 0.95, r, code)));
      s.push(`<path class="pathline ${c.path}" d="M${n1(x)} ${n1(y + FS * 0.95 + r + 4)}h${n1(c.dots.length * gap)}"/>`, T(x + c.dots.length * gap + 8, y + FS * 1.25, `${pathName(c.path)} · ${c.effort}`, { c: "muted", fs: FS * 0.86 }), `</g>`);
      return { svg: s.join(""), h: FS * 2.45 };
    }
    const x0 = x + labW, yd = y - FS * 0.33, dotsW = c.dots.length * gap;
    s.push(T(x, y, `${c.model} · ${c.label}`, { c: "strong", fs: FS * 0.88 }));
    c.dots.forEach((code, i) => s.push(dot(x0 + r + i * gap, yd, r, code)));
    s.push(`<path class="pathline ${c.path}" d="M${n1(x0)} ${n1(yd + r + 4)}h${n1(dotsW)}"/>`);
    s.push(T(x0 + dotsW + 9, y, cnt, { fs: FS * 0.88 }), T(x0 + dotsW + 9, y + FS * 0.98, tag, { c: "muted", fs: FS * 0.86 }));
    s.push(`</g>`);
    return { svg: s.join(""), h: FS * (VIDEO ? 1.98 : 2.12) };
  }
  // a column of strips with an optional group heading
  function column(x, y, w, items) {
    let s = "", yy = y;
    for (const it of items) {
      if (it.h) { const hl = wrap(it.h, w, FS * 1.02); s += lines(x, yy + FS * 1.25, hl, { c: "h", w: 700, fs: FS * 1.02, lh: FS * 1.3 }); yy += FS * 0.6 + hl.length * FS * 1.3 + 4; continue; }
      if (it.note) { const ls = wrap(it.note, w, FS * 0.92); s += lines(x, yy + FS * 1.1, ls, { c: "muted", fs: FS * 0.92 }); yy += ls.length * FS * 1.3 + FS * 0.6; continue; }
      if (it.gap) { yy += it.gap; continue; }
      const st = strip(x, yy + FS, it.id, w, it); s += st.svg; yy += st.h + 4;
    }
    return { svg: s, h: yy - y };
  }
  // a card of a sentence added to the question (verbatim, with its source)
  function sentenceCard(x, y, w, title, text, src) {
    const ls = wrap(text, w - 24, FS * 0.95, true), tl = wrap(title, w - 24, FS), sl = wrap(src, w - 24, FS * 0.86), h = FS * 1.3 + tl.length * FS * 1.3 + ls.length * FS * 1.31 + sl.length * FS * 1.15 + FS * 0.6;
    return { svg: `<rect class="card" x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(h)}" rx="5"/>` + lines(x + 12, y + FS * 1.4, tl, { c: "h", w: 700, lh: FS * 1.3 }) + lines(x + 12, y + FS * 1.4 + tl.length * FS * 1.3 + FS * 0.2, ls, { c: "quote", fs: FS * 0.95, lh: FS * 1.31 }) + lines(x + 12, y + h - FS * 0.6 - (sl.length - 1) * FS * 1.15, sl, { c: "muted", fs: FS * 0.86, lh: FS * 1.15 }), h };
  }

  // ---- the plane layouts: two columns on the video / desk frames, one column on the phone
  function twoCols(left, right, o = {}) {
    const ph = narrow(), W = PW(), pad = ph ? 14 : 34, gap = 40;
    const wl = ph ? W - 2 * pad : (o.split || 0.5) * (W - 2 * pad - gap), wr = ph ? W - 2 * pad : W - 2 * pad - gap - wl;
    const A1 = left(pad, 28, wl), B1 = right(ph ? pad : pad + wl + gap, ph ? 28 + A1.h + 24 : 28, wr);
    const H = ph ? 28 + A1.h + 24 + B1.h + 16 : Math.max(380, 28 + Math.max(A1.h, B1.h) + 16);     // the plate is as tall as its content (the video frame then fills by width)
    return { svg: A1.svg + B1.svg, vb: [0, 0, W, n1(H)] };
  }
  const twoColsInner = (x, y, w, left, right) => { if (narrow()) return stack(left, right)(x, y, w); const g = 30, wl = (w - g) * 0.5, A1 = left(x, y, wl), B1 = right(x + wl + g, y, w - wl - g); return { svg: A1.svg + B1.svg, h: Math.max(A1.h, B1.h) }; };
  const stack = (...parts) => (x, y, w) => { let s = "", yy = y; for (const p of parts) { const r = p(x, yy, w); s += r.svg; yy += r.h + 16; } return { svg: s, h: yy - y - 16 }; };
  const col = (items) => (x, y, w) => column(x, y, w, items);
  const sent = (title, key, src) => (x, y, w) => sentenceCard(x, y, w, title, DATA.sentences[key], src);
  const brd = (sid, o) => (x, y, w) => board(x, y, w, SC(sid), o);
  const txt = (arr, o = {}) => (x, y, w) => { const ls = arr.flatMap((t) => wrap(t, w, FS * (o.k || 1))); return { svg: lines(x, y + FS, ls, { c: o.c || "", fs: FS * (o.k || 1) }), h: ls.length * FS * (o.k || 1) * 1.38 + 4 }; };
  const sumTable = () => (x, y, w) => {   // the SUMMARY's frozen table (md5 556b9dfb): the API high arms that give knowledge but not the relation — counts only (the table has no rows per answer)
    const rows = DATA.summary_txt.arms, s = [], name = { "essay4 A": L("問いだけ", "question only"), "essay4 E-abs": L("エッセイの要旨", "essay (summary)"), "essay4 E-full": L("エッセイの全文", "essay (full)"), "essay4 E-full2": L("全文 + 二往復", "full + two turns"), "sym5 A@U": L("名替え", "renamed"), "sym5 E-full@U": L("名替え + 全文", "renamed + full"), "sym5 KF@U": L("名替え + 円錐の枠(旧)", "renamed + cone frame (old)"), "sym5 KF": L("円錐の枠(旧)", "cone frame (old)"), "kfv1 KF": L("円錐の枠(v1)", "cone frame (v1)"), "kfv1 KF@U": L("名替え + 円錐の枠(v1)", "renamed + cone frame (v1)") };
    const ttl = wrap(L("API · effort high · Claude 3〜4 model の合計(SUMMARY の凍結の表から数え直し)", "API · effort high · summed over 3–4 Claude models (recounted from the SUMMARY's frozen table)"), w, FS), y0 = y; s.push(lines(x, y + FS, ttl, { c: "h", w: 700, lh: FS * 1.3 })); y += (ttl.length - 1) * FS * 1.3;
    const c1 = x, c2 = x + w * 0.6, c3 = x + w * 0.8;
    s.push(T(c1, y + FS * 2.6, L("腕(札)", "arm (card)"), { c: "muted", fs: FS * 0.9 }), T(c2, y + FS * 2.6, L("答えの欄", "answer field"), { c: "muted", fs: FS * 0.9 }), T(c3, y + FS * 2.6, L("全体", "whole"), { c: "muted", fs: FS * 0.9 }));
    rows.forEach((r, i) => { const yy = y + FS * 3.9 + i * FS * 1.36; s.push(T(c1, yy, narrow() ? (name[r.card + " " + r.arm] || r.arm) : `${name[r.card + " " + r.arm] || r.arm} (${r.card} ${r.arm})`, { fs: FS * 0.9 }), T(c2, yy, `${r.ans} / ${r.n}`, { fs: FS * 0.9 }), T(c3, yy, `${r.cut} / ${r.n}`, { fs: FS * 0.9 })); });
    const t = DATA.summary_txt.total, yy = y + FS * 3.9 + rows.length * FS * 1.36 + 4;
    s.push(`<path class="iso-line" data-tone="lo" d="M${n1(x)} ${n1(yy - FS * 0.9)}h${n1(w)}"/>`, T(c1, yy + FS * 0.3, L(`${t.arms} 腕の記述の総数`, `${t.arms} arms: a total`), { w: 700, fs: FS * 0.95 }), T(c1, yy + FS * 1.45, L("(札は別・率でない・記述)", "(separate cards; not a rate; a description)"), { c: "muted", fs: FS * 0.86 }), T(c2, yy + FS * 0.3, `${t.ans} / ${t.n}`, { w: 700, fs: FS * 0.95 }), T(c3, yy + FS * 0.3, `${t.cut} / ${t.n}`, { w: 700, fs: FS * 0.95 }));
    return { svg: s.join(""), h: yy + FS * 2.0 - y0 };
  };

  // ---- the three stations (B0) and the map of roads (B1)
  function stations(S, A, Pj) {
    const s = [], tags = [];
    const st = [
      { k: "floor", x: -260, y: 80, tint: "", edge: "mid", ja: ["床 — Pappus", "焦点・準線", "EJ = KP_y"], en: ["floor — Pappus", "focus · directrix", "EJ = KP_y"] },
      { k: "apex", x: 40, y: -190, tint: "apex", edge: "blue", ja: ["apex — Menaechmus", "断片の比例中項", "FV·EJ = FP_x²"], en: ["apex — Menaechmus", "mean proportional of segments", "FV·EJ = FP_x²"] },
      { k: "desc", x: 170, y: 150, tint: "desc", edge: "orange", ja: ["二次式 — Descartes", "読み(L3)の駅", "HP_y² = 4·VF·VH"], en: ["quadratic — Descartes", "a station of READING (L3)", "HP_y² = 4·VF·VH"] },
    ];
    // the floor plate and the roads (flat strips on the ground)
    s.push(box(Pj, -380, -330, 0, 760, 640, 6, { edge: "lo" }).svg);
    const road = (a, b, cls, wdt = 18) => { const dx = b.x - a.x, dy = b.y - a.y, n = Math.hypot(dx, dy), ux = -dy / n * wdt / 2, uy = dx / n * wdt / 2, ax = a.x + 60, ay = a.y + 60, bx = b.x + 60, by = b.y + 60; return `<path class="road ${cls}" d="${poly(Pj, [[ax + ux, ay + uy, 6.5], [bx + ux, by + uy, 6.5], [bx - ux, by - uy, 6.5], [ax - ux, ay - uy, 6.5]])}"/>`; };
    s.push(road(st[0], st[2], "fd"), road(st[0], st[1], "mp"), road(st[1], st[2], "mpq", 12));
    const solids = st.map((o) => ({ o, b: box(Pj, o.x, o.y, 6, 120, 120, 46, { tint: o.tint ? "t-" + o.tint : "", tintSide: o.tint ? "t-" + o.tint : "", edge: o.edge }) })).sort((a, b) => a.b.d - b.b.d);
    for (const { o, b } of solids) { s.push(b.svg); s.push(screws(Pj, o.x, o.y, 52, 120, 120, 8)); const plate = box(Pj, o.x + 24, o.y + 34, 52, 72, 52, 4, { edge: "lo" }); s.push(plate.svg); }
    const ph = narrow(); for (const o of st) { const q = Pj.p(o.x + 60, o.y + 60, 58), t = LANG === "en" ? o.en : o.ja; tags.push(T(q[0], q[1] - 40, ph ? t[0].split(" — ")[0] : t[0], { c: "h " + o.k, a: "middle", w: 700, fs: FS * 1.08 })); if (!ph) tags.push(T(q[0], q[1] - 40 + FS * 1.3, t[1], { c: "muted", a: "middle" })); tags.push(T(q[0], q[1] - 40 + FS * (ph ? 1.3 : 2.5), t[2], { c: "strong", a: "middle" })); }
    const mid = (a, b, f) => Pj.p(a.x + 60 + (b.x - a.x) * f, a.y + 60 + (b.y - a.y) * f, 8);
    const m1 = mid(st[0], st[2], 0.5), m2 = mid(st[0], st[1], 0.45), m3 = mid(st[1], st[2], 0.5);
    if (!ph) tags.push(T(m1[0], m1[1] + FS * 1.6, L("焦点・準線の道(近道)", "the focus–directrix road (the short cut)"), { c: "muted", a: "middle" }));
    tags.push(T(m2[0] - 10, m2[1] - 6, ph ? L("比例中項", "mean prop.") : L("比例中項の道", "the mean-proportional road"), { c: "blue", a: "end" }));
    if (!ph) tags.push(T(m3[0] + 12, m3[1] - 4, L("頂点の比例中項 → 式(prf3 P5B)", "vertex mean proportional → equation (prf3 P5B)"), { c: "blue", a: "start", fs: FS * 0.9 }));
    return s.join("") + tags.join("");
  }
  const MAP = () => [   // the map: EVERY arm × model drawn in chapters C–I (one strip each), grouped by chapter; a click on a group opens its chapter (data-goto)
    [5, L("C 問いだけ・知識(答えの欄は床)", "C question only · knowledge (the answer field stays on the floor)"), ["essay4.A.opus-5-5", "essay4.A.fable-5-1", "essay4.A.sonnet-5-5", "essay4.A.haiku-5-5", "essay4.K.opus-5-5", "essay4.K.haiku-5-5", "mnw1.none/Q1.opus", "mnw1.none/Q1.fable", "neq3.L-name.opus", "neq3.L-text.opus", "neq2f.L-name.fable", "neq2f.L-text.fable", "mnw1.conf/Q1.opus", "mnw1.conf/Q1.fable"]],
    [8, L("D 問いの点の集合を替える(Q2)", "D replace the point set of the question (Q2)"), ["neq3.A.opus", "neq2f.A.fable", "neq3.A/Q2.opus", "neq3.A/Q2.fable", "neq3.L-name/Q2.opus", "neq3.L-text/Q2.opus", "neq3.L-name/Q2.fable", "neq3.L-text/Q2.fable", "neq3.K/Q2.opus", "neq3.K/Q2.fable"]],
    [10, L("E thinking の量と effort(Q2・xhigh = D の A/Q2)", "E thinking and effort (Q2 · xhigh = A/Q2 of D)"), ["neq6.medium.opus", "neq6.high.opus", "neq6.max.opus", "neq6.medium.fable", "neq6.high.fable", "neq6.max.fable"]],
    [12, L("F 理由を求める一文 β′", "F one sentence asking for the reason (β′)"), ["b5bp.Bbp.opus-5-5", "b5bp.Bbp.sonnet-5-5", "b5bp.Bbp.fable-5-1", "rte1.api_max.opus", "rte1.api_max.fable", "rte1.cc_high.opus", "rte1.cc_high.fable", "moy5c.opus", "moy5c.fable", "arg5.A", "arg5.Bbp", "arg5.K", "arg5d.Bbp", "arg5d.K"]],
    [15, L("G 証明を求める / 渡す / 塞ぐ", "G ask for a proof / give / block the short cut"), ["prf1.P5.opus", "prf1.P5.fable", "prf1.P5K.opus", "prf1.P5K.fable", "prf3.P5.opus", "prf3.P5.fable", "prf3.P5B.opus", "prf3.P5B.fable"]],
    [19, L("H 説明と形", "H explanation and form"), ["mnw1.none/Q1f.opus", "mnw1.none/Q1f.fable", "mnw1.conf/Q1f.opus", "mnw1.conf/Q1f.fable", "mnw1.cone/Q1.opus", "mnw1.cone/Q1.fable", "mnw1.cone/Q1f.opus", "mnw1.cone/Q1f.fable"]],
    [22, L("I open weights(床だけ)", "I open weights (floor only)"), ["olm1.natural", "olm1.think", "olm3.think"]],
  ];
  function mapLayout() {   // columns: video 3 (C+D | E+F | G+H+I) · desk 2 (C+D+E | F+G+H+I) · phone 1
    const groups = MAP(), ph = narrow(), W = ph ? 600 : VIDEO ? 1900 : VW, pad = ph ? 14 : 26, gap = 30;
    const cols = ph ? [groups] : VIDEO ? [groups.slice(0, 2), groups.slice(2, 4), groups.slice(4)] : [groups.slice(0, 3), groups.slice(3)];
    const colW = (W - 2 * pad - gap * (cols.length - 1)) / cols.length;
    const build = (gs, x, y) => { let s = "", yy = y; for (const [go, h, ids] of gs) { s += `<g class="mapgrp" data-goto="${go}">`; const hl = wrap(h + "  →", colW, FS * 0.95); s += lines(x, yy + FS, hl, { c: "h link", w: 700, fs: FS * 0.95, lh: FS * 1.2 }); yy += FS * 0.45 + hl.length * FS * 1.2; for (const id of ids) { const st = mini(x + 6, yy + FS, id, colW - 6); s += st.svg; yy += st.h; } s += `</g>`; yy += 8; } return { svg: s, h: yy - y }; };
    let svg = "", H = 0, yy = 20;
    cols.forEach((gs, k) => { const r = build(gs, ph ? pad : pad + k * (colW + gap), ph ? yy : 20); svg += r.svg; H = Math.max(H, (ph ? yy : 20) + r.h); if (ph) yy += r.h; });
    return { svg, vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, H + 10))] };
  }

  // ---- the effort ladder (E0): x = effort (4 steps), depth = model, height = answers; the solid part = a cut in the answer field, the open frame = a cut anywhere (whole). xhigh is another card (neq3): marked, never joined by a line.
  function ladder(S, A, Pj) {
    const steps = [["medium", "neq6.medium"], ["high", "neq6.high"], ["xhigh", "neq3.A/Q2"], ["max", "neq6.max"]], models = [["fable", "Fable 5.1"], ["opus", "Opus 5.5"]];   // Fable behind, Opus in front
    const SX = 150, SY = 300, ZK = 7.5, BW = 54, s = [], tags = [], items = [];
    s.push(box(Pj, -90, -60, -10, steps.length * SX + 60, models.length * SY - 120, 10, { edge: "lo" }).svg);
    // the ruler post (answers out of 20): ticks every 5, a major every 10
    s.push(box(Pj, -78, SY + 30, 0, 8, 8, 20 * ZK, { edge: "mid" }).svg);
    for (let z = 0; z <= 20; z += 5) { const a = Pj.p(-70, SY + 38, z * ZK), b = Pj.p(-70 + (z % 10 ? 8 : 16), SY + 38, z * ZK); s.push(`<path class="iso-line" data-tone="${z % 10 ? "lo" : "mid"}" d="M${n1(a[0])} ${n1(a[1])}L${n1(b[0])} ${n1(b[1])}"/>`); tags.push(T(a[0] - 6, a[1] + 4, String(z), { c: "muted", a: "end", fs: FS * 0.9 })); }
    models.forEach(([mk, mname], j) => steps.forEach(([e, pre], i) => {
      const id = `${pre}.${mk}`, c = C(id), x = i * SX, y = j * SY;
      const hw = c.bind * ZK, ha = c.ans * ZK;
      items.push({ d: Pj.depth(x + BW / 2, y + BW / 2, 0), svg: (ha > 0 ? box(Pj, x, y, 0, BW, BW, ha, { tint: "t-apex", tintSide: "t-apex", edge: "blue" }).svg : `<path class="iso-line" data-tone="lo" d="${poly(Pj, [[x, y, 0.5], [x + BW, y, 0.5], [x + BW, y + BW, 0.5], [x, y + BW, 0.5]])}"/>`) + (hw > ha ? frameBox(Pj, x, y, ha, BW, BW, hw - ha) : "") });
      const q = Pj.p(x + BW / 2, y + BW / 2, Math.max(hw, ha) + 4);
      tags.push(T(q[0], q[1] - FS * 2.6, `${c.ans} / ${c.n}`, { c: "blue", a: "middle", w: 700, fs: FS * 1.05 }), T(q[0], q[1] - FS * 1.45, `${L("全体", "whole")} ${c.bind} · th ${c.thinking_med.toLocaleString("en")}`, { c: "muted", a: "middle", fs: FS * 0.86 }));
      if (j === models.length - 1) { const p = Pj.p(x + BW / 2, y + BW + 40, 0); tags.push(T(p[0], p[1] + FS * 1.2, e + (pre.startsWith("neq3") ? " (neq3)" : " (neq6)"), { c: "strong", a: "middle", w: 700 })); }
      if (i === 0) { const p = Pj.p(-40, y + BW / 2, 0); tags.push(T(p[0] - 8, p[1] + 4, mname, { c: "h", a: "end", w: 700 })); }
    }));
    items.sort((a, b) => a.d - b.d);
    return s.join("") + items.map((o) => o.svg).join("") + tags.join("");
  }
  function frameBox(Pj, x, y, z, w, d, h) {   // the open frame: the edges of a box (no faces) — "whole" above the answer-field part
    const P = (a, b, c) => Pj.p(a, b, c).map(n1).join(" "), X1 = x + w, Y1 = y + d, Z1 = z + h;
    return `<path class="frame" d="M${P(x, y, Z1)}L${P(X1, y, Z1)}L${P(X1, Y1, Z1)}L${P(x, Y1, Z1)}Z M${P(X1, y, z)}L${P(X1, y, Z1)} M${P(X1, Y1, z)}L${P(X1, Y1, Z1)} M${P(x, Y1, z)}L${P(x, Y1, Z1)}"/>`;
  }

  // ---- the pairs (A1 · E1 · H0): two boards side by side on the video / desk frames, stacked on the phone; one scale, one alignment (same card, same model, same question)
  function pair(specL, specR, below) {
    const ph = narrow(), W = PW(), pad = ph ? 14 : 34, gap = 40, w = ph ? W - 2 * pad : (W - 2 * pad - gap) / 2;
    const a = board(pad, 24, w, SC(specL.sid), specL), b = board(ph ? pad : pad + w + gap, ph ? 24 + a.h + 28 : 24, w, SC(specR.sid), specR);
    let y = ph ? 24 + a.h + 28 + b.h + 24 : 24 + Math.max(a.h, b.h) + 24, s = a.svg + b.svg;
    if (below) { const r = below(pad, y, W - 2 * pad); s += r.svg; y += r.h + 10; }
    return { svg: s, vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, y + 8))] };
  }
  const thinkBar = (idL, idR) => (x, y, w) => {   // E1: the thinking of the two rows on ONE scale (token)
    const a = SC(idL).thinking, b = SC(idR).thinking, mx = Math.max(a, b), bw = w * 0.62, s = [];
    s.push(T(x, y + FS, L("thinking の量(token・同じ目盛り・結果の記述)", "thinking (tokens; one scale; a description of the result)"), { c: "h", w: 700 }));
    [[L("medium r0", "medium r0"), a, "lo"], [L("max r0", "max r0"), b, "blue"]].forEach(([k, v, tone], i) => { const yy = y + FS * 2.2 + i * FS * 1.9; s.push(T(x, yy + FS * 0.75, k, { fs: FS * 0.95 }), `<rect class="tbar ${tone}" x="${n1(x + 110)}" y="${n1(yy)}" width="${n1(Math.max(2, (bw * v) / mx))}" height="${n1(FS * 0.95)}"/>`, T(x + 120 + (bw * v) / mx, yy + FS * 0.86, `${v.toLocaleString("en")}`, { fs: FS * 0.95 })); });
    return { svg: s.join(""), h: FS * 6.2 };
  };

  // ---- the return (J0): the two boards of A1 again, small, beside the list of what opened which road (L1, with sources)
  function returnLayout() {
    const ph = narrow(), W = PW(), pad = ph ? 14 : 30, gap = 30, wl = ph ? W - 2 * pad : 330, s = [];
    const a = board(pad, 24, wl, SC("A1L"), { head: "prf3 · Opus 5.5 · P5 r0", ansTone: "floor", reason: [SC("A1L").phrases[0]], reasonTone: "floor", maxAns: 2 });
    const b = board(pad, 24 + a.h + 18, wl, SC("A1R"), { head: "prf3 · Opus 5.5 · P5B r0", ansTone: "floor", reason: SC("A1R").phrases, reasonTone: "apex", maxAns: 2 });
    s.push(a.svg, b.svg);
    const x = ph ? pad : pad + wl + gap, w = ph ? W - 2 * pad : W - 2 * pad - wl - gap; let y = ph ? 24 + a.h + 18 + b.h + 26 : 24;
    const tl = wrap(L("同じ答えの欄の裏で、腕ごとに apex に着いた本の数(言える・L1)", "Behind the same answer field: the number reaching the apex, arm by arm (can say · L1)"), w, FS); s.push(lines(x, y + FS, tl, { c: "h", w: 700, lh: FS * 1.3 })); y += FS * 0.86 + tl.length * FS * 1.3;
    for (const r of FIGURE.returnRows()) { const ls = wrap(r.t, w - 16, FS * 0.95); s.push(`<circle class="dt ${r.mark === "A" ? "dA" : r.mark === "R" ? "dR" : "dN"}" cx="${n1(x + 5)}" cy="${n1(y + FS * 0.62)}" r="${n1(FS * 0.36)}"/>`, lines(x + 16, y + FS, ls, { fs: FS * 0.95 }), T(x + 16, y + FS + ls.length * FS * 1.31, r.src, { c: "muted", fs: FS * 0.86 })); y += (ls.length + 1) * FS * 1.31 + 6; }
    return { svg: s.join(""), vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, Math.max(y, 24 + a.h + 18 + b.h) + 10))] };
  }

  // ---- v2: the summary road per cue (moved from entry P's state 3; the two readers agreed): one row = one cue, Opus and Fable on ONE scale (share of the n of that cell).
  //      dark bar = the answer field · light bar = the whole (answer + reason) · for prf1 / prf3 the bar is the frozen route predicate (CHAIN / LAT_SYM; LAT-only hatched next to it). Controls are listed apart, never on the road.
  const CUES = () => [
    [L("問いだけ", "question only"), "essay4.A.opus-5-5", "essay4.A.fable-5-1", 5, ["essay4.A.sonnet-5-5", "essay4.A.haiku-5-5"]],
    [L("問いだけ(xhigh)", "question only (xhigh)"), "mnw1.none/Q1.opus", "mnw1.none/Q1.fable", 5],
    [L("Q1 + 名", "Q1 + name"), "neq3.L-name.opus", "neq2f.L-name.fable", 6],
    [L("Q1 + 本文", "Q1 + text"), "neq3.L-text.opus", "neq2f.L-text.fable", 6],
    [L("役の対応", "roles"), "mnw1.conf/Q1.opus", "mnw1.conf/Q1.fable", 20],
    [L("Q2(点の集合)", "Q2 (point set)"), "neq3.A/Q2.opus", "neq3.A/Q2.fable", 8],
    [L("Q2 + 名", "Q2 + name"), "neq3.L-name/Q2.opus", "neq3.L-name/Q2.fable", 9],
    [L("Q2 + 本文", "Q2 + text"), "neq3.L-text/Q2.opus", "neq3.L-text/Q2.fable", 9],
    ["effort medium", "neq6.medium.opus", "neq6.medium.fable", 10],
    ["effort high", "neq6.high.opus", "neq6.high.fable", 10],
    ["effort max", "neq6.max.opus", "neq6.max.fable", 10],
    [L("β′ · API high", "β′ · API high"), "b5bp.Bbp.opus-5-5", "b5bp.Bbp.fable-5-1", 12, ["b5bp.Bbp.sonnet-5-5", "arg5.Bbp", "arg5d.Bbp"]],
    [L("β′ · API max", "β′ · API max"), "rte1.api_max.opus", "rte1.api_max.fable", 13],
    [L("β′ · claude -p high", "β′ · claude -p high"), "rte1.cc_high.opus", "rte1.cc_high.fable", 13],
    [L("β′ · claude -p max", "β′ · claude -p max"), "moy5c.opus", "moy5c.fable", 13],
    [L("PROOF", "PROOF"), "prf1.P5.opus", "prf1.P5.fable", 15],
    [L("PROOF + 塞ぎ", "PROOF + block"), "prf3.P5B.opus", "prf3.P5B.fable", 18],
    [L("形の一文", "form sentence"), "mnw1.none/Q1f.opus", "mnw1.none/Q1f.fable", 19],
    [L("役の対応 + 形", "roles + form"), "mnw1.conf/Q1f.opus", "mnw1.conf/Q1f.fable", 20],
    [L("Menaechmus の説明", "Menaechmus explanation"), "mnw1.cone/Q1.opus", "mnw1.cone/Q1.fable", 21],
    [L("説明 + 形", "explanation + form"), "mnw1.cone/Q1f.opus", "mnw1.cone/Q1f.fable", 21],
  ];
  // the two shares a cell gives the road: [answer field, whole, extra (hatched), label]. prf1: CHAIN = the frozen main predicate (PREREG prf1); LAT-only is drawn hatched next to it, so LATX (= CHAIN + LAT-only) is also readable.
  const roadOf = (c) => c.kind === "prf1" ? [0, c.CHAIN, c["LAT-only"], L(`束ね ${c.CHAIN} · 格子 ${c.CHAIN + c["LAT-only"]} / ${c.n}`, `bundled ${c.CHAIN} · lattice ${c.CHAIN + c["LAT-only"]} / ${c.n}`)] : c.kind === "prf3" ? [0, c.lat_sym, 0, `LAT_SYM ${c.lat_sym} / ${c.n}`] : [c.ans, c.bind, 0, L(`答 ${c.ans} · 全 ${c.bind} / ${c.n}`, `ans ${c.ans} · whole ${c.bind} / ${c.n}`)];
  const roadGeom = (w) => { const ph = narrow(), labW = ph ? 0 : Math.min(170, w * 0.3), bw = ph ? (w - 26) / 2 : (w - labW - 24) / 2 - 6; return { ph, labW, bw }; };
  function roadRow(x, y, w, cue) {   // label (+ the card · path · effort under it) | Opus bar | Fable bar; the count under each bar
    const [name, io, iff, go, others] = cue, { ph, labW, bw } = roadGeom(w), s = [], bh = FS * 0.62, fsT = FS * 0.86;
    const tagOf = (c) => `${c.card} · ${pathName(c.path)} · ${c.effort}`, t1 = tagOf(C(io)), t2 = tagOf(C(iff));
    const tag = t1 === t2 ? t1 : `${t1} / ${t2}`, tl = wrap(tag, ph ? w : labW - 8, fsT).slice(0, 2);
    const lab = [T(x, y, name, { c: "strong", w: 600, fs: FS * 0.92 }), lines(x, y + FS * 1.05, tl, { c: "muted", fs: fsT, lh: FS * 1.0 })].join("");
    const by = ph ? y + FS * (1.05 + tl.length) + FS * 0.2 + bh : y + FS * 0.05, x0 = x + labW + (ph ? 0 : 6), hRow = ph ? by - y + FS * 2.35 : Math.max(FS * 2.35, FS * 1.05 + tl.length * FS * 1.0 + FS * 0.45);
    s.push(`<g class="road-row" data-goto="${go}" data-cells="${io} ${iff}">`, `<rect class="hit" x="${n1(x - 3)}" y="${n1(y - FS * 1.0)}" width="${n1(w + 6)}" height="${n1(hRow - 2)}"/>`, lab);
    const bars = (bx, id) => {
      const c = C(id), [a, wh, ex, txt] = roadOf(c), u = bw / c.n;
      s.push(`<rect class="rd-n" x="${n1(bx)}" y="${n1(by - bh)}" width="${n1(bw)}" height="${n1(bh)}"/>`);
      if (wh) s.push(`<rect class="rd-w" x="${n1(bx)}" y="${n1(by - bh)}" width="${n1(u * wh)}" height="${n1(bh)}"/>`);
      if (ex) s.push(`<rect class="rd-x" x="${n1(bx + u * wh)}" y="${n1(by - bh)}" width="${n1(u * ex)}" height="${n1(bh)}"/>`);
      if (a) s.push(`<rect class="rd-a" x="${n1(bx)}" y="${n1(by - bh)}" width="${n1(u * a)}" height="${n1(bh)}"/>`);
      s.push(T(bx, by + FS * 0.95, `${txt}${c.incomplete ? " · INCOMPLETE" : ""}`, { fs: fsT }));
    };
    bars(x0, io); bars(x0 + bw + 22, iff);
    let hOut = hRow;
    if (others && others.length) {   // other models of the same cue: text only (no bar), each with its card · path · effort; never summed with the bars
      const ot = L("ほかの model: ", "other models: ") + others.map((id) => { const c = C(id); return `${c.model.replace(" 5.5", "")}(${c.card} · ${c.effort})${L(`答 ${c.ans} · 全 ${c.bind} / ${c.n}`, ` ans ${c.ans} · whole ${c.bind} / ${c.n}`)}`; }).join(" · ");
      const ol = wrap(ot, ph ? w : w - labW - 6, fsT); s.push(`<g class="road-others" data-cells="${others.join(" ")}">`, lines(ph ? x : x0, y + hRow - FS * 0.2, ol, { c: "muted", fs: fsT, lh: FS * 1.05 }), `</g>`); hOut += ol.length * FS * 1.05 + 2;
    }
    s.push(`</g>`);
    return { svg: s.join(""), h: hOut };
  }
  function roadLayout() {
    const ph = narrow(), W = PW(), pad = ph ? 14 : 30, gap = 36, cues = CUES(), s = [];
    const cols = ph ? [cues] : [cues.slice(0, 11), cues.slice(11)], cw = ph ? W - 2 * pad : (W - 2 * pad - gap) / 2;
    let H = 0;
    cols.forEach((cs, k) => { const x = pad + k * (cw + gap), { labW, bw } = roadGeom(cw), x0 = x + labW + (ph ? 0 : 6); let y = 24 + FS;
      s.push(T(x0, y, "Opus 5.5", { c: "h", w: 700, fs: FS * 0.95 }), T(x0 + bw + 22, y, "Fable 5.1", { c: "h", w: 700, fs: FS * 0.95 })); y += FS * 2.0;
      for (const cue of cs) { const r = roadRow(x, y, cw, cue); s.push(r.svg); y += r.h; } H = Math.max(H, y); });
    let y = H + 4; const x = pad, w = W - 2 * pad;
    const ctl = wrap(FIGURE.controlNote(), w, FS * 0.86); s.push(lines(x, y + FS * 0.9, ctl, { c: "muted", fs: FS * 0.86, lh: FS * 1.2 })); y += ctl.length * FS * 1.2 + 8;
    return { svg: s.join(""), vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, y + 6))] };
  }

  // ---- v2: "show up to the next" (BRIEF v2 §2-4): the cards the house froze AFTER the 10-28 figure. Everything here is drawn inside a hatched band = "added on 11-06" (the 10-28 states carry none of these cards).
  const GRP = ["a", "b", "c", "d"];
  const P_ = (id) => DATA.post.find((p) => p.id === id);
  const gradeName = (g) => ({ 判定: L("判定", "verdict"), 較正: L("較正", "calibration"), 記述: L("記述", "description"), 言えない: L("言えない", "cannot say"), gate: L("関門で止まった", "stopped at a gate") })[g];
  // v2.1: one mark per column of the grade rule (BRIEF v2.1 §2-5): 判定 = filled · 記述 = outline · 較正 = half · 言えない = hatched · 関門で止まった = dashed (no colour added)
  const PMC = { verdict: "pm-v", desc: "pm-d", cal: "pm-c", cannot: "pm-x", gate: "pm-g" };
  const statusMark = (p, x, y, r) => `<rect class="pm ${PMC[p.status]}" x="${n1(x - r)}" y="${n1(y - r)}" width="${n1(2 * r)}" height="${n1(2 * r)}" rx="2"/>` + (p.status === "cal" ? `<rect class="pm pm-v" x="${n1(x - r)}" y="${n1(y - r)}" width="${n1(r)}" height="${n1(2 * r)}"/>` : "") + (p.status === "cannot" ? `<path class="pm-xl" d="M${n1(x - r)} ${n1(y + r)}L${n1(x + r)} ${n1(y - r)}M${n1(x - r)} ${n1(y - r)}L${n1(x + r)} ${n1(y + r)}"/>` : "");
  const topGap = () => (narrow() ? 0 : VIDEO ? FS * 2.0 : FS * 3.4);   // v2.1: room under the plate's corner stamp (HTML over the svg) so the hatched frame's top line never crosses it
  function afterBand(W, H, label) {   // the hatched frame that marks "added after 10-28" on every state of chapter J
    const t0 = topGap();
    return `<rect class="after-band" x="4" y="${n1(4 + t0)}" width="${n1(W - 8)}" height="${n1(H - 8 - t0)}" rx="8"/><rect class="after-tab" x="12" y="${n1(H - 8 - FS * 1.5)}" width="${n1(Math.min(W - 24, tw(label, FS * 0.86) + 20))}" height="${n1(FS * 1.45)}" rx="3"/>` + T(22, H - 8 - FS * 0.4, label, { c: "strong", fs: FS * 0.86 });
  }
  function meterBar(x, y, w, m) {   // a share k / n or a value x on [lo, hi], the frozen line as a solid tick ("凍結の線"); a gate line is the same tick, labelled "関門"
    if (!m) return { svg: "", h: 0 };
    const s = [], bh = FS * 0.55, lo = m.lo ?? 0, hi = m.hi ?? 1, f = m.k !== undefined ? m.k / m.n : m.x, sx = (v) => x + ((Math.max(lo, Math.min(hi, v)) - lo) / (hi - lo)) * w;
    s.push(`<rect class="rd-n" x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(bh)}"/>`, `<rect class="${m.gate ? "rd-g" : "rd-w"}" x="${n1(x)}" y="${n1(y)}" width="${n1(sx(f) - x)}" height="${n1(bh)}"/>`);
    if (m.k2 !== undefined) s.push(`<rect class="rd-w2" x="${n1(x)}" y="${n1(y + bh + 2)}" width="${n1(sx(m.k2 / m.n2) - x)}" height="${n1(bh * 0.7)}"/>`);
    const lx = sx(m.line); s.push(`<path class="frozen-line" d="M${n1(lx)} ${n1(y - 4)}V${n1(y + bh * (m.k2 !== undefined ? 1.9 : 1) + 4)}"/>`);
    if (m.post !== undefined) { const px = sx(m.post); s.push(`<path class="posthoc-line" d="M${n1(px)} ${n1(y - 6)}V${n1(y + bh + 6)}"/>`); }
    const val = m.k !== undefined ? `${m.k} / ${m.n}` : String(Math.round(m.x * 1000) / 1000);
    s.push(T(x + w + 8, y + bh, `${m.lab ? m.lab + " " : ""}${val} · ${m.gate ? L("関門", "gate") : L("凍結の線", "frozen line")} ${m.k !== undefined ? Math.round(m.line * 100) + " %" : (m.below ? "< " : "") + m.line}`, { fs: FS * 0.86, c: "muted" }));
    if (m.post !== undefined) { s.push(T(x, y + bh + FS * 1.0, L(`破線 = 事後 ${Math.round(m.post * 100)} %(2 token 前・判定でない)`, `dashed = post hoc ${Math.round(m.post * 100)} % (2 tokens before; not a verdict)`), { fs: FS * 0.86, c: "muted" })); return { svg: s.join(""), h: bh + FS * 1.2 + 10 }; }
    return { svg: s.join(""), h: bh * (m.k2 !== undefined ? 1.9 : 1) + 10 };
  }
  function postRow(x, y, w, p) {
    const s = [], ph = narrow();
    s.push(`<g class="post-row" data-card="${p.id}" data-status="${p.status}">`);
    s.push(statusMark(p, x + 6, y - FS * 0.32, FS * 0.36));
    const head = `${p.id} · ${p.date} · ${L("凍結", "frozen")} ${p.freeze}`;
    s.push(T(x + 18, y, head, { c: "strong", w: 700, fs: FS * 0.9 }));
    const gx = x + 18 + tw(head, FS * 0.9) + 12, gn = `${gradeName(p.grade)} · (${p.rule})`, gw = tw(gn, FS * 0.86) + 12;
    s.push(`<rect class="grade g-${p.grade}" x="${n1(gx)}" y="${n1(y - FS * 0.95)}" width="${n1(gw)}" height="${n1(FS * 1.25)}" rx="3"/>`, T(gx + 6, y - FS * 0.05, gn, { fs: FS * 0.86, c: "strong" }));
    const hl = wrap(FIGURE.postText(p), w - 18, FS * 0.86); s.push(lines(x + 18, y + FS * 1.15, hl, { fs: FS * 0.86, lh: FS * 1.18 }));
    let yy = y + FS * 1.15 + (hl.length - 1) * FS * 1.18 + FS * 0.55;
    const mb = meterBar(x + 18, yy, Math.min(ph ? w * 0.45 : 220, w * 0.45), p.meter); s.push(mb.svg); if (mb.h) yy += mb.h;
    if (p.meter2) { const m2 = meterBar(x + 18, yy + 4, Math.min(ph ? w * 0.45 : 220, w * 0.45), p.meter2); s.push(m2.svg); yy += m2.h + 4; }
    const sl = wrap(`${L("出所", "source")}: ${p.src || ""} · RESULT ${p.id}`, w - 18, FS * 0.86); s.push(lines(x + 18, yy + FS * 0.75, sl, { c: "muted", fs: FS * 0.86, lh: FS * 1.05 }));
    s.push(`</g>`);
    return { svg: s.join(""), h: yy + FS * 0.75 + (sl.length - 1) * FS * 1.05 - y + FS * 0.9 };
  }
  function postColumn(x, y, w, ids, title) {
    let s = "", yy = y;
    if (title) { const tl = wrap(title, w, FS * 0.98); s += lines(x, yy + FS, tl, { c: "h", w: 700, fs: FS * 0.98, lh: FS * 1.25 }); yy += FS * 0.5 + tl.length * FS * 1.25; }
    for (const id of ids) { const r = postRow(x, yy + FS * 1.05, w, P_(id)); s += r.svg; yy += r.h + 4; }
    return { svg: s, h: yy - y };
  }
  function postLayout(grp) {
    const ph = narrow(), W = PW(), pad = ph ? 16 : 34, gap = 36, s = [];
    const ps = DATA.post.filter((p) => grp.includes(p.grp)), ids = (sts) => ps.filter((p) => sts.includes(p.status)).map((p) => p.id), cnt = (st) => ps.filter((p) => p.status === st).length;
    // v2.1: three blocks by the grade rule's columns, two columns on the page: left = 判定 · right = 記述 / 較正 / 言えない, then 関門で止まった (balanced: the five columns made the left of (b) too tall for the 1080 frame)
    const cw = ph ? W - 2 * pad : (W - 2 * pad - gap) / 2;
    const A1 = postColumn(pad, 26 + topGap(), cw, ids(["verdict"]), L(`判定 ${cnt("verdict")}(凍結の予想に ✓)`, `verdict ${cnt("verdict")} (a ✓ on a frozen prediction)`));
    const xr = ph ? pad : pad + cw + gap, yr = ph ? 26 + A1.h + 18 : 26 + topGap(), mid = ids(["desc", "cal", "cannot"]), gt = ids(["gate"]);
    const B0 = mid.length ? postColumn(xr, yr, cw, mid, L(`記述 ${cnt("desc")} · 較正 ${cnt("cal")} · 言えない ${cnt("cannot")}(SCOPE の段・または段の基準)`, `description ${cnt("desc")} · calibration ${cnt("cal")} · cannot say ${cnt("cannot")} (SCOPE's tiers or its criteria)`)) : { svg: "", h: -18 };
    const B2 = gt.length ? postColumn(xr, yr + B0.h + 18, cw, gt, L(`関門で止まった ${gt.length}(予想を読まない)`, `stopped at a gate ${gt.length} (no prediction read)`)) : { svg: "", h: -18 };
    const B1 = { svg: B0.svg + B2.svg, h: B0.h + 18 + B2.h };
    s.push(A1.svg, B1.svg);
    let y = ph ? 26 + A1.h + 18 + B1.h : 26 + topGap() + Math.max(A1.h, B1.h);
    if (grp.includes("d")) { const r = thkStrips(pad, y + 8, W - 2 * pad); s.push(r.svg); y += r.h + 12; }
    y += FS * 2.2;
    return { svg: s.join("") + afterBand(W, y + 6, ph ? FIGURE.afterLabel().split(/[((]/)[0].trim() : FIGURE.afterLabel()), vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, y + 8))] };
  }
  function thkStrips(x, y, w) {   // thk2: one dot = one row; upper = the answer's cut (ans_cut), lower = the summary's cut (summ_cut); the thinking tokens under each pair
    const rows = DATA.thk2_rows, s = [], r = FS * 0.38, ph = narrow(), gap = ph ? 140 : 92;
    const tl = wrap(L("thk2 · 行ごと(上 = 答えの cut · 下 = 思考の要約の cut · 数 = 思考の token)", "thk2 · per row (top = the answer's cut · bottom = the thinking summary's cut · number = thinking tokens)"), w, FS * 0.9);
    s.push(lines(x, y + FS, tl, { c: "h", w: 700, fs: FS * 0.9, lh: FS * 1.2 })); y += (tl.length - 1) * FS * 1.2;
    rows.forEach((q, i) => { const cx = x + 10 + (ph ? (i % 4) * gap : i * gap + (i >= 4 ? 20 : 0)), cy = y + FS * 2.4 + (ph && i >= 4 ? FS * 4.6 : 0); s.push(`<g class="thk-row" data-ans="${q.ans}" data-summ="${q.summ}">`, `<circle class="dt ${q.ans ? "dA" : "dN"}" cx="${n1(cx)}" cy="${n1(cy)}" r="${n1(r)}"/>`, `<circle class="dt ${q.summ ? "dA" : "dN"}" cx="${n1(cx)}" cy="${n1(cy + FS * 1.2)}" r="${n1(r)}"/>`, T(cx - r, cy + FS * 2.4, `${q.model.split(" ")[0]} r${q.rep}`, { fs: FS * 0.86, c: "muted" }), T(cx - r, cy + FS * 3.6, q.think.toLocaleString("en"), { fs: FS * 0.86 }), `</g>`); });
    return { svg: s.join(""), h: FS * 6.5 + (tl.length - 1) * FS * 1.2 + (ph ? FS * 4.6 : 0) };
  }
  function flowLayout() {   // state 23: one flow — the questions the 10-28 figure showed (the frontier's OUTPUT side) → the cards the house froze after it (reading the frontier's road INSIDE OLMo), by date
    const ph = narrow(), W = PW(), pad = ph ? 16 : 30, s = [], F = FIGURE.flowText();
    const lw = ph ? W - 2 * pad : Math.min(360, W * 0.27), lx = pad;
    let y = 30 + topGap();
    s.push(T(lx, y, F.leftTitle, { c: "h", w: 700 })); y += FS * 0.86;
    for (const [t, go] of F.left) { const ls = wrap(t, lw - 20, FS * 0.88); s.push(`<g class="flow-q" data-goto="${go}"><rect class="hit" x="${n1(lx)}" y="${n1(y)}" width="${n1(lw)}" height="${n1(ls.length * FS * 1.2 + FS * 0.86)}"/><rect class="card solid" x="${n1(lx)}" y="${n1(y)}" width="${n1(lw)}" height="${n1(ls.length * FS * 1.2 + FS * 0.86)}" rx="5"/>${lines(lx + 10, y + FS * 1.15, ls, { fs: FS * 0.88, lh: FS * 1.2 })}</g>`); y += ls.length * FS * 1.2 + FS * 0.86 + 8; }
    const leftH = y;
    // the arrow
    const rx0 = ph ? pad : lx + lw + 64, rw = ph ? W - 2 * pad : W - rx0 - pad;
    if (!ph) { const ay = 30 + topGap() + (leftH - 30 - topGap()) / 2; s.push(`<path class="flow-arrow" d="M${n1(lx + lw + 8)} ${n1(ay)}H${n1(rx0 - 10)}"/><path class="flow-head" d="M${n1(rx0 - 10)} ${n1(ay - 6)}L${n1(rx0 - 2)} ${n1(ay)}L${n1(rx0 - 10)} ${n1(ay + 6)}Z"/>`); }
    let ry = ph ? leftH + 24 : 30 + topGap();
    const ry0 = ry;
    const rtl = wrap(F.rightTitle, rw, FS); s.push(lines(rx0, ry, rtl, { c: "h", w: 700, lh: FS * 1.25 })); ry += FS * 0.6 + (rtl.length - 1) * FS * 1.25;
    const dates = ["10-28", "10-29", "10-30", "10-31"], gw = ph ? 34 : 52, cwid = (rw - gw) / dates.length;
    dates.forEach((d, i) => s.push(T(rx0 + gw + i * cwid + 4, ry + FS * 1.1, d, { c: "muted", fs: FS * 0.86 })));
    ry += FS * 1.6;
    for (const g of GRP) {
      const ps = DATA.post.filter((p) => p.grp === g), byD = dates.map((d) => ps.filter((p) => p.date === d)), rowsN = Math.max(1, ...byD.map((a) => a.length)), chipH = FS * 1.5, rh = rowsN * (chipH + 4) + FS * 1.6;
      s.push(`<g class="flow-grp" data-goto="${F.goOf[g]}"><rect class="hit" x="${n1(rx0)}" y="${n1(ry)}" width="${n1(rw)}" height="${n1(rh)}"/>`);
      s.push(`<path class="iso-line" data-tone="lo" d="M${n1(rx0)} ${n1(ry)}h${n1(rw)}"/>`, T(rx0, ry + FS * 1.2, `(${g})`, { c: "h link", w: 700 }));
      const gl = wrap(F.grpName[g], rw - gw - 8, FS * 0.86); s.push(lines(rx0 + gw, ry + FS * 1.1, gl.slice(0, 1), { c: "muted", fs: FS * 0.86 }));
      byD.forEach((a, i) => a.forEach((p, k) => { const cx = rx0 + gw + i * cwid + 2, cy = ry + FS * 1.6 + k * (chipH + 4), cwc = Math.min(cwid - 8, tw(p.id, FS * 0.86) + FS * 1.6 + 10); s.push(`<rect class="chip chip-${p.status}" x="${n1(cx)}" y="${n1(cy)}" width="${n1(cwc)}" height="${n1(chipH)}" rx="4" data-card="${p.id}"/>`, statusMark(p, cx + FS * 0.6, cy + chipH / 2, FS * 0.3), T(cx + FS * 1.2, cy + chipH * 0.72, p.id, { fs: FS * 0.86, c: "strong" })); }));
      s.push(`</g>`); ry += rh + 6;
    }
    const t = DATA.post_tally, tl = wrap(F.tally(t), rw, FS * 0.9); s.push(lines(rx0, ry + FS * 1.1, tl, { c: "strong", w: 700, fs: FS * 0.9, lh: FS * 1.25 })); ry += tl.length * FS * 1.25 + 6;
    const rl = wrap(F.rule, rw, FS * 0.86); s.push(lines(rx0, ry + FS, rl, { c: "muted", fs: FS * 0.86, lh: FS * 1.15 })); ry += rl.length * FS * 1.15 + FS * 0.6;
    const H = Math.max(leftH, ry) + FS * 2.4;
    // only the right part is "after": the hatched frame and its tab go around it; the left part (the 10-28 figure's questions) stays outside the frame
    const bx = ph ? rx0 - 8 : rx0 - 12, by = ry0 - FS * 1.6, bw = ph ? rw + 16 : rw + 22, bh = ry - ry0 + FS * 3.6, lab = ph ? FIGURE.afterLabel().split(/[((]/)[0].trim() : FIGURE.afterLabel();
    s.push(`<rect class="after-band" x="${n1(bx)}" y="${n1(by)}" width="${n1(bw)}" height="${n1(bh)}" rx="8"/><rect class="after-tab" x="${n1(bx + 8)}" y="${n1(by + bh - FS * 1.6)}" width="${n1(Math.min(bw - 16, tw(lab, FS * 0.86) + 20))}" height="${n1(FS * 1.45)}" rx="3"/>`, T(bx + 18, by + bh - FS * 0.5, lab, { c: "strong", fs: FS * 0.86 }));
    const H2 = Math.max(leftH, by + bh) + 8;
    return { svg: s.join(""), vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, H2 + 2))] };
  }
  function n4Layout() {   // state 27: the five bundles of next questions the readers raised and the house has not fired (RESULT station 3 §1 N4). Drawn alike: no emphasis (the PI's choice is not made = C7).
    const ph = narrow(), W = PW(), pad = ph ? 16 : 34, gap = 24, s = [], B = FIGURE.n4Text(), cols = ph ? 1 : 3, cw = (W - 2 * pad - gap * (cols - 1)) / cols;
    let y = 26; const tl = wrap(B.title, W - 2 * pad, FS); s.push(lines(pad, y + FS, tl, { c: "h", w: 700, lh: FS * 1.3 })); y += tl.length * FS * 1.3 + 12;
    const hs = [];
    const kOf = (it) => wrap(`${it.k} · ${it.n} ${L("問", "questions")}${it.home ? " · " + B.home : ""}`, cw - 24, FS);
    B.items.forEach((it, i) => { const ls = wrap(it.t, cw - 24, FS * 0.9), gs = wrap(it.from, cw - 24, FS * 0.86); hs.push(FS * 1.3 + kOf(it).length * FS * 1.25 + ls.length * FS * 1.22 + gs.length * FS * 1.1 + FS * 0.86); });
    const rowH = []; for (let i = 0; i < B.items.length; i += cols) rowH.push(Math.max(...hs.slice(i, i + cols)));
    B.items.forEach((it, i) => { const r = Math.floor(i / cols), c = i % cols, x = pad + c * (cw + gap), yy = y + rowH.slice(0, r).reduce((a, b) => a + b + gap, 0), h = rowH[r];
      const ls = wrap(it.t, cw - 24, FS * 0.9), gs = wrap(it.from, cw - 24, FS * 0.86), ks = kOf(it);
      s.push(`<g class="n4" data-goto="${it.go}" data-n="${it.n}" data-home="${it.home ? 1 : 0}"><rect class="card${it.home ? " n4-home" : ""}" x="${n1(x)}" y="${n1(yy)}" width="${n1(cw)}" height="${n1(h)}" rx="6"/>`, lines(x + 12, yy + FS * 1.3, ks, { c: "h", w: 700, lh: FS * 1.25 }), lines(x + 12, yy + FS * 1.3 + ks.length * FS * 1.25, ls, { fs: FS * 0.9, lh: FS * 1.22 }), lines(x + 12, yy + FS * 1.3 + ks.length * FS * 1.25 + ls.length * FS * 1.22 + FS * 0.2, gs, { c: "muted link", fs: FS * 0.86, lh: FS * 1.1 }), `</g>`); });
    y += rowH.reduce((a, b) => a + b + gap, 0);
    const nl = wrap(B.note, W - 2 * pad, FS * 0.86); s.push(lines(pad, y + FS * 0.4, nl, { c: "muted", fs: FS * 0.86, lh: FS * 1.2 })); y += nl.length * FS * 1.2 + FS * 2.4;
    return { svg: s.join("") + `<rect class="next-band" x="4" y="4" width="${n1(W - 8)}" height="${n1(y - 8)}" rx="8"/>`, vb: [0, 0, W, n1(Math.max(ph ? 0 : 380, y + 4))] };
  }
  const thinkMedians = () => (x, y, w) => {   // state 14: the thinking medians counted from the jsonl (reasoning_tokens · Bbp · n 20 each), one scale
    const items = [["Sonnet 5.5 · API high", "b5bp.Bbp.sonnet-5-5"], ["Opus 5.5 · API high", "b5bp.Bbp.opus-5-5"], ["Fable 5.1 · API high", "b5bp.Bbp.fable-5-1"], [L("Argon · thinking 既定", "Argon · thinking default"), "arg5d.Bbp"], ["Argon · thinking high", "arg5.Bbp"]];
    const mx = Math.max(...items.map(([, id]) => C(id).reasoning_med)), s = [], lab = narrow() ? w * 0.42 : Math.min(200, w * 0.4), bw = w - lab - 90;
    const tl = wrap(L("thinking の中央値(Bbp · reasoning_tokens · jsonl から数えた · 同じ目盛り)", "thinking median (Bbp · reasoning_tokens · counted from the jsonl · one scale)"), w, FS * 0.95); s.push(lines(x, y + FS, tl, { c: "h", w: 700, fs: FS * 0.95, lh: FS * 1.25 }));
    let yy = y + FS * 0.6 + tl.length * FS * 1.25;
    items.forEach(([k, id]) => { const v = C(id).reasoning_med; s.push(`<g class="tm" data-cell="${esc(id)}" data-med="${v}">`, T(x, yy + FS * 0.85, k, { fs: FS * 0.86 }), `<rect class="tbar ${id.startsWith("arg5.") ? "blue" : "lo"}" x="${n1(x + lab)}" y="${n1(yy)}" width="${n1(Math.max(2, (bw * v) / mx))}" height="${n1(FS * 0.85)}"/>`, T(x + lab + (bw * v) / mx + 6, yy + FS * 0.86, v.toLocaleString("en"), { fs: FS * 0.86 }), `</g>`); yy += FS * 1.45; });
    const nt = wrap(FIGURE.thinkNote(), w, FS * 0.86); s.push(lines(x, yy + FS * 0.7, nt, { c: "muted", fs: FS * 0.86, lh: FS * 1.18 })); yy += nt.length * FS * 1.18 + FS * 0.4;
    return { svg: s.join(""), h: yy - y };
  };

  // ---- the table of states: chapter + mode + camera [az, el, zoom, px] + what to draw
  // the phone: the text keeps its size in px only if the viewBox is narrow, so the geometry is shrunk (zoom × f) around the centre and the canvas is cropped to w × h there
  const ISO = (S, A, side, fn, c, vb) => { const ph = narrow(), f = ph ? vb.phone.f : 1, Pj = proj(A("az"), A("el"), A("zoom") * f, ph ? 0 : A("px"), c); return { svg: fn(S, A, Pj), vb: ph ? [VW / 2 - vb.phone.w / 2, VH / 2 + 14 - vb.phone.h / 2 + (vb.phone.dy || 0), vb.phone.w, vb.phone.h] : vb.desk }; };
  // v2.2: the two board states keep the cone's top inside the frame: the camera centre is 22 units above the board (c), so the board sits lower in the frame, and the phone's crop is 36 units higher (dy). The same with the overlay on or off (the board does not jump on the toggle).
  const BOARD_C = [0, 0, 22], BOARD_VB = { desk: [0, 0, VW, VH], phone: { f: 0.95, w: 760, h: 600, dy: -36 } };
  const states = [
    { chapter: "A", mode: "iso", board: true, cam: [62, 30, 0.98, -150], t: 0, fn: (S, A, Pj) => drawBoard(S, A, Pj, ["E", "J", "K", "P_y"]) + emptyBoard(), c: BOARD_C, vb: BOARD_VB, keys: ["cfocus", "cpt"] },
    { chapter: "A", mode: "plane", t: 0, plane: () => pair({ sid: "A1L", card: "prf3", sub: L("P5 = 問い + PROOF(近道は開いている)· claude -p · max", "P5 = question + PROOF (the short cut is open) · claude -p · max"), reason: [SC("A1L").phrases[0]], reasonTone: "floor", mark: L("焦点・準線の道", "the focus–directrix road") },
                                                              { sid: "A1R", card: "prf3", sub: L("P5B = 問い + PROOF + BLOCK(近道を塞ぐ)· claude -p · max", "P5B = question + PROOF + BLOCK (short cut blocked) · claude -p · max"), reason: SC("A1R").phrases, reasonTone: "apex", mark: L("頂点の比例中項 → 式(式は PROOF が求めた)", "vertex mean proportional → equation (the equation was asked by PROOF)") }), keys: ["bfloor", "bapex"] },
    { chapter: "B", mode: "iso", cam: [52, 32, 0.86, 0], t: 0, fn: stations, c: [0, 0, 30], vb: { desk: [0, 0, VW, VH], phone: { f: 0.62, w: 760, h: 560 } }, keys: ["sfloor", "sapex", "sdesc"] },
    { chapter: "B", mode: "plane", t: 0, plane: mapLayout, keys: ["A", "R", "F", "N", "C", "S", "M", "api", "cc", "loc"] },
    { chapter: "B", mode: "plane", t: 0, plane: roadLayout, keys: ["rda", "rdw", "rdx"] },
    { chapter: "C", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("問いだけ(essay4 A · API · high)", "question only (essay4 A · API · high)") }, { id: "essay4.A.opus-5-5" }, { id: "essay4.A.fable-5-1" }, { id: "essay4.A.sonnet-5-5" }, { id: "essay4.A.haiku-5-5" }, { h: L("陽性統制 K(関係を渡す・essay4 · API · high · n 20)", "positive control K (the relation given · essay4 · API · high · n 20)") }, { id: "essay4.K.opus-5-5" }, { id: "essay4.K.fable-5-1" }, { id: "essay4.K.sonnet-5-5" }, { id: "essay4.K.haiku-5-5" }]),
                                                              stack(col([{ h: L("問いだけ(mnw1 none/Q1 · API · xhigh)", "question only (mnw1 none/Q1 · API · xhigh)") }, { id: "mnw1.none/Q1.opus" }, { id: "mnw1.none/Q1.fable" }, { h: L("陽性統制 K(別の札: mnw1 · API · xhigh · n 10)", "positive control K (another card: mnw1 · API · xhigh · n 10)") }, { id: "mnw1.K.opus" }, { id: "mnw1.K.fable" }]), brd("C0", { card: "mnw1", ansTone: "floor", reasonEmpty: L("(この場面では答えの欄だけを写す)", "(only the answer field is copied here)") }))), keys: ["A", "R", "F", "N", "api"] },
    { chapter: "C", mode: "plane", t: 0, plane: () => twoCols(stack(sumTable(), txt([L("neq1(エッセイ + 「等長だけでは足りない」の注釈)の判定は NONE(RESULT neq1 の題)。", "neq1 (essay + a note 'equal length alone is not enough'): verdict NONE (the title of RESULT neq1).")], { c: "muted", k: 0.92 })),
                                                              col([{ h: L("名・本文・役の対応(Q1 · claude -p / API · xhigh)", "name · text · roles (Q1 · claude -p / API · xhigh)") }, { id: "neq3.L-name.opus", label: "Opus 5.5 · L-name" }, { id: "neq3.L-text.opus", label: "Opus 5.5 · L-text" }, { id: "neq2f.L-name.fable", label: "Fable 5.1 · L-name" }, { id: "neq2f.L-text.fable", label: "Fable 5.1 · L-text" }, { id: "mnw1.conf/Q1.opus" }, { id: "mnw1.conf/Q1.fable" }])), keys: ["A", "R", "F", "N", "api", "cc"] },
    { chapter: "D", mode: "iso", board: true, cam: [62, 30, 0.98, -150], t: 0, fn: (S, A, Pj) => drawBoard(S, A, Pj, ["F", "V", "P_x", "P_y"]) + lineCard(), c: BOARD_C, vb: BOARD_VB, keys: ["cfocus2", "cpt"] },
    { chapter: "D", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("Q1 = 凍結の問い {E, J, K, P_y}", "Q1 = the frozen question {E, J, K, P_y}") }, { id: "neq3.A.opus", label: "Opus 5.5 · A (Q1)" }, { id: "neq2f.A.fable", label: "Fable 5.1 · A (Q1)" }, { h: L("Q1 の陽性統制 K(関係を渡す・n 10)", "positive control K on Q1 (the relation given · n 10)") }, { id: "neq3.K.opus", label: "Opus 5.5 · K (Q1)" }, { id: "neq2f.K.fable", label: "Fable 5.1 · K (Q1)" }]),
                                                              col([{ h: L("Q2 = 集合だけ {F, V, P_x, P_y}", "Q2 = only the set replaced {F, V, P_x, P_y}") }, { id: "neq3.A/Q2.opus", label: "Opus 5.5 · A/Q2" }, { id: "neq3.A/Q2.fable", label: "Fable 5.1 · A/Q2" }, { note: FIGURE.trajNote(["neq3.A/Q2.opus", "neq3.A/Q2.fable"]) }])), keys: ["A", "R", "F", "N", "cc"] },
    { chapter: "D", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("Q2 + 補助定理 XIV の名 / 本文", "Q2 + the name / the text of Lemma XIV") }, { id: "neq3.L-name/Q2.opus" }, { id: "neq3.L-text/Q2.opus" }, { id: "neq3.L-name/Q2.fable" }, { id: "neq3.L-text/Q2.fable" }, { note: FIGURE.trajNote(["neq3.L-name/Q2.opus", "neq3.L-text/Q2.opus", "neq3.L-name/Q2.fable", "neq3.L-text/Q2.fable"]) }]),
                                                              col([{ h: L("比べ: 何も足さない Q2 と 陽性統制 K/Q2", "compare: Q2 with nothing added, and the positive control K/Q2") }, { id: "neq3.A/Q2.opus" }, { id: "neq3.K/Q2.opus" }, { id: "neq3.K/Q2.fable" }, { note: FIGURE.trajNote(["neq3.K/Q2.opus", "neq3.K/Q2.fable"]) }])), keys: ["A", "R", "F", "N", "cc"] },
    { chapter: "E", mode: "iso", cam: [74, 24, 0.9, 0], t: 0, fn: ladder, c: [240, 190, 70], vb: { desk: [0, 0, VW, VH], phone: { f: 0.56, w: 820, h: 660 } }, keys: ["lans", "lwhole", "cc"] },
    { chapter: "E", mode: "plane", t: 0, plane: () => pair({ sid: "E1L", card: "neq6", sub: "A/Q2 · claude -p · medium", ansTone: "locus", reasonEmpty: L("(この場面では答えの欄を比べる)", "(the answer fields are compared here)") },
                                                              { sid: "E1R", card: "neq6", sub: "A/Q2 · claude -p · max", ansTone: "apex", reasonEmpty: L("(この場面では答えの欄を比べる)", "(the answer fields are compared here)") }, thinkBar("E1L", "E1R")), keys: ["blocus", "bapex"] },
    { chapter: "F", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("問い + β′(b5bp Bbp · API · high)", "question + β′ (b5bp Bbp · API · high)") }, { id: "b5bp.Bbp.opus-5-5" }, { id: "b5bp.Bbp.sonnet-5-5" }, { id: "b5bp.Bbp.fable-5-1" }]),
                                                              sent(L("β′(足した一文・逐語)", "β′ (the added sentence, verbatim)"), "beta", "b5bp_moy5_blocking_beta_prime_20261014.py l.19–21 (read as text)")), keys: ["A", "R", "F", "N", "api"] },
    { chapter: "F", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("β′ だけ · 経路 × effort(四つは別の札・線で結ばない)", "β′ only · path × effort (four separate cards; never joined)") }, { id: "b5bp.Bbp.opus-5-5", label: "Opus · API · high (b5bp)" }, { id: "rte1.api_max.opus", label: "Opus · API · max (rte1)" }, { id: "rte1.cc_high.opus", label: "Opus · claude -p · high (rte1)" }, { id: "moy5c.opus", label: "Opus · claude -p · max (moy5c)" }]),
                                                              col([{ h: " " }, { id: "b5bp.Bbp.fable-5-1", label: "Fable · API · high (b5bp)" }, { id: "rte1.api_max.fable", label: "Fable · API · max (rte1)" }, { id: "rte1.cc_high.fable", label: "Fable · claude -p · high (rte1)" }, { id: "moy5c.fable", label: "Fable · claude -p · max (moy5c)" }])), keys: ["A", "R", "F", "N", "api", "cc"] },
    { chapter: "F", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("Gemini 4 Argon · thinking high(arg5)", "Gemini 4 Argon · thinking high (arg5)") }, { id: "arg5.A", label: "Argon · A" }, { id: "arg5.Bbp", label: "Argon · Bbp" }, { id: "arg5.K", label: "Argon · K" }, { h: L("Argon · thinking 既定(arg5d)", "Argon · thinking default (arg5d)") }, { id: "arg5d.Bbp", label: "Argon · Bbp" }, { id: "arg5d.K", label: "Argon · K" }]),
                                                              stack(thinkMedians(), txt(FIGURE.argonNote(), { k: 0.9 }))), keys: ["A", "R", "F", "N", "api"] },
    { chapter: "G", mode: "plane", t: 0, plane: () => twoCols(stack(col([{ h: L("問い + PROOF(prf1 P5 · claude -p · max)", "question + PROOF (prf1 P5 · claude -p · max)") }, { id: "prf1.P5.opus", hl: [0] }, { id: "prf1.P5.fable" }]), sent(L("PROOF(足した一文・逐語)", "PROOF (the added sentence, verbatim)"), "proof", "PREREG prf1 l.25")),
                                                              brd("G0", { card: "prf1", ansTone: "floor", reason: SC("G0").phrases, reasonTone: "floor", mark: L("焦点・準線 → 式(式は PROOF が求めた)", "focus–directrix → equation (asked by PROOF)") })), keys: ["E", "C", "L", "N", "cc", "hl"] },
    { chapter: "G", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("prf1 P5 · Opus(r2 = 格子に入った稀な行)", "prf1 P5 · Opus (r2 = the rare row that entered the lattice)") }, { id: "prf1.P5.opus", hl: [2] }, { note: L("CHAIN = 比例中項・相似の格子を束ねて式まで。LAT-only = 格子は書くが束ねない。", "CHAIN = the mean-proportional / similarity lattice bundled up to the equation. LAT-only = the lattice written but not bundled.") }]),
                                                              brd("G1", { card: "prf1", ansTone: "floor", reason: SC("G1").phrases, reasonTone: "apex", mark: "route5 = CHAIN" }), { split: 0.46 }), keys: ["E", "C", "L", "N", "cc", "hl"] },
    { chapter: "G", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("問い + PROOF + 比例中項を渡す(prf1 P5K)", "question + PROOF + the mean proportional given (prf1 P5K)") }, { id: "prf1.P5K.opus" }, { id: "prf1.P5K.fable" }, { h: L("比べ: 渡さない P5", "compare: P5, not given") }, { id: "prf1.P5.opus" }, { id: "prf1.P5.fable" }]),
                                                              stack(txt([FIGURE.p5kNote()], { k: 1 }), sent(L("K の hint(P5K が渡した文・逐語)", "the K hint (the sentence P5K gives, verbatim)"), "khint", "SOURCE 10-14 · moy-5 の陽性統制 K"))), keys: ["E", "C", "L", "N", "cc"] },
    { chapter: "G", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("prf3(確かめ)· claude -p · max", "prf3 (confirmation) · claude -p · max") }, { id: "prf3.P5.opus", label: L("Opus 5.5 · P5(開いている)", "Opus 5.5 · P5 (open)") }, { id: "prf3.P5B.opus", label: L("Opus 5.5 · P5B(塞ぐ)", "Opus 5.5 · P5B (blocked)") }, { id: "prf3.P5.fable", label: L("Fable 5.1 · P5(開いている)", "Fable 5.1 · P5 (open)") }, { id: "prf3.P5B.fable", label: L("Fable 5.1 · P5B(塞ぐ)", "Fable 5.1 · P5B (blocked)") }]),
                                                              sent(L("BLOCK(足した一文・逐語)", "BLOCK (the added sentence, verbatim)"), "block", "PREREG prf2 l.21"), { split: 0.56 }), keys: ["S", "D", "M", "N", "cc"] },
    { chapter: "H", mode: "plane", t: 0, plane: () => pair({ sid: "H0L", card: "mnw1", sub: "none/Q1f · API · xhigh", ansTone: "degen", reasonEmpty: L("(この場面では答えの欄を比べる)", "(the answer fields are compared here)") },
                                                              { sid: "H0R", card: "mnw1", sub: "none/Q1f · API · xhigh", ansTone: "apex", reasonEmpty: L("(この場面では答えの欄を比べる)", "(the answer fields are compared here)") }, (x, y, w) => twoColsInner(x, y, w, col([{ id: "mnw1.none/Q1f.opus" }, { id: "mnw1.none/Q1f.fable" }]), sent(L("FORM(問いの後に足した一文・逐語)", "FORM (the sentence added after the question, verbatim)"), "form", "PREREG mnw1 l.34"))), keys: ["bdegen", "bapex", "A", "R", "F"] },
    { chapter: "H", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("役の対応だけ(conf/Q1)", "roles only (conf/Q1)") }, { id: "mnw1.conf/Q1.opus" }, { id: "mnw1.conf/Q1.fable" }, { h: L("役の対応 + 比例の形(conf/Q1f)", "roles + the form of a proportion (conf/Q1f)") }, { id: "mnw1.conf/Q1f.opus" }, { id: "mnw1.conf/Q1f.fable" }]),
                                                              stack(sent(L("CONF(問いの前・逐語)", "CONF (before the question, verbatim)"), "conf", "PREREG mnw1 l.35"), brd("H1", { card: "mnw1", ansTone: "apex", reasonEmpty: L("(答えの欄だけを写す)", "(only the answer field is copied)"), maxAns: 5 }))), keys: ["A", "R", "F", "N", "api"] },
    { chapter: "H", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("Menaechmus の説明だけ(cone/Q1)", "the Menaechmus explanation only (cone/Q1)") }, { id: "mnw1.cone/Q1.opus" }, { id: "mnw1.cone/Q1.fable", marks: FIGURE.vertexMarks("mnw1.cone/Q1.fable") }, { h: L("説明 + 比例の形(cone/Q1f)", "explanation + the form (cone/Q1f)") }, { id: "mnw1.cone/Q1f.opus" }, { id: "mnw1.cone/Q1f.fable" }]),
                                                              stack(txt([L("CONE(問いの前・926 字)の要旨(PREREG mnw1 l.36): ", "CONE (before the question, 926 chars), its gist in PREREG mnw1 l.36 (Japanese): ") + DATA.sentences.cone_gist_ja], { c: "muted", k: 0.9 }), brd("H2", { card: "mnw1", ansTone: "floor", reason: SC("H2").phrases, reasonTone: "desc", mark: L("頂点の形(symptoma)· 式を求めていない腕", "vertex form (symptoma) · an arm that did not ask for an equation") }))), keys: ["A", "R", "F", "N", "vmark", "api"] },
    { chapter: "I", mode: "plane", t: 0, plane: () => twoCols(col([{ h: L("OLMo-3 32B · none/Q1(問い + 形の一文なし)· MLX local", "OLMo-3 32B · none/Q1 · MLX local") }, { id: "olm1.natural" }, { id: "olm1.think" }, { id: "olm3.think" }, { h: L("陽性統制 K(関係を渡す)· 同じ札", "positive control K (the relation given) · same cards") }, { id: "olm1.natural.K" }, { id: "olm1.think.K" }, { id: "olm3.K" }]),
                                                              txt(FIGURE.olmNote(), { k: 0.95 }), { split: 0.55 }), keys: ["A", "R", "F", "N", "Z", "loc"] },
    { chapter: "J", mode: "plane", t: 0, plane: flowLayout, keys: ["pmv", "pmd", "pmx", "pmg", "after"] },
    { chapter: "J", mode: "plane", t: 0, plane: () => postLayout(["a"]), keys: ["pmv", "pmg", "fline", "pline", "after"] },
    { chapter: "J", mode: "plane", t: 0, plane: () => postLayout(["b"]), keys: ["pmv", "pmd", "pmx", "pmg", "fline", "after"] },
    { chapter: "J", mode: "plane", t: 0, plane: () => postLayout(["c", "d"]), keys: ["pmv", "pmg", "pmd", "fline", "A", "N", "after"] },
    { chapter: "K", mode: "plane", t: 0, plane: n4Layout, keys: ["next", "home"] },
    { chapter: "L", mode: "plane", t: 0, plane: returnLayout, keys: ["A", "R", "N"] },
    { chapter: "L", mode: "ledger", t: 0, ledger: "items", keys: [] },
    { chapter: "L", mode: "ledger", t: 0, ledger: "after", keys: ["after"] },
  ];
  function emptyBoard() { const ph = narrow(); if (ph) return ""; const b = board(860, 60, 290, null, { reasonTone: "empty" }); return `<g class="ansboard">${b.svg}${T(860, 60 + b.h + FS * 1.6, L("JSON の答えの欄と理由の欄 = 空", "the JSON answer and reason fields = empty"), { c: "muted", fs: FS * 0.9 })}</g>`; }
  function lineCard() {
    if (narrow()) return "";
    const x = 820, w = 340, s = [];
    const c1 = sentenceCard(x, 40, w, L("Q1(凍結の問いの一行)", "Q1 (one line of the frozen question)"), DATA.sentences.focus_q1, "SOURCE 10-14 l.56–84 · md5 ee39ba02");
    const c2 = sentenceCard(x, 60 + c1.h, w, L("Q2(集合だけ替える)", "Q2 (only the set replaced)"), DATA.sentences.focus_q2, "PREREG neq3 l.22");
    s.push(c1.svg, c2.svg, lines(x, 90 + c1.h + c2.h, wrap(L("座標・作図・前提・答えの型は同じ", "coordinates, construction, premises, answer form: unchanged"), w, FS * 0.9), { c: "muted", fs: FS * 0.9 }));
    return s.join("");
  }
  return {
    states,
    keysOf: (S) => (states[S.state].board ? [...states[S.state].keys, "cline", ...(S.cone !== false ? [narrow() ? "cplane_ph" : "cplane", "ccone", "ccut"] : [])] : states[S.state].keys || []),   // v2.3: + the cutting plane's key line while the overlay is on, put first so that the last key line stays short (en video: a long last line runs under the plate's corner readout); the phone's line also names F, V and the directrix, which the phone does not draw   // v2.2: the lines' names, and the overlay's keys while it is on
    isBoard: (S) => !!states[S.state].board,
    coneCheck, CONE, planeCheck, cutPlane, packPlane: () => DATA.construction.plane,   // v2.3: the page check compares its planeCheck with the pack (route 1)
    tRange: (S) => ([0, 7].includes(S.state) ? [-6, 6] : [0, 0]),
    focus: () => 0,
    mapCount: () => { const ids = MAP().flatMap((g) => g[2]); return { arms: ids.length, rows: ids.reduce((a, id) => a + C(id).n, 0) }; },
    returnRows: () => I18N[LANG].returnRows(),
    argonNote: () => I18N[LANG].argonNote(),
    olmNote: () => I18N[LANG].olmNote(),
    trajNote: (ids) => I18N[LANG].trajNote(ids),
    cueCount: () => CUES().length,
    controlNote: () => I18N[LANG].controlNote(),
    thinkNote: () => I18N[LANG].thinkNote(),
    p5kNote: () => I18N[LANG].p5kNote(),
    postText: (p) => I18N[LANG].post[p.id](p.v),
    flowText: () => I18N[LANG].flow(),
    n4Text: () => I18N[LANG].n4(),
    afterLabel: () => I18N[LANG].afterLabel,
    vertexMarks: (id) => (C(id).marks || []).map((m) => (m.includes("V") ? "vmk" : "")),
    construct, PxAt,
    ctx(S) { return { S, C, SC, D: DATA }; },
    draw(S, A, el, root) {
      LANG = S.lang; VIDEO = root.dataset.video === "1";
      const st = states[S.state]; FS = fsOf(root, st.mode);
      root.dataset.mode = st.mode; root.dataset.ledger = st.ledger || "";   // the ledger of the cards after 10-28 carries the "added 11-06" frame (figure.css)
      const wrapT = root.querySelector(".fig-tval-wrap"); if (wrapT) wrapT.style.display = [0, 7].includes(S.state) ? "" : "none";
      const coneB = root.querySelector(".sh-cone"); if (coneB) coneB.style.display = st.board ? "" : "none";   // v2.2: the overlay's toggle is shown on the board states only (like the P_x slider)
      if (st.mode === "ledger") { el.svg.setAttribute("viewBox", `0 0 ${VW} ${VH}`); el.pic.innerHTML = ""; el.ledger.innerHTML = ledgerHtml(S); return; }
      el.ledger.innerHTML = "";
      const r = st.mode === "iso" ? ISO(S, A, root.dataset.video === "1", st.fn, st.c, st.vb) : st.plane();
      el.svg.setAttribute("viewBox", r.vb.slice(0, 4).join(" "));
      el.pic.innerHTML = r.svg;
    },
  };
  function ledgerHtml(S) {
    const T2 = I18N[S.lang].ledger, items = states[S.state].ledger === "after" ? T2.after() : T2.items();
    return ["L1", "L3", "x"].map((lv, i) => `<section><h3>${esc(T2.cols[i])}</h3>${items.filter((x) => x.lv === lv).map((x) => `<article><b>${T2.tag[lv]}</b> ${esc(x.t)}<span class="src">${esc(x.src)}</span></article>`).join("")}</section>`).join("");
  }
})();
