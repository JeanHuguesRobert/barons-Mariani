---
title: "Potentics of Compute"
subtitle: "From Dormant Capacity to Collective Capability"
description: "A bounded case study applying Potentics to distributed compute: the RAIX declination for compute, the cost of trust as a strong and testable binding-constraint hypothesis, a calibrated Compute Weather, and net delivered value with externalities as first-class constraints."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A. / FractaVolta"
date: "2026-07-30"
last_modified_at: "2026-07-30"
license: "CC BY-SA 4.0"
language: "en"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/potentics_of_compute.md"
last_stamped_at: unknown
version: "0.3"
status: "working-paper — published working hypothesis, under human arbitration"
methodology:
  - "Seconde méthode"
  - "Cogentia pipeline"
ai_assisted_by:
  - "ChatGPT — v0.1 drafting and v0.3 integration"
  - "Claude — v0.1 adversarial review and v0.2 redaction"
  - "Grok — constructive review of v0.2"
version_history:
  - "v0.1 — 2026-07-30 — initial draft"
  - "v0.2 — 2026-07-30 — Claude review integrated"
  - "v0.3 — 2026-07-30 — independent source verification and Grok review integrated"
document_role: "source"
tags:
  - potentics
  - distributed-compute
  - raix
  - compute-weather
  - capacity-fault
  - verifiable-inference
  - externalities
  - fractanet
related_documents:
  - "JeanHuguesRobert/barons-Mariani/research/potentics.md"
  - "JeanHuguesRobert/FractaVolta/research/capability_regimes.md"
  - "JeanHuguesRobert/FractaVolta/research/assured-capacity-reservations.md"
  - "JeanHuguesRobert/FractaVolta/research/garanteed_inference.md"
  - "JeanHuguesRobert/FractaVolta/research/inference_packet_network.md"
  - "JeanHuguesRobert/FractaVolta/research/value_shaped_solar_and_containerized_compute.md"
  - "JeanHuguesRobert/FractaVolta/research/fractanet.md"
  - "JeanHuguesRobert/FractaVolta/research/UNCONSCIOUS_GRID.md"
  - "JeanHuguesRobert/FractaVolta/research/packet_paper_template.md"
  - "JeanHuguesRobert/barons-Mariani/research/second_method.md"
  - "JeanHuguesRobert/barons-Mariani/research/review_protocol.md"
x-address: "1 cours Paoli, F-20250 Corte, Corsica, France"
x-email: "jhr@baronsmariani.org"
x-website: "https://fractavolta.com"
x-pending_human_arbitration:
  - "O1 — RAIX expansion: single owner of the acronym"
  - "O13 — χ as compute-specific dimension or amendment to canonical Π"
provenance:
  origin_type: "conversation"
  origin_repository: unknown
  origin_ref: unknown
  origin_date: "2026-07-30"
  derived_from:
    - "JeanHuguesRobert/barons-Mariani/research/potentics.md"
    - "Potentics_of_Compute.md v0.2"
review:
  status: "reviewed"
  reviewed_by:
    - "Claude (Anthropic), under cogentia/prompts/reviewer.md v0.1, 2026-07-30"
    - "Grok — constructive review, independently checked against primary sources, 2026-07-30"
update_policy: "UP-DEFAULT-REVIEWED"
---

# Potentics of Compute

## From Dormant Capacity to Collective Capability

**Jean Hugues Noël Robert, baron Mariani**
Institut Mariani / C.O.R.S.I.C.A. / FractaVolta
1 cours Paoli, F-20250 Corte, Corsica, France
jhr@baronsmariani.org | fractavolta.com

*Source working paper — v0.3 — July 2026*
*License: CC BY-SA 4.0*

---

## Abstract

Somewhere in the room where this sentence was written, a graphics card is idle. It has been idle for most of the day, it will be idle most of the night, and its owner pays for the electricity that keeps its fans turning slowly in the dark. Multiply that machine by the number of rooms in Europe and the arithmetic becomes provocative. Divide it by everything that stands between a dormant chip and a delivered answer, and the arithmetic becomes a research problem.

This note treats distributed compute as a bounded, measurable case study for Potentics. Its object is not nominal computing power considered in isolation, but the potentiality of heterogeneous, intermittently available, geographically dispersed or economically devalued resources to become useful collective capacity.

The claim is deliberately narrow. Orchestration creates no physical compute *ex nihilo*. What an appropriately organised array may produce is not more arithmetic but more *useful, continuous and controllable* capacity than the same resources considered as isolated units — and, more importantly, capacity of a kind that concentrated infrastructure does not supply: less captive, more local, more reversible.

Version 0.1 of this note argued that availability and compatibility were the binding constraints. Adversarial review overturned that ordering. This version adopts a stronger, deliberately falsifiable hypothesis: for the workload classes in scope, the binding constraint is the cost of trust. Cheap resources belonging to strangers are worth what their results can be proven to be worth, and if proof demands two or three redundant executions, the economic advantage of cheapness is consumed by the redundancy that makes it credible. That inversion is the central hypothesis of the note, not a demonstrated general law, and it has a principal falsifier.

