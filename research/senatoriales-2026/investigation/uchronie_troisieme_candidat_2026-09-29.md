---
title: "Uchronie sénatoriale 2026 — la branche du troisième candidat"
subtitle: "Exploration contrefactuelle contrainte d’un scrutin empêché"
author: "Jean Hugues Noël Robert"
date: "2026-09-29"
status: "active-checkpoint"
language: fr
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "constrained-political-counterfactual"
visibility: public
lifecycle_state: active
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: "post-scrutin constrained counterfactual analysis"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "research/senatoriales-2026/investigation/borne_contrefactuelle_offre_troisieme_candidature_2026-09-29.md"
derived_from:
  - "../data/resultats_officiels_scrutin_2026-09-27.md"
  - "borne_contrefactuelle_offre_troisieme_candidature_2026-09-29.md"
  - "analyse_exposition_collegial_senatoriales_2026.md"
  - "../requete-conseil-constitutionnel-projet-v0.2.md"
  - "../../../musee-mariani/methodes/articulation_musee_uchronique.md"
  - "../../../musee-mariani/methodes/exploration_rationnelle_des_possibles.md"
related_publication:
  - "../../../projects/suicide-corse/manuscript/magazine-n3/04-reality-case-senatoriales.md"
  - "../../../projects/suicide-corse/journals/2026-09-29-n3-convergence-effectivite-qpc.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Uchronie sénatoriale 2026 — la branche du troisième candidat

## 1. Objet

Ce document applique au scrutin sénatorial de Haute-Corse du 27 septembre 2026 une méthode déjà présente dans le Corpus : **l’uchronie contrainte**.

Il ne cherche pas à écrire un récit alternatif libre du type :

> « si la candidature Robert / Vernerey avait été admise, voici ce qui se serait passé ».

Il cherche à répondre à une question plus rigoureuse :

> **si le point de bifurcation avait produit l’admission de la troisième candidature, quels mondes électoraux restent compatibles avec les faits, les règles du scrutin et les traces aujourd’hui disponibles ?**

L’uchronie devient ici un instrument d’analyse rétrospective du Possible, non une prédiction électorale.

## 2. Cadre méthodologique hérité du Corpus

Le Corpus définit déjà le Musée uchronique comme un dispositif qui :

1. identifie un point de bifurcation ;
2. construit des scénarios contrefactuels soumis à des contraintes de cohérence ;
3. compare la trajectoire advenue aux trajectoires non advenues ;
4. cherche ce que cette comparaison apprend au présent.

Trois exigences gouvernent cette méthode :

- **continuité causale** ;
- **cohérence interne** ;
- **utilité heuristique**.

Dans l’Exploration Rationnelle du Possible, la règle complémentaire est :

```text
bifurcation proche et documentée
→ contrefactuel relativement contraint

cascade de conséquences
→ incertitude croissante
```

Le cas sénatorial est particulièrement adapté parce que la bifurcation est récente, formalisée et entourée de données quantitatives nombreuses.

## 3. Branche actuelle et branche empêchée

La bifurcation peut être représentée ainsi :

```text
candidature Robert / Vernerey
          ↓
décision sur l'enregistrement
          │
     ┌────┴────┐
     │         │
 admission    refus
     │         │
     │         └→ branche actuelle observée
     │             deux candidatures admises
     │             Parigi 442
     │             Battini 88
     │             blancs 36
     │             nuls 40
     │
     └→ branche non advenue
         trois candidatures
         campagne différente
         consignes possiblement différentes
         votes stratégiques possiblement différents
         résultat inconnu
```

La branche non advenue est **fermée comme événement historique**, mais elle n’est pas épistémiquement vide.

## 4. Contraintes du Réel

L’uchronie est bornée par les faits officiels du scrutin réellement tenu :

| Indicateur | Valeur |
|---|---:|
| Inscrits | 616 |
| Votants | 606 |
| Abstentions | 10 |
| Blancs | 36 |
| Nuls | 40 |
| Exprimés | 530 |
| Parigi | 442 |
| Battini | 88 |

Source officielle : ministère de l’Intérieur, résultats des sénatoriales 2026 en Haute-Corse.

L’article L.294 du code électoral impose, au premier tour, la majorité absolue des suffrages exprimés et au moins un quart des inscrits ; au second tour, la majorité relative suffit.

Ces règles imposent une frontière mathématique indépendante de toute préférence politique.

## 5. Frontière du second tour

Soit :

- `x` = nombre de voix observées sur Parigi qui, dans la branche à trois candidatures, ne se seraient plus portées sur lui ;
- `z` = nombre de blancs, nuls ou abstentions devenant suffrages exprimés valables.

La perte de majorité absolue au premier tour exige :

```text
442 - x <= floor((530 + z) / 2)
```

D’où :

