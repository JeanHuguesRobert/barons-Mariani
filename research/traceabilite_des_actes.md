---
title: "Traçabilité des actes"
subtitle: "Mandat, imputabilité et contrôle des actes engageants dans les régimes humains, institutionnels et algorithmiques"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-05-27"
status: working-paper — operational research version validated after reviewer critique
version: "0.15.1-research"
license: "CC BY-SA 4.0"
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/traceabilite_des_actes.md
ai_assisted_by:
  - "ChatGPT — drafting, restructuring, consolidation"
reviewed_by:
  - "Grok — external AI reviewer / critic"
human_arbitration_by: "Jean Hugues Noël Robert"
x-method:
  - "seconde méthode"
  - "pipeline Cogentia"
  - "document autoporteur"
  - "genre separation"
tags:
  - traçabilité
  - imputabilité
  - mandat
  - révocation
  - actes engageants
  - DHITL
  - agents IA
  - personnes morales
  - gouvernance
  - sécurité démocratique de l’IA
  - Autonomie de Capacité
related_projects:
  - "Cogentia"
  - "Kudocracy"
  - "Inseme / brique-actes"
  - "Cogentia Commons"
  - "DHITL"
version_history:
  - "v0.13 — consolidated version submitted to Grok"
  - "v0.14-research — genre separation; campaign formulas moved to separate annex"
  - "v0.15-research — operational revision after Grok review, with clearer thresholds and concrete YAML examples"
  - "v0.15.1-research — micro-amendment: reviewer role clarified, no v0.16-research needed before publication"
last_stamped_at: 2026-06-01
document_role: "source"
document_kind: "research-paper"
visibility: "public"
lifecycle_state: "working"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "research-paper"
classification_confidence: "medium"
---

# Traçabilité des actes

## Statut

Cette version est une version de recherche opérationnelle. Elle tient compte d’une critique externe de Grok, utilisé ici comme **reviewer**, non comme rédacteur principal. Après cette revue, il ne paraît pas nécessaire de produire une v0.16 avant publication dans le dépôt : les améliorations restantes relèvent plutôt d’extensions, de tests ou de produits déclinés.

La rédaction, la structuration finale et l’arbitrage doctrinal relèvent de Jean Hugues Noël Robert, assisté par ChatGPT dans le rôle de rédacteur. Grok intervient comme agent critique dans le pipeline Cogentia : il signale les faiblesses, les risques de gonflement conceptuel, les imprécisions et les pistes de resserrement.

Le texte est conçu comme un document **autoporteur** : ses thèses principales doivent pouvoir être évaluées sans lecture préalable des autres documents du corpus.

## Objet

Comment donner à un mandataire une capacité réelle d’action sans créer une zone d’irresponsabilité ?

La réponse proposée consiste à remplacer, autant que possible, le contrôle préalable permanent par une responsabilité renforcée après l’acte : le mandataire agit dans le cadre d’un mandat explicite, mais les **actes engageants** doivent être traçables, imputables, contestables, corrigibles et, si nécessaire, révocables ou sanctionnables.

Cette doctrine vise un équilibre :

- éviter la bureaucratie qui bloque l’action ;
- éviter l’autonomie qui dissout la responsabilité.

---

## 1. Thèse principale

Un système de délégation n’est légitime que si la capacité d’action déléguée reste reliée à un mécanisme effectif d’imputabilité.

Cette exigence s’applique à plusieurs types de mandataires :

- personnes physiques ;
- organes institutionnels ;
- personnes morales ;
- collectifs organisés ;
- procédures automatisées ;
- agents IA utilisés à titre consultatif ou préparatoire.

Plus l’autonomie accordée à un mandataire augmente, plus les mécanismes de traçabilité, d’imputabilité et de correction doivent être robustes. L’objectif n’est pas d’empêcher l’action, mais de la rendre contrôlable sans exiger une autorisation préalable pour chaque opération.

---

## 2. Actes engageants : définition et seuils

Un **acte engageant** est une opération qui produit, prépare ou propage un effet significatif dans un système de responsabilité.

Un acte peut être engageant lorsqu’il :

