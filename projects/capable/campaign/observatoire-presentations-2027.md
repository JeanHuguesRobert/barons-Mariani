---
title: "Observatoire des Présentations 2027 — working paper"
description: "Working paper définissant un observatoire public et traçable des proclamations et présentations présidentielles de 2027."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-04"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/capable/campaign/observatoire-presentations-2027.md"
update_policy: "UP-DEFAULT-REVIEWED"
document_role: "source"
document_kind: "campaign-observatory"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "explicit-metadata"
classification_confidence: "medium"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "e9a46dce274187a3bd6947da56f107b6cec705d2"
  origin_date: "2026-10-04"
  derived_from:
    - "architecture-des-campagnes.md"
    - "../public-claims.md"
    - "../manuscript/05-machines-et-correction.md"
    - "../manuscript/08-presidentielle-2027.md"
review:
  status: "partial"
  reviewed_by:
    - "Jean Hugues Noël Robert"
  reviewed_at: "2026-10-04"
  scope: "Architecture, principes et cohérence générale approuvés ; revue détaillée ligne par ligne et revue adverse encore ouvertes."
---

# Observatoire des Présentations 2027

## Objet

L'Observatoire est un **Révélateur électoral** : il conserve les proclamations publiques relatives aux « parrainages » ou présentations présidentielles, les qualifie, puis les confronte à leur matérialisation officielle lorsque celle-ci devient observable.

Il ne présume pas qu'un écart établit un mensonge.

```text
proclamation
→ source
→ date
→ qualification
→ matérialisation officielle
→ écart observable
→ explications concurrentes
```

## Principe de non-confusion

Les états suivants ne sont jamais additionnés ni assimilés :

```text
P0 — contact
P1 — réponse
P2 — intérêt
P3 — intention favorable
P4 — promesse explicite
P5 — présentation envoyée
P6 — présentation officiellement publiée / validée
```

Invariant :

> **On ne compte jamais un état N comme s'il était déjà N+1.**

## Traces

Chaque proclamation candidate doit pouvoir conserver au minimum :

```yaml
trace_id:
candidate:
observed_at:
source_type:
source_url:
claim_type:
claimed_value:
wording:
definition_provided:
evidence_status:
notes:
```

Une nouvelle proclamation crée une nouvelle trace ; elle ne réécrit pas silencieusement la précédente.

## Relation avec le registre Capable

`projects/capable/public-claims.md` reste le registre des proclamations publiques de Capable.

L'Observatoire généralise la même primitive à l'ensemble des candidatures pertinentes sans fusionner les deux registres.

## Révélateur / Stabilisateur

Révélateur :

> rendre visible l'écart entre ce qui a été proclamé et ce qui s'est effectivement matérialisé.

Stabilisateur :

- vocabulaire commun ;
- états normalisés ;
- provenance ;
- historique ;
- snapshots ;
- exports ouverts ;
- rapprochement avec les publications officielles.

## Symétrie

Capable doit être observé selon les mêmes règles que les autres candidatures.

L'objectif n'est pas de produire un « score de sincérité », mais de permettre au lecteur de distinguer :

- ce qui a été annoncé ;
- ce qui était défini ;
- ce qui a été sourcé ;
- ce qui s'est matérialisé ;
- ce qui reste inexpliqué.

## Produits possibles

Après le 7 octobre, et sans détourner de ressources du contentieux prioritaire :

- base de données ;
- tableau de bord ;
- journal des traces ;
- exports JSON / CSV ;
- snapshots versionnés ;
- API éventuelle ;
- agent conversationnel spécialisé.

## Prototype minimal

Un prototype utile peut se limiter à quelques traces réelles et à une table :

```text
Candidat | Date | Chiffre déclaré | Nature | Source | État officiel
```

Le prototype doit montrer la méthode avant de prétendre à l'exhaustivité.

## Priorité

Jusqu'au dépôt de la requête au Conseil constitutionnel le 7 octobre 2026 à 18 h, cet Observatoire reste **P2/P3**.

Sa sophistication technique ne doit pas mettre en risque le P0 procédural.
