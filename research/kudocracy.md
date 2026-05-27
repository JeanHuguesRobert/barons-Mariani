---
title: "Kudocracy"
subtitle: "Suggestions civiques traçables, votations et démocratie liquide assistée par agents"
description: "Working paper sur Kudocracy comme couche de suggestions civiques traçables pour des votations, complémentaire de la démocratie liquide et adjacente aux mandataires représentatifs. La recommandation y est traitée comme une forme plus forte que la suggestion, plus directive et donc plus strictement encadrée."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani — C.O.R.S.I.C.A. / Inseme / Cogentia"
version: "0.2"
date: "2026-05-22"
status: working-paper — révision conceptuelle
license: "CC BY-SA 4.0"
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/kudocracy.md
last_modified_at: "2026-05-22"
last_stamped_at: 2026-05-26
tags:
  - kudocracy
  - votations
  - democratie-liquide
  - suggestion-civique
  - recommandation-civique
  - agents-ia
  - agent-personnel
  - souverainete-citoyenne
  - non-pression-algorithmique
  - seconde-methode
related:
  - "./second_method.md"
  - "./autonomia.md"
  - "./pathologie_du_secret.md"
  - "https://github.com/JeanHuguesRobert/cogentia"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/prompts/cognitive_packet.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia_commons_method_packets.md"
changelog:
  - "v0.1 (2026-05-20) — premier draft : distinction votation/élection, recommandation/délégation, agents humains et artificiels, agent IA personnel, passage au crible de la seconde méthode, continuation."
  - "v0.2 (2026-05-22) — révision conceptuelle : distinction suggestion / recommandation / délégation / prescription ; remplacement du mode par défaut de recommandation civique par suggestion civique ; ajout du garde-fou contre la pression algorithmique ; clarification du rôle de l’agent IA personnel comme auxiliaire de jugement non prescriptif."
---

# Kudocracy

## Suggestions civiques traçables, votations et démocratie liquide assistée par agents

---

## Abstract

**Abstract —** Liquid democracy is usually framed as a hybrid between direct and representative democracy, allowing citizens either to vote directly or to delegate their voting power to proxies. Kudocracy proposes a complementary model focused on *votations* rather than elections: citizens vote on proposals, as in referendum-style direct democracy, while still allowing representative mandates to exist in adjacent institutional layers.

Instead of primarily transferring voting power, citizens may subscribe to traceable **civic suggestions** issued by human, collective, or artificial agents. A suggestion does not prescribe a vote. It opens an option, presents reasons, exposes uncertainty, and helps the citizen exercise judgment. Stronger civic recommendations remain possible, but they must be explicitly labelled as such, justified, auditable, and distinguishable from suggestion, delegation, and prescription.

These suggestions may be followed, ignored, overridden, compared, or transformed into explicit delegation while preserving individual agency and public auditability. A personal AI agent may act as a civic guardian, helping each citizen compare suggestions and recommendations, detect inconsistencies, preserve value alignment, identify conflicts of interest, and protect long-term interests without voting or deciding in the citizen’s place.

Kudocracy is therefore not merely an online voting mechanism, but a model of agent-assisted civic orientation, positioned between liquid democracy, deliberative systems, recommender architectures, and democratic AI governance. Its core principle is simple: **AI may illuminate the vote; it must not manufacture the slope that makes the citizen’s vote predictable.**

---

## Mots-clés

Kudocracy ; démocratie liquide ; votations ; démocratie directe ; suggestions civiques ; recommandations civiques ; agents IA ; agent personnel ; mandataires ; traçabilité ; auditabilité ; révocabilité ; autonomie de capacité ; Inseme ; Cogentia ; souveraineté citoyenne ; non-pression algorithmique.

---

## Note méthodologique

Ce texte applique la logique du *Discours de la seconde méthode* : publier le processus, distinguer faits, interprétations et propositions, transformer les objections en contributions de premier rang, écrire pour humains et agents, et considérer le corpus public, versionné et améliorable comme le lieu réel de la preuve.

Le présent document n’est donc pas une doctrine fermée. Il doit être lu comme une version de travail appelée à recevoir objections, corrections, contre-exemples, références supplémentaires, tests institutionnels, simulations et implémentations expérimentales.

La thèse proposée est simple :

> **Kudocracy est une couche de suggestion civique traçable pour des votations sur propositions, complémentaire de la démocratie liquide et adjacente aux systèmes de mandataires, sans se confondre avec l’élection représentative.**

La suggestion civique est la couche première parce qu’elle préserve la souveraineté du jugement citoyen. La recommandation civique reste possible, mais comme forme plus forte, explicitement signalée, justifiée, auditée et toujours subordonnée au droit de reprise du citoyen.

Cette thèse doit être mise à l’épreuve. Le présent texte fournit donc, outre la proposition elle-même, ses hypothèses testables, ses objections principales, ses conditions de réfutation et une clause de continuation.

---

# 1. Problème : le citoyen vote rarement sur ce qu’il peut réellement évaluer

La démocratie contemporaine souffre moins d’un manque formel de procédures que d’un déficit pratique de capacité.

Le citoyen dispose, en principe, du droit de voter, de s’exprimer, de s’informer, de soutenir ou de contester. Mais il est confronté à une masse croissante de décisions techniques, juridiques, économiques, écologiques, territoriales et géopolitiques. Dans ces conditions, l’autonomie politique formelle ne suffit plus. Il faut encore disposer des moyens concrets de comprendre, comparer, arbitrer et corriger.

La démocratie représentative classique répond à cette difficulté par l’élection de mandataires. Le citoyen ne décide pas directement sur chaque proposition ; il choisit des personnes chargées de décider en son nom.

La démocratie directe répond autrement : le citoyen vote sur des propositions.

La démocratie liquide tente de combiner ces deux approches : chacun peut voter directement ou déléguer son vote à une personne jugée plus compétente.

Kudocracy introduit un déplacement supplémentaire :

> **Avant de déléguer son vote, ou au lieu de le déléguer, le citoyen peut recevoir des suggestions civiques traçables.**

Ces suggestions peuvent être produites par des agents humains, collectifs ou artificiels. Elles peuvent être suivies, ignorées, contredites, comparées, révisées, rejetées ou transformées en recommandation forte ou en délégation explicite.

Le cœur du modèle n’est donc pas l’élection. Le cœur du modèle est la **votation sur proposition**, assistée par des agents de suggestion, de comparaison et d’explication.

---

# 2. Votations, non élections

Kudocracy doit être clairement distinguée d’un système électoral classique.

