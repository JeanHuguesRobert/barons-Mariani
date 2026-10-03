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

## Exigences

- chaque affirmation importante doit pouvoir remonter à sa source ;
- conserver les UNKNOWN visibles ;
- distinguer fait, interprétation et qualification ;
- aucune adresse personnelle non destinée à publication ;
- liens stables vers les commits / sources ;
- page lisible sans JavaScript ;
- export machine-readable de la matrice.

## Étape suivante

Un agent de coding peut implémenter le site à partir de ce contrat, en réutilisant les conventions des autres Livres Vivants du dépôt.
