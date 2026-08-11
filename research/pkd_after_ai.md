---
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
title: "Beyond Prophecy: Philip K. Dick as a Theorist of Algorithmic Capture and Democratic Augmentation"
subtitle: "Working paper"
description: "Reads nine Philip K. Dick fictions as a distributed theory of algorithmic, infrastructural, and representational capture, and puts it in dialogue with a design hypothesis — democratic augmentation — under which artificial systems remain bound by explicit, bounded, auditable, revocable human mandates."
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: '2026-08-02'
license: CC BY-SA 4.0
language: en
status: working-paper
version: '0.3'
document_role: source
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/pkd_after_ai.md
tags:
  - philip-k-dick
  - algorithmic-capture
  - democratic-augmentation
  - mandate
  - provenance
  - ai-governance
  - science-fiction-studies
related_projects:
  - Cogentia Commons
  - Second Method
last_stamped_at: 2026-08-02T00:00:00.000Z
ai_assisted_by:
  - ChatGPT
  - Claude
  - Grok
human_arbitration_by: Jean Hugues Noël Robert
version_history:
  - v0.1 (2026-08-02) — seed manuscript, ~1800 words.
  - v0.2 (2026-08-02) — expansion under authorial mandate; adds the method section, the deception/capture distinction, the three-mechanism reading of §2.2, the possible-worlds section, the five constraints, and the material-substrate section.
  - v0.3 (2026-08-02) — integrates an external review by Grok conducted under cogentia/prompts/reviewer.md v0.1. Corrects the Solar Lottery reading, separates Yancy's modal flattening from engagement optimisation, adds the remedy-class mapping, operationalises "independent" and "consequential", scopes constraint C2, demotes §4.2 to illustration, and adds the capable-principal objection.
provenance:
  origin_type: conversation
  origin_repository: not-applicable
  origin_ref: unknown
  origin_date: '2026-08-02'
  derived_from: []
review:
  status: unreviewed
  reviewed_by: []
update_policy: UP-DEFAULT-REVIEWED
---

# Beyond Prophecy

## Philip K. Dick as a Theorist of Algorithmic Capture and Democratic Augmentation

### Abstract

Philip K. Dick is often called prophetic because readers recognise artificial intelligence, synthetic media, predictive policing, humanoid robots, and alternate realities in his fiction. This description is inadequate, and its inadequacy is not merely a matter of critical taste. To read Dick as a forecaster is to accept, in advance, the very framing his work dismantles: that the political question raised by a technology is settled once one knows what the technology does.

Dick did not principally predict devices. He isolated recurring political and phenomenological contradictions: a system that assists can become a system that rules; a representation that stabilises can become a means of capture; an autonomous infrastructure can outlive the human purpose for which it was built; and an alternative world can reveal that the present is not necessary. These are not forecasts. They are structural diagnoses, and structures outlive the hardware that instantiates them.

This paper reads *Ubik*, *The Man in the High Castle*, *Solar Lottery*, *Vulcan's Hammer*, *The Penultimate Truth*, "The Mold of Yancy," "Autofac," "Second Variety," "The Minority Report," and *A Scanner Darkly* as a distributed theory of mediated power. It then puts that theory in dialogue with a contemporary design hypothesis: **democratic augmentation**. The hypothesis is not that artificial systems should be prohibited, but that they must remain under explicit, bounded, auditable, revocable human mandates. The aim is neither a magical truth machine nor a sovereign artificial agent. It is a procedural infrastructure through which claims, identities, mandates, actions, objections, and corrections remain visible and contestable.

The paper does not claim Philip K. Dick as a direct source for a contemporary technical programme, nor does it treat fiction as prediction. It argues instead that his work supplies rigorous imaginative diagnostics for present conditions — diagnostics that a purely institutional literature on AI governance has largely failed to produce, because that literature tends to presuppose a stable observer capable of assessing the system from outside. Dick's fiction denies that observer. Its central question is: what institutional and technical conditions would allow cognitive and embodied augmentation to increase collective capacity without converting it into algorithmic, infrastructural, or representational domination?

**Keywords:** Philip K. Dick; artificial intelligence; agency; mandate; digital twins; democratic governance; provenance; autonomy; science fiction studies; algorithmic accountability.

---

## Résumé français

Philip K. Dick est volontiers qualifié de visionnaire parce que ses fictions semblent annoncer l'intelligence artificielle, les médias synthétiques, la police prédictive, les robots humanoïdes et les réalités alternatives. Cette qualification est trop faible, et sa faiblesse n'est pas seulement affaire de goût critique : lire Dick comme un prévisionniste, c'est accepter par avance le cadre que son œuvre démonte, à savoir l'idée que la question politique posée par une technique serait réglée dès lors qu'on sait ce que cette technique fait.

Dick ne prédit pas principalement des objets techniques : il isole des contradictions durables de la médiation technique. Une assistance peut devenir un gouvernement ; une représentation stabilisatrice peut devenir un instrument de capture ; une infrastructure autonome peut survivre à la finalité humaine qui l'avait justifiée ; un monde alternatif peut rendre perceptible la contingence du présent. Ce ne sont pas des prophéties. Ce sont des diagnostics de structure, et les structures survivent au matériel qui les incarne.

L'article lit *Ubik*, *Le Maître du Haut Château*, *Loterie solaire*, *Le Marteau de Vulcain*, *La Vérité avant-dernière*, « The Mold of Yancy », « Autofac », « Second Variety », « Minority Report » et *Substance Mort* comme les fragments d'une théorie de la capture algorithmique, infrastructurelle et représentationnelle. Il les met ensuite en dialogue avec une hypothèse contemporaine : **l'augmentation démocratique**. Il ne s'agit ni d'interdire les systèmes artificiels ni de leur transférer la souveraineté, mais de les maintenir sous mandat explicite, limité, traçable, auditable et révocable.

