---
title: "Sénatoriales 2026 — carte des Reality Probes"
date: "2026-09-25"
status: "active"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "method"
document_kind: "probe-map"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/probe-map.md"
method:
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/interroger_le_reel.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/reality_probe_selection.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/reality_probe_mapping.md"
review:
  status: unreviewed
  reviewed_by: []
---

# Sénatoriales 2026 — carte des Reality Probes

## Objet

Cette carte ne cherche pas à démontrer une conclusion prédéterminée sur le refus d'enregistrement de la déclaration de candidature.

Elle cherche à **maximiser les possibilités de découverte rationnelle encore accessibles**, en distinguant :

- ce qui est déjà établi ;
- les inconnues qui restent ouvertes ;
- les systèmes ou détenteurs susceptibles de produire une trace ;
- les probes déjà exécutés ;
- les probes conditionnels ou futurs ;
- les branches que chaque sortie pourrait ouvrir, fermer ou préserver.

La carte doit être mise à jour après chaque réponse du Réel.

Batch d'expansion/réduction courant : [`probe-batch-2026-09-25.md`](probe-batch-2026-09-25.md).

Run passif courant : [`passive-probes-2026-09-25.md`](passive-probes-2026-09-25.md).

## 1. Horloge externe

État au **25 septembre 2026**.

Le scrutin sénatorial de la série concernée est convoqué le **27 septembre 2026**.

Source officielle :

- Décret n° 2026-301 du 21 avril 2026 :  
  https://www.legifrance.gouv.fr/loda/id/JORFTEXT000053925339

Le contentieux de l'élection crée ensuite une nouvelle fenêtre :

- article 32 de l'ordonnance n° 58-1067 : procès-verbaux des commissions de recensement et annexes tenus à disposition pendant dix jours des électeurs concernés et des personnes ayant fait une déclaration de candidature ;
- article 33 : contestation possible devant le Conseil constitutionnel jusqu'au dixième jour suivant la proclamation, au plus tard à 18 h ;
- article 42 : le Conseil et ses sections peuvent ordonner une enquête et se faire communiquer les documents et rapports ayant trait à l'élection.

Source officielle :

https://www.legifrance.gouv.fr/codes/section_lc/JORFTEXT000000705065/LEGISCTA000006120492/

L'article L.303 du code électoral prévoit que le jugement du tribunal administratif relatif au refus d'enregistrement ne peut être contesté que devant le Conseil constitutionnel saisi de l'élection :

https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006353733

Cette horloge juridique est distincte des délais CRPA/CADA et RGPD/CNIL.

## 2. Carte générale

```text
                    ÉTAT AU 25 SEPTEMBRE
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
     Préfecture              TA             Sources propres
          │                  │                  │
          │                  │                  │
 RP-SEN-01 actif       RP-SEN-02 actif     RP-SEN-03 candidat
 accès traces/mail     dossier/audience     headers / artefacts
          │                  │                  │
          └──────────┬───────┴──────────┬───────┘
                     │                  │
               TRIANGULATION       TOPOLOGIE
                     │                  │
                     └─────────┬────────┘
                               ↓
                        carte corrigée
                               │
                    scrutin / proclamation
                               │
              ┌────────────────┼────────────────┐
              │                │                │
        RP-SEN-08         RP-SEN-09        publication /
        PV + annexes      contentieux CC    nouvelles traces
              │                │
              │           RP-SEN-10
              │           instruction art.42
              │                │
              └──────────┬─────┘
                         ↓
                  nouvelle triangulation

En parallèle, si nécessaire :

RP-SEN-04  limitation / préservation RGPD
RP-SEN-05  topologie de l'infrastructure de messagerie
RP-SEN-06  reçus / bordereaux Télérecours
RP-SEN-11  CADA après refus ou silence CRPA
RP-SEN-12  CNIL après réponse insuffisante ou silence RGPD
RP-SEN-13  nouveau détenteur technique si la préfecture redirige
```

