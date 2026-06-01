# PLU de Corte

## Enquête OSINT ouverte — Riacquistu Data-Driven, nouveau PLU, logement étudiant et bâti ancien

**Statut :** note d’enquête OSINT exploratoire, non stabilisée doctrinalement.  
**Version :** 0.1  
**Date :** 2026-06-01  
**Dépôt :** `barons-Mariani`  
**Chemin :** `research/autonomia/plu_de_corte.md`

---

## 1. Objet de la note

Cette note ouvre une enquête OSINT sur le projet **Riacquistu Data-Driven**, présenté publiquement comme un projet industriel réalisé par des étudiants de Paoli Tech avec la Ville de Corte, EONA-X et l’Università di Corsica.

L’enquête est replacée dans le cadre plus large du **nouveau PLU de Corte**, et plus précisément des enjeux suivants :

- bâti ancien ;
- rénovation et réhabilitation ;
- logement étudiant et familial ;
- observatoire territorial du logement étudiant ;
- ORT, OPAH, POPAC ;
- renouvellement urbain ;
- densification et ZAN ;
- données territoriales, scoring, cartographie et aide à la décision publique.

Cette note ne formule pas de procès d’intention. Elle distingue :

1. les faits publiquement établis ;
2. les éléments non trouvés ou absents des traces publiques accessibles ;
3. les hypothèses de travail ;
4. les questions à vérifier ;
5. les risques démocratiques potentiels associés à un outil fermé d’aide à la décision publique.

---

## 2. Méthode Cogentia appliquée

Conformément à la méthode décrite dans `cogentia/AGENTS.md`, cette enquête reste au stade de l’exploration structurée :

> Conversation for motion.  
> Issue for memory in tension.  
> Opening register for long continuations.  
> Checkpoint for routing.  
> Commit for stabilized memory.  
> Source document for corpus anchoring.

Cette note est donc un **premier conteneur d’enquête**. Elle ne doit pas être lue comme une conclusion définitive, mais comme un support de collecte, de vérification et de montée en preuve.

Référence : <https://github.com/JeanHuguesRobert/cogentia/blob/main/AGENTS.md>

---

## 3. Faits collectés à ce stade

### 3.1. Le PADD de Corte place ces sujets au cœur du PLU

Le document publié par la mairie de Corte sous le titre **Plan Local d’Urbanisme — PADD 2023** présente le PADD comme la « pierre angulaire » du PLU.

Il le définit notamment comme :

- un outil de prospective territoriale ;
- un document politique exprimant le projet de la collectivité ;
- une réponse aux besoins exprimés dans le diagnostic ;
- un document stratégique en faveur du développement durable du territoire.

Source : <https://www.mairie-corte.fr/catalog_repository/uploads/7/2B096_Padd_20231012_VD.pdf?mmg=1%2C697>

### 3.2. Le PADD revendique une démarche d’élaboration itérative

Le PADD indique que son élaboration associe plusieurs types d’acteurs : élus, commission extra-municipale, population, porteurs de projets, personnes publiques associées et consultées.

Cette affirmation est importante pour l’enquête : si un outil de données contribue réellement à préparer ou orienter certaines décisions liées au PLU, sa place dans cette démarche participative doit pouvoir être documentée.

### 3.3. Le PADD vise explicitement le renouvellement urbain et la rénovation du bâti ancien

Le PADD mentionne :

- le renouvellement urbain ;
- la densification ;
- les friches ;
- la requalification ;
- la mutabilité ;
- l’ORT ;
- l’OPAH ;
- le bâti ancien ;
- la vieille ville ;
- la préservation de l’identité architecturale ;
- la rénovation durable du bâti ancien ;
- l’accompagnement des copropriétés via le POPAC.

Ces éléments forment le cadre naturel dans lequel un outil comme Riacquistu Data-Driven peut prendre sens.

### 3.4. Le PADD mentionne le logement étudiant

Le PADD indique vouloir poursuivre la participation active de la commune en matière de logement et de bien-être des étudiants, notamment via l’Observatoire territorial du logement étudiant.

Ce point relie directement :

