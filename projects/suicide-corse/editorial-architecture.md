---
title: "Suicide Corse — Architecture éditoriale"
subtitle: "Publication continue, éditions figées, asymétrie fond/forme et matérialisations"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-29"
last_modified_at: "2026-09-29"
version: "0.1"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "editorial-architecture"
document_kind: "working-note"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/suicide-corse/editorial-architecture.md"
update_policy: "UP-DEFAULT-REVIEWED"
ai_assisted_by:
  - "ChatGPT"
provenance:
  origin_type: "corpus-consolidation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "main"
  origin_date: "2026-09-29"
  derived_from:
    - "projects/suicide-corse/architecture.md"
    - "projects/suicide-corse/corpus.yml"
    - "projects/suicide-corse/editions/index.md"
    - "projects/suicide-corse/projections/n3-editorial-architecture.md"
    - "GitHub issue #51"
    - "GitHub issue #75"
    - "GitHub issue #84"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Suicide Corse — Architecture éditoriale

## 0. Objet

*Suicide Corse* n'est ni seulement un livre, ni seulement une revue, ni seulement un site, ni seulement une enquête.

C'est un **Corpus vivant** qui peut produire plusieurs projections éditoriales. Certaines projections sont publiées et **figées** à une date donnée ; le Corpus, lui, continue ensuite à évoluer.

Cette note stabilise l'architecture éditoriale qui était déjà présente de façon dispersée dans l'architecture d'enquête, le manifeste du Corpus, les contrats de projection et les Issues de publication.

Elle ne remplace pas :

- l'[architecture d'enquête](architecture.md), qui gouverne les Reality Cases, les mécanismes, les objections et les invariants candidats ;
- l'architecture documentaire, qui gouverne les sources, chronologies, registres, sous-corpus et états épistémiques ;
- les contrats de projection propres à chaque édition.

Elle définit **la relation entre le Corpus vivant et ses éditions**.

---

# 1. Nature de l'objet : publication continue à éditions figées

Le modèle général est :

```text
traces / sources / contributions / réponses du Réel
→ qualification et intégration au Corpus
→ Corpus vivant
→ intention éditoriale
→ projection candidate
→ contrôles de couverture et de provenance
→ freeze
→ édition immuable
→ diffusion / matérialisation
→ réponses du Réel
→ nouvelles traces
→ Corpus vivant
```

Une édition n'est donc jamais « le Corpus ».

Elle est :

> **un état daté, sélectionné, composé et gelé du Corpus.**

Le Corpus peut ensuite corriger, enrichir, contredire ou requalifier ce qui apparaissait dans cette édition sans réécrire silencieusement l'objet historique déjà publié.

Règle :

> **Freeze the edition, never the next projection.**

---

# 2. Principe d'asymétrie éditoriale

Le principe central est asymétrique :

> **Le contenu nouveau est contraint par l'histoire du contenu ; la forme nouvelle n'est pas contrainte par l'histoire des formes.**

## 2.1. Continuité forte du contenu

Un état éditorial ultérieur ne peut pas agir comme si les états antérieurs n'avaient jamais existé.

Le nouveau contenu peut :

- ajouter ;
- préciser ;
- corriger ;
- contredire ;
- rétracter ;
- requalifier ;
- rendre visible un `UNKNOWN` auparavant masqué ;
- fermer une hypothèse ;
- rouvrir une question à la lumière d'une nouvelle trace.

Mais ces opérations doivent conserver une provenance suffisante pour comprendre **ce qui a changé et pourquoi**.

Ainsi :

```text
C(n)
→ ajout | précision | correction | contradiction | rétractation | requalification
→ C(n+1)
```

avec :

```text
C(n+1) est historiquement contraint par C(n)
```

Une correction est un contenu de première classe. Elle n'est pas un échec à cacher.

## 2.2. Liberté forte de la forme

À l'inverse :

```text
F(n) ↛ F(n+1)
```

Une édition nouvelle n'est pas tenue de conserver :

- la maquette ;
- la typographie ;
- le genre visuel ;
- l'ordre des rubriques ;
- la grammaire narrative ;
- le format physique ;
- le rapport texte/image ;
- la logique d'illustration ;
- le style du numéro précédent.

Seuls subsistent les éléments d'identification, de responsabilité, de provenance et de lisibilité nécessaires à l'intégrité de la publication.

