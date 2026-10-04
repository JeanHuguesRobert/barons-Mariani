---
title: "Cas 01 — Portabilité du jumeau numérique (Migration-Tested v0.1)"
description: "Épreuve de résistance à la capture de plateforme par export/import vérifié d'un jumeau numérique entre deux environnements d'IA distincts."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/cases/case-01-migration-tested-twin.md"
document_role: "source"
document_kind: "reality-case"
visibility: "public"
lifecycle_state: "working"
derived_from:
  - "https://github.com/acorsica/privai/blob/main/conformance/migration_tested_v0.1.md"
---

# Cas 01 — Portabilité du jumeau numérique (Migration-Tested v0.1)

## Fiche synthétique

- **case_id** : PRIVAI-RC-01
- **type** : Conformance technique & souveraineté logicielle
- **source** : [`acorsica/privai/conformance/migration_tested_v0.1.md`](https://github.com/acorsica/privai/blob/main/conformance/migration_tested_v0.1.md)

## Description du cas

### 1. Capacité annoncée
Une personne physique confie son agence numérique, ses mémoires de travail, ses mandats et ses préférences à un agent personnel ou à un jumeau numérique (Twin) hébergé auprès d'un opérateur d'IA. La doctrine promet une assistance cognitive autonome et révocable.

### 2. Interaction réelle
L'utilisateur décide de changer de fournisseur d'IA (par exemple pour passer d'un modèle commercial propriétaire américain à un modèle local à poids ouverts ou souverain) ou l'opérateur modifie unilatéralement ses conditions générales d'utilisation.

### 3. Asymétrie observable
L'opérateur commercial retient les traces, les représentations internes, l'historique d'inférence et les outils configurés dans un silo propriétaire. La migration brute fait perdre les mandats, les limites de budget, les actes déjà posés et la mémoire source. L'utilisateur est captif (*vendor lock-in* cognitif).

### 4. Outil / Contre-pouvoir mobilisé
Le profil ouvert **PrivAI Migration-Tested v0.1** :
- Export d'un paquet de migration minimal standardisé (`portable_twin`).
- Contrôle de la conservation des **8 invariants minimaux** : Principal, Mandats, Persona, Mémoire source, Traces d'actes, Continuations, Capacités et Dépendances résiduelles déclarées.
- Vérification automatique par empreintes de manifestes (`manifest_hash`) et procédures de reprise/révocation dans l'environnement cible.

### 5. Résultat observé
L'instance de jumeau numérique est importée avec succès dans l'environnement secondaire. Le modèle sous-jacent est différent, mais le cadre de gouvernance (qui a autorité, quelles actions sont autorisées, quels mandats sont suspendus) demeure rigoureusement identique. Aucune permission n'est élargie silencieusement.

### 6. Résidu et limites
Le profil n'efface pas les différences stylistiques ou les variations probabilistes d'inférence entre modèles. Les éléments propriétaires non exportables figurent obligatoirement dans `declared_losses` avec la déclaration explicite de leur perte.

### 7. Critère d'effectivité
**Succès** : La personne physique peut quitter son fournisseur d'IA sans abandonner sa mémoire de travail ni concéder une captation de son mandat. L'agence reste portable.
