---
title: "2026-6589 SEN — Provenance, transcription et parcours de la vidéo P-13"
author: unknown
generated_by: Codex
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-21"
status: working-paper
language: fr
license: CC BY-SA 4.0
document_role: operational
document_kind: evidence-provenance-note
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/complement-2026-6589-sen/parcours-video-p13-v0.1.md"
target_audience: "Requérant et intégrateur du complément 2026-6589 SEN"
target_scene: electoral
document_function: "Notice de pièce et transcription pour intégration au complément"
provenance:
  origin_type: repository
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: 16054878
  origin_date: "2026-10-21"
  derived_from:
    - "research/senatoriales-2026/requete-conseil-constitutionnel.md"
    - "research/senatoriales-2026/complement-2026-6589-sen/checkpoint-provenance-2026-10-21.md"
review:
  status: unreviewed
  reviewed_by: []
---

# Dossier 2026-6589 SEN — Provenance et parcours de la déclaration vidéo P-13

**Projet de travail v0.1 — non envoyé.** Paquet #132 sous umbrella #127. Rattachement : griefs G2 (consentement et handicap), G3 (office du TA) et G4 (complétude de la transmission).

## Objet probatoire

La déclaration vidéo commune du 11 septembre 2026 est présentée pour établir l'identité, la volonté et le consentement exprimés à l'époque des faits. Elle ne remplace pas de plein droit la signature ou la mention manuscrite requises par L.299 ; cette question demeure litigieuse.

## Séquence vérifiable

| Date / temps local | Événement ou constat | Niveau de preuve et portée |
|---|---|---|
| 11 septembre avant 18 h | Déclaration filmée, selon les sources et la chronologie du dossier | Binaire conservé vérifié le 21 octobre ; métadonnée interne de création 17h45m55s CEST, sans authentification indépendante de l'horloge de capture |
| 11 septembre, 17h57m55s | Courriel P-12 avec lien vers la vidéo envoyé à la préfecture | **Émission établie**, réception serveur avant 18 h inconnue |
| 11 septembre, après 18h | Saisine préfectorale du TA, inventaire initial de 16 pièces | P-11 et P-12 ne figurent pas dans l'inventaire initial connu ; transmission complémentaire ultérieure **UNKNOWN** |
| 14 septembre, audience | Proposition de visionnage immédiat rapportée par le requérant | Témoignage ; ni visionnage ni refus matériel institutionnellement corroborés à ce stade |
| 14 septembre, 15h48m32s | Note en délibéré envoyée, enregistrée à 15h49 | Prise de connaissance par la formation ultérieurement confirmée ; ne démontre pas visionnage de la vidéo |
| 15–18 septembre | Demandes répétées sur réception avant 18 h, transmission au TA et éventuel complément | Aucune réponse matérielle fermant les trois questions retrouvée dans les sources examinées |
| 16 septembre puis 21–25 septembre | Demandes d'inventaire des pièces au greffe TA et échanges | Certaines informations éclaircies (notamment note en délibéré), parcours de P-13 encore ouvert |
| 1er octobre | Réponse de la greffière en chef invitant à soumettre les questions dans le contentieux électoral | Réponse au requérant établie ; pas une preuve de consultation de P-13 |
| 2 octobre | Questions structurées à la préfecture et au TA | Demandes identifiables ; l'absence de réponse retrouvée ne prouve pas une volonté de dissimulation |

## Questions que seule l'instruction peut éventuellement résoudre

1. À quelle date et heure l'infrastructure de l'État a-t-elle accepté le courriel P-12 ?
2. Quel traitement a été appliqué au message et au lien qu'il contenait ?
3. Ont-ils été communiqués au TA après la saisine initiale ?
4. Le dossier effectivement accessible à la formation comprenait-il ce message ou la vidéo ?
5. Des documents matériels d'audience établissent-ils une proposition de visionnage ou une réponse à cette proposition ?

Ces questions sont légitimes **sans présumer une mauvaise intention** des services. Leur réponse peut confirmer une circulation régulière aussi bien que révéler une lacune.

## Métadonnées et intégrité

