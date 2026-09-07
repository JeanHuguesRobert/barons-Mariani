---
title: "Suicide Corse — projet éditorial réactif"
description: "Point d'entrée canonique du projet Suicide Corse et de ses projections éditoriales."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-09-07"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "source-index"
document_kind: "project-readme"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/suicide-corse/README.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "generated"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-09-07"
  derived_from:
    - "GitHub issue #42"
    - "GitHub issue #43"
    - "memory/marie-louise/carte.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Suicide Corse

**Titre de travail : _Suicide Corse, ou comment réaliser l'impossible_.**

Ce répertoire matérialise le projet éditorial comme une **projection réactive du Corpus**, et non comme une nouvelle source autonome de vérité.

Le mouvement général est :

```text
Corpus canonique
→ carte / sélection des sources
→ projection éditoriale
→ publication / interaction / Act
→ réponse du Réel
→ nouvelles traces
→ correction du Corpus
→ nouvelle projection
```

## Principe documentaire

Le livre ne doit pas effacer la distinction entre :

- trace ;
- fait suffisamment documenté ;
- témoignage tiers ;
- assertion ;
- interprétation ;
- reconstruction ;
- hypothèse ;
- inconnu.

Concernant Marie-Louise, la source de synthèse actuelle est [`memory/marie-louise/carte.md`](../../memory/marie-louise/carte.md). Elle reste distincte du manuscrit.

## Structure

- [`corpus.yml`](corpus.yml) — manifeste des sources canoniques et chantiers reliés ;
- [`manuscript/`](manuscript/) — projection narrative minimale de l'édition n°0 ;
- [`projections/book.yml`](projections/book.yml) — contrat minimal de projection livre ;
- [`projections/journal-weekly.yml`](projections/journal-weekly.yml) — placeholder gouverné du journal ;
- [`projections/screenplay.yml`](projections/screenplay.yml) — placeholder de projection scénario ;
- [`projections/conversational-agent.yml`](projections/conversational-agent.yml) — placeholder de l'agent conversationnel ;
- [`editions/index.md`](editions/index.md) — registre des éditions figées ;
- [`journals/README.md`](journals/README.md) — emplacement des journaux de campagne.

## Édition n°0

L'édition n°0 doit rester courte, imparfaite et utile. Son but premier est d'exercer la chaîne complète :

```text
sources
→ sélection
→ manuscrit
→ projection
→ HTML / PDF
→ manifeste de provenance
```

Elle est structurée en cinq fichiers : ouverture, Marie-Louise, fermeture des possibles, Machine à Empêcher, réalisation de l'impossible.

## Règle Marie-Louise

Ne jamais fabriquer une parole, une volonté ou un consentement posthume de Marie-Louise. Les formulations interprétatives ou causales doivent rester explicitement qualifiées comme telles.

## Issues

- #42 — chantier parent ;
- #43 — bootstrap canonique et édition 0 ;
- #44 — snapshot hebdomadaire et Journal de campagne ;
- #45 — traces Marie-Louise 2008/2016 ;
- #47 — Machine à Empêcher et causalité ;
- #48 — Twin documentaire Marie-Louise ;
- #49 — scénario ;
- #50 — agent conversationnel ;
- #51 — Reactive Publication ;
- #52 — continuité de protection.

Dépendance générique de rendu : `JeanHuguesRobert/ubikia#24`.
