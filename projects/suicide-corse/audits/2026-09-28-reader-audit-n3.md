---
title: "Suicide Corse n°3 — audit de lecture grand public"
author: "Jean Hugues Noël Robert"
date: "2026-09-28"
status: "completed"
language: fr
license: CC BY-SA 4.0
document_role: "editorial-audit"
document_kind: "reader-audit"
visibility: public
lifecycle_state: active
update_policy: UP-DERIVED-SOURCE-LOCKED
provenance:
  origin_type: editorial-review
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: main
  derived_from:
    - projects/suicide-corse/projections/book-n3-working.yml
    - projects/suicide-corse/projections/n3-editorial-architecture.md
review:
  status: "assistant-reviewed"
  reviewed_by:
    - "GPT-5.6 Sol"
---

# Suicide Corse n°3 — audit de lecture grand public

## Objet

Cet audit vérifie la projection n°3 comme **expérience de lecture**, distinctement de l'audit documentaire et juridique.

Critère principal :

> le lecteur doit pouvoir comprendre le corps principal sans devenir archiviste du Corpus.

## Résultat global

**PASS — projection prête pour un rendu de vérification.**

Cela ne vaut ni gel éditorial ni publication.

## Volumes

### Livre

Ordre actuel :

1. Ouverture — 891 mots
2. Marie-Louise — une vie en mouvement — 1 825 mots
3. La parole de Marie-Louise — 1 573 mots
4. Quand les possibles se ferment — 873 mots
5. La Machine à Empêcher — 896 mots
6. De l'empêchement à la capacité — 1 619 mots
7. Changer d'échelle : la Corse — 1 302 mots
8. Réaliser l'impossible — 637 mots

**Total Livre : environ 9 616 mots.**

La cible de 9 100–11 800 mots est respectée.

### Magazine

Six rubriques récurrentes, première passe modulaire : environ **1 050 mots**, plus une courte page d'ouverture.

Cette brièveté est volontaire. Le Magazine pourra être enrichi si un rendu réel fait apparaître une rupture de rythme ou un manque de contexte ; il ne doit pas être rempli pour atteindre un quota.

## Contrôles

### R1 — Marie-Louise apparaît avant la théorie

**PASS.**

Le chapitre directement consacré à Marie-Louise est passé d'environ 184 à 1 825 mots. Il commence par ses créations, études, déplacements, engagements et tentatives de réouverture.

### R2 — Ouverture non envahissante

**PASS.**

L'ouverture est passée d'environ 1 395 à 891 mots. La méthode nécessaire reste présente, mais la pipeline et l'appareil documentaire ne précèdent plus la personne.

### R3 — Redondance conceptuelle

**PASS avec résidu acceptable.**

Les anciens chapitres `04`, `05` et `10` ont été recomposés en un chapitre reader-first `04-realiser-impossible.md`.

Les anciens `06` et `07` ont été recomposés en `06-vivre-transmettre.md`.

Les sources fusionnées restent dans le Corpus mais ne sont plus rendues comme chapitres successifs du Livre.

### R4 — Changement d'échelle

**PASS.**

Le chapitre Corse commence désormais par la limite de l'analogie : comparer des relations, non des psychologies.

Les détails du test d'invariance sont renvoyés en annexe.

### R5 — Sénatoriales

**PASS.**

Le Reality Case conserve les résultats observés et retire l'inférence qui transformait les 36 blancs et 40 nuls en réserve attribuable à une candidature absente.

Le scrutin contrefactuel reste explicitement inconnu.

### R6 — Contradiction

**PASS.**

Le Magazine possède une rubrique récurrente `Contrepoints`.

Refus, objections et contributions adverses peuvent y être signalés sans publication brute ni promotion automatique en faits.

### R7 — Vie privée

**PASS.**

Les nouveaux courriels privés et photographies sont projetés par leur existence, provenance, qualification ou conséquence documentaire seulement.

Aucune photographie privée nouvelle n'est publiée dans la recomposition n°3.

### R8 — Séparation Livre / Magazine / Annexes

**PASS.**

La liste de rendu comporte désormais trois blocs visibles :

~~~text
BOOK
MAGAZINE
ANNEXES
~~~

Deux pages de séparation explicites rendent cette architecture lisible.

### R9 — Références héritées de l'ancien sommaire

**PASS sur le Livre principal.**

Contrôle direct des huit fichiers du Livre : absence des références obsolètes ciblées `chapitre 14`, `chapitre 16` et de la formulation présentant la campagne sénatoriale 2026 comme encore en cours.

Les annexes historiques peuvent conserver des références internes à leurs propres états éditoriaux ; elles ne déterminent plus le flux principal.

### R10 — Structure de projection

**PASS.**

Contrôle direct de `book-n3-working.yml` :

- un seul `chapters_note` ;
- un seul `outputs` ;
- présence des trois couches ;
- conclusion dédiée présente ;
- introduction Magazine présente ;
- introduction Annexes présente ;
- anciens chapitres fusionnés `05` et `07` absents du rendu principal.

## Résidu non bloquant

- Le monolithe `18-le-reel-repond-2026-09-28.md` reste dans le Corpus comme snapshot/source historique mais n'est plus la surface Magazine préférée.
- Le Magazine modulaire est volontairement court ; le rendu visuel permettra de décider s'il faut enrichir certaines rubriques.
- Les annexes restent volumineuses par nature ; leur fonction est précisément de permettre la vérification sans alourdir le Livre.
- Cet audit ne remplace pas la validation du rendu final HTML/PDF/EPUB.

## Décision d'audit

La projection peut passer de :

~~~text
render_ready: false
~~~

à :

~~~text
render_ready: true
~~~

pour permettre un **rendu de vérification**.

Ce changement ne constitue pas :

- un freeze ;
- une publication ;
- une clôture de la fenêtre de contribution ;
- une validation définitive du rendu produit.
