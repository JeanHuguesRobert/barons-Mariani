---
title: "Sénatoriales Corse — analyse statistique comparée 2A/2B, 2020/2026"
subtitle: "Quatre scrutins simultanés par paire, non-expression et incertitude modèle"
author: "Jean Hugues Noël Robert"
date: "2026-10-02"
status: "active-checkpoint"
language: fr
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "comparative-electoral-statistical-analysis"
visibility: public
lifecycle_state: active
update_policy: UP-DEFAULT-REVIEWED
derived_from:
  - "../data/comparatif_2A_2B_2020_2026.csv"
  - "uchronie_troisieme_candidat_matrice_probes_2026-09-29.md"
  - "borne_contrefactuelle_offre_troisieme_candidature_2026-09-29.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Sénatoriales Corse — analyse statistique comparée 2A/2B, 2020/2026

## 1. Question

Le but n'est pas de calculer une probabilité de victoire ou une probabilité qu'un second tour « aurait eu lieu ».

Cette quantité contrefactuelle n'est pas identifiée par les seules données disponibles.

On peut en revanche estimer rigoureusement des quantités observables ou des paramètres probabilistes explicitement modélisés :

- taux de bulletins blancs+nuls parmi les votants ;
- différences de taux entre scrutins tenus le même jour et dans la même fenêtre horaire ;
- rapports de cotes sous hypothèse d'échangeabilité des bulletins ;
- probabilités bayésiennes portant sur des **propensions de non-expression**, et non sur l'issue électorale contrefactuelle.

## 2. Les quatre cas

| Année | Département | Candidats | Votants | Blancs | Nuls | Blancs+nuls | Exprimés | Taux non-exprimé |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2020 | Corse-du-Sud (2A) | 2 | 404 | 29 | 31 | 60 | 344 | 14,85 % |
| 2020 | Haute-Corse (2B) | 5 | 572 | 8 | 6 | 14 | 558 | 2,45 % |
| 2026 | Corse-du-Sud (2A) | 4 | 458 | 2 | 4 | 6 | 452 | 1,31 % |
| 2026 | Haute-Corse (2B) | 2 | 606 | 36 | 40 | 76 | 530 | 12,54 % |

Sources officielles :

- 2020 2A : Ministère de l'Intérieur, archives sénatoriales 2020 ;
- 2020 2B : Ministère de l'Intérieur, archives sénatoriales 2020 ;
- 2026 2A : Ministère de l'Intérieur, sénatoriales 2026 ;
- 2026 2B : Ministère de l'Intérieur, sénatoriales 2026.

En 2020, la Corse-du-Sud avait deux candidatures au premier tour : Jean-Jacques Panunzi et Baron Mariani. En Haute-Corse, cinq candidatures étaient présentes.

En 2026, la structure s'inverse : quatre candidatures en Corse-du-Sud et deux candidatures admises en Haute-Corse.

## 3. Comparabilité temporelle

Les comparaisons 2A/2B au sein d'une même année sont particulièrement intéressantes car les scrutins sont organisés le même jour et dans la même fenêtre légale.

En 2020 comme en 2026, dans les départements au scrutin majoritaire, le premier tour est ouvert à **08 h 30** et clos à **11 h 00**, sauf clôture anticipée si tous les électeurs ont voté.

Cette simultanéité réduit certains facteurs temporels grossiers :

- même journée nationale de scrutin ;
- même fenêtre horaire légale ;
- même contexte médiatique national immédiat.

Elle ne rend pas les deux départements interchangeables.

## 4. Observation centrale : un cross-over descriptif

Le motif descriptif est remarquable :

```text
2020
2 candidats  → 2A → 14,85 % non exprimés
5 candidats  → 2B →  2,45 %

2026
4 candidats  → 2A →  1,31 %
2 candidats  → 2B → 12,54 %
```

Autrement dit, dans les deux années, le scrutin à **deux candidats** est aussi celui où le taux de blancs+nuls est très supérieur au scrutin corse tenu simultanément avec davantage de candidats.

Le département portant cette configuration change entre 2020 et 2026.

C'est un motif de réplication descriptive de type **cross-over**.

Ce motif ne suffit pas à établir une causalité « moins de candidats → plus de blancs+nuls ».

## 5. Intervalles d'incertitude

Les résultats publiés sont des comptages exhaustifs du scrutin, pas un sondage.

Le taux observé lui-même n'a donc pas une « marge d'erreur d'échantillonnage » au sens classique.

Pour quantifier l'incertitude sur une **propension latente de non-expression**, on peut néanmoins utiliser un modèle binomial de travail.

### 5.1 Intervalles de Wilson à 95 %

| Scrutin | Taux observé | Intervalle Wilson 95 % |
|---|---:|---:|
| 2020 2A | 14,85 % | 11,72–18,65 % |
| 2020 2B | 2,45 % | 1,46–4,07 % |
| 2026 2A | 1,31 % | 0,60–2,83 % |
| 2026 2B | 12,54 % | 10,14–15,42 % |

Ces intervalles doivent être lus comme des intervalles de modèle sous répétition hypothétique d'un mécanisme comparable, pas comme une incertitude sur le comptage officiel lui-même.

## 6. Contrastes simultanés par année

### 2020

Différence brute de taux :

```text
14,85 % - 2,45 % = +12,40 points
```

Sous un modèle binomial bayésien de Jeffreys, l'intervalle crédible 95 % de la différence est approximativement :

```text
+8,84 à +16,23 points
```

