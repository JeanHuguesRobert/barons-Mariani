---
title: "DAO, imputabilité et DHITL"
subtitle: "Pourquoi la blockchain trace l’exécution sans garantir la responsabilité"
version: "v0.2-media-legal"
status: "working-paper — academic source form, media/legal reinforced"
document_role: "document source provisoire du corpus"
derived_from:
  - "conversation ChatGPT — 2026-06-03"
  - "barons-Mariani/research/traceabilite_des_actes.md"
  - "barons-Mariani/research/second_method.md"
  - "FractaVolta/traceable_governance.md"
  - "inseme/AGENTS.md"
  - "inseme/packages/brique-kudocracy/src/governance.js"
  - "review Grok — focus visibilité médiatique et recours juridiques"
source_status: "source provisoire; à consolider par revue adversariale et annexe juridique comparative"
document_family: "academic_source_form"
author: "Jean Hugues Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
license: "CC BY 4.0"
method: "seconde méthode — objections first-class, claims tracés, continuation explicite, revue adversariale attendue"
language: "fr"
abstract_language: "en"
date: "2026-06-03"
last_stamped_at: 2026-06-03
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/dao_imputabilite_dhitl.md"
repository_candidate:
  primary: "barons-Mariani"
  secondary: "cogentia"
  operational_links:
    - "inseme"
    - "FractaVolta"
    - "marenostrum"
related_concepts:
  - "DAO"
  - "blockchain"
  - "smart contracts"
  - "imputabilité"
  - "traçabilité des actes"
  - "DHITL"
  - "souveraineté des vivants"
  - "Kudocracy"
  - "COP"
  - "Cogentia"
  - "legal wrappers"
  - "revue adversariale"
  - "gouvernance distribuée"
  - "fractal traceability"
related_documents:
  - "barons-Mariani/research/traceabilite_des_actes.md"
  - "barons-Mariani/research/second_method.md"
  - "barons-Mariani/research/democratic_ai_safety.md"
  - "barons-Mariani/research/kudocracy.md"
  - "FractaVolta/traceable_governance.md"
  - "inseme/AGENTS.md"
  - "inseme/packages/brique-kudocracy/src/governance.js"
process_visibility: "partial; improved through process companion file and issue-based review"
continuation_status: "open"
human_validation_needed: true
---

# DAO, imputabilité et DHITL

## Pourquoi la blockchain trace l’exécution sans garantir la responsabilité

**Jean Hugues Robert**  
Institut Mariani / C.O.R.S.I.C.A. — Corte, Corsica  
Working paper — 2026-06-03

---

## Abstract

Decentralized autonomous organizations (DAOs) are often presented as transparent, verifiable and anti-capture forms of governance. This claim is only partially true. Public blockchains can record votes, signatures, proposals, token balances, treasury movements and smart-contract executions. Yet this technical traceability does not by itself create political, legal or institutional accountability.

This paper argues that the classical DAO model often confuses traceability of execution with imputability of decision. A distributed ledger can prove that something was signed, voted or executed; it does not prove that the act was legitimate, understood, contestable, reversible, correctable, or attributable to an identifiable respondent.

The paper applies the DHITL doctrine — Democratic Humans in the Loop — to DAO governance. As artificial agents may assist deliberation without absorbing accountability, smart contracts may execute decisions without absorbing responsibility. A DHITL-compatible DAO must attach every engaging act to an explicit mandate, a validation chain, an identifiable respondent, a public justification, a contestation path, and revocation or correction procedures.

---

## Résumé

Les organisations autonomes décentralisées — DAO — sont souvent présentées comme des architectures de gouvernance transparentes, vérifiables et résistantes à la capture institutionnelle. Cette présentation est partiellement vraie : les blockchains permettent d’enregistrer publiquement des votes, des signatures, des propositions, des transactions et des exécutions de smart contracts.

Mais cette traçabilité technique ne suffit pas à produire une imputabilité politique, juridique ou institutionnelle.

La thèse de cet article est la suivante :

> **La DAO classique confond souvent traçabilité de l’exécution et imputabilité de la décision.**

Un registre distribué peut prouver qu’un acte a été signé, voté ou exécuté. Il ne prouve pas que l’acte était légitime, compris, contestable, corrigible, révocable, ni rattachable à un répondant humain ou institutionnel.

