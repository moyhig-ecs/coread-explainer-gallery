# BUNDLE_NOTES — moy1_v3_1(駅 2 = moy-1 受領版 v3.1 の公開の束)

- 開始 2026-11-09 13:56 JST(zebrashark・作り手 = Opus 5.5 一人・依頼書 = BRIEF A3)。打ち切り 90 分 = 15:26。
- 守ったこと: install・通信・git の書き込みなし(git は rev-parse / log / diff --quiet / archive / describe の読むだけ)・実験の script は import も実行もしない(走らせたのは entry 自身の pack / 検査 / build の道具だけ)・ConstructGap の公開 clone は file を text として読んだだけ(`ast.literal_eval`)・model を動かさない・subagent なし・port は 28500〜28599(http.server 28500・marimo 28581・JupyterLab 28583〜28588)・止めたのは自分が起こした pid だけ。
- 元(読むだけ)= `conversations/2026-11-06/coread_station2_3/station2_moy1/receipt/entry_v3_1_received/`。builder = `conversations/2026-11-09/publish_prep/gallery/make_bundle_moy1_v3_1.py`。

## 何をしたか(順に・L1 = 走らせて見た事)

1. **data の集合を述語で決めた**: entry の写しを scratch に置き、`pack_moy1.py`(+ `pack_after.py`)・`check_claims.py`・`make_check.py` を audit hook(`open`・`os.listdir`・`glob.glob`・`subprocess.Popen`)と `exists` / `is_file` の包みの下で走らせ(MOY1_REPO = 家の repo)、repo の下で開いた file 187 + 存在だけ確かめた file 5(pc1 RESULT・screen 二つ・F5 ADJUDICATION・olm62 RESULT = `pack_moy1.py` の `CARD_FILES` の assert)= **192 file・11,942,467 B** を `data/` に repo の相対 path で写した。`claims_anchors.json` の file は全部この中にあった(足し分 0)。git の問い 38 種(PREREG の最初の commit・file の最後の commit の日付)の答えを `data/git_facts.json` に。
   - 一回目は「開いた file」だけで集合を作り、束の中の build が `pack_moy1.py:810` の `assert (REPO / _rel).exists()` で落ちた(L1)= 存在の確かめも述語に足した。trace は builder に入れた(`--work <scratch>`)。
   - 主 session の目安(10 MB 前後)より多い分: olm112 / olm114 の `gen.json`(1.1 MB + 0.5 MB・pack が読む)・olm84 / 85 / 86 / 95 の control・olm95 / 97 の read・家の札の md 31 本(RESULT / PREREG / SCOPE を script が読む・cards/ にも重ねて在る)・card tree の `tree_src.json`(0.5 MB)・inventory の `check_values.out`。
