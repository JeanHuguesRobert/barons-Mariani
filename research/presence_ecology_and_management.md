---
title: "Presence Ecology and Management — From Presence Maps to Agentic Presence Strategy"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-09-06"
version: "0.1"
license: "CC BY-SA 4.0"
language: "en"
status: "working-paper"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/presence_ecology_and_management.md"
last_stamped_at: "unknown"
update_policy: "UP-DEFAULT-REVIEWED"
document_role: "source-addendum"
document_kind: "research-note"
visibility: "public"
lifecycle_state: "working"
methodology:
  - "Cogentia Commons"
  - "Living Frontmatter candidate — Cogentia #159"
ai_assisted_by:
  - "GPT-5.6 Sol — research, structuring and drafting assistance"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unavailable"
  origin_date: "2026-09-06"
  derived_from:
    - "research/presencology.md"
    - "research/presencology_digital_social_presence_twins.md"
  origin:
    kind: "conversation"
    ref:
      status: "unavailable"
      reason: "No durable conversation identifier is currently materialized in the corpus."
    date: "2026-09-06"
  derivation:
    from:
      - "research/presencology.md"
      - "research/presencology_digital_social_presence_twins.md"
      - "JeanHuguesRobert/inseme:research/interactions_registry_and_multichannel_messaging.md"
      - "JeanHuguesRobert/inseme:research/discord_edge.md"
      - "JeanHuguesRobert/cogentia:research/byoc_external_interaction_edges.md"
  materialization:
    repository: "JeanHuguesRobert/barons-Mariani"
    path: "research/presence_ecology_and_management.md"
    initial_commit: "72a2f9435829fed5a78900ab0b08625383c9d262"
review:
  status: "unreviewed"
  reviewed_by: []
related_documents:
  - "research/presencology.md"
  - "research/presencology_digital_social_presence_twins.md"
  - "JeanHuguesRobert/inseme:research/interactions_registry_and_multichannel_messaging.md"
  - "JeanHuguesRobert/inseme:research/discord_edge.md"
  - "JeanHuguesRobert/cogentia:research/byoc_external_interaction_edges.md"
  - "JeanHuguesRobert/barons-Mariani#56"
  - "JeanHuguesRobert/cogentia#159"
---

# Presence Ecology and Management

## Abstract

Presencology models Presence as a qualified relation between a subject, a space and time. This working paper explores a consequence of that abstraction: a subject can hold multiple simultaneous Presences in heterogeneous physical, digital, social, technical, institutional, political, computational and conceptual spaces, and these Presences can interact with one another while consuming finite resources.

The paper proposes a deliberately provisional vocabulary for reasoning about such ensembles: **Presence Portfolio**, **Presence Strategy**, **Presence Gap**, **Presence Vitality**, **Presence Debt**, **Presence Ecology**, and **Presence Management Capability**. These terms are not proposed as replacements for existing work on channel portfolios, omnichannel management, organizational identity, attention allocation, online-community ecology, dynamic capabilities or platform dependency. Rather, the research question is whether Presencology provides a useful common abstraction across domains that those literatures usually study separately, and whether Personal and Collective Digital Twins can operationally maintain such Presences under explicit mandates, budgets and provenance constraints.

The first proposed Reality Test is intentionally mundane: establish and operate a normal Discord Presence for FractaVolta, then observe how it interacts with FractaVolta's Web, GitHub, social, agentic and physical Presences.

## 1. Scope and epistemic status

This is a **v0.1 working hypothesis document**. It does not modify the foundational definition of Presence in `presencology.md`, and it should not be read as claiming novelty for concepts that already have established counterparts in neighboring literatures.

The underlying Presencology abstraction remains:

```text
Presence(subject, space, time, modality)
```

The subject may be a human, software agent, Personal Digital Twin, Collective Digital Twin, institution or another addressable subject. The space need not be geographic.

This paper asks a downstream question:

> What follows when the same subject maintains many Presences across heterogeneous spaces, when those Presences interact, and when maintaining them consumes finite human, agentic, computational, financial and governance resources?

