import {
  buildContribution,
  byId,
  labelOf,
  matchCapability,
  metrics,
  publishedEntities,
  relationsFrom,
  searchEntities
} from "./logic.js";

const NAV = [
  ["index.html", "Accueil", "home"],
  ["directory.html", "Annuaire", "directory"],
  ["map.html", "Carte", "map"],
  ["match.html", "Correspondance", "match"],
  ["contribute.html", "Contribuer", "contribute"],
  ["book.html", "Livre", "book"],
  ["privacy.html", "Confidentialité", "privacy"]
];

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function currentPage() {
  return document.body.dataset.page || "";
}

function markNav() {
  const page = currentPage();
  for (const link of document.querySelectorAll("nav a")) {
    const item = NAV.find((entry) => entry[0] === link.getAttribute("href"));
    if (item && item[2] === page) link.setAttribute("aria-current", "page");
  }
}

async function loadSeed() {
  const response = await fetch("../data/seed.json");
  if (!response.ok) throw new Error(`seed HTTP ${response.status}`);
  return response.json();
}

function entityHref(id) {
  return `entity.html?id=${encodeURIComponent(id)}`;
}

function renderMetrics(seed, node) {
  const counts = metrics(seed);
  const items = [
    [counts.organizations, "organisations"],
    [counts.people, "personnes"],
    [counts.projects, "projets"],
    [counts.countries, "pays de présence"],
    [counts.corsican_communes, "communes corses sourcées"],
    [counts.skills, "compétences"],
    [counts.offers, "offres"],
    [counts.needs, "besoins"],
    [counts.relations, "relations"],
    [counts.contributions_awaiting_review, "contributions en attente dans le jeu"],
    [counts.open_to_help_true, "offres explicitement ouvertes à l'aide"]
  ];
  node.innerHTML = items
    .map(([value, name]) => `<li><strong>${value}</strong>${escapeHtml(name)}</li>`)
    .join("");
  const note = document.querySelector("[data-metric-note]");
  if (note) {
    note.textContent = `Communes : ${counts.commune_names.join(", ") || "aucune"}. Pays : ${counts.country_names.join(", ") || "aucun"}. ${counts.sourced_records} fiches publiées portent une source.`;
  }
}

