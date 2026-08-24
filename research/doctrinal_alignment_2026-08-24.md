---
title: "Alignement doctrinal — souveraineté, délégation et Agents Mandatés"
author: "Jean Hugues Noël Robert"
date: "2026-08-24"
version: "1.0"
status: "source — consolidation"
license: "CC BY-SA 4.0"
document_role: "source"
visibility: "public"
human_validation_required: true
related:
  - "./souverainete_delegation_agents_mandates.md"
  - "./noyau_doctrinal_rendre_capable.md"
  - "./democratie_capable.md"
  - "./kudocracy.md"
  - "./methode_terrains_feconds.md"
  - "./debord_stabilisateur_procedural.md"
  - "./security_model_representative_democracy.md"
---

# Alignement doctrinal — 24 août 2026

Ce document fixe l'alignement conservatif de plusieurs documents plus anciens avec la source transversale `souverainete_delegation_agents_mandates.md`. Il ne remplace pas leurs apports propres. En cas de contradiction sur les notions ci-dessous, la formulation la plus récente prévaut jusqu'à intégration éditoriale dans chaque source.

## 1. Délégation sans aliénation

Une délégation n'est pas, au sens doctrinal retenu ici, un transfert de propriété du pouvoir. Elle est l'autorisation bornée d'exercer une capacité qui demeure rattachée à sa source de légitimité.

Formule canonique :

> **Déléguer l'exercice d'une capacité n'aliène ni sa source, ni le droit de contrôle, ni le droit de reprise du principal, sous réserve des droits des tiers et des règles constitutives légitimes.**

Conséquence pour `kudocracy.md` : les formulations « transfert de pouvoir décisionnel », « la délégation transfère un pouvoir » et « je transfère temporairement mon vote » doivent être lues comme des raccourcis décrivant l'exercice délégué. Elles ne signifient ni cession de la source du pouvoir, ni abandon de souveraineté. La prochaine révision éditoriale de Kudocracy devra employer « autorisation d'exercice » ou « exercice délégué ».

## 2. Agent Mandaté

Un **Agent Mandaté** est un acteur humain, logiciel, institutionnel ou hybride qui exerce des capacités au nom d'un principal dans un périmètre explicite, versionné, borné, traçable et révocable.

Son autonomie peut être élevée dans l'exécution. Son autorité ne s'étend pas d'elle-même.

```text
autonomie opérationnelle != autonomisation de l'autorité
```

Un Agent Mandaté ne peut inférer une compétence du silence, étendre son propre mandat, augmenter ses budgets ou ses privilèges sans autorité distincte, ni transformer une recommandation en autorisation.

## 3. Souveraineté comme capacité effective

La souveraineté formelle est insuffisante si le principal ne peut comprendre, contester, corriger, révoquer ou reprendre l'exercice des capacités déléguées.

Cette règle relie directement :

- `noyau_doctrinal_rendre_capable.md` : droit abstrait -> capacité effective ;
- `democratie_capable.md` : souveraineté populaire -> infrastructure de décision et de reprise ;
- `security_model_representative_democracy.md` : selection is not security, non-auto-élévation et reprise ;
- `kudocracy.md` : suggestion, recommandation, délégation et votation ;
- `debord_stabilisateur_procedural.md` : mandat, provenance, séparation des capacités, révocation et remédiation.

## 4. Portabilité de capacité

La portabilité ne porte pas seulement sur les données. Une capacité réellement souveraine doit pouvoir, autant que raisonnablement possible, changer d'implémentation sans perdre son identité fonctionnelle, son historique pertinent, ses mandats, ses preuves et ses possibilités de reprise.

> **Exporter les données sans pouvoir rétablir la capacité est une portabilité incomplète.**

Cette règle généralise la « portabilité et pluralité d'infrastructure » du Stabilisateur procédural.

## 5. Pluralité d'implémentations, politique commune

Une doctrine de souveraineté ne doit pas dépendre d'une implémentation unique. Plusieurs runtimes, modèles, fournisseurs, interfaces ou organisations peuvent réaliser la même politique, à condition de respecter les invariants communs.

```text
politique commune
+ implémentations plurielles
+ preuves de conformité
= résistance à la capture
```

## 6. Méthode des terrains féconds

L'opposition « autonomie / délégation » est un terrain stérile si elle suppose qu'agir soi-même et faire agir autrui sont exclusifs.

Terrain reconfiguré :

> **souveraineté de la source, liberté d'organisation de l'exécution.**

De même, l'opposition « centralisation / décentralisation » peut être reconfigurée en :

> **règles communes vérifiables, capacités distribuées et reprenables.**

Ces formulations prolongent le principe « protocole commun, opérations libres » sans l'annuler.

## 7. Test d'architecture

Toute implémentation agentique prétendant servir cette doctrine doit permettre de répondre à neuf questions :

1. Qui est le principal ?
2. Quelle capacité est exercée ?
3. Quel mandat l'autorise ?
4. Quelles sont ses bornes de portée, durée et ressources ?
5. Qui peut modifier ces bornes ?
6. Quelle trace prouve l'acte et son autorisation ?
7. Comment le principal peut-il suspendre, corriger ou reprendre ?
8. Comment la capacité peut-elle être portée vers une autre implémentation ?
9. Quel mécanisme empêche l'agent de devenir sa propre autorité ?

Une réponse absente n'est pas automatiquement une vulnérabilité, mais elle doit être explicitement justifiée.

## 8. Règle de non-régression

Les révisions futures des documents liés doivent préserver les acquis propres de chaque texte. L'alignement ne doit pas homogénéiser artificiellement le corpus. Il corrige les contradictions de vocabulaire et stabilise les invariants transversaux, tout en conservant les différences de niveau : philosophie, démocratie, protocole, sécurité, architecture agentique et expérimentation.
