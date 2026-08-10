---
title: "Presencology — Presence Maps for the Rational Exploration of The Possible"
subtitle: "A proposed research programme linking presence, potentiality, stigmergy, distributed cognition, and procedural stabilization"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica, France"
license: "CC BY-SA 4.0"
language: "en"
date: "2026-08-10"
status: "working-paper — proposed research programme"
document_role: "source"
version: "0.2"
document_kind: "research-paper"
visibility: "public"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/presencology.md"
lifecycle_state: "working"
review:
  status: "unreviewed"
  reviewed_by: []
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "main"
  origin_date: "2026-08-10"
  derived_from:
    - "barons-Mariani/research/potentics.md"
    - "barons-Mariani/research/rational_odysseys_the_possible.md"
    - "barons-Mariani/research/second_method.md"
    - "inseme/research/cop_mission_stigmergy_exploration.md"
update_policy: "UP-DEFAULT-REVIEWED"
methodology:
  - "Second Method"
ai_assisted_by:
  - "GPT-5.6 Sol (Redactor drafting and internal critical review)"
  - "Claude Opus 5 (decorrelated adversarial review, reference verification, prior-art audit)"
changelog:
  - "v0.1 (2026-08-10) — first structured formulation of Presencology as a proposed research programme."
  - "v0.2 (2026-08-10) — human arbitration of A1 integrated: declared-vs-estimated retained as an internal epistemic distinction rather than the novelty boundary; PresenceClaim/PresenceEstimate distinction added."
  - "v0.2-review (2026-08-10) — decorrelated review pass: IETF presence prior art added to §2 and §16.8, novelty claims 2 and 3 narrowed, two references corrected from preprint to published venue, standards references added; residual bibliography placeholders resolved or deleted; Olé Olé relationship stated; RP-09 cross-referenced to §16.6; GEOPRIV threat analysis noted as model for RP-12; Continuation 2 marked partial."
---

# Presencology — Presence Maps for the Rational Exploration of The Possible

## Abstract

This paper proposes **Presencology** as a unifying research programme concerned with the representation, observation, estimation, dynamics, and forecasting of the presence of entities across space, time, and possible worlds. The proposal does not claim that the underlying problems are new. On the contrary, substantial adjacent work already exists in spatiotemporal statistics, occupancy modelling, human mobility forecasting, trajectory analysis, collective cognition, stigmergy, swarm intelligence, distributed systems, digital twins, and exploration–exploitation research. The proposed contribution is a common abstraction and a research agenda intended to connect problems that are usually treated separately.

A **Presence** is provisionally defined as an assertion that a subject is, was, will be, or might be present in a specified region of a space during a specified instant or interval, under an explicit epistemic or modal qualification. Presence is distinguished from the observation or evidence supporting it. A presence may concern a human, population, animal, vehicle, device, software agent, institution, event, or other addressable subject. The relevant space may be physical, conceptual, technical, legal, institutional, or a multidimensional region of **The Possible**.

Presencology is positioned beside **Potentics**, previously proposed as the rational exploration of The Possible. Potentics asks what may become actual and with what potentiality; Presencology asks how entities and explorers are distributed within projections of the spaces under consideration. Their conjunction supports a broader programme of **Rational Exploration of The Possible (REP)**. A Possibility or Potentiality Map indicates where potentially valuable regions may lie; a Presence Map indicates where agents are, have been, are expected to be, or could be. Their divergence can reveal candidate regions of under-exploration, while stigmergic traces preserve the consequences of previous exploration.

The paper further introduces the notion of a **Latent Functional Map**: a map need not exist as an explicit centralized representation. A distributed collective may function as if it possessed a map when the evolving configuration of presences, traces, local memories, environmental modifications, and interaction rules enables reliable orientation. Ant colonies provide a paradigmatic example without implying that insect cognition and artificial systems are identical. This perspective supports a procedural, distributed model of computer-assisted collective intelligence in which no omniscient central agent is required.

Presencology is deliberately presented as a **proposed field and open research programme**, not as an established discipline. The paper therefore ends with explicit objections, limits, and a first programme of research missions to be conducted under the principles of the *Second Method*: publish process as well as result, preserve objections as first-class contributions, maintain machine-readable provenance, and let the evolving corpus itself reveal whether the proposed framework is useful.

---

## 1. Introduction

Many technical and scientific systems need to answer variations of a simple question:

> **What is where, when?**

Ecologists estimate whether species occupy habitats despite imperfect detection. Mobility researchers estimate and forecast populations in spatial cells. Autonomous systems predict future occupancy of their surroundings. Network operators infer device density. Logistics systems track vehicles and goods. Digital twins maintain state estimates of physical or organizational systems. Multi-agent systems reason about where agents have explored and where they should explore next.

