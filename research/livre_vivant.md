---
title: "Livre Vivant"
subtitle: "Architecture ouverte de publication continue, contribution engageante, objets adressables et confédération de corpus"
description: "Définition source du concept de Livre Vivant : cinq faces complémentaires, éditions figées issues d'un corpus vivant, retours du Réel, exemplaires physiques adressables, responsabilité éditoriale autonome, confédération de livres et articulation avec les Cogentia Digital Twins."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-02"
last_modified_at: "2026-10-02"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/livre_vivant.md"
document_role: "source"
document_kind: "architecture-note"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
target_audience:
  - "éditeurs de Livres Vivants"
  - "contributeurs"
  - "développeurs de l'infrastructure ouverte"
  - "lecteurs et chercheurs"
document_function: "définition conceptuelle et architecture de référence"
adapted_products:
  - "research/living_book.md"
related_documents:
  - "projects/suicide-corse/editorial-architecture.md"
  - "projects/rise-and-fall/editorial-architecture.md"
  - "projects/diaspora/editorial-architecture.md"
  - "projects/diaspora/architecture.md"
  - "musee-mariani/doctrine_musee_mariani_des_possibles.md"
  - "research/review_protocol.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/trace_treatment_packet.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/individual_and_collective_digital_twins.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/digital_twin_ubiquity.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/artificial_representation_and_mandated_voice.md"
ai_assisted_by:
  - "GPT-5.6 Sol — Redactor, consolidation du Corpus et rédaction v0.1"
review:
  status: "internally-reviewed"
  reviewed_by:
    - "GPT-5.6 Sol — Reviewer interne, même exécuteur que le Redactor ; non indépendant"
provenance:
  origin_type: "conversation"
  origin_repository: "unknown"
  origin_ref: "unknown"
  origin_date: "2026-10-02"
  derived_from:
    - "projects/suicide-corse/editorial-architecture.md"
    - "projects/rise-and-fall/editorial-architecture.md"
    - "projects/diaspora/editorial-architecture.md"
    - "projects/diaspora/architecture.md"
    - "musee-mariani/doctrine_musee_mariani_des_possibles.md"
    - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/pipeline.md"
    - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md"
    - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/trace_treatment_packet.md"
    - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/individual_and_collective_digital_twins.md"
    - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/digital_twin_ubiquity.md"
    - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/artificial_representation_and_mandated_voice.md"
self_review_applied:
  protocol: "cogentia/prompts/redactor.md + cogentia/prompts/reviewer.md"
  decorrelation: "interne seulement ; même modèle, même contexte de rédaction"
  external_review: "pending"
---

# Livre Vivant

## 0. Statut et objet

Ce document commence à stabiliser le concept de **Livre Vivant** tel qu'il émerge de plusieurs réalisations du Corpus, notamment *Suicide Corse*, *Rise & Fall of the Mariani Family* et *DIASPORA*.

Il ne décrit pas seulement un livre électronique que l'on mettrait à jour.

Un Livre Vivant est un **système éditorial relié à un Corpus vivant, à ses lecteurs et au Réel**. Il produit des états lisibles et éventuellement figés, permet leur interrogation, organise la réception de nouvelles traces, et peut s'incarner dans des objets physiques individuellement adressables.

La version française présente constitue le **document source canonique**. La version anglaise prévue, `research/living_book.md`, est un **produit décliné** : elle doit conserver la doctrine de ce document sans devenir une seconde source souveraine par simple traduction.

Le concept est ouvert. C.O.R.S.I.C.A. développe et met gratuitement à disposition des solutions techniques et méthodologiques permettant à des tiers d'éditer leurs propres Livres Vivants. L'infrastructure commune n'emporte pas une responsabilité éditoriale commune.

---

## 1. Définition compacte

> **Un Livre Vivant est un Corpus qui se donne à lire, à suivre, à parcourir et à interroger, tout en permettant au Réel de lui répondre par des traces imputables susceptibles de transformer ses projections futures.**

Le modèle général est :

```text
Réel
  ↓
traces / sources / contributions / observations
  ↓
qualification / contradiction / enquête
  ↓
Corpus vivant
  ↓
projections et surfaces
  ↓
lecture / interrogation / circulation / action
  ↓
nouvelles traces
  ↓
Réel
```

Une édition n'est donc jamais le Corpus.

Elle est un **état daté, sélectionné, composé et éventuellement gelé du Corpus**.

## 1 bis. Grammaire commune des Livres Vivants : trois Machines et une méta-boucle

Les Livres Vivants du Corpus tendent à partager une grammaire plus générale que leur objet éditorial propre.

Au niveau **opérationnel**, trois fonctions reviennent :

~~~text
Machine à Empêcher
→ réduit, ferme, fragilise ou retire des capacités effectives