La doctrine DHITL — *Democratic Humans in the Loop* — permet de formuler une exigence plus stricte : les automates, qu’il s’agisse d’agents IA ou de smart contracts, peuvent assister, préparer, agréger ou exécuter ; ils ne doivent pas absorber l’imputabilité des actes engageants.

Dans une architecture conforme à cette doctrine, un acte de DAO doit donc rester rattaché à un mandat explicite, à une chaîne de validation, à un répondant identifiable, à une justification, à des voies de contestation, et à des conditions de révocation ou correction.

---

## 1. Statut du document

Ce document est une **forme académique source provisoire**. Il vise à stabiliser une thèse doctrinale et opérationnelle sur les DAO, l’imputabilité et DHITL.

Il s’inscrit dans le corpus suivant :

- `barons-Mariani/research/traceabilite_des_actes.md` — doctrine des actes engageants, de l’imputabilité et de la révocation ;
- `barons-Mariani/research/second_method.md` — seconde méthode, objections first-class, versionnement, corpus public ;
- `FractaVolta/traceable_governance.md` — gouvernance fractale, responsabilité locale et vérifiabilité globale ;
- `inseme/AGENTS.md` — mandat borné, invariants COP, séparation protocole/implémentation, traçabilité de l’incertitude ;
- `inseme/packages/brique-kudocracy/src/governance.js` — typologie de modèles de gouvernance, dont la DAO algorithmique.

Il doit être lu comme un document **autoporteur** : ses thèses principales doivent pouvoir être évaluées sans lecture préalable des autres documents du corpus. Les liens internes documentent la généalogie conceptuelle, non une autorité par auto-référence.

---

## 2. Problème

Les DAO apparaissent comme une réponse à deux défaillances classiques des organisations humaines :

1. la centralisation opaque ;
2. la capture institutionnelle.

Elles substituent à l’organisation traditionnelle un ensemble de règles inscrites dans des smart contracts, des votes pondérés par tokens, des propositions publiées, des transactions horodatées et des registres distribués.

Ce déplacement résout une partie du problème : l’acte technique devient plus difficile à dissimuler.

Mais il en ouvre un autre :

> **Qui répond de l’acte ?**

Une DAO peut produire une trace publique sans produire de répondant identifiable. Elle peut produire un historique immuable sans produire une responsabilité. Elle peut rendre visible l’exécution sans rendre imputable la décision.

C’est le point central.

---

## 3. Thèse principale

> **Une DAO ne doit pas être évaluée seulement par son degré de décentralisation technique, mais par sa capacité à maintenir l’imputabilité effective de ses actes engageants.**

Cette thèse prolonge deux propositions déjà présentes dans le corpus.

Premièrement, les architectures pleinement distribuées peuvent dissoudre l’accountability : lorsque quelque chose échoue, la responsabilité s’évapore dans le réseau. La crise de The DAO en 2016, le fork Ethereum qui l’a suivie, les cartels de validation, les pools, les délégations concentrées et les votes pondérés par tokens illustrent cette difficulté.

Deuxièmement, dans la doctrine de la traçabilité des actes, l’imputabilité n’est pas la simple visibilité de l’acte. Elle est le rattachement de l’acte à un répondant identifiable.

La formule centrale est :

> **Une trace sans répondant n’est qu’une archive.**

Appliquée aux DAO :

> **Une blockchain sans répondant n’est qu’une archive distribuée.**

---

## 4. Définitions

### 4.1. DAO

Une DAO est ici définie comme une organisation dont tout ou partie de la gouvernance est assurée par : smart contracts, tokens de gouvernance, propositions formalisées, votes on-chain ou off-chain, signatures cryptographiques, règles d’exécution automatisées, trésorerie ou droits contrôlés par protocole.

Cette définition est fonctionnelle. Elle ne suppose pas qu’une DAO soit juridiquement reconnue comme personne morale.

### 4.2. Traçabilité

La traçabilité désigne la capacité à reconstituer l’existence, le contexte, le mandat, la justification, les effets et les corrections éventuelles d’un acte engageant.

Dans une DAO, la traçabilité peut porter sur :

