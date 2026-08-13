---
title: "Digipees — asset and version inventory"
version: "0.1"
status: source document / open working paper
date: "2026-08-14"
author: "Jean Hugues Noël Robert"
repository: "JeanHuguesRobert/barons-Mariani"
intended_path: "hosted/digipees/docs/inventory.md"
theoretical_anchor: "hosted/digipees/docs/visual-grammar.md"
license: "CC BY 4.0"
open_source: true
non_profit: true
commercial_purpose: false
commons_orientation: "bien commun documentaire ouvert"
language: "en"
tags:
  - digipees
  - svg
  - inventory
related_projects:
  - barons-Mariani
  - FractaVolta
ai_assisted_by: [Claude]
---

# Digipees — asset and version inventory

Related issue: [barons-Mariani #33](https://github.com/JeanHuguesRobert/barons-Mariani/issues/33).
Inventory built by rasterizing `../originals/digipies02.svg` and
`../originals/digipees21-08-2006.svg` and reading the captions and layout directly (both
files carry the same layout; see `../originals/PROVENANCE.md` for what differs between
them).

## Characters

| Caption | Description |
|---|---|
| `User` | Generic standing figure, minimal features (two-dot eyes, no other face detail) |
| `Gram'a` | Grandmother figure — glasses, headscarf/hair silhouette, handbag on the arm |

## Devices

| Caption | Description |
|---|---|
| `Television` | CRT-style television, 3/4 view |
| `DVD Player-Recorder` | Slot-loading player/recorder unit |
| `Remote Control` | Handheld remote, button grid visible |
| `Mobile` | Flip/candybar mobile phone with antenna |
| `Digtal Camera` [sic, source spelling] | Compact digital camera |
| `MP3 Player` | Portable player with wired earphones |
| `Personal Computer` | Desktop tower + CRT monitor + keyboard |
| `LabTop` [sic, source spelling] | Open laptop |
| `ZeeBox` | Set-top / home gateway box (product-style name, not a generic label) |
| `WiFi` | Radio-wave glyph (three concentric arcs), no character/device body |

## Content symbols ("Fichiers" cluster)

A group of four file-type icons under the shared caption `Fichiers` (French: "Files"):

| Caption | Description |
|---|---|
| `Photos` | Portrait/photo card. Empty grey placeholder in the 09:04 source; filled with a small face glyph in the 11:07 source |
| `films` | Film-strip icon |
| `Documents` | Page-of-text icon |
| `Sons` | Speaker/audio-device icon |

Note: these four are the only captions rendered as live SVG `<text>`, and only in
`digipies02.svg` — see `../originals/PROVENANCE.md`.

## Scenes

| Caption | Description |
|---|---|
| `Salon` | Living room: two seated/standing characters, a couch, and a television on a stand — the only composed multi-character scene in the set. Reads as the "home" context tying the devices and characters together. |

## Version diff summary

See `../originals/PROVENANCE.md` for the full provenance write-up. Summary:

- Same 20 top-level items/groups, same layout, same `viewBox`, in both files.
- `digipies02.svg` (11:07 save) is strictly more finished than
  `digipees21-08-2006.svg` (09:04 save, same day): it adds the four `Fichiers` sub-labels
  as live text and fills in the `Photos` glyph.
- No item present in one file is absent from the other; the difference is completion, not
  content.

## Open questions (not resolved by this inventory)

- Whether "ZeeBox" refers to a specific real product of the era (2006) or is a generic
  invented device name — left unverified, flagged rather than guessed at (per the
  corpus rule against collapsing hypothesis into fact).
- Whether earlier/later versions of this sheet exist beyond the two recovered files.
