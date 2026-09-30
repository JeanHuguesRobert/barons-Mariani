---
title: "DIASPORA data model"
date: "2026-09-30"
language: "en"
document_role: "annex"
visibility: "public"
---

# Data model

Machine-readable contracts:

- `schemas/entity.schema.json`
- `schemas/relation.schema.json`
- `schemas/contribution.schema.json`

The executable check is `scripts/validate-seed.js`. It is stricter than the JSON Schema files: dangling edges, forbidden contact keys, unsourced public records, invented villages, and non-allowlisted public emails fail the script.

## Entity types

`person`, `organization`, `project`, `place`, `skill`, `need`, `offer`, `source`.

Phase 1 publishes no `person`.

## Relation types

`HAS_SKILL`, `OFFERS`, `NEEDS`, `MEMBER_OF`, `CONNECTED_TO`, `RUNS`, `CAN_ADDRESS`, `LOCATED_AT`.

`MEMBER_OF` is allowed and unused. No membership was sourced.

`CAN_ADDRESS` runs from an offer to a need. In this seed the only such edge is the project's correction offer addressing the project's own need for sourced records. It does not claim to fulfil Corsica Diaspora's five-year project.

## Publication states

`submitted`, `validated`, and `published` are different. Search and match read `visibility: public` and `publication_status: published` only.

## Identifiers

Stable ids are lowercase kebab-case. Public page: `web/entity.html?id=<id>`. Export: `data/seed.json`.
