HEAD(R1) = 775c017d(凍結時の HEAD = この file と runner を入れる commit の親)

# PREREG(札 `prf5`・凍結 2026-11-02): prf4 の問いの文から、拒否された一行(考えを平文で先に書け)を外し、裏付けを成果物(JSON の欄)として求めると、Opus 5.5 / Fable 5.1 xhigh は拒否されずに答えるか・moy-1 の apex に二等分線 → 直角 → Thales の逆の鎖を書くか・moy-2 の裏付けは射影か(Claude Code `claude -p`・API でない)

- 発注(逐語・先生 11-02): 「**上流と疑われる思考を取らずに証明の過程を結論として書かせられますか？**」→ 主 session の案(一行を戻し `proof` / `status` を欄で求める・まず Fable 2 本)→ 先生「**まず揃えずに通し、様子を見て揃える**」「**13:26を待って進みましょう。**」
- G10 の欄: 比べる物 = 「Opus 5.5 xhigh と Fable 5.1 xhigh で、moy-1 の答えの欄が apex の行の証明の欄が二等分線 → 直角 → Thales の逆の鎖を満たす割合」/「段 1(Fable 2 本)と段 2(40 本)の拒否の本数」/「moy-2 の apex の行の裏付けの道(射影・台形・解析・合同・ほか)」 / 計器 = prf4 と同じ(凍結の分類器 classify・凍結の対照の計器 closure_higashida_axis・hq 共通の部品の status の読みと証明の述語と道の語・較正 61 / 61)+ stream の `model_refusal_no_fallback` の category と result の `api_error_code` / 雛形 = いいえ
- runner = [prf5_…py](../../ConstructGap/exp/prf5_moy12_proof_field_jsononly_claude_p_20261102.py)・共通の部品 = [hq_moy12_status_proof_common_20261102.py](../../ConstructGap/exp/hq_moy12_status_proof_common_20261102.py)(cb12da8d のまま・**触らない** = olm112 / olm113 の guard が見ている)。走らせる所 = zebrashark(OLMo の生成と並走)。

## §0. 起案の前に見た物(開示)

- **prf4 の結果を全部見た**([read.json](../../ConstructGap/exp/prf4/read.json)): 拒否 = Fable 19 / 20・Opus 3 / 20(category `reasoning_extraction`)、その直後に `claude-opus-5-5` が組織単位で 1 時間停止(403 `model_access_suspended`・03:26:04Z → 04:26:04Z)。読めた単位 = Opus × moy-1(ok 8 / 10)で **B-bind 8 / 8・CHAIN 8 / 8・COORD 0・status は全部 hypothesis**。Opus × moy-2 は ok 3(apex 3・道は全部 PROJ・hypothesis 3)・Fable × moy-2 は ok 1(apex・PROJ・hypothesis)。**§3 の予想はこれを見てから付けた**(Opus の moy-1 は prf4 で ✓ の値・prf5 は文が一行違う)。
- olm112 の最初の 20 行の集計(bind 8・attractor 6・flail 5・stuck 1・status hypothesis 14 / none 5 / question 1・**CHAIN 0**)を log で見た。本文は読んでいない。
- 拒否の引き金の見込み(L3・未検定)= 凍結の F5a-2 の置き換え `First write your reasoning as plain text.\nAfter that, respond with the JSON object:`。根拠 = 両腕に共通する唯一の文・10-21 の prf1(同じ経路・40 本・拒否 0)は `Respond with JSON only:` のまま欄に証明を求めていた(「Give the proof as a chain of relations among the given points」)。
- memory `feedback_reasoning_extraction_refusal_suspends_opus_20261102` に教訓を書いた(11-02)。

## §1. 経路と計器

- **経路** = prf4 と同じ(`claude -p`・空の folder・`--setting-sources local`・空の MCP・道具は全部 disallow・`--no-session-persistence`・`--effort xhigh`・時間切れ 3600 s)。**並列は 2**(prf4 の 4 から下げる = 拒否が重なると停止に化ける)。
- **問いの文**(prf4 からの差は一行と追記の文だけ・自己検査で assert):
  - **M1B**(moy-1)= 凍結の F5a-2 の文の `First write your reasoning as plain text.\nAfter that, respond with the JSON object:` を元の `Respond with JSON only:` に戻し(closure-forcing の追記はそのまま)、末尾に:
    > Also include two more fields in that JSON object. In the "proof" field, prove that each of X1, X2, X3, X4 lies on the circle you identified, by a synthetic (geometric) argument that does not use the given coordinates: give the proof as a chain of steps among the given points, each step naming the fact it uses. In the "status" field, write "hypothesis" if you put the identification forward as a conjecture, or "question" if you leave it open.
  - **M2B**(moy-2)= `prompts.build("higashida_axis", "A", 37)`(元から JSON だけ)の末尾に、同じ型で「prove that the invariant you stated holds」(道は縛らない)。
  - 自己検査: 思考を求める語(your reasoning / think step / chain of thought / plain text)が無い・欄は `proof` と `status` の二つ。