| Scénario | Diminution minimale de Parigi |
|---|---:|
| aucun non-exprimé converti | 177 |
| 36 blancs convertis | 159 |
| 40 nuls convertis | 157 |
| 76 blancs+nuls convertis | 139 |
| blancs+nuls+10 abstentions convertis | 134 |

Cette plage **134–177** est une frontière de scénario, pas une estimation du score de la troisième candidature.

## 6. Carte des scénarios uchroniques

### U0 — Quasi-invariance

Hypothèse minimale :

- la troisième candidature attire peu de voix ;
- elle ne modifie pas substantiellement les consignes ni les comportements ;
- Parigi conserve la majorité absolue.

Statut :

> **compatible avec les faits ; non réfutable à ce stade.**

Cette branche rappelle que l’admission de la troisième candidature n’implique pas automatiquement une modification de l’issue.

### U1 — Conversion des seuls non-exprimés

Hypothèse :

- une partie ou la totalité des 36 blancs et 40 nuls devient suffrage valable ;
- aucune voix observée sur Parigi ne se déplace.

Même dans le cas maximal :

```text
Parigi = 442
exprimés = 606
majorité absolue = 304
```

Parigi reste élu au premier tour.

Statut :

> **insuffisant arithmétiquement pour créer un second tour.**

### U2 — Redistribution partielle sans second tour

Hypothèse :

- la troisième offre attire certains non-exprimés ;
- elle déplace aussi certaines voix observées sur Parigi et/ou Battini ;
- mais pas assez pour faire perdre la majorité absolue à Parigi.

Cette branche couvre une large zone de possibles.

Statut :

> **compatible avec une incidence électorale réelle mais non décisive sur l’élection au premier tour.**

### U3 — Franchissement de la frontière

Hypothèse :

- les non-exprimés se redistribuent en partie ;
- une fraction suffisante des 442 voix Parigi ne se porte plus sur lui ;
- la condition 134–177 est atteinte selon le scénario.

Conséquence :

> **Parigi ne dispose plus de la majorité absolue au premier tour ; un second tour devient nécessaire au regard de l’article L.294.**

Cette formulation ne dit pas qui aurait gagné ensuite.

Statut :

> **branche arithmétiquement définissable ; plausibilité empirique à instruire.**

### U4 — Recomposition stratégique

La présence d’un troisième candidat ne modifie pas seulement l’allocation mécanique de bulletins. Elle peut également modifier :

- la campagne ;
- les prises de position publiques ;
- les consignes ;
- les alliances ;
- les votes de premier choix ;
- les votes stratégiques ;
- le comportement entre premier et second tour.

Dans cette branche, la distribution observée 442 / 88 / 76 ne peut plus être traitée comme une matrice fixe à laquelle on ajouterait simplement une troisième colonne.

Statut :

> **possible en théorie, mais causalement plus éloigné et donc plus incertain.**

### U5 — Issue finale alternative

Toute proposition du type :

- « Robert aurait gagné » ;
- « Battini aurait été au second tour » ;
- « tel groupe aurait basculé » ;
- « tel grand électeur aurait voté pour tel candidat » ;

ajoute plusieurs maillons causaux non observables.

Statut :

> **fortement indéterminé en l’état ; ne pas utiliser comme conclusion.**

## 7. Tableau de discipline épistémique

| Élément | Statut |
|---|---|
| résultats 442 / 88 / 36 / 40 | fait observé |
| règles de L.294 | règle juridique |
| borne 134–177 | conséquence mathématique |
| troisième candidature = offre distincte | fait documentable |
| certains blancs/nuls auraient pu devenir exprimés | hypothèse |
| des voix Parigi auraient pu se déplacer | hypothèse nécessaire à U3 |
| amplitude effective de ces déplacements | inconnue |
| second tour effectif | uchronie possible, non prédiction |
| vainqueur d’un second tour | indéterminé |
| vote individuel d’un grand électeur | secret / non inféré |

## 8. Indices capables de discriminer les branches

L’uchronie devient utile si elle produit des probes.

### Probe A — Bulletins nuls

Question :

> les 40 bulletins nuls contiennent-ils des indications matérielles révélant une demande de choix non disponible ?

Effet potentiel :

- renforcer ou affaiblir U1/U2 ;
- ne suffit pas seul à établir U3.

### Probe B — Réactions post-scrutin

Question :

> des élus ou groupes ont-ils décrit publiquement des hésitations, reports, choix par défaut ou refus des offres disponibles ?

Effet potentiel :

- documenter la mobilité du collège ;
- contraindre U2/U3/U4 sans identifier les votes individuels.

### Probe C — Annuaire politique public

Question :

> quelles appartenances, alliances et consignes étaient objectivement documentées avant le vote ?

Effet potentiel :

- cartographier les expositions ;
- ne jamais transformer une exposition en bulletin.

