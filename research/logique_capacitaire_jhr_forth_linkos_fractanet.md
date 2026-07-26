---
title: "Logique capacitaire — de Forth et LinkOS à FractaNet"
subtitle: "Grille de lecture technique, doctrinale et autobiographique"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-07"
last_modified_at: "2026-07-13"
status: "draft"
document_role: "doctrine"
document_kind: "conceptual-lineage"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
related_repositories:
  - "JeanHuguesRobert/cogentia"
  - "JeanHuguesRobert/FractaVolta"
  - "JeanHuguesRobert/Inox"
  - "JeanHuguesRobert/marenostrum"
tags:
  - logique-capacitaire
  - possibilisme-capacitaire
  - forth
  - linkos
  - star-x25
  - sage-x
  - odisei
  - fractanet
  - agents-jhn
---

# Logique capacitaire — de Forth et LinkOS à FractaNet

## 1. Statut

Ce document est une grille de lecture prioritaire pour interpréter la trajectoire technique, politique et doctrinale de Jean Hugues Noël Robert, baron Mariani.

Il ne doit pas être lu comme une autobiographie complète, ni comme une revendication de priorité historique. Il sert à identifier une logique récurrente à l'œuvre dans plusieurs projets successifs.

Les faits historiques détaillés et leurs niveaux de preuve doivent être séparés de cette grille doctrinale. La note associée est [`notes/source_technique_1980_2001.md`](notes/source_technique_1980_2001.md).

## 2. Thèse centrale

Depuis les premières expérimentations autour de Forth, du Kaypro II, du Minitel, de LinkOS, de Star X25, de Sage/X, d'Odisei et jusqu'à FractaNet, une même logique apparaît :

> transformer des contraintes en capacités par l'interposition d'un système programmable, vérifiable et délégable.

Cette logique peut être nommée :

> possibilisme capacitaire.

## 3. Motif récurrent

Le motif récurrent est le suivant :

```text
contrainte subie
→ abstraction logicielle ou protocolaire
→ langage, noyau, passerelle ou couche d'orchestration
→ délégation contrôlée
→ supervision
→ correction
→ autonomie accrue
→ transmission
```

Le but n'est pas seulement d'automatiser. Le but est de rendre capable.

Le but n'est pas seulement de déléguer. Le but est de déléguer sans perdre le contrôle.

## 4. Ligne technique personnelle

La ligne technique peut être lue ainsi :

```text
Forth sur VIC-20
→ redirection écran/clavier du Kaypro II vers la liaison série
→ connexion au Minitel par montage dédié
→ projet de serveur Minitel multiprocesseur 6809
→ LinkOS, noyau multitâche personnel
→ tentative Unix-like avec appels système et fork/exec sur 80286
→ StarX25, pare-feu X.25 (X.25 Firewall ; mécanismes : auth, call deflection, …)
→ SAGE (Système d'Aide à la Gestion d'Equipements hétérogènes) / Emul
→ SAGE/X (port Unix, mid-1990s ; puis AIX) — le /X = Unix, pas X.25
→ DashBoard, transition SNMP/IP/Java/Web
→ Odisei, téléphonie IP logicielle et services distribués
→ l8, descendant contemporain de LinkOS
→ FractaNet, généralisation territoriale de cette logique
```

Le projet de serveur Minitel multiprocesseur 6809 fut mené avec Jean Vincent, au moins dans le souvenir personnel disponible : Jean Vincent au matériel, Jean Hugues au logiciel. Ce point doit rester qualifié et documenté avant toute présentation historique définitive.

## 5. Tableau de correspondance

| Épisode | Contrainte | Geste technique | Capacité créée |
|---|---|---|---|
| VIC-20 / Forth | machine limitée | langage extensible | programmer l'environnement |
| Kaypro II / BIOS | E/S figées | redirection écran-clavier | découpler machine et interface |
| Minitel | terminal supposé passif | usage comme périphérique réseau | transformer un terminal en accès télématique |
| Serveur 6809 | faibles moyens | multiprocesseur spécialisé | servir plusieurs sessions |
| LinkOS | machine nue | noyau multitâche | orchestrer des tâches |
| LinkOS / Unix | OS à reconstruire | fork/exec, appels système | exécuter et déléguer des processus |
| StarX25 | frontière X.25 non fiable | pare-feu X.25 (auth, call deflection, …) | accès conditionnel contrôlé |
| SAGE / Emul | équipements hétérogènes | *Système d'Aide à la Gestion d'Equipements hétérogènes* + Emul | superviser et agir sur des systèmes disparates |
| DashBoard | bascule Internet | SNMP, Java, Web | supervision réseau IP orientée performance |
| Odisei | téléphonie en mutation | IP-PBX logiciel | transformer l'appel en service programmable |
| FractaNet | dépendance territoriale | réseau distribué capacitaire | autonomie locale vérifiable |

## 6. LinkOS comme matrice

