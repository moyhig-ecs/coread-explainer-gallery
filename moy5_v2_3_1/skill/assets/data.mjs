// data.mjs — the SECOND route (template): the page's build counts the same numbers again, in JS, straight from the card's JSON, and compares them with the pack that pack_data.py wrote.
// A disagreement stops the build (expect throws). Exports DATA = what the page carries (nothing typed by hand).
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const raw = JSON.parse(readFileSync(join(HERE, "data", "synthetic_readout.json"), "utf8"));
const pack = JSON.parse(readFileSync(join(HERE, "generated", "pack.json"), "utf8"));
export const CONFIG = JSON.parse(readFileSync(join(HERE, "config.json"), "utf8"));
const expect = (cond, what) => { if (!cond) throw new Error(`data.mjs: the pack disagrees with the card's JSON / with itself: ${what}`); };

const [lo, hi] = raw.constants.band, CL = raw.constants.clip;
const median = (a) => { const s = [...a].sort((x, y) => x - y), n = s.length; return n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2; };
expect(pack.stage === raw.stage && pack.forward === 0 && pack.provenance.dirty === false && Object.values(pack.controls).every((c) => c.pass), "stage, forward 0, not dirty, controls pass");
for (const [key, r] of Object.entries(raw.rows)) {
  const mine = pack.rows[key];
  const bm = r.ranks.map((col) => median(col.slice(lo, hi + 1).map((v) => Math.min(v, CL + 1))));
  expect(JSON.stringify(bm) === JSON.stringify(mine.bandMedian), `${key}: the band medians recounted in JS equal the pack's`);
  expect(mine.keyPos === r.key_pos && bm[r.key_pos] === mine.keyRank, `${key}: the rank at the key position (${r.key_pos}) is ${mine.keyRank}`);
}
export const DATA = { config: CONFIG, ...pack };
