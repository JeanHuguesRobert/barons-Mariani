---
title: "Rise & Fall — reçu du déploiement public du 18 novembre 2026"
description: "Trace vérifiée de la projection corrigée du livre et de la publication atomique sur Fracta2."
author: unknown
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-11-18"
last_modified_at: "2026-11-18"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "investigation-journal"
document_kind: "production-deployment-receipt"
visibility: public
lifecycle_state: "active"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/journals/2026-11-18-deploiement-production-source-vers-site.md"
update_policy: "UP-DEFAULT-REVIEWED"
generated_by: "GPT-6"
provenance:
  origin_type: conversation
  origin_repository: unknown
  origin_ref: unknown
  origin_date: "2026-11-18"
  derived_from:
    - projects/rise-and-fall/manuscript/book/02-antoine-dominique-et-titre-1813.md
    - projects/rise-and-fall/investigation/notes/titre-mariani-legitimite-silences-et-branches.md
    - projects/rise-and-fall/sources/README.md
review:
  status: unreviewed
  reviewed_by: []
---

# Déploiement effectif de *Rise & Fall* — 18 novembre 2026

## Mandat et état de départ

Le Principal a demandé de privilégier l'intégration sur `main` et d'effectuer les déploiements réversibles malgré le risque d'indisponibilité temporaire, dans le contexte d'un service expérimental dont il déclare qu'il n'a pas encore d'usagers. Cette déclaration n'est pas une mesure instrumentée de trafic. Aucune autorisation de publication d'informations privées ni de gel d'édition n'en découle.

La source critique du 18 novembre corrige l'anachronisme « Conseil du Sceau créé en 1859 » (Conseil dès 1808, Commission en 1814, rétablissement en 1859). Le site public servait encore une release initiale de septembre 2026 avec des assertions devenues périmées sur la date du titre westphalien.

## Version source publiée

- **Révision exacte** : [`1cb7940ccebb386ae9d7196cc48690b601501c98`](https://github.com/JeanHuguesRobert/barons-Mariani/commit/1cb7940ccebb386ae9d7196cc48690b601501c98), poussée directement sur `main`.
- **Origine** : `projects/rise-and-fall/manuscript/book/`, neuf chapitres, et note critique du 18 novembre.
- **Générateur suivi** : `scripts/render-rise-and-fall-working.py`.
- **Projections mises à jour** : `projects/rise-and-fall/site/book.html`, `book.pdf`, `book.epub`, `editions/volume-1-preview/index.html`, `index.html`, navigation, `styles.css`, guide et `llms.txt`; miroirs et empreintes de `projections/preview.*`.
- **Aucune édition gelée modifiée** : le Volume I reste une préversion de travail.

## Opération de production

- **Cible** : `riseandfall.baronsmariani.org`, serveur `fracta2`, racine `/srv/www/riseandfall/`.
- **Source préparée** : un worktree propre au SHA exact, 21 fichiers publics, empreintes SHA-256 vérifiées en préflight ; fichier source `site/` sans lien symbolique.
- **Précondition réelle** : `current -> releases/2026-09-30-initial`, racine et Caddy actifs, HTTPS public 200/TLS valide.
- **Autorité / transport** : délégation explicite du Principal dans la conversation ; exécution par la route existante ThinkPad authentifié → SSH Fracta2 → `sudo`, après préflight en mode non privilégié. Ce résultat **n'est pas** une preuve d'admission canonique COP par un MandateDeclaration signé.
- **Action** : installation des 21 fichiers en release immuable `/srv/www/riseandfall/releases/1cb7940ccebb386ae9d7196cc48690b601501c98`, propriété `root:root`, puis échange atomique du lien `current`. **Aucun changement de DNS, Caddy, autre vhost ou service**. Pas de redémarrage Caddy.
- **Reçu effectif** : `PUBLISHED=PASS HOST=riseandfall.baronsmariani.org REV=1cb7940ccebb386ae9d7196cc48690b601501c98 OLD=releases/2026-09-30-initial HTTP=200 HTTPS=200 CERT=VALID BOOK=UPDATED PDF=200 EPUB=200`.
- **Lecture de confirmation** : `readlink /srv/www/riseandfall/current` donne `releases/1cb7940ccebb386ae9d7196cc48690b601501c98`. Les URL publiques `/`, `/book.html`, `/book.pdf`, `/book.epub`, `/styles.css`, `/editions/volume-1-preview/`, `/guide.html`, `/contribuer.html` répondent chacune **HTTP 200, TLS verify 0** depuis Fracta2 ; le HTML servi contient la rectification « Conseil du Sceau » et l'accueil « État de l’enquête — novembre 2026 ».
- **Contrôle voisinage** : `suicidecorse.baronsmariani.org`, `museum.baronsmariani.org`, `capable.acorsica.org` : HTTP 200 / TLS verify 0 au moment du contrôle ; `caddy.service=active`.

## Limites, reprise et retour arrière

Le test des liens HTML, des chapitres, des empreintes de projection et de la structure ZIP EPUB a réussi. Le fichier PDF possède un en-tête et une fin conformes, mais n'a **pas** fait l'objet ici d'une revue visuelle exhaustive de toutes les pages. Les tests de validation stricte du frontmatter Cogentia n'ont pas été exécutés dans cette passe.

**Retour arrière** : le répertoire `releases/2026-09-30-initial` reste disponible. Sur le nœud d'origine, sous autorité administrative appropriée, restaurer atomiquement le lien `current` vers cette release précédente puis vérifier les réponses publiques. Éviter de supprimer les releases antérieures tant que la publication n'est pas stabilisée.

La release publique est un état observé, non une preuve d'absence de trafic, de conformité historique exhaustive ou de gel éditorial. Les sources manquantes sur la création du titre et sa dévolution demeurent ouvertes dans le registre archivistique.
