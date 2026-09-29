---
title: "Suicide Corse n°3 — Spécial sénatoriales — audit de bouclage tardif"
author: "Jean Hugues Noël Robert"
date: "2026-09-29"
status: "active-close-audit"
language: fr
license: "CC BY-SA 4.0"
document_role: "editorial-audit"
document_kind: "late-close-audit"
visibility: public
lifecycle_state: active
update_policy: UP-DERIVED-SOURCE-LOCKED
provenance:
  origin_type: "editorial-close-decision"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: main
  derived_from:
    - projects/suicide-corse/projections/book-n3-working.yml
    - projects/suicide-corse/audits/2026-09-28-final-content-sweep-n3.md
    - research/senatoriales-2026/data/resultats_officiels_scrutin_2026-09-27.md
    - research/senatoriales-2026/investigation/analyse_exposition_collegial_senatoriales_2026.md
    - research/senatoriales-2026/investigation/borne_contrefactuelle_offre_troisieme_candidature_2026-09-29.md
review:
  status: "human-directed"
  reviewed_by:
    - "Jean Hugues Noël Robert"
---

# Suicide Corse n°3 — Spécial sénatoriales — audit de bouclage tardif

## 1. Décision éditoriale

Le numéro 3 de *Suicide Corse* est désormais qualifié :

> **Numéro 3 — Spécial sénatoriales**

Son bouclage intervient exceptionnellement le **mardi 29 septembre 2026**, soit un jour après la cadence hebdomadaire habituelle du lundi.

Ce décalage n'est pas traité comme un incident de production. Il résulte d'une décision éditoriale motivée par la temporalité même du Reality Case principal :

```text
dimanche 27 septembre
→ scrutin sénatorial

lundi 28 septembre
→ résultats stabilisés
→ premières réactions publiques
→ analyses et corrections du Corpus

mardi 29 septembre
→ intégration contradictoire
→ bouclage spécial
```

La publication du lundi aurait figé l'édition avant que les principales réactions au scrutin puissent être confrontées aux résultats officiels.

## 2. Règle de cadence

La cadence hebdomadaire du lundi reste la règle ordinaire.

Le présent numéro constitue une exception explicite :

```text
cadence normale
= lundi

événement structurant le dimanche
+ réactions significatives attendues le lundi
→ report borné au mardi
→ justification enregistrée
→ reprise de la cadence normale ensuite
```

Le retard doit rester **borné, explicite et productif**. Il ne crée pas une permission générale de repousser le freeze pour absorber indéfiniment de nouvelles informations.

## 3. Pourquoi les réactions post-scrutin sont matériellement pertinentes

Le n°3 ne se contente pas de rapporter un résultat électoral. Il examine un cas d'effectivité : une candidature exclue avant le vote, un scrutin finalement limité à deux candidatures et la question de savoir si l'exclusion peut être tenue pour manifestement sans incidence.

Les réactions publiées après le scrutin sont donc utiles lorsqu'elles permettent de mieux distinguer :

- implantation institutionnelle publique ;
- consignes documentées ;
- comportements agrégés observés ;
- interprétations revendiquées par les acteurs ;
- hypothèses encore ouvertes.

Elles ne doivent jamais servir à attribuer un vote individuel secret.

## 4. Corrections intégrées avant freeze

Le Corpus a été corrigé sur plusieurs points qui impactent directement le Spécial sénatoriales.

### 4.1. Résultats officiels

Haute-Corse :

- 616 inscrits ;
- 606 votants ;
- 36 blancs ;
- 40 nuls ;
- 530 exprimés ;
- 442 voix Parigi ;
- 88 voix Battini.

### 4.2. Battini : socle institutionnel ≠ votes certains

Les cinq grands électeurs institutionnellement rattachés à l'offre Battini ne sont pas traités comme cinq bulletins certains.

La formulation canonique devient :

```text
socle institutionnel identifiable : 5
score observé : 88
écart arithmétique : 83
```

Cet écart démontre que le score dépasse très largement le noyau institutionnel observable. Il ne permet pas d'identifier l'origine individuelle, politique ou territoriale des voix.

### 4.3. Parigi : exposition documentée ≠ origine des 442 voix

De même, le différentiel entre le périmètre documenté de soutien à Parigi et son score final ne permet pas d'attribuer automatiquement les voix supplémentaires aux communes rurales ou à une famille politique donnée.

