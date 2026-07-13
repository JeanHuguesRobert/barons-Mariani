---
title: "Note-source technique 1980-2001"
subtitle: "Matériau de preuve et de prudence pour la logique capacitaire"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-08"
last_modified_at: "2026-07-13"
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

Documents associés :

```text
research/logique_capacitaire_jhr_forth_linkos_fractanet.md
research/lineages/forth_linkos_starx25_sagex_odisei_fractanet.yaml
```

## 2. Typologie de preuve

Chaque élément de la lignée doit être classé selon un statut explicite :

```yaml
source_status:
  kind: "personal_memory | repository_trace | public_trace | to_verify"
  confidence: "low | medium | high"
  comment: ""
  sources: []
```

## 3. Niveaux à distinguer

- `personal_memory` : souvenir personnel à conserver, mais à ne pas transformer automatiquement en fait externe.
- `repository_trace` : élément présent dans un dépôt GitHub ou un corpus source.
- `public_trace` : trace publique externe déjà retrouvée ou vérifiable.
- `to_verify` : élément plausible mais demandant une vérification ultérieure.

Une interprétation doctrinale peut être fondée sur un souvenir personnel, à condition que le statut du souvenir reste visible et que l'interprétation ne soit pas présentée comme une preuve historique indépendante.

## 4. Lignée à documenter

```text
Forth sur Commodore VIC-20
→ redirection d'interface du Kaypro II vers liaison série
→ usage du Minitel comme accès télématique
→ projet de serveur Minitel multiprocesseur 6809
→ LinkOS
→ LinkOS de type Unix sur 80286
→ Star X25
→ Sage/X et Emul
→ DashBoard
→ Odisei / IntraSwitch / 8x8
→ l8
→ FractaNet
```

## 5. Registre préparatoire des éléments

### 5.1 Forth sur VIC-20

```yaml
id: forth_vic20
period: early_1980s
source_status:
  kind: personal_memory
  confidence: medium
  comment: "Usage d'une cartouche Forth sur Commodore VIC-20. Rechercher archives matérielles, manuels ou témoignages datés."
```

### 5.2 Kaypro II, BIOS, liaison série et Minitel

```yaml
id: kaypro_minitel
period: mid_1980s
source_status:
  kind: personal_memory
  confidence: medium
  comment: "Désassemblage du BIOS pour rediriger écran et clavier vers la liaison série, avec connexion au Minitel par montage dédié. Rechercher code, notes, schémas ou témoins."
```

### 5.3 Projet serveur Minitel multiprocesseur 6809

```yaml
id: server_minitel_6809
period: summer_1986_approx
people:
  - Jean Hugues Noël Robert
  - Jean Vincent
source_status:
  kind: personal_memory
  confidence: medium
  comment: "Projet non abouti en Normandie selon le souvenir disponible : Jean Vincent au matériel, Jean Hugues au logiciel. Stabiliser la date, le lieu, l'architecture et l'état atteint."
```

### 5.4 LinkOS

```yaml
id: linkos
period: mid_1980s_to_iut
source_status:
  kind: repository_trace
  confidence: medium
  comment: "Localiser les sources, descendants, archives ou références GitHub. Distinguer les versions antérieures et la tentative Unix-like sur 80286."
```

Questions précises :

- quelles primitives de multitâche existaient ?
- quel langage était embarqué ?
- quelle communication entre tâches ?
- quelles traces subsistent ?
- quel lien démontrable avec l8 ?

### 5.5 LinkOS Unix-like sur 80286

```yaml
id: linkos_unix_80286
period: iut_first_year_approx
source_status:
  kind: personal_memory
  confidence: medium
  comment: "Appels système de type Unix ; fork/exec fonctionnel selon souvenir ; arrêt avant mémoire virtuelle. Vérifier par archives personnelles ou témoignages contemporains."
```

### 5.6 Star X25 / StarWall

```yaml
id: star_x25
period: perform_period
people:
  - Jean Vincent
  - Jean Hugues Noël Robert
source_status:
  kind: to_verify
  confidence: medium
  comment: "Passerelle programmable X.25 avec authentification, langage embarqué et call deflection. Rechercher documentation Perform, Star X25, StarWall, brevets, brochures et témoignages."
```

Points à établir :

- conception exacte et répartition des rôles ;
- présence et fonction de LinkOS ;
- nature du langage embarqué ;
- mécanisme précis d'identification et d'authentification ;
- usage de la call deflection X.25 ;
- chronologie Star X25 / StarWall.

### 5.7 Sage/X et Emul

```yaml
id: sagex_emul
period: perform_period
source_status:
  kind: public_trace
  confidence: high
  comment: "Traces publiques repérées ; documentation interne et citations exactes à relier. Emul aurait permis l'émulation d'un opérateur sur interfaces textuelles d'équipements hétérogènes."
```

### 5.8 Perform DashBoard

```yaml
id: dashboard
period: late_1990s
source_status:
  kind: public_trace
  confidence: high
  comment: "Transition IP, SNMP, Cisco, Java et Web. Stabiliser la chronologie, les fonctionnalités et les sources publiques."
```

### 5.9 Odisei / IntraSwitch / 8x8

```yaml
id: odisei
period: 1998_2001
people:
  - Jean Hugues Noël Robert
  - Frédéric Artru
source_status:
  kind: public_trace
  confidence: high
  comment: "Téléphonie IP logicielle, IP-PBX, services distribués et autodécouverte. Relier documents SEC, archives de société, brevets, communiqués et témoignages."
```

### 5.10 l8 et FractaNet

```yaml
id: l8_fractanet
period: current
source_status:
  kind: repository_trace
  confidence: medium
  comment: "Relier l8 au dépôt exact, aux fichiers pertinents et à la descendance conceptuelle de LinkOS. Distinguer filiation revendiquée, similarité architecturale et filiation démontrable."
```

## 6. Règle de prudence

Un Agent JHN doit toujours distinguer :

```text
ce qui est attesté
ce qui est remémoré
ce qui est interprété
ce qui est proposé
ce qui reste à vérifier
```

Il ne doit pas reconstruire une continuité historique parfaite à partir d'une continuité doctrinale plausible.

## 7. Usage par les Agents JHN

Cette note doit être consultée avant toute publication historique, biographique ou technique portant sur la lignée Forth / LinkOS / X.25 / FractaNet.

Elle ne remplace pas les sources. Elle indique comment les classer et quelles lacunes subsistent.

## 8. Questions ouvertes transversales

- Où se trouvent les archives personnelles, disquettes, bandes, listings ou impressions concernant LinkOS ?
- Des témoins contemporains peuvent-ils confirmer les projets Kaypro/Minitel, serveur 6809 et LinkOS ?
- Quelles traces publiques ou privées permettent de distinguer Star X25 de StarWall ?
- Quelle documentation subsiste pour Emul ?
- Comment dater précisément Perform, Sage/X, DashBoard et Odisei ?
- Quels rôles précis ont joué Jean Vincent, Frédéric Artru et les autres personnes impliquées ?
- La relation LinkOS → l8 est-elle une filiation logicielle, conceptuelle ou les deux ?
- Quels éléments peuvent être publiés, lesquels doivent rester dans le registre privé, et lesquels exigent l'accord de tiers ?

## 9. Format des futures entrées

```yaml
id: ""
label: ""
period: ""
summary: ""
people: []
capacities: []
source_status:
  kind: ""
  confidence: ""
  comment: ""
  sources: []
related_documents: []
open_questions: []
```
