---
title: "De l’ordre juste à la Traçabilité des actes"
subtitle: "Généalogie de SimpliWiki, Kudocracy, COP et du Stabilisateur procédural"
version: "0.1"
date: "2026-09-15"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
status: "working note — généalogie corrigible"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "derived"
document_kind: "research-note"
visibility: "public"
lifecycle_state: "working"
repository: "JeanHuguesRobert/barons-Mariani"
canonical_path: "research/genealogie_ordre_transparence_traceabilite.md"
related_documents:
  - "research/traceabilite_des_actes.md"
  - "research/debord_stabilisateur_procedural.md"
  - "research/reality_safety_procedural_stabilizers.md"
  - "research/le_reel_le_virtuel_et_l_actuel.md"
  - "research/kudocracy.md"
external_repositories:
  - "JeanHuguesRobert/simpli"
  - "virteal/kudocracy"
  - "JeanHuguesRobert/inseme"
---

# De l’ordre juste à la Traçabilité des actes

## Généalogie de SimpliWiki, Kudocracy, COP et du Stabilisateur procédural

## 0. Statut et méthode

Cette note reconstruit une **généalogie technique et intellectuelle provisoire** de plusieurs idées aujourd’hui présentes dans le Corpus : transparence, versionnement, réversibilité, journalisation, délibération distincte de la décision, Traçabilité des actes et Stabilisateur procédural.

Elle ne prétend pas démontrer une filiation psychologique continue ni établir que les formulations de 2026 étaient déjà consciemment présentes dans les travaux antérieurs. Elle rassemble des **traces datées** montrant que plusieurs choix techniques et politiques récurrents apparaissent bien avant leur formalisation doctrinale actuelle.

Il faut distinguer :

- les **traces publiques vérifiables** dans les dépôts historiques ;
- les **publications anciennes déjà retrouvées mais pas encore toutes réintégrées dans le Corpus public** ;
- les **souvenirs de l’auteur**, qui orientent la recherche mais ne valent pas à eux seuls preuve documentaire ;
- l’**interprétation généalogique de 2026**, nécessairement rétrospective et corrigible.

Les futures extractions de publications Facebook et d’autres archives devront compléter, confirmer, déplacer ou contredire certains jalons intermédiaires.

---

## 1. 2009–2010 : ordre, désordre, transparence

### 1.1 « Pas d’art sans ordre »

L’auteur rapporte avoir réalisé en 2009 un détournement d’une œuvre de Ben Vautier portant la formule **« Pas d’art sans désordre »** : la formule devient **« Pas d’art sans ordre »**, la signature imitée de Ben étant suivie du monogramme JHR, produisant visuellement « Ben JHR ».

À ce stade, l’existence matérielle et la datation précise de cette œuvre reposent encore sur le témoignage de l’auteur ; une photographie, une publication datée ou une autre trace indépendante restent à retrouver.

L’intérêt généalogique n’est donc pas probatoire mais heuristique : le couple **ordre / désordre** apparaît très tôt comme une tension créatrice plutôt que comme une opposition où l’un des termes devrait abolir l’autre.

### 1.2 2010 : « ordre juste » et transparence

Une publication ancienne retrouvée, datée du 6 avril 2010, formule déjà plusieurs éléments qui seront repris plus tard sous une forme beaucoup plus opérationnelle :

> « Pas d’art sans ordre » ; « Le chaos n’aide pas » ; et la transparence comme condition nécessaire à « l’ordre juste ».

La distinction essentielle est déjà présente : **l’ordre n’est pas bon en soi**. Il peut être l’ordre promis par le dictateur. Le problème devient donc celui d’un ordre suffisamment structurant pour éviter le chaos, mais suffisamment contrôlable pour ne pas se transformer en domination opaque.

À ce stade, la **transparence** apparaît comme une partie importante de la réponse, mais le mécanisme permettant de produire durablement cette transparence n’est pas encore formalisé.

