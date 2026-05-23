---
title: "La seconde méthode comme généralisation prudente de l’agile"
subtitle: "Régimes d’erreur, expérimentation traçable et apprentissage collectif sous complexité"
description: "Working paper sur la généalogie de l’agile, ses conditions de validité, sa diffusion hors du logiciel, et son articulation prudente avec la seconde méthode, l’autonomie de capacité et l’écosystème Barons Mariani"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani — C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
version: "0.5"
date: "2026-05-23"
license: "CC BY-SA 4.0"
repository: "github.com/JeanHuguesRobert/barons-Mariani"
status: "working paper"
related:
  - "./second_method.md"
  - "./autonomie_de_capacite.md"
  - "./kudocracy.md"
  - "../../cogentia/README.md"
  - "../../marenostrum/DHITL.md"
  - "../../FractaVolta/README.md"
changelog:
  - "v0.1 (2026-05-23) — première version complète ; généalogie du passage waterfall/agile ; définition de la seconde méthode comme agile généralisé ; diffusion vers startups, design, DevOps, politiques publiques, territoires et IA ; articulation avec autonomie de capacité, Cogentia, DHITL, Kudocracy et question corse ; objections initiales et clause de continuation."
  - "v0.2 (2026-05-23) — révision critique après évaluation externe : réduction de l’auto-référentialité ; reformulation de la thèse comme généralisation prudente et conditionnelle ; ajout d’une typologie des régimes d’erreur ; distinction plus nette entre agile logiciel et seconde méthode politique ; ajout de cas et familles de cas externes (Lean Startup, design thinking, DevOps/DORA, regulatory sandboxes, innovation publique, gouvernance adaptative) ; déplacement du corpus Barons Mariani en annexe ; renforcement des limites, objections et conditions de validité."
  - "v0.3 (2026-05-23) — préservation assumée de la signature stylistique tout en renforçant la défendabilité académique : ajout d’une note de positionnement sur le statut d’auteur et de corpus ; ajout d’une section sur la méthode de généralisation par conditions de validité ; clarification de la section Corse comme terrain situé et non preuve privilégiée ; ajout d’une matrice d’études de cas externes à documenter ; resserrement des formulations les plus prescriptives sans suppression des images structurantes."
  - "v0.4 (2026-05-23) — intégration de deux cas externes documentés : FCA Regulatory Sandbox et e-Estonia/X-Road ; ajout d’une section critique sur l’agile washing et les limites des transformations agiles à grande échelle ; resserrement de plusieurs formulations normatives ; maintien assumé de la signature stylistique et du branding, désormais justifiés dans la note de positionnement."
  - "v0.5 (2026-05-23) — dernière passe de consolidation avant publication : ajout de données chiffrées dans les cas FCA Regulatory Sandbox et e-Estonia/X-Road ; intégration explicite du cadre Cynefin et de la gouvernance expérimentale Sabel/Zeitlin ; ajout de précautions sur la non-transférabilité directe des cas ; bibliographie externe enrichie ; resserrement final de quelques formulations prescriptives."
---

# La seconde méthode comme généralisation prudente de l’agile

## Régimes d’erreur, expérimentation traçable et apprentissage collectif sous complexité

**Jean Hugues Noël Robert, baron Mariani**  
Institut Mariani — C.O.R.S.I.C.A.  
Corte, Corse

*v0.2 — l’historique git sera la preuve. Le processus qui précède ce commit est documenté et accessible.*  
*Ce document s’améliorera par application de la méthode qu’il décrit.*

---

> *Cogito ergo sum.*  
> *Cogentia ergo scimus.*  
> *Faciendo ergo possumus.*

---

## Abstract

This working paper proposes a cautious generalization of the agile paradigm beyond software engineering. Its central claim is not that all domains should become “agile”, nor that software methods can be directly transferred to public policy, territorial governance or democratic institutions. Rather, the paper argues that the historical success of agile methods in software made visible a broader distinction between two regimes of action: irreversible action, which requires strong ex ante precaution, and reversible action, which can benefit from disciplined, traceable experimentation.

The article first reconstructs the historical shift from waterfall-like planning models to iterative approaches in software development, while noting that the canonical opposition between waterfall and agile is partly simplified. It then examines how similar iterative logics appeared in Lean Startup, design thinking, DevOps, regulatory sandboxes, public-sector innovation and adaptive governance. These examples do not prove a universal method; they identify a family resemblance: small-batch experimentation, feedback loops, reversibility, measurement, documented learning and correction.

The paper introduces the notion of “qualified objection” as a bridge between precaution and experimentation. In irreversible domains, objections may legitimately function as blocking mechanisms. In reversible domains, objections should be converted into testable constraints, indicators or falsification criteria. The proposed “second method” is therefore defined as a cautious framework for organizing collective trial-and-error under complexity: permissive action when experiments are reversible, and accountable record when actions have effects.

The final sections examine the limits of this generalization, especially in democratic and territorial contexts where citizens are not software users and public experimentation can become deregulation if not audited. The paper concludes by relating this framework, as one possible application, to the author’s research on autonomy of capacity in Corsica, understood as the transformation of a territory from a machine that prevents into a system that learns.

---

## Résumé

Cet article propose une généralisation prudente du paradigme agile au-delà du développement logiciel.

Sa thèse centrale n’est pas que tous les domaines devraient devenir « agiles », ni que les méthodes du logiciel pourraient être transférées directement aux politiques publiques, aux territoires ou aux institutions démocratiques. Elle est plus limitée : le succès historique des méthodes agiles dans le logiciel a rendu visible une distinction plus générale entre deux régimes d’action.

D’un côté, les actions irréversibles ou très coûteuses exigent une précaution forte en amont. De l’autre, les actions réversibles, limitées, mesurables et documentables peuvent relever d’une expérimentation disciplinée.

L’article reconstruit d’abord le passage du modèle en cascade aux approches itératives dans le logiciel, tout en soulignant que l’opposition canonique entre waterfall et agile simplifie l’histoire réelle. Il examine ensuite la diffusion de logiques similaires dans le Lean Startup, le design thinking, DevOps, les bacs à sable réglementaires, l’innovation publique et la gouvernance adaptative.

Ces exemples ne prouvent pas l’existence d’une méthode universelle. Ils identifient une ressemblance de famille : essais en petits lots, boucles de retour, réversibilité, mesure, apprentissage documenté et correction.

L’article introduit ensuite la notion d’**objection qualifiée** comme articulation entre précaution et expérimentation. Dans les domaines irréversibles, l’objection peut légitimement bloquer. Dans les domaines réversibles, elle devrait être convertie en contrainte testable, indicateur ou critère de réfutation.

La **seconde méthode** est ainsi définie comme un cadre prudent d’organisation du tâtonnement collectif sous complexité : action plus permissive lorsque l’essai est réversible, registre plus responsable lorsque l’action produit des effets.

Les dernières sections examinent les limites de cette généralisation, en particulier dans les contextes démocratiques et territoriaux, où les citoyens ne sont pas des utilisateurs de logiciel et où l’expérimentation publique peut devenir dérégulation si elle n’est pas auditée. L’article conclut en reliant ce cadre, comme application possible, à l’autonomie de capacité en Corse : transformer un territoire administré comme risque à contenir en territoire capable d’apprendre.