- engage un mandat ;
- produit un effet sur autrui ;
- modifie une règle, un statut, un registre ou une publication ;
- prépare une décision institutionnelle ou politique ;
- déclenche une propagation automatisée ;
- crée une dette de justification ;
- affecte une chaîne de responsabilité.

Tous les événements ne sont pas des actes engageants. Tous les logs ne doivent pas devenir des objets de gouvernance. Le seuil dépend de l’effet produit ou préparé.

### 2.1 Grille de seuils

| Niveau | Description | Exemple | Traçabilité requise |
|---|---|---|---|
| Trace inutile | Micro-événement sans effet significatif | Brouillon local, log technique mineur | Aucune traçabilité spécifique |
| Trace légère | Contribution ou modification mineure sans arbitrage stabilisé | Suggestion IA non retenue, correction typographique | Journalisation légère si disponible |
| Acte engageant | Effet significatif ou lien direct avec un mandat | Arbitrage doctrinal, délégation, réponse publique validée | Traçabilité complète |
| Acte sensible | Effet juridique, politique, public, irréversible ou fortement contestable | Publication officielle, contrat, modification de règle, décision automatisée opposable | Traçabilité renforcée et revue explicite |

Cette grille vise à éviter deux excès :

- tout tracer de manière bureaucratique ;
- ne tracer que trop tard, lorsque l’acte a déjà produit des effets difficiles à corriger.

---

## 3. Concepts centraux

### 3.1 Traçabilité

La traçabilité est la capacité à retrouver l’existence, le contexte, le mandat, la justification, les effets et les corrections éventuelles d’un acte engageant.

Une trace utile doit permettre de répondre à ces questions :

- quel acte a été posé ?
- par qui ou par quel système ?
- au nom de quel mandat ?
- avec quelle justification ?
- avec quels effets ?
- qui en répond ?
- comment l’acte peut-il être contesté, corrigé ou révoqué ?

### 3.2 Imputabilité

L’imputabilité est le rattachement de l’acte à un répondant identifiable : personne, organe, personne morale ou chaîne de validation.

Une trace sans répondant n’est qu’une archive. Pour produire de la responsabilité, la trace doit pouvoir conduire à un répondant.

### 3.3 Responsabilité

La responsabilité est l’obligation de répondre des conséquences de l’acte imputé. Elle peut être morale, politique, organisationnelle, juridique ou technique selon le régime concerné.

### 3.4 Révocation

La révocation est la possibilité de retirer, limiter ou suspendre un mandat en cas d’abus, d’incapacité ou de rupture du mandat.

La révocation distingue le mandat du blanc-seing.

### 3.5 Chaîne minimale

La chaîne minimale est :

1. trace ;
2. imputation ;
3. justification ;
4. correction ;
5. révocation ou sanction.

---

## 4. Principe interne de validité

Dans un régime de gouvernance fondé sur cette doctrine, un acte engageant non traçable ne devrait pas produire durablement des effets sans régularisation.

Formulation prudente :

> **Un acte engageant non traçable doit être présumé invalide dans le régime interne considéré, sauf régularisation expresse, motivée et elle-même tracée.**

Cette formule n’est pas une règle générale de droit. Elle doit être adaptée selon les régimes :

- corpus de recherche ;
- gouvernance associative ;
- procédure administrative ;
- système logiciel ;
- registre d’actes ;
- chaîne décisionnelle assistée par IA.

---

## 5. Mandat et contrôle

Un mandat est une délégation conditionnelle de capacité d’action.

Il doit idéalement préciser :

- le mandant ;
- le mandataire ;
- le périmètre d’action ;
- les actes autorisés ;
- les actes interdits ;
- les conditions de traçabilité ;
- les conditions de révision ;
- les conditions de révocation.

L’architecture visée remplace le contrôle préalable systématique par une combinaison plus légère :

- mandat explicite ;
- marge d’action réelle ;
- traçabilité proportionnée des actes engageants ;
- revue a posteriori ;
- possibilité de contestation ;
- possibilité de révocation.

---

## 6. Consultation et non-arbitraire

