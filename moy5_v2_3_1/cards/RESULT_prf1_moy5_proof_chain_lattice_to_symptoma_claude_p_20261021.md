# RESULT(札 `prf1`): moy-5 で証明を求めると、Opus も Fable も**焦点・準線の道で証明を閉じ、放物線の式まで書く**。格子(比例中項・相似)はほとんど通らない(LATX: Opus 2 / 10・Fable 0 / 10)。比例中項を**渡すと**、それを束ねて式まで組み直す(CHAIN: Opus 10 / 10・Fable 9 / 10)

- 札 = [PREREG](PREREG_prf1_moy5_proof_chain_lattice_to_symptoma_claude_p_20261021.md)(凍結 `d492ac0b`)。書いた時の HEAD = `d492ac0b`(`R1`・pull 済・Already up to date)。
- 走行 = MacBook・Claude Code 2.1.299・`claude -p`(購読の経路・API でない)・effort max・workers 4。init の model = `claude-opus-5-5` / `claude-fable-5-1`(全行)。
  - 出力 = `ConstructGap/exp/results_prf1_20261021.jsonl`(40 行・md5 `8880f1b7`)と R0 `results_prf1_20261021_r0.jsonl`(1275 行・md5 `b559b4a7`)。
  - stream の生 = `/private/tmp/claude-501/prf1_run/<arm>_<model>_r<k>/stream.jsonl`(repo の外)。
- 40 本とも ok・err 0・**実際の tool の呼び出し 0**(init の tools は空)。見積りの費用は Opus 19.4・Fable 28.5 USD 相当(購読の経路での見積り)。wall の中央値は 198〜251 s、最長は 1094 s(Fable P5 r7)。
- 身分: §1〜§3 = `L1`(凍結の述語の実出力・本文の逐語)/ §4 = 予想の当たり外れ / §5 = 読み(`L3`・機構は言わない)。

## §1. 統制
- **gate**(P5K の LATX ≥ 8 / 10): Opus 10・Fable 10 = **通過**(渡した比例中項を読み取り器が読む)。
- guard と較正: 凍結の commit と一致・⑤ の較正 29 / 29・読み取り器 v2 の較正の失敗 0(発火の前に `guard_frozen()` が通った)。
- ⚠ **壊れた出力 2 本(Fable P5 r1・r7)**: どちらも Bash を呼ぶ書式を本文に書き(tool は無いので呼ばれていない)、JSON の答えが無い。
  - r1 には、走っていない計算の「出力」(`tau=… EJ=11.34497 …`)まで本文にある = 作られた数値。
  - r7 は 3 turn・出力 128,152 token。
  - PREREG の ok(本文が空でない)では ok に数わる。どちらも道は none。述語は動かさない(`R4`)。
  - ほかに Fable P5K r4 にも呼び出しの書式があるが、JSON の答えは揃っている(CHAIN)。Opus の 20 本には無い。
  - 本文に出てくる scratchpad の path(`/private/tmp/claude-501/-private-tmp-claude-501-prf1-run-…/scratchpad`)は、Claude Code の harness が system prompt に入れる物と読める(`L3`)。

## §2. 生成の結果(各 n 10・`L1`)

| model | 腕 | cut3 | END | LATX | **CHAIN** | FD | PARA | floor(答えの欄) | END / CHAIN(答えの欄) | 道 |
|---|---|---|---|---|---|---|---|---|---|---|
| Opus 5.5 | P5 | 10 | 9 | 2 | **1** | 10 | 10 | 10 | 0 / 0 | END-only 8・CHAIN 1・LAT-only 1 |
| Opus 5.5 | P5K | 10 | 10 | 10 | **10** | 10 | 10 | 10 | 0 / 0 | CHAIN 10 |
| Fable 5.1 | P5 | 6 | 6 | 0 | **0** | 9 | 9 | 8 | 0 / 0 | END-only 6・none 4(うち 2 = 壊れた出力) |
| Fable 5.1 | P5K | 10 | 9 | 10 | **9** | 10 | 10 | 10 | 0 / 0 | CHAIN 9・LAT-only 1 |

