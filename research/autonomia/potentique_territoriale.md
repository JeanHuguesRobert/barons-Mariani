---
title: "Potentique territoriale"
subtitle: "Cartographier les possibles, les capacités et les mécanismes d'ouverture et de fermeture d'un territoire"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani — C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
version: "0.1"
date: "2026-09-01"
license: "CC BY-SA 4.0"
status: "working-paper"
document_role: "exploration"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
---

# Potentique territoriale

## Orientation

Ce document prolonge [Autonomia](../autonomia.md), qui définit l'**Autonomie de Capacité** comme test opératoire de l'autonomie territoriale corse. Il ne remplace pas ce document source : il ouvre un chantier plus spécifiquement potentique consacré à l'observation des possibles qu'un territoire ouvre, facilite, rend coûteux, invisibilise ou ferme pour différents sujets.

Il s'inscrit dans la Potentique (*Potentics*), entendue comme discipline de l'exploration rationnelle du Possible, et dans la doctrine **Le Réel Répond** : les cartes de potentialités doivent être corrigées par des interactions et expérimentations observables, traçables et, autant que possible, réversibles.

La Corse constitue le premier terrain d'observation. Le **Corsica Cogentia Digital Twin (CCDT)** est envisagé comme un instrument vivant de cette observation, non comme une autorité décrétant ce qui est possible.

## 1. Hypothèse centrale

Un territoire n'est pas seulement un espace dans lequel des événements se produisent. Il transforme la capacité de différents sujets à explorer et actualiser des possibles.

Pour un possible `p`, un sujet `s`, un territoire `T` et un instant `t`, on peut noter provisoirement :

\[
\phi(p \mid s,T,t)
\]

la potentialité contextuelle de `p` pour `s` dans `T` à `t`.

Cette écriture rappelle que la potentialité n'est pas une propriété intrinsèque et intemporelle du possible. Elle dépend notamment des ressources, institutions, infrastructures, connaissances, relations, droits, coûts, interfaces et circonstances disponibles au sujet.

Une première chaîne utile est :

```text
Possible → Accessible → Actualisable → Actualisé
```

Un possible peut exister dans le Territoire sans être représenté dans la Carte institutionnelle ; il peut être représenté sans être accessible à un sujet donné ; il peut être accessible sans être raisonnablement actualisable.

## 2. Autonomie de Capacité et Potentique territoriale

`Autonomia` pose une distinction structurante : l'autonomie statutaire décrit ce qu'un territoire a le droit de faire ; l'Autonomie de Capacité examine ce qu'il est effectivement capable de faire.

La Potentique territoriale généralise cette question :

> **Quels possibles un territoire rend-il effectivement explorables et actualisables, pour quels sujets, à quelles conditions et avec quels effets sur les autres possibles ?**

Le sujet peut être un individu, une famille, une association, une entreprise, une commune, une institution, un collectif ou le territoire lui-même.

Cette approche permet d'étudier simultanément l'autonomie collective et l'autonomie individuelle. Une augmentation de la capacité du territoire ne garantit pas une augmentation de la capacité de ses habitants. Inversement, des individus très capables mais enfermés dans une architecture collective incapable d'agir ne produisent pas nécessairement une forte Autonomie de Capacité territoriale.

## 3. Machines à Explorer et Machines à Empêcher

La Potentique territoriale rencontre deux familles de mécanismes.

### 3.1. Machine à Explorer

Une **Machine à Explorer** augmente la capacité d'un ou plusieurs sujets à découvrir, comparer, tester ou actualiser des possibles. Elle peut notamment :

- rendre une information accessible ;
- réduire un coût ou une friction ;
- créer une ressource ou une capacité ;
- rendre visible un chemin auparavant ignoré ;
- permettre la bifurcation, le retour ou la réversibilité ;
- améliorer la capacité à participer ;
- produire des traces permettant à d'autres explorations de bénéficier des précédentes.

### 3.2. Machine à Empêcher

Une **Machine à Empêcher** est provisoirement définie comme un mécanisme dont l'effet est de réduire la potentialité, l'accessibilité ou l'explorabilité de certains possibles pour certains sujets.

Elle peut prendre la forme d'une interdiction explicite, mais aussi d'une ontologie administrative trop pauvre, d'une interface, d'un coût, d'une dépendance, d'une asymétrie informationnelle, d'une norme sociale, d'une absence de canal traçable, d'une contrainte technique ou d'une accumulation de petites frictions.

Elle n'est pas nécessairement intentionnelle. Une hypothèse importante à tester est qu'une Machine à Empêcher peut émerger de la composition de contraintes localement raisonnables mais globalement non réévaluées du point de vue de la **Capacity to Participate**.

### 3.3. Ne pas confondre empêchement et nuisance

Toute fermeture d'un possible n'est pas mauvaise. Une règle peut réduire la potentialité de `p1` afin de préserver ou augmenter celle de `p2…pn`. Une analyse potentique ne classe donc pas mécaniquement une contrainte comme bonne ou mauvaise : elle cherche à observer la transformation du champ des potentialités et sa distribution entre sujets.

La question devient :

> Quel risque cette contrainte réduit-elle ? Quels possibles ferme-t-elle ? Pour qui ? Quels possibles protège-t-elle ou ouvre-t-elle ? Existe-t-il une manière moins restrictive d'obtenir la même garantie ?

## 4. Spécificité territoriale

Les Machines à Explorer et à Empêcher ne se manifestent probablement pas de manière identique selon les territoires.

Une propriété territoriale peut être empêchante pour un possible et facilitatrice pour un autre. L'insularité, la petite taille, la densité relationnelle, l'éloignement, la saisonnalité, les ressources naturelles ou l'organisation institutionnelle ne doivent donc pas être classés a priori en « forces » et « faiblesses ».

