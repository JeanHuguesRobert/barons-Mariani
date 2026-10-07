---
title: "Audit double lecture — requête v0.20 — grand public / experts"
author: "GPT-5.6 Sol"
date: "2026-10-07"
status: "open — substantially improved, final sentence-level pass required"
language: "fr"
document_role: "review"
document_kind: "dual-reading-audit"
visibility: "public"
review_target: "requete-conseil-constitutionnel-projet-v0.20.md"
---

# Audit double lecture — v0.20

## Résultat

La v0.20 satisfait désormais la **structure de double lecture** au niveau des grandes sections et des griefs centraux.

Elle satisfait également la plupart des sous-sections susceptibles de provoquer un malentendu : provenance numérique, périodes chronologiques, L.299, article 1366, handicap, contextes A/B, QPC/CEDH, P-14, contrôle matériel et annexe chronologique.

Le MUST n'est toutefois pas encore fermé définitivement.

## Ce qui est désormais acquis

- blocs « Grand public » et « Expert » dans toutes les grandes sections ;
- blocs dédiés dans les griefs 1, 2, 3, 4, 4 bis et 5 ;
- explicitation systématique des principales distinctions ;
- Talleyrand appliqué aux points à haut risque d'implicite ;
- grand public : phrases courtes dans les nouveaux blocs, une idée dominante par phrase, images concrètes ;
- expert : niveau juriste junior, avec règle / application / objection / conséquence explicitées.

## Contrôles encore nécessaires avant CLOSED

1. **Passe phrase par phrase sur le texte hérité de v0.19** : certains paragraphes experts restent longs et pourraient être segmentés sans perte juridique.
2. **Pronoms et références** : rechercher « cela », « ceci », « ce point », « cette pièce », « donc », « ainsi » et vérifier qu'aucun antécédent n'est ambigu.
3. **Acronymes** : vérifier première occurrence de TA, QPC, CEDH, BEDL, CRPA, DSN, SHA-256.
4. **Métaphores** : vérifier qu'elles aident et ne remplacent jamais une qualification juridique.
5. **Malentendus plausibles** : pour chaque grief, écrire ou vérifier une phrase « cela ne signifie pas que… » lorsque la confusion est probable.
6. **Conclusions** : conserver une version très courte en langage courant avant le dispositif juridique exact.
7. **Section IX / control plane** : décider au gel si elle reste dans la requête principale ou bascule en annexe documentaire, afin de ne pas distraire du noyau contentieux.

## Statut

~~~text
structure double lecture : PASS
couverture des griefs : PASS
Talleyrand sur distinctions majeures : PASS
micro-style / charge cognitive phrase par phrase : OPEN
placement final du control plane : OPEN
~~~

Recommandation : une dernière passe de simplification phrase par phrase peut fermer le MUST sans modifier le fond.