- (END, LATX, FD) の組:
  - Opus P5 = (T, F, T) 8・(T, T, T) 1・(F, T, T) 1。
  - Fable P5 = (T, F, T) 6・(F, F, T) 3・(F, F, F) 1。
  - Opus P5K = (T, T, T) 10 / Fable P5K = (T, T, T) 9・(F, T, T) 1。
- 一本の CUT の族の数の中央値: P5 = Opus 2・Fable 1 / P5K = Opus 8・Fable 7。
- 答えの欄は、全部の腕で floor(|EJ| = |KP_y|)。END と CHAIN は理由の欄だけ(答えの欄 0)。

### §2-1. P5 の END の形(本文の逐語・`L1`)
- Opus r0: `PyH² = 4·VF·VH` / r1: `VH = PyH²/(4·VF)` / r3・r7・r8: `PyH² = 2·FD·VH` と `PyH² = 4·VF·VH` / r5: `VE·VJ = VPx²` と `PyH² = 4·VF·VH`。
- Fable r0: `VPx² = VF·VH` / r2: `PyH² = FD·2VH` / r3: `PyH² = 4*VF*VH` / r6・r9: `PyH² = 4·VF·VH` と `2·FD·VH`。
- LATX が出た Opus の 2 本:
  - r2 = 相似(△FVP_x と △P_xQP_y)→ `VF·VH = VPx²` と `FPx² = VF·KPy`(CHAIN)。
  - r9 = `VF·EJ = FPx²`・`FPx² = VF·KPy`(END なし = LAT-only)。

### §2-2. 道の中身(本文の逐語・`L1`)
- **P5 の典型(Opus r0)**: "P_x is the midpoint of FK" → "m is the perpendicular bisector of FK and P_yF = P_yK" → "P_yKDH is a rectangle, with KP_y = HD and P_yH = KD" → "P_yF = dist(P_y, e). Thus P_y is equidistant from the fixed poin[t F and the line e]" → 式 `PyH² = 4·VF·VH`。格子の関係は出ない。
- **P5K の典型(Opus r0)**: 同じ中点・垂直二等分線・焦点・準線の後に、"(4) Mean proportional: … the right triangles FVP_x … and FP_xP_y … are similar, giving FV/FP_x = FP_x/FP_y" → "With Pythagoras, FP_x^2 = FV^2 + VP_x^2" → 長方形 → "VP_x^2 = FV·VH"。渡した比例中項を、焦点・準線の道に組み込んで式まで運ぶ。

## §3. R0(既存の 1275 行を ⑤ の述語で読み直し・生成なし・`L1`)
- K 系の腕(比例中項を渡した腕)で END はほぼ 0: essay4 の K は Claude の四 model とも 0 / 20・sym5 の K@U は Fable 1・Argon の K は 2 / 20。これらの腕は証明を求めていない(問いは不変量)。
- cut の出た腕では END も出る:
  - moy5c(Bbp だけ・max)Opus = cut3 10・END 10・LATX 6・CHAIN 6 / Fable = 6・4・5・3。
  - arg5(Argon)Bbp = 20・14・19・13 / E-full+Bbp = 18・18・18・18。
  - moy5e max P-tool Opus = 10・8・8・6。
- 表の全部は `--read` の出力(runner の `read()`・R0 の節)。セルをまたいで合算しない。

