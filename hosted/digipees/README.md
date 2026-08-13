# Digipees

Digipees is a **hosted repository** within `JeanHuguesRobert/barons-Mariani`.

It has its own identity, history, assets and workstream while relying on the parent repository for hosting, preservation and default governance. Hosting does not imply permanent merger: the project is intended to remain conceptually autonomous and extractable.

## Initial scope

The first workstream is deliberately narrow:

1. preserve the historical Digipees source assets;
2. document their provenance;
3. reconstruct and formalize the historical visual grammar;
4. distinguish canonical historical material from normalized and derived work;
5. prepare later thematic variants, including a FractaVolta primary-palette theme, without modifying the historical canon.

Generator tooling, broader applications and naming/licensing work may be split into later workstreams once the visual grammar is sufficiently understood.

## Hosted-repository status

```yaml
hosted_repository:
  id: digipees
  host: JeanHuguesRobert/barons-Mariani
  status: hosted
  autonomy: conceptual
  operational_autonomy: target
  extractable: true
```

See `docs/hosted-repositories.md` in the host repository for the emerging generic convention.

## Contents

- `HISTORY.md` — origin and preservation targets.
- `originals/` — the two recovered SVGs, byte-identical to the recovered files, never
  edited. See `originals/PROVENANCE.md` for dates and the differences between them.
- `docs/visual-grammar.md` — the graphic invariants (outline weights, palette, shadow and
  caption conventions, layer structure) and a FractaVolta theming-hook convention. See
  also `../../research/generative_graphic_design_lineage.md` §7–9 for the wider
  YanUg → Jana → Digipees lineage this sits in.
- `docs/inventory.md` — the full list of characters, devices, content symbols, and the
  one composed scene, plus a version-diff summary between the two recovered files.
- `normalized/digipees-icon-sheet.svg` — one candidate normalized asset: the full sheet
  with CSS custom-property theming hooks (`--digipee-ink`, `--digipee-surface`,
  `--digipee-shade`), each defaulting to the original color so it renders identically to
  canon until themed. Not a generator, not a per-icon extraction — a single demonstration
  file.

## Non-goals (issue #33)

No full generator, no application-specific asset kit, and no standalone Digipees
repository are in scope for this workstream. Provenance depth, licensing and naming are
tracked separately in issue #34. Building on the normalized asset and hooks above is
future work.
