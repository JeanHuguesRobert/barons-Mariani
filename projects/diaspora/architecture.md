---
title: "DIASPORA — implementation architecture"
date: "2026-09-30"
status: "working-paper"
language: "en"
document_role: "project-architecture"
document_kind: "working-note"
visibility: "public"
ai_assisted_by:
  - "Grok 4.7 (xAI), cold handler of GitHub issue 96"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/96"
  origin_date: "2026-09-30"
---

# DIASPORA — implementation architecture

Phase 1 is a static projection over one JSON seed. There is no account system, no application server, and no graph database.

```text
data/seed.json
  → web/logic.js          search, match, metrics, validation, contribution packets
  → web/*.html + app.js   French public pages
  → scripts/validate-seed.js
```

Relations stored in the seed are the capability graph. Matching reads those edges. It does not invent new facts.

## Location kinds

These stay separate:

- `organization_location` and `project_location` — where an organization or a project is publicly placed
- `current_location` — reserved for a person, unused in the phase-1 seed
- `corsican_origin_or_link` — a sourced Corsican commune, or an island-level link when no commune is sourced

A region filter uses presence only. A Corsican-link filter uses the link only.

## Matching

A candidate is a published person, organization, or project.

- Region must match presence.
- Capability must match a related skill or offer name.
- A need matches only through `CAN_ADDRESS`, or through an offer whose name contains the need's tokens.
- An entity that `NEEDS` something is the holder of that need, not a helper.
- `open_to_help` is `true`, `false`, or `unknown`. `unknown` is excluded when the query requires an explicit willingness to help.

The only `open_to_help: true` offer in the phase-1 seed is this project's own correction path.

## Contribution

`buildContribution` returns a `diaspora.contribution.v0` packet with `status: submission`, `validation_status: not-validated`, and `publication_status: not-published`. The page does not send it.

## Reuse audit

### Generic

Reused as doctrine and page shape, not imported as a runtime:

- Living-publication chain and the rule "freeze the edition, never the next projection", from `projects/suicide-corse/editorial-architecture.md` and `projects/rise-and-fall/editorial-architecture.md`.
- Book / magazine / annexes.
- Hand-written static HTML, as in `projects/rise-and-fall/site/`.
- C.O.R.S.I.C.A. name expansion from `projects/capable/README.md` and `projects/capable/genesis.md`.
- Corpus frontmatter and the rule that a GitHub issue is part of the corpus.

### Parametric

- `corpus.yml` follows the suicide-corse / rise-and-fall manifest shape, with DIASPORA paths and schema id.
- The reality-test journal follows the fields required by issue 96.

### Project-specific

- Actor, offer, need, and skill model.
- Match rules above.
- The public seed and its minimization choices.
- The local contribution packet.
- The unresolved status of the name "Suna".

### Missing

- The Suicide Corse / Ubikia renderer is not wired in. Pulling it into this pass would spend the experiment on generic machinery. Editorial invariants are referenced; the directory is local HTML.
- No production vhost, DNS record, or Operium change for `diaspora.acorsica.org`.
- No primary source for "Suna".
- No bulk RNA import.
- No legal opinion.

## Runtime dependencies

Pages, logic, and tests have no installed packages. The map page optionally loads Leaflet 1.9.4 and OpenStreetMap tiles. If that load fails, the text list remains.

## Deployment boundary

See `deploy/README.md`. Preparing that note is not a deployment.