These problems share a structural family resemblance, yet they are normally divided by domain, substrate, and vocabulary.

Presencology proposes that **presence itself** can be treated as a cross-domain object of study.

The intention is not to erase domain-specific methods. A person in a town, a ship in a port, an ant on a trail, an AI agent in a conceptual search space, and a hypothetical institution in a counterfactual scenario are not equivalent phenomena. They nevertheless admit a common question:

\[
\mathrm{Presence}(s, X, \tau, m)
\]

where:

- \(s\) is a subject;
- \(X\) is a region in some relevant space;
- \(\tau\) is an instant or interval;
- \(m\) is a modality or epistemic status.

The value of the abstraction must be demonstrated rather than assumed. A useful cross-domain abstraction should allow concepts, methods, warnings, and algorithms to transfer where justified, while preserving distinctions where transfer would be misleading.

This requirement places Presencology naturally within the methodological commitments of the **Second Method**: the proposal should expose its derivation, its adjacent literatures, its objections, its failures, and the open questions that would determine whether the abstraction deserves to survive.

---

## 2. Epistemic Status and Claim of Novelty

Presencology is a **proposed unifying framework**, not a claim that no one has studied presence before.

Adjacent fields already include, among others:

- occupancy and presence/absence modelling;
- spatiotemporal point processes and spatial statistics;
- human mobility modelling and occupancy-count forecasting;
- trajectory mining and movement ecology;
- crowd dynamics;
- sensor fusion and probabilistic state estimation;
- autonomous-system occupancy forecasting;
- swarm intelligence and ant-colony methods;
- stigmergy;
- collective sensing and collective cognition;
- distributed artificial intelligence and multi-agent systems;
- novelty search, quality-diversity methods, and exploration–exploitation;
- digital twins and state-space representations;
- **standardized presence models in communication systems**, where "presence" has been a formally specified abstraction since RFC 2778 (presence service, presentity, watcher), with a wire format in PIDF (RFC 3863), a person/device/service decomposition in RFC 4479, rich qualification in RPID (RFC 4480), explicit past and future time intervals in RFC 4481, and a location-and-privacy framework in GEOPRIV (RFC 3693, RFC 3694, RFC 4119).

Recent work, for example, models human mobility as occupancy counts over spatial cells and forecasts those counts over time. Other work predicts future occupancy around autonomous systems. These are clearly neighbouring instances of the broader family of problems considered here.

Likewise, stigmergy has a mature literature describing indirect coordination through traces left in an environment. Ant colonies can use environmental chemical marks as information-bearing "road signs", and collective ant navigation can solve problems beyond the sensing range of any individual ant.

The proposed novelty of Presencology is therefore narrower:

1. to make **Presence** an explicit cross-domain abstraction;
2. to include past, present, scheduled, expected, predicted, conditional, and hypothetical presence under one qualified model;
3. to distinguish a presence claim from the observation or evidence that supports it;
4. to generalize presence beyond geographic space to conceptual and possible spaces;
5. to couple Presence Maps explicitly with **Potentiality Maps** from Potentics;
6. to study latent and explicit maps as products of distributed informational configurations;
7. to use this coupling as an operational substrate for Rational Exploration of The Possible.

Whether this combination is sufficiently useful to justify a distinct term is itself a research question.

---

## 3. A Provisional Ontology of Presence

### 3.1 Presence is not observation

A foundational distinction is:

\[
\boxed{\mathrm{Presence} \neq \mathrm{Observation}}
\]

A GPS sample, Wi-Fi count, reservation, ticket scan, timetable, declaration, sensor event, or model output is not itself the presence it suggests.

Instead:

\[
\mathrm{Evidence} \rightarrow \mathrm{supports} \rightarrow \mathrm{PresenceClaim}
\]

This distinction is necessary because evidence can be incomplete, contradictory, delayed, biased, or wrong.

For example:

- a GPS observation may support a person's past presence in Corte;
- a ferry ticket may support an expected future presence in Bastia;
- a timetable may support a scheduled presence of a train;
- a forecasting model may support a predicted aggregate presence in Calvi;
- a scenario model may support a hypothetical presence conditional on an event.

Multiple evidence sources may support or contradict the same claim without requiring destructive overwrite.

A further distinction is useful between a **Presence Claim** and a **Presence Estimate**. A claim is a qualified assertion attributable to a source. An estimate is a derived epistemic state that may synthesize several claims or evidence items:

\[
\hat{P}(s,X,\tau \mid E_1,\ldots,E_n)
\]

A declaration by the subject is therefore neither excluded nor ontologically privileged: it is one evidence modality among others. The estimation process may assign it particular weight according to provenance, context, reliability, and purpose, but must not erase its origin. This distinction is provisional and belongs to RP-01 and RP-05 for formalization.

