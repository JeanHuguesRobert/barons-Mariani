# capable.lepp.fr — contrat de publication

Domaine cible : **https://capable.lepp.fr**

## MVP

Le premier site doit rendre visibles, sans dépendre d'un backend complexe :

1. l'objet du Livre Vivant ;
2. la Campagne du Réel ;
3. la chronologie ;
4. les acteurs ;
5. la matrice ;
6. les demandes et réponses ;
7. les pièces publiques ;
8. le protocole de contribution ;
9. un historique des corrections.

## Source-first

Le site est une projection du Corpus. Il ne devient pas la source canonique des faits.

## Pages minimales

- `/` — manifeste et état courant ;
- `/campagne/` — vue d'ensemble ;
- `/matrice/` — matrice filtrable ;
- `/acteurs/` — acteurs, rôles, états ;
- `/chronologie/` — événements ;
- `/contribuer/` — corrections / objections / contributions ;
- `/sources/` — index des pièces publiques ;
- `/methodologie/` — Réel, résolution, statuts probatoires.

## Surfaces réservées pour la présidentielle 2027

Deux surfaces sont désormais prévues sans obligation d'implémentation avant le dépôt de la requête au Conseil constitutionnel :

- `/marche/` — Marche du Soleil, étapes, traces et Journaux du Soleil ;
- `/presentations/` — Observatoire des Présentations 2027, proclamations sourcées, états normalisés et rapprochement officiel.

Sources :

- `projects/capable/campaign/marche-du-soleil.md`
- `projects/capable/campaign/observatoire-presentations-2027.md`

Avant le 7 octobre 2026 à 18 h, leur implémentation technique reste subordonnée au P0 procédural.

## Exigences

- chaque affirmation importante doit pouvoir remonter à sa source ;
- conserver les UNKNOWN visibles ;
- distinguer fait, interprétation et qualification ;
- aucune adresse personnelle non destinée à publication ;
- liens stables vers les commits / sources ;
- page lisible sans JavaScript ;
- export machine-readable de la matrice ;
- pour l'Observatoire, ne jamais assimiler contact, intérêt, intention, promesse, envoi et validation officielle.

## Étape suivante

Un agent de coding peut implémenter le site à partir de ce contrat, en réutilisant les conventions des autres Livres Vivants du dépôt.

Cette implémentation ne constitue pas une priorité supérieure à la sécurisation du dépôt de la requête au Conseil constitutionnel.
