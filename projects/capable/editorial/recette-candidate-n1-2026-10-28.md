---
title: "Capable — recette documentaire de la projection candidate n°1"
date: "2026-10-28"
status: "working-qa — non gelé"
document_role: derived
document_kind: editorial-quality-review
visibility: public
lifecycle_state: working
language: fr
---
# Recette documentaire — premier numéro candidat Capable

**Objet :** contrôler une projection éditoriale en préparation, sans prétendre réaliser un contrôle de publication HTML/PDF ni décider du gel.

## Périmètre observé

- **Livre : 11 chapitres** listés dans le [sommaire](../manuscript/README.md), relus et enrichis lors des passes précédentes.
- **Magazine : 6 chroniques rédigées** : [autonomie](../magazine/2026-10-28-autonomie-corse.md), [Campagne du Réel](../magazine/2026-10-28-campagne-du-reel-et-presentations.md), [énergie et mobilité](../magazine/2026-10-28-energie-et-capacites-territoriales.md), [genèse](../magazine/2026-10-28-genese-capable.md), [procédures et effectivité](../magazine/2026-10-28-procedures-et-effectivite.md). Une [rétrospective narrative](../magazine/2026-10-28-retrospective-notes-de-campagne.md) complète désormais [l'inventaire de provenance](inventaire-notes-campagne-2026-10-28.md), distinct du texte de publication.
- **Annexes : 8 dossiers**, répartis entre [A1–A4](../annexes/2026-10-28-dossiers-a1-a4.md) et [A5–A8](../annexes/2026-10-28-dossiers-a5-a8.md).
- **Assemblage** : [projection candidate](../editions/2026-10-28-projection-candidate-n1.md) ; journal antérieur de l'[édition ouverte](../editions/2026-10-09-en-preparation.md).

## Contrôles réalisés

| Contrôle | Résultat | Précision |
| --- | --- | --- |
| Existence des 5 fichiers de chroniques | PASS | Lecture directe GitHub des cinq chemins |
| Existence des 2 fichiers regroupant A1–A8 | PASS | Lecture directe GitHub |
| Principales sources du Magazine et des Annexes | PASS ciblé | Existence vérifiée pour doctrine du Livre Vivant, index, effectivité, Note du 27 octobre, veille sénatoriale, matrice, Marche du Soleil, observatoire et inventaire |
| Couverture du sommaire Magazine | FIXED | Les volets genèse et procédures étaient encore qualifiés de rubriques à rédiger ; correction effectuée dans la candidate, commit `7f47fb4` |
| Conformité Livre / Magazine / Annexes | PASS de structure | Corps durable, chroniques datées, dossiers probatoires séparés |
| Vérité des assertions, sources primaires externes | NOT TESTED intégralement | Le contrôle d'existence n'est pas une vérification au fond |
| Tous liens relatifs et liens externes | PARTIAL | Les principales dépendances ont été résolues ; pas de contrôle automatique exhaustif de chaque lien dans tous les textes |
| Rendu public HTML/PDF, navigation réelle, responsive | NOT TESTED | Aucun nouveau rendu créé ni déployé |
| Autorisation et empreinte de gel | NOT APPLICABLE | Numéro en préparation, non gelé |

## Défauts et dettes prioritaires

**P1 — Magazine : densité et statut de la rétrospective — PARTIELLEMENT RÉSOLU le 28 octobre.** Une [chronique narrative de synthèse](../magazine/2026-10-28-retrospective-notes-de-campagne.md) existe désormais aux côtés de l'inventaire et des six Notes. Elle conserve leurs attributions et inconnues. La revue de fidélité source par source reste à approfondir avant gel.

**P1 — Vérifiabilité : pièces primaires.** Les Annexes A4 et A8 restent dépendantes des documents sources et de calculs non revus ; compléter les références officielles des amendements, les hypothèses économiques et les objections.

**P1 — Edition HTML.** La candidate demeure une page Markdown de navigation. Rien dans cette recette ne démontre que les projections servies par le site reprennent les modifications récentes. Avant annonce de mise à jour publique, générer et vérifier la projection et conserver le reçu technique.

**P2 — Cohérence des statuts.** Ne pas confondre annonce publique de Capable, lancement d'une campagne, événements projetés et actes réalisés ; ne pas déduire une publication gelée des anciens noms de fichiers ou des anciennes pages.

**P2 — Lecture narrative.** Les onze chapitres constituent un livre bref et dense. Le Magazine apporte des exemples concrets, mais les transitions entre les deux faces gagneraient à être lues dans un rendu complet. La place finale du chapitre présidentiel et de l'essai philosophique reste un choix d'auteur.

**P2 — Liens et provenance.** Auditer automatiquement tous les liens Markdown de chaque fichier, y compris les références externes, et identifier les chemins historiques devenus des redirections. La preuve d'un chemin GitHub accessible n'établit pas la validité de ses liens sortants.

## Critères d'une candidate prévisualisable

Une **prévisualisation non gelée** peut être préparée à partir de ce contenu lorsque l'assemblage est cohérent et sa traçabilité explicite ; les inconnues peuvent figurer comme telles. En revanche, aucune affirmation de numéro achevé ou gelé ne doit précéder les contrôles : qualité du rendu, présence des trois ensembles, accès aux sources, absence de rupture de navigation, versions et date d'observation.

**Décision de cette recette :** progression éditoriale attestée ; contrôle documentaire ciblé concluant ; **recette complète non acquise**. Ni gel ni publication effectués.
