---
title: Registre des représentations d’identité
description: Registre factuel des formes sous lesquelles les identités du référentiel Barons Mariani sont représentées par des tiers.
author: Jean Hugues Noël Robert, baron Mariani
date: '2026-09-18'
last_modified_at: '2026-09-18'
version: '0.2'
status: working
language: fr
license: CC BY-SA 4.0
document_role: registry
document_kind: identity-representation-registry
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: conversation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: unknown
  origin_date: '2026-09-18'
  derived_from:
    - identity/public-identity-registry.md
    - research/genealogy/title_baron_mariani_evidence_chain.md
    - memory/marie-louise/carte.md
review:
  status: human-directed
  reviewed_by:
    - Jean Hugues Noël Robert
---

# Registre des représentations d’identité

## Objet

Ce registre conserve les représentations produites par des administrations,
institutions, médias, plateformes ou autres tiers.

Une différence avec le référentiel n’est **pas automatiquement une altération
fautive**.

## Qualification

Chaque occurrence peut recevoir l’une des qualifications provisoires suivantes :

- `FIDÈLE`
- `VARIANTE`
- `NORMALISATION`
- `ERREUR CERTAINE`
- `QUALIFICATION ÉDITORIALE`
- `À DÉTERMINER`

Une qualification peut évoluer lorsque de nouvelles preuves apparaissent.

## Schéma minimal

Chaque entrée doit documenter :

- personne ou objet concerné ;
- acteur ;
- date ;
- contexte ;
- forme source connue ;
- forme publiée exacte ;
- transformation observée ;
- qualification ;
- preuve ;
- éventuelle démarche de rectification ;
- réponse ;
- état final.

## Registre initial

### REP-2017-001 — Ministère de l’Intérieur — Baron Mariani

- **objet :** `JHR-001`
- **acteur :** Ministère de l’Intérieur
- **contexte :** élections législatives 2017, Haute-Corse 2B-02
- **forme publique :** `M. Le BARON MARIANI`
- **forme de candidature documentée :** `Baron Mariani`
- **transformation :** ajout d’une civilité et normalisation typographique
- **qualification :** `NORMALISATION`
- **preuve :** résultats électoraux officiels + dossier 2017
- **état :** clos comme occurrence documentaire

Cette occurrence constitue également une preuve positive de l’usage
institutionnel de l’identité publique.

### REP-2017-002 — Marie-Louise d'Angelis

- **objet :** `ML-001`
- **contexte :** législatives 2017
- **forme documentée de candidature :** `Marie-Louise d'Angelis`
- **qualification :** `FIDÈLE`
- **preuves internes :** récépissé définitif de candidature et courriels contemporains
- **source :** `memory/marie-louise/elections/2017-legislatives.md`

Cette entrée documente un usage positif ; elle est conservée afin que des
représentations ultérieures puissent être comparées à une source datée.

### REP-2024-001 — Conseil constitutionnel / Journal officiel

- **objets :** `JHR-001`, `ML-001`
- **acteur :** Conseil constitutionnel
- **contexte :** décision n° 2024-6309 AN
- **forme publiée :** `baronne et baron MARIANI`
- **qualification de l’institution :** `noms d'usage`
- **qualification du registre :** `VARIANTE`
- **état :** occurrence institutionnelle établie

Cette entrée est particulièrement importante parce que la source ne se contente
pas de reproduire une graphie : elle qualifie explicitement les formes employées
de `noms d'usage`.

### REP-2026-001 — Sénat — Baron MARIANI

- **objet :** `JHR-001`
- **acteur :** Sénat
- **contexte :** élections sénatoriales 2026, Haute-Corse
- **forme publiée :** `Baron MARIANI`
- **forme publique de référence :** `Baron Mariani`
- **transformation :** capitalisation du patronyme / segmentation de l’identité
- **qualification :** `NORMALISATION` / `À DÉTERMINER`
- **état :** actif

La qualification juridique de cette transformation est volontairement laissée
à la projection `identity/legal/`.

### REP-2026-002 — Ministère de l’Intérieur — `Maire-Louise`

- **objet :** identité de la remplaçante de la candidature sénatoriale 2026
- **acteur :** Ministère de l’Intérieur
- **source :** fichier national des candidatures individuelles au scrutin majoritaire
- **forme déclarée documentée :** `Marie-Louise`
- **forme publiée :** `Maire-Louise`
- **transformation :** permutation interne des lettres dans le prénom
- **qualification :** `ERREUR CERTAINE`
- **état :** rectification demandée

La version conservée du fichier comporte notamment :

- 223 lignes de candidature ;
- séparateur `;` ;
- SHA-256
  `cef331e9565648d6c19ecfc659aba9f01555151a26aa22c46cafaf291fbd8830`.

Une demande de rectification a été adressée au délégué à la protection des
données du ministère le 16 septembre 2026.

### Occurrences médiatiques à intégrer

Les occurrences médiatiques déjà repérées seront ajoutées après vérification
individuelle de leur texte et de leur date.

Les termes tels que :

- `pseudonyme de Baron Mariani` ;
- `dit le Baron Mariani` ;
- `les barons Mariani` ;

seront enregistrés comme **formes publiées exactes**. Lorsqu’ils constituent une
qualification du média plutôt qu’une simple graphie, leur état initial sera
`QUALIFICATION ÉDITORIALE`, sans conclure dans ce registre à leur exactitude
juridique.

## Principe

> Une représentation est une projection d’une source ; elle doit rester
> traçable comme projection et ne pas devenir silencieusement la nouvelle source.