### Probe D — Campagne qui n’a pas eu lieu

Question :

> quels actes de campagne, débats, prises de position ou ralliements auraient matériellement été possibles entre l’admission et le scrutin ?

Effet potentiel :

- contraindre la distance causale entre la bifurcation et U3/U4.

### Probe E — Offre parlementaire distincte

Question :

> la candidature exclue portait-elle une offre identifiable qui n’était pas contenue dans les deux offres admises ?

Effet potentiel :

- documenter qu’il existait réellement un troisième choix politique ;
- ne dit pas combien de voix il aurait reçu.

## 9. Uchronie et contentieux électoral

Cette analyse ne demande pas au juge de choisir une uchronie comme vraie.

Sa fonction contentieuse potentielle est plus limitée :

```text
irrégularité alléguée
→ offre supprimée
→ effet électoral non directement observable
→ espace contrefactuel borné
→ recherche de savoir si l'absence d'incidence
  peut réellement être tenue pour manifeste
```

La borne U3 transforme une spéculation vague en question mesurable : selon le scénario, **134 à 177 voix observées sur Parigi devaient se déplacer** pour rendre un second tour nécessaire.

Le reste doit être étayé ou affaibli par les probes.

## 10. Uchronie et Principe d’effectivité

Le cas illustre une forme particulière de perte d’observation :

```text
capacité juridique revendiquée
→ obstacle
→ branche non actualisée
→ résultat de cette branche devenu inobservable
→ reconstruction contrainte
→ recours / correction éventuelle
```

L’uchronie ne répare pas l’événement.

Elle permet de ne pas confondre :

```text
non observé
≠ impossible

possible
≠ probable

plausible
≠ établi
```

## 11. Lien avec l’Exploration Rationnelle du Possible

Le cas sénatorial devient un Reality Case contemporain de l’uchronie contrainte.

Le processus est :

```text
bifurcation documentée
→ fixer les invariants
→ cartographier les branches
→ éliminer les branches impossibles
→ graduer les branches restantes
→ chercher les probes discriminants
→ corriger la Carte
```

L’objectif n’est pas de produire une belle histoire alternative.

L’objectif est de **réduire rationnellement l’espace des histoires alternatives compatibles avec le Réel**.

## 12. Usage dans Suicide Corse n°3

Le corps Magazine peut utiliser une version courte :

> **Une uchronie n’est pas ici une histoire inventée. C’est une expérience de pensée contrainte : partir du seul embranchement qui n’a pas eu lieu — l’admission d’une troisième candidature — puis éliminer tout ce que les règles et les faits rendent impossible. Les 76 blancs et nuls ne suffisent pas à créer un second tour. Pour y parvenir, il aurait aussi fallu déplacer entre 134 et 177 voix observées sur Parigi selon les scénarios. Nous ne savons pas si cela se serait produit ; nous savons désormais ce qu’il aurait fallu pour que cela se produise.**

Le détail reste dans le Corpus.

## 13. Sources primaires et méthode

Sources électorales :

- Ministère de l’Intérieur — Sénatoriales 2026 — Haute-Corse :  
  https://www.resultats-elections.interieur.gouv.fr/Senatoriales2026/ensemble_geographique/94/2B/index.html
- Code électoral, article L.294 :  
  https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000027804524/2026-01-01

Méthode du Corpus :

- `research/uchronian_museum.md`
- `musee-mariani/methodes/articulation_musee_uchronique.md`
- `musee-mariani/methodes/exploration_rationnelle_des_possibles.md`
- `research/autonomia/potentique_territoriale.md`

## 13 bis. Matrice empirique des probes

La première passe de discrimination empirique U0–U5 est désormais conservée dans :

`research/senatoriales-2026/investigation/uchronie_troisieme_candidat_matrice_probes_2026-09-29.md`

Elle confronte les branches à sept probes déjà documentés :

- résultats officiels Haute-Corse ;
- existence publique pré-scrutin de la troisième candidature ;
- analyse pré-scrutin d’une droite « orpheline de candidat » ;
- écart entre noyau institutionnel Battini et score obtenu ;
- réactions post-scrutin sur les circulations de voix ;
- comparateur descriptif Corse-du-Sud ;
- contrôle de provenance sur les chiffres blancs/nuls ;
- cas Salge comme rappel de la distinction exposition / bulletin.

La matrice ne cherche pas à sélectionner une branche. Elle identifie ce que chaque trace permet ou interdit d’inférer.

## 14. Jalon

Ce document constitue le premier jalon explicite d’une **uchronie électorale contemporaine** dans le Corpus.

Sa formule canonique est :

> **L’uchronie ne cherche pas à écrire ce qui se serait passé ; elle cartographie ce qui pouvait encore se passer à partir du point de bifurcation, puis élimine progressivement les scénarios incompatibles avec les faits.**
