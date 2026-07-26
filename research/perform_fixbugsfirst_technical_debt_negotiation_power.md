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
| **SAGE** (Sage/X, + Emul) | **Management system** — gestion / supervision de réseaux hétérogènes (souvent privés **X.25**) |
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