## 2. Prior art and neighboring fields

The proposed framework intersects several established bodies of work. The purpose of this section is boundary-setting rather than novelty claiming.

### 2.1 Channel portfolios and omnichannel management

Marketing, retail and service research already studies channel portfolios, channel proliferation, channel choice and omnichannel integration. Organizations choose combinations of physical and digital touchpoints and must allocate resources to integrate them.

Consequently, **Presence Portfolio must not be presented merely as a new name for a set of communication or marketing channels**. Its possible added value is broader scope: Presencology can describe Presence in a Discord community, GitHub repository, physical territory, institution, scientific community, political body or computational search space using the same underlying relation.

### 2.2 Organizational and digital identity

Research on organizational identity and digital platforms shows that organizational identity is projected and negotiated through heterogeneous platform-specific interactions. This supports, but does not originate from, the distinction already made in the Presencology digital/social addendum:

```text
identity != persona != account != Presence
```

A Collective Twin can provide continuity above platform-specific accounts without requiring identical behavior or persona on every platform.

### 2.3 Attention as a finite organizational resource

The Attention-Based View and related organizational research treat attention as scarce and allocated among competing issues and opportunities. Online communities likewise compete for members' time and effort.

Cogentia's Human Attention Budget gives this general observation an operational expression: opening or maintaining another Presence should not be treated as cost-free merely because the external account itself is free.

### 2.4 Online-community ecology

Research on online communities has modeled competition for overlapping member attention and, more recently, changing relations of competition and mutualism among communities. This provides legitimate prior art for investigating ecological relations among some kinds of social Presence.

It does **not** by itself prove that ecological terminology transfers to every arbitrary Presence. That transfer remains a hypothesis to test.

### 2.5 Dynamic capabilities

The dynamic-capabilities literature emphasizes organizational abilities to sense changes, seize opportunities and transform resources/configurations. The Presence Management loop proposed below resembles that pattern. The relationship should therefore be treated as inheritance/analogy to established theory, not as an independently invented management cycle.

### 2.6 Platform dependence and abandonment

Research on social-platform use documents abandoned organizational accounts, opportunity costs, resource rationalization, platform power and dependency. These phenomena motivate the proposed term **Presence Debt**, but the underlying phenomena are not new.

The research question is whether a common Presence-level concept adds explanatory and operational value across heterogeneous spaces.

## 3. From a Presence Set to a Presence Portfolio

For a subject `S`, one can consider the set of relevant Presence claims at time `t`:

```text
PresenceSet(S, t) = { P1, P2, ... Pn }
```

For FractaVolta this might include, at different times and modalities:

```text
Presence(FractaVolta, Web, t, active)
Presence(FractaVolta, GitHub, t, active)
Presence(FractaVolta, Discord, t, proposed)
Presence(FractaVolta, LinkedIn, t, ...)
Presence(FractaVolta, Corte, t, ...)
Presence(FractaVolta, energy-event-X, t, scheduled)
```

A **Presence Portfolio** is provisionally defined not as a new fundamental object but as a purpose-bounded projection over Presence claims:

```text
PresencePortfolio(S, purpose, t)
  = selected projection of PresenceClaims concerning S
```

Examples include a public-communication portfolio, research-collaboration portfolio, territorial portfolio, institutional portfolio or operational-support portfolio.

This preserves the source-owned Presence claims and avoids creating a competing ontology.

## 4. Presence Strategy and Presence Gaps

A descriptive map answers:

> Where is the subject present?

Strategy asks:

> Where should the subject attempt to be present, why, under what modality, and at what cost/risk?

A **Presence Strategy** is therefore a policy for selecting, maintaining, transforming and retiring Presences in relation to objectives and constraints.

A **Presence Gap** is a difference between a desired/required Presence state and the best current Presence estimate.

```text
actual / estimated Presence
          |
          | compare
          v
possible / desired Presence
          |
          v
      Presence Gap
          |
          v
    candidate action
```