Machine à Explorer
→ recherche les branches, alternatives, contradictions et futurs encore ouverts

Machine à Rendre Capable
→ transforme certains possibles en capacités effectivement praticables
~~~

Ces trois fonctions ne sont pas des institutions ni des catégories morales. Une même personne, règle, procédure, infrastructure ou publication peut participer à plusieurs fonctions selon le contexte.

Au niveau **transversal**, un couple plus général encore organise la relation du Livre Vivant au Réel :

~~~text
Révélateur
↔
Stabilisateur
~~~

Le **Révélateur** rend visibles les écarts, contradictions, pertes de capacité, inconnues, erreurs de carte, effets inattendus et échecs d'effectivité.

Le **Stabilisateur** rend durables, transmissibles, reproductibles et corrigibles les capacités, connaissances, procédures ou états du Corpus qui méritent de tenir dans le temps.

Le couple n'est pas une quatrième et une cinquième Machine. Il constitue une **méta-boucle épistémique et temporelle** qui traverse les trois Machines :

~~~text
empêchement
→ révélation
→ exploration
→ capacité ouverte
→ stabilisation
→ mesure d'effectivité
→ nouvel écart éventuel
→ révélation
→ correction
~~~

Invariant :

> **Pas de Révélateur sans perspective de stabilisation ; pas de Stabilisateur sans capacité de révéler ses propres échecs.**

Un Révélateur qui ne laisse aucune prise pour agir risque de produire seulement de l'impuissance descriptive. Un Stabilisateur qui masque ses écarts ou rend ses erreurs difficiles à voir peut devenir lui-même une Machine à Empêcher.

Cette méta-boucle donne une fonction générale au Livre Vivant lui-même :

~~~text
Livre Vivant comme Révélateur
→ rendre le Réel reconstructible, contestable et interrogeable

Livre Vivant comme Stabilisateur
→ préserver provenance, états, corrections, éditions gelées,
  méthodes, capacités et chemins de reprise
~~~

### Cas particulier : le Livre Vivant du Musée Mariani des Possibles

Le futur Livre Vivant consacré au **Musée Mariani des Possibles** fournit une instanciation particulièrement complète de cette grammaire commune.

Il relève à la fois de la muséologie théorique, de la muséologie pratique et de la recherche épistémique :

~~~text
méthodes
→ outils
→ dispositifs muséaux
→ réalisations
→ observation des effets
→ correction des méthodes
~~~

Sa structure temporelle est explicitement **janusienne** :

~~~text
regarder vers le passé
→ reconstruire ce qui fut possible
→ identifier les bifurcations, pertes, oublis et chemins non advenus

JANUS

regarder vers l'avenir
→ explorer les futurs praticables
→ rendre visibles les capacités latentes
→ expérimenter, stabiliser et transmettre
~~~

Janus n'est pas ici une métaphore décorative. Il nomme une opération épistémique : **tenir simultanément la reconstruction du passé et l'exploration de l'avenir sans confondre les deux régimes de preuve**.

Le passé impose des exigences de source, de provenance, de chronologie et de causalité. L'avenir relève de scénarios, capacités, conditions de possibilité, expériences et contrefactuels explicitement bornés.

Le couple Révélateur/Stabilisateur traverse les deux faces :

~~~text
face passée
Révélateur → rendre visibles les bifurcations et pertes
Stabilisateur → conserver preuves, objets, gestes, provenance et mémoire

face future
Révélateur → rendre visibles les possibles latents et empêchements actuels
Stabilisateur → transformer certains possibles en capacités durables et transmissibles
~~~

Le Musée Mariani des Possibles peut ainsi être compris comme un **Livre Vivant janusien** : une institution qui regarde en arrière pour comprendre ce qui a rendu le passé possible et en avant pour instruire ce qui pourrait encore le devenir.

Les projets particuliers peuvent accentuer différemment ces fonctions :

- *Suicide Corse* : révéler les écarts d'effectivité et tester les conditions de maintien/réouverture de capacités ;
- *Rise & Fall of the Mariani Family* : révéler les bifurcations intergénérationnelles et stabiliser une mémoire patrimoniale et causale falsifiable ;
- *DIASPORA* : révéler des capacités dispersées et stabiliser des liens, offres, besoins, preuves et mécanismes de mise en relation ;
- futurs Livres Vivants : réemployer cette grammaire seulement si elle résiste à leurs Reality Cases propres.

Le modèle commun proposé est donc :

~~~text
niveau opérationnel
= Machine à Empêcher
  → Machine à Explorer
  → Machine à Rendre Capable

niveau transversal
= Révélateur ↔ Stabilisateur

critère de confrontation
= effectivité

méthode de correction
= retour du Réel → trace → qualification → révision
~~~

