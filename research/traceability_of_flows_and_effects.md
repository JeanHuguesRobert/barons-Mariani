---
title: "Traceability of Flows and Effects"
subtitle: "From Follow the Money to a general doctrine of accountable acts, resources, effects, evidence, and burden"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-08-14"
version: "0.2"
status: "working-note — source doctrine"
document_role: "source"
document_kind: "doctrinal-note"
visibility: "public"
lifecycle_state: "working"
language: "en"
license: "CC BY-SA 4.0"
repository: "JeanHuguesRobert/barons-Mariani"
canonical_path: "research/traceability_of_flows_and_effects.md"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/traceability_of_flows_and_effects.md"
update_policy: "UP-DEFAULT-REVIEWED"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "conversation checkpoint R4-R5; extended R47-R52"
  origin_date: "2026-08-14"
  derived_from:
    - "research/concepts.md"
    - "research/second_method.md"
    - "https://github.com/JeanHuguesRobert/inseme/issues/45"
review:
  status: "unreviewed"
  reviewed_by: []
related_documents:
  - "research/concepts.md"
  - "research/second_method.md"
  - "research/potentics.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/research/cogentia_accounting_architecture.md"
  - "https://github.com/JeanHuguesRobert/inseme/blob/main/packages/cop-core/COP_ACCOUNTING.md"
  - "https://github.com/JeanHuguesRobert/inseme/issues/45"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/administrative_burden_and_exemplar_tests.md"
methodology:
  - "Second Method"
ai_assisted_by:
  - "GPT-5.6 Sol (conceptual synthesis and drafting)"
tags:
  - traceability
  - follow-the-money
  - follow-the-burden
  - accounting
  - acts
  - mandates
  - resources
  - effects
  - evidence
  - reconciliation
  - administrative-burden
  - cogentia
  - fractanet
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "explicit-metadata"
classification_confidence: "medium"
changelog:
  - "v0.2 (2026-08-14) — adds Follow the Burden as a first-class flow analysis and connects burden distribution to institutional friction."
  - "v0.1 (2026-08-14) — first crystallization of Follow the Money as a general traceability doctrine; introduces Reality-to-Ledger completeness, Ledger-to-Reality soundness, No Unaccounted Effects, and compensating reconciliation."
---

# Traceability of Flows and Effects

## 1. Purpose

"Follow the money" can be understood as one instance of a more general method: **follow the flows that make actions, constraints, incentives, capabilities, and effects materially observable**.

In a computational, organisational, economic, or political system, declared intentions alone are insufficient to describe what the system actually does. A stronger description follows the links between authority, action, resource use, observable effect, beneficiary, burden, and evidence.

A compact formulation is:

```text
Follow the Intent
-> Follow the Act
-> Follow the Mandate
-> Follow the Resource
-> Follow the Money
-> Follow the Beneficiary
-> Follow the Burden
-> Follow the Evidence
```

These are complementary projections over the same underlying history of acts and effects.

## 2. Accounting as a projection of the register of acts

Accounting is best viewed as a **specialized projection of the register of acts** whenever an act creates, consumes, transfers, reserves, destroys, or otherwise changes an accountable resource.

A generic act may be represented as:

```text
Act
 |- actor / principal
 |- mandate / authority
 |- time and context
 |- resources mobilized
 |- execution trace
 |- effects
 |- beneficiaries / affected entities
 |- burden created or transferred
 |- evidence
 `- accounting projection, when resources are affected