Le 21 octobre 2026, le fichier natif a été récupéré depuis Drive par le connecteur autorisé, puis conservé localement hors du dépôt public. Le calcul porte sur les octets effectivement récupérés, sans réencodage :

| Contrôle | Résultat |
|---|---|
| Nom source | `VID_20260911_174455.mp4` |
| Taille calculée | **79 663 474 octets** |
| SHA-256 recalculée | `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8` |
| Comparaison à l'empreinte historique | **PASS — identique** |
| Métadonnée interne `creation_time` | `2026-09-11T15:45:55.000000Z`, soit 17h45m55s CEST |
| Création / modification Drive | `2026-09-11T15:52:17.185Z` / `2026-09-11T15:53:33.108Z` |
| Durée indiquée par le conteneur | 58,14 secondes |
| Flux présents | Vidéo H.264 1920 × 1080 ; audio AAC stéréo |

Les métadonnées sont des indications contenues dans le fichier ou fournies par Drive, pas une certification de l'heure réelle de captation. Quatre images échantillonnées ont été regardées ; elles montrent deux personnes dans une même scène. Cette inspection visuelle ne constitue ni une authentification des personnes, ni une expertise d'absence de montage, ni une vérification mot à mot de la piste sonore.

Le décodage intégral audio/vidéo par FFmpeg s'achève avec un code de sortie 0 ; deux avertissements de DTS non strictement croissants apparaissent dans le flux de sortie de contrôle. Ce résultat documente la lisibilité technique, sans expertise d'authenticité ni conclusion sur la signification de ces avertissements.

La copie locale vérifiée et le relevé technique restent privés. L'empreinte lie la présente notice au binaire conservé ; elle ne démontre pas les octets reçus par l'administration ou la juridiction. Avant une transmission, recalculer l'empreinte du fichier sélectionné et conserver l'accusé propre au canal réellement utilisé. Le [texte maître v0.4](texte-maitre-travail-v0.1.md) prévoit dans une version ancienne quatre fichiers TransfertPro ; le contrat actuel en prévoit six, dont le MP4 P-13 : la mention historique du « second fichier » ne décrit plus cette architecture. Aucun de ces fichiers n'est réputé envoyé.

## Texte préparé et transcription déjà consolidée

Le requérant précise dans la conversation du **21 octobre 2026** que le texte de cette déclaration a été dicté par l'assistant et qu'un document existant en donne une transcription fidèle. La [requête initiale, passage « Le contenu probatoire de la vidéo P-13 »](../requete-conseil-constitutionnel.md), contient déjà les trois interventions ci-dessous. La présente notice les reprend à l'identique, sans modifier la requête historique. L'origine assistée du texte est consignée sur déclaration du requérant ; la conversation préparatoire de septembre n'a pas été retrouvée dans cette passe.

**Jean Hugues Noël Robert :**

> Nous sommes le 11 septembre 2026. Je suis Jean Hugues Noël Robert, candidat à l’élection sénatoriale du 27 septembre en Haute-Corse, sous le nom de Baron Mariani. Laurence est ici avec moi.

**Laurence Marie Vernerey :**

> Je suis Laurence Marie Vernerey. Je confirme librement et sans ambiguïté avoir accepté d’être la remplaçante de Jean Hugues Noël Robert pour cette élection, sous le nom de Marie-Louise d’Angelis. Je confirme également les documents et le consentement que j’ai transmis pour cette candidature.

**Jean Hugues Noël Robert :**

> Cette vidéo est adressée aujourd’hui au bureau des élections de la préfecture de Haute-Corse afin qu’il ne puisse subsister aucune ambiguïté sur notre identité, notre volonté et notre consentement.

**Qualification :** transcription documentaire préexistante, signalée comme fidèle par le requérant ; aucune nouvelle transcription automatique ni écoute comparative indépendante n'est revendiquée. La préparation du texte et sa prononciation sont deux événements distincts. La notice est une pièce dérivée accompagnant le MP4, sans constituer un second original audiovisuel.

**Sélection proposée : JOIN**, notice avec cette transcription dans le PDF consolidé du complément, et MP4 natif distinct identifié par la même empreinte. Rattachement inchangé à G2/G3/G4. La transcription facilite l'examen du contenu et conserve sa provenance ; elle ne prouve pas la réception avant 18 h, le versement au TA ou le visionnage par la formation. L'intégration matérielle au PDF final et la remise restent à réaliser avec #133/#134.

