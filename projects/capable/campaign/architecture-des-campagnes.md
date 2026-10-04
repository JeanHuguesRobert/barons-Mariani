---
title: "Capable — architecture des campagnes"
author: "Jean Hugues Noël Robert"
date: "2026-10-04"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "campaign-architecture"
visibility: "public"
lifecycle_state: "working"
provenance:
  origin_type: "corpus-consolidation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "main"
  origin_date: "2026-10-04"
  derived_from:
    - "../README.md"
    - "../architecture.md"
    - "matrix.md"
    - "../manuscript/07-campagnes-comme-reality-tests.md"
    - "../manuscript/08-presidentielle-2027.md"
    - "../manuscript/05-machines-et-correction.md"
---

# Capable — architecture des campagnes

## 1. Principe de provenance

La **Campagne du Réel** désigne d'abord la première grande campagne documentée dans *Capable* : la séquence des Sénatoriales 2026 et ses prolongements documentaires, institutionnels et contentieux.

Elle ne doit pas être réécrite rétroactivement comme si elle avait toujours désigné une méthode générale.

Ce premier Reality Case permet toutefois d'extraire progressivement une **grammaire réutilisable des campagnes du Réel**.

> **La première campagne a donné son nom à une grammaire réutilisable ; la grammaire ne réécrit pas l'histoire de la première campagne.**

## 2. Architecture

```text
Capable
│
├── Campagne 1
│   Campagne du Réel
│   Sénatoriales 2026
│
└── Campagne 2
    Présidentielle 2027
    │
    ├── Marche du Soleil
    ├── Observatoire des Présentations 2027
    ├── Reality Cases / Acts
    └── autres dispositifs à qualifier
```

Capable est plus large que chacune de ses campagnes.

## 3. Grammaire commune

La grammaire issue de la première campagne est :

```text
trace
→ Révélateur
→ écart
→ exploration
→ Reality Test / Act
→ mesure
→ Stabilisateur
→ nouvelle confrontation au Réel
```

Cette grammaire n'impose pas les mêmes objets, acteurs, métriques ou procédures à chaque campagne.

Invariant :

> **Mêmes primitives lorsque leur utilité a été éprouvée ; autres instances, autres contraintes.**

## 4. Première campagne — Sénatoriales 2026

La Campagne du Réel constitue le Reality Case fondateur de cette architecture.

Elle a mobilisé notamment :

- chronologies ;
- sources primaires ;
- matrices d'interactions et d'effectivité ;
- demandes numérotées ;
- états `UNKNOWN` et `PENDING` ;
- distinction fait / interprétation / qualification ;
- contradiction et droit de réponse ;
- Cognitive Packets et continuations ;
- préparation puis saisine du Conseil constitutionnel.

Le contentieux qui se poursuit après le scrutin appartient à cette première campagne.

## 5. Deuxième campagne — Présidentielle 2027

La campagne présidentielle change d'échelle, de territoire, d'acteurs et de contraintes.

Elle réemploie la grammaire commune sans être renommée rétroactivement « Campagne du Réel n°2 ».

Trois dispositifs initiaux sont distingués :

1. **Soutiens → Relais → Présentateurs** : architecture de convergence sans confusion entre soutien politique, relais de réseau et présentation officielle ;
2. **Marche du Soleil** : dispositif territorial de rencontre du Réel ;
3. **Observatoire des Présentations 2027** : Révélateur public de l'écart entre proclamations de « parrainages » et matérialisation officielle.

## 6. Charnière du 7 octobre 2026

Le **7 octobre 2026 à 18 h** est d'abord une échéance procédurale forte de la première campagne : terme du délai identifié dans le Corpus pour la contestation de l'élection sénatoriale.

La lecture stratégique proposée le 4 octobre 2026 est d'en faire aussi une **charnière publique** :

```text
avant le dépôt
→ priorité absolue : requête CC + preuve du dépôt

après le dépôt
→ rendre visible la transition
→ ouvrir publiquement la seconde campagne
→ Km 0 de la Marche du Soleil
→ annoncer l'Observatoire
```

Cette charnière est une projection stratégique actuelle ; elle ne doit pas être rétrodatée comme intention antérieure.

## 7. Priorités opérationnelles jusqu'au 7 octobre

```text
P0 — requête au Conseil constitutionnel
P1 — tout ce qui sécurise P0
P2 — artefacts minimaux permettant la charnière publique
P3 — sophistication technique ultérieure
```

Règle :

> **Avant le 7 octobre 18 h, une nouvelle idée n'est prioritaire que si elle aide à sécuriser le dépôt ; sinon elle peut attendre.**

## 8. Symétrie et falsifiabilité

Les instruments construits par Capable doivent pouvoir révéler les propres écarts de Capable.

Un Révélateur qui ne peut contredire que les autres n'est pas un Révélateur suffisant.

Le même protocole de traçabilité doit donc être appliqué :

- aux proclamations des autres candidatures ;
- aux proclamations de Capable ;
- aux hypothèses de campagne ;
- aux résultats réellement observés.
