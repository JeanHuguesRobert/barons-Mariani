---
title: "Suicide Corse — reçu de snapshot candidat au gel (édition 2026-09-17)"
author: Jean Hugues Noël Robert
status: working-paper
date: '2026-09-18'
document_role: operational
document_kind: snapshot-receipt
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
license: CC BY-SA 4.0
affiliation: Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica
language: fr
review:
  status: unreviewed
  reviewed_by: []
provenance:
  origin_type: generated
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: issue-75-closing-window
  origin_date: '2026-09-18'
  derived_from:
    - projects/suicide-corse/editions/snapshot-candidate-protocol.md
    - projects/suicide-corse/projections/book-2026-09-17-anniversaire.yml
    - https://github.com/JeanHuguesRobert/barons-Mariani/issues/75
---

# Reçu de snapshot candidat au gel — Édition 2026-09-17

Ce document établit le reçu technique et éditorial du **snapshot candidat au gel**
pour le numéro spécial anniversaire de *Suicide Corse*, conformément au
[protocole de snapshot candidat au gel](snapshot-candidate-protocol.md).

> [!IMPORTANT]
> **Ce reçu prépare un candidat au gel ; il ne constitue pas un gel définitif.**
> Le statut éditorial demeure `draft`. La décision d'un gel définitif relève
> exclusivement d'une décision éditoriale humaine distincte de l'auteur.

---

## 1. Horodatages et fenêtre de production

```text
observed_at        : 2026-09-18T01:45:00+02:00
closing_threshold  : 2026-09-18T07:05:11+02:00 (lever du soleil à Corte, Corsica)
edition_date       : 2026-09-17
production_window  : 2026-09-17T07:04:00+02:00 / 2026-09-18T07:05:11+02:00
rendered_at        : 2026-09-17T22:25:23.793Z
published_at       : 2026-09-17T22:48:37Z
deployed_at        : 2026-09-17T22:48:37Z
```

Le rendu, sa publication Git et sa mise à disposition sur la passerelle publique
sont tous intervenus à l'intérieur de la fenêtre de production conventionnelle
de l'édition du 17 septembre 2026.

---

## 2. Dépôts, sources et renderer

```text
source_repository  : JeanHuguesRobert/barons-Mariani
source_commit      : 81945d1c378cd2351688dec626f80385c2eac24c
source_dirty       : false
source_head        : 8d9c022f121707bc7223b93307e3246fe0aba428
renderer_repository: JeanHuguesRobert/ubikia
renderer_commit    : 58746e673b30c4aaa37c8dfbc088c52a43f9754f
renderer_version   : Quarto 1.10.18 + TinyTeX (rendu simultané HTML, PDF, EPUB)
publication_status : draft
```

*Note sur la source :* Les commits intervenus sur `barons-Mariani` entre le build
`81945d1` et le HEAD actuel (`3c5b4ff`, `f2e95d3`, `c5ae102`, `2c8def9`, `8d9c022`)
concernent les notes de recherche de témoins 2009-2016, le parcours artistique
2016-2022, le protocole d'édition et la documentation de l'intake privé de contributions
pour #80. Aucun chapitre du manuscrit (`00` à `17`) ni le contrat de projection
n'ont subi de modification textuelle depuis `81945d1`.

---

## 3. Empreintes cryptographiques des composants

### Contrat de projection
- **Fichier :** `projects/suicide-corse/projections/book-2026-09-17-anniversaire.yml`
- **SHA-256 :** `3ff76d8e1989e3f30d2f8aaab3543d306e18091a79e37a90f3f37c0a92e32fd7`
- **Statut de projection :** `preview-open` (18 chapitres : 00-ouverture à 17-appel-a-temoignages)

### Manifeste de build
- **Fichier :** `suicide-corse-site/editions/2026-09-17/manifest.json`
- **SHA-256 :** `8af2dc15755720b3aa0f2ac74a209c1fde8a573e1cd1eaf619587aad0fa7c5b9`
- **Taille :** 55 655 octets

### Artefacts rendus