Cette lacune sera progressivement comblée par des choix techniques : versionner, conserver, rendre réversible, journaliser, publier les actes, puis relier trace, mandat, justification, correction et révocation.

---

## 2. 2010–2011 : SimpliWiki — versionner pour pouvoir revenir

Le dépôt historique `JeanHuguesRobert/simpli` et ses pages embarquées attestent SimpliWiki au plus tard en 2010–2011.

SimpliWiki introduit explicitement des mécanismes de **contrôle des changements** :

- une contribution d’un visiteur peut rester un *draft* ;
- un membre peut la valider (*stamp*) ;
- ou restaurer le **contenu précédent** de la page ;
- la documentation indique ensuite `Page History: yes` et `Page Revisions: yes`.

Le point généalogique est moins « un wiki possède un historique » que le choix explicite suivant :

> **un état courant ne doit pas effacer la possibilité de retrouver l’état précédent.**

Le versionnement permet donc une première forme de corrigibilité : l’action n’est pas seulement visible dans son résultat présent ; elle s’inscrit dans une histoire où le retour et la comparaison restent possibles.

On peut résumer ce premier jalon ainsi :

```text
VERSIONNER
→ conserver les états antérieurs
→ rendre le passé récupérable
→ rendre la correction praticable
```

Cette logique constitue un ancêtre technique plausible de la Traçabilité des actes, sans qu’il faille projeter rétrospectivement la doctrine actuelle sur SimpliWiki.

---

## 3. 2014–2015 : Kudocracy — séparer délibération et acte décisionnel

### 3.1 Une proposition, une page Wiki, un vote distinct

Le dépôt historique `virteal/kudocracy`, créé sur GitHub le 20 avril 2014, conserve une architecture particulièrement importante pour la présente généalogie.

Dans l’interface historique, une proposition Kudocracy peut être reliée à une **page Wiki portant le même identifiant ou label**. Le code affiche explicitement un lien vers le wiki depuis la proposition et, dans certaines configurations, indique que « la proposition dispose d’une page dans le wiki ».

L’architecture sépare ainsi deux fonctions :

```text
WIKI
→ documenter
→ argumenter
→ amender
→ délibérer
→ conserver l’historique

        ↕ proposition commune

KUDOCRACY
→ voter
→ déléguer
→ réviser son vote
→ agréger
→ publier le résultat
→ journaliser les actes
```

Cette séparation est structurante : **la délibération et la décision sont reliées mais ne sont pas confondues**.

Le wiki porte la construction collective de la Carte ; Kudocracy porte l’acte civique explicite.

### 3.2 Votes publics et réversibles

Une publication du 28 juin 2014 déjà retrouvée affirme explicitement que, dans Kudocracy :

- les votes pris en compte dans un corps électoral identifié sont publics ;
- la liste des votants est publique ;
- cette publicité doit permettre à chacun de vérifier l’absence de fraude électorale ;
- la formule politique proposée est : **« Transparence dans les affaires publiques, secret dans la vie privée. »**

Le README historique consolide ensuite plusieurs propriétés :

- votes sur des propositions plutôt que seulement sur des candidats ;
- délégation thématique ;
- votes **réversibles** ;
- votes **publics** pour éviter la fraude et favoriser la transparence et la discussion ouverte ;
- résultats actualisés en temps réel ;
- données ouvertes.

La transparence n’est donc déjà plus seulement un souhait moral. Elle devient une **propriété de l’architecture civique**.

### 3.3 Journal persistant et replay

Le moteur historique utilise notamment un stockage nommé `vote.json.log`.

La couche de données indique qu’un changement injecté dans la machine est :

1. enregistré dans un stockage persistant ;
2. conservé sous forme de changement ;
3. rejoué lorsque la machine redémarre.

L’implémentation normale écrit les changements par ajout dans le fichier (`appendFileSync`) et le code parle explicitement de *log based persistence* et de replay.