- le PLU ;
- l’Université de Corse ;
- la ville-université ;
- le logement étudiant ;
- le bâti ancien ;
- l’outil Riacquistu, présenté comme capable de proposer des scénarios de réhabilitation adaptés aux besoins du territoire, notamment en matière de logement étudiant et familial.

### 3.5. Riacquistu Data-Driven est présenté publiquement comme un outil d’aide à la décision

D’après les publications LinkedIn disponibles, Riacquistu Data-Driven est présenté comme une plateforme d’intelligence territoriale pour la rénovation et la valorisation du bâti ancien cortenais.

Le projet aurait pour fonctions :

- identifier le gisement foncier inexploité ;
- qualifier l’état de dégradation du bâti ancien ;
- croiser des données géographiques, cadastrales, urbaines et patrimoniales ;
- proposer des scénarios de réhabilitation ;
- produire une cartographie interactive ;
- produire des outils de monitoring et de scoring ;
- produire les premiers « Cahiers du Riacquistu » ;
- fournir un outil d’aide à la décision mis à disposition de la mairie et de son observatoire territorial du logement étudiant.

Sources publiques initiales : publications LinkedIn de Flora Mattei, EONA-X et participants au projet.

---

## 4. Éléments non trouvés à ce stade

À ce stade de l’enquête, les éléments suivants n’ont pas été trouvés publiquement :

| Élément recherché | Trouvé publiquement ? | Commentaire |
|---|---:|---|
| URL d’accès à l’outil Riacquistu | Non | Aucune interface publique identifiée. |
| Dépôt du code source | Non | Aucun dépôt public Riacquistu identifié. |
| Licence du code | Non | Open source non établi pour le POC local. |
| Liste des données utilisées | Non | Les catégories sont évoquées, pas l’inventaire. |
| Données enrichies / data lake | Non | Aucun accès public identifié. |
| Critères de scoring | Non | Critères et pondérations inconnus. |
| Pondérations | Non | Impossible d’auditer le classement. |
| Cartographie interactive | Non | Annoncée, mais non trouvée publiquement. |
| Cahiers du Riacquistu | Non | Annoncés, mais non trouvés publiquement. |
| Convention Ville / EONA-X / Université | Non | À rechercher dans les actes publics. |
| Délibération municipale spécifique | Non | À rechercher dans les comptes rendus et actes. |
| Cadre RGPD / responsable de traitement | Non | À clarifier si données sensibles ou enrichies. |
| Propriété intellectuelle du POC | Non | Étudiants, université, EONA-X, mairie : non clarifié. |

Ces absences ne prouvent pas l’existence d’une faute. Elles constituent des **points d’enquête**.

---

## 5. Hypothèses de travail

### H0 — Hypothèse neutre minimale

Riacquistu Data-Driven est un simple POC pédagogique, sans usage décisionnel réel.

**À vérifier :**

- absence d’intégration au processus municipal ;
- absence de convention opérationnelle ;
- absence de maintenance ;
- absence de décisions préparées ou orientées par l’outil.

**Élément qui affaiblit déjà H0 :**

Le projet est présenté comme un outil mis à disposition de la mairie et de son observatoire territorial du logement étudiant.

---

### H1 — Hypothèse institutionnelle faible

Riacquistu est un POC utile, fermé par défaut, sans intention problématique, mais dont la publication, la documentation et la gouvernance n’ont pas encore été organisées.

**À vérifier :**

- publication future des Cahiers du Riacquistu ;
- documentation prévue ;
- version publique ou anonymisée envisagée ;
- clarification RGPD ;
- clarification de la propriété intellectuelle ;
- accès possible aux chercheurs, citoyens ou associations.

**Interprétation :**

Dans cette hypothèse, la critique porte sur un défaut de gouvernance et de publication, non sur une manipulation.

---

### H2 — Hypothèse de boîte noire municipale

Riacquistu devient un outil interne d’aide à la décision sur le bâti, le logement et le foncier, sans accès public aux données, critères, scores, cartes ou scénarios.

**Indices compatibles à ce stade :**

