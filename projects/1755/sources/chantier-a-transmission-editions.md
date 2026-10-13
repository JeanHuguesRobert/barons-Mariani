---
title: "1755 — Chantier A : histoire du texte transmis"
date: "2026-10-13"
status: "investigation-open"
version: "0.1"
document_role: "source"
document_kind: "textual-collation"
license: "CC BY-SA 4.0"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/1755/sources/chantier-a-transmission-editions.md"
related_documents:
  - projects/1755/sources/reconstitution-texte-1755-etat-initial.md
  - projects/1755/sources/chantier-b-etablissement-manuscrit.md
---
# Chantier A — Histoire du texte transmis

**Objet autonome** : décrire ce que chaque éditeur a publié et transmis sous le nom de « Constitution corse de 1755 » ; établir les écarts, la filiation éditoriale, leur contexte et leurs conséquences éventuelles sur l'interprétation. Cela **n'établit pas** à soi seul le texte effectivement voté.

## Témoins, sans assimilation
| Sigle | Témoin | Accès | Statut de lecture |
|---|---|---|---|
| R1900 | Ambrogio Rossi, *Osservazioni storiche*, livre X, BSSHNC, fasc. 237–240 (1900), p. 136–141 | [Notice BnF](https://catalogue.bnf.fr/ark:/12148/cb31248785r), Gallica candidat bpt6k4801726 | Pages non collationnées directement |
| F1907 | Matthieu Fontana, *La constitution du généralat de Pascal Paoli*, appendice I, p. 161–164 | [Internet Archive](https://archive.org/details/ConstitutionPaoliCorse), [OCR](https://archive.org/stream/ConstitutionPaoliCorse/ConstitutionPaoliCorse_djvu.txt) | Extrait indirect rapporté dans dossier ; images à contrôler |
| C1974 | Dorothy Carrington, « Paoli et sa Constitution », *AHRF* 218, p. 508–541 | [Persée](https://www.persee.fr/doc/ahrf_0003-4436_1974_num_218_1_4183) | Citation critique d'un manuscrit, **pas une édition intégrale équivalente** |
| C1996 | Dorothy Carrington, *La constitution de Pascal Paoli 1755* | [M3C](https://m3c.universita.corsica/s/fr/item/128781) | Texte non récupéré |
| K2008 | Costanzo (éd.), *Costituzione della Corsica [1755]* | [Liberilibri](https://www.liberilibri.it/catalogo/costituzione-della-corsica-1755/) | Texte non récupéré |

## Apparatus de collation v0.1 : préambule (segment A-001)

**Lecture F1907, citée et à confirmer sur le fac-similé** : `La Dieta generale rappresentante il popolo di Corsica, unico padrone di se medesimo`.

**Lecture C1974 du manuscrit, citée, sans contrôle direct du manuscrit** : `La Dieta Generale del Populo di Corsica, Lecitimamente Patrone di se medesimo`.

L'orthographe exacte de F1907 doit être contrôlée contre la page image : le segment indiqué dans l'OCR a déjà fait l'objet d'une normalisation de travail ; dans une édition philologique, **ne jamais cacher cette intervention**.

| Lieu | F1907 (provisoire) | Manuscrit cité par Carrington | Différence |
|---|---|---|---|
| Fonction de la Diète | `rappresentante il popolo` | `del Populo` | qualification explicite de représentation vs appartenance |
| Qualité de maître | `unico padrone` | `Lecitimamente Patrone` | exclusivité vs légitimité |
| Graphies | `Dieta / popolo / padrone` | `Dieta / Populo / Patrone` | variantes de forme, à confirmer sur images |

**Portée** : une divergence substantielle de formulation est *signalée*, pas son origine ni la supériorité d'un témoin. Ne pas en déduire une thèse de souveraineté populaire sans examiner tout le préambule, le contexte de production et les institutions.

## Autres segments indexés, non encore collationnés
A-002 composition et chambres du Conseil d'État ; A-003 mode de délibération et rotation ; A-004 Général et guerre ; A-005 réunion annuelle de la Diète ; A-006 reddition de comptes et Sindacato. Le texte F1907 est présent dans son appendice ; pour chacun l'alignement mot à mot avec R1900/C1974 reste à faire.

## Acquisition et contrôles prioritaires
1. Télécharger légalement les **images** de F1907 p. 161–164 et noter index de scan / numéro imprimé / fichier / hash.
2. Extraire la transcription OCR brute séparément de la correction humaine ; noter chaque correction.
3. Récupérer R1900 p. 136–141 ; vérifier la filiation revendiquée par Fontana au lieu de présumer son identité mot à mot.
4. Collationner A-001 à A-006 avec provenance et incertitudes ; conserver aussi suppressions, additions et déplacements.
5. Ajouter C1996 et K2008 uniquement après consultation réelle.
6. Distinguer édition ancienne, texte historique, traduction moderne et commentaire ; ne pas attribuer de licence moderne au document ancien par confusion avec sa reproduction.

## Mesure d'effectivité
Une matrice reproductible par un tiers (fac-similés vérifiables, index précis, variantes localisées) et une chronologie des transformations du texte ; **ne pas compter des OCR bruts comme éditions établies**.

## Reality Test documentaire — correction FBF du 13 octobre 2026

Le [Packet de récupération](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6153511404) a obtenu HTTP 200 sur les métadonnées Archive de `ConstitutionPaoliCorse` et `IA41555227_0091`, mais n'a **pas** récupéré le texte OCR de Fontana (échec `fetch`). **Correction d'identité** : `IA41555227_0091` est également une numérisation de la thèse de **Matthieu Fontana (1907)**, selon ses métadonnées `creator/title`; ce n'est **pas** Rossi. La recherche directe Rossi effectuée durant ce test n'a donné aucun exemplaire confirmé. Cette correction ne doit pas effacer l'hypothèse antérieure : elle en documente l'invalidation.

[Calculette — leçon FBF](https://github.com/JeanHuguesRobert/cogentia/issues/233#issuecomment-6153596314) : `identifiant découvert ≠ source identifiée ≠ texte effectivement inspecté`. La branche `obtenir les pages` est **bloquée sur un mode de téléchargement**, non épuisée. Un [Packet de diagnostic des formats Archive](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6153605204) a été demandé ; ne pas inférer son succès avant son reçu.