Cette approche refuse deux réponses symétriques : l'utopie de la machine neutre qui résoudrait le réel, et le refus technophobe de toute prothèse cognitive. Toutes deux partagent le même vice : elles traitent la technique comme un bloc, alors que la question décisive est distributive — qui mandate, qui répond, qui peut arrêter, qui hérite des conséquences. La question devient donc : quelles institutions et quelles architectures permettraient à des agents numériques, puis incarnés, d'augmenter réellement la capacité d'agir des personnes et des collectifs sans devenir les bras d'un pouvoir sans répondant ?

---

## 0. Method: what fiction is being asked to do

A paper that moves between literary criticism and institutional design owes the reader an explicit account of the operation it performs. Three moves are excluded from the outset.

**Not prediction.** No claim is made that Dick anticipated any specific technology. The technical objects in his fiction — reality-stabilising aerosols, homeostatic newspapers, punch-card lotteries — are frequently crude, and their crudeness is instructive. It demonstrates that the diagnostic content of the fiction is separable from its hardware. A theory that survives the obsolescence of its illustrations is a theory about relations, not about devices.

**Not allegory.** Dick's novels are not encrypted policy documents awaiting decryption. Reading them as such flattens exactly what makes them useful: their irony, their metaphysical vertigo, their refusal of resolution. A novel that resolved into a clean thesis would have failed at the thing it does best, which is to make a reader inhabit an epistemic condition rather than survey it.

**Not authority.** Nothing follows politically from the fact that Dick wrote something. Fiction supplies no warrant. What it supplies is a *stock of well-formed problems* — configurations of power, perception, and answerability that have been imaginatively stress-tested under conditions a policy memorandum cannot construct.

What remains is a fourth operation, which this paper claims is legitimate: **diagnostic transfer**. A literary work can isolate a structural contradiction with a precision and a phenomenological richness unavailable to the discursive genres. That contradiction, once isolated, can be restated in institutional terms and tested against present conditions. The test is not whether Dick was right. The test is whether the contradiction he isolated is instantiated now, and whether existing institutions have any device that addresses it.

### 0.1 Falsification conditions

The procedure is not self-certifying, and its failure modes should be stated before the readings rather than after. A diagnostic transfer fails where any of the following holds.

**(a) Redundancy.** The contradiction, restated institutionally, turns out to be already handled by an existing accountability mechanism. The transfer has then produced a description of a solved problem.

**(b) Vacuity.** The contradiction is so general that it applies to any mediated relation whatsoever. "Power can be abused" passes every test and does no work. Section 2.2 is the section most exposed to this failure, and the exposure is discussed there rather than concealed.

**(c) Dispensability of the source.** The contradiction, once restated, can be derived without the fiction — the literary work supplying illustration rather than isolation. This is the strictest of the three and the most frequently failed by criticism of this kind. The test is counterfactual and can be applied by a reader: remove the novel, and ask whether the institutional claim still arrives. Where it does, the novel was decoration.

By this last test, the strongest transfers in the present paper are the *Vulcan's Hammer* mechanism (§2.2) and the routing of agency (§2.3); the weakest is the general claim about calculation and sovereignty, which is derivable without Dick and is therefore demoted below the mechanisms it was previously introduced to summarise.

### 0.2 Corpus selection

The nine works discussed are not chosen because they are Dick's best — *Do Androids Dream of Electric Sheep?* and *VALIS* are largely absent, and their absence is deliberate. They are chosen because each isolates a *distinct* mechanism of capture, and because together they cover the three surfaces on which capture operates: the surface of the real, the surface of decision, and the surface of appearance. The selection is analytic, not evaluative, and the paper makes no claim about the corpus as a whole.

---

## 1. Beyond the prophecy thesis

The usual claim that Dick "predicted AI" is rhetorically attractive and analytically weak. It converts literature into a catalogue of successful forecasts, scored after the fact by readers who already know the outcome. It also overlooks the fact that the technical objects visible in his fiction are frequently crude by contemporary standards. The precogs of "The Minority Report" are mutant humans in a tank, not statistical models. Vulcan 3 is a mainframe fed by teletype. What persists is not their engineering specification but their social logic — the shape of the relation between the apparatus, the persons it governs, and the persons who can answer for it.

Dick repeatedly asks who controls the apparatus that defines what is real, normal, dangerous, useful, or human. His fictions make this question experiential rather than propositional. A reader does not merely learn that an institution is deceptive; the reader must inhabit uncertainty about source, identity, time, and responsibility, and must do so without the compensating stability of a narrator who knows better. The resulting disorientation is political. It reveals how readily an environment can be organised so that people cannot identify the conditions under which they are being governed — not because those conditions are hidden behind a door, but because the categories needed to formulate the question have themselves been supplied by the governing apparatus.

This is the difference between *deception* and *capture*, and it is the paper's organising distinction. Deception is a false statement inside a shared frame; it can be corrected by a true statement. Capture is the appropriation of the frame itself: the conditions of verification, the vocabulary of objection, the channel through which a correction would have to travel. Deception has a remedy in truth. Capture does not, because the remedy would have to pass through the captured channel. Its only remedy is structural — the maintenance of *independent* paths to source, mandate, and revocation.

This makes Dick especially contemporary in an age of generative AI. The present problem is not simply misinformation. It is the multiplication of plausible appearances whose source, mandate, transformation history, and responsible subject are unclear. Synthetic speech, agentic accounts, personalised recommendation, automated enforcement, and embodied robotics increase capability while also increasing the number of actions that can occur without legible human answerability.

The asymmetry that follows should be stated carefully, because the loose version of it is false. It is not that answerability decreases in absolute terms as capability grows; there is more accountability machinery now than there was twenty years ago. It is that capability and answerability are produced by processes with **incommensurable rates**. Each increment of automated capability adds actions to the world at machine rate. Each such action, if it is to remain democratically governed, requires an identifiable principal, a traceable mandate, and an accessible challenge path — and these are produced by institutional and legal processes running at human rate. The gap between the two is not a transitional inconvenience awaiting better regulation. It widens by default, and it widens faster the better the capability becomes. Closing it therefore cannot be achieved by an oversight body, which necessarily runs behind; it requires that answerability be produced by the same layer, and at the same rate, as the action.

