---
title: "Sénatoriales Haute-Corse 2026 — Inventaire probatoire exhaustif et registre des pièces (Conseil constitutionnel)"
subtitle: "Registre analytique des sources, pièces, statuts de preuve et éléments de matérialisation du dossier contentieux"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-06"
version: "1.7"
status: "working-draft — aligned with CC petition v0.14 — for human review"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "evidence-manifest"
document_kind: "probative-inventory"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "corpus-legal"
classification_confidence: "strong"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/inventaire_probatoire_exhaustif_pieces_preuves.md"
source_documents:
  - "requete-conseil-constitutionnel-projet-v0.1.md"
  - "requete-conseil-constitutionnel-projet-v0.2.md"
  - "requete-conseil-constitutionnel-projet-v0.4.md"
  - "requete-conseil-constitutionnel-projet-v0.5.md"
  - "requete-conseil-constitutionnel-projet-v0.6.md"
  - "requete-conseil-constitutionnel-projet-v0.14.md"
  - "bordereau-pieces-requete-conseil-constitutionnel-v0.8.md"
  - "investigation/annexe-declarations-publiques-commentaires-presse-2026-10-06.md"
  - "investigation/sources/courriel-tracabilite-prefecture-2026-10-02.md"
  - "investigation/forensic-provenance-requete-prefectorale-2026-10-02.md"
  - "investigation/constat-consultation-2026-10-01-rp-sen-08-c.md"
  - "requete-conseil-constitutionnel-cahier-des-charges.md"
  - "dossier-ta-bastia-2026-09-14.md"
  - "investigation/chronology.md"
  - "investigation/defect-ledger.md"
  - "investigation/knowledge-matrix.md"
  - "investigation/passive-probes-2026-09-25.md"
  - "investigation/probe-map.md"
  - "case_studies/capable_test_article_72_5.md"
  - "case_studies/capable_test_senatoriales_2026_accessibilite.md"
  - "case_studies/capable_test_personnes_hypothetiques_72_5_effectivite.md"
provenance:
  origin_type: "repository"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "e7f6a11ff4495debd5abe8a792142d59dab87dad"
  origin_date: "2026-10-04"
  derived_from:
    - "research/senatoriales-2026/inventaire_probatoire_exhaustif_pieces_preuves.md"
review:
  status: "unreviewed"
  reviewed_by: []
human_arbitration_by: "Jean Hugues Noël Robert"
---

# INVENTAIRE PROBATOIRE DE TRAVAIL ET REGISTRE DES SOURCES / PIÈCES
## Contentieux de l'élection sénatoriale du 27 septembre 2026 — Haute-Corse
### Devant le Conseil constitutionnel (art. 59 de la Constitution et L. 303 du code électoral)

---

## I. PRINCIPES D'ARCHITECTURE PROBATOIRE ET DISCIPLINE DE QUALIFICATION

### Terminologie procédurale

Le présent document conserve le nom historique d'**inventaire probatoire**, mais il s'agit d'un **instrument analytique interne au Corpus**, plus large que la liste procédurale des pièces effectivement produites.

**Règle de complétude des courriels :** tous les courriels matériellement pertinents doivent rester identifiables et préservés dans le corpus probatoire, idéalement sous leur forme native. Cette complétude de conservation ne signifie pas que tous doivent être annexés au dépôt initial : la production demeure sélective, liée aux moyens invoqués, et minimisée lorsqu'elle implique des données privées ou sensibles.

Pour le dépôt contentieux, le terme de travail retenu est **bordereau de pièces** : le projet autonome correspondant à la requête v0.10 est :

`bordereau-pieces-requete-conseil-constitutionnel-v0.8.md`

La distinction est impérative :

`inventaire probatoire = ce qui est connu / disponible / analysé`

`bordereau de pièces = ce qui est identifié pour être effectivement annexé ou tenu en réserve de production`

Une pièce présente dans cet inventaire n'est donc **pas réputée produite** au Conseil constitutionnel par sa seule présence dans GitHub.



### 1. Structure de production

Le dossier probatoire est organisé autour de trois supports complémentaires :

