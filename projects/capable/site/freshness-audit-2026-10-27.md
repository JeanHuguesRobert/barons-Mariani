---
title: "Capable — audit différentiel de fraîcheur des projections"
date: "2026-10-27"
version: "0.1"
status: "working-audit"
document_role: derived
document_kind: reality-test-report
visibility: public
lifecycle_state: working
language: fr
license: CC BY-SA 4.0
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/capable/site/freshness-audit-2026-10-27.md"
source_documents:
  - "projects/capable/README.md"
  - "projects/capable/manuscript/README.md"
  - "projects/capable/editions/2026-10-09-en-preparation.md"
  - "projects/capable/site/README.md"
related_documents:
  - "https://github.com/JeanHuguesRobert/barons-Mariani/issues/152"
  - "https://github.com/JeanHuguesRobert/cogentia/issues/274"
  - "https://github.com/JeanHuguesRobert/ubikia/issues/41"
---

# Capable — matrice de fraîcheur et de propagation

**Date du constat :** 27 octobre 2026. **Nature :** audit différentiel, non édition gelée. Les preuves de la release sont les sorties SSH communiquées par l'exploitant ; l'état GitHub est issu de lectures des fichiers de `main`. La fraîcheur *sémantique* n'est pas automatiquement déduite de la date d'un fichier.

## Preuves opérationnelles

- Release historique sur Fracta2 : `/srv/www/capable/releases/2026-10-05-working`.
- Release promue et active : `/srv/www/capable/releases/2026-10-27-candidate-01`.
- La candidate a été obtenue par **copie de la release historique**, puis **remplacement de `index.html` et ajout de `en-preparation.html` seulement**.
- Vérifications locales : 200 pour `/`, `/en-preparation.html`, `/annexes.html`, `/cases.html`, `/magazine.html` ; l'exploitant confirme aussi l'accès externe au nouveau numéro.
- Comparaison `diff -qr` ancienne/nouvelle : seul `index.html` diffère et `en-preparation.html` est nouveau.
- Le fichier `book.html` public garde l'empreinte SHA-256 historique `df7cd708e3a4ab4e7916e108b0f06b2e0fff62270b9599d8349210331724df92` dans les deux releases.
- **Ne pas confondre** `HTTP 200` et contenu à jour, ni `source présente sur main` et fichier effectivement déployé.

## Matrice des surfaces

| Surface | Release active (preuve) | Projection source actuelle | Source éditoriale / situation | Écart et action bornée |
|---|---|---|---|---|
| `/` | **Actualisée** à partir du site GitHub le 27/10, HTTP 200 local | `site/index.html` SHA `0812da1` | Index Capable et doctrine générale ; rubrique numéro en préparation ajoutée | Technique résolu ; contrôle transversal des intitulés (« cinq faces ») et cohérence avec doctrine encore à faire |
| `/en-preparation.html` | **Nouvelle** page, HTTP 200 local et accessible selon l'auteur | `site/en-preparation.html` SHA `ea4e147` | `editions/2026-10-09-en-preparation.md` : `source_as_of: 2026-10-09`, malgré mentions d'événements postérieurs | **Dette éditoriale prouvée** : dater distinctement jalon d'ouverture, dernière actualisation des sources et couverture réelle ; actualiser l'édition sans la geler |
| `/book.html` | **Historique** identique au 05/10 (SHA-256 cité ci-dessus) | `site/book.html` SHA `1a4d402`, différent du HTML historique d'après la comparaison précédente | `manuscript/README.md`, 11 chapitres ; document source durable et dérivé | **Dette de projection** : comparer le rendu courant aux chapitres ; liens historiques cassés à réparer dans la chaîne de génération, pas par bricolage du déploiement |
| `/book.pdf`, `/book.epub` | **Historiques**, inchangés par promotion du 27/10 | `site/book.pdf`, `site/book.epub` existent, et avaient des différences constatées au premier `diff -qr` | Manuscrit Livre, artefacts dérivés | **Dette de projection** : valider le build, les empreintes et la cohérence du couple HTML/PDF/EPUB avant promotion conjointe |
| `/n1.html` | **Historique** inchangé par la dernière promotion | `site/n1.html` SHA `3ee0425`, différait de la release historique | Numéro 1 = projection datée de lancement, **à ne pas confondre** avec l'édition de travail ni réécrire silencieusement | **Décision éditoriale préalable** : vérifier si la version source est une correction admissible du n°1 ou un changement à porter au numéro en préparation |
| `/guide.html`, `/guide.js` | **Historiques** (différences avec la source GitHub constatées) | SHA `4a72734` et `802a83f` | Guide public et profil distant Cogentia | **Dette fonctionnelle** : audit des flux de données, des promesses de confidentialité et compatibilité du backend avant substitution |
| `/sources.html` | Historiquement inchangé le 27/10 | `site/sources.html` SHA `9ff21d9` | Documents sources / index, références remontant notamment à octobre 2026 | **Fraîcheur indéterminée** : mesurer la couverture réelle des nouvelles sources et corrections, ne pas inférer du seul nom de fichier |
| `/annexes.html`, `/cases.html`, `/magazine.html` | Conservées par promotion, HTTP 200 local | **Absentes** du répertoire `site/` lors du diff source/release de l'exploitant | Anciennes surfaces éditoriales toujours publiées ; annexes, cas, Magazine | **Risque d'orphelins** : récupérer et inventorier leur contenu ; choisir réintégration source ou redirection explicite avant de retirer un fichier |
| `/matrix.html`, `/acteurs.html`, `/chronologie.html`, `/contribuer.html` | Restées historiques le 27/10 | Fichiers source présents dans le répertoire du site, selon inventaire SSH | Matrice et campagnes documentaires | **À évaluer**, aucune preuve suffisante d'obsolescence sémantique ligne à ligne ; inventaire des dépendances requis |
| `/robots.txt`, `/sitemap.xml`, `/llms.txt` | Restés historiques le 27/10 | Fichiers source présents | Découvrabilité et crawl | Tester présence de `en-preparation.html`, URLs canoniques et dates de modification ; **non vérifié** |

