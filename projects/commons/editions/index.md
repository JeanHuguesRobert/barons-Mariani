---
title: "Commons — Index des éditions"
description: "Registre des éditions gelées du Livre Vivant Commons. Aucune édition n'est gelée dans cette tranche initiale."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/commons/editions/index.md"
update_policy: "UP-DEFAULT-REVIEWED"
document_role: "source-index"
document_kind: "edition-index"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
  - "Antigravity — drafting assistance, 2026-10-04"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/108"
  origin_date: "2026-10-04"
  derived_from:
    - "projects/privai/editions/index.md"
    - "research/livre_vivant.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Index des éditions — Commons

Aucune édition gelée définitive n'est arrêtée à ce jour.

Le projet a achevé l'ensemble des critères d'acceptation de son amorçage initial (**Phase 1**), instanciant les cinq faces de l'architecture éditoriale. Cette maturité permet d'établir une première **Release Candidate (RC1)** sous revue.

---

## 1. Candidature au gel : Édition n°1 — Release Candidate 1 (RC1)

- **Identifiant :** `edition-commons-n1-rc1`
- **Titre :** *Les biens communs, du passé au futur — Des communaux au cloud*
- **Statut :** `release-candidate`
- **Date d'ancrage :** 4 octobre 2026
- **Baseline commit de référence :** [`0f9576b`](https://github.com/JeanHuguesRobert/barons-Mariani/commit/0f9576b)
- **Périmètre documentaire immuable candidat :**
  1. **Face Livre — Corps principal :** Les 4 mouvements du manuscrit n°1 (`projects/commons/manuscript/n1/01-heritages.md` à `04-futurs-possibles.md`).
  2. **Face Livre — Annexes démonstratives :** *Carta de Foresta* (1217), archives communales corses, grille d'audit Ostrom (/24), comparatif critique des licences d'IA (`projects/commons/annexes/`).
  3. **Face Magazine :** Enquête sur l'enclosure du cloud et de l'IA ; retour de terrain sur les microréseaux solaires FractaVolta et les unités Kudos/CXU (`projects/commons/magazine/`).
  4. **Face Site Web :** Surface statique de lecture publique universelle (12 pages HTML5 sans framework externe sous `projects/commons/site/`, `styles.css`, `robots.txt`, `llms.txt`, `sitemap.xml`).
  5. **Face Agent Conversationnel & Collecte :** Profil d'inférence borné (`projects/commons/guide-profile.yml`), script client et générateur d'objections locales (`guide.html`, `guide.js`, `contribuer.html`).
  6. **Appareil critique et méthodologique :** 8 fiches de cas sous le modèle à 14 descripteurs (`projects/commons/cases/`), frise 1217–2026 (`projects/commons/chronology/`), cartographie des sources (`projects/commons/sources/`).

---

## 2. Règle doctrinale d'immuabilité et de vivant

Conformément à la doctrine fondamentale du Livre Vivant (`research/livre_vivant.md`) :

> **Freeze the edition, never the next projection.**  
> **Geler l'édition, jamais la projection suivante.**

1. Le gel définitif d'une édition future fixera un SHA-1 Git immuable et une empreinte cryptographique SHA-256 de chaque document source.
2. Une édition gelée n'est plus jamais réécrite : les erreurs, contestations ou nouvelles preuves issues du Réel sont intégrées dans les projections vivantes ultérieures (`projects/commons/projections/n1-working.yml` et suivantes).
3. Le corpus vivant continue d'évoluer en parallèle de l'édition gelée.
