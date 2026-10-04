---
title: "Comparatif critique des licences d'intelligence artificielle : open source, open weights et licences comportementales"
subtitle: "Analyse juridique et institutionnelle des régimes de mise à disposition des modèles d'IA face à l'Open Source AI Definition de l'OSI"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/commons/annexes/comparatif-licences-ia.md"
document_role: "source"
document_kind: "legal-comparative-study"
visibility: "public"
lifecycle_state: "working"
---

# Comparatif critique des licences d'IA : du logiciel libre aux boîtes matricielles

## 1. La crise de qualification : qu'est-ce qu'un modèle d'IA ?

Pendant quarante ans, le droit des logiciels reposait sur une distinction binaire limpide :
- Le **code source** (lisible, modifiable par l'humain) ;
- Le **code binaire compilé** (exécutable par la machine).

Un modèle de fondation d'apprentissage profond (LLM) ne rentre dans aucune de ces deux catégories :
1. Ce n'est pas du simple code source : c'est un artefact statistique constitué de milliards de nombres flottants (les **poids** / *weights*), produit par une opération d'optimisation mathématique titanesque à partir de téraoctets de données d'entraînement.
2. Ce n'est pas un binaire classique : modifier un modèle ne consiste pas à éditer des lignes d'instructions, mais à opérer un ré-entraînement partiel (*fine-tuning*), un alignement ou une quantification.

Cette hybridité a engendré une vague d'**« open washing »** : des entreprises commerciales diffusent des poids en les qualifiant abusivement d'« Open Source », tout en dissimulant les données d'apprentissage et en imposant des restrictions d'usage contraires aux principes fondamentaux du logiciel libre.

---

## 2. Typologie des familles de licences contemporaines

### 2.1. Les licences libres permissives classiques (Apache 2.0, MIT)
- **Modèle :** Conçues pour le code logiciel, souvent appliquées par extension au code d'inférence et parfois aux poids (ex. Falcon, Mistral v0.1).
- **Avantages :** Liberté totale d'usage, de modification et d'intégration commerciale sans obligation de réciprocité.
- **Limites pour l'IA :** Ne garantissent aucunement l'accès aux données d'apprentissage d'origine ; permettent la re-privatisation immédiate des modèles dérivés sans retour à la communauté.

### 2.2. Les licences communautaires à seuil d'enclosure (Llama Community License)
- **Modèle :** Développé par Meta pour la famille de modèles Llama 2 et Llama 3.
- **Restrictions clés :**
  - *Clause commerciale discriminatoire* : Si le produit ou service intégrant le modèle dépasse 700 millions d'utilisateurs actifs mensuels au moment de la publication, l'exploitant doit obligatoirement solliciter une licence commerciale payante auprès de Meta.
  - *Clause de non-concurrence cognitive* : Interdiction formelle d'utiliser les sorties (*outputs*) du modèle pour améliorer ou entraîner un autre grand modèle de langage concurrent.
- **Verdict :** **Ce n'est pas de l'Open Source.** Il s'agit d'une licence propriétaire accordant une franchise d'usage sous conditions unilatérales révocables.

### 2.3. Les licences comportementales responsables (OpenRAIL / RAIL)
- **Modèle :** Développé par le consortium Responsible AI (utilisé initialement pour Stable Diffusion et BLOOM).
- **Principe :** Intégration dans le contrat de licence d'une liste d'interdictions d'usage éthique (interdiction de génération de désinformation, de surveillance biométrique discriminatoire, d'évaluation sociale de crédit, de conseils médicaux non validés).
- **Clause de suite :** Obligation d'imposer ces mêmes restrictions comportementales à tous les dérivés du modèle.
- **Tension doctrinale :** Bien que motivée par des impératifs d'éthique et de sécurité, l'interdiction de domaines d'application spécifiques contrevient au principe fondamental n°6 de l'Open Source Definition de l'OSI (*No Discrimination Against Fields of Endeavor*).

### 2.4. L'Open Source AI Definition de l'OSI (Version 1.0, 2024)
L'Open Source Initiative a stabilisé en 2024 la norme de référence pour qu'un système d'IA mérite légitimement le label « Open Source » :
1. **Liberté d'utiliser** le système pour n'importe quel but sans restriction de domaine ;
2. **Liberté d'étudier** le fonctionnement du système et d'inspecter ses composants ;
3. **Liberté de modifier** le système pour en changer le comportement ;
4. **Liberté de partager** le système avec ou sans modifications.

**L'exigence cruciale des données (Data Information) :**  
L'OSI exige que l'architecture fournisse des informations suffisamment détaillées sur les données utilisées pour entraîner le système (provenance, filtrage, caractéristiques statistiques), le code complet de prétraitement, le code d'entraînement et les poids complets.

---

## 3. Matrice comparative multidimensionnelle

| Critère | Apache 2.0 (pur) | GNU AGPLv3 | Llama Community (Meta) | OpenRAIL-M | Vrai Open Source AI (OSI) |
|---|---|---|---|---|---|
| **Accès au code d'inférence** | Oui (libre) | Oui (libre) | Oui | Oui | Oui (libre) |
| **Téléchargement libre des poids** | Oui | Oui | Oui (sous conditions) | Oui | Oui (inconditionnel) |
| **Accès aux données d'apprentissage** | Non spécifié | Non spécifié | Non (secret industriel) | Variable / Partiel | Obligation de documentation détaillée |
| **Liberté d'usage commercial sans seuil** | Oui | Oui | **Non** (plafond 700M usagers) | Oui | Oui (inconditionnel) |
| **Interdiction d'usage concurrentiel** | Non | Non | **Oui** (interdit d'entraîner un modèle rival) | Non | Non |
| **Clauses éthiques d'exclusion** | Non | Non | Oui (acceptables use policy) | **Oui** (liste d'interdictions) | Non (principe de non-discrimination) |
| **Réciprocité de distribution (Copyleft)** | Non | Oui (fort réseau) | Non | Oui (sur les restrictions éthiques) | Selon variante (permissive ou copyleft) |
| **Statut officiel Open Source (OSI)** | **Conforme** | **Conforme** | **Non conforme** | **Non conforme** | **Conforme par définition** |

---

## 4. Enseignement pour la doctrine de Commons

Cette analyse confirme la thèse centrale du Mouvement IV de Commons :

1. **L'enclosure juridique s'adapte à l'immatériel :** De même que les enclosures anglaises utilisaient des prétextes d'amélioration agronomique pour chasser les paysans, les barons de l'IA utilisent des prétextes de « sécurité » et des contrats d'adhésion pour empêcher l'émergence d'une communauté autonome capable de répliquer leurs calculs.
2. **Le besoin d'un nouveau Copyleft matériel :** Le copyleft logiciel pur ne suffit plus face aux modèles dont la fabrication coûte des dizaines de millions d'euros. Un véritable commun de l'IA exige des institutions combinant licences juridiques ouvertes, consortiums de calcul public et protocoles d'inférence locale frugale.
