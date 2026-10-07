---
title: "Annexe documentation — double lecture grand public / experts"
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
version: "0.3"
status: "active — documentation layer"
language: "fr"
document_role: "legal-documentation-annex"
document_kind: "dual-reading-documentation"
visibility: "public"
lifecycle_state: "active"
---

# Annexe documentation — deux niveaux de lecture

## Objet

Le dossier doit pouvoir être lu par deux publics sans produire deux vérités.

### Lecture grand public

Objectif :
- comprendre ce qui s'est passé ;
- pourquoi chaque acte a été accompli ;
- quelles règles étaient en jeu ;
- ce qui était matériellement possible ;
- ce qui a été demandé ;
- ce qui a reçu une réponse ;
- ce qui est resté inconnu ;
- pourquoi cela importe pour l'effectivité du droit de candidature et du recours.

Cette lecture peut être longue. Elle privilégie :
- définitions ;
- narration ;
- chronologie ;
- exemples ;
- transitions ;
- contexte ;
- explication des acronymes et procédures ;
- distinction faits / règles / interprétations.

### Lecture expert

Objectif :
- vérifier rapidement les propositions juridiques et probatoires ;
- accéder aux textes, précédents, pièces et qualifications ;
- éviter la répétition de connaissances communes aux praticiens.

Cette lecture privilégie :
- références précises ;
- propositions courtes ;
- citations d'articles ;
- jurisprudence ;
- renvois P-xx ;
- tableaux de griefs ;
- chaîne causale ;
- demandes d'instruction ;
- limites et adversarial facts.

## Invariant

Les deux niveaux ne doivent jamais diverger.

~~~text
GRAND PUBLIC = expansion pédagogique du même claim
EXPERT = compression référencée du même claim
~~~

Une contradiction entre les deux est un bug de dossier.

## Architecture recommandée pour chaque grande section

1. **Lecture immédiate / grand public** — 3 à N paragraphes expliquant l'événement, la finalité et l'enjeu.
2. **Lecture experte** — règle, source, pièce, qualification, objection adverse, conséquence.
3. **Ce qui est établi / ce qui ne l'est pas**.
4. **Pourquoi ce point compte dans le recours**.
5. **Renvois documentaires**.

## Documentation transverse à fournir

- glossaire ;
- carte des acteurs ;
- chronologie détaillée ;
- schéma préfecture → TA → Conseil constitutionnel ;
- explication du dépôt de candidature sénatoriale ;
- explication de L.298 / L.299 / L.303 ;
- fiche sur l'article 34 et les canaux de saisine ;
- fiche sur la preuve électronique et la traçabilité ;
- fiche sur les statuts probatoires ;
- lecture guidée du bordereau ;
- tableau « question → trace → réponse → inconnue » ;
- tableau des solutions praticables avant 18 h le 11 septembre ;
- tableau des remèdes demandés et de leur portée.

## Longueur et complétude

La concision n'est pas une finalité autonome.

Le dossier initial doit contenir en substance tous les griefs matériels avant l'expiration du délai ; un grief nouveau soulevé ensuite peut être déclaré irrecevable. Les pièces doivent être annexées conformément à l'article 35, qui ne prévoit qu'une possibilité **exceptionnelle** de délai supplémentaire pour une partie des pièces.

La documentation peut donc être longue si cette longueur :
- ferme une ambiguïté ;
- rend une pièce intelligible ;
- empêche une interprétation erronée ;
- préserve un fait ou un grief matériel ;
- permet à un lecteur extérieur de comprendre le dossier sans le Corpus.

Elle doit en revanche rester structurée afin que la longueur ne masque pas le noyau juridique.


## La Traçabilité des Actes appliquée au présent dossier

La traçabilité n'est pas ici une théorie détachée du litige. Elle répond à une question très concrète : peut-on reconstituer, après coup et de manière contradictoire, ce qui a été reçu, transmis, examiné et décidé ?