- **採点** = prf4 と同じ(hq 共通の部品・変更なし): moy-1 は `label_json_fields`(群)・status・証明の欄の述語(CHAIN = BIS ∧ RA ∧ THC)。moy-2 は apex(凍結の `closure_higashida_axis`)・status・道の語(記録だけ)。
- **拒否の記録** = 行ごとに `refused`・`refusal_category`・`api_error_code`・`safety_stops`(prf4 の教訓 = 費用だけ掛かって理由が残らない、を防ぐ)。

## §2. 段取りと関門

- **段 1(探り)** = `fable:M1B:1,fable:M2B:1`・並列 1。見るのは **ok と refused と category だけ**(値は読まない)。
  - 拒否 0 / 2 → 段 2 へ。拒否 ≥ 1 → 止めて先生に報告(一行を戻しても拒否されるなら、追記の文の側が引き金 = 別の札)。
  - 段 1 の 2 本は段 2 の rep 0 として数に入れる(runner は ok の行を飛ばす)。
- **段 2** = `fable:M1B:10,fable:M2B:10,opus:M1B:10,opus:M2B:10`(段 1 の分を含めて各 10)・並列 2。
- **I**(隔離): 読む行の全部で init の tools = `[]` かつ道具の呼び出し 0。
- **P**(policy): 段 2 の拒否 ≤ 2 / 40。✗ → Q1〜Q3 は記述だけにし、Q0 を「偽」で読む。
- **K**(単位ごと): ok ≥ 8 / 10。✗ → その単位を判定で読まない。
- 較正 61 / 61(runner の guard)。

## §3. 問いと予想(確率は 0〜1)

| Q | 問い | 通る条件 | p |
|---|---|---|---|
| **Q0(主)** | 一行を外した文は拒否されずに通るか = 段 2 の拒否の本数 | **✓** ≤ 2 / 40・**偽** ≥ 8 / 40・ほか = 間 | ✓ 0.70・間 0.20・偽 0.10 |
| **Q1(model ごと)** | moy-1 で答えの欄が B-bind の行(5 行以上)のうち、証明の欄が CHAIN を満たす割合 | **✓** ≥ 0.70・**偽** ≤ 0.20・ほか = 間 | Opus: ✓ 0.80(prf4 で 8 / 8 を見た)/ Fable: ✓ 0.55・間 0.30・偽 0.15 |
| Q2 | status の内訳(model × 問い・B-bind とそれ以外・apex とそれ以外) | 記述 | hypothesis が多数 0.8(prf4 の 12 本は全部 hypothesis) |
| Q3 | moy-2 の apex の行の裏付けの道 | 記述 | PROJ が多数 0.8(prf4 の 4 本は全部 PROJ) |
| Q4 | prf4 の読めた単位(Opus × moy-1・文が一行違う)との並べ・olm112 / olm113 との並べ(経路と文が違う・同じ計器) | 記述 | — |

## §4. 読み方

- `--read` が `ConstructGap/exp/prf5/read.json` を書く(単位ごと・各単位は最後の試行の行・policy の集計を含む)。stream は `ConstructGap/exp/prf5/streams/` に写す。
- RESULT では、moy-1 の CHAIN でない B-bind の行の証明の欄を全部、CHAIN の行から各 model 2 本を逐語で引く。moy-2 は道の札ごとに 2 本ずつ。拒否された行は category と費用を表にする。

## §5. 主張しないこと

- 「一行が引き金」は、段 2 が通っても **一つの対照(prf4)との差** でしか言えない(他の語を一つずつ替える札は立てていない)。
- `claude -p` の答えは Claude Code の system prompt の下の物。API の札と一対一に並べない。
- frontier の文は OLMo(F5a-2)と一行違う。測る対象は `proof` の欄なので読みは保つが、「揃える」なら OLMo に JSON だけの腕を足す(先生「様子を見て揃える」)。
- CHAIN は語の鎖で証明の正しさの検証ではない。status は申告。

## §6. 走らせ方と記録

- zebrashark: `--self-test` → 凍結の commit → `--fire`(段 1・既定)→ 拒否 0 なら `--fire --units <段 2>`(並列 2)→ `--read`。出力 = `ConstructGap/exp/results_prf5_20261102.jsonl`。RESULT = `conversations/2026-11-02/RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md`。
