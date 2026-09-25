---
title: "Sénatoriales 2026 — ledger temporel des défauts / insuffisances signalés"
date: "2026-09-25"
status: "active"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "evidence-map"
document_kind: "defect-ledger"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/defect-ledger.md"
related:
  - "chronology.md"
  - "knowledge-matrix.md"
  - "probe-map.md"
  - "passive-probes-2026-09-25.md"
privacy_rule: "No raw identity document, signature image, health datum or private attachment is republished here."
review:
  status: unreviewed
  reviewed_by: []
---

# Ledger temporel des défauts / insuffisances signalés

## Objet

Ce ledger répond à une question différente de l'inventaire des pièces :

> **À chaque instant critique, quels défauts ou insuffisances étaient explicitement signalés, lesquels avaient été complétés, lesquels restaient documentés comme ouverts, et lesquels n'étaient pas documentés comme ayant été signalés ?**

Il ne présume pas qu'un défaut était juridiquement fondé ni qu'une correction suffisait à rendre la candidature conforme.

Il sépare quatre dimensions :

~~~text
existence matérielle d'un document
≠
signalement d'un défaut
≠
complétion / transmission
≠
conformité juridique finale
~~~

## 1. Statuts du ledger

~~~yaml
signaled:
  meaning: "défaut ou insuffisance explicitement signalé par une trace"
reported_signaled:
  meaning: "signalement rapporté par le candidat mais pas encore corroboré par une trace institutionnelle indépendante"
completed:
  meaning: "élément demandé transmis / accompli avant l'échéance"
acknowledged_received:
  meaning: "réception de la complétion explicitement accusée"
still_open:
  meaning: "défaut documenté comme restant non résolu à cet instant"
not_re_signaled_in_known_trace:
  meaning: "aucun nouveau signalement écrit identifié dans les traces actuellement connues ; ne prouve pas l'absence de signalement oral ou d'une trace non retrouvée"
not_a_prefectural_ground_identified:
  meaning: "élément connu mais non identifié comme motif de la saisine dans les sources actuelles"
unknown:
  meaning: "état non résolu"
~~~

---

# 2. Défauts / insuffisances suivis

## D-SEN-01 — présentation des originaux / support matériel des CERFA

**Nature :** dépôt / support / signatures.

**Première trace connue :** 10 septembre 2026, 20:05.

La réponse préfectorale du 10 septembre indique que le CERFA dématérialisé n'est pas considéré comme recevable pour le dépôt et demande la présentation des originaux lors du dépôt du lendemain, avec une attention particulière portée aux signatures et à la mention de la remplaçante.

**État :**

~~~text
10/09 20:05
SIGNALÉ PAR ÉCRIT

11/09 matin
candidat annonce sa venue physique

11/09 ~12:10–12:20
comparution physique + reçu provisoire
mais originaux papier des CERFA non documentés comme physiquement produits

11/09 après 12:20
aucune trace écrite actuellement identifiée montrant que ce défaut a été déclaré résolu

14/09 jugement
défaut retenu : absence des formulaires originaux / signatures manuscrites originales
~~~

**Point ouvert :**

> Entre la remise du reçu provisoire et 18 h, quelles demandes précises ont été faites au candidat concernant ce défaut, et par quel canal ?

Le jugement mentionne des « demandes des services préfectoraux » au pluriel. Une demande écrite du 10 septembre est établie ; l'existence d'autres demandes reste ouverte.

---

## D-SEN-02 — acte personnel de la remplaçante : signature et mention manuscrite

**Nature :** consentement / signature / mention.

**Base normative :** l'article L.299 prévoit l'acceptation écrite du remplaçant, sa signature et la mention manuscrite prescrite.

**Faits connus :**

- le CERFA transmis numériquement comportait une signature et une mention ;
- l'auteur matériel et le mode d'apposition ont ensuite été documentés côté candidat ;
- la préfecture a indiqué ne pas pouvoir vérifier l'authenticité en l'absence des originaux ;
- le jugement a retenu l'absence de signature manuscrite originale.

**État :**

~~~text
10/09 20:05
SIGNALÉ PAR ÉCRIT sous l'angle des originaux / authenticité

11/09 avant 18 h
consentement / autorisation documentés par plusieurs traces côté candidat
mais conformité juridique de l'acte personnel non résolue

14/09
défaut retenu par le jugement
~~~

**Ne pas fusionner :**

~~~text
consentement factuel
≠
acte personnel matériel
≠
support original
≠
conformité juridique
~~~

---

## D-SEN-03 — documents relatifs au mandataire financier

**Nature :** complétude documentaire.

**Signalement :** pendant le passage en préfecture le 11 septembre, un agent aurait indiqué que deux formulaires concernant le mandataire financier manquaient.

Statut du signalement : **reported_signaled**.

**Complétion indépendante établie :**

- 14:14:39 — envoi des deux formulaires demandés ;
- 16:14:05 — réponse humaine du Bureau des élections : « J'accuse réception des documents. »

**État :**

