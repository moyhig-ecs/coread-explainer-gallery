# captures — which file shows which state

State numbers come from config.json; the file names follow the coread-explainer skill (`video_s<NN>`, `page_<dark|light>_s<NN>[_en]`, `phone_<dark|light>_s<NN>`).
`J1` / `J2` = JupyterLab (state 0; after the figure's own next button reached the kernel) · `J3` = JupyterLab (v2: state 18 after `goto_chapter("sae")`, with the kernel's recount) · `M1` = marimo (state 4, after a Python button moved the figure) · `M2` = marimo (v2: state 18 after the Python button "chapter sae").

| state | what it shows (ja) | what it shows (en) | files present |
|---|---|---|---|
| 0 | 問題の図 — 座標から | the problem — from the coordinates | 2: `video_s00.png`, `video_en_s00.png` |
| 1 | 問題の図 — 二つの名指し | the problem — two ways to name the circle | 2: `video_s01.png`, `video_en_s01.png` |
| 2 | 二つの問題文 — open | two prompts — open | 2: `video_s02.png`, `video_en_s02.png` |
| 3 | 二つの問題文 — blocked | two prompts — blocked | 2: `video_s03.png`, `video_en_s03.png` |
| 4 | open で起こること — open の十行(blocked は薄く) | what open does — open's ten rows (blocked faded) | 2: `video_s04.png`, `video_en_s04.png` |
| 5 | open で起こること — 全文の label と答えの欄 | what open does — whole-text label vs the answer field | 2: `video_s05.png`, `video_en_s05.png` |
| 6 | open の場面 — JSON から書き始めた行(s3) | an open row — one that started with the JSON (s3) | 2: `video_s06.png`, `video_en_s06.png` |
| 7 | open の場面 — 29,550 字の行(s1) | an open row — 29,550 chars (s1) | 2: `video_s07.png`, `video_en_s07.png` |
| 8 | blocked で起こること — 書き始めで分かれる(open は薄く) | what blocked does — it splits by how the row starts (open faded) | 2: `video_s08.png`, `video_en_s08.png` |
| 9 | blocked で起こること — 二つの円の文がある行(open と blocked は別の標本) | what blocked does — rows with a sentence naming either circle (open and blocked are separate samples) | 2: `video_s09.png`, `video_en_s09.png` |
| 10 | blocked の場面 — 「直径 = He・Hi」の文が先・答えの欄は O1O2 の行(s2) | a blocked row — the 'diameter = He-Hi' sentence first, O1O2 in the answer field (s2) | 2: `video_s10.png`, `video_en_s10.png` |
| 11 | blocked で起こること — cue を替える | what blocked does — change the cue | 2: `video_s11.png`, `video_en_s11.png` |
| 12 | block の中で bind する瞬間 — 同じ一行の二つの位置 | the bind moment inside the block — two positions of one row | 2: `video_s12.png`, `video_en_s12.png` |
| 13 | 天秤 — ① He を書く位置(att・F5a-2 s1) | the balance — ① the position where He is written (att · F5a-2 s1) | 2: `video_s13.png`, `video_en_s13.png` |
| 14 | 天秤 — ② bind の瞬間(O の側) | the balance — ② the bind moment (O side) | 2: `video_s14.png`, `video_en_s14.png` |
| 15 | 立体 — 16 の位置 × 上位 10 head | the volume — 16 positions × the top-10 heads | 2: `video_s15.png`, `video_en_s15.png` |
| 16 | 他の model — open → blocked | other models — open → blocked | 2: `video_s16.png`, `video_en_s16.png` |
| 17 | 他の model — OLMo-3 32B の Think(Q4)と base(cue \n\n) | other models — OLMo-3 32B's Think (Q4) and base (cue \n\n) | 2: `video_s17.png`, `video_en_s17.png` |
| 18 | 作図と SAE の推移 — 本文が O1O2 を名指す所(F5a-2 考えの道 r15) | construction × SAE trajectory — where the text names O1O2 (F5a-2 thinking path, r15) | 2: `video_s18.png`, `video_en_s18.png` |
| 19 | 作図と SAE の推移 — 本文が He・Hi を名指す所(F5b-1 natural r14) | construction × SAE trajectory — where the text names He-Hi (F5b-1 natural, r14) | 2: `video_s19.png`, `video_en_s19.png` |
| 20 | 作図と SAE の推移 — 同じ目盛りで並べる(名指した token の前 32 / 後 32) | construction × SAE trajectory — side by side on one scale (32 tokens before / after the naming) | 2: `video_s20.png`, `video_en_s20.png` |
| 21 | 作図と SAE の推移 — 集計: 前 32 と後 32(O1O2 の出来事 59 行・He・Hi の出来事 34 行) | construction × SAE trajectory — the aggregate: 32 before vs 32 after (59 O1O2 events · 34 He-Hi events) | 2: `video_s21.png`, `video_en_s21.png` |
| 22 | 作図と SAE の推移 — 行ごとの坂: 59 行・34 行 × 四つの群(全分布) | Construction × SAE — the row-by-row slopes: 59 and 34 rows × four groups (the whole distribution) | 2: `video_s22.png`, `video_en_s22.png` |
| 23 | 作図と SAE の推移 — 中点の群の上がりと、本文が数式に移ること(olm62) | construction × SAE trajectory — the mid group's rise and the text moving into formulas (olm62) | 2: `video_s23.png`, `video_en_s23.png` |
| 24 | 作図と SAE の推移 — 数式に移らなかった O1O2 の 11 本でも、中点は上がる?(薄い ✓) | construction × SAE trajectory — does the mid group rise even in the 11 O1O2 events whose text did not move into formulas? (a thin ✓) | 2: `video_s24.png`, `video_en_s24.png` |
| 25 | 二つの label — cmt5 の 120 行の「bind」は、全文と答えの欄で数が替わる | two labels — cmt5's 120 rows: 'bind' changes with the label (whole text vs answer field) | 2: `video_s25.png`, `video_en_s25.png` |
| 26 | 札と系統樹 — この図の各章は、どの札から来て、その札は系統樹のどの塊に居るか | cards and the tree — which card each chapter of this figure draws on, and where that card sits in the card tree | 2: `video_s26.png`, `video_en_s26.png` |
| 27 | その後の流れ — 10-28 の図から olm128 まで(一本の流れ・11-06 版で足した部分) | What came after — from the 10-28 figure to olm128 (one stream · the part added in the 11-06 version) | 2: `video_s27.png`, `video_en_s27.png` |
| 28 | (a) 台帳の L3 → olm76 — 答えの欄の始まりでも、結びの群は線に届かない | (a) ledger L3 → olm76 — even at the start of the answer field, the close group does not reach the line | 2: `video_s28.png`, `video_en_s28.png` |
| 29 | (b) 推論空間の探し(1) — 先読みは、J-lens の読み出しでほぼ全部読める | (b) the inference-space search (1) — the look-ahead is almost all readable from the J-lens readout | 2: `video_s29.png`, `video_en_s29.png` |
| 30 | (b) 推論空間の探し(2) — 一貫して出る上乗せは k = 8 だけ(層 32・小さい) | (b) the inference-space search (2) — the only surplus that shows consistently is at k = 8 (layer 32 · small) | 2: `video_s30.png`, `video_en_s30.png` |
| 31 | (c) 語でない構造(1) — 指示語・束縛・行いを運ぶ head(合成の文) | (c) structure that is not words (1) — reference words · binding · the heads that carry the behaviour (synthetic sentences) | 2: `video_s31.png`, `video_en_s31.png` |
| 32 | (c) 語でない構造(2) — 位置を入れ替えたとき、行いが指しに従う割合と値に従う割合(層ごと・札ごと) | (c) structure that is not words (2) — when positions are swapped, the share of the behaviour that follows the pointer and the value (by layer · by card) | 2: `video_s32.png`, `video_en_s32.png` |
| 33 | (d) apex の証明(1) — 求めても、二等分線 → 直角 → Thales の逆の鎖は 0 / 37 | (d) the apex proof (1) — when asked, the chain bisector → right angle → converse of Thales is 0 / 37 | 2: `video_s33.png`, `video_en_s33.png` |
| 34 | (d) apex の証明(2) — frontier の段を与えると、続きは書く(26 / 40・23 / 40)・導きは別 | (d) the apex proof (2) — given the frontier's steps, the continuation is written (26 / 40 · 23 / 40) · deriving is another matter | 2: `video_s34.png`, `video_en_s34.png` |
| 35 | 次の問い(1) — 依頼者が選んだ A「cue × JSON から書き始める割合」は olm128 で読んだ: 位置 0 の書き始めでは cue の差は説明されない | the next question (1) — the teacher's choice A, "cue × the share starting with the JSON", was read as olm128: the start at position 0 does not explain the cue difference | 2: `video_s35.png`, `video_en_s35.png` |
| 36 | 次の問い(2) — 読み手が出した候補の並び(A は読んだ・B〜E は並べるだけ)と、第二段(依頼者の裁定待ち) | the next question (2) — the candidates the readers raised (A was read · B-E only listed), and the second stage (waits for the teacher) | 2: `video_s36.png`, `video_en_s36.png` |
| 37 | 台帳(1〜6 章)— 言える(L1)と読み(L3) | ledger (chapters 1-6) — can say (L1) and readings (L3) | 2: `video_s37.png`, `video_en_s37.png` |
| 38 | 台帳(7 章の olm59 と cmt5)— 言える(L1)と読み(L3): 作図と SAE の推移・cmt5 の二つの label | ledger (chapter 7: olm59 and cmt5) — can say (L1) and readings (L3): construction × SAE trajectory, cmt5's two labels | 2: `video_s38.png`, `video_en_s38.png` |
| 39 | 台帳(olm62 と札の系統樹)— 言える(L1)と読み(L3) | ledger (olm62 and the card tree) — can say (L1) and readings (L3) | 2: `video_s39.png`, `video_en_s39.png` |
| 40 | 台帳(その後の部分 1 / 2)— 言える(L1・L2) | ledger (the added part 1 / 2) — can say (L1, L2) | 2: `video_s40.png`, `video_en_s40.png` |
| 41 | 台帳(その後の部分 2 / 2)— 読み(L3)と言えない | ledger (the added part 2 / 2) — readings (L3) and cannot say | 2: `video_s41.png`, `video_en_s41.png` |
| 42 | 台帳 — 言えない と 受け入れの問い | ledger — cannot say, and the acceptance questions | 2: `video_s42.png`, `video_en_s42.png` |

