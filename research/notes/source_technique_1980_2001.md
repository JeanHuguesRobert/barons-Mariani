---
title: "Note-source technique 1980-2001"
subtitle: "Matériau de preuve et de prudence pour la logique capacitaire"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-08"
status: "draft"
document_role: "source-note"
document_kind: "technical-source-note"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
tags:
  - source-note
  - logique-capacitaire
  - forth
  - linkos
  - x25
  - perform
  - odisei
---

# Note-source technique 1980-2001

## 1. Rôle

Cette note sépare le matériau source de la doctrine.

Elle sert à éviter qu'une grille de lecture conceptuelle soit confondue avec une preuve historique complète.

Document associé :

```text
research/lineages/forth_linkos_starx25_sagex_odisei_fractanet.yaml
```

## 2. Typologie de preuve

Chaque élément de la lignée doit être classé selon un statut explicite :

```yaml
source_status:
  kind: "personal_memory | repository_trace | public_trace | to_verify"
  confidence: "low | medium | high"
  comment: ""
```

## 3. Niveaux à distinguer

- `personal_memory` : souvenir personnel à conserver, mais à ne pas transformer automatiquement en fait externe.
- `repository_trace` : élément présent dans un dépôt GitHub ou un corpus source.
- `public_trace` : trace publique externe déjà retrouvée ou vérifiable.
- `to_verify` : élément plausible mais demandant une vérification ultérieure.

## 4. Lignée à documenter

La lignée technique à documenter est :

```text
Forth sur micro-ordinateur
→ redirection d'interface vers liaison série
→ usage du Minitel comme accès télématique
→ projet de serveur Minitel multi-session
→ LinkOS
→ LinkOS de type Unix sur 80286
→ Star X25
→ Sage/X et Emul
→ DashBoard
→ Odisei / 8x8
→ l8
→ FractaNet
```

## 5. Règle de prudence

Un Agent JHN doit toujours distinguer :

```text
ce qui est attesté
ce qui est remémoré
ce qui est interprété
ce qui reste à vérifier
```

## 6. Usage par les Agents JHN

Cette note doit être consultée avant toute publication historique, biographique ou technique portant sur la lignée Forth / LinkOS / X.25 / FractaNet.

Elle ne remplace pas les sources. Elle indique comment les classer.

## 7. Prochaine étape

Compléter cette note par des entrées datées, chacune avec :

```yaml
id: ""
label: ""
period: ""
summary: ""
source_status:
  kind: ""
  confidence: ""
  comment: ""
related_documents: []
```
