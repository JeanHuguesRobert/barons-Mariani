---
title: "Suicide Corse — conservation de reprise, 30 septembre 2026"
author: "Jean Hugues Noël Robert"
date: "2026-09-30"
status: "superseded"
language: fr
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "conservation-record"
visibility: public
lifecycle_state: superseded
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: "handler-conservation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: main
  origin_date: "2026-09-30"
  derived_from:
    - projects/suicide-corse/audits/2026-09-30-special-senatoriales-editorial-date.md
    - projects/suicide-corse/audits/2026-09-30-special-senatoriales-content-close.md
    - projects/suicide-corse/projections/book-n3-working.yml
review:
  status: "human-directed"
  reviewed_by:
    - "Jean Hugues Noël Robert"
---

# Conservation de reprise — 30 septembre 2026

> Au 1er octobre 2026, la phrase qui dit que le site sert `releases/2026-09-30-f85da3d` est fausse. L'état courant est [`2026-10-01-conservation-reprise.md`](2026-10-01-conservation-reprise.md). Le reste de cette note conserve les décisions du 30 septembre.

Cette note conserve ce qu'un handler froid doit savoir lorsque le fil de travail qui l'a produite n'est plus disponible. Elle n'est pas une source nouvelle sur Marie-Louise, ni un gel, ni un PASS de Phase A.

## D'où partions-nous ?

Le 30 septembre au matin, le site public montrait encore une page antérieure au Spécial sénatoriales. Le dépôt de publication et l'arbre réellement servi sont deux objets distincts : un push sur `JeanHuguesRobert/suicide-corse` ne change pas `https://suicidecorse.baronsmariani.org/` tant que la release statique n'a pas été promue.

## Décisions du Principal conservées ici

1. Le numéro 3 est le **Spécial sénatoriales** du **mercredi 30 septembre 2026**. La décision de date est l'audit du même jour. Le gel n'est pas décidé.
2. Ce qui est affiché sur le site public doit être le commit le plus récent du dépôt de publication. Cette préférence vaut pour les mises à jour de la page. Elle ne publie pas à elle seule le livre, et elle n'autorise pas la Phase B.
3. La reprise du rendu de vérification est l'issue **#91**, déjà écrite comme Cognitive Packet. Il ne faut pas ouvrir un second paquet pour la Phase A.

## État au moment de cette inscription

Avant le commit qui ajoute cette note, `JeanHuguesRobert/barons-Mariani` `main` était `12e1141e6351669d2c4b4b84f34d16bce9ff2332`. Ce commit prépare notamment la couverture de vérification du n°3. Il contient aussi le pivot 1863–2026. L'audit de clôture de contenu exige que le prochain rendu parte du `main` courant et inclue `manuscript/07-pivot-rise-and-fall.md`.

Le repère `ddb832b`, nommé dans l'override de l'issue #91 à 09:45 UTC, est antérieur à la consolidation probatoire du 11 septembre, au pivot, et à la couverture. Il n'est pas un commit source à rendre. Les PASS de Phase A antérieurs restent périmés.

Le site public, au même moment, sert la release `releases/2026-09-30-f85da3d`, commit `f85da3db88664c6054ea6aabd6105244a27c2adb`. La page annonce le Spécial sénatoriales du 30 septembre et dit que les rendus HTML, PDF et EPUB du numéro ne sont pas publiés. Cette phrase reste exacte : cette inscription ne les publie pas.

Releases conservées, de la plus récente à la plus ancienne, pour pouvoir revenir en arrière :

- `releases/2026-09-30-f85da3d` — page courante ;
- `releases/2026-09-28-fcb5a71` ;
- `releases/2026-09-28-34c4e87` ;
- `releases/2026-09-26-d8f9992`.

Les reçus opérationnels sont les commentaires de [operium#56](https://github.com/JeanHuguesRobert/operium/issues/56) : [5868989098](https://github.com/JeanHuguesRobert/operium/issues/56#issuecomment-5868989098), [5877781109](https://github.com/JeanHuguesRobert/operium/issues/56#issuecomment-5877781109), [5906912542](https://github.com/JeanHuguesRobert/operium/issues/56#issuecomment-5906912542). Le mécanisme de promotion reste celui d'Operium. Cette note ne le réécrit pas.

## Ce qui n'a pas été fait

```text
inscription de reprise
≠ Phase A
≠ PASS
≠ gel
≠ publication du livre
≠ Phase B
≠ commit source épinglé
```

La Phase A de l'issue #91 autorise un rendu de vérification, son inspection, et des corrections bornées. Elle interdit de geler le numéro et de changer la release publique. Un PASS technique n'ouvre pas la Phase B. Le gel attend une validation explicite du Principal dans l'issue #91.

## Prochaine campagne

Reprendre l'issue #91 et exécuter la Phase A depuis le `main` courant, au moins aussi récent que `12e1141`. Le rendez-vous en préfecture du 1er octobre à 14 h reste hors du numéro 3. Son résultat appartient au numéro 4. La checklist est `research/senatoriales-2026/investigation/consultation-prefecture-2026-10-01-checklist.md`.
