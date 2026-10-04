---
title: "Institut — registre d’activité 2025"
subtitle: "Première reconstruction à partir des traces publiques disponibles"
description: "Registre préparatoire des activités 2025 attribuables au périmètre C.O.R.S.I.C.A. / Institut Mariani, avec séparation entre traces établies, reconstruction et inconnues."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-04"
version: "0.5"
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

## 7. Traces institutionnelles directes retrouvées dans Gmail / Agenda

La couche privée de reconstruction apporte désormais des traces qui attribuent explicitement certaines activités à C.O.R.S.I.C.A. ou au canal Institut. Les détails personnels, coordonnées et pièces privées ne sont pas reproduits ici.

| Date | Trace reconstruite | Qualification | Statut épistémique | Statut institutionnel |
|---|---|---|---|---|
| 2025-06-28 | événement Agenda « AG C.O.R.S.I.C.A. », 15h–16h à Corte, notifié par email la veille ; PV rétrospectif retrouvé dans Drive | AG fortement reconstruite | RECONSTRUCTED | occurrence et décisions décrites par PV rédigé le 27 avril 2026 ; signatures contemporaines non établies |
| juin–juil. 2025 | contrat d’assurance multirisque de l’association et avenant à signer ; tentative de signature du Président | administration associative | ESTABLISHED | EFFECTIVE pour l’existence du contrat ; avenant à qualifier |
| 2025-07-02 | démarche auprès de l’aviation civile pour un projet expérimental de démonstration VTOL à Corte, explicitement portée comme Président de C.O.R.S.I.C.A. | mobilité verte / innovation | ESTABLISHED | démarche externe effectuée |
| 2025-09-18 | courrier à EDF SEI Corse au nom de C.O.R.S.I.C.A. sur un projet d’autoconsommation collective photovoltaïque pilotée de 1 MWc à Corte, avec future SCIC « Vin Solaire Mariani » | énergie / autoconsommation / flexibilité | ESTABLISHED | démarche externe effectuée ; projet non réalisé à ce stade |
| 2025-10-13 | confirmation de dépôt à une Call for Ideas META-DEST reçue sur le canal Institut Mariani | candidature / innovation territoriale | ESTABLISHED pour le dépôt | contenu et portage exact à vérifier |
| 2025-10-18 | échange Web Summit : présentation d’une organisation à faible budget développant deux projets à fort impact — monnaie incitative et solution scalable pour green AI data centers | candidature / financement / mise en réseau | ESTABLISHED | rattachement juridique exact à C.O.R.S.I.C.A. à vérifier |
| 2025-10-21 | demande de conseils et partenaires ONG pour un projet Corse–Cuba : container, distillation pilotée, solaire, transfert de savoir-faire et commerce éthique, signée Président de C.O.R.S.I.C.A. | coopération / énergie / transmission | ESTABLISHED | démarche externe effectuée |

### 7.1 AG du 28 juin 2025

Trois couches de preuve sont désormais distinguées.

**Trace contemporaine :**
- événement Agenda « AG C.O.R.S.I.C.A. » le **28 juin 2025 de 15h à 16h à Corte** ;
- notification Gmail correspondante le 27 juin 2025.

**Trace rétrospective :**
- Google Doc intitulé « PV AG 2025 » ;
- contenu : Assemblée Générale Ordinaire du 28 juin 2025 à 15h à Corte ;
- participants indiqués : Jean Hugues Noël Robert, Yvon Ambrosi, Maguy Ghionga ;
- ordre du jour : rapport moral, rapport financier, réorganisation du bureau / mise à jour statutaire, poursuite des projets ;
- résolutions décrites comme adoptées à l’unanimité ;
- poursuite du Fonds Barons Mariani et du Mariani Motion Lab ;
- principe d’un bureau simplifié Président / Trésorier et mandat au Président pour préparer la modification statutaire.

**Temporalité du PV :**
- la liste de révisions Drive montre une création le **27 avril 2026** ;
- première révision vide à 15:34:36 UTC ;
- contenu complet ajouté à 15:35:01 UTC ;
- le document est donc un **PV rédigé rétrospectivement**, environ dix mois après la date de l’Assemblée ;
- aucun scan signé contemporain n’a été retrouvé lors de cette recherche.

Qualification prudente :

~~~text
AG programmée le 28/06/2025
→ ESTABLISHED par traces contemporaines

AG effectivement tenue
→ RECONSTRUCTED avec soutien fort
   (trace contemporaine + PV rétrospectif détaillé)

