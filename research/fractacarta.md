---
title: "FractaCarta"
subtitle: "Recursive, multidimensional and epistemically traceable cartography"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica, France"
date: "2026-09-18"
last_modified_at: "2026-09-18"
version: "0.1"
status: "working-note — FractaCarta working hypothesis"
document_role: "source"
document_kind: "doctrinal-note"
visibility: "public"
lifecycle_state: "working"
language: "en"
license: "CC BY-SA 4.0"
update_policy: "UP-DEFAULT-REVIEWED"
review:
  status: "unreviewed"
  reviewed_by: []
related_documents:
  - "research/potentics_exploration_ontology.md"
  - "research/rational_odysseys_the_possible.md"
  - "research/presencology.md"
  - "research/the_network_is_the_learning_computer.md"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "FractaCarta exploration — 2026-09-18"
  origin_date: "2026-09-18"
  derived_from:
    - "research/potentics_exploration_ontology.md"
    - "research/rational_odysseys_the_possible.md"
    - "research/presencology.md"
tags:
  - fractacarta
  - maps
  - territory
  - cartography
  - multidimensional
  - multiscale
  - recursive-cartography
  - provenance
  - potentics
  - cogentia
  - prior-art-friendly
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "explicit-metadata"
classification_confidence: "medium"
changelog:
  - "v0.1 (2026-09-18) — first stabilization of the FractaCarta working hypothesis, minimal model, transformations and prior-art-friendly lineage."
---

# FractaCarta

## 1. Problem

The Corpus repeatedly uses the distinction between **map and territory**. Potentics treats Maps as corrigible representations used to orient exploration, while Territory is encountered and can answer differently from what a representation predicts.

As the Corpus grows, one object may need many simultaneous maps: temporal, relational, geographical, documentary, institutional, technical, epistemic, artistic, biographical or other. No single tree, directory, graph view or ontology should silently become the territory.

FractaCarta names a working hypothesis for organizing such plurality without requiring one universal representation.

> **A map is not the territory; a useful territory may admit many local maps, and any sufficiently explored map can itself expose new territory requiring new maps.**

---

## 2. Working definition

**FractaCarta is an open grammar of recursive cartography for producing, navigating and comparing local, multidimensional, multiscale and epistemically traceable projections of a territory, without confusing any projection with the territory itself.**

FractaCarta is deliberately **not defined as**:

- a universal ontology;
- a database;
- a knowledge graph;
- a filesystem hierarchy;
- a visualization toolkit;
- a zoomable user interface;
- a replacement for RDF, provenance standards, nanopublications, GIS, OLAP, hypergraphs or Cognitive Packets.

Those may be substrates, representations, implementations or interoperable companions.

The fractal property is primarily **cartographic and navigational**, not a claim that the underlying Territory is mathematically fractal.

---

## 3. Map and territory

A useful provisional layering is:

```text
REAL / TERRITORY
        │
        │ observations / encounters
        ▼
      TRACES
documents / events / messages / photos / measurements
        │
        ▼
KNOWLEDGE SUBSTRATE
assertions / hypotheses / relations / contradictions
provenance / evidence / epistemic status
        │
        ▼
   FRACTACARTA
        │
projection according to anchor, dimensions,
scale, scope, question and epistemic policy
        │
        ▼
       MAP
```

This layering is itself a Map. The knowledge substrate is **not** the Territory either.

A Trace, assertion, Map, projection recipe or other represented object can become Territory for a subsequent inquiry.

A Map may also change its observer: an encounter with a representation can
alter what the observer subsequently notices, interprets, or projects, even
when the represented Territory has not changed.

```text
Map_n + Observer_n
        ↓ encounter
Observer_n+1
        ↓
new reading / projection
```

---

## 4. Minimal model

The initial minimal structural hypothesis contains four primitives.

### 4.1 Anchor

The **Anchor** identifies what the current Map is a map *of* or *around*.

Examples:

```text
a person
an email
an assertion
a place
a period
a relation
a software component
a Mission
another Map
```

The Anchor preserves orientation while representations change.

### 4.2 Projection

A **Projection** is the declared operation or recipe that produces a Map from an accessible knowledge substrate for a purpose.

A projection can select dimensions, resolution, filters, epistemic policies and presentation structures. It does not thereby create new facts.

### 4.3 Scope

**Scope** states the context in which a representation, assertion or Map is intended to be relevant.

Scope may include time, jurisdiction, source perspective, mission, vocabulary, community, epistemic assumptions or other contextual boundaries.

