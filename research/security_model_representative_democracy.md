---
title: "Une théorie de sécurité de la démocratie représentative"
subtitle: "Du principal-agent à la non-auto-élévation des privilèges politiques"
author: "Jean Hugues Noël Robert"
status: "document source — recherche — doctrinal"
version: "0.1"
date: "2026-08-21"
license: "CC BY-SA 4.0"
language: "fr"
repository: "barons-Mariani"
canonical_path: "barons-Mariani/research/security_model_representative_democracy.md"
source_status: "source souveraine du corpus politique et de recherche"
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
---

# Une théorie de sécurité de la démocratie représentative

## Résumé

La démocratie représentative peut être étudiée comme un système de délégation de capacités entre un **principal**, le peuple souverain, et des **agents**, ses représentants. Cette lecture n'est pas nouvelle : la science politique utilise depuis longtemps les modèles principal-agent pour étudier délégation, asymétrie d'information, contrôle et accountability.

L'hypothèse développée ici consiste à franchir une étape supplémentaire : appliquer à la représentation politique les principes de sécurité que l'informatique applique aux agents puissants et que le développement récent des agents d'intelligence artificielle rend désormais particulièrement explicites.

Un système sûr ne suppose pas l'agent vertueux. Il limite ses privilèges, trace ses actes, sépare les pouvoirs, prévoit la révocation et interdit qu'il élargisse lui-même son mandat. Or plusieurs de ces garanties paraissent plus naturelles lorsqu'il s'agit d'un agent logiciel ou d'un syndic de copropriété que lorsqu'il s'agit d'un représentant politique.

La question centrale devient donc :

> **Pourquoi accepter d'un agent politique ce que nous considérerions comme une vulnérabilité de sécurité chez un agent artificiel ou un mandataire ordinaire ?**

La thèse n'est pas que les représentants seraient individuellement malveillants. Elle est au contraire systémique : une architecture de pouvoir doit rester sûre lorsque ses agents se trompent, poursuivent leurs intérêts, subissent des conflits d'intérêts ou cherchent à conserver leurs privilèges. La vertu individuelle ne constitue pas un mécanisme de sécurité.

## 1. Changement de perspective : de la morale à la sécurité

Le débat politique personnalise volontiers les dysfonctionnements : mauvais élus, trahisons, corruption, carriérisme, manque de courage. Ces phénomènes existent, mais leur invocation peut masquer une question plus fondamentale : **que permet l'architecture ?**

En sécurité informatique, on ne construit pas un système en supposant que tous les administrateurs, processus ou agents resteront vertueux. On pose au contraire que l'erreur, la compromission et le conflit d'intérêts sont possibles, puis on limite leur portée.

Le même raisonnement peut être appliqué à la démocratie :

```text
bons individus + architecture vulnérable != système sûr
```

La démocratie représentative doit donc pouvoir rester démocratique même lorsque certains représentants ne le sont pas parfaitement.

## 2. Le modèle minimal

Le modèle comporte deux acteurs conceptuels :

```text
PRINCIPAL : le peuple souverain
AGENT     : le représentant mandaté
```

Le principal délègue certaines capacités à l'agent afin que celui-ci puisse agir efficacement en son nom.

Cette délégation ne devrait pas transférer la propriété de la source du pouvoir.

Invariant :

> **Un mandat autorise l'exercice d'un pouvoir. Il n'autorise pas l'appropriation de sa source.**

La distinction est essentielle entre :

- pouvoir délégué ;
- pouvoir approprié ;
- élévation légitime de privilèges autorisée par le principal ;
- auto-élévation de privilèges décidée par l'agent lui-même.

## 3. Trois mandataires, une seule question

Trois situations rendent le problème immédiatement visible.

| Principal | Agent | Attente de sécurité ordinaire |
|---|---|---|
| utilisateur | agent IA | permissions bornées, traces, arrêt, approbation des actes sensibles |
| copropriétaires | syndic | mandat borné, comptes, assemblée, contrôle, révocation |
| peuple | représentants | élection, publicité institutionnelle, contrôle beaucoup plus indirect |

La question commune est :

> **Le mandataire peut-il augmenter lui-même les pouvoirs que le mandant lui a confiés ?**

Pour un agent IA, une telle capacité est immédiatement identifiée comme un risque d'élévation de privilèges.

Pour un syndic, l'idée qu'il puisse librement redéfinir ses propres pouvoirs contre les copropriétaires serait manifestement anormale.