Three instruments follow. A potentiality profile Π(c) declining the canonical dimensions of Potentics onto a compute configuration, extended by one compute-specific dimension for externalities. A *Compute Weather*: not a price forecast, which markets already produce, but a calibrated forecast of the physical and behavioural layer beneath price, scored against declared baselines, whose operational purpose is the reduction of *capacity faults*. And a value equation in which delay decays usefulness rather than subtracting from it, and in which externalities are constraints rather than a late ethical correction.

The programme is not to build a worldwide Fractanet. It is to discover, at the smallest cost that produces knowledge, which combinations of diversity, redundancy, prediction, verification and governance let a real potentiality become a collective capability — and to preserve the failures, which in this discipline carry the same epistemic weight as the successes.

## Keywords

Potentics; distributed compute; RAIX; Compute Weather; capacity fault; verifiable inference; provenance; externalities; correlated failure; Fractanet.

---

## 1. Introduction

### 1.1 One machine, three numbers

Begin with the machine in the room, and refuse the temptation to generalise before measuring it.

It holds perhaps sixteen gigabytes of video memory. The model its owner would actually like to run, quantised to four bits, wants forty. That is not a graded difficulty; it is a wall. The machine cannot host the task at all, and no amount of orchestration will persuade it otherwise.

Suppose the task is resized to fit. The weights must arrive. On a domestic uplink of twenty megabits per second, forty gigabytes take somewhat over four hours. The first inference of the day therefore costs a morning, unless the weights were already there — which is a caching problem, not a compute problem, and which changes the architecture rather than the hardware.

Suppose they were already there. The machine is five years old. Per useful token it may spend several times the energy of current silicon; the factor is commonly asserted to lie between three and ten, and this note does not accept that range as established. It is exactly the kind of quantity a bounded pilot should measure, because if it is large, then pooling obsolete hardware increases the environmental cost of the same delivered answer, and the system has optimised its own price by displacing a cost onto someone else's atmosphere.

Three numbers, three distinct barriers: a wall, a delay, an externality. They already show why the interesting object is not old hardware. It is *idle* hardware — a recent gaming machine at three in the morning, a slack window in a datacentre otherwise fully booked, a preemptible instance that costs a fifth of its reserved twin because it may be reclaimed at any moment. Dormancy and obsolescence are not synonyms, and version 0.1 of this note conflated them. Dormancy is an opportunity. Obsolescence is a limit case, and usually an unfavourable one.

### 1.2 Existing architectures

The intuition that idle machines can be harvested is not new, and honesty about its age is the precondition of saying anything new about it.

Cycle-stealing was implemented before it was theorised: Condor hunted idle workstations from 1988 (Litzkow, Livny and Mutka). Volunteer computing turned the practice into an infrastructure with SETI@home in 1999 and Folding@home shortly after, then into a reusable platform with BOINC (Anderson, 2004), which also supplied the canonical answer to untrusted execution — redundant computation and quorum agreement. Grid and desktop-grid literature accumulated two decades of scheduling results. Federated learning (McMahan et al., 2017) moved the problem from cycles to data locality. Spot-instance and preemptible-fleet scheduling made interruption a first-class design parameter, and Sky Computing (Stoica and Shenker, 2021) with its practical descendants such as SkyPilot made cross-provider arbitrage ordinary engineering. Decentralised training over slow, unreliable links has produced its own line of results, from DiLoCo through the decoupled variant of April 2026, and its own demonstrations outside academia. Token-incentivised compute markets have supplied both an existence proof and a catalogue of failure modes.

The verdict of that literature is clear, and it is a bounded verdict. Pooling dispersed resources works, reliably and at scale, for workloads that are massively parallel, latency-tolerant, and cheap to verify by repetition. Outside that envelope it has repeatedly failed to displace concentrated infrastructure.

This note therefore does not claim the pooling result. It inherits it, along with its boundary.

### 1.3 Research gap and contribution

What the existing work does not supply is what Potentics asks for.

First, a graded account of the *potentiality* of a resource, as distinct from the binary question of whether a task can physically run on it — an account in which availability, compatibility, integration effort, coordination effort, use value, reversibility and externalities are named dimensions rather than implicit engineering constraints.

Second, a *calibrated* forecast of deliverable capacity. Schedulers react; markets price; neither produces a scored prediction of what a heterogeneous fleet will actually be able to deliver at a stated horizon, with an error that can be audited after the fact.

Third, externalities as constraints rather than as afterthought. Volunteer computing spent the owner's electricity without accounting for it. Spot markets externalise interruption onto the customer. A system that lowers its own price by exhausting a battery its owner needs has not created value; it has moved a cost out of its own ledger.

Fourth, *independence* as an explicit design dimension rather than a rhetorical virtue. A thousand nodes under one opaque operator, on one route, in one jurisdiction, on one supply chain, behind one model provider are numerous and structurally fragile at the same time.

The contribution of this note is the declination of those four items onto one substrate, with the vocabulary and the falsifiers stated. It is a research note, not a result.

### 1.4 Methodological status

This note follows the Seconde méthode. Claims are versioned and numbered (§12). Objections are first-class contributions: the review that reshaped this version is published alongside it, and §13 records which objections were integrated, which were deferred, and which await human arbitration. The corpus is the primary document; this file is a snapshot of it.

The note is a source document. Derived products for general audiences must remain traceable to it, and must not inherit its hypotheses as if they were results.

### 1.5 What this paper does not claim

