// widget_glue.js — the hand-written part of the anywidget front-end: traits <-> figure (template). Appended by build.mjs after DATA, I18N, FIGURE, mountFigure and SKELETON.
//   kernel -> figure:  state, lang, t, theme          figure -> kernel:  state, lang, t, theme, done, reading (what is on the screen, as text and numbers)
// A value this view sent a moment ago and has since moved on from, coming back from the kernel, is not a command (marimo also fires change:<name> for unchanged traits): `stale` guards the loop.
async function render({ model, el }) {
  const root = document.createElement("div");
  root.className = "sh iso"; root.tabIndex = 0; root.setAttribute("role", "group"); root.dataset.state = "0"; root.innerHTML = SKELETON; el.appendChild(root);
  const themeOf = () => { const t = model.get("theme"); return t === "auto" ? (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light") : t; };
  root.dataset.theme = themeOf();
  const sent = { state: [], lang: [], t: [] }, mark = (k, v) => { sent[k].push([v, performance.now()]); if (sent[k].length > 24) sent[k].shift(); };
  const stale = (k, v) => { const now = performance.now(), list = sent[k]; return !!list && list.length > 1 && list.slice(0, -1).some(([x, at]) => x === v && now - at < 1500); };
  const put = (k, v) => { if (model.get(k) === v) return; if (sent[k]) mark(k, v); model.set(k, v); model.save_changes(); };
  let api = null, lastReading = "";
  const host = {
    lang: () => model.get("lang"), state: () => model.get("state"), theme: themeOf,
    onState: (n) => put("state", n), onLang: (l) => put("lang", l), onTheme: (t) => put("theme", t), onSync: ({ t }) => put("t", t),
    onDone: (flag) => { if (model.get("done") !== flag) { model.set("done", flag); model.save_changes(); } },
    onReading: (r) => { const s = JSON.stringify(r); if (s !== lastReading) { lastReading = s; model.set("reading", r); model.save_changes(); } },
  };
  api = mountFigure(root, host);
  const offs = [], on = (name, fn) => { model.on(name, fn); offs.push(() => model.off(name, fn)); };
  on("change:state", () => { const v = model.get("state"); if (!api || v === api.state || stale("state", v)) return; api.goto(v, { fromKernel: true }); });
  on("change:lang", () => { const v = model.get("lang"); if (!api || v === api.lang || stale("lang", v)) return; api.setLang(v, true); });
  on("change:t", () => { const v = model.get("t"); if (!api || v < 0 || v === api.t || stale("t", v)) return; api.setT(v, true); });
  on("change:theme", () => { if (api) api.setTheme(themeOf()); });
  return () => { offs.forEach((off) => off()); api.destroy(); root.remove(); };
}
export default { render };
