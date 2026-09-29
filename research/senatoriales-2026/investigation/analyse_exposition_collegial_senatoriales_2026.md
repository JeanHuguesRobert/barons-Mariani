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
| **BASTIA** | 43 droit + 21 suppl. | 64 | 47 | 4 | 13 | 0 |
| **BIGUGLIA** | Délégués titulaires | 15 | 0 | 1 | 0 | 14 |
| **BORGO** | Délégués de droit | 33 | 0 | 0 | 0 | 33 |
| **CALVI** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **CORTE** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **GHISONACCIA** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **LUCCIANA** | Délégués titulaires | 15 | 0 | 0 | 0 | 15 |
| **TOTAL PÉRIMÈTRE PRIORITAIRE** | — | **209** | **76** | **5** | **13** | **115** |
| *Reste du collège (communes rurales)* | Délégués titulaires | 407 | 0 | 0 | 0 | 407 |
| **TOTAL GÉNÉRAL HAUTE-CORSE** | — | **616** | **76** | **5** | **13** | **522** |

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

**Constat probatoire** : le modèle identifie **5 grands électeurs institutionnellement rattachés** à la candidature Battini. Le score de **88 voix** crée donc un **écart arithmétique de 83** entre ce socle institutionnel identifiable et le résultat obtenu. Cet écart établit que le vote Battini a dépassé de très loin son seul noyau institutionnel documenté ; il ne permet pas d'affirmer que ces 5 électeurs ont tous voté Battini, ni d'identifier individuellement ou territorialement l'origine des 83 voix d'écart.