- It does not claim that distributed low-grade compute will generally outperform concentrated infrastructure. Large-scale training and tightly coupled workloads will continue to require dense, high-grade systems.
- It does not claim that pooling dispersed resources is a new idea. §1.2 states the contrary.
- It does not claim that the cost of trust has been measured. It advances, for the declared workload classes and proof levels, the strong hypothesis that it is binding, and states how it would be measured.
- It does not claim that Π is a unified metric, nor that it is cardinal.
- It does not claim that Compute Weather is achievable at a useful horizon. It states the score, the baseline and the failure condition under which the idea should be abandoned.
- It does not claim that compute is a *packet* in the sense of the Generalized Packet Networks framework. That claim would trigger the operational boundary rule of the packet paper template and is deliberately not made here; inference packets are treated in their own paper.
- It does not claim that the Corsican case generalises. Corsica is the laboratory, not the subject.

### 1.6 Disclosures

The author has a direct interest in the outcome. FractaVolta SAS would benefit from a favourable answer to the RAIX hypothesis. This note is published in the barons-Mariani repository, not the FractaVolta repository where the implementation layer is elaborated, including the prospective *Seconde Vie* offer built on second-life hardware. The author is a candidate for the French Senate for Haute-Corse in September 2026 on a platform, Plan 2038, that includes compute sovereignty. Institut Mariani of the C.O.R.S.I.C.A. non profit association governs the research corpus.

That last interest cuts against this note rather than with it, and the reader should notice. §1.1 and §5 treat obsolete hardware as the unfavourable limit case, not as the paradigm case, and §9 makes the energy penalty per useful token a measurement task rather than a premise. If that measurement comes back at the high end of the asserted range, the second-life *compute* case weakens — while the second-life *battery* case, RAIB, is untouched, because the two substrates degrade differently: a retired cell arrives with its embodied carbon already amortised and fails gracefully, whereas an ageing accelerator spends fresh energy on every token it produces. Conflating the two would flatter the commercial layer at the expense of the argument. The note declines to.

The declaration is not a formality. A researcher who would gain from an affirmative result must publish the falsifiers first, which is why §4 and §12 are written as they are, and why the review that produced this version is published rather than summarised.

---

## 2. Compute as potentiality

A dormant GPU, an older server, an intermittently connected vehicle, a preemptible instance, an unused window in an otherwise busy machine: none of these is necessarily useless. Each is a possible source of compute whose propensity to contribute to a useful result remains partially unrealised. The distinction Potentics draws between possibility and potentiality applies to them without adjustment.

A compute resource is *possibly* usable if a compatible task can physically execute on it. That question is binary and usually easy. Its *potentiality* is graded, and depends on whether it is likely to be available when needed, whether the relevant model can run at all, whether data can transit in time, whether execution can resume after interruption, whether the result can be trusted, and whether the resulting service has value for a real user at the moment it arrives.

For a compute configuration *c*, the potentiality profile is written as a declination of the canonical Π:

\[
\Pi(c) = f(
\phi_{\text{availability}},
\phi_{\text{compatibility}},
\epsilon_{\text{integration}},
\epsilon_{\text{coordination}},
\upsilon_{\text{use}},
\rho_{\text{reversibility}},
\chi_{\text{externalities}}
)
\]

Three statements make this usable rather than decorative.

*Correspondence.* φ, ε, υ and ρ are the canonical propensity, effort, value and reversibility dimensions of Potentics, subscripted for this substrate. χ is a compute-specific dimension added here. Whether χ should be promoted to the canonical set is a question for the source document, not for this note; it is recorded as pending arbitration (O13).

*Monotonicity.* Π is non-decreasing in φ, υ and ρ, and non-increasing in ε and χ. Nothing more is asserted about the shape of *f*.

*Ordinality.* Π is ordinal at this stage. It supports the comparison of two configurations under a stated task class; it does not support arithmetic. Any table of Π values must therefore be read as a ranking.

One clarification prevents a drift that would travel back into the source document. φ_availability admits a probabilistic estimator: the fraction of a time window in which a node responds is a frequency and can be forecast. Π as a whole is not a probability, and does not become one because one of its dimensions can be estimated that way. Potentiality remains a conditional, graded, revisable assessment of a path to actualisation; probability is one input to it.

---

## 3. The array and its two conditions

### 3.1 RAIX, and a note on ownership of the acronym

Within this corpus, RAIX is already defined. `capability_regimes.md` §6 gives it as *Redundant Array of Independent X*, where X ranges over compute, model, agent, gateway, route, cache, trace, policy, energy source, institution and human reviewer, and attaches claim CR-05: redundant capacity need not be active everywhere at all times, but must be mobilisable when the regime requires it.

This note is therefore not the introduction of RAIX. It is its first substrate declination for compute — the taxonomy work that `capability_regimes.md` §19 asks for — and it inherits CR-05 rather than restating it. Version 0.1 derived RAIX instead from the *inexpensive* branch of the RAID intuition (Patterson, Gibson and Katz, 1988) and asserted that both properties were required. That produced two expansions of one acronym inside one corpus, which is nuance and not a defect.

This version adopts the pre-existing expansion — *Independent X* — and treats inexpensiveness as a separately named premise rather than as part of the acronym. The precedent for that premise is already in the corpus: RAIB, *Redundant Array of Inexpensive Batteries*, in `UNCONSCIOUS_GRID.md` §6.3, where redundancy of cheap components replaces quality of expensive ones as the model of reliability. The compute case is the same argument on a different substrate, and can borrow its name honestly instead of overloading another.

