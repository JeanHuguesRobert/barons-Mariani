---
title: "Incremental Transmissible Corpus Model"
subtitle: "Cognitive backtracking, qualitative stigmergy, and cumulative exploration of possibilities"
version: "0.3"
status: "working-paper — source document — speculative embryo — externally reviewed"
date: "2026-06-13"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
language: "en"
intended_path: "research/modele_corpus_transmissible_incremental.md"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/modele_corpus_transmissible_incremental.md"
issue: "JeanHuguesRobert/barons-Mariani#7"
symmetry: "medium-high — source-hypothesis, still speculative"
corpus_role: "source-hypothesis"
review_status: "Grok constructive review integrated selectively — 2026-06-13"
review_file: "research/modele_corpus_transmissible_incremental_grok_review_2026-06-13.md"
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
  - "Grok constructive review v0.1, selectively integrated by ChatGPT, pending human arbitration, 2026-06-13"
critique_pending:
  - "Human arbitration on final naming, prototype scope, and technical derivations"
  - "Empirical micro-prototype before any stronger claim of acceleration"
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
  - "ChatGPT — drafting, state-of-the-art framing, structure, English version, review integration"
  - "Grok — constructive external reviewer, non-decisional"
human_validation_required: true
next_action: "Run a micro-prototype on a small curated corpus before producing stronger claims or technical derivatives."
---

# Incremental Transmissible Corpus Model

## Cognitive backtracking, qualitative stigmergy, and cumulative exploration of possibilities

**Jean Hugues Noël Robert**  
Institut Mariani / C.O.R.S.I.C.A.  
1 cours Paoli, F-20250 Corte, Corsica

*Working paper — June 13, 2026 — speculative embryonic source document — externally reviewed*

---

## Purpose

This document has a modest but strategic purpose: **to preserve the trace of a research intuition**.

The intuition is the following: current language models can generate, reformulate, approximate, compare, and sometimes explore several possible lines of reasoning. Yet they still lack, or lack sufficiently, a **transmissible corpus represented as an incremental model of exploration**: a versioned source corpus, structured as a graph, annotated by qualitative stigmergic traces, navigable through probabilistic heuristics, and capable of explicitly capitalizing on past explorations.

This document does not claim that the problem has been solved. It claims that the problem deserves attention.

The central question can be formulated as follows:

> What would current models still need in order to reason not merely as sequential text generators, but as cumulative explorers of a graph of possibilities, where each exploration leaves a reusable trace for future explorations?

---

## Review integration note

Version 0.3 integrates a constructive external review by Grok. The integration is selective and non-decisional: it preserves the speculative status of the paper, strengthens explicit open questions, clarifies the role of the scheduler, adds a first branch-relation taxonomy, adds a trace-validation workflow, and turns the research paths into a prioritized roadmap.

The review is not treated as authority. It is treated as a contribution to the corpus. The human author remains responsible for naming, scope, prototype decisions, and any future stabilization.

---

## Associated documents and corpus role