contenu des décisions
→ RECONSTRUCTED à partir du PV rétrospectif

PV contemporain signé
→ NOT FOUND / UNKNOWN
~~~

Le PV rétrospectif indique que « l’exercice écoulé » avait été volontairement calme et mentionne notamment Minesteggio, le Fonds Barons Mariani, le Mariani Motion Lab, un véhicule donné à l’association pour mobilité décarbonée, une trésorerie supérieure à 15 000 € à la Société Générale, ainsi que des dépenses principalement limitées à l’assurance MAIF et aux frais de compte.

Ces éléments doivent être recoupés avant usage comptable ou juridique définitif.

### 7.2 Une chronologie associative plus dense à partir de juin

Les traces directes modifient la reconstruction provisoire :

~~~text
janvier–mai
→ canal institutionnel actif, assurances / réseaux / newsletters reçues
→ peu d’actes sortants explicitement attribuables retrouvés au premier passage

juin
→ AG programmée
→ administration assurance

juillet
→ projet VTOL / mobilité verte

septembre
→ projet photovoltaïque ACC 1 MWc / flexibilité

octobre
→ META-DEST
→ Web Summit
→ Corse–Cuba
→ puis accélération Survey / Pertitellu dans l’écosystème technique et civique
~~~

L’absence d’acte sortant retrouvé entre janvier et mai n’est pas une preuve d’absence d’activité ; c’est seulement l’état de cette recherche ciblée.

### 7.3 Distinction désormais utile

Le registre 2025 peut maintenant séparer trois niveaux :

~~~text
A. ACTIVITÉ ASSOCIATIVE DIRECTEMENT ATTRIBUÉE
→ signature / canal / qualité Président C.O.R.S.I.C.A.

B. ACTIVITÉ INSTITUT / R&D À RATTACHEMENT À QUALIFIER
→ canal Institut, candidature, projet technique

C. ÉCOSYSTÈME PERSONNEL / POLITIQUE / OPEN SOURCE
→ continuité intellectuelle possible
→ ne pas intégrer comptablement sans mandat ou trace supplémentaire
~~~

Cette distinction devra guider le futur rapport d’activité et éviter de gonfler artificiellement le périmètre de l’association.



### 7.4 Décembre 2025 — souscription publique « Pascal Paoli »

Une trace publique indépendante, hors GitHub, documente une activité directement portée par C.O.R.S.I.C.A. en décembre 2025.

La page HelloAsso « Pascal Paoli » présente C.O.R.S.I.C.A. comme **porteur opérationnel** d'une souscription citoyenne destinée à tenter de conserver en Corse un portrait de Pasquale Paoli mis en vente à Bastia le 13 décembre 2025.

La page décrit notamment :

- objectif patrimonial : éviter la sortie de Corse de l'œuvre et organiser son accès public ;
- portage de la collecte par C.O.R.S.I.C.A. ;
- rôle R&D / communication attribué à l'Institut Mariani ;
- projet de reversement à une future structure patrimoniale en cas de succès ;
- engagement de transparence sur prix, frais, assurance, transport et emploi des fonds ;
- objectif affiché de collecte : 1 000 000 € ;
- résultat public actuellement affiché : **0 € collecté / 0 contributeur**.

Source publique :
`https://www.helloasso.com/associations/corse-organisant-la-reunion-sur-internet-de-competences-autonomes/collectes/pascal-paoli`

Qualification :

~~~text
existence de la campagne
→ ESTABLISHED

portage public par C.O.R.S.I.C.A.
→ ESTABLISHED

succès financier
→ FALSE selon état public de la page

flux financier collecté
→ 0 € affiché publiquement

travail bénévole consacré à la campagne
→ UNKNOWN / à reconstruire
~~~

Cet élément doit figurer dans le rapport d'activité même en l'absence de recette : une tentative documentée et infructueuse reste une activité et un Reality Test.

## 7. Ce qui reste inconnu

À ce stade, le registre ne permet pas encore de répondre de façon fiable à l’activité de janvier à novembre 2025, au temps bénévole total, aux dépenses ou recettes associées, aux ressources cloud ou compute consommées, aux réunions et actes de gouvernance, aux démarches extérieures, aux outputs non GitHub ni au lien institutionnel exact de chaque tâche.

Ces inconnues doivent être résolues par rapprochement avec d’autres traces, sans extrapoler depuis les 13 commits connus.

## 9. Prochain enrichissement

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