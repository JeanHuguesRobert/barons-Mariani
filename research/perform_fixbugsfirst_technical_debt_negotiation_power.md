---
title: "Perform, FixBugsFirst et le pouvoir de négociation (1987–1997)"
subtitle: "Note historique — dette technique avant le nom, SAGE/X, indépendance multi-vendeur"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-26"
last_modified_at: "2026-07-26"
status: "draft"
document_role: "source-note"
document_kind: "historical-source-note"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
language: "fr"
related_repositories:
  - "JeanHuguesRobert/operium"
  - "JeanHuguesRobert/cogentia"
  - "JeanHuguesRobert/FractaVolta"
tags:
  - perform
  - fix-bugs-first
  - technical-debt
  - sage-x
  - x25
  - negotiation-power
  - vendor-independence
  - logique-capacitaire
  - histoire-technique
related_documents:
  - "logique_capacitaire_jhr_forth_linkos_fractanet.md"
  - "notes/source_technique_1980_2001.md"
  - "lineages/forth_linkos_starx25_sagex_odisei_fractanet.yaml"
---

# Perform, FixBugsFirst et le pouvoir de négociation (1987–1997)

## 1. Statut

Cette note est **historique et biographique-technique**. Elle appartient au versant
**barons-Mariani** (mémoire, lignée, prudence épistémique), pas au versant
opérationnel immédiat d’Operium.

Elle ne prétend pas être une monographie d’entreprise complète ni une preuve
juridique de priorités. Elle fixe un fil oral et pratique **à conserver**, avec
statuts de preuve visibles, pour que la suite du corpus (Cogentia, Operium,
FractaNet) ne confonde pas **doctrine d’aujourd’hui** et **épisode d’hier**.

Documents associés :

```text
research/logique_capacitaire_jhr_forth_linkos_fractanet.md
research/notes/source_technique_1980_2001.md
research/lineages/forth_linkos_starx25_sagex_odisei_fractanet.yaml
```

Prolongements **opérationnels** (hors historique pur) :

```text
operium/docs/fix-bugs-first.md
operium/backlog/          (registre Bug/Feature contemporain)
cogentia (indépendance multi-modèle / multi-fournisseur)
```

## 2. Perform (Aix-en-Provence)

| Champ | Élément (statut) |
|-------|------------------|
| Raison sociale / projet | Société de logiciel **Perform** (édition de produits + services associés) |
| Lieu | **Aix-en-Provence** |
| Fondation | **1987** (`personal_memory`, confidence medium — à croiser archives / Kbis / presse si publication académique) |
| Sortie du capital fondateur | Cession au partenaire à **50 %**, fin **1997** (`personal_memory`) |
| Nature | Maison d’édition logicielle, services autour des produits |

Produits réseau Perform à distinguer (nomenclature opérateur) :

| Produit | Rôle |
|---------|------|
| **SAGE** (Sage/X, + Emul) | **S**ystème d'**A**ide à la **G**estion d'**É**quipements hétérogènes |
| **StarX25** | **X.25 Firewall** — pare-feu / contrôle d'accès sur le plan X.25 |

L'insight « indépendance multi-vendeur / pouvoir de négociation » s'attache
surtout à **SAGE** ; StarX25 est le volet **sécurité frontière** du même
écosystème (détail §4).


## 3. FixBugsFirst — solution à un problème encore sans nom courant

### 3.1 Le problème

Dans une maison produit, quand le chantier **dérape** (trop de features, trop
peu de maîtrise, qualité en chute), le risque est de **continuer à ajouter**
pour « rattraper » le marché. Le résultat est une perte de contrôle.

Le phénomène a plus tard un nom largement partagé : **technical debt**
(métaphore de Ward Cunningham, début des années 1990). **Avant** que ce
vocabulaire soit stabilisé dans l’industrie, la pratique locale à Perform a été
formulée autrement.

### 3.2 La réponse pratique : Fix Bugs First