## Accessibilité et chronologie : point central de la provenance

La question centrale est l'accès effectif à la procédure de candidature pour la remplaçante, compte tenu de ses difficultés de déplacement. La voie électronique était une solution pratique pour manifester et transmettre son consentement, non un objectif autonome. Le débat sur le support de l'original est complémentaire.

Le 10 septembre 2026, après un premier envoi rejeté pour taille excessive à 17 h 01, le dossier est retransmis à 17 h 54 avec le formulaire de consentement. Celui-ci comprend une mention manuscrite et une signature reproduites dans le PDF. La réponse préfectorale arrive à 20 h 05, moins de vingt-deux heures avant la clôture. Elle demande les originaux et indique que l'envoi électronique ne suffit pas, sans préciser quelle insuffisance propre aux inscriptions déjà visibles dans le PDF est retenue.

Le 11 septembre, le candidat se présente physiquement à Bastia, puis rejoint Ajaccio avec des concours humains pour permettre la déclaration audiovisuelle de sa remplaçante. Le courriel contenant le lien vers cette vidéo est envoyé à 17 h 57 min 55 s, avant la clôture de 18 heures.

La maxime « À l'impossible, nul n'est tenu » exprime ici les diligences accomplies face aux contraintes matérielles et temporelles. Elle n'emporte pas dispense automatique des formalités applicables. Il faut distinguer la reconnaissance administrative d'un handicap des limitations fonctionnelles concrètes, ainsi que l'envoi électronique du dépôt physique.

## Saisine de la CADA du 22 octobre 2026 — complément de provenance P-12/P-13

Le **22 octobre 2026 à 09 h 48 min 17 s (CEST)**, le requérant a saisi par courriel le secrétariat général de la **Commission d'accès aux documents administratifs (CADA)** afin d'obtenir son avis sur la communicabilité des documents détenus par la préfecture de la Haute-Corse relatifs au **courriel P-12 du 11 septembre 2026 à 17 h 57 min 55 s** et à son lien vers la **vidéo P-13**. Il a demandé notamment les traces de réception et de traitement par la messagerie, les échanges ou enregistrements internes entre services, et les pièces permettant d'établir **si et quand** ce courriel ou cette vidéo ont été transmis ou signalés au Tribunal administratif de Bastia. Cette saisine était accompagnée de quatorze courriels sources au format EML, conservés séparément.

Le **22 octobre 2026 à 09 h 48 min 55 s (CEST)**, le secrétariat général de la CADA a confirmé la bonne réception du courriel, en précisant qu'un second envoi postal était inutile. Un avis de non-distribution à **une adresse secondaire en copie** a également été reçu ; il ne contredit pas cette réception confirmée par le destinataire principal. **Aucun avis sur le fond et aucun numéro de dossier CADA n'étaient connus lors de la présente vérification.**

Ce nouvel acte documentaire ne prouve **ni** la réception de P-12 avant 18 heures le 11 septembre, **ni** la transmission de P-13 au TA, **ni** son visionnage par la juridiction. Il complète la **chronologie des démarches de vérification** déjà motivées par les griefs initiaux G2/G3/G4 ; il **n'introduit pas de grief électoral nouveau**. L'éventuel avis de la CADA ou la communication ultérieure de traces préfectorales constitueront, s'ils interviennent, des événements distincts à produire et à dater. La demande à la CADA ne vaut pas demande au Conseil constitutionnel de surseoir à statuer.

