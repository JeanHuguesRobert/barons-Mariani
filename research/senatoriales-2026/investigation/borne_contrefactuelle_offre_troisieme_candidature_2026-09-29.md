---
title: "Sénatoriales 2026 — borne contrefactuelle de l’incidence d’une troisième candidature"
subtitle: "Ce qu’il aurait fallu, arithmétiquement et politiquement, pour empêcher une élection au premier tour en Haute-Corse"
author: "Jean Hugues Noël Robert"
date: "2026-09-29"
status: "active — filing-support analysis"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "electoral-counterfactual-analysis"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "post-scrutin analysis"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "research/senatoriales-2026/investigation/analyse_exposition_collegial_senatoriales_2026.md"
derived_from:
  - "../data/resultats_officiels_scrutin_2026-09-27.md"
  - "analyse_exposition_collegial_senatoriales_2026.md"
  - "../requete-conseil-constitutionnel.md"
  - "../data/annuaire_electeurs_senatoriaux_2B_2026.csv"
related_publication:
  - "../../../projects/suicide-corse/manuscript/magazine-n3/04-reality-case-senatoriales.md"
  - "../../../projects/suicide-corse/manuscript/18-le-reel-repond-2026-09-28.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Sénatoriales 2026 — borne contrefactuelle de l’incidence d’une troisième candidature

## 1. Objet

Ce document ne cherche pas à prédire le score qu’aurait obtenu la candidature Jean Hugues Noël Robert / Laurence Vernerey, ni à attribuer rétrospectivement des bulletins individuels.

Son objet est plus étroit : **déterminer les conditions minimales sous lesquelles la présence d’une troisième candidature aurait pu modifier le fait juridiquement décisif du premier tour**, à savoir l’obtention ou non par Paul-Toussaint Parigi de la majorité absolue des suffrages exprimés.

Le document est destiné à servir simultanément :

- au dossier de recherche sénatorial ;
- à la requête en contestation devant le Conseil constitutionnel ;
- à la projection éditoriale de *Suicide Corse n°3* ;
- aux futures analyses contradictoires du Corpus.

Il distingue systématiquement :

```text
fait observé
≠
hypothèse
≠
borne arithmétique
≠
prédiction
```

## 1 bis. Cette borne comme frontière d’une uchronie contrainte

La présente note fournit désormais la **frontière mathématique** d’un chantier plus large :

`research/senatoriales-2026/investigation/uchronie_troisieme_candidat_2026-09-29.md`

Ce nouveau jalon applique au scrutin la méthode uchronique déjà présente dans le Corpus : point de bifurcation identifiable, scénarios contraints, continuité causale, cohérence interne et utilité heuristique.

La borne 134–177 n’est donc pas un score hypothétique. Elle sépare simplement :

```text
branches où Parigi reste élu au premier tour
≠
branches où sa majorité absolue disparaît
```

## 2. Faits observés

Les résultats publiés pour le premier tour en Haute-Corse sont :

| Indicateur | Valeur |
|---|---:|
| Inscrits | 616 |
| Votants | 606 |
| Abstentions | 10 |
| Blancs | 36 |
| Nuls | 40 |
| Suffrages exprimés | 530 |
| Paul-Toussaint Parigi | 442 |
| Nicolas Battini | 88 |

Source officielle : ministère de l’Intérieur, résultats des sénatoriales 2026, Haute-Corse (2B).

L’article L.294 du code électoral prévoit que, dans les départements où sont élus deux sénateurs ou moins, l’élection se déroule au scrutin majoritaire à deux tours. Pour être élu au premier tour, un candidat doit obtenir :

1. la majorité absolue des suffrages exprimés ;
2. un nombre de voix au moins égal au quart des électeurs inscrits.

Au second tour, la majorité relative suffit.

Dans le scrutin observé, le quart des inscrits vaut 154 voix. Avec 442 voix, M. Parigi satisfait très largement cette condition. La seule question arithmétique pertinente pour l’hypothèse d’un second tour est donc celle de sa **majorité absolue parmi les exprimés**.

## 3. Modèle minimal

Notons :