**FixBugsFirst** : lorsqu’un projet est hors de contrôle, on **arrête d’ajouter
des fonctionnalités** et on se dote d’un **suivi Bug/Feature suffisamment
sophistiqué** pour décider ce qui bloque quoi — puis on **répare d’abord**.

Ce n’est pas seulement un slogan de qualité. C’est une **technologie de
gouvernance de projet** : rendre le désordre **visible, typé, priorisé,
actionnable**.

### 3.3 Traces publiques (WikiWikiWeb / c2)

Sur le wiki original (c2), le principe est nommé et relié explicitement à
Jean Hugues Robert, notamment :

- [FixBugsFirst](https://wiki.c2.com/?FixBugsFirst)
- [JeanHuguesRobert](https://wiki.c2.com/?JeanHuguesRobert) — mention d’un succès
  (projet d’environ un million de lignes, en retard) par application du
  principe, et d’un échec aussi (donc pas de mythologie lisse)
- pages voisines : [BugFreeDoesntSell](https://wiki.c2.com/?BugFreeDoesntSell),
  [CreepingFeaturitis](https://wiki.c2.com/?CreepingFeaturitis),
  [NoBugDatabase](https://wiki.c2.com/?NoBugDatabase)

| Élément | `source_status` |
|---------|-----------------|
| Pratique FixBugsFirst chez Perform | `personal_memory` / medium |
| Pages c2 et formulation publique | `public_trace` / high |
| Identification exacte des projets « million de lignes » | `to_verify` |

## 4. SAGE (management) vs StarX25 (firewall)

### 4.0 Distinction produit (autorité opérateur)

```text
SAGE     = Système d'Aide à la Gestion d'Equipements hétérogènes
           (network management system)
StarX25  = X.25 Firewall
           (pare-feu X.25)
```

Ne pas fusionner les deux sous une seule étiquette « supervision X.25 ».
L’acronyme **SAGE** porte déjà le cœur de l’offre : **aide à la gestion**
d’**équipements hétérogènes** (pas un moniteur mono-constructeur).

### 4.1 SAGE — surface technique

**SAGE** (*Système d’Aide à la Gestion d’Equipements hétérogènes*) : management
system pour environnements **hétérogènes**, en particulier réseaux privés
**X.25**, avec médiation programmable (voir aussi **Emul** : émulation
d’opérateur sur interfaces textuelles d’équipements disparates — lignée
capacitaire).

### 4.1b SAGE → SAGE/X (le « /X » = Unix)

Le suffixe **/X** dans **SAGE/X** n’est pas décoratif : il marque le passage à
la version qui **tourne sous Unix**.

| Champ | Souvenir opérateur | Vérification externe (public) |
|-------|--------------------|-------------------------------|
| Signification de **/X** | version **Unix** de SAGE | — (nomenclature Perform) |
| Période SAGE/X | **milieu des années 1990** (approx.) | cohérent comme **fenêtre de port** pour une maison produit FR ; dates exactes Perform : `to_verify` |
| Contexte HP OpenView | « quand HP a sorti OpenView » | **nuance** : OpenView n’est **pas** une « sortie » milieu des années 90. La techno NNM/OpenView est déjà en place **vers 1990** (IBM **licence** la techno HP OpenView / NNM en **1990** et livre son NetView dérivé en **1992**). Le **milieu des années 90** est plutôt l’**apogée concurrentielle** du NMS Unix (OpenView vs SunNet Manager, bascule aussi vers Windows/NT annoncée ~1993–94) — moment où un port Unix de SAGE a du sens **commercialement**, sans coller à un « launch day » OpenView |
| Stations IBM / AIX | portage sur **AIX** | **RS/6000** + **AIX 3** annoncés **février 1990** (workstations *et* servers). AIX 3.2.x mature **1992–93**. Un port SAGE → AIX **milieu des années 90** est **plausible** (plateforme déjà installée chez les grands comptes) ; ce n’est pas l’année de naissance d’AIX |

Lecture courte (après croisement) :

```text
SAGE     → management system (ligne antérieure / non-« /X »)
SAGE/X   → runtime Unix (souvenir : ~mid-1990s)
         → porté ensuite / aussi sur IBM AIX (RS/6000)

Marché : OpenView déjà établi dès ~1990 ;
         mid-90s = pression concurrentielle NMS Unix + multi-plateforme,
         pas la date de première sortie OpenView.
```

Ne pas confondre **SAGE/X** (management sous Unix) avec **StarX25** (firewall
X.25) : le « X » de SAGE/X renvoie à **Unix**, pas à X.25.

#### Repères publics (hors Perform)

| Fait | Approx. | Source type |
|------|---------|-------------|
| IBM RS/6000 + AIX 3 | **fév. 1990** | encyclopédie / histoire produit IBM |
| IBM licence HP OpenView (NNM…) | **1990** | doc formation HP OpenView NNM (historique interne cité) |
| IBM NetView/6000 puis NetView for AIX | **1992** → renommages **1994** | IBM Systems Journal / presse technique |
| OpenView déjà cadre concurrent NT/Unix | **1993–94** | presse (HP / IBM / DEC vers NT) |
| OpenView cité comme leader face à SunNet Manager | **~1995** | littérature académique / marché NMS |

#### Statuts de preuve (corrigés)

| Élément | `source_status` |
|---------|-----------------|
| /X = Unix (nomenclature SAGE/X) | `personal_memory` / high |
| SAGE/X ~milieu des années 90 (Perform) | `personal_memory` / medium — **non contredit** par le calendrier public |
| « Sortie » OpenView au milieu des années 90 | **à reformuler** : OpenView est **antérieur** (~1990) ; mid-90s = **dominance / pression marché** (`public_trace` + nuance) |
| Port AIX sur machines IBM (RS/6000) | `personal_memory` / medium ; **plateforme disponible dès 1990** (`public_trace`) |
| Dates exactes SAGE/X, notes de version, supports Unix précis (HP-UX ? SunOS/Solaris ? AIX only ?) | `to_verify` |

### 4.1c Contexte normes : GDMO, CMIP/CMIS, SNMP

Même « époque » (fin des années 80 → milieu des années 90) : standardisation de la
**gestion de réseau**, avec **deux familles** qu’il ne faut pas fusionner.

| Sigle | Nom exact (public) | Rôle |
|-------|--------------------|------|
| **GDMO** | **Guidelines for the Definition of Managed Objects** (ISO/IEC 10165-4 / ITU-T X.722) | Notations / règles pour **définir des objets managés** (modèle d’information) — surtout monde **OSI / télécom** |
| **CMIP / CMIS** | Common Management Information Protocol / Service | Protocole / service de gestion **OSI** utilisant ces objets |
| **SNMP** | Simple Network Management Protocol | Gestion **TCP/IP** « simple » ; MIB, agents ; dominante pratique sur les réseaux IP |

**Nom :** le souvenir « Guidelines for the Management Of… » est **proche** mais
inexact. Le nom stabilisé est **Guidelines for the Definition of Managed
Objects** (définition des objets, pas « management of … » au sens titre).

**Chronologie publique (approx.) :**

| Moment | SNMP | GDMO / CMIP |
|--------|------|-------------|
| **1988–1990** | Premiers RFC SNMPv1 (**RFC 1065–1067**, 1988 ; suite **RFC 1155/1157**, 1990) | Cadre OSI de gestion d’objets en construction / formalisation (GDMO X.722 dans la famille ISO 10165) |
| **début → milieu des années 90** | SNMP déjà **déployé** largement ; SNMPv2 en débat / déploiement | GDMO/CMIP **matures** côté télécom ; coexistence concurrentielle avec SNMP dans les grands NMS |
| **Produits type OpenView / NetView** | Fortement **SNMP** (NNM) | Certaines briques / licences **CMIP** aussi (ex. IBM licence techno HP incluant NNM + CMIP, ~1990) |

**Lecture pour Perform / SAGE :**

```text
SAGE (hétérogène, X.25, émulation, …)
  → évolue dans un marché où
     SNMP  = plan IP « simple » dominant chez beaucoup de clients data
     GDMO/CMIP = plan objets managés OSI / opérateurs télécom
SAGE/X (Unix, mid-90s)
  → coïncide avec la maturité concurrentielle des NMS multi-standards
    (OpenView, NetView, SunNet Manager…), pas avec « l’invention » de SNMP
```

**Nuance mémoire :** SNMP n’« apparaît » pas au milieu des années 90 — il
**apparaît fin des années 80** et est déjà le standard de facto IP au moment du
port Unix. Le mid-90s, c’est plutôt la **généralisation des plateformes NMS**
et le **choc SNMP vs CMIP/GDMO** dans les choix d’architecture.

| Élément | `source_status` |
|---------|-----------------|
| GDMO = *Guidelines for the Definition of Managed Objects* | `public_trace` / high |
| SNMP RFCs initiaux ~1988–1990 | `public_trace` / high |
| Coexistence SNMP / CMIP-GDMO dans les années 90 | `public_trace` / high |
| Lien exact produit SAGE ↔ GDMO ou SNMP (implémentation) | `to_verify` (archives Perform) |

### 4.1d Témoignage opérateur — CMIP vs réalité SAGE (DOS / DESQview)

Lecture **personnelle** (Perform), non monographie protocolaire :

**CMIP** était bien le **protocole** (avec CMIS le service ; GDMO le formalisme
des objets). Il y avait de **bonnes idées**, mais :

1. **Conceptuellement lourd** à s’approprier (au moins pour l’opérateur ici) ;
2. **Difficile à implémenter** sur les machines de l’époque (coût CPU / mémoire /
   complexité d’agent et de manager) ;
3. **Incompatible avec la contrainte base installée** : Perform avait une base
   **SAGE sous DOS / DESQview** **conséquente** — à l’échelle de la **France**
   et de ses **réseaux X.25 privés** du moins.

**DESQview** (souvenir orthographié « Deskview ») : couche **multitâche** sur
MS-DOS (Quarterdeck), qui permettait aussi de l’**IPC** (*Inter-Process
Communication*) entre processus/tâches — pas seulement du « time-slicing »
visuel. Pour un NMS type SAGE, c’était un **runtime applicatif** : plusieurs
composants (acquisition, IHM, traitements) pouvaient coexister et **échanger**,
toujours sous la pression des **640 Ko**.

```text
MS-DOS 640 Ko
  + DESQview  →  multitâche + IPC
  + SAGE      →  gestion d'équipements hétérogènes (souvent X.25)

Monde « standards OSI »     CMIP + GDMO  →  riches, lourds, peu réalistes
                                              sur ce parc
Monde « produit Perform »   livrer de la gestion qui tourne déjà chez le client
```

Cela éclaire pourquoi une maison comme Perform ne bascule pas « par pureté
architecturale » vers CMIP : la **dette de parc** (DOS/DESQview + X.25 privé
FR) et la **complexité d’implémentation** pèsent plus que l’élégance du modèle
OSI. Le passage **SAGE → SAGE/X (Unix)** est une autre réponse à la pression
marché (NMS Unix type OpenView), **sans** confondre pour autant avec une
adoption pleine CMIP.

| Élément | `source_status` |
|---------|-----------------|
| CMIP = protocole ; bonnes idées mais conceptuel + implémentation lourds | `personal_memory` / high (jugement d’acteur) |
| Base installée SAGE sous **DOS / DESQview** conséquente (FR, X.25 privés) | `personal_memory` / medium–high |
| **DESQview** = multitâche DOS **+ IPC** (souvenir « Deskview ») | `personal_memory` (rôle pour SAGE) / high ; produit Quarterdeck : `public_trace` |
| Périmètre commercial « France / X.25 privés » (pas Europe entière) | `personal_memory` / medium — à croiser chiffre d’affaires / listes clients |
| Guerre des **Ko** sous la barre **640 Ko** MS-DOS (mémoire conventionnelle) | `public_trace` / high (architecture PC) + `personal_memory` opérateur SAGE |

#### Mémoire conventionnelle 640 Ko — le climat technique

C’est l’époque où l’on se battait pour **grapiller quelques Ko** de plus sous
**MS-DOS**, sous la limite de la **mémoire conventionnelle (~640 Ko)** du PC
IBM-compatible (espace 0–640 Ko réservé au « conventional memory » ; au-delà :
UMB, HMA, **EMS** / **XMS**, chargeurs hauts, etc.).

Pour un produit comme **SAGE sous DOS/DESQview**, chaque Ko comptait :
overlays, drivers réseau, stack X.25, multitâche DESQview, buffers — le
« système d’aide à la gestion » devait **tenir** dans un budget mémoire
ridicule par les standards d’aujourd’hui. Dans ce climat, un modèle **CMIP/GDMO**
lourd n’était pas seulement « conceptuellement compliqué » : il était souvent
**incompatible avec le plafond matériel** du parc client.

```text
640 Ko MS-DOS   →  contrainte physique / architecture
DESQview        →  multitâche + IPC dans ce plafond
SAGE FR X.25    →  produit qui doit tourner là, pas sur une station de rêve
CMIP            →  bonne architecture papier, mauvais rapport coût/bénéfice
                   sur ce parc
```

### 4.1e Emul — langage d’émulation d’opérateur (et LinkOS)

**Emul** : langage développé par l’opérateur (JHR) pour **émuler un opérateur**
devant écran/clavier d’équipements (interfaces textuelles, alarmes, événements)
— le bras programmable du plan **SAGE** « hétérogène ».

| Phase | Implémentation | Notes |
|-------|----------------|-------|
| 1 | **Turbo Prolog** | première version du langage Emul |
| 2 | **C / C++** | réécriture / production ; **noyau multitâche déjà baptisé LinkOS** |
| Suite | **LinkOS** évolue | même fil de noyau léger multitâche |
| Contemporain | dépôt **[l8](https://github.com/JeanHuguesRobert/l8)** | multitâche coopératif JS (Tasks/Steps) — *descendant attesté* de la lignée LinkOS ; suite runtime : Inox / l9, COP (inseme) |

```text
Emul (Turbo Prolog)
  → Emul (C/C++) + noyau multitâche LinkOS
    → LinkOS (évolution continue)
      → l8 (JS) → bridges COP / Inox (l9)
```

DESQview (multitâche + IPC sous DOS) et **LinkOS** (noyau multitâche *dans*
l’écosystème Emul/C) ne se confondent pas : l’un est le **runtime d’hôte**
du parc client DOS ; l’autre est le **noyau d’orchestration** porté par le
code Emul puis par la lignée l8.

| Élément | `source_status` |
|---------|-----------------|
| Emul d’abord en Turbo Prolog, puis C/C++ | `personal_memory` / high |
| LinkOS déjà présent comme noyau multitâche dans la phase C/C++ d’Emul | `personal_memory` / high |
| Continuité LinkOS → l8 (et au-delà) | `personal_memory` + `repository_trace` (l8 README / lignée COP-Inox) / medium–high |
| Code source Emul Turbo Prolog / C d’époque | `to_verify` (archives) |

### 4.2 StarX25 — surface technique

**StarX25** : produit **pare-feu X.25** (*X.25 Firewall*). Dans le corpus
capacitaire on le décrit aussi comme passerelle de sécurité (authentification,
call deflection, éventuel langage embarqué) : ce sont des **mécanismes**
possibles du produit firewall, pas un autre produit.

| Élément | `source_status` |
|---------|-----------------|
| SAGE = *Système d'Aide à la Gestion d'Equipements hétérogènes* ; StarX25 = X.25 Firewall | `personal_memory` (opérateur) / high |
| Mécanismes détaillés StarX25 (call deflection, etc.) | `to_verify` / medium |

### 4.3 Insight commercial (rétrospectif) — surtout SAGE

L’avantage concurrentiel affiché du **management** multi-vendeur : le client
peut **gérer** un parc **hétérogène**, donc n’est pas captif d’un seul
constructeur d’équipements.

Formulation plus nette, reconnue **après coup** :

> On ne vendait pas seulement un outil de supervision.  
> On vendait au client un **pouvoir de négociation** :  
> *« nous pouvons faire coexister vos équipements et ceux de vos concurrents ;
> vous n’êtes plus obligés de céder au vendeur qui verrouille le réseau. »*

Autrement dit : le logiciel est le **véhicule** ; le **cargo** est la capacité
de dire *we don’t care which vendor* — sans perdre la capacité d’opérer.

StarX25 renforce le même écosystème côté **frontière de confiance** (qui entre
sur le réseau X.25), sans se confondre avec le plan de gestion SAGE.

| Élément | `source_status` |
|---------|-----------------|
| Indépendance multi-vendeur comme argument produit SAGE | `personal_memory` + indices `public_trace` / medium–high |
| Lecture « pouvoir de négociation » comme insight commercial retardé | `personal_memory` / medium (interprétation d’acteur) |
| Périmètre exact clients / contrats SAGE vs StarX25 | `to_verify` |

## 5. Deux moitiés d’une même doctrine

```text
FixBugsFirst          →  maîtrise de l'entropie interne (dette, features hors contrôle)
Indépendance vendeur  →  maîtrise du graphe de dépendances externes (lock-in)
         ↓
   rester capable de choisir ;
   ne pas devenir captif d'un treadmill de features
   ni d'un fournisseur unique.
```

C’est la même logique capacitaire que la lignée Forth → LinkOS → Star X25 →
Sage/X → … → FractaNet, lue sur le **plan produit et marché**, pas seulement
sur le plan protocole.

## 6. Réplication contemporaine (lecture, non preuve d’identité)

| Alors (Perform / SAGE) | Maintenant (corpus) |
|------------------------|---------------------|
| Équipements X.25 hétérogènes | Modèles, agents, hôtes, dépôts, fournisseurs hétérogènes |
| Plan de gestion neutre | Corpus + contrats + routage (Cogentia / Magistral) |
| Client non captif d’un constructeur | Opérateur non captif d’un LLM / d’un agent / d’une machine |
| « Nous gérons l’hétérogène » | Failover, map multi-nœuds, gateway multi-CLI, politiques d’embedding explicites |
| FixBugsFirst maison produit | Operium : registre Bug/Feature + gate de sous-système |

**Prudence :** la réplication est une **lecture de continuité**. Elle n’implique
pas que Cogentia « soit » SAGE, ni que le marché 2026 soit le marché X.25 des
années 1990.

## 7. Ce qu’il reste à documenter (chantier historique)

- [ ] Archives Perform (statuts, brochures, manuels Sage/X / Star X25 / DashBoard)
- [ ] Citations exactes des traces publiques déjà repérées (profils, presse, BMC)
- [ ] Chronologie fine 1987 → produits → cession 1997 → Odisei
- [ ] Témoignages (associés, clients, Jean Vincent, etc.) avec consentement
- [ ] Lien éventuel brevets / dépôts de marques

## 8. Règle pour les agents

```text
souvenir personnel  ≠  fait historique publié
insight commercial  ≠  claim marketing actuel
doctrine Operium    ≠  monographie Perform
```

Lorsqu’on cite cette note hors barons-Mariani, renvoyer ici pour le **contexte
historique**, et vers Operium pour la **pratique Fix Bugs First d’aujourd’hui**.