1. **un recueil PDF consolidé**, paginé, contenant la requête, le bordereau et les pièces écrites communicables ;
2. **des pièces individuelles**, conservant leur format natif lorsque cela est utile à la preuve des métadonnées ;
3. **un registre d'intégrité**, contenant pour les pièces volumineuses ou non publiques leur désignation, leur empreinte cryptographique lorsqu'elle est disponible, leur détenteur et leur mode de communication possible.

La version publique du Corpus ne doit pas devenir le seul support d'une pièce nécessaire au contentieux. Les pièces comportant des données personnelles non nécessaires à la publicité sont produites institutionnellement sans publication intégrale. Cela vaut en particulier pour **P-43**, dont le Corpus public conserve l'index et la fonction probatoire, non le contenu privé intégral.

### 2. Portée de Git et des empreintes cryptographiques

Git est utilisé comme mécanisme de **traçabilité des versions et d'intégrité de contenu**. Un identifiant de commit ou une empreinte permet de vérifier qu'un contenu donné n'a pas changé entre deux références.

Cette propriété ne doit pas être sur-interprétée :

- un commit Git ne prouve pas, à lui seul, la vérité matérielle de ce qu'un document affirme ;
- l'horodatage Git est une trace technique à confronter aux autres sources et ne vaut pas automatiquement horodatage qualifié ;
- la publication sur GitHub n'accorde pas à une pièce une force probante prédéterminée ;
- lorsqu'une pièce primaire existe sous forme de courriel, document officiel, fichier original, photographie ou PDF communiqué par une institution, c'est cette source primaire qui doit rester identifiable.

### 3. Statuts probatoires

Chaque pièce ou affirmation est qualifiée, lorsque nécessaire, selon les catégories du dossier :

- **established** : directement établi par une ou plusieurs traces suffisantes ;
- **reported** : rapporté par un témoin ou le requérant, sans corroboration institutionnelle suffisante ;
- **inferred** : déduction explicite à partir de traces identifiées ;
- **open / UNKNOWN** : question non résolue.

L'inventaire décrit la **portée** d'une pièce ; il ne doit pas transformer sa présence au dossier en validation automatique du moyen juridique qui l'invoque.

## II. CATÉGORIE A — DILIGENCES ET RÉACTIVITÉ DOCUMENTÉES DU CANDIDAT

Cette série documente les actes accomplis par le candidat avant la clôture et pendant l'instruction. Elle permet d'apprécier sa chronologie de réponse sans présumer, par le seul inventaire, de leur suffisance juridique :

