# demo_marimo.py — a marimo app that shows the moy-2 line widget and what the kernel sees. Run (inside this maker's port band 27500–27599):
#   marimo run demo_marimo.py --headless --no-token --port 27531
# run_marimo_check.sh drives it: the figure's own buttons / drag move the kernel's values (figure -> kernel); the Python buttons move the figure (kernel -> figure).
import marimo

app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from moy2line_widget import Moy2Line, kernel_recount

    inner = Moy2Line(state=0)                 # kernel -> figure at the start: open on the scene (state 0 = the two real rows, v1.1)
    w = mo.ui.anywidget(inner)
    return inner, kernel_recount, mo, w


@app.cell
def _(mo):
    mo.md("""
    # moy-2 の折り返しの道具の系列(olm113 → olm127)を AI と共読する(anywidget・iframe なし)/ co-reading the moy-2 reflection-tool line
    図の button・章・積み木のドラッグで動かすと、下の「kernel が見ている値」が変わります。下の Python の button(`inner.state = 8` などの一行)を押すと図が動きます。
    *Press the figure's buttons or drag over the rack: the kernel's view below changes. Press a Python button (one line such as `inner.state = 8`): the figure moves.*
    """)
    return


@app.cell
def _(inner, mo):
    def line(label, **traits):
        def click(_):
            for name, value in traits.items():
                setattr(inner, name, value)
        return mo.ui.button(label=label, on_click=click)

    lines = mo.hstack([line("inner.state = 8; inner.row = 'olm125:b0_j16'", state=8, row="olm125:b0_j16"), line("inner.state = 6; inner.arm = 'olm119'", state=6, arm="olm119"),
                       line("inner.state = 19", state=19), line("inner.lang = 'en'", lang="en"), line("inner.lang = 'ja'", lang="ja"), line("inner.state = 0", state=0)], justify="start", wrap=True)
    lines
    return


@app.cell
def _(w):
    w
    return


@app.cell
def _(inner, kernel_recount, mo, w):
    v = w.value
    k = kernel_recount()
    r = v.get("reading") or {}
    mo.Html(f"<div id='kernel-view'>kernel が見ている値: state = <b>{v.get('state')}</b> ・ row = <b>{v.get('row') or '—'}</b> ・ arm = <b>{v.get('arm') or '—'}</b> ・ lang = <b>{v.get('lang')}</b> ・ done = <b>{v.get('done')}</b>"
            f" <small id='inner-view'>(trait: inner.state = {inner.state} ・ inner.row = {inner.row or '—'})</small></div>"
            f"<div id='reading'>図が今出している文: <b>state {r.get('state')}</b> ・ {r.get('readout', '')}</div>"
            f"<div id='kernel-recount'>kernel の数え直し(raw rows): olm125 v3 {k['olm125']['v3']} ・ olm127 v3 {k['olm127']['v3']} ・ olm125 calc {k['olm125']['calc']} ・ rej {k['olm125']['rej']} ・ typ {' · '.join(k['olm125']['typ'])}</div>")
    return


if __name__ == "__main__":
    app.run()
