---
title: "Digipees — visual grammar"
subtitle: "Formalizing the graphic invariants of the recovered 2006 icon set before building any generator"
version: "0.1"
status: source document / open working paper
date: "2026-08-14"
author: "Jean Hugues Noël Robert"
repository: "JeanHuguesRobert/barons-Mariani"
intended_path: "hosted/digipees/docs/visual-grammar.md"
theoretical_anchor: "hosted/digipees/originals/PROVENANCE.md"
license: "CC BY-SA 4.0"
open_source: true
non_profit: true
commercial_purpose: false
commons_orientation: "bien commun documentaire ouvert"
language: "en"
tags:
  - digipees
  - svg
  - visual-grammar
  - fractavolta
  - pictogram
related_projects:
  - barons-Mariani
  - FractaVolta
ai_assisted_by: [Claude]
---

# Digipees — visual grammar

Related issue: [barons-Mariani #33](https://github.com/JeanHuguesRobert/barons-Mariani/issues/33).
Source material: `../originals/` (see `PROVENANCE.md`). This document formalizes what is
observed in the 2006 sources; it does not propose new artwork. It is a close, file-level
read of the two source SVGs; for the wider historical lineage (d2lab origin, semantic and
kinetic grammar, Digipees Studio direction) see
`../../research/generative_graphic_design_lineage.md` §7–9, which this document
complements rather than duplicates.

## What the set is

A 2006 Adobe Illustrator pictogram sheet, originating in the mid-2000s **d2lab** project
("Digital People"), for a home-digital-literacy scenario: a generic `User` and a `Gram'a`
(grandmother) character navigating consumer electronics, files, and a living room
("Salon") scene. See `inventory.md` for the full item list. This fits the
corpus's cultural-mediation / digital-divide concerns (cf. `ai-based-cultural-mediation.md`)
rather than being a generic clip-art set.

## Graphic invariants

Observed consistently across both source files (`digipees21-08-2006.svg`, `digipies02.svg`):

1. **Isometric-ish oblique perspective.** Every device and character is drawn at the same
   consistent tilted 3/4 angle — a pseudo-3D "product shot" convention, not orthographic
   front views.

2. **Two-tier outline weight.**
   - Silhouette/outer contour: `stroke="#000000"`, `stroke-width="8"`, `fill="none"` —
     one thick pass per shape defining its outer boundary.
   - Interior detail lines: predominantly `stroke-width="1.5"` (the large majority),
     with `2.5`, `2`, `1.25`, `5` used sparingly for secondary emphasis (seams, buttons,
     accents). Always `stroke="#000000"`.
   - The outline and the fill are separate overlapping paths sharing the same `d`
     geometry — a duplicate-path technique (thick stroke-only pass + thin
     stroke-and-fill pass), not a single stroked-and-filled path.

3. **Two-color fill palette, nothing else.** Fills are restricted to `#FFFFFF` (white —
   the dominant, primary colorable surface) and `#B3B3B3` (mid-grey — a secondary/shade
   zone, used sparingly: 4–5 occurrences per file, e.g. the camera lens, the photo
   glyph). No other fill color appears anywhere in either file. `fill="none"` is used for
   line-only detail strokes.

4. **Implicit-black accents.** A small number of elements (the ground-shadow ellipses,
   the two-dot "eyes" on characters) carry no explicit `fill` attribute at all and rely on
   the SVG initial value (black). This is a real convention in the source, not an
   oversight — see the theming-hook note below for why it matters.

5. **Flat contact shadow.** Every free-standing character or device sits on a solid black
   ellipse (`<ellipse>`, unstyled fill) directly beneath it — a uniform "grounding"
   device rather than a rendered cast shadow or gradient.

6. **Simplified, rounded geometry.** Corners are consistently rounded, detail is
   minimized to the smallest number of shapes that still reads as the object (e.g. a
   laptop is a lid + base + two accent lines, not a rendering of a real laptop). This is
   a "friendly pictogram" register, not technical illustration.

7. **Captions.** Each item has a caption set in `Myriad-Roman`, roughly 12pt, positioned
   below the icon. In both files, all top-level captions ("User", "Gram'a", "Television",
   …) are outlined to vector paths (curves), not live text. The one exception is the four
   "Fichiers" sub-labels (`Photos`, `films`, `Documents`, `Sons`), which are live
   `<text>`/`<tspan>` elements — and only in the later `digipies02.svg` save (see
   `PROVENANCE.md`).

8. **Document structure.** Fixed `viewBox="0 0 2089.734 1580.7"`. Four Illustrator layers
   (`Calque_1`…`Calque_4`); only `Calque_2` holds artwork (~310 paths across 20 top-level
   groups). The other three are empty and carry no semantic meaning — do not treat the
   layer split as a content taxonomy.

## Historical canon vs. normalized vs. derived

Three distinct tiers, to keep separate per the corpus rule against collapsing categories:

- **Historical canon** — `../originals/*.svg`, byte-identical to the recovered files.
  Never edited.
- **Normalized assets** — cleaned derivatives that preserve the exact geometry and colors
  but expose theming seams (see `../normalized/`). Default rendering must stay
  pixel-identical to canon.
- **Derived themes** — future, out of scope here (see Non-goals). Would consume the
  normalized assets and set the theming hooks below to an actual palette.

## FractaVolta theming hook

The two-color-plus-black-and-white palette (invariant 3–4 above) is already, structurally,
a set of colorable zones. `../normalized/digipees-icon-sheet.svg` makes this explicit by
replacing the three literal presentation-attribute values with CSS custom properties, each
defaulting to its original value so the file renders identically until themed:

| Hook | Default (= canon) | Source role |
|---|---|---|
| `--digipee-ink` | `#000000` | `stroke="#000000"` — all outline/detail strokes |
| `--digipee-surface` | `#FFFFFF` | `fill="#FFFFFF"` — primary colorable fill |
| `--digipee-shade` | `#B3B3B3` | `fill="#B3B3B3"` — secondary/shade fill |

A consumer themes the whole sheet by setting these three properties on an ancestor
element, e.g. toward the FractaVolta palette from issue #33
(`#D7141A` red, `#F0C30F` yellow, `#0046AD` blue, `#1A1A1A` black, `#FFFFFF` white) —
tested during this work with `--digipee-ink:#0046AD; --digipee-shade:#F0C30F`, which
renders correctly with no geometry change.

Elements with no explicit `fill` (ground shadows, character eyes — invariant 4) are left
untouched: they already inherit whatever `fill` a wrapping element sets, which is a
pre-existing, zero-code hook for "ink accents." Adding an explicit override for them was
judged unnecessary and a needless divergence from canon.

Verified: `../normalized/digipees-icon-sheet.svg` rendered with no theme applied is
byte-identical (as a rasterized PNG) to `../originals/digipies02.svg` rendered the same
way.

## Non-goals (per issue #33)

No generator, no application-specific asset kit, and no standalone Digipees repository are
produced here. `../normalized/digipees-icon-sheet.svg` is a single hand-produced candidate
demonstrating the hook convention above, not a build pipeline.
