# Préparer des bandes de lecture reproductibles

**Statut : outil expérimental, sans OCR ni transcription automatique.** Il transforme une image en quatre (ou davantage) bandes PNG qui se recouvrent, conservant les coordonnées et empreintes de provenance. Le résultat est une aide au déchiffrement, jamais une attestation du texte historique.

## Exécuter via GitHub Actions

1. Ouvrir [Manuscript — reading crops](https://github.com/JeanHuguesRobert/barons-Mariani/actions/workflows/manuscript-reading-crops.yml).
2. Choisir **Run workflow**, sélectionner la branche `main`, puis renseigner le nom de l'image (ex. `FRAD02A_0002.jpg`) et le nombre de bandes (défaut : 4).
3. Une fois l'exécution terminée, récupérer l'**artefact** `manuscript-reading-<numéro>` contenant les bandes PNG et `manifest.json`.
4. Lire les bandes avec leurs coordonnées ; proposer les leçons dans [la fiche correspondante](README.md) ou par [issue GitHub](https://github.com/JeanHuguesRobert/barons-Mariani/issues/new). Ne pas intégrer directement une proposition au texte établi.

Le workflow est **manuel, en lecture seule** et ne publie aucune interprétation. En cas d'échec, consulter les logs ; une exécution locale est également possible.

## Exécuter localement

```sh
python -m pip install 'Pillow>=10,<12'
python scripts/test-prepare-manuscript-reading.py
python scripts/prepare-manuscript-reading.py \
  projects/1755/sources/constitution-1755-manuscrit/images/FRAD02A_0002.jpg \
  --output build/manuscript-reading/FRAD02A_0002 --bands 4 --overlap 120
```

Les PNG produits sont des dérivés d'inspection à conserver distincts des JPEG sources et des TIFF archivistiques. Le manifeste enregistre les rectangles `[x0,y0,x1,y1]` en pixels, la somme SHA-256 du fichier source, celles des bandes, les paramètres et l'état `unreviewed`. Les traits incertains exigent une relecture sur le TIFF fourni par les Archives du Pumonti, cote **1 J 7/1**.

## Limites et critères de promotion

- Découpage horizontal régulier : il ne suit pas automatiquement les lignes d'écriture ni les colonnes.
- Aucune reconnaissance d'écriture, aucun texte inventé, aucune correction silencieuse.
- Pour chaque proposition : `FRAD02A_xxxx`, rectangle ou lignes, lecture avec crochets d'incertitude, justification, éditeur/relecteur et référence du témoin.
- Promotion vers une transcription diplomatique seulement après lecture intégrale, contrôle des raccords, confrontation TIFF et seconde relecture.

[Registre des onze vues](registre-consolide-11-vues.md) · [Manifeste des JPEG](../manifest.json).
