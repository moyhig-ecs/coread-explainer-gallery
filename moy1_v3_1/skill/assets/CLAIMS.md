# CLAIMS — what the figure says, where each number comes from (template)

Every sentence the figure prints about the data is a row here, with its source (file + key) and its level. `check_claims.py` looks at each place: an anchor id (K..) in `claims_anchors.json` must have a row here, and a row here must have an anchor.
Levels: **L1** = a copy of a value in the card's output / a frozen verdict · **L2** = a number counted from the card's output (recounted by `check_claims.py`, a route independent of the build) · **L3** = a reading (whose reading; adoption is the human's) · **×** = not said.
Voice: nothing says what the model "knew", "hesitated over" or "chose wrongly"; a rank is the instrument's reading, not a map of the model's inside.

## A. The card (what was run)
| id | claim (as the figure prints it) | source (file · key) | level |
|---|---|---|---|
| K08 | "The card was run from a clean tree (not dirty)." | `data/synthetic_readout.json` · `provenance.dirty` = false | L1 |
| K09 | "A replay: no new forward pass." | `data/synthetic_readout.json` · `forward` = 0 | L1 |

## B. The rows (state 0, 1, 2)
| id | claim (as the figure prints it) | source (file · key) | level |
|---|---|---|---|
| K01 | "Row A: the key word is written at position 8." | `data/synthetic_readout.json` · `rows.A.key_pos` | L1 |
| K02 | "Row B: the key word is written at position 5." | `rows.B.key_pos` | L1 |
| K03 | "12 positions." | `rows.A.ranks` (length) | L1 |
| K04 | "Row A: the band-median rank at the key position is 9." | recount from `rows.A.ranks` (median over the band layers, ranks clipped at 1001) · `check_claims.py` `DERIVED["key_rank"]` | L2 |
| K05 | "Row B: the band-median rank at the key position is 54." | same recount for row B | L2 |
| K06 | "What the page carries for row A equals the recount." | `generated/pack.json` · `rows.A.keyRank` | L2 |
| K07 | "What the page carries for row B equals the recount." | `generated/pack.json` · `rows.B.keyRank` | L2 |

## C. What is not said (the ledger, state 3 — plain statements, never a small note)
- ×: the mechanism; identification with what the card's ruling left as "side by side only"; any quantitative judgment (a gap smaller than the error band); readings outside the instrument's valid domain; the side not read; "only" from one case; counting non-independent rows as independent.
- L3: "The nearer the band median is to rank 1 at the key position, the more the readout agrees with what was written" — whose reading: the author (execution layer); adoption: the human.

## D. Corrections between the brief and the data
(Write here every place where a value in a brief differed from the data: the data was used. Example: the brief said 390, the data is 389.5.)
