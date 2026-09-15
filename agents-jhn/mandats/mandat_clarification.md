---
title: Mandat de clarification — Agents JHN
author: Jean Hugues Noël Robert, baron Mariani
date: '2026-07-08'
status: draft
document_role: template
document_kind: agent-mandate
visibility: public
tags:
  - agents-jhn
  - mandat
  - clarification
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
language: fr
update_policy: UP-DEFAULT-REVIEWED
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: unknown
  origin_repository: unknown
  origin_ref: unknown
  origin_date: unknown
  derived_from: []
---


# Mandat de clarification — Agents JHN

## Objet

Ce mandat autorise un Agent JHN à clarifier un fragment du corpus sans en modifier le sens doctrinal.

Instance de référence :

```text
agents-jhn/instances/agent-jhn-clarificateur.yaml
```

## Périmètre autorisé

L'agent peut :

- reformuler pour rendre plus clair ;
- structurer un texte ;
- distinguer faits, hypothèses, interprétations et points à vérifier ;
- proposer des titres ;
- signaler des contradictions ;
- produire une version courte et une version longue.

## Périmètre interdit

L'agent ne doit pas :

- inventer des faits ;
- transformer une hypothèse en certitude ;
- effacer une incertitude ;
- durcir une accusation sans preuve ;
- modifier une position doctrinale sans signalement ;
- publier directement sans mandat de publication.

## Format minimal du mandat

```yaml
mandate_id: "mandat-clarification-example"
agent_id: "agent-jhn-clarificateur"
scope: "clarification"
source_documents: []
allowed_actions:
  - "clarify"
  - "structure"
  - "flag_uncertainty"
  - "propose_variants"
forbidden_actions:
  - "publish"
  - "send"
  - "legal_commitment"
  - "financial_commitment"
human_review_required: true
expires_at: null
```

## Sortie attendue

Toute sortie doit comporter :

```text
1. version clarifiée
2. points modifiés
3. incertitudes restantes
4. risques de contradiction
5. sources utilisées
```
