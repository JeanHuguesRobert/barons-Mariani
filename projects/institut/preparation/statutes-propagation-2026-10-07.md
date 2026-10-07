---
title: "C.O.R.S.I.C.A. — propagation du référentiel statutaire au Corpus"
subtitle: "Effets transversaux de la vérification des statuts 1995"
description: "Note de propagation recensant les corrections rendues nécessaires par la transcription et la vérification des statuts fondateurs de C.O.R.S.I.C.A."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-07"
last_modified_at: "2026-10-07"
version: "0.1"
status: "working-paper — propagation log"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/statutes-propagation-2026-10-07.md"
document_role: "operational"
document_kind: "propagation-log"
document_function: "cross-corpus consistency update"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/current-statutes-baseline.md"
  - "projects/institut/sources/statuts-corsica-1995-transcription.md"
  - "projects/privai/institutional-status.md"
  - "projects/institut/preparation/n1-architecture.md"
provenance:
  origin_type: "cross-corpus-propagation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-07"
  derived_from:
    - "verified 1995 statutes transcription"
    - "current statutes baseline v0.7"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Propagation du référentiel statutaire au Corpus

## 1. Référentiel désormais démontré

Le scan signé des statuts fondateurs a été transcrit et vérifié visuellement. La chaîne documentaire 1995–1996, 2018, 2023 et 2024 conduit au référentiel prudent suivant :

> Les statuts signés à Corte le 25 décembre 1995 constituent la baseline statutaire opératoire actuellement démontrée pour préparer l'assemblée 2026.

Le projet 2018 reste préparatoire. La refonte 2025–2026 reste inachevée.

## 2. Effets propagés

### Institut

- l'architecture du n°1 distingue désormais explicitement l'AG du 28 juin 2025 de l'AG 2026 relative à l'exercice 2025 ;
- les travaux AG/AGE doivent partir des règles 1995 tant qu'aucune version postérieure adoptée et déclarée n'est établie ;
- le siège statutaire est « Corte, Corse » ; 1 cours Paoli est une adresse publique d'usage à traiter séparément de la donnée administrative.

### PrivAI

Des formulations antérieures indiquaient que les statuts de C.O.R.S.I.C.A. n'avaient pas encore été lus. Elles sont devenues obsolètes.

La correction de fond est plus importante :

~~~text
mission fonctionnelle 2026 de l'Institut
→ peut inclure la préfiguration institutionnelle

statuts 1995
→ ne confèrent pas expressément
   un pouvoir de portage juridique de PrivAI Foundation
~~~

Donc :

> la préfiguration institutionnelle de PrivAI dans le périmètre de l'Institut ne vaut pas, à elle seule, portage juridique par C.O.R.S.I.C.A.

Tout portage juridique futur doit être établi séparément par le texte statutaire applicable, une décision de l'organe compétent et son effectivité.

## 3. Surfaces dérivées

Les sources Markdown ont été corrigées en priorité.

Les fichiers HTML de site et de projection qui contiennent encore la phrase « les statuts n'ont pas été relus » sont considérés comme **dérivés à régénérer**, et non comme sources à corriger manuellement.

Invariant :

~~~text
source corrigée
→ régénération dérivée

pas
→ patch manuel silencieux du HTML
~~~

## 4. Leçon FractaCognitive

Cette propagation confirme une règle déjà apparue pendant RT-LBF-001 :

~~~text
nouvelle preuve primaire
→ mise à jour de la baseline
→ recherche des assertions dépendantes
→ correction des sources
→ invalidation / régénération des projections
~~~

La propagation n'est donc pas une simple recherche-remplacement. Elle suit les dépendances sémantiques de l'assertion modifiée.

Candidat métacognitif :

> **Une correction de source doit propager son changement de portée, pas seulement ses mots.**

Ce candidat doit encore être testé sur d'autres corrections transversales avant toute promotion comme principe général.