Different scoped Maps may disagree without one automatically invalidating the others.

### 4.4 Provenance

**Provenance** makes inspectable what a Map or represented element rests upon and how it was produced.

It can link projections to assertions, traces, sources, agents, transformations and prior Maps.

A FractaCarta implementation SHOULD preserve enough provenance to permit criticism, reconstruction and comparison of Maps.

---

## 5. Fundamental transformations

The initial working hypothesis distinguishes three fundamental navigation transformations.

### 5.1 ZOOM

**ZOOM** changes resolution around an Anchor.

```text
Marie-Louise
→ identities
→ digital identities
→ email identities
→ a particular account
→ a particular name
```

Semantic zoom need not merely enlarge the same representation. A change of scale may produce a different Map appropriate to the new resolution.

### 5.2 PIVOT

**PIVOT** changes the dimensions or perspective of a projection while preserving a meaningful Anchor.

```text
Dorma
→ temporal projection
→ documentary projection
→ relational projection
→ evidentiary projection
```

### 5.3 REANCHOR

**REANCHOR(x)** takes an element encountered through the current Map and makes it the Anchor of a new cartographic exploration.

```text
assertion
→ supporting email
→ REANCHOR(email)
→ Map(email)
```

REANCHOR is not merely deeper zoom. It permits movement through a graph of local territories without pretending that those objects belong to one hierarchy.

---

## 6. Recursive cartography

Recursive cartography is the central FractaCarta hypothesis.

```text
Map(A)
  │
  ├─ element B
  │      └─ REANCHOR → Map(B)
  │
  └─ element C
         └─ REANCHOR → Map(C)
```

A Map may itself become an Anchor:

```text
Map(M1)
→ provenance of M1
→ assumptions of M1
→ comparison with M2
→ disagreements
→ traces supporting each projection
```

There is therefore no necessary universal "level 7" or canonical tree. There are transitions between local Maps.

---

## 7. Epistemic invariants

FractaCarta inherits and strengthens several Corpus invariants:

1. **Map ≠ Territory.**
2. **Knowledge substrate ≠ Territory.**
3. **Unknown ≠ absent ≠ impossible.**
4. **Navigation ≠ inference.** ZOOM, PIVOT and REANCHOR do not by themselves create facts.
5. **Projection ≠ truth.** A Map is situated and corrigible.
6. **Contradictions are cartographable.** A system SHOULD preserve incompatible sourced assertions when the evidence does not justify collapsing them.
7. **Provenance travels with claims and projections.**
8. **Locality before duplication.** Information SHOULD remain at the most local level where it stays intelligible; higher-level Maps SHOULD reference rather than unnecessarily copy underlying evidence.
9. **No premature formalization.** Exploration SHOULD NOT require Territory to fit a structure before evidence justifies that structure.
10. **Multiple Maps are normal.** Different questions, dimensions, scopes and epistemic policies may legitimately produce different Maps of overlapping Territory.

A useful map state may be modeled provisionally as:

```text
M = P(K | A, D, S, F, Φ, Q, Σ, E)
```

where:

```text
K = accessible knowledge substrate
A = anchor
D = selected dimensions
S = scale / resolution
F = focus
Φ = filters
Q = question / purpose
Σ = scope
E = epistemic policy
P = projection
M = resulting Map
```

Only Anchor, Projection, Scope and Provenance are currently proposed as minimal structural primitives. The other parameters remain useful modeling candidates rather than frozen ontology.

---

## 8. Relationship with the Corpus

### 8.1 Potentics

Potentics explains **why Maps are explored**: to rationally explore The Possible through corrigible representations and Reality tests.

FractaCarta provides a grammar for constructing and navigating plural Maps during such exploration.

```text
Map
→ exploration
→ encounter
→ trace
→ assertion / residue
→ Corpus assimilation
→ corrected or alternative Map
```

### 8.2 Cogentia

Cogentia can provide cognitive substrate, memory, agents, transformations and execution mechanisms beneath FractaCarta.

FractaCarta SHOULD remain independent of any one Cogentia implementation.

### 8.3 Cognitive Packets and Packet-Backed Projection

Cognitive Packets can transport bounded units of work or knowledge. Packet-Backed Projection can make projections traceable to their supporting packets.

FractaCarta can describe how such projections are organized and navigated without replacing packet semantics.

### 8.4 Olé Olé and Presencology

Olé Olé already provides a specialized partial implementation of multidimensional cartography: geography combines with time, intent, modality, coverage and presence.