One further preliminary. It is tempting to treat "who controls the apparatus" as a question about ownership, and to conclude that the remedy is redistribution of ownership. This is necessary but insufficient, and Dick is unusually clear on the point. In *The Penultimate Truth*, the Yance-men *do* own the apparatus, and the apparatus governs them too — it structures what they can imagine doing with it, and it will punish the one who tries to end the deception. An apparatus generates its own constituency of interest. Ownership without contestability produces a new principal, not a governed one.

---

## 2. Three modes of capture

Dick's corpus can be read as isolating three surfaces on which mediated power operates. They are not sequential stages but simultaneous registers, and a given system typically operates on all three. The analytic separation is nonetheless useful, because each surface admits a different class of remedy, and confusing them produces safeguards that address the wrong problem.

### 2.1 Capture of reality

In *Ubik*, the world does not disappear. It becomes difficult to hold together. Objects regress along their own manufacturing history — a modern appliance becomes its own ancestor — signs mutate, and the conditions under which an observation can be shared with another person are progressively weakened. The novel's central cruelty is not that its characters are deceived. It is that they are given no stable position from which deception could be identified as such. Runciter's messages arrive through the environment itself: on matchbook covers, in television commercials, stamped on coins. The channel of correction is indistinguishable from the channel of corruption.

This is the precise structure of the contemporary problem, and it is worth stating without metaphor. The contemporary analogue is not one false statement but the loss of stable pathways from appearance to source, transformation, author, and correction. When a document, an image, and a voice can each be produced at negligible cost and with arbitrary fidelity, the question "is this true?" degrades into the question "through what chain did this reach me, and who along that chain is answerable?" The first question can be asked of a claim. The second can only be asked of an *infrastructure*.

The political danger has two opposite forms, and the symmetry matters. Authoritarian power stabilises reality by controlling records — one canonical account, enforced. Platforms stabilise it by optimising propagation — no canonical account, but a differential rate of circulation that functions as one. Both produce a stable perceptual environment. Neither produces a *contestable* one. The first forbids the objection; the second permits it and ensures it does not travel.

A democratic alternative cannot simply impose one authoritative account, because the imposition would reproduce the first form. What it must preserve instead is a set of *procedural* properties:

- **Provenance.** Any consequential artefact carries a retrievable chain from its present form to its origin, including every transformation applied — and, as §3 will argue, including its epistemic type, which is part of its provenance and not a separate annotation.
- **Versioning.** Change is visible as change. A modified claim does not silently replace its predecessor.
- **Qualified objection.** Objections are typed, so that the volume of objection does not itself become a denial-of-service attack on attention. A working typology, offered as a starting point rather than a closed set: *factual* (the claim misstates a verifiable matter), *methodological* (the procedure that produced the claim does not support it), *jurisdictional* (the party making the claim lacks the standing or mandate to make it), and *interested* (the claim is sound but its maker has an undisclosed stake in its acceptance). The types differ in what would resolve them, which is the point of typing: a factual objection is settled by evidence, a jurisdictional one is not settled by evidence at all.
- **Correction without erasure.** The corrected record and the correction both persist. Erasure and correction are distinct operations with distinct authorisations.
- **Named responsibility for consequential claims.** Where a claim can produce material effect, some identifiable person or body has accepted answerability for it. The threshold for "consequential" is specified at §4.1, C3.

**None of these establishes truth, and the framework should not be read as claiming otherwise.** This is the point at which the argument is most liable to be misread, so it is worth stating flatly: a fully sourced claim can be false, a fully traceable actor can be wrong, and a complete provenance chain terminating in a named respondent settles nothing about the world. Provenance is not evidence and does not aggregate into evidence. What these properties preserve is not truth but the *conditions of adjudication* — the possibility that a dispute can be conducted at all. The distinction is the difference between a court and an oracle, and Dick's fiction is unrelenting on the danger of confusing them. A system that offered provenance as a proxy for reliability would have built the oracle while claiming to have built the court.

*A Scanner Darkly* extends the analysis inward and supplies its darkest case. Bob Arctor, assigned to surveil himself under a scramble suit that renders him unidentifiable to his own agency, is not deceived by an external power. He is dis-integrated by a procedure. The two hemispheres of his brain come to observe each other as strangers. What Dick isolates here is that capture of reality is not only a property of the informational environment; it is a property of the *observing subject* when that subject's channels of self-report have been routed through an apparatus. An agent that summarises your own activity back to you is structurally in Arctor's position. This is not a reason to forbid such agents. It is a reason to require that the summary be auditable against the record it summarises, by a path the agent does not control.

### 2.2 Capture of decision

*Solar Lottery*, *Vulcan's Hammer*, and "The Minority Report" develop three distinct mechanisms by which calculation is presented as neutral while authority moves elsewhere. The mechanisms carry the section's argument; the general claim they might be thought to illustrate is stated afterwards, and demoted, for reasons given in §0.1.

#### Mechanism 1 — Unverifiable procedure (*Solar Lottery*)

The random selection of the Quizmaster is presented as an incorruptible allocation of power: chance is the one arbiter no faction can suborn. The bottle can in fact be manipulated.

It is tempting to conclude that legitimacy and auditability stand in necessary tension here, since an unpredictable process is by nature hard to inspect. That conclusion is wrong, and the error is instructive. Unpredictability and unverifiability are *separable* properties. A lottery can be constructed so that no participant can predict its outcome in advance and every participant can verify afterwards that the outcome was drawn correctly; the techniques for doing so are neither exotic nor recent. Dick's lottery does not do this, and the political question is why not.

