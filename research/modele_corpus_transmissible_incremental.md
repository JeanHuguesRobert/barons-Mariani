---
title: "Incremental Transmissible Corpus Model"
subtitle: "Cognitive backtracking, stigmergic traces, and probabilistic exploration of possibilities"
version: "0.2"
status: "working-paper — source document — speculative embryo"
date: "2026-06-13"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
language: "en"
intended_path: "research/modele_corpus_transmissible_incremental.md"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/modele_corpus_transmissible_incremental.md"
issue: "JeanHuguesRobert/barons-Mariani#7"
symmetry: "medium — source candidate, not yet stable"
corpus_role: "source-hypothesis"
corpus_hierarchy:
  level: "speculative-source"
  parent_method: "JeanHuguesRobert/barons-Mariani/research/second_method.md"
  related_repositories:
    - "JeanHuguesRobert/cogentia"
    - "JeanHuguesRobert/inseme"
    - "JeanHuguesRobert/Inox"
    - "JeanHuguesRobert/barons-Mariani"
critique_integrated:
  - "ChatGPT drafting pass, 2026-06-13"
  - "English translation and title normalization, 2026-06-13"
critique_pending:
  - "Grok constructive review — requested next"
intended_derivatives:
  - "short_academic_note"
  - "substack_article"
  - "cogentia_architecture_note"
  - "cognitive_packet_yaml_schema"
  - "COP_exploration_protocol"
  - "research_pitch"
tags:
  - cogentia
  - corpus-source
  - transmissible-corpus-model
  - incremental-model
  - stigmergy
  - backtracking
  - graph-of-thoughts
  - tree-search
  - neuro-symbolic-ai
  - llm-agents
  - cop
  - second-method
  - speculative
  - human-validation
related_documents:
  - "JeanHuguesRobert/barons-Mariani/research/second_method.md"
  - "JeanHuguesRobert/barons-Mariani/research/trace_epistemology.md"
  - "JeanHuguesRobert/barons-Mariani/research/cognitive_waves.md"
  - "JeanHuguesRobert/barons-Mariani/research/stigmergie_sans_limite_haute.md"
  - "JeanHuguesRobert/cogentia/research/conversation_to_corpus_pipeline.md"
  - "JeanHuguesRobert/cogentia/research/cognitive_packets.md"
  - "JeanHuguesRobert/cogentia/research/derived_products.md"
  - "JeanHuguesRobert/inseme/AGENTS.md"
  - "JeanHuguesRobert/inseme/packages/cop-core"
ai_assisted_by:
  - "ChatGPT — drafting, state-of-the-art framing, structure, English version"
  - "Grok — planned external reviewer, non-decisional"
human_validation_required: true
next_action: "Submit to Grok reviewer; then integrate only critiques that improve signal/noise and preserve speculative status."
---

# Incremental Transmissible Corpus Model

## Cognitive backtracking, stigmergic traces, and probabilistic exploration of possibilities

**Jean Hugues Noël Robert**  
Institut Mariani / C.O.R.S.I.C.A.  
1 cours Paoli, F-20250 Corte, Corsica

*Working paper — June 13, 2026 — speculative embryonic source document*

---

## Purpose

This document has a modest but strategic purpose: **to preserve the trace of a research intuition**.

The intuition is the following: current language models can generate, reformulate, approximate, compare, and sometimes explore several possible lines of reasoning. Yet they still lack, or lack sufficiently, a **transmissible corpus represented as an incremental model of exploration**: a versioned source corpus, structured as a graph, annotated by stigmergic traces, exploitable through probabilistic heuristics, and capable of explicitly capitalizing on past explorations.

This document does not claim that the problem has been solved. It claims that the problem deserves attention.

The central question can be formulated as follows:

> What would current models still need in order to reason not merely as sequential text generators, but as cumulative explorers of a graph of possibilities, where each exploration leaves a reusable trace for future explorations?

---

## Associated documents