LinkOS n'est pas seulement un ancien noyau multitâche. Il doit être interprété comme une matrice conceptuelle : petites unités d'exécution, tâches autonomes, communication, langage embarqué, réseau, supervision et contrôle.

La continuité avec l8 et FractaNet n'est donc pas seulement technique. Elle est architecturale.

```text
LinkOS ancien
→ tâches légères coopérantes
→ langage embarqué
→ environnement contraint
→ réseau
→ supervision
→ l8 / agents actuels
→ FractaNet
```

Le souvenir d'une tentative Unix-like sur 80286, avec des appels système de type Unix et un couple fork/exec possiblement fonctionnel avant l'arrêt du projet au seuil de la mémoire virtuelle, doit être conservé comme témoignage à vérifier, non comme fait externe déjà établi.

## 7. StarX25 et SAGE (deux produits)

Distinction d’opérateur (à conserver) :

```text
StarX25  = the X.25 Firewall
SAGE     = Système d'Aide à la Gestion d'Equipements hétérogènes
```

**StarX25** est le produit **pare-feu X.25**. Les mécanismes techniques
rapportés ailleurs (authentification, call deflection, éventuel langage
embarqué) sont des **moyens** de ce firewall / de cette passerelle de
sécurité — pas une invitation à le renommer « autre chose que firewall ».

**SAGE** est le **Système d’Aide à la Gestion d’Equipements hétérogènes** —
le *management system*. L’acronyme encode déjà la promesse produit (aide à
gérer l’**hétérogène**). Emul prolonge ce plan : émuler un opérateur derrière
écran et clavier pour interagir avec les interfaces textuelles d’équipements
(alarmes, événements, états).

**SAGE/X** : le **/X** désigne la version qui **tourne sous Unix** (souvenir :
milieu des années 1990), puis portée sur **IBM AIX** (RS/6000). Ce « X » n’est
**pas** celui de X.25 (produit distinct : **StarX25**).

**Vérification 2026-07-26 (calendrier public) :** OpenView / NNM n’est pas une
« sortie » milieu des années 90 — la techno est déjà en place **vers 1990**
(licence IBM sur OpenView/NNM HP en 1990 ; NetView/6000 dès ~1992). Le mid-90s
correspond plutôt à l’**apogée concurrentielle** des NMS Unix. Les stations
**AIX/RS/6000** existent depuis **février 1990** : un port AIX mid-90s est
plausible. Détail et sources : note Perform §4.1b.

Le point commun reste le médiateur programmable entre un opérateur humain et
un monde technique dispersé — mais **sur deux plans produit** : frontière
(StarX25) vs pilotage (SAGE).

### 7.1 Perform, FixBugsFirst, pouvoir de négociation (lecture historique)

Le cadre **Perform** (Aix-en-Provence, 1987–1997) porte deux apports à ne pas
écraser dans la seule fiche produit :

1. **FixBugsFirst** — pratique de reprise de contrôle face à ce qui s’appellera
   plus tard *technical debt* : arrêter le treadmill de features, tenir un
   suivi Bug/Feature, réparer d’abord. Traces publiques sur le c2 ; note
   historique dédiée.
2. **Insight commercial SAGE** — l’indépendance multi-vendeur du *management
   system* n’était pas seulement une prouesse d’intégration : elle vendait au
   client un **pouvoir de négociation** face aux constructeurs (« nous gérons
   l’hétérogène »). StarX25 couvre le volet firewall du même écosystème.

La note-source historique (faits, statuts de preuve, prudence) est
[`perform_fixbugsfirst_technical_debt_negotiation_power.md`](perform_fixbugsfirst_technical_debt_negotiation_power.md).
La suite **opérationnelle** contemporaine de Fix Bugs First vit dans Operium
(`docs/fix-bugs-first.md`, `backlog/`). La lecture de continuité vers
Cogentia (indépendance multi-fournisseur / multi-agent) est une **interprétation**,
pas une identité historique.

## 8. Odisei comme bifurcation Internet

Odisei marque le passage du réseau transactionnel administré vers l'Internet des services logiciels distribués.

La téléphonie IP, l'IP-PBX, la découverte de serveurs et le routage logiciel d'appels prolongent la logique antérieure : l'appel devient programmable, routable, découvrable et orchestrable.

## 9. FractaNet comme généralisation territoriale

FractaNet n'est pas une rupture. C'est la généralisation territoriale du motif.

Avant :

```text
machine personnelle
→ terminal
→ réseau X.25
→ serveur
→ supervision
→ téléphonie IP
```

Maintenant :

```text
territoire
→ énergie
→ compute
→ agents
→ corpus
→ services
→ gouvernance
```

FractaNet vise à transformer un territoire dépendant en système capable, en reliant énergie locale, calcul distribué, agents logiciels, corpus versionné et contrôle démocratique dans une infrastructure ouverte, vérifiable et reproductible.

