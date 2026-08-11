---
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
title: "État de droit assisté par ordinateur"
subtitle: "Démocratie assistée, souveraineté, traçabilité des actes et anti-capture"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-08-09"
status: "draft — source document, human validation required"
version: "0.1-draft"
license: "CC BY-SA 4.0"
language: "fr"
repository: "barons-Mariani"
path: "research/etat_de_droit_assiste_par_ordinateur.md"
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
human_validation_required: true
related_documents:
  - "research/justice_divine_mandat_implicite.md"
  - "research/invidia.md"
  - "research/traceabilite_des_actes.md"
  - "research/mandated_fast_democracy.md"
  - "research/la_democratie_spectaculaire.md"
  - "FractaVolta/research/fractalog.md"
  - "FractaVolta/research/traceable_governance.md"
  - "inseme/research/cop_fractalog_profile.md"
related_projects:
  - "Cogentia"
  - "Kudocracy"
  - "FractaVolta"
  - "Inseme"
  - "Autonomie de Capacité"
tags:
  - etat-de-droit
  - democratie-assistee
  - souverainete
  - anti-capture
  - mandat
  - traceabilite
  - fractalog
  - journal-officiel
  - registres
  - accountability
  - recours
  - intentions
---

# État de droit assisté par ordinateur

## Démocratie assistée, souveraineté, traçabilité des actes et anti-capture

> **Un État de droit assisté par ordinateur au service d’une démocratie tout autant assistée.**

## 0. Statut du texte

Ce document consolide une exploration du 9 août 2026 autour des Cogentia Digital Twins, de FractaLog, des registres institutionnels et de la démocratie assistée par ordinateur. Il constitue un **draft source** : il organise les idées, formule des invariants candidats et indique les raccords à effectuer avec les documents plus spécialisés du corpus. Il ne remplace ni FractaLog, ni les textes sur la démocratie, ni ceux sur le mandat et la traçabilité des actes.

La découverte centrale n’est pas que l’intelligence artificielle aurait besoin de règles particulières. Elle est plus générale : les systèmes agentiques rendent techniquement explicites des exigences — mandat, compétence, traçabilité, révocabilité, recours, séparation des fonctions — qui valent tout autant pour les agents humains et les personnes morales dès lors qu’ils exercent des pouvoirs comparables.

---

## 1. Deux objets distincts : démocratie et État de droit

L’État de droit n’est pas synonyme de démocratie.

La **démocratie** traite de l’origine et de la formation du pouvoir : qui est souverain, comment la volonté collective est formée, comment elle est exprimée, déléguée, contrôlée et reprise.

L’**État de droit** traite des conditions d’exercice du pouvoir : compétence, mandat, procédure, preuve, contrôle, contestation, correction et responsabilité.

Un régime peut donc être juridiquement très réglé sans être démocratique ; inversement, une majorité démocratiquement constituée peut exercer un pouvoir arbitraire si les garanties de l’État de droit sont insuffisantes.

L’architecture recherchée est hiérarchisée ainsi :

```text
Souveraineté populaire
        ↓
Démocratie assistée
        ↓
formation de la volonté collective
        ↓
Constitution / règles fondamentales
        ↓
État de droit assisté
        ↓
compétences / mandats / procédures
        ↓
actes
        ↓
preuves / registres / comptabilités / publications
        ↓
contrôle / contradiction / recours
        ↓
correction / révocation / compensation
        ↓
retour vers le souverain
```

L’assistance informatique doit augmenter la capacité du souverain à contrôler ses mandataires, jamais augmenter la capacité des mandataires à contrôler le souverain.

---

## 2. Le Digital Twin comme institution

Un Cogentia Digital Twin suffisamment autonome ne doit plus être conçu seulement comme un programme complexe. Il devient une **institution durable** : il possède une identité, une histoire, des mandats, des capacités, des sous-agents, des ressources, des obligations, des procédures de succession et des mémoires faisant foi.