2. **書き換え**(全部 `BUNDLE_BUILD.json` の `rewrites`): `MOY1_REPO` の既定 = 束の `data/`(code 7 本: check_claims / pack_moy1 / pack_after / make_check / make_readme / widget ×2 / data.mjs)・git の呼び出し 6 か所 → `_git_fact` / `gitFact`(REPO が git の checkout なら git に聞き、そうでなければ `data/git_facts.json`)・`run_*.sh` の `PY` / `BUN` の既定 → PATH・`check_fence.py` の語の一覧 → env `FENCE_WORDS`(一覧を束に残さない・未設定なら「armed でない」と言って 0)・cards の外の PI の呼び名(内輪の語の一覧の語)11 か所 → 「依頼者」(make_readme 2・make_script 3・SCRIPT 2・ENTRY_README 2・NOTES 4 → NOTES の 4 のうち 1 は逐語の引用の中)・maker の README と DONE は `ENTRY_README.md` / `ENTRY_DONE` に。log と NOTES の絶対 path は `<entry>` / `<scratch>` / `<repo>` / `<home>` に伏せた。
3. **cards/ 61 file**(逐語・全部 HEAD と同じ bytes): 後の札 20(olm76・83〜86・88・89・91〜95・97・98・101・106・108・112・114・128)と olm59 / olm62 / prf4 の PREREG + RESULT(46)・probe の札の記録(replication の PREREG + RESULT・pc1 の PREREG + RESULT・screen 二つの RESULT・F5 の ADJUDICATION・cmt5 / cmt13 の PREREG + RESULT = 11)・SCOPE 二つ・BRIEF v3 / v3.1。見つからない = screen 二つと F5 の PREREG(その名の file が無い・screen の RESULT は「事前登録もしていない」と自分で書く)・moy_suite_report(札の file が無い data)。olm4 / olm7 は系統樹にあるが data を読まないので入れない。
4. **A4**: 公開 ConstructGap v1.0.1 の `probe_registry.py` の `ARMS_APPEND` と `prompts.py` の literal を `ast.literal_eval` で取り出し(import も実行もしない)、`make_prompt_provenance.py` が束の中だけで md5 の鎖を当てる = 凍結の 6 値が全部一致(open 3c7a63dd・blocked 616682f5・selection-supply a8186b8a・blocked + `\n\n` 03938930・F5a-2 c79980dc・F5b-1 cc05d498)・blocked の尾 324 字 = 公開の literal と byte 一致。**open の本文そのものは作れない**(座標は suite の geometry の計算 = 実行しないと出ない)= 作れないと書いた。open の 20 行のうち公開の `prompts.py` の文字列にそのまま在るのは 6 行(substring の検査・残りは f-string か計算)。
5. **skill/** = `git archive 674b789f .claude/skills/coread-explainer`(36 file・SKILL.md md5 1f76664d…)。
6. 手で書いた物: README.md・JUDGING_SUMMARY.md・cards/INDEX_en.md・CITATION.cff・LICENSE(駅 1 の MIT 本文 21 行)・LICENSE-Anatomy.txt と make_manifest.py(駅 1 の写し・md5 同じ)・make_prompt_provenance.py・この NOTES。

## 検査(結果は下の「結果」の節)

- C5: 束を scratch に写し(git の外)、`bun build.mjs` → 頁 4 本・widget・build_report・generated/ の全 file が元と byte で一致(28b2bcd8 / 47c6b01f / 8ce9d231・pack 3f4370e8)・`check_claims.py` 689 / 689・統制 9 / 9。
- 通し: 束の写しで `sh run_checks.sh checks`(env PY・BUN・MARIMO_PORT=28581・JUPYTER_PORT=28583・SH_TMP・FENCE_WORDS = 13 語)。
- C4: 束の写しを `python3 -m http.server 28500` で配り、4 頁 × desk / phone / video(?video=1)で 43 状態(`checks/check_states.json`)・console。script = 下の「C4 の command」。

## 結果

- **C5(L1)**: 束の写し(git の外)で `bun build.mjs` → `pages/` と `generated/` の全 file が元と byte 一致 = moy1 **28b2bcd8**・moy1-en **47c6b01f**・widget.js **8ce9d231**・pack 3f4370e8。`check_claims.py` **689 / 689**・統制 **9 / 9**。
- **通し(L1)**: 束の写しで `run_checks.sh checks` 14:05:21〜14:17:39(738 s)**exit 0**。測り 43 状態 × 全枠・robust 2,150 組 × 3 で例外 0・parity / sae / v21 / v3 / cards / chapters / words ✓・fence(FENCE_WORDS 13 語を設定)20 file 0・marimo 両向き ✓・JupyterLab 両向き ✓(cell ごとの走らせた回数 {1:1, 4:2, 5:1, 6:1} = 11-09 の直しの手順どおり一回で通った)・`console: clean` × 25 + JupyterLab の拡張の `console.warning` 3 行(error ではない・11-09 の log にも同じ 3 行)。log = `checks/run_checks_bundle_20261109.txt`(scratch の path は `<scratch>`)。
  - 違い 1 つ(L1): `SCRIPT_yukkuri.md` は make_script.py が書き直す = PI の呼び名 →「依頼者」で字数が変わり、長さ 284.6 s → **284.9 s**(≤ 285 のまま)。束の SCRIPT は builder が `make_script.py` で出し直した物(通しの出力と byte 一致)。
  - 通しは captures/ の J1〜J3・M2 を撮り直すが、束には作り手の撮影を残した(撮り直しは入れない)。
- **C4(L1)**: 下の表(4 頁 × desk 1440×1800 / phone 390×3200 / video 1920×1080・`http://127.0.0.1:28500/pages/…`)。
- **C6 / C7 / C1 / C2 / C3**: 下に追記。

### C4 の command(scratch の `c4_http.sh`・中身)

```
B=$1; PORT=${2:-28500}; PY=${PY:-python3}; BUN=${BUN:-bun}; SK=${ANATOMY:-$HOME/.claude/skills/anatomy}
cd "$B"; "$PY" -m http.server "$PORT" --bind 127.0.0.1 & pid=$!; trap 'kill $pid' EXIT
for pg in moy1 moy1-en moy1-light moy1-light-en; do for fr in "desk 1440 1800" "phone 390 3200" "video 1920 1080"; do
  "$BUN" "$SK/scripts/drive.mjs" "http://127.0.0.1:$PORT/pages/$pg.html[?video=1]" --actions checks/check_states.json --width W --height H
done; done      # measure_ok の数・console の行・drive の exit を一行ずつ
```
実行: `PY=<py314>/python3 BUN=<home>/.bun/bin/bun sh c4_http.sh <束の写し> 28500`

### 再現の command

```
python3 -I conversations/2026-11-09/publish_prep/gallery/make_bundle_moy1_v3_1.py --work <scratch>   # 手書きの file(README・LICENSE・CITATION・JUDGING_SUMMARY・INDEX_en・この NOTES・make_manifest・make_prompt_provenance・checks/run_checks_bundle_20261109.txt)は触らない
cd moy1_v3_1 && python3 -I make_prompt_provenance.py && python3 -I make_manifest.py && python3 -I make_manifest.py --verify
```

### C4 の結果(14:20〜14:31・port 28500・止めた pid は自分の http.server だけ・止めた後 28500 の listener なし)

```
moy1 desk 1440x1800: measure_ok 43 · console: clean · drive exit 0
moy1 phone 390x3200: measure_ok 43 · console: clean · drive exit 0
moy1 video 1920x1080: measure_ok 43 · console: clean · drive exit 0
moy1-en desk 1440x1800: measure_ok 43 · console: clean · drive exit 0
moy1-en phone 390x3200: measure_ok 43 · console: clean · drive exit 0
moy1-en video 1920x1080: measure_ok 43 · console: clean · drive exit 0
moy1-light desk 1440x1800: measure_ok 43 · console: clean · drive exit 0
moy1-light phone 390x3200: measure_ok 43 · console: clean · drive exit 0
moy1-light video 1920x1080: measure_ok 43 · console: clean · drive exit 0
moy1-light-en desk 1440x1800: measure_ok 43 · console: clean · drive exit 0
moy1-light-en phone 390x3200: measure_ok 43 · console: clean · drive exit 0
moy1-light-en video 1920x1080: measure_ok 43 · console: clean · drive exit 0
c4 done · exit 0
server pid 88503 stopped
```

### C1 / C2 / C3 / C7 / C8 / C9(L1・builder の最後の走り 14:3x の `BUNDLE_BUILD.json` の scan と fence_summary)

- **C1 内輪の語**(check_fence.py の 11 語 ∪ 手順書 C1 の 5 語 = 13 語・大小を区別しない・全 text file): cards/ 60 file 146 件(札の原本の逐語 + INDEX_en の語彙の節)・data/ 31 file 119 件(scripts が読む札の md の逐語の写し)・skill/ 1 file 1 件(SKILL.md の description の「…動画」の一語 = 674b789f の逐語)・**それ以外 0**。頁(pages/)は 0。
- **C2 絶対 path**: cards/ の外は 0。cards/ の 3 file(BRIEF v3・v3.1・PREREG prf4)は原本の逐語なので残す。機名 zebrashark は README(語彙の一行)・NOTES(作り手の記録 3)・この NOTES に残る(README の語彙で受ける)。
- **C3 内部の記録**: sealed / SEALED_* / reads / receipt_read / CRIT_* / TALLY_* / judging = 0(find)。JUDGING_SUMMARY は要約で読み手の返答の原文を含まない。ENTRY_README と NOTES は `receipt_read/reads/…` の名を文として挙げる(file は無い)。
- **C7 大きさ**: 42 MB(≤ 50 MB)。
- **C8**: frontier の model 名は data の写しに残る(prf4 read.json・凍結の replication config・olm114・moy_suite_report)= README の Provenance に一行。
- **C9**: 作り手 = v3 二口(Opus 5.5 xhigh / Sonnet 5.5 max)・v3.1 一人(Opus 5.5 xhigh)・主 session の直し 2 回 = README。
- **B4**: skill/ = 674b789f の `.claude/skills/coread-explainer`(SKILL.md md5 1f76664d2a856df62e747930ccd6a94a)。

## 易しかったこと / 難しかったこと(時刻つき)

- 易: 13:56〜14:05 entry の build が git の外の写しでそのまま byte 一致した(data と git の答えを写すだけで閉じた)。
- 難: 14:03 data の集合 = 「開いた file」だけでは足りず、`exists()` の assert で落ちた → 存在の確かめも trace に足した。git に聞く 6 か所(日付・凍結の commit)は data の写しでは答えられない → `data/git_facts.json` + 書き換え。
- 難: 14:0x〜14:1x 自動の許可の判定が数回「判定なし」で Write / Bash が止まった(内容は変えずに再送)。
- 判断(L3): skill/ の SKILL.md の一語は逐語のまま残した(公開済みの skill の版の写しで、md5 を README に書くため)。cards/INDEX_en.md の語彙の節にも PI の呼び名の漢字が 2 件ある(駅 1 の INDEX と同じ扱い)。

## 終わり

- C6 = `make_manifest.py` → `--verify`(下)。DONE を置いた時刻は DONE に。