Formule de compression :

> **Continuité épistémique ; liberté esthétique.**

Autre formulation :

> **Le fond a une mémoire obligatoire. La forme a un droit permanent à l'oubli.**

---

# 3. Une édition comme exercice de publication

Chaque édition peut être conçue comme une **interprétation formelle autonome** du même Corpus historique.

La référence littéraire candidate est *Exercices de style* de Raymond Queneau : la variation n'est pas un simple habillage de couverture, mais peut traverser la totalité de l'objet.

Une contrainte stylistique peut porter sur :

- la couverture ;
- la typographie ;
- la mise en page ;
- l'iconographie ;
- la structure du sommaire ;
- le rythme des textes ;
- la représentation des sources ;
- les encadrés ;
- les cartes et diagrammes ;
- la quatrième de couverture ;
- le choix du papier et du façonnage pour une matérialisation physique.

Exemples de régimes possibles :

```text
dossier d'instruction
journal populaire
carnet de laboratoire
atlas
correspondances
cahier d'écolier
revue futuriste
roman-photo documentaire
catalogue
```

Ces exemples ne constituent ni une liste fermée ni un programme de numéros.

Le style ne peut jamais modifier silencieusement le statut épistémique du contenu. Un fait reste un fait, une hypothèse reste une hypothèse, une fiction de mise en scène reste une fiction de mise en scène.

---

# 4. Chaque édition peut être un collector

Le caractère « collector » ne repose pas sur une rareté artificielle.

Il découle de trois propriétés réelles :

1. **un état historique unique du Corpus** ;
2. **un freeze irréversible de cette édition** ;
3. **une forme éditoriale qui n'a aucune obligation d'être reproduite dans l'édition suivante**.

Ainsi, une ancienne édition n'est pas nécessairement obsolète lorsque l'enquête progresse.

Elle devient un **objet historique** :

```text
ce que l'enquête pouvait alors établir
+ ce qu'elle croyait plausible
+ ce qu'elle ignorait encore
+ la manière singulière dont cet état fut rendu lisible
```

Une hypothèse ultérieurement réfutée ne doit pas être effacée de l'ancienne édition. Le Corpus courant doit en revanche rendre visible la correction.

---

# 5. Livre, Magazine, Annexes / Corpus

La distinction élaborée pour le n°3 reste une architecture de lecture utile, sans devenir une maquette obligatoire :

```text
Livre
= connaissance durable, mouvement de fond, récit et concepts nécessaires

Magazine
= delta depuis l'édition précédente, actualité de l'enquête, réponse récente du Réel

Annexes / Corpus
= preuve, chronologie, inventaires, hypothèses, méthode et profondeur de vérification
```

Principe :

> **Le corps principal raconte ; le Magazine actualise ; les annexes démontrent.**

Cette distinction est fonctionnelle.

Une future édition peut la rendre graphiquement méconnaissable, fusionner certaines surfaces ou inventer une autre organisation, tant que les fonctions restent correctement assumées.

---

# 6. Delta : contrainte d'attention, jamais contrainte de forme

Une nouvelle édition doit examiner ce qui a changé depuis la précédente.

Mais le Delta Review ne constitue pas un plan.

```text
Corpus courant
→ intention éditoriale libre
→ projection candidate
→ Delta Review / Coverage
→ révision éventuelle
→ freeze
```

Le delta contraint :

- l'attention ;
- la couverture ;
- la traçabilité ;
- la prise en compte des corrections et contradictions.

Il ne contraint pas :

- le sommaire ;
- l'ordre ;
- le style ;
- la longueur ;
- la maquette ;
- la reprise des mêmes chapitres.

Règle :

```text
source-locked ≠ editorial-locked
```

---

# 7. Cadence : pivots et déclenchements éditoriaux

*Suicide Corse* est une publication continue ; son rythme éditorial ne doit pas être réduit à une obligation artificielle de « remplir un numéro ».

Deux mécanismes peuvent coexister.

## 7.1. Éditions pivots

Hypothèse de travail actuelle : quatre jalons annuels faciles à identifier, formant un heartbeat minimal :

```text
21 mars
24 juin
17 septembre
25 décembre
```

Le **17 septembre** possède un statut particulier : il est le pivot anniversaire et peut donner son origine symbolique au cycle annuel de *Suicide Corse*.