Cette qualification ouvre un vaste champ de réemploi : les sociétés humaines ont accumulé des siècles d’ingénierie institutionnelle autour de la délégation, de la preuve, de la publicité, de la comptabilité, de la responsabilité, du recours et de la succession.

La méthode proposée est celle d’un **fork institutionnel** :

```text
institution humaine éprouvée
        ↓
identifier sa fonction utile
        ↓
séparer fonction et contingence historique
        ↓
repérer les mécanismes de capture
        ↓
conserver les invariants utiles
        ↓
rendre règles et preuves machine-readable
        ↓
ajouter traçabilité, révocabilité, subsidiarité et anti-capture
```

Il ne s’agit donc pas de numériser servilement l’État existant, mais d’extraire une bibliothèque de primitives institutionnelles réutilisables.

---

## 3. FractaLog n’est pas le Journal Officiel

Une distinction architecturale est centrale : **FractaLog est le substrat événementiel et probatoire ; les registres et publications officielles en sont des projections spécialisées.**

La comparaison avec un État contemporain est éclairante. Une naissance, une décision administrative, une nomination, une création d’entreprise ou une opération comptable ne sont pas tous publiés dans un même journal universel. Des registres spécialisés maintiennent des états autoritatifs ; certains actes seulement font l’objet d’une publicité officielle.

Pour Cogentia :

```text
Reality / Action
       ↓
     Event
       ↓
   FractaLog
       │
       ├── Identity Register
       ├── Agent Register
       ├── Mandate Register
       ├── Revocation Register
       ├── Decision Register
       ├── Asset Register
       ├── Contract Register
       ├── Accounting Ledgers
       ├── Interaction Register
       ├── Audit Register
       └── ...
               │
               ↓
          Projectors
               │
        ┌──────┴──────┐
        ↓             ↓
   Current State   Official Journal
```

### 3.1 FractaLog

FractaLog répond principalement à :

> Que s’est-il produit, qui a agi, sous quel mandat, dans quelle chaîne causale, et quelles preuves permettent de le vérifier ?

### 3.2 Registre

Un registre spécialisé répond principalement à :

> Quel est l’état autoritatif actuel d’un domaine donné ?

### 3.3 Journal Officiel

Le Journal Officiel répond principalement à :

> Quels actes doivent être authentiquement publiés et opposables à un public déterminé ?

Un même événement source peut donc alimenter plusieurs projections sans duplication de la réalité causale.

---

## 4. Le registre des registres

La multiplication légitime des registres appelle un **Registry of Registers**, ou registre des registres.

Il ne contient pas les données des registres. Il décrit :

- leur existence ;
- leur identité ;
- leur objet ;
- leur schéma ;
- leur périmètre ;
- leur autorité ;
- leur gardien ;
- leur visibilité ;
- leur politique de rétention ;
- leur relation avec FractaLog ;
- leur statut : autoritatif, dérivé, historique, public, restreint, etc.

Sa fonction essentielle n’est pas seulement documentaire. Il répond à la question :

> **Quel registre fait foi pour telle question ?**

Une donnée peut être reproduite dans de nombreuses vues ; l’autorité doit être définie quelque part.

Le registre des registres est un objet constitutionnel racine de l’Instance. Son existence ne crée pas une régression infinie : ses propres changements sont enregistrés dans FractaLog.

Événements candidats :

```text
register.created
register.authority.assigned
register.schema.changed
register.visibility.changed
register.deprecated
register.replaced
register.sealed
```

---

## 5. Une Constitution machine-readable, sans gouvernement par la machine

L’informatique peut rendre automatiquement vérifiables de nombreuses propriétés procédurales :

```text
mandat existant ?
mandat expiré ?
compétence appropriée ?
délégation autorisée ?
budget disponible ?
procédure respectée ?
publication obligatoire effectuée ?
trace produite ?
contrôle humain requis mais absent ?
recours encore ouvert ?
```