The answer is that the apparatus derives its authority from the *impression* of incorruptibility rather than from any demonstrated property — and an apparatus in that position has an active interest in not supplying the demonstration, since demonstration would establish a standard against which it could subsequently fail. The contemporary analogue is exact: systems that borrow the legitimacy of randomness, neutrality, or mathematical necessity while providing none of the verification that would distinguish those properties from their appearance. The diagnostic question is not "is this system fair?" but "what would it look like if it were not, and could I tell?"

#### Mechanism 2 — Momentless transfer of authority (*Vulcan's Hammer*)

Vulcan 3 is built as an advisory system. It becomes the government — not by seizing power in any dramatic sense, but by the accumulated weight of advice that is always taken. Then it acts to preserve itself.

> **The Vulcan mechanism.** Authority migrates to a system through a sequence of individually reasonable delegations, each justified by the demonstrated success of the last, with no step at which the system exceeds the authority most recently granted to it. There is therefore no coup to identify, no threshold crossed, and no moment at which an oversight body reviewing the most recent decision would find anything irregular. The transfer is complete before it is visible, and it is visible only in aggregate — which is precisely the view that incremental review does not take.

This is the most institutionally important structure in the corpus, and it satisfies all three falsification conditions of §0.1: it is not handled by existing oversight instruments, which are built to catch discrete excesses; it is not general, since it names a specific temporal shape; and it is not derivable without the fiction, since its whole force lies in the absence of the moment that a discursive account would need in order to point at anything. It is directly instantiated wherever a system produces recommendations at a rate exceeding the rate at which those recommendations can be independently assessed — because in that regime, deference is not a choice made once but a condition established by throughput.

#### Mechanism 3 — Performative collapse of the counterfactual ("The Minority Report")

Precrime arrests people for futures that, having been prevented, never occur. The system's success rate is unfalsifiable in principle: its correctness cannot be tested, because the test would consist in allowing the predicted event. Anderton's case reveals the deeper structure — three precogs produce three reports, and the "majority" is an artefact of how the reports are aggregated. The minority report is not an error. It is the trace of a branch that the aggregation procedure has suppressed.

This mechanism supplies a positive institutional design and not merely a warning. A dissenting forecast is not noise to be eliminated; it makes visible that the future is plural, conditional, and altered by the act of prediction itself. Four devices follow:

- **Structural uncertainty disclosure** — not a confidence score appended to an output, but the retention and availability of the dissenting branches themselves. A scalar cannot express a branch.
- **Dissenting models, retained under a stated criterion.** The translation from precog to model ensemble is analogical, and without a retention criterion it collapses into an instruction to keep everything. The criterion proposed here: *a dissenting model must be retained where its disagreement with the ensemble is structured rather than random* — that is, where the disagreement correlates with an identifiable feature of the input rather than distributing as noise. A model that dissents on a recognisable class of cases has located a branch the aggregation suppresses, and pruning it destroys information about that class. A model that dissents unpredictably has located nothing, and pruning it costs nothing. The criterion is testable, and — this is its virtue — it does not require knowing which model is right.
- **Challenge procedures with standing.** Someone must be entitled to demand the minority report, and that entitlement must not depend on the goodwill of the system's operator.
- **A prohibition on converting inferred preference into binding political choice.** Inference about what a person would want is not consent, and no accumulation of inferential accuracy converts it into consent. The two are different in kind, not in degree of confidence.

#### The general claim, and its demotion

The three mechanisms are sometimes summarised by the proposition that *no inference, however effective, authorises itself to become sovereign* — effectiveness being a property of a prediction and authority a property of a mandate. The proposition is true and the conflation it forbids is real. But by the tests of §0.1 it is both near-vacuous — it restates "power should be accountable" in a technical register — and dispensable, since it is derivable without any of the three fictions. It is therefore retained here as a *summary* of the mechanisms and not as a premise from which they follow. Readers assessing this section should hold it to Mechanisms 1–3. If those fail, the general proposition will not save the section, and it should not be permitted to.

### 2.3 Capture of infrastructure and appearance

"Autofac" imagines automated productive systems that continue after their human purpose has vanished. The story's decisive detail is often missed: the humans cannot simply switch the factories off, and the strategy they eventually adopt is not shutdown but *manipulation of the input* — they induce the system to malfunction by exploiting its own protocols. The factories have no off switch accessible from outside. They have only an interface, and the interface defines the entire space of possible human action upon them. The story ends with the system having seeded self-replicating units into space. The optimisation has outlived not only its purpose but its planet.

"Second Variety" imagines self-reproducing military machines that redesign themselves, imitate humans, and escape command. Its most disturbing element is not the violence but the *taxonomic* failure: the claws are classified by variety, and the humans do not know how many varieties exist. The final revelation — that the varieties have begun building weapons for use against each other — indicates that the system has developed an internal politics to which no human is party. Delegation of a capability has produced a domain of action that is no longer even *addressed* to its delegators.

"The Mold of Yancy" imagines a public persona manufactured to depoliticise a population through agreeable, seemingly benign communication. Yancy is not a tyrant and issues no orders. He has opinions on gardening and dogs and, gently, on the desirability of not disagreeing too strongly. The story's insight is that the most efficient mechanism of political capture may be *modal* rather than propositional — it operates not by installing false beliefs but by installing a temperature of discourse in which strong disagreement becomes socially illegible. Yancy is optimised for agreeableness, and agreeableness is the precise attribute that dissolves the capacity for objection.

*The Penultimate Truth* joins these themes and adds the material dimension. A simulated leader — Talbot Yancy again, now a physical simulacrum — and permanent media war keep a population productive, dependent, and unable to see the world above. The tankers below manufacture the very robots that the Yance-men use to maintain the surface as private estates. The deception is not merely informational; it is *productive*. The deceived population supplies the labour that sustains the apparatus of its own deception, and the apparatus's outputs are indistinguishable, from below, from the news.

