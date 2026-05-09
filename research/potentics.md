# What is Potentics?

## Toward a Science of Organized Potentials

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani / C.O.R.S.I.C.A.
1 cours Paoli, F-20250, Corte, Corsica, France

jhr@baronsmariani.org

*Preprint — May 2026*

---

## Abstract

Modern civilization increasingly depends on the interaction between energy systems, information systems, computation, and collective intelligence. Yet these domains are still largely studied separately. Energy is treated as a problem of production and storage. Computation is treated as an abstract informational process. Geography is often reduced to logistics. Intelligence is discussed independently from the physical infrastructures sustaining it.

This paper proposes *Potentics* as a tentative transdisciplinary research program studying how distributed potentials — energetic, gravitational, informational, computational, social, and territorial — may be transformed into organized and resilient intelligence under physical constraints.

Potentics does not claim that all systems obey identical laws, nor that metaphor alone is sufficient to establish scientific validity. Rather, it explores whether recurring structural patterns emerge across scales whenever gradients, storage, networks, and coordination interact. The central hypothesis is that civilization itself may be understood as a process that tends to optimize the transformation of available exergy into persistent cognitive and organizational capacity — a claim that remains to be formalized and empirically tested.

This perspective is grounded in thermodynamic principles — particularly the Landauer bound, Prigogine's dissipative structures, and the concept of exergy — and extends them toward a joint treatment of geography, computation, and collective intelligence. A formalization of Cognitive Exergy Density (κ) is proposed as a candidate metric, alongside the Compute eXergy Unit (CXU) as its computational instantiation. Both metrics are first approximations requiring empirical validation.

The framework is illustrated by a reference scenario for Corsica and the MareNostrum architecture, where solar intermittency, gravitational storage potential, territorial constraints, and AI inference capacity interact in ways that existing energy or computation frameworks cannot jointly model.

---

## 1. Introduction

The industrial age was fundamentally shaped by concentrated energy. Coal, oil, and centralized electrical grids enabled unprecedented levels of production, mobility, communication, and computation. The digital age then progressively abstracted information from its physical substrate, creating the widespread impression that computation exists independently from geography, infrastructure, or energetic constraints.

This separation is becoming increasingly difficult to sustain.

Training a large language model consumes on the order of 10³–10⁴ MWh of electrical energy (Patterson et al., 2021). Global data center electricity consumption reached approximately 200–250 TWh in 2022 and is projected to double or triple by 2030 (IEA, 2024). The physical footprint of intelligence is no longer negligible — it is geopolitical.

Simultaneously, the renewable transition introduces a structural discontinuity: unlike fossil fuels, which can be stored and dispatched on demand, solar and wind generation is inherently intermittent and geographically distributed. The question of where and when energy exists is no longer separable from the question of where and when computation occurs.

Artificial intelligence, large-scale computation, renewable intermittency, storage systems, distributed networks, and geopolitical fragmentation are together forcing civilization to confront the physical foundations of cognition:

- Computation consumes energy.
- Networks occupy territory.
- Intelligence requires infrastructure.
- Infrastructure depends on gradients.

Yet no unified framework currently attempts to study these relationships as manifestations of a common organizational phenomenon.

*Potentics* is proposed as a tentative name for such an inquiry. The etymology is deliberate: *potens* (Latin: having power, capable) combined with the suffix *-ics* (denoting a field of study). Potentics studies how distributed potentials — physical, informational, social, territorial — are organized into persistent capability.

---

> **Core Contribution**
>
> This paper proposes Potentics as a tentative transdisciplinary framework with:
> - **Four working hypotheses** (P1–P4) connecting thermodynamics, geography, and collective intelligence;
> - **Two candidate metrics**: the Compute eXergy Unit (CXU) and Cognitive Exergy Density (κ);
> - **A reference scenario** for Corsica illustrating how solar exergy might be transformed into sovereign cognitive infrastructure;
> - **A research agenda** identifying open questions and testable predictions.
>
> All claims are preliminary. Potentics is proposed as an open research program, not a completed theory.

---