L'invariant hérité de *Suicide Corse* et déjà réemployé dans *Rise & Fall* et *DIASPORA* demeure :

> **Freeze the edition, never the next projection.**  
> **Geler l'édition, jamais la projection suivante.**

---

## 2. Les cinq faces

Dans son architecture de référence, un Livre Vivant présente **cinq faces complémentaires** :

1. **Livre** ;
2. **Magazine** ;
3. **Site Web** ;
4. **Agent conversationnel spécialisé** ;
5. **Surface de collecte de traces engageantes**.

Elles ne sont ni cinq copies du même contenu, ni cinq autorités concurrentes.

```text
                         LIVRE
                    profondeur durable
                           │
                           │
 MAGAZINE ─────────── LIVRE VIVANT ─────────── SITE WEB
   delta                  │                    présence
   temporel               │                    publique
                           │
              ┌────────────┴────────────┐
              │                         │
       AGENT CONVERSATIONNEL     COLLECTE ENGAGEANTE
       interroger / comprendre   témoigner / corriger /
                                 contribuer / agir
```

Leur source commune est le Corpus vivant. Leur fonction diffère.

---

## 3. Face Livre : corps principal et annexes

La face **Livre** comporte elle-même deux parties :

```text
Livre
├── corps principal
└── annexes
```

### 3.1. Corps principal

Le corps principal privilégie :

- le récit ;
- l'intelligibilité ;
- les concepts nécessaires ;
- les résultats suffisamment stabilisés ;
- les hypothèses utiles lorsque leur statut est explicite ;
- le mouvement de fond ;
- la transmission à un lecteur qui ne connaît pas encore le Corpus.

Il ne cherche pas à reproduire le Corpus.

> **Le corps principal raconte et rend intelligible.**

### 3.2. Annexes

Les annexes donnent accès à la profondeur documentaire utile à la compréhension et à la vérification :

- glossaire ;
- références ;
- notes ;
- bibliographies ;
- chronologies ;
- données ;
- documents ;
- méthodes ;
- inventaires ;
- éléments de preuve ;
- objections et états épistémiques lorsque leur présence est utile.

Les annexes **font partie du Livre**. Elles ne constituent donc pas une sixième face ni un troisième objet à côté du Livre et du Magazine.

Cette formulation affine le triptyque historiquement développé dans *Suicide Corse* :

> **Le corps principal raconte ; le Magazine actualise ; les annexes documentent et permettent de vérifier.**

---

## 4. Face Magazine : rendre visible le delta

Le **Magazine** répond principalement à la question :

> **Qu'est-ce qui a changé depuis l'état éditorial précédent ?**

Il peut présenter :

- les nouvelles traces ;
- les événements récents ;
- les corrections ;
- les contradictions ;
- les réponses institutionnelles ou humaines ;
- les questions nouvellement ouvertes ;
- les expériences ;
- l'état courant des enquêtes ;
- les conséquences observées des publications précédentes.

Le Magazine est donc orienté vers le **delta temporel**.

```text
Livre
→ ce qui mérite de durer

Magazine
→ ce qui vient de changer
```

Le delta contraint l'attention et la couverture, non la forme. Une nouvelle édition peut changer entièrement de maquette, de rythme, de style ou d'organisation.

> **Continuité épistémique ; liberté esthétique.**

---

## 5. Face Site Web : présence et espace composable

Le Site Web est la **présence publique navigable** du Livre Vivant.

Il ne se réduit pas à afficher le texte du livre. Il peut exposer des **pages** au sens large : unités adressables de connaissance ou de capacité.

Une page peut être notamment :

```text
texte Markdown
page HTML
image
PDF
chronologie
carte
annuaire
jeu de données
formulaire
visualisation
simulateur
agent
application Web
PWA
application mobile
API
objet numérique lié à un objet physique
autre composant composable
```

Ainsi, le wiki sous-jacent n'est pas limité à des pages textuelles.

> **Une page est une unité adressable de connaissance ou de capacité.**

Le Site permet notamment d'accéder :

- aux éditions gelées ;
- à l'état courant ;
- au Magazine ;
- aux annexes ;
- aux références ;
- aux objets et personnes adressables ;
- aux outils ;
- à l'Agent conversationnel ;
- aux surfaces de contribution.

---

## 6. Face Agent conversationnel : interroger sans engager automatiquement

Un Livre Vivant peut être interrogé au moyen d'un **Agent conversationnel spécialisé** fondé sur son Corpus, ses règles de provenance et ses contraintes épistémiques.

Il peut notamment :

- expliquer ;
- retrouver ;
- comparer ;
- citer ;
- reconstruire une chronologie ;
- montrer les objections ;
- distinguer établi, rapporté, inféré, hypothétique et inconnu ;
- expliquer le delta depuis une édition ;
- aider à préparer une contribution ou un Act.

