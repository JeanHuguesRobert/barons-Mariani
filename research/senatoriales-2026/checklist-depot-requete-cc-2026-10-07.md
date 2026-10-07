---
title: "Checklist agile — dépôt de la requête au Conseil constitutionnel"
subtitle: "Sénatoriales Haute-Corse 2026 — contrôle pré-dépôt et points découverts en chemin"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
version: "0.13"
status: "active — living checklist"
language: "fr"
document_role: "operational"
document_kind: "legal-filing-checklist"
document_function: "pre-filing-control"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
related:
  - "requete-conseil-constitutionnel-projet-v0.17.md"
  - "bordereau-pieces-requete-conseil-constitutionnel-v0.9.md"
  - "investigation/architecture-recours-cc-cedh-remedes-2026-10-05.md"
  - "qpc/qpc-a-candidature-senatoriale-2026.md"
  - "investigation/precedents_contentieux_et_couverture_medias_2017_2020_2024_2026.md"
  - "pre-filing-operational-plan-2026-10-07.md"
  - "matrice-canaux-materiels-depot-2026-10-07.md"
  - "filing-package-manifest-2026-10-07.md"
  - "fiche-remise-requete-cc-2026-10-07.md"
  - "../reviews/review_internal_requete_cc_motifs_rejet_2026-10-06.md"
  - "../autonomia/corse_laboratoire.md"
  - "../autonomia/amendement_effectivite_article_72-5.md"
---

# Checklist agile — dépôt de la requête au Conseil constitutionnel

## Règle d'usage

Cette checklist est **vivante** jusqu'au dépôt.

Tout point nouveau rencontré en cours de préparation qui peut matériellement changer la recevabilité, un moyen, une pièce, une conclusion, une voie parallèle, un délai, un remède ou la capacité de vérification doit être ajouté immédiatement ici, puis relié au document concerné.

Principe :

```text
NEW TRACE / NEW OBJECTION / NEW REMEDY / NEW DEADLINE
→ est-ce matériel pour le dépôt ?
→ oui : ajouter à la checklist
→ qualifier : MUST BEFORE FILING | SHOULD BEFORE FILING | POST-FILING
→ relier au document / pièce / source
→ fermer seulement après vérification
```

Ne pas attendre une "version finale" pour enregistrer un point utile.

### Standard probatoire — niveau maximal raisonnablement atteignable

Le dossier vise, pour chaque fait matériel important, le **plus haut niveau de preuve raisonnablement accessible**, avec une méthode proche de celle d'un enquêteur judiciaire particulièrement scrupuleux et conscient des risques de falsification, d'altération, d'usurpation et d'attaque informatique.

Conséquences pratiques :

- privilégier les **traces primaires et vérifiables** plutôt que les souvenirs, reconstructions ou affirmations non corroborées ;
- conserver l'**original natif** chaque fois qu'il existe, sans le remplacer par une capture ou une transcription ;
- calculer et conserver une **empreinte cryptographique forte (SHA-256 au minimum)** de tout fichier produit ou référencé ;
- documenter autant que possible la **provenance**, la date, le canal d'acquisition, la chaîne de conservation et toute transformation effectuée ;
- distinguer strictement **original / copie / photographie / capture / export / transcription / reconstruction** ;
- rechercher des **corroborations indépendantes** : métadonnées, journaux, accusés, traces serveur, historiques, pièces postales, chronologies, témoins ou systèmes tiers ;
- ne jamais présenter comme certain ce qui n'est qu'inféré ; qualifier explicitement les niveaux : **établi / fortement corroboré / plausible / non établi** ;
- pour les éléments numériques sensibles, raisonner comme si une contestation d'authenticité ou une cyberattaque devait être examinée : intégrité, horodatage, identité de la source, continuité de la conservation, cohérence inter-traces et possibilité d'une vérification indépendante ;
- lorsqu'une preuve plus forte est raisonnablement accessible, ne pas se satisfaire d'une preuve plus faible par commodité.

Ce standard n'impose pas une preuve impossible : il impose de pouvoir expliquer **pourquoi le niveau produit est le meilleur niveau raisonnablement atteignable** au moment du dépôt.

### Invariant d'autonomie du dossier et des pièces

Le dossier remis au Conseil doit être **autoportant**. Un juriste ne doit jamais avoir à connaître le Corpus, une conversation passée, un dépôt GitHub, un courriel non produit ou une convention interne pour comprendre une affirmation, une pièce ou un raisonnement.

Règle impérative :

```text
TOUTE CHOSE INVOQUÉE
→ doit être définie avant usage ;
→ son rôle dans le raisonnement doit être explicite ;
→ si elle est matériellement utile, elle doit être produite dans le dossier final ;
→ si l'incorporation est impraticable, fournir un accès Internet stable et vérifié,
   accompagné d'une empreinte forte (SHA-256 au minimum), d'une date de gel,
   d'une description suffisante et, si nécessaire, d'une transcription ou extraction lisible ;
→ aucune référence orpheline à "le Corpus", "la vidéo", "le mail", "le document",
   "l'annexe" ou à toute notion interne non définie n'est admise.
```

Pour **chaque pièce**, le contrôle pré-dépôt doit permettre de retrouver au minimum : **numéro**, **intitulé bref**, **date**, **origine/provenance**, **description matérielle**, **fait(s) qu'elle établit ou éclaire**, **place dans le raisonnement**, **fichier(s) exact(s)**, **mode de production** (embarqué / annexe / lien externe), **URL vérifiée le cas échéant**, **SHA-256**, **statut de vérification**, **lisibilité**, **éventuelle transcription**, **éventuelle occultation/minimisation**, et **présence effective dans le paquet remis**.

## A. MUST BEFORE FILING