### 3.2 The hypothesis

> A well-orchestrated array of independent resources, made cheap enough that redundancy and experimentation are affordable, can provide a higher-grade collective capability than the same resources left isolated.

"Higher-grade" requires care, because the word carries three meanings in this field — hardware quality, contractual service class, and position on Π — and confusing them is how such claims become empty. Here it means the third, and specifically: the array can obtain properties that no isolated resource possesses. Discovery and matching of task to capability. Pooling of unused capacity. Graceful rather than catastrophic degradation. Checkpointing, migration and fallback. Diversity of hardware, routes, jurisdictions and energy sources. Explicit measurement of faults. Contractual classes of service.

An old accelerator does not become a recent one. That is not the claim, and no orchestration layer will make it so.

### 3.3 Against the stupid sum, and against a better opponent

The whole is not superior to the sum of its parts in any mystical sense. It is superior to the *stupid sum* of parts: a set of resources unable to discover one another, coordinate, compensate for faults, or learn from their own history.

The phrase is exact and it is also a trap, because nobody defends the stupid sum. A test won against it proves nothing. The comparison classes that matter are the ones the field actually fields: container orchestration and distributed execution frameworks; spot-fleet and cross-provider schedulers; BOINC-style quorum volunteer computing; and hyperscale itself, whose insufficiency for critical inference is argued separately in `garanteed_inference.md` §2. Every experiment proposed in §9 must declare which of these it is measured against. An experiment that declares none has measured nothing.

### 3.4 Independence, and how to stop asserting it

Independence carries half of the hypothesis and is usually left as a virtue. It has to become a quantity.

Two instruments are available. The corpus already specifies a dependency and correlated-risk graph in `assured-capacity-reservations.md` §18; it applies here without modification. Alongside it, a diversity index over the axes that actually produce common-mode failure — operator, jurisdiction, network route, energy source, model provider, silicon vendor — makes the difference between a thousand nodes and a thousand *independent* nodes measurable.

The estimation path is available too. The two-state Markov failure process already implemented in `ipn_sim.js` extends to correlated failures at modest cost, which converts independence from a preference into a hypothesis that a simulator can attack.

---

## 4. The cost of trust

This section did not exist in version 0.1, and its absence was the most serious defect of that draft.

Executing work on cheap machines belonging to strangers raises a question that precedes availability, compatibility and coordination: how does the requester know that the node ran the requested computation, with the declared model, and did not fabricate a plausible answer? The question is not exotic. A result that cannot be trusted has no use value, so υ collapses, and with it Π — however available and compatible the resource was.

The corpus already holds the beginning of an answer, and version 0.1 failed to import it: inference provenance and graded proof levels in `garanteed_inference.md` §7–§8, and the COP invariants of deterministic replay and transparency over convenience. Volunteer computing supplies the historical answer, which is cruder and better tested: execute redundantly and compare. Trusted execution environments and cryptographic proofs of inference offer stronger guarantees at a cost that is, at the time of writing, poorly characterised for models of useful size.

The consequence is the pivot of this note.

Let *r* be the effective end-to-end trust overhead required for a result to be admissible at a stated proof level:

\[
r = \frac{C_{\text{admissible array result}}}{C_{\text{reference result}}}
\]

The numerator includes replication where used, scheduling, coordination, proof production, proof verification, recovery from failure and any human or automated adjudication. This distinction matters. A lightweight verifier may cost about one per cent of an inference in a particular protocol; that does not make the production of a cryptographic proof free, nor does it remove the assumptions on which the protocol rests. Conversely, a workload with cheaply checkable output may need neither full replication nor a zero-knowledge proof. *r* is thus not a property of a GPU, but of a workload, an adversary model, a proof level and an architecture.

The cheap-resource advantage over a reference provider is real only if this end-to-end cost remains below the cost of one admissible reference execution. If *r* lies near two or three for the workload classes that matter, the advantage of cheapness is consumed by the trust mechanism, and the RAIX hypothesis fails for those classes — not because the machines were unavailable, but because their answers were unaffordable to believe.

The strong hypothesis of this note is therefore that, for the in-scope classes whose outcomes cannot be cheaply verified, the cost of trust is the binding constraint on RAIX. Availability remains a possible falsifier of a particular service, but it is not expected to be the first economic constraint. This is claim C6 in §12, and the experiment that attacks it is the first one worth running, before any question of fleet size or forecast quality.

It follows that verification is not a security annexe but an architectural parameter, and that proof level belongs in the service class alongside latency and price. A buyer should be able to purchase a cheap unverified answer, an expensive proven one, or a graded compromise, and should be told which was delivered.

---

## 5. Quantitative limits

The three numbers of §1.1 generalise into the three constraints that decide admissibility, and they should be stated as thresholds rather than as symbols.

**Memory.** Resident weights are a wall, not a gradient. A configuration is admissible for a task only if the quantised model, its context and its runtime overhead fit; otherwise φ_compatibility is zero regardless of every other dimension. Consumer-class accelerators commonly offer eight to twenty-four gigabytes; useful open-weight models at four-bit quantisation range from a few gigabytes to well beyond that ceiling. This single constraint eliminates most of the dormant fleet for most of the interesting tasks, and it is the reason the interesting workloads are small models, shards, and batch work rather than frontier inference.