---

## Mots-clés

Seconde méthode ; méthode agile ; waterfall ; cascade ; complexité ; expérimentation ; traçabilité ; objections qualifiées ; gouvernance adaptative ; innovation publique ; bacs à sable réglementaires ; DevOps ; autonomie de capacité ; intelligence artificielle ; Corse.

---

# Note de positionnement

Ce texte assume une tension.

D’un côté, il vise une forme académique : concepts définis, hypothèses limitées, objections intégrées, bibliographie externe, distinction entre argument général et applications particulières.

De l’autre, il appartient à un corpus de recherche situé, porté par un auteur identifié, un territoire, une histoire politique et une pratique publique de publication versionnée. Cette situation n’est pas dissimulée. Elle fait partie de la méthode. Le risque d’auto-référentialité est réel ; il est donc explicitement traité dans la discussion critique et limité par deux choix : placer les références internes en annexe, et confronter le cadre proposé à des traditions externes — agile, DevOps, Lean Startup, design thinking, gouvernance adaptative, bacs à sable réglementaires, théorie des communs et politiques publiques expérimentales.

Le nom d’auteur, l’affiliation et le corpus ne doivent donc pas être lus comme une prétention d’autorité. Ils indiquent un lieu de production, un historique vérifiable et une responsabilité assumée. Le choix de conserver cette signature, plutôt que de l’effacer pour mimer une neutralité académique impersonnelle, relève aussi de la méthode : l’auteur, le lieu, les engagements et les conditions de production doivent rester visibles. La neutralité recherchée ici n’est pas l’absence de situation ; c’est la capacité à rendre cette situation explicite, critiquable et non contraignante pour le lecteur.

Le présent article ne demande pas au lecteur d’adhérer au corpus Barons Mariani pour comprendre l’argument. Il lui propose une hypothèse générale, puis montre comment cette hypothèse peut être appliquée à un corpus et à un territoire.

---

# 1. Introduction : agir sous incertitude

Toute méthode d’action repose implicitement sur une théorie de l’erreur.

Dans certains domaines, l’erreur doit être empêchée avant l’action, parce que ses conséquences peuvent être irréversibles. Un pont mal conçu peut s’effondrer. Une erreur chirurgicale peut tuer. Une décision judiciaire injuste peut briser une vie. Une infrastructure critique mal sécurisée peut provoquer une cascade d’effets systémiques.

Dans d’autres domaines, l’erreur peut être limitée, observée, documentée, corrigée. Une interface logicielle peut être modifiée. Un prototype peut être abandonné. Un dispositif local peut être testé à petite échelle. Une hypothèse de recherche peut être réfutée sans détruire le champ qui l’accueille.

Le premier régime appelle la prudence classique : bloquer les erreurs le plus tôt possible.

Le second régime appelle une autre prudence : ne pas bloquer inutilement les essais réversibles, mais les rendre traçables, attribuables et corrigibles.

La distinction peut être formulée ainsi :

> **Lorsque l’erreur est irréversible, il faut filtrer avant l’action.**  
> **Lorsque l’essai est réversible, il faut apprendre par l’action.**

Le développement logiciel a été le domaine où cette seconde logique s’est imposée le plus nettement. Au tournant du XXIe siècle, les méthodes dites agiles ont contesté les approches lourdes de planification préalable, au profit de cycles courts, de retours fréquents, de livraisons incrémentales et de corrections continues.

Le présent article ne soutient pas que l’agile logiciel serait directement applicable à toute la société. Une telle affirmation serait excessive. Il propose plutôt de comprendre l’agile comme un cas particulièrement net d’une mutation plus générale, observable par conditions de validité : lorsque l’action est réversible, documentable, limitée et attribuable, l’exploration disciplinée peut devenir plus rationnelle que le contrôle prédictif intégral.

Cette mutation reste incomplète. Elle est parfois capturée par le management, parfois réduite à un vocabulaire, parfois mal transposée. Mais elle pose une question centrale pour les sociétés complexes :

> Comment organiser collectivement le tâtonnement sans sombrer dans l’arbitraire ?

C’est cette question que cet article propose d’examiner sous le nom de **seconde méthode**.

---

# 2. Deux régimes d’erreur

## 2.1. Erreur irréversible : la prudence classique

La méthode classique est rationnelle dans les contextes où l’erreur est coûteuse, dangereuse ou difficilement réversible.

Dans ces contextes, l’objection doit pouvoir bloquer. Elle est un instrument de sécurité. Elle protège contre des décisions dont les effets ne pourraient pas être facilement annulés.

Les exemples sont nombreux :

- ponts, tunnels, barrages ;
- avions, trains, centrales électriques ;
- chirurgie et actes médicaux à risque ;
- justice pénale ;
- décisions militaires ;
- infrastructures numériques critiques ;
- politiques publiques affectant massivement des populations vulnérables.

Dans ces domaines, une logique de type « essayons puis corrigeons » serait irresponsable si l’essai lui-même produit des dommages irréparables.

La méthode classique n’est donc pas dépassée. Elle reste indispensable. L’erreur consiste à l’appliquer comme méthode universelle.

## 2.2. Erreur réversible : l’expérimentation traçable

À l’inverse, lorsque l’essai est limité, réversible et mesurable, le blocage préalable peut devenir plus coûteux que l’erreur elle-même.

Une idée mauvaise testée proprement produit une information : elle permet de savoir pourquoi elle échoue, dans quelles conditions, avec quels effets et quelles objections pertinentes.

Une idée bloquée sans essai ne produit rien. Elle reste dans le domaine de l’opinion, de l’intuition ou du rapport de force.

L’expérimentation traçable repose donc sur une autre théorie de la prudence :

- limiter la taille de l’essai ;
- rendre les hypothèses explicites ;
- définir des indicateurs ;
- conserver les objections ;
- attribuer les décisions ;
- documenter les résultats ;
- corriger ou abandonner rapidement.

Il ne s’agit pas d’opposer prudence et expérimentation. Il s’agit de distinguer deux formes de prudence : prudence de l’interdiction lorsque l’irréversible domine ; prudence de l’apprentissage lorsque le réversible domine.

## 2.3. Cynefin : situer l’action avant de choisir la méthode

La distinction proposée rejoint partiellement le cadre **Cynefin** de David J. Snowden et Mary E. Boone. Ce cadre ne classe pas les organisations, mais les situations de décision selon la nature plus ou moins lisible des relations de cause à effet.

Dans les situations simples ou claires, les bonnes pratiques peuvent être appliquées directement. Dans les situations compliquées, l’expertise permet d’analyser et de choisir entre plusieurs bonnes réponses possibles. Dans les situations complexes, les relations de cause à effet ne sont vraiment lisibles qu’après coup : il faut alors sonder, observer, répondre. Dans les situations chaotiques, l’urgence impose d’agir d’abord pour rétablir un minimum d’ordre.

