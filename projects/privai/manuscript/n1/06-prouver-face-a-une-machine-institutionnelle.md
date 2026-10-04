---
title: "PrivAI n°1 — Chapitre 6 : Prouver face à une machine institutionnelle"
subtitle: "Traces, chronologie, conservation, provenance et reconstruction"
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
version: "0.1"
status: "working-paper"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/privai/manuscript/n1/06-prouver-face-a-une-machine-institutionnelle.md"
document_role: "source"
document_kind: "manuscript-chapter"
visibility: "public"
lifecycle_state: "working"
ai_assisted_by:
- "Antigravity (Gemini 3.8 Flash High) — drafting assistance, 2026-10-04"
provenance:
  origin_type: "corpus-derivation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "research/traceabilite_des_actes.md"
  origin_date: "2026-05-18"
---

# Chapitre 6 : Prouver face à une machine institutionnelle

## 1. L'inégalité devant la preuve

Dans tout litige qui oppose un citoyen à une grande organisation (administration fiscale, opérateur de télécommunications, banque de dépôt ou plateforme de réseaux sociaux), le nœud du conflit réside dans **l'accès et la validité de la preuve**.

L'institution possède les serveurs, conserve les journaux de connexion (*logs*), définit les horodatages, paramètre les règles d'effacement automatique et choisit les extraits qu'elle accepte de communiquer. L'individu, lui, ne dispose le plus souvent que de captures d'écran contestables, d'emails isolés ou de sa propre bonne foi.

Dès lors que l'institution déploie des systèmes d'IA pour automatiser la détection des anomalies, les contrôles de conformité ou le blocage d'accès, cette asymétrie probatoire devient absolue :
- la machine institutionnelle génère des millions de traces cryptées inaccessibles à l'administré ;
- l'individu est sommé de prouver un fait négatif (*« prouvez que vous n'avez pas commis l'infraction signalée par notre réseau neuronal »*) ;
- en cas d'erreur flagrante, l'institution brandit le rapport statistique de ses outils comme une vérité scientifique objective indiscutable.

Rétablir la souveraineté humaine exige d'armer la personne physique d'une infrastructure probatoire autonome capable d'opposer des preuves matérielles vérifiables aux allégations des machines institutionnelles.

---

## 2. La chaîne minimale d'imputabilité

Pour briser la dilution décisionnelle, le document doctrinal *Traçabilité des actes* (§3) définit la **chaîne minimale d'imputabilité** à laquelle tout système d'action numérique doit impérativement se conformer :

```text
Trace vérifiable
  ↓
Imputation humaine (qui a agi ou ordonné ?)
  ↓
Justification matérielle (en vertu de quel mandat ou règle ?)
  ↓
Possibilité de correction contradictoire
  ↓
Sanction ou révocation effective en cas d'arbitraire
```

Si l'un de ces maillons est manquant ou obscurci, le système bascule dans l'arbitraire. 

En pratique, les organisations contemporaines s'ingénient à saboter cette chaîne par **quatre stratégies types de dilution de la responsabilité** :
1. *« L'institution a décidé »* (dilution par la masse anonyme) : le directeur renvoie au conseil d'administration, qui renvoie aux comités d'éthique, qui renvoient à la gouvernance globale. Nul n'est coupable parce que tout le monde est réputé agir au nom de l'entité abstraite.
2. *« Le processus a été respecté »* (dilution par la conformité procédurale) : le respect formel des étapes d'un formulaire certifié ISO ou d'un flux de travail interne tient lieu de justification morale et juridique, indépendamment de l'injustice flagrante du résultat.
3. *« Le système l'a proposé »* (dilution technique) : l'opérateur humain affirme qu'il n'a fait que valider la recommandation de l'application métier, tout en reconnaissant qu'il ne disposait que de trois secondes pour l'examiner.
4. *« Le modèle l'a recommandé »* (l'alibi algorithmique suprême) : le recours à un réseau de neurones profond dont l'inscrutabilité mathématique est érigée en force majeure cognitive dédouanant toute responsabilité humaine.

PrivAI pose comme règle cardinale le refus catégorique de ces quatre alibis : **tout acte opposable à une personne physique doit pouvoir être rattaché à une chaîne humaine de mandat identifiable, explicitable et sanctionnable.**

---

## 3. Traces négatives et reconstruction temporelle

Une traçabilité émancipatrice ne se limite pas à accumuler passivement des fichiers de journalisation. Elle repose sur deux exigences techniques et juridiques rigoureuses :

### La trace négative
Dans l'expérience quotidienne des citoyens face aux bureaucraties, l'arme la plus destructrice n'est pas toujours la décision injuste explicite : c'est **le silence, l'inertie et l'absence de réponse**. 
Une trace négative documente formellement l'absence d'acte : elle enregistre de manière irréfutable qu'une requête a été déposée le jour J à telle heure, que le délai légal est forclos, et qu'aucune réponse motivée n'a été émise par l'autorité compétente. La trace négative ne spécule pas sur l'intention cachée de l'administration ; elle matérialise l'anomalie temporelle et ouvre droit aux recours pour déni de service.

### La reconstructibilité temporelle intégrale
Un rapport d'audit algorithmique fourni trois ans après les faits est dénué de valeur probante s'il ne permet pas de reconstituer exactement **l'état du système au millième de seconde où la décision litigieuse a été scellée**.
La personne morale doit être contrainte de prouver :
- la version exacte du modèle (empreinte cryptographique des poids) ;
- les données d'entrée fournies au modèle au moment T ;
- les règles de filtrage alors en vigueur ;
- l'identité de l'agent ou de l'opérateur humain qui a validé la recommandation.

Sans cette reconstructibilité, l'auditabilité n'est qu'un théâtre managérial. Donner aux citoyens les moyens de générer des **reçus cryptographiques infalsifiables** de leurs interactions avec les personnes morales constitue le premier jalon de leur contre-pouvoir probatoire.
