---
title: "Sénatoriales 2026 — analyse des réseaux d'exposition politique du collège électoral de Haute-Corse"
subtitle: "Analyse nominative et agrégée sur le périmètre prioritaire (209 grands électeurs sur 616)"
date: "2026-09-27"
status: "active"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "investigation-synthesis"
document_kind: "electoral-analysis"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "corpus-research"
classification_confidence: "strong"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
source_documents:
  - "../data/electeurs_senatoriaux_2B_2026.csv"
  - "../data/annuaire_electeurs_senatoriaux_2B_2026.csv"
  - "https://www.haute-corse.gouv.fr/Actions-de-l-Etat/Vie-democratique/Elections/Elections-senatoriales-2026/Tableau-des-electeurs-pour-l-election-des-senateurs-du-27-septembre-2026"
  - "Extrait du registre des délibérations du Conseil municipal de la Ville de Bastia du 05 juin 2026"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Sénatoriales 2026 — Analyse des réseaux d'exposition politique du collège électoral de Haute-Corse

## 1. Cadre méthodologique et règles de délimitation

Ce document et l'annuaire associé (`../data/annuaire_electeurs_senatoriaux_2B_2026.csv` et `.json`) constituent la première projection analytique et nominative de l'issue #85 du dépôt `JeanHuguesRobert/barons-Mariani`.

### Règle d'or de non-inférence du vote secret
Conformément aux exigences de la doctrine d'investigation et du droit électoral :
1. **Le vote individuel au scrutin sénatorial est secret** : il est strictement impossible et prohibé de déduire le bulletin d'un électeur à partir de sa commune, de son étiquette ou d'une consigne politique.
2. **Distinction des trois plans** :
   - plan 1 : appartenance / liste municipale ou territoriale publique ;
   - plan 2 : consigne, déclaration publique ou exposition documentée ;
   - plan 3 : vote effectif (inconnaissable individuellement).
3. **Périmètre d'exposition** : une consigne politique mesure uniquement un *ensemble exposé* ou une capacité théorique d'influence, jamais une attribution de bulletin.
4. **Conservation des inconnues** : toute case ou affiliation non formellement établie par une source primaire ou recoupée est expressément codée `inconnue` / `inconnu`.

---

## 2. Synthèse agrégée sur le périmètre prioritaire

Le collège électoral sénatorial de Haute-Corse compte **616 électeurs inscrits**.
Le périmètre prioritaire défini par l'issue #85 regroupe **209 grands électeurs** (soit 33,9 % du collège total) :
- les 3 parlementaires (2 députés, 1 sénateur) ;
- les 34 conseillers territoriaux de Haute-Corse siégeant à l'Assemblée de Corse ;
- les 7 communes démographiquement et politiquement structurantes du département : Bastia (64), Corte (15), Biguglia (15), Borgo (33), Lucciana (15), Ghisonaccia (15), Calvi (15).

### Tableau récapitulatif par entité et type de consigne documentée

| Entité / Commune | Type électoral | Total inscrits | Consigne Parigi | Consigne Battini | Consigne Blanc | Consigne Inconnue |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Parlementaires** | De droit | 3 | 2 | 0 | 0 | 1 |
| **Assemblée de Corse** | De droit | 34 | 27 | 0 | 0 | 7 |
| **BASTIA** | 43 droit + 21 suppl. | 64 | 47 | 4 | 12 | 1 |
| **BIGUGLIA** | Délégués titulaires | 15 | 0 | 1 | 0 | 14 |
| **BORGO** | Délégués de droit | 33 | 0 | 0 | 0 | 33 |
| **CALVI** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **CORTE** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **GHISONACCIA** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **LUCCIANA** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **TOTAL PÉRIMÈTRE PRIORITAIRE** | — | **209** | **76** | **5** | **12** | **116** |
| *Reste du collège (communes rurales)* | Délégués titulaires | 407 | 0 | 0 | 0 | 407 |
| **TOTAL GÉNÉRAL CORSE-DU-NORD** | — | **616** | **76** | **5** | **12** | **523** |

---

## 3. Analyse détaillée par pôle d'observation

### 3.1. Les 5 grands électeurs documentés de Mossa Palatina / Nicolas Battini
La presse régionale (France 3 Corse ViaStella, Alta Frequenza) rapportait que le mouvement identitaire Mossa Palatina disposait de **5 grands électeurs** au sein du collège électoral de Haute-Corse, ventilés en **4 à Bastia et 1 à Biguglia**.

L'instruction sur pièces primaires (délibération du conseil municipal de Bastia du 5 juin 2026 et arrêté préfectoral des candidatures) confirme nominativement et rigoureusement cette répartition :

