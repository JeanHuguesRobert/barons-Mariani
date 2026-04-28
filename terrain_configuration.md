# Terrain Configuration Theory for Democratic AI Infrastructure

## A Possibilist Framework for Compute Governance

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A. - 1 cours Paoli, F-20250 Corte.

jhr@baronsmariani.org

Working Paper — April 2026

*This paper applies the conceptual framework developed in the companion paper
"Possibilism: Notes Toward a Research Program on Possibility Exploration"
to the specific domain of AI infrastructure governance.
The theoretical foundation is developed there; this paper develops the application.*

*Part of the MareNostrum and FractaVolta research programs.*
*github.com/JeanHuguesRobert/marenostrum*
*github.com/JeanHuguesRobert/FractaVolta — fractavolta.com*

---

## Abstract

The dominant paradigm in AI governance treats computational infrastructure as a regulatory object: something to be measured, disclosed, constrained, and controlled. This paper proposes an alternative framing drawn from Possibilism (Robert, 2026a): AI infrastructure is a *terrain* — a configuration of the possibility space of AI development — and the most consequential governance choices concern terrain configuration rather than regulatory constraint.

This reframing has practical implications. Terrain configuration theory asks not "how do we constrain what AI systems can do?" but "what infrastructure configurations keep the space of democratic governance futures open?" The answer points toward distributed, traceable, exergy-grounded compute infrastructure as the terrain condition for democratic AI governance — not because it is more efficient, but because it is more *correctable*.

We develop three applied contributions: (1) the Compute Exergy framework as a terrain-configuration metric — a measure of governance-quality-adjusted computational capacity that captures whether a given infrastructure configuration expands or forecloses democratic possibility; (2) the Stella distributed network architecture as a concrete terrain configuration instantiating the correctability thesis; and (3) the outer optimizer governance gap as a terrain-configuration failure mode invisible to standard compute governance frameworks.

**Keywords:** Terrain configuration; AI governance; Compute exergy; Democratic infrastructure; Correctability; Distributed training; Outer optimizer; Mediterranean; Possibilism.

---

## 1. From Regulatory Object to Governance Terrain

### 1.1 The Standard Frame

Current AI governance frameworks — the EU AI Act, California SB 53, the New York RAISE Act, the compute governance literature (Sastry et al., 2024; Heim et al., 2024) — share a common implicit model: AI infrastructure is a regulatory object. It exists; it has measurable properties (compute capacity, energy consumption, market concentration); governance consists of measuring those properties, setting thresholds, and requiring disclosure or restricting access above thresholds.

This model has produced genuine progress. Export controls on advanced chips, cloud-provider "know-your-customer" requirements, and training compute reporting obligations are real interventions with real effects. We do not contest their value.

We contest their sufficiency — and more specifically, their implicit assumption that the topology of the AI governance possibility space is given, and that governance consists of navigating within it.

### 1.2 The Terrain Configuration Alternative

The alternative, drawn from Possibilism (Robert, 2026a), treats AI infrastructure as a *terrain* — a configuration of the possibility space that determines which governance futures are reachable.

The terrain configuration question is not: *given this infrastructure, what regulations should apply?*

It is: *what infrastructure configuration keeps the space of democratic governance futures maximally open?*

This is a design question, not a regulatory question. It asks what to build, not what to prohibit. And it generates different answers: not "set a reporting threshold at 10²⁶ FLOP" but "build infrastructure in which democratic accountability is architecturally embedded, making unaccountable use structurally difficult rather than merely prohibited."

### 1.3 The Correctability Criterion

The terrain configuration criterion for AI infrastructure, derived from the correctability thesis in Possibilism:

> *Prefer infrastructure configurations whose failures are recoverable over configurations that are more efficient but whose failures are irreversible.*

Applied to AI governance: prefer distributed, traceable, democratically accountable compute infrastructure over concentrated, opaque infrastructure — not because it produces better AI systems faster, but because its governance failures are correctable.

A democratically governed distributed compute network that produces suboptimal AI outcomes can be corrected: the governance process observes the outcomes, updates the infrastructure configuration, and redirects. A concentrated, opaque compute infrastructure that locks into a pathological attractor cannot be corrected from within: the actor controlling concentration determines both the direction of development and the evaluation of outcomes.

This is the structural argument for democratic AI infrastructure. It does not require the claim that democratic governance always produces better outcomes. It requires only the claim that recoverable failures are preferable to irrecoverable ones under radical uncertainty.

---

