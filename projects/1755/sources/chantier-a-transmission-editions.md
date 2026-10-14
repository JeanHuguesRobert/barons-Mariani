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

### Test de formats (13 octobre 2026, second reçu)

Le [résultat COP du Packet de formats](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6153617552) établit par lecture des métadonnées Archive que les copies **Fontana** `ConstitutionPaoliCorse` et `IA41555227_0091` comportent chacune des dérivés `_djvu.txt`, `_hocr.html`, un PDF, les images JP2 et des index de pagination. Les téléchargements directs OCR et hOCR du premier exemplaire **ont échoué** (erreur `fetch failed`) : disponibilité déclarée dans l'inventaire **≠** bytes téléchargés **≠** pages lues et validées. Le document **Rossi reste absent** de cet inventaire ; aucune collation directe supplémentaire n'est donc annoncée.

**Prochaine dépendance** : vérifier la récupération de pages via un canal Archive autorisé alternatif ou demande de consultation, puis annoter les indices image/imprimé, hash et transcriptions. Ne pas inférer l'identité bibliographique depuis un identifiant technique ni transformer un blocage transitoire en épuisement de la branche.

## Acquisition OCR effective F1907 — 13 octobre 2026

**Nouvelle preuve matérielle :** le [Packet COP d'acquisition](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6153730287) a enregistré l'OCR complet de Fontana depuis Internet Archive, en **283 345 octets**, empreinte SHA-256 `a6b89e3f4e34f9f8a9468a43e44bb37a883b191303b9231d720388049164a428`. [Run et artefact](https://github.com/JeanHuguesRobert/inseme/actions/runs/38456920141). Source réseau exacte : `https://ia600500.us.archive.org/22/items/ConstitutionPaoliCorse/ConstitutionPaoliCorse_djvu.txt`. L'accès fonctionne par le serveur Archive `d1`, malgré les redirections infructueuses de `archive.org/download` ; cela constitue un succès de récupération, **pas encore une lecture paléographique du fac-similé**.

L'inspection effective du fichier révèle que l'**Appendice I** est à l'offset caractères **249 304–256 800 environ** (texte UTF-8 décodé), du titre « Résolution votée par la Consulte de Corte des 16, 17 et 18 novembre 1755 » jusqu'à « APPENDICE II ». **FBF** : le premier script d'extraction a choisi le **dernier** mot « Appendices », présent dans la table des matières, et a donc produit un extrait de 1 008 octets **erroné** ; **l'OCR complet, lui, est correct et préservé**. Le passage réel a été inspecté depuis l'artefact téléchargé.

- À l'offset ~249 400, la traduction française commence « La Diète générale, représentant le peuple de la Corse » ; il faut signaler ses corruptions OCR (`sei»l`, `uiéme`) plutôt que les reproduire comme graphie éditoriale.
- À l'offset ~253 300, une note commence par l'italien, mais OCR gravement bruité : `La bieU générale rap présentante il popolo dî Gorsica, unico padrone di se medesimo`. Le sens et la correspondance avec les citations de Carrington peuvent être étudiés, mais **les graphies exactes exigent l'image imprimée**.
- À ~252 700 et ~256 400, passage de la Diète annuelle et de la reddition de comptes, dans les versions française et italienne : occurrence des obligations du Général et du `sindicato` des quatre personnes.

**Prochaine dépendance précise :** retrouver les pages-images correspondant aux pages imprimées **161–164** (index `_page_numbers.json` + serveur Archive) et y contrôler la ponctuation ainsi que les graphies. L'exemplaire R1900 reste une branche indépendante non récupérée. Statut : `F1907_OCR_acquired`, `F1907_facsimile_not_yet_verified`, `R1900_not_acquired`.

## FBF — collation sur fac-similé réellement inspecté (13 octobre 2026)

**Acquisition vérifiée :** [reçu de transfert PDF](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6154689992), fichier PDF de Fontana de 196 pages, 46 610 597 octets, SHA-256 `ea63cb0d49d6f0a9592da33d548e8374307b3f82622500410558c268a4085e3e`. Les **pages PDF 177–180** correspondent exactement à **l'Appendice I**, pages imprimées **161–164** ; les images ont été rendues localement et vues directement. Les fichiers `_page_numbers.json` et `_scandata.xml` ont leurs champs de numéro de page vides et ne permettaient pas cette identification : c'est la localisation dans le PDF qui la prouve. Le PDF isolé de ces quatre pages est un **extrait dérivé** non versionné, le fac-similé original étant ancré par sa somme.

**Correction substantielle à l'appareil A-001, sur la page imprimée 163 / PDF 179 :** la note italienne de Fontana commence (lecture visuelle de l'imprimé) :

> « La Dieta generale rappresentante il popolo di Corsica, unico padrone di se medesimo, legittimamente e secondo le forme dal generale convocata nella città di Corti [...] »

La graphie des derniers mots et la transcription complète demandent une deuxième lecture ; **les termes `unico padrone` ET `legittimamente` sont tous deux présents dans F1907**. La matrice précédente « `unico padrone` (Fontana) contre `Lecitimamente Patrone` (manuscrit cité par Carrington) » **suggérait à tort une exclusion de la légitimité dans Fontana**, en tronquant sa phrase. Il faut comparer les **énoncés complets**, leur syntaxe et la position de `legittimamente`, plutôt que deux fragments isolés : dans F1907, `legittimamente` se rattache prima facie à la convocation de la Diète, pas nécessairement à la qualité de propriétaire. La lecture de Carrington reste **une citation publiée d'un manuscrit, non un fac-similé manuscrit inspecté**.

La traduction française commence bien page imprimée 161 « La Diète générale, représentant le peuple de la Corse, seul maître de lui-même ». Page imprimée 163, Fontana prévoit la reddition annuelle de comptes du Général et le contrôle des autres magistrats par un sindicat de quatre citoyens ; page 164, la note italienne énonce `ogni magistrato ed ufficiale della Nazione sarà tenuto dar conto della sua condotta` (lecture à recontrôler sur scan haute résolution avant édition diplomatique).

**État de preuve :** `F1907_facsimile_inspected = true` (quatre pages), `F1907_comparison_text_partial = true`, `R1900_facsimile_inspected = false`, `M1755_manuscript_inspected = false`. Ne pas présenter les variantes de graphies OCR comme des différences historiques prouvées.

## Fac-similé Fontana acquis et contrôlé — 14 octobre 2026

**Provenance vérifiable :** [Inseme #120 reçu PDF](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6154689992), run `38464048114`. PDF entier de Fontana 1907, 46 610 597 octets, SHA-256 `ea63cb0d49d6f0a9592da33d548e8374307b3f82622500410558c268a4085e3e`. La conversion locale a identifié et inspecté les **pages PDF 177–180 = pages imprimées 161–164**, appendice I ; quatre images locales réalisées et assemblage des quatre pages en PDF de travail. L'index Archive `_page_numbers.json` est vide pour `pageNumber`, d'où la vérification par le PDF lui-même. Le premier essai de rendu distant a échoué car les programmes Poppler n'y étaient pas installés ; cela n'invalide pas l'acquisition du fichier.

**Contrôle direct du préambule italien :** page imprimée **163**, note (1), l'édition Fontana porte : `La Dieta generale rappresentante il popolo di Corsica, unico padrone di se medesimo, legittimamente e secondo le forme dal generale convocata nella città di Corti sotto li giorni 16, 17, 18 di novembre` (ponctuation/graphies terminales à confronter au tirage haute résolution avant citation diplomatique intégrale). Les segments `rappresentante il popolo di Corsica` et `unico padrone di se medesimo` sont **directement visibles**, et non des reconstructions de l'OCR. Le français à la p. 161 commence `La Diète générale, représentant le peuple de la Corse, seul maître de lui-même`.

**Statut critique :** témoin éditorial Fontana/Rossi en lecture directe acquise ; le manuscrit cité par Carrington est **distinct dans son texte** et reste une citation indirecte ici. Le Rossi imprimé en 1900 n'est pas encore vérifié de première main : ne pas assimiler automatiquement l'impression de Fontana à une copie diplomatique de Rossi. La différence `rappresentante il popolo / del Populo` reste à attribuer par collation des témoins.