* **Anticipation et sérieux au long cours** : La volonté électorale n'est pas une impulsion tardive : elle est publiquement déclarée dès le 1er octobre 2025 et réaffirmée les 12 mars, 20 mai et 24 mai 2026 auprès de la presse insulaire (*Corse Net Infos*).
* **Réaction immédiate à l'aléa de recomposition** : Face à la défection inattendue du premier colistier le samedi 5 septembre 2026, le ticket a été reconstitué en moins de 6 jours avec Mme Laurence Vernerey.
* **Transmission proactive dès le 10 septembre à 17h54** : Envoi anticipé de l'ensemble du dossier dématérialisé au bureau des élections de la préfecture (`pref-elections@haute-corse.gouv.fr`).
* **Réponse immédiate dès l'aube du 11 septembre (08h14)** : Dès réception le 10 septembre à 20h05 de l'objection préfectorale demandant la présentation d'originaux, le candidat répond dès 08h14 le vendredi 11 septembre pour confirmer qu'il se déplace personnellement en train depuis Corte pour se présenter au guichet.
* **Comparution physique personnelle dès la mi-journée (12h10)** : En dépit d'un retard ferroviaire sur la ligne Corte-Bastia documenté par photographies horodatées, le candidat se présente en préfecture dès 12h10 et obtient à 12h20 un **reçu provisoire** attestant de la prise en charge de la déclaration.
* **Complétion en un temps record (1h54)** : À la suite de la demande orale d'un agent préfectoral relative à deux imprimés du mandataire financier, le candidat recueille, renseigne et télétransmet les documents dès **14h14:39**, tout en écrivant formellement qu'il se tient à l'entière disposition des services jusqu'à 18h00 pour toute autre demande précise.
* **Accusé de réception sans nouvelle réserve à 16h14** : À 16h14:05, le Bureau des élections confirme par écrit la réception des pièces du mandataire financier sans formuler le moindre nouveau grief écrit.
* **Absence d'assistance préfectorale élémentaire** : Alors que le candidat était physiquement présent au guichet de 12h10 à 12h30, aucun agent de la préfecture ne lui a proposé d'imprimer son propre formulaire Cerfa pour qu'il le signe sur place à l'encre, l'administration préférant s'enfermer dans une posture de refus de guichet.
* **Transmission proactive de la vidéo du consentement à 17h57:55** : Pour lever toute incertitude sur l'authenticité de l'acceptation de Mme Vernerey, le candidat produit et expédie à 17:57:55 un lien vers l'enregistrement vidéo solennel de sa remplaçante.
* **Diligence contentieuse exceptionnelle durant le week-end du 12-13 septembre** : Rédaction d'un mémoire de défense juridique de 15 pages (`dossier-ta-bastia-2026-09-14.md`) et publication ouverte pour le contradictoire.
* **Présence à l'audience du TA du 14 septembre à 15h00** : Dépôt d'observations écrites d'audience et offre explicite de visionnage immédiat de la vidéo sur équipement informatique propre.
* **Production immédiate de l'attestation CAF AAH (15h48:32)** : Dès réception de l'attestation officielle de la CAF de Corse-du-Sud le 14 septembre, transmission immédiate d'une note en délibéré enregistrée à 15h49 par le greffe du Tribunal administratif.
* **Poursuite d'une démarche contradictoire sous le CRPA et le RGPD** : Envoi de six relances formelles entre le 15 et le 25 septembre 2026 pour préserver les traces techniques (logs SMTP) et clarifier les inventaires de pièces.

---

## III. CATÉGORIE B — CONTRAINTES MATÉRIELLES, TEMPORELLES ET FONCTIONNELLES

Cette série documente les contraintes invoquées par le requérant. Certaines sont directement établies (horaires, distances, séquence des messages), d'autres relèvent d'une appréciation de leur effet concret et doivent rester qualifiées comme telles :

* **Un délai légal de réaction réduit à quelques heures** : Entre la formulation de l'objection préfectorale le jeudi 10 septembre à 20h05 et la clôture légale du vendredi 11 septembre à 18h00, le temps utile de traitement était inférieur à 10 heures ouvrées.
* **La contrainte géographique insulaire** : Le candidat résidait à Corte (Centre Corse), la préfecture se trouvait à Bastia (Haute-Corse), et la candidate remplaçante résidait en Corse-du-Sud (région ajaccienne).
* **L'aléa de transport documenté** : La liaison ferroviaire Corte-Bastia empruntée par le candidat le 11 septembre au matin a subi un retard d'exploitation, attesté par des photographies horodatées (métadonnées EXIF), empêchant une arrivée avant midi.
* **Acheminement physique dans le temps restant** : le requérant soutient qu'un original établi à distance le 11 septembre ne pouvait raisonnablement être acheminé physiquement à Bastia avant 18 h ; cette proposition doit être rattachée aux horaires et moyens réellement disponibles plutôt qu'à un délai postal général présenté comme absolu.
* **Situation administrative de la remplaçante** : l'attestation CAF établit le bénéfice de l'AAH. Elle ne suffit pas, isolément, à établir la nature exacte du handicap ni l'impossibilité d'une formalité déterminée ; les difficultés fonctionnelles alléguées doivent être documentées séparément.
* **Possibilités de correction sur place** : le requérant rapporte qu'aucune impression de son propre formulaire suivie d'une signature manuscrite sur place ne lui a été proposée. Cette circonstance reste à corroborer par une trace institutionnelle ou un témoignage indépendant.

---

## IV. CATÉGORIE C — ÉLÉMENTS CONTEMPORAINS RELATIFS À L'IDENTITÉ ET AU CONSENTEMENT

