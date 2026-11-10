// data.mjs — the SECOND route: the build counts every cell again, in JS, straight from the frozen jsonl files (not from the pack), and compares it with the pack that pack_data.py wrote.
// A disagreement stops the build (expect throws). Exports DATA = what the page carries (nothing typed by hand).
// It also re-does the drawing control in JS: the construction recomputed from the frozen A, G, E, F, P_x must give the frozen K, P_y, J within 1e-3.
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const X = join(process.env.MOY5_REPO || join(HERE, "data"), "ConstructGap", "exp") + "/";   // bundle: the frozen files are copied under data/ at their repo paths
const pack = JSON.parse(readFileSync(join(HERE, "generated", "pack.json"), "utf8"));
export const CONFIG = JSON.parse(readFileSync(join(HERE, "config.json"), "utf8"));
const expect = (cond, what) => { if (!cond) throw new Error(`data.mjs: the pack disagrees with the frozen jsonl / with itself: ${what}`); };
const cache = {};
const rowsOf = (f) => (cache[f] ||= readFileSync(X + f, "utf8").split("\n").filter((l) => l.trim()).map((l) => JSON.parse(l)));
for (const [f, h] of Object.entries(pack.files)) if (f.endsWith(".jsonl")) expect(createHash("md5").update(readFileSync(X + f)).digest("hex") === h, `md5 of ${f}`);

const median = (a) => { const s = [...a].sort((x, y) => x - y), n = s.length; return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2; };
let nCells = 0, nRows = 0;
for (const [id, c] of Object.entries(pack.cells)) {
  let rs = c.files.flatMap((f) => rowsOf(f));
  const variant = id.startsWith("olm1.") ? id.split(".")[1] : null;
  const olmish = c.kind === "olm" || c.kind === "olmk";
  rs = rs.filter((r) => r.arm === c.arm && (olmish ? (variant ? r.variant === variant : true) : r.model && shortName(r.model) === c.model));
  if (!olmish) rs = rs.filter((r) => r.raw);
  rs.sort((a, b) => a.rep - b.rep);
  expect(rs.length === c.n, `${id}: n ${rs.length} vs pack ${c.n}`);
  expect(JSON.stringify(rs.map((r) => r.rep)) === JSON.stringify(c.reps), `${id}: the reps`);
  let dots;
  if (c.kind === "cut") {
    dots = rs.map((r) => (r.cut_in_conjecture ? "A" : r.bind ? "R" : r.closure ? "F" : "N"));
    expect(rs.filter((r) => r.bind).length === c.bind && rs.filter((r) => r.cut_in_conjecture).length === c.ans && rs.filter((r) => r.closure).length === c.floor, `${id}: bind / ans / floor`);
  } else if (c.kind === "prf1") {
    const code = { "END-only": "E", CHAIN: "C", "LAT-only": "L", none: "N" };
    dots = rs.map((r) => code[r.route5]);
  } else if (c.kind === "prf3") {
    dots = rs.map((r) => (r.lat_sym && r.malformed ? "Sm" : r.lat_sym ? "S" : r.malformed ? "M" : r.fd_use ? "D" : "N"));
    const ok = rs.filter((r) => !r.malformed);
    expect(ok.filter((r) => r.lat_sym).length === c.lat_sym_ok && ok.length === c.n_ok, `${id}: LAT_SYM without the malformed rows`);
  } else if (c.kind === "olmk") {
    dots = rs.map((r) => (!r.raw || (!("conjecture" in r) && !r.ok) ? "Z" : r.cut_in_conjecture ? "A" : r.bind ? "R" : r.closure ? "F" : "N"));
    expect(rs.filter((r) => r.bind).length === c.bind && rs.filter((r) => r.cut_in_conjecture).length === c.ans, `${id}: OLMo K bind / ans`);
  } else {
    dots = rs.map((r) => (!r.raw || (!("conjecture" in r) && !r.ok) ? "Z" : r.closure ? "F" : "N"));
  }
  if ("reasoning_med" in c) expect(median(rs.map((r) => r.reasoning_tokens)) === c.reasoning_med, `${id}: reasoning_tokens median`);
  if ("relations_med" in c) expect(median(rs.map((r) => r.relations.length)) === c.relations_med, `${id}: relations median (v2.1)`);
  if ("parabola_ans" in c) expect(rs.filter((r) => r.parabola_in_conjecture).length === c.parabola_ans, `${id}: parabola_in_conjecture`);
  expect(JSON.stringify(dots) === JSON.stringify(c.dots), `${id}: the dots recounted in JS equal the pack's (${dots.join("")} vs ${c.dots.join("")})`);
  nCells++; nRows += rs.length;
}
function shortName(m) { return { "claude-opus-5-5": "Opus 5.5", "claude-fable-5-1": "Fable 5.1", "claude-sonnet-5-5": "Sonnet 5.5", "claude-haiku-5-5": "Haiku 5.5", "gemini-4-argon": "Argon" }[m] || m; }