**Référence publique de traçabilité :** [Interaction Packet CADA du 22 octobre 2026](https://github.com/JeanHuguesRobert/cogentia/blob/main/interaction_packets/packets/2026/2026-10-22-cada-courriel-video-senatoriales.yaml). Sources primaires conservées dans Gmail : message expédié `1a162950fcb19b4a`, accusé CADA `1a16295a2cf631e3`, notification de défaut de distribution en copie `1a1629542d086e2a`. La référence publique ne reproduit pas les messages privés ni les EML joints.

**Portée pour le Conseil constitutionnel :** il peut être utile de signaler cette saisine comme nouvelle démarche visant à identifier des **documents administratifs préexistants**, sans préjuger de la communicabilité de chaque catégorie de document ni de la réponse de la CADA. Il reste loisible au requérant de solliciter du Conseil, dans le cadre des griefs initialement formés, les mesures d'instruction qu'il estimera utiles sur la réception, la circulation et la communication de P-12/P-13.

## Bloc prêt pour le texte maître

« Le requérant communique une déclaration audiovisuelle contemporaine du 11 septembre 2026, comme preuve de la volonté et du consentement manifestés à cette date et non comme régularisation automatique d'une formalité légale. Le parcours de cette pièce entre son signalement à la préfecture et le jugement du Tribunal administratif demeure partiellement inconnu. Malgré des demandes répétées et circonscrites, les traces disponibles n'ont pas permis de déterminer de manière certaine sa réception avant la clôture, son éventuel versement complémentaire au dossier du Tribunal administratif ni son éventuel examen. Le requérant sollicite, dans la mesure utile à l'instruction des griefs déjà soulevés, la production des traces existantes de réception, de transmission et de mise à disposition. »

## Non-régression

- Consentement ≠ conformité formelle.
- Message envoyé ≠ reçu avant échéance ≠ versé ≠ visionné.
- Note en délibéré lue ≠ vidéo visionnée.
- Réponse non retrouvée ≠ refus intentionnel.
- Pièce obtenue après la clôture ≠ régularisation rétroactive.


## Addendum du 15 novembre 2026 — la provenance des 58 secondes et sa double lecture

**Statut : note complémentaire de provenance et de contextualisation, à relire avant tout envoi.** Cette section ne modifie ni la requête initiale n° 2026-6589 SEN ni ses griefs G1 à G5, et ne prétend pas que des pièces absentes du dépôt initial y figuraient. Elle distingue les éléments probatoires des faits de contexte à visée politique. **Aucun nouveau grief, aucune pièce réputée reçue ou examinée du seul fait de cette rédaction.**

### I. La vidéo ne remplaçait pas une acceptation écrite absente

Le 10 septembre 2026, le candidat avait **déjà transmis** le CERFA de la remplaçante sous forme d'un PDF numérique composite portant une acceptation écrite, une signature reproduite et une mention manuscrite photographiée. Selon les précisions ultérieures du requérant, la mention manuscrite a été inscrite par lui sur une feuille de papier puis photographiée ; la signature de Mme Laurence Vernerey provient d'une attestation d'inscription sur les listes électorales d'Évisa, délivrée par l'administration. **L'original du document composite est numérique ; ses composants ont une provenance propre, dont une intervention manuscrite physique.** Il convient dès lors de distinguer deux propositions qui ne sont pas équivalentes : l'existence d'un document composite original au format numérique et celle, non alléguée, d'un acte unitaire original sur papier signé personnellement. L'authenticité, l'autorisation de réutilisation et la conformité des formalités légales sont à apprécier distinctement. Les composants sources ne sont pas réputés avoir été vérifiés directement par la présente mise à jour.

**P-43.a — autorisation du 10 septembre à 12 h 38 min 31 s.** Un courriel contemporain de Mme Vernerey autorise expressément le candidat à utiliser sa signature sur le CERFA où elle accepte de le remplacer. Il s'agit d'une **pièce complémentaire de preuve relative à un grief déjà soulevé**, antérieure à l'échéance : sa production ultérieure éclaire un fait préexistant et ne prétend pas régulariser rétroactivement le dépôt. Le requérant indique qu'il aurait pu la produire le 11 septembre si l'administration avait demandé la justification de l'apposition de signature ; aucune demande ciblée de cette nature n'est identifiée dans les échanges examinés. Cela ne signifie pas que la préfecture avait l'obligation de solliciter chaque justificatif possible, ni que la réutilisation de signature satisfaisait nécessairement L.299.

**P-13 — déclaration commune de 58,14 secondes.** La vidéo visait à apporter un éclairage direct **sur l'identité, la volonté et le consentement libre** de Mme Vernerey, en corroboration des documents écrits déjà transmis ; elle n'avait pas pour fonction de se substituer à ces documents. La vidéo a été filmée selon les métadonnées antérieurement décrites ; un lien vers celle-ci a été expédié dans P-12 le **11 septembre à 17 h 57 min 55 s**. Réception serveur avant 18 heures, communication au TA et visionnage demeurent à vérifier. Le contenu est une preuve de consentement à examiner ; sa seule existence n'annule pas une formalité électorale légale.

### II. Pourquoi le canal dématérialisé ? Handicap, assistance et délai utile

Le requérant explique que la voie numérique répondait d'abord à **une nécessité pratique d'accessibilité** : l'empêchement fonctionnel allégué de sa remplaçante, ses difficultés de déplacement et la difficulté d'organiser une nouvelle impression, signature manuscrite et transmission dans les délais, le candidat se trouvant à Bastia et elle ailleurs. Ce mobile est déclaré par le requérant et doit être corroboré par les échanges et éléments techniques contemporains. Il s'inscrit aussi dans sa démarche annoncée de dématérialisation et de réduction de l'usage du papier : son courriel du **10 septembre à 17 h 54** invoquait **déjà** le guide DITP « Objectif zéro papier : simplifier ». Ce rapprochement est un constat de **tension entre politiques publiques**, non la preuve qu'un programme administratif général dispense du droit électoral spécial.

Le requérant déclare avoir expliqué oralement le handicap aux agents de la préfecture lors du dépôt du 11 septembre et précise que cette déclaration n'a pas été retenue dans la trace écrite dont il dispose : **témoignage du requérant, sans corroboration institutionnelle indépendante à ce stade**. Ne pas affirmer que l'information a été enregistrée, ni que l'administration l'a délibérément occultée. En revanche, la situation de handicap a été portée **par écrit** au TA : **P-18**, attestation CAF relative à l'AAH, était jointe à la **note en délibéré P-19** envoyée le 14 septembre à **15 h 48 min 32 s**, enregistrée à **15 h 49**, dont le greffe a confirmé le 16 septembre la connaissance par la formation avant le jugement. La reconnaissance de handicap ne prouve pas, à elle seule, l'empêchement précis d'apposer la mention ou signature les 10 et 11 septembre : cette circonstance appelle les sources contemporaines correspondantes.

La décision du **Conseil d'État du 14 mai 2021, n° 445497 et 445540**, concernant L.265 (municipales), admet que lorsqu'un handicap permanent ou provisoire empêche un candidat d'apposer personnellement une signature ou une mention manuscrite, un tiers puisse accomplir le geste *à sa demande*, si son **consentement éclairé est établi**. Source primaire : <https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-05-14/445497>. Le dossier sénatorial relève de **L.299**, non de L.265 : la transposition doit être motivée par l'analogie des fonctions probatoires et les différences factuelles, non décrétée automatique. **L.299** exige acceptation écrite, signature et mention manuscrite ; il ne contient pas littéralement l'expression « original papier unitaire » : <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036563386/>. Les dispositions sur le dépôt et le formulaire doivent être examinées en outre.

**Portée au sein des griefs initiaux :** G1 (support/formalisme réellement imposé), G2 (défaut allégué d'examen individualisé de l'empêchement de la remplaçante), G3 (contrôle juridictionnel propre), G4 (chaîne de circulation des pièces). Pour **P-43.a**, la fonction principale est G2 ; pour **P-13**, ce sont consentement (G2), possibilité d'examen (G3) et provenance/transmission (G4). Ne pas inventer un grief autonome de « double contrainte » ou de politique environnementale.

### III. Lecture politique et constitutionnelle explicitement séparée de la preuve électorale

Le requérant souhaite que cette pièce soit lisible à **deux niveaux** : (1) **note technique** permettant au juge de comprendre ce que P-13 prouve, ne prouve pas et pourquoi sa production a été diligentée ; (2) **mise en perspective civique et politique** soulignant les conséquences concrètes du formalisme sur l'accès à la représentation. La présente section est donc un commentaire de portée institutionnelle revendiqué, **sans ajout de prétention contentieuse** ni confusion entre les dates. Aucun public, notamment universitaire, ne doit être réputé avoir effectivement pris connaissance de ce texte sans preuve.

**Avant les faits de septembre 2026 :** l'association **C.O.R.S.I.C.A.** a transmis une contribution écrite à la commission des lois de l'Assemblée nationale le **28 mai 2026**, recensée dans les contributions écrites du **rapport n° 2865 de Florent Boudié, 3 juin 2026**, sur le projet constitutionnel relatif à l'autonomie de la Corse. La doctrine « autonomie de capacité / effectivité des droits » précédait donc le différend électoral. Voir [genèse probatoire](../../autonomia/genese_probatoire_amendement_effectivite_2026.md) et [observatoire du processus d'autonomie](../../autonomia/observatoire_processus_autonomie_corse.md).

