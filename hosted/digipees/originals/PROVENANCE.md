---
title: "Digipees — provenance des sources originales"
version: "0.1"
status: source document / archival note
date: "2026-08-14"
author: "Jean Hugues Noël Robert"
repository: "JeanHuguesRobert/barons-Mariani"
intended_path: "hosted/digipees/originals/PROVENANCE.md"
license: "CC BY 4.0"
open_source: true
non_profit: true
commercial_purpose: false
commons_orientation: "bien commun documentaire ouvert"
language: "en"
tags:
  - digipees
  - svg
  - provenance
  - visual-grammar
  - fractavolta
related_projects:
  - barons-Mariani
  - FractaVolta
ai_assisted_by: [Claude]
---

# Digipees — original source provenance

Related issue: [barons-Mariani #33](https://github.com/JeanHuguesRobert/barons-Mariani/issues/33).

## Files

Both files were recovered from Jean Hugues Robert's personal archive (Google Drive:
`digipies02.svg` at the Drive root, `images/digipees21-08-2006.svg`) and are stored here
byte-for-byte, unmodified.

| File | Illustrator `ModifyDate` (UTC) | Size | Paths | Live `<text>` |
|---|---|---|---|---|
| `digipees21-08-2006.svg` | 2006-08-21T09:04:58Z | 654,395 B | 311 | 0 |
| `digipies02.svg` | 2006-08-21T11:07:19Z | 690,253 B | 317 | 4 |

Both carry the same Illustrator document identity (`xap:CreateDate` 2006-04-07T13:13:37Z,
same `rdf:about` UUID in the embedded XMP metadata), the same `viewBox`
(`0 0 2089.734 1580.7`), and the same four Illustrator layer names
(`Calque_1`…`Calque_4`, French for "Layer 1"…"Layer 4"). They are two saves of the same
Adobe Illustrator 11 document, about two hours apart, on the same day.

## Reading order / canon

`digipies02.svg` is the later, more complete save and is treated as the closer-to-canon
source for downstream work (see `../docs/visual-grammar.md`). `digipees21-08-2006.svg` is
kept as the earlier state, not discarded, per the corpus rule of preserving source material
distinct from derived products.

## Known differences (09:04 → 11:07 save)

- The "Fichiers" (files) icon cluster's four sub-icons are unlabeled in the 09:04 save;
  the 11:07 save adds four live SVG `<text>` elements (`Photos`, `films`, `Documents`,
  `Sons`), each in `Myriad-Roman` 12pt — the only live text in either file. Every other
  caption in both files ("User", "Gram'a", "Television", …) is outlined to vector paths,
  not live text.
- The "Photos" sub-icon is an empty grey placeholder rectangle in the 09:04 save; the
  11:07 save fills it with a small portrait/photo glyph.
- Path count differs by 6 (311 vs 317), consistent with the added photo glyph detail.
- Both files otherwise share the same geometry, layer structure, and style values
  (see `../docs/visual-grammar.md`).

## Structural note

Only `Calque_2` carries visible artwork (20 top-level groups, ~310 paths) in both files.
`Calque_1`, `Calque_3`, and `Calque_4` are present but empty — unused Illustrator layers
carried along by the export, not a meaningful content split. Do not read significance into
their names or `i:rgbTrio` values.

## Integrity

Do not edit the files in this directory. If a correction or a better-quality source is
found later, add it alongside with its own provenance entry rather than overwriting.
