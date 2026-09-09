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

- [`architecture.md`](architecture.md) — architecture d'enquête v2, invariants multi-échelle et continuations ;
- [`corpus.yml`](corpus.yml) — manifeste des sources canoniques et chantiers reliés ;
- [`manuscript/`](manuscript/) — projection narrative minimale de l'édition n°0 ;
- [`projections/book.yml`](projections/book.yml) — contrat minimal de projection livre ;
- [`projections/journal-weekly.yml`](projections/journal-weekly.yml) — placeholder gouverné du journal ;
- [`projections/screenplay.yml`](projections/screenplay.yml) — placeholder de projection scénario ;
- [`projections/conversational-agent.yml`](projections/conversational-agent.yml) — placeholder de l'agent conversationnel ;
- [`editions/index.md`](editions/index.md) — registre des éditions figées ;
- [`journals/README.md`](journals/README.md) — emplacement des journaux de campagne.

## Édition n°0 — bootstrap historique

Les cinq fichiers actuels constituent désormais l'**édition bootstrap historique**. Ils restent utiles et traçables, mais ne définissent plus l'architecture canonique de long terme. Leur but premier était d'exercer la chaîne complète :

```text
sources
→ sélection
→ manuscrit
→ projection
→ HTML / PDF
→ manifeste de provenance
```

Elle est structurée en cinq fichiers : ouverture, Marie-Louise, fermeture des possibles, Machine à Empêcher, réalisation de l'impossible.

## Architecture d'enquête v2

L'architecture courante est décrite dans [`architecture.md`](architecture.md). Elle privilégie :

```text
Reality Case
→ distinction
→ invariant candidat
→ changement d'échelle
→ test du non-invariant
→ mécanisme
→ Act
→ Réel
→ trace
→ correction
```

Elle traite Marie-Louise comme personne et ensemble de traces, Reality Case longitudinal et cas possible d'enquête causale — trois régimes à ne pas confondre. La matière territoriale corse doit être intégrée progressivement comme changement de zoom, en recherchant les invariants sans transférer abusivement les propriétés propres à une échelle.

### Continuations immédiates

- [ ] produire un document source court sur la **grammaire capacitaire multi-échelle et le test d'invariance** ;
- [ ] spécifier le **Reality Case Marie-Louise v2**, incluant un blind review contre le biais rétrospectif ;
- [ ] produire une première projection **« Avant de connaître la fin »**, destinée à remplacer progressivement l'actuel chapitre 01 sans effacer le bootstrap historique.

Ces continuations sont enregistrées mais **non exécutées** à ce stade.

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


## Suspension temporaire — 9 septembre 2026

Le chantier est volontairement suspendu à ce point afin de revenir au dossier de candidature sénatoriale.

Point de reprise :

- architecture courante : [`architecture.md`](architecture.md) ;
- trois continuations immédiates déjà enregistrées dans cette architecture et dans le présent README ;
- aucune de ces continuations n'est réputée exécutée ;
- les cinq fichiers de `manuscript/` restent les artefacts historiques de l'édition bootstrap.

La reprise doit donc partir de l'architecture v2 et non restaurer implicitement l'ancien plan bootstrap.
