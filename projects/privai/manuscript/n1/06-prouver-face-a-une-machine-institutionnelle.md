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
- "Antigravity (Gemini 3.8 Flash High) — drafting assistance, 2026-10-04, 2026-10-05"
provenance:
  origin_type: "corpus-derivation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "research/traceabilite_des_actes.md"
  origin_date: "2026-05-18"
  derived_from:
    - "barons-Mariani/research/trace_epistemology.md"
    - "barons-Mariani/projects/privai/cases/case-03-traceabilite-dilution-decisionnelle.md"
    - "barons-Mariani/projects/privai/cases/case-06-horizon-presomption-fiabilite-machine.md"
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

---

## 4. La rupture ontologique : du mirage « Event-Centric » à l'épistémologie « Trace-Centric »

L'informatique institutionnelle classique et les architectures de surveillance contemporaines reposent sur un biais réductionniste hérité de l'*Event Sourcing* : modéliser le monde sous la forme d'un flux d'« Événements » (`Events`).

Cette approche postule implicitement que le système central est un témoin omniscient, objectif et impartial qui consigne des événements pré-catégorisés dans un ordre chronologique idéal (*« L'utilisateur X a transféré un fichier interdit à 14h02 »*). Or, l'analyse épistémologique du Corpus (*Épistémologie des traces*, §3.1.1) démontre que ce postulat est une imposture cognitive :
- **Le réel matériel ne produit jamais des événements tout faits : il produit des traces.** Une trace est une altération physique, magnétique, thermique, biologique ou cryptographique brute, asynchrone, partielle, située et fragile.
- **L'« Événement » est une construction interprétative seconde :** c'est une narration causale rétrospective imposée par l'institution sur un faisceau tronqué de traces sélectionnées pour conforter son propre récit.

Dans l'état abstrait formel développé dans l'architecture JHN :
$$\mathcal{J} = (P, H, S, T)$$
où $P$ représente la Politique de contraintes, $H$ les capacités d'exécution (*Hop/RAIX*), $S$ la mémoire d'état interne mutable et $T$ le journal immuable des Traces, **seule la Trace $T$ constitue le socle opposable de la preuve**. Les états internes $S$ peuvent être corrompus ou réécrits unilatéralement par les administrateurs du serveur ; les moteurs d'inférence $H$ peuvent être modifiés : seule la Trace matérielle partagée $T$ résiste à la falsification rétrospective. 

Tant que l'individu est contraint d'accepter les « Événements » décrétés par la plateforme sans avoir accès à la texture brute des traces $T$, il demeure un sujet féodal démuni de tout droit de contradiction.

---

## 5. Renverser la présomption de fiabilité machine

Le cœur juridique de l'oppression algorithmique réside dans ce que la jurisprudence anglo-saxonne a cruellement mis en lumière lors du scandale *Post Office Horizon* ([Case 06](file:///C:/tweesic/barons-Mariani/projects/privai/cases/case-06-horizon-presomption-fiabilite-machine.md)) : la **présomption d'infaillibilité de l'ordinateur** (*presumption of computer reliability*).

Depuis l'abrogation en 1999 de la section 69 du *Police and Criminal Evidence Act* au Royaume-Uni, le droit commun postule qu'un système informatique fonctionne correctement en l'absence de preuve explicite du contraire. Transposée à l'âge des réseaux neuronaux profonds et des boucles agentiques autonomes, cette présomption constitue une monstruosité juridique :
- Elle fait peser sur la personne physique la charge d'une *probatio diabolica* : l'administré ou l'employé doit démontrer la présence d'un bug dans un code source de plusieurs millions de lignes ou dans des matrices de milliards de poids synaptiques protégés par le secret des affaires et des serveurs distants !
- Elle a conduit, dans l'affaire Horizon, à la condamnation pénale pour vol et fausse comptabilité de plus de 900 gérants de succursales postales innocents, ruinés et incarcérés sur la seule foi d'écarts comptables chimériques générés par le progiciel.

PrivAI réclame le **renversement absolu de la présomption de fiabilité** dans toute interaction asymétrique :

> **Principe d'inversion probatoire :** Tout acte institutionnel défavorable fondé directement ou indirectement sur un traitement automatisé ou un modèle probabiliste est présumé entaché d'erreur matérielle jusqu'à ce que la personne morale fournisse la preuve complète, vérifiable de bout en bout et contradictoirement rejouable de la validité de sa chaîne d'inférence.

---

## 6. L'écologie probatoire personnelle et l'égalité des armes

Pour que le droit à un procès équitable et l'égalité des armes (consacrés par l'article 6 de la Convention européenne des droits de l'homme) cessent d'être des voeux pieux face aux automates corporatifs, chaque citoyen doit pouvoir déployer sa propre **écologie probatoire personnelle**.

Cette écologie ne dépend pas du bon vouloir des plateformes. Elle s'incarne matériellement dans le [Jumeau numérique souverain](file:///C:/tweesic/barons-Mariani/projects/privai/manuscript/n1/07-jumeau-numerique-souverain.md) :
1. **Le contre-journal local indépendant :** Chaque échange de paquets, chaque soumission de formulaire, chaque promesse contractuelle et chaque délai fait l'objet d'un reçu cryptographique horodaté localement, signé avec la clé privée de l'utilisateur et consigné hors de portée des serveurs institutionnels.
2. **L'alibi non-machine :** La préservation systématique d'indices contextuels issus du monde physique (géolocalisation matérielle indépendante, signatures croisées, témoins tiers, reçus matériels) permettant de démentir les hallucinations d'un algorithme de conformité.
3. **Le séquestre contradictoire des preuves :** En cas de différend naissant, le protocole impose le dépôt automatisé des traces brutes des deux parties auprès d'un tiers neutre ou dans un coffre décentralisé inviolable, interdisant à la personne morale de purger discrètement ses serveurs de diagnostic sous couvert de « maintenance de routine ».

Prouver face à la machine ne consiste pas à supplier l'algorithme d'avoir de l'empathie ; cela consiste à lui opposer une chaîne de traces plus rigoureuse, plus dense et plus inattaquable que la sienne.
