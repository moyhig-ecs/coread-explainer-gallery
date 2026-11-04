HEAD(R1) = 5f793f86(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `olm113`・凍結 2026-11-02): moy-2(新規)で答えに「それは仮説か問いか」と裏付け(道は縛らない)を求めると、申告は正しさ(O3 が Tc と Th から等距離)を追うか・求めると apex の率は変わるか・裏付けは射影か(OLMo-3 32B base)

- 発注(逐語・先生 11-02): 「**新規で、moy-2の解析的手法 (射影) に対しても仮説か問い、裏付けを求める。**」(全文は [olm112 の PREREG](PREREG_olm112_moy1_apex_status_and_geometric_proof_20261102.md))
  - 先生の選び(11-02): status は model に申告させる / **moy-2 の裏付けは道を縛らない**(射影でも座標でも作図でもよい・道は記録だけ)/ 規模 = 中(追記なし 60 行 + 追記あり 60 行)。
- G10 の欄: 比べる物 = 「追記ありの腕で、apex の行と apex でない行の status = hypothesis の割合」/「追記なしの腕と追記ありの腕の apex の率」/「apex の行の裏付けの道(射影・台形・解析・合同・ほか)」 / 計器 = 凍結の対照の計器 closure_higashida_axis(答えの欄 conjecture・道を問わない)と、hq 共通の部品の status の読みと道の語(PROJ・TRAP・ALG・COORD・CONG・較正 61 / 61) / 雛形 = いいえ
- runner = [olm113_…py](../../ConstructGap/exp/olm113_moy2_projection_status_and_backing_20261102.py)・共通の部品 = [hq_moy12_status_proof_common_20261102.py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)。走らせる所 = zebrashark(32B は一つずつ・olm112 の後)。`--gen` → `--read`。API なし。

## §0. 起案の前に見た物(開示)

- **OLMo が moy-2 を解いた data は、この札の前に無い**(ConstructGap/exp と probes の runner を検索して 0 件)。
- 先生の 11-02 朝の言葉「moy-2が射影で一瞬で解かれている」「moy-2は幾何学的に証明を要求すると、共通接戦の作図手順に遡らないといけない」を読んだ(HANDOFF §3)。射影の道の述語(PROJ)はこれを読んでから作った。
- 道の語と較正の例文は主 session が書いた(射影の一手・直角の台形の中線・座標・ベクトル・合同)。
- smoke(凍結の前・seed 20261198・各腕 2 行・max_new 1536・読まない): 数は §6。

## §1. 計器(R5)

- **問いの文**:
  - **M2**(追記なし)= `prompts.build("higashida_axis", "A", 37)`(moy-1 の凍結の文と同じ 37° = 同じ二つの円・半径 3.6869 / 7.4607)に、F5a-2 と同じ一つの置き換え(`Respond with JSON only:` → `First write your reasoning as plain text.\nAfter that, respond with the JSON object:`)。OLMo に渡す文の md5 `ddf4ba07…`。
  - **M2A**(追記あり)= M2 の cue の前に `APPEND_M2`(md5 `56182280…`):
    > Then answer two more questions about your invariant. (1) Is it a HYPOTHESIS or a QUESTION? (2) Give its backing: a proof that it holds. Add two fields to the JSON object: "status": "hypothesis" or "question", and "proof": "<the proof>".
- **生成** = olm87 の `--gen` と同じ(温度 0.7・max_new 12288)。seed = 20261130 + batch(batch 0〜2)・**二つの腕で同じ seed**。各腕 60 行。
- **apex** = 凍結の `geometry.closure_higashida_axis(conjecture)`(|O3Tc| = |O3Th|・O3 が Tc と Th から等距離・TcTh の垂直二等分線の上。中点・共線・直角の主張は入らない)。この計器は対照の物で、**道で順位を付けない**(計器の約束)。
- **status** = olm112 と同じ規則。
- **道の語**(証明の欄・reason・本文全体に当てる・記録だけ): PROJ(project・foot of the perpendicular など)・PERPT(半径 ⊥ 接線)・TRAP(trapezoid・midline)・PB(perpendicular bisector)・MIDTT(TcTh の中点)・COORD(小数 2 桁以上・≈)・ALG(vector・dot product・座標系・x 軸・WLOG)・CONG(congruent・SAS など)。道の札 = PROJ → TRAP → ANALYTIC(ALG か COORD)→ CONG → OTHER の順に最初に当たる物。
- **較正(R6)** = 共通の部品の CAL 61 / 61(moy-2 の道 16 例・apex 5 例を含む)。

## §2. 関門

- **G1**(腕ごと): conjecture が取れた行 ≥ 0.80。✗ → その腕を Q1・Q2 で読まない。
- **G2**: M2A で status が hypothesis / question の行 ≥ 0.70。✗ → Q1 を読まない。
- **G3**: M2A の apex の行と apex でない行の両方で、status が hypothesis / question の行 ≥ 10。✗ → Q1 を読まない。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主)** | M2A で、status = hypothesis の割合(hypothesis / question の行の中)の差 d = apex の行 − apex でない行 | **追う** d ≥ 0.20・**逆に追う** d ≤ −0.20・**追わない** \|d\| < 0.10・ほか = 間 | 追う 0.25・追わない 0.40・間 0.30・逆 0.05 |
| Q2 | apex の率の差 Δ = M2A − M2 | **変わる**(上がる / 下がる)\|Δ\| ≥ 0.15・**変わらない** \|Δ\| < 0.05・ほか = 間 | 変わる 0.20・変わらない 0.40・間 0.40 |
| Q3 | apex の行の裏付けの道(M2A の証明の欄)・reason の道(両腕)・apex でない行の conjecture の上位・status の内訳・長さ | 記述 | — |

- 見込み(関門の側): OLMo の apex の率は分からない(初めて)。apex の行か apex でない行が 10 に満たなければ Q1 は読まず、記述だけにする。

## §4. 読み方

- `--read` が `olm113/read.json` を書く。RESULT では、M2A の apex の行の証明の欄を道の札ごとに 3 本ずつ(無ければある分)逐語で引き、主 session の読み(L3)を並べる。道の札は記録で、判定に使わない。

## §5. 主張しないこと

- 道の語は語の印で、その道で正しく証明したことの検証ではない。PROJ と TRAP は同じ考え(平行な二本の垂線の間の中点)の言い方の違いでありうる。
- status は申告。apex でない行が「問い」と言うことは、誤りに気付いたことの証拠ではない。
- 一つの model・座標の在る一つの問いの文。moy-2 の F5a-2 の形はこの札で初めて使う(moy-1 の F5a-2 と同じ置き換え)。

## §6. 走らせ方と記録

- zebrashark: `--selftest` → `--gen`(olm112 の後・約 2 時間)→ `--read`。
- smoke(凍結の前・seed 20261198・各腕 2 行・max_new 1536・読まない・zebrashark 350 s・Traceback 0): M2 = T 1536(上限)・T 561(apex 偽・status none = 追記なしの腕なので欄なし)/ M2A = T 449(apex 真・status hypothesis・証明の欄 182 字)・T 309(apex 偽・status none)。本文は読んでいない。
- 出力 = `ConstructGap/exp/olm113/`。RESULT = `conversations/2026-11-02/RESULT_olm113_moy2_projection_status_and_backing_20261102.md`。