### 3.2 Subject

The subject of a Presence may be:

- an individual person;
- an aggregate population;
- an animal;
- a vehicle;
- a vessel;
- a device;
- a physical object;
- a software agent;
- an organization;
- an event;
- another addressable entity.

A research question remains as to whether aggregates should be modelled as ordinary subjects or through a distinct occupancy/count construct.

### 3.3 Space

A Presence occurs relative to a space.

For ordinary geographic Presence, this may be a point, geometry, spatial cell, administrative area, route segment, building, or named place.

More generally, a space may be:

- physical;
- geographic;
- conceptual;
- technical;
- legal;
- institutional;
- economic;
- political;
- computational;
- a search space;
- a state space;
- a region of The Possible.

The generalization to non-physical spaces is not merely terminological. It requires explicit definitions of coordinates, dimensions, neighbourhood, distance, topology, accessibility, and resolution.

### 3.4 Time

A Presence may concern:

- the past;
- the present;
- a scheduled future;
- an expected future;
- a predicted future;
- a conditional future;
- a hypothetical world.

Temporal modelling should distinguish at least:

- **valid time** — when the presence is claimed to hold;
- **knowledge time** — when the system acquired or generated the claim.

This permits forecasts to be evaluated later without rewriting history.

### 3.5 Modality

A provisional vocabulary includes:

- observed;
- inferred;
- declared;
- scheduled;
- reserved;
- expected;
- predicted;
- conditional;
- possible;
- hypothetical.

These modalities must not be collapsed into a single confidence number. A scheduled train with a 0.99 operational confidence and a model prediction with 0.99 posterior probability are epistemically different objects.

### 3.6 Absence, non-observation, and unknown

Presencology must resist a common error:

\[
\mathrm{not\ observed} \not\Rightarrow \mathrm{absent}
\]

At minimum, it should distinguish:

- asserted absence;
- failed detection;
- missing observation;
- insufficient resolution;
- inaccessible evidence;
- unknown state.

This issue is already central in ecological occupancy modelling and is equally important in human mobility, sensor networks, and agentic exploration.

---

## 4. Presence Fields and Presence Maps

A collection of qualified Presence claims can be used to estimate a **Presence Field**.

For a geographic human population, one may write informally:

\[
\rho(x,y,t,c)
\]

where \(c\) is an optional class such as residents, visitors, vehicles, or anonymous devices.

A **Presence Map** is not identical to this field. It is a projection or representation selected for a purpose.

Examples include:

- a heatmap of people currently estimated in Corsican spatial cells;
- a historical map of seasonal visitor presence;
- a forecast map of human presence at 23:00;
- a map of exploratory software-agent activity in a conceptual search space.

The distinction between field and map matters because every map applies choices of:

- dimensions;
- projection;
- resolution;
- aggregation;
- smoothing;
- uncertainty representation;
- privacy transformation;
- temporal window.

---

## 5. The Possible as a Multidimensional Space

Potentics distinguishes local visible possibilities from **The Possible**, the wider domain of what reality has not forbidden under relevant constraints.

For Presencology, The Possible should not be imagined as a two-dimensional geographical surface.

Let:

\[
\Omega \subseteq D_1 \times D_2 \times \cdots \times D_n
\]

where dimensions may be continuous, discrete, symbolic, relational, hierarchical, or incompletely known.

A state in The Possible may involve dimensions such as:

- physical location;
- time;
- energy;
- compute;
- capital;
- law;
- institutional configuration;
- actors;
- knowledge;
- technical architecture;
- social acceptance;
- risk;
- reversibility;
- coordination capacity.

No claim is made that all these dimensions belong naturally to one Euclidean vector space. The notation is schematic.

### 5.1 Maps as projections

A map of The Possible is necessarily a projection:

\[
\pi_i : \Omega \rightarrow M_i
\]

where \(M_i\) is a lower-dimensional representation selected for a question.

Examples:

\[
\pi_{\text{cost,time}}(\Omega)
\]

or:

\[
\pi_{\text{energy,compute,latency}}(\Omega)
\]

or a legal–institutional projection.

The doctrinal invariant is:

> **No projection of The Possible should be mistaken for The Possible itself.**

A projection can create false neighbourhoods, merge distinct states, hide constraints, or produce apparent attractors that disappear in another view.

---

## 6. Potentics and Presencology

Potentics and Presencology are proposed as sibling perspectives within Rational Exploration of The Possible.

A compact distinction is:

> **Potentics maps what may actualize and with what potentiality.**

> **Presencology maps what occupies, has occupied, is expected to occupy, or might occupy relevant regions of the spaces under consideration.**

This gives two families of maps.

