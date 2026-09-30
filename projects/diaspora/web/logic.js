/**
 * DIASPORA directory logic. Shared by the static pages and the node checks.
 * Matching is deterministic: a need-holder is not treated as someone who can help.
 */

export const ACTOR_TYPES = ["person", "organization", "project"];
export const LOCATION_KINDS = [
  "current_location",
  "corsican_origin_or_link",
  "organization_location",
  "project_location"
];
export const PRESENCE_KINDS = [
  "current_location",
  "organization_location",
  "project_location"
];
export const RELATION_TYPES = [
  "HAS_SKILL",
  "OFFERS",
  "NEEDS",
  "MEMBER_OF",
  "CONNECTED_TO",
  "RUNS",
  "CAN_ADDRESS",
  "LOCATED_AT"
];

const FORBIDDEN_KEYS = new Set([
  "phone",
  "telephone",
  "mobile",
  "iban",
  "home_address",
  "personal_email",
  "password"
]);

const ALLOWED_PUBLIC_EMAILS = new Set(["contact@corsica-diaspora.com"]);

export function byId(seed) {
  const map = new Map();
  for (const entity of seed.entities || []) map.set(entity.id, entity);
  return map;
}

export function labelOf(entity) {
  if (!entity) return "";
  return entity.display_name || entity.name || entity.id;
}

export function publishedEntities(seed) {
  return (seed.entities || []).filter(
    (entity) => entity.visibility === "public" && entity.publication_status === "published"
  );
}

export function relationsFrom(seed, id, type) {
  return (seed.relations || []).filter((relation) => {
    if (relation.from !== id) return false;
    if (type && relation.type !== type) return false;
    return true;
  });
}

