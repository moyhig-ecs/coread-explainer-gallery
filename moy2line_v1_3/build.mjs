// build.mjs — builds the four pages (dark / light × ja / en) and the anywidget front-end (ESM + CSS) of the moy-2 reflection-tool line explainer. Never edit the generated files by hand.
//   PY=<python> bun build.mjs [--out dist]
//   1. runs pack_moy2.py (the first route of every number)   2. imports data.mjs (the second route; a disagreement stops the build)
//   3. builds the static isometric art with the Anatomy kit (art.mjs: the board and the rack)   4. writes <out>/<pages>.html, <out>/widget.js, <out>/widget.css, <out>/build_report.json
// Anatomy (MIT, Copyright (c) 2026 Ryan) is read from $ANATOMY or ~/.claude/skills/anatomy: its CSS (ISO_CSS), its page shell (pageHtml), its camera and solids (via art.mjs). The MIT notice is in every page and in README.md / LICENSE-Anatomy.txt.
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

execFileSync(PY, ["-I", join(HERE, "pack_moy2.py")], { stdio: "inherit" });          // 1. the pack (assert)
const { DATA: D0, CONFIG } = await import("./data.mjs");                                // 2. the recount in JS
const { makeArt } = await import("./art.mjs");
const ART = makeArt(K, D0);                                                              // 3. the kit's art (static)
const DATA = { ...D0, art: ART };
const read = (f) => readFileSync(join(HERE, f), "utf8");
const md5 = (t) => createHash("md5").update(t).digest("hex");
const figureCss = read("figure.css"), i18nSrc = read("i18n.js"), figureSrc = read("figure.js"), engineSrc = read("state_machine.js"), glueSrc = read("widget_glue.js");

const CHAPTERS = CONFIG.chapters, NSTATES = CHAPTERS[CHAPTERS.length - 1][2] + 1;
if (CHAPTERS.some(([, a, b], i) => b < a || (i === 0 ? a !== 0 : a !== CHAPTERS[i - 1][2] + 1))) throw new Error("config.json chapters must tile the states 0.." + (NSTATES - 1));
const stepBtn = (i) => `<button class="sh-btn sh-step" data-n="${i}" aria-current="false">${i}</button>`;
const steps = CHAPTERS.map(([c, a, b]) => `<span class="sh-stepgrp" data-chap="${c}" role="group">${Array.from({ length: b - a + 1 }, (_, k) => stepBtn(a + k)).join("")}</span>`).join("");
const chapButtons = CHAPTERS.map(([c, a]) => `<button class="sh-btn sh-chap" type="button" data-chap="${c}" data-go="${a}" aria-pressed="false"></button>`).join("");
const inner = () => `
<div class="sh-nav"><div class="sh-chaps" role="group">${chapButtons}</div>
<div class="sh-bar"><div class="sh-steps" role="group">${steps}</div><button class="sh-btn sh-prev" type="button">←</button><button class="sh-btn sh-next" type="button">→</button><span class="sh-sep"></span><button class="sh-btn sh-lang" type="button"></button><button class="sh-btn sh-theme" type="button" aria-label="theme">◐</button></div></div>
<header class="sh-head"><span class="sh-kicker"></span><h2 class="sh-q"></h2><p class="sh-lead"></p></header>
<figure class="iso-figure"><div class="iso-plate"><div class="iso-plate-corners" aria-hidden="true"><span class="iso-plate-corner" data-corner="fig"></span><span class="iso-plate-corner" data-corner="title"><span class="t1"></span><span class="sh-corner2"></span></span><span class="iso-plate-corner" data-corner="hint"></span><span class="iso-plate-corner" data-corner="readout" data-readout></span></div>
<div class="fig-body"><div class="fig-pic"><div class="fig-ctitle"></div><svg class="iso-svg fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 700" role="img" aria-label="${CONFIG.title}"><defs><pattern id="fx-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path class="fx-hatch-ln" d="M1 0V6"/></pattern><pattern id="fx-xhatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path class="fx-hatch-ln" d="M1 0V6M0 1H6"/></pattern></defs><g data-g="art"></g><g data-g="picture"></g></svg></div><div class="fig-side"></div></div>
<div class="fig-html"></div><div class="fig-ledger"></div>
<div class="sh-keys"></div></div><figcaption class="sh-caption"></figcaption></figure>
<div class="sh-panel"></div>
<div class="sh-strip"><div class="sh-lim"></div><div class="sh-notclaimed"></div></div>
<div class="sh-foot"></div>`;
const rootHtml = (theme, lang) => `<div class="sh iso" data-theme="${theme}" data-state="0" data-chapter="${CHAPTERS[0][0]}" data-lang="${lang}" tabindex="0" role="group" aria-label="${CONFIG.name}">${inner()}</div>`;

