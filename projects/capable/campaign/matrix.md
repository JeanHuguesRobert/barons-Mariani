---
title: "Campagne du Réel — matrice publique"
subtitle: "Cartographie dynamique des acteurs, demandes, déclencheurs, réponses, silences, recours et niveaux d'effectivité"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: '2026-10-02'
last_modified_at: '2026-10-02'
version: '0.3'
status: "working-note — operational matrix"
language: fr
license: CC BY-SA 4.0
document_role: source
document_kind: operational-matrix
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/capable/campaign/matrix.md
provenance:
  origin_type: conversation-and-corpus-consolidation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: "Capable / Campagne du Réel — conversation du 2026-10-02"
  origin_date: '2026-10-02'
  derived_from:
    - projects/capable/README.md
    - projects/capable/architecture.md
    - projects/capable/campaign/actors.yml
    - research/senatoriales-2026/matrice-reponses-ta-d1-d10-2026-10-02.md
    - research/senatoriales-2026/investigation/sources.md
    - research/second_method.md
    - research/triangulation_du_reel.md
    - research/livre_vivant.md
review:
  status: unreviewed
  reviewed_by: []
related_documents:
  - projects/capable/AGENTS.md
  - projects/capable/contribuer.md
  - projects/capable/site/README.md
  - research/senatoriales-2026/requete-conseil-constitutionnel-projet-v0.4.md
  - research/senatoriales-2026/inventaire_probatoire_exhaustif_pieces_preuves.md
tags:
  - capable
  - campagne-du-reel
  - effectivite
  - contentieux-electoral
  - senat-2026
  - acteurs
  - matrice
  - traces
  - recours
  - qpc
  - cedh
  - living-book
classification_source: cogentia.js
classification_version: '1'
classification_rule: explicit-metadata
classification_confidence: strong
---

# Campagne du Réel — matrice publique

**État consolidé : 2 octobre 2026**

Cette matrice est un instrument de navigation, de vérification et de continuation. Elle ne constitue pas une conclusion sur les responsabilités ni sur la qualification juridique finale des faits.

> **Établir. Relier. Qualifier.**

## 1. Légende probatoire

- **ESTABLISHED** : établi par une trace primaire ou une convergence suffisante ;
- **CONTESTED** : versions incompatibles ou contestation documentée ;
- **UNKNOWN** : information non établie ;
- **NOT_TREATED** : question identifiable mais pas encore traitée ;
- **PENDING** : demande adressée, réponse ou vérification attendue.

Une absence de réponse ne transforme jamais automatiquement `UNKNOWN` ou `PENDING` en `ESTABLISHED`.

## 2. Dimensions de la matrice

| Dimension | Fonction |
|---|---|
| Acteur | Qui détient, décide, transmet, contrôle ou juge ? |
| Sous-acteur / fonction | Quel service, quelle fonction ou quel interlocuteur concret ? |
| Rôle | Détenteur d'information, autorité de décision, transmetteur, contrôleur, juridiction ? |
| Demande | Quelle question factuelle autonome ? |
| Première trace | Quand la question apparaît-elle ? |
| Dernière relance | Quand a-t-elle été réitérée ? |
| Déclencheur | Quel événement justifie une nouvelle sollicitation maintenant ? |
| Ancienneté | Temps écoulé depuis la première trace pertinente |
| Compétence | L'interlocuteur peut-il répondre ou doit-il router ? |
| Routage | A-t-il été demandé, annoncé ou constaté ? |
| Priorité | Aucune hiérarchie ou priorité procédurale explicite ? |
| Réponse observable | Oui / non / partiel / refus / silence / en cours |
| Statut probatoire | ESTABLISHED / CONTESTED / UNKNOWN / NOT_TREATED / PENDING |
| Effet sur capacité | Quelle possibilité pratique est ouverte, réduite ou suspendue ? |
| Précédent personnel | Existe-t-il un épisode analogue documentable en 2017 ou 2024 ? |
| Niveau d'examen obtenu | Instruction contradictoire, irrecevabilité, examen documentaire, examen au fond, etc. |
| Échelon suivant | Quel acteur devient pertinent si la question reste ouverte ? |

