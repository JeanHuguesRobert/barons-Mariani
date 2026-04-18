# The Generalized Tocqueville Law: Progress, Rising Expectations, and the Structural Production of Dissatisfaction

**Jean Hugues Noël Robert**  
Institut Mariani R&D / C.O.R.S.I.C.A. — 1 cours Paoli, F-20250 Corte, Corsica  
jhr@baronsmariani.org

*Working paper. First posted: Les Carnets du Baron Mariani (Substack), 17 October 2025. This version: April 2026.*

---

**Abstract**

Across technologically advanced societies, objective improvements in safety, institutional quality, and material welfare have paradoxically coincided with intensifying perceptions of crisis, injustice, and systemic failure. This paper formalises a structural mechanism — the *Generalized Tocqueville Law* — that accounts for this counterintuitive dynamic. Building on Tocqueville's original intuition regarding the French Revolution, and on subsequent sociological work on relative deprivation (Runciman, 1966; Gurr, 1970), reference groups (Merton, 1968), and political mobilisation (Boudon, 1977; Davies, 1962), we argue that progress systematically shifts tolerance thresholds, elevates normative horizons, amplifies relative frustration, and produces structural amnesia about prior gains. The paper's central formal contribution is a *perceived severity index* S(t) = Δ(t)/(1 − Q(t)) — the residual deficit measured relative to the remaining distance to perfection — which is shown to increase monotonically under a tractable parametric family of threshold functions, even as the absolute deficit Δ(t) narrows. This formalises Tocqueville's claim that "sensibility grows keener even as the evil diminishes" in mathematically precise terms. The law is illustrated through three extended case studies chosen from analytically distinct domains: (1) high-reliability technical systems; (2) digital content moderation, where the 160-fold increase in NCMEC CyberTipline reports between 2010 and 2023 reflects improved detection rather than increasing harm; and (3) Corsican nationalist mobilisation. Theoretical scope conditions — specifying when the mechanism does *not* activate — are developed, rendering the law falsifiable. The paper concludes with institutional implications and a research agenda.

**Keywords:** Tocqueville effect · relative deprivation · rising expectations · tolerance threshold · perceived severity · political mobilisation · content moderation · high-reliability systems · Easterlin paradox

**Word count:** approximately 11,400 (main text and notes, excluding references and appendix).

---

## 1. Introduction: A Universal Paradox

Contemporary societies face an arresting paradox. By virtually every objective measure — infant mortality, life expectancy, per-capita income, the frequency of inter-state war, the proportion of populations living under democratic government — the present era represents a historical peak of material and institutional progress. And yet surveys of subjective wellbeing across advanced democracies consistently reveal declining institutional trust, rising anxiety, and an intensifying sense that things are going fundamentally wrong (Dalton, 2004; Norris and Inglehart, 2019). Citizens of the safest societies in recorded history regard their lives as more precarious than their grandparents did. Populations enjoying the greatest political freedoms report unprecedented levels of alienation from democratic institutions.

This is not a superficial or ephemeral phenomenon attributable to media distortion or individual irrationality. It reflects a deep structural mechanism: one identified, in embryonic form, by Alexis de Tocqueville in the nineteenth century, but whose full generality has not been systematically developed in the sociological literature. We call this mechanism the **Generalized Tocqueville Law** and define it as follows:

> *In any progressing society, the perception of residual defects grows faster than their objective reduction, because expectations rise and tolerance declines in proportion to demonstrated improvement.*

The implications are wide-ranging. This law explains why the fortyfold improvement in aviation safety since 1970 has been accompanied by an approximately tenfold increase in aviation safety regulation (Figure 1). It explains why the exponential improvement of automated content moderation — Meta's systems now detect 97% of violating content before any user report — has produced a 160-fold increase in CyberTipline reports and the most demanding regulatory framework in the history of the internet (Figure 2). It explains why progressive institutional accommodations of national minorities intensify rather than pacify political mobilisation. In each domain, objective progress does not eliminate the problem — it transforms it, relocating the threshold of the intolerable and ensuring that a new frontier of legitimate grievance is always available.

The paper's central formal contribution is the introduction of the **perceived severity index** S(t) = Δ(t)/(1 − Q(t)), where Δ(t) = τ(t) − Q(t) is the absolute deficit between the tolerance threshold and objective quality. S(t) measures not how large the deficit is, but what fraction of the remaining distance to perfection it represents. Under the conditions specified in Section 3 and Appendix A, S(t) increases monotonically as Q(t) rises — providing mathematical content to Tocqueville's observation that "sensibility grows keener even as the evil diminishes" (Figure 3).

The paper proceeds as follows. Section 2 traces the theoretical genealogy. Section 3 formalises the law and its four mechanisms. Sections 4, 5, and 6 develop three case studies. Section 7 discusses scope conditions and normative implications. Section 8 concludes. Appendix A provides the mathematical derivation.

---

## 2. Theoretical Genealogy and Literature