Cette série rassemble les éléments invoqués pour établir l'identité et le consentement. Leur force probante doit être distinguée de la question séparée de la satisfaction du formalisme électoral :

* **L'attestation d'inscription sur les listes électorales** : Établie et signée par Mme Laurence Vernerey, transmise dès le 10 septembre.
* **L'autorisation expresse d'apposition de signature** : Courriel explicite de Mme Vernerey autorisant M. Robert à faire usage de son fac-similé de signature pour le dépôt du formulaire officiel.
* **L'enregistrement vidéo contemporain du 11 septembre 2026** : Mme Vernerey y décline son identité et confirme oralement son acceptation d'être la remplaçante de M. Robert ; la vidéo est un élément de consentement et d'identification, sans se substituer automatiquement aux formalités prévues par le code électoral.
* **L'attestation officielle de la CAF de Corse-du-Sud** : Établissant le bénéfice de l'AAH au titre d'un handicap légalement reconnu immédiatement contemporain des opérations de candidature (*SHA-256: 308754ffac6100b050dea6c43830562d0d581e8c020898201e011ab73b79fbb2*).

---

## V. CATÉGORIE D — CHAÎNE DE TRANSMISSION PRÉFECTURE → TRIBUNAL

La récupération du PDF préfectoral original permet désormais de séparer ce qui est établi de ce qui demeure ouvert :

* **Saisine et motivation établies** : la requête de la préfète est disponible dans le bundle communiqué par le TA le 11 septembre.
* **Inventaire initial établi** : la requête décrit explicitement seize pièces, détaillées plus bas sous les identifiants **PREF-1 à PREF-16**.
* **Absences de l'inventaire initial établies** : l'accusé humain de 16 h 14 (**P-11**) et le courriel de 17 h 57 min 55 s (**P-12**) ne figurent pas dans cette liste.
* **Réception de P-12 avant 18 h : ouverte** : l'émission avant 18 h est établie côté expéditeur ; l'heure d'acceptation par l'infrastructure de l'État reste à établir.
* **Productions préfectorales ultérieures : ouvertes** : le dossier doit encore établir si des éléments ont été transmis au TA après le bundle initial et avant le jugement.
* **Qualification juridique : ouverte** : l'absence d'une pièce du bundle initial ne doit être qualifiée de rétention, omission fautive ou déloyauté qu'après établissement de sa disponibilité pour l'administration et de la chaîne de transmission pertinente.

## V bis. PROVENANCE NUMÉRIQUE ET CHAÎNE DÉCISIONNELLE PRÉFECTORALE

Ce front est ouvert par **P-35** et documenté méthodologiquement par **P-36**.

* **Établi** : le 2 octobre à 13 h 33 min 55 s, dix-huit demandes autonomes ont été adressées à la préfecture.
* **Établi** : la copie de la requête préfectorale disponible dans les bundles du TA est lisible mais issue d'une recomposition ultérieure qui n'expose pas, à elle seule, les métadonnées natives du fichier source.
* **Ouvert** : fichier exact effectivement transmis, nom original, empreintes, PVN Télérecours, accusés, chronologie de création/finalisation/validation/transmission.
* **Ouvert** : auteur de préparation, validateur, autorité de décision, délégation utilisée et base informationnelle effectivement disponible au moment où les motifs de saisine ont été arrêtés.
* **Règle** : la demande d'une trace primaire ne vaut pas affirmation que cette trace a disparu ou qu'une irrégularité a été commise.

## VI. CATÉGORIE E — EXAMEN DU DOSSIER PAR LE TRIBUNAL ADMINISTRATIF : ÉTABLI, RAPPORTÉ, OUVERT