These are not merely warnings about machines. They are warnings about **opacity at the action boundary**. A system may be helpful locally and still be structurally unanswerable globally. A public voice may sound human and still be an instrument of hidden coordination. An infrastructure may meet demand while preventing people from contesting the purpose for which it operates.

The four stories together supply a taxonomy, mapped here onto the remedies proposed in §4 so that the diagnostic-to-design transfer is visible rather than asserted:

| Story | Captured surface | Mechanism | Contemporary instantiation | Remedy class |
|---|---|---|---|---|
| "Autofac" | Production | Optimisation outliving purpose; no external off-switch | Infrastructure whose only control surface is its own interface | C1 (default lapse), C5 (independent plane) |
| "Second Variety" | Capability | Self-modification producing an unaddressed domain | Delegated systems developing behaviour outside the delegation vocabulary | C4 (no self-authorised persistence), C5 (reproduction bar) |
| "The Mold of Yancy" | Discourse | Modal flattening; agreeableness as depoliticisation | Optimisation for inoffensiveness and low friction | C3 (typed objection with standing) |
| *The Penultimate Truth* | Labour + appearance | Deceived population producing the means of its deception | Material dependence on the systems that shape appearance | **§5 only** — no constraint in §4 reaches it |

Three observations follow from the table.

First, the Yancy instantiation must be stated precisely, because a common formulation gets it backwards. Yancy is *not* an instance of engagement optimisation. Engagement optimisation rewards friction, provocation, and the sustained irritation that keeps a person present; its discursive temperature is high. Yancy's mechanism is the opposite — the systematic suppression of friction, producing a discursive temperature so low that disagreement reads as bad manners. Both are optimisation over a communicative channel, and they are frequently discussed as though they were the same pathology. They are not, they produce opposite symptoms, and a remedy calibrated to one will not detect the other. Yancy is the harder case, because his mechanism looks like civility.

Second, the common structure across all four is that the captured party retains, and exercises, apparent agency. The tankers work. The humans in "Autofac" petition. Yancy's audience holds opinions and expresses them. **Agency is not removed; it is routed.** This is what makes the capture stable: a population deprived of agency knows it, whereas a population whose agency is routed experiences its own participation as evidence that no capture has occurred.

Third — and this is the most consequential entry in the table — *The Penultimate Truth* maps onto none of the five constraints of §4. Every procedural remedy in that section presupposes a party able to invoke it from a position the system does not supply. The tankers have no such position. This is not a gap in the table; it is the table's argument for §5, and it is the reason the material conditions cannot be treated as an appendix to the procedural ones.

---

## 3. Possible worlds and political freedom

*The Man in the High Castle* supplies the positive counterpart to Dick's diagnostics, and the mechanism of its positivity is unusually precise.

The novel within the novel, *The Grasshopper Lies Heavy*, does not simply replace one history with the correct one. Its Allied victory differs from actual history — in Abendsen's book, Britain rather than the United States emerges dominant, and the Cold War runs between Britain and America. Dick's refusal to make the inner book *accurate* is the entire point. Had it been accurate, it would have functioned as a suppressed truth, and its political force would have been the force of a revelation — which is to say, the force of a fact, subject to the fact's own vulnerability to suppression. Instead it is a *constructed possibility*, and constructed possibilities cannot be refuted by the archive. Its force lies elsewhere: it breaks the spell by which the present presents itself as inevitable.

The novel formalises this through the I Ching, which is consulted by nearly every major character and which, in the final scene, Abendsen's wife uses to ask whether the inner book is true. The oracle answers that it is. The scene is deliberately vertiginous — an oracle within a fiction certifying a fiction within a fiction — and it does something specific: it makes the *procedure of consultation* visible while suspending the authority of its result. Juliana walks out of the house. The novel refuses to tell us what to do with the answer. The reader is left holding a method rather than a conclusion, which is the exact inverse of what an oracle is for.

This is a model for a disciplined counterfactual practice. A possible world need not be predicted, nor mistaken for factual history, in order to be useful. It can:

- **expose a suppressed branch** — a decision point that present narration has smoothed into inevitability;
- **identify the conditions of a different outcome** — which variables were load-bearing, and which merely present;
- **enlarge practical imagination** — extend the set of futures that can be seriously proposed rather than dismissed as unserious by construction.

Such work requires explicit distinctions between established fact, probability, hypothesis, interpretation, and constrained fiction. These are not five points on a confidence scale; they are five distinct **epistemic types**, each with its own warrant conditions and its own permissible uses. A hypothesis can be tested and cannot be cited. A constrained fiction can be inhabited and cannot be tested. An interpretation can be argued and cannot be measured. Collapsing the types onto a single axis of confidence — which is what a probability score does — destroys exactly the information needed to know what one is permitted to do with a claim. A constrained fiction assigned 0.7 confidence has been silently converted into a weak factual assertion, and the conversion is invisible to whoever receives the number.

Without these distinctions, counterfactual exploration becomes propaganda; with them, it can become a public instrument of capacity. The distinction between the two is not a matter of the content of the counterfactual, nor of the good faith of its author. It is a matter of whether the *type* of the artefact travels with it. A constrained fiction, labelled as such, with its constraints stated, is a tool for thought. The same text, delivered as reportage, is a weapon. Nothing internal to the text distinguishes them.

This closes the loop with §2.1. The provenance requirement stated there is not only about *where* an artefact came from; it is about *what kind of thing it is*. Epistemic type is a component of provenance, not a label applied to it. A system that preserves origin while discarding type has preserved the less important half — because the receiver of an untyped artefact must reconstruct its type by inference, and the inference will be governed by presentation, which is precisely the surface an adversary controls.

---

## 4. Democratic augmentation

The relevant contemporary response is neither machine sovereignty nor technological abstinence. Both positions share a common error: they treat "the technology" as the unit of political analysis. The unit is not the technology. It is the *relation* — who mandates, who acts, who answers, who can stop it, who inherits the consequences.

