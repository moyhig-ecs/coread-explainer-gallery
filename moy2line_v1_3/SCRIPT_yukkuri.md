# SCRIPT — a two-voice scene for the video (札 Q v1.3, 2026-11-04 夕)

- Length: **149.2 s** in all (characters / 7.4 per second + 0.45 s between lines; written by `make_script.py` from `generated/pack.json`). ≤ 150 s. The first 10 s (lines 01–02) are state 0, the scene: the two real rows of olm125 (the same kind of calculation — S1 reflected Th, S2 reflected Tc — the same reject, different proof fields; v1.2 G1). The drafting board (what is true and false in the figure) follows at state 1 (v1.1 F2).
- Two voices: **A** = the listener (asks), **B** = the explainer. No real character's name, picture or voice. Each line names the state it cues and the claim ids (CLAIMS.md) it rests on.
- Words the script does not use: the model thought / understood / noticed / hesitated; "fixed" for olm127's zero; an order of the three sentences; a flat "分けられない" (v1.2 G7: 1 of the 7 Fisher pairs lies below 0.05).
- **状態 8 は行を選ぶ道具。動画は 11〜13(述語に当たる行だけ灯す)を使う**(v1.2 G12)。状態 8 の 420 本の全点灯は、読者が行を選ぶための頁で、台本は cue しない。
- The cues are **not in state order** (6 → 4 → 9: the rates first, then why two arms have no verdict, then the Fisher reference). v1.2 G12 added one line each for state 10 (the denominators) and state 15 (the round trip of the olm118 Q3 band). v1.3 H3: the state-6 line now says the band words (0.108 = olm124's band 戻る, 0.225 = olm125's band 上がる; the edges are each card's PREREG, printed on states 5 / 6); to stay ≤ 150 s the state-10 and state-15 lines were shortened. v1.3 H1: the state-13 line says 「数値で退けた」.

| # | voice | line (spoken) | cue (state) | length | start | claims |
|---|---|---|---|---|---|---|
| 01 | A | 同じ問いの文の二行。どちらも折り返しを計算して退けた？ | state 0 | 3.6 s | 0:00.0 | K68 · K69 |
| 02 | B | はい。二行とも本文で Not the same と書く。でも二行のうち、証明の欄に O1O2 についての対称を書いたのは b1_j17 だけ(主語は接線)。 | state 0 | 10.5 s | 0:04.0 | K68 · K43 · K90 · K115 · K116 |
| 03 | A | 図で、何が真で何が偽？ | state 1 | 1.5 s | 0:15.0 | K71 |
| 04 | B | 等距離 O3Tc = O3Th は真で、どちらも 3.842。Th を O1O2 で折り返しても Tc には着かない。だから「接点は O1O2 について対称」は偽。 | state 1 | 11.1 s | 0:16.9 | K71 · K73 |
| 05 | A | 腕ごとに、何が違うの？ | state 2 | 1.5 s | 0:28.5 | K83 |
| 06 | B | 問いの文の Tool の段だけ。式だけ、式に宣言の文、式に指示の文。 | state 2 | 4.6 s | 0:30.4 | K83 |
| 07 | A | 証明の欄の線対称の率は？ | state 6 | 1.6 s | 0:35.5 | K04 |
| 08 | B | 道具なし 0.122、式だけ 0.108 と 0.108、宣言の文 0.318、指示の文 0.225。指示の文の二回目は判定なしで、参考 0.086。0.108 は olm124 の帯で 戻る、0.225 は olm125 の帯で 上がる。境は札ごとの PREREG。 | state 6 | 18.1 s | 0:37.5 | K04 · K07 · K08 · K06 · K09 · K10 · K20 · K22 · K33 · K110 · K112 |
| 09 | A | 判定なし、って？ | state 4 | 1.1 s | 0:56.1 | K17 |
| 10 | B | 取れた行 0.75 以上が関門。45 / 60 は境ちょうど、二回目は 40 / 60 で落ちた。 | state 4 | 6.6 s | 0:57.6 | K14 · K15 |
| 11 | B | 隣り合う腕の Fisher は参考。7 対のうち 6 対は 0.05 の上、1 対、olm127 対 olm119 は下。判定ではなく、多重比較は補正していない。 | state 9 | 10.9 s | 1:04.7 | K79 · K91 · K108 |
| 12 | B | 計算した行で数えると、退けは olm119 が 10 / 13(全行 11)、olm122 が 5 / 12(全行 6)、四腕で 42 / 56。 | state 10 | 9.9 s | 1:16.0 | K78 · K88 |
| 13 | A | 計算した行は、折り返しを退ける？ | state 11 | 2.2 s | 1:26.4 | K36 |
| 14 | B | olm125 では計算した 18 本のうち 15 本が退ける。18 本の最終の conjecture の類は、等距離 9、OTHER 4、JSON なし 5、共線 0。 | state 11 | 11.4 s | 1:29.0 | K39 · K48 · K49 · K50 · K89 |
| 15 | A | 退けた後の、証明の欄は？ | state 12 | 1.6 s | 1:40.9 | K43 |
| 16 | B | 線対称に戻る行が 3 本。二回目は 0 本だが、退けた 6 本のうち 5 本は上限で証明の欄に届かない。直ったとは言わない。 | state 12 | 8.4 s | 1:42.9 | K43 · K45 · K87 |
| 17 | B | 数値で退けた命題を次の候補に出し続ける行もある。b2_j08 は 343 回、b1_j13 は 542 回。 | state 13 | 7.3 s | 1:51.8 | K66 · K67 |
| 18 | B | 計器を直す間に、olm118 Q3 の帯は 変わらない → 間 → 間 → 変わらない と往復した。 | state 15 | 6.8 s | 1:59.5 | K61 · K60 |
| 19 | A | 計器を替えたら、判定は変わる？ | state 16 | 2.0 s | 2:06.8 | K62 |
| 20 | B | v6 で率は最大 +0.054 動く。でも凍結の判定は 7 / 7 同じ。 | state 16 | 5.0 s | 2:09.2 | K62 · K63 |
| 21 | B | 凍結の判定で言えるのは、式だけは戻る(一回目は参考)、宣言の文は上がる、指示の文は一回目 上がる・二回目は関門に落ちて判定なし = 二回で立たない、まで。答え合わせは在るが読みは無い、は主 session の読み。 | state 19 | 14.5 s | 2:14.7 | K20 · K21 · K22 · K17 · K114 |

## Switching the states (a guide for the editor)
The order below is the order of the cues, **not the state numbers** (6 → 4 → 9; states 3, 5, 7, 8, 14, 17, 18 are not cued; state 8 is the row-picking tool).
| state | starts | video 1920 × 1080 | desk (1440, dark) | phone (390, dark) |
|---|---|---|---|---|
| 0 | 0:00.0 | `captures/video_s0.png` | `captures/page_dark_s0.png` | `captures/phone_dark_s0.png` |
| 1 | 0:15.0 | `captures/video_s1.png` | `captures/page_dark_s1.png` | `captures/phone_dark_s1.png` |
| 2 | 0:28.5 | `captures/video_s2.png` | `captures/page_dark_s2.png` | `captures/phone_dark_s2.png` |
| 6 | 0:35.5 | `captures/video_s6.png` | `captures/page_dark_s6.png` | `captures/phone_dark_s6.png` |
| 4 | 0:56.1 | `captures/video_s4.png` | `captures/page_dark_s4.png` | `captures/phone_dark_s4.png` |
| 9 | 1:04.7 | `captures/video_s9.png` | `captures/page_dark_s9.png` | `captures/phone_dark_s9.png` |
| 10 | 1:16.0 | `captures/video_s10.png` | `captures/page_dark_s10.png` | `captures/phone_dark_s10.png` |
| 11 | 1:26.4 | `captures/video_s11.png` | `captures/page_dark_s11.png` | `captures/phone_dark_s11.png` |
| 12 | 1:40.9 | `captures/video_s12.png` | `captures/page_dark_s12.png` | `captures/phone_dark_s12.png` |
| 13 | 1:51.8 | `captures/video_s13.png` | `captures/page_dark_s13.png` | `captures/phone_dark_s13.png` |
| 15 | 1:59.5 | `captures/video_s15.png` | `captures/page_dark_s15.png` | `captures/phone_dark_s15.png` |
| 16 | 2:06.8 | `captures/video_s16.png` | `captures/page_dark_s16.png` | `captures/phone_dark_s16.png` |
| 19 | 2:14.7 | `captures/video_s19.png` | `captures/page_dark_s19.png` | `captures/phone_dark_s19.png` |

## Every state's stills by name (folder `captures/`; v1.1 F8)
| state | heading | video | desk dark | phone dark | also |
|---|---|---|---|---|---|
| 0 | A0 場面 — 同じ種類の計算(折り返しを数値で出して退けた・S1 は Th を、S2 は Tc を折り返した)・違う証明の欄 | `video_s0.png` | `page_dark_s0.png` | `phone_dark_s0.png` | `page_light_s0.png` · `page_dark_s0_en.png` · `video_en_s0.png` |
| 1 | A1 場面 — 問いの図と読み方 | `video_s1.png` | `page_dark_s1.png` | `phone_dark_s1.png` | `page_light_s1.png` · `page_dark_s1_en.png` · `video_en_s1.png` |
| 2 | B0 道具の段 — 三種の文(逐語) | `video_s2.png` | `page_dark_s2.png` | `phone_dark_s2.png` | — |
| 3 | B1 計器 — 語の印と較正 | `video_s3.png` | `page_dark_s3.png` | `phone_dark_s3.png` | — |
| 4 | B2 関門 G1 — 取れた行 ≥ 0.75 | `video_s4.png` | `page_dark_s4.png` | `phone_dark_s4.png` | — |
| 5 | B3 判定の帯 — 札ごとの規則 | `video_s5.png` | `page_dark_s5.png` | `phone_dark_s5.png` | — |
| 6 | C0 七腕の表 — 一つの目盛り | `video_s6.png` | `page_dark_s6.png` | `phone_dark_s6.png` | `page_light_s6.png` · `page_dark_s6_en.png` · `video_en_s6.png` |
| 7 | C1 七腕の表 — ほかの列 | `video_s7.png` | `page_dark_s7.png` | `phone_dark_s7.png` | — |
| 8 | C2 七腕の表 — 積み木の棚(行を選ぶ) | `video_s8.png` | `page_dark_s8.png` | `phone_dark_s8.png` | `page_light_s8.png` · `page_dark_s8_en.png` · `video_en_s8.png` · `video_s8a.png` · `video_s8b.png` (the drag) |
| 9 | C3 七腕の表 — 隣り合う腕の Fisher(参考) | `video_s9.png` | `page_dark_s9.png` | `phone_dark_s9.png` | `page_light_s9.png` · `page_dark_s9_en.png` · `video_en_s9.png` |
| 10 | D0 計算した行 — 分けて数える | `video_s10.png` | `page_dark_s10.png` | `phone_dark_s10.png` | — |
| 11 | D1 計算した行 — 退けた後の類 | `video_s11.png` | `page_dark_s11.png` | `phone_dark_s11.png` | — |
| 12 | D2 計算した行 — b2_j07 の型 | `video_s12.png` | `page_dark_s12.png` | `phone_dark_s12.png` | `page_light_s12.png` |
| 13 | D3 計算した行 — 戻り続ける行(olm127) | `video_s13.png` | `page_dark_s13.png` | `phone_dark_s13.png` | `video_en_s13.png` |
| 14 | E0 見た形 / 見ていない形 — 等半径の対照 | `video_s14.png` | `page_dark_s14.png` | `phone_dark_s14.png` | — |
| 15 | F0 計器の系譜 — v3 → v6 | `video_s15.png` | `page_dark_s15.png` | `phone_dark_s15.png` | `page_light_s15.png` · `page_dark_s15_en.png` |
| 16 | F1 計器の系譜 — 判定は計器の形に依らない | `video_s16.png` | `page_dark_s16.png` | `phone_dark_s16.png` | — |
| 17 | G0 次の問い — 先生の問い | `video_s17.png` | `page_dark_s17.png` | `phone_dark_s17.png` | — |
| 18 | G1 次の問い — 候補(採否は先生) | `video_s18.png` | `page_dark_s18.png` | `phone_dark_s18.png` | — |
| 19 | H 台帳 — 言える / 記述 / 読み / 言えない | `video_s19.png` | `page_dark_s19.png` | `phone_dark_s19.png` | `page_light_s19.png` · `page_dark_s19_en.png` · `video_en_s19.png` |

## Reading guide (for a voice synthesiser)
| written | read as |
|---|---|
| O1O2 | オー・イチ・オー・ニ |
| O3Tc / O3Th | オー・サン・ティー・シー / オー・サン・ティー・エイチ |
| Tc / Th | ティー・シー / ティー・エイチ |
| b1_j17 | ビー・イチ・ジェイ・イチナナ |
| v6 | ブイ・ロク |
| JSON | ジェイソン |

Caption to add if wanted: 「図は説明用。数は凍結した札の出力の写しと数え直し。計器は書いた語の印で、証明の正しさは読まない。」