Pour le représentant politique, en revanche, l'architecture accepte que les représentants participent directement à la définition des pouvoirs de la représentation et des conditions dans lesquelles le peuple peut reprendre directement la décision.

Cette différence demande justification.

## 4. Les invariants de sécurité

### 4.1 Non-auto-élévation des privilèges

> **Aucun agent humain, institutionnel ou artificiel ne peut augmenter les pouvoirs qui lui ont été délégués sans autorisation du principal dont ils procèdent.**

Ce principe ne signifie pas qu'un mandat ne puisse jamais évoluer. Il signifie que l'agent ne doit pas être l'autorité suffisante pour augmenter ses propres privilèges.

### 4.2 Least privilege

L'agent ne reçoit que les capacités nécessaires à sa mission, dans le périmètre nécessaire et pour la durée nécessaire.

Transposition politique : subsidiarité et mandat borné.

### 4.3 Traçabilité des actes

Tout exercice significatif d'un pouvoir délégué doit produire une trace permettant de répondre au minimum à :

```text
Qui a fait quoi ?
Au nom de qui ?
Avec quel mandat ?
Sur quelle base ?
Qui l'a autorisé ?
Quels pouvoirs ont été modifiés ?
Qui a voté pour ou contre ?
Comment l'acte peut-il être contesté ?
```

La publicité brute ne suffit pas. Une masse de documents juridiquement publics mais pratiquement inexploitable ne produit pas nécessairement une capacité de contrôle.

### 4.4 Révocabilité

Un principal qui ne peut retirer une délégation problématique conserve imparfaitement le contrôle de son agent.

La traçabilité sans révocabilité permet de constater l'abus mais pas d'interrompre le mandat qui le permet.

Invariant :

```text
mandater -> tracer -> contrôler -> corriger ou révoquer
```

### 4.5 Refus effectif de l'offre

Le contrôle du principal ne peut être réduit au choix périodique entre les agents que le système lui propose.

Un vote blanc reconnu mais sans capacité d'invalider ou de renouveler l'offre illustre un refus enregistré mais dépourvu d'effet décisionnel.

Un peuple effectivement souverain doit donc pouvoir non seulement choisir, mais aussi **refuser l'offre politique** selon des règles déterminées à l'avance.

### 4.6 Reprise du contrôle

Le principal doit conserver une capacité effective de reprise du contrôle.

Dans une démocratie, cela peut prendre plusieurs formes : décision directe, référendum déclenchable par les citoyens, révocation, nouvelle élection provoquée par un seuil de refus, ou autres mécanismes constitutionnels.

La forme est discutable ; l'invariant l'est moins : une délégation irréversible jusqu'à une échéance décidée par le système réduit la capacité effective du principal.

## 5. Le test du désaccord

Le pouvoir est difficile à observer lorsque principal et agent veulent la même chose.

Le test pertinent est donc :

```text
Peuple = OUI ; représentants = NON
Qui gagne ?

Peuple = NON ; représentants = OUI
Qui gagne ?
```

La souveraineté effective apparaît lorsque les volontés divergent.

Une formulation opérationnelle est :

> **Est souverain celui dont le refus ne peut être renversé par celui qui prétend agir en son nom, dans le domaine légitime de cette souveraineté et sous réserve des droits fondamentaux.**

Cette définition ne remplace pas le droit constitutionnel positif. Elle constitue un test capacitaire.

## 6. Souveraineté formelle et souveraineté effective

La Constitution française affirme que la souveraineté nationale appartient au peuple et qu'aucune section du peuple ni aucun individu ne peut s'en attribuer l'exercice.

Une lecture strictement représentative considère les élus comme représentants de la Nation entière et non comme une simple section exerçant son intérêt particulier.

La théorie de sécurité proposée ici pose une question différente :

> **Quelles garanties empêchent l'exercice par représentation de devenir progressivement maîtrise de l'exercice par les représentants ?**

La titularité formelle ne suffit pas à répondre à cette question. Il faut mesurer les capacités effectives : initiative, veto, contrôle, révocation, accès à l'information, capacité de déclencher la décision directe.

Le problème devient donc celui de l'écart entre :

```text
owner(sovereignty) = people
```

et les capacités réellement disponibles pour exercer cette propriété.

## 7. L'urgence comme test de sécurité

