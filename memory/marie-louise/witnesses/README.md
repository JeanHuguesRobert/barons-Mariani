---
title: "Marie-Louise — registre distribué des témoins potentiels"
author: Jean Hugues Noël Robert
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
license: CC BY-SA 4.0
language: fr
status: working-paper
date: 2026-09-18
document_role: index
document_kind: witness-directory-index
visibility: public
provenance:
  origin_type: unknown
  origin_repository: unknown
  origin_ref: unknown
  origin_date: unknown
  derived_from: []
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

Études transversales actuellement disponibles :

- [`campaign-01.md`](campaign-01.md) : première campagne de sollicitation, organisée par vagues et Knowledge Gaps ;
- [`nantes_zad_tournage.md`](nantes_zad_tournage.md) : Nantes, ZAD et tournage ;
- [`research-2009-2016.md`](research-2009-2016.md) : recherche documentaire et témoins de l'adolescence jusqu'à l'entrée en CPES.

Ces études n'ont pas vocation à devenir des fiches uniques de toutes les personnes qu'elles mentionnent.

## Documents de méthode

- [`METHOD.md`](METHOD.md) : protocole de collecte, qualification, sollicitation et restitution ;
- [`MODEL.md`](MODEL.md) : modèle conceptuel minimal et règles d'évolution.

## Principe agile

Cette structure est stable dans son intention mais non figée dans sa représentation.

Le registre doit pouvoir évoluer sous la pression de l'usage réel. Les champs, catégories et projections peuvent être raffinés, fusionnés ou séparés lorsque l'expérience le justifie. Une base SQL pourra être introduite ultérieurement si les besoins de requête, de déduplication ou de collaboration la rendent utile.

Ne pas concevoir prématurément une ontologie relationnelle définitive. Préserver l'information riche et sa provenance, exposer la plus petite structure utile, puis promouvoir de nouveaux champs ou relations lorsque l'usage crée une pression suffisamment claire.

## Chronologie documentaire

Le travail sur les témoins alimente directement la chronologie documentaire de Marie-Louise, sans créer une chronologie canonique concurrente.

Références principales :

- [`../carte.md`](../carte.md) : synthèse générale, chronologie, traces et inconnues ;
- [`../formation/parcours_artistique_2016_2022.md`](../formation/parcours_artistique_2016_2022.md) : reconstruction sourcée du parcours de formation et de création entre 2016 et 2022 ;
- [`research-2009-2016.md`](research-2009-2016.md) : couche de recherche détaillée pour la période antérieure.

Principe de circulation :

```text
trace datée
→ événement chronologique
→ témoin / organisation / piste
→ KnowledgeGap
→ recherche ou sollicitation
→ contribution
→ qualification épistémique
→ chronologie éventuellement précisée
```

La date à laquelle une source est retrouvée ou transmise ne doit pas être confondue avec la date de l'événement qu'elle documente. Une source postérieure au décès peut documenter une relation, un événement ou une période antérieurs.

Les résultats négatifs bornés font aussi partie de la chronologie de l'enquête : ils indiquent qu'une recherche déterminée, dans une source et un périmètre donnés, n'a pas permis de résoudre une lacune, sans transformer cette absence de résultat en absence de fait ou de relation.

## Projections éditoriales — Suicide Corse

Le registre et la chronologie documentaire doivent pouvoir alimenter deux chapitres publics de *Suicide Corse* :

- **Chronologie** — vue lisible et sourcée des événements, périodes, transitions, contradictions et zones `UNKNOWN` ;
- **Annuaire** — vue lisible des témoins potentiels, personnes à identifier, organisations, relais et détenteurs de traces.

Ces chapitres sont des **projections dérivées**. Ils ne doivent pas devenir des sources concurrentes du Corpus. Toute information publiée doit rester reliée à sa provenance et respecter les règles de confidentialité.

Le chapitre « Annuaire » ne doit pas publier automatiquement les coordonnées privées connues. Le chapitre « Chronologie » doit distinguer clairement fait stabilisé, trace, témoignage, hypothèse et résultat négatif borné.

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
