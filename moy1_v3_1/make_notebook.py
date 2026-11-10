"""make_notebook.py — writes demo_jupyter.ipynb (run the cells one at a time). Kept as a script so the notebook is generated, not hand-edited."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = lambda cid, *lines: {"cell_type": "markdown", "id": cid, "metadata": {}, "source": [l + "\n" for l in lines[:-1]] + [lines[-1]]}
code = lambda cid, *lines: {"cell_type": "code", "execution_count": None, "id": cid, "metadata": {}, "outputs": [], "source": [l + "\n" for l in lines[:-1]] + [lines[-1]]}
cells = [
    md("c1", "# moy-1: block で何が替わり、open で何が起こらないか(共読の図解・JupyterLab・anywidget)", "",
       "図の button・章の button・滑り棒で動かすと、下の cell の値が変わります。Python の側で `w.state = 8` のように書くと図が動きます。cell は **上から 1 つずつ**実行してください(図の側の値は、cell と cell の間に kernel へ届きます)。", "",
       "*Press the figure's buttons, the chapter buttons or slide: the values read in the cells below change. Write `w.state = 8` and the figure moves. Run the cells one at a time (what the figure reports reaches the kernel between cells).*"),
    code("c2", "import sys", "sys.path.insert(0, \".\")          # open this notebook from the entry's folder", "from widget import CoreadFigure", "w = CoreadFigure(state=0)     # 0 = the problem figure", "w"),
    code("c3", "# kernel -> figure: the figure above moves", "w.state = 8                  # blocked: the ten bands", "w.lang = \"en\""),
    code("c4", "w.lang = \"ja\"", "w.goto_chapter(\"open\")      # the first state of a chapter", "w.t = 1                      # the focus row s1"),
    code("c5", "# figure -> kernel: press a button of the figure, then run this cell", "print(\"state\", w.state, \"· t\", w.t, \"· lang\", w.lang, \"· done\", w.done)", "print(w.reading.get(\"kicker\"))", "print(w.reading.get(\"readout\"))"),
    code("c6", "# the kernel's own recount against what the screen reports", "w.state = 4", "import time; time.sleep(3.0)", "w.check_counts()"),
    code("c7", "# v2: the chapter 'construction x SAE trajectory' (states 18-24; v2.1: olm62 = 22-23): where the text names O1O2 / He-Hi and what the layer-32 SAE's four groups do around it", "w.goto_chapter(\"sae\")", "import time; time.sleep(2.0)", "w.check_counts()"),
]
nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
(HERE / "demo_jupyter.ipynb").write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print("demo_jupyter.ipynb written:", len(cells), "cells")