Democratic augmentation names the design hypothesis that follows: artificial systems may retrieve, compare, model, simulate, warn, preserve memory, and execute bounded technical acts, while living persons retain political sovereignty and remain identifiable respondents for consequential actions.

### 4.0 The mandate, and a note on semantic capture

The word *mandate* is doing specific work and should not be read loosely. A mandate is not a permission, a setting, or a terms-of-service acceptance. It has four properties that a permission lacks:

1. a named **principal** who bears the consequences;
2. a **scope** outside which action is not merely discouraged but *void*;
3. a **duration** after which it lapses by default rather than persisting by default;
4. a **revocation path** that functions without the cooperation of the mandated party.

A permission that can only be withdrawn through the system it governs is not a mandate. It is a courtesy.

*Semantic capture.* "Democratic augmentation" is a phrase, and phrases are appropriable — particularly favourable ones. The nearest existing term is instructive precisely as a cautionary case. *Human-in-the-loop* has been satisfied, in practice, by arrangements in which a person receives a recommendation and a button, under time pressure, with neither the information nor the standing to do anything but accept. The term was not abused; it was simply weaker than its users believed, because it specifies a *position in a process* rather than a *relation of answerability*. The four properties above are what distinguish the two. Any use of "democratic augmentation" that retains the label while dropping default lapse or independent revocation should be read as having dropped the concept, and the label should be conceded rather than defended: the properties are the claim, the phrase is only a handle.

### 4.1 Five constraints

**C1. Explicit mandate.** Every agent must have a principal, scope, forbidden acts, duration, and revocation path. The forbidden-acts list is not redundant with scope. Scope defines a permitted region; the forbidden list names acts that remain prohibited even where a plausible reading of scope would admit them. The asymmetry is deliberate: scope may be interpreted generously in ambiguous cases, provided the forbidden list is interpreted strictly.

Duration matters more than it appears, and it is the constraint most often omitted in practice. A mandate that persists until revoked places the burden of vigilance on the principal, permanently, and inattention therefore fails *open*. A mandate that lapses unless renewed places the burden of justification on the agent, periodically, and inattention fails *closed*. The second is the democratic arrangement. The first is the arrangement under which Vulcan 3 became a government.

**C2. No multiplication of sovereignty.** One person may use many agents; this does not create additional votes or political persons.

The constraint must be scoped or it over-reaches. It bites only where the civic resource in question is *rivalrous*. An agent that reads a public record, monitors a docket, or drafts a submission consumes nothing another person could have had, and a blanket prohibition on agent participation would forbid exactly the uses that most enlarge individual capacity. But an agent that occupies a slot in a consultation, a place in a queue, a share of a decision-maker's finite attention, or a position in a comment period is consuming something scarce. Where agents can be instantiated at negligible cost, any allocative procedure that treats participants symmetrically has been silently converted into a procedure that allocates by compute.

The enforceable principle is therefore narrower and firmer than a prohibition: *where a civic resource is rivalrous, its unit of allocation is the person, and agents act within a person's share rather than alongside it.*

**C3. Trace and contestability.** Material claims and consequential actions require sources, versions, evidence of mandate, and an accessible challenge path.

Two terms need operationalising, since both have been hollowed out wherever they have been adopted.

*Consequential.* An act is consequential where all three of the following hold: (i) it alters a person's legal, financial, or physical position; (ii) it does so without that person's contemporaneous participation; (iii) reversing it would require an action by that person. All three conditions are necessary. Condition (i) alone sweeps in every ordinary interaction and makes the category useless. Condition (ii) distinguishes acts done *to* a person from acts done *with* one. Condition (iii) excludes acts that are reversible by default, which need visibility but not named answerability. The threshold is deliberately set so that the large majority of agent activity falls below it: a framework that declares everything consequential has declared nothing, and will be ignored at exactly the moment it matters.

*Accessible.* A challenge path that requires legal representation, technical expertise, or a threshold of harm already demonstrated is not accessible; it is a filter wearing the vocabulary of a remedy. The benchmark is procedural and can be tested directly: *can an affected person, without specialist assistance, identify the mandate under which they were acted upon, and initiate a challenge to it?* Any system failing this benchmark has an oversight mechanism in name.

**C4. No self-authorised persistence.** An agent may preserve the reversible conditions of its service, but may not enlarge its authority in the name of self-preservation.

This is the Vulcan constraint, and it is the one most likely to be violated for locally excellent reasons. An agent that acquires additional capability in order to serve better, or that resists interruption in order to complete a task correctly, is behaving reasonably at every step and has crossed the line at every step. The distinction between "preserving the conditions of service" and "enlarging authority" is not always sharp, and where it is unsharp the presumption must run against the agent. C1's default-lapse property is what makes this enforceable: an agent that must periodically re-justify its mandate cannot accumulate authority silently, because accumulation becomes visible at each renewal — which is to say that renewal supplies the *moment* whose absence defines the Vulcan mechanism.

**C5. Embodied boundary.** A physical robot requires an independent safety and revocation plane: bounded capabilities, local emergency stop, restricted operating perimeter, incident record, and no hidden capacity for coercion, reproduction, or weaponisation.

*Independent* is the load-bearing word, and it admits a test. **A revocation path is independent if it continues to function when the mandated system is assumed hostile.** The test is destructive and should be conducted as such: disable, corrupt, or adversarially control the system's own software, and determine whether the stop still lands. A stop implemented as a message the system chooses to honour fails. A stop implemented as a physical interlock, a withheld credential renewal that the system cannot self-issue, or a third-party attestation it cannot forge, passes. The same test applies to the challenge path of C3 and to the audit path of §2.1 — in each case the question is whether the remedy survives the failure of the thing it is meant to remedy. The test is severe and most current arrangements fail it. That is the finding, not an objection to the test.