v2 pairs (skill §6: a moment gets a before / after still; 1920 x 1080, ja, dark): `video_s18a.png` / `video_s18b.png` = state 18 with the cursor on the last token before the naming that no predicate hits (nothing lights) / on the first naming token (the O1O2 circle lights) · `video_s19a.png` / `video_s19b.png` = the same for state 19 (the He-Hi circle).

| pattern | what | taken in | measured (PNG header) |
|---|---|---|---|
| `video_sNN.png` | video still, ja, dark | 1920 x 1080 frame | image 1920 x 1080 |
| `video_en_sNN.png` | video still, en, dark | 1920 x 1080 frame | image 1920 x 1080 |
| `page_dark_sNN.png` | desk, dark, ja | 1440-wide window | not taken |
| `page_light_sNN.png` | desk, light, ja | 1440-wide window | not taken |
| `page_dark_sNN_en.png` | desk, dark, en | 1440-wide window | not taken |
| `page_light_sNN_en.png` | desk, light, en | 1440-wide window | not taken |
| `phone_dark_sNN.png` | phone, dark, ja | 390-wide window | not taken |
| `phone_light_sNN.png` | phone, light, ja | 390-wide window | not taken |

The desk and phone stills are of the figure element (the page's margins are outside the image, so the image is narrower than the window); a phone still is as tall as the content (the long ledger state is the tallest).
