---
title: "DIASPORA"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-30"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "project"
document_kind: "project-index"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
  - "Grok 4.7 (xAI), cold handler of GitHub issue 96"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/96"
  origin_date: "2026-09-30"
---

# DIASPORA

DIASPORA est une initiative de C.O.R.S.I.C.A. dont la phrase directrice est : **mobiliser les Corses du monde entier.**


Comme les autres Livres Vivants du Corpus, DIASPORA peut être lu avec une grammaire commune :

~~~text
Empêcher
→ Explorer
→ Rendre Capable

Révélateur ↔ Stabilisateur
~~~

Dans DIASPORA, l'annuaire et le graphe jouent d'abord un rôle de **Révélateur** des capacités dispersées ; leur valeur durable dépend ensuite de **Stabilisateurs** de provenance, consentement, correction, actualisation et reprise. Voir [architecture éditoriale](editorial-architecture.md) et [Livre Vivant](../../research/livre_vivant.md).

Le projet est à la fois un livre vivant et un annuaire de capacités. Il passe de « qui est où ? » à « qui peut aider qui à faire quoi ? ». Il ne prétend pas être la première tentative. Corsica Diaspora, depuis 2004, et d'autres réseaux publics, dont communiti, existent déjà.

Le nom public visé est `diaspora.acorsica.org`. Ce dépôt ne le sert pas encore.

Entrées :

- livre : [`web/book.html`](web/book.html) et [`manuscript/00-ouverture.md`](manuscript/00-ouverture.md)
- annuaire : [`web/directory.html`](web/directory.html)
- jeu de données : [`data/seed.json`](data/seed.json)
- journal du Reality Test : [`journals/reality-test-2026-09-30.md`](journals/reality-test-2026-09-30.md)
- issue : <https://github.com/JeanHuguesRobert/barons-Mariani/issues/96>

## Build and test

From `projects/diaspora`, with Node, and without installing packages:

```text
node scripts/validate-seed.js
node scripts/serve.js
```

The server prefers `http://127.0.0.1:8765/`. If that port is already taken and `PORT` is unset, it tries the next ports and prints the URL that actually opened. Set `PORT` to require one port. `/` redirects to `/web/index.html`. Opening the HTML files directly will not load the seed. The checks cover the seed invariants, search, the separation between a place of presence and a Corsican link, and the rule that holding a need does not make an entity a helper.

`npm test` runs the same check when npm is available. No dependency is required.

## Scope of this slice

Included: schema, sourced seed, static directory, map-ready locations, explainable matching, local contribution packets, living-book entry, benchmark skeleton, reality-test journal.

The static tree is published at `https://diaspora.acorsica.org`. See `deploy/README.md` for the release pointer. Still not included: accounts, a graph database, AI enrichment, a frozen edition, and any claim that the two-hour benchmark produced worldwide coverage.
