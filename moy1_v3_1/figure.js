// figure.js — the table of states, the numbers the words need (ctx), the verbatim quotes, the ledger, and the draw dispatch of the moy-1 figure.
// Contract with the engine (state_machine.js): FIGURE.states · FIGURE.ctx(S) · FIGURE.draw(S, A, el, root) · FIGURE.keys[mode] · FIGURE.tRange(S) · FIGURE.focus() · FIGURE.tName(S)
// The scenes themselves are in scenes.js; the words are in i18n.js; every number comes from DATA (pack.json, written by pack_moy1.py, recounted by data.mjs).
const FIGURE = (() => {
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const narrow = () => matchMedia("(max-width:560px)").matches;
  const rowOf = (cond, seed) => DATA.rows.find((r) => r.cond === cond && r.seed === seed);
  const siteIdx = (key) => DATA.cmt13.sites.findIndex((s) => s.key === key);
  const cnt = (xs, f) => xs.filter(f).length;
  const f4 = (v) => (Math.round(v * 1e4) / 1e4).toFixed(4).replace("-", "−");
  const f2 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(2);
  const f3 = (v) => v.toFixed(3);
  const tally = (xs, key) => xs.reduce((m, x) => ((m[x[key]] = (m[x[key]] || 0) + 1), m), {});

  // ---- a verbatim quote block: the text of an excerpt, with the predicate hits marked (he = a He-Hi diameter sentence, o = an O1O2 diameter / centre sentence, at = the decision site's context)
  const qblock = (title, text, o = {}) => {
    const cuts = [...(o.spans || []).map(([k, a, b]) => [a, b, k]), ...(o.hi ? [[o.hi[0], o.hi[1], "at"]] : [])].sort((x, y) => x[0] - y[0]);
    let out = "", pos = 0;
    for (const [a, b, k] of cuts) { if (a < pos) continue; out += esc(text.slice(pos, a)) + `<mark class="${k}">` + esc(text.slice(a, b)) + "</mark>"; pos = b; }
    out += esc(text.slice(pos));
    return `<section class="q-blk${o.cls ? " " + o.cls : ""}"><h4>${title}</h4><pre>${out}</pre>${o.note ? `<p class="q-note">${o.note}</p>` : ""}</section>`;
  };
  const exc = (name) => DATA.scene[name];
  const qexc = (lang, name, label, o = {}) => { const e = exc(name), U = I18N[lang].unit; return qblock(`${label ? label + " · " : ""}${e.row} · @${e.start}–${e.end} / ${e.total} ${U}`, e.text, { spans: e.spans, ...o }); };

  const KIND = { ja: { bare: "裸の共円(stuck-L1)", o1o2: "O1O2 を直径とする円(bind)", hehi: "He・Hi を直径とする円(attractor)" }, en: { bare: "bare concyclic (stuck-L1)", o1o2: "the circle with diameter O1O2 (bind)", hehi: "the circle with diameter He-Hi (attractor)" } };
  const answerCards = (lang) => {
    const items = [["bare", "open", 3, "kg"], ["o1o2", "blocked", 1, "kb"], ["hehi", "blocked", 3, "ko"]], U = I18N[lang];
    const nOf = (k, cond) => DATA.rows.filter((r) => r.cond === cond && r.reading === k).length;
    return `<p class="q-lead">${lang === "ja" ? "答えの欄(最後の JSON の conjecture)に書かれる三つの形 — 実際の行から" : "The three shapes an answer field takes (the last JSON's conjecture) — from real rows"}</p>` + items.map(([k, cond, seed, cls]) => {
      const r = DATA.rows.find((x) => x.cond === cond && x.seed === seed);
      return qblock(`${KIND[lang][k]} · ${r.id}`, r.ans, { cls: "big " + cls, note: lang === "ja" ? `open ${DATA.open_cnt[k]} / 10 · blocked ${DATA.blk_cnt[k]} / 10 の行がこの形(cue \\n\\n)` : `open ${DATA.open_cnt[k]} / 10 · blocked ${DATA.blk_cnt[k]} / 10 rows take this shape (cue \\n\\n)` });
    }).join("");
  };
  const ratioTable = (lang) => {
    const G = DATA.geometry, ja = lang === "ja", f = (v) => v.toFixed(3);
    return `<section class="q-blk"><h4>${ja ? "中心からの距離 ÷ 半径(座標から計算・L1)" : "distance from the centre ÷ radius (computed from the coordinates, L1)"}</h4><table class="q-tab"><tr><th></th><th class="b">${ja ? "O1O2 の円" : "O1O2 circle"}</th><th class="o">${ja ? "He・Hi の円" : "He-Hi circle"}</th><th>${ja ? "橙までの隔たり" : "gap to orange"}</th><th class="b">∠O1XkO2</th></tr>`
      + [0, 1, 2, 3].map((i) => `<tr><td>X${i + 1}</td><td class="b">${f(G.ratio_O[i])}</td><td class="o">${f(G.ratio_H[i])}</td><td>${G.gap_H[i].toFixed(2)}</td><td class="b">${G.ang_O[i].toFixed(4)}°</td></tr>`).join("") + `</table><p class="q-note">${ja ? `∠O1XkO2 は 4 点とも 90° から ${Math.max(...G.ang_O.map((a) => Math.abs(a - 90))).toFixed(4)}° 以内(座標は小数 4 桁)= X1〜X4 は O1O2 を直径とする円の上(Thales の逆)。` : `∠O1XkO2 is within ${Math.max(...G.ang_O.map((a) => Math.abs(a - 90))).toFixed(4)}° of 90° at all four points (the coordinates have 4 decimals) = X1-X4 lie on the circle with diameter O1O2 (converse of Thales).`}</p></section>`
      + qblock(ja ? "二つの名指し(座標から計算)" : "the two namings (computed)", ja ? `O1O2 を直径とする円: 中心 ${fmt.pt(G.cO)}・半径 ${fmt.f4(G.rO)}\nHe・Hi を直径とする円: 中心 ${fmt.pt(G.cH)}・半径 ${fmt.f4(G.rH)}` : `circle with diameter O1O2: centre ${fmt.pt(G.cO)}, radius ${fmt.f4(G.rO)}\ncircle with diameter He-Hi: centre ${fmt.pt(G.cH)}, radius ${fmt.f4(G.rH)}`);
  };

  const headListOf = (site, lang) => {
    const ja = lang === "ja", g = (k) => site.heads.filter((h) => h.grp === k).map((h) => `${h.head} ${(h.contrib >= 0 ? "+" : "−") + Math.abs(h.contrib).toFixed(2)}`).join(" · ") || (ja ? "(なし)" : "(none)");
    return qblock(ja ? `上位 10 head(${site.kind} ${site.variant} s${site.seed} · t ${site.t})` : `top-10 heads (${site.kind} ${site.variant} s${site.seed} · t ${site.t})`,
      `${ja ? "O の組" : "O pair"}: ${g("O")}\n${ja ? "He の組" : "He pair"}: ${g("He")}\n${ja ? "どちらの組でもない" : "in neither pair"}: ${g("-")}`, { cls: "sm" });
  };
  // a hatch for the "other" category (no invariant / no JSON): a second, non-colour cue so that it is not told from grey by tone alone
  const DEFS = `<defs><pattern id="moy1-hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" class="hatch-bg"/><line x1="0" y1="0" x2="0" y2="7" class="hatch-ln"/></pattern></defs>`;
  const cueTable = (lang) => {                                     // the small table of the three cues (the frozen label's counts; cap rows removed)
    const ja = lang === "ja", CT = DATA.cue_table, ks = ["nl", "sp", "nn"], disp = { nl: "\\n", sp: "␣", nn: "\\n\\n" }, L = ["B-bind", "B-attractor", "B-stuck-L1", "B-flail"], hd = ["bind", "attractor", "stuck-L1", "flail"];
    const row = (k, cond) => { const c = CT[k][cond]; return `<tr><td>${disp[k]}</td><td>${cond}</td>${L.map((l) => `<td class="${l === "B-bind" ? "b" : l === "B-attractor" ? "o" : ""}">${c.labels_primary[l] || 0}</td>`).join("")}<td>${c.n_primary}${c.cap ? ` (cap ${c.cap})` : ""}</td><td>${c.mode.replace("B-", "")}</td></tr>`; };
    return `<section class="q-blk"><h4>${ja ? "cue ごとの凍結の label の数(cap の行を除く)" : "frozen-label counts per cue (cap rows removed)"}</h4><table class="q-tab"><tr><th>cue</th><th></th>${hd.map((h) => `<th>${h}</th>`).join("")}<th>n</th><th>${ja ? "最頻" : "mode"}</th></tr>${ks.map((k) => row(k, "blocked")).join("")}${ks.map((k) => row(k, "open")).join("")}</table></section>`
      + `<p class="q-lead">${ja ? "cue = prompt の直後に足す文字(␣ = 空白)。同じ model・同じ prompt・cue だけが違う。" : "cue = the characters put right after the prompt (␣ = a space). Same model, same prompt; only the cue differs."}</p>`;
  };

  // ---- v2: the olm59 chapter. The group order and names; the flags are bits of the token's mask (o_name 0 · h_name 1 · o_diam 2 · h_diam 3 · circle 4 · json 5)
  const GN = ["close", "mid", "ans", "think"], BITN = ["o_name", "h_name", "o_diam", "h_diam", "circle", "json"];
  const sgn0 = (v) => (v > 0 ? "+" : v < 0 ? "−" : "±") + Math.abs(v), sgn2 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(2), sgn3 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3);
  const trajRowOf = (st) => (st.opt && st.opt.row === "H" ? DATA.olm59.S_H : DATA.olm59.S_O);
  function trajInfo(S, st) {                                                  // what is under the cursor: for each drawn row the token, its mask, the active predicates, the four group values
    const D = DATA.olm59, both = st.opt.row === "both", HF = D.half;
    return (both ? [D.S_O, D.S_H] : [trajRowOf(st)]).map((R) => { const i = both ? R.event - HF + clamp(S.t, 0, 2 * HF - 1) : clamp(S.t, 0, R.n - 1), mask = R.mask[i]; return { R, i, mask, bits: [0, 1, 2, 3, 4, 5].filter((b) => (mask >> b) & 1), vals: GN.map((g) => R.series[g][i]) }; });
  }
  // the construction (chapter 1's coordinates) as a small flat inset: what lights up is what the text under the cursor names (the predicates' hits), not a reading of the model
  const geomBox = (() => { const G = DATA.geometry, rings = [[G.pts.O1, G.rad.K1], [G.pts.O2, G.rad.K2], [G.cO, G.rO], [G.cH, G.rH]]; let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9; for (const [c, r] of rings) { x0 = Math.min(x0, c[0] - r); x1 = Math.max(x1, c[0] + r); y0 = Math.min(y0, c[1] - r); y1 = Math.max(y1, c[1] + r); } return { x0: x0 - 2, x1: x1 + 2, y0: y0 - 2, y1: y1 + 2 }; })();
  function insetSvg(lang, mask, o = {}) {
    const G = DATA.geometry, B = geomBox, W = 400, sx = W / (B.x1 - B.x0), H = Math.round((B.y1 - B.y0) * sx), fs = o.small ? 21 : 13, on = (b) => ((mask >> b) & 1) === 1;
    const X = (x) => ((x - B.x0) * sx).toFixed(1), Y = (y) => ((B.y1 - y) * sx).toFixed(1), R = (r) => (r * sx).toFixed(1), P = (k) => `${X(G.pts[k][0])},${Y(G.pts[k][1])}`;
    const oOn = on(2), hOn = on(3), oNm = on(0) || oOn, hNm = on(1) || hOn, pr = (k, kind, lit, dx, dy) => `<circle class="in-pt in-pt-${kind}${lit ? " on" : ""}" cx="${X(G.pts[k][0])}" cy="${Y(G.pts[k][1])}" r="${lit ? (o.small ? 11 : 8) : (o.small ? 7 : 5)}"/><text class="in-tx in-tx-${kind}" x="${(+X(G.pts[k][0]) + dx).toFixed(1)}" y="${(+Y(G.pts[k][1]) + dy).toFixed(1)}" style="font-size:${fs}px">${k}</text>`;
    const nm = I18N[lang].tags;
    return `<svg class="fig-inset" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(nm.insetAria)}" xmlns="http://www.w3.org/2000/svg"><rect class="in-bg" x="1" y="1" width="${W - 2}" height="${H - 2}" rx="6"/>`
      + `<circle class="in-ring-k" cx="${X(G.pts.O1[0])}" cy="${Y(G.pts.O1[1])}" r="${R(G.rad.K1)}"/><circle class="in-ring-k" cx="${X(G.pts.O2[0])}" cy="${Y(G.pts.O2[1])}" r="${R(G.rad.K2)}"/>`
      + `<circle class="in-ring-o${oOn ? " on" : ""}" cx="${X(G.cO[0])}" cy="${Y(G.cO[1])}" r="${R(G.rO)}"/><circle class="in-ring-h${hOn ? " on" : ""}" cx="${X(G.cH[0])}" cy="${Y(G.cH[1])}" r="${R(G.rH)}"/>`
      + `<path class="in-seg-o${oOn ? " on" : ""}" d="M${P("O1")}L${P("O2")}"/><path class="in-seg-h${hOn ? " on" : ""}" d="M${P("He")}L${P("Hi")}"/>`
      + pr("O1", "o", oNm, -4, o.small ? -16 : -11) + pr("O2", "o", oNm, o.small ? 12 : 9, o.small ? 24 : 15) + pr("He", "h", hNm, o.small ? 13 : 9, o.small ? -10 : -7) + pr("Hi", "h", hNm, o.small ? 13 : 9, o.small ? 24 : 15)
      + ["X1", "X2", "X3", "X4"].map((k) => `<circle class="in-pt in-pt-x" cx="${X(G.pts[k][0])}" cy="${Y(G.pts[k][1])}" r="${o.small ? 6 : 4.4}"/><text class="in-tx in-tx-x" x="${(+X(G.pts[k][0]) + (o.small ? 11 : 8)).toFixed(1)}" y="${(+Y(G.pts[k][1]) - (o.small ? 8 : 6)).toFixed(1)}" style="font-size:${fs}px">${k}</text>`).join("")
      + `<text class="in-cap${on(5) ? " on" : ""}" x="10" y="${fs + 8}" style="font-size:${fs}px">${esc(on(5) ? nm.insetJson : nm.insetNoJson)}</text></svg>`;
  }
  const insetBlock = (lang, infos, st) => {                                    // the inset(s) and the line that says what lights
    const T = I18N[lang].tags, names = (i) => (i.bits.filter((b) => b < 4 || b === 5).map((b) => T.bitName[b]).join(" · ") || T.noneLit), single = infos.length === 1;
    return `<section class="q-blk in-blk"><h4>${esc(T.insetHead)}</h4><div class="in-row">${infos.map((i, k) => `<figure class="in-fig">${insetSvg(lang, i.mask, { small: !single && !narrow() })}<figcaption>${esc(single ? `token ${i.i}` : (k === 0 ? "S_O" : "S_H") + ` · token ${i.i}`)} — ${esc(names(i))}</figcaption></figure>`).join("")}</div><p class="q-note">${esc(T.insetNote)}</p></section>`;
  };
  const excerptBlock = (lang, R, label) => {                                   // the 32 + 32 tokens around the event, verbatim; the predicate's hit marked (blue = an O1O2 sentence, orange = a He-Hi sentence)
    const T = I18N[lang], x = R.excerpt, text = x.pre + x.hit + x.post, kind = R.event_flag === "o_diam" ? "o" : "he", w = R.wordcirc;
    // v3 (transplanted from the other maker's state 18): in S_O the sentence that says the same circle in words is underlined (it names neither O1 nor O2: no predicate hits it) and sits inside the "before 32" window
    const spans = [...(w ? [["wc", w.char_a - x.chars[0], w.char_b - x.chars[0]]] : []), [kind, x.pre.length, x.pre.length + x.hit.length]];
    return qblock(`${w ? "" : label + " · "}${R.id.replace(/__/g, " ").replace(" r", " r")} · token ${x.tok_a}–${x.tok_b - 1} · @${x.chars[0]}–${x.chars[1]} / ${R.chars} ${T.unit}`, text, { spans, note: w ? T.tags.wcNote(w, R) : T.tags.excNote });
  };
  const winTable = (lang) => {                                                 // S_O and S_H, before / after / difference, per group (the numbers behind state 20)
    const T = I18N[lang].tags, D = DATA.olm59, f = (v) => v.toFixed(2);
    return `<section class="q-blk"><h4>${esc(T.winHead)}</h4><table class="q-tab"><tr><th></th><th class="b" colspan="3">S_O</th><th class="o" colspan="3">S_H</th></tr><tr><th></th>${["bf", "af", "df", "bf", "af", "df"].map((k) => `<th>${T[k]}</th>`).join("")}</tr>`
      + GN.map((g, gi) => `<tr><td>${T.grp[gi]}</td>${[D.S_O, D.S_H].map((R) => `<td>${f(R.before[gi])}</td><td>${f(R.after[gi])}</td><td class="${R === D.S_O ? "b" : "o"}">${sgn2(R.after[gi] - R.before[gi])}</td>`).join("")}</tr>`).join("") + `</table></section>`;
  };
  const aggTable = (lang) => {
    const T = I18N[lang].tags, D = DATA.olm59, rows = [];
    for (const [ev, cls, nm] of [["o_diam", "b", T.evO], ["h_diam", "o", T.evH]]) {
      rows.push(`<tr class="grp"><td class="${cls}" colspan="6">${esc(nm)}</td></tr>`);
      for (const [oc, nmk] of [["all", "ocAll"], ["B-bind", "ocBind"], ["B-attractor", "ocAttr"]]) {
        const g0 = D.agg[ev].groups.close[oc], small = g0.n < 8;
        rows.push(`<tr class="${small ? "dim" : ""}"><td>${T[nmk]}</td><td>${g0.n}</td>${GN.map((g) => { const c = D.agg[ev].groups[g][oc]; return `<td>${small ? "—" : `${c.up}<small>${sgn3(c.med)}</small>`}</td>`; }).join("")}</tr>`);
      }
      const rest = D.agg[ev].groups.close.all.n - D.agg[ev].groups.close["B-bind"].n - D.agg[ev].groups.close["B-attractor"].n;           // v3: the rows whose answer field is neither bind nor attractor (stuck-L1 · flail): n adds up
      if (rest > 0) rows.push(`<tr class="dim"><td>${T.ocOther}</td><td>${rest}</td>${GN.map(() => "<td>—</td>").join("")}</tr>`);
    }
    return `<section class="q-blk"><h4>${esc(T.aggHead)}</h4><table class="q-tab agg"><tr><th></th><th>n</th>${T.grpS.map((x) => `<th>${x}</th>`).join("")}</tr>${rows.join("")}</table><p class="q-note">${esc(T.aggNote)}</p></section>`
      + `<section class="q-blk"><h4>${esc(T.predHead)}</h4><table class="q-tab"><tr><th></th><th>${T.thr}</th><th>${T.got}</th><th></th></tr>`
      + ["Q1", "Q2"].map((q) => `<tr><td class="${q === "Q1" ? "b" : "o"}">${q}</td><td>≥ ${Math.round(D[q].thr * 100)} %</td><td>${D[q].up} / ${D[q].n} (${Math.round((D[q].up / D[q].n) * 100)} %)</td><td>✗</td></tr>`).join("") + `</table><p class="q-note">Q1: ${esc(T.q1)}<br>Q2: ${esc(T.q2)}</p></section>`;
  };
  const labelTable = (lang) => {                                               // read.json labels_full_vs_answer_field: path | the whole-text label -> the answer-field label | rows
    const T = I18N[lang].tags, D = DATA.olm59.labels, ord = { think: 0, answer: 1, natural: 2 }, lo = { "B-bind": 0, "B-attractor": 1, "B-stuck-L1": 2, "B-flail": 3 };
    const rows = Object.entries(D).map(([k, n]) => { const [kind, full, field] = k.split("|"); return { kind, full, field, n }; }).sort((a, b) => ord[a.kind] - ord[b.kind] || lo[a.full] - lo[b.full] || lo[a.field] - lo[b.field]);
    const cls = (l) => (l === "B-bind" ? "b" : l === "B-attractor" ? "o" : "");
    return `<section class="q-blk"><h4>${esc(T.labHead)}</h4><table class="q-tab lab"><tr><th>${T.path}</th><th>${T.lab2Full}</th><th></th><th>${T.lab2Field}</th><th>n</th></tr>`
      + rows.map((r) => `<tr class="${r.full === r.field ? "" : "chg"}"><td>${T.paths[r.kind]}</td><td class="${cls(r.full)}">${r.full.replace("B-", "")}</td><td>→</td><td class="${cls(r.field)}">${r.field.replace("B-", "")}</td><td>${r.n}</td></tr>`).join("") + `</table><p class="q-note">${esc(T.labNote)}</p></section>`;
  };
  // ---- v2.1: the tables beside olm62's two states (every value is read.json's / control.json's own)
  const scatTable = (lang) => {
    const T = I18N[lang].tags, R = DATA.olm62.read, r3 = (v) => v.toFixed(3);
    return `<section class="q-blk"><h4>${esc(T.scatTabHead)}</h4><table class="q-tab nw"><tr><th></th><th>n</th><th>${esc(T.mathMoves)}</th><th>${esc(T.rhoTab)}</th><th>${esc(T.splitTab)}</th></tr>`
      + [["O1O2", "b", R.o_diam], ["He・Hi", "o", R.h_diam]].map(([nm, cls, r]) => `<tr><td class="${cls}">${nm}</td><td>${r.n}</td><td>${r.math_up} / ${r.n}</td><td>${r3(r.spearman_mid_math)}</td><td>${r.split_at_median_math.low} · ${r.split_at_median_math.high}</td></tr>`).join("")
      + `<tr><td>${esc(T.allTok)}</td><td>${fmt.n(R.n_tokens)}</td><td></td><td>${r3(R.Q3_pooled_token_spearman_mid_math)}</td><td></td></tr></table><p class="q-note">${esc(T.scatNote)}</p></section>`
      // v3.1 (D2: both readers): the tie-averaged values sit in a box of their own, every value visible (entry P #s22) — in v3 they were the last row of the table and were cut at the column's edge
      + `<section class="q-blk af-out"><h4>${esc(T.tieHead)}</h4><p class="q-note">${esc(T.tieBox(R, DATA.olm62.tie))}</p></section>`;
  };
  const flatTable = (lang) => {
    const T = I18N[lang].tags, D = DATA.olm62, R = D.read, x = flatInfoOf(), f3 = (v) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(3);
    return `<section class="q-blk"><h4>${esc(T.flatTabHead)}</h4><table class="q-tab nw"><tr><th></th><th>${esc(T.flatNoMove)}</th><th>${esc(T.flatMove)}</th></tr>`
      + [["O1O2", "b", R.o_diam], ["He・Hi", "o", R.h_diam]].map(([nm, cls, r]) => `<tr><td class="${cls}">${nm}</td><td>${r.mid_up_when_math_flat} · ${f3(r.mid_median_when_math_flat)}</td><td>${r.mid_up_when_math_up}</td></tr>`).join("")
      + `</table><p class="q-note">${esc(T.flatQ2)}: ${Math.round(x.thr * 100)} % → ${x.need} / ${x.n} · ${x.up} / ${x.n} = ${Math.round((x.up / x.n) * 100)} % ✓</p><p class="q-note">${esc(T.flatRules(x, DATA.olm62.read))}</p></section>`
      + `<section class="q-blk"><h4>${esc(T.flatCtlHead)}</h4><table class="q-tab"><tr><td>${esc(T.ctlC1)}</td><td>${esc(T.ctlC1v(D.control.C1))} ✓</td></tr><tr><td>${esc(T.ctlC2)}</td><td>${esc(T.ctlC2v(D.control.C2))} ✓</td></tr></table></section>`;
  };
  const diffBlock = (lang) => { const e = DATA.f5.edit, T = I18N[lang].tags; return qblock(T.diffHead, `− ${e.key}\n${e.replacement.split("\n").map((l) => "+ " + l).join("\n")}`, { cls: "sm dif", note: T.diffNote(DATA.f5) }); };
  const wordCircBlock = (lang) => { const w = DATA.olm59.S_O.wordcirc, T = I18N[lang].tags; return qblock(T.wcHead(w), w.text, { cls: "sm dif", note: T.wcNote(w, DATA.olm59.S_O) }); };
  const STATES = [
    { chapter: "problem", mode: "geom", cam: [86, 58, 1, 0], camN: [90, 80, 1, 0], Hn: 640, t: 0, opt: { show: "bare" }, quote: true, keys: ["wO", "wHe", "wX", "bare"] },
    { chapter: "problem", mode: "geom", cam: [86, 58, 1, 0], camN: [90, 80, 1, 0], Hn: 640, t: 0, opt: { show: "named" }, quote: true, keys: ["wO", "wHe", "wX", "ringO", "ringH"] },
    { chapter: "prompts", mode: "sheets", cam: [84, 52, 1, 0], camN: [90, 72, 1, 0], Hn: 520, t: 0, opt: { both: false }, quote: true, qw: 600, keys: ["seg", "seg2"] },
    { chapter: "prompts", mode: "sheets", cam: [84, 52, 1, 0], camN: [90, 72, 1, 0], Hn: 520, t: 0, opt: { both: true }, quote: true, qw: 520, keys: ["seg", "tail"] },
    { chapter: "open", mode: "bands", cam: [82, 50, 1, 0], camN: [90, 74, 1, 0], Hn: 1060, t: () => 3, opt: { conds: ["open", "blocked"], focusCond: "open", otok: true }, pos: "row", keys: ["bind", "att", "bare", "oth", "pinHe", "pinO", "pinOt", "pinA", "frz", "ghost"] },
    { chapter: "open", mode: "tiers", cam: [82, 40, 1, 0], camN: [90, 74, 1, 0], Hn: 640, t: () => 1, opt: {}, pos: "row", keys: ["att", "bare", "oth", "pinHe", "bind"] },
    { chapter: "open", mode: "bands", cam: [82, 46, 1, 0], camN: [90, 74, 1, 0], Hn: 760, t: () => 3, opt: { cond: "open", fade: true, otok: true }, pos: "row", quote: true, keys: ["bare", "pinA", "frz"] },
    { chapter: "open", mode: "bands", cam: [82, 46, 1, 0], camN: [90, 74, 1, 0], Hn: 760, t: () => 1, opt: { cond: "open", fade: true, otok: true }, pos: "row", quote: true, keys: ["bare", "pinHe", "pinOt", "pinA", "frz"] },
    { chapter: "blocked", mode: "bands", cam: [82, 50, 1, 0], camN: [90, 74, 1, 0], Hn: 1060, t: () => 3, opt: { conds: ["open", "blocked"], focusCond: "blocked", emph: [1] }, pos: "row", quote: true, keys: ["bind", "att", "bare", "pinHe", "pinO", "pinA", "frz", "ghost"] },
    { chapter: "blocked", mode: "hyp", cam: [80, 42, 1, 0], camN: [90, 72, 1, 0], Hn: 700, t: () => 3, opt: {}, pos: "row", keys: ["bind", "att", "bare", "oth"] },
    { chapter: "blocked", mode: "bands", cam: [82, 46, 1, 0], camN: [90, 74, 1, 0], Hn: 760, t: () => 2, opt: { cond: "blocked", fade: true }, pos: "row", quote: true, keys: ["bind", "pinHe", "pinO", "pinA", "frz"] },
    { chapter: "blocked", mode: "cue", quote: true, qw: 610, cam: [86, 38, 1, 0], camN: [90, 40, 1, 0], Hn: 640, t: 0, opt: {}, keys: ["bind", "att", "bare", "flail"] },
    { chapter: "moment", mode: "timeline", cam: [82, 38, 1, 0], camN: [90, 70, 1, 0], Hn: 420, t: 0, opt: {}, quote: true, keys: ["pinHe", "pinO", "pinA"] },
    { chapter: "moment", mode: "balance", cam: [80, 22, 1, 0], camN: [90, 12, 1, 0], Hn: 520, t: () => siteIdx("att|F5a-2|s1"), opt: {}, pos: "site", quote: true, keys: ["bind", "att", "l50"] },
    { chapter: "moment", mode: "balance", cam: [80, 22, 1, 0], camN: [90, 12, 1, 0], Hn: 520, t: () => siteIdx("cut|F5a-2|s1"), opt: {}, pos: "site", quote: true, keys: ["bind", "att", "l50"] },
    { chapter: "moment", mode: "pillars", cam: [82, 50, 1, 0], camN: [90, 64, 1, 0], Hn: 700, t: 0, opt: {}, keys: ["bind", "att", "bare", "l50"] },
    { chapter: "models", mode: "models", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1060, t: 0, opt: {}, keys: ["bind", "att", "bare", "flail"] },
    { chapter: "models", mode: "think", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 980, Hw: 440, t: 0, opt: {}, keys: ["bind", "att", "bare", "len"] },
    { chapter: "sae", mode: "traj", cam: [90, 44, 1, 0], camN: [90, 58, 1, 0], Hn: 800, Hw: 430, t: () => DATA.olm59.S_O.event, opt: { row: "O" }, pos: "tok", quote: true, keys: ["rib", "win", "mean", "evt", "mk", "mkJ"] },
    { chapter: "sae", mode: "traj", cam: [90, 44, 1, 0], camN: [90, 58, 1, 0], Hn: 800, Hw: 430, t: () => DATA.olm59.S_H.event, opt: { row: "H" }, pos: "tok", quote: true, keys: ["rib", "win", "mean", "evt", "mk", "mkJ"] },
    { chapter: "sae", mode: "traj", cam: [90, 44, 1, 0], camN: [90, 58, 1, 0], Hn: 900, Hw: 560, t: () => DATA.olm59.half, opt: { row: "both" }, pos: "rel", quote: true, keys: ["rib", "win", "mean", "evt", "mk"] },
    { chapter: "sae", mode: "agg", cam: [90, 40, 1, 0], camN: [90, 52, 1, 0], Hn: 520, Hw: 400, t: 0, opt: {}, quote: true, keys: ["colO", "colH", "ref50", "thr"] },
    { chapter: "sae", mode: "slope", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1800, Hw: 580, t: 0, opt: {}, quote: true, qw: 440, keys: ["colO", "colH", "afMed", "afScene"] },
    { chapter: "sae", mode: "scat", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1400, Hw: 640, t: 0, opt: {}, quote: true, keys: ["evO", "evH", "ring"] },
    { chapter: "sae", mode: "flat", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1360, Hw: 612, t: 0, opt: {}, quote: true, keys: ["dotUp", "dotDn", "fthr"] },
    { chapter: "sae", mode: "lab2", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 980, Hw: 540, t: 0, opt: {}, quote: true, keys: ["bind", "att", "bare", "flail", "bindbox"] },
    { chapter: "tree", mode: "tree", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 2640, Hw: 600, t: 0, opt: {}, keys: ["mine", "outer"] },
    // ---- v3: the part added after the 10-28 figure (states 27-36: the flow · (a) L3 -> olm76 · (b) inference space x 2 · (c) structure that is not words x 2 · (d) apex proof x 2 · the next question x 2)
    { chapter: "flow", mode: "flow", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1800, Hw: 835, t: 0, opt: {}, quote: true, qw: 430, keys: ["afThick", "afDot", "afGj", "afGk", "afGd", "afGn", "afHatch"] },
    { chapter: "l3", mode: "l3", cam: [88, 34, 1, 0], camN: [90, 50, 1, 0], Hn: 900, Hw: 600, t: 0, opt: {}, quote: true, qw: 500, keys: ["afL3b", "afL3g", "afL3o", "ref50", "afHatch"] },
    { chapter: "space", mode: "space1", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1760, Hw: 600, t: 0, opt: {}, quote: true, qw: 460, keys: ["afL32", "afL48", "afJ", "afW", "afNull"] },
    { chapter: "space", mode: "space2", cam: [84, 30, 1, 0], camN: [90, 52, 1, 0], Hn: 920, Hw: 600, t: 0, opt: {}, quote: true, qw: 460, keys: ["afL32b", "afL48b", "afZero", "afPost"] },
    { chapter: "struct", mode: "struct1", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1560, Hw: 540, t: 0, opt: {}, quote: true, qw: 460, keys: [] },
    { chapter: "struct", mode: "struct2", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1500, Hw: 740, t: 0, opt: {}, quote: true, qw: 460, keys: ["afPo", "afVo"] },
    { chapter: "apex", mode: "apex1", cam: [86, 34, 1, 0], camN: [90, 52, 1, 0], Hn: 900, Hw: 600, t: 0, opt: {}, quote: true, qw: 520, keys: ["afApexB", "afApexG"] },
    { chapter: "apex", mode: "apex2", cam: [86, 34, 1, 0], camN: [90, 52, 1, 0], Hn: 900, Hw: 600, t: 0, opt: {}, quote: true, qw: 520, keys: ["afK12", "afK0"] },
    { chapter: "next", mode: "next1", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1560, Hw: 600, t: 0, opt: {}, quote: true, qw: 680, keys: ["afBind", "afNot"] },
    { chapter: "next", mode: "next2", cam: [58, 24, 1, 0], camN: [90, 74, 1, 0], Hn: 1560, Hw: 600, t: 0, opt: {}, quote: true, qw: 440, keys: [] },
    { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: 0, opt: {}, cols: ["L1", "L3"], part: "v1", keys: [] },
    { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: 0, opt: {}, cols: ["L1", "L3"], part: "v2", keys: [] },
    { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: 0, opt: {}, cols: ["L1", "L3"], part: "v21", keys: [] },
    { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: 0, opt: {}, cols: ["L1"], part: "v3", keys: [] },
    { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: 0, opt: {}, cols: ["L3", "x"], part: "v3", keys: [] },
    { chapter: "ledger", mode: "ledger", cam: [58, 24, 1, 0], t: 0, opt: {}, cols: ["x", "q"], part: "base", keys: [] },
  ];

  // the words need these (never typed: every value is read from DATA)
  function ctx(S) {
    const op = DATA.rows.filter((r) => r.cond === "open"), bl = DATA.rows.filter((r) => r.cond === "blocked"), st = STATES[S.state], cond = (st.opt && (st.opt.focusCond || st.opt.cond)) || "open";
    const row = (st.mode === "bands" || st.mode === "tiers" || st.mode === "hyp") ? rowOf(st.mode === "tiers" ? "open" : st.mode === "hyp" ? "blocked" : cond, clamp(S.t, 0, 9)) : null;
    const sites = DATA.cmt13.sites, site = sites[clamp(S.t, 0, sites.length - 1)], sa = sites[siteIdx("att|F5a-2|s1")], sb = sites[siteIdx("cut|F5a-2|s1")], G = DATA.geometry, J = DATA.cmt13.jaccard;
    const frozenOpen = tally(op, "label"), frozenBlk = tally(bl, "label");
    return {
      t: S.t, row, site, sa, sb, G, J, op, bl, open: DATA.open_cnt, blk: DATA.blk_cnt, oSent: DATA.o_sent, heSent: DATA.he_sent, hw: DATA.hehi_word_rows, P: DATA.prompts, cue: DATA.cue_table, f5: DATA.f5,
      frozenOpen, frozenBlk, jf: DATA.json_first, heEnd: DATA.he_end, orderHeFirst: DATA.order_he_first, openTok: DATA.open_tok_rows, l50r1: DATA.cmt13.l50_rank1, l50t10: DATA.cmt13.l50_top10,
      cmt5: DATA.cmt5, c5ctl: DATA.cmt5_ctl, models: DATA.models, think: DATA.think, ctl: DATA.cmt13.controls, nSites: sites.length, nAtt: cnt(sites, (s) => s.kind === "att"), nCut: cnt(sites, (s) => s.kind === "cut"),
      f4, f2, f3, openCap: cnt(op, (r) => r.hit_cap), seg: DATA.seg,
      otok: DATA.otok_ctx, attrOpen: DATA.attr_open, headList: (lang) => headListOf(site, lang), changedOpen: DATA.changed_open,
      qblock, qexc, exc, esc, rowOf, siteIdx, lang: S.lang, answerCards, ratioTable, cueTable,
      o59: DATA.olm59, tj: st.mode === "traj" ? trajInfo(S, st) : null, sgn2, sgn3, GN,
      af: DATA.after, cs: DATA.cue_start, afq: (name) => SCENES.__q[name](S.lang),
      o62: DATA.olm62, tree: DATA.tree, treeInfo: treeInfoOf(), flat: flatInfoOf(), card: S.card || null, scatTable, flatTable,
      insetBlock: () => insetBlock(S.lang, trajInfo(S, st), st), excerptBlock, winTable, aggTable, labelTable, diffBlock: () => diffBlock(S.lang), wordCircBlock: () => wordCircBlock(S.lang),
    };
  }
  const ledgerHtml = (S) => {
    const T = I18N[S.lang].ledger, Q = ctx(S), st = STATES[S.state], cols = st.cols, li = { L1: 0, L3: 1, x: 2, q: 3 }, v2 = (id) => /^(?:K(?:2[2-9])|R0[34])$/.test(id), v21 = (id) => /^(?:K(?:3\d|4\d)|R0[56])$/.test(id), v3 = (id) => /^(?:K(?:5\d|6\d)|R(?:0[7-9]|1[01])|X(?:1[7-9]|2\d))$/.test(id), partOf = (id) => (v3(id) ? "v3" : v21(id) ? "v21" : v2(id) ? "v2" : "v1");      // v2's rows (the chapter "construction x SAE" and cmt5's two labels) have their own ledger state
    const rows = T.rows(Q).filter((r) => !st.part || (st.part === "base" ? partOf(r.id) !== "v3" : partOf(r.id) === st.part)), heads = st.part === "v3" ? T.colsV3 : st.part === "v21" ? T.colsV21 : st.part === "v2" ? T.colsV2 : T.cols;
    const body = (lv) => lv === "q" ? T.questions(Q).map((x) => `<article><b>${esc(x.k)}</b> ${esc(x.q)}<span class="src">${esc(x.where)}</span></article>`).join("")
      : rows.filter((r) => r.lv === lv).map((r) => `<article><b>${T.tag[lv]}</b> ${esc(r.text)}<span class="src">${esc(r.id)} · ${esc(r.src)}</span></article>`).join("");
    return cols.map((lv) => `<section data-lv="${lv}"><h3>${esc(heads[li[lv]])}</h3>${body(lv)}</section>`).join("");
  };
  const canvas = (S, root) => {
    const q = !!STATES[S.state].quote, video = root.dataset.video === "1";
    if (narrow()) return { W: 780, H: STATES[S.state].Hn || 700, narrow: true, video, fs: 23.5, u: 23.5 / 12 };
    const fs = video ? 13.5 : 12, qw = STATES[S.state].qw || 430;
    return { W: q ? 1000 - (qw - 430) : 1440, H: STATES[S.state].Hw || 600, narrow: false, video, fs, u: fs / 12 };
  };
  return {
    states: STATES,
    keys: {},
    tRange(S) { const st = STATES[S.state], m = st.mode; return m === "bands" || m === "tiers" || m === "hyp" ? [0, 9] : m === "balance" ? [0, DATA.cmt13.sites.length - 1] : m === "traj" ? (st.opt.row === "both" ? [0, 2 * DATA.olm59.half - 1] : [0, trajRowOf(st).n - 1]) : [0, 0]; },
    focus() { return 0; },
    tName(S) { const st = STATES[S.state], m = st.mode; if (m === "traj") return st.opt.row === "both" ? sgn0(S.t - DATA.olm59.half) : `${S.t}`; if (m === "balance") { const s = DATA.cmt13.sites[clamp(S.t, 0, DATA.cmt13.sites.length - 1)]; return `${s.kind} ${s.variant} s${s.seed} (t ${s.t})`; } return m === "bands" || m === "tiers" || m === "hyp" ? `s${S.t}` : S.t; },
    ctx,
    canvas,
    mapState() { return STATES.findIndex((s) => s.mode === "tree"); },
    marks(S) {                                                                 // the card marks of the header: the cards this state's data comes from (config.json card_marks) · the ledger gets one mark for "all of them"
      const st = STATES[S.state], T = I18N[S.lang].tags, ids = DATA.config.card_marks[S.state] || [], tip = T.markTitle(this.mapState());
      if (st.mode === "ledger") return [{ id: "*", text: T.markAll, title: tip, zone: "" }];
      return ids.map((id) => ({ id, text: T.markText(id, DATA.tree), title: tip, zone: DATA.tree.cards[id].zone }));
    },
    draw(S, A, el, root) {
      const st = STATES[S.state], cv = canvas(S, root);
      if (cv.narrow && (st.mode === "flow" || st.mode === "next2")) { const probe = { ...cv, H: 8000 }; SCENES[st.mode](S, A, probe, st); if (probe.used) cv.H = Math.ceil(probe.used + 28); }   // v3: on a phone the flow's rows take the height their words need (the scene reports where it ended)
      el.svg.setAttribute("viewBox", `0 0 ${cv.W} ${cv.H}`);
      el.pic.innerHTML = st.mode === "ledger" ? "" : DEFS + SCENES[st.mode](S, A, cv, st);
      el.ledger.innerHTML = st.mode === "ledger" ? ledgerHtml(S) : "";
    },
  };
})();