~~~text
~12:20
REPORTED_SIGNALÉ

14:14:39
COMPLETED

16:14:05
ACKNOWLEDGED_RECEIVED

après 16:14
aucun nouveau défaut relatif à ces deux formulaires actuellement identifié
~~~

Le fait que la réception soit accusée ne vaut pas validation juridique de l'ensemble de la candidature.

---

## D-SEN-04 — variation de la mention manuscrite / indication des prénoms du candidat

**Nature :** contenu littéral de la mention.

Une projection de défense du 12 septembre relevait une variation apparente de la formule portée sur le CERFA, notamment l'absence apparente de « Noël » dans l'indication du candidat.

**État :**

~~~text
connu côté défense avant l'audience
NOT_A_PREFECTURAL_GROUND_IDENTIFIED dans les sources actuellement disponibles
~~~

Le mémoire de travail précise que la préfecture n'avait pas fondé sa saisine sur cette variation.

**Discipline :** ne pas transformer cette observation en défaut administratif effectivement signalé sans nouvelle source.

---

## D-SEN-05 — vidéo / preuve complémentaire du consentement

**Nature :** preuve complémentaire, non formalité de dépôt.

**État :**

~~~text
17:57:55
élément complémentaire envoyé côté candidat

18:00
heure d'acceptation destinataire inconnue

18:16
absent de l'inventaire initial Télérecours connu
~~~

La vidéo n'est pas traitée comme correction formelle de D-SEN-01 ou D-SEN-02. Elle avait pour fonction déclarée de documenter identité, volonté et consentement.

---

# 3. Ledger temporel

| Instant | Défauts / insuffisances explicitement connus | Action / changement | État épistémique après l'instant |
|---|---|---|---|
| 10/09 17:54:50 | dossier électronique envoyé ; complétude non encore appréciée dans une réponse humaine | huit catégories de pièces transmises | réception électronique établie, conformité inconnue |
| 10/09 20:05:04 | **D-SEN-01 / D-SEN-02 signalés par écrit** : présentation des originaux, signatures / mention de la remplaçante | préfecture demande présentation des originaux le lendemain | défauts connus du candidat avant sa venue |
| 11/09 08:14:11 | mêmes défauts connus | candidat indique avoir pris connaissance et annonce sa venue | disponibilité pour correction physique établie côté candidat |
| ~12:10 | D-SEN-01/D-SEN-02 non documentés comme résolus ; **D-SEN-03 signalé oralement selon le candidat** | présence physique au guichet | contenu exact des échanges oraux partiellement inconnu |
| 12:20 | conformité non acquise | **reçu provisoire** délivré | déclaration prise en charge dans la séquence L.301 ; conformité finale non établie |
| après 12:20 | D-SEN-03 en cours de correction | récupération / remplissage des formulaires mandataire rapportés | correction en préparation |
| 14:14:39 | D-SEN-03 | deux formulaires mandataire transmis | completed |
| 16:14:05 | D-SEN-03 | réception accusée par le BEDL | acknowledged_received ; aucun nouveau défaut écrit dans ce message |
| 16:14–17:57 | D-SEN-01/D-SEN-02 : aucun nouveau signalement écrit retrouvé à ce stade | candidat reste disponible selon son message de 14:14 | not_re_signaled_in_known_trace ≠ absence de défaut |
| 17:57:55 | D-SEN-02 : preuve de consentement encore renforcée côté candidat ; conformité matérielle toujours litigieuse | vidéo complémentaire envoyée | émission établie ; acceptation côté destinataire inconnue |
| 18:00 | clôture | fin de la fenêtre de dépôt | état final des défauts tel que détenu par l'administration à cette seconde encore incomplet dans notre carte |
| 18:16 | saisine TA | inventaire initial pièces 1–16 | vidéo 17:57 absente de l'inventaire initial connu |
| 14/09 | D-SEN-01/D-SEN-02 retenus dans le jugement | refus d'enregistrement | la motivation juridictionnelle ne permet pas encore d'identifier toutes les demandes concrètes faites entre 12:20 et 18:00 |

---

# 4. Fenêtre critique 12:20 → 18:00

Le ledger révèle que l'espace le plus informatif n'est plus toute la journée du 11 septembre, mais la fenêtre suivante :

~~~text
12:20
reçu provisoire
    │
    ├── D-SEN-03 : défaut signalé → complété → réception accusée
    │
    └── D-SEN-01 / D-SEN-02 :
         défauts connus depuis la veille
         mais trajectoire précise au guichet / après le guichet encore incomplète
              │
              ├── demande répétée ?
              ├── impossibilité déclarée ?
              ├── proposition de correction ?
              ├── aucune nouvelle interaction ?
              └── trace existante mais non encore obtenue ?
                       ↓
                    18:00
~~~

Ce contraste est un **discriminant documentaire**, pas une conclusion sur la légalité :

> pour D-SEN-03, une boucle complète signalement → correction → accusé de réception est documentée ; pour D-SEN-01 / D-SEN-02, la demande écrite de la veille et le défaut retenu ensuite sont établis, mais la trajectoire intermédiaire du 11 septembre reste incomplète.