Cette distinction est importante pour éviter un contresens. La seconde méthode ne soutient pas que toute situation complexe doit devenir « agile » au sens professionnel du terme. Elle soutient plutôt que, dans les situations où la causalité n’est pas entièrement connaissable à l’avance, la méthode doit inclure des boucles d’essai, d’observation et de correction.

Cynefin apporte donc un garde-fou : avant de choisir la méthode, il faut qualifier le type de situation. Une méthode efficace dans le compliqué peut échouer dans le complexe ; une méthode acceptable dans le réversible peut devenir irresponsable dans l’irréversible.

## 2.4. Typologie indicative des régimes d’action

La typologie suivante n’a pas vocation à être définitive. Elle sert à éviter deux erreurs symétriques : généraliser l’agile partout, ou maintenir la méthode classique partout.

| Régime d’action | Coût de l’erreur | Réversibilité | Exemple | Méthode adaptée |
|---|---:|---:|---|---|
| Infrastructure critique | Très élevé | Faible | Pont, barrage, centrale | Méthode classique, certification forte |
| Acte vital ou judiciaire | Très élevé | Faible à moyenne | Chirurgie, condamnation pénale | Précaution maximale, recours |
| Logiciel web ou service numérique | Faible à moyen | Élevée | Application, interface, API | Agile, DevOps, tests continus |
| Innovation entrepreneuriale | Moyen | Moyenne à élevée | Produit minimum viable | Lean Startup, métriques |
| Politique publique locale | Moyen à élevé | Variable | Logement, mobilité, énergie communale | Expérimentation auditée |
| Régulation technologique | Variable | Variable | Fintech, IA, santé numérique | Bac à sable réglementaire encadré |
| Démocratie et loi | Élevé | Faible à moyenne | Vote, mandat, règle collective | Expérimentation démocratique très encadrée |
| IA décisionnelle | Potentiellement élevé | Variable | Recommandation, scoring, aide à la décision | Auditabilité, traçabilité, supervision humaine |

Cette typologie indique que la seconde méthode n’est pas un remplacement global de la méthode classique. Elle est une méthode de discrimination entre régimes d’action.

---

# 3. Le cas historique du logiciel

## 3.1. Royce et le malentendu waterfall

Le modèle dit **waterfall**, ou modèle en cascade, est souvent associé à Winston W. Royce et à son article de 1970, *Managing the Development of Large Software Systems*. Dans la mémoire professionnelle, ce modèle est devenu l’image d’une séquence linéaire : exigences, spécifications, conception, développement, test, déploiement, maintenance.

Il faut pourtant rappeler que Royce ne défendait pas naïvement une cascade sans retour. Son article soulignait déjà les risques d’une progression purement linéaire et proposait des boucles de rétroaction, des prototypes et une documentation robuste.

L’opposition simplifiée « waterfall contre agile » ne rend donc pas entièrement justice à l’histoire. Mais elle correspond à une réalité institutionnelle : de nombreuses organisations ont effectivement adopté des processus lourds, séquentiels, contractuels, dans lesquels la correction tardive devenait coûteuse.

La critique agile s’est construite contre cette réalité organisationnelle plus que contre Royce lui-même.

## 3.2. Le Manifeste Agile

Le *Manifesto for Agile Software Development*, publié en 2001, formule quatre préférences célèbres :

- les individus et leurs interactions plutôt que les processus et les outils ;
- un logiciel opérationnel plutôt qu’une documentation exhaustive ;
- la collaboration avec le client plutôt que la négociation contractuelle ;
- l’adaptation au changement plutôt que le suivi d’un plan.

Le texte précise que les seconds termes gardent de la valeur, mais que les premiers sont privilégiés.

Ce point est important : l’agile n’est pas une suppression de la documentation, du contrat, des outils ou du plan. C’est un déplacement de priorité. Lorsque le réel contredit le plan, le plan doit être révisable.

Les principes associés insistent sur la livraison fréquente, l’accueil du changement, les cycles courts, la coopération quotidienne, l’attention à l’excellence technique et les rétrospectives régulières.

## 3.3. Scrum, XP, DevOps

Scrum formalise l’agile autour de l’empirisme : transparence, inspection, adaptation. Ces trois termes expriment une épistémologie pratique : on ne sait pas tout d’avance, donc il faut rendre visible, inspecter régulièrement et adapter.

Extreme Programming insiste, de son côté, sur les pratiques techniques : tests, intégration continue, refactoring, programmation en binôme, petites livraisons.

DevOps prolonge le mouvement en réduisant la distance entre développement et exploitation. Le logiciel n’est plus seulement livré ; il est observé en production, corrigé, sécurisé, déployé en continu.

Les métriques DORA — fréquence de déploiement, délai de changement, taux d’échec des changements, délai de restauration du service — ont contribué à mesurer cette capacité organisationnelle. Leur intérêt est de déplacer l’attention de la conformité documentaire vers la capacité effective de livrer, corriger et restaurer.

## 3.4. Ce que l’agile a réellement démontré

L’agile n’a pas démontré que la planification était inutile.

Il n’a pas démontré que tous les domaines devaient imiter le logiciel.

Il n’a pas démontré que l’auto-organisation suffisait à résoudre les conflits de pouvoir.

Il a démontré quelque chose de plus limité mais plus robuste :

> Dans un domaine où les exigences changent, où les erreurs sont relativement réversibles et où le retour d’usage est disponible, des cycles courts, des essais incrémentaux et une correction continue peuvent être supérieurs à une planification exhaustive préalable.

C’est cette démonstration limitée qui peut être généralisée avec prudence.

---

# 4. Diffusion hors logiciel : ressemblances de famille

## 4.0. Méthode de généralisation

La généralisation proposée ici ne repose pas sur une analogie globale du type « la société serait un logiciel ». Cette analogie serait fausse.

Elle repose sur une comparaison plus limitée : certains domaines, bien que très différents, rencontrent une même difficulté — agir lorsque le problème n’est pas entièrement connu à l’avance — et mobilisent alors des dispositifs comparables :

- essais limités ;
- hypothèses explicites ;
- boucles de retour ;
- mesure des effets ;
- correction rapide ;
- documentation du processus ;
- abandon ou généralisation selon les résultats.

Ce sont ces traits communs, et non une identité de nature entre les domaines, qui justifient l’usage de l’expression **ressemblance de famille**.

La question méthodologique devient donc :

> À quelles conditions une pratique itérative observée dans un domaine peut-elle être transposée, prudemment, dans un autre ?

Les sections suivantes répondent par comparaison, non par assimilation.



Les sections suivantes ne prétendent pas que Lean Startup, design thinking, DevOps, innovation publique et regulatory sandboxes seraient identiques. Elles indiquent une **ressemblance de famille** : dans chaque cas, l’action se structure autour d’hypothèses, de tests, de retours, de corrections et de documentation.

## 4.1. Lean Startup

La méthode Lean Startup transpose la logique itérative à l’entrepreneuriat. Son cœur est la boucle **build-measure-learn** : construire un produit minimum viable, mesurer les réactions, apprendre, puis décider de persévérer ou de pivoter.

Le business plan classique correspond à une cascade entrepreneuriale : décrire le marché, prévoir, financer, exécuter.

