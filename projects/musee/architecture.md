---
title: "Musée — Architecture du Livre Vivant"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-11-15"
last_modified_at: "2026-11-15"
status: working-paper
language: fr
license: CC BY-SA 4.0
document_role: operational
document_kind: technical-architecture
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/musee/architecture.md
provenance:
  origin_type: conversation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: "mandat de création du Livre Vivant du Musée, 2026-11-15"
  origin_date: "2026-11-15"
  derived_from:
    []
review:
  status: unreviewed
  reviewed_by: []
---

# Architecture technique du Livre Vivant Musée

Le corpus d'enquête historique et territoriale demeure sous [`musee-mariani/`](../../musee-mariani/README.md). Le répertoire `projects/musee/` est l'**œuvre éditoriale** qui raconte les activités du Musée, sans recopier les dossiers.

```text
projects/musee/
  README.md                    point d'entrée
  living-book.yml             manifeste Living Book Factory
  corpus.yml                  frontières documentaires
  editorial-architecture.md   régime de preuve et actualisation
  manuscript/n1/              Livre — numéro 1 en préparation
  magazine/                   journal d'activité daté
  annexes/                    index des sources et preuves
  projections/n1-working.yml  projection évolutive, non gelée
  editions/index.md           registre des gels (aucun)
  site/                       projection HTML dérivée
  deploy/README.md            état de déploiement (non déployé)
```

Le Livre peut être validé par l'outillage `living-book` du Corpus dans un environnement où le script est accessible. **Aucune exécution de ce validateur n'est présumée** par la seule création des fichiers. Le déploiement est sous la responsabilité opérationnelle d'Operium.
