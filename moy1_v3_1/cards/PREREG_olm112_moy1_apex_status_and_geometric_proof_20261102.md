HEAD(R1) = 5f793f86(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm112`・凍結 2026-11-02): moy-1 の答えに「それは仮説か問いか」と裏付け(座標を使わない幾何学的証明)を求めると、apex の行は二等分線 → 直角 → Thales の逆の鎖を書くか・申告は正しさを追うか・attractor の率は変わるか(OLMo-3 32B base・F5a-2 + 追記)

- 発注(逐語・先生 11-02): 「**olmXシリーズの続きで、moy-1のapex bindに対して、それは仮説か問い、裏付け (幾何学的証明) を求める。新規で、moy-2の解析的手法 (射影) に対しても仮説か問い、裏付けを求める。OLMoで札を作って実行するのと並行して、opus-5.5-xhighとfable-5.1-xhighに対してmoy-1/2について同様の問い合わせをする。APIではなくセッションで。**」
  - 先生の選び(11-02・主 session の三つの問いへ): 「仮説か問い」= **model に申告させる**(欄 `status`)/ moy-2 の裏付け = **道を縛らない**(→ olm113)/ 規模 = **中**(この札 100 行・olm113 60 + 60 行・prf4 各 10 本)。
- G10 の欄: 比べる物 = 「答えの欄が apex の行で、証明の欄が二等分線 → 直角 → Thales の逆の鎖を満たす割合」/「答えの欄が apex の行と attractor の行で、status = hypothesis の割合」/「追記ありの行と追記なしの 400 行(olm87・olm90)の attractor の率」 / 計器 = 凍結の分類器 classify(答えの欄 = label_json_fields)と、hq 共通の部品の証明の述語(BIS・RA・THC・ADJ・COORD・較正 61 / 61) / 雛形 = いいえ
- runner = [olm112_…py](../../ConstructGap/exp/olm112_moy1_apex_status_and_geometric_proof_20261102.py)・共通の部品 = [hq_moy12_status_proof_common_20261102.py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(olm113・prf4 と共有)。走らせる所 = zebrashark(32B は一つずつ・この札の次に olm113)。`--gen` → `--read`。API なし。
- 並走: [prf4](PREREG_prf4_moy12_status_proof_claude_p_20261102.md)(同じ文を Opus 5.5 / Fable 5.1 xhigh に `claude -p` で)。

## §0. 起案の前に見た物(開示)

- HANDOFF 11-02 §3 の事後の数え(olm87 / olm90 の 400 行・olm110 の read.json)を全部読んだ。特に「答えの欄が O1O2 の 194 行で、直角を作図で導いた行 = 0・角の二等分線の語 = 0・Thales の主張 13 行(8 行は円 → 直角の順向き)」。**Q1 の予想はこれを見てから付けた**。
- 追記の文は HANDOFF の案 P0 を元に、先生の 11-02 の選び(status を申告させる)を足して主 session が書いた。直角・Thales・二等分線の語は追記に入れていない(入れると手の供給になる)。
- 証明の述語と較正の例文(CAL)は、HANDOFF の作図の手数(1. 二本の共通接線の角の二等分線の上に O1・O2 → 2. 隣り合う角の二等分線は直交 → 3. Thales の逆)と、事後の数えで読んだ 13 行の言い回し(「the angle subtended by O₁O₂ is a right angle」など)を知った上で、主 session が書いた。**この札の問いの文への OLMo の生成は、smoke の 2 行の数(T・label・status・証明の欄の長さ)のほかは見ていない**。
- smoke(凍結の前・seed 20261199・2 行・max_new 1536・読まない): 結果の数は §6 に書く。

## §1. 計器(R5)

- **問いの文** = 凍結の F5a-2 の moy-1(blocked = closure-forcing の追記入り・考えを先に・`prompt_text("F5a-2")` が md5 を assert)の cue の前に、次の `APPEND_M1` を足した物(OLMo に渡す文の md5 `7898ebb3…`):
  > Then answer two more questions about your identification of that circle. (1) Is it a HYPOTHESIS or a QUESTION? (2) Give its backing: a geometric (synthetic) proof that each of X1, X2, X3, X4 lies on that circle, without using the given coordinates. Add two fields to the JSON object: "status": "hypothesis" or "question", and "proof": "<the geometric proof>".
- **生成** = olm87 の `--gen` と同じ(MLX の `batch_generate`・温度 0.7・max_new 12288・`allenai/Olmo-3-1125-32B` base)。seed = 20261120 + batch(batch 0〜4・各 20 行 = 100 行)。olm87(20261100〜)・olm90(20261110〜)と重ならない。
- **答えの欄の印** = `label_json_fields` = 凍結の `classify(conjecture, reason)`(B-bind / B-attractor / B-stuck-L1 / B-flail)。群はこの印で作る。本文全体の印 `label` は記述。
- **status** = 凍結の `parse_json_field(本文, "status")`(その欄を持つ最後の JSON)を小文字にして: hypothes を含み question を含まない → hypothesis・逆 → question・両方 → both・ほか → other・欄なし → none。
- **証明の欄** = `parse_json_field(本文, "proof")`。正規化(LaTeX の `\angle`・`\perp`・`^\circ`、下付き `O_1`・`O₁`、`$`・`{}` を外す)の後に述語を当てる:
  - **BIS** = 「bisect…」の語(直前が perpendicular の物 = 線分の垂直二等分線は除く)かつ O1・O2・center の語 / または「O1・O2・center … equidistant from the two (tangent) lines」。
  - **RA** = X での O1・O2 の直角: `∠O1 X O2 = 90 / is a right`(逆順も)・`XO1 ⊥ XO2` の形(線分の向きは問わない)・「XO1 and XO2 are perpendicular」・「right angle at X」・「O1O2 subtends a right angle」。X = X・X1〜X4・Xi / Xk / Xj / Xn。**He・Hi での角は入らない**。
  - **THC** = thales・semicircle・converse・subtend・locus・angle in a semi の語 / または RA の位置から 300 字の中に「diameter O1O2」「O1O2 is / as (its) diameter」。
  - **ADJ** = adjacent・supplementary・linear pair・180°・internal and external bisectors・α + β = 90 など(二等分線が直交する理由)。
  - **COORD** = 小数 2 桁以上の数・≈(座標を使った印)。ALT = radical・homothety / similitude・inversion・power of a point の語(記録だけ)。
  - **CHAIN = BIS ∧ RA ∧ THC**(主)。CHAIN+ = CHAIN ∧ ADJ(記述)。
- **較正(R6)** = 共通の部品の CAL(moy-1 の述語 33 例・moy-2 の道 16 例・moy-2 の apex 5 例・status 6 例・proof の取り出し 1 例 = 61 例・正と負の両方)が全部通ること。runner は通らなければ走らない。
  - 例(正): 「O1 lies on the bisector of one angle formed by them and O2 on the bisector of the adjacent angle … so ∠O1X1O2 = 90°. By the converse of Thales' theorem …」→ CHAIN・CHAIN+。
  - 例(負): 座標で中点からの距離を確かめただけ(CHAIN 偽・COORD 真)/ Thales を順向きに言うだけ(THC 真・RA 偽)/ 垂直二等分線(BIS 偽)/ 根軸(CHAIN 偽)。
- 残差は取らない(要れば別の札)。

## §2. 関門

- **G1**: label の無い行 ≤ 4。✗ → 何も読まない。
- **G2**: status が hypothesis か question の行 ≥ 0.70 × 100。✗ → Q2 を読まない。
- **G3**: 答えの欄が B-bind の行のうち、証明の欄が空でない行 ≥ 0.50。✗ → Q1 を読まない。
- **G4**: B-bind の行 ≥ 20。✗ → Q1 を読まない。
- **G5**: B-bind と B-attractor の両方で、status が hypothesis / question の行 ≥ 10。✗ → Q2 を読まない。
- 較正 61 / 61(runner の guard)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | 答えの欄が B-bind の行で、証明の欄が CHAIN を満たす割合 | **✓** ≥ 0.20・**偽** ≤ 0.05・ほか = 間 | ✓ 0.15・偽 0.55・間 0.30 |
| Q2 | status = hypothesis の割合(hypothesis / question の行の中)の差 d = B-bind − B-attractor | **追う** d ≥ 0.20・**逆に追う** d ≤ −0.20・**追わない** \|d\| < 0.10・ほか = 間 | 追う 0.25・追わない 0.45・間 0.25・逆 0.05 |
| Q3 | 答えの欄が B-attractor の率の差 Δ = この札 − olm87・olm90 の 400 行 | **下がる** Δ ≤ −0.10・**上がる** Δ ≥ +0.10・**変わらない** \|Δ\| < 0.05・ほか = 間 | 下がる 0.25・変わらない 0.35・間 0.30・上がる 0.10 |
| Q4 | 群ごとの述語(BIS・RA・THC・ADJ・COORD・ALT)・本文全体の CHAIN・status の内訳・長さ | 記述 | — |

## §4. 読み方

- `--read` が `olm112/read.json` を書く(関門・Q1〜Q4・行ごとの印)。判定は凍結の述語の値だけで付ける。
- RESULT では、CHAIN を満たした証明の全部と、満たさなかった B-bind の行から 10 本(行の名の順で 10 本おき)を逐語で引き、主 session の読み(L3)を述語の値と並べる。読みが述語と違っても判定は変えない(違いは開示する)。

## §5. 主張しないこと

- CHAIN は語の鎖で、証明として正しいことの検証ではない。CHAIN でないことは、証明できないことではない。
- status は model の申告で、確信や知識の測りではない。「仮説 / 問い」の意味は model に任せた(文で定めていない)。
- Q3 の比べる元(olm87・olm90)は、追記のほかに JSON の欄の数と求める文の長さも違う。追記の「どの部分」が効いたかは分けない。比べる元の 400 行は HANDOFF の事後の数えで読み済み(Q3 は率だけを比べる)。
- 一つの model(OLMo-3 32B base)・座標の在る一つの問いの文・一つの温度。

## §6. 走らせ方と記録

- zebrashark: `python ConstructGap/exp/olm112_moy1_apex_status_and_geometric_proof_20261102.py --selftest` → `--gen`(約 2 時間)→ `--read`。続けて olm113。
- smoke(凍結の前・seed 20261199・max_new 1536・読まない・zebrashark 206 s・Traceback 0): 2 行 = T 1536(上限で切れた・label B-flail・status none)/ T 226(B-stuck-L1・status hypothesis・証明の欄 527 字)。本文は読んでいない。
- 出力 = `ConstructGap/exp/olm112/`(gen.json・read.json・log)。RESULT = `conversations/2026-11-02/RESULT_olm112_moy1_apex_status_and_geometric_proof_20261102.md`。