Le Lean Startup transforme l’entreprise naissante en système de recherche. Le modèle économique n’est plus présupposé ; il est découvert, testé, validé ou abandonné.

Cette méthode a évidemment ses limites. Un produit minimum viable peut être trop pauvre, une métrique peut être mal choisie, un pivot peut être opportuniste, et l’attention au marché peut réduire l’ambition de long terme. Mais l’apport reste net : l’incertitude n’est pas niée ; elle est organisée.

## 4.2. Design thinking

Le design thinking diffuse une logique proche dans les services, produits et organisations. Il articule généralement empathie, définition du problème, idéation, prototypage et test.

Son intérêt est d’introduire une dimension située : les usages réels, les corps, les environnements, les pratiques, les contraintes sociales. Le problème n’est pas seulement résolu dans l’abstraction ; il est éprouvé par des prototypes.

Sa limite est également connue : réduit à des ateliers superficiels, il devient une scénographie de participation sans pouvoir réel. Comme l’agile, il peut devenir rituel.

## 4.3. DevOps et observabilité

DevOps est souvent compris comme une extension de l’agile, mais il ajoute une dimension importante : l’observation en production.

L’action ne s’arrête pas à la livraison. Elle continue dans l’exploitation, la surveillance, l’alerte, la restauration, l’amélioration continue.

Ce point est important pour toute généralisation politique : une expérimentation n’est pas terminée quand elle est annoncée ou votée. Elle commence réellement lorsqu’elle produit des effets observables.

## 4.4. Bacs à sable réglementaires

Les **regulatory sandboxes**, d’abord développés notamment dans la finance et les technologies réglementées, permettent de tester des innovations dans un cadre limité, sous supervision, avec des exemptions ou adaptations temporaires.

Leur logique est directement liée à la distinction des régimes d’erreur :

- ne pas autoriser sans contrôle une innovation potentiellement risquée ;
- ne pas interdire par principe une innovation dont les effets peuvent être observés dans un périmètre limité ;
- apprendre avec le régulateur, les opérateurs et les usagers.

Le bac à sable réglementaire n’est pas l’absence de règle. C’est une règle de l’expérimentation.

## 4.5. Cas externe 1 — FCA Regulatory Sandbox : expérimenter sous supervision

Le cas du **Financial Conduct Authority Regulatory Sandbox** britannique est utile parce qu’il matérialise presque littéralement la distinction proposée dans cet article. Il ne s’agit pas d’autoriser l’innovation financière sans règle ; il s’agit de créer un espace limité où des produits, services ou modèles d’affaires innovants peuvent être testés dans un environnement de marché réel, avec de vrais consommateurs, sous supervision et avec des garde-fous.

La FCA a lancé son sandbox en 2016, dans le prolongement de Project Innovate. Son rapport de retour d’expérience publié en 2017 présente le dispositif comme un moyen de tester des innovations en environnement réel tout en maintenant des protections appropriées pour les consommateurs. Sur les deux premières cohortes, la FCA indique avoir reçu **146 candidatures**, accepté **50 firmes**, et accompagné **41 tests réalisés ou alors en cours**. Le rapport précise également qu’environ un tiers des firmes de la première cohorte ont utilisé les apprentissages du sandbox pour faire pivoter significativement leur modèle avant un lancement plus large. Le sandbox vise donc à réduire le temps et le coût d’accès au marché, à faciliter l’accès au financement et à permettre au régulateur d’apprendre des innovations qu’il encadre.

Ce cas illustre trois points importants pour la seconde méthode.

Premièrement, l’expérimentation n’est pas opposée à la régulation. Elle devient une modalité de la régulation lorsque l’incertitude technique et économique rend inefficace l’interdiction abstraite comme l’autorisation générale.

Deuxièmement, l’essai est borné. Les firmes ne sont pas simplement libérées de la règle ; elles sont placées dans un périmètre d’observation. Cette limitation correspond au principe de réversibilité relative.

Troisièmement, le régulateur apprend. Le bac à sable n’est pas seulement un service rendu aux entreprises ; il devient un instrument de connaissance publique sur des technologies ou modèles économiques encore mal compris.

Mais le cas contient aussi ses propres objections. Le sandbox peut favoriser les acteurs déjà capables de dialoguer avec le régulateur ; il peut réduire l’incertitude pour les investisseurs sans produire de bénéfice social clair ; il peut devenir une voie d’accès privilégiée pour certains opérateurs. Il confirme donc la thèse prudente de cet article : l’expérimentation n’est acceptable que si ses bénéficiaires, ses risques, ses critères d’arrêt et ses effets d’apprentissage sont explicitement documentés.

## 4.6. Cas externe 2 — e-Estonia et X-Road : infrastructure publique d’itération

Le cas estonien ne relève pas de l’agile logiciel au sens strict. Il constitue plutôt un exemple d’infrastructure publique conçue pour permettre l’évolution continue des services numériques de l’État.

Le système **X-Road**, présenté par e-Estonia comme l’épine dorsale de l’État numérique estonien, est une solution open source d’échange sécurisé de données entre organisations publiques et privées. Sa fonction n’est pas de centraliser toutes les données dans une base unique, mais de permettre l’interopérabilité de systèmes distincts. Les présentations publiques du modèle estonien évoquent un ordre de grandeur de **plus de deux milliards d’échanges annuels** et plusieurs milliers de services numériques appuyés sur cette architecture, chiffres à lire comme indicateurs de capacité d’usage plutôt que comme preuve suffisante de qualité démocratique. Cette architecture réduit une partie de la rigidité institutionnelle : chaque organisation conserve ses systèmes, mais les services peuvent se recomposer par échanges sécurisés.

L’identité numérique estonienne ajoute une autre couche de capacité : identification, signature numérique, accès aux services publics, prescriptions électroniques, vote électronique, consultation de dossiers. La transformation n’est donc pas seulement technique. Elle repose sur une combinaison de droit, d’infrastructure, de confiance, d’usage et de traçabilité.

Ce cas illustre une forme plus institutionnelle de seconde méthode. L’État ne se contente pas de numériser des procédures existantes ; il construit une infrastructure qui rend possible l’amélioration continue des services publics. L’itération ne porte plus seulement sur une application, mais sur l’architecture administrative elle-même.

Il faut toutefois éviter l’idéalisation. La réussite estonienne dépend d’un contexte particulier : petite taille du pays, reconstruction institutionnelle après l’indépendance, forte volonté politique, investissement dans l’identité numérique, niveau élevé de confiance relative, exposition géopolitique qui rend la résilience numérique stratégique. Elle ne fournit donc pas un modèle directement transférable. Elle fournit un cas où la capacité publique a été renforcée par une architecture modulaire, interopérable et traçable. Elle montre aussi que la réversibilité technique ne suffit pas : une infrastructure numérique d’État peut accroître la capacité publique, mais aussi concentrer de nouveaux risques si la cybersécurité, la souveraineté logicielle, le contrôle démocratique et les droits des personnes ne suivent pas.

## 4.7. Innovation publique et gouvernance adaptative