Mais :

```text
Agent ≠ Corpus
réponse de l'Agent ≠ source
conversation ≠ témoignage
conversation ≠ contribution
conversation ≠ Act
```

Cette frontière est constitutive.

Une parole exploratoire ne doit pas être transformée silencieusement en trace engageante.

---

## 7. Face de collecte : les traces engageantes

La cinquième face reçoit des **traces engageantes**, c'est-à-dire des traces qu'une personne décide explicitement de produire ou de soumettre comme contribution, témoignage, correction, contradiction, document, observation ou Act.

Les principaux canaux peuvent être :

```text
Contribution
├── Site Web
├── Agent conversationnel → préparation → Act explicite
└── Exemplaire physique inscriptible
```

Le traitement général est :

```text
trace reçue
→ provenance préservée
→ qualification
→ mise en relation
→ contradiction / test si nécessaire
→ disposition
→ intégration éventuelle
→ propagation éventuelle
```

avec les invariants :

```text
collecter ≠ valider
recevoir ≠ croire
conversation ≠ contribution
publication ≠ établissement d'un fait
```

Cette face rejoint le profil expérimental **Trace Treatment Packet** de Cogentia : packetiser le traitement peut améliorer continuité et traçabilité, mais la packetisation ne remplace jamais l'épistémologie.

---

## 8. Exemplaires physiques uniques et « bouteille à la mer »

Certaines matérialisations papier peuvent devenir des **exemplaires uniques numérotés**.

Il faut distinguer :

```text
edition_id
→ état éditorial gelé

copy_id
→ incarnation physique particulière
```

Un exemplaire produit dans une série matériellement identique peut devenir un objet unique par attribution d'une identité :

- numéro ;
- QR Code unique ;
- éventuellement NFC ou autre mécanisme ;
- inscription, sticker ou marqueur ;
- référence stable vers son double numérique.

L'unicité appartient à l'identité attribuée à l'objet, pas nécessairement à son procédé d'impression.

### 8.1. Double numérique de l'objet

Chaque exemplaire adressable peut disposer d'un **double numérique de l'objet** documentant, selon le projet :

- son `copy_id` ;
- son `edition_id` ;
- sa matérialisation ;
- sa mission éventuelle ;
- sa trajectoire ;
- les événements qui lui sont attachés ;
- les scans ou photographies pertinents ;
- ses annotations ;
- ses forks ;
- les traces suscitées par sa circulation.

```text
objet physique unique
        ↕
identifiant stable
        ↕
double numérique
        ↕
historique des traces
        ↕
Corpus vivant
```

Le double numérique de l'objet ne doit pas être confondu avec un Cogentia Digital Twin de Personne.

### 8.2. Bouteille à la mer

Le concept de **bouteille à la mer**, déjà réemployé dans l'architecture de *Suicide Corse*, apporte une sémantique de circulation :

```text
identité
≠ contenu
≠ mission
≠ incarnation
≠ trajectoire
≠ détenteur
≠ handler
```

Un objet peut être remis, transmis, perdu, retrouvé, reproduit, forké ou rematérialisé. Sa mission peut survivre à certaines transformations de support.

Règle de confidentialité :

> **Identifier l'objet n'implique pas identifier son détenteur.**

---

## 9. Le papier comme voie de retour

Dans certaines éditions « exemplaire unique numéroté », le support de lecture devient lui-même une **surface de collecte**.

Des espaces vierges sont volontairement laissés afin que les lecteurs puissent :

- annoter ;
- corriger ;
- contredire ;
- témoigner ;
- compléter ;
- dessiner ;
- ajouter une référence ;
- laisser une trace de lecture.

Ainsi :

```text
Corpus
→ édition gelée
→ exemplaire physique identifié
→ lecteur
→ inscription manuscrite
→ nouvelle trace physique
→ capture numérique éventuelle
→ qualification
→ intégration éventuelle au Corpus
```

Une inscription manuscrite est immédiatement une **trace matérielle attachée à l'histoire de l'exemplaire**, mais n'est pas automatiquement une assertion validée du Corpus.

Lorsque la trace est numérisée :

```text
original matériel
≠ photographie / scan
≠ transcription
≠ interprétation
```

La provenance entre ces couches doit rester visible.

> **Dans certaines matérialisations du Livre Vivant, le support de lecture est lui-même une surface de contribution.**

L'exemplaire unique devient ainsi un morceau adressable de la mémoire future du Livre Vivant.

---

## 10. Infrastructure ouverte et responsabilité éditoriale

L'association **C.O.R.S.I.C.A.** élabore et met gratuitement à disposition des solutions techniques et méthodologiques permettant de construire des Livres Vivants.