> **Working Hypotheses (overview — developed in Section 3)**
>
> | Hypothesis | Informal statement | Status |
> |-----------|-------------------|--------|
> | P1 | Civilizational intelligence is a dissipative structure maintained by exergy flux | Theoretical, plausible |
> | P2 | A minimum cognitive exergy density exists below which complex adaptation fails | Speculative, testable |
> | P3 | Civilizational resilience is partially measurable as cognitive exergetic efficiency | Speculative, operationalizable |
> | P4 | Optimal cognitive infrastructure exhibits scale-free topology with algebraic connectivity proportional to criticality | Theoretical, to be tested |

---

This paper is organized as follows. Section 2 establishes formal definitions. Section 3 develops the thermodynamic and information-theoretic foundations, together with the four working hypotheses. Sections 4 and 5 extend the framework from physical potentials to intelligence and geography. Section 6 presents the Corsica reference scenario as a concrete illustration. Section 7 examines fractal organization across scales. Section 8 proposes a candidate measurement framework. Section 9 outlines the Potentics research program. Section 10 concludes.

---

> **What Potentics is NOT**
>
> - Not a claim that all complex systems obey identical laws.
> - Not an assertion that geography determines civilizational outcomes.
> - Not a projection or financial forecast for any specific territory.
> - Not a completed scientific theory — it is a research direction.
> - Not a replacement for thermodynamics, network science, or information theory; it is a proposed unification of insights from these fields.

---

## 2. Formal Definitions

We begin by establishing working definitions for the core concepts of Potentics. These definitions are intended to be precise enough to generate testable predictions, while remaining open to revision as the framework develops.

### 2.1 Potential

**Definition 1 (Potential).** A *potential* Φ is a scalar field defined over a configuration space S such that a displacement ds along any path in S produces a free energy differential dF = −∇Φ · ds. Potentials are sources of gradients and therefore of directed transformation.

This definition encompasses electrical potential (voltage), gravitational potential (Φ_g = gh), chemical potential (μ_i = ∂G/∂n_i at constant T, P), thermal potential (temperature T as the driver of heat flow), and — more tentatively — informational potential, interpreted as Shannon entropy H = −Σ p_i log p_i measuring the capacity for uncertainty reduction.

### 2.2 Gradient

**Definition 2 (Gradient).** A *gradient* G(Φ) = ∇Φ is the spatial or state-space derivative of a potential. It is the operational quantity driving flows, transformations, and work extraction.

No gradient implies no available work. The basic claim of Potentics is that civilization is the organized exploitation of gradients.

### 2.3 Exergy

**Definition 3 (Exergy).** The *exergy* Ξ of a system is the maximum useful work extractable as it reversibly reaches thermodynamic equilibrium with its environment at reference state (T₀, P₀):

> Ξ = (U − U₀) + P₀(V − V₀) − T₀(S − S₀)

Unlike energy, exergy is destroyed — not conserved — by irreversibilities. It is therefore the appropriate measure of useful potential: it answers "how much work can this system still do?"

### 2.4 Cognitive Exergy

**Definition 4 (Cognitive Exergy).** *Cognitive exergy* Ξ_cog is the component of exergy consumed in processes that generate, store, or transmit structured information, adaptive models, or decision capacity.

This connects to Landauer's (1961) result that the erasure of one bit of information dissipates a minimum of:

> E_L = k_B T ln 2 ≈ 2.85 × 10⁻²¹ J at 300 K

Real systems operate far above this bound — current CMOS dissipates approximately 10⁷ × E_L per logical operation. The gap between the Landauer floor and current engineering practice represents the irreversibility margin of contemporary cognitive infrastructure, and a potential domain for efficiency improvement.

### 2.5 Compute eXergy Unit (CXU)

**Definition 5 (CXU).** The *Compute eXergy Unit* is a composite metric for the exergy-efficiency of computational work:

> CXU = E × η_hw × η_sys × η_sla

where:
- E is total electrical energy consumed (J or kWh)
- η_hw ∈ [0,1] is hardware efficiency (PUE⁻¹ × compute utilization)
- η_sys ∈ [0,1] is system-level efficiency (algorithmic efficiency, model sparsity)
- η_sla ∈ [0,1] is service-level availability (uptime weighted by demand alignment)

CXU operationalizes cognitive exergy at the data center scale. All three efficiency parameters require empirical determination for any specific deployment; the values used in Section 6 are working assumptions, not validated measurements.

### 2.6 Cognitive Exergy Density (κ)