function card(seed, entity) {
  const map = byId(seed);
  const skills = relationsFrom(seed, entity.id, "HAS_SKILL").map((relation) => labelOf(map.get(relation.to)));
  const offers = relationsFrom(seed, entity.id, "OFFERS").map((relation) => labelOf(map.get(relation.to)));
  const needs = relationsFrom(seed, entity.id, "NEEDS").map((relation) => labelOf(map.get(relation.to)));
  const location = entity.location || {};
  const where = [location.city, location.region, location.country].filter(Boolean).join(", ");
  return `<article class="result">
    <h2><a href="${entityHref(entity.id)}">${escapeHtml(labelOf(entity))}</a></h2>
    <p class="muted">${escapeHtml(entity.type)} · ${escapeHtml(entity.verification_status || "")}</p>
    <p>${escapeHtml(entity.summary || "")}</p>
    <p>${where ? escapeHtml(`${location.kind || "lieu"} : ${where}`) : ""}</p>
    ${location.activity_area ? `<p>Zone d'activité déclarée : ${escapeHtml(location.activity_area)}</p>` : ""}
    ${skills.length ? `<p>Compétences : ${skills.map(escapeHtml).join(", ")}</p>` : ""}
    ${offers.length ? `<p>Offres : ${offers.map(escapeHtml).join(", ")}</p>` : ""}
    ${needs.length ? `<p>Besoins portés : ${needs.map(escapeHtml).join(", ")}</p>` : ""}
  </article>`;
}

function initDirectory(seed) {
  const form = document.querySelector("#search-form");
  const output = document.querySelector("#results");
  const run = () => {
    const data = new FormData(form);
    const found = searchEntities(seed, {
      q: data.get("q"),
      type: data.get("type"),
      region: data.get("region"),
      corsican: data.get("corsican"),
      language: data.get("language")
    }).filter((entity) => ["person", "organization", "project"].includes(entity.type));
    output.innerHTML = found.length
      ? `<p>${found.length} fiche${found.length > 1 ? "s" : ""}.</p>${found.map((entity) => card(seed, entity)).join("")}`
      : `<p class="notice">Aucune fiche publiée ne correspond. Le filtre de région utilise le lieu de présence, pas le lien corse.</p>`;
  };
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    run();
  });
  const params = new URLSearchParams(location.search);
  for (const key of ["q", "type", "region", "corsican", "language"]) {
    if (params.get(key) && form.elements[key]) form.elements[key].value = params.get(key);
  }
  run();
}

function initEntity(seed) {
  const output = document.querySelector("#entity");
  const id = new URLSearchParams(location.search).get("id");
  const entity = byId(seed).get(id);
  if (!entity || entity.visibility !== "public" || entity.publication_status !== "published") {
    output.innerHTML = `<p class="notice">Fiche introuvable dans le jeu publié.</p>`;
    return;
  }
  document.title = `${labelOf(entity)} — DIASPORA`;
  const map = byId(seed);
  const relations = (seed.relations || [])
    .filter((relation) => relation.from === entity.id || relation.to === entity.id)
    .map((relation) => {
      const outbound = relation.from === entity.id;
      const other = map.get(outbound ? relation.to : relation.from);
      const direction = outbound ? "→" : "←";
      return `<li>${escapeHtml(relation.type)} ${direction} <a href="${entityHref(other.id)}">${escapeHtml(labelOf(other))}</a>${relation.location_kind ? ` <span class="tag">${escapeHtml(relation.location_kind)}</span>` : ""}</li>`;
    })
    .join("");
  const sources = (entity.provenance.sources || [])
    .map((sourceId) => {
      const source = map.get(sourceId);
      const href = source && source.url ? source.url : entityHref(sourceId);
      return `<li><a href="${escapeHtml(href)}">${escapeHtml(source ? labelOf(source) : sourceId)}</a></li>`;
    })
    .join("");
  const location = entity.location || {};
  const contact = entity.contact || {};
  output.innerHTML = `
    <p class="muted">${escapeHtml(entity.type)} · vérification : ${escapeHtml(entity.verification_status)}</p>
    <h1>${escapeHtml(labelOf(entity))}</h1>
    <p>${escapeHtml(entity.summary || entity.name)}</p>
    ${location.kind ? `<p>Lieu (${escapeHtml(location.kind)}) : ${escapeHtml([location.city, location.region, location.country].filter(Boolean).join(", "))}</p>` : ""}
    ${location.coordinate_note ? `<p class="muted">${escapeHtml(location.coordinate_note)}</p>` : ""}
    ${location.activity_area ? `<p>Zone d'activité déclarée, distincte du lieu : ${escapeHtml(location.activity_area)}</p>` : ""}
    ${(entity.corsican_links || []).map((link) => `<p>Lien corse : ${escapeHtml(link.commune || "sans commune")} · ${escapeHtml(link.role || "")}. ${escapeHtml(link.note || "")}</p>`).join("")}
    <p>Ouvert à l'aide : <strong>${escapeHtml(entity.open_to_help || "non porté par cette fiche")}</strong></p>
    ${contact.public_url ? `<p><a href="${escapeHtml(contact.public_url)}">Lien public</a></p>` : ""}
    ${contact.public_email ? `<p>Email public : ${escapeHtml(contact.public_email)}</p>` : ""}
    ${contact.public_postal_address ? `<p>Adresse publique : ${escapeHtml(contact.public_postal_address)} ${escapeHtml(contact.postal_address_note || "")}</p>` : ""}
    ${entity.registry ? `<h2>Répertoire</h2><p>SIREN ${escapeHtml(entity.registry.siren)} · RNA ${escapeHtml(entity.registry.rna)} · création ${escapeHtml(entity.registry.date_creation)} · état ${escapeHtml(entity.registry.etat_administratif)}.</p><p>Siège légal publié : ${escapeHtml(entity.registry.legal_seat_address)}.</p>` : ""}
    <h2>Relations</h2>
    <ul>${relations || "<li>Aucune.</li>"}</ul>
    <h2>Sources</h2>
    <ul>${sources}</ul>
    <p class="muted">Observé le ${escapeHtml(entity.provenance.observed_at)}. ${escapeHtml(entity.provenance.notes || "")}</p>
  `;
}

function initMatch(seed) {
  const form = document.querySelector("#match-form");
  const select = form.elements.needId;
  const needs = publishedEntities(seed).filter((entity) => entity.type === "need");
  select.innerHTML = `<option value="">Aucun besoin précis</option>` + needs
    .map((need) => `<option value="${escapeHtml(need.id)}">${escapeHtml(labelOf(need))}</option>`)
    .join("");
  const output = document.querySelector("#match-results");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const result = matchCapability(seed, {
      region: data.get("region"),
      capability: data.get("capability"),
      needId: data.get("needId"),
      requireOpenToHelp: data.get("requireOpenToHelp") === "on"
    });
    const blocks = result.matches
      .map((match) => `<article class="result"><h2><a href="${entityHref(match.id)}">${escapeHtml(match.name)}</a></h2><p>open_to_help : ${escapeHtml(match.open_to_help)}</p><ul>${match.rationale.map((line) => `<li>${escapeHtml(line)}</li>`).join("")}</ul></article>`)
      .join("");
    output.innerHTML = `${result.empty_reason ? `<p class="notice">${escapeHtml(result.empty_reason)}</p>` : ""}<p class="muted">${result.excluded.length} fiches écartées, avec motif.</p>${blocks}`;
  });
}

function initContribute() {
  const form = document.querySelector("#contribute-form");
  const output = document.querySelector("#packet");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const built = buildContribution({
      authorized: data.get("authorized") === "on",
      declaration: data.get("declaration"),
      type: data.get("type"),
      name: data.get("name"),
      city: data.get("city"),
      region: data.get("region"),
      country: data.get("country"),
      commune: data.get("commune"),
      languages: data.get("languages"),
      skills: data.get("skills"),
      offers: data.get("offers"),
      needs: data.get("needs"),
      public_url: data.get("public_url"),
      public_email: data.get("public_email"),
      notes: data.get("notes")
    }, new Date().toISOString());
    if (!built.ok) {
      output.textContent = built.error;
      return;
    }
    output.textContent = JSON.stringify(built.packet, null, 2);
  });
  document.querySelector("#copy-packet").addEventListener("click", async () => {
    const text = output.textContent || "";
    if (!text.trim()) return;
    try {
      await navigator.clipboard.writeText(text);
      output.insertAdjacentHTML("afterend", "<p class=\"ok\" id=\"copied\">Copié dans le presse-papiers. Rien n'a été envoyé.</p>");
    } catch {
      output.insertAdjacentHTML("afterend", "<p class=\"warn\">Copie indisponible. Sélectionnez le texte. Rien n'a été envoyé.</p>");
    }
  });
}

function mapPoints(seed) {
  const points = [];
  for (const entity of publishedEntities(seed)) {
    const location = entity.location;
    if (!location || typeof location.lat !== "number" || typeof location.lon !== "number") continue;
    if (!["organization", "project", "place"].includes(entity.type)) continue;
    points.push({
      id: entity.id,
      name: labelOf(entity),
      kind: location.kind || "current_location",
      lat: location.lat,
      lon: location.lon,
      precision: location.coordinate_precision || ""
    });
  }
  return points;
}

async function initMap(seed) {
  const list = document.querySelector("#map-list");
  const kinds = new Set(["organization_location", "project_location", "corsican_origin_or_link"]);
  const drawList = () => {
    const points = mapPoints(seed).filter((point) => kinds.has(point.kind));
    list.innerHTML = points
      .map((point) => `<li><a href="${entityHref(point.id)}">${escapeHtml(point.name)}</a> <span class="tag">${escapeHtml(point.kind)}</span> <span class="muted">${escapeHtml(point.precision)}</span></li>`)
      .join("") || "<li>Aucun point pour ces couches.</li>";
    return points;
  };
  drawList();
  for (const box of document.querySelectorAll("[data-kind]")) {
    box.addEventListener("change", () => {
      if (box.checked) kinds.add(box.dataset.kind);
      else kinds.delete(box.dataset.kind);
      drawList();
      if (window.__diasporaRedraw) window.__diasporaRedraw();
    });
  }
  const host = document.querySelector("#map");
  try {
    await new Promise((resolve, reject) => {
      const css = document.createElement("link");
      css.rel = "stylesheet";
      css.href = "https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css";
      document.head.appendChild(css);
      const script = document.createElement("script");
      script.src = "https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js";
      script.onload = resolve;
      script.onerror = () => reject(new Error("leaflet"));
      document.head.appendChild(script);
    });
    const map = window.L.map(host).setView([42.5, 9], 5);
    window.L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 18,
      attribution: "&copy; OpenStreetMap"
    }).addTo(map);
    let layer = window.L.layerGroup().addTo(map);
    window.__diasporaRedraw = () => {
      layer.clearLayers();
      for (const point of mapPoints(seed).filter((item) => kinds.has(item.kind))) {
        window.L.marker([point.lat, point.lon]).addTo(layer).bindPopup(
          `<a href="${entityHref(point.id)}">${escapeHtml(point.name)}</a><br>${escapeHtml(point.kind)}`
        );
      }
    };
    window.__diasporaRedraw();
  } catch {
    host.innerHTML = "<p class=\"notice\">Le fond de carte n'a pas pu être chargé. La liste reste utilisable.</p>";
  }
}

async function main() {
  markNav();
  const page = currentPage();
  if (page === "contribute") {
    initContribute();
    return;
  }
  if (page === "book" || page === "privacy") return;
  const slot = document.querySelector("[data-seed-status]");
  try {
    const seed = await loadSeed();
    if (slot) slot.textContent = "Jeu chargé depuis data/seed.json.";
    if (page === "home") renderMetrics(seed, document.querySelector("#metrics"));
    if (page === "directory") initDirectory(seed);
    if (page === "entity") initEntity(seed);
    if (page === "match") initMatch(seed);
    if (page === "map") initMap(seed);
  } catch (error) {
    if (slot) slot.textContent = "Le jeu n'a pas pu être lu. Ouvrez ces pages via scripts/serve.js, pas en fichier local.";
    console.error(error);
  }
}

main();