**Continuité électorale :** le binôme Robert–Vernerey avait déjà été présenté aux sénatoriales **2020** en Corse-du-Sud ; Mme Vernerey figurait, en **quatrième position**, sur la liste territoriale **« A voce di a natura corsa »** de Jean-François Baccarelli en **2017**. L'étiquette **« Le Petit Parti – A Voce »** en 2026 renvoie à l'alliance revendiquée avec ce mouvement. Sources et limites : [notice de candidature](../../notice_candidature_senatoriales_2026_medias.md) et [dossier de presse](../dossier_presse_2026-09.md). Ces précédents sont un **contexte de sérieux et de continuité**, pas un consentement légal substitutif pour 2026.

**Après les faits de septembre, sans valeur rétroactive :** la publication d'un **amendement candidat dit « Baron Mariani »** sur l'effectivité du futur article 72-5, les contributions ultérieures au Sénat, le mouvement **Capable** et l'annonce d'une démarche de **candidature présidentielle** prolongent la ligne politique revendiquée par le requérant. Ils ne constituent **ni une adoption parlementaire, ni une candidature présidentielle légalement enregistrée, ni une régularisation des formalités sénatoriales**. Le **projet de loi constitutionnelle** relatif à l'autonomie de la Corse est celui du Gouvernement et du Parlement ; ne pas l'attribuer au requérant : son rôle documenté est celui de contributeur et d'auteur d'une proposition d'amendement. Le Sénat a rejeté l'ensemble du projet en première lecture le **26 octobre 2026** ; conserver cette chronologie. Voir [proposition 72-5](../../autonomia/amendement_effectivite_article_72-5.md), [contribution C.O.R.S.I.C.A. au Sénat](../../autonomia/contribution_senat_CORSICA_2026-10-14_source.md), [veille du rejet](../../autonomia/veille_senat_rejet_2026-10-26.md).

