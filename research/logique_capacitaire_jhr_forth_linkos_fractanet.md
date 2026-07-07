---
title: "Logique capacitaire — de Forth, LinkOS et X.25 à FractaNet"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-07-07"
status: "draft"
document_role: "source_doctrinale_pivot"
document_kind: "grille-de-lecture"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
related_documents:
  - "research/baron_mariani_singulier_pluriel_agents_jhn.md"
  - "research/lineages/forth_linkos_starx25_sagex_odisei_fractanet.yaml"
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

# Logique capacitaire — de Forth, LinkOS et X.25 à FractaNet

## Statut

Ce document est une grille de lecture prioritaire pour interpréter la trajectoire technique, politique et doctrinale de Jean Hugues Noël Robert, baron Mariani.

Il ne doit pas être lu comme une autobiographie complète, ni comme une revendication de priorité historique. Il fixe une logique récurrente : la transformation de contraintes en capacités par interposition de systèmes programmables, vérifiables et délégables.

## Thèse centrale

Depuis les premières expérimentations autour de Forth, du Kaypro II, du Minitel, de LinkOS, de Star X25, de Sage/X, d'Odisei et jusqu'à FractaNet, une même logique apparaît :

> transformer des contraintes en capacités par l'interposition d'un système programmable, vérifiable et délégable.

Nom proposé : **possibilisme capacitaire**.

Cette logique n'est pas seulement informatique. Elle relie logiciel, réseau, souveraineté, contrôle, transmission et autonomie de capacité.

## Motif récurrent

Le schéma récurrent est le suivant :

1. une contrainte matérielle, institutionnelle, territoriale ou cognitive est rencontrée ;
2. cette contrainte est abstraite sous forme de problème de système ;
3. un langage, un protocole, un noyau, une passerelle ou une couche d'orchestration est introduit ;
4. cette couche permet de déléguer des actes à des machines, programmes, agents ou institutions ;
5. cette délégation doit rester explicite, traçable, révocable, supervisable et corrigible ;
6. la capacité ainsi produite doit pouvoir être transmise, répliquée et augmentée.

```text
contrainte subie
→ abstraction logicielle ou protocolaire
→ langage / noyau / passerelle
→ délégation contrôlée
→ supervision
→ correction
→ autonomie accrue
→ transmission
```

## Ligne personnelle de la logique capacitaire

### Forth sur VIC-20

Forth apporte une idée fondatrice : une machine limitée peut devenir extensible si elle reçoit un langage compact, interactif, enrichissable par dictionnaire de mots.

Le point n'est pas seulement le langage. C'est la possibilité d'augmenter la machine depuis l'intérieur.

### Kaypro II, BIOS et Minitel

Le désassemblage du BIOS du Kaypro II pour rediriger écran et clavier vers la liaison série, elle-même reliée à un Minitel par montage électronique, manifeste une opération fondamentale : découpler l'interface, la machine et le réseau.

```text
machine locale
→ redirection des E/S
→ liaison série
→ Minitel
→ réseau télématique
```

Ce geste annonce une logique de virtualisation de l'interface utilisateur et de détournement capacitaire des machines disponibles.

### Projet serveur Minitel multiprocesseur 6809

À l'été 1986 environ, le projet mené avec Jean Vincent en Normandie visait un serveur Minitel multiprocesseur à base de 6809 : Jean Vincent au hardware, Jean Hugues au software.

Même non abouti, ce projet doit être lu comme une tentative précoce de construire une petite infrastructure télématique multi-session spécialisée.

### LinkOS

LinkOS constitue le noyau personnel de cette généalogie : tâches légères, multitâche, langage embarqué, système contraint, coopération entre unités d'exécution.

L'étude de Minix en IUT et la tentative d'une version de LinkOS avec appels système de type Unix, sur 80286, avec un souvenir de fork/exec fonctionnel mais arrêt avant mémoire virtuelle, montrent une ambition Unix-like partielle : processus, lancement contrôlé, séparation noyau / utilisateur, orchestration.

### Star X25

Star X25, conçu par Jean Vincent et fortement influencé par Jean Hugues, embarquait un langage de programmation et une version de LinkOS. Il utilisait la call deflection X.25 après identification / authentification de l'utilisateur.

