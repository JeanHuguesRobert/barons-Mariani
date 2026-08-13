---
title: "Generative Graphic Design Lineage — YanUg, Jana, Digipees"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
language: "en"
date: "2026-08-13"
last_modified_at: "2026-08-13"
status: "working-paper"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/generative_graphic_design_lineage.md"
last_stamped_at: unknown
document_role: "source"
document_kind: "research-note"
visibility: "public"
lifecycle_state: "working"
generated_by:
  - "Jean Hugues Noël Robert"
  - "GPT-5.6 Sol (research reconstruction, drafting and structuring)"
ai_assisted_by:
  - "GPT-5.6 Sol"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: unknown
  origin_date: "2026-08-13"
  derived_from: []
review:
  status: "unreviewed"
  reviewed_by: []
update_policy: "UP-DEFAULT-REVIEWED"
---

# Generative Graphic Design Lineage — YanUg, Jana, Digipees

This note records a historical progression in the graphical corpus associated with Jean Hugues Noël Robert and related projects.

It is intentionally a **provenance-oriented historical trace**, not a claim that every intermediate step was consciously conceived at the time as part of one unified theory.

The conceptual continuity described here is therefore partly retrospective:

> several independent graphic experiments progressively moved from fixed images toward structured, programmable and eventually AI-assisted spaces of possible forms.

## 1. From image to generative visual system

A useful summary of the progression is:

```text
image
  → structured vector
  → programmable / parametric form
  → parameterized family of forms
  → semantic visual grammar
  → AI-assisted generative exploration
```

The important shift is not only technological.

The **object of design** progressively moves:

```text
design one form
→ describe its structure
→ encode how it is produced
→ define how it may vary
→ define a coherent visual language
→ explore a space of possible forms
```

A compact working formula is:

> **Image → structure → function → generative space.**

---

## 2. YanUg — early visual symbol

**YanUg** is a smiling, sun-like symbol derived visually from a yin-yang structure.

The currently recovered historical material establishes that YanUg existed at least by early 2007.

### 2.1 Copyright trace — March 2007

A CopyrightDepot acknowledgement dated **30 March 2007** records a declaration made by Jean Hugues Robert under the title:

```text
YanUg Ying Yang Face
```

This is currently the strongest dated archival anchor recovered for the name and identity of the symbol.

The email is useful as historical evidence of the existence and naming of YanUg. It should not by itself be interpreted here as a legal conclusion about the current scope or enforceability of rights.

### 2.2 Historical SVG — May 2007

An email sent by Jean Hugues Robert to himself on **30 May 2007**, with subject:

```text
yanug.svg
```

contains the SVG attachment:

```text
yanug2.svg
```

This establishes that a vector representation of YanUg already existed in 2007.

The recovered source is now also locally available for coding agents as:

```text
Downloads/yanug2.svg
```

It should be preserved as an historical source before normalization or reconstruction.

### 2.3 Raster usage remained active — 2008

A later email, dated **27 June 2008**, publishes:

```text
The YanUg.
```

with an attached:

```text
yanug64.gif
```

Thus the transition to vector representation did not simply replace raster assets.

For some time, the same visual identity existed through several technological projections:

```text
YanUg concept
├── raster image
├── GIF
└── SVG
```

This already illustrates a recurring principle in the later corpus:

> the represented visual identity is distinct from any one of its renderings.

---

## 3. YanUg becomes programmable — 2010

An especially significant historical trace appears in a December 2010 discussion around **SimpliWiki**.

Jean Vincent suggested rebuilding YanUg using **Raphael**, with SVG/VML primitives, noting that the symbol could essentially be reduced to:

```text
3 circles
+ 2 paths
+ fills
```

and that this would also permit animation.

During the same discussion, Jean Hugues Robert stated that an older SVG version had been recovered and exposed at:

```text
simpliwiki.com/yanug.svg
```

Jean Vincent then produced a Raphael-based version and explicitly noted that its **design parameters could be controlled by modifying parameters at the beginning of the code**.

This is an important correction to a simpler initial reconstruction of the lineage:

> **the transition from logo-as-file to logo-as-program was already being explored in 2010.**

The relevant progression is therefore not:

```text
bitmap → SVG → Jana code
```

but rather:

```text
bitmap / GIF
→ SVG
→ programmable parametric YanUg
→ later, more explicit generators of design families
```

This distinction matters historically.

---

## 4. YanUg animation and continuing reuse

### 4.1 Web animation — attested again in 2017

In an email dated **21 May 2017**, Jean Hugues Robert described YanUg as:

