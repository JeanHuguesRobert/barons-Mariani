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
research/perform_fixbugsfirst_technical_debt_negotiation_power.md
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

### 5.5b Perform (société) et FixBugsFirst

```yaml
id: perform_company
period: 1987_1997
place: Aix-en-Provence
source_status:
  kind: personal_memory
  confidence: medium
  comment: "Maison logicielle fondée en 1987 ; cession au partenaire 50 % fin 1997. Note historique dédiée."
  see: research/perform_fixbugsfirst_technical_debt_negotiation_power.md
```

```yaml
id: fix_bugs_first
period: perform_period
source_status:
  kind: public_trace
  confidence: high
  comment: "Pratique de gouvernance de projet (bugs avant features) face à la dette technique avant le nom courant. Traces c2 : FixBugsFirst, JeanHuguesRobert. Suite ops contemporaine : operium/docs/fix-bugs-first.md"
```

### 5.6 StarX25 / StarWall (X.25 Firewall)

```yaml
id: star_x25
period: perform_period
product_kind: x25_firewall
people:
  - Jean Vincent
  - Jean Hugues Noël Robert
source_status:
  kind: personal_memory
  confidence: high
  comment: "Nomenclature opérateur : StarX25 = the X.25 Firewall (distinct de SAGE = management system). Mécanismes (auth, call deflection, langage embarqué, StarWall) et documentation : to_verify."
```

Points à établir :

- conception exacte et répartition des rôles ;
- présence et fonction de LinkOS ;
- nature du langage embarqué ;
- mécanisme précis d'identification et d'authentification ;
- usage de la call deflection X.25 ;
- chronologie StarX25 / StarWall ;
- positionnement commercial « firewall » vs doc technique « gateway ».

### 5.7 SAGE / Emul (management system)

```yaml
id: sagex_emul
period: perform_period
product_kind: network_management_system
acronym_fr: "Système d'Aide à la Gestion d'Equipements hétérogènes"
runtime_early:
  - DOS
  - DESQview   # Quarterdeck; multitasking + IPC under DOS; memory may say "Deskview"
desqview_role: "multitasking layer + Inter-Process Communication (IPC)"
market_scope_memory: "France; private X.25 networks; substantial installed base"
source_status:
  kind: personal_memory
  confidence: high
  comment: >
    SAGE acronym + distinct from StarX25. Early/mainline installs: DOS/DESQview
    before/beside SAGE/X Unix. DESQview provided multitasking and IPC between
    processes/tasks — application runtime for SAGE, not mere UI switching.
    CMIP hard given machines + installed base. See perform note §4.1d.
```

### 5.7b SAGE/X (Unix)

```yaml
id: sage_x
period: mid_1990s_approx
product_kind: network_management_system_unix
slash_x_means: Unix
platforms:
  - Unix
  - IBM AIX  # RS/6000 line available from Feb 1990; port mid-90s still plausible
market_context: "Unix NMS competitive era (OpenView established ~1990; mid-90s heyday vs SunNet Manager)"
source_status:
  kind: personal_memory
  confidence: medium
  comment: >
    /X = Unix (Perform). ~mid-1990s. External check 2026-07-26: OpenView/NNM technology
    already licensed by IBM from HP in 1990 — not a mid-90s first release. RS/6000+AIX
    from 1990. Reformulate "when HP released OpenView" as market pressure / dominance era.
    Exact SAGE/X ship dates and Unix targets (HP-UX, Solaris, AIX…): to_verify.
    See research/perform_fixbugsfirst_technical_debt_negotiation_power.md §4.1b.
```

### 5.7d Emul language + LinkOS kernel

```yaml
id: emul_language
period: perform_period
name_from: "Emulation — automate human actions at a VT100-class screen/keyboard"
role: "operator-emulation language (not CPU emulator); text terminal automation"
implementations:
  - Turbo Prolog (first)
  - C/C++ (second; includes multitasking kernel already named LinkOS)
linkos_role: "multitasking kernel inside Emul C/C++ era; continues evolving"
contemporary_trace:
  - "https://github.com/JeanHuguesRobert/l8  # JS cooperative multi-tasker; LinkOS lineage"
  - "Inox l9 / inseme COP  # later generalizations"
source_status:
  kind: personal_memory
  confidence: high
  comment: >
    Emul developed by JHR: Turbo Prolog then C/C++ with LinkOS kernel already
    present. LinkOS evolved and still does; l8 is the attested JS descendant.
    Period Emul sources: to_verify in personal archives. See perform note §4.1e.
```

### 5.7c Standards context (GDMO / CMIP / SNMP)

```yaml
id: nms_standards_era
period: late_1980s_to_mid_1990s
terms:
  GDMO: "Guidelines for the Definition of Managed Objects (ISO/IEC 10165-4 / ITU-T X.722)"
  CMIP_CMIS: "Common Management Information Protocol / Service (OSI)"
  SNMP: "Simple Network Management Protocol (TCP/IP); first RFCs ~1988–1990"
source_status:
  kind: public_trace
  confidence: high
  comment: >
    Memory cue "Guidelines for the Management Of…" ≈ GDMO but exact name is
    Definition of Managed Objects. SNMP does not "appear" mid-90s — SNMPv1 RFCs
    1988/1990; mid-90s is NMS product maturity and SNMP vs CMIP/GDMO coexistence.
    SAGE product binding to either stack: to_verify. See perform note §4.1c.
```

### 5.8 Perform DashBoard

```yaml
id: dashboard
period: late_1990s
source_status:
  kind: public_trace
  confidence: high
  comment: "Transition IP, SNMP, Cisco, Java et Web. Stabiliser la chronologie, les fonctionnalités et les sources publiques. SNMP déjà standard IP avant DashBoard."
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