**Séparation des pouvoirs et protection contre le surajout normatif :** l'**article 16 de la Déclaration de 1789**, texte de valeur constitutionnelle, lie **garantie effective des droits et séparation des pouvoirs** (<https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006527443/>). L'**article 24 de la Constitution** dispose que **« Le Parlement vote la loi »** (<https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000019241014/>), et l'**article 34** lui réserve notamment la détermination des règles concernant les droits civiques et les garanties fondamentales (<https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/2026-07-10>). Une préfecture n'a pas compétence pour **ajouter par pratique administrative** une condition d'éligibilité ou de candidature que les normes applicables n'autorisent pas. Il appartient au juge **d'interpréter les textes et de les appliquer aux faits**, dans le respect des compétences du législateur ; le désaccord soulevé porte sur la portée exacte des conditions légales et réglementaires invoquées, non sur le pouvoir juridictionnel d'interprétation en lui-même. Soutenir une erreur de droit exige d'identifier la condition effectivement ajoutée et d'examiner les autres textes, règlements et jurisprudences applicables.

**Correspondance européenne :** l'**article 3 du Protocole n° 1 à la CEDH** protège, sous conditions, les élections libres et le droit de se porter candidat à un organe législatif ; l'**article 6 § 1 de la CEDH** énonce le principe du tribunal indépendant et impartial mais **n'est pas automatiquement applicable aux contestations portant sur des droits politiques**, qui ne relèvent pas nécessairement de « droits et obligations de caractère civil ». L'**article 47 de la Charte de l'UE** garantit le recours effectif et le tribunal indépendant **dans le champ du droit de l'Union** ; ne pas lui attribuer une application automatique à ce scrutin purement interne. Sources : <https://www.echr.coe.int/documents/d/echr/convention_fra> ; <https://eur-lex.europa.eu/eli/treaty/char_2012/art_47/oj>.

