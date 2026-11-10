# CLAIMS_v22 — the overlay of v2.2 (BRIEF v2.2 §1 · 2026-11-07): the board read as the plane through the axis of a cone

The overlay (the cone, the Dandelin sphere, the contact circle, the cut's parabola) is **drawing**: computed from the frozen coordinates of SOURCE 10-14 (not data; it says nothing about a model).
**Default: shown** (the page's button 「円錐を重ねる」/ "cone overlay" and the widget's trait `cone` hide it). Written by `make_anchors_v22.py`; `check_claims.py` (kind `cone`) recomputes each value from the SOURCE.

| id | claim | source (file · quantity) | level | state |
|---|---|---|---|---|
| K429 | C lies on f = the tangent of the circle at G (a generatrix of the cone in the board) · C_on_f ≈ 0 (tol 0.001) | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `C_on_f` | 作図(L1 の座標から) | 0, 7 |
| K430 | C lies on g = the tangent at E (the other generatrix; J is on g, so CJ is a generatrix) → C = the apex · C_on_g ≈ 0 (tol 0.001) | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `C_on_g` | 作図(L1 の座標から) | 0, 7 |
| K431 | F = the antipode of G on the circle (so j, through F parallel to f, touches the sphere at F = the focus) · F_antipode_of_G ≈ 0 (tol 0.001) | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `F_antipode_of_G` | 作図(L1 の座標から) | 0, 7 |
| K432 | the chord GE is perpendicular to the axis CA (GE = the trace of the contact circle's plane) · GE_perp_axis ≈ 0 (tol 0.001) | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `GE_perp_axis` | 作図(L1 の座標から) | 0, 7 |
| K433 | the cone's half-angle asin(r / CA) = 30° (r 4, CA 8) · half_angle_deg = 30.0 (tol 0.0001) | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `half_angle_deg` | 作図(L1 の座標から) | 0, 7 |
| K434 | P_y lifted above H by HP_y (the cut folded up about j) lies on the cone (angle to the axis = the half-angle, radians) · Py_on_cone ≈ 0 (tol 0.0001) | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` · coordinates A · C · G · E · F · P_x · c = Circle(A, 4) → `Py_on_cone` | 作図(L1 の座標から) | 0, 7 |
