---
title: "Note de Campagne numéro 3 : le cas EDF expliqué"
subtitle: "Dossier technique — Calacuccia, Ricanto, stockage, préjudice continu et Autonomie de Capacité"
status: "draft_for_review"
version: "v0.4"
date: "2026-06-18"
target_repository: "JeanHuguesRobert/barons-Mariani"
suggested_path: "cas_edf.md"
human_validation_required: true
review_status: "Grok/Claude EDF review integrated — 2026-06-18"
---

# Note de Campagne numéro 3 : le cas EDF expliqué

## Dossier technique — Calacuccia, Ricanto, stockage, préjudice continu et Autonomie de Capacité

### Statut

Ce document est un **dossier de travail technique et politique**.

Il vise à préparer :

1. une publication publique ;
2. une note de campagne ;
3. une demande de transparence ;
4. une éventuelle saisine de la CRE, de l’Autorité de la concurrence, de la Commission européenne ou de la CADA ;
5. une proposition industrielle FractaVolta.

Il ne prétend pas encore établir judiciairement une faute d’EDF. Il établit un faisceau d’indices quantitatifs et institutionnels permettant de soutenir qu’il existe un **préjudice public continu** : solaire limité, barrages sous-mobilisés comme stockage, recours thermique coûteux, charges publiques élevées, absence de comparaison contradictoire, verrouillage potentiel des ressources physiques.

---

### Note sur les revues critiques externes

La revue adverse constructive Grok / Claude du 18 juin 2026 porte bien sur les deux documents `cas_edf.md` et `cas_edf_blogpost.md`. Elle classe plusieurs points comme bloquants pour la version grand public : projections par famille, exposition trop forte de FractaVolta, section FUD, langage d’intention, extrapolation trop spectaculaire au parc hydraulique complet.

Arbitrage retenu :

- conserver la puissance politique de la note ;
- supprimer du blogpost les projections par famille ;
- passer les montants Calacuccia en fourchette ;
- retirer le terme FUD du blogpost ;
- remplacer “confisquée” par “gâchée” dans la version grand public ;
- conserver FractaVolta dans la version technique, où la déclaration d’intérêts et la gouvernance anti-capture sont nécessaires ;
- réduire fortement la présence nominative de FractaVolta dans le blogpost, en la cantonnant à une déclaration d’intérêts en fin de texte.

La version technique assume donc la précision institutionnelle. La version grand public assume l’impact politique, mais sans prêter inutilement le flanc à l’accusation d’opportunisme ou de confusion comptable.

## 0. Thèse centrale

La Corse dispose de trois ressources physiques majeures :

- le soleil ;
- l’eau ;
- le relief.

Ces ressources pourraient être combinées en une architecture :

> **solaire + stockage hydraulique + batteries + pilotage logiciel + seconde vie photovoltaïque + autoconsommation collective.**

Or l’architecture actuelle traite une partie du solaire comme une énergie « fatale », maintient un recours coûteux au thermique / bioliquide, et laisse les grands ouvrages hydrauliques sous contrôle EDF sans comparaison publique suffisante avec une solution alternative.

La thèse n’est pas d’abord morale. Elle est architecturale :

> **Le problème n’est pas le soleil. Le problème est l’architecture qui ne transforme pas l’abondance solaire en capacité pilotable.**

Dans la dialectique révélateur / stabilisateur :

- **EDF révèle** le défaut d’architecture : énergie solaire limitée, barrages verrouillés, thermique compensé.
- **FractaVolta stabilise** : elle propose gratuitement à la Corse une architecture pilote, destinée ensuite à être exportée.

---

## 1. Niveaux de preuve

| Niveau | Signification | Usage dans cette note |
|---|---|---|
| Fait documenté | Source publique officielle ou institutionnelle | Ricanto, CRE, EDF, Collectivité de Corse, INSEE |
| Calcul direct | Opération arithmétique à partir d’un fait documenté | €/habitant, €/MWh, GWh/jour |
| Hypothèse pédagogique | Scénario simplifié destiné à faire voir l’ordre de grandeur | STEP Calacuccia 1 GWh cyclée chaque jour |
| Extrapolation | Extension d’un cas à un ensemble plus large | Calacuccia → parc hydraulique EDF corse |
| Allégation à expertiser | Hypothèse politiquement forte mais juridiquement non prouvée | préjudice indemnisable, abus de position dominante |
| Revendication | Demande politique ou contentieuse | audit, cessation, réparation, mise en concurrence |

