---
title: "Assistance personnelle capacitaire"
subtitle: "Articulation entre aide humaine, Personal Digital Twin et capacités externes"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-08-21"
status: "working-paper"
version: "0.1"
document_role: "source"
document_kind: "research-note"
visibility: "public"
lifecycle_state: "working"
license: "CC BY-SA 4.0"
language: "fr"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "main"
  origin_date: "2026-08-21"
  derived_from:
    - "research/autonomia/assistance_non_directive_capacitaire.md"
    - "research/serenia_autonomie_assistee_ia.md"
    - "research/autonomia/grammaire_autonomie_de_capacite.md"
review:
  status: "unreviewed"
  reviewed_by: []
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "research/autonomia/assistance_non_directive_capacitaire.md"
  - "research/serenia_autonomie_assistee_ia.md"
  - "research/autonomia/grammaire_autonomie_de_capacite.md"
classification_source: "cogentia.js"
classification_version: "1"
classification_rule: "explicit-metadata"
classification_confidence: "medium"
---

# Assistance personnelle capacitaire

## 1. Objet

Cette note spécialise la doctrine générale de l’**assistance non directive capacitaire** dans le champ de l’aide concrète apportée à une personne dans sa vie quotidienne.

Elle ne crée pas une doctrine concurrente. Elle fournit une interface entre :

- l’Autonomie de Capacité ;
- Serenia ;
- Cogentia et les Personal Digital Twins ;
- les aidants humains ;
- les services à la personne ;
- les services autonomie à domicile ;
- les professionnels et capacités externes spécialisés.

## 2. Définition

> **L’assistance personnelle capacitaire est l’ensemble des moyens humains, numériques et organisationnels permettant à une personne de maintenir, restaurer, désentraver ou augmenter sa capacité effective à conduire sa propre existence, en privilégiant l’assistance sur la substitution évitable et en subordonnant toute délégation à un mandat explicite, borné, traçable et révocable.**

Elle applique l’invariant :

> **Une capacité assistée reste une capacité de son titulaire.**

## 3. Trois régimes d’aide

### 3.1 Aide substitutive

```text
la personne ne peut pas accomplir l’acte
→ un tiers l’accomplit pour elle
```

La substitution peut être indispensable. L’assistance capacitaire ne nie ni le handicap, ni la maladie, ni la fatigue, ni les limites physiques ou cognitives réelles.

### 3.2 Assistance capacitaire

```text
la personne pourrait accomplir ou décider
si un obstacle était supprimé
→ l’assistance désentrave la capacité
```

Exemples : rendre une interface lisible, retrouver un document, expliquer un courrier, fournir une connexion réseau, rappeler une échéance, préparer les éléments nécessaires à une décision.

### 3.3 Assistance augmentée

```text
personne
+ Personal Digital Twin
+ humains
+ outils / modèles / services externes
→ capacité effective augmentée
```

Les ressources peuvent être distribuées sans déplacer le principal. Le titulaire de la capacité reste la personne tant que finalités, mandats, contrôle et traces restent effectivement rattachés à elle.

## 4. Principe de substitution minimale

L’objectif n’est pas de minimiser l’aide, mais la **substitution évitable**.

Formulation de travail :

```text
assistance personnelle capacitaire
= aide nécessaire
+ désentravement maximal raisonnable
+ substitution évitable minimale
+ maintien du choix
```

Une aide est capacitairement meilleure lorsqu’elle obtient le même niveau de sécurité et de bien-être tout en préservant ou restaurant davantage de capacité propre.

Ce principe ne doit jamais devenir une injonction à l’autonomie contre la volonté ou au détriment de la personne. Recevoir volontairement une aide alors qu’on pourrait matériellement accomplir une tâche peut être un choix légitime.

## 5. Le Personal Digital Twin comme routeur de capacité

Un Personal Digital Twin peut contribuer à déterminer quelle capacité doit être mobilisée pour satisfaire un besoin, sans devenir lui-même fournisseur universel.

```text
besoin de la personne
        ↓
Personal Digital Twin
        │
        ├─ capacité propre suffisante → information / rappel / faire soi-même
        ├─ capacité entravée → désentraver / apprendre / Serenia
        ├─ aide humaine ordinaire → prestataire adapté
        ├─ aide à l’autonomie physique → SAD / aidant compétent
        ├─ santé → professionnel de santé
        ├─ droit → professionnel compétent
        └─ action numérique → agent sous mandat explicite
```

Le routage doit prendre en compte au minimum :

- le souhait de la personne ;
- sa capacité actuelle ;
- l’importance et la réversibilité de l’acte ;
- les mandats disponibles ;
- les qualifications requises ;
- le coût ;
- le délai ;
- la confidentialité ;
- la possibilité de sortie ou de changement de prestataire.

## 6. Continuité informationnelle

L’aide à la personne est fréquemment fragmentée. La personne doit expliquer plusieurs fois son histoire, transmettre les mêmes documents et maintenir elle-même la cohérence entre famille, administrations, aidants et professionnels.