Les crises constituent un cas particulièrement dangereux parce qu'elles justifient facilement l'augmentation temporaire des pouvoirs de l'agent.

Le document `democratie_crise_mandats_express.md` propose les **mandats express** comme stabilisateur : préparer démocratiquement la vitesse avant l'urgence plutôt que laisser l'urgence fabriquer son propre souverain.

La règle de sécurité devient :

```text
urgence accrue
-> mandat plus explicite
-> périmètre plus borné
-> trace plus forte
-> sunset automatique
-> revue obligatoire
```

et non :

```text
urgence accrue
-> discrétion accrue
-> contrôle réduit
```

L'agent qui bénéficie des pouvoirs d'urgence ne doit pas pouvoir, seul, créer, prolonger ou élargir l'état qui justifie ces pouvoirs.

## 8. Capture sans complot : stigmergie institutionnelle

Une architecture capturante ne suppose pas une conspiration.

Chaque génération de représentants hérite de règles, procédures et pouvoirs créés par les générations précédentes. Elle rencontre des dispositifs qui augmentent ou diminuent sa propre capacité d'action.

Une hypothèse simple est qu'une règle avantageuse pour l'appareil rencontre moins d'incitations internes à sa suppression qu'une règle réduisant fortement les pouvoirs de cet appareil n'en rencontre pour son adoption.

On peut appeler **stigmergie institutionnelle** cette accumulation : les traces institutionnelles laissées par les acteurs précédents modifient l'environnement des suivants et orientent leurs décisions sans qu'aucun acteur n'ait besoin de concevoir le résultat global.

```text
optimisations locales répétées
-> sélection institutionnelle
-> concentration émergente de capacité
```

Cette hypothèse doit être testée empiriquement. Elle a cependant une conséquence méthodologique immédiate : changer les personnes ne suffit pas nécessairement à changer le système.

## 9. Pourquoi l'IA change la situation

La représentation politique historique répond en partie à un problème de capacité : aucun citoyen ne peut matériellement lire tous les textes, suivre tous les amendements, contrôler tous les budgets et vérifier tous les actes publics.

L'IA réduit progressivement ce coût cognitif.

Un agent personnel peut, en principe :

- surveiller les actes publics pertinents ;
- relier un vote à un mandat et à ses conséquences ;
- signaler une augmentation de privilèges institutionnels ;
- comparer engagements et actes ;
- résumer les alternatives ;
- conserver les traces ;
- aider le citoyen à exercer ses droits.

Le progrès agentique produit donc un paradoxe historique : au moment même où nous apprenons à empêcher les machines de s'auto-attribuer des privilèges, nous découvrons que nous avons insuffisamment appliqué cette règle aux agents politiques humains.

Formule :

> **Ce que nous apprenons à interdire aux agents IA, nous devrons finir par l'interdire aux agents politiques.**

L'enjeu n'est pas de supprimer la représentation. Il est de transformer le modèle de confiance :

```text
trust me
```

vers :

```text
verify me
```

## 10. Traçabilité des transferts de capacité : Follow the Power

La traçabilité des actes peut être étendue à une comptabilité des capacités politiques.

Pour chaque réforme :

```text
Qui possédait la capacité ?
Qui la transfère ?
À qui ?
Pour combien de temps ?
Sous quelles conditions ?
Qui peut la reprendre ?
Qui a approuvé le transfert ?
```

Cette approche peut être résumée par : **Follow the Power**.

Elle complète `Follow the Money` : il ne s'agit plus seulement de suivre les ressources mais les transformations de capacité.

Une réforme qui augmente les capacités de l'appareil sans augmenter celles des citoyens peut alors être détectée comme une modification du rapport de pouvoir, même si aucun droit formel n'est explicitement retiré.

## 11. Application : autonomie institutionnelle et autonomie des habitants

Le débat sur l'autonomie de la Corse fournit un cas d'étude naturel.

Un transfert de compétences de l'État vers la Collectivité augmente les capacités de cette dernière. Il ne suffit donc pas de demander :

```text
Combien de pouvoir passe de Paris à Ajaccio ?
```

Il faut également demander :

```text
Comment évolue le rapport de capacité
entre les habitants et les institutions
qui exerceront ces nouveaux pouvoirs ?
```

Si les capacités institutionnelles augmentent sans garantie d'augmentation correspondante des capacités des habitants, l'autonomie relative de l'appareil augmente par rapport à eux.

Formule populaire :

