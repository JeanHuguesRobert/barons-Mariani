#!/usr/bin/env node
/**
 * Project a single audited browser client into each Living Book static site.
 * Static projections are byte-identical; the body's data-guide-* attributes
 * carry each book's identity, source scope and optional exploration grammar.
 * Never publish or deploy: --write updates local projections only.
 */
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const source = path.join(root, "scripts/lib/living-book-guide/client.js");
const targets = ["capable", "privai"].map(id =>
  path.join(root, "projects", id, "site", "guide.js"));
const args = process.argv.slice(2);
if (args.some(x => !["--check","--write"].includes(x)) ||
    (args.includes("--check") && args.includes("--write"))) {
  throw new Error("Usage: node scripts/ops/sync-living-book-guides.mjs [--check|--write]");
}
const write = args.includes("--write");
const expected = fs.readFileSync(source, "utf8");
assert(expected.includes("GUIDE_PROFILE") && expected.includes("postGuideStream"),
  "Canonical Guide client missing profile scoping or SSE");
let changed = 0;
for (const file of targets) {
  const current = fs.existsSync(file) ? fs.readFileSync(file,"utf8") : null;
  if (current === expected) continue;
  if (write) {
    fs.writeFileSync(file, expected);
    changed++;
  } else {
    throw Error(path.relative(root,file) +
      " diverges from scripts/lib/living-book-guide/client.js; run --write to regenerate");
  }
}
console.log(JSON.stringify({ok:true,mode:write?"write":"check",
  canonical:path.relative(root,source),
  projected:targets.map(x=>path.relative(root,x)),changed},null,2));