Cette distinction est essentielle. Le dossier doit être offensif, mais non vulnérable par confusion entre calcul pédagogique et preuve juridiquement liquidée.

---

## 2. Faits documentés

### 2.1. Population de référence

L’INSEE indique qu’au 1er janvier 2026, la Corse compte environ **365 600 habitants**.

Cette population sert à ramener les chiffres globaux à une échelle individuelle.

Source : INSEE, *Une fécondité historiquement basse mais une population toujours en hausse*, avril 2026.  
https://www.insee.fr/fr/statistiques/8973577

### 2.2. Ricanto : centrale EDF / EDF PEI, 133,7 MW, bioliquide, 25 ans

La CRE décrit le projet Ricanto comme un contrat entre EDF Corse / EDF SEI et EDF PEI, filiale à 100 % d’EDF, pour une centrale de **133,7 MW** fonctionnant au bioliquide, située à Ajaccio.

La CRE indique :

- puissance : **133,7 MW** ;
- durée du contrat : **25 ans** ;
- hypothèse initiale : **5 000 heures équivalent pleine puissance** ;
- prix du bioliquide : **1 200 €/t** ;
- taux de rémunération du capital immobilisé : **9,55 % nominal avant impôt** ;
- surcoût d’achat imputable aux charges de service public : environ **6,3 Md€ courants sur 25 ans**.

Source : CRE, délibération n°2024-138 du 10 juillet 2024.  
https://www.cre.fr/fileadmin/Documents/Deliberations/2024/240710_2024-138_CNC_Ricanto.pdf

### 2.3. Stockage en Corse : la CRE reconnaît des économies massives

En 2026, la CRE valide en Corse cinq projets de stockage :

- deux STEP ;
- trois batteries électrochimiques.

La CRE indique :

- charges SPE : **181,6 M€** ;
- surcoûts de production évités : **535,3 M€** ;
- économie nette de charges SPE : **353,7 M€ sur 30 ans**.

Le stockage n’est donc pas une idée marginale : il est reconnu par le régulateur comme économiquement utile en Corse.

Source : CRE, délibération n°2026-111 du 26 mai 2026.  
https://www.cre.fr/fileadmin/Documents/Deliberations/2026/260526_2026-111_Guichet_Corse.pdf

### 2.4. Parc EDF Corse : 199 MW hydrauliques pilotables

Le bilan prévisionnel EDF Corse 2024 indique :

- **233 MW photovoltaïques** installés fin 2023 ;
- **282 GWh** de production photovoltaïque en 2023 ;
- **199 MW** d’installations hydrauliques pilotables EDF, réparties sur quatre vallées et huit aménagements ;
- production hydraulique EDF 2023 : **497 GWh** ;
- moyenne décennale hydraulique : **469 GWh**.

Source : EDF Corse, *Bilan prévisionnel 2024*.  
https://corse.edf.fr/sites/sei_corse/files/2024-12/edf-sei-bilan-previsionnel-2024-corse.pdf

### 2.5. Limitation des ENR intermittentes

EDF Open Data Corse indique que la part maximale d’énergies renouvelables intermittentes — éolien et photovoltaïque sans stockage — pouvant être injectée à un instant donné sur les réseaux insulaires est limitée à **35 %**. Au-delà, des déconnexions ou limitations sont possibles.

Source : EDF Open Data Corse, *Limitations de production au titre de la sûreté système*.  
https://opendata-corse.edf.fr/datasets/deconnexions-des-installations-photovoltaiques-corse

### 2.6. Calacuccia : un projet plus ambitieux dépendait d’un accord EDF

Un rapport de la Collectivité de Corse relatif au développement du lac de Calacuccia indique qu’un projet initial d’aménagement hydraulique global en turbinage-pompage depuis le barrage de Calacuccia dépendait d’un accord avec EDF. Une solution moins ambitieuse et moins dépendante d’EDF a été retenue.

Ce point est crucial : il montre que le verrou EDF n’est pas théorique. Il réduit concrètement l’ambition d’un projet territorial.

Source : Collectivité de Corse, rapport 2024E1134.  
https://www.isula.corsica/assemblea/docs/rapports/2024E1134-.pdf

### 2.7. Maîtrise corse des ouvrages hydroélectriques : sujet déjà posé politiquement