### 3.2. La consigne de vote blanc de Julien Morganti et le groupe d'opposition bastiais
Le 25 septembre 2026, Julien Morganti (tête du groupe d'opposition bastiais « Uniti per dumane ») a publiquement appelé ses soutiens et les grands électeurs à **voter blanc**.

1. **Périmètre exposé au vote blanc à Bastia** :
   - Au conseil municipal du 5 juin 2026, la Liste B (« Uniti per dumane » portée par Julien Morganti) a obtenu **9 voix** de conseillers municipaux (délégués de droit).
   - Cette liste a obtenu **4 délégués supplémentaires** : Ange-Jean LORENZI (`index: 119`), Christelle POGGI (`index: 120`), Nicolas VINCENSINI (`index: 121`), Livia GRAZIANI-SANCIU (`index: 122`).
   - L'ensemble exposé totalise ainsi **13 grands électeurs**.
2. **Événement du 27 septembre 2026 (scission)** :
   - Hélène SALGE (`index: 96`) a ensuite annoncé sa rupture avec le groupe Uniti per dumane pour siéger comme élue du Parti radical.
   - La source consultée établit ce départ et un désaccord avec une prise de position du groupe, **sans préciser que ce désaccord portait sur la consigne sénatoriale de vote blanc**.
   - Il n'est donc pas méthodologiquement justifié de la retrancher du périmètre **exposé** à la consigne au seul motif de cette rupture ultérieure. Le périmètre d'exposition demeure **13 grands électeurs**, sans aucune inférence sur leur vote individuel.
3. **Rapprochement électoral** :
   - Le scrutin a enregistré **36 bulletins blancs** et **40 bulletins nuls** (total 76 non-exprimés, selon les premiers chiffres).
   - Les **13 électeurs bastiais exposés** à la consigne Morganti ne peuvent être assimilés aux bulletins blancs effectivement déposés. Le total de 36 blancs montre seulement que le vote blanc dépasse ce seul périmètre d'exposition documenté ; l'origine des autres bulletins demeure inconnue.

### 3.3. Le pôle majoritaire autonomiste (Paulu Santu Parigi / Gilles Simeoni)
Le sénateur sortant Paulu Santu Parigi a été réélu avec **442 voix**.
Dans le périmètre prioritaire, son socle de soutien documenté (`consigne_type: parigi`) s'élève à **76 grands électeurs** :
- **2 parlementaires** (Michel Castellani, et Paul-Toussaint Parigi lui-même) ;
- **27 conseillers territoriaux** à l'Assemblée de Corse (24 Fà Populu Inseme / Femu a Corsica + 3 Avanzemu/PNC) ;
- **47 délégués bastiais** (31 conseillers municipaux de la majorité de Pierre Savelli et Gilles Simeoni + 16 délégués supplémentaires élus sur la Liste A de Didier Grassi).

L'écart entre les **76 grands électeurs exposés à un soutien Parigi documenté** dans ce périmètre et les **442 voix** finalement obtenues est de 366. Cet écart montre que le score dépasse très largement le noyau d'exposition documenté, mais le secret du vote interdit d'en déduire que ces 366 voix proviennent toutes des communes de l'intérieur ou d'une catégorie politique déterminée.

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
* **Écart score / socle institutionnel de Nicolas Battini** : 5 grands électeurs sont institutionnellement rattachés à son offre, contre **88 voix** obtenues. Le ratio descriptif est de 17,6, mais il ne faut pas le convertir en attribution : l'écart de 83 voix n'identifie ni les électeurs concernés ni leur origine politique ou territoriale.
* **Volume élevé des bulletins blancs et nuls (76 — 12,54 % des votants)** : 36 blancs et 40 nuls n'ont produit aucun suffrage exprimé. Ils ne constituent pas un bloc politiquement homogène et ne peuvent être qualifiés globalement de « contestation » sans autre preuve. Ils montrent seulement qu'une fraction non négligeable des votants n'a produit de suffrage valable pour aucun des deux candidats admis.
* **Conséquence pour le contentieux électoral** : les 76 bulletins non exprimés sont un élément descriptif, mais ne suffisent pas à eux seuls à rendre possible un second tour. Une analyse contrefactuelle utile doit calculer explicitement la diminution minimale du score Parigi nécessaire à la perte de sa majorité absolue, selon plusieurs hypothèses de conversion des blancs, nuls et abstentions.

---

### 4.ter. Capacité arithmétique d'une troisième candidature à provoquer un second tour

Cette section ne cherche pas à prédire le score de la candidature Robert / Vernerey. Elle borne seulement le **niveau de redistribution nécessaire** pour modifier le fait juridiquement décisif du premier tour : l'obtention ou non par M. Parigi de la majorité absolue des suffrages exprimés prévue par l'article L.294 du code électoral.

Notons :

- \(x\) = nombre de voix effectivement obtenues par M. Parigi dans le scrutin observé qui, dans un scrutin à trois candidatures, ne se seraient plus portées sur lui ;
- \(z\) = nombre de bulletins parmi les 36 blancs, 40 nuls et, selon le scénario, 10 abstentions qui seraient devenus des suffrages exprimés valables.

En conservant toutes les autres données inchangées, le nombre de suffrages exprimés devient \(530 + z\), et le score de M. Parigi devient \(442 - x\). Pour qu'il **ne dispose plus de la majorité absolue au premier tour**, il faut :

\[
442 - x \leq \left\lfloor\frac{530+z}{2}\right\rfloor.
\]

D'où les bornes suivantes :

| Scénario purement arithmétique | Nouveaux exprimés \(z\) | Exprimés totaux | Diminution minimale du score Parigi \(x\) pour empêcher l'élection au 1er tour |
|---|---:|---:|---:|
| Aucun blanc/nul converti | 0 | 530 | **177** |
| Tous les 36 blancs convertis | 36 | 566 | **159** |
| Tous les 40 nuls convertis | 40 | 570 | **157** |
| Tous les blancs + nuls convertis | 76 | 606 | **139** |
| Blancs + nuls + 10 abstentions convertis | 86 | 616 | **134** |

Deux conséquences méthodologiques suivent :

1. **Les 76 blancs et nuls ne suffisent pas, à eux seuls, à provoquer un second tour.** Même si chacun devenait un vote valable pour une troisième candidature, M. Parigi conserverait 442 voix sur 606 exprimées et resterait au-dessus de la majorité absolue.
2. L'hypothèse d'un second tour suppose donc une **redistribution substantielle de voix initialement portées sur M. Parigi**, au minimum comprise entre 134 et 177 voix selon le nombre de non-exprimés qui deviendraient exprimés. Cela représente environ **30,3 % à 40,0 %** de son score observé de 442 voix.

Cette borne ne dit pas qu'une telle redistribution aurait eu lieu. Elle dit exactement ce qu'il faudrait établir ou rendre suffisamment plausible par des éléments supplémentaires pour soutenir l'hypothèse d'un second tour sans transformer les blancs, nuls ou appartenances politiques en votes fictifs.

Inversement, l'analyse ne doit pas être limitée au seul score direct qu'aurait obtenu la troisième candidature. Une offre supplémentaire peut aussi modifier les choix stratégiques, les consignes, la campagne et la répartition entre les autres candidats. Ces effets systémiques sont possibles mais, faute d'observation, ne sont pas quantifiables avec précision.

---

## 5. Prochaines étapes recommandées pour l'Issue #85

1. **Clôture opérationnelle du jalon prioritaire** : Le collège des 616 électeurs est entièrement cartographié, enrichi et confronté aux résultats réels.
2. **Consultation du procès-verbal (RP-SEN-08)** : Solliciter l'accès aux 40 bulletins nuls auprès de la préfecture pour vérifier l'existence de bulletins au nom de Robert / Baron Mariani.
3. **Exploitation dans le mémoire contentieux** : Verser le jeu de données `resultats_scrutin_2B_2026.json` comme pièce justificative (P-25) devant le Conseil constitutionnel.

