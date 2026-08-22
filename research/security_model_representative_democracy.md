---
title: "Une théorie de sécurité de la démocratie représentative"
subtitle: "Du principal-agent à la non-auto-élévation des privilèges politiques"
author: "Jean Hugues Noël Robert"
status: "document source — recherche — doctrinal — validé pour publication"
version: "0.4"
date: "2026-08-22"
license: "CC BY-SA 4.0"
language: "fr"
repository: "barons-Mariani"
canonical_path: "barons-Mariani/research/security_model_representative_democracy.md"
source_status: "source souveraine du corpus politique et de recherche"
review_status: "revue adverse Grok 4.5 intégrée ; stress-test de droit public intégré ; principe Selection is not security ajouté après contrôle de non-régression sémantique"
publication_history:
  - date: "2026-08-21"
    event: "publication prématurée"
    human_assessment: "sans conséquence grave"
    cause: "écriture GitHub avant revue adverse et validation humaine requises"
  - date: "2026-08-21"
    event: "revue adverse"
    reviewer: "Grok 4.5"
  - date: "2026-08-21"
    event: "validation humaine et autorisation de publication"
    validator: "Jean Hugues"
  - date: "2026-08-22"
    event: "extension doctrinale"
    change: "explicitation de la sécurité par sélection, du principe Selection is not security et de la faible opposabilité substantielle du mandat représentatif"
    preservation: "ajout conservatif ; structure et thèses antérieures préservées"
related_research:
  - "barons-Mariani/research/non_auto_elevation_privileges.md"
  - "barons-Mariani/research/democratie_crise_mandats_express.md"
  - "barons-Mariani/research/traceabilite_des_actes.md"
  - "cogentia/research/mandated_fast_democracy.md"
related_projects:
  - "Autonomie de Capacité"
  - "Cogentia"
  - "Kudocracy"
keywords:
  - "démocratie représentative"
  - "sécurité"
  - "principal-agent"
  - "least privilege"
  - "privilege escalation"
  - "révocabilité"
  - "traçabilité"
  - "capture institutionnelle"
  - "souveraineté effective"
  - "IA agentique"
  - "selection is not security"
  - "principe de distinction"
---

# Une théorie de sécurité de la démocratie représentative

## Résumé

La démocratie représentative peut être étudiée comme un système de délégation de capacités entre un **principal politique**, le peuple souverain, et des **agents**, ses représentants. La théorie principal-agent fournit depuis longtemps une partie de ce vocabulaire. L'hypothèse étudiée ici consiste à franchir une étape supplémentaire : appliquer à la représentation politique les principes de sécurité employés pour gouverner des agents puissants, notamment les agents d'intelligence artificielle.

Un système sûr ne suppose pas l'agent vertueux. Il borne ses privilèges, trace ses actes, sépare action et autorisation, prévoit la révocation et interdit l'auto-élévation des privilèges. Or ces garanties paraissent plus naturelles pour un agent logiciel ou un syndic de copropriété que pour un représentant politique.

> **Pourquoi accepter d'un agent politique ce que nous considérerions comme une vulnérabilité de sécurité chez un agent artificiel ou un mandataire ordinaire ?**

La thèse est systémique et non morale : une architecture de pouvoir doit rester sûre lorsque ses agents se trompent, poursuivent leurs intérêts, subissent des conflits d'intérêts ou cherchent à conserver leurs privilèges.

La contribution revendiquée reste une **hypothèse d'originalité à falsifier**. Elle porte moins sur chacune des briques — délégation, accountability, recall, checks and balances, least privilege, audit — que sur leur traduction systématique dans un même *security model* et sur quatre objets candidats : **non-auto-élévation**, **Follow the Power**, **test capacitaire du désaccord** et application aux transferts d'autonomie territoriale.

## 1. De la vertu à l'architecture

En sécurité, on ne construit pas un système en supposant que tous ses agents resteront vertueux. L'erreur, la compromission et le conflit d'intérêts sont des propriétés à contenir.

```text
bons individus + architecture vulnérable != système sûr
```

La démocratie représentative devrait satisfaire la même exigence : **rester démocratique même lorsque certains représentants ne le sont pas parfaitement**.

