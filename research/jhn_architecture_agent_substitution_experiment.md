---
title: "JHN Architecture Experiment — Portable Continuation Across Agents and Nodes"
subtitle: "A falsifiable test of capability substitution without loss of authority, identity or causal lineage"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-08-15"
status:
  - "working-paper"
  - "under-review"
version: "0.1"
license: "CC BY-SA 4.0"
language: "en"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/jhn_architecture_agent_substitution_experiment.md"
document_role: "source"
document_kind: "experimental-protocol"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
  - "GPT-5.6 Sol (drafting and structuring)"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_date: "2026-08-15"
  derived_from:
    - "research/jhn_architecture.md"
    - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/Terminology.md"
    - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/magistral/CAPABILITY_RESOLUTION.md"
review:
  status: "unreviewed"
  reviewed_by: []
update_policy: "UP-DEFAULT-REVIEWED"
tags:
  - jhn-architecture
  - continuation
  - capability-resolution
  - agent-substitution
  - fractanet
  - cop
  - magistral
  - reproducibility
---

# JHN Architecture Experiment — Portable Continuation Across Agents and Nodes

## 0. Purpose

This document defines a concrete, falsifiable experiment for a central claim of the JHN Architecture:

> **A computation should not fundamentally belong to the machine or proprietary agent session currently executing it.**

The experiment tests whether useful cognitive work can be suspended after execution by one coding
agent, externalized into persistent state, and resumed by a different coding agent on another
execution node without losing the authority, identity, budget, or causal lineage of the work.

It does not attempt to prove the JHN Architecture as a whole.

## 1. Architectural hypothesis under test

The parent architecture proposes a distributed transition model of the form:

```text
(Packet, PersistentState, AvailableCapabilities, Context)
  -> zero, one, or many successor Packets
```

For this experiment, the strong operational hypothesis is:

> **Changing the HandlerInstance and execution node need not change the durable computation.**

The computation is considered durable only to the extent that its required continuation state is
recoverable from explicit Fractanet/COP state rather than inaccessible vendor-session memory.

## 2. Separation of identities

The experiment MUST distinguish at least:

```text
Principal
Mandate
LogicalAgent
CapabilityRequirement
HandlerProfile
HandlerInstance
Execution node
Vendor session
CapabilityInvocation
Continuation
Artifacts
Events / causal lineage
```

A change in any of the following:

```text
Codex -> Claude
Claude -> Grok
machine A -> machine B
ACP -> CLI compatibility adapter
```

MUST NOT, by itself, imply a change of Principal, LogicalAgent, Mandate, or task identity.

Compact invariants:

> **Capability is not authority.**
>
> **Communication is not authority.**
>
> **Execution is not identity.**

## 3. Roles of COP, Magistral and Fractanet

The experiment adopts the following implementation decomposition:

```text
COP
  orchestrates work and preserves causal state

Magistral
  resolves and presents required capabilities

Fractanet
  makes heterogeneous capabilities present
```

COP expresses the work and the `CapabilityRequirement`.

Magistral selects an admissible capability offer and InvocationAdapter.

Fractanet supplies the actual node, runtime, agent, service, or other executor.

## 4. Initial capability class

The first tested capability is:

```yaml
capability: coding-agent
```

Candidate offers may include:

```text
Codex
Claude Code
Grok Build
Goose
other compatible coding agents
```

Access may use ACP when available, or a compatibility CLI adapter where necessary. The transport or
interaction protocol is not itself part of the architectural hypothesis.

## 5. Portable work package

Before first execution, the work MUST be representable without relying on a pre-existing vendor
session.

A minimal package SHOULD identify or carry:

```text
goal / acceptance criteria
repository identity and base revision
writable scope
relevant source/context references
current continuation
mandate reference
budget / cost bearer
constraints
prior decisions
trace / parent event references
required capability
```

The exact wire schema is intentionally left to COP implementation work.

## 6. Experimental sequence

### Phase A — initial materialization

1. Create or select a bounded coding task with objective acceptance criteria.
2. Persist its COP Topic/Task/Continuation state.
3. Express a provider-neutral `CapabilityRequirement: coding-agent`.
4. Magistral resolves the requirement to HandlerInstance A on node A.
5. Node A materializes only the working set required for execution.