**Position civique du requérant :** lorsqu'une formalité conçue pour s'assurer du consentement devient inaccessible à une personne handicapée, que les preuves contemporaines d'identité et de volonté existent, et qu'aucune analyse individualisée des aménagements n'est visible dans les traces disponibles, le principe d'effectivité commande de regarder **ce que les institutions ont réellement permis**, et non seulement quels formulaires elles ont écartés. Cette lecture de portée civique accompagne, sans la remplacer, l'analyse des textes électoraux applicables : elle explicite le sens de la production de P-13 **à l'appui des griefs initiaux**.

**Observation diplomatique destinée à l'examen des griefs déjà formulés :** les formalités de candidature répondent à une exigence légitime de sécurité et de sincérité électorales, à laquelle le requérant souscrit. C'est précisément au regard de cette finalité qu'il sollicite l'examen des pièces contemporaines établissant l'identité et le consentement de Mme Vernerey, ainsi que des circonstances de handicap ayant motivé les modalités pratiques retenues. Il serait utile de préciser **quelle protection supplémentaire** la production d'un original papier unitaire aurait apportée dans les circonstances du dossier, **quelle disposition** rendait cette production indispensable et **quelle appréciation** a été portée sur la possibilité d'une assistance conforme à la jurisprudence du Conseil d'État du 14 mai 2021. Ces trois questions ne préjugent ni la réponse ni l'interprétation des textes ; elles permettent de mesurer si la sécurité recherchée et l'accessibilité effective de la candidature ont été conciliées.

### IV. Interface de production pièce par pièce — aucune extension du litige

| Pièce ou élément | Rôle précis au soutien des griefs déjà formulés | Limite de preuve à écrire dans le complément |
| --- | --- | --- |
| PDF composite CERFA du 10 septembre | G1/G2 : acceptation écrite effectivement proposée, provenance distincte des composants | Signature fac-similée et mention faite par tiers : validité formelle litigieuse ; ne pas inventer d'original papier unitaire |
| P-43.a — autorisation du 10 septembre | G2 : commande/consentement à l'utilisation de la signature, antérieur à l'échéance | Ne prouve pas par elle-même qu'une apposition personnelle conforme a eu lieu ni que la préfecture l'a reçue |
| P-43.b — désignation du 11 septembre | G2/G4 : continuité de volonté et de représentation après le dépôt, le 11 septembre | Ne modifie pas les prescriptions de L.299 |
| P-13 et sa transcription | G2/G3/G4 : identité/consentement contemporain et possibilité de visionnage ; pièce audiovisuelle native | Envoi P-12 établi côté expéditeur, réception et visionnage institutionnels inconnus |
| P-18/P-19 — AAH et note en délibéré | G2/G3 : information relative au handicap portée au TA et lue avant jugement selon confirmation du greffe | AAH ≠ preuve automatique d'incapacité physique à un geste précis ; connaissance par préfecture à qualifier séparément |
| Pièces préexistantes de candidature 2017/2020 | G2/contextualisation : antériorité d'identité électorale, continuité des personnes | Ne valent pas consentement pour 2026 ni preuve d'enregistrement de la candidature contestée |
| Contexte politique avant/après septembre | **Seconde lecture** pour contextualiser sérieux et enjeu public de l'effectivité | Les actes postérieurs ne prouvent aucun fait du 11 septembre ; pas de nouveau grief ni pièce électorale déterminante |

**Garde-fou final :** conserver le texte et le bordereau de la requête initiale sans réécriture ; toute production doit identifier son lien à G1/G2/G3/G4, sa date, sa provenance, son statut de transmission et son effet probatoire, et faire l'objet d'une revue avant dépôt. Cette note est destinée à préparer la communication de P-13 et de pièces préexistantes déjà mentionnées ; elle n'établit aucune remise effective au Conseil constitutionnel.