Le problème étudié n'est donc pas « les élus sont-ils vertueux ? », mais : **quelles propriétés du système empêchent un agent politique de convertir une délégation temporaire en avantage structurel sur son principal ?**

### 1.1 De la sélection des meilleurs à la sécurité de l'architecture

Le gouvernement représentatif peut être lu comme reposant partiellement sur une **stratégie de confiance par sélection** : choisir périodiquement des représentants jugés suffisamment aptes pour leur reconnaître ensuite une large autonomie de jugement. L'interdiction du mandat impératif est cohérente avec cette architecture : le représentant est sélectionné pour décider, délibérer et exercer son jugement, non pour exécuter continuellement les instructions juridiquement opposables de ses électeurs.

Cette logique partage une intuition avec l'idéal ancien du gouvernement des meilleurs, notamment platonicien, sans s'y identifier historiquement ni institutionnellement. Dans le gouvernement représentatif, l'élection ne démontre pas la sagesse : elle sélectionne les candidats capables de remporter la procédure électorale. Le **principe de distinction** étudié par Bernard Manin et les modèles contemporains de *selection* en représentation permettent de traiter cette propriété sans supposer que les élus seraient objectivement « les meilleurs ».

Le point de sécurité est ailleurs : **la qualité supposée de la sélection ne peut constituer à elle seule une propriété suffisante de sécurité**.

```text
sélection d'un agent réputé bon
!=
système sûr
```

Un système informatique critique ne supprime pas permissions fines, observabilité, révocation, expiration ou réautorisation au motif que l'agent a été soigneusement sélectionné. De même, un syndic choisi par les copropriétaires reste soumis à un mandat, à des comptes et à des mécanismes de contrôle.

> **Selection is not security. La sélection d'un agent ne remplace pas la sécurité de l'architecture qui gouverne ses capacités.**

Cette proposition déplace la critique. La question n'est pas principalement de savoir si les électeurs choisissent de « bons » représentants, mais **pourquoi la sûreté du système devrait dépendre aussi fortement de la réussite de cette sélection initiale**.

Schématiquement, le régime représentatif classique combine souvent :

```text
sélection électorale
-> forte autonomie du représentant
-> faible opposabilité substantielle du mandat aux électeurs
-> contrôle surtout indirect et ex post
-> sanction périodique par renouvellement ou non-renouvellement
```

Une théorie de sécurité ajoute une seconde ligne de défense : même correctement sélectionné, l'agent reste borné, observable, contrôlable et récupérable par le système dont procèdent ses capacités.

## 2. Modèle minimal, puis correction multi-principals

Le modèle heuristique minimal est :

```text
PRINCIPAL : le peuple souverain
AGENT     : le représentant mandaté
```

Le principal délègue des capacités à l'agent pour qu'il agisse en son nom. Cette délégation ne devrait pas transférer la propriété de la source du pouvoir.

> **Un mandat autorise l'exercice d'un pouvoir. Il n'autorise pas l'appropriation de sa source.**

Mais le « peuple » n'est pas l'équivalent simple d'un utilisateur unique. La démocratie est un système **multi-principals** : citoyens individuels, majorité politique momentanée, minorités, collectivités, générations présentes et futures peuvent avoir des intérêts divergents. Les droits fondamentaux et les garanties constitutionnelles peuvent alors être compris comme des bornes empêchant un principal momentané de capturer irréversiblement les capacités des autres.

Cette correction interdit une transposition naïve de l'informatique au droit constitutionnel. Le modèle principal-agent reste un instrument d'analyse, non une définition exhaustive de la représentation politique.

## 3. Trois mandataires, une question

| Principal | Agent | Mécanisme principal de confiance | Attente de sécurité ordinaire |
|---|---|---|---|
| utilisateur | agent IA | sélection/configuration + contrôle continu | permissions bornées, logs, arrêt, approbation des actes sensibles |
| copropriétaires | syndic | sélection contractuelle + mandat | mandat borné, comptes, assemblée, contrôle, révocation |
| peuple | représentants | sélection électorale + sanction périodique | élection, publicité institutionnelle, contrôle beaucoup plus indirect |