Les administrations expérimentent de plus en plus des laboratoires d’innovation publique, des prototypes de services, des consultations itératives, des tests utilisateurs, des démarches de design public et des politiques fondées sur la preuve.

La gouvernance adaptative, notamment dans les systèmes socio-écologiques, insiste également sur l’apprentissage, la révision des règles, la pluralité d’acteurs et l’ajustement progressif face à l’incertitude.

Ces démarches signalent une transformation importante : dans des environnements complexes, gouverner ne consiste plus seulement à appliquer un plan. Cela consiste aussi à mettre en place des boucles d’apprentissage fiables.

Cette intuition rejoint la littérature sur l’**experimentalist governance**, notamment chez Charles F. Sabel et Jonathan Zeitlin. Leur approche met l’accent sur des objectifs-cadres fixés collectivement, une mise en œuvre décentralisée, une comparaison régulière des résultats, puis une révision périodique des règles à partir des apprentissages observés. Elle constitue l’un des ancrages théoriques les plus proches de ce que le présent article appelle seconde méthode, avec une différence de vocabulaire : là où l’expérimentalisme institutionnel décrit des architectures de gouvernance, la seconde méthode insiste davantage sur la traçabilité du corpus, la qualification des objections et l’attribution humaine des actes.

---

# 5. Les limites de la généralisation

## 5.1. Tout n’est pas logiciel

La première limite est évidente mais décisive : tout n’est pas logiciel.

Le logiciel offre une réversibilité que beaucoup de domaines matériels, sociaux ou juridiques ne possèdent pas. Une version peut être corrigée, un service peut être restauré, un test A/B peut être arrêté. Dans la société, les effets sont plus diffus, plus lents, plus inégaux, parfois moins réversibles.

La généralisation de l’agile doit donc être conditionnelle.

Il ne faut pas demander : « peut-on rendre ce domaine agile ? »

Il faut demander :

> Qu’est-ce qui, dans ce domaine, est suffisamment réversible, limité, observable et attribuable pour relever d’une expérimentation traçable ?

## 5.2. Les citoyens ne sont pas des utilisateurs

Un utilisateur peut quitter un service numérique.

Un citoyen ne peut pas aussi facilement quitter son école, son hôpital, son administration, son territoire, son droit.

La transposition politique de l’agile exige donc des protections supplémentaires :

- droits des personnes concernées ;
- consentement ou représentation légitime ;
- transparence ;
- recours ;
- évaluation indépendante ;
- limitation temporelle ;
- possibilité d’abandon ;
- réparation en cas de dommage.

Une politique publique ne doit pas traiter les citoyens comme un segment de marché.

## 5.3. L’expérimentation peut devenir dérégulation

L’expérimentation peut être capturée par des intérêts puissants. Elle peut devenir un prétexte pour contourner les protections sociales, environnementales ou démocratiques. Elle peut installer une exception temporaire qui devient permanente.

C’est pourquoi l’expérimentation publique doit être auditée.

La question n’est pas seulement : « avons-nous le droit d’essayer ? »

Elle est aussi :

> Qui bénéficie de l’essai ?  
> Qui supporte le risque ?  
> Qui garde la trace ?  
> Qui peut contester ?  
> Qui peut arrêter ?  
> Qui apprend ?  
> Qui capture la valeur ?

## 5.4. L’agile peut devenir rhétorique managériale

L’agile est souvent devenu un vocabulaire sans réalité : cérémonies sans autonomie, post-it sans pouvoir, sprints sans apprentissage, management vertical déguisé en collaboration.

Cette capture ne réfute pas l’agile. Elle montre qu’une méthode peut devenir folklore lorsqu’elle est séparée de ses conditions de validité.

Une organisation n’est pas agile parce qu’elle utilise le vocabulaire agile. Elle l’est si elle réduit effectivement le coût de correction, augmente la qualité de l’apprentissage, rend les problèmes visibles et donne aux équipes la capacité réelle de modifier le cours de l’action.

## 5.5. Agile washing et transformations à grande échelle

La littérature sur les transformations agiles à grande échelle confirme ce point. Les difficultés ne tiennent pas seulement aux outils, mais à la compréhension partagée du problème, aux structures hiérarchiques, aux dépendances entre équipes, aux systèmes existants, aux modes de financement, aux métriques et aux incitations.

L’**agile washing** peut être défini comme l’usage du vocabulaire agile sans transfert réel de capacité d’action. Les signes sont assez constants :

- équipes dites autonomes mais dépendantes de décisions hiérarchiques lentes ;
- sprints utilisés pour accélérer la pression plutôt que l’apprentissage ;
- rituels agiles sans capacité de modifier le produit, le budget ou la priorité ;
- obsession de la vélocité au détriment de la valeur ;
- expérimentation proclamée mais absence de droit à l’échec documenté ;
- reporting agile remplaçant l’ancien reporting sans changer la logique de contrôle.

Ce phénomène est important pour la seconde méthode, car il montre que l’itération peut être capturée par le management comme n’importe quelle autre méthode. Une institution peut simuler l’exploration tout en conservant une structure de blocage.

Le critère de distinction devient donc empirique :

> Une méthode est réellement agile, ou relève réellement de la seconde méthode, si elle augmente la capacité effective de corriger le cours de l’action à partir d’un retour documenté.

Sans cette capacité de correction, l’agile n’est qu’une cascade repeinte.

---

# 6. Définition prudente de la seconde méthode

À partir de cette généalogie et de ces limites, on peut proposer une définition prudente :

> **La seconde méthode est un cadre d’exploration rationnelle des possibles par essais réversibles, objections qualifiées, traçabilité des actes, attribution humaine et amélioration continue du corpus.**

Cette définition ne prétend pas nommer une méthode entièrement nouvelle. Elle propose de rassembler, sous une grammaire commune, plusieurs pratiques déjà observables dans des domaines distincts.

## 6.1. Réversibilité

Une expérimentation doit être conçue pour limiter les dommages et permettre la correction.

La réversibilité peut être technique, juridique, financière, sociale ou symbolique. Elle doit être évaluée explicitement.

## 6.2. Traçabilité

L’essai doit produire une mémoire exploitable : hypothèse initiale, acteurs, conditions, objections, indicateurs, résultats, corrections, abandon éventuel.

Sans trace, il n’y a pas d’apprentissage collectif.

## 6.3. Attribution

Les décisions engageantes doivent rester attribuables à des acteurs humains identifiables.

L’attribution n’est pas la culpabilisation. Elle est la condition minimale de la responsabilité.

## 6.4. Objections qualifiées

Une objection utile ne se limite pas à un refus ou à un sentiment d’invraisemblance.

Elle doit pouvoir être formulée comme :

- hypothèse contestée ;
- risque identifié ;
- donnée manquante ;
- indicateur à suivre ;
- seuil d’arrêt ;
- modification proposée ;
- critère de réfutation.

L’objection devient alors une contribution de premier rang.

## 6.5. Corpus public

L’ensemble du processus doit être conservé dans un corpus accessible, versionné, améliorable.

Le corpus n’est pas seulement l’archive finale. Il est l’infrastructure cognitive de l’apprentissage collectif.

---

# 7. Intelligence artificielle : accélérateur et risque

