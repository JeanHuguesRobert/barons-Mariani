---
title: 1755 — Livre Vivant du constitutionnalisme démocratique moderne
description: Point d'entrée du Livre Vivant 1755 sur la Constitution corse de 1755 et sa réintégration dans l'histoire constitutionnelle mondiale.
author: Jean Hugues Noël Robert, baron Mariani
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
date: '2026-10-04'
last_modified_at: '2026-10-09'
version: '0.1'
status: working-paper
license: CC BY-SA 4.0
language: fr
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/1755/README.md
document_role: source
document_kind: project-readme
visibility: public
lifecycle_state: working
target_audience:
  - historiens
  - constitutionnalistes
  - citoyens
  - contributeurs
document_function: point d'entrée canonique du projet 1755
ai_assisted_by:
  - Antigravity — project bootstrap, 2026-10-04
provenance:
  origin_type: synthesis
  origin_repository: barons-Mariani
  derived_from:
    - research/autonomia/projet_1755.md
    - research/autonomia/1755.md
    - research/livre_vivant.md
    - projects/commons/annexes/nobles-douze-et-gouvernance-corse.md
review:
  status: unreviewed
  reviewed_by: []
related_documents:
  - projects/1755/corpus.yml
  - projects/1755/architecture.md
  - projects/1755/editorial-architecture.md
  - research/autonomia/projet_1755.md
changelog:
  - v0.1 (2026-10-04) — initial candidate bootstrap of Living Book 1755 under five-face architecture.
---


# 1755 — La Constitution de Pascal Paoli et le constitutionnalisme moderne

**1755** est un **Livre Vivant** consacré à la révolution constitutionnelle corse de 1755 et à sa réintégration argumentée dans l'histoire mondiale de la démocratie représentative moderne.

Il ne s'agit ni d'un repli mémoriel insulaire ni d'une sanctification anachronique, mais d'une **enquête probatoire ouverte** :

> **La Constitution votée à Corte en novembre 1755 est-elle l'un des premiers textes constitutionnels écrits de l'histoire moderne fondant la légitimité politique sur la souveraineté populaire, la séparation des pouvoirs et la désignation élective des magistrats par les chefs de famille ?**

---

## 1. Origine et articulation avec Commons

