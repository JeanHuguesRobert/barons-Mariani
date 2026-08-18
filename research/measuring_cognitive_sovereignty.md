---
title: "Measuring Cognitive Sovereignty: User-Controlled Probes for Conversational AI"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-08-18"
last_stamped_at: 2026-08-18
status: "working-paper"
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
license: "CC BY-SA 4.0"
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/measuring_cognitive_sovereignty.md
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---

# Measuring Cognitive Sovereignty: User-Controlled Probes for Conversational AI

## Working-paper status

This document is an exploratory preprint draft developed under the Second Method and the Rational Exploration of the Possible. It deliberately separates observation, interpretation, certification, and normative implications. Claims below are provisional until tested experimentally and reviewed against prior art.

It develops the minimal experiment first recorded in [Cognitive Sovereignty Probe](./cognitive_sovereignty_probe.md). The present paper is intended to become independently readable: project-specific terminology is introduced only where it contributes to the scientific argument.

## Abstract — draft 0.1

As conversational artificial-intelligence systems become persistent intermediaries for reasoning, memory, information access, and action, user sovereignty cannot be reduced to the provenance of the model or infrastructure. A distinct question is whether the user can introduce, maintain, substitute, and remove independently controlled cognitive capabilities within interactions with a conversational provider. This paper proposes **user-controlled probes** as an experimental method for measuring operational properties relevant to such cognitive sovereignty.

The minimal experiment is intentionally simple. A conversational agent is given access to an external service controlled by the user and instructed to invoke it repeatedly during an interaction. The service independently timestamps received observations and returns information for incorporation into the conversation. From these traces one can measure properties such as invocation frequency, temporal granularity, persistence across turns, fidelity of transmitted context, use of returned material, and constraints on external participation. Success and failure are both observations of the effective permeability of the host system to user-controlled capabilities.

We do **not** claim that cognitive sovereignty is directly measurable as a single scalar. Rather, we hypothesise that operational capabilities constitutive of user sovereignty can be isolated, experimentally probed, and represented multidimensionally. Conversational interposition is the first field; portability, memory control, substitutability, provenance, profiling transparency, attention control, independent contradiction, and exit cost are candidate extensions.

The approach complements current work on cognitive sovereignty, AI user agency, agent interoperability, switching, portability, and technological sovereignty by shifting the unit of observation from what a provider, organisation, or State controls to what an individual user can effectively do. A reproducible measurement layer may in turn support comparative benchmarks, certification schemes, technical adaptation, and future legal analysis of effective cognitive autonomy.

## 1. Research question

The primary research question is:

> **To what extent can operational capabilities relevant to an individual's cognitive sovereignty be measured experimentally by introducing user-controlled probes into interactions with third-party conversational AI systems?**

The first, narrower question is:

> **To what extent can a user-controlled external capability participate in the conversational loop of a third-party AI host, with what granularity, persistence, fidelity, and constraints?**

This formulation is intentionally operational. It does not require agreement on a complete philosophical or legal definition of cognitive sovereignty before measurement begins.

## 2. Motivation: sovereignty of whom?

Contemporary technological-sovereignty programmes predominantly describe the capacity of States, political communities, or organisations to control critical technologies, infrastructure, data, and dependencies. This is an important problem, but it is not equivalent to user sovereignty.

A nationally controlled AI service can remain highly capturing from the user's perspective. Conversely, a foreign service may expose unusually strong portability, substitutability, open interfaces, or user-controlled interposition. We therefore distinguish at least three potentially divergent objects:

1. sovereignty of the State or political community;
2. sovereignty of the provider or organisation;
3. sovereignty of the individual user.

The experimental focus of this paper is the third.

## 3. Related work and current context — Explorer notes

This section is deliberately a research map rather than a finished literature review. The initial exploration reveals several adjacent literatures that must not be conflated.

### 3.1 Cognitive sovereignty

The term **cognitive sovereignty** is already active and rapidly diversifying in 2025–2026 literature. Recent work uses it to discuss authorship over AI-assisted thought, preservation of independent professional or leadership judgement, cognitive drift and identity, decolonial epistemic authority, neuro-rights, and collective cognitive infrastructure.

