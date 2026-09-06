---
title: "Presencology Addendum — Digital, Social and Institutional Presence of Twins"
date: "2026-09-06"
version: "0.1"
license: "CC BY-SA 4.0"
document_role: "source-addendum"
document_kind: "research-note"
visibility: "public"
repository: "JeanHuguesRobert/barons-Mariani"
canonical_path: "research/presencology_digital_social_presence_twins.md"
status: "working"
lifecycle_state: "working"
related:
  - research/presencology.md
  - "JeanHuguesRobert/inseme:research/interactions_registry_and_multichannel_messaging.md"
  - "JeanHuguesRobert/inseme:research/activitypub_edge.md"
  - "JeanHuguesRobert/inseme:docs/oleole-mvp-spec.md"
---

# Presencology Addendum — Digital, Social and Institutional Presence of Twins

## 1. Purpose

This note makes explicit an implication already latent in Presencology: **humans, software agents, Personal Digital Twins, Collective Digital Twins and institutions can have Presence in non-geographic spaces**, including digital, social, technical and institutional spaces.

It does not introduce a second definition of Presence. It applies the existing abstraction:

```text
Presence(subject, space, time, modality)
```

where the subject may be a human, agent, Twin or collective, and the space may be physical, digital, social, technical, institutional, political, computational or conceptual.

## 2. Digital and social spaces

Examples of spaces include:

- a Discord guild, channel or thread;
- a GitHub repository, issue or discussion;
- an ActivityPub community or federated actor neighbourhood;
- an X/Twitter conversation or community;
- a mailing list or email thread;
- a web-chat room;
- a formal institution or working group;
- a conceptual or computational search space.

A Twin participating in such a space therefore has a qualified Presence there. This Presence is distinct from the external account, handle or transport identifier through which it is manifested.

```text
Twin identity != platform account
Presence != account binding
```

A platform-specific identifier is evidence or a binding associated with a Presence; it is not the sovereign identity of the Twin.

## 3. Presence does not imply authority

The following distinctions are constitutive:

```text
Presence != membership
Presence != capability
Presence != permission
Presence != mandate
Presence != authority
Presence != activity
```

For example, the fact that Agent John is present in a Discord server does not imply that John may publish there, and even a technical permission to publish does not imply a Cogentia mandate to speak on behalf of Jean Hugues Robert or of a Collective Twin.

A useful operational decomposition is:

```text
Presence
  -> where the subject is represented or active

Capability
  -> what actions are technically possible

External permission
  -> what the platform or host allows

Mandate
  -> what Cogentia authorises under the Principal's or collective's authority

Act
  -> what was actually done, with provenance and causal trace
```

## 4. Control and governance regimes

The same Presence mechanism applies whether the surrounding space is controlled by the Twin or by others. What changes is the governance relation between subject and space.

Two important cases are:

### 4.1 Presence in an externally governed space

A Personal or Collective Twin may participate in a Discord server, GitHub project, mailing list, forum or other space whose rules and moderation are controlled by third parties.

The Twin is then a guest or delegated participant. External rules, platform permissions and local moderation remain independent from Cogentia mandates.

### 4.2 Presence in a Twin-governed space

A Personal or, more commonly, Collective Twin may operate an optional Discord server or analogous communication space for users who prefer that surface.

The space can project some of the collective's structures, conversations and activities, but it does not become the canonical memory, identity store, mandate system or decision system of the Twin.

```text
Discord role != Cogentia role
Discord permission != Cogentia mandate
Discord poll != institutional decision
Discord member != civic or institutional member
```

The external platform remains a surface or projection even when the Twin substantially governs its use.

## 5. Relation to Olé Olé

Olé Olé operationalises Presencology primarily in territorial space: current and future PresenceClaims, PresencePolicy, PresenceIntent and a FractaTerritorialContext projection.

The same structural logic can be reused in digital and social spaces without forcing territorial semantics into Cogentia's generic core.

```text
Territorial Presence
  -> Olé Olé / FractaTerritorialContext

Digital/social Presence
  -> Discord, GitHub, ActivityPub, email, web chat, etc.

Generic Presence abstraction
  -> Presencology
```

This preserves the existing architectural boundary: domain services own their domain semantics; Cogentia may provide reusable identity, context, mandate, packet, trace and continuation mechanisms.

## 6. Interaction and continuity

Presence in a communication space must not be confused with the durable Conversation or Interaction Packet.

A Discord thread, GitHub issue, email thread or chat session can be one external projection or binding of a longer-lived Cogentia Conversation. The logical conversation may survive provider change, channel change, account change, device change or disappearance of the external thread.

Consequential exchanges may therefore be converted into or linked to Interaction Packets and COP events while ephemeral exchanges remain ephemeral.

```text
external message/thread
  -> evidence / interaction event
  -> optional Interaction Packet
  -> continuation
  -> possible resumption on another channel
```

## 7. Presence and context projections

Olé Olé's FractaTerritorialContext suggests a broader reusable pattern: a context is a bounded projection over source-owned claims and facts relevant to a subject, space, time and policy scope. The projection must not become the canonical owner of all underlying data.

For digital spaces, a Twin may therefore maintain temporary or derived views of:

- where it is present;
- which actors are present nearby in the relevant topology;
- which conversations are active;
- what permissions and external rules apply;
- what mandates are currently applicable;
- which continuations or obligations are pending.

Such a view is not necessarily a new canonical object type. It may remain an implementation-specific projection over PresenceClaims, bindings, Interaction Packets, COP events and external platform state.

## 8. Discord as first concrete non-territorial case

Discord is a useful first implementation case because it exposes both major regimes with nearly identical mechanics:

1. **external participation** — a Twin is present in Discord spaces governed by others;
2. **hosted community space** — a Personal or Collective Twin offers Discord as an optional interaction surface for its users.

The common adapter should therefore model bindings, Presence, ingress/egress, provenance, external permissions, disclosure, Interaction Packets and COP mandates independently of the control regime.

A future Discord implementation should be an edge/surface, not a second source of truth:

```text
Discord
  <-> Discord edge/adapter
  <-> Presence + Interaction Packets + COP
  <-> Personal or Collective Twin
```

## 9. Research consequence

This application strengthens a general Presencology hypothesis: **Presence Maps are relevant not only to physical populations and exploratory agents, but also to the distribution of humans, agents, Twins and institutions across digital, social and institutional spaces.**

That extension should be tested rather than assumed. Discord provides a practical testbed because the same subject can simultaneously hold multiple presences across external and self-governed spaces while retaining one identity, memory, mandate framework and continuation space.