Presencology generalizes Presence beyond physical location and explicitly distinguishes Presence, observations, claims, estimates and maps.

These are existing local maps within the broader FractaCarta hypothesis, not subordinate examples to be redesigned from scratch.

---

## 9. Friends — prior-art-friendly lineage

FractaCarta follows the Corpus principle of **prior-art-friendly exploration**.

> **Independent convergence is evidence and opportunity, not a defect. Relate before reinventing.**

When existing work expresses part of FractaCarta adequately, the preferred first move is to learn, cite, reuse where permitted, interoperate and cooperate rather than create a competing universal format.

Current friends include:

| Friend / lineage | What it already gives us | FractaCarta question |
|---|---|---|
| **RDF / Linked Data** | open graph representation, identifiers, vocabularies | how to project and navigate plural local maps over heterogeneous graphs |
| **Wikidata / Wikibase** | statements, qualifiers, references, ranks and contextualized claims | how those claims participate in recursive maps |
| **W3C PROV-O** | interoperable provenance vocabulary | how map derivation and navigation preserve provenance |
| **Nanopublications** | assertion + provenance + publication information; durable publication patterns | how bounded knowledge units become map material |
| **Topic Maps** | subjects, topics, occurrences, associations and scope | how scope and subject identity relate to Anchor and Projection |
| **RDF Data Cube / OLAP** | dimensions, slices, drill-down, roll-up, pivot | how multidimensional analytical operations generalize to heterogeneous knowledge |
| **Graph OLAP** | multigranular and multiperspective graph analysis | how graph aggregation relates to semantic zoom |
| **Pad++ / zoomable interfaces** | scale as an information-navigation dimension | how visual scale becomes semantic and epistemic scale |
| **Spatial hypertext** | emergent organization and resistance to premature formalization | how provisional structure remains revisable |
| **Faceted navigation** | multidimensional exploration and progressive refinement | how Pivot and filtering preserve Anchor and context |
| **GraphRAG** | hierarchical graph communities and multiscale retrieval | how retrieval-generated maps relate to durable maps and evidence |
| **Graphiti / temporal knowledge graphs** | evolving temporal graph memory and provenance-oriented ingestion | how time and changing knowledge alter projections |
| **Hypergraphs** | native n-ary relations | how complex events and assertions avoid forced binary decomposition |
| **GIS / OpenStreetMap** | layers, locality, extensible community vocabularies and practical cartography | how geographical lessons generalize without forcing all Territory into spatial geometry |
| **Olé Olé / Presencology** | Corpus-native multidimensional presence maps | how existing operational maps become FractaCarta-compatible projections |

This list is a research constellation, not a claim of equivalence or exhaustive prior art.

### Design rule

> **FractaCarta SHOULD reuse existing open representations and protocols wherever they adequately express part of the model. Its purpose is to connect maps, not to impose another universal map.**

Licensing, governance, interoperability surfaces and active communities SHOULD be recorded when a friend becomes an implementation candidate.

---

## 10. Open questions

1. Is the proposed minimal core — Anchor, Projection, Scope, Provenance — actually irreducible?
2. Are ZOOM, PIVOT and REANCHOR fundamental transformations, or can one be derived cleanly from the others?
3. What makes two Maps maps of the "same" Territory when their anchors, dimensions or scopes differ?
4. How should map identity and versioning work when the knowledge substrate evolves?
5. How should a projection declare its epistemic policy without creating a large mandatory ontology?
6. When should contradictory Maps remain separate, be superposed, or generate a new synthesis?
7. Can FractaCarta map Maps themselves without introducing an infinite regress problem in practice?
8. Which existing open standards can directly serialize the minimal primitives?
9. Can a filesystem/Git tree remain merely one documentary projection while graph navigation and computed Maps coexist above it?
10. What is the smallest useful FractaCarta experiment already achievable with Marie-Louise, Olé Olé or another existing Corpus territory?

---

## 11. Current restraint

FractaCarta is a **working hypothesis**, not a frozen architecture.

The next useful work is not to create a large FractaCarta ontology or bespoke storage engine. It is to:

```text
test the minimal model
→ confront it with existing Corpus maps
→ search for open friends and reusable standards
→ identify residue and mismatches
→ implement only what remains necessary
→ return the results to the Corpus
```

This restraint is part of the design.

> **The purpose of FractaCarta is to help us navigate representations without allowing any representation — including FractaCarta itself — to become confused with the Territory.**
