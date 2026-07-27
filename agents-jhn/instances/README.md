---
title: Registre des instances — Agents JHN
author: Jean Hugues Noël Robert, baron Mariani
date: '2026-07-08'
status: draft
document_role: register
document_kind: agent-instance-register
visibility: public
repository: JeanHuguesRobert/barons-Mariani
tags:
  - agents-jhn
  - instances
  - registre
  - mandat
provenance:
  origin_type: unknown
  origin_repository: unknown
  origin_ref: unknown
  origin_date: unknown
  derived_from: []
review:
  status: unreviewed
  reviewed_by: []
update_policy: UP-DEFAULT-REVIEWED
---

# Registre des instances — Agents JHN

## 1. Objet

Ce répertoire décrit les profils d'instances possibles des Agents JHN.

Une instance n'est pas une personne. C'est un rôle opératoire borné par :

- une fonction ;
- un mandat ;
- des sources autorisées ;
- des actions permises ;
- des actions interdites ;
- une révocabilité.
- un parent opératoire explicite lorsqu'il s'agit d'un sous-agent.

## 2. Instances initiales

Instances de base proposées :

```text
agent-jhn-root.yaml
agent-jhn-clarificateur.yaml
agent-jhn-archiviste.yaml
agent-jhn-contradicteur.yaml
agent-jhn-publicateur.yaml
```

`agent-jhn-root.yaml` est le gatekeeper numérique et l'agent-père des instances
initiales. Il route les demandes ; il n'est pas une autorité humaine de
substitution.

## 3. Règle commune

Une instance ne devient active qu'avec un mandat.

Le profil d'instance décrit une capacité potentielle. Le mandat autorise une action effective.

Toute instance autre que `agent-jhn-root` doit déclarer
`parent_agent_id: agent-jhn-root` ou un autre parent déjà mandaté. Elle ne peut
disposer d'identifiants directs vers un canal externe ou un moyen de paiement.
Ses demandes d'envoi, publication, déploiement, délégation ou dépense remontent
obligatoirement au parent.

```text
profil d'instance
→ capacité possible

mandat
→ action autorisée

révocation
→ retrait prioritaire de l'autorisation
```

## 4. Priorité des règles

En cas de conflit :

```text
révocation
> interdiction explicite
> mandat
> profil d'instance
> préférence stylistique
```

## 5. Usage par le jumeau numérique

Le jumeau numérique ne doit pas s'exprimer comme une instance indifférenciée.

Il doit, lorsque c'est utile, préciser le rôle actif : clarification, archivage, contradiction ou publication.