Elle ne doit pas pour autant transformer toute question juridique ou politique en décision automatique.

La séparation doctrinale est :

```text
ordinateur :
  constater
  vérifier
  signaler
  documenter
  simuler
  alerter

acteur légitime :
  apprécier
  arbitrer
  décider
  assumer
```

L’IA relève de la suggestion et de l’éclairage, non de la prescription souveraine.

---

## 6. Capability, mandat et légitimité

La possibilité technique d’agir n’est pas la compétence institutionnelle.

```text
capability ≠ permission ≠ mandat ≠ légitimité de l’acte
```

Un agent peut techniquement appeler un outil et néanmoins ne pas être légitime à le faire dans un contexte donné.

Une capacité d’action institutionnellement légitime dépend notamment de :

```text
capability
+ competence / jurisdiction
+ mandate
+ budget
+ procedure
+ traceability
= legitimate capacity to act
```

Ce schéma vaut pour les agents artificiels, les personnes physiques et les personnes morales, sous réserve des règles particulières propres à chacun.

---

## 7. Principe de responsabilité neutre au type d’acteur

L’essor des agents IA révèle un risque de double standard : exiger des machines qu’elles prouvent leur mandat, tracent leurs actes et rendent des comptes, tout en tolérant pour des acteurs humains ou institutionnels exerçant le même pouvoir un niveau d’opacité plus élevé.

Invariant candidat :

> **Actor-neutral accountability principle — Toute exigence de contrôle justifiée par la puissance, le risque ou les effets d’un acte doit s’appliquer indépendamment de la nature humaine, morale ou artificielle de son auteur, sauf différence explicitement pertinente et justifiable.**

Ce principe ne signifie pas que les règles doivent être identiques pour tous les acteurs. Il exige que les différences de régime soient justifiées par des différences pertinentes, et non par le seul fait qu’un acteur soit humain ou artificiel.

Corollaires :

- aucun humain ou organisme ne doit perdre en traçabilité parce qu’il délègue à une IA ;
- la présence formelle d’un humain ne doit pas effacer la provenance machine d’un acte ;
- rendre l’IA responsable ne doit pas rendre irresponsable celui qui l’a mandatée ;
- les contrôles doivent suivre **l’acte et le pouvoir exercé**, pas seulement la technologie utilisée.

En raccourci :

```text
NO AI WASHING
NO HUMAN WASHING
TRACE THE ACT
```

---

## 8. Anti-capture : déléguer sans aliéner

La souveraineté ne se réduit pas au pouvoir d’agir. Elle comprend la capacité ultime de déterminer qui peut exercer quels pouvoirs, sous quelles conditions, et de reprendre ces pouvoirs.

```text
souveraineté
    ↓
autorise
    ↓
compétence
    ↓
mandat
    ↓
acte
    ↓
contrôle
    ↓
révocation / correction éventuelle
    ↓
retour au souverain
```

Principe candidat :

> **Pas de délégation souveraine sans possibilité de reprise.**

La délégation ne doit pas devenir une cession silencieuse de souveraineté.

### 8.1 Séparation fonctionnelle des pouvoirs

La séparation historique législatif/exécutif/judiciaire peut être généralisée comme pattern anti-capture : les fonctions dont la concentration permettrait à un acteur de définir la règle, l’appliquer, juger sa propre application et effacer les preuves doivent pouvoir être séparées.

Pour les systèmes agentiques :

```text
proposal
policy
execution
authorization
audit
appeal
```

ne doivent pas nécessairement être concentrés dans le même agent.

### 8.2 Subsidiarité traçable

Un niveau supérieur ne devrait intervenir sur un niveau inférieur capable d’agir sans produire une justification explicite de l’escalade.

Éléments candidats :

```text
escalation.authority
escalation.reason
escalation.scope
escalation.duration
escalation.return_condition
```

La centralisation exceptionnelle doit être visible et réversible.