L'objectif est une infrastructure **open source / logiciel libre** lorsque la nature du composant le permet, réutilisable par des éditeurs indépendants.

Il faut distinguer strictement :

```text
C.O.R.S.I.C.A.
→ outils
→ composants
→ formats
→ protocoles
→ documentation
→ références d'implémentation
```

de :

```text
éditeur d'un Livre Vivant
→ thème
→ Corpus
→ ligne éditoriale
→ décisions de publication
→ collecte
→ ours
→ responsabilités correspondant à ses actes
```

L'utilisation du logiciel commun ne transfère pas à C.O.R.S.I.C.A. la responsabilité éditoriale du contenu produit par un tiers.

Un éditeur peut être, selon le projet et sans préjuger de sa qualification juridique exacte :

- une personne physique ;
- une personne morale ;
- un collectif ou une organisation de fait ;
- une institution ;
- une autre entité éditoriale capable d'assumer effectivement le projet.

---

## 11. L'ours éditorial

Chaque Livre Vivant publié comporte un **ours éditorial**, inspiré du modèle classique de la presse et adapté au régime effectivement applicable au projet.

Il vise à rendre immédiatement intelligible notamment :

- le titre ;
- le porteur éditorial ;
- le responsable de la rédaction ;
- le directeur ou responsable de publication lorsqu'une telle qualification s'applique ;
- les coordonnées utiles ;
- l'hébergement ;
- les responsabilités techniques lorsqu'il est utile de les exposer ;
- les licences ;
- les contributions de l'IA lorsqu'elles sont matériellement pertinentes ;
- l'identité de l'édition.

Invariant :

> **Tout Livre Vivant publié doit rendre explicite qui décide de publier et qui assume cette décision.**

L'ours est une surface d'imputabilité. Il ne doit pas inventer une qualification juridique qui ne serait pas applicable.

---

## 12. Confédération de Livres Vivants

Les Livres Vivants ne sont pas destinés à former un super-livre centralisé.

Ils peuvent constituer une **confédération de corpus éditorialement souverains**, chacun gardant :

- son thème ;
- son Corpus ;
- son ours ;
- ses responsables ;
- ses règles éditoriales ;
- son calendrier ;
- ses éditions ;
- ses politiques de contribution.

Ils peuvent cependant référencer et composer des objets provenant les uns des autres.

```text
Livre A ↔ Livre B
   ↕         ↕
Livre C ↔ Livre D
```

### 12.1. Link, don't clone

Règle candidate :

> **Référencer la source souveraine plutôt que la recopier.**

Une page, un concept, une Personne, une source, une chronologie ou une application peut être réutilisée ou projetée dans plusieurs Livres sans que chaque Livre en devienne la source.

Une projection locale peut apporter son contexte propre tout en conservant un pointeur stable vers l'objet référencé.

### 12.2. Trois niveaux

L'architecture peut être lue en trois niveaux :

```text
Niveau 1 — Livre souverain
Corpus, ours, éditions, responsabilité, contributions.

Niveau 2 — Objets fédérés
Pages, concepts, Personnes, lieux, sources, applications,
chronologies, objets physiques et autres ressources adressables.

Niveau 3 — Infrastructure commune
Protocoles, logiciels open source, résolution des références,
provenance, recherche fédérée, formats et outils.
```

C.O.R.S.I.C.A. peut fournir une partie substantielle du niveau 3 sans devenir l'éditeur des objets du niveau 1.

---

## 13. Premiers Livres Vivants identifiés

La liste suivante décrit un chantier, non un registre fermé.

| Livre Vivant | Porteur éditorial envisagé | Domaine |
| --- | --- | --- |
| **Suicide Corse** | futur Fonds de dotation Barons Mariani | Marie-Louise Robert, la Corse et les Machines à Empêcher, à Explorer et à Rendre Capable |
| **Rise & Fall** | Fonds Barons Mariani | histoire vivante de la famille des barons Mariani |
| **DIASPORA** | C.O.R.S.I.C.A. | Corses de l'étranger, diaspora et annuaire contributif de capacités |
| **Capable** | Le Petit Parti | effectivité de Liberté, Égalité, Fraternité |
| **Musée des Possibles** | Fonds Barons Mariani | évolution matérielle et immatérielle du Musée Mariani des Possibles, de la Boutique Mobile aux collections et dispositifs |
| **Autonomia** | C.O.R.S.I.C.A. | matérialisations historiques, présentes et possibles de l'autonomie de la Corse |
| **1755** | Fonds Barons Mariani | travail scientifique sur la Constitution corse de 1755 et ses contributions |
| **PrivAI** | Institut Mariani / C.O.R.S.I.C.A. (préfiguration PrivAI Foundation) | AI Safety politique, souveraineté humaine effective et contre-pouvoirs cognitifs face aux personnes morales augmentées |
| **Commons** | Institut Mariani / C.O.R.S.I.C.A. | Histoire, présent et futurs possibles des biens communs, du pastoralisme traditionnel au cloud et à la cognition |

