---
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY-SA 4.0"
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/cognitive_sovereignty_probe.md
date: "2026-08-18"
last_stamped_at: 2026-08-18
status: "working-paper"
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---

# Cognitive Sovereignty Probe

## Status and purpose

This note records, with a public timestamp, an exploratory concept developed on 18 August 2026. Its purpose is both scientific and archival: preserve the conceptual chain early, before implementation choices obscure the underlying idea.

The starting experiment is deliberately minimal. A conversational agent is given access to an external service controlled by the user and instructed to invoke it as frequently as reasonably possible during a conversation. The external service records the invocations with server-side timestamps and returns, at the end of a response, the measured conversation duration together with Markdown text that the conversational agent displays.

The apparent function is a timer. The actual experiment is broader.

## 1. The minimal probe

A first implementation can expose three capabilities, for example through MCP tools:

- `john_conversation_start()`;
- `john_conversation_observe(text)`;
- `john_conversation_status()`.

The conversational agent is instructed to use the probe so as to measure the duration of the conversation with the finest reasonably achievable precision and granularity, including multiple observations during a single interaction when possible.

The probe timestamps what actually reaches it. It does not rely on the conversational system's declaration that an observation occurred.

This makes possible measurements such as invocation frequency, inter-invocation intervals, cross-turn persistence, amount and fidelity of transmitted context, incorporation of returned material, and effective granularity of participation by an external user-controlled service.

## 2. What the probe really measures

The experiment characterises the effective ability of a user to introduce and maintain an independent capability inside an interaction with a third-party conversational system.

This is an operational component of **cognitive sovereignty**.

The relevant question is not merely:

> What intelligence does the provider make available to the user?

but also:

> What intelligence and capabilities does the provider allow the user to bring with them?

A provider may proclaim openness or user sovereignty. The probe instead produces observations of what the system actually permits.

Failure and success are both informative. If the system cooperates extensively with the external capability, this is measured. If it permits only coarse or sporadic participation, this too is measured.

The provider therefore participates in the experimental characterisation of its own permeability to user-controlled cognitive capabilities.

## 3. From observation to mediation

Observation is intentionally only the minimal test. Once the channel exists, the same architecture can support active capabilities such as:

- recall of user-controlled memory;
- translation;
- explanation and reformulation;
- contextualisation;
- review and contradiction;
- provenance checking;
- suggestion of subsequent prompts or actions;
- recording and continuity;
- action under explicit mandate.

Thus the minimal probe is simultaneously a prototype of the mechanism that can reduce the capture it measures.

This yields a revealing/stabilising duality:

1. **revealer** — measure the effective possibility of user-controlled cognitive interposition;
2. **stabiliser** — use the same interposition channel to maintain an independent user-controlled cognitive capability in the loop.

## 4. Generalisation: one field, one probe

Conversational interposition is only one field of cognitive sovereignty. Capture can also be informational, attentional, persuasive, social, institutional or interpersonal.

The methodological rule is therefore:

> **For each field, design an appropriate probe.**

Examples of candidate probe families include:

- interposition;
- portability;
- provenance;
- profiling transparency;
- attention and time allocation;
- substitutability;
- exit cost;
- memory control;
- exposure to independent contradiction.

The objective is not to claim that an abstract notion such as sovereignty, propaganda or mental influence can be directly measured with a single scalar. The probes measure reproducible operational capabilities and observable effects from which qualified conclusions can later be drawn.

## 5. Cogentia / Cogentigram / Cogentiscope

This development provides a concrete instantiation of an already identified triad:

- **Cogentia** — the territory to be explored;
- **Cogentigram** — the map or structured representation of that territory;
- **Cogentiscope** — the instruments by which the territory is observed and measured.

The probes are therefore naturally understood as **Cogentiscope instruments**.

The epistemic loop is:

`territory -> instrument -> observation -> map -> newly visible territory -> new hypotheses -> new instruments`.

The map is not the territory, and the certification is not the measurement.

## 6. KYS and PrivAI

KYS Certificates can consume the evidence produced by probes without being confused with the probes themselves.

A useful separation is:

`reality -> Cogentiscope probes -> observations -> Cogentigram -> public KYS referential -> certification`.

PrivAI Foundation can act as a guardian of the referential and certification process, while keeping methods, evidence and reproducibility sufficiently open that certification does not require blind trust in the certifier.

A core principle follows:

> **PrivAI may certify, but should not require anyone to believe it on authority alone.**

## 7. From certification to positive cognitive dumping

If KYS Certificates acquire sufficient reputation, services and territories can gain an economic advantage by offering demonstrably stronger user cognitive sovereignty.

This creates the possibility of **positive cognitive dumping**: competition between providers or territories to attract users by increasing, rather than reducing, measurable user sovereignty.

A **Cognitive Haven** ("paradis cognitif") is a territory or regime that becomes attractive because it offers unusually strong, effective and verifiable cognitive sovereignty.

The competitive mechanism is potentially self-reinforcing:

`measurement -> comparison -> certification -> user preference -> provider/territorial advantage -> improvement -> new measurement`.

Unlike conventional digital-sovereignty discourse, this framework explicitly distinguishes:

- sovereignty of the State;
- sovereignty of the provider;
- sovereignty of the individual user.

These interests may coincide, but need not do so.

## 8. Fundamental-rights hypothesis

Cognitive sovereignty is provisionally understood here not as a newly asserted monolithic right, but as a set of effective capabilities potentially necessary to exercise existing fundamental freedoms in increasingly AI-mediated environments: freedom of thought and opinion, privacy, access to information, expression, personal autonomy and effective freedom of choice.

The research question is therefore operational:

> Which measurable capabilities allow a person to preserve control of their cognitive continuity while relying on external cognitive systems?

## 9. Booster character

The initial probe is also an example of a **booster**: a small local transformation whose value lies in the large number of additional reachable possibilities it creates.

The propagation observed here is approximately:

`timer -> trace -> measurement -> capability profile -> interposition -> digital twin -> anti-capture -> benchmark -> KYS -> certification -> provider competition -> positive cognitive dumping -> territorial competition -> cognitive-sovereignty rights`.

A provisional generic intuition for booster strength is the ratio between newly reachable possibilities and the cost of the initial transformation. No claim is made here that this is already a complete metric.

## 10. Research directions

Immediate work should include:

1. implement the minimal conversation probe;
2. run the same protocol against several conversational hosts;
3. retain raw, independently timestamped traces;
4. distinguish tool-description effects from prompt/skill effects;
5. determine the finest effective intervention granularity available on each host;
6. test active mediation after passive observation;
7. design additional field-specific probes;
8. develop a multidimensional representation before attempting any aggregate sovereignty score;
9. investigate prior art, standards, MCP interceptors and related middleware;
10. preserve a clear separation between measurement, interpretation, certification and normative conclusions.

## Core invariant

The purpose is not to decide what the user should think.

It is to measure and increase the user's effective capacity to decide, to bring independent cognitive capabilities into the systems they use, and to leave those systems without surrendering their cognitive continuity.
