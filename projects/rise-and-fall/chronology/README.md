---
title: "Rise & Fall of the Mariani Family — Master Timeline"
subtitle: "Chronologie critique intégrée des bifurcations familiales et patrimoniales (1776–2026)"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-30"
last_modified_at: "2026-09-30"
version: "0.1"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "chronology-index"
document_kind: "readme"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/chronology/README.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "corpus-consolidation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "GitHub issue #94"
  origin_date: "2026-09-30"
  derived_from:
    - "musee-mariani/personnes/README.md"
    - "projects/rise-and-fall/architecture.md"
    - "research/relevement_nom_dangelis.md"
    - "research/protestation_electorale_1863_mariani_gavini.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Master Timeline — Rise & Fall of the Mariani Family

## 0. Rôle de la chronologie critique

Ce dossier héberge la **colonne vertébrale chronologique** du projet *Rise & Fall of the Mariani Family*.

Elle sert de référence commune et d'arbitre pour les deux démarches méthodologiques :
- **Pass A (Archéologie régressive) :** Remonter de 2026 à 1776 en s'assurant que chaque saut vers l'amont repose sur un maillon temporel réel et documenté.
- **Pass B (Reconstitution des possibles) :** Dérouler les bifurcations dans l'ordre naturel du temps (1776 $\to$ 2026) pour vérifier qu'aucune causalité anachronique n'est projetée sur le passé.

---

## 1. Données structurées (`00_master_timeline.tsv`)

Les événements majeurs sont consignés de manière tabulaire dans le fichier [`00_master_timeline.tsv`](00_master_timeline.tsv).

Chaque ligne comporte :
1. `event_id` : Identifiant unique de l'événement (ex. `EVT-1863-GAVINI`) ;
2. `date_display` : Date lisible ou période ;
3. `date_sort` : Date normalisée ISO pour le tri (`YYYY-MM-DD` ou `YYYY`) ;
4. `actors` : Personnes et institutions impliquées ;
5. `proof_code` : Code critique du degré de preuve (**E**, **P**, **S**, **D**, **O**) ;
6. `title` : Intitulé factuel de la bifurcation ;
7. `capacity_delta` : Impact direct sur les capacités familiales (patrimoine, droit, politique, réputation) ;
8. `source_primary_ref` : Source de référence dans le dépôt ou aux archives.

---

## 2. Codes de preuve applicables

Conformément à la grille du Musée Mariani ([`musee-mariani/notes-critiques/preuves-et-incertitudes.md`](../../musee-mariani/notes-critiques/preuves-et-incertitudes.md)) :

| Code | Signification |
|:---:|---|
| **E** | **Établi** par une source primaire directe, un acte d'état civil, un document authentique ou officiel. |
| **P** | **Probable** / forte convergence documentaire, encore à fermer par un acte juridique direct. |
| **S** | Donnée provenant d'une **source secondaire** (généalogie imprimée, annuaire, biographie). |
| **D** | **Discordance** entre plusieurs sources documentaires (à maintenir ouverte jusqu'à résolution). |
| **O** | Question ouverte / **blanc documentaire** nécessitant une recherche en archives. |

---

## 3. Règle d'or de maintenance

Une date incertaine ou une parenté présumée ne doit jamais être maquillée en certitude pour fluidifier le récit. Tout changement de statut dans la chronologie doit être consigné dans le journal d'enquête du projet.
