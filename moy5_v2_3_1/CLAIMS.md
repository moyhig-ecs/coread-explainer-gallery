# CLAIMS — every number the figure prints, where it comes from (entry_v2_1_received · moy-5 · v1 2026-10-28 → v2 2026-11-06 → v2.1 2026-11-07)

v2.1: a fourth file **[CLAIMS_v21.md](CLAIMS_v21.md)** holds the rows of what v2.1 moved, decided and fixed (92 anchors · the grade of each card after 10-28 recomputed from SCOPE 10-31 / its RESULT · written by `make_anchors_v21.py`). The rows K250–K269 of CLAIMS_after.md carry the grade of the requester's rule (G-26). All four files < 60 KB.

v2: the ledger is split in three files so that each is < 60 KB (a cold reader reads each within its Read limit): **CLAIMS.md** (this file: v1's 145 rows with the state column renumbered for v2 + the rows of what v2 moved from entry P and of the four disagreements) · **[CLAIMS_cells.md](CLAIMS_cells.md)** (audit G-22: every strip's printed numbers, one row per strip) · **[CLAIMS_after.md](CLAIMS_after.md)** (chapters J / K / L-after: the cards frozen after 10-28, the next questions, SCOPE 10-31). `check_claims.py` reads all three.

Each row = one anchor of `claims_anchors.json` (`check_claims.py` looks at the place itself, from the raw jsonl / text, without the pack). The figure's sentences are functions of these values (`i18n.js` reads `DATA`; nothing is typed).
Levels: **L1** = a copy of a value / a frozen text · **L2** = a number counted from the frozen output's fields (recounted here; the reader v2 is NOT run again) · **L3** = a reading (in the ledger, with whose reading; adoption is the human's) · **×** = not said.
Counting rule (one place): a *cell* = one model × one arm of one card; rows with `raw` only (mnw1 + mnw1b = only the rows that have `raw`; OLMo = every row drawn, empty ones kept). `answer field` = `cut_in_conjecture`; `whole` = `bind`; `floor` = `closure` (prf: `floor`).