Dans les débats de l’Assemblée de Corse, la question de savoir si la Collectivité de Corse doit devenir **autorité concédante** pour les ouvrages hydroélectriques est explicitement posée. L’Exécutif indique que cette possibilité est étudiée dans le cadre de la PPE, de l’autonomie énergétique et du processus autonomie.

Source : Assemblée de Corse, compte rendu cité.  
https://www.isula.corsica/file/241510/

---

## 3. Calculs de base

### 3.1. Ricanto ramené à chaque habitant

Données :

- compensation Ricanto : **6,3 Md€ sur 25 ans** ;
- population corse : **365 600 habitants**.

Calculs :

```text
6,3 Md€ / 25 ans = 252 M€/an
252 M€/an / 365 600 hab. = 689 €/habitant/an
6,3 Md€ / 365 600 hab. = 17 232 €/habitant sur 25 ans
```

Ordre de grandeur :

> **Ricanto représente environ 690 €/habitant/an de charges compensées mises à l’échelle de la population corse.**

Ce n’est pas une facture EDF individuelle. C’est une mise à l’échelle pédagogique d’une charge publique.

### 3.2. Coût reconstitué par MWh Ricanto

Données :

- puissance : **133,7 MW** ;
- fonctionnement initial : **5 000 h/an** ;
- compensation annuelle moyenne : **252 M€/an**.

Calcul :

```text
133,7 MW × 5 000 h = 668 500 MWh/an
252 M€/an / 668 500 MWh/an = 377 €/MWh
```

Ordre de grandeur :

> **1 GWh thermique Ricanto évité représente environ 377 000 € de charges compensées évitées.**

En formulation publique simplifiée :

> **environ 400 000 € par GWh.**

### 3.3. Hypothèse Calacuccia 1 GWh

Hypothèse pédagogique :

> Une STEP Calacuccia de **1 GWh**, cyclée une fois par jour, évite 1 GWh thermique par jour.

Si cette batterie hydraulique permet d’éviter 1 GWh thermique Ricanto par jour dans le scénario haut :

> **Scénario haut : 1 GWh/jour substitué à du thermique Ricanto.**

Pour tenir compte des incertitudes — hydrologie, rendement, saisonnalité, disponibilité de pompage, contraintes réseau — il faut aussi afficher une fourchette prudente :

> **Scénario prudent : 0,5 GWh/jour substitué.**  
> **Scénario haut : 1 GWh/jour substitué.**

Dans le scénario haut :

Calcul :

```text
1 GWh = 1 000 MWh
1 000 MWh × 377 €/MWh = 377 000 €
1 000 MWh × 400 €/MWh = 400 000 €
365 GWh/an × 377 €/MWh = 137,6 M€/an
365 GWh/an × 400 €/MWh = 146 M€/an
```

Par habitant :

```text
137,6 M€/an / 365 600 hab. = 376 €/habitant/an
146 M€/an / 365 600 hab. = 399 €/habitant/an
```

Ordres de grandeur :

| Scénario | Énergie substituée | Valeur annuelle à 377 €/MWh | Valeur annuelle à 400 €/MWh |
|---|---:|---:|---:|
| Prudent | 0,5 GWh/jour | ≈ 68,8 M€/an | ≈ 73 M€/an |
| Haut | 1 GWh/jour | ≈ 137,6 M€/an | ≈ 146 M€/an |

> **Une STEP Calacuccia 1 GWh doit donc être présentée comme un gisement de l’ordre de 70 à 146 M€/an de coût thermique compensé évitable, selon les hypothèses de cyclage et de substitution.**

### 3.3 bis. Vérification volumétrique de la STEP 1 GWh

Une STEP de 1 GWh n’implique pas un second lac équivalent à Calacuccia.

Formule simplifiée :

```text
E = ρ × g × H × V × η
```

Avec :

- ρ ≈ 1 000 kg/m³ ;
- g ≈ 9,81 m/s² ;
- H ≈ 400 à 450 m selon l’implantation du bassin bas ;
- η ≈ 0,75 à 0,85 selon rendement aller-retour ou rendement de pompage/turbinage retenu.

Ordre de grandeur :

- à 400-450 m de chute utile, **1 GWh stocké** correspond à un volume actif de l’ordre de **0,9 à 1,2 million de m³** selon rendement retenu ;
- cela reste très inférieur au volume de la retenue de Calacuccia, mais impose un bassin bas sérieux, des études foncières, géologiques, environnementales et hydrauliques.

