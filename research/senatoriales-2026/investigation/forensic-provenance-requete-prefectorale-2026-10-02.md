---
title: "Sénatoriales 2026 — provenance numérique de la requête préfectorale"
date: "2026-10-02"
status: "working-note — forensic observation"
language: fr
document_role: "derived-analysis"
document_kind: "forensic-note"
visibility: "public"
lifecycle_state: "active"
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/investigation/forensic-provenance-requete-prefectorale-2026-10-02.md"
---

# Provenance numérique de la requête préfectorale — état au 2 octobre 2026

## Objet

Distinguer le **contenu lisible** de la requête préfectorale figurant dans le dossier communiqué par le Tribunal administratif de Bastia de l'**objet numérique natif** effectivement produit puis transmis par la préfecture.

## Constat borné

Les bundles PDF communiqués par le TA pour les dossiers n° 2601714 et 2601715 exposent des métadonnées de production correspondant à une recomposition ultérieure :

- producteur : `Aspose.PDF for .NET 21.2` ;
- date de création du bundle 2601714 : environ **18:43:03 CEST le 11 septembre 2026** ;
- date de création du bundle 2601715 : environ **18:40:03 CEST le 11 septembre 2026** ;
- le dossier juridictionnel indique une saisine enregistrée vers **18:16**.

Les pages correspondant à la requête préfectorale sont intégrées dans ces bundles sous forme d'images JPEG. La copie communiquée permet donc de lire le texte, mais n'expose pas à elle seule les métadonnées natives du fichier source préfectoral ni la totalité de sa provenance numérique.

## Ce que ce constat n'établit pas

Il n'établit pas :

- que le fichier source préfectoral n'existe plus ;
- que le Tribunal administratif aurait supprimé intentionnellement des métadonnées ;
- que la recomposition est irrégulière ;
- la date exacte de création du fichier natif préfectoral ;
- l'identité de l'auteur technique ou du validateur du fichier source ;
- l'heure exacte de son dépôt dans Télérecours.

## Question probatoire ouverte

La manière la plus directe de fermer cette inconnue consiste à obtenir :

1. le fichier électronique exact effectivement transmis par la préfecture ;
2. le fichier source ayant servi à le générer, s'il est distinct ;
3. le nom original du fichier ;
4. les empreintes et le procès-verbal numérique Télérecours ;
5. les accusés de dépôt/enregistrement ;
6. les traces de création, modification, validation et transmission disponibles.

Ces éléments ont été demandés dans le courriel P1–P18 envoyé le **2 octobre 2026 à 13:33:55 CEST**.

Source primaire de cette demande :
`research/senatoriales-2026/investigation/sources/courriel-tracabilite-prefecture-2026-10-02.md`.

## Règle épistémique

> Copie lisible ≠ objet numérique source ≠ preuve complète de provenance.

Le constat forensic est une **analyse dérivée**. La preuve primaire recherchée reste le fichier natif et ses traces de transmission.
