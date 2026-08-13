---
title: "Digipees"
subtitle: "Recovered 2006 home-digital-literacy icon set — sources preserved, grammar formalized"
version: "0.1"
status: source document / open working paper
date: "2026-08-14"
author: "Jean Hugues Noël Robert"
repository: "JeanHuguesRobert/barons-Mariani"
intended_path: "hosted/digipees/README.md"
license: "CC BY 4.0"
open_source: true
non_profit: true
commercial_purpose: false
commons_orientation: "bien commun documentaire ouvert"
language: "en"
tags:
  - digipees
  - svg
  - fractavolta
related_projects:
  - barons-Mariani
  - FractaVolta
ai_assisted_by: [Claude]
---

# Digipees

Related issue: [barons-Mariani #33](https://github.com/JeanHuguesRobert/barons-Mariani/issues/33).

Digipees is a 2006 Adobe Illustrator pictogram sheet — a `User` and a `Gram'a`
(grandmother) character navigating home consumer electronics, files, and a living-room
scene. Two dated saves of the original document were recovered and are preserved here.

## Contents

- `originals/` — the two recovered SVGs, byte-identical to the recovered files, never
  edited. See `originals/PROVENANCE.md` for dates, differences, and integrity notes.
- `docs/visual-grammar.md` — the graphic invariants (outline weights, palette, shadow and
  caption conventions, layer structure) and the FractaVolta theming-hook convention.
- `docs/inventory.md` — the full list of characters, devices, content symbols, and the
  one composed scene, plus a version-diff summary.
- `normalized/digipees-icon-sheet.svg` — one candidate normalized asset: the full sheet
  with CSS custom-property theming hooks (`--digipee-ink`, `--digipee-surface`,
  `--digipee-shade`), each defaulting to the original color so it renders identically to
  canon until themed. Not a generator, not a per-icon extraction — a single demonstration
  file.

## Non-goals

No full generator, no application-specific asset kit, and no standalone Digipees
repository are in scope here (per issue #33). Building on the normalized asset and hooks
above is future work.
