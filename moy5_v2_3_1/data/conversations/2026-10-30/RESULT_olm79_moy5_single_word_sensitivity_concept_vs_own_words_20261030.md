HEAD(R1) = ee497d0c(走行の時の zebrashark の HEAD = 凍結 1ad08f57 + 台帳の一行・dirty なし)

# RESULT(札 `olm79`・2026-10-30 夜・zebrashark): moy-5(線 2・L2-2)— 一語ずつの lens は精度は立つが(C0 ✓・0.997)、行の中の前触れを拾う感度の陽性統制が線に届かない(C1 ✗・45 / 77 = 58 %・p 0.086)= Q1〜Q3 は読まない・一語の計器の線を閉じる

- 凍結 = [PREREG](PREREG_olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.md)(1ad08f57)・runner = [olm79_…py](../../ConstructGap/exp/olm79_moy5_single_word_sensitivity_concept_vs_own_words_20261030.py)。
- forward = zebrashark・366 行(層 48 だけ)・23:32〜23:50(1,087 秒)・log = `ConstructGap/exp/olm79/fire.log`。
- 出力 = `ConstructGap/exp/olm79/series/*.npz`(366)・`control.json`(md5 `fd600cca…`)・`read.json`(md5 `b81c8cf7…` = 「C1 ✗ = 読まない」)。

## 統制

| | 判 | 実出力 |
|---|---|---|
| C0 一語の精度 | ✓ | CUT の語の 1 token 前の u の中央値 **0.997**(129 語)・陰性 0.039 |
| **C1 感度(O の行・一語の d)** | **✗** | d > 0 **45 / 77(58.4 %)**・中央値 +0.0258・符号検定 p **0.086**(線 = 60 % かつ p < 0.05) |

- C1 ✗ → §2・§3 の枝のとおり **Q1〜Q3 は読まない**(CUT の語と自分の語の比べの値は出していない)。

## 判定と、動かす主張(PREREG §3 の枝)

- 「一語ずつの計器は、32 token の走り込みを線(60 % かつ p < 0.05)まで拾わない」。集合(CUT の 5 語の log Σ p)では同じ型の d が立つ(olm74 Q2 = 192 / 288)。一語にすると向きは同じでも(中央値 +0.026・58 %)線に届かない。
- **olm73 Q2 ✗(自分の語の計器)は「言えない」に確定**する(一語の計器で前触れの比べはできない)。
- **一語の計器の線は閉じる**(§4 = 5 札 + 本札 = 6 札目・作り直さない)。PLAN P2-2「前触れは概念の語に出る」は「言えない」のまま。

## 記述

- C1 は線の手前(60 % まであと 2 行 = 47 / 77 で 61 %)。R3 のとおり、線は下げない。
- C0 の行 = O と L の CUT の語の在る行 129(O 77・L 52)。

## 言えないこと

- 「前触れは概念の語に出る」も「自分の語に出る」も言えない(Q1 を読んでいない)。
- 集合の d と一語の d の違いが、語の数(5 語の和)から来るのか、一語の系列の揺れから来るのかは分けていない。

## 運用の記録

- zebrashark はこの session で GitHub に届かないため、凍結の commit は `git bundle` で送り、zebrashark で `fetch` → `merge --ff-only` した。
- 出力の commit(e78fe47c)は zebrashark で作り、MacBook が SSH で取り込んだ(早送り)。LFS の中身 366 個は写して sha256 を全部照合(不一致 0)し、push した。origin・MacBook・zebrashark は同じ所。
