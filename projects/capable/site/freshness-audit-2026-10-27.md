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
