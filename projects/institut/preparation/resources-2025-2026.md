---
title: "Institut — registre préparatoire des ressources 2025–2026"
subtitle: "Argent, bénévolat, compute, infrastructures, communs et outputs"
description: "Cadre préparatoire pour reconstruire les ressources effectivement mobilisées par C.O.R.S.I.C.A. / Institut Mariani sans confondre unités natives et valorisations monétaires."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-04"
version: "0.1"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/resources-2025-2026.md"
document_role: "operational"
document_kind: "resource-register"
document_function: "resource and in-kind contribution reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/janus-master.md"
  - "projects/institut/preparation/ag-age-2025-2026.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/living_book_factory.md"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-04"
  derived_from:
    - "projects/institut/preparation/janus-master.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Institut — registre préparatoire des ressources 2025–2026

## 1. Objet

Les comptes bancaires ne suffisent pas à décrire l'activité réelle d'une association qui produit beaucoup par bénévolat, logiciels ouverts, compute, infrastructure et réemploi de communs.

Le registre doit d'abord conserver les ressources dans leur unité native.

~~~text
quantité native
→ primaire

valorisation monétaire
→ projection secondaire, sourcée, datée et méthodologique
~~~

## 2. Dimensions minimales

| Ressource | Unité native | 2025 | 2026 | Trace / méthode | Valorisation possible | Statut |
|---|---:|---:|---:|---|---|---|
| Flux monétaires | EUR | à reconstruire | à reconstruire | comptes / pièces | montant transactionnel | UNKNOWN |
| Travail bénévole | heure | à reconstruire | à reconstruire | Git, mails, calendrier, outputs, journaux | forfait / coût de remplacement / autre méthode justifiée | RECONSTRUCTED |
| Compute API | tokens / appels / quota | à reconstruire | à reconstruire | fournisseurs / logs / COP | valeur faciale / marché comparable / remplacement | UNKNOWN |
| Compute GPU | GPU-hour ou workload équivalent | à reconstruire | à reconstruire | fournisseur / allocation | idem | UNKNOWN |
| Cloud / hébergement | mois, stockage, bande passante, service | à reconstruire | à reconstruire | factures / contrats / logs | prix transactionnel / remplacement | UNKNOWN |
| Matériel | unité / durée de mise à disposition | à reconstruire | à reconstruire | inventaire | remplacement / amortissement analytique | UNKNOWN |
| Logiciels et communs | réemploi / composant / licence | à inventorier | à inventorier | dépôts / licences | généralement non réduit à une valeur unique | RECONSTRUCTED |
| Temps d'attention / administration | heure | à reconstruire | à reconstruire | traces et estimation | valorisation séparée si utile | UNKNOWN |

## 3. Travail bénévole

Le temps bénévole doit rester une ressource visible, même lorsqu'aucun euro ne circule.

~~~text
HOURS_CONFIRMED
→ trace temporelle suffisamment directe

HOURS_RECONSTRUCTED
→ estimation argumentée à partir d'actes et outputs

HOURS_UNKNOWN
→ activité certaine mais durée non estimable honnêtement
~~~

Ne pas fabriquer de précision horaire rétrospective.

Pour chaque bloc significatif, conserver au minimum la quantité, l'unité, le statut de reconstruction, le projet ou la fonction, les traces disponibles et la méthode de valorisation éventuelle.

La valorisation ne devient jamais du cash reçu.

## 4. Compute

Séparer systématiquement :

~~~text
native quantity
≠ provider face value
≠ observed transaction price
≠ comparable market value
≠ attainable replacement cost
≠ internal use value
≠ cash received
~~~

Exemple de formulation correcte :

> Allocation de compute affichée par le fournisseur à une valeur faciale de X selon son tarif de référence ; valeur de remplacement analytique Y selon la méthode Z ; cash reçu : 0.

Ne pas écrire « X euros reçus » pour un crédit ou une allocation non monétaire.

## 5. Effet de levier

Une projection utile pour l'AG et les financeurs futurs pourra distinguer :

~~~text
cash réellement mobilisé
+ bénévolat
+ compute
+ hébergement / infrastructure
+ communs réemployés
= capacité totale mobilisée
~~~

Une addition monétaire de dimensions hétérogènes n'est admissible que comme valorisation analytique explicitement méthodée, jamais comme solde comptable.

## 6. Lien avec « Sans Argent »

Le registre doit permettre de tester :

> **Faire avec le moins d'argent dédié raisonnablement nécessaire, sans sacrifier légalité, effectivité, sécurité, traçabilité ni soutenabilité.**

Cela exige une comptabilité plus riche, pas une absence de comptabilité.

## 7. Reconstruction 2025–2026

Ordre de collecte proposé :

1. GitHub : commits, issues, releases, documents et dates ;
2. Corpus : publications et états de projet ;
3. Gmail / calendrier lorsque la préparation de l'AG exigera ces données et que l'accès sera explicitement mobilisé ;
4. factures / relevés / fournisseurs ;
5. logs de compute et cloud ;
6. déclarations humaines pour les activités non tracées ;
7. rapprochement puis estimation bornée.

Les données privées nécessaires à la comptabilité ne doivent pas être copiées dans le Corpus public. Le présent document ne contient que la méthode et les agrégats publiables.

## 8. Affectation financière envisagée au fonds Barons Mariani — 22 novembre 2026

Le Président indique qu'une assemblée antérieure, il y a approximativement trois ans, a réservé des fonds au projet de fonds de dotation Barons Mariani. **Antécédent déclaré, montant, PV et ventilation comptable à retrouver**. La décision ancienne n'est pas substituée à un justificatif bancaire ou au pouvoir de l'organe compétent pour la dépense effective.

**Hypothèse à soumettre à la prochaine AG** : C.O.R.S.I.C.A., cofondatrice, apporte **15 000 € en numéraire** à la dotation initiale du fonds, qualifiée **consomptible** par les statuts du fonds ; les frais du transfert de Minesteggio peuvent être financés sur cette trésorerie si leur objet et leur traitement sont correctement établis. Ne pas compter les mêmes euros une seconde fois comme réserve non consommée.

**Plan de cash indicatif, non budget adopté** : dotation 15 000 € ; prélèvements immobiliers estimés à environ 6 571 € si exonération DMTG et renonciation du notaire à ses émoluments ; trésorerie restante théorique **8 429 €** avant autres frais, ou **5 929 €** avec provision de 2 500 € de géomètre. Si émoluments facturés, l'enveloppe doit être réévaluée. Valeur indicative de Minesteggio : 1 M€ en pleine propriété, avec réserve d'usufruit et donation de droits immobiliers estimés fiscalement à 920 k€ après les 61 ans du fondateur ; **aucune de ces valeurs patrimoniales n'est de la trésorerie**.

Voir [dossier institutionnel et notarial](barons-mariani-fonds-dotation-notaire-2026.md). Aucune écriture comptable ou décision de dépense n'est actée par cette notice.