const core = () => `const DATA = ${JSON.stringify(DATA)};\n${i18nSrc}\n${figureSrc}\n${engineSrc}\n`;
const stateRe = `^#s?(${Array.from({ length: NSTATES }, (_, i) => i).reverse().join("|")})$`;
const pageGlue = (lang) => `
const root = document.querySelector(".sh"), q = new URLSearchParams(location.search);
const stateOfHash = () => { const m = new RegExp(${JSON.stringify(stateRe)}).exec(location.hash); return m ? Number(m[1]) : 0; };
const themeOf = () => (q.get("theme") === "light" || q.get("theme") === "dark" ? q.get("theme") : document.body.dataset.theme);
document.body.dataset.theme = themeOf();
if (q.get("video") === "1") root.dataset.video = "1";
const api = mountFigure(root, { lang: () => ((q.get("lang") || "${lang}") === "en" ? "en" : "ja"), state: stateOfHash, theme: themeOf, row: () => q.get("row") || "", arm: () => q.get("arm") || "", onState: (n) => history.replaceState(null, "", location.pathname + location.search + "#s" + n), onTheme: (t) => { document.body.dataset.theme = t; } });
addEventListener("hashchange", () => api.goto(stateOfHash()));
window.__sh = api; window.__fig = FIGURE; window.__data = DATA;
`;
const pageOf = (theme, lang) => {
  const html = K.pageHtml({ title: lang === "en" ? "moy-2 reflection-tool line · co-reading" : "moy-2 折り返しの道具の系列 · 共読", theme, body: rootHtml(theme, lang), script: core() + pageGlue(lang), width: 1180 });
  return `<!-- The Anatomy kit's sheet, page shell, camera and solids (MIT, Copyright (c) 2026 Ryan) are used in this page. -->\n` + html.replace("</style>", `${figureCss}\n.iso-page{margin-top:16px}</style>`).replace('<html lang="en">', `<html lang="${lang}">`);
};
for (const [file, [theme, lang]] of Object.entries(CONFIG.pages)) writeFileSync(join(OUT, file), pageOf(theme, lang));
writeFileSync(join(OUT, "widget.js"), `// widget.js — GENERATED by build.mjs. Do not edit.\n// Anatomy: MIT, Copyright (c) 2026 Ryan.\n${core()}\nconst SKELETON = ${JSON.stringify(inner())};\n${glueSrc}\n`);
writeFileSync(join(OUT, "widget.css"), `/* widget.css — GENERATED by build.mjs: the Anatomy kit's sheet (MIT, Copyright (c) 2026 Ryan) + figure.css. */\n${K.ISO_CSS}\n${figureCss}`);
const size = (f) => statSync(join(OUT, f)).size;
writeFileSync(join(OUT, "build_report.json"), JSON.stringify({ built_with: { anatomy: ANATOMY.replace(process.env.HOME || "", "~"), runtime: typeof Bun !== "undefined" ? `bun ${Bun.version}` : `node ${process.version}` },
  inventory: DATA.inventory, read_prov: DATA.read_prov, states: NSTATES, ln_v3: Object.fromEntries(DATA.arms.map((a) => [a.id, `${a.agg.LN3} / ${a.agg.n_proof}`])), verdicts: Object.fromEntries(Object.entries(DATA.verdicts).map(([a, v]) => [a, v.read ?? `(no verdict; ref band ${v.calc})`])),
  art: { board_bytes: ART.board.svg.length, rack_bytes: ART.rack.svg.length, rack_blocks: ART.rack.hits.length }, files: Object.fromEntries([...Object.keys(CONFIG.pages), "widget.js", "widget.css"].map((f) => [f, size(f)])),
  source_md5: { "figure.js": md5(figureSrc), "i18n.js": md5(i18nSrc), "state_machine.js": md5(engineSrc), "art.mjs": md5(read("art.mjs")), "pack_moy2.py": md5(read("pack_moy2.py")) } }, null, 1) + "\n");
console.log(`built: ${Object.keys(CONFIG.pages).length} pages · widget js ${(size("widget.js") / 1024).toFixed(0)} KB · css ${(size("widget.css") / 1024).toFixed(0)} KB · ${NSTATES} states → ${OUT}`);