La comparaison ne prétend pas à l'identité juridique des trois relations. Elle révèle une différence d'architecture : dans les deux premiers cas, la sélection de l'agent n'épuise manifestement pas la question de sa sécurité ; dans le troisième, une part beaucoup plus importante de la confiance est placée dans la sélection et le contrôle périodique.

> **Le mandataire peut-il augmenter lui-même les pouvoirs que le mandant lui a confiés ?**

Pour l'agent IA, ce serait un risque d'élévation de privilèges. Pour le syndic, une redéfinition unilatérale de son mandat contre les copropriétaires serait anormale. Pour le représentant politique, les représentants participent pourtant à la définition des pouvoirs de la représentation et des conditions de reprise directe de la décision par le peuple. Cette différence demande justification.

## 4. Trois niveaux à ne pas confondre

La revue adverse a fait apparaître une distinction nécessaire, notamment face au pouvoir constituant dérivé et à l'autonomie normale des institutions.

### A. Exercice du mandat

L'agent utilise les pouvoirs qui lui ont été conférés. C'est la fonction normale de la délégation.

### B. Auto-administration du mandat

L'institution règle son calendrier, ses procédures internes et son organisation dans les limites de compétences déjà conférées. Une démocratie fonctionnelle ne peut soumettre chaque acte d'administration interne à une autorisation populaire directe.

### C. Modification du rapport de capacité principal/agent

L'agent modifie les règles qui déterminent son propre pouvoir relativement au principal : durée, révocabilité, conditions de contrôle, capacité de décision directe du principal, étendue substantielle des prérogatives ou barrières à leur reprise.

C'est ici que le gate doit devenir plus fort.

> **Un agent peut administrer l'exercice de son mandat ; il ne peut modifier unilatéralement en sa faveur le rapport de capacité qui le lie à son principal.**

Cette formulation évite de qualifier abusivement toute évolution institutionnelle d'« élévation de privilèges » tout en isolant le risque de sécurité pertinent.

## 5. Invariants de sécurité

### 5.1 Non-auto-élévation

> **Aucun agent humain, institutionnel ou artificiel ne devrait pouvoir augmenter unilatéralement, en sa faveur, les pouvoirs qui déterminent son rapport de capacité avec le principal dont ils procèdent.**

Ce principe est normatif. En droit constitutionnel français positif, le Parlement participe notamment au pouvoir de révision prévu par l'article 89 ; la théorie proposée ici ne prétend pas que cette participation est actuellement illicite. Elle propose un critère de sécurité pour distinguer exercice constitutionnel et modification auto-intéressée du rapport de pouvoir.

### 5.2 Least privilege

L'agent ne reçoit que les capacités nécessaires à sa mission, dans le périmètre et pour la durée nécessaires. Transposition politique : subsidiarité, compétence attribuée et mandat borné.

### 5.3 Traçabilité des actes

Tout exercice significatif d'un pouvoir délégué doit permettre de répondre : qui a fait quoi, au nom de qui, avec quel mandat, sur quelle base, avec quelle autorisation, avec quel effet sur la distribution des pouvoirs, et comment l'acte peut être contesté.

La publicité brute n'est pas la traçabilité effective : des milliers de pages publiques mais cognitivement inexploitables ne suffisent pas.

### 5.4 Révocabilité

La traçabilité sans révocabilité permet de constater un abus mais pas d'interrompre le mandat qui le permet.

```text
mandater -> tracer -> contrôler -> corriger ou révoquer
```

La révocabilité n'est toutefois pas un bien sans coût : un mécanisme mal conçu peut favoriser harcèlement politique, instabilité permanente ou capture par une minorité fortement mobilisée. Le *recall* doit donc lui-même être sécurisé : seuils, délais, conditions et protections contre les usages abusifs.

### 5.5 Refus effectif de l'offre

Le contrôle du principal ne peut se réduire au choix périodique entre les agents proposés par le système. Un vote blanc comptabilisé mais sans effet décisionnel constitue un refus enregistré mais impuissant.

### 5.6 Reprise du contrôle

Le principal doit conserver une capacité effective de reprise : décision directe, référendum déclenchable, révocation, renouvellement forcé de l'offre électorale ou mécanisme équivalent. La forme est discutable ; l'invariant est la conservation d'une capacité de reprise compatible avec les droits fondamentaux et la pluralité des principals.

## 6. Test du désaccord

