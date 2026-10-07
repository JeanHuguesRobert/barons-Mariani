---
title: "Incident d’accès temporaire au PDF canonique — requête Conseil constitutionnel Haute-Corse 2026"
description: "Chronologie technique et probatoire du bref incident de résolution/déploiement ayant affecté l’URL canonique du PDF le 7 octobre 2026 autour de 18 h."
author: "Jean Hugues Noël Robert"
date: "2026-10-07"
status: "documented-incident"
language: "fr"
license: "CC BY-SA 4.0"
document_role: "operational"
document_kind: "incident-trace"
visibility: "public"
lifecycle_state: "active"
related_case: "2026-6589 SEN"
canonical_pdf_url: "https://jhn.baronsmariani.org/cc/requete-conseil-constitutionnel-haute-corse-2026.pdf"
canonical_source_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/requete-conseil-constitutionnel.md"
---

# Incident d’accès temporaire au PDF canonique — 7 octobre 2026

## Objet

Cette note documente le bref incident ayant affecté l’URL publique du PDF de la requête contestant l’élection sénatoriale du 27 septembre 2026 en Haute-Corse.

Elle distingue explicitement :

1. l’existence du contenu source ;
2. la matérialisation de sa projection PDF ;
3. l’envoi des messages de saisine/transmission ;
4. la réception institutionnelle ;
5. le fonctionnement effectif du chemin HTTP public ;
6. l’acte technique de remédiation ;
7. la publication du nouveau déploiement ;
8. la vérification externe de son effectivité.

La requête a ensuite été officiellement enregistrée par le Conseil constitutionnel sous la référence **2026-6589 SEN**.

## Chronologie

| Heure CEST | Trace | Portée |
|---|---|---|
| 17:57:21 | commit Git `de70c4b82677711b7fd58fbd110026ba010b3e6e` | le correctif de routage du PDF est intégré au dépôt |
| 18:01:21 | sonde HTTP | l’URL publique sert encore le HTML du SPA ; le code correct n’est donc pas encore effectif sur la surface publique |
| 18:02:33.179 | log Supabase | activation de l’extension HTTP sous la migration `enable_http_for_emergency_netlify_deploy`, étape préparatoire explicite au déploiement d’urgence |
| 18:03:37.477 | API Netlify | création du build `6ac66d599949a6a4660df18a` |
| 18:03:49 | courriel du greffe du Conseil constitutionnel | le greffe signale : « Le lien communiqué ne fonctionne pas. » ; cette trace est externe au système de publication |
| 18:04:30.873 | API Netlify | publication du deploy `6ac66d599949a6a4660df18c` |
| 18:04:40.385 | API Netlify | dernier état enregistré `ready` |
| 18:05:05.882 | sonde HTTP externe | HTTP 200, `application/pdf`, PDF effectivement servi |
| 18:19:57 | notification du Conseil constitutionnel | la requête est déclarée reçue le 7 octobre 2026 et enregistrée sous `2026-6589 SEN` |
| 19:40:46 | réponse Gmail du requérant | accusé de réception et explication détaillée de l’incident envoyés dans le même fil au greffe |

## Fichier PDF vérifié

URL canonique :

https://jhn.baronsmariani.org/cc/requete-conseil-constitutionnel-haute-corse-2026.pdf

Lors de la vérification de 18:05:05.882 :

- HTTP : `200`
- type : `application/pdf`
- taille : `200935` octets
- SHA-256 : `2968cbe0a5de0f5e279e70d28c0769d4a8dbf8ca8f6f7e4571864333ecaa02a0`

## Source et projection

Le PDF est une projection dans un format raisonnablement portable du contenu source textuel versionné dans Git.

Source canonique :

https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/requete-conseil-constitutionnel.md

La distinction source / projection / chemin de consultation est essentielle : un incident de résolution HTTP sur la projection publique ne doit pas être confondu avec l’existence ou la provenance du contenu source.

## Lecture causale

La séquence permet de reconstruire quatre états distincts :

**INTENTION / CODE**
→ correctif intégré au dépôt ;

**ACTE**
→ mécanisme de déploiement d’urgence activé puis nouveau build créé ;

**MATÉRIALISATION**
→ nouveau deploy publié par Netlify ;

**EFFECTIVITÉ**
→ une sonde extérieure reçoit réellement le PDF.

Le message du greffe à 18:03:49 constitue une observation extérieure indépendante, située entre la création du build et la publication du deploy.

## Portée méthodologique — Traçabilité des Actes

Cet incident constitue un cas concret de la valeur de la Traçabilité des Actes.

Sans traces, il ne resterait qu’un récit approximatif : « le lien ne marchait pas puis il a été réparé ».

Avec les traces, il devient possible de distinguer et d’ordonner :

- l’état du code ;
- l’état du service réellement exposé ;
- l’acte de remédiation ;
- la création du build ;
- la publication ;
- l’état `ready` ;
- l’observation externe de l’effectivité ;
- l’observation indépendante d’un tiers institutionnel ;
- la réponse apportée à ce tiers.

Les traces ne démontrent pas seulement qu’un événement a eu lieu ; elles permettent de reconstruire **quel acte a provoqué quel changement observable**, avec des bornes temporelles vérifiables.

## Limite

Cette note documente un incident technique et sa résolution. Elle ne préjuge pas, à elle seule, de la qualification juridique de la saisine, de sa recevabilité ou des effets que le Conseil constitutionnel pourrait attacher à tel ou tel canal ou horodatage.
