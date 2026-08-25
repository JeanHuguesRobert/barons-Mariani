---
title: "JHN Architecture — Packet Closure Addendum"
subtitle: "Distributed continuations, packet-native state, governed effects, and the abstract machine beyond process-local execution"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica, France"
date: "2026-08-25"
version: "0.1"
status: "integrated"
document_role: "derived"
document_kind: "research-addendum"
visibility: "public"
lifecycle_state: "archived-source-note"
language: "en"
license: "CC BY-SA 4.0"
related_documents:
  - "research/jhn_architecture.md"
  - "research/the_network_is_the_learning_computer.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_closure_and_packet_native_semantics.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_switching.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Architecture.md"
tags:
  - jhn-architecture
  - packet-closure
  - continuation
  - call-cc
  - distributed-memory
  - packet-placement
  - effects
  - post-von-neumann
  - cognitive-packet-switching
---

# JHN Architecture — Packet Closure Addendum

## Integration status

**Integrated into `research/jhn_architecture.md` v0.3 (2026-08-25).**

This source addendum is retained as an auditable historical trace of the transition from process-local continuation to distributed Packet Closure.

Proposed future changelog entry:

> **v0.3 (2026-08-25)** — introduces Packet Closure as the distributed continuation boundary; distinguishes packet identity, causal history, Packet Snapshot and travelling Packet Capsule; separates logical Packet Stores from physical storage technologies; materializes Event → EffectIntent → EffectReceipt → Event; and extends the abstract machine with placement and governed external effects.

## 1. From `call/cc` to distributed continuation closure

The parent architecture treats continuations as packetizable computational futures.

The classical continuation literature normally assumes a runtime-local universe. A captured continuation can depend on memory, bindings, runtime conventions and code that remain reachable from the same execution environment.

In simplified form:

```text
call/cc
→ capture continuation
→ retain implicit access to process/runtime memory
→ resume
```

JHN Architecture deliberately breaks the locality assumption:

```text
capture future work
→ persist
→ move
→ wait
→ change machine/runtime/provider
→ resume
```

This requires a stronger property.

> **Packet Closure is the distributed equivalent of the implicit environment that makes a process-local continuation resumable.**

A continuation packet is closed when every dependency required for admissible resumption is either embedded, stably referenced, or verifiably materializable.

The architecture therefore does not merely serialize continuations. It externalizes the closure conditions of continuation.

## 2. Closure is representation-independent

Packet Closure must not require a native stack image.

Equivalent representations may include:

```text
serialized runtime frame
code + input bindings
code + memoized effects
Artifact graph
Event history + snapshot
Corpus references
content-addressed objects
human-readable continuation packet
```

This preserves the parent paper's Side/replay insight:

> **the future of a computation may be reconstructed rather than serialized when reconstruction is cheaper or more portable.**

The invariant is resumption closure, not one storage representation.

## 3. Packet identity, historical truth and travelling state

The architecture should distinguish four objects that are easy to collapse accidentally:

```text
Packet Identity
    stable identity of the computational/cognitive work

Historical Truth
    Events and Artifacts establishing what occurred

Packet Snapshot
    materialized current state derived from that history

Packet Capsule
    bounded travelling representation required for the next hop
```

The Capsule carries a **causal frontier** stating which portion of history its snapshot represents.

A handler can then determine whether the Capsule is sufficient or whether additional state must be materialized before execution.

This prevents the network packet from growing recursively with its entire history.

## 4. A richer memory model

The parent paper already reverses the priority between RAM and persistent memory.

Packet Placement makes that model operational.

A packet can occupy several memory tiers without changing identity:

```text
RAM / local cache
local SQLite working store
principal durable SQL store
Git/GitHub Corpus placement
cold archive
posterity/offline preservation
```

The architecture should therefore distinguish:

```text
logical store
    the semantic role of the store

physical binding
    SQLite / PostgreSQL / Supabase / Git / object store / archive technology

placement
    the fact that packet state currently exists there
```

This allows technology replacement without redefining computation.

## 5. Store capabilities rather than one universal storage API

Different memory substrates are not equivalent.

The abstract machine should reason in terms of capabilities such as:

```text
ObjectStore
EventStore
SnapshotStore
SearchStore
IndexStore
ArchiveStore
TransactionalStore
SubscriptionStore
```

with characteristics such as latency, durability, sovereignty, cost, retention and transactional semantics.

A storage resolver can then choose or materialize a placement according to packet constraints.

This makes storage another heterogeneous capability field rather than a hidden runtime implementation detail.

## 6. Granularity becomes a computational decision

A Continuation Packet should become independently identifiable when some work can usefully be:

```text
routed
resumed
authorized
budgeted
retried
cancelled
branched
returned
reused
archived
```

The granularity of the architecture is therefore not the CPU instruction and not necessarily the function call.

It is the **smallest useful independently governable continuation of work**.

Local micro-operations may remain ordinary von Neumann execution. JHN Architecture becomes visible when an execution boundary deserves durable independent identity.