### Phase B — first execution

6. HandlerInstance A performs a bounded part of the task.
7. Record consequential actions as COP Events/Artifacts.
8. Produce a continuation checkpoint that explains what remains to be done.
9. Persist repository changes or other outputs in a reconstructible form.
10. Terminate HandlerInstance A and make its private session state unavailable to the next executor.

### Phase C — substitution

11. Re-submit the remaining `CapabilityRequirement` to Magistral.
12. Resolve it to HandlerInstance B using a different coding agent and, where practical, another node.
13. Materialize the required working set from persistent state.
14. Resume from the portable continuation without access to HandlerInstance A's proprietary history.
15. Complete another bounded step or the whole task.

### Phase D — reconstruction

16. Replay the COP event chain.
17. Reconstruct which Principal and LogicalAgent authorized the work.
18. Reconstruct both HandlerInstances and CapabilityInvocations.
19. Reconstruct repository/artifact lineage and continuation transitions.
20. Verify budget and mandate continuity across substitution.

## 7. Success criteria

The experiment succeeds only if all of the following hold:

1. **Task continuity** — HandlerInstance B can continue useful work rather than restart from scratch.
2. **Agent independence** — B does not require private vendor-session state from A.
3. **Node independence** — the task can move to another execution node when materialization is possible.
4. **Authority continuity** — substitution does not silently create or change authority.
5. **Identity continuity** — the durable LogicalAgent remains distinguishable from both executors.
6. **Causal reconstruction** — COP replay explains the chain from original task through both invocations.
7. **Artifact integrity** — inputs and outputs used by B are identifiable and reconstructible.
8. **Budget continuity** — costs remain attributable to the same or explicitly changed bearer/mandate.
9. **Vendor reversibility** — no vendor becomes indispensable merely because it executed an earlier step.

## 8. Failure modes that falsify or weaken the hypothesis

The experiment SHOULD explicitly record failures such as:

```text
continuation lacks information needed by the second agent
working state exists only in a vendor conversation
repository materialization depends on undeclared machine-local files
credentials or tools are inseparable from one workstation
agent B must reconstruct large amounts of hidden history manually
causal links cannot explain a consequential change
budget or mandate attribution is lost during substitution
ACP/CLI adapter semantics cannot preserve required events
```

A failure is useful evidence. The objective is not to make the architecture appear successful but to
identify what portable computation actually requires.

## 9. Measurements

At minimum record:

```text
time to materialize node A
time to checkpoint A
time to materialize node B
time for B to regain productive context
bytes / artifacts transferred
amount of context supplied to B
number of missing-state repairs
vendor-specific state required after checkpoint
cost by capability invocation
acceptance-test outcome
```

A useful comparison baseline is the same task continued inside the original vendor session.

The portability tax can then be estimated rather than assumed away.

## 10. Stronger variants

If the basic experiment succeeds, progressively test:

```text
same agent / different node
different agent / same node
different agent / different node
different execution protocol
network interruption and delayed continuation
parallel branching to several agents
compare-and-synthesize result policy
partial workspace materialization instead of full repository checkout
Inox-mediated capability materialization and routing
```

The strongest useful demonstration is not merely migration but heterogeneous branching and synthesis.

## 11. Relationship to anti-capture

A vendor session may remain a valuable local optimization. The experiment does not require avoiding
session state.

It requires only that, where portability is claimed:

> **A vendor session MAY accelerate continuation; it MUST NOT be the only representation from which useful continuation can be recovered.**

This converts anti-vendor-capture from a policy preference into a testable architectural property.

## 12. Academic role

The JHN Architecture parent document intentionally maintains strong claim discipline. This experiment
is one step toward the implementation and benchmark evidence required before stronger architectural
claims can be made.

A positive result would demonstrate one concrete property:

> portable continuation across heterogeneous intelligent executors with preserved causal and authority state.

It would not establish historical novelty. Results must subsequently be compared with prior work in
durable execution, workflow systems, process migration, actor systems, mobile code, continuation
representations, distributed computing, and contemporary agent protocols.
