---
title: "Sénatoriales 2026 — cahier des charges de la requête au Conseil constitutionnel"
subtitle: "Spécification contentieuse, probatoire, historique et Archia"
author: "Jean Hugues Noël Robert, baron Mariani"
date: "2026-09-26"
version: "0.1"
status: "working specification"
language: "fr"
license: "CC BY-SA 4.0"
visibility: "public"
document_role: "method"
document_kind: "contentious-filing-specification"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
source_documents:
  - "README.md"
  - "investigation/chronology.md"
  - "investigation/knowledge-matrix.md"
  - "investigation/defect-ledger.md"
  - "investigation/probe-map.md"
  - "../autonomia/amendement_effectivite_article_72-5.md"
  - "../contribution_commission_lois_autonomie_capacite.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Cahier des charges de la requête au Conseil constitutionnel

## 1. Finalité

La requête doit remplir simultanément deux fonctions sans les confondre :

1. **fonction contentieuse** — constituer une contestation réelle de l’élection sénatoriale ;
2. **fonction historique** — déposer auprès d’une institution constitutionnelle un état daté, vérifiable et aussi complet que raisonnablement possible des actes pertinents du requérant dans la candidature sénatoriale et le débat sur l’autonomie de la Corse.

Principe :

> **la fonction historique ne doit jamais détruire la fonction contentieuse.**

## 2. Objectif de traçabilité

La requête applique la doctrine Archia :

```text
acteur
→ information disponible
→ pouvoir / compétence / obligation éventuelle
→ acte ou abstention
→ trace
→ effet
→ capacité conservée ou perdue
→ correction encore possible ou non
```

Pour chaque fait significatif, distinguer :

- `established` — trace suffisante ;
- `reported` — témoignage non indépendamment établi ;
- `inferred` — conclusion issue de plusieurs traces ;
- `open` — question non résolue.

## 3. Invariant temporel

Trois périodes ne doivent jamais être confondues :

1. **avant 18 h le 11 septembre** — faits et formalités existant avant la clôture ;
2. **après 18 h mais avant le jugement du 14 septembre** — éléments pouvant vérifier un fait antérieur sans constituer une régularisation tardive ;
3. **après le jugement** — traces permettant de reconstruire traitement, transmission, instruction et archivage.

## 4. Déclencheur post-scrutin

La requête ne doit être finalisée comme contestation de l’élection qu’après la **proclamation** du résultat.

Le dossier est préparé pour que la matérialisation puisse intervenir au plus tôt après cette proclamation, avec une cible symbolique de **12 h 00 le 27 septembre 2026** si la proclamation est déjà acquise.

Toujours conserver séparément :

```text
T1 = proclamation
T2 = document final matérialisé
T3 = acte de saisine
T4 = accusé / réception institutionnelle
T5 = publication publique
```

Aucune heure ne doit être reconstruite ou fusionnée avec une autre.

## 5. Premier écran

Les premières pages doivent permettre de comprendre immédiatement :

- identité et qualité du requérant ;
- élection contestée ;
- élu ou élus dont l’élection est contestée ;
- déclaration de candidature déposée ;
- refus d’enregistrement ;
- moyens principaux ;
- incidence alléguée sur l’élection ;
- conclusions.

Le contexte historique vient ensuite.

## 6. Architecture du corps principal

### I — Recevabilité et qualité du requérant

Identifier la circonscription, la proclamation, le délai et la qualité pour agir.

### II — Résumé exécutif

Deux à quatre pages maximum.

### III — Chronologie probatoire

Dates, heures, acteurs, actes, statuts de preuve et renvoi à chaque pièce.

### IV — Formalités de candidature

Distinguer :

- exigence légale ou réglementaire ;
- notice / formulaire ;
- support matériel ;
- signature ;
- mention manuscrite ;
- identité ;
- consentement ;
- obstacle fonctionnel éventuel.

### V — Traitement administratif

Pour chaque étape :

```text
information disponible
→ ce que l’administration devait faire
→ ce qu’elle pouvait faire
→ ce qu’elle a fait
→ capacité restant ouverte
```

Ne jamais transformer un simple `pouvait` en `devait` sans fondement identifié.

### VI — Traitement juridictionnel

Documenter notamment :

- observations écrites et orales ;
- note manuscrite du 14 septembre ;
- note en délibéré ;
- prise de connaissance par la formation de jugement ;
- signalement de l’existence de la vidéo ;
- questions ouvertes sur sa transmission et son examen.

### VII — Incidence sur le scrutin

Montrer pourquoi les griefs ne sont pas manifestement dépourvus d’incidence sans prédire le nombre de voix qu’aurait obtenu une candidature empêchée.

### VIII — Temporalité et pertes irréversibles

Distinguer :