La Potentique territoriale cherche plutôt à observer leurs effets conditionnels :

```text
territoire + sujet + possible + contexte
                    ↓
       facilitateurs / contraintes
                    ↓
       trajectoire effectivement suivie
                    ↓
             réponse du Réel
```

La comparaison entre territoires devient alors particulièrement instructive : un même possible poursuivi par des sujets comparables peut révéler des gradients territoriaux de potentialité.

## 5. Protocole minimal d'observation

Une observation devrait, lorsque les données le permettent, conserver au moins :

```yaml
observation:
  possible: ...
  subject_type: individual | association | company | commune | institution | collective | territory
  territory: ...
  time: ...
  intended_outcome: ...
  required_capabilities: ...
  facilitators: ...
  obstacles: ...
  workaround: ...
  effort: ...
  monetary_cost: ...
  human_attention: ...
  channel: ...
  trace: ...
  outcome: ...
  reality_response: ...
  reopened_possibles: ...
  closed_possibles: ...
  uncertainty: ...
```

Ce schéma est exploratoire. Il ne doit pas devenir une ontologie rigide avant confrontation suffisante au Réel.

## 6. Le Corsica Cogentia Digital Twin comme instrument

Le CCDT peut progressivement devenir une **Carte expérimentale du Possible en Corse**.

Il doit conserver une séparation stricte entre Carte et Territoire. Il ne déclare pas qu'un possible est impossible parce qu'il ne le connaît pas. Il représente plusieurs interprétations concurrentes lorsque nécessaire et conserve provenance, incertitude, désaccords et corrections humaines.

Boucle générale :

```text
Corse réelle
    ↓
observations / interactions / données publiques / Reality Tests
    ↓
traces avec provenance
    ↓
Corsica Cogentia Digital Twin
    ↓
carte provisoire des capacités et potentialités
    ↓
nouveaux possibles / bifurcations / Reality Tests
    ↓
Corse réelle
```

La boucle de retour vers le Réel est constitutive du dispositif.

## 7. Capacity to Participate

L'une des applications principales concerne la démocratie.

Les droits formels ne suffisent pas à produire une participation effective. Un sujet doit disposer de capacités suffisantes pour accéder à l'information, comprendre, interroger, contester, formuler une alternative, interagir avec une institution et conserver une trace exploitable de cette interaction.

L'**Autonomie de Capacité** peut donc être examinée à deux niveaux simultanés :

1. capacité du territoire à décider et agir par lui-même ;
2. capacité des personnes et collectifs du territoire à comprendre, participer, choisir, contester et agir par eux-mêmes.

Une autonomie territoriale qui augmenterait la première tout en réduisant ou laissant inchangée la seconde serait une autonomie de capacité incomplète.

## 8. Premiers Reality Tests

Le travail ne doit pas commencer par une taxonomie exhaustive des empêchements corses. Il doit commencer par des interactions réelles.

Les premiers cas peuvent provenir notamment :

- des démarches institutionnelles et administratives conduites en Corse ;
- des expérimentations documentées liées à `Autonomia` ;
- des démarches de participation démocratique et électorale ;
- des interactions nécessaires à la construction du CCDT et d'Olé Olé ;
- des projets énergétiques, de mobilité, de logement, d'accès aux services ou d'accès aux capacités numériques et IA ;
- des comparaisons avec des démarches équivalentes conduites hors de Corse.

Un cas externe peut également servir à calibrer la méthode. L'exploration 2026 de l'accès EuroHPC, par exemple, fait apparaître des mécanismes possibles d'empêchement par catégories juridiques, affiliation, relation salariale, identité professionnelle, formats documentaires et architecture des canaux. Ces observations ne doivent être qualifiées qu'à partir de traces et de réponses institutionnelles effectivement obtenues : **Le Réel Répond**.

## 9. Programme de recherche

Premières questions ouvertes :

1. Comment distinguer une contrainte territoriale d'une contrainte nationale, européenne ou universelle ?
2. Comment comparer les potentialités sans prétendre les réduire à un scalaire unique ?
3. Comment mesurer l'effort, le délai, l'attention humaine et les coûts cachés ?
4. Comment représenter qu'une même règle ouvre certains possibles tout en en fermant d'autres ?
5. Comment préserver les différences entre sujets souverains dans une représentation commune ?
6. Comment détecter les effets de composition de contraintes localement raisonnables ?
7. Comment transformer une observation en Reality Test reproductible ou comparable ?
8. Comment permettre au CCDT de découvrir des Machines à Explorer, et pas seulement des empêchements ?
9. Comment relier cette cartographie à l'évaluation empirique d'un futur statut d'autonomie de la Corse ?

## 10. Principe de prudence épistémique

La Potentique territoriale ne doit pas partir à la recherche de preuves qu'un territoire « empêche » ou « permet ».

Elle part de possibles effectivement poursuivis, observe les trajectoires, conserve les traces, compare lorsque c'est possible, puis corrige sa Carte.

> **Nous essayons de faire quelque chose. Nous observons ce qui nous aide et ce qui nous en empêche. Le Réel répond ; la Carte apprend.**

## Continuations

- relier explicitement ce document à `autonomia.md` sans alourdir le document source ;
- créer un protocole/versionnement des observations territoriales ;
- relier la méthode aux travaux Potentics, Machine à Explorer / Machine à Empêcher, Interaction Packets et traçabilité symétrique ;
- instrumenter progressivement ces observations dans le Corsica Cogentia Digital Twin ;
- comparer des possibles identiques entre Corse et autres territoires ;
- utiliser les résultats publics comme matériau de mesure de l'Autonomie de Capacité, sans transformer le CCDT en outil partisan.
