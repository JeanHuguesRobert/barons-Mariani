# Diagnostic reproductible — OCR Tesseract de FRAD02A_0002

Date : 20 octobre 2026. Source : Archives du Pumonti, cote 1 J 7/1, JPEG `FRAD02A_0002.jpg`.

## Calcul réellement réalisé

- [GitHub Actions run 39397729120](https://github.com/JeanHuguesRobert/barons-Mariani/actions/runs/39397729120) : succès technique.
- Artefact `manuscript-reading-3`, ID `12253295443`, téléchargé puis inspecté, incluant `ocr-candidate.txt`, `ocr-provenance.json` et quatre bandes PNG.
- Moteur : Tesseract, modèle de langues `ita+fra`, segmentation `--psm 3`, source JPEG d'origine (pas les bandes chevauchantes).
- Sortie OCR : **1 976 caractères Unicode**, **125 lignes**, **605 mots approximatifs** par découpage espaces.
- Contrôle lexical *exact*, sans normalisation ni appariement flou : les marqueurs `Dieta`, `Generale`, `convocarsi`, `Magistrato`, `Delle cause` sont **tous absents** ; `lire` apparaît au moins une fois. Ces marqueurs viennent des fiches de lecture provisoires et ne sont pas un jeu de vérité terrain validé.
- Exemple OCR : `Di pie Ace «Lor AC FA ; rh - : L È * + eee LE > grind ss` ; bruit dominant.

**Interprétation** : pipeline de découpe et OCR opérationnel, **sortie textuelle inutilisable en l'état comme transcription**. Ne pas ajouter ces 125 lignes au texte critique, ni prétendre mesurer un CER sans transcription de référence contrôlée.

## Décision de traitement

1. Conserver l'artefact et ce diagnostic comme preuve d'essai, non comme texte établi.
2. Tester un **HTR** spécialisé sur un ou deux petits passages dont nous aurons une transcription de référence manuellement contrôlée.
3. Premier candidat : **Kraken** (logiciel libre, modèles historiques avec possibilité de spécialisation), eScriptorium pour l'interface éventuelle. Il faut contrôler la compatibilité du modèle choisi avec l'italien cursif du XVIIIe siècle avant une exécution en lot.
4. Alternative externalisée : modèle **Transkribus Italian Handwriting M1**, spécifiquement annoncé pour les écritures italiennes des XVIe–XIXe siècles ; nécessite de vérifier les conditions d'usage, comptes, traitements externes et droits sur les images avant transmission.
5. Comparaison équitable : mêmes zones source, sorties conservées sans édition, mesure CER/WER **seulement sur le segment de vérité terrain validée**, provenance (modèle/version/hachage/paramètres) conservée. Ne pas annoncer une qualité fondée sur une métrique publiée sur d'autres documents.

Liens techniques : [Kraken](https://github.com/mittagessen/kraken), [eScriptorium](https://escriptorium.eu/about/), [Transkribus Italian Handwriting M1](https://www.transkribus.org/models/transkribus-italian-handwriting-m1).

**État :** `tesseract_rejected_for_transcription / htr_evaluation_pending`.