Il faut rester précis : ce mécanisme applicatif n’est pas, à lui seul, un registre cryptographiquement infalsifiable. Un administrateur disposant des droits sur le fichier peut techniquement le réécrire. Mais la **sémantique normale de fonctionnement** est bien :

```text
ACTE
→ ajout au journal
→ conservation chronologique
→ replay
→ reconstruction de l’état
```

C’est un jalon nettement plus proche de la Traçabilité des actes que le simple versionnement d’un document.

---

## 4. De la transparence à la reconstructibilité

Les jalons précédents permettent de distinguer progressivement deux notions :

> **La transparence rend visible ; la traçabilité rend reconstructible.**

Une institution peut publier énormément d’informations sans permettre de répondre à des questions simples :

- qui a fait quoi ?
- au nom de quel mandat ?
- à quel moment ?
- à partir de quelles informations ?
- avec quels effets ?
- qui en répond ?
- comment l’acte peut-il être contesté, corrigé ou révoqué ?

La Traçabilité des actes, telle qu’elle est formalisée en 2026 dans `research/traceabilite_des_actes.md`, généralise ce besoin sous une forme beaucoup plus exigeante : l’acte engageant doit laisser suffisamment de traces pour devenir **imputable, justifiable, contestable et corrigible**.

La chaîne devient :

```text
TRACE
→ IMPUTATION
→ JUSTIFICATION
→ CORRECTION
→ RÉVOCATION / SANCTION éventuelle
```

L’hypothèse généalogique de cette note est donc la suivante : la doctrine de 2026 ne surgit pas ex nihilo ; elle **généralise progressivement plusieurs choix techniques et politiques plus anciens**.

---

## 5. 2026 : GitHub reprend une partie du rôle du Wiki

Le Corpus actuel est largement construit dans GitHub :

- documents versionnés ;
- Issues ;
- commentaires ;
- commits ;
- historique inspectable ;
- provenance des modifications ;
- possibilité de relire les états antérieurs.

GitHub joue ainsi aujourd’hui une partie du rôle autrefois confié à SimpliWiki : il fournit une **surface documentaire et délibérative versionnée**.

L’équivalence n’est évidemment pas stricte, mais la séparation fonctionnelle reste reconnaissable :

```text
SimpliWiki hier
≈ documents + discussions versionnées

GitHub aujourd’hui
≈ documents + Issues + commentaires + commits

Kudocracy
≈ couche distincte d’actes civiques et de décision
```

La règle conceptuelle reste :

> **on discute et construit la Carte dans un espace délibératif ; on pose ensuite l’acte décisionnel dans un espace où cet acte doit être explicite et traçable.**

---

## 6. Inseme : réarticuler Wiki, propositions, votes et provenance Git

Le dépôt `JeanHuguesRobert/inseme` contient en 2026 plusieurs traces de cette réarticulation.

Une migration désormais classée `superseded` — donc à considérer comme **trace architecturale**, non comme schéma courant autoritatif — réunissait explicitement :

- `wiki_pages` ;
- `propositions` ;
- `votes` ;
- `delegations` ;
- `git_sync_log` avec suivi des commits et de la provenance des pages.

Un document de migration mentionne également la validation du mapping entre :

> « propositions Kudocracy, votes, pages/révisions Wiki »

et les schémas Inseme / COP.

Il existe donc une continuité technique explicite entre le couple historique Wiki/Kudocracy et l’architecture contemporaine Inseme.

---

## 7. COP : généraliser la trace, l’ordre et la causalité

Le **Cognitive Orchestration Protocol (COP)** pousse plus loin ce mouvement.

Sa spécification actuelle est *trace-centric* et traite notamment comme objets de premier rang :

- Traces ;
- Events ;
- Artifacts ;
- Assertions ;
- EvidenceRelations ;
- Topics ;
- Acts ;
- mandats et capacités d’exécution.

Elle prévoit notamment :

