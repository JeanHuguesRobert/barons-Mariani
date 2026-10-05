---
title: "Mariani Village — Architecture technique"
subtitle: "Structure des dossiers, contrats de projection et outillage d'inspection"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-10-04"
version: "0.1"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
---

# Mariani Village — Architecture technique

## 1. Arborescence du projet

```text
projects/village/
├── README.md                  # Entrée générale du projet
├── living-book.yml            # Manifeste déclaratif living-book/v1
├── corpus.yml                 # Manifeste de corpus
├── architecture.md            # Spécification technique
├── editorial-architecture.md  # Doctrine éditoriale et régimes de preuve
├── guide-profile.yml          # Profil d'inférence Cogentia Guide borné
├── manuscript/                # Manuscrit du Livre
├── magazine/                  # Chroniques, deltas et articles
│   └── federated/             # Items syndiqués depuis d'autres Livres Vivants
├── annexes/                   # Pièces justificatives et preuves
├── editions/                  # Registre des éditions gelées (index.md)
├── projections/               # Contrats de projection de travail
├── deploy/                    # Documentation de déploiement (Operium)
└── site/                      # Projection statique pour le Web
```

## 2. Outillage Living Book Factory

Ce projet est inspecté et validé via l'outil `living-book` :

```bash
# Valider le manifeste
node scripts/living-book.js validate projects/village/living-book.yml

# Inspecter la conformité doctrinale et technique
node scripts/living-book.js inspect projects/village/living-book.yml
```