- very geometric;
- constructible with only a few circles plus the smile;
- available through a Web animation.

The email states:

```text
Je ne l'ai plus en vectoriel, mais c'est très géométrique en fait,
on le construit avec seulement quelques cercles, plus le sourire.

J'ai une animation web : http://virteal.com/virteal/yanug.html
```

This confirms that YanUg had become not only vector/programmatic but also **kinetic**.

### 4.2 Graphic identity reuse — 2017–2022

YanUg continued to be reused as an emblem in later graphical contexts.

Examples recovered from email archives include:

- 2017 electoral material specifying `Logo Yanug` and an all-orange treatment;
- 2018 Institut Mariani graphic material specifying a version with **YanUg above the tower**;
- 2022 electoral material specifying YanUg explicitly as the **emblem**, in black or orange.

This longevity suggests that YanUg should be treated not merely as an obsolete historical logo but as a persistent element of the graphical corpus.

---

## 5. YanUg as code in later repositories

Later source code continues the same direction.

In:

```text
JeanHuguesRobert/serra/core/src/utils/YanUg.js
```

YanUg is represented procedurally through SVG geometry.

Older traces also exist in:

```text
JeanHuguesRobert/simpli/lib/yanug.png.js
```

The important observation is therefore:

```text
visual symbol
→ multiple rendered artifacts
→ explicit geometry
→ executable representation
```

YanUg is an early example, in this corpus, of a graphic object whose identity progressively migrates from a particular file toward a **generative description**.

---

## 6. Jana — from parametric form to explicit design space

The **Jana / FractaVolta logo generator** represents another step.

Its historical source is the standalone HTML generator:

```text
jana.html
```

originally published as a GitHub Gist and being retrofitted into:

```text
JeanHuguesRobert/FractaVolta/tools/jana-logo-generator/
```

Jana should not be described as the first time a logo became code: YanUg already provides evidence of that transition.

The qualitative difference is instead that Jana makes the **generation of variants itself a first-class design function**.

Its logic is closer to:

```text
visual grammar
+ constrained palette
+ parameters
→ multiple valid instances
```

rather than merely:

```text
code
→ reproduce one logo
```

Jana therefore marks a transition from:

```text
parametric form
→ parameterized design space
```

The designer increasingly specifies:

- invariants;
- allowed variation;
- palette;
- structure;
- composition rules;
- reproducible transformations.

The resulting logo is an **instance** of a constrained generative system.

---

## 7. Digipees — from graphical assets to visual language

The historical **d2lab Digipees** assets represent another qualitative step.

Two recovered historical SVG sources are currently available:

```text
digipees21-08-2006.svg
digipies02.svg
```

They are also locally available to coding agents as:

```text
Downloads/digipees21-08-2006.svg
Downloads/digipies02.svg
```

These source files should be preserved byte-for-byte before normalization.

The Digipees assets already contain more than characters.

They include a recurring graphical vocabulary for:

```text
persons
physical objects
information objects
signals
scenes
```

Examples include characters, computers, mobile devices, cameras, television, media objects, Wi-Fi and domestic scenes.

The current reconstruction therefore treats Digipees not merely as a collection of illustrations, but as evidence of an underlying **visual grammar**.

---

## 8. Static, semantic and kinetic grammar

The current Digipees preservation work aims to separate:

```text
historical canon
        ↓
normalized assets
        ↓
visual grammar
        ↓
semantic grammar
        ↓
kinetic grammar
        ↓
themes / community profiles
        ↓
generative scenes and media
```

### 8.1 Visual grammar

Observed recurring properties include:

- strong black external contour;
- thinner internal details;
- rounded masses and corners;
- highly simplified recognizable silhouettes;
- low visual texture;
- little or no realistic lighting;
- simplified perspective;
- explicit ground shadows for many embodied entities;
- labels associated with assets.

### 8.2 Identity delta

Historical Digipees characters appear to derive much of their individual identity from relatively small variations over a stable common morphology.

This suggests a useful working rule:

> **stable common base + small highly discriminating identity delta**

rather than a combinatorial character generator based on hundreds of unrelated interchangeable pieces.

### 8.3 Kinetic grammar

A remembered characteristic of the original animated Digipees is now treated as part of the historical kinetic canon:

```text
Digipee character
= slight levitation above ground
+ slow vertical oscillation
+ ground shadow below
+ shadow synchronized with character motion
```

Exact historical amplitude, period, easing, shadow scale or opacity variation remain unknown unless an original animation source is recovered.

They must therefore not yet be canonized from reconstruction alone.

---

## 9. From Digipees assets to Digipees Studio

