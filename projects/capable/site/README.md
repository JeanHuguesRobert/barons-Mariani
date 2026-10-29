# Capable — contrat de publication

**Adresse de départ retenue le 29 octobre 2026 : https://capable.acorsica.org**.

Ancienne cible `capable.lepp.fr` : référence historique à migrer, non canonique. L'hébergement/délégation DNS et l'effectivité HTTP de la nouvelle adresse restent à vérifier ; la décision éditoriale ne vaut pas déploiement.

Le rattachement à `acorsica.org` marque la continuité des travaux de société civile de C.O.R.S.I.C.A. sur l'autonomie de la Corse (article 72-5) et des contributions transmises à la commission des lois de l'Assemblée nationale. La forme exacte de l'intégration parlementaire doit rester étayée par les pièces sources avant toute affirmation publique plus précise.

Capable est un référentiel ouvert de **doctrine, méthodes et outils d'Autonomie de Capacité**, réutilisable sans adhésion à un parti ou soutien à une candidature. L'activité éditoriale associative et la candidature présidentielle personnelle restent distinctes quant aux responsabilités, moyens et obligations électorales.

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

La contrainte P0 liée au dépôt de la requête au Conseil constitutionnel était une **contrainte historique avant le 7 octobre 2026 à 18 h**. La requête ayant depuis été enregistrée sous le n° **2026-6589 SEN**, cette phrase ne constitue plus une priorité opérationnelle courante.

## Exigences

- chaque affirmation importante doit pouvoir remonter à sa source ;
- conserver les UNKNOWN visibles ;
- distinguer fait, interprétation et qualification ;
- aucune adresse personnelle non destinée à publication ;
- liens stables vers les commits / sources ;
- page lisible sans JavaScript ;
- export machine-readable de la matrice ;
- pour l'Observatoire, ne jamais assimiler contact, intérêt, intention, promesse, envoi et validation officielle.

## État constaté au 28 octobre 2026 — projection ≠ source

La première publication du site est désormais effective. Le point d'entrée `/en-preparation.html` est une **page d'accès** au texte de l'édition de travail, non une édition gelée ni la reproduction intégrale de celle-ci. Le document canonique courant de ce chantier reste `projects/capable/editions/2026-10-09-en-preparation.md`, avec son statut de brouillon et sa date d'observation propre. Les actualités du 26 et du 27 octobre sont documentées dans ce texte et sur la page d'accès, sans mise à jour automatique du Livre durable.

Le Livre (`book.html`, PDF, EPUB) et le n°1 (`n1.html`) ont été promus dans la release du 27 octobre ; les contenus des pages historiques `annexes.html`, `cases.html`, `magazine.html` ont été conservés **sans preuve d'une régénération sémantique récente**. Leur provenance et leur éventuelle convergence demeurent à examiner : ne jamais les remplacer par une projection vide pour obtenir une symétrie de façade.

Le Guide a fait l'objet d'une publication corrective le 28 octobre. Les tests publics de conversation sourcée et de préparation de brouillon sont réussis ; le profil `capable`, le mandat COP et la stratégie `doctrinal_synthesis` ont été validés sur Fracta2. La politique effective de conservation des requêtes et traces demeure non démontrée et son étude est différée, sans garantie de zéro rétention.

## Matrice des prochaines propagations éditoriales

| Élément du Corpus | Destination candidate | Statut et règle |
| --- | --- | --- |
| `projects/capable/editions/2026-10-09-en-preparation.md` | `en-preparation.html` et aperçu HTML versionné | Maintenir un accès traçable au texte courant ; ne pas qualifier d'édition finale |
| `projects/capable/manuscript/` | `book.html`, PDF, EPUB | Texte durable : revue contradictoire des modifications, puis rendu déterministe et contrôle |
| `projects/capable/manuscript/essai-quest-ce-que-la-politique.md` | Livre ou publication autonome | En atelier, non promu ; décision éditoriale explicite nécessaire |
| `projects/capable/research/ccm-quest-ce-que-la-politique.md` | Annexes scientifiques, références | En cours de revue ; ne pas présenter comme annexe validée |
| Archives déjà servies `magazine.html`, `annexes.html`, `cases.html` | Sources canoniques à retrouver | Provenance inconnue à ce stade : préserver, identifier, puis comparer avant régénération |

La prochaine opération de fond est un **différentiel sémantique source-first**, non un déploiement systématique. Pour chaque proposition : source, date de validité, type (fait / interprétation / proposition / inconnu), destination, arbitrage et preuve après publication.

Suivi : [audit différentiel du 27 octobre](freshness-audit-2026-10-27.md) et [Cognitive Packet #152](https://github.com/JeanHuguesRobert/barons-Mariani/issues/152).