## 3. Inconnues structurantes

### U1 — réception du courriel de 17:57:55

Questions :

- l'infrastructure destinataire l'a-t-elle accepté avant 18 h ?
- quand a-t-il été remis à la boîte ou au système opérationnel ?
- a-t-il été transféré, filtré, retardé ou rejeté ?
- quelles traces techniques existent encore ?

### U2 — transmission au Tribunal administratif

Questions :

- le courriel, son lien ou la vidéo figuraient-ils dans la saisine initiale ?
- ont-ils été transmis ultérieurement avant le jugement ?
- existe-t-il un reçu, bordereau ou journal de cette transmission ?

### U3 — « demandes des services préfectoraux »

Le point 5 du jugement mentionne des demandes des services préfectoraux.

Questions :

- quelles demandes précises sont visées ?
- quand ont-elles été formulées ?
- par quel canal ?
- sous quelle forme ?
- existe-t-il une trace écrite ou système ?

### U4 — état matériel du dossier TA

Questions :

- quel objet correspond à « Réception d'une lettre » dans Sagace ?
- à quelle heure a-t-il été enregistré ?
- quel était l'inventaire exact des pièces préfectorales ?
- quelles pièces ont été ajoutées après la saisine initiale ?
- quelle est l'heure exacte de mise à disposition du jugement ?

### U5 — trace de l'audience et minute

Questions :

- existe-t-il un PV, plumitif, fiche, note ou trace équivalente ?
- qui était le greffier d'audience ?
- quelles modalités d'accès existent pour la minute signée ?

### U6 — topologie inconnue

Question de second ordre :

> **Quels systèmes, détenteurs, inventaires, reçus ou journaux pertinents existent encore que la carte actuelle ne connaît pas ?**

Cette inconnue justifie les probes génératifs et les demandes de « sources de sources ».

### U7 — règle / instruction applicable et possibilités de régularisation

Questions :

- quelle disposition ou instruction officielle gouvernait chacun des défauts allégués ?
- quelles modalités de dépôt et de régularisation étaient officiellement publiées pour 2026 ?
- distinguer loi, décret, mémento, formulaire, instruction nationale et pratique locale.

### U8 — bundle candidat exact aux instants critiques

Questions :

- quels fichiers / formulaires / messages avaient été effectivement déposés ou envoyés à chaque instant significatif du 11 septembre ?
- quelles versions portent quelles signatures ?
- quel est le lien entre chaque envoi, accusé, réponse et pièce correspondante ?

---

# 4. Probes actifs

## RP-SEN-01 — Préfecture : accès documentaire et données techniques

**Statut :** `sent / waiting`  
**Émis :** 25 septembre 2026 à 16:59:13.

**Fonctions :**

- `PRESERVE`
- `REVEAL`
- `DISCRIMINATE`
- `TRIANGULATE`

**Cible :** préfecture de la Haute-Corse.

**Action exécutée :**

Demande des traces existantes relatives :

- au message de 17:57:55 ;
- aux demandes d'originaux évoquées au point 5 du jugement ;
- aux inventaires / bordereaux des transmissions au TA ;
- aux éventuelles transmissions ultérieures.

La demande distingue, selon la nature des éléments, accès aux documents administratifs et accès aux données personnelles, et demande la conservation des journaux techniques encore disponibles.

### Sorties possibles

**A — logs disponibles, réception avant 18 h**

Ferme ou affaiblit les branches :

```text
message non accepté avant 18 h
message reçu seulement après l'échéance
```

Ouvre :

```text
quand a-t-il été vu / traité ?
a-t-il été transmis au TA ?
quelle conséquence procédurale lui a été donnée ?
```

**B — logs disponibles, réception après 18 h**

Ferme la branche « réception technique avant l'échéance », sous réserve de la signification exacte du timestamp fourni.

