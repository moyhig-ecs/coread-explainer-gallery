// build.mjs — the skeleton of the build (template): from the card's data and the Anatomy kit, make the pages (dark / light x ja / en) and the anywidget front-end (ESM + CSS). Never edit the generated files by hand.
//   bun build.mjs [--out dist]          (bun >= 1.3 or Node >= 20.10; the py env's node may be too old for the Anatomy kit)
//   1. runs pack_data.py (the first route of every number)   2. imports data.mjs (the second route; a disagreement stops the build)
//   3. writes <out>/<pages>.html, <out>/widget.js, <out>/widget.css, <out>/build_report.json (with the md5 of the kit's iso-kit.mjs and the CHANGELOG's first dated heading)
//   ANATOMY=/path/to/anatomy bun build.mjs    (default: ~/.claude/skills/anatomy). The kit is needed only here; dist/ is self-contained.
// Anatomy (MIT, Copyright (c) 2026 Ryan) is read from $ANATOMY or ~/.claude/skills/anatomy: only its CSS (ISO_CSS), its page shell (pageHtml) and its camera formula (copied into figure.js) are used.
// This template does NOT copy the kit: it refers to the `anatomy` skill. The MIT notice is written into every page and kept in README.md.
import { readFileSync, writeFileSync, mkdirSync, existsSync, statSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const arg = (name, dflt) => { const i = process.argv.indexOf(name); return i >= 0 ? process.argv[i + 1] : dflt; };
const OUT = join(HERE, arg("--out", "dist")); mkdirSync(OUT, { recursive: true });
const ANATOMY = [process.env.ANATOMY, join(process.env.HOME || "", ".claude/skills/anatomy")].filter(Boolean).find((p) => existsSync(join(p, "kit/iso-kit.mjs")));
if (!ANATOMY) throw new Error("the `anatomy` skill (its kit/iso-kit.mjs) was not found: install the skill or set ANATOMY=/path/to/anatomy");
const PY = process.env.PY || "python3";
const K = await import(pathToFileURL(join(ANATOMY, "kit/iso-kit.mjs")).href);

execFileSync(PY, ["-I", join(HERE, "pack_data.py")], { stdio: "inherit" });          // 1. the pack (assert)
const { DATA, CONFIG } = await import("./data.mjs");                                   // 2. the recount in JS
const read = (f) => readFileSync(join(HERE, f), "utf8");
const md5 = (t) => createHash("md5").update(t).digest("hex");
const figureCss = read("figure.css"), i18nSrc = read("i18n.js"), figureSrc = read("figure.js"), engineSrc = read("state_machine.js"), glueSrc = read("widget_glue.js");

// ---- the markup (the same for the page and the widget). The chapters come from config.json: one place for the state numbers.
const CHAPTERS = CONFIG.chapters, NSTATES = CHAPTERS[CHAPTERS.length - 1][2] + 1;
if (CHAPTERS.some(([, a, b], i) => b < a || (i === 0 ? a !== 0 : a !== CHAPTERS[i - 1][2] + 1))) throw new Error("config.json chapters must tile the states 0.." + (NSTATES - 1));
const stepBtn = (i) => `<button class="sh-btn sh-step" data-n="${i}" aria-current="false">${i}</button>`;
const steps = CHAPTERS.map(([c, a, b]) => `<span class="sh-stepgrp" data-chap="${c}" role="group">${Array.from({ length: b - a + 1 }, (_, k) => stepBtn(a + k)).join("")}</span>`).join("");
const chapButtons = CHAPTERS.map(([c, a]) => `<button class="sh-btn sh-chap" type="button" data-chap="${c}" data-go="${a}" aria-pressed="false"></button>`).join("");
const inner = () => `
<div class="sh-nav"><div class="sh-chaps" role="group">${chapButtons}</div>
<div class="sh-bar"><div class="sh-steps" role="group">${steps}</div><button class="sh-btn sh-prev" type="button">←</button><button class="sh-btn sh-next" type="button">→</button><span class="sh-sep"></span><button class="sh-btn sh-lang" type="button"></button><button class="sh-btn sh-theme" type="button" aria-label="theme">◐</button><label class="fig-tval-wrap"><input class="fig-range" type="range" min="0" max="1" step="1" value="0"><span class="fig-tval"></span></label></div></div>
<header class="sh-head"><span class="sh-kicker"></span><h2 class="sh-q"></h2><p class="sh-lead"></p></header>
<figure class="iso-figure"><div class="iso-plate"><div class="iso-plate-corners" aria-hidden="true"><span class="iso-plate-corner" data-corner="fig"></span><span class="iso-plate-corner" data-corner="title"><span class="t1"></span><span class="sh-corner2"></span></span><span class="iso-plate-corner" data-corner="hint"></span><span class="iso-plate-corner" data-corner="readout" data-readout></span></div>
<svg class="iso-svg fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 700" role="img" aria-label="${CONFIG.title}"><g data-g="picture"></g></svg><div class="fig-ledger"></div>
<div class="sh-keys"></div></div><figcaption class="sh-caption"></figcaption></figure>
<div class="sh-panel"></div>
<div class="sh-strip"><div class="sh-lim"></div><div class="sh-notclaimed"></div></div>
<div class="sh-foot"></div>`;
const rootHtml = (theme) => `<div class="sh iso" data-theme="${theme}" data-state="0" data-chapter="${CHAPTERS[0][0]}" data-lang="ja" tabindex="0" role="group" aria-label="${CONFIG.name}">${inner()}</div>`;

// ---- what the page carries: DATA (from the pack) + the words + the figure + the engine
const core = () => `const DATA = ${JSON.stringify(DATA)};\n${i18nSrc}\n${figureSrc}\n${engineSrc}\n`;
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
`;
const pageOf = (theme, lang) => {
  const html = K.pageHtml({ title: CONFIG.title, theme, body: rootHtml(theme), script: core() + pageGlue(lang), width: 1180 });
  return `<!-- The Anatomy kit's sheet, page shell and camera formula (MIT, Copyright (c) 2026 Ryan) are used in this page. -->\n` + html.replace("</style>", `${figureCss}\n.iso-page{margin-top:16px}</style>`).replace('<html lang="en">', `<html lang="${lang}">`);
};
for (const [file, [theme, lang]] of Object.entries(CONFIG.pages)) writeFileSync(join(OUT, file), pageOf(theme, lang));