A **Potentiality Map** may estimate:

\[
\Pi_{\pi}(m,t)
\]

for a point or region \(m\) in projection \(\pi\).

A corresponding **Presence Map** may estimate:

\[
\rho_{\pi}(m,t)
\]

for explorers or other relevant entities.

Their relationship can reveal a candidate **Exploration Gap**.

The naive expression:

\[
G = \Pi - \rho
\]

is inadequate because potentiality and presence need not share units and because low presence may be rationally explained by cost, risk, inaccessible dimensions, or model error.

The deeper research problem is therefore:

> **Under what conditions does the joint structure of Potentiality Maps and Presence Maps provide actionable evidence that a region is underexplored?**

This should be treated as an empirical and formal problem, not as an assumed theorem.

---

## 7. Stigmergy: Presence, Trace, and Future Presence

Stigmergy is coordination through effects left in a shared environment.

Presencology clarifies a useful distinction:

\[
\boxed{\mathrm{Presence} \neq \mathrm{Trace}}
\]

A presence answers, roughly:

> where is or was the explorer?

A trace answers:

> what informational modification remains available to influence later action?

The basic loop is:

\[
\mathrm{Presence}
\rightarrow
\mathrm{Trace}
\rightarrow
\mathrm{Future\ Presence}
\]

A trace may be positive, negative, uncertain, or decaying. In a cognitive exploration system, rich traces may indicate:

- promising path;
- dead end;
- danger;
- contradiction;
- verified result;
- unresolved question;
- bridge to another domain;
- synthesis candidate;
- return required.

This extends insect stigmergy without pretending that pheromone trails and scientific arguments are equivalent. What transfers is the coordination pattern: an action modifies a medium, and the modification changes the distribution of later actions.

---

## 8. The Ant-Colony Analogy and Distributed Exploration

Ant colonies are useful not because they provide a metaphysics of intelligence but because they demonstrate that robust collective orientation can arise without an omniscient central map.

Individual ants may use local memory, path integration, landmarks, pheromones, and interactions. The colony additionally benefits from distributed sensing and environmental traces.

A colony can therefore exhibit navigational competence that exceeds the accessible representation of any single worker.

This motivates a distinction between an **explicit map** and a **functional map**.

### 8.1 Explicit map

An explicit map is an identifiable representation:

\[
M = \mathrm{graph,\ GIS,\ matrix,\ document,\ model,\ldots}
\]

### 8.2 Distributed explicit fragments

Information may be physically distributed across agents and media:

\[
M \approx M_1 \cup M_2 \cup \cdots \cup M_k
\]

although no single component contains the full representation.

### 8.3 Latent Functional Map

More radically, a system may exhibit map-like orientation while no explicit map exists anywhere.

Let the evolving state of a distributed system be:

\[
C(t)=\{
\text{presences},
\text{traces},
\text{agent states},
\text{local memories},
\text{environment},
\text{interaction rules}
\}
\]

The system **functionally possesses a map** to the extent that the structure and dynamics of \(C(t)\) enable action that is systematically sensitive to relevant relations in the space.

Provisional definition:

> **A Latent Functional Map is the map-like actionable structure embodied by an evolving distributed information configuration, whether or not an equivalent explicit representation is stored anywhere in the system.**

This is deliberately functional. It should be tested through interventions: if the environment changes, can the collective reorient in ways requiring sensitivity to the altered structure?

A major open question is how to define this criterion without making "map" synonymous with any adaptive state.

---

## 9. Maps, Supermaps, and Reconstruction

Different projections can constrain each other.

Suppose:

\[
\pi_1(\Omega), \pi_2(\Omega), \ldots, \pi_k(\Omega)
\]

produce partial maps from technical, legal, economic, social, geographic, or other perspectives.

Their alignment may reveal information absent from any individual map.

For example:

> technically feasible + economically favourable + legally permitted + socially blocked.

This motivates a **Supermap** concept, but the term requires care.

An **Explicit Supermap** is a revisable synthesis of several maps and their alignments, contradictions, uncertainties, and provenance.

It is not The Possible.

Nor should it be assumed to be the primary form of collective knowledge.

A distributed system may instead embody a richer **Latent Functional Map** than any explicit Supermap can reconstruct.

Thus:

\[
\mathrm{Latent\ Functional\ Map}
\xrightarrow{\mathrm{reconstruction}}
\mathrm{Explicit\ Supermap}
\]

may be intrinsically lossy.

Contradictions between maps must be preserved rather than erased. A disagreement may reveal:

- hidden dimensions;
- incompatible resolutions;
- faulty observations;
- invalid projections;
- genuine constraint conflicts.

The ability to retain unresolved contradictions is therefore part of the procedural stabilizer.

---