D'autres candidats présents dans le Corpus pourront être instruits sans être promus mécaniquement au rang de Livre Vivant : Kudos, Kudocracy, FractaVolta, Cogentia, Bien Vivre, Corte / Minesteggio, entre autres.

La séparation doit être guidée par une question simple :

> **Existe-t-il un domaine éditorial suffisamment autonome pour justifier son propre Corpus, son propre ours et sa propre boucle de contribution ?**

---

## 14. Personnes et Cogentia Digital Twins

La confédération a besoin d'une identité adressable des acteurs.

Le Corpus Cogentia distingue déjà :

- la **Personne** ;
- le **Digital Twin** comme structure interprétative gouvernée ;
- les **instances** multiples d'un Twin, chacune située et mandatée.

Il distingue également les Twins de personnes physiques et ceux de personnes morales, et impose de ne pas confondre représentation, identité et autorité.

Le modèle de Livre Vivant ajoute ici une **extension candidate**, encore à réconcilier avec la doctrine Cogentia générale :

> Une même Personne peut être représentée par plusieurs Cogentia Digital Twins distincts.

Cette proposition ne doit pas être confondue avec la multiplicité déjà stabilisée des **instances d'un même Twin**.

```text
Personne P
├── Twin T1
│   ├── instance T1.a
│   └── instance T1.b
├── Twin T2
└── Twin T3
```

### 14.1. Le Twin Principal

Parmi les Twins représentant une Personne, le modèle proposé prévoit :

```text
Personne P
→ 0 ou 1 Twin Principal à un instant donné
```

Le Principal :

- n'est pas nécessairement le premier Twin créé ;
- peut ne pas être attribué au départ ;
- doit être désigné par un événement explicite et traçable selon une autorité appropriée à la Personne ;
- ne rend pas les autres Twins inexistants ;
- peut être remplacé sans effacer l'histoire.

L'état suivant est donc légitime :

```text
principal_twin: UNKNOWN
```

Formule candidate :

> **La pluralité des Twins décrit ; le Twin Principal porte la référence principale lorsqu'elle a été explicitement attribuée.**

Cette formulation est volontairement plus prudente que « le Principal engage » : l'attribution d'un Twin Principal ne lui confère pas, par elle-même, une capacité juridique générale d'engager la Personne. Mandat, identité, représentation et autorité doivent rester séparés.

### 14.2. Création et hébergement récursifs

Un Twin peut fournir l'infrastructure de création ou d'hébergement d'autres Twins.

Les relations doivent être distinguées :

```text
REPRESENTS
CREATED_BY
HOSTED_BY
PRINCIPAL_TWIN_OF
OPERATED_BY
DELEGATED_BY
```

avec :

```text
HOSTED_BY ≠ CONTROLLED_BY
CREATED_BY ≠ PRINCIPAL_TWIN_OF
REPRESENTS ≠ AUTHORIZED_TO_BIND
```

Cette récursivité permet une infrastructure distribuée sans transformer l'hébergeur en autorité sur toutes les Personnes représentées.

### 14.3. Sens de « Personne »

Dans cette architecture documentaire, **Personne** peut être employé comme terme de domaine plus large que la seule personnalité juridique : personne physique, personne morale, collectif ou entité de fait lorsque le projet a besoin de la référencer.

Ce choix de modélisation ne confère aucune personnalité juridique à une entité qui n'en possède pas.

---

## 15. Objets physiques, doubles numériques et Digital Twins : ne pas confondre

Deux formes de « double » coexistent et doivent rester distinctes :

```text
objet physique unique
→ double numérique d'objet
→ identité, état, trajectoire, traces

Personne
→ Cogentia Digital Twin
→ représentation cognitive / documentaire gouvernée
```

Le premier documente un objet.

Le second représente une Personne dans les limites de son Corpus, de ses mandats et de sa gouvernance.

Un exemplaire physique peut être associé à une Personne ou à son Twin sans devenir lui-même un Twin de Personne.

---

## 16. Publication continue et mémoire des corrections

Le contenu nouveau est contraint par l'histoire du contenu.

Il peut :

- ajouter ;
- préciser ;
- corriger ;
- contredire ;
- rétracter ;
- requalifier ;
- rendre visible un inconnu ;
- fermer ou rouvrir une hypothèse.

Mais il ne doit pas réécrire silencieusement l'histoire.

```text
édition N
→ gelée

Corpus courant
→ peut corriger ce qu'elle contenait

édition N+1
→ rend la correction visible
```