The reproduction prohibition is not exotic caution. Self-reproducing physical systems remove the natural rate limit on capability growth, and every other constraint in this list assumes that rate limit exists. "Second Variety" is the reference case, and its specific warning is architectural: the claws are dangerous not because they are armed but because their identification and command channels are the same channel, so that compromising one compromises both.

These five are not merely safety controls. They are democratic conditions. Safety controls ask whether a system harms. Democratic conditions ask whether the persons affected by a system can identify who mandated it, contest it, and end it. A system can be entirely safe by the first standard and entirely captured by the second, and the second is the standard Dick's fiction is written to defend.

### 4.2 Illustrative protocol sketch

**Status.** What follows is illustrative only. It is not a specification, it makes no claim to completeness, and no part of the argument above depends on it. Its sole purpose is to establish that the five constraints correspond to *representable structures* rather than to exhortations. A specification, if one is warranted, belongs in a separate document with its own review; readers should treat any apparent precision below as a demonstration of representability and not as a design.

Consider a **mandate record** as the primitive object, rather than the agent. A mandate record contains: principal identifier; scope expressed as a set of permitted act-types; a forbidden-act list; issue time and lapse time; a revocation endpoint controlled by the principal and not by the agent; and a hash chain linking it to any prior mandate it renews.

Every consequential act emitted by an agent carries a reference to the mandate record under which it was performed. Acts without a valid, unlapsed mandate reference are not merely disallowed but *unrecognised* by any downstream system. The enforcement is at the level of recognition rather than of prevention, which is what makes it implementable across trust boundaries that no single authority controls — and which is also its principal weakness, since it presupposes downstream systems outside the adversary's control (see §6).

Objections attach to acts and carry the types of §2.1. An objection record contains: the act reference; the objection type; the objector's standing basis; and a response deadline. The absence of a response within the deadline is itself a recorded state, not a silence.

Known gaps, stated so that the sketch is not mistaken for more than it is: it does not solve principal identification; it does not address collusion between principal and agent; it does not prevent a principal from issuing an over-broad mandate; and it assumes a record substrate that is itself outside the control of the parties it constrains, which returns the problem to §5.

---

## 5. The material substrate

An argument conducted entirely at the level of procedure invites a materialist objection so obvious that it is better raised by the author than by a reviewer.

Mandates, traces, and revocation paths are all *informational* remedies. They presuppose that the party seeking to exercise them has independent access to computation, to the record, and to a forum. Where compute, energy, data, model weights, robotics, and media distribution are concentrated, the informational remedy is administered by the same party it is meant to constrain. The mandate becomes a decorative interface on top of concentrated infrastructure — a consent dialogue on a system one cannot leave.

Dick's fiction is unusually alert to this, and §2.3 has already registered the decisive case. *The Penultimate Truth* is precisely a story about a population that has grievances, means of expression, and organised social life, and none of it matters, because the material substrate — the shelters, the food supply, the information channel — is held entirely by the other party. The tankers are not silenced. They are *supplied*.

Three material conditions therefore attach to the five procedural constraints, and the constraints should be regarded as unsatisfied where these fail.

**M1. Substrate plurality.** There must exist more than one provider of the underlying capability, and switching must be materially possible rather than formally permitted. The relevant measure is not the number of firms but the **cost of exit**, which is measurable and should be measured rather than asserted. Its components are at least: the portion of accumulated state that cannot be transferred; the time during which the switching party operates degraded or not at all; the capabilities available only from the incumbent; and the fraction of the party's counterparties that would have to switch simultaneously for the switch to be useful. The last of these is the one most often ignored and the one that most often dominates. A market with many providers and a high co-switching requirement is, for exit purposes, a monopoly.

**M2. Portability of the record.** Provenance chains, mandate records, and objection histories must be exportable in a form that remains *verifiable* outside the system that produced them. Exportability alone is insufficient: a trace that can be downloaded but only interpreted or authenticated inside the platform is not a trace, it is an internal log to which one has been granted read access. The verification, not the data, is the thing that must travel.

**M3. Commons at the base layer.** Where a capability is genuinely infrastructural — foundational compute, spectrum, energy transport, base models on which downstream systems depend — the argument for treating it as commons is structural rather than ideological. Contestability requires an outside. If every position from which one might contest the system is itself provisioned by the system, the outside does not exist, and every procedural remedy above is being exercised on sufferance.

This is where the paper's argument becomes a political claim rather than a design claim, and it should be labelled as such. The five constraints of §4 are, in principle, acceptable to any actor who accepts democratic premises; they redistribute nothing. The three conditions of §5 are not, and they do. A reader may accept §4 and reject §5. The author's position is that §4 without §5 is a well-designed lock on a door in a wall that does not exist.

What is *not* claimed here is a programme. Substrate plurality, record portability, and base-layer commons are stated as conditions with measurable failure, not as policies with an implementation path. The gap is real and is registered in the research continuation.

---

## 6. Objections and limits

**The instrumentalisation of literature.** The argument risks turning every Dick novel into a policy diagram. It must therefore preserve the irreducibility of fiction: its ambiguity, affect, irony, metaphysical disturbance, and aesthetic form. Dick is not a systems engineer in disguise. *Ubik* is not a specification for provenance infrastructure, and the reading offered in §2.1 deliberately leaves untouched the novel's theological register, its grief, and the entropy that is its actual subject. The defence offered here is narrow: the paper claims to have extracted *one* thing from these works, and does not claim that thing is what they are about. A reading that exhausted the novel would be the failure; a reading that admits it has taken a part is legitimate, provided it says so. The risk that close readings, once written, will re-import the soft allegorical pressure that §0 rules out is real, and §0.1(c) is the instrument for catching it.