Elle ne vise pas d’abord à élire des représentants. Elle vise à permettre des décisions collectives sur des **propositions**.

Le terme le plus juste est donc celui de **votation**, au sens où l’on vote sur un objet déterminé : une règle, une décision, une orientation, une priorité, un budget, une modification statutaire, une résolution, une initiative ou un veto.

L’analogie suisse est utile, avec prudence : dans les votations suisses, les citoyens ne votent pas seulement pour des personnes ; ils votent régulièrement sur des objets soumis à décision populaire. Kudocracy s’inscrit dans cette logique de vote sur propositions, sans prétendre copier les institutions suisses.

Cette précision évite une confusion majeure.

Kudocracy ne dit pas :

> Il faut supprimer les mandataires.

Elle dit :

> Les mandataires ne doivent pas absorber toute la capacité démocratique. Une société démocratique doit aussi pouvoir décider directement sur des propositions, avec des outils de suggestion, de comparaison, de traçabilité et de révocation adaptés à la complexité contemporaine.

Les mandataires restent possibles, nécessaires dans certains contextes, et même utiles. Mais ils sont adjacents au modèle, non son centre.

Kudocracy peut donc coexister avec :

- des élus ;
- des mandataires associatifs ;
- des représentants institutionnels ;
- des délégations temporaires ;
- des assemblées ;
- des conseils ;
- des votations directes ;
- des procédures consultatives ou décisionnelles.

Ce qu’elle ajoute est une couche de capacité civique : pouvoir se prononcer sur des propositions avec l’aide d’agents suggestifs, de recommandations explicites lorsqu’elles sont nécessaires, et de mandats audités lorsque le pouvoir décisionnel est transféré.

---

# 3. Définitions minimales

## 3.1. Proposition

Une **proposition** est un objet soumis à discussion, suggestion, recommandation, amendement ou vote.

Elle peut être :

- normative : adopter une règle ;
- budgétaire : affecter une ressource ;
- stratégique : choisir une orientation ;
- territoriale : prioriser un projet ;
- institutionnelle : modifier une gouvernance ;
- corrective : annuler, suspendre ou réviser une décision ;
- expérimentale : autoriser un test limité et réversible.

Dans Kudocracy, le citoyen vote sur des propositions, non sur des personnes.

## 3.2. Votation

Une **votation** est une procédure par laquelle une communauté décide explicitement sur une proposition.

Elle peut être :

- contraignante ou consultative ;
- locale, thématique ou générale ;
- ouverte à tous les ayants droit ou limitée à un périmètre défini ;
- précédée d’une phase d’argumentation ;
- accompagnée de suggestions et recommandations traçables ;
- réversible selon des conditions prévues.

## 3.3. Agent suggestif

Un **agent suggestif** est une source identifiable de suggestions civiques.

Il peut être :

- une personne ;
- un collectif ;
- une association ;
- une institution ;
- un média ;
- un expert ;
- un groupe local ;
- un agent IA spécialisé ;
- une combinaison hybride humain-machine.

Son rôle n’est pas de voter à la place du citoyen. Son rôle premier est de formuler des possibilités d’analyse, d’amendement, de vigilance, de comparaison ou d’action, de manière explicite, motivée, traçable et contestable.

Un agent suggestif peut parfois produire une recommandation plus forte, mais celle-ci doit être explicitement marquée comme recommandation. Elle ne doit jamais être confondue avec une délégation, encore moins avec une prescription.

## 3.4. Abonnement civique

Un **abonnement civique** est le lien volontaire par lequel un citoyen choisit de recevoir les suggestions ou recommandations d’un agent.

Cet abonnement peut être :

- global ;
- thématique ;
- temporaire ;
- conditionnel ;
- révocable ;
- public ou privé selon les règles du système ;
- transformable en délégation explicite dans certains cas.

L’abonnement civique ne doit pas être assimilé à une délégation. Il organise l’arrivée d’informations, de suggestions, de comparaisons ou de recommandations ; il ne transfère pas par lui-même le pouvoir de décision.

## 3.5. Suggestion civique

Une **suggestion civique** est un avis structuré, non contraignant et non prescriptif portant sur une proposition.

Elle ne dit pas au citoyen ce qu’il doit voter. Elle lui présente une ou plusieurs possibilités de jugement ou d’action.

Elle doit idéalement indiquer :

- la proposition concernée ;
- l’option ou les options suggérées ;
- les raisons principales ;
- les arguments contraires ;
- les sources utilisées ;
- les incertitudes ;
- les conflits d’intérêts éventuels ;
- la date ;
- l’auteur ou l’agent responsable ;
- les conditions de révision ;
- le niveau de force de la suggestion.

Une suggestion civique peut prendre plusieurs formes :

| Forme | Fonction |
|---|---|
| suggestion d’analyse | éclairer les enjeux |
| suggestion de question | indiquer ce qu’il faut vérifier |
| suggestion d’amendement | améliorer la proposition |
| suggestion de vigilance | signaler un risque |
| suggestion de comparaison | rapprocher plusieurs positions |
| suggestion de conséquence | expliciter effets directs et indirects |
| suggestion de vote | proposer une option sans la prescrire |

La suggestion civique doit renforcer le jugement du citoyen, non le remplacer.

## 3.6. Recommandation civique

Une **recommandation civique** est une forme plus forte de suggestion.

Elle indique explicitement qu’un agent estime préférable une option déterminée : voter pour, voter contre, s’abstenir, amender, ajourner, déléguer ou demander révision.

Parce qu’elle est plus directive, elle doit être plus strictement encadrée.

Une recommandation civique légitime doit être :

- explicitement signalée comme recommandation ;
- motivée ;
- traçable ;
- contestable ;
- comparable à d’autres recommandations ;
- révocable dans ses effets ;
- distincte d’une délégation ;
- distincte d’une prescription ;
- accompagnée d’un niveau d’incertitude ;
- accompagnée d’une déclaration de conflit d’intérêts si nécessaire.

Dans Kudocracy, la recommandation n’est pas interdite. Elle est simplement plus forte que la suggestion, donc plus exigeante en justification et en auditabilité.

## 3.7. Délégation

Une **délégation** est un transfert explicite, limité et révocable de pouvoir décisionnel.

Elle est plus forte qu’une recommandation.

La suggestion dit :

> Voici une possibilité à examiner.

La recommandation dit :

> Je pense que cette option est préférable.

La délégation dit :

> Décide pour moi dans le cadre que je t’accorde.

Kudocracy privilégie la suggestion comme couche première. La recommandation reste possible comme orientation plus forte. La délégation reste possible comme transfert explicite de pouvoir, mais elle doit être traçable, bornée et révocable.

