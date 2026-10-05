---
title: "C.O.R.S.I.C.A. — corps électoral préparatoire de l’AGE"
subtitle: "Qui peut voter, et sur quelle base documentaire ?"
description: "Registre préparatoire destiné à reconstruire le corps électoral statutaire avant toute convocation d’une AGE, sans publier les données personnelles du registre d’adhérents."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-05"
last_modified_at: "2026-10-05"
version: "0.1"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/age-electoral-body.md"
document_role: "operational"
document_kind: "governance-register"
document_function: "AGE electoral body reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/statuts-1995-transcription.md"
  - "projects/institut/preparation/statutory-mandate-2025-2026.md"
  - "projects/institut/preparation/ag-age-2025-2026.md"
provenance:
  origin_type: "multi-source-reconstruction"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-05"
  derived_from:
    - "founding statutes scan"
    - "Adhérents CORSICA spreadsheet, 2018-2019"
    - "PV bureau dated 2020-10-15"
    - "retrospective PV AG 2025"
review:
  status: "unreviewed"
  reviewed_by: []
---

# C.O.R.S.I.C.A. — corps électoral préparatoire de l’AGE

## 1. Règle statutaire retrouvée

Sous réserve de confirmation finale que les statuts signés le 25 décembre 1995 sont toujours les statuts applicables, leur article 8 prévoit que l’assemblée générale comprend les membres fondateurs, les membres d’honneur, les membres bienfaiteurs et les membres actifs. Les membres adhérents n’en font pas partie.

L’article 3 précise que les membres d’honneur et bienfaiteurs sont nommés par le conseil d’administration. L’admission comme membre relève également du conseil d’administration.

> **Le simple fait d’apparaître dans un fichier d’adhérents, d’usagers ou de bénévoles ne suffit pas à établir le droit de vote.**

## 2. Registre « Adhérents CORSICA »

Un tableur intitulé « Adhérents CORSICA » existe dans les archives.

~~~text
créé : 3 juillet 2018
dernière modification observée : 10 octobre 2019
environ 33 personnes renseignées dans la plage utilisée
~~~

Le tableur utilise des catégories pratiques telles que Président, secrétaire / ancien secrétaire, chargé de communication, bénévole, usager ou bénévole incubé.

Ces catégories ne constituent pas une table de correspondance fiable vers les catégories statutaires fondateur / membre d’honneur / membre bienfaiteur / membre actif / membre adhérent.

Le tableur est donc une **trace historique de personnes liées à l’activité**, pas un registre électoral actuel.

Les coordonnées personnelles et données bancaires présentes dans cette source privée ne sont pas reproduites dans le Corpus public.

## 3. Jalons ultérieurs

### 15 octobre 2020

Un PV de renouvellement du bureau identifie un président réélu, un trésorier élu et une secrétaire élue.

La version retrouvée dans le dossier bancaire était signalée comme non signée par Société Générale en 2023. Ce PV renseigne le bureau mais ne fournit pas la liste complète des membres de l’assemblée ni leur catégorie statutaire.

### 28 juin 2025

Le PV rétrospectif de l’AG 2025 indique trois personnes présentes et qualifie l’une d’elles de membre active après simplification envisagée du bureau.

Il ne fournit pas une liste exhaustive de tous les membres ayant alors droit de vote.

## 4. État courant

~~~text
liste historique de personnes liées à l’association
→ ESTABLISHED

bureau 2020
→ RECONSTRUCTED / document non signé dans le dossier bancaire retrouvé

participants AG 2025
→ RECONSTRUCTED depuis PV rétrospectif

liste actuelle des membres ayant droit de vote
→ UNKNOWN

nombre servant au quorum de l’AGE
→ UNKNOWN
~~~

Aucun quorum ne doit être calculé avant résolution de cette inconnue.

## 5. Reconstruction nécessaire avant convocation

Pour chaque personne potentiellement électrice, il faut établir : qualité de membre, catégorie statutaire, continuité de cette qualité, droit de vote et règles de pouvoir.

La reconstruction doit privilégier les décisions et PV plutôt que les simples listes de contacts.

## 6. Reality Test

Le futur outillage de gouvernance devra rendre impossible la confusion suivante :

~~~text
liste de contacts
≠ registre des membres
≠ catégories statutaires
≠ corps électoral
~~~

Une future structure machine-readable pourrait conserver séparément :

~~~yaml
person_id: ...
membership:
  status: active
  category: active_member
  admitted_by: ...
  admitted_at: ...
  evidence: ...
governance:
  voting_right: true
  voting_basis: statutes_article_8
~~~

Cette proposition reste préparatoire et ne modifie pas rétroactivement les qualités des personnes.