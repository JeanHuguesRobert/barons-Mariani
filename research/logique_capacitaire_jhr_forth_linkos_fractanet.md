---
title: "Logique capacitaire — de Forth et LinkOS à FractaNet"
subtitle: "Grille de lecture technique, doctrinale et autobiographique"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-07"
last_modified_at: "2026-09-05"
version: "0.2"
status: "draft v0.2"
document_role: "source"
document_kind: "conceptual-lineage"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
related_repositories:
  - "JeanHuguesRobert/cogentia"
  - "JeanHuguesRobert/FractaVolta"
  - "JeanHuguesRobert/Inox"
  - "JeanHuguesRobert/marenostrum"
related_documents:
  - "cogentia/research/learning_computer_genese_et_architecture.md"
  - "research/principe_rossignol.md"
  - "research/jhn_architecture.md"
  - "https://github.com/JeanHuguesRobert/l8"
  - "https://github.com/JeanHuguesRobert/side"
tags:
  - logique-capacitaire
  - possibilisme-capacitaire
  - forth
  - linkos
  - star-x25
  - sage-x
  - odisei
  - l8
  - side-js
  - packet-closure
  - learning-computer
  - fractanet
  - agents-jhn
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "explicit-metadata"
classification_confidence: "high"
legacy_document_role: "doctrine"
changelog:
  - "2026-07-07 — draft v0.1: première cartographie de la logique capacitaire de Forth/LinkOS à FractaNet."
  - "2026-09-05 — draft v0.2: propagation Issue #55; insertion des jalons pivots majeurs l8 (2014) et side.js (2016) entre Odisei et FractaNet, formalisation du germe du Packet Closure et du non-bloquant synchrone vers le Learning Computer."
---

# Logique capacitaire — de Forth et LinkOS à FractaNet

## 1. Statut

Ce document est une grille de lecture prioritaire pour interpréter la trajectoire technique, politique et doctrinale de Jean Hugues Noël Robert, baron Mariani.