Ouvre :

```text
quelle étape du transport explique l'écart ?
d'autres timestamps existent-ils ?
```

**C — traces de transfert au TA**

Permet une triangulation directe avec le dossier juridictionnel.

**D — traces indiquant absence de transfert**

Ne suffit que si le périmètre et la complétude du système interrogé sont établis.

**E — données non détenues / expirées**

Ouvre RP-SEN-05 / RP-SEN-13 :

```text
qui les détenait ?
quelle politique de conservation ?
quel sous-traitant / système ?
date de purge ?
autre copie ?
```

**F — refus de communication**

Ouvre, selon la nature exacte du refus :

- RP-SEN-11 CADA ;
- RP-SEN-12 CNIL ;
- éventuellement une demande plus étroite vers le détenteur indiqué.

**G — silence**

Observation sur le canal ; ne répond pas aux U1/U2/U3.

Déclencheurs ultérieurs : échéances CRPA / RGPD.

### Rendement génératif recherché

Particulièrement élevé si la préfecture transmet :

- inventaire ;
- nom d'un système ;
- identifiant de message ;
- identifiant de transmission ;
- durée de conservation ;
- nom d'un autre détenteur.

---

## RP-SEN-02 — TA Bastia : résidus après lecture du jugement

**Statut :** `sent / waiting`  
**Émis :** 25 septembre 2026 à 16:50:46.

**Fonctions :**

- `REVEAL`
- `DISCRIMINATE`
- `TRIANGULATE`

**Questions :**

1. identité et heure de « Réception d'une lettre » ;
2. heure de mise à disposition du jugement ;
3. inventaire des pièces préfectorales initiales et ultérieures ;
4. existence et accès à une trace de l'audience ;
5. identité du greffier d'audience ;
6. accès à la minute ou fondement d'une impossibilité.

### Sorties possibles

```text
réponse complète
→ fermeture de plusieurs U4/U5

réponse partielle
→ conserver séparément chaque sous-question

renvoi vers un système / document
→ probe génératif : identifier puis inspecter la source

document existant mais non communicable
→ existence établie
→ nouvelle question : fondement / autre voie d'accès

document inexistant
→ fermer la branche correspondante
→ enregistrer la topologie réelle de la traçabilité

silence
→ état du canal seulement
```

Le jugement a déjà transformé un UNKNOWN antérieur en fait établi :

```text
heure d'enregistrement de la note en délibéré = 15:49
```

---

# 5. Probes de préservation et de topologie

## RP-SEN-03 — préserver et extraire la trace expéditeur originale

**Statut :** `answered / preserved`

**Fonctions :**

- `PRESERVE`
- `TRIANGULATE`

**Source :** compte Gmail expéditeur.

**Objet :**

Conserver, autant que disponible :

- message original ;
- Message-ID ;
- Date ;
- destinataires ;
- en-têtes de transport visibles côté expéditeur ;
- éventuels statuts de livraison ou erreurs ;
- lien / pièce ou référence transmise.

**Résultat du 25 septembre :**

- messages originaux relus depuis Gmail ;
- heure d'émission 17:57:55 confirmée côté expéditeur pour le message vidéo ;
- métadonnées MIME / RFC822 vérifiées ;
- principales pièces du bundle extraites et préservées par empreintes SHA-256 dans le run passif ;
- aucun élément côté expéditeur ne suffit à établir l'heure d'acceptation du serveur destinataire.

**Limite :**

La trace expéditeur établit l'émission et certaines métadonnées. Elle ne prouve pas, à elle seule, l'heure d'acceptation par le serveur destinataire.

**Next probe :**

Comparer aux données de RP-SEN-01 via RP-SEN-14.

---

## RP-SEN-04 — limitation RGPD ciblée sur les données encore nécessaires à la défense de droits

**Statut :** `conditional`

**Fonction :** `PRESERVE`