## Anomalies de liens héritées

La recette différentielle a détecté dans l'ancien `book.html` six liens locaux non résolus : `../site/styles.css`, `preview.pdf`, `preview.epub`, `../site/index.html`, `../campaign/observatoire-presentations-2027.md`, `../campaign/marche-du-soleil.md`. Le même contenu ancien a été conservé par la release du 27/10 ; ce ne sont **pas** des régressions de cette promotion. Les versions de source GitHub `site/book.html` utilisent déjà certains chemins différents ; ne pas appliquer aveuglément les correctifs anciens à la nouvelle source.

## Plan d'action incrémental

1. **P0 — Non-régression documentaire :** prendre un inventaire et des empreintes de la release active, archiver la liste des ressources publiées et leurs réponses HTTP ; conserver la release du 05/10 et celle du 27/10.
2. **P0 — Fraîcheur sémantique :** comparer édition « en préparation », chronologie et index des sources avec l'état courant du Corpus ; expliciter les nouveautés depuis le 09/10 sans transformer l'édition en numéro gelé.
3. **P1 — Livre :** vérifier les chapitres puis produire un ensemble cohérent HTML/PDF/EPUB ; recette de liens et reçus de rendu.
4. **P1 — Pages orphelines :** intégrer `annexes/cases/magazine` à la source du site, ou établir des remplacements explicites sans perte sémantique ; ne jamais les effacer par synchronisation destructive.
5. **P1 — Guide :** comparer précisément JS/HTML, tracer données envoyées et exigences de confidentialité avant promotion.
6. **P2 — Contractualisation Factory → Operium :** plan d'impact source → pages, candidate déterministe, diff ancien/nouveau, vérification des liens **avec baseline de défauts connus**, approbation de promotion, rollback atomique, vérification HTTP publique, reçu immuable.

## Gates

Un fichier récent n'est pas nécessairement une édition récente. Une édition datée n'est pas obsolète parce qu'elle est historique. Une page publique n'est pas à jour parce qu'elle répond 200. Aucune publication/déploiement n'est autorisé par ce document seul. La prochaine tranche est **un inventaire différentiel mesuré**, pas une copie globale de `site/` sur la production.


## Addendum de vérification sémantique — 28 octobre 2026

