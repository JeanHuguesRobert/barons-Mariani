import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import {
  buildContribution,
  matchCapability,
  metrics,
  searchEntities,
  validateSeed
} from "../web/logic.js";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const seed = JSON.parse(readFileSync(join(root, "data", "seed.json"), "utf8"));
const failures = [];

function check(name, condition) {
  if (!condition) failures.push(name);
  else console.log(`ok ${name}`);
}

const validation = validateSeed(seed);
check("seed invariants", validation.ok);
if (!validation.ok) console.error(validation.errors.join("\n"));

const counts = metrics(seed);
console.log(JSON.stringify(counts));
check("no people", counts.people === 0);
check("four organizations", counts.organizations === 4);
check("two projects", counts.projects === 2);
check("one country of presence", counts.countries === 1 && counts.country_names[0] === "France");
check("two corsican communes", counts.corsican_communes === 2);

const bastia = searchEntities(seed, { q: "Bastia", type: "organization" }).map((entity) => entity.id);
check("search Bastia finds Corsica Diaspora", bastia.includes("org-corsica-diaspora"));

const bordeaux = searchEntities(seed, { q: "Bordeaux" }).map((entity) => entity.id);
check("search Bordeaux finds the Eysines association", bordeaux.includes("org-amicale-corsica"));
check("search Bordeaux does not treat Bastia as Bordeaux", !bordeaux.includes("org-corsica-diaspora"));

const gironde = searchEntities(seed, { region: "Gironde", type: "organization" }).map((entity) => entity.id);
check("presence filter Gironde is the amicale", gironde.length === 1 && gironde[0] === "org-amicale-corsica");

const corsePresence = searchEntities(seed, { region: "Haute-Corse", type: "organization" }).map((entity) => entity.id);
check("presence filter Haute-Corse excludes Eysines", corsePresence.includes("org-corsica-diaspora") && !corsePresence.includes("org-amicale-corsica"));

const link = searchEntities(seed, { corsican: "Bastia", type: "organization" }).map((entity) => entity.id);
check("corsican-link filter Bastia", link.includes("org-corsica-diaspora") && !link.includes("org-amicale-corsica"));

const openMatch = matchCapability(seed, {
  region: "Corte",
  capability: "correction",
  needId: "need-sourced-public-records",
  requireOpenToHelp: true
});
check(
  "open match is only DIASPORA",
  openMatch.matches.length === 1 && openMatch.matches[0].id === "project-diaspora"
);

const stated = matchCapability(seed, {
  region: "Bastia",
  capability: "animation",
  requireOpenToHelp: false
});
check(
  "stated Bastia animation stays unknown",
  stated.matches.some((match) => match.id === "org-corsica-diaspora" && match.open_to_help === "unknown")
);

const strictStated = matchCapability(seed, {
  region: "Bastia",
  capability: "animation",
  requireOpenToHelp: true
});
check(
  "unknown open_to_help is excluded when help is required",
  strictStated.matches.every((match) => match.id !== "org-corsica-diaspora")
);

const holder = matchCapability(seed, { needId: "need-cd-digital-tools", requireOpenToHelp: false });
check(
  "need holder is not a helper",
  holder.matches.every((match) => match.id !== "org-corsica-diaspora" && match.id !== "project-cd-five-year")
);

const gathering = matchCapability(seed, {
  region: "Eysines",
  capability: "retrouver",
  requireOpenToHelp: false
});
check(
  "Eysines gathering matches the amicale without a help commitment",
  gathering.matches.some((match) => match.id === "org-amicale-corsica" && match.open_to_help === "unknown")
);

const refused = buildContribution({ authorized: false, name: "Test" }, "2026-09-30T00:00:00+02:00");
check("contribution requires declaration", refused.ok === false);

const packet = buildContribution({
  authorized: true,
  declaration: "public",
  type: "organization",
  name: "Exemple",
  city: "Marseille"
}, "2026-09-30T00:00:00+02:00");
check(
  "contribution is not publication",
  packet.ok === true &&
    packet.packet.status === "submission" &&
    packet.packet.publication_status === "not-published" &&
    packet.packet.validation_status === "not-validated"
);

const pages = readdirSync(join(root, "web")).filter((name) => name.endsWith(".html"));
check("eight public pages", pages.length === 8);
for (const name of pages) {
  const html = readFileSync(join(root, "web", name), "utf8");
  check(`${name} is french`, html.includes("lang=\"fr\""));
  check(`${name} loads the app`, html.includes("app.js"));
  check(`${name} has no phone field`, !html.includes("name=\"phone\"") && !html.includes("type=\"tel\""));
}
const appSource = readFileSync(join(root, "web", "app.js"), "utf8");
const fetches = appSource.match(/fetch\([^)]+\)/g) || [];
check("app reads only the canonical seed", fetches.length === 1 && fetches[0].includes("../data/seed.json"));

if (failures.length) {
  console.error(`FAILED ${failures.length}\n${failures.join("\n")}`);
  process.exit(1);
}
console.log("validate-seed: all checks passed");