* **Établi** : le jugement mentionne des « observations écrites et orales » du requérant ; la note en délibéré a été enregistrée à 15 h 49 et le greffe a confirmé que la formation en avait pris connaissance avant de décider.
* **Document primaire du requérant** : une note manuscrite recto-verso, datée et signée, portant les deux numéros d'instance, est conservée photographiquement (**P-17**). Sa remise en main propre au début de l'audience est rapportée par le requérant ; son rattachement à l'entrée Sagace « Réception d'une lettre » reste ouvert.
* **Rapporté** : le requérant indique avoir proposé le visionnage immédiat de la vidéo et avoir entendu la présidente dire, en substance, que l'absence des CERFA originaux papier suffisait sans examen supplémentaire des autres pièces.
* **Ouvert** : aucune trace institutionnelle actuellement identifiée ne permet de confirmer ou d'infirmer ces propos d'audience, l'offre de visionnage ou l'étendue annoncée de l'examen des pièces.
* **Probe contentieux** : rechercher, s'ils existent, procès-verbal, plumitif, fiche, note d'audience ou document équivalent ; obtenir la minute signée du jugement et identifier le greffier d'audience.

## VII. CATÉGORIE F — SCRUTIN, INCIDENCE ALLÉGUÉE ET CONTEXTE D'EFFECTIVITÉ

Cette série documente le scrutin réel, les analyses d'incidence et le contexte doctrinal. Elle ne permet pas d'attribuer une intention de vote aux bulletins blancs ou nuls ni de reconstituer avec certitude un scrutin contrefactuel :

* **Proposition parlementaire d'amendement à l'article 72-5 (v0.4-rc4)** : Texte de doctrine constitutionnelle formalisé en vue de la session sénatoriale d'octobre 2026 sur l'autonomie de la Corse.
* **Les 6 cas d'application du Principe d'Effectivité (Capable Test)** : Cadre d'évaluation éprouvé démontrant la carence d'effectivité des droits fondamentaux.
* **Annuaire public des 616 grands électeurs de Haute-Corse** : Base de données vérifiée établissant la structure du collège sénatorial et la réalité de l'exposition politique.
* **Doctrine de l'ARCOM sur l'exposition équitable** : Règles du régulateur audiovisuel démontrant le mécanisme pervers de double peine : exclusion d'un scrutin entraînant un score nul, justifiant ensuite l'éviction médiatique future.

---

## VIII. REGISTRE MATRICIEL — 44 PIÈCES / ENSEMBLES DE PIÈCES