## 3.8. Mandataire

Un **mandataire** est une personne ou une structure habilitée à agir au nom d’autrui dans un cadre déterminé.

Kudocracy ne supprime pas les mandataires. Elle clarifie leur place.

Un mandataire peut être :

- élu ;
- désigné ;
- mandaté par contrat ;
- mandaté par une assemblée ;
- mandaté temporairement pour une mission ;
- contrôlé par des votations ;
- évalué par l’historique public de ses actes.

Le principe est le suivant :

> Plus un mandataire agit au nom d’autrui, plus son mandat doit être explicite, traçable, révocable ou contrôlable.

## 3.9. Suggestion, recommandation, délégation, prescription

Kudocracy repose sur une échelle de force civique.

| Niveau | Formule | Effet | Régime de contrôle |
|---|---|---|---|
| Suggestion | “Voici une possibilité à examiner.” | Ouverture du jugement | justification légère à forte selon influence |
| Recommandation | “Je pense que cette option est préférable.” | Orientation plus directive | justification forte et auditabilité |
| Délégation | “Décide pour moi dans ce cadre.” | Transfert temporaire de pouvoir | mandat explicite, borné, révocable |
| Prescription | “Tu dois voter ainsi.” | Pression ou substitution au jugement | en principe exclue du système civique |

La suggestion donne du pouvoir au citoyen.

La recommandation oriente plus fortement.

La délégation transfère un pouvoir.

La prescription met le citoyen sous pression et doit être exclue comme mode normal d’assistance civique.

Principe :

> Plus un agent se rapproche de la recommandation forte, de la délégation ou de la prescription, plus l’exigence de justification, d’auditabilité, de révocabilité et de contrôle humain augmente.

---

# 4. De la démocratie liquide à la suggestion liquide

La démocratie liquide est généralement décrite comme une combinaison de démocratie directe et de démocratie représentative : chacun peut voter directement ou déléguer son vote.

Ce modèle a une puissance évidente. Il rend la représentation plus fluide, plus thématique, plus réversible.

Mais il conserve une difficulté : la délégation transfère un pouvoir. Même lorsqu’elle est révocable, elle peut devenir routinière, concentrée, opaque ou socialement captée.

Kudocracy propose de placer la suggestion avant la recommandation, et la recommandation avant la délégation.

Cela produit plusieurs niveaux d’engagement :

| Niveau | Formule | Effet |
|---|---|---|
| Consultation | “Je lis cette suggestion.” | Information |
| Abonnement | “Je reçois les suggestions de cet agent.” | Orientation régulière |
| Suggestion ponctuelle | “J’examine cette possibilité.” | Jugement assisté |
| Recommandation ponctuelle | “Je considère cette option comme préférable selon cet agent.” | Orientation forte |
| Suivi thématique | “Je suis cet agent sur ce domaine.” | Confiance spécialisée |
| Suivi conditionnel | “Je suis sauf alerte de mon agent personnel.” | Automatisation surveillée |
| Délégation | “Je transfère temporairement mon vote.” | Décision par autrui |
| Reprise | “Je reprends directement la main.” | Réversibilité |

La suggestion liquide permet donc de bénéficier de la compétence d’autrui sans abandonner son pouvoir de décision et sans être immédiatement placé sous la pression d’une recommandation forte.

Elle correspond mieux à la réalité ordinaire du jugement humain : nous décidons rarement seuls, mais nous devons pouvoir savoir qui nous influence, pourquoi, avec quelles raisons, selon quelle force, et avec quelle possibilité de correction.

---

# 5. Architecture civique de Kudocracy

Kudocracy repose sur une architecture simple :

1. Des propositions sont formulées.
2. Des agents suggestifs produisent des suggestions civiques.
3. Certains agents peuvent produire des recommandations civiques plus fortes, explicitement signalées.
4. Les citoyens s’abonnent volontairement à certains agents.
5. Les suggestions et recommandations sont reçues, comparées, expliquées.
6. Chaque citoyen vote, s’abstient, suit, contredit, diffère, amende ou délègue.
7. Les actes d’influence civique pertinents sont tracés selon des règles publiques.
8. Les abonnements et délégations restent révocables.
9. L’historique produit une mémoire civique auditable.

Cette architecture ne suppose pas que tout soit public au même degré.

Elle suppose en revanche que les actes prétendant orienter la décision commune deviennent suffisamment traçables pour être discutés, contestés et corrigés.

La traçabilité est proportionnelle au pouvoir d’influence.

Un citoyen ordinaire doit conserver une sphère de protection. Un agent suggestif influent, un agent recommandateur, un mandataire, un collectif militant, une IA publique ou une institution doivent accepter un niveau supérieur d’auditabilité.

---

# 6. L’agent IA personnel

L’agent IA personnel est une composante centrale de Kudocracy.

Il ne doit pas être compris comme un souverain artificiel. Il doit être compris comme un auxiliaire de souveraineté individuelle.

Sa fonction est de protéger les intérêts, les valeurs, la mémoire décisionnelle et la cohérence de son propriétaire.

Il peut notamment :

- lire les propositions soumises à votation ;
- résumer les enjeux ;
- comparer plusieurs suggestions ou recommandations ;
- distinguer suggestion, recommandation, délégation et prescription ;
- détecter les contradictions ;
- rappeler les décisions antérieures ;
- identifier les conflits d’intérêts possibles ;
- signaler les effets indirects d’une proposition ;
- proposer des questions à examiner ;
- suggérer des amendements ;
- suggérer des conséquences à vérifier ;
- alerter contre un suivi automatique dangereux ;
- refuser de produire une recommandation de vote lorsque les informations sont insuffisantes ;
- conserver une mémoire civique personnelle ;
- produire une explication compréhensible des options possibles.

La règle critique est la suivante :

> **L’agent IA personnel ne doit pas être l’agent de la plateforme. Il doit être l’agent du citoyen.**

Sinon, Kudocracy devient un système de manipulation algorithmique.

Un agent personnel légitime doit donc être :

- contrôlable par son propriétaire ;
- explicable dans ses suggestions et recommandations ;
- corrigeable ;
- exportable ;
- compatible avec plusieurs plateformes ;
- distinct des agents d’influence ;
- capable de signaler ses incertitudes ;
- soumis à des règles de minimisation des données.

Formule centrale :

> **L’agent IA personnel ne vote pas à la place du citoyen ; il protège la capacité du citoyen à juger, refuser, différer, contredire, déléguer explicitement ou reprendre la main.**

