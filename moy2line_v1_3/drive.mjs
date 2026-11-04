// drive.mjs — a small headless-Chrome driver over the DevTools protocol (copied as a tool from the DevTools driver of the 10-31 explainer in <an earlier entry>/; the figure does not use it).
// Changes for this entry: the DevTools port is fixed inside this maker's band (27500–27599: --port or $DRIVE_PORT, default 27511), the Chrome profile lives inside the entry's scratch (.chrome/), and a ["drag", sel, fx0, fy0, fx1, fy1, steps] action (real mouse events).
//   bun drive.mjs <url|file> --actions <file.json> [--width W] [--height H] [--reduced]
// actions: ["eval", js] · ["click", selector] (a REAL mouse click at the element's centre) · ["key", key, modifiers?] (8 = shift) · ["wait", ms] · ["shot", path, selector|"html", scale, [x, y, w, h]?]
// It prints "eval: …", "shot: …", "exception: …", "console: <n> error(s)". Exit 1 if an eval throws, a console error or a page exception occurs.
// Chrome = $CHROME or /Applications/Google Chrome.app (local only: file:// pages and localhost; background networking is switched off).
import { readFileSync, mkdtempSync, rmSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve, dirname } from "node:path";
import { pathToFileURL } from "node:url";

const argv = process.argv.slice(2);
const opt = (n, d) => { const i = argv.indexOf(n); return i >= 0 ? argv[i + 1] : d; };
let target = argv[0];
if (!/^(file|http):/.test(target)) target = pathToFileURL(resolve(target.split("?")[0])).href + (target.includes("?") ? "?" + target.split("?").slice(1).join("?") : "");
const W = Number(opt("--width", 1440)), H = Number(opt("--height", 1800)), reduced = argv.includes("--reduced");
const actions = JSON.parse(readFileSync(opt("--actions"), "utf8"));
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
// the DevTools port: the first free one of 27511–27529 (inside this maker's band 27500–27599), or --port / $DRIVE_PORT
const free = (p) => { try { const sv = Bun.listen({ hostname: "127.0.0.1", port: p, socket: { data() {} } }); sv.stop(true); return true; } catch (_) { return false; } };
let PORT = Number(opt("--port", process.env.DRIVE_PORT || 0));
const BAND = Number(process.env.DRIVE_BAND || 27500);  // bundle: the port band is chosen by env (default 27500–27599)
if (!PORT) PORT = Array.from({ length: 19 }, (_, i) => BAND + 11 + i).find(free) || 0;
if (!(PORT >= BAND && PORT <= BAND + 99)) { console.log(`error: no free port inside ${BAND}–${BAND + 99}`); process.exit(2); }
const HOME_DIR = dirname(new URL(import.meta.url).pathname); mkdirSync(join(HOME_DIR, ".chrome"), { recursive: true });
const prof = mkdtempSync(join(HOME_DIR, ".chrome", "p-"));
const proc = Bun.spawn([CHROME, "--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${prof}`, "--no-first-run", "--no-default-browser-check", "--disable-background-networking", "--disable-component-update", "--disable-sync", "--disable-extensions", "--disable-features=Translate,MediaRouter,OptimizationHints", "--allow-file-access-from-files", "--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE localhost , EXCLUDE 127.0.0.1", "--hide-scrollbars", `--window-size=${W},${H}`, "about:blank"], { stderr: "pipe", stdout: "ignore" });
process.on("exit", () => { try { proc.kill(); } catch (_) {} });          // never leave a Chrome behind, even on an uncaught error
if (!(W > 0 && H > 0)) { console.log("error: bad --width / --height"); proc.kill(); process.exit(2); }
const stop = async (code) => { try { proc.kill(); await proc.exited; } catch (_) {} try { rmSync(prof, { recursive: true, force: true }); } catch (_) {} console.log(`chrome pid ${proc.pid} stopped (port ${PORT})`); process.exit(code); };
let wsUrl = "", buf = "";
const reader = proc.stderr.getReader(), dec = new TextDecoder();
const started = (async () => { while (!wsUrl) { const { value, done } = await reader.read(); if (done) break; buf += dec.decode(value); const m = /DevTools listening on (ws:\/\/\S+)/.exec(buf); if (m) wsUrl = m[1]; } })();
await Promise.race([started, Bun.sleep(20000)]);
if (!wsUrl) { console.log("error: chrome did not start\n" + buf.slice(0, 500)); await stop(2); }
const ws = new WebSocket(wsUrl);
await new Promise((ok, no) => { ws.onopen = ok; ws.onerror = no; });
let seq = 0; const waiting = new Map(), listeners = [];
ws.onmessage = (ev) => { const m = JSON.parse(ev.data); if (m.id && waiting.has(m.id)) { const { ok, no } = waiting.get(m.id); waiting.delete(m.id); m.error ? no(new Error(JSON.stringify(m.error))) : ok(m.result); } else if (m.method) listeners.forEach((f) => f(m)); };
const send = (method, params = {}, sessionId) => new Promise((ok, no) => { const id = ++seq; waiting.set(id, { ok, no }); ws.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) })); });
const { targetId } = await send("Target.createTarget", { url: "about:blank" });
const { sessionId } = await send("Target.attachToTarget", { targetId, flatten: true });
const S = (m, p) => send(m, p, sessionId);
let errors = 0, failed = false;
listeners.push((m) => {
  if (m.sessionId !== sessionId) return;
  if (m.method === "Runtime.consoleAPICalled" && (m.params.type === "error" || m.params.type === "assert")) { errors++; console.log("console: error " + m.params.args.map((a) => a.value ?? a.description ?? "").join(" ").slice(0, 300)); }
  if (m.method === "Runtime.exceptionThrown") { errors++; console.log("exception: " + (m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text).slice(0, 400)); }
  if (m.method === "Log.entryAdded" && m.params.entry.level === "error" && !/favicon/.test(m.params.entry.url || "")) { errors++; console.log("console: log-error " + m.params.entry.text.slice(0, 300) + " " + (m.params.entry.url || "")); }
});
await S("Page.enable"); await S("Runtime.enable"); await S("Log.enable");
await S("Emulation.setDeviceMetricsOverride", { width: W, height: H, deviceScaleFactor: 1, mobile: W < 500 });
if (reduced) await S("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: "reduce" }] });
const loaded = new Promise((ok) => listeners.push((m) => { if (m.sessionId === sessionId && m.method === "Page.loadEventFired") ok(); }));
await S("Page.navigate", { url: target });
await Promise.race([loaded, Bun.sleep(15000)]);
const evaluate = async (expression) => { const r = await S("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true }); if (r.exceptionDetails) throw new Error((r.exceptionDetails.exception?.description || r.exceptionDetails.text || "").slice(0, 1500)); return r.result.value; };
const rectOf = (sel) => evaluate(`(() => { const e = ${sel === "html" ? "document.documentElement" : `document.querySelector(${JSON.stringify(sel)})`}; if (!e) throw new Error('no element ${sel.replace(/'/g, "")}'); ${sel === "html" ? "" : "e.scrollIntoView({block:'center'});"} const r = e.getBoundingClientRect(); return {x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height, vx: r.left, vy: r.top}; })()`);
for (const a of actions) {
  try {
    if (a[0] === "wait") await Bun.sleep(a[1]);
    else if (a[0] === "eval") { const v = await evaluate(a[1]); console.log("eval: " + (typeof v === "string" ? v : JSON.stringify(v)).slice(0, 4000)); }
    else if (a[0] === "click") { const r = await rectOf(a[1]); const x = r.vx + r.w / 2, y = r.vy + r.h / 2; for (const type of ["mouseMoved", "mousePressed", "mouseReleased"]) await S("Input.dispatchMouseEvent", { type, x, y, button: "left", clickCount: 1 }); }
    else if (a[0] === "drag") { const [, sel, fx0, fy0, fx1, fy1, steps = 12] = a; const r = await rectOf(sel); const at = (f, g) => [r.vx + r.w * f, r.vy + r.h * g];
      let [x, y] = at(fx0, fy0); await S("Input.dispatchMouseEvent", { type: "mouseMoved", x, y }); await S("Input.dispatchMouseEvent", { type: "mousePressed", x, y, button: "left", buttons: 1, clickCount: 1 });
      for (let i = 1; i <= steps; i++) { [x, y] = at(fx0 + ((fx1 - fx0) * i) / steps, fy0 + ((fy1 - fy0) * i) / steps); await S("Input.dispatchMouseEvent", { type: "mouseMoved", x, y, button: "left", buttons: 1 }); await Bun.sleep(16); }
      await S("Input.dispatchMouseEvent", { type: "mouseReleased", x, y, button: "left", buttons: 0, clickCount: 1 }); }
    else if (a[0] === "key") { const k = a[1], modifiers = a[2] || 0, code = { ArrowRight: 39, ArrowLeft: 37, Enter: 13, Escape: 27 }[k] || k.toUpperCase().charCodeAt(0); for (const type of ["keyDown", "keyUp"]) await S("Input.dispatchKeyEvent", { type, key: k, modifiers, code: k.startsWith("Arrow") || k === "Enter" || k === "Escape" ? k : "Key" + k.toUpperCase(), windowsVirtualKeyCode: code, ...(k === "Enter" && type === "keyDown" ? { text: "\r" } : {}) }); }
    else if (a[0] === "shot") {
      const [, path, sel, scale = 1, clip] = a; mkdirSync(dirname(path), { recursive: true });
      let c; if (clip) c = { x: clip[0], y: clip[1], width: clip[2], height: clip[3], scale }; else { const r = await rectOf(sel); c = { x: r.x, y: r.y, width: Math.ceil(r.w), height: Math.ceil(r.h), scale }; }
      const { data } = await S("Page.captureScreenshot", { format: "png", clip: c, captureBeyondViewport: true });
      await Bun.write(path, Buffer.from(data, "base64")); console.log(`shot: ${path} ${c.width}x${c.height}`);
    }
  } catch (e) { failed = true; console.log("exception: action " + JSON.stringify(a).slice(0, 120) + " -> " + String(e.message || e).slice(0, 1500)); }
}
console.log(`console: ${errors} error(s)`);
try { ws.close(); } catch (_) {}
await stop(failed || errors ? 1 : 0);