Cette vérification ne prouve pas la faisabilité du site. Elle montre seulement que l’ordre de grandeur n’est pas absurde.

### 3.3 ter. Prudence sur MW pilotable et MW de pompage

La puissance hydraulique pilotable existante ne doit pas être confondue avec la puissance de pompage d’une future STEP.

- **MW pilotables** : puissance restituable par les turbines existantes ou adaptées.
- **MW de pompage** : puissance électrique absorbable pour remonter l’eau.
- **MWh stockés** : quantité d’énergie disponible dans le volume d’eau remonté.

Un projet réel devra dimensionner séparément :

1. la puissance de pompage ;
2. la puissance de turbinage ;
3. le volume utile du bassin bas ;
4. la durée de décharge ;
5. les contraintes de débit réservé et d’usage de l’eau.

### 3.4. Extrapolation à tout le parc hydraulique EDF corse

Données :

- parc hydraulique EDF Corse : **199 MW** ;
- référence Calacuccia/Golo utilisée : **56,8 MW** ;
- facteur d’extrapolation : **199 / 56,8 = 3,5**.

Extrapolation indicative :

```text
1 GWh/jour × 3,5 = 3,5 GWh/jour
3,5 GWh/jour × 400 000 €/GWh = 1,4 M€/jour
1,4 M€/jour × 365 = 511 M€/an
511 M€/an / 365 600 hab. = 1 398 €/habitant/an
```

Ordre de grandeur :

> **À l’échelle du parc hydraulique EDF corse, l’enjeu théorique pourrait dépasser 500 M€/an de coût thermique évitable, soit environ 1 400 €/habitant/an.**

Prudence : ce n’est pas une étude de faisabilité ouvrage par ouvrage. C’est une extrapolation destinée à montrer l’ordre de grandeur.

---

## 4. Qualification du préjudice

### 4.1. Préjudice passé

Depuis environ vingt ans, le photovoltaïque corse s’est développé dans une architecture où l’énergie solaire reste partiellement contrainte, limitée ou sous-valorisée, faute de stockage suffisant et de pilotage territorial.

Les premiers contrats d’obligation d’achat photovoltaïque arrivent à échéance. La CRE rappelle que la loi du 10 février 2000 a instauré des contrats d’achat renouvelables sur 20 ans et que les tarifs photovoltaïques incitatifs datent notamment de 2006.

Source : CRE, renégociation des contrats photovoltaïques.  
https://www.cre.fr/actualites/toute-lactualite/renegociation-des-contrats-pv.html

### 4.2. Préjudice actuel

Le préjudice actuel est quotidien :

- solaire limité ;
- barrages non pleinement mobilisés comme batteries territoriales ;
- recours au thermique / bioliquide ;
- charges publiques compensées ;
- absence de comparaison contradictoire ;
- impossibilité pratique pour un acteur alternatif d’accéder à certains verrous physiques.

### 4.3. Préjudice futur

Ricanto engage une trajectoire contractuelle de 25 ans. La réforme hydroélectrique nationale risque de renforcer la sécurité juridique des exploitants actuels des barrages.

Le préjudice n’est donc pas seulement passé. Il est programmé.

---

## 5. Objections fortes et traitement

### Objection 1 — La STEP Calacuccia 1 GWh n’est pas encore étudiée techniquement

Réponse : exact. C’est pourquoi il faut demander une étude contradictoire. Le chiffre 1 GWh sert d’hypothèse pédagogique et de révélateur d’ordre de grandeur, non de devis d’exécution.

Action : étude hydrologique, topographique, environnementale, énergétique et financière.

### Objection 2 — Un GWh/jour ne se substitue pas toujours à du Ricanto

Réponse : exact. La substitution dépend du profil de demande, du niveau de stockage, de la disponibilité hydraulique, du solaire, du réseau et des contraintes environnementales.

Action : simulation horaire sur une année représentative, puis années sèches / humides.

### Objection 3 — Le coût de 400 €/MWh peut varier

Réponse : exact. Le calcul strict issu de la CRE donne plutôt 377 €/MWh à partir des hypothèses initiales. 400 €/MWh est un arrondi public, cohérent avec l’ordre de grandeur.

Action : conserver deux colonnes dans les tableaux : 377 €/MWh et 400 €/MWh.