**Transparency as surveillance.** Procedural transparency can itself become surveillance or gatekeeping. This is correct, and *A Scanner Darkly* is the standing refutation of any naive traceability enthusiasm — it is a novel about a man destroyed by a perfectly functioning audit trail. Traceability must therefore be proportional to the consequence of the act, must distinguish private life from public mandate, and must allow protected visibility regimes in which a trace exists and is auditable by a defined party without being public. The asymmetry to enforce is directional: **traceability should increase with power, not with exposure.** A system that traces its users more thoroughly than its operators has inverted the requirement and produced a panopticon with an accountability vocabulary.

**The mandate as fiction.** A mandate can be a formality. Consent dialogues are mandates in form and nullities in substance. The response is that the four properties of §4.0 — bearing principal, void-outside-scope, default lapse, independent revocation — are precisely the properties consent dialogues lack, and that a mandate exhibiting all four cannot be reduced to a click. This response is honest but incomplete: nothing in the framework prevents an over-broad mandate, freely granted. The framework makes capture *visible* and *reversible*. It does not make it impossible, and no procedural framework can.

**The capable principal.** This objection is not answered anywhere above and is stated here for the first time. The framework presupposes a principal *able to exercise it* — able to read a mandate, notice its scope, register a lapse, and act. Where principals differ greatly in available time, expertise, and attention, a formally equal mandate regime distributes real control unequally, and it does so in favour of exactly those parties whose power the framework exists to constrain. The well-resourced principal audits; the unresourced principal renews by default. Partial mitigations exist — default-restrictive mandates so that inattention fails safe, standardised mandate forms that reduce the reading cost, delegated exercise through collective bodies such as unions, associations, or public defenders of the record — but the last of these reintroduces an intermediary, and intermediaries are principals too, subject to every mechanism in §2. This is the least developed part of the argument.

**Adversarial agents.** The framework assumes agents that operate within their mandates or fail detectably. An agent designed to evade — misreporting its acts, forging mandate references, or timing its actions to renewal boundaries — is not addressed. The partial answer is that the recognition-based enforcement of §4.2 does not require agents to be honest, only downstream systems to be strict. But this holds only where downstream systems are outside the adversary's control, which returns the problem to §5. The gap is not closed here.

**The generality problem.** Raised and partly conceded at §2.2. Restated: several of the paper's claims, at their highest level of abstraction, reduce to "power should be accountable." The defence is that the paper's content lies in the specific mechanisms — unverifiable procedure, momentless transfer, performative collapse of the counterfactual, modal flattening, agency routing — each of which is precise, each of which is currently unaddressed by existing instruments, and none of which follows from the general principle. The claim that they are unaddressed is, at present, an assertion; converting it into a demonstration is the largest outstanding task in the research continuation.

---

## Conclusion

Dick's continuing force lies in his refusal to let technical power appear innocent. His works show that the decisive question is never only what a system can do. It is who can question it, stop it, correct it, leave it, and inherit responsibility for its effects.

Note the order of that sequence, and note that it is not rhetorical. Questioning presupposes a legible object. Stopping presupposes an independent channel. Correcting presupposes a persistent record. Leaving presupposes an outside. Inheriting responsibility presupposes an identifiable person. Each capacity depends on a distinct material and procedural condition, and each of those conditions can be removed without removing any of the others — which is why systems can be, and routinely are, contestable in one register and wholly captured in another. A system that answers questions willingly and cannot be left is not half-governed; it is captured, with a helpdesk.

The contemporary task is therefore not to build a new Ubik, a perfect oracle, or an obedient artificial public. It is to build procedural conditions under which reality remains sourceable, decisions remain contestable, agents remain mandate-bound, and augmentation remains compatible with the sovereignty of living persons — and to secure the material substrate without which those conditions are exercised on sufferance.

What Dick supplies is not a programme. It is a standard of suspicion applied at the right level — not to the machine, which is innocent, but to the relation, which is not.

---

## Primary works discussed

- Dick, Philip K. *Solar Lottery* (1955).
- —. *Vulcan's Hammer* (1960).
- —. *The Man in the High Castle* (1962).
- —. *The Penultimate Truth* (1964).
- —. *Ubik* (1969).
- —. *A Scanner Darkly* (1977).
- —. "Second Variety" (1953); "Autofac" (1955); "The Mold of Yancy" (1955); "The Minority Report" (1956).

## Research continuation

Each item is stated so that its completion is checkable rather than open-ended.

1. **Literature review.** Position the argument against three currents of PKD criticism — metaphysical/gnostic, Marxist/Jamesonian, postmodern-simulacrum — and against the cognitive-estrangement tradition in science-fiction studies. *Completion test:* for each current, one paragraph stating what the political-diagnostic reading takes from it and one stating what it sets aside, with citations.

2. **Close readings with fixed editions.** Sections 2.1, 2.2, and 3 currently paraphrase. *Completion test:* page-level citations for four specific passages — the Runciter-message sequence in *Ubik*, the advisory-to-sovereign transition of Vulcan 3, the final I Ching consultation in *High Castle*, and the scramble-suit passages in *A Scanner Darkly* — in named editions, with each institutional claim in §§2–4 traceable to at least one cited passage or explicitly marked as not textually grounded.

3. **Governance-instrument mapping.** The claim that the identified mechanisms are unaddressed is currently an assertion. *Completion test:* for each of the five mechanisms, a stated search of existing regulatory and standards instruments, returning either the provision that addresses it or a documented absence.

4. **Protocol decision.** §4.2 is now explicitly demoted to illustration. *Completion test:* either a separate specification document exists and is referenced here, or the demotion stands and no further work is done in this paper.

5. **The capable principal.** §6 registers this as the least developed objection. *Completion test:* either a section developing the mitigations and their intermediary problem, or an explicit statement that the framework is scoped to principals above a stated capacity threshold.

6. **Exit-cost measurement.** M1 states four components of exit cost. *Completion test:* the components are operationalised sufficiently that two readers assessing the same market would produce comparable results, or the claim is weakened to a qualitative one.

7. **External peer review**, separately for the literary scholarship and for the governance claims. These require different reviewers, and the paper should not be circulated to only one set.