1. **Nicolas BATTINI** (`index: 60`, Bastia) : Délégué de droit, conseiller municipal d'opposition, tête de liste « Populu di Bastia », candidat aux élections sénatoriales.
2. **Michel BRUSCHINI** (`index: 62`, Bastia) : Délégué de droit, conseiller municipal d'opposition « Populu di Bastia », mandataire de la liste « Unione di i patriotti » au conseil du 5 juin 2026.
3. **Valérie IDDA** (`index: 79`, Bastia) : Délégué de droit, conseillère municipale d'opposition « Populu di Bastia ».
4. **Philippe SERRA** (`index: 123`, Bastia) : Délégué supplémentaire élu au titre de la Liste C (« Unione di i patriotti », 3 voix obtenues au conseil municipal, lui conférant exactement 1 délégué supplémentaire).
5. **Audrey MORI** (`index: 142`, Biguglia) : Déléguée titulaire, conseillère municipale d'opposition à Biguglia, et **suppléante officielle de Nicolas Battini** sur sa déclaration de candidature sénatoriale déposée en préfecture.

**Constat probatoire** : Le « socle institutionnel » formel de Nicolas Battini s'élevait donc rigoureusement à **5 voix documentées**. Avec **88 voix recueillies** au soir du scrutin du 27 septembre 2026, Nicolas Battini a bénéficié d'un apport net de **83 suffrages extérieurs** à son groupe d'origine.

