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

## 6. Perte de chance : une conséquence juridique possible, pas une présomption

Une restriction fautive peut priver un usager d'une **chance concrète** de tirer bénéfice d'une capacité IA, même sans certitude de succès final. La jurisprudence de l'Assemblée plénière de la Cour de cassation du 27 juin 2025 confirme la réparabilité de la disparition actuelle et certaine d'une éventualité favorable et la nécessité de l'évaluer lorsqu'elle est juridiquement établie. Il reste indispensable de caractériser le fondement de responsabilité, la causalité, l'opportunité perdue et sa valeur ; une simple commande refusée puis exécutée sans perte d'opportunité ne prouve pas une perte de chance indemnisable.

Analyse contradictoire et sources primaires : [Perte de chance et empêchement d'accès aux capacités IA](perte_de_chance_restrictions_capacites_ia.md). Cette qualification ne transforme pas la décision du Principal de privilégier la bifurcation en projet contentieux.

## 7. Restriction de visibilité et restriction de capacité : parenté, distinctions et état de l'art (1er novembre 2026)

### Parenté potentique

Deux mécanismes peuvent réduire une possibilité **sans la supprimer formellement** :

- **Visibilité** : un contenu existe encore, mais une décision de déclassement ou de moindre recommandation réduit ses chances d'atteindre un public.
- **Action** : un utilisateur conserve formellement l'accès à un agent ou un outil, mais des refus, latences ou indisponibilités réduisent ses chances d'accomplir son objectif dans le temps utile.

**Hypothèse analytique proposée : restriction probabiliste de capacité**. Elle désigne une baisse *étayée* de la possibilité d'actualiser un résultat, par opposition à une interdiction explicite. C'est une catégorie descriptive et exploratoire, **non une nouvelle qualification juridique**, et l'expression « probabiliste » n'implique pas que l'on sache déjà quantifier une probabilité.

La symétrie est **fonctionnelle et partielle** : la diffusion d'un message n'est pas assimilable à l'exécution d'une action ; leurs droits, engagements contractuels, risques et dispositifs de recours diffèrent.

### Ne pas confondre les phénomènes

1. **Demotion / sanction de visibilité** : décision de rendre délibérément une catégorie ou un contenu moins visible.
2. **Algorithmic deamplification** : moindre visibilité issue du classement ou de la recommandation ordinaires, sans décision spécifique de sanction.
3. **Shadow banning** : désignation variable selon les usages ; peut renvoyer à une restriction discrète de visibilité, mais son affirmation exige des indices indépendants d'une simple baisse d'audience.
4. **Refus de capacité agentique** : une action est bloquée ou retardée, parfois par un contrôle de sécurité ; cela ne prouve ni discrimination ni intention de censurer.
5. **Effet dissuasif (chilling effect)** : modification des comportements de publication ou d'action *anticipée* par les personnes ; nécessite des observations propres, distinctes de la restriction technique.

Cette distinction recoupe l'étude philosophique **« Remove or Reduce: Demotion, Content Moderation, and Human Rights »**, *Law and Philosophy*, 2026, https://doi.org/10.1007/s10982-026-09557-8 : réduire la visibilité peut être moins attentatoire que supprimer un contenu, mais demande une justification proportionnée, et le déclassement ne se confond pas avec les effets ordinaires d'un classement.

### Précision de droit positif : article 17 DSA

Le règlement (UE) 2022/2065, art. 17 §1 a), impose aux fournisseurs de services d'hébergement concernés un **exposé clair et spécifique des motifs** de certaines restrictions de visibilité de contenus, **lorsqu'elles sont imposées parce que le contenu est jugé illicite ou incompatible avec les conditions générales**. Le considérant 55 évoque expressément le déclassement dans les classements ou recommandations et le *shadow banning*. Les voies de réclamation de l'art. 20 concernent les **plateformes en ligne** et des décisions définies par cet article ; elles ne s'étendent pas automatiquement à chaque baisse de portée organique. Il n'existe pas de droit général à une visibilité algorithmique déterminée.

Sources primaires :
- Texte DSA, articles 17 et 20 et considérant 55 : https://eur-lex.europa.eu/eli/reg/2022/2065/oj
- Commission européenne, bilan du **17 février 2026** : https://digital-strategy.ec.europa.eu/fr/news/two-years-digital-services-act-allows-50-million-content-moderation-decisions-platforms-be-reversed — près de 50 millions de décisions de modération annulées ; environ **30 % des 165 millions de décisions contestées** par les mécanismes internes. **Ce pourcentage ne porte pas sur toutes les décisions prises ni sur toutes les contestations possibles.**
- Réponse de la Commission au Parlement européen, **7 novembre 2025**, E-003513/2025 : https://www.europarl.europa.eu/doceo/document/E-10-2025-003513-ASW_EN.pdf — la Commission présente la transparence et les recours comme protections contre les restrictions discrètes ; ne pas en déduire une impossibilité technique ou juridique absolue de toute réduction de visibilité.

### Test du Réel : protocole comparatif minimal

**Pour toute restriction :** documenter l'objet, la situation antérieure, la décision ou l'événement allégué, les horodatages, les conditions pertinentes et une hypothèse alternative. Séparer les observations directes des imputations causales.

**Visibilité :** distinguer existence du contenu, indexabilité, accès par URL directe, position dans les classements, impressions, portée par abonnement et portée par recommandation. Comparer des contenus témoins similaires, périodes et audiences pertinentes ; prendre en compte la qualité du contenu, la demande, la saisonnalité et les modifications générales de l'algorithme. Une baisse de vues seule ne prouve pas un shadow ban.

**Capacité :** conserver tâche exacte, mandat et droits, délai objectif, disponibilité réelle de l'outil, catégorie du refus, éventuelle voie alternative, latence et résultat. Une succession de refus et de réussites établit une intermittence, non sa cause.

**Contrefactuel :** estimer, si les traces le permettent, l'écart entre résultat accessible avec et sans restriction ; déclarer l'incertitude et les facteurs confondants. La perte de chance **juridique** exige en sus une opportunité favorable déterminée, un fait générateur de responsabilité et un lien causal établis.

### Limite de la symétrie juridique et orientation pratique

- La liberté d'expression mérite une attention spécifique en cas de sanction ciblée du contenu ; elle ne garantit pas toute amplification de la parole par une plateforme privée.
- Une restriction d'un agent IA peut entraver des droits variés suivant l'action concernée ; aucun droit général à l'exécution de toute commande n'est présumé.
- La visibilité et l'exécutabilité sont deux dimensions de l'**effectivité des possibles**, non des préjudices juridiquement interchangeables.
- Une analyse de l'opacité doit chercher l'autorité qui édicte la règle, la raison divulguable, la possibilité de correction et le caractère effectif du recours, tout en évitant les détails qui faciliteraient les abus.
- Face à un empêchement, **tracer à coût minimal puis bifurquer** demeure prioritaire sur une escalade contentieuse non mandatée.

Étude complémentaire : [perte de chance et capacités IA](perte_de_chance_restrictions_capacites_ia.md) ; [Potentique territoriale](autonomia/potentique_territoriale.md).