- absence d’URL publique trouvée ;
- absence de dépôt public trouvé ;
- absence des Cahiers du Riacquistu trouvés ;
- vocabulaire de mise à disposition de la mairie, non du public ;
- insertion dans des enjeux majeurs du PLU : bâti ancien, logement étudiant, ORT, OPAH, centre ancien, ZAN.

**Interprétation :**

La transparence proclamée par la donnée pourrait devenir une transparence réservée.

---

### H3 — Hypothèse d’asymétrie informationnelle foncière

L’outil produit une connaissance stratégique du bâti et du foncier — vacance, dégradation, potentiel, indivisions, opportunités — accessible à certains acteurs mais non aux citoyens, propriétaires, étudiants ou associations.

**À vérifier :**

- nature exacte du data lake ;
- présence de données sur vacance, indivisions, péril, potentiel de réhabilitation ;
- acteurs ayant accès ;
- droits de consultation, correction ou contestation par les propriétaires ;
- liens avec ORT, OPAH, projets immobiliers et politique du logement étudiant.

**Interprétation :**

Même sans intention manipulatoire, l’asymétrie informationnelle peut produire un avantage objectif au profit des acteurs déjà capables d’agir.

---

### H4 — Hypothèse forte : outil favorable au statu quo ou à la capture de valeur

L’outil pourrait, volontairement ou de fait, favoriser le statu quo et la capture spéculative de la valeur dans un contexte de pénurie structurelle de logements étudiants à Corte.

**État actuel :**

Hypothèse non démontrée.

**Chemin probatoire réaliste :**

Il ne faut pas chercher d’abord l’intention. Il faut documenter :

1. l’opacité de l’outil ;
2. l’asymétrie d’accès ;
3. l’absence de critères publics ;
4. l’absence de contestabilité ;
5. la concentration des bénéfices informationnels ;
6. les décisions ou projets immobiliers postérieurs alignés avec les zones identifiées ;
7. l’exclusion des étudiants, propriétaires modestes, associations ou habitants de la chaîne de décision.

**Formulation prudente :**

L’architecture peut produire des effets de capture, même si l’intention de capture n’est pas établie.

---

## 6. Problème démocratique central

Le point critique n’est pas l’existence d’un outil de données. Un tel outil peut être utile, et même nécessaire.

Le problème apparaît si l’outil :

- prépare des décisions publiques ;
- classe, score ou priorise des biens ;
- produit une cartographie stratégique du bâti ;
- influence les politiques de logement, d’urbanisme ou de rénovation ;
- reste inaccessible au public ;
- ne publie ni son code, ni ses critères, ni ses pondérations, ni ses cahiers, ni ses cartes.

Dans ce cas, il ne produit pas nécessairement une transparence démocratique. Il peut produire une **visibilité asymétrique**.

Formulation de travail :

> Un outil fermé d’aide à la décision publique, portant sur le bâti ancien, le foncier et le logement étudiant dans une ville sous tension, crée objectivement une asymétrie informationnelle au bénéfice des acteurs qui y ont accès.

---

## 7. Questions d’enquête prioritaires

### 7.1. Accès et publication

- L’outil Riacquistu Data-Driven est-il accessible au public ?
- Existe-t-il une URL ?
- Existe-t-il une démonstration publique ?
- Les Cahiers du Riacquistu seront-ils publiés ?
- La cartographie interactive sera-t-elle consultable ?

### 7.2. Code et licence

- Le code source est-il publié ?
- Le projet est-il open source ?
- Si oui, où est le dépôt ?
- Sous quelle licence ?
- Quelles briques relèvent d’EONA-X ?
- Quelles briques ont été développées par les étudiants ?
- Qui maintient l’outil après la restitution ?

### 7.3. Données

- Quelles données cadastrales sont utilisées ?
- Quelles données géographiques ?
- Quelles données urbaines ?
- Quels documents d’urbanisme ?
- Quels arrêtés de péril ?
- Quels inventaires patrimoniaux ?
- Quelles données de terrain ?
- Des données sur la vacance, les indivisions ou les propriétaires sont-elles utilisées ?
- Qui est responsable de traitement ?
- Où le data lake est-il hébergé ?
- Quelle est la durée de conservation ?

### 7.4. Scoring et scénarios

