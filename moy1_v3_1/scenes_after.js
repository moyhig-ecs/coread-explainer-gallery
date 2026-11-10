// scenes_after.js — the scenes of the part that was ADDED after the 10-28 figure (v3): what the home struck after it (olm76 ... olm128), as one flow. Inlined right after scenes.js by build.mjs.
// Every number is read from DATA.after (generated/pack.json: pack_after.py, recounted by data.mjs); nothing is typed here except layout constants. The words are in i18n_after.js: I18N[lang].af.
// The part is told from the 10-28 part by its look: a hatched node on the rail, dashed outlines, the ribbon of figure.css (data-part="after"); grades are told by shape, never by a new hue.
(() => {
  const H = SCENES.__h, { begin, n1, esc, newScene, flush, box, camera, tagger, lines, estW } = H;
  const AF = () => DATA.after, TX = (lang) => I18N[lang].af;
  const f3 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3), f2 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(2), f1 = (v) => v.toFixed(1), f3u = (v) => v.toFixed(3);
  const pc = (a, b) => Math.round((a / b) * 100);
  const GKEY = { "判定": "j", "確かめた記述": "k", "記述": "d", "読まない(関門 ✗)": "n" };
  const chart = (cv) => `<rect class="chartbg" x="2" y="2" width="${cv.W - 4}" height="${cv.H - 4}" rx="6"/>`;
  const rect = (x, y, w, h, cls, rx = 0) => `<rect class="${cls}" x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(h)}" rx="${rx}"/>`;
  const ln = (x1, y1, x2, y2, cls) => `<path class="${cls}" d="M${n1(x1)} ${n1(y1)}L${n1(x2)} ${n1(y2)}"/>`;
  // the grade of a card told by SHAPE (no hue): solid square = 判定 · half-filled = 確かめた記述 · outline = 記述 · dashed with a cross = read nothing (a gate failed)
  const glyph = (x, y, r, grade) => {
    const k = GKEY[grade] || "d", w = 2 * r;
    if (k === "j") return rect(x, y, w, w, "gl j", 1.5);
    if (k === "k") return rect(x, y, w, w, "gl d", 1.5) + rect(x, y, r, w, "gl j half", 1.5);
    if (k === "n") return rect(x, y, w, w, "gl n", 1.5) + ln(x + 2, y + 2, x + w - 2, y + w - 2, "gl x") + ln(x + w - 2, y + 2, x + 2, y + w - 2, "gl x");
    return rect(x, y, w, w, "gl d", 1.5);
  };
  // ---- the rail: the six stations of the flow (the 10-28 figure, then what the home struck after it). The 10-28 node is solid grey; every later node is hatched with a dashed edge (= added later)
  function rail(cv, T, active, y, opt = {}) {
    const st = AF().stations, W = cv.W, nar = cv.narrow, fs = cv.fs, n = st.length, x0 = nar ? 44 : 60, x1 = W - (nar ? 44 : 60), dx = (x1 - x0) / (n - 1), sc = newScene(), tag = tagger(sc, cv), nw = nar ? 34 : 30;
    let s = "";
    for (let i = 0; i < n - 1; i++) s += ln(x0 + i * dx + nw / 2, y, x0 + (i + 1) * dx - nw / 2, y, i === 0 ? "af-rail dash" : "af-rail dash");
    st.forEach((q, i) => {
      const cx = x0 + i * dx, on = i === active, base = i === 0;
      s += `<rect class="af-node${base ? " base" : " later"}${on ? " on" : ""}" x="${n1(cx - nw / 2)}" y="${n1(y - nw / 2)}" width="${nw}" height="${nw}" rx="6"${base ? "" : ' fill="url(#moy1-hatch)"'}/>`;
      tag([cx, y + 0.4 * fs], String(i), "pt strong", 0, 0, "middle", { fixed: true });
      tag([cx, y + nw / 2 + fs * 1.15], nar ? T.railShort[i] : T.railLab[i], "pt " + (on ? "strong" : "muted"), 0, 0, "middle", { fixed: true });
      if (!nar) tag([cx, y - nw / 2 - fs * 0.5], q.date, "pt muted", 0, 0, "middle", { fixed: true });
    });
    if (opt.cap) tag([x0 - nw / 2, y - nw / 2 - fs * (nar ? 1.4 : 1.55)], opt.cap, "pt muted", 0, 0, "start", { fixed: true });
    return s + sc.tags.join("");
  }
  // a title that wraps to the canvas (the long sentence of a scene's head): draws it on as many lines as it needs and returns the extra height (px) beyond one line, so that the content starts lower
  const ttl = (tag, cv, text, x, y, o = {}) => {
    const fs = o.fs || cv.fs, anchor = o.anchor || "start", lh = fs * 1.34, room = o.maxW || (anchor === "middle" ? cv.W - 28 : cv.W - x - 14), ls = lines(text, room / 1.06, fs).slice(0, 4);
    ls.forEach((l, i) => tag([x, y + i * lh], l, "title", 0, 0, anchor, { fixed: true }));
    return (ls.length - 1) * lh;
  };
  // the 3D camera of the scenes with solids: the title may take more than one line, so the solids are fitted into the room below it (ex = the extra height of the title)
  const cam3 = (A, bb, cv, ex, bot = 0) => { const Pj = camera(A("az"), A("el"), A("zoom"), A("px"), bb, cv.W, cv.H - (cv.narrow ? 96 : 86) - ex - bot, 0.97, 0.9), p0 = Pj.p; Pj.p = (x, y, z) => { const q = p0(x, y, z); return [q[0], q[1] + ex]; }; return Pj; };
  const S = SCENES;

  // =============================================================================================== the flow (state: one picture of the whole stream)
  S.flow = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF(), sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : (cv.video ? 13.5 : 12.5), L = fs * 1.32, W = cv.W, LX = nar ? 38 : 66, NW = 34;
    const tg = tagger(sc, { ...cv, fs });
    const stn = D.stations, txX = LX + (nar ? 30 : 44), txW = W - txX - (nar ? 14 : 28);
    let s = chart(cv), body = "";
    const ex = ttl(tg, { ...cv, fs }, T.flowHead, nar ? 14 : 22, nar ? 30 : 28);
    let y = (nar ? 74 : 52) + ex; const ys = [];
    stn.forEach((q, i) => {
      const base = i === 0, cards = q.cards.map((id) => D.cards.find((c) => c.id === id)).concat((T.gateOnly[i] || []).map((g) => ({ id: g.id, grade: "読まない(関門 ✗)" })));      // v3.1: + the cards stopped at a control / gate that the pack does not read (olm83 · olm88)
      ys.push(y);
      body += `<rect class="af-node${base ? " base" : " later"}" x="${n1(LX - NW / 2)}" y="${n1(y)}" width="${NW}" height="${NW}" rx="6"${base ? "" : ' fill="url(#moy1-hatch)"'}/>`;
      tg([LX, y + NW / 2 + fs * 0.36], String(i), "pt strong", 0, 0, "middle", { fixed: true });
      let yy = y + fs * 1.0;
      for (const ln_ of lines(i === 0 ? T.flowSt[i] : `${T.flowSt[i]}  ·  ${q.date}`, txW / 1.06, fs).slice(0, 3)) { tg([txX, yy], ln_, "title", 0, 0, "start", { fixed: true }); yy += L * 1.05; } yy += L * 0.1;
      // the cards of the station: a glyph (grade by shape) + the card's name; wrapped when the row is narrow
      let cx = txX, cy = yy - fs * 0.78;
      const tw = (t) => estW(t) * fs + 8;
      if (cards.length) cards.forEach((c) => { const w = 14 + 5 + tw(c.id) + 8; if (cx + w > txX + txW) { cx = txX; cy += L * 1.1; } body += glyph(cx, cy, 6.5, c.grade); tg([cx + 19, cy + 11.5], c.id, "pt strong", 0, 0, "start", { fixed: true }); cx += w + 4; });
      else tg([txX, yy], T.flowS0cards, "pt muted", 0, 0, "start", { fixed: true });
      yy = cy + L * 1.6;
      for (const ln_ of lines(T.flowRes[i](D), txW, fs).slice(0, nar ? 9 : 4)) { tg([txX, yy], ln_, "pt", 0, 0, "start", { fixed: true }); yy += L; }
      if (i < stn.length - 1) { yy += L * 0.15; for (const ln_ of lines("↓ " + T.flowQ[i + 1], txW, fs).slice(0, nar ? 4 : 2)) { tg([txX, yy], ln_, "pt muted af-q", 0, 0, "start", { fixed: true }); yy += L; } }
      y = yy + L * 0.45;
    });
    // v3.1 (entry P #s26): the rail between two nodes is THICK when the question into the lower node came from this figure (ledger R04 · the readers' next A), DOTTED when it continues the house's line 1
    for (let i = 0; i < ys.length - 1; i++) s += ln(LX, ys[i] + NW, LX, ys[i + 1], T.fromFig.includes(i + 1) ? "af-rail thick" : "af-rail dot");
    s += body; cv.used = y;
    return s + sc.tags.join("");
  };

  // =============================================================================================== (a) the L3 of the 10-28 ledger -> olm76: three columns (the share of rows whose later 32 tokens' mean of the close group exceeds the earlier 32's)
  S.l3 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().l3, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, CW = nar ? 62 : 74, CD = nar ? 46 : 52, GAP = nar ? 60 : 96, HS = nar ? 330 : 250;
    const cols = [["b", D.q1.pos, D.q1.n, D.q1.median, T.l3bind, D.q1.sign_p], ["g", D.pseudo.pos, D.pseudo.n, D.pseudo.median, T.l3false, D.pseudo.sign_p], ["o", D.attr.pos, D.attr.n, D.attr.median, T.l3attr, null]];
    const XEND = cols.length * (CW + GAP) + 30, ex = ttl(tag, cv, T.l3head, cv.W / 2, 24, { anchor: "middle" });
    const Pj = cam3(A, [-60, -60, -6, XEND, CD + 60, HS + 60], cv, ex, nar ? 270 : 80);
    box(sc, Pj, -50, -50, XEND + 40, CD + 100, 5, "p", -5, { key: -1e9 });
    sc.flat.push(`<path class="ln zero" d="${H.path(Pj, [[-14, -12, HS * 0.5], [XEND - 20, -12, HS * 0.5], [XEND - 20, CD + 12, HS * 0.5], [-14, CD + 12, HS * 0.5]], true)}"/>`);
    tag(Pj.p(-14, CD + 12, HS * 0.5), "50 %", "pt muted", -4, 4, "end", { fixed: true });
    cols.forEach(([tone, pos, n, med, nm, p], i) => {
      const x0 = 14 + i * (CW + GAP), h = Math.max(0.8, (pos / n) * HS);
      box(sc, Pj, x0, 0, CW, CD, h, tone, 0, {});
      tag(Pj.p(x0 + CW / 2, CD / 2, h), `${pos}/${n}`, "title " + (tone === "g" ? "" : tone), 0, -8, "middle", { fixed: true });
      tag(Pj.p(x0 + CW / 2, CD, 0), f3(med), "pt muted", 0, 15, "middle", { fixed: true });
      const lw = Math.max(110, Math.min(nar ? 250 : 190, Pj.k * (CW + GAP) - 14)), nl = lines(nm, lw, cv.fs);
      for (const [k, ln_] of nl.entries()) tag(Pj.p(x0 + CW / 2, CD, 0), ln_, "pt strong", 0, 33 + k * cv.fs * 1.25, "middle", { fixed: true });
      if (p !== null) tag(Pj.p(x0 + CW / 2, CD, 0), `p ${p.toFixed(3)}`, "pt muted", 0, 33 + nl.length * cv.fs * 1.25 + 4, "middle", { fixed: true });
    });
    return flush(sc) + rail(cv, T, 1, cv.H - (nar ? 64 : 52), {});
  };

  // =============================================================================================== (b1) the inference-space search: what a probe on the residual reads beyond the J-lens readout and a bag of words
  // one row per card; the AUC axis 0.4 .. 1.0; four markers (layer 32 residual ● · layer 48 residual ○ · J-lens readout ◆ · bag of words ▲); the grey band = the card's own null (the layer-32 probe on pseudo labels)
  S.space1 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().space, sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), W = cv.W, L = fs * 1.35;
    const rows = [...D.look.map((x, i) => ({ id: x.card, name: T.spLook[i], x })), { id: "olm91", name: T.spFirst, x: D.first64 }];
    const XA = nar ? 40 : 244, XB = W - (nar ? 28 : 170), lo = 0.4, hi = 1.0, X = (v) => XA + ((v - lo) / (hi - lo)) * (XB - XA), RH = nar ? 236 : 108;
    let s = chart(cv);
    const ex = ttl(tag, { ...cv, fs }, T.spHead, nar ? 14 : 22, nar ? 34 : 30), Y0 = (nar ? 120 : 92) + ex;
    // axis
    for (const v of [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) { s += ln(X(v), Y0 - 22, X(v), Y0 + rows.length * RH - 22, v === 0.5 ? "axzero" : "axtick"); tag([X(v), Y0 - 30], v.toFixed(1), "pt muted", 0, 0, "middle", { fixed: true }); }
    tag([XB, Y0 + rows.length * RH - 22 + L * 0.7], T.spAxis, "pt muted", 0, 0, "end", { fixed: true });
    rows.forEach((r, i) => {
      const y = Y0 + i * RH + RH / 2 - 22, x = r.x, nb = x.null;
      const nb0 = Math.max(nb.p05, lo), nb1 = Math.min(nb.p95, hi); s += rect(X(nb0), y - 24, X(nb1) - X(nb0), 48, "af-null");
      s += ln(X(0.5), y, X(1.0), y, "axtick");
      const mk = (v, kind, k2) => { const cx = X(v), cy = y; return kind === "dot" ? `<circle class="af-mk l32" cx="${n1(cx)}" cy="${n1(cy)}" r="${nar ? 8 : 6.5}"/>` : kind === "ring" ? `<circle class="af-mk l48" cx="${n1(cx)}" cy="${n1(cy)}" r="${nar ? 8 : 6.5}"/>` : kind === "dia" ? `<path class="af-mk j" d="${H.dia(cx, cy, nar ? 9 : 7.5)}"/>` : `<path class="af-mk w" d="M${n1(cx)} ${n1(cy - 8)}L${n1(cx + 7.5)} ${n1(cy + 6)}L${n1(cx - 7.5)} ${n1(cy + 6)}Z"/>`; };
      // whiskers (5 % .. 95 %) of the layer-32 probe
      s += ln(X(Math.max(x.auc.L32.p05, lo)), y - 16, X(Math.min(x.auc.L32.p95, hi)), y - 16, "af-whisk");
      s += mk(x.auc.W.med, "tri") + mk(x.auc.J.med, "dia") + mk(x.auc.L48.med, "ring") + mk(x.auc.L32.med, "dot");
      tag([nar ? 14 : 22, y - (nar ? 56 : 22)], r.id, "pt strong", 0, 0, "start", { fixed: true });
      let k = 0; for (const ln_ of lines(r.name.replace(/^olm\d+ · /, ""), nar ? W - 28 : XA - 44, fs).slice(0, nar ? 3 : 4)) { tag([nar ? 14 : 22, y - (nar ? 56 : 22) + L * (k + 1)], ln_, "pt muted", 0, 0, "start", { fixed: true }); k++; }
      const e = x.E.L32;
      tag([nar ? 14 : XB + 16, nar ? y + 84 : y - 4], `E(L32) ${f3(e.med)}`, "pt strong", 0, 0, "start", { fixed: true });
      tag([nar ? 14 + estW(`E(L32) ${f3(e.med)}`) * fs + 18 : XB + 16, nar ? y + 84 : y + 14], `[${f3(e.p05)}, ${f3(e.p95)}]`, "pt muted", 0, 0, "start", { fixed: true });
    });
    return s + sc.tags.join("") + rail(cv, T, 2, cv.H - (nar ? 60 : 44), {});
  };

  // =============================================================================================== (b2) the k table: E (layer-32 / layer-48 probe minus the better of J and the bag of words) by how many tokens ahead
  S.space2 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().space, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, BW = nar ? 12 : 15, BD = nar ? 22 : 26, PG = nar ? 6 : 8, CG = nar ? 10 : 16, GG = nar ? 28 : 46, ZS = nar ? 7600 : 5600, cards = ["olm86", "olm89", "olm92"], ks = ["1", "8", "16", "32"];
    const trip = 3 * (2 * BW + 2) + 2 * CG, XEND = ks.length * trip + (ks.length - 1) * GG + 40, ZTOP = 0.056 * ZS, ZBOT = -0.012 * ZS, ex = ttl(tag, cv, T.sp2Head, cv.W / 2, 22, { anchor: "middle" });
    const Pj = cam3(A, [-40, -50, ZBOT - 10, XEND, BD + 60, ZTOP + 40], cv, ex, nar ? 50 : 20);
    box(sc, Pj, -30, -40, XEND + 10, BD + 80, 5, "p", ZBOT - 14, { key: -1e9 });
    const plane = (z, cls, label) => { sc.flat.push(`<path class="ln ${cls}" d="${H.path(Pj, [[-12, -10, z], [XEND - 20, -10, z], [XEND - 20, BD + 10, z], [-12, BD + 10, z]], true)}"/>`); tag(Pj.p(-12, BD + 10, z), label, "pt muted", -4, 4, "end", { fixed: true }); };
    plane(0, "zero", "0"); plane(D.line_false * ZS, "zero", "+0.01"); plane(D.line_candidate * ZS, "zero cand", "+0.05"); plane(0.02 * ZS, "zero post", T.post02);      // v3.1: +0.02 = olm89's confirming line, set after seeing olm86 (PREREG olm89 §0) = after the fact; the judgment uses the frozen +0.01
    ks.forEach((k, gi) => {
      const gx = 14 + gi * (trip + GG);
      cards.forEach((c, ci) => {
        const cx = gx + ci * (2 * BW + 2 + CG), e = D.ktab[c][k];
        [["L32", "g", 0], ["L48", "h", BW + 2]].forEach(([ly, tone, dx]) => {
          const v = e[ly], h = Math.abs(v) * ZS;
          box(sc, Pj, cx + dx, 0, BW, BD, Math.max(h, 0.7), tone, v >= 0 ? 0 : -h, {});
          if (k === "8" && !nar) tag(Pj.p(cx + dx + BW / 2, BD / 2, v >= 0 ? h : 0), f3(v).replace("+0.0", "+.0"), "pt " + (ly === "L32" ? "strong" : "muted"), 0, -7, "middle", { fixed: true });
        });
        if (!nar || k === "8") tag(Pj.p(cx + BW, BD, ZBOT - 14), c.replace("olm", ""), "pt muted", 0, 13, "middle", { fixed: true });
      });
      tag(Pj.p(gx + trip / 2, BD, ZBOT - 14), `k = ${k}`, "title", 0, nar ? 34 : 36, "middle", { fixed: true });
    });
    return flush(sc) + rail(cv, T, 2, cv.H - (nar ? 60 : 44), {});
  };

  // =============================================================================================== (c1) structures that are not words: a name written -> "this circle" (probe) · the heads that carry the behaviour (attention share · replacement)
  S.struct1 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().struct, sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), W = cv.W, L = fs * 1.35;
    let s = chart(cv), y = nar ? 34 : 30;
    const panW = nar ? W - 28 : Math.min(W * 0.5, 440) - 30, exA = ttl(tag, { ...cv, fs }, T.s1HeadA, nar ? 14 : 22, y, { maxW: panW }); y += exA + L * 1.2;
    // panel A: AUC bars (0.4 .. 1.0): to "this circle" (dark) vs to the word before "this" (light) for L32 · L48 · J · W
    const ax0 = nar ? 60 : 80, axW = nar ? W - 90 : Math.min(W * 0.5, 440) - 90, pH = nar ? 250 : 190, py0 = y + 14, Y = (v) => py0 + pH - ((v - 0.4) / 0.6) * pH, pg = axW / 4;
    for (const v of [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) { s += ln(ax0, Y(v), ax0 + axW, Y(v), v === 0.5 ? "axzero" : "axtick"); tag([ax0 - 6, Y(v) + 4], v.toFixed(1), "pt muted", 0, 0, "end", { fixed: true }); }
    ["L32", "L48", "J", "W"].forEach((m, i) => {
      const x = ax0 + i * pg + pg * 0.14, bw = pg * 0.32;
      [["to_dem", "c-g", 0], ["to_ctl", "c-x", bw + 4]].forEach(([k, cl, dx]) => { const v = D.ref.olm94_q2[k][m]; s += rect(x + dx, Y(Math.max(v, 0.4)), bw, Math.max(1, Y(0.4) - Y(Math.max(v, 0.4))), "cell " + cl); tag([x + dx + bw / 2, Y(Math.max(v, 0.4)) - (k === "to_dem" ? 5 : 5 + L)], v.toFixed(nar ? 2 : 3), "pt " + (k === "to_dem" ? "strong" : "muted"), 0, 0, "middle", { fixed: true }); });
      tag([x + bw, py0 + pH + L * 1.2], T.s1Probe[i], "pt strong", 0, 0, "middle", { fixed: true });
    });
    y = py0 + pH + L * 2.6;
    for (const [i, ln_] of lines(T.s1KeyA, nar ? W - 28 : Math.min(W * 0.5, 440) - 30, fs).entries()) tag([nar ? 14 : 22, y + i * L], ln_, "pt muted", 0, 0, "start", { fixed: true });
    y += L * (nar ? 2.4 : 1.6) + L * 1.2;
    // panel B (right on a wide canvas, below on a narrow one): the share of the top-10 heads' attention by span
    const bx = nar ? 14 : Math.min(W * 0.5, 440) + 24, bw0 = nar ? W - 28 : W - bx - 22; let by = nar ? y + 10 : 30;
    const exB = ttl(tag, { ...cv, fs }, T.s1HeadB, bx, by, { maxW: bw0 }); by += exB + L * 1.4;
    const sh = D.heads.share, order = ["ref_name", "oth_name", "dem", "sel", "ctl", "v_letters", "self", "rest"], lab = T.s1Spans, lx = bx, rowP = nar ? L * 2.25 : L * 1.45, barX = nar ? bx : bx + 175, barW = nar ? bw0 - 110 : bw0 - 240, SC = barW / 0.5;
    order.forEach((k, i) => { const yy = by + i * rowP, yb = nar ? yy + L * 0.95 : yy; tag([lx, yy + 4], lab[i], "pt " + (i < 2 ? "strong" : "muted"), 0, 0, "start", { fixed: true }); s += rect(barX, yb - 8, Math.max(1.5, sh[k] * SC), nar ? 16 : 12, "cell " + (i === 0 ? "c-g" : "c-x")); tag([barX + sh[k] * SC + 6, yb + 4], sh[k].toFixed(3), "pt " + (i < 2 ? "strong" : "muted"), 0, 0, "start", { fixed: true }); });
    by += order.length * rowP + L * 0.8;
    for (const [i, ln_] of lines(T.s1Patch(D.heads), bw0, fs).entries()) tag([bx, by + i * L], ln_, "pt strong", 0, 0, "start", { fixed: true });
    by += lines(T.s1Patch(D.heads), bw0, fs).length * L + L * 0.5;
    for (const [i, ln_] of lines(T.s1Overlap(D.heads), bw0, fs).entries()) tag([bx, by + i * L], ln_, "pt muted", 0, 0, "start", { fixed: true });
    return s + sc.tags.join("") + rail(cv, T, 3, cv.H - (nar ? 60 : 44), {});
  };

  // =============================================================================================== (c2) pointer -> value by layer: how often the behaviour follows the source's pointer (solid) / the source's value (dashed) when a position is replaced with the source's
  S.struct2 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().struct.layers, sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), W = cv.W, L = fs * 1.35;
    const panels = [["sel", D.sel, T.s2Sel, [[D.sel_drop, T.s2MarkSel]]], ["end", D.end, T.s2End, [[D.end_val_first, T.s2MarkEnd]]], ["tail", D.tail, T.s2Tail, [[D.tail_switch, T.s2MarkTail]]]];
    const ax0 = nar ? 50 : 70, axW = W - ax0 - (nar ? 24 : 40), pH = nar ? 190 : 118, gap = nar ? 112 : 70, X = (l) => ax0 + (l / 56) * axW;
    let s = chart(cv);
    const ex = ttl(tag, { ...cv, fs }, T.s2Head, nar ? 14 : 22, nar ? 32 : 30), Y0 = (nar ? 142 : 84) + ex;
    panels.forEach(([key, data, name, marks], pi) => {
      const y0 = Y0 + pi * (pH + gap), Y = (v) => y0 + pH - v * pH;
      { const nl = lines(name, W - ax0 - 20, fs).slice(0, 3); nl.forEach((l, k) => tag([ax0, y0 - 12 - (nl.length - 1 - k) * L], l, "pt strong", 0, 0, "start", { fixed: true })); }
      for (const v of [0, 0.5, 1]) { s += ln(ax0, Y(v), ax0 + axW, Y(v), v === 0 ? "axbase" : "axtick"); tag([ax0 - 6, Y(v) + 4], String(v), "pt muted", 0, 0, "end", { fixed: true }); }
      for (const l of [8, 16, 24, 32, 40, 48, 56]) { s += ln(X(l), y0 + pH, X(l), y0 + pH + 4, "axtick"); if (pi === 2) tag([X(l), y0 + pH + L * 1.25], String(l), "pt muted", 0, 0, "middle", { fixed: true }); }
      for (const [l, lab] of marks) { s += ln(X(l), y0 - 2, X(l), y0 + pH, "af-vline"); tag([X(l) + 6, y0 + 10], `${lab} ${l}`, "pt strong", 0, 0, "start", { fixed: true }); }
      const pts = (k) => data.map((r) => [X(r.L), Y(r[k])]);
      s += `<path class="af-curve po" d="M${pts("po").map((p) => p.map(n1).join(" ")).join("L")}"/>` + `<path class="af-curve vo" d="M${pts("vo").map((p) => p.map(n1).join(" ")).join("L")}"/>`;
      pts("po").forEach((p) => { s += `<circle class="af-mk po" cx="${n1(p[0])}" cy="${n1(p[1])}" r="${nar ? 5.5 : 4.2}"/>`; });
      pts("vo").forEach((p) => { s += rect(p[0] - (nar ? 5 : 4), p[1] - (nar ? 5 : 4), nar ? 10 : 8, nar ? 10 : 8, "af-mk vo"); });
    });
    for (const [k, ln_] of lines(T.s2Axis, axW, fs).entries()) tag([ax0 + axW, Y0 + 2 * (pH + gap) + pH + L * 2.5 + k * L], ln_, "pt muted", 0, 0, "end", { fixed: true });
    return s + sc.tags.join("") + rail(cv, T, 3, cv.H - (nar ? 56 : 40), {});
  };

  // =============================================================================================== (d1) apex proof, olm112: what the 37 rows whose answer field is the apex circle write in their proof field
  S.apex1 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().apex.olm112, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, CW = nar ? 34 : 42, CD = nar ? 34 : 40, G = nar ? 26 : 40, HS = nar ? 300 : 230, n = D.bind.n;
    const bars = [["BIS", D.bind.BIS], ["RA", D.bind.RA], ["THC", D.bind.THC], ["CHAIN", D.bind.CHAIN], ["radical", D.bind.ALT_radical], ["homothety", D.bind.ALT_homothety], ["power", D.bind.ALT_power]];
    const P4 = AF().apex.prf4, XP = 12 + bars.length * (CW + G) + 2 * (nar ? 14 : 30);      // v3.1: the prf4 bar (another card · a chat model), apart at the right
    const XEND = XP + CW + 40 + (nar ? 20 : 40), ex = ttl(tag, cv, T.a1Head, cv.W / 2, 22, { anchor: "middle" });
    const Pj = cam3(A, [-50, -50, -6, XEND, CD + 70, HS * 0.5 + 50], cv, ex + (nar ? 60 : 24), nar ? 100 : 56);
    box(sc, Pj, -40, -44, XEND + 20, CD + 110, 5, "p", -5, { key: -1e9 });
    bars.forEach(([k, v], i) => {
      const x0 = 12 + i * (CW + G) + (i >= 4 ? (nar ? 14 : 30) : 0), h = (v / n) * HS, chain = k === "CHAIN";
      box(sc, Pj, x0, 0, CW, CD, Math.max(h, 0.8), i < 4 ? "b" : "g", 0, { cls: chain ? "af-zero" : "" });
      tag(Pj.p(x0 + CW / 2, CD / 2, Math.max(h, 0.8)), `${v}`, "title " + (i < 4 ? "b" : ""), 0, -8, "middle", { fixed: true });
      for (const [k, ln_] of lines(T.a1Bars[i], Pj.k * (CW + G) - 4, cv.fs).entries()) tag(Pj.p(x0 + CW / 2, CD, 0), ln_, "pt strong", 0, 15 + k * 13, "middle", { fixed: true });
    });
    { const h = (P4.chain / P4.bind) * HS; box(sc, Pj, XP, 0, CW, CD, h, "b", 0, { cls: "af-ext" }); tag(Pj.p(XP + CW / 2, CD / 2, h), `${P4.chain} / ${P4.bind}`, "title", 0, -8, "middle", { fixed: true }); for (const [k, ln_] of lines(T.a1Prf4, Pj.k * (CW + G) + 30, cv.fs).slice(0, 4).entries()) tag(Pj.p(XP + CW / 2, CD, 0), ln_, "pt muted", 0, 15 + k * 13, "middle", { fixed: true }); }
    { const ap = Pj.p(12 + 4 * (CW + G) + (nar ? 14 : 30), 0, HS), aL = lines(T.a1Alt, Math.max(120, cv.W - ap[0] - 14), cv.fs).slice(0, 3); aL.forEach((l, k) => tag(ap, l, "pt muted", 0, -12 - (aL.length - 1 - k) * 13, "start", { fixed: true })); }
    return flush(sc) + rail(cv, T, 4, cv.H - (nar ? 60 : 44), {});
  };

  // =============================================================================================== (d2) apex proof, olm114: the frontier's proof given in steps; does the base model write the next steps?
  S.apex2 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().apex.olm114, sc = newScene(), tag = tagger(sc, cv), nar = cv.narrow, CW = nar ? 40 : 46, CD = nar ? 38 : 44, G = nar ? 22 : 34, HS = nar ? 300 : 230;
    const k0 = D.Q3, cols = [
      { nm: T.a2K0, v: k0.bind, n: k0.k0_rows, tone: "x", note: T.a2K0n, gate: true },
      { nm: T.a2K1, v: D.Q1.RA_and_THC, n: D.Q1.k1_rows, tone: "g", fam: [D.fam.k1.opus.RA_and_THC, D.fam.k1.fable.RA_and_THC, 20] },
      { nm: T.a2K2, v: D.Q2.THC, n: D.Q2.k2_rows, tone: "g", fam: [D.fam.k2.opus.THC, D.fam.k2.fable.THC, 20] },
    ];
    const XEND = cols.length * (2 * CW + G + 70) + 20, ex = ttl(tag, cv, T.a2Head, cv.W / 2, 22, { anchor: "middle" });
    const Pj = cam3(A, [-60, -60, -6, XEND, CD + 70, HS * 0.7 + 50], cv, ex, nar ? 230 : 120), pitch = Pj.k * (2 * CW + G + 70) - 10;
    box(sc, Pj, -50, -50, XEND + 30, CD + 120, 5, "p", -5, { key: -1e9 });
    sc.flat.push(`<path class="ln zero" d="${H.path(Pj, [[-14, -12, HS * 0.5], [XEND - 24, -12, HS * 0.5], [XEND - 24, CD + 12, HS * 0.5], [-14, CD + 12, HS * 0.5]], true)}"/>`);
    tag(Pj.p(-14, CD + 12, HS * 0.5), "50 %", "pt muted", -4, 4, "end", { fixed: true });
    cols.forEach((c, i) => {
      const x0 = 14 + i * (2 * CW + G + 70), h = Math.max(0.8, (c.v / c.n) * HS);
      box(sc, Pj, x0, 0, CW, CD, h, c.tone, 0, { cls: c.gate ? "af-zero" : "" });
      tag(Pj.p(x0 + CW / 2, CD / 2, h), `${c.v}/${c.n}`, "title", 0, -8, "middle", { fixed: true });
      if (c.fam) c.fam.slice(0, 2).forEach((fv, fi) => { const hh = Math.max(0.8, (fv / c.fam[2]) * HS); box(sc, Pj, x0 + CW + 6 + fi * (nar ? 24 : 30), 0, nar ? 20 : 26, CD, hh, fi === 0 ? "x" : "g", 0, {}); tag(Pj.p(x0 + CW + 6 + fi * (nar ? 24 : 30) + (nar ? 10 : 13), CD / 2, hh), `${fv}`, "pt strong", 0, -6, "middle", { fixed: true }); tag(Pj.p(x0 + CW + 6 + fi * (nar ? 24 : 30) + (nar ? 10 : 13), CD, 0), fi === 0 ? "O" : "F", "pt muted", 0, 14, "middle", { fixed: true }); });
      const nmL = lines(c.nm, pitch, cv.fs), y2 = 32 + nmL.length * 13 + 6;
      nmL.forEach((ln_, k) => tag(Pj.p(x0 + CW / 2, CD, 0), ln_, "pt strong", 0, 32 + k * 13, "middle", { fixed: true }));
      if (c.note) for (const [k, ln_] of lines(c.note, Math.min(pitch, nar ? 190 : 200), cv.fs).entries()) tag(Pj.p(x0 + CW / 2, CD, 0), ln_, "pt muted", 0, y2 + k * cv.fs * 1.25, "middle", { fixed: true });
      if (c.fam && i === 1) for (const [k, ln_] of lines(T.a2Fam, Math.min(pitch, nar ? 220 : 210), cv.fs).entries()) tag(Pj.p(x0 + CW, CD, 0), ln_, "pt muted", 0, y2 + k * cv.fs * 1.25, "middle", { fixed: true });
    });
    return flush(sc) + rail(cv, T, 4, cv.H - (nar ? 60 : 44), {});
  };

  // =============================================================================================== (next 1) olm128: the candidate A (the teacher's choice) was frozen and read: one cell = one blocked row (bind blue / not bind grey), by where the row starts, by cue
  S.next1 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), D = AF().next, CS = DATA.cue_start.cells, sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), W = cv.W, L = fs * 1.35;
    const cues = [["nl", "nl", "\\n"], ["sp", "space", "␣"], ["nn", "nlnl", "\\n\\n"]];
    let s = chart(cv);
    const ex = ttl(tag, { ...cv, fs }, T.n1Head, nar ? 14 : 22, nar ? 34 : 30);
    const CWd = nar ? 26 : 30, CHt = nar ? 24 : 26, colW = nar ? W - 28 : (W - 44) / 3, Y0 = (nar ? 78 : 64) + ex;
    cues.forEach(([ck, rk, nm], ci) => {
      const cells = CS[ck], c = D.cells[rk], bx = nar ? 14 : 22 + ci * colW, by = nar ? Y0 + ci * 330 : Y0;
      tag([bx, by + 4], `${T.n1Cue} ${nm}`, "title", 0, 0, "start", { fixed: true });
      tag([bx, by + 4 + L * 1.15], `${T.n1Blocked} · n ${c.n} · bind ${c.bind}`, "pt muted", 0, 0, "start", { fixed: true });
      [["json", T.n1Json, c.json], ["text", T.n1Text, c.text]].forEach(([k, nm2, cnt], ri) => {
        const yy = by + L * 3.4 + ri * (nar ? 120 : 112), xs = cells.filter((x) => x.start === k);
        tag([bx, yy - 10], `${nm2} · ${cnt}`, "pt strong", 0, 0, "start", { fixed: true });
        const perRow = Math.max(1, Math.floor((colW - 14) / (CWd + 3)));
        xs.sort((a, b) => (a.label === "B-bind" ? 0 : 1) - (b.label === "B-bind" ? 0 : 1) || a.seed - b.seed).forEach((x, i) => { const cx = bx + (i % perRow) * (CWd + 3), cy = yy + Math.floor(i / perRow) * (CHt + 4); s += rect(cx, cy, CWd, CHt, "cell " + (x.label === "B-bind" ? "c-b" : "c-g")); tag([cx + CWd / 2, cy + CHt / 2 + 4], "s" + x.seed, "pt " + (x.label === "B-bind" ? "" : "muted"), 0, 0, "middle", { fixed: true }); });
        const bnd = xs.filter((x) => x.label === "B-bind").length;
        tag([bx, yy + (CHt + 4) * Math.max(1, Math.ceil(xs.length / perRow)) + L * 0.9], cnt ? `bind ${bnd} / ${cnt}` : "—", "pt " + (cnt ? "strong" : "muted"), 0, 0, "start", { fixed: true });
      });
    });
    return s + sc.tags.join("") + rail(cv, T, 5, cv.H - (nar ? 56 : 40), {});
  };

  // =============================================================================================== (next 2) the candidates the readers raised: A answered by olm128, B-E left (listed only), and the second stage waits for the teacher
  S.next2 = (S_, A, cv, st) => {
    begin(cv);
    const T = TX(S_.lang), sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), W = cv.W, L = fs * 1.35;
    let s = chart(cv), y = nar ? 34 : 30;
    y += ttl(tag, { ...cv, fs }, T.n2Head, nar ? 14 : 22, y); y += L * 1.5;
    const rows = T.n2Rows, bx = nar ? 12 : 20, bw = W - 2 * bx;
    rows.forEach((r, i) => {
      const tl = lines(r.q, bw - 74, fs).slice(0, nar ? 5 : 2), cl = lines(r.cmp, bw - 74, fs).slice(0, nar ? 4 : 2), h = (tl.length + cl.length) * L + L * (nar ? 2.8 : 1.7);
      s += `<rect class="af-cand${r.done ? " done" : ""}${r.res ? " res" : ""}" x="${bx}" y="${n1(y)}" width="${bw}" height="${n1(h)}" rx="7"${r.res ? ' fill="url(#moy1-hatch)" fill-opacity=".35"' : ""}/>`;
      tag([bx + 12, y + L * 1.15], r.k, "title", 0, 0, "start", { fixed: true });
      let yy = y + L * 1.15 + (nar ? L * 1.1 : 0);
      tl.forEach((t) => { tag([bx + 52, yy], t, "pt strong", 0, 0, "start", { fixed: true }); yy += L; });
      cl.forEach((t) => { tag([bx + 52, yy], t, "pt muted", 0, 0, "start", { fixed: true }); yy += L; });
      tag([bx + bw - 12, y + L * 1.15], r.tag, "pt " + (r.done ? "strong" : "muted"), 0, 0, "end", { fixed: true });
      y += h + (nar ? 10 : 8);
    });
    cv.used = y + (nar ? 90 : 60);
    return s + sc.tags.join("") + rail(cv, T, 5, cv.H - (nar ? 56 : 40), {});
  };

  // =============================================================================================== (10-28 part, transplanted) the row by row slopes of olm59: small multiples, one panel per (event kind x group); the bars are the rows sorted by (after - before)
  S.slope = (S_, A, cv, st) => {
    begin(cv);
    const T = I18N[S_.lang].tags, TA = TX(S_.lang), D = DATA.olm59, sc = newScene(), nar = cv.narrow, fs = nar ? cv.fs : 12, tag = tagger(sc, { ...cv, fs }), W = cv.W, L = fs * 1.35;
    const evs = [["o_diam", "b", T.evO], ["h_diam", "o", T.evH]], GN4 = ["close", "mid", "ans", "think"];
    let mx = 0; for (const ev of ["o_diam", "h_diam"]) for (const r of D.slopes[ev]) for (const v of r.d) mx = Math.max(mx, Math.abs(v)); mx = Math.ceil(mx * 20) / 20;
    const cols = nar ? 2 : 4, pw = nar ? (W - 40) / 2 : (W - 44 - 3 * 14) / 4, ph = nar ? 130 : 138, gx = 14, gy = nar ? 100 : 66, X0 = nar ? 14 : 22;
    let s = chart(cv);
    const ex = ttl(tag, { ...cv, fs }, TA.slHead, nar ? 14 : 22, nar ? 34 : 30), Y0 = (nar ? 108 : 84) + ex;
    let pi = 0;
    evs.forEach(([ev, tone, nm]) => GN4.forEach((g, gi) => {
      const col = pi % cols, row = Math.floor(pi / cols), x0 = X0 + col * (pw + gx), y0 = Y0 + row * (ph + gy), yc = y0 + ph / 2, rows = D.slopes[ev].map((r) => ({ d: r.d[gi], r })).sort((a, b) => a.d - b.d), n = rows.length, bw = pw / n, sc_ = (ph / 2) / mx;
      const up = rows.filter((x) => x.d > 0).length, ds = rows.map((x) => x.d), medv = n % 2 ? ds[(n - 1) / 2] : (ds[n / 2 - 1] + ds[n / 2]) / 2;
      s += rect(x0, y0, pw, ph, "af-panel") + ln(x0, yc, x0 + pw, yc, "axzero");
      rows.forEach((x, i) => { const h = Math.abs(x.d) * sc_; s += rect(x0 + i * bw + 0.4, x.d >= 0 ? yc - h : yc, Math.max(1, bw - 0.8), Math.max(0.8, h), "bar62 " + (tone === "b" ? "o" : "h") + (x.r.id === D.S_O.id || x.r.id === D.S_H.id ? " scene" : "")); });
      s += ln(x0, yc - medv * sc_, x0 + pw, yc - medv * sc_, "af-med");
      tag([x0 + 2, y0 - 6 - L], `${T.grp[gi]}`, "pt strong", 0, 0, "start", { fixed: true });
      tag([x0 + 2, y0 - 6], `${up}/${n} ↑ · ${T.medShort} ${f3(medv)}`, "pt " + (tone === "b" ? "b" : "o"), 0, 0, "start", { fixed: true });
      if (gi === 0) tag([x0, y0 + ph + L * 1.1], TA.slEvt[ev === "o_diam" ? 0 : 1], "pt muted", 0, 0, "start", { fixed: true });
      pi++;
    }));
    for (const [k, ln_] of lines(TA.slScale(mx), W - 2 * X0 - 8, fs).entries()) tag([X0, Y0 + Math.ceil(8 / cols) * (ph + gy) - gy + L * 2.2 + k * L], ln_, "pt muted", 0, 0, "start", { fixed: true });
    return s + sc.tags.join("");
  };

  // =============================================================================================== the quote column of the added states (HTML): the card table (card · frozen commit · grade · source file and key) and a few verbatim blocks
  const gl = (g) => `<i class="gl-h ${GKEY[g] || "d"}"></i>`;
  const cardsOf = (ids) => ids.map((id) => AF().cards.find((c) => c.id === id));
  const cardTable = (lang, ids, head) => {
    const T = TX(lang), cs = cardsOf(ids), hd = lang === "ja" ? ["札", "凍結", "格", "出所の file と key(ConstructGap/exp/…)"] : ["card", "frozen", "grade", "source file and keys (ConstructGap/exp/…)"];
    const grade = (g) => T.grade[g] || g;
    return `<section class="q-blk"><h4>${esc(head || T.cardsHead)}</h4><table class="q-tab af-ct"><tr>${hd.map((x) => `<th>${esc(x)}</th>`).join("")}</tr>` + cs.map((c) => `<tr><td><b>${esc(c.id)}</b></td><td class="mono">${esc(c.freeze)}${c.id === "olm76" ? `<br>→ ${esc(c.read_commit)}` : ""}</td><td class="gr">${gl(c.grade)} ${esc(grade(c.grade))}</td><td class="src">${esc(c.src_file.replace("ConstructGap/exp/", ""))}<br>${esc(c.src_keys.join(" · "))}</td></tr>`).join("") + `</table></section>`;
  };
  const fx = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3);
  const kv = (rows) => `<table class="q-tab nw">${rows.map(([a, b, c]) => `<tr><td>${a}</td><td>${b}</td>${c !== undefined ? `<td>${c}</td>` : ""}</tr>`).join("")}</table>`;
  const blk = (title, body, note, cls = "") => `<section class="q-blk ${cls}"><h4>${esc(title)}</h4>${body}${note ? `<p class="q-note">${note}</p>` : ""}</section>`;
  // the verdict words of a card are the card's own (Japanese) strings; the English page glosses them (the number and the card stay as they are)
  const VW = { "偽": "false", "追わない": "not pursued", "変わらない": "unchanged", "保たれない": "not kept", "動く(説明の向き)": "moves (the explaining direction)", "逆": "reversed", "書き始めでは説明されない": "not explained by the start", "続ける": "continues", "片方なし": "one side missing", "間(錯覚の印)": "in between (illusion mark)", "遅い": "late", "無い": "none", "在る": "present" };
  const vw = (lang, s) => (lang === "ja" ? s : VW[s] || s);
  const Q = {};
  Q.l3 = (lang) => {
    const T = TX(lang), D = AF().l3, ja = lang === "ja";
    return blk(T.l3OldHead, `<pre>${esc(T.l3Old)}</pre>`, esc(T.l3OldNote), "af-old")
      + blk(T.l3NewHead, kv([[T.l3r1, `${D.q1.pos} / ${D.q1.n}`, `${fx(D.q1.median)} · p ${D.q1.sign_p.toFixed(3)}`], [T.l3r2, `${D.pseudo.pos} / ${D.pseudo.n}`, `${fx(D.pseudo.median)} · p ${D.pseudo.sign_p.toFixed(3)}`], [T.l3r3, `${fx(D.q3.median_a)} / ${fx(D.q3.median_b)}`, `${T.l3diff} ${fx(D.q3.diff)} · p ${D.q3.perm_p.toFixed(3)}`], [T.l3r4, `${D.commit_c3.pos} / ${D.commit_c3.n}`, `${T.l3c3}`]]), esc(T.l3NewNote))
      + cardTable(lang, ["olm76"]);
  };
  Q.flow = (lang) => {
    const T = TX(lang), D = AF(), grade = (g) => T.grade[g] || g, rows = [];
    D.stations.forEach((q, i) => { for (const id of q.cards) { const c = D.cards.find((x) => x.id === id); rows.push({ id, date: c.date, freeze: c.id === "olm76" ? `${c.freeze} → ${c.read_commit}` : c.freeze, g: c.grade, why: "" }); } for (const g of T.gateOnly[i] || []) rows.push({ id: g.id, date: g.date, freeze: g.freeze, g: "読まない(関門 ✗)", why: g.why }); });
    rows.sort((a, b) => Number(a.id.slice(3)) - Number(b.id.slice(3)));
    const nRead = D.cards.filter((c) => c.grade !== "読まない(関門 ✗)").length, nGate = rows.length - nRead;
    return `<section class="q-blk"><h4>${esc(T.ctHead)}</h4><table class="q-tab af-ct2"><tr>${T.ctCols.map((x) => `<th>${esc(x)}</th>`).join("")}</tr>` + rows.map((r) => `<tr><td><b>${esc(r.id)}</b></td><td>${esc(r.date)}</td><td class="mono">${esc(r.freeze)}</td><td class="gr">${gl(r.g)} ${esc(grade(r.g))}${r.why ? ` · ${esc(r.why)}` : ""}</td></tr>`).join("") + `</table><p class="q-note">${esc(T.ctNote(nRead, nGate))}</p></section>`;
  };
  Q.space1 = (lang) => { const T = TX(lang), D = AF().space; return cardTable(lang, ["olm84", "olm85", "olm86", "olm91"], T.cardsHead) + blk(T.sp1Cond, `<p class="q-note" style="margin:0">${esc(T.sp1CondTxt)}</p>`, ""); };
  Q.space2 = (lang) => {
    const T = TX(lang), D = AF().space, e = D.e89, p = D.plus;
    return blk(T.sp2Rows, kv([["olm89 Q1 (k = 8)", `L32 ${fx(e.L32.med)}`, `[${fx(e.L32.p05)}, ${fx(e.L32.p95)}]`], ["", `L48 ${fx(e.L48.med)}`, `[${fx(e.L48.p05)}, ${fx(e.L48.p95)}]`], ["olm92 E+ (k = 8)", `L32 ${fx(p.L32.med)}`, `[${fx(p.L32.p05)}, ${fx(p.L32.p95)}]`], ["", `L48 ${fx(p.L48.med)}`, `[${fx(p.L48.p05)}, ${fx(p.L48.p95)}]`]]), esc(T.sp2RowsNote))
      + cardTable(lang, ["olm86", "olm89", "olm92"]);
  };
  Q.struct1 = (lang) => cardTable(lang, ["olm93", "olm94", "olm95", "olm97", "olm98"]);
  Q.struct2 = (lang) => {
    const T = TX(lang), D = AF().struct.layers, b = D.branches;
    return blk(T.s2Br, kv([["olm101", b.olm101.map((w) => vw(lang, w)).join(" · ")], ["olm106", b.olm106.map((w) => vw(lang, w)).join(" · ")], ["olm108", b.olm108.map((w) => vw(lang, w)).join(" · ")]]), esc(T.s2BrNote)) + cardTable(lang, ["olm101", "olm106", "olm108"]);
  };
  Q.apex1 = (lang) => {
    const T = TX(lang), D = AF().apex.olm112, q = (id, t, k) => `<section class="q-blk sm dif"><h4>${esc(k)}</h4><pre>${esc(t)}</pre></section>`;
    const P4 = AF().apex.prf4;
    return cardTable(lang, ["olm112"]) + blk(T.a1P4Head, kv([[`prf4 · ${esc(P4.model)} · M1A`, `${T.a1P4Chain} ${P4.chain} / ${P4.bind}`]]), `${esc(T.a1P4Note)} ${esc(P4.file.replace("ConstructGap/exp/", ""))} ${esc(P4.key)}`) + blk(T.a1Q, kv([["Q1", `${D.Q1.chain} / ${D.Q1.bind}`, vw(lang, D.Q1.verdict)], ["Q2", `${D.Q2.bind_hyp} / ${D.Q2.bind_hq} · ${D.Q2.attr_hyp} / ${D.Q2.attr_hq}`, vw(lang, D.Q2.verdict)], ["Q3", `${D.Q3.new_attr} / ${D.n} · ${D.Q3.baseline_attr} / ${D.Q3.baseline_n}`, vw(lang, D.Q3.verdict)]]), esc(T.a1QNote))
      + D.ex.map((e) => q(e.key, e.text.length > 200 ? e.text.slice(0, 200).replace(/\s+\S*$/, "") + " …" : e.text, `${e.key} · ${T.a1Ex} ${e.label_json.replace("B-", "")} · T ${e.T}`)).join("");      // v3.1: the long example is cut at 240 characters (the prf4 box took its room)
  };
  Q.apex2 = (lang) => {
    const T = TX(lang), D = AF().apex.olm114, la = D.look, ks = [1, 2, 3, 4, 5, 6, 7, 8], row = (nm, k) => `<tr><td>${nm}</td>${ks.map((i) => `<td>${la[k][String(i)].toFixed(2)}</td>`).join("")}</tr>`;
    return cardTable(lang, ["olm114"]) + `<section class="q-blk"><h4>${esc(T.a2Look)}</h4><table class="q-tab"><tr><th></th>${ks.map((i) => `<th>${i}</th>`).join("")}</tr>${row("bis", "lens_BIS")}${row("perpendicular", "lens_RA")}${row("converse", "lens_THC")}${row("He · Hi · radical", "lens_ATTR")}${row("adjacent", "lens_ADJ")}</table><p class="q-note">${esc(T.a2LookNote)}</p></section>`
      + D.ex.map((e) => `<section class="q-blk sm dif"><h4>${esc(e.key)} · k = ${e.k} · ${esc(e.family)}</h4><pre>${esc(e.text.trim().slice(0, 300))}${e.text.trim().length > 300 ? "…" : ""}</pre></section>`).join("");
  };
  Q.next1 = (lang) => {
    const T = TX(lang), D = AF().next, v = D.verdicts, c = D.cells, E = DATA.cue_start.early, rj = { nl: "nl", sp: "space", nn: "nlnl" }, nm = { nl: "\\n", sp: "␣", nn: "\\n\\n" };
    const tab = `<table class="q-tab nw"><tr><th>cue</th><th>${esc(T.n1Json)}</th><th>${esc(T.n1Text)}</th><th>bind</th></tr>` + ["nl", "sp", "nn"].map((k) => { const x = c[rj[k]]; return `<tr><td>${nm[k]}</td><td>${x.json} (${T.n1b} ${x.json_bind})</td><td>${x.text} (${T.n1b} ${x.text_bind})</td><td>${x.bind} / ${x.n}</td></tr>`; }).join("") + `</table>`;
    const post = `<table class="q-tab nw"><tr><th>cue</th><th>${esc(T.n1Early)}</th><th>${esc(T.n1Late)}</th></tr>` + ["nl", "sp", "nn"].map((k) => `<tr><td>${nm[k]}</td><td>${E[k].early} / ${E[k].n} (${T.n1b} ${E[k].early_bind})</td><td>${E[k].late} (${T.n1b} ${E[k].late_bind})</td></tr>`).join("") + `</table>`;
    return blk(T.n1Tab, tab, esc(T.n1TabNote)) + blk(T.n1Verd, kv([["C0", T.n1C0], ["Q1", `${v.Q1_concordance.toFixed(3)} = ${Math.round(v.Q1_concordance * v.Q1_N)} / ${v.Q1_N}`, vw(lang, v.Q1)], ["Q2 \\n", fx(v.Q2_nl_diff), vw(lang, v.Q2_nl)], ["Q2 ␣", fx(v.Q2_space_diff).slice(0, 5), vw(lang, v.Q2_space)], ["Q3", vw(lang, v.Q3)]])) + blk(T.n1PostHead, post, esc(T.n1PostNote), "af-post") + cardTable(lang, ["olm128"]);
  };
  Q.next2 = (lang) => { const T = TX(lang); return cardTable(lang, ["olm128"], T.cardsHead) + blk(T.n2Second, `<ol class="af-ol">${T.n2SecondItems.map((x) => `<li>${esc(x)}</li>`).join("")}</ol>`, esc(T.n2SecondNote)); };
  Q.slope = (lang) => {
    const T = TX(lang), TT = I18N[lang].tags, D = DATA.olm59, one = (ev, tone) => {
      const bk = D.agg[ev].by_kind, ks = Object.keys(bk).sort((a, b) => bk[b] - bk[a] || (a < b ? -1 : 1)), n = D.agg[ev].n, sum = (lab) => ks.filter((k) => k.endsWith("|B-" + lab)).reduce((a, k) => a + bk[k], 0), bind = sum("bind"), attr = sum("attractor"), oth = n - bind - attr;
      const name = (k) => { const [p, l] = k.split("|"); return `${TT.paths[p]} × ${l.replace("B-", "")}`; };
      const parts = (lab) => ks.filter((k) => k.endsWith("|B-" + lab)).map((k) => `${TT.paths[k.split("|")[0]]} ${bk[k]}`).join(" + ");
      const othp = ks.filter((k) => !k.endsWith("|B-bind") && !k.endsWith("|B-attractor")).map((k) => `${name(k)} ${bk[k]}`).join(" · ");
      return `<section class="q-blk"><h4>${esc(ev === "o_diam" ? TT.evO : TT.evH)} · n ${n}</h4><table class="q-tab nw"><tr><td>bind ${bind}</td><td>= ${esc(parts("bind"))}</td></tr><tr><td>attractor ${attr}</td><td>= ${esc(parts("attractor"))}</td></tr>${oth ? `<tr><td>${esc(T.slOther)} ${oth}</td><td>= ${esc(othp)}</td></tr>` : ""}</table></section>`;
    };
    return `<p class="q-note" style="margin:0 0 6px">${esc(T.slBkHead)}</p>` + one("o_diam") + one("h_diam") + `<p class="q-note">${esc(T.slBkNote)}</p>`;
  };
  SCENES.__q = Q;
})();
