---
title: "Corpus Status — barons-Mariani"
description: "Current state of the barons-Mariani knowledge corpus — what is proved, what is open, what remains possible"
layout: default
nav_order: 2
last_modified_at: 2026-05-16
repository: "github.com/JeanHuguesRobert/barons-Mariani"
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/corpus-status.md
last_stamped_at: 2026-05-16
---

# Corpus Status — barons-Mariani

*Auto-refreshed by `cogentia.js corpus-status`. The structural sections —*
*Registered Repositories, Cross-Reference Graph, Published, What Remains Possible —*
*are regenerated from the registry and from `research/index.md` on every run.*
*The substantive sections — What Is Proved and Open Objections —*
*are manually curated and preserved across refreshes.*

---

## Registered Repositories

<!-- BEGIN_AUTO: registered_repos -->
| Repository | research/index.md | Branch | Last commit |
|---|---|---|---|
| cogentia | ✅ | main | 2026-05-15 |
| FractaVolta | ✅ | main | 2026-05-15 |
| marenostrum | ✅ | main | 2026-05-15 |
| barons-Mariani | ✅ | main | 2026-05-15 |
| inseme | ✅ | main | 2026-05-15 |
<!-- END_AUTO: registered_repos -->

---

## Cross-Reference Graph

<!-- BEGIN_AUTO: graph -->
```mermaid
graph LR
  cogentia["📄 cogentia"]
  FractaVolta["📄 FractaVolta"]
  marenostrum["📄 marenostrum"]
  barons-Mariani["📄 barons-Mariani"]
  inseme["📄 inseme"]
  cogentia --> marenostrum
  cogentia --> barons-Mariani
  cogentia --> FractaVolta
  cogentia --> inseme
  FractaVolta --> marenostrum
  FractaVolta --> barons-Mariani
  FractaVolta --> cogentia
  FractaVolta --> inseme
  marenostrum --> barons-Mariani
  marenostrum --> FractaVolta
  marenostrum --> cogentia
  marenostrum --> inseme
  barons-Mariani --> marenostrum
  barons-Mariani --> FractaVolta
  barons-Mariani --> cogentia
  barons-Mariani --> inseme
  inseme --> cogentia
  inseme --> marenostrum
  inseme --> FractaVolta
  inseme --> barons-Mariani
```
<!-- END_AUTO: graph -->

---

## Concepts