## 2. Compute Exergy as a Terrain-Configuration Metric

### 2.1 The Measurement Problem

Terrain configuration theory requires a metric that captures whether a given infrastructure configuration expands or forecloses democratic possibility. Raw compute metrics (FLOP counts, GPU-hours) fail this requirement: they measure quantity without capturing governance quality. Financial metrics fail similarly.

The companion paper DHITL (Robert, 2026b) proposes **Compute Exergy (Xc)** as such a metric:

$$X_c = E \times \eta_{hw} \times \eta_{sys} \times \eta_{sla} \times \eta_{gov}$$

where $\eta_{gov} \in [0,1]$ is a governance quality factor capturing traceability and democratic accountability, with the nullity condition $X_c = 0$ if $\eta_{gov} = 0$.

From a terrain configuration perspective, Xc is not merely an accounting unit. It is a *topological measure*: it quantifies the degree to which a given unit of compute contributes to an infrastructure configuration in which democratic governance futures remain reachable.

The nullity condition is the formal expression of the terrain configuration criterion: compute without democratic accountability contributes nothing to the reachable space of democratic governance futures, regardless of its raw quantity.

### 2.2 The Value Multiplier as Terrain Signal

The Constellia architecture (Robert & Valdes, 2026) documents a market-observed value multiplier: identical solar energy, converted to compute at different governance certification levels, commands prices of €90/MWh (raw electricity), €350/MWh (uncertified batch compute), €1,100/MWh (certified premium compute), or €2,800/MWh (sovereign-critical certified compute).

From a terrain configuration perspective, this ×31 spread is not merely a price premium. It is a *market signal about terrain topology*: the market prices the difference between infrastructure configurations that expand democratic possibility (high $\eta_{gov}$) and those that do not. The premium is the revealed preference of actors who need their compute to remain governable, auditable, and democratically accountable.

This is the terrain configuration reading of what the DHITL paper treats as an economic finding: governance quality is a productive input, not merely a constraint, because it determines which terrain — which configuration of possibility — the infrastructure instantiates.

### 2.3 Concentration as Terrain Foreclosure

The **Compute Exergy Concentration Index (CECI)** measures the HHI of Xc distribution across actors in a jurisdiction:

$$\text{CECI} = \sum_i (X_{c,i} / X_{c,\text{total}})^2$$

From a terrain configuration perspective, high CECI is not merely a market concentration indicator. It is a *terrain foreclosure signal*: as compute concentration increases, the space of reachable democratic governance futures contracts. Above the structural instability threshold (CECI > 0.40), the concentrated actor may begin to determine the terms of its own governance — closing the feedback loop that democratic correction requires.

In current global conditions — five actors controlling approximately 85% of frontier AI compute — we are operating in or near this terrain foreclosure zone. The governance challenge is not primarily to regulate what these actors do. It is to reconfigure the terrain so that democratic governance futures remain reachable.

---

## 3. Distributed Architecture as Terrain Configuration

### 3.1 The Stella Network

The Constellia architecture (Robert & Valdes, 2026) proposes the **Stella network**: a distributed energy-compute infrastructure of 60 autonomous nodes across the Mediterranean quadrilateral (Corsica, Sardinia, Sicily, Tunisia), each comprising sovereign solar generation, multi-layer storage, and compute capacity.

From a terrain configuration perspective, Stella is not primarily an energy or compute infrastructure. It is a *terrain configuration*: an instantiation of distributed, traceable, democratically governed compute that keeps the space of democratic AI governance futures open by making concentration structurally difficult.

The ARPANET design principle (Baran, 1964) that underlies Stella — distribution such that destruction of any 30% of nodes reduces capacity by 30%, without cascade failure — is a terrain configuration principle, not an engineering optimization. It does not produce the most efficient network. It produces the most correctable one: a network whose failures are proportional, visible, and recoverable.

The Mediterranean physical substrate — high solar irradiance (1,700–1,850 kWh/m²/year in Corsica), multi-jurisdictional governance topology, existing submarine fiber infrastructure — provides the terrain conditions for Stella: a distributed physical substrate that resists monopolization because its energy source (solar irradiation) is physically distributed and cannot be captured by any single actor.

### 3.2 Value-Shaped Generation as Temporal Terrain Configuration

The FractaVolta companion paper (Robert, 2026c) introduces *temporal agrivoltaics*: the co-optimization of photovoltaic production timing with electricity market value, using vertical east-west bifacial panels that produce morning and evening peaks aligned with high-value electricity hours.

