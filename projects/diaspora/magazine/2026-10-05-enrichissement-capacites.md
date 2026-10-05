---
title: "Magazine — enrichissement sourcé du graphe et consolidation des 5 faces"
date: "2026-10-05"
status: "working-note"
language: "fr"
document_role: "magazine"
visibility: "public"
provenance:
  origin_type: "issue-continuation"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/109"
  origin_date: "2026-10-05"
---

# 5 octobre 2026 — enrichissement sourcé du graphe et consolidation des 5 faces

Ce nouveau numéro du Magazine enregistre l'accomplissement du premier jalon d'élargissement qualitatif et méthodologique de DIASPORA ([Issue #109](https://github.com/JeanHuguesRobert/barons-Mariani/issues/109)) et sa structuration complète sous l'architecture des 5 faces du Livre Vivant ([Issue #96](https://github.com/JeanHuguesRobert/barons-Mariani/issues/96) / `research/livre_vivant.md`).

## 1. De la preuve de concept à l'hétérogénéité des fonctions collectives

Le seed initial (phase 1) comptait 30 entités centrées sur la démonstration de la machine. L'incrément du 5 octobre 2026 intègre des catégories fonctionnelles diversifiées, sans aucune ingestion de profil individuel :

- **Réseau professionnel et mobilité de retour** : modélisation de `communiti` (Ajaccio) et du projet opérationnel `Vultà`, première offre du graphe explicitement ouverte (`open_to_help: true`) pour l'accompagnement des actifs souhaitant revenir travailler en Corse ;
- **Coordination associative territoriale** : intégration de la `Fédération des Groupements Corses de Marseille et des Bouches-du-Rhône` (RNA W133003272, SIREN 397649187), active depuis 1959 dans la fédération, la culture et la solidarité ;
- **Réseau sectoriel éducatif** : intégration de l'association des `Corses de l'Éducation Nationale` (RNA W133010679), orientée vers le soutien à la jeunesse et l'entraide ;
- **Réseau de sociabilité et culture en région Sud** : intégration d'`Anima Corsa` (Nice, RNA W062007254) et d'`Anima Corsa 06` (Cannes, RNA W061008755, SIREN 824778468), reliant île, continent et diaspora.

## 2. Invariants épistémiques vérifiés

Quatre tests de validation épistémique ont été appliqués avec succès :

- **Test A (mobilité de retour)** : requête combinant la région Corse, le besoin de retour et l'exigence d'une aide ouverte (`requireOpenToHelp: true`) isolant de façon univoque l'offre de `Vultà`, tout en refusant les acteurs n'ayant qu'un intérêt générique déclaré ;
- **Test B (coordination territoriale)** : recherche sur Bouches-du-Rhône et coordination découvrant la Fédération de Marseille avec son statut d'objet associatif déclaré (`open_to_help: unknown`) ;
- **Test C (entraide locale)** : recherche sur les Alpes-Maritimes et la solidarité découvrant Anima Corsa Nice et Cannes ;
- **Test D (anti-hallucination d'aidant)** : une entité formulant un besoin n'est jamais promue au rang d'aidante.

## 3. Consolidation des 5 faces du Livre Vivant

L'architecture s'incarne désormais pleinement dans ses cinq composantes canoniques :

1. **Livre** : texte de fond (`manuscript/`), chapitres de la Corse furtive, annexes probatoires et version lue en ligne (`web/book.html`) ;
2. **Magazine** : veille continue et traçabilité des deltas (`web/magazine.html`) ;
3. **Site Web** : présence publique navigable, annuaire dynamique, carte géographique Leaflet/OSM, moteur de correspondance explicable (`web/`) ;
4. **Agent conversationnel spécialisé** : Guide conversationnel borné (`web/guide.html`, `web/guide.js`, profil `projects/diaspora/guide-profile.yml`) reposant sur 8 invariants stricts et préparation locale de contributions/objections sans transmission serveur ;
5. **Surface de collecte de traces engageantes** : formulaire local de préparation de paquets de contribution (`web/contribute.html`) conforme au schéma `diaspora.contribution.v0`.