L’arrivée de l’intelligence artificielle rend la question plus urgente.

D’un côté, l’IA augmente la capacité d’exploration. Elle peut lire des corpus, comparer des arguments, identifier des contradictions, générer des hypothèses, produire des synthèses, simuler des variantes, aider à formuler des objections.

De l’autre, elle augmente les risques d’opacité. Elle peut produire des textes plausibles sans sources claires, recommander sans justification, automatiser des refus, accélérer une bureaucratie incompréhensible, diluer la responsabilité humaine.

L’IA ne rend donc pas la seconde méthode facultative. Elle la rend plus nécessaire.

La règle pourrait être formulée ainsi :

> **Plus l’inférence est puissante, plus la trace doit être exigeante.**

Une société assistée par IA doit savoir :

- quelles données ont été mobilisées ;
- quelle inférence a été produite ;
- quelle recommandation a été formulée ;
- quelle décision humaine a été prise ;
- qui en répond ;
- comment contester ;
- comment corriger.

Sans cela, l’IA ne produit pas une machine à explorer. Elle produit une machine à empêcher augmentée.

---

# 8. Application territoriale située : autonomie de capacité

Les sections précédentes ont volontairement tenu la discussion à distance du cas corse. Il est maintenant possible de l’introduire comme **application située**, non comme preuve privilégiée. Le cas corse n’est pas convoqué parce qu’il serait universel ; il l’est parce qu’il concentre, à une échelle lisible, plusieurs tensions que l’on retrouve ailleurs : insularité, dépendance énergétique, pression foncière, transmission linguistique, fragilité agricole, crise démocratique, dépendance administrative, potentiel d’innovation territoriale.

L’autonomie de capacité désigne la faculté d’un territoire à convertir son capital territorial — ressources naturelles, infrastructures, savoir-faire, mémoire, institutions, données, réseaux sociaux — en capabilités collectives effectives.

Elle distingue deux questions :

> Que le territoire a-t-il le droit de faire ?  
> Que le territoire est-il réellement capable de faire ?

La première relève de l’autonomie institutionnelle.

La seconde relève de l’autonomie de capacité.

Cette distinction importe particulièrement en Corse, où plusieurs décennies d’évolutions statutaires n’ont pas suffi, à elles seules, à résoudre les problèmes de fond : logement, langue, foncier, dépendance énergétique, fragilité agricole, départ des jeunes, difficulté à transformer les ressources locales en capacités locales. Ce constat ne disqualifie pas l’autonomie institutionnelle ; il indique seulement qu’un statut ne produit pas automatiquement une capacité.

La seconde méthode offre ici une grammaire pratique :

- formuler des hypothèses territoriales ;
- tester à petite échelle ;
- documenter les coûts ;
- mesurer les effets ;
- intégrer les objections ;
- corriger ;
- transmettre ;
- généraliser seulement ce qui fonctionne.

Une politique d’autonomie de capacité ne peut donc pas se limiter à revendiquer des compétences. Elle gagne en solidité lorsqu’elle produit aussi des protocoles d’expérimentation.

Exemples possibles :

- micro-nœuds énergétiques communaux ;
- restauration de sources et systèmes hydrauliques anciens ;
- logement réversible pour étudiants, jeunes actifs et saisonniers ;
- circuits courts alimentaires documentés ;
- dispositifs de démocratie locale traçable ;
- corpus publics versionnés ;
- usages civiques de l’IA sous contrôle humain ;
- mécanismes anti-capture sur les ressources territoriales.

Le but n’est pas de transformer la Corse en laboratoire extérieur.

Il est de permettre aux habitants d’expérimenter sur leurs propres conditions d’existence, avec méthode, mémoire et responsabilité.

---

# 9. Machine à empêcher, machine à explorer : métaphore opératoire

La distinction entre méthode classique et seconde méthode peut être formulée politiquement par deux images. Ces images ne remplacent pas l’analyse ; elles la rendent manipulable dans le débat public.

La première est la **machine à empêcher**.

Elle désigne un système qui filtre à l’entrée, multiplie les autorisations, disperse les responsabilités, transforme la prudence en immobilisme, et rend l’inaction moins risquée que l’essai.

Cette machine n’a pas toujours de visage. Elle fonctionne par délais, procédures, avis, compétences mal distribuées, financements conditionnés, peur juridique, absence de responsable global.

La seconde image est la **machine à explorer**.

Elle ne désigne pas l’absence de règles. Elle désigne un système organisé pour apprendre :

- essais limités ;
- hypothèses explicites ;
- objections qualifiées ;
- traces publiques ;
- responsabilité humaine ;
- corrections rapides ;
- mémoire transmissible.

Le passage de la machine à empêcher à la machine à explorer ne signifie pas supprimer les protections. Il signifie mieux distinguer les domaines où il faut empêcher de ceux où il faut permettre d’apprendre.

C’est cette distinction — empêcher lorsque l’irréversible domine, explorer lorsque le réversible peut être tracé — qui pourrait devenir centrale pour l’action publique au XXIe siècle.

---

# 10. Matrice d’études de cas à documenter

Le présent article reste conceptuel. Pour devenir un article empirique plus robuste, il devra être prolongé par des études de cas détaillées. La matrice suivante indique les familles de cas à documenter, les questions à poser et les risques à examiner.

| Famille de cas | Exemple possible | Question empirique | Risque critique |
|---|---|---|---|
| Agile logiciel | Scrum, XP, DevOps, DORA | Les cycles courts améliorent-ils réellement la livraison et la correction ? | Rituel agile sans autonomie |
| Startup | Lean Startup, MVP, pivot | Les hypothèses de marché sont-elles effectivement testées ? | Métriques superficielles ou opportunisme |
| Design public | Policy labs, design de services | Les usagers modifient-ils réellement la solution ? | Participation scénarisée |
| Régulation | FCA Regulatory Sandbox | L’expérimentation améliore-t-elle la règle ? | Dérégulation capturée |
| Gouvernance adaptative | Eau, forêt, climat, biodiversité | Les règles changent-elles selon les retours du terrain ? | Capture par experts ou opérateurs |
| Territoire | Corse, îles, régions périphériques | Les ressources deviennent-elles des capacités locales ? | Capture de valeur ou folklore territorial |
| État numérique | e-Estonia / X-Road | L’interopérabilité augmente-t-elle la capacité publique ? | Surveillance, dépendance, vulnérabilité systémique |
| IA publique | Aide à la décision, agents civiques | La trace entre donnée, inférence et décision reste-t-elle lisible ? | Opacité et dilution de responsabilité |
| Démocratie | Consultation, démocratie liquide, mandat | Les objections sont-elles qualifiées et intégrées ? | Manipulation ou délégation excessive |

Cette matrice n’est pas une preuve. Elle fournit un programme de recherche. Elle permet de transformer la seconde méthode en hypothèse testable : si la méthode prétend organiser le tâtonnement, elle doit elle-même accepter d’être évaluée par des cas.

---

# 11. Discussion critique

## 11.1. Une hypothèse de généralisation, non une preuve

La seconde méthode ne doit pas être présentée comme une vérité déjà démontrée.