From a terrain configuration perspective, value-shaped generation is a *temporal terrain configuration*: it reconfigures the possibility space of renewable energy economics by making the temporal structure of generation a design variable rather than a physical given.

The conjunction of value-shaped generation with flexible compute dispatch (*compute as virtual storage*) is a double terrain configuration: it reconfigures both the energy landscape (production at high-value hours) and the compute landscape (absorption of surplus generation by deferrable workloads). The result is an infrastructure in which AI compute is physically, temporally, and institutionally grounded in democratic energy governance.

### 3.3 Decoupled DiLoCo as Terrain Expansion

Decoupled DiLoCo (Douillard et al., 2026) demonstrated that frontier-scale model training across geographically separated islands at internet-scale bandwidth is achievable — with 88% goodput under high-failure conditions and near-parity ML performance.

From a terrain configuration perspective, this is a *terrain expansion event*: a previously unavailable configuration (distributed frontier training without co-located hardware) has become reachable. The space of democratic AI governance futures has expanded, because it is now technically feasible to train frontier models on democratically distributed infrastructure.

However, DiLoCo simultaneously introduces a *terrain foreclosure risk*: the outer optimizer governance gap. In the DiLoCo architecture, an outer optimizer aggregates gradient updates from distributed islands and applies global parameter updates. Whoever controls the outer optimizer controls what the model learns — regardless of where the compute hardware sits. Distributed hardware with concentrated outer optimizer authority is not democratic infrastructure; it is the appearance of democratic infrastructure.

The **Algorithmic Control Concentration Index (ACCI)**, introduced in the DHITL companion paper (Robert, 2026b), measures this dimension of terrain foreclosure:

$$\text{ACCI} = \sum_\phi [X_c(\phi) \times \sum_i W(\phi,i)^2] / \sum_\phi X_c(\phi)$$

where $W(\phi,i)$ is the fraction of gradient aggregation authority held by actor $i$ over training run $\phi$.

The ACCI threshold (0.15 warning, 0.25 instability) is set lower than the CECI threshold (0.25/0.40) because outer optimizer concentration is faster, less visible, and less reversible than hardware concentration. Distributed hardware with concentrated outer optimizer is the terrain configuration failure mode most likely to emerge from the Decoupled DiLoCo paradigm — and least visible to existing governance frameworks.

---

## 4. The Mediterranean as Terrain Configuration Testbed

### 4.1 Why the Mediterranean

The Mediterranean quadrilateral — Corsica, Sardinia, Sicily, Tunisia — is proposed not as a demonstration of Terrain Configuration Theory but as a *testbed*: a site where the theory's predictions can be tested against empirical outcomes.

The enabling conditions:

- **Solar exergy endowment:** 1,700–2,100 kWh/kWp/year across the quadrilateral, physically distributed and unmonopolizable.
- **Multi-jurisdictional topology:** four governance frameworks (France, Italy, Italy/island, Tunisia) providing natural variation in governance variables at equivalent physical endowments.
- **Fiber infrastructure:** existing and planned submarine cables providing the bandwidth required for Decoupled DiLoCo-style distributed training (2–5 Gbps between nodes).
- **Historical institutional precedent:** the CECA (1951) demonstrates that pooling strategic substrates (then coal and steel; now solar exergy and compute) under shared democratic governance can make monopolization structurally impossible.

### 4.2 The Testable Prediction

Terrain Configuration Theory makes a specific prediction for the Mediterranean testbed:

> *A distributed energy-compute infrastructure (Stella network) instantiating low CECI, low ACCI, and high $\eta_{gov}$ will exhibit higher governance resilience under stress — measured as the capacity for democratic correction of AI governance failures — than an equivalent infrastructure with high CECI or ACCI.*

This is Proposition P3 from the DHITL framework, restated in terrain configuration terms. It is testable across the ~40–60 island states and autonomous regions that meet the Constellia generalization conditions (solar ≥ 1,400 kWh/kWp/year; agrivoltaic land ≥ 5,000 ha; governance stability for 20-year contracts).

### 4.3 The CECA Analogy as Terrain Configuration History

The European Coal and Steel Community (1951) is the canonical historical instantiation of terrain configuration thinking, even if it was not described in those terms.

The CECA did not solve the problem of Franco-German military competition by finding an optimal solution. It reconfigured the terrain: by pooling the strategic industrial substrate (coal and steel) under shared democratic governance, it made the weaponization of that substrate by any single member structurally difficult — not prohibited, but structurally foreclosed.

