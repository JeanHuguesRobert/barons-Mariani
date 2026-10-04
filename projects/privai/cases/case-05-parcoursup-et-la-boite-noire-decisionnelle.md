---
title: "Cas 05 — Parcoursup et l'opacité décisionnelle des algorithmes locaux"
description: "Analyse de l'asymétrie cognitive et juridique entre les candidats lycéens et les algorithmes paramétrables des commissions d'examen des vœux."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/cases/case-05-parcoursup-et-la-boite-noire-decisionnelle.md"
document_role: "source"
document_kind: "reality-case"
visibility: "public"
lifecycle_state: "working"
derived_from:
  - "projects/privai/doctrine/anti-demos.md"
  - "research/traceabilite_des_actes.md"
  - "research/pathologie_du_secret.md"
---

# Cas 05 — Parcoursup et l'opacité décisionnelle des algorithmes locaux

## Fiche synthétique

- **case_id** : PRIVAI-RC-05
- **type** : Affectation éducative, secret administratif & asymétrie de classement
- **source** : Décision du Conseil Constitutionnel n° 2020-834 QPC du 3 avril 2020 ; Code de l'éducation (art. L. 612-3) ; rapports de la Cour des Comptes (2020, 2023) ; [`research/traceabilite_des_actes.md`](file:///C:/tweesic/barons-Mariani/research/traceabilite_des_actes.md).

## Description du cas

### 1. Capacité annoncée
La plateforme nationale Parcoursup centralise et harmonise les vœux d'accès à l'enseignement supérieur pour près d'un million de lycéens chaque année. La promesse de l'État est une démocratisation de l'orientation, un traitement égalitaire sans passe-droit et une fluidification des admissions via un algorithme national transparent.

### 2. Interaction réelle
Si le code source de l'algorithme national d'appariement a été rendu public après une longue bataille juridique menée par des collectifs étudiants, le cœur réel de la décision d'admission réside dans les **algorithmes locaux d'aide à la décision** développés de manière discrétionnaire par les commissions d'examen des vœux de chaque formation universitaire ou école.
Chaque filière applique ses propres pondérations statistiques (notes du bac, coefficients par matière, réputation du lycée d'origine, analyse automatisée des lettres de motivation).

### 3. Asymétrie observable
Le jeune citoyen candidat (souvent mineur ou jeune majeur) est placé dans une asymétrie cognitive et juridique totale :
- Il postule sans connaître les critères de pondération réels appliqués à son dossier ;
- Le secret des délibérations des jurys (sanctuarisé par la loi) est opposé aux familles pour refuser la communication des lignes de code et des barèmes précis ;
- Le candidat rejeté reçoit un refus stéréotypé sans motivation personnalisée explicite, rendant tout recours contentieux quasi impossible.

### 4. Outil / Contre-pouvoir mobilisé
La doctrine PrivAI oppose à cette fermeture les exigences suivantes :
- **L'auditabilité obligatoire des motifs :** toute décision administrative automatisée ou semi-automatisée doit fournir immédiatement au citoyen la décomposition mathématique et qualitative des critères ayant conduit au classement de son dossier ;
- **L'interdiction des critères clandestins :** interdiction de discriminations territoriales occultes (cote officieuse des lycées) non soumises à la délibération publique ;
- **Le droit d'objection assistée :** la possibilité pour le candidat d'utiliser un jumeau civique numérique pour vérifier la cohérence des décisions prises par rapport aux dossiers acceptés ayant des profils comparables.

### 5. Résultat observé
Le Conseil Constitutionnel a jugé conforme à la Constitution le secret des délibérations des jurys, mais a assorti sa décision d'une réserve majeure : l'administration a l'obligation légale de communiquer les critères généraux et les motifs individuels à tout candidat non retenu qui en fait la demande.
Néanmoins, dans les faits, l'asymétrie institutionnelle persiste : les délais de réponse administrative dépassent largement le calendrier de rentrée universitaire, vidant le recours de toute effectivité.

### 6. Résidu et limites
Le cas Parcoursup illustre la limite de la « transparence formelle » : publier un algorithme national ne sert à rien si les algorithmes locaux qui le nourrissent demeurent des secrets d'État à l'échelle de chaque établissement.

### 7. Critère d'effectivité
**Échec d'effectivité démocratique partielle** : La personne morale étatique s'est retranchée derrière le secret juridique pour préserver son confort discrétionnaire, maintenant les citoyens dans l'opacité décisionnelle. Ce cas justifie l'urgence d'inscrire le principe d'explicabilité obligatoire dans la législation sur l'IA publique.
