// data.mjs — the SECOND route: the build recounts the figure's numbers in JS straight from the inventory's raw rows (data/moy2_line_inventory.json) and from each read.json,
// and compares them with the pack that pack_moy2.py wrote. A disagreement stops the build (expect throws). Exports DATA = what the page carries (nothing typed by hand).
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const inv = JSON.parse(readFileSync(join(HERE, "data", "moy2_line_inventory.json"), "utf8"));
const pack = JSON.parse(readFileSync(join(HERE, "generated", "pack.json"), "utf8"));
const read = (n) => JSON.parse(readFileSync(join(HERE, "data", "read", `olm${n}.json`), "utf8"));
export const CONFIG = JSON.parse(readFileSync(join(HERE, "config.json"), "utf8"));
const expect = (cond, what) => { if (!cond) throw new Error(`data.mjs: the pack disagrees with the raw data: ${what}`); };
const r4 = (a, b) => (b ? Math.round((a / b) * 1e4) / 1e4 : 0);
const median = (a) => { const s = [...a].sort((x, y) => x - y), n = s.length; return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2; };

for (const arm of pack.arms) {
  const raw = inv.arms[arm.id].rows, A = arm.agg;
  const pf = raw.filter((r) => r.has_proof), calc = raw.filter((r) => r.calc), nonc = raw.filter((r) => !r.calc);
  const ln3 = (r) => !!(r.proof_v3 && r.proof_v3.LN_a), ln6 = (r) => !!(r.proof_v6 && r.proof_v6.LN6_a), out3 = (r) => !!(r.proof_v3 && r.proof_v3.OUTER_a), out6 = (r) => !!(r.proof_v6 && r.proof_v6.OUTER6_a);
  const parsed = raw.filter((r) => r.cls !== "NONE").length;
  const got = { parsed, n_proof: pf.length, LN3: pf.filter(ln3).length, LN6: pf.filter(ln6).length, OUT3: pf.filter(out3).length, OUT6: pf.filter(out6).length, CALC: calc.length, REJ: raw.filter((r) => r.rej6).length,
    REJ_calc: calc.filter((r) => r.rej6).length, TN: raw.filter((r) => r.tool_named).length, cap: raw.filter((r) => r.hit_cap).length, typ: raw.filter((r) => r.rej6_then_proof_LN6).map((r) => r.key).join(","),
    MIDO3_rate: r4(raw.filter((r) => r.cls === "MIDO3").length, parsed), EQ_rate: r4(raw.filter((r) => r.cls === "EQ").length, parsed), LN3_rate: r4(pf.filter(ln3).length, pf.length), LN6_rate: r4(pf.filter(ln6).length, pf.length),
    T_med: median(raw.map((r) => r.T)), cs: [calc.filter((r) => r.has_proof).length, calc.filter((r) => r.has_proof && ln3(r)).length, nonc.filter((r) => r.has_proof).length, nonc.filter((r) => r.has_proof && ln3(r)).length].join("/") };
  const want = { ...A, typ: A.typ.join(","), cs: [A.calc_split.n_proof, A.calc_split.LN3, A.noncalc_split.n_proof, A.noncalc_split.LN3].join("/") };
  for (const k of Object.keys(got)) expect(got[k] === want[k], `${arm.id} ${k}: JS ${got[k]} vs pack ${want[k]}`);
  expect(arm.rows.length === 60 && arm.rows.every((r, i) => r.k === raw[i].key && r.T === raw[i].T && r.cls === raw[i].cls && r.proof === raw[i].proof && r.rejf === (raw[i].rej6_first || "")), `${arm.id}: the rows the page carries are the raw rows (key, T, class, proof, reject sentence)`);
}
// the frozen rates against each read.json, in JS
const A = Object.fromEntries(pack.arms.map((a) => [a.id, a.agg]));
expect(read(119).Q1.LN_a_rate_proof.tool === A.olm119.LN3_rate && read(124).Q1.LN_a_rate_proof.rerun === A.olm124.LN3_rate && read(125).Q1.LN_a_rate_proof.use === A.olm125.LN3_rate && read(127).Q1.LN_a_rate_proof.rerun === A.olm127.LN3_rate, "LN v3 rates = read.json Q1");
expect(read(118).Q1.LN_a_rate_proof.olm113 === A.olm113.LN3_rate && read(118).Q1.LN_a_rate_proof.olm117 === A.olm117.LN3_rate, "olm118 Q1 rates");
expect([124, 125, 127].every((n) => read(n).gates.G1_parsed === A[`olm${n}`].parsed), "G1 parsed counts");
expect(Object.entries(read(126).Q2.LN6_rate_proof).every(([a, v]) => A[a].LN6_rate === v), "v6 LN rates = olm126 Q2");
expect(JSON.stringify(read(126).Q2.frozen) === JSON.stringify(read(126).Q2.v6), "olm126: the 7 frozen verdicts are the same under v6");
// the verdicts the page shows = the read.json verdicts (G1-failed arms have none)
for (const [a, v] of Object.entries(pack.verdicts)) { if (pack.arms.find((x) => x.id === a).g1fail) expect(v.read === null, `${a} has no verdict`); else expect(v.calc === v.read, `${a}: ${v.calc} = ${v.read}`); }
// the brief's values (BRIEF §2), in JS
expect(pack.arms.map((a) => `${a.agg.LN3}/${a.agg.n_proof}`).join(" ") === "5/41 7/46 14/44 4/37 4/37 9/40 3/35", "BRIEF §2 item 1");
expect(pack.arms.map((a) => a.agg.parsed).join(" ") === "50 50 48 46 45 45 40", "BRIEF §2 item 3");
expect(pack.arms.map((a) => a.agg.typ.length).join(" ") === "0 0 3 2 1 3 0", "BRIEF §2 item 4 (b2_j07 type)");
expect(pack.scenes.S8.loop_count === 343 && pack.scenes.S10.loop_count === 542, "BRIEF §2 item 10 (loops)");
expect(pack.recount.n === 20 && pack.recount.ok === 20, "BRIEF §2 item 11 (20 / 20)");
expect(Math.abs(pack.geo.dTc - pack.geo.dTh) < 1e-3 && pack.geo.gap_refl > 1, "the configuration: apex true, reflection of Th is not Tc");
// v1.1: the four arms' rejects among calc rows (F1) and the Fisher tests (F4), recounted in JS from the raw rows
const rawA = (a) => inv.arms[a].rows, rc = (a) => [rawA(a).filter((r) => r.calc && r.rej6).length, rawA(a).filter((r) => r.calc).length];
const four = ["olm119", "olm124", "olm125", "olm127"].map(rc);
expect(four.reduce((s, x) => s + x[0], 0) === pack.four.num && four.reduce((s, x) => s + x[1], 0) === pack.four.den && pack.four.num === 42 && pack.four.den === 56, "BRIEF v1.1 §2 item 12 (four arms 42 / 56)");
const lnp = (a) => { const p = rawA(a).filter((r) => r.has_proof); return [p.filter((r) => r.proof_v3 && r.proof_v3.LN_a).length, p.length]; };
const comb = (n, k) => { let c = 1; for (let i = 1; i <= k; i++) c = (c * (n - k + i)) / i; return c; };
const fisherJS = (a, n1, b, n2) => { const K = a + b, N = n1 + n2, pr = (x) => (comb(n1, x) * comb(n2, K - x)) / comb(N, K), p0 = pr(a); let s = 0; for (let x = Math.max(0, K - n2); x <= Math.min(K, n1); x++) if (pr(x) <= p0 * (1 + 1e-7)) s += pr(x); return Math.min(1, s); };
const grp = { pool_f: [lnp("olm122")[0] + lnp("olm124")[0], lnp("olm122")[1] + lnp("olm124")[1]], pool_i: [lnp("olm125")[0] + lnp("olm127")[0], lnp("olm125")[1] + lnp("olm127")[1]] }, kOf = (id) => grp[id] || lnp(id);
for (const f of pack.fisher) { const [x, y] = [kOf(f.x), kOf(f.y)]; expect(Math.abs(fisherJS(x[0], x[1], y[0], y[1]) - f.p) < 1e-4, `Fisher ${f.x} vs ${f.y}: JS ${fisherJS(x[0], x[1], y[0], y[1])} vs pack ${f.p}`); }
expect(pack.brief_check.n === 23 && pack.brief_check.ok === 23, "BRIEF §2 items 1–23");
// v1.3: item 22 in JS from the raw rows (olm127's rejecting rows: 5 at the cap, 1 reaches a proof field without the line symmetry) · H1: the two rows of state 13 have no REJ6 · H6: the extra rejects of olm119 / olm122
{ const rj = inv.arms.olm127.rows.filter((r) => r.rej6); expect(rj.filter((r) => r.hit_cap).length === 5 && rj.filter((r) => r.has_proof).map((r) => r.key).join() === "b2_j11" && !rj.some((r) => r.has_proof && r.proof_v6 && r.proof_v6.LN6_a), "v1.3 item 22");
  const k8 = inv.arms.olm127.rows.find((r) => r.key === pack.scenes.S8.key), k10 = inv.arms.olm127.rows.find((r) => r.key === pack.scenes.S10.key); expect(pack.scenes.S8.key === "b2_j08" && pack.scenes.S10.key === "b1_j13" && !k8.rej6 && !k10.rej6, "v1.3 H1: b2_j08 / b1_j13 have no REJ6");
  expect(["olm119", "olm122"].flatMap((a) => inv.arms[a].rows.filter((r) => r.rej6 && !r.calc).map((r) => r.key)).join() === "b2_j08,b1_j19", "v1.3 H6: b2_j08 · b1_j19"); }