**Definition 6 (κ).** The *Cognitive Exergy Density* of a territory A over a time window τ is:

> κ(A, τ) = CXU(A, τ) / (area(A) × τ)     [W·m⁻²]

This measures the spatial intensity of organized cognitive work per unit territory — analogous to power density in energy geography, but specifically tracking the cognitive component. κ is proposed as a candidate metric for comparing territorial configurations, not as a measure of cognitive quality or societal value.

---

## 3. Thermodynamic and Information-Theoretic Foundations

Having established definitions, we now present the theoretical foundations from which the four working hypotheses are derived. These hypotheses are explicitly labeled as tentative: they are intended to generate testable predictions, not to assert established facts.

### 3.1 Dissipative Structures and Organized Complexity

The second law requires that entropy dS ≥ 0 in isolated systems. Yet organized structures — from crystals to cells to cities — exhibit local reductions in entropy. The resolution: such structures are open systems that maintain internal order by exporting entropy to their environment.

Prigogine and Stengers (1984) formalized this through dissipative structures: systems far from equilibrium can spontaneously develop and maintain organized states, provided they are driven by a continuous flux of exergy through them. For a system with internal entropy production σ_i ≥ 0:

> dS/dt = σ_i + dS_e/dt

Organization requires dS/dt < 0, which necessitates dS_e/dt < −σ_i.

> **Tentative Hypothesis P1 (to be tested):** *Civilizational intelligence is best understood as a dissipative structure maintained by a sustained flux of exergy — primarily solar at geological scales — through geographic and institutional substrates. Disruption of this flux, if sustained, produces organizational collapse.*
>
> *Testability:* Historical analysis of civilizational collapse episodes correlated with documented exergy supply disruptions (Tainter, 1988); comparative exergy accounting across contemporary states.

### 3.2 The Landauer Bound and Physical Computation

Shannon's (1948) theory of communication established that information H = −Σ p_i log₂ p_i measures uncertainty reduction precisely. Landauer (1961) and Bennett (1973) grounded this in thermodynamics: information is not merely mathematical — its acquisition, storage, and erasure have irreducible physical costs.

Any physical intelligence requires a minimum exergy flux proportional to its information processing rate:

> Ξ_min ≥ k_B T ln 2 × I_rate

where I_rate is the rate of irreversible logical operations per second. This bound is far below current engineering practice but establishes a theoretical floor.

> **Tentative Hypothesis P2 (to be tested):** *There exists, for any given temperature and organizational scale, a minimum cognitive exergy density κ_min below which complex adaptive behavior cannot be sustained. Systems operating below κ_min degrade toward lower-complexity equilibria.*
>
> *Testability:* Empirical determination of κ across functioning and collapsing complex systems; theoretical derivation from Landauer bound and organizational complexity estimates.

### 3.3 Adaptive Systems and Free Energy Minimization

Friston's free energy principle (2010) proposes that adaptive biological systems minimize variational free energy F:

> F = E_q[log q(z) − log p(x, z)]

where q(z) is the system's internal model and p(x, z) is the generative model of the environment. Minimizing F is equivalent to improving model accuracy while limiting model complexity — a form of bounded rationality with thermodynamic grounding.

This framework may extend, with appropriate caution, beyond neuroscience: any system that maintains an internal model of its environment can tentatively be understood as minimizing surprise per unit of exergy consumed.

> **Tentative Hypothesis P3 (to be tested):** *Civilizational resilience can be partially measured by the ratio of adaptive model quality to exergy consumed in maintaining it — a quantity we term cognitive exergetic efficiency (η_cog = I_useful / Ξ_consumed). Higher η_cog implies greater resilience per physical cost.*
>
> *Testability:* Comparative institutional analysis; AI system benchmarking relative to compute consumed; historical case studies.

> **Tentative Hypothesis P4 (to be tested):** *Optimal cognitive infrastructure networks exhibit scale-free degree distributions (for resilience to random failures), moderate local clustering (for redundancy), and algebraic connectivity λ₂ proportional to the criticality of their supported functions.*
>
> *Testability:* Network analysis of existing infrastructure topologies (Internet, electrical grids, AI inference networks); stress-testing under simulated failure modes.

---

