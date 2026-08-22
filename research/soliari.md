---
title: "Soliari — Corte Ski Station and Infrastructure-Light Mountain Access"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica, France"
date: "2026-08-22"
version: "0.2"
status: "working-note"
document_role: "source"
document_kind: "project-research-note"
visibility: "public"
lifecycle_state: "working"
language: "en"
license: "CC BY-SA 4.0"
external_source:
  - "https://soliari.wordpress.com/"
methodology:
  - "Second Method"
  - "Rational Exploration of Possibilities"
related_documents:
  - "research/potentics.md"
  - "research/potentics_interdependencies.md"
  - "research/rational_odysseys_the_possible.md"
  - "research/the_network_is_the_learning_computer.md"
  - "https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/capability_regimes.md"
tags:
  - soliari
  - corte
  - lattiniccia
  - punta-latiniccia
  - skiing
  - drones
  - raix
  - rational-exploration
  - potentics
  - explorer-machine
  - infrastructure-light
  - corsica
---

# Soliari

## Corte Ski Station and Infrastructure-Light Mountain Access

## 1. Status

**Soliari** is a long-running exploratory project concerning the possibility of a ski area linked to Corte and the Lattiniccia / Punta Latiniccia mountain area.

A public historical record exists at:

- https://soliari.wordpress.com/

The present document does not replace that archive. It creates a durable entry point in the current Corpus and connects the project to more recent work on Potentics, Rational Exploration of Possibilities, RAIX, and the Explorer Machine.

The project should be understood as a **continuation and transformation of an older Corte / Lattiniccia ski-station idea**, not as an isolated proposal originating with drones.

## 2. Pre-Soliari lineage: the older Lattiniccia project

The idea of a ski station above Corte substantially predates Soliari.

The Soliari archive itself states in January 2012 that a centre-Corsica ski station had been discussed for a very long time under the name **Projet Lattiniccia**, after the mountain dominating the proposed area. That post also points to an older piste layout placed online by **Franck Rinaldi**.

Independent web traces support an older lineage, although some of them are forum testimony rather than archival primary sources. A 2006 discussion on Skipass refers to a **regional committee project around 2001–2002** and treats the Punta/Lattiniccia project as already established prior art. The same discussion contains a 2008 message from a student in Corte stating that a university group had been asked to prepare an impact notice/study for the Lattiniccia station project.

These traces are useful but must be weighted by source quality:

```text
Soliari dated archive
→ primary evidence for the Soliari continuation

older public forum discussions
→ corroborating evidence for pre-existing Lattiniccia activity
→ not sufficient alone to establish formal institutional history
```

A future historical pass should seek surviving documents from the Comité Corse du Ski, university work, municipal or territorial archives, and any original maps or studies.

## 3. The Soliari continuation: change the access architecture

The January 2012 Soliari note identifies its principal innovation relative to the older Lattiniccia project as a **cable-car connection between Corte and the ski area**, conceived not only as winter infrastructure but as a major panoramic attraction usable in summer.

This is important: Soliari was already a **four-season territorial-development project**, not merely a proposal to install ski lifts.

The underlying strategic hypothesis was that Corte and inland Corsica could benefit from a second tourism season, using infrastructure and accommodation that otherwise serve mainly summer activity.

The public archive also records contemporaneous attention to:

- snow reliability and seasonality;
- comparison with existing Corsican ski areas;
- winter tourism demand among Corsican residents;
- possible visitors from Sardinia and mainland Europe;
- possible attractiveness for university students;
- rebalancing tourism away from the coast and toward inland Corsica;
- reuse of tourism infrastructure across two seasons rather than one.

These historical arguments should now be re-examined rather than repeated unchanged. Climate evolution, tourism economics, mobility, environmental constraints, and technology have all changed.

## 4. Dated drone turn: 2016–2018

By 2016, Soliari was explicitly exploring drones as an alternative to conventional fixed mountain transport infrastructure.

A 9 May 2016 note, **“Des drones de skieurs”**, identifies two major blockers of the conventional design:

- the cost and environmental footprint of a cable-car connection from Corte toward the lower ski area, around 1,800 m;
- the cost and impact of conventional lifts required to continue toward Punta Latiniccia, around 2,410 m.

The post then proposes autonomous drones as skier-transport devices and already anticipates a fleet, batteries, charging infrastructure, and personnel at departure and arrival points.