### Objection 4 — L’extrapolation à tout le parc hydraulique EDF corse est grossière

Réponse : exact. Elle ne doit pas être présentée comme une étude d’ingénierie. Elle montre seulement que le sujet dépasse largement Calacuccia.

Action : demander un audit ouvrage par ouvrage.

### Objection 5 — L’abus de position dominante n’est pas prouvé

Réponse : exact. C’est une qualification à instruire, non à affirmer comme acquise.

Action : formuler ainsi : “la question d’un abus de position dominante ou d’un verrouillage anticoncurrentiel doit être examinée”.

---

## 6. Demandes institutionnelles

### 6.1. Demande de transparence

Publier ou obtenir :

- production annuelle de chaque barrage EDF corse ;
- revenus associés ;
- coûts d’exploitation ;
- redevances ;
- contraintes hydrologiques ;
- volumes d’eau ;
- données de déconnexion / limitation solaire ;
- coûts évités par stockage ;
- études STEP existantes ;
- scénarios alternatifs non retenus ;
- justification du recours Ricanto comparé au stockage.

### 6.2. Demande de cessation

Demander que cesse le préjudice continu :

- pas de verrouillage long des droits EDF sans comparaison contradictoire ;
- pas de limitation durable du solaire sans plan de stockage public ;
- pas de centrale thermique compensée sans évaluation d’alternative STEP / stockage ;
- pas d’opacité sur les barrages publics.

### 6.3. Demande de réparation

La réparation financière directe est peu probable à court terme, mais il faut la demander pour fixer le cadre.

Forme réaliste :

> création d’un fonds de réparation capacitaire destiné à financer STEP, batteries, seconde vie photovoltaïque, autoconsommation collective, effacement, pilotage logiciel et projets d’eau territoriale.

Réparer, ce n’est pas seulement indemniser le passé. C’est empêcher que le préjudice se perpétue.

---

## 7. Axes contentieux possibles

### 7.1. CRE

Demander une évaluation contradictoire :

- Ricanto ;
- Calacuccia STEP 1 GWh ;
- parc hydraulique EDF ;
- stockage distribué ;
- seconde vie photovoltaïque ;
- coût évité SPE.

### 7.2. Autorité de la concurrence

Question à poser :

> EDF, par sa maîtrise cumulée du réseau insulaire, des barrages, des moyens thermiques compensés et des conditions d’intégration du solaire, limite-t-elle l’émergence d’alternatives techniquement disponibles et économiquement moins coûteuses ?

### 7.3. Commission européenne

Question à poser :

> La réforme hydroélectrique française traite-t-elle correctement le cas corse, zone non interconnectée, où une ouverture virtuelle continentale ne résout pas le verrou physique local des barrages ?

### 7.4. CADA / accès aux documents

Demander communication des documents administratifs relatifs :

- aux concessions ;
- conventions EDF / collectivités ;
- données hydrauliques ;
- données économiques ;
- études d’impact ;
- études de scénarios alternatifs.

---

## 8. FractaVolta : nature, gouvernance et positionnement

FractaVolta ne doit pas apparaître comme un acteur cherchant à remplacer une rente EDF par une rente privée.

Position correcte :

> **FractaVolta est une startup à impact, conçue comme outil industriel au service prioritaire des habitants de la Corse, avec activités d’intérêt général local et gouvernance anti-capture.**

Elle n’a pas vocation à capter localement une rente. Elle doit fonctionner comme une architecture d’intérêt général local, avec une gouvernance anti-capture.

### 8.1. Mission prioritaire locale

En Corse, FractaVolta propose gratuitement ses services pour servir de territoire pilote.

Objectifs locaux :

- réduire la facture énergétique supportée par les usagers ;
- organiser la seconde vie photovoltaïque ;
- valoriser l’autoconsommation individuelle et collective ;
- installer ou coordonner batteries, STEP, pilotage logiciel et effacement ;
- aider les communes et communautés à devenir capables ;
- fournir une architecture ouverte, contrôlable et reproductible ;
- préserver la valeur créée au bénéfice des habitants permanents.

La Corse n’est donc pas un marché captif. Elle est le territoire fondateur.

### 8.2. Gouvernance envisagée

La structure capitalistique devra empêcher la capture privée.

Orientation à formaliser :

