---
title: "Marie-Louise — registre distribué des témoins potentiels"
status: working-paper
date: 2026-09-17
document_role: research
document_kind: witness-directory-index
visibility: public
lifecycle_state: active
update_policy: UP-DEFAULT-REVIEWED
review:
  status: unreviewed
  reviewed_by: []
---

# Registre distribué des témoins potentiels

## Objet

Ce sous-corpus organise la découverte, la qualification et la sollicitation éventuelle des personnes physiques et morales susceptibles d'apporter des informations, documents, traces ou indications utiles à la compréhension documentée du parcours de Marie-Louise.

Il ne constitue ni une liste de témoins établis, ni une interprétation causale de son parcours ou de sa mort. L'inscription d'une personne signifie seulement qu'il existe une raison documentée de considérer sa sollicitation comme potentiellement utile.

## Architecture

Le registre est volontairement distribué et incrémental. Il ne doit pas être condensé dans un document monolithique.

Il peut contenir :

- des fiches de témoins ou de personnes à identifier ;
- des fiches d'organisations ;
- des études transversales portant sur une période, un lieu ou un réseau ;
- des index dérivés ;
- des liens vers les sources, sollicitations et contributions ;
- des lacunes documentaires du futur Digital Twin de Marie-Louise.

Le document existant `nantes_zad_tournage.md` est une étude transversale de ce type. Il n'a pas vocation à devenir la fiche unique de tous les témoins qu'il mentionne.

## Documents de méthode

- [`METHOD.md`](METHOD.md) : protocole de collecte, qualification, sollicitation et restitution ;
- [`MODEL.md`](MODEL.md) : modèle conceptuel minimal et règles d'évolution.

## Principe agile

Cette structure est stable dans son intention mais non figée dans sa représentation.

Le registre doit pouvoir évoluer sous la pression de l'usage réel. Les champs, catégories et projections peuvent être raffinés, fusionnés ou séparés lorsque l'expérience le justifie. Une base SQL pourra être introduite ultérieurement si les besoins de requête, de déduplication ou de collaboration la rendent utile.

Ne pas concevoir prématurément une ontologie relationnelle définitive. Préserver l'information riche et sa provenance, exposer la plus petite structure utile, puis promouvoir de nouveaux champs ou relations lorsque l'usage crée une pression suffisamment claire.

## Digital Twin

Ce travail contribue à la complétude du futur Cogentia Digital Twin de Marie-Louise en permettant notamment de :

- compléter la chronologie ;
- documenter le graphe relationnel ;
- relier événements, lieux, institutions et œuvres ;
- identifier et réduire des zones `UNKNOWN` ;
- conserver les contradictions sans les écraser ;
- distinguer une source, une assertion et un fait stabilisé.

Chaîne de principe :

```text
témoin potentiel
→ sollicitation
→ témoignage / trace / document
→ qualification épistémique
→ intégration éventuelle au Digital Twin
```

Un témoignage n'est jamais intégré automatiquement comme fait établi.

## Confidentialité

Le dépôt est public. Les coordonnées privées, données sensibles ou informations issues de sources privées ne doivent pas être publiées automatiquement dans ce sous-corpus.

Une fiche publique peut indiquer qu'un moyen de contact existe sans nécessairement le reproduire. Toute réutilisation publique de matière privée doit respecter les règles du Corpus et les intérêts légitimes des tiers.

## Évolution et correction

Le registre suit une discipline d'Optimistic Locking : lire l'état courant, appliquer le plus petit changement suffisant, préserver la provenance, et ne jamais écraser silencieusement un changement concurrent. En cas de divergence, relire, réconcilier, puis produire une correction traçable.

Le but n'est pas de produire un annuaire « terminé », mais un système vivant, vérifiable et améliorable de découverte et de mobilisation de témoins potentiels.
