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
| R1900 | Ambrogio Rossi, *Osservazioni storiche*, livre X, BSSHNC, fasc. 237–240 (1900), p. 136–141 | [Notice BnF](https://catalogue.bnf.fr/ark:/12148/cb31248785r), ARK Gallica `bpt6k4801726` non vérifié ; [notice Geneanet livre X](https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron) | Livre X identifié ; pages 136–141 non acquises, aucune collation directe |
| F1907 | Matthieu Fontana, *La constitution du généralat de Pascal Paoli*, appendice I, p. 161–164 | [Internet Archive](https://archive.org/details/ConstitutionPaoliCorse), [OCR](https://archive.org/stream/ConstitutionPaoliCorse/ConstitutionPaoliCorse_djvu.txt) | OCR et fac-similés p. 161–164 acquis et contrôlés ; collation avec Rossi encore ouverte |
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

## Rossi 1900 — localisation bibliographique renforcée (14 octobre 2026)

**Livre identifié sans ambiguïté dans les catalogues** : Ambrogio Rossi, *Osservazioni storiche sopra la Corsica*, livre X (1752–1760), publié par Lucien-Auguste Letteron, dans *Bulletin de la Société des sciences historiques et naturelles de la Corse*, 20e année, fascicules 237–240 (septembre–décembre 1900). Table du catalogue de la Société : volume (99), 365 pages. Bibliographie Carrington 1974 : texte relatif à 1755 aux **pages 136–141**.

Sources de contrôle : [catalogue BnF de Rossi](https://catalogue.bnf.fr/ark:/12148/cb31248785r), [catalogue de la Société](https://www.societesciencescorse.fr/lecatalogue/), [Carrington 1974 sur Persée](https://www.persee.fr/doc/ahrf_0003-4436_1974_num_218_1_4183).

La notice BnF détaille les 13 volumes numériques et le **volume 6** correspond au *Livre X* ; les volumes voisins sont associés à `NUMM-480183` (livre IX) et `NUMM-480173` (livre XI). **`NUMM-480172` / `bpt6k4801726` reste l'identifiant candidat** tant que la correspondance n'a pas été confirmée sur la notice détaillée ou par lecture de la page de titre. La notice indique bien une numérisation Gallica, mais **aucune page de Rossi n'a encore été effectivement téléchargée et collationnée**.

**Action suivante** : confirmer l'ARK numérique du sixième exemplaire, puis récupérer uniquement les images des pages imprimées 136–141. Ne pas confondre ce témoin avec une deuxième numérisation Fontana (`IA41555227_0091`).

## Rossi livre X — nouvelle piste de consultation (14 octobre 2026)

Une notice dédiée existe dans la [Bibliothèque Geneanet, document 4846194](https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron) : *Osservazioni storiche sopra la Corsica. Livre X, 1752–1760*, Ambrogio Rossi, éd. Ollagnier (Bastia), 368 pages selon cet index. **L'accès aux pages est réservé aux abonnés Premium**, malgré la recherche publique et l'indexation des noms. Cette piste n'est donc pas assimilable à une acquisition libre ou à une collation directe. La [Société des sciences historiques et naturelles de la Corse](https://www.societesciencescorse.fr/lecatalogue/) confirme les fascicules 237–240 (1900) et une pagination de 365 pages : divergence de décompte à résoudre sur le fac-similé. La [notice BnF](https://catalogue.bnf.fr/ark:/12148/cb31248785r) atteste l'exemplaire physique du livre X, sans lien numérique individuel vérifié pour cette partie. Maintenir `R1900_source_identified`, `R1900_catalogue_available`, `R1900_pages_not_read`, et ne pas promouvoir un candidat ARK par analogie numérique. Chercher ensuite un exemplaire libre ou une consultation autorisée de ces six pages.

## Rossi X — nouveaux points d'accès (14 octobre 2026)

- [Geneanet, notice du livre X](https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron) : index nominatif et 368 pages annoncées, mais consultation réservée aux abonnés Premium. Identité bibliographique confirmée, provenance de la numérisation et accès aux pages 136–141 non vérifiés.
- [BnF, notice du périodique](https://catalogue.bnf.fr/ark:/12148/cb32724456z.public) : identifie explicitement une reproduction numérique dans la [Digital Cullezzione de l'Université de Corse](https://bucullezzione.univ-corse.fr/s/digital-cullezzione/item-set/2625), ainsi qu'un fonds HathiTrust. Ce sont des **pistes de recherche de la série**, non la preuve que le fascicule 237–240 y est accessible.
- [HathiTrust, série 008697237](https://catalog.hathitrust.org/Record/008697237) : liste des volumes consultables trouvés, mais **pas l'année 1900** dans les exemplaires affichés.

**État de preuve** : Rossi X attesté et indexé chez Geneanet ; numérisation libre des p. 136–141 toujours à identifier. Éviter de déduire la disponibilité d'un fascicule précis de la seule numérisation de sa série.

## Nouvelle piste vérifiable pour Rossi X — 14 octobre 2026

[Geneanet, document 4846194](https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron) catalogue séparément le livre X (1752–1760) de Rossi, édité par Letteron (Bastia, Ollagnier), avec **368 pages annoncées** et indexation de passages de l'ouvrage. Il s'agit d'une piste de numérisation/texte indexé **plus précise que l'ARK Gallica conjectural**, mais ni les images des pages 136–141 ni leur texte intégral n'ont été récupérés dans cette passe ; la consultation Geneanet peut nécessiter un abonnement Premium. Les [fascicules 237–240 (1900)](https://www.societesciencescorse.fr/lecatalogue/) et l'[exemplaire imprimé BnF du livre X](https://catalogue.bnf.fr/ark:/12148/cb31248785r) sont confirmés indépendamment. Une [notice de vente d'une collection complète](https://www.gazette-drouot.com/lots/18237129-bsshnc--rossi-ambrogio---osservazioni---) atteste une autre copie historique, mais pas un accès numérique aux pages.

**État de la branche** : `R1900_identified`, `R1900_independent_digital_index_found`, `R1900_pages_136_141_not_acquired`, `R1900_collation_not_started`. Première action suivante : déterminer si Geneanet donne un accès licite au fac-similé ou retrouver ce fascicule dans une collection numérisée libre ; à défaut demander une reproduction ciblée de six pages à une bibliothèque, sans déclencher de contact extérieur sans mandat spécifique.

## Rossi 1900 — piste Geneanet (14 octobre 2026)

Le catalogue de la Société identifie le volume (99), fascicules 237–240 (1900), livre X (1752–1760), pagination imprimée 1–365 : https://www.societesciencescorse.fr/lecatalogue/ . La notice BnF est https://catalogue.bnf.fr/ark:/12148/cb31248785r . Une **notice Geneanet spécifique au livre X** (368 pages annoncées, distincte de la série générale) offre « Consulter cet ouvrage » : https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron . C'est une piste d'accès plus précise que l'identifiant Gallica hypothétique ; **le fac-similé n'a pas encore été ouvert et ses pages 136–141 n'ont pas été inspectées**. La différence 365/368 pages reste non expliquée, possiblement liée au comptage de feuillets préliminaires. Ne pas inférer un témoin collationné à partir de la seule notice.

## Journal d'accessibilité documentaire — source de l'enquête (14 octobre 2026)

**Objet :** documenter non seulement la transmission du texte mais aussi les conditions observables d'accès aux témoins. Ce registre est une suite d'observations datées et situées, **pas** un jugement général sur un établissement ni une supposition sur la cause de l'obstacle. Pour chaque essai : objet et identifiant, URL, date, environnement/agent, opération, résultat HTTP ou erreur, artefact/reçu, possibilité effective de lire les pages, hypothèse de cause séparée, prochaine voie autorisée.

| Objet / tentative | Observation / preuve | Qualification |
|---|---|---|
| Fontana F1907, métadonnées Archive | API metadata HTTP 200, inventaire de PDF/OCR/JP2 ; [reçu COP](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6153617552) | Notice/fichiers annoncés, **pas encore accès au texte** lors de cette étape |
| Fontana, téléchargement standard | `archive.org/download` renvoie HTTP 302 vers un nœud CDN ; téléchargement `fetch` en échec dans un premier environnement | Échec **de ce chemin** ; ni document absent, ni interdiction générale |
| Fontana, serveur `d1` Archive | Requête directe au serveur indiqué par metadata, OCR complet 283 345 octets, puis PDF complet 46 610 597 octets ; [reçu OCR](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6153730287), [reçu PDF](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6154689992) | **Accès effectif acquis** et hash vérifiable |
| Fontana, pagination et rendu | `_page_numbers.json` contient 196 feuillets mais les `pageNumber` consultés sont vides ; extraction distante non réalisée faute d'outils Poppler ; rendu local possible, pages PDF 177–180 = imprimé 161–164 ; [diagnostic](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6154667505) | Limitation de métadonnées puis **capacité de l'environnement**, non indisponibilité de l'œuvre |
| Rossi R1900, référence bibliographique | [Catalogue de la Société](https://www.societesciencescorse.fr/lecatalogue/) : `(99) N° 237–240 (1900)`, *Osservazioni*, livre X, 365 p. ; [notice BnF](https://catalogue.bnf.fr/ark:/12148/cb31248785r) | **Existence bibliographique établie**, lecture directe non acquise |
| Rossi, accès numérique Gallica | Identifiant `bpt6k4801726` **candidat non vérifié** ; l'affichage consulté de la notice BnF ne donne pas de lien direct incontestable vers le livre X | **Localisation numérique inconnue** : absence de lien observé ≠ preuve d'absence de numérisation |
| Université de Corse, Digital Cullezzione | [Exemple de Bulletin historique numérisé (1918)](https://bucullezzione.univ-corse.fr/s/digital-cullezzione/item/2579), proposé comme PDF en domaine public | Canal alternatif **attesté**, présence du numéro 237–240 **non vérifiée** |

### Questions d'enquête

1. **Trouvabilité :** un lecteur qui dispose de la référence exacte du tome Rossi X peut-il découvrir un exemplaire numérique ? À quelles étapes échoue-t-il ?
2. **Accessibilité opérationnelle :** un objet signalé « numérisé » est-il effectivement lisible/téléchargeable, pour un navigateur ordinaire comme pour un agent outillé ? Séparer HTTP, redirection, identité, octets et lecture.
3. **Reproductibilité :** un autre handler peut-il refaire le parcours en suivant les références publiques, sans dépendre d'une conversation privée ?
4. **Effet documentaire :** quels témoins et variantes demeurent de fait invisibles lorsque l'accès ne fonctionne pas ? Ne pas déduire de cette invisibilité que le témoin n'existe pas.
5. **Canaux alternatifs :** vérifier les fonds de la Société, Digital Cullezzione, les bibliothèques et exemplaires physiques sans chercher à contourner des restrictions de service.

**Principe de la Calculette :** chaque obstacle observé est une trace et une dépendance de la recherche, pas un `branch_exhausted`. Sa résolution ultérieure **n'efface pas** la difficulté rencontrée : elle complète son histoire et permet d'étudier l'effectivité des canaux d'accès. Observation ≠ interprétation ≠ preuve d'intention ou de faute.

## Rossi 1900 — recherche indépendante du fascicule (14 octobre 2026)

Le [catalogue de la Société des sciences historiques et naturelles de la Corse](https://www.societesciencescorse.fr/lecatalogue/) confirme l'entrée **(99), fascicules 237–240, 1900, 365 pages**, constituée des *Osservazioni storiche sopra la Corsica*, livre X (1752–1760). La [notice BnF](https://catalogue.bnf.fr/ark:/12148/cb31248785r) confirme le sixième tome imprimé, coté `8-LC20-5 (6,1900)`, mais ne permet pas à elle seule d'établir un exemplaire numérique accessible de **ce tome précis**. Les voisins en ligne ne suffisent pas à l'identifier. Ne pas traiter `bpt6k4801726` comme confirmé sans inspection de sa page de titre.

La recherche indépendante porte sur le **fascicule complet** (ou volume n° 99) plutôt que sur un supposé ARK de monographie. Les résultats publics actuels confirment le catalogue, **pas encore une copie ouverte des pages 136–141**. Un [Packet de vérification des canaux Archive/BnF/Gallica](https://github.com/JeanHuguesRobert/inseme/issues/120#issuecomment-6161086564) est soumis ; attendre son reçu pour conclure sur la disponibilité effective.

Prochaine opération : à la première copie disponible, relever le titre et l'année dans le fac-similé, aligner la pagination imprimée 136–141, extraire les pages, puis collationner R1900 contre F1907 sans projeter les variantes antérieures comme attestées.

## Rossi 1900 — numérisation indépendante repérée (14 octobre 2026)

- [Geneanet, livre X, 1752–1760](https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron) : document numérisé identifié, 368 pages annoncées, index de noms avec fragments textuels ; **lecture intégrale réservée aux abonnés Premium**, pages 136–141 non consultées dans notre chaîne.
- [Catalogue historique de la Société des sciences historiques et naturelles de la Corse](https://www.societesciencescorse.fr/lecatalogue/) : volume n°99, fascicules 237–240 (1900), Rossi livre X, pages 1–365 ; écart de décompte avec Geneanet (368 pages) à ne pas interpréter sans voir les pages liminaires.
- [Collection numérisée BU Università di Corsica](https://bucullezzione.univ-corse.fr/s/digital-cullezzione/item-set/1586) : plusieurs numéros accessibles, mais le n°237–240 ne figurait pas dans le lot visible consulté ; cela ne démontre pas son absence de leurs collections.

**Statut précis** : `R1900_digitization_identified`; `R1900_fulltext_not_accessible_in_current_scope`; `R1900_p136_141_not_verified`. Ne pas inférer un accès intégral depuis les snippets d'indexation ni reprendre une graphie italienne de Rossi sans image. Prochaine action : rechercher un exemplaire ouvert ou solliciter une reproduction des six pages par les détenteurs autorisés (aucun courrier envoyé).

## Rossi X — nouvel accès candidat (14 octobre 2026)

La bibliothèque Geneanet propose une notice spécifique pour le *Livre X, 1752-1760* (Ambrogio Rossi, Ollagnier, Bastia), sous l'identifiant de document `4846194`, avec 368 pages annoncées et des extraits indexés : https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbate-ambrogio-rossi-publie-par-m-l-abbe-letteron . Le catalogue de la Société confirme le volume 99 du *Bulletin*, fascicules 237-240 (1900), pagination 1-365 : https://www.societesciencescorse.fr/lecatalogue/ . **Statut : identification bibliographique et indexation numérique établies, pages 136-141 non lues directement**, accès complet et droits de consultation restant à vérifier. Ne pas en déduire de variantes textuelles par rapport à Fontana avant collation.

## Rossi 1900 — point d'étape critique (14 octobre 2026)

La [Société des sciences historiques et naturelles de la Corse](https://www.societesciencescorse.fr/lecatalogue/) identifie **sans ambiguïté** son volume bibliographique **(99), fascicules 237–240 (1900)**, *Osservazioni storiche sopra la Corsica*, **livre X (1752–1760)**, 365 pages. La [notice BnF cb31248785r](https://catalogue.bnf.fr/ark:/12148/cb31248785r) confirme l'auteur Ambrogio Rossi, l'éditeur scientifique Letteron et l'édition de septembre–décembre 1900. Une notice imprimée attestée **ne suffit pas à établir qu'un fac-similé de ce tome est accessible** ; l'identifiant numérique `bpt6k4801726` reste hypothétique et aucune lecture directe des pages Rossi n'est acquise.

**Point de contrôle supplémentaire :** Fabrizio Dal Passo, *Il Mediterraneo dei Lumi*, [PDF de recherche](https://www.stmoderna.it/uploads/pubblicazioni/878/14.MEDITERRANEODEILUMI6.pdf), renvoie à Rossi livre X **p. 124–126** pour « il testo della Consulta ». Ce renvoi ne doit pas être confondu sans vérification avec les **p. 136–141** indiquées dans le dossier pour le document constitutionnel de novembre. Les deux emplacements sont **à contrôler séparément** sur l'exemplaire R1900 : correspondance, complément ou autre texte, non déterminé.

**Question historique gouvernante :** attribuer la divergence entre F1907 (« rappresentante il popolo ») et le témoin manuscrit cité par Carrington (« del Populo »). L'absence de R1900 bloque cette **attribution**, mais pas le reste de la recherche. Prochaine action ciblée : obtenir les pages imprimées 124–126 **et** 136–141, identifier exactement leur statut dans l'édition, puis aligner les témoins ; ne jamais promouvoir une hypothèse de filiation éditoriale en certitude.

## Nouvelle piste indépendante R1900 — 14 octobre 2026

Une [notice Geneanet propre au Livre X de Rossi](https://www.geneanet.org/bibliotheque-genealogie/doc/4846194/osservazioni-storiche-sopra-la-corsica-livre-x-1752-1760-dell-abbe-ambrogio-rossi-publie-par-m-l-abbe-letteron) signale une copie numérisée de 368 pages, avec indexation de noms ; consultation intégrale réservée aux abonnés Premium. Le témoin bibliographique est donc identifié hors Gallica, mais **les pages 136–141 ne sont pas lues ni acquises**. La [BnF](https://catalogue.bnf.fr/ark:/12148/cb31248785r) et le [catalogue de la Société](https://www.societesciencescorse.fr/lecatalogue/) confirment indépendamment le livre X (fasc. 237–240, 1900). Cette copie ne doit pas être confondue avec les deux numérisations de Fontana.

Prochaine dépendance : vérifier si la société savante ou une bibliothèque détient une copie numérisée librement consultable ; à défaut, préparer une demande précise de reproduction des six pages. Toute citation Rossi demeure indirecte tant que les pages ne sont pas consultées.
