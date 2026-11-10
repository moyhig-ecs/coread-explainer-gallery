# BUNDLE_NOTES — moy5_v2_3_1(駅 3 = moy-5 受領版 v2.3.1 の公開の束)

- 開始 2026-11-10 11:35:35 JST(最初の command の `date`・zebrashark・作り手 = Opus 5.5 一人・依頼書 = BRIEF B4′)。60 分 = 12:35 に進み具合を一行・打ち切り 75 分 = 12:50。
- 守ったこと: install・通信・git の書き込みなし(git は rev-parse / diff --quiet / archive / describe / log -1 の読むだけ)・実験の script は import も実行もしない(走らせたのは entry 自身の pack / 検査 / anchor / build / 比べの道具だけ・b5bp の runner は pack_data.py が text として読む = data に写しただけ)・ConstructGap の公開 clone は file を text として読んだだけ・model を動かさない・subagent なし・Fable なし・port は 28700〜28799(http.server 28700・marimo 28781・JupyterLab 28783〜28788)・止めたのは自分が起こした pid だけ。
- 元(読むだけ)= `conversations/2026-11-06/coread_station2_3/station3_moy5/receipt/entry_v2_3_1/`。手本(読むだけ)= `conversations/2026-11-09/publish_prep/gallery/`(BRIEF B4・`make_bundle_moy5_v2_2.py`・`moy5_v2_2/`)。builder = `conversations/2026-11-10/publish_prep/gallery/make_bundle_moy5_v2_3_1.py`(v2.2 の builder の写し + 直し・直した所は builder の docstring の頭)。scratch = `<scratch>`(work = trace・orig = 元の写しの build・bundle = 束の写しの build・照合・通し・base22 = v2.2 の束の写し・anch = make_anchors_v23 の冪等の確かめ・c4 = C4 の写し・tools = C4 の script)。

## 何をしたか(順に・L1 = 走らせて見た事)

1. **builder** = v2.2 の builder を写し、直したのは: 元 / 置き場の path・trace に `make_anchors_v23.py` と `compare_v22.py` を足した(後者は引数の二つの file しか開かないので、builder が作る合成の dump 二つで走らせた)・cards に BRIEF v2.3 を足した・内輪の語の書き換えの数を v2.3.1 で数え直した(下の 3)。写したまま = 除外の規則・data の述語・reader_reply_facts・skill の写し・masks・scan。
2. **data の集合を述語で決め直した**(見込みで済ませない・依頼書 §2-1): entry の写しを scratch に二つ置き、`pack_data.py`・`check_claims.py`・`check_claims.py --calibrate`・`make_check.py`・`make_script.py`・`list_headings.py`・`make_anchors_v21.py`・`make_anchors_v22.py`・**`make_anchors_v23.py`**・**`compare_v22.py`** を audit hook(`open`・`os.listdir`・`glob.glob`・`subprocess.Popen`)と `exists` / `is_file` の包みの下で走らせた(REPO = 家の repo・10 本とも exit 0・subprocess 0)。repo の下で開いた file 99 + 存在だけ 0 ∪ `claims_anchors.json` の file / files(足し分 0・面の anchor 13 本の file = SOURCE 10-14 は既に在る)= 99 から、家の審査の記録 4(`station3_moy5/reads/{N_R1_Q,N_R2_P,N_R2_Q,T_R2}/judge_reply.md`)を除いた **95 file・8,246,529 B**。
   - **v2.2 の束の `data/` との差**(`diff -rq`): 足した 0・減った 0・中身が違う 1 = `data/reader_reply_facts.json`(違うのは `house_head` と `made` の二行だけ・md5 と確かめた三つ組 5・含む文 5 は同じ)。`data/SOURCES.tsv` は byte で同じ(95 行の md5・bytes・same_as_HEAD が全部同じ)。= v2.3 / v2.3.1 で data は変わっていない、を述語で確かめた。