Having established the thermodynamic and information-theoretic foundations, we now examine how these principles manifest at the scale of physical potentials and their hierarchical coupling.

---

## 4. Potentials, Gradients, and the Hierarchy of Organization

A potential is fundamentally a difference capable of producing transformation. Civilization emerges from the capture, storage, transformation, and coordination of such differences.

### 4.1 The Hierarchy of Potentials

Different potential types operate at characteristic scales and speeds, and critically, they couple: higher-order potentials depend structurally on lower-order ones.

| Potential Type | Timescale | Spatial Scale | Transformation Product |
|---------------|-----------|---------------|----------------------|
| Gravitational | Geological | Continental | Hydraulic exergy |
| Solar thermal | Daily–seasonal | Regional | Thermal / electrical exergy |
| Chemical (fossil) | Decadal | Global markets | Industrial exergy |
| Electrical | Milliseconds | Grid | Mechanical / computational work |
| Informational | Microseconds | Network | Decision, coordination |
| Social / institutional | Decades | Political territory | Governance, norms |

Social institutions presuppose informational infrastructure, which presupposes electrical infrastructure, which presupposes primary energy. Disruption at any lower level propagates upward.

### 4.2 Gradient Coupling and Value Multiplication

A central observation, preliminary and based on current market data, is that the value generated by a gradient can be multiplied when coupled to a higher-order transformation rather than dissipated at its natural level.

Consider solar exergy on a typical Mediterranean island (order-of-magnitude estimates only; see Section 6 for full assumptions):

| Transformation Path | Approx. value per MWh solar | Multiplier | Basis |
|--------------------|----------------------------|------------|-------|
| Wholesale electricity export | ~50 € | 1× | EU spot market, 2024 |
| Hydrogen production | ~80–150 € | 1.6–3× | Current electrolyzer economics |
| Standard GPU cloud compute | ~200–400 € | 4–8× | Current hyperscaler pricing |
| AI inference (specialized) | ~250–1,000 € | 5–20× | Current LLM API pricing, declining rapidly |

*These multipliers are illustrative and should be treated as order-of-magnitude estimates only, not as revenue projections. They are derived from current market prices, which are declining rapidly — particularly for AI inference. Infrastructure, operational, and capital costs are excluded from this table, and would substantially reduce net value. The structural argument (higher-order transformations tend to command higher value) is more robust than any specific price estimate.*

The apparent value gradient from electricity to inference reflects the thermodynamic hierarchy: higher-order transformations require more organized infrastructure, which commands a premium — for now. This premium may compress as AI inference commoditizes. This is not a financial projection and does not account for capital costs.

### 4.3 Potentials, Constraints, and Organizational Possibility

Potentics does not claim that higher-value transformations are always optimal or achievable. Each step up the hierarchy requires additional infrastructure, institutional capacity, and governance — all of which consume resources and introduce failure modes. The hypothesis is simply that the hierarchy exists and that the possibility space of a territory is shaped by which potentials are accessible to it.

---

## 5. From Energy to Intelligence

### 5.1 The Incompleteness of Current Metrics

Modern societies typically optimize energy systems according to production, efficiency, cost, or carbon emissions. These metrics are essential but incomplete.

A civilization may consume large quantities of energy while producing little resilient intelligence. Conversely, relatively constrained systems may generate extraordinary adaptive capacity through organization, coordination, and knowledge preservation.

This suggests that energy quantity alone is not the primary variable. Exergy quality — the capacity to perform directed work — is more relevant. But exergy, too, is insufficient when the question is the cognitive output of a system.

### 5.2 Cognitive Exergetic Efficiency

We define the cognitive exergetic efficiency η_cog of a system as:

> η_cog = I_useful / Ξ_consumed

where I_useful is the structured information produced (maintained complexity, or task-specific performance), and Ξ_consumed is total exergy consumed. How I_useful should be measured remains an open problem — this is a conceptual proposal, not an operational formula.

Contemporary AI systems illustrate both the challenge and the opportunity: inference queries consuming 10⁻³ kWh may produce responses of significant informational value, but model training consumed 10⁶× more exergy for a proportionally smaller marginal gain in capability. Improving η_cog is a research priority.

### 5.3 The Emergy Tradition

