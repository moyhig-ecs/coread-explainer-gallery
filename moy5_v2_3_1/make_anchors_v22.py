"""make_anchors_v22.py — the anchors of v2.2 (BRIEF v2.2 §1: the board read as the plane through the axis of a cone) and their rows in CLAIMS_v22.md. Never written by hand.
The overlay is DRAWING (computed from the frozen coordinates of SOURCE 10-14; not data, nothing about a model). These anchors say that its geometry holds on those coordinates;
check_claims.py (kind `cone`) recomputes it from the SOURCE, apart from figure.js (whose FIGURE.coneCheck is the page's route, make_check.py check_v22).
    python -I make_anchors_v22.py      (idempotent: replaces the anchors of kind `cone`)
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = "conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md"
ROWS = [  # (quantity, expect, tol, the claim as the figure / NOTES says it)
    ("C_on_f", 0.0, 1e-3, "C lies on f = the tangent of the circle at G (a generatrix of the cone in the board)"),
    ("C_on_g", 0.0, 1e-3, "C lies on g = the tangent at E (the other generatrix; J is on g, so CJ is a generatrix) → C = the apex"),
    ("F_antipode_of_G", 0.0, 1e-3, "F = the antipode of G on the circle (so j, through F parallel to f, touches the sphere at F = the focus)"),
    ("GE_perp_axis", 0.0, 1e-3, "the chord GE is perpendicular to the axis CA (GE = the trace of the contact circle's plane)"),
    ("half_angle_deg", 30.0, 1e-4, "the cone's half-angle asin(r / CA) = 30° (r 4, CA 8)"),
    ("Py_on_cone", 0.0, 1e-4, "P_y lifted above H by HP_y (the cut folded up about j) lies on the cone (angle to the axis = the half-angle, radians)"),
]
anchors = [a for a in json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8")) if a.get("kind") != "cone"]
last = max(int(a["id"][1:]) for a in anchors)
new = []
for i, (q, e, tol, note) in enumerate(ROWS):
    new.append({"id": f"K{last + 1 + i}", "kind": "cone", "q": q, "expect": e, "tol": tol, "file": SRC, "note": note})
(HERE / "claims_anchors.json").write_text(json.dumps(anchors + new, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
lines = ["# CLAIMS_v22 — the overlay of v2.2 (BRIEF v2.2 §1 · 2026-11-07): the board read as the plane through the axis of a cone", "",
         "The overlay (the cone, the Dandelin sphere, the contact circle, the cut's parabola) is **drawing**: computed from the frozen coordinates of SOURCE 10-14 (not data; it says nothing about a model).",
         "**Default: shown** (the page's button 「円錐を重ねる」/ \"cone overlay\" and the widget's trait `cone` hide it). Written by `make_anchors_v22.py`; `check_claims.py` (kind `cone`) recomputes each value from the SOURCE.", "",
         "| id | claim | source (file · quantity) | level | state |", "|---|---|---|---|---|"]
for a in new:
    lines.append(f"| {a['id']} | {a['note']} · {a['q']} {'= ' + str(a['expect']) if a['expect'] else '≈ 0'} (tol {a['tol']:g}) | `{SRC}` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `{a['q']}` | 作図(L1 の座標から) | 0, 7 |")
(HERE / "CLAIMS_v22.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"anchors: {len(anchors)} + {len(new)} (kind cone: {new[0]['id']}..{new[-1]['id']}) · CLAIMS_v22.md {len(new)} rows")
