---
title: "Sénatoriales 2026 — exécution des probes passifs RP-SEN-15/16/17"
date: "2026-09-25"
run_id: "RPR-SEN-2026-09-25-01"
status: "working"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "analysis"
document_kind: "reality-probe-run"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
source_map: "research/senatoriales-2026/investigation/probe-map.md"
source_batch: "research/senatoriales-2026/investigation/probe-batch-2026-09-25.md"
privacy_rule: "No raw identity document, address, signature image, health datum or private attachment is republished here."
review:
  status: unreviewed
  reviewed_by: []
---

# Sénatoriales 2026 — run passif RP-SEN-15 / 16 / 17

## Objet

Ce run exécute trois probes passifs sans produire de nouveau contact externe :

- **RP-SEN-15** — corpus juridique et administratif officiel ;
- **RP-SEN-16** — reconstruction côté candidat ;
- **RP-SEN-17** — jurisprudence comparable.

---

## RP-SEN-15 — corpus juridique et administratif officiel

**Statut :** `answered / continuing`

### Noyau normatif

- **L.298** : déclaration revêtue de la signature du candidat.
- **L.299** : acceptation écrite du remplaçant revêtue de sa signature, suivie de la mention manuscrite légalement prévue.
- **L.301** : dépôt en double exemplaire à la préfecture avant l'heure limite ; reçu provisoire puis récépissé définitif si la déclaration est conforme.
- **R.149** : déclaration rédigée sur un imprimé et déposée par un candidat, son remplaçant ou un mandataire.
- **Décret n° 2015-1423** : la déclaration de candidature sénatoriale figure parmi les démarches exclues du droit général de saisine électronique.

Sources officielles :
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036563393
- https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000036563386
- https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006085760
- https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006134815
- https://www.legifrance.gouv.fr/loda/id/JORFTEXT000031425652
- https://www.haute-corse.gouv.fr/Actions-de-l-Etat/Vie-democratique/Elections/Elections-senatoriales-2026/Memento-a-l-usage-des-candidats

### Notice CERFA effectivement envoyée

La notice du CERFA n° 15217*04 contenue dans le bundle du 10 septembre distingue elle-même :

- la **signature manuscrite originale** ;
- le dépôt en **double exemplaire** ;
- le fait que **le second exemplaire peut être photocopié** ;
- l'utilité du téléphone et du courriel pour permettre à la préfecture de contacter le candidat si le dossier est incomplet.

### Discriminant obtenu

Ne pas fusionner :

~~~text
A — dépôt à distance par courriel
B — dépôt physique sur imprimé
C — actes personnels : signature / mention
D — support matériel qualifié d'« original »
~~~

L.298/L.299 portent directement sur **C**. L.301/R.149 structurent **B**. Le décret de 2015 exclut le droit général d'accomplir **A** par simple saisine électronique.

La formule littérale **« original papier »** n'a pas été identifiée dans ces quatre articles. La notice emploie en revanche **signature manuscrite originale** et prévoit qu'un second exemplaire peut être photocopié.

Ce résultat ne tranche pas la conséquence juridique du défaut retenu par le jugement ; il rend U7 plus précise.

### Corroboration par les instructions 2026 publiées ailleurs

Plusieurs pages préfectorales 2026, qui renvoient au même mémento national, publient explicitement les modalités suivantes :

- aucun dépôt de candidature par messagerie électronique ;
- dossier en double exemplaire ;
- selon les pages, précision qu'il peut s'agir d'un original et d'une copie ;
- les formulaires officiels rappellent eux-mêmes la signature manuscrite originale et la possibilité de photocopier le second exemplaire.

Exemples officiels :
- Haute-Garonne : https://www.haute-garonne.gouv.fr/Actualites/Depot-des-declarations-de-candidature-Senatoriales-2026
- Alpes-de-Haute-Provence : https://www.alpes-de-haute-provence.gouv.fr/Actions-de-l-Etat/Elections/Elections-politiques/Elections-Senatoriales-2026
- Haute-Savoie : https://www.haute-savoie.gouv.fr/Actualites/Elections/Elections-politiques/Elections-senatoriales/Candidatures
- Bas-Rhin : https://www.bas-rhin.gouv.fr/Actions-de-l-Etat/Elections-Elus/Elections-politiques/Elections-senatoriales-2026/Candidats/Calendrier-de-candidature-et-dossier-du-candidat