```text
Peuple = OUI ; représentants = NON
Qui gagne ?

Peuple = NON ; représentants = OUI
Qui gagne ?
```

Le pouvoir devient observable lorsque les volontés divergent.

> **Est souverain, au sens capacitaire, celui dont la décision peut effectivement prévaloir sur celle de son agent dans le domaine où il est légitime qu'il décide, sous réserve des droits fondamentaux et des garanties dues aux autres principals.**

Cette proposition est un test analytique, non une description du droit positif.

## 7. Stress-test de droit public français

Le droit positif français impose plusieurs corrections importantes à l'analogie du mandat.

L'article 3 de la Constitution dispose que la souveraineté nationale appartient au peuple, exercée par ses représentants et par la voie du référendum, et qu'aucune section du peuple ni aucun individu ne peut s'en attribuer l'exercice. L'article 27 dispose cependant que **tout mandat impératif est nul**. Le représentant parlementaire n'est donc pas, juridiquement, un mandataire civil soumis aux instructions permanentes de ses électeurs.

Cette objection ne détruit pas le modèle ; elle en fixe le statut. Le vocabulaire principal-agent sert ici à **tester les capacités et les contrôles**, non à prétendre que le mandat représentatif est juridiquement identique à un mandat privé.

Elle fait aussi apparaître une propriété remarquable du droit positif : une fois retranchées les obligations générales, les règles de probité, de transparence, d'incompatibilité, de procédure et de fonctionnement institutionnel, **le contenu substantiel du mandat parlementaire est faiblement opposable aux électeurs**. Le représentant n'est juridiquement tenu ni d'exécuter son programme électoral, ni de suivre les instructions de ses électeurs, ni de voter conformément à une volonté populaire ponctuellement mesurée. À l'échéance, l'habilitation expire ou peut être renouvelée ; la sanction du contenu de l'action est principalement politique et périodique.

Cette faible opposabilité n'est pas nécessairement une anomalie : elle protège l'autonomie de jugement, la délibération et la capacité de compromis du représentant. Mais elle rend d'autant plus importante la question architecturale posée ici : **si l'agent dispose volontairement d'une forte autonomie substantielle, quelles autres propriétés garantissent la sécurité de la délégation ?**

Deuxième objection : le Parlement participe légitimement à la production de la loi et, selon l'article 89, au pouvoir de révision constitutionnelle. Toute modification des institutions par des représentants ne peut donc être assimilée à une auto-élévation illégitime. Le test pertinent doit porter sur la **variation du rapport de capacité** et sur les gates applicables lorsque l'agent bénéficie lui-même de cette variation.

Troisième objection : une souveraineté populaire sans bornes peut devenir domination majoritaire. Le modèle doit donc être articulé aux droits fondamentaux, au contrôle juridictionnel et aux protections des minorités. Une « reprise du contrôle » n'est pas une permission de supprimer les garanties qui rendent possible l'existence politique des autres principals.

Quatrième objection : indépendance du représentant et accountability sont en tension. Une révocation instantanée à chaque divergence pourrait transformer le représentant en simple terminal de sondage et rendre impossibles compromis, délibération et décision de long terme. Le problème de sécurité n'est donc pas de supprimer toute autonomie de l'agent, mais de **rendre cette autonomie bornée, observable et récupérable**.

Conclusion du stress-test : la théorie survit si elle abandonne l'identification simpliste `élu = mandataire civil` et se présente comme une **couche de sécurité capacitaire complémentaire** de la théorie constitutionnelle classique.

## 8. Souveraineté formelle et souveraineté effective

La question de sécurité devient :

> **Quelles garanties empêchent l'exercice par représentation de devenir progressivement maîtrise de l'exercice par les représentants ?**

La titularité formelle doit être confrontée aux capacités effectives : initiative, veto, contrôle, révocation, information exploitable et possibilité de décision directe.

```text
owner(sovereignty) = people
```

ne renseigne pas à lui seul sur :

```text
who_can_trigger()
who_can_veto()
who_can_revoke()
who_can_change_permissions()
who_can_recover_control()
```

La théorie de sécurité s'intéresse précisément à cette seconde couche.

## 9. Urgence et mandats express

