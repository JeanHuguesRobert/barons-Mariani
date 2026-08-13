# Hosted repositories

A **hosted repository** is a repository-scale autonomous unit hosted inside another Git repository.

The notion complements, rather than replaces, the conventional **monorepo** model:

- **monorepo** describes the technical fact that several projects or components share one Git repository;
- **hosted repository** describes the institutional and lifecycle relationship between an autonomous unit and its host.

A hosted repository MAY contain documentation, source code, assets, data, tests and executable tools.

## Core properties

A hosted repository SHOULD preserve the following properties.

### 1. Identity

The hosted unit has a stable name, purpose and local root. Hosting does not imply conceptual absorption by the host.

### 2. Provenance

Its history and earlier publication locations are recorded. Migration or retrofit SHOULD NOT silently rewrite history.

### 3. Governance

The host provides default governance, contribution, preservation and infrastructure rules. A hosted unit MAY define explicit local rules where needed.

### 4. Operational autonomy

When executable code is present, the hosted unit SHOULD remain independently understandable, runnable and testable from its own subtree, modulo explicitly declared shared infrastructure.

### 5. Extractability

The hosted unit SHOULD be designed so that it can later be extracted into a standalone Git repository with minimal semantic or technical repair.

A useful practical test is whether history-preserving extraction of the subtree (for example with `git filter-repo`) would produce a coherent repository after only small adjustments.

### 6. Hostability is not permanence

Hosting is a lifecycle state, not an irreversible merger. A hosted repository MAY remain hosted indefinitely, move to another host, or become autonomous.

## Minimal local structure

No mandatory layout is imposed, but a hosted repository SHOULD normally expose at least a local `README.md`. Depending on scope it MAY also contain:

```text
hosted/<name>/
  README.md
  HISTORY.md
  docs/
  assets/
  src/ or tools/
  tests/
```

The structure SHOULD be proportional to the project. A one-file tool does not need the same scaffolding as a project containing a visual grammar, historical assets and multiple generators.

## Initial concrete cases

### Digipees — hosted by `barons-Mariani`

Digipees is being revived as a patrimonial and creative project whose historical assets, visual grammar and future tools can initially live under `barons-Mariani`. This is an explicit hosted-repository case: autonomous identity, host-level preservation, and future extractability.

### Jana logo generator — embedded in `FractaVolta`

The Jana logo generator was first published independently as a GitHub Gist and later produced assets used by FractaVolta. Its retrofit into a local `tools/jana-logo-generator/` subtree is a smaller software-oriented precedent. The historical Gist remains a provenance anchor while the in-repository subtree provides a canonical maintenance location.

These two cases intentionally differ in scale. Their common invariants are what should drive future generic rules.

## Status

This document is an initial convention derived from concrete cases, not a frozen specification. New rules SHOULD be introduced only when repeated cases demonstrate their necessity.