- `x` = nombre de voix effectivement portées sur M. Parigi dans le scrutin observé qui, avec une troisième candidature admise, ne se seraient plus portées sur lui ;
- `z` = nombre de bulletins blancs, nuls ou, dans le scénario maximal, d’abstentions qui seraient devenus des suffrages exprimés valables.

Le nombre de suffrages exprimés devient alors :

```text
530 + z
```

et le score de M. Parigi :

```text
442 - x
```

Pour qu’il ne dispose plus de la majorité absolue au premier tour, il faut :

```text
442 - x <= floor((530 + z) / 2)
```

Cette formule ne suppose aucune origine politique particulière aux voix déplacées. Elle exprime seulement la condition arithmétique minimale.

## 4. Bornes du scénario de second tour

| Scénario purement arithmétique | Nouveaux exprimés `z` | Exprimés totaux | Diminution minimale du score Parigi `x` |
|---|---:|---:|---:|
| Aucun blanc/nul converti | 0 | 530 | **177** |
| Tous les 36 blancs convertis | 36 | 566 | **159** |
| Tous les 40 nuls convertis | 40 | 570 | **157** |
| Tous les blancs + nuls convertis | 76 | 606 | **139** |
| Blancs + nuls + 10 abstentions convertis | 86 | 616 | **134** |

La plage pertinente est donc de **134 à 177 voix**, selon le nombre de non-exprimés qui auraient été convertis en suffrages valables.

Rapportée aux 442 voix observées de M. Parigi, cette diminution correspond à environ **30,3 % à 40,0 %** de son score.

## 5. Premier résultat : les 76 blancs et nuls ne suffisent pas

Une lecture trop rapide consisterait à traiter les 36 blancs et 40 nuls comme un « réservoir » susceptible de créer à lui seul un second tour.

Cette hypothèse est arithmétiquement fausse.

Même si les 76 bulletins devenaient tous des suffrages valables pour une troisième candidature, sans déplacer aucune voix de M. Parigi :

```text
Parigi = 442
exprimés = 606
majorité absolue = 304
```

M. Parigi resterait élu au premier tour.

Cette correction est importante pour le contentieux : **l’argument ne peut pas reposer sur la seule existence des blancs et nuls**.

## 6. Deuxième résultat : une troisième candidature pouvait agir sur plus que les non-exprimés

L’autre erreur symétrique serait d’en déduire que la présence d’une troisième candidature ne pouvait rien changer.

Une candidature supplémentaire modifie potentiellement plusieurs objets à la fois :

```text
choix disponible
+ campagne
+ prises de position publiques
+ consignes
+ premier choix des électeurs
+ votes stratégiques
+ blancs / nuls
+ répartition entre les autres candidats
```

Le contrefactuel pertinent n’est donc pas :

> « Combien des 76 blancs ou nuls auraient voté Robert ? »

mais plutôt :

> **« Une offre supplémentaire, distincte des deux offres admises, pouvait-elle déplacer au total au moins 134 à 177 voix aujourd’hui observées sur Parigi, selon le niveau de conversion des non-exprimés ? »**

Cette question est beaucoup plus exigeante. Elle ne peut recevoir une réponse certaine, puisque la candidature n’a jamais été soumise au suffrage. Mais elle peut être **étayée, bornée, contredite ou rendue plus plausible** par des observations.

## 7. Indices actuellement pertinents — sans attribution de vote individuel

### 7.1. L’écart Battini

Le modèle documentaire identifie cinq grands électeurs institutionnellement rattachés à l’offre Battini, tandis que celui-ci obtient 88 voix.

Le seul constat robuste est :

```text
socle institutionnel identifié : 5
score observé : 88
écart : 83
```

Cet écart montre que l’appartenance institutionnelle publiquement observable ne suffit pas à prévoir le comportement agrégé de l’urne.

Il ne permet pas de dire quels électeurs ont voté Battini, ni d’où viennent les 83 voix d’écart.

### 7.2. Les blancs et nuls

Les 76 blancs et nuls montrent qu’une fraction non négligeable des votants n’a produit de suffrage valable en faveur d’aucun des deux candidats admis.