export function fold(value) {
  return String(value || "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/\p{M}/gu, "");
}

export function tokens(value) {
  return fold(value)
    .split(/[^a-z0-9]+/u)
    .filter((token) => token.length >= 3);
}

function relatedLabels(seed, entity) {
  const map = byId(seed);
  const parts = [];
  for (const relation of seed.relations || []) {
    if (relation.from !== entity.id && relation.to !== entity.id) continue;
    const otherId = relation.from === entity.id ? relation.to : relation.from;
    const other = map.get(otherId);
    if (other) parts.push(labelOf(other), other.name || "");
    if (relation.location_kind) parts.push(relation.location_kind);
    if (relation.qualifier) parts.push(relation.qualifier);
  }
  return parts;
}

export function haystack(seed, entity) {
  const location = entity.location || {};
  const links = entity.corsican_links || [];
  const parts = [
    entity.name,
    entity.display_name,
    entity.summary,
    entity.type,
    entity.verification_status,
    entity.statement_status,
    entity.open_to_help,
    location.city,
    location.region,
    location.country,
    location.activity_area,
    location.kind,
    ...(entity.languages || []),
    ...links.flatMap((link) => [link.commune, link.village, link.role, link.note, link.kind]),
    ...relatedLabels(seed, entity)
  ];
  return fold(parts.filter(Boolean).join(" "));
}

function containsText(hay, query) {
  const wanted = tokens(query);
  if (wanted.length === 0) return String(query || "").trim().length === 0;
  return wanted.every((token) => hay.includes(token));
}

export function searchEntities(seed, filters = {}) {
  const query = filters.q || "";
  return publishedEntities(seed).filter((entity) => {
    if (filters.type && entity.type !== filters.type) return false;
    if (filters.verification && entity.verification_status !== filters.verification) return false;
    const hay = haystack(seed, entity);
    if (query && !containsText(hay, query)) return false;
    if (filters.country && !containsText(hay, filters.country)) return false;
    if (filters.region && !presenceMatches(seed, entity, filters.region)) return false;
    if (filters.corsican && !corsicanMatches(seed, entity, filters.corsican)) return false;
    if (filters.language) {
      const languages = (entity.languages || []).map(fold);
      if (!languages.includes(fold(filters.language))) return false;
    }
    return true;
  });
}

function presenceBlob(seed, entity) {
  const map = byId(seed);
  const parts = [];
  const location = entity.location || {};
  if (!location.kind || PRESENCE_KINDS.includes(location.kind)) {
    parts.push(location.city, location.region, location.country, location.activity_area);
  }
  for (const relation of relationsFrom(seed, entity.id, "LOCATED_AT")) {
    if (relation.location_kind && !PRESENCE_KINDS.includes(relation.location_kind)) continue;
    const place = map.get(relation.to);
    if (place) parts.push(place.name, place.location && place.location.city, place.location && place.location.region);
  }
  return fold(parts.filter(Boolean).join(" "));
}

function corsicanBlob(seed, entity) {
  const map = byId(seed);
  const parts = [];
  for (const link of entity.corsican_links || []) {
    parts.push(link.commune, link.village, link.role);
  }
  for (const relation of relationsFrom(seed, entity.id, "CONNECTED_TO")) {
    if (relation.location_kind !== "corsican_origin_or_link") continue;
    const place = map.get(relation.to);
    if (place) parts.push(place.name, place.location && place.location.region);
  }
  return fold(parts.filter(Boolean).join(" "));
}

export function presenceMatches(seed, entity, text) {
  if (!String(text || "").trim()) return true;
  return containsText(presenceBlob(seed, entity), text);
}

export function corsicanMatches(seed, entity, text) {
  if (!String(text || "").trim()) return true;
  return containsText(corsicanBlob(seed, entity), text);
}

function capabilityHits(seed, entity, text) {
  const map = byId(seed);
  const hits = [];
  const kinds = [
    ["HAS_SKILL", "skill"],
    ["OFFERS", "offer"]
  ];
  for (const [type, word] of kinds) {
    for (const relation of relationsFrom(seed, entity.id, type)) {
      const target = map.get(relation.to);
      if (!target) continue;
      const blob = fold(`${target.name} ${target.summary || ""} ${target.statement_status || ""}`);
      if (containsText(blob, text)) {
        hits.push({
          relation_id: relation.id,
          via: target.id,
          text: `${word} ${labelOf(target)} (${target.statement_status || target.verification_status})`
        });
      }
    }
  }
  return hits;
}

function addressingOffers(seed, entity, need) {
  const map = byId(seed);
  const offers = relationsFrom(seed, entity.id, "OFFERS")
    .map((relation) => ({ relation, offer: map.get(relation.to) }))
    .filter((item) => item.offer);
  const hits = [];
  for (const item of offers) {
    const address = (seed.relations || []).find(
      (relation) =>
        relation.type === "CAN_ADDRESS" &&
        relation.from === item.offer.id &&
        relation.to === need.id
    );
    if (address) {
      hits.push({
        relation_id: address.id,
        offer: item.offer,
        text: `offer ${labelOf(item.offer)} CAN_ADDRESS ${labelOf(need)} (${address.id})`
      });
      continue;
    }
    const blob = fold(`${item.offer.name} ${item.offer.summary || ""}`);
    const needBlob = tokens(need.name);
    if (needBlob.length && needBlob.every((token) => blob.includes(token))) {
      hits.push({
        relation_id: item.relation.id,
        offer: item.offer,
        text: `offer text overlaps the need name: ${labelOf(item.offer)}`
      });
    }
  }
  return hits;
}

export function matchCapability(seed, query = {}) {
  const region = String(query.region || "").trim();
  const capability = String(query.capability || "").trim();
  const needId = String(query.needId || "").trim();
  const requireOpen = query.requireOpenToHelp === true;
  const map = byId(seed);
  const matches = [];
  const excluded = [];

  if (!region && !capability && !needId) {
    return {
      matches: [],
      excluded: [],
      empty_reason: "Indiquez une région, une capacité, ou un besoin."
    };
  }

  const need = needId ? map.get(needId) : null;
  if (needId && (!need || need.type !== "need")) {
    return {
      matches: [],
      excluded: [],
      empty_reason: "Ce besoin n'est pas dans le jeu publié."
    };
  }

  for (const entity of publishedEntities(seed)) {
    if (!ACTOR_TYPES.includes(entity.type)) continue;
    const rationale = [];
    const blocks = [];

    if (region) {
      if (presenceMatches(seed, entity, region)) {
        const kind = (entity.location && entity.location.kind) || "presence";
        rationale.push(`région « ${region} » correspond à ${kind}, pas au lien corse`);
      } else {
        blocks.push("la région demandée ne correspond pas au lieu de présence");
      }
    }

    let capabilityOffers = [];
    if (capability) {
      const hits = capabilityHits(seed, entity, capability);
      if (hits.length === 0) blocks.push("aucune compétence ni offre publiée ne correspond");
      else {
        rationale.push(...hits.map((hit) => hit.text));
        capabilityOffers = hits
          .filter((hit) => hit.via && map.get(hit.via) && map.get(hit.via).type === "offer")
          .map((hit) => map.get(hit.via));
      }
    }

    let needOffers = [];
    if (need) {
      const hits = addressingOffers(seed, entity, need);
      if (hits.length === 0) {
        const holds = relationsFrom(seed, entity.id, "NEEDS").some((relation) => relation.to === need.id);
        blocks.push(
          holds
            ? "cette fiche porte le besoin ; elle n'est pas comptée comme répondante"
            : "aucune offre inspectable ne répond à ce besoin"
        );
      } else {
        rationale.push(...hits.map((hit) => hit.text));
        needOffers = hits.map((hit) => hit.offer);
      }
    }

    const relevantOffers = [...capabilityOffers, ...needOffers];
    const openValues = relevantOffers.map((offer) => offer.open_to_help || "unknown");
    if (openValues.length === 0 && entity.open_to_help) openValues.push(entity.open_to_help);
    const open = openValues.includes("true") ? "true" : openValues.includes("false") ? "false" : "unknown";

    if (requireOpen && open !== "true") {
      blocks.push(`open_to_help vaut « ${open} », pas « true »`);
    } else if (open === "true") {
      rationale.push("open_to_help est true sur l'offre qui répond");
    } else if (blocks.length === 0) {
      rationale.push(`open_to_help vaut « ${open} » : ce n'est pas un engagement d'aide`);
    }

    if (blocks.length) excluded.push({ id: entity.id, name: labelOf(entity), blocks });
    else matches.push({ id: entity.id, name: labelOf(entity), type: entity.type, open_to_help: open, rationale });
  }

  return {
    matches,
    excluded,
    empty_reason: matches.length
      ? ""
      : "Aucune fiche publiée ne réunit les critères. Les objectifs déclarés sans engagement d'aide restent visibles dans l'annuaire, pas dans ce filtre."
  };
}

export function metrics(seed) {
  const entities = publishedEntities(seed);
  const ofType = (type) => entities.filter((entity) => entity.type === type);
  const people = ofType("person");
  const organizations = ofType("organization");
  const projects = ofType("project");
  const places = ofType("place");
  const countries = new Set();
  for (const entity of [...people, ...organizations, ...projects]) {
    const country = entity.location && entity.location.country;
    const kind = entity.location && entity.location.kind;
    if (country && (!kind || PRESENCE_KINDS.includes(kind))) countries.add(country);
  }
  const communes = new Set();
  for (const entity of entities) {
    for (const link of entity.corsican_links || []) {
      if (link.commune) communes.add(link.commune);
    }
  }
  const sourced = entities.filter((entity) => entity.provenance && entity.provenance.sources && entity.provenance.sources.length);
  return {
    entities: entities.length,
    people: people.length,
    organizations: organizations.length,
    projects: projects.length,
    places: places.length,
    countries: countries.size,
    country_names: [...countries].sort(),
    corsican_communes: communes.size,
    commune_names: [...communes].sort(),
    skills: ofType("skill").length,
    offers: ofType("offer").length,
    needs: ofType("need").length,
    sources: ofType("source").length,
    relations: (seed.relations || []).length,
    sourced_records: sourced.length,
    contributions_awaiting_review: entities.filter((entity) => entity.publication_status === "submitted").length,
    open_to_help_true: entities.filter((entity) => entity.open_to_help === "true").length
  };
}

function walk(value, visit) {
  if (Array.isArray(value)) {
    value.forEach((item) => walk(item, visit));
    return;
  }
  if (!value || typeof value !== "object") {
    visit(null, value);
    return;
  }
  for (const [key, child] of Object.entries(value)) {
    visit(key, child);
    walk(child, visit);
  }
}

export function validateSeed(seed) {
  const errors = [];
  const map = byId(seed);
  if (seed.schema !== "diaspora.seed.v0") errors.push("schema must be diaspora.seed.v0");
  if (!Array.isArray(seed.entities) || seed.entities.length === 0) errors.push("entities missing");
  if (!Array.isArray(seed.relations)) errors.push("relations missing");

  const seen = new Set();
  for (const entity of seed.entities || []) {
    if (!entity.id || seen.has(entity.id)) errors.push(`bad or duplicate id ${entity.id}`);
    seen.add(entity.id);
    for (const key of ["type", "name", "visibility", "publication_status", "verification_status", "updated_at"]) {
      if (!entity[key]) errors.push(`${entity.id} missing ${key}`);
    }
    if (!entity.provenance || !Array.isArray(entity.provenance.sources) || entity.provenance.sources.length === 0) {
      errors.push(`${entity.id} missing provenance.sources`);
    }
    if (!entity.provenance || !entity.provenance.observed_at) errors.push(`${entity.id} missing observed_at`);
    if (entity.visibility === "public" && entity.publication_status === "published") {
      for (const sourceId of (entity.provenance && entity.provenance.sources) || []) {
        const source = map.get(sourceId);
        if (!source || source.type !== "source") errors.push(`${entity.id} cites missing source ${sourceId}`);
      }
    }
    if (entity.type === "person") {
      const links = entity.corsican_links || [];
      const declared = links.some((link) => link.declared_by && (link.commune || link.village || link.place_id));
      if (!declared) errors.push(`${entity.id} person lacks a sourced Corsican link`);
    }
    if (entity.contact && entity.contact.public_email && !ALLOWED_PUBLIC_EMAILS.has(entity.contact.public_email)) {
      errors.push(`${entity.id} public_email is not on the allowlist`);
    }
    for (const link of entity.corsican_links || []) {
      if (link.village) errors.push(`${entity.id} has a village; this seed must not invent one`);
      if (link.kind !== "corsican_origin_or_link") errors.push(`${entity.id} corsican link kind collapsed`);
    }
  }

  for (const relation of seed.relations || []) {
    if (!RELATION_TYPES.includes(relation.type)) errors.push(`${relation.id} bad type ${relation.type}`);
    if (!map.has(relation.from) || !map.has(relation.to)) errors.push(`${relation.id} dangling endpoint`);
    if (!relation.provenance || !relation.provenance.sources) errors.push(`${relation.id} missing provenance`);
    const from = map.get(relation.from);
    const to = map.get(relation.to);
    if (!from || !to) continue;
    if (relation.type === "LOCATED_AT" && !LOCATION_KINDS.includes(relation.location_kind)) {
      errors.push(`${relation.id} missing location_kind`);
    }
    if (relation.type === "CONNECTED_TO" && relation.location_kind !== "corsican_origin_or_link") {
      errors.push(`${relation.id} CONNECTED_TO must keep the Corsican-link kind`);
    }
    if (relation.type === "CAN_ADDRESS" && (from.type !== "offer" || to.type !== "need")) {
      errors.push(`${relation.id} CAN_ADDRESS must run from offer to need`);
    }
    if (relation.type === "NEEDS" && to.type !== "need") errors.push(`${relation.id} NEEDS target`);
    if (relation.type === "OFFERS" && to.type !== "offer") errors.push(`${relation.id} OFFERS target`);
    if (relation.type === "HAS_SKILL" && to.type !== "skill") errors.push(`${relation.id} HAS_SKILL target`);
    if (relation.type === "RUNS" && (from.type !== "organization" || to.type !== "project")) {
      errors.push(`${relation.id} RUNS shape`);
    }
    if ((relation.type === "LOCATED_AT" || relation.type === "CONNECTED_TO") && to.type !== "place") {
      errors.push(`${relation.id} place target`);
    }
  }

  walk(seed, (key) => {
    if (key && FORBIDDEN_KEYS.has(String(key).toLowerCase())) errors.push(`forbidden key ${key}`);
  });

  return { ok: errors.length === 0, errors };
}

export function buildContribution(input, now) {
  const declaration = String(input.declaration || "");
  if (input.authorized !== true) {
    return { ok: false, error: "La déclaration est requise. Rien n'est envoyé." };
  }
  const packet = {
    schema: "diaspora.contribution.v0",
    status: "submission",
    validation_status: "not-validated",
    publication_status: "not-published",
    created_at: now,
    entity: {
      type: input.type || "organization",
      name: String(input.name || "").trim(),
      location: {
        kind: input.type === "project" ? "project_location" : "organization_location",
        city: String(input.city || "").trim(),
        region: String(input.region || "").trim(),
        country: String(input.country || "").trim()
      },
      corsican_links: String(input.commune || "").trim()
        ? [{
          kind: "corsican_origin_or_link",
          commune: String(input.commune).trim(),
          village: null,
          declared_by: "submitter",
          note: "Déclaration du déposant. Non vérifiée."
        }]
        : [],
      languages: String(input.languages || "").split(",").map((item) => item.trim()).filter(Boolean),
      skills: String(input.skills || "").split(",").map((item) => item.trim()).filter(Boolean),
      offers: String(input.offers || "").split(",").map((item) => item.trim()).filter(Boolean),
      needs: String(input.needs || "").split(",").map((item) => item.trim()).filter(Boolean),
      contact: {
        public_url: String(input.public_url || "").trim(),
        public_email: String(input.public_email || "").trim()
      },
      open_to_help: "unknown",
      visibility: "unlisted",
      notes: String(input.notes || "").trim()
    },
    declaration,
    next_step: "Un humain doit relire ce paquet avant toute publication. Cette page ne l'envoie nulle part."
  };
  if (!packet.entity.name) return { ok: false, error: "Le nom est requis." };
  return { ok: true, packet };
}