## 10. Rational Exploration of The Possible

The **Rational Exploration of The Possible** can now be described as a closed, but revisable, procedural loop.

\[
\mathrm{The\ Possible}
\rightarrow
\mathrm{Projections}
\rightarrow
\mathrm{Potentiality\ Maps}
\rightarrow
\mathrm{Exploration\ Missions}
\rightarrow
\mathrm{Presences}
\rightarrow
\mathrm{Traces}
\rightarrow
\mathrm{Updated\ Maps}
\]

A mission need not optimize a known objective over a fixed search space.

It may instead:

- discover previously unseen dimensions;
- invalidate a projection;
- reveal a hidden inhibitor;
- encounter a serendipitous attractor;
- document a dead end;
- create a new question;
- change the map by acting.

This is why rational exploration differs from one-shot optimization.

### 10.1 Exploration and exploitation

Dense presence in a region may indicate:

- high potentiality;
- ease of access;
- imitation;
- institutional inertia;
- path dependence;
- publicity;
- an artefact of the observation system.

Thus:

\[
\mathrm{PresenceDensity} \not\Rightarrow \mathrm{Potentiality}
\]

A rational system must preserve minority exploration, including missions toward regions with:

- high estimated potentiality and low exploratory presence;
- high uncertainty;
- low prior presence for reasons not yet understood;
- unknown dimensions or weakly mapped frontiers.

This connects Presencology to exploration–exploitation research, novelty search, and quality-diversity methods without reducing REP to any one of them.

---

## 11. Procedural Stabilization

The broader objective is not metaphysical.

The engineering problem is:

> **How can computer-assisted human collectives remain oriented, accountable, and capable of correction in environments too complex for any individual to represent completely?**

The proposed answer is procedural.

A **Procedural Stabilizer** maintains capabilities such as:

\[
\mathrm{Observe}
\rightarrow
\mathrm{Trace}
\rightarrow
\mathrm{Compare}
\rightarrow
\mathrm{Deliberate}
\rightarrow
\mathrm{Act}
\rightarrow
\mathrm{Observe}
\]

The stabilizer does not make reality static.

Instead:

> **stability means preserving the capacity to detect error and correct course.**

Within this architecture:

- Presencology contributes orientation;
- Potentics contributes structured attention to unrealized potential;
- stigmergy contributes distributed memory and coordination;
- provenance preserves evidential lineage;
- mandates govern who may act for whom;
- digital twins maintain operational representations;
- human governance retains responsibility for engaging decisions.

A crucial anti-capture requirement follows:

> **The procedural stabilizer must itself be procedurally stabilizable.**

Its ontologies, maps, fusion rules, exploration policies, and algorithms must remain versioned, contestable, inspectable, and revisable.

---

## 12. First Experimental Domain: Human Presence Weather

Geographic human presence provides an unusually convenient experimental domain because maps and coordinate systems already exist.

A service may estimate:

\[
\rho(\text{latitude},\text{longitude},t,c)
\]

from heterogeneous evidence such as:

- voluntary mobile-app contributions;
- privacy-preserving partner applications;
- aggregated telecommunications data (subject to the constraints of RP-11 and applicable data-protection regimes);
- Wi-Fi occupancy counts;
- transport flows;
- events;
- reservations;
- public and commercial observations.

The resulting application can expose a **weather of presence**:

- current estimated presence;
- historical patterns;
- forecasts;
- anomalies;
- confidence and coverage.

A playful public interface (provisionally named **Olé Olé**) is intended only as one possible entry point to a more general **Presence** infrastructure; it is an implementation sketch, not a claim that the research programme exists to justify a product. It supplies a concrete testbed for privacy, uncertainty, multi-source fusion, forecasting, identity separation, and network effects.

The conceptual importance of this domain is methodological:

> **It tests Presencology in a space for which society already possesses mature explicit maps.**

Only after these primitives survive the geographic case should their generalization to conceptual and possible spaces be considered convincing.

---

## 13. Second Experimental Domain: Cognitive Exploration

The second experimental domain is deliberately very different.

Consider a distributed system of human and artificial explorers investigating a multidimensional possible-space.

Each explorer may have:

- limited compute;
- a specialized reference corpus;
- a partial projection;
- local memory;
- a mission;
- a budget;
- access to shared traces.

A mission produces a trajectory through a projection of The Possible.

Presencology can then ask:

- which regions have been explored?
- by which kinds of agents?
- how recently?
- under which assumptions?
- with which traces?
- where do agents converge?
- what regions remain untouched?
- where does low presence conflict with high estimated potentiality?
- where does high presence result from self-reinforcing imitation?

The same machinery used to build a geographic Presence Map can thus inspire a **Research Presence Map**, while preserving the deep differences between physical and conceptual space.