Règle de conception :

> **Par défaut, un agent IA civique produit des suggestions, non des recommandations de vote.**

Il peut produire une recommandation seulement si le citoyen le demande explicitement ou si le cadre d’usage le prévoit clairement. Même alors, la recommandation doit rester explicable, contestable, réversible dans ses effets et subordonnée au jugement humain.

---

# 7. Traçabilité publique et vie privée

Kudocracy repose sur une distinction stricte entre vie privée et acte civique public.

La vie privée doit être protégée.

Mais lorsqu’un agent produit une suggestion ou recommandation destinée à orienter une décision commune, cet acte relève d’un espace public ou semi-public. Il doit pouvoir être audité à proportion de son pouvoir d’influence.

Il ne s’agit pas de surveiller les personnes. Il s’agit de rendre visibles les chaînes d’influence.

Cette distinction répond à l’objection du “crédit social”.

Kudocracy ne vise pas à noter les individus, surveiller leurs opinions privées ou produire un classement moral des citoyens. Elle vise à rendre traçables les actes par lesquels certains acteurs prétendent orienter la décision collective.

La règle pourrait être formulée ainsi :

> **Plus un acteur prétend influencer la décision commune, plus ses suggestions, recommandations, mandats et actes doivent être explicites, traçables et vérifiables.**

Kudocracy ne surveille pas les faibles. Elle rend auditable l’influence exercée sur le commun.

---

# 8. Granularité

La granularité est l’un des principaux avantages de Kudocracy.

Dans un système représentatif classique, la confiance est massive et périodique : on choisit un représentant pour un ensemble très large de sujets, pour une durée relativement longue.

Dans Kudocracy, la confiance peut être :

- locale ;
- thématique ;
- temporaire ;
- conditionnelle ;
- partagée ;
- pondérée ;
- révoquée.

Un citoyen peut recevoir ou suivre :

- un collectif écologique sur une question de biodiversité ;
- un ingénieur sur une question énergétique ;
- une association locale sur un problème communal ;
- un juriste sur une question institutionnelle ;
- un agent IA personnel pour comparer les suggestions ;
- aucun agent lorsqu’il souhaite décider directement.

Cette granularité permet de sortir de la logique partisane globale.

On ne dit plus seulement :

> Je soutiens ce parti.

On peut dire :

> Sur cette proposition, dans ce contexte, j’examine cette suggestion, je comprends cette recommandation, je conserve mon droit de reprise, et je décide.

---

# 9. Rapport avec les mandataires

Kudocracy est adjacente au mandat, non hostile au mandat.

Un système politique ou associatif peut avoir besoin de mandataires pour :

- négocier ;
- exécuter ;
- représenter ;
- signer ;
- gérer ;
- administrer ;
- arbitrer en urgence ;
- assurer la continuité.

Mais le mandat doit être encadré.

Kudocracy peut servir à contrôler ou compléter les mandataires par :

- des votations sur propositions ;
- des suggestions publiques ;
- des recommandations explicitement signalées ;
- des mandats explicites ;
- des révocations ;
- des consultations thématiques ;
- des journaux d’actes ;
- des votes correctifs ;
- des obligations d’explication.

Elle peut aussi aider les mandataires eux-mêmes.

Un mandataire peut publier ses suggestions, ses recommandations, ses votes, ses raisons, ses incertitudes et ses conflits d’intérêts. Il devient alors non seulement représentant, mais agent civique responsable.

Dans cette perspective, Kudocracy ne remplace pas la représentation. Elle la désenclave.

Elle donne au corps politique les moyens de décider directement lorsque c’est pertinent, de contrôler les mandataires lorsque c’est nécessaire, et de bénéficier d’orientations civiques traçables lorsque la complexité l’exige.

---

# 10. Différence avec les plateformes de recommandation commerciales

La notion de suggestion civique permet de marquer une rupture avec les systèmes de recommandation commerciaux.

Les plateformes commerciales recommandent souvent des contenus ou comportements selon des objectifs implicites : engagement, rétention, publicité, temps d’écran, viralité, polarisation rentable. Le terme même de recommandation y est déjà ambigu : il donne l’apparence d’un conseil utile alors qu’il sert souvent une fonction d’optimisation opaque.

Le citoyen ne sait pas toujours pourquoi il voit tel contenu plutôt qu’un autre. Il ne contrôle pas réellement les critères de recommandation.

Kudocracy doit éviter cette ambiguïté. C’est pourquoi son mode par défaut doit être la suggestion civique : une ouverture explicite de possibilités, non une poussée comportementale.

Une suggestion civique doit être :

- explicite ;
- motivée ;
- non prescriptive par défaut ;
- auditable ;
- comparable ;
- paramétrable ;
- révocable dans ses effets ;
- orientée vers la capacité de décision du citoyen ;
- non orientée vers sa captation attentionnelle.

Le but n’est pas d’augmenter l’engagement. Le but est d’augmenter la capacité civique.

Une démocratie assistée par agents ne peut être légitime que si les agents renforcent l’autonomie du citoyen au lieu de l’affaiblir.

---

# 11. Kudocracy comme autonomie de capacité civique

Kudocracy s’inscrit dans la logique de l’autonomie de capacité.

La démocratie ne se réduit pas à la possession abstraite d’un droit. Elle exige la capacité réelle d’exercer ce droit.

Un citoyen submergé d’informations, exposé à des manipulations, privé de temps, de méthode ou de soutien cognitif, reste formellement souverain mais pratiquement affaibli.

Kudocracy cherche à combler cet écart.

Elle ne prétend pas que chacun devienne expert en tout. Elle propose de rendre la compétence circulante, vérifiable et réversible.

Elle transforme la confiance en objet civique explicite.

La souveraineté démocratique devient alors moins une fiction individuelle qu’une capacité distribuée :

- capacité de formuler des propositions ;
- capacité de comprendre leurs effets ;
- capacité de recevoir des suggestions ;
- capacité de comparer les suggestions et recommandations ;
- capacité de décider ;
- capacité de différer ;
- capacité d’amender ;
- capacité de revenir sur une décision ;
- capacité de contrôler ceux qui influencent ou exécutent.

---

# 12. Inseme : prolongement en gestation

Kudocracy a vocation à trouver une première forme expérimentale dans la plateforme Inseme.

Le développement d’un MVP est en gestation, mais il ne constitue pas l’objet principal du présent document.

À ce stade, l’enjeu prioritaire est de formaliser correctement le modèle : distinguer votation et élection, suggestion et recommandation, recommandation et délégation, agent suggestif et mandataire, assistance IA personnelle et manipulation algorithmique.