- le wallet du proposant ;
- le hash de la proposition ;
- le texte public de la proposition ;
- le code ou payload exécuté ;
- les votes ;
- le quorum ;
- le résultat ;
- la transaction d’exécution ;
- l’historique de la trésorerie ;
- les délégations de vote ;
- les changements de paramètres.

Cette traçabilité est forte sur le plan technique. Elle reste insuffisante si elle ne permet pas d’identifier le régime de responsabilité.

### 4.3. Imputabilité

L’imputabilité est le rattachement d’un acte à un répondant.

Dans une DAO, le répondant peut être un proposant identifié, un organe validateur, une personne morale enveloppante, un council, un groupe borné de signataires, un délégataire révocable, ou une chaîne de validation explicitement définie.

Le répondant ne devrait pas être seulement :

- “la communauté” ;
- “le code” ;
- “le protocole” ;
- “le marché” ;
- “les token holders” pris comme masse indéterminée.

Ces termes peuvent désigner des contextes ou des mécanismes. Ils ne suffisent pas, seuls, à produire de l’imputabilité.

### 4.4. Acte engageant DAO

Un acte DAO est engageant lorsqu’il produit, prépare ou propage un effet significatif dans un système de responsabilité.

Exemples :

- transfert de trésorerie ;
- modification de protocole ;
- upgrade de smart contract ;
- changement de paramètres économiques ;
- délégation massive de votes ;
- nomination ou révocation d’un signataire ;
- déclaration publique au nom de la DAO ;
- décision affectant des tiers ;
- exécution irréversible.

---

## 5. État empirique récent

### 5.1. Concentration du pouvoir

La littérature récente confirme que les DAO ne sont pas spontanément démocratiques. Plusieurs travaux 2024-2026 convergent sur un point : la gouvernance par tokens tend à produire ou renforcer la concentration du pouvoir.

Une analyse à grande échelle de 100 DAO, publiée en 2024, indique que le degré de décentralisation dépend fortement de la participation effective et de la variance du pouvoir de vote ; la distribution du pouvoir mesurée par des indicateurs de type Gini est donc centrale pour évaluer la gouvernance réelle d’une DAO.

Des travaux de 2026 sur 48 DAO Ethereum observent que token registration, staking et délégation, censés améliorer sécurité ou participation, peuvent aussi renforcer la concentration du pouvoir de vote.

Une autre étude de 2026 soutient qu’aucune règle de vote dérivée uniquement du solde de wallet ne peut garantir une gouvernance anti-ploutocratique sur blockchain permissionless, en raison des stratégies de fragmentation Sybil et des coûts réalistes d’attaque.

### 5.2. Délégation et représentativité

La délégation de vote est souvent présentée comme un remède à l’apathie. Elle peut aussi concentrer la visibilité et l’influence.

Des recherches récentes sur la délégation montrent que les interfaces de ranking et les effets de réputation peuvent concentrer les délégations sur un petit nombre d’acteurs visibles. Un système de délégation peut donc accroître l’efficacité apparente tout en réduisant la pluralité réelle.

Ce point est directement pertinent pour Kudocracy : la délégation ne doit pas devenir un blanc-seing. Elle doit rester explicite, révocable, tracée et contestable.

### 5.3. Lisibilité texte/code

La gouvernance DAO repose souvent sur une séparation fragile entre description humaine et payload exécutable. Une proposition peut être votée sur la base d’un texte simplifié alors que l’exécution réelle dépend d’un code ou d’un calldata difficilement lisible.

Le risque n’est pas seulement l’erreur technique. Il est institutionnel : les participants peuvent voter sur un objet qu’ils croient comprendre, alors que l’acte exécuté diffère fonctionnellement de l’acte décrit.

Une DAO-DHITL doit donc intégrer une exigence de correspondance texte/code : résumé humain, diff ou payload vérifiable, revue technique, signalement des incertitudes, et responsabilité du validateur.

---

## 6. État juridique et réglementaire

### 6.1. The DAO et Ethereum

The DAO reste le cas fondateur. L’incident de 2016 a montré qu’un système peut être formellement gouverné par du code tout en laissant irrésolue la question politique de la correction après exploitation.

