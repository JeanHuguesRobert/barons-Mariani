---
title: "2026-6589 SEN — audit FBF du lot de communication des pièces"
date: "2026-11-10"
status: "audit documentaire — lot non prêt"
document_role: operational
document_kind: evidence-delivery-audit
visibility: public
lifecycle_state: working
filing_ready: false
language: fr
---
# Reprise FBF du dossier de pièces — 10 novembre 2026

## Contrat d'autorité et périmètre

Le checkpoint du 1er novembre dans [#127](https://github.com/JeanHuguesRobert/barons-Mariani/issues/127) fait autorité sur les scénarios plus anciens. Le prochain acte proposé est une **communication de pièces préexistantes déjà citées dans la requête initiale enregistrée**, et de notices bornées à la provenance, à l'intégrité et au rattachement à G1–G5 déjà formulés. **Pas** de nouveau mémoire argumentatif, de nouveau grief, ni d'insertion furtive des QPC L.299/L.303. L'auteur réalise lui-même tout envoi final après examen. Ce rapport est public et ne contient aucun original personnel ni binaire.

Sources contrôlées : [requête historique](../requete-conseil-constitutionnel.md), [bordereau de production](bordereau-production-propose.csv), [matrice de réconciliation du 22 octobre](matrice-reconciliation-pieces-p01-p46-2026-10-22.md), [notices de provenance](notes-provenance-v0.1.md), [vidéo P-13](parcours-video-p13-v0.1.md), [assembleur](../../../scripts/sen-2026-6589-build.py), [test FBF](../../../scripts/check-sen-2026-6589-build.py), et checkpoints récents #131–#134.

## Constat matériel sur le CSV actuel

Le CSV a été lu en respectant les champs entre guillemets et les virgules internes. **54 enregistrements, 17 colonnes, 0 erreur de structure** :
- `JOIN` : **43** ; `RESERVE` : **6** ; `CITE` : **5**.
- `delivery_artifact_ready=true` : **1** (P-13.mp4) ; `false` : **53**.
- `delivery_status=NOT_SENT` : **54**. `historical_delivery=UNKNOWN` : **54**.
- **44/54** champs `delivery_channel` évoquent encore l'architecture antérieure « QPC / PDF consolidé » ; ce sont des données historiquement tracées, **pas le mandat actif**.
- Les empreintes de sources notées `PASS` dans le bordereau attestent seulement les vérifications documentées à leur date : elles ne valent pas preuve que le *dérivé final expurgé* existe ou a la même empreinte.
- L'unique `ready=true` porte sur un **binaire source**, pas sur le lot complet ; la copie finale de P-13 destinée à l'envoi reste à retrouver et à re-hasher.

## Contradiction FBF à corriger avant toute remise

Le [tableau de réconciliation du 22 octobre](matrice-reconciliation-pieces-p01-p46-2026-10-22.md) et plusieurs `delivery_channel` du CSV présupposent encore le montage **mémoire principal + PDF QPC L.299 + PDF QPC L.303 + annexes TA + vidéo P-13**. Le checkpoint du 1er novembre de #127 annule **l'applicabilité à la prochaine communication**, mais non la valeur historique de ces variantes. Ne pas écraser ces archives : séparer une **sélection de livraison actuelle** de la matrice historique, et bloquer tout générateur qui relirait les anciennes instructions comme actives.

La stratégie de #133 a déjà été corrigée : `scripts/sen-2026-6589-build.py` utilise par défaut `exhibits` et réserve le mode argumentatif à `--legacy-argumentative-preview`. Son test source `scripts/check-sen-2026-6589-build.py` vérifie ces invariants ; **son exécution réelle n'a pas été reproduite durant le présent audit**.

## Ordre de traitement proposé sans sollicitations inutiles

1. **#131 — sélection source et minimisation.** Repartir du bordereau des **pièces effectivement citées dans la requête initiale** (et non des seuls 43 `JOIN` hérités). Pour chaque entrée : `citation_initiale` (référence/page), fichier natif localisé, taille, SHA natif réellement recalculé, type d'extrait ou reproduction nécessaire, statut expurgation, `delivery_ready` de l'**artefact** final, destination et statut. Conserver les références CITE/RESERVE motivées et les possibles doublons dans les PDF TA.
2. **#132 — P-13.** Fichier natif privé `VID_20260911_174455.mp4` : taille historique 79 663 474 octets, SHA-256 historique `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8`. Identifier la **copie actuelle exacte** et recalculer taille/empreinte avant statut `READY`. L'expédition du lien P-12 le 11/09 à 17:57:55 ne prouve ni réception avant 18 h, ni transmission au TA.
3. **#133 — assemblage borné.** Prendre la sélection actuelle, produire le texte d'accompagnement, le bordereau des **fichiers réellement présents**, et un manifeste de production. Ne pas construire une « pièce » à partir d'un simple pointeur Drive ou d'une transcription. `filing_ready=false` par défaut ; sortie sans QPC introduites implicitement.
4. **#134 — contrôle de sortie.** Recalculer SHA-256 des **octets finaux**, vérifier expurgation et correspondance avec liste et canaux, statut des originaux, contrôle juridique des notices, absence de secrets, capacités de dépôt, instructions manuelles, en distinguant `PREPARED / STAGED / SENT / RECEIVED / EXAMINED`.
5. **#127 — arbitrage final.** Ne solliciter l'auteur que sur une sélection substantielle non résoluble, ou une fois le lot entièrement prêt pour son contrôle ; tout envoi reste exclusivement manuel et volontaire.

## Tableau PASS / UNKNOWN / BLOCKED

| Gate | État vérifié dans cette passe |
|---|---|
| Mandat de livraison du 01/11 identifié | PASS |
| CSV structurellement lisible (54 × 17) | PASS |
| Sélection actuelle depuis les pièces citées | UNKNOWN |
| Présence de tous les originaux sélectionnés | UNKNOWN |
| Copies minimisées finales disponibles | **NOT READY** (53/54 `ready=false` dans CSV historique ; ne pas assimiler sélection courante et CSV ancien) |
| SHA-256 des fichiers de sortie finales | UNKNOWN |
| Binaire P-13 récupérable et re-hashé dans cet environnement | UNKNOWN |
| Rendu de l'assembleur et test de non-insertion QPC exécutés ici | NOT TESTED |
| Cohérence exacte courriel / pièces / TransfertPro et instructions humaines | UNKNOWN |
| Livraison au greffe et accusé | **NON ATTESTÉS** |

## Informations conservées

- Les deux copies volumineuses TA 2601714/2601715 sont décrites comme disponibles sur Drive privé dans des checkpoints antérieurs ; il faut vérifier leur disponibilité et leurs empreintes **aujourd'hui** avant de les compter comme artefacts prêts.
- Les 46 EML de P-46, leur archive locale et les décisions de minimisation ne sont pas présumés repris ou revus depuis le 23 octobre.
- La requête initiale enregistrée, les originaux sensibles et la version historique des QPC ne sont pas modifiés.
- Aucune transmission, aucun dépôt, aucune attestation d'envoi ou de réception n'a été créé.
