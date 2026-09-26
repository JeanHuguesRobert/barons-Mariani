---
title: "Suicide Corse — enquête et publication réactive"
description: "Point d'entrée canonique du projet Suicide Corse : Corpus vivant, enquêtes, projections et éditions datées."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-09-18"
last_modified_at: "2026-09-26"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "source-index"
document_kind: "project-readme"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/suicide-corse/README.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "generated"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "GitHub issues #42, #75, #80, #81"
  origin_date: "2026-09-07"
  derived_from:
    - "projects/suicide-corse/architecture.md"
    - "projects/suicide-corse/corpus.yml"
    - "memory/marie-louise/README.md"
    - "GitHub issue #81"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Suicide Corse

**Titre de travail : _Suicide Corse, ou comment réaliser l'impossible_.**

*Suicide Corse* est un **processus d'enquête, de mémoire et de publication réactive**. Il ne se confond ni avec un manuscrit particulier, ni avec une édition datée, ni avec le sous-corpus consacré à Marie-Louise.

La règle structurante est :

```text
Corpus vivant
→ qualification épistémique
→ enquête / modèles / Reality Cases
→ projection éditoriale
→ édition datée / Act
→ réponse du Réel
→ nouvelles traces
→ correction du Corpus
→ nouvelle projection
```

Une édition peut donc être gelée tandis que le Corpus continue d'évoluer.

## État courant — 26 septembre 2026

### Numéro spécial anniversaire — 17 septembre 2026

Le numéro spécial du 17 septembre 2026 est **gelé**. Son identité, son commit source, ses artefacts et son manifeste sont enregistrés dans [`editions/index.md`](editions/index.md) et [`editions/2026-09-17-freeze.md`](editions/2026-09-17-freeze.md).

Le gel protège cette projection historique ; il ne clôt ni l'enquête, ni les Continuations, ni le Corpus.

### Suicide Corse n°2 — 21 septembre 2026