| N° | Date & heure | Intitulé | Portée probatoire bornée | Source / support |
|---|---|---|---|---|
| **P-01** | 01/10/2025 | Annonce publique de candidature | Antériorité publique | Capture / trace publique |
| **P-02** | 20/05/2026 | « Autonomia - 1974, 1991, 2026 » | Contexte doctrinal antérieur | research/autonomia.md |
| **P-03** | 24/05/2026 | Courriel à Corse Net Infos | Information précoce de la presse | Courriel source |
| **P-04** | 10/09 17:54:50 | Envoi du dossier à la préfecture | Courriel + huit PJ ; repris comme PREF-1 à PREF-9 | Courriel source / bundle P-14 |
| **P-05** | 10/09 17:56:53 | Accusé automatique | Réception de P-04 par la messagerie de l'État | Courriel source |
| **P-06** | 10/09 20:05:04 | Réponse BEDL | Position préfectorale sur les originaux | Courriel source / PREF-10 |
| **P-07** | 11/09 08:14:11 | Réponse du candidat | Déplacement annoncé | Courriel source |
| **P-08** | 11/09 matin | Traces de trajet | Contexte matériel, sans portée juridique automatique | Photos / chronologie |
| **P-09** | 11/09 12:20 | Reçu provisoire | Prise en charge d'une déclaration, pas preuve de conformité | Document officiel / PREF-13 |
| **P-10** | 11/09 14:14:39 | Courriel mandataire + 2 PJ | Complétion et disponibilité jusqu'à 18 h | Courriel / PREF-14 à PREF-16 |
| **P-11** | 11/09 16:14:05 | « J'accuse réception des documents » | Accusé humain ; absent du bundle initial PREF-1 à 16 | Courriel source |
| **P-12** | 11/09 17:57:55 | Courriel complémentaire avec lien vidéo | Émission avant 18 h ; réception serveur à établir | Courriel source |
| **P-13** | 11/09 | Vidéo commune | Identité, volonté, consentement contemporains | Fichier vidéo / empreinte à fixer |
| **P-14** | 11/09 | Requêtes préfectorales n° 2601714 et 2601715 + bundles | Motivation préfectorale et inventaire initial 1–16 | PDF originaux reçus via France Transfert |
| **P-15** | 14/09 14:09:17 | Alerte avant audience | Signalement de transmissions que le requérant estimait manquantes | Courriel source |
| **P-16** | 14/09 | Mémoire en défense | Moyens soumis au TA | dossier-ta-bastia-2026-09-14.md |
| **P-17** | 14/09 audience | Note manuscrite recto-verso | Existence/contenu photographiés ; remise en main propre rapportée | Photos privées / transcription |
| **P-18** | 14/09 | Attestation CAF | Établit le bénéfice de l'AAH, rien de plus sur la nature fonctionnelle | Document privé |
| **P-19** | 14/09 15:48:32 | Note en délibéré | Envoi ; enregistrement 15 h 49 ; prise de connaissance confirmée | Courriel + jugement + P-30 |
| **P-20** | 14/09 | Jugement TA Bastia | Décision attaquable via L.303 devant le CC saisi de l'élection | Jugement |
| **P-21** | 15–25/09 | Demandes documentaires post-jugement | Diligences pour clarifier le dossier | Ensemble de courriels |
| **P-22** | 25/09 16:59:13 | Demande à la préfecture / conservation des traces | Logs, demandes d'originaux, transmissions au TA | Courriel source |
| **P-23** | 26/09 | Amendement d'effectivité art. 72-5 | Contexte doctrinal, non norme positive applicable au litige | Document public |
| **P-24** | 27/09 | Capable Test / cas d'effectivité | Grille méthodologique | Document public |
| **P-25** | 28/09 | Annuaire / étude d'exposition | Structure du collège ; aucune inférence individuelle de vote | CSV + analyse |
| **P-26** | 28/09 | Demande PV et pièces électorales | Demande de consultation post-scrutin | Courriel / document source |
| **P-27** | 27/09 | Résultats officiels | 606 votants, 36 blancs, 40 nuls, 530 exprimés, 442/88 | Source officielle / data |
| **P-28** | 30/09 08:16:30 | Réponse BEDL | Consultation sur place proposée le 1er octobre | Courriel source |
| **P-29** | 16/09 08:38:28 | Première demande TA sur la liste des pièces | Première demande explicite d'inventaire identifiée | Courriel source |
| **P-30** | 16/09 | Réponse du greffe TA | Écritures préfectorales dites communiquées en totalité ; note prise en compte | Courriel greffe |
| **P-31** | 21/09 | Réponse du greffe TA | Jugement présenté comme répondant aux questions ; disponibilité annoncée | Courriel greffe |
| **P-32** | 25/09 16:50:46 | Six questions résiduelles au TA | Questions factuelles après lecture du jugement | Courriel source |
| **P-33** | 01/10 15:13:26 | Réponse de la greffière en chef | Refus de donner suite ; invitation au CC ; référence L.292 | Courriel greffe / registre interaction |
| **P-34** | 01/10 | Courriel consolidé à la préfecture | Cinq questions sur réception/transmission de P-12 | investigation/sources/courriel-consolidation-prefecture-ta-2026-10-01.md |
| **P-35** | 02/10 13:33:55 | Relance consolidée P1–P18 à la préfecture | Établit les demandes de traçabilité, provenance numérique, chaîne de décision, conservation et routage ; réponses encore PENDING | investigation/sources/courriel-tracabilite-prefecture-2026-10-02.md |
| **P-36** | 02/10 | Note forensic sur la provenance numérique de la requête préfectorale | Analyse dérivée : bundles TA recomposés, contenu lisible mais provenance native non exposée ; ne prouve ni disparition ni altération fautive | investigation/forensic-provenance-requete-prefectorale-2026-10-02.md |
| **P-37** | 01/10 10:11:07 | Adresse du rendez-vous | 15 Avenue Jean Zuccarelli ; salons de la préfecture indisponibles ce jour-là | investigation/sources/courriel-prefecture-adresse-rendez-vous-2026-10-01.md |
| **P-38** | 01/10 12:30:20 | Réponse sur cette adresse | Phrase familiale et expropriation ; train annoncé en principe à 15 h ; retard annoncé. Ni l'arrivée effective ni l'inventaire des pièces | investigation/sources/courriel-reponse-adresse-rendez-vous-2026-10-01.md |
| **P-39** | 01/10, stabilisé 04/10 | Constat de consultation RP-SEN-08-C | Établit la tenue de la consultation, le lieu matériel, l'accueil par Adrien Vidal, les quatre dossiers, le formulaire signé, les pièces photographiées et sépare les propos oraux des faits documentés | investigation/constat-consultation-2026-10-01-rp-sen-08-c.md |
| **P-40** | 01/10, versé 02/10 | Bulletin « BARON MARIANI » et enveloppe | Trace photographique primaire ; bulletin imprimé « (Elections Sénatoriales 2027) BARON MARIANI », enveloppe associée, SHA-256 et copies Drive ; n'identifie aucun électeur et ne fixe pas à lui seul le motif juridique de nullité | investigation/sources/bulletin-nul-baron-mariani-2026-10-01.md |
| **P-41** | 06/10 | Annexe — déclarations publiques et commentaires de presse | Source contextuelle structurée ; distingue déclarations d'acteurs, commentaires journalistiques, faits officiels et inférences ; documente A Voce, intentions Battini rapportées, cadre adverse, Giuseppi et autonomie | investigation/annexe-declarations-publiques-commentaires-presse-2026-10-06.md |
| **P-42** | 26/09 + 01–02/10 | Saisine Défenseur des droits et suivi | Saisine sur l’effectivité ; aucune réponse de la déléguée retrouvée au 06/10 dans la recherche Gmail ciblée ; état de trace, pas preuve d’absence de traitement | investigation/sources/saisine-defenseur-droits-2026-09-26.md |
| **P-43** | 07–14/09 | Correspondance contemporaine avec Laurence Vernerey | Participation, consentement, aide matérielle, porte-parole, vidéo, accessibilité ; source privée, production sélective/minimisée | investigation/sources/index-correspondance-laurence-vernerey-2026-09.md + Gmail natif |
| **P-44** | 11/09 18:45:53 | France Transfert — deux courriels de communication des requêtes 2601714 / 2601715 | Établit la provenance de transmission au requérant : avis de pli du greffe + mot de passe séparé ; secrets techniques non publiés | investigation/sources/france-transfert-ta-requetes-2026-09-11.md + Gmail natif |