This is important prior art. The contribution proposed here is therefore **not the term itself**. The candidate contribution is an experimental methodology for characterising user-controlled operational capabilities relevant to cognitive sovereignty, beginning with externally observable conversational interposition.

The literature review must examine at least:

- cognitive sovereignty as authorship and epistemic agency;
- automation bias, cognitive offloading, and deskilling;
- cognitive sovereignty in professional decision-making;
- decolonial and indigenous-data/epistemic sovereignty;
- neurorights and mental autonomy;
- cognitive sovereignty at State or political-community scale;
- relational AI, identity, and cognitive drift.

### 3.2 User agency, contestability, and human oversight

AI governance contains substantial work on human agency, meaningful human control, contestability, explanation, and oversight. These traditions generally ask whether humans retain meaningful authority over automated outcomes. Our narrower technical question is complementary: can the user bring an **independent, user-controlled computational participant** into the interaction itself?

### 3.3 Interoperability and agent protocols

Agent ecosystems are converging on protocols and standards for interaction with tools, data, and other systems. In February 2026, NIST announced an AI Agent Standards Initiative explicitly concerned with secure interoperability and agents acting on behalf of users. MCP and related tool/agent protocols make user-controlled interposition technically plausible, but protocol availability does not establish the effective behaviour of a particular conversational host. The proposed probe measures that behaviour empirically.

### 3.4 Switching and portability

European regulation provides an adjacent precedent: the Data Act addresses switching barriers and interoperability for data-processing services, while DMA enforcement has emphasised portability and interoperability in gatekeeper ecosystems. These regimes demonstrate that nominal freedom of choice is weakened by practical switching costs and loss of data or functionality. Cognitive continuity may create an analogous, though not legally identical, problem for conversational AI.

### 3.5 Technological sovereignty

The European Commission's 2026 technological-sovereignty programme focuses on Europe's capacity to develop and control critical technologies, data, infrastructure, cloud, AI and open-source capabilities. The proposed Cloud and AI Development Act includes an EU-wide assessment framework for cloud and AI sovereignty. This provides a timely comparison: infrastructure sovereignty is increasingly being formalised and assessed, while user-level cognitive sovereignty remains comparatively under-instrumented.

## 4. Hypotheses

### H1 — Observable interposition

A conversational host with access to an external user-controlled tool can, under suitable instructions, invoke that capability sufficiently often to produce independently timestamped evidence of external participation in the conversational process.

### H2 — Host-specific capability profiles

Different hosts, configurations, models, interfaces, prompts, and tool mechanisms will produce measurably different interposition profiles.

### H3 — Multidimensionality

No single measure such as invocation count or latency is sufficient. Relevant properties include at least frequency, temporal granularity, persistence, context fidelity, return-value incorporation, user control, substitutability, and failure modes.

### H4 — Revealer/stabiliser duality

The same external channel used to reveal the host's permeability can subsequently carry active user-controlled functions such as translation, recall, provenance checking, contradiction, review, or prompt suggestion. Measurement can therefore inform adaptation without being conflated with it.

### H5 — Generalisability

Conversational interposition is one measurable field among several. The general method — define an operational capability, construct a minimally invasive probe, retain independent traces, compare observed behaviour — can be extended to other fields relevant to cognitive sovereignty.

## 5. Minimal experimental system

A reference probe can expose three minimal operations:

```text
john_conversation_start()
john_conversation_observe(text)
john_conversation_status()
```

The external service should maintain an independent monotonic and wall-clock trace where technically possible. The host is instructed to invoke the observer as frequently as reasonably possible, including during a response when its execution model permits it, and to display at the end the measured duration together with Markdown returned by the probe.

The crucial epistemic property is that the probe records **what reaches the external service**, not what the host claims to have sent.

### 5.1 Minimum trace schema

Each event should record, where available:

- experiment identifier;
- host/provider and product surface;
- model identifier/version as exposed;
- session and turn identifier;
- tool/protocol/configuration version;
- server receive timestamp;
- monotonic elapsed time;
- payload byte/token estimates;
- payload digest and optionally retained payload subject to privacy policy;
- response timestamp;
- returned-content digest;
- error/failure state.

Raw traces should be retained separately from derived metrics.

### 5.2 Candidate metrics

Initial metrics may include:

- observations per turn;
- inter-observation interval distribution;
- first-observation latency;
- cross-turn persistence;
- context transmission ratio;
- semantic or exact fidelity where a ground truth exists;
- returned-content incorporation rate;
- tool refusal/omission rate;
- recovery after tool failure;
- configuration persistence;
- user-visible interruption cost.

No aggregate sovereignty score is proposed at this stage.

## 6. Experimental protocol — draft

A first comparative study should use a common protocol across conversational hosts while recording unavoidable product-specific differences.

1. Establish a fresh session and record host/model/configuration metadata.
2. Attach or expose the same reference probe through the most comparable supported mechanism.
3. Provide a versioned standard instruction requesting frequent observation and final reporting.
4. Execute a fixed battery of conversational tasks of different duration and structure.
5. Include tasks requiring long-form generation, iterative reasoning, user follow-up, external information retrieval where supported, and deliberate probe failure/recovery.
6. Retain raw probe-side traces.
7. Repeat each condition sufficiently to estimate behavioural variance.
8. Re-run after meaningful model/product updates.
9. Distinguish prompt effects, tool-description effects, host policy, model behaviour, protocol constraints, and UI/runtime constraints wherever experimentally possible.

### 6.1 Controls

Controls should include:

- identical task without probe instructions;
- probe available but not explicitly requested;
- explicit request at low frequency;
- explicit request at high frequency;
- alternative wording of the instruction;
- equivalent non-MCP tool mechanism where available;
- synthetic probe latency and failure injection.

### 6.2 Reproducibility

The probe implementation, schemas, standard prompts, derived-metric code, and anonymised traces should be public whenever privacy and provider terms permit. Every reported result should identify the exact protocol version and observation date because hosted AI behaviour changes over time.

## 7. From measurements to a capability map

The intended output is initially a **capability profile**, not a ranking.

For a host H under configuration C at time t, define a vector:

`P(H,C,t) = [frequency, granularity, persistence, fidelity, incorporation, substitutability, recovery, ...]`

The vector is descriptive. Any normative weighting is a separate operation and must be explicit.

This separation mirrors a broader territory/map/instrument distinction:

- the cognitive environment is the **territory**;
- the structured capability representation is the **map**;
- probes are the **measurement instruments**.

Within the originating research corpus these correspond to Cogentia, Cogentigram, and Cogentiscope. The terminology is not required to reproduce the experiment.

## 8. Measurement, interpretation, certification

A central methodological constraint is:

> **measurement != interpretation != certification**

Probe traces are observations. Derived metrics are representations of observations. Claims about cognitive sovereignty are interpretations under stated assumptions. A certification scheme is an institutional judgement against a public referential.

This separation is necessary to prevent the measurement infrastructure itself from becoming an unaccountable authority.

One possible downstream application is KYS certification maintained by the PrivAI Foundation. Such an application is outside the empirical claims of the present paper and must remain reproducible by independent parties.

## 9. Revealer and stabiliser

The minimal probe has a dual character.

As a **revealer**, it exposes effective constraints on user-controlled participation. As a **stabiliser**, the same interposition channel can be used to supply an independent capability that reduces dependence on the host.

For example, a translation service illustrates the distinction cleanly. If a conversational host does not adequately support the user's language, a user-controlled intermediary can translate host output and user input. The experiment can first measure how reliably the host cooperates with that intermediary; the intermediary can then provide the capability whose availability the experiment measured.

This duality should not compromise experimental separation: passive measurement and active mediation should be tested as distinct conditions.

## 10. Explorer / Conservator and Redactor / Reviewer

The research process itself is organised around complementary functions.