A January 2018 note, **“Taxi des neiges”**, continues the same exploration and explicitly describes a drone-based connection between Corte and the foot of the slopes around 1,800 m.

These dated traces matter because they establish that the drone concept predates the current Potentics and RAIX vocabulary by many years.

## 5. Current conceptual reformulation

The project should not be reduced to:

> “Use drones instead of ski lifts.”

The more general functional problem is:

> **How can people repeatedly gain altitude on a mountain while minimizing permanent ground infrastructure, ecological disturbance, fixed capital, and the cost of dependable capacity?**

Once formulated this way, conventional cable cars, chairlifts, surface lifts, walking, autonomous traction systems, aerial systems, distributed drone arrays, and hybrid systems become alternative implementations rather than assumptions embedded in the problem statement.

## 6. Three distinct drone modes

The current exploration distinguishes at least three modes that should not be conflated.

### 6.1 Low-altitude carrying

A person may be supported by a drone while remaining very close to the ground and following the slope profile.

The important design variable is therefore not merely “flight”, but **ground clearance**.

A system operating tens of centimetres above the terrain has a radically different failure geometry from one operating at conventional aviation altitude.

This does not establish safety. It changes the problem that must be analysed.

### 6.2 Drone surface-lift / traction mode

More radically, the skier need not be lifted from the ground at all.

The drone can act as a **mobile autonomous traction source**:

```text
skier on snow
    +
flexible link
    +
autonomous drone
    →
controlled uphill traction
```

Functionally, this resembles a surface lift whose pulling capability has become mobile and individually addressable.

The key architectural property is:

> **uphill traction without continuous fixed infrastructure along the slope.**

This potentially removes or reduces pylons, continuous haul rope, sheaves, and other linear infrastructure characteristic of conventional lifts.

### 6.3 RAIX cooperative traction

A further architecture follows the **RAIX — Redundant Array of Independent X** principle developed elsewhere in the Corpus.

Instead of requiring one large drone to provide all required force, several smaller independent drones can synchronize and aggregate their individual contributions:

```text
              D1
            ↙
D2 → shared traction point → skier
            ↖
              D3
```

Conceptually:

```text
F_required
→ discover available traction units
→ assemble temporary RAIX
→ distribute load
→ synchronize
→ perform ascent
→ degrade gracefully if one unit fails
→ dissolve/reassign array after mission
```

The important property is not simply redundancy. It is **the reduction in the cost of dependable capability**, analogous to the historical economic significance of RAID in storage systems.

A useful system may therefore emerge before any single inexpensive drone can perform the whole task alone.

## 7. Granularity as a practicability variable

Soliari highlights a general Potentics variable: **how many independent units must be assembled to obtain a useful capability?**

```text
N very large
→ coordination and economic overhead may dominate

N small enough
→ aggregation becomes operationally manageable
```

The important threshold is not necessarily `N = 1`.

A capability can become practical when improvements in elementary units reduce the required array from, for example, dozens or hundreds of units to a small coordinated group.

This is directly analogous to current AI trends: increasingly capable small models may make useful cognitive RAIX configurations practical before one local model can do everything.

The relevant predictive quantities are therefore not only unit capability but also:

```text
N(C,R,t)       minimum units required for capability C at reliability R
Cost(C,R,t)    total cost of obtaining dependable capability
Coord(C,R,t)   coordination overhead
```

A Possible may cross from theoretical to deployable when these quantities pass a practical threshold.

## 8. Mental-schema case study

Soliari is useful to Potentics because reactions to the project reveal how conceptual schemas can close a possibility before engineering analysis begins.

A common implicit schema is:

> **vehicle = something the passenger is inside or on**

A skier connected by a line to an autonomous flying or traction device does not fit that familiar category. The person may instead be perceived as “cargo” or “a package being carried”.

This symbolic recategorization can produce rejection independently of technical feasibility.

The case therefore illustrates a broader principle:

> **Inherited categories may silently contain implementation assumptions, and the boundaries of those categories can then be mistaken for boundaries of Reality.**

## 9. Typical possibility closures

Soliari has historically elicited several forms of premature closure relevant to the Explorer Machine:

- **“It is impossible.”** — ontological closure without demonstrated impossibility.
- **“It is utopian.”** — feasibility closure without explicit capability analysis.
- **“It is not done.”** — conventional closure.
- **“If it were possible, somebody would already have done it.”** — historical absence treated as proof of impossibility.
- **“People cannot be transported like packages.”** — symbolic/category closure.
- **“The mountain must be earned.”** — moralization of physical effort and access.
- **“Technology is inherently anti-ecological.”** — ideological closure when it substitutes for comparative lifecycle measurement.

These objections are not to be dismissed. Each should be transformed into an investigable proposition whenever possible.

## 10. Potentics interpretation

Soliari is a useful longitudinal Potentics case because the proposition can remain relatively stable while its surrounding capability topology changes over time.

Examples of changing enabling conditions include:

- battery energy density;
- electric propulsion;
- autonomous flight control;
- localization and terrain following;
- perception systems;
- cooperative multi-drone control;
- dynamic load sharing;
- fault-tolerant distributed control;
- fleet coordination;
- low-cost computation;
- renewable electricity;
- regulatory frameworks;
- public familiarity with autonomous delivery drones.

Thus:

```text
same imagined function
+ changed surrounding capabilities
+ changed cost of dependable capability
→ changed effective possibility
```

A proposal can therefore move over time through states such as:

```text
conceivable
→ technically plausible
→ blocked by missing capability
→ newly enabled
→ integrable
→ experimentally testable
→ economically practical
→ viable or refuted
```

The absence of realization at an earlier date is not sufficient evidence of present impossibility.

## 11. No central nervous system

The RAIX variant also connects Soliari to a broader architectural intuition already present in the Corpus through ant colonies, Physarum, Fractanet, and the Learning Computer:

> **No component needs to possess the collective capability, and no central nervous system needs to contain the complete solution.**

Each unit may act from local state, local sensing, shared constraints, communication, mechanical feedback, and limited coordination rules.

The collective capability can reside in the **organization of the units and their relations**.

This matters both technically and conceptually. A centralized coordinator would recreate a single point of coordination failure. The stronger RAIX hypothesis is that sufficiently capable local units can form a temporary, fault-tolerant collective whose useful behavior emerges without a unique commanding brain.

The image is close to:

- a colony of ants accomplishing work no individual ant can perform alone;
- a swarm of butterflies collectively moving a sleeper;
- Physarum solving spatial problems without a central nervous system.

These are analogies, not proofs. Their value is to keep the design space open to architectures in which coordination and capability are properties of the network rather than a central controller.

## 12. Environmental and territorial context

The Corte mountain environment is not an empty technical substrate.

The Restonica valley has been a protected/classified landscape for decades and is managed through a long-running Grand Site approach focused on protection, visitor management, mobility, landscape quality, and sustainable local economic activity.

The municipality's Grand Site material explicitly treats traffic management, alternative mobility, protection of the site, local economic activity, and sustainable tourism as coupled problems.

This strengthens rather than settles the Soliari question. A low-infrastructure architecture is relevant precisely because conventional access and mountain infrastructure have significant physical and landscape consequences.

Any current Soliari exploration must therefore compare complete systems and include:

- permanent land take;
- structures and foundations;
- construction and maintenance access;
- noise;
- wildlife disturbance;
- battery/material lifecycle;
- energy source;
- visitor throughput;
- reversibility;
- seasonal reuse;
- emergency and rescue implications;
- landscape visibility.

## 13. Environmental hypothesis

The ecological claim must remain a hypothesis, not a slogan.

A drone or autonomous-traction system may reduce permanent mountain infrastructure, but may introduce other costs: batteries and materials, energy consumption, acoustic disturbance, maintenance, fleet replacement, potential effects on wildlife, and increased visitor throughput.

The correct comparison is therefore between **whole systems**, not between the labels “technology” and “nature”.

A Soliari design should be considered ecologically preferable only if comparative measurement supports that conclusion.

## 14. Accessibility and capability

Mountain access is also a capability question.

A system that reduces the physical effort required to gain altitude may be recreational convenience for one person and a decisive accessibility technology for another.

The proposition “the mountain must be earned” therefore contains a normative assumption about who should have access and under what bodily conditions.

Potentics should instead ask which capabilities are opened or closed for different people and at what external cost.

## 15. Why Soliari matters to the current Corpus

Soliari provides a concrete historical example of several concepts that were formalized much later:

- Rational Exploration of Possibilities;
- changing capability topology;
- temporal evolution of the Possible;
- granularity thresholds;
- cost of dependable capability;
- RAIX aggregation and graceful degradation;
- relational/emergent capability;
- premature Possibility Closure;
- mental schemas as blockers;
- Think Against Yourself;
- comparative rather than dogmatic ecological evaluation;
- Explorer Machine versus Prevention Machine;
- Reality Response through bounded experiments.

It should therefore be treated not merely as an old local ski-station proposal, but as a **longitudinal case study of a Possible whose surrounding Reality has been changing for decades**.

## 16. Historical evidence levels

### Established from dated Soliari sources

- by January 2012, Soliari explicitly presents itself as a continuation/reformulation of an older Projet Lattiniccia;
- Soliari's early differentiator was a Corte-to-mountain cable car intended for both winter and summer use;
- the project monitored snow conditions, tourism economics, and existing Corsican ski stations;
- by May 2016, drone transport was explicitly proposed as a response to the cost and environmental footprint of conventional infrastructure;
- by January 2018, the drone concept was still active and described as a Corte-to-1,800 m “snow taxi”.

### Corroborating but not yet archival-grade

- public forum traces place an organized Lattiniccia project around 2001–2002;
- a 2008 forum post from a student at Corte refers to an assigned impact-study exercise concerning the Lattiniccia station;
- older web discussions describe substantial conventional-lift layouts for the proposed station.

These claims should be upgraded only if original documents are recovered.

## 17. Next investigations

- recover and index the most relevant historical posts from the WordPress archive;
- seek original Lattiniccia documents from roughly 2001–2008;
- identify Franck Rinaldi's original piste map and preserve it if licensing/provenance allow;
- search University of Corsica archives for the 2008 impact-study work;
- reconstruct a dated timeline of technical assumptions and blockers from the pre-Soliari project through 2026;
- distinguish the “Corte-to-ski-area access” problem from the “on-slope ascent” problem;
- compare carrying, single-drone traction, RAIX traction, tethered, ground-powered, and hybrid architectures;
- perform a first-order force and energy model for a skier on representative slopes;
- model `N(C,R,t)`, total cost, reserve margin, and graceful degradation for a RAIX traction array;
- identify current regulatory categories without assuming they map cleanly onto the proposed architecture;
- define the smallest safe non-human or instrumented field experiment capable of testing traction, multi-drone load sharing, and terrain following;
- compare lifecycle and land-impact profiles against conventional lift infrastructure;
- study winter climate and snow persistence with current data rather than reusing 2012 assumptions.

## 18. Continuation

```yaml
continuation:
  project: "Soliari"
  external_archive: "https://soliari.wordpress.com/"
  status: "historical project re-entered into active rational exploration"

  established:
    - "Soliari continues an older Lattiniccia ski-station project."
    - "The Soliari public archive documents the continuation from at least January 2012."
    - "Its early differentiator was a four-season cable-car connection from Corte."
    - "Drone-based skier transport was publicly proposed by May 2016."
    - "A 2018 post continued the drone-access concept."
    - "The current exploration distinguishes carrying, ground-contact traction, and RAIX cooperative traction."
    - "The central design objective is infrastructure-light uphill mobility and dependable capability at acceptable cost, not attachment to a particular vehicle category."

  corroborating_history:
    - "Public web traces refer to an organized Lattiniccia project around 2001-2002."
    - "A 2008 public forum post refers to a University of Corsica impact-study exercise on the project."
    - "These points require archival confirmation."

  hypotheses:
    - "Autonomous mobile traction may reduce the need for continuous fixed lift infrastructure."
    - "A small RAIX of independent drones may provide a cheaper and more resilient traction capability than one large specialized drone."
    - "Mental schemas and symbolic acceptance may be important blockers independent of technical feasibility."
    - "The capability topology and cost topology surrounding the original proposal have materially improved since the 2010s."
    - "Soliari is a useful longitudinal instrument for studying when a Possible crosses practical granularity and economic thresholds."

  next:
    - "Build a pre-2001-to-2026 Soliari/Lattiniccia timeline."
    - "Recover higher-quality historical sources."
    - "Develop engineering and economic models of traction and RAIX modes."
    - "Define a bounded Reality test."
```