### 3.2. La consigne de vote blanc de Julien Morganti et le groupe d'opposition bastiais
Le 25 septembre 2026, Julien Morganti (tête du groupe d'opposition bastiais « Uniti per dumane ») a publiquement appelé ses soutiens et les grands électeurs à **voter blanc**.

1. **Périmètre exposé au vote blanc à Bastia** :
   - Au conseil municipal du 5 juin 2026, la Liste B (« Uniti per dumane » portée par Julien Morganti) a obtenu **9 voix** de conseillers municipaux (délégués de droit).
   - Cette liste a obtenu **4 délégués supplémentaires** : Ange-Jean LORENZI (`index: 119`), Christelle POGGI (`index: 120`), Nicolas VINCENSINI (`index: 121`), Livia GRAZIANI-SANCIU (`index: 122`).
   - L'ensemble exposé totalise ainsi **13 grands électeurs**.
2. **Événement du 27 septembre 2026 (scission)** :
   - La conseillère municipale Hélène SALGE (`index: 96`) a publiquement annoncé le 27 septembre 2026 qu'elle se désolidarisait de la position de Julien Morganti pour rejoindre le Parti Radical.
   - Par conséquent, son statut de consigne a été basculé en `inconnue`.
   - L'ensemble exposé net au vote blanc s'établit donc à **12 électeurs**.
3. **Rapprochement électoral** :
   - Le scrutin a enregistré **36 bulletins blancs** et **40 bulletins nuls** (total 76 non-exprimés, selon les premiers chiffres).
   - Les 12 électeurs bastiais exposés à la consigne Morganti ne constituent qu'une fraction de ce volume de votes blancs/nuls, confirmant une dispersion plus large à travers les communes rurales.

### 3.3. Le pôle majoritaire autonomiste (Paulu Santu Parigi / Gilles Simeoni)
Le sénateur sortant Paulu Santu Parigi a été réélu avec **442 voix**.
Dans le périmètre prioritaire, son socle de soutien documenté (`consigne_type: parigi`) s'élève à **76 grands électeurs** :
- **2 parlementaires** (Michel Castellani, et Paul-Toussaint Parigi lui-même) ;
- **27 conseillers territoriaux** à l'Assemblée de Corse (24 Fà Populu Inseme / Femu a Corsica + 3 Avanzemu/PNC) ;
- **47 délégués bastiais** (31 conseillers municipaux de la majorité de Pierre Savelli et Gilles Simeoni + 16 délégués supplémentaires élus sur la Liste A de Didier Grassi).

Les 366 voix complémentaires nécessaires pour atteindre les 442 voix proviennent des communes de l'intérieur et du littoral, démontrant la pénétration de la majorité territoriale dans le monde rural.

### 3.4. Le cas spécifique de Corte et de Xavier Poli
L'issue #85 ordonnait d'isoler explicitement le cas du maire de Corte :
> « Le cas Xavier Poli / Corte reste à vérifier séparément : ne pas lui attribuer l'appel au blanc de Morganti sans source directe. »

L'examen attentif des déclarations publiques, de la presse locale et des prises de parole institutionnelles confirme :
- **Aucune consigne publique formelle** n'a été émise par Xavier Poli ou la majorité municipale de Corte pour les sénatoriales 2026 ;
- L'appel au blanc de Julien Morganti est strictement restreint à son propre groupe bastiais et ne saurait être étendu à la municipalité de Corte ;
- En application de la méthodologie, les 15 délégués de Corte sont rigoureusement enregistrés avec `consigne_type: inconnue` et `niveau_preuve: inconnu`.

### 3.5. Borgo, Lucciana, Ghisonaccia, Calvi et la question des « 88 voix »
Dans ses déclarations post-scrutin rapportées par France 3 Corse ViaStella, Nicolas Battini a affirmé avoir recueilli les voix de :
1. « la droite républicaine privée de candidat » (suite à l'absence de candidature officielle investie par LR / Droite Républicaine en Haute-Corse) ;
2. « quelques maires de l'ancienne gauche rurale ».

**Constat d'intégrité probatoire** :
- Ni Jean Dominici à Borgo (33 délégués), ni Ange Santini à Calvi (15 délégués), ni Joseph Galletti à Lucciana (15 délégués), ni Francis Giudici à Ghisonaccia (15 délégués) n'ont publié de consigne de vote en faveur de Nicolas Battini.
- De même, aucun maire rural issu de l'ancienne gauche départementale n'a revendiqué publiquement avoir voté pour le candidat soutenu par Mossa Palatina et le Rassemblement National.
- **Règle absolue** : Conformément aux consignes de recherche de l'Institut Mariani, **ces déclarations politiques globales de Nicolas Battini ne sont pas transformées en faits nominatifs**. Aucun électeur individuel n'est étiqueté « Battini » par présomption.
- Tous ces délégués restent classés `inconnue`, préservant la stricte frontière entre l'analyse politique d'ensemble et le respect de la liberté et du secret de vote de chaque grand électeur.

---

## 4. Données et artefacts livrés

1. **`research/senatoriales-2026/data/annuaire_electeurs_senatoriaux_2B_2026.csv`** :
   Annuaire tabulaire complet des 616 grands électeurs, enrichi sur 25 colonnes combinant le profil républicain d'origine, les listes municipales, les courants politiques, les consignes et niveaux de preuve, et les coordonnées institutionnelles publiques.
2. **`research/senatoriales-2026/data/annuaire_electeurs_senatoriaux_2B_2026.json`** :
   Format JSON structuré intégrant l'intégralité des attributs pour requêtage machine, intégration au Corpus Cogentia et traçabilité des sources.
3. **`research/senatoriales-2026/data/resultats_officiels_scrutin_2026-09-27.md` & `.json`** :
   Synthèse des résultats officiels proclamés (participation 98,38 %, Parigi 442 voix, Battini 88 voix, 76 blancs et nuls) et confrontation statistique avec le modèle d'exposition.

---

## 4.bis. Confrontation post-scrutin du 27 septembre 2026 : Réseau d'exposition vs Résultats proclamés

Le dépouillement du scrutin sénatorial du 27 septembre 2026 confirme et éclaire la grille d'exposition :
* **Sur-pénétration de Nicolas Battini (17,6x)** : Partant de 5 grands électeurs militants documentés (4 à Bastia, 1 à Biguglia), Battini recueille **88 voix**, démontrant une captation de 83 voix additionnelles parmi les maires et délégués ruraux de droite départementale ou sans étiquette.
* **Volume massif des votes blancs et nuls (76 voix — 12,54 %)** : Avec 36 blancs et 40 nuls, la contestation passive surpasse le groupe bastiais documenté (12 blancs) et traduit un refus marqué de choisir entre Parigi et Battini.
* **Conséquence pour le contentieux électoral** : La perte de chance causée par l'exclusion de la candidature indépendante Robert / Vernerey s'apprécie au regard de ce réservoir de 76 voix non-exprimées et de la marge de mise en ballottage pour un second tour.

---

## 5. Prochaines étapes recommandées pour l'Issue #85

1. **Clôture opérationnelle du jalon prioritaire** : Le collège des 616 électeurs est entièrement cartographié, enrichi et confronté aux résultats réels.
2. **Consultation du procès-verbal (RP-SEN-08)** : Solliciter l'accès aux 40 bulletins nuls auprès de la préfecture pour vérifier l'existence de bulletins au nom de Robert / Baron Mariani.
3. **Exploitation dans le mémoire contentieux** : Verser le jeu de données `resultats_scrutin_2B_2026.json` comme pièce justificative (P-25) devant le Conseil constitutionnel.

