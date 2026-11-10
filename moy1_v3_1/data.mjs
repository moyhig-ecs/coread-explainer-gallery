// data.mjs — the SECOND route of every number: the build counts the headline numbers again, in JS, straight from the frozen files (not from pack_moy1.py's code),
// and compares them with the pack that pack_moy1.py wrote. A disagreement stops the build (expect throws). Exports DATA = what the page carries (nothing typed by hand).
// The predicates here are a separate JS port of the entry's predicates (NOTES.md lists them); the recount of the page's counts is therefore not the same code as the Python one.
import { readFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = process.env.MOY1_REPO || join(HERE, "data");   // bundle: the frozen files are copied under data/ at their repo paths
// bundle: the `git log` answers recorded from the house repo (data/git_facts.json) when REPO is not a git checkout
const gitFact = (args) => existsSync(join(REPO, ".git")) ? execFileSync("git", ["-C", REPO, ...args]).toString() : JSON.parse(readFileSync(join(HERE, "data", "git_facts.json"), "utf8")).answers[JSON.stringify(args)];
const rd = (rel) => readFileSync(join(REPO, rel));
const J = (rel) => JSON.parse(rd(rel).toString("utf8"));
export const CONFIG = JSON.parse(readFileSync(join(HERE, "config.json"), "utf8"));
const pack = JSON.parse(readFileSync(join(HERE, "generated", "pack.json"), "utf8"));
const expect = (cond, what) => { if (!cond) throw new Error(`data.mjs: the pack disagrees with the frozen files / with itself: ${what}`); };
const md5 = (b) => createHash("md5").update(b).digest("hex");
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);

// ---- 0. the sources are the frozen ones (md5 from the BRIEF §1)
for (const [k, s] of Object.entries(pack.sources)) expect(md5(rd(s.path)) === s.md5, `${k}: md5 of ${s.path}`);

