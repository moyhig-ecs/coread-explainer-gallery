// figure.js — the EXAMPLE content of the figure (template): what to draw in each state, from DATA. Replace this file for a new subject; state_machine.js (the engine) does not change.
// Contract with the engine:  FIGURE.states = the table of states (chapter names must be the ones of config.json) · FIGURE.ctx(S) = the numbers the texts need (Q) · FIGURE.draw(S, A, el) draws the picture ·
// FIGURE.keys[mode] = the legend keys · FIGURE.tRange(S) = [lo, hi] of the position slider. Every number comes from DATA (pack.json); nothing is typed here.
const FIGURE = (() => {
  const VW = 1180, VH = 700, K0 = 1.7, PI = Math.PI;
  const P = DATA.positions, NL = DATA.layers, SW = 26, ZP = 24, XL = P * SW, ZL = (NL - 1) * ZP, DM = 140, YT = DM + 36;       // 3 axes: x = position, z = layer, y = rank (log; rank 1 at the front, DM at 1000, fog beyond)
  const depthY = (r) => (DM * Math.log10(Math.max(1, Math.min(r, 1000)))) / 3;
  const n1 = (v) => Math.round(v * 10) / 10;
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  // the camera: the kit's isometric formula with free azimuth / elevation / zoom (c = the point that stays at the centre)
  function proj(az, el, zoom, px, c) {
    const a = (az * PI) / 180, e = (el * PI) / 180, sA = Math.sin(a), cA = Math.cos(a), sE = Math.sin(e), cE = Math.cos(e), k = K0 * zoom;
    const ox = VW / 2 + px - (c[0] * sA - c[1] * cA) * k, oy = VH / 2 + 14 - ((c[0] * cA + c[1] * sA) * sE - c[2] * cE) * k;
    return { p: (x, y, z) => [ox + (x * sA - y * cA) * k, oy + ((x * cA + y * sA) * sE - z * cE) * k], az };
  }
  const quad = (Pj, a, b, c, d) => "M" + [a, b, c, d].map((v) => Pj.p(...v).map(n1).join(" ")).join("L") + "Z";
  const seg = (Pj, a, b) => "M" + Pj.p(...a).map(n1).join(" ") + "L" + Pj.p(...b).map(n1).join(" ");
  const narrow = () => matchMedia("(max-width:560px)").matches;   // the phone: the plate is limited by its WIDTH, so the canvas is cropped to the picture and the tags are larger (figure.css)
  const row = (k) => DATA.rows[k];
  const keyRow = (k) => ({ name: k, label: row(k).label, keyPos: row(k).keyPos, keyWord: row(k).keyWord, keyRank: row(k).keyRank });

  // ---- a body = one row's volume drawn into the shared path lists (PATHS) and tag list (TAGS). Two bodies in ONE projection (a pair) just call it twice with different dx / dy:
  //      the paths are concatenated, so the camera is shared and turning one turns both. (Limit: the two bodies are not depth-sorted against each other; keep them apart.)
  function body(o, Pj, PATHS, TAGS) {
    const { key, dx = 0, dy = 0, t, title } = o, cls = key === "B" ? "b" : "a", r = row(key), bm = r.bandMedian, X = (p) => (p + 0.5) * SW;
    const Q = { p: (x, y, z) => { const q = Pj.p(x + dx, y, z); return [q[0], q[1] + dy]; } };
    const add = (name, d) => { PATHS[name] = (PATHS[name] || "") + d; };
    const tag = (pt, text, c = "", ox = 0, oy = 0, anchor = "start") => TAGS.push(`<text class="fig-tag ${c}" x="${n1(pt[0] + ox)}" y="${n1(pt[1] + oy)}" text-anchor="${anchor}">${esc(text)}</text>`);
    add("fig-floor", quad(Q, [0, 0, 0], [XL, 0, 0], [XL, -YT, 0], [0, -YT, 0]));
    add("fig-fog", quad(Q, [0, -DM, 0], [XL, -DM, 0], [XL, -YT, 0], [0, -YT, 0]));                                    // the fog: below the 1000th (clipped values; drawn as fog, never as "sunk")
    add("fig-wall", quad(Q, [0, -YT, 0], [XL, -YT, 0], [XL, -YT, ZL], [0, -YT, ZL]));
    const [lo, hi] = DATA.band;
    for (let l = 0; l < NL; l++) add(l >= lo && l <= hi ? "fig-plate band" : "fig-plate", quad(Q, [0, 0, l * ZP], [XL, 0, l * ZP], [XL, -YT, l * ZP], [0, -YT, l * ZP]));   // the plates (layers); the record band is the thick one
    const zMid = ((lo + hi) / 2) * ZP, pts = bm.map((m, p) => (m > 1000 ? null : Q.p(X(p), -depthY(m), zMid)));
    bm.forEach((m, p) => { if (m <= 1000 && m > 1) add(`fig-stem ${cls}`, seg(Q, [X(p), 0, zMid], [X(p), -depthY(m), zMid])); });          // stems: the band median at each position (the depth = the rank)
    let d = "", pen = false; pts.forEach((q) => { if (!q) { pen = false; return; } d += (pen ? "L" : "M") + q.map(n1).join(" "); pen = true; }); add(`fig-trace ${cls}`, d);
    add("fig-face", quad(Q, [X(r.keyPos), 0, 0], [X(r.keyPos), -YT, 0], [X(r.keyPos), -YT, ZL], [X(r.keyPos), 0, ZL]));                              // the face of the key position (the alignment is declared, not implied)
    const tt = Math.max(0, Math.min(P - 1, t)); if (pts[tt]) TAGS.push(`<circle class="fig-dot ${cls}" cx="${n1(pts[tt][0])}" cy="${n1(pts[tt][1])}" r="4"/>`);
    tag(Q.p(X(tt), 9, 0), `t ${tt}: ${bm[tt] > 1000 ? "> 1000" : "rank " + bm[tt]}`, "", 0, 24, "middle");
    tag(Q.p(X(r.keyPos), 9, 0), `${r.keyWord} (key position ${r.keyPos})`, "", 0, 42, "middle");
    for (const rk of [1, 10, 100, 1000]) tag(Q.p(XL, -(rk === 1 ? 0 : depthY(rk)), 0), `rank ${rk}`, "muted", 10, 14);
    for (let p = 0; p < P; p += 3) tag(Q.p(X(p), 9, 0), String(p), "muted", 0, 12, "middle");
    if (title) tag(Q.p(XL / 2, -YT, ZL), title, "title", 0, -18, "middle");
  }
  const MODES = {
    vol(S, A) { const Pj = proj(A("az"), A("el"), A("zoom"), A("px"), [XL / 2, -YT / 2, ZL / 2]), PATHS = {}, TAGS = []; body({ key: "A", t: S.t, title: `row A · ${row("A").label}` }, Pj, PATHS, TAGS); return paths(PATHS) + TAGS.join(""); },
    pair(S, A, side) {   // side by side in the video frame (the plate is limited by its height); stacked on the desk and the phone (limited by its width)
      const GAP = 90, zoom = A("zoom") * (side ? 0.9 : 0.78), a = (A("az") * PI) / 180, e = (A("el") * PI) / 180, k = K0 * zoom, STEP = 300;
      const Pj = proj(A("az"), A("el"), zoom, A("px"), [side ? (XL + GAP + XL) / 2 : XL / 2, -YT / 2, ZL / 2]), PATHS = {}, TAGS = [];
      const where = side ? [{ dx: 0, dy: 0 }, { dx: XL + GAP, dy: -(XL + GAP) * Math.cos(a) * Math.sin(e) * k }] : [{ dx: 0, dy: -STEP / 2 }, { dx: 0, dy: STEP / 2 }];   // the second body is lifted by the tilt of the x axis so that both stand on one baseline
      body({ key: "A", t: S.t, title: `row A · ${row("A").label}`, ...where[0] }, Pj, PATHS, TAGS); body({ key: "B", t: S.t, title: `row B · ${row("B").label}`, ...where[1] }, Pj, PATHS, TAGS);
      return paths(PATHS) + TAGS.join("");
    },
    plane(S) {   // a plane chart on the plate's own canvas: a table and bars (log scale)
      const L = (ja, en) => (S.lang === "en" ? en : ja), ks = Object.keys(DATA.rows), BW = narrow() ? 280 : 520; let s = `<text x="60" y="60" class="fig-h">${esc(L("要の位置の順位(帯の median)", "Rank at the key position (band median)"))}</text>`;
      ks.forEach((k, i) => { const r = row(k), y = 130 + i * 70, w = BW * (1 - Math.log10(Math.min(1000, r.keyRank)) / 3 * 0.95); s += `<text x="60" y="${y}" class="fig-c">${esc(`row ${k} · ${r.label} · ${r.keyWord} (t ${r.keyPos})`)}</text><rect x="60" y="${y + 12}" width="${n1(w)}" height="22" class="fig-bar ${k === "B" ? "b" : "a"}"/><text x="${n1(60 + w + 12)}" y="${y + 30}" class="fig-c">${esc(L(`${r.keyRank} 位`, `rank ${r.keyRank}`))}</text>`; });
      const note = L(["2 行・1 位置。量としては言わない。", "棒が長い = 手前(1 位に近い)。"], ["Two rows, one position; not said as a quantity.", "A longer bar = nearer the front (nearer rank 1)."]);
      return s + note.map((t, i) => `<text x="60" y="${320 + i * 26}" class="fig-m">${esc(t)}</text>`).join("");
    },
    ledger() { return ""; },   // html: fig-ledger is filled by ledgerHtml()
  };
  const paths = (PATHS) => Object.entries(PATHS).map(([c, d]) => `<path class="${c}" d="${d}"/>`).join("");
  const ledgerHtml = (S) => { const T = I18N[S.lang].ledger, by = (lv) => DATA.statements.filter((x) => x.level === lv).map((x) => `<article><b>${T.tag[lv]}</b> ${esc(x.text)}<span class="src">${esc(x.src)}</span></article>`).join(""); return ["L1", "L3", "x"].map((lv, i) => `<section><h3>${esc(T.cols[i])}</h3>${by(lv)}</section>`).join(""); };
  return {
    states: [   // the table of states: chapter + mode + camera [az, el, zoom, px] (+ options). The chapter names must be those of config.json.
      { chapter: "scene", mode: "vol", cam: [58, 24, 1.0, 0], t: "focus", auto: "sweep" },
      { chapter: "body", mode: "pair", cam: [70, 22, 0.85, 0], t: "focus" },
      { chapter: "body", mode: "plane", cam: [58, 24, 1, 0], t: "focus" },
      { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: "focus" },
    ],
    keys: { vol: ["a", "fog", "fp"], pair: ["a", "b", "fog", "fp"], plane: ["a", "b"], ledger: [] },
    tRange: () => [0, P - 1], focus: () => row("A").keyPos,
    ctx(S) { const bm = (k) => row(k).bandMedian[Math.max(0, Math.min(P - 1, S.t))], n = (lv) => DATA.statements.filter((x) => x.level === lv).length; return { t: S.t, rowA: keyRow("A"), rowB: keyRow("B"), here: bm("A"), hereB: bm("B"), n: { L1: n("L1"), L3: n("L3"), x: n("x") } }; },
    draw(S, A, el, root) {
      const mode = FIGURE.states[S.state].mode, side = root.dataset.video === "1";
      const vb = !narrow() ? [0, 0, VW, VH] : mode === "plane" ? [0, 0, 780, 420] : mode === "pair" ? [170, 40, 850, 660] : [170, 110, 850, 500];
      el.svg.setAttribute("viewBox", vb.join(" "));
      el.pic.innerHTML = MODES[mode](S, A, side);
      el.ledger.innerHTML = mode === "ledger" ? ledgerHtml(S) : "";
    },
  };
})();
