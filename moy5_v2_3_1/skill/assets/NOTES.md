# NOTES — how this version was made, what was fixed, who pointed it out (template)

## vN (date) — what is new
- **State table**: (n states; chapters from `config.json`). After any renumbering, `python3 -I list_headings.py` and read the list.
- **Routes of each number**: pack_data.py (assert) → data.mjs (JS recount, stops the build) → check_claims.py (from scratch) → [widget kernel side].
- **Checks run**: build · list_headings · check_claims · make_check (console / robust / chapter buttons / min px / overflow) · [marimo / JupyterLab]. Results: ...

## vN.1 (date) — a small fix
- What: ... Why (who pointed it out, verbatim): "...". Files touched: ... Captures re-shot: ...

## Facts worth keeping (what surprised us)
- (e.g. a control that stopped the run and what it caught; a value in the brief that the data corrected; a limit of the drawing — two bodies in one projection are not depth-sorted against each other.)

## What I am least sure of
- ...
