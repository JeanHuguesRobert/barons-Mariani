---
title: "Sénatoriales Haute-Corse 2026 — matrice de matérialisation des pièces"
author: "Jean Hugues Noël Robert"
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-07"
last_modified_at: "2026-10-07"
version: "0.2"
status: "active — pre-filing materialization control"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "operational"
document_kind: "filing-materialization-map"
visibility: "public"
lifecycle_state: "active"
update_policy: "UP-DEFAULT-REVIEWED"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/filing-materialization-map-2026-10-07.md"
provenance:
  origin_type: "conversation"
  origin_repository: "JeanHuguesRobert/barons-Mariani"
  origin_ref: "unknown"
  origin_date: "2026-10-07"
  derived_from:
    - "research/senatoriales-2026/filing-package-2026-10-07.yml"
    - "research/senatoriales-2026/bordereau-pieces-requete-conseil-constitutionnel.md"
review:
  status: "reviewed — synchronized with materialization audit 2026-10-07"
  reviewed_by: []
---

# Matrice de matérialisation des pièces

## Objet

Cette matrice relie le **bordereau juridique** au **fichier PDF local effectivement attendu par l'assembleur Ubikia**.

Documents de contrôle :

- [requête canonique](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/requete-conseil-constitutionnel.md) ;
- [bordereau canonique](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/bordereau-pieces-requete-conseil-constitutionnel.md) ;
- [contrat d'assemblage](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/filing-package-2026-10-07.yml) ;
- [manifeste du paquet](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/filing-package-manifest-2026-10-07.md).

Les PDF de travail sont placés localement dans :

`.filing-materials/senatoriales-2026/`

Ce répertoire est ignoré par Git. Un fichier n'est considéré comme matérialisé que lorsqu'il existe réellement à l'emplacement prévu et a été contrôlé.

## État de la passe du 7 octobre 2026

Une vérification directe de Gmail a confirmé l'existence des **46 messages constituant P-46**, ainsi que des messages spécifiques **P-43.a**, **P-43.b** et **P-45.a à P-45.d**. Les pièces jointes signalées par Gmail ont également été inventoriées.

Cette vérification signifie : **source Gmail retrouvée et lisible par l'outil**.

Elle ne signifie pas encore : **PDF final produit, occulté, paginé et validé**.

## Légende

- **AUTO-GMAIL** : source native Gmail vérifiée ; représentation PDF générable automatiquement.
- **AUTO-ATTACH** : pièce jointe récupérable identifiée.
- **AUTO-CORPUS** : source structurée présente dans le Corpus.
- **MANUEL/PRIVÉ** : fichier, scan, photo, vidéo ou original extérieur à retrouver ou fournir.
- **COMPOSITE** : plusieurs sources doivent être assemblées avec identification/provenance.
- **SPÉCIAL** : type de source non directement incorporable au contrat PDF.

## Matrice

| Pièce | Cible locale | Source / ancrage principal | Mode | État après vérification |
|---|---|---|---|---|
| P-04 | `.filing-materials/senatoriales-2026/P-04.pdf` | [index P-04](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/sources/p04-premier-envoi-dsn-retransmission-2026-09-10.md) + Gmail P-46.01/P-46.02 et DSN associés | COMPOSITE / AUTO-GMAIL | sources principales retrouvées ; PDF à produire |
| P-05 | `.filing-materials/senatoriales-2026/P-05.pdf` | Gmail `1a08c0953c1f9ff2` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-06 | `.filing-materials/senatoriales-2026/P-06.pdf` | Gmail `1a08c7eb62cc13ec` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-07 | `.filing-materials/senatoriales-2026/P-07.pdf` | Gmail `1a08f1a2d612bb08` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-08 | `.filing-materials/senatoriales-2026/P-08.pdf` | photos / chronologie du trajet du 11 septembre | MANUEL/PRIVÉ / COMPOSITE | source photographique à localiser et sélectionner |
| P-09 | `.filing-materials/senatoriales-2026/P-09.pdf` | PREF-13 inclus dans le bundle primaire P-14 | AUTO-ATTACH / COMPOSITE | source primaire localisée ; sous-document à extraire et contrôler contre la transcription |
| P-10 | `.filing-materials/senatoriales-2026/P-10.pdf` | Gmail `1a0906430ac3adee` + 2 PDF joints | COMPOSITE / AUTO-GMAIL / AUTO-ATTACH | message et deux pièces jointes vérifiés |
| P-11 | `.filing-materials/senatoriales-2026/P-11.pdf` | Gmail `1a090d1926fe460b` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-12 | `.filing-materials/senatoriales-2026/P-12.pdf` | Gmail `1a0913095d550884` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-13 | `.filing-materials/senatoriales-2026/P-13.pdf` | fichier primaire Google Drive `VID_20260911_174455.mp4` | SPÉCIAL / SOURCE PRIMAIRE VÉRIFIÉE | PDF de représentation généré dans le staging conversationnel : SHA-256 `1cccc5a65df7d07401aa5d09923287509e085b6290abb815d6417d79c13fb03a`; natif SHA-256 `aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8`; à copier dans le staging local du dépôt |ncordant avec la fiche d'intégrité ; fiche PDF de représentation encore à produire |
| P-14 | `.filing-materials/senatoriales-2026/P-14.pdf` | PDF originaux des requêtes 2601714/2601715 reçus via France Transfert | COMPOSITE / SOURCE PRIMAIRE LOCALISÉE | deux bundles primaires retrouvés dans la bibliothèque ; retenir les copies canoniques et assembler |
| P-15 | `.filing-materials/senatoriales-2026/P-15.pdf` | Gmail `1a09fd25895322fe` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-16 | `.filing-materials/senatoriales-2026/P-16.pdf` | PDF candidat + page de garde de qualification | COMPOSITE / REPRODUCTION CANDIDATE | PDF de production généré : SHA-256 `54387f8cc8a109712136ea94288c5e7ede0186cba4294e2196ec0ebd41b3a4df`; réserve sur identité binaire conservée; à copier dans le staging local du dépôt |ndidat `observations_ecrites_defense_TA_Bastia_2601714_2601715_2026-09-14.pdf` + traces TA | COMPOSITE / REPRODUCTION CANDIDATE | PDF matérialisé, 55 546 octets, SHA-256 `d9e2b1672df34526c884b6ef10af01e46ef9d4ee21c925eeb6811d3d4ddcb60a` ; le jugement établit des observations écrites et orales, mais l'identité binaire exacte avec l'exemplaire remis n'est pas indépendamment prouvée |
| P-17 | `.filing-materials/senatoriales-2026/P-17.pdf` | deux JPG primaires + transcription contrôlée | COMPOSITE / SOURCE PRIMAIRE LOCALISÉE | images primaires retrouvées ; assembler recto-verso + transcription sans confondre original et dérivé |
| P-18 | `.filing-materials/senatoriales-2026/P-18.pdf` | original CAF + dérivé minimisé | AUTO-ATTACH / SENSIBLE | PDF minimisé généré : SHA-256 `836bf9a0f350b7cb2f5a51b1fa82c5b050ab931274254003e9757d5020001fcd`; à copier dans le staging local du dépôt |nte `1789382961469-cnaf.pdf` | AUTO-ATTACH / SENSIBLE | primaire verrouillé : 94 775 octets, SHA-256 `308754ffac6100b050dea6c43830562d0d581e8c020898201e011ab73b79fbb2` ; produire version minimisée/occultée |
| P-19 | `.filing-materials/senatoriales-2026/P-19.pdf` | Gmail `1a0a02d3fbcb466c` + éléments d'enregistrement | COMPOSITE / AUTO-GMAIL | message vérifié ; compléter avec preuve d'enregistrement utile |
| P-20 | `.filing-materials/senatoriales-2026/P-20.pdf` | scans P-20.a à P-20.g + couverture | COMPOSITE / SOURCES PRIMAIRES LOCALISÉES | PDF composite généré et rendu contrôlé : SHA-256 `c0062283f7049da075f26ff2d92363ed9fbbe10bdd6bf8c2c3ff1137d713b2a7`; à copier dans le staging local du dépôt |nscription contrôlée et index des scans primaires](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/sources/p20-jugement-ta-bastia-notification-transcription-2026-09-25.md) | COMPOSITE / SOURCES PRIMAIRES LOCALISÉES | P-20.a à P-20.g identifiés : avis de passage, AR/pli, contexte toponymique, lettre de notification et trois pages du jugement ; assemblage PDF restant |
| P-22 | `.filing-materials/senatoriales-2026/P-22.pdf` | Gmail `1a0d913e4ba70b29` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-26 | `.filing-materials/senatoriales-2026/P-26.pdf` | Gmail `1a0e2a9480a91dfa` + `1a0e6fe59ed9e8f1` | COMPOSITE / AUTO-GMAIL | sources vérifiées ; PDF à produire |
| P-27 | `.filing-materials/senatoriales-2026/P-27.pdf` | [résultats officiels](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/data/resultats_officiels_scrutin_2026-09-27.md) + source officielle | AUTO-CORPUS / COMPOSITE | données structurées présentes ; copie source officielle à privilégier |
| P-28 | `.filing-materials/senatoriales-2026/P-28.pdf` | Gmail `1a0f0f52e3f74c2b` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-29 | `.filing-materials/senatoriales-2026/P-29.pdf` | Gmail `1a0a8f038b082d1e` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-30 | `.filing-materials/senatoriales-2026/P-30.pdf` | Gmail `1a0aac0e1cd83b86` + 2 RTF | COMPOSITE / AUTO-GMAIL / AUTO-ATTACH | message et RTF vérifiés ; conversion lisible requise |
| P-31 | `.filing-materials/senatoriales-2026/P-31.pdf` | Gmail `1a0c4b6353e64219` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-32 | `.filing-materials/senatoriales-2026/P-32.pdf` | Gmail `1a0d90c299ec4899` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-33 | `.filing-materials/senatoriales-2026/P-33.pdf` | Gmail `1a0f799394da9a39` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-39 | `.filing-materials/senatoriales-2026/P-39.pdf` | [constat RP-SEN-08-C](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/constat-consultation-2026-10-01-rp-sen-08-c.md) + photographies primaires | COMPOSITE / AUTO-CORPUS / MANUEL-LOCAL | constat disponible ; images primaires à incorporer/contrôler |
| P-40 | `.filing-materials/senatoriales-2026/P-40.pdf` | [index bulletin/enveloppe](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/sources/bulletin-nul-baron-mariani-2026-10-01.md) + photographies | COMPOSITE / AUTO-CORPUS / MANUEL-LOCAL | index disponible ; fichiers image primaires à localiser |
| P-41 | — | annexe presse | RÉSERVE | non prioritaire et non prévue dans le paquet initial ; ne réintégrer que par arbitrage explicite |
| P-43.a | `.filing-materials/senatoriales-2026/P-43.a.pdf` | Gmail `1a08ae5f35fd72f0` | AUTO-GMAIL / SENSIBLE | source vérifiée ; occultation des données non nécessaires |
| P-43.b | `.filing-materials/senatoriales-2026/P-43.b.pdf` | Gmail `1a0914a4db8cf48b` | AUTO-GMAIL / SENSIBLE | source vérifiée ; occultation des données non nécessaires |
| P-44 | `.filing-materials/senatoriales-2026/P-44.pdf` | [index France Transfert](https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/sources/france-transfert-ta-requetes-2026-09-11.md) + Gmail `1a0915c87f89b632` / `1a0915c86f65c427` | COMPOSITE / AUTO-GMAIL | deux messages vérifiés ; secrets techniques à occulter |
| P-45.a | `.filing-materials/senatoriales-2026/P-45.a.pdf` | Gmail `1a0dce31564ec625` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-45.b | `.filing-materials/senatoriales-2026/P-45.b.pdf` | Gmail `1a0e7c8da5ef2262` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-45.c | `.filing-materials/senatoriales-2026/P-45.c.pdf` | Gmail `1a0f65f52d19c6f7` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-45.d | `.filing-materials/senatoriales-2026/P-45.d.pdf` | Gmail `1a0fc64750fe95b6` | AUTO-GMAIL | source vérifiée ; PDF à produire |
| P-46 | `.filing-materials/senatoriales-2026/P-46.pdf` | 46 messages Gmail P-46.01 à P-46.46 | COMPOSITE / AUTO-GMAIL | **46/46 sources vérifiées** ; recueil PDF à générer avec occultations prévues |