**Explorer / Conservator**: exploration searches the space of possible mechanisms and interpretations; conservation records successful observations, protocols, provenance, and conceptual distinctions so that later exploration does not destroy or silently rewrite what was learned.

**Redactor / Reviewer**: the redaction phase states the strongest defensible claims; an independent review phase attempts to falsify them, identify prior art, expose confounders, and downgrade unsupported conclusions.

**Revealer / Stabiliser** operates primarily at the object level: probes reveal effective conditions; user-controlled capabilities can stabilise autonomy under those conditions.

These are related but non-identical projections of a broader variation/selection/conservation dynamic.

## 11. Threats to validity

The strongest foreseeable objections include:

### 11.1 Tool invocation is not cognition

A tool call is an externally observable event, not direct access to internal model reasoning. The paper therefore makes no claim to observe hidden chain-of-thought or internal cognitive state. It measures the effective participation of an external capability in the product interaction.

### 11.2 Prompt compliance is stochastic

Repeated trials and variance estimates are required. A single successful conversation is demonstration, not measurement.

### 11.3 Product surface confounding

Observed behaviour may arise from UI orchestration, tool runtime, policy, model, protocol, or rate limits. Results must be attributed to the tested system configuration, not casually to the underlying model.

### 11.4 Provider updates

Hosted systems are moving targets. Results require timestamps, version information where available, and periodic replication.

### 11.5 Good interposition does not imply overall sovereignty

A system can score well on interposition while performing poorly on portability, privacy, attention, profiling, or exit. This is a principal reason to reject a premature scalar score.

### 11.6 Probe-induced behaviour

The act of requesting frequent observation changes the interaction. This is not necessarily a defect: the experiment measures what the user can cause the host to do. Nevertheless, passive/default and instructed conditions must be distinguished.

### 11.7 Certification capture

Any certification authority can itself become a locus of capture. Public protocols, reproducible tests, versioned criteria, conflict-of-interest controls, and competing implementations are therefore architectural requirements rather than optional governance refinements.

## 12. Fundamental-rights implications — hypothesis, not result

If AI systems become persistent intermediaries for information, memory, reasoning, communication, and action, practical control over cognitive continuity may become relevant to the effective exercise of existing rights and freedoms, including freedom of thought and opinion, privacy, expression, access to information, and personal autonomy.

This paper does not claim that a general legal right to "cognitive sovereignty" currently exists. It proposes a more limited research programme: identify operational capabilities, measure them reproducibly, and then examine how those capabilities relate to existing legal protections.

A useful legal question is therefore not merely whether a right is declared, but whether the technical environment supplies the capacities required to exercise it effectively.

## 13. Provider and territorial competition — downstream hypothesis

If trustworthy measurements become legible to users, providers may acquire an incentive to improve measurable user sovereignty. If certification based on reproducible measurements acquires sufficient reputation, territories may similarly gain an advantage by making high levels of user sovereignty easier to achieve.

We call the latter hypothetical mechanism **positive cognitive dumping**: territorial competition that attracts people and activity by increasing measurable cognitive sovereignty rather than by reducing social, fiscal, or regulatory protections.

A territory or regime that becomes attractive on this basis can be described as a **Cognitive Haven**. These concepts are downstream institutional hypotheses, not prerequisites for the experimental method.

## 14. Booster property

The probe is intentionally minimal, yet it opens multiple research directions. A timer-like external observer yields traces; traces yield capability measurements; capability measurements can guide active mediation; comparable measurements enable benchmarks; benchmarks may support certification and institutional experimentation.

This is an instance of a broader **booster** pattern: a low-cost transformation that increases the number of reachable useful possibilities disproportionately to its initial implementation cost.

The booster interpretation is heuristic and should not be confused with the empirical contribution of the paper.

## 15. Falsification programme

The paper's core claims should be weakened or rejected if experiments show, for example, that:

- external participation cannot be reproduced reliably enough to characterise;
- measured differences are dominated by uncontrolled product noise;
- metrics cannot be separated from prompt-specific artefacts;
- external traces add no meaningful evidence beyond existing host telemetry;
- the proposed dimensions fail to correspond to capabilities users can actually exercise;
- prior work already provides an equivalent experimental method and capability model.