Il ne doit pas être lu comme une autobiographie complète, ni comme une revendication de priorité historique. Il sert à identifier une logique récurrente à l'œuvre dans plusieurs projets successifs.

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
→ langage ou noyau
→ délégation contrôlée
→ supervision
→ correction
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
→ Star X25, passerelle programmable X.25 avec authentification et call deflection
→ Sage/X et Emul, supervision programmable d'équipements hétérogènes
→ DashBoard, transition SNMP/IP/Java/Web
→ Odisei, téléphonie IP logicielle et services distribués
→ l8 (2014), Tasks, Steps, algèbre de Promises avec cancel, et germe du Packet Closure
→ side.js (2016), non-bloquant en style synchrone, retry from top et cache de slots en RAM
→ FractaNet, généralisation territoriale de cette logique
```

## 5. Tableau de correspondance

| Épisode | Contrainte | Geste technique | Capacité créée |
|---|---|---|---|
| VIC-20 / Forth | machine limitée | langage extensible | programmer l'environnement |
| Kaypro II / BIOS | E/S figées | redirection écran-clavier | découpler machine et interface |
| Minitel | terminal supposé passif | usage comme périphérique réseau | transformer un terminal en accès télématique |
| Serveur 6809 | faibles moyens | multiprocesseur spécialisé | servir plusieurs sessions |
| LinkOS | machine nue | noyau multitâche | orchestrer des tâches |
| LinkOS / Unix | OS à reconstruire | fork/exec, appels système | exécuter et déléguer des processus |
| Star X25 | réseau fermé ou risqué | authentification + call deflection | accès conditionnel contrôlé |
| Sage/X / Emul | équipements hétérogènes | langage d'émulation et supervision | agir sur des systèmes disparates |
| DashBoard | bascule Internet | SNMP, Java, Web | supervision réseau IP orientée performance |
| Odisei | téléphonie en mutation | IP-PBX logiciel | transformer l'appel en service programmable |
| l8 (2014) | asynchronisme éclaté et acteurs distribués | Tasks, Steps, algèbre de Promises étendue avec `cancel`, closures sérialisées pour acteurs | composer dynamiquement des graphes de calcul et isoler l'état distribué (germe du *Packet Closure*) |
| side.js (2016) | latences I/O bloquantes et complexité des callbacks | style synchrone sur non-bloquant, retry from top sur exception, cache de slots en RAM (µs) et delayed writes | persistance ultra-rapide et tolérance aux pannes sans enfer asynchrone |
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

## 7. Star X25 et Sage/X

Star X25 ne doit pas être réduit à un simple firewall X.25.

Formulation plus juste :

> Star X25 était une passerelle programmable de sécurité et de routage X.25, construite autour d'une logique d'authentification, de déflexion d'appel et d'exécution embarquée.

Sage/X et Emul prolongent le même motif dans un autre domaine : la supervision et l'action sur des équipements hétérogènes.

Le point commun est la construction d'un médiateur programmable entre un opérateur humain et un monde technique dispersé.

## 8. Odisei comme bifurcation Internet

Odisei marque le passage du réseau transactionnel administré vers l'Internet des services logiciels distribués.

La téléphonie IP, l'IP-PBX, la découverte de serveurs et le routage logiciel d'appels prolongent la logique antérieure : l'appel devient programmable, routable, découvrable et orchestrable.

## 8.1 l8 (2014) comme matrice de contrôle et germe du Packet Closure

Développé en 2014, [`l8`](https://github.com/JeanHuguesRobert/l8) représente le chaînon pivot entre les noyaux multitâches locaux (LinkOS) et les protocoles distribués contemporains. 

Face à l'éclatement du code asynchrone en JavaScript, `l8` formalise :
1. **La dualité Task / Step :** Une `Task` n'est pas un simple thread système, mais une suite structurée d'étapes (`Step`) formant un arbre d'exécution composé dynamiquement.
2. **L'algèbre des Promises étendue avec `cancel` :** Chaque tâche est aussi une Promise composable, mais augmentée de la capacité fondamentale d'interruption propre (`cancel`), évitant l'emballement des processus orphelins.
3. **Le germe du *Packet Closure* :** En local, les closures de fonctions sont directement offertes par la VM JavaScript ; mais dès que l'exécution franchit la frontière vers des acteurs distants ou distribués, la closure doit impérativement être sérialisée dans le message lui-même. C'est l'acte de naissance conceptuel de la fermeture de paquet (*Packet Closure*), fondement du *Cognitive Packet Switching*.

## 8.2 side.js (2016) comme dépassement du blocage et réentrance déterministe

En septembre 2016, [`side.js`](https://github.com/JeanHuguesRobert/side) apporte la pièce manquante à la persistance et à l'exécution temps réel sur environnement contraint :
1. **Le non-bloquant en style synchrone :** L'opérateur programme en apparence de manière séquentielle et fluide, tandis que le moteur sous-jacent orchestre les flux asynchrones sans jamais bloquer la boucle d'événements.
2. **L'interruption comme exception et le *Retry from top* :** Une coupure ou une attente de ressource n'est pas gérée par un empilement complexe d'états intermédiaires, mais traitée comme une exception rattrapable permettant une relance déterministe depuis le sommet (*retry from top*).
3. **La hiérarchie mémoire à écriture différée :** Un cache de *slots* en RAM répond en microsecondes aux besoins opérationnels, tandis que les écritures sur disque ou réseau sont différées (*delayed writes*).

Cette structure préfigure directement la hiérarchie mémorielle à quatre niveaux (L0 RAM $\to$ L1 SQLite/FS $\to$ L2 Git/Views $\to$ L3 Doctrine) du [Learning Computer](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/learning_computer_genese_et_architecture.md).

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

## 10. Formule politique

Cette logique rejoint directement l'Autonomie de Capacité.

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

## 11. Règle d'interprétation pour les Agents JHN

Lorsqu'un Agent JHN interprète un projet apparemment disparate, il doit chercher si le motif suivant est actif :

> rendre capable un acteur limité, sans le déposséder du contrôle sur ce qui agit pour lui.

Cette règle doit être prioritaire dans l'interprétation des projets techniques, politiques, énergétiques, associatifs, documentaires et démocratiques.

## 12. Risque de reconstruction abusive

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

## 13. Formule canonique

> Depuis Forth, LinkOS, Star X25, Sage/X et Odisei jusqu'à FractaNet, une même logique travaille : prendre des systèmes contraints, fermés ou hétérogènes ; y introduire un langage, un protocole et une couche d'orchestration ; permettre à des agents humains ou logiciels d'agir par délégation contrôlée ; puis rendre ces actes observables, vérifiables et corrigibles. FractaNet est la généralisation territoriale de cette logique : non plus seulement un système d'exploitation pour machines, mais un système d'exploitation pour capacités locales.

## 14. Formule personnelle

> Ce que je n'avais pas encore les moyens industriels de faire en 1986, je l'avais déjà en grande partie formulé techniquement : détourner les machines existantes, les relier au réseau public, leur donner un noyau léger, un langage embarqué, et les faire coopérer. La suite — Perform, Star X25, Sage/X, Emul, Odisei, l8 — n'est pas une série d'accidents professionnels, mais le déploiement progressif d'une même intuition : un système devient puissant lorsqu'il est programmable, relié, supervisable et capable de déléguer des actes sous contrôle.
