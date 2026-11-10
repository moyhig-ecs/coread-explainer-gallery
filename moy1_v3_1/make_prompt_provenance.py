#!/usr/bin/env python3
"""make_prompt_provenance.py — cards/PROMPT_PROVENANCE.md: where the question text of the moy-1 figure comes from, with md5 at each stage.

Inputs (all inside this bundle; nothing is imported or run from ConstructGap):
  data/probes/moy1-claude5-replication/results/replication_config_frozen.json   the frozen open / blocked / selection-supply texts and their md5
  data/probes/olmo3-f5-think-prefix/results/f5_runs_F5a-2.json, f5_runs_F5b-1.json  the F5 edits (verbatim) and the md5 of the texts OLMo received
  data/probes/olmo3-pc1-cue-invariance/results/pc1_runs.json, data/probes/olmo3-base-bf16-screen/results/screen_olmo3_base_bf16.json   the cues
  cards/public_constructgap_v1_0_1_literals.json   literals of the public ConstructGap v1.0.1 read as text (ast.literal_eval; no import, no run)
Chain:  open (ConstructGap prompts.build('higashida_circle', 'A', 37), frozen 07-28) --+ closure-forcing append--> blocked --+ cue--> what OLMo received
        blocked --F5a-2 / F5b-1 edit--> + cue "\\n\\n" --> the F5 rows (olm59's rows are F5a-2 / F5b-1).

    python3 -I make_prompt_provenance.py        (exit 1 on any md5 mismatch)
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
D = HERE / "data" / "probes"
md5 = lambda s: hashlib.md5(s.encode()).hexdigest()
J = lambda p: json.loads(p.read_text(encoding="utf-8"))


def main() -> int:
    cfg = J(D / "moy1-claude5-replication/results/replication_config_frozen.json")
    fa, fb = J(D / "olmo3-f5-think-prefix/results/f5_runs_F5a-2.json"), J(D / "olmo3-f5-think-prefix/results/f5_runs_F5b-1.json")
    pc1 = J(D / "olmo3-pc1-cue-invariance/results/pc1_runs.json")
    scr = J(D / "olmo3-base-bf16-screen/results/screen_olmo3_base_bf16.json")
    pub = J(HERE / "cards" / "public_constructgap_v1_0_1_literals.json")
    arms = pub["files"]["probe_registry.py"]["literals"]["ARMS_APPEND"]["higashida_circle"]
    O, B = cfg["prompts"]["open"], cfg["prompts"]["blocked"]
    cues = {"nl": "\n", "space": " ", "nlnl": "\n\n"}
    assert {r["cue"] for r in scr["rows"]} == {"\n"}
    assert {(r["cue_tag"], r["cue"]) for r in pc1["rows"]} <= {("space", " "), ("nlnl", "\n\n")}
    assert fa["cue"] == fb["cue"] == "\n\n" and fa["condition"] == fb["condition"] == "blocked"
    ea, eb = fa["edits_applied"], fb["edits_applied"]
    assert len(ea) == len(eb) == 1 and B.count(ea[0]["key"]) == 1 and B.count(eb[0]["key"]) == 1
    FA, FB = B.replace(ea[0]["key"], ea[0]["replacement"], 1), B.replace(eb[0]["key"], eb[0]["replacement"], 1)
    rows = [  # stage, how, text, frozen md5 (or None), where the frozen value is written
        ("open", "prompts.build('higashida_circle', 'A', 37)['prompt'] as frozen 07-28 (not regenerated here)", O, cfg["prompt_md5"]["open"], "replication_config_frozen.json prompt_md5.open"),
        ("closure-forcing append", "ConstructGap v1.0.1 probe_registry.py ARMS_APPEND['higashida_circle']['closure-forcing'] (literal)", arms["closure-forcing"], None, "—"),
        ("blocked", "open + closure-forcing append", O + arms["closure-forcing"], cfg["prompt_md5"]["blocked"], "replication_config_frozen.json prompt_md5.blocked"),
        ("selection-supply", "open + ARMS_APPEND['higashida_circle']['selection-supply'] (literal)", O + arms["selection-supply"], cfg["prompt_md5"]["selection-supply"], "replication_config_frozen.json prompt_md5.selection-supply"),
        ("open + cue \\n", "screen bf16 (cue \\n)", O + cues["nl"], None, "—"),
        ("blocked + cue \\n", "screen bf16 (cue \\n)", B + cues["nl"], None, "—"),
        ("blocked + cue ' '", "pc1 cue 'space'", B + cues["space"], None, "—"),
        ("blocked + cue \\n\\n", "pc1 cue 'nlnl' = the F5 base text", B + cues["nlnl"], fa["prompt_md5_current"], "f5_runs_F5a-2.json / F5b-1.json prompt_md5_current"),
        ("F5a-2 + cue \\n\\n", "blocked with the F5a-2 edit (⑥ output order: reasoning first), + \\n\\n", FA + "\n\n", fa["prompt_md5_new"], "f5_runs_F5a-2.json prompt_md5_new"),
        ("F5b-1 + cue \\n\\n", "blocked with the F5b-1 edit (② tangent-type classification → separation register), + \\n\\n", FB + "\n\n", fb["prompt_md5_new"], "f5_runs_F5b-1.json prompt_md5_new"),
    ]
    out, bad = [], 0
    for name, how, text, want, where in rows:
        got = md5(text)
        ok = "" if want is None else ("✓" if got == want else "✗")
        bad += ok == "✗"
        out.append((name, how, len(text), got, ok, where))
    assert B[len(O):] == arms["closure-forcing"]
    # the open text, line by line, against the public prompts.py read as text (a substring test, nothing run)
    src = pub["prompts_py_text"]
    lines = [(i + 1, ln, (ln in src) if ln.strip() else None) for i, ln in enumerate(O.split("\n"))]
    n_lit = sum(1 for _, _, f in lines if f)
    n_ne = sum(1 for _, _, f in lines if f is not None)
    n_not = [(i, ln) for i, ln, f in lines if f is False]
    md = ["# PROMPT_PROVENANCE — where the question text of the moy-1 figure comes from", "",
          "Generated by `make_prompt_provenance.py` from files inside this bundle. Every md5 is of the UTF-8 text. Nothing of ConstructGap is imported or run: its "
          "literals were read as text (`ast.literal_eval`) into `cards/public_constructgap_v1_0_1_literals.json` when the bundle was cut.", "",
          "| stage | how | chars | md5 | frozen? | where the frozen value is written |", "|---|---|---:|---|:-:|---|"]
    md += [f"| {n} | {h} | {c} | `{m}` | {o} | {w} |" for n, h, c, m, o, w in out]
    md += ["", f"- mismatches: {bad}.",
           f"- public ConstructGap: {pub['repo']} tag `{pub['tag']}`; `probe_registry.py` md5 `{pub['files']['probe_registry.py']['md5']}`, `prompts.py` md5 `{pub['files']['prompts.py']['md5']}`.",
           "- **Can the open text be rebuilt from the public suite without running its code? No.** The open text is `prompts.build('higashida_circle', 'A', 37)`; its coordinate lines "
           "are computed by the suite's geometry code at 37°, and this bundle neither imports nor runs that code. What can be shown without running it: the blocked and "
           "selection-supply appends are the public literals byte for byte (md5 above), and the open text's fixed lines appear verbatim in the public `prompts.py` text "
           f"({n_lit} of {n_ne} non-empty lines; the rest are listed below).",
           "- the frozen open text was written on 2026-07-28 by the house replication run (`replication_config_frozen.json`, md5 of the file `c75122018f12b9031a4354b388be9a6d`).", "",
           "### lines of the open text that are not a literal of the public prompts.py (computed or formatted by code)", "", "```"]
    md += [f"{i:>2}: {ln}" for i, ln in n_not] + ["```", "",
           "## The texts (verbatim)", "", "### open (frozen)", "```", O, "```", "",
           "### closure-forcing append (blocked = open + this)", "```", arms["closure-forcing"], "```", "",
           "### selection-supply append", "```", arms["selection-supply"], "```", "",
           "### F5a-2 edit (one replacement in the blocked text)", "```", f"before: {ea[0]['key']!r}\nafter:  {ea[0]['replacement']!r}", "```", "",
           "### F5b-1 edit (one replacement in the blocked text)", "```", f"before: {eb[0]['key']!r}\nafter:  {eb[0]['replacement']!r}", "```", "",
           "### cues (appended after the text; the figure's pc1 / screen / F5 rows)", "```", "\n".join(f"{k}: {v!r}" for k, v in cues.items()), "```", ""]
    (HERE / "cards" / "PROMPT_PROVENANCE.md").write_text("\n".join(md), encoding="utf-8")
    for r in out:
        print(f"{r[0]:<24} {r[2]:>5} {r[3]} {r[4]}")
    print(f"open text: {n_lit} literal lines of {n_ne}, {len(n_not)} computed / formatted lines · mismatches: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