Le n°2 est **totalement bouclé et gelé**. Son chantier éditorial historique reste documenté par [#81](https://github.com/JeanHuguesRobert/barons-Mariani/issues/81), avec le bouclage technique et éditorial tracé par #83.

Le gel interdit toute réinjection silencieuse de découvertes ultérieures. Les réponses et événements postérieurs appartiennent au Corpus courant, au n°3 ou à un erratum explicitement identifié.

### Suicide Corse n°3 — en construction

Le chantier éditorial actif est [l'issue #84](https://github.com/JeanHuguesRobert/barons-Mariani/issues/84). Sa surface de travail est [`projections/book-n3-working.yml`](projections/book-n3-working.yml) et son journal courant [`journals/2026-09-23-n3-construction.md`](journals/2026-09-23-n3-construction.md).

Le n°3 doit désormais être **bouclé le lundi 28 septembre 2026 au matin**. Son sommaire et sa longueur restent ouverts jusqu'au freeze : la fin de semaine est assumée comme une **phase magazine à forte intensité**, capable d'intégrer les réponses du Réel jusqu'au dernier moment sans modifier les éditions déjà gelées. Il collecte le delta postérieur au n°2 sans présumer de sa composition. Parmi les entrées désormais enregistrées figure le **delta sénatorial du 25 septembre** : réception effective du jugement du TA, résolution de l'heure 15:49 pour la note en délibéré, résidus documentaires persistants, relance du greffe et demande formelle d'accès aux traces auprès de la préfecture.

Principe : **le delta contraint l'attention ; il ne dicte pas le sommaire.**

### Axe longitudinal désormais prioritaire

Le delta du 26 septembre impose un changement de focale : le contentieux sénatorial 2026 n'est plus traité comme un îlot. Il devient un **Reality Case contemporain** dans une enquête beaucoup plus longue sur la continuité des capacités, des protections et des recours.

Deux lignes temporelles doivent être distinguées puis confrontées :

- **histoire électorale documentée : 2017–2026**, avec Marie-Louise et Jean Hugues dans des rôles successifs de candidate, suppléante, remplaçante proposée ou requérante ;
- **histoire de protection de Marie-Louise : antérieure à 2017**, incluant l'intervention de la justice au titre de l'assistance éducative et, plus largement, la question de la continuité entre institutions de protection.

L'enjeu éditorial n'est pas de construire une causalité totale. Il est de demander, à chaque bifurcation : **quel possible existait encore, qui pouvait agir, avec quelle information, dans quel délai, et quelle capacité a été maintenue, réduite, réouverte ou définitivement perdue ?**

Cette ligne permet de reboucler explicitement sur *Suicide Corse* : la perte de chance, la continuité de protection, l'effectivité des droits et la fermeture des possibles deviennent des objets communs à plusieurs Reality Cases, sans supposer une identité de mécanisme entre eux.

### Appel à témoignages

L'appel public à témoignages est actif sur [suicidecorse.baronsmariani.org](https://suicidecorse.baronsmariani.org). Son implémentation documentaire et son pipeline de réception structurée sont suivis par [l'issue #80](https://github.com/JeanHuguesRobert/barons-Mariani/issues/80).

Principe : simplicité pour le témoin, conservation privée de la source, qualification structurée, et décision de publication séparée. Le dépôt public ne doit pas devenir un entrepôt de messages privés ou de données sensibles.

## Architecture documentaire

Le projet distingue trois architectures qui ne doivent plus être confondues :

1. **architecture d'enquête** — concepts, Reality Cases, invariants candidats, objections, Acts et réponse du Réel ;
2. **architecture documentaire** — sources, sous-corpus, chronologies, registres, méthodes, Knowledge Gaps et provenance ;
3. **architecture éditoriale** — sélection temporaire de cette matière pour un numéro, un site, un catalogue, un scénario ou une autre projection.

[`architecture.md`](architecture.md) décrit principalement la première. [`corpus.yml`](corpus.yml) sert de manifeste navigable de la seconde. Les contrats de [`projections/`](projections/) et le registre [`editions/`](editions/) décrivent la troisième.

## Marie-Louise : sous-corpus, non simple chapitre

Marie-Louise est à la fois une personne dont les traces ont une valeur propre, un Reality Case longitudinal et un cas possible de l'enquête causale sur le suicide. Ces trois régimes restent séparés.

Le sous-corpus [`memory/marie-louise/`](../../memory/marie-louise/) comprend notamment :

- carte et chronologies ;
- formation et trajectoire artistique ;
- œuvres et catalogue raisonné en construction ;
- élections et représentations publiques ;
- matrice des possibles et contrôles épistémiques ;
- enquête sur les pièces et traces détenues ou liées à la gendarmerie ;
- témoins potentiels, méthode de collecte et réception des contributions.

Les recherches généalogiques Mariani / Casabianca / d'Angelis appartiennent au Corpus familial plus large et peuvent être projetées dans *Suicide Corse* lorsqu'elles sont éditorialement pertinentes. Elles ne sont pas créées pour confirmer a posteriori une théorie du suicide.

Les travaux récents sur les identités et représentations imposent une discipline supplémentaire : distinguer personne, compte, adresse technique, nom affiché, signature, nom inscrit dans une pièce, contexte, période, source et statut épistémique. Une coexistence de noms ou d'identités numériques ne constitue pas, par elle-même, une interprétation psychologique.

## Catalogue raisonné et Twin

Le catalogue raisonné vise l'**œuvre au sens large** : objets, textes, images, vidéos, performances, interventions, engagements et autres productions lorsque les sources permettent de les documenter comme telles. Une trace de vie n'est pas automatiquement une œuvre ; une œuvre n'est pas automatiquement une preuve causale.

Le futur Twin documentaire de Marie-Louise doit être alimenté par les mêmes sources qualifiées. *Suicide Corse*, le catalogue raisonné et le Twin sont donc des **projections différentes d'un Corpus partagé**, et non trois bases concurrentes.

## Discipline épistémique

Le projet conserve explicitement les distinctions suivantes :

```text
trace
≠ fait établi
≠ parole directe
≠ témoignage
≠ assertion
≠ inférence
≠ hypothèse
≠ UNKNOWN
```

Règles invariantes :

- **Agency before outcome** : le suicide ouvre l'enquête ; il ne devient pas la clé rétroactive de toute la vie.
- **Unknown is part of the evidence** : un blanc documentaire ne doit pas être rempli narrativement.
- Une trace de vie n'est pas automatiquement une preuve causale.
- Une récurrence entre échelles n'est pas une identité de mécanisme.
- Toute fermeture candidate appelle une recherche symétrique des maintiens, contournements et réouvertures.
- Ne jamais fabriquer une parole, une volonté, une intention ou un consentement posthume de Marie-Louise.
- Les éditions gelées sont immuables ; les sources vivantes et les projections futures restent corrigibles.

## Organisation du répertoire

- [`architecture.md`](architecture.md) — architecture d'enquête v2 ;
- [`corpus.yml`](corpus.yml) — manifeste courant des sources et chantiers ;
- [`manuscript/`](manuscript/) — **espace historique et de travail éditorial**, pas table des matières canonique ;
- [`projections/`](projections/) — contrats de projection ;
- [`editions/`](editions/) — registre et déclarations des éditions gelées ;
- [`journals/`](journals/) — journaux de campagne ;
- [`handoffs/`](handoffs/) — paquets de reprise temporaires et traçables.

### À propos de `manuscript/`

Le répertoire contient désormais plusieurs sortes d'objets : chapitres d'édition, appel à témoignages, généalogie, annuaire, chronologie et questions ouvertes. Les deux préfixes `17-*` montrent à eux seuls que sa numérotation ne constitue plus une architecture canonique.

Aucun déplacement massif n'est effectué ici : des chemins sont déjà référencés par des éditions, issues et documents. Les futurs déplacements devront préserver les références ou être accompagnés d'une migration explicite. Pour une nouvelle édition, le contrat de projection — et non l'ordre lexical du répertoire — détermine le contenu.

## Projections

Le même Corpus peut alimenter, sans les confondre :

```text
Suicide Corse — éditions successives
catalogue raisonné de Marie-Louise
Twin documentaire de Marie-Louise
agent conversationnel
scénario
journaux de campagne
autres projections à venir
```

Une projection ne devient jamais automatiquement source de vérité pour les autres.

## Issues actives structurantes

- [#42](https://github.com/JeanHuguesRobert/barons-Mariani/issues/42) — chantier parent ;
- [#75](https://github.com/JeanHuguesRobert/barons-Mariani/issues/75) — édition anniversaire et gel ;
- [#80](https://github.com/JeanHuguesRobert/barons-Mariani/issues/80) — réception structurée des témoignages ;
- [#81](https://github.com/JeanHuguesRobert/barons-Mariani/issues/81) — chantier historique du n°2 désormais gelé ;
- [#84](https://github.com/JeanHuguesRobert/barons-Mariani/issues/84) — préparation active du n°3.

Les issues spécialisées historiques restent partie du Corpus lorsqu'elles portent des traces, décisions, objections ou Continuations, sans devenir pour autant des sources canoniques stabilisées.

## Principe de continuation

Une piste non traitée ne doit ni disparaître ni être artificiellement intégrée au prochain numéro. Elle devient une **Continuation explicite**, avec provenance, état et condition de reprise.

Ainsi :

```text
ne pas tout publier
≠ oublier
≠ fermer
```

Le projet reste volontairement incomplet, mais l'incomplétude doit être visible, traçable et exploitable.
