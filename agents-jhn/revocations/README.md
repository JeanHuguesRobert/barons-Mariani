---
title: "Registre de révocation — Agents JHN"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-08"
status: "draft"
document_role: "register"
document_kind: "revocation-register"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
tags:
  - agents-jhn
  - revocation
  - mandat
  - controle
---

# Registre de révocation — Agents JHN

## 1. Objet

Ce répertoire documente les révocations relatives aux Agents JHN.

La révocation est une primitive de souveraineté : une instance, un mandat, une capacité ou une source doit pouvoir être retiré du périmètre d'action d'un agent.

## 2. Ce qui peut être révoqué

Une révocation peut viser :

- une instance d'Agent JHN ;
- un mandat ;
- une capacité ;
- une source ;
- un droit d'accès ;
- une clé ;
- une publication ;
- une période d'activité ;
- un modèle ou outil autorisé.

## 3. Effets attendus

Une révocation doit :

1. identifier ce qui est révoqué ;
2. préciser la date d'effet ;
3. indiquer si elle est temporaire ou définitive ;
4. conserver la trace de la décision ;
5. empêcher la réactivation implicite ;
6. indiquer les conditions éventuelles de réactivation.

## 4. Format recommandé

Utiliser le modèle :

```text
template_revocation.yaml
```

## 5. Priorité

En cas de conflit entre un profil d'instance, un mandat et une révocation, la révocation prime.

```text
révocation
> interdiction explicite
> mandat
> profil d'instance
> préférence stylistique
```

## 6. Règle pour les Agents JHN

Un Agent JHN doit vérifier ce registre avant d'exécuter un mandat.

En cas de conflit entre un mandat et une révocation, la révocation prime.
