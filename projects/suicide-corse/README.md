---
title: "Suicide Corse — projet éditorial réactif"
description: "Point d'entrée canonique du projet Suicide Corse et de ses projections éditoriales."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A."
date: "2026-09-07"
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
  origin_ref: "unknown"
  origin_date: "2026-09-07"
  derived_from:
    - "GitHub issue #42"
    - "GitHub issue #43"
    - "memory/marie-louise/carte.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Suicide Corse

**Titre de travail : _Suicide Corse, ou comment réaliser l'impossible_.**

Ce répertoire matérialise le projet éditorial comme une **projection réactive du Corpus**, et non comme une nouvelle source autonome de vérité.

## Objet hybride et chaîne de projections

*Suicide Corse* est un objet éditorial hybride.

- Il est un **livre** : une édition narrative produite par ordinateur à partir d’un corpus de sources, de règles de projection et de traces qualifiées.
- Il est aussi un **magazine d’enquête** : son *Journal de campagne contre l’impossible* a vocation à paraître selon une cadence hebdomadaire, pour signaler les changements depuis l’édition précédente — nouvelles traces, témoignages, contradictions, corrections, hypothèses abandonnées ou pistes ouvertes.

Le journal hebdomadaire est un contrat de projection en préparation, non une publication déjà tenue. Sa première livraison reste à produire.

Les chapitres présents dans `manuscript/` constituent déjà une projection de recherche : ils sélectionnent, organisent et rendent lisibles les traces et documents bruts du Corpus. Ils ne sont ni les sources elles-mêmes, ni la dernière forme du projet. Lors de l’édition proprement dite, ils seront à leur tour traités par une pipeline de production distincte, avec ses propres règles de sélection, de mise en forme, de rendu et de provenance.

```text
traces et sources brutes du Corpus
→ projection de recherche : chapitres actuels
→ pipeline éditorial distinct
→ édition proprement dite : livre / magazine / formats rendus
```

La génération informatique ne délègue pas le jugement à la machine : elle rend reproductible la projection du Corpus. Les sources, leur niveau de preuve, les décisions éditoriales et les révisions restent explicitement traçables et humainement imputables. Une nouvelle trace peut corriger le Corpus, le Corpus corriger les chapitres, et les chapitres être recomposés dans une édition ultérieure.

Le mouvement général est :

```text
Corpus canonique
→ carte / sélection des sources
→ projection éditoriale
→ publication / interaction / Act
→ réponse du Réel
→ nouvelles traces
→ correction du Corpus
→ nouvelle projection
```

## Principe documentaire

Le livre ne doit pas effacer la distinction entre :

- trace ;
- fait suffisamment documenté ;
- témoignage tiers ;
- assertion ;
- interprétation ;
- reconstruction ;
- hypothèse ;
- inconnu.

Concernant Marie-Louise, la source de synthèse actuelle est [`memory/marie-louise/carte.md`](../../memory/marie-louise/carte.md). Elle reste distincte du manuscrit.

## Structure

- [`architecture.md`](architecture.md) — architecture d'enquête v2, invariants multi-échelle et continuations ;
- [`corpus.yml`](corpus.yml) — manifeste des sources canoniques et chantiers reliés ;
- [`manuscript/`](manuscript/) — projection narrative minimale de l'édition n°0 ;
- [`projections/book.yml`](projections/book.yml) — contrat minimal de projection livre ;
- [`projections/journal-weekly.yml`](projections/journal-weekly.yml) — placeholder gouverné du journal ;
- [`projections/screenplay.yml`](projections/screenplay.yml) — placeholder de projection scénario ;
- [`projections/conversational-agent.yml`](projections/conversational-agent.yml) — placeholder de l'agent conversationnel ;
- [`editions/index.md`](editions/index.md) — registre des éditions figées ;
- [`journals/README.md`](journals/README.md) — emplacement des journaux de campagne.

## Correction de doctrine — le bootstrap est révisable comme le reste, 15 septembre 2026