Le fork Ethereum a été une décision de gouvernance exceptionnelle. Il montre que, même dans un univers prétendument “code is law”, les communautés humaines réintroduisent la décision lorsque l’exécution automatique produit un résultat politiquement ou économiquement inacceptable.

### 6.2. Ooki, bZx, Compound, Lido

Les contentieux américains récents explorent la possibilité de traiter certaines DAO comme associations non constituées, partenariats généraux ou collectifs juridiquement atteignables.

Dans Ooki DAO, une juridiction américaine a admis, dans le cadre procédural de l’affaire, qu’une DAO puisse être traitée comme une association non constituée. Dans bZx DAO, Compound et Lido, des demandeurs ont soutenu que certains détenteurs de tokens, backers ou participants actifs pouvaient être exposés à une responsabilité fondée sur une théorie de partenariat général ou d’association.

La leçon n’est pas que toutes les DAO seraient identiques. Elle est plus précise :

> **Lorsque la DAO ne produit pas sa propre imputabilité, le juge peut la reconstruire de l’extérieur.**

Cette reconstruction peut être brutale, incertaine, et atteindre des acteurs qui ne se pensaient pas répondants.

### 6.3. Legal wrappers

Les legal wrappers — Wyoming DAO LLC, Marshall Islands DAO LLC, fondations, associations, sociétés, structures suisses ou autres — peuvent réduire l’incertitude externe. Ils permettent de désigner une entité, un droit applicable, une capacité à contracter, parfois une limitation de responsabilité.

Mais ils ne résolvent pas tout. Une personne morale enveloppante peut produire une façade juridique tout en laissant intactes les pathologies internes : vote capturé, délégation opaque, payload incompris, absence de recours, absence de révocation réelle.

Un legal wrapper est donc une condition possible de sécurité juridique, non une preuve de démocratie.

### 6.4. MiCA, eIDAS 2 et contexte européen

Le règlement MiCA fournit un cadre européen pour les crypto-actifs et les prestataires de services sur crypto-actifs. Il n’est pas une loi générale des DAO, mais il modifie l’environnement dans lequel les organisations crypto doivent opérer en Europe.

En mai 2026, l’AMF française a rappelé l’urgence pour les sociétés crypto opérant dans l’Union européenne d’obtenir les autorisations requises sous MiCA avant la date limite de juin 2026, sous peine de mesures d’exécution et de poursuites.

Le contexte européen renforce donc l’exigence d’imputabilité : même si une DAO reste techniquement distribuée, ses interfaces avec utilisateurs, prestataires, trésoreries, émetteurs et opérateurs deviennent de plus en plus susceptibles d’être rattachées à des personnes ou entités juridiquement qualifiables.

---

## 7. Outils open source et infrastructures actuelles

Les outils DAO existants résolvent une partie du problème, mais pas tout le problème.

### 7.1. OpenZeppelin Governor

OpenZeppelin Governor fournit des contrats modulaires de gouvernance on-chain. Il formalise propositions, votes, quorum, timelocks et exécution. Il améliore fortement la traçabilité et la sécurité contractuelle, mais ne décide pas qui répond politiquement ou juridiquement des actes engageants.

### 7.2. Aragon OSx

Aragon OSx fournit une infrastructure open source de gouvernance DAO, avec plugins, permissions et exécution. Il permet de construire des organisations plus structurées, mais l’imputabilité dépend encore du design institutionnel choisi par la communauté.

### 7.3. Snapshot

Snapshot est très utilisé pour le vote off-chain signé. Il réduit les coûts de vote et facilite la participation, mais il dissocie souvent signal politique et exécution on-chain. La chaîne d’imputabilité doit donc être explicitement reconstruite entre vote, validation, multisig et exécution.

### 7.4. Safe

Safe est un standard de multisig et de smart accounts. Il fournit un excellent outil de contrôle opérationnel, mais un multisig n’est pas en soi une gouvernance démocratique. Les signataires doivent avoir un mandat, des obligations de justification, des règles de conflit d’intérêts et une révocabilité.

### 7.5. Tally et interfaces de gouvernance

Tally et autres portails rendent la gouvernance plus lisible et plus accessible. Mais les interfaces peuvent aussi orienter la délégation, amplifier certains acteurs visibles et simplifier excessivement des propositions complexes.

### 7.6. Conclusion outillage