- un ordre par Topic (`topicSeq`) ;
- des liens de causalité (`parentEventIds`) ;
- des sémantiques de replay ;
- des projections reconstructibles ;
- des identifiants et versions ;
- le hashing ;
- des signatures optionnelles ;
- des mécanismes d’auditabilité.

COP ne garantit pas magiquement la vérité, la responsabilité juridique ou l’inaltérabilité absolue. La garantie effective dépend de l’implémentation, des politiques, du stockage et du contexte institutionnel. Mais il fournit un **substrat protocolaire** permettant de rendre les actes, leurs dépendances et leur histoire beaucoup plus explicitement traçables.

La différence avec Kudocracy historique peut être formulée ainsi :

```text
Kudocracy
→ journaliser des actes civiques spécifiques

COP
→ généraliser la notion de trace et de causalité
  à des actes, artefacts, décisions et processus hétérogènes
```

---

## 8. Du révélateur au Stabilisateur procédural

Cette généalogie rejoint directement le couple **révélateur / stabilisateur**.

Une trace n’est pas seulement une archive passive. Elle permet de reconstruire ce qui s’est effectivement passé. À ce titre, la Traçabilité des actes peut devenir un **révélateur** : elle rend visibles les dépendances, les décisions, les délais, les bifurcations et les responsabilités qui produisent une situation.

Mais la même traçabilité sert aussi le **Stabilisateur procédural**.

Un stabilisateur sain ne doit pas seulement rendre une action reproductible ; il doit préserver la possibilité de comprendre et de corriger son propre fonctionnement.

On peut donc proposer la formulation suivante :

> **Un Stabilisateur procédural est une organisation opérationnelle suffisamment ordonnée pour rendre l’action normalement praticable, mais suffisamment traçable pour que son fonctionnement, ses écarts et ses échecs restent reconstructibles et corrigibles.**

La Traçabilité des actes relie ainsi les deux côtés :

```text
RÉVÉLATEUR
→ rendre le fonctionnement reconstructible
→ comprendre ce qui ouvre ou ferme des possibles

TRAÇABILITÉ DES ACTES
→ conserver actes, ordre, provenance, causalité et mandat

STABILISATEUR PROCÉDURAL
→ rendre une capacité reproductible
→ tout en conservant la capacité de corriger la procédure
```

Une formule en découle :

> **La Traçabilité des actes empêche l’ordre de devenir aveugle.**

---

## 9. Chronologie provisoire

| Date | Trace / jalon | Statut épistémique | Apport à la généalogie |
|---|---|---|---|
| 2009 | détournement « Pas d’art sans ordre », signature « Ben JHR » | témoignage de l’auteur ; trace matérielle indépendante à retrouver | tension ordre / désordre |
| 6 avril 2010 | publication « Le chaos n’aide pas » ; transparence comme condition de « l’ordre juste » | publication ancienne retrouvée ; réintégration publique à compléter | transparence comme exigence politique |
| septembre 2010–2011 | SimpliWiki attesté ; drafts, restauration du contenu précédent | dépôt / pages historiques | versionnement, retour, corrigibilité |
| 20 avril 2014 | création du dépôt `virteal/kudocracy` | métadonnée GitHub | début public vérifiable du dépôt actuel |
| avril–juin 2014 | Wiki lié aux propositions ; `vote.json.log` ; persistence par log et replay | code historique | séparation délibération / acte ; journalisation |
| 28 juin 2014 | votes publics, liste publique des votants, transparence des affaires publiques | publication ancienne retrouvée | transparence transformée en propriété civique opératoire |
| 2015 | README Kudocracy : votes réversibles/publics, résultats temps réel, données ouvertes | dépôt historique | publicité + réversibilité + ouverture |
| 2016 | reprise Kudocracy / Nuit Debout, lien avec SimpliWiki encore présent | dépôt historique | continuité du couple Wiki/Kudocracy |
| dates à retrouver | publications Facebook sur transparence, responsabilité et « Traçabilité des actes » | traces annoncées, non encore extraites | datation de la cristallisation conceptuelle |
| 2026 | `traceabilite_des_actes.md` | document source du Corpus | formalisation : trace, mandat, imputabilité, contrôle, correction |
| 2026 | GitHub / Inseme / COP | dépôts et spécifications | versionnement, provenance, causalité, replay, hashing, mandat |
| 2026 | Stabilisateur procédural | documents du Corpus | rendre la capacité durable sans rendre la procédure incorrigible |