## 10. Analogie du système d'exploitation territorial

La généralisation peut être représentée par une correspondance entre les objets d'un système d'exploitation et ceux d'une infrastructure territoriale capacitaire :

```text
processus
→ agents

machines
→ ressources locales

ordonnanceur
→ orchestration énergétique, computationnelle et civique

appels système
→ mandats explicites

journaux
→ traçabilité publique ou gouvernée

fork/exec
→ instanciation contrôlée d'agents

permissions
→ capacités, interdictions et révocations
```

Les objets orchestrés ne sont plus seulement des programmes :

- panneaux solaires ;
- batteries ;
- nœuds de calcul ;
- agents logiciels ;
- données ;
- mandats ;
- associations ;
- institutions ;
- actes publics ;
- flux énergétiques ;
- flux économiques.

Cette analogie n'affirme pas qu'un territoire est littéralement un ordinateur. Elle sert à transférer des exigences éprouvées de séparation, d'ordonnancement, de contrôle, de journalisation et de révocation vers une infrastructure distribuée.

## 11. Formule politique : autonomie de papier et autonomie de capacité

Cette logique rejoint directement l'Autonomie de Capacité.

```text
autonomie de papier
→ compétence formelle sans puissance garantie

autonomie de capacité
→ moyens vérifiables d'agir, de contrôler, de corriger et de transmettre
```

Un système devient émancipateur lorsqu'il permet à des acteurs limités d'agir au-delà de leurs moyens immédiats, sans perdre le contrôle de ce qui agit pour eux.

Donc :

```text
pas seulement communiquer
→ agir

pas seulement agir
→ déléguer

pas seulement déléguer
→ contrôler

pas seulement contrôler
→ apprendre

pas seulement apprendre
→ transmettre
```

## 12. Règle d'interprétation pour les Agents JHN

Lorsqu'un Agent JHN interprète un projet apparemment disparate, il doit chercher si le motif suivant est actif :

> rendre capable un acteur limité, sans le déposséder du contrôle sur ce qui agit pour lui.

Cette règle doit être prioritaire dans l'interprétation des projets techniques, politiques, énergétiques, associatifs, documentaires et démocratiques.

## 13. Risque de reconstruction abusive

Il faut éviter une reconstruction trop linéaire.

La bonne lecture n'est pas :

```text
un grand plan continu déjà entièrement conçu
```

La bonne lecture est :

```text
intuition récurrente
→ prototypes
→ bifurcations
→ contraintes matérielles
→ contraintes économiques
→ reprises industrielles partielles
→ oubli historique
→ redécouverte conceptuelle actuelle
```

Cette prudence rend la lignée plus crédible.

Il ne s'agit pas de refaire le passé ni de transformer chaque souvenir en priorité historique.

Il s'agit de reconnaître des structures récurrentes afin de faire mieux maintenant, à un niveau plus ouvert, plus collectif et plus transmissible.

## 14. Formule canonique

> Depuis Forth, LinkOS, Star X25, Sage/X et Odisei jusqu'à FractaNet, une même logique travaille : prendre des systèmes contraints, fermés ou hétérogènes ; y introduire un langage, un protocole et une couche d'orchestration ; permettre à des agents humains ou logiciels d'agir par délégation contrôlée ; puis rendre ces actes observables, vérifiables et corrigibles. FractaNet est la généralisation territoriale de cette logique : non plus seulement un système d'exploitation pour machines, mais un système d'exploitation pour capacités locales.

## 15. Formule personnelle

> Ce que je n'avais pas encore les moyens industriels de faire en 1986, je l'avais déjà en partie formulé techniquement : détourner les machines existantes, les relier au réseau public, leur donner un noyau léger, un langage embarqué et les faire coopérer. La suite — Perform, Star X25, Sage/X, Emul, Odisei, l8 — peut être lue non comme un plan prédéterminé, mais comme le déploiement progressif et discontinu d'une même intuition : un système devient puissant lorsqu'il est programmable, relié, supervisable et capable de déléguer des actes sous contrôle.

## 16. Données à stabiliser

Les éléments suivants relèvent encore, totalement ou partiellement, du témoignage personnel, d'une interprétation ou de traces à relier :

- dates exactes et participants du projet serveur Minitel 6809 ;
- statut, chronologie et traces de LinkOS ;
- réalité exacte du couple fork/exec et état du projet 80286 ;
- relation entre LinkOS et l8 ;
- documentation de Star X25 / StarWall, de son langage embarqué et de la call deflection ;
- documentation d'Emul et de Sage/X ;
- chronologie Perform / DashBoard / Odisei ;
- rôle précis de Jean Vincent, Frédéric Artru et des autres personnes citées ;
- liens entre les traces publiques, les dépôts GitHub et les archives personnelles.

Ces éléments doivent être complétés dans la note-source, avec un statut de preuve et un niveau de confiance explicites.
