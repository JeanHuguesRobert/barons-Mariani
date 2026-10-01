---
title: "Suicide Corse — conservation de reprise, 1er octobre 2026"
author: "Jean Hugues Noël Robert"
date: "2026-10-01"
status: "conservation-record"
language: fr
license: "CC BY-SA 4.0"
document_role: "source"
document_kind: "conservation-record"
visibility: public
lifecycle_state: active
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: "handler-conservation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: main
  origin_date: "2026-10-01"
  derived_from:
    - projects/suicide-corse/journals/2026-09-30-conservation-affichage-et-reprise.md
    - projects/suicide-corse/manuscript/19-ours.md
    - projects/rise-and-fall/assets/cover/blason.md
review:
  status: "human-directed"
  reviewed_by:
    - "Jean Hugues Noël Robert"
---

# Conservation de reprise — 1er octobre 2026

Cette note remplace, pour l'état des sites publics, la conservation du 30 septembre. Elle n'est pas un PASS de Phase A, ni un gel, ni une source nouvelle sur Marie-Louise.

Avant le commit qui ajoute cette note, `JeanHuguesRobert/barons-Mariani` `main` était `ebaecf09024e5df7d3bc045c25722c801bf49563`.

## Ce qui est déjà dans le corpus

Ces décisions n'ont pas à être réécrites :

- Le numéro 3 est le Spécial sénatoriales du 30 septembre 2026. Le gel n'est pas décidé.
- Le contenu du numéro 3 s'arrête avant le rendez-vous en préfecture du 1er octobre. Le résultat de ce rendez-vous appartient au numéro 4.
- L'association C.O.R.S.I.C.A. produit les outils, incube les initiatives et assume les publications. Jean Hugues Noël Robert en est le président. `institutmariani@gmail.com` est l'adresse publique voulue. C'est écrit dans l'ours du numéro 3.
- Les dates restent séparées : sous-préfecture de Corte en 1811, titre de baron westphalien en 1813.
- Le timbre de la couverture Rise & Fall est un tortil depuis le commit `a05b5b1`. La note est `projects/rise-and-fall/assets/cover/blason.md`. Ce dessin n'a ni heaume ni cimier, et il ne ferme pas un blason historique.
- La reprise du rendu de vérification reste l'issue #91. Il ne faut pas ouvrir un second paquet.

## État public observé le 1er octobre 2026

`https://suicidecorse.baronsmariani.org/` sert `releases/2026-09-30-n3-preview-7d454d1`, commit de publication `7d454d1`. C'est une preview de vérification, non gelée. Le livre est à `/editions/2026-09-30-n3-preview/`. Le chemin gelé `/editions/2026-09-30-n3/` n'est pas servi. Le statut de cette preview dit : Phase A **PARTIAL**, source `9db0774`, moteur Ubikia `361ec32`, 32 chapitres, PDF de 137 pages, pivot 1863–2026 présent dans les trois formats. La couverture composée est sur la page d'accueil et n'est pas la première page du PDF. L'adresse `institutmariani@gmail.com` y figure. La phrase de l'ours qui explique pourquoi elle doit y rester n'est pas encore dans ce rendu.

`https://riseandfall.baronsmariani.org/` sert `releases/2026-09-30-initial`. Les visiteurs y voient encore la couronne. Le tortil est dans le dépôt, pas sur ce site.

La note du 30 septembre et le commentaire de conservation de l'issue #91 daté du 30 septembre à 20:44 UTC disent encore que Suicide Corse sert `f85da3d`. Cette phrase est périmée. Le reçu Operium du même moment l'est aussi.

## Décision d'outil

Le Principal a demandé s'il fallait changer d'outil d'édition. La réponse inscrite ici est non. Le corps du numéro 3 reste rendu par Ubikia et Quarto. Le défaut de couverture est un assemblage après le rendu : placer la couverture composée devant le PDF. Ce n'est pas une raison de changer d'outil.

## Ce qui n'a pas été fait

```text
cette inscription
≠ nouveau rendu du numéro 3
≠ PASS
≠ gel
≠ promotion du tortil sur riseandfall.baronsmariani.org
≠ importation dans le numéro 3 du rendez-vous du 1er octobre
```

## Prochaine campagne

Reprendre l'issue #91. Un nouveau rendu de vérification part du `main` courant, au moins aussi récent que `ebaecf0`, pour que l'ours y soit. Le tortil de Rise & Fall ne fait pas partie de ce livre. Le gel attend la lecture de ce rendu et la phrase explicite du Principal dans l'issue #91.
