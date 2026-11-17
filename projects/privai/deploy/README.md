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