The emerging target is not merely a character generator.

A future **Digipees Studio** may support:

```text
Character Factory
Object Factory
Scene Factory
Motion Engine
Story Engine
Renderer
Asset / provenance catalog
```

A graphical entity could increasingly be described semantically:

```yaml
entity:
  type: digipee
  identity: john
  morphology:
    age_expression: mature
    glasses: round
  motion:
    idle: levitate
  visual_profile: digipees-corsica
```

or:

```yaml
entity:
  type: object
  class: battery
  capacity: 5kWh
  visual_profile: client.example
```

The desired architecture becomes:

```text
semantic description
+ visual grammar
+ motion grammar
+ visual profile
+ state
→ rendered instance
```

The graphic asset becomes a projection of a richer entity description.

---

## 10. Digital Twins: representation is not the represented entity

This work intersects directly with the Cogentia / Fractanet Digital Twin architecture.

A Digital Twin is not its icon, SVG, avatar, photograph or animation.

Conceptually:

```text
represented entity
      ↓
Digital Twin
      ↓
projection
  ├── photograph
  ├── diagram
  ├── dashboard
  ├── Cogentigram
  ├── Digipees view
  └── client/community view
```

The same Digital Twin may therefore have several legitimate graphical projections.

This follows the broader map/territory discipline of the corpus:

> **the representation must remain distinguishable from what it represents.**

Digipees are particularly useful because their non-photoreal nature makes that representational status explicit.

A photograph tends toward a trace of physical appearance.

A Digipees rendering openly belongs to the domain of **representation**.

---

## 11. Semantic interoperability does not imply visual uniformity

The same semantic entity should be renderable through different visual identities.

For example:

```yaml
entity: battery:corte-01
kind: industrial-twin
state:
  soc: 72
  charging: true
```

may be rendered through:

```text
digipees-corsica
fractavolta
client.<name>
community.<name>
engineering
```

without changing the semantic identity of the battery.

This yields an important architectural invariant:

> **Semantic interoperability must not require visual uniformity.**

Or, in the wider language of the corpus:

> **Put in common what allows understanding; leave diverse the ways it is represented.**

Digipees can therefore serve as a generic/reference **Made-in-Corsica** visual language, while FractaVolta can support visual identities specific to clients, communities, projects or sub-networks.

---

## 12. Graphic Design as part of the FractaVolta offer

This progression also supports an explicit **Graphic Design** component in the FractaVolta offering.

It may include:

- visual identity;
- semantic iconography;
- Digital Twin projections;
- client visual profiles;
- community visual profiles;
- characters;
- objects;
- places;
- diagrams;
- motion grammar;
- animation;
- scenes;
- generative Web media;
- image and video production.

The distinguishing feature is that Graphic Design is connected to the semantic and operational model rather than applied only as decoration after implementation.

Conceptually:

```text
Digital Twin semantics
+ state
+ context
        ↓
Graphic Design projection layer
        ↓
Web / diagram / dashboard / image / animation / video
```

---

## 13. AI — from generator to Machine à Explorer

Generative AI introduces another qualitative step.

A future visual-production pipeline may combine:

```text
semantic intent
+ Digital Twin state
+ visual grammar
+ asset libraries
+ constraints
+ context
+ client/community profile
+ generative AI
+ human/agent review
→ coherent visual propositions
```

The designer is increasingly concerned not only with producing a final form but with defining and navigating the **space of possible forms**.

Creativity therefore moves partly toward:

- grammar design;
- conceptual modeling;
- constraints;
- invariants;
- parameter spaces;
- semantic mappings;
- mutation/generation rules;
- evaluation;
- selection;
- provenance;
- reproducibility.

This is not necessarily less creative.

It is a different level of creative activity.

---

## 14. Relation to the Machine à Explorer

The corpus distinguishes the **Machine à explorer** from the **Machine à empêcher**.

A generative graphic system can be understood as a specialized Machine à Explorer applied to visual forms:

```text
grammar
+ constraints
+ libraries
+ generators
+ AI
+ variation
+ comparison
+ selection
+ traceability
→ exploration of visual possibles
```

The corresponding anti-pattern would be a graphical pipeline that progressively closes the space of possibilities through:

- proprietary lock-in;
- opaque generation;
- non-reproducible assets;
- a single imposed visual representation;
- loss of source provenance;
- inability to fork, modify or reinterpret the grammar.

The relevant design principle becomes:

> **Stabilize enough to preserve meaning and provenance; generate enough diversity to explore.**

In that sense:

> **Generative Graphic Design is a specialized Machine à Explorer.**