Ces pages ne remplacent pas la source applicable en Haute-Corse ; elles servent de **corroboration de l'interprétation administrative nationale 2026**.

### Travaux préparatoires de la loi de 2018

Le rapport du Sénat sur la proposition devenue loi n° 2018-51 éclaire la finalité de la mention manuscrite ajoutée à L.299 : il s'agit de **confirmer par écrit l'accord du remplaçant** et de réduire le risque de candidatures ou de suppléances formées à l'insu des personnes concernées.

Source officielle :
https://www.senat.fr/rap/l17-087/l17-0877.html

Cela crée un discriminant supplémentaire :

~~~text
finalité documentée de la formalité
= établir personnellement le consentement du remplaçant

question distincte
= quel support matériel doit porter cette manifestation de consentement ?
~~~

Cette distinction n'abolit pas le formalisme du dépôt. Elle permet simplement de séparer la **garantie recherchée par le législateur** de la question du **support exact exigé pour l'établir**.

### Résidu U7

Restent ouverts :

- contenu exact du mémento Haute-Corse / national 2026 sur le point invoqué par la préfecture ;
- éventuelles instructions locales supplémentaires ou consignes orales au dépôt ;
- portée juridique exacte de la notion d'« original » dans le régime sénatorial ;
- articulation entre la formalité substantielle, sa finalité de consentement et les possibilités concrètes de correction avant l'heure limite.

---

## RP-SEN-16 — reconstruction côté candidat

**Statut :** `partly answered / generative`

Le probe sépare désormais :

~~~text
U8a — bundle électronique
U8b — bundle physiquement présenté / remis lors du dépôt
~~~

**U8a est largement reconstruite. U8b reste ouverte.**

### 10 septembre

**17:01:56** — premier envoi électronique avec huit catégories de pièces ; rejet serveur pour dépassement de taille.

**17:54:50** — retransmission allégée, Gmail `1a08c07a7fbb141b`, avec huit catégories de pièces effectivement attachées : CERFA candidat, identité et situation électorale du candidat, CERFA remplaçante, identité et situation électorale de la remplaçante, désignation du mandataire financier, acceptation du mandataire.

Le message demande explicitement que toute pièce ou formalité manquante soit signalée afin de pouvoir régulariser sans délai.

**17:56:53** — accusé automatique préfectoral : réception de la saisine électronique confirmée, sans préjuger de sa recevabilité ou de sa complétude.

**20:05:04** — réponse préfectorale, Gmail `1a08c7eb62cc13ec`, indiquant explicitement que le CERFA dématérialisé n'est pas considéré comme recevable pour le dépôt et demandant la présentation des **originaux**, spécialement au regard de la mention du remplaçant et de la signature manuscrite originale.

### Conséquence pour U3 / Q18

L'existence d'**au moins une demande écrite d'originaux** par les services préfectoraux est désormais **établie**.

Ce qui reste ouvert est plus étroit :

> la formule du point 5 du jugement — « en dépit des demandes des services préfectoraux » — vise-t-elle seulement cette demande écrite du 10 septembre, ou aussi d'autres demandes, notamment lors du dépôt physique ?

### 11 septembre

**08:14:11** — le candidat répond avoir pris connaissance de la demande relative aux originaux et annonce sa venue physique.

**vers 12:10–12:20** — présence physique et délivrance du reçu provisoire. Le dossier TA situe l'arrivée vers 12:10 ; le courriel contemporain de 14:14 indique que le reçu provisoire a été remis à 12:20.

**14:14:39** — Gmail `1a0906430ac3adee` transmet deux formulaires relatifs au mandataire financier, établis selon les modèles du mémento après la régularisation proposée lors du passage. Le candidat y indique rester disponible jusqu'à 18 h pour toute demande complémentaire précise.

**16:14:05** — accusé humain du Bureau des élections : « J'accuse réception des documents. » Aucune nouvelle liste de défauts n'apparaît dans ce message.

**17:57:55** — Gmail `1a0913095d550884` envoie le lien vers la vidéo complémentaire. Le MIME source confirme l'heure d'émission côté expéditeur. L'heure d'acceptation côté destinataire reste U1.