Une crise peut transformer la vitesse nécessaire en concentration de pouvoir. Les **mandats express** proposent l'inversion suivante : préparer démocratiquement la vitesse avant l'urgence.

```text
urgence accrue
-> mandat plus explicite
-> périmètre plus borné
-> trace plus forte
-> sunset automatique
-> revue obligatoire
```

L'agent bénéficiaire de pouvoirs d'urgence ne doit pas pouvoir, seul, créer, prolonger ou élargir l'état qui les justifie.

## 10. Capture sans complot : stigmergie institutionnelle

Une architecture capturante ne suppose pas une conspiration. Chaque génération hérite de règles et de privilèges. Les dispositifs favorables à l'appareil peuvent rencontrer moins d'incitations internes à leur suppression que les dispositifs réduisant sa latitude n'en rencontrent pour leur adoption.

```text
optimisations locales répétées
-> sélection institutionnelle
-> concentration émergente de capacité
```

Cette **stigmergie institutionnelle** reste une hypothèse à tester empiriquement. Elle ne doit pas être confondue avec un fait démontré. Sa conséquence méthodologique est déjà utile : changer les personnes ne suffit pas nécessairement à changer les incitations du système.

## 11. Pourquoi l'IA change la situation

Une justification historique de la délégation massive est capacitaire : aucun citoyen ne peut lire tous les textes, suivre tous les amendements, contrôler tous les budgets et vérifier tous les actes. L'IA réduit ce coût cognitif.

Un agent personnel peut surveiller les actes pertinents, relier votes et mandats, détecter les transferts de pouvoir, comparer engagements et actes, conserver les traces et aider le citoyen à exercer ses droits.

Le paradoxe devient alors :

> **Ce que nous apprenons à interdire aux agents IA, nous devrons finir par l'interdire aux agents politiques.**

Cette formule désigne une direction normative, non l'identité juridique des deux catégories d'agents.

Le modèle de représentation peut passer de `trust me` à `verify me`.

### 11.1 Le Twin doit subir son propre test

Le Personal Digital Twin qui augmente la capacité du citoyen ne doit pas devenir son nouveau gatekeeper. Il doit donc lui-même satisfaire les invariants : least privilege, mandat explicite, traçabilité, révocation, possibilité d'arrêt ou de bypass humain, et absence d'auto-élévation de privilèges.

La théorie est réflexive : **l'outil de contrôle doit être contrôlable**.

## 12. Follow the Power

La Traçabilité des actes peut devenir une comptabilité des capacités politiques :

```text
Qui possédait la capacité ?
Qui la transfère ?
À qui ?
Pour combien de temps ?
Sous quelles conditions ?
Qui peut la reprendre ?
Qui a autorisé le transfert ?
Qui gagne une capacité de veto, d'initiative ou de contrainte ?
Qui la perd ?
```

**Follow the Power** complète ainsi *Follow the Money*.

Une réforme qui augmente les capacités de l'appareil sans augmenter celles des citoyens modifie leur rapport de pouvoir même sans suppression formelle d'un droit.

### 12.1 Instrument minimal

Pour éviter que `Follow the Power` reste une simple formule, tout audit doit au minimum produire :

| Champ | Avant | Après | Delta |
|---|---|---|---|
| capacité de l'appareil | ? | ? | ? |
| capacité de l'habitant | ? | ? | ? |
| capacité de contrôle/reprise | ? | ? | ? |
| trace exploitable | ? | ? | ? |

Le prochain Reality Test consiste à remplir ce tableau sur **une compétence réelle** du projet d'autonomie corse à partir des textes applicables.

## 13. Cas d'étude : autonomie de la Corse

Un transfert de compétences de l'État vers la Collectivité de Corse augmente les capacités institutionnelles de cette dernière. Il faut donc poser une seconde question après « combien de pouvoir passe de Paris à Ajaccio ? » :

> **Comment évolue le rapport de capacité entre les habitants et les institutions qui exerceront ces nouveaux pouvoirs ?**

Si les capacités de l'appareil augmentent sans garantie d'augmentation correspondante des capacités des habitants, l'autonomie relative de l'appareil augmente par rapport à eux.

> **Plus de pouvoir sur nous n'est pas plus de pouvoir pour nous.**

