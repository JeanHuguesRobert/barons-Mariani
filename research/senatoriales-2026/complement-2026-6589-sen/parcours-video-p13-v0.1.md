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