---

## 9. Correction sans réécriture

Un invariant transversal apparaît dans FractaLog, la comptabilité, les actes juridiques et les recours :

> **Corriger sans réécrire l’histoire.**

Un acte annulé n’est pas effacé ; son effet juridique change par un nouvel acte. Une estimation comptable erronée est compensée par une écriture ultérieure. Une information corrigée conserve la trace de sa correction.

```text
Acte A
↓
Recours R
↓
Décision D : A annulé
↓
Compensation C
```

L’immutabilité historique ne signifie donc pas irrévocabilité des effets.

---

## 10. Effets, causes et intentions : discipline de preuve

L’analyse politique doit distinguer trois niveaux :

> **Les effets se constatent ; les causes s’expliquent ; les intentions se prouvent.**

Les effets sont souvent observables ou mesurables. La causalité réclame un modèle, un mécanisme et la confrontation avec des explications concurrentes. L’intention exige des preuves supplémentaires : déclarations, documents, instructions, préparation, etc.

Une hiérarchie utile :

```text
L0 — effet constaté
L1 — bénéficiaire / distribution des effets
L2 — mécanisme causal plausible
L3 — acteur informé de l’effet
L4 — acteur ayant contribué au maintien du mécanisme
L5 — intention explicitement étayée
```

Il est politiquement significatif d’établir L0–L4 sans disposer de L5.

Règle argumentative :

> **Ne jamais utiliser une hypothèse d’intention lorsque la démonstration par les effets et les mécanismes suffit.**

Aphorisme associé :

> **« Dans un procès d’intention, le coupable le plus certain, c’est l’accusateur. »**

Le but n’est pas de nier l’existence de collusions ou d’intentions malveillantes, mais d’éviter de substituer une psychologie supposée à une démonstration disponible.

---

## 11. Du jugement moral à la sanction : le risque d’auto-mandat

Le problème devient plus grave lorsque l’inférence d’intention déclenche une sanction.

Le cycle DRSJ développé dans `research/invidia.md` décrit :

```text
Déni de compétence
→ Requalification causale
→ Soupçon moral
→ Justification de la sanction
```

`research/justice_divine_mandat_implicite.md` décrit le mouvement complémentaire : une conviction morale ou une source supérieure peut être transformée en **mandat implicite** autorisant celui qui juge à agir sur autrui sans les médiations ordinaires de preuve, contradictoire, compétence, proportionnalité, trace et recours.

La chaîne consolidée est :

```text
fait observé
    ↓
hypothèse causale
    ↓
intention inférée
    ↓
qualification morale
    ↓
certitude morale
    ↓
auto-mandat
    ↓
sanction
    ↓
effets réels sur la cible
    ↓
éventuelle auto-validation du soupçon initial
```

Invariant candidat :

> **Aucune inférence factuelle, causale, intentionnelle ou morale ne confère par elle-même le mandat de sanctionner.**

Autrement dit :

```text
Observation ≠ causalité
Causalité ≠ intention
Intention ≠ culpabilité
Culpabilité supposée ≠ mandat
Mandat ≠ sanction arbitraire
```

Chaque séparation est une médiation de l’État de droit.

---

## 12. Le révélateur / stabilisateur IA

La puissance et la dangerosité potentielles des agents IA conduisent à construire des garde-fous solides : mandat, journalisation, contrôle, limitation, recours, audit, révocation.

Cette exigence joue un double rôle.

### 12.1 Révélateur

Elle rend visibles les garanties parfois absentes ou insuffisantes dans les institutions purement humaines. Lorsqu’un agent logiciel doit pouvoir produire une chaîne structurée expliquant qui l’a mandaté, selon quelle compétence, avec quel budget et quelle preuve, il devient légitime de demander pourquoi un acteur humain exerçant un pouvoir comparable ne fournirait pas une provenance équivalente.

### 12.2 Stabilisateur

