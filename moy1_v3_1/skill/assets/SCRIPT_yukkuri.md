# SCRIPT — a two-voice scene for the video (template)

- Length: about N seconds (characters / 7.4 per second + 0.45 s between lines). **≤ 150 s in all.** The first 10 s (lines 01–02) are state 0, the scene: the core is visible from the first second.
- Two voices: **A** = the listener (asks; the question is the state's headline, shortened), **B** = the explainer. No real character's name, picture or voice.
- Each line names the state it cues and the claim ids it rests on. Numbers are read from the data by `make_script.py`, never typed.

| # | voice | line (spoken) | cue (the state shown) | length | start | claims |
|---|---|---|---|---|---|---|
| 01 | A | <the question of state 0, short> | state 0 | 3.0 s | 0:00.0 | K01 |
| 02 | B | <the answer in one breath; the number read from the data> | (same state) | 5.0 s | 0:03.5 | K04 |
| 03 | A | <the next question> | state 1 | ... | ... | ... |

## Switching the states (a guide for the editor)
| state | starts | headline (A's line shortens this) | the picture |
|---|---|---|---|
| 0 | 0:00 | ... | ... |

## Reading guide (for a voice synthesiser)
| written | read as |
|---|---|
| ... | ... |

Caption to add if wanted: "The figure is illustrative. The numbers are copies and counts of frozen values."
