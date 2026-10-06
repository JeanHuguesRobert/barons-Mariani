---
title: "Sénatoriales Haute-Corse 2026 — manifeste du paquet de dépôt"
author: "Jean Hugues Noël Robert"
date: "2026-10-06"
status: "pre-filing — materialization control"
language: "fr"
document_role: "operational"
document_kind: "filing-package-manifest"
visibility: "public"
lifecycle_state: "active"
related:
  - "requete-conseil-constitutionnel-projet-v0.14.md"
  - "bordereau-pieces-requete-conseil-constitutionnel-v0.8.md"
---

# Manifeste du paquet de dépôt

## 1. Noyau documentaire

| Objet | Version courante | État |
|---|---|---|
| Requête | v0.14 | texte source prêt pour gel ; non déposé |
| Bordereau | v0.8 | cohérent P-01 à P-43 ; non déposé |
| Inventaire probatoire | v1.6 | outil interne ; ne pas annexer par défaut |
| Checklist | v0.9+ | outil interne ; ne pas annexer par défaut |

## 2. Production A proposée

Les pièces actuellement classées **A — production proposée** dans le bordereau sont :

~~~text
P-04 P-05 P-06
P-09 P-10 P-11 P-12 P-13 P-14 P-15 P-16 P-17
P-19 P-20 P-22
P-27
P-29 P-30 P-31 P-32 P-33
P-39 P-40
~~~

Statut de ce manifeste :

> la présence d'une pièce dans cette liste signifie qu'elle est **candidate prioritaire à la production** ; elle ne certifie pas encore que son fichier final, sa lisibilité, son occultation, sa pagination ou son impression ont été contrôlés.

## 3. Pièces à arbitrer / minimiser

- **P-18** : sensible ; produire seulement si nécessaire à l'argument d'accessibilité, avec minimisation.
- **P-41** : soutien contextuel ; après vérification des principales URLs et affirmations, **ne pas joindre par défaut** sauf décision expresse de soutenir la branche influence.
- **P-42** : diligence Défenseur des droits ; réserve/soutien, pas nécessaire au noyau de recevabilité.
- **P-43** : correspondance privée ; ne produire que les messages strictement nécessaires, sous forme native ou lisible, avec occultation des données non nécessaires.

## 4. Chaîne TA

La séquence P-29 à P-33 doit être matérialisée comme une chaîne intelligible :

~~~text
P-29 — 16/09 demande d'inventaire / vérifications
P-30 — 16/09 réponse du greffe
P-31 — 21/09 nouvelle réponse / disponibilité annoncée
P-32 — 25/09 six questions résiduelles
P-33 — 01/10 refus de commentaires complémentaires + invitation au CC
~~~

La requête doit distinguer :

- demande établie ;
- réponse reçue ;
- document non communiqué ;
- absence de réponse retrouvée ;
- absence de document prouvée, qui est une proposition plus forte et ne doit pas être inférée sans source.

## 5. Contrôle final obligatoire

Pour chaque pièce effectivement annexée, renseigner avant gel :

| N° | fichier / original | pages | lisible | occultation | annexé | SHA si utile |
|---|---|---:|---|---|---|---|
| P-xx | À renseigner | — | [ ] | [ ] | [ ] | — |

Ce tableau doit être remplacé ou complété par l'état réel au moment du gel.

## 6. Invariant

~~~text
Corpus source
≠ bordereau candidat
≠ paquet matériel
≠ paquet effectivement remis
~~~

Le post-filing snapshot devra identifier le quatrième objet sans ambiguïté.
