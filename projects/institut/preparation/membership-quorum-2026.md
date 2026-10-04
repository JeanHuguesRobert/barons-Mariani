---
title: "C.O.R.S.I.C.A. — quorum préparatoire 2026"
subtitle: "Établir le corps votant avant toute assemblée modificative"
description: "Registre public minimal des conditions de calcul du quorum, sans publication des coordonnées ni de la liste nominative privée des membres."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-04"
version: "0.2"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/membership-quorum-2026.md"
document_role: "operational"
document_kind: "governance-register"
document_function: "quorum reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/statuts-1995-transcription.md"
  - "projects/institut/preparation/statutes-lineage.md"
  - "projects/institut/preparation/ag-age-2025-2026.md"
provenance:
  origin_type: "privacy-minimized-reconstruction"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-04"
  derived_from:
    - "private membership register — aggregate only"
    - "governance records 2020 and 2025"
review:
  status: "unreviewed"
  reviewed_by: []
---

# C.O.R.S.I.C.A. — quorum préparatoire 2026

## 1. Règle

Si les statuts 1995 restent applicables, l’article 17 exige pour la première assemblée modificative la présence ou représentation d’au moins **un quart des membres en exercice**.

L’article 8 inclut dans l’assemblée générale les membres fondateurs, d’honneur, bienfaiteurs et actifs ; les membres adhérents n’en font pas partie.

## 2. Ancien registre retrouvé

Un registre privé d’adhérents créé en 2018 et modifié pour la dernière fois en 2019 contient **33 entrées**.

Ses catégories opérationnelles — par exemple usager, bénévole ou fonctions de projet — ne correspondent pas directement aux catégories juridiques des statuts 1995.

~~~text
présence dans le registre 2018–2019
≠
qualité de membre votant en 2026
~~~

Les coordonnées et la liste nominative ne sont pas publiées dans le Corpus.

## 3. État du calcul

~~~yaml
voting_members_2026:
  count: UNKNOWN
  quorum_25_percent: NOT_COMPUTABLE_YET
  reason: "absence de registre 2026 qualifié selon les catégories statutaires applicables"
~~~

Le nombre historique de 33 entrées ne doit pas être utilisé automatiquement comme dénominateur. Le nombre de personnes présentes dans un PV récent ne doit pas davantage être assimilé à l’effectif total.

## 3 bis. Traces postérieures retrouvées

### Adhésion 2020

Un email intitulé `Adhésion 2020` a été retrouvé. Il ne s'agit **pas** de l'adhésion d'une personne à C.O.R.S.I.C.A. : il s'agit de **C.O.R.S.I.C.A. adhérant elle-même à Énergie Partagée Association**.

Cette trace confirme une activité institutionnelle en 2020 mais n'ajoute aucun membre au corps votant interne.

### Usage d'AssoConnect

Des traces 2021–2022 montrent que C.O.R.S.I.C.A. disposait d'un compte AssoConnect. Le présent passage n'a cependant retrouvé ni export d'adhérents ni liste de membres issue de cet outil.

~~~text
outil de gestion utilisé
≠
registre de membres retrouvé
~~~

### Déclaration de mars 2026 : « 40 membres actifs »

Le 12 mars 2026, dans le cadre d'une demande extérieure relative à des vélos cargos, le Président écrit qu'« une population de 40 membres actifs de l'association C.O.R.S.I.C.A. va raisonnablement participer » à l'initiative.

Cette phrase constitue une **déclaration contemporaine d'ordre de grandeur**, mais elle ne suffit pas à établir que 40 personnes possèdent juridiquement la qualité de `membre actif` au sens précis de l'article 8 des statuts 1995.

Qualification :

~~~yaml
declared_active_population_2026:
  value: 40
  epistemic_status: REPORTED_BY_ASSOCIATION_PRESIDENT
  context: external_project_participation_estimate
  statutory_membership_equivalence: NOT_ESTABLISHED
  use_as_quorum_denominator: PROHIBITED_WITHOUT_RECONCILIATION
~~~

Elle devient néanmoins une piste importante : un écart éventuel entre un registre statutaire reconstitué et cet ordre de grandeur devra être expliqué.

## 4. Reconstruction requise

Le registre nominatif de travail doit rester privé et, pour chaque personne, déterminer uniquement ce qui est nécessaire : catégorie statutaire, trace d’entrée, éventuelle sortie, droit de vote et source de cette qualification.

Le Corpus public pourra publier l’agrégat :

~~~text
membres votants établis : N
cas probables : M
cas à vérifier : K
quorum conservatoire : Q
~~~

## 5. Principe conservatoire

En cas d’incertitude sur une qualité de membre encore plausible, le cas doit rester explicitement à vérifier. Aucune exclusion du corps votant ne doit être déduite d’un simple silence documentaire.