Le Corpus contient depuis mai 2026 une note doctrinale autonome, `research/traceabilite_des_actes.md`, consacrée à cette question. Elle définit la traçabilité comme la capacité à retrouver l'existence, le contexte, l'auteur, la justification, les effets et les corrections éventuelles d'un acte engageant. Elle insiste également sur la « trace négative » : une demande sans réponse, une réponse incomplète, un refus explicite ou une information indisponible peuvent être enregistrés comme faits procéduraux sans être transformés en accusation.

Dans le présent dossier, cette grille éclaire plusieurs séquences.

### La réception du courriel du 11 septembre à 17 h 57 min 55 s

Le requérant établit l'envoi du courriel contenant le lien vers la déclaration vidéo avant l'heure limite de 18 heures. La question qui subsiste est celle de son arrivée dans l'infrastructure de l'État, de son éventuel traitement avant la saisine du Tribunal administratif et de sa transmission ultérieure.

Une trace de réception horodatée, un journal de messagerie ou un historique de routage pourrait fermer cette question dans un sens ou dans l'autre.

### La constitution de la saisine préfectorale

P-14 permet d'identifier les seize pièces de l'ensemble initial transmis au Tribunal administratif. Il reste utile de pouvoir distinguer la création du fichier, sa finalisation, sa validation, l'ajout des pièces et son enregistrement dans Télérecours.

Cette distinction importe parce qu'un document peut avoir été reçu par la préfecture sans avoir été intégré à un ensemble déjà préparé, ou au contraire avoir été ajouté avant la transmission finale.

### Les productions complémentaires

L'absence d'une pièce dans l'inventaire initial ne permet pas de conclure qu'elle n'a jamais été transmise ensuite.

La bonne question est donc positive : existe-t-il une production complémentaire, un bordereau, un courriel, une entrée Télérecours ou toute autre trace montrant qu'un élément a été ajouté au dossier avant le jugement ?

### L'accès de la formation de jugement aux pièces

La présence matérielle d'un document dans un dossier, sa communication aux parties et son examen effectif par la formation de jugement sont trois faits différents.

La traçabilité permet de les distinguer au lieu de les confondre.

### Les modalités de remise du recours

La même question se retrouve au stade du recours devant le Conseil constitutionnel. Le requérant a demandé comment remettre une requête au représentant de l'État au titre de l'article 34 : lieu, canal, heure limite pratique et preuve de réception.

Dans une procédure enfermée dans un délai bref, ces informations ne sont pas de simples détails logistiques. Elles conditionnent la possibilité de démontrer qu'un recours a été remis dans les temps.

### Pourquoi la traçabilité protège les deux parties

Une trace fiable ne sert pas seulement à révéler une éventuelle erreur.

Elle protège aussi l'administration et la juridiction. Si un journal établit qu'un courriel a été reçu après 18 heures, qu'une pièce a bien été transmise ou qu'un document figurait effectivement au dossier du juge, la contestation correspondante peut être fermée immédiatement.

La traçabilité réduit donc les conflits inutiles. Elle remplace les souvenirs, suppositions et reconstructions par des faits vérifiables.

### Ce que produit l'absence de traçabilité

Lorsqu'une trace nécessaire n'est pas disponible, plusieurs conséquences apparaissent :

- il devient plus difficile de distinguer une erreur, un oubli, un choix ou un incident technique ;
- les responsabilités se diluent ;
- la correction devient plus difficile ;
- le contradictoire s'appauvrit ;
- les hypothèses se multiplient ;
- le recours peut devenir moins effectif si le délai expire avant que les faits nécessaires soient accessibles.

Aucune de ces conséquences ne permet, à elle seule, d'attribuer une intention.

Elles suffisent en revanche à expliquer pourquoi le requérant demande au Conseil, lorsqu'il l'estime utile, de se faire communiquer les traces détenues par les institutions concernées.

## Évolution observable des réponses institutionnelles

Une note d'enquête autonome, `investigation/evolution-reponses-interlocuteurs-etatiques-2026-09-15-2026-10-07.md`, rassemble cette séquence.