## 7. Event/effect/event and the commit boundary

The current abstract machine groups Events and effects together. That is too coarse once packets can cause real external consequences.

A safer transition is:

```text
Event
→ packet handling
→ EffectIntent
→ authority / budget / policy validation
→ commit through a capability
→ EffectReceipt
→ observation Event
```

This provides an explicit commit boundary under retries, branching and revocation.

A provisional effect model can distinguish:

```text
planned
prepared
authorized
committed
failed
compensated
observed
```

where appropriate.

The architecture must not imply that every computation is transactional. The point is that consequential effects can be explicitly governed when required.

## 8. Four orthogonal state graphs

The distributed machine should preserve at least four graphs:

```text
Authority graph
    who may cause what on whose behalf

Causal graph
    what event/decision/effect produced what next event

Execution graph
    which handlers/capabilities/providers actually processed the work

Custody graph
    where the state was placed, replicated, archived and restored
```

These graphs intersect at the Cognitive Packet but remain semantically distinct.

This is essential for responsibility in a machine whose executor, storage and provider may all change during one Odyssey.

## 9. Revised abstract machine

The parent paper provisionally defines:

`J = (P, A, K, M, B, T)`

The packet-native refinement can be represented provisionally as:

`J* = (P, C, A, S, K, M, G, B, T, X)`

where:

- `P` — active Cognitive Packets / continuations;
- `C` — closure and causal-frontier state;
- `A` — available capabilities / actors;
- `S` — logical stores, physical bindings and placements;
- `K` — persistent knowledge, Events and Artifacts;
- `M` — local volatile working sets and caches;
- `G` — governance, authority and mandate state;
- `B` — resource budgets and accounting constraints;
- `T` — trace, lineage and provenance;
- `X` — outstanding external EffectIntents, receipts and observed consequences.

A transition becomes conceptually:

```text
select / attract packet p
→ materialize closure if necessary
→ resolve admissible handler capability
→ execute locally or remotely
→ emit Artifacts / Events / downstream packets
→ stage governed effects where necessary
→ update placements and causal frontier
→ return/assimilate when appropriate
```

The exact tuple is not normative. Its purpose is to expose state that a process-local architecture can keep implicit but a distributed packet architecture cannot.

## 10. Why this is beyond von Neumann without replacing von Neumann

The comparison should remain disciplined.

A von Neumann machine answers efficiently:

```text
Given local state and a program counter,
which instruction transforms memory next?
```

JHN Architecture asks at a different scale:

```text
Given independently continuable work,
where is its closure,
which admissible capability can advance it,
under whose authority,
with which resources,
through which effect boundary,
and where must its yield return?
```

The local handler may still be an ordinary von Neumann machine.

The proposed post-von-Neumann move is therefore not transistor-level replacement. It is a change in the **canonical unit and locus of computational continuity**:

```text
from:
    machine-local instruction stream + RAM

toward:
    packetized continuation + materializable closure
    + distributed capability field + persistent memory field
```

## 11. Relationship to the Learning Computer

JHN Architecture provides the general computational substrate.

*The Network is the Learning Computer* adds the cognitive cycle:

```text
packet journey
→ return to Ithaca
→ assimilation
→ changed future packetization/routing/handling
```

The Reactive Corpus supplies durable semantic memory.

COP supplies the operational protocol for events, continuations, authority, routing, accounting and effects.

Thus:

```text
JHN Architecture
    general packet/continuation machine

Cognitive Packet Switching
    packet-centric cognitive specialization

COP
    operational protocol/runtime semantics

Reactive Corpus
    durable changing semantic environment

Learning Computer
    architecture in which assimilated journeys alter future cognition
```

## 12. Agile validation path

The architecture should now be tested through successive boundary crossings rather than broadened speculatively.

### Test A — process boundary

Resume a closed packet after destroying all volatile handler state.

### Test B — store boundary

Move one packet from local SQLite to PostgreSQL/Supabase while preserving identity and closure.

### Test C — node boundary

Resume that packet on another node with no undocumented state from the first node.

### Test D — effect boundary

Execute one idempotent governed external effect through EffectIntent/EffectReceipt; prove retries and mandate changes are handled correctly.

### Test E — Corpus boundary

Promote an operational packet to a Git/GitHub Corpus placement without changing packet identity.

### Test F — time boundary

Archive, remove hot copies, restore later, reconstruct authority and resume or inspect the packet.

Each failed test should produce explicit **residue** describing what the current abstract machine could not represent.

That residue is architectural evidence.

## 13. Research consequence

Packet Closure strengthens the main JHN Architecture hypothesis because it identifies the hidden assumption behind machine-local continuations: shared reachable state.

Removing that assumption forces memory, storage, causality, authority and effects into the architecture.

This gives a concrete research program:

> **Discover which concepts become unavoidable when the future of computation is required to survive location, process, handler, provider, storage and time.**

Cognitive Packet Switching is not only an application of that architecture. It is one of the principal experimental methods by which the architecture can be discovered.
