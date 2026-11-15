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

**État au 15 novembre 2026 : publication HTTPS opérationnelle ; sept pages HTML et une feuille CSS accessibles, dont la Boutique en préparation.**

- **Hôte canonique retenu par le Principal le 15 novembre 2026** : `museum.baronsmariani.org`. **Un seul hôte, sans alias ni redirection `musee`**, selon le principe d'Occam.
- **DNS et publication vérifiés (15 novembre 2026)** : `CNAME museum.baronsmariani.org → fracta.fractavolta.com` (Cloudflare, DNS only), HTTP/HTTPS Caddy actif, certificat TLS validé, pages HTTP 200. **Aucun alias `musee`.**
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


## Mise à jour du 15 novembre 2026 — DNS réellement créé

À la suite de la clarification par le Principal de la **délégation permanente Optimistic Locking**, le provisionneur existant d'Operium a réalisé un seul effet DNS sur le ThinkPad propriétaire : `museum.baronsmariani.org`, CNAME vers `fracta.fractavolta.com`, proxy Cloudflare désactivé, TTL automatique. L'API Cloudflare a retourné une création réussie et une lecture de contrôle indépendante a confirmé le nom, le type, la cible et le mode DNS-only.

Les deux serveurs Cloudflare faisant autorité confirment la résolution ; aucun alias `musee` n'est prévu. La vérification HTTPS a échoué lors de la négociation TLS. Le domaine **existe**, mais le Musée **n'est pas encore accessible en HTTPS**.

La modification a été effectuée selon l'instruction permanente et spécifique du Principal, **sans démonstration d'une admission canonique COP** ; le raccordement du mandat permanent à l'exécuteur Cogentia demeure à réparer génériquement, sans mandat ponctuel supplémentaire. Voir le [reçu opérationnel Operium](https://github.com/JeanHuguesRobert/operium/blob/main/docs/living-books-deployment.md).

Restent uniquement la mise en place du répertoire de publication `/srv/www/musee/current`, du vhost Caddy et du certificat, puis la vérification des pages d'accueil, Livre, Magazine, **Boutique**, Annexes et Contribuer.


## Déploiement accompli le 15 novembre 2026

La publication statique du Musée a été installée à partir de la révision GitHub `3487f3d4e3c504d5044355dc39bd75323e3bb0ec` sous `/srv/www/musee/releases/`, avec un lien `current` atomique. Les fragments Caddy dédiés `museum.caddy` (HTTP) et `museum-tls.caddy` (HTTPS) ont été ajoutés au serveur public Fracta2, sans modification des hôtes existants. Le script borné, le précontrôle et la méthode de retour arrière sont disponibles dans [Operium](https://github.com/JeanHuguesRobert/operium/blob/main/scripts/ops/publish-museum-static.sh).

Le contrôle public a constaté un code **200** et un certificat valide pour l'accueil, le Livre, le Magazine, la **Boutique**, les Annexes, Contribuer, les Mentions et la CSS. Les sites voisins Suicide Corse, Rise & Fall et Capable sont restés en **200** ; le navigateur protégé est resté en **401**, comme attendu. Le premier lancement a connu une erreur d'échappement sans mutation, puis une tentative avec réponse de commande tardive a été **confirmée par relecture indépendante de l'état réel**.

Cette mise en ligne ne change **ni l'état de préparation du numéro 1**, ni le statut non commandable des produits de la Boutique. Les constats antérieurs de ce document restent conservés comme historique, mais **leurs mentions « DNS absent », « TLS absent » et « site non déployé » sont désormais supersédées** par le présent reçu.


### FBF du contenu après publication — révision finale du 15 novembre 2026

Le premier déploiement contenait encore des indications obsolètes « domaine non publié » dans l'accueil, le Magazine et les pieds de page. Sources corrigées sur `main` dans le commit `f7f8ef131b5fc81d5a68e11cb404e886ad865861`, puis **nouvelle release immuable** déployée : `/srv/www/musee/current → releases/f7f8ef131b5fc81d5a68e11cb404e886ad865861`.

Relecture indépendante : mentions « domaine non publié » absentes de l'accueil ; mentions de l'accès HTTPS présentes sur l'accueil et le Magazine ; `/`, `/magazine.html` et `/boutique.html` renvoient chacun **HTTP 200, certificat valide**. Aucun incident observé sur Suicide Corse, Rise & Fall et Capable ; le navigateur privé conserve son contrôle d'accès 401. Le numéro 1 demeure en préparation, la Boutique n'accepte aucune commande. Voir le reçu complet dans Operium.
