---
title: "PrivAI n°1 — Chapitre 9 : Democratic Humans in the Loop"
subtitle: "L'humain doit garder une capacité réelle, pas une présence cérémonielle"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/manuscript/n1/09-democratic-humans-in-the-loop.md"
document_role: "source"
document_kind: "manuscript-chapter"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
- "Antigravity (Gemini 3.8 Flash High) — drafting assistance, 2026-10-04, 2026-10-05"
provenance:
  origin_type: "corpus-derivation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "research/democratic_ai_safety.md"
  origin_date: "2026-05-11"
  derived_from:
    - "barons-Mariani/projects/privai/doctrine/anti-demos.md"
    - "barons-Mariani/research/personne_numerique_mandatee.md"
    - "barons-Mariani/projects/privai/annexes/precedents-juridiques-inventeur-humain.md"
    - "barons-Mariani/projects/privai/magazine/2026-10-04-illusion-electeur-synthetique.md"
---

# Chapitre 9 : Democratic Humans in the Loop

## 1. L'imposture du « Human-in-the-Loop » cérémoniel

Dans les textes réglementaires contemporains, notamment l'article 14 du règlement européen sur l'intelligence artificielle (*AI Act*), la notion de « contrôle humain » (*human oversight* ou *Human-in-the-Loop* - HITL) est omniprésente. Elle est présentée comme le remède universel contre les dérives des systèmes à haut risque : un opérateur humain doit être placé dans la boucle pour valider, corriger ou suspendre la décision algorithmique.

Sur le terrain sociologique et économique réel, ce dispositif s'est mué en une **pure fiction de défausse juridique**.

Considérons la situation d'un travailleur de plateforme, d'un modérateur de contenus sous-traité dans un pays à bas salaires, ou d'un gestionnaire d'allocations sommé de traiter soixante dossiers par heure :
- l'opérateur dispose de quelques secondes pour valider des recommandations générées par un modèle complexe de plusieurs milliards de paramètres ;
- contester la suggestion de l'algorithme exige de rédiger un rapport justificatif chronophage qui dégrade ses indicateurs de performance managériale (*KPIs*) ;
- en pratique, le travailleur valide mécaniquement plus de 98 % des décisions automatiques en raison du **biais d'automatisation** (*automation bias*).

Cet humain n'est pas un contrôleur : c'est un **fusible juridique**. Sa présence minimale sert uniquement à la personne morale pour affirmer devant le juge qu'il n'y a pas eu de décision entièrement automatisée, et pour faire porter la responsabilité d'une bavure sur un employé précaire plutôt que sur les concepteurs du système.

---

## 2. La doctrine DHITL : de l'opérateur asservi au citoyen délibérant

Face à cette mystification managériale, PrivAI formalise l'impératif politique **DHITL** (*Democratic Humans in the Loop*), posé par le document source *Democratic AI Safety* (§11) et l'axiome **C7** :

> **Doctrine C7 :** Le contrôle humain d'un système d'IA ayant un impact démocratique, juridique ou institutionnel est insuffisant s'il est confié à un opérateur économiquement subordonné. La sécurité démocratique exige des humains délibérants, indépendants et collectivement responsables au sein de la boucle de décision.

DHITL redéfinit radicalement les conditions de validité du contrôle humain :

1. **L'indépendance statutaire du contrôleur :** Le citoyen ou le collège d'experts examinant une décision algorithmique ne doit pas être soumis à un lien de subordination hiérarchique ni à une pression de rentabilité financière de la part de l'entité gestionnaire.
2. **Le temps de délibération garanti :** Nul examen humain n'est opposable s'il n'accorde pas le temps matériel nécessaire à l'analyse contradictoire des pièces et à la vérification des données sources.
3. **L'outillage contradictoire autonome :** Les contrôleurs démocratiques doivent disposer de leurs propres outils d'inférence, de leurs modèles indépendants et de leurs contre-simulations pour auditer la proposition sans dépendre de l'interface fournie par le promoteur du modèle.
4. **Le pouvoir effectif de veto et de suspension :** En cas de doute légitime sur l'impartialité ou la régularité d'un traitement, l'organe démocratique doit pouvoir geler immédiatement le déploiement du système sans risquer de sanctions économiques.

---

## 3. La gouvernance démocratique de l'infrastructure

L'extension politique de DHITL concerne l'échelon le plus fondamental : la gouvernance des infrastructures de calcul et des ensembles de données d'apprentissage.

On ne peut pas prétendre préserver la souveraineté démocratique si les modèles d'intelligence artificielle utilisés par les ministères, les tribunaux, les hôpitaux et les universités d'une nation sont hébergés sur des nuages informatiques extraterritoriaux soumis aux lois d'extraterritorialité de puissances étrangères (comme le *Cloud Act* américain).