- participation envisagée du fonds de dotation **Barons Mariani**, sous réserve de faisabilité juridique et statutaire ;
- participation éventuelle du public ou de véhicules collectifs adaptés ;
- participation de structures communales, intercommunales, SCIC ou équivalents ;
- ouverture à des acteurs locaux de l’énergie, de l’agriculture, de l’eau et de la rénovation ;
- droits de contrôle, traçabilité et clauses anti-capture ;
- priorité statutaire aux usages corses à l’année.

Le point important n’est pas seulement qui possède les parts. Le point important est que les droits économiques et les droits de décision soient alignés avec l’intérêt territorial.

### 8.3. Revenus commerciaux : à l’export, pas sur la rente corse

La valeur commerciale de FractaVolta doit venir principalement de l’exportation de la solution mise au point en Corse :

- autres îles ;
- zones non interconnectées ;
- territoires isolés ;
- vallées de montagne ;
- pays méditerranéens ;
- collectivités cherchant une autonomie énergétique de capacité.

Les revenus commerciaux issus de l’export devront bénéficier aux structures corses impliquées, donc indirectement ou directement aux habitants de la Corse selon les modalités de gouvernance retenues.

Formule :

> **Les revenus commerciaux sont à l’export ; la capacité locale est pour les Corses.**

### 8.4. Position personnelle du fondateur

Le fondateur ne doit pas être présenté comme un rentier énergétique potentiel.

Position à expliciter :

> **Je travaille pour la gloire : pour démontrer en Corse une architecture d’autonomie exportable, pas pour extraire une rente personnelle.**

Cela ne signifie pas absence de structure économique. Cela signifie que l’enrichissement personnel du fondateur n’est pas l’objectif du projet. L’objectif est de créer une capacité territoriale, puis une solution exportable dont les bénéfices reviennent prioritairement aux Corses et aux structures d’intérêt général impliquées.

### 8.5. Briques proposées

FractaVolta articule :

- seconde vie photovoltaïque ;
- batteries stationnaires ;
- batteries mobiles ;
- STEP territoriales ;
- pilotage logiciel ;
- autoconsommation collective ;
- effacement / déplacement des usages ;
- paquets d’énergie ;
- gouvernance ouverte ;
- traçabilité ;
- modèle non captif.

Formule :

> **EDF fait payer la rareté. FractaVolta propose gratuitement à la Corse l’architecture de l’abondance.**

### 8.6. Objection à anticiper : conflit d’intérêts

Objection prévisible :

> Si FractaVolta critique EDF, n’est-ce pas pour prendre sa place ?

Réponse :

> Non. FractaVolta ne demande pas une rente locale. FractaVolta propose gratuitement à la Corse une architecture pilote, ouverte, contrôlable et gouvernée par des structures d’intérêt général local. La valeur commerciale éventuelle viendra de l’exportation de cette solution, et non de la captation des ressources corses.

Cette réponse doit être intégrée dès le départ pour neutraliser l’accusation d’opportunisme.

---

## 9. Formules stabilisées

### Formule technique

> Le solaire corse n’est pas fatal par nature. Il est rendu fatal par une architecture qui ne le stocke pas suffisamment.

### Formule politique

> Pas d’autonomie énergétique sans maîtrise des barrages, du stockage et de l’eau.

### Formule contentieuse

> EDF doit démontrer que son architecture est la meilleure pour la Corse. À défaut, l’absence de transparence, de comparaison et d’accès aux actifs stratégiques devient contestable.

### Formule FractaVolta

> FractaVolta ne vient pas vendre une rente à la Corse ; FractaVolta propose de construire en Corse une solution exportable.

### Formule révélateur / stabilisateur

> EDF révèle le problème. FractaVolta apporte le stabilisateur.

---

## 10. Conclusion

Le cas EDF-Calacuccia est plus qu’un dossier énergétique.

C’est un cas d’école de l’Autonomie de Capacité.

La question n’est pas seulement : qui produit l’électricité ?

La vraie question est :

> Qui contrôle les capacités physiques qui transforment les ressources naturelles corses en pouvoir d’achat, sécurité, résilience et souveraineté ?

Tant que le soleil, l’eau et le relief corses ne sont pas organisés en capacité locale, l’autonomie reste incomplète.

Le dossier EDF révèle cette contradiction.

FractaVolta propose une architecture pour la stabiliser, sans demander de rente locale : une startup à impact au service prioritaire des habitants de la Corse, construite localement puis exportable.