**Transfer.** Weight and data movement is a delay with a hard floor: time equals quantity divided by transfer rate. Forty gigabytes over a twenty-megabit domestic uplink is a matter of hours; over a hundred megabits, of tens of minutes. Cold placement is therefore incompatible with any interactive deadline, and warm caching is not an optimisation but a precondition. The corpus vocabulary for this is the hot/cold gradient, and it applies literally.

**Energy.** Older silicon spends more energy per useful token. The magnitude is asserted more often than measured; this note treats it as unknown within a plausible range and as a measurement task, not as a premise. The methodological point is independent of the number: if the factor is large, obsolete hardware raises χ, and a system that ignores χ can appear cheaper while being worse. That is precisely the failure mode §7 exists to prevent.

---

## 6. Compute Weather

### 6.1 What it is not

A spot market does not directly measure the deliverable capacity of a particular heterogeneous fleet at a stated service level. It measures price, which is an incomplete and endogenous signal. Public-cloud spot availability varies with supply and demand; past performance is not a guarantee. Empirical work shows that availability signals can nevertheless be informative at useful short horizons. The research question is therefore not whether availability is metaphysically predictable, but whether a declared model beats declared baselines for the allocation decision at hand.

Nor is generation forecasting the novelty. This corpus already specifies solar generation forecasting at fifteen-minute resolution up to forty-eight hours ahead, driving workload pre-scheduling, in `value_shaped_solar_and_containerized_compute.md`. Compute Weather sits on top of that, not beside it.

### 6.2 What it is

Compute Weather is a calibrated forecast of the physical and behavioural layer beneath price: which nodes and which compute profiles will probably be available; what demand and task mix will probably arrive; what transit delay and network reliability to expect; what hazard of interruption or preemption applies; and — the quantity that actually matters — the probability that a promised service level can be met.

Its operational purpose is the reduction of *capacity faults*. A capacity fault is an event, not a mood: a task that cannot be served within its declared constraints because the required compute, route, model, proof level, budget or time window is absent. Events are countable. Countable events have costs. A system that reports its fault rate and its fault cost per period can be argued with.

### 6.3 How it is scored

A forecast without a score is a promise, and a promise about scarcity made by a party that sells scarcity relief is worse than no forecast at all. The commitments are therefore stated in advance.

*Scores.* Brier score for binary availability and interruption events; continuous ranked probability score, or pinball loss at declared quantiles, for capacity and delay distributions.

*Baselines.* Persistence — tomorrow resembles today — and climatology, the seasonal and diurnal mean. A forecast that does not beat both has no demonstrated incremental value.

*Horizons.* Declared and separately scored: minutes for preemption hazard, hours for availability and demand, days for capacity planning. Skill at one horizon is not skill at another and must not be reported as such.

*Decision link.* The value of the forecast is the reduction in permanently held premium reserve at constant fault rate — a newsvendor problem, whose solution states how much reserve a given forecast skill saves. If that reduction is not measurable, the forecast has no economic content whatever its score.

*Abandonment condition.* If no configuration beats persistence and climatology on the declared scores at any useful horizon, Compute Weather should be abandoned and the note amended to say so. This is claim C7 and its own falsifier.

### 6.4 Why the weather analogy is dangerous

The atmosphere does not play against the forecast. A fleet of node owners and capacity buyers does.

A published availability forecast changes the behaviour it forecasts: owners withhold capacity when tension is announced, buyers pre-book, and the prediction partly produces its own realisation. Worse, whoever publishes the forecast while selling reserve capacity has a standing incentive to forecast tension. The corpus already names this structure and its remedy: the anti-arson invariant of `assured-capacity-reservations.md` §9, which forbids profiting from self-created scarcity, together with the trigger governance and evidence requirements of that document.

The transposition to information about capacity is direct and should be adopted before any forecast is published: separation between the party that scores the forecast and the party that sells the relief; publication of forecasts and outcomes together; and an audit trail on the trigger that turns a forecast into a reservation. A forecaster who is also an arsonist is not a meteorologist.

---

## 7. From price to value

The price of a GPU-hour is not the value of compute. An inference that arrives after the decision it was meant to inform has expired may be worthless however cheaply it was produced. A modest local inference may be worth a great deal if it preserves continuity through a network, cloud, energy or institutional failure.

Version 0.1 wrote this as a subtraction, and the subtraction contradicted its own example: an expired deadline is a cliff, not a discount. The corrected form separates decay from cost.

Let *R* be the delivered result in value units, *d(t)* a freshness factor in [0,1] with *d(t) = 0* beyond the hard deadline, *F* the expected fault cost, *X* the externalised cost, and *V* the net delivered value:

\[
V = R \cdot d(t) - F - X
\]

with, following the corpus mathematical layer, an exponential decay *d(t) = e^{-t/\tau}* where usefulness fades gradually, and a step at the deadline where it does not. Where a unit of account is required, the corpus supplies one: the Compute eXergy Unit of `garanteed_inference.md` §9.

Two properties of this form matter more than its algebra. It is a *value*, not a capacity — the confusion of the two was the dimensional error of version 0.1, and net delivered value per service unit, not throughput, is the quantity to compare across configurations. And *X* is inside the equation rather than appended to it. A system that lowers its own price by exhausting a battery its owner needs, congesting a local network, exposing private data, concentrating market power or displacing an environmental cost has not created net value; it has moved a cost off its own books. Externalities are constraints, not a concluding paragraph about ethics.