---

# 5. Audit du canal écrit entre 12:20 et 18:00

Une recherche Gmail ciblée sur le 11 septembre a été effectuée le 25 septembre.

### Résultat positif

Le message envoyé par le candidat à **14:14:39** contient trois éléments particulièrement discriminants :

1. il rattache explicitement les deux nouveaux formulaires à la **« régularisation proposée lors de [son] passage et [qu'il a] acceptée »** ;
2. il indique : **« Sauf avis contraire de votre part précisant un autre élément qui serait encore manquant, il me semble donc que la seule difficulté subsistante concerne la production d’“originaux”. »**
3. il précise rester disponible jusqu'à **18 heures** pour toute demande complémentaire précise et demande qu'un éventuel élément encore nécessaire lui soit indiqué **« sans délai »**.

À **16:14:05**, le Bureau des élections répond seulement :

> « J'accuse réception des documents. »

Aucun nouveau défaut ou élément manquant n'est mentionné dans cette réponse.

### Audit négatif borné

Les recherches Gmail du 25 septembre sur :

- tous les messages du 11 septembre provenant de `pref-elections@haute-corse.gouv.fr` ;
- plus largement, les messages provenant d'une adresse `@haute-corse.gouv.fr` ;
- les termes `original`, `manquant`, `compléter`, `régularisation`, `CERFA`, `remplaçant` ;

n'ont retrouvé **aucun autre message entrant de la préfecture le 11 septembre** que l'accusé de 16:14.

Le résultat correctement formulé est :

> **Dans les courriels Gmail actuellement accessibles, aucun re-signalement écrit d'un défaut supplémentaire entre 12:20 et 18:00 n'a été retrouvé après la demande explicite du candidat de 14:14 ; la seule réponse préfectorale retrouvée est l'accusé de réception de 16:14.**

Ce résultat n'établit pas :

- qu'aucun échange oral n'a eu lieu ;
- qu'aucun autre canal n'a été utilisé ;
- qu'aucune trace institutionnelle non présente dans Gmail n'existe ;
- que le défaut des originaux était juridiquement régularisé.

### Effet sur le ledger

Pour le **canal écrit Gmail**, D-SEN-01 / D-SEN-02 passent de :

```text
not_re_signaled_in_known_trace
```

à une qualification plus précise :

```text
written_channel_audited
→ aucun re-signalement écrit retrouvé après 14:14
→ accusé de réception simple à 16:14
→ résidu déplacé vers oral / notes internes / autre canal / dossier TA
```

Cela réduit U9 sans fermer U3/Q18.

---

# 6. Nouveau Reality Probe généré

## RP-SEN-20 — ledger des défauts actifs

**Statut :** active / passive + waiting

**Fonctions :**

- DISCRIMINATE
- TRIANGULATE
- REVEAL

**Question :**

> Pour chaque défaut qui a finalement motivé le refus, quel était son état exact à 12:20, 14:14, 16:14 et immédiatement avant 18:00 : signalé, expliqué, corrigible, corrigé, reçu, non résolu ou non re-signalé ?

**Sources actuelles :**

- Gmail 10–11 septembre ;
- récépissé provisoire primaire ;
- dossier préfectoral / inventaire Télérecours ;
- jugement ;
- traces propres du candidat.

**Sources attendues :**

- réponse RP-SEN-01 de la préfecture, notamment les traces des « demandes des services préfectoraux » ;
- réponse RP-SEN-02 du TA sur l'inventaire des pièces initiales / ultérieures ;
- toute pièce primaire retrouvée concernant l'échange au guichet.

### Sorties discriminantes

~~~text
trace d'une demande explicite après 12:20 sur D-SEN-01 / 02
→ ferme "aucun nouveau signalement documenté"
→ préciser heure, contenu, capacité matérielle de correction

trace proposant une modalité concrète de correction
→ nouvelle branche : correction offerte / acceptée / impossible / non effectuée

trace indiquant qu'aucune autre demande n'a été faite
→ réduit fortement U3/Q18

simple rappel générique aux originaux
→ maintient ouverte la question de la correction concrète au guichet

absence de trace
→ ne prouve pas absence d'échange oral
→ conserve distinction canal / proposition
~~~

---

# 7. Règle de mise à jour

Chaque nouvelle trace doit mettre à jour **un défaut identifié**, pas seulement la chronologie globale.

Format :

~~~yaml
defect_event:
  defect_id: D-SEN-..
  event_time: ...
  actor: ...
  channel: ...
  action: signaled|completed|acknowledged|rejected|re_signaled|resolved|unknown
  source: ...
  establishes: ...
  does_not_establish: ...
~~~

Le but est de pouvoir reconstruire à tout instant :

> **ce que le candidat savait devoir corriger, ce qu'il avait effectivement corrigé, ce que l'administration savait avoir reçu, et ce qui restait explicitement en litige.**