This creates a natural bridge to Potentics: Presencology can describe actual, claimed, inferred, expected or possible Presence, while Potentics explores possible states. Strategy selects some possibilities for attempted actualization.

## 5. Presence lifecycle

Presences should not be assumed permanent. A provisional lifecycle vocabulary is:

```text
proposed
   |
provisional
   |
active
   |
maintained
  /        \
dormant   degraded
  \        /
    retired
```

These are management states, not replacements for Presencology modalities. A Presence may, for example, be `scheduled` epistemically/modally while its management lifecycle is `provisional`.

Retirement is a normal management operation. Keeping a misleading, unsafe or unmaintainable Presence indefinitely is not inherently preferable to closing it cleanly.

## 6. Presence Vitality

A technically existing Presence may be practically dead. Account existence therefore cannot be equated with effective Presence.

**Presence Vitality** is proposed as a multidimensional estimate of how effectively a Presence remains alive relative to its purpose. Candidate dimensions include:

- freshness;
- responsiveness;
- useful interaction;
- continuity;
- maintained provenance and identity binding;
- adequacy to declared purpose;
- participant activity where relevant;
- operational health where relevant.

No universal scalar `VitalityScore` is assumed. Different Presence types and purposes require different evidence. A small technical community may be highly vital with few participants, while a large follower count can coexist with a practically abandoned Presence.

## 7. Presence Debt

### 7.1 Provisional definition

**Presence Debt** is the accumulated liability created when a subject continues to project or maintain a Presence whose expectations, obligations, risks or maintenance requirements exceed the resources and mandates actually allocated to sustain it appropriately.

The metaphor intentionally resembles technical debt but should not be confused with a claim that all Presence Debt can be measured in a single unit.

### 7.2 Candidate forms

```text
Presence Debt
  |
  +-- Maintenance Debt
  |     stale information, broken integrations, obsolete bindings
  |
  +-- Interaction Debt
  |     unanswered consequential questions or obligations
  |
  +-- Expectation Debt
  |     apparent availability that is not actually provided
  |
  +-- Governance Debt
  |     obsolete roles, permissions, moderation or ownership
  |
  +-- Dependency Debt
        increasing dependence on a provider or external space
```

These categories are hypotheses for operational usefulness. They may overlap and should be revised if Reality does not support the distinctions.

### 7.3 A tentative management rule

```text
Do not create a durable Presence
without considering its maintenance mandate and budget.
```

This is a management heuristic, not a Presencology axiom.

## 8. Presence Ecology

A subject's Presences need not be independent. Their interactions can alter the costs, benefits and behavior of one another.

For example:

```text
Discord -> GitHub
  community discussion exposes a bug or idea

GitHub -> Discord
  durable work produces an update for the community

Web -> Discord
  publication recruits participants

physical event <-> social Presence
  attendance and online interaction reinforce one another
```

Candidate inter-Presence relations include:

- **competition** — Presences compete for scarce participant or organizational attention;
- **mutualism** — activity in each Presence increases the usefulness or viability of the other;
- **dependency** — one Presence requires another or its provider/infrastructure;
- **substitution** — one Presence can replace another for a purpose;
- **amplification** — one Presence increases the reach/effect of another;
- **duplication** — multiple Presences consume resources while providing substantially redundant function.

The term **Presence Ecology** denotes the study or operational representation of these interacting Presences and their resource environment.

The ecological analogy must remain falsifiable. It is useful only where it improves explanation, prediction or action; it should not become decorative vocabulary.

## 9. Resource model

A Presence can both capture and consume resources.

A simplified causal sketch is:

```text
Presence
  -> visibility / availability
  -> attention received
  -> interaction
  -> possible value

Presence
  -> updates / questions / moderation / obligations
  -> human + agent + compute + governance attention
  -> maintenance cost and risk
```

A deliberately non-scalar decomposition is preferable to premature optimization:

```text
PresenceResourceDemand(P) = {
  human_attention,
  agent_attention,
  compute,
  money,
  moderation,
  governance,
  maintenance,
  dependency_risk
}
```

These dimensions can later be accounted for by Cogentia/COP where appropriate.

## 10. Presence Management Capability

A **Presence Management Capability** is provisionally the capability of a subject, organization or Twin to manage the lifecycle and ecology of its Presences under explicit objectives and constraints.

A candidate loop is:

```text
Sense
  discover spaces, changes, opportunities and degradation

Evaluate
  estimate purpose, value, cost, risk and dependency

Select
  choose desired Presences and allocate resources

Instantiate
  establish a Presence

Integrate
  connect it with identity, interaction and other Presences

Maintain
  respond, update, moderate and repair

Observe
  collect evidence of what actually happens

Adapt
  revise strategy, budgets, mandates and behavior

Retire
  close or withdraw cleanly when justified
```

This loop overlaps substantially with dynamic-capabilities theory. Its potential contribution is operationalization through Twins and explicit agentic governance rather than invention of the general management pattern.

## 11. Agentic Presence Management

Personal and Collective Digital Twins may change the economics of maintaining multiple Presences.

Traditionally, an additional channel or Presence often implies additional human workload. An agentic system can route routine work to agents and reserve human attention for uncertainty, importance, risk, value conflict or explicit human preference.

```text
new interaction
      |
      v
agent handling under mandate
      |
      +-- routine/reversible -> agent continuation
      +-- specialist need    -> specialist agent/tool
      +-- high STAKE/risk    -> human escalation
```

The important constraint is that technical capability is not authority:

```text
Presence != Capability != Permission != Mandate != Authority != Act
```

Platform permissions, even in a space operated by the subject, do not create institutional authority. Agent activity remains bounded by mandate, budget, disclosure and provenance requirements.

## 12. Relation to Cogentia and Fractanet

Presencology supplies the generic concept of Presence. Cogentia can supply operational mechanisms around it:

- identity and Twin continuity above platform accounts;
- mandates and authority boundaries;
- Human Attention Budgets and other budgets;
- Interaction Packets;
- governed Conversations and Continuations;
- provenance and causal trace;
- accounting;
- agents and routing.

These mechanisms should not be retroactively treated as constitutive parts of Presencology itself.

At Fractanet scale, subjects may inhabit many overlapping networks. Their Presences form interfaces between the subject and those networks. A network-of-networks therefore naturally contains a changing topology of Presence relations without requiring any single network or platform to become canonical.

## 13. Relation to Potentics and `Le Réel Répond`

The proposed operational loop is:

```text
Presencology
  maps actual / claimed / expected Presence
        |
Potentics
  explores possible Presence
        |
Presence Strategy
  selects desirable possibilities
        |
Action
  attempts actualization
        |
Le Réel Répond
  produces consequences and evidence
        |
Presence Estimates
  are revised
        |
Vitality / Value / Debt / Ecology
  are re-estimated
        |
Strategy
  is revised
```

This is intended as an experimental loop. A Presence Strategy should be corrigible when the observed consequences differ from expectations, including unexpected and Black-Swan-like events that invalidate prior models.

## 14. Falsifiable research hypotheses

The framework should generate propositions that can fail.

### H1 — Agentic Presence Capacity

At comparable human-attention budget, a correctly governed Twin can maintain more useful Presences than an otherwise comparable purely human workflow without proportional degradation of service quality.

### H2 — Integration effect

For some pairs of Presences, integration reduces marginal maintenance cost or increases combined usefulness relative to operating the Presences independently.

### H3 — Presence Debt effect

Increasing unresolved Presence Debt predicts measurable degradation in one or more purpose-relevant outcomes such as responsiveness, correctness, trust, conversion of interactions into durable work, or operational reliability.

### H4 — Inter-Presence mutualism

Some pairs or groups of Presences produce sustained positive cross-effects such that their combined purpose-relative value exceeds what is observed when they operate in isolation.

### H5 — Platform-dependency resilience