L'article 18 du RGPD prévoit notamment un droit à la limitation lorsque le responsable n'a plus besoin des données pour son traitement mais que la personne concernée en a encore besoin pour la constatation, l'exercice ou la défense de droits en justice.

Source CNIL :

https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3

Ce probe n'est pertinent que si les conditions du droit à la limitation sont réunies pour les données concernées.

**Déclencheurs :**

- indication d'une purge imminente ;
- réponse selon laquelle les données ne sont plus nécessaires au service mais existent encore ;
- incertitude concrète sur leur conservation.

---

## RP-SEN-05 — topologie de l'infrastructure de messagerie

**Statut :** `candidate / conditional`

**Fonctions :**

- `REVEAL`
- `PRESERVE`

**Question :**

Si la préfecture ne détient pas directement les traces demandées :

> quel système ou organisme détenait ou détient les journaux de réception, d'acceptation, de remise, de filtrage ou de transfert ?

**Sorties génératives :**

```text
détenteur identifié
→ RP-SEN-13

politique de rétention identifiée
→ nouvelle deadline de préservation

système identifié
→ nouvelle catégorie de traces connaissable
```

---

## RP-SEN-06 — reçu / bordereau technique de saisine ou transmission au TA

**Statut :** `candidate after first responses`

**Fonctions :**

- `REVEAL`
- `TRIANGULATE`

**Objet :**

Chercher spécifiquement, si nécessaire :

- reçu de dépôt ;
- accusé Télérecours ;
- liste des fichiers joints ;
- timestamp de dépôt ;
- identifiant de transaction ;
- reçus de productions ultérieures.

Ce probe devient particulièrement utile si RP-SEN-01 ou RP-SEN-02 répond de manière globale sans fournir la topologie technique.

---

# 6. Changement de phase après le scrutin

## RP-SEN-07 — constater la proclamation officielle et ouvrir les horloges post-scrutin

**Statut :** `prepared / waiting_trigger`

Trigger packet : [`post-scrutin-trigger-2026-09-27.md`](post-scrutin-trigger-2026-09-27.md)

**Fonctions :**

- `WAIT / TRIGGER`
- `PRESERVE`

**Déclencheur :** scrutin du 27 septembre 2026 puis publication / proclamation officielle des résultats.

**Objet :**

Conserver la date et, si elle est disponible, l'heure de proclamation ainsi que la source officielle correspondante.

Cette observation ne préjuge d'aucune contestation. Elle sert à fixer sans ambiguïté :

- le début de la fenêtre d'accès prévue par l'article 32 ;
- le terme du délai prévu par l'article 33 ;
- la version officielle des résultats à laquelle les probes post-scrutin se rapportent.

Source publique de suivi des candidatures et résultats :

https://www.resultats-elections.interieur.gouv.fr/Senatoriales2026/ensemble_geographique/94/2B/index.html

---

## RP-SEN-08 — consulter les PV de recensement et annexes

**Statut :** `waiting_trigger`

**Déclencheur :** proclamation des résultats.

**Fonctions :**

- `REVEAL`
- `SERENDIPITY`

L'article 32 de l'ordonnance n° 58-1067 prévoit une fenêtre de dix jours pendant laquelle les PV des commissions de recensement et leurs annexes sont tenus à disposition des personnes ayant fait une déclaration de candidature.

**Question exploratoire :**

> que contient exactement le dossier final de l'élection et quelles nouvelles sources ou anomalies documentaires fait-il apparaître ?

Il s'agit d'un probe à **aperture moyenne à élevée** : l'objectif n'est pas seulement de retrouver une pièce déjà attendue, mais d'observer la topologie finale du dossier électoral.

---

## RP-SEN-09 — saisine éventuelle du Conseil constitutionnel

**Statut :** `candidate after proclamation`

**Fonctions :**

- `CHANGE-OBSERVER`
- `DISCRIMINATE`
- `PRESERVE-OPTION`