## Cas P-45 — parent logique

P-45 regroupe P-45.a à P-45.d. Le contrat machine matérialise ces quatre sous-pièces séparément et **ne prévoit volontairement aucun `P-45.pdf` autonome**. Le contrôle de complétude doit donc considérer P-45 satisfait lorsque les quatre sous-pièces sont présentes et validées.

## Cas P-13 — vidéo

Le contrat `ubikia.filing-package.v0` accepte uniquement des entrées `markdown` et `pdf`. La vidéo P-13 ne peut donc pas être incorporée nativement au PDF final.

La représentation `P-13.pdf` doit au minimum contenir :

1. l'identification exacte du fichier vidéo ;
2. sa taille ;
3. son SHA-256 calculé sur le fichier natif ;
4. sa date/provenance ;
5. une transcription vérifiée ;
6. le mode matériel de remise de la vidéo native ou son emplacement dans le paquet électronique ;
7. si utilisé, un lien ou QR code stable qui ne remplace pas la remise de la pièce native.

Le PDF est une **fiche de représentation** ; il ne doit jamais être présenté comme la vidéo elle-même.

## Ordre de matérialisation

1. courriels simples sans pièce jointe ;
2. courriels + PDF/RTF joints ;
3. recueil P-46 ;
4. pièces Corpus facilement rendables ;
5. composites photo/scan ;
6. P-13 vidéo ;
7. contrôle terminal : pagination, occultations, SHA-256 et concordance avec le bordereau.