Ces outils sont nécessaires. Ils ne suffisent pas.

Ils produisent des primitives : vote, signature, quorum, exécution, multisig, timelock, délégation. Le modèle DAO-DHITL ajoute une couche manquante : mandat, répondant, justification, contestation, correction, révocation.

---

## 8. Modèle DAO-DHITL

Une DAO compatible DHITL devrait respecter au moins neuf conditions.

### 8.1. Mandat explicite

Chaque acte engageant doit préciser qui agit, au nom de quel pouvoir, dans quel périmètre, avec quelles limites et pour quelle durée.

### 8.2. Lisibilité opposable

Le texte humain, le code, le diff, le calldata et les effets attendus doivent être suffisamment alignés pour que le vote porte sur l’acte réellement exécuté.

### 8.3. Répondant identifié

Le répondant peut être individuel, organique ou institutionnel. Il ne doit pas être dissous dans “la communauté”.

### 8.4. Fenêtre de contestation

Tout acte sensible devrait prévoir un délai de contestation proportionné à son irréversibilité.

### 8.5. Journalisation des arbitrages

Les objections, réponses, motifs de rejet, conflits d’intérêts et corrections doivent être conservés comme éléments de gouvernance, non comme bruit.

### 8.6. Révocabilité

Délégations, councils, signataires, opérateurs, oracles et interfaces critiques doivent pouvoir être révoqués selon une procédure explicite.

### 8.7. Séparation protocole / implémentation

Le smart contract exécute un protocole. Il ne doit pas redéfinir silencieusement la constitution de l’organisation.

### 8.8. Minimisation identitaire

L’imputabilité ne doit pas devenir surveillance généralisée. Une DAO-DHITL doit distinguer : identité publique, identité vérifiée, preuve d’éligibilité, preuve de mandat, preuve de responsabilité, et exposition inutile de données personnelles.

### 8.9. Mesure publique de concentration

Une DAO qui prétend être décentralisée devrait publier des indicateurs de concentration : Gini du pouvoir de vote, parts des principaux votants, concentration des délégations, dépendance aux delegates, poids des investisseurs, quorum réel, abstention, et évolution avant/après votes sensibles.

---

## 9. Schéma minimal d’acte DAO imputable

```yaml
dao_act:
  id: "dao-act-YYYYMMDD-001"
  dao: "DAO_NAME"
  chain: "ethereum | arbitrum | optimism | other"
  governance_stack:
    vote_tool: "Governor | Snapshot | Aragon | custom"
    execution_tool: "Governor | Safe | timelock | custom"
    legal_wrapper: "none | LLC | foundation | association | other"
  contract: "0x..."
  proposal:
    id: "proposal-id"
    hash: "proposal-hash"
    human_readable_summary: "..."
    code_diff_or_execution_payload: "..."
    text_code_consistency_check: "passed | failed | partial | not_reviewed"
  actor:
    proposer: "wallet | person | legal_person | council"
    validators: []
    voters_scope: "token_holders | delegates | members | mixed"
  mandate:
    source: "constitution | governance rules | prior vote | legal wrapper"
    scope: "treasury | protocol upgrade | parameter change | public statement"
    expiry: "date or condition"
  decision:
    voting_rule: "token_weighted | quadratic | one_person_one_vote | delegated | hybrid"
    quorum: "..."
    threshold: "..."
    turnout: "..."
    concentration_metrics:
      gini_voting_power: "..."
      top_5_voters_share: "..."
      top_10_delegates_share: "..."
  dhitl:
    human_review_required: true
    reviewer_body: "council | audit committee | assembly | legal representative"
    ai_or_automation_role: "analysis | drafting | simulation | execution"
    binding_decision_by_automation: false
  accountability:
    accountable_respondent: "person | organ | legal_person | bounded signer set"
    justification: "..."
    expected_effects: "..."
    affected_parties: []
  review:
    objection_window: "..."
    appeal_body: "..."
    emergency_pause: "available | unavailable"
    revocation_path: "..."
  execution:
    timelock: "..."
    executed_at: "..."
    transaction_hash: "..."
  status:
    valid_internal_act: "yes | no | contested | regularized"
    known_uncertainties: []
```

---

## 10. Worked example — transfert de trésorerie