### Autorisation de la remplaçante

Gmail `1a08ae5f35fd72f0` contient, avant l'échéance, une autorisation écrite expresse de Laurence Vernerey relative à l'apposition de sa signature sur le CERFA.

Cette trace établit l'autorisation ; elle ne tranche pas à elle seule la conformité juridique de la formalité.

### Empreintes de préservation

Les copies extraites de Gmail ont été hashées :

~~~text
2750b7541ba740ac97fbbe1e981ee7b9e7f25eb5e65187992c94ca2a9d391e6f  CERFA candidat — 10/09
92267e91e078b0f4d14ad66121224d0f9a0955e6ef9c86b6cd40f94549eb1417  CERFA remplaçante — 10/09
1d8fc52ed3abb1920f996314fd42ebba36cefe2a9801e2c67fbc3046c68aba3e  désignation mandataire — bundle 10/09
f3209fcebdad267378a9964277d441f5b5ba31d9f72700c9ebc9f02887a35a91  acceptation mandataire — bundle 10/09
15954a5344e8a125b8a6508259a0d97abca578e5911bd151182c82ddf5907d8b  formulaire mandataire — 11/09 14:14
9cd3ca041fa055e05f51b0eaf042aa7558905975c376a585dcf803e2862fd06c  accord mandataire — 11/09 14:14
~~~

### Gap génératif

Le bundle **physique** du dépôt n'est pas encore reconstruit avec la même précision que le bundle électronique.

Cela génère **RP-SEN-18**.

---

## RP-SEN-17 — jurisprudence comparable

**Statut :** `answered / continuing`

### J1 — refus d'enregistrement sénatorial contrôlé après l'élection

**Conseil constitutionnel, n° 2014-4909 SEN, 23 janvier 2015.**

Le Conseil a examiné dans le contentieux de l'élection le grief portant sur le refus préfectoral d'enregistrement d'une candidature sénatoriale.

Source :
https://qpc360.conseil-constitutionnel.fr/2015-01-23/decision-2014-4909-sen-23-janvier-2015

Le motif de refus concernait toutefois l'inéligibilité, non les signatures ou originaux.

### J2 — handicap et acte manuscrit accompli par un tiers

**Conseil d'État, 14 mai 2021, n° 445497 et 445540.**

Dans le régime municipal de L.265, le Conseil d'État juge que signature et mention manuscrite sont en principe personnelles. Il pose cependant une exception lorsqu'un handicap permanent ou provisoire fait obstacle à l'accomplissement personnel et que le consentement éclairé est établi : la signature **ou** la mention peut alors être apposée à la demande de la personne par un tiers sans invalider la candidature.

Dans l'affaire jugée, le candidat avait lui-même signé mais n'avait pu rédiger personnellement la mention en raison d'un handicap résultant d'un AVC ; il avait demandé à un tiers de l'apposer, et son consentement éclairé était établi.

Sources officielles :
- https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2021-05-14/445497
- https://www.legifrance.gouv.fr/ceta/id/CETATEXT000043741066

Ce précédent est **analogique** : il porte sur L.265, non sur L.299. Sa valeur exploratoire tient précisément à la proximité de structure entre les formalités de consentement issues de la loi de 2018, sans préjuger de leur transposition au scrutin sénatorial.

### J3 — photocopie / original et mécanisme spécial de complétion

**Conseil d'État, 31 mai 2004, n° 268145**, puis **4 juin 2004, n° 268279**, élections européennes.

Une déclaration déposée sous forme de simple photocopie a été déclarée irrégulière ; le régime particulier de cette élection permettait alors de la compléter sous 48 heures par production des originaux.

Sources :
- recherche Légifrance n° 268145 ;
- https://www.legifrance.gouv.fr/ceta/id/CETATEXT000008177056

La valeur est comparative seulement : autre scrutin, autre texte, mécanisme spécial de complétion.

### Résidu

Aucune décision officielle directement superposable n'a encore été identifiée combinant :

~~~text
sénatoriales
+ L.299
+ signature / mention du remplaçant
+ intervention d'un tiers
+ handicap
~~~

Cette absence de résultat n'est pas une preuve d'absence de jurisprudence.

---

# Diff de carte

## Réduction