### 4.4. Hélène Salge / consigne Morganti

La rupture d'Hélène Salge avec Uniti per dumane est documentée, mais la source consultée ne permet pas d'établir que son désaccord concernait spécifiquement la consigne sénatoriale de vote blanc.

Elle ne doit donc pas être retranchée du périmètre **exposé** à cette consigne sur cette seule base.

Le périmètre bastiais documenté comme exposé à la consigne reste à **13 grands électeurs**, sans inférence sur leurs bulletins.

## 5. Borne contrefactuelle : second tour

La principale amélioration analytique du late close est la formalisation d'une borne arithmétique du scénario de second tour.

Les 76 blancs et nuls ne suffisaient pas, à eux seuls, à empêcher l'élection de M. Parigi au premier tour.

En notant :

- `x` = voix observées de Parigi qui ne se seraient plus portées sur lui ;
- `z` = blancs, nuls ou abstentions devenant exprimés ;

la perte de majorité absolue exige :

```text
442 - x <= floor((530 + z) / 2)
```

Les bornes obtenues sont :

| Scénario | Diminution minimale du score Parigi |
|---|---:|
| Aucun non-exprimé converti | 177 |
| 36 blancs convertis | 159 |
| 40 nuls convertis | 157 |
| 76 blancs + nuls convertis | 139 |
| Blancs + nuls + 10 abstentions convertis | 134 |

La candidature supplémentaire aurait donc dû modifier non seulement des blancs/nuls mais aussi une part substantielle des voix effectivement portées sur Parigi.

Cette plage de **134 à 177 voix** n'est pas une prédiction. Elle mesure la magnitude minimale du changement collectif nécessaire pour modifier l'issue du premier tour.

## 6. Règle éditoriale pour le Spécial sénatoriales

Le numéro doit rendre visible la hiérarchie suivante :

```text
FAIT
résultats officiels observés

BORNE
distance arithmétique au second tour

HYPOTHÈSE
une troisième offre aurait pu modifier la répartition

UNKNOWN
amplitude réelle de cette modification

INTERDIT
attribuer rétroactivement des bulletins individuels
```

La prudence ne doit pas effacer l'hypothèse ; l'hypothèse ne doit pas être promue en résultat.

## 7. Usage dans Suicide Corse n°3

Le Magazine peut retenir une formulation courte :

> Les 76 bulletins blancs et nuls observés ne suffisaient pas à eux seuls à provoquer un second tour. Selon la part des non-exprimés qui serait devenue valable, une troisième candidature aurait dû déplacer en outre entre 134 et 177 voix aujourd'hui observées sur Parigi. Cette plage ne prédit pas ce qui se serait passé ; elle mesure la distance minimale qu'une offre supplémentaire aurait dû franchir pour modifier l'issue du premier tour.

Le détail démonstratif reste dans :

`research/senatoriales-2026/investigation/borne_contrefactuelle_offre_troisieme_candidature_2026-09-29.md`

Principe :

> **Le corps principal raconte ; le Magazine actualise ; le Corpus démontre.**

## 8. Freeze gate du mardi

Avant freeze du Spécial sénatoriales :

1. rerendre la projection courante depuis le HEAD réel ;
2. vérifier que le rendu référence bien le 29 septembre et le label « Spécial sénatoriales » ;
3. vérifier que l'analyse 134–177 apparaît dans le Reality Case sans être présentée comme prédiction ;
4. vérifier que les 76 blancs/nuls ne sont nulle part qualifiés comme voix potentielles certaines ;
5. vérifier que Battini 5→88 reste formulé comme écart entre socle observable et score, non comme transfert prouvé ;
6. vérifier que la requête au Conseil constitutionnel reste qualifiée selon son état réel au moment du freeze ;
7. effectuer l'inspection visuelle PDF déjà requise par l'issue #89 ;
8. ne publier/freeze qu'après validation explicite du Principal.

## 9. Statut

```text
28 septembre
= checkpoint pré-freeze historique

29 septembre
= late close actif
= Spécial sénatoriales

freeze
= pas encore acquis par ce document
```

Le report d'un jour est donc lui-même une trace de méthode : **attendre juste assez pour laisser le Réel répondre, mais pas assez pour transformer une publication réactive en chantier indéfini.**