Le prototype viendra ensuite comme expérimentation concrète d’une hypothèse démocratique plus générale.

---

# 13. État de l’art minimal

La démocratie liquide est généralement analysée comme un vote par délégation transitive, où un citoyen peut voter directement ou confier son vote à un autre participant.

La littérature identifie plusieurs problèmes importants :

- cycles de délégation ;
- perte possible de rationalité individuelle lorsque les propositions sont interdépendantes ;
- concentration des délégations ;
- réduction de la diversité des sources d’information ;
- fragilité en cas de mauvaise identification des experts ;
- tension entre anonymat, transparence et robustesse ;
- difficulté à garantir l’explicabilité des délégations.

Ces limites ne disqualifient pas la démocratie liquide. Elles montrent qu’un transfert direct de pouvoir de vote n’est pas toujours la meilleure unité de base.

Kudocracy propose donc une unité plus faible et plus inspectable : la suggestion.

Elle ne supprime ni la recommandation ni la délégation. Elle place la suggestion avant la recommandation, puis la recommandation avant la délégation, comme une échelle de force civique explicite.

Références de départ :

- Christoff, Z., & Grossi, D. (2017). *Binary Voting with Delegable Proxy: An Analysis of Liquid Democracy*. Electronic Proceedings in Theoretical Computer Science, 251, 134–150. https://doi.org/10.4204/EPTCS.251.10
- Christoff, Z., & Grossi, D. (2016). *Liquid Democracy: An Analysis in Binary Aggregation and Diffusion*. arXiv. https://arxiv.org/abs/1612.08048
- Campbell, J., Casella, A., de Lara, L., Mooers, V. R., & Ravindran, D. (2022). *Liquid Democracy. Two Experiments on Delegation in Voting*. NBER Working Paper 30794. https://www.nber.org/papers/w30794
- Utke, M., & Schmidt-Kraepelin, U. (2023). *Anonymous and Copy-Robust Delegations for Liquid Democracy*. arXiv. https://arxiv.org/abs/2307.01174
- Chancellerie fédérale suisse. *Votations populaires*. https://www.ch.ch/fr/votations-et-elections/votations/

---

# 14. Passage au crible de la seconde méthode

Cette section applique au présent texte les exigences de la seconde méthode : expliciter la thèse, distinguer les niveaux d’affirmation, formuler les objections fortes, indiquer les conditions de réfutation et ouvrir les continuations.

## 14.1. Thèse centrale testée

> **Kudocracy augmente la capacité démocratique lorsque des citoyens votent sur des propositions en s’appuyant d’abord sur des suggestions civiques traçables, puis éventuellement sur des recommandations plus fortes ou des délégations explicites, sans abandonner leur capacité de décision finale.**

Cette thèse n’est pas une certitude. C’est une hypothèse de recherche appliquée.

## 14.2. Statut épistémique des affirmations

| Affirmation | Statut |
|---|---|
| La démocratie liquide existe comme modèle théorique et expérimental | Fait établi |
| Les votations sur propositions sont distinctes des élections de représentants | Distinction institutionnelle solide |
| La délégation liquide peut produire concentration, cycles ou fragilités informationnelles | Appuyé par la littérature |
| La suggestion est moins forte que la recommandation | Définition conceptuelle |
| La recommandation est moins forte que la délégation | Définition conceptuelle |
| Une suggestion traçable peut augmenter la capacité de décision | Hypothèse principale |
| Un agent IA personnel peut protéger la cohérence civique de son propriétaire | Hypothèse technique et éthique |
| Kudocracy peut améliorer Inseme | Hypothèse de développement |
| Kudocracy peut fonctionner à grande échelle | Hypothèse non démontrée |

## 14.3. Claims vérifiables

### K1 — Distinction votation/élection

**Claim.** Kudocracy doit être évaluée comme système de votation sur propositions, non comme système d’élection représentative.

**Test.** Toute critique assimilant Kudocracy à un remplacement complet des élus ou mandataires doit être reformulée : vise-t-elle les votations, les mandats, ou leur articulation ?

**Condition de révision.** Si le modèle ne permet pas de distinguer clairement les propositions, les mandataires et les actes d’exécution, il doit être réécrit.

### K2 — Suggestion avant recommandation, recommandation avant délégation

**Claim.** La suggestion civique est une unité démocratique plus faible, plus ouverte et moins directive que la recommandation ; la recommandation est elle-même plus faible et plus réversible que la délégation du vote.

**Test.** Comparer, sur un cas simple, les effets d’une suggestion, d’une recommandation et d’une délégation automatique.

**Condition de révision.** Si les citoyens suivent mécaniquement les suggestions comme des prescriptions, la différence pratique entre suggestion, recommandation et délégation devient insuffisante.

### K3 — Granularité

**Claim.** La granularité thématique augmente la qualité de l’orientation civique.

**Test.** Observer si les citoyens utilisent réellement plusieurs agents selon les domaines, ou s’ils se regroupent autour de quelques agents généralistes dominants.

**Condition de révision.** Si la granularité théorique se transforme en concentration réelle, le modèle doit intégrer des limites, alertes ou mécanismes anti-capture.

### K4 — Agent IA personnel

**Claim.** Un agent IA personnel contrôlé par le citoyen peut réduire le risque de manipulation et améliorer la cohérence décisionnelle.

**Test.** Simuler des propositions contradictoires et mesurer si l’agent personnel détecte les incohérences, conflits d’intérêts et changements de valeurs.

**Condition de révision.** Si l’agent personnel dépend de la plateforme ou oriente l’utilisateur selon des critères opaques, il cesse d’être protecteur.

### K5 — Traçabilité proportionnelle

**Claim.** La traçabilité doit augmenter avec le pouvoir d’influence exercé sur le commun.

**Test.** Définir des seuils : citoyen ordinaire, agent suggestif, agent recommandateur, agent influent, mandataire, institution, plateforme.

**Condition de révision.** Si la traçabilité produit une surveillance généralisée des citoyens ordinaires, le modèle échoue éthiquement.

### K6 — Adjacent aux mandataires

**Claim.** Kudocracy peut coexister avec des mandataires sans se confondre avec eux.

**Test.** Décrire un cas institutionnel où des mandataires exécutent, tandis que les citoyens votent sur certaines propositions et contrôlent les mandats.

**Condition de révision.** Si le modèle bloque l’action des mandataires ou crée une instabilité permanente, il doit être limité à certains types de décisions.

### K7 — Non-pression algorithmique