Une DAO vote le transfert de 100 000 USDC vers un prestataire pour financer un audit.

Dans un modèle classique :

1. une proposition est publiée ;
2. des wallets votent ;
3. un quorum est atteint ;
4. un timelock expire ;
5. le contrat ou multisig exécute.

La trace existe. L’imputabilité reste incomplète si personne ne peut répondre clairement : qui a vérifié le prestataire, qui a contrôlé le conflit d’intérêts, qui a validé la correspondance entre texte et payload, qui peut contester la mauvaise exécution, qui est responsable si le paiement finance autre chose que l’audit annoncé.

Dans un modèle DAO-DHITL, l’acte devrait ajouter :

- mandat du proposant ;
- texte/code consistency check ;
- répondant institutionnel ou organique ;
- fenêtre d’objection ;
- justification publique ;
- clause de révocation ou suspension ;
- trace de livraison ;
- procédure de correction si l’audit n’est pas livré.

Le gain n’est pas bureaucratique. Il est institutionnel : le transfert devient un acte imputable, non seulement une transaction.

---

## 11. Claims et niveaux de preuve

| Claim | Type | Solidité actuelle | À renforcer |
|---|---|---:|---|
| La blockchain permet une forte traçabilité technique des votes et exécutions. | constat technique | élevée | cas détaillés par chaîne |
| La traçabilité technique ne garantit pas l’imputabilité. | thèse conceptuelle | élevée | typologie juridique comparée |
| Les DAO tokenisées tendent vers la concentration du pouvoir. | constat empirique | moyenne à élevée | datasets supplémentaires |
| Les mécanismes de délégation peuvent accroître la concentration. | constat empirique | moyenne à élevée | étude multi-DAO répliquée |
| Les legal wrappers réduisent certains risques sans résoudre toute la question démocratique. | hypothèse juridique | moyenne | comparaison Wyoming / Marshall Islands / Suisse / UE / France |
| DHITL fournit une grille transposable des IA aux smart contracts. | proposition doctrinale | élevée en cohérence interne | objections adversariales |
| Un acte DAO engageant non imputable devrait être présumé invalide dans le régime interne de la DAO. | proposition normative | moyenne | articulation juridique fine |

---

## 12. Failure modes

| Failure mode | Description | Gravité |
|---|---|---:|
| Archive sans répondant | trace technique sans sujet imputable | critique |
| Oligarchie tokenisée | concentration effective du vote chez quelques détenteurs ou délégués | critique |
| Interface manipulatoire | ranking, UX ou simplification orientant délégation/vote | majeure |
| Mismatch texte/code | le texte voté ne correspond pas exactement à l’exécution | critique |
| Legal wrapper façade | personnalité juridique sans gouvernance interne imputable | majeure |
| Multisig non mandaté | signataires puissants mais insuffisamment révocables | majeure |
| Surveillance sous prétexte d’imputabilité | excès d’identification personnelle | majeure |
| Timelock décoratif | délai trop court ou sans voie réelle d’objection | mineure à majeure |
| Emergency pause capturée | pouvoir de suspension concentré ou abusif | majeure |

---

## 13. Objections principales

### Objection 1 — Une DAO vise précisément à éviter les répondants centralisés

Réponse : l’imputabilité n’implique pas nécessairement centralisation. Elle exige un rattachement explicite de l’acte à un répondant ou à une chaîne de répondants. Une architecture fractale peut conserver une responsabilité locale et une vérifiabilité globale sans rétablir un centre opaque.

### Objection 2 — Les token holders sont les répondants

Réponse : seulement si le régime l’indique explicitement, si les détenteurs sont identifiables ou au moins juridiquement qualifiables, et si leur participation correspond à un acte conscient. Sinon, on confond détention économique, vote, spéculation, délégation passive et responsabilité.

### Objection 3 — Le code est la loi

Réponse : le code est une modalité d’exécution. Il n’est pas nécessairement une source légitime de normativité. Cette objection confond validité technique et validité institutionnelle.

### Objection 4 — Ajouter de l’imputabilité réduit la décentralisation

Réponse : cela réduit surtout l’irresponsabilité. La décentralisation peut porter sur la décision, l’exécution, la vérification ou la contestation. Elle n’exige pas que la responsabilité devienne introuvable.