Ces dates sont des **points d'ancrage éditoriaux**, non des obligations de volume. Une édition pivot peut être courte si le Corpus le justifie.

Leur emploi doit rester compatible avec les règles administratives effectivement applicables au moment où un statut de publication de presse est recherché ; la présente architecture ne vaut pas qualification juridique automatique.

## 7.2. Éditions déclenchées par le contenu

Entre deux pivots, une édition supplémentaire peut être décidée lorsqu'un état de l'enquête **mérite une nouvelle cristallisation** :

- nouvelle trace structurante ;
- retournement d'une hypothèse ;
- correction importante ;
- événement extérieur matériel ;
- ensemble cohérent de contributions ;
- avancée méthodologique ou documentaire substantielle ;
- autre seuil éditorial explicite.

Ainsi :

> **cadence minimale structurée, cadence effective agile.**

Le plafond candidat de **52 éditions par an** exprime une borne de non-flux : *Suicide Corse* peut être réactif sans devenir un fil continu dépourvu de seuil éditorial.

---

# 8. Papier : matérialisation, pas source

Le papier n'est pas l'aboutissement naturel ni la source de vérité de *Suicide Corse*.

Il est une **matérialisation physique d'une édition gelée**.

```text
Corpus vivant
→ projection
→ freeze
→ édition
   ├── HTML
   ├── PDF
   ├── EPUB
   └── matérialisation papier éventuelle
```

Le papier possède des propriétés propres :

- physicalité ;
- finitude ;
- impossibilité de patch silencieux ;
- archivabilité ;
- transmissibilité ;
- distribution hors ligne ;
- collectionnabilité.

Une matérialisation papier est donc justifiée lorsque :

```text
valeur éditoriale de l'état gelé
+ intérêt de l'objet physique
+ conditions économiques acceptables
→ matérialisation
```

Il n'existe aucune obligation doctrinale d'imprimer chaque état ou chaque publication numérique.

---

# 9. IA : liberté générative sous contrainte épistémique

L'IA fait partie du processus éditorial de *Suicide Corse*.

Elle peut contribuer notamment à :

- rechercher et rapprocher des éléments ;
- proposer des structures ;
- résumer ;
- comparer ;
- rédiger ou réécrire des formulations ;
- traduire ;
- explorer des formes graphiques ;
- produire des variantes ;
- préparer des projections ;
- aider à auditer cohérence, couverture et contradictions.

Mais :

> **l'IA appartient au processus de transformation ; elle ne remplace ni la provenance des sources, ni les contrôles épistémiques, ni la décision éditoriale, ni la responsabilité humaine.**

Le régime est volontairement asymétrique.

## 9.1. Sur le fond

```text
sources
→ qualification
→ assistance IA possible
→ rédaction / restructuration
→ contrôle épistémique
→ décision et responsabilité éditoriales humaines
```

La génération ne peut pas convertir une hypothèse en fait, une lacune en certitude, une ressemblance en causalité ou un récit plausible en trace.

## 9.2. Sur la forme

```text
contrainte artistique
→ exploration générative large
→ variantes nombreuses
→ sélection / correction humaines
→ réalisation
```

L'IA peut donc augmenter très fortement l'espace des formes possibles précisément parce que la couche de contenu demeure gouvernée par des contraintes de provenance et de statut.

Règle :

> **L'IA peut élargir la forme sans relâcher la contrainte épistémique sur le fond.**

Les usages matériels de l'IA doivent rester suffisamment documentés pour que la provenance éditoriale puisse être comprise et auditée.

---


# 9 bis. Matérialisation solidaire et Kudos

L'architecture papier peut distinguer plusieurs matérialisations du **même contenu** :

```text
numérique
→ gratuit

papier accessible
→ prix bas

papier collector
→ objet plus riche

papier suspendu
→ remis sans paiement au bénéficiaire lorsqu'un exemplaire financé est disponible
```

La doctrine Kudos fournit une couche complémentaire de don / contre-don à ce mécanisme.

Référence : [`../../research/kudos.md`](../../research/kudos.md).

Les trois registres restent séparés :

```text
euros
→ financent la matière et la transaction réelle

exemplaires suspendus
→ représentent une capacité matérielle disponible

Kudos
→ documentent et prolongent des actes de don / contre-don selon les règles propres à Kudos
```

