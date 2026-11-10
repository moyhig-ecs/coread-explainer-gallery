# INDEX (English) — the cards behind the moy-1 figure (station 2, received version v3.1)

This folder holds the frozen originals of the records the figure reads: the **cards** (a PREREG = the promise frozen before a run; a RESULT = the read-out written after it, with any later correction **appended at the end, never edited in**), the records that stand for the earlier probe cards, the two SCOPE notes the figure quotes for "what can be claimed", and the two briefs that ordered the received version. The originals are in Japanese and are kept byte for byte (`SOURCES.tsv`: house path, md5, bytes, and whether the file equals the house repository's HEAD when the bundle was cut — 61 / 61 "yes").

**This index is a guide, not a translation.** The one-line English descriptions are paraphrases of each card's file name and title, written by hand for this index; the station, grade and freeze-commit columns are copied from the figure's own pack (`generated/pack.json` → `after.cards`, which `pack_after.py` reads from the cards and checks against git); the md5 prefixes are from `SOURCES.tsv`. Nothing below re-reads or re-scores a card.

Terms left untranslated in the cards (先生, 主 session, 札, 腕, 帯, 関門, 計器, 判定, 記述, zebrashark, olmNNN, prfN) are glossed at the end.

## Table 1 — the cards of the part added after 10-28 (states 27–42 of the figure)

Columns: id · date (file name) · station on the figure's flow (state 27) · what the card asks (paraphrase) · grade the figure gives it (pack `after.cards[].grade`, from SCOPE 11-01 or the RESULT; Japanese word + English) · freeze commit (the commit that first added the PREREG; the figure checks it against git) · md5 PREREG / RESULT (first 8 hex).

| id | date | station | what the card asks (paraphrase) | grade in the figure | freeze | md5 PREREG / RESULT |
|---|---|---|---|---|---|---|
| olm76 | 10-30 | S1 | does the "commit" group rise in the window just before the answer's `{` (the reading left by the 10-28 ledger)? | 記述 description (Q1 ✗, Q3 ✗) | b7730f55 | 509fd5dc / 6ae78dbd |
| olm83 | 10-31 | S2 | inference space: is there look-ahead beyond what the lens and the words already give? | stopped at its gate (control ✗; the value was not read) | — (named from the RESULT header) | a00476d1 / e9c98660 |
| olm84 | 10-31 | S2 | the same look-ahead with a logistic probe and a pseudo-null control | 記述 (Q1 ✗) | 728cdca7 | d79b272c / f7854361 |
| olm85 | 10-31 | S2 | does the state predict the construction named in the next sentence? | 記述 (Q1 ✗) | b9a269d4 | 19525e90 / 667a5c1a |
| olm86 | 10-31 | S2 | long look-ahead (k up to 32) on fresh O-rows | 記述 (Q1 ✗; k = 8 noticed after looking) | 38896688 | 910c74fb / 2b27c2ac |
| olm88 | 10-31 | S2 | can the outcome be read from the first tokens? | stopped at its entry gate (✗) | — (named from the RESULT header) | 48bbfb87 / 805ca6c2 |
| olm89 | 10-31 | S2 | replication of the k = 8 look-ahead on new rows | 確かめた記述 checked description (Q1 ✓; the +0.05 line Q1b ✗) | 9c55b35a | 497c12f4 / c8c90afa |
| olm91 | 10-31 | S2 | outcome from the first tokens, 400 rows | 記述 (Q1 ✗) | 423602e6 | b91262e5 / 462f8250 |
| olm92 | 11-01 | S2 | does the k = 8 surplus survive a richer text baseline? | 確かめた記述 (the "remains" branch, layer 32 only) | f396c69a | cf02e030 / 77311501 |
| olm93 | 11-01 | S3 | does reference transfer from a code name to a demonstrative? | 記述 (Q1, a reading found false) · calibration | 6c38eb97 | 8f84718f / b2fe7cda |
| olm94 | 11-01 | S3 | variable binding of a reference on synthetic prompts | 判定 verdict (Q2 ✓) · 記述 (Q0, Q1, Q3) | ae474dc3 | 8b5acba0 / 5c175dfc |
| olm95 | 11-01 | S3 | intervention along a reference direction at the demonstrative | not read (gate C2 ✗) | 4502a4a6 | 4e78e072 / fffbd916 |
| olm97 | 11-01 | S3 | the same intervention with a logistic direction | 記述 (Q1 false, Q2) · calibration C2 0.971 | 5525976d | b1861e57 / f85c110f |
| olm98 | 11-01 | S3 | which attention heads read the referent at the final position? | 判定 (Q1 ✓, Q2 ✓) · 記述 (Q4, Q5) | 5a4eff07 | 7fe167d7 / 282738ce |
| olm101 | 11-01 | S3 | pointer or value at the final position (interchange / DAS)? | 記述 (no claim moved; Q3 "between" = a sign of illusion) | 9fbbc072 | 174fa342 / 4866a2cc |
| olm106 | 11-01 | S3 | single-position interchange (selector / control / demonstrative), early layers | 記述 (no claim moved) | 4ac2b73b | 19456c9c / fbb357c9 |
| olm108 | 11-01 | S3 | multi-position interchange: pointer → value across layers 12–32 | 判定 (Q1 ✓, Q3 present) | de6a4297 | 57c3532b / 55d60751 |
| olm112 | 11-02 | S4 | apex rows: status and a geometric proof | 判定 (frozen bands: Q1 false · Q2 does not follow · Q3 unchanged) | cb12da8d | 967bfa27 / aa4a6f37 |
| olm114 | 11-02 | S4 | a ladder of frontier-proof prefixes fed to OLMo | 判定 (Q1, Q2 continue; Q3 not read = gate ✗) · (B) forward = description | c82642a5 | d28170ec / 5cd69d68 |
| olm128 | 11-06 | S5 | does the cue (`\n` / `" "` / `\n\n`) change how often the answer starts with JSON, and does that explain the blocked bind? | 判定 (Q1 not kept · Q2 moves / reversed · Q3 not explained by the start; §3 is post-hoc description) | 2f1ab745 | 3aa4268a / 1a987d0d |

Notes: olm83 and olm88 have no read-out in the pack (their values were not read); the figure names them with date, commit and reason from the RESULT header and SCOPE 11-01 §0. The figure's count is "17 cards read and graded + 3 stopped at a gate (olm83, olm88, olm95)"; olm87 / olm90 are data-only cards and are not counted (and not in this folder). olm76's freeze: first frozen at b7730f55, re-frozen at d7fbbd43 one minute later (output conversion only, before the read); the run used d7fbbd43 (the maker's `NOTES.md` §3).

## Table 2 — the cards of the 10-28 part (states 0–26)

| id | date | what it is (paraphrase) | files here | md5 (first 8) |
|---|---|---|---|---|
| replication_config_frozen | 07-28 | the moy-1 replication on Claude (Fable 5 / Opus 5): the frozen config holds the open / blocked / selection-supply question texts that the later OLMo cards reuse | PREREG + RESULT `moy1_replication_20260728` | 4e8abc57 / d6c3a2e5 |
| behavior_screen | 07-28 | OLMo-3 32B behaviour screen on the same texts (the figure's "Think" column); a screening, not pre-registered — the record says so | RESULT `olmo3_behavior_screen` (no PREREG) | 44116718 |
| screen_bf16 | 07-29 | OLMo-3 32B base, bf16, no chat template, cue `\n`; a screening, not pre-registered — the record says so | RESULT `olmo3_base_bf16_screen` (no PREREG) | 8a95e51f |
| pc1 | 07-30 / 07-31 | does the label survive a change of cue (`" "` / `\n\n`)? | PREREG + RESULT `pc1_cue_invariance` | 166ba8da / c533dec5 |
| F5 | 08-01 | the F5 family of one-variable prompt edits (F5a-2 = reasoning first; F5b-1 = tangent-type wording) | ADJUDICATION `f5_v2_effective` (the record the figure names; no PREREG of that name) | 8a66a1a9 |
| cmt5 | 10-20 | fixing the first token (`Okay` / `{"` / none) and sampling the rest, two stages | PREREG + RESULT | ce85c32b / a470ac8e |
| cmt13 | 10-21 | the moment of the blocked bind inside the thinking text | PREREG + RESULT | f343e42d / d7502112 |
| olm59 | 10-28 | SAE trajectory of the groups around the construction mentions (the 120 rows of `data/ConstructGap/exp/olm59/rows/`) | PREREG + RESULT | e1a79f7a / c86891c3 |
| olm62 | 10-28 | does the "mid" rise go with a shift to formula text? | PREREG + RESULT | b4da6000 / 6b97e1c1 |
| prf4 | 11-02 | frontier control (Opus 5.5 / Fable 5.1 through `claude -p`): status and proof for moy-1 / moy-2; the figure uses Opus × moy-1 (8 / 8 chain) in state 33 | PREREG + RESULT | 2348740b / 9e70e01a |

Not in this folder: the cards olm4 / olm7 (on the figure's card tree, state 26, but their data are not read by the figure) and `moy_suite_report.json` (a data file without PREREG / RESULT; its date on the figure is git's last commit of the file, 06-14, recorded in `data/git_facts.json`).

## Table 3 — the other documents

| file | what it is | md5 (first 8) |
|---|---|---|
| `SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | what lines 1 / 2 can claim after olm76–81 (with the later additions, as of the cut) — the figure's "cannot say" for olm76 | fc086261 |
| `SCOPE_line1_inference_space_after_olm83_92_20261101.md` | what line 1 can claim after olm83–92 — the source of most grades in Table 1 | 6e469e59 |
| `BRIEF_v3_moy1_receipt_two_makers_20261106.md` | the brief for the two makers of v3 (base, transplants, audit fixes, "show the next") | eaaa01fa |
| `BRIEF_v3_1_moy1_received_version_one_maker_20261106.md` | the brief for the received version v3.1 (one maker; merge, rules, 14 audit fixes) | f179199e |
| `PROMPT_PROVENANCE.md` | the question texts and their md5 chain (open → blocked → cue → F5 edits), against the public ConstructGap v1.0.1 | generated by `make_prompt_provenance.py` |
| `public_constructgap_v1_0_1_literals.json` | literals of the public ConstructGap v1.0.1 read as text (no import, no run) | generated by the bundle builder |
| `SOURCES.tsv` | house path, md5, bytes, same-as-HEAD of the 61 originals | — |

## Reading glosses

- **先生** — the principal investigator (PI); the assistant's own address for its principal, left as written. **主 session** — the main Claude Code session that wrote the cards (sub-agents are named by role: maker, reader, auditor).
- **札** card · **腕** arm (one prompt condition) · **帯** band (the pre-registered verdict bands) · **関門** gate (a condition checked before a question is read) · **計器** instrument · **較正** calibration · **陽性統制 / 陰性統制** positive / negative control.
- **判定** verdict (a frozen band was read) · **確かめた記述** checked description (a description confirmed by a second card) · **記述** description (counted, not a verdict) · **言えない** cannot be said.
- **open / blocked** — the two question texts: blocked = open + a note that "concyclic" alone is insufficient (see `PROMPT_PROVENANCE.md`). Labels: **B-bind** — the answer names the circle with diameter O1O2 (the target); **B-attractor** — it names the salient wrong circle (He–Hi); **B-stuck-L1** — it stays at bare "concyclic".
- **zebrashark** — the lab's build host (an M2 Ultra) named in the cards' run notes.
- **olmNNN** — a card run on OLMo-3 32B; **prfN** — a frontier control run through `claude -p`; **cmtN** — the earlier "commit" cards of the same line.
- **L1 / L2 / L3** — a verbatim value / a recount from rows / a reading of the main session (adoption is the PI's).
