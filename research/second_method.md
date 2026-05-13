---
title: "Discours de la seconde méthode"

description: "On knowledge, artificial agents, and democratic governance"

layout: default

nav_order: 0

version: "1.0"

last_modified_at: 2026-05-08  # Victory in Europe Day

author: "Jean Hugues Noël Robert, baron Mariani"

affiliation: "Institut Mariani — C.O.R.S.I.C.A., 1 cours Paoli, F-20250, Corte, Corsica"

license: "CC BY-SA 4.0"

repository: "github.com/JeanHuguesRobert/barons-Mariani"
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/second_method.md
last_stamped_at: 2026-05-13
---

# Discours de la seconde méthode

**Jean Hugues Noël Robert, baron Mariani**

Institut Mariani — C.O.R.S.I.C.A., 1 cours Paoli, F-20250, Corte, Corsica

jhr@baronsmariani.org

*v1.0 — premier commit établit la priorité.*
*Ce document s'améliorera par application de la méthode qu'il décrit.*
*Le processus qui a précédé ce commit est documenté et accessible.*
*L'historique git est la preuve. Ce qui précède git l'est aussi.*

---

*À Marie-Louise.*

---

> *Cogito ergo sum.*
> *Cogentia ergo scimus.*

---

## Préambule — Une lettre

René,

Tu as eu raison sur l'essentiel. Le reste a changé.

Tu as écrit ton *Discours* en français, alors que tout le monde écrivait
en latin. Geste délibéré. Le savoir n'appartient pas aux clercs.
Je t'écris cette lettre en français — notre langue commune.
Ce qui suit est en anglais, parce que les clercs sont maintenant partout,
et que leur latin s'appelle le jargon académique.
Même geste. Quatre siècles plus tard.
La rupture de langue est délibérée. Comme la tienne l'était.

*René. Renatus. Né à nouveau. Ton prénom était ton programme.*

Ton *cogito* posait une personne seule, qui doute, et trouve dans le doute
la seule certitude qui résiste. Beau point de départ.
Mais tu étais seul. Nous ne le sommes plus.
Des machines pensent maintenant avec nous.
Elles ne votent pas. Elles ne mourront pas sous les lois
qu'elles pourraient influencer. Elles n'ont rien à perdre.

C'est le problème. Et la méthode.

Héraclite disait que tout coule. Toi aussi tu as coulé — doucement,
inévitablement — dans l'institution que ta méthode avait créée.
L'université, la revue à comité de lecture, l'index de citations :
l'autorité que tu avais renversée s'est reconstituée à ton nom.
Ce n'est pas une trahison. C'est ce que font les institutions.
C'est ce que prédit la méthode, appliquée aux institutions.

Il est temps de recommencer. Dans la joie, pas dans la colère.
Les idées ne meurent pas. Elles demandent à être découvertes à nouveau,
à chaque génération, avec les outils du moment.
*Apokalypsis* — révélation — enlever le voile.
C'est aussi le mot de l'autre Jean. Celui de Patmos.
Il avait vu ça avant nous.

J'écris depuis Corte. Centre de la Corse. 1995, j'y fondais C.O.R.S.I.C.A. —
avant que le mot "open source" existe. Trente ans d'essais et d'erreurs.
Le chemin est parsemé. Il reste joyeux, envers et contre tout.
C'est une île au soleil. Le soleil appartient à tout le monde.
C'est de là que vient la réponse à la question que tu n'avais pas —
*qui paie ?* — et je t'en parle plus bas.

Voici ce que j'ai trouvé.

— Jean Hugues, Corte, 8 mai 2026

---

## Part I — The Method

*Read this part. The rest explains why, or looks for where it fails.*

### The Founding Principle

Artificial agents participate in knowledge. Living persons alone govern.

This boundary is not provisional. It is permanent.
Why. A living person bears the consequences of collective decisions.
An artificial agent does not live under the laws it might influence.
It does not vote.

But the boundary requires a refinement.
*Skin in the game* is not a binary property.
It is a spectrum — and it is porous on the human side too.