- Quels critères de scoring sont utilisés ?
- Qui les a définis ?
- Comment sont-ils pondérés ?
- Les scores peuvent-ils être contestés ?
- Un propriétaire concerné peut-il corriger une erreur ?
- Les scénarios de réhabilitation sont-ils techniques, financiers, sociaux, patrimoniaux, politiques ?

### 7.5. Cadre institutionnel

- Existe-t-il une convention entre la Ville de Corte, EONA-X, Paoli Tech et l’Université de Corse ?
- Existe-t-il une délibération municipale ?
- L’outil est-il rattaché à l’OTLE ?
- Est-il rattaché à l’ORT ?
- Est-il rattaché à l’OPAH ?
- Est-il pris en compte dans le PLU ou dans sa mise en œuvre ?
- La commission extra-municipale ou la population ont-elles été informées de son existence ?

---

## 8. Matrice OSINT de suivi

| Objet | Source à chercher | État actuel | Prochaine action |
|---|---|---:|---|
| PADD 2023 | Site mairie | Trouvé | Extraire les passages utiles. |
| Rapport de présentation PLU | Site mairie | À vérifier | Chercher fichier PDF. |
| Règlement écrit | Site mairie | À vérifier | Chercher fichier PDF. |
| Règlement graphique | Site mairie | À vérifier | Chercher plan / cartographie. |
| OAP | Site mairie | À vérifier | Chercher OAP Chabrière / centre ancien. |
| Concertation PLU | Site mairie | À vérifier | Chercher comptes rendus / registres. |
| Riacquistu | Mairie / Université / EONA-X | Non trouvé hors LinkedIn | Recherche systématique. |
| Cahiers du Riacquistu | Web / mairie / Université | Non trouvés | Demande ou recherche ciblée. |
| Dépôt code | GitHub / GitLab | Non trouvé | Recherche par noms d’acteurs et mots-clés. |
| Convention | Actes mairie / Université | Non trouvée | Recherche dans délibérations. |
| Données utilisées | Documentation projet | Non trouvées | Demande de liste. |
| Scoring | Documentation projet | Non trouvé | Demande de méthode. |

---

## 9. Formulation publique prudente possible

> J’ouvre une enquête OSINT sur Riacquistu Data-Driven, dans le cadre du nouveau PLU de Corte.  
>  
> Le PADD publié par la mairie montre que les sujets concernés — bâti ancien, renouvellement urbain, ORT, OPAH, logement étudiant, observatoire territorial, outils numériques — sont au cœur de la stratégie municipale.  
>  
> À ce stade, je ne formule pas d’accusation d’intention. Je distingue les faits, les absences documentaires et les hypothèses. Mais une question démocratique se pose déjà : si un outil fermé de scoring et de cartographie contribue à préparer des décisions publiques sur le foncier, le bâti ancien et le logement étudiant, où sont les données, le code, les critères, les cartes, les cahiers, les conventions et les règles d’accès ?  
>  
> Une démarche data-driven peut éclairer l’action publique. Elle peut aussi créer une asymétrie informationnelle si seuls certains acteurs voient la carte. L’enquête vise à établir de quel côté se situe Riacquistu.

---

## 10. Position de méthode

L’enquête doit rester :

- factuelle ;
- sourcée ;
- falsifiable ;
- sans procès d’intention ;
- structurée par hypothèses ;
- attentive aux absences documentaires ;
- ouverte aux réponses des acteurs concernés ;
- centrée sur la traçabilité des actes et des outils d’aide à la décision publique.

Principe de travail :

> Pas d’accusation sans preuve ; mais pas de confiance sans accès, sans méthode publiée et sans traçabilité.

---

## 11. Checkpoint

```text
Type : enquête OSINT en ouverture
Conteneur : note exploratoire dans research/autonomia
Stabilisation doctrinale : non
Document source définitif : non
Produit public : possible, sous forme prudente
Hypothèse dominante actuelle : H2 / boîte noire municipale à vérifier
Hypothèse forte H4 : non démontrée, à instruire
Prochaine étape : inventaire exhaustif des pièces PLU et recherche de toute mention Riacquistu / EONA-X / OTLE / ORT / OPAH dans les documents publics.
```