Odum (1988) proposed *transformity* as a measure of the solar energy required, directly and indirectly, to produce one unit of a resource. High-transformity resources (information, organization) embody large prior energy flows. The *emergy* tradition provides a useful precedent for Potentics: it grounds value hierarchies in thermodynamic work. Potentics extends this intuition to explicitly include AI infrastructure as a thermodynamically grounded process, subject to the same accounting discipline.

---

## 6. Reference Scenario: Corsica and the MareNostrum Architecture

*This section presents a reference scenario to illustrate the order of magnitude of Cognitive Exergy Density achievable under favorable conditions. It is not a prediction, a project proposal, or a financial analysis. All parameter values are working assumptions.*

### 6.1 Context

The MareNostrum architecture is a proposed framework for transforming Mediterranean solar abundance into distributed sovereign AI compute infrastructure, grounded in the Potentics framework. Corsica (8,680 km², population ~340,000) is used as the primary reference territory.

**Corsica's potential portfolio (physical basis):**

| Potential Type | Quantity | Notes |
|---------------|----------|-------|
| Annual solar irradiance | ~14.7 TWh/yr (potential) | 8,680 km² × 1,700 kWh/m² (DNI) |
| Agrivoltaic potential | ~10.8 GWp | 30,000 ha abandoned vineyards × 360 Wp/m² |
| Net electricity (agrivoltaic) | ~16 TWh/yr | Bifacial E-W panels, estimated 25% losses |
| STEP storage potential | ~2–5 GWh | Based on existing hydraulic infrastructure |
| Current AI compute capacity | ~0 GW | No sovereign AI infrastructure present |
| Peak export capacity | 600 MW | SARCO interconnection to mainland France |

### 6.2 The Value Multiplication Argument

Under the current configuration, surplus solar energy would be exported via SARCO at wholesale electricity prices. The MareNostrum hypothesis is that converting this exergy into sovereign AI compute tokens would yield significantly higher social and economic value — based on the coupling hierarchy described in Section 4.2.

*Caveat: The value estimates in Section 4.2 reflect current market conditions. AI inference prices have been declining rapidly. The structural argument (higher-order transformations command higher value) is more robust than any specific price estimate.*

### 6.3 The SARCO Bottleneck as Structural Incentive

A counterintuitive feature: the limited capacity of the SARCO interconnection (600 MW peak, frequently constrained) functions as a structural incentive for local exergy transformation. A territory fully connected to a continental grid faces competitive pressure to export commodity electricity. An island constrained by interconnection capacity has a natural incentive to transform energy locally into higher-value forms.

This is an instance of a broader principle: infrastructural constraints shape organizational possibilities. The SARCO limit is not merely a problem to be solved by a larger cable — it is a structural feature that may incentivize the development of sovereign cognitive infrastructure.

### 6.4 Reference Computation of κ

> **Key Assumptions for κ Calculation**
>
> | Parameter | Value | Justification / Status |
> |-----------|-------|------------------------|
> | Installed agrivoltaic capacity | 3 GWp (first phase) | Assumed, not committed |
> | Effective continuous compute load | 500 MW | Assumed after storage smoothing |
> | Territory | 8,680 km² | Corsica total area |
> | η_hw (hardware efficiency) | 0.70 | Typical modern data center PUE ~1.3–1.4 |
> | η_sys (system efficiency) | 0.60 | Estimated for mixed workloads |
> | η_sla (service availability) | 0.85 | Assumed with storage backup |
> | All efficiency values | Working assumptions | Require empirical validation |

Under these assumptions:

> CXU = 500 × 10⁶ W × 0.70 × 0.60 × 0.85 ≈ 179 MW_effective

> κ = 179 × 10⁶ W / (8.68 × 10⁷ m²) ≈ **2.06 W·m⁻²**

For reference: incident solar power averages ~200 W·m⁻² in Corsica. A κ of ~2 W·m⁻² would represent approximately 1% of incident solar power converted to organized compute. This is the combined result of solar panel efficiency (~20%), land coverage (~15% of territory), power conversion and storage losses, and the three efficiency parameters above. The overall solar-to-compute conversion efficiency of ~1% is ambitious — it sits at the high end of efficiencies observed in productive natural ecosystems (C3 photosynthesis: ~0.5–2%) — and assumes all favorable conditions are simultaneously achieved. *Meaningful benchmarks require data from existing compute-dense territories, which we have not yet compiled. This scenario is intended to illustrate the upper bound of what the Potentics framework suggests is physically plausible under favorable conditions, not what is likely or planned.*

