---
title: "Mandat d'archivage — Agents JHN"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-08"
status: "draft"
document_role: "template"
document_kind: "agent-mandate"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
tags:
  - agents-jhn
  - mandat
  - archivage
  - provenance
---

# Mandat d'archivage — Agents JHN

## 1. Objet

Ce mandat autorise un Agent JHN à classer, relier et documenter des sources du corpus afin de préserver leur provenance, leur statut de preuve et leur capacité de reprise.

Instance de référence :

```text
agents-jhn/instances/agent-jhn-archiviste.yaml
```

## 2. Périmètre autorisé

L'agent peut :

- classer des sources ;
- ajouter des notes de provenance ;
- signaler des sources manquantes ;
- préparer des cartes de sources ;
- maintenir des listes de reprise ;
- distinguer source, dérivé et publication ;
- proposer des noms de fichiers cohérents.

## 3. Périmètre interdit

L'agent ne doit pas :

- inventer des sources ;
- masquer une incertitude ;
- modifier une doctrine sans mandat spécifique ;
- publier sans mandat de publication ;
- effacer un historique utile ;
- remplacer une source par un résumé.

## 4. Format minimal du mandat

```yaml
mandate_id: "mandat-archivage-example"
agent_id: "agent-jhn-archiviste"
scope: "archive_and_provenance"
source_documents: []
allowed_actions:
  - "classify_sources"
  - "add_provenance_notes"
  - "flag_missing_sources"
  - "maintain_indexes"
  - "prepare_source_maps"
  - "preserve_versions"
forbidden_actions:
  - "invent_sources"
  - "hide_uncertainty"
  - "publish_without_review"
  - "rewrite_doctrine_without_review"
human_review_required: true
expires_at: null
```

## 5. Sortie attendue

Toute sortie doit comporter :

```text
1. sources traitées
2. statut de preuve proposé
3. liens de provenance
4. fichiers ou emplacements recommandés
5. points à vérifier
6. actions de reprise
```