- **U3 / Q18** : au moins une demande écrite d'originaux est maintenant établie.
- **U7** : noyau normatif structuré ; résidu plus étroit.
- **U8a** : bundle électronique largement reconstruit.

## Maintien

- **U1** : réception serveur du mail 17:57:55 ;
- **U2/U4/U5/U6** : inchangées en attente des réponses institutionnelles ;
- **U8b** : bundle physique exact du dépôt.

## Nouveau probe

### RP-SEN-18 — reconstruction du bundle physique du 11 septembre

**Fonctions :**
- PRESERVE
- REVEAL
- TRIANGULATE
- DISCRIMINATE

**Question :**

> quels documents exacts ont été matériellement présentés, remis, conservés ou rendus lors du dépôt physique entre l'arrivée vers 12:10 et le reçu provisoire vers 12:20 ?

**Sources à interroger d'abord sans nouveau contact :**

- récépissé provisoire ;
- scans / photographies / fichiers locaux conservés côté candidat ;
- pièces du dossier TA déjà disponibles ;
- requête préfectorale et inventaire Télérecours ;
- messages immédiatement postérieurs au dépôt.

**Sources conditionnelles :**

- réponse future de la préfecture à RP-SEN-01 ;
- réponse future du TA à RP-SEN-02.

**Règle :**

Ne pas demander à une institution ce qui peut être reconstruit d'abord depuis les traces propres déjà accessibles.

## Première exécution de RP-SEN-18

La recherche dans les traces propres et le gel documentaire du 12 septembre réduit déjà U8b.

Éléments désormais retrouvés :

- présence physique vers 12:10 et délivrance d'un reçu provisoire ;
- le gel du 12 septembre indique qu'**un seul document papier relatif au mandataire financier a été physiquement présenté** ;
- une autre projection contemporaine précise que la pièce dont l'existence physique est certaine est **le document signé par Marguerite (Maguy) Ghionga**, mandataire financière ;
- elle avertit explicitement qu'il serait factuellement inexact d'écrire que tous les documents précédemment transmis par courriel avaient été physiquement présentés ;
- les CERFA candidat et remplaçante sont par ailleurs décrits dans le dossier préfectoral comme signés dans leur version numérique, mais **non produits physiquement en version papier**.

Le Drive de préparation du 10 septembre contient les huit originaux numériques destinés à la préfecture, mais aucun récépissé provisoire ni snapshot supplémentaire du bundle physique n'a été retrouvé dans les dossiers Drive de candidature inspectés.

### État réduit de U8b

~~~text
établi / fortement documenté :
- présence physique
- reçu provisoire
- au moins une pièce papier : document signé par la mandataire financière
- CERFA candidat/remplaçante non produits physiquement sur papier

encore ouvert :
- identité exacte et exhaustivité des autres pièces éventuellement manipulées, montrées sans remise, ou rendues au guichet
- copie primaire du reçu provisoire et son éventuel inventaire / mentions
~~~

### Continuation

Avant tout nouveau contact externe :

1. rechercher une copie primaire du reçu provisoire hors des dossiers Drive déjà inspectés ;
2. comparer le dossier préfectoral / inventaire Télérecours avec cette reconstruction ;
3. attendre les réponses de RP-SEN-01 et RP-SEN-02 pour trianguler le bundle détenu par l'administration.

**Statut RP-SEN-18 après cette passe :** `partly answered / waiting for primary receipt or institutional triangulation`.


## Deuxième passe RP-SEN-18 — recherche du récépissé primaire

Une seconde recherche passive a été effectuée le 25 septembre sur les surfaces propres accessibles, sans nouveau contact externe.

### Google Drive

Le dossier racine **« Sénatoriales 2026 – Baron Mariani »** a été retrouvé puis listé directement.

Il contient deux sous-dossiers :

- `01 – Dossier Préfecture – originaux` ;
- `02 – Dossier public – versions expurgées`.

Le sous-dossier `01 – Dossier Préfecture – originaux` contient exactement huit fichiers correspondant au bundle numérique préparé le 10 septembre :

1. CERFA candidat ;
2. pièce d'identité candidat ;
3. situation électorale candidat ;
4. CERFA remplaçante ;
5. pièce d'identité remplaçante ;
6. situation électorale remplaçante ;
7. désignation du mandataire financier ;
8. acceptation / pièce du mandataire financier.

