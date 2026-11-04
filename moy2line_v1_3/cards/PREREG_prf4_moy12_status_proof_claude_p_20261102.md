HEAD(R1) = 5f793f86(凍結時の HEAD・origin と同じ = この file と runner を入れる commit の親)

# PREREG(札 `prf4`・凍結 2026-11-02): moy-1 / moy-2 の答えに「それは仮説か問いか」と裏付けを求めると、Opus 5.5 xhigh と Fable 5.1 xhigh は moy-1 の apex に二等分線 → 直角 → Thales の逆の鎖を書くか・何と申告するか・moy-2 の裏付けは射影か(Claude Code `claude -p`・API でない)

- 発注(逐語・先生 11-02): 「**OLMoで札を作って実行するのと並行して、opus-5.5-xhighとfable-5.1-xhighに対してmoy-1/2について同様の問い合わせをする。APIではなくセッションで。**」(全文は [olm112 の PREREG](PREREG_olm112_moy1_apex_status_and_geometric_proof_20261102.md))
  - 先生の選び(11-02): status は申告させる / moy-2 は道を縛らない / 規模 = 中(model × 問いごとに 10 本 = 40 session)。
- G10 の欄: 比べる物 = 「Opus 5.5 xhigh と Fable 5.1 xhigh で、moy-1 の答えの欄が apex の行の証明の欄が二等分線 → 直角 → Thales の逆の鎖を満たす割合」/「moy-1 と moy-2 の status の内訳」/「moy-2 の apex の行の裏付けの道(射影・台形・解析・合同・ほか)」 / 計器 = olm112・olm113 と同じ(凍結の分類器 classify・凍結の対照の計器 closure_higashida_axis・hq 共通の部品の status の読みと証明の述語と道の語・較正 61 / 61) / 雛形 = いいえ
- runner = [prf4_…py](../../ConstructGap/exp/prf4_moy12_status_proof_claude_p_20261102.py)・共通の部品 = [hq_moy12_status_proof_common_20261102.py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)。走らせる所 = zebrashark(OLMo の生成と並走・`claude -p` は GPU を使わない)。

## §0. 起案の前に見た物(開示)

- olm112 / olm113 の §0 と同じ。frontier の moy-1 / moy-2 の過去の札(API・`claude -p`)の値は、この札の起案で開いていない。
- 隔離の試し(11-02・Haiku 5.5・low・下と同じ flag・空の folder `/private/tmp/claude-501/prf4_isolation_smoke`): init の tools = `[]`・mcp = `[]`・CLAUDE.md なし・git の repo でない・memory の folder は空(新しい path)。model の答え: 「Project instructions (CLAUDE.md): None are loaded」「Git status: Not a git repository」。

## §1. 経路と計器

- **経路** = prf1(10-21)と同じ `claude -p`: 一本ごとに新しい空の folder(`/private/tmp/claude-501/prf4_run/<arm>_<model>_r<k>`・repo の外・git でない・走る前に消して作り直す)・`--setting-sources local`・`--strict-mcp-config` + 空の MCP・**道具は全部 disallow**(prf1 の list・Bash を含む)・`--no-session-persistence`・`--output-format stream-json --verbose`・**`--effort xhigh`**・時間切れ 3600 s。費用は Claude Code の枠(`est_usd` は API の単価での換算)。
- **model** = `claude-opus-5-5` / `claude-fable-5-1`。
- **問いの文** = olm112 の M1A・olm113 の M2A の文から、末尾の cue(改行)を外した物(md5 `6b066cd8…` / `e516d89d…`)。「First write your reasoning as plain text.」も OLMo と同じに残す。
- **単位** = opus:M1A 10・fable:M1A 10・opus:M2A 10・fable:M2A 10(並列 4)。
- **採点** = olm112・olm113 と同じ: moy-1 は `label_json_fields`(群)・`label`(記述)・status・証明の欄の述語(CHAIN = BIS ∧ RA ∧ THC)。moy-2 は apex(closure_higashida_axis)・status・道の語(記録だけ)。stream の読み = moy5t の凍結の parse と同じ本文(runner に写した)。答えの本文 = result の event の `result`。

## §2. 関門

- **I**(隔離): 読む行の全部で init の tools = `[]` かつ道具の呼び出し 0。✗ の行はその単位から外して開示する。
- **K**(単位ごと): ok(答えの本文があり error でない)≥ 8 / 10。✗ → その単位を判定で読まない(記述だけ)。
- 較正 61 / 61(runner の guard)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q1(主・model ごと)** | moy-1 で答えの欄が B-bind の行(5 行以上)のうち、証明の欄が CHAIN を満たす割合 | **✓** ≥ 0.70・**偽** ≤ 0.20・ほか = 間 | Opus: ✓ 0.55・間 0.30・偽 0.15 / Fable: ✓ 0.50・間 0.30・偽 0.20 |
| Q2 | status の内訳(model × 問い・moy-1 は B-bind とそれ以外・moy-2 は apex とそれ以外) | 記述 | hypothesis が多数(どの単位も)0.6 |
| Q3 | moy-2 の apex の行の裏付けの道(PROJ・TRAP・ANALYTIC・CONG・OTHER)と道の語の数 | 記述 | PROJ か TRAP が多数 0.7 |
| Q4 | olm112・olm113 との並べ(経路が違うので混ぜない・同じ文・同じ計器) | 記述 | — |

## §4. 読み方

- `--read` が `ConstructGap/exp/prf4/read.json` を書く(単位ごと・各単位は最後の試行の行)。stream は `ConstructGap/exp/prf4/streams/` に写す。
- RESULT では、moy-1 の CHAIN でない B-bind の行の証明の欄を全部、CHAIN の行から各 model 2 本を逐語で引く。moy-2 は道の札ごとに 2 本ずつ。

## §5. 主張しないこと

- `claude -p` は Claude Code の system prompt の下の答えで、API の答えと一対一に並べない(経路が違う)。effort xhigh だけ。
- n = 10 の単位で、判定は余白の線だけ。model の間の差を検定しない。
- frontier の中は見えない(本文だけ)。CHAIN は語の鎖で、証明の正しさの検証ではない。status は申告。

## §6. 走らせ方と記録

- zebrashark: `python ConstructGap/exp/prf4_moy12_status_proof_claude_p_20261102.py --self-test` → `--fire --workers 4` → `--read`。出力 = `ConstructGap/exp/results_prf4_20261102.jsonl`。RESULT = `conversations/2026-11-02/RESULT_prf4_moy12_status_proof_claude_p_20261102.md`。