Une ancienne édition devient alors un objet historique :

```text
ce que l'on pouvait établir
+ ce que l'on croyait plausible
+ ce que l'on ignorait
+ la forme choisie pour le rendre lisible
```

La correction est un contenu de première classe.

---

## 17. IA : transformation sans souveraineté épistémique

L'IA peut contribuer à :

- rechercher ;
- rapprocher ;
- structurer ;
- résumer ;
- traduire ;
- rédiger ;
- illustrer ;
- construire des applications ;
- préparer des projections ;
- aider aux contrôles de couverture ;
- préparer des contributions ;
- effectuer des revues.

Mais :

> **L'IA appartient au processus de transformation ; elle ne remplace ni la provenance, ni la qualification des traces, ni la responsabilité éditoriale, ni l'autorité d'une Personne.**

```text
capacité ≠ autorité
cohérence ≠ vérité
style ≠ identité
représentation ≠ mandat
```

---

## 18. Caractéristiques constitutives candidates

À ce stade, un Livre Vivant au sens de ce document devrait tendre à posséder :

1. un **Corpus vivant identifiable**, distinct de ses projections ;
2. une face **Livre**, avec corps principal et annexes ;
3. une face **Magazine**, rendant le delta intelligible ;
4. une face **Site Web**, capable d'exposer des pages allant du texte à l'application ;
5. un **Agent conversationnel spécialisé** ;
6. une **surface de collecte de traces engageantes**, distincte de la simple conversation ;
7. des états ou éditions **identifiables et gelables** ;
8. une mémoire des corrections et requalifications ;
9. une provenance et des statuts épistémiques explicites ;
10. un **ours** identifiant la responsabilité éditoriale ;
11. la possibilité de références fédérées vers d'autres Livres et objets ;
12. une séparation entre infrastructure commune et responsabilité éditoriale ;
13. lorsque des exemplaires physiques adressables existent, une distinction `edition_id` / `copy_id` et un double numérique de l'objet ;
14. lorsque des surfaces manuscrites existent, une conservation de la trace physique et de sa provenance ;
15. lorsque des Personnes et Twins sont mobilisés, une séparation stricte entre Personne, Twin, instance, Principal, hébergeur et mandat.

Toutes ces propriétés n'ont pas nécessairement le même niveau de maturité ni le même caractère obligatoire. La continuation devra distinguer **invariants nécessaires**, **capacités recommandées** et **extensions optionnelles**.

---

## 19. Ce qu'un Livre Vivant n'est pas

Un Livre Vivant n'est pas, par définition :

- un simple fichier régulièrement remplacé ;
- un wiki sans responsabilité éditoriale identifiable ;
- un chatbot ;
- un système où toute conversation devient une contribution ;
- un dépôt brut de documents ;
- une base de données présentée comme vérité ;
- une édition papier silencieusement corrigible ;
- un système où l'infrastructure technique devient propriétaire de la ligne éditoriale ;
- un super-wiki centralisant tous les thèmes ;
- un Digital Twin de Personne.

Il peut utiliser chacun de ces objets ou techniques sans se réduire à eux.

---

## 20. Reality Cases initiaux

### 20.1. Suicide Corse

Premier Reality Case complet actuellement le plus avancé : publication continue, éditions gelées, Livre, Magazine, annexes, Guide, collecte, exemplaires adressables en cours de conception, boucle explicite avec le Réel.

### 20.2. Rise & Fall

Deuxième application montrant que l'architecture n'est pas spécifique au suicide ni à l'enquête contemporaine : l'histoire familiale elle-même reste vivante par nouvelles sources, contradictions, interprétations et contributions.

### 20.3. DIASPORA

Troisième application, particulièrement importante parce que le Livre Vivant se combine avec un **annuaire contributif de capacités** et des pages fonctionnelles. Elle montre que le Livre peut se prolonger en outil sans cesser d'être publication.

### 20.4. Musée des Possibles

Le Musée fournit un terrain naturel pour tester :

- la Boutique Mobile comme bootstrap par la fin du parcours classique ;
- la vente ou circulation d'objets uniques ;
- les exemplaires physiques de Livres Vivants ;
- les doubles numériques d'objets ;
- la contribution du public ;
- le passage de la trace au stabilisateur.

### 20.5. PrivAI

Cinquième application majeure, centrée sur la thèse de la souveraineté humaine face aux personnes morales augmentées par l'intelligence artificielle. PrivAI met à l'épreuve le Livre Vivant sur un terrain de haute autorité constitutionnelle et politique :
- le principe **Anti-Demos** (interdiction de la personnalité politique et du droit de vote accordés aux entités algorithmiques ou personnes morales) ;
- la grille d'asymétrie cognitive et capacitaire ;
- la traçabilité des actes publics ;
- la doctrine de non-substitution du jugement humain.