### 6.5 Governance Implications (Exploratory — see Appendix A)

The MareNostrum scenario generates institutional questions that exceed the scope of this paper. Three exploratory directions are noted: cooperative exergy accounting across Mediterranean territories (a possible analog to the 1951 CECA for energy commons); municipal participation structures enabling local revenue from compute infrastructure; and the AI compute token as a potential unit of account for regional sovereignty agreements.

These are questions generated by the Potentics framework, not policy proposals. They are developed separately in Appendix A for readers interested in the institutional dimension; they are not necessary to evaluate the scientific content of Sections 2–8.

---

Having grounded the framework in a concrete scenario, we now return to the more general question of organizational structure across scales.

---

## 7. Fractal Organization Across Scales

### 7.1 Recursive Structures in Complex Systems

Many organized systems exhibit recurring multi-scale patterns: local storage supporting larger networks; distributed redundancy increasing resilience; hierarchical coordination emerging from decentralized interactions; packetized circulation of matter, energy, or information.

These patterns appear in biological systems (vascular trees, neural networks), ecological systems (river basins), infrastructure systems (electrical grids, the Internet), and political systems (federations). Potentics does not claim these systems are identical. It asks whether similar organizational constraints repeatedly emerge whenever distributed potentials must be stabilized and coordinated under physical limits.

### 7.2 Network Science Formalization

Let G = (V, E) be a network where V is the set of nodes (storage or computation units) and E the set of edges (transmission links). Relevant structural metrics include:

- **Degree distribution** P(k): scale-free networks (P(k) ~ k^{−γ}) are robust to random failures but vulnerable to targeted attack.
- **Clustering coefficient** C_i: measures local interconnection density, correlating with resilience to targeted removal.
- **Betweenness centrality** g(v): identifies bottleneck nodes whose removal most severely disrupts network flows.
- **Algebraic connectivity** λ₂(L): the second smallest eigenvalue of the graph Laplacian. λ₂ = 0 implies disconnection; higher values imply greater network robustness.

These metrics, well-established in network science, provide an existing mathematical toolkit that Potentics can adopt without modification.

### 7.3 The Packetization Principle

A convergence is observable across organized systems: they tend to transmit resources in discrete packets rather than continuous flows. Electrical grids use AC cycles; the Internet uses IP packets; capital markets use discrete transactions; neural systems use action potentials; AI inference systems use tokens.

This packetization may reflect a deep organizational principle: discrete units allow error correction, prioritization, routing, and flow control that continuous flows cannot support. Potentics tentatively conjectures that the tokenization of AI inference and the proposed tokenization of compute-backed energy units are instances of this general pattern — but this conjecture is speculative and is noted as such.

---

## 8. A Candidate Measurement Framework

### 8.1 The Problem of Measuring Civilizational Intelligence

Current aggregate measures are inadequate for Potentics purposes:

| Existing metric | Limitation for Potentics |
|-----------------|--------------------------|
| GDP | Measures economic throughput, not knowledge quality or organizational resilience |
| HDI | Captures wellbeing proxies, not adaptive capacity |
| Patent counts | Measures documented novelty, not implemented intelligence |
| Network connectivity | Measures infrastructure reach, not cognitive output |

Potentics requires metrics that bridge physical infrastructure and cognitive output. The following are candidate metrics — first approximations requiring empirical development.

### 8.2 Candidate Metrics

**Cognitive Exergy Density (κ)** — defined in Section 2.6 [W·m⁻²]:

> κ(A, τ) = CXU(A, τ) / (area(A) × τ)

Measures spatial intensity of organized computation per territory. Useful for territorial comparison.

**Exergetic Intelligence Ratio (EIR)**:

> EIR = I_retained / Ξ_consumed

where I_retained is structured information (models, knowledge, coordination capacity) maintained per unit time. How to measure I_retained is an open research problem; EIR is conceptually useful before it is operationally precise.

**Resilience Depth (RD)**:

> RD = τ_autonomous × κ_mean

where τ_autonomous is the maximum duration of full cognitive function under external supply interruption. RD measures temporal resilience relative to operating level.

