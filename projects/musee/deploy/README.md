---
title: "Musée — État du déploiement"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-11-15"
last_modified_at: "2026-11-15"
status: working-paper
language: fr
license: CC BY-SA 4.0
document_role: operational
document_kind: deployment-note
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/musee/deploy/README.md
provenance:
  origin_type: conversation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: "mandat de création du Livre Vivant du Musée, 2026-11-15"
  origin_date: "2026-11-15"
  derived_from:
    []
review:
  status: unreviewed
  reviewed_by: []
---

# Publication Web envisagée

**État au 15 novembre 2026 : source GitHub et projection HTML, pas de déploiement autonome vérifié.**

- **Hôte canonique retenu par le Principal le 15 novembre 2026** : `museum.baronsmariani.org`. **Un seul hôte, sans alias ni redirection `musee`**, selon le principe d'Occam.
- **DNS, TLS et routage** : à contrôler puis configurer dans le plan opérationnel autorisé ; la présente décision ne signifie pas qu'un service est déjà déployé.
- **Site préparé** : `projects/musee/site/`, ensemble de pages statiques source-first.
- **Registre opérationnel** : [Operium — living-books-deployment.md](https://github.com/JeanHuguesRobert/operium/blob/main/docs/living-books-deployment.md). Les onze Livres Vivants précédemment recensés n'incluent pas `musee`.
- **Prochaine étape opératoire** : inspecter la topologie publique réellement active (route, DNS, TLS, origine et déploiement) ; enregistrer la décision de nom de domaine, puis effectuer un déploiement autorisé séparément avec vérification HTTP, contenu, liens et retour arrière.

L'existence d'un manifeste, d'un site sous GitHub ou d'un nom proposé n'est pas la preuve d'un service accessible. Ne pas créer d'enregistrement DNS ni modifier une passerelle HTTPS au seul motif de ce document.