Une formulation antérieure de ce README présentait la modification de `manuscript/00-ouverture.md` comme une « exception » à un principe de non-réécriture du bootstrap. Cette présentation était elle-même une erreur de doctrine, corrigée ici.

Ni la seconde méthode (`research/agile.md`) ni l'Optimistic Locking (`cogentia/instructions/AGENTS.shared.md`, *Delivery policy*) ne fondent un régime de protection spéciale pour les cinq fichiers bootstrap. L'Optimistic Locking prescrit l'inverse d'une bureaucratie d'exception : des commits directs et atomiques sur la branche canonique, sans branche, geste d'approbation ni cérémonie de révision pour un travail borné et de risque mesuré ; une branche ou un geste de protection doivent se justifier par un bénéfice concret, jamais par une prudence générique ou un état d'âme. Le statut « artefact historique » des fichiers 00-04 décrit leur origine et leur ancienneté relative dans le Corpus ; il ne leur confère aucune immunité éditoriale. Réviser `00-ouverture.md` quand une lecture du Corpus ou une instruction de l'issue le justifie n'est donc pas une entorse ponctuelle à documenter comme telle : c'est le fonctionnement normal du Corpus. Seule reste nécessaire — et elle l'est pour tout fichier, bootstrap ou non — la traçabilité ordinaire : provenance mise à jour, historique git, pas de réécriture silencieuse qui dissimulerait ce qui a changé.

## Édition n°0 — bootstrap historique

Les cinq fichiers actuels constituent l'**édition bootstrap historique** : ce nom décrit leur ancienneté et leur fonction d'origine, pas un statut protégé. Ils ne définissaient déjà plus, avant même la correction de doctrine ci-dessus, l'architecture canonique de long terme — cela ne les rendait pas non plus intouchables, seulement moins structurants pour la suite. Leur but premier était d'exercer la chaîne complète :

```text
sources
→ sélection
→ manuscrit
→ projection
→ HTML / PDF
→ manifeste de provenance
```

Elle est structurée en cinq fichiers : ouverture, Marie-Louise, fermeture des possibles, Machine à Empêcher, réalisation de l'impossible.

## Chapitres additionnels — édition anniversaire du 17 septembre 2026 (#75)

Quatre chapitres supplémentaires, rédigés pour le contrat minimal de l'édition anniversaire (issue #75), complètent le manuscrit sans renuméroter ni réécrire les cinq fichiers bootstrap :

- [`05-machine-a-rendre-capable-de-vivre.md`](manuscript/05-machine-a-rendre-capable-de-vivre.md) — hypothèse-limite Machine à Empêcher de Vivre / Machine à Rendre Capable de Vivre ;
- [`06-vivre-transmettre.md`](manuscript/06-vivre-transmettre.md) — changement d'échelle vivre → se projeter → transmettre, fécondité et projection intergénérationnelle ;
- [`07-corse-capacite-dormante.md`](manuscript/07-corse-capacite-dormante.md) — fatalisme, capacité dormante, seuil et réactivation, réactance et révolte, histoire longue corse, source antique sur les esclaves corses ;
- [`08-hypotheses-non-resolues.md`](manuscript/08-hypotheses-non-resolues.md) — liste visible des hypothèses non résolues et gate épistémique de l'édition.

Ces chapitres restent `status: draft`, non revus, et doivent encore recevoir une revue contradictoire avant toute clôture d'édition.

Un cinquième chapitre a été ajouté après coup, en cours de rédaction, et non prévu par le sommaire initial de l'issue #75 :

- [`09-test-invariance-echelle.md`](manuscript/09-test-invariance-echelle.md) — première instanciation du test d'invariance capacitaire (`architecture.md`, §14) à partir de cas effectivement documentés dans `memory/marie-louise/possible_matrix.md`, mis en regard de matériau territorial corse.