---

## 8. The frontier of this laboratory

Every piece of research in this corpus declares its frontier. Here it is.

| Workload class | In scope | Reason |
|---|---:|---|
| Batch embedding and indexing | yes | parallel, latency-tolerant, cheap to verify by repetition |
| OCR, transcription, speech-to-text at batch | yes | same, with verifiable outputs |
| Low-priority fine-tuning shards | yes | interruption-tolerant with checkpointing |
| Retrieval and pre-computation for local services | yes | value is continuity, not speed |
| Long-horizon agentic work with slack deadlines | yes | tolerant of migration and restart |
| Small-model inference under local sovereignty constraint | yes | value from locality and reversibility |
| Interactive inference under sub-second service levels | no | transfer floor and interruption hazard |
| Frontier-scale training | no | tightly coupled, dense high-grade systems required |
| Any task whose resident weights exceed available memory | no | φ_compatibility is zero, not small |
| Work whose results cannot be verified at any affordable redundancy | no | §4; υ collapses |

The frontier is itself revisable. Moving a line requires a measurement, not an argument.

---

## 9. Why test before building

The first question is not whether a worldwide Fractanet should be built. It is whether the hypothesis is worth testing at all — a direct case of epistemic metapotentiality:

\[
\Pi_e = \text{value of knowing whether distributed compute potentiality is real}
\]

Part of that knowledge already exists in this corpus and version 0.1 understated it. The inference packet network paper, with its zero-dependency solar-backed simulator, has already exercised part of the question and validated part of its claim set under explicitly declared limits. What it did not settle is what this note now places first: the cost of trust, correlated failure, forecast skill against declared baselines, and net delivered value including externalities.

A small simulator and a bounded pilot can produce that knowledge at a fraction of the cost of premature deployment. Each comparison is stated so that it can fail:

- verified against unverified execution, at declared proof levels, measuring *r* and total cost per admissible result — the experiment of §4, to be run first;
- isolated against pooled resources, against a declared non-trivial baseline from §3.3;
- reactive against forecast-driven allocation, scored per §6.3;
- homogeneous fleets against diverse fleets, under the correlated-failure model of §3.4;
- ordinary routing against checkpointing and migration, under measured interruption hazard;
- economic gain before and after accounting for *X*.

Failures are informative if they are preserved, which requires a place to preserve them. This corpus has one: the interaction packet registry with its graded disclosure levels, and the claim manifest below, in which a refuted claim is marked refuted rather than quietly removed. A failed routing policy, an unavailable vehicle node, an uneconomic old accelerator, a forecast that will not calibrate — each reduces uncertainty about the true potentiality of the system, and each is worth its cost only if it is written down.

---

## 10. Failure modes

| Mode | Description | Severity | Detection |
|---|---|---:|---|
| Trust collapse | verification overhead exceeds the cheapness advantage | fatal to C5 | measure *r* and cost per admissible result |
| Compatibility wall | resident weights exceed node memory across the fleet | fatal per task class | static admission check |
| Cold placement | transfer time exceeds deadline | fatal for interactive classes | modelled transfer floor |
| Externality inversion | pooling raises energy or displaces cost onto owners | fatal to the value claim | measure *X* before and after |
| Correlated failure | apparent diversity, single common mode | severe | dependency graph, diversity index |
| Forecast capture | forecaster benefits from predicted tension | severe, governance | anti-arson separation, published outcomes |
| Metric drift | reporting throughput instead of net delivered value | severe, epistemic | fix vocabulary, audit reports against §7 |
| Baseline inflation | measuring against the stupid sum | severe, epistemic | every experiment declares its baseline |
| Owner attrition | contributors leave once real costs appear | moderate | track retention as a first-class metric |
| Conceptual inflation | treating compute as a packet without passing the boundary rule | moderate | the claim is explicitly not made, §1.5 |

---

## 11. Corpus links

**What this note receives.** From `potentics.md`: the possibility/potentiality distinction, the canonical Π dimensions, epistemic metapotentiality, the epistemic value of designed failure. From `capability_regimes.md`: the RAIX definition and CR-05 regime-sensitivity. From `assured-capacity-reservations.md`: capacity promises, degraded and substituted delivery, the correlated-risk graph, the anti-arson invariant. From `garanteed_inference.md`: provenance, proof levels, CXU, and the correct adversary in hyperscale. From `value_shaped_solar_and_containerized_compute.md`: generation forecasting and pre-scheduling. From `inference_packet_network.md`: the simulator and its declared limits. From `UNCONSCIOUS_GRID.md`: the RAIB precedent for cheap-component redundancy. From `packet_paper_template.md`: claim manifest discipline, non-claims, mathematical forms, and the boundary rule this note declines to trigger. From `second_method.md`: publication of process, objections as contributions, corpus as its own evidence.

**What this note gives back.** To `potentics.md`: a substrate declination of Π, and a candidate new dimension χ awaiting arbitration. To `capability_regimes.md`: the compute branch of the RAIX taxonomy its continuation section requested, and a request to settle the acronym. To `assured-capacity-reservations.md`: the transposition of the anti-arson invariant from capacity to information about capacity. To `garanteed_inference.md`: proof level as a purchasable service-class parameter, and *r* as the quantity that decides the business case. To `fractanet.md`: a laboratory programme with declared falsifiers rather than an architectural assertion.

