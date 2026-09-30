---
title: "Rise & Fall of the Mariani Family — projet de recherche et d'enquête"
description: "Point d'entrée canonique du projet Rise & Fall of the Mariani Family : méthodologie en deux passes, enquête capacitaire, projections et premier Reality Case 1863."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-30"
last_modified_at: "2026-09-30"
version: "0.1"
status: "working-paper"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "project-readme"
document_kind: "readme"
visibility: "public"
lifecycle_state: "working"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/rise-and-fall/README.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "issue-continuation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "GitHub issue #94"
  origin_date: "2026-09-29"
  derived_from:
    - "projects/suicide-corse/architecture.md"
    - "projects/suicide-corse/editorial-architecture.md"
    - "projects/suicide-corse/corpus.yml"
    - "research/protestation_electorale_1863_mariani_gavini.md"
    - "musee-mariani/README.md"
    - "musee-mariani/personnes/README.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Rise & Fall of the Mariani Family

**Sous-titre de travail : *Reconstitution régressive et prospective des bifurcations de capacité d'une famille corse (1776–2026)***

Projet de recherche académique, documentaire et muséal rattaché au **Musée Mariani des Possibles** et à l'**Institut Mariani** (Corte, Corse).

---

## 1. Objet et hypothèse d'enquête

Le projet *Rise & Fall of the Mariani Family* prend pour objet la trajectoire historique, patrimoniale, politique, juridique et territoriale de la famille des barons Mariani depuis le Premier Empire jusqu'à nos jours.

L'investigation est guidée par une hypothèse centrale de recherche :

> **Dans quelle mesure, par quels mécanismes institutionnels précis, et avec quels contrefactuels plausibles l'État français et ses émanations ont-ils contribué à la perte progressive de capacité économique, patrimoniale, juridique, sociale ou intergénérationnelle de la famille Mariani ?**

### Règle épistémique fondamentale
Cette proposition est une **hypothèse de travail à éprouver, non une conclusion préjugée ni une accusation globale**.

L'enquête a pour devoir explicite de tester symétriquement l'hypothèse nulle et les explications concurrentes :
- mutation économique générale et déclin des rentes foncières ;
- effets du droit commun successoral républicain (Code civil de 1804 et partage égalitaire) ;
- arbitrages et décisions privées familiales (conflits d'indivision, dépenses, investissements, choix de carrières) ;
- dispersion géographique et mobilités hors de Corse ;
- contingences, démographie et aléas historiques.

Le projet n'a de valeur que par sa capacité à discriminer, affaiblir, requalifier ou rejeter les responsabilités alléguées.

---

## 2. Méthodologie en deux passes

Le projet applique une discipline méthodologique rigoureuse en deux mouvements complémentaires :

```text
PASS A : Archéologie régressive
État présent (contraintes, pertes observées, verrous capacitaires)
  → cause immédiate documentée
  → décision ou acte juridique antérieur
  → bifurcation préalable
  → état antérieur documenté...

PASS B : Reconstitution prospective des Possibles
État initial documenté à t0
  → capacités effectives et possibles ouverts
  → événement / mécanisme (public ou privé)
  → possibles fermés ou dégradés
  → capacités résiduelles
  → bifurcation suivante (t1, t2... tn)
```

La confrontation des deux passes permet de vérifier si l'histoire causale apparente reconstruite à rebours survit à la chronologie directe sans anachronisme ni déterminisme rétrospectif.

---

## 3. Invariants éditoriaux (héritage de Suicide Corse)

Le projet réutilise les invariants stabilisés dans [*Suicide Corse*](../suicide-corse/editorial-architecture.md) sans en dupliquer aveuglément les contenus spécifiques :

1. **La tripartition fonctionnelle :**
   > *« Le corps principal raconte ; le Magazine actualise ; les annexes démontrent. »*
   - **Livre** : Récit intelligible au long cours, structuré par la méthode en deux passes.
   - **Magazine** : Journal d'enquête périodique accueillant les deltas, découvertes d'archives et réponses du Réel.
   - **Annexes / Corpus** : Dossiers de preuves exhaustifs, transcriptions d'actes, relevés cadastraux et généalogie critique.
2. **L'asymétrie fond/forme :**
   > *« Continuité épistémique ; liberté esthétique. »*  
   Le fond conserve obligatoirement la mémoire de ses états et corrections ; chaque nouvelle édition jouit d'une totale liberté formelle et typographique.
3. **Le régime des éditions immuables :**  
   Une édition publiée est gelée de façon irréversible (`freeze`). Toute correction ultérieure appartient au Corpus vivant et à la projection suivante.
4. **Le delta sémantique :**  
   Application de la doctrine de l'[Issue #93](../issues/93) permettant à tout lecteur d'une édition passée de consulter gratuitement le différentiel d'avancement de l'enquête.

---

## 4. Premier Reality Case pilote

Le modèle est amorcé et testé de bout en bout sur un cas historique à forte densité documentaire primaire :

- **Reality Case RC-01 :** [*L'élection de 1863 — Louis-Thomas Mariani contre Sampiero Gavini*](investigation/reality_cases/RC-01-1863-gavini.md).
- **Enseignement épistémique majeur :** En 1863, le baron Mariani est le *candidat officiel du Gouvernement impérial* battu par un bonapartiste non officiel au terme d'une lutte de factions locales et d'allégations de fraudes de terrain. Ce cas interdit tout récit simpliste d'une hostilité continue de l'État et force à analyser le jeu complexe entre pouvoir central, administration préfectorale et notabilités locales.

---

## 5. Organisation du projet

```text
projects/rise-and-fall/
├── README.md                 # Le présent point d'entrée
├── corpus.yml                # Manifeste de projet, sources et règles
├── architecture.md           # Architecture d'enquête, grammaire capacitaire, causalité
├── editorial-architecture.md # Architecture éditoriale, tripartition, protocole de gel
├── schemas/                  # Schémas machine-readable (bifurcations, causalité)
├── chronology/               # Master timeline critique intégrée
├── investigation/            # Dossiers d'enquête, passes A/B et Reality Cases
├── manuscript/               # Manuscrit éditorial (Livre, Magazine, Annexes)
├── sources/                  # Bibliographie critique, inventaire des actes primaires
├── projections/              # Contrats de projection Quarto / Ubikia
└── editions/                 # Registre des éditions gelées et déclarations de freeze
```

---

## 6. Règle de non-dispersion et périmètre

Conformément à la règle d'Occam du Corpus :
- Le projet est logé au sein de `JeanHuguesRobert/barons-Mariani` pour bénéficier de l'accès direct aux sources patrimoniales et généalogiques existantes.
- La création d'un dépôt séparé ou la réservation d'infrastructures DNS externes (`riseandfall.baronsmariani.org`) ne sera mise en œuvre que si l'autonomie éditoriale et le volume de diffusion le justifient, après accord explicite.