Règle :

> **L'euro matérialise ; le suspendu partage ; le Kudos ouvre et mémorise le contre-don.**

Le Kudos ne remplace donc pas le règlement initial en euros et ne devient pas un coupon d'achat automatique pour *Suicide Corse*.

La solidarité ne doit pas non plus créer une hiérarchie éditoriale :

> **Le collector ne donne pas accès à davantage de contenu ; il donne accès à davantage d'objet.**

Une contribution non monétaire à l'enquête — source, correction, vérification, traduction, distribution, contradiction utile — peut être aussi pertinente pour Kudos qu'un acte de financement.

Principe anti-capture :

```text
capacité économique ≠ mérite contributif
montant donné ≠ autorité éditoriale ou morale
```


# 10. Publication réactive

Une publication est dite **réactive** lorsque ses propres Acts peuvent produire des réponses du Réel qui reviennent ensuite modifier le Corpus.

```text
Corpus
→ projection
→ publication / Act
→ lecteur / témoin / institution / événement
→ réponse
→ trace
→ qualification
→ Corpus corrigé
→ nouvelle projection possible
```

Le produit publié n'est donc pas un terminal mort.

Il peut :

- susciter un témoignage ;
- faire apparaître une pièce ;
- provoquer une contradiction ;
- révéler une erreur ;
- ouvrir une voie de recherche ;
- susciter un Act extérieur ;
- produire une nouvelle observation.

La publication devient alors elle-même un instrument de l'enquête.

---

# 11. Contribution : le lecteur peut modifier l'état futur

Le lecteur de *Suicide Corse* n'est pas seulement destinataire.

Il peut devenir :

- témoin ;
- contradicteur ;
- source ;
- contributeur ;
- vérificateur ;
- détenteur d'une pièce ;
- explorateur d'une question ouverte.

Une contribution n'entre jamais automatiquement dans le Corpus stabilisé.

Elle suit la même discipline que les autres traces :

```text
contribution
→ provenance
→ qualification
→ contradiction / vérification
→ intégration éventuelle
→ effet éventuel sur une édition future
```

Le papier peut donc aussi servir de **capteur hors ligne**, en dirigeant le lecteur vers les canaux contributifs appropriés.

---

# 12. Immutabilité et corrections

Une édition gelée reste immuable.

Une erreur découverte après publication suit normalement le mouvement :

```text
édition N contient X
→ nouvelle trace / objection
→ X doit être corrigé ou requalifié
→ Corpus courant enregistre la correction
→ édition N reste historiquement intacte
→ édition N+1 ou erratum explicite rend la correction visible
```

La correction silencieuse d'une édition gelée détruirait précisément la valeur historique et probatoire du freeze.

L'immutabilité n'interdit donc pas la correction.

Elle impose que **la correction ait elle-même une histoire**.

---

# 13. Invariants éditoriaux

À l'état actuel, les invariants suivants sont stabilisés comme règles de travail :

```text
Corpus ≠ projection
projection ≠ source
édition gelée = immuable
future projection = libre
plan précédent ≠ plan obligatoire
source-locked ≠ editorial-locked
delta contraint l'attention, pas la forme
contenu nouveau hérite de l'histoire du contenu
forme nouvelle n'hérite pas nécessairement de la forme ancienne
correction = contenu de première classe
papier = matérialisation éventuelle, pas source
IA = moyen de transformation, pas autorité épistémique
publication = Act susceptible de produire de nouvelles traces
```

---

# 14. Architecture résumée

```text
                         CORPUS VIVANT
                              │
                contenu historiquement contraint
                              │
                     état courant du Corpus
                              │
                              ▼
                   INTENTION ÉDITORIALE
                              │
                 forme libre / exploratoire
                 IA largement mobilisable
                              │
                              ▼
                        PROJECTION
                              │
              Delta Review / provenance / contrôle
                              │
                            FREEZE
                              │
                      ÉDITION IMMUABLE
                    /      |       |       \
                  web     PDF     EPUB    papier
                                           │
                                        collector
                                           │
                                           ▼
                                   RÉPONSE DU RÉEL
                                           │
                                           └──→ Corpus
```

Formule de compression :

> **Un objet sémantique vivant, historiquement contraint, périodiquement interprété sous une forme libre puis figé comme édition vérifiable.**