Cette conclusion ne suppose aucune hypothèse sur la vertu ou les intentions individuelles des élus.

## 14. État de l'art et positionnement

Les briques sont anciennes ou établies : théorie principal-agent, accountability, représentation comme autorisation et sanction, recall, checks and balances, democratic backsliding, least privilege, contrôle d'accès, audit et sécurité agentique.

La littérature principal-agent sur les démocraties parlementaires décrit depuis longtemps les pertes d'agence possibles entre électeurs et représentants et traite l'accountability comme une question de design institutionnel. Les travaux contemporains sur la représentation rappellent toutefois que le modèle principal-agent n'épuise pas la notion de représentation : sélection, jugement autonome, délibération et pluralité des principals compliquent la métaphore. Le principe `Selection is not security` proposé ici ne nie pas la fonction démocratique de la sélection ; il affirme seulement que la sélection ne suffit pas, à elle seule, à garantir la sûreté du rapport de capacité.

Du côté agentique, les travaux NIST 2026 sur l'identité et l'autorisation des agents posent explicitement les questions de least privilege, délégation « on behalf of », révocation, preuve d'autorité, audit et non-répudiation. Cette convergence fournit un vocabulaire technique particulièrement utile pour réexaminer les délégations politiques.

### Hypothèse d'originalité à falsifier

La contribution candidate n'est pas chacune de ces briques mais leur **traduction systématique dans une théorie commune de sécurité de la représentation**, notamment :

1. `NO SELF-ESCALATION` appliqué au rapport de capacité représentant/représenté ;
2. `Follow the Power` comme comptabilité des transferts de capacités politiques ;
3. le **test du désaccord** comme mesure de souveraineté effective ;
4. l'audit simultané de l'autonomie de l'appareil et de l'**Autonomie de Capacité** des habitants ;
5. `SELECTION IS NOT SECURITY` comme séparation entre qualité supposée de l'agent et sûreté de l'architecture qui gouverne ses capacités.

Cette revendication doit rester falsifiable par la bibliographie et par des contre-exemples.

## 15. Spécification minimale

1. **Pouvoir minimal nécessaire** — aucun agent ne reçoit plus de capacité que nécessaire.
2. **Non-auto-élévation** — aucun agent ne modifie unilatéralement en sa faveur le rapport de capacité avec son principal.
3. **Traçabilité** — tout exercice significatif laisse une trace exploitable.
4. **Révocabilité sécurisée** — le principal peut retirer la délégation selon une procédure qui évite elle-même la capture.
5. **Refus effectif** — le principal peut refuser l'offre des agents.
6. **Reprise du contrôle** — le principal conserve une voie de décision directe compatible avec les droits fondamentaux.
7. **Réflexivité** — les outils de contrôle, y compris IA, sont eux-mêmes contrôlables.
8. **Sélection non suffisante** — la qualité supposée ou observée de l'agent ne dispense jamais de sécuriser les capacités qui lui sont déléguées.

```text
MANDATER
-> BORNER
-> TRACER
-> CONTRÔLER
-> RÉVOQUER
-> REPRENDRE

SELECTION IS NOT SECURITY
NO SELF-ESCALATION
```

## 16. Programme de recherche

1. Rechercher une antériorité formulant explicitement la démocratie représentative comme *security model* transposant least privilege, privilege escalation, revocation et audit.
2. Formaliser la frontière entre exercice, auto-administration et modification du rapport de capacité.
3. Construire un modèle multi-principals compatible avec droits fondamentaux, minorités et générations futures.
4. Tester une procédure de révocation résistante au harcèlement et à la capture minoritaire.
5. Exécuter un premier `Follow the Power` sur une compétence réelle du projet d'autonomie corse.
6. Construire un registre public `Follow the Power` à partir des votes, amendements, actes et compétences.
7. Spécifier les invariants de sécurité d'un Personal Digital Twin chargé d'assister le citoyen.
8. Tester historiquement l'hypothèse de stigmergie institutionnelle.
9. Rechercher des contre-exemples où une extension des pouvoirs représentatifs a effectivement accru les capacités de contrôle du peuple.
10. Tester historiquement et comparativement l'hypothèse selon laquelle le gouvernement représentatif compense une faible opposabilité substantielle du mandat par la sélection électorale et la sanction périodique.

