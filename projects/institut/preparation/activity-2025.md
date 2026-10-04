---
title: "Institut — registre d’activité 2025"
subtitle: "Première reconstruction à partir des traces publiques disponibles"
description: "Registre préparatoire des activités 2025 attribuables au périmètre C.O.R.S.I.C.A. / Institut Mariani, avec séparation entre traces établies, reconstruction et inconnues."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-04"
version: "0.2"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/activity-2025.md"
document_role: "operational"
document_kind: "activity-register"
document_function: "annual activity reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/janus-master.md"
  - "projects/institut/preparation/resources-2025-2026.md"
  - "projects/institut/preparation/ag-age-2025-2026.md"
  - "research/institut_mariani.md"
provenance:
  origin_type: "repository-reconstruction"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-04"
  derived_from:
    - "public GitHub commit history of JeanHuguesRobert/inseme"
    - "research/institut_mariani.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Institut — registre d’activité 2025

## 0. Portée

Ce document est une **première reconstruction** de l’activité 2025. Il ne constitue pas encore le rapport d’activité soumis à l’Assemblée générale.

Le premier passage porte uniquement sur des traces publiques GitHub. Il ne couvre pas encore les courriels, calendriers, factures, démarches administratives, activités physiques, réunions, téléphones, prestations de tiers ni activités non versionnées.

~~~text
absence de commit
≠ absence d’activité

commit présent
→ trace publique durable d’une activité technique ou documentaire
~~~

## 1. Résultat de la remontée GitHub

Un balayage des dépôts publics accessibles du compte JeanHuguesRobert fait apparaître **803 enregistrements de commits datés de 2025 dans 13 dépôts**.

Ce chiffre décrit des traces Git, pas des heures, ni des journées, ni une valeur économique. Un commit peut être minuscule, automatisé, fusionner un travail antérieur ou au contraire condenser beaucoup de travail.

Répartition observée :

| Mois 2025 | Commits observés | Dépôts actifs observés |
|---|---:|---|
| février | 18 | DEnBUG, gabriel, serra, ubikial |
| mars | 93 | DEnBUG, ubikial, Rhuma, Ubiks, Ubik-jean-hugues, Mailai, StructEnv |
| avril | 6 | DEnBUG, Rhuma, Inox |
| mai | 0 | aucun dans le périmètre public balayé |
| juin | 2 | pertitellu |
| juillet | 0 | aucun dans le périmètre public balayé |
| août | 0 | aucun dans le périmètre public balayé |
| septembre | 0 | aucun dans le périmètre public balayé |
| octobre | 75 | StructEnv, pertitellu, survey |
| novembre | 222 | pertitellu, survey |
| décembre | 387 | survey, inseme |

Les dépôts barons-Mariani et cogentia ne présentent pas de commit 2025 dans ce balayage. Leur absence ne signifie pas absence d’activité hors Git.

### 1.1 Périodes qui apparaissent

La reconstruction fait désormais apparaître quatre séquences publiques :

~~~text
février–avril
→ vague R&D IA / interfaces / outils / configuration

juin
→ amorce Pertitellu

octobre–novembre
→ forte reprise civique et Survey / Pertitellu

décembre
→ très forte activité Survey, premiers noyaux COP, puis Inseme
~~~

### 1.2 Attribution institutionnelle : ne pas rétroprojeter

Plusieurs dépôts portent aujourd’hui un frontmatter ou une documentation les reliant à l’Institut Mariani / C.O.R.S.I.C.A. Cette qualification actuelle ne suffit pas à prouver qu’en 2025 chaque commit constituait juridiquement ou comptablement une activité de l’association.

Par exemple :

- le README actuel de Survey porte l’affiliation Institut Mariani / C.O.R.S.I.C.A. et conserve un changelog 2025 ;
- le README actuel de Serra porte également cette affiliation ;
- mais leurs états initiaux de 2025 ne suffisent pas, à eux seuls, à démontrer un mandat associatif contemporain ;
- Pertitellu est explicitement un projet politique/citoyen : il ne doit pas être imputé à C.O.R.S.I.C.A. sans base institutionnelle spécifique.

