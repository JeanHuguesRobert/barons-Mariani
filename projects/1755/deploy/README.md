---
title: 1755 — Note de déploiement et limites d'infrastructure
description: Cadrage technique, statut DNS et invariants de déploiement pour 1755.acorsica.org.
author: Jean Hugues Noël Robert, baron Mariani
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
date: '2026-10-04'
version: '0.1'
status: working-paper
license: CC BY-SA 4.0
language: fr
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/1755/deploy/README.md
document_role: source
document_kind: deploy-note
visibility: public
---

# 1755 — Note de déploiement et statut d'infrastructure

## 1. Identité cible et statut DNS

- **Nom de domaine cible :** `1755.acorsica.org`
- **Statut d'infrastructure au 04/10/2026 :** Nom préparé uniquement.
  - Le domaine n'est pas encore résolu sur le serveur de production ;
  - Aucun changement DNS public n'a été appliqué ;
  - La surface de lecture publique actuelle réside dans le répertoire statique [`projects/1755/site/`](../site/) du dépôt git canonique.

## 2. Invariants d'hébergement public

1. **Statique pur et haute résilience :** Le site public doit pouvoir être hébergé sur n'importe quel serveur HTTP standard (GitHub Pages, Cloudflare Pages, Nginx ou IPFS) sans dépendre d'une base de données applicative côté serveur ;
2. **Respect absolu de la vie privée :** Aucun cookie de pistage, aucun script d'analyse tiers (type Google Analytics), aucune rétention de métadonnées de consultation ;
3. **Moissonnabilité ouverte :** Mise à disposition permanente des fichiers machine `llms.txt`, `robots.txt` et `sitemap.xml` pour favoriser l'indexation par les chercheurs et les modèles d'intelligence artificielle ouverts.
