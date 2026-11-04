// figure.js — what to draw in each state of the moy-2 reflection-tool line explainer, from DATA (pack + the kit's art). Every number comes from DATA; nothing is typed here.
// Contract with the engine: FIGURE.states · FIGURE.ctx(S) · FIGURE.draw(S, el, root) · FIGURE.keys[mode] · FIGURE.pick(S, x, y) · FIGURE.rowsOf(S) · FIGURE.allRows · FIGURE.armIds
// Words: the names of the arms, classes and marks live in ONE place (I18N[lang].names); the short words of the charts are L(ja, en) pairs here.
const FIGURE = (() => {
  const ARMS = DATA.arms, AID = ARMS.map((a) => a.id), armOf = (id) => ARMS.find((a) => a.id === id), ART = DATA.art;
  const rowOf = (id) => { const [a, k] = id.split(":"); const arm = armOf(a); return arm && arm.rows.find((r) => r.k === k); };
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const n3 = (v) => (v == null ? "—" : Number(v).toFixed(3)), sgn = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3), sgn4 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(4);
  const int = (v) => Number(v).toLocaleString("en-US");
  const NM = (S) => I18N[S.lang].names, L = (S, ja, en) => (S.lang === "en" ? en : ja);
  const narrow = () => matchMedia("(max-width:560px)").matches;
  const allRows = ARMS.flatMap((a) => a.rows.map((r) => `${a.id}:${r.k}`));
  const FILTERS = { "": () => true, calc: (r) => r.calc, typ: (r) => r.rej, o127: (r, a) => a === "olm127" };
  const states = [
    { chapter: "scene", mode: "slips", view: "stack" },                // v1.1 F2: A0 = the two real rows (the first 10 seconds) · v1.2 G1: + the band under them (view "stack" = html over svg)
    { chapter: "scene", mode: "board", view: "split" },                // v1.1 F2: A1 = the drafting board
    { chapter: "tool", mode: "tools", view: "html" },
    { chapter: "tool", mode: "instr", view: "html" },
    { chapter: "tool", mode: "gate", view: "svg" },
    { chapter: "tool", mode: "bands", view: "svg" },
    { chapter: "arms", mode: "scale", view: "split", pick: "arm", arm: "olm125" },
    { chapter: "arms", mode: "side", view: "svg" },
    { chapter: "arms", mode: "rack", view: "split", pick: "row", sel: "olm125:b1_j17", filter: "" },
    { chapter: "arms", mode: "fisher", view: "svg" },                  // v1.1 F4: C3 = Fisher between neighbouring arms (reference)
    { chapter: "calc", mode: "split", view: "svg" },
    { chapter: "calc", mode: "rack", view: "split", pick: "row", sel: "olm125:b1_j17", filter: "calc" },
    { chapter: "calc", mode: "rack", view: "split", pick: "row", sel: "olm124:b2_j07", filter: "typ" },
    { chapter: "calc", mode: "rack", view: "split", pick: "row", sel: "olm127:b2_j08", filter: "o127" },
    { chapter: "shape", mode: "equal", view: "svg" },
    { chapter: "lineage", mode: "lineage", view: "split" },
    { chapter: "lineage", mode: "same", view: "svg" },
    { chapter: "next", mode: "question", view: "html" },
    { chapter: "next", mode: "nextq", view: "html" },
    { chapter: "ledger", mode: "ledger", view: "ledger" },
  ];
  const rowsOf = (S) => { const f = FILTERS[states[S.state].filter || ""] || FILTERS[""]; return ARMS.flatMap((a) => a.rows.filter((r) => f(r, a.id)).map((r) => `${a.id}:${r.k}`)); };

  // ---------------------------------------------------------------- svg helpers (plane charts)
  const T = (x, y, s, c = "fig-c", a = "start", extra = "") => `<text x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" class="${c}" text-anchor="${a}"${extra}>${esc(s)}</text>`;
  const LN = (x1, y1, x2, y2, c) => `<path class="${c}" d="M${(+x1).toFixed(1)} ${(+y1).toFixed(1)}L${(+x2).toFixed(1)} ${(+y2).toFixed(1)}"/>`;
  const RC = (x, y, w, h, c) => `<rect x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" width="${Math.max(0, w).toFixed(1)}" height="${Math.max(0, h).toFixed(1)}" class="${c}"/>`;
  const CI = (x, y, r, c) => `<circle cx="${(+x).toFixed(1)}" cy="${(+y).toFixed(1)}" r="${r}" class="${c}"/>`;
  const layout = (root, view) => { const nar = narrow(), vid = root.dataset.video === "1"; const W = nar ? 560 : view === "split" ? 800 : 1180; return { nar, vid, W, f: nar ? 17 : vid ? 13 : 14, armLbl: (S, a) => (nar ? a.id.replace("olm", "") : a.id) }; };
  const armName = (S, a) => NM(S).tool[a.tool];

  // C0: the seven arms on ONE scale (0 .. 0.4): v3 = filled dot (the verdict's instrument), v6 = ring (reference); each arm's own band edges (from its PREREG) as dashed ticks; G1-failed arms carry "no verdict"
  function scale(S, Lo) {
    const { W, f, nar } = Lo, x0 = nar ? 64 : 250, x1 = W - (nar ? 18 : 40), X = (v) => x0 + (v / 0.4) * (x1 - x0), rowH = nar ? 118 : 74, y0 = nar ? 84 : 70;
    const TTL = L(S, "証明の欄の線対称の率(v3 = 塗り・判定 / v6 = 輪・参考)", "Rate of the line symmetry in the proof field (v3 = filled, verdict / v6 = ring, reference)"); Lo.title = TTL; let s = nar ? "" : T(20, 24, TTL, "fig-h");
    for (let t = 0; t <= 4; t++) { const v = t / 10; s += LN(X(v), y0 - 18, X(v), y0 + rowH * 7 - 30, "fig-grid") + T(X(v), y0 - 24, v.toFixed(1), "fig-m", "middle"); }
    ARMS.forEach((a, i) => {
      const y = y0 + i * rowH, A = a.agg, v = DATA.verdicts[a.id], sel = a.id === S.arm, mid = y + 16;
      if (sel) s += RC(nar ? 2 : 10, y - 6, W - (nar ? 4 : 20), rowH - 10, "fig-selrow");
      s += T(nar ? 8 : 20, y + 12, Lo.armLbl(S, a), "fig-c strong") + T(nar ? 8 : 20, y + 12 + f * 1.25, nar ? "" : armName(S, a), "fig-m");
      s += LN(x0, mid, x1, mid, "fig-axis");
      if (v) for (const [name, lo, hi] of v.segs) { if (lo != null && lo > 0 && lo < 0.4) s += LN(X(lo), mid - 9, X(lo), mid + 9, "fig-edge"); if (hi != null && hi < 0.4 && hi > 0) s += LN(X(hi), mid - 9, X(hi), mid + 9, "fig-edge"); }
      if (v) (DATA.edges[a.id] || []).filter(([e]) => e > 0 && e < 0.4).forEach(([e, txt], k) => (s += T(X(e), mid + (nar ? (k % 2 ? 74 : 52) : 26), txt, "fig-m rk-edge", "middle")));   // v1.2 G8: the edge printed beside its tick
      s += CI(X(A.LN6_rate), mid, 7.5, "fig-v6") + CI(X(A.LN3_rate), mid, 6, a.g1fail ? "fig-v3 nv" : "fig-v3");
      const lab = `${A.LN3} / ${A.n_proof} = ${n3(A.LN3_rate)}`, tag = a.g1fail ? L(S, " · G1 ✗ 判定なし", " · G1 ✗ no verdict") : v ? ` · ${NM(S).verdict[v.read] || v.read}` : L(S, " · 基準(帯なし)", " · baseline (no band)");
      const txt = lab + (nar ? "" : tag), right = X(Math.max(A.LN3_rate, A.LN6_rate)) + 14, room = W - right, need = txt.length * f * 0.62;
      s += room > need ? T(right, mid - 10, txt, a.g1fail ? "fig-c nv" : "fig-c") : T(X(Math.min(A.LN3_rate, A.LN6_rate)) - 14, mid - 10, txt, a.g1fail ? "fig-c nv" : "fig-c", "end");
      if (nar) s += T(x0, mid + 26, tag.replace(/^ · /, ""), a.g1fail ? "fig-m nv" : "fig-m");
    });
    return { svg: s, vb: [0, 0, W, y0 + rowH * 7 - 10] };
  }
  function pickArm(S, x, y) { const Lo = { nar: narrow() }, rowH = Lo.nar ? 118 : 74, y0 = Lo.nar ? 84 : 70; const i = Math.floor((y - y0 + 10) / rowH); return i >= 0 && i < ARMS.length ? AID[i] : null; }

  // B2: the gate G1 = conjecture parsed >= 0.75 (45 / 60); 0.80 was the line of olm119 / olm122
  function gate(S, Lo) {
    const { W, f, nar } = Lo, x0 = nar ? 70 : 300, x1 = W - (nar ? 170 : 60), X = (v) => x0 + v * (x1 - x0), rowH = nar ? 64 : 56, y0 = 64;
    const TTL = L(S, "conjecture が取れた行 / 60(関門 G1)", "Rows whose conjecture was parsed / 60 (gate G1)"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    for (const g of [DATA.g075, DATA.g080]) s += LN(X(g), y0 - 14, X(g), y0 + rowH * 7 - 18, g === DATA.g075 ? "fig-gate" : "fig-gate old") + (g === DATA.g075 ? T(X(g), y0 - 20, `G1 ${g.toFixed(2)}`, "fig-m", "end") : T(X(g), y0 - 20, L(S, `旧 ${g.toFixed(2)}`, `old ${g.toFixed(2)}`), "fig-m", "start"));
    ARMS.forEach((a, i) => {
      const y = y0 + i * rowH, A = a.agg, gk = DATA.gates[a.id], line = a.id === "olm119" || a.id === "olm122" ? DATA.g080 : DATA.g075;
      s += T(nar ? 8 : 20, y + 18, Lo.armLbl(S, a), "fig-c strong") + (nar ? "" : T(20, y + 18 + f * 1.2, armName(S, a), "fig-m"));
      s += RC(x0, y + 4, X(A.parsed_rate) - x0, 22, gk === false ? "fig-bar nv" : gk === undefined ? "fig-bar off" : "fig-bar");
      const msg = gk === undefined ? L(S, "(この関門の札でない)", "(not a G1 card)") : gk ? L(S, `通る(≥ ${line.toFixed(2)})`, `pass (≥ ${line.toFixed(2)})`) : L(S, `✗ 判定なし(< ${line.toFixed(2)})`, `✗ no verdict (< ${line.toFixed(2)})`);
      const tx = Math.max(X(A.parsed_rate), X(DATA.g080)) + (nar ? 10 : 14);   // v1.2 G3: clear of both dashed lines (0.75 / 0.80)
      s += T(tx, y + 21, `${A.parsed} / 60 = ${n3(A.parsed_rate)}`, "fig-c") + T(nar ? x0 : tx, y + (nar ? 46 : 21 + f * 1.25), msg, gk === false ? "fig-m nv" : "fig-m");
    });
    return { svg: s, vb: [0, 0, W, y0 + rowH * 7 + 4] };
  }
  // B3: each frozen verdict's own band (named segments, from the PREREG) with the arm's value
  function bands(S, Lo) {
    const { W, f, nar } = Lo, x0 = nar ? 16 : 300, x1 = W - (nar ? 16 : 50), X = (v) => x0 + (Math.max(0, Math.min(0.4, v)) / 0.4) * (x1 - x0), rowH = nar ? 124 : 92, y0 = 84;
    const list = ["olm117", "olm119", "olm122", "olm124", "olm125", "olm127"];
    const TTL = L(S, "凍結の判定の帯(PREREG の規則)と線対称の率(v3)", "The frozen verdict bands (PREREG rules) and the line-symmetry rate (v3)"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    list.forEach((id, i) => {
      const a = armOf(id), v = DATA.verdicts[id], y = y0 + i * rowH, top = nar ? y + 50 : y;
      s += T(nar ? 8 : 20, y + 14, `${Lo.armLbl(S, a)} · ${armName(S, a)}`, "fig-c strong") + (nar ? "" : T(20, y + 14 + f * 1.25, L(S, `札 ${v.band} の Q1`, `card ${v.band} Q1`), "fig-m"));
      (DATA.edges[id] || []).filter(([e]) => e > 0 && e < 0.4).forEach(([e, txt]) => (s += X(e) - x0 < 24 ? T(x0, top - 5, txt, "fig-m rk-edge", "start") : T(X(e), top - 5, txt, "fig-m rk-edge", "middle")));   // v1.2 G8: each edge of the card's PREREG printed
      v.segs.forEach(([name, lo, hi], k) => {
        const a0 = X(lo == null ? 0 : lo), a1 = X(hi == null ? 0.4 : hi);
        s += RC(a0, top, a1 - a0, 26, `fig-seg s${k % 2}${!a.g1fail && name === v.read ? " hit" : ""}`);
        if (a1 - a0 > (nar ? 40 : 46)) s += T((a0 + a1) / 2, top + 18, NM(S).verdict[name] || name, "fig-m", "middle");
      });
      s += LN(X(a.agg.LN3_rate), top - 6, X(a.agg.LN3_rate), top + 32, a.g1fail ? "fig-mark nv" : "fig-mark");
      const lab = `${n3(a.agg.LN3_rate)} → ${a.g1fail ? L(S, "判定なし(G1 ✗)・参考の位置 = " + (NM(S).verdict[v.calc] || v.calc), "no verdict (G1 ✗) · reference position = " + (NM(S).verdict[v.calc] || v.calc)) : NM(S).verdict[v.read] || v.read}`;
      const ov = id === "olm127" ? L(S, "(残る は 0.165 から・重なり 0.165〜0.168 は 戻る が先)", " (stays from 0.165; the overlap 0.165–0.168 goes to returns)") : "";
      s += T(nar ? 8 : x0, top + 26 + f * 1.4, lab + (nar ? "" : ov), a.g1fail ? "fig-c nv" : "fig-c") + (nar && ov ? T(8, top + 26 + f * 2.7, ov.trim(), "fig-m nv") : "");
    });
    return { svg: s, vb: [0, 0, W, y0 + rowH * list.length + 4] };
  }
  // C3 (v1.1 F4): two-sided Fisher exact p between neighbouring arms, counted by the pack from the rows (L2) and set against the RESULT literals (L1). Reference only: not frozen, verdicts are the bands, no correction for multiple comparisons.
  function fisher(S, Lo) {
    const { W, f, nar } = Lo, FR = DATA.fisher, x0 = nar ? 16 : 520, x1 = W - (nar ? 150 : 210), X = (v) => x0 + Math.max(0, Math.min(1, v)) * (x1 - x0), rowH = nar ? 96 : 66, y0 = nar ? 64 : 84;
    const nm = (id) => (nar ? { pool_f: L(S, "式だけ pool", "formula pool"), pool_i: L(S, "指示 pool", "instr. pool") } : { pool_f: L(S, "式だけ pool(122 + 124)", "formula-only pool (122 + 124)"), pool_i: L(S, "指示 pool(125 + 127)", "instruction pool (125 + 127)") })[id] || id;
    const TTL = L(S, "隣り合う腕の Fisher の正確確率検定(両側・証明の欄の線対称 v3・参考)", "Fisher exact tests between neighbouring arms (two-sided; line symmetry v3 in the proof field; reference)"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    for (const v of [0, 0.25, 0.5, 0.75, 1]) s += LN(X(v), y0 - 16, X(v), y0 + rowH * FR.length - 20, "fig-grid") + T(X(v), y0 - 22, v === 0 ? "0" : v.toFixed(2).replace(/0$/, ""), "fig-m", "middle");
    s += LN(X(0.05), y0 - 16, X(0.05), y0 + rowH * FR.length - 20, "fig-ref05") + T(X(0.05) + 6, y0 + rowH * FR.length - 4, L(S, "0.05(参考の目盛り)", "0.05 (reference tick)"), "fig-m");
    FR.forEach((r, i) => {
      const y = y0 + i * rowH, lab = `${nm(r.x)} ${r.kx[0]} / ${r.kx[1]} ${L(S, "対", "vs")} ${nm(r.y)} ${r.ky[0]} / ${r.ky[1]}`, top = nar ? y + f * 1.3 : y;
      s += T(nar ? 8 : 20, y + 16, lab, "fig-c strong") + (nar ? "" : T(20, y + 16 + f * 1.3, L(S, `出所の文 ${r.src} = p ${r.lit_s}`, `as written in ${r.src}: p ${r.lit_s}`), "fig-m"));
      s += RC(x0, top + 2, X(r.p) - x0, 20, "fig-bar") + T(Math.max(X(r.p), X(0.05)) + 8, top + 17, `p ${r.p.toFixed(r.p < 0.1 ? 4 : 3)}`, "fig-c");
      if (nar) s += T(8, top + 44, L(S, `出所の文 ${r.src} = p ${r.lit_s}`, `${r.src}: p ${r.lit_s}`), "fig-m");
    });
    const up = FR.filter((r) => r.p >= 0.05).length, dn = FR.filter((r) => r.p < 0.05), fy = y0 + rowH * FR.length + (nar ? 30 : 34);   // v1.2 G7
    const g7 = L(S, [`${FR.length} 対のうち ${up} 対は参考の目盛り(0.05)の上・${dn.length} 対(${dn.map((r) => `${nm(r.x)} ${r.kx[0]} / ${r.kx[1]} 対 ${nm(r.y)} ${r.ky[0]} / ${r.ky[1]}`).join("・")})は下。`, "参考であって判定ではなく、多重比較は補正していない。"],
      [`Of the ${FR.length} pairs, ${up} lie above the reference tick (0.05) and ${dn.length} (${dn.map((r) => `${nm(r.x)} ${r.kx[0]} / ${r.kx[1]} vs ${nm(r.y)} ${r.ky[0]} / ${r.ky[1]}`).join(" · ")}) below.`, "A reference, not a verdict; no correction for multiple comparisons."]);
    const g7n = L(S, [`${FR.length} 対のうち ${up} 対は参考の目盛り(0.05)の上・`, `${dn.length} 対(${dn.map((r) => `${nm(r.x)} ${r.kx[0]} / ${r.kx[1]} 対 ${nm(r.y)} ${r.ky[0]} / ${r.ky[1]}`).join("・")})は下。`, "参考であって判定ではなく、", "多重比較は補正していない。"],
      [`Of the ${FR.length} pairs, ${up} lie above the reference tick (0.05)`, `and ${dn.length} (${dn.map((r) => `${nm(r.x)} ${r.kx[0]} / ${r.kx[1]} vs ${nm(r.y)} ${r.ky[0]} / ${r.ky[1]}`).join(" · ")}) below.`, "A reference, not a verdict;", "no correction for multiple comparisons."]);
    (nar ? g7n : [g7.join(L(S, "", " "))]).forEach((line, i) => (s += T(nar ? 8 : 20, fy + i * (nar ? 26 : 22), line, "fig-c strong fx-g7")));
    return { svg: s, vb: [0, 0, W, fy + (nar ? 26 * 3 + 16 : 14)] };
  }
  // C1: the other columns of the table, per arm (descriptive)
  function side(S, Lo) {
    const { W, f, nar } = Lo;
    const cols = [["CALC_rate", L(S, "式を数値で使った / 60", "used the formula / 60"), (A) => `${A.CALC}`], ["TN", L(S, "道具の名指し / 60", "named the tool / 60"), (A) => `${A.TN}`, 60], ["MIDO3_rate", L(S, "MIDO3(偽)/ 取れた", "MIDO3 (false) / parsed"), (A) => n3(A.MIDO3_rate)], ["EQ_rate", L(S, "EQ(真)/ 取れた", "EQ (true) / parsed"), (A) => n3(A.EQ_rate)], ["OUT3_rate", L(S, "外接線の印 v3 / 証明", "outer marker v3 / proof"), (A) => `${A.OUT3} / ${A.n_proof}`]];
    const cw = nar ? (W - 80) / 2 : (W - 280) / cols.length, x0 = nar ? 70 : 280, rowH = nar ? 40 : 52, y0 = nar ? 80 : 92;
    const TTL = L(S, "同じ 60 行の、ほかの列(記述)", "The other columns of the same 60 rows (descriptive)"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    const show = nar ? cols.slice(0, 2) : cols;
    show.forEach(([k, name], c) => { const cx = x0 + c * cw; s += T(cx, y0 - 30, name, "fig-m"); });
    ARMS.forEach((a, i) => {
      const y = y0 + i * rowH, A = a.agg;
      s += T(nar ? 8 : 20, y + 14, Lo.armLbl(S, a), "fig-c strong") + (nar ? "" : T(110, y + 14, armName(S, a), "fig-m"));
      show.forEach(([k, , txt, den], c) => { const cx = x0 + c * cw, v = den ? A[k] / den : A[k], w = (cw - (nar ? 130 : 70)) * Math.min(1, v / 0.8);
        s += RC(cx, y, w, 18, `fig-bar${k === "MIDO3_rate" ? " mido" : k === "EQ_rate" ? " eq" : ""}${a.g1fail ? " nv" : ""}`) + T(cx + w + 6, y + 14, k === "CALC_rate" ? `${txt(A)} = ${n3(A.CALC_rate)}` : txt(A), "fig-c"); });
    });
    return { svg: s, vb: [0, 0, W, y0 + rowH * 7 + 8] };
  }
  // D0: calc rows vs the others: the proof field's line symmetry, the reject rate inside the calc rows, the T medians
  function split(S, Lo) {
    const { W, f, nar } = Lo, list = ARMS.filter((a) => a.agg.CALC > 0), x0 = nar ? 70 : 300, cw = nar ? (W - 80) / 2 : 200, rowH = nar ? 58 : 66, y0 = 96;
    const TTL = L(S, "計算した行 / しない行で割った、証明の欄の線対称(v3)", "Line symmetry in the proof field (v3), split by rows that used the formula"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    const heads = [L(S, "計算した行", "calc rows"), L(S, "計算しない行", "non-calc rows"), L(S, "退け REJ6(計算した行)", "reject REJ6 (calc rows)"), L(S, "T の中央値(計算 / しない)", "median T (calc / non-calc)")];
    (nar ? heads.slice(0, 2) : heads).forEach((h, c) => (s += T(x0 + c * cw, y0 - 34, h, "fig-m")));
    list.forEach((a, i) => {
      const y = y0 + i * rowH, A = a.agg, cs = A.calc_split, ns = A.noncalc_split;
      s += T(nar ? 8 : 20, y + 14, Lo.armLbl(S, a), "fig-c strong") + (nar ? "" : T(20, y + 14 + f * 1.2, armName(S, a), "fig-m"));
      [[cs.LN3, cs.n_proof], [ns.LN3, ns.n_proof]].forEach(([k, n], c) => { const cx = x0 + c * cw, w = (cw - 90) * (n ? k / n : 0) / 0.4; s += RC(cx, y, Math.min(cw - 90, w), 18, `fig-bar${a.g1fail ? " nv" : ""}`) + T(cx + Math.min(cw - 90, w) + 6, y + 14, `${k} / ${n}`, "fig-c"); });
      if (!nar) { s += T(x0 + 2 * cw, y + 14, `${A.REJ_calc} / ${A.CALC}` + (A.REJ !== A.REJ_calc ? L(S, `(全行 ${A.REJ})`, ` (all rows ${A.REJ})`) : ""), "fig-c");
        s += T(x0 + 3 * cw, y + 14, `${int(A.T_med_calc)} / ${int(A.T_med_noncalc)}`, "fig-c"); }
      else s += T(x0, y + 40, L(S, `退け ${A.REJ_calc} / ${A.CALC}・T ${int(A.T_med_calc)} / ${int(A.T_med_noncalc)}`, `reject ${A.REJ_calc} / ${A.CALC} · T ${int(A.T_med_calc)} / ${int(A.T_med_noncalc)}`), "fig-m");
    });
    return { svg: s, vb: [0, 0, W, y0 + rowH * list.length + 6] };
  }
  // E0: the equal-radii control (olm117) against the general figure (olm113): the frozen olm118 verdicts (v3)
  function equal(S, Lo) {
    const { W, f, nar } = Lo, a = armOf("olm113").agg, b = armOf("olm117").agg, F = DATA.frozen.o118;
    const rows = [[L(S, "線対称(証明の欄・v3)", "line symmetry (proof, v3)"), a.LN3, a.n_proof, b.LN3, b.n_proof, a.LN3_rate, b.LN3_rate, F.Q1], [L(S, "点対称(証明の欄・v3)", "point symmetry (proof, v3)"), a.PT, a.n_proof, b.PT, b.n_proof, a.PT_rate, b.PT_rate, F.Q2],
      [L(S, "外接線の印(証明の欄・v3)", "outer marker (proof, v3)"), a.OUT3, a.n_proof, b.OUT3, b.n_proof, a.OUT3_rate, b.OUT3_rate, F.Q3], [L(S, "MIDO3(取れた行・記述)", "MIDO3 (parsed rows, descriptive)"), a.cls.MIDO3, a.parsed, b.cls.MIDO3, b.parsed, a.MIDO3_rate, b.MIDO3_rate, null]];
    const x0 = nar ? 16 : 360, x1 = W - (nar ? 250 : 60), X = (v) => x0 + v * (x1 - x0), rowH = nar ? 120 : 96, y0 = 84;
    const TTL = L(S, "一般の図(olm113)と、半径を揃えた図(olm117)", "The general figure (olm113) and the equal-radii figure (olm117)"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    for (let t = 0; t <= 10; t += 2) s += LN(X(t / 10), y0 - 22, X(t / 10), y0 + rowH * 4 - 20, "fig-grid") + T(X(t / 10), y0 - 28, (t / 10).toFixed(1), "fig-m", "middle");
    rows.forEach(([name, k1, n1, k2, n2, r1, r2, fz], i) => {
      const y = y0 + i * rowH, top = nar ? y + 26 : y;
      s += T(nar ? 8 : 20, y + 16, name, "fig-c strong") + (nar ? "" : T(20, y + 16 + f * 1.3, fz ? L(S, `olm118: Δ ${sgn4(fz[0])} → ${NM(S).verdict[fz[1]] || fz[1]}`, `olm118: Δ ${sgn4(fz[0])} → ${NM(S).verdict[fz[1]] || fz[1]}`) : L(S, "凍結の判定は olm117 の札(記述)", "verdict on card olm117 (descriptive)"), "fig-m"));
      s += RC(x0, top, X(r1) - x0, 18, i === 3 ? "fig-bar mido" : "fig-bar") + T(X(r1) + 6, top + 14, `olm113 ${k1} / ${n1} = ${n3(r1)}`, "fig-c");   // v1.2 G2
      s += RC(x0, top + 26, X(r2) - x0, 18, i === 3 ? "fig-bar mido alt2" : "fig-bar alt") + T(X(r2) + 6, top + 40, `olm117 ${k2} / ${n2} = ${n3(r2)}`, "fig-c");
      if (nar && fz) s += T(8, top + 66, `olm118: Δ ${sgn4(fz[0])} → ${NM(S).verdict[fz[1]] || fz[1]}`, "fig-m");
    });
    return { svg: s, vb: [0, 0, W, y0 + rowH * 4 + 4] };
  }
  // F0: the instrument lineage v3 -> v6 and the band of olm118 Q3 (outer marker, equal - general) on each version
  function lineage(S, Lo) {
    const { W, f, nar } = Lo, Lg = DATA.lineage, vs = ["v3", "v4", "v5", "v6"], cw = (W - (nar ? 20 : 120)) / 4, x0 = nar ? 10 : 80, y0 = 90;
    const TTL = L(S, "計器の系譜: 較正の行数と olm118 Q3 の帯", "The instrument lineage: calibration rows and the olm118 Q3 band"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    const H = nar ? 120 : 150, maxC = 144;
    vs.forEach((v, i) => {
      const cx = x0 + i * cw + 10, n = Lg.cal[v], h = (H * n) / maxC, q = Lg.q3[i];
      s += RC(cx, y0 + H - h, cw * 0.42, h, "fig-bar") + T(cx, y0 + H - h - 8, `${v} · ${n}`, "fig-c strong");
      // the Q3 ruler: |Δ| < 0.06 = 変わらない
      const ry = y0 + H + 70, rx0 = cx, rx1 = cx + cw - 24, RX = (d) => rx0 + (d / 0.08) * (rx1 - rx0);
      s += LN(rx0, ry, rx1, ry, "fig-axis") + LN(RX(0.06), ry - 12, RX(0.06), ry + 12, "fig-edge") + T(RX(0.06), ry + 28, "0.06", "fig-m", "middle") + T(rx0, ry + 28, "0", "fig-m");
      s += CI(RX(q[1]), ry, 6.5, "fig-v3") + (nar ? T(rx0, ry - 46, sgn4(q[1]), q[2] === "間" ? "fig-c strong" : "fig-c") + T(rx0, ry - 22, NM(S).verdict[q[2]] || q[2], q[2] === "間" ? "fig-c strong" : "fig-c") : T(rx0, ry - 22, `${sgn4(q[1])} → ${NM(S).verdict[q[2]] || q[2]}`, q[2] === "間" ? "fig-c strong" : "fig-c"));
    });
    const l1 = L(S, ["olm118 Q3 = 外接線の印の率の差(olm117 − olm113)", "帯の境 |Δ| < 0.06"], ["olm118 Q3 = gap in the outer-marker rate (olm117 − olm113)", "band edge |Δ| < 0.06"]);
    const l2 = L(S, [`陰性統制 prf5(frontier の証明 ${Lg.neg.n} 本):`, `外接線の印 ${Lg.neg.outer} / ${Lg.neg.n}・点対称 + 線対称 ${Lg.neg.pt_ln} / ${Lg.neg.n}`], [`negative control prf5 (${Lg.neg.n} frontier proofs):`, `outer marker ${Lg.neg.outer} / ${Lg.neg.n} · point + line symmetry ${Lg.neg.pt_ln} / ${Lg.neg.n}`]);
    const lines = nar ? [[l1[0], "fig-m"], [l1[1], "fig-m"], [l2[0], "fig-c"], [l2[1], "fig-c"]] : [[l1.join("・").replace("・band", " · band"), "fig-m"], [l2.join(" "), "fig-c"]];
    lines.forEach(([t, c], i) => (s += T(nar ? 8 : 20, y0 + H + 128 + i * (nar ? 26 : 34), t, c)));
    return { svg: s, vb: [0, 0, W, y0 + H + 140 + lines.length * (nar ? 26 : 34)] };
  }
  // F1: v3 vs v6 rates for the five arms of olm126 and the seven frozen verdicts under both instruments
  function same(S, Lo) {
    const { W, f, nar } = Lo, list = ["olm113", "olm119", "olm122", "olm124", "olm125"], x0 = nar ? 70 : 200, x1 = W - (nar ? 230 : 700), X = (v) => x0 + (v / 0.4) * (x1 - x0), rowH = nar ? 50 : 56, y0 = 80;
    const TTL = L(S, "計器を v3 → v6 に替えた時の率と、凍結の判定", "Rates under v3 → v6, and the frozen verdicts"); Lo.title = TTL; let s = nar ? "" : T(20, 26, TTL, "fig-h");
    list.forEach((id, i) => {
      const a = armOf(id), A = a.agg, y = y0 + i * rowH;
      s += T(nar ? 8 : 20, y + 6, Lo.armLbl(S, a), "fig-c strong") + LN(X(A.LN3_rate), y, X(A.LN6_rate), y, "fig-axis") + CI(X(A.LN3_rate), y, 6, "fig-v3") + CI(X(A.LN6_rate), y, 7.5, "fig-v6");
      s += T(X(A.LN6_rate) + 14, y + 5, `${n3(A.LN3_rate)} → ${n3(A.LN6_rate)} (${sgn(A.LN6_rate - A.LN3_rate)})`, "fig-c");
    });
    const fz = DATA.lineage.frozen, v6 = DATA.lineage.v6same, keys = Object.keys(fz), tx = nar ? 10 : W - 420, ty = nar ? y0 + rowH * 5 + 30 : y0 - 6;
    s += T(tx, ty, L(S, "凍結の判定(v3) / v6 で引き直した判定", "frozen verdict (v3) / redone under v6"), "fig-m");
    keys.forEach((k, i) => { const yy = ty + 26 + i * (nar ? 26 : 30); s += T(tx, yy, k.replace("_", " "), "fig-c") + T(tx + (nar ? 220 : 220), yy, `${NM(S).verdict[fz[k]] || fz[k]} / ${NM(S).verdict[v6[k]] || v6[k]}`, fz[k] === v6[k] ? "fig-c strong" : "fig-c"); });
    const same7 = keys.filter((k) => fz[k] === v6[k]).length;
    s += T(tx, ty + 26 + keys.length * (nar ? 26 : 30) + 6, L(S, `同じ ${same7} / ${keys.length}(olm126 Q2 = ${NM(S).verdict["同じ"]})`, `the same ${same7} / ${keys.length} (olm126 Q2)`), "fig-c strong");
    return { svg: s, vb: [0, 0, W, nar ? ty + 40 + keys.length * 26 + 20 : Math.max(y0 + rowH * 5, ty + 60 + keys.length * 30)] };
  }

  // ---------------------------------------------------------------- the kit's art: board and rack (static), with tags drawn here
  let artNow = "";
  function setArt(el, which) { if (artNow === which) return; el.art.innerHTML = which ? ART[which].svg : ""; artNow = which; }
  // v1.2 G1: the band under the two rows: stage names above S1, the marks' words beside each slab (S1 above its slabs, S2 below), the row names at the left
  function slipsTags(S, Lo) {
    const tg = Object.fromEntries(ART.slips.tags.map((x) => [x.id, x])), P0 = DATA.slip0, nar = Lo.nar, fs = nar ? 32 : Lo.vid ? 16 : 17;
    const st = nar ? [L(S, "本文", "body"), L(S, "退けの文", "reject"), L(S, "証明の欄", "proof")] : [L(S, "本文(前半)", "body (first half)"), L(S, "退けの文", "the reject sentence"), L(S, "証明の欄", "the proof field")];
    const k1 = { S1: DATA.scenes.S1.key, S2: DATA.scenes.S2.key };
    const mark = (sid, si) => si === 0 ? (nar ? L(S, `計算 ✓ ${P0.refl[k1[sid]]}`, `calc ✓ ${P0.refl[k1[sid]]}`) : L(S, `■ 計算 ✓ · ${P0.refl[k1[sid]]} を折り返す`, `■ calc: reflects ${P0.refl[k1[sid]]}`)) : si === 1 ? (nar ? L(S, "退け ✓", "reject ✓") : L(S, "▬ 退け ✓ · Not the same", "▬ reject ✓ (Not the same)"))
      : sid === "S1" ? (nar ? L(S, "● 線対称 ✓", "● symm. ✓") : L(S, "● 線対称 v3 ✓", "● symmetry v3 ✓")) : (nar ? L(S, "○ なし", "○ none") : L(S, "○ 線対称の語なし", "○ no symmetry words"));
    let s = "";
    [0, 1, 2].forEach((si) => { const a = tg[`S1-${si}`]; s += T(a.top[0], a.top[1] - fs * 2.1, st[si], "fig-tag strong sl-head", "middle"); });
    ["S1", "S2"].forEach((sid) => { const a = tg[`${sid}-0`]; s += T(a.left[0] - 16, a.left[1] + fs * 0.35, nar ? sid : `${sid} ${k1[sid]}`, "fig-tag strong", "end");
      [0, 1, 2].forEach((si) => { const b = tg[`${sid}-${si}`]; s += sid === "S1" ? T(b.top[0], b.top[1] - fs * 0.7, mark(sid, si), si === 2 ? "fig-tag strong" : "fig-tag", "middle") : T(b.front[0], b.front[1] + fs * 1.25, mark(sid, si), si === 2 ? "fig-tag muted" : "fig-tag", "middle"); }); });
    return s;
  }
  function boardTags(S, Lo) {
    const g = DATA.geo, tg = Object.fromEntries(ART.board.tags.map((t) => [t.id, t.xy])), c = "fig-tag";
    // v1.3 H4: each tag is placed in a free place (placeBoard): its v1.2 offset if that is clear, else the nearest clear place around its point, joined by a leader
    const it = (id, text, dx, dy, cls = c, a = "start") => ({ id, text, cls, ax: tg[id][0], ay: tg[id][1], dx, dy, a });
    const items = [it("O3", "O3", -10, 4, c + " strong", "end"), it("Tc", "Tc", -10, -8, c + " strong", "end"), it("Th", "Th", 10, 16, c + " strong"),
      it("M", Lo.nar ? "M ≠ O3" : L(S, "M = TcTh の中点 ≠ O3", "M = midpoint of TcTh ≠ O3"), 14, 14, c + " mido"),
      it("eqTc", `${g.dTc.toFixed(3)}`, -8, -4, c + " eq", "end"), it("eqTh", `${g.dTh.toFixed(3)}`, -10, 12, c + " eq", "end"),
      it("Th_r", Lo.nar ? "Th′" : L(S, "Th′(折り返し)", "Th′ (reflection)"), 6, -16, c + " muted"), it("Tc_r", Lo.nar ? "Tc′" : L(S, "Tc′(折り返し)", "Tc′ (reflection)"), -8, 20, c + " muted", "end"),
      it("O1", "O1", 8, 18), it("O2", "O2", -8, 20, c, "end"), it("l1", "l1", 8, 6), ...(Lo.nar ? [] : [it("o12", "O1O2", 8, 16, c + " muted")]), it("c", "c", -6, 0, c + " muted", "end"), it("h1", "h1", 10, 0, c + " muted")];
    let s = "";
    for (const n of placeBoard(Lo, items)) s += (n.lead ? `<path class="fig-lead bd-leadtag" d="M${n.ax.toFixed(1)} ${n.ay.toFixed(1)}L${n.ex.toFixed(1)} ${n.ey.toFixed(1)}"/>` : "") + T(n.x, n.y, n.text, n.cls, n.anchor);
    return s;
  }
  // v1.3 H4: a free place for each board tag = its rectangle meets no line drawn on the board (circles, l1, O1O2, the radii, the blue apex segments, the reflection dashes, the rings: art.mjs keeps them as polylines),
  // no pin and no tag already placed, and stays inside the viewBox. The widths are estimated on the generous side (mono 0.62 em, other characters 1 em); the check measures the real boxes.
  function placeBoard(Lo, items) {
    const B = ART.board, fs = Lo.nar ? 23 : 14, [vx, vy, vw, vh] = Lo.nar ? [70, 170, 660, 300] : [0, 0, ...B.vb], placed = [], m = 2.5;
    const segs = B.lines.flatMap((pl) => pl.slice(1).map((q, i) => [pl[i][0], pl[i][1], q[0], q[1]]));
    const hitSeg = ([x1, y1, x2, y2], r) => { let t0 = 0, t1 = 1; const dx = x2 - x1, dy = y2 - y1, P = [-dx, dx, -dy, dy], Qq = [x1 - r[0], r[2] - x1, y1 - r[1], r[3] - y1];
      for (let i = 0; i < 4; i++) { if (P[i] === 0) { if (Qq[i] < 0) return false; } else { const t = Qq[i] / P[i]; if (P[i] < 0) { if (t > t1) return false; if (t > t0) t0 = t; } else { if (t < t0) return false; if (t < t1) t1 = t; } } } return true; };
    const grow = (r, d) => [r[0] - d, r[1] - d, r[2] + d, r[3] + d];
    const free = (r) => { const R = grow(r, m); if (!(r[0] > vx + 4 && r[2] < vx + vw - 4 && r[1] > vy + 4 && r[3] < vy + vh - 4)) return false;
      if (segs.some((sg) => hitSeg(sg, R))) return false; if (B.pins.some(([px, py]) => px > R[0] - 5 && px < R[2] + 5 && py > R[1] - 5 && py < R[3] + 5)) return false;
      return !placed.some((b) => r[0] < b[2] + 6 && r[2] > b[0] - 6 && r[1] < b[3] + 4 && r[3] > b[1] - 4); };
    const width = (t) => [...t].reduce((w, ch) => w + (ch.charCodeAt(0) < 128 ? 0.62 : 1.0) * fs, 0) + 3;
    const rectAt = (x, base, w, anchor) => { const x0 = anchor === "end" ? x - w : x; return [x0, base - fs * 1.02, x0 + w, base + fs * 0.32]; };
    return items.map((it) => {
      const w = width(it.text); let best = null;
      const pr = rectAt(it.ax + it.dx, it.ay + it.dy, w, it.a); if (free(pr)) best = { x: it.ax + it.dx, y: it.ay + it.dy, anchor: it.a, rect: pr };
      search: for (const rr of best ? [] : [10, 14, 18, 23, 29, 36, 44, 53, 63, 75, 88, 102, 118, 136, 156]) for (let k = 0; k < 24; k++) {
        const th = ((k * 15 + (it.a === "end" ? 180 : 0)) * Math.PI) / 180, px = it.ax + rr * Math.cos(th), py = it.ay + rr * Math.sin(th), anchor = Math.cos(th) >= -0.01 ? "start" : "end", base = py + fs * 0.35, r = rectAt(px, base, w, anchor);
        if (free(r)) { best = { x: px, y: base, anchor, rect: r }; break search; } }
      if (!best) best = { x: it.ax + it.dx, y: it.ay + it.dy, anchor: it.a, rect: pr };
      placed.push(best.rect); const ex = Math.max(best.rect[0], Math.min(it.ax, best.rect[2])), ey = Math.max(best.rect[1], Math.min(it.ay, best.rect[3]));
      return { ...it, ...best, ex, ey, lead: Math.hypot(ex - it.ax, ey - it.ay) > 9 };
    });
  }
  function rackTags(S, Lo, st) {
    const f = Lo.nar ? 30 : Lo.vid ? 13 : 16, R = ART.rack;
    let s = "";
    R.labels.forEach((l, i) => { const a = ARMS[i]; s += T(l.xy[0], l.xy[1] + (Lo.nar ? 22 : 10), Lo.nar ? a.id.replace("olm", "") : a.id, `fig-tag strong${a.g1fail ? " nv" : ""}`, "middle"); if (!Lo.nar) s += T(l.xy[0], l.xy[1] + 10 + f * 1.15, a.g1fail ? "G1 ✗" : armName(S, a).slice(0, S.lang === "en" ? 22 : 9), "fig-tag muted", "middle"); });
    R.ticks.forEach((t) => { if (t.T === 10000) return; s += T(t.lxy[0] - (Lo.nar ? 10 : 8), t.lxy[1] + (t.T === 12288 ? -4 : 5), t.T === 12288 ? L(S, "12,288 上限", "12,288 cap") : int(t.T), "fig-tag muted rk-tick", "end"); });   // v1.1 F6
    if (!Lo.nar) s += T(R.ticks[4].lxy[0] - 8, R.ticks[4].lxy[1] - 28, L(S, "T(書いた token・対数)", "T (tokens written, log)"), "fig-tag muted", "end");
    // the selected block: a lit ring on its top; v1.2 G4: its key (and the ◇ names of state 13) go to a free place found below, joined by a leader line
    const names = [], hit = R.hits.find(([ai, ri]) => `${AID[ai]}:${ARMS[ai].rows[ri].k}` === S.row);
    if (hit) { s += CI(hit[2], hit[3], Lo.nar ? 9 : 7, "fig-selring"); names.push({ text: ARMS[hit[0]].rows[hit[1]].k, cls: "fig-tag strong sel rk-name", hx: hit[2], hy: hit[3] }); }
    if (st.filter === "o127") for (const k of DATA.quoted.apex127.keys) {        // v1.1 F5: ◇ = reached |O3Tc| = |O3Th| with numbers (RESULT olm127 §3.4 / §4 names them; no inventory predicate)
      const h = R.hits.find(([ai, ri]) => AID[ai] === "olm127" && ARMS[ai].rows[ri].k === k); if (!h) continue; const d = Lo.nar ? 11 : 8, cy = h[3] - (Lo.nar ? 16 : 12);
      s += `<path class="fig-apexmk" d="M${h[2].toFixed(1)} ${(cy - d).toFixed(1)}L${(h[2] + d).toFixed(1)} ${cy.toFixed(1)}L${h[2].toFixed(1)} ${(cy + d).toFixed(1)}L${(h[2] - d).toFixed(1)} ${cy.toFixed(1)}Z"/>`; names.push({ text: `◇ ${k}`, cls: "fig-tag eq rk-name", hx: h[2], hy: cy - d }); }
    for (const n of placeNames(Lo, names)) s += `<path class="fig-lead" d="M${n.ax.toFixed(1)} ${n.ay.toFixed(1)}L${n.ex.toFixed(1)} ${n.ey.toFixed(1)}"/>` + T(n.x, n.y, n.text, n.cls, n.anchor);
    return s;
  }
  // v1.2 G4: a free place for each name tag: candidates around the block's top (nearest first), clear of every block's rectangle (from the kit's corners, art.mjs), the axis labels, the arm labels and the tags already placed
  function placeNames(Lo, items) {
    const R = ART.rack, fs = Lo.nar ? 31 : Lo.vid ? 14 : 16.5, [vx, vy, vw, vh] = rackVB(Lo), placed = [];
    const avoid = R.hits.map((h) => h[5]).concat(R.labels.map((l) => [l.xy[0] - (Lo.nar ? 70 : 90), l.xy[1] - 4, l.xy[0] + (Lo.nar ? 70 : 90), l.xy[1] + 16 + fs * 1.4]), R.ticks.map((t) => [t.lxy[0] - (Lo.nar ? 230 : 150), t.lxy[1] - fs - 4, t.lxy[0] + 2, t.lxy[1] + 8]));
    const meets = (r) => avoid.some((b) => r[0] < b[2] + 4 && r[2] > b[0] - 4 && r[1] < b[3] + 4 && r[3] > b[1] - 4) || placed.some((b) => r[0] < b[2] + 8 && r[2] > b[0] - 8 && r[1] < b[3] + 5 && r[3] > b[1] - 5);
    const inside = (r) => r[0] > vx + 4 && r[2] < vx + vw - 4 && r[1] > vy + 4 && r[3] < vy + vh - 4;
    return items.map((it) => {
      const w = [...it.text].length * fs * 0.62 + (it.text.startsWith("◇") ? fs * 0.5 : 0), ax = it.hx, ay = it.hy - 3; let best = null;
      search: for (const r of [22, 34, 50, 70, 95, 125, 160, 200, 250, 310, 380, 460, 560]) for (const deg of [-25, 25, -55, 0, 55, -85, 155, 205, 125, 235, 95, 265]) {
        const th = (deg * Math.PI) / 180, px = ax + r * Math.cos(th), py = ay + r * Math.sin(th), right = Math.cos(th) >= -0.01, x0 = right ? px : px - w, base = py + fs * 0.35, rect = [x0, base - fs * 1.0, x0 + w, base + fs * 0.3];
        if (inside(rect) && !meets(rect)) { best = { x: px, y: base, anchor: right ? "start" : "end", rect }; break search; } }
      if (!best) { const x0 = Math.min(Math.max(ax - w / 2, vx + 8), vx + vw - w - 8), base = vy + fs * 1.3 + placed.length * fs * 1.4; best = { x: x0, y: base, anchor: "start", rect: [x0, base - fs, x0 + w, base + fs * 0.3] }; }
      placed.push(best.rect); const ex = Math.max(best.rect[0], Math.min(ax, best.rect[2])), ey = Math.max(best.rect[1], Math.min(ay, best.rect[3]));
      return { ...it, ...best, ax, ay, ex, ey };
    });
  }
  // v1.2 G4: the rack's viewBox keeps room on the right and on top for the name tags
  function rackVB(Lo) { const R = ART.rack, xs = R.hits.map((h) => h[2]).concat(R.labels.map((l) => l.xy[0])), ys = R.hits.map((h) => h[3]).concat(R.labels.map((l) => l.xy[1] + 40), R.ticks.map((t) => t.xy[1]), [R.ticks[4].lxy[1] - 48]); const pad = Lo.nar ? 30 : 24; const x0 = Math.min(Math.min(...xs) - (Lo.nar ? 40 : 70), R.ticks[0].lxy[0] - (Lo.nar ? 230 : 150)) - pad, y0 = Math.min(...ys) - pad - 20 - (Lo.nar ? 50 : 30), x1 = Math.max(...xs) + pad + (Lo.nar ? 60 : 150), y1 = Math.max(...ys) + pad + (Lo.nar ? 30 : 10); return [x0, y0, x1 - x0, y1 - y0]; }
  function pickRow(S, x, y) {
    const list = new Set(rowsOf(S)); let best = null, bd = 1e9;
    for (const [ai, ri, hx, hy] of ART.rack.hits) { const id = `${AID[ai]}:${ARMS[ai].rows[ri].k}`; if (!list.has(id)) continue; const d = Math.hypot(hx - x, hy - y); if (d < bd) { bd = d; best = id; } }
    return bd < 22 ? best : null;
  }

  // ---------------------------------------------------------------- html panels
  const chipsRow = (items) => `<div class="fx-tags">${items.filter(Boolean).map(([k, v, tone]) => `<span class="fx-tag"${tone ? ` data-tone="${tone}"` : ""}><b>${esc(k)}</b> ${esc(v)}</span>`).join("")}</div>`;
  function rowPanel(S, id, opt = {}) {
    const [aid] = id.split(":"), a = armOf(aid), r = rowOf(id), N = NM(S); if (!r) return "";
    const yes = L(S, "あり", "yes"), no = L(S, "なし", "no");
    return `<div class="fx-row" data-cls="${r.cls}"><div class="fx-h">${esc(aid)} <b>${esc(r.k)}</b> <span class="fx-sub">${esc(armName(S, a))} · seed ${r.seed}</span></div>
${chipsRow([[L(S, "類", "class"), aid === "olm117" && N.clsEqual[r.cls] ? N.clsEqual[r.cls] : N.cls[r.cls], r.cls === "MIDO3" ? "mido" : r.cls === "EQ" ? "eq" : ""], ["T", int(r.T) + (r.cap ? L(S, "(上限)", " (cap)") : "")], ["status", r.st], [L(S, "計算", "calc"), r.calc ? yes : no], [L(S, "退け REJ6", "reject REJ6"), r.rej ? yes : no], [L(S, "線対称 v3 / v6", "line symm. v3 / v6"), `${r.ln3 ? "✓" : "–"} / ${r.ln6 ? "✓" : "–"}`], [L(S, "外接線の印 v3", "outer v3"), r.out3 ? "✓" : "–"]])}
${r.conj ? `<div class="fx-k">conjecture</div><div class="fx-q">${esc(r.conj)}</div>` : `<div class="fx-k">conjecture</div><div class="fx-q muted">${L(S, "(JSON が取れない = NONE)", "(no JSON = NONE)")}</div>`}
<div class="fx-k">${L(S, "証明の欄(全文・逐語)", "proof field (full, verbatim)")}</div><div class="fx-q">${r.proof ? esc(r.proof) : `<span class="muted">${L(S, "(証明の欄なし)", "(no proof field)")}</span>`}</div>
${r.hit ? `<div class="fx-k">${L(S, "線対称の計器が拾った窓(逐語)", "the window the line-symmetry reader caught (verbatim)")}</div><div class="fx-q mono">…${esc(r.hit)}…</div>` : ""}
${r.rejf ? `<div class="fx-k">${L(S, "本文の退けの文(REJ6 の最初・逐語)", "the body's reject sentence (first REJ6, verbatim)")}</div><div class="fx-q mono">…${esc(r.rejf)}…</div>` : r.calc ? `<div class="fx-k">${L(S, "本文の計算の頭(逐語)", "the start of the body's calculation (verbatim)")}</div><div class="fx-q mono">…${esc(r.fc.slice(0, 220))}…</div>` : ""}
${opt.loop ? `<div class="fx-k">${L(S, "繰り返す文(棚卸しの述語・回数)", "the repeated sentence (inventory predicate, count)")}</div><div class="fx-q mono">“${esc(opt.loop[0])}” × ${opt.loop[1]}</div>` : ""}
</div>`;
  }
  function slips(S) {
    const P0 = DATA.slip0, ids = [["S1", `${DATA.scenes.S1.arm}:${DATA.scenes.S1.key}`], ["S2", `${DATA.scenes.S2.arm}:${DATA.scenes.S2.key}`]], N = NM(S), yes = L(S, "あり", "yes"), no = L(S, "なし", "no");
    const cells = (fn) => ids.map(([sid, id]) => `<div class="fx-cell" data-s="${sid}">${fn(sid, rowOf(id), id.split(":")[0])}</div>`).join("");
    const head = (sid, r, aid) => `<div class="fx-badge">${sid === "S1" ? L(S, "S1 · 退けた後に証明の欄で線対称", "S1 · rejects, then line symmetry in the proof field") : L(S, "S2 · 退けた後の証明の欄に線対称なし", "S2 · rejects, no line symmetry in the proof field")}</div>
<div class="fx-h">${esc(aid)} <b>${esc(r.k)}</b> <span class="fx-sub">${esc(armName(S, armOf(aid)))} · seed ${r.seed}</span></div>
${chipsRow([[L(S, "類", "class"), N.cls[r.cls], r.cls === "EQ" ? "eq" : ""], ["T", int(r.T)], ["status", r.st], [L(S, "計算", "calc"), r.calc ? yes : no], [L(S, "退け REJ6", "reject REJ6"), r.rej ? yes : no], [L(S, "線対称 v3 / v6", "line symm. v3 / v6"), `${r.ln3 ? "✓" : "–"} / ${r.ln6 ? "✓" : "–"}`]])}`;
    const conj = (sid, r) => `<div class="fx-k">conjecture</div><div class="fx-q">${esc(r.conj)}</div>`;
    const rej = (sid, r) => `<div class="fx-k">${L(S, `本文の退けの文(REJ6 の最初・逐語)— ${P0.refl[r.k]} を O1O2 で折り返した`, `the body's reject sentence (first REJ6, verbatim) — it reflected ${P0.refl[r.k]} across O1O2`)}</div><div class="fx-q mono">…${esc(r.rejf)}…</div>`;
    const proof = (sid, r) => { let tx = esc(r.proof); if (r.ln3 && r.proof.includes(P0.phrase)) tx = tx.replace(esc(P0.phrase), `<mark class="fx-hit">${esc(P0.phrase)}</mark>`); return `<div class="fx-k">${L(S, "証明の欄(全文・逐語)", "proof field (full, verbatim)")}</div><div class="fx-q">${tx}</div>`; };
    const frame = (sid, r) => r.ln3 ? `<div class="fx-frame yes"><i class="fx-fmk"></i><span>${L(S, "線対称の計器 v3 が拾った語(v3 ✓ / v6 ✓)", "words the line-symmetry reader v3 caught (v3 ✓ / v6 ✓)")}: “${esc(P0.phrase)}”</span></div>`
      : `<div class="fx-frame no"><i class="fx-fmk"></i><span>${L(S, `線対称の語なし(v3 ${r.ln3 ? "✓" : "–"} / v6 ${r.ln6 ? "✓" : "–"})`, `no line-symmetry words (v3 ${r.ln3 ? "✓" : "–"} / v6 ${r.ln6 ? "✓" : "–"})`)}</span></div>`;
    return `<div class="fx-grid2">${[head, conj, rej, proof, frame].map(cells).join("")}</div>
<p class="fx-note">${L(S, "そろえ方: 二行を「本文の退けの文」の段でそろえた(同じ問いの文 olm125・同じ座標・同じ種類の計算 = 折り返しを数値で出して退けた・折り返した点は違う)。本文の中の位置(token)は棚卸しに無いので、段の高さは縮尺どおりでない。計器(証明の欄の語の印)と証明(正しさ)は別: 図は正しさを読まない。", "Alignment: the two rows are aligned at the body's reject sentence (same prompt olm125, same coordinates, the same kind of calculation = computed a reflection with numbers and rejected it; the reflected point differs). The token position in the body is not in the inventory, so the panels are not to scale. The instrument (word marks in the proof field) is not the proof: the figure does not read correctness.")}</p>`;
  }
  function tools(S) {
    const P = DATA.prompts, md = P.md5;
    const box = (name, arms, text, note) => `<section class="fx-tool"><div class="fx-h">${esc(name)} <span class="fx-sub">${esc(arms)}</span></div><pre class="fx-pre">${esc(text)}</pre><div class="fx-sub">${esc(note)}</div></section>`;
    const formula = P.formula, decl = P.decl, use = P.formula + P.use;
    return `<div class="fx-tools">${box(NM(S).tool.none, "olm113 (M2A)", L(S, "(Tool の段なし)", "(no Tool section)"), L(S, "基準", "baseline"))}
${box(NM(S).tool.formula, "olm122 · olm124", formula, L(S, `${formula.length} 字・問いの文の md5 ${md["olm122/124"].slice(0, 8)}`, `${formula.length} chars · prompt md5 ${md["olm122/124"].slice(0, 8)}`))}
${box(NM(S).tool.decl, "olm119", decl, L(S, `${decl.length} 字・式 + 宣言の文「${P.second.trim()}」`, `${decl.length} chars · formula + the declaration "${P.second.trim()}"`))}
${box(NM(S).tool.instr, "olm125 · olm127", use, L(S, `${use.length} 字・問いの文の md5 ${md["olm125/127"].slice(0, 8)}(二回とも逐語同じ)`, `${use.length} chars · prompt md5 ${md["olm125/127"].slice(0, 8)} (verbatim the same both times)`))}</div>`;
  }
  function instr(S) {
    const Lg = DATA.lineage, N = NM(S);
    const tr = (mark, name, what, cal) => `<tr><td class="fx-mk">${mark}</td><td><b>${esc(name)}</b></td><td>${esc(what)}</td><td>${esc(cal)}</td></tr>`;
    return `<table class="fx-table"><thead><tr><th></th><th>${L(S, "計器の印", "mark")}</th><th>${L(S, "何を拾うか(語の印・正規表現)", "what it catches (word marks, regular expressions)")}</th><th>${L(S, "較正 / 統制", "calibration / control")}</th></tr></thead><tbody>
${tr('<i class="mk-ln3"></i>', N.mark.ln, L(S, "証明の欄で Tc と Th が O1O2 について対称 / 折り返すと重なる、を肯定して述べる(否定・仮定は除く)", "the proof field asserts Tc and Th are symmetric about O1O2 / reflect onto each other (negations and suppositions excluded)"), L(S, `v3 = 判定(較正 ${Lg.cal.v3})・v6 = 参考(較正 ${Lg.cal.v6})`, `v3 = verdict (calibration ${Lg.cal.v3}) · v6 = reference (calibration ${Lg.cal.v6})`))}
${tr('<i class="mk-ln6"></i>', L(S, "線対称(v6 だけが拾う)", "line symmetry (v6 only)"), L(S, "v6 が足した形: 直の目的語「reflect(ing) Tc across O1O2 yields Th」と入れ替え・式の写しは外す", "what v6 added: the direct object \"reflect(ing) Tc across O1O2 yields Th\" and the swap; copies of the formula removed"), L(S, `陰性統制 prf5 ${Lg.neg.pt_ln} / ${Lg.neg.n}`, `negative control prf5 ${Lg.neg.pt_ln} / ${Lg.neg.n}`))}
${tr('<i class="mk-out"></i>', N.mark.out, L(S, "接線 ∥ O1O2・O1O2 ⊥ 接線・O1O2 が接点の垂直二等分線(外側の共通接線の性質・一般の図では偽)", "tangent ∥ O1O2 · O1O2 ⊥ tangent · O1O2 bisects the contact points (outer-tangent properties; false on the general figure)"), L(S, `陰性統制 prf5 ${Lg.neg.outer} / ${Lg.neg.n}`, `negative control prf5 ${Lg.neg.outer} / ${Lg.neg.n}`))}
${tr('<i class="mk-calc"></i>', N.mark.calc, L(S, "本文で折り返しの式を数値で使った(REFL_CALC)", "the body used the reflection formula with numbers (REFL_CALC)"), "olm119〜")}
${tr('<i class="mk-rej"></i>', N.mark.rej, L(S, "折り返しを数値で出して「not the same / is not Th / ≠ / doesn't match」と書いた(REJ6・v6)", "the body computed the reflection and wrote \"not the same / is not Th / ≠ / doesn't match\" (REJ6, v6)"), L(S, `olm126 Q3 = ${N.verdict[Lg.q3_126] || Lg.q3_126}(回帰の基準は据えていない)`, `olm126 Q3 = ${N.verdict[Lg.q3_126] || Lg.q3_126} (its regression basis is not settled)`))}
</tbody></table><p class="fx-note fx-q3row"><b>${L(S, "RESULT olm126 §2 の表の Q3 の行(写し・L1)", "RESULT olm126 §2, the Q3 row of the table (copied verbatim in Japanese, L1)")}:</b> ${esc(DATA.quoted.q3_126.ja)}</p><p class="fx-note">${L(S, "どれも「書いた語」の印で、model の中身ではない。証明の正しさは読まない。類(一般の図で MIDO3 偽 / EQ 真・等半径の図 olm117 では MIDO3 も真)は配置の事実として使い、各行の正しさは数えない。", "All are marks of the words written, not the model's inside. The correctness of a proof is not read. The classes (on the general figure MIDO3 false / EQ true; on the equal-radii figure olm117 MIDO3 is true as well) are facts of the configuration; correctness per row is not counted.")}</p>`;
  }
  function question(S) {
    const N = NM(S), parts = I18N[S.lang].memo;
    return `<div class="fx-qbox"><div class="fx-k">${L(S, "先生の問い(逐語・11-04 朝・この章でだけ扱う)", "The teacher's question (verbatim, 11-04 morning; only in this chapter)")}</div><div class="fx-big">「olmXシリーズから評価関数を導出できますか？」</div>
<div class="fx-k">${L(S, "主 session の答え(MEMO §4 の要約・L3・採否は先生)", "The main session's answer (summary of MEMO §4; L3; adoption is the teacher's)")}</div><div class="fx-q">${esc(parts.answer)}</div></div>
<table class="fx-table"><thead><tr><th>${L(S, "自己対戦の部品(動画の枠)", "part of self-play (the video's frame)")}</th><th>${L(S, "olmX の値(この図の data)", "olmX values (this figure's data)")}</th><th>${L(S, "家に在るか(主 session の読み)", "present? (main session's reading)")}</th><th>${L(S, "出所", "source")}</th></tr></thead><tbody>${parts.rows.map(([p, v, h, src]) => `<tr><td><b>${esc(p)}</b></td><td>${esc(v)}</td><td>${esc(h)}</td><td class="fx-src">${esc(src)}</td></tr>`).join("")}</tbody></table>`;
  }
  function nextq(S) {
    const c = I18N[S.lang].next;
    return `<div class="fx-next"><div class="fx-k">${esc(c.head)}</div><ol>${c.items.map((t) => `<li>${esc(t)}</li>`).join("")}</ol><p class="fx-note">${esc(c.note)}</p>
<button class="sh-btn fx-back" type="button" data-go-state="0">${esc(c.back)}</button></div>`;
  }
  function ledger(S) {
    const T2 = I18N[S.lang].ledger;
    return ["L1", "D", "L3", "x"].map((lv, i) => `<section><h3>${esc(T2.cols[i])}</h3>${T2.rows.filter((x) => x.level === lv).map((x) => `<article><b>${T2.tag[lv]}</b> ${esc(x.text)}<span class="src">${esc(x.src)}</span></article>`).join("")}</section>`).join("");
  }
  function boardSide(S) {
    const g = DATA.geo, st = I18N[S.lang].read;
    return `<div class="fx-steps">${st.map((t, i) => `<div class="fx-step"><b>${i + 1}</b> ${esc(t)}</div>`).join("")}</div>
<table class="fx-table small"><tbody>
<tr><td><span class="sw-mido"></span> MIDO3</td><td>${L(S, `M = (${g.mid_TcTh.join(", ")})・O3 = (${g.O3.map((v) => v.toFixed(4)).join(", ")})・距離 ${g.gap_mid_O3}`, `M = (${g.mid_TcTh.join(", ")}) · O3 = (${g.O3.map((v) => v.toFixed(4)).join(", ")}) · distance ${g.gap_mid_O3}`)}</td><td>${NM(S).truth.f}</td></tr>
<tr><td><span class="sw-eq"></span> EQ</td><td>|O3Tc| = ${g.dTc.toFixed(4)} · |O3Th| = ${g.dTh.toFixed(4)}</td><td>${NM(S).truth.t} (apex)</td></tr>
<tr><td>${NM(S).mark.ln}</td><td>${L(S, `Th を O1O2 で折り返す = (${g.Th_r.join(", ")})・Tc = (${g.Tc.join(", ")})・距離 ${g.gap_refl}`, `reflect Th across O1O2 = (${g.Th_r.join(", ")}) · Tc = (${g.Tc.join(", ")}) · distance ${g.gap_refl}`)}</td><td>${NM(S).truth.f}</td></tr>
</tbody></table><p class="fx-note">${L(S, `座標 = olm125 b1_j17 の本文に写された問いの座標(頭と退けの文)・半径 ${g.r2} / ${g.r1}。折り返し・中点・距離はこの頁の pack がその座標で計算した(b1_j17 自身の値 (6.6167, 0.3767) と 0.01 以内で一致)。`, `Coordinates = the prompt's coordinates as written in olm125 b1_j17's body (its head and reject sentence) · radii ${g.r2} / ${g.r1}. Reflections, midpoint and distances are computed by this page's pack from those coordinates (within 0.01 of b1_j17's own value (6.6167, 0.3767)).`)}</p>`;
  }
  function rackSide(S, st) {
    const N = NM(S), f = st.filter || "", sc = DATA.scenes;
    let head = "";
    if (f === "calc") { const A5 = armOf("olm125").agg, cc = A5.calc_cls, rp = DATA.rej_to_proof_125.length;
      head = `<div class="fx-k">${L(S, "計算した行(REFL_CALC)の数・うち退け REJ6(REJ6 ∧ REFL_CALC / REFL_CALC)", "rows that used the formula (REFL_CALC) · of which reject REJ6 (REJ6 ∧ REFL_CALC / REFL_CALC)")}</div><div class="fx-mini">${ARMS.filter((a) => a.agg.CALC).map((a) => `<span>${a.id} <b>${a.agg.REJ_calc} / ${a.agg.CALC}</b></span>`).join("")}</div>
<p class="fx-note">${L(S, `olm125: 計算した ${A5.CALC} 本のうち ${A5.REJ_calc} 本が退ける。${A5.CALC} 本の最終の conjecture の類は 等距離 ${cc.EQ}・OTHER ${cc.OTHER}・JSON なし ${cc.NONE}・共線 ${cc.MIDO3}(退けた ${A5.REJ_calc} 本の行き先ではない)。退けた ${A5.REJ_calc} 本のうち証明の欄に至った行は ${rp}。`, `olm125: of the ${A5.CALC} calc rows, ${A5.REJ_calc} reject. The final conjecture classes of the ${A5.CALC} rows are equidistant ${cc.EQ} · OTHER ${cc.OTHER} · no JSON ${cc.NONE} · collinear ${cc.MIDO3} (not where the ${A5.REJ_calc} rejects went). Of the ${A5.REJ_calc} rejecting rows, ${rp} reach a proof field.`)}</p>`; }
    if (f === "typ") head = `<div class="fx-k">${L(S, "b2_j07 の型(退け ∧ 証明の欄の線対称 v6)", "the b2_j07 type (reject ∧ line symmetry v6 in the proof field)")}</div><div class="fx-mini">${ARMS.filter((a) => a.tool !== "none_eq").map((a) => `<span>${a.id} <b>${a.agg.typ.length}</b>${a.agg.typ.length ? ` <button class="fx-rowbtn" type="button" data-row="${a.id}:${a.agg.typ[0]}">${a.agg.typ.join(" · ")}</button>` : ""}${a.id === "olm127" ? ` <span class="fx-sub fx-cap127">${esc(I18N[S.lang].cap127short())}</span>` : ""}</span>`).join("")}</div>`;
    if (f === "o127") { const ap = DATA.quoted.apex127;
      head = `<div class="fx-k">${L(S, "olm127 の場面(棚卸しの述語)", "olm127 scenes (inventory predicates)")}</div><div class="fx-mini">${["S8", "S9", "S10"].map((k) => `<button class="fx-rowbtn" type="button" data-row="${sc[k].arm}:${sc[k].key}">${k} ${sc[k].key}</button>`).join("")}</div>
<p class="fx-note fx-rejnote">${esc(I18N[S.lang].rejNote())}${L(S, "(RESULT olm127 §3.4 / §4 の 5)", " (RESULT olm127 §3.4 / §4 item 5)")}</p>
<div class="fx-k">${L(S, "◇ 等距離に数値で着いた二行(RESULT olm127 §3.4 / §4 の名指し・棚卸しに述語は無い)", "◇ the two rows that reach the equidistance with numbers (named in RESULT olm127 §3.4 / §4; no inventory predicate)")}</div><div class="fx-mini">${ap.keys.map((k) => `<button class="fx-rowbtn" type="button" data-row="olm127:${k}">◇ ${k}</button>`).join("")}</div>
<p class="fx-note">${L(S, `b0_j00「${ap.b0_j00}」= status / 証明の欄に至らない。b2_j09 = 証明の欄が数値だけ(「${ap.b2_j09}」)。apex(真)に着いたことと、証明の正しさは別(図は正しさを読まない)。`, `b0_j00 "${ap.b0_j00}" = reaches no status / proof field. b2_j09 = the proof field is numbers only ("${ap.b2_j09}"). Landing on the apex (true) is not the correctness of a proof (the figure does not read correctness).`)}</p>`; }
    const loopOf = Object.values(sc).find((x) => `${x.arm}:${x.key}` === S.row && x.loop_count);
    return head + rowPanel(S, S.row, { loop: loopOf ? [loopOf.loop_phrase, loopOf.loop_count] : null });
  }
  function scaleSide(S) {
    const a = armOf(S.arm), P = DATA.prompts, N = NM(S), qf = DATA.quoted;
    const text = { none: L(S, "(Tool の段なし)", "(no Tool section)"), none_eq: L(S, `(Tool の段なし・半径を ${qf.r_equal} に揃えた図)`, `(no Tool section; both radii set to ${qf.r_equal})`), formula: P.formula, decl: P.decl, instr: P.formula + P.use }[a.tool];
    const v = DATA.verdicts[a.id];
    return `<div class="fx-h">${esc(a.id)} <span class="fx-sub">${esc(armName(S, a))} · seed ${a.agg.seeds.join(" / ")}</span></div><div class="fx-k">${L(S, "Tool の段(逐語)", "the Tool section (verbatim)")}</div><pre class="fx-pre">${esc(text)}</pre>
${chipsRow([[L(S, "取れた", "parsed"), `${a.agg.parsed} / 60`], [L(S, "証明の欄", "proof field"), `${a.agg.n_proof}`], ["v3", `${a.agg.LN3} = ${n3(a.agg.LN3_rate)}`], ["v6", `${a.agg.LN6} = ${n3(a.agg.LN6_rate)}`], [L(S, "判定", "verdict"), a.g1fail ? L(S, "なし(G1 ✗)", "none (G1 ✗)") : v ? N.verdict[v.read] || v.read : L(S, "基準", "baseline")]])}
<p class="fx-note">${L(S, `隣り合う腕の Fisher(参考・PREREG に無い・多重比較は補正していない): olm125 の 9 / 40 は olm124 4 / 37 と p ${qf.fisher.p124}・式だけ pool 120 行と p ${qf.fisher.ppool}・olm119 と p ${qf.fisher.p119}(RESULT olm125 §2)。olm127 3 / 35 は olm124 と p ${qf.fisher127.p124}・olm125 と p ${qf.fisher127.p125}・olm119 と p ${qf.fisher127_more.p119}(RESULT olm127 §2)。七対の並びは状態 9。判定は凍結の帯で、大きさは走らせ直しで。`, `Fisher between neighbouring arms (reference, not in the PREREG, no correction for multiple comparisons): olm125's 9 / 40 vs olm124 4 / 37 p ${qf.fisher.p124}, vs the formula-only pool of 120 rows p ${qf.fisher.ppool}, vs olm119 p ${qf.fisher.p119} (RESULT olm125 §2). olm127 3 / 35 vs olm124 p ${qf.fisher127.p124}, vs olm125 p ${qf.fisher127.p125}, vs olm119 p ${qf.fisher127_more.p119} (RESULT olm127 §2). All seven pairs: state 9. The verdict is the frozen band; the size needs reruns.`)}</p>`;
  }

  function lineageSide(S) {
    const N = NM(S), c4 = DATA.cases.find((c) => c.id === "v4_drop"), c5 = DATA.cases.find((c) => c.id === "v5_drop");
    const add = DATA.v6_added.olm124.includes("b0_j00") ? "olm124:b0_j00" : null, drop = DATA.v6_dropped.olm124.includes("b1_j01") ? "olm124:b1_j01" : null;
    const box = (title, id, marks, text) => `<div class="fx-case"><div class="fx-k">${esc(title)}</div><div class="fx-h">${esc(id)} <span class="fx-sub">${esc(marks)}</span></div><div class="fx-q mono">${esc(text)}</div></div>`;
    const mk = (r) => `${L(S, "線対称", "line symm.")} v3 ${r.ln3 ? "✓" : "–"} / v6 ${r.ln6 ? "✓" : "–"} · ${L(S, "外接線", "outer")} v3 ${r.out3 ? "✓" : "–"} / v6 ${r.out6 ? "✓" : "–"}`;
    let h = `<div class="fx-k">${L(S, "計器を直した所(逐語・証明の欄)", "where the instrument was fixed (verbatim, proof field)")}</div>`;
    h += box(L(S, "v4 が落とした本物の外接線の印(主語と動詞の間に句)→ v6 で戻る", "a true outer marker v4 dropped (a phrase between subject and verb) → back in v6"), `${c4.arm}:${c4.key}`, mk(rowOf(`${c4.arm}:${c4.key}`)), c4.proof);
    h += box(L(S, "v5 が落とした本物(「, so the line TcTh is thus parallel」)→ v6 で戻る", "a true one v5 dropped (\", so the line TcTh is thus parallel\") → back in v6"), `${c5.arm}:${c5.key}`, mk(rowOf(`${c5.arm}:${c5.key}`)), c5.proof);
    if (add) h += box(L(S, "v6 が足した線対称(直の目的語「Reflecting Th over O1O2 yields Tc」)", "line symmetry v6 added (the direct object \"Reflecting Th over O1O2 yields Tc\")"), add, mk(rowOf(add)), rowOf(add).proof);
    if (drop) h += box(L(S, "v6 が外した線対称(式の写し)", "line symmetry v6 removed (a copy of the formula)"), drop, mk(rowOf(drop)), rowOf(drop).proof);
    return h + `<p class="fx-note">${L(S, "どれも一行の違い。olm118 Q3 の帯の名(変わらない / 間)は、この一行で境 0.06 を越えたり戻ったりした。", "Each is a one-row difference; the olm118 Q3 band name (unchanged / between) crossed the 0.06 edge and came back on such a row.")}</p>`;
  }

  // ---------------------------------------------------------------- draw
  const PLANE = { scale, gate, bands, side, fisher, split, equal, lineage, same };
  function draw(S, el, root) {
    const st = states[S.state], Lo = layout(root, st.view);
    el.side.innerHTML = ""; el.html.innerHTML = ""; el.ledger.innerHTML = ""; if (el.ctitle) el.ctitle.textContent = "";
    if (st.mode === "slips") { setArt(el, "slips"); el.svg.setAttribute("viewBox", [0, 0, ...ART.slips.vb].join(" ")); el.pic.innerHTML = slipsTags(S, Lo); }
    else if (st.mode === "board") { setArt(el, "board"); const vb = Lo.nar ? [70, 170, 660, 300] : [0, 0, ...ART.board.vb]; el.svg.setAttribute("viewBox", vb.join(" ")); el.pic.innerHTML = boardTags(S, Lo); el.side.innerHTML = boardSide(S); }
    else if (st.mode === "rack") {
      setArt(el, "rack"); el.svg.setAttribute("viewBox", rackVB(Lo).map((v) => v.toFixed(1)).join(" ")); el.pic.innerHTML = rackTags(S, Lo, st);
      el.art.querySelectorAll(".rk[data-sel]").forEach((g) => g.removeAttribute("data-sel")); const g = el.art.querySelector(`.rk[data-r="${S.row}"]`); if (g) g.setAttribute("data-sel", "");
      el.side.innerHTML = rackSide(S, st);
    } else if (PLANE[st.mode]) { setArt(el, ""); const out = PLANE[st.mode](S, Lo); if (el.ctitle) el.ctitle.textContent = Lo.nar ? Lo.title || "" : ""; el.svg.setAttribute("viewBox", out.vb.join(" ")); el.pic.innerHTML = out.svg; if (st.mode === "scale") el.side.innerHTML = scaleSide(S); if (st.mode === "lineage") el.side.innerHTML = lineageSide(S); }
    else { setArt(el, ""); el.pic.innerHTML = ""; el.svg.setAttribute("viewBox", "0 0 10 10"); }
    if (st.mode === "slips") el.html.innerHTML = slips(S); else if (st.mode === "tools") el.html.innerHTML = tools(S); else if (st.mode === "instr") el.html.innerHTML = instr(S);
    else if (st.mode === "question") el.html.innerHTML = question(S); else if (st.mode === "nextq") el.html.innerHTML = nextq(S); else if (st.mode === "ledger") el.ledger.innerHTML = ledger(S);
  }
  function ctx(S) {
    const A = Object.fromEntries(ARMS.map((a) => [a.id, a.agg])), r = S.row ? rowOf(S.row) : null;
    return { S, A, arm: S.arm, armA: S.arm ? A[S.arm] : null, row: r, rowId: S.row, V: DATA.verdicts, F: DATA.frozen, G: DATA.geo, Lg: DATA.lineage, SC: DATA.scenes, P: DATA.prompts, Qd: DATA.quoted, nRows: rowsOf(S).length, n3, sgn, sgn4, int, pool: DATA.pool127, four: DATA.four, FR: DATA.fisher, FB: DATA.fisher_below, E: DATA.edges, P0: DATA.slip0, rp125: DATA.rej_to_proof_125, gates: DATA.gates, g075: DATA.g075, g080: DATA.g080, armName: (id) => armName(S, armOf(id)) };
  }
  return {
    states, ctx, draw, rowsOf, allRows, armIds: AID,
    pick: (S, x, y) => (states[S.state].pick === "row" ? pickRow(S, x, y) : states[S.state].pick === "arm" ? pickArm(S, x, y) : null),
    keys: { slips: ["slpin", "lnno", "calcmk", "rejs"], board: ["mido", "eq", "refl"], rack: ["mido", "eq", "other", "none", "ln3", "ln6", "out", "rej", "cap"], rack_o127: ["mido", "eq", "other", "none", "ln3", "ln6", "out", "rej", "cap", "apex"], scale: ["v3", "v6", "edge", "nv"], gate: ["gate", "nv"], bands: ["seg", "v3"], side: ["mido", "eq"], split: ["bar"], equal: ["bar", "mido"], lineage: ["edge", "v3"], same: ["v3", "v6"], fisher: ["pbar", "ref05"] },
  };
})();
