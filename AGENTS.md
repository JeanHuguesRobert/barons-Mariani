---
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/AGENTS.md
shared_instructions: https://github.com/JeanHuguesRobert/cogentia/blob/main/instructions/AGENTS.shared.md
last_stamped_at: 2026-07-13T00:00:00.000Z
last_modified_at: '2026-11-27'
document_role: operational
document_kind: agent-mandate
visibility: public
lifecycle_state: active
classification_source: cogentia.js
classification_version: '1'
classification_rule: agent-mandate
classification_confidence: strong
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
language: en
date: '2026-09-15'
update_policy: UP-DEFAULT-REVIEWED
status: working-paper
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: unknown
  origin_repository: unknown
  origin_ref: unknown
  origin_date: unknown
  derived_from: []
---


# AGENTS.md — Barons Mariani corpus mandate

This file gives operational instructions to AI agents and human assistants working in the `JeanHuguesRobert/barons-Mariani` repository.

It is not the full doctrine. It is a compact mandate for acting inside this repository without damaging the corpus.

## Shared baseline and read order

Before acting here:

1. read this repository-local `AGENTS.md`;
2. read the shared [`cogentia/AGENTS.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/AGENTS.md);
3. apply this local mandate wherever it is more specific or more restrictive;
4. consult the linked source doctrine when interpretation is needed.

The shared baseline supplies the default workflow. This high-authority corpus mandate narrows it where doctrine, legal or political positions, patrimony, or sensitive material are involved.

## Repository role

`barons-Mariani` is a source repository for long-form doctrine, patrimonial memory, public political/legal reasoning, historical work, and the Barons Mariani / Institut Mariani / C.O.R.S.I.C.A. corpus.

Treat it as a **high-authority corpus repository**.

It may contain:

- source documents;
- research notes;
- legal or quasi-legal analysis;
- public doctrine;
- historical/patrimonial material;
- products declined from source documents;
- sensitive family or institutional context.

## Core instruction

Before modifying this repository, distinguish:

```text
fact
hypothesis
interpretation
public formulation
legal/political position
element to verify
source document
derived / declined product
temporary trace
```

Do not collapse these categories.

## JHN sub-agent routing gate

When an Agent JHN delegates work to a sub-agent, apply
[`agents-jhn/charte_agents_jhn.md`](agents-jhn/charte_agents_jhn.md), especially
the operational-parent and double-gatekeeper rule.

Every JHN sub-agent MUST:

- declare a `parent_agent_id`;
- return results and action requests to that parent;
- use `external_action_route: parent_only` and `budget_route: parent_only`;
- never send externally, publish, commit, push, merge, deploy, spend, create
  accounts, access payment means, or spawn further sub-agents directly.

The parent Agent JHN may reject, correct, or route a request. It MUST NOT treat
its own approval as human authorization. Editorial acts remain routed through the parent under the standing mandate; doctrinal promotion and engaging acts still require the applicable explicit authorization of Jean Hugues Robert.

A technically available direct channel is not an authorized channel. Any direct
external action by a JHN sub-agent is a mandate incident: stop the action,
preserve the trace, suspend the capability, and request human review.

## Corpus-wide rule

Apply the Cogentia Agent Configuration Layer:

```text
AGENTS.md is an operational projection, not the corpus itself.
The corpus remains the source of truth.
Human authorization governs doctrinal promotion and external commitments; faithful editorial stabilization is covered by the standing public-Corpus mandate.
```

References:

- [`cogentia/AGENTS.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/AGENTS.md)
- [`cogentia/research/agent_configuration_layer.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_configuration_layer.md)
- [`cogentia/research/optimistic_mainline_governance.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/optimistic_mainline_governance.md)

## Direct-main rule

This repository follows **Optimistic Mainline Governance** by reference, not by copying the doctrine here.

Small direct commits to `main` are acceptable under the standing editorial mandate or a specific authorization, when scoped, reversible, inspectable by diff, and reported after completion.

Do not create a branch or PR by default. Use one only when explicit instruction, collaboration, repository protection, high risk, or genuine isolation value justifies it.