**Claim.** Une interface fondée sur des suggestions non prescriptives préserve mieux le sentiment de souveraineté citoyenne qu’une interface fondée sur des recommandations de vote par défaut.

**Test.** Comparer deux interfaces expérimentales : l’une suggérant des questions, arguments et conséquences ; l’autre proposant directement un vote recommandé.

**Condition de révision.** Si l’interface de suggestion produit la même pression comportementale qu’une recommandation de vote, elle doit être redessinée.

---

# 15. Objections et réponses provisoires

## Objection 1 — “Ce n’est qu’un vote en ligne de plus.”

**Réponse.** Non. Le vote en ligne n’est qu’un canal. Kudocracy porte sur la structure de l’influence civique : propositions, suggestions, recommandations, abonnements, agents, traçabilité, révocabilité, agent personnel.

Le cœur n’est pas le clic de vote. Le cœur est la chaîne d’orientation auditable qui précède la décision.

## Objection 2 — “Les citoyens suivront aveuglément les agents populaires.”

**Réponse.** C’est un risque réel. Mais ce risque existe déjà avec les partis, médias, influenceurs et leaders d’opinion.

Kudocracy ne supprime pas l’influence. Elle la rend visible.

Le système doit cependant intégrer des garde-fous : pluralité des suggestions, comparaison contradictoire, alertes de concentration, justification obligatoire pour les recommandations fortes, révocation simple.

## Objection 3 — “L’IA personnelle peut devenir manipulatrice.”

**Réponse.** Oui, si elle est contrôlée par la plateforme, par un parti, par un fournisseur opaque ou par un modèle non vérifiable.

C’est pourquoi l’agent IA personnel doit être conçu comme agent du citoyen, non comme agent de la plateforme.

La condition de légitimité est l’alignement institutionnel : qui contrôle l’agent, qui le paramètre, qui audite ses suggestions et recommandations, qui peut le remplacer ?

## Objection 4 — “La traçabilité publique menace la vie privée.”

**Réponse.** Elle la menace si elle est mal conçue.

La règle doit être proportionnelle : protéger la vie privée des citoyens ordinaires, mais rendre auditables les actes publics d’influence et les mandats.

L’objectif n’est pas de surveiller les opinions privées. L’objectif est de contrôler les chaînes d’influence qui prétendent orienter la décision commune.

## Objection 5 — “Les mandataires deviendront inutiles.”

**Réponse.** Non. Kudocracy ne prétend pas remplacer tous les mandataires.

Elle traite prioritairement des votations sur propositions. Les mandataires restent nécessaires pour exécuter, négocier, représenter, gérer et assumer la continuité.

Kudocracy sert à mieux encadrer les mandats, non à nier toute fonction mandataire.

## Objection 6 — “Le système sera trop complexe.”

**Réponse.** La complexité existe déjà. Elle est simplement cachée dans les partis, médias, cabinets, réseaux d’influence et algorithmes de plateforme.

Kudocracy doit éviter d’ajouter une complexité illisible. Elle doit au contraire rendre la complexité navigable : propositions claires, suggestions lisibles, recommandations explicites, agent personnel, comparaisons simples, droit de reprise.

## Objection 7 — “La suggestion n’empêche pas la manipulation.”

**Réponse.** Elle ne l’empêche pas mécaniquement. Elle crée des prises pour la détecter, la documenter, l’imputer et la corriger.

Une démocratie robuste ne promet pas l’absence de manipulation. Elle promet que la manipulation peut être rendue visible, contestée et sanctionnée.

## Objection 8 — “Les votations permanentes fatigueront les citoyens.”

**Réponse.** C’est un risque sérieux. Kudocracy ne doit pas produire une injonction permanente à voter.

La suggestion, l’abonnement, la recommandation explicite, la délégation conditionnelle et l’agent personnel servent précisément à réduire la charge cognitive sans supprimer le droit de reprise.

Le bon critère n’est pas le nombre maximal de votes. C’est la capacité réelle de décider quand cela compte.

## Objection 9 — “La suggestion est trop faible pour aider réellement.”

**Réponse.** La suggestion n’interdit pas la recommandation. Elle l’encadre.

Le modèle ne refuse pas qu’un agent dise : “je pense que cette option est préférable”. Il exige seulement que cette force directive soit nommée, justifiée et auditée.

## Objection 10 — “Le système sera capturé par les interfaces.”

**Réponse.** C’est une objection centrale.

Une interface peut transformer une suggestion en pression comportementale. Kudocracy doit donc traiter l’interface comme un organe politique, non comme un simple habillage technique.

---

# 16. Conditions d’échec

Kudocracy devrait être considérée comme défaillante si l’un des phénomènes suivants devient dominant :

1. Les citoyens ne distinguent plus suggestion, recommandation et délégation.
2. Quelques agents captent l’essentiel de l’influence.
3. Les suggestions deviennent des prescriptions déguisées.
4. Les recommandations deviennent opaques ou non justifiées.
5. Les agents IA produisent des recommandations de vote par défaut.
6. L’interface exerce une pression algorithmique sur le vote.
7. L’agent IA personnel est contrôlé par la plateforme plutôt que par le citoyen.
8. La traçabilité se transforme en surveillance sociale des citoyens ordinaires.
9. Les mandataires ne peuvent plus agir efficacement.
10. Les votations deviennent trop nombreuses et produisent fatigue ou abstention massive.
11. Les propositions sont mal formulées, ambiguës ou manipulatoires.
12. Le système favorise les acteurs déjà puissants.
13. Les données civiques deviennent captives d’un fournisseur non auditable.
14. Les citoyens ne disposent plus d’un droit effectif de reprise.

Ces conditions d’échec ne sont pas des détails secondaires. Elles doivent guider la conception.

---

# 17. Garde-fous minimaux

## 17.1. Clarté des propositions

Une votation doit porter sur une proposition formulée clairement.

Une proposition doit indiquer :

- son objet ;
- son périmètre ;
- ses effets attendus ;
- ses coûts connus ;
- ses incertitudes ;
- sa durée ;
- ses conditions de révision.

## 17.2. Justification des suggestions et recommandations

Un agent suggestif doit fournir une justification minimale lorsque sa suggestion prétend orienter une décision commune.

Une suggestion sans justification est un signal faible. Une suggestion justifiée devient un objet discutable.

Une recommandation forte doit fournir une justification plus complète, parce qu’elle oriente plus directement le jugement.

## 17.3. Révocabilité

Tout abonnement ou délégation doit être révocable.

La révocation doit être simple, effective et traçable.

## 17.4. Pluralité

Le système doit rendre visibles les suggestions et recommandations divergentes.