---

## 14. Research Agenda

Presencology should begin with a list of problems that may invalidate, constrain, or refine it.

### RP-01 — Ontology of Presence

Determine the minimal distinctions among:

- Presence;
- PresenceClaim;
- PresenceEstimate;
- Absence;
- Unknown;
- NonObservation;
- Observation;
- Evidence;
- Location;
- Occupancy;
- Movement;
- Trajectory;
- Flow;
- Trace;
- Subject;
- Aggregate;
- Scenario.

**Failure condition:** the abstraction becomes either domain-specific or so general that it explains nothing.

### RP-02 — Formal Spaces and Projections

Define how Presencology applies to spaces that are:

- Euclidean;
- graph-based;
- symbolic;
- categorical;
- relational;
- hierarchical;
- mixed;
- incompletely known.

Specify projection metadata, retained and collapsed dimensions, distortion, resolution, and domain of validity.

### RP-03 — Functional Map Criterion

Define an operational test for whether a distributed system functionally possesses a map.

Candidate requirement:

> intervention on relevant spatial structure produces adaptive behaviour that depends on information about that structure.

**Open objection:** this may still classify too many generic adaptive systems as map-bearing.

### RP-04 — Latent-to-Explicit Reconstruction

Study when and how an Explicit Supermap can be reconstructed from:

- presences;
- trajectories;
- traces;
- local memories;
- interactions;
- environmental state.

Characterize information loss and non-identifiability.

### RP-05 — Evidence Fusion

Compare methods for combining heterogeneous and contradictory evidence:

- Bayesian inference;
- state-space estimation;
- belief functions;
- possibility-theoretic approaches;
- robust statistics;
- ensemble methods.

No fusion rule should erase provenance.

### RP-06 — Temporal Semantics

Formalize:

- valid time;
- knowledge time;
- prediction time;
- scenario time;
- recurrence;
- seasonality;
- persistence;
- decay;
- revision.

### RP-07 — Multi-Resolution Presence

Define consistency conditions between assertions such as:

> present in Corte;

> present in a particular building in Corte.

Spatial and conceptual maps require multi-scale reasoning without forcing false exclusivity.

### RP-08 — Potentiality–Presence Coupling

Test whether Presence Maps improve the allocation of exploratory effort when combined with Potentiality Maps.

Compare against:

- random exploration;
- novelty-driven exploration;
- uncertainty sampling;
- exploitative policies;
- quality-diversity methods.

### RP-09 — Reflexivity

Study how publishing maps changes the presences being mapped.

Examples include:

- a nightlife heatmap attracting people to an already-hot location;
- an exploration dashboard drawing agents to a supposedly underexplored branch.

The measuring system becomes part of the causal system. This research problem is the operational counterpart of the objection stated in §16.6.

### RP-10 — Stigmergic Dynamics

Study:

\[
\mathrm{Presence}
\rightarrow
\mathrm{Trace}
\rightarrow
\mathrm{FuturePresence}
\]

under:

- reinforcement;
- decay;
- negative traces;
- contradiction;
- adversarial traces;
- stale information;
- multiple agent classes.

### RP-11 — Privacy and Visibility Governance

Define who may:

- observe;
- infer;
- store;
- aggregate;
- publish;
- predict;
- link identities to presences.

A Presence infrastructure that improves collective orientation can also become a surveillance infrastructure. Evidence sources listed in §12 that involve aggregated telecommunications data fall under this problem and under applicable regimes (GDPR, ePrivacy Directive and successor instruments).

### RP-12 — Procedural Anti-Capture

Ensure that the stabilizer itself cannot silently become a central gatekeeper.

Research requirements include:

- inspectable rules;
- reversible ontologies;
- plural maps;
- preserved contradictions;
- federated participation;
- explicit mandates;
- auditability;
- provider substitution.

RFC 3694 (Threat Analysis of the Geopriv Protocol) supplies a concrete, two-decade-old model of publishing a threat analysis alongside a data format; the same discipline is required here.

### RP-13 — Evaluation Metrics

Candidate metrics include:

- coverage;
- epistemic gain;
- uncertainty reduction;
- novelty discovered;
- value discovered;
- cost per useful discovery;
- diversity of explored regions;
- correction latency;
- map calibration;
- robustness to missing or adversarial observations.

No single metric should be assumed sufficient.

### RP-14 — Discipline Boundary

Test whether Presencology is best understood as:

1. a distinct discipline;
2. an interdisciplinary research programme;
3. an ontology;
4. an engineering layer;
5. a vocabulary connecting existing fields.

A documented result that option 1 is unnecessary would still be a successful research outcome.

---

## 15. Applying the Second Method to Presencology

The construction of Presencology should itself instantiate the method it proposes to support.

