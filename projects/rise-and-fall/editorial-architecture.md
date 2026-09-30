---
title: "Rise & Fall of the Mariani Family — Architecture éditoriale"
subtitle: "Publication continue, éditions immuables, asymétrie fond/forme et triptyque éditorial"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-30"
last_modified_at: "2026-09-30"
version: "0.1"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "editorial-architecture"
document_kind: "working-note"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/editorial-architecture.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "GitHub issue #94"
  origin_date: "2026-09-29"
  derived_from:
    - "projects/suicide-corse/editorial-architecture.md"
    - "projects/suicide-corse/architecture.md"
    - "GitHub issue #93"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Rise & Fall of the Mariani Family — Architecture éditoriale

## 0. Objet

Cette note fixe l'**architecture éditoriale** du projet *Rise & Fall of the Mariani Family*.

Elle gouverne la chaîne de publication, le cycle de vie des éditions, la relation entre le Corpus vivant et ses projections figées, ainsi que les règles de rendu numérique et physique.

Elle applique les invariants éprouvés dans [*Suicide Corse*](../suicide-corse/editorial-architecture.md) en les adaptant à une enquête académique et archivistique au long cours.

---

## 1. Publication continue à éditions figées

Le projet n'est pas un livre statique à parution unique, ni un fil continu sans mémoire. C'est un **Corpus d'enquête vivant** produisant périodiquement des **éditions gelées et vérifiables**.

```text
Traces primaires / archives / actes notariés / contributions
  │
  ▼
Qualification critique et intégration au Corpus vivant
  │
  ▼
Intention éditoriale et sélection
  │
  ▼
Projection candidate (Livre / Magazine / Annexes)
  │
  ▼
Contrôles de couverture, Delta Review et revue adverse
  │
  ▼
FREEZE (déclaration datée, commit source scellé, empreintes SHA-256)
  │
  ▼
Édition immuable (HTML, PDF, EPUB, tirage papier éventuel)
  │
  ▼
Réponses du Réel / découvertes ultérieures
  │
  ▼
Retour au Corpus vivant sans réécriture de l'édition gelée
```

Règle absolue héritée :

> **Freeze the edition, never the next projection.**

Une édition ancienne demeure un témoin historique de ce qui était alors établi ; les corrections ultérieures figurent dans le Corpus courant et l'édition suivante.

---

## 2. Le principe d'asymétrie éditoriale

Le principe structurant est asymétrique :

> **Le contenu nouveau est contraint par l'histoire du contenu ; la forme nouvelle n'est pas contrainte par l'histoire des formes.**

### 2.1. Continuité épistémique du fond
Toute modification du savoir (correction d'une date, découverte d'un acte contredisant une généalogie, requalification d'un mécanisme) doit rester traçable. On ne fait jamais disparaître silencieusement une erreur passée : la correction est un contenu de premier ordre.

### 2.2. Liberté esthétique de la forme
Chaque projection éditoriale ou numéro peut réinventer sa maquette, sa typographie, son genre visuel ou son découpage en fonction du public visé (dossier académique, exposition muséale, atlas patrimonial, livre grand public).

Formule de compression :

> **Continuité épistémique ; liberté esthétique.**

---

## 3. Le triptyque fonctionnel : Livre, Magazine, Annexes

Le projet adopte la tripartition fonctionnelle :

> **Le corps principal raconte ; le Magazine actualise ; les annexes démontrent.**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                                 LIVRE                                  │
│   Connaissance durable, mouvement de fond, intelligibilité narrative   │
│   (Pass A régressive et Pass B prospective des possibles)             │
├────────────────────────────────────────────────────────────────────────┤
│                               MAGAZINE                                 │
│   Delta depuis l'édition précédente, actualité de l'enquête,           │
│   découvertes d'archives récentes, réponses des institutions           │
├────────────────────────────────────────────────────────────────────────┤
│                            ANNEXES / CORPUS                            │
│   Preuves exhaustives, cotes d'archives, transcriptions intégrales,    │
│   registres cadastraux, calculs d'imposition, généalogie probatoire    │
└────────────────────────────────────────────────────────────────────────┘
```

### Rubriques récurrentes du Magazine
Pour assurer la continuité des éditions, le Magazine s'appuie sur six rubriques modulaires :
1. **Le Réel répond :** Réponses des administrations, services d'archives, mairies ou contradicteurs.
2. **Nouvelles traces :** Actes d'état civil, minutes notariales, plans ou correspondances récemment découverts.
3. **Le point de l'enquête :** Évolution des statuts épistémiques (`ESTABLISHED`, `HYPOTHESIS`, `UNKNOWN`).
4. **Reality Case :** Examen approfondi et borné d'un cas ou d'une transaction historique précise.
5. **Contrepoints :** Objections méthodologiques, hypothèses alternatives et preuves résistantes.
6. **Continuations :** Chantiers d'archives en cours, pistes ouvertes et conditions de reprise.

---

## 4. Doctrine du delta sémantique (Application de l'Issue #93)

Chaque édition physique ou numérique collector reste reliée au présent grâce au **moteur de delta sémantique** :

```text
Édition N (gelée) ───[ Identifiant d'édition / QR / URL ]───► Page « Depuis ce numéro »
                                                                      │
                                                                      ▼
                                                      Delta sémantique (N → today)
                                                      - Éléments ajoutés
                                                      - Faits corrigés
                                                      - Hypothèses contredites
                                                      - Questions résolues
```

Le lecteur d'un tirage papier conserve un objet historique scellé sans être coupé de l'avancement de la recherche. Le delta s'exprime en catégories épistémiques compréhensibles, jamais en simple `git diff`.

---

## 5. Cadence éditoriale

Contrairement à *Suicide Corse* qui a expérimenté une cadence hebdomadaire réactive liée à une campagne, *Rise & Fall* est une **enquête documentaire au long cours**.

Sa cadence repose sur deux régimes :
1. **Éditions pivots (rythme structuré) :** Jalons saisonniers ou annuels (ex. jalon patrimonial de printemps, jalon anniversaire d'automne).
2. **Éditions déclenchées par le contenu (rythme agile) :** Publication d'une édition exceptionnelle lorsqu'un dépouillement substantiel ou une découverte d'archive transforme la compréhension d'une période (ex. accès aux minutes notariales du don de 1924, ou redécouverte du rapport parlementaire de 1863).

---

## 6. Pipeline de rendu Quarto / Ubikia

Les manuscrits sources sont rédigés en Markdown enrichi avec frontmatter YAML.

Le pipeline technique est délégué à [`JeanHuguesRobert/ubikia`](https://github.com/JeanHuguesRobert/ubikia) et Quarto :
- Compilation en un passage vers les formats requis : **HTML** (web / consultation interactive), **PDF** (mise en page livre / lecture posée), et **EPUB** (liseuses).
- Génération automatique du manifeste technique scellé (`manifest.json`) consignant le commit Git source, les empreintes SHA-256 de chaque chapitre et la version du compilateur.