**Gradient Coupling Efficiency (GCE)**:

> GCE = Ξ_cognitive / Ξ_primary

the fraction of primary exergy (e.g., solar irradiance on a territory) ultimately converted to cognitive exergy. Current systems achieve GCE ≈ 10⁻⁴ to 10⁻³. Improving GCE is a core engineering challenge.

### 8.3 Measurement Challenges

Operationalizing these metrics requires: standardized exergy accounting at infrastructure scale; information-theoretic measures of organizational output; territorial data at appropriate spatial resolution; and temporal alignment between intermittent energy supply and variable cognitive demand. These requirements are themselves a research agenda.

---

## 9. Potentics as a Research Program

Potentics is not proposed as a completed theory. It is proposed as an open research direction.

### 9.1 Working Hypotheses: Summary

| Hypothesis | Statement | Testability | Priority |
|-----------|-----------|-------------|----------|
| P1 | Civilizational intelligence is a dissipative structure maintained by exergy flux | Historical analysis, comparative exergy accounting | Medium |
| P2 | A minimum κ_min exists below which complex adaptation fails | Empirical survey across territories and epochs | High |
| P3 | Civilizational resilience is measurable as η_cog | Institutional benchmarking, AI efficiency studies | High |
| P4 | Optimal cognitive networks exhibit scale-free topology with λ₂ ∝ criticality | Network analysis of real infrastructure | Medium |

### 9.2 Open Research Questions

- Can resilient intelligence production be measured relative to available exergy?
- Does a universal κ_min exist, or is it scale- and technology-dependent?
- Do certain geographic configurations structurally favor distributed cognitive infrastructure?
- How should renewable intermittency and distributed AI inference be co-optimized temporally?
- What governance forms maximize long-term organizational resilience per exergy unit?
- Is there a meaningful relationship between Friston's free energy minimization and exergy minimization at civilizational scale?
- Which network topologies best preserve adaptive capacity under cascading failure?

### 9.3 Relationship to Existing Fields

Potentics does not claim novelty in any single discipline. Its proposed contribution is integration:

| Field | Contribution to Potentics | Limitation addressed |
|-------|--------------------------|---------------------|
| Thermodynamics | Exergy, entropy, dissipative structures | Does not address territorial or cognitive specifics |
| Information theory | Shannon entropy, Landauer bound | Largely a-physical in applications |
| Network science | Topology, robustness, algebraic connectivity | Does not model energy flows jointly with information flows |
| Emergy analysis (Odum) | Transformity, solar basis of value | Not extended to AI computation |
| Free energy principle (Friston) | Adaptive model minimization | Not extended to territorial infrastructure |
| Energy geography | Spatial analysis of energy systems | Does not model cognitive outputs |

### 9.4 Methodological Approaches

Potential methods include: thermodynamic modeling (exergy analysis, entropy accounting); network science (graph theory, spectral methods, robustness analysis); complexity science (criticality, phase transitions); cybernetics (feedback systems, viable system model); infrastructure studies; distributed systems engineering; AI systems analysis; and political economy.

---

## 10. Conclusion

The renewable era may be forcing civilization to rediscover a fundamental reality: intelligence is physical.

Thought depends on infrastructure. Infrastructure depends on energy. Energy depends on gradients. Gradients depend on cosmic, geological, biological, and social conditions. The Landauer bound tells us that no intelligence — artificial or biological — is exempt from thermodynamic law. Prigogine tells us that organized complexity requires continuous exergy throughput. Friston tells us that adaptive systems are fundamentally about model maintenance — and model maintenance has a physical cost.

Potentics proposes that these relationships should no longer be studied in isolation. It is an attempt to reconnect exergy, geography, computation, infrastructure, governance, and intelligence within a common framework centered on the organization of distributed potentials.

The formal apparatus proposed here — Cognitive Exergy Density κ, the Compute eXergy Unit CXU, Exergetic Intelligence Ratio EIR, and the four working hypotheses P1–P4 — is explicitly preliminary. The metrics require empirical validation. The hypotheses require testing against real systems. The governance implications require institutional analysis well beyond what a single paper can provide.

---