// the values of BRIEF v1 §6 (the same list as pack_data.py; written again here so that the two routes do not share code)
const cc = (id) => pack.cells[id];
const V = [
  ["essay4.A.opus-5-5", "bind", 0], ["essay4.A.haiku-5-5", "floor", 19], ["essay4.A.haiku-5-5", "n", 19], ["b5bp.Bbp.opus-5-5", "bind", 6], ["b5bp.Bbp.sonnet-5-5", "bind", 2], ["b5bp.Bbp.fable-5-1", "bind", 0],
  ["arg5.Bbp", "bind", 20], ["arg5d.Bbp", "bind", 8], ["moy5c.opus", "bind", 10], ["moy5c.fable", "bind", 6], ["neq3.A/Q2.opus", "ans", 7], ["neq3.A/Q2.fable", "ans", 20], ["neq2f.A.fable", "ans", 0],
  ["neq6.medium.opus", "ans", 0], ["neq6.high.opus", "ans", 1], ["neq6.max.opus", "ans", 19], ["neq6.max.opus", "thinking_med", 8506.5], ["neq3.A/Q2.opus", "thinking_med", 1734.5],
  ["prf1.P5.opus", "END-only", 8], ["prf1.P5K.opus", "CHAIN", 10], ["prf1.P5K.fable", "CHAIN", 9], ["prf3.P5B.opus", "lat_sym", 10], ["prf3.P5B.fable", "lat_sym", 4], ["prf3.P5B.fable", "n_ok", 8],
  ["mnw1.conf/Q1f.opus", "ans", 19], ["mnw1.conf/Q1f.fable", "ans", 13], ["mnw1.cone/Q1.fable", "bind", 5], ["mnw1.cone/Q1.fable", "vertex", 5], ["mnw1.cone/Q1f.fable", "n", 11],
  ["olm1.natural", "floor", 0], ["olm1.think", "floor", 2], ["olm3.think", "floor", 5],
];
for (const [id, k, v] of V) expect(cc(id)[k] === v, `BRIEF §6 ${id}.${k} = ${cc(id)[k]} (brief ${v})`);
for (const [id, f] of [["neq3.A/Q2.opus", "results_neq3_moy5_20261019_claude-opus-5-5.jsonl"], ["neq3.A/Q2.fable", "results_neq3_moy5_20261019_claude-fable-5-1.jsonl"]])
  expect(median(rowsOf(f).filter((r) => r.arm === "A/Q2").map((r) => r.usage.output_tokens_details.thinking_tokens)) === cc(id).thinking_med, `${id}: the xhigh thinking median from usage`);

// v2: the values moved from entry P, written again here (the second route; not shared with pack_data.py)
const V2 = [["neq3.K.opus", "ans", 6], ["neq3.K.opus", "bind", 9], ["neq2f.K.fable", "ans", 7], ["olm1.natural.K", "bind", 2], ["olm1.think.K", "bind", 10], ["olm3.K", "bind", 10], ["mnw1.K.opus", "ans", 1], ["mnw1.K.fable", "ans", 4],
  ["essay4.K.fable-5-1", "bind", 19], ["b5bp.Bbp.sonnet-5-5", "reasoning_med", 1020.5], ["b5bp.Bbp.opus-5-5", "reasoning_med", 1742.5], ["b5bp.Bbp.fable-5-1", "reasoning_med", 2233], ["arg5.Bbp", "reasoning_med", 8468.5], ["arg5d.Bbp", "reasoning_med", 965],
  ["neq3.A/Q2.fable", "parabola_ans", 5], ["neq3.L-name/Q2.opus", "parabola_ans", 2], ["neq3.L-text/Q2.opus", "parabola_ans", 0]];