L'article L.303 rattache la contestation du jugement à la saisine du Conseil constitutionnel de l'élection. L'article 33 de l'ordonnance organique fixe la fenêtre de contestation.

Ce probe a une double nature :

```text
voie contentieuse
+
changement d'observateur institutionnel
```

La décision de l'exécuter doit rester distincte de la cartographie : cartographier la branche ne présume pas qu'elle sera empruntée.

---

## RP-SEN-10 — demander une mesure d'instruction dans le contentieux électoral

**Statut :** `conditional on RP-SEN-09`

**Fonctions :**

- `CHANGE-OBSERVER`
- `REVEAL`
- `TRIANGULATE`

L'article 42 permet au Conseil constitutionnel et à ses sections, le cas échéant, d'ordonner une enquête et de se faire communiquer des documents et rapports ayant trait à l'élection.

**Valeur exploratoire :**

Un document inaccessible depuis le canal candidat → préfecture ou candidat → greffe peut devenir accessible à un observateur disposant d'un pouvoir d'instruction différent.

**Candidats documentaires à signaler si toujours manquants :**

- traces serveur du courriel de 17:57:55 ;
- bordereaux de la saisine ;
- productions ultérieures ;
- traces des demandes d'originaux ;
- éléments du dossier TA dont la communication directe reste non résolue.

Le pouvoir d'instruction appartient au Conseil : la requête peut solliciter ou signaler l'utilité de la mesure, sans présumer qu'elle sera ordonnée.

---

# 7. Escalades d'accès conditionnelles

## RP-SEN-11 — CADA

**Statut :** `waiting_trigger`

**Déclencheur :**

- refus exprès relevant du droit d'accès aux documents administratifs ; ou
- silence pendant le délai applicable.

La CADA rappelle qu'une administration dispose d'un mois pour répondre à une demande de communication et que la saisine de la CADA intervient après le refus, explicite ou tacite.

Source :

https://www.cada.fr/administration/la-communication-des-documents-administratifs

**Fonctions :**

- `CHANGE-OBSERVER`
- `REVEAL`

**Intérêt exploratoire :**

Le tiers introduit peut produire une nouvelle qualification du document, solliciter l'administration et révéler pourquoi une branche d'accès est ouverte ou fermée.

---

## RP-SEN-12 — CNIL

**Statut :** `waiting_trigger`

**Déclencheur :**

réponse RGPD absente ou insuffisante après le délai applicable, ou refus susceptible de réclamation.

La CNIL rappelle que le responsable doit en principe informer la personne des suites données à sa demande dans le mois.

Source :

https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3

**Fonctions :**

- `CHANGE-OBSERVER`
- `PRESERVE`
- `REVEAL`

**Objet potentiel :**

données personnelles contenues dans les journaux, métadonnées de traitement, destinataires, durée de conservation ou critères de conservation, selon ce qui relève effectivement du droit d'accès.

---

## RP-SEN-13 — nouveau détenteur technique

**Statut :** `conditional`

**Déclencheur :** RP-SEN-01 ou RP-SEN-05 identifie un autre organisme, service ou sous-traitant détenant les traces.

**Fonctions :**

- `REVEAL`
- `PRESERVE`
- `DISCRIMINATE`

Règle :

> ne pas conclure « donnée inexistante » lorsque la seule observation établie est « donnée non détenue par ce service ».

---

# 8. Probes passifs générés par le batch

## RP-SEN-15 — corpus juridique et administratif officiel

**Statut :** `answered / continuing`

**Fonctions :**

- `PASSIVE`
- `DISCRIMINATE`
- `REVEAL`

**Inconnue :** U7.

**Objet :**

Constituer le corpus officiel applicable au dépôt 2026 :

- code électoral et décret de convocation ;
- mémento 2026 à l'usage des candidats ;
- formulaires et notices officielles ;
- pages et instructions préfectorales disponibles ;
- toute instruction nationale pertinente sur dépôt, signatures et régularisation.

