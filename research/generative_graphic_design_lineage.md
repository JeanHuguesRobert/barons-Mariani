---
title: "Generative Graphic Design Lineage — YanUg, Jana, Digipees"
date: 2026-08-13
status: working
visibility: public
document_role: historical-trace
document_kind: research-note
---

# Generative Graphic Design Lineage — YanUg, Jana, Digipees

This note records a historical progression in the graphical corpus associated with Jean Hugues Noël Robert and related projects. It is a provenance-oriented trace, not a claim that every intermediate step was consciously designed as part of one theory at the time.

## 1. From fixed image to generative visual system

A useful summary of the progression is:

```text
image
  → structured vector
  → parametric code
  → generative visual system assisted by AI
```

The important shift is not only technological. The object of design progressively moves from a single produced form toward the rules, parameters, grammars and exploration processes that can produce families of coherent forms.

## 2. YanUg — fixed graphic, then parametric vector form

YanUg is a sun-like / yin-yang-derived smiling symbol designed roughly two decades ago. Early surviving uses include raster forms.

A later implementation in `JeanHuguesRobert/serra` defines YanUg procedurally as SVG in `core/src/utils/YanUg.js`: the symbol is generated from geometric primitives and a radius parameter rather than stored only as a fixed bitmap.

This provides an early transition:

```text
logo as image
→ logo as explicit geometry
→ logo as a function
```

Historical traces also exist in older code such as `JeanHuguesRobert/simpli/lib/yanug.png.js`.

The orange/white YanUg image remains an historical visual source and should be preserved independently of later reconstructions or parameterized versions.

## 3. Jana — the logo becomes a generator of variants

The Jana / FractaVolta logo generator goes further. The source is not merely code capable of reproducing one fixed logo: it generates multiple variants from a constrained visual grammar and palette.

The historical Gist `jana.html` is being retrofitted into:

```text
JeanHuguesRobert/FractaVolta/tools/jana-logo-generator/
```

Jana therefore marks a further shift:

```text
form as function
→ family of forms as parameterized design space
```

The design work increasingly consists in specifying invariants, allowed variation and reproducible transformations.

## 4. Digipees — from assets to a generative visual language

The historical d2lab Digipees assets already contain more than characters: people, devices, information objects, signals and scenes share a recognizable graphic language.

The current preservation and analysis work aims to separate:

```text
historical canon
→ normalized assets
→ visual grammar
→ kinetic grammar
→ semantic asset libraries
→ themes / community visual profiles
→ generative scenes and media
```

The target is therefore not merely a character generator. It is a possible **Digipees Studio** capable of generating coherent characters, objects, scenes, animations, diagrams and derived media.

## 5. AI — design moves toward exploration of a space of possibilities

Generative AI introduces another qualitative step. A future visual production pipeline may combine:

```text
semantic intent
+ Digital Twin state
+ visual grammar
+ asset libraries
+ constraints
+ community/client profile
+ generative AI
+ human/agent selection and review
→ coherent visual projections
```

The designer is no longer concerned only with producing one final form. Design increasingly includes the conception of the **space of possible forms** and of the machinery used to explore that space.

This does not imply less creativity. Creativity moves partly toward:

- grammar design;
- selection of invariants;
- parameter spaces;
- semantic mappings;
- constraints;
- generation and mutation rules;
- evaluation and selection;
- provenance and reproducibility.

## 6. Relation to the Machine à Explorer

This lineage now connects naturally with the corpus concept of **Machine à explorer**.

A generative graphic studio can be understood as a specialized Machine à Explorer applied to forms:

```text
grammar
+ constraints
+ libraries
+ generative mechanisms
+ variation
+ comparison
+ selection
+ traceability
→ rational exploration of visual possibles
```

The corresponding anti-pattern would be a visual pipeline that narrows possibilities through opacity, proprietary lock-in, unreproducible outputs or a single imposed representation.

The relevant doctrinal relation is therefore:

> Stabilize enough to preserve meaning and provenance; generate enough diversity to explore.

## 7. Relation to Cogentia / Fractanet / Digital Twins

The same progression now enters the Cogentia/Fractanet architecture.

The semantic model should remain independent from its graphical projection. A Digital Twin may be rendered through:

- a Digipees reference profile;
- a client visual identity;
- a community-specific profile;
- a technical/engineering view;
- a photographic or near-realistic representation;
- an animated or narrative representation.

Digipees can therefore serve as a generic Made-in-Corsica visual language while FractaVolta's Graphic Design offering supports alternate client and community identities over the same semantics.

This follows the same map/territory discipline as Cogentia/Cogentigram: the representation must remain distinguishable from what it represents.

## 8. Historical sequence

```text
~2000s   YanUg bitmap / fixed visual asset
            ↓
          YanUg procedural SVG
            ↓
2026      Jana parameterized logo generator
            ↓
2026      Digipees visual + kinetic + semantic grammar
            ↓
          AI-assisted generative visual studio
```

The dates above should be refined when stronger provenance is recovered. The purpose of this note is to preserve the lineage while the source material is still being reconstructed.

## 9. Related work

- `barons-Mariani/hosted/digipees/`
- `barons-Mariani` issue #33 — Digipees visual grammar
- `barons-Mariani` issue #34 — Digipees provenance, licensing and naming
- `FractaVolta/tools/jana-logo-generator/`
- `FractaVolta` issue #21 — Jana retrofit
- `FractaVolta` issue #22 — configurable visual profiles / Graphic Design offering
- `cogentia` issue #98 — cognitive and industrial Digital Twin projections
- `cogentia/research/concepts.md` — Machine à explorer / Machine à empêcher
- `JeanHuguesRobert/serra/core/src/utils/YanUg.js`
- `JeanHuguesRobert/simpli/lib/yanug.png.js`

## 10. Working formula

> **Image → structure → function → generative space.**

And, in the vocabulary of the corpus:

> **Generative graphic design is a specialized Machine à Explorer: an Exploration Rationnelle et Joyeuse du Possible applied to forms.**