> **Potentics is proposed as an open research program, not a completed theory. The metrics and hypotheses presented here are first approximations. Their value will be determined by whether they prove useful for guiding infrastructure decisions and generating testable predictions. Empirical tests, critiques, and extensions from any discipline are invited. The Mediterranean island of Corsica may serve as one living laboratory among others — but it is neither the only one, nor a predetermined success.**

---

## Acknowledgments

This paper was developed iteratively using what the author terms the *Seconde méthode* — a practice of systematic critical review in which successive drafts are submitted to independent AI reasoning systems for structured evaluation prior to human revision. Specifically, Anthropic's Claude (Sonnet 4.6) contributed to the development and structuring of the expanded draft, and xAI's Grok provided two rounds of critical review, including a quantified "Bullshit Meter" assessment that guided successive rounds of hedging, caveat placement, and sectional reorganization. The governance content was relocated to an appendix and the value multipliers revised downward as a direct result of this process.

The author remains solely responsible for all scientific claims, hypotheses, and errors. The AI contributions were editorial and critical, not generative of the underlying scientific content.

## References

Acemoglu, D., & Robinson, J. A. (2012). *Why Nations Fail: The Origins of Power, Prosperity, and Poverty*. Crown Publishers.

Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development*, 17(6), 525–532.

Diamond, J. (1997). *Guns, Germs, and Steel: The Fates of Human Societies*. W. W. Norton.

Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Georgescu-Roegen, N. (1971). *The Entropy Law and the Economic Process*. Harvard University Press.

IEA (2024). *Electricity 2024: Analysis and Forecast to 2026*. International Energy Agency, Paris.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191.

Odum, H. T. (1988). Self-organization, transformity, and information. *Science*, 242(4882), 1132–1139.

Patterson, D., Gonzalez, J., Le, Q., Liang, C., Munguia, L.-M., Rothchild, D., & Dean, J. (2021). Carbon considerations for large language model training under different constraints. *arXiv preprint arXiv:2104.10350*.

Prigogine, I., & Stengers, I. (1984). *Order Out of Chaos: Man's New Dialogue with Nature*. Bantam Books.

Robert, J. H. (2025). *Cahier des Charges: Safe Compute Exergy (SCE) — Compute eXergy Unit (CXU)*. Institut Mariani, Corte. [github.com/JeanHuguesRobert/marenostrum]

Schrödinger, E. (1944). *What is Life? The Physical Aspect of the Living Cell*. Cambridge University Press.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

Simon, H. A. (1962). The architecture of complexity. *Proceedings of the American Philosophical Society*, 106(6), 467–482.

Tainter, J. A. (1988). *The Collapse of Complex Societies*. Cambridge University Press.

---

*Released under CC BY-SA 4.0. Comments and contributions: jhr@baronsmariani.org | github.com/JeanHuguesRobert/marenostrum*

---

## Appendix A: Exploratory Governance Hypotheses (MareNostrum)

*This appendix is not part of the core scientific argument. It records institutional questions generated by applying the Potentics framework to the Corsica reference scenario. None of the proposals below has been validated, costed, or formally proposed to any institution.*

**A.1 Mediterranean Solar Commons.** If solar radiation is treated as a territorial commons — analogous to maritime commons under UNCLOS — cooperative exergy accounting protocols could enable fair-use and revenue-sharing agreements among Mediterranean island territories (Corsica, Sardinia, Sicily, Cyprus, Malta). The 1951 CECA provides a historical precedent for sectoral resource pooling across sovereign states.

**A.2 Municipal Participation Structures.** A three-tier institutional structure is tentatively proposed: (i) a SCIC SA as operational core, with impartible reserves constituting a sovereign fund; (ii) a Fonds de Dotation for distributing compute revenue to participating municipalities; (iii) an OFS/BRS mechanism for perpetual affordable housing tied to infrastructure revenue. This structure would need to be tested against French cooperative law and EU state-aid rules before implementation.

**A.3 The Compute Token as Unit of Account.** The AI compute token — a unit of scheduled inference capacity — may serve as a non-fiat store of value for territorial sovereignty agreements in a distributed AI economy, in a role analogous to gold in Bretton Woods-era monetary systems. This is a speculative institutional analogy, not a monetary proposal.

*These three directions are included because the Potentics framework, if valid, implies institutional consequences — and intellectual honesty requires making those implications explicit even when they are speculative. They should not be read as advocacy.*