---

## 10. Hypothèse généalogique

L’hypothèse de travail à tester est :

> **La Traçabilité des actes généralise progressivement plusieurs intuitions et choix techniques antérieurs : conserver les versions avec SimpliWiki ; séparer délibération et acte avec le couple SimpliWiki/Kudocracy ; rendre les votes publics et réversibles ; journaliser les changements ; puis généraliser avec Git, Inseme et COP la provenance, l’ordre, la causalité, le replay, le mandat et l’imputabilité.**

Cette hypothèse est **soutenue mais non close**. Elle devra être corrigée à mesure que les archives anciennes — notamment Facebook — seront extraites et datées.

Il faut notamment rechercher les premières occurrences documentées des expressions ou idées suivantes :

- transparence ;
- ordre juste ;
- responsabilité ;
- imputabilité ;
- traçabilité ;
- Traçabilité des actes ;
- journal des actes ;
- vote public ;
- historique ;
- versions ;
- correction ;
- révocation.

---

## 11. Formules de travail

> **Versionner, c’est rendre le passé récupérable.**

> **Journaliser, c’est rendre l’action reconstructible.**

> **Tracer les actes, c’est rendre l’exercice du pouvoir imputable et corrigible.**

> **Le wiki garde mémoire de ce que nous avons pensé et discuté ; le registre décisionnel garde mémoire de ce que nous avons fait ; COP cherche à conserver aussi le lien causal entre les deux.**

> **La transparence rend visible ; la traçabilité rend reconstructible.**

> **La Traçabilité des actes empêche l’ordre de devenir aveugle.**

---

## 12. Sources et pistes de vérification

### Dépôts historiques

- `https://github.com/JeanHuguesRobert/simpli`
- `https://github.com/virteal/kudocracy`
- `https://github.com/JeanHuguesRobert/inseme`

### Fichiers historiques particulièrement utiles

- `JeanHuguesRobert/simpli/simplijs/wiki/SimpliWikiDifference`
- `virteal/kudocracy/README.md`
- `virteal/kudocracy/lib/main.js`
- `virteal/kudocracy/lib/ephemeral.js`
- `virteal/kudocracy/lib/pageproposition.js`
- `virteal/kudocracy/lib/pageindex.js`
- `JeanHuguesRobert/inseme/packages/cop-core/Architecture.md`

### Corpus actuel

- [`traceabilite_des_actes.md`](traceabilite_des_actes.md)
- [`debord_stabilisateur_procedural.md`](debord_stabilisateur_procedural.md)
- [`reality_safety_procedural_stabilizers.md`](reality_safety_procedural_stabilizers.md)
- [`le_reel_le_virtuel_et_l_actuel.md`](le_reel_le_virtuel_et_l_actuel.md)
- [`kudocracy.md`](kudocracy.md)

### Continuation

1. Extraire progressivement les publications Facebook et autres archives personnelles anciennes.
2. Dater les premières occurrences de « traçabilité » et « Traçabilité des actes ».
3. Retrouver si possible une trace indépendante de l’œuvre « Pas d’art sans ordre » de 2009.
4. Vérifier les commits historiques de SimpliWiki et Kudocracy pour resserrer les dates d’apparition des fonctions de versionnement, log, replay et liaison Wiki/Kudocracy.
5. Comparer les invariants historiques de Kudocracy avec le profil civique actuel d’Inseme/COP sans écraser leurs différences techniques et politiques.
6. Réviser la présente chronologie lorsque de nouvelles traces contredisent ou précisent la Carte.
