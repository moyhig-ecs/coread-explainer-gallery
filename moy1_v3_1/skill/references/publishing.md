# 公開(論文に添える検証 site)

## 形
- **GitHub Pages**: 図解の folder(頁 4 本・pack・kit の写し・widget の file)を公開の repo に置き、Pages で配る → `https://<account>.github.io/<repo>/<entry>/<page>.html#s15` のように状態の hash まで指せる。GitHub の repo の画面は HTML を描画しない(source が出るだけ)。無料の plan では Pages に公開の repo が要る。
- **Zenodo**: 同じ repo の release を Zenodo の GitHub 連携で凍結 → DOI。Zenodo は HTML を描画しないが、一式を落とせば `file://` で動く(fetch を使う頁なら、`python -m http.server` で開く手順を README に)。
- 稿には両方を書く: 見る = Pages の URL / 残る = Zenodo の DOI。

## 束に入れるもの
- 図解の folder(内部の層を除く)・pack と、その元の data(凍結した札の出力)・札の PREREG と RESULT・script(md5 つき)。
- **この skill の SKILL.md と references**(図解を作った手順 = プロンプト。完全な再現でなくても、手順を示せる)。
- MANIFEST(path・md5・取得 / 作成の日時)。
- Anatomy の MIT の表示(Copyright (c) 2026 Ryan)・自分の license。

## 束から外すもの
- 内部の層(`*_layer.js` / `*.css` / `README_internal.md`)— 外したあとで本体が動くこと(検査)と、本体に内輪の語が 0 件であること(grep)を確かめる。
- 外向けにしない内部の記録(研究室の政治的な memo・未公開の判定の原文)。
- scratch・巨大な中間物(必要なら LFS のまま Zenodo には入れない)。

## 外向けの操作
新しい公開の repo を作る・Pages を有効にする・Zenodo の release を作るのは外向けの操作。依頼者の確認を取ってから行う。
