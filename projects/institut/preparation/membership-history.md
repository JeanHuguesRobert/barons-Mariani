---
title: "C.O.R.S.I.C.A. — histoire des membres actifs et des usagers"
subtitle: "Méthode de reconstruction d’une population ouverte et de son noyau actif"
description: "Registre préparatoire distinguant usagers, membres actifs, responsables et périodes d’activité, sans prétendre reconstituer exhaustivement tous les usagers historiques."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-05"
last_modified_at: "2026-10-05"
version: "0.1"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/membership-history.md"
document_role: "operational"
document_kind: "historical-membership-register"
document_function: "membership and activity history reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/governance-membership-baseline.md"
  - "projects/institut/preparation/membership-quorum-2026.md"
  - "projects/institut/preparation/age-electoral-body.md"
provenance:
  origin_type: "multi-source-reconstruction"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-05"
  derived_from:
    - "Adhérents CORSICA spreadsheet 2018–2019"
    - "governance records and correspondence"
    - "president contemporary declaration 2026-10-05"
review:
  status: "unreviewed"
  reviewed_by: []
---

# C.O.R.S.I.C.A. — histoire des membres actifs et des usagers

## 1. Principe

L’association a longtemps fonctionné avec une population ouverte d’usagers, bénévoles, participants, locataires, personnes incubées ou engagées ponctuellement.

Il serait artificiel de prétendre reconstituer une liste exhaustive continue de tous les membres / usagers.

La question historique utile est :

> **Qui a été actif, à quel moment, dans quelle capacité, et sur quelle trace ?**

## 2. Pratique ancienne

Le registre opérationnel 2018–2019 distingue déjà des usagers, bénévoles, responsables, personnes incubées et fonctions de projet.

Une trace de 2019 emploie explicitement la distinction entre membres actifs qui votent et membres inactifs qui ne votent pas.

Cette pratique précède la refonte 2026.

## 3. État courant déclaré

Au 5 octobre 2026 :

~~~text
noyau actif continu
→ Jean Hugues Noël Robert — Président
→ Maguy Ghionga — Trésorière

usagers actifs épisodiquement
→ existent
→ nombre et identité variables

population totale d’usagers / membres
→ inconnue
→ non nécessairement exhaustivable
~~~

La charge opérationnelle de la Trésorière est décrite par le Président comme largement réduite depuis le blocage du compte Société Générale.

Cela illustre :

~~~text
fonction institutionnelle
≠ volume apparent d’activité
≠ capacité opérationnelle disponible
~~~

## 4. Reconstruction par épisodes

Le futur registre privé doit préférer des intervalles :

| Personne / identifiant | Période | Relation | Activité | Fonction | Source | Confiance |
|---|---|---|---|---|---|---|
| JHNR | 1995–2026 | fondateur / actif | continue | Président | statuts + actes | strong |
| MG | périodes à préciser ; continuité actuelle déclarée | active | continue actuellement | Trésorière actuelle déclarée | déclaration 2026 + traces historiques | medium |
| autres | à reconstruire | usager / bénévole / actif ponctuel / responsable | épisodique ou continue | éventuelle | traces | variable |

## 5. Cas particuliers

### Usagers / locataires

Une personne ayant utilisé un logement, un jardin, une activité, un service ou un équipement peut appartenir à l’histoire de l’association comme usager sans devenir pour autant membre actif ou participant à la gouvernance.

### Bénévoles

Le bénévolat est un indice d’activité, mais sa durée, son intensité et sa continuité doivent être datées.

### Responsables

Une fonction de Président, Trésorier, Secrétaire ou autre responsabilité est une trace forte d’activité, mais il faut distinguer :

~~~text
fonction pratiquée
≠ fonction votée
≠ fonction déclarée
≠ fonction encore en cours
≠ capacité effective d’exercice
~~~

## 6. Modèle minimal

~~~yaml
relationship_episode:
  person_ref: private-or-public-id
  start: YYYY-MM-DD | YYYY | UNKNOWN
  end: YYYY-MM-DD | YYYY | OPEN | UNKNOWN
  relation:
    - user
    - member
    - active_member
    - volunteer
    - tenant
    - beneficiary
    - officer
  activity_level:
    - continuous
    - episodic
    - historical
    - unknown
  office:
    role: president | treasurer | secretary | other | null
    operational_capacity: full | reduced | blocked | unknown
  evidence: [...]
  confidence: strong | medium | weak
~~~

## 7. Objectif

Le Livre Vivant Institut n’a pas besoin d’une fausse liste exhaustive de personnes.

Il a besoin d’une histoire honnête des capacités humaines réellement mobilisées :

~~~text
qui était là ?
pour quoi faire ?
pendant combien de temps ?
avec quelle responsabilité ?
avec quelle capacité effective ?
sur quelle preuve ?
~~~
