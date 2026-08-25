---
title: "JHN Architecture — Normative Definition Draft"
subtitle: "Minimal conformance definition for packet/continuation computing"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica, France"
date: "2026-08-25"
last_modified_at: "2026-08-25"
version: "0.2"
status: "candidate normative core"
license: "CC BY-SA 4.0"
language: "en"
document_role: "source"
document_kind: "architecture-specification"
visibility: "public"
lifecycle_state: "working"
related_documents:
  - "research/jhn_architecture.md"
  - "research/jhn_architecture_packet_closure_addendum.md"
  - "research/the_network_is_the_learning_computer.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_closure_and_packet_native_semantics.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Architecture.md"
tags:
  - jhn-architecture
  - normative
  - conformance
  - cognitive-packets
  - packet-closure
  - continuations
  - distributed-computing
update_policy: "UP-DEFAULT-REVIEWED"
---

# JHN Architecture

## 1. Definition

A **JHN Architecture instance** is a computational system in which independently continuable work is represented by persistent, identifiable **Packets** whose execution may move across replaceable handlers, nodes and storage substrates without losing continuity or causality.

A Packet is the smallest unit of work for which independent identity is useful for one or more of:

```text
resumption | routing | accounting | retry | cancellation |
branching | return | reuse | persistence | authorization
```

A conforming implementation MUST satisfy the invariants below.

## 2. Abstract state

A JHN instance is represented provisionally by:

\[
\mathcal{J} = (P, H, S, T, G, X)
\]

where:

```text
P  active or durable Packets
H  available handler capabilities
S  logical stores, bindings and placements
T  causal, lineage and execution trace
G  optional governance, authority and resource constraints
X  optional outstanding or completed external effects
```

`G` and `X` MAY be empty in JHN/Core and become constrained by stricter profiles.

Each Packet `p ∈ P` has at least:

```text
identity
continuation semantics
Packet Closure
current state or state references
causal frontier
lineage
constraints
```

Additional profiles MAY require budget, mandate, Ithaca, disclosure, accounting or assimilation fields.

## 3. Packet Closure

For every Packet accepted for execution:

\[
Closed(p, h, \mathcal{J}) = true
\]

for the selected admissible handler `h`.

`Closed` means that every dependency required for correct continuation is either:

```text
embedded in the Packet,
stably and verifiably referenced,
or materializable through declared resolvers/stores.
```

Undocumented process-local state MUST NOT be required for resumption across a declared durability or mobility boundary.

## 4. Continuity invariant

Packet identity and continuation MUST NOT depend on the continued existence of the handler, process, node, provider or physical store that last processed the Packet.

Local volatile state MAY be used as an optimization.

After a declared durable boundary, loss of such volatile state MUST NOT destroy accepted durable progress.

## 5. Handler invariant

Handlers are capability providers, not owners of computational continuity.

A Packet MAY be processed by different admissible handlers over its lifetime.

Handler selection MAY depend on locality, cost, trust, latency, energy, quality, authority, jurisdiction or other declared constraints.

## 6. Storage invariant

Packet identity MUST be independent of physical storage technology.

A Packet MAY have zero, one or several placements.

A logical store MAY change physical binding without changing Packet identity.

Storage substrates MAY expose different capabilities; a conforming architecture MUST NOT require all stores to implement one identical universal interface.

## 7. Transition semantics

Processing a Packet is modeled as:

\[
(p, h, \mathcal{J}) \rightarrow (Y, P', I, \mathcal{J}')
\]

where:

```text
Y   zero or more results / Artifacts / observations
P'  zero or more successor or downstream Packets
I   zero or more proposed external EffectIntents
J'  resulting architectural state
```

`|P'|` MAY be `0..n`.

Composition MAY include sequence, fork, join, race, cancellation, selection or synthesis.

JHN/Core MAY leave `I` empty. External consequential effects are governed by JHN/Governed.

## 8. Causality and lineage invariant

Every durable transition MUST preserve enough information to reconstruct its causal relation to prior durable state.

Authority lineage and semantic dependency relations, when present, MUST remain distinguishable.

A downstream Packet MUST identify its upstream Packet relation.

## 9. Packet state and history

A conforming implementation MAY distinguish:

```text
Packet Identity
Historical Events / Artifacts
Packet Snapshot
Packet Capsule
```

A travelling representation MUST NOT be required to embed the complete historical trace if closure and causal integrity remain materializable and verifiable.

## 10. JHN/Core conformance

An implementation conforms to **JHN/Core** iff it satisfies Sections 3–9 for every Packet crossing a durability or mobility boundary that the implementation declares JHN-governed.

Purely local micro-operations MAY remain ordinary machine-local computation and need not become Packets.

A system MUST NOT claim JHN/Core conformance for a boundary across which Packet continuity depends on undocumented hidden state.

## 11. JHN/Governed profile

A JHN/Governed instance is a JHN/Core instance that permits consequential delegated acts.

For every such act:

```text
Principal
→ authority source
→ mandate
→ actor / handler
→ capability invocation
→ effect
```

MUST be reconstructible to the degree required by the governing policy.

Delegated authority MUST NOT exceed upstream authority.

A handler MUST NOT enlarge its own mandate, budget or capability authorization by its own authority.

A consequential external effect MUST be distinguishable from the cognition that proposed it.

The normative pattern is:

```text
Event / Packet state
→ EffectIntent
→ authority / policy / budget validation
→ effect commitment
→ EffectReceipt
→ resulting observation/Event
```

Authorization MUST be valid at the commit boundary when required by policy.

Retries MUST NOT silently duplicate effects that require at-most-once or idempotent semantics.

An EffectReceipt records executor evidence; it MUST NOT be treated as independent proof that external reality has the expected state.

## 12. Termination and cognitive return

A Packet MAY terminate with no successor Packet.

A Packet MAY declare a return target or continuation destination.

JHN/Cognitive MAY define this semantic home as **Ithaca** and distinguish:

```text
solved → returned → assimilated
```

These semantics are not required by JHN/Core.

## 13. Profiles

```text
JHN/Core
    packetized continuation, closure, mobility, causality

JHN/Governed
    JHN/Core + Principal, mandates, budgets, delegated authority, effect gates

JHN/Cognitive
    JHN/Core or JHN/Governed + Cognitive Packets, COP semantics, Ithaca

JHN/Learning
    JHN/Cognitive + Reactive Corpus, assimilation,
    changed future packet generation/routing/handling
```

A profile MAY strengthen requirements but MUST NOT weaken requirements inherited from its base profile.

## 14. Minimal conformance evidence

A JHN/Core implementation SHOULD be able to demonstrate, for at least one Packet:

```text
process restart without loss of durable continuation
handler substitution
store/placement change without Packet identity change
causal reconstruction of a downstream Packet
```

A JHN/Governed implementation SHOULD additionally demonstrate retry-safe governed commitment of at least one external effect.

The specification intentionally contains no historical justification. Rationale, prior art and historical placement belong in *The Network is the Learning Computer* and related research notes.