Aucun récépissé provisoire, photographie du récépissé ou artefact supplémentaire relatif au dépôt physique n'y apparaît.

Des recherches Drive supplémentaires sur les termes `récépissé`, `recepisse`, `reçu provisoire`, `sénatoriales`, `préfecture`, ainsi que plusieurs patrons de date / photographie, n'ont pas fait apparaître de copie primaire du récépissé.

### Gmail

Une recherche des messages avec pièces jointes autour des 11–12 septembre n'a pas retrouvé de scan ou photographie du récépissé.

Les pièces jointes pertinentes retrouvées sont les deux formulaires de mandataire transmis le 11 septembre à 14:14:39 et, le 12 septembre, une nouvelle transmission du CERFA candidat dans le cadre d'une demande distincte de vérification / rectification de données.

### Portée de ce résultat négatif

Le résultat correct est :

> **aucune copie primaire du récépissé provisoire n'a été retrouvée sur les surfaces Gmail / Drive interrogées.**

Il ne permet pas de conclure :

- que le récépissé n'existe plus ;
- qu'aucune photographie n'a jamais été prise ;
- qu'il n'existe pas sur un appareil local, un stockage non indexé, un support papier ou une autre surface.

### Nouveau discriminant

Les sources connectées accessibles étant désormais largement épuisées sur ce point, le prochain probe peu coûteux n'est plus une nouvelle recherche sémantique identique.

Il devient un probe de **localisation d'artefact physique / mémoire directe du déposant**, suivi seulement en cas de résultat par une inspection de la pièce.


## Troisième passe RP-SEN-18 / exécution RP-SEN-19 — récépissé retrouvé

Le récépissé provisoire primaire a été retrouvé le 25 septembre dans la bibliothèque de travail, dossier **« Candidature sénatoriale 2026 »**, sous deux formes privées :

- photographie : `2026-09-11_recepisse_provisoire_candidature_senatoriale.jpg` ;
- transcription visuelle : `2026-09-11_recepisse_provisoire_candidature_senatoriale_transcription.md`.

Le document lui-même établit directement :

- nature : **récépissé provisoire** de déclaration de candidature aux élections sénatoriales ;
- circonscription : **(2B) Haute-Corse** ;
- candidat porté sur le récépissé : **M. MARIANI BARON** ;
- remplaçante portée sur le récépissé : **Mme D’ANGELIS Marie-Louise** ;
- lieu : **Bastia** ;
- date et heure portées par l'administration : **11 septembre 2026 à 12H20 heure locale** ;
- signataire administratif indiqué : **Marie-Françoise RAFFALLI**, pour la préfète et par délégation, directrice des Collectivités territoriales et des Politiques publiques ;
- le texte précise que l'enregistrement ne sera effectué que lors de la remise du récépissé définitif, annoncée dans un délai maximal de quatre jours.

Particularité matérielle conservée sans correction : la formule **« donne récépissé provisoire à »** apparaît sans nom visible immédiatement après `à`, avant la ligne suivante relative à la déclaration de candidature.

Le déposant indique que la photographie a été prise à **12:37**. La copie JPEG actuellement conservée ne contient pas de métadonnée EXIF exploitable permettant de corroborer techniquement cette heure ; elle doit donc être conservée comme **heure rapportée par le déposant**, distincte de l'heure **12H20** imprimée sur le récépissé.

### Effet sur U8b

La présence physique et la prise en charge administrative du dépôt ne sont plus seulement établies par des projections et courriels postérieurs : elles disposent désormais d'une **source primaire contemporaine émise par la préfecture**.

Le récépissé ne comporte toutefois **aucun inventaire des pièces matériellement remises ou montrées au guichet**. Il ne résout donc pas, à lui seul, l'exhaustivité du bundle physique.

### État de RP-SEN-19

`answered / primary artifact found`

La branche « localiser le récépissé primaire » est fermée. La branche suivante reste :

```text
récépissé primaire retrouvé
→ heure administrative 12:20 établie
→ candidature et remplaçante telles qu'enregistrées sur le reçu établies
→ aucun inventaire des pièces sur le reçu
→ trianguler avec dossier préfectoral / TA et réponses RP-SEN-01 / RP-SEN-02
```

