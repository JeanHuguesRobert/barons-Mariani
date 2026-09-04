---
title: "Potentics of Compute — RAIX Collective-Capability Addendum"
subtitle: "From nominal node power to realizable collective capability"
description: "Addendum connecting Potentics of Compute to the corrected RAIX concept: arrays may aggregate useful compute as well as provide redundancy, and their gain should be measured per bounded workload class."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
date: "2026-08-22"
last_modified_at: "2026-09-04"
version: "0.1"
status: "integrated"
license: "CC BY-SA 4.0"
language: "en"
document_role: "source"
document_kind: "research-addendum"
visibility: "public"
lifecycle_state: "working"
methodology:
  - "Second Method"
  - "Potentics"
  - "Reactive Corpus semantic propagation"
related_documents:
  - "research/potentics_of_compute.md"
  - "research/the_network_is_the_learning_computer.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/raix.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractanet.md"
tags:
  - potentics
  - raix
  - distributed-compute
  - collective-capability
  - capacity-gain
  - heterogeneous-compute
  - edge-ai
---

# Potentics of Compute — RAIX Collective-Capability Addendum

## 1. Why this addendum exists

`Potentics of Compute` already distinguishes nominal physical resources from the useful, continuous and controllable capacity that organization can actually deliver. The 2026-08-22 RAIX consolidation sharpens one consequence:

> **RAIX is not only a redundancy mechanism. An organized array may create useful compute capacity unavailable to any individual participating node.**

This does not create arithmetic ex nihilo. It changes which workloads become realizable and at what delivered utility.

On 2026-09-04, this addendum was fully integrated into the canonical paper [`research/potentics_of_compute.md`](potentics_of_compute.md) (v0.4, see Sections 3.5, 3.6, 6.5, 9.1, 9.2, 10, 12, and 13), resolving GitHub issue `JeanHuguesRobert/barons-Mariani#36`. This note is preserved for provenance and historical reference.

## 2. Nominal versus realizable collective capacity

For a bounded workload class `T`, let nodes expose individual capability profiles `C_i(T)`.

The relevant Potentics object is not merely:

\[
\sum_i nominal\ compute_i
\]

but a deliverable collective capability:

\[
C_{collective}(T)=F_T(C_1,\ldots,C_n,network,state,coordination,trust,energy)
\]

Depending on the workload:

\[
C_{collective}(T) > \max_i C_i(T)
\]

may hold because memory, throughput, specialized operations or independent subproblems can be composed across nodes.

It may also fail badly. Communication, state transfer, synchronization, verification and trust costs can erase the apparent benefit.

The proposition is therefore experimentally falsifiable rather than architectural doctrine.

## 3. RAIX gain as an experiment-local instrument

For a declared utility function `U` and task class `T`, define:

\[
G_{RAIX}(T)=\frac{U(RAIX\ configuration,T)}{U(best\ available\ individual\ configuration,T)}
\]

`U` must be declared before measurement. Depending on the experiment it may include:

- delivered throughput;
- latency;
- probability of successful completion;
- maximum executable model or working set;
- energy per useful result;
- monetary cost;
- verification cost;
- independence from a provider or jurisdiction;
- reversibility;
- human attention cost.

`G_RAIX` is not a universal scalar and should not be added to canonical Potentics as though it were one. It is an experiment-local comparison instrument.

A result below one is useful evidence.

## 4. Hardware trend as an experimental opportunity

The rapid 2026 evolution of low-cost MCUs and edge AI devices reduces the economic cost of forming heterogeneous arrays. ESP32-class RISC-V devices, ESP32-P4-like compute nodes, inexpensive NPU boards, SBCs, older PCs and local GPUs increasingly occupy a continuous capability spectrum rather than separate worlds.

This makes small bounded experiments possible without assuming that a globally distributed Fractanet must first exist.

A useful first ladder is:

```text
MCU / smart sensor
→ AI-capable MCU
→ small NPU edge node
→ SBC
→ desktop / local GPU
→ remote provider
```

The research question is not which rung is universally best. It is which composition produces the highest useful capacity under the declared regime and constraints.

## 5. Candidate bounded experiments

### E1 — Memory-wall experiment

Choose a workload that cannot fit on one cheap node but can be partitioned across several. Measure whether the collective configuration crosses the wall at acceptable latency, energy and coordination cost.

### E2 — Throughput experiment

Use independent inference or transformation packets and compare one stronger node against several weaker nodes at similar purchase cost and energy envelope.

### E3 — Heterogeneity experiment

Route different stages to different comparative advantages: MCU real-time preprocessing, NPU inference, CPU irregular logic, GPU dense operations.

### E4 — Trust-cost experiment

Repeat the same computation across independently governed resources and measure when verification redundancy consumes the economic gain. This directly tests the existing `Potentics of Compute` hypothesis that trust cost may be binding.

### E5 — Learned composition experiment

Allow routing/composition policy to use observations from previous runs. Test whether assimilation improves future `G_RAIX` without creating unacceptable opacity, lock-in or correlated capture.

## 6. Connection to Compute Weather

Compute Weather can forecast not only isolated availability but **composition opportunity**.

A future state estimate may say, for example:

```text
local solar surplus: high
three edge NPUs: idle
home uplink: degraded
GPU workstation: unavailable
remote provider: expensive
```

The meaningful output is not merely a price forecast. It may change which RAIX configuration is realizable and desirable for the next packet population.

Thus the capacity forecast should ultimately be capable of answering:

> **What useful collective configurations are likely to be realizable during this horizon?**

## 7. Strong falsifier

The RAIX compute hypothesis should be narrowed aggressively if, across the task classes that matter to Fractanet, the combined costs of communication, coordination, trust, state movement and energy consistently make `G_RAIX ≤ 1` compared with ordinary concentrated compute.

The purpose is not to defend distributed low-cost compute. It is to discover its real envelope.
