// art.mjs — the static isometric art, built ONCE at build time with the Anatomy kit (MIT, Copyright (c) 2026 Ryan): its camera (iso / fitProjection), its solids (slabOf / cylinder / extrude),
// its four-tone shading and its SVG renderers (solidSvg / lineSvg). Two objects:
//   board(geo)  = the moy-2 configuration drawn to its coordinates on a drafting board (two circles, the inner tangent l1, Tc / Th / O3, the line O1O2, the reflections of Tc and Th across O1O2)
//   rack(arms)  = a specimen rack: one tray per arm, one block per row (3 batches × 20 jobs). Block height = log10(T) (T = tokens written, cap 12,288 = a lid), colour = the class of the conjecture,
//                 a disc on top = the proof field asserts the line symmetry (v3), a ring = only v6 reads it, a dashed square = the outer-tangent marker (v3), a collar = the body rejects the reflection (REJ6).
// Every number comes from the pack (generated/pack.json); nothing is typed here except sizes of the drawing.
export function makeArt(K, PACK) {
  const R = (v) => Math.round(v * 10) / 10;
  // ---------------------------------------------------------------- the board
  function board() {
    const g = PACK.geo, S = 8.2, cx = 2.1, cy = -4.3;
    const W = ([x, y]) => [(x - cx) * S, -(y - cy) * S];                 // geometry (y up) -> world floor (no mirror under the kit's camera)
    const BX = { x: -13.6 * S, y: -9.4 * S, w: 27.2 * S, d: 18.6 * S, r: 6 }, TOP = 7;
    const pts = [[BX.x, BX.y, 0], [BX.x + BX.w, BX.y, 0], [BX.x, BX.y + BX.d, 0], [BX.x + BX.w, BX.y + BX.d, 0], [BX.x, BX.y, TOP + 30], [BX.x + BX.w, BX.y + BX.d, TOP + 30]];
    const P = K.fitProjection(pts, 760, 560, { pad: 26, azimuth: 52, elevation: 36 });
    const on = (p, z = TOP) => K.iso([...W(p), z], P);
    const out = [];
    // feet, board, a groove and corner screws, a label plate
    for (const [fx, fy] of [[BX.x + 14, BX.y + 14], [BX.x + BX.w - 14, BX.y + 14], [BX.x + 14, BX.y + BX.d - 14], [BX.x + BX.w - 14, BX.y + BX.d - 14]]) out.push(K.solidSvg(K.cylinder(fx, fy, 6, -6, 6, P, 20), { tone: "mid" }));
    out.push(K.solidSvg(K.slabOf(BX, 0, TOP, P, 6, 0.8), { tone: "mid", halo: true }));
    out.push(K.lineSvg(K.planOutline(K.insetPlan(BX, 5), TOP, P, 6), { tone: "faint" }));
    for (const [sx, sy] of K.corners(BX, 9)) out.push(K.solidSvg(K.cylinder(sx, sy, 1.6, TOP, 0.4, P, 12), { tone: "lo" }));
    const plate = { x: BX.x + BX.w - 78, y: BX.y + BX.d - 22, w: 66, d: 13, r: 1.5 };
    out.push(K.solidSvg(K.slabOf(plate, TOP, 0.8, P, 4, 0.3), { tone: "lo" }));
    for (let i = 0; i < 3; i++) out.push(K.lineSvg(K.lineOnTop([plate.x + 6, plate.y + 3.5 + i * 3], [plate.x + plate.w - 6 - i * 12, plate.y + 3.5 + i * 3], TOP + 0.8, P), { tone: "faint", free: true }));
    // a ruler strip along the near edge (1 geometry unit per tick)
    const rul = { x: BX.x + 12, y: BX.y + BX.d - 9, w: 20 * S, d: 5, r: 0.6 };
    out.push(K.solidSvg(K.slabOf(rul, TOP, 0.6, P, 2), { tone: "lo" }));
    for (let i = 0; i <= 20; i++) out.push(K.lineSvg(K.segment([rul.x + i * S, rul.y, TOP + 0.6], [rul.x + i * S, rul.y + (i % 5 ? 1.8 : 3.4), TOP + 0.6], P), { tone: i % 5 ? "lo" : "mid" }));
    // the drawing on the board's top: circles, the line O1O2 (extended), the tangent l1 (extended), radii to the contact points
    // v1.3 H4: every line drawn on the board is also kept as a screen polyline (lines) so the tags can be placed clear of it (figure.js placeBoard) and the check can test it
    const lines = [], keep = (pts) => { lines.push(pts.map(([x, y]) => [R(x), R(y)])); return pts; };
    const circ = (c, r, cls) => `<path class="bd-circ ${cls}" d="${K.pathOf(keep(Array.from({ length: 97 }, (_, i) => { const a = (i / 96) * Math.PI * 2; return on([c[0] + r * Math.cos(a), c[1] + r * Math.sin(a)]); })))}"/>`;
    const lineThrough = (a, b, t0, t1) => [[a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0], [a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1]];
    const seg = (a, b, cls) => `<path class="${cls}" d="${K.pathOf(keep([on(a), on(b)]))}"/>`;
    out.push(circ(g.O2, g.r2, "c"), circ(g.O1, g.r1, "h1"));
    const [o12a, o12b] = lineThrough(g.O1, g.O2, -0.22, 1.22); out.push(seg(o12a, o12b, "bd-line o12"));
    const [l1a, l1b] = lineThrough(g.Tc, g.Th, -0.75, 1.75); out.push(seg(l1a, l1b, "bd-line l1"));
    out.push(seg(g.O2, g.Tc, "bd-thin"), seg(g.O1, g.Th, "bd-thin"));
    // the apex: O3 to Tc and to Th (equal: computed by the pack from these coordinates)
    out.push(seg(g.O3, g.Tc, "bd-eq"), seg(g.O3, g.Th, "bd-eq"));
    // the reflections across O1O2 (computed by the pack with the formula of the Tool section; S1's own number is within 0.01 of it)
    out.push(seg(g.Th, g.Th_r, "bd-refl"), seg(g.Tc, g.Tc_r, "bd-refl"));
    const pin = (p, r, tone, lit) => K.solidSvg(K.cylinder(...W(p), r, TOP, 1.6, P, 14), { tone, lit });
    const ring = (p, r, cls) => `<path class="${cls}" d="${K.pathOf(keep(Array.from({ length: 25 }, (_, i) => { const a = (i / 24) * Math.PI * 2; return K.iso([W(p)[0] + r * Math.cos(a), W(p)[1] + r * Math.sin(a), TOP + 0.3], P); })))}"/>`;
    out.push(pin(g.O1, 1.4, "mid"), pin(g.O2, 1.4, "mid"));
    out.push(ring(g.Th_r, 3.2, "bd-ghost"), ring(g.Tc_r, 3.2, "bd-ghost"), ring(g.mid_TcTh, 2.6, "bd-mid"));
    out.push(pin(g.Tc, 2.0, "hi", true), pin(g.Th, 2.0, "hi", true), pin(g.O3, 2.0, "hi"));
    const tagAt = (id, p, z = TOP + 2) => ({ id, xy: K.iso([...W(p), z], P).map(R) });
    const tags = [tagAt("O1", g.O1), tagAt("O2", g.O2), tagAt("O3", g.O3), tagAt("Tc", g.Tc), tagAt("Th", g.Th), tagAt("Th_r", g.Th_r), tagAt("Tc_r", g.Tc_r), tagAt("M", g.mid_TcTh),
      tagAt("l1", l1b), tagAt("o12", o12a), tagAt("c", [g.O2[0] - g.r2 * 0.72, g.O2[1] - g.r2 * 0.72]), tagAt("h1", [g.O1[0] + g.r1 * 0.8, g.O1[1] + g.r1 * 0.65]),
      tagAt("eqTc", [(g.O3[0] + g.Tc[0]) / 2, (g.O3[1] + g.Tc[1]) / 2]), tagAt("eqTh", [(g.O3[0] + g.Th[0]) / 2, (g.O3[1] + g.Th[1]) / 2]),
      tagAt("plate", [(plate.x + plate.w / 2) / S + cx, -(plate.y + plate.d / 2) / S + cy], TOP + 1), tagAt("ruler", [(rul.x + 10 * S) / S + cx, -(rul.y + 8) / S + cy], TOP + 1)];
    const pins = [g.O1, g.O2, g.Tc, g.Th, g.O3].map((p) => K.iso([...W(p), TOP + 1.6], P).map(R));
    return { svg: out.join(""), vb: [760, 560], tags, lines, pins };
  }
  // ---------------------------------------------------------------- the rack
  function rack() {
    const CELL = 10, BLK = 7.2, TRAY_W = 3 * CELL + 5, GAP = 11, DEPTH = 20 * CELL + 5, HMAX = 46, LOGMAX = Math.log10(12288), Z0 = 6;
    const hOf = (T) => Math.max(3, (HMAX * Math.log10(Math.max(10, T))) / LOGMAX);
    const XL = PACK.arms.length * TRAY_W + (PACK.arms.length - 1) * GAP;
    const base = { x: -26, y: -12, w: XL + 40, d: DEPTH + 40, r: 4 };
    const pts = [[base.x, base.y, -6], [base.x + base.w, base.y, -6], [base.x, base.y + base.d, -6], [base.x + base.w, base.y + base.d, -6], [base.x, base.y, Z0 + HMAX + 6], [base.x + base.w, base.y, Z0 + HMAX + 6]];
    const P = K.fitProjection(pts, 1180, 700, { pad: 24, headroom: 16, azimuth: 62, elevation: 36 });
    const out = [], hits = [], labels = [], ticks = [];
    for (const [fx, fy] of [[base.x + 12, base.y + 12], [base.x + base.w - 12, base.y + 12], [base.x + 12, base.y + base.d - 12], [base.x + base.w - 12, base.y + base.d - 12]]) out.push(K.solidSvg(K.cylinder(fx, fy, 5, -6, 6, P, 18), { tone: "mid" }));
    out.push(K.solidSvg(K.slabOf(base, 0, 4, P, 6, 0.8), { tone: "mid", halo: true }));
    out.push(K.lineSvg(K.planOutline(K.insetPlan(base, 4), 4, P, 6), { tone: "faint" }));
    for (const [sx, sy] of K.corners(base, 7)) out.push(K.solidSvg(K.cylinder(sx, sy, 1.3, 4, 0.4, P, 10), { tone: "lo" }));
    // the T ruler: a post at the back-left with a strip of ticks (log10 of T); the cap height = 12,288 tokens
    const post = { x: -20, y: -6, w: 5, d: 5, r: 0.8 };
    out.push(K.solidSvg(K.slabOf(post, 4, Z0 + HMAX + 2 - 4, P, 2, 0.4), { tone: "mid" }));
    for (const T of [10, 100, 1000, 10000, 12288]) { const z = Z0 + hOf(T); out.push(K.lineSvg(K.segment([post.x + post.w, post.y + post.d, z], [post.x + post.w + (T === 12288 ? 9 : 5), post.y + post.d, z], P), { tone: T === 12288 ? "hi" : "mid" })); const cs = [[post.x, post.y], [post.x + post.w, post.y], [post.x, post.y + post.d], [post.x + post.w, post.y + post.d]].map(([x, y]) => K.iso([x, y, z], P)), left = cs.reduce((m, c) => (c[0] < m[0] ? c : m));
      ticks.push({ T, xy: K.iso([post.x + post.w + 9, post.y + post.d, z], P).map(R), lxy: left.map(R) }); }   // v1.1 F6: lxy = the post's leftmost corner at that height (the label goes to its left, clear of the first tray)
    // trays, one per arm (front label plate with three rule lines)
    PACK.arms.forEach((arm, ai) => {
      const x0 = ai * (TRAY_W + GAP);
      const tray = { x: x0, y: 0, w: TRAY_W, d: DEPTH, r: 1.5 };
      out.push(K.solidSvg(K.slabOf(tray, 4, 2, P, 4, 0.5), { tone: "lo" }));
      out.push(K.lineSvg(K.planOutline(K.insetPlan(tray, 1.6), Z0, P, 4), { tone: "faint" }));
    });
    // the blocks: painter's order = column (x) first, then job (y): in a uniform grid every overlapping pair is separated along x or along y, so this order is a valid one (README)
    const cols = [];
    PACK.arms.forEach((arm, ai) => { for (let b = 0; b < 3; b++) cols.push([ai, b]); });
    for (const [ai, b] of cols) {
      const arm = PACK.arms[ai], x0 = ai * (TRAY_W + GAP) + 2.5 + b * CELL + (CELL - BLK) / 2;
      for (let j = 0; j < 20; j++) {
        const ri = arm.rows.findIndex((r) => r.b === b && r.j === j); if (ri < 0) throw new Error(`rack: ${arm.id} b${b}_j${j} missing`);
        const r = arm.rows[ri], y0 = 2.5 + j * CELL + (CELL - BLK) / 2, h = r.cap ? HMAX : hOf(r.T);
        const plan = { x: x0, y: y0, w: BLK, d: BLK, r: 0 };
        const f = ["rk", `cls-${r.cls}`, r.calc ? "f-calc" : "", r.rej ? "f-rej" : "", r.typ ? "f-typ" : "", r.ln3 ? "f-ln3" : "", r.ln6 && !r.ln3 ? "f-ln6" : "", r.out3 ? "f-out" : "", r.cap ? "f-cap" : "", r.tn ? "f-tn" : "", r.pf ? "f-pf" : "f-nopf"].filter(Boolean).join(" ");
        let inner = "";
        let body = K.solidSvg(K.slabOf(plan, Z0, h, P, 1), { tone: "hi" });
        if (r.rej) body += K.solidSvg(K.slabOf(K.insetPlan(plan, -0.7), Z0 + h * 0.42, 1.6, P, 1), { tone: "mid", className: "rk-collar" });
        if (r.cap) body += K.solidSvg(K.slabOf(K.insetPlan(plan, -0.9), Z0 + h, 1.1, P, 1), { tone: "mid", className: "rk-lid" });
        const zt = Z0 + h + (r.cap ? 1.1 : 0), c = [x0 + BLK / 2, y0 + BLK / 2];
        if (r.ln3) inner += `<path class="rk-ln3" d="${K.ring(c[0], c[1], 2.3, zt, P, 14)}"/>`;
        else if (r.ln6) inner += `<path class="rk-ln6" d="${K.ring(c[0], c[1], 2.3, zt, P, 14)}"/>`;
        if (r.out3) inner += `<path class="rk-out" d="${K.planOutline(K.insetPlan(plan, 1.1), zt, P, 1)}"/>`;
        out.push(`<g class="${f}" data-r="${arm.id}:${r.k}">${body}${inner}</g>`);
        const top = K.iso([c[0], c[1], zt], P), foot = K.iso([c[0], c[1], Z0], P);
        const cs = [];
        for (const zz of [Z0, zt + 0.4]) for (const [px, py] of [[x0 - 0.9, y0 - 0.9], [x0 + BLK + 0.9, y0 - 0.9], [x0 - 0.9, y0 + BLK + 0.9], [x0 + BLK + 0.9, y0 + BLK + 0.9]]) cs.push(K.iso([px, py, zz], P));
        hits.push([ai, ri, R(top[0]), R(top[1]), R(foot[1]), [R(Math.min(...cs.map((q) => q[0]))), R(Math.min(...cs.map((q) => q[1]))), R(Math.max(...cs.map((q) => q[0]))), R(Math.max(...cs.map((q) => q[1])))]]);   // v1.2 G4: [x0, y0, x1, y1]
      }
    }
    PACK.arms.forEach((arm, ai) => {
      const x0 = ai * (TRAY_W + GAP), plate = { x: x0 + 2, y: DEPTH + 4, w: TRAY_W - 4, d: 9, r: 1.2 };
      out.push(K.solidSvg(K.slabOf(plate, 4, 1.6, P, 3, 0.3), { tone: "mid", className: `rk-plate${arm.g1fail ? " g1fail" : ""}` }));
      for (let i = 0; i < 2; i++) out.push(K.lineSvg(K.lineOnTop([plate.x + 3, plate.y + 3 + i * 3], [plate.x + plate.w - 3 - i * 8, plate.y + 3 + i * 3], 5.6, P), { tone: "faint", free: true }));
      labels.push({ arm: arm.id, xy: K.iso([x0 + TRAY_W / 2, DEPTH + 16, 4], P).map(R), back: K.iso([x0 + TRAY_W / 2, -2, Z0 + HMAX + 4], P).map(R) });
    });
    const jx = [0, 19].map((j) => ({ j, xy: K.iso([-4, 2.5 + j * CELL + CELL / 2, 5], P).map(R) }));
    return { svg: out.join(""), vb: [1180, 700], hits, labels, ticks, jx, hmax: HMAX };
  }
  // ---------------------------------------------------------------- v1.2 G1: the scene's band (state 0, under the two rows): two rows S1 / S2 × three stages (body, first half · the reject sentence · the proof field),
  // aligned at the reject stage. The stages are NOT to scale (the token position inside the body is not in the inventory). The difference is told by SHAPE only: on the proof-field slab S1 carries
  // a filled disc (the v3 reader caught the line symmetry) and S2 an empty dotted ring (no line-symmetry words). The body slab carries the calc mark, the reject slab the reject strip (the rack's collar).
  function slips() {
    const SW = 100, SD = 20, SG = 16, ROWG = 26, H = 4;
    const rowY = [0, SD + ROWG], stX = [0, 1, 2].map((i) => i * (SW + SG));
    const base = { x: -18, y: -10, w: 3 * SW + 2 * SG + 36, d: 2 * SD + ROWG + 20, r: 3 };
    const pts = [[base.x, base.y, -3], [base.x + base.w, base.y, -3], [base.x, base.y + base.d, -3], [base.x + base.w, base.y + base.d, -3], [base.x, base.y, H + 14], [base.x + base.w, base.y + base.d, H + 14]];
    const P = K.fitProjection(pts, 1180, 250, { pad: 36, headroom: 22, azimuth: 80, elevation: 22 });
    const out = [], tags = [];
    out.push(K.solidSvg(K.slabOf(base, -3, 3, P, 6, 0.6), { tone: "mid", halo: true }));
    out.push(K.lineSvg(K.planOutline(K.insetPlan(base, 3), 0, P, 6), { tone: "faint" }));
    // the alignment line: the reject stage's left edge, across both rows (a guide on the base)
    out.push(K.lineSvg(K.segment([stX[1] - SG / 2, base.y + 4, 0.2], [stX[1] - SG / 2, base.y + base.d - 4, 0.2], P), { tone: "mid", dashed: true }));
    out.push(K.lineSvg(K.segment([stX[2] - SG / 2, base.y + 4, 0.2], [stX[2] - SG / 2, base.y + base.d - 4, 0.2], P), { tone: "mid", dashed: true }));
    ["S1", "S2"].forEach((sid, ri) => {
      const y0 = rowY[ri];
      stX.forEach((x0, si) => {
        const plan = { x: x0, y: y0, w: SW, d: SD, r: 1.6 };
        out.push(K.solidSvg(K.slabOf(plan, 0, H, P, 4, 0.5), { tone: si === 2 ? "hi" : "lo", className: `sl-slab sl-${sid}-${si}` }));
        const c = [x0 + SW / 2, y0 + SD / 2];
        if (si === 0) out.push(K.solidSvg(K.slabOf({ x: c[0] - 4, y: c[1] - 4, w: 8, d: 8, r: 0.6 }, H, 1.2, P, 2), { tone: "mid", className: "sl-calc" }));
        if (si === 1) out.push(K.solidSvg(K.slabOf({ x: x0 + 6, y: c[1] - 2.2, w: SW - 12, d: 4.4, r: 0.6 }, H, 1.2, P, 2), { tone: "mid", className: "sl-rej" }));
        if (si === 2) {
          const PR = 9, PH = 12;   // the mark: S1 = a solid lit pin (filled) · S2 = the same pin's outline, dotted and empty
          if (sid === "S1") out.push(K.solidSvg(K.cylinder(c[0], c[1], PR, H, PH, P, 28), { tone: "hi", lit: true, className: "sl-ln-yes" }));
          else { const ring = Array.from({ length: 48 }, (_, i) => [c[0] + PR * Math.cos((i / 48) * Math.PI * 2), c[1] + PR * Math.sin((i / 48) * Math.PI * 2)]), scr = ring.map((q) => K.iso([q[0], q[1], H], P)[0]);
            const lo = ring[scr.indexOf(Math.min(...scr))], hi = ring[scr.indexOf(Math.max(...scr))];
            out.push(`<path class="sl-ln-no" d="${K.ring(c[0], c[1], PR, H + 0.05, P, 40)}${K.ring(c[0], c[1], PR, H + PH, P, 40)}${K.segment([lo[0], lo[1], H], [lo[0], lo[1], H + PH], P)}${K.segment([hi[0], hi[1], H], [hi[0], hi[1], H + PH], P)}"/>`); }
        }
        const front = K.iso([x0 + SW / 2, y0 + SD, 0], P), top = K.iso([x0 + SW / 2, y0, H], P), left = K.iso([x0, y0 + SD / 2, H / 2], P);
        tags.push({ id: `${sid}-${si}`, front: front.map(R), top: K.iso([x0 + SW / 2, y0, si === 2 ? H + 12 : H], P).map(R), left: left.map(R), mark: K.iso([c[0], c[1], H + 2], P).map(R) });
      });
    });
    const vb = [1180, 250];
    return { svg: out.join(""), vb, tags };
  }
  return { board: board(), rack: rack(), slips: slips() };
}
