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

## État vérifié sur Fracta2 — 15 novembre 2026

Le contrôle en lecture seule depuis l'hôte `fracta2` établit que :

- les serveurs DNS de `baronsmariani.org` sont chez Cloudflare, mais `museum.baronsmariani.org` ne présente **pas encore de réponse CNAME/A** ;
- le domaine de comparaison `suicidecorse.baronsmariani.org` pointe par CNAME vers `fracta.fractavolta.com` (origine publique actuellement résolue) ;
- `/srv/www/musee/` et `/srv/www/musee/current` **n'existent pas** ;
- aucun vhost Caddy `museum.baronsmariani.org` n'a été trouvé dans les répertoires de configuration inspectés ; un appel HTTP local avec cet en-tête Host a répondu **401**, et non une page du Musée ; le même essai avec `suicidecorse.baronsmariani.org` a répondu **200** ;
- les répertoires publics et la configuration Caddy sont administrés par root ; le shell `ubuntu` normal ne peut pas y déployer automatiquement un site.

Le coffre JHN comporte la référence privée de la clé Cloudflare. Cependant, la tentative d'utiliser une méthode documentée d'appel API depuis Supabase a été **bloquée par les contrôles d'exécution avant l'appel Cloudflare** ; aucun DNS n'a été créé, et les droits effectifs du jeton n'ont pas été évalués. Le shell Fracta2 ne dispose pas de cette clé et le CLI existant déclare l'absence d'identifiants utilisables. Une commande distante via le système Cogentia exige également une autorisation d'effet émise indépendamment ; son simple inventaire ne donne pas le droit de l'exécuter.

**Dépendances restantes (séparées) :** (1) opération Cloudflare sémantique autorisée et lecture contradictoire de l'enregistrement ; (2) release statique incluant [Boutique](../site/boutique.html) dans `/srv/www/musee/current` ; (3) vhost Caddy HTTP/HTTPS, certificat et contrôles d'accès appropriés ; (4) vérification extérieure de `/`, `/book.html`, `/magazine.html`, `/boutique.html` et des liens de sources. Le journal opérationnel figure dans [Operium](https://github.com/JeanHuguesRobert/operium/blob/main/docs/living-books-deployment.md).

**Aucune étape ci-dessus n'est déclarée achevée sans réception et vérification de son effet.**