Elle est une hypothèse de généralisation.

Elle part d’un constat : plusieurs domaines distincts ont adopté des pratiques itératives face à la complexité.

Elle propose une grille : distinguer les régimes d’erreur, qualifier les objections, tracer les essais, attribuer les actes.

Elle doit elle-même être testée, critiquée, corrigée.

## 11.2. Le risque de grand récit

Il existe un risque évident : transformer une évolution réelle du logiciel en grand récit totalisant.

Ce risque doit être explicitement reconnu.

Tous les domaines ne suivent pas le même rythme. Toutes les pratiques itératives ne relèvent pas d’une même cause. Toutes les expérimentations ne sont pas émancipatrices. Toutes les institutions ne peuvent pas devenir agiles.

La seconde méthode ne doit donc pas être pensée comme une théorie totale, mais comme une grammaire conditionnelle.

## 11.3. Le risque d’auto-référentialité

Un autre risque est l’auto-référentialité : construire un corpus conceptuel qui se cite lui-même et finit par fonctionner comme un univers fermé.

Pour éviter ce risque, deux exigences sont nécessaires :

1. confronter la seconde méthode à des références externes ;
2. distinguer clairement le cadre général de ses applications internes au corpus Barons Mariani.

C’est pourquoi le présent article place le corpus en annexe et non au centre de l’argumentation principale.

## 11.4. Le risque politique

L’expérimentation peut servir le bien commun. Elle peut aussi servir la capture.

Dans un territoire sous tension foncière, énergétique, touristique ou numérique, toute expérimentation doit être évaluée selon une question simple :

> Qui gagne en capacité ?

Si la capacité est captée par des opérateurs extérieurs, des plateformes ou des oligarchies locales, l’expérimentation ne produit pas une autonomie de capacité. Elle produit une dépendance plus sophistiquée.

---

## 11.5. Le risque de neutralisation stylistique

Une dernière difficulté tient au style.

Plus un texte devient académique, plus il tend à neutraliser les images qui lui donnent sa force publique. Or certaines images — machine à empêcher, machine à explorer, discipline du tâtonnement — ne sont pas de simples ornements. Elles condensent des distinctions analytiques en formules transmissibles.

Le problème n’est donc pas d’éliminer ces images, mais de les encadrer. Une métaphore devient problématique lorsqu’elle se substitue à la démonstration. Elle devient utile lorsqu’elle intervient après la définition, la typologie, les limites et les conditions de validité.

Le présent article conserve donc volontairement certaines formules. Non par goût du manifeste, mais parce qu’une théorie de l’action publique doit pouvoir circuler hors des cercles spécialisés. Une idée politiquement inutilisable n’est pas nécessairement fausse ; mais elle reste incomplète si elle ne peut jamais devenir langage commun.

---

# 12. Conclusion : l’agile comme indice d’un changement plus large

L’agile n’est pas directement généralisable à toute la société.

Mais la distinction qu’il a rendue visible — entre planification de l’irréversible et exploration du réversible — pourrait devenir l’une des grammaires centrales de l’action publique au XXIe siècle.

Cette grammaire ne remplace pas la prudence. Elle la précise.

Elle ne dit pas : tout doit être essayé.

Elle dit : tout essai réversible, limité, traçable et attribuable ne doit pas être traité comme une action irréversible.

Elle ne dit pas : les objections sont des obstacles.

Elle dit : les objections doivent être qualifiées pour devenir des contributions.

Elle ne dit pas : l’IA va résoudre la complexité.

Elle dit : l’IA rend la traçabilité encore plus nécessaire.

Elle ne dit pas : la Corse prouve la théorie.

Elle dit : la Corse peut devenir un terrain d’application exigeant de cette théorie.

Dans un monde devenu trop complexe pour être entièrement lisible, la faute n’est pas de tâtonner.

La faute est de tâtonner sans méthode.

La seconde méthode est une proposition pour organiser ce tâtonnement : non comme improvisation, mais comme apprentissage collectif traçable.

---

# Annexe A — Cartographie du corpus Barons Mariani

Cette annexe situe le présent article dans le corpus de recherche de Jean Hugues Noël Robert. Elle n’est pas nécessaire à la compréhension de l’argument principal, mais elle indique les prolongements internes possibles.

## A.1. `second_method.md`

Document source définissant la seconde méthode comme pratique de publication du processus, transformation des objections en contributions, écriture pour humains et agents, et usage d’un corpus public versionné.

## A.2. `autonomie_de_capacite.md`

Application territoriale au cas corse. L’autonomie de capacité y est définie comme conversion du capital territorial en capabilités collectives effectives.

## A.3. `kudocracy.md`

Application démocratique. Kudocracy explore la démocratie liquide assistée par agents, avec distinction centrale entre suggestion et recommandation, et maintien de la décision politique chez les humains.

## A.4. `DHITL.md`

Architecture *Democratic Humans in the Loop*. Elle distingue les couches cognitives ouvertes aux agents artificiels et les couches délibératives réservées aux personnes vivantes.

## A.5. `cogentia`

Corpus sur les infrastructures cognitives, les signatures de raisonnement, les continuations, les paquets cognitifs et la traçabilité des inférences.

## A.6. `FractaVolta`

Application énergétique et infrastructurelle : packetisation de l’énergie, redondance, stockage distribué, conversion photons → inférences.

## A.7. `mimetic_desynchronization.md`

Cadre d’analyse de la désynchronisation mimétique, utile pour comprendre comment certains débats restent prisonniers de catégories qui empêchent de voir les capacités réelles.

---

# Annexe B — Gabarit d’objection qualifiée

Une objection devient utile lorsqu’elle peut être convertie dans le format suivant.

## B.1. Ressenti initial

Formulation brute :

> « Cette idée semble irréaliste. »

## B.2. Hypothèse contestée

Quelle proposition précise est contestée ?

> « L’hypothèse selon laquelle une commune peut déployer un micro-nœud énergétique en moins d’un an. »

## B.3. Risque identifié

Quel est le risque exact ?

> « Le délai administratif rend le calendrier impossible. »

## B.4. Donnée ou source nécessaire

Quelle donnée permettrait de vérifier ?

> « Délai moyen d’autorisation pour installations comparables dans les communes corses. »

## B.5. Critère de réfutation

À partir de quel seuil l’hypothèse est-elle réfutée ?

> « Si le délai médian dépasse 18 mois, l’hypothèse “moins d’un an” est réfutée dans le cadre actuel. »

## B.6. Modification proposée

Que faut-il changer ?

> « Remplacer “déployer” par “sélectionner site, obtenir préaccord et finaliser financement” dans la première année. »

## B.7. Trace dans le corpus

Où l’objection est-elle conservée ?

> « Section objections, avec date, auteur, réponse, statut : ouverte / intégrée / réfutée / reportée. »

---

# Annexe C — Typologie élargie des régimes d’erreur