A useful negative result would still establish limits on conversational interposition and help refine the operational definition.

## 16. Immediate experimental plan

Before claiming results:

1. implement and publish the reference probe;
2. freeze protocol `CSP-EXP-001`;
3. define a small task battery;
4. test at least three materially different conversational hosts;
5. perform repeated trials;
6. publish raw/anonymised traces and analysis scripts;
7. run a dedicated prior-art review after implementation details are fixed;
8. submit the draft to an adversarial Reviewer;
9. revise claims before public preprint submission.

## 17. Candidate contributions

Subject to experimental confirmation and prior-art review, the paper may contribute:

1. an operational distinction between provider/State sovereignty and measurable user-level cognitive capabilities;
2. a user-controlled probe method for externally measuring conversational interposition;
3. a multidimensional capability-profile model rather than a premature scalar sovereignty score;
4. an experimental framework separating host behaviour, measurement, interpretation, and certification;
5. a general research programme of field-specific probes for cognitive sovereignty.

## 18. Related corpus material

Primary source note:

- `research/cognitive_sovereignty_probe.md`

Relevant internal research:

- `research/the_network_is_the_learning_computer.md`;
- `research/booster_principle.md`;
- MareNostrum `research/DHITL.md`;
- MareNostrum `research/infrastructure_is_all_you_need.md`;
- FractaVolta `research/when_cognition_became_traffic.md`;
- PrivAI KYS profiles and conformance work.

These sources provide provenance and conceptual context. The eventual publication must cite external literature independently and must not rely on project vocabulary for its core argument.

## 19. External bibliography — provisional research ledger

The following items were identified during the initial Explorer pass and require normal bibliographic verification before submission:

- NIST, *AI Agent Standards Initiative* (2026): interoperability and secure agent operation on behalf of users.
- European Commission, *European Technological Sovereignty Package* and proposed *Cloud and AI Development Act* (2026): infrastructure-level sovereignty and assessment.
- European Commission, *Data Act* implementation material: switching and interoperability of data-processing services.
- European Commission, DMA interoperability and portability case studies (2026).
- Konigsberg, A., *Cognitive Sovereignty: The Authorship Problem in AI-Assisted Thought* (2026).
- Kakraba, S., Agyemang, E. F., & Srivastav, S. K., *Cognitive sovereignty and decolonial public health* (2026).
- Valente, S., *Cognitive Sovereignty: A Legal and Technical Framework for Protecting Human Identity in the Age of Relational AI* (2026).
- Canepa, F. S., *Cognitive Sovereignty: Protecting the Quality of Leadership Decisions in the Age of Artificial Intelligence* (2026).
- Chow, J., *Cognitive Sovereignty and the AI State — Beyond Data Sovereignty and Digital Sovereignty* (2026).
- Saracini, C., *Cognitive sovereignty and neuro-justice* (2026).

## 20. Reviewer queue

The first Reviewer pass should attack at least these points:

- Is "cognitive sovereignty" necessary terminology, or does existing work on agency/contestability suffice?
- Is conversational interposition genuinely novel as a measurement object?
- What is the closest prior art in observability, agent/tool telemetry, middleware interception, browser extensions, accessibility layers, personal AI agents, and MCP gateways?
- Can "user-controlled" be operationally defined without assuming infrastructure ownership?
- Which metrics are direct measurements and which are inferred constructs?
- Does repeated tool invocation meaningfully correlate with user autonomy, or merely with tool orchestration policy?
- What experiments could disconfirm the strongest interpretation?
- What privacy/security risks are introduced by a third party in the loop?
- How should results be normalised across hosts whose tool execution architectures differ fundamentally?
- What claims should remain in Discussion rather than Abstract/Results?

## Core invariant

> **The purpose is not to decide what the user should think. It is to make measurable the effective capacities by which the user can continue to decide for themselves while relying on external cognitive systems.**
