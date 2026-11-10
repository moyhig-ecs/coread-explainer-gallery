# demo_marimo.py — the moy-5 figure in marimo, with what the kernel sees.   marimo run demo_marimo.py --headless --no-token --port 27731
import marimo

app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from widget import Moy5RouteFigure

    w = Moy5RouteFigure(state=1)
    fig = mo.ui.anywidget(w)
    return fig, mo, w


@app.cell
def _(fig, mo):
    mo.vstack([fig, mo.md(f"**kernel sees**: state = `{fig.state}` · lang = `{fig.lang}` · done = `{fig.done}` · cone = `{fig.cone}` · readout = `{(fig.reading or {}).get('readout', '')}`")])
    return


@app.cell
def _(fig, mo):
    # kernel -> figure: one button per chapter (the first state of each chapter, read from config.json)
    import json, pathlib
    chapters = json.loads((pathlib.Path(__file__).parent / "config.json").read_text())["chapters"]
    buttons = mo.hstack([mo.ui.button(label=f"go {c} → {a}", on_click=lambda _, a=a: setattr(fig.widget, "state", a)) for c, a, _b in chapters] + [mo.ui.button(label="lang en", on_click=lambda _: setattr(fig.widget, "lang", "en")),
                         mo.ui.button(label="cone off", on_click=lambda _: setattr(fig.widget, "cone", False)), mo.ui.button(label="cone on", on_click=lambda _: setattr(fig.widget, "cone", True))])   # v2.2: the overlay on states 0 and 7
    buttons
    return


@app.cell
def _(fig, mo):
    mo.md(f"**kernel check (route 5)**: `{fig.widget.kernel_check()}`")
    return


if __name__ == "__main__":
    app.run()
