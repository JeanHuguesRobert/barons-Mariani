---
title: "Digipees — character set v1"
subtitle: "New 2026 artwork extending the historical two characters toward demographic variety"
version: "0.1"
status: source document / derived artwork
date: "2026-08-15"
author: "Jean Hugues Noël Robert"
repository: "JeanHuguesRobert/barons-Mariani"
intended_path: "hosted/digipees/docs/character-set.md"
theoretical_anchor: "hosted/digipees/docs/visual-grammar.md"
license: "CC BY-SA 4.0"
open_source: true
non_profit: true
commercial_purpose: false
commons_orientation: "bien commun documentaire ouvert"
language: "en"
tags:
  - digipees
  - characters
  - visual-grammar
  - fractavolta
related_projects:
  - barons-Mariani
  - FractaVolta
ai_assisted_by: [Claude]
---

# Digipees — character set v1

Asset: [`../derived/characters/character-set-v1.svg`](../derived/characters/character-set-v1.svg).
Companion: `visual-grammar.md`, `../../research/generative_graphic_design_lineage.md` §8.2
(morphology / identity-delta rule).

## What this is

Four new characters — **not** extracted from the historical originals, **not** a
reconstruction of anything from the 2006 sources. This is new 2026 artwork, authored to
extend `User` and `Gram'a` (the two historical characters, unchanged, still living only in
`../originals/` and `../normalized/`) toward demographic variety.

The brief was: variety of **people** — sex/gender presentation, age, look — not variety of
**personality**. Unlike a Smurfs-style ensemble (each figure defined by a trait — Grumpy,
Brainy, Vain), none of these characters carries a backstory or disposition. The captions
(`Gramp'a`, `Junior`, `Sis`, `Mate`) are a casual family-register naming convention
matching `Gram'a`, not role or personality labels.

## Roster

| Caption | Variety axis | Distinguishing delta from the base figure |
|---|---|---|
| `Gramp'a` | age (elderly), presenting male | flat cap, mustache, cane |
| `Junior` | age (child) | smaller scale, larger head-to-body ratio, twin pigtails |
| `Sis` | presenting female | swept ponytail (two thin strokes) |
| `Mate` | mobility | wheelchair in place of legs, shorter seated torso |

Together with the existing `User` (generic) and `Gram'a` (elderly, presenting female,
glasses), that is six figures spanning three age bands, both commonly-read gender
presentations, and one visible mobility variation — without any of them being reduced to
a joke or a single trait.

## Design approach: stable base + identity delta

Per the lineage doc's own morphology rule (§8.2): a shared base (head circle, pill-shaped
torso, ground-shadow ellipse, two-dot eyes, standing pose) carries every figure, and each
character differs by one or two small, legible deltas (a cap, a hairstyle, a scale change,
a mobility aid) rather than being redrawn from scratch. This is deliberate: it is what
makes the set easy to extend — a new figure is "base + one new delta," not a new drawing.

## Construction note (why these look different from the historical originals)

The historical `User`/`Gram'a` are hand-drawn Adobe Illustrator paths with organic Bezier
curves. Reproducing that exact line quality by hand-authoring SVG coordinates (no vector
illustration tool, only render-and-inspect iteration) was judged unreliable and likely to
look worse than a clean, deliberately simplified alternative. These four characters are
instead built from a small vocabulary of primitives — circles, rounded rectangles, a few
short curved strokes — styled with the same stroke/fill values as the rest of the grammar.
This is consistent with the grammar's own invariant 6 ("simplified, rounded geometry...
detail minimized to the smallest number of shapes"), just leaning further into it. If a
closer visual match to the historical hand-drawn line is wanted later, that is a redraw,
not a fix to this file.

## Grammar conformance

- Outline: `stroke="var(--digipee-ink, #000000)"`, stroke-width 8 for silhouette (7 for
  smaller accessory shapes at this scale, 5–6 for fine accents) — thicker than the
  original's exact weights but proportionally consistent (thick silhouette / thin detail).
- Fill: restricted to `var(--digipee-surface, #FFFFFF)` and, once,
  `var(--digipee-shade, #B3B3B3)` (the wheelchair seat cushion) — same two-color-plus-ink
  palette as invariant 3.
- Ground shadow: solid ellipse per figure, same convention as invariant 5.
- Theming: uses the same three hooks as `../normalized/digipees-icon-sheet.svg`. Verified
  by re-rendering with `--digipee-ink:#0046AD; --digipee-shade:#F0C30F` (the same
  FractaVolta combination already used in `digipees-icon-sheet.fractavolta-theme.svg`) —
  themes correctly with no geometry change.

## Non-goals

Not a generator (each figure is hand-authored, not parametrically produced from a schema,
even though a small script was used as an authoring convenience). Not a claim about the
historical canon. Does not attempt skin-tone or literal race representation — variety is
carried by silhouette/accessory, consistent with the grammar staying in the register of
"representation," not photoreal likeness (cf. `../../research/generative_graphic_design_lineage.md`
§10).

## Extending this set

Follow the same pattern: pick one or two new deltas (a headscarf, a taller/shorter
proportion set, glasses, a different accessory), reuse the base head/torso/legs/shadow
functions, keep the same stroke/fill values. The roster above is v1, not a closed set.