Cet ajout illustre volontairement la doctrine de [`research/agile.md`](../../research/agile.md) : le sommaire d'une édition est révisable par le Corpus lui-même en cours de rédaction, plutôt que déroulé jusqu'au bout indépendamment de ce que la relecture des sources fait apparaître. Les chapitres 5 et 7 ont été légèrement amendés en conséquence, avec renvoi explicite vers ce nouveau chapitre.

Un sixième chapitre poursuit la même recherche d'invariants dans le matériau territorial contemporain :

- [`10-stabilisateur-et-capacite-distribuee.md`](manuscript/10-stabilisateur-et-capacite-distribuee.md) — introduit la fonction de Stabilisateur procédural (absente des chapitres 3-4), rapproche le test territorial `Follow the Power` de l'écart entre statut électoral formel et influence effective de Marie-Louise, et relie la règle du petit Act borné (chapitre 4) à son instanciation concrète `#1755-01`.

Le chapitre 8 (hypothèses non résolues) a été mis à jour en conséquence.

Un septième chapitre rapproche un mécanisme institutionnel déjà nommé dans le Corpus territorial d'un épisode précis du dossier Marie-Louise :

- [`11-impunite-par-obscurite.md`](manuscript/11-impunite-par-obscurite.md) — met en regard `research/autonomia/impunite_par_obscurite_cas_corse.md` (dilution des responsabilités, fonds européens, agences et offices de Corse) et le rejet procédural du 27 septembre 2024 de la requête électorale 2024-6309 AN, comme deux instances d'un même mécanisme sans auteur unique, en marquant explicitement que ce rejet est postérieur au décès et ne doit jamais entrer dans une reconstruction causale de l'été 2024.

Un huitième chapitre assume une méthode différente : la lecture flottante, non dirigée par une hypothèse préalable.

- [`12-carnet-de-serendipite.md`](manuscript/12-carnet-de-serendipite.md) — consigne deux trouvailles non cherchées : un cas d’écart entre information publiée et information effectivement accessible, issu de `research/opheline_ophelia_pertitellu_genesis.md`, et l’apport de `research/bien_vivre.md` comme définition positive manquante aux chapitres 5 et 6.

## Épigraphes en proverbes corses (issue #75, commentaires du 15 septembre 2026)

Six proverbes corses sourcés sont désormais employés comme épigraphes dans les chapitres 6, 7, 9, 10 et 12, avec un septième réservé à la clôture (chapitre 12, haute sensibilité, encadré explicitement) :

- [`13-proverbes-epigraphes.md`](manuscript/13-proverbes-epigraphes.md) — appareil de sourcing complet (forme corse, traduction, équivalent, source, fonction, niveau de sensibilité), trace du trio structurel prioritaire (Empêcher / Résister / Explorer), et liste explicite des proverbes volontairement non retenus pour cette édition, dont les trois proverbes sur la mort classés à haute sensibilité par l'issue elle-même et non employés faute de revue éditoriale explicite.