### Sous-inventaire exact décrit par la requête préfectorale P-14

La comparaison des deux bundles confirme que les saisines préfectorales signées de trois pages ont le **même contenu substantiel**. Dans l'exposé des faits, elles mentionnent le rappel de **L.298 et L.299** ; dans la partie « Discussion », l'exigence d'« original » est développée en reproduisant expressément **L.299**, sans développement autonome de L.298. Le sens des conclusions e-Sagace mentionne pour sa part **L.298, L.299 et L.301** : ne pas confondre ces trois niveaux documentaires.

La requête préfectorale n° 2601714 indique elle-même la structure suivante :

| Préf. | Pièce décrite dans la requête |
|---|---|
| **PREF-1** | Courriel du candidat du 10/09 à 17 h 54 |
| **PREF-2** | CERFA n° 15217*04 du candidat |
| **PREF-3** | Justificatif d'identité du candidat |
| **PREF-4** | Attestation de situation électorale du candidat |
| **PREF-5** | CERFA n° 15218*04 de la remplaçante |
| **PREF-6** | Justificatif d'identité de la remplaçante |
| **PREF-7** | Attestation de situation électorale de la remplaçante |
| **PREF-8** | Déclaration de désignation de Mme Marguerite Ghionga comme mandataire financier |
| **PREF-9** | Acceptation manuscrite du mandataire avec justificatif d'identité |
| **PREF-10** | Courriel préfectoral du 10/09 à 20 h 05 |
| **PREF-11** | Dossier physique du 11/09 contenant une pièce unique ; l'intitulé primaire reste à isoler |
| **PREF-12** | Circulaire ministérielle du 20/07/2026 |
| **PREF-13** | Reçu provisoire |
| **PREF-14** | Courriel du candidat du 11/09 à 14 h 14 |
| **PREF-15** | Déclaration de désignation du mandataire financier jointe à PREF-14 |
| **PREF-16** | Accord / acceptation du mandataire financier joint à PREF-14 |