Because this is a high-authority corpus repository, preserve the distinction between editorial work and doctrinal promotion, legal/political decisions, sensitive material, accusations and institutional commitments. Seek the appropriate substantive arbitration or specific authorization for the latter, not for mere proximity to a doctrinal document or because several documents must be synchronized. Use an issue, checkpoint, branch, PR or staged patch only when it serves a concrete need.

## Working discipline

Use the smallest sufficient container:

```text
conversation -> exploration
issue        -> memory in tension
draft        -> proposed formulation
source file  -> stabilized corpus element
derived text -> public-facing product
commit       -> durable trace
```

**This sequence describes the level and role of stabilization; it is not a boundary of Corpus membership.** A GitHub Issue, and materially relevant comments on it, are integral parts of the Corpus when they carry work, objections, continuations, decisions, observations, provenance, or other relevant traces. They may function as memory in tension, trace-bearing work loci, or Cognitive Packet/Capsule projections while remaining provisional and non-canonical.

Therefore distinguish explicitly:

```text
belongs to the Corpus
≠ stabilized source document
≠ canonical doctrine
≠ established fact
```

Creating or updating a public Issue or materially relevant Issue comment changes the Corpus even when no Git-tracked source file changes. When reporting such work, do not say that "the Corpus was not modified"; say instead, for example, **"the Corpus changed at the Issue/trace layer; no stabilized source file was modified."**

When modifying a research document, preserve or add, when useful:

- status;
- date;
- author;
- repository/path;
- source/derived distinction;
- level of certainty;
- continuations;
- objections or verification needs.

## Sensitive material

Stop and require explicit scoped authorization before changing or publishing material involving:

- Marie-Louise / Malou;
- succession, testament, family conflict, or legal facts;
- names of private persons not already public in the document;
- institutional commitments;
- political candidacy documents;
- legal positions that could be used externally;
- accusations or imputations of wrongdoing.

Do not intensify a claim without evidence.

## Public writing rule

For texts intended for Facebook, do not use markdown syntax. Use plain text. Unicode bold may be used sparingly when useful.

For GitHub research documents, markdown is appropriate.

## GitHub write and publication gate