- [`barons-Mariani/research/second_method.md`](second_method.md) — general methodological doctrine. This paper applies its discipline of signal/noise, explicit objections, evidential levels, self-containment, and human validation.
- [`barons-Mariani/research/trace_epistemology.md`](trace_epistemology.md) — epistemology of traces and imputability under uncertainty. This paper extends the trace from documentary evidence to exploration memory.
- [`barons-Mariani/research/cognitive_waves.md`](cognitive_waves.md) — stigmergic framework for cognitive terrains. This paper narrows that framework toward a model of cumulative reasoning.
- [`barons-Mariani/research/stigmergie_sans_limite_haute.md`](stigmergie_sans_limite_haute.md) — stigmergic continuity from simple agents to cognitive agents. This paper applies that continuity to versioned corpora.
- [`cogentia/research/conversation_to_corpus_pipeline.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/conversation_to_corpus_pipeline.md) — conversation-to-corpus pipeline. This paper treats exploration traces as candidates for corpus integration.
- [`cogentia/research/cognitive_packets.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/cognitive_packets.md) — transmissible cognitive packets. Branches, traces, fusions and validations should later become compatible with cognitive packet extraction.
- [`cogentia/research/derived_products.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/derived_products.md) — source and derivative-product logic. The proposed model is intended to reduce drift between source corpus and derivative products.
- [`inseme/AGENTS.md`](https://github.com/JeanHuguesRobert/inseme/blob/main/AGENTS.md) — bounded mandate, traceability, human validation, agentic continuation. The scheduler proposed here is compatible in spirit with bounded agentic mandates.

The present document belongs in `barons-Mariani/research` because it is still primarily a speculative and doctrinal source-hypothesis. A later technical derivative may belong in `cogentia` or `inseme`, but only after a micro-prototype has clarified schema, cost, and feasibility.

---

## Methodological alignment

This document attempts to apply the second method rather than merely describe an idea. It therefore follows five constraints.

| Constraint | Application in this document |
|---|---|
| Signal/noise | Only stabilizable traces and high-leverage objections should enter the corpus. Raw conversational wandering is not the target. |
| Evidential levels | The proposal distinguishes established adjacent techniques from speculative claims about corpus models. |
| Objection conversion | Objections are converted into testable tasks: cost, branch fusion, trace validation, scheduler, prototype metrics. |
| Self-containment | The core claim should remain understandable without reading the whole surrounding corpus. |
| Human validation | LLMs and reviewers suggest; the author arbitrates naming, stabilization, and publication. |

---

## Abstract

Large language models have made a powerful form of probabilistic linguistic generation practically usable. They can produce answers, reformulate knowledge, suggest hypotheses, write code, translate intent into plans or queries, and sometimes explore several reasoning paths. Their dominant architecture nevertheless remains insufficient for a specific form of reasoning: **the cumulative exploration of possibilities**.

The deeper problem is not merely hallucination or weak sourcing. The problem is that current systems usually lack an external, durable, versioned, and governed space where explorations become transmissible objects. A useful exploration should leave a trace: open branch, suspended branch, refuted branch, branch merged with another one, exploration cost, evidential level, reopening conditions, objections, provenance, and validation status.

This document provisionally names **Incremental Transmissible Corpus Model** a system in which the source corpus remains sovereign, but is compiled into a directed exploration graph, qualitative stigmergic traces, typed cognitive units, vector indexes, verifiers, and navigation heuristics. The LLM is not the judge of truth. It is a heuristic function for generation, provisional evaluation, analogy detection, and navigation. Authority remains distributed among the corpus, sources, tests, rules, human validation, and explicit mandates.

The state of the art already offers several adjacent building blocks: Tree of Thoughts, Graph of Thoughts, Language Agent Tree Search, Reflexion, GraphRAG, blackboard systems, truth maintenance systems, tabled Prolog, continual learning for LLMs, ant colony optimization, and stigmergy. Yet none of these lineages, taken in isolation, seems to provide a complete model of a transmissible, incremental, stigmergic, and governed corpus.

The hypothesis is that this class of models could accelerate intellectual, scientific, legal, political, or technical explorations by relying on the accumulated experience of past explorations. It could transform errors, dead ends, and contradictions into resources. But this remains unproven. Node granularity, branch equivalence, trace quality, corpus corruption, maintenance cost, update governance, derivative-product synchronization, and empirical evaluation remain open.

---

## Key open questions deliberately left open

This paper deliberately leaves the following questions unresolved:

1. **Name** — Is "Incremental Transmissible Corpus Model" the right term, or does "model" import misleading machine-learning expectations?
2. **Node granularity** — What is the smallest useful unit: statement, claim, hypothesis, objection, branch, document section, decision?
3. **Branch equivalence** — When do two branches truly merge, and when are they merely analogous or partially convergent?
4. **Trace validation** — Who or what validates a trace, and under which evidential threshold does it become reusable?
5. **Scheduler** — What is the minimal policy for choosing depth, breadth, suspension, reopening, fusion, or publication?
6. **Cost** — Can the trace layer accelerate exploration without suffocating it under documentary overhead?
7. **Governance** — How are validated traces, scheduler policies, forks, merges, and reversals audited over time?
8. **Derivative products** — How can Substack posts, academic notes, technical schemas or political texts remain linked to graph versions without rigidifying writing?
9. **Empirical value** — Does the system outperform plain Git + Markdown, Obsidian-like notes, simple RAG, or GraphRAG on real corpus-resumption tasks?

---

## Transformation map

```text
initial intuition
→ useful reasoning is not a simple chain of text
→ it resembles a tree-like exploration of possibilities
→ branches can fail, succeed, merge, cycle, or be suspended
→ the apparent tree technically becomes a directed graph
→ each passage must leave a qualitative stigmergic trace
→ the trace indicates what was attempted, found, cost, refuted, validated, or suspended
→ the LLM can serve as a probabilistic navigation heuristic
→ the source corpus remains sovereign and versioned
→ the operational model is a compilation of the corpus, not its replacement
→ exploration becomes incremental: each passage can improve following passages
→ possible new class: Incremental Transmissible Corpus Model
```

---

## 1. Problem: current models answer better than they durably explore

Current LLMs are often evaluated by their ability to produce a correct answer to a given query. Even when a model appears to reason, the visible unit usually remains the final answer, or at most an intermediate sequence of justification.

That logic is suitable for many tasks. It is insufficient for longer intellectual work: exploring a territory of possibilities, capitalizing on dead ends, reopening an old branch, merging two hypotheses, preserving a contradiction, or transmitting to another agent what has already been attempted.

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

An ordinary LLM can produce this YAML. Producing a trace is not yet having a system in which such traces are persistent, typed, versioned, reused, corrected, compared, consolidated, and reintegrated into the corpus.

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

> an exploration with a dominant tree-like shape, represented as a directed graph of continuations, annotated by qualitative stigmergic traces.

Stigmergy turns simple exploration into cumulative exploration. A visited branch is not merely traversed; it is marked. The trace modifies future explorations.

In the classical biological case, the trace may be a pheromone. In ant colony optimization, the trace is often primarily quantitative. In the cognitive-documentary case proposed here, the trace should be qualitative: status, proof, objection, cost, confidence, provenance, validation status, and reopening conditions.

This distinction matters. The proposed trace is not an automatic attractor. It is a governed artifact used by a scheduler and subject to human arbitration.

---

## 3. Provisional definition

> An Incremental Transmissible Corpus Model is a system in which a versioned source corpus is compiled into operational representations — exploration graph, qualitative stigmergic traces, typed cognitive units, vector indexes, rules, verifiers, and navigation heuristics — in order to accelerate future explorations through explicit capitalization of past experience, without dissolving knowledge into opaque weights.

This definition contains four constraints.

| Constraint | Meaning |
|---|---|
| Source sovereignty | The corpus remains the auditable, forkable, versioned source. The operational model must remain derivable from it. |
| Branch-situated knowledge | Claims retain their histories: hypotheses, objections, tests, arbitrations, rejections, reformulations. |
| Incrementality of search | The system does not merely add documents; it improves how branches are reopened, suspended, fused, or avoided. |
| Non-sovereign LLM | The LLM suggests, reformulates and estimates. It does not decide truth or stabilization. |

```text
source corpus ≠ operational model
source code ≠ compiled binary
```

A compiled program may be fast, but it does not replace the source if one wants to understand, correct, fork, audit, or transmit it. The same distinction should hold for a corpus model.

---

## 4. Operational core: scheduler and exploration budget

The critical component is not merely the graph. A graph without an exploration policy becomes a complex archive. The operational core is the scheduler.

The scheduler allocates the available **exploration budget**: tokens, computation, human attention, review time, maintenance debt, documentary complexity, and political or institutional risk. In the vocabulary of Autonomy of Capability, this may be called **cognitive exergy**, provided the term remains operational rather than rhetorical.

It should arbitrate between:

- depth and breadth;
- exploiting a promising branch and exploring a neglected branch;
- reopening an old hypothesis and opening a new one;
- merging two nodes and preserving a distinction;
- temporary abandonment and definitive closure;
- publishing a result and keeping it in internal research.

Possible criteria:

```yaml
scheduler_criteria:
  promise: "probability of producing useful clarification"
  risk: "risk of error, confusion, capture, or premature closure"
  cost: "time, tokens, attention, maintenance, review burden"
  novelty: "degree of real novelty"
  convergence: "ability to connect or merge several branches"
  evidence_gap: "gap between thesis and available evidence"
  derivative_value: "ability to produce useful derivative products"
  strategic_value: "importance for the corpus or action"
  reversibility: "ease of rollback"
  human_validation_need: "need for human arbitration"
```

This remains a list of criteria, not yet a decision procedure. A minimal prototype should begin with a rule-based scheduler, not with a learned scheduler.

---

## 5. State of the art: proximities and gaps

This document does not start from nothing. Several traditions have already explored fragments of the problem.

### 5.1 Backtracking, Prolog, and tabling

Logical backtracking is an obvious matrix: one explores a rule, descends, fails or succeeds, then returns. Prolog made this mechanism programmable.

Tabling in logic programming adds an essential dimension: memorizing already called subgoals and their answers in order to avoid recomputation and better handle recursion. This lineage already addresses two central problems: branch merging and cycles.

Gap: tabling remains defined in a formal logical and computational framework. The model proposed here targets a broader field: hypotheses, objections, texts, partial evidence, dead branches, derivative products, human validation.

### 5.2 Stigmergy and ant colony optimization

Stigmergy, introduced by Pierre-Paul Grassé in relation to termites, designates indirect coordination through traces left in the environment. Marco Dorigo's Ant Colony Optimization transposes this idea into optimization: agents explore paths and leave pheromone-like traces that probabilistically influence future explorations.

Proximity: probabilistic path selection based on traces.

Gap: in ant colony optimization, the trace is often primarily quantitative. In a transmissible corpus model, the trace should be qualitative, argumentative, sourced, versioned, and governed.

### 5.3 Blackboard systems

Classical AI blackboard systems rely on a shared space updated by different specialized modules. A controller chooses which knowledge sources to activate according to the current state of the blackboard.

Proximity: shared space, partial contributions, opportunistic control.

Gap: the blackboard is not necessarily a versioned, transmissible, auditable, publishable, and forkable corpus. The trace of past explorations is not always a central doctrinal object.

### 5.4 Truth maintenance systems

Truth Maintenance Systems preserve the dependencies and justifications of beliefs in order to restore coherence when new information contradicts the current state.

Proximity: dependencies, justifications, contradictions, revision.

Gap: the proposed model adds probabilistic exploration, qualitative stigmergy, versioned source corpus, derivative products, and explicit human validation.

### 5.5 Tree of Thoughts, Graph of Thoughts, and LATS

Tree of Thoughts proposes to move beyond token-by-token generation by exploring multiple reasoning units, with self-evaluation, lookahead, and backtracking. Graph of Thoughts generalizes this logic by representing thought units as graph vertices, enabling combination, aggregation, and feedback loops. Language Agent Tree Search combines LLMs, Monte Carlo Tree Search, value functions, and external feedback for agents capable of reasoning, acting, and planning.

Proximity: multiple-path exploration, heuristic selection, backtracking, tree or graph structure.

Gap: these approaches often remain centered on inference for a task or query. The exploration graph is not necessarily preserved as a durable, governed, and transmissible corpus.

### 5.6 Reflexion and textual agent memory

Reflexion proposes that language agents learn from their errors without updating their weights, through a textual memory of experience feedback. This is close to the principle that an exploration should leave a trace.

Proximity: linguistic feedback, episodic memory, improvement without fine-tuning.

Gap: Reflexion memory is mainly oriented toward agentic performance. The model proposed here aims at corpus memory, with thesis status, evidential levels, publication possibility, human review, fork, and transmission.

### 5.7 RAG, GraphRAG, and knowledge graphs

RAG allows a model to consult external documents. GraphRAG or knowledge-graph RAG variants seek to structure retrieval further through entities, relations, and multi-hop paths.

Proximity: externalization of knowledge, structured retrieval, documentary support.

Gap: RAG retrieves content; it does not necessarily preserve explorations as objects. A transmissible corpus model should represent not only documents, but the cognitive acts that transformed those documents into hypotheses, objections, decisions, and derivative products.

### 5.8 Continual learning for LLMs

Continual learning seeks to allow LLMs to adapt to new data, tasks, or preferences without retraining everything and without forgetting previous acquisitions. The major difficulties remain catastrophic forgetting, regression, and update control.

Proximity: incrementality, adaptation, continuity.

Gap: the proposed model partially bypasses the problem by placing the primary increment outside the model weights: in the corpus, graph, traces, and heuristics.

---

## 6. What current models still lack

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

This table does not imply that every current system lacks everything. It indicates that the complete combination remains rare or unstabilized.

---

## 7. Speculative minimal architecture

A minimal architecture could contain the following layers.

```text
1. Versioned source corpus
   Markdown, YAML, documents, references, commits, history.

2. Cognitive-unit extractor
   Facts, hypotheses, objections, proofs, definitions, decisions, continuations.

3. Directed exploration graph
   Nodes, arcs, dependencies, fusions, contradictions, versions, statuses.

4. Qualitative stigmergic traces
   Passage, result, cost, confidence, source, validation status, reopening condition.

5. Vector indexes and semantic signatures
   Similarities, possible duplicates, analogies, conceptual neighborhoods.

6. Verifiers
   Sources, tests, rules, citations, internal coherence, human validation.

7. Exploration scheduler
   Allocation of exploration budget / cognitive exergy among branches.

8. Heuristic LLM
   Generation, reformulation, provisional evaluation, analogies, objections.

9. Controlled commit
   Stabilization, diff, justification, impact, rollback.

10. Derivative products
    Academic article, Substack post, political note, technical schema, issue, protocol.
```

---

## 8. Typed cognitive units

The model cannot function properly if everything remains undifferentiated text. At least some typed units are required.

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

The list is not a final ontology. It is a working vocabulary for a micro-prototype.

---

## 9. Branch relations and fusion taxonomy

Branch fusion is a core feasibility risk. Two branches may appear identical while resting on different assumptions. Merging them too early may destroy information; refusing every merge may fragment the graph.

A first taxonomy can reduce that risk.

| Relation | Meaning | Default action |
|---|---|---|
| `strong_equivalence` | Same claim or state under compatible assumptions. | Candidate merge after validation. |
| `partial_convergence` | Different paths support overlapping conclusions. | Link, do not merge yet. |
| `analogy` | Similar structure, different domain or assumptions. | Mark as analogy; no merge. |
| `neighborhood` | Semantically close but not clearly related. | Keep separate; retrieval hint only. |
| `apparent_contradiction` | Tension detected, not yet analyzed. | Open contradiction branch. |
| `real_contradiction` | Incompatibility confirmed under shared assumptions. | Require arbitration, revision, or split. |
| `supersession` | One branch replaces an earlier version. | Preserve old branch, mark superseded. |

No LLM-generated fusion should be treated as final. The LLM may propose candidate relations; validation belongs to rules, sources, tests, or human arbitration.

---

## 10. Trace validation workflow

A trace should not become reusable merely because it exists. It should pass through explicit statuses.

```text
proposed_trace
→ evidence_checked
→ validated_by_rule_or_human
→ reusable_trace
```

Alternative paths must also exist:

```text
proposed_trace → rejected_trace
validated_trace → superseded_trace
validated_trace → disputed_trace → revised_trace
```

Minimal fields:

```yaml
trace_status:
  - proposed
  - evidence_checked
  - validated
  - reusable
  - rejected
  - disputed
  - superseded
  - revised

validation_fields:
  validator: "human | rule | test | source-check | reviewer"
  validation_date: "YYYY-MM-DD"
  evidential_level: "speculative | plausible | sourced | tested | validated"
  provenance: "conversation | document | tool | human review | external review"
  reopening_condition: "what would justify revision"
```

This workflow is intentionally minimal. It exists to prevent LLM-generated traces from contaminating the corpus as if they were validated knowledge.

---

## 11. Strong objections converted into research tasks

### Objection 1 — Documentary cost may suffocate the process

Tracing every exploration may become more costly than the exploration itself.

Research task: measure person-hours, number of traces produced, number of traces actually reused, and documentary cost per useful clarification during the micro-prototype.

### Objection 2 — Branch fusion is hard

Branch equivalence, fusion and contradiction detection are substantially harder than the first sketch may imply.

Research task: test the branch-relation taxonomy above on a small corpus; count false merges, missed contradictions, and human-arbitrated cases.

### Objection 3 — Trace validation is under-specified

A graph of validated traces creates a de facto authority surface.

Research task: implement proposed / validated / rejected / disputed / superseded statuses, then test whether later users can identify who or what validated a trace.

### Objection 4 — Governance may dominate the architecture

Beyond single-author use, mandates, forks, merges, scheduler changes and trace validation require governance.

Research task: map each graph-level change to an event, artifact, decision, validator, and rollback path. Assess compatibility with COP invariants.

### Objection 5 — Acceleration remains unproven

The central value claim is testable but not demonstrated.

Research task: compare the prototype against plain Git + Markdown, simple RAG, and GraphRAG-like retrieval on the same resumption task.

### Objection 6 — Architectural detail can create premature closure

YAML schemas, layers and named components can freeze an idea before empirical feedback.

Research task: keep schema v0.1 explicitly provisional; move detailed examples to annex or derivative technical files after prototype feedback.

---

## 12. Current evidential levels

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

## 13. Prioritized roadmap

### 13.1 Micro-prototype on a limited corpus — priority 1

Test on five documents:

1. `second_method.md`;
2. `trace_epistemology.md`;
3. `stigmergie_sans_limite_haute.md`;
4. `conversation_to_corpus_pipeline.md`;
5. this document.

Success criteria:

- at least one populated graph fragment;
- at least five traces, with different statuses;
- at least two branch-relation classifications;
- at least one rejected or disputed trace;
- at least one branch reopened because of a prior trace;
- measured documentation time;
- short lessons-learned note on overhead versus reuse.

### 13.2 Minimal YAML schema — priority 2

Define only the fields necessary for:

- branch;
- trace;
- branch relation;
- contradiction;
- validation;
- derivative product link.

Do not attempt a complete ontology before prototype feedback.

### 13.3 Scheduler stub — priority 3

Implement a minimal rule-based scheduler. For example:

```text
if branch.status == "blocked" and no reopening_condition is met:
    do not reopen
elif branch.evidence_gap == "high" and derivative_value == "high":
    request source search or human arbitration
elif branch.relation == "apparent_contradiction":
    open contradiction branch
else:
    keep as low-priority open branch
```

This is not meant to be elegant. It is meant to make the scheduler falsifiable.

### 13.4 Comparison baseline — priority 4

Compare four conditions:

1. plain Git + Markdown;
2. simple RAG;
3. GraphRAG or knowledge-graph retrieval;
4. corpus model with exploration traces.

Question: does adding exploration traces improve resumption, coherence, contradiction detection, and avoidance of already-failed branches?

### 13.5 COP articulation — priority 5

Articulate this model with COP only after the micro-prototype clarifies the event and artifact types actually needed. Candidate COP alignment:

- immutable events;
- durable artifacts;
- topic-local ordering;
- deterministic replay;
- stateless agents;
- explicit schema versioning;
- transparency over convenience.

---

## 14. Possible effects if it worked

### 14.1 Acceleration of explorations

The first effect would be to avoid starting again from zero. Each future exploration would benefit from already opened branches, identified dead ends, recurring objections, and stabilized fusions.

### 14.2 Transformation of errors into resources

A properly traced error becomes a resource. It says: do not restart here without new data; beware of this confusion; this analogy is seductive but false; this branch cost too much for too little gain.

### 14.3 More faithful transmission

A transmissible corpus would transmit not only conclusions. It would transmit paths, hesitations, reasons, statuses, critiques, validations.

### 14.4 Better human / AI articulation

AI would not be charged with deciding; it would contribute to exploration. The human would retain the role of arbitration, mandate, validation, and responsibility.

### 14.5 More coherent derivative products

A Substack article, an academic note, a Facebook response, a technical protocol, or a political proposal could derive from the same source graph. This remains a hypothesis unless derivative products are explicitly linked to graph versions and source branches.

### 14.6 Reduction of capture by opacity

A model whose source remains versioned, auditable, and forkable resists capture better than a model whose memory is dissolved into proprietary non-inspectable weights.

---

## 15. Positioning within Cogentia

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

## 16. Possible derived products

The review suggests six derivative products. They should not all be produced at once.

| Product | Audience | Recommended timing |
|---|---|---|
| short academic note | neuro-symbolic AI, agentic systems, digital humanities | after v0.3 review or micro-prototype plan |
| Substack article | broader audience concerned with AI amnesia and living corpora | after source stabilization |
| Cogentia architecture note | Cogentia / Inseme contributors | after minimal schema exists |
| cognitive packet YAML schema | implementers and future corpus contributors | during micro-prototype |
| COP exploration protocol | COP implementers | after event/artifact needs are observed |
| research pitch | potential collaborators or funders | after one demonstrable prototype fragment |

---

## 17. Provisional doctrinal formula

> LLMs have shown that a corpus can be absorbed into a statistical model. The complementary path is to make a versioned corpus operational as a model without dissolving it into opaque weights. An Incremental Transmissible Corpus Model does not replace the corpus: it compiles it into an exploration graph, qualitative stigmergic traces, cognitive units, and navigation heuristics. Reasoning is no longer a simple chain of text; it becomes a governed exploration of possibilities, accumulating its own passages in order to better orient the next ones.

---

## 18. Initial bibliography and documentary paths

This bibliography is not stabilized. It serves as a starting point for review and prototype work.

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

## 19. Provisional conclusion

The problem deserves attention because it touches a blind spot of current models: not producing a locally plausible answer, but **capitalizing on the experience of exploration**.

The central intuition is that useful reasoning resembles an exploration more than a chain. This exploration often begins as a tree, technically becomes a graph, and becomes truly cumulative only if it is stigmergic: each passage leaves a trace usable by future passages.

If the transmissible corpus can be represented as some models are represented today — but without losing readability, versionability, governance, and transmissibility — then a new class becomes conceivable: not an additional language model, but a living, incremental, exploratory, and transmissible corpus model.

This class remains hypothetical. Its difficulty is high. Its interest is sufficient to justify a source document, an external review, and a first micro-prototype.

---

## 20. Minimal completion report

```text
Issue: JeanHuguesRobert/barons-Mariani#7
Files changed: research/modele_corpus_transmissible_incremental.md
Tests run: none — research document only
Known risks: speculative status; bibliography incomplete; architecture not validated; risk of over-formalization; acceleration claim not demonstrated
Next step: micro-prototype on a small curated corpus, then lessons-learned note
Human validation needed: yes
```