Il ne faut donc pas le réduire à un « firewall X.25 ». Il s'agit plutôt d'une passerelle programmable de sécurité et de routage X.25 : authentification, décision, déflexion, délégation d'accès.

### Sage/X et Emul

Sage/X prolonge la logique vers la supervision de réseaux hétérogènes. Emul, langage inspiré de Smalltalk, permettait d'émuler un utilisateur derrière écran/clavier pour interagir avec les interfaces textuelles d'équipements hétérogènes recevant et émettant alarmes, événements ou états.

Le motif devient : parler aux systèmes tels qu'ils existent déjà, puis les rendre supervisables et actionnables.

### DashBoard

DashBoard marque le passage vers IP, SNMP, Cisco, Internet et Java. Il traduit la logique Sage/X dans un environnement où SNMP apparaît comme standard probable de gestion de réseau.

La continuité est claire : supervision, standardisation, intégration, vue opérationnelle.

### Odisei

Odisei déplace la logique vers la téléphonie IP logicielle : l'appel devient un service programmable, routable, découvrable, orchestrable.

On passe d'un réseau d'équipements administrés à un réseau de services logiciels distribués.

### l8 et FractaNet

l8 est à lire comme un descendant contemporain de LinkOS.

FractaNet est l'extension territoriale de cette même logique : non plus seulement un noyau pour orchestrer des processus sur une machine, mais un noyau distribué pour transformer des ressources locales dispersées en capacité collective vérifiable.

## FractaNet comme généralisation

FractaNet transpose la logique système à l'échelle territoriale :

```text
processus
→ agents

machines
→ ressources locales

ordonnanceur
→ orchestration énergétique / computationnelle / civique

appels système
→ mandats explicites

journaux
→ traçabilité publique

fork/exec
→ instanciation contrôlée d'agents
```

Les objets orchestrés ne sont plus seulement des programmes :

- panneaux solaires ;
- batteries ;
- nœuds de compute ;
- agents logiciels ;
- données ;
- mandats ;
- associations ;
- institutions ;
- actes publics ;
- flux énergétiques ;
- flux économiques.

## Règle d'interprétation pour le jumeau numérique

Lorsqu'un projet de Jean Hugues Noël Robert semble dispersé, hybride ou excessivement large, il faut d'abord chercher s'il applique le motif suivant :

> rendre capable un acteur limité, sans le déposséder du contrôle sur ce qui agit pour lui.

Cette règle vaut pour les projets techniques, politiques, énergétiques, associatifs, documentaires et démocratiques.

## Lien avec l'Autonomie de Capacité

L'Autonomie de Capacité est la traduction politique de cette logique.

Elle ne demande pas seulement davantage de compétences formelles. Elle demande des capacités effectives : énergie, compute, agents, corpus, mandats, outils de contrôle, preuve des actes, infrastructures d'exécution.

```text
autonomie de papier
→ compétence formelle sans puissance garantie

autonomie de capacité
→ moyens vérifiables d'agir, de contrôler et de transmettre
```

## Point de vigilance

Cette grille ne doit pas être interprétée comme une plainte rétrospective.

La bonne lecture est :

> certaines structures avaient été identifiées tôt ; les conditions actuelles permettent de les reprendre à un niveau plus élevé, plus ouvert, plus transmissible et plus collectif.

Il ne s'agit pas de refaire le passé.

Il s'agit de faire mieux maintenant.

## Formule canonique

> Depuis Forth, LinkOS, Star X25, Sage/X et Odisei jusqu'à FractaNet, une même logique travaille : prendre des systèmes contraints, fermés ou hétérogènes ; y introduire un langage, un protocole et une couche d'orchestration ; permettre à des agents humains ou logiciels d'agir par délégation contrôlée ; puis rendre ces actes observables, vérifiables et corrigibles. FractaNet est la généralisation territoriale de cette logique : non plus seulement un système d'exploitation pour machines, mais un système d'exploitation pour capacités locales.

## Données à stabiliser

Les éléments suivants relèvent à ce stade du témoignage personnel et doivent être croisés avec d'éventuelles sources :

- dates exactes du projet serveur Minitel 6809 ;
- statut et traces de LinkOS ;
- relation exacte entre LinkOS et l8 ;
- traces de Star X25 / StarWall ;
- documentation Emul ;
- chronologie Perform / DashBoard / Odisei ;
- rôle précis des personnes citées dans chaque bifurcation.