## 3. Dimension acteur — état de campagne

| Acteur | État | Fonction dominante |
|---|---|---|
| Préfecture de Haute-Corse | CURRENT | détention de traces, administration électorale, transmission |
| Bureau des élections | CURRENT | interlocuteur opérationnel et détenteur probable de traces |
| Sous-préfecture de Corte | CURRENT | canal territorial potentiel vers le représentant de l'État |
| Tribunal administratif de Bastia | CURRENT | juridiction ayant statué et détenteur du dossier juridictionnel |
| Défenseur des droits — délégation territoriale | CURRENT | autorité indépendante saisie sur l'effectivité des droits |
| Conseil constitutionnel — contentieux électoral | IMMINENT | juge de l'élection et éventuelle autorité d'instruction |
| Conseil d'État — QPC | PROSPECTIVE | filtre QPC dans l'ordre administratif selon la voie procédurale |
| Conseil constitutionnel — QPC | PROSPECTIVE | contrôle de constitutionnalité |
| CADA | CONDITIONAL | accès aux documents selon le régime applicable |
| CNIL | CONDITIONAL | données personnelles et certaines traces techniques |
| CEDH | PROSPECTIVE | contrôle conventionnel après satisfaction des conditions de recevabilité |
| Comité des ministres du Conseil de l'Europe | TERMINAL | exécution éventuelle d'un arrêt CEDH |

Le détail machine-readable est maintenu dans [actors.yml](actors.yml).

## 4. Modes de priorité

### 4.1 Tribunal administratif — `priority_mode: none`

Les demandes D1–D10 restent **autonomes et non hiérarchisées**.

Raison : elles visent à établir exhaustivement l'état du dossier juridictionnel. Donner à certaines une priorité explicite pourrait laisser entendre que les autres sont accessoires.

Principe :

> **TA = exhaustivité horizontale.**

### 4.2 Préfecture — `priority_mode: procedural`

Toutes les demandes restent maintenues, mais leur exécution peut être ordonnée selon leur utilité immédiate pour la saisine du Conseil constitutionnel.

Ordre opérationnel actuel :

1. **Priorité 1 — sécuriser la saisine du CC** : modalités, canal, heure limite effective, récépissé, transmission ;
2. **Priorité 2 — établir la chaîne probatoire centrale** : réception, traitement et transmission de la vidéo ;
3. **Priorité 3 — établir la chronologie décisionnelle préfectorale** : régularisation, constitution et transmission du dossier ;
4. **Priorité 4 — fermer les demandes pendantes et les questions de compétence/routage**.

Principe :

> **Préfecture = exhaustivité maintenue, exécution verticale par urgence procédurale.**

## 5. Déclencheur procédural

Une relance rapprochée n'est pas analysée isolément.

Le modèle est :

`question ancienne + événement procédural nouveau → utilité nouvelle ou urgence nouvelle → relance légitime et traçable`.

Cas canonique :

| Date | Événement |
|---|---|
| 11/09 17:57:55 | transmission de la déclaration vidéo à la préfecture avec demande d'accusé de réception |
| 14/09 12:09 | demande, avant audience, que l'élément soit communiqué au TA s'il manque |
| 15/09 08:42 | première demande structurée de traçabilité réception → transmission → disponibilité |
| 01/10 | le TA indique que la contestation des jugements relève de la saisine du Conseil constitutionnel |
| 02/10 13:33:55 | relance consolidée P1–P18 effectivement envoyée ; source primaire archivée |

Cette chronologie interdit de traiter la relance du 2 octobre comme si elle créait ex nihilo une nouvelle série de questions.

