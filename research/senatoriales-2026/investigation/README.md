---
title: "Sénatoriales 2026 — enquête documentaire"
date: "2026-09-25"
status: "active"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "method"
document_kind: "investigation-method"
visibility: "public"
lifecycle_state: "active"
---

# Enquête documentaire

Ce répertoire conserve l'état évolutif de la reconstruction factuelle relative à la candidature sénatoriale de Haute-Corse de septembre 2026 et aux instances TA Bastia n° 2601714-1 et 2601715-1.

Son objectif n'est pas de défendre une conclusion prédéterminée.

Il vise à réduire progressivement les incertitudes en conservant la distinction entre ce qui est établi, rapporté, inféré, hypothétique et encore inconnu.

## 1. Statuts épistémiques

```yaml
established:
  meaning: "fait soutenu par une preuve documentaire directe ou une convergence documentaire suffisante"
reported:
  meaning: "fait rapporté par une personne identifiée, conservé comme témoignage ou déclaration"
inferred:
  meaning: "déduction explicitement dérivée d'un ou plusieurs faits établis"
hypothesis:
  meaning: "explication ou possibilité non établie"
open:
  meaning: "question factuelle non résolue"
superseded:
  meaning: "état antérieur remplacé ou précisé par une information ultérieure"
```

Un statut qualifie l'état de notre connaissance, non l'importance du fait.

## 2. Trois temps à distinguer

Pour chaque élément significatif, distinguer autant que possible :

```text
event_time
    moment où le fait s'est produit
institutional_knowledge_time
    moment où une institution déterminée disposait ou pouvait disposer de l'information
corpus_knowledge_time
    moment où le Corpus a obtenu suffisamment d'éléments pour qualifier le fait
```

Cette distinction est essentielle pour reconstruire ce que la préfecture ou le tribunal savait effectivement à un moment déterminé.

## 3. Principe de non-rétroactivité documentaire

Une preuve obtenue après le jugement peut établir qu'un événement s'est produit avant celui-ci.

Elle ne permet pas, à elle seule, d'affirmer que la formation de jugement connaissait alors cet événement.

La question de la connaissance doit être documentée séparément.

## 4. Reality Probes

Une demande d'information ciblée peut être traitée comme un **Reality Probe**.

Pour chaque probe, conserver :

- la question exacte ;
- son destinataire ;
- sa date ;
- les réponses reçues ;
- les questions effectivement résolues ;
- le résidu non résolu.

Une réponse qui fournit une information adjacente sans répondre à la question initiale ne ferme pas automatiquement celle-ci.

## 5. Documents

- [`chronology.md`](chronology.md) — chronologie probatoire ;
- [`knowledge-matrix.md`](knowledge-matrix.md) — état des questions résolues et ouvertes ;
- [`sources.md`](sources.md) — index des sources et de leur fonction ;
- [`probe-map.md`](probe-map.md) — carte évolutive des Reality Probes : inconnues, détenteurs, sorties possibles, deadlines et nouvelles branches rendues accessibles.

## 6. Règle de mise à jour

Lorsqu'une information nouvelle apparaît :

1. identifier sa source ;
2. qualifier ce qu'elle établit réellement ;
3. mettre à jour la matrice ;
4. ajouter ou préciser l'événement correspondant dans la chronologie ;
5. conserver l'ancien état lorsqu'il est utile à la compréhension de l'enquête ;
6. ne pas extrapoler au-delà de la preuve.

## 7. Neutralité causale

L'enquête peut constater une erreur, une omission, une contradiction, une absence de réponse ou une lacune documentaire lorsqu'elles sont établies.

Elle distingue ces observations de toute attribution de cause ou d'intention.

```text
observation != explication
corrélation != causalité
absence de réponse != preuve d'une intention
```