```

This suggests a general invariant:

> Every material act should produce an attributable, durable and auditable event. Every resource-affecting act should additionally produce an accounting event.

The accounting event is neither the act itself nor an optional report about it. It is one verifiable projection of the act's consequences on accountable resources.

## 3. From Follow the Money to Follow the Flows

Money is especially useful because financial flows can expose relationships that declarations do not: who finances, who receives, who bears costs, who captures benefits, and where incentives are located.

The same method applies to other scarce or consequential resources:

- money and financial claims;
- compute, tokens, GPU time, storage, bandwidth;
- energy;
- human time and attention;
- permissions and mandates;
- Kudos or other accounting units;
- physical assets and inventories;
- information and evidence where their movement is itself consequential;
- administrative, cognitive, documentary, and procedural burden.

The relevant question becomes:

> Which flows materially constrain or enable the system, and can they be traced back to attributable acts and forward to observable effects?

This matters for Cogentia and Fractanet because their relevant economy is not limited to currency. A Cognitive Packet may consume compute, invoke providers, reserve budgets, delegate capabilities, traverse nodes, create downstream effects, and impose human attention costs before a financial invoice exists.

## 4. The Reality <-> Ledger objective

Strict accounting requires two complementary properties.

### 4.1 Completeness — Reality -> Ledger

For every actually consumed, transferred, reserved, or otherwise affected accountable resource, there should be one attributable authoritative accounting trace, modulo explicitly modelled aggregation.

```text
real effect
-> execution
-> attribution
-> resource measurement
-> accounting event
-> durable persistence
```

A real accountable effect with no corresponding trace is an **orphan effect**.

### 4.2 Soundness — Ledger -> Reality

For every authoritative accounting entry, there should be evidence or an explicit justification connecting it to reality.

The justification may be an observed execution, provider usage record, physical measurement, contractual transaction, explicitly labelled estimate or provision, correction, reversal, projection, or consolidation.

An entry with no such basis is an **orphan ledger entry**.

### 4.3 Practical bijection

The target can be summarized as a practical:

```text
Reality <-> Ledger
```

This is an engineering objective rather than a claim that accounting can perfectly represent reality: differences between material effects and authoritative traces should be either prevented, explicitly provisional, or durably detectable and reconcilable.

## 5. No Unaccounted Effects

The strict form of the doctrine is:

> **No accountable effect without an attributable, durable and auditable event.**

And, more specifically:

> **No resource-affecting act without an accounting event.**

A critical corollary is:

> **Accounting failure must never silently disappear.**

This does not require every execution to synchronously stop when the authoritative ledger is temporarily unavailable. A system may use a durable degraded path, such as a local spool followed by replay, provided that the divergence is explicit, recoverable, observable, and cannot silently become permanent.

The invariant is that an accountable effect cannot become **silently unaccounted**.

## 6. Reconciliation without rewriting history

Initial accounting knowledge may be provisional. A model call can have a locally estimated cost before the provider publishes authoritative billing data. Energy, cloud, or network resources may likewise be measured first approximately and later precisely.

When better information arrives, the preferred rule is:

> **Do not rewrite a valid historical observation merely because a later observation is better. Record the difference explicitly.**

Example:

```text
provisional cost              1.23450000 USD
provider-confirmed cost       1.24170000 USD
reconciliation adjustment    +0.00720000 USD
```

The reconciliation event preserves both what the system knew at execution time and what later evidence established.

## 7. Verification by attempted bypass

Strict traceability should be verified from real effects back to their records, not only by inspecting the accounting module itself.

A useful audit path is:

```text
effect
-> call site
-> measurement
-> attribution
-> event
-> validation
-> persistence
-> projection
-> external truth
-> reconciliation
```

A practical acceptance test is:

> Try to consume one cent, one token, one compute unit, one unit of energy, or another accountable resource without the ledger recording or explicitly detecting the divergence.

The reverse test is equally important:

> Try to create an authoritative ledger entry for which no attributable act, evidence, estimate, correction, or projection can be found.

Together these tests operationalize completeness and soundness.

## 8. Follow the Burden

Burden should be treated as a first-class consequential flow, especially in institutional and human-facing systems.

A requirement can create work without directly transferring money. It may consume:

- human attention;
- learning time;
- document preparation;
- repeated data entry;
- correction effort;
- waiting time;
- emotional or psychological capacity;
- opportunity cost;
- professional assistance.

For each significant requirement or procedure, ask:

```text
Who creates the work?
Who performs it?
Who pays for it?
Who bears the cognitive load?
Who bears delay and error risk?
Who must justify the requirement?
Who saves work because another actor performs it?
Who benefits from keeping the arrangement unchanged?
```

This is **Follow the Burden**.

It allows asymmetry to be observed without presuming malicious intent. A procedure may be convenient for the institution precisely because it externalizes cost onto users. Whether that externalization is justified is a separate interpretive question.

A useful normative complement is **Burden Reinternalization**:

> **An entity that imposes a requirement should bear as much as reasonably possible of the informational, explanatory, and justificatory cost created by that requirement.**

This principle is developed further in Cogentia's `administrative_burden_and_exemplar_tests.md`.

## 9. Relation to Cogentia and Fractanet

Cogentia and Fractanet provide a concrete execution substrate on which this doctrine can be tested rather than merely asserted.

A representative chain is:

```text
mandate
-> Cognitive Packet
-> Fractanet hop
-> provider / runtime execution
-> measured resource usage
-> spending event
-> accounting transaction
-> durable event store or explicit spool
-> ledger projection
-> external provider truth
-> reconciliation
```

Human-facing workflows add another projection:

```text
requirement
-> burden creation
-> burden bearer
-> work performed
-> observable outcome
-> justification / challenge
```

The implementation-oriented accounting audit is tracked in:

- `JeanHuguesRobert/inseme#45` — **Strict Accounting / No Unaccounted Effects — adversarial audit and enforcement**.

This note preserves the broader conceptual invariant while the implementation evolves.

## 10. Broader interpretation

The doctrine extends beyond bookkeeping.

For governance, it asks whether power can be followed from mandate to act and effect. For distributed computation, it asks whether resource consumption and delegation can be followed across nodes and agents. For epistemic work, it asks whether conclusions can be followed back to observations, transformations, assumptions, and evidence. For institutional analysis, it asks who bears costs and burdens, who receives benefits, and which flows reveal the operational structure beneath declared purposes.

The recurring structure is:

```text
claim / mandate
-> act
-> flow
-> effect
-> beneficiary / burden bearer
-> evidence
-> correction
```

The deeper objective is not exhaustive observation of everything. It is **accountability at the points where acts create consequential effects or externalized burdens**.

## 11. Continuation

Potential later work:

1. connect this doctrine explicitly to the Corpus concepts of mandate, act register, Cognitive Packet, accounting event, burden, and evidence;
2. formalize the minimum invariant set in machine-checkable form;
3. distinguish authoritative events from projections, summaries, estimates, and reconciliations;
4. generalize the Follow-the-Money audit from financial units to heterogeneous resources and burdens;
5. study where strict traceability should deliberately stop for privacy, proportionality, autonomy, and cost reasons;
6. use implementation failures discovered by audits as case studies for the broader doctrine of verifiable action;
7. compare burden created by existing procedures with burden measured in Exemplar Tests.