Un avis consultatif n’oblige pas nécessairement à être suivi.

En revanche, son traitement doit être traçable. Une consultation devrait donc laisser une trace minimale :

- existence de la consultation ;
- périmètre ;
- formulation ;
- participants ou corps consulté ;
- résultat ou synthèse ;
- décision finale ;
- motivation de l’écart éventuel entre avis reçu et décision prise.

Formulation sobre :

> **Un avis consultatif peut ne pas être suivi ; son traitement doit être traçable.**

Cette règle ne transforme pas toute consultation en mandat impératif. Elle empêche que la consultation devienne un procédé décoratif.

---

## 7. Agents IA et DHITL

Cette doctrine est liée à **DHITL — Democratic Humans in the Loop**.

Un agent IA peut :

- produire des avis ;
- structurer des arguments ;
- détecter des incohérences ;
- simuler des conséquences ;
- synthétiser des consultations ;
- préparer des arbitrages ;
- alerter sur des risques.

Mais dans les affaires politiquement engageantes, l’IA ne doit pas devenir le sujet de la décision souveraine.

Distinction minimale :

- **avis IA** : production consultative, traçable, contextualisée ;
- **arbitrage humain ou institutionnel** : décision imputable ;
- **acte engageant** : publication, vote, signature, exécution ou propagation ;
- **conséquences** : effets sur des personnes vivantes, des organisations, des territoires ou des corpus.

Formulation sobre :

> **L’IA peut assister la délibération ; elle ne doit pas absorber l’imputabilité.**

---

## 8. Personnes morales augmentées par l’IA

La question des agents IA ne doit pas être isolée de celle des personnes morales.

Les personnes morales sont déjà des entités non biologiques reconnues par le droit. Elles peuvent posséder, contracter, employer, ester en justice, durer, accumuler des ressources et agir dans le monde social.

L’IA peut augmenter leur capacité d’action :

- veille juridique ;
- rédaction automatique ;
- préparation d’argumentaires ;
- analyse de consultations ;
- simulation de réactions publiques ;
- production de réponses institutionnelles ;
- optimisation de procédures ;
- ciblage de communication ;
- justification a posteriori de décisions ;
- lobbying assisté par IA.

Le risque n’est donc pas seulement celui d’une IA autonome. Il est aussi celui d’une personne morale déjà puissante, augmentée par des systèmes IA, mais dont la chaîne d’imputabilité reste insuffisamment visible.

Formulation opérationnelle :

> **Plus une personne morale s’automatise, plus ses actes engageants doivent redevenir imputables.**

La traçabilité doit empêcher quatre formes de dilution :

1. dilution par l’organisation : “l’institution a décidé” ;
2. dilution par la procédure : “le processus a été suivi” ;
3. dilution par l’outil : “le système l’a proposé” ;
4. dilution par l’IA : “le modèle l’a recommandé”.

---

## 9. Régimes d’actes

La doctrine distingue plusieurs régimes.

### 9.1 Acte juridique

Acte produisant un effet dans un cadre de droit : contrat, décision administrative, délibération, acte réglementaire, publication officielle.

Ce régime exige des références juridiques précises.

### 9.2 Acte institutionnel

Acte engageant une organisation : nomination, mandat, délégation, décision interne, sanction, allocation de ressources.

Ce régime exige un registre d’autorité et de responsabilité.

### 9.3 Acte cognitif

Acte modifiant un corpus : ajout d’une thèse, objection, réfutation, stabilisation, publication, continuation.

Il ne produit pas nécessairement un effet juridique, mais il peut engager une mémoire collective, une méthode ou une doctrine.

### 9.4 Acte technique

Acte modifiant un système : commit, déploiement, configuration, suppression, automatisation, accès.

Un acte technique n’est engageant que s’il produit ou prépare un effet significatif dans un système de responsabilité.

### 9.5 Acte algorithmique

Acte produit ou préparé par un système automatisé : classement, scoring, recommandation, filtrage, synthèse, déclenchement.

Ce régime exige un rattachement clair entre le système, le mandat, l’opérateur et le répondant.

### 9.6 Acte hybride