Ils ne forment pas nécessairement un bloc homogène et ne peuvent pas être transformés en voix potentielles pour une candidature exclue.

### 7.3. La consigne Morganti

Un appel public au vote blanc a existé à Bastia. Le groupe concerné fournit un **périmètre d’exposition**, non un décompte de bulletins.

Le cas Hélène Salge doit rester traité avec prudence : son départ ultérieur du groupe est documenté, mais la source consultée ne permet pas d’établir que son désaccord portait spécifiquement sur la consigne sénatoriale de vote blanc.

### 7.4. Nature de la candidature exclue

La candidature 2026 constituait une offre distincte des deux candidatures finalement admises. Elle associait Jean Hugues Noël Robert au courant de Jean-François Baccarelli et portait notamment une proposition parlementaire propre relative à l’effectivité du futur article 72-5 de la Constitution.

Il ne s’agit donc pas d’un simple clonage des offres Parigi ou Battini.

Cette différence est documentable ; son effet électoral ne l’est pas directement.

## 8. Hiérarchie des hypothèses

Pour éviter de masquer les hypothèses tout en conservant leur statut, le Corpus retient la gradation suivante :

| Hypothèse | Statut actuel |
|---|---|
| Une troisième candidature aurait obtenu au moins une partie des blancs/nuls | plausible mais non quantifiable |
| Elle aurait également déplacé des voix aujourd’hui portées sur Battini | possible, non quantifiable |
| Elle aurait déplacé des voix aujourd’hui portées sur Parigi | nécessaire pour le scénario de second tour, mais amplitude inconnue |
| Elle aurait déplacé au moins 134 à 177 voix de Parigi selon le scénario | condition arithmétique du second tour, non démontrée empiriquement |
| Un second tour aurait effectivement eu lieu | hypothèse ouverte, non prédiction |
| La candidature exclue aurait gagné | non établi et non inféré |

Cette hiérarchie constitue un garde-fou contre deux excès opposés :

```text
surinterprétation
→ transformer une hypothèse en résultat

sous-interprétation
→ traiter comme nulle une hypothèse simplement parce qu’elle ne peut plus être observée
```

## 9. Portée pour le contentieux électoral

Le point utile pour la requête n’est pas de convaincre le Conseil constitutionnel qu’un second tour aurait nécessairement eu lieu.

Il est de rendre la question de l’incidence **concrète et testable** :

- quelle était la règle de majorité ?
- quelle redistribution minimale aurait modifié l’issue du premier tour ?
- quels faits observés montrent que l’offre électorale et les blocs publics ne se convertissent pas mécaniquement en bulletins ?
- quels éléments supplémentaires pourraient renforcer ou affaiblir l’hypothèse ?

La formulation prudente est donc :

> **Le scrutin observé ne permet pas de démontrer qu’une troisième candidature aurait provoqué un second tour. Il permet en revanche de calculer exactement la magnitude minimale du changement nécessaire pour qu’un second tour ait lieu, puis de rechercher si le contexte politique et documentaire rend cette magnitude manifestement impossible, possible mais peu étayée, ou suffisamment plausible pour qu’une incidence ne puisse être écartée sans examen.**

Cette approche ne transforme pas la perte d’observation produite par l’exclusion en certitude favorable au requérant. Elle interdit simplement de la transformer automatiquement en certitude défavorable.

## 9 bis. Traduction directe pour la requête

La présente borne n'est pas un pronostic électoral.

Elle fournit seulement un test de matérialité de l'incidence.

Les résultats observés sont :
- **71,8 % du collège électoral (442 voix sur 616)** pour M. Parigi ;
- **14,3 % du collège (88 voix sur 616)** pour M. Battini ;
- **12,3 % du collège (76 bulletins sur 616)** pour les blancs et nuls ;
- **86,0 % du collège (530 suffrages exprimés sur 616)**.

Pour faire disparaître la majorité absolue de M. Parigi au premier tour, une troisième offre aurait dû produire, selon les scénarios retenus, une modification équivalente à **134 à 177 voix aujourd'hui observées sur M. Parigi**, éventuellement combinée à une conversion d'une partie des non-exprimés en suffrages valables.