The Charte du Soleil Méditerranéen (Robert, 2026a) proposes the same terrain reconfiguration for solar exergy and compute: a pooling arrangement that makes monopolization structurally impossible by making the substrate collectively governed. The analogy is not rhetorical. It is structural: the mechanism is the same — substrate pooling under democratic governance forecloses pathological attractors.

---

## 5. Failure Modes of the Terrain Configuration Framework

### 5.1 Application-Level Failure Modes

**FM-T1: Terrain configuration without governance.** A distributed infrastructure can be built without democratic governance — 60 nodes owned by 60 different private actors, with no accountability mechanism. This instantiates low CECI (hardware distribution) without the governance properties that make low CECI meaningful. Distributed ownership is not the same as democratic governance. The Stella network requires both.

**FM-T2: Governance theater.** Democratic governance mechanisms can be formally present without being substantively operative — advisory boards without authority, transparency requirements without enforcement, participation processes without genuine agenda-setting power. Formal democracy with operational oligarchy (FM-2 in DHITL) is a terrain configuration failure: the terrain appears open while being effectively foreclosed.

**FM-T3: Terrain rigidity.** A terrain configuration optimized for current conditions may become a constraint under changed conditions. The Mediterranean solar infrastructure optimized for 2026 AI workloads may not be the right configuration for 2036 AI workloads. Terrain configurations must include mechanisms for their own revision — a meta-terrain property that is easy to neglect in the design of specific configurations.

**FM-T4: Outer optimizer migration.** As the Decoupled DiLoCo paradigm diffuses, actors who currently control centralized training infrastructure may migrate to controlling outer optimizer functions in nominally distributed systems. The terrain expansion (distributed hardware) may be accompanied by terrain foreclosure (concentrated algorithmic control) if governance frameworks do not extend to the outer optimizer layer. ACCI monitoring is the detection mechanism; democratic outer optimizer governance is the prevention.

---

## 6. Conclusion: Two Questions

Standard AI governance asks: *given this AI infrastructure, what constraints should apply?*

Terrain Configuration Theory asks: *what infrastructure configuration keeps the space of democratic governance futures maximally open?*

Both questions are necessary. Neither is sufficient alone. But the second question is causally prior — the answer to the first depends on the answer to the second — and it is systematically underasked in current governance discourse.

The Mediterranean testbed offers a candidate answer to the second question at meso-scale: a distributed, solar-grounded, democratically governed energy-compute infrastructure, instantiated through the Stella network, governed by the Galassia sovereign fund, and certified through the Compute Exergy framework. Whether this answer generalizes beyond the Mediterranean — whether it constitutes a terrain configuration that keeps democratic AI governance futures open at civilizational scale — is the empirical question the research program proposes to investigate.

The question is not whether exploration occurs.

The question is who configures the terrain.

And the answer, for this research program, begins with the sun.

---

## References

Baran, P. (1964). On distributed communications networks. RAND Corporation Memorandum RM-3420-PR.

Douillard, A., Rush, K., Donchev, Y., et al. (2026). Decoupled DiLoCo. Google DeepMind, arXiv:2604.21428.

Heim, L., et al. (2024). Training compute thresholds. arXiv:2405.10799.

Robert, J.-H. N. (2026a). Possibilism: Notes toward a research program on possibility exploration. Institut Mariani Working Paper.

Robert, J.-H. N. (2026b). Democratic Humans in the Loop (DHITL). MareNostrum Working Paper. `github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md`

Robert, J.-H. N. (2026c). Value-shaped solar and containerized compute. FractaVolta Working Paper. `github.com/JeanHuguesRobert/FractaVolta`

Robert, J.-H. N. (2026d). Electricity in containers. FractaVolta Working Paper. `github.com/JeanHuguesRobert/FractaVolta`

Robert, J.-H. N., & Valdes, G. (2026). Constellia. ICOME'26 (submitted). `github.com/JeanHuguesRobert/marenostrum/blob/main/constellia.md`

Sastry, G., et al. (2024). Computing power and the governance of AI. arXiv:2402.08797.

Simon, H. A. (1969). *The Sciences of the Artificial*. MIT Press.

*(Full bibliography to be completed before release.)*

---

*© 2026 Jean Hugues Noël Robert, baron Mariani — Institut Mariani / C.O.R.S.I.C.A.*
*Working paper. Not for citation without permission.*
*Website: fractavolta.com · github.com/JeanHuguesRobert/marenostrum*
*Contact: jhr@baronsmariani.org*
