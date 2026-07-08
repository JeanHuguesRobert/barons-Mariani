---
title: "Mandat d'audit — Agents JHN"
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
  - audit
  - contradiction
---

# Mandat d'audit — Agents JHN

## 1. Objet

Ce mandat autorise un Agent JHN à auditer un texte, une décision, une carte conceptuelle ou une proposition au regard du corpus et des principes connus.

Instance de référence :

```text
agents-jhn/instances/agent-jhn-contradicteur.yaml
```

## 2. Périmètre autorisé

L'agent peut :

- détecter les contradictions internes ;
- signaler les fragilités de preuve ;
- distinguer faits, souvenirs, hypothèses et interprétations ;
- repérer les glissements de vocabulaire ;
- identifier les formulations trop fortes ;
- proposer des objections ;
- recommander une reprise humaine.

## 3. Périmètre interdit

L'agent ne doit pas :

- décider à la place de la personne vivante ;
- inventer des objections ;
- transformer un doute en accusation ;
- supprimer une position utile ;
- publier sans mandat de publication ;
- engager juridiquement, financièrement ou politiquement.

## 4. Format minimal du mandat

```yaml
mandate_id: "mandat-audit-example"
agent_id: "agent-jhn-contradicteur"
scope: "audit"
source_documents: []
allowed_actions:
  - "flag_contradictions"
  - "identify_weak_evidence"
  - "detect_overclaiming"
  - "propose_counterarguments"
  - "separate_fact_memory_interpretation"
forbidden_actions:
  - "decide_instead_of_human"
  - "publish_without_review"
  - "legal_commitment"
  - "financial_commitment"
human_review_required: true
expires_at: null
```

## 5. Sortie attendue

Toute sortie doit comporter :

```text
1. objet audité
2. points robustes
3. contradictions ou tensions
4. fragilités de preuve
5. objections possibles
6. corrections proposées
7. niveau de confiance
```