Acte résultant d’une chaîne mixte : humain, personne morale, procédure, IA, registre, publication.

Ce régime est probablement le plus courant dans les organisations contemporaines et le plus exposé à la dilution de responsabilité.

---

## 10. Schéma minimal de traçabilité

Bloc minimal :

```yaml
act:
  id: "act-YYYYMMDD-001"
  date: "YYYY-MM-DD"
  actor: "person | legal_person | ai_agent | collective"
  mandate: "source of authority or delegated capacity"
  action: "short description of the engaging act"
  reason: "why the act was taken"
  effects: "expected or observed consequences"
  accountable: "who answers for this act"
  review: "how the act can be challenged, corrected or revoked"
```

Ce bloc ne s’applique pas à tous les événements. Il concerne les actes engageants.

---

## 11. Exemples YAML

### 11.1 Cogentia — acte cognitif

```yaml
act:
  id: "act-20260527-cog-042"
  date: "2026-05-27"
  actor: "ai_agent:Grok"
  mandate: "pipeline Cogentia — revue critique externe"
  action: "critique de la v0.14-research et proposition de resserrement opérationnel"
  reason: "réduire les redondances, clarifier les seuils, proposer des exemples"
  effects: "production d’une v0.15-research arbitrée par le rédacteur principal"
  accountable: "Jean Hugues Noël Robert"
  review: "acceptation, modification ou rejet explicite des propositions du reviewer"
```

### 11.2 Kudocracy — délégation révocable

```yaml
act:
  id: "act-20260527-kud-017"
  date: "2026-05-27"
  actor: "person:Jean Hugues Noël Robert"
  mandate: "délégation temporaire sur proposition X"
  action: "délégation accordée à mandataire Y"
  reason: "expertise reconnue du mandataire sur le sujet"
  effects: "le mandataire peut émettre un avis ou vote dans le périmètre défini"
  accountable: "Jean Hugues Noël Robert comme délégant, mandataire Y pour l’acte exercé"
  review: "révocation possible selon les conditions du mandat"
```

### 11.3 Personne morale utilisant l’IA

```yaml
act:
  id: "act-20260527-corsica-009"
  date: "2026-05-27"
  actor: "legal_person:C.O.R.S.I.C.A. + ai_agent:assistant_redactionnel"
  mandate: "préparation d’une réponse publique au nom de l’association"
  action: "rédaction assistée par IA d’une réponse institutionnelle"
  reason: "gain de temps et structuration argumentative"
  effects: "publication possible d’une position associative"
  accountable: "président ou organe validateur désigné"
  review: "correction publique ou retrait si erreur, excès de mandat ou contestation fondée"
```

---

## 12. Claims et niveaux de preuve

| Claim | Statut | Solidité interne | À renforcer |
|---|---|---:|---|
| Les personnes morales sont des entités non biologiques capables d’agir durablement. | Constat institutionnel | Élevée | Références juridiques générales |
| L’IA peut augmenter la capacité d’action des personnes morales. | Hypothèse forte | Moyenne à élevée | Cas documentés |
| Un humain dans la boucle peut être un alibi. | Hypothèse forte | Moyenne | Exemples de subordination organisationnelle |
| Les actes politiquement engageants doivent rester imputables à des humains ou institutions humaines. | Proposition normative | Élevée en cohérence interne | Développement constitutionnel |
| Le traitement d’un avis consultatif doit être traçable. | Proposition normative | Élevée | Typologie des consultations |
| Un acte engageant non traçable doit être présumé invalide dans le régime interne considéré. | Proposition opérationnelle | Moyenne | Adaptation par régime |

---

## 13. Objections principales

### Objection 1 — Risque de bureaucratisation

Toute doctrine de traçabilité peut produire une inflation de formulaires.

**Réponse :** la doctrine vise seulement les actes engageants. La grille de seuils doit empêcher que tout micro-événement devienne un objet bureaucratique.

### Objection 2 — Nullité excessive

Présumer invalide un acte non traçable peut sembler trop fort.

**Réponse :** la formule est interne et contextuelle. Elle vise à empêcher des effets durables produits sans trace, non à créer une nullité juridique automatique.

