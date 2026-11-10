# SCRIPT — a two-voice scene for the video (moy-5 · the roads to the apex · entry_v2_1_received)

- Length: **146.8 s** (characters / 7.4 per second + 0.45 s between lines; written and measured by `make_script.py`). ≤ 150 s.
- The lines that start in the first 10 s (2 lines; the last of them ends at 0:09.6) all cue **state 1** (A1): two real rows of one card, both answer fields on the floor, the roads parting in the reason field — the core. (v1 wrote this as 'the first 10 s … to 0:17.5'; the two readers flagged the mismatch: the 10 s are covered by state 1, and the last line that starts before 10 s ends later.)
- Two voices: **A** = the listener, **B** = the explainer. No real character's name, picture or voice. Each line names the state it cues and the claim ids it rests on (CLAIMS.md). Every number is read from `generated/pack.json`.
- Show the 1920 × 1080 stills `captures/video_s<N>.png` (state 0 also `video_s0a.png` / `video_s0b.png` = P_x moved, drawing only).

| # | voice | line (spoken) | cue (state) | length | start | claims |
|---|---|---|---|---|---|---|
| 01 | A | 同じ問い・同じ model なのに、答えが二つとも同じ。何が違うの? | state 1 | 4.6 s | 0:00.0 | — |
| 02 | B | 答えの欄はどちらも床 EJ = KP_y。理由の欄に書いた道が違う。 | state 1 | 4.6 s | 0:05.0 | K060, K061 |
| 03 | B | 左は焦点・準線で閉じた行(10 本中 10)。右は近道を塞いだ行で、頂点の比例中項から式へ(10 本中 10・壊れの印 1 本を含む)。 | state 1 | 9.2 s | 0:10.1 | K058, K052 |
| 04 | A | そもそも、どんな問い? | state 0 | 1.5 s | 0:19.7 | — |
| 05 | B | 円と接線から点 P_y を作り、P_x がどこでも成り立つ関係を一つ答える。答えの板は最初は空。 | state 0 | 6.5 s | 0:21.7 | K105 |
| 06 | B | 手がかりごとに Opus と Fable を一本ずつ。濃い青が答えの欄、淡い青が全体。 | state 4 | 5.8 s | 0:28.6 | K150 |
| 07 | A | 何も足さないと? | state 5 | 1.1 s | 0:34.9 | — |
| 08 | B | 問いだけでは四つの model とも全体の cut が 0。Opus の K では全体 20 本中 20 で、計器は立つ。 | state 5 | 8.2 s | 0:36.4 | K001, K099 |
| 09 | A | どうすれば答えの欄に出る? | state 8 | 1.8 s | 0:45.1 | — |
| 10 | B | 問いの点の集合を一行替えると、答えの欄に Opus 7、Fable 20(20 本中)。 | state 8 | 5.9 s | 0:47.3 | K021, K026 |
| 11 | B | 同じ札 neq6 の中で、Opus の答えの欄は medium 0 から max 19。thinking の量は結果の記述。 | state 10 | 8.4 s | 0:53.7 | K029, K033 |
| 12 | B | 理由を求める一文 β′ では理由の欄に cut の在る行が Opus 6、Sonnet 2、Fable 0。答えの欄は 0。 | state 12 | 8.4 s | 1:02.5 | K010, K013 |
| 13 | B | 近道を塞ぐと、Opus は 10 本中 10 が頂点の比例中項を書いた。Fable は 4、壊れた出力を除くと 4 / 8。 | state 18 | 8.4 s | 1:11.3 | K052, K056 |
| 14 | B | Argon の thinking は、行の数えで Claude の 3.8〜8.3 倍。SUMMARY の 3.8〜8.2 倍は真ん中二本の上の値。 | state 14 | 10.0 s | 1:20.2 | K365 |
| 15 | B | Menaechmus の説明だけで、Fable は理由の欄に頂点の形を 5 本。答えの欄は 0。 | state 21 | 6.5 s | 1:30.6 | — |
| 16 | B | OLMo-3 32B は問いだけでは床にも 20 本中 0〜5。この地図の外。 | state 22 | 5.3 s | 1:37.6 | K086, K092 |
| 17 | A | その後は? | state 23 | 0.7 s | 1:43.3 | — |
| 18 | B | 家は OLMo の内側で frontier の道を読む札を 20 本打った。格は判定 9、記述 4、較正 0、言えない 2、関門で止まった 5。足して 20。 | state 23 | 10.7 s | 1:44.4 | K357 |
| 19 | B | cut の文の手前 32 token で、OLMo の言語空間は、同じ行の別の文の手前より、床の答えの語に比べて CUT の語の側へ寄る。192 / 288。 | state 25 | 10.7 s | 1:55.5 | K296 |
| 20 | B | 自分の語で測る計器は、関門や統制で止まって閉じた。 | state 25 | 3.4 s | 2:06.7 | K417 |
| 21 | B | 読み手が出した次の束は五つ。家が打つのは束 ①、thinking の量。 | state 27 | 4.9 s | 2:10.5 | K321, K422 |
| 22 | B | その寄りの過半は語の積み上がり。ここは読みで、採否は依頼者。 | state 30 | 4.1 s | 2:15.8 | K415 |
| 23 | B | 言えないこと。開いた条件で着かないのが「選ばない」のか「引き金が無い」のかは、腕で分けていない。 | state 29 | 6.5 s | 2:20.3 | K126 |

## Switching the states (a guide for the editor)

| state | starts | picture |
|---|---|---|
| 1 | 0:00.0 | `captures/video_s1.png` |
| 0 | 0:19.7 | `captures/video_s0.png` |
| 4 | 0:28.6 | `captures/video_s4.png` |
| 5 | 0:34.9 | `captures/video_s5.png` |
| 8 | 0:45.1 | `captures/video_s8.png` |
| 10 | 0:53.7 | `captures/video_s10.png` |
| 12 | 1:02.5 | `captures/video_s12.png` |
| 18 | 1:11.3 | `captures/video_s18.png` |
| 14 | 1:20.2 | `captures/video_s14.png` |
| 21 | 1:30.6 | `captures/video_s21.png` |
| 22 | 1:37.6 | `captures/video_s22.png` |
| 23 | 1:43.3 | `captures/video_s23.png` |
| 25 | 1:55.5 | `captures/video_s25.png` |
| 27 | 2:10.5 | `captures/video_s27.png` |
| 30 | 2:15.8 | `captures/video_s30.png` |
| 29 | 2:20.3 | `captures/video_s29.png` |

## Reading guide (for a voice synthesiser)

| written | read as |
|---|---|
| EJ = KP_y | イー・ジェイ イコール ケー・ピー・ワイ |
| P_x / P_y | ピー・エックス / ピー・ワイ |
| apex | エイペックス |
| β′ | ベータ・プライム |
| cut | カット |
| effort / thinking | エフォート / シンキング |
| Menaechmus | メナイクモス |
| OLMo | オルモ |

Caption to add if wanted: 「図は説明用。数は凍結した出力の欄の写しと数え。」
