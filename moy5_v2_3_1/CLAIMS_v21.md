# CLAIMS_v21 — what v2.1 moved, decided and fixed (BRIEF v2.1 §2-2〜§2-7 · 2026-11-07)

Each row has one anchor in `claims_anchors.json` (`check_claims.py` looks at the place itself: the card's json / jsonl, SCOPE 10-31, a RESULT, a PREREG). Written by `make_anchors_v21.py` (never by hand).
The grade of each card is recomputed by `check_claims.py` from SCOPE 10-31 (rule i) or the card's RESULT line (rule ii), apart from `pack_data.py`.

| id | claim (value as the figure prints it) | source (file · key) | level | state |
|---|---|---|---|---|
| K337 | olm60 · grade **関門** · rule (ii) | `conversations/2026-10-28/RESULT_olm60_moy5_frontier_routes_read_by_olmo_sae_STOPPED_at_C1_20261028.md` · «Q1〜Q5 は走っていない(判定なし)» | L1 | 23–26, 30 |
| K338 | olm61 · grade **判定** · rule (ii) | `conversations/2026-10-28/RESULT_olm61_moy5_olmo_continues_frontier_route_C1_stop_sae_route_read_20261028.md` · «**22 / 30**(73 %) | ✓» | L1 | 23–26, 30 |
| K339 | olm64 · grade **判定** · rule (ii) | `conversations/2026-10-28/RESULT_olm64_moy5_frontier_routes_direction_readout_20261028.md` · «観測以上の乱数 0 / 2000) | ✓» | L1 | 23–26, 30 |
| K340 | olm67 · grade **判定** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 判定 · 較正 · 記述 | L1 | 23–26, 30 |
| K341 | olm68 · grade **判定** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 判定 · 記述 | L1 | 23–26, 30 |
| K342 | olm69 · grade **記述** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 記述 | L1 | 23–26, 30 |
| K343 | olm70 · grade **関門** · rule (ii) | `conversations/2026-10-29/RESULT_olm70_moy5_own_word_instrument_calibration_and_retry_20261029.md` · «C ✗ のため**読まない**» | L1 | 23–26, 30 |
| K344 | olm71 · grade **関門** · rule (ii) | `conversations/2026-10-29/RESULT_olm71_moy5_opening_and_body_word_instruments_by_group_20261029.md` · «Q2〜Q5 は読まない» | L1 | 23–26, 30 |
| K345 | olm72 · grade **関門** · rule (ii) | `conversations/2026-10-29/RESULT_olm72_moy5_body_words_without_after_condition_20261029.md` · «Q2・Q3 は読まない» | L1 | 23–26, 30 |
| K346 | olm73 · grade **言えない** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 言えない | L1 | 23–26, 30 |
| K347 | olm74 · grade **判定** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 判定 · 記述 | L1 | 23–26, 30 |
| K348 | olm77 · grade **記述** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 記述 · 言えない | L1 | 23–26, 30 |
| K349 | olm78 · grade **判定** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 判定 · 較正 · 記述 · 言えない | L1 | 23–26, 30 |
| K350 | olm79 · grade **言えない** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 言えない | L1 | 23–26, 30 |
| K351 | olm81 · grade **判定** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 判定 · 記述 · 言えない | L1 | 23–26, 30 |
| K352 | olm82 · grade **判定** · rule (ii) | `conversations/2026-10-31/RESULT_olm82_moy5_common_mode_drop_next_token_concentration_20261031.md` · «S1 **0.83**・S2 **0.77**・S3 **0.84** | **✓**» | L1 | 23–26, 30 |
| K353 | olm63 · grade **判定** · rule (ii) | `conversations/2026-10-28/RESULT_olm63_moy5_sae_calibration_notation_context_position_20261028.md` · «**+0.0516** | ✓» | L1 | 23–26, 30 |
| K354 | olm80 · grade **記述** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 記述 · 言えない | L1 | 23–26, 30 |
| K355 | thk1 · grade **関門** · rule (ii) | `conversations/2026-10-30/RESULT_thk1_moy5_q2_thinking_summary_pilot_20261030.md` · «止める規則 §4 で各 model 1 行で止まった» | L1 | 23–26, 30 |
| K356 | thk2 · grade **記述** · rule (i) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 · tiers where the name stands in the 根拠 column / a 言えない bullet: 記述 | L1 | 23–26, 30 |
| K357 | the five columns: 判定 9 · 記述 4 · 較正 0 · 言えない 2 · 関門で止まった 5 = **20** (rule i 11 · ii 9) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` §1 + the RESULT lines of the 9 cards not named there | L1 | 23, 30 |
| K358 | b5bp Bbp opus-5-5 · median number of relations = **19.5** (mean of the two middle rows = the SUMMARY's relations column) | `ConstructGap/exp/results_b5bp_20261014_claude-opus-5-5_a.jsonl` · relations | L1 | 14 |
| K359 | b5bp Bbp fable-5-1 · median number of relations = **19.5** (mean of the two middle rows = the SUMMARY's relations column) | `ConstructGap/exp/results_b5bp_20261014_claude-fable-5-1_a.jsonl` · relations | L1 | 14 |
| K360 | b5bp Bbp sonnet-5-5 · median number of relations = **11.0** (mean of the two middle rows = the SUMMARY's relations column) | `ConstructGap/exp/results_b5bp_20261014_claude-sonnet-5-5_a.jsonl` · relations | L1 | 14 |
| K361 | arg5 Bbp · median number of relations = **36.0** | `ConstructGap/exp/results_arg5_20261016_gemini-4-argon_a.jsonl` · relations | L1 | 14 |
| K362 | b5bp Bbp claude-sonnet-5-5 · the upper of the two middle rows of reasoning_tokens = **1,030** (= the SUMMARY §6 table's value · decision ①) | `ConstructGap/exp/results_b5bp_20261014_claude-sonnet-5-5_a.jsonl` · reasoning_tokens | L1 | 14 |
| K363 | b5bp Bbp claude-opus-5-5 · the upper of the two middle rows of reasoning_tokens = **1,753** (= the SUMMARY §6 table's value · decision ①) | `ConstructGap/exp/results_b5bp_20261014_claude-opus-5-5_a.jsonl` · reasoning_tokens | L1 | 14 |
| K364 | b5bp Bbp claude-fable-5-1 · the upper of the two middle rows of reasoning_tokens = **2,233** (= the SUMMARY §6 table's value · decision ①) | `ConstructGap/exp/results_b5bp_20261014_claude-fable-5-1_a.jsonl` · reasoning_tokens | L1 | 14 |
| K365 | arg5 Bbp Argon · the upper of the two middle rows of reasoning_tokens = **8,494** (= the SUMMARY §6 table's value · decision ①) | `ConstructGap/exp/results_arg5_20261016_gemini-4-argon_a.jsonl` · reasoning_tokens | L1 | 14 |
| K366 | neq3 A/Q2 Opus · rows with a parabola AND a cut in the answer field = **7** (every cut row also writes the locus) | `results_neq3_moy5_20261019_claude-opus-5-5.jsonl` · parabola_in_conjecture ∧ cut_in_conjecture | L1 | 8 |
| K367 | neq6 max Opus · rows with both in the answer field = **18** (locus 19 · cut 19 · decision ⑤) | `results_neq6_moy5_20261019_claude-opus-5-5.jsonl` · parabola_in_conjecture ∧ cut_in_conjecture | L1 | 11 |
| K368 | prf1 P5K = Bbp + essay4's K hint verbatim + PROOF (decisions ③ ④: the K-hint card's source is SOURCE 10-14, not mnw1; P5K is kept off the road) | `conversations/2026-10-21/PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md` l.23 | L1 | 4, 17 |
| K369 | prf1's PREREG names P5K the instrument's positive control (gate: LATX ≥ 8 / 10) — decision ④ | same PREREG l.52 | L1 | 4 |
| K370 | mnw1 none/Q1f claude-opus-5-5 r12 · the answer field writes the floor as a ratio, then «VE : VP_x = VP_x : VJ» (decision ⑦: an answer-field cut, not only a degenerate proportion) | `ConstructGap/exp/results_mnw1_moy5_20261022_claude-opus-5-5.jsonl` · raw | L1 | 28 |
| K371 | mnw1 none/Q1f claude-fable-5-1 r3 · the answer field writes the floor as a ratio, then «VE : VP_x = VP_x : VJ» (decision ⑦: an answer-field cut, not only a degenerate proportion) | `ConstructGap/exp/results_mnw1_moy5_20261022_claude-fable-5-1.jsonl` · raw | L1 | 28 |
| K372 | mnw1 none/Q1f claude-fable-5-1 r7 · the answer field writes the floor as a ratio, then «VE : VP_x = VP_x : VJ» (decision ⑦: an answer-field cut, not only a degenerate proportion) | `ConstructGap/exp/results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · raw | L1 | 28 |
| K373 | mnw1 none/Q1f claude-fable-5-1 r17 · the answer field writes the floor as a ratio, then «FV : FP_x = FP_x : KP_y» (decision ⑦: an answer-field cut, not only a degenerate proportion) | `ConstructGap/exp/results_mnw1b_moy5_20261022_claude-fable-5-1.jsonl` · raw | L1 | 28 |
| K374 | post-hoc look-ahead 2 tokens before = 75 % (dashed; D3 ①) | `ConstructGap/exp/olm67/read.json` · Q2 → frac_top5_by_k → 2 | L1 | 24 |
| K375 | Q3 run-up difference cut − floor = +0.054 (✓; not for outside use · D3 ② · G-04) | `ConstructGap/exp/olm67/read.json` · Q3 → diff | L1 | 24 |
| K376 | d̂ cut Opus +0.825 (G-01) | `ConstructGap/exp/olm67/read.json` · Q1_desc → cut|opus → median_delta | L1 | 24 |
| K377 | d̂ cut Fable +0.744 (G-01) | `ConstructGap/exp/olm67/read.json` · Q1_desc → cut|fable → median_delta | L1 | 24 |
| K378 | d̂ floor Opus +0.868 (G-01) | `ConstructGap/exp/olm67/read.json` · Q1_desc → floor_only|opus → median_delta | L1 | 24 |
| K379 | d̂ floor Fable +0.227 (G-01: Fable separates) | `ConstructGap/exp/olm67/read.json` · Q1_desc → floor_only|fable → median_delta | L1 | 24 |
| K380 | d̂ cut all median +0.765 (G-24) | `ConstructGap/exp/olm67/read.json` · Q1 → median_delta | L1 | 24 |
| K381 | random 95 % point 0.135 (G-24) | `ConstructGap/exp/olm67/read.json` · Q1 → null_median_p95 | L1 | 24 |
| K382 | d̂ floor all +0.512 (G-24) | `ConstructGap/exp/olm67/read.json` · Q1_desc → floor_only|all → median_delta | L1 | 24 |
| K383 | olm64 random 95 % point 0.1765 (G-24) | `ConstructGap/exp/olm64/read.json` · Q1_P5B_lat_L32 → null_median_p95 | L1 | 24 |
| K384 | olm64 Q3 null 0.3645 (G-24) | `ConstructGap/exp/olm64/read.json` · Q3_apex_minus_floor_L32 → null_p95 | L1 | 24 |
| K385 | olm71 BODY|L 57 / 75 = 76 % (D3 ③) | `ConstructGap/exp/olm71/read.json` · gates_test → BODY|L → rows_nonempty | L1 | 25 |
| K386 | olm71 BODY|L n 75 | `ConstructGap/exp/olm71/read.json` · gates_test → BODY|L → n_rows | L1 | 25 |
| K387 | olm71 BODY|A 11 / 16 = 69 % (D3 ③) | `ConstructGap/exp/olm71/read.json` · gates_test → BODY|A → rows_nonempty | L1 | 25 |
| K388 | olm71 BODY|A n 16 | `ConstructGap/exp/olm71/read.json` · gates_test → BODY|A → n_rows | L1 | 25 |
| K389 | olm72 BODY|L 57 / 75 (D3 ③) | `ConstructGap/exp/olm72/read.json` · gates_test → BODY|L → rows_nonempty | L1 | 25 |
| K390 | olm72 BODY|A 11 / 16 (D3 ③) | `ConstructGap/exp/olm72/read.json` · gates_test → BODY|A → rows_nonempty | L1 | 25 |
| K391 | olm80 within-card null median 0.522 (the line 0.60 is on the 95 % point · decision ⑨ · G-21) | `ConstructGap/exp/olm80/control.json` · C2_within_card_null → null_auc32 → median | L1 | 26 |
| K392 | olm81 Q3 formula − words +0.027 (R3 one-reader item kept: SCOPE 記述) | `ConstructGap/exp/olm81/read.json` · Q3_desc → F_vs_W_O → diff_F_minus_W | L1 | 25 |
| K393 | olm81 Q3 permutation p 0.13 | `ConstructGap/exp/olm81/read.json` · Q3_desc → F_vs_W_O → perm_p_two_sided | L1 | 25 |
| K394 | olm81 median +0.070 (G-24) | `ConstructGap/exp/olm81/read.json` · Q1_formula_only_O → median | L1 | 25 |
| K395 | olm74 Q2 sign test p 8.1e−9 (rows as independent · G-06) | `ConstructGap/exp/olm74/read.json` · Q2 → binom_p | L1 | 25 |
| K396 | olm63 Q1 ASCII +0.0093 ✗ (decision ⑪) | `ConstructGap/exp/olm63/read.json` · Q1_ascii_gain → S2_minus_S1 | L1 | 26 |
| K397 | olm63 Q2 no question text +0.0516 ✓ (decision ⑪) | `ConstructGap/exp/olm63/read.json` · Q2_no_prompt_gain → S3_minus_S1 | L1 | 26 |
| K398 | olm82 ρ min 0.772 (line 0.3 · G-24) | `ConstructGap/exp/olm82/read.json` · Q2_jlens_rho_common_vs_entropy → S2_given_route | L1 | 25 |
| K399 | olm82 ρ max 0.836 | `ConstructGap/exp/olm82/read.json` · Q2_jlens_rho_common_vs_entropy → S3_formula_only | L1 | 25 |
| K400 | thk1 claude-opus-5-5 · thinking_tokens = **2,724** (one row · R2 one-reader item kept · token vs characters = decision ⑩) | `ConstructGap/exp/results_thk1_moy5_20261030_claude-opus-5-5.jsonl` · thinking_tokens | L1 | 26 |
| K401 | thk1 claude-fable-5-1 · thinking_tokens = **7,704** (one row · R2 one-reader item kept · token vs characters = decision ⑩) | `ConstructGap/exp/results_thk1_moy5_20261030_claude-fable-5-1.jsonl` · thinking_tokens | L1 | 26 |
| K402 | thk1 claude-opus-5-5 · summary_chars = **2,762** (one row · R2 one-reader item kept · token vs characters = decision ⑩) | `ConstructGap/exp/results_thk1_moy5_20261030_claude-opus-5-5.jsonl` · summary_chars | L1 | 26 |
| K403 | thk1 claude-fable-5-1 · summary_chars = **8,342** (one row · R2 one-reader item kept · token vs characters = decision ⑩) | `ConstructGap/exp/results_thk1_moy5_20261030_claude-fable-5-1.jsonl` · summary_chars | L1 | 26 |
| K404 | olm72: 113 of the 118 rows without a word have a formula-only cut sentence (RESULT olm72's diagnosis; the 118 is recounted from read.json) | `conversations/2026-10-29/RESULT_olm72_moy5_body_words_without_after_condition_20261029.md` | L1 | 25 |
| K405 | olm82 Q1a ✗ (R3 one-reader item kept) | `conversations/2026-10-31/RESULT_olm82_moy5_common_mode_drop_next_token_concentration_20261031.md` | L1 | 25 |
| K406 | olm82 L3 cannot be resolved | `conversations/2026-10-31/RESULT_olm82_moy5_common_mode_drop_next_token_concentration_20261031.md` | L1 | 25 |
| K407 | olm80 C2: median 0.522, 95 % point 0.739, the line ≤ 0.60 on the 95 % point (decision ⑨) | `conversations/2026-10-31/RESULT_olm80_moy5_layer32_change_cut_vs_floor_beyond_words_20261031.md` | L1 | 26 |
| K408 | olm74 Q2: 192 / 288 = O rows with d > 0 against the same row's pseudo event; +0.052 = the median of d (decision ⑧) | `conversations/2026-10-29/RESULT_olm74_moy5_lemma_arms_vs_other_cut_rows_cut_word_set_20261029.md` | L1 | 25 |
| K409 | olm74 Q3: the same +0.052 is O's median d, compared with L (decision ⑧) | `conversations/2026-10-29/RESULT_olm74_moy5_lemma_arms_vs_other_cut_rows_cut_word_set_20261029.md` | L1 | 25 |
| K410 | olm74: by card × model 15 / 19, p 0.0096 (G-06) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25, 30 |
| K411 | olm68: Q1 ✓ pooled only, Opus alone p 0.052 (G-13) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25 |
| K412 | olm81: Opus 36 / 53 = 3 rows above the smallest pass (G-14) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25 |
| K413 | olm74: the lemma arms' weakness splits by model (G-15) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25 |
| K414 | olm67: Fable separates cut and floor (G-01) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 24 |
| K415 | olm78: 'most of it is the words piling up' = SCOPE's wording, put at L3 (G-07 · D3 ⑥) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25, 30 |
| K416 | SCOPE's 11-07 note on the main verdict (thk3 Q2 ✗) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 30 |
| K417 | the own-word instruments closed (SCOPE §4 · D3 ③ title) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25 |
| K418 | olm67 Q2: 2 tokens before 75 % is post hoc (D3 ①) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 24 |
| K419 | olm67 Q3 / olm68: not for outside use (G-04 · G-05) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 24, 25 |
| K420 | olm68: the 10-31 correction (G-05) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 25 |
| K421 | the inner state is not said (D3 ⑤ · G-10) | `conversations/2026-10-31/SCOPE_line1_line2_claimable_after_olm76_81_20261031.md` | L1 | 29, 30 |
| K422 | bundle ① carries 'the house fires it' (PI 11-07 F4 = C7) | `conversations/2026-11-06/coread_station2_3/station3_moy5/BRIEF_v2_1_moy5_received_version_one_maker_20261107.md` | L1 | 27 |
| K423 | bundle ③ in the RESULT's words (D3_R2 D-19) | `conversations/2026-11-06/coread_station2_3/station3_moy5/RESULT_station3_moy5_next_visible_two_maker_variation_20261106.md` | L1 | 27 |
| K424 | bundle example (reader's verbatim) N_R2_Q N-2: «同じ札・同じ effort の腕の中で、答えの欄に cut が出た行と出なかった行は、行ごとの …» | `conversations/2026-11-06/coread_station2_3/station3_moy5/reads/N_R2_Q/judge_reply.md` | L1 | 27 |
| K425 | bundle example (reader's verbatim) N_R2_Q N-3: «β′ の一文を一つの札で、経路 {API, claude -p} × effort {high,…» | `conversations/2026-11-06/coread_station2_3/station3_moy5/reads/N_R2_Q/judge_reply.md` | L1 | 27 |
| K426 | bundle example (reader's verbatim) T_R2 N-4: «比例の形の一文を Q1 の点の集合 {E, J, K, P_y} でなく Q2 の {F, V,…» | `conversations/2026-11-06/coread_station2_3/station3_moy5/reads/T_R2/judge_reply.md` | L1 | 27 |
| K427 | bundle example (reader's verbatim) N_R1_Q N-1: «塞ぎの一文を禁止と指図に分ける — prf3 P5B の LAT_SYM(Opus 10 / 1…» | `conversations/2026-11-06/coread_station2_3/station3_moy5/reads/N_R1_Q/judge_reply.md` | L1 | 27 |
| K428 | bundle example (reader's verbatim) N_R2_P N-4: «読み取り器 v1・v2・人の裁定で cut の判定が割れるのはどの行か。その割れは答えの欄と理由…» | `conversations/2026-11-06/coread_station2_3/station3_moy5/reads/N_R2_P/judge_reply.md` | L1 | 27 |