On distingue donc :

~~~text
TRACE TECHNIQUE ÉTABLIE
→ le travail public existe

CONTINUITÉ R&D RECONSTRUITE
→ le projet peut éclairer la généalogie de l’Institut

ATTRIBUTION ASSOCIATIVE
→ à vérifier séparément

DÉPENSE / RESSOURCE ASSOCIATIVE
→ exige une trace comptable ou institutionnelle propre
~~~

## 2. Traces établies

| Date UTC | Dépôt | Trace | Action / output observable | Catégorie | Temps | Statut |
|---|---|---|---|---|---|---|
| 2025-12-23 | inseme | a3b42c43 | v2 | développement / consolidation | UNKNOWN | ESTABLISHED |
| 2025-12-23 | inseme | eadabc77 | sauvegarde de code | conservation / continuité | UNKNOWN | ESTABLISHED |
| 2025-12-24 | inseme | 1cdac1cc | fusion de Survey dans apps/platform | plateforme / consultation | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | 5ce535d3 | déploiement du système de chat Inseme et mise à jour de Survey | plateforme / interaction | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | 0b7a9f87 | débogage du nouveau projet Netlify inseme | déploiement | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | 3e703332 | passage à Node 24 | build / infrastructure | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | 642567aa | imposition de Node 24 | build / infrastructure | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | 5d0724b9 | ajout d’un badge de build | qualité / visibilité | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | 92925a3b | configuration Node 24 à la racine pour Netlify | déploiement | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | f2d45ff5 | restauration de fonctions Edge tronquées et correction des imports | correction / infrastructure | UNKNOWN | ESTABLISHED |
| 2025-12-25 | inseme | fd7f7e1d | validation locale puis vérification prévue sur Netlify | test / déploiement | UNKNOWN | ESTABLISHED |
| 2025-12-26 | inseme | d76d90e5 | sauvegarde | conservation / continuité | UNKNOWN | ESTABLISHED |
| 2025-12-28 | inseme | 6428fb78 | sauvegarde | conservation / continuité | UNKNOWN | ESTABLISHED |

## 3. Remontée par projets

| Période | Dépôt | Commits 2025 observés | Objet observable | Lien au futur écosystème Institut | Attribution C.O.R.S.I.C.A. 2025 |
|---|---|---:|---|---|---|
| fév.–avr. | DEnBUG | 5 | bibliothèque de trace/debug hiérarchique | traçabilité technique | UNKNOWN |
| fév. | gabriel | 4 | assistant personnel IA / esprit critique | agents personnels, médiation IA | UNKNOWN |
| fév. | serra | 6 | interfaces et dashboards pilotés par IA ; continuation async | interfaces adaptatives, continuations | UNKNOWN |
| fév.–mars | ubikial | 13 | gestion de personas et cross-posting | future infrastructure de dérivation/publication | UNKNOWN |
| mars–avr. | Rhuma | 37 | simulation, PVGIS, états, Kudos, exports | simulation énergétique / monnaie / données | UNKNOWN |
| mars | Ubiks | 3 | adaptation de contenus multi-plateformes | personas / publication dérivée | UNKNOWN |
| mars | Ubik-jean-hugues | 2 | persona publique | identité/perspective | UNKNOWN |
| mars | Mailai | 13 | assistant mail, multi-provider IA, MCP, Node-RED | agents, MCP, automatisation | UNKNOWN |
| mars–oct. | StructEnv | 34 | format de configuration structuré ; expérimentation génération IA | configuration, spécifications explicites, agentic coding | UNKNOWN |
| avr. | Inox | 1 | système de classes, intégration Serra | expérimentation logicielle | UNKNOWN |
| juin–nov. | pertitellu | 24 | projet citoyen pour Corte, wiki et ressources | démocratie locale / consultation | **NE PAS IMPUTER** sans mandat spécifique |
| oct.–déc. | survey | 648 | consultation citoyenne, wiki, IA, Kudocracy, COP naissant | très forte continuité vers Inseme/COP | TO VERIFY |
| déc. | inseme | 13 | plateforme, Survey intégré, chat, Netlify, Edge | continuité directe vers plateforme 2026 | TO VERIFY |