The research process should therefore preserve:

- drafts;
- objections;
- review reports;
- rejected formulations with reasons when material;
- open problems;
- experimental failures;
- versioned definitions;
- changes in terminology;
- links to evidence;
- explicit uncertainty.

Each Research Problem may become a **Mission**.

A mission can contain:

- question;
- possible-space;
- mandate;
- scout agents;
- contradictor agents;
- cartographer;
- evidence boundary;
- experiment;
- return protocol;
- result;
- map update;
- continuation.

This yields a reflexive experimental loop:

\[
\mathrm{Potentics}
\rightarrow
\mathrm{Research\ Possibility\ Map}
\rightarrow
\mathrm{REP}
\rightarrow
\mathrm{Research\ Missions}
\rightarrow
\mathrm{Presence + Traces}
\rightarrow
\mathrm{Updated\ Map}
\]

Presencology can therefore become one of its own first experimental subjects.

---

## 16. Open Objections and Known Limits

This first formulation deliberately leaves several load-bearing questions unresolved.

### 16.1 "Presence" may be too broad

The term may collapse distinct phenomena whose methods do not transfer usefully.

### 16.2 Non-physical presence may remain metaphorical

The extension from geographic to conceptual and possible spaces requires operational definitions. Without them, "presence in The Possible" risks being only rhetoric.

### 16.3 The functional-map concept may be trivial

If every system whose state affects later behaviour is said to possess a map, the concept loses discriminating power.

### 16.4 Supermap reconstruction may be impossible in principle

Distinct distributed configurations may produce observationally identical collective behaviour. A unique explicit reconstruction may therefore not exist.

### 16.5 Potentiality and presence are not naturally commensurable

An Exploration Gap cannot be treated as a simple arithmetic difference.

### 16.6 Observation changes behaviour

Especially for human systems, publishing presence information may reshape the field being estimated. (See also RP-09.)

### 16.7 Privacy constraints may limit observability

The most socially acceptable system may deliberately prevent the very individual-level reconstruction that would make modelling easier.

### 16.8 Existing fields may already provide sufficient vocabulary

If the proposed framework adds no predictive, explanatory, engineering, or organizational value beyond existing concepts, Presencology should remain a local vocabulary rather than claim disciplinary status.

This objection has a concrete instance that must be answered rather than acknowledged in the abstract. The IETF presence family already provides a formally specified subject (`presentity`), an observer (`watcher`), a mediating service, an extensible tuple format, a person/device/service decomposition, qualified status beyond binary open/closed, past and future validity intervals, and — through GEOPRIV — a location model published together with its own threat analysis and privacy requirements. That is an ontology, an interchange format, a temporal semantics and a disclosure-governance framework for presence, deployed at scale for two decades.

Presencology therefore does **not** claim novelty for presence as a formal information object, nor for temporal, qualified, or location-aware presence. Its proposed contribution is to investigate whether a broader cross-domain framework becomes useful when declared presence is treated as one evidence modality among others; presence is generalized to heterogeneous physical and non-physical spaces; evidence from cooperative and non-cooperative sources can remain distinct and be fused without loss of provenance; explicit maps are related to latent distributed informational configurations; and Presence Maps are coupled with Potentiality Maps for Rational Exploration of The Possible.

The distinction between **declared** and **estimated** presence is consequently internal to Presencology rather than its boundary with the IETF family. A subject declaration, a sensor observation, a reservation, a timetable, a third-party report, and a model prediction may all contribute qualified evidence about presence while retaining their different provenance and epistemic status. The remaining novelty question is therefore not whether earlier presence vocabularies exist — they clearly do — but whether this wider conjunction has enough explanatory, predictive, engineering, or organizational value to justify Presencology as a distinct research programme.

These are not defects to hide. They define the initial research programme.

---

## 17. Conclusion

Presencology begins from a simple observation: many systems need to reason not only about what exists or what might exist, but about **what is where, when, according to which evidence and under which modality**.

Its proposed contribution is to make this structure explicit and general enough to connect physical presence, occupancy, movement, distributed exploration, stigmergy, and possible-space reasoning.

The central relationship is not:

\[
\mathrm{Presence} = \mathrm{Potentiality}
\]

but:

\[
\boxed{
\mathrm{Potentiality\ Maps}
+
\mathrm{Presence\ Maps}
+
\mathrm{Trace\ Maps}
\rightarrow
\mathrm{Rational\ Exploration}
}
\]

Each map is partial. The Possible is multidimensional. Projections distort. Contradictions matter. The collective may embody a richer map than any central representation can store.

The ant-colony analogy captures the architectural intuition: a colony may orient effectively without any ant possessing the colony's map and without a map existing as a single physical artefact. The relevant "map" may instead be embodied by the evolving configuration of agents, presences, traces, environmental modifications, memories, and interaction rules.