- [`barons-Mariani/research/second_method.md`](second_method.md) — general methodological doctrine.
- [`barons-Mariani/research/trace_epistemology.md`](trace_epistemology.md) — epistemology of traces and imputability under uncertainty.
- [`barons-Mariani/research/cognitive_waves.md`](cognitive_waves.md) — stigmergic framework for cognitive terrains.
- [`barons-Mariani/research/stigmergie_sans_limite_haute.md`](stigmergie_sans_limite_haute.md) — stigmergic continuity from simple agents to cognitive agents.
- [`cogentia/research/conversation_to_corpus_pipeline.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/conversation_to_corpus_pipeline.md) — conversation-to-corpus pipeline.
- [`cogentia/research/cognitive_packets.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) — transmissible cognitive packets.
- [`inseme/AGENTS.md`](https://github.com/JeanHuguesRobert/inseme/blob/main/AGENTS.md) — bounded mandate, traceability, human validation, agentic continuation.

---

## Assisted genesis note

This document emerged from a conversation on Turbo Prolog, backtracking, neuro-symbolic approaches, and the possibility of representing a living corpus as something more than a documentary archive.

The logical thread was the following:

1. Turbo Prolog recalled an older attempt to industrialize Prolog through typing, compilation, and speed.
2. Backtracking appeared as a conceptual core: exploring branches, returning, and trying otherwise.
3. Purely tree-like exploration proved insufficient once two branches merge or cycles appear.
4. A directed graph therefore appeared as a more accurate technical representation.
5. Stigmergy provided the central mechanism: leaving traces indicating that a branch has already been explored, and what was found there.
6. LLMs were repositioned not as authorities of reasoning, but as probabilistic heuristics able to orient exploration.
7. The transmissible corpus then appeared as a possible class of models: not an additional LLM, but a versioned, exploratory, incremental, and transmissible corpus model.

This document is deliberately speculative. It must not conceal its embryonic status. Its purpose is to preserve the problem, formulate the intuition, locate existing analogues, identify risks, and prepare an external critical review.

---

## Abstract

Large language models have made a powerful form of probabilistic linguistic generation practically usable. They can produce answers, reformulate knowledge, suggest hypotheses, write code, translate intent into plans or queries, and sometimes explore several reasoning paths. However, their dominant architecture remains insufficient for a specific form of reasoning: **the cumulative exploration of possibilities**.

The problem is not only that models hallucinate, lack sources, or sometimes fail to reason. The deeper problem is that they do not possess an external, durable, versioned, and governed space where explorations become transmissible objects. A useful exploration should leave a trace: open branch, suspended branch, refuted branch, branch merged with another one, exploration cost, evidential level, reopening conditions, objections, and sources.

This document provisionally names **Incremental Transmissible Corpus Model** a system in which the source corpus remains sovereign, but is compiled into a directed graph of exploration, stigmergic traces, vector indexes, typed cognitive units, verifiers, and navigation heuristics. The LLM would not be the judge of truth; it would serve as a heuristic function for generation, provisional evaluation, and navigation. Authority would remain distributed among the corpus, sources, tests, rules, human validation, and explicit mandates.

The state of the art already offers several adjacent building blocks: Tree of Thoughts, Graph of Thoughts, Language Agent Tree Search, Reflexion, GraphRAG, blackboard systems, truth maintenance systems, tabled Prolog, continual learning for LLMs, ant colony optimization, and stigmergy. Yet none of these lineages, taken in isolation, seems to provide a complete model of a transmissible, incremental, stigmergic, and governed corpus.

The hypothesis is that this class of models could significantly accelerate intellectual, scientific, legal, political, or technical explorations by relying on the accumulated experience of past explorations. It could transform errors, dead ends, and contradictions into resources. But the path is difficult: node granularity, branch equivalence, trace quality, risks of corpus corruption, maintenance cost, update governance, and empirical evaluation remain open.

---

## Transformation map

```text
initial intuition
→ useful reasoning is not a simple chain of text
→ it resembles a tree-like exploration of possibilities
→ branches can fail, succeed, merge, cycle, or be suspended
→ the apparent tree technically becomes a directed graph
→ each passage must leave a stigmergic trace
→ the trace indicates what was attempted, found, cost, refuted, validated, or suspended
→ the LLM can serve as a probabilistic navigation heuristic
→ the source corpus remains sovereign and versioned
→ the operational model is a compilation of the corpus, not its replacement
→ exploration becomes incremental: each passage improves the following ones
→ possible new class: Incremental Transmissible Corpus Model
```

---

## 1. Problem: current models answer better than they durably explore

Current LLMs are often evaluated by their ability to produce a correct answer to a given query. Even when a model appears to reason, the visible unit usually remains the final answer, or at most an intermediate sequence of justification. This logic is suitable for many tasks, but it fails to represent a longer intellectual activity: exploring a territory of possibilities, capitalizing on dead ends, reopening an old branch, merging two hypotheses, or transmitting to other agents what has already been attempted.

The fundamental lack is not memory in the ordinary sense. Long context, RAG, agent memories, vector databases, and knowledge graphs already exist. The lack is rather an **operational memory of explorations**.

An exploration system should be able to state:

```yaml
branch: "hypothesis X"
status: "suspended"
reason: "insufficient data"
evidence:
  - "source A"
  - "test B"
objections:
  - "possible contradiction with thesis Y"
cost:
  tokens: "high"
  time: "medium"
reopening_condition:
  - "new independent source"
  - "better fusion criterion with hypothesis Z"
```

An ordinary LLM can produce this YAML. But producing a trace is not yet having a system in which such traces are persistent, typed, versioned, reused, corrected, compared, consolidated, and reintegrated into the corpus.

---

## 2. Hypothesis: reasoning as stigmergic exploration of a graph of possibilities

The hypothesis of this document is that some complex forms of reasoning should be treated as graph explorations.

The initial mental schema may remain tree-like:

```text
initial question
├── hypothesis A
│   ├── branch A1
│   └── branch A2
├── hypothesis B
│   └── branch B1
└── hypothesis C
```

But as soon as two branches lead to the same subproblem, or a contradiction forces a return with an enriched state, the tree technically becomes a directed graph:

```text
initial question
├── hypothesis A ──┐
│                  ├── subproblem X
└── hypothesis B ──┘

subproblem X → test → contradiction → hypothesis A' versioned
```

The actual structure is therefore:

> an exploration with a dominant tree-like shape, represented as a directed graph of continuations, annotated by stigmergic traces.

Stigmergy is the mechanism that turns simple exploration into cumulative exploration. A visited branch is not merely traversed; it is marked. The trace modifies future explorations.

In the classical biological case, the trace may be a pheromone. In the cognitive case, the trace should be qualitative: status, proof, objection, cost, confidence, provenance, reopening conditions.

---

## 3. Provisional definition: Incremental Transmissible Corpus Model

The following provisional definition can be proposed:

> An Incremental Transmissible Corpus Model is a system in which a versioned source corpus is compiled into operational representations — exploration graph, stigmergic traces, typed cognitive units, vector indexes, rules, verifiers, and navigation heuristics — in order to accelerate future explorations through explicit capitalization of past experience, without dissolving knowledge into opaque weights.

This definition contains several constraints.

### 3.1 The source corpus remains sovereign

The model does not absorb the corpus in the way a neural training process absorbs data into weights. It produces an operational representation, but that representation must remain derivable from the corpus.

```text
source corpus ≠ operational model
source code ≠ compiled binary
```

The source-code analogy is important. A compiled program may be fast, but it does not replace the source if one wants to understand, correct, fork, audit, or transmit it.

### 3.2 Knowledge is not merely stored; it is situated in branches

A stabilized thesis has a history: it comes from hypotheses, proofs, objections, arbitrations, rejections, reformulations. The model should preserve this history in an exploitable form.

### 3.3 Incrementality concerns how to search

Incrementality does not only mean adding documents. The system gradually learns which branches are fertile, which analogies are misleading, which fusion criteria are robust, which paths consume too much cognitive exergy, and which objections recur.

### 3.4 The LLM is heuristic, not sovereign

The LLM can suggest branches, estimate their promise, reformulate nodes, detect analogies, and produce candidate fusions. But it must not decide truth or stabilization in the corpus by itself.

---

## 4. State of the art: proximities and gaps

This document does not start from nothing. Several traditions have already explored fragments of the problem.

### 4.1 Backtracking, Prolog, and tabling

Logical backtracking is an obvious matrix: one explores a rule, descends, fails or succeeds, then returns. Prolog made this mechanism programmable.

Tabling in logic programming adds an essential dimension: memorizing already called subgoals and their answers in order to avoid recomputation and better handle recursion. This lineage is important because it already addresses two problems central to this document: branch merging and cycles.

Limit: tabling remains defined in a relatively formal logical and computational framework. The model proposed here targets a broader field: hypotheses, objections, texts, partial evidence, dead branches, derivative products, human validation.

### 4.2 Stigmergy and Ant Colony Optimization

Stigmergy, introduced by Pierre-Paul Grassé in relation to termites, designates indirect coordination through traces left in the environment. It has since been extended to multi-agent systems, distributed intelligence, and collective organizations.

Marco Dorigo's Ant Colony Optimization transposes this idea into optimization: agents explore paths and leave pheromone-like traces that probabilistically influence future explorations.

Proximity: probabilistic path selection based on traces.

Gap: in ant colony optimization, the trace is often primarily quantitative. In a transmissible corpus model, the trace should be qualitative, argumentative, sourced, versioned, and governed.

### 4.3 Blackboard systems

Classical AI blackboard systems rely on a shared space updated by different specialized modules. A controller chooses which knowledge sources to activate according to the current state of the blackboard.

Proximity: shared space, partial contributions, opportunistic control.

Gap: the blackboard is not necessarily a versioned, transmissible, auditable, publishable, and forkable corpus. The trace of past explorations is not always a central doctrinal object.

### 4.4 Truth Maintenance Systems

Truth Maintenance Systems preserve the dependencies and justifications of beliefs in order to restore coherence when new information contradicts the current state. They are close to the idea that any conclusion must retain its validity conditions.

Proximity: dependencies, justifications, contradictions, revision.

Gap: the proposed model adds probabilistic exploration, stigmergy, versioned source corpus, and derivative products.

### 4.5 Tree of Thoughts, Graph of Thoughts, and LATS

Tree of Thoughts proposes to move beyond simple token-by-token generation by exploring multiple reasoning units, with self-evaluation, lookahead, and backtracking. Graph of Thoughts generalizes this logic by representing thought units as graph vertices, enabling combination, aggregation, and feedback loops. Language Agent Tree Search combines LLMs, Monte Carlo Tree Search, value functions, and external feedback for agents capable of reasoning, acting, and planning.

Proximity: multiple-path exploration, heuristic selection, backtracking, tree or graph structure.

Gap: these approaches often remain centered on inference for a task or query. The exploration graph is not necessarily preserved as a durable, governed, and transmissible corpus.

### 4.6 Reflexion and textual agent memory

Reflexion proposes that language agents learn from their errors without updating their weights, through a textual memory of experience feedback. This is very close to the principle that an exploration should leave a trace.

Proximity: linguistic feedback, episodic memory, improvement without fine-tuning.

Gap: Reflexion memory is mainly oriented toward agentic performance. The model proposed here aims at a corpus memory, with thesis status, evidential levels, possibility of publication, human review, fork, and transmission.

### 4.7 RAG, GraphRAG, and knowledge graphs

RAG allows a model to consult external documents. GraphRAG or knowledge-graph RAG variants seek to structure retrieval further through entities, relations, and multi-hop paths.

Proximity: externalization of part of the knowledge, structured retrieval, documentary support.

Gap: RAG retrieves content; it does not necessarily preserve explorations as objects. A transmissible corpus model should represent not only documents, but the cognitive acts that transformed those documents into hypotheses, objections, decisions, and derivative products.

### 4.8 Continual learning for LLMs

Continual learning seeks to allow LLMs to adapt to new data, tasks, or preferences without retraining everything and without forgetting previous acquisitions. The major difficulties remain catastrophic forgetting, regression, and update control.

Proximity: incrementality, adaptation, continuity.

Gap: the proposed model partially bypasses the problem by placing the primary increment outside the model weights: in the corpus, graph, traces, and heuristics.

---

## 5. What current models still lack

The lack can be summarized in ten points.

| Lack | Description |
|---|---|
| Persistent space of possibilities | Explored branches do not always become durable objects. |
| Versioned directed graph | Dependencies, fusions, and returns are not represented as a stable structure. |
| Qualitative stigmergic trace | Previous passages are not always marked by status, proof, cost, objection, reopening. |
| Memory of dead ends | Errors and dead branches are not sufficiently capitalized. |
| Explicit scheduler | The system does not sufficiently decide what to deepen, suspend, merge, abandon. |
| Typed cognitive units | The token or paragraph is not enough; one needs fact, hypothesis, objection, proof, branch, continuation. |
| Sovereign source corpus | Opaque weights are not auditable like a versioned corpus. |
| Governed validation | Stabilization decisions lack explicit mandates, statuses, and evidential levels. |
| Non-destructive incremental learning | LLM weights remain difficult to update without drift or forgetting. |
| Transmission/fork/rollback | A model should be reusable, correctable, forkable, auditable, and replayable. |

This table does not imply that every current system lacks everything. It indicates rather that the complete combination remains rare or unstabilized.

---

## 6. Speculative minimal architecture

A minimal architecture could contain the following layers.

```text
1. Versioned source corpus
   Markdown, YAML, documents, references, commits, history.

2. Cognitive-unit extractor
   Facts, hypotheses, objections, proofs, definitions, decisions, continuations.

3. Directed exploration graph
   Nodes, arcs, dependencies, fusions, contradictions, versions, statuses.

4. Stigmergic traces
   Passage, result, cost, confidence, source, reopening condition.

5. Vector indexes and semantic signatures
   Similarities, possible duplicates, analogies, conceptual neighborhoods.

6. Verifiers
   Sources, tests, rules, citations, internal coherence, human validation.

7. Exploration scheduler
   Allocation of cognitive exergy among branches.

8. Heuristic LLM
   Generation, reformulation, provisional evaluation, analogies, objections.

9. Controlled commit
   Stabilization, diff, justification, impact, rollback.

10. Derivative products
    Academic article, Substack post, political note, technical schema, issue, protocol.
```

---

## 7. Typed cognitive units

The model cannot function properly if everything remains undifferentiated text. At least some typed units are required.

### 7.1 Minimal types

```yaml
cognitive_unit_types:
  - fact
  - source
  - hypothesis
  - objection
  - argument
  - counter_argument
  - definition
  - distinction
  - branch
  - continuation
  - contradiction
  - fusion
  - validation
  - derivative_product
  - decision
  - mandate
```

### 7.2 Example branch

```yaml
branch:
  id: "itcm.branch.001"
  title: "Can a transmissible corpus be represented as a model?"
  parent: "itcm.root"
  status: "open_speculative"
  promise: "high"
  risk: "conceptual_overreach"
  explored_by:
    - "JHR"
    - "ChatGPT"
  findings:
    - "Kinship with ToT, GoT, Reflexion, GraphRAG, TMS, ACO."
    - "Central difference: the graph does not disappear after inference; it becomes corpus."
  objections:
    - "Node granularity remains unresolved."
    - "Equivalence between branches is difficult to establish."
    - "Risk of documentary overhead."
  reopening_condition:
    - "Define a minimal YAML schema."
    - "Test on a limited Cogentia sub-corpus."
```

### 7.3 Example stigmergic trace

```yaml
stigmergic_trace:
  id: "itcm.trace.2026-06-13.001"
  branch: "itcm.branch.001"
  event: "initial_formulation"
  result: "source_hypothesis_created"
  status_after_event: "to_review"
  evidence_level: "conceptual_plausibility"
  confidence: "low_to_medium"
  cost:
    attention: "medium"
    technical_debt: "high_if_implemented_too_early"
  next_action:
    - "Grok review"
    - "minimal schema"
    - "micro-prototype on 5 documents"
  warning:
    - "Do not present as solved architecture."
```

---

## 8. The scheduler: core of the model

The critical component is not merely the graph. A graph without an exploration policy becomes a complex archive. The operational core is the scheduler.

It should arbitrate between:

- depth and breadth;
- exploiting a promising branch and exploring a neglected branch;
- reopening an old hypothesis and opening a new one;
- merging two nodes and preserving a distinction;
- temporary abandonment and definitive closure;
- publishing a result and keeping it in internal research.

In the logic of Autonomy of Capability, one could say that the scheduler allocates available **cognitive exergy**.

Possible criteria:

```yaml
scheduler_criteria:
  promise: "probability of producing useful clarification"
  risk: "risk of error, confusion, or capture"
  cost: "time, tokens, attention, maintenance"
  novelty: "degree of real novelty"
  convergence: "ability to merge several branches"
  evidence_gap: "gap between thesis and available evidence"
  derivative_value: "ability to produce useful derivative products"
  strategic_value: "importance for the corpus or action"
  reversibility: "ease of rollback"
  human_validation_need: "need for human arbitration"
```

---

## 9. Possible effects if it worked

### 9.1 Acceleration of explorations

The first effect would be to avoid starting again from zero. Each future exploration would benefit from already opened branches, identified dead ends, recurring objections, and stabilized fusions.

### 9.2 Transformation of errors into resources

A properly traced error becomes a resource. It says: do not restart here without new data; beware of this confusion; this analogy is seductive but false; this branch cost too much for too little gain.

### 9.3 More faithful transmission

A transmissible corpus would transmit not only conclusions. It would transmit paths, hesitations, reasons, statuses, critiques, validations.

### 9.4 Better human / AI articulation

AI would not be charged with deciding; it would contribute to exploration. The human would retain the role of arbitration, mandate, validation, and responsibility.

### 9.5 More coherent derivative products

A Substack article, an academic note, a Facebook response, a technical protocol, or a political proposal could derive from the same source graph without losing the doctrinal core.

### 9.6 Reduction of capture by opacity

A model whose source remains versioned, auditable, and forkable resists capture better than a model whose memory is dissolved into proprietary non-inspectable weights.

---

## 10. Strong objections

### Objection 1 — Documentary cost may suffocate the process

Tracing every exploration may become more costly than the exploration itself.

Provisional response: a signal/noise rule is required. Not everything should enter GitHub. The corpus should preserve stabilizable traces, not every tentative movement.

### Objection 2 — Branch fusion is a difficult problem

Two branches may appear identical while resting on different assumptions. Merging them too early may destroy information.

Provisional response: several statuses should be provided: strong equivalence, partial convergence, analogy, neighborhood, apparent contradiction, real contradiction.

### Objection 3 — The LLM may contaminate traces

If the LLM produces false traces, the system may accumulate toxic memory.

Provisional response: distinguish proposed trace, validated trace, rejected trace. No LLM-generated trace should be sovereign without validation or verification.

### Objection 4 — Incrementality may produce conservative inertia

A system that preserves its traces too well may favor already known paths and reduce radically new exploration.

Provisional response: the scheduler should preserve a quota of low-probability / high-novelty exploration.

### Objection 5 — The model metaphor may be misleading

A versioned corpus, even augmented, is not necessarily a model in the machine-learning sense.

Provisional response: the term model is justified only if the compiled corpus has inference, navigation, update, validation, and transmission functions. Otherwise, one should speak only of an augmented corpus.

### Objection 6 — The risk of self-reference is real

A living corpus may become circular: citing its own traces as justification.

Provisional response: principle of self-containment. The main claims must remain assessable without relying only on internal references.

---

## 11. Current evidential levels

| Element | Status | Evidential level |
|---|---|---|
| LLMs can explore several paths through ToT/GoT/LATS | established in experimental literature | medium to strong depending on tasks |
| Stigmergic traces can guide collective exploration | established in stigmergy / ACO | strong for optimization, weaker for documentary cognition |
| Maintenance systems can handle dependencies and contradictions | established in symbolic AI | medium to strong |
| RAG/GraphRAG externalize part of knowledge | established | strong for retrieval, variable for reasoning |
| A versioned corpus can become an incremental transmissible model | hypothesis of this document | weak to speculative |
| The proposed system would effectively accelerate intellectual explorations | testable hypothesis | not demonstrated |
| The architecture would be sustainable at reasonable cost | critical hypothesis | not demonstrated |

---

## 12. Paths to explore

### 12.1 Minimal YAML schema

Define a minimal schema for:

- branch;
- trace;
- fusion;
- contradiction;
- continuation;
- validation;
- derivative product.

### 12.2 Micro-prototype on a limited corpus

Test on only five documents, for example:

1. `second_method.md`;
2. `trace_epistemology.md`;
3. `stigmergie_sans_limite_haute.md`;
4. `conversation_to_corpus_pipeline.md`;
5. this document.

Objective: determine whether branches, traces, and fusions can be represented without excessive overhead.

### 12.3 Detection of neighboring branches

Use embeddings and LLMs to propose:

- duplicates;
- analogies;
- contradictions;
- candidate fusions;
- reactivable dead branches.

But every fusion should remain a candidate until human validation or an explicit rule.

### 12.4 COP scheduler

Articulate this model with COP: immutable events, durable artifacts, topic-local ordering, deterministic replay, stateless agents, transparency, schema versioning.

A working hypothesis: COP could provide the execution and supervision layer for the exploration scheduler.

### 12.5 Efficiency measures

Possible indicators:

- time required to resume an old project;
- number of contradictions detected;
- number of branches avoided thanks to traces;
- coherence of derivative products;
- ratio of validated fusions to rejected fusions;
- documentary cost per useful clarification;
- ability to replay an exploration.

### 12.6 Comparison with RAG and fine-tuning

Compare three approaches on the same sub-corpus:

1. simple RAG;
2. GraphRAG or knowledge graph;
3. corpus model with exploration traces.

Question: does adding exploration traces actually improve resumption, coherence, and dead-end detection?

---

## 13. Positioning within Cogentia

This document probably sits at the intersection of several layers:

| Layer | Role |
|---|---|
| Cogentia | corpus, cognitive packets, coherence, derivative products |
| COP | orchestration, events, artifacts, continuation, replay |
| Inox | governed execution, capabilities, verbs, controlled composition |
| Ubikia | publication / derivation agent, not sovereign source |
| Barons Mariani | patrimonial, doctrinal, speculative, memorial repository |

The present document belongs to `barons-Mariani` because it still concerns a doctrinal and patrimonial hypothesis about corpus transmission. A more technical derivative could later be placed in `cogentia` or `inseme`, once schemas and invariants are better defined.

---

## 14. Provisional doctrinal formula

> LLMs have shown that a corpus can be absorbed into a statistical model. The complementary path is to make a versioned corpus operational as a model without dissolving it into opaque weights. An Incremental Transmissible Corpus Model does not replace the corpus: it compiles it into an exploration graph, stigmergic traces, cognitive units, and navigation heuristics. Reasoning is no longer a simple chain of text; it becomes a governed exploration of possibilities, accumulating its own passages in order to better orient the next ones.

---

## 15. Proposed prompt for Grok reviewer

```text
Role: critical reviewer, non-decisional.

Document to review:
JeanHuguesRobert/barons-Mariani/research/modele_corpus_transmissible_incremental.md

Review objective:
Evaluate a speculative embryonic source document on the idea of an Incremental Transmissible Corpus Model.

Criteria:
1. Is the speculative status clear enough?
2. Is the thesis sufficiently distinct from RAG, GraphRAG, knowledge graphs, memory agents, and fine-tuning?
3. Is the state of the art properly located, or are important lineages missing?
4. Are the strong objections sufficient?
5. Is the notion of qualitative stigmergic trace defined clearly enough?
6. Is the role of the LLM as a non-sovereign heuristic coherent?
7. Does the document follow the second method: signal/noise, evidential levels, objections, self-containment, human validation?
8. Which passages risk overstatement?
9. Which three improvements would add the most robustness?
10. Which elements should remain open instead of being stabilized too early?

Expected output:
- 10-line synthesis.
- Strong points.
- Fragile points.
- Major objections.
- Restructuring suggestions.
- Missing bibliography.
- Verdict: keep / revise / split / move to cogentia or inseme.
```

---

## 16. Initial bibliography and documentary paths

This bibliography is not stabilized. It serves as a starting point for review.

### Backtracking, Prolog, tabling

- Tamaki, H., Sato, T. (1986). *OLD resolution with tabulation*. Lecture Notes in Computer Science.
- Sagonas, K., Swift, T., Warren, D. S. (1994). *XSB as an efficient deductive database engine*. ACM SIGMOD Record.
- XSB Prolog — https://xsb.sourceforge.net/

### Stigmergy and ant colony optimization

- Grassé, P.-P. (1959). *La reconstruction du nid et les coordinations interindividuelles chez Bellicositermes natalensis et Cubitermes sp. La théorie de la stigmergie*. Insectes Sociaux.
- Theraulaz, G., Bonabeau, E. (1999). *A brief history of stigmergy*. Artificial Life.
- Dorigo, M., Maniezzo, V., Colorni, A. (1996). *Ant System: Optimization by a colony of cooperating agents*. IEEE Transactions on Systems, Man, and Cybernetics.
- Dorigo, M., Stützle, T. (2004). *Ant Colony Optimization*. MIT Press.

### Blackboard systems and truth maintenance

- Erman, L. D., Hayes-Roth, F., Lesser, V. R., Reddy, D. R. (1980). *The Hearsay-II Speech-Understanding System: Integrating Knowledge to Resolve Uncertainty*. ACM Computing Surveys.
- Nii, H. P. (1986). *Blackboard Systems*. AI Magazine.
- Doyle, J. (1979). *A Truth Maintenance System*. Artificial Intelligence.
- de Kleer, J. (1986). *An Assumption-based TMS*. Artificial Intelligence.

### LLMs, tree search, and agents

- Yao, S. et al. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. arXiv:2305.10601 — https://arxiv.org/abs/2305.10601
- Besta, M. et al. (2023). *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*. arXiv:2308.09687 — https://arxiv.org/abs/2308.09687
- Zhou, A. et al. (2023). *Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models*. arXiv:2310.04406 — https://arxiv.org/abs/2310.04406
- Shinn, N. et al. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. arXiv:2303.11366 — https://arxiv.org/abs/2303.11366

### RAG, GraphRAG, and continual learning

- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. arXiv:2005.11401.
- Microsoft Research / GraphRAG literature, to verify and complete.
- Wu, T. et al. (2024). *Continual Learning for Large Language Models: A Survey*. arXiv:2402.01364 — https://arxiv.org/abs/2402.01364
- Shi, H. et al. (2024). *Continual Learning of Large Language Models: A Comprehensive Survey*. arXiv:2404.16789 — https://arxiv.org/abs/2404.16789

---

## 17. Provisional conclusion

The problem deserves attention because it touches a blind spot of current models: not producing a locally plausible answer, but **capitalizing on the experience of exploration**.

The central intuition is that useful reasoning resembles an exploration more than a chain. This exploration often begins as a tree, technically becomes a graph, and becomes truly cumulative only if it is stigmergic: each passage leaves a trace usable by future passages.

If the transmissible corpus can be represented as some models are represented today — but without losing readability, versionability, governance, and transmissibility — then a new class becomes conceivable: not an additional language model, but a living, incremental, exploratory, and transmissible corpus model.

This class remains hypothetical. Its difficulty is high. But its interest is sufficient to justify a source document, a critical review, and a first micro-prototype.

---

## 18. Minimal completion report

```text
Issue: JeanHuguesRobert/barons-Mariani#7
Files changed: research/modele_corpus_transmissible_incremental.md
Tests run: none — research document only
Known risks: speculative status; bibliography incomplete; architecture not validated; risk of over-formalization
Next step: submit to Grok reviewer, then integrate selected critique
Human validation needed: yes
```