> **Plus de pouvoir sur nous n'est pas plus de pouvoir pour nous.**

Cette analyse ne dépend d'aucune hypothèse sur la vertu ou les intentions des élus. Elle porte sur l'architecture du pouvoir.

## 12. État de l'art : briques existantes, synthèse à tester

Plusieurs traditions préexistent à cette proposition :

- théorie principal-agent et délégation politique ;
- accountability démocratique ;
- recall et contrôle continu des représentants ;
- travaux sur democratic backsliding et capture institutionnelle ;
- séparation des pouvoirs et checks and balances ;
- least privilege et privilege escalation en sécurité informatique ;
- identité, autorisation, confinement et audit des agents IA.

L'hypothèse d'originalité ne porte donc pas sur chacune de ces briques.

Elle porte sur leur **traduction systématique dans une théorie commune de sécurité de la représentation**, applicable indifféremment à des agents humains, institutionnels ou artificiels.

Cette revendication d'originalité doit rester falsifiable : une revue bibliographique approfondie devra rechercher des travaux antérieurs ayant déjà proposé explicitement cette unification.

## 13. Spécification minimale d'une démocratie représentative sûre

Une première spécification peut tenir en cinq invariants :

1. **Pouvoir minimal nécessaire** — aucun agent ne reçoit plus de capacité que nécessaire à son mandat.
2. **Non-auto-élévation** — aucun agent ne peut augmenter seul les privilèges reçus du principal.
3. **Traçabilité** — tout exercice significatif du pouvoir délégué laisse une trace exploitable.
4. **Révocabilité** — le principal dispose d'un mécanisme effectif de retrait de la délégation.
5. **Reprise du contrôle** — le principal conserve la capacité de décider directement et de refuser l'offre des agents lorsque les conditions prévues sont réunies.

Sous forme compacte :

```text
MANDATER
-> BORNER
-> TRACER
-> CONTRÔLER
-> RÉVOQUER
-> REPRENDRE
```

avec l'invariant transversal :

```text
NO SELF-ESCALATION
```

## 14. Programme de recherche

Cette théorie demande maintenant à être attaquée plutôt que simplement défendue.

Questions prioritaires :

1. Quels travaux ont déjà formalisé la démocratie représentative comme système de sécurité plutôt que seulement comme relation de délégation ?
2. Où l'analogie entre agent logiciel et représentant politique cesse-t-elle d'être valide ?
3. Comment concilier révocabilité et nécessité pour un représentant de résister parfois à une opinion momentanée ?
4. Comment empêcher qu'un mécanisme de révocation devienne lui-même une arme de capture ou de harcèlement politique ?
5. Quels droits fondamentaux doivent demeurer hors de portée d'une majorité instantanée ?
6. Comment mesurer quantitativement les transferts de capacité politique ?
7. Peut-on construire un registre public `Follow the Power` à partir des votes, amendements, actes et compétences ?
8. Comment un Personal Digital Twin peut-il augmenter la capacité de contrôle sans devenir lui-même un nouveau gardien capturant l'autonomie de son utilisateur ?
9. Quels mécanismes constitutionnels implémentent le mieux la non-auto-élévation des privilèges ?
10. L'hypothèse de stigmergie institutionnelle est-elle observable historiquement et comparativement ?

## Conclusion

La démocratie représentative est habituellement étudiée comme un régime politique, une théorie de la légitimité ou un système de délégation. Elle peut également être étudiée comme un **système de sécurité**.

Cette perspective déplace la question :

```text
Les représentants sont-ils vertueux ?
```

vers :

```text
Le système reste-t-il sûr lorsqu'ils ne le sont pas ?
```

La réponse ne peut reposer uniquement sur des élections périodiques et la confiance.

Un principal réellement souverain doit pouvoir mandater, observer, contrôler, refuser, révoquer et reprendre la décision. Ses agents doivent disposer des capacités nécessaires à leur mission sans pouvoir transformer ces capacités en propriété autonome du pouvoir.

Le principe central est donc :

> **Aucun agent ne doit pouvoir s'attribuer lui-même davantage de pouvoir sur son principal.**

Ce principe vaut pour une intelligence artificielle, pour un syndic, pour une administration et pour un représentant politique.

Si nous savons désormais qu'il constitue une condition élémentaire de sécurité pour les machines puissantes, il devient difficile d'expliquer pourquoi il ne devrait pas constituer également une condition élémentaire de sécurité de la démocratie.