For computer-assisted collective intelligence, this suggests an alternative to the omniscient central agent. The objective is not to centralize every representation, but to build **procedures that preserve orientation, evidence, plurality, correction, and return**.

Presencology is therefore proposed neither as a settled science nor as a metaphysical thesis. It is a research programme.

Its first obligation is to test whether it deserves to exist.

---

## References — initial working set

> **Bibliographic status:** working list with placeholders resolved. Primary-source verification of pagination and exact titles remains advisable before final stabilization. Internal self-review does not clear `review.status: unreviewed`.

- Bonabeau, E., Dorigo, M., & Theraulaz, G. (1999). *Swarm Intelligence: From Natural to Artificial Systems*. Oxford University Press.
- Grassé, P.-P. (1959). La reconstruction du nid et les coordinations interindividuelles chez *Bellicositermes natalensis* et *Cubitermes* sp. La théorie de la stigmergie: Essai d’interprétation du comportement des termites constructeurs. *Insectes Sociaux*, 6(1), 41–80. https://doi.org/10.1007/BF02223791
- Theraulaz, G., & Bonabeau, E. (1999). A brief history of stigmergy. *Artificial Life*, 5(2), 97–116. https://doi.org/10.1162/106454699568700
- Wystrach, A., Beugnon, G., & Cheng, K. (2011). Landmarks or panoramas: what do navigating ants attend to for guidance? *Frontiers in Zoology*, 8, 21. https://doi.org/10.1186/1742-9994-8-21
- Fonio, E., Heyman, Y., Boczkowski, L., Gelblum, A., Kosowski, A., Korman, A., & Feinerman, O. (2016). A locally-blazed ant trail achieves efficient collective navigation despite limited information. *eLife*, 5, e20185. https://doi.org/10.7554/eLife.20185
- Gelblum, A., Fonio, E., Rodeh, Y., Korman, A., & Feinerman, O. (2020). Ant collective cognition allows for efficient navigation through disordered environments. *eLife*, 9, e55195. https://doi.org/10.7554/eLife.55195
- Pherwani, P., Hass, N., & Yanchenko, A. K. (2024). Spatiotemporal Modeling and Forecasting at Scale with Dynamic Generalized Linear Models. In *Proceedings of the 1st ACM SIGSPATIAL International Workshop on Geospatial Anomaly Detection (GeoAnomalies’24)*, Atlanta, GA, 16–27. https://doi.org/10.1145/3681765.3698449 (arXiv:2410.07161)
- Toyungyernsub, M., Yel, E., Li, J., & Kochenderfer, M. J. (2022). Dynamics-Aware Spatiotemporal Occupancy Prediction in Urban Environments. In *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 10836–10841. (arXiv:2209.13172)
- Day, M., Rosenberg, J., & Sugano, H. (2000). *A Model for Presence and Instant Messaging*. RFC 2778.
- Sugano, H., Fujimoto, S., Klyne, G., Bateman, A., Carr, W., & Peterson, J. (2004). *Presence Information Data Format (PIDF)*. RFC 3863.
- Rosenberg, J. (2006). *A Data Model for Presence*. RFC 4479.
- Schulzrinne, H. et al. (2006). *RPID: Rich Presence Extensions to PIDF*. RFC 4480.
- Schulzrinne, H. (2006). *Timed Presence Extensions to PIDF for Past and Future Time Intervals*. RFC 4481.
- Cuellar, J., Morris, J., Mulligan, D., Peterson, J., & Polk, J. (2004). *Geopriv Requirements*. RFC 3693; and Danley, M. et al. (2004). *Threat Analysis of the Geopriv Protocol*. RFC 3694.
- Peterson, J. (2005). *A Presence-based GEOPRIV Location Object Format*. RFC 4119.
- Dorigo, M., Maniezzo, V., & Colorni, A. (1996). Ant system: optimization by a colony of cooperating agents. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)*, 26(1), 29–41. https://doi.org/10.1109/3477.484436
- Lehman, J., & Stanley, K. O. (2011). Abandoning objectives: Evolution through the search for novelty alone. *Evolutionary Computation*, 19(2), 189–223. https://doi.org/10.1162/EVCO_a_00025
- Mouret, J.-B., & Clune, J. (2015). Illuminating search spaces by mapping elites. arXiv:1504.04909.
- Robert, J. H. N. (2026). *What is Potentics? Toward a Science of the Possible*. Barons Mariani corpus.
- Robert, J. H. N. (2026). *Rational Odysseys into The Possible*. Barons Mariani corpus.
- Robert, J. H. N. (2026). *Discours de la seconde méthode*. Barons Mariani corpus.
