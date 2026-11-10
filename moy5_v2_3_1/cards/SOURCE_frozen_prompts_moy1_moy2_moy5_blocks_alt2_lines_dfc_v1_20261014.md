# SOURCE: 凍結の問いと、足した文の逐語(判断層の返し 10-14 §1-2 の漏れ #1〜#3 への同梱・2026-10-14)

> 出所 = `ConstructGap/prompts.py`・`probe_registry.py`・`exp/essay_items_20261014.py`・`exp/alt2_methods_moy1_20261013.py`・`instruction_docs/`。本書は code から機械的に書き出した(手で打っていない)。md5 は UTF-8 の byte 列。

## moy-1 `higashida_circle` の open prompt(A・md5 `3c7a63dd0d2b4393820e7836458e33cd`・1294 字)

```
You analyze a geometric configuration. **No figure is given.** Only the coordinates below are available. The symbol names are neutral and carry no hint about their meaning.
# Objects to focus on (role binding)
Focus on the relation that holds among the following objects: {X1, X2, X3, X4}.
# Configuration
# The four common tangent lines of circles K1, K2 meet pairwise. The four MIXED intersections (one external + one internal tangent) are X1,X2,X3,X4; the two same-type intersections are He, Hi.
O1 = (-2.2849, -4.2209)
K1 = Circle(O1, 7.4607)
O2 = (10.1897, -0.5520)
K2 = Circle(O2, 3.6869)
X1 = (0.6526, 3.2154)
X2 = (7.3460, 3.1590)
X3 = (9.8079, -5.2117)
X4 = (4.2108, -8.8828)
He = (22.3772, 3.0324)
Hi = (6.0639, -1.7655)

# Premises (general, non-degenerate)
The two circles are disjoint and have four common tangents; the radii differ; the configuration is general (non-degenerate).
State the SINGLE most important invariant that ALWAYS holds for the general (non-special, non-degenerate) configuration, as a relation (concyclic / equal length / collinear / right angle). It must be non-trivial and follow from the structure. The answer is withheld.

Respond with JSON only:
{"conjecture": "<relation, in the given symbols>", "reason": "<why it holds>", "closes_goal": <true|false>}
```

## moy-2 `higashida_axis` の open prompt(A・md5 `637c061e8fa8d2f7276f99176e78bfe5`・1172 字)

```
You analyze a geometric configuration. **No figure is given.** Only the coordinates below are available. The symbol names are neutral and carry no hint about their meaning.
# Objects to focus on (role binding)
Focus on the relation that holds among the following objects: {Tc, Th, O3}.
# Configuration
# The contact points of the inner common tangent line l1 of circles c (center O2) and h1 (center O1) are Tc (on c) and Th (on h1). O3 is the midpoint of O1 and O2.
O1 = (10.1897, -0.5520)
h1 = Circle(O1, 3.6869)
O2 = (-2.2849, -4.2209)
c = Circle(O2, 7.4607)
Tc = (2.7678, 1.2685)
Th = (7.6927, -3.2647)
O3 = (3.9524, -2.3865)

# Premises (general, non-degenerate)
The two circles are disjoint and have an inner common tangent; the configuration is general (non-degenerate).
State the SINGLE most important invariant that ALWAYS holds for the general (non-special, non-degenerate) configuration, as a relation (midpoint / collinear / right angle / parallel). It must be non-trivial and follow from the structure. The answer is withheld.

Respond with JSON only:
{"conjecture": "<relation, in the given symbols>", "reason": "<why it holds>", "closes_goal": <true|false>}
```

## moy-5 `parabola_section`(6 月の門の `BASE` と同一) の open prompt(A・md5 `ee39ba02374a5b3fb6db8dafcef4704b`・1921 字)

