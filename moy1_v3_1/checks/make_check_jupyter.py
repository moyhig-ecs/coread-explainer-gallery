"""Write the JupyterLab drive actions for station 2 (moy-1) v3.1 with the waits of station 3 v2.1.

Fixed sleeps are replaced by `until` and by re-running a cell until ITS OWN output matches (station 3 v2.1's `__retry`).
The kernel's recount compares the frozen files (always the same) with the figure's screen; a re-run can only pass
when the screen's numbers arrive, so a real mismatch still times out. Each cell's output is read on its own
(the old step for the sae chapter searched all outputs joined, so state 4's 'equal': True could pass it).
usage: python -I checks/make_check_jupyter.py checks/check_jupyter.json(entry の folder から)
"""
import json
import sys

HELPERS = (
    "(() => { window.__p = window.jupyterapp.shell.currentWidget; window.__nb = () => window.__p.content; "
    "window.__run = (i) => { const nb = window.__nb(); nb.activeCellIndex = i; return window.jupyterapp.commands.execute('notebook:run-cell'); }; "
    "window.__out = (i) => { const c = window.__nb().widgets[i]; const o = c && c.node.querySelector('.jp-OutputArea'); return o ? o.textContent : ''; }; "
    "window.__last = {}; window.__tries = {}; window.__seen = {}; "
    "window.__retry = (i, src, every) => { const cur = window.__out(i); if (new RegExp(src).test(cur)) return true; const now = Date.now(); "
    "if (!window.__last[i] || now - window.__last[i] > every) { if (cur) (window.__seen[i] = window.__seen[i] || []).push(cur.slice(0, 240)); "
    "window.__last[i] = now; window.__tries[i] = (window.__tries[i] || 0) + 1; window.__run(i); } return false; }; "
    "window.__fig = () => document.querySelector('.jp-OutputArea .sh'); "
    "window.__f = () => { const sh = window.__fig(); return sh ? {state: sh.dataset.state, chapter: sh.dataset.chapter, lang: sh.dataset.lang, "
    "readout: (sh.querySelector('[data-readout]') || {}).textContent} : null; }; return 'helpers'; })()"
)

R_VALUES = "state 5 · t \\d+ · lang ja"            # cell 4 prints: state <n> · t <t> · lang <lang> · done ...
R_STATE4 = "'state': 4,[\\s\\S]*'equal': True"           # cell 5: w.state = 4 → check_counts()
R_STATE18 = "'state': 18,[\\s\\S]*'equal': True"         # cell 6: goto_chapter('sae') → check_counts()


def assert_fig(state, lang, key):
    return (f"(() => {{ const f = window.__f(); if (!f || f.state !== '{state}' || f.lang !== '{lang}') "
            f"throw new Error('kernel -> figure failed: ' + JSON.stringify(f)); return JSON.stringify({{{key}: f}}); }})()")


def assert_cell(i, rx, key, extra=""):
    return (f"(() => {{ const o = window.__out({i}); if (!new RegExp({json.dumps(rx)}).test(o)) "
            f"throw new Error('cell {i} does not show the expected output: ' + o.slice(-300)); {extra}"
            f"return JSON.stringify({{{key}: true, tries: window.__tries[{i}] || 0, seen_before: window.__seen[{i}] || [], out: o.slice(-300)}}); }})()")


ACTIONS = [
    ["until", "!!window.jupyterapp && document.querySelectorAll('.jp-Notebook .jp-Cell').length === 7", 90000],
    ["wait", 1500],
    ["click", ".jp-Notebook .jp-Cell:nth-of-type(2) .jp-InputArea-editor"],
    ["until", "!!window.jupyterapp.shell.currentWidget && window.jupyterapp.commands.isEnabled('notebook:run-cell')", 20000],
    ["eval", HELPERS],
    ["until", "!!(window.__p.sessionContext.session && window.__p.sessionContext.session.kernel && "
              "window.__p.sessionContext.session.kernel.connectionStatus === 'connected')", 60000],
    ["eval", "window.__run(0).then(() => 'cell 0 (markdown)')"],
    # cell 1: the widget (state 0)
    ["until", "window.__fig() || window.__retry(1, '.', 15000) && false", 90000],
    ["until", "window.__fig() && window.__fig().dataset.state === '0'", 30000],
    ["eval", "JSON.stringify({after_cell_1_widget: window.__f(), tries: window.__tries[1] || 0})"],
    ["shot", "captures/J1_jupyterlab_state0.png", ".jp-LabShell", 1],
    # cell 2: kernel -> figure (state 8, en)
    ["eval", "window.__run(2).then(() => 'cell 2: w.state = 8, w.lang = en (kernel -> figure)')"],
    ["until", "window.__fig().dataset.state === '8' && window.__fig().dataset.lang === 'en'", 30000],
    ["eval", assert_fig("8", "en", "after_cell_2_python_wrote_state_8_en")],
    # cell 3: kernel -> figure (ja, chapter open = state 4, t = 1)
    ["eval", "window.__run(3).then(() => 'cell 3: lang ja, goto_chapter(open), t = 1 (kernel -> figure)')"],
    ["until", "window.__fig().dataset.state === '4' && window.__fig().dataset.lang === 'ja'", 30000],
    ["eval", assert_fig("4", "ja", "after_cell_3")],
    # figure -> kernel: press next in the figure, then cell 4 until it prints state 5
    ["eval", "window.__fig().querySelector('.sh-next').click(); 'figure -> kernel: pressed next (state 4 -> 5)'"],
    ["until", "window.__fig().dataset.state === '5'", 20000],
    ["until", f"window.__retry(4, {json.dumps(R_VALUES)}, 2500)", 40000],
    ["eval", assert_cell(4, R_VALUES, "figure_to_kernel_values_cell_4")],
    ["shot", "captures/J2_jupyterlab_figure_button_reached_kernel.png", ".jp-LabShell", 1],
    # cell 5: the kernel's recount of state 4 (the cell sleeps 3.0 s: re-run no sooner than 6 s)
    ["until", f"window.__retry(5, {json.dumps(R_STATE4)}, 6000)", 60000],
    ["eval", assert_cell(5, R_STATE4, "recount_state4_equal")],
    # cell 6: goto_chapter('sae') and the recount of state 18 (sleeps 2.0 s)
    ["until", f"window.__retry(6, {json.dumps(R_STATE18)}, 6000) && window.__fig().dataset.state === '18'", 60000],
    ["eval", assert_cell(6, R_STATE18, "sae_recount_state18_equal",
                         "if (window.__fig().dataset.state !== '18') throw new Error('the figure did not follow goto_chapter(sae): ' + window.__fig().dataset.state); ")],
    ["shot", "captures/J3_jupyterlab_sae_state18.png", ".jp-LabShell", 1],
    ["eval", "JSON.stringify({tries_until_equal_by_cell: window.__tries, note: 'runs of each cell until its own output matched (1 = the first run)'})"],
]

if __name__ == "__main__":
    out = sys.argv[1]
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(ACTIONS, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print(f"wrote {out}: {len(ACTIONS)} actions")
