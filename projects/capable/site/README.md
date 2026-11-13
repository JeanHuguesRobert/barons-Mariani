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

## Publication canonique automatisable — 13 novembre 2026

**Objet :** faire apparaître dans `https://capable.acorsica.org/` la dernière projection publique **« en préparation »**, sans écraser les fichiers durables `book.*` ni les éditions datées. L'accueil et `en-preparation.html` doivent conduire à `candidate.html` ; la release expose également `candidate.pdf`, `candidate.epub`, `candidate-manifest.json`, `candidate-formats.json` et `candidate-deploy.json`.

**Implémentation sur main :** [déployeur atomique](../../../scripts/ops/deploy-capable-working.py), [déclencheur SSH fixe](../../../scripts/ops/capable-deploy-trigger.sh), [test non privilégié](../../../scripts/ops/check-deploy-capable-working.py) et job `deploy-capable-canonical` du [workflow existant](../../../.github/workflows/living-books-news-previews.yml). Le déployeur lit les *blobs Git immuables* d'`origin/main`, vérifie les 23 sources et les empreintes PDF/EPUB, copie la release courante dans une nouvelle release nommée par son contenu, conserve le Livre durable et bascule atomiquement le lien `current`. Une reprise identique n'ajoute aucune release. Le contrôle d'acceptation vérifie ensuite publiquement HTTPS, les fichiers et le reçu.

**Préparation administrative unique (nécessaire avant activation du job) :** installer le déployeur et son déclencheur comme programmes **appartenant à root, non modifiables par le compte de déploiement**, configurer un droit `sudo` limité à l'exécutable de déploiement validé, et une clé SSH dédiée dont l'entrée `authorized_keys` utilise `restrict,command="/usr/local/sbin/capable-deploy-trigger"`. Ne pas transmettre une clé SSH générale ou réutiliser le compte personnel dans les secrets de CI. Il revient au propriétaire de Fracta2 d'autoriser et d'effectuer ce provisionnement administratif ; la simple présence d'un runner n'y donne pas droit.

**Paramètres GitHub Actions du même dépôt :**
- Variables : `CAPABLE_CANONICAL_AUTODEPLOY=true`, `CAPABLE_DEPLOY_HOST` (hôte Fracta2), `CAPABLE_DEPLOY_USER` (compte ayant la clé restreinte).
- Secrets : `CAPABLE_DEPLOY_SSH_PRIVATE_KEY` (clé dédiée), `CAPABLE_DEPLOY_SSH_KNOWN_HOSTS` (empreinte SSH vérifiée indépendamment, pas une capture non authentifiée).
- Tant que le booléen n'est pas activé, le job canonique est **désactivé sans bloquer GitHub Pages**, tandis que le test d'atomicité est intégré à la CI. Ne jamais afficher « déployé sur le site canonique » avant que les reçus distants et HTTP soient conformes.

**Vérification et continuité :** [issue Capable #158](https://github.com/JeanHuguesRobert/barons-Mariani/issues/158) pour l'activation sur Fracta2 ; [#112](https://github.com/JeanHuguesRobert/barons-Mariani/issues/112) pour la Factory ; [#152](https://github.com/JeanHuguesRobert/barons-Mariani/issues/152) pour la sélection éditoriale. La publication GitHub Pages fonctionne indépendamment de l'activation sur Fracta2.

## Candidate de travail publique — 13 novembre 2026

Les 23 sources du [n°1 en préparation](../editions/2026-10-28-projection-candidate-n1.md), comprenant la [proposition nationale de révision constitutionnelle de l'article 72](../doctrine/revision_constitutionnelle_article_72.md), sont assemblées en [HTML](../../../previews/en-preparation/capable.html), [PDF](../../../previews/en-preparation/capable.pdf) et [EPUB](../../../previews/en-preparation/capable.epub), avec [reçus et empreintes](../../../previews/en-preparation/capable-formats.json).

**La prévisualisation HTML est déjà consultable en ligne** sur [GitHub Pages](https://jeanhuguesrobert.github.io/barons-Mariani/previews/en-preparation/capable.html), avec PDF et EPUB téléchargeables depuis le dépôt. Leur exposition directe sous `/candidate.html`, `/candidate.pdf` et `/candidate.epub` sur le site Fracta2 reste un déploiement distinct ; l'ancien `/book.html` n'héberge pas encore cette candidate.

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

## Hébergement mutualisé Fracta2 — décision du 29 octobre 2026

**Choix de plateforme :** héberger le site associé au Livre Vivant Capable sur **Fracta2**, en réutilisant la chaîne d'hébergement prévue pour `jhn.baronsmariani.org`, plutôt que de dépendre de Netlify. Conserver l'URL éditoriale canonique **`https://capable.acorsica.org`** ; mutualiser le socle d'exploitation, **pas** les identités publiques, mandats, données ou secrets.

**Réutilisation recherchée :** même reverse proxy / terminaison TLS, administration des domaines, supervision, mécanisme de build et de déploiement, sauvegarde et retour arrière ; un hôte virtuel / routage propre à Capable et un répertoire d'artefacts distinct. Le contenu statique (Livre, Magazine, annexes, éditions) ne doit pas attendre l'achèvement des services dynamiques JHN. Les éventuels services conversationnels/API sont isolés et raccordés seulement après vérification des mandats et des protections.

**Recette nécessaire avant mise en service :** inventorier les services et ports déjà employés par JHN sur Fracta2, contrôler le Caddyfile réel et les droits d'accès ; choisir le répertoire de publication et les permissions ; valider DNS, certificat, réponse HTTP, liens, empreinte du manifeste et publication `en-preparation` ; tester rollback et absence de régression pour JHN. Corriger les anciennes URL `capable.lepp.fr` et les balises canonical, mais ne pas supposer que le DNS ou le déploiement sont déjà effectifs.

**Coordination :** publication des Livres Vivants dans `barons-Mariani#112` ; évolution de l'identité JHN dans `inseme#33` et migration de LePP dans `inseme#59`. Ne pas créer un second moteur de publication ni intervenir sur la production sans contrôle du socle partagé.