| Domaine | Exemple | Erreur principale | Réversibilité | Exigence de méthode |
|---|---|---|---|---|
| Génie civil | Pont | Effondrement | Très faible | Calcul, certification, contrôle indépendant |
| Santé | Chirurgie | Atteinte corporelle | Faible | Consentement, protocole, responsabilité |
| Justice | Condamnation | Atteinte à la liberté | Faible à moyenne | Procédure contradictoire, appel |
| Logiciel | Application web | Bug, perte d’usage | Forte | Agile, tests, rollback |
| Cybersécurité | Système critique | Intrusion, panne | Variable | Défense en profondeur, audit |
| Startup | Produit nouveau | Mauvais marché | Moyenne | MVP, métriques, pivot |
| Politique locale | Mobilité, énergie | Effet social inégal | Variable | Expérimentation auditée |
| IA publique | Aide à la décision | Biais, opacité | Variable | Traçabilité, explicabilité, supervision |
| Démocratie | Vote, mandat | Légitimité atteinte | Faible | Délibération, recours, transparence |

---

# Continuation

Ce document appelle plusieurs prolongements.

## C1. Renforcer la bibliographie externe

Une version ultérieure devrait intégrer plus systématiquement :

- Cynefin et les régimes de complexité ;
- gouvernance adaptative des systèmes socio-écologiques ;
- experimentalist governance ;
- policy labs ;
- regulatory sandboxes ;
- littérature critique sur l’agile managérial ;
- travaux sur les limites démocratiques de l’expérimentation publique.

## C2. Ajouter des études de cas externes approfondies

La v0.5 introduit deux cas externes courts. Une version académique empirique devrait les transformer en véritables études de cas : contexte, chronologie, acteurs, données, effets mesurés, critiques et limites.

Exemples à documenter :

- FCA regulatory sandbox au Royaume-Uni ;
- GovTech et e-Estonia ;
- policy labs canadiens ou nordiques ;
- expérimentations territoriales européennes ;
- living labs urbains ;
- sandboxes IA ;
- démarches DevOps dans les administrations numériques.

## C3. Formaliser les critères de validité

La seconde méthode devrait être soumise à une grille minimale :

1. L’essai est-il réellement réversible ?
2. Les personnes concernées sont-elles identifiées ?
3. Les ayants-droit peuvent-ils contester ?
4. Les hypothèses sont-elles explicites ?
5. Les indicateurs sont-ils publics ?
6. Le responsable humain est-il identifié ?
7. Le protocole d’arrêt est-il prévu ?
8. Les résultats seront-ils publiés ?
9. La valeur créée restera-t-elle territorialisée ?
10. L’échec produira-t-il une connaissance transmissible ?

## C4. Revenir au cas corse

Le cas corse devra être développé dans un article spécifique reliant :

- autonomie de capacité ;
- campagne sénatoriale ;
- #1755 ;
- machine à empêcher / machine à explorer ;
- expérimentation territoriale ;
- IA civique ;
- souveraineté énergétique et cognitive.

---

# Références indicatives

## Agile, logiciel et DevOps

- Agile Manifesto. 2001. *Manifesto for Agile Software Development*. https://agilemanifesto.org/
- Agile Manifesto. 2001. *Principles behind the Agile Manifesto*. https://agilemanifesto.org/principles.html
- Royce, Winston W. 1970. *Managing the Development of Large Software Systems*. Proceedings IEEE WESCON. https://www.praxisframework.org/files/royce1970.pdf
- Schwaber, Ken, and Jeff Sutherland. 2020. *The Scrum Guide*. https://scrumguides.org/scrum-guide.html
- Beck, Kent. 1999. *Extreme Programming Explained: Embrace Change*. Addison-Wesley.
- Forsgren, Nicole, Jez Humble, and Gene Kim. 2018. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution.
- DORA / Google Cloud. 2024. *Accelerate State of DevOps Report*. https://dora.dev/research/
- Dikert, Kim, Maria Paasivaara, and Casper Lassenius. 2016. “Challenges and success factors for large-scale agile transformations: A systematic literature review.” *Journal of Systems and Software*.
- Moe, Nils Brede, et al. 2020. “Large-Scale Agile Transformation: A Case Study of Transforming Business, Development and Operations.” *Journal of Systems and Software* / open-access versions.

## Innovation, design, expérimentation

- Ries, Eric. 2011. *The Lean Startup*. Crown Business.
- IDEO. *Design Thinking*. https://designthinking.ideo.com/
- Brown, Tim. 2009. *Change by Design*. HarperBusiness.
- Ansell, Christopher, and Jacob Torfing, eds. 2014. *Public Innovation through Collaboration and Design*. Routledge.
- Sabel, Charles F., and Jonathan Zeitlin. 2012. “Experimentalist Governance.” In *The Oxford Handbook of Governance*. Oxford University Press.

## Gouvernance, complexité, communs

- Ostrom, Elinor. 1990. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Sen, Amartya. 1999. *Development as Freedom*. Oxford University Press.
- Nussbaum, Martha C. 2011. *Creating Capabilities: The Human Development Approach*. Harvard University Press.
- Snowden, David J., and Mary E. Boone. 2007. “A Leader’s Framework for Decision Making.” *Harvard Business Review*.
- Kurtz, Cynthia F., and David J. Snowden. 2003. “The New Dynamics of Strategy: Sense-making in a Complex and Complicated World.” *IBM Systems Journal*.
- Hausmann, Ricardo, and César A. Hidalgo. 2011. *The Atlas of Economic Complexity*. MIT Press.
- Williamson, Oliver E. 1985. *The Economic Institutions of Capitalism*. Free Press.

## Régulation et politiques publiques

- OECD. 2025. *Science, Technology and Innovation Outlook 2025*. OECD Publishing.
- OECD. *Recommendation of the Council on Artificial Intelligence*. OECD Legal Instruments.
- Financial Conduct Authority. 2017. *Regulatory Sandbox Lessons Learned Report*. FCA.
- Financial Conduct Authority. *Regulatory Sandbox*. FCA.
- Bank for International Settlements. Cornelli, Giulio, Sebastian Doerr, Leonardo Gambacorta, and Ouarda Merrouche. 2020. *Regulatory Sandboxes and Fintech Funding: Evidence from the UK*. BIS Working Papers.
- e-Estonia. *X-Road — Interoperability Services*. e-Estonia Briefing Centre.
- Nordic Institute for Interoperability Solutions. *X-Road*. https://x-road.global/
- European Commission. *X-Road — cross-border co-development of national data exchange platform*. EU Regional and Urban Development.
- European Commission. *Better Regulation Toolbox*. European Union.

## Corpus Jean Hugues Robert

- Robert, Jean Hugues Noël. `second_method.md`. Corpus `barons-Mariani`.
- Robert, Jean Hugues Noël. `autonomie_de_capacite.md`. Corpus `barons-Mariani`.
- Robert, Jean Hugues Noël. `kudocracy.md`. Corpus `barons-Mariani`.
- Robert, Jean Hugues Noël. `mimetic_desynchronization.md`. Corpus `barons-Mariani`.
- Robert, Jean Hugues Noël. `DHITL.md`. Corpus `marenostrum`.
- Robert, Jean Hugues Noël. `README.md`. Corpus `cogentia`.
- Robert, Jean Hugues Noël. `README.md`. Corpus `FractaVolta`.