### Objection 5 — Le droit existant finira par régler le problème

Réponse : le droit peut reconstituer des responsabilités après coup, mais souvent au prix d’une incertitude élevée. La doctrine proposée vise une imputabilité interne, lisible avant crise, plutôt qu’une responsabilité reconstruite après contentieux.

### Objection 6 — L’imputabilité menace l’anonymat légitime

Réponse : l’imputabilité n’exige pas toujours l’identité publique complète. Elle exige un répondant ou une chaîne de validation. Des mécanismes de preuve d’éligibilité, de rôle, de mandat ou de responsabilité peuvent limiter l’exposition identitaire tout en évitant l’irresponsabilité totale.

---

## 14. Non-claims

Cet article ne prétend pas que toutes les DAO sont illégitimes.

Il ne prétend pas que les blockchains seraient inutiles à la gouvernance.

Il ne prétend pas que les legal wrappers suffisent.

Il ne prétend pas qu’une DAO doit forcément redevenir une association ou une société classique.

Il ne prétend pas que DHITL résout tous les problèmes juridiques des DAO.

Il ne prétend pas que l’imputabilité impose une surveillance générale des participants.

Il affirme seulement ceci :

> **Une gouvernance distribuée qui ne sait pas rattacher ses actes engageants à des répondants identifiables produit de la traçabilité sans responsabilité.**

---

## 15. Public traceability and adversarial review

This working paper is intended to become fully traceable through Git history, issue-based adversarial review, and explicit continuation packets.

The paper is not only about accountability; it must remain accountable as a document. Its author, institutional affiliation, claims, uncertainty levels, objections, and future verification tasks are explicitly identified.

The next methodological step is to expose the paper to adversarial review by DAO practitioners, blockchain lawyers, political theorists, governance designers, open-source maintainers and institutional actors. Objections should be treated as first-class contributions and, where relevant, converted into traceable issues, amendments, or counter-claims.

---

## 16. Conclusion

Les DAO ont déplacé le problème de la gouvernance. Elles n’ont pas supprimé le problème de la responsabilité.

Leur apport principal est réel : elles rendent certains actes visibles, signés, horodatés, vérifiables et exécutables. Mais cette visibilité peut masquer une carence plus profonde : l’absence de sujet imputable.

La doctrine DHITL permet de reformuler le problème. De même qu’une IA peut assister la délibération sans absorber l’imputabilité, un smart contract peut exécuter une décision sans devenir le sujet responsable de cette décision.

La question centrale n’est donc pas :

> La DAO est-elle décentralisée ?

Mais :

> Ses actes engageants sont-ils traçables, imputables, justifiables, contestables, corrigibles et révocables ?

La blockchain répond surtout à la première partie : tracer.  
DHITL impose les suivantes : imputer, justifier, contester, corriger, révoquer.

---

## 17. Bibliographie provisoire

### Corpus interne

- Jean Hugues Robert, `barons-Mariani/research/traceabilite_des_actes.md`.
- Jean Hugues Robert, `barons-Mariani/research/second_method.md`.
- Jean Hugues Robert, `FractaVolta/traceable_governance.md`.
- Jean Hugues Robert, `inseme/AGENTS.md`.
- Jean Hugues Robert, `inseme/packages/brique-kudocracy/src/governance.js`.

### Littérature académique et empirique

- Kitzler, Saggese, Balietti, Haslhofer, Strohmaier, *The Governance of Decentralized Autonomous Organizations: A Study of Contributors’ Influence, Networks, and Shifts in Voting Power*, arXiv:2309.14232, 2023.
- Sharma, Potter, Pongmala, Wang, Miller, Song, Wang, *Future of Algorithmic Organization: Large-Scale Analysis of Decentralized Autonomous Organizations (DAOs)*, arXiv:2410.13095, 2024.
- Bongaerts, Lambert, Liebau, Roosenboom, *Vote Delegation in DeFi Governance*, arXiv:2503.11940, 2025.
- Messias, Ide, *Fairness in Token Delegation: Mitigating Voting Power Concentration in DAOs*, arXiv:2510.05830, 2025.
- Pahari, Chandrasekaran, Messias, Gummadi, Dash, *On the Centralization of Governance Power in Decentralized Autonomous Organizations*, arXiv:2604.25959, 2026.
- Bennett, Vander Vos, Le, Belenkiy, *Concave is the New Linear: The Impossibility of Anti-Plutocratic DAO Governance*, arXiv:2605.18990, 2026.
- Bayan, Banach, *A Privacy-Preserving DAO Model Using NFT Authentication for the Punishment not Reward Blockchain Architecture*, arXiv:2405.13156, 2024.
- Chaffer et al., *Decentralized Governance of Autonomous AI Agents*, arXiv:2412.17114, 2024.