### 2.1 The Tocquevillean Intuition

In *L'Ancien Régime et la Révolution* (1856), Tocqueville confronted a puzzle that had troubled every analyst of the French Revolution: why did the most transformative revolution in European history erupt not under the most oppressive regime but under one actively engaged in reform? His answer centred on the perceptual effects of improvement itself:

> "The suffering that is endured patiently as inevitable becomes intolerable the moment the idea of escaping it crosses one's mind. Every abuse then removed seems only to lay bare those that remain, and to make them more galling; the evil has lessened, it is true, but sensibility has grown keener."[^1]

In *Democracy in America* (1835), he extended this analysis to social equality:

> "When inequality is the common law of a society, the most striking inequalities do not catch the eye; but when everything is more or less level, the slightest gap is offensive."[^2]

These observations remained embedded within Tocqueville's broader political sociology and were not theorised as a general structural law applicable across domains.

### 2.2 Relative Deprivation, Reference Groups, and the J-Curve

The concept of *relative deprivation*, introduced by Stouffer et al. (1949), was developed into a general theory of political discontent by Runciman (1966) and Gurr (1970). Runciman's central contribution was to distinguish egotistical relative deprivation (comparing one's own past and present situations) from fraternalistic relative deprivation (comparing one's group to a reference group). Both forms share the Tocquevillean structure: what provokes grievance is not absolute deprivation but the gap between a perceived entitlement and an actual state.

Gurr's (1970) *Why Men Rebel* formalised this as a causal model linking political violence to the gap between value expectations and value capabilities. Crucially, Gurr identified *progressive* relative deprivation — where rising expectations permanently outpace improvements in capability — as a major pathway to collective discontent. Davies's (1962) J-curve theory focuses on the acute case where rising expectations are interrupted by objective deterioration.[^3] In our framework, the J-curve is a special case; the mechanism we identify is chronic and does not require any objective reversal.

The present paper's contribution relative to Gurr is threefold: (1) extension to domains where political violence is irrelevant; (2) decomposition into four analytically distinct mechanisms; (3) introduction of a formal index — S(t) — that specifies precisely when and why perceived severity increases, rendering the law falsifiable in a way Gurr's framework is not.

Merton's (1968) analysis of reference groups adds a crucial dimension: progress expands the horizon of available reference groups, continuously renewing the supply of unfavourable comparisons. The parallel literature on the *hedonic treadmill* (Brickman and Campbell, 1971) and the Easterlin paradox (Easterlin, 1974) documents the same mechanism at the individual psychological level: rising income does not produce lasting increases in reported happiness because aspirations adapt upward at a comparable rate (Figure 5). The Generalized Tocqueville Law is mechanistically homologous but analytically distinct: the hedonic treadmill is an intra-individual aspiration process; the law describes collective normative recalibration, governed by social comparison, institutional dynamics, and the logic of rights and recognition rather than by hedonic psychology alone.

### 2.3 Political Mobilisation and the Paradox of Reform

Raymond Boudon (1977) formalised what he termed the *loi tocquevillienne de la mobilisation politique*: the objective improvement of a condition can facilitate the expression of discontent rather than allay it. Hirschman's (1991) perversity thesis offers a structural parallel: reform efforts frequently produce consequences that undermine their own stated objectives. The present paper's contribution is to provide a unified mechanism — with four named components and a formal index — that subsumes these observations and extends them beyond their original domains.

---

## 3. The Generalized Tocqueville Law: Formal Statement

### 3.1 Formulation

Let Q(t) ∈ (0, 1) denote an objective quality indicator at time t (safety, equality, moderation accuracy, institutional responsiveness), increasing continuously with dQ/dt > 0. Let τ(t) ∈ (0, 1) denote the socially constructed *tolerance threshold* below which outcomes are deemed unacceptable. The Generalized Tocqueville Law states:

    dτ/dt > 0  whenever  dQ/dt > 0

The *absolute deficit* Δ(t) = τ(t) − Q(t) need not converge to zero as Q(t) → 1, because τ(t) co-evolves with Q(t). Two structural properties characterise this co-evolution.

**Ratchet asymmetry.** Tolerance thresholds adjust upward in response to improving quality but rarely descend when quality deteriorates. Once a norm of near-perfect aviation safety is established, it cannot be unestablished by returning to a higher accident rate.

**Convexity near the ceiling.** As Q approaches 1, normative pressure accelerates: the demonstrated proximity of perfection makes each remaining increment of demonstrated improvement generate disproportionately large normative demand. This is formalised in Appendix A.

### 3.2 The Perceived Severity Index

The paper introduces:

    S(t) = Δ(t) / (1 − Q(t))

S(t) measures the deficit relative to the remaining distance to perfection — the fraction of residual imperfection that falls within the zone of socially unacceptable performance. **Proposition A.1** (Appendix A) establishes that under the parametric family τ = g(Q) = 1 − (1 − Q)^γ with γ > 1, S(Q) = 1 − (1 − Q)^(γ−1) is strictly increasing on (0, 1), with S → 1 as Q → 1.

The interpretation is precise: as quality approaches perfection, virtually all remaining imperfection falls within the zone of legitimate intolerance. Even near-perfect systems are experienced as failing — not because they are objectively poor, but because the tolerance threshold has moved so close to the ceiling that the residual gap is perceived as entirely avoidable and therefore entirely unacceptable. Figure 3 illustrates this co-evolution.

### 3.3 Mechanism 1 — Tolerance Threshold Displacement

What was acceptable, even invisible, in a context of widespread imperfection becomes intolerable when that imperfection becomes exceptional. Tolerance is calibrated against the perceived norm of what is achievable. As the norm shifts upward, the threshold of the intolerable shifts with it. This mechanism operates at the level of *social norms*, not individual psychology: societies collectively redefine acceptable performance through law, journalism, regulatory practice, and political discourse.

### 3.4 Mechanism 2 — Normative Horizon Elevation

Progress does not merely improve existing conditions; it produces evidence that further improvement is achievable, and therefore legitimate to demand. Each advance narrows the frontier between the real and the possible. The residual imperfection, however statistically small, ceases to be merely unfortunate — it becomes scandalous, because demonstrably avoidable. This mechanism has a self-propelling, logically grounded character: the demand for zero aircraft fatalities is irrational only if zero fatalities is impossible; each decade's progress weakens the plausibility of that assumption.

### 3.5 Mechanism 3 — Relative Frustration

Individuals and groups do not compare their current situation to their historical baseline but to what they regard as *reasonably attainable* in the present context. As opportunities expand, the psychological weight of the remaining gap intensifies: the absolute distance shrinks, but the experienced distance grows. This asymmetry is amplified by the implicit contracts that reliable systems generate: when a system performs well 999 times out of 1,000, the hundredth failure is processed not as statistical inevitability but as breach of an assumed obligation.

### 3.6 Mechanism 4 — Structural Amnesia of Gains

Acquired progress becomes invisible by becoming normal. Each generation inherits a world it did not build and perceives its features as givens rather than achievements. The *costs* of achieving the current baseline disappear from social memory. The residual distance to perfection is therefore perceived without reference to the difficulty of traversing it, systematically inflating frustration relative to what historically calibrated expectations would generate.

### 3.7 The Combined Effect

These four mechanisms are mutually reinforcing, as illustrated schematically in Figure 4. Threshold displacement creates the social norm against which frustration is measured. Horizon elevation defines the new target. Relative frustration converts the gap into experienced dissatisfaction. Structural amnesia removes the historical context that would moderate the response. Together, they constitute a structural generator of dissatisfaction endogenous to progress: the more a society improves, the more effectively it produces the experiential and normative conditions for perceiving itself as failing.

---

## 4. Case Study I — Technical Reliability and the Intolerance of Residual Failure

### 4.1 The Observable Paradox

Commercial aviation in 2022 recorded approximately 0.07 fatal accidents per million flight sectors, a roughly fortyfold improvement over 1970 figures.[^4] Surgical mortality in high-income countries has fallen from around 10% at the beginning of the twentieth century to below 0.5% for most procedures today. And yet social, legal, and regulatory responses to technical failure have grown continuously more intense. Figure 1 displays the two trajectories in parallel: as the accident rate declined fortyfold, regulatory output approximately tenfold increased. A single aircraft accident now triggers global media coverage, exhaustive regulatory review, and significant legislative action. Medical error has generated a judicialisation of clinical practice so extensive that many practitioners describe conditions of *defensive medicine* that actively compromise care quality (Kessler and McClellan, 1996).[^5]

### 4.2 Application of the Four Mechanisms

**Threshold displacement.** In 1900, a railway disaster killing fifty people was a tragedy but a contextually expected one. Today, a single aircraft accident is processed as an exceptional, almost incomprehensible event, generating a response wildly disproportionate in statistical terms to the marginal contribution of any single accident to overall mortality risk. Technical death has become *abnormal*, and abnormal events demand accountability in ways that statistically comparable mortality from chronic causes does not.

**Horizon elevation.** The demonstrated achievement of 99.93% reliability generates not satisfaction but the demand for 99.99%. This is a rational inference from evidence that improvement is technically achievable. Each increment of demonstrated progress narrows the perceived gap between the actual and the theoretically possible, making the remaining distance more morally salient.

**Relative frustration.** Users compare their experience not to their grandparents who accepted train derailments but to their own recent experience, in which the system performed reliably on the previous ninety-nine occasions. The hundredth failure is processed as breach of contract. The psychological violation is proportional to the preceding reliability, not to the absolute failure rate.

**Structural amnesia.** No one awakens grateful that civil aviation has eliminated 97% of its 1970 fatal accident rate. That reduction is invisible. What is visible is the one accident that occurred.

### 4.3 Systemic Consequences

These mechanisms jointly produce: regulatory ratcheting (each accident triggers new regulation regardless of marginal safety benefit); accountability paralysis (decision-making migrates toward legally protective processes at the expense of operational competence); and disproportionate media amplification (a single spectacular failure carries more political weight than thousands of successful operations).

---

## 5. Case Study II — Digital Content Moderation and the Escalation Paradox

### 5.1 The Context

Digital platforms provide a uniquely well-documented and temporally compressed observation of the Generalized Tocqueville Law: decades of normative evolution compressed into years, with quantitative data unavailable in most sociological domains. The arc is consistent across platforms: sustained, technically impressive improvement in moderation accuracy has produced not diminishing regulatory pressure but escalating demand, intensifying public outrage, and a normative horizon that continuously outruns demonstrated capability.

### 5.2 The Empirical Record

Meta's transparency reports document that by 2023, automated systems were identifying and removing approximately 97% of violating content before any user report was filed (Meta, 2023). YouTube removed 7.2 million videos for policy violations in Q4 2022 alone, with the large majority detected automatically (YouTube, 2023). On CSAM specifically, the NCMEC CyberTipline received 36.2 million reports in 2023, compared to 223,374 in 2010 (NCMEC, 2024) — a 160-fold increase driven primarily by improved automated detection, not by a proportional increase in underlying harm.[^6]

Figure 2 makes the paradox visually immediate: both the detection rate and the volume of reported harm rise in parallel. The 160-fold increase in CyberTipline reports reflects the introduction of PhotoDNA (2009) and successive generations of hash-matching and AI detection — technology that made previously invisible violations visible. The objective situation improved substantially; the perceived situation moved in the opposite direction.

The institutional response tracked the perceived deterioration rather than the objective improvement. The EU Digital Services Act (2023), enacted at a moment when platform moderation capabilities had never been stronger, imposes obligations that do not specify acceptable harm rates but require *continuous reduction of systemic risk* — a structurally open-ended requirement.[^7] Platforms' Trust and Safety workforce grew from negligible in 2010 to an estimated 100,000+ globally by 2020, while regulatory scrutiny intensified continuously. Meta reportedly spent approximately $5 billion on safety and security in 2022 while simultaneously facing its most intense regulatory challenge in the company's history.

### 5.3 Application of the Four Mechanisms

**Threshold displacement.** The internet of 2005–2010 contained vast quantities of content that would today be considered self-evidently unacceptable. As platforms progressively removed the most egregious material, the normative baseline shifted accordingly. Content invisible against the background noise of 2010 is conspicuous against 2023's substantially cleaner environment.

**Horizon elevation.** The detection of 97% of violating content does not produce satisfaction; it produces: "if 97% is achievable, why not 99%? What is the acceptable explanation for the 3%?" The DSA's systemic risk framework institutionalises this horizon precisely: there is always a further systemic risk to be assessed. A further dimension: once one platform demonstrates a moderation capability, that capability becomes the normative baseline for all platforms. Improvement of the best actors continuously raises the standard against which all are evaluated.

**Relative frustration.** Platform users process harmful content encounters not against the pre-moderation baseline but against an implicit expectation of safety reinforced by terms of service, safety marketing, and millions of preceding unproblematic interactions. Advertisers' rapid withdrawal at the first sign of brand adjacency to harmful content reflects the same structure: the implicit contract of brand-safe environments, once established, generates zero tolerance for its violation.

**Structural amnesia.** The sustained effort — technical, financial, organisational — that produced current capabilities is invisible. The asymmetry is amplified by news media, which covers moderation failures and not successes, and by platform critics whose professional activity requires continuous identification of failures.

### 5.4 The Adversarial Amplifier

Content moderation presents a structural feature absent from the aviation and Corsica cases: the supply of violating content responds strategically to moderation improvement. As detection of one category improves, producers adapt — shifting to new formats, platforms, obfuscation techniques. The perceived deficit Δ(t) is therefore sustained by two independent forces: upward pressure on τ(t) through the Tocqueville mechanisms, and adversarial maintenance of Q(t) below τ(t) through strategic adaptation. This makes digital content moderation an especially resistant domain for closing the perceived gap, and a particularly important domain for the policy implications discussed in Section 7.

### 5.5 The Regulatory Ratchet

The Generalized Tocqueville Law predicts a specific institutional dynamic: each regulatory response to a perceived moderation failure raises the normative bar, generating new categories of unacceptable residual harm whose boundary shifts continuously upward regardless of actual harm rates. The DSA's systemic risk framework instantiates this precisely: by construction, it cannot be fully satisfied. This dynamic has a direct structural parallel with regulatory ratcheting in aviation and medicine, with one important difference: the speed of the feedback loop compresses from years (aviation: accident → investigation → regulation) to weeks (digital: incident → virality → parliamentary question → regulatory proposal → implementation). The mechanism is the same; the tempo makes its structure more legible.

---

## 6. Case Study III — Corsica and the Dynamics of Progressive Recognition

### 6.1 The Observable Paradox

Since its annexation by France in 1769, Corsica has experienced a trajectory of progressive institutional accommodation: from departmentalisation, through the creation of a special regional statute in 1982, to the establishment of a Collectivité de Corse with significantly expanded powers in 2018. Simultaneously, the French state has extended substantial fiscal transfers and progressively reduced the historical suppression of the Corsican language. By any historical benchmark, the institutional situation of Corsica within the French Republic has improved substantially.

And yet, far from moderating, Corsican nationalist mobilisation has intensified. The 2021 territorial elections saw nationalist parties obtain approximately 68% of seats in the Assemblée de Corse, up from under 30% in the early 1990s.[^8] Demands have escalated from administrative autonomy to linguistic co-officiality to constitutional recognition to, in some currents, full independence. The more France has conceded, the more the demand has grown.

### 6.2 The Mutual Incomprehension

This trajectory generates symmetrical incomprehension: from the metropolitan perspective, extensive concessions have been made and further demands seem ungrateful; from the Corsican nationalist perspective, each concession validates the principle of distinct identity requiring distinct treatment, making the partiality of recognition a sign of bad faith rather than progressive good will. Neither reading is accurate. Both are predictable consequences of the structural mechanism.

### 6.3 Application of the Four Mechanisms

**Threshold displacement.** In the nineteenth century, Corsica experienced comprehensive cultural and linguistic suppression — domination so total that it was either passively endured or contested through sporadic revolt. Today, because formal equality has substantially advanced, the asymmetries that persist are conspicuous against a background of partial recognition in precisely the way they were not conspicuous against total suppression. That structural economic decisions are made in Paris, that land markets are dominated by mainland capital, that constitutional recognition has been repeatedly blocked — these residual asymmetries are now psychologically and politically intolerable in ways structurally produced by the progress that preceded them.

**Horizon elevation.** Each institutional concession has not extinguished the nationalist demand but legitimised and elevated it. By granting a special statute, the state implicitly acknowledged that Corsica is not a region *comme les autres*, validating the premise that generates the demand for the next step. Recognition is not a point on a scale but a recursive process: each act of recognition generates a new plane on which its adequacy can be questioned.

**Relative frustration.** Contemporary Corsican nationalists compare their situation not to 1850 but to an ideal of self-determination that the process of recognition has rendered imaginable and legitimate, and to comparable territories — Scotland, the Faroe Islands, the Åland Islands — that have achieved or are pursuing higher degrees of autonomy.[^9] Rising education levels in Corsica have simultaneously produced a politically articulate civil society capable of sustaining and elaborating these comparative claims.

**Structural amnesia.** For the generation of Corsicans who came of age after the 1982 statute, its features are not experienced as hard-won concessions but as the baseline from which further demands are legitimately made.

### 6.4 Comparative Evidence

The generality of this dynamic is confirmed by parallel trajectories. In Scotland, the devolution settlement of 1999 provided the institutional infrastructure within which independence sentiment could be more effectively organised, culminating in the 2014 referendum and sustained majority support for independence in subsequent polling. In Catalonia, successive statutes of autonomy since 1979 paradoxically strengthened rather than moderated the independence movement. In Quebec, the recognition of French and the expansion of provincial powers provided the institutional base from which two referendums were conducted. In each case: institutional progress validates the legitimacy of the underlying claim, elevates the normative horizon, and generates a new threshold of intolerable inadequacy. This is not a pathology specific to any of these communities; it is a universal property of recognition processes in diverse states.

---

## 7. Discussion: Scope Conditions, Falsifiability, and Normative Implications

### 7.1 When Does the Law Not Activate? Towards a Null Model

Three conditions appear necessary for the mechanism to activate, each generating a falsifiable prediction:

**Condition 1: Reflexive awareness of progress.** The mechanism requires that actors can know that things have improved and interpret improvement as evidence of further possibility. *Prediction:* expectation adjustment should be weaker in domains where progress is poorly communicated or attributed to uncontrollable factors. *Test:* compare the intolerance of residual failure in transparent versus opaque systems holding objective performance constant.

**Condition 2: Availability of comparison reference groups.** The relative frustration mechanism requires salient comparison reference points. *Prediction:* the mechanism should be weaker in societies with low international connectivity. *Test:* cross-national comparison of expectation adjustment rates controlling for media exposure and educational attainment.

**Condition 3: Sufficient organisational capacity for demand articulation.** *Prediction:* the mechanism should be stronger in societies with high civil society density, press freedom, and legal infrastructure — precisely the conditions under which the paradox is most observed. *Test:* within-country comparison of the mechanism's intensity across periods of civil society expansion and contraction.

**Candidate counter-examples.** The *Trente Glorieuses* (1945–1975) saw intense economic progress accompanied by rising rather than falling institutional trust in most Western European societies. Several factors are consistent with our framework: the Cold War threat may have suppressed the relative frustration mechanism through a unifying external reference point; the postwar social contract explicitly connected progress to institutional agency, moderating structural amnesia; and the pace of improvement may have temporarily exceeded the pace of expectation adjustment. The Botswana case (rapid development 1990–2010 without social explosion) similarly suggests that the speed of improvement relative to expectation adjustment is a relevant parameter. These are scope conditions to be specified, not refutations.

### 7.2 What the Law Does Not Claim

The law is not a critique of progress. The fact that rising expectations accompany improving safety does not make improved safety undesirable — it means the systemic consequences of the accompanying expectation dynamics must be managed. The law is not an argument for the status quo: dissatisfaction generated by progress typically represents an upward displacement of the threshold of the intolerable, which is a form of social improvement even when it produces political turbulence. The law is not a psychological claim about ingratitude or irrationality; it describes a structural dynamic that operates independently of individual motivations. And it is not fatalistic: identifying the mechanism enables its management.

### 7.3 Productive versus Pathological Dissatisfaction

Not all instantiations of the mechanism are equivalent. Dissatisfaction that drives further improvement toward a genuinely achievable standard through viable institutional pathways is *productive* — it is the motive force Tocqueville identified as the cognitive structure of agency. Dissatisfaction that generates regulatory paralysis, zero-sum political conflict, or resource misallocation without viable resolution is *pathological*. The distinction turns on whether the normative horizon elevation is connected to achievable institutional pathways. Governance that manages this distinction — fostering productive dissatisfaction while attenuating pathological expressions — is the institutional challenge that the law identifies.

### 7.4 Towards Institutional Regulation

**Historical accounting as a public good.** Structural amnesia is partially counteracted by systematic public accounting of progress. Regulatory agencies and democratic governments that routinely publicise progress data alongside deficit data provide a cognitive corrective. This is not manufactured gratitude; it is calibrated information that enables calibrated expectations.

**Transparency about feasibility constraints.** Users who understand why zero-defect is not achievable — because of irreducible stochasticity, resource constraints, or adversarial dynamics — calibrate expectations accordingly. Opacity amplifies frustration; transparency moderates it.

**Explicit acknowledgement in political negotiations.** In minority recognition contexts, agreeing explicitly that each concession will predictably generate further demand is not a reason to withhold concessions — it is a precondition for planning a viable long-term institutional trajectory rather than engaging in cycles of reactive concession and renewed escalation.

**Long-horizon institutional design.** Governance requires planning not for the resolution of the current demand but for the predictable trajectory of demands that progress will generate. This is a structural challenge for democratic institutions with short electoral cycles, but one whose origin the law identifies precisely.

---

## 8. Conclusion: Progress as Transformation, Not Resolution

The Generalized Tocqueville Law invites a fundamental reconceptualisation of the relationship between objective improvement and subjective satisfaction. Progress is not a linear trajectory from imperfection to perfection. It is a dialectical process in which the resolution of one order of problem systematically generates a new order of problem — not by failure, but by success.

The paper's three case studies were chosen to illustrate the law's operation across analytically distinct domains: a physical infrastructure subject to irreducible stochastic failure (aviation/medicine); a sociotechnical system subject to adversarial dynamics (digital platforms); and a political recognition process subject to the recursive logic of identity claims (Corsica). The consistency of the mechanism across these domains is the primary evidence for its generality.

The introduction of the perceived severity index S(t) = Δ(t)/(1 − Q(t)) provides this generality with formal content. Appendix A shows that under a tractable parametric family of threshold functions, S(t) increases monotonically as quality approaches perfection — formalising Tocqueville's "keener sensibility" and providing a testable prediction that distinguishes the law from generic claims about rising expectations.

The Tocquevillean insight — that the suffering borne patiently as inevitable becomes intolerable at the moment that escape is conceived — is not a counsel of despair. It is a description of the cognitive structure of agency. The moment a society conceives of escaping a condition, it has already partially escaped it. The intolerance that follows is not an obstacle to further improvement but its primary motive force. What the Generalized Tocqueville Law adds is the recognition that this motive force is structural, permanent, and universal — and that its management, rather than its elimination, is what governance in progressive societies fundamentally requires.

---

## Notes

[^1]: Original French: *"Le mal qu'on souffrait patiemment comme inévitable semble insupportable dès qu'on conçoit l'idée de s'y soustraire. Tout ce qu'on ôte alors des abus semble mieux découvrir ce qui en reste et en rend le sentiment plus cuisant : le mal est devenu moindre, il est vrai, mais la sensibilité est plus vive."* Tocqueville (1856), p. 223.

[^2]: Original French: *"Quand l'inégalité est la loi commune d'une société, les plus fortes inégalités ne frappent point l'œil ; quand tout est à peu près de niveau, les moindres le blessent."* Tocqueville (1835), vol. II, p. 254.

[^3]: Davies's J-curve model predicts that revolutions are most likely when a prolonged period of objective development is followed by a sharp reversal, creating a rapidly widening gap between expectations and reality (Davies, 1962, p. 6).

[^4]: Data from IATA Safety Report series and Boeing's *Statistical Summary of Commercial Jet Airplane Accidents* (2023 edition). The figure of approximately 0.07 fatal accidents per million flight sectors in 2022 compares to roughly 3 per million in 1970.

[^5]: On the judicialisation of medicine, see also Mello et al. (2010), who estimate the US medical liability system's total annual cost at approximately $55.6 billion, including defensive practice costs that exceed direct liability costs.

[^6]: NCMEC CyberTipline 2023 Report. The 2010 figure is from NCMEC's annual statistics archive. The majority of 2023 reports were generated by platform automated detection, not user complaints.

[^7]: The Digital Services Act (Regulation (EU) 2022/2065) entered into force 16 November 2022, applicable to VLOPs from August 2023.

[^8]: Official results from the *Ministère de l'Intérieur*, elections to the Assemblée de Corse, 2021.

[^9]: On the Scottish trajectory, see Keating (2001) and Curtice (2023). Scotland's 2014 referendum returned 45% in favour of independence; subsequent polling has consistently shown majority support.

---

## Acknowledgements

The author used Claude (Anthropic, Sonnet 4.x) as a research assistant for structural editing, critical review, bibliographic suggestion, and development of the mathematical formalisation in Appendix A. All intellectual responsibility for arguments, claims, and conclusions remains with the author.

The Corsican case study (Section 6) draws on research conducted independently of the author's candidacy for the French Senate (Haute-Corse, September 2026). Its initial formulation was published in *Les Carnets du Baron Mariani* (Substack) on 17 October 2025, prior to and independently of that candidacy. The author declares this potential conflict of interest in full.

---

## Appendix A: Mathematical Properties of the Perceived Severity Index

### A.1 Setup

Let Q ∈ (0, 1) denote objective quality, and let τ = g(Q) denote the socially constructed tolerance threshold, where g : (0,1) → (0,1) satisfies:

- **(A1)** g(Q) > Q for all Q ∈ (0, 1)  *(the threshold exceeds current quality)*
- **(A2)** g(0) = 0, g(1) = 1  *(boundary conditions)*

The absolute deficit is Δ(Q) = g(Q) − Q, and the perceived severity index is S(Q) = Δ(Q)/(1 − Q).

### A.2 The Power Transformation Family

Consider the parametric family:

    g(Q) = 1 − (1 − Q)^γ,   γ > 1

**Verification of A1 and A2.** For γ > 1 and Q ∈ (0,1): g(Q) − Q = 1 − (1−Q)^γ − Q. Let h(Q) = 1 − (1−Q)^γ − Q. Then h(0) = 0, h(1) = 0, and h''(Q) = −γ(γ−1)(1−Q)^(γ−2) < 0 for all Q ∈ (0,1). A concave function that is zero at both endpoints and has h'(0) = γ − 1 > 0 must be strictly positive on (0,1). Hence g(Q) > Q ✓. Boundary conditions hold by inspection ✓.

**Proposition A.1.** For g(Q) = 1 − (1−Q)^γ with γ > 1, the perceived severity index satisfies:

    S(Q) = 1 − (1−Q)^(γ−1)

and S is strictly increasing on (0, 1), with S(0) = 0 and S(Q) → 1 as Q → 1.

**Proof.** Let r = 1 − Q ∈ (0,1). Then:

    S = Δ/(1−Q) = [1 − r^γ − (1−r)] / r = [r − r^γ] / r = 1 − r^(γ−1)

Since γ − 1 > 0, r^(γ−1) is strictly decreasing in r (for r ∈ (0,1)), hence strictly increasing in Q. Therefore S(Q) = 1 − r^(γ−1) is strictly increasing in Q. □

### A.3 Interpretation

**The absolute deficit** Δ(Q) = h(Q) = 1 − (1−Q)^γ − Q has an interior maximum at Q* = 1 − γ^(−1/(γ−1)) and converges to zero at both endpoints. The absolute gap narrows as quality approaches perfection.

**The perceived severity** S(Q) = 1 − (1−Q)^(γ−1) is monotonically increasing, approaching 1 as Q → 1. In the limit, virtually all remaining imperfection falls within the zone of socially constructed intolerance — even though the absolute amount of imperfection is vanishingly small.

This captures formally what Tocqueville described: "sensibility grows keener even as the evil diminishes." The evil (Δ) diminishes; the sensibility (S) grows.

**Example (γ = 2).** S(Q) = 1 − (1−Q) = Q. Perceived severity equals objective quality: a system that is 90% reliable generates 90% perceived severity, despite an absolute deficit of only Δ = 1−(1−0.9)² − 0.9 = 0.09. A system that is 99% reliable generates 99% perceived severity despite a deficit of Δ = 0.0099.

**Example (γ = 3).** S(Q) = 1 − (1−Q)². At Q = 0.5: S = 0.75. At Q = 0.9: S = 0.99. At Q = 0.99: S = 0.9999. The experienced severity increases rapidly as the system approaches perfection.

### A.4 General Condition for S Increasing

For a general threshold function g satisfying A1–A2, differentiation gives:

    S'(Q) ∝ Δ'(Q)·(1−Q) + Δ(Q)

S is increasing whenever Δ(Q) > |Δ'(Q)|·(1−Q) for Q in the declining-Δ regime — that is, whenever the absolute deficit declines more slowly than the remaining distance to perfection. The power family provides a tractable characterisation of when this condition holds globally. Alternative parametric families (e.g., logit transformations, beta-function thresholds) yield qualitatively similar results provided they satisfy A1–A2 and a mild regularity condition on the rate of convergence of Δ to zero.

### A.5 Connection to the Hedonic Treadmill

The Easterlin paradox literature (Easterlin, 1974; Stevenson and Wolfers, 2008) models individual aspiration adjustment as A(t) = f(Y(t)) where Y(t) is income and A(t) is the aspiration level, with A tracking Y such that reported wellbeing W ∝ Y/A stabilises. The present model is structurally analogous: τ plays the role of A, Q plays the role of Y, and S plays the role of experienced wellbeing deficit. The key difference is that τ is a collective normative construction governed by social comparison and institutional dynamics, whereas A in the hedonic treadmill literature is primarily an individual psychological process. The two phenomena are mechanistically homologous but operate on different levels of social organisation and through different causal mechanisms.

---

## References

Boudon, R. (1977). *Effets pervers et ordre social*. Paris: Presses Universitaires de France.

Brickman, P. and Campbell, D.T. (1971). Hedonic relativism and planning the good society. In M.H. Appley (ed.), *Adaptation-Level Theory*. New York: Academic Press, 287–302.

Curtice, J. (2023). *Support for Scottish Independence: The Long-Run Trend*. Edinburgh: ScotCen Social Research.

Dalton, R.J. (2004). *Democratic Challenges, Democratic Choices: The Erosion of Political Support in Advanced Industrial Democracies*. Oxford: Oxford University Press.

Davies, J.C. (1962). Toward a theory of revolution. *American Sociological Review*, 27(1), 5–19.

Easterlin, R.A. (1974). Does economic growth improve the human lot? Some empirical evidence. In P.A. David and M.W. Reder (eds), *Nations and Households in Economic Growth*. New York: Academic Press, 89–125.

European Union (2022). Regulation (EU) 2022/2065 on a Single Market for Digital Services (Digital Services Act). *Official Journal of the European Union*, L 277, 1–102.

Gurr, T.R. (1970). *Why Men Rebel*. Princeton: Princeton University Press.

Hirschman, A.O. (1991). *The Rhetoric of Reaction: Perversity, Futility, Jeopardy*. Cambridge, MA: Harvard University Press.

IATA (2023). *Safety Report 2022*. Montreal: International Air Transport Association.

Keating, M. (2001). Reforging the union: Devolution and constitutional change in the United Kingdom. *Publius: The Journal of Federalism*, 28(1), 217–244.

Kessler, D. and McClellan, M. (1996). Do doctors practice defensive medicine? *Quarterly Journal of Economics*, 111(2), 353–390.

Mello, M.M., Chandra, A., Gawande, A.A. and Studdert, D.M. (2010). National costs of the medical liability system. *Health Affairs*, 29(9), 1569–1577.

Merton, R.K. (1968). *Social Theory and Social Structure* (enlarged edition). New York: Free Press.

Meta (2023). *Community Standards Enforcement Report Q4 2023*. Menlo Park: Meta Platforms.

National Center for Missing and Exploited Children (2024). *CyberTipline 2023 Report*. Alexandria, VA: NCMEC.

Norris, P. and Inglehart, R. (2019). *Cultural Backlash: Trump, Brexit, and Authoritarian Populism*. Cambridge: Cambridge University Press.

Robert, J.H.N. (2025). La Loi de Tocqueville généralisée : pourquoi le progrès nourrit l'insatisfaction. *Les Carnets du Baron Mariani* (Substack), 17 October. [Working paper antecedent to this article.]

Runciman, W.G. (1966). *Relative Deprivation and Social Justice*. London: Routledge.

Stevenson, B. and Wolfers, J. (2008). Economic growth and subjective well-being: Reassessing the Easterlin paradox. *Brookings Papers on Economic Activity*, 2008(1), 1–87.

Stouffer, S.A., Suchman, E.A., DeVinney, L.C., Star, S.A. and Williams, R.M., Jr (1949). *The American Soldier: Adjustment During Army Life*, vol. 1. Princeton: Princeton University Press.

Tocqueville, A. de (1835/1840). *De la démocratie en Amérique*, 2 vols. Paris: Gallimard (Folio edition, 1986).

Tocqueville, A. de (1856). *L'Ancien Régime et la Révolution*. Paris: Lévy.

YouTube (2023). *YouTube Community Guidelines Enforcement: Q4 2022 Report*. San Bruno: Google LLC.