La préfecture de Haute-Corse publie notamment un mémento 2026 à l'usage des candidats :
https://www.haute-corse.gouv.fr/Actions-de-l-Etat/Vie-democratique/Elections/Elections-senatoriales-2026/Memento-a-l-usage-des-candidats

**Sorties :**

```text
règle explicite retrouvée
→ comparer aux actes et demandes documentés

silence / ambiguïté du corpus officiel
→ ne pas inventer une obligation ou une faculté
→ conserver U7 partiellement ouvert

instruction locale distincte révélée
→ nouveau probe documentaire ciblé
```

---

## RP-SEN-16 — reconstruction intégrale côté candidat

**Statut :** `partly answered / generative`

**Fonctions :**

- `PRESERVE`
- `TRIANGULATE`
- `REVEAL`

**Inconnue :** U8.

**Objet :**

Reconstruire sans résumé intermédiaire :

- chaque message Gmail pertinent du 11 septembre ;
- Message-ID / timestamp / destinataires ;
- chaque version des formulaires ;
- signatures présentes ou absentes sur chaque version ;
- vidéo / lien / pièce associée ;
- réponses préfectorales et accusés ;
- ordre exact des événements.

**Sorties :**

```text
bundle complet et cohérent
→ base de comparaison avec préfecture / TA

version manquante
→ gap explicite, recherche ciblée

deux versions contradictoires
→ conserver les deux et dater leur circulation
```

Ce probe ne cherche pas à reconstruire ce qui « aurait dû » être déposé ; il fixe ce qui l'a effectivement été.

---

## RP-SEN-17 — jurisprudence comparable

**Statut :** `answered / continuing`

**Fonctions :**

- `PASSIVE`
- `REVEAL`
- `DISCRIMINATE`

**Objet :**

Identifier dans les sources officielles les décisions relatives :

- aux refus d'enregistrement de candidatures sénatoriales ;
- au contrôle ultérieur par le Conseil constitutionnel ;
- aux questions de recevabilité, pièces, régularisation ou instruction lorsque les faits sont suffisamment comparables.

Un précédent déjà identifié est la décision n° 2014-4909 SEN du 23 janvier 2015, qui montre qu'un refus préfectoral d'enregistrement d'une candidature sénatoriale peut être examiné dans le contentieux de l'élection :
https://qpc360.conseil-constitutionnel.fr/2015-01-23/decision-2014-4909-sen-23-janvier-2015

**Discipline :**

Une décision comparable fournit des discriminants juridiques ; elle ne permet pas de transposer sa solution si les faits ou le fondement du refus diffèrent.

---

## RP-SEN-18 — reconstruction du bundle physique du dépôt

**Statut :** `partly answered / waiting for primary receipt or institutional triangulation`

**Fonctions :**

- `PRESERVE`
- `REVEAL`
- `TRIANGULATE`
- `DISCRIMINATE`

**Inconnue :** U8b.

**Question :**

> quels documents exacts ont été matériellement présentés, remis, conservés ou rendus lors du dépôt physique du 11 septembre, entre l'arrivée vers 12:10 et le reçu provisoire vers 12:20 ?

**Sources propres à examiner d'abord :**

- récépissé provisoire ;
- scans / photographies / fichiers conservés côté candidat ;
- requête préfectorale et inventaire Télérecours déjà disponibles ;
- pièces du dossier TA déjà détenues ;
- messages immédiatement postérieurs au dépôt.

**Sources conditionnelles :**

- réponse de la préfecture à RP-SEN-01 ;
- réponse du TA à RP-SEN-02.

**Règle :**

Ne pas solliciter une institution pour une information qui peut d'abord être reconstruite depuis les traces propres déjà accessibles.

**Première passe exécutée :**