Le Livre Vivant 1755 est le prolongement politique direct du Livre Vivant **Commons** ([`projects/commons/`](../commons/README.md)) :
- La démocratie paolienne prend sa source dans la défense de la *Terra di Comune* (communaux pastoraux, forêts indivises et droits d'usage collectifs institués en 1358).
- C'est l'effondrement et la trahison oligarchique de la médiation corporatiste génoise — les **Nobles Douze** (*Nobili Dodici*, analysés dans [`annexes/01-nobles-douze-et-faillite-corporatiste.md`](annexes/01-nobles-douze-et-faillite-corporatiste.md)) — qui a poussé les communautés paysannes à briser le cadre colonial en 1729 et à instituer leur propre souveraineté constituante à Corte en 1755.

---

## 2. L'architecture des Cinq Faces

Conformément à la spécification canonique du Livre Vivant ([`architecture.md`](architecture.md)), **1755** s'articule autour de cinq faces publiques :

1. **Le Livre & les Annexes ([`manuscript/n1/`](manuscript/n1/) & [`annexes/`](annexes/)) :** Le récit fondamental en 4 mouvements et ses dossiers probatoires (texte critique de la Constitution, analyse des Nobili Dodici, inventaire archivistique, pistes de reconnaissance internationale).
2. **Le Magazine ([`magazine/`](magazine/)) :** Chroniques de vulgarisation et débats historiographiques vivants (le vote des femmes en 1755, l'écho américain et les *Sons of Liberty*).
3. **Le Site Web ([`site/`](site/)) :** Surface de lecture publique universelle statique, sans cookie ni pistage, conforme aux standards du Web ouvert et aux spécifications `llms.txt`.
4. **Le Guide Conversationnel ([`guide-profile.yml`](guide-profile.yml) & [`site/guide.html`](site/guide.html)) :** Agent d'exploration publique borné par 8 invariants stricts et le respect des 4 niveaux de preuve (Level A à C).
5. **La Collecte Engageante ([`site/contribuer.html`](site/contribuer.html)) :** Interface citoyenne locale de génération d'objections, de transcriptions archivistiques et de propositions d'amendements.

---

## 3. Plan du dossier

```text
projects/1755/
├── corpus.yml                  # Manifeste canonique du corpus 1755
├── architecture.md             # Spécification des 5 faces et des invariants
├── editorial-architecture.md   # Cadrage narratif et double temporalité janusienne
├── guide-profile.yml           # Invariants de l'agent conversationnel borné
├── README.md                   # Le présent fichier d'orientation
├── manuscript/n1/              # Les 4 mouvements du livre fondamental
├── annexes/                    # Pièces d'archives et traductions critiques
├── magazine/                   # Chroniques d'actualité et vulgarisation
├── chronology/                 # Chronologie comparée 1729–1769–présent
├── sources/                    # Registre des sources d'archives et bibliographie
├── editions/                   # Spécification de la Release Candidate 1 (RC1)
├── projections/                # Spécification de projection n1-working
├── deploy/                     # Cadrage d'hébergement pour 1755.acorsica.org
├── journals/                   # Journal d'amorçage et audit trails
└── site/                       # Surface statique de lecture universelle
```

---

## 4. Cadre institutionnel et licence

- **Porteur éditorial :** Institut Mariani, émanation R&D de l'association C.O.R.S.I.C.A., en lien avec le futur Fonds de dotation Barons Mariani.
- **Licence :** Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0).
- **Gouvernance :** Projet ouvert non lucratif orienté vers le bien commun documentaire mondial.

---

## Écho constitutionnel contemporain — état au 9 octobre 2026

L'examen en octobre 2026 du projet de loi constitutionnelle pour une Corse autonome au sein de la République est un **point de comparaison contemporain**, et non une preuve historique relative à la Constitution de 1755. La commission des lois du Sénat a référencé l'audition ministérielle du 7 octobre ; la séance du 26 octobre est programmée. Le rapporteur du texte n° 782 n'est pas nominativement confirmé dans le présent relevé.

- [Observatoire contemporain de l'autonomie](../../research/autonomia/observatoire_processus_autonomie_corse.md)
- [Continuité parlementaire](../../research/autonomia/note_continuite_parlementaire_autonomie_2026-09.md)

Conserver la distinction entre sources primaires historiques, interprétations historiographiques et processus constitutionnel contemporain.


---

## Actualisation des preuves — audition Gatel (9 octobre 2026)

Le [registre canonique des traces](../../research/autonomia/observatoire_processus_autonomie_corse.md) distingue désormais l’annonce de l’audition du 7 octobre, l’accès ultérieurement défaillant à sa fiche officielle (404), l’absence de compte rendu pour la semaine du 5 octobre sur la page consultée et le replay non vérifié. Il serait injustifié d’attribuer à la ministre un propos sur l’effectivité du projet n° 782 sans source primaire. Cette incertitude demeure ouverte et corrigible ; les éditions datées restent inchangées.


## Journal du 9 octobre 2026 — manuscrit de 1755

La cote **1 J 7/1** est repérée dans un catalogue patrimonial de la Constitution du 18 novembre 1755, attribuée aux Archives de Corse–Pumonti ; confrontation archivistique au manuscrit décrit par Carrington encore ouverte. Deux demandes documentaires ont été adressées le 9 octobre 2026 aux Archives de Corse (Ajaccio et Bastia). [Nouvelle chronique du Magazine](magazine/2026-10-09-une-cote-pour-la-constitution.md) ; [dossier probatoire](../../research/autonomia/1755-manuscrit-1j7-1-enquete.md).


## ⛔ INTERDICTION ABSOLUE D'ENVOYER DES COURRIELS SANS VALIDATION EXPRESSE

**Règle impérative de Jean Hugues Noël Robert (9 octobre 2026).** Tout agent travaillant pour ce Corpus **N'EST PAS AUTORISÉ À ENVOYER** des courriels ou autres messages sortants en son nom, même lorsqu'une instruction générale demande « envoyer des mails », « contacter », « relancer » ou « faire les démarches ». **Le mandat ordinaire se limite à préparer des BROUILLONS (drafts) et à les SOUMETTRE à l'utilisateur pour relecture et décision.**

- **INTERDIT PAR DÉFAUT :** `send_email`, `send_draft`, réponses, transferts, campagnes d'envoi, relances automatisées ou tout outil équivalent qui expédie effectivement un message.
- **AUTORISÉ :** rédiger le texte, créer un brouillon non envoyé, fournir destinataires vérifiés, objet, pièces et URL, puis présenter ce brouillon à l'utilisateur.
- **Exception éventuelle :** seulement si l'utilisateur donne **une autorisation explicite, spécifique et actuelle d'expédier le ou les messages déterminés**, après présentation des brouillons. Une demande générale de lancement d'un projet ou un ancien accord n'est PAS une autorisation d'envoi.
- La création d'un brouillon ne vaut **jamais** envoi. Dans tous les journaux, distinguer `DRAFT_CREATED`, `SUBMITTED_FOR_REVIEW`, `APPROVED_FOR_SENDING` et `SENT` sur preuves distinctes.
- **Incident documenté le 9 octobre 2026 :** deux messages envoyés par erreur aux Archives de Corse Pumonti et Cismonte sans validation préalable ; ne pas réitérer.
