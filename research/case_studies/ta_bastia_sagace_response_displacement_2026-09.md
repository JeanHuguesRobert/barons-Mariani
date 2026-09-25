---
title: "TA Bastia / Sagace — déplacement non résolutif de la réponse"
subtitle: "Reality Case — demande de précisions matérielles, réponse du greffe et consultation de Sagace"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-09-25"
version: "1.1"
status: "reality case — active"
language: "fr"
license: "CC BY-SA 4.0"
visibility: "public"
document_role: "case-study"
document_kind: "reality-evidence"
lifecycle_state: "active"
related_documents:
  - "../senatoriales-2026/dossier-ta-bastia-2026-09-14.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/non_resolutive_response_patterns.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/skills/response-resolution-check/SKILL.md"
---

# TA Bastia / Sagace — déplacement non résolutif de la réponse

## Objet

Ce document applique au cas des dossiers TA Bastia n° 2601714-1 et 2601715-1 la méthodologie Cogentia des **Non-Resolutive Response Patterns**.

Il ne cherche pas à établir une intention du greffe. Il décrit une séquence documentaire et mesure ce qu'elle résout réellement.

## 1. Question initiale

Le 16 septembre 2026, une demande adressée au greffe du tribunal administratif de Bastia portait notamment sur :

1. la date et l'heure auxquelles les décisions avaient été rendues ou mises à disposition ;
2. la date et l'heure d'enregistrement de la note en délibéré envoyée le 14 septembre à 15 h 48 ;
3. son versement au dossier avant la décision ;
4. la liste chronologique des pièces enregistrées dans chacun des deux dossiers.

## 2. Réponse du greffe

Le greffe a fourni plusieurs informations utiles :

- les décisions ont été rendues le 14 septembre ;
- elles ont été notifiées le même jour par voie postale ;
- la formation de jugement a pris connaissance de la note en délibéré avant de prendre sa décision ;
- pour la chronologie des pièces, le demandeur a été invité à consulter le système de suivi Sagace / e-Sagace.

## 3. Consultation effective de Sagace

Le renvoi a été suivi pour les deux dossiers.

Les historiques Sagace des dossiers 2601714 et 2601715 sont strictement parallèles et font apparaître notamment :

```text
11/09/2026  Requête nouvelle — PRÉFECTURE DE LA HAUTE-CORSE
11/09/2026  Mise au rôle
11/09/2026  communications de la requête / avis d'audience
14/09/2026  Audience publique
14/09/2026  Réception d'une lettre — M. ROBERT
14/09/2026  Réception d'une note en délibéré — M. ROBERT
14/09/2026  Jugement
14/09/2026  notifications du jugement
```

Sagace confirme donc l'existence de deux productions distinctes le 14 septembre : une **lettre** et une **note en délibéré**.

## 4. Gain informationnel réel

La séquence permet d'établir ou de renforcer plusieurs faits :

- une note en délibéré a été enregistrée ;
- une autre production distincte, qualifiée de « lettre », a également été enregistrée ;
- les deux événements sont antérieurs, dans l'ordre d'affichage Sagace, à la ligne « Jugement » ;
- la formation de jugement avait pris connaissance de la note en délibéré avant de décider, selon la réponse écrite du greffe.

## 5. Résidu non résolu

La consultation Sagace ne fournit pas :

- l'heure d'enregistrement de la « lettre » ;
- l'heure d'enregistrement de la note en délibéré, **désormais résolue à 15:49 par le jugement reçu / publié** ;
- l'heure du jugement ou de sa mise à disposition ;
- l'identification précise du document correspondant à la « lettre » ;
- l'inventaire exact des pièces annexées à la « Requête nouvelle » préfectorale ;
- le détail permettant de déterminer si certaines pièces reçues par la préfecture avant 18 h le 11 septembre ont ou non été transmises au tribunal.

## 6. Classification FractaCognition

```yaml
response_resolution_check:
  classification: response_displacement
  target_question: "obtenir heures précises et inventaire matériel du dossier"
  directly_resolved:
    - "la note en délibéré a été connue avant décision"
    - "l'heure d'enregistrement de la note en délibéré est 15:49"
    - "les décisions ont été rendues le 14 septembre"
  useful_adjacent_information:
    - "Sagace distingue une lettre et une note en délibéré"
  referral:
    source: "Sagace / e-Sagace"
    followed: true
    yield: "chronologie sommaire sans heures ni inventaire détaillé"
  residual_uncertainty:
    - "heure d'enregistrement de la lettre"
    - "heure du jugement"
    - "nature exacte de la lettre"
    - "inventaire des pièces de la requête préfectorale"
  intent_status: "unknown"
  next_reality_probe: "relance étroite exécutée le 25 septembre après lecture de l'expédition du jugement"
```

## 7. Discipline d'interprétation

### FACT
- une demande précise a été formulée ;
- le greffe a répondu partiellement ;
- le greffe a renvoyé vers Sagace ;
- Sagace a été effectivement consulté ;
- les informations décisives restantes n'y figurent pas dans la vue accessible.

### INFERENCE
Le renvoi Sagace est **partiellement informatif mais non résolutif** pour les questions des heures et de l'inventaire des pièces.

### HYPOTHESIS
Toute qualification d'évitement volontaire, de délai, d'obstruction ou de stratégie resterait hypothétique en l'absence d'éléments indépendants supplémentaires.

## 8. Test de Réalité exécuté le 25 septembre

Le greffe a répondu le 21 septembre à la demande distincte sur la trace d'audience, le greffier et la minute en invitant à retirer le pli postal et en indiquant que le jugement répondait aux interrogations, tout en restant disponible si des questions subsistaient après lecture.

Le pli a été retiré et le jugement lu le 25 septembre. Cette lecture a effectivement résolu un point important — l'heure d'enregistrement de la note en délibéré, **15:49** — mais n'a pas fourni :

- l'identité ni l'heure de la « Réception d'une lettre » ;
- l'heure exacte de mise à disposition du jugement ;
- l'inventaire des pièces préfectorales initiales et ultérieures ;
- l'existence et les modalités d'accès à une trace d'audience ;
- la confirmation de l'identité du greffier présent à l'audience ;
- les modalités d'accès à la minute.

Une relance limitée à ces six points a donc été envoyée le **25 septembre à 16:50:46**, dans le fil existant, avec Laurence Ceccaldi et Maguy en copie.

La séquence ajoute un second test du pattern : une réponse peut être utile et de bonne foi tout en surestimant ce que la source vers laquelle elle renvoie résout réellement. L'intention reste `unknown` ; seul le différentiel entre **questions posées** et **questions effectivement résolues** est ici mesuré.

## Compression

> La réponse du greffe a apporté une information importante, puis renvoyé vers Sagace pour le reste. Sagace a confirmé plusieurs événements mais n'a pas fourni les heures ni l'inventaire demandé. Le résidu reste donc objectivement identifiable, sans qu'il soit nécessaire d'attribuer une intention au greffe.
