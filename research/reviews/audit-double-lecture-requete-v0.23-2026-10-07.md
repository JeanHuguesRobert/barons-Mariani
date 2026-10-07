---
title: "Audit double lecture et amélioration — requête v0.23"
author: "GPT-5.6 Sol"
date: "2026-10-07"
status: "completed — substantive pass; material filing controls remain open"
language: "fr"
document_role: "review"
document_kind: "pre-filing-improvement-audit"
visibility: "public"
review_target: "requete-conseil-constitutionnel-projet-v0.23.md"
---

# Audit double lecture et amélioration — v0.23

## Résultat

La v0.23 satisfait la structure de **double lecture grand public / expert** sur toutes les grandes sections utiles au dépôt :

- premier écran contentieux ;
- recevabilité ;
- résumé exécutif ;
- chronologie ;
- formalités et régimes normatifs ;
- solutions praticables ;
- griefs centraux ;
- temporalité ;
- conclusions ;
- bordereau et matérialisation.

Le **control plane** a été retiré du corps de la requête : check-list Cognitive Packet, protocole de revue adverse et changelogs restent dans le Corpus. Le texte destiné au Conseil conserve le data plane et les explications utiles à sa lecture.

## Améliorations de la boucle

- propagation de la dernière qualification de P-20 et de la photographie « Avenue du Baron Mariani » ;
- borne ante quem de transmission de cette photographie conservée sans la transformer en horodatage de prise de vue ;
- article L.318 réintroduit de manière bornée dans le grief d'incidence : participation légalement contrainte, sans réattribution des voix ;
- suppression de deux formulations pronominales susceptibles de créer un antécédent ambigu ;
- suppression du libellé historique « note de périmètre v0.5 » au profit d'un intitulé fonctionnel ;
- séparation plus stricte entre texte juridictionnel et outils internes de construction.

## Contrôle de cohérence

Les trois risques dominants restent inchangés :

1. dépôt effectif et preuve de réception dans le délai ;
2. portée de L.299, formalisme et handicap / empêchement fonctionnel ;
3. incidence possible sur le scrutin.

La v0.23 ne prétend pas résoudre par le style une faiblesse de preuve ou de droit. Elle rend les propositions, les réserves et les UNKNOWN plus faciles à identifier.

## État

~~~text
double lecture structurelle : PASS
séparation data plane / control plane : PASS
P-20 dernière qualification : PASS
L.318 borné : PASS
micro-style ciblé : PASS
micro-audit exhaustif de chaque phrase : non requis avant la matérialisation si aucun nouveau bug n'est détecté
paquet matériel : OPEN
gel / SHA / pagination : OPEN
preuve de réception : OPEN
~~~

## Prochaine boucle utile

La prochaine boucle doit porter d'abord sur le **paquet réel** :

~~~text
pièces A matérialisées
→ concordance requête / bordereau / fichiers
→ pagination / occultations / SHA-256
→ gel de la chronologie
→ paquet canonique
→ remise
→ preuve de réception
~~~
