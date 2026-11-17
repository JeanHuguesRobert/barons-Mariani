---
title: "PrivAI — Déploiement et preuves de publication"
author: unknown
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: CC BY-SA 4.0
language: fr
date: "2026-10-04"
last_modified_at: "2026-11-17"
status: working-paper
document_role: operational
document_kind: deployment-report
visibility: public
lifecycle_state: active
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/deploy/README.md
update_policy: UP-DEFAULT-REVIEWED
provenance:
  origin_type: unknown
  origin_repository: unknown
  origin_ref: unknown
  origin_date: unknown
  derived_from: []
review:
  status: unreviewed
  reviewed_by: []
ai_assisted_by:
  - GPT-6
---

# Note de déploiement — PrivAI

Nom public cible : `https://privai.acorsica.org`

## 1. Schéma d'hébergement prévu (modèle Operium / FractaVolta)

Conformément à la convention déjà opérationnelle pour `diaspora.acorsica.org` :

1. **Routage DNS** : CNAME Cloudflare `privai.acorsica.org` pointant vers `fracta.fractavolta.com` (gestion réservée à Operium).
2. **Terminaison TLS & Reverse-Proxy** : Prise en charge par `fracta.fractavolta.com` avec reverse-proxy vers l'origine Fracta2.
3. **Origine HTTP** : Fracta2 sert une release statique immuable sous `/srv/www/privai/current`.
4. **Racine publiée** : Arborescence `projects/privai/site/` (HTML5 pur, styles CSS, robots.txt, sitemap.xml, llms.txt).
5. **Absence de CNAME dans Git** : Aucun fichier `CNAME` n'est placé dans ce dossier afin d'éviter toute capture parasite par GitHub Pages.

## 2. État au 4 octobre 2026

- **Nom de domaine** : `privai.acorsica.org` ne résout pas encore (aucun enregistrement forcé sans ordre exprès).
- **Surface statique** : Prête et vérifiée dans `projects/privai/site/` (100% de liens internes valides, aucun framework externe).
- **Gouvernance opérationnelle** : Le déploiement effectif et la gestion des certificats relèvent d'**Operium** (`operium up`). Aucun script d'infrastructure ad-hoc ne doit être inventé dans ce dépôt.

## 3. Prévisualisation locale

```bash
cd projects/privai/site
python -m http.server 8791
```

## 4. Observations du 17 novembre 2026

Une vérification HTTPS indépendante a confirmé que `guide.html` et `guide.js` de PrivAI sont servis (HTTP 200). L'origine utilise une release immuable `/srv/www/privai/releases/2026-10-05-working` et un lien `current` ; cette vérification n'autorise aucune mise à jour silencieuse de la production.

La mutualisation du Guide avec Capable dans le Corpus produit une **nouvelle projection source**, non une publication de cette projection sur `privai.acorsica.org`. Toute mise en service doit préserver le contenu durable, utiliser un déploiement atomique autorisé et produire des preuves indépendantes (version/source, empreintes HTTP, contrôles réels du Guide). Ne pas confondre état Git, artefact et contenu servi.

## 5. Mise en service vérifiée — 17 novembre 2026

Le point 4 ci-dessus conserve **l'observation historique avant publication**. Une nouvelle release a ensuite été déployée sous mandat du Principal et vérifiée sur le domaine public.

- **Nouvelle release immuable :** `/srv/www/privai/releases/guide-cd0201b782b6`.
- **Source fixée :** `JeanHuguesRobert/barons-Mariani` commit `cd0201b782b628962c14b57121814786b8ffdee4`, deux fichiers issus du client de Guide partagé.
- **Périmètre exact :** seuls `guide.html` et `guide.js` ont changé ; 16 autres fichiers sont inchangés.
- **Empreintes publiques SHA-256 :** `guide.html` = `1d13d42bbd6ea9336995f0ea7eb345b3ab65478ebcd24b887f863755fc97748b` ; `guide.js` = `a98a5b4d9d1bf54dbc8344de8e3880123442fc5839c5e5e2feb8c55e573b9e72`.
- **Édition durable intacte :** `book.html` = `93860eaa7e1bb00ee6d43dd2aa2b7baee77edaf5725c44b644bca66c85057f6f` ; `book.pdf` = `d227970cd604830a779816daa1c18677195e96e8e9d8062336c23c77423a935a` ; `book.epub` = `1986d027aff591c55d793d76e4459363cff6cac13ff219546182acb596afc007`.
- **Retour arrière conservé :** `/srv/www/privai/releases/2026-10-05-working` demeure disponible ; le lien `current` bascule atomiquement, sans modification des données de l'ancienne release.
- **Reçu d'administration local non public :** `/srv/www/privai/guide337-deploy-receipt.json`.
- **Vérifications de réalité :** pages HTTPS 200 et empreintes vérifiées après le basculement ; test Chromium réel en affichage mobile 390 px avec requête SSE complète, réponse affichée et aucune conservation locale sans consentement.

### Condition transverse : autorisation CORS

Le Guide public contacte `https://cogentia.fractavolta.com/guide/chat` depuis une autre origine. Les origines `https://privai.acorsica.org` et `https://capable.acorsica.org` doivent donc être présentes **explicitement** dans `COGENTIA_CORS_ORIGIN`. Sur Fracta2, cette politique est projetée par `/etc/systemd/system/mcp-cogentia.service.d/zz-guide337-cors.conf` ; elle préserve les origines antérieures. Les prérequêtes `OPTIONS` sont vérifiées en HTTP 204, avec `Access-Control-Allow-Origin` exact et `Vary: Origin`, et aucune autorisation pour une origine non approuvée.

Le mécanisme général de Factory ne doit pas assimiler la génération de `guide.js` à l'activation d'un profil et de son origine CORS.

### Limites de confidentialité

La conservation locale est volontaire ; le collage d'une réponse d'agent externe et la transmission d'historique sont des actes distincts sous contrôle du visiteur. Les paquets COP du Guide ont été modifiés pour ne plus conserver la question en clair en mémoire, mais **cela ne démontre aucune absence de rétention** dans les fournisseurs de modèles, les proxys ou les journaux d'infrastructure. Le délai de conservation de ces composants doit être audité séparément.

Les éditions ne sont pas gelées par le déploiement du Guide. Les modifications de l'infrastructure de calcul d'embeddings relèvent d'un paquet cognitif parallèle.