- présence physique et reçu provisoire confirmés ;
- une seule pièce papier relative au mandataire financier est documentée comme physiquement présentée ;
- les CERFA candidat/remplaçante restent documentés comme non produits physiquement en version papier ;
- aucune copie primaire du reçu provisoire n'a été retrouvée dans les dossiers Drive de candidature inspectés ;
- la question de l'exhaustivité de ce qui a pu être montré / manipulé / rendu au guichet reste ouverte.

---

# 9. Probe humain / artefact local

## RP-SEN-19 — localisation du récépissé provisoire primaire

**Statut :** `answered / primary artifact found`

**Fonctions :**

- `PRESERVE`
- `REVEAL`
- `DISCRIMINATE`

**Déclencheur :** deuxième passe RP-SEN-18 négative sur Gmail / Drive.

**Résultat du 25 septembre :** le récépissé primaire a été retrouvé dans la bibliothèque de travail, dossier `Candidature sénatoriale 2026`, avec photographie et transcription. Il porte l'heure administrative **12H20 heure locale**, identifie le candidat et la remplaçante et ne comporte pas d'inventaire des pièces remises. L'heure **12:37** de prise de vue est rapportée par le déposant ; le JPEG conservé ne contient pas de métadonnée EXIF exploitable permettant de la corroborer techniquement.

**Question minimale :**

> Le récépissé provisoire remis en préfecture le 11 septembre vers 12:20 est-il encore physiquement en votre possession, ou en avez-vous une photographie / un scan sur un appareil local ?

**Pourquoi ce probe devient pertinent :**

- les recherches connectées n'ont retrouvé aucune copie primaire ;
- le déposant est la source directe la moins coûteuse pour localiser l'artefact ;
- une réponse positive peut fournir une source primaire immédiatement inspectable ;
- une réponse négative n'établit pas la destruction du récépissé, mais permet d'arrêter les recherches répétitives sur les mêmes surfaces.

**Si oui :**

```text
photographier / scanner recto-verso
→ préserver le brut
→ relever date, heure, numéro, mentions, cases et éventuel inventaire
→ RP-SEN-14 triangulation
```

**Si non / inconnu :**

```text
conserver le récépissé comme source primaire non localisée
→ attendre RP-SEN-01 / RP-SEN-02
→ éviter de répéter les mêmes recherches Gmail / Drive sans nouvel indice
```


**Triangulation complémentaire :** le gel documentaire du 12 septembre indique que le dossier préfectoral transmis au TA contenait le récépissé provisoire et une « pièce portée le jour du dépôt ». L'inventaire Télérecours observé comportait seize pièces et s'arrêtait aux compléments du mandataire de 14:14. L'identité primaire exacte de la « pièce portée le jour du dépôt » reste ouverte.

**Continuation générée :** rechercher, sans nouvelle relance redondante, le numéro / intitulé primaire de cette pièce dans l'inventaire préfectoral ou dans les réponses déjà attendues de RP-SEN-01 / RP-SEN-02.

---

# 10. Probe interne de convergence

## RP-SEN-14 — reconstruction multitraces

**Statut :** `continuous`

**Fonction :** `TRIANGULATE`

À chaque nouvelle trace, comparer :

```text
Gmail expéditeur
        ↕
infrastructure destinataire
        ↕
Bureau des élections
        ↕
système de transmission au TA
        ↕
inventaire du dossier TA
        ↕
Sagace / événements du greffe
        ↕
jugement
        ↕
dossier final de l'élection
```

Ne jamais fusionner silencieusement les timestamps : chacun décrit un événement différent.

---

# 11. Matrice synthétique