Rapportée au collège électoral total, cette borne correspond à environ **21,8 % à 28,7 % du collège**.

Cette traduction est importante : elle permet de comparer la magnitude nécessaire à des phénomènes observables sans prétendre prédire un score.

Le scrutin de Corse-du-Sud fournit un comparateur descriptif utile : une offre distincte y a recueilli environ **32,9 % du collège électoral** le même jour. Cette comparaison ne permet pas d'assimiler les deux circonscriptions ni les candidatures. Elle montre seulement qu'un ordre de grandeur supérieur à la borne minimale calculée en Haute-Corse n'est pas, en soi, électoralement inconcevable dans le contexte corse du même scrutin.

Le point contentieux peut donc être formulé ainsi :

> **l'incidence d'une troisième candidature n'est pas démontrée ; elle n'est pas non plus manifestement exclue par l'arithmétique du scrutin ni par les seuls soutiens publiquement visibles.**

La disparition de l'offre empêche précisément d'observer :
- son score ;
- ses effets sur les choix de premier tour ;
- ses effets sur les blancs et nuls ;
- ses effets sur les reports stratégiques ;
- ses effets sur la campagne et sur les alliances.

Cette perte d'observation ne doit être transformée ni en preuve favorable au requérant ni en preuve de l'absence d'incidence.

## 10. Éléments encore utiles à documenter

Le document doit évoluer en fonction de nouvelles traces. Les recherche ciblées les plus discriminants sont :

1. **procès-verbal et bulletins nuls** — déterminer les motifs matériels des 40 nullités ;
2. **réactions post-scrutin** — identifier les acteurs qui décrivent explicitement des reports, hésitations ou refus d’offre ;
3. **consignes documentées** — distinguer exposition publique et vote secret ;
4. **annuaire des grands électeurs** — enrichir les appartenances et sources sans inférer les bulletins ;
5. **comparaisons inter-scrutins** — uniquement descriptives, sans supposer que deux collèges ou deux candidatures sont interchangeables ;
6. **campagne empêchée** — documenter ce qui n’a pas pu être observé du fait de l’exclusion : débat audiovisuel, prise de position des soutiens, éventuels reports et alliances.

Chaque nouvelle trace doit pouvoir :

```text
renforcer
affaiblir
ou laisser inchangée
```

l’hypothèse d’une incidence substantielle.

## 11. Usage éditorial dans Suicide Corse n°3

Dans *Suicide Corse n°3*, cette analyse ne doit pas devenir une démonstration électorale opaque.

Le corps magazine peut en retenir quatre idées simples :

1. 76 blancs et nuls ont été observés, mais ne suffisent pas à eux seuls à créer un second tour ;
2. une troisième candidature aurait dû modifier aussi une part importante des 442 voix Parigi ;
3. la borne minimale se situe entre 134 et 177 voix selon les scénarios ;
4. l’exclusion de la candidature rend précisément non observable l’effet qu’elle aurait pu produire sur les comportements et la campagne.

Les tableaux, équations et hypothèses détaillées restent dans le Corpus comme annexe vérifiable.

Cette articulation suit la règle éditoriale :

> **le corps principal raconte ; le Corpus démontre.**

## 12. Sources publiques principales

- Ministère de l’Intérieur, résultats des sénatoriales 2026, Haute-Corse : https://www.resultats-elections.interieur.gouv.fr/Senatoriales2026/ensemble_geographique/94/2B/index.html
- Code électoral, article L.294 : https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000027804524/2026-01-01
- Annuaire et modèle d’exposition : `research/senatoriales-2026/data/annuaire_electeurs_senatoriaux_2B_2026.csv` et `investigation/analyse_exposition_collegial_senatoriales_2026.md`
- Requête stable au Conseil constitutionnel : `research/senatoriales-2026/requete-conseil-constitutionnel.md`

## 13. Formule de clôture provisoire

```text
on ne sait pas quel aurait été le scrutin
≠
on ne peut rien dire du contrefactuel

on peut au minimum :
mesurer la distance au second tour
+ documenter les mécanismes capables de déplacer cette distance
+ conserver les inconnues
+ laisser le Réel renforcer ou affaiblir l’hypothèse
```