Rapport de cotes ballot-level :

```text
OR = 6,95
IC 95 % ≈ 3,83–12,63
```

### 2026

Différence brute de taux :

```text
12,54 % - 1,31 % = +11,23 points
```

Intervalle crédible 95 % de la différence sous le même modèle :

```text
+8,41 à +14,11 points
```

Rapport de cotes :

```text
OR = 10,80
IC 95 % ≈ 4,66–25,04
```

Dans les deux années, le contraste est donc très grand relativement aux tailles des collèges.

## 7. Probabilités de modèle

Avec un prior de Jeffreys Beta(1/2,1/2) pour chaque propension de non-expression, la probabilité postérieure que la propension du scrutin à deux candidats soit supérieure à celle du scrutin simultané avec davantage de candidats est supérieure à **99,999 %** dans chacune des deux années.

Cette quantité signifie uniquement :

> **sous le modèle binomial choisi et conditionnellement aux quatre comptages observés, les données soutiennent très fortement un contraste de propension de non-expression entre les deux scrutins de chaque année.**

Elle ne signifie pas :

- qu'il existe une probabilité de 99,999 % que le nombre de candidats soit la cause du contraste ;
- qu'une troisième candidature aurait reçu telle proportion de voix ;
- qu'un second tour aurait eu telle probabilité ;
- qu'un résultat électoral alternatif peut être prédit.

## 8. Estimation stratifiée exploratoire

En traitant 2020 et 2026 comme deux strates et en comparant, dans chaque strate, le scrutin à deux candidats au scrutin corse simultané avec davantage de candidats, l'odds ratio de Mantel-Haenszel est :

```text
OR_MH ≈ 8,40
IC 95 % ≈ 5,15–13,71
```

Le test d'homogénéité des odds ratios ne détecte pas d'incompatibilité notable entre les effets ballot-level de 2020 et 2026 :

```text
p ≈ 0,392
```

Mais ce résultat ne transforme pas deux années en grand échantillon d'élections.

L'unité causale pertinente reste l'**élection**, et nous n'avons ici que quatre cellules électorales.

Traiter les 2 040 votants comme 2 040 expériences politiques indépendantes produirait une pseudo-réplication.

## 9. Ce que le cross-over apporte réellement

Le motif est plus informatif qu'une simple comparaison 2A/2B en 2026 :

```text
2020 :
la configuration à deux candidats est en 2A
et le taux de non-expression élevé est en 2A

2026 :
la configuration à deux candidats est en 2B
et le taux de non-expression élevé est en 2B
```

Ainsi, l'association descriptive « configuration à deux candidats ↔ forte non-expression » survit au changement :

- d'année ;
- de département ;
- de candidats principaux ;
- de composition exacte des collèges.

C'est un **indice de robustesse descriptive**.

Ce n'est pas une identification causale, car d'autres variables changent simultanément.

## 10. Pourquoi 2020 2A est un comparateur particulièrement utile

Le cas 2020 2A n'est pas une comparaison abstraite : le scrutin comportait précisément deux candidatures, dont Baron Mariani.

Les résultats officiels sont :

- Panunzi : 336 ;
- Baron Mariani : 8 ;
- blancs : 29 ;
- nuls : 31 ;
- exprimés : 344 ;
- votants : 404.

Cela offre un antécédent empirique utile pour observer ce que peut produire une configuration corse à deux candidats comportant cette offre de candidature.

Il serait toutefois erroné de transporter mécaniquement les 8 voix de 2020 vers 2026 : département, collège, contexte, offre concurrente et campagne diffèrent.

## 11. Relation avec l'uchronie 2026

Cette analyse change la qualité de la branche U1/U2/U4 mais ne résout pas U3.

Elle apporte ceci :

```text
fait 1 :
les deux scrutins corses à deux candidats
présentent chacun un taux de non-expression élevé

fait 2 :
les deux scrutins corses simultanés avec 4 ou 5 candidats
présentent chacun un taux de non-expression faible

fait 3 :
au moins un nul 2B 2026 porte matériellement
« BARON MARIANI »

mais :

on ne connaît toujours pas
le déplacement contrefactuel de 134–177 voix Parigi
nécessaire selon les scénarios U3.
```

L'analyse statistique contraint donc les mécanismes de l'uchronie sans attribuer une probabilité à l'issue électorale alternative.

## 12. Programme scientifique suivant

Pour augmenter réellement la résolution, il faut élargir l'échantillon d'**élections**, pas seulement le nombre de bulletins.

Priorités :

1. récupérer les élections sénatoriales corses antérieures comparables, idéalement plusieurs renouvellements ;
2. enregistrer pour chacune le nombre de candidatures, blancs, nuls, votants, exprimés et éventuel second tour ;
3. rechercher des départements métropolitains comparables à un siège et scrutin majoritaire ;
4. ajuster ensuite un modèle hiérarchique au niveau élection, avec effets année/département et nombre d'offres ;
5. publier des distributions postérieures et intervalles crédibles, en séparant toujours :
   - comportement de non-expression ;
   - causalité de l'offre ;
   - résultat électoral contrefactuel.

## 13. Règle de publication

Toute probabilité doit préciser son objet.

Forme acceptable :

> « Sous le modèle M, la probabilité postérieure que la propension de non-expression du scrutin A dépasse celle du scrutin B est … »

Forme à proscrire avec les données actuelles :

> « Il y avait X % de chances qu'un troisième candidat provoque un second tour. »

La seconde quantité n'est pas identifiée par les observations disponibles.
