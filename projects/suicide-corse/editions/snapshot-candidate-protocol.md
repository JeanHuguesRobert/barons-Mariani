---
title: "Suicide Corse — protocole de snapshot candidat au gel"
author: Jean Hugues Noël Robert
status: working-paper
date: '2026-09-18'
document_role: operational
document_kind: snapshot-protocol
visibility: public
lifecycle_state: planned
update_policy: UP-DEFAULT-REVIEWED
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
language: fr
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: repository
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: issue-75-closing-window
  origin_date: '2026-09-18'
  derived_from:
    - projects/suicide-corse/projections/book-2026-09-17-anniversaire.yml
    - https://github.com/JeanHuguesRobert/barons-Mariani/issues/75
---

# Protocole de snapshot candidat au gel

Ce document prépare un snapshot **candidat** au gel de l'édition anniversaire.
Il n'est pas lui-même un snapshot, ne change pas le statut `draft` de l'édition
et ne décide pas d'un gel définitif.

## Seuil temporel convenu

La fenêtre éditoriale du 17 septembre se clôt selon la convention suivante :

```text
lieu de référence : Corte, Corsica
seuil : 2026-09-18T07:05:11+02:00
```

Avant ce seuil, aucun snapshot candidat ne doit être présenté comme clôturant
la fenêtre. Après ce seuil, chaque nouveau fait éditorial substantiel appelle
un nouveau rendu traçable ou un erratum, même si l'édition demeure `draft`.

## Date d'édition et instants techniques

La date portée par une édition désigne sa **fenêtre de production**, non
l'instant auquel un fichier devient accessible. L'édition du 17 septembre 2026
comprend donc les rendus produits entre le lever du soleil du 17 et le seuil de
clôture du 18 septembre à Corte.

Le reçu distingue obligatoirement :

```text
edition_date       = date de la fenêtre de production
production_window  = début et fin conventionnels de cette fenêtre
rendered_at        = instant technique du rendu
published_at       = première disponibilité publique de l'artefact
deployed_at        = bascule de la release effectivement servie
```

Un rendu, un push ou un déploiement intervenant avant la fin de la fenêtre
conserve `edition_date: 2026-09-17`, y compris s'il se produit après minuit
civil. Après le seuil, un changement éditorial substantiel relève d'une édition
ultérieure ou d'un erratum ; l'accessibilité publique tardive d'un artefact ne
change pas, à elle seule, la date de son édition.

## Préconditions

1. Source Corpus et renderer à jour, propres et identifiés par commit.
2. Projection `book-2026-09-17-anniversaire.yml` relue comme préversion.
3. Rendu frais HTML, PDF et EPUB par Ubikia/Quarto.
4. Manifeste présent, parseable et cohérent avec le commit source observé.
5. Diff du dépôt d'artefacts lu avant tout commit ou promotion.
6. Promotion de release distincte du push Git et vérification HTTPS distincte
   de la promotion.

## Reçu de snapshot à produire

Le reçu candidat doit consigner, sans information privée :

```text
observed_at
closing_threshold
edition_date
production_window
rendered_at
published_at
deployed_at
source_repository + source_commit + source_dirty
renderer_repository + renderer_commit
projection path + projection SHA-256
manifest SHA-256
HTML / PDF / EPUB paths and SHA-256
artifact_repository + artifact_commit
Fracta2 release path
public endpoint status and content type
publication_status
```

Le reçu doit aussi identifier la release précédente, afin qu'un retour arrière
opérationnel reste possible sans confondre ce retour avec une réécriture de
l'histoire éditoriale.

## Réserves obligatoires

Le snapshot candidat doit répéter les limites suivantes :

- `publication_status: draft` ne devient pas un statut final ;
- l'enquête et l'appel à témoignages restent ouverts ;
- la revue contradictoire indépendante reste à réaliser ;
- les personnes identifiables dans les notes de recherche sont des sources,
  témoins potentiels ou pistes, non des personnes mises en cause ;
- le canal email de contribution est actif, mais ses messages ne sont ni
  publics ni automatiquement exploitables ;
- toute correction substantielle postérieure doit être publiée comme nouvelle
  projection ou erratum traçable.

## Décision ultérieure

Un gel définitif exige une décision éditoriale humaine distincte, après lecture
du reçu candidat et de ses réserves. Cette décision ne peut pas être déduite de
l'existence d'un rendu, d'un commit, d'un push ou d'une release accessible.