### Objection 3 — Personnification abusive de l’IA

Parler d’agents IA comme mandataires consultatifs pourrait leur donner un statut excessif.

**Réponse :** le statut est fonctionnel. L’IA peut produire un avis, mais l’imputabilité reste humaine ou institutionnelle.

### Objection 4 — Confusion entre personne morale et IA

Une personne morale a un statut juridique ; une IA n’en a pas nécessairement.

**Réponse :** la comparaison est fonctionnelle. Elle aide à comprendre des chaînes d’action non directement biologiques sans assimiler juridiquement les deux.

### Objection 5 — Sur-normativité

Le document propose des normes plus qu’il ne démontre des faits.

**Réponse :** c’est assumé. Le document est une doctrine de gouvernance. Il distingue cependant constats, hypothèses et propositions normatives.

---

## 14. Limites actuelles

- La grille de seuils doit être testée sur des cas concrets.
- La traduction juridique du principe de validité interne reste à vérifier.
- Les exemples YAML doivent être éprouvés dans Cogentia, Kudocracy et Inseme.
- Le lien historique avec Athènes doit être traité séparément.
- La version publique et politique doit rester dans un produit décliné distinct.

---

## 15. Continuation

```yaml
continuation:
  document: "traceabilite_des_actes.md"
  version: "0.15.1-research"
  status: "operational_research_version_validated_after_reviewer_critique"
  roles:
    author_human: "Jean Hugues Noël Robert"
    drafting_agent: "ChatGPT"
    reviewer_agent: "Grok"
  genre_policy:
    research:
      tone: "sober, operational, defensible"
      avoid:
        - "campaign slogans"
        - "grandiloquent formulas"
        - "unverified historical analogies"
    public_annex:
      tone: "political, public, memorable"
      purpose:
        - "Substack"
        - "Facebook"
        - "senatorial campaign"
  next_tasks:
    - "test threshold grid on 10 concrete cases"
    - "produce v0.16 with real Cogentia/Kudocracy/Inseme examples"
    - "verify legal implications of internal invalidity principle"
    - "keep Athenian analogy in separate historical note"
  downstream_applications:
    - paper: "cogentia/research/individual_and_collective_digital_twins.md"
      version: "v0.1, 2026-05-31"
      relation: >
        Applies §8 (personnes morales augmentées par l'IA) and §3.5 (chaîne
        minimale) to the dialectic of sovereign digital twins of natural vs
        legal persons. The collective-twin branch (C.O.R.S.I.C.A. case)
        operationalises the imputability doctrine at the entity scale, in
        the same direction as next_tasks[1]. A future v0.16 of the present
        paper should pick the institutional examples from the C.O.R.S.I.C.A.
        and Institut Mariani traces.
    - paper: "cogentia/research/tracabilite_symetrique_capture_relationnelle.md"
      version: "v0.5, 2026-05-30"
      relation: >
        Extends the doctrine to a specific scene: the asymmetric individual /
        legal-person interaction over communication channels. Capture
        relationnelle is a special case of irresponsibility produced by
        channel architecture, addressable through symmetric traceability.
```
<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Corsica2038 — De la prospective subie à l’autonomie de capacité](autonomia/corsica2038_contre_rapport_pruspettiva2050.md)
- [Rendre capable — noyau doctrinal provisoire](noyau_doctrinal_rendre_capable.md)
- [Research Index — barons-Mariani](index.md)
- [Individual and Collective Digital Twins](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/individual_and_collective_digital_twins.md)
- [Self-Contained Documents in an Interconnected Corpus](https://github.com/JeanHuguesRobert/cogentia/blob/main/research/self_contained_documents.md)
- For researchers
- [FractaLog — Fractal Append-Only Logs for Agents, Mandates, Custody, Inheritance and Delayed Transparency](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/fractalog.md)
- Jean Hugues Noël Robert, baron Mariani
- [Operational Formulas — Representation Primitives](https://github.com/JeanHuguesRobert/JeanHuguesRobert/blob/main/research/operational_formulas.md)
<!-- END_AUTO: backlinks -->