| Format | Fichier | SHA-256 | Taille (octets) |
|---|---|---|---|
| **HTML** | `editions/2026-09-17/index.html` | `41ec94a5aa6ba456579000b4049fe69f31373b107bf09b6e18853eb6903d26f7` | 40 632 |
| **PDF** | `editions/2026-09-17/suicide-corse-edition-2026-09-17-anniversaire.pdf` | `2850a369b1d03790b79c9f2895f28af79e0c201f3afd7d73809c8c4578e296f4` | 269 036 |
| **EPUB** | `editions/2026-09-17/suicide-corse-edition-2026-09-17-anniversaire.epub` | `749961a858a7b3a1e5cf66721ff93bf8d805d012fc4551d6f1f43fb179035444` | 225 320 |

Tous les SHA-256 calculés sur les fichiers locaux coïncident strictement
avec les valeurs scellées dans `manifest.json`.

---

## 4. Dépôt d'artefacts et diffusion publique

```text
artifact_repository: JeanHuguesRobert/suicide-corse (clone local suicide-corse-site)
artifact_commit    : 261f459308ce2e578c41c42e6304df33741ef1ae
previous_release   : 76776e0ef6b4372a912bb09c693246a4805e3df0
Fracta2 origin     : /home/ubuntu/suicide-corse/editions/2026-09-17
Serving topology   : Passerelle TLS Fracta (Caddy) → maillage authentifié → origine statique Fracta2
```

### Vérification des points d'accès publics (HTTPS)

- `https://suicidecorse.baronsmariani.org/`
  - Statut : `HTTP/1.1 200 OK`
  - Type : `text/html`
- `https://suicidecorse.baronsmariani.org/editions/2026-09-17/index.html`
  - Statut : `HTTP/1.1 200 OK`
  - Type : `text/html; charset=utf-8`
  - Taille : 40 632 octets
- `https://suicidecorse.baronsmariani.org/editions/2026-09-17/suicide-corse-edition-2026-09-17-anniversaire.pdf`
  - Statut : `HTTP/1.1 200 OK`
  - Type : `application/pdf`
  - Taille : 269 036 octets
- `https://suicidecorse.baronsmariani.org/editions/2026-09-17/suicide-corse-edition-2026-09-17-anniversaire.epub`
  - Statut : `HTTP/1.1 200 OK`
  - Type : `application/epub+zip`
  - Taille : 225 320 octets
- `https://suicidecorse.baronsmariani.org/editions/2026-09-17/manifest.json`
  - Statut : `HTTP/1.1 200 OK`
  - Type : `application/json`
  - Taille : 55 655 octets

---

## 5. Réserves obligatoires

Le présent snapshot candidat répète expressément les limites suivantes :

1. **Statut d'ébauche :** `publication_status: draft` ne constitue en aucun cas
   un statut final ni une proclamation de version achevée ;
2. **Enquête et témoignages ouverts :** L'enquête documentaire et l'appel à
   témoignages restent ouverts ([`manuscript/17-appel-a-temoignages.md`](../manuscript/17-appel-a-temoignages.md)) ;
3. **Revue contradictoire indépendante :** La revue contradictoire par un tiers
   indépendant reste à réaliser (chantier ouvert répertorié au chapitre 16,
   *Continuations*) ;
4. **Statut des personnes identifiables :** Les personnes mentionnées dans les
   notes de recherche ou d'enquête sont des sources, témoins potentiels ou
   pistes d'instruction, et non des personnes mises en cause ;
5. **Canal de contribution :** Le canal email de contribution
   (`institutmariani@gmail.com`) est actif, mais ses messages ne sont ni
   publics ni automatiquement exploitables sans qualification probatoire ;
6. **Règle de post-clôture :** Toute correction substantielle postérieure à la
   clôture de la fenêtre (2026-09-18T07:05:11+02:00) devra obligatoirement être
   publiée sous forme d'une nouvelle projection datée ou d'un erratum traçable.

---

## 6. Référence de rollback opérationnel

Si un incident de diffusion exigeait un retour arrière opérationnel sans
altération de l'histoire éditoriale :
- Release de repli identifiée : `76776e0ef6b4372a912bb09c693246a4805e3df0`
  (sur le dépôt d'artefacts `suicide-corse`).

---

## 7. Décision ultérieure de gel

Un gel définitif exige une décision éditoriale humaine distincte par l'auteur,
après lecture du présent reçu candidat et de ses réserves. Cette décision ne
peut en aucun cas être déduite de l'existence d'un rendu, d'un commit Git,
d'un push ou de la disponibilité publique de la release.
