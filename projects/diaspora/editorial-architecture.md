---
title: "DIASPORA — architecture éditoriale"
author: unknown
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
date: "2026-09-30"
last_modified_at: "2026-10-06"
status: "working-paper"
language: "fr"
document_role: "editorial-architecture"
document_kind: "working-note"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/diaspora/editorial-architecture.md"
review:
  status: "unreviewed"
  reviewed_by: []
ai_assisted_by:
  - "Grok 4.7 (xAI), handler froid de l'issue GitHub 96"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "https://github.com/JeanHuguesRobert/barons-Mariani/issues/96"
  origin_date: "2026-09-30"
  derived_from:
    - "projects/suicide-corse/editorial-architecture.md"
    - "projects/rise-and-fall/editorial-architecture.md"
---

# DIASPORA — architecture éditoriale

DIASPORA réemploie les invariants déjà tenus par *Suicide Corse* et *Rise & Fall*. Il n'en réécrit pas le moteur.

```text
traces et contributions
→ qualification
→ corpus vivant
→ projection
→ revue
→ gel
→ édition immuable
→ réponse du réel
→ traces nouvelles
```

Règle héritée : **geler l'édition, jamais la projection suivante.**

Au 30 septembre 2026, aucune édition DIASPORA n'est gelée. `editions/index.md` le dit. Le site dans `web/` est une projection de travail.

## Grammaire commune : trois Machines, Révélateur / Stabilisateur

DIASPORA reprend aussi la couche doctrinale commune des Livres Vivants définie dans [Livre Vivant](../../research/livre_vivant.md).

~~~text
Machine à Empêcher
→ Machine à Explorer
→ Machine à Rendre Capable

Révélateur ↔ Stabilisateur
~~~

Ici, la lecture candidate est :

- **Machine à Empêcher** : invisibilité des capacités, fragmentation des réseaux, asymétries d'information, absence de chemin entre besoin et aide disponible ;
- **Machine à Explorer** : annuaire, graphes de capacités, recherche, matching explicable, appels à contribution ;
- **Machine à Rendre Capable** : mise en relation effective permettant à une personne, un projet ou une communauté d'accéder à une ressource ou compétence utilisable ;
- **Révélateur** : rendre visibles les capacités dispersées, besoins non satisfaits, liens manquants et erreurs du graphe ;
- **Stabilisateur** : préserver provenance, consentement, corrections, liens vérifiés, états du corpus et mécanismes reproductibles de mise en relation.

> **Pas de Révélateur sans perspective de stabilisation ; pas de Stabilisateur sans capacité de révéler ses propres échecs.**

Un annuaire figé et opaque pourrait devenir lui-même Machine à Empêcher ; un graphe vivant doit donc pouvoir signaler ses données périmées, ses faux positifs et ses capacités devenues inaccessibles.

## Triptyque

> Le corps principal raconte. Le magazine actualise. Les annexes démontrent.

| Partie | Rôle | Entrée |
| --- | --- | --- |
| Livre | synthèse durable | `manuscript/00-ouverture.md`, `manuscript/01-la-corse-furtive.md`, `web/book.html` |
| Magazine | écarts, essais, initiatives en cours | `magazine/` |
| Annexes | modèle, sources, mesures, revue, méthode | `annexes/`, `journals/`, `data/` |

L'annuaire n'est pas le livre. C'est une projection outillée du corpus. Une fiche publiée reste une trace sourcée, pas un jugement sur une personne.

### Reality Case — registre local et projection d'annuaire

DIASPORA constitue un Reality Case du pattern générique **registre local → projection d'annuaire** désormais explicité dans le *Living Book Factory*.

Son `data/seed.json` reste une implémentation locale souveraine. Il n'a pas à être refactoré pour satisfaire une abstraction commune tant qu'aucune friction réelle ne le justifie.

Règle d'Occam :

~~~text
implémentation locale suffisante
→ ne pas ajouter de couche

friction répétée et démontrée
→ extraire seulement le plus petit mécanisme commun utile
~~~

L'annuaire, la carte, la recherche et les autres surfaces restent des projections : elles ne deviennent pas une nouvelle source d'autorité sur les entrées.

Le chantier **« Corse furtive »** étend le rôle du Révélateur : non seulement rendre visibles des personnes ou capacités dispersées, mais aussi détecter des **structures collectives invisibles à l'échelle des trajectoires individuelles**. La règle probatoire reste inchangée : proxy ≠ preuve individuelle ; surreprésentation ≠ coordination ; toute mesure doit expliciter son dénominateur.

## Asymétrie

Le contenu nouveau peut ajouter, préciser, corriger ou retirer, avec une provenance. La forme de la projection peut changer sans reprendre l'historique des formes. Le premier site statique n'oblige pas les suivants.

## Statuts à ne pas confondre

```text
dépôt ≠ validation ≠ publication
énoncé public ≠ service constaté
lien corse sourcé ≠ origine inférée
cadre institutionnel déclaré ≠ statut relu
```

## Suna

Le corps du livre garde la déclaration du Principal et l'absence de source primaire. Cette absence est une continuation, pas un trou à remplir par conjecture.
