# Deployment note — Napoléon

Public name: `https://napoleon.acorsica.org`.

## Architecture de déploiement préparée

Le nom de domaine cible `napoleon.acorsica.org` est rattaché à l'infrastructure confédérale Operium / Fracta :
- Enregistrement DNS-only Cloudflare CNAME `napoleon.acorsica.org` pointant vers `fracta.fractavolta.com`.
- Terminaison TLS gérée par Fracta avec reverse-proxy vers l'origine HTTP Fracta2.
- Racine servie : projection statique de `projects/napoleon/site/` (et accès au corpus structuré sous `projects/napoleon/data/`).

## État de déploiement

- **Statut :** Projection de travail locale prête, configuration cible préparée sur le papier (`deployment performed: false`).
- **Principe de gouvernance :** Aucune mutation d'infrastructure en direct (DNS, certificats ou hôtes distants) n'est exécutée sans passage explicite du GitHub Write Gate et validation humaine.
- **Publication continue :** Les mises à jour s'effectuent par commit Git auditable sur la branche `main` du dépôt `barons-Mariani` rattaché à l'[Issue #99](https://github.com/JeanHuguesRobert/barons-Mariani/issues/99).

## Utilisation locale

Pour servir la projection statique en local :

```bash
cd projects/napoleon/site
python -m http.server 8080
# ou npx serve
```