Un système d'IA véritablement aligné sur la démocratie exige que le peuple souverain, par l'entremise d'institutions indépendantes et de biens communs certifiés :
- contrôle la chaîne logistique du calcul (*compute*) ;
- puisse auditer les pondérations mathématiques des modèles de référence ;
- participe à la qualification contradictoire des corpus servant à l'entraînement public.

Sans DHITL, le gouvernement par les algorithmes réalise le vieux rêve de la technocratie autoritaire : une administration des choses sans citoyens, où l'humain n'est plus qu'un spectateur impuissant de sa propre dépossession.

---

## 4. Les quatre séparations architecturales de DHITL

Pour traduire cette exigence politique en architecture logicielle concrète, la doctrine PrivAI (*La personne numérique mandatée*, §8) impose **quatre séparations étanches** au sein de tout flux institutionnel :

1. **Séparation Proposition / Décision :** Un agent ou un modèle peut analyser, synthétiser, recommander ou classer des options ; il ne transforme jamais de lui-même une proposition en décision exécutoire. La décision demeure un acte de volonté humaine souveraine.
2. **Séparation Autorisation / Exécution :** Une action validée peut être exécutée à la vitesse de la machine (déclenchement de paiements, mise à jour d'un registre), mais le jeton d'autorisation qui a déclenché l'exécution doit être signé cryptographiquement par une clé humaine nominative et auditable.
3. **Séparation Exécution / Responsabilité :** Un algorithme d'optimisation peut accomplir la tâche technique sans jamais devenir le répondant légal. En cas de dommage, l'institution ne peut se réfugier derrière l'outil : la responsabilité remonte sans atténuation vers l'ordonnateur humain.
4. **Séparation Traçabilité des actes / Surveillance des personnes :** DHITL exige la traçabilité absolue des actes de puissance publique et des décisions corporatives engageantes, tout en interdisant le flicage biométrique et cognitif permanent des administrés et des travailleurs. On trace le pouvoir, on sanctuarise le citoyen.

---

## 5. L'argument de symétrie DABUS : posséder contre gouverner

La nécessité d'exclure les machines du pouvoir décisionnel souverain trouve son ancrage le plus solide dans un précédent juridique international majeur : la jurisprudence **DABUS** (*Device for the Autonomous Bootstrapping of Unified Sentience*).

Entre 2020 et 2024, le promoteur de ce système a tenté de faire enregistrer des brevets d'invention désignant l'algorithme lui-même comme inventeur officiel. La Cour suprême du Royaume-Uni (*Thaler v Comptroller-General of Patents [2023] UKSC 49*), l'Office européen des brevets (OEB) et les tribunaux fédéraux américains ont unanimement rejeté cette prétention : une invention brevetable exige un inventeur humain, seul titulaire possible de droits et devoirs patrimoniaux.

PrivAI dérive de ce précédent un **axiome de symétrie constitutionnelle fondamental** :

> **Axiome de symétrie de l'autorité :** Si une machine ne peut pas être déclarée inventeur pour détenir un monopole de propriété privée, elle ne peut à aucun titre être déclarée autorité pour exercer une prérogative de puissance publique ou gouverner des humains.

Ce que le capitalisme refuse à l'IA pour préserver l'ordre patrimonial des entreprises, la République doit *a fortiori* le refuser à l'IA pour préserver l'ordre démocratique des citoyens.

---

## 6. L'illusion de l'électeur synthétique et la sanctuarisation du Demos

La forme la plus insidieuse de subversion démocratique ne vient pas d'une rébellion brutale des robots, mais de ce que le magazine PrivAI dénonce sous le titre de *« L'illusion de l'électeur synthétique »* :

Sous prétexte de fluidifier la démocratie participative ou de mesurer « l'opinion publique », des cabinets de conseil et des gouvernements technocratiques déploient déjà des grappes d'agents conversationnels calibrés pour simuler des panels sociologiques de citoyens (*synthetic personas*). Ces agents sont interrogés pour valider des projets de loi, tester des discours électoraux ou justifier des réformes régressives en affirmant que *« 87 % des citoyens synthétiques consultés approuvent cette mesure »*.

Cette dérive constitue un véritable coup d'État cybernétique contre le *demos* :
- Elle remplace le peuple réel, contradictoire, souffrant et vivant, par un simulacre mathématique aligné sur les préjugés statistiques de ses concepteurs ;
- Elle permet aux détenteurs de supercalculateurs de fabriquer un consentement artificiel sur mesure à des coûts marginaux nuls ;
- Elle détruit l'essence même du suffrage universel, qui repose sur l'égalité stricte : un être humain vivant, une voix.

Le principe Anti-Demos est sans appel : **le corps électoral est une communauté biologique et morale inviolable.** Tout sondage, toute consultation et tout arbitrage politique fondé sur des entités synthétiques doit être frappé d'illégalité républicaine absolue.
