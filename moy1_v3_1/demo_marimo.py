# demo_marimo.py — a marimo app that shows the widget and what the kernel sees. Run:  marimo run demo_marimo.py --headless --no-token --port 27451
# marimo draws its controls inside shadow roots, so a driver cannot `click` them; run_marimo_check.sh walks the shadow roots with an eval and calls .click() (figure -> kernel) and presses the Python buttons (kernel -> figure).
import marimo

app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from widget import CHAPTERS, STATES, CoreadFigure

    w = CoreadFigure(state=0)
    inner = mo.ui.anywidget(w)
    return CHAPTERS, STATES, inner, mo, w


@app.cell
def _(inner, mo):
    mo.vstack([inner, mo.md(f"kernel sees: state = {inner.state} · t = {inner.t} · lang = {inner.lang} · done = {inner.done}")])
    return


@app.cell
def _(CHAPTERS, inner, mo):
    # kernel -> figure: a button per chapter; a driver presses them and waits for the figure to follow
    buttons = mo.hstack([mo.ui.button(label=f"chapter {name}", on_click=lambda _, a=a: setattr(inner.widget, "state", a)) for name, (a, b) in CHAPTERS.items()])
    buttons
    return


@app.cell
def _(inner, mo):
    # the kernel's own recount against what the screen reports (a third route for the numbers)
    mo.md(f"kernel recount: `{inner.widget.check_counts()}`")
    return


if __name__ == "__main__":
    app.run()