**Principal decision, 2026-11-27:** the standing [public-Corpus editorial mandate](https://github.com/JeanHuguesRobert/cogentia/blob/main/instructions/AGENTS.policy-effects.md#standing-public-corpus-editorial-mandate--principal-decision-2026-11-27) applies to this repository. Agents may perform and publish ordinary corrections, research enrichments, attributed hypotheses, conceptual connections, synchronization and faithful propagations on public Corpus sources, including commits and pushes on `main`, within the effective mandate and authorized execution route. No additional permission is required merely because a new file or several files are involved. Preserve attribution, status, visibility, optimistic locking and traceability. A public branch, commit, issue, comment or draft PR is publication; it is not a confidentiality mechanism.

**Doctrinal sovereignty:** apply the [shared doctrinal arbitration rule](https://github.com/JeanHuguesRobert/cogentia/blob/main/instructions/AGENTS.policy-epistemics.md#doctrinal-promotion-and-editorial-autonomy--principal-decision-2026-11-27). Any new doctrinal promotion belongs to the Principal. Whenever doubt arises about the doctrinal nature or scope of a change, ask the Principal to clarify its meaning or attribution before promoting it. A validated decision may be faithfully propagated without another per-file approval. The inclusion of attributed research in a doctrinal document does not make it the Principal's adopted position.

Outside the standing editorial mandate, GitHub writes require the applicable explicit, scoped authorization. Approval of an idea or a generic "ok" alone does not authorize an otherwise unmandated act. Before a write requiring specific approval, identify the repository, branch or target, affected files or objects, operation and visibility consequence; act only within the authorization. The standing mandate does not cover sensitive material identified above, new legal/political commitments, changes of visibility, authority or mandates, external communications, or deployment. Preserve the sub-agent routing constraints and all independent provider/account controls.

## Language gate for new source documents

The language of the conversation MUST NOT automatically determine the normative language of a new source document.

Before drafting a new source document, the agent MUST determine or explicitly confirm the intended language using, in order:

1. an explicit user instruction;
2. the language of the canonical source lineage and adjacent load-bearing documents;
3. the repository's established architectural convention;
4. a direct clarification when the choice remains materially ambiguous.

A translation is a separate derivative unless the user explicitly adopts it as the new canonical source.

## Validation

Before presenting work as ready, report:

```text
Scope:
Files changed:
Source/derived status:
Facts checked:
Hypotheses marked:
Known risks:
Reversibility:
Next step:
Human validation needed: yes/no
```

If no external verification was performed, say so.

## Authorization rule

Agents may prepare, draft, summarize, route, compare, and propose.

Agents may commit, push and publish public-Corpus editorial work within the standing mandate above. Outside it, agents must obtain the applicable explicit, scoped authorization for consequential acts, including sending, signing, spending, new commitments and doctrinal promotion. Where doctrinal effect is in doubt, ask the substantive question; where authority is in doubt, prepare the affected operation and clarify its scope. Continue independent authorized work.


## ⛔ INTERDICTION ABSOLUE D'ENVOYER DES COURRIELS SANS VALIDATION EXPRESSE

**Règle impérative de Jean Hugues Noël Robert (9 octobre 2026).** Tout agent travaillant pour ce Corpus **N'EST PAS AUTORISÉ À ENVOYER** des courriels ou autres messages sortants en son nom, même lorsqu'une instruction générale demande « envoyer des mails », « contacter », « relancer » ou « faire les démarches ». **Le mandat ordinaire se limite à préparer des BROUILLONS (drafts) et à les SOUMETTRE à l'utilisateur pour relecture et décision.**

- **INTERDIT PAR DÉFAUT :** `send_email`, `send_draft`, réponses, transferts, campagnes d'envoi, relances automatisées ou tout outil équivalent qui expédie effectivement un message.
- **AUTORISÉ :** rédiger le texte, créer un brouillon non envoyé, fournir destinataires vérifiés, objet, pièces et URL, puis présenter ce brouillon à l'utilisateur.
- **Exception éventuelle :** seulement si l'utilisateur donne **une autorisation explicite, spécifique et actuelle d'expédier le ou les messages déterminés**, après présentation des brouillons. Une demande générale de lancement d'un projet ou un ancien accord n'est PAS une autorisation d'envoi.
- La création d'un brouillon ne vaut **jamais** envoi. Dans tous les journaux, distinguer `DRAFT_CREATED`, `SUBMITTED_FOR_REVIEW`, `APPROVED_FOR_SENDING` et `SENT` sur preuves distinctes.
- **Incident documenté le 9 octobre 2026 :** deux messages envoyés par erreur aux Archives de Corse Pumonti et Cismonte sans validation préalable ; ne pas réitérer.

## Editorial register: analysis versus political speech

When drafting for this corpus, distinguish academic analysis, legal notes and evidence audits from expressly attributed political speeches, manifestos and opinion chronicles. In analytic work, disclose uncertainty, objections and limits in the body as appropriate. In political writing, **do not reflexively dilute the author's normative claims with repetitive methodological qualifiers**; preserve the intended force and voice, and route supporting qualifications to citations or annexes when suitable. This does **not** permit fabricating facts, concealing material contradictions, attributing unverified motives or describing predictions as proven outcomes. Keep the same factual standard across registers. Political conflict in the Campagnes du Réel is strictly nonviolent and documentary; external communications require the principal's specific authorization. See [Capable editorial guidance](projects/capable/AGENTS.md).


## Living Books: common editorial architecture

The canonical cross-project definition is [research/livre_vivant.md](research/livre_vivant.md). Apply its separation of **Book** (durable readable work), **Book annexes** (evidence, sources, objections) and **Magazine** (dated changes and interventions) across all Living Books, not only Capable. Preserve traceable corrections between editions: working candidates may change, frozen editions remain identifiable, and later issues may publish errata or substantive revisions with clear provenance. Maintain the same standard of factual accuracy in analytic and expressive genres, without mechanically weakening attributed political or opinion writing. Do not duplicate the canonical doctrine in each project's local instructions.

