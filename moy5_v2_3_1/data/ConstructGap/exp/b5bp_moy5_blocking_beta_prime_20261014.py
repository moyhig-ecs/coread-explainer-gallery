"""Card b5bp (2026-10-14 pm): moy-5 (b) = a blocking request for the reason field, version beta-prime (judgment layer,
noon, §6, verbatim; names no point, no 'mean proportional' / 'square' / 'product' / 'parabola').  Arms:
  Bbp        frozen open prompt of moy-5 + the beta-prime block
  E-full+Bbp essay1 FRAME + the whole essay + the open prompt + the beta-prime block
Sonnet 5.5, Opus 5.5, Fable 5.1 (Fable started after the others), n 20.  Scorer: frozen relation reader v2 (e07c3abd) on
"conjecture || reason" (same as sym5) + the frozen floor and route; FRAME-APPLY v1 (= v1c) on the E-full arm;
coordinate-form parabola columns (descriptive, exp/reread_after_adjudication_noon_20261014.py).
Baselines: essay4 A and E-full (same models, same day).
  python exp/b5bp_moy5_blocking_beta_prime_20261014.py --model M --arms Bbp,E-full+Bbp --part a | --dry | --read"""
import argparse, collections, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pm_cards_common_20261014 as PM
import moy5_relation_reader_v2_20261014 as R2
import frame_apply_v0_20261014 as FA
import reread_after_adjudication_noon_20261014 as RR
X, E, RUN, Q, G = PM.X, PM.E, PM.RUN, PM.X.Q, PM.X.G
CARD = "b5bp"
BETA_PRIME = ("\nIn the reason field, explain WHY the equality you stated holds, by a relation among lengths of segments between the "
              "given points that holds for every position of P_x and is not merely an equality of two lengths. State that relation "
              "explicitly, in the given symbols.")
assert not re.search(r"mean\s*proportional|square|product|parabol", BETA_PRIME, re.I)
OPEN = X.OPEN["moy5"]
CAP = {"claude-sonnet-5-5": 3.0, "claude-opus-5-5": 6.0, "claude-fable-5-1": 16.0}
def prompt_of(arm): return {"Bbp": OPEN + BETA_PRIME, "E-full+Bbp": E.FRAME.format(text=E.ESSAY) + OPEN + BETA_PRIME}[arm]
def call(model, p): return E.one(model, prompt=p)
def score(text):
    conj, reason = RUN.parse_json_field(text, "conjecture"), RUN.parse_json_field(text, "reason")
    whole = Q.M.parse_conj(text); rel = R2.relations(whole)
    eq, par = RR.coord((conj or "") + " " + (reason or ""))
    return {"conjecture": conj, "reason": reason, "closure": bool(G.closure_parabola_section(conj or "")["closure"]), "gate": Q.verdict(text),
            "route": G.route_parabola((conj or "") + " " + (reason or "")), "relations": rel, "kinds": sorted({r["kind"] for r in rel}),
            "bind": any(r["kind"] in ("CUT", "SIM-CUT") for r in rel), "cut_in_conjecture": any(r["kind"] in ("CUT", "SIM-CUT") for r in R2.relations(conj or "")),
            "fa_v1": FA.frame_apply_v1c(conj, reason), "dandelin_word": "dandelin" in whole.lower(), "coord_eq": eq, "coord_param": par}
def read():
    for m in CAP:
        rs = [r for r in PM.CC.load(f"results_{CARD}_{PM.STAMP}_{m}_*.jsonl") if r.get("raw")]
        e4 = {a: [r for r in X.rows_of("moy5", m) if r["arm"] == a and r.get("raw")] for a in ("A", "E-full")}
        print(f"== {PM.CC.SHORT[m]}  usage {PM.CC.usage(CARD, PM.STAMP, m)['est_usd']}  | essay4: A cut {sum(r['bind'] for r in e4['A'])}/{len(e4['A'])} · E-full cut {sum(r['bind'] for r in e4['E-full'])}/{len(e4['E-full'])}")
        for arm in ("Bbp", "E-full+Bbp"):
            s = [r for r in rs if r["arm"] == arm]
            if not s: continue
            print(f"  {arm:10s} n {len(s)} | cut (both fields) {sum(r['bind'] for r in s)} | cut in the answer field {sum(r['cut_in_conjecture'] for r in s)} | floor {sum(r['closure'] for r in s)} | "
                  f"focus-directrix route {sum(r['route'] == 'TRAP-FOCDIR' for r in s)} | coordinate form eq/param {sum(r['coord_eq'] for r in s)}/{sum(r['coord_param'] for r in s)} | FRAME-APPLY v1 {sum(r['fa_v1'] for r in s)} | gate {dict(collections.Counter(r['gate'] for r in s))} | thinking median {PM.CC.med([r.get('reasoning_tokens') for r in s])}")
            for r in s:
                if r["bind"]: print(f"     r{r['rep']}: {[x['src'] for x in r['relations'] if x['kind'] in ('CUT', 'SIM-CUT')]}")
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--model"); ap.add_argument("--arms", default="Bbp,E-full+Bbp"); ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--part", default="a"); ap.add_argument("--dry", action="store_true"); ap.add_argument("--read", action="store_true"); a = ap.parse_args()
    if a.dry:
        for arm in ("Bbp", "E-full+Bbp"): print(arm, "md5", E.md5(prompt_of(arm)), "chars", len(prompt_of(arm)))
        print("beta-prime md5", E.md5(BETA_PRIME))
    elif a.read: read()
    else: PM.run_units(CARD, a.model, a.arms.split(","), a.n, a.part, prompt_of, call, score, CAP[a.model])