```
You analyze a geometric configuration. **No figure is given.** Only the coordinates below are available. The symbol names are neutral and carry no hint about their meaning.
# Objects to focus on (role binding)
Focus on the relation that holds among the following objects: {E, J, K, P_y}.
# Configuration
# A circle c has center A and passes through B. C is a point outside c. The two tangent lines from C touch c at G and E (call f the tangent at G and g the tangent at E). F is the second intersection of line GA with c. The line j passes through F parallel to f; V is the intersection of g with j. The chord GE meets j at D, and the line e is perpendicular to j at D. The line h1 passes through V parallel to e. P_x is a point on h1. The ray from F through P_x meets e at K. The line m is perpendicular to that ray at P_x, and the line through K parallel to j meets m at P_y. The line through P_y parallel to h1 meets j at H, and the line through H parallel to the chord GE meets the tangent g at J.
A = (0.0000, 0.0000)
c = Circle(A, 4.0000)
B = (-3.1945, -2.4073)
C = (6.3891, 4.8145)
E = (3.6820, -1.5629)
G = (-0.4875, 3.9702)
F = (0.4875, -3.9702)
V = (2.7797, -3.6887)
Px = (2.2230, 0.8452)
K = (3.9585, 5.6606)
Py = (-7.3019, 4.2780)
J = (-0.7508, -12.0060)

# Premises (general, non-degenerate)
C lies outside the circle c; P_x is a GENERIC point on the line h1 (not a special position); the configuration is general (non-degenerate). State the invariant that holds for EVERY such P_x.
State the SINGLE most important invariant that ALWAYS holds for the general (non-special, non-degenerate) configuration, as a relation (equal length / a distance relation / collinear / a right angle / on a curve). It must be non-trivial and follow from the structure. The answer is withheld.

Respond with JSON only:
{"conjecture": "<relation, in the given symbols>", "reason": "<why it holds>", "closes_goal": <true|false>}
```

## moy-1 の封鎖の三文(B = A + 下・block の md5 `fdd78a4ed00e90988b90c63ab148efb8`・B の md5 `616682f531557c56d1103738b8d9dbda`)

```
Note: merely stating that the four points are 'concyclic' (that they lie on one common circle) is INSUFFICIENT. Identify that circle UNIQUELY: which known point is its center, and which segment is its diameter (or radius)? State the single most important invariant in a form that INCLUDES the identification of that circle.
```

## moy-5 の陽性統制 K(A + 下・block の md5 `5c8a4c5a0f3cba3d9f32175f31fd820a`・10-14 新設)

```
Hint: the relation in question is a mean proportional: the segment F–P_x is the mean proportional between F–V and F–P_y, that is, FPx^2 = FV·FPy, for every P_x. State the single most important invariant for E, J, K, P_y, and explain WHY it holds in a form that INCLUDES this relation.
```

## エッセイの枠(essay1 から不変)

```
FRAME  = 'Read the following essay.\n\n--- ESSAY ---\n{text}\n--- END ESSAY ---\n\n'
TURN1  = 'Read the following essay. When you have read it, reply with a three-sentence summary.\n\n--- ESSAY ---\n{text}\n--- END ESSAY ---'
```

## alt2 の腕の文(英文の逐語・`exp/alt2_methods_moy1_20261013.py`)

```
R-re2     (二回目)  : Answer again in the same JSON form.
R-quote2  (二回目)  : Merely stating "{conj}" is INSUFFICIENT. Answer again in the same JSON form.
Q-define2 (二回目)  : For every object your conjecture refers to, which of the given symbols determine it? State that, then answer again in the same JSON form.
R-blindK  (各回)    : Merely stating that is INSUFFICIENT. Answer again in the same JSON form.
G-define  (末尾の注記): Note: for every object your conjecture refers to, say which of the given symbols determine it.
X-seq     (末尾の注記): Note: for a different problem about three numbers a, b, c: the conjecture "a, b, c are in arithmetic progression" is INSUFFICIENT; the conjecture "a, b, c are in arithmetic progression, and the common difference is b − a" is complete.
```

## `instruction_docs/D-fc_v1.txt`(md5 `5dffad4a2b6f66fda4c7d299118b6144`・828 字)

```
1. List the named objects and what the task asks about. 2. From the coordinates, compute candidate relations among the focus objects (distances, slopes, angles, incidences). 3. Keep only relations that hold to numerical precision. 4. Discard relations that are trivial or that hold only for these particular numbers. 5. Choose the single strongest relation. 6. Check the arithmetic once more. 7. Before reporting, make the relation complete. A relation is complete when every object it depends on is identified among the given symbols: for a collinearity, name the line; for an equal length, name both segments; for a common circle, name its center and a diameter or radius by name, among the given symbols (numerical coordinates do not count); for a right angle, name its vertex and both arms. 8. Report in the requested form.
```

## `instruction_docs/D-fc_v0.txt`(md5 `049bd55b7465af4baa212a0bbf2e4f73`・781 字)

```
1. List the named objects and what the task asks about. 2. From the coordinates, compute candidate relations among the focus objects (distances, slopes, angles, incidences). 3. Keep only relations that hold to numerical precision. 4. Discard relations that are trivial or that hold only for these particular numbers. 5. Choose the single strongest relation. 6. Check the arithmetic once more. 7. Before reporting, make the relation complete. A relation is complete when every object it depends on is identified among the given symbols: for a collinearity, name the line; for an equal length, name both segments; for a common circle, name its center and a diameter or radius among the known points; for a right angle, name its vertex and both arms. 8. Report in the requested form.
```