La clôture du chapitre 12 (proverbe à haute sensibilité *A risa di l'addulurati hè a più bella*) a été renforcée : elle n'appuie plus sur ce seul proverbe, mais sur trois registres indépendants et non concertés — proverbial corse, doctrine possibiliste déjà stabilisée dans le Corpus (`research/le_reel_le_virtuel_et_l_actuel.md`, §9.5 et §14.7, qui répond déjà à l'objection « injonction cruelle »), et tradition chrétienne (Béatitudes, 2 Corinthiens 6, 10 — introduite ici pour la première fois, sans généalogie antérieure dans le Corpus). Objectif explicite : neutraliser toute lecture d'insensibilité par convergence de sources indépendantes plutôt que par un argument unique.

## Texte intégral d'une œuvre source — 17 septembre 2026

- [`14-le-dieu-de-leau-texte-integral.md`](manuscript/14-le-dieu-de-leau-texte-integral.md) — reproduit intégralement, pour la première fois dans le manuscrit lui-même (et non seulement comme source liée), *Le dieu de l'eau* (2008) et le mail original par lequel Marie-Louise l'a transmis à son père. Publication déjà autorisée le 8 septembre 2026 (`memory/marie-louise/works/le_dieu_de_leau_2008.md`). Le chapitre 01 (bootstrap) ne faisait jusqu'ici que mentionner cette œuvre sans la reproduire.

## Réconciliation avec les apports parallèles du Corpus — 16-17 septembre 2026

Deux apports arrivés sur `main` pendant la rédaction ont été absorbés sans réécriture des chapitres 00-04 :

- [`memory/marie-louise/2024_portes_et_controles_epistemiques.md`](../../memory/marie-louise/2024_portes_et_controles_epistemiques.md) (issue #75, commentaire du 2026-09-16T04:48:28Z) — règle anti-certitude, contradiction Nantes 2017 (hypothèse père vs hypothèse Ferdinand Pancrazi), portes candidates non stabilisées de l'été 2024 (parrain, Villa Arson, paiement de chantier), agence encore exercée début 2024, et la variable candidate de **fiabilité perçue d'un possible**. Répercuté dans le chapitre 5 (nouvelle section) et le chapitre 8 (nouvelles entrées).
- `research/triangulation_du_reel.md` §4.1 (parcimonie causale, rasoir de Hanlon, échelle d'escalade vers l'intention) — répercuté dans l'ouverture (00), pour étayer formellement pourquoi la Machine à Empêcher n'y devient jamais une mise en cause personnelle, et dans le chapitre 8.

## Architecture d'enquête v2

L'architecture courante est décrite dans [`architecture.md`](architecture.md). Elle privilégie :

```text
Reality Case
→ distinction
→ invariant candidat
→ changement d'échelle
→ test du non-invariant
→ mécanisme
→ Act
→ Réel
→ trace
→ correction
```

Elle traite Marie-Louise comme personne et ensemble de traces, Reality Case longitudinal et cas possible d'enquête causale — trois régimes à ne pas confondre. La matière territoriale corse doit être intégrée progressivement comme changement de zoom, en recherchant les invariants sans transférer abusivement les propriétés propres à une échelle.

### Continuations immédiates

- [ ] produire un document source court sur la **grammaire capacitaire multi-échelle et le test d'invariance** ;
- [ ] spécifier le **Reality Case Marie-Louise v2**, incluant un blind review contre le biais rétrospectif ;
- [ ] produire une première projection **« Avant de connaître la fin »**, destinée à remplacer progressivement l'actuel chapitre 01 sans effacer le bootstrap historique.

Ces continuations sont enregistrées mais **non exécutées** à ce stade.

## Règle Marie-Louise

Ne jamais fabriquer une parole, une volonté ou un consentement posthume de Marie-Louise. Les formulations interprétatives ou causales doivent rester explicitement qualifiées comme telles.

## Issues

- #42 — chantier parent ;
- #43 — bootstrap canonique et édition 0 ;
- #44 — snapshot hebdomadaire et Journal de campagne ;
- #45 — traces Marie-Louise 2008/2016 ;
- #47 — Machine à Empêcher et causalité ;
- #48 — Twin documentaire Marie-Louise ;
- #49 — scénario ;
- #50 — agent conversationnel ;
- #51 — Reactive Publication ;
- #52 — continuité de protection.

Dépendance générique de rendu : `JeanHuguesRobert/ubikia#24`.


## Suspension temporaire — 9 septembre 2026

Le chantier est volontairement suspendu à ce point afin de revenir au dossier de candidature sénatoriale.

Point de reprise :

- architecture courante : [`architecture.md`](architecture.md) ;
- trois continuations immédiates déjà enregistrées dans cette architecture et dans le présent README ;
- aucune de ces continuations n'est réputée exécutée ;
- les cinq fichiers de `manuscript/` restent les artefacts historiques de l'édition bootstrap, révisables comme tout autre fichier du Corpus si le travail en cours le justifie (voir la correction de doctrine ci-dessus).

La reprise doit donc partir de l'architecture v2 et non restaurer implicitement l'ancien plan bootstrap.