## 6. Front 2026 — entrées transversales initiales

| ID | Acteur | Objet | Première trace | Déclencheur au 02/10 | Priorité | État |
|---|---|---|---|---|---|---|
| CR-001 | Préfecture / Bureau élections | Réception de la déclaration vidéo | 11/09 17:57:55 | Invitation du TA à saisir le CC le 01/10 | P2 | PENDING |
| CR-002 | Préfecture | Versement / transmission de la vidéo au TA | 14/09 12:09 | Même déclencheur | P2 | PENDING |
| CR-003 | Préfecture | Chaîne de traçabilité réception → traitement → transmission | 15/09 08:42 | Même déclencheur | P2 | PENDING |
| CR-004 | TA de Bastia | Pièces effectivement reçues et disponibles avant jugement | 16/09 puis demandes ultérieures | Invitation CC du 01/10 | NONE | PENDING |
| CR-005 | Sous-préfecture de Corte | Modalités et heure limite de remise au représentant de l'État | 28/09 | Dépôt CC devenu imminent | P1 | PENDING |
| CR-006 | Défenseur des droits | Enregistrement / traitement de la saisine sur l'effectivité | 26/09 | Chaîne institutionnelle et recours en cours | P4 | PENDING |
| CR-007 | Conseil constitutionnel — élection | Requête et éventuelles mesures d'instruction | futur dépôt | Voie indiquée par le TA | MAIN EFFORT | NOT_TREATED |
| CR-008 | Préfecture / Bureau élections | Relance consolidée P1–P18 envoyée le 02/10 à 13:33:55 | 02/10 13:33:55 | Invitation du TA à saisir le CC | P1→P4 selon groupe | PENDING |
| CR-009 | Préfecture / Télérecours | Fichier natif, empreintes, PVN, accusés et provenance numérique | 02/10 13:33:55 | Besoin de vérifiabilité des pièces | P3 | PENDING |
| CR-010 | Préfecture / chaîne décisionnelle | Création, finalisation, validation, signature et transmission de la saisine | 02/10 13:33:55 | Stabilisation factuelle avant recours | P3 | PENDING |
| CR-011 | Préfecture / routage | Compétence, délégation et transmission à l'autorité compétente | 02/10 13:33:55 | Réponses partielles et routage demandés | P4 | PENDING |

## 7. Vue campagne : fronts et fonctions

| Front | Fonction | Intensité actuelle |
|---|---|---|
| Conseil constitutionnel | **Effort principal** : préparer et déposer un recours utile et documenté | maximale |
| Préfecture | Alimenter le recours par les faits et traces détenus côté administration électorale | élevée |
| TA de Bastia | Établir l'état du dossier juridictionnel et la disponibilité des pièces | élevée, sans hiérarchie interne |
| Sous-préfecture | Sécuriser la logistique de remise / transmission | élevée jusqu'à fermeture de la question |
| Défenseur des droits | Documenter et, le cas échéant, examiner l'effectivité institutionnelle | secondaire à court terme |
| QPC / Conseil d'État | Préserver et préparer les questions constitutionnelles pertinentes | réserve stratégique |
| CEDH | Préserver les griefs et documenter la profondeur 2017 / 2024 / 2026 | réserve stratégique de long terme |

## 8. Règles de lecture

### R1 — Silence

Une absence de réponse ne prouve pas l'inexistence d'un document, d'une trace ou d'un événement.

### R2 — Déclencheur

Une relance doit être reliée à son déclencheur lorsqu'un événement nouveau modifie l'utilité, l'urgence ou la destination d'une information déjà demandée.

### R3 — Acteur

`détient l'information` ≠ `peut décider` ≠ `peut répondre juridiquement` ≠ `peut transmettre`.

Lorsque l'interlocuteur n'est pas compétent, la matrice enregistre :

- l'autorité compétente identifiée ;
- le routage demandé ;
- le routage effectivement constaté ;
- sa date et sa trace éventuelles.