---

## 12. Claim manifest — v0.3

| Claim | Status | Description |
|---|---|---|
| C1 | Definition | The potentiality of a compute configuration is a graded, conditional, revisable assessment distinct from the binary possibility of execution, profiled by Π(c) over the seven dimensions of §2 |
| C2 | Definition | A *capacity fault* is an event in which a task cannot be served within its declared constraints because compute, route, model, proof level, budget or time window is absent |
| C3 | Definition | A *Compute Weather* is a scored forecast of the physical and behavioural layer beneath price, not of price itself |
| C4 | Operational rule | Net delivered value, *V = R·d(t) − F − X*, replaces throughput and price as the comparison quantity; *X* is a constraint inside the equation |
| C5 | Hypothesis | An orchestrated array of independent, cheap resources yields higher net delivered value than the same resources isolated, for the workload classes of §8 and against the baselines of §3.3 |
| C6 | Strong hypothesis | For the in-scope workload classes whose outcomes cannot be cheaply verified at the selected proof level, the binding constraint on C5 is the end-to-end cost of trust. If effective overhead *r* approaches two to three, C5 fails for the classes concerned. This is the primary falsifier; it is workload-, adversary- and architecture-specific |
| C7 | Hypothesis | A forecast can beat persistence and climatology on declared scores at a horizon useful for allocation; if not, Compute Weather is abandoned |
| C8 | Metric | Independence is measurable as a diversity index over operator, jurisdiction, route, energy source, model provider and silicon vendor, with correlated failure estimated by an extension of the existing two-state Markov model |
| C9 | Observation | Dormancy and obsolescence are distinct; obsolete hardware raises *X* and is an unfavourable limit case, not the paradigm case |
| C10 | Non-claim | The pooling result is not claimed as new; it is inherited from the literature of §1.2 together with its narrow envelope |
| C11 | Non-claim | Compute is not claimed to be a packet in the Generalized Packet Networks sense; the boundary rule is deliberately not invoked |
| C12 | Research programme | The six comparisons of §9, in the stated order, beginning with the verification experiment |
| C13 | Implementation claim | The corpus simulator is extensible to correlated failure and verification overhead at modest cost, and is the intended first instrument |

---

## 13. Revision history and integration record

Per `review_protocol.md` §6, integration is recorded rather than silent. This section is part of the document, not an annexe to it: a reader is entitled to know which objections shaped the text.

**v0.1 — 2026-07-30.** Drafted with ChatGPT. Structure: compute as potentiality; RAIX derived from the *inexpensive* branch of RAID; Compute Weather as a wishlist; price-to-value as an additive subtraction; epistemic metapotentiality; research commitment. No claim manifest, no non-claims section, no references, no corpus links, no numbers.

**Adversarial review — 2026-07-30.** Claude, under `cogentia/prompts/reviewer.md` v0.1, with corpus inspected at public HEAD. Eighteen objections, three blocking. Published as `review.md`.

| Objection | Source | Severity | Decision | Effect in v0.2 |
|---|---|---:|---|---|
| O1 RAIX collides with `capability_regimes.md` §6 | Claude | Blocking | Provisionally integrated, arbitration pending | §3.1 adopts *Independent X*; inexpensiveness renamed as a premise with RAIB precedent |
| O2 Verification absent, may invert the economics | Claude | Blocking | Integrated | New §4; claim C6 as primary falsifier |
| O3 `useful capacity` dimensionally inconsistent, delay additive | Claude | Blocking | Integrated | §7 rewritten as *V = R·d(t) − F − X* |
| O4 No claim manifest, no non-claims | Claude | Blocking | Integrated | §12 and §1.5 |
| O5 No corpus links | Claude | Blocking | Integrated | §11, bidirectional |
| O6 Existing simulator understated | Claude | Strong | Integrated | §9 opening |
| O7 Forecast unscored | Claude | Strong | Integrated | §6.3 with abandonment condition |
| O8 Forecast performativity | Claude | Strong | Integrated | §6.4 via anti-arson invariant |
| O9 Baseline is the stupid sum | Claude | Strong | Integrated | §3.3 |
| O10 No prior art | Claude | Strong | Integrated | §1.2, with the boundary of the known result |
| O11 Independence unmeasured | Claude | Strong | Integrated | §3.4, claim C8 |
| O12 Dormant/obsolete conflated, no numbers | Claude | Strong | Integrated | §1.1 and §5 |
| O13 χ added to Π without status | Claude | Medium | Partially integrated | §2 declares χ compute-specific; promotion pending arbitration |
| O14 No declared frontier | Claude | Medium | Integrated | §8 |
| O15 Frontmatter | Claude | Medium | Integrated | normalised; `visibility: public` |
| O16 No xPsN / CPsN positioning | Claude | Medium | Deferred | requires the naming decision to be propagated corpus-wide first |
| O17 φ_availability probabilistic while Π is not | Claude | Medium | Integrated | §2, final paragraph |
| O18 "Compute Weather" collision check | Claude | Stylistic | Deferred | to be checked before external submission |

