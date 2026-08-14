---
title: "JHN Architecture — A Packet/Continuation Computational Architecture"
subtitle: "Beyond machine-local execution: continuations, capabilities, persistent memory and distributed branching"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-08-14"
last_modified_at: "2026-08-14"
last_stamped_at: "2026-08-14T00:00:00.000Z"
status:
  - "working-paper"
  - "under-review"
version: "0.2"
license: "CC BY-SA 4.0"
language: "en"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/jhn_architecture.md"
document_role: "source"
document_kind: "working-note"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
  - "GPT-5.6 Sol (drafting and structuring)"
provenance:
  origin_type: "unknown"
  origin_repository: "unknown"
  origin_ref: "unknown"
  origin_date: "unknown"
  derived_from: []
review:
  status: "unreviewed"
  reviewed_by: []
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "research/potentics.md"
  - "research/potentics_the_possible_addendum.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/alan_turing_mcp.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packet_switching.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-kernel/src/continuation.js"
  - "https://github.com/JeanHuguesRobert/Inox/blob/master/research/fractanet_language_abstractions.md"
  - "https://github.com/virteal/side"
tags:
  - jhn-architecture
  - continuations
  - packets
  - fractanet
  - alan
  - side
  - persistent-memory
  - distributed-computing
  - branching
  - rational-exploration
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "working-note"
classification_confidence: "medium"
changelog:
  - "v0.1 (2026-08-14) — initial architectural working note."
  - "v0.2 (2026-08-14) — corrected frontmatter and explicitly marked the document under review and unreviewed under the Redactor/Reviewer contract."
---

# JHN Architecture

## A Packet/Continuation Computational Architecture

## 0. Status and claim discipline

This note defines an architectural hypothesis and a research program.

The phrase **JHN Architecture** names the proposed architecture for the purpose of discussion and traceability. It is not yet a claim of historical uniqueness comparable to the established status of the von Neumann architecture. Such a claim would require systematic prior-art comparison, formal semantics, implementations, benchmarks and independent evaluation.

The proposed shift is nevertheless explicit:

> **A computation should not fundamentally belong to the machine currently executing it. Its future should be representable as a packet that can remain local, persist, travel, branch, compete, recombine and resume wherever suitable capability exists.**

Short form:

```text
The Network is the Computer — when continuations can travel, branch and recombine.
```

---

## 1. Contrast with the conventional machine model

A simplified von Neumann-style abstraction is:

\[
(Memory, PC, Instruction) \rightarrow (Memory', PC')
\]

The machine-local program counter selects a next instruction operating over machine-local working memory.

The JHN architecture proposes instead a distributed transition model:

\[
(Packet, PersistentState, AvailableCapabilities, Context)
\rightarrow
\{Packet'_1, Packet'_2, \ldots, Packet'_n\}
\]

The important changes are:

- there need not be one globally privileged program counter;
- the future of a computation can be explicit and portable;
- the next executor need not be known when the continuation is created;
- one continuation may resolve through zero, one or many branches;
- branches may use heterogeneous capabilities and substrates;
- results may be selected, merged, synthesized, abandoned or retained as reusable artifacts;
- machine-local volatile state is an optimization, not the canonical home of durable computational state.

This is not an argument that von Neumann machines disappear. They remain highly efficient local substrates on which parts of the architecture may execute.

---

## 2. Core primitive: the Continuation Packet

A **Continuation** represents what remains possible or required for a computation to proceed.

In the JHN architecture:

> **A continuation is canonically representable as a Packet.**

This does not require every local continuation to be serialized eagerly. The packet is the exchangeable and persistent form, not necessarily the permanent in-memory representation.

A continuation packet may carry or reference:

```text
intent
resume semantics
input bindings
state references
required or desired capabilities
constraints
mandate / authorization context
budget and cost bearer
deadline / TTL
provenance
trace references
branch / parent lineage
acceptance conditions
merge / synthesis policy
```

A continuation may therefore survive:

```text
process exit
machine reboot
provider replacement
network partition
runtime migration
human delay
agent replacement
```

provided its required state and semantics remain reconstructible.

---

## 3. Direct style without RPC semantics

The architecture does not require programmers or LLMs to write explicit continuation-passing style.

Alan provides the intended reconciliation:

```alan
weather = mcp weather.forecast location="Corte"
plan = call optimize weather=$weather
approval = mcp human.approve proposal=$plan
result = mcp energy.execute plan=$plan
return result=$result
```

This resembles ordinary direct-style procedure calls, but the effectful operations have continuation semantics:

```text
need capability
→ suspend if necessary
→ expose/persist continuation
→ resolve policy and routing
→ obtain admissible result
→ resume
```

The syntax may resemble RPC. The semantics do not assume that a remote call is equivalent to a local call.

---

## 4. Branching as a first-class operation

A continuation need not resolve through a single path.

\[
C \rightarrow \{C_1, C_2, \ldots, C_n\}
\]

Branches may execute:

```text
locally
on another CPU
on a GPU
on another Fractanet node
through a database query
through symbolic reasoning
through an LLM
through a human
through an organization or institution
through a physical sensor or actuator
```

They may differ in algorithm, language, cost, latency, confidence, energy consumption or trust properties.

A branch policy may specify for example:

```text
first-success
race
all
quorum
best-under-budget
highest-confidence-before-deadline
compare-and-synthesize
explore-until-marginal-value-below-threshold
```

This gives the architecture a relationship to parallel logic programming and speculative execution, but the search space is not restricted to logical proofs or homogeneous processors.

---

## 5. Synthesis, not only selection

Branching is useful even when one branch eventually wins, but the stronger case is **synthesis**.

A resolver may produce an output that existed in no branch separately:

\[
S(C_1, C_2, \ldots, C_n) \rightarrow C'
\]

Examples include:

```text
combine several partial proofs
merge independent observations
reconcile conflicting estimates
compose capabilities from several actors
use one branch to criticize another
combine symbolic and neural results
combine machine computation and human judgment
```

This connects directly to Potentics: exploration may reveal and synthesis may create new effective capabilities, thereby changing which possibles become accessible next.

---

## 6. Memory model: persistent by default, volatile locally

The architecture reverses the usual conceptual priority between RAM and persistence.

Machine-local RAM is treated primarily as:

> **a localized optimization for access to a larger persistent computational memory.**

The canonical durable state may live in heterogeneous substrates:

```text
Artifacts
Events
content-addressed objects
SQL rows
Geo Time Series
git objects
object stores
logs
human or institutional records
other trustworthy persistent stores
```

A local execution activates a working set:

\[
PersistentState
\rightarrow
LocalWorkingSet
\rightarrow
Transformation
\rightarrow
PersistentState'
\]

If the local working state can be reconstructed from persistent state and trace, loss of RAM or loss of one machine need not imply loss of the computation.

"Persistent" does not mean immortal. The architecture requires explicit consolidation, obsolescence, forgetting and garbage collection.

---

## 7. Side: replay and memoization as a fast path

The historical `virteal/side` work provides an important performance principle.

Side allowed asynchronous JavaScript code to retain a synchronous face by:

```text
attempt computation
→ block on unresolved read
→ abandon current run
→ cache the asynchronous result when available
→ replay from the beginning
→ reuse memoized prior results
→ advance until the next unresolved dependency
```

The key consequence for JHN Architecture is:

> **A continuation need not always be stored as a full serialized runtime frame. It may be reconstructed by deterministic replay over memoized results when that is cheaper.**

Equivalent continuation representations may therefore include:

```text
local runtime frame
serialized continuation packet
code + inputs + memoized effect results
stable artifact/reference graph
```

This suggests two optimization rules:

```text
materialize continuations lazily
prefer reconstruction over serialization when cheaper
```

Side also anticipates controlled effect semantics: delayed writes, reversible effects and once-only effects. These map naturally to provisional computation followed by explicit commit.

---

## 8. Locality and the cost of distribution

"The Network is the Computer" must not mean "everything goes over the network".

The architecture should prefer the cheapest admissible capability according to locality and constraints.

A conceptual hierarchy is:

```text
same execution frame
same process
same machine
nearby machine
local Fractanet
remote Fractanet
Internet service
human / institution / distant physical capability
```

A resolver may approximate:

\[
Resolve(C)=\arg\min_{k\in Capabilities(C)} Cost(C,k)
\]

subject to constraints such as:

```text
mandate
security
privacy
quality
confidence
latency
energy
financial budget
availability
jurisdiction
reversibility
```

The common case may therefore remain a very fast local call. Distribution is a capability of the semantics, not a tax that must be paid on every step.

---

## 9. Capability attraction rather than fixed addressing

The continuation should preferably describe **what capability is required**, not which machine must perform it.

This permits:

```text
late binding
provider substitution
anti-capture redundancy
failover
competition
locality-aware execution
specialist discovery
```

Fractanet `Packet Attractors` extend this further: capable and legitimate processors may advertise or attract packets they can handle, reducing dependence on a central scheduler.

The resulting system resembles an ecology of capacities more than a cluster controlled by one global dispatcher.

---

## 10. Control, responsibility and budget are part of execution

A distributed computational architecture that can invoke humans, agents and physical capabilities cannot treat governance as an external afterthought.

Continuation packets should be able to carry:

```text
mandate
rights
responsibility chain
budget
cost bearer
policy
provenance
trace obligations
human validation requirement
```

Alan's existing invariant applies:

```text
Tool availability is not authorization.
Authorization is not execution.
```

Similarly:

```text
No compute without budget.
No budget without bearer.
No bearer without mandate.
No mandate without trace.
```

These are not necessarily mandatory fields for every microscopic local operation; they are architectural capabilities that become explicit where consequences require them.

---

## 11. Garbage collection, obsolescence and memory temperature

A persistent computational memory must not retain every intermediate state forever.

The system therefore needs governed lifecycle operations such as:

```text
promote
cool
summarize
supersede
obsolete
freeze
forget
garbage-collect
```

The generalized collection decision is richer than ordinary heap reachability:

\[
GC = f(reachability, utility, evidentiary\ value, reconstructibility, cost, policy)
\]

Raw traces may be summarized into stable artifacts; dead branches may become obsolete; reconstructible caches may be discarded; legally or historically significant evidence may remain retained.

This keeps persistence compatible with entropy, finite resources and continuous change.

---

## 12. Relation to Potentics

Potentics is independent of this architecture, but the architecture can be understood as one computational implementation of Rational Exploration of The Possible.

A minimal correspondence is:

```text
possible continuation
→ candidate path
branch
→ exploration of several candidate paths
capability resolution
→ mobilization of available potential
result artifact
→ stabilized realization
synthesis
→ composition producing new capability
new continuation set
→ changed accessible possible
```

The loop is:

\[
Possible\ Continuations
\rightarrow
Exploration
\rightarrow
Synthesis
\rightarrow
Realized\ Artifacts/Events
\rightarrow
New\ Capabilities
\rightarrow
New\ Possible\ Continuations
\]

This relation is a research hypothesis, not a requirement that Potentics depend on JHN Architecture.

---

## 13. Components and their roles

The architecture currently emerges across several existing projects. Their roles should remain distinct:

```text
Alan
  direct-style authoring with continuation semantics

Cognitive Packets / COP
  exchangeable envelopes, traces, artifacts, continuation lineage

Side
  replay, memoization and controlled-effect fast-path ideas

Fractanet
  distributed field of capabilities and packet routing/attraction

Inox
  target sovereign language/runtime and adapter surface

Cogentia
  cognitive and institutional use of the architecture

Potentics
  general science of Rational Exploration of The Possible
```

None of those components alone is the JHN Architecture.

---

## 14. Minimal abstract machine

A first abstract state can be represented as:

\[
\mathcal{J} = (P, A, K, M, B, T)
\]

where provisionally:

- \(P\): active packets/continuations;
- \(A\): available capabilities/actors;
- \(K\): persistent knowledge and artifacts;
- \(M\): local volatile working sets/caches;
- \(B\): budgets, mandates and execution constraints;
- \(T\): trace and lineage state.

A transition chooses or attracts a packet \(p\), resolves one or more admissible capabilities, and produces:

\[
(p, \mathcal{J})
\rightarrow
(E, O, P', K', T')
\]

where:

- \(E\) is the set of emitted Events/effects;
- \(O\) is the set of resulting Artifacts/observations;
- \(P'\) is zero, one or many continuation packets;
- \(K'\) and \(T'\) are updated persistent knowledge and trace.

The model deliberately permits branching and termination:

\[
|P'| \in \{0,1,2,\ldots\}
\]

A later version should formalize equivalence between local-frame, serialized and replay-reconstructed continuation representations.

---

## 15. Research questions before stronger claims

Before presenting JHN Architecture as historically novel, compare it rigorously with at least:

```text
Actor Model
CSP and π-calculus
dataflow machines
Linda / tuple spaces
continuation-passing and delimited continuations
mobile code and process migration
Erlang/BEAM
Oz/Mozart
distributed logic programming
blackboard systems
workflow engines / durable execution
futures/promises and async/await
speculative execution
serverless orchestration
content-addressed and event-sourced systems
```

Questions to answer include:

1. Which combination of properties is genuinely distinctive?
2. What is the minimal formal semantics?
3. Can direct-style Alan programs compile to the abstract machine without semantic ambiguity?
4. When is replay cheaper than continuation serialization?
5. How are irreversible effects committed exactly once under branching and retries?
6. How are branch budgets allocated and reclaimed?
7. How is synthesis represented and audited?
8. What consistency guarantees are required of persistent memory?
9. How much of RAM can practically be treated as reconstructible cache?
10. What benchmarks show useful performance against conventional orchestration models?

---

## 16. Initial falsifiable implementation target

A useful first demonstration should not attempt to replace a general computer.

Implement one Alan/COP computation that:

```text
starts in direct style
branches into at least three heterogeneous resolvers
executes at least one branch remotely
memoizes/replays at least one expensive read Side-style
survives termination of the initiating process
reconstructs or reloads its continuation
merges or synthesizes branch outputs
commits one controlled side effect
records complete lineage and cost
```

Then compare:

```text
latency
serialization overhead
replay overhead
network traffic
failure recovery
traceability
cost
implementation complexity
```

against an equivalent conventional local/RPC/workflow implementation.

That experiment would turn the architecture from a conceptual proposal into an engineering object.