<!-- BEGIN_AUTO: concepts -->
| Concept | Scope | Status | Type |
|---|---|---|---|
| [Cogentia](./concepts.md#cogentia) | Global | Working | abstract concept / agentivity class |
| [Cogentigram](./concepts.md#cogentigram) | Global | Working | representation / map |
| [Potentics](./concepts.md#potentics) | Global | Defined | philosophy |
| [Cognitive Waves](./concepts.md#cognitive-waves) | Global | Working | sociological concept |
| [Mimetic Desynchronization](./concepts.md#mimetic-desynchronization) | Global | Defined | systemic intervention |
| [Invidia](./concepts.md#invidia) | Global | Working | abstract concept |
| [Transition Markets](./concepts.md#transition-markets) | Global | Working | economic model |
| [The Uchronian Museum](./concepts.md#the-uchronian-museum) | Global | Seed | project / concept |
| [Possibilism](./concepts.md#possibilism) | Global | Canonical | ideology |
| [Territoires Possibilistes](./concepts.md#territoires-possibilistes) | project-specific | Working | political framework |
| [The Second Method](./concepts.md#the-second-method) | repository-specific | Canonical | epistemological framework |
| [Projet Minesteggio](./concepts.md#projet-minesteggio) | project-specific | Working | cultural initiative |
| [Discret Holography](./concepts.md#discret-holography) | repository-specific | Seed | conceptual joke |
<!-- END_AUTO: concepts -->

## Concept Graph

<!-- BEGIN_AUTO: concept_graph -->
```mermaid
graph LR
  c_cogentia["Cogentia"]
  c_cogentigram["Cogentigram"]
  c_continuation_protocol["Continuation Protocol"]
  c_cogentia_commons["Cogentia Commons"]
  c_sovereign_digital_twin["Sovereign Digital Twin"]
  c_agent_resumable_cli["Agent-Resumable CLI"]
  c_kernel_extractor["Kernel Extractor"]
  c_kys_know_your_system_psychocognitive_analysis["KYS (Know Your System) / Psychocognitive Analysis"]
  c_cogentia_workflows["Cogentia Workflows"]
  c_cogentia["Cogentia"]
  c_cogentigram["Cogentigram"]
  c_ipn_inference_packet_network["IPN (Inference Packet Network)"]
  c_epn_energy_packet_network["EPN (Energy Packet Network)"]
  c_pgn_power_generation_node["PGN (Power Generation Node)"]
  c_packet_attractors["Packet Attractors"]
  c_the_unconscious_grid["The Unconscious Grid"]
  c_mariani_village["Mariani Village"]
  c_value_shaped_solar["Value-Shaped Solar"]
  c_containerized_compute_tera["Containerized Compute (Tera)"]
  c_traceable_governance["Traceable Governance"]
  c_cogentia["Cogentia"]
  c_cogentigram["Cogentigram"]
  c_dhitl_democratic_human_in_the_loop["DHITL (Democratic Human In The Loop)"]
  c_cxu_compute_and_exergy_unit["CXU (Compute and Exergy Unit)"]
  c_safe_compute_exergy["Safe Compute Exergy"]
  c_constellia["Constellia"]
  c_corsica_forest_synergies["Corsica Forest Synergies"]
  c_infrastructure_is_all_you_need["Infrastructure is All You Need"]
  c_sun_to_sovereignty["Sun to Sovereignty"]
  c_cogentia["Cogentia"]
  c_cogentigram["Cogentigram"]
  c_potentics["Potentics"]
  c_cognitive_waves["Cognitive Waves"]
  c_mimetic_desynchronization["Mimetic Desynchronization"]
  c_invidia["Invidia"]
  c_transition_markets["Transition Markets"]
  c_the_uchronian_museum["The Uchronian Museum"]
  c_possibilism["Possibilism"]
  c_territoires_possibilistes["Territoires Possibilistes"]
  c_the_second_method["The Second Method"]
  c_projet_minesteggio["Projet Minesteggio"]
  c_discret_holography["Discret Holography"]
  c_cogentia["Cogentia"]
  c_cogentigram["Cogentigram"]
  c_cop_continuous_operation_protocol["COP (Continuous Operation Protocol)"]
  c_briques["Briques"]
  c_kudocracy["Kudocracy"]
  c_agora["Agora"]
  c_ophelia["Ophélia"]
  c_cop_invariants["COP Invariants"]
  c_brique_spec_multi_instance["Brique Spec / Multi-Instance"]
  c_modular_system["Modular System"]
  c_traceable_agency["traceable agency"]
  c_traceable_agency --> c_cogentia
  c_cogentia --> c_cogentigram
  c_operational_memory["operational memory"]
  c_cogentia --> c_operational_memory
  c_map_vs_territory["map vs territory"]
  c_cogentigram -.-> c_map_vs_territory
  c_cogentigram -.-> c_operational_memory
  c_cogentigram -.-> c_traceable_agency
  c_agent_resumable_cli --> c_continuation_protocol
  c_dhitl["dhitl"]
  c_dhitl --> c_infrastructure_is_all_you_need
```
<!-- END_AUTO: concept_graph -->

---

## Published in this repo

<!-- BEGIN_AUTO: published -->
| Title | Location | Date |
|---|---|---|
| [Discours de la seconde méthode](second_method.md) *(founding methodological doctrine — v1.0)* | this repo | 2026-05-08 |
| [Invidia — envie et désir mimétique](../invidia.md) | this repo | 2026 |
| [Indirect Action Under Mimetic Constraints](../mimetic_desynchronization.md) | this repo | 2026 |
| [Toy Story, AI, and Mimetic Desynchronization — Cultural Strategy for Cognitive Transition](../toy_story.md) *(v6.0)* | this repo | 2026-05-11 |
| [VIGILIA — Distributed avoidance, signalling, and territorial perception (FR)](../vigilia.md) *(v1.3)* | this repo | 2026-05-12 |
| [The Generalized Tocqueville Law — Progress, Rising Expectations, Structural Dissatisfaction](../tocqueville_law.md) | this repo | 2026 |
| [The Republic of Donkeys — A Situated Micro-Experiment in Commons Governance](../the_republic_of_donkeys.md) *(v2.0)* | this repo | 2026 |
| [Markets of Usage Transitions in Multi-Use Physical Assets](../transition_markets.md) | this repo | 2026 |
| [Terrain Configuration Theory for Democratic AI Infrastructure](../terrain_configuration.md) | this repo | 2026 |
| [Possibilism — Notes Toward a Research Program](../possibilism_04_2026.md) | this repo | 2026-04 |
| [Territoires possibilistes — Autonomie alimentaire, diversité épistémique et innovation durable (FR)](territoires_possibilistes.md) | this repo | 2026 |
| [Le Musée uchronique comme dispositif d'inférence historique (FR)](../uchronian_museum.md) | this repo | 2026 |
| [Projet Minesteggio — Fondation Barons Mariani / Musée Uchronique « Napoléon 1821 » (FR)](../projet_minesteggio.md) | this repo | 2026 |
| [Literary Works as Navigable Spaces — AI-Based Cultural Mediation](../ai-based-cultural-mediation.md) | this repo | 2026 |
| [Architecture de l'univers-automate — résolution systémique 2D-4D (FR)](../discret_holography.md) | this repo | 2026-02-27 |
| [Sailing the Cognitive Waves — Stigmergic Cognitive-Terrain Framework](cognitive_waves.md) | this repo | 2026 |
| [Potentics — Toward a Science of the Possible](potentics.md) | this repo | 2026 |
| [Protection responsable](../protection_responsable.md) | this repo | 2026 |
| [Corpus Status](corpus-status.md) *(living view — auto-refreshed by `cogentia.js corpus-status`)* | this repo | refreshable |
| [Concept Index](concepts.md) *(typed concept registry — mapped by `cogentia.js concepts`)* | this repo | refreshable |
<!-- END_AUTO: published -->

---

## What Is Proved

*Manually curated: claims demonstrated by the published work in this corpus.*

| Claim | Status | Evidence |
|---|---|---|
| Public corpus improves via objection integration | ✅ Demonstrated | v0.1→v1.0 git history of `second_method.md`, multiple public AI reviews integrated |
| Machine-readable structure does not degrade human readability | 🔄 In progress | `research/index.md` network navigable; `cogentia.js graph` renders Mermaid |
| Rule 0 boundary documented | ✅ Documented | [DHITL.md Layer 3 / Layer 4 boundary](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) |
| Rule 0 boundary implemented | ❌ Open research problem | No complete technical specification yet |
| Mimetic-desynchronization theory of structural change | ✅ Published | [`mimetic_desynchronization.md`](../mimetic_desynchronization.md) — DRSJ cycle + six mechanisms |
| Generalized Tocqueville Law | ✅ Published | [`tocqueville_law.md`](../tocqueville_law.md) |
| Possibilism research program | ✅ Published | [`possibilism_04_2026.md`](../possibilism_04_2026.md), [`research/potentics.md`](potentics.md) |

---

## Open Objections

*Manually curated: objections received publicly, not yet fully resolved.*

| Objection | Source | Status |
|---|---|---|
| Rule 0 has no complete technical implementation | Grok (v0.4–v0.9 review) | 🔄 Named, partially documented, unresolved |
| MareNostrum chiffres need independent verification | Grok (v0.4–v0.9 review) | 🔄 Documented in repo, awaiting external audit |
| Corpus is solo — fractal claim unproven at scale | Grok (v0.4–v0.9 review) | ❌ Known structural limit — invitation to fork open |
| Claim 4 (transparent infra = AI safety) lacks case study | Grok (v0.7–v0.9 review) | ❌ Weakest claim — empirical test pending |

---

## What Remains Possible

<!-- BEGIN_AUTO: possibilities -->
- Uchronian museology — the Mariani public museum as institutional form
- Casabianca family archive — collateral descent, Battle of Aboukir 1798, WWII submarine
- Generalized Tocqueville Law — formal treatment beyond the aphorism
- Invidia × Ostrom: commons governance as antidote to mimetic capture
<!-- END_AUTO: possibilities -->

---

*Generated with `cogentia.js corpus-status` — [scripts/cogentia.js](https://github.com/JeanHuguesRobert/cogentia/blob/main/scripts/cogentia.js)*
*Challenge via issues. Fork to explore alternatives.*


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Corpus Status — barons-Mariani](corpus-status.md)
- [Research Index — barons-Mariani](index.md)
- [Discours de la seconde méthode](second_method.md)

<!-- END_AUTO: backlinks -->
