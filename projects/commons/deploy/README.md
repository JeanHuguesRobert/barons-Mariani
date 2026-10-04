# Note de déploiement — Commons

Nom public cible : `https://commons.acorsica.org`

## 1. Schéma d'hébergement prévu (modèle Operium / FractaVolta)

Conformément à la convention déjà opérationnelle pour `diaspora.acorsica.org` et spécifiée pour `privai.acorsica.org` :

1. **Routage DNS** : CNAME Cloudflare `commons.acorsica.org` pointant vers `fracta.fractavolta.com` (gestion d'infrastructure réservée à Operium).
2. **Terminaison TLS & Reverse-Proxy** : Prise en charge par `fracta.fractavolta.com` avec reverse-proxy vers l'origine Fracta2.
3. **Origine HTTP** : Fracta2 sert une release statique immuable sous `/srv/www/commons/current`.
4. **Racine publiée** : Arborescence `projects/commons/site/` (HTML5 pur, styles CSS, robots.txt, sitemap.xml, llms.txt, scripts JavaScript vanilla).
5. **Absence de CNAME dans Git** : Aucun fichier `CNAME` n'est placé dans ce dossier afin d'éviter toute capture parasite ou redirection conflictuelle par GitHub Pages.

## 2. État au 4 octobre 2026

- **Nom de domaine** : `commons.acorsica.org` ne résout pas encore depuis ce poste de travail (aucun enregistrement forcé sans ordre exprès).
- **Surface statique** : Prête et vérifiée dans `projects/commons/site/` (100% de liens internes valides, aucun framework externe, compatible lecture universelle).
- **Gouvernance opérationnelle** : Le déploiement effectif et la gestion des certificats relèvent d'**Operium** (`operium up`). Aucun script d'infrastructure ad-hoc ne doit être inventé dans ce dépôt.

## 3. Prévisualisation locale

```bash
cd projects/commons/site
python -m http.server 8793
```