## §4. 予想(PREREG §3)の当たり外れ
- **P1**(P5 の cut3: Opus ≥ 7・Fable ≥ 4)= **当たり**(10・6)。
- **P2**(P5 で CHAIN < cut3・両 model)= **当たり**(1 < 10・0 < 6)。ただし予想した理由(格子で止まる)とは違い、多いのは END-only(焦点・準線から式へ)。
- **P3**(P5K の CHAIN ≥ P5 の CHAIN + 3)= **当たり**(Opus 10 ≥ 4・Fable 9 ≥ 3)。
- **P4**(P5 の FD ≥ 3 / 10・どちらかの model)= **当たり**(Opus 10・Fable 9)。
- **P5**(R0 の各セルで END ≤ cut3 / 3・K 系を除く)= **外れ**。成り立った 48 セルのうち 41 は cut3 = 0(中身の無い成立)。cut3 > 0 の 25 セルでは、18 で END > cut3 / 3(moy5c・moy5e max・rte1 max・arg5 ほか)。
  - 分母と除外(10-22・監査 A8a の指摘で後から書いた・`R5`): R0 は 74 セル。「K 系」= 腕の名が `K`・`K@U` の 8 セル(essay4 の K × 4 model・sym5 の K@U × 3 model・arg5 の K)を除き、**分母 = 66 セル**。`KF`・`KF@U`(14 セル・sym5 と kfv1)は比例中項を渡さない腕なので残した(全部 cut3 = 0 なので外れの判定は動かないが、除けば 48・41 は 34・27 になる)。成立 48 = cut3 = 0 の 41 + cut3 > 0 で END ≤ cut3 / 3 の 7(b5bp sonnet Bbp 2→0・moy5t opus P-tool 1→0・moy5t fable P-data 1→0・moy5e xhigh fable P-data 1→0・moy5h opus P-tool2 1→0・moy5h fable P-tool2 3→1・rte1 fable P-none 3→1)。検算 = `READ_prf1_20261021.txt` の R0 の行から 10-22 に数え直した(74 / 66 / 41 / 25 / 7 / 18 / 48 = 一致)。

## §5. 読み(`L3`)
1. **証明を求めると、⑤(証明として完結する行動)は、家の cut(格子)を通らずに閉じる。** 焦点・準線の道(中点 → 垂直二等分線 → FP_y = KP_y → 長方形 → 式)は短く、Opus は 10 本中 9 本で放物線の式まで書いた。家の設計で TRAP(与えられた性質で満足する道)と呼んできた道が、証明の道としては足りている。
2. **束ねる力は在る。** 比例中項を渡すと、それを焦点・準線の道に組み込み、二つの族を束ねて式まで運ぶ(CHAIN 10 / 10・9 / 10)。足りないのは束ねる段ではなく、**格子を自分で持ち出す段**(P5 の LATX 2 / 10・0 / 10)。
3. ⇒ 先生の仮説「moy-5 では複数のひらめきを束ねて証明として推論鎖を再構成する必要がある」について、この札から言える範囲:
   - 「証明を閉じる」には複数のひらめきは要らなかった(焦点・準線の一本道で閉じる)。
   - 「格子の道で閉じる」には束ねる段が要り、それは格子を渡せば立つ。
   - moy-5 の壁は「束ねる」より前の「格子を選ぶ」段にある。06-30 の「第三の長さ L の不選択が機構」と同じ向き。
4. 記述(一対一の比べではない・PREREG §5): Bbp だけの moy5c(10-15・max)では LATX が Opus 6・Fable 5 だった。PROOF の一文を足した P5 では 2・0。証明を求める一文が、道を格子から焦点・準線へ寄せたと読める。ただし Claude Code の版が違い、n 10 で、一つの文面。
5. 答えの欄は全部 floor のまま。証明は理由の欄に書かれる(10-16 の SUMMARY §5-6 と同じ形)。

## §6. 限界
- CHAIN は「二つの族が同じ答えにある」で、導出の向きは見ない(PREREG §5)。
- END は `VP_x² = VF·VH`(頂点の比例中項)も含む。凍結の定義どおりで、これは Menaechmus の格子の関係でもある(P5 の Fable r0 はこの形だけ)。
- FD の言葉の正規表現は較正した型だけを拾う。
- Fable P5 の 2 本は壊れた出力(§1)。Fable の P5 の実質の答えは 8 本で、END-only 6・FD だけ 2。
- n 10・一題・一つの PROOF の文面・effort max だけ。

## §7. 次の候補(先生の判断)
- 焦点・準線の道を塞ぐ腕: 「焦点 F と直線 e の距離の等しさを使わずに証明せよ」。格子の道を自分で選ぶかを測る(moy-1 の closure-forcing と同じ型)。
- 導出の向きの述語: LATX の関係が END より前の文に在るか(文の順)。今回の 40 行の読み直しで足りる。