| id | claim (value as the figure prints it) | source (file · key) | level | state |
|---|---|---|---|---|
| K001 | V1 essay4 A opus-5-5 bind = **0** | `results_essay4_moy5_20261014_claude-opus-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-opus-5-5_r.jsonl` · model = claude-opus-5-5 · arm = A · field `bind` | L2 | 5, 28, 29 |
| K002 | V1 essay4 A fable-5-1 bind = **0** | `results_essay4_moy5_20261014_claude-fable-5-1_a.jsonl` + `results_essay4_moy5_20261014_claude-fable-5-1_r.jsonl` · model = claude-fable-5-1 · arm = A · field `bind` | L2 | 5, 28, 29 |
| K003 | V1 essay4 A sonnet-5-5 bind = **0** | `results_essay4_moy5_20261014_claude-sonnet-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-sonnet-5-5_r.jsonl` · model = claude-sonnet-5-5 · arm = A · field `bind` | L2 | 5, 28, 29 |
| K004 | V1 essay4 A haiku-5-5 bind = **0** | `results_essay4_moy5_20261014_claude-haiku-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-haiku-5-5_r.jsonl` · model = claude-haiku-5-5 · arm = A · field `bind` | L2 | 5, 28, 29 |
| K005 | V1 essay4 A opus-5-5 floor (closure) = **20** | `results_essay4_moy5_20261014_claude-opus-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-opus-5-5_r.jsonl` · model = claude-opus-5-5 · arm = A · field `closure` | L2 | 5, 28, 29 |
| K006 | V1 essay4 A fable-5-1 floor (closure) = **20** | `results_essay4_moy5_20261014_claude-fable-5-1_a.jsonl` + `results_essay4_moy5_20261014_claude-fable-5-1_r.jsonl` · model = claude-fable-5-1 · arm = A · field `closure` | L2 | 5, 28, 29 |
| K007 | V1 essay4 A sonnet-5-5 floor (closure) = **20** | `results_essay4_moy5_20261014_claude-sonnet-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-sonnet-5-5_r.jsonl` · model = claude-sonnet-5-5 · arm = A · field `closure` | L2 | 5, 28, 29 |
| K008 | V1 essay4 A haiku-5-5 floor (closure) = **19** | `results_essay4_moy5_20261014_claude-haiku-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-haiku-5-5_r.jsonl` · model = claude-haiku-5-5 · arm = A · field `closure` | L2 | 5, 28, 29 |
| K009 | V1 essay4 A haiku n (_a 16 + _r 3) = **19** | `results_essay4_moy5_20261014_claude-haiku-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-haiku-5-5_r.jsonl` · model = claude-haiku-5-5 · arm = A · rows | L2 | 5, 28, 29 |
| K010 | V2 b5bp Bbp opus-5-5 bind = **6** | `results_b5bp_20261014_claude-opus-5-5_a.jsonl` · model = claude-opus-5-5 · arm = Bbp · field `bind` | L2 | 12, 14, 28 |
| K011 | V2 b5bp Bbp sonnet-5-5 bind = **2** | `results_b5bp_20261014_claude-sonnet-5-5_a.jsonl` · model = claude-sonnet-5-5 · arm = Bbp · field `bind` | L2 | 12, 14, 28 |
| K012 | V2 b5bp Bbp fable-5-1 bind = **0** | `results_b5bp_20261014_claude-fable-5-1_a.jsonl` · model = claude-fable-5-1 · arm = Bbp · field `bind` | L2 | 12, 14, 28 |
| K013 | V2 b5bp Bbp opus answer field = **0** | `results_b5bp_20261014_claude-opus-5-5_a.jsonl` · model = claude-opus-5-5 · arm = Bbp · field `cut_in_conjecture` | L2 | 12, 14, 28 |
| K014 | V2 arg5 Bbp bind = **20** | `results_arg5_20261016_gemini-4-argon_a.jsonl` · model = gemini-4-argon · arm = Bbp · field `bind` | L2 | 12, 14, 28 |
| K015 | V2 arg5d Bbp bind = **8** | `results_arg5d_20261016_gemini-4-argon_a.jsonl` · model = gemini-4-argon · arm = Bbp · field `bind` | L2 | 12, 14, 28 |
| K016 | V2 arg5 K bind = **20** | `results_arg5_20261016_gemini-4-argon_a.jsonl` · model = gemini-4-argon · arm = K · field `bind` | L2 | 12, 14, 28 |
| K017 | V2 arg5d K bind = **20** | `results_arg5d_20261016_gemini-4-argon_a.jsonl` · model = gemini-4-argon · arm = K · field `bind` | L2 | 12, 14, 28 |
| K018 | V3 moy5c P-none claude-opus-5-5 bind = **10** | `results_moy5c_20261015.jsonl` · model = claude-opus-5-5 · arm = P-none · field `bind` | L2 | 13 |
| K019 | V3 moy5c P-none claude-fable-5-1 bind = **6** | `results_moy5c_20261015.jsonl` · model = claude-fable-5-1 · arm = P-none · field `bind` | L2 | 13 |
| K020 | V4 neq3 opus A answer field = **0** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K021 | V4 neq3 opus A/Q2 answer field = **7** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2 · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K022 | V4 neq3 opus L-name/Q2 answer field = **20** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = L-name/Q2 · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K023 | V4 neq3 opus L-text/Q2 answer field = **20** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = L-text/Q2 · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K024 | V4 neq3 opus L-name answer field = **0** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = L-name · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K025 | V4 neq3 opus L-text answer field = **0** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = L-text · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K026 | V4 neq3 fable A/Q2 answer field = **20** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2 · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K027 | V4 neq2f fable A (Q1) answer field = **0** | `results_neq2f_moy5_20261019.jsonl` · model = claude-fable-5-1 · arm = A · field `cut_in_conjecture` | L2 | 6, 8, 9, 28 |
| K028 | V4 neq3 opus A/Q2 parabola_in_conjecture = **20** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2 · field `parabola_in_conjecture` | L2 | 6, 8, 9, 28 |
| K029 | V5 neq6 opus-5-5 A/Q2@medium answer field = **0** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@medium · field `cut_in_conjecture` | L2 | 10, 28, 29 |
| K030 | V5 neq6 opus-5-5 A/Q2@medium thinking median = **1038.5** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@medium · median of `thinking` | L2 | 10, 28, 29 |
| K031 | V5 neq6 opus-5-5 A/Q2@high answer field = **1** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@high · field `cut_in_conjecture` | L2 | 10, 28, 29 |
| K032 | V5 neq6 opus-5-5 A/Q2@high thinking median = **1371.0** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@high · median of `thinking` | L2 | 10, 28, 29 |
| K033 | V5 neq6 opus-5-5 A/Q2@max answer field = **19** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@max · field `cut_in_conjecture` | L2 | 10, 28, 29 |
| K034 | V5 neq6 opus-5-5 A/Q2@max thinking median = **8506.5** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@max · median of `thinking` | L2 | 10, 28, 29 |
| K035 | V5 neq6 fable-5-1 A/Q2@medium answer field = **15** | `results_neq6_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2@medium · field `cut_in_conjecture` | L2 | 10, 28, 29 |
| K036 | V5 neq6 fable-5-1 A/Q2@medium thinking median = **2365.0** | `results_neq6_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2@medium · median of `thinking` | L2 | 10, 28, 29 |
| K037 | V5 neq6 fable-5-1 A/Q2@high answer field = **17** | `results_neq6_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2@high · field `cut_in_conjecture` | L2 | 10, 28, 29 |
| K038 | V5 neq6 fable-5-1 A/Q2@high thinking median = **2722.0** | `results_neq6_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2@high · median of `thinking` | L2 | 10, 28, 29 |
| K039 | V5 neq6 fable-5-1 A/Q2@max answer field = **20** | `results_neq6_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2@max · field `cut_in_conjecture` | L2 | 10, 28, 29 |
| K040 | V5 neq6 fable-5-1 A/Q2@max thinking median = **7858.0** | `results_neq6_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2@max · median of `thinking` | L2 | 10, 28, 29 |
| K041 | neq3 opus A/Q2 (= xhigh) thinking median from usage = **1734.5** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2 · median of `usage.output_tokens_details.thinking_tokens` | L2 |  |
| K042 | neq3 fable A/Q2 (= xhigh) thinking median from usage = **4144.0** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2 · median of `usage.output_tokens_details.thinking_tokens` | L2 |  |
| K043 | V6 prf1 claude-opus-5-5 P5 route5 = CHAIN = **1** | `results_prf1_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · route5 = CHAIN | L2 | 15–17, 29 |
| K044 | V6 prf1 claude-opus-5-5 P5 route5 = END-only = **8** | `results_prf1_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · route5 = END-only | L2 | 15–17, 29 |
| K045 | V6 prf1 claude-opus-5-5 P5 route5 = LAT-only = **1** | `results_prf1_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · route5 = LAT-only | L2 | 15–17, 29 |
| K046 | V6 prf1 claude-fable-5-1 P5 route5 = END-only = **6** | `results_prf1_20261021.jsonl` · model = claude-fable-5-1 · arm = P5 · route5 = END-only | L2 | 15–17, 29 |
| K047 | V6 prf1 claude-fable-5-1 P5 route5 = none = **4** | `results_prf1_20261021.jsonl` · model = claude-fable-5-1 · arm = P5 · route5 = none | L2 | 15–17, 29 |
| K048 | V6 prf1 claude-opus-5-5 P5K route5 = CHAIN = **10** | `results_prf1_20261021.jsonl` · model = claude-opus-5-5 · arm = P5K · route5 = CHAIN | L2 | 15–17, 29 |
| K049 | V6 prf1 claude-fable-5-1 P5K route5 = CHAIN = **9** | `results_prf1_20261021.jsonl` · model = claude-fable-5-1 · arm = P5K · route5 = CHAIN | L2 | 15–17, 29 |
| K050 | V6 prf1 claude-fable-5-1 P5K route5 = LAT-only = **1** | `results_prf1_20261021.jsonl` · model = claude-fable-5-1 · arm = P5K · route5 = LAT-only | L2 | 15–17, 29 |
| K051 | V7 prf3 claude-opus-5-5 P5 lat_sym = **0** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · field `lat_sym` | L2 | 1, 18, 28, 29 |
| K052 | V7 prf3 claude-opus-5-5 P5B lat_sym = **10** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5B · field `lat_sym` | L2 | 1, 18, 28, 29 |
| K053 | V7 prf3 claude-opus-5-5 P5B malformed = **1** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5B · field `malformed` | L2 | 1, 18, 28, 29 |
| K054 | V7 prf3 claude-fable-5-1 P5 lat_sym = **0** | `results_prf3_20261021.jsonl` · model = claude-fable-5-1 · arm = P5 · field `lat_sym` | L2 | 1, 18, 28, 29 |
| K055 | V7 prf3 claude-fable-5-1 P5 malformed = **5** | `results_prf3_20261021.jsonl` · model = claude-fable-5-1 · arm = P5 · field `malformed` | L2 | 1, 18, 28, 29 |
| K056 | V7 prf3 claude-fable-5-1 P5B lat_sym = **4** | `results_prf3_20261021.jsonl` · model = claude-fable-5-1 · arm = P5B · field `lat_sym` | L2 | 1, 18, 28, 29 |
| K057 | V7 prf3 claude-fable-5-1 P5B malformed = **2** | `results_prf3_20261021.jsonl` · model = claude-fable-5-1 · arm = P5B · field `malformed` | L2 | 1, 18, 28, 29 |
| K058 | V7 prf3 claude-opus-5-5 P5 fd_use = **10** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · field `fd_use` | L2 | 1, 18, 28, 29 |
| K059 | V7 prf3 claude-opus-5-5 P5B fd_use = **0** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5B · field `fd_use` | L2 | 1, 18, 28, 29 |
| K060 | V7 prf3 claude-opus-5-5 P5 floor = **10** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · field `floor` | L2 | 1, 18, 28, 29 |
| K061 | V7 prf3 claude-opus-5-5 P5B floor = **10** | `results_prf3_20261021.jsonl` · model = claude-opus-5-5 · arm = P5B · field `floor` | L2 | 1, 18, 28, 29 |
| K062 | V8 mnw1+mnw1b claude-opus-5-5 conf/Q1f bind = **19** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1f · field `bind` | L2 | 19–21, 28, 29 |
| K063 | V8 mnw1+mnw1b claude-opus-5-5 conf/Q1f cut_in_conjecture = **19** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1f · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K064 | V8 mnw1+mnw1b claude-opus-5-5 conf/Q1f form_focal = **19** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1f · field `form_focal` | L2 | 19–21, 28, 29 |
| K065 | V8 mnw1+mnw1b claude-opus-5-5 conf/Q1f form_vertex = **0** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1f · field `form_vertex` | L2 | 19–21, 28, 29 |
| K066 | V8 mnw1+mnw1b claude-opus-5-5 none/Q1f bind = **1** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = none/Q1f · field `bind` | L2 | 19–21, 28, 29 |
| K067 | V8 mnw1+mnw1b claude-opus-5-5 none/Q1f cut_in_conjecture = **1** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = none/Q1f · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K068 | V8 mnw1+mnw1b claude-opus-5-5 none/Q1f form_vertex = **1** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = none/Q1f · field `form_vertex` | L2 | 19–21, 28, 29 |
| K069 | V8 mnw1+mnw1b claude-opus-5-5 cone/Q1 bind = **0** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = cone/Q1 · field `bind` | L2 | 19–21, 28, 29 |
| K070 | V8 mnw1+mnw1b claude-opus-5-5 conf/Q1 cut_in_conjecture = **0** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1 · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K071 | V8 mnw1+mnw1b claude-opus-5-5 conf/Q1 bind = **0** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1 · field `bind` | L2 | 19–21, 28, 29 |
| K072 | V8 mnw1+mnw1b claude-opus-5-5 none/Q1 bind = **0** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = none/Q1 · field `bind` | L2 | 19–21, 28, 29 |
| K073 | V8 mnw1+mnw1b claude-fable-5-1 conf/Q1f bind = **17** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = conf/Q1f · field `bind` | L2 | 19–21, 28, 29 |
| K074 | V8 mnw1+mnw1b claude-fable-5-1 conf/Q1f cut_in_conjecture = **13** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = conf/Q1f · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K075 | V8 mnw1+mnw1b claude-fable-5-1 conf/Q1f form_focal = **17** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = conf/Q1f · field `form_focal` | L2 | 19–21, 28, 29 |
| K076 | V8 mnw1+mnw1b claude-fable-5-1 cone/Q1 bind = **5** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1 · field `bind` | L2 | 19–21, 28, 29 |
| K077 | V8 mnw1+mnw1b claude-fable-5-1 cone/Q1 cut_in_conjecture = **0** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1 · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K078 | V8 mnw1+mnw1b claude-fable-5-1 cone/Q1 form_vertex = **5** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1 · field `form_vertex` | L2 | 19–21, 28, 29 |
| K079 | V8 mnw1+mnw1b claude-fable-5-1 cone/Q1f bind = **9** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1f · field `bind` | L2 | 19–21, 28, 29 |
| K080 | V8 mnw1+mnw1b claude-fable-5-1 cone/Q1f cut_in_conjecture = **6** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1f · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K081 | V8 mnw1+mnw1b claude-fable-5-1 none/Q1f cut_in_conjecture = **3** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = none/Q1f · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K082 | V8 mnw1+mnw1b claude-fable-5-1 conf/Q1 cut_in_conjecture = **0** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = conf/Q1 · field `cut_in_conjecture` | L2 | 19–21, 28, 29 |
| K083 | V8 mnw1+mnw1b claude-fable-5-1 conf/Q1 bind = **1** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = conf/Q1 · field `bind` | L2 | 19–21, 28, 29 |
| K084 | V8 mnw1+mnw1b opus conf/Q1f n (raw rows) = **20** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = conf/Q1f · rows | L2 | 19–21, 28, 29 |
| K085 | V8 mnw1+mnw1b fable cone/Q1f n (raw rows; INCOMPLETE) = **11** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1f · rows | L2 | 19–21, 28, 29 |
| K086 | V9 olm1 base natural none/Q1 floor (denominator = rows drawn) = **0** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · arm = none/Q1 · variant = natural · field `closure` · all rows drawn | L2 | 22, 29 |
| K087 | V9 olm1 base natural none/Q1 rows drawn = **20** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · arm = none/Q1 · variant = natural · rows · all rows drawn | L2 | 22, 29 |
| K088 | V9 olm1 base natural none/Q1 answer field = **0** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · arm = none/Q1 · variant = natural · field `cut_in_conjecture` · all rows drawn | L2 | 22, 29 |
| K089 | V9 olm1 base think none/Q1 floor (denominator = rows drawn) = **2** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · arm = none/Q1 · variant = think · field `closure` · all rows drawn | L2 | 22, 29 |
| K090 | V9 olm1 base think none/Q1 rows drawn = **20** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · arm = none/Q1 · variant = think · rows · all rows drawn | L2 | 22, 29 |
| K091 | V9 olm1 base think none/Q1 answer field = **0** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · arm = none/Q1 · variant = think · field `cut_in_conjecture` · all rows drawn | L2 | 22, 29 |
| K092 | V9 olm3 Think none/Q1 floor = **5** | `results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl` · arm = none/Q1 · field `closure` · all rows drawn | L2 | 22, 29 |
| K093 | V9 olm3 Think none/Q1 answer field = **0** | `results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl` · arm = none/Q1 · field `cut_in_conjecture` · all rows drawn | L2 | 22, 29 |
| K094 | F1 rte1 api claude-opus-5-5 bind (= SUMMARY §10) = **6** | `results_rte1_20261015_api_max.jsonl` · model = claude-opus-5-5 · arm = Bbp · field `bind` | L2 | 13 |
| K095 | F1 rte1 api claude-fable-5-1 bind (= SUMMARY §10) = **2** | `results_rte1_20261015_api_max.jsonl` · model = claude-fable-5-1 · arm = Bbp · field `bind` | L2 | 13 |
| K096 | F1 rte1 cc claude-opus-5-5 bind (= SUMMARY §10) = **2** | `results_rte1_20261015_cc_high.jsonl` · model = claude-opus-5-5 · arm = P-none · field `bind` | L2 | 13 |
| K097 | F1 rte1 cc claude-fable-5-1 bind (= SUMMARY §10) = **3** | `results_rte1_20261015_cc_high.jsonl` · model = claude-fable-5-1 · arm = P-none · field `bind` | L2 | 13 |
| K098 | F1 rte1 api_max fable answer field (the only answer-field cut of the four) = **1** | `results_rte1_20261015_api_max.jsonl` · model = claude-fable-5-1 · arm = Bbp · field `cut_in_conjecture` | L2 | 13 |
| K099 | C0 essay4 K opus bind (positive control) = **20** | `results_essay4_moy5_20261014_claude-opus-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-opus-5-5_r.jsonl` · model = claude-opus-5-5 · arm = K · field `bind` | L2 | 5 |
| K100 | C0 essay4 K haiku answer field = **15** | `results_essay4_moy5_20261014_claude-haiku-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-haiku-5-5_r.jsonl` · model = claude-haiku-5-5 · arm = K · field `cut_in_conjecture` | L2 | 5 |
| K101 | C1 neq2f fable L-name bind (reason field) = **7** | `results_neq2f_moy5_20261019.jsonl` · model = claude-fable-5-1 · arm = L-name · field `bind` | L2 | 6 |
| K102 | D2 neq3 opus K/Q2 answer field = **10** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = K/Q2 · field `cut_in_conjecture` | L2 | 9 |
| K103 | D2 neq3 fable K/Q2 answer field = **10** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = K/Q2 · field `cut_in_conjecture` | L2 | 9 |
| K104 | C1 SUMMARY §5-1 '1 / 717' recounted from the frozen table (10 API high arms without K, K@U, Bbp, E-full+Bbp) = **0 / 717 (answer field) · 1 / 717 (whole) · 10 arms** | check_claims.py summary_sum | L2 | 6 |
| K105 | A0 drawing control: K, P_y, J recomputed from the frozen coordinates = **0.001** | check_claims.py construct | L2 | 0, 7 |
| K106 | scene P5 r0: perpendicular bisector of FK, : «perpendicular bisector of FK, so P_yF = P_yK» | `results_prf3_20261021.jsonl` · rep 0 · raw | L1 | 1, 28 |
| K107 | scene P5B r0: Parabola, derived without P_yF: «Parabola, derived without P_yF = P_yK» | `results_prf3_20261021.jsonl` · rep 0 · raw | L1 | 1, 28 |
| K108 | scene P5B r0: VP_x² = VD·VH = FV·VH: «VP_x² = VD·VH = FV·VH» | `results_prf3_20261021.jsonl` · rep 0 · raw | L1 | 1, 28 |
| K109 | scene P5B r0: HP_y² = 4·VP_x² = 4·FV·VH: «HP_y² = 4·VP_x² = 4·FV·VH» | `results_prf3_20261021.jsonl` · rep 0 · raw | L1 | 1, 28 |
| K110 | scene A/Q2@medium r0: P_y lies on the parabola with : «P_y lies on the parabola with focus F and vertex V» | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · rep 0 · raw | L1 | 11 |
| K111 | scene A/Q2@max r0: FP_x^2 = FV · FP_y: «FP_x^2 = FV · FP_y» | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · rep 0 · raw | L1 | 11 |
| K112 | scene P5 r0: P_y is equidistant from the fi: «P_y is equidistant from the fixed point F and the fixed line e» | `results_prf1_20261021.jsonl` · rep 0 · raw | L1 | 15 |
| K113 | scene P5 r2: VF·VH = VP_x²: «VF·VH = VP_x²» | `results_prf1_20261021.jsonl` · rep 2 · raw | L1 | 16 |
| K114 | scene none/Q1f r0: EJ : KP_y = KP_y : EJ: «EJ : KP_y = KP_y : EJ» | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` · rep 0 · raw | L1 | 19 |
| K115 | scene none/Q1f r12: VE : VP_x = VP_x : VJ: «VE : VP_x = VP_x : VJ» | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` · rep 12 · raw | L1 | 19 |
| K116 | scene conf/Q1f r0: Newton's Lemma XIV: «Newton's Lemma XIV» | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` · rep 0 · raw | L1 | 20 |
| K117 | scene cone/Q1 r6: Menaechmus symptoma |P_yH|^2 =: «Menaechmus symptoma |P_yH|^2 = 4·VF·VH» | `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · rep 6 · raw | L1 | 21 |
| K118 | F2 Argon thinking ratio: «Bbp 3.8〜8.2» | `conversations/2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md` | L1 |  |
| K119 | F2 relations per answer: «Bbp 36 対 11〜19.5» | `conversations/2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md` | L1 |  |
| K120 | C1 the SUMMARY's own words: «1 / 717» | `conversations/2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md` | L1 | 6 |
| K121 | every screen: the reader's range: «読み取り器 v2 は線分の関係しか読まない» | `conversations/2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md` | L1 |  |
| K122 | neq2f effort (the rows carry no effort field): «Fable 5.1 xhigh» | `conversations/2026-10-19/RESULT_neq2f_moy5_principia_lemma14_fable51_xhigh_20261019.md` | L1 |  |
| K123 | C1 neq1 verdict: «判定 NONE» | `conversations/2026-10-19/RESULT_neq1_moy5_essay_not_equal_length_note_20261019.md` | L1 | 6 |
| K124 | H2 INCOMPLETE: «Fable の cone/Q1f は 11 / 20(INCOMPLETE)» | `conversations/2026-10-22/RESULT_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md` | L1 |  |
| K125 | L3 reading (mnw1 §5-1): «「比例として述べよ」は点の集合に負ける» | `conversations/2026-10-22/RESULT_mnw1_moy5_menaechmus_newton_explanation_x_form_opus_fable_xhigh_20261022.md` | L1 |  |
| K126 | cannot say: won't vs no trigger: «選択(won't)か引き金の不在かは、本札の腕では分けていない» | `conversations/2026-10-21/RESULT_prf3_moy5_confirm_lattice_bundle_claude_p_20261021.md` | L1 |  |
| K127 | olm1 banner read: «訂正(全体の監査 10-27» | `conversations/2026-10-22/RESULT_olm1_moy5_olmo3_32b_mnw1_arms_20261022.md` | L1 |  |
| K128 | BLOCK verbatim: «Derive the equation from other relations among the given points.» | `conversations/2026-10-21/PREREG_prf2_moy5_proof_block_focus_directrix_claude_p_20261021.md` | L1 |  |
| K129 | PROOF verbatim: «ending with an equation that every position of P_y satisfies» | `conversations/2026-10-21/PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md` | L1 |  |
| K130 | β′ verbatim (read as text): «is not merely an equality of two lengths» | `ConstructGap/exp/b5bp_moy5_blocking_beta_prime_20261014.py` | L1 |  |
| K131 | Q2 line: «{F, V, P_x, P_y}» | `conversations/2026-10-19/PREREG_neq3_moy5_lemma14_question_set_2x2_opus_fable_xhigh_20261019.md` | L1 |  |
| K132 | the frozen question's md5: «md5 `ee39ba02374a5b3fb6db8dafcef4704b`» | `conversations/2026-10-14/SOURCE_frozen_prompts_moy1_moy2_moy5_blocks_alt2_lines_dfc_v1_20261014.md` | L1 |  |
| K133 | C1 arm names: «**名替え** = 問いの七つの名を替えた» | `conversations/2026-10-16/SUMMARY_moy5_cut_across_arms_effort_route_and_argon_20261016.md` | L1 | 6 |
| K134 | frozen file results_prf3_20261021.jsonl = **3fa335be** | `ConstructGap/exp/results_prf3_20261021.jsonl` | L1 |  |
| K135 | frozen file results_neq6_moy5_20261019_claude-opus-5-5.jsonl = **a957c784** | `ConstructGap/exp/results_neq6_moy5_20261019_claude-opus-5-5.jsonl` | L1 |  |
| K136 | frozen file results_mnw1_moy5_20261022_claude-opus-5-5.jsonl = **d9de546a** | `ConstructGap/exp/results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` | L1 |  |
| K137 | frozen file results_b5bp_20261014_claude-opus-5-5_a.jsonl = **d589e2bb** | `ConstructGap/exp/results_b5bp_20261014_claude-opus-5-5_a.jsonl` | L1 |  |
| K138 | frozen file results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl = **f7133073** | `ConstructGap/exp/results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` | L1 |  |
| K139 | frozen file summary_table_moy5_cut_all_cards_20261016.txt = **556b9dfb** | `conversations/2026-10-16/data_moy5_summary/summary_table_moy5_cut_all_cards_20261016.txt` | L1 |  |
| K140 | the pack's prf3.P5B.fable.lat_sym equals the recount = **pack = recount** | `results_prf3_20261021.jsonl` · model = claude-fable-5-1 · arm = P5B · field `lat_sym` | L2 |  |
| K141 | the pack's neq3.A/Q2.opus.ans equals the recount = **pack = recount** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2 · field `cut_in_conjecture` | L2 |  |
| K142 | the pack's mnw1.cone/Q1.fable.bind equals the recount = **pack = recount** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = cone/Q1 · field `bind` | L2 |  |
| K143 | the pack's neq6.max.opus.thinking_med equals the recount = **pack = recount** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2@max · median of `thinking` | L2 |  |
| K144 | the pack's olm3.think.floor equals the recount = **pack = recount** | `results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl` · arm = none/Q1 · field `closure` · all rows drawn | L2 |  |
| K145 | the pack's essay4.A.haiku-5-5.n equals the recount = **pack = recount** | `results_essay4_moy5_20261014_claude-haiku-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-haiku-5-5_r.jsonl` · model = claude-haiku-5-5 · arm = A · rows | L2 |  |

## Readings (L3) and what is not said (×) — the ledger of state 29 (v1's state 23)
- L3 (execution layer, MEMO 10-22 §3 as copied in BRIEF v1 §4): «関係は一揃い浮かんでいて、答えの欄は問いと近道が決め、探る量と封鎖で族の中の選択が動く» — adoption is the human's.
- L3 (the PI's words of 10-22 + the execution layer): the three regimes Pappus / Menaechmus / Descartes — the orange station of state 2 carries this tag.
- L3 (RESULT mnw1 §5-1): «形の指図は点の集合に負ける» (anchored by the text row above).
- × (all as plain statements in state 23): won't vs no trigger (prf3 §4-3) · the prf3 lattice = the 06-25 house CUT · the prf1/prf3 quadratic as attractor evidence · effort across cards / paths · Argon 'stronger' · names / texts / explanations 'got across' · 'the model lacks the relation' · open weights in general · sums across cards; one of the two cuts written alone as 'cut'.

## Corrections between the brief and the data
- None of BRIEF v1 §6 differed from the data (pack_data.py and data.mjs assert all of them; this file anchors them again from raw).
- The frozen question read from SOURCE l.56–84 has md5 `ee39ba02` only with its final newline (1921 characters); without it, 1920 characters / `8071db19`. The essay4 A rows carry `prompt_md5 = ee39ba02…` (asserted in pack_data.py).
- SUMMARY §5-3 says β′ Opus 7 / 20 *with r8*; the field `bind` is 6 / 20. The figure prints 6 and names the r8 value (7) from the SUMMARY's frozen table as a limit (state 11).
- The essay4 Fable K row 17: the stored `bind` is false, the SUMMARY's re-read says true (SUMMARY table, last section). The figure uses the stored field (19 / 20) where Fable K appears (it is not drawn in state 4).

## v2 (11-06): moved from entry P (both readers agreed) and the four disagreements decided by the data

| id | claim (value as the figure prints it) | source (file · key) | level | state |
|---|---|---|---|---|
| K146 | P→Q · Q1 positive control K · Opus answer field = **6** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = K · field `cut_in_conjecture` | L2 | 8 |
| K147 | P→Q · Q1 positive control K · Opus whole = **9** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = K · field `bind` | L2 | 8 |
| K148 | P→Q · Q1 positive control K · Fable answer field = **7** | `results_neq2f_moy5_20261019.jsonl` · model = claude-fable-5-1 · arm = K · field `cut_in_conjecture` | L2 | 8 |
| K149 | P→Q · Q1 positive control K · Fable whole = **9** | `results_neq2f_moy5_20261019.jsonl` · model = claude-fable-5-1 · arm = K · field `bind` | L2 | 8 |
| K150 | P→Q · locus sentence in the answer field · Opus A/Q2 = **20** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = A/Q2 · field `parabola_in_conjecture` | L2 | 8 |
| K151 | P→Q · locus sentence · Fable A/Q2 = **5** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = A/Q2 · field `parabola_in_conjecture` | L2 | 8 |
| K152 | P→Q · locus sentence · Opus L-name/Q2 = **2** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = L-name/Q2 · field `parabola_in_conjecture` | L2 | 9 |
| K153 | P→Q · locus sentence · Opus L-text/Q2 = **0** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = L-text/Q2 · field `parabola_in_conjecture` | L2 | 9 |
| K154 | P→Q · locus sentence · Fable L-name/Q2 = **0** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = L-name/Q2 · field `parabola_in_conjecture` | L2 | 9 |
| K155 | P→Q · locus sentence · Fable L-text/Q2 = **1** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = L-text/Q2 · field `parabola_in_conjecture` | L2 | 9 |
| K156 | P→Q · locus sentence · Opus K/Q2 = **4** | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = K/Q2 · field `parabola_in_conjecture` | L2 | 9 |
| K157 | P→Q · locus sentence · Fable K/Q2 = **0** | `results_neq3_moy5_20261019_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = K/Q2 · field `parabola_in_conjecture` | L2 | 9 |
| K158 | P→Q · decision ② · mnw1 K Opus whole (API xhigh · n 10) = **9** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = K · field `bind` | L2 | 4, 5 |
| K159 | P→Q · decision ② · mnw1 K Opus answer field = **1** | `results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` + `results_mnw1b_moy5_20261022_claude-opus-5-5.jsonl` · model = claude-opus-5-5 · arm = K · field `cut_in_conjecture` | L2 | 4, 5 |
| K160 | P→Q · decision ② · mnw1 K Fable whole = **10** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = K · field `bind` | L2 | 4, 5 |
| K161 | P→Q · decision ② · mnw1 K Fable answer field = **4** | `results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` + `results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · model = claude-fable-5-1 · arm = K · field `cut_in_conjecture` | L2 | 4, 5 |
| K162 | decision ② · essay4 K Fable whole = the STORED field (r17 false; the SUMMARY re-read says true) = **19** | `results_essay4_moy5_20261014_claude-fable-5-1_a.jsonl` + `results_essay4_moy5_20261014_claude-fable-5-1_r.jsonl` · model = claude-fable-5-1 · arm = K · field `bind` | L2 | 4, 5 |
| K163 | decision ② · essay4 K Fable answer field = **1** | `results_essay4_moy5_20261014_claude-fable-5-1_a.jsonl` + `results_essay4_moy5_20261014_claude-fable-5-1_r.jsonl` · model = claude-fable-5-1 · arm = K · field `cut_in_conjecture` | L2 | 4, 5 |
| K164 | decision ② · essay4 K Sonnet whole = **20** | `results_essay4_moy5_20261014_claude-sonnet-5-5_a.jsonl` + `results_essay4_moy5_20261014_claude-sonnet-5-5_r.jsonl` · model = claude-sonnet-5-5 · arm = K · field `bind` | L2 | 5 |
| K165 | decision ④ · prf1 P5 Opus LATX (= CHAIN 1 + LAT-only 1) = **2** | `results_prf1_20261021.jsonl` · model = claude-opus-5-5 · arm = P5 · field `latx` | L2 | 4, 15, 16 |
| K166 | decision ④ · PREREG prf1: «**CHAIN(主)**» = the road's apex predicate is CHAIN; LAT-only is drawn hatched next to it | `conversations/2026-10-21/PREREG_prf1_…md` | L1 | 4 |
| K167 | P→Q · decision ① · b5bp.Bbp.sonnet-5-5 thinking median from the jsonl = **1020.5** (the SUMMARY §6 table prints 1,030 = the upper middle row) | `results_b5bp_20261014_claude-sonnet-5-5_a.jsonl` · arm = Bbp · median of `reasoning_tokens` | L2 | 14 |
| K168 | P→Q · decision ① · b5bp.Bbp.opus-5-5 thinking median from the jsonl = **1742.5** (the SUMMARY §6 table prints 1,753 = the upper middle row) | `results_b5bp_20261014_claude-opus-5-5_a.jsonl` · arm = Bbp · median of `reasoning_tokens` | L2 | 14 |
| K169 | P→Q · decision ① · b5bp.Bbp.fable-5-1 thinking median from the jsonl = **2233.0** (the SUMMARY §6 table prints 2,233 = the upper middle row) | `results_b5bp_20261014_claude-fable-5-1_a.jsonl` · arm = Bbp · median of `reasoning_tokens` | L2 | 14 |
| K170 | P→Q · decision ① · arg5.Bbp thinking median from the jsonl = **8468.5** (the SUMMARY §6 table prints 8,494 = the upper middle row) | `results_arg5_20261016_gemini-4-argon_a.jsonl` · arm = Bbp · median of `reasoning_tokens` | L2 | 14 |
| K171 | P→Q · decision ① · arg5d.Bbp thinking median from the jsonl = **965.0** (the SUMMARY §6 table prints 1,005 = the upper middle row) | `results_arg5d_20261016_gemini-4-argon_a.jsonl` · arm = Bbp · median of `reasoning_tokens` | L2 | 14 |
| K172 | decision ① · SUMMARY §6: «| Bbp | — | 1,030 | 1,753 | 2,233 | 8,494 |» (= median_high of the same 20 rows; ratio 3.8〜8.2 · the data median gives 3.8〜8.3) | `conversations/2026-10-16/SUMMARY_…md` §6 | L1 | 14 |
| K173 | P→Q · decision ③ · olm1 base natural · K · bind = **2** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · variant natural · arm = K · field `bind` · all rows drawn | L2 | 22 |
| K174 | P→Q · decision ③ · olm1 base natural · K · cut_in_conjecture = **1** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · variant natural · arm = K · field `cut_in_conjecture` · all rows drawn | L2 | 22 |
| K175 | P→Q · decision ③ · olm1 base think · K · bind = **10** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · variant think · arm = K · field `bind` · all rows drawn | L2 | 22 |
| K176 | P→Q · decision ③ · olm1 base think · K · cut_in_conjecture = **0** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · variant think · arm = K · field `cut_in_conjecture` · all rows drawn | L2 | 22 |
| K177 | olm1 base natural · K · rows drawn (empty kept) = **10** | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · variant natural · arm = K · rows | L2 | 22 |
| K178 | olm1 base natural · K · rows with raw = **5** (= 5 empty rows) | `results_olm1_moy5_20261022_olmo-3-1125-32b-mlx-bf16.jsonl` · variant natural · arm = K · rows with raw | L2 | 22 |
| K179 | P→Q · olm3 Think B1 · K · bind = **10** | `results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl` · arm = K · field `bind` · all rows drawn | L2 | 22 |
| K180 | P→Q · olm3 Think B1 · K · cut_in_conjecture = **0** | `results_olm3_moy5_20261022_olmo-3-32b-think-mlx-bf16.jsonl` · arm = K · field `cut_in_conjecture` · all rows drawn | L2 | 22 |
| K181 | decision ③ · the olm1 banner: «think K r3 の答えの JSON は» … `cut_in_conjecture` False · `bind` True = it touches the answer field (rule 0 / reading 1), not the whole | `conversations/2026-10-22/RESULT_olm1_…md` l.4 | L1 | 22 |
| K333 | D_R2 (3) · neq6 Opus A/Q2@medium · locus sentence in the answer field = **20** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · arm = A/Q2@medium · field `parabola_in_conjecture` | L2 | 11 |
| K334 | D_R2 (3) · neq6 Opus A/Q2@max · locus sentence in the answer field = **19** | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · arm = A/Q2@max · field `parabola_in_conjecture` | L2 | 11 |
| K335 | D_R1 ④ · the K hint (card of state 17): «Hint: the relation in question is a mean proportional: the segment F–P_x is the mean proportional between F–V and F–P_y» | `conversations/2026-10-14/SOURCE_…md` (moy-5 の陽性統制 K) | L1 | 17 |
| K336 | D_R1 ④ · the FORM sentence (card of state 19): «state the invariant as a PROPORTION (a mean proportional), not as an equality of lengths.» | `conversations/2026-10-22/PREREG_mnw1_…md` l.34 | L1 | 19 |

### The four disagreements (BRIEF v2 §2-2) — how the data decided them
- ① **Argon's thinking ratio and the source of its medians**: the jsonl `reasoning_tokens` medians (mean of the two middle rows, n 20) are Sonnet 1020.5 · Opus 1742.5 · Fable 2233 · Argon high 8468.5 · Argon default 965 → ratio 3.8〜8.3. The SUMMARY §6 table prints 1,030 · 1,753 · 2,233 · 8,494 · (1,005) = exactly `statistics.median_high` of the same 20 rows (asserted in pack_data.py) → ratio 3.8〜8.2. Same rows, another way of taking the middle. The figure draws the data median (state 14) and names the SUMMARY values and their origin in the note.
- ② **The card of the positive control K**: both are drawn, as different cards: essay4 (API high · n 20: Opus 20 / 20 · Fable 19 / 20 · Sonnet 20 / 20 · Haiku 20 / 20 whole) and mnw1 (API xhigh · n 10: Opus 9 / 10 · Fable 10 / 10 whole) in state 5. essay4 Fable K row 17: the stored `bind` is false, the SUMMARY's re-read says true → the figure uses the stored field (19 / 20) and says so in the limit line. 'The control stands' is said on the whole-answer cut (the answer field differs by model and card).
- ③ **Does the olm1 banner touch OLMo's K?** The banner (10-27 audit A1) names think K r3: its answer JSON wrote the cut, the reader emptied the conjecture on a bad escape → `cut_in_conjecture` False, `bind` True. It changes the answer-field count (rule 0 / reading 1), not the whole count (bind 10 / 10). The figure carries the whole counts (2 / 10 · 10 / 10 · 10 / 10) and states the banner's reach in state 22.
- ④ **The apex predicate of prf1 P5**: PREREG prf1 names **CHAIN (main)**; LATX (lattice written) = CHAIN + LAT-only. The summary road (state 4) draws CHAIN as the bar and LAT-only hatched next to it, so 1 / 10 (CHAIN) and 2 / 10 (LATX) are both readable; the dots of states 3 / 15 / 16 keep the route5 classes.