Elle montre que plusieurs demandes logistiques, documentaires ou d'accès ont reçu une réponse : orientation vers Sagace, proposition de Télérecours Citoyens, consultation des pièces électorales, organisation du rendez-vous du 1er octobre.

Dans le même temps, les demandes portant sur la réception du courriel de 17 h 57 min 55 s, les transmissions initiales ou complémentaires au Tribunal, la chronologie de validation de la saisine, les traces matérielles d'audience et les modalités de remise du recours demeurent plus souvent ouvertes.

Cette observation doit être lue avec une qualification précise de chaque cas : réponse absente, réponse non retrouvée, réponse partielle, réponse hors sujet ou information explicitement déclarée indisponible.

La séquence ne permet pas, par elle-même, d'identifier une cause unique. Elle documente en revanche un problème d'effectivité : certaines informations nécessaires à la vérification contradictoire restent difficiles à obtenir dans le temps utile.


## Pourquoi les deux QPC sont générales

Une question prioritaire de constitutionnalité naît dans un litige concret, mais elle porte sur une disposition législative générale.

Le cas Robert–Vernerey permet d'établir que L.299 et L.303 sont applicables et que leurs effets ne sont pas hypothétiques. La réponse recherchée doit cependant valoir pour toute situation juridiquement comparable.

Pour **L.299**, la question est générale : comment une formalité manuscrite doit-elle s'appliquer lorsqu'un remplaçant est empêché par un handicap d'accomplir personnellement le geste alors que son consentement peut être établi ?

Pour **L.303**, la question est générale : quelles garanties doivent exister lorsqu'une candidature est exclue avant le scrutin et que la loi ferme toute autre contestation jusqu'au contentieux de l'élection ?

Cette généralité empêche de réduire les QPC aux seules personnes du présent dossier.


## Pourquoi les treize jours comptent

Le Tribunal administratif a statué le **14 septembre 2026**.

Le scrutin a eu lieu le **27 septembre 2026**.

Il s'est donc écoulé **treize jours calendaires** entre le jugement d'exclusion et le vote.

Pendant cette période, le dommage n'était pas encore complètement consommé : la candidature pouvait encore, matériellement, participer au scrutin si une décision juridictionnelle utile était intervenue.

L'article L.303 impose pourtant au Tribunal administratif de statuer en trois jours puis prévoit que son jugement ne peut être contesté que devant le Conseil constitutionnel saisi de l'élection.

La difficulté peut être résumée ainsi :

> **trois jours pour décider ; treize jours sans autre voie de contestation utile ; puis le scrutin rend l'exclusion irréversible.**

La question constitutionnelle n'est donc pas seulement celle d'un second degré de juridiction. Elle porte sur l'existence d'un contrôle utile pendant une période où l'atteinte peut encore être évitée.

## Lecture guidée de P-43 — correspondance contemporaine avec Laurence Vernerey du 7 au 14 septembre

Deux sous-pièces sont particulièrement importantes :

- **P-43.a — courriel « Autorisation » du 10 septembre 2026** : Laurence Vernerey autorise expressément Jean Hugues Robert à utiliser sa signature sur le CERFA où elle se porte remplaçante ;
- **P-43.b — courriel « Porte-parole » du 11 septembre 2026** : elle le désigne expressément comme porte-parole de la campagne.

Ces pièces ne remplacent pas les formalités électorales. Elles documentent la volonté, le consentement et la demande faite au tiers.

## Lecture guidée de P-45 — demandes et relances sur les modalités pratiques de remise du recours

P-45 rassemble quatre démarches distinctes des 26 septembre, 28 septembre, 1er octobre et 2 octobre 2026.

Elles documentent la recherche, avant l'échéance, du lieu, du canal, de l'heure pratique et de la preuve de réception nécessaires à la remise d'une requête au représentant de l'État.

La proposition probatoire doit rester exacte : **aucune réponse substantielle n'a été retrouvée sur ces modalités malgré les demandes identifiées**. Cela ne signifie pas que l'administration n'a répondu à aucune autre demande.