And, in the vocabulary of the possibilist doctrine:

> **Generative Graphic Design is an Exploration Rationnelle et Joyeuse du Possible applied to forms.**

---

## 15. Historical sequence

The currently evidenced sequence is approximately:

```text
≤ 2007-03
YanUg exists as "YanUg Ying Yang Face"
        ↓
2007-05
historical YanUg SVG (`yanug2.svg`)
        ↓
2008
continued GIF/raster use
        ↓
2010
Raphael / programmable parametric YanUg
+ explicit modifiable design parameters
+ animation possibility
        ↓
2017
YanUg Web animation explicitly attested
+ continuing emblem/logo use
        ↓
2018–2022
continued reuse in Institut Mariani and electoral graphics
        ↓
2026
Jana parameterized logo-family generator
        ↓
2026
Digipees visual + semantic + kinetic grammar reconstruction
        ↓
2026 →
AI-assisted generative visual studio
```

The dates should continue to be refined if earlier source material is recovered.

The historical significance lies less in a claim of continuous intentional development than in the recurrence of a pattern:

```text
fixed representation
→ explicit structure
→ executable structure
→ variable structure
→ visual grammar
→ Machine à Explorer
```

---

## 16. Provenance status

### Strongly evidenced historical anchors

Current primary or near-primary evidence includes:

- **2007-03-30** — CopyrightDepot email naming `YanUg Ying Yang Face`;
- **2007-05-30** — email carrying `yanug2.svg`;
- **2008-06-27** — email carrying `yanug64.gif`;
- **2010-12-22** — SimpliWiki/Facebook-notification discussion concerning SVG/VML, Raphael, animation and modifiable design parameters;
- **2017-05-21** — campaign-design email describing YanUg geometry and a Web animation;
- **2018-06-22** — Institut Mariani graphic instruction using YanUg;
- **2022-05-21** — electoral graphic specification explicitly using YanUg as emblem;
- **2006 Digipees SVG sources** recovered in 2018 from Jean-François Catz;
- **2026 Jana Gist** and FractaVolta generator sources.

### Historical interpretation

The following is a retrospective interpretation rather than a claim about original intent:

> these artifacts form a lineage from fixed graphic objects toward programmable and increasingly generative visual systems.

That interpretation is useful precisely because the historical artifacts themselves predate the current conceptual vocabulary.

---

## 17. Source preservation rule

Historical sources should remain distinct from normalized or derived assets.

Conceptually:

```text
historical source
        ↓
preservation
        ↓
normalization
        ↓
semantic / graphic model
        ↓
derived themes
        ↓
generative production
```

Never overwrite a historical source merely because a cleaner or more modern representation exists.

Examples:

```text
yanug2.svg
≠ normalized YanUg SVG
≠ procedural YanUg implementation
≠ themed YanUg instance
```

and:

```text
historical Digipees SVG
≠ extracted character SVG
≠ normalized character grammar
≠ generated Digipee
```

---

## 18. Related work

### Barons Mariani

- `barons-Mariani/hosted/digipees/`
- `barons-Mariani` issue #33 — Digipees visual grammar
- `barons-Mariani` issue #34 — Digipees provenance, licensing and naming
- this historical trace

### FractaVolta

- `FractaVolta/tools/jana-logo-generator/`
- `FractaVolta` issue #21 — Jana retrofit
- `FractaVolta` issue #22 — configurable visual profiles / Graphic Design offering

### Cogentia

- `cogentia` issue #98 — cognitive and industrial Digital Twin projections
- `cogentia/research/concepts.md` — Machine à explorer / Machine à empêcher
- Digital Twin / Cogentigram / map-territory doctrine

### Historical code

- `JeanHuguesRobert/serra/core/src/utils/YanUg.js`
- `JeanHuguesRobert/simpli/lib/yanug.png.js`

### Historical source files currently recovered locally

```text
Downloads/yanug2.svg
Downloads/digipees21-08-2006.svg
Downloads/digipies02.svg
```

These local paths are operational hints for coding agents, not durable provenance identifiers.

---

## 19. Working formulas

### Technical evolution

> **Image → structure → function → generative space.**

### Design evolution

> **Designing a form → designing the rules that make coherent forms possible.**

### Machine à Explorer

> **A generative studio is a Machine à Explorer applied to an aesthetic and semantic possibility space.**

### Possibilist reading

> **Generative Graphic Design is an Exploration Rationnelle et Joyeuse du Possible applied to forms.**

### Digital Twin discipline

> **The Twin is not its image; the image is not reality; a good projection makes the Twin intelligible without pretending to be the represented reality.**
