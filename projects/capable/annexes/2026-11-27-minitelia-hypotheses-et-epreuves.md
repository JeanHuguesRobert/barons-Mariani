---
title: "Minitelia — hypothèses économiques et épreuves du Réel"
date: '2026-11-27'
author: "Orientations de Jean Hugues Noël Robert ; consolidation assistée, candidate"
language: fr
license: CC BY-SA 4.0
status: working-paper
document_role: derived
document_kind: research-annex
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
canonical_url: https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/capable/annexes/2026-11-27-minitelia-hypotheses-et-epreuves.md
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: conversation
  origin_date: '2026-11-27'
  derived_from:
    - projects/capable/doctrine/nouveau-contrat-social.md
---

# Minitelia — hypothèses économiques et épreuves du Réel

Annexe de travail du [Nouveau Contrat Social](../doctrine/nouveau-contrat-social.md). Les chiffres suivants sont des hypothèses illustratives de la discussion, non des mesures du parc national ni un devis. L'expérience sur KasmVNC est qualitative à ce stade.

## 1. Enveloppes et volumes

Pour une population de référence de 69,1 millions, le budget annuel à couverture intégrale est 12 × population × dotation mensuelle. À 1, 3 et 5 €/mois par personne : 829,2 M€, 2,488 Md€ et 4,146 Md€/an. Pour 400 000 personnes (scénario Corsica2038) : 4,8, 14,4 et 24 M€/an. Une enveloppe de 1 à 5 Md€/an constitue une hypothèse d'étude, non une promesse de service.

Bureau distant : 20 millions d'utilisateurs actifs × 10 heures/mois = 200 millions d'heures/mois ; pour un mois moyen de 730 heures, environ 274 000 sessions simultanées en moyenne et 822 000 en pointe sous hypothèse d'un facteur 3. À 2 Go et 0,5 vCPU par session : environ 1,64 Po de RAM et 411 000 vCPU en pointe. À 0,03 €/heure : 72 M€/an de calcul, hors coûts fixes et autres postes.

Inférence : 20 millions d'utilisateurs × 1 million de tokens/mois × 12 = 240 000 milliards de tokens/an. À 0,10 / 0,50 / 1 / 2 / 5 € par million : 24 / 120 / 240 / 480 / 1 200 M€/an. Distinguer entrée, sortie, contexte, raisonnement, cache et qualité de service.

## 2. Trois leviers d'économie

- Matériel : rendement calcul/énergie/euro ; logiciel : travail utile par unité de calcul ; réutilisation : travail effectivement évité. Éviter le double comptage.
- Mutualisation temporelle : ressources actives, suspension, stockage et reprise ; distinguer l'interactif et le différé, les pics corrélés et les coûts réseau.
- Mutualisation cognitive : pour un grand nombre de tâches, une fraction commune de 90 % conduirait idéalement à un coût relatif proche de 10 % ; recherche, validation, adaptation et confidentialité réduisent le gain. Cette fraction est illustrative.
- Scénario prospectif : 30 %/an de gain matériel et 30 %/an de gain logiciel, contre 25 %/an de croissance d'usage, donnent (1,3 × 1,3 / 1,25)^12 ≈ 37,3. Ces taux sont hypothétiques et ne décrivent pas l'évolution de tous les coûts.

Inclure stockage, réseaux, exploitation, renouvellement, formation, accompagnement, sûreté, résilience et garanties de sortie dans le coût complet. BYOAI ne réduit le budget mutualisé que dans la mesure où il évite réellement des dépenses.

## 3. Épreuves proposées

| Épreuve | Observables et critères à fixer avant test |
|---|---|
| Bureau distant | Coût complet par heure utile, latence, RAM et CPU actifs/suspendus, reprise, qualité selon terminaux et réseau |
| Réutilisation cognitive | Travail évité, erreurs d'adaptation, provenance et coût de vérification |
| Pluralité | Accès aux besoins minoritaires, langues, exploration indépendante, refus et changement de modèle |
| Sûreté démocratique | Délai de détection, recours, preuves minimales, imputabilité, révocation ciblée, protection des métadonnées |
| Exil et asile | Restauration indépendante, coût, délai, pertes fonctionnelles, ressources et droits d'accueil |
| Références Communes | Désaccords conservés, sources et procédures vérifiables, corrections, observations externes |
| Nature | Énergie, eau, matériel, renouvellement, impacts locaux et régénération ; distinguer faits et arbitrages |

Comparer les scénarios de maintien, migration et indisponibilité d'un opérateur. Commencer avec des données synthétiques et des mandats bornés. Le taux d'adhésion ne suffit pas à établir la sûreté démocratique.

## 4. Sources et interlocuteurs

Le [Collège des Interlocuteurs](2026-11-27-college-interlocuteurs-nouveau-contrat-social.md) constitue le programme de lecture. Vérifier les données historiques et nationales auprès des sources primaires (Insee, Baromètre du numérique, DREES ; plan Informatique pour tous), les capacités et tarifs auprès des opérateurs, et les résultats techniques au moyen d'expériences reproductibles. Le [dépôt KasmVNC](https://github.com/kasmtech/KasmVNC) est une piste d'implémentation, non une dépendance normative. Les travaux [FractaVolta](https://github.com/JeanHuguesRobert/FractaVolta/blob/main/research/value_shaped_solar_and_containerized_compute.md) et [Migration-Tested](https://github.com/acorsica/privai/blob/main/conformance/migration_tested_v0.1.md) donnent des terrains techniques distincts.

Aucune mesure nationale, expérimentation de masse ou garantie d'asile n'est établie par cette annexe. Les références primaires et les résultats doivent l'enrichir progressivement.
