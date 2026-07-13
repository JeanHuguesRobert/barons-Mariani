---
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/AGENTS.md
last_stamped_at: 2026-07-13
document_role: "operational"
document_kind: "agent-mandate"
visibility: "public"
lifecycle_state: "active"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "agent-mandate"
classification_confidence: "strong"
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

## Corpus-wide rule

Apply the Cogentia Agent Configuration Layer:

```text
AGENTS.md is an operational projection, not the corpus itself.
The corpus remains the source of truth.
Human authorization governs stabilization.
```

References:

- [`cogentia/AGENTS.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/AGENTS.md)
- [`cogentia/research/agent_configuration_layer.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/agent_configuration_layer.md)
- [`cogentia/research/optimistic_mainline_governance.md`](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/optimistic_mainline_governance.md)

## Direct-main rule

This repository follows **Optimistic Mainline Governance** by reference, not by copying the doctrine here.

Small direct commits to `main` are acceptable only when explicitly authorized, scoped, reversible, inspectable by diff, and reported after completion.

Do not create a branch or PR by default. Use one only when explicit instruction, collaboration, repository protection, high risk, or genuine isolation value justifies it.

Because this is a high-authority corpus repository, direct-main work must remain more conservative than in implementation repositories. Use an issue, checkpoint, branch, PR, staged patch or human validation when a change touches doctrine, legal/political position, sensitive material, accusations, institutional commitments, or several documents at once.

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

Approval of an idea, analysis, plan, sequence, outline, or next intellectual step is **not** authorization to write to GitHub.

The following expressions, when used alone, MUST NOT be treated as GitHub write authorization:

```text
ok
yes
good
reasonable
continue
go on
that is the right direction
```

A GitHub write requires an **explicit, action-specific, repository-specific instruction**. The authorization must make clear which operation is permitted, for example:

```text
create a branch in JeanHuguesRobert/barons-Mariani
commit this file to that branch
push the branch
open a draft pull request
update AGENTS.md on main
merge pull request #N
publish this document in the corpus
```

Authorization for one document, repository, branch, or prior task does not transfer to another.

Before any external GitHub write, the agent MUST restate the intended operation in one concise line containing:

```text
repository
branch or target ref
files or objects affected
write operation
public/private consequence
```

The agent MUST then act only if the user's instruction explicitly covers that operation.

A branch, commit, issue, comment, or draft pull request in a **public repository counts as publication**, even when it is not merged into the default branch. Branching and draft status protect canonical stabilization; they do not preserve confidentiality.

When explicit GitHub authorization is absent, the agent may:

- reason in conversation;
- prepare an outline;
- draft text in the chat;
- create a local or sandbox artifact that is not pushed;
- present a proposed patch for review.

It MUST NOT create or update remote branches, commits, issues, pull requests, comments, labels, releases, or repository files.

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

Agents must not commit, push, publish, send, sign, spend, or otherwise stabilize an action unless Jean Hugues Robert has given explicit, scoped authorization for that operation.

When authorization is ambiguous, prepare the batch and ask before acting.