Le Twin peut devenir un **fil d’Ariane personnel** conservant, selon les autorisations du principal :

- faits utiles ;
- documents ;
- démarches ;
- échéances ;
- décisions ;
- preuves ;
- intervenants ;
- mandats ;
- préférences ;
- incidents ;
- capacités disponibles.

Le bénéfice attendu n’est pas seulement l’automatisation. Il est la réduction du coût cognitif de la continuité.

## 7. Protection et observabilité

L’assistance personnelle capacitaire doit protéger prioritairement la personne plutôt que surveiller la personne.

Le Twin peut rendre plus observables les interactions susceptibles de l’engager : contrats, factures, prélèvements, demandes administratives, messages, promesses, changements inhabituels ou décisions.

Il doit respecter le principe déjà formulé dans l’assistance non directive capacitaire :

> observer localement et inférer localement lorsque c’est possible ; divulguer le minimum nécessaire.

## 8. Frontières juridiques

L’assistance personnelle capacitaire est une **catégorie conceptuelle**, pas une qualification juridique française.

Une prestation concrète peut relever selon les cas :

- d’un service numérique ordinaire ;
- de l’assistance informatique à domicile ;
- de l’assistance administrative à domicile ;
- de la téléassistance ou visio-assistance ;
- de la coordination de services à la personne ;
- d’un service autonomie à domicile ;
- d’une profession réglementée ;
- ou d’aucune de ces catégories.

La qualification doit être faite sur l’acte effectivement fourni, son lieu, son public et son mode de réalisation. Il faut éviter de faire dériver l’ensemble de Cogentia dans un régime réglementaire du seul fait qu’un de ses usages particuliers y entre.

## 9. Twin de la personne avant Twin médical du patient

La perte d’autonomie quotidienne n’est pas uniquement médicale.

Elle peut provenir de :

- la complexité des interfaces ;
- l’absence de réseau ;
- la perte d’un mot de passe ;
- la difficulté à retrouver un document ;
- la complexité administrative ;
- la multiplication des interlocuteurs ;
- la fatigue ;
- l’isolement ;
- l’asymétrie d’information ;
- la difficulté à conserver et mobiliser une mémoire opérationnelle.

Cogentia peut donc produire une valeur capacitaire importante avant toute médicalisation du Twin. Les usages de santé doivent constituer un domaine explicitement délimité avec leur propre analyse réglementaire et scientifique.

## 10. Critère économique

Une assistance capacitaire a un coût économique même lorsque son logiciel est open source, son coût marginal d’inférence est faible ou une partie importante du travail de recherche est bénévole.

Il faut distinguer :

```text
coût de conception bénévole
≠ coût récurrent du service
≠ prix payé par le bénéficiaire
≠ valeur produite pour le bénéficiaire et la collectivité
```

Le financement peut être mutualisé ou pris en charge par un tiers sans modifier le principe capacitaire. En revanche, le modèle économique doit éviter que la dépendance de la personne devienne la source principale de rentabilité du prestataire.

Un bon modèle économique doit pouvoir bénéficier de la réussite capacitaire : prévention d’incidents, diminution des interventions évitables, meilleure orientation, mutualisation du support et réduction du coût global d’accompagnement.

L’étude des mécanismes de financement — SAP et crédit d’impôt, APA/PCH lorsque pertinentes, collectivités, caisses, complémentaires, France Travail, inclusion numérique, mécénat, fonds de dotation, dons, mutualisation et contribution des bénéficiaires — constitue un chantier séparé à documenter avec le droit positif et les critères d’éligibilité applicables.

## 11. Mesure

L’évaluation ne doit pas porter seulement sur le nombre d’actes réalisés par le service.

Indicateurs possibles :

- capacités créées, restaurées ou désentravées ;
- proportion d’actes accomplis directement par la personne lorsqu’elle le souhaite ;
- nombre d’interventions humaines évitables évitées ;
- délai de résolution ;
- incidents évités ou détectés ;
- qualité de la continuité informationnelle ;
- coût total de la capacité maintenue ;
- satisfaction et sentiment de maîtrise ;
- possibilité effective de changer de prestataire ou d’exporter le dossier ;
- diminution ou augmentation de la dépendance au système.

## 12. Hypothèse de recherche

L’augmentation rapide des capacités de l’IA peut déplacer une partie de l’aide à la personne :

```text
faire pour
→ faire avec
→ rendre capable de faire
```

Ce déplacement ne supprime pas le besoin humain. Il peut au contraire concentrer l’attention humaine sur les situations où présence, jugement, relation, geste physique, qualification professionnelle ou responsabilité sont réellement nécessaires.

Dans une société vieillissante et confrontée à des ressources humaines contraintes, la question centrale pourrait devenir moins :

> combien d’actes un service peut-il accomplir ?

que :

> combien de capacité humaine effective peut-il maintenir ou restaurer avec les ressources disponibles ?

Cette dernière question relève directement de Potentics.