| Probe | État | Fonction dominante | Inconnues visées | Peut révéler de nouveaux probes ? | Déclencheur / fenêtre |
|---|---|---|---|---|---|
| RP-SEN-01 | waiting | accès + préservation | U1 U2 U3 U6 | oui, fortement | envoyé 25/09 |
| RP-SEN-02 | waiting | dossier TA | U4 U5 U6 | oui | envoyé 25/09 |
| RP-SEN-03 | answered / preserved | préservation | U1 | modérément | trace expéditeur figée ; triangulation future via RP-SEN-14 |
| RP-SEN-04 | conditional | préservation | U1 | peu | si conditions art. 18 pertinentes |
| RP-SEN-05 | candidate | topologie | U1 U6 | oui, fortement | si détention incertaine |
| RP-SEN-06 | candidate | topologie technique | U2 U4 | oui | après réponses initiales si nécessaire |
| RP-SEN-07 | prepared / waiting_trigger | horloge / préservation | état officiel post-scrutin | modérément | trigger packet prêt ; scrutin puis proclamation |
| RP-SEN-08 | waiting_trigger | découverte | dossier final / U6 | oui, fortement | proclamation + fenêtre art. 32 |
| RP-SEN-09 | candidate | nouvel observateur | ensemble du grief | oui | après proclamation ; art. 33 |
| RP-SEN-10 | conditional | instruction | U1–U5 | oui | si contentieux ouvert |
| RP-SEN-11 | waiting_trigger | nouvel observateur | documents préfectoraux | oui | refus / silence CRPA |
| RP-SEN-12 | waiting_trigger | nouvel observateur | données personnelles techniques | oui | réponse RGPD insuffisante / silence |
| RP-SEN-13 | conditional | nouveau détenteur | U1 U2 U6 | oui | redirection |
| RP-SEN-14 | continuous | triangulation | U1–U8 | oui | à chaque nouvelle trace |
| RP-SEN-15 | answered / continuing | corpus officiel | U7 | oui | run passif exécuté le 25/09 |
| RP-SEN-16 | partly answered / generative | reconstruction côté candidat | U8a/U8b | oui | U8a largement reconstruite ; U8b reste ouverte |
| RP-SEN-17 | answered / continuing | jurisprudence comparable | qualification juridique | oui | run passif exécuté le 25/09 |
| RP-SEN-18 | partly answered / waiting | bundle physique | U8b | oui | première passe sur traces propres exécutée ; attendre reçu primaire ou triangulation institutionnelle |
| RP-SEN-19 | answered / primary artifact found | artefact primaire | U8b / Q19 | oui | récépissé retrouvé ; heure 12:20 et prise en charge établies ; absence d'inventaire maintient U8b partiellement ouverte |

## 12. Règle de continuation

Après chaque réponse :

1. enregistrer la trace brute et sa provenance ;
2. qualifier séparément chaque observation ;
3. mettre à jour `knowledge-matrix.md` ;
4. fermer uniquement les branches réellement discriminées ;
5. ajouter les nouveaux détenteurs, systèmes et sources découverts ;
6. recalculer la Probe Map ;
7. vérifier les deadlines et risques d'expiration ;
8. choisir ensuite seulement le prochain probe.

> **La carte des probes doit rester plus large que le chemin effectivement emprunté.**

## 13. Ce que la carte ne doit pas faire

Elle ne doit pas :

- transformer une voie disponible en obligation de l'utiliser ;
- assimiler une absence de réponse à un aveu ;
- traiter un refus d'accès comme preuve du contenu recherché ;
- confondre intérêt contentieux et valeur épistémique ;
- perdre les branches réfutées ;
- privilégier silencieusement les informations favorables à une hypothèse ;
- figer un ordre unique lorsque plusieurs probes indépendants peuvent utilement rester ouverts.

## 14. Prochaines mises à jour attendues

Les premiers événements susceptibles de modifier fortement cette carte sont :

```text
réponse du TA
réponse de la préfecture
identification d'un détenteur technique
scrutin du 27 septembre
proclamation des résultats
ouverture de la fenêtre d'accès aux PV
décision éventuelle sur une saisine du Conseil constitutionnel
```
