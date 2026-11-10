# SCRIPT — a two-voice scene for the video (moy-1)

- Length: about 285 seconds (characters / 7.4 per second + 0.45 s between lines). **≤ 285 s in all** (v3: the part added after the 10-28 figure, 12 lines; v2.1 was ≤ 195 s, v2 ≤ 180 s, v1 ≤ 150 s). The first 10 s (lines 01–02) are the core, on state 8: **open は 10 行中 8 行が裸の共円、blocked は 10 行中 6 行が O1O2 の円(別の標本)。**
- Two voices: **A** = the listener (asks; the question is the state's headline, shortened), **B** = the explainer. No real character's name, picture or voice.
- Each line names the state it cues and the claim ids it rests on (CLAIMS.md). Numbers are read from the data by `make_script.py`, never typed. Frames: `captures/video_s<N>.png` (1920 × 1080).

| # | voice | line (spoken) | cue (the state shown) | length | start | claims |
|---|---|---|---|---|---|---|
| 01 | A | 問題文に一文足すだけで、何が変わるの? | state 8 | 2.6 s | 0:00.0 | K06 |
| 02 | B | open の 10 行は裸の共円 8 行、blocked の 10 行は O1O2 の円 6 行(別の標本)。 | state 8 | 7.4 s | 0:03.0 | K03 K06 K07 K69 |
| 03 | A | そもそも、問題は? | state 0 | 1.2 s | 0:10.9 | K19 |
| 04 | B | X1 から X4 は一つの円の上。O1O2 を直径とする円なら載る。He・Hi を直径とする円には載らない。 | state 1 | 7.3 s | 0:12.6 | K19 |
| 05 | A | 足した一文は、答えを教えているの? | state 3 | 2.3 s | 0:20.3 | K01 K02 |
| 06 | B | いいえ。末尾に 324 字、共円で止まる答えを不十分とし、中心と直径の名指しを求める。O1O2 も He・Hi も 0 件。 | state 3 | 8.4 s | 0:23.1 | K01 K02 |
| 07 | A | 足さない open では? | state 4 | 1.8 s | 0:31.9 | K03 |
| 08 | B | 10 行のうち 8 行の答えの欄が裸の共円。O1O2 を円の直径や中心と名指す文は 0 行。 | state 4 | 6.2 s | 0:34.1 | K03 K04 |
| 09 | A | でも label は attractor が 5 行だよね。 | state 5 | 4.1 s | 0:40.8 | K05 |
| 10 | B | あれは全文の label。本文に He か Hi の語があれば付く。答えの欄で He・Hi の行は 0。 | state 5 | 7.0 s | 0:45.3 | K05 |
| 11 | A | 足すと? | state 8 | 0.5 s | 0:52.7 | K06 |
| 12 | B | bind 7、attractor 3。JSON から書き始めた 3 行は全部 attractor、文から書き始めた 7 行は全部 bind。 | state 8 | 9.5 s | 0:53.7 | K06 K07 |
| 13 | A | 考えたから bind した、ってこと? | state 8 | 2.6 s | 1:03.6 | K07 X01 |
| 14 | B | とは言えない。相関で、n は 10、一つの model、一つの cue。cue を替えれば bind は 2 / 9 から 7 / 10。 | state 11 | 9.3 s | 1:06.7 | K10 X01 X02 |
| 15 | B | 別の標本で並べる。O1O2 の文がある行は open 0・blocked 7、He・Hi の直径の文は open 1・blocked 5。 | state 9 | 9.3 s | 1:16.4 | K08 K09 |
| 16 | A | bind する瞬間は? | state 13 | 1.5 s | 1:26.2 | K11 K12 |
| 17 | B | 同じ一行で、先に He・Hi と書く位置。O の組 +2.74 対 He の組 -7.13、He の皿が重い。 | state 13 | 7.4 s | 1:28.1 | K11 |
| 18 | B | 後で O1O2 の中点と書く位置。O の組 +9.64 対 -8.21、O の皿が重い。L50H23 は両方で He の皿の一番下。 | state 14 | 8.9 s | 1:36.0 | K12 K13 |
| 19 | B | 上位 10 head の重なりは 0.528 対 0.513。同じ部品かは言わない。機構は見ていない。 | state 15 | 6.9 s | 1:45.4 | K14 X03 |
| 20 | A | 他の model は? | state 16 | 1.5 s | 1:52.7 | K17 |
| 21 | B | model ごとに並べる。qwen3:32b は 0 から 1 で、blocked の attractor 7。順位にはしない。 | state 16 | 8.6 s | 1:54.7 | K17 X06 |
| 22 | B | token 329 で O1O2 を中点と名指す前後で、考えの中点の群は 0.10 から 0.93、答えの側は 2.15 から 1.29。右で円が光る。 | state 18 | 10.3 s | 2:03.8 | K23 |
| 23 | B | He・Hi を直径と名指す一行は、差が最大でも 0.16。 | state 19 | 3.9 s | 2:14.5 | K24 |
| 24 | B | 同じ目盛りでも、行の種類が違う。対の比べではない。 | state 20 | 3.4 s | 2:18.9 | K23 K24 X12 |
| 25 | B | O1O2 を名指す 59 行で、考えの中点が上がる行は 48、結びは 9。 | state 21 | 5.0 s | 2:22.7 | K25 |
| 26 | B | He・Hi の 34 行では 11 から 19。結びが立つ予想は 6 / 36 と 17 / 34、どちらも外れた。 | state 21 | 7.8 s | 2:28.1 | K26 K27 |
| 27 | A | 考え始めたってこと? | state 21 | 1.4 s | 2:36.4 | X09 X11 |
| 28 | B | とは言えない。相関で、上がりの大半は本文が計算に移ることと一緒に動く。 | state 21 | 4.7 s | 2:38.2 | X09 X10 X11 |
| 29 | B | O1O2 を名指した後は 48 / 59 で本文が数式に移る。He・Hi の後は 8 / 34。順位相関は 0.78 対 0.21。 | state 23 | 8.9 s | 2:43.4 | K31 K32 |
| 30 | B | 移らない 11 本でも 7 本で小さく上がる。閾に余裕は 0 本、薄い ✓。 | state 24 | 5.1 s | 2:52.8 | K33 X14 |
| 31 | A | bind の数は? | state 25 | 1.2 s | 2:58.4 | K16 K28 |
| 32 | B | 全文の label で 40 対 8、答えの欄の label で 36 対 4。片方だけを bind と書かない。 | state 25 | 7.7 s | 3:00.0 | K16 K28 X01 |
| 33 | B | 札は 12 本。系統樹の中 4・前 6・後 2。札の印を押すと地図へ。 | state 26 | 4.7 s | 3:08.2 | K40 K41 K42 K43 X16 |
| 34 | A | 10-28 の図の後に、家は何を打ったの? | state 27 | 2.8 s | 3:13.4 | K50 |
| 35 | B | 台帳の読みから五つの束。olm76、推論空間の探し、語でない構造、apex の証明、olm128。読んで格に届いた札は 17 本。関門で止まった札は別に 3 本。 | state 27 | 10.9 s | 3:16.7 | K50 |
| 36 | A | 台帳の「まだ答えを閉じていない」は? | state 28 | 2.4 s | 3:28.0 | K51 R04 |
| 37 | B | 答えの欄の手前でも、結びの群は線に届かない。上がった行は bind の 28 / 48、偽の窓は 21 / 48。支持されない読み。 | state 28 | 8.9 s | 3:30.9 | K51 R04 X17 |
| 38 | B | 先読みは、層 32 の残差と J-lens の読み出しでほぼ同じ。0.996 対 0.994。一貫して出る上乗せは k = 8 だけで、+0.022 から +0.041。 | state 30 | 11.5 s | 3:40.3 | K52 K53 X18 X19 |
| 39 | B | 名の直後の形は this circle へ 0.970、this の直前の語へは 0.603。head は指す先の名を 2.37 倍読む。機構は言わない。 | state 31 | 10.4 s | 3:52.2 | K55 K56 X22 |
| 40 | B | 位置を入れ替えると、指しに従う割合は層 16 で半分を割り、組は層 20 で値の側へ。 | state 32 | 5.8 s | 4:03.1 | K57 R08 X23 |
| 41 | A | apex の証明は書ける? | state 33 | 1.8 s | 4:09.4 | K58 |
| 42 | B | 求めても、二等分線から直角、Thales の逆の鎖は 0 / 37。frontier の段を与えると、続きは 26 / 40 と 23 / 40。導きは別。 | state 34 | 10.5 s | 4:11.6 | K58 K59 X24 |
| 43 | A | 次の問いは? | state 35 | 0.8 s | 4:22.5 | K60 |
| 44 | B | 依頼者が選んだ A は olm128 で読んだ。位置 0 の書き始めでは cue の差は説明されない。0.579。他の候補は並べるだけで、採否は依頼者。 | state 35 | 10.3 s | 4:23.8 | K60 K61 R10 X25 |
| 45 | A | 言えないことは? | state 42 | 1.1 s | 4:34.5 | X01〜X27 |
| 46 | B | 考えたから bind した、cue をまたいだ効果、回路、活性が bind を決める、model が確かめた、とは言わない。 | state 42 | 8.4 s | 4:36.1 | X01 X02 X03 X10 X14 X15 |

## Switching the states (a guide for the editor)

| state | starts | headline (A's line shortens this) | the picture |
|---|---|---|---|
| 0 | 0:10.9 | X1〜X4 は一つの円の上(裸の共円) | `captures/video_s00.png` |
| 1 | 0:12.6 | O1O2 の円と He・Hi の円(座標から) | `captures/video_s01.png` |
| 3 | 0:20.3 | blocked = open + 324 字(足した一文を全画面に) | `captures/video_s03.png` |
| 4 | 0:31.9 | 二十行の帯(open を強調・blocked は薄く): open の答えの欄は裸の共円・青の印は 0 | `captures/video_s04.png` |
| 5 | 0:40.8 | 全文の label と答えの欄(三段・糸で結んだ行が色の替わった行) | `captures/video_s05.png` |
| 8 | 0:00.0 | 二十行の帯(blocked を強調・open は薄く): JSON から書き始めた行は橙・文から書き始めた行は青 — 冒頭の芯の一枚 | `captures/video_s08.png` |
| 9 | 1:16.4 | 二つの円の文の数(open の 10 行 → blocked の 10 行・別の標本) | `captures/video_s09.png` |
| 11 | 1:06.7 | cue を替えた三つの積み木 | `captures/video_s11.png` |
| 13 | 1:26.2 | 天秤 ① t 289(He の皿が重い) | `captures/video_s13.png` |
| 14 | 1:36.0 | 天秤 ② t 397(O の皿が重い・L50H23 は He の皿の一番下) | `captures/video_s14.png` |
| 15 | 1:45.4 | 16 の位置 × 上位 10 head の立体 | `captures/video_s15.png` |
| 16 | 1:52.7 | 他の model(並べるだけ) | `captures/video_s16.png` |
| 18 | 2:03.8 | 上の列 = 本文の述語の印・下 = 群の値の推移(S_O): 印の token で O1O2 の円が光る | `captures/video_s18.png` |
| 19 | 2:14.5 | S_H(He・Hi を名指す一行): 差は最大 0.16 | `captures/video_s19.png` |
| 20 | 2:18.9 | 同じ目盛りで並べる(前 32 / 後 32): 青 S_O・橙 S_H | `captures/video_s20.png` |
| 21 | 2:22.7 | 集計の柱(O1O2 の 59 行・He・Hi の 34 行)と予想 Q1・Q2(✗) | `captures/video_s21.png` |
| 23 | 2:43.4 | olm62: 本文が数式に移る割合(O1O2 48 / 59・He・Hi 8 / 34)と、Δ中点 × Δmath の散布(同じ目盛り) | `captures/video_s23.png` |
| 24 | 2:52.8 | 数式に移らない O1O2 の 11 本: 中点 ↑ 7 / 11(薄い ✓・余裕 0 本) | `captures/video_s24.png` |
| 25 | 2:58.4 | cmt5 の二つの label(全文 40 → 答えの欄 36・8 → 4) | `captures/video_s25.png` |
| 26 | 3:08.2 | 札と系統樹: 札 12 本の置き場(中 4・前 6・後 2)と使う状態 | `captures/video_s26.png` |
| 27 | 3:13.4 | 10-28 の図から olm128 までの一本の流れ(札 18 本・斜線の節点 = 後から足した部分) | `captures/video_s27.png` |
| 28 | 3:28.0 | 台帳の読みと olm76: 結びが上がる行 28 / 48(偽の窓 21 / 48) | `captures/video_s28.png` |
| 30 | 3:40.3 | k token 先の E: 上乗せは k = 8 だけ | `captures/video_s30.png` |
| 31 | 3:52.2 | this circle へ移る形と、指す先を読む head | `captures/video_s31.png` |
| 32 | 4:03.1 | 位置の入れ替え: 指しに従う割合が 0.5 を割る層 16(olm106)・値の側へ替わる層 20(olm108) | `captures/video_s32.png` |
| 33 | 4:09.4 | apex の証明の欄: 鎖は 0 / 37 | `captures/video_s33.png` |
| 34 | 4:11.6 | frontier の段を与えた続き: 26 / 40 · 23 / 40 | `captures/video_s34.png` |
| 35 | 4:22.5 | olm128: 書き始め別 × cue 別の blocked の行 | `captures/video_s35.png` |
| 42 | 4:34.5 | 言えない(平叙文)と受け入れの問い | `captures/video_s42.png` |

## Reading guide (for a voice synthesiser)

| written | read as |
|---|---|
| O1O2 | オー・ワン・オー・ツー |
| He・Hi | ヒー・ハイ(点の名) |
| X1〜X4 | エックス・ワン から エックス・フォー |
| L50H23 | エル・ごじゅう・エイチ・にじゅうさん |
| bind / attractor | バインド / アトラクター |
| cue \n\n | キュー・改行二つ |
| Jaccard | ジャッカード |
| qwen3:32b | クウェン・スリー・さんじゅうに・ビー |
| ⟨+2.74⟩ | プラス にてんなな よん |

Caption to add if wanted: "The figure is illustrative. The numbers are copies and counts of frozen values (CLAIMS.md)."

Not on the voice track (cannot say): 考えたから bind した、block の効果を cue をまたいで、O の組 / He の組を回路・担い手と、3・4 章と 5 章を同じ prompt と、open の attractor 5 を答えが He・Hi に向いたと、model を一つの曲線・順位に、model が O1O2 で考え始めた / He・Hi では考えなかった、活性が bind を決める・結びの latent = commit の正体、cmt5 の bind を、どちらの label かを言わずに、計算に移らなくても上がる(薄い ✓)と強く、model が確かめた(「確かめに入る」は本文の形からの読み)。
