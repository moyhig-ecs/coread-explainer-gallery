// build.mjs — the build of the moy-1 figure (from the coread-explainer template): from the card's data and the Anatomy kit, make the pages (dark / light x ja / en) and the anywidget front-end (ESM + CSS). Never edit the generated files by hand.
//   bun build.mjs [--out pages]          (bun >= 1.3 or Node >= 20.10; the py env's node may be too old for the Anatomy kit)
//   1. runs pack_moy1.py (the first route of every number)   2. imports data.mjs (the second route; a disagreement stops the build)
//   3. writes <out>/<pages>.html, <out>/widget.js, <out>/widget.css, <out>/build_report.json
// Anatomy (MIT, Copyright (c) 2026 Ryan) is read from $ANATOMY or ~/.claude/skills/anatomy: only its CSS (ISO_CSS), its page shell (pageHtml) and its camera formula (copied into figure.js) are used.
// This template does NOT copy the kit: it refers to the `anatomy` skill. The MIT notice is written into every page and kept in README.md.
import { readFileSync, writeFileSync, mkdirSync, existsSync, statSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const arg = (name, dflt) => { const i = process.argv.indexOf(name); return i >= 0 ? process.argv[i + 1] : dflt; };
const OUT = join(HERE, arg("--out", "pages")); mkdirSync(OUT, { recursive: true });
const ANATOMY = [process.env.ANATOMY, join(process.env.HOME || "", ".claude/skills/anatomy")].filter(Boolean).find((p) => existsSync(join(p, "kit/iso-kit.mjs")));
if (!ANATOMY) throw new Error("the `anatomy` skill (its kit/iso-kit.mjs) was not found: install the skill or set ANATOMY=/path/to/anatomy");
const PY = process.env.PY || "python3";
const K = await import(pathToFileURL(join(ANATOMY, "kit/iso-kit.mjs")).href);

execFileSync(PY, ["-I", join(HERE, "pack_moy1.py")], { stdio: "inherit" });          // 1. the pack (assert)
const { DATA, CONFIG } = await import("./data.mjs");                                   // 2. the recount in JS
const read = (f) => readFileSync(join(HERE, f), "utf8");

const md5 = (t) => createHash("md5").update(t).digest("hex");
const figureCss = read("figure.css"), i18nSrc = read("i18n.js") + "\n" + read("i18n_after.js"), scenesSrc = read("scenes.js") + "\n" + read("scenes_after.js"), figureSrc = read("figure.js"), engineSrc = read("state_machine.js"), glueSrc = read("widget_glue.js");      // v3: i18n_after.js / scenes_after.js = the part added after the 10-28 figure (loaded right after i18n.js / scenes.js)

// ---- the ledger rows (ja / en), evaluated from the very sources the page carries: CLAIMS.md is generated from them (make_claims.py), so the claim text is never copied by hand
{
  const mod = new Function("DATA", "matchMedia", `${i18nSrc}\n${scenesSrc}\n${figureSrc}\nreturn { I18N, FIGURE };`)(DATA, () => ({ matches: false }));
  const led = {};
  const LS = CONFIG.chapters.find(([c]) => c === "ledger")[1], LAST = CONFIG.chapters[CONFIG.chapters.length - 1][2], STALE_LAST = 29;   // v3: 29 was the last state of the 10-28 figure (v2.1); it is now the first state of the structure chapter, so no css rule may still name it as the ledger
  if (!new RegExp(`data-state="${LAST}"`).test(figureCss) || figureCss.includes(`data-state="${STALE_LAST}"`)) throw new Error(`figure.css must name the last state (${LAST}) of the ledger`);
  for (const lang of ["ja", "en"]) { const Q = mod.FIGURE.ctx({ state: LS, t: 0, lang }); led[lang] = { rows: mod.I18N[lang].ledger.rows(Q), questions: mod.I18N[lang].ledger.questions(Q) }; }
  writeFileSync(join(HERE, "generated", "ledger_rows.json"), JSON.stringify(led, null, 1));
  // the headings as the page really has them (v2.1: the new states are spliced into i18n.js at load time, so a regex over the source no longer sees the order): list_headings.py and make_readme.py read this
  writeFileSync(join(HERE, "generated", "states_table.json"), JSON.stringify(mod.FIGURE.states.map((st, n) => ({ n, chapter: st.chapter, mode: st.mode, ja: mod.I18N.ja.states[n].kicker, en: mod.I18N.en.states[n].kicker })), null, 1));
}

// ---- v3.1 (BRIEF v3.1 §2-5): the card marks are DERIVED here from what each state reads (the rule of entry P's v3, adapted to this build's DATA keys):
//      DATA is wrapped in a tracking proxy, every state's words (lead · readout · lim · chips · quote) and picture (wide and phone canvas) are evaluated in ja / en,
//      the dotted DATA paths a state touches are mapped to cards by ONE rule (CARD_RULE) and the result must equal config.json card_marks (a difference stops the build).
//      Rule = "the card whose frozen output file a state's numbers / verbatim text are read from + the card that froze the instrument those numbers are made with (the SAE groups)".
//      The cards struck after the 10-28 figure (DATA.after · DATA.cue_start = olm128) never become a mark on a 10-28 state: the part added later shows them in its own card table (Q's rule).
//      The page itself carries no proxy.
{
  const seen = new Set(); let on = false; const cache = new WeakMap();
  const prox = (o, p) => { if (!o || typeof o !== "object") return o; let m = cache.get(o); if (!m) { m = new Map(); cache.set(o, m); } if (m.has(p)) return m.get(p); const px = new Proxy(o, { get(t, k, r) { const v = Reflect.get(t, k, r); if (typeof k !== "string") return v; const q = p ? `${p}.${k}` : k; if (on && !/^\d+$/.test(k)) seen.add(q.replace(/\.\d+(?=\.|$)/g, "")); return v && typeof v === "object" ? prox(v, q) : v; } }); m.set(p, px); return px; };
  const M = new Function("DATA", "matchMedia", `${i18nSrc}\n${scenesSrc}\n${figureSrc}\nreturn { I18N, FIGURE, SCENES };`)(prox(DATA, ""), () => ({ matches: false }));
  const GROUPS = ["olm59", "olm7", "olm4"];
  const CARD_RULE = (path) => {
    const [k0, k1] = path.split(".");
    if (["geometry", "prompts", "seg"].includes(k0)) return ["replication_config_frozen"];
    if (["rows", "open_cnt", "blk_cnt", "o_sent", "he_sent", "hehi_word_rows", "he_end", "order_he_first", "open_tok_rows", "changed_open", "attr_open", "json_first", "otok_ctx", "logmax", "flags"].includes(k0)) return ["pc1"];
    if (k0 === "scene") return k1 && k1.startsWith("f5") ? ["F5"] : k1 ? ["pc1"] : [];
    if (k0 === "excerpts") return ["pc1"];
    if (k0 === "cue_table") return k1 === "nl" ? ["screen_bf16"] : k1 ? ["pc1"] : [];
    if (k0 === "cmt13") return ["cmt13"];
    if (k0 === "f5") return ["F5"];
    if (k0 === "cmt5" || k0 === "cmt5_ctl") return ["cmt5"];
    if (k0 === "models") return ["moy_suite_report"];
    if (k0 === "think") return k1 === "base" ? ["pc1"] : ["behavior_screen"];
    if (k0 === "olm59") return k1 === "cmt5_two" ? ["cmt5"] : k1 === "labels" ? ["olm59", "cmt5"] : GROUPS;
    if (k0 === "olm62") return ["olm62", ...GROUPS];
    return [];                                                     // tree · config · title · sources (the map itself) · after · cue_start (the cards after 10-28: shown in the added part's card table, never as a mark)
  };
  const order = Object.keys(DATA.tree.cards), derived = [];
  M.FIGURE.states.forEach((st, n) => {
    const got = new Set();
    for (const lang of ["ja", "en"]) for (const narrow of [false, true]) {
      const t0 = typeof st.t === "function" ? st.t() : st.t, S = { state: n, t: t0, lang, card: null };
      on = false; seen.clear(); const Q = M.FIGURE.ctx(S); on = true;
      const T = M.I18N[lang].states[n];
      for (const f of ["lead", "readout", "lim"]) if (typeof T[f] === "function") T[f](Q);
      if (typeof T.chips === "function") T.chips(Q); if (typeof T.quote === "function") T.quote(Q);
      if (st.mode !== "ledger") { const cam = narrow ? st.camN || st.cam : st.cam, A = (k) => ({ az: cam[0], el: cam[1], zoom: cam[2], px: cam[3] })[k] ?? 1, cv = narrow ? { W: 780, H: st.Hn || 700, narrow: true, video: false, fs: 23.5, u: 23.5 / 12 } : { W: 1000, H: st.Hw || 600, narrow: false, video: false, fs: 12, u: 1 }; M.SCENES[st.mode](S, A, cv, st); }
      on = false;
      if (st.mode !== "ledger") { const all = [...seen]; for (const p of all) if (!all.some((q) => q.startsWith(p + "."))) for (const c of CARD_RULE(p)) got.add(c); }
    }
    derived.push(order.filter((c) => got.has(c)));
  });
  const cfg = CONFIG.card_marks.map((a) => order.filter((c) => a.includes(c)));
  const diff = derived.map((a, n) => (a.join() === cfg[n].join() ? null : `state ${n}: derived [${a}] · config [${cfg[n]}]`)).filter(Boolean);
  writeFileSync(join(HERE, "generated", "marks_derived.json"), JSON.stringify({ rule: CONFIG.card_mark_rule, derived, config: cfg, differences: diff }, null, 1));
  if (diff.length && !process.env.MARKS_REPORT_ONLY) throw new Error("config.json card_marks differ from the marks derived from what each state reads:\n  " + diff.join("\n  "));
  if (diff.length) console.log("marks differ:\n  " + diff.join("\n  "));
}

// ---- the markup (the same for the page and the widget). The chapters come from config.json: one place for the state numbers.
const CHAPTERS = CONFIG.chapters, NSTATES = CHAPTERS[CHAPTERS.length - 1][2] + 1;
if (CHAPTERS.some(([, a, b], i) => b < a || (i === 0 ? a !== 0 : a !== CHAPTERS[i - 1][2] + 1))) throw new Error("config.json chapters must tile the states 0.." + (NSTATES - 1));
const AFTER = (CONFIG.parts && CONFIG.parts.after) || [], isAfter = (n) => AFTER.some(([a, b]) => n >= a && n <= b);           // v3: the states of the part added after the 10-28 figure (config.json parts)
const stepBtn = (i) => `<button class="sh-btn sh-step" data-n="${i}" data-part="${isAfter(i) ? "after" : "base"}" aria-current="false">${i}</button>`;
const steps = CHAPTERS.map(([c, a, b]) => `<span class="sh-stepgrp" data-chap="${c}" data-part="${isAfter(a) ? "after" : "base"}" role="group">${Array.from({ length: b - a + 1 }, (_, k) => stepBtn(a + k)).join("")}</span>`).join("");
const chapButtons = CHAPTERS.map(([c, a]) => `<button class="sh-btn sh-chap" type="button" data-chap="${c}" data-go="${a}" data-part="${isAfter(a) ? "after" : "base"}" aria-pressed="false"></button>`).join("");
const inner = () => `
<div class="sh-nav"><div class="sh-chaps" role="group">${chapButtons}</div>
<div class="sh-bar"><div class="sh-steps" role="group">${steps}</div><button class="sh-btn sh-prev" type="button">←</button><button class="sh-btn sh-next" type="button">→</button><span class="sh-sep"></span><button class="sh-btn sh-lang" type="button"></button><button class="sh-btn sh-theme" type="button" aria-label="theme">◐</button><label class="fig-tval-wrap"><input class="fig-range" type="range" min="0" max="1" step="1" value="0"><span class="fig-tval"></span></label></div></div>
<header class="sh-head"><div class="sh-kickrow"><span class="sh-kicker"></span><span class="sh-cards" role="group"></span></div><h2 class="sh-q"></h2><p class="sh-lead"></p></header>
<figure class="iso-figure"><div class="iso-plate"><div class="iso-plate-corners" aria-hidden="true"><span class="iso-plate-corner" data-corner="fig"></span><span class="iso-plate-corner" data-corner="title"><span class="t1"></span><span class="sh-corner2"></span></span><span class="iso-plate-corner" data-corner="hint"></span><span class="iso-plate-corner" data-corner="readout" data-readout></span></div>
<svg class="iso-svg fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 700" role="img" aria-label="${CONFIG.title}"><g data-g="picture"></g></svg><div class="fig-ledger"></div><div class="fig-quote"></div>
<div class="sh-keys"></div></div><figcaption class="sh-caption"></figcaption></figure>
<div class="sh-panel"></div>
<div class="sh-strip"><div class="sh-lim"></div><div class="sh-notclaimed"></div></div>
<div class="sh-foot"></div>`;
const rootHtml = (theme) => `<div class="sh iso" data-theme="${theme}" data-state="0" data-chapter="${CHAPTERS[0][0]}" data-lang="ja" tabindex="0" role="group" aria-label="${CONFIG.name}">${inner()}</div>`;

// ---- what the page carries: DATA (from the pack) + the words + the figure + the engine
const core = () => `const DATA = ${JSON.stringify(DATA)};\n${i18nSrc}\n${scenesSrc}\n${figureSrc}\n${engineSrc}\n`;
const stateRe = `^#s?(${Array.from({ length: NSTATES }, (_, i) => i).reverse().join("|")})$`;          // the hash regex is made from the number of states (never typed)
const pageGlue = (lang) => `
const root = document.querySelector(".sh"), q = new URLSearchParams(location.search);
const stateOfHash = () => { const m = new RegExp(${JSON.stringify(stateRe)}).exec(location.hash); return m ? Number(m[1]) : 0; };
const themeOf = () => (q.get("theme") === "light" || q.get("theme") === "dark" ? q.get("theme") : document.body.dataset.theme);
document.body.dataset.theme = themeOf();
if (q.get("video") === "1") root.dataset.video = "1";           // the 1920 x 1080 frame: chrome that is not part of a video still is hidden by figure.css
const api = mountFigure(root, { lang: () => ((q.get("lang") || "${lang}") === "en" ? "en" : "ja"), state: stateOfHash, theme: themeOf, onState: (n) => history.replaceState(null, "", "#s" + n), onTheme: (t) => { document.body.dataset.theme = t; } });
addEventListener("hashchange", () => api.goto(stateOfHash()));
window.__sh = api;
window.__DATA = DATA;                          // the checks read the pack's numbers from here (they are the page's own)
`;
const pageOf = (theme, lang) => {
  const html = K.pageHtml({ title: CONFIG.title, theme, body: rootHtml(theme), script: core() + pageGlue(lang), width: 1500 });
  return `<!-- The Anatomy kit's sheet, page shell and camera formula (MIT, Copyright (c) 2026 Ryan) are used in this page. -->\n` + html.replace("</style>", `${figureCss}\n.iso-page{margin-top:16px}</style>`).replace('<html lang="en">', `<html lang="${lang}">`);
};
for (const [file, [theme, lang]] of Object.entries(CONFIG.pages)) writeFileSync(join(OUT, file), pageOf(theme, lang));

// ---- the anywidget front-end: ESM (data + figure + engine + SKELETON + glue) and CSS (the kit's sheet + figure.css; class-scoped)
writeFileSync(join(OUT, "widget.js"), `// widget.js — GENERATED by build.mjs. Do not edit.\n// Anatomy: MIT, Copyright (c) 2026 Ryan.\n${core()}\nconst SKELETON = ${JSON.stringify(inner())};\n${glueSrc}\n`);
writeFileSync(join(OUT, "widget.css"), `/* widget.css — GENERATED by build.mjs: the Anatomy kit's sheet (MIT, Copyright (c) 2026 Ryan) + figure.css. */\n${K.ISO_CSS}\n${figureCss}`);

// ---- the report (what went in; the md5 of the card's file; the numbers the build counted)
const size = (f) => statSync(join(OUT, f)).size;
writeFileSync(join(OUT, "build_report.json"), JSON.stringify({ built_with: { anatomy: ANATOMY.replace(process.env.HOME || "", "~"), runtime: typeof Bun !== "undefined" ? `bun ${Bun.version}` : `node ${process.version}` }, card: { sources: DATA.sources, cmt13_provenance: DATA.cmt13.provenance, cmt13_controls_all_pass: DATA.cmt13.controls.all_pass }, counts: { rows: DATA.rows.length, open_reading: DATA.open_cnt, blocked_reading: DATA.blk_cnt, sites: DATA.cmt13.sites.length }, states: NSTATES, files: Object.fromEntries([...Object.keys(CONFIG.pages), "widget.js", "widget.css"].map((f) => [f, size(f)])), source_md5: { "scenes.js": md5(scenesSrc), "figure.js": md5(figureSrc), "i18n.js": md5(i18nSrc), "state_machine.js": md5(engineSrc) } }, null, 1) + "\n");
console.log(`built: ${Object.keys(CONFIG.pages).length} pages · widget js ${(size("widget.js") / 1024).toFixed(0)} KB · css ${(size("widget.css") / 1024).toFixed(0)} KB · ${NSTATES} states → ${OUT}`);