**Méthode.** Comparaison ponctuelle des contenus de `main` (édition de travail, Corps rendu, accueil, page « En préparation », index de manuscrit, carte doctrinale, doctrine canonique de Livre Vivant et CCM) ; confrontation avec le reçu de publication [#153](https://github.com/JeanHuguesRobert/barons-Mariani/issues/153). Ce contrôle n'est **pas** une revue exhaustive des sources et ne prouve pas l'actualité en temps réel du monde extérieur. La recherche globale Cogentia par index n'a retourné aucun document pour trois requêtes multi-termes (repli sur recherche lexicale) ; la vérification s'appuie donc sur la lecture directe de fichiers GitHub versionnés.

### Réconciliation de publication
Le relevé initial ci-dessus décrit **candidate-01**, et reste exact *pour le moment de cet audit historique*. Depuis, [#153](https://github.com/JeanHuguesRobert/barons-Mariani/issues/153#issuecomment-6456192740) atteste `candidate-02` avec `book.html`, `book.pdf`, `book.epub` et `n1.html`, liens canoniques et conservation binaire des trois pages historiques. Ne plus traiter la régénération de ces quatre fichiers comme tâche ouverte sans nouvel écart démontré.

### Écarts et décisions bornées

| Objet | Constats directs sur `main` | Qualification | Suite |
| --- | --- | --- | --- |
| Numéro en préparation | `source_as_of: 2026-10-27`, `last_modified_at: 2026-10-27` ; contient résultat du vote du Sénat du 26/10, absence d'entrée en vigueur 72-5, analyse explicitement attribuée et distinction fait/analyse/proposition | **PASS limité** : source éditoriale consolidée au 27/10 ; publication intégrale de cette consolidation sur le site non démontrée par la seule page `en-preparation.html` | Comparer page publique et édition complète ; conserver la profondeur historique et les dates |
| Corps | `book.html` reprend subsidiarité, Révélateur, Stabilisateur, démocratie directe et l'essai candidat comme référence ; aucun jalon textuel « 27 octobre » dans le Livre rendu | **Non-régression**, pas forcément lacune : les faits datés appartiennent d'abord au Magazine. **UNKNOWN** : propagation de changements doctrinaux récents au Corps | Revue sémantique chapitre ↔ sources canoniques, sans insérer automatiquement l'actualité dans le Corps |
| Magazine | `projects/capable/site/magazine.html` absent de `main`, fichier historique toujours servi selon #153 | **DETTE PROUVÉE** : contenu publié non traçable depuis cette source Git | Inventorier contenu, provenance et mécanisme de régénération avant toute réécriture ou retrait |
| Annexes et cas | `site/annexes.html` et `site/cases.html` également absents de `main` mais préservés sur la release | **DETTE PROUVÉE** : surfaces orphelines | Retrouver les sources et indexer les références savantes / Reality Cases |
| Guide | `guide.html` existe sur `main` avec avertissements éditoriaux déjà corrigés au 26/10 ; la release #153 n'a remplacé ni `guide.html` ni `guide.js` | **UNKNOWN / risque de décalage** : promesses actuellement déployées, service, rétention et réponses non testés dans cette passe | Reality Test spécifique sur le Guide et son backend, sans inférer absence de transmission |
| Essai candidat | `manuscript/README.md` indique explicitement *Qu'est-ce que la politique ?* comme atelier non inséré ; CCM v0.2 encore non validé | **PASS de statut**, **travail de fond ouvert** | Revue contradictoire et décision éditoriale séparée |
| Index de lecture | L'accueil a une mention d'actualité du 27/10 ; l'index du manuscrit date du 03/10 mais distingue le Livre durable des éditions datées | **Dates non comparables sans analyse** | Ne pas qualifier d'obsolète sur sa date seule |

### Décision
La publication technique est **PASS**, mais la conformité sémantique globale à l'état actuel du Corpus est **PARTIAL / NON DÉMONTRÉE**. Priorités : (1) vérifier la couverture de l'édition datée sur la page publique, (2) récupérer provenance/contenu des trois pages orphelines, (3) contrôler le Guide servi, (4) revue source-first du Corps sur un échantillon d'affirmations et documents nouveaux. Éviter toute régénération générale ou nouvelle release avant d'avoir mesuré les écarts.


## Vérification des pages historiques — 28 octobre 2026

**Résultat du contrôle du dépôt courant :** les chemins `projects/capable/site/magazine.html`, `projects/capable/site/annexes.html` et `projects/capable/site/cases.html` retournent tous **404** à la lecture du dépôt GitHub `barons-Mariani/main`. Cette absence au chemin attendu ne démontre pas l'absence de documents sources ailleurs dans le Corpus, ni l'origine du HTML conservé sur le serveur.

L'audit opérationnel antérieur avait confirmé que ces trois pages sont **présentes dans la release active** et que leurs empreintes demeuraient inchangées lors de la publication du Livre. Aucun des trois fichiers historiques n'a été récupéré ou inspecté dans cette passe ; **le contenu et la provenance restent UNKNOWN**. Une recherche de code sur leurs noms renvoie des pages homonymes d'autres Livres Vivants (Commons, PrivAI, etc.), sans établir une filiation Capable. Il serait erroné de les copier ou de les réinterpréter comme sources de Capable.

**Prochaine preuve minimale sur Fracta2 :** relever pour chaque fichier de la release active (1) taille et SHA256, (2) `<title>` et `<link rel="canonical">`, (3) titres `h1`/`h2`, (4) liens de provenance éventuels et (5) date des métadonnées. Ne produire aucune modification de publication avant ce relevé ; conserver les contenus et les liens existants. Une fois ces éléments obtenus, rechercher leurs sources documentaires dans les autres chemins du Corpus et dans les historiques Git pertinents, puis dresser un tableau affirmation → source → état.

**Décision de cette passe :** provenance non résolue, conservation maintenue, aucune promotion éditoriale ni qualification de fraîcheur fondée sur le seul nom ou la disponibilité HTTP.


## Relevé des fichiers historiques réellement servis — 28 octobre 2026

L'exploitant a lu les métadonnées des fichiers de `/srv/www/capable/current` (taille, SHA256, titre, titres de section et liens vers les sources). **Ce relevé ne contient pas le corps complet des pages**, et ne permet donc pas encore d'en auditer chaque affirmation.

| Projection | Empreinte SHA256 | Contenu et provenance observables |
| --- | --- | --- |
| `magazine.html` (5 832 octets) | `910db16cf90dbf462209c5a3e54e2dc9faee1685fdeafb90d4729a06936c23c2` | « Le Magazine — Capable » ; n°2 « Jalon P1–P18, Matrice d'Effectivité et Twins Institutionnels » et n°1 « Lancement de la campagne présidentielle 2027 ». Liens vers les issues #98 et #100 et deux chemins `projects/capable/magazine/*.md`. |
| `annexes.html` (1 195 octets) | `aedb82e0c448735466a9e69178d9f52ef4f8614ea9a979c047ca19816a55d1d7` | « Annexes & Sources » ; aucun lien de provenance relevé ; absence d'URL canonique dans le HTML. |
| `cases.html` (3 238 octets) | `8d33c91d422075ddd1db12cdf9f0473de453041269bac1034b597d5d13e8e8e0` | « Études de cas & Épreuves du Réel » ; cas 01 « L'épreuve des présentations à la présidentielle 2027 », cas 02 « Le test d'effectivité de l'accès aux droits en milieu rural ». Aucun lien GitHub ou lien contenant « source » détecté par le relevé. |

### Résolution des pointeurs du Magazine

Les deux liens Markdown déclarés par `magazine.html` sont :
- `projects/capable/magazine/2026-10-05-jalon-p1-p18-matrice-eim.md` ;
- `projects/capable/magazine/2026-10-02-n1-lancement-campagne-presidentielle.md`.

**Vérification GitHub sur `barons-Mariani/main` : les deux chemins renvoient 404.** Ce sont donc des **pointeurs de provenance dans le HTML**, mais ils ne constituent pas encore des sources canoniques accessibles à ces chemins. Les issues #98 et #100 sont des pistes de recherche, non la preuve de l'existence des deux documents à leur emplacement attendu.

Pour `cases.html`, les deux intitulés orientent vers les chantiers de l'Observatoire des présentations et d'accès effectif aux droits ; cela reste une hypothèse de filiation tant que le texte intégral n'est pas confronté aux sources. Pour `annexes.html`, la filiation demeure inconnue.

### Décision de conservation et méthode de réconciliation

1. **Ne rien supprimer ni écraser** : les trois pages ont un contenu éditorial identifiable, malgré leur absence de la source Git attendue.
2. **Récupérer leurs corps intégraux en lecture seule** depuis la release active et les comparer au Corpus ; rechercher les documents et versions par historique Git et par issues si nécessaire.
3. Réparer d'abord les liens du Magazine devenus introuvables ; éviter toute déclaration de provenance vérifiée sans résolution effective.
4. Une fois les sources retrouvées, importer les projections pertinentes dans la chaîne éditoriale versionnée, avec métadonnées de dérivation et validation de fraîcheur. Aucun déploiement n'est impliqué dans ce constat.
