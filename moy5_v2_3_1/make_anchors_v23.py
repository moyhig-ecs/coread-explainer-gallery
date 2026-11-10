"""make_anchors_v23.py — the anchors of v2.3 (BRIEF v2.3 §1: the cutting plane = the plane through the line FVD (line j) perpendicular to the board) and their rows in CLAIMS_v23.md. Never written by hand.
The plane is DRAWING (computed from the frozen coordinates of SOURCE 10-14; not data, nothing about a model). Three routes: pack_data.py (asserts, generated/pack.json construction.plane),
the page (FIGURE.planeCheck on what it draws, make_check.py check_v23) and check_claims.py (kind `plane`, recomputed here from the SOURCE by separate code).
    python -I make_anchors_v23.py      (idempotent: replaces the anchors of kind `plane`)
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = "conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md"
ROWS = [  # (quantity, expect, tol, the claim as the figure / NOTES says it) — the expected values are BRIEF v2.3 §1 (the main session's values from pack.json construction)
    ("u_x", 0.992546, 1e-6, "the unit along j (= the line FVD, through F parallel to f), x"),
    ("u_y", 0.121874, 1e-6, "the unit along j, y"),
    ("V_off_j", 4.1e-5, 1e-6, "V (the question's coordinates, rounded to 4 decimals) lies on j: its distance from j"),
    ("D_off_j", 0.0, 1e-9, "D (= the chord GE meets j) lies on j"),
    ("tV_over_tD", 0.500007, 1e-6, "V is the midpoint of FD: t_V / t_D along j from F"),
    ("FV", 2.3094, 1e-4, "|FV|"),
    ("FD", 4.6188, 1e-4, "|FD| (= 2 |FV|)"),
    ("A_to_j", 4.000018, 1e-6, "the distance from A to j = the radius r of the circle c (4)"),
    ("AF_dot_j", 0.0, 1e-9, "AF ⟂ j (|unit AF · u|) → j touches c at F; the cutting plane touches the Dandelin sphere at F = the focus"),
    ("par_n", 41, 0, "the drawn parabola's samples (40 from the vertex j ∩ g towards F up to H + the top = P_y lifted above H; the brief asks ≥ 20)"),
    ("par_off_plane", 0.0, 1e-6, "every sample of the drawn parabola lies in the cutting plane (largest distance from the vertical plane through j)"),
    ("par_on_cone", 0.0, 1e-4, "every sample of the drawn parabola lies on the cone (apex C, axis CA, half-angle 30°): largest |angle to the axis − 30°| in radians"),
    ("plane_dot_board", 0.0, 1e-9, "the cutting plane is perpendicular to the board: |its normal · the board's normal| (the normal from the drawn rectangle's two edges)"),
]
anchors = [a for a in json.loads((HERE / "claims_anchors.json").read_text(encoding="utf-8")) if a.get("kind") != "plane"]
last = max(int(a["id"][1:]) for a in anchors)
new = [{"id": f"K{last + 1 + i}", "kind": "plane", "q": q, "expect": e, "tol": tol, "file": SRC, "note": note} for i, (q, e, tol, note) in enumerate(ROWS)]
(HERE / "claims_anchors.json").write_text(json.dumps(anchors + new, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
lines = ["# CLAIMS_v23 — the cutting plane of v2.3 (BRIEF v2.3 §1 · 2026-11-09 · 依頼者「moy-5の円錐断面が直線FVDを鉛直に切る平面だとわかるように図示する」)", "",
         "The cutting plane (through the line FVD = line j, perpendicular to the board), its directrix (the vertical line through D) and the parabola drawn in it are **drawing**: computed from the frozen coordinates of SOURCE 10-14 (not data; it says nothing about a model).",
         "It belongs to the overlay of v2.2 (**default: shown**; the page's button 「円錐を重ねる」/ \"cone overlay\", `?cone=0` and the widget's trait `cone` hide it with the rest). Written by `make_anchors_v23.py`; `check_claims.py` (kind `plane`) recomputes each value from the SOURCE.", "",
         "| id | claim | source (file · quantity) | level | state |", "|---|---|---|---|---|"]
for a in new:
    lines.append(f"| {a['id']} | {a['note']} · {a['q']} = {a['expect']} (tol {a['tol']:g}) | `{SRC}` · coordinates A · C · G · E · F · V · P_x · c = Circle(A, 4) → `{a['q']}` | 作図(L1 の座標から) | 0, 7 |")
(HERE / "CLAIMS_v23.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"anchors: {len(anchors)} + {len(new)} (kind plane: {new[0]['id']}..{new[-1]['id']}) · CLAIMS_v23.md {len(new)} rows")
