# demo_marimo.py — a marimo app that shows the widget and what the kernel sees (template). Run:  marimo run demo_marimo.py --headless --no-token --port <PORT>
# marimo draws its controls inside shadow roots, so a driver cannot `click` them; make_check.py's marimo steps walk the shadow roots with an eval and call .click() (figure -> kernel) and press the Python buttons (kernel -> figure).
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from widget import CoreadFigure

    w = CoreadFigure(state=0)
    inner = mo.ui.anywidget(w)
    return inner, mo, w


@app.cell
def _(inner, mo):
    mo.vstack([inner, mo.md(f"kernel sees: state = {inner.state} · t = {inner.t} · lang = {inner.lang} · done = {inner.done}")])
    return


@app.cell
def _(inner, mo):
    # kernel -> figure: a button per state; a driver presses them and waits for the figure to follow
    buttons = mo.hstack([mo.ui.button(label=f"inner.state = {i}", on_click=lambda _, i=i: setattr(inner.widget, "state", i)) for i in range(4)])
    buttons
    return


if __name__ == "__main__":
    app.run()