3. **書き換え**(全部 `BUNDLE_BUILD.json` の `rewrites`・21 件 = v2.2 の 17 件の型 + 4): path(`REPO` の既定 = 束の `data/`・env `MOY5_REPO`・`data.mjs` の `X`・`build.mjs` の `PY`・`run_*.sh` の `PY` / `PYD` / `BUN`)・読み手の返答の二か所(v2.2 と同じ)・PI の呼び名 →「依頼者」**22 か所**(pack_data の注 3・make_script 1・ENTRY_README 5・NOTES_v1 3・NOTES_v2 2・NOTES_v21 4・**NOTES.md(v2.3)1・NOTES_v231.md 1・make_anchors_v23.py 1 + CLAIMS_v23.md 1**・逐語の引用の話者名を含む・中身は変えない)。make_anchors_v23.py は CLAIMS_v23.md の題の行を書くので、二つを同じに書き換えた → 束の写しで `make_anchors_v23.py` を走らせ直して CLAIMS_v23.md と claims_anchors.json が byte で同じ(冪等)を確かめた。`SCRIPT_yukkuri.md` は make_script.py で出し直した(146.8 s・v2.2 の束の物と byte で同じ)。maker の README は `ENTRY_README.md` に。**v2.3.1 の entry には DONE が無い**(NOTES_v231 の「DONE は写さない」)= `ENTRY_DONE` も無い。
4. **頁(dist/)**: 元の entry の `dist/` は git に在る(7 file・HEAD と同じ)が、v2.2 の束の型のまま entry から写さず、束を scratch に写して(`MOY5_REPO` を外して)`bun build.mjs` した物を束に写した(C10 で `git add -f`)。
5. **cards/ 80 file**(逐語・全部 HEAD と同じ bytes): v2.2 の束の 79 file + **BRIEF v2.3**(768ec87e)。79 は v2.2 の束と md5 が同じ。見つからない = mnw1b の RESULT(v2.2 と同じ・作らない)。**v2.3.1 には依頼書が無い**(`NOTES_v231.md` の「発」の行が依頼)= `cards/INDEX_en.md` に書いた。`PROMPT_PROVENANCE.md` は `make_prompt_provenance.py`(v2.2 の束の写し)で出し直し = v2.2 の束の物と byte で同じ(ee39ba02・9 / 21・6 / 22 行)。
6. **skill/** = `git archive 674b789f .claude/skills/coread-explainer`(36 file・SKILL.md md5 1f76664d…・v2.2 の束と同じ)。
7. 手で書いた物: README.md(頭に v2.2 の束からの差の数行)・JUDGING_SUMMARY.md(v2.2 の束の物 + v2.3・v2.3.1・受領の検査 741cef54 / ce4b7e3f)・cards/INDEX_en.md・CITATION.cff(version 2.3.1)・この NOTES。それぞれ v2.2 の束の物を scratch の小さな script(`make_readme.py`・`make_judging.py`・`make_index.py`・`make_cff.py`・一つの置換ごとに数を assert)で直した。LICENSE・LICENSE-Anatomy.txt・make_manifest.py・make_prompt_provenance.py は v2.2 の束の写し(md5 同じ)。
8. 撮影は撮り直していない(依頼書 §2-4): `captures/` 69 枚 = v2.3.1 の entry の写し(撮り直し 6 枚 + v2.3 の写し)。

## 結果

- **頁と widget の md5 の四つの一致(L1)**: 元の entry の写し(家の repo を読む・`dist/` と `generated/` を消してから)と束の写し(git の外・束の `data/` を読む・`MOY5_REPO` なし)で `bun build.mjs`(bun 1.3.0・anatomy 689dcf9)。

  | file | 元の entry の `dist/`(git) | 元の写しの build | 束の写しの build | 束の `dist/` | 記録(NOTES_v231 §3 + 主 session 11-10) |
  |---|---|---|---|---|---|
  | moy5_route.html | 03e6408d | 03e6408d | 03e6408d | 03e6408d | 03e6408d |
  | moy5_route-en.html | d2515fad | d2515fad | d2515fad | d2515fad | d2515fad |
  | moy5_route-light.html | 40a17e38 | 40a17e38 | 40a17e38 | 40a17e38 | 40a17e38 |
  | moy5_route-light-en.html | 207a5d1f | 207a5d1f | 207a5d1f | 207a5d1f | 207a5d1f |
  | widget.js | 5761d49f | 5761d49f | 5761d49f | 5761d49f | 5761d49f |
  | widget.css | 6dc3b024 | 6dc3b024 | 6dc3b024 | 6dc3b024 | — |
  | build_report.json | 31266642 | 6593d8ec | 6593d8ec | 6593d8ec | — |

  - `build_report.json` だけ entry と違う = 中身の差は `"runtime": "bun 1.4.3"` 対 `"bun 1.3.0"` の一行だけ(`json.tool` で比べた)。頁・widget は bun の版が違っても同じ bytes(v2.2 の束と同じ)。`generated/pack.json` は三つとも cac8f992(entry と同じ)。
- **C5(L1)**: 束の写し(`MOY5_REPO` なし)で `check_claims.py` **447 / 447**(missing or different 0)・`--calibrate` **19 / 19**・面 13 / 13 + 仕込み 3 / 3(frozenV・shift・tilt を捕まえる)。`make_anchors_v23.py` の冪等も束の写しで確かめた(上の 3)。
- **通し(L1)**: 束の写しで `run_checks.sh`(引数なし・env PY・BUN・MARIMO_PORT=28781・JUPYTER_PORT=28783・SH_TMP・**BASE22 = v2.2 の束の scratch の写し**)11:38:16〜11:53:36 **run_checks: PASS**(exit 0)。log の頭の頁の md5 03e6408d / d2515fad / 5761d49f・447 / 447・19 / 19・script 146.8 s・measure_ok 31 × 8 + 6 × 5・robust 496 組 errors 0・v22_ok 6 × 5・**v23_ok 8 × 7・geom23_ok**・marimo(両向き + cone 両向き・own pid 止まった・listener 0)・JupyterLab(両向き + cone・state 18 の図 → kernel は 2 回目で一致・listener 0)・console は clean 40・JupyterLab の拡張の console.warning 3 行だけ(v2.2 の束の通しと同じ 3 行・図解の側ではない)。log = `checks/run_checks_bundle_20261110.txt`(path は伏せた)。束の `checks/last_run.txt` は作り手の log のまま(path は伏せた)。
- **BASE22 の比べ(L1)**: `compare_v22 … 33 dumps · equal 31 · differ 2 ['0/on', '7/on'] · unexpected 0` × 6(moy5_route / -en × video / desk / phone)= NOTES_v231 §3 と同じ。
- **C4(L1)**: 下の 28 drive 全部 console clean・exit 0。
- **差の一覧(v2.2 の束との `diff -rq`・11:4x に BUNDLE_NOTES / MANIFEST / DONE と版の log を置く前に取った 58 行・種類ごと・39 + 7 + 10 + 1 + 1 = 58)**:
  - entry の v2.2 → v2.3.1 の差がそのまま来た物 39: 頁の元(figure.js・figure.css・i18n.js)3・検査と anchor(check_claims.py・make_check.py・run_checks.sh・pack_data.py・claims_anchors.json)5・新しい file(CLAIMS_v23.md・NOTES_v231.md・make_anchors_v23.py・compare_v22.py)4・NOTES.md 1・ENTRY_README.md 1・generated/pack.json 1・captures 8(撮り直し 6 + marimo_s10・jupyterlab_s18)・checks 15(違う 11 = json 10 + last_run.txt・新しい json 4)・`ENTRY_DONE` が A だけ 1(v2.3.1 の entry に DONE が無い)。元の二つの entry の `diff -rq` の行と一対一。
  - build し直した dist 7(頁 4・widget 2・build_report 1)。
  - 手で書いた物・生成した物 10: README・CITATION・JUDGING_SUMMARY・cards/INDEX_en・cards/SOURCES.tsv(一行足した)・BUNDLE_BUILD.json・BUNDLE_NOTES / MANIFEST / DONE(A だけ = 置く前に比べた)・checks/run_checks_bundle_20261109.txt(A だけ = v2.2 の束の通しの log・この束には 20261110 の log を置いた)。
  - 札 1(BRIEF v2.3)・data 1(reader_reply_facts.json の head / made)。
  - **予期しない差 0**(SCRIPT_yukkuri.md・skill/・data/ の 95 file・cards の 79 file・PROMPT_PROVENANCE・LICENSE 類は同じ)。
- **C1 内輪の語**(13 語・大小を区別しない・BUNDLE_BUILD.json の `fence`): cards/ 73 file・data/ 27 file(逐語の写し)・skill/ 1 file(674b789f の SKILL.md)・**頁の元 3 file(i18n.js 12・figure.js 3・figure.css 1)と dist/ 6 file(頁 4 × 16・widget.js 15・widget.css 1)= PI の呼び名(漢字)**・それ以外 0。頁は byte で保つため書き換えず README の語彙(sensei = PI)で受けた(v2.2 の束・駅 1 の C11 の裁可と同じ)。v2.3 / v2.3.1 で頁の呼び名は figure.js が 1 → 3 に増えた(v2.3 の面の注の行)。
- **C2 絶対 path**: cards/・data/ の外は 0(cards の BRIEF v2 〜 v2.3 と PREREG 数本・data の写し 2 本は原本の逐語)。機名 zebrashark は NOTES.md 2・NOTES_v1 3・README / INDEX の語彙の行・この NOTES(README の語彙で受ける)。NOTES_v231 の `~/.local/bin/bun` は `~` の形(家の path でない・そのまま)。
- **C3 内部の記録**: SEALED_* / TALLY_* / CRIT_* / reads / receipt_read / prompts / judging = 0(find)。RESULT 駅 3 は pack_data.py が読むので data/ に(v2.2 と同じ・判断 L3)。
- **C7 大きさ**: 下の MANIFEST の値(≤ 50 MB・zip は不要)。
- **C8**: README の Provenance の一行(v2.2 の束のまま・model の名は data に残る)。
- **C9**: v1・v2 二口(Opus 5.5 xhigh / Sonnet 5.5 max)・v2.1 / v2.2 / v2.3 一人(Opus 5.5 xhigh)= NOTES_v21・NOTES.md の頭(v2.3「作り手一人 = Opus 5.5 xhigh」・v2.2 同じ)と BRIEF v2.3 の「作り手 = 一人・Opus 5.5 xhigh」で確かめた・**v2.3.1 = 依頼者と対話していた主 session(Opus 5.5)**= NOTES_v231 の頭「作り手 = 主 session」・effort は記録に無いので書かない。
- **B4**: skill/ = 674b789f(36 file・SKILL.md 1f76664d2a856df62e747930ccd6a94a)。

### C4 の結果(11:54〜12:08・`python3 -m http.server 28700`・束の写し(`checks/` の action は make_check.py で出し直し = 束の物と byte で同じ)・止めた pid は自分の server だけ・止めた後 28700 の listener 0)

4 頁 × desk / phone / video × 全 31 状態 + `?cone=0` + check_v22(状態 0・7 で 表示 → 非表示 → 表示)+ check_v23(状態 0・7 で面が t = ±5 で動かない = `v23_ok`)= 28 drive。

```
moy5_route desk 1440x1800: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route phone 390x3000: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route video 1920x1080: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route cone=0 desk: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route overlay on/off desk (check_v22): measure_ok 6 · v22_ok 6 · v23_ok 0 · console: clean · drive exit 0
moy5_route plane desk (check_v23): measure_ok 0 · v22_ok 0 · v23_ok 8 · console: clean · drive exit 0
moy5_route-en desk 1440x1800: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-en phone 390x3000: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-en video 1920x1080: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-en cone=0 desk: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-en overlay on/off desk (check_v22): measure_ok 6 · v22_ok 6 · v23_ok 0 · console: clean · drive exit 0
moy5_route-en plane desk (check_v23): measure_ok 0 · v22_ok 0 · v23_ok 8 · console: clean · drive exit 0
moy5_route-light desk 1440x1800: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light phone 390x3000: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light video 1920x1080: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light cone=0 desk: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light overlay on/off desk (check_v22): measure_ok 6 · v22_ok 6 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light plane desk (check_v23): measure_ok 0 · v22_ok 0 · v23_ok 8 · console: clean · drive exit 0
moy5_route-light-en desk 1440x1800: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light-en phone 390x3000: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light-en video 1920x1080: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light-en cone=0 desk: measure_ok 31 · v22_ok 0 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light-en overlay on/off desk (check_v22): measure_ok 6 · v22_ok 6 · v23_ok 0 · console: clean · drive exit 0
moy5_route-light-en plane desk (check_v23): measure_ok 0 · v22_ok 0 · v23_ok 8 · console: clean · drive exit 0
moy5_route overlay on/off video (check_v22): measure_ok 6 · v22_ok 6 · v23_ok 0 · console: clean · drive exit 0
moy5_route overlay on/off phone (check_v22): measure_ok 6 · v22_ok 6 · v23_ok 0 · console: clean · drive exit 0
moy5_route plane video (check_v23): measure_ok 0 · v22_ok 0 · v23_ok 8 · console: clean · drive exit 0
moy5_route-en plane phone (check_v23): measure_ok 0 · v22_ok 0 · v23_ok 8 · console: clean · drive exit 0
c4 done · exit 0
server pid 14079 stopped
```

C4 の script(scratch の `tools/c4_http.sh` = v2.2 の束の物 + check_v23 の行・実行 = `PY=<py314>/python3 BUN=<home>/.bun/bin/bun sh c4_http.sh <束の写し> 28700`):

```sh
#!/bin/sh
# c4_http.sh <bundle copy> [port] — C4 (BRIEF B4′ §3): serve a copy of the bundle with python's http.server (127.0.0.1, port 28700 by default) and drive the four pages
# in desk / phone / video frames through every state (check_states.json), ?cone=0 (overlay hidden), the overlay on / off (check_v22.json) and the v2.3 plane check
# (check_v23.json: states 0 and 7, the plane does not move at t = ±5 -> v23_ok). Stops only the server pid it started. (v2.2 bundle's c4_http.sh + the check_v23 rows)
B=$1; PORT=${2:-28700}; PY=${PY:-python3}; BUN=${BUN:-bun}; SK=${ANATOMY:-$HOME/.claude/skills/anatomy}
cd "$B" || exit 1
"$PY" -m http.server "$PORT" --bind 127.0.0.1 > /dev/null 2>&1 &
pid=$!
trap 'kill $pid; echo "server pid $pid stopped"' EXIT
i=0; until curl -s -o /dev/null "http://127.0.0.1:$PORT/dist/moy5_route.html"; do i=$((i + 1)); [ $i -gt 50 ] && { echo "server did not start"; exit 1; }; sleep 0.2; done
fail=0
run() {   # label url actions w h
  out=$(mktemp); "$BUN" "$SK/scripts/drive.mjs" "$2" --actions "$3" --width "$4" --height "$5" > "$out" 2>&1; code=$?
  m=$(grep -c 'measure_ok[^:]*:true' "$out"); v=$(grep -c 'v22_ok[^:]*:true' "$out"); v3=$(grep -c 'v23_ok[^:]*:true' "$out"); con=$(grep -E '^console' "$out" | head -3 | tr '\n' ' ')
  echo "$1: measure_ok $m · v22_ok $v · v23_ok $v3 · ${con}· drive exit $code"; [ $code -eq 0 ] || fail=1; rm -f "$out"
}
U="http://127.0.0.1:$PORT/dist"
for pg in moy5_route moy5_route-en moy5_route-light moy5_route-light-en; do
  run "$pg desk 1440x1800" "$U/$pg.html" checks/check_states.json 1440 1800
  run "$pg phone 390x3000" "$U/$pg.html" checks/check_states.json 390 3000
  run "$pg video 1920x1080" "$U/$pg.html?video=1" checks/check_states.json 1920 1080
  run "$pg cone=0 desk" "$U/$pg.html?cone=0" checks/check_states.json 1440 1800
  run "$pg overlay on/off desk (check_v22)" "$U/$pg.html" checks/check_v22.json 1440 1800
  run "$pg plane desk (check_v23)" "$U/$pg.html" checks/check_v23.json 1440 1800
done
run "moy5_route overlay on/off video (check_v22)" "$U/moy5_route.html?video=1" checks/check_v22.json 1920 1080
run "moy5_route overlay on/off phone (check_v22)" "$U/moy5_route.html" checks/check_v22.json 390 3000
run "moy5_route plane video (check_v23)" "$U/moy5_route.html?video=1" checks/check_v23.json 1920 1080
run "moy5_route-en plane phone (check_v23)" "$U/moy5_route-en.html" checks/check_v23.json 390 3000
echo "c4 done · exit $fail"
exit $fail
```

## 易しかったこと / 難しかったこと(時刻つき)

- 易: 11:37 builder の trace が一回目から通り、data の集合が v2.2 の束と同じ 95 file に閉じた(手本の builder の述語がそのまま効いた)。11:37〜11:38 元の写し・束の写しの build がどちらも一回目で entry の `dist/` と byte 一致(bun 1.3.0 対 1.4.3 でも同じ)。
- 易: 11:38〜11:53 通しが一回で PASS・BASE22 の比べも記録どおり 31 / 33。
- 難(小): `make_anchors_v23.py` が CLAIMS_v23.md の題の行を書くので、PI の呼び名を片方だけ書き換えると出し直しで戻る → 二つを同じに書き換え、冪等を走らせて確かめた。
- 難(小): Bash の zsh で `echo ====` が `=` 展開で落ち、一つの command の後半が走らなかった(読むだけの command・やり直した)。
- 判断(L3): 頁の呼び名(i18n.js ほか)は byte 一致を優先して残した(v2.2 と同じ)・RESULT 駅 3 を data に入れた(v2.2 と同じ)・`build_report.json` の bun の版の一行の差は「頁と widget の一致」の外として扱った。

## 再現の command

```
python3 -I conversations/2026-11-10/publish_prep/gallery/make_bundle_moy5_v2_3_1.py --work <scratch>/work   # 手書きの file は触らない
cp -R moy5_v2_3_1 <scratch>/bundle && cd <scratch>/bundle && env -u MOY5_REPO PY=<py314>/python3 bun build.mjs   # → dist/ を束に写す
cd <scratch>/bundle && env -u MOY5_REPO BASE22=<v2.2 の束の写し> PY=… BUN=… MARIMO_PORT=28781 JUPYTER_PORT=28783 SH_TMP=<scratch>/shtmp sh run_checks.sh
PY=<py314>/python3 BUN=<home>/.bun/bin/bun sh <scratch>/tools/c4_http.sh <scratch>/c4 28700
cd moy5_v2_3_1 && python3 -I make_prompt_provenance.py && python3 -I make_manifest.py && python3 -I make_manifest.py --verify
```

## 終わり

- 所要: 11:35 開始 → 11:53 通し PASS → 12:08 C4 済 → 12:1x MANIFEST・DONE(約 40 分・60 分の行は不要だった)。打ち切り 75 分の内。
- 一番自信の無い点: 頁の元(i18n.js・figure.js・figure.css)と dist/ の PI の呼び名(漢字)を書き換えなかったこと(v2.2 の束と同じ判断・v2.3 で figure.js の当たりが 1 → 3 に増えた)。次点: JUDGING_SUMMARY の v2.3 / v2.3.1 の段は NOTES と commit の本文からの要約(英語)で、依頼者の言葉は「それで進めます」だけ逐語・「切断平面が育つ…」は英訳を引用符で示した(訳は束を切った者)。
- C6 = `make_manifest.py` → `--verify`(MANIFEST.md の頭)。DONE を置いた時刻は DONE に。