- [x] **Délai** — échéance légale vérifiée : **7 octobre 2026 à 18 h** (art. 33 de l’ordonnance du 7 novembre 1958).
- [~] **Version canonique de dépôt** — la v0.17 est le brouillon courant ; la version réellement déposée devra être explicitement figée et tracée au moment du dépôt.
- [x] **Premier écran contentieux** — juridiction, requérant, qualité pour agir, élection contestée, décision initiale, délai, griefs et conclusions sont explicités dans la v0.17.
- [x] **Forclusion des griefs nouveaux** — point load-bearing : tous les moyens matériels doivent être contenus en substance dans la requête initiale. Décision n° 2024-6345/6354/6370 AN/QPC : un grief présenté pour la première fois après le délai de l’article 33 est irrecevable.
- [x] **Article 35 : pièces, pas réserve générale de moyens** — le Conseil peut exceptionnellement accorder un délai pour une partie des pièces ; ne pas compter sur cette faculté pour créer un grief nouveau après 18 h.
- [~] **Canal de dépôt — article 34** — règle juridique vérifiée : requête écrite au secrétariat général du Conseil constitutionnel ou au représentant de l’État. La matrice `matrice-canaux-materiels-depot-2026-10-07.md` distingue désormais destinataire juridique, modalité matérielle, preuve et risque. L’acte matériel de remise reste à accomplir. Ne pas compter sur un simple courriel du requérant comme canal acquis.
- [ ] **Redondance matérielle du dépôt — même paquet, plusieurs voies** — mobiliser autant que raisonnablement possible plusieurs voies indépendantes **du même paquet gelé** : au minimum remise physique au représentant de l’État à Bastia ; si possible remise directe d’un exemplaire strictement identique au secrétariat général du Conseil constitutionnel à Paris par porteur/coursier ; envisager un commissaire de justice comme renfort probatoire de remise. Chaque voie doit produire sa propre preuve datée et horodatée.
- [ ] **Anti-divergence entre dépôts redondants** — avant toute remise multiple, figer une seule requête canonique, un seul bordereau et un seul jeu de pièces ; calculer les SHA-256 et identifier les exemplaires physiques. Interdiction de déposer silencieusement des versions différentes par des canaux parallèles. Une correction postérieure devient un objet distinct et explicitement daté.
- [ ] **Réception avant délai ≠ expédition avant délai** — pour tout canal postal, express ou coursier, exiger une preuve de **réception** avant l’échéance ; ne pas considérer le cachet d’expédition comme filet suffisant. Jurisprudence de contrôle : décisions 2017-5267 QPC/SEN et 2017-5256 QPC/AN.
- [ ] **Préfecture Bastia — sécuriser l’accès pratique** — l’accueil public ordinaire publié est 8 h 30–11 h 30 et 13 h 30–15 h 30, sur rendez-vous. Confirmer dès l’ouverture le service concret receveur, l’accès et la possibilité d’obtenir récépissé/cachet avec heure ; viser une remise très antérieure à 15 h 30, sans organiser le dépôt autour de 18 h.
- [ ] **Conseil constitutionnel — remise directe à Paris** — confirmer dès l’ouverture les modalités pratiques de réception d’une requête électorale au secrétariat général, 2 rue de Montpensier, et, si une personne/coursier est mobilisable à Paris, lui transmettre un exemplaire strictement identique avec instruction d’obtenir une preuve de remise datée et horodatée.
- [ ] **Sous-préfecture de Corte — ne pas présumer l’habilitation** — aucune source examinée ne suffit à établir qu’une remise à la sous-préfecture vaut à elle seule saisine du « représentant de l’État » au sens de l’article 34. Ne compter cette voie qu’après confirmation explicite qu’elle reçoit la requête pour le compte du représentant de l’État ; sinon la traiter comme tentative/trace complémentaire.
- [ ] **Courriel / télécopie — copie de traçabilité seulement** — sauf confirmation institutionnelle expresse d’un mode de saisine électronique, ne jamais utiliser courriel ou fax comme seul dépôt. Une copie numérique peut être envoyée parallèlement ou après la remise matérielle, clairement étiquetée comme copie de traçabilité ne se substituant pas au dépôt article 34.
- [ ] **Gel pré-dépôt** — une fois la dernière revue terminée : figer SHA/version, PDF ou exemplaire réellement remis, bordereau et pièces ; toute correction ultérieure doit devenir explicitement postérieure au dépôt.
- [x] **Fondement du recours** — articulation stabilisée : Constitution art. 59 / ordonnance de 1958 / code électoral, notamment L.303.
- [ ] **Bordereau autonome** — vérifier que le bordereau de pièces correspond exactement aux pièces effectivement jointes et à leur numérotation.
- [ ] **Registre probatoire autoportant pièce par pièce** — pour chaque P-xx (et chaque sous-pièce d'un ensemble composite), contrôler numéro, titre, date, provenance, description, rôle probatoire/argumentatif, fichier source, URL éventuelle, empreinte SHA-256, transcription si utile, confidentialité/occultation, et présence effective dans le paquet final. Une référence externe ne remplace jamais une définition suffisante dans la requête ou le bordereau.
- [ ] **Pièces composites — sous-numérotation stable** — lorsqu'une même séquence probatoire comporte plusieurs objets matériels distincts (avis postal, enveloppe, page de notification, jugement, photographie contextuelle, recto/verso, transcription), conserver le numéro principal mais attribuer des sous-identifiants stables (ex. P-20.a, P-20.b…) afin qu'une citation pointe vers un objet précis sans renumérotation globale du dossier.
- [ ] **Pièces critiques** — vérifier présence, lisibilité, date, origine et concordance des pièces relatives au dépôt de candidature, aux formalités de la remplaçante, au TA, aux échanges préfectoraux et au scrutin.
- [ ] **P-09 — récépissé provisoire : scan + transcription textuelle** — joindre au paquet remis le scan/reproduction lisible du récépissé provisoire délivré le **11 septembre 2026 à 12 h 20** et une transcription textuelle fidèle de tous les champs lisibles. La transcription déjà conservée dans le Corpus peut servir de base, mais la version de dépôt doit être contrôlée ligne à ligne contre l'image primaire ; signaler explicitement toute mention illisible, anomalie ou lacune au lieu de la compléter par inférence.
- [ ] **P-17 — note manuscrite recto-verso remise à l'audience : scan + transcription textuelle** — joindre la reproduction recto-verso de la feuille manuscrite remise en main propre au début de l'audience du **14 septembre 2026**, ainsi qu'une transcription textuelle fidèle. Le texte avait été dicté dans une conversation contemporaine, mais le libellé exact doit être récupéré ou vérifié contre le scan : **ne pas reconstruire silencieusement de mémoire**. Cette pièce doit être traitée comme une production autonome de l'audience et reliée à la chronologie et au bordereau.
- [ ] **P-17 — granularité matérielle** — distinguer au minimum le recto, le verso et la transcription vérifiée comme trois objets identifiables sous un même numéro principal ; préciser pour chacun le fichier exact et son SHA-256. La transcription est un dérivé de lecture ; les images du manuscrit restent les pièces primaires.
- [x] **P-14 — deux requêtes préfectorales retrouvées et comparées** — les bundles `2601714` et `2601715` contiennent une saisine signée de trois pages au même contenu substantiel ; leur position dans les bundles diffère. Ne pas parler d'identité binaire des PDF complets sans comparaison de fichiers.
- [x] **P-14 — distinction L.298 / L.299 dans la saisine** — l'exposé des faits rappelle **L.298 et L.299** ; la partie « Discussion » reproduit et développe expressément **L.299** pour l'exigence d'« original », sans développement autonome de L.298.
- [x] **e-Sagace — sens des conclusions** — les deux dossiers affichent un refus pour méconnaissance alléguée de **L.298, L.299 et L.301**. Qualifier correctement : il s'agit du sens des conclusions, pas du jugement.
- [ ] **Jugement primaire — contrôle L.298 / L.299 / L.301** — relire ligne à ligne l'expédition primaire P-20 et enregistrer exactement les dispositions visées et développées. Si L.298 est absent de la motivation alors qu'il figure dans le sens des conclusions e-Sagace, décrire cette différence sans en déduire automatiquement qu'un moyen aurait été ignoré.
- [ ] **P-20 — chaîne matérielle de notification du jugement du 14 septembre** — traiter séparément, sous P-20 avec sous-identifiants stables, (a) l'avis de passage / notification trouvé dans la boîte aux lettres, (b) l'enveloppe ou pli recommandé retiré à La Poste et les éléments permettant d'en rattacher le retrait au lieu et à la date, y compris la photographie de la plaque « Avenue du Baron Mariani » si elle est utile et datable, (c) la page de notification du greffe, (d) les trois pages du jugement. Pour chaque élément : fichier exact, date/provenance, SHA-256, lisibilité et fonction probatoire. Ne pas présenter une photographie comme horodatée si ses métadonnées ou une autre trace indépendante ne l'établissent pas.
- [x] **P-44 — chaîne France Transfert retrouvée** — deux courriels reçus le 11 septembre à **18 h 45 min 53 s** : avis de pli provenant du greffe et mot de passe transmis séparément. Le premier annonce les quatre fichiers (deux CRAASE + deux PDF préfectoraux). Mot de passe et liens non publiés.
- [ ] **P-44 — pièce à matérialiser pour le dépôt** — joindre au paquet Conseil une copie des deux courriels France Transfert établissant la provenance de P-14, en masquant mot de passe, lien et jetons inutiles ; conserver les originaux natifs disponibles pour vérification.
- [x] **Influence sur le scrutin** — la requête distingue clairement :
  - l'écart entre candidats présents ;
  - la distance à la majorité absolue ;
  - la borne contrefactuelle ;
  - les comparaisons 2A/2B comme ordres de grandeur, non comme transferts de voix.
- [x] **22–29 % / 33 %** — pourcentages entiers dans le framing public et la démonstration principale ; valeurs exactes et dénominateurs conservés dans la couche de vérification.
- [x] **A Voce** — nature politique de l’offre 2026 intégrée et sourcée ; ne pas réduire 2026 à une répétition mécanique de la candidature de 2020.
- [x] **"Acqua in bocca" / soutien public ≠ vote réel** — intégré comme problème d’inférence électorale, non comme essence culturelle : base institutionnelle minimale identifiable d’environ **1 % (5 grands électeurs)** contre **14 % (88 voix)** au résultat, sans attribution individuelle des bulletins.
- [x] **Déclarations publiques / commentaires de presse — P-41** — principales sources et bornes revérifiées ; conserver comme **B — soutien / réserve**, non comme pièce du noyau à joindre par défaut. Les formulations adverses restent conservées ; aucune intention rapportée ni appartenance institutionnelle n’est transformée en bulletin secret.
- [x] **Bulletin nul "BARON MARIANI"** — statut borné dans la v0.14 et le bordereau : trace matérielle d'une offre absente ; ni suffrage valide, ni identification certaine d'un électeur, ni preuve autonome d'influence déterminante.
- [x] **Conclusions** — la v0.14 distingue annulation comme conclusion principale, mesures d’instruction subsidiaires et proclamation directe comme conclusion infiniment subsidiaire / probe exploratoire.
- [x] **Effet de l’annulation — LO 322** — v0.14 corrigée : demander l’annulation comme remède principal et demander au Conseil d’en tirer les conséquences légales ; LO 322 prévoit l’élection partielle dans les trois mois.
- [x] **Remède extrême** — décision explicite : la proclamation directe est conservée comme conclusion infiniment subsidiaire et probe exploratoire ; elle n’est pas présentée comme le remède normalement disponible.
- [~] **QPC** — correction procédurale acquise : une QPC peut être posée directement au Conseil constitutionnel dans le contentieux électoral parlementaire. Reste à cristalliser séparément chaque mémoire : disposition législative précise, applicabilité au litige, droit/liberté garanti, nouveauté/sérieux. QPC A : L.299 est le premier candidat à tester. QPC B reste ouverte faute de disposition législative applicable identifiée.
- [~] **Kill-switch QPC** — ne pas faire du nombre de QPC un objectif. QPC A n’est déposée que si le grief attaque réellement L.299 lui-même et satisfait les conditions organiques ; QPC B reste hors dépôt si aucune disposition législative applicable et question sérieuse ne sont stabilisées.
- [x] **Défenseur des droits** — saisine maintenue distincte du recours CC ; aucun effet suspensif sur les délais ne lui est attribué.
- [x] **Trace Défenseur des droits — P-42** — saisine du 26 septembre vérifiée dans Gmail ; déléguée mise en copie les 1er et 2 octobre ; aucune réponse provenant de son adresse retrouvée dans la recherche ciblée au 6 octobre. Ne pas écrire « aucune réponse n'existe », mais « aucune réponse retrouvée ».
- [ ] **Corpus complet des courriels** — conserver et indexer tous les courriels matériellement pertinents avec préfecture, TA, Défenseur des droits, remplaçante et autres acteurs ; distinguer **complétude de conservation** et **sélectivité de production au Conseil**.
- [~] **Minute du jugement / demandes réitérées au TA — P-21, P-29 à P-33** — chaîne documentaire matérialisée dans `investigation/chaine-ta-p29-p33-2026-10-06.md`, avec séparation demande/réponse/inconnu. Reste à vérifier que les courriels natifs P-29 à P-33 sont effectivement présents et lisibles dans le paquet matériel remis ; l’index ne les remplace pas.
- [x] **Correspondance Laurence — P-43** — index vérifié créé à partir de Gmail ; messages décisifs identifiés (préparation, identité, autorisation expresse, porte-parole, vidéo, AAH). Ne pas republier dans GitHub le contenu privé intégral ; produire au Conseil seulement ce qui est nécessaire, avec minimisation.
- [ ] **Diligence Bastia → Ajaccio du 11 septembre** — documenter explicitement la séquence matérielle après le dépôt physique à Bastia : déplacement du candidat jusqu’à Ajaccio pour rejoindre Mme Vernerey et enregistrer avec elle, avant 18 h, une déclaration vidéo commune. Vérifier et relier les traces disponibles du déplacement et de l’horaire ; ne pas réduire cette diligence à la simple existence abstraite d’une « vidéo ».
- [ ] **Vidéo P-13 — texte exact lu en commun** — retrouver ou établir une transcription fidèle du texte effectivement lu par M. Robert et Mme Vernerey dans la prise continue du 11 septembre ; permettre au Conseil de lire immédiatement les affirmations d’identité, de volonté et de consentement sans dépendre du seul visionnage. Conserver la distinction : force probatoire du consentement ≠ substitution automatique aux formalités de L.299.
- [x] **P-12/P-13 — émission avant l’échéance** — courriel de transmission envoyé au Bureau des élections le 11 septembre à **17 h 57 min 55 s**, avec lien vers la déclaration vidéo commune ; l’inventaire initial P-14 ne mentionne ni P-11 ni P-12. Ne pas confondre émission établie avec réception par l’infrastructure de l’État ou versement au TA, qui restent des questions distinctes.
- [ ] **Chaîne de relances vidéo — 14–18 septembre** — faire apparaître dans la requête, pièces à l’appui, la continuité des démarches : **14/09 avant audience**, demande à la préfecture avec greffe en copie de faire verser le courriel/vidéo manquant ; **15/09**, trois questions factuelles (reçu avant 18 h ? transmis avec la saisine ? transmis ultérieurement ?) ; **16/09**, relance ; réponse Vidal ne répondant pas matériellement aux trois questions ; **17/09**, reformulation « oui / non / information non disponible » ; **18/09**, nouvelle relance constatant l’absence de réponse. Relier ensuite les demandes des 25/09, 01/10 et 02/10.
- [ ] **Vidéo — triptyque probatoire** — distinguer et documenter séparément : **(a) produite/envoyée**, **(b) reçue/versée au dossier**, **(c) effectivement examinée/visionnée**. À ce stade : (a) établi côté expéditeur ; (b) non établi pour P-12/P-13 ; (c) aucune trace institutionnelle identifiée. Ne jamais convertir l’absence de preuve de (b) ou (c) en preuve positive de non-transmission ou de non-examen.
- [ ] **Diligences maximales sur le consentement** — vérifier que la requête expose cumulativement, et non en fragments dispersés : autorisation écrite de Laurence, pièces d’identité et électorales, présence physique du candidat, déplacement pour rencontre physique commune, déclaration vidéo en prise continue, transmission avant 18 h, offre de visionnage au TA rapportée, puis production AAH. L’objet est de permettre au Conseil d’apprécier la réalité et l’intensité des garanties apportées sur l’authenticité du consentement.
- [ ] **Biais de cadrage / propagation de prémisse** — vérifier que la requête explique, sans psychologie attribuée aux personnes, le risque qu’une prémisse administrative globale (« originaux papier ») ait structuré l’examen juridictionnel au point de rendre périphériques les éléments dissonants : consentement documenté, handicap, présence physique du candidat, solutions praticables, vidéo et distinction L.298/L.299. Employer un vocabulaire de cadrage institutionnel / propagation de prémisse, pas un diagnostic cognitif individuel.
- [~] **Test de cohérence candidat / remplaçante** — isoler la question suivante : si la dématérialisation était en elle-même rédhibitoire, pourquoi distinguer le traitement du candidat physiquement présent et celui de la remplaçante absente, alors que la saisine mobilise spécialement L.299 ? Si le vrai nœud est l’acte personnel de la remplaçante, vérifier que handicap, consentement éclairé et CE 14 mai 2021, n° 445497 sont examinés explicitement.
- [x] **CEDH** — la v0.14 ne présente pas Strasbourg comme un appel du Conseil constitutionnel et conserve la logique recours internes pertinents → décision interne définitive → délai de quatre mois.
- [x] **Symétrie seulement conditionnelle** — la v0.14 explicite que Robert comme Parigi ne peuvent envisager Strasbourg qu’en qualité personnelle de victime d’un grief conventionnel défendable ; la fermeture de la voie interne ne crée pas à elle seule un droit à un examen au fond.
- [x] **2017 / 2024 / 2026** — répétition conservée comme contexte, connaissance institutionnelle et hypothèse de mécanisme récurrent ; **répétition ≠ situation continue** et ne rouvre pas, à elle seule, les délais expirés.
- [ ] **Qualité de victime CEDH — matrice Robert / Vernerey** — séparer les griefs directement subis par le candidat de ceux directement liés à la remplaçante et au handicap ; ne pas présumer qu’un requérant peut porter automatiquement le grief personnel de l’autre.
- [ ] **Comparatif média service public — 2017 / 2020 / 2024 / 2026** — inventorier, pour chacune des quatre candidatures, France 3 Corse ViaStella / France Télévisions et Radio France-ICI/RCFM : invitation ou non aux débats, entretiens, durée/format, date dans la campagne, présentation éditoriale, comparateurs parmi les autres petites candidatures ; distinguer trace d'absence de couverture, absence réellement vérifiée et refus explicite.
- [ ] **Comparatif média général — 2017 / 2020 / 2024 / 2026** — même grille pour Corse-Matin, Corse Net Infos, Alta Frequenza et autres médias significatifs ; comparer les petites candidatures entre elles, pas seulement aux favoris.
- [ ] **Forme et fond des quatre candidatures** — documenter séparément : titulaire/remplaçant, étiquette ou alliance, offre politique effectivement formulée, thèmes de fond, dispositif de campagne, originalités de forme, et manière dont les médias résument ou caricaturent éventuellement cette offre ; ne pas confondre ton éditorial et description du programme.
- [ ] **CSA / Arcom / juridictions — effectivité des recours** — tracer pour 2017 et 2024 les saisines, accusés, numéros, réponses de fond éventuelles et absence de suite retrouvée. État vérifié au 6 octobre : ticket CSA **227435** accusé le 7 juin 2017 ; alerte Arcom **807989** validée le 21 juin 2024 ; recherche ciblée actuelle sans réponse de fond retrouvée sous ces identifiants. Une absence de réponse retrouvée n'est pas encore une preuve d'absence absolue.
- [ ] **Hypothèse “décoratif vs effectif”** — ne pas l'énoncer comme fait global avant matrice comparative. Tester : droit formel d'être candidat / accès réel au débat / recours accessible / réponse obtenue / remède capable de réparer. Relier cette grille à l'amendement d'effectivité sans prétendre que le droit positif consacre déjà un principe général d'effectivité.
- [ ] **Corse laboratoire / expérimentation mesurée** — conserver l'ancrage historique vérifié : un rapport de l'Assemblée nationale qualifie explicitement 1982-1992 de « laboratoire institutionnel » et le statut de 1982 d'anticipation de la décentralisation ensuite étendue aux régions. Pour toute affirmation plus large (« nombreuses innovations généralisées »), exiger une série de cas documentés avant publication.
- [ ] **Droit positif de l'expérimentation** — rappeler que l'article 72 de la Constitution et les articles LO1113-1 s. CGCT organisent déjà des expérimentations territoriales bornées dans le temps et évaluées ; utiliser ce voisin juridique comme précédent de méthode, non comme validation automatique de l'amendement 72-5.
- [~] **Revue adverse finale** — passe interne corrélée « motifs de rejet » effectuée et archivée ; trois risques dominants : dépôt/preuve, L.299 + exception handicap, incidence sur le scrutin. Une revue externe décorrélée reste souhaitable si disponible mais ne doit pas retarder le dépôt.
- [x] **Précédent refus d’enregistrement — 2014-4909 SEN** — conserver le précédent direct : le Conseil, saisi de l’élection, a examiné un refus préfectoral d’enregistrement d’une candidature sénatoriale ; ne pas lui faire dire davantage sur le fond de 2026.
- [x] **Calendrier Sénat objectivé** — 7 octobre 15 h : audition de la ministre ; 21 octobre matin : réunion de la commission pour le rapport ; 26 octobre : discussion en séance publique. Utiliser ces dates pour la perte temporelle et une demande d’examen dans les meilleurs délais, sans inventer de procédure d’urgence.
- [ ] **Faits / hypothèses / arguments** — dernière passe de qualification : aucun élément rapporté ou inféré ne doit être promu silencieusement en fait acquis.
- [ ] **Intelligible par le grand public** — vérifier qu'un lecteur non juriste peut comprendre en une lecture : ce qui s'est passé, pourquoi cela compte, quel est le seuil ou l'ordre de grandeur pertinent, et ce qui est demandé au Conseil, sans devoir reconstruire l'argument à partir des annexes.
- [ ] **Intelligible par un juriste junior du Conseil constitutionnel** — vérifier qu'un juriste découvrant le dossier peut identifier immédiatement : compétence, recevabilité, faits matériels, griefs, normes invoquées, pièces utiles, démonstration d'influence, conclusions principales/subsidiaires et points restant incertains, sans connaissance préalable du Corpus.

## B. SHOULD BEFORE FILING

- [ ] **Architecture recours** — vérifier la cohérence entre requête, QPC, Défenseur des droits, éventuelle CEDH et probes de remèdes.
- [ ] **Synchronisation Suicide Corse n°4** — refléter les changements substantiels de la requête sans prétendre qu'un brouillon est déjà déposé.
- [ ] **Communication publique** — vérifier que les publications publiques restent compatibles avec la requête sans lui substituer une rhétorique différente sur les faits.
- [ ] **Ouverture assumée — texte à préserver sans altération** — si l'ouverture est retenue dans la requête ou dans une version publique associée, conserver exactement : **« Obtenir le respect, en Corse comme ailleurs, réclame d'en manifester ; le mépris appelle le mépris ».** Ne pas lisser cette phrase au nom d'une prudence stylistique ; contrôler seulement sa place, sa fonction et la transition immédiate vers les faits et le droit.
- [ ] **Style / panache sans perte probatoire** — le texte peut mobiliser avec parcimonie des références historiques, maximes et proverbes corses lorsqu'ils servent la compréhension ou la mémorisation. Chaque citation doit être soit vérifiée, soit explicitement présentée comme attribution traditionnelle. Éviter l'empilement décoratif : une référence doit porter une idée ou une transition, pas remplacer une démonstration.
- [ ] **Danton / audace** — si mobilisé, préférer la formulation historiquement attestée du discours du 2 septembre 1792 : « de l'audace, encore de l'audace, toujours de l'audace » ; l'utiliser comme signal de méthode ou de ton, non comme argument juridique.
- [ ] **Talleyrand / explicitation** — rappeler si utile la maxime traditionnellement attribuée à Talleyrand, « Ce qui va sans dire va encore mieux en le disant », comme principe de lisibilité : expliciter ce qui est décisif même si cela paraît évident.
- [ ] **Proverbes corses** — avant insertion, vérifier graphie, sens, source et adéquation au passage ; éviter toute formule dont le sens serait ambigu pour un lecteur non corsophone.
- [ ] **Framing** — appliquer la règle : fait fort → conséquence → borne ; éviter le defensive-first.
- [ ] **Estimations** — éviter les décimales dans le framing lorsqu'elles créent une fausse précision ; conserver l'exact dans les annexes.
- [ ] **Traçabilité** — conserver pour chaque nouvelle source le lien, la date, l'auteur, le statut de vérification et l'usage exact envisagé.

## C. CEDH — CHECKLIST DE PRÉSERVATION DU GRIEF

Ces points ne remplacent pas le dépôt au Conseil constitutionnel. Ils servent à éviter qu'une future voie européenne soit affaiblie aujourd'hui par omission.

### MUST BEFORE FILING AU CONSEIL CONSTITUTIONNEL

- [ ] **Soulever en substance le grief conventionnel pertinent** — faire apparaître dans la requête nationale, sans transformer celle-ci en requête CEDH, la substance du droit invoqué : droit de se porter candidat et effectivité du recours électoral au titre de l'article 3 du Protocole n° 1.
- [ ] **Ne pas surcharger l'article 13** — le traiter, s'il est maintenu, comme grief conventionnel distinct à vérifier ; ne pas supposer qu'il ajoute automatiquement une garantie autonome à celle que la jurisprudence déduit déjà de l'article 3 du Protocole n° 1.
- [ ] **Article 14 / handicap** — ne l'ouvrir que si le dossier permet d'identifier un traitement défavorable suffisamment rattachable à un critère protégé et au champ d'un droit conventionnel ; conserver séparément les faits d'accessibilité et la qualification de discrimination.
- [ ] **Applicabilité au Sénat** — documenter que l'article 3 du Protocole n° 1 couvre le choix de la législature et peut s'appliquer à une chambre haute disposant de pouvoirs législatifs ; ne pas traiter ce point comme acquis par simple analogie.
- [ ] **Épuisement utile** — identifier les recours internes **normaux et effectifs** pour chaque grief. Ne pas croire qu'une démarche extraordinaire, discrétionnaire ou dépourvue de pouvoir de redressement prolonge le délai de Strasbourg.
- [ ] **Défenseur des droits ≠ suspension du délai CEDH** — le mobiliser pour documenter, recommander, intervenir ou qualifier une difficulté ; ne jamais lui attribuer un effet interruptif ou suspensif sur le délai européen.
- [ ] **2017 / 2024** — les conserver comme contexte de répétition et éléments de connaissance institutionnelle ; ne pas les présenter comme rouvrant le délai de quatre mois d'une décision ancienne.
- [ ] **2024 hors délai autonome** — à défaut d'un fondement exceptionnel précis et vérifié, traiter la contestation autonome de la décision 2024 comme hors délai CEDH.
- [ ] **2026 : point de départ à calculer après la décision finale pertinente** — ne pas pré-calculer aujourd'hui une date de Strasbourg ; enregistrer exactement la date de la décision définitive et, le cas échéant, sa date de notification.
- [ ] **Formulaire complet** — rappeler que seul l'envoi d'une requête complète conforme aux exigences de la Cour interrompt le délai de quatre mois ; une lettre d'intention ou une démarche incomplète ne doit pas être utilisée comme filet de sécurité.
- [ ] **Même grief, même substance** — conserver la trace de l'endroit où chaque grief conventionnel a été soulevé devant le juge national afin de pouvoir démontrer l'épuisement.
- [ ] **Qualité de victime** — après décision nationale, vérifier séparément que le requérant demeure directement affecté par chaque violation alléguée et qu'aucun remède national n'a effacé cette qualité.
- [ ] **Remède demandé à Strasbourg** — ne pas présenter la CEDH comme pouvant "proclamer un sénateur". Distinguer constat de violation, satisfaction équitable éventuelle et mesures générales/individuelles relevant ensuite de l'exécution.
- [ ] **Réponse du Réel** — si Strasbourg rejette pour irrecevabilité, classer la cause exacte : délai, non-épuisement, incompatibilité ratione materiae/personae, défaut manifeste de fondement, absence de désavantage significatif, autre. Ne jamais convertir une irrecevabilité en validation du fond.

### POST-DÉCISION DU CONSEIL CONSTITUTIONNEL

- [ ] Geler immédiatement la décision, sa date de publication, sa date de notification éventuelle et le dossier national réellement examiné.
- [ ] Dresser une matrice **grief CEDH → fait → norme → endroit où le grief a été soulevé en France → réponse nationale → résidu**.
- [ ] Calculer le délai de quatre mois **par grief**, à partir de la décision finale pertinente dans le processus d'épuisement.
- [ ] Vérifier si un recours supplémentaire invoqué est réellement normal et effectif avant de considérer qu'il retarde le point de départ.
- [ ] Préparer le formulaire Rule 47 et les annexes suffisamment tôt pour qu'une requête complète parte avant l'échéance, sans compter sur un week-end ou un jour férié pour prolonger le délai.
- [ ] Séparer clairement : **2026 = objet potentiel de la requête** ; **2017/2024 = contexte, répétition, connaissance, éventuellement preuve de pattern**, sauf grief autonome encore recevable démontré.


## D. POST-FILING / NEXT REALITY TESTS

- [ ] Enregistrer la preuve du dépôt : date, heure, canal, récépissé / accusé, version exacte, liste exacte des pièces.
- [ ] Geler une copie forensique de la requête déposée et du bordereau.
- [ ] Distinguer toute version ultérieure de la version déposée.
- [ ] Suivre les mesures d'instruction, observations adverses et demandes du Conseil.
- [ ] Mettre à jour la matrice : `NEW TRACE → confirme → infirme → OPEN → documents modifiés`.
- [ ] Après décision nationale définitive, réévaluer séparément toute voie CEDH et calculer son délai propre.
- [ ] En cas de rejet, classer précisément : recevabilité, absence d'influence, fond, office, preuve, autre.
- [ ] En cas d'accueil partiel ou total, cartographier immédiatement les conséquences et voies possibles pour chaque partie.

## E. Règle agile

Un point découvert en chemin n'a pas besoin d'attendre la prochaine "grande version".

S'il est matériel et vérifiable :

> **on l'ajoute, on le relie, on le qualifie, puis on le ferme quand la Réalité a répondu.**


## UPDATE — 6 octobre 2026 — v0.9

- brouillon courant promu : `requete-conseil-constitutionnel-projet-v0.9.md` ;
- correction matérielle : la QPC est directement possible à l'occasion du contentieux électoral parlementaire devant le Conseil constitutionnel ; le verrou n'est donc plus l'instance mais la **qualité juridique de chaque question** ;
- QPC A : `L.299` devient le premier candidat à tester dans un mémoire distinct ;
- QPC B : non cristallisée à ce stade ;
- proclamation directe : désormais conclusion **infiniment subsidiaire**, explicitement exploratoire, à revoir avant dépôt.

## UPDATE — 6 octobre 2026 — lisibilité double public / juriste junior

- ajout d'un contrôle d'intelligibilité grand public ;
- ajout d'un contrôle d'intelligibilité pour un juriste junior du Conseil constitutionnel ;
- ces deux contrôles sont classés **MUST BEFORE FILING** : la requête doit être simultanément compréhensible sans jargon inutile et navigable juridiquement sans connaissance préalable du Corpus.


## UPDATE — 6 octobre 2026 — v0.10 / annexe P-41

- brouillon courant promu : `requete-conseil-constitutionnel-projet-v0.10.md` ;
- bordereau courant : `bordereau-pieces-requete-conseil-constitutionnel-v0.8.md` ;
- création de P-41 : annexe ciblée de déclarations publiques et commentaires de presse contemporains ;
- règle de crible : conserver les sources favorables **et** le framing adverse ; distinguer acteur / journaliste / résultat primaire / inférence ;
- point de vigilance renforcé : « cinq grands électeurs » désigne une **base institutionnelle minimale directement identifiable**, jamais l'ensemble des soutiens publics ni cinq bulletins attribuables ;
- avant dépôt, décider si P-41 est effectivement jointe ou reste une pièce de soutien/réserve.


## UPDATE — 6 octobre 2026 — répétition, médias, effectivité, Corse laboratoire

- ouverture d'un comparatif longitudinal **2017 / 2020 / 2024 / 2026** de la couverture du service public et de la couverture médiatique générale, avec comparateurs parmi les petites candidatures ;
- ajout d'une analyse séparée de la **forme** et du **fond** des quatre candidatures afin de mesurer les écarts entre offre réellement formulée et présentation médiatique ;
- traces institutionnelles confirmées : CSA ticket **227435** (2017) et Arcom alerte **807989** (2024) ; aucune réponse de fond retrouvée sous ces identifiants dans la recherche Gmail ciblée au 6 octobre ;
- l'hypothèse « droit décoratif / droit effectif » devient une **hypothèse à tester par chaîne d'effectivité**, pas une conclusion présupposée ;
- ancrage historique confirmé par une source parlementaire : la Corse est explicitement décrite comme **« laboratoire de la décentralisation »** pour la séquence ouverte en 1982 ;
- la généralisation « de nombreuses innovations corses ont ensuite été reprises ailleurs » reste à démontrer cas par cas ; ne pas sur-vendre ce point avant inventaire.


## UPDATE — 6 octobre 2026 — v0.8 / plateau pré-dépôt

- brouillon courant : `requete-conseil-constitutionnel-projet-v0.17.md` ;
- découverte load-bearing : **les griefs nouveaux sont forclos après le délai de l’article 33** ; toutes les branches matérielles doivent donc être présentes en substance dans la requête initiale ;
- distinction durcie : article 35 = délai exceptionnel pour certaines **pièces**, pas réserve générale de moyens ;
- canal de dépôt de l’article 34 ajouté comme contrôle opérationnel prioritaire ;
- grief L.299 recentré sur le texte réel + exception handicap, et non sur une équivalence simpliste papier/numérique ;
- calendrier sénatorial exact intégré : 7 / 21 / 26 octobre ;
- QPC soumises à un **kill-switch de qualité** : aucune QPC de remplissage ;
- CEDH : répétition ≠ situation continue ; qualité de victime Robert/Vernerey à cartographier ;
- à ce stade, les gains restants sont surtout matériels : dépôt, bordereau, pièces, QPC A éventuelle et revue adverse finale.


## UPDATE — 6 octobre 2026 — CEDH / boucle vers le plateau

- le volet CEDH est désormais traité comme une **préservation de griefs dès le dépôt national**, non comme un travail à commencer après coup ;
- la règle des quatre mois est couplée à l'épuisement des seuls recours **normaux et effectifs** : une démarche extraordinaire ou sans pouvoir de redressement ne sert pas à étirer le délai ;
- la saisine du Défenseur des droits est utile comme probe et source institutionnelle, mais n'interrompt pas le délai CEDH ;
- 2017 et 2024 servent d'abord à tester la **répétition** et la connaissance du problème ; ils ne ressuscitent pas une requête autonome hors délai ;
- le plateau pré-dépôt sera atteint lorsque les nouvelles objections deviennent répétitives et qu'aucun point nouveau ne change matériellement recevabilité, grief, pièce, conclusion, QPC ou préservation CEDH.



## UPDATE — 6 octobre 2026 — style, audace et lisibilité publique

- conservation verbatim demandée pour l'ouverture possible : **« Obtenir le respect, en Corse comme ailleurs, réclame d'en manifester ; le mépris appelle le mépris ».** ;
- ajout d'un contrôle **style / panache sans perte probatoire** : références historiques et proverbes peuvent rythmer le texte s'ils servent une idée et restent séparés de la démonstration juridique ;
- Danton : formulation de référence « de l'audace, encore de l'audace, toujours de l'audace » ;
- Talleyrand : l'explicitation reste un principe de lisibilité et de FractaCognition ;
- toute formule corse doit être vérifiée avant insertion afin d'éviter un effet de style au prix d'une ambiguïté de sens.

## UPDATE — 6 octobre 2026 — v0.11 / corpus courriels

- brouillon courant : `requete-conseil-constitutionnel-projet-v0.11.md` ;
- bordereau courant : `bordereau-pieces-requete-conseil-constitutionnel-v0.8.md` ;
- ajout **P-42** : saisine Défenseur des droits et suivi vérifié ;
- ajout **P-43** : index probatoire de la correspondance avec Laurence Vernerey ;
- règle nouvelle : **tout courriel matériellement pertinent doit être conservé et indexé ; tout courriel conservé n'a pas vocation à être annexé** ;
- priorité pré-dépôt : matérialiser les messages natifs effectivement cités dans la requête et vérifier qu'aucune pièce privée redondante n'alourdit le dossier.


## UPDATE — 6 octobre 2026 — FBF v0.9

Passe **Fix Bugs First** sur le paquet pré-dépôt :

- requête courante : `v0.17` ;
- bordereau courant : `v0.8` ;
- inventaire probatoire : aligné sur `v0.17` ;
- corrections des références résiduelles `v0.13` / `v0.11` / bordereau `v0.7` lorsqu’elles prétendaient décrire l’état courant ;
- contrôle mécanique du bordereau : séquence continue `P-01` à `P-43`, aucune pièce citée par la requête n’est absente du bordereau ;
- fermetures de checklist sur les points déjà effectivement résolus par la v0.14 : premier écran contentieux, statut du bulletin nul, architecture des conclusions, remedial probe, séparation Défenseur des droits, cadrage CEDH et symétrie conditionnelle.

Restent volontairement ouverts les points qui exigent un acte matériel ou une vérification du paquet réellement déposé : canal et preuve de dépôt, gel pré-dépôt, concordance exacte bordereau ↔ fichiers joints, lisibilité des pièces critiques, P-41, matérialisation P-21/P-29 à P-33, et revue adverse finale centrée sur les motifs de rejet.


## UPDATE — 6 octobre 2026 — plan de dépôt et revue de rejet

Objets ajoutés :

- `pre-filing-operational-plan-2026-10-07.md` — articles 33–35, canal légal, preuve de remise et marge opérationnelle ;
- `filing-package-manifest-2026-10-07.md` — distinction Corpus / bordereau / paquet matériel / paquet remis ;
- `../reviews/review_internal_requete_cc_motifs_rejet_2026-10-06.md` — revue interne corrélée centrée sur les voies de rejet.

Arbitrage P-41 : **soutien/réserve**, ne pas joindre par défaut au noyau initial.

La fermeture complète du dépôt reste impossible avant vérification matérielle des pièces et obtention de la preuve réelle de remise.


## UPDATE — 6 octobre 2026 — v0.10 / vidéo, consentement et traçabilité

- ajout du contrôle de la **diligence Bastia → Ajaccio** du 11 septembre, à documenter par traces disponibles ;
- ajout d’un contrôle de **transcription exacte de P-13**, afin que le contenu probatoire de la déclaration commune soit immédiatement lisible ;
- ajout de la chaîne de demandes **14–18 septembre** portant spécifiquement sur la réception, le versement et le traitement du courriel de 17 h 57 / vidéo, avant les relances des 25 septembre, 1er et 2 octobre ;
- ajout du triptyque **produite/envoyée → reçue/versée → effectivement examinée**, avec interdiction de transformer une inconnue en fait négatif acquis ;
- ajout d’un contrôle des **diligences cumulatives** destinées à garantir l’authenticité du consentement de la remplaçante ;
- ajout du **biais de cadrage / propagation de prémisse** comme test institutionnel et non psychologique ;
- ajout du **test de cohérence candidat/remplaçante**, articulé à L.298, L.299, au handicap et à CE, 14 mai 2021, n° 445497.


## UPDATE — 6 octobre 2026 — v0.11 / requêtes préfectorales et France Transfert

- synchronise la checklist avec la **requête v0.17** et le **bordereau v0.9** ;
- ferme la récupération et la comparaison des deux saisines préfectorales ;
- distingue explicitement **L.298/L.299 dans la saisine**, **L.298/L.299/L.301 dans le sens des conclusions e-Sagace**, et le contrôle encore à effectuer sur les motifs exacts du jugement primaire ;
- ajoute **P-44** comme chaîne de provenance France Transfert en deux courriels, avec règle de non-publication des secrets techniques ;
- maintient ouvert uniquement le travail matériel restant sur ce sous-front : contrôle primaire du jugement et matérialisation expurgée de P-44 dans le paquet de dépôt.

## UPDATE — 6 octobre 2026 — P-09 / P-17 : image primaire + transcription

- **P-09** : le récépissé provisoire ne doit pas être seulement cité ; le paquet de dépôt doit contenir son **scan lisible** et une **transcription textuelle vérifiée** ;
- **P-17** : la note manuscrite recto-verso remise à l'audience doit être produite sous les deux formes, **reproduction recto-verso + transcription textuelle** ;
- règle commune : l'image primaire fait foi ; toute transcription est dérivée et doit signaler ses incertitudes ; aucune lacune ne doit être comblée par inférence ;
- le texte exact de P-17 est à récupérer de la conversation contemporaine et/ou à vérifier sur le scan dès qu'il est retrouvé ;
- les scans du jugement du TA recherchés parallèlement feront l'objet du contrôle primaire déjà ouvert sur P-20.


## UPDATE — 7 octobre 2026 — redondance des canaux de dépôt

La stratégie de dépôt devient explicitement **redondante**, sous une contrainte d'identité stricte du paquet.

Source de travail : `matrice-canaux-materiels-depot-2026-10-07.md`.

Invariants ajoutés :

~~~text
plusieurs voies de remise
≠ plusieurs versions du recours

preuve d'expédition
≠ preuve de réception

courriel de copie
≠ saisine acquise

sous-préfecture
≠ représentant de l'État sans confirmation
~~~

Priorité opérationnelle :
1. remise physique anticipée à la préfecture de Bastia avec récépissé horodaté ;
2. si matériellement possible, remise directe redondante du même paquet au Conseil constitutionnel à Paris ;
3. commissaire de justice / porteur comme renfort probatoire ;
4. copies numériques ou fax uniquement comme traces supplémentaires, jamais comme unique fondement de la saisine.

La jurisprudence retrouvée impose une prudence maximale sur le temps : le Conseil a déjà rejeté des requêtes en se fondant sur leur **date de réception** au secrétariat général, postérieure au délai.
