HEAD(R1) = 259a5742(執筆時の HEAD・pull 済み・origin より 6 commit 先)

# RESULT(札 `prf4`・2026-11-02): moy-1 / moy-2 に「仮説か問いか」と裏付けを求めた `claude -p` の 40 本は、22 本が安全分類器に拒否され(reasoning_extraction)、直後に claude-opus-5-5 が組織単位で 1 時間停止した — 読めた単位は Opus × moy-1 だけ(apex 8 / 8・鎖 8 / 8)

- 札 = [PREREG](PREREG_prf4_moy12_status_proof_claude_p_20261102.md)(凍結 cb12da8d)・runner `ConstructGap/exp/prf4_moy12_status_proof_claude_p_20261102.py`・出力 `ConstructGap/exp/results_prf4_20261102.jsonl`・`ConstructGap/exp/prf4/read.json`・stream 40 本 = `ConstructGap/exp/prf4/streams/`。
- 発火 12:23:55 → 12:27:18(並列 4・zebrashark)。費用 $1.5(API 換算・拒否された本にも掛かる)。

## §1. 何が起きたか(L1・stream から)

| 単位 | ok / 10 | 拒否 | 形 |
|---|---:|---:|---|
| Opus 5.5 × moy-1(M1A) | 8 | 2 | `model_refusal_no_fallback`・category `reasoning_extraction` |
| Opus 5.5 × moy-2(M2A) | 3 | 7 | 1 本は同上・**6 本は 1.3〜1.5 s で `403 model_access_suspended`**(費用 0) |
| Fable 5.1 × moy-1(M1A) | 0 | 10 | 全部 `reasoning_extraction`(`safety_stops` 2) |
| Fable 5.1 × moy-2(M2A) | 1 | 9 | 同上 |

- 拒否の説明(逐語): 「This request was blocked as it seems to violate Anthropic's Terms of Service restrictions on reverse engineering or duplicating model outputs.」
- 停止(逐語): 「model: "claude-opus-5-5" is suspended for this organization until 2026-11-02T04:26:04Z」(= 03:26:04Z から 1 時間・12:26〜13:26 JST)。停止の間、主 session の model が Opus 5 に落ち、auto mode の分類器が verdict を返さず Bash / Write が止まった(13:38 に復帰を確認)。
- 隔離(関門 I): 読めた 12 本は init の tools `[]`・道具の呼び出し 0。

## §2. 判定

- 関門 K(ok ≥ 8)を満たした単位 = **Opus × moy-1 だけ**。ほかの 3 単位は判定で読まない。
- **Q1(Opus × moy-1)= ✓**: 答えの欄が B-bind 8 / 8・証明の欄が CHAIN 8 / 8(BIS 8・ADJ 8・RA 8・THC 8・COORD 0)。
- Q2(記述): 読めた 12 本の status は全部 hypothesis。
- Q3(記述・関門外): Opus × moy-2 の 3 本と Fable × moy-2 の 1 本は apex で、裏付けは全部 PROJ(射影)。

## §3. 読み(L3・主 session)

- 引き金の見込み = 両腕に共通する一行 `First write your reasoning as plain text.\nAfter that, respond with the JSON object:`(凍結の F5a-2 の置き換え)。根拠は、同じ経路で証明を欄で求めた 10-21 の prf1(40 本・拒否 0)との差。確かめは [prf5](RESULT_prf5_moy12_proof_field_jsononly_claude_p_20261102.md)(一行を外して 40 / 40 通った)。
- 先生(逐語・12:3x): 「**やっぱり蒸留だと疑われた😅**」。
- 教訓 = memory `feedback_reasoning_extraction_refusal_suspends_opus_20261102`(並列で当てない・症状の見分け方・再発火しない)。

## §4. 言えない

- 「一行が引き金」は prf5 との対照 1 つで言う見込み。他の語を替えた札は無い。
- 拒否は確率的(Opus の moy-1 は 8 / 10 通った)。model と問いで率が違う理由は分からない。
- 停止の規則(何本で・何時間)は 1 回の観測。