- participation au scrutin ;
- capacité éventuelle liée au mandat ;
- calendrier parlementaire ;
- ce qu’une décision tardive peut encore réparer ;
- ce qu’elle ne peut plus restaurer.

### IX — Conclusions

Courtes, juridiquement identifiables et indépendantes de l’objectif historique.

## 7. Gabarit obligatoire de chaque grief

```text
FAIT
→ PREUVE
→ RÈGLE
→ ÉCART
→ INCIDENCE
→ INCERTITUDE RÉSIDUELLE
→ MESURE D'INSTRUCTION ÉVENTUELLE
```

## 8. Inconnues structurantes à ne pas masquer

À suivre notamment :

- heure d’acceptation destinataire du message de 17:57:55 ;
- traitement de ce message ;
- transmission éventuelle au TA ;
- consultation éventuelle de la vidéo ;
- correspondance exacte de « Réception d’une lettre » dans Sagace ;
- inventaire final des pièces ;
- traces d’audience ;
- chronologie précise des transmissions.

Un `UNKNOWN` documenté vaut mieux qu’une certitude fabriquée.

## 9. Consentement de la remplaçante

Séparer quatre questions :

```text
identité
≠ consentement
≠ conformité formelle
≠ obstacle fonctionnel / handicap
```

L’existence d’éléments forts sur les deux premières ne doit pas être présentée comme réglant automatiquement les deux dernières.

## 10. Partie historique autonome

Prévoir une annexe :

> **État documenté des interventions du requérant dans le processus relatif à l’autonomie de la Corse au jour de la saisine**

Cette annexe doit établir notamment l’antériorité :

- de la candidature ;
- de l’Autonomie de Capacité ;
- de la contribution C.O.R.S.I.C.A. ;
- du lien entre candidature et intervention constitutionnelle ;
- de l’amendement d’effectivité.

Le contentieux sénatorial est un cas d’étude ultérieur, pas l’origine de la doctrine.

## 11. Interventions parlementaires post-scrutin

Les courriels envoyés après le scrutin et avant la requête doivent pouvoir figurer comme **actes historiques datés**, pas comme preuve de faits antérieurs à la clôture des candidatures.

Pour chaque envoi :

```text
destinataire
→ qualité
→ heure
→ objet
→ texte / pièce / lien
→ Message-ID
→ résultat de livraison
→ réponse éventuelle
```

## 12. Classification des annexes

### A — pièces contentieuses essentielles

Nécessaires aux moyens.

### B — pièces de contexte probatoire

Renforcent chronologie et compréhension.

### C — pièces historiques

Documentent les interventions sur l’autonomie sans constituer un moyen électoral autonome.

## 13. Version institutionnelle / version publique

Produire deux artefacts synchronisés :

**Institutionnel** — données nécessaires au contentieux.

**Public** — mêmes structure et version, avec occultation des données personnelles non nécessaires.

Conserver autant que possible :

- version ;
- date ;
- liste de pièces ;
- commit ;
- empreintes SHA-256 ;
- table de correspondance entre pièces publiques et institutionnelles.

## 14. Manifeste Archia du dépôt

Créer après matérialisation un manifeste contenant :

- proclamation ;
- génération du PDF ;
- signature ;
- SHA-256 ;
- canal de saisine ;
- heure de remise / transmission ;
- accusé / récépissé ;
- identifiant de dossier éventuel ;
- commit Git ;
- liens publics ;
- liste des pièces et empreintes.

## 15. Test de complétude historique

Avant dépôt, vérifier qu’un lecteur futur peut :

- reconstruire l’antériorité de la candidature ;
- établir que l’Autonomie de Capacité précède le contentieux ;
- retrouver la contribution de mai ;
- reconstruire les 10, 11 et 14 septembre ;
- distinguer fait, témoignage, inférence et inconnu ;
- retrouver les principales sources ;
- connaître l’état exact de l’amendement au jour du dépôt ;
- connaître les inconnues restantes à cette date.

## 16. Test de qualité contentieuse

Avant dépôt, vérifier que :

- conclusions et élection contestée sont identifiées ;
- les griefs sont intelligibles sans lire l’annexe historique ;
- chaque grief renvoie à une preuve ou à une demande d’instruction précise ;
- l’incidence possible est expliquée ;
- les éléments postérieurs ne sont pas utilisés comme régularisation rétroactive ;
- le dépôt intervient dans le délai applicable.

## 17. Test final Archia

Pour chaque épisode critique :

> **Qui savait quoi ? Qui pouvait quoi ? Qui devait quoi ? Qui a fait quoi ? Quelle trace l’établit ? Quel effet en a résulté ? Quelle capacité restait encore ouverte ?**

La requête doit être lisible à deux époques :

> **aujourd’hui par un juge électoral ; demain par un citoyen ou un historien.**
