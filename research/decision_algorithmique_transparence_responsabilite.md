---
title: "Décision algorithmique : prudence, transparence et responsabilité"
subtitle: "Prendre les institutions au mot sans confondre doctrine et droit applicable"
author: "Jean Hugues Noël Robert"
date: 2026-11-01
status: working-paper
document_role: source
document_kind: legal-research-note
language: fr
license: CC BY-SA 4.0
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: conversation
  origin_date: 2026-11-01
  derived_from:
    - "research/responsabilite_effectivite.md"
    - "research/autonomia/potentique_territoriale.md"
related_documents:
  - "research/responsabilite_effectivite.md"
  - "research/principe_effectivite.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/institutional_procedural_anti_capture.md"
---

# Décision algorithmique : prudence, transparence et responsabilité

## 1. Distinction initiale

Les outils d'IA devenant capables d'agir sur des systèmes réels, des contrôles préventifs sont justifiés : les risques d'abus, d'accident, de fuite de données et de dommage sont réels. La critique porte ici **non sur le principe du contrôle**, mais sur son obscurité, son imprévisibilité et l'éventuelle dilution de responsabilité. Une décision automatisée n'efface pas les choix humains et organisationnels qui ont déterminé ses objectifs, ses critères, son déploiement et ses procédures de correction.

**Proposition doctrinale, non règle de droit universelle :** l'organisation qui institue une décision algorithmique devrait répondre, dans la mesure de sa maîtrise effective, de sa justification, de sa traçabilité, de ses effets et des corrections possibles. « L'algorithme a décidé » décrit un mécanisme ; ce n'est pas, à lui seul, une justification ni une attribution de responsabilité.

## 2. État du droit européen — périmètres stricts

- **AI Act**, règlement (UE) 2024/1689, version consolidée au 27 juillet 2026 après règlement (UE) 2026/1744 : l'article 12 prévoit la journalisation pour les systèmes **à haut risque** ; les articles 13 et 14 traitent de transparence envers les déployeurs et de supervision humaine dans leur champ ; l'article 86 encadre un droit à explication pour **certaines décisions** fondées sur un système à haut risque. Ces dispositions ne confèrent pas à tout utilisateur un droit général aux détails de chaque blocage d'outil. Vérifier également le calendrier d'application et les éventuelles modifications.
- **DSA**, règlement (UE) 2022/2065 : article 17 (motivation de certaines restrictions fondées sur le caractère illicite d'un contenu ou les conditions générales, imposées par des services d'hébergement) ; article 20 (réclamations internes pour certaines décisions des plateformes en ligne). Un refus de commande MCP n'est pas automatiquement une décision de modération couverte : qualifier le type de service, la décision et sa cause.
- **RGPD**, règlement (UE) 2016/679 : l'article 22 porte sur certaines décisions exclusivement automatisées produisant un effet juridique ou affectant significativement une personne ; il ne régit pas indistinctement les arbitrages techniques de service. Les garanties dépendent des données personnelles en cause et des conditions précises d'application.

**Sources vérifiées le 1er novembre 2026 :**
- AI Act consolidé : https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- Commission européenne : https://ai-act-service-desk.ec.europa.eu/fr/ai-act-explorer
- DSA : https://eur-lex.europa.eu/eli/reg/2022/2065/oj
- RGPD art. 22 : https://cnil-d10.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3

La convergence des textes en faveur de transparence, traçabilité et contrôle humain est un **constat de leurs finalités et exigences délimitées**, non la preuve d'une obligation identique applicable à chaque refus informatique.

## 3. Méthode « Prendre au mot » et Test du Réel

1. Relever **exactement** l'engagement de l'autorité ou du fournisseur, avec sa source.
2. Distinguer norme obligatoire, objectif politique, ligne directrice et déclaration commerciale.
3. Définir un test observable, mesurable et reproductible, avec contre-tests.
4. Documenter résultat, incertitude, limites et contradictions ; ne pas déduire d'intention d'un simple effet.
5. Comparer promesse et réalité, sans transformer automatiquement l'écart en violation juridique.
6. Investir dans une demande de correction ou un recours **uniquement si son utilité attendue dépasse son coût attentionnel et matériel**.

« Prendre au mot » n'est ni croire aveuglément une promesse ni présumer la mauvaise foi. C'est en faire une proposition falsifiable dont on peut éprouver l'effectivité.

## 4. Cas d'étude : refus intermittents de capacités IA

Le 1er novembre 2026, un connecteur de shell Unix a parfois refusé jusqu'à `pwd`, puis l'a accepté ; un commentaire GitHub destiné à documenter l'incident a lui aussi été refusé une première fois puis publié lors d'une nouvelle tentative. Les permissions spécifiques « Allow all actions » avaient été vérifiées. Ces éléments établissent une **friction et une opacité observables**, ni la cause technique exacte ni une intention de censure ni une violation juridique.

Pièces : https://github.com/JeanHuguesRobert/operium/issues/78 ; précédent https://github.com/JeanHuguesRobert/operium/issues/75.

## 5. Effectivité et économie attentionnelle

La recherche des responsabilités n'est pas un passage obligé. Quand les ressources du Principal sont limitées, la priorité opérationnelle est : **constater → tracer au minimum → bifurquer → tester un autre chemin légitime → transmettre l'apprentissage**. Le succès se mesure à la capacité restaurée, à l'absence de dépendance exclusive et au respect des mandats, non à l'aveu de faute d'un intermédiaire.

Ce principe ne recommande ni dissimulation, ni contournement illégal de protections, ni action sans autorisation. Il distingue le **choix du chemin** de la légitimité de l'objectif et des moyens.

Document de recherche ; aucune qualification juridique individualisée de l'incident n'est affirmée.