## 17. Bibliographie de travail

### Délégation, représentation, contrôle

- Strøm, Kaare, Wolfgang C. Müller & Torbjörn Bergman (dir.). **Delegation and Accountability in Parliamentary Democracies.** Oxford University Press, 2003.
- Gailmard, Sean. **“Accountability and Principal–Agent Theory.”** In *The Oxford Handbook of Public Accountability*, Oxford University Press, 2014, pp. 90–105.
- Pitkin, Hanna Fenichel. **The Concept of Representation.** University of California Press, 1967.
- Manin, Bernard. **The Principles of Representative Government.** Cambridge University Press, 1997.
- Mansbridge, Jane. **“A ‘Selection Model’ of Political Representation.”** Working Paper RWP08-010, Harvard Kennedy School, 2008 ; version publiée ultérieurement dans *Journal of Political Philosophy*.

### Droit constitutionnel français

- **Constitution du 4 octobre 1958**, notamment articles 2, 3, 27 et 89.
- **Déclaration des droits de l'homme et du citoyen de 1789**, notamment article 6.
- Conseil constitutionnel, jurisprudence relative à la souveraineté nationale, à la représentation et au mandat parlementaire — à approfondir dans une version juridique dédiée.

### Sécurité et gouvernance des agents IA

- NIST / NCCoE. **Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization.** Concept Paper, 5 février 2026.
- OpenAI. **Running Codex safely at OpenAI.** 8 mai 2026.
- Anthropic. **How we contain Claude across products.** 25 mai 2026.
- Google Cloud. Documentation IAM relative aux identités et autorisations des agents, 2026.

## 18. Statut épistémique et éditorial

Le texte a connu une première publication GitHub prématurée avant revue adverse et validation humaine. L'incident est conservé dans l'historique et qualifié, par appréciation humaine, de **« publication prématurée, sans conséquence grave »**.

La v0.3 intégrait :

- la revue adverse indépendante de Grok 4.5 ;
- l'arbitrage des objections N1–N6 ;
- un stress-test de droit public portant notamment sur les articles 3, 27 et 89 de la Constitution ;
- la distinction exercice / auto-administration / modification du rapport de capacité ;
- la correction multi-principals ;
- un instrument minimal `Follow the Power` ;
- l'application réflexive des invariants au Personal Digital Twin.

La v0.4 ajoute, sans retirer ces éléments :

- l'hypothèse de la **sécurité par sélection** comme explication partielle de la forte autonomie représentative ;
- le principe `SELECTION IS NOT SECURITY` ;
- l'explicitation de la faible opposabilité substantielle du mandat parlementaire envers les électeurs ;
- la distinction entre sélection électorale et sécurité continue des capacités ;
- l'extension comparative du tableau agent IA / syndic / représentant ;
- un programme de falsification historique et comparative de cette hypothèse.

La publication initiale a été explicitement autorisée par Jean Hugues le 21 août 2026. La v0.4 constitue une extension conservatrice de la thèse publiée : aucune thèse antérieure n'est supprimée ni inversée.

Le prochain test n'est pas une nouvelle couche doctrinale : **c'est l'exécution d'un premier Follow the Power sur un cas réel.**

## Conclusion

La démocratie représentative peut être étudiée comme un système de sécurité. La question « les représentants sont-ils vertueux ? » devient secondaire devant : **le système reste-t-il sûr lorsqu'ils ne le sont pas ?**

La sélection électorale est une composante légitime de la représentation, mais elle ne constitue pas à elle seule une architecture de sécurité. Un principal réellement souverain doit disposer de capacités effectives pour mandater, observer, contrôler, refuser, révoquer et reprendre la décision, tout en respectant les droits fondamentaux et la pluralité des principals. Ses agents doivent conserver l'autonomie nécessaire à la délibération et à l'action sans pouvoir convertir cette autonomie en propriété autonome du pouvoir.

> **Aucun agent ne devrait pouvoir modifier unilatéralement en sa faveur le rapport de pouvoir qui le lie à son principal.**

> **Selection is not security.**

Si ces propriétés deviennent élémentaires pour la sécurité des machines puissantes, leur application aux institutions représentatives mérite au minimum d'être testée avec la même rigueur.