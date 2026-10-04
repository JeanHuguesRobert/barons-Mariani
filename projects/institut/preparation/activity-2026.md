---
title: "Institut — registre d’activité 2026"
subtitle: "Première reconstruction structurée des programmes de capacité et outputs publics"
description: "Registre préparatoire des activités 2026 dans le périmètre C.O.R.S.I.C.A. / Institut Mariani, fondé d’abord sur les traces publiques des dépôts du Corpus."
author: "Jean Hugues Noël Robert, baron Mariani"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-04"
last_modified_at: "2026-10-04"
version: "0.1"
status: "working-paper — preparatory"
license: "CC BY-SA 4.0"
language: "fr"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/projects/institut/preparation/activity-2026.md"
document_role: "operational"
document_kind: "activity-register"
document_function: "annual activity reconstruction"
visibility: "public"
lifecycle_state: "working"
update_policy: "UP-DEFAULT-REVIEWED"
related_documents:
  - "projects/institut/preparation/janus-master.md"
  - "projects/institut/preparation/resources-2025-2026.md"
  - "projects/institut/preparation/ag-age-2025-2026.md"
  - "research/institut_mariani.md"
  - "https://github.com/JeanHuguesRobert/cogentia/blob/main/research/living_book_factory.md"
provenance:
  origin_type: "repository-reconstruction"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-04"
  derived_from:
    - "public GitHub histories of JeanHuguesRobert/barons-Mariani"
    - "public GitHub histories of JeanHuguesRobert/cogentia"
    - "public GitHub histories of JeanHuguesRobert/inseme"
    - "research/institut_mariani.md"
review:
  status: "unreviewed"
  reviewed_by: []
---

# Institut — registre d’activité 2026

## 0. Portée

Ce document est une première reconstruction du **1er janvier au 4 octobre 2026**.

Le volume de traces GitHub rend une transcription commit par commit peu utile pour la lecture. Cette v0.1 regroupe donc l’activité en **programmes de capacité**, tout en conservant des commits témoins.

Le regroupement est RECONSTRUCTED ; les commits et fichiers cités sont des traces ESTABLISHED.

## 1. Vue d’ensemble

| Programme | Nature de la capacité | Exemples de traces publiques | État |
|---|---|---|---|
| COP / accounting / mandats | orchestration, comptabilité de ressources, autorité bornée | inseme/packages/cop-core ; d91a50e3, 7cb00cd3, 46a761c5 | ESTABLISHED |
| FractaLog / lifecycle des traces | journalisation et continuité d’actes gouvernés | 7647ba65, 8cf8b6fe, bfa3931a, ee0dc059 | ESTABLISHED |
| Cognitive Packets / continuation | travail distribué reprenable, handoffs et reprise externe | cogentia + inseme ; aa81447b, 4d6c6035, 23f5df98 | ESTABLISHED |
| Agent JHN / Interaction Cases | surfaces gouvernées d’interaction et projections SQL | 8114cce7, 5f0454c9, 93897305, d940211e | ESTABLISHED |
| Compute / Magistral | sélection de handlers, budgets, receipts, préemption | 5ba35fed, e16fe57a, c23cb56c, 43bbea57, e7e228f8 | ESTABLISHED |
| FractaCognition | métacognition, localité, Talleyrand, Pattern Mining | research/fractacognition_principles.md ; 15afcae9, 3bb7f98d, 0a80f180 | ESTABLISHED |
| Living Books | publication continue et confédération de corpus | research/livre_vivant.md et projets associés | ESTABLISHED |
| Living Book Press | éditions / exemplaires physiques singuliers | cogentia eca9e3f0 | ESTABLISHED |
| Living Book Factory | génération, validation et apprentissage transversal | 43907537, d0227e23, cogentia#229 | ESTABLISHED / PREPARATORY |
| Suicide Corse | enquête, guide, magazine et projections éditoriales | projects/suicide-corse | ESTABLISHED |
| Rise & Fall | histoire familiale, généalogie, chronologie et sources | projects/rise-and-fall | ESTABLISHED |
| DIASPORA | annuaire contributif de capacités / Livre Vivant | projects/diaspora | ESTABLISHED |
| Capable | doctrine d’effectivité et campagne / Livre Vivant | projects/capable | ESTABLISHED |
| PrivAI | AI Safety politique / souveraineté humaine / Livre Vivant | projects/privai | ESTABLISHED |
| Commons | histoire et futurs des biens communs / Livre Vivant | projects/commons | ESTABLISHED |
| Autonomia / #1755 | autonomie de capacité, histoire constitutionnelle, contribution publique | research/autonomia | ESTABLISHED |
| Campagne du Réel / sénatoriales | campagne, contentieux, preuves, chronologies | research/senatoriales-2026 | ESTABLISHED |

## 2. Exemple de matérialisation récente

Le 4 octobre 2026 seul illustre la densité du système : création et approfondissement de Commons et PrivAI, poursuite de Capable, consolidation de Suicide Corse n°4, maintenance du dossier sénatoriales, création de Living Book Factory, généralisation de la grammaire epistemic / institutional / effect, puis préparation du Livre Vivant Institut.

Le rapport annuel ne doit pas compter ces commits comme unités de travail, mais montrer les capacités et outputs auxquels ils contribuent.

## 3. Typologie d’outputs 2026

~~~text
RESEARCH
SOFTWARE
INFRASTRUCTURE
PUBLICATION
GOVERNANCE
CIVIC / INSTITUTIONAL
META
~~~

Une même trace peut contribuer à plusieurs catégories ; le rapport final devra éviter le double comptage des ressources.

## 4. Activité ≠ valeur monétaire

~~~text
activité attestée
→ ESTABLISHED

volume humain
→ CONFIRMED | RECONSTRUCTED | UNKNOWN

compute consommé
→ unités natives si disponibles

valorisation
→ projection séparée, méthodée
~~~

## 5. Lien institutionnel

Le frontmatter et les documents publics rattachent de nombreux travaux à l’Institut Mariani / C.O.R.S.I.C.A., mais ce rattachement documentaire ne doit pas être utilisé pour inventer un mandat formel, une dépense associative, un financement, une décision d’Assemblée ou une propriété juridique non documentée.

~~~text
activité documentée dans le périmètre Institut
≠ acte juridique de C.O.R.S.I.C.A.
≠ dépense de C.O.R.S.I.C.A.
~~~

## 6. Prochain enrichissement quantitatif

Pour chaque programme majeur, reconstruire ensuite période active, outputs, travail humain, compute, cash, communs réemployés et effet observé.

## 7. Couverture et limites

Cette v0.1 est volontairement un **registre de départ**, pas un inventaire complet.

Les prochains passages devront explorer les historiques GitHub au-delà des 100 traces les plus récentes par dépôt, identifier les autres dépôts publics pertinents, rapprocher les issues et journaux de projet, puis intégrer les traces privées nécessaires au rapport annuel sans les publier brutes.

La densité 2026 rend plausible une automatisation substantielle de ce travail : c’est précisément un Reality Test de l’investissement d’outillage de l’Institut.