### R4 — Réponse partielle

Une réponse partielle ferme seulement les dimensions qu'elle établit.

### R5 — Document actuel / disponibilité historique

La présence actuelle d'un document dans un dossier ne prouve pas qu'il était disponible pour le décideur à la date pertinente.

Ces deux questions sont séparées.

### R6 — Répétition et précédents

Les épisodes 2017, 2024 et 2026 peuvent être rapprochés comme **précédents personnels** ou comme éléments de contexte.

La répétition ne suffit pas, à elle seule, à établir une pratique générale ou une violation conventionnelle.

### R7 — Niveau d'examen obtenu

Pour chaque épisode contentieux, la matrice distingue :

- instruction contradictoire ou non ;
- recevabilité ;
- examen des pièces ;
- établissement des faits ;
- examen juridique au fond ;
- mesure d'instruction éventuelle.

## 9. Profondeur 2017 → 2024 → 2026

Cette branche doit rester descriptive tant que les sources primaires n'ont pas été intégrées complètement.

| Année | Instance | Sort procédural | Niveau d'examen factuel | Statut dans la matrice |
|---|---|---|---|---|
| 2017 | Conseil constitutionnel | à documenter précisément par la décision primaire | à documenter précisément | NOT_TREATED |
| 2024 | Conseil constitutionnel | rejet définitif à documenter par la décision primaire | à documenter précisément | NOT_TREATED |
| 2026 | TA puis Conseil constitutionnel | cycle en cours | cycle en cours | PENDING |

## 10. Échelons suivants

La matrice ne doit pas devenir une liste abstraite de recours.

Un acteur prospectif n'est activé que lorsqu'une condition concrète est remplie.

Exemples :

- **Conseil constitutionnel — élection** : voie imminente du contentieux 2026 ;
- **Conseil d'État / QPC** : selon la juridiction et le support procédural permettant de soulever la question ;
- **CEDH** : grief conventionnel défini + voies internes pertinentes épuisées + délai respecté.

## 11. Contribution et falsifiabilité

Le plan de campagne est public.

Toute personne ou institution est invitée à :

- produire une trace manquante ;
- contredire une ligne de la matrice ;
- montrer qu'un acteur n'est pas compétent ;
- identifier une erreur de chronologie ;
- proposer une qualification alternative ;
- proposer un meilleur routage ;
- corriger une source.

Une contradiction sourcée augmente la résolution de la carte.

## 12. Lentille stratégique

Conformément à [`projects/capable/AGENTS.md`](../AGENTS.md), toute étape significative peut faire l'objet d'une lecture séparée :

**Lentille Napoléon — action vraisemblablement évaluée**

Cette lecture stratégique reste distincte :

- des faits ;
- de la qualification juridique ;
- de la décision d'agir.

### État au 2 octobre

L'effort principal est la **préparation du recours au Conseil constitutionnel**.

Les autres fronts sont ordonnés selon leur contribution à cet objectif :

`CC ← Préfecture + TA + sécurisation logistique`

Les QPC, Conseil d'État et CEDH sont des réserves à préparer sans détourner les ressources critiques du point décisif actuel.

## 13. Continuations

- importer D1–D10 sous forme structurée ;
- source primaire : [courriel-tracabilite-prefecture-2026-10-02.md](../../research/senatoriales-2026/investigation/sources/courriel-tracabilite-prefecture-2026-10-02.md) ;
- importer P1–P18 sous forme structurée avec `priority_mode: procedural` ;
- documenter la saisine du Défenseur des droits et son état de réponse ;
- intégrer les décisions primaires de 2017 et 2024 ;
- construire une vue `acteur × demande` ;
- construire une vue chronologique ;
- ajouter un registre machine-readable des demandes ;
- générer JSON/YAML pour `capable.leppe.fr` ;
- soumettre cette matrice à une revue adverse interne puis externe.