La requête précise que le dossier avait été transmis principalement sous forme dématérialisée « à l'exception du document portant sur l'acceptation des fonctions du mandataire financier ». Cela suggère fortement que PREF-11 correspond à cette pièce physique, sans dispenser d'isoler le document primaire pour clore définitivement ce point.

**Deux constats doivent rester séparés :**
- P-11 et P-12 ne figurent pas dans l'inventaire initial PREF-1 à PREF-16 ;
- cela ne prouve pas, à lui seul, que P-12 avait été reçu par la préfecture avant 18 h ni qu'aucune transmission complémentaire n'a ensuite été faite au TA.

## IX. SYNTHÈSE POUR LA MATÉRIALISATION DU DOSSIER AU CONSEIL CONSTITUTIONNEL

Avant dépôt, produire un manifeste final séparant :

1. **la requête signée** avec l'identité et la qualité du requérant, l'élu dont l'élection est contestée et les moyens invoqués ;
2. **le bordereau autonome v0.6**, avec pour chaque pièce candidate son numéro P-xx, son intitulé, son rôle, son statut de production, son support réel, sa pagination dans le recueil et, si utile, son empreinte ;
3. **le recueil PDF consolidé**, sans faire dépendre l'accès du Conseil d'un simple lien web ;
4. **les pièces natives décisives**, notamment les courriels dont les métadonnées sont probatoires, la vidéo P-13 et les PDF originaux P-14 ;
5. **un registre des UNKNOWN**, afin qu'une demande d'instruction soit formulée là où le requérant ne dispose pas lui-même de la pièce ;
6. **la trace du dépôt** : canal utilisé, date, heure, récépissé ou accusé, empreinte du PDF final et version Git correspondante.

L'article 33 de l'ordonnance n° 58-1067 fixe le délai au dixième jour suivant la proclamation, à 18 heures. L'article 34 permet une requête écrite adressée au secrétariat général du Conseil constitutionnel ou au représentant de l'État. Le canal matériel retenu devra être vérifié au moment du dépôt et documenté sans confondre préparation et saisine effectivement accomplie.

### Contrôle de cohérence v1.5

- La requête **v0.17**, le présent inventaire **v1.7** et le **bordereau autonome v0.9** doivent rester alignés avant tout dépôt.
- Le bundle préfectoral initial dispose de son sous-inventaire PREF-1 à PREF-16.
- P-17 est qualifiée comme document manuscrit recto-verso dont l'existence et le contenu sont établis, la remise restant rapportée.
- Les éventuelles productions postérieures au bundle initial restent UNKNOWN.
- La « minute » demandée est la minute signée du **jugement** ; une éventuelle trace d'audience constitue un objet documentaire distinct.
- Les pièces doctrinales P-23/P-24 ne sont pas présentées comme des normes juridiques positives applicables au litige.
- Les résultats P-27 ne sont pas utilisés pour attribuer une intention aux électeurs blancs ou nuls.
- P-41 conserve séparément propos politiques, commentaires de presse, résultats officiels et inférences ; elle ne sert jamais à attribuer un bulletin secret à une personne nommée.

Fait à Corte, le 1er octobre 2026.

**Jean Hugues Noël ROBERT**  
*(Baron Mariani)*


## UPDATE v1.7 — 6 octobre 2026

- ajoute **P-44**, chaîne France Transfert en deux courriels ;
- documente la comparaison des deux saisines préfectorales et la distinction **L.298 / L.299** dans leur motivation ;
- conserve séparément le **sens des conclusions e-Sagace (L.298, L.299, L.301)** et les motifs du jugement, qui doivent être vérifiés sur l'expédition primaire ;
- aligne le contrôle de cohérence sur **requête v0.17 / inventaire v1.7 / bordereau v0.9**.