Une démocratie assistée par agents ne doit pas produire une monoculture d’influence.

## 17.5. Auditabilité des agents influents

Les agents qui acquièrent une influence significative doivent être plus fortement auditables.

L’audit doit porter sur leurs suggestions publiques, leurs recommandations publiques, leurs sources, leurs conflits d’intérêts et leur historique, non sur leur vie privée sans lien avec leur rôle civique.

## 17.6. Contrôle citoyen de l’agent personnel

L’agent IA personnel doit pouvoir être corrigé, remplacé, exporté ou désactivé.

Il doit expliquer ses suggestions, distinguer ses recommandations fortes, et signaler ses incertitudes.

## 17.7. Séparation des rôles

Il faut distinguer :

- citoyen votant ;
- agent personnel ;
- agent suggestif ;
- agent recommandateur ;
- mandataire ;
- plateforme ;
- administrateur technique ;
- autorité d’audit.

La confusion des rôles est une source majeure de capture.

## 17.8. Absence de pression algorithmique

Kudocracy doit interdire la pression algorithmique sur le vote.

Une interface civique ne doit pas :

- masquer les options minoritaires ;
- présenter une option comme évidente sans justification ;
- confondre popularité et légitimité ;
- produire un bouton de vote prérempli par défaut ;
- transformer une suggestion en injonction visuelle ;
- favoriser systématiquement les agents dominants ;
- pousser le citoyen à voter vite lorsque la proposition exige réflexion ;
- produire une recommandation forte sans l’indiquer comme telle.

L’interface doit au contraire rendre possible :

- le doute ;
- l’abstention ;
- l’ajournement ;
- la demande d’amendement ;
- la comparaison contradictoire ;
- la reprise de contrôle ;
- le refus de suivre un agent.

---

# 18. Hypothèses de recherche

## H1 — Suggestion civique traçable

Une suggestion civique traçable augmente la qualité perçue du vote par rapport à une recommandation opaque ou à une influence non déclarée.

## H2 — Agent personnel

Un agent IA personnel contrôlé par le citoyen réduit le risque de vote incohérent avec les valeurs déclarées du citoyen.

## H3 — Pluralité d’agents

La comparaison de plusieurs agents suggestifs ou recommandateurs réduit la dépendance à une source unique d’influence.

## H4 — Granularité thématique

La granularité par domaines produit des décisions plus acceptables que la confiance globale envers un seul représentant ou parti.

## H5 — Traçabilité proportionnelle

La traçabilité proportionnelle au pouvoir d’influence est mieux acceptée qu’une publicité uniforme de tous les actes civiques.

## H6 — Mandataires contrôlés

Les mandataires restent nécessaires, mais leur légitimité augmente lorsque leurs actes sont contrôlables par des votations, suggestions et recommandations publiques.

## H7 — Non-pression algorithmique

Une interface fondée sur des suggestions non prescriptives préserve mieux le sentiment de souveraineté citoyenne qu’une interface fondée sur des recommandations de vote par défaut.

---

# 19. Programme expérimental minimal

Le MVP Inseme est en gestation. Sans en détailler ici l’architecture, l’expérimentation devra permettre de tester au moins :

- une proposition claire ;
- plusieurs agents suggestifs ;
- des suggestions justifiées ;
- des recommandations explicitement signalées lorsqu’elles existent ;
- des abonnements volontaires ;
- la possibilité de suivre ou non une suggestion ;
- la possibilité de comparer plusieurs suggestions ;
- une révocation simple ;
- une trace exploitable ;
- une première assistance par agent IA personnel ;
- une distinction nette entre votation, suggestion, recommandation, délégation et mandat ;
- une interface sans pression algorithmique.

Le prototype n’est pas la preuve. Il sera un instrument de réfutation ou d’amélioration.

---

# 20. Discussion : une démocratie orientable, non pilotée

Kudocracy part d’un constat : la décision démocratique est déjà orientée.

Elle est orientée par les médias, les partis, les réseaux sociaux, les intérêts économiques, les experts, les affects, les habitudes, les plateformes et les algorithmes.

La question n’est donc pas de savoir s’il faut de l’influence ou non. Il y aura toujours influence.

La question est :

> **Quelle influence, exercée par qui, selon quelles règles, avec quelle traçabilité, au bénéfice de qui, et avec quel droit de reprise ?**

Kudocracy propose une réponse :

- l’influence doit être explicite ;
- les suggestions doivent être non prescriptives par défaut ;
- les recommandations doivent être signalées comme plus fortes ;
- les abonnements doivent être volontaires ;
- les délégations doivent être réversibles ;
- les agents personnels doivent servir leurs propriétaires ;
- les mandataires doivent rester contrôlables ;
- les votations doivent porter sur des propositions claires ;
- les traces doivent permettre l’audit sans détruire la vie privée.

Il ne s’agit pas de piloter les citoyens. Il s’agit de leur donner les moyens de s’orienter.

---

# 21. Conclusion provisoire

Kudocracy n’est pas un système d’élection.

C’est une architecture de votations assistées par suggestions civiques traçables, dans laquelle la recommandation reste possible mais explicitement plus forte, plus encadrée et toujours subordonnée au droit de reprise du citoyen.

Elle ne supprime pas les mandataires. Elle les situe dans un espace démocratique plus large, où les citoyens peuvent aussi décider directement sur des propositions, recevoir des suggestions, comparer des agents, suivre ou contredire, déléguer explicitement et reprendre la main.

Son originalité tient à cinq déplacements :

1. du vote pour des personnes vers la votation sur propositions ;
2. de la délégation du pouvoir vers la suggestion préalable ;
3. de la recommandation opaque vers la suggestion traçable et la recommandation explicitement signalée ;
4. de l’IA de plateforme vers l’agent IA personnel du citoyen ;
5. de l’influence algorithmique vers la non-pression algorithmique.

La démocratie liquide a montré qu’il était possible de fluidifier la représentation. Kudocracy propose de fluidifier d’abord l’orientation civique, sans transformer l’orientation en prescription.

La démocratie assistée par agents ne doit pas transformer le citoyen en terminal d’exécution d’un calcul politique. Elle doit lui donner les moyens de comprendre, comparer, différer, contredire, amender, déléguer explicitement ou décider.

> **En démocratie, l’IA suggère. Le citoyen décide.**

Formule noyau :

> **Kudocracy ne remplace pas le citoyen par un agent. Elle donne au citoyen des agents capables de suggérer, comparer, alerter et expliquer, afin qu’il ne soit pas remplacé par le système.**

---

