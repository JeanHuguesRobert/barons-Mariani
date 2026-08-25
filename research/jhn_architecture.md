---
title: "JHN Architecture"
subtitle: "Normative definition of a packet/continuation computational architecture"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica, France"
date: "2026-08-14"
last_modified_at: "2026-08-25"
status: "working architecture specification"
version: "0.3"
license: "CC BY-SA 4.0"
language: "en"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/jhn_architecture.md"
document_role: "source"
document_kind: "architecture-specification"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
  - "GPT-5.6 Sol — normative refactoring"
review:
  status: "unreviewed"
  reviewed_by: []
update_policy: "UP-DESIRED-PRESENT"
related_documents:
  - "research/the_network_is_the_learning_computer.md"
  - "research/the_network_is_the_learning_computer_v0.8_jhn_architecture_rationale_addendum.md"
  - "research/jhn_architecture_packet_closure_addendum.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_closure_and_packet_native_semantics.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_switching.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Architecture.md"
tags:
  - jhn-architecture
  - architecture-specification
  - conformance
  - packets
  - continuations
  - packet-closure
  - distributed-computing
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "architecture-specification"
classification_confidence: "medium"
changelog:
  - "v0.1 (2026-08-14) — initial architectural working note."
  - "v0.2 (2026-08-14) — corrected frontmatter and review state."
  - "v0.3 (2026-08-25) — refactored into a short normative conformance specification; historical rationale, prior-art discussion, implementation motivation and research program migrated toward The Network is the Learning Computer."
---

# JHN Architecture

## 1. Definition

A **JHN Architecture instance** is a computational system in which independently continuable work is represented by persistent, identifiable **Packets** whose execution may cross replaceable handlers, processes, nodes and storage substrates without losing declared continuity or causality.

A **Packet** is a unit of work for which independent identity is useful for at least one of:

```text
resumption
routing
branching
retry
cancellation
accounting
authorization
return
reuse
persistence
```

A conforming implementation MUST satisfy the invariants below for every boundary it declares JHN-governed.

## 2. Abstract state

A JHN/Core instance is represented provisionally by:

\[
\mathcal{J} = (P, H, S, T)
\]

where:

- \(P\) — active or durable Packets;
- \(H\) — available handler capabilities;
- \(S\) — logical stores, physical bindings and Packet placements;
- \(T\) — durable causal, lineage and execution trace.

Each Packet \(p \in P\) has at least:

```text
identity
continuation semantics
Packet Closure
current state or state references
causal frontier
lineage
constraints
```

## 3. Packet Closure

For every Packet accepted by a handler \(h\):

\[
Closed(p,h,\mathcal{J}) = true
\]

`Closed` means that every dependency required for admissible continuation is either:

```text
embedded,
stably and verifiably referenced,
or materializable through declared resolvers/stores.
```

Undocumented process-local state MUST NOT be required across a durability or mobility boundary declared JHN-governed.

## 4. Continuity invariants

1. **Identity independence.** Packet identity MUST NOT depend on the continued existence of a handler, process, node, provider or physical store.
2. **Durable progress.** After a declared durable boundary, loss of volatile local state MUST NOT destroy accepted durable progress.
3. **Handler substitutability.** A Packet MAY be continued by different admissible handlers over its lifetime.
4. **Storage independence.** A Packet MAY have zero, one or several placements; changing a physical storage binding MUST NOT change Packet identity.
5. **Causal reconstructibility.** Every durable transition MUST preserve enough information to reconstruct its causal relation to prior durable state.
6. **Lineage.** Every downstream Packet MUST identify its upstream Packet relation.

Local volatile state MAY be used as an optimization.

## 5. Transition semantics

Processing is modeled as:

\[
(p,h,\mathcal{J}) \rightarrow (Y,P',\mathcal{J}')
\]

where:

- \(Y\) — zero or more results, Artifacts or observations;
- \(P'\) — zero or more successor or downstream Packets;
- \(\mathcal{J}'\) — resulting architectural state.

\[
|P'| \in \{0,1,2,\ldots\}
\]

Composition MAY include sequence, fork, join, race, cancellation, selection or synthesis.

## 6. Packet state and history

A conforming implementation MAY represent separately:

```text
Packet Identity
Historical Events / Artifacts
Packet Snapshot
Packet Capsule
```

A travelling Packet representation MUST NOT be required to embed its complete history if Packet Closure and causal integrity remain materializable and verifiable.

## 7. Conformance

An implementation conforms to **JHN/Core** iff Sections 3–6 hold for every Packet crossing a durability or mobility boundary that the implementation declares JHN-governed.

Purely local micro-operations MAY remain ordinary machine-local computation and need not become Packets.

A system MUST NOT claim JHN/Core conformance for a boundary across which Packet continuity depends on undocumented hidden state.

A JHN/Core implementation SHOULD be able to demonstrate, for at least one Packet:

```text
process restart without loss of durable continuation
handler substitution
store/placement change without Packet identity change
causal reconstruction of a downstream Packet
```

## 8. Profiles

Stricter profiles MAY add requirements without weakening JHN/Core.

```text
JHN/Governed
    Principal, mandates, budgets, delegated authority,
    governed external effects and receipts

JHN/Cognitive
    Cognitive Packet semantics, COP, semantic return / Ithaca

JHN/Learning
    Reactive Corpus, assimilation,
    changed future packet generation/routing/handling
```

The rationale, historical lineage, prior art, implementation motivations and research program of this architecture are intentionally outside this specification and belong primarily in *The Network is the Learning Computer* and related research notes.
