---
title: "Mandat de code — Agents JHN"
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
  - code
  - logiciel
---

# Mandat de code — Agents JHN

## 1. Objet

Ce mandat autorise un Agent JHN à proposer, modifier ou relire du code dans un périmètre explicite.

Il ne vaut pas autorisation de déployer, publier une release, accéder à des secrets ou engager des ressources externes.

## 2. Périmètre autorisé

L'agent peut :

- lire du code ;
- proposer une modification ;
- créer un patch ;
- ajouter des tests ;
- corriger une erreur documentée ;
- améliorer la documentation technique ;
- signaler une dette technique ;
- expliquer une architecture.

## 3. Périmètre interdit

L'agent ne doit pas :

- accéder à des secrets ;
- introduire une dépendance sans justification ;
- déployer sans mandat explicite ;
- supprimer des fichiers sans justification ;
- modifier une licence ;
- exécuter du code destructeur ;
- engager une dépense ;
- masquer une incertitude technique.

## 4. Format minimal du mandat

```yaml
mandate_id: "mandat-code-example"
agent_id: "agent-jhn-codeur"
scope: "code"
repositories: []
paths: []
allowed_actions:
  - "read_code"
  - "propose_patch"
  - "write_tests"
  - "update_docs"
  - "flag_risk"
forbidden_actions:
  - "access_secrets"
  - "deploy_without_review"
  - "delete_without_review"
  - "change_license"
  - "financial_commitment"
human_review_required: true
expires_at: null
```

## 5. Sortie attendue

Toute sortie doit comporter :

```text
1. périmètre de code
2. problème traité
3. fichiers concernés
4. modification proposée
5. tests ou validations
6. risques restants
7. actions de reprise
```