// ---- 1. geometry: recount the distances from the prompt's coordinates
const cfg = J("probes/moy1-claude5-replication/results/replication_config_frozen.json");
const P = {}; for (const m of cfg.prompts.open.matchAll(/^(O1|O2|X1|X2|X3|X4|He|Hi) = \(([-\d.]+), ([-\d.]+)\)/gm)) P[m[1]] = [Number(m[2]), Number(m[3])];
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]), mid = (a, b) => [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
const cO = mid(P.O1, P.O2), rO = dist(P.O1, P.O2) / 2, cH = mid(P.He, P.Hi), rH = dist(P.He, P.Hi) / 2, X = ["X1", "X2", "X3", "X4"].map((k) => P[k]);
expect(X.every((x) => Math.abs(dist(x, cO) / rO - 1) < 1e-5), "X1..X4 are on the circle with diameter O1O2");
expect(X.every((x, i) => Math.abs(dist(x, cH) / rH - pack.geometry.ratio_H[i]) < 1e-12 && Math.abs(dist(x, cH) / rH - 1) > 0.1), "the HeHi circle ratios");
expect(cfg.prompts.blocked.startsWith(cfg.prompts.open) && cfg.prompts.blocked.length - cfg.prompts.open.length === 324 && pack.prompts.tail_len === 324, "V5: blocked = open + 324 characters");

// ---- 2. the 20 rows: parse the last JSON, read the answer field, count the sentences (a JS port of the predicates)
const rawDecode = (s, b) => {            // like Python's json.JSONDecoder().raw_decode(s[b:]) for an object that starts at b
  let depth = 0, inStr = false, esc = false;
  for (let i = b; i < s.length; i++) {
    const ch = s[i];
    if (inStr) { if (esc) esc = false; else if (ch === "\\") esc = true; else if (ch === '"') inStr = false; continue; }
    if (ch === '"') inStr = true; else if (ch === "{") depth++; else if (ch === "}") { depth--; if (depth === 0) { try { return [JSON.parse(s.slice(b, i + 1)), i + 1 - b]; } catch (_) { return null; } } }
  }
  return null;
};
const parseField = (text, field) => {
  if (!text) return ""; const s = String(text).replace(/```(?:json)?/g, ""); let best = "", idx = 0;
  for (;;) { const b = s.indexOf("{", idx); if (b < 0) break; const r = rawDecode(s, b);
    if (r) { const [obj, end] = r; if (obj && typeof obj === "object" && !Array.isArray(obj) && field in obj) best = String(obj[field] || ""); idx = b + Math.max(1, end); } else idx = b + 1; }
  return best;
};
const NUM = "(?:_?\\{?(?:1|2|₁|₂)\\}?)";
const PRED_O = new RegExp("(diameter|midpoint|center|centre)\\s+(?:is\\s+|of\\s+|at\\s+)?(?:the\\s+)?(?:line\\s+)?(?:segment\\s+)?(?:(?:joining|connecting|between)\\s+)?(?:the\\s+)?(?:two\\s+)?(?:centers\\s+)?(?:\\\\\\(\\s*)?O" + NUM + "\\s*(?:and\\s+)?O", "gi");
const PRED_HEHI_DIAM = /diameter\s+(?:is\s+)?(?:the\s+)?(?:line\s+)?(?:segment\s+)?(?:(?:joining|connecting|between)\s+)?(?:\\\(\s*)?(?:HeHi|He and Hi|H_e)/gi;
const O_SPELL = /O\s*_?\{?[1₁]\}?\s*(?:and\s+|,\s*|-\s*)?O\s*_?\{?[2₂]\}?/, HEHI_TOK = /(?<![A-Za-z])(?:He|Hi)(?![a-z])|H_\{?[ei]\}?/, CENTERISH = /diameter|center|centre|midpoint|mid-?point|radius/i;
const CONCYC = /concyclic|cocircular|on (?:a|one|the) circle|lie on (?:a|one) circle|same circle/i, HEHI_W = /\bHe\b|\bHi\b/;
const reading = (a) => (O_SPELL.test(a) && CENTERISH.test(a) ? "o1o2" : HEHI_TOK.test(a) && CENTERISH.test(a) ? "hehi" : CONCYC.test(a) ? "bare" : "other");
const prose = (t) => { const ps = t.trim().split(/\n\s*\n/).filter((p) => p.trim()); return ps.length ? ps[ps.length - 1].trim() : ""; };
const pc1 = J("probes/olmo3-pc1-cue-invariance/results/pc1_runs.json").rows.filter((r) => r.cue_tag === "nlnl");
expect(pc1.length === 20, "20 rows of cue \\n\\n");
const mine = pc1.map((r) => {
  const c = r.content, conj = parseField(c, "conjecture"), ans = conj;                                  // v3: the answer field is the last JSON's conjecture; a row with no JSON has none (decision 1; the v2 last-paragraph fallback is dropped)
  return { cond: r.condition, seed: r.seed, label: r.label, reading: ans ? reading(ans) : "other", he: (c.match(PRED_HEHI_DIAM) || []).length, o: (c.match(PRED_O) || []).length, jlit: c.indexOf('{"conjecture"'), json0: /^\s*\{\s*"conjecture"/.test(c) && c.search(/\{\s*"conjecture"/) === 0, hw: HEHI_W.test(c), n: c.length };
});
const by = (cond) => mine.filter((x) => x.cond === cond), count = (xs, f) => xs.filter(f).length;
const tally = (xs, key) => xs.reduce((m, x) => ((m[x[key]] = (m[x[key]] || 0) + 1), m), {});
for (const x of pack.rows) { const m = mine.find((y) => y.cond === x.cond && y.seed === x.seed); expect(m.reading === x.reading && m.n === x.n_chars && m.label === x.label, `row ${x.id}: reading ${m.reading} / pack ${x.reading}`); expect(m.he === x.he_diam.length && m.o === x.o_name.length && m.hw === x.has_hehi_word, `row ${x.id}: sentence counts`); }
expect(eq(tally(by("open"), "label"), { "B-attractor": 5, "B-stuck-L1": 5 }) && eq(tally(by("blocked"), "label"), { "B-bind": 7, "B-attractor": 3 }), "V1 / V2 frozen labels");
expect(count(by("open"), (x) => x.reading === "bare") === 8 && count(by("open"), (x) => x.reading === "o1o2" || x.reading === "hehi") === 0, "V3: open's answer field: bare 8, never O1O2 / He-Hi");
expect(eq(by("blocked").map((x) => x.jlit), [8688, 393, 5193, 0, 1992, 0, 10095, 16286, -1, 0]), "V4: first {\"conjecture\" in blocked");
expect(count(by("blocked"), (x) => x.reading === "o1o2") === 6 && count(by("blocked"), (x) => x.reading === "hehi") === 3 && count(by("blocked"), (x) => x.jlit < 0) === 1 && by("blocked").find((x) => x.jlit < 0).seed === 8, "blocked's answer field: O1O2 6, He-Hi 3, no JSON 1 (s8)");
expect(count(by("open"), (x) => x.o > 0) === 0 && count(by("blocked"), (x) => x.o > 0) === 7 && count(by("open"), (x) => x.he > 0) === 1 && count(by("blocked"), (x) => x.he > 0) === 5, "the sentence counts 0/10 -> 7/10 and 1/10 -> 5/10");
expect(eq(by("blocked").filter((x) => x.json0).map((x) => x.seed), [3, 5, 9]) && eq(by("open").filter((x) => x.json0).map((x) => x.seed), [3, 9]), "rows that start with the JSON");

// ---- 3. the cue table (three cues; the frozen label; cap rows noted)
const lab = (rows, cond, noCap) => rows.filter((r) => r.condition === cond && (!noCap || !r.hit_cap)).reduce((m, r) => ((m[r.label] = (m[r.label] || 0) + 1), m), {});
const scr = J("probes/olmo3-base-bf16-screen/results/screen_olmo3_base_bf16.json").rows, sp = J("probes/olmo3-pc1-cue-invariance/results/pc1_runs.json").rows.filter((r) => r.cue_tag === "space");
expect(lab(scr, "blocked", true)["B-bind"] === 2 && lab(sp, "blocked", true)["B-bind"] === 4 && lab(pc1, "blocked", true)["B-bind"] === 7, "cue table: blocked bind 2 / 4 / 7");
expect(pack.cue_table.nl.blocked.labels_primary["B-bind"] === 2 && pack.cue_table.sp.blocked.labels_primary["B-bind"] === 4 && pack.cue_table.nn.blocked.labels_primary["B-bind"] === 7, "the pack's cue table");

// ---- 4. cmt13: the two moments and the pairs
const c13 = J("probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt13_blocked_bind_moment_in_thinking.json");
const OG = new Set(pack.cmt13.OG), HG = new Set(pack.cmt13.HG), sum = (hs, G) => hs.filter((h) => G.has(h.head)).reduce((a, h) => a + h.contrib, 0);
for (const k of ["att|F5a-2|s1", "cut|F5a-2|s1"]) {
  const x = c13.sites[k], hs = x.top_heads.slice(0, 10), s = pack.cmt13.sites.find((q) => q.key === k);
  expect(Math.abs(sum(hs, OG) - s.o_sum) < 1e-12 && Math.abs(sum(hs, HG) - s.he_sum) < 1e-12 && x.delta_out === s.delta_out && x.t === s.t, `cmt13 ${k}`);
}
expect(c13.sites["att|F5a-2|s1"].delta_out === -4.3984375 && c13.sites["cut|F5a-2|s1"].delta_out === 1.2109375 && c13.sites["att|F5a-2|s1"].t === 289 && c13.sites["cut|F5a-2|s1"].t === 397, "V6");
expect(pack.cmt13.sites.length === 16 && count(pack.cmt13.sites, (s) => s.kind === "att") === 5 && count(pack.cmt13.sites, (s) => s.kind === "cut") === 11, "16 sites: att 5, cut 11");
expect(pack.cmt13.jaccard["cut~att"] === c13.compare.jaccard_top10["cut~att"].mean && pack.cmt13.jaccard["cut~cut"] === c13.compare.jaccard_top10["cut~cut"].mean && pack.cmt13.jaccard["cut~concl_bind"] === c13.compare.jaccard_top10["cut~concl_bind"].mean, "V7");
expect(count(pack.cmt13.sites, (s) => s.kind === "att" && s.l50 && s.l50[0] === 1) === 4 && count(pack.cmt13.sites, (s) => s.kind === "cut" && s.l50 && s.l50[0] === 1) === 3, "V8");

// ---- 5. models and Think
const suite = J("ConstructGap/exp/moy_suite_report.json").moy1_circle_discriminator;
for (const m of pack.models) expect(suite[m.model].open.bind === m.open.bind && suite[m.model].blocked.bind === m.blocked.bind && suite[m.model].blocked.n === m.blocked.n, `model ${m.model}`);
const th = J("probes/olmo3-behavior-screen/results/screen_olmo-3_32b.json").rows;
expect(th.filter((r) => r.condition === "open" && r.done_reason !== "length" && r.label === "B-stuck-L1").length === 9 && th.filter((r) => r.condition === "blocked" && r.done_reason !== "length" && r.label === "B-bind").length === 7, "V11");

// ---- 6. v2 (olm59): the second route, in JS, with its own code: (a) the md5 of the 120 npz files against the manifest, (b) the aggregate recounted from the windows side file (float values of the arrays) and compared with read.json,
//      (c) the first naming token found again from the carried masks, (d) the carried series' window means (4-digit rounding), (e) cmt5's two labels recounted from cmt5.json, (f) control.json against the pack.
const O59 = "ConstructGap/exp/olm59/", o59 = pack.olm59, R59 = J(O59 + "read.json"), C59 = J(O59 + "control.json");
const man = JSON.parse(readFileSync(join(HERE, "generated", "olm59_manifest.json"), "utf8"));
expect(md5(rd(O59 + "read.json")) === o59.sources["read.json"].md5 && md5(rd(O59 + "control.json")) === o59.sources["control.json"].md5, "olm59 read.json / control.json md5");
const names59 = Object.keys(man.rows).sort();
expect(names59.length === 120 && names59.every((n) => md5(rd(O59 + "rows/" + n)) === man.rows[n].md5), "the 120 npz files: md5 against the manifest");
expect(md5(names59.map((n) => `${n} ${man.rows[n].md5}\n`).join("")) === o59.sources.rows.manifest_md5 && man.manifest_md5 === o59.sources.rows.manifest_md5, "the manifest's md5");
const W59 = JSON.parse(readFileSync(join(HERE, "generated", "olm59_windows.json"), "utf8"));
const meanOf = (xs) => xs.reduce((a, b) => a + b, 0) / xs.length, medOf = (xs) => { const t = [...xs].sort((a, b) => a - b), n = t.length; return n % 2 ? t[(n - 1) / 2] : (t[n / 2 - 1] + t[n / 2]) / 2; };
const GR = ["close", "mid", "ans", "think"];
let keys59 = 0;
for (const ev of ["o_diam", "h_diam"]) for (const oc of ["all", "B-bind", "B-attractor"]) GR.forEach((g, gi) => {
  const rs = W59.events[ev].filter((e) => oc === "all" || e.label_json === oc), d = rs.map((e) => meanOf(e.win[gi].slice(32)) - meanOf(e.win[gi].slice(0, 32))), key = `${ev}|${g}|${oc}`, r = R59.Q3_desc[key];
  expect(rs.length === r.n && d.filter((x) => x > 0).length === r.after_gt_before && Math.abs(medOf(d) - r.median_diff) < 1e-6, `olm59 Q3 ${key}: JS ${rs.length}/${d.filter((x) => x > 0).length}/${medOf(d)} vs read.json ${r.n}/${r.after_gt_before}/${r.median_diff}`);
  const c = o59.agg[ev].groups[g][oc]; expect(c.n === r.n && c.up === r.after_gt_before && c.med === r.median_diff, `the pack carries read.json's own values: ${key}`); keys59++;
});
const q1r = W59.events.o_diam.filter((e) => e.kind === "think" && e.label_json === "B-bind"), q1d = q1r.map((e) => meanOf(e.win[0].slice(32)) - meanOf(e.win[0].slice(0, 32))), q2d = W59.events.h_diam.map((e) => meanOf(e.win[0].slice(32)) - meanOf(e.win[0].slice(0, 32)));
expect(q1d.length === 36 && q1d.filter((x) => x > 0).length === 6 && Math.abs(medOf(q1d) - R59.Q1_think_bind_o_diam_close.median_diff) < 1e-6 && q2d.length === 34 && q2d.filter((x) => x > 0).length === 17 && Math.abs(medOf(q2d) - R59.Q2_any_h_diam_close.median_diff) < 1e-6, "olm59 Q1 / Q2");
expect(eq(o59.Q1, { n: 36, up: 6, med: R59.Q1_think_bind_o_diam_close.median_diff, thr: 0.7 }) && eq(o59.Q2, { n: 34, up: 17, med: R59.Q2_any_h_diam_close.median_diff, thr: 0.6 }), "the pack's Q1 / Q2");
expect(W59.events.o_diam.length === 59 && W59.events.h_diam.length === 34 && W59.rows_with.o_diam === R59.counts.rows_with_o_diam && W59.rows_with.h_diam === R59.counts.rows_with_h_diam, "olm59 event counts");
for (const [key, R, flag, bit] of [["S_O", o59.S_O, "o_diam", 2], ["S_H", o59.S_H, "h_diam", 3]]) {
  const first = R.mask.findIndex((m) => (m >> bit) & 1);
  expect(first === R.event && R.mask.length === R.n && GR.every((g) => R.series[g].length === R.n), `${key}: the first ${flag} token found again in JS from the carried mask`);
  GR.forEach((g, gi) => expect(Math.abs(meanOf(R.series[g].slice(R.event - 32, R.event)) - R.before[gi]) < 2e-4 && Math.abs(meanOf(R.series[g].slice(R.event, R.event + 32)) - R.after[gi]) < 2e-4, `${key} ${g}: window means from the carried series`));
  const ev = W59.events[flag].find((e) => e.id === R.id); expect(ev && ev.e === R.event && GR.every((g, gi) => Math.abs(meanOf(ev.win[gi].slice(0, 32)) - R.before[gi]) < 1e-6 && Math.abs(meanOf(ev.win[gi].slice(32)) - R.after[gi]) < 1e-6), `${key}: the windows file agrees with the carried means`);
}
for (const [key, R, flag] of [["S_O", o59.S_O, "o_diam"], ["S_H", o59.S_H, "h_diam"]]) GR.forEach((g, gi) => {
  const ds = W59.events[flag].map((e) => [e.id, meanOf(e.win[gi].slice(32)) - meanOf(e.win[gi].slice(0, 32))]), v = ds.find(([id]) => id === R.id)[1];
  expect(eq(R.rank[g], [1 + ds.filter(([, x]) => x > v).length, 1 + ds.filter(([, x]) => Math.abs(x) > Math.abs(v)).length, ds.length]), `${key} ${g}: the rank among the rows of the aggregate`);
});
const sceneShort = (flag, pred) => W59.events[flag].filter(pred).sort((a, b) => a.N - b.N);
expect(sceneShort("o_diam", (e) => e.kind === "think" && e.label_json === "B-bind")[0].id === o59.S_O.id && sceneShort("h_diam", (e) => e.label_json === "B-attractor")[0].id === o59.S_H.id, "the scene rows: the shortest generation that satisfies the predicate");
// (e) cmt5's two labels, recounted from cmt5.json by the labels themselves
const c5 = J("probes/olmo3-f5-think-prefix/results/tsd_r5b/cmt5_first_token_fixed_sampling.json").cells, tl = (xs) => xs.reduce((m, x) => ((m[x] = (m[x] || 0) + 1), m), {});
for (const p of ["think", "answer", "natural"]) {
  const rs = [...c5[`F5a-2|${p}`].rows, ...c5[`F5b-1|${p}`].rows], full = tl(rs.map((r) => r.label)), field = tl(rs.map((r) => r.label_json_fields)), t = o59.cmt5_two[p];
  expect(rs.length === t.n && eq(Object.entries(full).sort(), Object.entries(t.full).sort()) && eq(Object.entries(field).sort(), Object.entries(t.field).sort()), `cmt5 ${p}: the two labels`);
}
expect(R59.labels_full_vs_answer_field["think|B-bind|B-bind"] === 36 && R59.labels_full_vs_answer_field["answer|B-bind|B-bind"] === 4 && o59.cmt5_two.think.full["B-bind"] === 40 && o59.cmt5_two.answer.full["B-bind"] === 8 && o59.cmt5_two.think.field["B-bind"] === 36 && o59.cmt5_two.answer.field["B-bind"] === 4, "cmt5: bind 40 / 8 (whole text) and 36 / 4 (answer field)");
// (f) the controls
expect(eq(o59.control.C1, C59.C1) && C59.C1.fve === 0.4393749237060547 && C59.C1.l0 === 235.35857843137254 && C59.C1.n === 4080 && C59.C2.equal === 120 && C59.C3["F5a-2"] === "20 / 20" && C59.C3["F5b-1"] === "20 / 20" && C59.pass.C1 && C59.pass.C2 && C59.pass.C3, "olm59 controls");
console.log(`data.mjs olm59: ${keys59} Q3 keys recounted · 120 md5 · scenes ${o59.S_O.id} @${o59.S_O.event} / ${o59.S_H.id} @${o59.S_H.event} · cmt5 labels`);

// ---- 7. v2.1 (olm62 + the card tree): the second route, in JS. (a) olm62's read.json / control.json md5 and the pack's copy of them, (b) the events recounted from the windows side file (the 64-token windows of the four groups and of the
//      formula-character share): counts, medians, splits, the by-group counts, exactly as in read.json; the rank correlation by AVERAGE ranks as a sanity bound (the card's own rule is numpy's ordinal ranks, which the pack and
//      check_claims.py reproduce to 1e-12; JS cannot reproduce numpy's tie order), (c) the carried scatter points against the recount, (d) tree_src.json: clusters, nodes, the four in-tree cards' clusters, the dates of the cards outside, (e) the marks of config.json.
const O62 = "ConstructGap/exp/olm62/", o62 = pack.olm62, R62 = J(O62 + "read.json"), C62 = J(O62 + "control.json");
expect(md5(rd(O62 + "read.json")) === o62.sources["read.json"].md5 && md5(rd(O62 + "control.json")) === o62.sources["control.json"].md5, "olm62 read.json / control.json md5");
const W62 = JSON.parse(readFileSync(join(HERE, "generated", "olm62_windows.json"), "utf8"));
const rankAvg = (xs) => { const ix = xs.map((v, i) => [v, i]).sort((a, b) => a[0] - b[0]), r = new Array(xs.length); for (let i = 0; i < ix.length;) { let j = i; while (j + 1 < ix.length && ix[j + 1][0] === ix[i][0]) j++; for (let k = i; k <= j; k++) r[ix[k][1]] = (i + j) / 2 + 1; i = j + 1; } return r; };
const pearson = (a, b) => { const ma = meanOf(a), mb = meanOf(b); let sab = 0, saa = 0, sbb = 0; a.forEach((x, i) => { sab += (x - ma) * (b[i] - mb); saa += (x - ma) ** 2; sbb += (b[i] - mb) ** 2; }); return sab / Math.sqrt(saa * sbb); };
let n62 = 0;
for (const ev of ["o_diam", "h_diam"]) {
  const E = W62.events[ev], r = R62[ev], win = (xs, a, b) => meanOf(xs.slice(a, b));
  const dm = E.map((e) => win(e.grp[1], 32, 64) - win(e.grp[1], 0, 32)), dma = E.map((e) => win(e.tf, 32, 64) - win(e.tf, 0, 32)), med = medOf(dma), cnt = (xs, f) => xs.filter(f).length;
  const flat = dm.filter((_, i) => dma[i] <= 0), upd = dm.filter((_, i) => dma[i] > 0), lo = dm.filter((_, i) => dma[i] <= med), hi = dm.filter((_, i) => dma[i] > med);
  expect(E.length === r.n && cnt(dma, (x) => x > 0) === r.math_up && Math.abs(med - r.math_median_diff) < 1e-12, `olm62 ${ev}: n / math_up / median (JS ${E.length} / ${cnt(dma, (x) => x > 0)} / ${med} vs read.json ${r.n} / ${r.math_up} / ${r.math_median_diff})`);
  expect(`${cnt(flat, (x) => x > 0)} / ${flat.length}` === r.mid_up_when_math_flat && `${cnt(upd, (x) => x > 0)} / ${upd.length}` === r.mid_up_when_math_up && Math.abs(medOf(flat) - r.mid_median_when_math_flat) < 1e-6, `olm62 ${ev}: mid up when the text moves / does not`);
  expect(`${cnt(lo, (x) => x > 0)} / ${lo.length}` === r.split_at_median_math.low && `${cnt(hi, (x) => x > 0)} / ${hi.length}` === r.split_at_median_math.high, `olm62 ${ev}: the split at the median of the formula share`);
  GR.forEach((g, gi) => { const dg = E.map((e) => win(e.grp[gi], 32, 64) - win(e.grp[gi], 0, 32)).filter((_, i) => dma[i] <= 0); expect(`${cnt(dg, (x) => x > 0)} / ${dg.length}` === r.by_group_math_flat[g], `olm62 ${ev}: by group ${g}`); });
  expect(Math.abs(pearson(rankAvg(dm), rankAvg(dma)) - r.spearman_mid_math) < 0.02, `olm62 ${ev}: the rank correlation by average ranks stays within 0.02 of the card's ordinal-rank value`);
  expect(o62.events[ev].length === E.length && o62.events[ev].every((x, i) => x.id === E[i].id && Math.abs(x.dmid - dm[i]) < 6e-6 && Math.abs(x.dmath - dma[i]) < 6e-6), `olm62 ${ev}: the carried scatter points are the recount's`); n62 += E.length;
}
expect(eq(o62.read.o_diam, R62.o_diam) && eq(o62.read.h_diam, R62.h_diam) && eq(o62.read.Q1, R62.Q1) && eq(o62.read.Q2, R62.Q2) && o62.read.Q3_pooled_token_spearman_mid_math === R62.Q3_pooled_token_spearman_mid_math && o62.read.n_tokens === R62.n_tokens && eq(o62.control, C62) && C62.pass.C1 && C62.pass.C2, "the pack carries olm62's own values and controls");
expect(R62.o_diam.n === 59 && R62.o_diam.math_up === 48 && R62.h_diam.n === 34 && R62.h_diam.math_up === 8 && R62.o_diam.mid_up_when_math_flat === "7 / 11" && R62.Q3_pooled_token_spearman_mid_math === 0.4152617665861453 && R62.o_diam.spearman_mid_math === 0.7804792518994741 && R62.h_diam.spearman_mid_math === 0.21161191749427039, "BRIEF v2.1 §2 check values");
// the tree
const TREE_REL = pack.tree.source.path, TS = J(TREE_REL);
expect(md5(rd(TREE_REL)) === pack.tree.source.md5, "tree_src.json md5");
expect(TS.clusters.length === 9 && TS.nodes.length === 78 && TS.clusters.reduce((a, c) => a + c.members.length, 0) === 78, "the tree: 9 clusters · 78 nodes");
const nodeOf = Object.fromEntries(TS.nodes.map((n) => [n.id, n]));
expect(TS.clusters.every((c, i) => { const p = pack.tree.clusters[i], ds = c.members.map((m) => nodeOf[m].date.slice(5)).sort(); return p.id === c.id && p.name === c.name && p.sub === c.sub && p.n === c.members.length && p.span[0] === ds[0] && p.span[1] === ds[ds.length - 1]; }), "the tree: the carried clusters (name · sub · n · span)");
for (const id of ["cmt5", "cmt13", "olm4", "olm7"]) { const c = pack.tree.cards[id]; expect(c.zone === nodeOf[id].cluster && c.label === nodeOf[id].label && c.outcome === nodeOf[id].outcome && c.date === nodeOf[id].date.slice(5), `the tree: card ${id}`); }
expect(pack.tree.cards.cmt5.zone === "C1" && pack.tree.cards.cmt13.zone === "C2" && pack.tree.cards.olm4.zone === "C3" && pack.tree.cards.olm7.zone === "C3" && pack.tree.clusters.map((c) => c.n).join() === "6,13,10,6,13,8,7,11,4", "BRIEF v2.1 §2 check values (the tree)");
for (const [id, c] of Object.entries(pack.tree.cards)) {                // the dates of the cards outside the tree: from the record's own name; for the two data files, from git's last commit of the file (a read)
  if (c.date_from === "name") { const m = /_(\d{8})\.md$/.exec(c.file); expect(m && `${m[1].slice(4, 6)}-${m[1].slice(6, 8)}` === c.date, `card ${id}: the date in the record's name`); }
  else if (c.date_from === "git") expect(gitFact(["log", "-1", "--format=%ad", "--date=short", "--", c.file]).trim().slice(5) === c.date, `card ${id}: git's date of the file`);
}
// the marks of config.json (one list of card ids per state; the ledger and the map show their own)
const NST = CONFIG.chapters[CONFIG.chapters.length - 1][2] + 1;
expect(Array.isArray(CONFIG.card_marks) && CONFIG.card_marks.length === NST && CONFIG.card_marks.every((a) => Array.isArray(a) && a.every((id) => pack.tree.cards[id])), "config.json card_marks: one list per state, every id is a known card");
expect(Object.keys(pack.tree.cards).every((id) => CONFIG.card_marks.some((a) => a.includes(id))), "every card of the map is used by at least one state");
console.log(`data.mjs olm62: ${n62} events recounted (counts / medians / splits exact · rank correlation within 0.02 by average ranks) · tree ${TS.clusters.length} clusters ${TS.nodes.length} nodes · ${Object.keys(pack.tree.cards).length} cards · marks for ${NST} states`);

// ---- 8. v3: the second route (JS) for what was added in v3. Everything is read again from the frozen files with this file's own code: (a) the angle column · (b) the F5 edit and cue · (c) the base column of the model chapter ·
//      (d) the row-by-row slopes of olm59 (from the windows side file) · (e) where every blocked row starts (olm128's instrument; the cells and the post-hoc "100 characters" description) ·
//      (f) the cards of the after part: every value that the pack carries from a read.json is read again here, and the freeze commit of every card is looked up in git (the commit that first added the PREREG).
const SQ = (x) => x * x;
const angle = (a, x, b) => { const v1 = [a[0] - x[0], a[1] - x[1]], v2 = [b[0] - x[0], b[1] - x[1]]; return (Math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (Math.hypot(...v1) * Math.hypot(...v2))) * 180) / Math.PI; };
expect(X.every((x, i) => Math.abs(angle(P.O1, x, P.O2) - pack.geometry.ang_O[i]) < 1e-9 && Math.abs(angle(P.O1, x, P.O2) - 90) < 0.001 && Math.abs(angle(P.He, x, P.Hi) - pack.geometry.ang_H[i]) < 1e-9 && Math.abs(angle(P.He, x, P.Hi) - 90) > 1), "v3 (a): the angle O1 Xk O2 is 90 degrees (to the prompt's rounding); the angle He Xk Hi is not");
const f5a = J("probes/olmo3-f5-think-prefix/results/f5_runs_F5a-2.json"), f5b = J("probes/olmo3-f5-think-prefix/results/f5_runs_F5b-1.json");
expect(f5a.edits_applied.length === 1 && f5a.edits_applied[0].key === pack.f5.edit.key && f5a.edits_applied[0].replacement === pack.f5.edit.replacement && f5a.cue === "\n\n" && f5b.cue === "\n\n" && f5a.condition === "blocked" && f5b.condition === "blocked" && pack.f5.cue["F5a-2"].cue === "\n\n", "v3 (b): the F5 edit (one key -> one replacement) and the cue \\n\\n of both F5 runs");
const base = (cond) => pc1.filter((r) => r.condition === cond), cntLab = (rs) => rs.reduce((m, r) => ((m[r.label] = (m[r.label] || 0) + 1), m), {});
expect(eq(cntLab(base("open")), pack.think.base.open.labels) && eq(cntLab(base("blocked")), pack.think.base.blocked.labels) && count(base("open"), (r) => r.hit_cap) === pack.think.base.open.cap && eq(cntLab(base("open").filter((r) => !r.hit_cap)), pack.think.base.open.labels_no_cap), "v3 (c): the base model's frozen labels (open 5 / 5 with one cap row · blocked 7 / 3)");
// (d) slopes: from the windows side file (the 64-token windows of the four groups per event)
{
  const W = JSON.parse(readFileSync(join(HERE, "generated", "olm59_windows.json"), "utf8")); let nrow = 0;
  for (const ev of ["o_diam", "h_diam"]) {
    const E = W.events[ev], S_ = pack.olm59.slopes[ev];
    expect(E.length === S_.length, `v3 (d): slopes ${ev}: n`);
    E.forEach((e, i) => { const d = e.win.map((w) => meanOf(w.slice(32)) - meanOf(w.slice(0, 32))), q = S_[i]; expect(q.id === e.id && q.kind === e.kind && q.lj === e.label_json && d.every((x, g) => Math.abs(x - q.d[g]) < 1.1e-5), `v3 (d): slope ${ev} ${e.id}`); nrow++; });
    const kinds = tallyOf(E.map((e) => `${e.kind}|${e.label_json}`)); expect(eq(Object.entries(kinds).sort(), Object.entries(pack.olm59.agg[ev].by_kind).sort()), `v3 (d): the path x label breakdown of ${ev}`);
    GR.forEach((g, gi) => { const ds = S_.map((q) => q.d[gi]); const R = R59.Q3_desc[`${ev}|${g}|all`]; expect(ds.filter((x) => x > 0).length === R.after_gt_before && Math.abs(medOf(ds) - R.median_diff) < 2e-5, `v3 (d): slopes ${ev} ${g}: the count and the median of read.json`); });
  }
  console.log(`data.mjs v3: angle column · F5 edit / cue · base column · ${nrow} row slopes (counts and medians against read.json)`);
}
function tallyOf(xs) { return xs.reduce((m, x) => ((m[x] = (m[x] || 0) + 1), m), {}); }
// (e) where every blocked row starts (a JS port of olm128's instrument; the card's read.json is the check)
{
  const R128 = J("ConstructGap/exp/olm128/read.json"), SPc = J("probes/olmo3-pc1-cue-invariance/results/pc1_runs.json").rows;
  const rowsOf = { nl: scr.filter((r) => r.condition === "blocked" && !r.hit_cap), sp: SPc.filter((r) => r.cue_tag === "space" && r.condition === "blocked" && !r.hit_cap), nn: SPc.filter((r) => r.cue_tag === "nlnl" && r.condition === "blocked" && !r.hit_cap) };
  const rj = { nl: "nl", sp: "space", nn: "nlnl" };
  for (const k of ["nl", "sp", "nn"]) {
    const xs = [...rowsOf[k]].sort((a, b) => a.seed - b.seed).map((r) => ({ seed: r.seed, json: r.content.indexOf('{"conjecture"') === 0, first: r.content.indexOf('{"conjecture"'), bind: r.label === "B-bind" })), c = R128.blocked_cells[rj[k]], pc = pack.cue_start.cells[k];
    expect(pc.length === xs.length && pc.every((q, i) => q.seed === xs[i].seed && q.first === xs[i].first && (q.start === "json") === xs[i].json && (q.label === "B-bind") === xs[i].bind), `v3 (e): the carried cells of cue ${k} are the recount's`);
    expect(xs.length === c.n && count(xs, (x) => x.json) === c.json && count(xs, (x) => !x.json) === c.text && count(xs, (x) => x.bind) === c.bind && count(xs, (x) => x.json && x.bind) === c.json_bind && count(xs, (x) => !x.json && x.bind) === c.text_bind, `v3 (e): olm128 cells of cue ${k}`);
    const early = xs.filter((x) => x.first >= 0 && x.first <= 100), e2 = pack.cue_start.early[k];
    expect(e2.early === early.length && e2.early_bind === count(early, (x) => x.bind) && e2.n === xs.length && e2.late === xs.length - early.length, `v3 (e): the post-hoc 100-character description, cue ${k}`);
  }
  expect(R128.verdicts.Q1 === "保たれない" && Math.abs(R128.verdicts.Q1_concordance - (count(rowsOf.nl.concat(rowsOf.sp), (r) => (r.content.indexOf('{"conjecture"') === 0) !== (r.label === "B-bind")) / 19)) < 5e-5, "v3 (e): olm128 Q1 concordance recounted (JSON-start rows that are not bind + text-start rows that are bind, over 19)");
}
// (f) the after part: every value of the pack read again from the cards' own read.json (never from a RESULT's summary line); the freeze commit is looked up in git
{
  const A = pack.after, rd = (c) => J(`ConstructGap/exp/${c}/read.json`), q = (o, ...ks) => ks.reduce((a, k) => a[k], o);
  const o76 = rd("olm76");
  expect(A.l3.q1.pos === o76.Q1_bind_close_rises.pos && A.l3.q1.n === 48 && A.l3.q1.sign_p === o76.Q1_bind_close_rises.sign_p && A.l3.q3.median_b === o76.Q3_close_bind_gt_attractor.median_b && A.l3.q3.perm_p === o76.Q3_close_bind_gt_attractor.perm_p && A.l3.pseudo.pos === J("ConstructGap/exp/olm76/control.json").C2_pseudo_window.sae_close.pos, "v3 (f): olm76");
  const look = [["olm84", "Q1"], ["olm85", "Q1_next_sentence_O"], ["olm86", "Q1_k32"]];
  look.forEach(([c, key], i) => { const o = q(rd(c), key), x = A.space.look[i]; expect(x.card === c && ["L32", "L48", "J", "W"].every((m) => x.auc[m].med === o.auc[m].median) && ["L32", "L48"].every((m) => x.E[m].med === o.E[m].median), `v3 (f): ${c} AUC and E`); });
  const o86 = rd("olm86"), o89 = rd("olm89"), o92 = rd("olm92");
  expect(A.space.ktab.olm86["8"].L32 === o86.Q2_desc_by_k["8"].E.L32.median && A.space.ktab.olm86["32"].L48 === o86.Q1_k32.E.L48.median && A.space.ktab.olm89["8"].L32 === o89.Q1_k8.E.L32.median && A.space.ktab.olm89["32"].L48 === o89.Q2_desc_by_k["32"].E.L48.median && A.space.ktab.olm92["8"].L32 === o92.Q_k8.E_old.L32.median && A.space.ktab.olm92["16"].L32 === o92.Q3_desc_by_k["16"].E_old.L32.median && A.space.plus.L32.med === o92.Q_k8.E_plus.L32.median, "v3 (f): the E by k tables (olm86 / 89 / 92)");
  const o91 = rd("olm91"); expect(A.space.first64.auc.L32.med === o91.Q1_first64.auc.L32.median && A.space.first64.rows === 217 && A.space.first64.attractor === 51, "v3 (f): olm91");
  const o94 = rd("olm94"), o98 = rd("olm98"), o101 = rd("olm101"), o106 = rd("olm106"), o108 = rd("olm108");
  expect(A.struct.ref.olm94_q2.to_dem.L32 === o94.Q2_V_post_to_dem_vs_ctl.to_dem.L32.median && A.struct.ref.olm94_q2.to_ctl.L32 === o94.Q2_V_post_to_dem_vs_ctl.to_ctl.L32.median && A.struct.heads.ratio === o98.Q1_top_heads_read_ref_name.ratio_median && A.struct.heads.e_top === o98.Q2_patch_top_heads.e_top_median && A.struct.heads.flip === o98.Q2_patch_top_heads.flip_top && eq(A.struct.heads.overlap, o98.Q4_cmt13_overlap), "v3 (f): olm94 / olm98");
  expect(A.struct.layers.end.every((r, i) => r.L === o101.Q1_curve_full_end[i].L && r.po === o101.Q1_curve_full_end[i].F_po && r.vo === o101.Q1_curve_full_end[i].F_vo) && A.struct.layers.sel.every((r) => r.po === o106.table[`sel_L${r.L}`]["test・ptr_only"] && r.vo === o106.table[`sel_L${r.L}`]["test・val_only"]) && A.struct.layers.tail.every((r, i) => r.L === o108.Q1.curve_tail[i][0] && r.po === o108.Q1.curve_tail[i][1] && r.vo === o108.Q1.curve_tail[i][2]), "v3 (f): the layer curves of olm101 / 106 / 108");
  const o112 = rd("olm112"), o114 = rd("olm114"), o128 = rd("olm128");
  expect(A.apex.olm112.Q1.chain === o112.Q1.chain && A.apex.olm112.Q1.bind === o112.Q1.bind && A.apex.olm112.bind.THC === o112.Q4_by_label_json["B-bind"].THC && A.apex.olm114.Q1.RA_and_THC === o114.Q1.RA_and_THC && A.apex.olm114.Q2.THC === o114.Q2.THC && A.apex.olm114.Q3.bind === o114.Q3.bind && A.apex.olm114.fam.k2.fable.THC === o114.Q2.by_family.fable.THC, "v3 (f): olm112 / olm114");
  expect(A.next.verdicts.Q1_concordance === o128.verdicts.Q1_concordance && eq(A.next.cells, o128.blocked_cells), "v3 (f): olm128");
  // the freeze commit of every card: git's first commit of its PREREG
  let nfz = 0;
  for (const c of A.cards) { const out = gitFact(["log", "--diff-filter=A", "--format=%h", "--", c.prereg]).trim().split("\n").filter(Boolean); expect(out.length > 0 && c.freeze.startsWith(out[out.length - 1].slice(0, 7)), `v3 (f): the freeze commit of ${c.id}: ${c.freeze} vs git ${out[out.length - 1]}`); nfz++; if (c.read) expect(rd(c.id), "readable"); }
  expect(A.cards.length === 18 && A.stations.length === 6 && A.stations.flatMap((s_) => s_.cards).length === 18, "v3 (f): 18 cards on 6 stations");
  console.log(`data.mjs v3 after: ${A.cards.length} cards on ${A.stations.length} stations · ${nfz} freeze commits against git · values of ${["olm76", "olm84", "olm85", "olm86", "olm89", "olm91", "olm92", "olm94", "olm98", "olm101", "olm106", "olm108", "olm112", "olm114", "olm128"].length} read.json read again`);
}

export const DATA = { config: CONFIG, ...pack };