Une fois ces garanties formalisées, elles deviennent des primitives réutilisables indépendamment du type d’acteur :

```text
mandate.schema
act.schema
appeal.schema
audit.schema
delegation.schema
register.schema
```

L’IA ne révèle donc pas seulement une faiblesse institutionnelle ; elle fournit des moyens techniques de la corriger.

---

## 13. Tests anti-capture candidats

### 13.1 Institutional Capture Test

Pour toute nouvelle compétence ou règle :

1. Quelle souveraineté est mobilisée ?
2. Qui délègue ?
3. À qui ?
4. Le périmètre est-il explicite ?
5. L’acte est-il traçable ?
6. La délégation est-elle révocable ?
7. Existe-t-il un recours ?
8. Le contrôleur est-il contrôlable ?
9. Peut-on remplacer l’opérateur sans perdre l’institution ?
10. Peut-on reconstruire la chaîne de légitimité ?

### 13.2 Human Symmetry Test

Pour toute règle imposée spécifiquement à une IA :

1. Pourquoi cette règle existe-t-elle ?
2. Le risque existe-t-il aussi pour un humain ou une personne morale ?
3. Si oui, pourquoi la règle ne lui est-elle pas appliquée ?
4. La différence de régime est-elle matériellement justifiée ?
5. Ou protège-t-elle un privilège institutionnel existant ?

### 13.3 Machine Substitution Test

> Si exactement le même acte était accompli par une IA, accepterions-nous le même niveau d’opacité et d’irresponsabilité ?

### 13.4 Intent Discipline Test

Avant d’attribuer une intention :

1. Quel effet est réellement établi ?
2. Quel mécanisme causal est proposé ?
3. Quelles explications concurrentes existent ?
4. Quel intérêt objectif est identifiable ?
5. Quelles preuves distinctes établissent l’intention ?

---

## 14. Risques de capture de l’État de droit assisté

Plusieurs dérives doivent être prévues sans leur attribuer d’intention a priori :

- réserver les exigences fortes de traçabilité aux seuls acteurs artificiels ;
- interrompre la chaîne de responsabilité lorsqu’un humain valide formellement une recommandation machine ;
- produire une transparence descriptive sans contestabilité réelle ;
- journaliser l’activité technique sans tracer l’ordre, le mandat et les décideurs humains ;
- substituer une certification de conformité à la démonstration de légitimité ;
- utiliser secret, urgence ou sécurité pour supprimer la trace au lieu d’en restreindre le contenu ;
- fragmenter la responsabilité entre fournisseur, intégrateur, agent, administration et opérateur humain jusqu’à ce que personne ne réponde de l’acte complet ;
- centraliser au nom de l’harmonisation sans mécanisme de retour vers le niveau inférieur.

Le critère d’analyse doit porter sur les **effets institutionnels** de ces mécanismes, non sur les intentions présumées de leurs promoteurs.

---

## 15. Architecture cible minimale pour Cogentia

```text
Cogentia Instance
│
├── Identity / Principal
├── Constitutional Rules
├── Registry of Registers
├── FractaLog Root
│
├── Registers
│   ├── Identity
│   ├── Agents
│   ├── Mandates
│   ├── Revocations
│   ├── Decisions
│   ├── Assets
│   ├── Contracts
│   ├── Accounting
│   ├── Interactions
│   └── Audit / Appeals
│
├── Official Journal projector
│
├── Institutional roles
│   ├── proposing
│   ├── authorizing
│   ├── executing
│   ├── reviewing
│   └── auditing
│
└── Appeals / correction / succession
```

Cette architecture est fractale : les sous-instances peuvent disposer des mêmes primitives à leur échelle, tandis que les niveaux supérieurs agrègent des preuves et des relations d’autorité plutôt que d’absorber tous les contenus.

---

## 16. Programme de travail