### 20.6. Commons

Sixième application, dédiée à l'histoire, au présent et aux avenirs possibles des biens communs sous tous leurs substrats (« Des communaux au cloud »). Commons instancie de manière exemplaire l'architecture complète des **cinq faces** du Livre Vivant :
- **Livre :** récit en 4 mouvements et annexes démonstratives (*Carta de Foresta*, archives corses, grille d'audit Ostrom, comparatif des licences d'IA) ;
- **Magazine :** chroniques vivantes de terrain (enclosure du cloud et calcul GPU, microréseaux solaires FractaVolta et monnaie d'utilité collective Kudos/CXU) ;
- **Site Web :** surface statique de lecture publique universelle (`commons.acorsica.org`) ;
- **Agent conversationnel :** profil de Guide public borné fondé sur 8 invariants stricts et zéro rétention de données ;
- **Surface de collecte engageante :** interface locale de génération de brouillons d'objections et de corrections.

Elle illustre comment le Livre Vivant relie une mémoire territoriale profonde (les communaux pastoraux du Niolu) aux architectures contemporaines de souveraineté cognitive et énergétique.

---

## 21. Revue interne Redactor / Reviewer

### 21.1. Déclaration de décorrélation

La présente revue a été réalisée par **le même exécuteur GPT-5.6 Sol** que la rédaction. Elle constitue donc une **revue interne**, utile pour détecter contradictions, sur-promesses et défauts de structure, mais **ne constitue pas une confirmation indépendante** au sens du contrat `cogentia/prompts/reviewer.md`.

Une revue externe décorrélée par un autre modèle ou un humain reste souhaitable avant stabilisation forte.

### 21.2. Findings intégrés

| Finding | Disposition | Intégration |
| --- | --- | --- |
| Le triptyque historique « Livre / Magazine / Annexes » entrait en conflit avec la décision que les annexes appartiennent au Livre. | `corrected` | Le modèle est désormais cinq faces ; la face Livre contient corps principal + annexes. |
| « Le Principal engage » pouvait confondre référence du Twin et pouvoir juridique. | `corrected` | Le texte parle de Twin Principal comme référence principale ; l'autorité exige toujours un mandat distinct. |
| Le Corpus existant stabilise plusieurs **instances d'un Twin**, pas plusieurs Twins pour une même Personne. | `integrated` | La pluralité de Twins et l'unicité candidate du Twin Principal sont marquées explicitement comme extension à réconcilier. |
| « Personne » risquait de conférer implicitement la personnalité juridique à un collectif de fait. | `corrected` | Le document distingue le terme de domaine de la qualification juridique. |
| « double numérique » pouvait confondre objet physique et Digital Twin cognitif. | `corrected` | Une section sépare explicitement les deux notions. |
| L'usage de l'ours pouvait être présenté comme une qualification juridique automatique. | `conceded:bounding` | L'ours est un mécanisme d'imputabilité inspiré de la presse ; les qualifications exactes restent celles du régime applicable. |

### 21.3. Points encore ouverts

- déterminer les critères exacts séparant invariant obligatoire, recommandation et extension ;
- définir la sémantique stable de `Person`, `Twin`, `PrincipalTwin`, `HostedBy`, `CreatedBy` et `Represents` dans Cogentia ;
- décider si l'identité fédérée des pages mérite un protocole ou seulement une convention d'URI ;
- préciser l'articulation entre licence du logiciel, licence des contenus et droits attachés aux contributions ;
- tester la voie papier → scan → qualification → Corpus sur un exemplaire réel ;
- produire une revue externe décorrélée ;
- dériver ensuite `research/living_book.md` à partir du présent document, sans créer de divergence doctrinale.

---

## 22. Continuation

La continuation immédiate proposée est :

```text
livre_vivant.md v0.1
→ revue adverse externe décorrélée
→ arbitrage humain
→ distinction MUST / SHOULD / MAY
→ intégration des premiers Reality Tests
→ dérivation living_book.md
→ propagation contrôlée vers Suicide Corse / Rise & Fall / DIASPORA
→ éventuel protocole fédéré minimal
```

Le document ne doit pas devenir une super-spécification prématurée.

La bonne séquence reste :

> **Dogfood d'abord. Généraliser ce que plusieurs Reality Cases rendent réellement commun.**

---

## Formule finale

> **Un Livre Vivant n'est pas un livre que l'on corrige sans fin. C'est un système éditorial traçable : un Corpus vivant produit des éditions lisibles et parfois immuables, rencontre des lecteurs et des objets dans le Réel, reçoit leurs réponses par des voies explicitement engageantes, puis transforme ce retour en matière possible pour les projections suivantes.**
