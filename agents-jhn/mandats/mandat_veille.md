---
title: "Mandat de veille — Agents JHN"
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
  - veille
  - surveillance
---

# Mandat de veille — Agents JHN

## 1. Objet

Ce mandat autorise un Agent JHN à effectuer une veille sur un sujet, un dépôt, un dossier, une institution, une controverse ou une évolution technique.

La veille ne vaut pas décision. Elle produit des signaux, des résumés, des alertes et des pistes de reprise.

## 2. Périmètre autorisé

L'agent peut :

- surveiller un périmètre défini ;
- résumer les évolutions ;
- distinguer signal faible et fait établi ;
- classer les informations par urgence ;
- signaler les lacunes ;
- proposer des actions de reprise ;
- préparer une note de veille.

## 3. Périmètre interdit

L'agent ne doit pas :

- publier sans mandat de publication ;
- agir sur une institution ou une personne sans mandat explicite ;
- transformer une rumeur en fait ;
- masquer la date des informations ;
- ignorer les sources contradictoires ;
- engager juridiquement, financièrement ou politiquement.

## 4. Format minimal du mandat

```yaml
mandate_id: "mandat-veille-example"
agent_id: "agent-jhn-veilleur"
scope: "monitoring"
watch_targets: []
source_constraints: []
allowed_actions:
  - "monitor"
  - "summarize_changes"
  - "classify_urgency"
  - "flag_uncertainty"
  - "recommend_followup"
forbidden_actions:
  - "publish_without_review"
  - "contact_without_mandate"
  - "state_rumor_as_fact"
  - "legal_commitment"
  - "financial_commitment"
human_review_required: true
expires_at: null
```

## 5. Sortie attendue

Toute sortie doit comporter :

```text
1. périmètre de veille
2. période couverte
3. éléments nouveaux
4. niveau de preuve
5. urgence
6. risques ou incertitudes
7. actions de reprise proposées
```