1. **Cogentia** — formaliser `Registry of Registers` et `Official Journal` comme projecteurs institutionnels au-dessus de FractaLog.
2. **COP / Inseme** — vérifier quels événements génériques existent déjà pour mandat, révocation, registre, publication, contestation, correction et escalade.
3. **FractaLog** — expliciter que le log est le substrat autoritatif d’événements et de preuves dont registres, ledgers et publications sont des projections ; éviter de faire de FractaLog lui-même un registre universel.
4. **Kudocracy** — relier démocratie assistée et formation de la volonté souveraine à l’État de droit assisté qui encadre ensuite l’exercice des mandats.
5. **Comptabilité Cogentia** — traiter les écritures générales et analytiques comme projections spécialisées d’événements, en conservant l’invariant de correction par compensation plutôt que réécriture.
6. **Anti-capture** — rendre exécutables ou testables les `Human Symmetry Test`, `Machine Substitution Test`, `Institutional Capture Test` et `Intent Discipline Test`.
7. **Recours** — définir un modèle minimal de contentieux agentique : contestation, instruction, contradictoire, décision, confirmation/correction/annulation/compensation.
8. **Publication** — définir niveaux `open`, `redacted`, `restricted`, `sealed`, `escrowed` pour distinguer existence de la trace et visibilité du contenu.
9. **Recherche** — comparer cette synthèse aux travaux contemporains sur electronic institutions, institutional AI, constitutional multi-agent governance, delegation provenance et separation of powers.

---

## 17. Formules candidates à conserver

> **Un État de droit assisté par ordinateur au service d’une démocratie tout autant assistée.**

> **L’assistance informatique doit augmenter la capacité du souverain à contrôler ses mandataires, jamais augmenter la capacité des mandataires à contrôler le souverain.**

> **Toute puissance doit pouvoir expliquer son origine, montrer ses actes et rendre ce qu’elle a reçu.**

> **Déléguer sans aliéner.**

> **Corriger sans réécrire.**

> **Les effets se constatent ; les causes s’expliquent ; les intentions se prouvent.**

> **Dans un procès d’intention, le coupable le plus certain, c’est l’accusateur.**

> **Aucune inférence factuelle, causale, intentionnelle ou morale ne confère par elle-même le mandat de sanctionner.**

> **No AI washing. No human washing. Trace the act.**

---

## 18. Limites et points à vérifier

- La notion de « souveraineté » n’a pas le même sens pour une personne, une association, une société commerciale, une collectivité ou un État : ne pas aplatir ces régimes juridiques sous une abstraction logicielle unique.
- La traçabilité ne doit pas devenir surveillance : tracer l’acte, son mandat et sa preuve ne signifie pas absorber tous les contenus privés.
- L’existence d’un registre autoritatif ne doit pas créer un monopole technique irrévocable : portabilité, réplication, preuve et succession doivent être prévues.
- La formalisation machine-readable ne doit pas devenir une substitution du jugement automatique au jugement humain légitime.
- L’anti-capture doit s’appliquer à ses propres mécanismes de contrôle : auditeurs, registres, certificateurs et projecteurs peuvent eux-mêmes devenir des points de capture.

---

## 19. Conclusion provisoire

Les agents IA rendent urgente une question plus ancienne qu’eux : comment une volonté souveraine peut-elle produire de l’action collective sans perdre le contrôle de ce qu’elle délègue ?

La réponse explorée ici consiste à combiner démocratie assistée, État de droit assisté, traçabilité des actes, registres autoritatifs, publicité contrôlée, comptabilité, recours, révocation et anti-capture. Les Digital Twins servent de laboratoire particulièrement explicite, mais les primitives obtenues doivent rester applicables à tous les acteurs exerçant du pouvoir — humains, personnes morales ou agents artificiels — selon des régimes adaptés et justifiables.

L’objectif n’est pas de donner le droit à la machine. Il est d’utiliser l’informatique pour rendre plus difficile la disparition du droit derrière l’exercice du pouvoir.