# 22. Continuation

## 22.1. Objet de la continuation

La présente continuation permet de reprendre ce travail dans un autre agent, une autre conversation ou une future itération du dépôt.

Elle est auto-descriptive : elle contient suffisamment de contexte pour permettre une reprise sans accès intégral à la conversation d’origine.

## 22.2. État courant

Document produit :

- fichier prévu : `barons-Mariani/research/kudocracy.md`
- version : `0.2`
- statut : working paper — révision conceptuelle
- langue : français, abstract en anglais
- thèse : Kudocracy est une couche de suggestion civique traçable pour des votations sur propositions, complémentaire de la démocratie liquide et adjacente aux mandataires.
- correction principale depuis v0.1 : la recommandation n’est plus le mode par défaut ; elle devient une forme plus forte de suggestion.
- contrainte forte intégrée : Kudocracy porte sur des **votations**, non sur des élections ; elle n’implique pas de se passer de mandataires.

## 22.3. Décisions prises

1. Ne pas centrer le texte sur le MVP.
2. Mentionner seulement que le MVP Inseme est en gestation.
3. Distinguer explicitement :
   - votation ;
   - élection ;
   - suggestion ;
   - recommandation ;
   - délégation ;
   - prescription ;
   - mandat ;
   - agent personnel ;
   - agent suggestif ;
   - agent recommandateur.
4. Faire de la suggestion civique le mode par défaut.
5. Conserver la recommandation comme forme plus forte, plus encadrée.
6. Ajouter la non-pression algorithmique comme garde-fou.
7. Appliquer la seconde méthode par :
   - thèse testée ;
   - statut épistémique ;
   - claims vérifiables ;
   - objections ;
   - conditions d’échec ;
   - hypothèses de recherche ;
   - continuation.

## 22.4. Prochaines branches possibles

### Branche A — Renforcement académique

Ajouter une revue de littérature plus complète :

- démocratie liquide ;
- démocratie délibérative ;
- systèmes de recommandation ;
- IA personnelle ;
- vote électronique ;
- démocratie directe suisse ;
- mandats et théorie de la représentation ;
- dark patterns et pression algorithmique ;
- human agency in AI-assisted decision-making.

### Branche B — Formalisation technique

Produire un schéma minimal :

- `proposal`
- `civic_suggestion`
- `civic_recommendation`
- `agent`
- `subscription`
- `vote`
- `delegation`
- `mandate`
- `audit_log`

Cette branche peut aller dans Inseme, pas nécessairement dans ce document.

### Branche C — Formalisation juridique

Analyser :

- valeur juridique d’une votation ;
- statut d’un agent suggestif ;
- statut d’une recommandation civique ;
- responsabilité d’un mandataire ;
- protection des données ;
- publicité des actes civiques ;
- limites du vote public ;
- articulation avec associations, communes, collectifs et plateformes.

### Branche D — Cas d’usage corse

Construire trois cas :

1. proposition communale simple ;
2. consultation associative ;
3. votation territoriale expérimentale.

### Branche E — Agent IA personnel

Développer la doctrine :

- agent du citoyen, non de la plateforme ;
- mémoire civique ;
- protection des valeurs ;
- détection des contradictions ;
- exportabilité ;
- auditabilité ;
- minimisation des données ;
- refus de recommander lorsque l’information est insuffisante.

## 22.5. Objections à traiter en priorité

1. Risque de surveillance sociale.
2. Risque de capture par agents dominants.
3. Risque d’illusion de contrôle par agent IA personnel.
4. Risque de complexité excessive.
5. Risque de confusion entre votation et référendum juridiquement contraignant.
6. Risque d’affaiblissement des mandataires utiles.
7. Risque d’instrumentalisation par des plateformes privées.
8. Risque de pression algorithmique invisible.
9. Risque de transformation des suggestions en prescriptions déguisées.

## 22.6. Phrase noyau à préserver

> **Kudocracy ne remplace pas le citoyen par un agent. Elle donne au citoyen des agents capables de suggérer, comparer, alerter et expliquer, afin qu’il ne soit pas remplacé par le système.**

## 22.7. Instruction de reprise

Pour continuer ce travail :

1. lire le présent document ;
2. choisir une branche de continuation ;
3. conserver la distinction votation / élection ;
4. ne pas présenter Kudocracy comme suppression des mandataires ;
5. ne pas revenir à la recommandation comme mode par défaut ;
6. renforcer les objections avant de renforcer la thèse ;
7. produire une version `v0.3` avec changelog explicite ;
8. maintenir le document compatible avec la seconde méthode.

---

# 23. Références initiales

Campbell, J., Casella, A., de Lara, L., Mooers, V. R., & Ravindran, D. (2022). *Liquid Democracy. Two Experiments on Delegation in Voting*. NBER Working Paper 30794. https://www.nber.org/papers/w30794

Chancellerie fédérale suisse. *Votations populaires*. https://www.ch.ch/fr/votations-et-elections/votations/

Christoff, Z., & Grossi, D. (2016). *Liquid Democracy: An Analysis in Binary Aggregation and Diffusion*. arXiv. https://arxiv.org/abs/1612.08048

Christoff, Z., & Grossi, D. (2017). *Binary Voting with Delegable Proxy: An Analysis of Liquid Democracy*. Electronic Proceedings in Theoretical Computer Science, 251, 134–150. https://doi.org/10.4204/EPTCS.251.10

Utke, M., & Schmidt-Kraepelin, U. (2023). *Anonymous and Copy-Robust Delegations for Liquid Democracy*. arXiv. https://arxiv.org/abs/2307.01174

Robert, J. H. N. (2026). *Discours de la seconde méthode*. Institut Mariani / C.O.R.S.I.C.A. https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md

Robert, J. H. N. (2026). *Autonomie de capacité*. Institut Mariani / C.O.R.S.I.C.A. https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/autonomia.md

Robert, J. H. N. (2026). *Cognitive Packets*. Cogentia. https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md

Robert, J. H. N. (2026). *Cogentia Commons — Method Packets, Continuations, and the Generative Corpus*. Cogentia. https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cogentia_commons_method_packets.md

<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [La seconde méthode comme généralisation prudente de l’agile](agile.md)
- [Mauvaise calibration métacognitive face aux intelligences xénoformes](alien_academic.md)
- [Verticalisation de la Chrétienté](christianity_verticalization.md)
- [Concept Index — barons-Mariani](concepts.md)
- [Corpus Status — barons-Mariani](corpus-status.md)
- [Research Index — barons-Mariani](index.md)

<!-- END_AUTO: backlinks -->