for (const [id, k, v] of V2) expect(cc(id)[k] === v, `v2 ${id}.${k} = ${cc(id)[k]} (P ${v})`);
// v2: the cards after 10-28 — every value of the pack is read again from the card's own output in JS (json key / jsonl), and the tally of the statuses is recounted
const Y = (rel) => JSON.parse(readFileSync(X + rel, "utf8"));
const dig = (o, ks) => ks.reduce((a, k) => a[k], o);
const PV = { olm60: [["fve", "olm60/control.json", ["C1", "fve"]]], olm61: [["apex_lat", "olm61/read_text_only.json", ["Q2", "apex", "lat"]], ["floor_fd", "olm61/read_text_only.json", ["Q2", "floor", "fd"]]],
  olm64: [["up", "olm64/read.json", ["Q1_P5B_lat_L32", "up"]], ["med", "olm64/read.json", ["Q1_P5B_lat_L32", "median_delta"]]], olm67: [["up", "olm67/read.json", ["Q1", "up"]], ["lens", "olm67/control.json", ["C1_lens", "all", "lens_med"]]],
  olm68: [["diff", "olm68/read.json", ["Q1", "diff"]]], olm69: [["L", "olm69/read.json", ["Q1", "L", "cut_word_in_cut_sentence"]]], olm70: [["u", "olm70/read.json", ["C_test_k1", "median_u_k1"]]], olm71: [["rows", "olm71/calibrate.json", ["BODY", "rows_nonempty"]]],
  olm72: [["rows", "olm72/calibrate.json", ["BODY", "rows_nonempty"]]], olm73: [["pos", "olm73/read.json", ["Q2", "pos"]]], olm74: [["pos", "olm74/read.json", ["Q2", "pos"]], ["L", "olm74/read.json", ["Q1", "median_L"]]], olm77: [["W", "olm77/control.json", ["C1_positive_1_8", "W"]]],
  olm78: [["rW", "olm78/read.json", ["Q1_layer48_word_order", "r_W"]]], olm79: [["pos", "olm79/control.json", ["C1_sensitivity_O_rows", "pos"]]], olm81: [["pos", "olm81/read.json", ["Q1_formula_only_O", "pos"]]],
  olm63: [["best", "olm63/read.json", ["S4", "all", "fve"]]], olm80: [["dw", "olm80/control.json", ["C1_words_instrument_calibration", "delta_word", "median"]]] };
let nPost = 0;
for (const p of pack.post) for (const [k, f, ks] of PV[p.id] || []) { expect(dig(Y(f), ks) === p.v[k], `post ${p.id}.${k}`); nPost++; }
const tk2 = ["opus-5-5", "fable-5-1"].flatMap((m) => rowsOf(`results_thk2_moy5_20261030_claude-${m}.jsonl`));
expect(JSON.stringify(tk2.map((r) => [r.thinking_tokens, !!r.ans_cut, !!r.summ_cut])) === JSON.stringify(pack.thk2_rows.map((r) => [r.think, r.ans, r.summ])), "thk2 rows");
const tally = { 判定: 0, 記述: 0, 較正: 0, 言えない: 0, 関門: 0 }; pack.post.forEach((p) => tally[p.grade5]++);   // v2.1: the five columns of the grade rule (BRIEF v2.1 §2-5), recounted in JS; their sum must be 20
expect(Object.values(tally).reduce((a, b) => a + b, 0) === 20 && pack.post.length === 20, "the five columns of the grade rule sum to 20");
expect(JSON.stringify(tally) === JSON.stringify(pack.post_tally.grade), "the five columns recounted in JS equal the pack's");
expect(pack.post.filter((p) => p.rule === "i").length + pack.post.filter((p) => p.rule === "ii").length === 20, "every card took rule (i) or (ii)");

// the drawing control in JS (the construction): the same definitions as the question's text, written separately from pack_data.py
const P = pack.construction.coords, sub = (a, b) => [a[0] - b[0], a[1] - b[1]], add = (a, b) => [a[0] + b[0], a[1] + b[1]], mul = (a, k) => [a[0] * k, a[1] * k], perp = (v) => [-v[1], v[0]];
const meet = (p, u, q, v) => { const d = u[0] * v[1] - u[1] * v[0], t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / d; return add(p, mul(u, t)); };
const fd = perp(sub(P.G, P.A)), gd = perp(sub(P.E, P.A)), Vv = meet(P.F, fd, P.E, gd), Dd = meet(P.G, sub(P.E, P.G), P.F, fd), ed = perp(fd);
const Kk = meet(P.F, sub(P.P_x, P.F), Dd, ed), Py = meet(P.P_x, perp(sub(P.P_x, P.F)), Kk, fd), Hh = meet(Py, ed, P.F, fd), Jj = meet(Hh, sub(P.E, P.G), P.E, gd);
const err = Math.max(...[[Vv, P.V], [Kk, P.K], [Py, P.P_y], [Jj, P.J]].map(([a, b]) => Math.hypot(a[0] - b[0], a[1] - b[1])));
expect(err < 1e-3, `the drawing control: K, P_y, J recomputed within 1e-3 (max ${err})`);
console.log(`data.mjs: ${nCells} cells · ${nRows} rows recounted from the jsonl in JS · BRIEF §6 ${V.length} values · drawing control max err ${err.toExponential(2)}`);
export const DATA = { config: CONFIG, ...pack, recount: { cells: nCells, rows: nRows, briefValues: V.length, v2Values: V2.length, postValues: nPost, drawingErr: err } };