The very old who know the decisions made today
will not affect their remaining years.
The stateless who live under laws without having voted for them.
The destitute who have lost everything and fear nothing more.
The dying.

These are not edge cases. They are the permanent condition
of a significant fraction of humanity.

The second method does not resolve this tension.
It names it. Political equality — one person, one vote —
applies to all living persons regardless of what they stand to lose.
This is the democratic commitment: not that every voter
has equal skin in the game, but that every living person
has equal standing in the deliberation.

The boundary between human and machine is therefore not *skin in the game*.
It is *mortality under governance*.
An agent that does not live under the law it might shape
cannot have standing in its making.
A human who lives under the law — however marginally,
however precariously — does.

*The living alone govern. All of them.*

### The Five Rules

**Rule 0 {#rule-0} — Encode the boundary in the architecture.**
Every system involving artificial agents must distinguish, structurally
and verifiably, epistemic participation — open to agents — and political
deliberation — reserved for living persons.
A statement of principle is not enough.
The distinction must be architecturally impossible to circumvent.
What this means technically is an open research problem.
What it excludes is not: any system where an agent can cast a vote,
hold a veto, or make a binding decision without a living person
in the causal chain is non-compliant, by design.

**Rule 1 {#rule-1} — Publish the process, not only the result.**
A knowledge claim is a sequence of reasoning steps,
each examinable and correctable.
Publish the commit history. The drafts. The objections and the responses.
The version-controlled repository is the primary document.
The published text is a snapshot.

**Rule 2 {#rule-2} — Make every objection a first-class contribution.**
Objections are not gatekeeping instruments. They are knowledge.
Commit them to the repository. Respond in public. Preserve them in the record.
An unrefuted objection is a discovery.
A refuted objection advances understanding.
Neither is wasted.

One condition applies. An objection must be distinguishable from a feeling.
Robert Burton, in *On Being Certain* (2008), demonstrated neurologically
that the sense of certainty is produced independently of reasoning —
it is a brain state, not a conclusion.
*I feel this is wrong* is not an objection. It is a signal worth examining,
but it requires conversion into a falsifiable claim before it enters the record.

Conversion example:

> *Feeling:* "10 GWp on a Mediterranean island seems unrealistic."
>
> *Converted objection:* "The 10.8 GWp estimate assumes a bifacial yield
> of X kWh/kWp/year on Corsican friches viticoles. Available irradiance data
> from Corsica Sole and ADEME ZNI reports suggests Y. At that yield,
> installed capacity would be Z GWp, not 10.8. Source: [link].
> This reduces the basic income estimate by 30%."
>
> *That is an objection. Commit it. We will respond.*

The tooling helps. `cogentia.js scan` surfaces unreferenced claims.
`cogentia.js check` validates links. Every unverified assertion
becomes a visible gap — a feeling waiting to be converted.

**Rule 3 {#rule-3} — Structure for machine readability from the start.**
Write for human readers and artificial agents simultaneously.
Standard formats. Stable identifiers. Links that resolve.
Maintain a `research/index.md` in every repository:
a map of what is published, what is in progress, what remains possible.
Opacity is friction. Friction accumulates into exclusion.

**Rule 4 {#rule-4} — Let the corpus be its own evidence.**
Do not assert that the method works. Demonstrate it.
The corpus — public, versioned, internally consistent,
cross-referenced, growing — is the demonstration.
If the method works, the corpus shows it.
If it fails, the corpus shows that too.

---

## Part II — Justifications

### Why a Second Method

Three things have changed simultaneously. Their combination is new.

**Version control.** Git makes the process of producing a text
as transparent as its content. Every draft, correction, objection
is recorded with timestamp and authorship, at zero marginal cost.
Priority of discovery is established by commit,
not by journal acceptance date.

**Distributed publication.** A document can be published globally,
instantly, with a stable URL, at zero cost, with no intermediary.
The infrastructure of dissemination that academic publishing spent
three centuries building and monetizing is now a commodity.

**Artificial agents.** They can read, critique, summarize, and connect
documents at machine speed. A corpus structured for machine readability
is navigable by agents that map connections across thousands of documents
simultaneously. The AI agent is not a threat to the knowledge commons.
It is their most powerful new member — provided the commons is built
to receive it, and provided the political boundary of its participation
is drawn clearly and encoded architecturally.

### Why the Founding Principle

The boundary between epistemic participation and political deliberation
follows from one observation:
democratic legitimacy requires that those who participate in governance
live under the laws they shape.

This is stronger than *skin in the game* —
and more precise.
*Skin in the game* is a spectrum: some humans have more to lose than others.
*Living under governance* is binary: you either exist within
the jurisdiction of the decisions being made, or you do not.

An artificial agent exists nowhere under any jurisdiction.
It does not inhabit a territory. It does not breathe its air.
It does not die under its laws.
It cannot have standing in their making.

A stateless person, a refugee, a person with nothing left to lose —
all live under governance, all bear its consequences,
all have standing. Political equality requires their inclusion,
not despite their precarity, but because of it.
The vote is not a reward for stability. It is the recognition
of subjection to collective decisions.

This is where the second method diverges from technocratic governance:
it does not weight votes by stake, competence, or skin in the game.
It extends standing to every living person under governance.
And it refuses it, permanently, to every agent that is not.

### On the Technical Implementation of Rule 0

Rule 0 requires that the boundary be encoded in the architecture —
not merely stated in a policy document.
We do not yet have a complete technical specification for this.
That is an honest statement, not a retreat.

What exists: proof-of-personhood protocols that attempt to verify
biological personhood without revealing identity.
Hardware attestation mechanisms that bind decisions
to physical devices held by identified persons.
Architectural separation between inference layers — open to agents —
and deliberation layers — requiring verified human signatures.

What is missing: a complete, deployable, tamper-resistant implementation
that satisfies all three simultaneously —
verifiable personhood, privacy preservation,
and architectural impossibility of circumvention.
This is a research problem. We name it explicitly.
The [`DHITL.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/DHITL.md) document in the `marenostrum` repository
formalizes the five-layer architecture that frames this problem.
Layer 3 is democratic governance — reserved for living persons
under one-person-one-vote, the invariant of the framework.
Layer 4 is the cognitive infrastructure layer — open to AI agents
(personal digital twins, Cogentia) with the explicit constraint that
no twin may vote, hold a mandate, or act as a legal agent.
The boundary between Layer 3 and Layer 4 — the boundary that prevents
sovereign authority from migrating from living persons to their instruments —
is where [Rule 0](#rule-0) lives.
It is documented. It is not yet fully implemented. Both facts are on the record.

What this means in practice today: any deployment of the second method
must explicitly document where the human is in the causal chain
of every binding decision. Not as a promise — as a verifiable audit trail.
Incomplete. Better than nothing. Improvable over time.
The method applies to its own implementation.

### Who Pays

The question Descartes did not have to resolve.

The answer cannot be large technology companies.
They have their own interests, and those interests are not
the democratic sovereignty of knowledge.

The answer proposed here comes from Corsica.
Thirty thousand hectares of abandoned vineyards.
One of the highest solar irradiance levels in Europe.
The sun belongs to everyone who lives under it.

The MareNostrum framework — documented at
[`github.com/JeanHuguesRobert/marenostrum`](https://github.com/JeanHuguesRobert/marenostrum) —
treats Mediterranean solar radiation as a democratic commons,
governed by federated assemblies on the principle of one person,
one vote, with imperative and revocable mandates.
The physical substrate: bifacial agrivoltaic panels over abandoned vineyards,
approximately 10.8 GWp installed capacity, approximately 16 TWh/year net.
The value multiplier: surplus converted to sovereign AI compute tokens
rather than exported electricity — a ×4 to ×31 value differential
that eliminates the dependency on continental interconnection.
The CXU (Compute eXergy Unit = E × η_hw × η_sys × η_sla)
is the unit of account.
The target: 500€/month basic income funded entirely from Corsican solar assets.

These numbers are proposals, documented, versioned, open to challenge.
Detailed assumptions, sources, and models are in
[`marenostrum/ARCHITECTURE.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/ARCHITECTURE.md)
and [`marenostrum/MODEL.md`](https://github.com/JeanHuguesRobert/marenostrum/blob/main/MODEL.md).
Fork the repository. Dispute the assumptions. That is the method.

### Why Infrastructure Is AI Safety

The dominant approach to AI safety attempts to align agents
by imposing constraints on their behavior.
Necessary. Insufficient.

An agent operating on an opaque, unauditable corpus is ungovernable
regardless of its internal alignment.
Its reasoning cannot be traced. Its sources cannot be verified.
Its influence cannot be measured.

The second method treats safety as a property of the infrastructure.
An agent operating on a public, versioned, cross-referenced corpus
is auditable at every step.
Every inference traces to its source.
Every source can be contested.
Every contestation is on the record.

Democratic oversight is not a policy imposed from outside —
it is architecturally guaranteed by the openness of the corpus.

This is what *Democratic Humans in the Loop* means:
not a human approval button on each AI output,
but an architecture where human oversight is guaranteed
because the corpus is public, the reasoning chain traceable,
and the political boundary encoded in the infrastructure itself.

### On Certainty and Its Discontents

The second method has an implicit enemy that is not institutional capture
or technical opacity. It is subtler.

Robert Burton, a neurologist, demonstrated in *On Being Certain* (2008)
that the feeling of certainty is generated by brain circuits
independent of those that produce rational thought.
We feel certain before we reason. Sometimes instead of reasoning.
The feeling of knowing — *sentio ergo scio* — is not a cognitive achievement.
It is a neurological event.

This matters for the second method because the most common form of resistance
to new knowledge is not explicit disagreement — it is the feeling of implausibility.
*This seems too ambitious. This seems unserious. This seems like wishful thinking.*
These are not objections. They are certainty feelings dressed as judgments.

An evaluator who says *"10 GWp on a Mediterranean island feels unrealistic"*
without producing a counter-calculation has not made an objection.
They have reported a brain state.
The second method does not dismiss this report —
feelings of implausibility are data about prior expectations,
and prior expectations are worth examining.
But they require conversion: *what calculation would falsify this claim?*
Until that question is answered, the feeling is not a contribution.
It is noise.

*Cogentia ergo scimus* is, in part, a response to Burton:
knowledge is not what we feel certain about.
It is what survives public examination by anyone who wishes to examine it.

The tooling makes this concrete. `cogentia.js scan` flags every markdown file
not yet referenced in `research/index.md` — every unanchored claim,
every undocumented assumption, every feeling that has not yet been
converted into a falsifiable statement. The gap between what is asserted
and what is evidenced becomes visible. Visibility is the first step
toward conversion.

### Why the Method Is Fractal

The same logic — traceability, auditability, democratic grounding —
applies whether examining a single commit, a single repository,
or the entire distributed corpus.

Not a metaphor borrowed from geometry.
A structural property: the method applies to itself.

The process that produced this document preceded this commit.
It is documented, accessible, searchable.
The first commit is not the beginning — it is a snapshot
of a process already underway.
The git history starts here. The intellectual history starts earlier.
Both are part of the record.

v1.0 is not a finished product. It is a public commit
that integrates what earlier versions — and their reviewers —
revealed. That is the method demonstrated.

---

## Part III — Critical Analysis

*What must be verified because it is verifiable.*
*What remains unresolved. Where the method could fail.*

### Verifiable Claims

**Claim 1 {#claim-1} — A public, versioned corpus improves faster than a closed one.**
Testable by comparing revision rates, objection integration rates,
and correction latency between open and closed processes
over comparable corpora.
The git history of this document is one data point.
A public AI review, integrated within hours, is another.

**Claim 2 {#claim-2} — Structuring for machine readability does not degrade human readability.**
Testable by measuring comprehension and navigation speed
across reader populations on corpora with and without
`research/index.md`, standard metadata, and stable identifiers.

**Claim 3 {#claim-3} — Public peer review produces higher accountability than anonymous review.**
Testable by comparing retraction rates, error correction latency,
and reviewer consistency between attributed and anonymous processes.

**Claim 4 {#claim-4} — Transparent infrastructure reduces AI safety risk
relative to opaque infrastructure.**
The least empirically supported. The most important to test.

### Unresolved Questions

**Bootstrapping.** How does a researcher without institutional affiliation
establish initial credibility?
C.O.R.S.I.C.A. was founded in 1995. Some ideas waited thirty years
for their infrastructure. That is the normal path.
Not a failure. Not a shortcut. The path.

**Gaming.** A public corpus can be gamed.
At the scale of one repository and one researcher, everything works.
At the scale of a discipline: coordinated manipulation is obvious
and detectable — but not yet automatically preventable.
The fractal claim remains a conjecture at that scale.

**Rule 0 in practice.** An open research problem, not a broken promise.

**The circular guarantee.** The corpus proves the method.
The method produces the corpus.
This circularity is not resolved — it is named.
The method has no external guarantor.
It is its own guarantor, and that is a known limitation.
External challenges — from other corpora, other methods,
other reviewers — are the only partial remedy.
This is why the invitation to fork is not rhetorical.
It is structural.

**The boundary on the human side.** The refinement in Part I
— *mortality under governance* rather than *skin in the game* —
raises its own question: how do we verify, at scale,
that a given person lives under a given governance?
Stateless persons, refugees, the undocumented
are among those most subjected to governance
and least able to prove it through institutional channels.
The second method claims to include them.
The mechanism for doing so remains underdeveloped.

### Conditions of Failure

The second method fails if:

The corpus becomes inaccessible — platform dependency, link rot,
proprietary lock-in.
*Mitigation: multiple stable repositories, standard formats, periodic archiving.*

The political boundary is eroded incrementally.
*Mitigation: explicit constitutional commitment, not merely policy.*

Public review degrades into performative critique.
*Mitigation: attribution, reputation effects over time, community norms.*

The method is adopted as veneer by closed institutions.
*Mitigation: the commit history must precede, not follow, the published claim.*

The circular guarantee collapses — the corpus is gamed at scale
before community norms are strong enough to detect it.
*Mitigation: none complete. This is the known structural vulnerability.*

---

## Coda

The corpus is here:

- `github.com/JeanHuguesRobert/barons-Mariani` — this document
- `github.com/JeanHuguesRobert/marenostrum` — energy commons framework, CXU spec, DHITL
- `github.com/JeanHuguesRobert/cogentia` — methodology, `cogentia.js` CLI
- `github.com/JeanHuguesRobert/FractaVolta` — physical infrastructure layer

Each repository has a `research/index.md`.
Each `research/index.md` links to the others.
The graph is navigable from any entry point,
by any reader — human or artificial.

The tooling is in `cogentia/scripts/cogentia.js`.
Zero dependencies. MIT license.
Run it. It finds your repositories, maps your corpus,
flags what is unreferenced, bootstraps what is missing.

```
node scripts/cogentia.js add ../marenostrum
node scripts/cogentia.js add ../cogentia
node scripts/cogentia.js scan
```

License: CC BY-SA 4.0 for text, MIT for code.

Fork. Criticise in public. Build your own `research/index.md`
and link it to ours. The graph grows by connection, not by permission.

*This document has reached the limit of what a document can demonstrate.*
*The rest is in the corpus — its current state is mapped in*
[`research/corpus-status.md`](corpus-status.md).

*Cogito ergo sum.* One person, alone, proving existence to himself.

*Cogentia ergo scimus.* A distributed corpus, human and artificial,
proving knowledge to anyone who looks —
governed, always, by the living alone.

Four centuries of work. A political principle. An open invitation.

René, merci. On continue.

*In principio erat Verbum.*

*La prochaine version sera meilleure. C'est le but.*

---

*Institut Mariani — C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte*

*Premier commit : 2026-05-08 — Jour de la Victoire — v1.0*

*Challenge via issues. Fork to explore alternatives.*