// ---- the anywidget front-end: ESM (data + figure + engine + SKELETON + glue) and CSS (the kit's sheet + figure.css; class-scoped)
writeFileSync(join(OUT, "widget.js"), `// widget.js — GENERATED by build.mjs. Do not edit.\n// Anatomy: MIT, Copyright (c) 2026 Ryan.\n${core()}\nconst SKELETON = ${JSON.stringify(inner())};\n${glueSrc}\n`);
writeFileSync(join(OUT, "widget.css"), `/* widget.css — GENERATED by build.mjs: the Anatomy kit's sheet (MIT, Copyright (c) 2026 Ryan) + figure.css. */\n${K.ISO_CSS}\n${figureCss}`);

// ---- the report (what went in; the md5 of the card's file; the numbers the build counted)
const size = (f) => statSync(join(OUT, f)).size;
// the pin of the kit (reproducibility): the md5 of kit/iso-kit.mjs and the first dated heading of the anatomy CHANGELOG.md. No absolute path is written.
const changelog = existsSync(join(ANATOMY, "CHANGELOG.md")) ? readFileSync(join(ANATOMY, "CHANGELOG.md"), "utf8").split("\n").filter((l) => l.startsWith("## ")) : [];
const dated = changelog.find((l) => /\d{4}-\d{2}-\d{2}/.test(l));
const kitPin = { iso_kit_md5: md5(readFileSync(join(ANATOMY, "kit/iso-kit.mjs"))), changelog_top: changelog[0] || null, changelog_first_dated: dated || null, changelog_date: dated ? dated.match(/\d{4}-\d{2}-\d{2}/)[0] : null };
const anatomyFrom = process.env.ANATOMY && ANATOMY === process.env.ANATOMY ? "$ANATOMY" : "~/.claude/skills/anatomy";
writeFileSync(join(OUT, "build_report.json"), JSON.stringify({ built_with: { anatomy: anatomyFrom, anatomy_kit: kitPin, runtime: typeof Bun !== "undefined" ? `bun ${Bun.version}` : `node ${process.version}` }, card: { md5: DATA.md5, provenance: DATA.provenance, controls: DATA.controls }, key_ranks: Object.fromEntries(Object.entries(DATA.rows).map(([k, r]) => [k, r.keyRank])), states: NSTATES, files: Object.fromEntries([...Object.keys(CONFIG.pages), "widget.js", "widget.css"].map((f) => [f, size(f)])), source_md5: { "figure.js": md5(figureSrc), "i18n.js": md5(i18nSrc), "state_machine.js": md5(engineSrc) } }, null, 1) + "\n");
console.log(`built: ${Object.keys(CONFIG.pages).length} pages · widget js ${(size("widget.js") / 1024).toFixed(0)} KB · css ${(size("widget.css") / 1024).toFixed(0)} KB · ${NSTATES} states → ${OUT}`);
