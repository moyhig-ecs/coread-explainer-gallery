"""make_marimo_check.py — writes checks/check_marimo.json: the widget inside marimo, both directions (figure -> kernel and kernel -> figure), and two stills.
marimo draws its controls (and the widget) inside shadow roots, so the steps walk the shadow roots with an eval and call .click() / dispatch pointer events.
    python3 -I make_marimo_check.py      then   sh run_marimo_check.sh
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CAP = (HERE / "captures").as_posix()
H = r"""const find = (root, sel) => { const f = root.querySelector(sel); if (f) return f; for (const el of root.querySelectorAll('*')) { if (el.shadowRoot) { const r = find(el.shadowRoot, sel); if (r) return r; } } return null; };
const all = (root, sel, acc = []) => { root.querySelectorAll(sel).forEach((e) => acc.push(e)); for (const el of root.querySelectorAll('*')) if (el.shadowRoot) all(el.shadowRoot, sel, acc); return acc; };
const sh = () => find(document, '.sh'); const kv = () => (find(document, '#kernel-view') || {}).textContent || ''; const rd = () => (find(document, '#reading') || {}).textContent || ''; const kr = () => (find(document, '#kernel-recount') || {}).textContent || '';
const pyButton = (label) => all(document, 'button').find((b) => b.textContent.trim() === label);
const until = async (f, ms) => { const t0 = Date.now(); while (Date.now() - t0 < ms) { try { if (f()) return true; } catch (_) {} await new Promise((r) => setTimeout(r, 250)); } return false; };"""
step = lambda body: ["eval", f"(async () => {{ {H}\n{body} }})()"]
steps = [
    ["wait", 4000],
    step("const ok = await until(() => sh() && sh().dataset.state === '0' && kv().includes('state = 0'), 60000); if (!ok) throw new Error('marimo: the widget did not open on state 0: ' + kv()); return JSON.stringify({marimo_open: true, kernel: kv().slice(0, 120), recount: kr().slice(0, 160)});"),
    ["shot", f"{CAP}/M1_marimo_open_state0.png", "html", 1, [0, 0, 1440, 1400]],
    # figure -> kernel: the figure's own buttons
    step("sh().querySelector('.sh-step[data-n=\"8\"]').click(); const ok = await until(() => kv().includes('state = 8') && kv().includes('olm125:b1_j17'), 20000); if (!ok) throw new Error('figure -> kernel (state 8): ' + kv()); return JSON.stringify({figure_to_kernel_state: true, kernel: kv().slice(0, 140)});"),
    # figure -> kernel: a drag on the rack picks another row (pointer events on the svg)
    step("const svg = sh().querySelector('.fig-svg'), r = svg.getBoundingClientRect(); const ev = (type, fx, fy) => svg.dispatchEvent(new PointerEvent(type, { clientX: r.left + r.width * fx, clientY: r.top + r.height * fy, pointerId: 7, pointerType: 'mouse', button: 0, buttons: type === 'pointerup' ? 0 : 1, bubbles: true, composed: true }));"
         " ev('pointerdown', 0.3, 0.45); for (let i = 1; i <= 10; i++) ev('pointermove', 0.3 + 0.03 * i, 0.45 + 0.015 * i); ev('pointerup', 0.6, 0.6);"
         " const picked = (sh().querySelector('.rk[data-sel]') || {}).dataset; const id = picked && picked.r; const ok = await until(() => id && id !== 'olm125:b1_j17' && kv().includes(id), 20000); if (!ok) throw new Error('figure -> kernel (drag): ' + id + ' / ' + kv()); return JSON.stringify({figure_to_kernel_drag: true, picked: id, kernel: kv().slice(0, 160)});"),
    ["shot", f"{CAP}/M2_marimo_drag_reached_kernel.png", "html", 1, [0, 0, 1440, 1400]],
    # kernel -> figure: a Python button
    step("const b = pyButton(\"inner.state = 6; inner.arm = 'olm119'\"); if (!b) throw new Error('no python button'); b.click(); const ok = await until(() => sh().dataset.state === '6' && (sh().querySelector('.fig-side .fx-h') || {}).textContent.includes('olm119') && kv().includes('state = 6'), 30000); if (!ok) throw new Error('kernel -> figure: ' + sh().dataset.state + ' / ' + kv()); return JSON.stringify({kernel_to_figure: true, figure_state: sh().dataset.state, side: sh().querySelector('.fig-side .fx-h').textContent.slice(0, 60), kernel: kv().slice(0, 140)});"),
    step("const b = pyButton(\"inner.state = 8; inner.row = 'olm125:b0_j16'\"); b.click(); const ok = await until(() => sh().dataset.state === '8' && (sh().querySelector('.rk[data-sel]') || {dataset: {}}).dataset.r === 'olm125:b0_j16', 30000); if (!ok) throw new Error('kernel -> figure (row)'); return JSON.stringify({kernel_to_figure_row: true, lit: sh().querySelector('.rk[data-sel]').dataset.r, reading: rd().slice(0, 140)});"),
    step("const b = pyButton(\"inner.lang = 'en'\"); b.click(); const ok = await until(() => sh().dataset.lang === 'en' && kv().includes('lang = en'), 20000); if (!ok) throw new Error('kernel -> figure (lang)'); return JSON.stringify({kernel_to_figure_lang: true, kicker: sh().querySelector('.sh-kicker').textContent});"),
    ["shot", f"{CAP}/M3_marimo_python_wrote_state8_row_en.png", "html", 1, [0, 0, 1440, 1400]],
]
(HERE / "checks").mkdir(exist_ok=True)
(HERE / "checks" / "check_marimo.json").write_text(json.dumps(steps, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote checks/check_marimo.json ({len(steps)} steps)")