Subjects whose identity, consequential interaction history and continuations remain independent of a platform suffer less loss of operational continuity when that platform becomes unavailable or undesirable.

### H6 — Twin continuity

A logical Twin can preserve identity, consequential interactions, mandates and continuations across replacement or disappearance of a platform-specific Presence.

These hypotheses require operational definitions and experimental designs before they can be considered tested.

## 15. FractaVolta Discord Reality Test

### 15.1 Why Discord

The first Reality Test should be ordinary rather than exotic. Many companies and open-source projects maintain a Discord community as a normal institutional/social Presence. FractaVolta can do the same using a genuine Discord server fully integrated with the Discord ecosystem.

The experiment is not whether Discord itself works. The question is whether the surrounding Presence-management model provides useful additional capabilities.

### 15.2 Initial state

```text
t0:
  FractaVolta Web Presence        existing/observable
  FractaVolta GitHub Presence     existing/observable
  FractaVolta Discord Presence    absent/proposed
```

The creation of the Discord server attempts to actualize a clearly identified Presence Gap.

### 15.3 Minimum observations

Without prematurely inventing a universal metric, collect evidence such as:

- participants joining and remaining active;
- questions and discussions;
- response latency and resolution;
- human attention consumed;
- agent attention/compute consumed;
- proportion of interactions handled without human escalation;
- escalations and their causes;
- consequential interactions converted to Interaction Packets or GitHub work;
- GitHub events that resume Discord continuations;
- moderation/governance work;
- stale or unanswered obligations;
- failures of bindings/integrations;
- cross-Presence flows among Discord, GitHub, Web and physical activities.

### 15.4 What would count against the model

Evidence against strong forms of the proposed framework would include:

- Presence-management metadata costs more than it helps;
- agent handling increases rather than reduces human-attention burden;
- cross-Presence integration creates duplication without measurable benefit;
- proposed Debt categories do not help predict or correct degradation;
- Presence Ecology relations cannot be operationalized beyond metaphor;
- platform-independent continuation provides no practical resilience benefit.

## 16. Multi-entity replication

If the FractaVolta experiment is useful, the same mechanisms can later be tested with other Collective Twins, potentially including C.O.R.S.I.C.A., the Fonds de dotation Barons Mariani, Les Amis de Malou and other entities.

This replication is important because each entity has different purposes, publics, governance, resources and appropriate Presence portfolios. A generic Presence-management capability should preserve the common mechanism without forcing identical Presences on every organization.

The correct default is therefore not:

```text
every organization must have Discord
```

but:

```text
for each Subject:
  determine which Presences are useful,
  maintain them according to purpose and resources,
  and retire them when Reality no longer justifies them.
```

## 17. Research agenda

The next research cycle should:

1. strengthen the state-of-the-art review with primary academic sources;
2. determine whether `Presence Debt` or close equivalents already exist under other terminology;
3. formalize relations among Presence claims, management lifecycle and purpose-bounded projections;
4. operationalize Vitality without collapsing it into a universal score;
5. determine when ecological relations are empirically meaningful;
6. define measurable versions of H1-H6;
7. run the FractaVolta Discord Reality Test;
8. compare results across at least one additional Collective Twin;
9. feed observed failures back into the vocabulary and model.

## 18. Provisional conclusion

The potentially distinctive contribution is not any isolated term. Channel portfolios, attention scarcity, digital identity, community competition, dynamic capabilities, account abandonment and platform dependency all have substantial prior art.

The candidate contribution is their integration under a domain-general Presence abstraction:

```text
arbitrary Subjects
x heterogeneous Spaces
x temporal/modal Presence
x identity above platform bindings
x Presence lifecycle and strategy
x finite human/agent/resource budgets
x inter-Presence relations
x mandate/authority separation
x agentic maintenance
x experimental correction by Reality
```

Whether this synthesis is scientifically useful remains an empirical question. The framework should therefore advance through bounded Reality Tests and Redactor/Reviewer criticism rather than through vocabulary accumulation alone.