Le statut `TO VERIFY` signifie : continuité technique forte, mais attribution associative 2025 non encore établie par une pièce contemporaine suffisante.

## 4. Survey : principal foyer public retrouvé

Survey démarre publiquement le **20 octobre 2025** et totalise **648 commits observés jusqu’au 21 décembre 2025**.

Les commits montrent notamment :

- consultation citoyenne et wiki ;
- assistant IA ;
- pages et actes municipaux ;
- cartographie/Géoportail ;
- gestion de configuration et vault ;
- recherche web ;
- amélioration de la traçabilité/audit ;
- travaux MCP ;
- premiers agents fondés sur COP ;
- premier réseau COP ;
- premier kernel COP côté serveur ;
- CLI de test ;
- schémas SQL ;
- migration progressive vers une architecture plus structurée.

Le README actuel conserve par ailleurs un changelog détaillé à partir de novembre 2025 et présente Survey comme « Consultation Citoyenne Petit Parti / Pertitellu », désormais reliée au dépôt parent Inseme.

Épistémiquement :

~~~text
existence et activité Survey 2025
→ ESTABLISHED

continuité Survey → Inseme / COP
→ RECONSTRUCTED avec forte convergence des traces

portage formel par C.O.R.S.I.C.A. en 2025
→ UNKNOWN / TO VERIFY
~~~

## 5. Premiers enseignements sur 2025

La représentation initiale « activité surtout fin décembre » est falsifiée par la remontée.

La meilleure reconstruction provisoire est maintenant :

~~~text
février–avril
R&D ouverte dispersée
→ assistants IA
→ interfaces adaptatives
→ simulation
→ personas
→ publication multi-plateformes
→ configuration / MCP

juin–novembre
expérimentation civique
→ Pertitellu

octobre–décembre
accélération Survey
→ consultation
→ wiki
→ IA
→ audit
→ MCP
→ COP

fin décembre
convergence vers Inseme
~~~

Cela fournit une hypothèse de continuité technologique très plausible vers l’Institut 2026, mais pas encore une identité institutionnelle rétroactive.

## 6. Premier regroupement capacitaire

Les traces permettent au minimum de documenter quatre capacités travaillées fin 2025 : plateforme de consultation, interaction conversationnelle, infrastructure de déploiement et continuité technique.

Cette classification reste une projection analytique : les commits sont établis ; leur regroupement en capacités est RECONSTRUCTED.

## 7. Ce qui reste inconnu

À ce stade, le registre ne permet pas encore de répondre de façon fiable à l’activité de janvier à novembre 2025, au temps bénévole total, aux dépenses ou recettes associées, aux ressources cloud ou compute consommées, aux réunions et actes de gouvernance, aux démarches extérieures, aux outputs non GitHub ni au lien institutionnel exact de chaque tâche.

Ces inconnues doivent être résolues par rapprochement avec d’autres traces, sans extrapoler depuis les 13 commits connus.

## 8. Prochain enrichissement

~~~text
GitHub autres dépôts / historiques plus anciens
→ Corpus 2025
→ Gmail institutionnel
→ calendrier
→ factures / banques / fournisseurs
→ déclarations humaines
→ consolidation et estimation bornée
~~~

Pour les heures : HOURS_CONFIRMED / HOURS_RECONSTRUCTED / HOURS_UNKNOWN.

Aucune estimation horaire n’est introduite dans cette v0.1.