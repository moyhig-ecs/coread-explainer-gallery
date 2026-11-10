# INDEX (English) — the cards behind the moy-5 figure (station 3, received version v2.3.1)

This folder holds the frozen originals of the records the figure reads: the **cards** (a PREREG = the promise frozen before a run; a RESULT = the read-out written after it, with any later correction **appended at the end, never edited in**), the frozen question texts (SOURCE 10-14), the summary table the figure recounts (SUMMARY 10-16), the SCOPE note the figure uses for "what can be claimed" and for the grade rule, and the four briefs that ordered the received versions (v2 two makers · v2.1 one maker · v2.2 the cone overlay · v2.3 the cutting plane). The originals are in Japanese and are kept byte for byte (`SOURCES.tsv`: house path, md5, bytes, and whether the file equals the house repository's HEAD when the bundle was cut — 80 / 80 "yes").

**This index is a guide, not a translation.** The one-line English descriptions are paraphrases of each card's title line, written by hand for this index; the date, freeze commit and grade columns of Table 1 are copied from the figure's own pack (`generated/pack.json` → `post`, which `pack_data.py` reads from the RESULT heads and SCOPE 10-31 and asserts); the md5 prefixes are from `SOURCES.tsv`. Nothing below re-reads or re-scores a card.

Terms left untranslated in the cards (先生, 主 session, 実行層, 札, 腕, 帯, 関門, 計器, 判定, 記述, 床, zebrashark, olmNN, prfN) are glossed at the end.

## Table 1 — the 20 cards the house froze after the 10-28 figure (states 23–27 of the figure)

Columns: id · date · group on the figure (a = the frontier's road read by OLMo · b = the words before a cut · c = calibration of the instruments · d = the thinking summaries) · what the card asks (paraphrase) · grade the figure gives it (rule (i) = the tier SCOPE 10-31 §1 / §2 names; rule (ii) = SCOPE's criteria applied to the card's RESULT; see `JUDGING_SUMMARY.md` §3) · freeze commit (named in the head of its RESULT; the pack asserts it) · md5 PREREG / RESULT (first 8 hex).

| id | date | grp | what the card asks (paraphrase) | grade (rule) | freeze | md5 PREREG / RESULT |
|---|---|---|---|---|---|---|
| olm60 | 10-28 | a | can a public SAE (layer 32) reconstruct OLMo-3 32B base's residual while it reads Opus 5.5 / Fable 5.1's moy-5 text? | 関門 stopped at a gate (ii; C1 FVE 0.343 < 0.40) | 0e3edd75 | 51b0cd17 / 3bee9fca |
| olm61 | 10-28 | a | given the frontier text up to the key sentence, does OLMo continue the floor road or the apex road? | 判定 verdict (ii) | 79076ae6 | 27987422 / 097c2e12 |
| olm64 | 10-28 | a | does reading the apex (mean-proportional) sentence move OLMo's state along olm4's "answer and stop" direction? | 判定 (ii) | b0c690fa | 9d661000 / 6421ba1b |
| olm67 | 10-29 | a | the same direction on all cut sentences (361) — and on the floor sentences; the language space | 判定 (i) | 4729c23e | e835656f / 19efa3aa |
| olm68 | 10-29 | b | the time profile of the lean toward the cut words before a cut sentence, with false events as control | 判定 (i) | cd4a7ae0 | f0f994a8 / 9baf28e5 |
| olm69 | 10-29 | b | do the arms shown Lemma XIV use different words in their cut sentences? | 記述 description (i) | 3f138f1e | d448b622 / d947da58 |
| olm70 | 10-29 | b | calibrate an instrument on the model's own words, then retry | 関門 (ii) | f4e56ab0 | 166a61cf / ecd221cf |
| olm71 | 10-29 | b | opening-word and body-word instruments, by group | 関門 (ii) | 417dff60 | 674df1db / 82548685 |
| olm72 | 10-29 | b | body words without the "not after the sentence" condition | 関門 (ii) | 842ecabf | e56a58d0 / 117415d5 |
| olm73 | 10-29 | b | in the universe of rows that write the cut in words, is there a run-up in the lemma arms? | 言えない cannot say (i) | 30b429fe | 0bfe3942 / bf8ed6d9 |
| olm74 | 10-29 | b | lemma arms vs the other cut rows: is the run-up weaker? | 判定 (i) | ec45e01c | fc8cdc9f / 47a32d60 |
| olm77 | 10-30 | b | cut vs floor inside one card | 記述 (i) | 3fdfeb93 | b2188d43 / 18304b37 |
| olm78 | 10-30 | b | is the within-row run-up word order or word accumulation? (layer 48 and the final layer) | 判定 (i) | 8b5673be | d4e924ca / f081f731 |
| olm79 | 10-30 | b | single-word lens: concept words vs the model's own words | 言えない (i) | 1ad08f57 | 243bcd56 / 4da583b4 |
| olm81 | 10-31 | b | cut sentences written only as formulas: is there a run-up toward the concept set? | 判定 (i) | 6671fe53 | cc6bab55 / 08a9cfad |
| olm82 | 10-31 | b | does the joint rise and fall of the word sets go with the spread of the next-token distribution? | 判定 (ii) | 61e7917d | e5ce3570 / 0c77f6be |
| olm63 | 10-28 | c | SAE calibration: notation, context, JSON, position — can any reach the FVE gate? | 判定 (ii) | 842aefce | 33b7d044 / d6b093b4 |
| olm80 | 10-31 | c | does the layer-32 change separate cut from floor beyond the words? | 記述 (i) | 32e1b4ad | 4f47f3ab / 859ab6ff |
| thk1 | 10-30 | d | pilot: ask for the thinking summary on Q2 (stopped by its stop rule after one row per model) | 関門 (ii) | f2ccf1be | 528b2f57 / 884b2cd6 |
| thk2 | 10-30 | d | pilot: do the thinking summaries come back, how long are they, and do they carry the cut? | 記述 (i) | 85464c61 | f24fa652 / 8bc45b6a |

Tally (the figure's state 23): verdict 9 · description 4 · calibration 0 · cannot say 2 · stopped at a gate 5 = 20 (rule (i) 11 · rule (ii) 9).

## Table 2 — the cards of the 10-28 part (states 0–22)

| id | date | what it is (paraphrase) | md5 PREREG / RESULT |
|---|---|---|---|
| essay4 | 10-14 | ask after an essay is read — three items (moy-1 / moy-2 / moy-5) × four Claude 5.5 tiers, n 20; the moy-5 arms A / K / E-* (file names `…essay_reading_three_items…`; the id `essay4` is in the title) | 864cd933 / bfd752a5 |
| b5bp | 10-14 | one of six afternoon cards (file `…pm_cards_eprem1_gname2_b5bp_…`): the β′ sentence ("explain WHY … a relation among lengths …") added to the question | 1e0ff2e6 / 5999a7d9 |
| moy5c | 10-15 | the b5bp question alone at effort max (a control for moy5e) | cb1a2956 / 8d2e0b75 |
| rte1 | 10-15 | separate route (API / `claude -p`) and effort, question only, Opus 5.5 / Fable 5.1 | e9d3ccdc / c25e6a88 |
| arg5 | 10-16 | Gemini 4 Argon, five arms × n 20, thinking high | b02a0789 / 2095956e |
| arg5d | 10-16 | Gemini 4 Argon, K and Bbp, thinking left at the default | 8a620243 / c81a1b26 |
| neq1 | 10-19 | the essay with a note "equal lengths are not enough" — Opus 5.5 pre-check (verdict NONE) | e2885181 / 8461aa3a |
| neq2f | 10-19 | Principia Lemma XIV (name / text) with Fable 5.1 xhigh — the name alone pulled the cut | a5916064 / 4aceb4d1 |
| neq3 | 10-19 | the question's point set (Q1 / Q2) × Lemma XIV (name / text), Opus / Fable xhigh | 5b00269b / d902b88e |
| neq6 | 10-19 | effort dose on Q2 (medium → max), Opus / Fable | 25283fb4 / 361da2c1 |
| prf1 | 10-21 | ask for a proof (`claude -p`): the focus-directrix road vs the lattice; P5K gives the mean proportional | 83863c74 / d26974c9 |
| prf2 | 10-21 | block the focus-directrix road (its frozen main predicate failed by an instrument defect) | b85437e1 / f7cadb9f |
| prf3 | 10-21 | confirm on new samples: blocked → the lattice bundle (LAT_SYM) | af3a07fd / 3779aaad |
| mnw1 | 10-22 | Menaechmus / Newton: roles × proportion form × cone explanation, Opus / Fable xhigh (the RESULT covers mnw1b too) | 68fcb585 / 68c5ec34 |
| mnw1b | 10-22 | continuation of mnw1 after a usage limit | d83cad43 / — (no RESULT of its own: reported in mnw1's RESULT) |
| olm1 | 10-22 | mnw1's arms on OLMo-3 32B base (MLX bf16) — stopped at the Stage-0 screen | b4f50f87 / fa142c17 |
| olm3 | 10-22 | OLMo-3 32B Think on the moy-5 screen (bf16 MLX and ollama Q4) | 05296745 / a0cefc81 |

## Table 3 — the other records

| file | what | md5 (first 8) |
|---|---|---|
| `SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` | the frozen question texts (moy-5 = block `parabola_section`, 1921 characters, md5 ee39ba02…; the K hint) | 574ea5c5 |
| `SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md` | the cut across arms, effort, route and Argon (its data table is recounted by the figure) | 39b74e9a |
| `SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | what can be claimed after olm76–81 (lines 1 and 2), with the later additions; the grade rule (i) reads its §1 / §2 | fc086261 |
| `BRIEF_v2_moy5_receipt_two_makers_20261106.md` | the brief of the received version v2 (two makers) | 801f1e21 |
| `BRIEF_v2_1_moy5_received_version_one_maker_20261107.md` | the brief of v2.1 (one maker; the grade rule; the audit fixes) | 89486bc5 |
| `BRIEF_v2_2_moy5_board_cone_overlay_20261107.md` | the brief of v2.2 (the cone overlay on the board) | 48b3b577 |
| `BRIEF_v2_3_moy5_cutting_plane_FVD_20261109.md` | the brief of v2.3 (the cutting plane: the plane through the line FVD = line j, perpendicular to the board, with its parabola and directrix — drawing, not data) | 768ec87e |
| `PROMPT_PROVENANCE.md` | the question texts and their md5 (generated by `make_prompt_provenance.py`) | — |
| `public_constructgap_v1_0_1_text.json` | the text of the public ConstructGap v1.0.1 `prompts.py` / `probe_registry.py` (read as text) | — |

Not found (not made): a RESULT file of `mnw1b` (its result is in mnw1's RESULT). **v2.3.1 has no brief**: its request is the 「発」 (origin) line at the head of the maker's record `NOTES_v231.md` (the requester's words quoted there: the growing plane may be harder to read → fix the plane and the parabola at the frozen P_x; only the lifted point moves). Compared with the v2.2 bundle's cards: one file added (the v2.3 brief); the other 79 are the same bytes. Records the figure reads that are not cards in this sense (the readers' replies of the station-3 reading) are house records and are not here.

## What the cards say they do not claim (summary)

The cards' own "not claimed" sections are in Japanese; in short, as the figure's ledger (states 28–30) repeats: no claim about what a model "holds inside" or lacks (an answer field without the cut is not evidence of absence); the SAE / direction / lens readings are descriptions of OLMo-3 32B base reading the frontier's text, not of the frontier models; the "33–64 tokens before" phrase of olm68 is not used outward (SCOPE 10-31 correction); a run-up "of words" (olm78) is a reading (L3); grades are the SCOPE's tiers or the RESULT's frozen predicates, not the maker's.

## Glossary

- **先生** (*sensei*, "teacher") — the principal investigator (PI); how the assistant that wrote the cards addresses its principal. Left as written in the cards and in the page text (see README).
- **主 session** — the main Claude Code session that wrote the cards; **実行層** — "the execution layer" = the same assistant as runner.
- **札** card · **腕** arm · **帯** band · **関門** gate · **計器** instrument · **判定** verdict · **記述** description · **較正** calibration · **言えない** cannot say · **床** floor (the frozen invariant EJ = KP_y) · **cut** = the mean-proportional relation at the apex.
- **zebrashark** — the lab's build host (an M2 Ultra) named in the cards' run notes.
- **olmNN** — a card on OLMo-3 (32B base unless named); **prfN** — a proof card run with `claude -p`.