### Contentieux et régulation

- The DAO, Ethereum governance crisis and fork, 2016.
- Commodity Futures Trading Commission v. Ooki DAO.
- Sarcuni v. bZx DAO.
- Houghton v. Leshner / Compound DAO litigation.
- Lido DAO litigation.
- Reuters, *Digital assets and DAOs: new theories of liability*, 2024.
- Reuters, *In blow to crypto collectives, judge rules venture backers must face claims*, 2024.
- Regulation (EU) 2023/1114 — Markets in Crypto-Assets Regulation (MiCA).
- Reuters, *Crypto companies without EU licences face prosecution, French regulator warns*, 2026.

### Outils et infrastructures open source

- OpenZeppelin Governor.
- Aragon OSx.
- Snapshot.
- Safe.
- Tally.

---

## 18. Paquet de continuation

```yaml
continuation:
  document: "dao_imputabilite_dhitl.md"
  version: "v0.2-media-legal"
  status: "working paper public — traçabilité à poursuivre"
  external_reviews:
    - reviewer: "Grok"
      date: "2026-06-03"
      role: "external AI reviewer"
      focus:
        - "visibility media"
        - "legal remedies"
        - "second method compliance"
      assessment: >
        The paper is methodologically coherent and ready for public traceable
        publication, provided the process visibility is completed through Git
        history, public objections, and legal claim consolidation.
  bounded_mandate:
    issue_title: "Publier et consolider DAO-DHITL : traçabilité publique, revue adversariale et annexe juridique"
    target_file: "research/dao_imputabilite_dhitl.md"
    expected_closure_condition: >
      Working paper committed, process note added, adversarial review issue opened,
      and legal appendix path clearly identified.
  invariants_preserved:
    - "objections first-class"
    - "répondant humain identifiable"
    - "séparation protocole / implémentation"
    - "traçabilité des claims"
    - "human validation pour positionnement public/juridique"
  claims_to_verify_next:
    - "comparative legal status of DAOs: Wyoming, Marshall Islands, Switzerland, EU, France"
    - "case law: Ooki DAO, bZx DAO, Compound DAO, Lido DAO"
    - "empirical concentration metrics in major DAO governance systems"
    - "proposal text/code mismatch in DAO governance"
    - "formal model of an accountable DAO act"
  downstream_products:
    - "Facebook post with Unicode bold highlights"
    - "Substack public essay"
    - "GitHub issue for adversarial review"
    - "comparative legal appendix"
    - "Kudocracy / COP implementation note"
  human_validation_needed: true
```

---

## 19. Rapport minimal AGENTS-compatible

```text
Issue:
À créer — "Revue adversariale — DAO, imputabilité, legal wrappers et DHITL (v0.2)"

Files changed:
research/dao_imputabilite_dhitl.md
research/dao_imputabilite_dhitl_process.md

Tests run:
Corpus review against traceabilite_des_actes.md, second_method.md, traceable_governance.md, AGENTS.md and governance.js.
External bibliographic and legal references identified.
No software test run.

Known risks:
Legal claims remain jurisdiction-dependent.
Comparative legal appendix still required.
Empirical DAO concentration claims require deeper dataset review.
Some references are provisional and should be converted to stable citations.

Next step:
Open adversarial review issue and invite DAO practitioners, legal experts, governance designers and open-source maintainers.

Human validation needed:
yes — public doctrine, legal framing, political implications and downstream products.
```


<!-- BEGIN_AUTO: backlinks -->
### Backlinks

*These documents link to this file:*
- [Corpus Status — barons-Mariani](corpus-status.md)
- [Research Index — barons-Mariani](index.md)

<!-- END_AUTO: backlinks -->