**Hop 3 — constructive review and source verification — 2026-07-30.** A subsequent constructive review proposed that recent verifiable-inference systems might render the cost of trust negligible, requested evidence on spot availability forecasting, and restored the reference to Decoupled DiLoCo. The relevant sources were independently checked. `zkGPT` is a USENIX Security 2025 paper; `NANOZK` is an ICLR 2026 workshop submission; `DeepProve` and `VeriLLM` are current preprints. Their results justify the distinction between verifier cost and end-to-end trust cost introduced in §4; they do not yet falsify C6 across the declared frontier. The evidence on spot availability supports a scored forecasting programme, not an unqualified predictability claim. Decoupled DiLoCo is restored with its arXiv identifier in the references.

**Residual weaknesses of this version, declared and retained here.**

1. Every number in §1.1 and §5 is an order of magnitude, not a measurement, and the energy factor is explicitly declared unknown. A note insisting on quantitative limits still contains no measured quantity.
2. C6 is the pivot of this version but rests on an unmeasured *r*. Cheap verification is plausible for some classes, including outputs that can be checked independently. A measured counterexample would narrow or refute the strong hypothesis, rather than merely qualify it.
3. The frontier table of §8 is a hypothesis in table form, written from argument rather than derived from measurement.
4. §3.1 makes an editorial choice inside an open arbitration. Defensible for a published working hypothesis; indefensible for a frozen canonical artifact.

**Pending human arbitration.** O1 among its three admissible outcomes; O13 on the status of χ. The publication destination is now resolved by this published version; any later canonicalisation remains a separate decision.

**Unpropagated corpus decision noted in passing.** The `FractaNet` capitalisation decided on 2026-07-21 is absent from the repository, which writes `Fractanet` throughout. This note follows the repository and does not arbitrate.

---

## 14. Research commitment

Nothing here asserts that dispersed compute will beat concentrated infrastructure. The narrower proposition is that, for the workload classes declared in §8, a properly governed architecture may convert dormant and underused resources into a valuable continuity layer: less captive, more locally available, more reversible and more resilient than those resources in isolation — and that whether it can do so is decided first by the cost of trust, then by the quality of prediction, then by the honesty of the accounting.

Fractanet is proposed as a laboratory of Potentics applied to compute. Its task is not to assert a global solution in advance. Its task is to discover, through traceable and bounded experiments, which combinations of diversity, redundancy, prediction, verification and governance allow real potentialities to become collective capabilities — and to leave, whichever way the answers fall, a record that someone else can use.

The machine in the room is still idle. That is a fact about the world, not yet an argument. Turning it into one is the work.

---

## References

Anderson, D. P. (2004). BOINC: A System for Public-Resource Computing and Storage. *Proceedings of the 5th IEEE/ACM International Workshop on Grid Computing*.

Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1).

Douillard, A. et al. (2023). DiLoCo: Distributed Low-Communication Training of Language Models. *arXiv:2311.08105*.

Douillard, A. et al. (2026). Decoupled DiLoCo for Resilient Distributed Pre-training. *arXiv:2604.21428*.

Gailly, N. et al. (2026). DeepProve: Verifiable End-to-End Large Language Model Inference. *IACR Cryptology ePrint Archive*, 2026/1112.

Gelenbe, E. (2001–2012). Cognitive Packet Networks; Energy Packet Networks.

Litzkow, M., Livny, M. and Mutka, M. (1988). Condor — A Hunter of Idle Workstations. *Proceedings of the 8th International Conference on Distributed Computing Systems*.

Matheson, J. E. and Winkler, R. L. (1976). Scoring rules for continuous probability distributions. *Management Science*, 22(10).

McMahan, H. B. et al. (2017). Communication-Efficient Learning of Deep Networks from Decentralized Data. *AISTATS*.

Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.

Patterson, D. A., Gibson, G. and Katz, R. H. (1988). A Case for Redundant Arrays of Inexpensive Disks (RAID). *SIGMOD*.

Qu, W. et al. (2025). zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference. *34th USENIX Security Symposium*.

Stoica, I. and Shenker, S. (2021). From Cloud Computing to Sky Computing. *HotOS*.

Wang, K. et al. (2025). VeriLLM: A Lightweight Framework for Publicly Verifiable Decentralized Inference. *arXiv:2509.24257*.

Wang, Z. G. (2026). NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable Large Language Model Inference. *ICLR 2026 Workshop on Verifiable and Reliable AI*.

Kim, K. et al. (2026). Ding-Dong Ditch: Peeking Into Spot Instance Availability. *arXiv:2604.16457*.

Taleb, N. N. (2012). *Antifragile*. Random House.

*Corpus references are given in §11 by path within the repositories listed in the frontmatter. The references newly introduced in v0.3 were checked against their primary publication pages on 2026-07-30. The remaining bibliography remains subject to normal source verification before a frozen or external edition.*

---

## Continuation

1. Arbitrate O1. It is a decision, not an edit, and §3 and §11 depend on it.
2. Decide the status of χ (O13), and if it is promoted, open an amendment note against `potentics.md` rather than editing a document at plateau.
3. Extend `ipn_sim.js` with verification overhead *r* and correlated failure; run the §4 experiment first.
4. Open the Compute Weather work as its own document once §6.3 is instrumented; do not publish a forecast before the anti-arson separation exists.
5. Verify every bibliographic entry against primary sources.
6. Submit this version to a decorrelated hop, then return it to the drafting agent for reintegration.