// v1.2: the Fisher pairs on each side of the 0.05 reference tick (G7) · the scene rows' reflected point (G1) · the band edges printed (G8), in JS from the raw data
expect(JSON.stringify(pack.fisher.filter((f) => f.p < 0.05).map((f) => [f.x, f.y])) === JSON.stringify(pack.fisher_below) && pack.fisher.filter((f) => f.p >= 0.05).length === 6, "G7: 6 pairs above 0.05, 1 below");
const r125 = Object.fromEntries(inv.arms.olm125.rows.map((r) => [r.key, r]));
for (const [k, w] of Object.entries(pack.slip0.refl)) expect(new RegExp(`^\\s*2F\\s*-\\s*${w}\\b`).test(r125[k].rej6_start), `G1: ${k} reflects ${w}`);
expect(r125.b1_j17.proof.includes(pack.slip0.phrase) && !r125.b0_j16.proof_v6_ln_hits.length, "G1: the phrase is in S1's proof field; S2 has no line-symmetry hit");
expect(JSON.stringify(pack.edges.olm124.map((e) => e[0])) === JSON.stringify([0.122 - 0.06, 0.122 + 0.06, 0.318 - 0.06, 0.318 + 0.06].map((v) => Math.round(v * 1000) / 1000)) && JSON.stringify(pack.edges.olm125.map((e) => e[0])) === JSON.stringify([0.048, 0.168]), "G8: olm124 / olm125 edges = base ± 0.06");
export const DATA = { config: CONFIG, ...pack };
